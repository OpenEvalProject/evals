# Peer review - Round 1

Editors:
- J Andrew Pruszynski, Western University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.57021.sa1](https://doi.org/10.7554/eLife.57021.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The present modelling study and non-human primate experiments suggest a new theory for the origin of the speed-accuracy tradeoff, a key feature of motor behavior across effectors and contexts. The authors posit that, rather than signal-dependent noise, the speed-accuracy trade-off arises because of planning variability. That is, more difficult task demands (i.e. smaller targets) reduce the availability of good control solutions (i.e. fast reaches).

Decision letter after peer review:

Thank you for submitting your article "High-fidelity musculoskeletal modeling reveals a motor planning contribution to the speed-accuracy tradeoff" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Andrew Pruszynski as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Ronald Calabrese as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Friedl de Groote (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional work is required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

The present paper presents a novel theory for the origin of Fitts' Law, that is, the speed-accuracy trade-off observed across movement tasks. The most prominent current theory suggests that the speed-accuracy tradeoff emerges due to the optimization of movements in the face of signal-dependent noise. The authors suggest that, under a physiologically realistic simulation of the arm, motor planning in the absence of motor noise can also give rise the speed-accuracy trade-off. The simulation predictions are coupled with behavioral data from a straightforward human reaching experiment and the simulations are linked to a potential underlying neural mechanism via single-units recordings obtained from a macaque monkey doing a similar reaching task.

All three reviewers thought that this is an interesting and provocative study that may provide an important new perspective on the origins of Fitts' Law, the implications of which would be very broad. However, all three reviewers converged on a set of common concerns about the current version of the paper that need to be addressed.

Essential revisions:

1) All the reviewers raised substantial concerns about how the authors handle physiological noise in their simulations. There were two related issues.

a) In the present version of the model, muscle activation terms are squared and the authors suggest that this serves as an approximation of metabolic power consumption. The reviewers raised the point that, in other contexts, minimizing squared muscle activations has been interpreted as minimizing motor noise (i.e. acts like the kind of signal-dependent noise term). It is important that the authors clarify how this term influences the ability to make a clean separation between the hypotheses being tested.

b) Physiological noise is an established phenomenon that is not included in the present model. The reviewers understand why the authors chose this route (both conceptually and practically) but thought it would be important to show what happens when physiological noise is included. In this case, would the same optimization procedure with the same cost function converge similarly on a Fitts law-like solution? How would the optimized control signals in this case differ from the ones they found presently?

2) All the reviewers raised the substantial concern that the present work does not establish a meaningful link between the optimal control model being proposed – and its reasons for showing Fitts' Law – and a sensible neurophysiological analog. That is, what neurally feasible computational mechanism occurs during movement preparation that produces greater variability for small targets. Given the present model algorithm does not seem feasible, what to the authors have in mind? At the very least, the authors need to provide more complete discussion about how their algorithm relates or does not relate to neurophysiological mechanisms.

3) The authors claim that a major factor that allows them to better investigate the origins of Fitt's Law is their physiologically realistic model of the upper limb. However the authors do not make any attempts to investigate which aspects of the model specifically are responsible, either alone, or in combination, for the observed effects. An analysis of the sort described by Lillicrap and Scott (2013, Neuron) would seem helpful here.

4) The description of the approach lacks important details. CMA-ES with a population size of 20 was used but it is not clear what parameter settings are used for sampling and how these settings influence the results. The authors refer to the solutions of the CMA-ES algorithm as local optima but this may not be mathematically correct as the number of iterations was predefined and optimality criteria were not evaluated. Also, it seems that the target was not successfully reached in all trials. For example in Figure 1B, the most rightward target is not reached. Finally, muscle excitations are prescribed every 100 ms only. This limits the set of feasible solutions. Would the results be different when increasing the number of controls (which might be more realistic physiologically)?

5) Methods related to the NHP work are lacking. In Figure 4, the authors talk about not using spike sorting and just using threshold crossings. Why? What are the implications of this approach. In general, methods associated with the monkey data are not described in the Materials and methods section. This needs substantial work to be acceptable.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your article "High-fidelity musculoskeletal modeling reveals a motor planning contribution to the speed-accuracy tradeoff" for consideration by eLife. Your revised article has been reviewed by three peer reviewers, including Andrew Pruszynski as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Ronald Calabrese as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Friedl de Groote (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

As you will see, the reviewers all thought that you did a very good job addressing their concerns and remain very enthusiastic about your work. There are however two important issues that remain outstanding, which the reviewers all believe need addressing to ensure the paper provides the advance it hopes to provide.

Revisions for this paper:

1) Previous concern #3 was not addressed and is seen by all reviewers as being very important for interpreting the findings. Specifically, the comparison is still limited to the torque-driven model and the fully complex model. The reviewers believe that it would be feasible to follow the approach of Lillicrap and Scott (2003) to assess which aspects of the model are responsible for the observed effect and that the insights gained from such assessment would be very valuable.

2) There remains a disconnect between the results of the modeling exercise and the neurophysiological data - a gap that one might expect to be bridged by a theory or model, which is still absent. In the simulations, the model behaves according to Fitt's Law because built into the model is a sort of explicit "search" within a subspace, a search that takes time. In the model this search happens pre-movement during what the authors call a movement planning epoch. The neural data are centered around a pre-movement time epoch as well, but clearly the brain is not literally executing an algorithmic "search" during this time. The reviewers all believe that, for this paper to have the desired impact, more discussion is needed to bridge the gap between the model and the nervous system.
