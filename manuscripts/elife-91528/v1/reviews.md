# Peer review - Round 1

Editors:
- Wei Yan, Washington State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.91528.3.sa0](https://doi.org/10.7554/eLife.91528.3.sa0)

This useful study reports datasets on gene expression and chromatin accessibility profiles of spermatogonia at different postnatal ages in mice. Overall, the technical aspects of the sequencing analyses and computational/bioinformatics are solid. This study may be of interest to biomedical researchers working on male germline stem cells and male fertility.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91528.3.sa1](https://doi.org/10.7554/eLife.91528.3.sa1)

Summary

This study was designed to investigate changes in gene expression and associated chromatin accessibility patterns in spermatogonia in mice at different postnatal stages from pups to adults. The objective was to describe dynamic changes in these patterns that potentially correlate with functional changes in spermatogonia as a function of development and reproductive maturation. The potential utility of this information is to serve as a reference against which similar data from animals subjected to various disruptive environmental influences can be compared.

Major Strengths and Weaknesses of the Methods and Results

A strength of the study is that it reviews previously published datasets describing gene expression and chromatin accessibility patterns in mouse spermatogonia. A weakness of the study is that it is not clear what new information is provided by the data provided that was not already known from previously published studies (see below). Specific weaknesses include the following...

- Terminology - In the Abstract and first part of the Introduction the authors use the generic term "spermatogonial cells" in a manner that seems to be referring primarily to spermatogonial stem cells (SSCs) but initially ignores the well-known heterogeneity among spermatogonia - particularly the fact that only a small proportion of developing spermatogonia become SSCs - and ONLY those SSCs and NOT other developing spermatogonia - support steady-state spermatogenesis by retaining the capacity to either self-renew or contribute to the differentiating spermatogenic lineage throughout the male reproductive lifespan. The authors eventually mention other types of developing male germ cells, but their description of prospermatogonial stages that precede spermatogonial stages is deficient in that M-prospermatogonia - which occur after PGCs but before T1-prospermatogonia - are not mentioned. This description also seems to imply that all T2-prospermatogonia give rise to SSCs which is far from the case. It is the case that prospermatogonia give rise to spermatogonia, but only a very small proportion of undifferentiated spermatogonia form the foundational SSCs and ONLY SSCs possess the capacity to either self-renew or give rise to sequential waves of spermatogenesis.

- Introduction - Statements regarding distinguishing transcriptional signatures in spermatogonia at different postnatal stages appear to refer to ALL subtypes of spermatogonia present at each stage collectively, thereby ignoring the well-known fact that there are distinct spermatogonial subtypes present at each postnatal stage and that some of those occur at certain stages but not at others. This brings into question the usefulness of the authors' discussion of what types of genes are expressed and/or what types of changes in chromatin accessibility are detected in spermatogonia at each stage.

- Methodology - The authors based recovery (enrichment) of spermatogonia from male pups on FACS sorting for THY1 and RMV-1. While sorting total testis cells for THY1+ cells does enrich for spermaogonia, this approach is now known to not be highly specific for spermatogonia (somatic cells are also recovered) and definitely not for SSCs. There are more effective means for isolating SSCs from total testis cells that have been validated by transplantation experiments (e.g. use of the Id4/eGFP transgene marker).

The authors then used "deconvolution" of bulk RNA-seq data in an attempt to discern spermatogonial subtype-specific transcriptomes. It is not clear why this is necessary or how it is beneficial given the availability of multiple single-cell RNA-seq datasets already published that accomplish this objective quite nicely - as the authors essentially acknowledge. Beyond this concern, a potential flaw with the deconvolution of bulk RNA-seq data is that this is a derivative approach that requires assumptions/computational manipulations of apparent mRNA abundance estimates that may confound interpretation of the relative abundance of different cellular subtypes within the hetergeneous cell population from which the bulk RNA-seq data is derived. Bottom line, it is not clear that this approach affords any experimental advantage over use of the publicly available scRNA-seq datasets and it is possible that attempts to employ this approach may be flawed yielding misleading data.

- Results & Discussion - In general, much of the information reported in this study is not novel. The authors' discussion of the makeup of various spermatogonial subtypes in the testis at various ages does not really add anything to what has been known for many years on the basis of classic morphological studies. Further, as noted above, the gene expression data provided by the authors on the basis of their deconvolution of bulk RNA-seq data does not add any novel information to what has been shown in recent years by multiple elegant scRNA-seq studies - and, in fact, as also noted above - represents an approach fraught with potential for misleading results. The potential value of the authors' report of "other cell types" not corresponding to major somatic cell types identified in earlier published studies seems quite limited given that they provide no follow-up data that might indicate the nature of these alternative cell types. Beyond this, much of the gene expression and chromatin accessibility data reported by the authors - by their own admission given the references they cite - is largely confirmatory of previously published results. Similarly, results of the authors' analyses of putative factor binding sites within regions of differentially accessible chromatin also appear to confirm previously reported results. Ultimately, it is not at all novel to note that changes in gene expression patterns are accompanied by changes in patterns of chromatin accessibility in either related promoters or enhancers. The discussion of these observations provided by the authors takes on more of a review nature than that of any sort of truly novel results. As a result, it is difficult to discern how the data reported in this manuscript advance the field in any sort of novel or useful way beyond providing a review of previously published studies on these topics.

Likely impact - The likely impact of this work is relatively low because, other than the value it provides as a review of previously published datasets, the new datasets provided are not novel and so do not advance the field in any significant manner.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91528.3.sa2](https://doi.org/10.7554/eLife.91528.3.sa2)

This revised manuscript attempts to explore the underlying chromatin accessibility landscape of spermatogonia from the developing and adult mouse testis. The key criticism of the first version of this manuscript was that bulk preparations of mixed populations of spermatogonia were used to generate the data that form the basis of the entire manuscript. To address this concern, the authors applied a deconvolution strategy (CIBERSORTx (Newman et al., 2019)) in an attempt to demonstrate that their multi-parameter FACS isolation (from Kubota 2004) of spermatogonia enriched for PLZF+ cells recovered spermatogonial stem cells (SSCs). PLZF (ZBTB16) protein is a transcription factor known to mark all or nearly all undifferentiated spermatogonia and some differentiating spermatogonia (KIT+ at the protein level) - see Niedenberger et al., 2015 (PMID: 25737569). The authors' deconvolution using single-cell transcriptomes produced at postnatal day 6 (P6) argue that 99% of the PLZF+ spermatogonia at P8 are SSCs, 85% at P15 and 93% in adults. Quite frankly given the established overlap between PLZF and KIT and known identity of spermatogonia at these developmental stages, this is impossible. Indeed - the authors' own analysis of the reference dataset demonstrates abundant PLZF mRNA in P6 progenitor spermatogonia - what is the authors' explanation for this observation? The same is essentially true in the use of adult references for celltype assignment. The authors found 63-82% of SSCs using this different definition of types (from a different dataset), begging the question of which of these results is true.

In their rebuttal, the authors also raise a fair point about the precision of differential gene expression among spermatogonial subsets. At the mRNA level, Kit is definitely detectable in undifferentiated spermatogonia, but it is never observed at the protein level until progenitors respond to retinoic acid (see Hermann et al., 2015). I agree with the authors that the mRNAs for "cell type markers" are rarely differentially abundant at absolute levels (0 or 1), but instead, there are a multitude of shades of grey in mRNA abundance that "separate" cell types, particularly in the male germline and among the highly related spermatogonial subtypes of interest (SSCs, progenitor spermatogonia and differentiating spermatogonia). That is, spermatogonial biology should be considered as a continuous variable (not categorical), so examining specific cell populations with defined phenotypes (markers, function) likely oversimplifies the underlying heterogeneity in the male germ lineage. But, here, the authors have ignored this heterogeneity entirely by selecting complex populations and examining them in aggregate. We already know that PLZF protein marks a wide range of spermatogonia, complicating the interpretation of aggregate results emerging from such samples. In their rebuttal, the authors nicely demonstrate the existence of these mixtures using deconvolution estimation. What remains a mystery is why the authors did not choose to perform single-cell multiome (RNA-seq + ATAC-seq) to validate their results and provide high-confidence outcomes. This is an accessible technique and was requested after the initial version, but essentially ignored by the authors.

A separate question is whether these data are novel. A prior publication by the Griswold lab (Schleif et al., 2023; PMID: 36983846) already performed ATAC-seq (and prior data exist for RNA-seq) from germ cells isolated from synchronized testes. These existing data are higher resolution than those provided in the current manuscript because they examine germ cells before and after RA-induced differentiation, which the authors do not base on their selection methods. Another prior publication from the Namekawa lab extensively examined the transcriptome and epigenome in adult testes (Maezawa et al., 2000; PMID: 32895557; and several prior papers). The authors should explain how their results extend our knowledge of spermatogonial biology in light of the preceding reports.

The authors are also encouraged to improve their use of terminology to describe the samples of interest. The mitotic male germ cells in the testis are called spermatogonia (not spermatogonial cells, because spermatogonia are cells). Spermatogonia arise from Prospermatogonia. Spermatogonia are divisible into two broad groups: undifferentiated spermatogonia (comprised of few spermatogonial stem cells or SSCs and many more progenitor spermatogonia - at roughly 1:10 ratio) and differentiating spermatogonia that have responded to RA. The authors also improperly indicate that SSCs directly produce differentiating spermatogonia - indeed, SSCs produce transit-amplifying progenitor spermatogonia, which subsequently differentiate in response to retinoic acid stimulation. Further, the use of Spermatogonial cells (and SPGs) is imprecise because these terms do not indicate which spermatogonia are in question. Moreover, there have been studies in the literature which have used similar terms inappropriately to refer to SSCs, including in culture. A correct description of the lineage and disambiguation by careful definition and rigorous cell type identification would benefit the reader.

Overall, my concern from the initial version of this manuscript stands - critical methodological flaws prevent interpretation of the results and the data are not novel. Readers should take note that results in essentially all Figures do not reflect the biology of any one type of spermatogonium.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91528.3.sa3](https://doi.org/10.7554/eLife.91528.3.sa3)

In this study, Lazar-Contes and colleagues aimed to determine whether chromatin accessibility changes in the spermatogonial population during different phases postnatal mammalian testis development. Because actions of the spermatogonial population set the foundation for continual and robust spermatogenesis and the gene networks regulating their biology are undefined, the goal of the study has merit. To advance knowledge, the authors used mice as a model and isolated spermatogonia from three different postnatal developmental age points using cell sorting methodology that was based on cell surface markers reported in previous studies and then performed bulk RNA-sequencing and ATAC-sequencing. Overall, the technical aspects of the sequencing analyses and computational/bioinformatics seems sound but there are several concerns with the cell population isolated from testes and lack of acknowledgement for previous studies that have also performed ATAC-sequencing on spermatogonia of mouse and human testes. The limitations, described below, call into question validity of the interpretations and reduce the potential merit of the findings.

I suggest changing the acronym for spermatogonial cells from SC to SPG for two reasons. First, SPG is the commonly used acronym in the field of mammalian spermatogenesis. Second, SC is commonly used for Sertoli Cells.

The authors should provide a rationale for why they used postnatal day 8 and 15 mice.

The FACS sorting approach used was based on cell surface proteins that are not germline specific so there was undoubtedly somatic cells in the samples used for both RNA and ATAC sequencing. Thus, it is essential to demonstrate the level of both germ cell and undifferentiated spermatogonial enrichment in the isolated and profiled cell populations. To achieve this, the authors used PLZF as a biomarker of undifferentiated spermatogonia. Although PLZF is indeed expressed by undifferentiated spermatogonia, there have been several studies demonstrating that expression extends into differentiating spermatogonia. In addition, PLZF is not germ cell specific and single cell RNA-seq analyses of testicular tissue has revealed that there are somatic cell populations that express Plzf, at least at the mRNA level. For these reasons, I suggest that the authors assess the isolated cell populations using a germ cell specific biomarker such as DDX4 in combination with PLZF to get a more accurate assessment of the undifferentiated spermatogonial composition. This assessment is essential for interpretation of the RNA-seq and ATAC-seq data that was generated.

A previous study by the Namekawa lab (PMID: 29126117) performed ATAC-seq on a similar cell population (THY1+ FACS sorted) that was isolated from pre-pubertal mouse testes. It was surprising to not see this study referenced to in the current manuscript. In addition, it seems prudent to cross-reference the two ATAC-seq datasets for commonalities and differences. In addition, there are several published studies on scATAC-seq of human spermatogonia that might be of interest to cross-reference with the ATAC-seq data presented in the current study to provide an understanding of translational merit for the findings.
