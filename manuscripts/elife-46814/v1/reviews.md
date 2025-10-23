# Peer review - Round 1

Editors:
- Ronald L Calabrese, Emory University United States

Reviewers:
- William S Ryu, University of Toronto Canada
- Elizabeth Cropper, Icahn School of Medicine at Mount Sinai United States

## Review text

DOI: [10.7554/eLife.46814.027](https://doi.org/10.7554/eLife.46814.027)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A model of conserved global neuronal dynamics predicts future behaviors in Caenorhabditis elegans" for consideration by eLife. Your article has been reviewed by Ronald Calabrese as the Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: William S Ryu (Reviewer #1); Elizabeth Cropper (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper reports a "coarse" grain model that takes whole "brain," single-neuron calcium data from C. elegans and provides behaviorally relevant results using a manifold detection method based on diffusion mapping. The paper is technical enough to be of interest to specialists, but written in a way that is accessible and potentially interesting to a general audience. The Materials and methods sections is particularly clearly presented.

Essential revisions:

While there was considerable enthusiasm for the approach, there were several concerns that must be addressed before publication. The expert reviews are appended and will be of critical importance in the revision. The most important concerns are:

1) The data is from constrained animals and this impacts the interpretation of the results. Reviewers #1 (comment 1) and #3 (comment 1) share this concern and have specific prescriptions.

2) Not enough detail is provided about the model itself. Reviewers #1 (comment 2) and #3 (comment 2) share this concern and have specific prescriptions.

3) The time scale of the delay embedding is a concern and should be addressed as called for in comment 5 of reviewer #3.

4) There was a concern that predicting behavior based on the data that was used to define behavior is circular. To justify the conclusions the authors should show that the conclusions continue to hold when using the data without AVA (comment 3, reviewer #3).

5) There was a concern about neuronal identification in the data. This concern is difficult to address since the authors rely on published data and are not themselves doing the neuronal identification. The authors should combine a discussion of the robustness of their analysis with respect to neuronal mis-identification (especially considering that neuron identification for large scale recordings is still a major technical challenge for many labs) with a general robustness analysis for the previous point, where they would remove AVA and systematically explore how removal/identity shuffles would affect the resulting manifold and prediction. If this discussion and analysis is provided, the authors need not address reviewer #3, comment 4 further.

Title

The authors should consider revising the Title to reflect reviewer concern about whether the model is predictive.

Reviewer #1:

This is a very nice paper describing a "coarse" grain model that takes whole "brain," single-neuron data and provides behaviorally relevant results. The paper is technical enough to be of interest to specialists, but written in a way that is accessible and potentially interesting to a general audience. The Materials and methods section is particularly clearly presented. I think the work clears the bar for eLife.

1) Since the data are from constrained worms, it is not clear to the reader how these behavioral states were measured. A naive reader would assume behavior labeled as "forward locomotion," "reverse," etc. would come from observations of moving worms independently and not from interpreting the global brain signals themselves. Anyway, this can be made clear up front without asking the reader to go through Kato et al. For example, for Figure 2A, the authors explicitly write that they used the AVA signals to define the start of forward locomotion. What about the rest of the defined behaviors?

2) Not enough detail is given about the model in order for the reader to appreciate the jump from Figure 1 to Figure 2. The authors reference Figure 1—figure supplement 1 early in the Results sections but I would think something like Figure 4 would be necessary for the reader to be able to assess Figure 2. There should be enough technical detail given in the text so that the model is understandable.

3) Maybe this is a minor point (or an argument of semantics), but does the model really predict behavior of C. elegans up to 30 seconds in the future? Or does it predict the probability of a stochastic transition at some time T and so the event has some expected time, t, and manifests itself observably at t on average. The Title of the paper reads as if the signals deterministically predict future behavior.

4) A natural question is raised when discussing the number of neurons needed to see similar global brain dynamics. From 100 neurons to 15 neurons to 8 neurons. How far can one go for this specific dataset?

Discussion section. "C. elegans do not fire action potentials." Not strictly true. For example, see: Liu et el., 2018

Reviewer #2:

This report takes advantage of the powerful tools that have been developed that make it possible to relate neural activity to behavior in C. elegans. Namely, imaging techniques with single neuron precision can record activity in intact worms as they freely switch between different forms of locomotion. It is therefore possible to do more than simply correlate an activity pattern with a behavior. The temporal evolution of behavior can be characterized. There are not many systems where this can be accomplished, and this is a very exciting area of research. A potential 'drawback' of experiments like this that generate so much data is that data can be difficult to analyze and interpret. Studies such as this that develop tools for this purpose are therefore clearly needed.

