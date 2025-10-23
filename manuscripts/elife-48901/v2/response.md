# Author response - Round 1

Authors:
- Thea Hogan
- Maria Nowicka
- Daniel Cownden
- Claire F Pearson
- Andrew J Yates ([ORCID: 0000-0003-4606-4483](https://orcid.org/0000-0003-4606-4483))
- Benedict Seddon ([ORCID: 0000-0003-4352-3373](https://orcid.org/0000-0003-4352-3373))

## Response text

DOI: [10.7554/eLife.48901.sa2](https://doi.org/10.7554/eLife.48901.sa2)

Essential revisions:

1) The main question is regarding the modeling approach. We appreciate that the authors have tested three different models and chosen the best one. But all the models are linear, and so to achieve the balance observed between source, fast and slow cells requires fine tuning of the dynamical parameters. The question is whether it would make more biological sense to have some kind of feedback or density-dependent mechanism. Although we don't think you have to "invent a more complex model" when the simpler one works well, this could at least be a point of discussion.

This is a nice point. We considered it but concluded that a treatment of feedback regulation of cell numbers will not be informative here, for three reasons;

1) The memory cell numbers we observe from age 10 weeks onwards only vary by factor of 2 or 3; the average pool sizes in clean and dirty mice differ by a similar factor (Figure 1B); and we don’t find significant differences in the average net loss rates of each subset in the two environments (Figure 4B and Table 2). Without larger perturbations to cell numbers, then, we do not expect to be able to identify any density dependence of the net loss rates with our data. For the two-compartment model, we are also already at the limit of the number of parameters we are comfortable attempting to estimate.

2) None of the models require fine-tuning to achieve stability. Numbers are simply the balance of slowly declining influx from the naive pool (constant force of recruitment * naive numbers, which decline naturally); and first order decay from one or more sequential compartments. So in these models all memory (sub)compartments can achieve a stable steady state without feedback regulation.

3) Arguably there is little experimental evidence for homeostatic regulation of memory numbers, at least in SPF mice — we see three levels of stable memory in the three facilities, memory pools appears not to fill up rapidly with large clones in very young mice; and memory cell numbers are expandable following multiple infections in older animals (Vezys, Yates et al. Nature 2009).

We have added a discussion of these points.

2) Another question is that the authors model central and effector memory cells independently. Could these two cell populations be coupled, for example, through interconversion? How would this affect the modeling approach? And more importantly, could it affect the conclusions?

In response to other comments we revisited the data with some alternative models (thank you for suggesting this) and in the process improved our descriptor functions for the sources and our strategy for parameter estimation; detailed in Materials and methods. As a result we now clearly favour a naive – CM – EM pathway.

We reached this conclusion by fitting naive -> CM and CM -> EM separately. We were not able to fit all three simultaneously – the number of parameters was too large, and given that we find heterogeneity within both pools there is some uncertainty in how to connect the two models. Even with a constant rate of conversion, solving two coupled models where survival changes continuously with cell age is technically beyond us. Also – since there may be an expansion factor between CM and EM, the two are only coupled weakly as regards fitting.

We did model a Naive-EM-CM pathway but the fits are extremely poor (see Author response image 1). Indeed we argue that such a pathway is inconsistent with the timecourses of chimerism in the two pools. So we choose not to include these fits.

The model underestimates the accumulation of CM donor chimerism, as it is constrained by the lower chimerism of the upstream EM cells.
