# Author response - Round 1

Authors:
- Carla de la Fuente
- Alexandre Grondin ([ORCID: 0000-0001-6726-6274](https://orcid.org/0000-0001-6726-6274))
- Bassirou Sine
- Marilyne Debieu
- Christophe Belin ([ORCID: 0000-0003-2129-5349](https://orcid.org/0000-0003-2129-5349))
- Amir Hajjarpoor
- Jonathan A Atkinson
- Sixtine Passot
- Marine Salson
- Julie Orjuela ([ORCID: 0000-0001-8387-2266](https://orcid.org/0000-0001-8387-2266))
- Christine Tranchant-Dubreuil
- Jean-Rémy Brossier
- Maxime Steffen
- Charlotte Morgado
- Hang Ngan Dinh
- Bipin K Pandey ([ORCID: 0000-0002-9614-1347](https://orcid.org/0000-0002-9614-1347))
- Julie Darmau
- Antony Champion
- Anne-Sophie Petitot
- Celia Barrachina
- Marine Pratlong
- Thibault Mounier
- Princia Nakombo-Gbassault
- Pascal Gantet ([ORCID: 0000-0003-1314-0187](https://orcid.org/0000-0003-1314-0187))
- Prakash Gangashetty
- Yann Guedon
- Vincent Vadez
- Jean-Philippe Reichheld
- Malcolm J Bennett
- Ndjido Ardo Kane ([ORCID: 0000-0002-1879-019X](https://orcid.org/0000-0002-1879-019X))
- Soazig Guyomarc'h
- Darren M Wells ([ORCID: 0000-0002-4246-4909](https://orcid.org/0000-0002-4246-4909))
- Yves Vigouroux ([ORCID: 0000-0002-8361-6040](https://orcid.org/0000-0002-8361-6040))
- Laurent Laplaze ([ORCID: 0000-0002-6568-6504](https://orcid.org/0000-0002-6568-6504))

## Response text

DOI: [10.7554/eLife.86169.3.sa3](https://doi.org/10.7554/eLife.86169.3.sa3)

The following is the authors’ response to the original reviews.

Reviewer #1 (Recommendations For The Authors):

Some suggestions:

1. It's obviously concerning that your GWAS results are not at all robust to the approach used (Fig S3). Did you try something non-parametric, like a Kruskal-Wallis test?

We used both GWAS and crosses (F2) to validate the presence of the QTL. So ,evidence is not only brought by GWAS. We did not use non parametric tests as we will have difficulty to account for population structure/relatedness with such approaches. Our GWAS approach is certainly a little underpowered associated with the number of individuals we used and certainly the polygenic nature of the root growth traits. But F2 crosses allow us to put more evidence weight on some region we identified with GWAS.

1. You don't explain what you do with heterozygotes, nor discuss the level of inbreeding in general.

We are dealing with inbred lines, but indeed there are not completely fixed inbred lines. For the remaining heterozygotes, they were randomly fixed in one or the other alleles. The median heterozygosity value was low at 5.6%. We clarified this point in the material and methods.

1. The finding that over 30% of RNA-seq reads don't seem to have an annotated home should give you pause. Do they map anywhere? At least discuss what is going on. Also, note that you likely have enormous errors in SNP-calling due to cryptic structural variation - think about what this might do?

We agree with reviewer #1. We added a few sentences in the result section to clarify this point: “When further analyzed, 15.15% of the unmapped reads (with no correspondence to predicted CDS) were found not to match the reference genome. These might correspond either to unsequenced regions or to genotype-specific genomic regions that are not present in the reference line. The remaining unmapped reads corresponded to either rRNA and tRNA genes (40.28% of the unmapped reads) or to non-annotated genes or non-coding RNAs (44.57% of the unmapped reads).”As we used the same reference genome for mapping the RNAseq reads, some genes might not being present in our analysis for the two lines we studied.

1. Did you consider moving PgGRXC9 into Arabidopsis?

This is a great suggestion. In fact, we plan to explore more how some GRXs regulate root growth and how this is conserved in plants in a follow up project. This is however beyond the scope of this manuscript.

Minor suggestions:

1. Why not calculate H^2 simply as line variance divided by total?

Heritability estimated on single individuals in population, approaches generally used for human and animal breeding led directly to line variance divided by total phenotypic variance.

But in plant breeding (or plant science), we generally work on replicated genotypes in different blocks/experimental repetition. So we estimate the heritability of the mean phenotype of genotypes. There is ample literature (Nyquist, 1991; Holland et al. 2003; for a very nice and smartly written explanation, on the introduction of this PhD: http://opus.uni-hohenheim.de/volltexte/2020/1720/pdf/20200221_PhD_Thesis_Publikationsversion.pdf). Calculation of heritability (of the mean phenotype) should take into account for the calculation of the phenotypic variance (denominator) the number of replicate genotypes (we do not have a single plant, but several clones when using inbred lines: n). The meaning of the formula is that the error in the model is inflated because we have n replicate plants per genotype. And so to estimate the heritability of the average genotype, we have to take into account this inflated variance in the errors.

1. While the paper overall is well-written, the captions need further proof-reading.

We corrected all the captions.

Reviewer #2 (Recommendations For The Authors):

Major suggestions:

1. The experimental support for the mutant phenotype of roxy19 needs to be further substantiated. Current methods available for CRISPR mutagenesis make it relatively easy to generate additional alleles. Alternatively, the authors could complement the mutant with a wild-type copy of the gene. These approaches represent the standard of the field and should be used here as well.

We agree with rev #2. We added some sentences in the discussion to stress out the limitations of our study to link the QTL to PgGRXC9.

As stated above we’d like to explore more how some GRXs regulate root growth and how this is conserved in plants. We plan to generate new single and multiple mutants in ROXY19 and its closest homologues (using CRISPR). This is, however, beyond this manuscript.

1. The authors may want to state more clearly what the hypothesis is for how redox levels might contribute to root length differences and more clearly state what the limits of their current study are.

We modified the discussion to try to clearly indicate the limitations of our study.

1. Differences in root growth can be the consequence of a number of different parameters that contribute to root elongation and the authors need to more clearly define which of these are likely affected in their different genotypes.

We agree with Reviewer #2. However, as stated before, we plan to further explore the molecular and cellular mechanisms responsible for the phenotype we observe in Arabidopsis. This will need extra work and is beyond the scope of this manuscript.

1. Page 13, first paragraph. The authors provide an overly strong statement that suggests they have determined the molecular basis for the difference in PgGRXC9:" Altogether, our results suggest that PgGRXC9 is a positive regulator of root growth and that a polymorphism in the promoter region of PgGRXC9 associated with changes in its expression level appeared responsible for a quantitative difference in root growth between the two lines."

While their results suggest the PgGRXC9 locus is associated with root growth variation, they have not directly tested the effect of the polymorphisms in the promoter on gene expression and this statement needs to be weakened.

We changed the text to: “Altogether, our results suggest that PgGRXC9 is a positive regulator of root growth and that a polymorphism in the promoter region of PgGRXC9 might led to changes in its expression level and ultimately to a quantitative difference in root growth between the two lines. However, the effect of the polymorphisms in the promoter on gene expression need to be tested to validate this hypothesis.”

We also changed the title of the manuscript to better reflect our results.

Minor suggestions:

1. Page 4: "FTSW below 0.3 was considered a stressful condition." It was not specified how this threshold was determined.

This value corresponds to the measured FTSW value at which pearl millet genotypes subjected to a dry down generally start to reduce their transpiration rate (see Fig. 1 of Kholová et al, 2010; https://doi.org/10.1093/jxb/erp314). At FTSW values above 0.3, transpiration is not affected. At FTSW values around 0.3, the water supply from pearl millet roots cannot fully support transpiration. The plant enters a drought stress responsive phase and progressively closes its stomata to reduce water losses and decrease plant productive functions to match water supply. We have clarified this in the manuscript.

1. Page 6: Figure 1; footnote: at the end of the description of panel A, a comma is missing between "red" and "blue."

Thanks for pointing that out. This was corrected.

1. The root growth data determined by X-ray imaging is not significant (Fig S4B), yet the authors describe the result in the main text without qualification. The authors should clarify this in the text.

We added some text to clarify this.

1. Page 9: Figure 2C; It would be better to enlarge these images and annotate them to indicate what specific anatomical features have been measured. Currently, only an expert in the field would be able to interpret these images.

While we understand the point made by Reviewer #2, Fig2C was meant to illustrate differences in the root tip of the two lines.

1. Page 9: Figures 2D and E; the number of biological samples measured is not indicated (what is "n"?).

Thanks again for pointing this out. This was added to the figure legend.

1. Page 14: Figure 4B; scale bar needs to be included.

Scale bars were added to the pictures.

1. Page 14: Figure 4; I recommend adding confocal images or DIC of cleared root apex tissues to easily compare the RAM size and cell lengths in both WT and roxy19 mutant.

Once again, we plan to have a follow up study on the molecular and cellular mechanisms of action of ROXY19 and its closest homologues on root development. We believe a thorough analysis of differences in phenotype could be illustrated in a future manuscript.

1. Page 18: main text; "we propose that redox regulation in the root meristem is responsible for a root growth QTL in pearl millet." This statement is ambiguous in the description of the mechanism. The authors do not clarify if the role they propose for PgGRXC9 is in the meristematic or elongation zone. Likely the authors are not able to know precisely where the gene is acting at this point, and so the presented hypothesis needs to more clearly state what limitations there are in assigning a mode of action for the PgGRXC9 and ROXY19 genes in root growth.

We rewrote this paragraph to clarify the current gap in our understanding of the putative PgGRXC9 function.
