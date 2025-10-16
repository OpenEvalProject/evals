# Peer review - Round 1

Editors:
- K VijayRaghavan, https://ror.org/03ht1xw27 National Centre for Biological Sciences, Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81527.sa0](https://doi.org/10.7554/eLife.81527.sa0)

This article uses a genetically encoded calcium indicator to assess neural activity across a population of axons connecting the fly’s brain to its ventral nerve cord while the tethered fly behaves on a floating ball. The preparation and large-scale analysis represent a significant step forward in determining how the brain compresses sensory and state information to convey commands to the ventral nervous system for behavior execution by motor circuits.


---

# Peer review - Round 1

Editors:
- K VijayRaghavan, https://ror.org/03ht1xw27 National Centre for Biological Sciences, Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81527.sa1](https://doi.org/10.7554/eLife.81527.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Descending neuron population dynamics during odor-evoked and spontaneous limb-dependent behaviors" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and K VijayRaghavan as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The authors use a challenging preparation in which they were able to record from up to 100 DNs simultaneously in tethered flies performing spontaneous and odor-evoked behaviors on a treadmill. They combine their recordings with motion capture approaches and automated behavioral classification, which allows them to correlate DN population activity with behavior on an unprecedented scale. This approach is valuable and adds a different perspective to previously published studies aimed at tying individual, often command-like DNs to different behaviors and characterizing their activity in detail. The authors use relatively complex analysis methods, which is necessary due to the rich behavioral and neuronal activity data sets. In several instances, they verify that their conclusions drawn from the output of their analysis pipeline hold when tested with more simple and common analysis methods (see for example Figures 5g or 4c). After correlating the activity of the DN population with aspects of walking and grooming, they outline an approach that allowed them to identify a single pair of DNs from the population data set. Overall, the study combines several cutting-edge methods and significantly adds to our understanding of descending motor control. For example, the authors demonstrate that a large number of DNs likely contributes to turning, whereas changes in walking speed are encoded, perhaps driven, by fewer, more distributed DNs.

In our consultation, we agreed that the data and presentation are strong, and the biological findings are important. Some word choices are confusing, and some additional discussion of implications, comparisons, or limits is warranted, but can be achieved with text revision. It is with this in mind that the major points are to be addressed. These points are given below.

1) The use of the word "encoding" is problematic. It may be best reserved for when we know that a neuron's activity pattern occurs in direct response to specific sensory inputs or causes specific motor outputs. The changes in fluorescence seen here correlate better with certain behaviors than others, but the sensory input is not controlled, the time resolution is limited, and the causality is not shown. The experimental data is fine – but we would describe it as signal correlation rather than encoding.

We would prefer to see that word – encoding – removed. If not, an early definition and an extended Discussion of the way the authors are using the word with a clear presentation of the caveats would be acceptable.

2) How do the authors handle statistical significance in rare behaviors or comparisons of correlation strength between behaviors that occur with different frequencies? Turning doesn't happen that often. Particular combinations of joint angles might not be common. If you bin all of the micromovements that compose grooming, you'd aggregate a lot more signal than for any of the individual limb positions. Do you normalize by time? This is a concern for assessing the conclusion that the calcium signal correlates better with higher-order behavior categories (walking or grooming) than it does with shorter, rarer movements or limb positions.

3) In their experiments, the authors did not perturb the activity of any of the DNs, either by activation or silencing. Moreover, the temporal resolution of the DN population recordings is relatively low compared to, for example, single cell patch-clamp recordings. This is fair given the scope of the study, but as a consequence it remains unclear whether a DN whose activity is correlated with a certain behavior is driving this particular behavior, or whether the DN is activated because the behavior is executed. The latter could for example be due to sensory feedback. This caveat makes it challenging to interpret the results presented since a causal link between DN activity and behavior cannot be assumed. Overall, the authors are relatively careful when interpreting their data, but there are several instances where they overinterpret their findings. These instances need to be addressed and clarified:

– The statements in line 63ff regarding the reasoning for using an approach that allows parallel recordings from many DNs do not seem ideal for several reasons:

