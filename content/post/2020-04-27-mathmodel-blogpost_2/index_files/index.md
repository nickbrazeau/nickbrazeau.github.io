---
author: Nick Brazeau
title: Stochastic Simulations for Flattening the Curve Playground
date: 2020-04-27
tags:
  - simulation
categories:
  - R
---

Below, you will find code for creating a shiny flex-dashboard for performing simple stochastic simulations with one time-interruption corresponding to an intervention (unrealistically simulated all at once). Code relies on the excellent EpiModel R package.



```
   ---
  title: "Stochastic Simulations for Flattening the Curve"
  date: "`r format(Sys.time(), '%B %d, %Y')`"
  editor_options:
    chunk_output_type: console
  output: flexdashboard::flex_dashboard
  runtime: shiny
  ---


  {r setup, include=FALSE}
  knitr::opts_chunk$set(echo = F, warning = F, message = F, fig.align = 'center', results = 'hide', fig.keep = 'all')
  library(tidyverse)
  library(EpiModel)
  library(furrr)
  # https://rmarkdown.rstudio.com/flexdashboard/layouts.html#multiple_pages



  ### Sidebar {.sidebar}

  {r, results='asis'}
  #..............................................................
  # Sliding Panel for Different Parameters we are estimating
  #..............................................................

  inputPanel(
    sliderInput("ntime", label = "Time of Intervention",
                min = 0, max = 200, value = 100, step = 10),

    sliderInput("obstime", label = "Epidemic Time-Span",
                min = 0, max = 300, value = 200, step = 50),

    sliderInput("inf.prob", label = "Unmitigated Prob. of Infxn",
                min = 0, max = 1, value = 0.5, step = 0.05),

    sliderInput("act.rate", label = "Unmitigated Prob. of Contact",
                min = 0, max = 1, value = 0.5, step = 0.05),

    sliderInput("newinf.prob", label = "Mitigated Prob. of Infxn",
                min = 0, max = 1, value = 0.25, step = 0.05),

    sliderInput("newact.rate", label = "Mitigated Prob. of Contact",
                min = 0, max = 1, value = 0.25, step = 0.05),

    actionLink("button", "Ruh Roh!", icon("bug"),
               style="color: #fff; background-color: #337ab7; border-color: #2e6da4")

  )






 ### Stochastic Interventions

  {r, results='asis', fig.align='center', fig.height=11, fig.width=8}

  renderPlot({ withProgress(message = 'Making plot', {
    # re-render button
    input$button

    # make unmitigated model
    param <- param.icm(inf.prob = input$inf.prob, act.rate = input$act.rate, rec.rate = 0.01)
    init <- init.icm(s.num = 1e3, i.num = 1, r.num = 0)
    control <- control.icm(type = "SIR", nsims = 20, nsteps = input$ntime)
    mod.unmit <- icm(param, init, control)

    # cheap way to have an intervention
    unmitdat <- as.data.frame(mod.unmit)
    new_init <- unmitdat %>%
      dplyr::filter(time == input$ntime) %>%
      dplyr::select(c("s.num", "i.num", "r.num")) %>%
      dplyr::mutate(endtime = input$obstime - input$ntime,
                    newinf.prob = input$newinf.prob,
                    newact.rate = input$newact.rate)

    wrap_icm <- function(newinf.prob, newact.rate, s.num, i.num, r.num, endtime){
      newparam <- param.icm(inf.prob = newinf.prob, act.rate = newact.rate, rec.rate = 0.01)
      newinit <- init.icm(s.num = as.numeric(s.num),
                          i.num = as.numeric(i.num),
                          r.num = as.numeric(r.num)) # as.numeric for stupid corner case
      newcontrol <- control.icm(type = "SIR", nsims = 1, nsteps = as.numeric(endtime))
      # out
      mod <- icm(newparam, newinit, newcontrol)
      return(mod)
    }

    # mitigation
    mit.icm <- furrr::future_pmap(new_init, wrap_icm)
    mitdat <- lapply(mit.icm, function(x){ret <- as.data.frame(x); ret[, colnames(ret) != "sim"]} )
    mitdat <- mitdat %>%
      dplyr::bind_rows(., .id = "sim")  %>%
      dplyr::mutate(time = input$ntime + time)


    fulldat <- rbind.data.frame(unmitdat, mitdat)
    df.mean <- fulldat %>%
      dplyr::group_by(time) %>%
      dplyr::summarise(
        s.num = mean(s.num),
        i.num = mean(i.num),
        r.num = mean(r.num),
      )
    # plot
    ggplot() +
      geom_line(data = fulldat, mapping = aes(time, s.num, group = sim), alpha = 0.25,
                lwd = 0.5, color = "#238b45") +
      geom_line(data = df.mean, mapping = aes(time, s.num), color = "#238b45", lwd = 1.2) +
      geom_line(data = fulldat, mapping = aes(time, i.num, group = sim), alpha = 0.25,
                lwd = 0.55, color = "#cb181d") +
      geom_line(data = df.mean, mapping = aes(time, i.num), color = "#cb181d", lwd = 1.2) +
      geom_line(data = fulldat, mapping = aes(time, r.num, group = sim), alpha = 0.25,
                lwd = 0.55, color = "#54278f") +
      geom_line(data = df.mean, mapping = aes(time, r.num), color = "#54278f", lwd = 1.2) +
      geom_vline(data = fulldat, aes(xintercept = input$ntime), color = "#000000", linetype = "dashed", size = 1.5, alpha = 0.8) +
      xlab("Time") + ylab("Num.") + ggtitle("Stochastic SIR Model Runs with Intervention (Black)") +
      theme_minimal() +
      theme(
        plot.title = element_text(family = "Helvetica", face = "bold", vjust = 0.5,  hjust = 0.5, size = 22),
        axis.title = element_text(family = "Helvetica", face = "bold", hjust = 0.5, vjust = 0.5, size = 18),
        axis.text = element_text(family = "Helvetica", hjust = 0.5, vjust = 0.5, size = 17),
        panel.background = element_rect(fill = "transparent"),
        plot.background = element_rect(fill = "transparent"),
        axis.line = element_line(color = "#000000", size = 1.2),
        legend.position = "none")

  }) # end of progress bar
  })
```
