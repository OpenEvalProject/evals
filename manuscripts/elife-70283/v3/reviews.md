# Peer review - Round 1

Editors:
- Weiwei Dang, https://ror.org/02pttbw34 Baylor College of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70283.sa0](https://doi.org/10.7554/eLife.70283.sa0)

This manuscript reports a unique, comprehensive, multi-omic resource for the study of replicative senescence. This resource encompasses temporal metabolomic, proteomic, bulk transcriptomic, single cell transcriptomic, and chromatin accessibility states of fibroblasts as they transition from proliferative to replicatively senescent. Hence, it will be considered a valuable resource by aging researchers.


---

# Peer review - Round 1

Editors:
- Weiwei Dang, https://ror.org/02pttbw34 Baylor College of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70283.sa1](https://doi.org/10.7554/eLife.70283.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Revisiting the Hayflick Limit: Insights from an Integrated Analysis of Changing Transcripts, Proteins, Metabolites and Chromatin" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Matt Kaeberlein as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Lynne Cox (Reviewer #2); Payel Sen (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) All three reviewers have raised various concerns about robustness of analyses and statistics for the multi-omics data. They recognize that significant amounts of these analyses will need to be redone and some additional analyses were recommended. However, they all agree that these revisions are essential. Please address these concerns as much as possible.

2) Reviewers #2 and #3 pointed out the necessity to provide some biological validations for novel findings from these multi-omics analyses. This will require additional experiments but will greatly improve this manuscript.

3) All three reviewers have identified the lack of description for certain methods and techniques, mislabeling, typographical errors, etc. Please address all these issues.

4) Reviewer #2 pointed out that the proteomics data should be made publicly available at one of the major proteomics data repositories. Reviewer #1 also pointed out that in-house software codes and scripts for data analyses should also be made publicly available.

Reviewer #1 (Recommendations for the authors):

1. There are major concerns about the statistics in the analysis of the dataset.

a. For the differential expression analysis (4.2.3), the authors state: "DEGs were defined as having p-values < 0.001." This is an incorrect method of filtering DEGs as it does not correct for multiple hypothesis testing. This is all the more surprising because DESeq2, used by the authors, natively provides FDR corrected p-values. The data should be re-analyzed after proper multiple hypothesis correction control (native DEseq2 FDR, Bonferroni, or other).

b. Potentially related to the absence of FDR thresholding, the number of DEGs identified-"8969 genes change with increasing PDL … 11652 genes vary with increasing cell density"-seemed, to this reviewer, really high, and likely the result of improper FDR correction. It will be interesting to see how those numbers change with the multiple testing correction.

c. Based on the methods, the other analyses should also always incorporate a multiple testing correction, i.e. differential ATACseq peaks (4.4.3 p < 0.001, no FDR correction), metabolomics (4.5 no information on differential analysis) and proteomics (4.6.5 no information on differential analysis).

d. When carrying out differential analyses, the authors should always avoid filtering on fold change. They do this for instance in section 2.4 "we focused on compounds exhibiting PDL-dependent changes in abundance > log2 0.5.". Fold-change filtering leads to extremely poor FDR control and should not be used post hoc – the only acceptable method to integrate fold change filtering includes a new statistical framework which takes into account fold change for FDR calculations (see PMC2654802). All results should be presented with this criterion removed or re-calculated with a method that takes fold-change into account.

e. Based on figure legends (Figure 1F, 3A, etc) and methods (4.2.5), FDR correction for multiple testing was also not performed for GSEA results. Please recompute everything including the correction, and only report corrected p-values.

f. There are several key issues with the ATAC-seq analysis (4.4.2), which will require a ground-up reanalysis of the data. Quantile normalization of count data and subsequent use of limma for differential accessibility analysis of ATAC-seq (4.4.2, end) is potential problematic. Indeed, limma is not appropriate for count data (it should only be used for continuous data such as microarray) unless the authors mean that they used limma-voom, which is a different algorithm. Please correct this in the revised analyses. In cases where differential depth cannot be corrected for appropriately, the authors should instead use downsampling of mapped reads to match the lowest depth sample. This will remove sequencing depth biases and allow proper count based methods, such as DEseq2, to perform properly.

2. Additional methodological information is needed for long-term reproducibility of analyses.

a. For reproducibility of code and analyses, all analytical code for this study should be deposited in a repository such as github or made available as a Supplementary file.

b. Please include all version numbers for all used software (e.g. R, Trimmomatic, Salmon, LISA, etc.) packages and R packages (e.g. DESeq2, fgsea, etc.) command parameters where relevant (such as for Trimmomatic, if not available elsewhere). The same should be applied to annotation databases, and if a version number doesn't exist, date of access should be provided.

c. All reagents (e.g. DMEM) should include suppliers and catalogue numbers in order to remove any ambiguity as to which product was used.

