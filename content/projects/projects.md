+++
# A Projects section created with the Portfolio widget.
widget = "portfolio"
headless = true
active = true
weight = 20

title = "Projects"
subtitle = ""

[content]
  page_type = "project"

  filter_default = 0

  [[content.filter_button]]
    name = "All"
    tag = "*"

  [[content.filter_button]]
    name = "Active"
    tag = "active"

  [[content.filter_button]]
    name = "R Packages"
    tag = "rpackage"

  [[content.filter_button]]
    name = "Malaria"
    tag = "malaria"

  [[content.filter_button]]
    name = "COVID-19"
    tag = "covid"

  [[content.filter_button]]
    name = "Antimicrobial Resistance"
    tag = "AMR"

  [[content.filter_button]]
   name = "Other Projects"
   tag = "other"

[design]
  columns = "1"
  view = 3
  flip_alt_rows = false

[design.background]

[advanced]
 css_style = ""
 css_class = ""
+++
