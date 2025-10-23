# Peer review - Round 1

Editors:
- Amy J Wagers, Harvard University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.19130.018](https://doi.org/10.7554/eLife.19130.018)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Cell culture-based profiling across mammals reveals DNA repair and metabolism as determinants of species longevity" for consideration by eLife. Your article has been favorably evaluated by Janet Rossant as the Senior Editor and three reviewers, one of whom is a member of our Board of Reviewing Editors. The following individuals involved in review of your submission have agreed to reveal their identity: Daniel Promislow (Reviewer #2) and Yousin Suh (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript by Gladyshev and colleagues seeks to correlate gene expression and metabolite signatures in cultured fibroblasts from 16 different mammals with longevity phenotypes of the respective mammals, including maximal lifespan, body size, female time to maturity, and stress resistance. Using RNAseq and mass spec, the authors show that the constructed gene expression profiles reflect phylogenetic relationships, and identify subsets of genes and metabolites that correlate, positively or negatively, with multiple longevity traits (but not necessarily body size). The study presents a massive amount of work, particularly in compiling the various datasets and developing the informatics pipelines to specify species-specific ortholog sets and assess the robustness of the results, which will certainly be of interest to the community of researchers studying the biology of aging. All three reviewers agreed that the study provides interesting insights into aging and longevity, and should be of broad interest. However, as detailed below, a number of concerns were also raised, relating in large part to insufficient clarity in the current version with respect to the authors' methods and the limitations of their approach and data.

Essential revisions:

1) As this fibroblast culture system is the cornerstone of the authors' approach, it is essential that they provide clear and complete details regarding the experimental strategies used to isolate and culture these cells. In particular, detailed answers to the following key questions must be available in the present manuscript:

A) What age and sex were the animals from which the fibroblasts were isolated (e.g., was% max lifespan of donor animals matched for the different species? Were they sex-matched?)?

B) From what region of the body were fibroblasts isolated? This is important since other studies have shown that fibroblasts retain a regional gene expression program (e.g., hox patterning) after isolation.

C) What is the media system used, and strategy for cell passaging? How were these culture conditions chosen, and how can it be determined if they are optimal for all species (e.g., the authors recently published on a specific sensitivity to oxygen tension for fibroblasts from lab mice, but not other rodent species). This information should be very clearly articulated and discussed in the manuscript text itself, since it forms the basis for the experimental system used.

D) At what passage number were gene expression and metabolite profiles generated?

E) What is the in vitro proliferation rate of the different fibroblast isolates, and does this correlate with any of the gene expression profiles or longevity traits analyzed?

2) It should also be discussed that in vitro cell culture conditions dramatically change chromatin architecture (Zhu et al., Cell 2013), and so gene expression patterns. The gene expression signature detected may simply reflect the ability of cells to differentially adjust to the in vitro conditions, and may contribute to the multiplex stress resistance. This caveat should be discussed in the text.

3) It is not clear whether the common 9,389 gene orthologs that were reliably detected across the 15 species are comparable to the number of expressed genes detected by RNA-seq in fibroblasts in the 5 species with annotated genomes. The base line information on how many transcripts are detected in the 5 species should be available as they may provide a way to estimate the number of potentially missing orthologs, due to sequence divergence, some of which may be critical contributors to longevity through drastic functional alterations of gene products. The text should be clarified to address this point.

4) It is not clear what the baseline gene set was for the enrichment analysis of the 827 top hits (Figure 3D). Was it 9,389 genes or whole gene sets? And if the latter, which species? The data should be presented to show the enriched pathways in the top hits using the whole gene sets vs. 9,389 genes as baseline. This is because if DNA repair pathways are already enriched among the 9,389 genes, the conclusion that it is a longevity-associated molecular signature can be misleading. It is formerly possible that genes in these ancient pathways (such as DNA repair or glucose metabolism) may be more conserved sequence-wise and therefore more enriched among the orthologs, and thus among top hits. The text and data presentation should be clarified to address this point.

5) Subsection “Longevity trait variation across mammal”. The authors need to provide more information on how they calculated residuals from body mass. The reference to Ma et al. 2015b gives allometric equations, but no information is provided regarding where those equations come from. The description in Ma et al. (residual LS = LS/(a x Massb)) implies that residuals were taken from a least-squares regression of log(LS) vs. log(Mass) with an intercept of log(a) and a slope of b. But this is not mentioned in the present manuscript, and must be inferred from the Ma et al. manuscript. If a least-squares regression approach was used, one important assumption is that the residuals are normally distributed. The data for Figure 1 (MLres and FTMres) do not look normally distributed. If they are not, a general linear model with an appropriate link function must be applied.

6) The authors use maximum lifespan as a metric of aging, and thus should add to the text of their manuscript a discussion of the concerns that have been raised regarding this statistic (e.g. Moorad et al. 2012 Aging Cell). In particular, it does not provide a measure of aging per se, is quite sensitive to small sample size, and is not in itself under direct selection.

7) Analyses of primate and bird species (subsection “Validation of amino acid patterns in primate and bird fibroblasts”) does not appear to be size corrected. Numerous studies have shown strong size effects of life span not only in primates, but also in birds. Therefore, size effects should be addressed here as well.

8) Subsection “Evaluation of amino acid levels in bird and primate fibroblast cell lines”. For the bird/primate analysis, the authors state, "when two or more […] features were annotated as corresponding to the same amino acid, we tabulated the degree of association from the feature most strongly correlated with lifespan among the species studied." This approach will necessarily bias the result in favor of suggesting a stronger relationship between lifespan and metabolite levels than might be true, and this caveat must be mentioned.
