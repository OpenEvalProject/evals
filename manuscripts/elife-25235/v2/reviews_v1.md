# Peer review - Round 1

Editors:
- Andreas Martin, University of California, Berkeley , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.25235.015](https://doi.org/10.7554/eLife.25235.015)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Symmetry broken and rebroken during the ATP hydrolysis cycle of the mitochondrial Hsp90 TRAP1" for consideration by eLife. Your article has been favorably evaluated by John Kuriyan (Senior Editor) and three reviewers, one of whom, Andreas Martin (Reviewer #1), is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: Art Horwich (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In the present study, Elnathan et al. investigate the ATPase mechanism of the mitochondrial Hsp90 TRAP1, how its ATP hydrolysis is coupled to dimer asymmetry, and how hydrolysis-coupled conformational switching of protomers between buckled and straight states may rearrange client protein binding sites for remodeling. Using a combination of X-ray structure determination and kinetic crystallography, MD simulations, and elegant biochemical experiments with wild-type TRAP1 and mutant heterodimers, the authors provide strong evidence for sequential and deterministic ATP hydrolysis in the asymmetric dimer, which may induce a conformational flip to drive the ATPase cycle forward and promote the mechanical remodeling of clients. This study thus answers important, long-standing questions about the coordination of ATP hydrolysis and conformational changes of Hsp90.

All reviewers agreed in their overall positive assessments, sharing enthusiasm about this elegant study and its important novel insights into the ATP-hydrolysis cycle of Hsp90. However, they also agreed about revisions that will be necessary before we can make a final decision about publication. These revisions will, for instance, have to address discrepancies in the presented kinetics for dimer closure and ATP hydrolysis, and the derived model for the rate-limiting step in the ATPase cycle. Furthermore, the study in general lacks required statistical analyses, as there is no information provided about the number of measurement repeats, errors, or statistical significance of the results. The authors should also strongly consider to further experimentally support the main conclusion about conformational switching. It may indeed be possible to directly monitor the switch in protomer conformation upon ATP hydrolysis, using a heterodimer that is already available. The reviewers agreed that such measurements would significantly strengthen the conclusions of this manuscript and should be feasible to be completed within a couple of months.

As outlined below, the reviewers also request additional discussions, clarifications, and the presentation of more detailed data, for instance for the FRET-based measurements.

Critical revisions:

The reviewers have suggested that a set of experiments would be valuable to resolve some important questions. These proposed experiments should be considered seriously, and if not considered feasible then the revised manuscript should provide a careful justification for why that is the case.

These questions concern the proposal that preferential ATP hydrolysis in the buckled subunit of the closed asymmetric TRAP1 dimer leads to a conformational flip, in which the buckled, now ADP-bound subunit straightens and the straight subunit becomes buckled to facilitate the second ATP hydrolysis event. However, the authors were so far unable to directly monitor this conformational switch or show any succession of states. The current model is solely based on results for static, non-switching subunits that show differential hydrolysis activities and preferred buckled vs. straight conformations depending on the nucleotide state. The authors state in the discussion that "kinetic rather than thermodynamic processes govern progression through the conformational cycle", but present mainly thermodynamic two state measurements that may also be explained by a shift in equilibrium. Experimentally monitoring the switch would therefore significantly strengthen the main conclusion and model.

By using spin-labeled heterodimers in DEER measurements, it may in fact be possible to directly detect the conformational switching upon ATP hydrolysis. The authors should consider spin-labeling the wild-type subunit in the wild-type / E115A heterodimer. Assuming an equal probability of WT and E115A subunits adopting the buckled conformation after adding ATP, about 50% of the WT subunits should be buckled with a small interprobe distance. ATP hydrolysis upon Mg addition is expected to induce straightening of those WT subunits, which should be accommodated by a shift to the larger interprobe distance. This state would then be stable due to the lack of ATP hydrolysis in the E115A subunit (as shown for the high-FRET closed state in Figure 1D). Heterodimers in which the E115A subunit was buckled and the labeled WT subunit was straight after ATP addition should not lead to an inverse change in DEER signal, because the EA subunit is hydrolysis incompetent. Actually showing a shift in interprobe distance that follows the kinetics of ATP hydrolysis in the WT subunit would thus nicely confirm the prosed model.

These DEER experiments on subunit flipping could be performed before and after Mg addition to monitor the start and end state only, or by taking aliquots during the transition to actually detect flipping kinetics, with the prerequisite that snap-freezing of the sample slows down the ATP hydrolysis and conformational changes enough to preserve the not yet flipped population during measurement.

Other important revisions:

The reviewers have raised a number of other issues that we feel could be addressed through careful revision of the manuscript, with explanations provided as needed, but without necessarily engaging in additional experiments.

1) Errors and number of repeats should be reported for all measurements.

2) The authors convincingly show by kinetic crystallography that the buckled protomer in the asymmetric TRAP1 dimer hydrolyzes ATP in the absence Mg more rapidly than the straight protomer. However, what is the evidence that these differences in Mg-independent hydrolysis directly translate to the Mg-dependent hydrolysis, which occurs an order of magnitude more rapidly? The authors should comment on potential mechanistic similarities between Mg-independent and Mg-dependent ATP hydrolysis by Hsp90 that would support this assumption. Furthermore, there is some concern about the direct comparison between hTRAP1 and zTRAP, which show a ~ 10-fold difference in Km.

