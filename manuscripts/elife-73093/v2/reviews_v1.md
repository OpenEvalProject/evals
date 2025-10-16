# Peer review - Round 1

Editors:
- Baron Chanda, https://ror.org/01yc7t268 Washington University in St. Louis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73093.sa0](https://doi.org/10.7554/eLife.73093.sa0)

This study examines the influence of voltage on conformational dynamics of voltage-sensing Hv1 channel at a single molecule resolution. Previously it was shown that although Hv1 channels lack a separate pore domain unlike most members of the voltage-gated channel family, the pore opening and voltage-sensing are distinct but linked processes. This study provides new insight in the mechanism of gating by showing that the voltage-sensor is able to access an intermediate conformation distinct from the activated and resting state.


---

# Peer review - Round 1

Editors:
- Baron Chanda, https://ror.org/01yc7t268 Washington University in St. Louis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73093.sa1](https://doi.org/10.7554/eLife.73093.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for sending your article entitled "Structural dynamics determine voltage and pH gating in human voltage-gated proton channel" for peer review at eLife. Your article is being evaluated by 3 peer reviewers, and the evaluation is being overseen by a Reviewing Editor and Richard Aldrich as the Senior Editor.

Please pay attention to Editor's note in parenthesis for further clarification.

Reviewer #1:

This paper uses a powerful single-molecule fluorescence approach to study the conformational dynamics of the voltage sensor in a human voltage-gated protein channel. The approach is impressive and builds on previous work of the senior author adapting single-molecule fluorescence to study gating dynamics. The major advance of the paper is the demonstration of smFRET on reconstituted human voltage gated proton (hHv1) channels in liposomes. The major conclusions of the paper are: (1.) the voltage sensing S4 helix is dynamic and altered by both pH and voltage; (2.) An intermediate state exists between the activated and resting states; (3.) H140 residue is important for sensing extracellular pH. These conclusions are supported by the data presented. The work could be further strengthened through a more thorough analysis of their existing data to make their proposed gating model more quantitative and predictive. Overall, this work will be of interest to colleagues in the ion channel and smFRET communities.

Major comments:

1. The authors claim that conformational changes between deactivated and activated states are probabilistic, not deterministic. This is not necessarily true without information on dynamics, as one can imagine a model where transitions from deactivated to activated proceed through an irreversible intermediate state (thereby, 3 states exist but transitions are deterministic). To test this hypothesis, the authors should examine the transitions between the states using transition density plots or (even better) build kinetic model(s) of the data as a function of voltage/pH using software such as QuB (which is accessible directly from SPARTAN) or ebFRET. Such analysis would allow rates to be included in Figure 5 and enable probabilities of state occupancies and transitions to be calculated given a pH or voltage, leading to testable predictions of the model in other backgrounds and for other voltage-gated channels.

2. A key advantage of smFRET data is the ability to link conformational dynamics to structure. While the authors estimate the movement of the S4 segment to be ~20 angstroms, it is unclear how large the movement to the "intermediate" state is, whether that distance is consistent between the different FRET pairs used, and whether that distance agrees with structural predictions.

3. The authors note the use of SPARTAN for single-molecule analysis; however, more details need to be provided to communicate how the data were treated to ensure reproducibility. For example, it is unclear how images were preprocessed, how single molecules were defined (e.g., pixel size), how crosstalk between the channels was accounted for (if at all) and if any background subtraction was performed. In addition, there is no equation provided for how FRET efficiency was computed and whether correction factors were applied (see DOI: 10.7554/eLife.60416 for example).

4. Two comments regarding single molecule idealization. First, the authors use SPARTAN and fit the data to three states, but it is unclear if any other models were tested (e.g., 2 states or 4 states) and if so, how they were ranked. This is particularly important since a major conclusion of the paper rests on the existence of a third, intermediate state. Second, it is unclear why transitions are identified in the Viterbi paths (idealized trajectories) once the acceptor has photobleached (FRET = 0) in Figures 1d and S3b. This suggests the model may be overfitting the data and interpreting noise as signal. Were the traces pre-processed prior to idealization by truncating at the photobleaching event?

Reviewer #2:

