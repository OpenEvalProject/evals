# Peer review - Round 1

Editors:
- M Joanne Lemieux, https://ror.org/0160cpw27 University of Alberta Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76090.sa0](https://doi.org/10.7554/eLife.76090.sa0)

This work provides a strong contribution to our understanding of intramembrane proteolysis and in particular the subtle structural but significant influence of the lipid bilayer on proteolytic activity and coordination of the active site geometry.


---

# Peer review - Round 1

Editors:
- M Joanne Lemieux, https://ror.org/0160cpw27 University of Alberta Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76090.sa1](https://doi.org/10.7554/eLife.76090.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Active site geometry stabilization of a presenilin homolog by the lipid bilayer promotes intramembrane proteolysis" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Joanne Lemieux as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Michael S. Wolfe (Reviewer #3).

Our decision has been reached after a consultation among editors and reviewers. Based on these discussions and the individual reviews below, we regret to inform you that eLife will not be considering this submission for publication. We recognize the importance of this work and the progress made towards a better understanding of the factors that influence intramembrane proteolysis. Indeed, the reviewers' evaluation of the experimental work was positive overall. However, the reviewers also identified critical problems in the computational component. Although it seems possible to address these problems, it also seems that the revision would exceed the two-month period that is typically allowed. Hence, we believe the appropriate action is to reject the current version of your manuscript and allow you to consider your options. Should you decide to address all the concerns raised by the reviewers, we would be willing to examine a new version of your manuscript – but please note it would be considered a new submission, and therefore, that it might not be sent for review or be evaluated by the same reviewers.

Reviewer #1:

The activity of the archeal presenilin homolog (PSH) is assessed using a portion of the amyloid precursor substrate C99 substrate in DDM detergent and also in a POPC liposome environment. Mass spectrometry was used to precise indicate cleavage species as well as SDS. The results clearly show lipid influence both the rate of cleavage and the species generates. Modelling was used to determine structures of the PSH with the substrate in both app and holo forms. Similar to the cryoEM structures of PS with Notch and APP, a hybrid enzyme-substrate beta-sheet is observed between substrate and active site, suggesting a valid model for MD situations. These were used in MD simulations in both detergent and lipid environments. Importantly protonation states were analyzed for this Aspartyl protease, in which the two Asp residues were evaluated independently. D220 was determined to be the protonated Asp with D162 left charged in the simulations in different environments. The MD simulations show there were less structural changes in the DOPC embedded protein compared to the non-lipid sample, with a notable shift in TMD6a only in the DDM sample . MD simulations support the above experimentally observations that the lipid stabilize the E-S complex.

Overall this is an interesting paper that combines both experimental and structural studies to rationale differences in membrane environment and protease activity.

Reviewer #2:

I have several comments and suggestions for the authors to consider improving the quality of the paper:

1. Utilization of C100 for enzymatic analysis.

Authors utilized the recombinant C100-His6 as a substrate for the enzymatic assay. In contrast, they modeled the complex structure of PSH with C83, as the template cryo-EM structure was PS1-C83 complex. Essentially γ-secretase cleaves several substrates regardless the sequence. However, N-terminal length of the substrate might affect the proteolytic efficacy of the γ-secretase. In fact, Funamoto et al. (Nat Commun 2013) reported that AICD production from C83-FLAG was much greater than that from C99-FLAG (i.e., distinct Km and Vmax values). These data suggest the possibility that the formation of E-S complex is regulated by the N-terminal length of the substrate in the proteolytic mechanism of the γ-secretase. Thus, I would recommend the authors to compare the cleavage and trimming patterns of C83 by PSH in either DDM or POPC, as shown in the modeling analysis and the MD simulation. Such comparison strengthens the author's conclusion that the stabilization of E-S complex is critical to the intramembrane proteolysis.

2. Importance of TMD6a and hybrid β-sheet in the proteolysis by PSH.

Modeled structure of PSH-C83 strongly implicates the importance of these two structural elements in the proteolysis of PSH. However, it remains unclear whether these elements are truly required for the proteolytic activity of PSH. The possibility that these structures artificially modeled because the authors used the γ-secretase-C83 structure as a template. Thus, authors should test the proteolytic activity of mutant PSH that carries amino acid substitutions in TMD6a or beta2-strand to abolish the interaction with the substrate.

3. Figure presentation

In figure 5A, it is difficult to understand the difference of TMD6a conformation in DDM/POPC because of superimposed structure. They should be presented separately.

Reviewer #3:

In this manuscript, Feilen et al. combined biochemical experiments and molecular dynamics (MD) simulations to investigate the effects of detergent solubilization versus lipid vesicle reconstitution on intramembrane protease activity of an archaeal presenilin homolog (PSH). This PSH has been previously reported to process amyloid precursor (APP)-based substrate to amyloid β-peptides (A-β) in a manner closely similar to that accomplished by the presenilin-containing γ-secretase complex. The archaeal PSH is employed here as a surrogate to gain mechanistic insight into γ-secretase.

