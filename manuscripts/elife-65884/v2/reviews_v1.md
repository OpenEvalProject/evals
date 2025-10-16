# Peer review - Round 1

Editors:
- Job Dekker, University of Massachusetts Medical School United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65884.sa1](https://doi.org/10.7554/eLife.65884.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This manuscript finds common molecular features in the blood of three mouse models for neurodevelopmental disorders, Kabuki syndromes 1 and 2 and Rubinstein-Taybi syndrome type 1. These shared features (chromatin accessibility and gene expression) may underlie some of the clinical similarities of these disorders. This work will be of interest to researchers, and to some clinicians studying neurodevelopmental disorders.

Decision letter after peer review:

Thank you for submitting your article "Leveraging the Mendelian Disorders of the Epigenetic Machinery to Systematically Map Functional Epigenetic Variation" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Huda Zoghbi as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. The reviewers and the Reviewing Editor find that an extensive revision is required for the work to be suitable for publication in eLife.

Essential revisions:

1) The introduction is rather short, although the journal does not limit the length of this section. For instance, there is no introduction to the disease phenotypes, what genes are implicated in these diseases, and what is known about their clinical and molecular overlap. As some of this information is in the first sections of the results, the authors should consider moving these paragraphs to the introduction.

2) The authors' rationale for focusing their studies on these conditions is the overlapping immune system dysfunction in these disorders. This overlap should be better described. As immune dysfunction may be biased with respect to sex this issue needs to be addressed as well.

3) The use of ATAC- and RNA-seq data from the same mice as well as the exploration of the GO function of these genes is an important contribution to the literature. The hypothesis of the study (as stated and shown in figure 1) is that shared molecular (ATAC-seq peaks) features across the three conditions cause the common phenotypic features of these conditions. While stating the hypothesis in this way clearly frames the motivation of the study, it is not strictly tested by the experiments performed. While this study moves our understanding of these disorders forward, it does not directly address causation. Further, the GO functions and TFs identified are not clearly linked to disorder-relevant pathways. The authors should consider reframing the hypothesis to better reflect the advances presented in the paper.

4) The ATAC-seq data are generally clearly presented, but there are a few areas where this could be improved:

– Line 139: it would be beneficial to the reader to give a quick summary of the new method to detect overlapping peaks here, so they are not required to flip to the methods section to understand the main idea.

– The authors did not indicate the rationale behind their choice of performing the experiments in 2.5-to 3.5 old mice.

– In the fast ATAC-seq protocol, the authors need to clarify the number of mice used for each comparison -maybe best to add them to Figure 1 and also indicate that all are female which is a limitation of the study.

– What is the justification for using a 10% FDR over a more standard 5%?

– 10% may be justified given that the analysis involves overlapping multiple datasets, and a more permissive q-value cut-off was used to capture more potential findings. If this is the justification, it should be noted.

– In figure 2, why is (f) not shown on the same plot as e)? It appears that the shared peaks differentiate KS1 and KS2, (and perhaps K2S and KS1 from RTS if plotted together). This would seem to be a very notable finding, that is the "shared" peaks differ in the magnitude of change for each condition. Can the authors clarify these data especially from a quantitative perspective, and elaborate on their interpretation?

In the methods, the authors stated that they counted the number of reads that map to each of the 78,193 features (overlapping DHS) from each sample and they only included features with median (across samples) counts greater than 10. How many of these 78,193 features are left for differential analysis? In addition, the authors state that they used surrogate variable analysis to estimate unobserved confounding variables which they adjusted for. Can the authors clearly describe the confounding variables that were identified?

– The PCA on the 313 overlapping promoter peaks (of the initial 824 identified in KS1) within the 3 disorders separate KS1 from KS2 (Figure 2e) , The authors state that this is surprising given the clinical overlap but the authors have only used female KS2 animals. As this is an X-linked gene, these mice may not necessarily exhibit the full KS2 phenotypic spectrum. The rationale for choosing female mice exclusively needs to be provided and the interpretation of the data should be contextualized for only female data.

5) The RNA-seq analysis needs to be improved:

– The authors state that a subset of the mice from the ATAC-seq experiment were used for RNA-seq, can they clarify the exact nature of the overlap? Were all RNA-seq mice part of the ATAC-seq experiment?

