# Peer review - Round 1

Editors:
- Elana J Fertig, https://ror.org/00za53h95 Sidney Kimmel Comprehensive Cancer Center, Johns Hopkins University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73796.sa0](https://doi.org/10.7554/eLife.73796.sa0)

This paper performs a comprehensive mechanistic and genomic evaluation of the impact of macrophage polarization on metabolic changes in pancreatic cancer. It provides an important advance to the understanding of the role of the microenvironment in the context of this disease.


---

# Peer review - Round 1

Editors:
- Elana J Fertig, https://ror.org/00za53h95 Sidney Kimmel Comprehensive Cancer Center, Johns Hopkins University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73796.sa1](https://doi.org/10.7554/eLife.73796.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your work entitled "Multi-omic Characterization of Pancreatic Cancer-Associated Macrophage Polarization Reveals Deregulated Metabolic Programs Driven by the GMCSF-PI3K Pathway" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluated has been overseen by Mone Zaidi as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: David DeNardo (Reviewer #3).

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewer #1:

This paper performs comprehensive multi-omics assessment of tumor-educated macrophages to evaluate the mechanisms underlying their critical role in pancreatic cancer.

While this is unquestionably an important study for the field and these omics data are comprehensive, the bioinformatics analysis and data presentation could benefit from further enhancement to better convey the biological findings from the data.

The primary critique in this paper is the presentation and analyses based upon the omics data. These need to be greatly enhanced for publication as described below.

Figure 1 – Differential analyses refer to performing a one-way anova with dunnett's post-hoc test, but the methods describe DESeq2 analysis for the RNA-seq data. This should be clarified in the figure. The presentation for panels C / D would benefit from lines over the *** to clarify that comparisons are relative to the TEM population. In the heatmaps in D, it's unclear why the particular group of TEM is boxed or what comparisons are made to obtain the subset of genes/proteins that are plotted. Moreover, in absence of gene names these heatmaps do not provide considerable information. Recommend adding volcano plots, considering annotations of genes, or similar to help obtain biological insights from the heat maps presented. At minimum, a supplemental table of the differential expression analysis would enable interested readers to evaluate the findings. IT is also unclear whether the mean centering for the heatmaps is performed on variance stabilized gene expression data or merely log transformed data.

The subsection "Metabolism and cytokine signaling are distinctive features of pancreatic TEMs" describes pathway-centric approaches but surprisingly does not perform any pathway analyses.

Figure 2 – As described for figure 1, the statistical method described in the figure caption for the RNA-seq data does not match the methods and would benefit from improved visualization to clarify that comparisons are made relative to to the TEM group. Red / green coloring should be avoided in the heatmap in panel E.

The STRING analysis refers to "a particularly strong functional association", but does not provide statistics to describe how strength was assessed.

Individual PI3K pathway genes are assessed in the scRNA-seq data, but pathway analyses would strengthen the proposed associations.

Figure 4 – As described above, the heatmap could benefit from enhanced gene annotation to assess the biological relevance of the analyses performed.

Reviewer #2:

The authors find that tumor cell conditioned media from Kras-expressing PDAC cells contains high levels of GM-CSF and lactate, which combine to generate macrophages that resemble suppressive macrophages found in the PDAC tumor microenvironment. The authors perform extensive metabolomics on cultured macrophages, correlate these findings with transcriptional and protein-level data, and connect the dots between Kras, GM-CSF, PI3K/AKT signaling, and the suppressive enzyme Arg1. They also find that GM-CSF and lactate are sufficient to synergistically induce Arg1 transcription.

Overall, these data support and extend a wealth of prior literature showing suppressive effects of GM-CSF on tumor-associated myeloid cells, including two seminal papers in Cancer Cell in 2012 reporting that pancreatic cancer cells secreted high levels of GM-CSF. GM-CSF can come from a number of sources in the tumor microenvironment, notably fibroblasts (PMID: 27184426), which are not modeled in the work as currently presented and should be mentioned in the discussion as a limitation/opportunity for future directions.

There are several limitations to the work that modestly detract from the authors' conclusions. First, the in vitro studies were performed in standard tissue culture conditions and the contribution of hypoxia was not addressed. This should be mentioned in the discussion in a paragraph about ways to improve the cross-talk in vitro model along with inclusion of other cell types such as fibroblasts. Second, the connection to human PDAC macrophages is tenuous. Examination of Supplemental Figure 3 reveals that both TXNIP and ACLY are robustly expressed across most cell types, and indeed all of the TEM macrophage genes shown here are shared with at least one other cell type. I believe the authors are trying to say that human PDAC macrophages show a signature of having been polarized by GM-CSF and lactate. It is possible that the other cell types in the tumor microenvironment are not the best comparison; a better strategy might be to compare macrophages differentiated from peripheral blood CD14+ cells +/- human PDAC conditioned media. Alternatively, the authors could examine macrophages from their chronic pancreatitis cohort (PMID: 34296197) or other non-PDAC tissue macrophages as a comparison to show the PDAC-induced upregulation of a TEM signature.

Line 140 and Figure 2B: What is an "enzyme marker"? Please define the specific enzymes that are differentially regulated in TEMs.

Lines 261-263: "In addition, blocking GM-CSF led to a modest decrease in expression of ACLY and TXNIP (Figure 6B, Supplementary Figure 5B), which builds upon our M0 + GM-CSF + lactate qPCR data, in support of an activating role of GM-CSF on enzymatic TEM markers." Awkward phrasing. Please rewrite for clarity and remove the phrase "enzymatic TEM markers".

Figure 6 legend: Please include a reminder to the reader what the drugs target (pan-PI3K inhibitor, BKM120; pan-AKT inhibitor, MK-2206).

Lines 266-267: GM-CSF blockade appears to have no effect on phosphorylated sugars as shown in Supplemental Figure 5C. Please modify this statement accordingly.

Reviewer #3:

The paper by Boyer et al., is an excellent multi-omic approach to try to link changes in macrophage metabolism with RNAseq and proteomic changes. The authors show PDAC-cell derived cytokines (GM-CSF) along with metabolic mediators (lactate) regulate key features in macrophage phenotype and metabolism. This is overall an excellent study with high impact. I have no formal suggestion of new experiments needed, as the studies already done are excellent. However the paper would be considerable improved for the reader with some changes in text and some detailed analysis of the data sets on hand. Otherwise the authors are to commended on a fine piece of work.

1. The authors have a very nice data set. I would love to see them run traditional pathway analysis, GSEA on proteomics and RNAseq, and layer this into the story line. There are some hints at this with limited string analysis and Figure 2C. But this could be improved and discussed. These are likely biologic process that TEMs have that require the metabolic switched shown. Anything here would be of interest.

2. In Figure 4, agin the data are excellent. But I would really love to see more formal pathway analysis and GSEA approaches to identify biologic process. And then I would love to see the authors comment on how these changes in biologic process, require or cross talk with the metabolism. Of course, this can take place in analysis added to results and commentary in the discussion.

3. There is some ambiguity in the results presented in Figure 2B-ED The legend and figure say genes and proteins. Which is it. Did the authors look for overlapping changes (ven diagram style) and then map these to the results? The authors should be explicit here what they did and it they are showing RNA or protein data. E appears to say co-expressed RNA/protein, but details lacking.
