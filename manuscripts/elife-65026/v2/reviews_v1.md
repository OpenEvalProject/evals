# Peer review - Round 1

Editors:
- Jan Gruber, Yale-NUS College Singapore

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65026.sa1](https://doi.org/10.7554/eLife.65026.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Global, cell non-autonomous gene regulation drives individual lifespan among isogenic C. elegans" for consideration by eLife. Your article has been reviewed by a Senior Editor, a Reviewing Editor, and three reviewers. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

The reviewers agreed that the question posed is an important one and that some of the data presented is interesting. However, in the reviews and during the subsequent discussions, there was also a general consensus that several of the major claims about the causal structure of the ageing process and about the cell non-autonomous nature of the effects are not sufficiently supported in the current version of the manuscript. The reviewers suggested several additional experiments and controls that might be employed to address these limitations. However, given the COVID-19 situation, we appreciate that it may not be possible to carry out these additional experiments in a timely manner. Unfortunately, without substantial additional evidence, these claims would have to be removed or substantially weakened, necessitating changes that would go beyond major revisions.

The reviewers suggested that, should you decide to carry out the additional experiments and address these concerns in the future, you may consider re-submitting the manuscript as a new submission to eLife.

Reviewer #1:

This manuscript presents a very interesting study of the stochastic nature of aging. It has long been known that identical clones have varying lifespans as can be seen from every "control" lifespan curve published. The authors use a very innovative approach of tracking the expression of GFP marking miRNAs in individual worms to see if they are predictive of lifespan. The findings are equally striking as ~half of miRNAs correlate with lifespan.

The major issue with this manuscript is the way that it is written. The main result is striking, but the writing takes the reader into detailed descriptions of the statistical methods, counterfactuals and nearly philosophical discussions. The Results section needs to be cut. The Discussion needs to be cut. The authors should consider moving some of the text to the Materials and methods section.

I do not believe further experiments are needed.

Reviewer #2:

Kisner et al., present a thoughtful and carefully executed study of a panel of in vivo GFP-promoter fusion constructs that they deploy to dissect the causal structure of lifespan-determining processes in C. elegans. The authors focus on inter-individual differences within isogenic populations. They consider the covariation structure among their GFP reporters and lifespan and cleverly argue that inter-individual differences in lifespan are driven largely (but not completely) by some upstream factor shared among the various gene regulatory elements governing microRNA expression. Because these gene regulatory elements act in separate tissues and at different times in life, the authors conclude that there is, minimally, a hierarchical structure among lifespan-determining processes and, perhaps, that the lifespan of their animals was determined by a single organism-wide, cell-non-autonomous process. This seems like an important contribution as it articulates a precise question: what is this lifespan-determining process? The authors exclude one obvious answer-DAF-16 activity -and leave a compelling puzzle ripe for future study.

By employing bespoke quantitative approaches for GFP reporter and extensive manual validation, the authors decouple image processing quirks from their downstream statistical analyses. This is satisfying and likely contributes to the agreement between their measurements and the limited previously published results on the subject.

Much of the reasoning in this paper depends on comparisons between small correlations and r-squared values. In such contexts where "effect sizes" are small relative to the "noise", statistical analyses must be performed and interpreted with great care. The authors do this well, but they may have overlooked the potential for truncation effects to be driving some of the observed correlation between reporter measurements and lifespan. If present, truncation effects could potentially confound the major conclusions of the manuscript. The authors should address this concern (described in Major Point #1) with additional statistical analysis that rule out the possibility for truncation effects influencing their conclusions, or, if possible, by performing orthogonal experiments that support the same conclusions in a different way.

1) For each microRNA, the authors identify a time interval (shared among all individuals) during which they calculate the mean and change in pixel intensity data. To identify predictors of lifespan, they then regress these means and slopes against individual lifespan. If no deaths occurred during the time interval chosen, this would be a relatively straightforward calculation, as there would be no relationship between death time and the number of measurements used to calculate pixel intensity averages. However, the authors use time intervals that do include deaths, which means that short-lived animals will necessarily have fewer measurements available during the interval compared to longer-lived animals. This introduces a potential confounding effect that in principle could make time-dependent processes completely unrelated to lifespan appear like biomarkers.

Perhaps with similar concerns in mind, the authors state that they restrict the time intervals used for each reporter to a maximum upper bound of 90% survival. In Figure 2A, 90% survival appears to correspond to 8 days post-hatch. An upper bound at 90% of survival would reduce the effect of truncations but not eliminate them. Yet, the authors do not appear to follow their stated limitation, as in Table 2 the time windows appear to extend out to 10 days at which point 50% of individuals have died. This opens the possibility that truncation effects could underlie a substantial fraction of the reporter / lifespan correlations reported. Worse, because the death of an individual will necessarily truncate all reporters simultaneously, truncation effects could additionally contribute to the overlap in the predictive powers observed between multiple reporters.

2) The authors present two opposing models regarding the source of inter-individual differences: exogenous factors acting differentially between individuals throughout life and exogenous factors that establish stable inter-individual differences early in life. The contrast between stable changes early and continuous changes seems reasonable-but why must inter-individual different arise solely from exogenous factors? It would seem that the authors conceptual and analytic framework would describe equally well extrinsic and intrinsic factors (including spontaneous differences arising during development, or random stochastic fluctuations in gene regulatory networks occurring throughout life).