The manuscript entitled "Structural dynamics determine voltage and pH gating in human voltage-gated proton channel" by Shuo Han et al. studied the conformational dynamics of the human voltage-gated proton channel (Hv1) under different voltages and pHs, which are two stimuli that change the open probability of the channel. The authors purified the wild-type Hv1 and confirmed its function after reconstitution using fluorescence flux assays. Then, they introduced two pairs of cysteine mutations in the cysteineless background and measured the conformational dynamics through single-molecule fluorescence resonance energy transfer (smFRET) after labeling the channel. However, they did not observe changes in smFRET when voltage was changed in the proteoliposomes. Then, they introduced the N214R mutation, which abolised Hv1 proton currents without perturbing the channel's gating. In this background, smFRET population distributions were observed at different voltages, suggesting that the absence of changes found in the wild-type Hv1 was caused by the internal acidification of the liposomes, which disfavor the channel activation. Next, using the N214R background mutant, the authors showed that smFRET population distributions depended on the imposed transmembrane voltage. The observed smFRET changes at different voltages suggested that an S4 outward movement occurs at depolarizing voltages. The smFRET population distributions also depended on the internal and external pH values implying that the S4 position changed according to the pH values. The smFRET changes observed at different internal pHs were abolished in the H168Q mutant, which was previously shown to alter the internal pH dependence of the channel. Finally, they propose that H140 is the external pH sensor since the H140A mutation showed smFRET population distribution changes in the wild-type background channel. Although the approach is novel and the results are interesting, the work has a series of important issues that the authors must address.

– A main concern about this paper is that the authors must determine if the dimeric nature of Hv1 is affecting their experimental results. Since the Hv1 dimer is small, there is the possibility that two pairs of fluorophores in different subunits are close enough in space to produce FRET. When two pairs of cysteine mutations are inserted in the channel to measure smFRET between them, there are four cysteines per molecule instead of two. Therefore, the multiple levels of FRET signals measured by the authors could be produced by a putative complicated combination of distances between fluorophores located in different subunits. The authors must address this critical point to assure that the interpretation of the smFRET signal changes is correct.

– It seems that the authors have confusion regarding the activation of the Hv1 voltage sensor, which also applies to other voltage-gated ion channels and proteins in general. As any kinetic process, there are expected different protein conformations at the steady-state distribution, and the macromolecular observable is the average of the ensemble. The state's distribution and the macromolecular ensemble change when the system is perturbed, as it happens for Hv1 when the voltage or the pH is changed. During the entire manuscript, the authors claim that their results "… suggested the biological gating is determined by the conformational distributions of the hHv1 voltage sensor, rather than the conformational transitions between the presumptive 'resting' and 'activated' conformations." There are similar statements in all the sections of the manuscript. Structural models obtained from X-ray diffraction or cryo-EM are models of the more stable conformations, which does not mean that the atomic positions of the protein undergoing activation or deactivation gating are constrained to only those possible conformation trapped by X-ray crystallography. I think the authors' statements refer to the high structural dynamics of the channel, i.e., the small kinetics barriers between the states of the channel. The authors should modify these ideas or interpretations in the manuscript.

