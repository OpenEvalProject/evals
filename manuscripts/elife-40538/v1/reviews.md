# Peer review - Round 1

Editors:
- Jonathan Flint, University of California, Los Angeles United States

Reviewers:
- Greg Gibson, Georgia Tech United States

## Review text

DOI: [10.7554/eLife.40538.029](https://doi.org/10.7554/eLife.40538.029)

In the interests of transparency, eLife includes the editorial decision letter, peer reviews, and accompanying author responses.

[Editorial note: This article has been through an editorial process in which the authors decide how to respond to the issues raised during peer review. The Reviewing Editor's assessment is that all the issues have been addressed.]

Thank you for submitting your article "Genetic and environmental perturbations lead to regulatory decoherence" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Diethard Tautz as the Senior Editor. The following individual involved in review of your submission has agreed to reveal identity: Greg Gibson (Reviewer #1). The other reviewer remains anonymous.

The reviewers, and I, are convinced of the value of your approach (as one reviewer points out, this is long overdue). We do indeed have a limited understanding of the factors that shape correlations between genes and your work addresses this problem. In particular your observation that decoherent metabolites are good predictors is noteworthy, as is your successful identification of 'correlation-QTLs'. Though perhaps it is not surprising that the degree of correlation is under genetic control, it's certainly good to have that confirmed and analysed, as you have done here. Altogether, your paper represents an important advance.

I want to highlight one issue, to do with unacknowledged confounds. As one of the reviewers points out, the inclusion of expression data from multi-cellular tissues like blood is problematic, and I expected you might incorporate into your method one of the more recent analytical approaches to decompose the contributions (e.g. Nat Methods. 2017 Feb 28;14(3):218-219. doi: 10.1038/nmeth.4190). Would that improve the signal?

Separate reviews (please respond to each point):

Reviewer #1:

The manuscript on decoherence by Amanda Lee and colleagues presents a novel, and in my view long over-due, framework for considering decay of modularity of gene expression in disease conditions (among other applications). Alternative approaches describing statistical support for conservation of modules do not have resolution to individual transcripts or metabolites, so this approach holds considerable promise. I thought that the Introduction and Discussion sections were particularly insightful. I also applaud eLife for the experiment in "acceptance prior to review" and am happy to support this in this case. I hope that two more major sets of comments, followed by some minor ones, are helpful to the authors.

My first comment goes to the transparency of the description of CILP and its relationship to canalization. I think the way it is presented is overly complicated. If I am not mistaken, CILP is simply a t-test (or potentially ANOVA) of the Pearson correlation coefficients for all pairs of biomarkers in an analysis. The formula at the start of the Results section is that quantity, but then you say it is correlate with some random variable x. In actuality x is a fixed effect in all your comparisons, and it would be clearer to call it a test of association with x since it is the biomarkers that are being correlated. Furthermore, in Figure 3 you switch to the Spearman correlation, which I can see being appropriate, but is at odds with the rest of the description. Also to this point, canalization is commonly used in reference to increase in variance, which I can see could lead to de-coherence, but that is neither necessary nor sufficient, and this could be remarked upon.

My second comment has to do with the effect of unaccounted for factors on covariance. All transcriptomes and metabolomes have a high correlation structure, due to a combination of trans-acting influences, environmental influences, and mixtures of cell types. As far as I can see, the opening simulation study does not incorporate overall correlation, it only models pairwise effects due to cis-acting variation and correlation-QTL as defined by the authors. This should be acknowledged: it is extremely hard to model true transcriptional variation, but I suspect it makes a big difference. (Parenthetically, why call the cis effects b1 and b2, and the correlation effects b – another symbol for the latter would also be less confusing). Regarding the blood gene expression datasets, in the Materials and methods you consider the possibility that cell-type mixtures matter but don't find any influence of available cell counts. However, I can tell you from extensive experience that the major impact on whole blood gene expression in relation to BMI is reticulocyte count, which surprisingly is unrelated to RBC count, but if you fit Axis 2 from Preininger et al. (PMID: 23516379), renamed as Axis R in PMID: 29950172 and PMID: 30223463 and shown to strongly associate with BMI in PMID: 25300922 and PMID: 23162571 and countless other studies we've looked at, it is basically reticulocyte count. I certainly am not asking you to reference these studies (!) but do suggest you fit Axis 2 and see if it has an effect, because it is one of the major components of whole blood expression. I agree that the other Axes that correlate with B and T cell or Neutrophils only weakly associate with BMI.

Minor Comments:

Here are a few more minor comments:

Figure 2. Panel (C) described in the Legend has been removed from the version in the manuscript

LPS study: Need to reference the Fairfax et al. dataset, in the text (you don't do so until the Discussion). Also note that they describe a number of eQTL that have significantly different effects at BL, 2hr LPS, and 24hr LPS, some switching between the two exposure times. Do your correlation QTL tend to be the same, or overlap with, those instances?

Metabolic study. It is not clear from the text whether the results in Figure 3A to 3C are from t0 or from a combined analysis. I suspect just t0, please clarify. But I am also concerned that there may be inflation of the prediction of disease progression in Figure 3D due to use of the discovery dataset in the testing phase (winner's curse), especially if you used t1 and t3 in the discovery. (There will in any case be a bias due to correlations across times within individuals). I'd rather see a more robust analysis that uses a subset of the individuals and then predicts expression in the remainder – there should be sufficient sample size for this.

Subsection “Identification of disease-associated variation in metabolite correlation”, instead of stating the percentages of the subset of genes (74.4 and 25.6), state the percentages of all genes, it will still be 3:1.

Is there any indication that the transcripts that encode the enzymes that regulate the de-coherent metabolite sets are also de-coherent? I guess you may need data of both types from the same individuals, or from liver.

Regarding the correlation QTLs in NESDA, the first thing I think you should report is what fraction of them are also main effect cis-eQTL for one or the other transcript in each pair. Concerning RAP1GAP specifically, is it a trans-eQTL hotspot (I have some vague recollection that it may be, in blood). The enrichment statistics for its binding sites do not convince me at all: P<0.03 is a bit of a joke, and fibroblasts are not relevant, I don't think that result helps at all. Regarding the TF enrichment, I think you need to define what you mean by "involved in" since we now know that the locally regulated gene is usually not the closest one.

Finally, it would be interesting to know what happens to the expression in individuals who do not fall into the Healthy or MetS classes. Such ambiguous cases may have even more extreme de-coherence as they are transitional, at least at one of the time points. If the result is interesting it could be worth reporting.

Thanks for the opportunity to review such an interesting manuscript. Good luck with it.

Additional data files and statistical comments:

If the authors address some of the comments above, they will be addressing some rigor and reproducibility issues. I do not see a need for additional files.

Reviewer #2:

In this work, the authors start to investigate the potential for using the correlation between genes/metabolites as a distinct trait that may be parsable from the mean and variance of the same components. Overall, the approach seems solid albeit at points the strongest available support does not seem to be being used which does hinder the papers potential broad appeal. It is as if the need to write to clinical geneticists has slightly hamstrung the authors from really diving into the concepts that are actually very interesting and thought provoking. I have some specific questions and changes below.

On a general note, the paper is written in the general where this approach and its inferences are possibly of use in non-human systems. However, there isn't an obvious effort to discuss work in other systems, Drosophila, yeast, Arabidopsis, Maize, etc, that might influence the ideas and conclusions of this paper. There is similar work in these systems (See below) that touches on these topics and if the goal is really a broad audience they should be cited. If the goal is just a human audience than every term should be caveated by the word human, i.e. evolutionary genetics should be human evolutionary genetics, biology should be human biology, etc. Human Genetics can benefit from reading and acknowledging the work in other systems especially as Human Genetics greatly benefits from the of excellent young senior authors who come from other systems like Drosophila.

In the Introduction, the authors say "asking whether predefined sets of genes are differentially co-expressed between groups. Almost universally, these approaches are only designed for comparisons between two groups, and none can accommodate continuous predictor variables." Isn't that really only true of some approaches for the predefined set? There are groups that use the predefined sets in nested generalized models that can be extended to any complex experimental design and can include confounders and covariates. Maybe not in human genetics but at the very least in Drosophila and Arabidopsis. This should probably be tempered.

In the first section on permutation analysis (Table 1). Because of the lack of replication on individuals, VarQTLs in human genetics are a blend of all non-additive sources of variance, especially epistasis and stochasticity. Is there a difference in how epistatic variance or stochastic variance influences the claims made in this section? I ask because mechanistically it would be possible for stochastic variance to be more localized to the gene in question and not spread to other genes while epistatic variance could influence the whole network.

In the section on immunity, what was the reasoning behind limiting their analysis to the 1460 genes that were differentially expressed at the 2 hour time point? I would think that the power of the correlation approach would be that it could get more directly at the interaction term than limit itself to single timepoint selection. This choice should be explained. Especially as I wonder if this choice could create the appearance of decoherence as it does not allow for genes showing a difference at the other time points but not at 24 hours.

The RAP1GAP focus of the final section of the results has me slightly off-kilter. The authors argue for correlation being separable from other traits but then the key example is a gene with a large effect cis polymorphism. This could lead to a change in correlation by shifting genes from regulated by RAP1GAP when RAP1GAP is well expressed to no-correlation when there is low to no RAP1GAP simply because RAP1GAP is not functional. I agree that this is a real observation and does show some utility of their approach. But it would be very helpful to provide some insight of the approaches ability to get at the deeper questions that drive this manuscript. Like some examples of TF-Target correlations that were affected by trans polymorphisms. Or even metabolic gene-metabolic gene correlations that mapped to novel loci. This would help illuminate how much novel information this approach is finding.

I may be wrong but if the authors ideas about decoherence are true, shouldn't this predict that the slope in Figure 3B is less than 1? I.e. there is lower general metabolite to metabolite correlation in the y-axis (metabolic syndrome) than in the x-axis (healthy). As such, it seems that the most direct use of this data to support their conclusion would be to test if the slope is significantly lower than 1 as my interpretation of the model predicts. The rest of the information in this section seems superfluous to the idea it is trying to test.

As a small aside, there has been some work in Arabidopsis on how endogenous single gene mutants can or cannot change the correlational network in response to immune stresses similar to what is proposed in Figure 1A/B and Figure 2. These citations help to support the claim that correlation is a genetically separable trait [1,2]. I'm sure there are likely other similar citations in yeast and Drosophila.

1) Mine A, Seyfferth C, Kracher B, Berens ML, Becker D, Tsuda K: The Defense Phytohormone Signaling Network Enables Rapid, High-amplitude Transcriptional Reprogramming During Effector-Triggered Immunity. 2018.

2) Zhang W, Corwin JA, Copeland D, Feusier J, Eshbaugh R, Chen F, Atwell S, Kliebenstein DJ: Plastic transcriptomes stabilize immunity to pathogen diversity: The jasmonic acid and salicylic acid networks within the Arabidopsis/Botrytis pathosystem. Plant Cell 2017, online.
