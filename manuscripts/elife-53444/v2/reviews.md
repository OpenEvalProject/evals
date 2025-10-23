# Peer review - Round 1

Editors:
- Arun Radhakrishnan, University of Texas Southwestern Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53444.sa1](https://doi.org/10.7554/eLife.53444.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Water for sterol: an unusual mechanism of sterol egress from a StARkin domain" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

Your study examines the interesting and poorly-understood question of how a sterol-binding protein releases its bound sterol into a lipid bilayer. You provide several lines of evidence that the bound sterol is ejected from a sterol-binding STARkin protein domain by the penetration of water into the binding pocket. Your finding that the binding pocket accommodates the hydrophobic sterol as well as water is surprising and intriguing.

All the reviewers agreed that this study was thought-provoking and constituted a significant Research Advance. However, they also raised several concerns, addressing which would take more than the two-month revision window. The reviewers welcome assessment of a revised submission, but only if it addressed all the points raised in the full reviews listed below.

Reviewer #1:

This study by Khelashvili et al. follows up on two previous studies, one in eLife where ER proteins with sterol-binding StARkin domains were identified (2015) and a second in JBC where the structure of a yeast StARkin domain was determined (2018). Those previous studies did not yield mechanistic insights into how the StARkin domain delivered its bound sterol to the membrane. Here, the authors use molecular dynamics simulations to show that the ejection of the sterol into the membrane is preceded by penetration of water into the binding cavity – hence the "water for sterol" title. Since sterols are extremely hydrophobic, this is a surprising finding in that the binding pocket seems to accommodate the hydrophobic sterol as well as the complete opposite molecule on the hydrophobicity scale – water! The simulations identify a lysine residue (K89) that is important for modulating this egress step. This is an intriguing paper that could constitute an advance, but there are two main issues that need to be addressed.

1) This study focuses on the transfer of cholesterol from cholesterol-Lam4S2 complex to the membrane. The crystal structure in the Jentsch et al. paper shows sterol-bound Lam4S2, but the bound sterol is 25-hydroxycholesterol (25HC), not cholesterol (or ergosterol). The complex that is the starting point here replaces the bound 25HC with cholesterol. To fortify their starting point, the authors should show that bound 3H-25HC is competed away by unlabeled 25HC as well as cholesterol (or ergosterol). The authors report a sterol extraction assay with 3H-cholesterol in Figure 6D, so a binding assay seems possible to design to address this point. Alternatively, the simulations could be done with Lam4S2-ergosterol complexes, which may yield more robust results since it is the natural ligand, and is likely the sterol that is transported. I understand the authors want to make a general point about these StARkin domains, but the use of ergosterol instead of cholesterol would not dampen the provocative "water-for-sterol" ejection mechanism.

2) The elegant simulations indicate that the first step in sterol egress is widening of the side-entrance (microstate 2 and 3) to allow more water molecules into the binding pocket. Presumably, this only happens when the Lam4S2/sterol binds to or is close to a membrane? What in the membrane-bound state mediates this widening? In other words, why doesn't the widening and water penetration occur when the Lam4S2 is in solution?

Reviewer #2:

In their manuscript Menon and co-workers examine at the atomistic level how cholesterol exits the binding pocket of the Starkin domain of Lam4 (LAMS2), a recently discovered sterol transfer protein that functions in ER/PM contacts in yeast. By an impressive number of unbiaised MD simulations and elegant analyses by PCA, they reveal a mechanism by which water molecules enter via a fracture along the sterol-binding pocket to destabilize a key interaction between the 3-OH of sterol and Lam4S2. A triad of residues closing the top of this fracture is involved in the pace of this mechanism and plays a substantial role in stabilizing sterol in Lam4. Overall the work is very interesting mostly due to the in silico approaches. Indeed we see sterol egress in a non-steered MD and its entry in a bilayer. Yet it is difficult in the second-part of the manuscript to apprehend to what degree the water-mediated mechanism of sterol exit is supported by in vivo/in vitro experiments. Rather, experimental data suggest that a point mutation of a residue K89, found in simulation to limit sterol stability, renders Lam4 inactive but is this sufficient to validate the occurrence of the water-mediated mechanism? I think the manuscript deserves to be published in eLife but with more experimental data to buttress the MD simulations.

- Stage 1 simulations identify two poses for LamS2 on a bilayer: one seems impossible due to steric constraints imposed by the N and C regions around the Starkin domain whilst the second one seems compatible. Functional assays suggest that a few residues found to insert in the membrane by MD are indeed key for membrane recognition. However, this does not tell that the selected orientation of Lam4S2 in MD is the genuine one. Authors should provide evidences on this as this orientation is the starting point for the analysis of sterol exit, thus of the rest of the study.

- There is somehow a gap between MD and functional assays as there is no structural analysis in between. Indeed, there is no direct experiments to measure the accessibility of the binding pocket to water molecules in the presence/absence of the ligand and/or mutation – possibly, H-D exchange experiments by NMR using D2O could be useful in that respect. Also there is no assay to quantitatively measure the stability of sterol in Lam4S2 at equilibrium and/or its release in membrane. Osh3 and Osh4 were found to load DHE by measuring energy transfer between W residues, surrounding the pocket, and DHE (Tong et al., Structure. 2013, 21(7):1203-13; De Saint-Jean et a, J Cell Biol. 2011;195(6):965-78.). Offloading of DHE into membrane can be measured also by FRET in lipidic vesicles in real time. Authors should try such approaches that could more directly support MD simulations. Last they might use transport rates inferred from DHE transport assays with Lam4S2 to estimate an energy barrier for sterol extraction by the protein instead of quoting Dittman and Menon, 2017.

- Authors should check at least that single-mutation K89A or S181A does not affect the membrane-binding ability of Lam4S2

- it is quite surprising that 2 mutants out of 3 are not defective in yeast. In particular the D61A mutant do not phenocopy the K89A mutant, which is unexpected considering the existence of a electrostatic interaction with K89 and its central position in the triad of residues, making also contact with S181. Is there any explanation for this ?

Reviewer #3:

The mechanism of cholesterol release from endoplasmic reticulum domains that possess sterol-binding domains was studied. A computer model of the protein was derived from recently published crystallographic and spectroscopic structural data. Simulations have been well executed. Appropriate literature regarding previous evidence has been cited. The mildly steered molecular simulations provide deeper insight into the process of cholesterol release as well as its energetics. It highlights the role of water molecules in release of cholesterol from the binding domain. Conclusions are strengthened by studying the influence of alanine mutations on cholesterol binding and release both experimentally and in simulations. The paper is informative and very well written.

I suggest addressing the following question in more detail: Sterol molecules are amphipathic. The binding pocket for sterols must accommodate both polar and hydrophobic regions of cholesterol. How does the binding pocket deal with water influx into hydrophobic areas of the binding pocket? Is there evidence for structural changes in the protein to reduce energetically unfavorable interactions?
