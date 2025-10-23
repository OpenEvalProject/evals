# Peer review - Round 1

Editors:
- Gabrielle T Belz, https://ror.org/00rqy9422 University of Queensland Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69157.sa0](https://doi.org/10.7554/eLife.69157.sa0)

This paper describes a newly developed, publicly available algorithm (iROAR) that was tested on pre-exisiting datasets and is of interest to T and B cell immunologists who perform repertoire analysis via multiplex PCR based techniques. iROAR utilises naturally occurring non-functional sequences to improve and partially correct the amplification bias inherent in multiplex PCR based sequencing technologies.


---

# Peer review - Round 1

Editors:
- Gabrielle T Belz, https://ror.org/00rqy9422 University of Queensland Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69157.sa1](https://doi.org/10.7554/eLife.69157.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "The use of non-functional clonotypes as a natural spike-in for multiplex PCR bias correction in immune receptor repertoire profiling" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Tadatsugu Taniguchi as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Lindsay Cowell (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers are enthusiastic about this manuscript. They have identified a number of issues that require clarification and are generally thought to be important to reach the broad immunology audience.

Reviewer #1 (Recommendations for the authors):

The conclusions are mostly well supported. However, there are some concerns that should be addressed before this paper is accepted for publication.

The authors have kindly provided the iROAR software free for non-profit use on Github. As this entire study was performed to validate and share this software to other scientists, I would suggest that the iROAR documentation be improved such that it can be used by a wide audience. More detailed instructions for use and perhaps even a step by step example on how to replicate the results in this study included in the documentation would be very helpful.

The authors utilised pre-existing datasets that performed both multiplex PCR (high bias) and 5'-RACE (low bias) on the same sample to test the functionality of iROAR. The iROAR algorithm improved the PCR bias in repertoires that were obtained by multiplex PCR which better correlated with the same repertoire determined by 5'-RACE. It is important to note that although the iROAR algorithm improved PCR bias, it is by no means perfect and cannot substitute for a low bias approach. Even for a 5'-RACE repertoire in which artificial bias was introduced in silico, iROAR improved the correlation of the in silico biased 5'-RACE from R2 = 0.4052 to R2 = 0.6286 which is an improvement but certainly cannot substitute for a repertoire that was determined using a low bias approach.

The authors very nicely showed the extent of amplification bias when using multiplex PCR based technologies by plotting the OAR distributions in Figure 2A and Figure 2B. It would be very informative to plot the iROAR corrected OAR and OAR distributions as well in order to visualise the improvement in bias correction in the same way..

The authors state that an F-test was performed to compare OAR distributions in Figure 2A. Please state exactly which F-test was used to calculate statistical significance.

The authors state that they use a z-test to exclude outliers from the OAR calculation that may have resulted from large clonotypes introduced by PCR bias or naturally generated from clonal expansions. The authors should describe further how this affects analysis of repertoires in which large clonal expansions are expected such as during an antiviral immune response.

The authors nicely compared clonal frequency between iROAR corrected and 5'-RACE repertoires in Figure 4B-D. I think it would also be important to know how the iROAR algorithm would affect other measurements commonly used when analysing TCR/BCR repertoires. For example, does iROAR also affect measurements of diversity? This would be especially useful when comparing corrected repertoires vs. 5'-RACE.

As per eLife policy, "Regardless of whether authors use original data or are reusing data available from public repositories, they must provide program code, scripts for statistical packages, and other documentation sufficient to allow an informed researcher to precisely reproduce all published results." I would recommend that the authors very much improve the documentation provided in the Github repository for iROAR such that anyone can reproduce the published results before publication. Additionally, eLife suggests that the authors should license their code using an open source license.

Line 158: What do you mean by z-test? Can you explain under which circumstances you can decide to exclude abnormally large clonotypes? How has this threshold been calculated? Would this negatively affect measurements of OAR during an immune response such as viral infections where large clonotypes might be observed?

Line 167, 2.5 reads is a minimal sufficient sequencing coverage. Does the package provide this quality control check? This would be useful information that could be included in the manuscript as well as within iROAR documentation.

Line 203 Figure 4: Can the authors also generate the OAR distributions (a per Figure 2B) for these datasets before and after iROAR? Would be very useful as a comparison between 5' RACE and other multiplex PCR methods as well as to assess the efficacy of iROAR in correcting bias.

Line 219, How does the in silico introduced bias look with regards to the OAR? Can you generate the OAR distributions of in silico biased and unbiased samples using the same graphing method in Figure2B?

The Discussion section needs much more discussion on its applications as well as limitations. Ie., how does the software deal with instances where clonal expansions occur in cell clones that are also bearing a non-functional receptor? How does this affect the OAR calculation?

Reviewer #2 (Recommendations for the authors):

