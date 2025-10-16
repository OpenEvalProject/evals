# Peer review - Round 1

Editors:
- K VijayRaghavan, National Centre for Biological Sciences Tata Institute of Fundamental Research India

Reviewers:
- Hongyan Wang, Duke-NUS Medical School Singapore
- Sonia Sen, University of Oregon United States

## Review text

DOI: [10.7554/eLife.46566.041](https://doi.org/10.7554/eLife.46566.041)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Transcription factor Odd-paired regulates temporal identity in neural progenitors via an incoherent feed-forward loop" for consideration by eLife. Your article has been reviewed by three reviewers and the evaluation has been overseen by K VijayRaghavan as the Senior and Reviewing Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Hongyan Wang (Reviewer #1); Sonia Sen (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. This a very nice study with valuable conclusions. Congratulations.

Summary:

In the Drosophila brain, Type II neuroblasts (NBs) generate transit-amplifying lineages (INPs) that divide like Type I NBs to expand the neural population. Like the NBs, INPs too experience temporal patterning allowing them to generate different progeny over time. The temporal cascade in INPs consists of D>Grh>Ey and earlier work from this lab had uncovered the mechanism by which the cascade is initiated in INPs (via Osa activating D), and the mechanism by which the Grh>Ey temporal switch occurred (via Ham repressing Grh). However, much remains unknown in INP temporal patterning.

In this work, Abdusselamoglu et al., take a transcriptomic approach to this problem. They use FACS sorting to isolate the three temporally distinct INP populations followed by RNA-seq analysis to identify genes that are differentially expressed at these stages. To identify factors that ensure proper temporal switching in the INPs, the authors focus on Opa, which displays an RNA expression profile complementary to Ham. Using genetic manipulations and immunohistochemistry, they show that Opa is activated by Osa, and is responsible for repressing D (the first temporal factor in the INP). They also show neural fate specification effects that are consistent with this temporal progression.

Overall the data are of high quality, well documented and clearly presented. To my knowledge, this is the first time INP temporal patterning has been revisited since their first descriptions in 2013 and 2014, and so this manuscript advances our understanding in this field. This is particularly true due to the nature of the approach taken and the tools generated in the process.

Before we highlight the major concerns which can be speedily addressed, here are some specific points, appreciating the study, that a reviewer raised, which could be of value to the authors.

Some general comments which may be useful:

The differentially regulated genes in the temporal windows belong to different GO terms, which are difficult to make sense of, except for the presence of glial markers in the later Ey temporal window. This is of reduced importance.

However, the authors then focus on genes that regulate the transitions from one window to the next. The find that opa is a good candidate as a 'target' of Osa, a component of the SWI/SNF complex. Opa has an expression pattern that is anti-correlated with Hamlet. Interestingly, opa mutants appears to stop the progression of the temporal clock at D, and later windows do not open. The authors conclude that opa inhibits D and acts to promote the transition from D to Grh and correspondingly, leads to the accumulation of Bsh early neurons and the loss of late Eya neurons. But then how is opa controlled to inhibit D if both are osa targets?

The most interesting part of the paper deals with the answer to this question and presents a model that osa regulates both opa and Dichaete, but with very different kinetics: they propose that opa represses D, and thus allow the progression of the temporal cascade and the activation of Grh. This is where the authors introduce the notion of an incoherent feed-forward loop in which osa activates both opa and D, but then opa represses D, but only late as it is turned on later than D. This is an excellent motif to allow temporal progression (or circling).

The paper is very solid and makes robust conclusions, and the model that the timing of expression controls the efficiency of their incoherent FFL is well supported and consistent with the data.

Therefore, the work adds one important detail to the concept that temporal windows progress through time. They show that a circuit motif allows the efficient progression of the cascade. Even if opa is not a temporal factor, it plays an important role in the transitions. We believe that this is an important result.

A concern though is the role of osa, which controls everything while it is a chromatin complex that is recruited by transcription factors: what these TFs are, remains a mystery although their identification would be a major breakthrough.

Essential revisions:

1) When expressing D-GFP, Ey-GFP and Grh-GFP for FACS sorting, are they expressed under their endogenous level to avoid overexpression effect? The D-GFP was described in the methods and appeared to be based on CRISPR/Cas9- mediated gene editing. If this is true, please indicate it clearly. There is no description or citation for the generation of Ey-GFP and Grh-GFP.

2) In FACS-purified GrH+ INPs (Figure 2F), the expression Ey is also high. What is the reason for this contamination? Does it mean that many INPs have co-expression of Grh and Ey at the same time?

3) The reason for choosing to focus on Opa is unclear. The expression of Ham in D+, GrH+ and Ey+ INPs are similar, only fluctuating slightly. Therefore, the expression pattern of Ham doesn't seem to be a good example of dynamic expression in INPs. Can the authors clearly indicate how many genes have dynamic expression patterns in INPs and what criteria, i.e. based on fold changes, is applied to rank and select Opa? Currently, it appeared to be hand-picked.

4) Is asymmetric division of INPs impaired and resulting in the change of INPs numbers upon loss-of-opa or opa overexpression?

5) We appreciate the excellent quality of the FACS sorting of the three temporally distinct INP populations and are very impressed with how cleanly the authors were able to isolate the 3 populations, and how well they have documented it! This makes the RNA-seq data particularly invaluable to the field.

6) With respect to Opa and its place in the temporal transitions, we are largely in agreement with the authors and their interpretations. They propose a model where Opa represses D and suggest that Opa also activates Grh. However, in their subsequent interpretations they seem to consider Opa's repression of D as its main mechanism of action in temporal progression. Would not Opa's activation of Grh, leading indirectly to repression of D, tie in all the data from this and the Byaraktar and Eroglu papers better? It would explain why D+, Opa+ double positive INPs are seen at all, why D-/- INPs can still progress through the temporal cascade, and why overexpressing Opa resulted in loss of D+ INPs and increase in GrH+, Ey+ INPs (incomplete expression of Grh in UAS-Opa shown in Figure 5 might be due to presence of Ham). Furthermore, it would not call upon differential levels of expression of Opa (which the authors have not shown at the protein level), as timing of expression/inhibition of these genes as the INP divides might account for the temporal transitions.

7) If the authors agree with this, have they looked at the DM1 lineage, which is known to not express Grh? Is Opa expressed in this lineage? If not, does misexpression of Opa there result in Grh activation and D repression? The authors have analysed this in DM2 and DM3 – the same brains could be analysed for DM1.

8) The authors must have verified the Opa:V5 tool before using it. Could they please describe this?

9) The authors show that D comes up in INPs before Opa does. However, this is not very clear from the images. Could the authors maybe show magnified insets of these types INPs with the two reporters co-localised? Am I right in understanding that apart from this one difference, Opa is co-localised with every other temporal factor in the INPs? Related to this, the authors find that Opa RNA levels are high early and late in the lineage, and dip in the middle. Do the protein levels reflect these dynamics? Their discussion seems to suggest it does.
