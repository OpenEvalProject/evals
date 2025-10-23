# Peer review - Round 1

Editors:
- James M Berger, Johns Hopkins University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.47405.045](https://doi.org/10.7554/eLife.47405.045)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Ctf4 organizes sister replisomes and Pol α into a replication factory" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Cynthia Wolberger as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The current work presents the 3.8 Å resolution structure of a CMG complex bound to Ctf4. The structures for Ctf4 occupied by 2 or 3 CMG complexes (at 6Å and 7 Å resolution) are also shown, along with a model Ctf4-Pol-α/primase (obtained at 12 Å resolution) that identifies one lone tethering point between Pol-α and Ctf4. Based on the ability of Ctf4 to bind multiple CMGs and a single Pol-α, a model for how Ctf4 coordinates the action of two helicases and the lagging strand polymerase in a prospective replication factory is proposed. This framework is then used to speculate as to how factories might promote sister chromosome cohesion.

The strength of this manuscript lies in the structural studies of various Ctf4 complexes. This information is important as it identifies two previously unknown Ctf4 interactions with CMG subunits Cdc45 and Psf2 and substantiates the prediction that multiple CMG assemblies can bind to Ctf4 without clashing. In addition, Ctf4 is found to preferentially bind one DNA Pol-α/primase. Overall, these insights contribute to our general understanding of the architecture of the eukaryotic replisome. This said, there are several extant issues that need to be addressed.

Essential revisions:

1) A substantial portion of the paper is dedicated to several elaborate models that are consistent with available data but never explicitly tested, such as the idea that replication factories might have a role in facilitating sister chromatid cohesion. The work would be substantially improved if mutations in the newly discovered Ctf4-CMG interface (or even a Ctf4 deletion, which is viable) could be examined for their ability to disrupt the observation made by Tanaka and colleagues showing that DNA at equal distances from an origin come together at the time of replication. Otherwise discussion topics such as the role of Pol-α-Ctf4-CMG in parental histone re-deposition appear more solidly grounded. Barring the addition of genetic or cell biological studies aimed at testing aspects of the cohesion model, it would be appropriate to focus the discussion on the Ctf4-CMG interaction (i.e., eliminating the speculation about cohesion and Figure 8—figure supplement 2B) and to limit the Discussion to the two-CMG-one Pol-α/primase model.

2) The manuscript does not take into account that amino acid changes in the CIP motif in Chl1 (a cohesin interactor) give rise to a sister chromatid cohesion phenotype, unlike a mutation in the CIP motif of Sld5. Taken at face value, the evidence indicates that Chl1 interaction with Ctf4, and not two CMGs bridged by Ctf4, is important for sister chromatid cohesion. If genetic or cell biological data are presented to test the proposed cohesion model, these findings will need to be noted.

3) The Pol-α modeling is based on less solid data than the higher-resolution CMG–Ctf4 interactions. There is some concern as to veracity of the placement the different Pol-α/primase elements with respect to Ctf4 and/or the CMG. Since the location of these regions is an important part of the replication factory model, it is important that more data be shown to boost confidence about their placement. Details of the cryo-EM volume with different views/different thresholds should be shown, as well as the model-to-map Fourier Shell Correlation plot comparing best and second-best docking solution. Was RELION multi-body refinement attempted for this complex? The resolution of the Pol-α lobe might improve using this strategy. Also, panels A and B/C of Figure 6 should be scaled so that the Pol-α NTD has the same size.

4) In the Sun, 2015, replisome paper (Figure 5E), Pol-α/primase maps to the opposite Ctf4 side compared to that described in the current study. This discrepancy should be addressed more clearly.

5) The biochemical data in Figures S13, S14, and S15 are somewhat buried, which detracts from the impact of the work. It would be preferable for these panels to be included in the main results in place of the extensive discussion of the model that is there now. Along these lines, is this the first time that the binding of the CMG to Ctf4 is seen to stimulate Pol-α binding (i.e., that their association is cooperative) and vice versa? If so, please note as much, or else cite the appropriate references that the findings confirm. Similarly, is this first time that stoichiometric studies have been performed to show that helicase activity is supported by a dual-CMG/Ctf4 complex? Do the authors think that the difference between 1.7 CMG–Ctf4-3 versus 1 CMG–Ctf4-3 in Figure S15 is a result of cooperative action of the two helicases? If so, how might this cooperativity emerge?

6) It would seem that only the double CMG–Ctf4-3 works well in the elongation assay (in S15B), which contradicts the idea that one or two CMGs bound to Ctf4 bind and unwind as well as CMG alone (S14). Please describe the tests that were performed to determine whether the time of preincubation was long enough to ensure that only unwinding is being measured in these assays rather than fork binding and unwinding. Based on recent work from the Yardimci lab, it would seem that many previous studies are likely to be measuring binding as well as unwinding (with binding being rate limiting).

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting your article "Ctf4 organizes sister replisomes and Pol α into a replication factory" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Cynthia Wolberger as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Primary issues:

1) In the prior review, it was requested that "Details of the cryo-EM volume with different views/different thresholds should be shown, as well as the model-to-map Fourier Shell Correlation plot comparing best and second-best docking solution." The reply states that "We did not provide a map-to-coordinated correction curve, because we simply used rigid body docking – the original crystal structures were unaltered." This reply is unclear. Do the authors mean "map-to-coordinate correlation curve"?

It was requested that a map-to-model correlation curve be shown for the best rigid body docking solution and the second-best rigid body docking solution. If the cryo-EM map is sufficiently featured to model one Pol α orientation with confidence, then the FSC for the best solution should show significantly higher correlation than the second-best solution. The authors could also simply quote the average correlation score for the best vs second best docking solution. Please address.

2) The evidence that the CMG helicase can use ATPγS to unwind DNA is not compelling. The data in Figure 7B appear to use extremely high concentrations of nucleotide (100 and 500 mM) concentrations – are the units actually μM? The ATPγS may be contaminated with ATP (which is commonly the case), and it may be this nucleotide rather than ATPγS that is used by the CMG.

The more relevant data to this point may be in Figure 7—figure supplement 3, where the experiment is performed at a more realistic concentration of 0.1 mM ATPγS. Here it is suggested that the same amount of unwinding is seen with ATPγS as when ATP is added. There are two issues with these data. First, in the ATPγS data, the overall signal is weak and the detected released DNA is very weak. In contrast, the experiment with ATP shows a much more robust signal. Second, there is no direct comparison with ATP versus ATPγS (as in 7B). Experiments using equivalent concentrations of ATPγS and ATP at similar (low) concentrations need to be shown to provide a direct comparison.

3) Related to (2), an important issue that is not addressed is whether there is a very small amount of a contaminating helicase in the preps that is responsible for the unwinding. Given the very slow different kinetics seen with ATPγS (it takes around 30 minutes and then makes up all of the slower rates observed earlier) and previous data from others (where the hydrolysis rate found for Mcm2-7 with ATPγS was 2% of that seen with ATP), it seems possible that the observed activity derives from a contaminant. A mutant form of the CMG carrying a critical ATPase motif substitution that is necessary for unwinding needs to be tested to demonstrate that unwinding is indeed lost.

Alternatively, the ATPγS data and claims could just be removed, as they are not central to the primary thrust of the paper.
