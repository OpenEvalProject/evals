# Peer review - Round 1

Editors:
- Laura Ruth Delgui, https://ror.org/03cqe8w59 National Scientific and Technical Research Council Argentina

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68404.sa0](https://doi.org/10.7554/eLife.68404.sa0)

This study presents a valuable finding on the viroporin activity of the ZIKV M protein. The evidence supporting the claims of the authors is solid. The work will be of interest since M protein could be a relevant target for the development of new therapies.


---

# Peer review - Round 1

Editors:
- Laura Ruth Delgui, https://ror.org/03cqe8w59 National Scientific and Technical Research Council Argentina

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68404.sa1](https://doi.org/10.7554/eLife.68404.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Inhibitors of the Small Membrane (M) Protein Viroporin Prevent Zika Virus Infection" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Nir Ben-Tal as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Olga Boudker as the Senior Editor.

Essential revisions (for the authors):

Experiments:

1. Small molecule Inhibitors of ZIKV fusion targeting the E protein have been recently described (see Pitts et al. DOI:10.1016/j.antiviral.2019.02.008, or Li et al. DOI:10.1021/acsinfecdis.8b00322). Since similar inhibitors identified in this work appear to exert their action at the level of viral entry, they could also interfere with receptor binding, viral particle integrity or membrane fusion. The authors should add direct experimental evidence that the inhibitors indeed operate on the M protein. For example, in their previous work, where this issue was covered, the authors used Lentiviral vectors pseudotyped with viral glycoproteins to demonstrate the specificity of the inhibitors towards the viroporin target.

Related to this, to prove direct binding of the compounds to M it would be interesting to measure experimentally the process by ITC (detergent-stabilized samples?) or SPR (see for instance: https://doi.org/10.1016/j.bbamem.2015.12.028).

2. Permeability assays. Bilayers made of PC:PA might not reproduce adequately the viral membrane (thickness, potential interactions with specific lipids). Lipid compositions that approach more closely that of the ZIKV envelope should be used. In this regard, given the high curvature of the viral membrane (small radius of the particle), SUVs or LUVs produced by extrusion through 0.05 um-pore filters might be more adequate model systems to assay M-induced permeability than the larger vesicles used by the authors.

3. The authors claim that helix 1 and protonation of His28 therein are required for M channel function. In the channel model (Figure 6A), to span the bilayer, Helix 1 in a tilted angle combines with the following helix-turn-helix motif. It remained unclear if the authors acknowledge this key structural role of Helix 1. Are monomers of δ-Helix 1 spanning the bilayer in their simulations (Figure 7D)? The importance of helix 1 and His28 for M function can be easily tested in liposome permeabilization assays using synthetic δ-Helix 1 or peptides lacking His at position 28.

4. Figure 8D: rimantadine inhibition is rather low (at 1 μM and within this particular assay). Is it good enough to support the model? JK3/42 inhibition looks more convincing but it is surprising that there is no inhibitor with, say, 10% activity compared to DMSO. And anyway, we probably need a real dose response curve, rather than a single concentration.

5. Figure 9. Full dose response curves are required at least for the most promising hits.

Computations:

6. To prove that M protein is indeed a viroporin the authors should show that their in-silico models indeed translocate ions with specificity. A general methodology to show ion channel activity has been previously described in terms of the total flux of particles for p7 of the Hepatitis C virus (see Chandler et al. PLoS Comp. Bio. https://doi.org/10.1371/journal.pcbi.1002702).

7. The statistical treatment of the simulations needs to be further developed. Although, multiple replicates for each simulations are provided, there is no analysis that combines the results from the multiple replicates.

8. An assessment of the quality of the computationally derived models is lacking. The RMSD traces show values that are typical of intrinsically disordered proteins or poor structural integrity raising questions on the quality of the models and the ability to derive biologically relevant interpretations from the data.

9. The radius of the oligomeric model of the M protein was introduced as an ad-hoc parameter that was never optimized nor explored in detail. Simulations and analysis that prove the robustness of the results to the parameter should be performed. A similar issue is encountered in terms of the tilt-angle of the protein.

10. Details related to the relaxation of the lipid bilayer are not provided. Similarly, convergence of lipid-protein interfaces is not presented so it is impossible to assess if the simulations are well converged.

11. "Simulations of the two species within a POPC lipid bilayer revealed that the single helix rapidly began to revert to a hairpin-like structure (Figure 4c, d).": The figure does not support this statement. To judge this statement the reader needs to see a hairpin structure towards the end of the simulation and a plot of the RMSD of current conformation to the hairpin conformation from cryoEM as a function of simulation time.

12. "The N-terminal extra-membranous helix regulates formation of predicted M dimers": What is the point in this section? Are the dimers physiologically relevant? In which context?

13. "Molecular dynamics simulations favour the formation of compact hexameric channel complexes": The simulations started from tentative oligomeric structures, which is very risky because they may explore irrelevant regions of conformational space. Indeed, most of these tentative models collapsed and were rejected. However, there is no compelling evidence that the "compact hexameric channel complex" is physiologically relevant.

14. Rimantadine docking (Figure 8B): Without hydrogen bonds that provide specificity, the suggested docking pose does not look particularly good. How does this pose compare with that of binding to the influenza M2 channel, where we know that binding is real?

15. "Thus, inhibitor effects and docking data supported the presence of more than one distinct druggable binding site within M complexes, to exploit via novel chemical series": A bold statement that is not supported by any data. There is no direct evidence that links the predicted docking poses and inhibitory data. Especially that theoretically the compounds may act on a completely different target. Either another viral protein or a host protein that interfaces with the virus.

16. "Whilst it is possible that the canonical targets for these repurposed compounds might exert indirect antiviral activity rather than acting upon M, the chances of this occurring for the complete set were remote given their diversity": Incorrect statement. Theoretically each compound might affect its own unique target.
