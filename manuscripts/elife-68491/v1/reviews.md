# Peer review - Round 1

Editors:
- Redmond G O'Connell, Trinity College Dublin Ireland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68491.sa1](https://doi.org/10.7554/eLife.68491.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This paper is of interest to neuroscientists and psychologists working on perceptual decision-making and metacognition. Using a novel task varying the timing of covert decisions, together with sophisticated computational modelling, allowed identifying neural correlates of latent states related to confidence. The conclusions are in line with other papers identifying a dissociation between brain activity supporting performance and confidence, but provide a novel lens through which to understand these differences by focusing on confidence noise.

Decision letter after peer review:

Thank you for submitting your article "Separable neural signatures of confidence during perceptual decisions" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Redmond G O'Connell as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Michael Frank as the Senior Editor. The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions (for the authors):

1) The study needs to be more clearly framed with respect to the previous literature. Extensive neuroimaging and lesion work has already provided compelling evidence that perceptual decisions and metacognition rely on distinct neural circuits. In addition, previous modeling work that has provided a joint account of first- and second-order behaviour has assigned a key role to post-decision processing (whether within same or different circuits). The authors should clarify their hypotheses and how they relate to this previous work.

2) Substantial rewriting of the Results is necessary. A clear rationale should be provided for each analysis step and the results of those analyses need to be linked back to the study hypotheses.

3) Consider whether a simpler model-free analysis (e.g. check whether confidence resolution is higher for More vs Less trials) could be done to validate the key claim of confidence/performance dissociations (see Reviewer 2 comment)

4) Check impact of high-pass filtering and current source density on CPP signals (or consider removing those signals from the analysis if they are not speaking to the study hypotheses).

Reviewer #1 (Recommendations for the authors):

Some substantial rewriting of the Results section is required to clarify the rationale for each analysis without requiring that the reader read all of the Supplemental Materials in order to follow the narrative. In several instances it is not clear why the analysis is being run or what we should take from it. A prominent example is the ERP analysis where the choice of signals or their relevance to the hypothesis is not explained and the relevance of the reported results to those hypotheses is similarly not clarified. It is not clear why only the More and Less conditions are compared or why post-response time-points are considered relevant. Additionally the purpose of the decoding analysis is left obscure and it is not clear why 8-32Hz is the focus Throughout I think a lot more hand holding is required for the reader to follow why each analysis is being run and how exactly it relates to the stated hypotheses.

I also have a few more specific comments regarding particular aspects of the results.

If the CPP analyses are deemed important to the overall story then the use of a 0.5Hz filter may be problematic as it is likely to attenuate a slow building signal like the CPP. This could conceivably lead to some issues when comparing Less/Same/More trials where the CPP may build over different durations. The authors might also consider applying CSD transformation which has been shown to reduce interference from overlapping fronto-central negativities (e.g. Kelly and O'Connell 2013, J Neurosci).

One of the key observations is that the precision of neural representations of accumulated evidence drop towards the end of the More trials but there is no such dropoff in the decision update representation. I am struggling to understand how this might arise and it would be helpful if the authors could provide an explanation.

The authors report that there is no significant effect of More vs Same on choice accuracy but the figure suggests that there is a substantial numerical difference in the expected direction. Bayes factors should be provided to quantify the evidence in favour of the null hypothesis.

Reviewer #2 (Recommendations for the authors):

I found myself wondering in lots of places here whether a simpler model-free analysis could have been done to validate the key claim of confidence/performance dissociations in behaviour and neural activity. For behaviour, would it not be possible to eg check whether confidence resolution is higher for More compared to Same trials? Or do a lagged regression (similar to Figure 4c, but now for behaviour) to show the latter samples have an impact on confidence but not performance on More trials?

I found the writing hard going in places. It was often difficult to figure out what exactly had been done in analysis – in particular "representation precision" (line 228) was only briefly defined in the figure legend, and it would be useful to spend some more time unpacking this in the text to help the reader follow along.

Line 399 of the supplement, "We used the representation error as an estimate of the inference error of the observer: the absolute difference between the cluster predicted value and the expected value given the cluster representation and the true value of the accumulated evidence based on the orientations presented to the observer." There are two "ands" here, so I did not understand what the absolute difference was between.
