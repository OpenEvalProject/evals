# Peer review - Round 1

Editors:
- José D Faraldo-Gómez, National Heart, Lung and Blood Institute, National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55132.sa1](https://doi.org/10.7554/eLife.55132.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Conformational distributions of isolated myosin motor domains encode their mechanochemical properties" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by José Faraldo-Gómez as the Senior/Reviewing Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Senior Editor has drafted this decision to help you prepare a revised submission.

Summary:

This work provides important insights into a question of broad significance in molecular biophysics, namely how the functional mechanisms of proteins emerge from their structural dynamics. The authors carry out extensive molecular dynamics simulations of several myosin motor domains to probe the conformational distribution of the nucleotide binding site. The results are used to construct the free energy landscape and kinetics for the transition between different metastable states in the general framework of Markov State models (MSM). The underlying hypothesis is that the intrinsic free energy landscape of the binding site (or the P-loop, in particular) in the absence of nucleotide contributes to explain the nucleotide binding properties of the motor domain. In this perspective, key properties of the motor domain that are correlated with functional features, such as duty ratio, are encoded in sequence. The hypothesis is supported by the observed correlation between experimentally measured (in previous literature) duty ratios and ADP release rates with the computed free energy difference between the two key basins, which correlate with the nucleotide compatible and nucleotide-free structural states. Overall, the study is a good demonstration of how extensive, state-of-the-art MD simulations can be used to capture somewhat subtle yet mechanistically relevant features in complex molecular systems. It is easy to envisage how a similar methodology could be used to probe other biological problems that involve shift of populations among different structural states. The work is also a good illustration of how to leverage information from homology modeling, i.e. through a systematic analysis of general mechanistic features in a family or collection of models, as opposed to detailed aspects specific of given protein, likely to be beyond the accuracy of such models.

Essential revisions:

1) The analysis provided points towards a specific peptide bond whose dynamics causes the backbone carbonyl oxygen of S180 to point either towards the nucleotide binding site or away from it. It would be of great interest to provide an experimentally testable hypothesis by predicting a mutation that specifically determines the conformational preference of this peptide bond, thereby shifting the activity either up or down for a particular myosin.

2) In Figure 4B, the authors claim the error bars are too small to be seen. This is surprising given that the underlying data for each point is a few microseconds of MD simulation. The authors should carefully explain and justify their error analysis. If the MD data is fragmented into, say, 10 parts, do the MSM deduced from each fragment yield indistinguishable free-energy difference values? Showing some trajectories in which the system switches between basins might help make this point also.

3) In the whole-motor Markov models, a lag time of only ~1 ns (Table 2) does not seem immediately intuitive. This choice requires some kind of rationale and, ideally, data to support it.

4) The authors indicate that phylogeny relationships were used to infer duty ratios. This approach needs justification and validation, if indeed it was actually used in the data shown – in which case inferred values should be noted (not the same as a measurement).

5) In their analysis, the authors identify an interesting mutation distant from the active site that nevertheless affects the ADP off rate, for which the transition rate P(A->B) is taken as proxy. Do the simulations provide insight into how this distant mutation alters the barrier for the A->B transition?

6) Given that the identified thermodynamic (duty ratio) and kinetic (ADP off rate) functional readouts point towards the same A-B transition, do the data allow to speculate whether the two are inherently linked to each other or whether they might have evolved independently?
