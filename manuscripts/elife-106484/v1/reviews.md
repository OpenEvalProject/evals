# Peer review - Round 1

Editors:
- Jungsan Sohn, Johns Hopkins University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.106484.3.sa0](https://doi.org/10.7554/eLife.106484.3.sa0)

This fundamental study demonstrates that lipid binding can regulate the dimerization state of the SARS-CoV2 Orf9b protein. The data from biophysical and cellular experiments along with mathematical modeling are compelling. This paper is broadly relevant to those studying coupled equilibria across all aspects of biology.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.106484.3.sa1](https://doi.org/10.7554/eLife.106484.3.sa1)

Summary:

Felipe and colleagues try to answer an important question in Sarbecovirus Orf9b-mediated interferon signaling suppression, given that this small viral protein adopts two distinct conformations, a dimeric β-sheet-rich fold and a helix-rich monomeric fold when bound by Tom70 protein. Two Orf9b structures determined by X-ray crystallography and Cryo-EM suggest an equilibrium between the two Orf9b conformations, and it is important to understand how this equilibrium relates to its functions. To answer these questions, the authors developed a series of ordinary differential equations (ODE) describing the Orf9b conformation equilibrium between homodimers and monomers binding to Tom70. They used SPR and a fluorescent polarization (FP) peptide displacement assay to identify parameters for the equilibrium and create a theoretical model. They then used the model to characterize the effect of lipid-binding and the effects of Orf9b mutations in homodimer stability, lipid binding, and dimer-monomer equilibrium. They used their model to further analyze dimerization, lipid binding, and Orf9b-Tom70 interactions for truncated Orf9b, Orf9b fusion mutant S53E (blocking Tom70 binding), and Orf9b from a set of Sars-CoV-2 VOCs. They evaluated the ability of different Orf9b variants for binding Tom70 using Co-IP experiments and assessed their activity in suppressing IFN signaling in cells.

Overall, this work is well designed, the results are of high quality and well-presented; the results support their conclusions.

Strengths:

(1) They developed a working biophysical model for analyzing Orf9b monomer-dimer equilibrium and Tom70 binding based on SPR and FP experiments; this is an important tool for future investigation.

(2) They prepared lipid-free Orf9b homodimer and determined its crystal structure.

(3) They designed and purified obligate Orf9b monomer, fused-dimer, etc., a very important Orf9b variant for further investigations.

(4) They identified the lipid bound by Orf9b homodimer using mass spectra data.

(5) They proposed a working model of Orf9b-Tom70 equilibrium.

Weaknesses:

(1) It is difficult to understand why the obligate Orf9b dimer has similar IFN inhibition activity as the WT protein and obligate Orf9b monomer truncations.

(2) The role of Orf9b homodimer and the role of Orf9b-bound lipid in virus infection, remains unknown.

Comments on revisions:

In the revised manuscript, the authors have addressed my concerns.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.106484.3.sa2](https://doi.org/10.7554/eLife.106484.3.sa2)

Summary:

This study focuses on Orf9b, a SARS-COV1/2 protein that regulates innate signaling through interaction with Tom70. San Felipe et al use a combination of biophysical methods to characterize the coupling between lipid-binding, dimerization, conformational change, and protein-protein-interaction equilibria for the Orf9b-Tom70 system. Their analysis provides a detailed explanation for previous observations of Orf9b function. In a cellular context, they find other factors may also be important for the biological functioning of Orf9b.

Strengths:

San Felipe et al elegantly combine structural biology, biophysics, kinetic modelling, and cellular assays, allowing detailed analysis of the Orf9b-Tom70 system. Such complex systems involving coupled equilibria are prevalent in various aspects of biology, and a quantitative description of them, while challenging, provides a detailed understanding and prediction of biological outcomes. Using SPR to guide initial estimates of the rate constants for solution measurements is an interesting approach.

Weaknesses:

This study would benefit from a more quantitative description of uncertainties in the numerous rate constants of the models, either through a detailed presentation of the sensitivity analysis or another approach such as MCMC. Quantitative uncertainty analysis, such as MCMC is not trivial for ODEs, particularly when they involve many parameters and are to be fitted to numerous data points, as is the case for this study. The authors use sensitivity analysis as an alternative, however, the results of the sensitivity analysis are not presented in detail, and I believe the authors should consider whether there is a way to present this analysis more quantitatively. For example, could the residuals for each +/-10% parameter change for the peptide model be presented as a supplementary figure, and similarly for the more complex models? Further details of the range of rate constants tested would be useful, particularly for the ka and kB parameters.

The authors build a model that incorporates an α-helix-β-sheet conformational change, but the rate constant for the conversion to the α-helix conformation is required to be second order. Although the authors provide some rationale, I do not find this satisfactorily convincing given the large number of adjustable parameters in the model and the use of manual model fitting. The authors should discuss whether there is any precedence for second-order rate constants for conformational changes in the literature. On page 14, the authors state this rate constant "had to be non-linear in the monomer β-sheet concentration" - how many other models did the authors explore? For example, would αT↔α↔αα↔ββ (i.e., conformational change before dimer dissociation) or α↔βαT↔ββ (i.e., Tom70 binding driving dimer dissociation) be other plausible models for the conformational change that do not require assumptions of second-order rate constants for the conformational change?

Overall, this study progresses the analysis of coupled equilibria and provides insights into Orf9b function.

Comments on revisions:

The authors have done a satisfactory job addressing my concerns.

Regarding my recommendations to the authors - point 7: "Orf9b-FITC:Tom70" and "PT", representing the same species, are still both used in the equations on page 14, which is confusing for anyone who may wish to re-use the model. I appreciate this is quite a subtle point but given the importance of the model for the manuscript I feel the authors should do their due diligence to ensure it is presented as clearly as possible.
