# Peer review - Round 1

Editors:
- David Kleinfeld, University of California, San Diego , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.10696.017](https://doi.org/10.7554/eLife.10696.017)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Prediction of primary somatosensory neuron activity during active tactile exploration" for peer review at eLife. Your submission has been favorably evaluated by Eve Marder (Senior editor), a Reviewing editor, and three reviewers.

The Reviewing editor and the reviewers agree that this is a potentially very important work that defines the features of whisking and vibrissa contact that cause a trigeminal ganglion neuron to spike. Further, while this latter topic has been explored extensively in anesthetized animals, there is limited work in the awake case. Thus a study of parameters that lead to spiking in the awake case would be a welcome contribution to the vibrissa field. Yet there are major weaknesses in the current submission that must be addressed, with additional analysis and potentially new experiments, before we can proceed further.

Major issues:

The choice of the angular variable was absolute angle – which is likely to be a poor choice. The analysis should be redone in terms of deflection angle. The change in position of the mystacial pad also needs to be taken into account in the analysis, as noted by multiple reviewers. Related to this is a need to re-evaluate claims, as noted by reviewer 3 "[…]only 50% of the data shows a drop in performance when angle is used instead of curvature. The other 50% seems to perform as well for angle as it does for curvature. The conclusion that curvature is therefore the single most important parameter seems not to be supported by the data." This requires reanalysis, yet also may require some additional data to increase the spike count.

The application of the GLM was done with relatively few spikes, about 550 or 275 each for training and testing sets for 8 feature parameters and an unstated number of spike history parameters, which gives the editor pause. It would be thus imperative for the author to show the feature vector and the history term for at least a few units, as opposed to just predictions. In fact, the feature vector is a main point of such an analysis. Further, while the recorded data show clear cycle-by-cycle whisks (Figure 1), and "whisking" cells in the trigeminal ganglion faithfully respond on a cycle-by-cycle basis, these fast changes do not appear in the predicted spike rates of Figure 2. The reason for this omission, as pointed out by Reviewer #1, needs to be explained.

Further on the topic of analysis, Reviewer #2 notes "The authors use the poor performance of angle GLMs during active pole exploration as evidence that curvature changes are what drive PWNs. But it is known that touch dominates PWN spiking responses, so including touch periods when assessing angle GLM decoding will trivially result in very low GLM angle performance. More interesting would be comparing the performance of angle GLMs during non-touch, free whisking periods with performance of curvature GLMs during touch periods." The critical issue is to determine if there is a big difference between passive and active states or if, within strong statistics, there is not a big difference. This requires reanalysis, yet also may require some additional data to increase the spike count.

Please read through the attached thorough and very thoughtful reviews by three of your colleagues and please address all of the issues raised in a cover letter to accompany the resubmitted manuscript.

Reviewer #1:

This is an elegant work, addressing a crucial question – what do sensory neurons code during active exploration and touch – in a professional manner. The paradigm is simple and clear, and the paper is well written (for the most part), expressing clear thinking and straight-forward reasoning. This impressive work can potentially advance the understanding of sensory coding significantly. Yet, in its current form there is a danger that the paper will instead increase the confusion in the field – this is due to several major flaws that need to be carefully addressed.

1) The choice of the angular variable for analysis. The authors analyze the angle of the whisker relative to the head – let's call this the "absolute angle" here. There are 2 problems with it. One, portions of the pad rotate with significant angles during active whisking such that the absolute angle of a whisker changes but this has no effect on the shaft-follicle mechanical interactions (the entire complex moves together). This can be seen in the supplementary video of the paper, when examining the pad. Thus, the angle should be measured relative to the pad surrounding the whisker and not to the fixed head. Second, the relevant angular variable in the sensory coding game is most likely the change in angle upon contact. Both the "push angle" (Quist and Hartman, 2012; Bagdasarian et al., 2013) and the "Angle absorption" (Bagdasarian et al., 2013) carry meaningful information. This analysis of relative angular changes upon touch will also make the angle-curvature comparison more symmetric (currently the change in curvature upon touch is compared with the absolute angle).

2) After reading through the Results section it turns out that this study actually (re) revealed two types of cells – those termed by Szwed et al. (2003) as "Whisking" cells and "Touch" cells. As in Szwed et al. (2003), the former respond to whisking in air and are sensitive to the phase of whisking and the latter respond to touch and are sensitive to curvature changes. This fact should be described at the outset (Abstract, Introduction, Discussion) and compared with the relevant previous reports.