(Editor's Note- This comment has come up later too. Please rephrase these sentences to emphasize the novelty of the study. In our opinion, it is the detection of these low probability conformations for voltage-activated process. It may be worth calculating how this compares with a distribution predicted for a simple two state process, where the channel is either activated or resting)

– There is no quantifiable and statistical criterium in the manuscript to demonstrate differences or similarities of the measured distributions. Changes in the smFRET population distributions between different conditions seem subjective, and in some cases, the differences are not evident or clearly derived from the presented results. For instance, although the smFRET population distributions are evident in the mutant K169C-Q194C-N214R at different voltages in figure 1c, this is not obvious for the mutant K125C-S224C-N214R in figure 1e since the red density histogram in the figure does not correspond with the contour map showed. Similarly, figure 2 is poorly analyzed, and no statistical analysis is evident to demonstrate the validity of the conclusions. From the contour maps shown for the mutant S98C-Q194C-N214R, this reviewer observed a higher occupancy of low smFRET at -85 mV compared with 0 and 120 mV, especially when compared with the contours shown in figure 1e. Figure 3a has the same problem since distributions are different for the low smFRET when pHin/pHout 7.5/7.5 and 8.5/7.5 are compared, although the authors do not discuss that. As presented now, it seems that the authors observe differences only when it is convenient for the paper's narrative. A proper statistical analysis of the data is needed in the presented figures and the used methodology.

– Symmetrical pH distributions were obtained using β-escine (concentration? Time of incubation?), while the asymmetric pHs were obtained by changing the extra liposome solution pHs. A better approach would be to establish symmetrical pH during liposomes formation and avoid permeabilization with β-escine since it can perturb the Hv1 conformational dynamics.

(Editor's note- Please address in your discussion)

– Authors concluded that "… Our data conclusively indicate that pH gating of the hHv1 channels originates from the pH-dependent conformational changes of the voltage sensing S4 segment." The data shown by the authors is not sufficient to support this claim since only the mutant K125C-S224C-N214R was evaluated. To properly support this statement, the authors must measure the smFRET distributions using other mutants, including the mutant K169C-Q194C-N214R along with those shown in figure 2. This approach has the additional advantage of showing a better picture of the conformational changes of Hv1 at different pHs.

– To support the claim that H168 is the key internal pH sensor in hHv1, additional experiments are needed. I strongly suggest that electrophysiology should be performed to confirm this claim. Also, the authors' results do not support a direct interaction of H168 or H140 and S4, so it should be stated explicitly that this is only a proposed model to be tested in the future unless additional evidence is presented.

(This is controversial and may require additional experiments. See if you want to possibly resubmit a report rather than a full length article and remove the pH sensor part. We can discuss this if needed.)

– Proton fluxes assays presented in this work are very long when compared with results previously reported by others. For instance, the Mackinnon's group obtained fluorescence steady-state readings after 5 minutes of 40 nM valinomycin addition (Lee et al., 2009). In contrast, the steady-state level in this work is reached at around 30 minutes after adding 450 nM valinomycin, which is an exceedingly high concentration. This difference suggests to this reviewer that perhaps the functional integrity of the purified hHv1 channel has been compromised during purification process and/or liposome reconstitution. The authors should discuss the origin of this discrepancy with previously published work.

– Since proton flux measurements take so long despite of using very high concentrations of valinomycin, a control with empty liposomes treated with the same reconstitution protocol without hHv1 should be included to demonstrate that it is the channel that produced the observed proton fluxes and that they are not originated from liposomes' proton leak. The controls included in figure S1 are insufficient since leaky liposomes will show the same results even in the absence of protein.

– A proton flux assay of the mutant H140A in the wild-type hHv1 background must be included to assure the single mutation does not alter the hHv1 function.

– There is an inconsistency between fluxes shown in figure 4c and S2c. The former showed higher activity of mutant K169C-Q194C compared to wild-type, while the latest show wild-type has higher or equal activity than the mutant. A similar incongruency is evident between figure S1c and S2b in the wild-type channel fluxes. Representative flux assays of each mutant must be included in a supplementary figures section to show the constancy and reproducibility of the functional assay.

– Protein reconstitution protocols for the functional assay and smFRET measurements are different. Is the hHv1 function comparable between these protocols? The authors must demonstrate that the function of the proteoliposomes is similar when the protein is reconstituted using these two different protocols.

Reviewer #3:

The gating of Hv1 protons channels is distinguished from related voltage-sensitive ion channels and phosphatases by an apparently unique sensitivity to changes in both membrane potential and the transmembrane pH gradient (ΔpH = pHo – pHi). The mechanism of ΔpH sensitivity in Hv1 is of widespread interest, but remains only partially understood. In particular, extracellular ionizable residues that are postulated to be required for sensing changes in pHo remain unidentified.

Here the authors utilize a FRET approach in which recombinant, purified Hv1 channels carrying Cys mutations at pairs of extra- and intra-cellular residues are labeled with separate fluorophores and fluorescence changes (and the corresponding FRET ratios) are measured optically over time under conditions that are predicted to alter membrane potential and at various pHi. Although the development of a new optical assay to indirectly measure Hv1 channel activity represents a potentially important advance in the field, the data on which the authors base their main conclusions can be explained by alternative mechanisms that have not been ruled out. Furthermore, the authors' putative identification of a single mutation (H140A) that is purported to abolish pHo sensitivity is inconsistent with previous study showing that simultaneous mutation of both candidate extracellularly-exposed His residues in Hv1 (H140A-H193A) is insufficient to abolish pHo-dependent shifts in the apparent POPEN-V relation measured using voltage clamp electrophysiology 1.

(The previous electrophysiology data is particularly problematic. Please clarify how you expect this to be reconciled.)

The caveats to interpretation of the data presented in this manuscript are many, but several central concerns are outlined here:

1. FRET changes measured here are not independently correlated with channel activity measured using electrophysiological methods, and it remains unclear what effects the double-Cys mutations (either before or after labeling) may have had on the voltage dependence and/or kinetics of channel gating. The reader must assume that mutant channels are WT-like, but a previously published survey of many Hv1 mutations clearly shows that altering channel structure can have major impacts on functional parameters 1.

(Address the caveats in discussion..)

2. The authors interpret FRET changes to selectively report movement of the S4 helix, but Cys residues are introduced into predicted loops between helical segments, and could also report local changes that occur independently of S4 helix movements that are thought to underlie voltage-dependent gating. There appears to be no independent experimental evidence that FRET changes actually report S4 movement. Of concern, only one mutant pair (K169C-Q194C) appears to exhibit a substantial voltage-dependent change in FRET ratio (5 other Cys mutant pairs exhibit little or no apparent voltage-dependent FRET changes), and data in Figure 1f showing this change contains undescribed error bars; neither is any statistical method for quantifying the magnitude of the voltage-dependent FRET change described in Methods.

(This type of concern is understandable but the fact that you are measuring conformational distributions indicates that the channel S4 is detecting different conformations although it may be hard to predict the specific details of this conformation)

3. The data shown in Figure 4d are interpreted to mean that H140A mutation abolishes pHo sensitivity measured by pH-dependent quenching of a pH-sensitive dye (ACMA) within liposomes containing purified and reconstituted Hv1 channels (a similar method was previously described 2, but is evidently not cited in the References). The authors state that "on the H140A mutation background, the FRET distributions at the K169C-Q194C labeling sites do shift by voltage (Figure 4d)", which seems to mainly argue that this mutant channel remains voltage-dependent, and evidently does not directly address whether pHo sensitivity is altered. Furthermore, a previous study showed that H140A-H193A mutant Hv1 channels retain WT-like pHo sensitivity (-46 mV/pHo unit shift in VTHR, which is similar to the -38 mV/pHo unit shift measured for WT Hv1; see Table S1) 1.

1 Ramsey, I. S. et al. An aqueous H+ permeation pathway in the voltage-gated proton channel Hv1. Nat Struct Mol Biol 17, 869-875, doi:10.1038/nsmb.1826 (2010).

2 Lee, S. Y., Letts, J. A. & MacKinnon, R. Functional reconstitution of purified human Hv1 H+ channels. J Mol Biol 387, 1055-1060, doi:10.1016/j.jmb.2009.02.034 (2009).

Recommendations for the authors:

1. Determine whether mutations alter biophysical properties of expressed Hv1 channels.

2. Establish that FRET changes necessarily report conformational rearrangements of the S4 helix, and not other motions that may be correlated with but not causal to voltage-dependent gating.

3. Address why FRET data are evidently contradictory to previously published electrophysiological data.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Structural dynamics determine voltage and pH gating in human voltage-gated proton channel" for further consideration by eLife. Your revised article has been evaluated by Richard Aldrich (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed in the text, as outlined below:

1. Overall, the authors basic observation that changes in membrane potential alter S4 position in a way that is consistent with the general consensus of voltage sensor function and previous reports of Hv1 specifically. Despite the potential of smFRET to reveal new insights into conformational rearrangements that occur during Hv1 channel gating, caveats to the interpretations of the data limit the value of the information in the current manuscript, and the work does not significantly advance knowledge in the field.

Data in Figure 3 lead the authors to hypothesize that in H168Q, more negative voltage is required to move S4 into the resting (down) conformation than would be required for WT Hv1. A previous report1 shows that whereas both WT Hv1 and H168T manifest qualitatively similar positive shifts in the positions of their G-V curves as pHi is raised, the magnitude of the pH sensitive-shift in the position of the G-V curve is shallower (~20 mV/pHi unit) in H168T than in WT Hv1 (~40 mv/pHi unit). A positive shift in the G-V (i.e., at higher pHi) shows that channel closing occurs at less hyperpolarized potentials (or opening occurs at more depolarized voltages), which is opposite to the conclusion reached by the authors. One possible explanation is that the direction of proton currents at positive potentials is inward for H168T at high pHi all voltages between Vthr and the Nernst potential for H+ (EH+). Because the G-V is less shifted at acidic pHi in H168 mutants, there is a higher likelihood that the net current is inward, and if proton fluxes are oppositely directed in WT and H168Q channels, one might expect dramatically different effects on intra-liposomal pH (pHo) to result, as demonstrated by the authors for WT vs. N214R.

The apparent effects of pHi acidification on S4 position is complicated by the possibility pHi is unknown under the experimental conditions used here.

Please discuss these concerns in the discussion.

2. An alternative explanation for the data in Figure 3 not stated by the authors is that Hv1 H168Q channels enter a closed-state conformation in which nonetheless S4 remains in the activated (out) position, but this seems unlikely given that Hv1 channels do not appear to inactivate. The apparent paradox requires explanation and/or demonstration that membrane potentials and intra-liposomal pH remain intact during the experiments with H168Q; similar caveats apply to measurements of fluorescently-labeled WT (K125C-S224C and K169C-Q194C) channels. Unfortunately, it's not clear to me that the authors will be able to measure membrane potential and/or intra-liposomal pH (pHo) may not be within the authors av

Cherny, V. V., Morgan, D., Thomas, S., Smith, S. M. E. & DeCoursey, T. E. Histidine(168) is crucial for DeltapH-dependent gating of the human voltage-gated proton channel, hHV1. J Gen Physiol, doi:10.1085/jgp.201711968 (2018).

In order to provide a nuanced perspective, please discuss the above limitations and its impact on your conclusions.

3. There are still a number of typos/mistakes in the revised version. Please have it proofread carefully if needed by an experienced colleague.
