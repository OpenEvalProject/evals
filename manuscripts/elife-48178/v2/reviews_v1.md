# Peer review - Round 1

Editors:
- John Huguenard, Stanford University School of Medicine United States

Reviewers:
- Tim Jarsky, Allen Institute for Brain Science United States

## Review text

DOI: [10.7554/eLife.48178.sa1](https://doi.org/10.7554/eLife.48178.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Peng et al. have adopted and optimized recent innovations such as patch pipette cleaning, multiple amplifiers and automated pressure control to create a very high throughput semi-automated method for simultaneous multiple patch clamp recordings from precious tissue, such as resected brain tissue from epilepsy surgeries. Here they show their robotic system can obtain high numbers of successful paired recordings in part due to a system that allows for cleaning and reusing patch electrodes for multiple serial recordings. This approach yields hundreds of potential neural pairs per patient sample, which will undoubtedly yield novel insights on altered synaptic connectivity relevant to epileptic networks. Detailed plans and control software source code are provided, and the overall approach is validated in both rat and human brain slices. This paper should be a valuable and accessible resource for those needing to optimize the yield of paired intracellular recordings from precious tissue.

Decision letter after peer review:

Thank you for submitting your article "High-throughput microcircuit analysis of individual human brains through next-generation multineuron patch-clamp" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Eve Marder as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Tim Jarsky (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This Tools and Resource paper describes a low cost, high throughput, multipatching system designed to optimize discovery from precious live brain material, such as that obtained in human epilepsy surgery. The approach utilizes and acknowledges a number of advances developed by other research groups, and the authors provide early results indicating that the approach will highly leverage what can be gained from such precious materials. The methodology is well laid out, with appropriate drawings, photos, parts lists, and videos. It should be an accessible method that would be utilized by exactly those that would most benefit.

Essential revisions:

1) One major concern is the pipette cleaning system the authors adapted. Based on the CR Forest's original protocol, an additional step is needed to clear the residual detergent adhering to the outside surface of the pipette tip with aCSF before moving pipettes into the recording chamber for patch attempt, yet Peng and colleagues omitted this step. There is a good practical reason for omitting this step, as stated by the authors, but little or no data are provided to support this practice. They claim that there were not differences in recording quality or electrophysiological properties between pipettes at first and after cleaning, but these claims should be supported with the data. In particular it would be important to report how the membrane potential, input resistance, synaptic events, and action potential parameters (amplitude, width et al) change over time after patching and repatching.

2) The article overemphasizes connectivity analysis and ignores its limitations, e.g., false negatives. The authors may wish, instead, to emphasize that multipatch recordings are currently the only technique available to assay the strength and short-term plasticity of monosynaptic connectivity.

3) Important missing experimental details include specifying if it is possible to patch cells while recording from other cells, the time that is taken to probe connectivity and an analysis of the distance distribution of recorded cells (e.g., is the distance distribution of cells obtained to extend recordings the same as those obtained initially?).

4) The authors emphasize some benefits of the semi-automated approach but do not identify other aspects of multipatch experiments that could benefit from automation – for example, data acquisition and online QC, and real-time connection detection. With the potential for so much data gathering, data format (e.g. Neurodata without borders), data sharing, automation of connection detection and analysis, should be addressed.

5) While taking advantage of rare live human tissue and especially to increase the data yield from each sample is a valid rationale for developing multi-patching systems, it may it is not known yet whether this will be sufficient yet to probe the difference between individuals. When discussing difference across human individuals, what kind of differences were observed? Cell types, connections? I would suggest the authors to tone down this claim.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "High-throughput microcircuit analysis of individual human brains through next-generation multineuron patch-clamp" for further consideration by eLife. Your revised article has been evaluated by Eve Marder as the Senior Editor, and a Reviewing Editor.

The manuscript has been very much improved but there is one remaining issue that need to be addressed before acceptance, as outlined below:

Regarding the new experiments on repatching following Alconox treatment without Alconox rinsing (subsection “The final expulsion sequence does not require additional wells containing aCSF”). These are convincing and show that in young rat brain tissue that in general there is little cumulative effect of the cleaning process on subsequent neuronal health. There are two points that need clarification here.

1) Do the authors expect that the results with mature human brain tissue will be equivalent to that with young rat brain tissue? Is there any limitation we should be aware of in this validation experiment.

2) Were the same neurons ever repatched following cleaning? This would allow for direct comparison of neuronal properties before and after patch pipette cleaning.

In addition, since each patch electrode was used more than once, arguably the relevant statistical comparison here is repeated measures ANOVA, rather than group population statistics, as appears to have been reported in Figure 3J, K and L.
