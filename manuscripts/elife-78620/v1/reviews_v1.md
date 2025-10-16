# Peer review - Round 1

Editors:
- Timothy Verstynen, https://ror.org/05x2bcf33 Carnegie Mellon University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78620.sa0](https://doi.org/10.7554/eLife.78620.sa0)

This manuscript provides a valuable set of findings that provide clarity on how striatal direct pathways regulate macroscopic information flow in the brain via the thalamus. The manuscript represents a powerful piece of evidence that will be relevant to researchers across many fields in neuroscience.


---

# Peer review - Round 1

Editors:
- Timothy Verstynen, https://ror.org/05x2bcf33 Carnegie Mellon University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78620.sa1](https://doi.org/10.7554/eLife.78620.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Neuromodulation of striatal D1 cells shapes BOLD fluctuations in anatomically connected thalamic and cortical regions" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Timothy Verstynen as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Michael Frank as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

1. Classifier as an evaluation method.

Reviewer 1 points out that the authors largely rely on a support vector machine (SVM) classifier to predict whether BOLD dynamics within atlas-defined regions reflect stimulation-on or stimulation-off windows. While in one way this is a conservative method for evaluating stimulation effects in the resting BOLD fluctuations, the authors largely report their findings as accuracies of the classifier. Figures 3-5 largely only report model accuracy effects, but we get no sense as to what exactly is happening to the BOLD dynamics in each region. The autocorrelation analysis (Figure 6) somewhat tries to get at this, but only for a subset of regions and the results are largely unclear (see comment below). As a result, a key goal of the study is left largely unaddressed for the reader: i.e. how do intra-region BOLD dynamics change with direct pathway stimulation? The study needs more effort put into this descriptive level of analysis to complement the rigorous classifier analysis.

This reviewer also suggests that the classifier method itself seems highly parameterized. The hctsa method returns 7702 features for each time series. It is unclear exactly how many were in the final set used to run the classification, but even if half of the features were removed, it would still make the classification problem highly overparameterized (e.g., 23 and 25 observations against thousands of features for the excitation and inhibition classifiers respectively). Assuming the authors used cross-validation correctly (which we need more information to support), the risk of inflated classification performance is mitigated. However, we need the details to be able to vet that the bias-variance tradeoff was resolved effectively in this model. In addition, it would be nice to know the features that loaded highly on the final model to resolve the questions about what changes in the local BOLD dynamics from excitation and inhibition of the direct pathway.

Along these same lines, Reviewer 3 points out that, in the first finding the authors show that D1 activation/inactivation produces reliable changes in the infected region (DMS), but most importantly, also produced changes in adjacent areas, suggesting intra-striatal communication. The way the data is presented and discussed appears to be confirmatory of what has been previously described with electrophysiological recordings. In their opinion, the most important part of this section would be to fully describe the differences between activation and inactivation groups. Is interesting that opposite manipulations of D1 receptors produced very similar maps of discrimination (Figure 3). Therefore, it would be necessary to discuss the meaning of obtaining similar classification accuracy indices with opposite manipulations. Perhaps, the use of SVM classifiers can be complemented with other analytical techniques to further disentangle the consequences of manipulating intrastriatal D1 receptors.

2. Variation across individuals

Reviewer 2 points out that while the methods adopted by the authors to acquire the data and evaluate the experimental manipulations are robust and the obtained results are compelling, the current analysis comes short of relating whether variation that can be estimated across the animals has an impact on these results. Specifically, the authors do not leverage the individual animal viral expression or impact on behavior to constrain and estimate the observed responses reported subsequently. Several reports in humans have used individual variability to estimate the relation between behavior and changes in the BOLD fMRI responses at rest, and a basic demonstration of this type of result has been achieved in mice. Applying a similar approach here would further strengthen the result reported here by identifying which regions are linked to the behavioral deficit (e.g., whether the primary motor cortex is linked to contraversive/ipsiversive rotations at the individual level).

