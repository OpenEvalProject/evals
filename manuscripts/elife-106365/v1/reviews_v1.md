# Peer review - Round 1

Editors:
- Anne-Florence Bitbol, Ecole Polytechnique Federale de Lausanne (EPFL) Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.106365.3.sa0](https://doi.org/10.7554/eLife.106365.3.sa0)

This manuscript introduces a useful protein-stability-based fitness model for simulating protein evolution and unifying non-neutral models of molecular evolution with phylogenetic models. The model is applied to five viral proteins that are of structural and functional importance. While the general modelling approach is solid, and effectively preserves folding stability, the evidence for the model's predictive power remains limited, since it shows little improvement over neutral models in predicting protein evolution. The work should be of interest to researchers developing theoretical models of molecular evolution.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.106365.3.sa1](https://doi.org/10.7554/eLife.106365.3.sa1)

Summary:

Ferreiro et al. present a method to simulate protein sequence evolution under a birth-death model where sequence evolution is guided by structural constraints on protein stability. The authors then use this model to explore the predictability of sequence evolution in several viral proteins. In principle, this work is of great interest to molecular evolution and phylodynamics, which has struggled to couple non-neutral models of sequence evolution to phylodynamic models like birth-death processes. Unfortunately, though, the model shows little improvement over neutral models in predicting protein sequence evolution, although it can predict protein stability better than models assuming neutral evolution. It appears that more work is needed to determine exactly what aspects of protein sequence evolution are predictable under such non-neutral phylogenetic models.

Major concerns:

(1) The authors have clarified the mapping between birth-death model parameters and fitness, but how fitness is modeled still appears somewhat problematic. The authors assume the death rate = 1 - birth rate. So a variant with a birth rate b = 1 would have a death rate d = 0 and so would be immortal and never die, which does not seem plausible. Also I'm not sure that this would "allow a constant global (birth-death) rate" as stated in line 172, as selection would still act to increase the population mean growth rate r = b - d. It seems more reasonable to assume that protein stability affects only either the birth or death rate and assume the other rate is constant, as in the Neher 2014 model.

(2) It is difficult to evaluate the predictive performance of protein sequence evolution. This is in part due to the fact that performance is compared in terms of percent divergence, which is difficult to compare across viral proteins and datasets. Some protein sequences would be expected to diverge more because they are evolving over longer time scales, under higher substitution rates or under weaker purifying selection. It might therefore help to normalize the divergence between predicted and observed sequences by the expected or empirically observed amount of divergence seen over the timescale of prediction.

(3) Predictability may also vary significantly across different sites in a protein. For example, mutations at many sites may have little impact on structural stability (in which case we would expect poor predictive performance) while even conservative changes at other sites may disrupt folding. I therefore feel that there remains much work to be done here in terms of figuring out where and when sequence evolution might be predictable under these types of models, and when sequence evolution might just be fundamentally unpredictable due to the high entropy of sequence space.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.106365.3.sa2](https://doi.org/10.7554/eLife.106365.3.sa2)

In this study, the authors aim to forecast the evolution of viral proteins by simulating sequence changes under a constraint of folding stability. The central idea is that proteins must retain a certain level of structural stability (quantified by folding free energy, ΔG) to remain functional, and that this constraint can shape and restrict the space of viable evolutionary trajectories. The authors integrate a birth-death population model with a structurally constrained substitution (SCS) model and apply this simulation framework to several viral proteins from HIV-1, SARS-CoV-2, and influenza.

The motivation to incorporate biophysical constraints into evolutionary models is scientifically sound, and the general approach aligns with a growing interest in bridging molecular evolution and structural biology. The authors focus on proteins where immune pressure is limited and stability is likely to be a dominant constraint, which is conceptually appropriate. The method generates sequence variants that preserve folding stability, suggesting that stability-based filtering may capture certain evolutionary patterns.

However, the study does not substantiate its central claim of forecasting. The model does not predict future sequences with measurable accuracy, nor does it reproduce observed evolutionary paths. Validation is limited to endpoint comparisons in a few datasets. While KL divergence is used to compare amino acid distributions, this analysis is only applied to a single protein (HIV-1 MA), and there is no assessment of mutation-level predictive accuracy or quantification of how well simulated sequences recapitulate real evolutionary paths. No comparison is made to real intermediate variants available from extensive viral sequencing datasets which gather thousands of sequences with detailed collection date annotation (SARS-CoV-2, Influenza, RSV).

The selection of proteins is narrow and the rationale for including or excluding specific proteins is not clearly justified.

The analyzed datasets are also under-characterized: we are not given insight into how variable the sequences are or how surprising the simulated sequences might be relative to natural diversity. Furthermore, the use of consensus sequences to represent timepoints is problematic, particularly in the context of viral evolution, where divergent subclades often coexist - a consensus sequence may not accurately reflect the underlying population structure.

The fitness function used in the main simulations is based on absolute ΔG and rewards increased stability without testing whether real evolutionary trajectories tend to maintain, increase, or reduce folding stability over time for the particular systems (proteins) that are studied. While a variant of the model does attempt to center selection around empirical ΔG values, this more biologically plausible version is underutilized and not well validated.

Ultimately, the model constrains sequence evolution to stability-compatible trajectories but does not forecast which of these trajectories are likely to occur. It is better understood as a filter of biophysically plausible outcomes than as a predictive tool. The distinction between constraint-based plausibility and sequence-level forecasting should be made clearer. Despite these limitations, the work may be of interest to researchers developing simulation frameworks or exploring the role of protein stability in viral evolution, and it raises interesting questions about how biophysical constraints shape sequence space over time.
