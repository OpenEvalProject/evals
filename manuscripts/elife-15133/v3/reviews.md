# Peer review - Round 1

Editors:
- Christian Rosenmund, Charité-Universitätsmedizin Berlin , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.15133.032](https://doi.org/10.7554/eLife.15133.032)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Physical determinants of vesicle mobility and supply at a central synapse" for consideration by eLife. Your article has been reviewed by two peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Gary Westbrook as the Senior Editor. The reviewers have opted to remain anonymous. The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript examines vesicle mobility and supply at mossy fibre synaptic terminals (MFTs), to determine how these parameters contribute and are putatively rate limiting during high release activity. Using a combination of 3D ultrastructural analysis, measurements of vesicle diffusion and simulations, the authors convincingly conclude that vesicle diffusion is the main rate limiting factor in vesicle supply, which is surprising as this would limit the impact of vesicle tethering and priming processes at least on a long time scale, previously considered to be the critical rate limiting step in preparing vesicle for fusion.

Essential revisions:

A major criticism relates to the feasibility of using simple confocal FRAP measurements to obtain vesicle mobility values in this preparation:

1) As stated in the text MFTs in contrast to e.g. small hippocampal boutons offer the advantage of being clearly larger than the confocal bleaching volume. However, exactly this fact might account for the differences in measured SV mobilities compared to hippocampal boutons: the confocal volume for FRAP or FCS measurements in the latter case almost inevitably contains the volume close to the active zone (in axial direction the volume extends far beyond the small bouton boundaries). This is less likely the case in FRAP experiments in the MFTs which measured 7 to 10 µm according to the authors: thus, rather volumes in the middle of the MFT at some distance to the AZs where the SV density is lowest (Figure 6) are probed. Although multiple or at least three measurements were made per terminal at different locations the large axial extent of the bleaching volume implies that mostly volumes away from the small AZs are covered. Given this and that the '3D reconstructions revealed the AZs of MFTs are small and surrounded by a cloud of vesicles that is highly variable in shape and extent', could the measured fast rates of fluorescence recovery predominantly reflect fast SV movements at the fringes of these SV clouds and even in-between clusters from different AZs? Here, overall SV densities are small and thus the dynamics might be much higher than within the densely packed areas close to the AZ, where SVs in EM tomograms even appear interconnected by short filaments, which might highly reduce their mobility.

In summary, given the experimental design of the FRAP measurements and the geometry of MFTs with their inhomogeneous SV distributions, there was concern about the claim that these results 'show diffusion ultimately limits vesicle supply during sustained high-frequency signaling at a central synapse'! SV supply and mobility at the AZ simply have not been and cannot be easily measured in this preparation.

2) An important conclusion of the paper is that "the geometry of the diffusible space determines the size of the RPV", based on the fact that back extrapolation of the cumulative release provides a similar pool size as measured in MFTs. However, before arriving at this conclusion several aspects should be addressed/discussed:

a) Using linear back extrapolation is known to underestimate the RRP due to the fact that the replenishment rate is not constant but depends on the depletion of the RRP (for a full RRP at steady-state the net replenishment rate is 0) (Neher, 2015). This error is larger for higher replenishment rates, which could explain the low RRP for the open geometry. Since in the simulations all vesicles are tractable, accurate estimates of the replenishment rates over time should be calculated and used for more accurate RRP estimates in the default- and open geometry.

b) It is not clear how (molecular) priming is addressed in the model. Primed vesicles in the RRP are most likely docked at/tethered to the membrane via (partial?) assembly of SNARE-complexes and are therefore not free to diffuse (?). One would expect that this stabilizes an RRP of a certain size, independent of the geometry of the diffusible space but dependent on the number of available docking sites. This is supported by the fact that deletion of priming molecules like Munc13 and Munc18 produce a complete loss of RRP without affecting the geometry of the terminal. The impact of molecular priming on the RRP in the diffusion model should be discussed in the context of this evidence.

c) A well-established method to assess the RRP is the application of hypertonic solutions. Interestingly, although this manipulation most likely has a strong impact on the geometry of the diffusible space (shrinkage), concentrations beyond 500mM have a strong effect on release kinetics but not on the total release or steady-state priming rates at the end of the stimulus. The authors should discuss how these findings can be reconciled with the model.

3) Priming/RRP replenishment is sped up in a Ca2+ dependent manner during high frequency stimulation (Sakaba & Neher, 2001). This suggests an active flow of vesicles in the direction of the AZ during or a change in mobility properties of the vesicles. The authors should discuss how this fits in their model.

4) Software or scripts should be made available to the community as supplementary material via eLife or via a public repository for computational models for neuroscience.
