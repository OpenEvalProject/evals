# Peer review - Round 1

Editors:
- Stefan Glasauer, Ludwig-Maximilian University of Munich Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.28074.036](https://doi.org/10.7554/eLife.28074.036)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A unified internal model theory to resolve the paradox of active versus passive self-motion sensation" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Senior Editor and a Reviewing Editor. The following individual involved in review of your submission has agreed to reveal his identity: Laurence Harris (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This very timely and comprehensive theory paper studies the way self-motion may be estimated by the brain and mainly concerns the vestibular system during active and passive head movements. In particular, it suggests a unified theory for how active and passive motion can be estimated by a single internal model. This extends previous, well-established work by the authors and others applying internal models to the problem of estimation of passive motion. A Kalman filter framework was used to determine optimal (Bayesian) solutions. The paper draws on a considerable amount of previously published experimental evidence from a rich series of elegant experiments to argue the hypothesis and to consolidate a large amount of previously collected data into an explanatory model. The internal forward model proposed here is used to make a series of specific experimental predictions (mainly found in the supplementary information). The model's mathematical development and execution is very thoroughly motivated, as it draws on a solid body of previous computational work. The manuscript did an excellent job of simplifying the description of such complex models. Model simulation results are shown for different scenarios and compared descriptively with neurophysiologic evidence. A particularly strong point about the paper is that it makes multiple testable predictions and could be used, for example, to predict the consequences of experience in microgravity. The principle of this type of model may find application beyond the situation considered here, for example, in looking at how the sensory consequences of an eye movement are combined with retinal information to provide the perception of an apparently stable world (e.g., Bridgeman et al. 1994).

The reviewers appreciate the structure of the paper and the systematic testing using different conditions building in complexity. The unusual interactive connection with the supplemental material to try and keep the main paper shorter is also appreciated.

Essential revisions:

1) Novelty: A major concern for the paper is the nature of the advancement of our understanding of computational principles in the brain: Internal forward models, priors and their impact on error-based movement correction have been extensively studied in the human reaching / motor control literature (from Wolpert et al. to Bernicker et al.; some of this should be mentioned to make a connection to this body of literature) and as such their ability to explain active and passive motion (of arms) are not especially novel. Thus, the main advance must lie in the domain of vestibular information processing, which needs to motivated better.

2) Cancellation mechanism: The authors state that "we have tested the hypothesis that this postulated cancellation mechanism uses exactly the same sensory internal model computations…." While the authors have put forward one framework that explains a variety of phenomenon, the reviewers wonder if other models could also explain these phenomena. Perhaps (at least for some of the scenarios) the motor command could be subtracted from the sensory estimate of a "passive only" internal model and yield the same response. This should be addressed by a comparison to an alternative "subtraction model". The simple model is probably what people naively think might be the case and so demonstrating its failings might give the paper more impact.

3) Reliance of motor command generation: The model does not include an additional feedback pathway – the reliance of motor command generation on sensory estimates. For example, a passive head movement could result in a stabilizing active motor command. Or an active head movement could be less than desired because of noise, requiring an adjustment of the motor command to compensate. Obviously these additional pathways complicate the solution to the Kalman filter gains. While the model is still an important contribution without these pathways, the limitations of the model without these pathways should be addressed.

4) Motor commands: The authors assume that the motor command is a noiseless signal that is perfectly executed. This apparently doesn't account for motor error, since the effect of motor commands is not deterministic and noiseless, as assumed by injecting the motor command as Xu (see Figure 1B) into the system model. It seems that this ignores motor noise and execution noise, even though these sources of noise are extremely important (see work by Wolpert and others). In the second paragraph of the subsection “Model of motor commands” the authors claim that 𝑋𝜀 includes motor noise, but this is not evident and needs to be discussed better. Motor noise would, in this reviewer's opinion, enter before applying M and therefore would have a different noise spectrum and/or covariance matrix than the system noise 𝑋𝜀.

An alternative view would be that processed efference copy signals (i.e. predicted sensory signals) have to be treated the same way as other sensory signals, because 1) the efference copy just like any neural signal cannot be assumed to be noiseless and 2) it would take into account the motor noise appropriately (instead of treating it as external perturbation). Is that view wrong? Or would it provide an alternative to your present model? It seems to me that approaches such as described in papers by Wolpert et al. would consider efference copy input as containing noise. For example, MacNeilage and Glasauer (Front Comput Neurosci 2017) assume that vestibular and efference copy signals are combined like two sensory signals, weighted by their reliability.

5) Reference frames: a theoretical concern is how do the motor signals (and proprioceptive signals) arrive in the correct form and frame of reference to be compared to the sensory information?

6) Active vs. passive movements: As mentioned in the text (subsection “Interruption of internal model computations during proprioceptive mismatch”), the current model cannot reproduce some important results concerning active movements: when active head movement is blocked or torque is applied, "central neurons were shown to encode net head motion". The authors suggest that this "result may be reproduced by the Kalman filter by switching off the internal model of the motor plant.…". However, this actually means that the Kalman filter model fails to explain this result, because it would need another element. What the authors propose here sounds like an ad-hoc extension of the model (a switch) to explain results, which can as well be interpreted as evidence against the model. It is important to discuss this more appropriately.

In the second paragraph of the aforementioned subsection, the authors suggest that "proprioceptive mismatch" would cause to stop using the internal model. However, that seems a bit oversimplifying: Proprioceptive mismatch occurs due to a variety of natural conditions (e.g. increased head inertia due to carrying food, or due to fatigue, etc.) for which it would make no sense at all to completely stop using the internal model.

7) Parameter variations: Technically, systematic parameter variations to test for the robustness of the model predictions are missing (which can be easily addressed).

8) One reviewer would also like to see more quantitative results showing time courses of adaptation in the model and e.g. firing rates match up with each other. This brings up the question of whether the model does adapt or whether all Kalman filters operate with steady state gain (as suggested by another reviewer).
