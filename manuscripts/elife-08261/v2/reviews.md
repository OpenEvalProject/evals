# Peer review - Round 1

Editors:
- Tanya T Whitfield, University of Sheffield , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.08261.022](https://doi.org/10.7554/eLife.08261.022)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled “First quantitative high-throughput screen in zebrafish identifies novel pathways for increasing pancreatic β-cell mass” for peer review at eLife. Your submission has been evaluated by Fiona Watt (Senior editor), Tanya Whitfield (Reviewing editor), and three reviewers, who had also seen your previous submission. One of the three reviewers, Wenbiao Chen, has agreed to share his identity.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

As you will see, all three reviewers find your manuscript much improved, and all agree that the assays you describe demonstrate an important 'proof of principle' technical demonstration for your high throughput ARQiv system. However, all three reviewers also have significant concerns with the manuscript, which must be addressed in any revision. The full reviews are appended below for your reference, but please pay particular attention to the following points:

1) Reviewers 1 and 2 have some remaining questions concerning the underlying biology of the system. Please add extra experimental detail or discussion as requested.

2) Improve the resolution of the figures where possible.

3) The statistical analysis is a concern and needs strengthening. Re-do the statistical analysis with appropriate tests (i.e. ANOVA with post-hoc correction for multiple comparisons, rather than serial t-tests).

Reviewer #1:

The revision has markedly improved the manuscript. The authors have successfully addressed my concerns except for the first two. Overall, the study is interesting because 1) it is the first true HTS screen performed in a vertebrate organism; and 2) it has identified new regulators of β-cell mass.

Minor comments:

1) The authors only partially took care of my concern that the increase of β cells in some cases may be a consequence of impaired insulin signaling. I would have been completely satisfied on this if glucose was measured within the first day of treatment, rather than after 3 days at which compensation may have run its course. A statement acknowledging this possibility should suffice.

2) The authors only partially addressed my concern on their interpretation of proliferation vs differentiation. The authors were correct that proliferation of both β cells and progenitor cells is interesting, but differentiation from replicated progenitors is still differentiation. The data in Figure 6B does not support that β cell replication plays a major role in paroxetine-induced β cell increase. If the new β cells were all from replication, only 3 β cells would have gained from 6 double-positive cells, accounting less than half of the 7 new β cells. The authors should take this into consideration.

Reviewer #2:

In the current resubmission, the authors have substantially improved the manuscript and addressed many, although not all, of the concerns. Overall, the data are now presented in a manner that makes it comprehensible to the reader. My remaining questions:

1) The secondary islet assays. It still seems like a major part of their results depend on the increase of secondary islets from the drugs. In their rebuttal, they state that at day 7, the identification of such islets is “not robust” because of the ins/ss reporters, so they turned to the neuroD and pax6 reporters as orthogonal assays. But what I still don't quite understand is the fact that many of the drugs seem to globally increase neurod:GFP expression: in Figure 3A/B, it seems like the overall increase in neurod:GFP is not confined to the pancreas (i.e. just below the clearly shown dotted line delineating the pancreas). I can accept that there are ectopic islets in the pancreas as marked, but it just seems hard to separate this effect out from the more global effects on neuroD expression. Is there any type of histology that could increase confidence that these are truly secondary islets, and not just an artifact of the transgenic reporter system?

2) Figure 5: It is unclear to me why DMSO produces a “predictable increase in signal”; of which reporter? Also, in Figure 5F, what reporter are you referring to here? The NFκB-GFP or hmgb1-mCherry?

3) Figure 6G/G': The serotonin staining seems extremely widespread throughout the pancreas, and while it overlaps with insulin, there are many areas that do not. How did you validate the serotonin antibody to ensure this has any specificity in your assay?

Reviewer #3:

This is a much improved manuscript that is now easier to read and understand. The re-write has made clear how the whole organism HTS was done, including how big of an effect size they expected to be able to detect, how the data was analyzed, and how the screen was performed – none of which was clear in the earlier version. I appreciate the point that the hits are expected to be (hoped to be!) weaker than the positive control for biological reasons and retract my earlier concerns about this.

The “high-throughputness” is most impressive and represents a significant advance. I am also more convinced in this version by the validation of serotonin and NF-κB hits, with much more details and controls (such as validation of NF-κB in the transgenic). This overall improves the manuscript and better highlights these pathways as interesting from biological and future pre-clinical screening viewpoints.

I still have one quibble:

1) I disagree with the interpretation of doing serial t-tests as valid without correction. After all, if you did 100 follow up experiments and showed one test at a measly p=0.05, would you call that a real result, when such a result is quite likely by chance? No. In fact, the initial screening does take this into account with false discovery assessments, but the follow-up studies, which you might consider a “mini-screen” do not. This is incongruous.

