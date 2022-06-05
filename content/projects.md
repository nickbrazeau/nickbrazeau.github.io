# Interests
* Evolutionary Medicine
* Internal Medicine
* Infectious Diseases
* Statistical Modeling
* Population Genetics
* Spatial Statistics
&nbsp;
## Projects
There is always more work to be done: no rest for the wreary! Here, I have listed my ongoing projects as well as topics that I am currently intrested in/learning more about. Additionally, at the end is a list of software packages at various stages of development.
### Ongoing Project Topics
* Signals of genetic relatedness through space
    + Identity by descent models
    + Spatial lattice models and fast kriging
* Intertwining spatial, causal inference, and compartment based models
    + Consilience of various ID statistical model approaches
* Capacity building in underserved communities
    + Mobile Health Clinic, Kanyawara, Uganda
### Lifelong learning
* Advanced Bayesian statistics
    + Better MCMC techniques
    + Better prior checks
    + Better modeling techniques
* Computational skills
        - Advanced Cpp
        - Core R
        - Intermediate python
## Available Software
Many thanks to Bob Verity, who has been a mentor and accomplice in all statistical programs/software design projects to date.

[DISCent](https://github.com/nickbrazeau/discent)  
**Description**: _To Be Released Shortly_
&nbsp;

[polysimIBD](https://github.com/nickbrazeau/polysimibd)  
**Description**: _To Be Released Shortly_
&nbsp;

[HMMERTIME](https://github.com/nickbrazeau/HMMERTIME)  
**Description**: _To Be Released Shortly_

[COVIDCurve](https://github.com/mrc-ide/COVIDCurve/)
**Description**: The purpose of this package is to provide a framework to fit age-specific infection fatality ratios (IFRs) in an epidemic that is using serologic data to estimate prevalence. The model was originally designed in response to the COVID-19 pandemic (hence the name) but is broadly applicable.
Accurate inference of the IFR based on serological data is challenging due to a number of factors that can bias estimates away from the true value, including: (1) the delay between infection and death, (2) the dynamical process of seroconversion and seroreversion, (3) potential differences in age-specific attack rates, and (4) serological test characteristics. These delay-distributions and serologic test characteristics are expected to cause both shifts in when deaths are observed as well as when and how many true infections are observed, which will then affect the IFR.
The model used in `COVIDCurve` can be briefly summarized as having two pieces: (1) an infection curve shape that is informed by the shape the of the observed death curve but "thrown"" backwards in time; (2) a pin or a point on the y-axis that the shape must go through (i.e. a pin to inform the area under the curve, or cumulative infections). This pin is informed by the observed serologic data, accounting for test characteristics (e.g. sensitivity and specificity) as well as the time from infection to seroconversion and seroreversion. Accounting for seroreversion, or the waning of antibodies over time that then produces a false negative test, becomes increasingly important as epidemics progress and/or as daily infections start to contract.
