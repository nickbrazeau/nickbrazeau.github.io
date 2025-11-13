+++
# Research widget.
widget = "blank"  # See https://sourcethemes.com/academic/docs/page-builder/
headless = false  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 30  # Order that this section will appear in.

title = ""

# Choose the user profile to display
# This should be the username of a profile in your `content/authors/` folder.
# See https://sourcethemes.com/academic/docs/get-started/#introduce-yourself

[design.background]
  # Apply a background color, gradient, or image.
  #   Uncomment (by removing `#`) an option to apply it.
  #   Choose a light or dark text color by setting `text_color_light`.
  #   Any HTML color name or Hex value is valid.

  # Background color.
  # color = "navy"

  # Background gradient.
  # gradient_start = "DeepSkyBlue"
  # gradient_end = "SkyBlue"

  # Background image.
  #  image = "headers/tree.jpg"  # Name of image in `static/img/`.
  #  image_darken = 0  # Darken the image? Range 0-1 where 0 is transparent and 1 is opaque.

  # Text color (true=light or false=dark).
  text_color_light = false

[advanced]
 # Custom CSS.
 css_style = "research"
+++

<!-- Research section -->
<h1 style="text-align: center;">Research & Interests</h1>

_Below, I briefly summarize my research to date and elaborate on my interests and what I hope to continue to work on in the future. At the end of this page, you will find current and past projects._

&nbsp;
&nbsp;
&nbsp;
&nbsp;


<img align="left" width=45% height=200px padding="100" style="padding-top:15%; padding-bottom:15%; padding-right: 5%" src="/img/idmodel.png">


### Infectious Disease Modeling

My infectious disease modeling work spans statistical, spatial, evolutionary, and computational approaches. In one framework, I examined **who** became infected, **where** infections occurred, and the **origin** of pathogens in regions previously considered resilient to transmission. To evaluate *who* was at risk, I applied causal inference methods using inverse probability treatment weights generated through the SuperLearner ensemble. To determine *where* infections clustered, I used Bayesian Gaussian spatial process models. To assess *origin*, I generated and analyzed pathogen genetic data.

For research questions involving severity or burden estimation, I have implemented Bayesian statistical models and contributed to mathematical modeling for scenario planning. Most recently, I have explored how structural features of contact networks hinder pandemic prediction and evaluated AI/ML-driven agent-based models for improving forecasting.

Broadly, I am interested in the intersections of statistical modeling, infectious disease dynamics, machine learning/AI, and spatial analysis. I aim to use these tools to understand transmission and characterize antimicrobial resistance evolution and ultimately identify points where within-host and between-host propagation can be disrupted.

***

<img align="right" width="50%" height="300px" style="padding-top:20%; padding-bottom:15%; padding-left:5%" src="/img/phylo.png">

### Bioinformatics, Genomics, Statistical Genetics

Molecular surveillance and pathogen genomics critically inform infectious disease epidemiology and intervention planning. Much of my work focuses on antimicrobial resistance, especially putative antimalarial resistance. I have used genome-wide barcodes to study how antimalarial selection pressures shape *Plasmodium falciparum* population structure in the Democratic Republic of the Congo and performed whole-genome sequencing analyses to identify novel antimicrobial resistance mutations in *Staphylococcus epidermidis*.

I also develop statistical genetics methods, including:  
1. **Estimating local inbreeding** with [`DISCent`](https://github.com/nickbrazeau/discent), relevant for sink–source dynamics and public health intervention design.  
1. **Simulating malaria transmission dynamics** with [`polySimIBD`](https://github.com/nickbrazeau/polySimIBD) using a forwards in-time simulation with a spatial discrete-time, discrete-loci structured Wright Fisher model.
2. **Inferring identity-by-descent** in polyclonal malaria infections with [`HMMERTIME`](https://github.com/nickbrazeau/HMMERTIME).

<br>

***

<img align="left" width="40%" height="200px" style="padding-top:5%; padding-bottom:5%; padding-right:5%" src="/img/world.png">

### Global Health & Medicine, Translational Research

Global medicine has become local medicine— and vice versa. I am committed to supporting capacity building and collaborative research in low- and middle-income countries and historically underserved communities. My work aims to integrate computational, molecular, and clinical perspectives to improve infectious disease prevention, diagnosis, and treatment across diverse settings.

<br>

***