One could argue that your screen has now given you a prior expectation for a positive result, so subsequent statistical analyses can reflect this, for example, using a one-tailed t-test instead of a two-tailed one, since you actually have a prediction for the directionality of the result. Or other Bayesian methods may be appropriate. However, the number of experiments you do must still be accounted for statistically.

I do note that additional follow-up tests for key hits (serotonin/NFκB) mitigates these flaws somewhat, but that doesn't justify t-test mis-use.

[…] I do appreciate that how to statistically handle this kind of data in some sense is still up for debate. However, as this paper will be laying the foundation for future true high-throughput screening in the zebrafish, establishing rigorous standards for follow-up validation is of significant importance. May I recommend a nice discussion of these issues in Colquhoun D. (2014) An investigation of the false discovery rate and the misinterpretation of p-values. R. Soc. Open sci. 1: 140216. http://dx.doi.org/10.1098/rsos.140216 as a starting point for thinking through these issues?

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The previous decision letter after peer review is shown below.]

Thank you for choosing to send your work entitled “Quantitative in vivo high-throughput screen: repurposing drugs for increased β-cell mass” for consideration at eLife. Your full submission has been evaluated by Fiona Watt (Senior editor), Tanya Whitfield (Reviewing Editor), and three peer reviewers. The decision was reached after discussions between the reviewers. Based on our discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

As you will see, while the reviewers found the work potentially interesting, all three have substantial and overlapping concerns with the manuscript, including the design, analysis and interpretation of the study, and the advances that it makes over existing work.

Reviewer #1:

This work describes an application of the ARQiv system to a high throughput identification of chemicals that stimulate β-cell differentiation or proliferation. It uses novel transgenic zebrafish reporters and imaging to generate statistical measurements of compounds that rise above the noise of such assays. Although the application is important and technically impressive, there are substantial concerns about the manner in which the data is interpreted and presented which make me less than enthusiastic about the manuscript in its current form. I will highlight several key issues:

1) Using a ratio of β/δ cells: It is unclear to me precisely what practical function the δ cells serve in the initial screen. I realize the goal was to find things that specifically worked only in β cells, but wouldn't a compound that simply kept β cell intensity constant, yet decreased δ cell intensity, also show up in the screen? Where is this data used, as the biological differences here could be potentially important?

2) The assay they are using for induced β-cell differentiation: Nowhere do the authors show a photo of validation using the original transgenics used in the screen. Only in Figures 3 and 4, using the neuroD reporter, do they show validation. neuroD marks many cell types in this region, and the representative fish they show in Figures 3 and 4 show many, many ectopic GFP+ cells outside of the dashed line presumably marking the pancreas. Without the data from the original, how do we know that these drugs do not simply increase insulin-YFP expression in multiple areas of the embryo, which would have scored as a “hit” in the screen? Furthermore, and in line with this concern, how do they know that counting the neuroD positive cells outside of the dotted area does not simply represent abnormal migration/morphology of the endocrine progenitors? For instance, in Figure 3A, it really looks like the large GFP islet is diffuse in the parthenolide treated animal, so it is hard to know if this result truly represents enhanced differentiation or simply a migratory effect.

3) The signal/noise ratio calculation: This is very difficult to interpret in its current form. In Figure 1C/D, what exactly do the black/yellow (or red/yellow) bars indicate? And why is there seemingly no dose response relationship?

4) Positive controls: It is odd that in their initial screen, they used the notch inhibitor DAPT (notoriously insoluble) and this seemed to show a specific effect on β cells. Yet, in Figure 5, they use a different notch inhibitor (RO4929097) which now shows essentially no specific effect on β cells but instead an effect on both β and δ cells. This discrepancy makes it hard to know how to interpret the original screen. In fact, if anything, in Figure 5H, it looks like RO4929097 causes a decrease in the number of GFP+ cells.

5) Baseline stability of the reporters: In the discussion of 5HT section ('Serotonin signaling selectively increases β-cell proliferation’), the DMSO animals had 29 β cells, which went up to 35 β cells with RO4929097 (the positive control). Yet, in the next paragraph, and shown in Figure 6, the DMSO animals now show that the DMSO animals have 33 β cells, nearly the same number seen in their “positive control”. Granted, this further increases with fluoxetine to 42, but these inconsistencies when looking for relatively modest effects is of great concern, if the baseline stability of the assay (i.e. DMSO from experiment to experiment) is not especially stable.

6) The NF-κB reporter: In Figure 4, the authors show a dual color confocal of an NFκB/Notch reporter line, but yet oddly do not show the effect when they add in their hit compounds. While it is interesting that there are a few cells that co-label, this figure does not help us understand how these compounds may be affecting this signaling pathway in the fish.

