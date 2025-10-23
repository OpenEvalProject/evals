# Peer review - Round 1

Reviewers:
- Anshul Kundaje, Stanford University , United States

## Review text

DOI: [10.7554/eLife.18541.032](https://doi.org/10.7554/eLife.18541.032)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Determining sampling rates for high-throughput time series studies" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aviv Regev as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted these comments in an effort to crystallize our concerns about the novelty of this work. Before we render a binding decision, the Board asks that you respond soon to the essential concerns below in order to help us assess the technical advance you have achieved.

Summary:

Time course studies are critical for understanding biological processes. Facilitated by advances in sequencing technologies, high-throughput time series analyses are becoming more and more prevalent, and often more than one type of data is collected for each time point in order to probe/understand various aspects of cellular activity. Selecting the precise time points to use in such studies is challenging and often ad-hoc. In this manuscript, Kleyman et al. describe Time Point Selection (TPS), a method designed to address the problem of determining sampling rates in time series studies. The idea behind TPS is as follows:

1) start with a small set of genes known to be important for the process to be studied;

2) use cheap array-based experiments (e.g. NanoString) to measure expression of these genes at a high, uniform, sampling rate;

3) use the data to infer a subset of points that can be used to optimally "reconstruct" the entire data set from step 2 (importantly, the authors implement a rigorous, spline-based procedure for identifying optimal time points);

4) use the time points selected in step 3 for the genome-wide experiments.

The authors applied TPS to lung development in mice, and showed that the time points identified by TPS are better than uniform sampling and even phenotype-based sampling (in terms of reconstructing the mRNA profiles of the selected genes), and can be used not only for time series expression data, but also for miRNA and methylation time series data. The general strategy implemented in TPS has potential and could prove useful for future time course studies.

Essential concerns:

1) All the reviewers felt that the method is only compared to the most trivial baselines (uniform and random). E.g. there is no comparison to even the authors’ own 2005 paper on a closely related setup. There are various existing works on selecting knots for splines. One could use them, for example, by first fitting a spline to all the high-rate data, and then select points for that curve. Does TPS work better than non-trivial baselines? The authors must perform systematic comparisons to related work such as Rosa et al. 2012, Optimal Timepoint Sampling in High-Throughput Gene Expression Experiments. Further, the paragraph in the Discussion section showing the advantage of using TPS over phenotype-based sampling should be moved into the main text and presented clearly as this is a critical part of the paper.

2) All the reviewers also felt the manuscript required additional clarity and specific comments are below.

3) Since TPS uses an iterative algorithm for solving an optimization problem with many local optima, the initialization procedure is critical. I appreciate the fact the authors tested multiple procedures for initialization, and when using TPS one can try all initialization procedures (and in the end select the one with the best results on the left-out data). It is not clear, however, whether the software implemented by the authors tests all these initialization procedures.

4) In addition, the initialization metrics/methods are confusing. The Methods and Supplementary Methods sections talk about "uniform", "intervals of equal sizes", "max distance", metricA, metricB, and metricC. But it is not clear what initialization method was used in different analyses/figures. What procedure was used in Figure 1? The figure caption should mention that. The authors should decide on specific names for the different initialization methods, and use them consistently throughout the paper. Also, some figures present redundant results. Figure 1—figure supplement 1 presents results for "max distance", metricA, metricB, and metricC. Figure 1—figure supplement 2 presents "max distance", metricA, metricB, and metric, random points. So Figure 1—figure supplement 1 could be removed.

5) The "iterative improvement" procedures are also confusing. The method presented in Methods optimizes the mean squared error (on the left out data points) by iteratively removing/adding one point at a time. I assume this method was used in Figure 1. Then, in Figure 2A, what does "absolute difference mean"? (I assume this refers to an initialization procedure, right?) The way the authors name the combinations of search and initialization procedures in Figure 2 is very confusing. Some names reflect an initialization procedure (Uniform Selection), other a search procedure (Simulated Annealing), others an evaluation criterion (Weighted Error). Thus, the results presented in Figure 2B are confusing, and neither the caption nor the main text clarify what is being tested. Similarly for Figure 4.

