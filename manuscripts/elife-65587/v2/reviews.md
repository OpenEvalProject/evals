# Peer review - Round 1

Editors:
- Sebastian Deindl, Uppsala University Sweden

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65587.sa1](https://doi.org/10.7554/eLife.65587.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

The authors present an elegant combination of cryo-EM, analytical ultracentrifugation and molecular dynamics simulations to investigate the structure and dynamics of archaeal histone – DNA complexes, termed archaeasomes to distinguish them from eukaryotic nucleosomes. This rigorous biophysical study provides important new insights into archaeal genome biology and will no doubt be of interest to the archaeal research community as well as the chromatin biology field in general.

Decision letter after peer review:

Thank you for submitting your article "Archaeal chromatin 'slinkies' are inherently dynamic complexes with deflected DNA wrapping pathways" for consideration by eLife. Your article has been reviewed by two peer reviewers, including Sebastian Deindl as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Cynthia Wolberger as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Yamini Dalal (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

This is a very strong manuscript. Please consider the reviewers' recommendations and suggestions below by making the appropriate textual changes. No additional experiments are required.

Reviewer #1 (Recommendations for the authors):

It is not completely clear why the authors chose histones from Thermococcuskodakarensis for the experimental part of the work, while the previously published crystal structure and the simulations presented in this study used histones from Methanothermus fervidus. Can the authors comment more on this choice? Are the histones from one species are easier to express and purify than those from the other species? The text would benefit from a brief explanation, although this is not a concern for the validity of the study, given the high degree of sequence identity between these histones.

"consistent with a systemic error"

Do the authors mean "systematic" (as opposed to random) error?

In Table 2, is there a 95% confidence interval to report for sedimentation coefficients? If not, can the authors explain why?

"A total of 1,879,294 particles were identified and classified according to a neural network trained on manual particle selections"

This statement is a bit unclear. Is it particle picking that was performed using a neural network (crYOLO, as the Materials and methods section indicates), or is it the selection of good 2D class averages (which is also possible, using the program Cindirella from the same authors who make crYOLO)? If the former, I suggest mentioning the neural network before the classification procedure; this sentence as written now could be understood as if a neural network was used to select good 2D class averages (which is not what the Materials and methods section explains).

"Refinement of these densities yielded maps at 9.5 Å and 11.5 Å resolution for the closed and open forms, respectively (Figure 6E, F)."

There is no panel F in Figure 6. Earlier references to Figure 6 in the same paragraph also seem to be off by one panel.

"Even though Arc207 (207 base pairs of DNA bound to 7 histone dimers) were deposited on the grid, our refined density of the closed state describes only 150 base pairs of DNA and 5 histone dimers"

Is it possible that what the authors call the closed conformation is in fact the "base" of an open conformation, and that this reconstruction was obtained from truly open particles in which the "lid" was more dynamic and therefore not resolved? This would explain the missing molecular weight in this reconstruction. This possibility does not change the main conclusion that archaeasomes are dynamic, but it could change the way the 90 degrees open state is seen: it could correspond to an intermediate between the fully open and fully closed conformations, with the "lid" resolved because it is more stable than in the majority of the particles, that are fully open states in which the "lid" cannot be resolved, and the dataset may not contain many (any?) truly closed particles (which one would expect to yield a reconstruction showing all 207 base pairs of DNA and 7 copies of the histone dimer). The authors should comment on this.

"Close inspection of the "closed state" two-dimensional classes indeed shows additional out-of-plane density that is consistent with the missing two dimers and ~60 base pairs of DNA, albeit at low contrast relative to background (Figure 7C)"

There is no Figure 7. This statement likely refers to Figure 6C.

"Archaeasome compaction can be stabilized with divalent cations. In absence of archaeal ATP-dependent chromatin remodeling factors (large machines that regulate chromatin access in eukaryotes), this architecture provides an alternative mechanism for compacting chromatin and adjusting genome accessibility"

There are several examples of regulatory mechanisms for chromatin remodeling in eukaryotes that involve domains which bind to specific histone post-translational modifications as a way to target remodeling activity, making it a mostly deterministic process (presence of a PTM causes recruitment of a remodeler). It is difficult to envision that any regulation mechanism in archaea could emerge from random conformational changes in their chromatin only. Is it definitely established from whole-genome sequencing that archaea do not have chromatin remodelers? Or could they have them, but these proteins have yet to be identified? Could the compaction induced by divalent cations be the main regulatory mechanism in vivo? (in which case membrane ion channels would also indirectly act as chromatin remodelers on a genome-wide scale by regulating intracellular concentrations of these ions?). The authors should consider discussing these points to enrich the Discussion section and potentially strengthen the connection between the their biophysical results and archaeal genome biology.

Materials and methods section, cryoEM grid preparation

The glow discharge conditions should be indicated.

"a Gatan K3 camera at 29,000x magnification in non-super resolution mode"

This mode can be called "counting mode".

"dosage rate of ~1 e/Å, and 50 frames per micrograph stack"

The dose rate's unit is e/Å2/s, unless the authors are referring to the dose per frame (in which case it should be clarified). In addition, the total dose accumulated over the entire exposure time should be indicated.

When first mentioning the Widom 601 sequence, the authors should cite (Lowary and Widom, 1998).

"Gel shift assays showed that full complex saturation occurs when DNA and histones are mixed at the previously reported stoichiometric limit"

This statement should cite an adequate reference.

Reviewer #2 (Recommendations for the authors):

It would be nice if they could include the rationale to study dimer-dimer and dimer-DNA interactions by MD using 90 bp, 120 bp and 180 bp.

A MNase ladder is mentioned, but no citation or figure is referenced, please add the MNase ladder.

The authors very nicely show that Mg2+ does not impact archaeasome oligomerization, how does salt concentration impact oligomerization?

The authors mention that particles that interacted with neighboring particles were not used in the analysis. We are curious whether these particles would more closely resemble what would happen in cells where this is higher density (one presumes) of chromatin?

What was the distribution of the angle of the open conformation found for the archaeasome?

It would be interesting and timely if the authors could discuss their results in light of the recent publication of the archaea genome organization by Takemata and Bell, 2020.
