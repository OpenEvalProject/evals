# Peer review - Round 1

Editors:
- James M Berger, Johns Hopkins University School of Medicine , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.21884.020](https://doi.org/10.7554/eLife.21884.020)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Single-Molecule Complexes Unveil Utmost Nuclease Accuracy in DNA Replication and Repair" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jessica Tyler as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The present paper uses single-molecule FRET methods, complemented by other ensemble-averaging biophysical approaches, to understand how the flap endonuclease FEN1 interacts with its substrate. In particular, the authors focus on the classical question of induced fit or conformational selection as the two main models that describe recognition of a substrate and productive interaction with it. A series of elegant single-molecule experiments are described that provide great detail of the kinetic steps underlying flap cleavage with a number of different cognate and noncognate substrates. The main conclusion is that both protein and DNA undergo conformational changes upon binding to ensure great selectivity and specificity in enzymatic activity. The work is comprehensive and detailed, and other complementary tools such as MD simulations, ensemble time resolved FRET, biochemical cleavage assays and surface plasmon resonance are employed to support their findings and interpretations. The results are intriguing and the findings are very relevant to the field, specifically for the area of DNA replication/ repair and for the broader area of enzymology. However, a number of important arguments and conclusions in the manuscript are not backed up by the data shown. Discrimination between the different models and scenarios requires high accuracy in the quantitative determination of FRET levels, transition rates etc. While the numbers in the manuscript seem to make sense, the underlying raw data, distributions, and analyses to arrive at these numbers are either not shown or not adequately explained. Before a decision can be made regarding publication, a revised manuscript should submitted that addresses the following comments:

Essential revisions:

– A major disagreement exists between the present manuscript and one of the authors' previous reports (Sobhy et al., Cell Reports 2013). Here, human FEN1 binds with about 5 nM Kd to various DNA substrates whereas in the previous work, the Kd was about 50 times higher. In addition, k-bending/binding is diffusion limited here, whereas in the previous work it is orders of magnitude lower. This discrepancy needs to be resolved.

– Along these lines, the authors claim in the previous work that, "we find a multistep mechanism that verifies all substrate features before inducing the intermediary-DNA bending step that is believed to unify 5' nuclease mechanisms. This is achieved by coordinating threading of the 5' flap of a nick junction into the conserved capped-helical gateway, overseeing the active site, and bending by binding at the base of the junction." These statements, if they are true, certainly steal some thunder from the current manuscript; however, in the absence of discussion of the previous results here, it is unclear whether or not the authors chose to disregard their previously published study because it was incorrectly performed. This issue needs resolution. In addition, the authors should cite a related single molecule FRET study of FEN1 by the Penedo lab published in Nucleic Acids Research 2014.

– Many of the critical arguments in the manuscript are based on the authors' ability to very precisely construct the distributions of times elapsed between bending and cutting. From the description in the manuscript it is not clear how this experimentally is exactly done. The authors need to clarify how they determine the exact moment of bending, and whether they exclude certain molecules based on the properties in their FRET traces.

– It is stated that the fraction of binding/bending events that result in cleavage is 100%. Please provide supporting data/statistics are provided to bolster this claim.

– In Figure 2 and 5, the authors analyze the delay time between FRET decrease (bending) and disappearance of donor signal (flap cutting). How do they know the disappearance of donor signal is not caused by donor bleaching? The authors should provide experimental evidence to exclude this scenario.

– For non-optimal substrates, cleavage and product release is still observed, but only after many rounds of nonproductive binding/bending events. The authors treat the final binding event differently from the earlier binding events but why? A strong possibility is that each binding event can lead to cleavage but with a lower rate than in the case of optimal substrates. How is this possibility excluded? If it can be shown that the dwell time distribution of the final binding event is quantitatively different from the dwell time distributions of the earlier binding events, perhaps the current interpretation can be favored. Otherwise, the interpretation and with the last paragraph in subsection “FEN1 avoids off-target DNA cleavage in the DNA lockdown step” is suspect.

– In Figure 2, the authors show a rise-and-decay distribution of the times elapsed between bending and cutting. It is argued that this distribution is caused by the presence of multiple rate-limiting steps, including a disorder-order transition and cleavage chemistry. An important property of rise-and-decay distributions is that they only arise if the underlying steps are roughly equally rate limiting. In a subsequent, elegant experiment, the authors slow down the disorder-order transitions by a factor of 3-4 (Figure 2D). This result provides a strong prediction; namely, that the rise-and-decay distribution should now collapse into a distribution that is entirely determined by the disorder-order transition as the rate-limiting step. However, when looking at Figure 2—figure supplement 1B and C, a rise-and-decay distribution is seen with an even larger number of rate-limiting steps. This disconnect needs to be resolved.

– The argument for mutual induced fit is very speculative. Protein conformational changes are not measured directly and any conformational change inferred does not seem well supported by the data. It is strongly recommend that these claims be removed.

– The conclusions drawn based on the data in Figure 3 rely on the authors' ability to reliably distinguish fairly similar FRET levels. It is described how the confocal FRET data was analyzed to do so, but the data aren't actually shown. Given the high level of confidence needed to believe the accuracy of the FRET values, it is critical that the authors to show these data, the observed variation within the sets of three experimental replicates, and the fitting of the data.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Single-molecule FRET unveils induced-fit mechanism for substrate selectivity in flap endonuclease 1" for further consideration at eLife. Your revised article has been favorably evaluated by Jessica Tyler (Senior editor), a Reviewing editor, and two reviewers.

The manuscript has been improved but some of the comments seem to have been misunderstood and as a result, their revision in response did not adequately answered the questions. These few remaining issues (outlined below) need to be addressed before acceptance:

1) "For non-optimal substrates, cleavage and product release is still observed but after many rounds of nonproductive binding/bending events. The authors treat the final binding event differently from the earlier binding events but why? A strong possibility is that each binding event can lead to cleavage but with a lower rate than in the case of optical substrates. How do they exclude this possibility? If they can show that the dwell time distribution of the final binding event is quantitatively different from the dwell time distributions of the earlier binding events, perhaps their current interpretation can be favored."