What seems to be missing here are two complementary analyses – the sensitivity of "Whisking" cells to touch and of "Touch" cells to whisking in air. Thus, the fractions of pure whisking and touch cells, and that of a combined "whisking-Touch" type (Szwed, 2003) is not clear. True, the cell count is not high (I believe it is total of 20, although this was hard to dig – please state it at the outset) but the cost of this should not be in flattening all types to one common denominator.

Importantly, the point in the paper where the reader realizes that half of the cells are "Whisking" cells is a confusing point, reflecting back on the initial analysis. For clarity, the separation between cell types should be clarified at the beginning.

3) The Abstract statement "[…]we found that primary neuron responses were poorly predicted by kinematics but well-predicted by rotational forces acting on the whisker[…]" is not supported by the data. In fact, the insisting on a single mechanical variable does not make much sense, is not convincing and, as said, is not consistent with the data presented in the paper. I strongly recommend re-considering it. First, the paper shows that half of the cells (the whisking cells) are actually sensitive to a kinematic variable, acceleration. Indeed, it is associated with force but aren't all kinematic changes associated with forces? Also, selecting whisker acceleration instead of other angular variables, such as phase and velocity, and even angle itself, seems to be arbitrary. As for the Touch cells, indeed the curvature is correlated with various angular variables, but the parameters of these correlations depend on the interactions with external objects (see Bagdasarian et al., 2013), interactions that are not investigated here. In fact, Bagdasarian et al. showed that relying on a single mechanical variable must lead to ambiguity about external features.

4) The paper deals only with slow dynamics of coding – in time scales of seconds and resolution > 100 ms. Analysis at higher temporal resolutions (as was impressively done by the Petersen lab previously) is probably not possible in the current challenging setup of TG recording in awake animals. Yet, perceptual processing depends crucially on within-cycle millisecond time scales. This should be emphasized at the outset and discussed in relation to candidate sensory variables and relevant external features. It seems that while this slow time course may be relevant to features such as object radial distance (in the case of touch) and intensity of whisking (combination of whisking amplitude and frequency, which determine average acceleration throughout the cycle – see Figure 3D), but not object azimuthal position, texture or shape and not phase within the whisking cycle. Also, the choice of 100 ms should be justified, and the dependency of the results on this choice should be described.

5) Figure 1B & C show a whisker that pushes against the object during retraction. The video and Figure 1D shows the "standard" contact, during protraction. The authors should make it clear whether their analysis was based on both directions. If so, this comment becomes a major one – the authors must include the direction as one of the analyzed variables and describe the dependency of the various findings on it. Also, curvatures are very strong in this study (Figure 2B, movie). Please refer to it and compare to free-head conditions in which often the minimal impingement principle (Prescott et al., 2013) applies. Please discuss the implications on the predominance of curvature coding in this study.

Reviewer #2:

Key findings:

1) PWNs are relatively insensitive to absolute whisker angle but highly sensitive to curvature change.

2) The degree to which PWNs are tuned to curvature change predicts their response to inertial force during free whisking.

These results are well supported by the data, and the data is valuable, nicely collected and presented. However, the results don't change the general understanding of PWN coding and thus are not novel. The paper focuses on overturning a straw-man characterization of the literature, that PWNs are tuned to absolute whisker angle, not deflection forces.

It is unfair to characterize the current results as "at odds with passive stimulation studies (Gibson 1983, Lichtenstein 1990[…])". The classic studies refer to PWN tuning to angle of deflection not absolute angle. These particular studies had no ability to assess PWN tuning in the absence of deflection. In Bale (2013), again the positional tuning was in the context of positional deflection not free whisking angle. Indeed, Leiser (2007) showed that firing rates are 10x higher in PWNs during contact than during awake free whisking. The logical interpretation of this and many other cited studies of PWN coding is that deflection-induced forces (often quantified as deflection angle) are the primary driver of PWN spiking, not whisker position absent deflection.

The authors use the poor performance of angle GLMs during active pole exploration as evidence that curvature changes are what drive PWNs. But it is known that touch dominates PWN spiking responses, so including touch periods when assessing angle GLM decoding will trivially result in very low GLM angle performance. More interesting would be comparing the performance of angle GLMs during non-touch, free whisking periods with performance of curvature GLMs during touch periods.

