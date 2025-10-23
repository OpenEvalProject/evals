# Peer review - Round 1

Editors:
- Michael J Frank, Brown University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.20944.020](https://doi.org/10.7554/eLife.20944.020)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Matching tutor to student: rules and mechanisms for efficient two-stage learning in neural circuits" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Michael Frank as the Reviewing Editor and Andrew King as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This is a careful and well-designed study of the role of the matching between plasticity rules and instructive signals for efficient learning in a two-stage model, wherein the reinforcement signal is processed by one circuit that in turn provides input to another circuit that drives the actual behavior. This is particularly applicable to recent detailed findings in the birdsong field. Several important results are laid out in the manuscript: (1) matching is important for fast learning, (2) matching is not as important when the tutor timescale is shorter than STDP timescales (3) similar results are obtained for rate-based or spiking-based models, (4) learning drives student neurons to become more bursty, (5) learning drives pruning of connections in spiking networks, and (6) sequential learning is obtained when the tutor memory is long.

Essential revisions:

All involved found the work to be of high quality and of broad interest to researchers in sensorimotor and reinforcement learning, as well as being of particular interest to those working on neural recording in the songbird brain.

1) However, an invigorating consultation session among the reviewers was needed to get down to the bottom of whether some of the main modeling results were circular/trivial or not. It was determined that in fact they are not, and that rather some of them show that the model is robust to the precise form of the motor error. But the reason for this initial difference in opinion could be traced to a lack of clarity in the manuscript over the definition of tau_tutor. One reviewer originally understood it as the timescale over which the firing rate of the tutor neurons is modulated, which led to the conclusion that g(t) is constrained to have a timescale of tau_tutor, which would mean that the main finding that your results "predict the temporal structure of the [LMAN signal] given a plasticity rule" – would be a trivial consequence of the plasticity rule….

However, as explained in a small sentence above Equation 1, what tau_tutor actually refers to is the timescale over which motor errors are integrated into the firing of tutor neurons. This definition of tau_tutor is specific to the Taylor series approximation taken in A.8 and hence, their matching results point to the robustness of the model. One way to summarize the finding is if you want to use an STDP rule in motor learning, you should convolve your motor error signal with a particular exponential smoothing function, with a particular timescale related to the plasticity rule, independent of the form of the motor error signal.

Another interesting observation is that their derivation for the timescale tau_tutor is not valid when tau_tutor is of a comparable magnitude to tau1 and tau2. Stated simply, they make an assumption in their derivation that tau_tutor >> tau1 and tau2. Therefore, they don't see clear matching in areas where this assumption is violated. A discussion of this in subsection “Match vs. unmatched learning” may also improve the readability of the paper.

The authors should comment on what they would conclude if one observed a different form for g(t) in the songbird brain. It's a subtle point – a g(t) with the \tau^* they predict would certainly shore up their theory, but one with a different form might mean either a) that their theory is wrong, or b) that their approximation (A.8) is wrong.

2) Both reviewers strongly agreed that more is needed to motivate what the model predicts. In the Abstract and Discussion, a claim is made that the results presented here make clear and testable predictions for experimentalists. The manuscript would be greatly improved if this were made more explicit and specific. Indeed, explicitly connecting the model to falsifiable experimental predictions would make the difference between this being a paper of truly broad interest.

Perhaps the authors envision revealing the precise form of the plasticity rule by looking at the structure of the tutor signal. Perhaps they envision inferring the form of the motor error signal. Perhaps they will test coarser effects that result from this kind of tutor signal, like the progressive clumping of student responses into burst-like events during learning. If these predictions were laid out more clearly, concerns about what exactly is being claimed through the calculation in Appendix 3 would be ameliorated.

A couple of other suggestions for how the manuscript might be revised are given here:

– The point \α = \β is the case that corresponds to the study by Mehaffey and Doupe, so a detailed discussion of the tutor \tau's that yield reasonable learning in that part of parameter space would be useful. How big is the range of \tau_{tutor}'s in that case? Does it span many orders of magnitude? How well does the model activity at these points align with real LMAN activity in the developing bird?

– What precise features of the firing of LMAN neurons are predicted for the models that yield efficient learning and match known plasticity features? What should an experimentalist measure in their spike trains? Putting some numbers to the predictions would be great.

3) One reviewer thought that Figure 3C is not very convincing that learning is good only along the diagonal. It does not seem to matter at short timescales (which the authors discuss briefly), where performance is equivalent regardless of whether timescales are matched or unmatched (e.g. 10 ms vs 80 ms). But even at timescales >80 ms, the performance does not seem strictly diagonal, and the asymptotic performance of the model is significantly worse than at shorter timescales. Therefore it seems like the two key findings – timescale matching and the ability to learn – do not coexist. The other reviewer noted that the error is on a log scale is very important here. There is a steep valley sloping towards the diagonal. The larger error reached at longer timescales was thus less worrisome. 3B shows that this amount of error doesn't stem from huge differences in the output time course. We would therefore like to ask the authors for another plot like B at yet longer timescales to see how and if things break down. Also, 250 iterations isn't that many in terms of number of renditions sung during development, and we might want to see what the error surface looks like after a few thousand. Finally, the paper does discuss the flattening of the valley at short timescales, but this could be expanded.