The authors showed that the carboxypeptidase-like activity of PSH is impaired in DDM micelles compared to a POPC lipid bilayer. Evidence is also provided suggesting that DDM-solubilized PSH binds more weakly to a transition-state analog inhibitor compared with POPC-bilayer PSH. Comparative MD simulations suggested that the lipid bilayer stabilized relevant structural elements of PSH for substrate binding (notably TMD6a) and formation of the enzyme active site geometry for proteolysis. A number of suggestions that could help improving the manuscript include the following:

1. While it is understood that archaeal PSH is taken as a surrogate for presenilin in the γ-secretase complex, the authors should explain why this is necessary. All the described experiments, including the MD simulations, could have been conducted with γ-secretase itself. In the discussion, the specific implications for γ-secretase (especially FAD mutations) should be de-emphasized and more emphasis put on the implications for intramembrane proteolysis in general.

2. For the MS analysis of A-β peptide products in Figure 1D, a table of observed vs. calculated m/z should be provided. Some of these peaks (A-β-43, -45, and -46) are quite weak. The same is true of AICD MS analysis in Figure 2D.

3. Given crystal structures of the PSH, is it more reasonable to preserve protein coordinates in these crystal structures, but only add the missing residues (e.g., TMD6a) using the PS1/γ-secretase cryo-EM structures as template? The Results section is vague about how the homology modeling of enzyme-substrate complex was generated; an additional sentence or two should be provided so the reader does not have to refer to the experimental section to answer this basic question.

4. Assuming pKa calculations depend on local geometry of the protonation site, the protein structure(s) used for the calculations need to be described clearly. Moreover, how do the residue pKa's depend on the protein structures (e..g, 4Y6K and 4HYG crystal structures of PSH, the apo and holo cryo-EM structures of PS1/γ-secretase, and simulation equilibrated protein structures in notably two different conformations with the D162-D220 distance centered around ~6.5 and ~8.2 Angstroms in Figure 6A).

5. It is unclear why the Amber force field was used in simulations of holo PSH with two different protonation states, but CHARMM36m in simulations of the apo and holo PSH in different membrane environments. It would help to evaluate the force field differences and potential effects by adding simulations using CHARMM36m to the holo PSH with different protonation states or simulations using Amber to the apo and holo PSH in different membrane environments.

6. In Figure 3A, what is the RMSD between the PSH homology model and its crystal structures?

7. In Figures 4C-4E, it would help to add error bars (standard deviations) to examine what differences are significant. The authors calculated RMSFs of PSH in the apo and holo forms to describe its stability in different lipid environments. It is better to show error bars (with total simulation times across different replicates) to describe RMSF differences in notably, the TMD6a, TMD4 and TM2-TM3 loop. There is a notable RMSF difference just beyond TMD6a, which should be mentioned and explained. In addition to RMSF, further simulation analysis such as comparison of the distances between the catalytic aspartate and scissile peptide bond in C83 could provide more insights.

8. In Figure 5A, it would help to quantitatively calculate and plot the helicity of TMD6a and/or secondary structures of residues in TMD6a as a function of simulation time and compare these quantities between the different simulated systems.

9. In Figure 5C-5D, the authors described that the DDM molecule can insert itself between TMD2 and TMD6 and intervenes intra- and intermolecular interactions and thus destabilize TMD6a. It would be better to have more explanation if these insertions are with just one lipid molecule or there are multiple molecules involved during different time frames of the simulations. In addition, it would be more convincing to see atomic detailed interaction between the DDM molecule and the protein, especially because DDM is a nonionic detergent. Moreover, it could help to calculate -SCD order parameters that are usually obtained from NMR experiments to measure orientational anisotropy of the C-H bonds lipid chains and quantify differences of the lipid orientations.

10. For Figure 6A, it would help to plot the D162-D220 distance vs. time in simulations of the different systems also. What are the corresponding distance values in the PSH crystal and PS1 cryo-EM structures? In addition to a main peak at ~6.5 Å distance, there seems another peak at ~8.2 Å distance between D162-D220; what is this conformational state?

11. In Figure 6B, there is substantial non-specific binding of the biotinylated Merck C to PSH in DDM; the parent inhibitor is essentially not competing, even at 20 microM. This makes the interpretation that specific binding is stronger in POPC vesicles less convincing. Some comment to this effect should be added to the Results section.

Reviewer #4:

Feilen et al. address an interesting mechanistic and biophysical question, namely the significance of the lipid environment for intramembrane enzymatic activity – through biochemical experiments and MD simulations. While the experimental component seems compelling, my opinion is that the structural/computational element is unsuitable for publication in eLife. It is well known that the construction of homology models relies on multiple arbitrary decisions, from the choice of template structure to the sequence alignments to the scoring function – which together imply a degree of inaccuracy that is simply unknown a priori. When a complex is modeled, the uncertainties accumulate. At the same time, MD simulations are, by design, highly sensitive to the details of the input structure. It follows, that systematic inaccuracies in the input model for an MD simulation might result in observations that have no mechanistic significance. At the level of an eLife publication, therefore, it is essential that the authors demonstrate that their conclusions are robust and independent from those built-in uncertainties. A possible way forward would be to carry out simulations of existing experimental structures that might be relevant (with or without minor modifications). Alternatively, or in addition, the authors could consider equally plausible but meaningfully different homology models, constructed on the basis of different assumptions. Either way, I do not believe the manuscript can move forward to publication without an extensive overhaul of the computational section (or its removal), so as to clearly ascertain the conclusions are indeed significant and robust.

