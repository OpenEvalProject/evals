# Peer review - Round 1

Editors:
- Sara Mitri, University of Lausanne Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.88480.3.sa0](https://doi.org/10.7554/eLife.88480.3.sa0)

This manuscript introduces two valuable new metrics - "variant vulnerability" and "drug applicability" - that would be of use to identify candidate drugs for treating infections while considering longer-term, evolution-based treatment outcomes. Despite the intuitive appeal of the metrics and their potential, the study remains incomplete, as it fails to demonstrate the generality of the approach. The work could be improved by analysing a broader range of data in a systematic way and directly tying the metrics to outcomes, which would make it possible to better assess their impact and utility.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88480.3.sa1](https://doi.org/10.7554/eLife.88480.3.sa1)

The manuscript by Geurrero and colleagues introduces two new metrics that extend the concept of "druggability"- loosely speaking, the potential suitability of a particular drug, target, or drug-target interaction for pharmacological intervention-to collections of drugs and genetic variants. The study draws on previously measured growth rates across a combinatoriality complete mutational landscape involving 4 variants of the TEM-50 (beta lactamase) enzyme, which confers resistance to commonly used beta-lactam antibiotics. To quantify how growth rate - in this case, a proxy for evolutionary fitness - is distributed across allelic variants and drugs, they introduce two concepts: "variant vulnerability" and "drug applicability".

Variant vulnerability is the mean vulnerability (1-normalized growth rate) of a particular variant to a library of drugs, while drug applicability measures the mean across the collection of genetic variants for a given drug. The authors rank the drugs and variants according to these metrics. They show that the variant vulnerability of a particular mutant is uncorrelated with the vulnerability of its one-step neighbors, and analyze how higher-order combinations of single variants (SNPs) contribute to changes in growth rate in different drug environments.

The work addresses an interesting topic and underscores the need for evolution-based metrics to identify candidate pharmacological interventions for treating infections. The authors are clear about the limitations of their approach - they are not looking for immediate clinical applicability - and provide simple new measures of druggability that incorporate an evolutionary perspective, an important complement to the orthodoxy of aggressive, kill-now design principles.

As I said in my initial review, I think the work could be improved with additional analysis that tie the new metrics to evolutionary outcomes. Without this evidence, or some other type of empirical or theoretical support for the utility of these metrics, I am not fully convinced that these concepts have substantial impact. The new metrics could indeed be useful--and they have intuitive appeal--but the current revisions stop short of demonstrating that these intuitive notions hold up under "realistic" conditions (whether in simulation, theory, or experiment).


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88480.3.sa2](https://doi.org/10.7554/eLife.88480.3.sa2)

In the main text, the authors apply their metrics to a data set that was published by Mira et al. in 2015. The data consist of growth rate measurements for a combinatorially complete set of 16 genetic variants of the antibiotic resistance enzyme beta-lactamase across 10 drugs and drug combinations at 3 different drug concentrations, comprising a total of 30 different environmental conditions. In my previous report I had asked the authors to specify why they selected only 7 out of 30 environments for their analysis, with only one concentration for drug, but a clear explanation is still lacking. In the Data section of Material and Methods, the authors describe their criterion for data selection as follows: "we focus our analyses on drug treatments that had a significant negative effect on the growth of wildtype/TEM-1 strains". However, in Figure 2 it is seen that, even for the selected data sets, not all points are significant compared to wild type (grey points). So what criterion was actually applied?

In effect, for each chosen drug or drug combination, the authors choose the data set corresponding to the highest drug concentration. As a consequence, they cannot assess to what extent their metrics depend on drug concentration. This is a major concern, since Mira et al. concluded in their study that the differences between growth rate landscapes measured at different concentrations were comparable to the differences between drugs. I argued before that, if the new metrics display a significant dependence on drug concentration, this would considerably limit their usefulness. The authors challenge this, saying in their rebuttal that "no, that drug concentration would

be a major actor in the value of the metrics does not limit the utility of the metric. It is simply another variable that one can consider when computing the metrics." While this is true in principle, I don't think any practicing scientist would disagree with the statement that the existence of additional confounding factors (in particular if they are unknown) reduces the usefulness

of a quantitative metric.

As a consequence of the small number of variant-drug-combinations that are used, the conclusions that the authors draw from their analysis are mostly tentative. For example, on line 123 the authors write that the observation that

the treatment of highest drug applicability is a combination of two drugs "fits intuition". In the Discussion this statement is partly retracted with reference to the piperacillin/tazobactam-combination which has low drug applicability. Being based on only a handful of data points, both observations are essentially anecdotal and it is unclear what the reader is supposed to learn.

To assess the environment-dependent epistasis among the genetic mutations comprising the variants under study, the authors decompose the data of Mira et al. into epistatic interactions of different orders. This part of the analysis is incomplete in two ways. First, in their study, Mira et al. pointed out that a fairly large fraction of the fitness differences between variants that they measured were not statistically significant. This information has been removed in the depiction of the Mira et al. fitness landscapes in Figure 1 of the present manuscript, and it does not seem to be reflected in the results of the interaction analysis in Figure 4. Second, the interpretation of the coefficients obtained from the epistatic decomposition depends strongly on the formalism that is being used. In a note added on page 15 of the revised manuscript, the authors write that they have used the LASSO regression for their analysis and refer the reader to a previous publication (Guerrero et al. 2019) which however (as far as I could see) also does not fully explain how the method works. To give an example of the difficulty of interpreting the data in Figure 4 without further information: The substitution C (G238S) is well known to have a strong positive effective in cefotaxime, but the corresponding coefficient is essentially zero. So whatever the LASSO regression does, it cannot simply measure the effect on growth.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88480.3.sa3](https://doi.org/10.7554/eLife.88480.3.sa3)

The authors introduce two new concepts for antimicrobial resistance borrowed from pharmacology, "variant vulnerability" (how susceptible a particular resistance gene variant is across a class of drugs) and "drug applicability" (how useful a particular drug is against multiple allelic variants). They group both terms under an umbrella term "drugability". They demonstrate these features for an important class of antibiotics, the beta-lactams, and allelic variants of TEM-1 beta-lactamase. In the revised version, they investigate a second drug class that targets dihydrofolate reductase in Plasmodium (the causative agent of malaria).

The strength of the result is in its conceptual advance and that the concepts seem to work for beta-lactam resistance and DHFR inhibitors in a protozoan. However, I do not necessarily see the advance of lumping both terms under "drugability", as this adds an extra layer of complicaton in my opinion.

I think that the utility of the terms will be more comprehensively demonstrated by using examples across a breadth of drug classes classes and/or resistance genes. For instance, another good bacterial model with published data might have been trimethoprim resistance, which arises through point mutations in the folA gene (although, clinical resistance tends to be instead conferred by a suite of horizontally acquired dihydrofolate reductase genes, which are not so closely related as the TEM variants explored here).

The impact of the work on the field depends on a more comprehensive demonstration of the applicability of these new concepts to other drugs. This would be demonstrated in future work.
