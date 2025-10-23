# Peer review - Round 1

Editors:
- Timothy D Griffiths, University of Newcastle United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55508.sa1](https://doi.org/10.7554/eLife.55508.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The work describes a relationship between α activity and the prioritisation of elements held in working memory that will be of broad interest.

Decision letter after peer review:

Thank you for submitting your work entitled "Auditory cortical α desynchronization prioritizes the representation of memory items during a retention period" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: William Sedley (Reviewer #2).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work is not currently suitable for publication in eLife. It is eLife policy that if needed revisions would take more than 8 weeks, we reject a manuscript. In your case, that is where we stand: your paper is of potential interest, but requires significant revisions that we believe require more than 2 months to resolve.

Specifically, the reveiewers found the work interesting in measuring α changes in auditory areas measured using MEG as a function of the presence of a (temporally predictable) auditory distractor. The authors use a modified Sternberg technique with strong and weak distractors presented in different blocks and a phonological WM task after Bonnefond and Jensen's visual version. The group data show decreases in pre-distractor induced but not phase locked α power in left temporal cortex and lower decoding accuracy for the target letter before the strong distractor compared to the weak. In contrast, analysis of the individual α changes showed that increased α correlated with decreased decoding accuracy at the time of the distractor explaining about 1/3 of variance.

We encourage you to consider resubmitting the paper to eLife if you are able to address the issues described below. The most significant points include potential circularity in the analysis, the specificity of the effect with respect to α, the specification of time windows, and the discussion of the basis.

Major comments:

1) The cover mentions 'In daily life we are forced to prioritize ongoing sensory information, to be able to deal with the tremendous amount of input we are exposed to.' Does a situation ever occur in daily life when we have to deal with a distractor that is entirely predictable in time?

2) The central message of this paper relates to α, but the data suggests it is more of a β effect (e.g. the difference plot in Figure 3A, the 10-16Hz band used for the correlation analysis). While the authors make a strong case in the Introduction for the effect to arise in the α band, the data disputes this. Yet, the authors continue to focus on α throughout the Discussion.

3) Throughout the analysis, the authors use restricted windows of analysis. Such practices help limit the multiple comparison problem, but strong a priori reasons are required for window selection – reasons that are not supplied in the manuscript. Were these windows were selected post-hoc (intentionally or not)? This is most troublesome at the start of subsection “Pre-distractor α power modulations of probe-related information”, where the α band was defined as 10-16Hz. This selection is particularly worrying as it does not appear to be either a priori (10-16Hz is really pushing the boundaries of what is consider α) or driven by earlier analysis (the effect in Figure 3A extends from 10-25Hz). Given that this effect is only marginally significant (p = 0.0272), the concern is that worry these parameters may have been selected to drop the p-value below the "significance" threshold, and would not survive multiple comparison correction should the window be expanded.

4) The reviewers struggled with the rationale of the decoding approach. Subsection “Decoding probe-related information” paragraph one describes beginning by decoding from post-probe activity whether that probe was part of the memory set or not. Is decoding accuracy here intended to act as a proxy for how well the memory set was encoded/retained in memory? If so, shouldn't that accuracy be greater than chance earlier than 300 ms after the probe onset (Figure 2A shows it is at chance until then)? This also seems rather an indirect proxy – presumably the neural activity post-probe also heavily features the identity of the probe itself. Furthermore, the neural activity involved in distinguishing presence vs. absence in the memory set might also reflect differential adaptation of the probe representation (although the timescales are probably long enough for this not to be a consideration in sensory cortices). Perhaps decoding accuracy is not supposed to be a proxy for how well the memory set was encoded/retained in memory, since later (paragraph two and elsewhere) the authors refer to using this trained classifier to look for how well the probe is represented during the retention period. To address this question we might have expected the authors to have trained a classifier on neural representations of specific letters (e.g. using the period after each is presented during the memory set, or when they appear as probes) and test for these representations during the retention period. With such an analysis the expectation might be that in a successful trial (and perhaps more so for a weak distractor), that trial's probe letter would be better neurally represented during retention if it were present in the memory set but not if it were absent. We may have misunderstood the rationale of the analyses, in which case it likely needs to be set out more clearly in the manuscript.

5) A major concern was the potential circularity of the analysis. The same signal was used to get the classifier estimates and the α/β power. If α/β contributes to the classifier then the signal would essentially be correlated with itself. There are ways to get around this issue, for instance by using a band-stop filter (i.e. taking out α/β from the signal) on the data before feeding it into the classifier. The reviewers suggest orthogonalizing their α/β data and classifier data before attempting a correlation.