A related issue pertains to the comparison of PC bilayers vs DDM micelles. The authors construct and examine one micelle system with a specific number of DDM molecules solubilizing the protein in a specific volume. This choice seems again arbitrary – or at least it is not explained. While the characteristics of lipid bilayer models in odellingn have been extensively studied and optimized (area per lipid, bending modulus, etc), I am unclear the same applies to DDM micelles. What are the observables that give the authors confidence that the structural and elastic properties of their micelle model are realistic? Given that the differences between the POPC and DDM simulations are ultimately modest, this comparative analysis needs to be much more systematic than it currently is to merit publication in eLife. As with the homology odelling, the question is whether different micelles or different DDM models would lead to alternative conclusions.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled “Active site geometry stabilization of a presenilin homolog by the lipid bilayer promotes intramembrane proteolysis” for further consideration by eLife. Your revised article has been evaluated by 3 reviewers, including Joanne Lemieux as the Reviewing Editor and reviewer #1 and overseen by José Faraldo-Gómez as Senior Editor.

Reviewers and editors agree that the manuscript has been improved but there are some remaining issues that need to be addressed, outlined below. While recognizing the merits of the work, all agree the authors at times overstate the novelty of their findings and that the narrative must be toned down on account of the published work in this area. Furthermore, the reviewers add some insight that could be brought into the discussion.

Reviewer #1:

The authors provide an exciting body of work to support the role of the lipid bilayer in stabilizing the coordination of active site residues. The PSH protein is a suitable model since it does not contain any co-factors and is an active protease on its own. The authors demonstrate that the lipid bilayer enhances processivity of PSH. The data is supported by in vitro cleavage assays in detergent and lipid vesicles. Furthermore, in this revised version there are MD analyses conducted of several apo- and substrate: protease complexes, which provide insight into the protease dynamics and interactions with substrates. The revisions add depth to the paper and is suitable for publication.

Reviewer #2:

Comments and suggestions that could improve the manuscripts are below:

1. In the case of the deletions/proline mutations in the hybrid β-sheet and the lysine mutations in TMD6a, I would have liked to see some type of experiment (DLS, SEC, etc.) to show that the mutations did not simply result in aggregated or misfolded protein. I find it troublesome that it is rare to see confirmation that point mutations to key residues did not completely disrupt protein folding, particularly when detergents are being used for solubilization.

2. It would be worthwhile to consider the possibility that the inhibitors partition into the DDM micelle in the detergent environment. This is a known phenomenon and could explain the poor inhibition of PSH by both L-685,458 and Merck C in the DDM environment, particularly if the DDM that was added to the POPC experiments was to aid in the solubilization of what I gather is a highly insoluble molecule. In general, more detail in the experimental section regarding the in vitro cleavage assay and affinity precipitations would be helpful.

3. The manuscript suggests that it is remarkable to see a rise in processivity when PSH is reconstituted in POPC membranes. In fact, highly inconsistent enzymatic activities (and structures!) have been observed for numerous enzymes in detergent vs. lipid bilayers (e.g. MsbA, MalFGK). It could be beneficial to consider these examples in the discussion and tone down the language, as it is not particularly surprising to see this sort of inconsistency in these different environments.

4. Both the in vitro and in silico experiments in the lipid environment were carried out in POPC, but PSH is an archaeal homologue. The lipids found in archaea are very different to other membranes, and while it may be outside the scope of this study to carry out the experiments in the natural PSH lipid environment (or not possible due to availability), it may be worthwhile running MD simulations a more representative environment, particularly because it well established that the identity of the annular lipids around an enzyme can significantly affect its activity.

5. Related to the above point, I realize that working with a single lipid simplifies things, but could or should the experiments in lipid bilayer not have been done in a brain lipid extract to more accurately recapitulate the environment of the enzyme that PSH is meant to be a surrogate for? Or as above, at the very least the MD simulations could have been done in a more representative environment.

Reviewer #3:

The manuscript by Feilen et al. underwent significant revisions and addressed the reviewer's concerns adequately. The manuscript focuses on the importance of the lipid environment for intramembrane proteolysis. Before I list a number of only smaller suggestions for this manuscript, I would like to mention that while I fully understand that this is beyond the scope of the present manuscript, it would have been interesting if the authors could have enforced the aspect of direct lipid-enzyme interactions, about which very little is known. For example, could the authors deduce amino acids in PSH that are important for the interaction with POPC molecules, and mutate those? Or is the stabilizing effect of POPC solely conveyed through the self-ordering of membrane molecules?