d. Salmon is a pseudoaligning method that uses a transcriptome reference, not a genome. The methods say that the index was derived from hg38, but how and using which information and software is not clear. In general, the authors should make sure that all key analytical steps are explicitly documented in the methods for long term reproducibility of the study.

3. It is completely unclear which data/plots were generated using the Illumina mRNA kit and which were generated using the Total RNA Kit. Please specify in text and legend.

Reviewer #2 (Recommendations for the authors):

The -omics aspects of the paper are generally well conducted and provide either confirmatory data on pre-existing studies of senescence or add new data (especially on the key FMT pathway and transcription factors involved). Log2FC of +/- 0.5 is somewhat lower than usual cut-offs, so justification is needed where that is selected. No mention is made of quality control steps in RNAseq analysis, but I assume these were conducted? Use of in-house programs for proteomics analysis does mean that others will not be able to conduct the same analyses, though availability of datasets should allow for validation of findings on other data analysis platforms – have these been publicly deposited as links provided are only to RNAseq datasets? From the protocol provided, it is also not clear that the methodology for protein extraction would release chromatin-bound factors – inclusion of a potent nuclease e.g. Benzonase, would ensure that tightly bound proteins are not lost in the spin steps to remove 'cellular debris'.

Figure 2E: there appears to be an aberrant pattern for cells at PDL33 that is present in all parts – is 33 an outlier? What is this cluster?

The cell biology aspects are much less well described making it impossible for others to reproduce the work – in particular, cell seeding density is critical but not even mentioned for longitudinal culture, and Figure 1D images suggest significant cell crowding. Along the senescence trajectory, primary fibroblasts grown in monolayers increase in surface area (and to some extent in volume) and populations at later PDLs undergo contact inhibition at lower cell densities than those at earlier PDLs so it may be the case that some of the 'gradual' changes (especially those associated with cell cycle changes) reflect simply quiescence form contact inhibition rather than steps to senescence. Methodology to count cells and calculate PDL is needed as different labs may conduct this differently. Daily microscopy inspection of cultures to assess appropriate time points for subculturing is essential – simply choosing to split at 4 or 7 days according to PDL does not account for the morphological changes that occur across the replicative lifecourse. It would therefore be helpful to determine to what degree these findings are cell type specific and which changes represent general cell senescence, especially as multiple RNAseq datasets exist on lung and skin fibroblast senescence with various mode of senescence induction. The Methods mentions 'deep senescence' but it is not clear in the main text what datasets are derived from this. Images of cells at different points along the pathway to senescence would be reassuring, and orthogonal validation of senescence markers e.g. p16, p21 by qRT-PCR is needed. It would be extremely helpful if the RNA seq and protein changes reported were cross validated by conventional techniques.

Although studies are conducted on the influence of cell density on -omics changes over a short time course of 10 days, the effect of cell cycle exit in senescence would be better accounted for by comparing with genuinely quiescent cell populations e.g. serum starvation of the hTERT cells eg Figure 3A

Time points used for comparisons are poorly labelled – are hTERT samples taken at daily intervals or at the same time points in long term culture as the RS samples? The text states that the aim is to control for the effects of long-term cell culture, but this is not apparent from later figures. Figure 1D implies that cell population at the same PDL are used for RS and hTERT groups (were cells transduced at PDL20 to allow analysis at PDL25 allowing for drug selection steps?) yet later on time points are simply given numbers e.g. 1,7 in Figure 2B and 2,4,5,6,7 in Figure 3A. It is not even stated if these are days, weeks or sample numbers.

A comparison between early PDL WT WI38 with hTERT WI38 should be conducted (the authors have the relevant data sets) to ensure that the hTERT expression simply leads to cell immortality without impacting on gene expression patterns – this is critical since telomerase has roles other than at the telomere, including in gene expression control, RNA splicing and mitochondrial metabolism. hTERT transduction is very poorly described in the methods section so that others will not be able to reproduce the experiments: "appropriate target plasmid and packaging constructs" are completely uninformative, as is 'selected. with a selection drug". Specific details are needed.

Experiments on radiation damage to induce senescence assay relatively early time points – cell cycle exit is an early event in the DNA damage response but not indicative of senescence per se. True damage-induced senescence onset should be monitored at later time points post-damage (eg from 14 days) to avoid conflating the acute DDR with senescence-specific gene expression patterns. This could account for the large discrepancy between RS and RIS datasets here.

The oxidative phosphorylation data are interesting and consistent with known changes on senescence (though the effect on ROS generation should be considered more). However, the citation in this context of papers that refer to lipid peroxidation – a state of lipid damage – rather than physiological energy generation through β oxidation of fats. Please take care not to conflate energy generating β oxidation and damaging oxidation in the citations.

The NNMT data are fascinating and really provocative – did the authors consider including bisulfite sequencing to assess DNA methylation state in conjunction with the ATAC-seq data? The finding of CTCF upregulation is also interesting in the context of the LAD/NAD data – would 3C/Hi-C give clearer data on overall chromatin configuration? (It would be intersting to see if TADs change significantly, which would be predicted from the data here).