In response to this comment, the authors compared the lifetimes of the bound state in the presence of calcium with the lifetime of the final bound state before cleavage. However, such a comparison does not address the issue at hand, because one cannot rule out the possibility that having calcium instead of magnesium may change the kinetics on non-optimal substrates. Because the non-optimal substrates show multiple binding events (1, 2,.…, n-1) before the nth binding event results in cleavage, they should build the histogram of dwell times of prior binding events and compare it to the dwell time histogram of the final event. Only if the two are substantially different, would this conclusion be supported.

2) "– In Figure 2, the authors show a rise-and-decay distribution of the times elapsed between bending and cutting. It is argued that this distribution is caused by the presence of multiple rate-limiting steps, including a disorder-order transition and cleavage chemistry. An important property of rise-and-decay distributions is that they only arise if the underlying steps are roughly equally rate limiting. In a subsequent, elegant experiment, the authors slow down the disorder-order transitions by a factor of 3-4 (Figure 2D). This result provides a strong prediction; namely, that the rise-and-decay distribution should now collapse into a distribution that is entirely determined by the disorder-order transition as the rate-limiting step. However, when looking at Figure 2—figure supplement 1B and C, a rise-and-decay distribution is seen with an even larger number of rate-limiting steps. This disconnect needs to be resolved."

Again, the authors seem to have misunderstood the comment. At least one of the statements in the original manuscript is wrong, but which one has not been identified.

3) "– The data analysis seems to assume that productive release occurs instantaneously because the dwell time between initial bending and fluorescence disappearance is interpreted as a reaction time. Please provide justification for this supposition."

This is essentially a non-answer because the disappearance of ssDNA flap is defined as cleavage ("the ssDNA flap has no interaction with FEN1, whose disappearance is defined as cleavage in our assay"). Of course, with such a definition, product release is simultaneous with cleavage. However, cleavage should really relate to the chemical reaction of backbone scission; there is no a priori reason to believe that the cleavage product should be released instantaneously. This issue still needs to be addressed.

4) Regarding the observation that upon addition of viscogen, the dwell-time distribution remains a rise and decay (which implies that multiple rate-limiting steps continue to exist), it is stated that the presence of visogen itself would introduce a more complicated free-energy landscape that would result in additional rate-limiting steps. While this is possible in principle, it is not clear that the width of the dwell-time distribution necessarily is caused by diffusion. This statement should be clarified or omitted.