Enthusiasm is dampened by the fact that the proposed method is not directly compared to the gold standard of biological spike-ins. The results would be stronger if the authors could use data generated with a biological spike-in and compare correction using data from the spike-in versus their proposed algorithm. If such a data set is publicly available or can be obtained by request, this should be done. If such a data set cannot be obtained, then the Discussion section should directly address the fact that this gold standard validation remains to be done.

Figure 2:

– More interpretation of the results is needed in the Discussion. For example, Figure 2a appears to show that for VMPlex and VJMPlex, most genes suffer from under- rather than over-amplification. This seems unexpected. I would have expected "zero-sum-game" behavior. Also, it is surprising that VJMPlex shows less overall bias than VMPlex. Does this make sense? Why or why not? I think a plot like Figure 1 is needed for VMPlex and VJMPlex to ensure that the base assumption underlying OAR calculation holds in the same way and to the same degree across the three technologies.

– Regarding the input data: "for each method type 15 PBMC TCR repertoires were chosen randomly from" and this is followed by a list of 11 study/project identifiers. More information is needed. Fifteen seems like a small number, but it depends on the details. How do the 11 studies distribute across the three methods? How many studies were included in each method? Were 15 repertoires total used for each method? Or 15 from each study? Did the different studies within a method use the same primer set? The same depth coverage?

– How much within-study between-repertoire variability is there for a single V or J gene? And how much variability is there across studies? It seems important to understand this basic behavior of the metric before pooling into a single figure, as the pooling can average out important behavior.

Figure 3: More interpretation of the results is needed.

– In Figure 3a, the range of values is greater for TRBV and IGHV. Could this be attributed to a larger number of genes or primers, or to more sequence variability (and presumably therefore greater variability in primer hybridization efficiency)?

– In Figure 3b, while there may be no difference in the mean or median OAR value across cell types, there does appear to be a difference in the range, with PBMCs and THs showing much less variability than the other cell types. What could explain this? Is this an artifact of the way samples were pooled for the figure? Are both donors represented in all six cell types? Or does this point to some interesting biology? If the latter, then exploration of this is understandably beyond the scope of this paper, but it should be mentioned and possible explanations should be put forward.

Lines 197 – "the procedure can be recursively repeated with a modified normalization coefficient defined as described coefficient raised to the power of a number in the range from 0 to 1.": How is the value of this number determined? This sounds like an optimization procedure, in which case much more information is needed. In particular: what algorithm was used? what is the objective function? What are the stopping criteria? In which of the presented results was this procedure applied?

Line 87 "constant during a lifetime": this needs to be substantiated with either a reference or data. The authors show relevant data in Supplementary Figure 1, but there is no description of how the data shown in the figure were derived. For example: are all data points from a single study? do all data points used in a single regression (i.e., all those corresponding to the same gene segment) derive from the same patient? do all data in the figure derive from one single patient? what sequencing protocol was used? Has the proposed correction been applied? The strength of the claim should reflect the strength of the data. Note: I don't think the truth of this claim is a requirement for the proposed method to be valid. So if the data are such that the statement cannot be generalized to "all" repertoires, I don't see this as a problem.

Line 89 "reproducible": reproducible in what way? Over multiple aliquots of a sample? Over multiple samples for the same person? Over multiple people?

Figure 1: Is the same stability observed for the sequencing protocols with even more amplification bias (VMPlex and VJMPlex)?

Lines 102 – 109: this paragraph is not clearly written, but it is the heart of the manuscript. The paragraph reads as if only the two terms with summations are based on out-of-frame rearrangements. I assume all four terms are based on out-of-frame rearrangements? Because otherwise the equation does not make sense …. Also, I recommend removing "a percentage of" in line 105, as this reads as if there is a percentage in the numerator of the numerator (i.e., the RC(Vi) term). Finally, in line 107, I assume you mean PCR amplification instead of clonal expansion?

Figure 2: More information about the data is needed. Specific details are below.

Lines 149 – 153 starting with "the average population frequencies": It isn't clear what is meant by "average population frequencies", and it isn't clear what the rest of the paragraph implies about calculations described in the paper and results displayed in the figures. It sounds as if different repertoires may have been subjected to different calculations.

Lines 157 – 158: The last sentence of this paragraph suggests that V- or J-genes with large or small relative frequencies may have been excluded. More details are needed. Were only large clones excluded? How were they identified for exclusion? By what method and what exclusion threshold was used? How many were excluded from each repertoire? If more than "a few", then before and after data need to be shown for some repertoires to show how this impacts the OAR distributions and averages.

Lines 167 – 169: how is "adequate" defined? Within the 10% error range discussed in the context of Supplemental Figure 3?

Lines 257 – 262: These sentences suggest that the proposed approach is more reliable than biological spike-ins. This should be substantiated before being claimed. The authors state that this is because "the impact of CDR3 structure" is minimized. Why is this? Because the number of out-of-frame rearrangements is much much larger than the number of cell-line or synthetic spike-ins and so captures more CDR3 diversity? Or some other reason? More explanation of why this is being suggested should be given and the wording should make clear that this is an untested hypothesis.
