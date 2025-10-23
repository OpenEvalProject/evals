# Peer review - Round 1

Editors:
- Chris I Baker, https://ror.org/04xeg9z08 National Institute of Mental Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84086.sa0](https://doi.org/10.7554/eLife.84086.sa0)

This important study combines behavioral and imaging experiments to understand how levels of important brain chemicals shape the processing of information in the brain in children and young adults. The sample size and data quality are outstanding and some of the data are convincing. However, there are important caveats for some of the results, as discussed by the authors, and future replication will be important to fully substantiate the findings. This work will be of interest to neuroscientists, psychologists, and neuroimaging researchers investigating the developing brain in health and disease.


---

# Peer review - Round 1

Editors:
- Chris I Baker, https://ror.org/04xeg9z08 National Institute of Mental Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84086.sa1](https://doi.org/10.7554/eLife.84086.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Dissecting the chain of information processing and its interplay with neurochemicals and fluid intelligence across development" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Chris Baker as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Georg Oeltzschner (Reviewer #1); Reuben Rideaux (Reviewer #2); Alexander Weigard (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

While the reviewers highlight many strengths of the work including the extensive nature of the dataset, they raise some substantial concerns that significantly weaken the interpretability of the results. There are two major areas of concern.

1) There is a need for more transparency regarding the analytic decisions made in the manuscript and greater justification for those decisions. While there are aspects of compelling robustness (e.g., large sample size, test re-test replication), these are weakened by factors suggesting unreliability (e.g., multiple comparisons, liberal α values, selective reporting). All three reviewers have provided clear and concrete suggestions for improving the reporting of the methods and analyses and the implicit assumptions made in those decisions.

R1's comment regarding the choice of metabolite quantification methods provides a good example. There are many different methods for MRS processing and quantification, and each decision in the pipeline produces a different set of estimates at the end. While there may be justifiable reasons for using the analysis presented in the manuscript, these decisions are currently opaque, which prevents an assessment of their legitimacy. Reporting the results of using alternative processing/quantification methods (e.g., those previously used by the group on this dataset) would give an indication of the robustness of the findings.

2) Reviewer 3 highlights a number of concerns about the interpretation and use of the DDM parameters and the associated mediation analyses. In particular, they highlight the weak conceptual link between the t0 parameter and intelligence in prior work and are concerned about the α value of 0.10 that seems to have been chosen post hoc in the mediation analyses. The claims with regard to both of these aspects of the manuscript may need to be weakened.

In addition, you should include greater consideration of age trajectories of MRS-derived metabolite estimates during childhood and early adulthood.

Reviewer #1 (Recommendations for the authors):

1. I have found the MRS methodological section to be largely inadequate at this stage – there is a considerable lack of detail regarding acquisition and data analysis, as well as some unresolved confusion, particularly with respect to the exact corrections being made. In addition, the terminology is a little ambiguous and potentially misleading.

a. "Absolute neurochemical concentrations were then scaled based on the structural properties of the selected regions and based on the predefined values shown in MRS-eq1 and MRS-eq2 (see below) (84); these predefined scaling values were therefore determined before the data collection." This sentence is very troubling and unclear, particularly the part "these predefined scaling values were therefore determined before the data collection". Tissue correction of water-scaled MRS levels is done on a subject-specific basis, i.e. by co-registering the MRS voxel to the structural image, and determining the (subject-specific) fractional tissue volumes for GM/WM/CSF. You describe how you have implemented precisely this routine – and it is, therefore, difficult for me to understand why you state "the scaling values were determined before the data collection". Does this mean that co-registration has only been done once, and the segmentation is then assumed to be valid (and identical) for all subjects? This would counteract the benefits of individual tissue and relaxation correction. Please clarify, and if necessary, please repeat the analysis with subject-specific tissue and relaxation correction.

