# Peer review - Round 1

Editors:
- Timothy D Griffiths, University of Newcastle United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64501.sa1](https://doi.org/10.7554/eLife.64501.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The work addresses whether predictive coding models of perception, that have previously been applied to cortical analysis, can also be applied subcortical processing. This has been been done using high field fMRI and a paradigm that aims to disambiguate sensory adaptation and expectation for sound sequences.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Abstract rules drive adaptation in the subcortical sensory pathway via hierarchical predictive coding" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Timothy D Griffiths as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

The reviewers raise a number of issues that require an extensive revision is in order to be addressed. It is likely that further data and analysis will also be required as discussed below. It is eLife policy to reject any manuscript where the work necessary to address criticisms would take more than 3 months; therefore, we are rejecting the paper at this time. That said, the reviewers agree that the work addresses an important issue, and that it is possible that further analyses and clarification will address the large number of concerns raised by the reviewers. We therefore would welcome a "new" submission of this work when you are in a position to address the concerns raised by the reviewers.

General comments

The work addresses the interesting question of whether high-level prediction effects processing in the ascending auditory pathway. There is much less work on possible correlates of constructive models of auditory perception compared to visual perception and much less work on afferent pathways to the sensory cortices as opposed to cortical processing, so the initiative is welcome. BOLD responses are studied in the human subcortical auditory pathway using 7 Tesla fMRI with a spatial resolution of 1.5 mm isotropic to study adaptation in the subcortical regions of the auditory pathway, more precisely in the inferior colliculus and medial geniculate thalamus in order study the hierarchical predictive coding. The paradigm is appealing because of the claim that it allows interpretation in terms of stimulus specific adaptation versus predictive coding.

The reviewers were all concerned about interpretation of the data in terms of subcortical bases for predictive coding. A formal model comparison is suggested by one reviewer, and another required an additional control. The interpretation of the data is speculative in places. A further concern was the extent to which this is an advance on the work of Parras and colleagues who demonstrated a hierarchical organization of prediction error at the neural level.

Specific criticisms

Data

1) Several frequency combinations are used in the paradigm. Authors show that the latency of response for the early DEV is larger than for the later ones. This is quite reasonable and expected. While the main paradigm used is generally interesting, there is a question whether or not the BOLD response shows genuine expectancy. This issue is that expectance may be generated when authors warn subjects that a DEV will be in 4th, 5th or 6th position. It is unclear whether this BOLD response is something that brain will extract from the history of stimulation. The experimental subjects already know that these DEV will appear, no matter what, on these 3 positions. A missing control is to have a regular sequence with unexpected DEV where the subjects will have no idea of when the dev will appear. Then you can manipulate the appearance of the DEV the way you wish making the DEV to appear regularly or irregularly and see if subject can really extract any abstract rule. One reviewer felt this control required to know if the BOLD response is due to the expectancy, the position of the DEV or any other reason.

2) Another confound is that authors wish to show Stimulus specific adaptation (SSA) in IC and MGB. Subsection “Adjudicating between habituation and predictive coding”. Strictly speaking to show SSA; one should use the classical oddball paradigm and used the flip-flop control to make sure that there is indeed a genuine adaptation that is specific to the stimulus and that the differences is not due of a different sensitivity to the two frequencies uses ad DEV and STD.

3) The choice of contrast to represent adaptation was std0>std2, but why not also std0>std1?

4) In the same vein as above, Deviance detection was defined as dev4>std2, why not also consider dev 4> std1. But also, why focus only on dev4, would it not be more complete to look at all deviants (that is devi>stdj with i=4, 5, and 6; and j=1,2), since they all elicit deviance detection? (Even if dev6 is predictable, it is still deviant).

5) Were the data from the silent gaps analysed? These data are potentially invaluable to disentangle between the 2 models since with gaps we evoke prediction errors but not adaptation.

6) It was unclear how the 3 pure tones were played in the sequence structure. Did they alternate between std and dev? was a Flip-flop design used (where sound A being dev in one sequence is then dev in a different sequence? Why use 3 pure tones instead of 2 (one for dev and one for std).

7) The correlational approach to test of H2) predictive coding seems somewhat suboptimal since it's not really formal model comparison. A regressor for probability in the GLM would make more sense, if the goal is to show that BOLD responses increase a function of probability (as per Figure 1C). Alternatively, even more elegantly, a bayesian approach comparing the 2 models simultaneous using posterior probability mapping (Rosa et al., 2010) would be most appropriate to adjudicate between these alternative models. That approach has the great advantage of formally testing alternative (2 or more) models simultaneously at each and every voxel (while also avoiding the need for multiple comparisons) – hence at the end one has a map of where h1 and h2 are more likely.

8) The approaches above mentioned would also preserve the original 7T superb spatial resolution. It seems from Table 2 that activity from all voxels within MGB and IC were lumped together for the correlations – is this really necessary or even desirable? Given how ubiquitous habituation is in the brain, it is quite likely that it also occurs along this subcortical pathway. And yet, with the approach taken, this is surprisingly completely ruled out. It is possible that by lumping the data together we're losing specificity about voxels within IC/MGB where habituation is more likely than predictive coding, and voxels where the reverse (predictive coding) is more likely? If the latter dominates then by lumping data, we can only see predictive coding likely missing out on evidence for habituation (in at least some voxels).

9) If a hierarchy exist as the authors claim, this would ideally be shown by a quantitative analysis of the observed effect between the IC and MGB.

10) Why restrict the analysis to IC and MGB with functional localisers? Would it not be interesting to see if these effects emerge elsewhere in the brain (within the slab imaged – e.g., replicate effects within primary auditory cortex for example)? Also why use functional localisers instead of anatomically defined ROIs?

11) Authors also claim that the response is observed in both lemniscal and non-lemniscal regions of the IC and MGB, however, again I miss a detailed analysis about this issue and how they have separate the lemniscal IC vs non lemniscal IC and similarly about MGB. Authors refer to a previous work, but no details and actual results are provided or evident here. In fact, no data are shown about the IC.

12) Will code and data be made publicly available in keeping with the open science framework?

Exposition

1) Nomenclature. This is not a trivial issue. Authors made an unconventional use of the words habituation, stimulus-specific adaptation, stimulus-specific habituation, etc. and then they speak of neural habituation. These need to be precisely defined and used consistently in the text.

2) The section on “Results cannot be explained by task-engagement” is basically a discussion where authors try to argue if results could be explained by effects of task-engagement. This whole part pertains to the Discussion, which on the other hand is unusually brief and rather speculative and unfocused.

3) The Discussion itself required expansion to more deeply reflect on the implications of this study.
