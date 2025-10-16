# Peer review - Round 1

Editors:
- Krystel R Huxlin, https://ror.org/022kthw22 University of Rochester United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78106.sa0](https://doi.org/10.7554/eLife.78106.sa0)

In a methodologically sophisticated study of pre-saccadic processing at the fovea, Kroell and Rolfs provide compelling evidence that saccade preparation causes feature-specific pre-saccadic visual enhancement restricted largely to the center of gaze. The authors were able to differentiate this effect from pre-saccadic enhancement during passive fixations and to rule out criterion shifts as a mechanistic explanation. The fundamental implication of these findings will be of interest to both vision scientists and modelers. They parametrize a potential mechanism for visual continuity across saccades, with foveal processing identified as a key, contributing component.


---

# Peer review - Round 1

Editors:
- Krystel R Huxlin, https://ror.org/022kthw22 University of Rochester United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78106.sa1](https://doi.org/10.7554/eLife.78106.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Foveal vision anticipates defining features of eye movement targets" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Chris Baker as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Included here is a brief evaluation summary and a list of revisions the reviewers and review editor deem essential for the authors to address. The public summaries and full, individual reviewers' recommendations for the authors are also appended below. The authors are advised to address the public summaries briefly, and the individual recommendations in a detailed, point-by-point manner.

As you will be able to read below, all reviewers appreciated the study and manuscript describing it as a potentially very valuable contribution to the field of vision science. The writing was clear, the figures elegant and importantly, the study design and analyses were deemed rigorous, generally appropriate and elegant. The insights and data presented – especially if strengthened as detailed below – should be highly interesting to those studying active vision, as well as those studying low-level and high-level visual perception. However, as you will also see, reviewers raised some significant concerns with regard to the claims and data interpretation. Perhaps these issues cannot be addressed without collecting additional data, or at least additional analyses. However, given the interest in the research question and the value of the dataset, it was agreed that we would like to give the authors a chance at rebuttal.

In addition to the recommendations listed below in individual reviews, the points that need to be addressed can be summarized as follows:

1. More careful use of terminology related to the foveal region analyzed: please specify throughout whether you are referring to the foveola/central fovea, or the fovea. This is crucial to reduce confusion, and given implications in terms of different circuitry and neurophysiology between these regions, will impact the interpretation of the results.

2. The paper's main limitation is that it appears to entertain only one hypothesis (that saccade preparation enhances sensory processing) to explain the findings. But in fact, there are several alternative hypotheses, including the possibility of a criterion shift, purely sensory enhancements related to fixation duration, enhancements related to covert attention (and not saccade preparation), among others. These are not considered in the manuscript, and they should be.

For instance, the addition of a no-saccade experimental condition could help assess if spatial selectivity of enhancement remains the same as during the saccade task already reported. We realize that this would require collecting additional data on subjects, but at some level, this comparison may be what is needed to critically test the authors' current/sole hypothesis.

In addition, it would be good to see an assessment/discussion of whether a criterion shift may explain the present results. This could be tested by performing a quantitative comparison between two 2-stage models: one with sensory gain and one with criterion shifts at the decision stage.

In sum, at a minimum, the authors should outline and discuss other possible hypotheses, and this may ultimately cause them to tone down their main claims. Alternatively, they should provide data or modeling evidence (i.e., a convincing rationale) as to why these other hypotheses should be ruled out.

Reviewer #2 (Recommendations for the authors):

I thought the paper was clearly written and the figures were gorgeous. My concerns are outlined in the public review, but I really do think more needs to be done to address the issue of "enhancement". I have a few ideas for how this could be achieved.

The best idea I have is to use the external noise and project each frame on either the "optimal template" or on a "subject-specific template" to get a single 2D decision variable. I use the term "optimal" loosely, but the ideal observer would have a template that is matched to the target (orientation / SF energy). Now, there are two possible targets and a present/absent judgement, so it's a 2D task. But by projecting on a single template (or set of two templates) you either end up with a 1D variable or a 2D variable and then you can condition on that to calculate something like a d-prime. It involves a few assumptions, but I think they're minimal and reasonable. You want to show that based on this signal, the subjects are making choices more accurately. This is like looking at a spatiotemporal psychophysical kernel using the full reverse correlation, but collapsing across space (orientation and SF) using a template.

Another idea is to use a computational model of the choices to show that this must be a gain change. You'd have to build the same type of observer model (linear template -> decision variable -> criterion), but then you could play with how gain on the templates change vs how criterion shifts change. I think this level of additional analysis is really necessary here because enough about this task is new that it really needs these alternative models quantitatively examined. In the best case, I would lay out the different hypotheses specifically and quantitatively compare them.

Similarly, the spatial tuning of enhancement needs something to show that it's not just a static gain on an already tuned mechanism. That could easily be done with a few subjects doing the task without a saccade. Or more extensive modeling work could tease apart the shape of effects under different hypotheses.

On a smaller note, the language about the "fovea" can be confusing. In the anatomical literature (which is referenced in the 0.01% to 8% over-representation number in the intro), the "fovea" refers to the entire pit in the retina, which subtends more than 5 degrees of visual angle. The "foveola" is the rod-free zone that takes up only 0.01%. I realize that neurophysiologists are often sloppy about this distinction and it detracts from a simple "foveal" narrative, but it kind of continues the sloppiness in the field. I wonder if being precise about what exactly you mean by "fovea" would be that much of a hindrance to the writing? It does matter for thinking about the circuitry because the one-to-one projections in the fovea extend well beyond the central one degree. So what really is special about the foveola (lots of things, but it's not spelled out here)?

One paper of potential relevance for the discussion is "Transsaccadic integration of visual information is predictive, attention-based, and spatially precise" by Wilmott and Michel.

https://jov.arvojournals.org/article.aspx?articleid=2776566

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Foveal vision anticipates defining features of eye movement targets" for further consideration by eLife. Your revised article has been evaluated by Chris Baker (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

All three reviewers appreciated the manner in which you were able to address the great majority of their comments, and the additional experiments performed, which were deemed to add significant value to the study.

Reviewers were reasonably convinced by your arguments that criterion shifts are unlikely to explain the phenomena at hand. However, they requested that you modify your Discussion to include consideration of alternative mechanisms. Specifically, please respond to the following concerns, which revolve around the notion that dismissing criterion shifts as explaining the obtained results because of spatial/temporal specificity might be too simplistic an interpretation:

1. Please discuss whether the particular task design used in the present study could cause spatial distributions of hit rates and false alarm rates that might be incorrectly interpreted as enhancement, as suggested in the work of Sridharan et al., JNeurosci (2017).

2. Additionally, based on the extensive literature on temporal changes in criterion during decision-making (i.e., "collapsing bounds" or "urgency signals"), please discuss if there could there be urgency signals during saccade preparation that lead up to a decision and then saccade generation? Is it possible that the reason for an increase, then a decrease in hit rates pre-saccadically is a temporal change in criterion until saccade generation is hit (i.e., a bound is crossed)?
