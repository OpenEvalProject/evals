# Peer review - Round 1

Editors:
- J Andrew Pruszynski, https://ror.org/02grkyz14 Western University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67620.sa0](https://doi.org/10.7554/eLife.67620.sa0)

This elegant study furthers our understanding about the mechanisms by which distributed systems control rhythmic movements of different speeds. The authors trained an artificial recurrent neural network to produce muscle activity patterns similar to those that monkeys generate when performing an arm cycling task at different speeds. The dominant patterns in the neural network do not directly reflect muscle activity, and these dominant patterns do a better job than muscle activity at capturing key features of neural activity recorded from the monkey motor cortex in the same task. In addition to the main result, the study provides a particularly clear example of how thinking in terms of network dynamics can naturally explain empirical observations in terms of the computation being performed.


---

# Peer review - Round 1

Editors:
- J Andrew Pruszynski, https://ror.org/02grkyz14 Western University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67620.sa1](https://doi.org/10.7554/eLife.67620.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Motor cortex activity across movement speeds is predicted by network-level strategies for generating muscle activity" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Andrew Pruszynski as Reviewing Editor and Joshua Gold as Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The reviewers raise a number of important points about the RNN, the characterization of its dynamics, and its relationship to the empirical data. This includes further details about the network and analysis but also a broader perspective on the interpretation. Three notable considerations along these lines are: (a) establishing whether strong interactions between the "dominant" dimensions generate the rhythm while muscle-related dimensions do not push on these dominant dimensions; (b) further consideration about the constant inputs into the network and the implications of this choice in terms of the observed relationship to M1 activity and overall interpretation; (c) explicitly laying out what muscle like commands would look like.

2) The long-term impact of this study could be increased by providing a more comprehensive high-level discussion about the relationship between the extracted PCs and the computations done in motor cortex. Use this as an opportunity to link the present work to more traditional concepts in the field like the representation of motor commands.

Reviewer #1 (Recommendations for the authors):

1. Was the torque applied by the animals to the handle measured at each speed and is an estimate of the handle's damping ratio available?

2. The authors state that data windows of variable length were used "to avoid overly specific solutions." Was this done to enforce a return to a stable fixed point when the inputs switch to zero, independently of the movement phase at which this switch occurred?

3. The authors may wish to comment on whether the RNN dynamics in the dominant dimensions might be topologically equivalent to a simple canonical model. Intuitively, it looks like the network trajectories might obey something like θ' = cs, r' = r(1 – r^2), z' = s – z, where θ is the angle in the x-y plane, r is the radius, z is the vertical dimension, s is the speed input, and c is a constant. Establishing the existence of smooth transformations from the vector fields learned by the networks to a canonical model would bolster the claim that the networks have found the same general solution, but this analysis is not critical.

4. More details on the RNN and fitting could be provided in the Methods. What values were chosen for the time constant τ and time step Δt? If I understand correctly, the node state does not depend explicitly on speed, so the notation v(t,s) (line 754) was slightly confusing.

Reviewer #2 (Recommendations for the authors):

How do the stacked ellipses observed here resemble or not resemble the spiral trajectories observed in SMA during motor sequences?

Reviewer #3 (Recommendations for the authors):

This study is a further examination of the dynamical-systems (non-representational) view of the motor cortex, and its relation to motor execution and muscle activity. It combines modeling with single-electrode neural and EMG recordings in two monkeys, using the cycling paradigm that this group has developed over the last number of years. In particular, they examine the question how each of these signals (including modeled manifold solutions) change with the speed and direction of pedaling. The experiments are well designed and the paper is clearly written, with the occasional lapse into excessive neural or mathematical jargon. In addition to the central questions the authors pose, it provides a good discussion of the nature of these dynamical models, what we can learn from them, and what is still unknown. I have no major concerns.

The one methodical approach that should be presented more clearly is that of the "population recordings" from M1:

22: "…we recorded motor cortex population activity during the same task."

76: "We compared network solutions with empirical population activity recorded from motor cortex.

Describing post-hoc time-aligned single-electrode recordings this way is a bit of a stretch. I was actually confused for a while, assuming initially that the neural trajectories must all have been from the ANNs. It is compounded by the fact that there is no explicit discussion of this issue, which I would recommend adding. The same concern applies to the EMGs, though less so. I doubt there are any significant issues, but it should be acknowledged.

In a similar vein, I was occasionally lost, trying to figure out which results came from the artificial networks and which from electrodes. There is at least one reference to "empirical" networks, an adjective I've never found terribly useful as a reference to something in the brain as opposed to the computer (perhaps, "recorded", "actual"?). This was mostly an issue when I was thinking the manifold responses must all from the networks, with comparisons make to only single electrodes, but it might help to make more explicit reference consistently to ANNs.

I find the relation between the initial (elliptical, non-muscle-like) PCs and the higher-order ones intriguing. Are the former "pulling along" the latter to produce a muscle-like output? Are they somehow doing separate computations? is it all just a computational trick that separates them?

One reference to the literature that gets swept aside to quickly is this:

485: "For example, autonomous dynamics provide a poorer fit to the data during grasping…"

To the extent that this comment reflects the effect of afferent input during object manipulation ("Tangling will also be high when unpredictable external inputs dominate…"), it should be noted that their data did not include contact. This observation remains an important one.
