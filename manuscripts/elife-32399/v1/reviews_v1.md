# Peer review - Round 1

Editors:
- Nicole Rust, University of Pennsylvania United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.32399.012](https://doi.org/10.7554/eLife.32399.012)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Pupillometry reveals perceptual differences that are tightly linked to autistic traits in typical adults" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Duje Tadin (Reviewer #1); Sebastiaan Mathôt (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

In this manuscript, the authors use the pupil light response to track whether participants pay attention to the front of a bistable rotating cylinder (by using different brightness levels for the front and back). Crucially, they find that the extent to which participants selectively attend to the front of the stimulus (rather than to the stimulus as a whole) correlates strongly with their autism-spectrum quotient (AQ). The reviewers found the result to be both timely and interesting. They also note that while the global vs. local processing hypothesis has been longstanding in ASD work, the present approach is both elegant and objective and the control experiments are insightful.

At the same time, the reviewers noted the following concerns that need to be addressed before publication:

1) The key assumption of the paper is that switch-triggered pupil changes are indicative of individual differences in default perceptual styles. The authors support this by having additional experiments that bias all subjects toward the same perceptual style-which is a nice control. An additional strong support for this key assumption would be within-subject evidence that if a person switches her/his perceptual style that would result in a predicted modulation of switch-triggered pupil changes. Such a within-subject control would not need as many subjects, and would show that self-initiated changes in the perceptual style yield predictable pupil results-further supporting the main assumption of the paper. (This could be done with or without an objective confirmation that the perceptual style changed).

2) The relative directions of pupil changes in Figures 1B and 3A are consistent with the authors' assumptions, but the sign of those changes is not. That is, in Figure 1B, shouldn't going from black in front to white in front result in a decrease in pupil size? It appears that we're seeing two effects, one that is modulated by dot color and a main effect of switch that causes an increase in pupil size. One can come up with a reasonable explanation for that, but it needs to be included in the manuscript. If there are indeed two effects there, it would be interesting to see if they can be analytically separated and correlated with AQ.

3) There is concern with the strength of the correlation observed between the pupil measure and the total AQ score. The. 7 value seems extremely strong for this type of effect, and such a strong correlation between two measures is only possible if the measures themselves are highly reliable. Using the rule of thumb that the between-test correlation can be at most the product of the reliabilities of the two tests, would indicate that the pupil measure and total AQ score should have reliabilities of around. 8. This seems high for these kind of data. Is there evidence that this is so? Or is the correlation reported here an overestimate despite the substantial sample size (for which the authors should be applauded). This of course doesn't mean that the correlation isn't real, and even a substantially weaker correlation would be useful information here. The authors should review the correlations, and report reliability information if available to provide an estimate of what a realistic upper bound for the correlation is. It may be that the theoretical upper bound is lower than the observed correlation.

4) It is impressive that pupil size changes explains so much variance in autistic traits, not only because other behavioral measures did not seem to be as successful (as reviewed briefly in the Discussion), but also because pupil size changes are believed to be a noisy measure. Given that the authors "re-used" a subsample of their participants in the "swapped motion direction" control experiment, and yet another subsample in the "double task" control experiment, it would be nice to present the correlation of the test-retest sessions for each of these repeated experiments. We expect the pupil size changes to correlate very strongly between sessions, thus offering an upper-bound on the correlation one might expect to measure between pupils size changes and autistic traits.

5) One reviewer noted concerns about the availability of the data. eLife policy is that all data and software crucial to understand and replicate the findings of a manuscript ought to be publicly available (eLife's data availability policy can be found here: https://submit.elifesciences.org/html/eLife_author_instructions.html#policies; please refer to sections "Availability of Data, Software, and Research Materials" and "Data Availability"). Please clarify whether there are any constraints preventing you from making this data publicly available. If not, the data should be provided in the form of supplementary files, source data files or source code (when applicable) with the submission or deposited to an external repository. A comprehensive catalogue of databases has been compiled by the BioSharing information resource (https://fairsharing.org/biodbcore/) but eLife Editorial staff can offer more specific guidance as needed.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Pupillometry reveals perceptual differences that are tightly linked to autistic traits in typical adults" for further consideration at eLife. Your revised article has been favorably evaluated by Richard Ivry as the Senior Editor, Nicole Rust as the Reviewing Editor, and three reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) The description of the new experiment seems to be missing from the Materials and methods. It is not difficult to figure out the details of the experiment, but, for completeness, it should be in the Materials and methods.

2) Regarding the experimental materials: It's great that you have now made these available, including the experimental scripts. But the materials can still use a bit of editing to make them more accessible. Here are some ideas on how you might improve things (although you should feel free to do this however you think best):

- Add a README file that clearly explains the dependencies (i.e. what software do you need), how the analysis should be executed, and the file/ folder structure (i.e. what is located where).

- Add the raw data. Right now the data is provided in.mat format. But it would be better to also (or only) include the datafiles as they are created by the eye tracker (i.e. EDF for the EyeLink), and explain how these can be converted to.mat for further analysis.

- Add a LICENSE file to specify the license, such as CC-by.
