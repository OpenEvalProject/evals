# Peer review - Round 1

Reviewers:
- Randy Schekman, Howard Hughes Medical Institute, University of California, Berkeley , United States

## Review text

DOI: [10.7554/eLife.13053.030](https://doi.org/10.7554/eLife.13053.030)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Synthetic protein interactions reveal a functional map of the cell" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Randy Schekman as the Senior and Reviewing Editor.

The following individuals involved in review of your submission have agreed to reveal their identity: Stanley Fields and Nevan Krogan (peer reviewers).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors present a screen using their newly developed SPI system, which allows for the creation of artificial interactions between pairs of proteins. They create binary interactions between each of the ~6,000 yeast proteins and 23 target proteins that represent the major cellular compartments. The effects of these interactions on growth are assayed by measuring colony sizes. In spite of these interactions often leading to protein relocalization, they find only a small fraction lead to a measurable growth phenotype, suggesting that the cells are tolerant of both protein movement and association. The authors highlight how their method can be used to discover new regulatory relationships and to provide structural information on large cellular complexes.

The SPI system provides an exciting complement to PPIs and genetic interactions, and the scale of the collected dataset is impressive. The manuscript is well written and for the most part the methods are clearly described. Together, the importance and quality of the work makes it suited for publication in eLife as a tool/resource. However, there are a number of important points that need to be addressed.

Essential revisions:

1) The analysis on a limited number (24) of GFP-fusion proteins suggests that for only roughly ~20% of time when they co-express a GFP-fusion query protein with a target protein do they see mislocalization of the GFP fusion outside of where it is normally found. But even this may be a large over estimation of the degree to which their system is causing protein mislocalization. First, they do not evaluate what fraction of the GFP-fusion is mislocalized. Second, cleavage of the GFP from the fusion protein will result in mislocalization of the GFP domain but not of the rest of the protein. Finally, they report on ~6000 individual GFP fusion proteins obtained from the library developed in Huh et al. (2003). But in that paper only ~4500 of the fusion proteins were validated and observable. Thus unless the remaining 1500 strains were made and validated separately, they are suspect. In the end because of these and other concerns, I think it is not possible evaluate from these data what fraction of the proteins tolerate being effectively mislocalized to a cellular location that is different from where it is naturally found. This limitation must be discussed and explained.

2) The potentially most interesting result reported here is the detection of Synthetic Physical Interactions (SPIs), where a forced interaction does cause a growth phenotype. But it's not entirely clear that one learns all that much from these results. The one example of an SPI that they do examine in more detail in Figure 5 could easily be an indirect relationship rather than a direct molecular link (yeast null for chromatin associated proteins, hmo1 and Sgf29, show increase levels of a kinetochore protein Dad4). This would be much more compelling if the authors had data indicating some direct physical interaction (IP/mass spec) or biochemical rational for how hmo1 could regulate the kinetochore to support their claim that SPIs can identify functional regulators- this could easily be a case where hmo1 regulates transcription of Dad4 directly or indirectly. If so, please include this in the revised version or at least comment on relevant data in support of a direct and/or functional interaction.

3) The clustering of complexes (Figure 6) is not that convincing. the approach seems like an awkward strategy for obtaining information that is much more effectively obtained by mass-spec. For example, the histones fall into two distinct categories and the CPC, NDC80, Spc105 and MAPs complexes don't seem to cluster at all. This seeming disparity with known interactions requires explanation.

4) Results, second paragraph: “we found that 98% of GBP-GFP combinations […] do not affect the growth of cells.” Do 98% not affect growth at all, or are they using a z-score threshold? If z-score, this should be clarified, as it is not necessarily the same as "no effect on growth".

