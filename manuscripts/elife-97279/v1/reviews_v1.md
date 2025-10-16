# Peer review - Round 1

Editors:
- Lydia WS Finley, Memorial Sloan Kettering Cancer Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.97279.3.sa0](https://doi.org/10.7554/eLife.97279.3.sa0)

This valuable study proposes that protein secreted by colon cancer cells induces cells with Paneth-like properties that favor colon cancer metastasis. The evidence supporting the conclusions is solid but the study would benefit from more direct experiments to test the functional role of Paneth-like cells and to monitor metastasis from colon tumors. The work will be of interest to researchers studying colon cancer metastasis.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97279.3.sa1](https://doi.org/10.7554/eLife.97279.3.sa1)

Summary:

The authors addressed the influence of DKK2 on colorectal cancer (CRC) metastasis to the liver using an orthotopic model transferring AKP-mutant organoids into the spleens of wild-type animals. They found that DKK2 expression in tumor cells led to enhanced liver metastasis and poor survival in mice. Mechanistically, they associate Dkk2-deficiency in donor AKP tumor organoids with reduced Paneth-like cell properties, particularly Lz1 and Lyz2, and defects in glycolysis. Quantitative gene expression analysis showed no significant changes in Hnf4a1 expression upon Dkk2 deletion. Ingenuity Pathway Analysis of RNA-Seq data and ATAC-seq data point to a Hnf4a1 motif as a potential target. They also show that HNF4a binds to the promoter region of Sox9, which leads to LYZ expression and upregulation of Paneth-like properties. By analyzing available scRNA data from human CRC data, the authors found higher expression of LYZ in metastatic and primary tumor samples compared to normal colonic tissue; reinforcing their proposed link, HNF4a was highly expressed in LYZ+ cancer cells compared to LYZ- cancer cells.

Strengths:

Overall, this study contributes a novel mechanistic pathway that may be related to metastatic progression in CRC.

Weaknesses:

The main concerns are related to incremental gains, missing in vivo support for several of their conclusions in murine models, and missing human data analyses.

Main comments

Novelty:

The authors previously described the role of DKK2 in primary CRC, correlating increased DKK2 levels to higher Src phosphorylation and HNF4a1 degradation, which in turn enhances LGR5 expression and "stemness" of cancer cells, resulting in tumor progression (PMID: 33997693). A role for DKK2 in metastasis has also been previously described (sarcoma, PMID: 23204234)

Mouse data:

(a) The authors analyzed liver mets, but the main differences between AKT and AKP/Dkk2 KO organoids could arise during the initial tumor cell egress from the intestinal tissue (which cannot be addressed in their splenic injection model), or during pre-liver stages, such as endothelial attachment. While the analysis of liver mets is interesting, given that Paneth cells play a role in the intestinal stem cell niche, it is questionable whether a study that does not involve the intestine can appropriately address this pathway in CRC metastasis.

(b) The overall number of Paneth cells found in the scRNA-seq analysis of liver mets was low (17 cells, Fig.3), and assuming that these cells are driving the differences seems somewhat far-fetched.

(c) Fig. 6 suggests a signaling cascade in which the absence of DKK2 leads to enhanced HNF4A expression, which in turn results in reduced Sox9 expression and hence reduced expression of Paneth cell properties. It is therefore crucial that the authors perform in vivo (splenic organoid injection) loss-of-function experiments, knockdown of Sox9 expression in AKP organoids, and Sox9 overexpression experiments in AKP/Dkk2 KO organoids to demonstrate Sox9 as the central downstream transcription factor regulating liver CRC metastasis.

(d) Given the previous description of the role of DKK2 in primary CRC, it is important to define the step of liver metastasis affected by Dkk2 deficiency in the metastasis model. Does it affect extravasation, liver survival, etc.?

Human data:

Can the authors address whether the expression of Dkk2 changes in human CRC and whether mutations in Dkk2 as correlated with metastatic disease or CRC stage?

Bioinformatic analysis

GEO repositories remain not open (at the time of the re-review) and SRA links for raw data are still unavailable. Without access to raw data, it is not possible to verify the analyses or fully assess the results. A part of the article was made by re-analyzing public data so the authors should make even the raw available and not just the count tables


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97279.3.sa2](https://doi.org/10.7554/eLife.97279.3.sa2)

Summary:

The authors propose that DKK2 is necessary for the metastasis of colon cancer organoids. They then claim that DKK2 mediates this effect by permitting the generation of lysozyme-positive Paneth-like cells within the tumor microenvironmental niche. They argue that these lysozyme-positive cells have Paneth-like properties in both mouse and human contexts. They then implicate HNF4A as the causal factor responsive to DKK2 to generate lysozyme-positive cells through Sox9.

Strengths:

The use of a genetically defined organoid line is state-of-the-art. The data in Figure 1 and the dependence of DKK2 for splenic injection and liver engraftment, as well as the long-term effect on animal survival, are interesting and convincing. The rescue using DKK2 administration for some of their phenotype in vitro is good. The inclusion and analysis of human data sets help explore the role of DKK2 in human cancer and help ground the overall work in a clinical context.

Remaining Weaknesses after revision:

(1) The authors have effectively explained the regulation of HNF4A at both mRNA and protein levels. To further strengthen their findings, I recommend using CRISPR technology to generate DKK2 and HNF4A double knockout organoids. This approach would allow the authors to investigate whether the AKP liver metastasis is restored in the double knockout condition. Such an experiment would provide more direct evidence that HNF4A protein stabilization is the crucial mechanism for liver metastasis suppression following DKK2 knockout.
