# Peer review - Round 1

Editors:
- Naama Barkai, Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.51002.sa1](https://doi.org/10.7554/eLife.51002.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Kuchen et al. have developed a general model that can explain the high degree of intra-generational correlation in cell cycle times that have been observed in multiple systems. Based on insight provided by this general model, they show that these correlations can arise from a unidirectional coupling of cell size and cell-cycle speed by a minimal cell-size checkpoint, which they verify using perturbation experiments.

Decision letter after peer review:

Thank you for submitting your article "Hidden long-range memories of growth and cycle speed correlate cell cycles in lineage trees" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Naama Barkai as the Senior and Reviewing Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Kuchen et al. have developed an interesting and general model that can explain the high degree of intra-generational correlation in cell cycle times that have been observed in multiple systems. First, using Bayesian inference on their own time-lapse data, they find that a model of two unidirectionally coupled heritable components that affect cell-cycle time best explains their data. They go on to propose that these components can be cell size and cell-cycle speed, provided that growth and division are coupled via a minimum size checkpoint. They then verify this model through perturbation experiments.

Essential Revisions:

Please address all comments below.

In particular please pay a special attention to the following two points:

1) The concerns over reproducibility between datasets,

2) Provide much clearer explanation of the unbiased model-selection.

Reviewer #1:

The paper studies division time correlations within neuroblastoma cells through time-lapse microscopy. Their approach uses unbiased statistical models to infer a minimal model that they claim recapitulates the experimentally observed correlations within populations of cells based on a set of heritable factors influencing interdivision times. The authors then study a model of division times based on growth to a threshold size and the inheritance of cell cycle progression factors that determine the rate of passage through the cell cycle. The authors claim that this second model recapitulates WT data in addition to matching the correlations observed in cells either grown with rapamycin (to limit cell growth) or cells with a reduced rate of passage through the cell cycle obtained by restricting the expression of the oncogene MYCN.

I found their unbiased statistical approach of particular interest since they considered a range of hierarchical models and used a metric for evaluating them which accounts for potential effects of overfitting with larger numbers of fitting parameters. However, to interpret this section with a critical eye requires more intuition for the metric of discrimination between these hierarchical models. In particular, Equation 12 which appears to address this should be referenced and discussed in the main text. With regards to the rest of the paper, the predictions of the authors when varying the limitations of either growth or cell cycle progression were unclear. This would be greatly aided by giving the reader intuition about what one would expect for either "pure" model (either a pure sizer for size control or cells which are completely limited by cell cycle progression).

Additionally, the following main comments should be addressed:

1) How are the fitting parameters re-evaluated when inhibiting growth or cell cycle progression relative to the control case?

2) Why do the authors switch to logistic growth during the MYCN growth? This is currently not even mentioned in the main text. It is concerning that in order to fit the MYCN growth case this fundamental assumption needed to be altered.

3) Is the agreement between the model predictions and the observed division time correlations robust to variations in the cell size control strategies assumed? There is increasing evidence that many mammalian cells follow an "adder" model (see for example Cadart et al., 2018 which is incorrectly referred to in the paper as supporting a critical size), so testing the model for this size control strategy would be an important test of the proposed model.

4) The choice of cell cycle timing as a feature of interest was not adequately justified. The results would be stronger if the authors can use data on correlations in cell size between relatives to test Model V and its predictions.

5) The explanation of the results shown in Figure 4 does not provide clear intuition for why the correlations should be altered in the observed fashion. It would be helpful if the authors took more care when explaining this. For example: The authors show in Figure 3E that growth-limited cells have negative mother-daughter correlations in cell cycle timing. This being the case, why is it that the mother-daughter correlations in the presence of rapamycin (Figure 4D) are in fact larger than those correlations measured in the MYCN treated cells?

Reviewer #2:

In the present manuscript, Kuchen and colleagues investigate how regulation of cell cycle progression and cell growth are coupled using analysis of extended cell lineages and mathematical modeling. Initially, they performed time-resolved live-cell microscopy of a MYCN – over-expressing neuroblastoma line to generate cell lineage trees spanning 5-7 generations. As previously reported, they observed higher intra-generational than ancestral correlations, which has so far been attributed to coupling between cell cycle and circadian clock (Sandler et al., 2015, Chakrabarti et al., 2018). The authors now took an unbiased approached based on a Gaussian latent variables and propose a model where two unidirectionally coupled variables are inherited to daughter cells. They mechanistically implement these two variables as cell growth and cell-cycle progression and show that it is sufficient to couple both through a minimal-size checkpoint to account for the observed correlation patterns in lineage trees. This model is supported by experimental perturbations of cell growth (via mTOR inhibition) and cell cycle progression (decreasing MYCN levels) as well as by analysis of existing lineage data from rapidly cycling human ES cells.