6) For the miRNA data, the authors perform a comparison of results using mRNA versus miRNA data for deciding the sampling time points. But the way the results are presented is again confusing. In the main text the authors say: "The results are presented in Figure 4. In addition to the comparison included in the mRNA figure, the miRNA figure includes the optimal results for using the actual miRNA data (as opposed to mRNA data) to select the points." But the results using the miRNA data are not in that figure.

7) It is nice that the project has a website but it looks mostly incomplete. Can the authors make the site a full-fledged web service so novice users and biologists with no programming background can use the software? Users should be able to upload a time series dataset and receive results with interactive visualization.

8) There is only one case study. The method is described as a broad method, but since it was applied to one process, it should be stated more carefully that it is a general method. Perhaps the authors should focus on this case study without the need to "sell" the method as the primary focus of the study.

9) The examples in Figure 6 are impressive. But how typical are they? What is the distribution of MSE across genes with TPS and with predefined timepoints?

10) Performance curves (Figure 2, 4). Is the benefit due to a small number of genes, or consistent across the genome? It would be useful to show scatter plot (across genes) of MSE with TPS and with the best baseline.

11) Figure 5. How were these three genes selected? Are the correlations surprisingly strong when corrected for multiple comparisons? In 5A, the correlation is probably dominated by an outlier (third green marker) otherwise It is hard to see that the two curves are strongly anti-correlated. A similar outlier is also in Figure 6—figure supplement 1C. Accompanying with a scatter plot would clarify the relation between the two. Also, compute confidence-interval for that correlation using bootstrap.

12) Figure 2: Seems that the uniform baseline was omitted from the left panel, please add it. Please also provide error bars for TPS and uniform baseline (on the left panel) by bootstrapping across the set of genes.

13) Subsection “Identified time points using mRNA data are appropriate for miRNA profiling”, second paragraph: "Using the selected based on mRNA data […] random points (p<0.01)". What is the p-value for the uniform baseline?

14) There is a line in the paper that says 'performance is very similar [...].0.43 […] 0.40". Provide a measure supported by a statistical test.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Selecting the most appropriate time points to profile in high-throughput studies" for further consideration at eLife. Your revised article has been favorably evaluated by Aviv Regev as the Senior Editor, a Reviewing Editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below by the referees. We ask that you pay close attention to these specific items, which we call out here, and are in the specific reviews below:

1) The revised version still has formatting issues. The response refers to Table 5, but no such table is given; figures are not numbered and provided separately from their captions, which makes it hard to follow and comment.

2) The new Figure 5 replaced outlier genes. The main text should explain how the 3 examples shown were selected.

3) We do not see a benefit in having the left panel of Figure 2. In their response, the authors say they wanted to show the difference between TPS and uniform selection. But panel (A) shows random selection, not uniform selection. Random selection is a made-up baseline designed to make TPS look good. Now that they have better baselines comparisons, the paper does not need it, and panel (A) can be removed.

4) Figure 3. Replace "Rem points" with "remaining points".

5) The authors mentioned that they "improved the caption of Figure 1 to explicitly state which initialization method is used for each result". But Figure 1 caption is unchanged. (They did clarify other figure captions.)

6) The authors added Figure 4—figure supplement 3 to show the performance of TPS trained on miRNA data. But that plot could/should be included directly in Figure 4. Otherwise it is hard for the reader to compare TPS when trained on mRNA versus miRNA data. Also, since there are several versions of TPS, which one was used in Figure 4—figure supplement 3? These kinds of details are still missing.

7) Some of the figures are still of inadequate quality. Some plots have a strange aspect ratio (e.g. Figure 5). Several plots do not have a y-axis label (e.g. Figure 3). Sometimes the labels are incomplete (e.g. "Error" in the comparison to Singh et al.; is it mean squared error?) Overall, the paper is still difficult to follow. (The fact that all references appear as "?" in the PDF also makes the paper hard to read. I assume the text file was not processed correctly during submission. But shouldn't the author verify that before submitting the paper?)

Reviewer #1:

The authors addressed most of the concerns raised. Most importantly, the authors added some evaluation to other approaches for selecting time points, and replaced results based on outliers.

The revised version still has formatting issues. The response refers to Table 5, but no such table is given; figures are not numbered and provided separately from their captions, which makes it hard to follow and comment.

Reviewer #2:

The authors addressed several comments from reviewers. I am now ok with the substance of the paper. While it would be useful to see validation on additional data/systems, I appreciate the difficulties in getting additional data sets for further testing of the method.
