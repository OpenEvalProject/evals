# Peer review - Round 1

Editors:
- Michael J Frank, Brown University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.09000.017](https://doi.org/10.7554/eLife.09000.017)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled "Testing sensory evidence against mnemonic templates" for peer review at eLife. Your submission has been favorably evaluated by Eve Marder (Senior Editor), Michael J Frank (Reviewing Editor), and two reviewers, one of whom, Floris de Lange, has agreed to reveal his identity.

Overall, we are enthusiastic about this paper. The conceptual issue at hand is topical, the experiment is cleverly designed, and the analyses are novel and insightful. However there are a number of interpretative and analysis limitations that need to be addressed for further consideration.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors measured EEG/MEG responses during a perceptual decision-making task, in which human subjects had to compare visual stimuli against a mnemonic template. They find evidence of stimulus coding, template coding, as well as coding of the signed difference between stimulus and template. Template coding appeared shortly before/during initial stages of stimulus processing, showing that the search template is transiently re-activated just prior to and during encoding of each stimulus. The authors mimic the geometry of neural responses with a toy computational model that consists of a perceptual, template and decision layer in which the decision layer uses population coding.

Essential revisions (contributed by all reviewers):

1) Reviewers agreed that while the findings are informative and novel, they are somewhat oversold, with language that is and should be interpreted more conservatively. The main advances of the paper are in showing the efficacy of MEEG methods for decoding and in demonstrating that the search template is transiently re-activated, which is worthwhile. Many of the other interpretations seem to be based on overly stringent (and probably incorrect) assumptions about how a neural code must be perfectly stationary over time, in conjunction with a possible misunderstanding about how different dipole orientations would produce different topographies without reflecting different neural computations. The paper should be reframed. The authors should consider which of the elements they have direct evidence for and which are speculations.

2) The core of the paper is in the first 4 or 5 figures; the remaining ones and analysis were less well motivated. One reviewer notes that, after Figure 3, no data are shown and, by Figure 7, interpretations are based on parameters far abstracted that it is difficult to know how those relate back to the data. As such, the manuscript is quite dense, with many highly complex analyses and results. These analyses are highly sophisticated, but it is not always clear why a particular analysis is performed. In the same vein, some details of the response-related coding analysis were also unclear. For example, why does the cosine of 'stim-template' reflect the task-relevant information, and the sine the irrelevant information?

3) Concerning the section "Stimulus and task codes vary dynamically throughout the epoch", the authors have not really shown this to be the case. We would need to see how the codes differ, for example with qualitatively changing topographies. If the neural source is oscillatory, then rapid changes in the phases would limit temporal extendability to one cycle and could lead to the misinterpretation that "multiple stimulus-specific codes must have been activated in sequence". Thus if the codes really vary over time, the topographies would have to be different in a way that is inconsistent with rotating or oscillating dipoles. This is a critical point, because the authors rely on the interpretation of the "code" being dynamic through the rest of the manuscript.

But this is more than just methodological. There is an implicit assumption here, which is that a "neural code" is an instantaneous spatial pattern, and so if it changes slightly from millisecond to millisecond, the "code" must be different. This assumption is inconsistent with neurophysiology: It is well established that neurons are sensitive to their history of inputs, and that their precise spike timing carries information about input patterns. Thus a specific representation can include time (frequency multiplexing is a simple illustration of this). Therefore, what the authors call a dynamic code could simply be a static code that has time as a dimension. If the authors were to interpret the findings more conservatively this wouldn't be problematic.

4) Rather strong statements are made about sensory representations on the basis of whole-head MEG recordings. For example, they state: "Since coding did not cross-generalize over time, multiple stimulus-specific codes must have been activated in sequence".

As noted above, we are a bit worried about the logic that the (in)ability to read out orientation signals in a generalizable fashion over time must mean that the neural codes are not stable. There are plenty of other reasons why a stable sensory code would nevertheless not generalize over time. For example, MEG measures a mixture of activity of many sources at any moment in time. If a stable source would be accompanied by a variety of other neural sources that change over time (which is almost certainly the case) this could also result in a (partial) break-down of generalization. More generally, the fact that a machine learning algorithm can "decode" a particular feature/stimulus, does not imply that the brain has "encoded" this feature. The 'decoder' could have picked up on any feature that has a non-zero correlation with the feature under investigation. Again it would be prudent to better qualify what can and cannot be concluded from the data.

5) Differences between decoding and representational geometry:

The differences in generalizability between decoding and representational similarity are intriguing. At first, it appeared that these may simply be an artifact of the method, as opposed to conceptually different characteristics of the neural activity patterns. This is better explained in the Discussion, but the reason for doing these two types of analyses, and how they provide an answer to distinct questions, could be better motivated upfront.

6) Discussion on predictive coding:

We found the link made to predictive coding somewhat of a stretch. The authors state that the signed difference between template and stimulus is passed down, in line with predictive coding. But also the stimulus itself is encoded, see Figure 3A. And the prediction error in predictive coding would serve to update perception, not a decision about whether a percept is different from an internal template. This signed difference is mandated by the task in this case. Finally, the statement "Our results, using non-invasive imaging, suggest that template and stimulus coding may be similarly segregated across cortical layers" is quite over-stated. The authors investigate whole-head MEG responses, localizing their signals to roughly the back of the head. How that would suggest segregation across cortical layers is very unclear at best.

7) Equations 1 and 2: CCT and WTW are invertible only if C and W are full column rank. Was this evaluated (for W; I assume the columns of C are all linearly independent) or was the psuedo inverse used? MEEG data are often reduced-rank, particularly after ICA cleaning. A minor aside: It might be useful to mention that these equations are the solutions to AX = b, which would help the linear-algebra-challenged readers understand the analyses.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Testing sensory evidence against mnemonic templates" for further consideration at eLife. Your revised article has been favorably evaluated by Eve Marder (Senior Editor), Reviewing Editor Michael Frank, and two reviewers. The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below.

As you will see, the second reviewer is satisfied with your revised manuscript, but Reviewer 1 has some lingering concerns. Partly this reflects a difference in taste and style, but please address the specific interpretative and statistical issues that the referee raises regarding Figures 3, 4, and 6. It is important that these issues are transparent.

Reviewer #1:

The authors made some adjustments but the overall manuscript is more or less how it was in the first submission.

The Discussion is really long, and most of it is just a rehash of the results rather than actual discussion.

The figures are still difficult to interpret, and neither the legends nor the text is very helpful. Examples:

I don't understand the outlines in Figure 4A, C. The legend suggests it's the significance of the difference between the diagonal and off-diagonal, but the outline includes dark red regions very close to the diagonal, and it doesn't include much of the plot that should also be different from the diagonal. And what is the difference between the lines and the opaque shading in panel B?

I also don't understand Figure 6. The small black outline in panel A doesn't seem to match the darker areas in the figure, and is nothing statistically significant in panel B?

Is Figure 3 supposed to be the diagonals of Figure 4? The significances don't seem to map on to each other.

Reviewer #2:

I think the authors have dealt with all the reviewers' comments in an exemplary way, and I congratulate the authors with their interesting manuscript.
