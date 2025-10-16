# Peer review - Round 1

Editors:
- Mani Ramaswami, https://ror.org/02tyrky19 Trinity College Dublin Ireland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80923.sa0](https://doi.org/10.7554/eLife.80923.sa0)

Memory recall is more precise when discrimination is required. This work in Drosophila shows that two related odors trigger near identical Kenyon cell responses when tested in isolation, but trigger different responses to the second odor if these are experienced in sequence within a small temporal window. The authors argue that this template comparison requires some activity downstream of Kenyon cells, that is recruited by MBONs. Overall, the experiments, building on a clever method to build "miminal memories" via optogenetically restricting the formation of memory traces in selective output compartments of the Kenyon cell (KC) axon terminals, provide very nice physiological evidence for a neural mechanism that underlies a contextual basis for the precision of memory recall.


---

# Peer review - Round 1

Editors:
- Mani Ramaswami, https://ror.org/02tyrky19 Trinity College Dublin Ireland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80923.sa1](https://doi.org/10.7554/eLife.80923.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "One engram two readouts: stimulus dynamics switch a learned behavior in Drosophila" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Mani Ramaswami as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by K VijayRaghavan as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) There appear to be a variety of ambiguities not acknowledged in the text as well as prior work not considered in necessary depth. These are indicated or reflected in various reviewer comments. Please address all of them and provide point-by-point responses indicating how these concerns have been addressed in the revised manuscript.

2) One concern, is the claim and focus around "one engram and two responses" is both incompletely justified (e.g. see reviewer 2 comment that the boutons represent the engram and not the cells) and not intellectually useful in terms of communicating the findings to a broader audience. Figure 4, which contains the most impressive and impactful observations in the paper indicates that after the specific optogenetic learning protocol is deployed, two odors are perceived similarly (or as a common category or class of odors) in one condition but cab discriminated as two different odorants in another condition. First, at least one reviewer feels that the excitement of this figure is in the clear demonstration of. neural correlates of this contextual discrimination phenomenon – a point that is inadequately made here and somehow occluded by a pitch around "one-engram two outcomes". Second, a more solid basis for a general discussion here may be around the concept of categories. There appears to be a contextual ability to go beyond clubbing two odorants into a common category vs splitting them into distinct objects. We appreciate that the authors can decide on how they wish to discuss their data, but do ask that these suggestions/ concerns be considered as final revisions are made.

3. Please provide genetic controls requested in Reviewer 2 point d.

4. Consider if it would be useful to respond materially to the other comments.

Reviewer #1 (Recommendations for the authors):

1. Title of first section "Learning can support…". Implies learning is required for and/or contributes to discrimination, which would not be correct. What this really shows is that discrimination is not hindered by what appears to be "generalized" learning. A more appropriate title is needed.

2. Same page – "flies learn both generalization and discrimination tasks," What is the evidence that discrimination is learned? Perhaps it is always possible as supported by the Results section 2, showing that KC inputs in "naïve" flies have enough information for discrimination. (Though not shown, presumably this is true with MBONs too in naïve flies). It seems that the ability is not exercised unless needed. Notably (Results section 3) – learning is not associated with any increase in physiological correlates of discrimination.

3. The differences between discrimination after DAN stimulation in the two compartments could be Kenyon cells activated by one of the odorants may make more or less synapses in compartments innervated by one MBON compared to the others.

4. Figure 4 – the key: a very nice observation around which the paper's significance should really be explained/ focussed.

5. Difference between MBON a-3 and MBON g2A'1 could be due to the multiple lobes and compartments involved. The alternative, that this is an MBON dedicated to such discrimination may be true but isn't convincingly shown. In any event, a discussion of alternative possibilities is required,

6. Is the term "uncorrelated" sometimes more appropriate to use than "decorrelated?"

Reviewer #2 (Recommendations for the authors):

a. I am confused by the use of 'one engram' and 'single set of synapses' – 'single set' is entirely arbitrary, and what is one engram in this context? Single odor engram triggering different behavior is not novel. Several prior works have shown that a single odorant can trigger different actions in learned flies depending on either stimulus history or the fly's internal state.

b. Authors have imaged calcium dynamics in the KC cell bodies to compare if two engrams should be perceptually similar. However, Bilz et al. 2019 have shown that the KC boutons, not the cell bodies, are the units of olfactory memory engrams. I understand that imaging KC boutons will be challenging to combine with optogenetic stimulations, but this nonetheless creates a significant caveat in their approach and needs to be discussed in the manuscript.

c. Given that odorant similarity is concentration-dependent (e.g., Hallem and Carlson 2006), I am unsure how the authors chose the odor concentrations. Behavior experiments in Campbell et al. 2013 were performed in a vastly different apparatus; authors need to check if flies indeed find it difficult to discriminate between BA and PA in the current setup under standard aversive learning protocol. It would also be reassuring to see additional odor pairs to ensure the generality of their results.

d. Authors have not included any genetic control (e.g., empty split) and stimulation control (-retinal) in the behavioral experiments (Figures 1 and 6) to show the baseline response. Discrimination data in Figure 1g looks bimodal, and I wonder if discr. vs. gen. will become significant with a larger sample size. What is the rationale for the chosen sample size for these experiments? DA rescue data in Figure 1i is also incomplete as it does not contain any easy discrimination, and generalization data for γ2α'1 and α3 rescue data is entirely missing. Figure 6 includes only γ2α'1 data but no α3 activation data; α3 is an essential control for testing their predictions.

e. In Figure 4 and supplementary Figures 3 and 4, dissimilar odorants are presented as isolated pulses, not as a transition. A fairer comparison would present them as a transition to match the behavioral experience. Why were optogenetics not used for the α3 imaging experiments in Figure 3?

f. Does the starting KC weight matrix in Figure 5 match the EM connectivity data? How does the transition data from this figure look in the PC space, and how well does the decoder from Figure 2 performs on the transition data? Similarly, how well the regression model performs if it's trained purely on single pulse data?

g. Multiple papers have shown how odor transitions affect learned behavior in flies, e.g., DasGupta et al. 2014, Groschner et al. 2018, Vrontou et al. 2021. Yet, the authors have not discussed how their results support/contradict these prior models. It's an integral part of the manuscript and could point towards significant differences in experimental approach and/or intensity vs. identity coding. For example, Groschner et al. 2018 and Vrontou et al. 2021 had shown that the main difference among the KC responses during intensity discrimination is in the spike latency, not in the KC identity-I wonder if the apparent lack of discriminability in Figure 5 comes from the slow GCamp responses in the KC cell bodies.

Reviewer #3 (Recommendations for the authors):

The story is novel and convincing, but a little patchy in parts.

I am not convinced that Figure 4d-f should be done with shock and not DAN stimulation. The authors should attempt the equivalent optogenetic experiment for γ and α DANs.

Other less important, but noticeable points of asymmetry exist throughout the manuscript. Experiments were done with α but not γ DANs, including Figure 3 and others.

A loss of function experiment with DAN inhibition in natural learning would be appropriate and very helpful.

The dopamine biosynthesis KO experiment of Figure 1i should really be done for both populations of DANs, and ideally for easy discrimination as well as hard discrimination.

More discussion of potential mechanisms would also help.