– Again, Figure 4 (e) and (f) are not plotted together, making interpreting the nature of the relationships across disorders (a primary outcome of this study) more difficult. And here again, it appears that though many gene expression changes are shared, the magnitude of the change differentiates the conditions from each other. If this is the case can the authors elaborate-are the changes/differences statistically significant?

– Given the low adjusted p-value threshold, have the authors attempted to validate a subset of their findings using another method such as qPCR?

6) In the discussion, (line 330) I agree that the functional relevance of DNA methylation signatures is unclear at this time, due to blood being peripheral to brain. However, several studies have found indications that they may be indeed be relevant. For DNA methylation data, cell type-heterogeneity is addressed better in blood than many other tissues, and is seldom ignored in studies published in the last 2-3 years. When drawing parallels to DNA methylation studies, I would suggest the authors highlight the much stronger relationship between ATAC-seq and gene expression, than that for DNA methylation and gene expression (as demonstrated in this study).

7. The authors need to examine further their methodology to see if they can come to a more definitive understanding of what is driving the predominant skew to open chromatin and the lack of enriched targets for these specific chromatin modifier mutations. Instead of their grouped alignment for their ATAC-seq, they should align the samples individually and examine the previously identified loci for any indication of differences between the samples that may indicate technical confounding, or else. As mentioned, rare genetic variation can still occur in substrains (Watkins-Chow and Pavan, PMID: 18032724), so this should be excluded via SNPs, CNV, Indels within C57BL/6J from Mortazavi et al., (BioRxiv 10.1101/2020.03.16.993683), other datasets, or explored more directly in their data. Although clearly more predominate in human populations, common or rare allelic genetic variation via SNP/ CNV/Indel/Polymorphic Repeats within promoters in loci can drive epigenetic/open chromatin variation (Leinert et al., PMID: 21964573; Do et al., PMID27153397; Martin-Trujillo et al., PMID: 33216750). Although the authors found their loci were predominately within DHSs, this does not preclude that some of these DHS may be polymorphic. One possibility is that the grouping may be accentuating open regions in the potentially more homogeneous mutant strains in comparison to the wild-type mice. If potential strain variation background is adding noise to real results, these may then become more apparent if these are removed, enabling more explainable pathway effects that can be easier interpreted and bring the insights aimed for.

8. The authors state that these Mendelian trait monogenic diseases should be regarded as complex traits "arising from widely distributed epigenetic perturbations across the genome". This may, however, lead to some confusion regarding genetic terminology as they are Mendelian disorders. Instead, the authors could put this in the context of the expanding understanding of a complex modifier landscape of underlying genetic background effects as well as environmental and stochastic factors on penetrance and expressivity of monogenic traits (Oetjens et al., PMID: 31653860; Wright et al., PMID: 30665703; Czyz et al. PMID: 22898292).

9. The authors highlight the overlapping phenotypic features of intellectual disability, growth defects, and immune dysfunction as the justification for looking at these d,ifferent primary genetic defects for common downstream epigenomic alterations. However, they should also acknowledge that specific analysis of each MDEM may bring a more precise evaluation of the disease-driving signals, as multiple distinct pathways can lead to these very broad phenotypes.

10. In regard to the examples in the Introduction of robust relationships between epigenetic alterations and specific phenotypes – the authors should also include the oncogenic role of the promoter methylation of mismatch repair gene MLH1 (Gazzoli et al., PMID:12124320). Additionally, there is no current strong evidence of a role of 'metastable epialleles' in human phenotypes.

11. Authors should also acknowledge that some aspects of the human immunological features of these MDEMs will not be directly comparable in mice (Seok et al., PMID: 23401516, etc).

12. The comment in the Discussion, re DNA methylation 'epi-signatures' should also take into account that these are being used as 'biomarkers' to help improve diagnosis of variants of indeterminate significance in monogenic traits. Therefore, they themselves do not all have to be proved functional to have clinical utility. Furthermore, that this also takes advantage of the fact that the DNA methylome and chromatin modifications are highly interconnected (Thomson et al., PMID: 20393567; Baubec et al., PMID: 25607372, etc).