a) To resolve how different DNs modulate ongoing behavior, it seems the best approach would be to activate these DNs individually or in groups to get an idea of their behavioral effects and establish causality, as opposed to correlating their activity with spontaneous behavior at low temporal resolution.

b) In order to establish how DNs are recruited depending on sensory context, it would seem more important to provide a large variety of sensory contexts rather than recording from many neurons at the same time. It would be perfectly fine to establish sensory context for one DN at a time.

c) If one main goal was to establish whether DNs provide raw sensory information or processed, abstract commands, it would seem more important to have precise control over sensory stimuli and perhaps a higher temporal resolution on the DN activity readout rather than recording from multiple DNs in spontaneously behaving flies at relatively low temporal resolution.

The approach used by the authors is very valuable and it provides insights that single neuron recordings or optogenetic activation will never be able to deliver, but the reasons stated in the introduction do not really highlight the strengths of the present study.

4) – Line 82ff: The experiments presented do not rule out a strong context-dependence of DN activity in general. They merely show that many of the DNs found to 'encode' aspects of walking and grooming do so independently of whether the behavior was spontaneous or facilitated by olfactory stimulation. However, it is absolutely conceivable that different subsets of DNs control turning when it is induced by visual vs. mechanosensory vs. unilateral olfactory cues, for example. As far as I can see, this possibility has not been explored or tested in any of the experiments presented.

5) – l. 89: 'global view' seems overstated given that the authors recorded from <100 out of about 1000 DNs (in one species). It is certainly a wider view than we had before!

6) – In l. 167, the authors suggest that DNs encode high-level behaviors and in l. 136f they speculate that DNs likely drive these behaviors. This would seem like a reasonable assumption for descending neurons. However, when the authors follow up on one of the DNs they identified individually using EM tracing and a sparse driver lines, they actually show that this particular DN (DNx01) neither encodes high-level behaviors, nor does it seem to drive the behavior its activity is most strongly correlated with (head grooming). Instead, DNx01 seems to convey simple, mechanosensory inputs from the antennae to the VNC (figure 5g). How do the authors reconcile this observation with the general underlying assumption that the large majority of DNs they recorded drive behavior rather than encode sensory feedback?

7) – It seems that it was possible to identify the DNx01s due to their strong sensory responses and large axons that were easily distinguishable in EM stacks and functional imaging. It would be nice if the authors could discuss a little further whether and how it will be feasible to expand this approach to other DNs in the future.

8) In l. 254, the authors suggest that turning might be driven by asymmetries in VNC networks rather than by asymmetric activation of VNC networks via DNs. This model is hard to reconcile with existing knowledge about motor control. It is possible for VNC networks to independently generate asymmetric activity of course (for example in response to unilateral local sensory inputs). However, if DNs are not asymmetrically activated to drive turning, how would the brain be able to drive voluntary turns? What is the underlying model?

9) The authors use NeuroMechFly, a biomechanical simulation of the Drosophila body, to play back movements recorded by their motion capturing pipeline and detect collisions between the front legs and the right and left antennae. What is the reason for using such an indirect approach to detect potential antennal deflections? It seems the authors should be able to detect antennal deflections unambiguously in their video recordings. From looking at the supplemental videos, the leg movements of the model and the fly do not always seem to match perfectly (as would be expected from an approximation). Did the authors verify that their predictions were accurate?

10) The definition of 'posterior movement' (l.127) is vague. Does this include every instance of abdominal bending? Were hind leg movements and abdominal bending treated the same way in the analysis? Why would that be a reasonable simplification? It would be nice if the authors could expand on this a little bit.

11) The Discussion of the implications should be expanded, in particular, to include parallels to the ascending neurons, whose activity also seems to correlate with higher order/larger scale representations. An explicit comparison to electrophysiological recordings of DNs should be included. An advantage of calcium imaging over electrophysiological recordings is the population aspect – signal can be compared among neurons to determine patterns and co-activation. How was this employed here? Why express GCaMP in most DNs at once, rather than in specific DN split GAL4 lines? Whether fluorescence changes correlated with behaviors could have been explored in both cases.