b. Generally, the term "absolute concentrations" is advised against, because absolute quantification relies on a lot of assumptions. As stated in a recent consensus paper on MRS terminology: "The term absolute quantification was originally coined for the conversion to standard concentration units, where the conversion includes all corrections needed based on measurements and calibrations for the currently reported case to contrast with relative quantification. However, this narrow meaning is an idealization that normally cannot be realized in practice, and "absolute quantitation" today is also used for plain conversion to standard units with calibrations from earlier studies or literature values, but this usage is not encouraged" (https://onlinelibrary.wiley.com/doi/10.1002/nbm.4347).

c. In this paper, you are using the term "absolute neurochemical concentrations" equivalent to un-corrected metabolite estimates with respect to the internal tissue water, as output by LCModel, starting with the sentence "Absolute neurochemical concentrations were extracted from the spectra using a water signal as an internal concentration reference". This is unclear at best, and misleading at worst, and should be changed to avoid confusion. You need to explicitly state that you start with the "raw" metabolite-to-water amplitude ratios that LCModel returns, and describe in greater detail how they are produced. By default, LCModel assumes pure white matter as water concentration reference, and already performs an extremely basic relaxation correction using the parameters WCONC, ATTH2O, and ATTMET. Please describe how all of these parameters were set in the control file.

d. Likewise, the term "scaling" is not often used to describe the procedure of tissue and relaxation corrections. Please use the appropriate term "correction".

e. Quality control. You mention that cases with CRLB>50% or SNR or concentration value beyond 3 SD were excluded from further analyses. How many cases were excluded according to each criterion? Is Figure 1 showing the spectra before or after exclusion? If a GABA CRLB was >50%, was the entire spectrum discarded, or did you keep the Glu value (which was likely never >50%)?

f. There is no mention of the MRI field strength, vendor, or scanner type. The MRS paragraph gives it away with the sentence "Simulations were performed using the same RF pulses and sequence timings as in the 3T system described above", but the system is not described above (unlike in the other papers published with identical methods sections). Please also provide more information about the MRspa process, specifically about the processing steps that were being taken (coil combination, alignment of individual transients, etc.).

g. The experimental description is a little misleading. If my calculations are correct, the pure measurement time per voxel should have been roughly 2 minutes, but you state that sequence planning and shimming took 10-15 minutes. This is because you don't mention the acquisition of the water T2 series in every participant, except for the one paragraph during data processing.

h. Please show a complete LCModel fit, not just a single GABA and Glu model. This should include the spectrum itself (primarily to judge single-spectrum SNR), the fit, the residual, the baseline estimation, and the individual contributions from all basis functions (for example, as a stacked plot).

i. To illustrate the variability of the GABA and Glu fits, you could consider showing their mean +/- SD as well, not just a single example (or even all of them on top of each other).

2. Introduction

a. "In other words, do the associations between frontoparietal neurochemicals and visuomotor processing is replicated across different tasks such as numerical processing (Figure 1, Task 2) and mental rotation (Figure 1, Task 3)?"- This should probably read "replicate across different tasks".

b. Reference (34) in "For example, it is known that neurochemical changes may precede anatomic changes (34)" is a study on brain tumors. It is a bit of a stretch to derive from this a "unique predictive ability of MRS" to discern how neurochemicals shape the developmental trajectory of neurobiological processes. I would suggest removing this particular reference – or adding ones that are more relevant to development and metabolite age trajectories (e.g., https://pubmed.ncbi.nlm.nih.gov/34061022/).

3. Figures

a. The caption of Figure 5 includes descriptions of panels A-D, but only shows three panels A-C.

Reviewer #2 (Recommendations for the authors):

Line 105: "…explained current and predicted future developmental changes in numerical cognition…" – I think it would be more accurate to state that ref 26 found a relationship between GABA/Glu concentration and mathematical achievement.

Figure 1a: Are these examples of anatomical T1-weighted images? I think more information on what is being shown in this panel would be useful in the figure caption. Also, the contrast seems quite low, these images may be easier to interpret if the luminance is increased.

Figure 1: The resolution of this figure is very low, which makes it difficult to assess it. For example, the text below the attention network task is barely legible.

Line 129: "In other words, do the associations between frontoparietal neurochemicals and visuomotor processing is replicated…" – a typo here.

Line 134: "A more optimal and informative way to address these questions is by using…" This is a strange way to begin a paragraph given that you have not discussed an alternative – less optimal – way of addressing those questions in the previous paragraph. Consider rewriting for clarity.

Line 139: "Therefore, it is possible to utilize and extend this unique predictive ability of MRS to discern which of these key neurobiological processes (cognitive, decision, visuomotor) are shaped by highly specialized neurochemical concentration across development." – This language seems to imply that finding a correlation between MRS detected metabolite concentrations and task performance is indicative of a causal relationship. I think it's important to be clear that correlations, even those that are predictive of future states, are not necessarily indicative of causal relationships.

Supplementary File 2: This file could be made clearer. Including more than two plots on each page, and grouping them according to either task or model parameters would allow for easier comparison. Some of the y-axis labels have typos, e.g., DISTANCEFARMINUSCLOSE, which I think are probably due to the way MATLAB treats underscores in text. Perhaps try using different clearer or correct these issues in a separate figure editing package. I think it would be useful to include an explanation of all the terms (e.g., alerting, orienting, executive, etc.) at the top of the file.

A large number of correlations were tested in this study. I appreciate that the authors performed an FDR correction and tested the test-retest reliability with a 1.5-year gap. I think that it would also be useful to see the distribution of all the correlation values, i.e., in a histogram, to get an idea of how distinguishable those that were categorized as meaningful are from those that were categorized as not meaningful.

I understand the choice of colour schemes for the scatterplots in the main text (blue and red for excitation and inhibition, respectively), however, the individual datapoints are difficult to parse between groups because they are all the same colour and semi-transparent. To improve the clarity of the plots, you could use different colours for each group, or something similar. Also, making the dots smaller will reduce the overlap and probably make them easier to distinguish from one another.

Figures 2-4: Please indicate the units of the x and y labels. Also, please indicate in the figure caption whether higher scores in visuomotor processing are associated with better or worse task performance.

Figures 2-4: "For visualization purposes, we did not control for boundary separation and mean drift rate when plotting these panels." – I don't understand how not controlling for the variability helps visualization, could the authors please clarify?

The authors find a correlation between IPS GABA and Glu and visuomotor processing in three different tasks. It would be interesting to test whether there is independent variability explained by the neurotransmitters in each task or not. For example, how correlated are the visuomotor processing scores between tasks, and if you control for the variability in one/two tasks, is there still a correlation between GABA/Glu and visuomotor processing in the third task?

Line 367: "These findings suggest that the relationship between IPS glutamate and GABA and visuomotor processing across development is task-independent." – This is related to the previous comment. This may have very little to do with GABA/Glu and more to do with the reliability of measuring the same latent construct with these three tasks. I think that the analysis suggested above could help to test this and to put this assertion into a better context.

A recent study found evidence for a brain-wide positive relationship between GABA and Glu concentration in adults (Rideaux et al., 2022, NeuroImage). Thus, one might predict that if GABA were positively correlated with task performance, then Glu would also be positively correlated. By contrast, in the current study it appears that for the majority of correlations between GABA and task performance, there appears to be an inverse relationship with Glu. This seems quite interesting, could the authors speak to this? For example, does the relationship between GABA and Glu change with age?

The authors found relationships between IPS GABA/Glu and task performance, but not MFG GABA/Glu. This could be due to poorer signal-to-noise in the MFG measurements. Can the authors test this possibility by comparing measures of signal quality between the voxel locations, i.e., FWHM, CRLB, SNR, and fitting residuals?

Line 310: "Since we identified a strong and task-independent developmental effect between IPS neurochemicals and visuomotor processing…" – By what categorization method is this effect strong? Most of the β values seem relatively weak (e.g., between 0.15-0.20). Perhaps the authors mean reliable?

Line 447: "…through the visuomotor resting-state connectivity depending on the individual's developmental stage." – This claim relies on both positive results, e.g., evidence of a relationship at some ages, and negative results, e.g., evidence of no relationship at other ages. However, the latter can only be established by directly testing the likelihood of the null hypothesis, e.g., with Bayesian statistics.

The paragraph starting at line 461: Related to the above point, several explanations are provided for why the relationship was only found for older participants. Another explanation is that the data may have been noisier for younger participants which led to a failure to detect the relationship.

Please provide a plot showing the positioning of the voxels, ideally with the degree of overlap between participants.

Please report the following MRS information: spectral width, number of data points acquired, and number of water-unsuppressed averages.

Please report the phase and frequency alignment method used on subspectra prior to averaging.

Please report the test-retest reliability of the GABA and Glu concentration estimates and compare them with previously reported test-retest reliability studies, e.g., Saleh et al., 2016, Magn. Reson. Mater. Phys. Biol. Med.

It is reported in the Methods that metabolite estimates were rejected as outliers prior to performing tissue correction. I think that tissue correction should be performed prior to outlier rejection.

Line 682: "…as this helped to assess the whether the results.." – typo.

Line 713: "…but this did not survive the neurochemical and neurotransmitter specificity…" – What is the difference between neurochemical and neurotransmitter specificity?

Please report the order in which participants performed the 3 tasks (was it always the same, randomized, or counterbalanced?). Related to this, FDR correct was performed on the attention network task correlations, but not on the subsequent "replication" correlations with the other two tasks (digit comparison and mental rotation). Could the authors please specify whether analyses were performed on the attention network task, prior to analysing the correlations between GABA/Glu and the other two tasks?

Line 760: "Since we obtained the same pattern of findings regarding visuomotor processing across Task 1-3 which was one of our earlier aims was addressed…" – typo.

Line 764: "zscored" – hyphenate.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Dissecting the chain of information processing and its interplay with neurochemicals and fluid intelligence across development" for further consideration by eLife. Your revised article has been evaluated by two of the original reviewers and by Chris Baker as Senior/Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below.

While the reviewers appreciate the detailed responses to the initial comments, there remain a number of specific issues that you need to address in a revision (see detailed comments from the two reviewers below). In particular, both reviewers think you need to be more open about the limitations of the data and analyses and temper some of the claims. This applies to issues such as correlations between GABA/Glu and task performance (R1), analyses of signal quality (R1), and mediation analyses (R2).

Additional analyses and careful revisions will be required for a positive decision on the manuscript.

Reviewer #2 (Recommendations for the authors):

The revised manuscript is an improvement on the original and the authors have addressed most of my previous reviews. However, there remain a number of outstanding issues, which will need to be addressed.

There are both red and pink data points in Figures 2-6, yet these don't appear to be labelled or described. Please fix this if it is a visualization error, otherwise please explain the distinction.

The authors misunderstood my previous request. I wasn't asking whether task performance is correlated. I had asked if there were independent relationships between GABA and task performance and Glu and task performance. For example, if you partial out the variability of GABA from Glu, does the relationship between Glu and task performance disappear? If so, this would make it difficult to infer specific associations between GABA/Glu and these tasks. In particular, Glu and GABA measurements tend to share variance, due to both metabolic (e.g., synthesis cycles) and non-metabolic factors (e.g., signal quality, frequency drift, subject age). If task performance is associated with this shared pool of GABA-Glu variance, then it is difficult to say which neurotransmitter is involved or (worse) if the task isn't simply correlated with the variance associated with non-metabolic factors. I think this is an important point and should be addressed.

The authors found that the signal quality in MFG was significantly poorer than that in IPS, as indicated by multiple indicators of signal quality. Please report this in the main text of the manuscript and acknowledge that this could explain why a relationship was not detected between MFG GABA/Glu and task performance. I appreciate that the authors feel confident that this is not the explanation; however, I think it's important that readers be made aware of the significantly lower signal quality of the MFG spectra.

The authors indicate that they are confident that the MRS measurements from all age groups have sufficient signal quality to detect meaningful relationships with their additional measures because they have excluded the datasets with poorest signal quality. This point is also offered in R2.R11. Matching the datasets in terms of their minimum signal quality is not sufficient to show that signal quality differences cannot explain the failure to detect relationships with other measurements. To make this claim, the authors need to demonstrate that the average signal quality is similar between groups. Please compare the average signal quality between groups, as was done between IPS and MFG in R2.R11. and report whether there are significant differences in the main text of the manuscript. If the average signal quality is significantly lower in groups where relationships were not detected, please acknowledge that lower signal quality may explain the failure to detect these relationships.

Please increase the luminance of the T1-weighted images to make the structure more visible and provide axial, sagittal, and coronal views for each voxel.

I think that the authors have misinterpreted my request – I agree that LCModel is an established method of metabolite quantification. I requested that the authors show the test-retest reliability of the GABA/Glu measurements for two reasons: (1) this is useful comparative information regarding MRS measurements and will be of interest to a broad range of readers and (2) because it provides the reader with an indication of the dynamic reliability/consistency of these measurements, which is influenced by many factors other than the quantification algorithm applied. Thus, could the authors please provide the test-retest reliability of the measurements (not simply the p-values for the correlation between them)?

Reviewer #3 (Recommendations for the authors):

In my view, the authors were moderately responsive to reviewer comments. I appreciate the authors' clarifications of prior work on DDM parameters and intelligence, the motivation for the supplemental experiment, and the resting state fMRI analysis procedures. I also think that the addition of the parameter correlation tables and the supplemental EFA increase confidence that the Ter parameter being measured is a task-general construct. I cannot speak as to whether the additional details about the MRS aspects of the study would impact the other reviewers' concerns, but it does seem like there is now greater transparency about the MRS procedures. I still disagree with the choice to investigate DDM parameters across the three tasks as three manifest variables rather than a single latent variable and the choice to visualize effects by binning ages rather than showing age as a continuous factor, but in both cases, I could see why there are reasonable arguments for the choices the authors made. However, I still have several concerns that I do not think were adequately addressed.

Simply showing the fits of nonlinear models to age differences in DDM parameter values in supplemental materials does not really address the possibility that non-linear effects of age could impact the main analyses reported in the paper, in which linear age appears to moderate the associations between DDM parameter values and MRS measures. There appears to be clear nonlinearity in relationships between age and Ter, the parameter that received the greatest focus. Unless there is a clear reason why sensitivity analyses that include nonlinear age terms would not be possible, such sensitivity analyses would be very valuable for determining whether the primary findings of the study are robust to these considerations.

The evidence from the mediation analysis is still concerningly weak. The authors now acknowledge the post hoc nature of the analyses and the liberal, uncorrected α level (although the other reason for concern, the inconsistency of effects across age groups, does not seem to be acknowledged as a limitation of the evidence for these effects). However, the mediation effects are still framed as a central claim of the paper. I think it makes sense to report the mediation results for completeness and to describe them as preliminary findings that could be replicated, but given the weakness of the evidence I don't think it makes sense to describe these results as a central finding. For example, the statement in the abstract that "We showed that fluid intelligence performance is explained by IPS GABA and glutamate and is mediated by visuomotor processing" seems like much too strong of a claim given the available evidence and the inconsistency in the details of the mediation effects across age groups. The age moderation effects of associations between DDM parameters and MRS measures that are reported seem to be robust and interesting in their own right, which makes me question the need to highlight a mediation analysis that provides evidence that, in my view, can be thought of as preliminary at best.

I appreciate the authors' addition of key details about how the DDM parameters were estimated. It seems like several of these details would be appropriate to mention as limitations in the discussion, including the relatively low number of trials and the high accuracy rate of the tasks, both of which can negatively impact the reliability of parameter estimates. However, a parameter recovery study would greatly increase confidence in the assumption that these features of the task data did not impede the accurate estimation of DDM parameters.
