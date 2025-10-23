# Peer review - Round 1

Editors:
- Armita Nourmohammad, University of Washington United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.104934.3.sa0](https://doi.org/10.7554/eLife.104934.3.sa0)

This useful manuscript provides a newly curated database (termed AACDB) of antibody-antigens structural information, alongside annotations that are either taken and from the PDB, or added de-novo. Sequences, structures, and annotations can be easily downloaded from the AACDB website, speeding up the development of structure-based algorithms and analysis pipelines to characterize antibody-antigen interactions. The methodology presented for this data curation is solid. The curated dataset will be of broad interest and value to researchers interested in antibody-antigen interactions.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.104934.3.sa1](https://doi.org/10.7554/eLife.104934.3.sa1)

This work introduces and describes a useful curation pipeline of antibody-antigen structures downloaded from the PDB database. The antibody-antigen structures are presented in a new database called AACDB - with associated website - alongside annotations that were either corrected from those present in the PDB database, or added de-novo with solid methodology. Sequences, structures and annotations can be very easily downloaded from the AACDB website, speeding up the development of structure-based algorithms and analysis pipelines to characterize antibody-antigen interactions. However, AACDB is missing some important annotations that I believe would greatly enhance its usefulness, such as binding affinity annotations.

I think the potentially most significant contribution of this database is the manual data curation to fix errors present in the PDB entries, by cross-referencing with the literature. The authors also seem to describe, whenever possible, the procedures they took to correct the annotations.

I have personally verified some of the examples presented by the authors, and found that SAbDab appears to fix the mistakes related to mis-identification of antibody chains, but not other annotations.

"(1) the species of the antibody in 7WRL was incorrectly labeled as "SARS coronavirus B012" in both PDB and SabDab" → I have verified the mistake and fix, and that SAbDab does not fix is, just uses the pdb annotation.

"(2) 1NSN, the resolution should be 2.9 , but it was incorrectly labeled as 2.8" → I have verified the mistake and fix, and that saabdab does not fix it, just uses the PDB annotation.

"(3) mislabeling of antibody chains as other proteins (e.g. in 3KS0, the light chain of B2B4 antibody was misnamed as heme domain of flavocytochrome b2)" → SAbDab fixes this as well in this case.

"(4) misidentification of heavy chains as light chains (e.g. both two chains of antibody were labeled as light chain in 5EBW)" → SAbDab fixes this as well in this case.

I believe the splitting of the pdb files is a valuable contribution as it standardizes the distribution of antibody-antigen complexes. Indeed, there is great heterogeneity in how many copies of the same structure are present in the structure uploaded to the PDB, generating potential artifacts for machine learning applications to pick up on. That being said, I have two thoughts both for the authors and the broader community. First, in the case of multiple antibodies binding to different epitopes on the same antigen, one should not ignore the potentially stabilizing effect that the binding of one antibody has on the complex, thereby enabling the binding of the second antibody. In general, I urge the community to think about what is the most appropriate spatial context to consider when modeling the stability of interactions from crystal structure data. Second, and in a similar vein, some antigens occur naturally as homomultimers - e.g. influenza hemagglutinin is a homotrimer. Therefore, to analyze the stability of a full-antigen-antibody structure, I believe it would be necessary to consider the full homo-trimer, whereas in the current curation of AACDB with the proposed data splitting, only the monomers are present.

I think the annotation of interface residues is a very useful addition to structural datasets.

I am, however, not convinced of the utility of *change* in SASA as a useful metric for identifying interacting residues, beyond what is already identified via pairwise distances between the antibody and antigen residues. If we had access to the unbound conformation of most antibodies and antigens, then we could analyze the differences in structural conformations upon binding, which can be in part quantified by change in SASA. However, as only bound structures are usually available, one is usually force to approximate a protein's unbound structure by computationally removing its binding partner - as it seems to me the authors of this work are doing.

Some obvious limitations of AACDB in its current form include:

AACDB only contains entries with protein-based antigens of at most 50 amino-acids in length. This excludes non-protein-based antigens, such as carbohydrate- and nucleotide-based, as well as short peptide antigens https://www.biorxiv.org/content/10.1101/2023.12.10.570461v1.

AACDB does not include annotations of binding affinity, which are present in SAbDab and have been proven useful both for characterizing drivers of antibody-antigen interactions (cite https://www.sciencedirect.com/science/article/pii/S0969212624004362?via%3Dihub) and for benchmarking antigen-specific antibody-design algorithms cite.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.104934.3.sa2](https://doi.org/10.7554/eLife.104934.3.sa2)

Summary:

Antibodies, thanks to their high binding affinity and specificity to cognate protein targets, are increasingly used as research and therapeutic tools. In this work, Zhou et al. have created, curated and made publicly available a new database of antibody-antigen complexes to support research in the field of antibody modelling, development and engineering.

Strengths:

The authors have performed a manual curation of antibody-antigen complexes from the Protein Data Bank, rectifying annotation errors; they have added two methods to estimate paratope-epitope interfaces; they have produced a web interface capable of effective visualisation and of summarising the key useful information in one page. The database is also cross-linked to other databases that contain information relevant to antibody developability and therapeutic applications.

Weaknesses:

The database does not import all the experimental information from PDB and contains only complexes with large protein targets.

Comments on revisions: I thank the authors for having incorporated my feedback and I look forward to the next releases of this database.
