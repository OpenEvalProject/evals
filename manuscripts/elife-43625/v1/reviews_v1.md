# Peer review - Round 1

Editors:
- Nicole Rust, University of Pennsylvania United States

Reviewers:
- Jim DiCarlo, Massachusetts Institute of Technology United States

## Review text

DOI: [10.7554/eLife.43625.024](https://doi.org/10.7554/eLife.43625.024)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Representational untangling by the firing rate nonlinearity in V1 simple cells" for consideration by eLife. Your article has been reviewed by two peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Joshua Gold as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Jim DiCarlo (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this study, the authors examine the role of threshold nonlinearities (a model of the mechanisms that intervene between membrane potential and firing rate) in neurons in cortical area V1. They use a combination of simulations and a bit of experimental data to argue that those thresholds appear to be set to maximize the (population) linear decodability of stimulus orientation in the face of nuisance parameters (phase, contrast, and spatial frequency). This hypothesis is referred to as representational untangling (RU). While untangling is an essential component of the visual form processing pathway, the mechanisms that support it are incompletely described, and in that context, this paper addresses an important and interesting set of issues. The reviewers have identified a number of issues that need to be addressed but they believe that they can be addressed via further analyses and some re-writing.

Essential revisions:

1) What is/are the main alternative hypotheses (to RU) and which figures/results reject those alternatives?

The main setup of this study is that the "designer" of V1 has followed a particular optimization goal (= a particular RU variant). (I mean "designer" here in the general sense of evolution, development, etc.) I kept wishing that the authors would more directly pose and test at least one serious alternative optimization goal. The main one they seem to entertain is preservation of total information:

"These results suggest that information re-formatting, rather than maximisation, may already be a relevant computational goal for the early visual system."

But that alternative is dismissed as almost trivial (and some versions are), which leaves one wondering why a study is even needed. As the authors point out, thresholds can only remove information. The more interesting alternative optimizations have to do with preserving information in the face of energy costs or other forms of compression (e.g. sparseness).

Here is a first attempt at stating an alternative:

"However, despite the obvious loss of total information caused by the rectifying aspect of the FRNL, which is due to all membrane potential values below the firing threshold being mapped to zero firing rate…" But this is not at all obvious at the population level.

And then "While this drastic removal of a large fraction of responses can clearly lead to severe total information loss (Barak et al., 2013)," The key word here is "can." But does it?

For example, the total information from the population of retinal ganglion cells might be spread out across an overcomplete set of V1 neurons, such that, even with thresholds, the V1 population maintains the total information (i.e. no loss). Of course, even if that were true (which I don't believe), then one would still have to suggest what the reason for doing that overcomplete spread out might be (e.g. preservation of information about natural images (not total information), energy costs, etc.).

To be more concrete and constructive: The most interesting testable experimental question here is how the thresholds are set (i.e. under what possible optimization goal.) The main setup seems to go like this: the population of V1 encoders is fixed, the noise in the membrane potentials of those encoders is irreducible, and the parameter under (optimization) control of this system is the threshold. Under these assumptions, the question posed is, what optimization goal is the system using to set the uth parameter for each neuron? The authors claim that it is the particular RU goal they setup (Figure 7). It would be stronger if they could show that it is not (or less) consistent with some other optimization goal. In both cases, the simulations would assume the same fixed number of neuron and irreducible noise. This would make the paper much stronger. Alternatively, perhaps the authors could consider a range of RU optimization hypotheses (e.g. separability of orientation, separability of contrast, etc.)? Or, similarly, optimization for RU under limited training examples for the decoders? (see point 3 below).

Similarly, the authors focused solely on RU of the orientation of sinusoidal gratings from the responses of model simple cells. Optimality of the firing rate threshold is defined in the context of untangling information about the orientation of sinusoidal gratings, absent any reference to why posing the problem this way makes sense, given that these neurons presumably evolved to process natural images.

2) Try to strengthen the presented evidence for RU from the image input to this level of V1 (spiking outputs of V1 simple cells).

Previous experimental results advocating for RU along the ventral stream have made comparisons at two points of processing (e.g. V4 population spike rates and IT population spike rates). It would strengthen the claims if the authors would do something similar across the key stage of processing they are focused on here. E.g. compare with pixels, center-surround (e.g. difference of gaussians (DOG) to approx. RGC and LGN responses).

We understand that some decodes were attempted on the simulated intracellular potential population and compared with the spiking outputs. That is good, but this seems a bit like comparing apples and oranges.

3) Better define the RU hypothesis (or alternative variants of it). In particular, the operational definition of linear separability is not agreed upon in the field, and different definitions tend to test different things. We suggest would be to explore these different operational variants (below) and decide if the results are robust to that, or if they point in an even more interesting direction.

Most notably: It appears that the linear decoder test that was applied was only a test of generalization to new noise samples (subsection “Linear decoder”), rather than generalization to unseen values of the stimulus parameters. Is this correct? But then the manuscript reads: "RU was quantified by the performance of a linear decoder which decoded stimulus orientation from membrane potentials or firing rates in the face of noise and variability in other (nuisance) parameters of the stimulus: phase, contrast, and spatial frequency (Figure 1, blue)." This might imply tests of generalization to new stimulus values, but it is unclear. (Side point, the paper must be significantly clarified around this issue, regardless of what was done.)

Assuming that the training data completely cover all the test data (i.e. generalization only to new noise samples), then it is surprising to see that this linear decodability test would not be partially successful with decoders on the pixel (+noise) input representation. (Note that the two dimensional examples such as Figure 2 provide useful intuition, but tend to hide the possibilities of successful linear separability that is possible in high dimensional population spaces.) But the intuition might be wrong here because the chosen nuisance variables might strongly push against this possibility. Clarification around this issue would strengthen the paper. That is, one RU possibility is that NO separating hyperplane exists in the population state space. Another RU possibility is that multiple separating hyperplanes exists, but that they require a very large number of training examples to discover – thus, in practice, they appear not to exist. The difference in these two variants of RU depends on the amount of training data and the amount of required generalization.

To summarize: the improved linear decodabilty of the V1 population relative to a pixel or DOG representation should be shown directly and the dependence on training sample size should be explored in some way. The key result might be: for limited number of training examples, the properly thresholded V1 decoding performance is higher than the pixel and DOG representations, but that result is not true in the limit of infinite training data. To be clear, either of the possibilities above are interesting and publishable, but they are impossible to disentangle right now.

Related: an intuitive solution to increase linearly separability is to set RELU thresholds very high such that the representation of each image is ultra-sparse. In the limit, each image would be coded as one-hot population response vector. Under some operational definitions of linear separability, this solution is perfectly fine (e.g. test only at the training images). However, it is not a real world solution because it has little to no generalization power and it requires a very large number of neurons to maintain information and corresponding large numbers of training examples. Thus, the trick for real world tests of linear separability in the setting explored in this paper is to set the thresholds high enough to enable linear separability in the context of limited training data and test generalization to new nuisance values of the stimulus parameters – what that limit should be and how "far" the "new" stimuli should be are admittedly unclear, but both could be considered and explored to firm up the arguments. Perhaps this has already been done and it was missed it in the presentation.