This reviewer also highlights that it would be ideal to link the behavior of individual animals to changes in the fMRI signal. This requires an estimation of structure-function that is driven by each individual animal's expression map may enhance the current analysis approach by leveraging potential subtle expression variations to reveal whether the observed changes can be explained by the extent to which expression is different across animals. In addition, a quantification of the difference between the excitatory and inhibitory cohorts will rule out that differences in the impact on the fMRI signal were a result of unintentional group differences in expression extent. The authors should consider adding analyses that relate the individual animal's behavior to the results observed. Namely, whether the magnitude of change in contraversive/ipsiversive rotations is linked to classification-based or pairwise observed results. The authors should consider replicating the analyses conducted in humans to leverage individual variability. This will also strengthen the report by linking its result to human work.

3. Local stimulation effects in the striatum

Reviewer 1 thought that Figure 3 is quite confusing. The classifier is supposed to predict stimulation (excitation or inhibition) on vs. stimulation off (control) periods. This would predict a single number (balanced prediction accuracy) per striatal nuclei. Yet the heat maps shown in this figure show classification accuracies for both stimulation and control conditions. Where do the two numbers come from? Also, given the extremely limited short-range lateral connectivity in the striatum, why are the only stimulation effects observed not in the subnucleus being stimulated (Cpl,dm,cd), but for adjacent subnuclei (CPre, CPivmv) and *only* for excitation conditions? This lack of direct change in BOLD dynamics at the stimulated site seems important and largely ignored.

4. Quantifying viral expression

Reviewer 2 points out that a significant weakness in the current version of the manuscript is the lack of quantification of the viral expression. Currently, the authors do not provide enough information on the extent of coverage of viral expression on average or at the individual level. In particular, while the authors are careful to use the Allen Mouse Brain Connectivity atlas to constrain the fMRI results, they do not relate the specific expression extent, to clearly communicate to the readers, which regions within the striatum are likely to have better representation given the actual expression levels. A better presentation of the extent of the viral expression maps should be provided. The current exposition in Figure 1 is not sufficient to estimate the extent and consistency of expression across animals in each of the groups.

5. Time series effects

Reviewer 1 points out that the one attempt to characterize what happens in the intra-region BOLD dynamics is the autocorrelation analysis reported on page 11 and in Figure 6. However this analysis (a) only focuses on the thalamic nuclei (not also the cortical and the single striatal site shown to exhibit stimulation effects) and (b) only focuses on a few time series measures. Why this limited focus of both target (thalamic nuclei) and measure (first lag of the autocorrelation)? There are many measures for characterizing the temporal characteristics of autocorrelated series from the hctsa analysis. This selective focus seems both narrow and incomplete.

This concern is echoed in Reviewer 3's concern about the observation that thalamic but not cortical regions presented low-frequency fluctuations. What is the meaning of an increase in slow fluctuations? Why did D1 activation (and not inactivation) induced this effect? Are striatal sub-regions also presenting these slow fluctuations?

6. Connectivity results

Reviewer 1 found the changes in functional connectivity as a result of direct pathway stimulation (excitation and inhibition) are both fascinating and limited. There is a clear excitation/inhibition difference in effects, as shown in Figure 7 B-C. However, Figure 7B suggests something different than the change results shown in Figure 7C. It appears that the application of clozapine increases functional connectivity in the control mice (black line Figure 7B). This effect is exaggerated in the inhibition condition, but (most importantly) direct pathway excitation does not really reveal a significant change in the BOLD connectivity patterns. Now this does not change the authors' overall conclusions (connectivity is suppressed with direct pathway excitation relative to control mice), but the nuance of what is happening in the control mice is important for interpretation purposes: direct pathway excitation does not necessarily decrease functional connectivity but does not express the increase in connectivity observed from the application of clozapine. This needs to be elaborated more.

Along the same lines, Reviewer 1 points out that there is an interesting disconnect between the intra-region results and the inter-region (connectivity) results. It is clear that resting BOLD dynamics in thalamic nuclei that project back to the striatum, as well as more unimodal cortical areas, change from direct pathway stimulation in the dorsal caudate. Yet, only one cortical region (MOp) with significant functional connectivity changes overlaps with the set of nuclei that exhibit intra-region BOLD changes. This suggests that local BOLD dynamics and global connectivity are largely disconnected effects. Yet this seems to be largely ignored in the current work. It would be nice to see more analysis, and discussion, of the intra-region and inter-region stimulation effects.

