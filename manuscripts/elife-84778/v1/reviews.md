# Peer review - Round 1

Editors:
- Arturo Casadevall, Johns Hopkins Bloomberg School of Public Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84778.sa0](https://doi.org/10.7554/eLife.84778.sa0)

This paper describes a new method to investigate Staphylococcus aureus intracellular virulence that has produced important insights into the mechanisms of staphylococcal pathogenesis. The results are convincing and the methodology is state-of-the-art. The authors have responded to the reviewer comments and resolved the issues identified during the review. This paper will be of interest to scientists studying microbial intracellular pathogenesis and cell biology.


---

# Peer review - Round 1

Editors:
- Arturo Casadevall, Johns Hopkins Bloomberg School of Public Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84778.sa1](https://doi.org/10.7554/eLife.84778.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A high-throughput cytotoxicity screening platform reveals agr-independent mutations in bacteraemia-associated Staphylococcus aureus that promote intracellular persistence" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Arturo Casadevall as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Matthew Culyba (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Reviewer #1 (Recommendations for the authors):

Consider depositing the long read sequence of the HeLa strain, or at least chromosome mapping/ structure variant mapping. These could be important when other investigators attempt to reproduce results using their version of the cell line.

Line 145 – What specifically is "very low intra assay variation"?

Line 283 – Unclear if these are the only 28 pairs that met the criterion, or if there were others but that weren't selected.

Line 290 – Were homoplasic mutations in these loci found between other pairs of strains (ie where there were no significant differences)

Line 324-328 – This correlation between π AUC and intracellular bacterial titer should be shown as a scatterplot for clarity

Reviewer #2 (Recommendations for the authors):

1. The InToxSa assay was devised to reflect the toxicity of intracellular S. aureus, however, it is not made clear in the manuscript that the intracellular nature of this assay is actually an important feature that distinguishes it from what would be observed by testing the same strains in the equivalent extracellular toxicity assay. For example, the interpretation of the InToxSa versus Tryptan blue exclusion assay data was that InToxSa was more sensitive. However, two key variables differed in this comparison: (1) extracellular toxicity vs intracellular toxicity and (2) cell type used. Is InToxSa more sensitive in this comparison because of the intracellular nature of the assay, or because it employs HeLa cells instead of THP1 macrophages? Maybe HeLa cells are just more sensitive regardless? What would happen if you repeated the Tryptan blue exclusion assay with HeLa cells?

2. High throughput screening assays often report a 'reconfirmation rate' for the assay. This helps address day-to-day assay signal variation from the actual experimental samples (instead of controls). If you just rerun the 56 isolates that make up the 28 pairs from the convergence analysis, how well do the data replicate in terms of the difference in π uptake? I'm wondering how much of the low validation/confirmation rate with the NTLM and allelic exchange strains could be due to day-to-day assay noise in the primary screen. Maybe some of these 'hits' were simply false positives?

3. The analysis focuses on negative π difference values. What is the interpretation of a positive value for π differences? Higher toxicity? Were any of these identified by GWAS or the convergence analysis? Are these of biological interest?

4. I'm wondering how the authors envision others deploying this system to screen clinical isolates since the 'gene burden GWAS' only found agr, which is a well-described virulence locus. How many isolates would have to be screened and analyzed in this manner to find additional biologically relevant mutant alleles? The statistical power of this approach is related to the number of isolates (N), their genetic relatedness, the magnitude of the effect size (in this case, π uptake signal), and the gene burden. A power analysis could be a useful way how to think about deploying this assay using the 'phenomics' approach. Would it be possible to model these parameters in the gene burden GWAS, and provide an estimate of the number of isolates (N) that would need to be screened using the assay to find mutant alleles as a function of their effect size (i.e. PI-uptake), gene burden, and the genetic relatedness of the sample population? Perhaps you will find that the assay is best deployed in settings where the strains being screened are all very closely genetically related (e.g. serial isolates from the same patient or transmission outbreak). Outside of these situations, I wonder if N might be too large for this to be a feasible approach to finding novel genes involved in intracellular toxicity. Modeling this as a power analysis would describe this quantitatively and likely point to the best types of clinical strain samples to pursue given the practical constraint that screening more than a few thousand isolates in this system would not be feasible. It seems you already took steps to enrich for serial isolates from the same patient and then the convergence analysis was even further enriched for these samples. These are clearly critical steps to get good information output. Modeling the statistical power of this would be a nice complement I think.

5. All of the 'hits' from the gene burden GWAS and convergence analyses were attempted to be validated using the corresponding strains from the NTML. This begs the question: why not just screen the entire NTML as a starting point? It seems this approach would have not only offered better validation for the utility of the assay but also provided maximal statistical power for genotype-phenotype correlations given the isogenic background within this strain library. With this in mind, can you elaborate further on your choice of approach?

6. The manuscript describes using HeLa cells as an in vitro model system for professional phagocytic cells that are thought to be important for S. aureus clearance in vivo. The biological relevance of the HeLa cell system would be further supported by also studying some mutants in a system that employs professional phagocytes to study intracellular S. aureus persistence. For example, it would be of interest to know if the ausA mutants have a persistence phenotype in a macrophage or not.

7. The statistical 'gene burden GWAS' procedure only identified agr as having a significant P-value. In contrast, a manual 'convergence' analysis and hunt for homoplastic mutations for π uptake seemed to identify additional plausible candidates, but this manual procedure was not supported by statistical analysis. Can you explain why the convergence analysis would find loci that the 'gene burden GWAS' failed to identify? Can the mutations identified by the convergence analysis be further supported within a formal statistical framework? In the 'convergence' analysis, you only consider pairs with <200 SNP differences, which effectively increases the chance (i.e. statistical power) that any given mutation could be responsible for the observed π uptake effect size. What would happen if you re-ran the 'gene burden GWAS' using only a subset of the more genetically related strain pairs? Would that increase sensitivity enough to identify the homoplastic mutations you found in the 'convergence' analysis?
