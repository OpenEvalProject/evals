# Peer review - Round 1

Editors:
- Daniel J Kliebenstein, University of California, Davis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.40655.034](https://doi.org/10.7554/eLife.40655.034)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Identification and characterisation of epigenetic loci controlling transgenerational immune priming in Arabidopsis" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Christian Hardtke as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This work utilizes a collection of epiRILs to show that there is potential epigenetic variation in controlling defense responses.

Essential revisions:

After discussion, there were considered two essential components that need addressing to make the manuscript publishable in eLife.

First, it was felt that the work is highly interesting in itself but that at a number of locations, claims were made that were not supported by the data at best and occasionally contradictory information was available in other papers. As such, it was agreed that the authors should use the guidance in the reviews to rewrite the manuscript to more precisely focus on what has and has not been shown in this manuscript and others.

Second, we all agreed that the Hi-C was a potentially interesting idea but that the claims were unsupported. To support the claims would require doing Hi-C in the specific epiRILs or drop it from the manuscript at this point in time.

Reviewer #1:

– If they were just honest about what they found, it would be a really nice paper and I would support it for eLife. But their claims are simply unjustified by their analysis.

The authors map epiQTLs that link to resistance to Hpa, then assess potential epigenetic influences on transcripts and how this may be priming. Finally, the authors look for chromatin interactions in WT/ddm1 and use them to argue that this is the mechanism. The data itself is very nice. but I find that the claims are not justified based on the conducted analysis. The experiments and data themselves will be very useful but the authors would need to focus on what they do show. To illustrate, they nicely map resistance epiQTLs and do some really nice transcriptomics. Just presenting that as plainly as what they found would be interesting.

In contrast, the writing makes extensive claims about priming, transgenerational and chromatin interactions. The transgenerational argument is trying to link in with the work showing that there is one-generation of disease effects on resistance. However, there is no analysis of if their loci really play any role in this phenomena. They just have loci whose ddm1 marks lead to altered resistance. They would have to show that these same loci influence the transgenerational resistance phenomena to make their arguments.

The chromatin interactions are all done in ddm1 v. WT and not in the epiRILs v. WT or v. ddm1 so I'm not sure they can actually make their claims. Wouldn't they need to look at interactions in the epiRILs to make any of these arguments.

Priming concerns –

I should caveat the following in that I have some quant/eco/evo training in my background so I go by a very strict definition of priming; a pre-treatment leads to an elevated response to a secondary treatment that cannot be explained by any effect of the pre-treatment. Similar to the definition I work off of for epistasis. The effect of A x B is not explainable by adding up the effect of A and B separately.

Given this definition, the transcriptomics analysis does not make a direct test of priming. The authors use pairwise analysis which do not allow for a statistical testing of priming directly. To claim priming would require re-analyzing the data with a linear model where Transcript = genotype + treatment + genotype x treatment. And only the transcripts with a significant genotype x treatment term would fit into what might be called priming. Priming is the interaction term rather than the main effect of genotype or treatment.

This concern about what is or is not priming, arises from their own data that argues against priming even when they say it argues for priming. If you notice in Figure 2B, the PCA plot actually shows that the main transcript variance in the epiRILs are not priming but mainly constitutive changes as the change from Mock to Hpa infected is a similar level of variance in each genotype. If it was truly a predominantly priming effect, the uninduced would all be similar to the WT uninduced. Figure 2—figure supplement 2A also shows my worry about priming. If you look at the plots for what a primed transcript looks like, only 2 of those five plots would truly fit what is priming.

The authors argue that priming is the sole thing altered and that other defense traits aren't influenced. There are a couple of potential issues with this exclusionary arguments. The use of the 8 most resistance epiRIL lines to test other interactions is not really evidence of much. There isn't enough statistical power to say anything other than they aren't exactly 100% the same traits. It is possible that there is still a correlation. Additionally, at least one if not two of their loci are linked to variation in defense metabolism in this population based on previous work looking at epigenetic variation in defense metabolites within population. This shows that there are defense traits that are altered in these lines prior to infection. This previous work should be cited and incorporated appropriately when discussing the authors results as it contradicts the central claim about exclusivity of effects.

Reviewer #2:

This study uses the ddm1 epiRIL population to identify QTL controlling resistance to. At least four epiQTL are identified which contribute >50% of the heritable variation. To explore these epiQTL further, transcriptome and methylome analyses were performed. These experiments revealed that four of the epiRIL lines with the highest resistance display a heightened transcriptome response to Hpa indicating these lines are already primed. This enhanced priming explains why the lines are not suffering a growth defect as there is not a constitutive response to Hpa or other a/biotic stresses. To understand how the priming of Hpa induced genes occurs the DNA methylome data were integrated, which generally revealed that the loci within the QTL regions were not directly affected by loss of DNA methylation and that perhaps there is a genome-wide trans affect occurring in these lines due to the global loss of DNA methylation. To provide a mechanistic explanation for how this could occur the authors hypothesize that long range chromatin interactions could be in play. To test this, Hi-C data from WT and ddm1 was analyzed to revealed the existence of long range chromatin interaction between the QTL and the affected defence genes.

Overall, this is an interesting study, especially with the identification of epiRILs that are resistant to Hpa seemingly with no growth defects. However, the causal basis for these phenotypes requires additional evidence. The use of Hi-C is innovative, but it does not prove the strong statement made in the subsection “DDM1-dependent chromatin interactions between the resistance epiQTLs and distant defence genes as a potential trans-priming mechanism”, in the Abstract and in the Discussion.

1) Throughout the manuscript there are references to phrases that do not make sense. What are "epigenetic loci" as stated in the title or "epigenetic resistance". I would refer to these as "loci" and "resistance". Furthermore, why is "transgenerational" invoked throughout the paper? QTL are stably inherited. There are no transgenerational experiments presented in this study. Please remove this phrase from the study unless referring to the literature.