These authors use imaging data to construct a model of neuronal dynamics. Their approach is novel, and differs from traditional approaches in that it does not proceed in a 'bottom-up' fashion (it was not built by characterizing all of the biophysical properties and synaptic connections of the neurons in the network). There are a number of drawbacks to the bottom-up approach, as the authors point out. For example, an assumption usually inherent in this type of work is that a particular network output is encoded by one set of circuit parameters. Work in other systems has indicated that this is not necessarily the case, and the authors demonstrate that activity in identified neurons in C. elegans is variable during the behaviors studied.

The tools that the authors develop extract information from a subset of the neurons that mediate behavior. There are hundreds of neurons in C. elegans but the authors were only able to consistently identify fifteen. This speaks to the potential utility of this method since it is generally not possible to record from all of the neurons in a network of interest. This is, however, not simply a 'methods' paper. The authors use their techniques to simulate neuronal activity and interestingly demonstrate that these simulations can be used to predict behavioral switches before they occur in a different cohort of animals (i.e., not the animals used to develop the model). Finally, the authors construct manifolds using specific data sets (e.g., activity of the fifteen identified neurons recorded from in four out of the five animals of the study) and demonstrate that left out data are well approximated by these manifolds. Taken together, this research comes to a fundamentally important conclusion – that global dynamics in the functioning of the nervous system are conserved despite the fact that there are differences in the activity of individual neurons.

Reviewer #3:

The authors of "A model of conserved global neuronal dynamics predicts future behaviors in Caenorhabditis elegans" re-analyze existing wholebrain calcium data from C. elegans using a manifold detection method based on diffusion mapping. Based upon the current manuscript I have a few concerns that if addressed would significantly improve the clarity of the manuscript.

1) My main concern is the interpretation of the results as predicting behavior: From the Title and the main text it is unclear to the reader that the animals in question are actually immobilized (according to Kato et al. these animals are in microfluidics and sometimes even treated with a paralytic). Kato et al. show that animals where AVA is silenced do not perform any reversals, but the global brain dynamics are still observed. This indicates a loose connection between these manifold dynamics and behavior at best. Kato et al. also reported that prolonged activation phases of neurons such as RIM only occur in immobilized animals, not in freely moving ones, indicating that immobilization changes neural dynamics. Based upon these caveats in their data, I urge the authors to carefully re-word their interpretation of their results as 'behavioral coding', and be more careful about this wording throughout, but particularly in the Discussion and the Title.

2) Reading the paper, it is unclear if the authors main goal is to present a method or to describe new findings. If the main goal is to present a generalizable method, the authors should be much more explicit about the steps of the data analysis process. In the current manuscript, the model is not described in the main text at all (subsection “ng neuronal dynamics give rise to neuronal activity” introduces the model without describing any of its properties). In either case, I strongly urge the authors to either present a cartoon or an example data set that underwent all of their processing, embedding and dimensionality reduction, etc. If I read this manuscript as a methods paper, I would like to see how parameter choices (in particular delays, smoothing parameters, numbers of dimensions chosen after reduction) affect the outcome. This could be done on purely synthetic data even.

3) As far as I can tell from the methods, the 'behavior' is deducted from the activity of the motor command interneuron AVA. AVAL and AVAR also appear among the 15 neurons that are common between datasets. It seems that AVAR and AVAL were not removed from the data used to create the manifold. Predicting behavior based on the data that was used to define behavior seems circular. It would strengthen the conclusions if they were still true from the data without AVA.

4) Neuronal identity: The analysis by Brennan and Proekt relies on unambiguous identification of the neuronal identity. The conclusions about variability in activity between neurons (Discussion section), and the fact that PCA does not create reliable manifolds could possibly indicate that a subset of the neurons were mis-identified. On a subset of only 15 common neurons, even one misidentified neuron could possibly have a large impact. From the periodic, low dimensional example dataset shown in Figure 1, and the somewhat consistent PCA weights shown in Figure S2 of Kato et al. this conclusion is surprising and could be better supported to motivate the more complex strategy presented in the paper.

Relatedly, one of the first findings presented in Figure 1 is that there are consistent statistical differences in the activity of the same neuron across animals. Based upon single neuron Calcium imaging, it is not surprising that neurons are showing diverse activity in 'behaviors' they do not control. Comparing these data with previous studies on variability in neural activation (Gordus et al., 2015 for example) could provide context for these observations.

5) Timescales: Delay embedding is highly sensitive to the chosen timescales of the delay(s). The authors used a delay of ~4 seconds. However, the highly periodic nature of the neural activities (see e.g. Figure 1A, cyclic activity in most neurons) means that the auto-correlations will also have periodicity and signals will have non-zero auto-correlation over significantly longer times. The authors could show the auto-correlations explicitly and show how the delay embedding changes with significantly longer delay times or using a different method such as mutual information to calculate the delay. I suspect the signals have auto-correlation times much longer than 30 seconds.
