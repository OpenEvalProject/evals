# Peer review - Round 1

Editors:
- Alan M Moses, https://ror.org/03dbr7087 University of Toronto Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79812.sa0](https://doi.org/10.7554/eLife.79812.sa0)

The authors develop important machine-learning approaches to extract single-cell growth rates and show convincing evidence that their methods can yield insight into growth control. They also introduce compelling new methodologies for several other aspects of automated image analysis.


---

# Peer review - Round 1

Editors:
- Alan M Moses, https://ror.org/03dbr7087 University of Toronto Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79812.sa1](https://doi.org/10.7554/eLife.79812.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A label-free method to track individuals and lineages of budding cells" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Naama Barkai as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. Overall, all the reviewers were impressed by the innovative techniques and potential biological insights in the paper. At the same time, however, after discussion, the reviewers were not convinced that the work represents a "method" in the sense that it could actually be used by others or on data from other labs. Further, the reviewers all had major problems with the clarity of the manuscript, finding it difficult to fully understand either the key methodological or biological contributions.

Essential revisions:

1) Convince the reader that the "method" described here can be applied in other settings and that improved identification of small buds will be a generally important advance towards estimating growth rates from movies. As it stands, the reviewers wondered if the contribution here was really only a solution to a specific data analysis problem that arises in the specific imaging/microfluidics set-up considered here. Ideally, this issue could be addressed by clearly specifying the problem(s) that the method is designed to solve (e.g., is it bud identification, cell tracking and/or growth rate estimation), and clear comparison of this method to state-of-the-art methods on a variety of datasets (with appropriate held out test data and statistics.)

2) Clarify what the major novelty/contributions/discoveries are in the main manuscript text, describe them fully, and move all the other clever innovations (that are not fully supported by empirical data) to the supplementary materials or Methods section. For each contribution, give the appropriate context (previous work, hypothesis, importance, etc.) and ensure that the generality of the claims match the experiments/data presented (e.g., generality of observation of sizer vs timer regulating bud growth or generality of the tracking results beyond cells grown in traps). Ensure that the Title and Abstract reflect what has actually been demonstrated in the paper.

3) Overall, clarify the writing to give the appropriate scientific context for a general biology audience, and remove or explain technical jargon that will not be familiar to the readers of eLife.

Reviewer #1 (Recommendations for the authors):

Specific issues:

– I am left wondering if this a software that other groups can expect to download and use, or is it an abstract "method" to make the point that it's possible to accurately segment small buds and extract growth rates and other labs should implement similar systems for their own imaging setups?

– Quite a bit of discussion of "morphological erosion" which I could not really follow. Is it the same usage as this?

https://en.wikipedia.org/wiki/Erosion_(morphology)

The authors should define what they mean by this term and explain why it is important.

– Very hard for me to understand the training and testing data: what is the data used? Was the method ever evaluated on data from other microscopes/labs/benchmarks? The only numbers I got were the training images 588 trap images – 1813 annotated cells in total.

– Sfp1 experiments are explained relatively clearly compared to the rest of the paper, but still major improvements are needed. E.g., it is never stated that the authors are assuming nuclear localization of Sfp1 reflects its "activity" (what is even meant, transcriptional activity?) While plausible, what is the evidence that this is true? Similarly, "enters the nucleus in response to two conserved nutrient-sensing kinases" – again this is not specific enough. How does Sfp1 "respond"? Presumably the kinases phosphorylate something and eventually Sfp1 translocates into the nucleus, and the authors are quantifying the GFP-signal in the nucleus? Non- experts will not be able to follow this without much more specific explanation.

– "With BABY, we add the ability – with no extra imaging costs – to measure what is often our best estimate of fitness, single-cell growth rates." one of the points of the paper is that the cell size/growth information can be obtained 'for free' (i.e., with no additional labels) from microfluidics experiments. Have the authors actually gone back and reanalyzed any (even of their own) previously published data to illustrate this point? As it stands it seems a bit like a rhetorical argument.