Reviewer #3:

In this paper, Holly Kinser, Matthew Mosley, Isaac Plutzer, and Zachary Pincus set out to identify biomarkers of aging in C. elegans. The questions they set out to answer are important to understanding the causal structure of the aging process. C. elegans is a great system to address these questions in a multicellular setting. The authors use a powerful imaging platform that the lab developed that enables them to image fluorescent reporters in individual worms throughout their lifespan. They focus on a set of micro RNA expression reporter fusions and identify several reporters with age-dependent changes in expression that correlate with remaining lifespan. For a subset of these reporters that they identify as strong predictors of life expectancy they find that these predictions remain in mutants of daf-16/FOXO, an important effector of the insulin singling pathway. The authors then examine whether multiple markers provide additional information about life expectancy and find that they do not. Overall, my impression is that these findings are interesting, but more work would be needed to ascertain the robustness and generality of these reporter predictions. In addition, some the central claims of the paper need better support.

1) How robust are these findings? The authors only use one transgenic line for each reporter. Additional lines of evidence are needed to determine if these findings are robust. This is important because, in principle, their findings could be dependent on the position in the genome where the transgene was integrated. That is, are the regulatory sequences in the transgenes sufficient to produce the age dependent expression patterns and correlations with life expectancy? Or could regulatory regions near the site of integration be necessary or sufficient for that regulation?

2) The authors take advantage of many existing reporter constructs fusing regulatory regions of micro RNA genes to GFP. They do not provide sufficient information about how these key tools were built. What are the promoter sequences used? Did the GFP reporter have introns? Which 5' UTR was used in each case? What coinjection marker was used in each case? Where the transgenes single copy or multicopy? Where the lines outcrossed? This is important because it is possible that the age-dependent regulation they observe could be due to factors other than the promoter sequences. For example, the unc-54 3' UTR is well known to drive gene expression in the posterior intestine, and introns in GFP stabilize the mRNA.

3) The authors make several claims that need better support. They claim that age-dependent predictors are "independent of insulin signaling". But they only look at the dependency for one effector of this pathway, DAF-16, when there is extensive literature going back decades showing that SKN-1/NRF, HSF-1/HSF, and many other transcription factors also act downstream of the DAF-2 receptor (and independently of DAF-16) in the regulation of lifespan. Could those effectors of insulin signaling be involved?

4) The authors claim in the title that "Global, cell non-autonomous gene regulation drives individual lifespan." Yet this set of claims is one of many models that can explain their findings. Issues with these specific claims:

4.1) Gene regulation: What is the evidence that transcriptional changes cause differences in lifespan? The authors say in the results that all their models share a "mutual transcriptional relationship with a single lifespan-determining process." Does that process need to be transcriptional just because it also affects expression of the GFP reporters?

4.2) Cell non-autonomous: I am not sure what the rationale for this claim is. Why couldn't there be a set of cell autonomous killing processes in the different tissues where the separate predictors of lifespan are expressed? This would be similar to links in a chain, the chain breaks when the weakest link breaks, but links break independently (autonomously). What would the authors have expected to turn out differently if the lifespan determining process acted cell autonomously?

5) The authors claim in the Abstract that they "demonstrate a hierarchy among several transgenes expressed in distinct tissues" that report on a single lifespan determining process. Could the transgenes with non-additive lifespan predicting capacity just have overlapping independent (ie non-hierarchical) transcriptional determinants? (that is could they share regulatory elements that each report on an independent lifespan determinant?)