5) Results, third paragraph and Figure 2: “Fluorescent imaging confirmed that ~83% of interactions do occur and typically result in protein relocation […] Of the 524 GBP-GFP combinations that we could score, 435 were detectably colocalized (Figure 2C), indicating that in most cases the protein-protein fusions do occur.” Figure 2C shows this and 2D breaks it down in more detail. However, ~50% of the colocalized strains belong to the "indistinguishable" category = proteins that normally colocalize (2D). It is misleading to include this category for estimating how often relocation/interaction occurs. Correcting for this will result in a percentage dramatically lower than 83%. Similarly, this should be clarified in the counts in the text ("435 of 524") and the Figure 2C legend.

6) Results, fifth paragraph: “Around 2% of the forced interactions restrict growth […]” Specify z-score cutoff used to qualify as restriction in main text.

7) Results, fifth paragraph: “[…]of the 727 SPI proteins […]” -> of the 727 SPI query proteins.

8) Results, fifth paragraph: “[…] whose sequestration to another compartment is lethal […]” Did they show it's actually lethal or just decreases growth (i.e. sick)?

9) Results, fifth paragraph: Discuss why there is a difference in suppression of interactions between the frequent and non-frequent SPI groups.

10) Results, sixth paragraph and Figure 4B: It's here stated that target proteins from the same cellular compartment give similar SPIs. While the figure and analysis are suggestive of this, it would be better to carry out a statistical test to corroborate the statement. E.g. Box plots of the distributions of SPIs from same vs. different compartments, accompanied by a Wilcoxon rank-sum test to determine significance.

11) Results, seventh paragraph and Figure 4C: The authors are comparing two distributions of PPI counts (SPI vs. non-SPI) and compute a p-value for the difference using Spearman's rank correlation. I doubt Spearman's rank correlation can be used to produce a p-value for the difference between two distributions. Additionally, the stated p-value (2.2E-16) appears extremely optimistic given the large overlap of the box plots.

12) Results, seventh paragraph and Figure 4D: The CLIK analysis should be described better.

13) Results, eighth paragraph: Describe or reference the gene ontology enrichment analysis.

14) Results, eighth paragraph: Was fluorescently tagged Nuf2 examined in these cells as well? How is Nuf2 affected?

15) Figure 5A: Explain why Mtw1 was chosen.

16) Figure 5B and 5C: Describe in much more detail how to interpret these plots. Also, what are the error bars? Finally, is the p-value (E-10) really correct? Depending on what the error bars represent this looks low.

17) Results, last paragraph: “[…] SPI data can be used to predict protein complexes […]” Substantiate this claim. Show if the SPI data actually have predictive power with a ROC or precision recall curve.

18) Results, last paragraph: Try to interpret why the DAM/DASH complex segregates into distinct clusters.

19) Discussion: I suggest explicitly writing "physical interactions" instead of "interactions" to not confuse with SPIs.

20) Discussion: “[…] and derive quaternary structure […]” ‘provide information on’ would be more appropriate than ‘derive’.

21) Discussion: “[…] 54% (394) are conserved in human cells.” May be worth discussing how this compare to the conservation of the complete yeast genome to human?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting your article "Synthetic protein interactions reveal a functional map of the cell" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Randy Schekman as the Senior and Reviewing Editor. Stanley Fields and Nevan Krogan have agreed to share their identity. There remains one concern with the language in your Abstract. Please adjust this according to the suggestion of reviewer #1.

Reviewer #1:

The authors have largely addressed the concerns I raised and put in appropriate caveats in their revised manuscript. I am still concerned that their Abstract is misleading in claiming to establish that proteins have an "unanticipated tolerance for forced protein associations and consequently their relocation". I think it is likely that in many, perhaps the large majority, of the cases where apparent relocation of a protein does not disrupt function has to do with at least partial retention of the protein in its correct locations. It would indeed be quite surprising if most nuclear proteins could function in the cytosol or most organellar localized proteins could function outside of their native organelle. I do not think this is what the authors intend to say (and certainly is not what they have shown) but I could easily see how a casual reader of the Abstract could be left with this impression.

Reviewer #2:

I find the revised version acceptable.

Reviewer #3:

I am happy with the revisions and support publication.