The manuscript has not been fully proof-read which is somewhat frustrating for the reader e.g. the first few references don't even have volume or page numbers, there is incorrect use of upper/lower case in some places (e.g. amp instead of AMP) and there are various typos throughout. Methods section has gaps/omissions e.g. 4.4.3 refers to Figure ??B, 4.5.1 refers to "(vendor?)" and 4.7.2 refers to "(Cite CIS-BP)". Tenses should be consistent.

Most worryingly, very little effort has been made to ensure the Supplementary figures are informative – figure legends are lacking, labels of figure parts are missing e.g. time points/PDLs on Figure S2, Figure S3; the interpretation that EMT (or rather FMT) is a feature of sesncence depends to some extent on the data in Figure S2 but these appear to show that there is no change of the progression from early proliferation to senescence (though hard to tell as PDLs not given)? statements such as "S phase and G2M cells were isolated" – this is wholly misleading as the cells were not isolated physically according to cell cycle stage (eg FACS), but the data were processed post-hoc to determine which cell cycle stage they most closely fit with according to gene expression patterns. Figure S8 legend states cells at PDL20, figure labels cells at PDL25; time points/cell ages are missing for Figure S9- and cannot state mitochondrial functions are already simply by looking at protein levels – safer to say that changes are consistent with altered mitochondrial metabolism. Again, PDL20 is referred to yet throughout the paper, the earliest PDL analysis is at 25. Figure S10 is uninterpretable as no X axis is given, and time points/PDLs are also missing in Figure S11B. Figure S12D – what do the boxes represent? The lack of labels and suitable legend make it impossible to interpret. Why analyse PDL 46 here, as cells are not yet senescent? Is the whole of chromosome 22 shown in part E? Please provide Mb scale – and state what platform was used to view (e.g. IGV?).Figure S14 – GO terms would be a better way of showing the processes than the word clouds used. Figure S15 lacks a legend – myofibroblast markers (from lit) – I presume from literature? Which are the fibrillar collagens (the collagen number matters).

When describing what samples the data shown are compared against, the terminology "the first sample" needs more information – is this PDL25 for RS? But this 'first sample' appears later in metabolomic analysis eg Figure 3E (hence fold changes will not be comparable with proteomics).

Overall this could be a really great paper, bringing together a range of potent -omics techniques to study replicative senescence at high resolution cross time. Most of the paper is well written and provides a clear and sensible discussion of the work carried out, the data and implications of the results. It is somewhat dense (which may be inevitable with multi-omics studies) and could benefit from more accessible explanation of some of the analyses performed (eg readers will be more familiar with tSNE than UMAP – a brief explanation would help here). However, the paper is let down in parts by sloppy presentation, lack of critical experimental detail (meaning the work cannot be reproduced by others), poor design (or one hopes simply poor description) of comparators, an apparent lack of understanding of the nuances of senescent cell behaviour in culture, and by lack of statical validation of the simpler experiments (no n values noted in some cases – e.g. Figure 1D, Figure 5A, C, Figure S3 etc etc). Confirmatory experiments to cross validate top hits from the -omics studies are also required. Mining the existing proteomics data for PTMs should also be possible and may add some value, though not essential here.

Reviewer #3 (Recommendations for the authors):

1. There are some technical points about ATAC-seq that need to be clarified. (a) global chromatin accessibility may be higher in senescent cells. Could the authors share the bioanalyzer profiles of the ATAC-seq libraries from the different timepoints? Are they similar? (b) senescent cells typically produce far more mitochondrial reads. Could the authors confirm that sufficient depth of sequencing was achieved in their ATAC-seq runs? These data including sequencing statistics, peak coordinates, fragment distribution graphs etc. should be included in the Supplementary Section.

2. The ATAC-seq data might benefit from a RepEnrich analysis to identify peaks in repeat elements that are known to be heterochromatinized in proliferating cells and derepressed in senescence. This, in my opinion, is a better way to look at constitutive heterochromatin desilencing compared to NAD/LAD overlap and is also independent of NAD/LAD calls in a different cell line (in this case IMR-90).

3. What are the authors thoughts about the decrease in chromatin accessibility at promoters, enhancers, and gene bodies in their ATAC-seq data (Figure 5B)? Does this imply a global shut down of transcription? Is it reflected in the transcriptomic analyses?

4. While the authors perform an in-depth analyses of transcription factors most likely to drive RS, they haven't really shown the direct binding of these factors to chromatin in RS (and not hTERT, RIS or CD cells) and/or the change in their expression in senescence. Additionally, no functional experiments are performed by knocking down or overexpressing TEAD1 and investigating its effect on senescence. If possible, it would be nice to include this data (i.e., a western blot, genomic binding of TEAD1 and some functional experiments).