Reviewer #2:

The manuscript by Wang et al., “Quantitative in vivo high-throughput screen: repurposing drugs for increased β-cell mass”, describes an ARQiv-based quantitative HTS screen in zebrafish for identification of drugs that increase β-cell mass. The screen identified drugs that enhance β-cell neogenesis and drugs that promote β-cell replication. Of those the role of NF-κB and serotonergic signaling were validated with additional experiments. Overall, the study is interesting because 1) it is the first true HTS screen performed in a vertebrate organism; and 2) it identified new regulators of β-cell mass. However, there are several issues with regard to the experimental approaches and the interpretations of the results.

Major issues:

1) Although the whole organism screen is powerful for identifying compounds [that increase β-cell mass, the hits may act direct to increase β-cell mass or indirectly by impairing insulin signaling or glucose metabolism, which in turn induces increase of β-cell mass. The latter may be problematic for therapeutic purposes. The long (from 3dpf to 7dpf) drug treatment in the screening protocol makes it difficult to distinguish the 2 possibilities. This should be addressed in the validation step. For example, do the selected hits increase glucose in the fish? Assuming the new β-cells are functional, do treated animals have a larger capacity to maintain glucose homeostasis under diabetogenic conditions?

2) The conclusions on β-cell replication are based on prolonged EdU labeling. The labeling protocol cannot distinguish whether EdU is incorporated prior to or after β-cell differentiation. This is especially the case for the adult studies where a two-week labeling period was used.

3) The evidence for the conclusion that NF-κB signaling in pancreatic progenitor cells regulate endocrine differentiation needs to be strengthened. For example, it is not shown whether the inhibitors decrease EGFP expression in the ductal progenitor cells.

4) The conclusion that neurotransmitter modulators act through the neuronal signaling pathway is too simplistic. The pancreatic β-cells have many neuronal characteristics, including the ability to synthesize and perceive many neurotransmitters. These modulators may act directly on β-cells.

Reviewer #3:

Wang et al. describes a high throughput screen in zebrafish for small molecules that can affect pancreatic β-cell proliferation. Given that similar screens have been previously described (Tsuji et al. 2014), including by this group (Rovira et al. 2011), the main advance described here is the high automation of the screening assay, with a secondary novel finding being the link between β-cell production and NF-κB signaling. Unfortunately, I found the description of the screening, especially all the computations, statistical calls, and subsequent validations, to be so sloppily described that it is difficult to understand what was actually done. The work does not appear to have been carefully edited, with major editing errors appearing as early as the Introduction – the sentence starting with “OR-4” appears to be an editing note – and this permeates throughout the figures and the text. My impression is that there is not much of an advance over the other zebrafish pancreas screens. It is also unfortunate that none of their hits appear even close to as effective as their positive control, DAPT (e.g. Figure 3C, where DAPT is off the charts and most of the 'hits' look like modest effects at best).

First, they lay out some details of the positive control, DAPT, in Figure 1, but there the mysteries already begin. Figure 1C and D show some box plots, with color-coding that I do not understand, with a curve fit to the data in some way that is not described, and a reference to a “blue-lined range” that doesn't exist. Somehow this data is used to evaluate hits later, but I already don't understand it, and this is not described in the very superficial Methods section, either. Figure 2A-D shows a glimpse of the computational logic, but none of this is explained. There is some kind of curve fitting, never once mentioned in the text or Methods, Figure 2B shows something called a “Ranked Avgs”, also never described, and Figure 2C shows a map of SSMD values, but how this is calculated, and how the 1.3 cutoff was chosen, is never said. All this detail is important, but I cannot find it anywhere, in the Methods, or supplement or figure legends.

In the next step, they validate their hits, but I still have concerns. First, none get even close to the effect of the positive control. Second, the Methods say this was evaluated by Student's t-test, but surely this needs to be corrected for multiple comparisons. Third, I am unclear about how a secondary islet is counted, as the arrows shown in Figure3–figure supplement 1 seems to point to more like 6-10 islets, but Figure 3C never gets above 6 islets. Are these best cases only? Are some islets more dispersed, so not counted the same? I can't tell.

Finally, they implicate two signaling pathways, NF-κB and serotonin, in β-cell proliferation. The serotonin pathway is already well described, so the novelty of these results rest on the NF-κB story. Unfortunately, this is not terribly convincing-the compounds from the initial screen, thioctic acid and parthenolide, are not exactly NF-κB go-to compounds, and the other compounds they test in Figure 4C are barely described and should be shown as a dose-response, not a single, mysterious dose. Whether these compounds affect NF-κB signaling in zebrafish in these conditions is also unknown, but they could have tested this directly with their NF-κB reporter fish.
