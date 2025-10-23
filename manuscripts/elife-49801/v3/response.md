# Author response - Round 1

Authors:
- Omaya Dudin ([ORCID: 0000-0002-6673-3149](https://orcid.org/0000-0002-6673-3149))
- Andrej Ondracka ([ORCID: 0000-0003-4193-6027](https://orcid.org/0000-0003-4193-6027))
- Xavier Grau-Bové ([ORCID: 0000-0003-1978-5824](https://orcid.org/0000-0003-1978-5824))
- Arthur AB Haraldsen
- Atsushi Toyoda ([ORCID: 0000-0002-0728-7548](https://orcid.org/0000-0002-0728-7548))
- Hiroshi Suga
- Jon Bråte ([ORCID: 0000-0003-0490-1175](https://orcid.org/0000-0003-0490-1175))
- Iñaki Ruiz-Trillo ([ORCID: 0000-0001-6547-5304](https://orcid.org/0000-0001-6547-5304))

## Response text

DOI: [10.7554/eLife.49801.041](https://doi.org/10.7554/eLife.49801.041)

Essential revisions:

The reviewers find this study to be striking, exciting and well conducted. However, they request that the following points be addressed in a revised submission prior to acceptance.

1) Datasets: The article reports conclusions drawn from new genome sequences of S. arctica and S. tapetis. The sequencing, genome assembly, gene annotation, and RNA-seq data are not provided along with the manuscript. Links to primary data should be provided in the revision, to the accepted standard that ought to accompany the reporting of a newly-sequenced genome. (There is also no GitHub link provided for analysis code.)

We have provided links to all of the requested genome files, as well as the transcriptome analysis code in the Materials and methods section.

2) Literature: Throughout the paper the authors refer to the work in Drosophila as this is indeed the model where cellularization has been chiefly studied. It is noteworthy that the authors consistently refer to a single review by Mazumdar and Mazumdar (who interestingly never worked on cellularization) but never cite the primary literature (mostly from the Wieschaus lab), with the exception of a single paper (Hunter and Wieschaus). This presents a rather skewed reference to the literature, and omits the contribution of membrane dynamics (endo/exocytosis) and its interaction with the actin cytoskeleton (i.e. membrane tension) in cellularization, which has also been a subject of intense investigation in standard cytokinesis. More generally the idea of membrane reservoirs at the cell surface (and in organelles/vesicles) has been thoroughly addressed (e.g. dating back from Erickson and Trinkaus, 1976) but is absent from analysis and discussions. The cited literature should be broadened to address these issues.

We agree. We have expanded the literature and references to cover zygotically transcribed genes and membrane remodeling. We now also emphasize that homologs of zygotically transcribed genes (mostly done by Wieschaus lab) regulating cellularization in Drosophila (such as nullo and slam) are absent in S. arctica. Finally, we have added Figure 5—figure supplement 1 showing the expression of homologs of Rab5 and Rab11 which regulate membrane trafficking in Drosophila and are important for cellularization. Despite being highly expressed (for most), their expression profiles appears to be constant. This might suggest that membrane trafficking does not only intervene during cellularization but also is important during coenocytic development. However, in absence of further investigation, that we believe is beyond the scope of this study, we cannot speculate on the role of membrane trafficking in the cellularization of S. arctica.

3) Statistical support: The authors state that "overall age of the transcriptome across the life cycle revealed an hourglass pattern". Although visually this seems to be the case, it would strengthen the point if the authors could provide statistical evidence by performing an hourglass test for the transcriptome age index. (For example, tools for such a test are provided in Drost et al., 2015.)

We thank the reviewers for pointing out these statistical tests. We have implemented the tests, and we indeed find statistical support for the hourglass pattern for both replicates.

4) Materials and methods: The authors should provide, in Materials and methods, sufficient technical details underlying phylostratigraphic analysis so readers can reproduce the main results. How were splice variants handled when passing proteome sequences to orthofinder? Which output of orthofinder was used? The core orthologs (unicopy 1-1 orthologs) or the pairwise orthologs between all pairwise species comparisons? How many orthogroups were found? The authors could provide either reproducible analysis scripts, or the orthofinder output and phylostratum categorization of genes used to be able to reproducibly compute TAI values (as supplementary data).

We have expanded the Materials and methods section on the orthofinder and phylostratigraphic analysis to address the reviewer’s concerns. Furthermore, in addition to the file of all orthogroups, which was already uploaded as source data, we now include a categorization of genes by gene age according to Dollo parsimony, as a source data file (Figure 4—source data 5).