2) There is a potentially interesting observation of a trans effect being causal for the resistance, but this has not been proven as stated in the Abstract and the paper.

3) The epiQTL span regions associated with 4 out of 5 pericentromeric regions indicating that overall depletion of DNA methylation and potentially loss of heterochromatin is associated with Hpa resistance. What is the association between the amount of ddm1 like chromosomes within the epiRILs and the resistance phenotype. Essentially, if you remade Figure 1 to show the amount of Col vs. ddm1 chromosome would it correlate with the observed resistance phenotype?

4) Why was ddm1 not included in the transcriptome study upon Hpa infection? This would be useful to understand if it is stronger than the epiQTL, which seems to be a prediction based on the discussion.

5) The data presented to support a "tight correlation" between hypomethylation and gene expression in Figure 3B needs additional support. While it is expected that loss of methylation and transposon genes could result in their reactivation, this is not as likely to occur at genes given that most genes are unmethylated, a small percent are gene body methylation (which is causally linked to expression) and rare genes show transposon-like methylation profiles. This can be resolved by splitting out the genes into unmethylated, gene body methylation (CG) and TE-like methylation (CG, CHG and CHH). Although some of these genes are cis-regulated by DNA methylation, it does not look like they all are as stated. This could be further tested using a scatter plot between change in DNA methylation versus change in expression.

6) There is no data provided to support the statement that "their transcriptional profile is determined by their associated TEs." Please rephrase this as a hypothesis.

7) The use of Hi-C data is an interesting idea. It is stated that "43 interactions between the epiQTLs…" were reduced or intensified in ddm1 vs. wt. Yet, there is no statistical support to indicate whether this represents an enrichment over background expectations. This is a critical test as this forms the mechanistic basis for how the trans interactions occur.

Reviewer #3:

I think this paper is likely to be of broad interest. The demonstration that demethylation of particular bits of the genome affects a particular phenotype, in this case immunity, is intriguing. The authors have made a serious effort to understand why, and have made substantial progress in that direction. They have demonstrated increased effectiveness of callose, a known factor in resistance to this pathogen, and they have shown increased expression of genes known to be induced in response to infection. They make use of a new technology, Hi-C, and obtain data suggesting that the altered methylation may have long distance effects on expression levels of genes associated with immunity, possibly explaining the resistance phenotype. I found this rather unexpected, as conventional wisdom is that in the small genome of Arabidopsis, control of gene expression is nearly always very local. This work suggests that may not be correct, and a wider view is needed.

The authors were faced with the considerable challenge of working out how the epiQTLs affect expression of immmunity-related genes. In the last experiment, they use Hi-C and find connections between the epiQTL DNA and certain infection-inducible genes outside the QTL regions. Moreover, those genes are up-regulated in the resistant epiRILs carrying the epiQTL alleles. This is temptingly close to showing a mechanism. However, more statistical analysis is needed to make this convincing. A large number of infection-inducible genes are up-regulated in the resistant epi-RILs. Is the fraction of these detected in the Hi-C experiment as being linked to the QTL loci greater than would be expected by chance?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Identification and characterisation of hypomethylated DNA loci controlling quantitative resistance in Arabidopsis" for further consideration at eLife. Your revised article has been favorably evaluated by Christian Hardtke as the Senior Editor, and three reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below. There are just a few requests for clarification in terminology and the like that will help to raise the readability and visibility of the manuscript.

Reviewer #1:

The authors have largely responded to my previous concerns. One thing that I think might help this version of the manuscript is to simplify the Discussion and definitions surrounding augmentation and priming. I found myself getting confused about what was being meant. It would help to have discrete explicit definitions being given to allow the reader to fully understand what the authors mean.

Reviewer #2:

The authors have made significant improvements to this study.

Reviewer #3:

This revised version of the manuscript addresses all of my concerns. I agree with the decision to leave out the Hi-C data. The inclusion of additional experiments has strengthened the work. The conclusions are now more conservative.
