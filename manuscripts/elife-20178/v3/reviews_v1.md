# Peer review - Round 1

Editors:
- Jack L Gallant, University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.20178.020](https://doi.org/10.7554/eLife.20178.020)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The heritability of multi-modal connectivity in human brain activity" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom, Jack Gallant (Reviewer #1), is a member of our Board or Reviewing Editors and the evaluation has been overseen by Sabine Kastner as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: David Glahn (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Although the Discussion highlighted some hesitation about the publication of this work in eLife, the reviewers have decided to ask for a revision, which should deal with (1) additional analyses, (2) novelty issues, (3) other smaller issues. Of particular concern is that we are not yet convinced that this work is sufficiently novel; the authors will have to make the case for that.

Summary:

This study examines genetic influences on resting state MRI and MEG connectivity. The article is clearly written and the data analysis procedures are reasonable as far as they go. However, the genetic influences on resting state have been reported several times using similar methods, and at this point it is unclear whether this paper is appropriate for publication in eLife, or rather whether it merely reflects an incremental increase in scientific knowledge. Furthermore, the current analyses appear to be insufficient. The MEG results are rather underpowered and many essential analytical controls are missing. After consultation the reviewers decided that the paper should be returned to the authors for revisions focusing on (1) elucidating the novel contributions of the work, (2) performing additional analysis as suggested and (3) dealing with a variety of smaller issues.

Essential revisions:

1) The genetic influences on resting state have been reported several times using similar methods. However, the current paper does not really include any detailed comparison of the current results with those reported previously, so it is difficult to judge the novelty of this contribution. In revision the authors should include a detailed discussion of precisely which aspects of the paper are novel. This may require further data analysis apart from what is requested as controls below. It would also be helpful if the authors would make more of an effort to explain some potential causal mechanisms that might underlie their reported relationships.

2) Additional analyses should be included to account for potential contamination of the FC data by confounding factors having nothing to do with cortical connectivity or communication, but which are nevertheless heritable. The obvious candidates here are body motion, head motion, eye movements, or other physiological factors.

3) The results are all based on one particular parcellation. Some evidence should be provided that the results do not depend on this particular choice. The optimal way to address this problem would be to rerun the analysis pipeline using several different parcellation schemes.

4) There appear to be several differences between the way that the fMRI and the MEG data were processed. These should be justified and explained, or a more consistent approach should be used.

Reviewer #1:

This is a fine study as far as it goes and it includes several good controls for potential contaminating factors (though these could be substantially improved). However, the paper is going to require revision and additional data analysis before it is suitable for publication.

Although the authors show THAT genetics influences FC, they provide no information about WHY genetics influences FC. Which of the many mechanisms that contribute to observed BOLD FC are influenced by genetics? As the authors note, several of the results reported here (such as the heritability of FC from EEG data) have been reported already in previous studies. It is claimed here that these previous studies are less interpretable than the current study. That may be true, but then the authors need to provide the interpretation. If not then this paper loses a lot of its potential novelty and impact and I am not sure that it will be suitable for publication in this venue. Some effort should be made to explain several of the more interesting and unusual effects as well. For example, it is stated that there is significant heritability in the alpha and beta bands of the MEG data but not in the theta band. Why? What is a plausible mechanism that would generate this pattern of results?

There is one major class of potential confounds which appear to be given short shrift here: potential contamination of the FC data by confounding factors having nothing to do with cortical connectivity or communication, but which are nevertheless heritable. The problem is that genetic factors might influence processes that are well known to influence correlations in MRI data (and likely MEG data as well). For example, if genetics causes some people to wiggle more in the magnet, that is obviously going to influence FC. (In fact I am fairly certain that I saw another study recently that reported just that effect, though unfortunately I am unable to find it now.)

To take just one specific example of the above concern, it is reported that the visual system has a high degree of FC in the MEG data. The most likely candidate here would be eye movements, which will clearly affect MEG correlations, and which may also be influenced by genetics. However, I didn't see any report here that the eyes were tracked properly, or that the eye tracking data were regressed out when calculating FC. It is precisely these sorts of potential confounds (i.e., genetic influences operating on behavior that in turn influences FC rather than operating on FC directly) that must be scrupulously accounted for before publication.

Perhaps one good way to get an intuitive handle on these sorts of potential indirect genetic influences would be to run separate analyses to determine the heritability of the various confounds that are known to affect FC, such as motion, eye movements, beamforming errors (in the MEG data). For that matter other factors that might affect FC indirectly might also be heritable. BOLD data taken directly off the scanner are non-Gaussian, and these are Gausianized during pre-processing by a necessarily imprecise procedure. Is the distribution of raw BOLD signals heritable? All these seem plausible, and all could potentially affect FC. A systematic analysis of these factors would seem to be critical for making any strong claims about direct genetic influences on FC.

Smaller issues:

The claims in the Abstract and Discussion are a bit over-stated in several places given the results because they do not make any reference to places where no heritability is found. For example, while effects in the MEG alpha and beta frequency bands are observed, this is not true for the theta frequency band.

The figures and the supplementary movies in this paper are rather poor, especially the connectivity figures. There are many excellent choices for visualization software these days.

Issues related to data analysis:

The pre-processing and data analysis procedures are necessarily complicated, and of course it is always possible that some decision that was made during those procedures might have biased the results. On the other hand, if we started requiring every single step to be addressed in multiple ways to ensure against this sort of bias then none of us would get anywhere! So in the next few paragraphs I only ask for further work on data analysis steps that I think could be particularly problematic, or where additional analysis might provide worthwhile enlightenment.

The entire data analysis procedure is based on the HCP ICA parcellation. It would inspire more confidence in the conclusions if some analysis was provided that showed whether the choice of parcellation scheme makes any difference on the results or the conclusions. I don't think that it would make much difference in the results if one compared the HCP ICA parcellation to, say, the Glasser HCP parcellation, because these are both fine-scale parcellations that are likely to include more spatial information than can really be supported by genetics data anyway. (In the case of the MEG data, the HCP ICA parcellation may very well have higher resolution than can be supported by either the genetics or the MEG.) It would be immensely helpful to know whether a coarser parcellation schemewould change the results, and I think that knowing the answer to this question might also help us address the question of why these apparent genetic influences are found.

It looks as if subject motion was removed during pre-processing in both the fMRI and the MEG data, but subject motion was still used as a regressor during ACE modeling in the fMRI data. Subject motion is a problem in both fMRI and MEG, so if it was a problem in the fMRI data even after pre-processing why was pre-processing sufficient for the MEG data? At a minimum it seems that it should also be included in the MEG modeling analysis.

Very small confusing issues:

This is a side point, but I find it surprising that it is useful/helpful to regress out the MR image reconstruction software version in ACE modeling. This suggests that these data really do live at the very limit of sensitivity, and that confounds and bias really can creep into the data even after pre-processing. It seems like the best practice would be to use the same version of the software to process all the data and I find it a bit worrisome that this was not done.

In Subsection “E. Three-component variance models” it is stated that the variance partitioning analysis addresses non-negative portions of the variance. Why do these procedures produce negative variance estimates at all? Is this just statistical error?

Reviewer #2:

Colclough and colleagues examine the genetic influences on resting state MRI and MEG connectivity in "The heritability of multi-modal connectivity in human brain activity." Subjects included 461 individuals with MRI data and a group of 61 primarily overlapping individuals with MEG data all from the Human Connectome Project. Subjects were from extended twin pairs or unrelated individuals. The goals of the article are to estimate the heritability and common genetic influences on resting state and MEG measures of connectivity. The article is clearly written and the analytic plan is both complex and reasonable. Unfortunately, the findings represent only an incremental increase in scientific knowledge, as the genetic influences on resting state have been reported several times using conceptually similar methods. While the MEG results are novel, that analysis is rather underpowered, as the authors appropriately note in the Discussion. Thus, while I believe the findings should be reported, the authors should either describe the work as replication or conduct additional analyses that will increase novelty.

Reviewer #3:

This is an excellent article, which combines state-or-the-art resting-state MEG analysis methods with new approaches to assessing heritability and environmental facts in this type of electrophysiological dataset. As such it both helps to drive the field forward and will be of general interest to the eLife readership. I recommend publication after the following issues are addressed:

1) I think the authors should clarify why 39 cortical regions are chosen, as opposed to other common parcellation schemes, which often have 50-100 regions.

2) I'm surprised that the Authors did not at least attempt to reconstruct networks in the higher gamma band. Why only theta/alpha/beta?

3) One of my main concerns is the use of partial correlations in the FMRI analysis and simple correlations in the MEG network analysis. Why this difference? The Authors cite two of their own papers as justification but this not particularly convincing. Could we have a short justification here?

4) The authors state that the beta-band "exhibits broad connectivity over the whole cortex". That doesn't really appear to be the case looking at Figure 1. In ay case, what does that statement actually mean – it's quite a woolly phrase that is not backed up by any kind of quantification.

5) The authors look at both genetic and environmental factors in terms of contribution to signal power (in both FMRI and MEG), partly as a control for these as confounds in the connectivity analyses, but also as interesting exploratory analyses in their own right. I have two concerns here. 1) Can the authors please describe how "power" was assessed in the FMRI signal? I assume this is some measure of temporal variation around the mean of the voxel time series? 2) For the MEG, the power passed by a beamformer in an RSN analysis can be quite dependent on geometric effects (even after weights normalisation). Wouldn't a better measure of 'activity" in the MEG amplitude envelopes be some measure of temporal variability? The standard deviation (SD) is often used, but the SD of the virtual-sensor and the Mean are often correlated in beamformer reconstructions, so a better measure might be some proportional change (e.g. SD/Mean). "Activity" in both the FMRI and MEG time series could thus be assessed using the same (or very similar) metric.

6) In the ACE model, quite a few nuisance covariates are regressed out of the model before heritability/environmental effects were assessed. How were these parameters (and their second-order versions) chosen? In addition, when regressing out some many parameters, is there an issue with statistical power in the MEG analyses as some of the groups only have relatively few subjects (i.e. 11 monozygotic twin pairs)?

7) Finally, with these "nuisance" regressors Is there a potential problem with interaction with heritability? For example age is 100% matched in the twin-pairs, but is presumably not matched for the non-related pairings.