The paper is well written and easy to follow. The authors present a very plausible alternative explanations for the non-intuitive correlation patterns in lineage trees and provide further evidence for a size checkpoint in mammalian cell cycle regulation. As the focus of the manuscript is on the use of abstracted mathematical models to explain a complex cellular phenotype (inheritance of cell cycle length), there is little mechanistic/molecular inside regarding the details of the observed phenomena (e.g. minimal cell size checkpoint). However, the provided experimental validation provides strong support for the presented hypothesis. As an experimentalist, I would have liked to see additional orthogonal perturbations to further strengthen the data, but believe that this would be beyond the scope of this study.

Main points:

1) While the modelling results match the data within the estimated error bounds, the correlation patterns seem to be less pronounced. For example, the increased correlation to first cousins compared to aunts in Figure 3C (and Figure 3—figure supplement 1D) is hardly reproduced in the model. Similarly, the correlations to the removed side-branch seem to be about equal for all generations in the model, while the data indicates increased intra-generational correlations. It would be helpful if the authors comment on and explain such deviations or limitations of the model.

2) As a main assumption of the authors is that MYCN over-expression disrupts the circadian clock which has been previously linked to the inheritance patterns of cell cycle length, they should validate this in the cell line used. This could be done for example by quantifying BMAL1 expression in the presence/absence of doxycycline (see Figure 4—figure supplement 1A.

Reviewer #3:

Kuchen et al. have developed an interesting and general model that can explain the high degree of intra-generational correlation in cell cycle times that have been observed in multiple systems. First, using Bayesian inference on their own time-lapse data, they find that a model of two unidirectionally coupled heritable components that affect cell-cycle time best explains their data. They go on to propose that these components can be cell size and cell-cycle speed, provided that growth and division are coupled via a minimum size checkpoint. They then verify this model through perturbation experiments. Although the paper appears to be of general interest to eLife readers, there are several points that require clarification before publication.

1) Representation of data. The authors present 3 repeats of the time-lapse microscopy for neuroblastoma TET21N cell lineages. (Figure 1E). For the Bayesian analysis (Figure 2) they only show the different models plotted against Repeat 1 in the main and supplemental figures (which appears to be the bottom dataset of Figure 1E – it would be helpful if the different repeats were labelled in this figure). However, there appears to be significant differences between the 3 repeats shown in Figure 1E. Although it is difficult to see (in part because the horizontal line across each axis is at a different value of the Cross correlation coefficient – how was this value selected?) it appears that in repeats 2 and 3 the level of correlation in distant side branches is much lower (around 0). This appears particularly worrying given the results of the Bayesian analysis for Model VII (Figure 2—figure supplement 1). Although this model results in no correlation past first cousins, it gives the best fit to data for repeat 2 and 3 (better in fact than model 5, Figure 2—figure supplement 1), and only fails to reproduce replicate 1. This suggests that for 2 out of 3 datasets a model that assumes no correlations past first cousins is being selected as the best model from the Bayesian analysis. The authors should address this issue, and show plots of the Bayesian analysis against all 3 repeats.

In the rest of the figures, which dataset chosen is not consistent. Although they do display a fit of their growth/progression model to repeat 1 and 2 in the Figure 3—figure supplement 1, they now chose repeat 3 to display in Figure 3 – which appears to be the best fit to the model. In Figure 4, panel C shows cell-cycle lengths for repeat 3, but it is not clear which repeat(s) is/are used in the calculation of the correlation ratios. It would be helpful if the authors were consistent with their data selection in the main figures and supplements throughout the paper.

2) Experimental evidence for cell size/cell cycle checkpoint model. The authors relate latent variables x1 and x2 to cell size and the cycling of cell cycle factors respectively. However, since these quantities are not dynamically tracked throughout cell growth, I have some questions about the authors' interpretation and model. First, the model assumes the existence of a size threshold. If size does not affect cell cycle progression (another assumption), that suggests small-born cells are under a sizer-type control, whereas large-born cells (progression limited) are under a timer-type control. Such a model seems difficult to square with ongoing work in other organisms, which typically find adder-type (many single-cell microbes but also a number of mammalian cell lines, cf. Cadart et al., 2018) or sizer-type (e.g. fission yeast) control. Could the authors comment on how their model is biologically justified and how does it relate to alternative models of cell growth? Timer control is usually not considered because, on its own, it does not generate stable cell size. Indeed, in the appendix the authors note that, in the progression-limited regime, their model generates cells that are too large, so they implemented logistic, rather than exponential growth. In my understanding, this effectively implements a sizer again. What evidence do the authors have for these assumptions?

On the other hand, in subsection “Effects ofmolecular perturbations on cell-cycle correlations correctly predicted by the model” the authors claim that the growth of MYCN-inhibited cells is not affected. How did the authors verify this? If growth is logistic, as in the model, then growth rate is clearly affected beyond a certain size. Naively, I would also expect slower growth rates if growth is exponential and cell size is homeostatic. Additionally, the effects on cell size due to the addition of rapamycin appears weak (Figure 4B) – Is it possible to quantify this difference, with an estimation of errors?
