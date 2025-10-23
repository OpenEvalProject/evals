# Peer review - Round 1

Editors:
- Heedeok Hong, Michigan State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66662.sa1](https://doi.org/10.7554/eLife.66662.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This is a wonderful study that advances our understanding of GPCR oligomerization and provides new physical insights into GPCR-mediated cellular signaling.

Decision letter after peer review:

Thank you for submitting your article "Oligomerization of the Human Adenosine A2A Receptor Is Driven by the Intrinsically Disordered C-Terminus" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Heedeok Hong as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Olga Boudker as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Antonella Di Pizio (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. On the rigor and validity of size-exclusion chromatography (SEC)

(1a) Justifying the peak assignment in the SEC data as monomer, dimer and HMW oligomers (Figure 1 and Figure S1):

While the UV signals on the SEC profiles suggest the existence of well-resolved peaks of oligomers, dimers and monomers, the SDS-PAGE and Western blotting results that were carried out in a denaturing environment (SDS) predominantly display monomers in the "dimer" and "HMW" fractions. An alternative method may be needed to verify the assignment (e.g., crosslinking, an assignment based on the standard curve-i.e., mobility vs MW standard, analytical ultracentrifuge, native gel, etc.).

(1b) Ensuring that oligomer distributions are thermodynamic products:

The clarification of this point seems necessary to support the conclusion that multiple types of molecular forces serve as "driving forces" in oligomerization. Probably, it would be helpful to rerun SEC for the fractions of each major peak (possibly C394X mutants) and investigate the dependence of oligomer distribution on protein and detergent concentrations, the presence of deca-His tag and the length of storage. It would also be important to confirm that "UV in arbitrary units" scales with the protein concentration in the fractions.

(1c) Strengthening the rigor of statistical analysis:

Reported experimental uncertainties of content of oligomerized receptor fractions are solely based on reproducibility of fits of a single elution profile. It may underestimate experimental error limits. How reproducible are results when chromatographic experiments are repeated using the same protein stock?

2. Verifying the influence of mutation and C-terminal truncation on ligand binding capability.

3. Providing further details and additional analysis of MD simulation.

(3a) More detailed descriptions for initial modeling and its evaluation procedures (please see Reviewer 3's comments). For example, which was(were) template(s) used for the modelling of the initial state and how was the reliability of the model evaluated?

(3b) Please, address reviewers' concerns about how the system equilibration was ensured (simulation sufficiently long or repeated sufficiently with a variation of initial conditions to yield results that are not biased by initial conditions) and report time-dependent RMSDs that can provide the information on the equilibration and dynamics of the system.

(3c) Additional analysis will help further strengthening the conclusion: (i) statistical analysis of properties of interaction sites between neighbored molecules; (ii) the role of protein segments other than the C-terminus for oligomerization; (iii) statistical analysis of intra- and intermolecular "nonpolar" contacts to support authors' claim that the hydrophobic interaction is one of the key driving forces in oligomerization.

4. Clarifying the putative disulfide bridge involving C394.

It would be useful to provide a list of Cys residues that potentially can interact with Cys394 and discuss the validity of authors' claim on the formation of putative disulfide bridge.

5. Addressing additional major scientific concerns from reviewers:

(5a) Is the result obtained in micelles relevant in the lipid bilayer or cellular context?

(5b) What is the basis of claiming the "cooperativity" in the C-terminal domain interactions?

6. Please, address reviewers' major concerns that have been brought up (see below) but not listed above.

Reviewer #1 (Recommendations for the authors):

I have several suggestions that may help.

1. How relevant is the peak assignment in the SEC data as monomer, dimer and HMW oligomers (Figure 1)?

Although the assignment is supported by SDS-PAGE and Western blotting (Figure S1), SDS provides a denaturing environment. As seen in the data (Figure S1), the proteins in the "dimer" and "HMW" fractions on SEC dominantly migrate as monomers on SDS-PAGE, which indicates that SDS destabilizes oligomers or, if not, each peak contains a significant portion of monomer. An alternative method may be needed to verify the assignment (for example, crosslinking, an assignment based on the standard curve- mobility vs MW standards, analytical ultracentrifuge or native gel).

2. Ensuring that the oligomer distributions are thermodynamic products.

Probably, it might be helpful to rerun SEC with the fractions of each major peak (possibly C394X mutants) and see if the redistribution of oligomeric states occurs.

3. On the contribution of the hydrophobic interactions to oligomerization.

(3a) Since it has been suggested that the hydrophobic effect is one of the key driving forces for oligomerization, it would be informative to (3a-i) show the fraction of nonpolar residues in the C-term tail and (3a-ii) analyze the number of nonpolar contacts during CGMD simulations

(3b) What are the RMSDs of the IDRs during simulation? This analysis will be highly informative with regards to the equilibration of the system, the dynamics of the IDR, and the effect of truncation on the dynamics.

Reviewer #2 (Recommendations for the authors):

I am concerned about inconsistencies between UV absorbance and Western Blot analysis of eluted fractions in Figure S1B. While the UV signal suggests existence of well-resolved peaks of oligomers, dimers and monomers, the Western blots show high concentration of monomers underneath the dimer peak. What is the cause for this discrepancy? What are the protein concentration applied to the column and concentrations in the eluted fractions? Does aggregation behavior depend on protein concentration, detergent concentration, temperature, length of storage? Did the protein denature partially on the column? Did the authors repeat experiments on concentrated eluted fractions? Could it be that baseline correction of UV absorbance obscured a broad peak of monomer elution?

The use of the term "UV in arbitrary units" when reporting ratios of protein in oligo-, di- and monomers is ambiguous. Does protein concentration in the fractions scale with integral intensity of UV absorbance traces? If yes, the ratios would faithfully report relative differences in protein content of those fractions.

Reported experimental uncertainties of content of oligomerized receptor fractions are solely based on reproducibility of fits of a single elution profile. It yields experimental error limits that are rather low. How reproducible are results when chromatographic experiments are repeated using the same protein stock?

The authors report evidence for disulfide bond formation between neighbored molecules at C394. The level of disulfide bond formation is known to depend on cofactors including protein concentration, oxygen exposure, pH, the presence of oxidizing or reducing agents, temperature, time, etc. Were those variables controlled?

Does the deca-His tag influence oligomerization of the protein?

Does truncation of the receptor influence its function? Did the authors observe differences in ligand binding affinity and G protein activation rates for truncated/mutated receptor? Does protein truncation influence expression yield? Does truncation influence thermal stability of the expressed protein? Are eluted protein fractions obtained by size exclusion chromatography ligand binding- and G protein activation competent?

Experimental results are accompanied by an impressive set of molecular simulations. Were simulations sufficiently long or repeated sufficiently often with variation of initial conditions to yield results that are not biased by initial conditions? Would it be possible to conduct a statistical analysis of properties of interaction sites between neighbored molecules? What is the role of protein segments other than the C-terminus for aggregation?

Reviewer #3 (Recommendations for the authors):

1. The putative disulfide bridge involving C394 should be further investigated.

– In light of the suggested C-terminus/C-terminus interaction in absence of the TM domain, the Cys partner might be in the C-terminus. It would be useful to provide a list of Cys residue that potentially can interact with Cys394 and experimentally validate these hypotheses

– The discussion in lines 338-391 should be extended accordingly: 'A previous study showed that residue C394 in A2AR dimer is available for nitroxide spin labelling(Schonenbach et al. 2016), suggesting that some of these disulfide bonds may be between 390 residue C394 and another cysteine in the hydrophobic core of A2AR that do not form intramolecular disulfide bonds(De Filippo et al. 2016; Naranjo et al. 2015; O'Malley et al. 2010)'

– Moreover, in some parts of the manuscript the putative disulfide bridge is ignored, es: Lines 86-87: 'a model GPCR that could engage in diverse non-covalent interactions, such as electrostatic interactions, hydrogen bonds, or hydrophobic interactions. These non covalent interactions are readily tunable by external factors', Lines 291-293: 'The variable 13 291 nature of A2AR oligomeric interfaces suggests that the main driving forces must be non-covalent interactions, such as electrostatic interactions and hydrogen bonds as identified by the above MD simulations'

2. MD simulations

The C-terminus is not present in any of the A2AR crystal structures and is very long (Lines 104-105: A striking example is A2AR, a model GPCR with a particularly long, 122-residue, C-terminus that is truncated in all published structural biology studies).

The C-terminus is therefore modelled, however, the only reference to the C-terminus modelling I could find is in Lines 594-595: 'missing residues added using MODELLER 9.23(Eswar et al. 2006)'. Which template(s) was(were) used for the modelling and which is the sequence similarity? The detailed modelling procedure and the computational evaluation should be provided.

Results of the MD are highly dependent of the input model. Moreover, the information about the disulfide bridge is not incorporated in the models but this is an important structural feature to be considered.

Also, the conclusions about the role of the ERR motif are based on the modelling, but we do not have information to judge the modelling.

Lines 409-410: 'This observation is supported by our experimental results showing that substituting this charged cluster with alanines reduces the total A2AR oligomer levels' – the experimental results suggest the involvement of these residues on the oligomerization process, but do not say a lot about the molecular mechanisms – localizing these residues far from the interacting surface and the intramolecular interactions are hypotheses based on the modelling.

3. The impact of findings is weakly stated, some related sentences in the paper are very general:

– Line 38 in the abstract: 'offering important guidance for structure-function studies of A2AR and other GPCRs'

– Lines 55-56: 'it is crucial to identify the driving factors that govern the oligomerization of GPCRs, such that the properties of GPCR oligomers can be understood'

– Lines 473-475: 'In that context, this study offers valuable insights and approaches to tune the oligomerization of A2AR and potentially of other GPCRs using its intrinsically disordered C-terminus'

4. I suggest labeling TM residues with BW numbering, so it will be easier to distinguish between TM residues and C-terminus residues in the figures and the text.

5. Title: 'homo-oligomerization' should replace 'oligomerization'