3) The authors performed MD simulations on buckled and straight protomers to explain the differential rates in ATP hydrolysis. However, for those MD simulations the authors replaced the ADP-AlF4 in the crystal structure with ATP-Mg and modeled the ATP lid region of both protomers to be identical and ordered. The authors should at least comment on why it is valid to assume that the nucleotide replacement does not affect the local structure and dynamics of the ATPase sites, and why they assume that fixing the ATP lid, which directly faces the ATP phosphates and is disordered in the straight protomer, is not expected to have a significant effect on the MD simulations (in particular for the straight protomer). It is surprising to me that having more and longer-lived waters in the straight compared to the buckled protomer would lead to slower hydrolysis.

4) The authors present in Figure 1C the single-turnover ATP hydrolysis of the WT / E115A heterodimer (induced by addition of hot/cold ATP-Mg), with a kcat of 0.37 min-1. In Figure 1D, they present the kinetics for the buildup of the closed state of WT / E115A, and discuss that "The buildup rate of the heterodimer (0.16 min-1) is comparable to the steady-state ATP turnover rate of the cysteine-free wildtype (0.19 min-1, Supplementary file 1A), indicating that having only one active ATP site does not affect the kinetics of forming the closed state."

However, it is unclear why the formation of the closed state for WT /E115A should show the same rate constant as steady-state ATP hydrolysis by WT TRAP1. Due to the hydrolysis-incompetent E115A subunit that traps the closed state (cf. Figure 1F), the closed-state formation can be considered single-turnover and should show the same kinetics as single-turnover ATP hydrolysis (0.37 min-1). Both experiments were started by the addition of ATP-Mg, and since forming the closed state precedes hydrolysis, its kinetics should be as fast or faster. The authors should explain the observed 2-fold difference between those rates.

5) Figure 3 shows the kinetics of dimer closure induced by ATP / no Mg, with a rate of 0.116 min-1. Considering that dimer closure precedes hydrolysis, as proposed in the authors' model, why is single-turnover ATP hydrolysis (induced by addition of ATP-Mg) almost 5-fold faster (k = 0.54 min-1, Figure 1 C)? The dimer closure is also ~ 1.6 fold slower than the steady-state hydrolysis-rate of TRAP1 (0.19 min). Is this difference significant and indicating some effect of Mg on dimer closure, or just experimental error?

Does the difference in rate for dimer closure of WT TRAP1 and the WT / E115A heterodimer upon ATP (no Mg) addition (Figure 1E) indicate some additional effect of the EA mutation, besides eliminating ATP hydrolysis?

In the Discussion the authors mention that dimer closure is normally rate-limiting, which could be bypassed by adding ATP in the absence of Mg. But we wonder how the closure step can be rate-limiting, if single-turnover ATP hydrolysis (which should include domain closure) is significantly faster than steady-state hydrolysis (0.54 min-1 vs. 0.19 min-1).

6) When proposing their model, the authors state that "two ATP hydrolyses are required for TRAP1 to progress efficiently through its ATPase cycle". However, this is contradicted by the WT / E402A heterodimer, which shows stimulated ATP hydrolysis (Supplementary file 1), despite the E402A mutation inducing a permanent ADP state and significantly reducing the ATP hydrolysis rate of the protomer / homodimer. This may indicate that both protomers have to adopt the ADP state, but not necessarily hydrolyze ATP, in order to progress efficiently through the ATPase cycle (i.e. one protomer could remain ADP bound throughout the entire cycle).

7) Figure 1A: Is the deviation significant? How was the error in the ATPase activity determined? The authors should present statistics on at least 3 repeats of the experiment, which is particularly important given the low ATPase activities. What was die ATP concentration? Is ATP definitely saturated? Could this effect be explained by a shift in KM or vmax?

8) Figure 1B: How was the functionality of the labelled proteins tested? Especially as the Cys-light version already has only 20% ATPase.

9) Figure 1C: How is the +/E115A trace normalized?

10) Figure 1D, Figure 3A, and Figure 3—figure supplement 1: What is "Change in FRET"? Are the authors referring to FRET efficiency? Please show the absolute acceptor and donor fluorescence here and also in Figure 1E, 1F. Otherwise the significance of the changes cannot be judged, and it is important to convincingly rule out quenching etc.

11) Figure 3B: How is the 80% closed state calculated? There seems to be more than 20% overlap judged by eye.

12) The R402 in hTRAP1 solely contacts the γ-phosphate, but how is this knowledge enough to state that R402A mimics the ADP state?

13) Why is closing in Figure 5—figure supplement 1 not shown with the FRET-assay (Figure 1), which would in addition give kinetic information?

14) Figure 5A-C: The authors claim that nearly all molecules are buckled on one side in 5B, 5C. Please quantify. This might be even less than 80%, especially in 5C.
