# Peer review - Round 1

Reviewers:
- Nir Ben-Tal, Tel Aviv University , Israel

## Review text

DOI: [10.7554/eLife.18432.031](https://doi.org/10.7554/eLife.18432.031)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Mechanism of allosteric regulation of β2-adrenergic receptor by cholesterol" for consideration by eLife. Your article has been favorably evaluated by Arup Chakraborty (Senior Editor) and two reviewers, one of whom, Nir Ben-Tal (Reviewer #1), is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The effects of membrane lipids on the structural and dynamic properties of membrane-bound proteins, as well as on their biological function, has been the subject of numerous studies. Cholesterol constitutes a particularly interesting example, as it has a complex effect on membrane structure and is also known to bind specifically to many membrane proteins. One such case is the β2-adrenergic receptor (β2-AR), to which cholesterol molecules have been shown to bind specifically. Moreover, cholesterol has been found to improve the stability, ligand binding, and signaling properties of the β2-AR. However, the mechanisms underlying these effects have never been explained in detail, and it is unclear whether cholesterol acts directly or by changing membrane properties like thickness or order. Aside of the academic interest in understanding how cholesterol modulates GPCR action, this issue is also important for the pharmaceutical industry. GPCRs constitute a major target for pharmaceutical drugs and there is a growing interest in finding molecules that can modulate GPCR activity by binding to allosteric sites.

In the current project, Vattulainen et al. studied the effect of cholesterol on the structural and dynamic properties of the β2-AR using extensive MD simulations. The simulations predicted three main cholesterol binding sites. The first (IC1) is in agreement with the crystal structures of the β2-AR, and is at the general area of a known conserved cholesterol-binding motif (CCM). The second binding site (IC2) is undocumented, and the third (EC1) is in agreement with the crystal structure of the adenosine 2A receptor. While the validity of EC1 and IC2 as specific cholesterol binding sites is yet to be confirmed, the fact that the well-documented IC1 has also been predicted by the same simulations is encouraging. Furthermore, EC1 and IC2, if valid, can be used as potential target sites for GPCR-specific drugs.

The simulations also predicted two cholesterol-induced effects on the β2-AR. The first is a general restriction of the inherent dynamics of the protein. This effect was not observed when the general properties of the membrane were changed in the absence of cholesterol, and thus, the authors concluded that this effect is specific. The second cholesterol-induced effect predicted by the simulation appeared in the second binding site, IC2. There, cholesterol was predicted to push the intracellular end of TM6 more towards the core of the helical bundle, and prevented the outward movement of this helix. This effect is particularly interesting, as the outward movement of TM6 is associated with GPCR activation, and creates the binding site for the receptor's cognate G-protein. The restriction of TM6 movement by cholesterol is a potentially important allosteric effect, which again, can be used to modulate GPCR activity.

This is an important project and the manuscript reads well, however, a number of outstanding issues, listed below, should be addressed before decision can be made about publication.

Essential revisions:

1) The general restriction of β2-AR dynamics by cholesterol is rather obvious considering the rigid structure of cholesterol; this rigidity would restrict the dynamics of any molecule bound to cholesterol, be it a neighboring membrane lipid or a protein. Having said that, the fact that cholesterol analogues had a weaker effect on protein dynamics despite their rigid structure suggests that additional factors are in play. Perhaps this issue could be explored in greater detail to decipher the energy determinants and physicochemical underlines.

2) A discussion of the effect of cholesterol binding to the first binding site (IC1) is missing. This site resides in a cleft created by TMs 1-4 and contains the conserved cholesterol consensus motif (CCM). The conservation of the CCM has implicated it as a possible allosteric site in class A GPCRs. Since the current study focusses on possible allosteric effects of cholesterol, the neglect of IC1 in the analysis of the results seems odd. Perhaps the authors can extract this information from the existing simulations.

3) Furthermore, the results could be correlated with evolutionary data (e.g., using ConSurf). The anticipation is that biologically relevant binding sites would be shared among other GPCRs (orthologues at the very least), which implies that the binding residues should be evolutionarily conserved.

4) Figure 1—figure supplement 1: That the shape of the distances distribution changes with cholesterol concentration in a non-monotonic manner is of concern. Maybe in spite of the long simulation time the results are still not converged in all ranges?

5) This has implications on the main research question here, i.e., whether cholesterol affects the conformational changes of the receptor directly or via general effect on membrane properties. The authors argue that the distribution of receptor' conformations when cholesterol binds the receptor directly (Figure 1) is markedly different in comparison to when it does not (Figure 3). However, to me the difference is small, and in view of the non-monotonic behavior mentioned above, the conclusion might be erroneous.

6) While the focus here is on inactivation it would be nice to show also activation for completeness.

7) In the Introduction – we would value a little more background on what is known of the effect of cholesterol on GPCR and specifically β2AdR function. The Introduction says that cholesterol likely interacts with GPCRs and 'has been shown to influence the ligand binding and signaling properties of β2AR'. This is a bit vague given this underlies the whole of the study presented here. Or perhaps not much is known experimentally, in which case to what extent can one formulate a clear hypothesis to be tested via simulation?

8) Introduction, last paragraph. The 'physiological' concentration of cholesterol is given as 10 mol%; Sampaio et al. says cholesterol concentration in e.g. epithelial cell membranes is more like 25 to 30 mol% (Sampaio et al., 2011, PNAS).

9) Subsection “Membrane-mediated interactions not the key”: the authors show quite conclusively that the effects of cholesterol on the conformational dynamics of the receptor and are not due simply to a change in the physical state of the surrounding bilayer. A clinching test would be to place cholesterol at the binding sites (perhaps by taking a snapshot from the high cholesterol simulation), then place the receptor/cholesterol complex in a cholesterol free membrane and see how the conformational dynamics of the protein change as the cholesterol is release. Has this been done? From the discussion of binding lifetimes (subsection “Binding lifetime depends on cholesterol”), the bound cholesterols might dissociate on a 0.1 µs timescale. Indeed, is this the simulation in Figure 1—figure supplement 1A (it is not clear – Table 1 is a bit impenetrable)? And if so, what is the time course for unbinding of the cholesterols? This needs to be explored/explained in more detail.

10) Subsection “Cholesterol analogues interact with β2AR”. Are there any experimental data for the specificity of the cholesterol effects on β2AdR function?

11) The Discussion could perhaps be a bit tighter – to some extent it re-iterates what has been said earlier.
