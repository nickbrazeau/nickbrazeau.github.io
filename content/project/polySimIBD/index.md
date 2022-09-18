---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "polySimIBD"
summary: "Spatial Structured Wright Fisher Model for Malaria Population Genetic Simulations"
authors: []
tags: [rpackage, malaria, active]
categories: [r]
date: 2020-04-30T08:00:20-07:00


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
  url: https://github.com/nickbrazeau/polySimIBD
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

The goal of polySimIBD is to perform forwards in-time simulation of malaria population genetics. The model uses a discrete-time, discrete-loci structured Wright Fisher approximation to account for (simplified) malaria transmission dynamics and can be parameterized across demes to include a spatial component.

The model was originally used in Verity & Aydemir & Brazeau _et al._ 2020 in Nature Communications[^1] to assess the bias in our identity by descent calculation.

[^1]: Verity R, Aydemir O, Brazeau NF, Watson OJ, Hathaway NJ, Mwandagalirwa MK, Marsh PW, Thwai K, Fulton T, Denton M, Morgan AP, Parr JB, Tumwebaze PK, Conrad M, Rosenthal PJ, Ishengoma DS, Ngondi J, Gutman J, Mulenga M, Norris DE, Moss WJ, Mensah BA, Myers-Hansen JL, Ghansah A, Tshefu AK, Ghani AC, Meshnick SR, Bailey JA, Juliano JJ. The impact of antimalarial resistance on the genetic structure of Plasmodium falciparum in the DRC. Nat Commun. 2020 Apr 30;11(1):2107. doi: 10.1038/s41467-020-15779-8. PMID: 32355199; PMCID: PMC7192906.
