# Peer review - Round 1

Editors:
- Axel T Brunger, Howard Hughes Medical Institute, Stanford University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.00708.010](https://doi.org/10.7554/eLife.00708.010)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Her2 activation mechanism reflects evolutionary preservation of asymmetric ectodomain dimers in the human EGFR family” for consideration at eLife. Your article has been favorably evaluated by a Senior Editor and 3 reviewers, one of whom, Axel Brunger, is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

General assessment:

The mechanism of Her2 activation and signaling is of considerable importance considering its role in human disease (including cancer) and as a drug target. The available biochemical data suggest that the activation process upon ligand binding requires formation of a heterodimer consisting of Her2 and Her3. Her2 lacks ligand binding (or binding is weak), whereas Her3 does not have significant kinase activity. Thus, it is only upon hetero-dimerization that ligand binding can initiate kinase activity. Yet, structural studies by x-ray crystallography of the human EGFR-family receptors ectodomains showed only symmetric dimers with ligands bound in both monomers. Intriguingly, crystal structures of Drosophila EGFR ectodomains showed asymmetric dimers with only one ligand bound. The question, however, was if the Drosophila crystal structures are representative, what is going on for the human EGFR receptors as well. This work now suggests that this is indeed the case: starting from the crystal structures of the human Her2 homodimer as well as the Her2-Her3 heterodimer, long-timescale (microsecond) molecular dynamics simulations were performed. The simulations were first successfully tested starting from the Drosophila heterodimer structures.

Highlight:

The simulations show that a model of the human Her2 homodimer is not stable, but, rather, that the dimer interface opens to produce a large gap. In contrast, a model of the Her2-Her3 heterodimer with one bound ligand was stable. This work thus suggests that the asymmetric Drosophila EGFR ectodomain crystal structures indeed represent the norm, rather than the exception.

While this is an important finding, the simulations should allow the authors to draw some mechanistic conclusions about how the conformational changes within the various dimers occur and how the different interfaces are stabilized. Such additional mechanistic insights would also illustrate the power of their long-time simulations and considerably strengthen this work.

Required revisions:

1) By taking the richness of the MD simulations and reducing them to cartoons in Figures 3A, 4, and 5, the authors do not go much beyond simply confirming conclusions already drawn from the studies of Drosophila EGFR. Surely the purpose of simulations such as those described here is to generate informative models that make experimentally testable predictions? In the crystallographic studies of dEGFR, identification of residues involved in interactions across the asymmetric dimer interface was informative. The nature of this new interface is crucial for understanding the fly receptor, but here the authors unfortunately give no details for the analogous interfaces in the human heterodimers studied. This omission deprives those in this field of the most useful information to be gleaned from the simulations presented. Are the interfaces (e.g., at the top of Figure 4A) similar to those seen in dEGFR? Do they involve conserved residues?

2) The “structural explanation for the preference of Her2 to partner with a ligand-bound EGFR or Her3, rather than with Her2 or ligand-free EGFR or Her3” is not really a result of this paper. Quite frankly, this was already clear from the Drosophila work. What the present (excellent) study does add to this, though, is the potential of a detailed view – yet the authors disappointingly describe no details that can be used for designing experiments. The brief discussion does not suffice and key areas of contact are omitted from Figure 6B. Are there key residues in the domain II interface in the asymmetric hEGFR dimer (outside the region shown in Figure 6B) that are well conserved? Can predictions be made for mutations that might selectively destabilize the asymmetric hEGFR dimer but not the symmetric 2-ligand dimer? These would be useful outcomes of the modeling studies and analysis of these questions are likely to yield valuable insight in and of itself.

3) Why are heterodimers formed between the EGFR and Her2 (or Her2 and Her3) ectodomains so much weaker than EGFR-EGFR ectodomain homodimers? This is a clear experimental result in the literature. In fact, EGFR-Her2 ectodomain heterodimers have not yet been directly observed, following ligand binding, although there are hints from biophysical studies that weak Her2-Her3 ectdomain dimers may form (this varies from study to study). By contrast, EGFR and dEGFR ectodomain dimers are strong (at least 50-fold stronger). The simulations might address the question of different dimerization strengths. By ignoring the well-established affinity differences – when taken at face value – the presentation in this work is a little misleading. For example, what do the authors mean by suggesting that the Her3-Her2 heterodimers are particularly robust? If they mean that the affinity of Her3 for Her2 is particularly strong, they are not correct – there is no evidence for this. Evidence for heterodimer formation is qualitative at best, and the only quantitative data show that EGFR-EGFR homodimers and Her4-Her4 homodimers are much “tighter” than any homodimer, at least where ectodomains are concerned. Analysis and description of the dimer interfaces could provide insight into this issue too.

4) Although this manuscript is well-written and beautifully illustrated, it is spoiled by its logical framework. For example, Figure 1B shows the symmetrical human EGFR (hEGFR) dimer. It also shows tethered and untethered forms of the monomer, but specifically does not address them. If these are not addressed, why illustrate them. The fact that Her2 without a ligand looks superficially like hEGFR with a ligand makes one want to assume that this is how Her2 works. Also, it should be made clearer (e.g., in the figure caption) which specific crystal structures of which domains and homo or heterodimers have been determined, along with their PDB IDs.

5) Figure 2A shows the symmetric Drosophila EGFR (dEGFR) dimer, the logical counter-part of the symmetric human EGFR dimer in Figure 1. It also shows the effect of a simulation on dEGFR without both its ligands. Figure 3 shows a simulation of hEGFR without one its ligands. It seems that both the human and Drosophila x-ray structures should be introduced together so as to emphasize their different symmetries.

6) The results of parallel simulations in both hEGFR and dEGFR need to be shown. This may require additional work as hEGFR has been simulated without one ligand whereas dEGFR has been simulated without both ligands.

7) The results of the MD simulations seem reproducible in that two independent several-micro-second simulations give similar results for this huge system with almost 300,000 atoms. This remarkable result could be emphasized more explicitly by comparison of the final structures of the respective pairs of simulations.