Reviewer 2 points out that the authors do not use their own nor the Allen Institute data to carry out a formal structure-function analysis (following Stafford et al., 2014 PNAS, for example). This is critical since the authors wish to infer on the impact of their manipulation on both cortical and thalamic regions while the precise region in the striatum that they affect is never quantified. A better presentation of the extent of the viral expression maps should be provided. The current exposition in Figure 1 is not sufficient to estimate the extent and consistency of expression across animals in each of the groups. A formal structure-function analysis will significantly strengthen the current report by linking the expression extent (at the individual or cohort level) to anatomically connected regions.

This concern is echoed in Reviewer 3's comment that the second finding (Figure 4) indicates that thalamic regions forming "closed loops" with the striatum were more affected by chemogenetic manipulations. We knew from anatomical studies that the BG are part of anatomically segregated cortico-BG-thalamic loops. Therefore, it would be expected that these anatomical boundaries would somehow limit functional connectivity maps. Here again, we suggest that the manuscript would be improved with further analysis or discussion. For example, it would be interesting to perform further analysis relating the previous section (local striatal connectivity) with this one. In this section, several thalamic nuclei presented higher levels of classification accuracy, but in the previous section, the authors showed that DMS manipulation also produced the same effects in different intrastriatal regions. Therefore, it is not possible to know if the thalamic effects are related to the manipulation of D1 in the DMS or its adjacent regions.

This reviewer also points out that, in the third finding (Figure 5) the authors show that the most "sensitive" cortical regions to the manipulations were classified as "unimodal". This is an interesting result; however, it would be necessary to at least provide further discussion on its potential meaning. It is important to consider that the cortical regions with significant changes, for example, primary sensorimotor cortices, mainly target the dorsolateral, not the dorsomedial striatum. In this context, would it be possible to establish a new analysis to characterize potential correlations between cortical regions and striatal subregions?

Reviewer 3 identifies concerns about the potential changes in functional connectivity (FC) between the striatum and cortical and subcortical regions. Contrary to the results obtained with the SVM-based analytical tool, FC analysis revealed that D1 activation and inactivation produced opposite results, while D1 activation decreased FC in several cortical and subcortical regions, D1 inactivation increased it. While this set of data is clearly described, the implications of these relationships could be further discussed. For example, how do the authors explain that FC with SSp was not significantly changed with this analytical method, but was one of the most affected regions with the Balanced Classification Accuracy method?

Finally, Reviewer 3 points out that in rodents, the dorsal striatum is anatomically and functionally segregated into dorsomedial and dorsolateral, with the last one more related to sensorimotor functions. Please include in the discussion the potential implications of this segregation in the current set of data. Would the authors expect different results if D1 is manipulated in the DLS?

7. Links to behavior

Reviewer 3 noticed that there is no section in the discussion where the behavioral effects observed in figure 2 are contextualized in the massive set of BOLD results presented in the following sections. Do brain-behavior associations exist in this data set?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Neuromodulation of striatal D1 cells shapes BOLD fluctuations in anatomically connected thalamic and cortical regions" for further consideration by eLife. Your revised article has been evaluated by Michael Frank (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewer #1 (Recommendations for the authors):

The authors have done an excellent job addressing most, but not all, of my original concerns. I have one lingering major concern and one minor issue with the revised manuscript.

1. My original point regarding the interpretation of the classifier results as an evaluation method of the influence of D1 excitation/inhibition on the BOLD response remains somewhat unaddressed. The authors have done an incredible job providing many more details, particularly with the inclusion of the new Figure 6, which highlights how different timeseries features contribute to the classification accuracy. However, this does not really help to address the original question: what is changing with stimulation? In the abstract, the authors conclude "Our results provide a comprehensive understanding of how targeted cellular-level manipulations affect local BOLD dynamics at the macroscale, contributing to ongoing attempts to understand the influence of structure-function relationships in shaping inter-regional communication at subcortical and cortical levels." A similar sentence is made in the Discussion. But I am not entirely sure that this is correct. We know that there are *some* changes in the timeseries characteristics that allow for a classifier to reliably discern stimulation from control conditions, but the complexity of the feature space makes it nearly impossible to interpret the important question of "how". Exactly are the connectivity patterns changing? Is connectivity increasing or decreasing? Is the nature of the autocorrelative structure in the signal increasing or decreasing? Are the specific features that change uniform across regions or do they vary? This remains unanswered in the current version of the manuscript and leaves the reader scratching their head as to what to make of D1 excitation effects, other than to conclude that "something happens."
