# Peer review - Round 1

Editors:
- George H Perry, Pennsylvania State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.99210.3.sa0](https://doi.org/10.7554/eLife.99210.3.sa0)

It is known from model organisms that genes' effects on traits are often modulated by environmental variables, but similar gene-by-environment (GxE) interactions have been difficult to detect using statistical analyses of genomic data, e.g., in humans. This study introduces a new framework to estimate gene-by-environment effects, treating it as a bias-variance tradeoff problem. The authors convincingly show that greater statistical power can be achieved in detecting GxE if an underlying model of polygenic GxE is assumed. This polygenic amplification model is a truly novel view with fundamental promise for the detection of GxE in genomic datasets, especially with continued development to detect more complex signals of amplification.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99210.3.sa1](https://doi.org/10.7554/eLife.99210.3.sa1)

Experiments in model organisms have revealed that the effects of genes on heritable traits are often mediated by environmental factors -- so-called gene-by-environment (or GxE) interactions. In human genetics, however, where indirect statistical approaches must be taken to detect GxE, limited evidence has been found for pervasive GxE interactions. The present manuscript argues that the failure of statistical methods to detect GxE may be due to how GxE is modelled (or not modelled) by these methods.

The authors show, via re-analysis of an existing dataset in Drosophila, that a polygenic 'amplification' model can parsimoniously explain patterns of differential genetic effects across environments. (Work from the same lab had previously shown that the amplification model is consistent with differential genetic effects across the sexes for a number of traits in humans.) The parsimony of the amplification model allows for powerful detection of GxE in scenarios in which it pertains, as the authors show via simulation.

Before the authors consider polygenic models of GxE, however, they present a very clear analysis of a related question around GxE: When one wants to estimate the effect of an individual allele in a particular environment, when is it better to stratify one's sample by environment (reducing sample size, and therefore increasing the variance of the estimator) versus using the entire sample (including individuals not in the environment of interest, and therefore biasing the estimator away from the true effect specific to the environment of interest)? Intuitively, the sample-size cost of stratification is worth paying if true allelic effects differ substantially between the environment of interest and other environments (i.e., GxE interactions are large), but not worth paying if effects are similar across environments. The authors quantify this trade-off in a way that is both mathematically precise and conveys the above intuition very clearly. They argue on its basis that, when allelic effects are small (as in highly polygenic traits), single-locus tests for GxE may be substantially underpowered.

The paper is an important further demonstration of the plausibility of the amplification model of GxE, which, given its parsimony, holds substantial promise for the detection and characterization of GxE in genomic datasets. However, the empirical and simulation examples considered in the paper (and previous work from the same lab) are somewhat "best-case" scenarios for the amplification model, with only two environments and with these environments amplifying equally the effects of only a single set of genes. It would be an important step forward to demonstrate the possibility of detecting amplification in more complex scenarios, with multiple environments each differentially modulating the effects of multiple sets of genes. This could be achieved via simulations similar to those presented in the current manuscript.

Comments on revisions:

The authors have (with reasonable justification) said that my main recommendations for strengthening the conclusions of the paper are beyond its scope, and they have thoughtfully responded to my (and the other reviewer's) other comments. The paper is now more clearly written---in particular, the connection between the single-locus bias-variance tradeoff calculations and the polygenic results is much more transparent than before. Given that the authors have (again, with fair justification) chosen not to address my major comment, my broad assessment of the paper is unchanged---I think it is an important contribution to a critical topic---and I have no further comments for its improvement (though I note an issue with figure referencing in the captions of Supplementary Figs S2 and S3).