6) We would like to see the brain distribution of the AUC in Figure 2A as a function of time. We cannot work out what latency the brain data shown correspond to. We agree the data are left lateralised but there seems to be an effect in right operculum and DLPFC.

7) From 2B left and right, the decoding of probe-related information prior to the distractor seems to be at/below chance for strong distractors and below chance for weak distractors (assuming chance is AUC = 50%). On that basis, I'm not sure whether the difference (shown in 2B right) underpinning one of the paper's main conclusions is really interpretable. The authors do not mention or discuss this.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Auditory cortical α desynchronization prioritizes the representation of memory items during a retention period" for further consideration by eLife. Your revised article has been evaluated by Barbara Shinn-Cunningham (Senior Editor) and a Reviewing Editor.

The authors have addressed a number of concerns raised in a previous round, importantly providing a clearer rationale for their approach, and checking the α-specificity of the effects. The additional analysis of memory content decoding by frequency band has also strengthened the paper. There are two remaining issues that need to be addressed before acceptance, as outlined below.

Major Issue 1: Below chance classifier decoding.

1) There does not seem to be any reference to the cross-validation of the classifier in the main text. Before seeing whether the classifier can generalise to the retention window, it would be important to see whether the classifier can generalise across different folds of the probe window. This supplementary analysis would allow more confidence in the validity of the classifier.

2) A lack of detail about the classification approach in the Materials and methods makes it difficult to evaluate the suitability of said classification approach. It would be helpful to note explicitly the number of trials used for training/testing, and the number and nature of features included.

3) The below chance decoding in paragraph two of subsection “Decoding probe-related information” is a major concern, particularly because of the apparent absence of cross-validation during the probe window. It would be important to demonstrate that:

i) This is not due to overfitting to the training dataset. It is unclear from the Materials and methods, but perhaps 306 sensors and 50 timepoints (i.e. 15,300 features) have been used to train on (by my count) 288 trials. Such a large number of features relative to a low number of trials can mean that the classifier cannot generalise to any data set other than the training data set (potentially explaining the below chance decoding).

ii) This is not due to linear dependence between features. Again, it is unclear, but it would appear that raw time/sensor data has been used as features in the classifier. Though MEG has excellent spatial resolution, there is still some co-linearity in the signal between sensors. This can impede the generalisability of the classifier to test data sets.

Both of these points could be addressed by running a PCA on the features prior to classification. PCA will help minimise linear dependencies between features, and if one then takes only the top 100 components, then the number of features will not exceed the number of training trials.

Major Issue 2: Correlation between α power variability and ability to decode memorandum.

The authors have correlated, across subjects, a measure of α power variability with the effect of α power on memorandum decodability. As a previous reviewer points out, this is rather removed from the data and does not clearly support the interpretation that α power and decodability themselves are linked. A trial-by-trial analysis of α power versus memorandum decodability was suggested. This would require some consideration of across-subject differences in the raw measures. So either a correlation could be performed subject by subject, and then the correlation coefficients tested against zero as a group, or a single trial-by-trial regression could be run across subjects with appropriate normalization or inclusion of random subject effects.

It might be that the trial-wise data are too noisy for such an approach, and that this is a reason for the authors' use of the median split into high-α and low-α trials. However, the appropriate analysis would then seem to be to compare memorandum decodability for low-α versus (minus) high-α trials, testing whether this difference is significantly greater than zero for the group. The correlation shows only that α power variability is associated with the effect of α power on memorandum decodability. This might not be meaningless, but as the scatter plots in 4B show, there is a fairly balanced split of subjects for whom higher α is associated with better decoding and those for whom lower α is associated with better decoding (positive and negative differences on the y axis). The axis labels are not too clear as to the direction of the comparisons. A possible interpretation is that for subjects on the left of the scatter plots with a lower log10 α ratio (nearer 0.7, i.e. nearer 10^0.7 = four times more α power in high- than low-α trials), high-α trials lead to better decoding than low-α trials, whereas for subjects on the right of the scatter plots with a higher log10 α ratio (nearer 0.9, i.e. nearer 10^0.9 = eight times more α power in high- than low-α trials), the reverse is true.

In the absence of clarification or a new analysis along the lines suggested, it is not clear that the data support the conclusions of the paper.