– "To better characterise how growth rate varies during the cell cycle, we ran experiments for cells with the gene MYO1 tagged with Green Fluorescent Protein" Very hard to follow this. "Ran experiments" is not scientific. What is the logic? What was measured? "We determined that we could predict cytokinesis from growth rate because at cytokinesis the mother's and bud's growth rates often reach a similar magnitude (Appendix 5)." I can't follow this. What is the evidence that cytokinesis can be predicted? How is this measured? What are the alternative models that were rejected? Do I need to read Appendix 5? I found this claim in Appendix 5: "We evaluated the algorithm by the correlation between the real time of cytokinesis and the predicted time" What were the sample sizes for the test data? etc., etc., How was the "real" time measured? Is it this: "The actual time of cytokinesis is taken to be the candidate point with the minimal derivative, corresponding to the strongest down-shift in fluorescence."?

Reviewer #2 (Recommendations for the authors):

1. It is not entirely clear to me how successful the automated bud-mother assignment actually is. In the main text (page 6) the authors talk about 80% precision. However, in the appendix we learn that the recall is only 47%. What is the actual accuracy of correct mother-bud identifications after the downstream assignment? How many tracks are rejected by the post-processing? The accuracy of the final pedigree analysis needs to be reported more directly.

2. Along those lines, the results shown in Figure 3c and d make it very hard to assess the actual accuracy of the automated extraction of cell cycle information. Especially the low number of only 6 daughter cells in Figure 3c is far from sufficient, as can be also seen by the unusual bimodal distribution – which does not reflect the distributions in Figure 3d. Instead, the authors should compare the results in Figure 3d to a manual analysis of the same cells (or at least a significant subfraction). Rather than histograms, it would be informative to see plots showing predicted vs manually analyzed TM and TD or a distribution of differences between those values in manually annotated and predicted data.

3. Unfortunately, the correlations shown in Figure 2a and c of Appendix 5 are mostly meaningless. The high correlation is simply a consequence of the fact that absolute time of the experiment is shown, and obviously cells born later in the experiment will finish cytokinesis later (or have a later time of predicted cytokinesis). As can be seen from this plot, predictions often deviate dramatically (on the timescale of hours!) from the ground truth. We need to see the same plot using time relative to bud emergence rather than absolute time.

4. The plots shown in Figure 3a and b are fine, but it would be beneficial to also see more standard metrics, such as average precision vs IoU threshold (see for example https://doi.org/10.1038/s41592-020-01018-x), or MOTA for tracking.

5. To allow fair comparison, segmentation by BABY using a single z-slice should

be compared with e.g. YeaZ (and ideally other deep learning methods) retrained with the same data.

6. It is not entirely clear to me whether Figure 4d and e rely on the Myo1-GFP signal or are purely obtained with automated BABY analysis. The Myo1-based data are a nice opportunity to further quantify the accuracy of the BABY-based cell cycle predictions. Again it would be nice to see predicted vs Myo1-based cell-cycle duration plotted against each other.

7. The biological results shown in Figure 4 are very interesting. However, I think to support the claim of sizer-timer based bud growth regulation, more than two conditions are needed. Does this claim still hold with multiple different media, or even appropriate mutants?

8. If I understand correctly, buds by definition are defined as independent cells if they become larger than 24 fL (page 33)? How many buds are affected by this criteria? How does this match with Figure 4e, where we clearly see bigger buds?

9. The claim in Figure S1 that YeaZ underestimates bud size more than BABY should be supported by a more direct plot, e.g. showing YeaZ (and BABY) predictions vs ground truth bud size on a single bud level.

10. Is the choice of evaluating 10 sets of hyperparameters in Appendix 3, Figure 3 determined by limiting computational resources? If not, this seems rather sparse, especially given the fact that panel b does not give the impression that a parameter set close to the optimum is found. Would testing more combinations not likely result in a significant improvement?

Reviewer #3 (Recommendations for the authors):

I would recommend the authors rewrite the paper focusing on the very interesting biology. Then, they can choose whatever method they like to analyze their data since that is not the main focus of the paper and there are no claims as to which method is better than which other.