In the study, active touch occurs at multiple pole positions, while passive deflections have only one starting position. Thus the comparison of curvature and angle coupling between active and passive conditions (Figure 4) is apples to oranges. For example, if the mouse must position his whisker 10 degrees more protracted to contact the pole in one position vs. another during active sensing, the correlation between angle and curvature will be degraded when averaged across pole positions. Including non-touch periods in the analysis further degrades the correlation. Thus the poor cross-correlation for the awake condition in Figure 4D is trivial.

The more interesting and fair comparison is the extent to which active control of whisker position impacts the relationship between curvature and push angle. Push angle is defined as the angle through which the whisker is rotated into the object (see Quist and Hartmann, 2012 or Hires, 2013 for details). Active control could alter the rigidity of the follicle, impacting follicle stresses and thus spiking activity of PWNs. This should be detectable via comparing the difference in push angle/curvature coupling (i.e. the slope of touch trajectories in 4E, assuming curvature was measured at the same radial distance) between active and passive states.

Additional comments:

The data in the paper are interesting and do have potential to address some open questions that would increase the importance and novelty of the work. Some possible ideas that reanalysis could address, (in order of increasing interest):

1) Do PWNs that are tuned to acceleration direction show the same directional selectivity to deflection direction?

2) Do force components (Faxial, bending moment) differentially drive PWNs?

3) Do PWN responses to passive vs. active touch exhibit different sensitivity to deflection angle or whisker curvature change?

Detailed justification:

1) This would be a simple expansion of the analysis of Figure 3 to show correlation of directional tuning between touch and whisking across the population of whisking sensitive neurons. This would make the Figure 3 result more compelling.

2) Using Faxial and Bending Moment as independent predictors in a GLM could determine if PWNs specialize for these components during active touch. Longitudinal deflection of whiskers causes robust responses in PWNs (Zucker and Welker 1969, Stuttgen 2008). Axial and lateral/moment ratios are used for radial object localization (Solomon 2011, Pammer 2013). This could bridge those physiology and behavior results.

3) Quantifying a non-trivial difference between passive and active touch, particularly if reflected in spiking activity would make the paper much more interesting. In cortex differences have been seen (e.g. airpuff of whiskers when awake elicits much weaker dendritic responses in Figure 1—figure supplement 1 than active touch, despite the much greater deflections air puffs evoke Xu 2012 Nature). Are these differences inherited from PWNs due to different mechanical coupling or sensitivity between these states?

Reviewer #3:

The manuscript of Campagner et al. investigates the whisker parameters (angle and curvature) that allow reliable prediction of spiking of primary whisker neurons upon passive or active touch. The manuscript is potentially interesting, although I have some concern about experimental setup and the validity of comparisons between passive and active conditions. Additionally, even though curvature reliably predicts spiking in awake rats for a subset of the data, the range of quantified reliability is large and not discussed.

1) The major conclusion (curvature much better predicts spiking than angle) is based predominantly on Figure 2C. The full range of reliability measures for curvature is 0.1 – 0.9. The authors put a lot of emphasis on the fraction of high values (max 0.88), but completely ignore the lower measures. Vice versa, the high values for angle GLMs are only briefly mentioned and emphasis put on poor predicting values. It seems very relevant to discuss the entire range for both conditions. Additionally, only 50% of the data shows a drop in performance when angle is used instead of curvature. The other 50% seems to perform as well for angle as it does for curvature. The conclusion that curvature is therefore the single most important parameter seems not to be supported by the data. Since the authors also describe W-sensitive neurons (subsection "Primary whisker neuronal activity during whisking is predicted by moment”), it seems more optimal to present the data in W-sensitive, curvature-sensitive and angle-sensitive fractions of the population data (how many neurons were recorded from in n=10 animals?).

2) Angle changes as a function of curvature as presented in Figure 4—figure supplement 1. This is very informative for the interpretation of Figure 4E and I would suggest moving Figure 4—figure supplement 1 into the main manuscript. Since angle changes dramatically during touch for individual pole positions (up to 20 degrees change in whisker angle for a fixed pole position), it can be concluded that angle is not independent from curvature and this probably underlies the range of reliability measures in curvature GLM and angle GLM. The authors should better discuss how the angle-curvature inter-dependence influences their model.

3) Passive stimulation is achieved by trimming the whiskers to 5 mm (methods). Under these conditions, it is (in my experience) impossible to induce meaningful curvature changes. The authors should better explain the experimental conditions if their experimental design allows accurate curvature measurement with a whisker trimmed to 5 mm and capillary 2 mm on whisker (Figure 4).
