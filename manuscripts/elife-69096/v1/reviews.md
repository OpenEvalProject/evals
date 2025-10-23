# Peer review - Round 1

Editors:
- Nir Ben-Tal, Tel Aviv University Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69096.sa0](https://doi.org/10.7554/eLife.69096.sa0)

FoF1-ATP synthase is a membrane enzyme that uses the proton motive force to synthesize ATP via rotation-coupled mechanism. The symmetry of this high-order homo-oligomeric enzyme suggests cooperativity among the protomers. Here, biochemical and molecular biology studies, and simulations demonstrate that energy transduction is indeed inherently cooperative in FoF1-ATP synthase.


---

# Peer review - Round 1

Editors:
- Nir Ben-Tal, Tel Aviv University Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69096.sa1](https://doi.org/10.7554/eLife.69096.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Cooperation among c-subunits of FoF1-ATP synthase in rotation-coupled proton translocation" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Nir Ben-Tal as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Richard Aldrich as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Hiroyuki Noji (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. A main concerns is the accuracy of biochemical assays, ATP synthesis activity measurement and ATP-driven proton pumping activity measurement. To our knowledge, it is not easy to achieve highly accurate and precise biochemical assays such as error within a few % even if we use highly purified enzymes. In this paper, the authors reported very small experimental error: around 1 % or even less. However, we have not found description of the how the experimental errors were determined. The authors did not use purified enzymes but inverted vesicles of E. coli expressing the mutated enzymes. One of critical parameters for the accuracy is the quantification of the enzymes in the vesicles that were estimated from the decoupled ATP hydrolysis activity measurement. The error in this quantification should be substantially smaller than 1 % to achieve such a high accuracy. In addition, the ATP synthesis activity and ATP-driven proton pumping activity were measured from the time courses of the assays that should also include some experimental errors as found in the noise and drift in the time courses of proton pumping measurement (Figure 2c). Because the activity difference among the double mutants were subtle, the accuracy and precision of the biochemistry part are the critical points to prove the validity of their arguments. Detailed explanations on the estimation of experimental error as well as reproducibility are required.

2. Another concern is the validity of the simulation. The authors conduced Monte Carlo simulation for proton transfer step between c-subunit and a-subunit. The rate constant was represented in a simple exponential factor: exp(-A(r-r0)), where 'A' represents the decay rate, 'r' is physical distance between c-subunit and a-subunit and 'r0' is the offset value that represents the sum of sidechain length of the proton transferring residues on c-subunit and a-subunit. They assumed smaller 'r0' and larger 'A' for cE59D mutant. Although the smaller 'r0' would be reasonable considering the shorter side change of aspartic acid, the reason for higher 'A' for the mutant is not clear. In addition, different values for pKa were given to the glutamic acid in the wild type c subunit (cE59) and to the aspartic acid in the mutant (cE59D), without rationalization. These parameters should be critical for the simulation results. The validity of the different 'A' and pKa in the mutant should be explained.

3. Another concern is that cooperativity is shown here in case of mutants, but it is not so obvious how it relates to the WT enzyme. One clue, to which authors only briefly relate, is that according to their earlier simulations in WT the preferred pathway is when 2 or 3 Glu are unprotonated at any time rather than just one Glu being protonated/unprotonated. This kind of "cooperativity" in WT enzyme and its relation to the data presented should be discussed in greater detail.

Also, parts of the text, such as the Introduction, are not very clearly written and can be improved.

Reviewer #1 (Recommendations for the authors):

1. Show computations (Figure 3b) and experimental data (Figure 2d?) side by side to make it easy to evaluate the correspondence.

2. Simulation procedure should be explained in greater detail. Not just as a pointer to the previous publication.

3. "Although the pKa value specific to the corresponding site is unknown, we empirically chose pKa = 8.0 for cE59 and 7.0 for cE59D considering the intrinsic difference in pKa values.": These values are much higher than the pKa of these amino acids in solution (around 4). Maybe justify the values based on calculation of the pKa shifts? PROPKA or something.

Reviewer #3 (Recommendations for the authors):

l. 72 – there are now true atomic structures of F-ATPase, which should be quoted here (e.g. yeast, bovine, ovine).

Figure 1 – which structure was used for depiction? Quote PDB and species.

There is no comment at all why Glu to Asp mutation was used. Previous study from this group (ref 8) indicated that replacement of a single E with Q in c10 ring completely abolishes the activity, as discussed at the end of this manuscript. This should be mentioned at least briefly at a point in text when E to D mutations are introduced.

l. 170-175 – for mutants eh-ej there is no evidence for fluorescence quenching after ATP addition in Figure 2c, so there is no evidence for proton pumping activity. It is not clear at all why authors used quenching after FCCP addition as an apparent measure of pumping. In mutants ef-ej this signal is reversed compared to c10 and e. By the same token one could argue that eg-ej are more active than ef, as they show larger quenching after FCCP addition. It seems fair to say only that e to eg show decreased pumping as they show slow quenching after ATP addition, while eh-ej do not show any pumping.

Similarly, it is not clear if in Figure 2b eh-ej show genuine ATP synthesis or this is more of unspecific reaction. Authors could show here a control with their previous E56Q mutant which does not show such activity.

Figure 2 A – very poor blot, not clear at all that we are looking at a specific signal.

C – for c10 the steady level of fluorescence is not achieved, so it is incorrect to use it for comparison with other mutants.

Table 1 – would be good to include data for WT for comparison.

l. 249 – comment should be added on the increased values for g, h, i in Figure 4e, which are presumably linked to e behavior.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Cooperation among c-subunits of FoF1-ATP synthase in rotation-coupled proton translocation" for further consideration by eLife. Your revised article has been reviewed by 2 peer reviewers and the evaluation has been overseen by Richard Aldrich as the Senior Editor, and a Reviewing Editor.

The manuscript has been improved but one remaining issue still needs to be addressed.

The core data of this manuscript is the ATP synthesis activities of the mutants with double cE56E mutations: ef, eg, eh, ei, and ej in Figure 2b, on which all of arguments and the simulations are based. The main concern was the precision and accuracy of this measurement. This is because the ATP synthesis activity of the double mutants are remarkably smaller than that of the reference sample, c10. In addition, the difference in the activity among the mutants are also quite small, in the range from 1-4 % when standardized with the activity of the reference sample. Therefore, the biochemical measurement should achieve extremely high precision and accuracy to quantify the differences in the activity among the double mutants.

In the original manuscript, the error bars were represented with standard deviations (s. d.) that ranged 3-10 % as coefficient of variance (c. v.), that were extraordinarily small as a biochemical assay. Furthermore, the ATP synthesis activity measurement has multiple steps for calibrations and data corrections: baseline correction, calibrations for ATP quantification, and quantifications of ATP synthase protein in the inversed vesicles. Each step should have some experimental errors. Therefore, this reviewer asked the authors to provide experimental data to verify such small error bars.

Along this request, the authors re-calculated standard deviations in the revised version, considering the experimental errors in quantifications of synthesized ATP molecules and the enzyme molecules in the inversed vesicles. Resultant errors are 17-30 % as c. v. for each mutant. Although lot-to-lot variance of inverted vesicles and errors in baseline correction are still not considered, the error estimation seems to be relatively valid.

Then, the arising question is "Are the differences among the double mutants statistically significant?". The revised manuscript does not mention this point at all, even though this is the most critical point and the basis of the main concern. The authors provide the p-values between double mutants that range from 10-68%, in the 'source data' file. At least, the authors should clearly mention the statistical uncertainties of the ATP synthesis activities of the mutants, providing the standard deviations (not standard errors) and p-values in the main text. Otherwise, readers are not able to judge the significance of differences in ATP synthesis activity among the mutants.

Arguments based on such subtle differences with large p-values might be misleading. The authors are asked to reconsider the statistical validity and to re-build the arguments as well as the title and abstract to avoid possible overstatements.

Lastly, we want to mention a point about data correction on ATP synthesis activity measurement from another angle: The fraction of coupled enzyme that can be estimated from DCCD sensitivity (Table. 1). When we consider the DCCD sensitivity in the quantification of 'coupled ATP synthase enzyme in the inverted vesicles', the resultant ATP synthesis activity of the mutants may differ from the present one, possibly showing a different trend. Did the authors correct the quantification of ATP synthase enzyme in the reversed vesicles with the DCCD sensitivity?
