# Peer review - Round 1

Editors:
- László Csanády, Semmelweis University Hungary

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.28626.017](https://doi.org/10.7554/eLife.28626.017)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Conformational dynamics in TRPV1 channels reported by an encoded coumarin amino acid" for consideration by eLife. Your article has been favorably evaluated by Richard Aldrich (Senior Editor) and three reviewers, one of whom, László Csanády (Reviewer #1), is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

This is a highly ambitious study pioneering in two techniques: exploiting engineered unnatural aminoacids as a means for targeted introduction of a small fluorescent probe into a protein, and using single-molecule imaging to track in real time conformational changes of a membrane protein in a living cell. The authors apply these techniques to address potential gating-associated motions of a residue (Y671) in the vicinity of the selectivity filter of the TRPV1 cation channel. By incorporating hydroxyl-coumarin into position 671 the authors show that this residue is exposed to a different local environment in the presence of the activating ligand capsaicin and interpret this to indicate that Y671 is more water exposed (dimmer) in the closed state. They conclude that channel opening is accompanied by a conformational change of the Y671 side chain, which decreases its solvent exposure. The results suggest that the TRPV1 selectivity filter plays a role in gating, and illustrate the power of optical recordings for studying protein conformational dynamics at a single-molecule level.

The experiments are carefully designed and carried out, and seem to mostly support the conclusions. However, there are a number of conceptually important points in the manuscript that are unclear to the reviewers. These will need to be clarified before the manuscript can be published. Specific guidelines are provided below.

Essential revisions:

1) Autocorrelation time constant:

"changed the slow time constant from 1360+/-287 ms to 580+/-182 ms […] reporting on an agonist-induced increase in tau. Such a result can be interpreted in multiple ways: i) the stabilization of the open state after ligand binding (i.e. longer bursts of activity)…"

There is double confusion here. First, tau decreases, rather than increases, upon agonist addition. Second, the autocorrelation time constant is the inverse of the sum of the opening and closing rate (for a two-state channel tau=1/(kco+koc)). Therefore, a lengthening of open times (i.e., a decrease in koc) would prolong, rather than shorten this time constant. Also, please comment on how the autocorrelation time constant in the presence of capsaicin (>500 ms, Figure 3C) agrees with the current activation time constant seen in electrophysiological measurements (t1/2 of capsaicin activation is on the order of 100 ms according to Yao, Liu and Qin, BJ, 2010). Is the component (1364ms) at 0 cap due to spontaneous openings? If so, how does this value correlate with the spontaneous gating kinetics of TRPV1.

2) Dwell-time analysis:

Please comment on the reliability of the threshold analysis shown in Figure 3B. The choice of a threshold at 2.5 SD of the background signal seems arbitrary. It appears that if the threshold had been chosen at e.g., 2.3 SD, then many additional "openings" would have been identified (although for a Gaussian-distributed background noise the area under the tail beyond 2.3 SD would still be expected only ~1%). Is there anything to be said about an optimal choice of the threshold, and about the specificity vs. sensitivity of the threshold approach?

3) Figure 3E-F:

Please clarify what the difference is between the plot shown with black symbols in Figure 3E and the plot shown with gray symbols in Figure 3F (both fitted with orange lines), apart from normalization? The plot in 3E reports a less-than-2-fold, that in 3F an ~3-fold, stimulation by saturating capsaicin concentrations.

How can the only 2x (3x?) increase in PL1 upon exposure to saturating capsaicin, suggested by the analysis of the optical recordings (Figure 3E-F, plots fitted with orange lines), be reconciled with the ~10x increase in Po measured in electrophysiological recordings (Figure 3F, plot fitted with blue line)? Is the PL1 of ~0.2 in the absence of capsaicin related to the "intrinsic blinking" of the dye (Discussion, third paragraph)? But there it is said that this "background open probability" was subtracted from the data. Do the plots shown in Figures 3E-F represent such corrected, or uncorrected data? – This should be clearly indicated in the figure legend.

4) Electrophysiology:

Why was the capsaicin concentration dependence of TRPV1 currents (Figure 3F) obtained at +140 mV, whereas the optical measurements on intact cells clearly reflect behaviour at negative (physiological) membrane potentials? Given the voltage dependence of TRPV1 gating, the EC50 for capsaicin activation is expected to be dramatically different at +140 mV vs. Vm<0.

5) The fluorescence data traces for the control W426 control position are not shown. Please make these control traces and photon counts a prominent part of the main paper so the reader can compare the behavior of control positions with both types of imaging.

6) The molecular simulation was done with wild-type, not coumarin-carrying channels. Y671 is a critical residue (e.g., cysteine replacement severely disrupts channel function), so it is hard to predict how the local pore structure might be perturbed by the coumarin -> Tyr substitution. For that reason, it is uncertain to what extent the simulation results can be extrapolated to mutant channels. Thus, this part might be better positioned in the Discussion section.

7) It should be pointed out that the proposed hydration model is not conclusive: the data support a change in the local environment around Y671, but many other factors could be involved that may contribute to these changes by perturbing local polarity, including movement of the pore helix with associated changes in the direction of its dipole moment. A more thorough discussion of this issue would improve the paper.

8) The methodology (coumarin incorporation and optical measurement) should be described in more detail. For example, what is the efficiency of incorporation of non-natural amino acid? How about the specificity (i.e., off-target incorporation)? How bright is the fluorescence (relative to conventional dyes or FPs)? How is the 7/1 expression ratio controlled? How long does the dye last for recording before it is bleached in the single-molecule recording mode?