4. It seems misleading to call τ1 and τ2 the timescales of synaptic plasticity of the student. They are simply timescales of two exponential kernels that are linearly combined to create the final filtering kernel. If the authors want to relate τ1 and τ2 to the timescales of synaptic plasticity, they should include a discussion of how and why they consider them to be related. In general it would be helpful if the authors are more clear in defining their variables through the paper – especially since tau1 and tau2 are very different from tau_tutor.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Rules and mechanisms for efficient two-stage learning in neural circuits" for further consideration at eLife. Your revised article has been favorably evaluated by Andrew King (Senior editor), Reviewing editor Michael Frank, and one external reviewer.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined clearly by the reviewer below:

By and large we are happy with the changes the authors have made.

However, there are still a few important aspects of the paper that need to be significantly revised to improve clarity and address some issues of interpretation:

1) The (qualitative) definition of tau_tutor could still be much clearer. When we first read the initial submission, we mistakenly thought that tau_tutor represented the timescale over which the firing rate of the tutor neurons is modulated, rather than (as is actually the case) the timescale over which motor errors are integrated into the firing of tutor neurons. Based on our comments from last time, the authors have somewhat clarified this, however this could still be more clear (in fact, I got confused in the same way reading the revised paper). We think this could be easily clarified with a couple of minor changes

a) Just above Equation 4, revise to "Moreover, for effective learning, the timescale t_tutor – ***which quantifies the timescale on which error information is integrated into the tutor signal*** – appearing in Equation 3…" (or something similar).

b) Be a bit more specific when talking about "matching". For example, the first sentence in 2.3 simply reads "…when the tutor is matched to the student…". I think it would be much better (especially for less quantitative readers) to explicitly state what is being matched by expanding this to read something like "…when the ***timescale on which error information is integrated into the tutor signal (tau_tutor) is matched to the student plasticity rule***…".

c) More generally, throughout the paper replace the term "tutor timescale" – which many biologists will misinterpret as the timescale on which tutor activity varies – with "tutor error integration timescale" or something like this.

2) We appreciate the authors expanding the duration of simulations and range of timescales tested in the simulations shown in Figure 3C and 5D. However, the authors should be more explicit (and consistent) in explaining how these simulations are conducted. My understanding is that in Figure 3C, tau_1 and tau_2 are fixed at [80 40]msec, and to obtain a particular t_tutor*, plasticity parameters α and β are adjusted for each simulation (subject to the constraint α-β=1). Provided this is correct, the fact that α and β were different for different simulations (i.e. for different squares in Figure 3C, 5D) should be explicitly stated in the results text and/or legend to Figure 3. Similarly, as far as I can tell a similar approach (fix tau_1,2, vary α/β to get a particular tau_tutor*) was used in the analysis shown in Figure 5D. However, this is not made clear in the text/caption (I find the caption to 5D especially confusing). Authors should explicitly state the procedures for 5D and explain any differences in the general methods used in 3C. Furthermore, the authors should present (maybe as a supplemental figure) the values of α or β used for all simulations (e.g. a heatmap of α values to go along with Figures 3C and 5D).

3) The following is a somewhat subtle point, so I'll leave it up to the Authors to deal with as they see fit.

As noted above, tau_tutor is the timescale over which motor errors are integrated into the firing of tutor neurons. Furthermore, the various models (linear rate, spiking, etc.) can work over a big range of tau_tutors, say from 10ms-1280msec, as shown in Figures 3C and 5D. In the revised Discussion, the authors correctly assert that LMAN/tutor firing "should reflect the integral of the motor error with the timescale predicted by the model". The authors also correctly point out that we don't really know what the motor error signal looks like.

However – a key physiological fact is that firing in the "tutor" brain area – LMAN – consists of both short bursts (~15 msec duration) as well as single spikes whose overall rate varies much more slowly. So, although we don't know how fast the error signal varies, even if the error signal were a pulse that only lasted, say, 1 msec, it would affect the firing of the LMAN neuron on timescale tau_tutor – e.g. over >100 msec if tau_tutor=100. So, if I'm getting this right, it seems implausible that a 15 msec burst in LMAN could possibly reflect motor error – even an infinitely brief motor error – if tau_tutor were longer than, say, 50 msec. The authors may want to discuss this issue, especially whether their model suggests that only slow changes in the rate of single-spikes, and not bursts, are carrying error information? I think that such an implication is both important for understanding the implications of the model and for guiding future work in the system.

Additionally, as indicated just below Equation 4, the model assumes that tau_tutor>>tau_1,2. In many simulations (definitely in Figure 3C, also I think in Figure 5D, see my question above), tau_1 and tau_2 have values of 40 and 80 msec, which are values derived from the Mehaffey and Doupe STDP paper. This would suggest that tau_tutor should be >>80 msec, and that cases with tau_tutor and tau_tutor* less than this value (which make up a significant region of the parameter space shown in Figures 3C and 5D) are biologically implausible. This seems to me to be something the authors should address.
