# Peer review - Round 1

Editors:
- Kate M Wassum, University of California, Los Angeles United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55585.sa1](https://doi.org/10.7554/eLife.55585.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The role of the insula cortex is widely varied and highly complex. There remain questions regarding the connectivity of its global inputs and outputs. This manuscript presents a comprehensive dataset of insular cortex anterograde and retrograde mapping using modern tools such as AAVs, monosynaptic rabies tracing, and high-quality quantitative analyses. The study is technically very well executed. Semi-automated approaches for brain alignment and cell quantification to reduce bias are used and discussed. While some of the results presented have been previously reported in earlier studies, presenting it all in one place within a consistent experimental and analytical framework is extremely useful for advancing future investigations of insular cortex. The data is of high quality and is plotted in ways that make it easy for the reviewer to digest these large data sets.

Decision letter after peer review:

Thank you for submitting your article "A whole-brain connectivity map of mouse insular cortex" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Kate Wassum as the Senior Editor and Reviewing Editor. The following individual involved in review of your submission has agreed to reveal their identity: Yoav Livneh (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Essential revisions:

1) Statistical comparison of the connectivity patterns in Figures 2-5 need to be run. With many regions and a small n (n=3), it is likely that many of the differences will not be significant after correcting for multiple comparisons. Thus we suggest to increase n to ensure sufficient statistical power to make more concrete claims about the organization of connectivity. This will help support some of the main conclusions.

2) Since Cre drivers were broadly expressed, please report which layers the starter cells occupied. Though they are claimed to target all layers, in the representative images shown in Figure 1—figure supplement 1A and 1B, the majority of starter cells seem to be in layer 5. Adding n may also allow them to identify biases in input/output organization based on the layer distribution of the starter cells.

3) Rabies traced cells tend to have highly variable fluorescence levels and machine thresholding tends to exclude many dim cells. Please include human counts for several rabies brains to verify the cell counts collected by the algorithm. Using several human counts to verify the rabies cell numbers in a single brain, please verify the expected percent error for various human counts and machine counts.

4) There are several places where additional details and clarity are needed:

a) Aligning atlas borders to coronal sections may not accurately define area borders, especially if there are defects in the tissue. Warping or skewing due to mounting and shrinking, as well as imperfect cutting often lead to coronal sections that do not match the atlas. How are reliable landmarks being used across the entire surface of the tissue to properly warp the atlas borders to the tissue? Please clarify.

b) Regarding spillover to Pir, S1, S2 and M1 – the authors mention that they "…asked if these contaminations affected the qualitative connectivity structure by comparing them to tracings without contamination". However, it is unclear how this was done and no data is presented to demonstrate this. Please describe this in detail and present examples of excluded data and criteria for exclusion? This is a critical point for interpretation of the data.

c) When detecting axons, how was thickness handled? Depending on the pixel resolution, it is possible that bundled or single axons will not be represented proportionally. In addition, differing saturations can result in halo effects and thickening. Were these types of effects considered when counting pixels?

d) In Figure 1 and main text, the author described "minimal (or small) percentage of cells” were detected in the M/S, Pir. Please indicate the actual numbers. Any starter neurons in other IC regions? Thus, in mIC or pIC when aIC was targeted etc.

e) The authors should provide more details about their analysis methods, especially for the machine learning-based approaches.

f) Overall the methods about quantification of axon tracing should be described more in detail. Specifically, the steps applied in the custom FIJI macros used.

5) Axon pixel counts rely on methods that are highly sample dependent as noted by Grider et al., 2006. Grider et al. maintained uniform acquisition settings across the samples, however, variable acquisition settings were used by the authors. In addition, thresholding in this manuscript was done for each image, a destructive task, and hessian ridge detection can then find more or fewer pixels than existed in the original image according to Grider. These results may be more qualitative than quantitative, on the contrary to what the authors described in their main text. Please clarify and address this.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A whole-brain connectivity map of mouse insular cortex" for further consideration by eLife. Your revised article has been evaluated by Kate Wassum (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Essential revisions:

1) In this revised manuscript, the authors ran multiple t-tests instead of increasing number n. Multiple t-tests are not the best test since they increase the Type I error rate. An ANOVA with posthoc multiple-comparison tests, or non-parametric to be more meticulous, would be more appropriate. Please include this analysis.

2) Contrary to the authors' argument using RPDs, human count versus automatic counting do not correspond well. For example, according to Supplementary file 1, sheet 2, B section, in aIC-Po, human 3 = 26, automated = 133. This is an order of magnitude difference. In pIC-Po, human 3 = 249, automated = 118. Then, this time the human 3 counts more than ~100 cells than the automated does. Thus, the trends are opposite. In addition, RPD cannot predict the directionality; thus, whether the humans tend to count more or less than the automated counting does. This concern should be addressed. The reviewers suggested that showing the raw data overlaid with automatically identified cells would be a helpful first start to understand the sources of discrepancies and that perhaps the classifier needs to be tweaked for different brain regions which have different densities of cells labeled.

3) Figure 1—figure supplement 2: In aIC input excitatory tracing, 20% of starter neurons were found outside of IC, thus Pir. This is a significant number. The difference between aIC and mIC/pIC must result from Pir inclusion? What are the results of Pir input tracing? Or by using a simple retrograde tracer injection (cholera toxin subunit B) to Pir, which regions will be labeled? Would that affect aIC input tracing results? It is not clear to me whether the paired t-test is the right choice of analysis to answer the contaminated starting neuron question. Please also address this remaining concern. Reviewers suggested that adding more animals with better targeting would be the best solution to this problem. If that's not possible, comparing the results to existing data for PIR, e.g., from the online resources, would be helpful. If neither of these can address the issues, it would strengthen the conclusion to use more stringent spillover exclusion criteria.
