---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "`DISCent`: Spatial Inbreeding Estimation"
summary: "An algorithm for detecting deme inbreeding spatial coefficients from recombining pathogen genetic data"
authors: []
tags: [rpackage, malaria, active]
categories: [r]
date: 2022-03-09T08:00:20-07:00


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: "Center"
  preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
links:
- name: GitHub
  url: https://github.com/nickbrazeau/discent
  icon_pack: fab
  icon: github

url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---

This is a simple package with a single function that runs a simple isolation by distance and identity by descent model for producing deme inbreeding spatial coefficients (DISCs). By theory, genetic relatnedness is strictly limited to measure of identity by descent. For a full mathematical overview of the simple model, please see the supplements from Brazeau et al. 2022 in in preperation[^1].

Briefly, in the early 1970s, Malécot described a relationship between genetic relatedness and physical distance under the premise that pairs that are far apart are less likely to mate: isolation by distance. Capitalizing on this framework by using measures of identity by descent (IBD), we produce a deme inbreeding spatial coefficient (DISC) for point process data in continuous space. Essentially, this measure estimates the amount of "inbreeding" or within deme relatedness under the assumption that relatedness between two locations in space can be measured from the average pairwise IBD between those two locations conditional on the physical distance that separates them. Further, we assume that geographic distance is scaled by a migration rate, which is a global parameter among all spatial locations (i.e. the migration rate is assumed to be constant through space). As a result, the model produces a DISC for each spatial location considered (user defined) and an overall migration rate parameter (m). Parameter optimization is achieved with a "vanilla" gradient descent algorithm. Given that "vanilla" gradient descent is used, we recommend running numerous models from a wide of array of start parameters to ensure that your final results are the global maximum and not a local maximum (i.e. a false peak).

[^1]: Nicholas F Brazeau, _in preparation_.
