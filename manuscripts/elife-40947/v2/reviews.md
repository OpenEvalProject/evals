# Peer review - Round 1

Editors:
- Alfonso Valencia, Barcelona Supercomputing Center Spain

Reviewers:
- Kevin Litchfield, Francis Crick Institute United Kingdom

## Review text

DOI: [10.7554/eLife.40947.052](https://doi.org/10.7554/eLife.40947.052)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Somatic mutations in early metazoan genes disrupt regulatory links between unicellular and multicellular genes in cancer" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aviv Regev as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Kevin Litchfield (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The paper adds to the analysis of the relationship between evolutionary age of genes and their possible role in cancer. A representative set of genes are analysed in terms of accumulated point mutations and copy number changes in seven solid tumours from TCGA. The results are then discussed in terms of the relation between gene age, type of mutations and functional role of the genes as master in gene regulation at different levels. The difference between mutations and CNVs is also interpreted in terms of a potential differential role in gene regulation.

Essential revisions:

There are questions about the use of a more complete TCGA dataset and selection of the initial gene set that affects the scope of the study and results. They have to be properly addressed.

There is also an important question about the relation between the possible positive selection on point mutations in early EM regulators that requires specific considerations, as well as a number of other comment and criticisms regarding clarity and interpretation of the results.

In more detail:

Data completeness:

1) TCGA currently comprises of data from a large number of tumour types. The authors have analysed data from only seven tumour types? Why have the authors conducted the analysis in only a subset of the available solid tumour types in TCGA? Several solid tumour types have been missed (e.g. renal, melanoma, testicular, pancreatic, etc) with no apparent explanation. Please could the authors either extend the analysis to the full TCGA solid tumour dataset, or clarify why only a subset of available data has been utilised.

2) The gene filtering strategy (subsection “Enrichment of recurrent point mutations and CNAs in phylostrata”) raises some concern – only taking genes with more missense+LoF than synonymous mutations may miss some important driver events (e.g. by chance a long gene may carry a number of synonymous mutations, and then missense mutations only in hotspot domains (KRAS G12D, V600E, etc)). By chance drivers may be excluded. Could the authors confirm whether this approach was done on a per tumour type basis, or across all histologies combined? The latter would be particularly concerning. As a minimum the authors should provide a supplementary table showing this data and the genes excluded, so readers can confirm what is being excluded. A better approach instead could be to take only genes significant in MutSigCV analysis for each cancer type (which are already available for all tumor types in the Broad Firehose repository). The mutsigCV algorithm implements a similar method but in a much comprehensive way.

Presentation:

1) Some sections of the text (particularly Results section “Point mutations disrupt the regulation between UC and EM Genes”) should be cut down and streamlined, so the salient (and significant) results are better highlighted, and other non-significant descriptive text removed. For example endless "x out of y" results are quoted, e.g. (4/6 and 5/6 regulators). These proportions are stated with no associated p-values, so it is somewhat unclear to the reader if these significant results or not?

2) The authors have tried to link transcriptional states with mutation states of genes such as gene expression down-regulation has been linked to missense or LoF mutations. This claim needs to be supported with some evidence. It will be particularly helpful for the reader if the authors are able to give more biological context in their analysis. I think this study will definitely benefit from more examples of specific UC/EM-i genes and the pathways they regulate in tumorigenesis.

Positive selection of EM regulators:

The authors propose a model of point mutations in early EM regulators being key drivers under positive selection in cancer (paragraph five “Point mutations disrupt the regulation between UC and EM genes”). This point needs to be further substantiated, by showing these mutated genes are indeed enriched as clonal driver events. Can the authors show the variant allele frequencies for these EM regulator mutations are higher than average, or higher than other groups? This would support their role as drivers and presence in a high proportion of cancer cells.
