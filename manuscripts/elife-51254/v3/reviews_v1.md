# Peer review - Round 1

Editors:
- Naama Barkai, Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.51254.sa1](https://doi.org/10.7554/eLife.51254.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In your article, you present individual transcriptomes of diploid yeast cells, applying your method to monitor transcriptional changes across an array of newly generated barcoded deletion mutants across a panel of stresses. Beyond the development of the method, the main and most original point of the manuscript is that you infer gene regulatory networks based on the transcriptomes retrieved from barcoded genotypes in diverse conditions. The manuscript is well written and together with related reports will become one of the golden standards for yeast single cells. You are commended for providing a complete and user-friendly dataset (deposited and interactive through a shiny app), which will be a valuable resource for the yeast community.

Decision letter after peer review:

Thank you for submitting your work entitled "Gene regulatory network reconstruction using single-cell RNA sequencing of barcoded genotypes in diverse environments" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below. As you will see, the reviewers found the paper to be a bit preliminary in the interpretation and the meaningfulness of the presented data. The reviewers did find the work to be potentially suitable for eLife and will be happy to look at a revised version, provided that you can fully address all comments raised in the individual reviews.

Reviewer #1:

Here, Jackson et al. apply for the first time a 10x Genomics protocol for scRNAseq in barcoded S. cerevisiae deletion strains. The work analyzed 11 transcription-factor deletion strains pooled together and responding to 11 different conditions related to nitrogen metabolism. The authors then applied a gene-regulatory network (GRN) inference method to predict a nitrogen metabolism regulatory network.

The pluses of the work are that it is a hot topic and, although not the first scRNAseq in fungi, the first to look very broadly at tens of thousands of yeast cells. The barcoding method is interesting, although unclear how it's different from the barcode sequencing that is part of the standard 10x genomics pipeline and has been used before in other systems.

The weaker points for me were in the analysis. The authors have expertise in GRN inference, but I had a hard time understanding from the main text what was novel here and specific for single cell data versus previously published methods applied to data pooled across cells/conditions. I will leave it to network inference modelers to dissect those details. But in a broader sense, I was left wanting more follow-up to show that the methods produced new insights. The authors predicted a network but as there is no biological validation and little computational validation it's unclear how big of an advance this is. I was also left wondering about the biological insights that can be gleaned from having single cell data (beyond variation in cell-cycle stage, which is readily identifiable in all scRNAseq studies). I suspect there is interesting biology in the heterogeneity in the response data but there was not much addressed on that topic. In my opinion, this is a great new method with a potentially powerful dataset. But since there are many GRN methods and this overall approach seems similar to Perturb-seq and other methods, the results and impact for me fall below the bar of eLife.

Some specific points are outlined below.

1) The authors report reads from 38,000 cells, which to date is the most cells studied in fungi. But the median number of genes covered is only <700. Since the paper focuses on re-bulked data (to call differentially expressed genes by DESeq2 and, I think, for their main GRN network inference?), I was left wondering how many genes are measured in the re-bulked data per condition. I was surprised how few genes were called by DESeq (Figure 4B), but it's unclear how many genes are actually measured in >1 cell condition/mutant. I was also curious what fraction of known targets (e.g. based on prior studies or ChIP-seq datasets) were called for measured genes.

2) It would be useful to know how well the 10x protocol works for cells and if the aggregated wild-type data recapitulates bulk profiles in conditions that have been previously measured. I was a little concerned at how the cells were collected, which appeared to take live cells and wash them several times in RNALater buffer – does that immediately kill cells? If not, I was wondering if that is inducing a response. I was also left wondering if the protocol captures only the most abundant transcripts. Perhaps I missed this on the supplement, but I was wondering how the% cells in which a transcript was measured compared to RPKM from bulk measurements. Clearly more abundant transcripts will be more easily captured, but some more analysis here would be useful for a new method.

3) The GRN modeling was not clear to me from the main text. It appears that the authors are using their published Inferelator method that takes priors based on ChIP-seq data, and re-bulks the scRNAseq data (at least for the multi-task inference). Perhaps their point is that the 10x approach allows pooling of many genotypes and conditions, but for me the analysis missed the potential power of having single cell data. The authors make statements on the networks in Figure 6 and Figure 7 about the number of "novel" regulatory connections – but I saw no validation of those predictions, including by computation. How do we know that any of these are real and that the method is producing new insights? AUROCs comparing to known data is not enough to say that new regulatory connections were discovered. This was especially true for Figure 7 – how do we know these new predictions mean anything about a connection to cell cycle without some validation?

4) I had some quibbles with part of the Discussion.

i) First, while the authors cite several recent S. cerevisiae scRNAseq datasets, saying that this is the "first report of large-scale scRNAseq" in yeast is not accurate – it's true they measured 38,000 cells but at a depth of only <700 genes per cell, which is far fewer than 2500-3000 of other studies in several hundred cells. A fairer sentence is required, also citations of recent Sz. pombe scRNAseq (Saint et al., 2019) should be included.

ii) "We observe significant heterogeneity in individual cells.… Much of this variation can be explained by the mitotic cell cycle" – that statement is not true, there does not seem to be an attempt to quantify heterogeneity over most genes. That they see heterogeneity in cell cycle stage as expected does not mean that cell cycle stage explains heterogeneity in the rest of the response, which was not reported on here.

Reviewer #2:

In the manuscript submitted by Jackson et al., the authors proposed to profile individual transcriptomes of diploid yeast cells optimizing the 10x genomics pipeline. The manuscript demonstrates the feasibility and robustness of the method and the authors applied it to monitor the transcriptional networks across an array of newly generated barcoded deletion mutants across a panel of stresses. The manuscript is scientifically sound and of outstanding quality, it's well written and together with previous reports this year will become one of the golden standards for yeast single cells.

The authors provide a complete and user-friendly dataset (deposited and interactive through a shiny app) that will be a valuable resource for the yeast community. All in all, I think this is a very solid manuscript that with minor corrections I would strongly support for publication in eLife.

Beyond the development of the method, the main and most original point of the manuscript is that the authors aim to generate infer gene regulatory networks based on the transcriptomes retrieved from barcoded genotypes in diverse conditions. I have some questions and comments (of varying levels of concern) that I feel should be addressed in the current version of the manuscript.

The authors leverage in their previous experience in GRN reconstruction and propose this approach has allowed them to discover novel regulatory relationships between cell cycle-regulated gene expression in response to changes in nitrogen source. In my opinion, this part of the manuscript needs to be reinforced and some of the conclusions driven from the GRN should be and some representative novel regulatory relationships experimentally demonstrated. As well the authors should provide context to their findings as they often read a bit disconnected.

In terms of data quality, the number of mitochondrial and ribosomal reads per genotype and condition should be plotted, as a quality metric and given that a lot of ribosomal gene expression is cell cycle regulated. This could be relevant to understand separate clusters within conditions which the authors do not mention in the results and/or discussion and given the fact that different zymolyase concentrations were used for cell lysis.

The optical density of the cells at the harvesting (besides the total cell number) should be provided to ease the reproducibility for other labs.

If I understand correctly, cell cycle clusters within conditions in Figure 3 is confusing. For example expression of DSE2 or PIR1 seem to be highest in the green and grey clusters respectively (Figure 3A) however in Figure 3B panel I the highest expression is assigned to the grey-yellow for DSE2 and PIR1 to the green cluster.

As well, the UMAPS from Figure 3A, the authors claim the clustering is mainly condition-dependent and genotype-independent. However, conditions like MMEtOH, CSTARVE, NLIM-PRO have clear clusters that do not seem cell cycle-dependent and these might be biologically relevant. The authors should at least comment or those or run a DE analysis to see what these are.

How do the newly generated data compare to Gasch et al., 2017 and Nadal-Ribelles et al., 2019?

The number of differentially expressed genes even in the YPD condition seems a bit low. How do these pseudobulk compare to the deletome data (Holstege lab) or other published datasets?

As well, the authors use DESeq in Figure 4B, but these results are contradictory with what is shown in Figure S4Bi which is done by Welch testing. This is a bit confusing and does not add much to the reader. I would suggest to run DE between conditions using DESeq or provide the reasoning as to why these two different approaches are used and done?

Why do transcription factor activities FKH1 and FKH2 and SWI4 SWI5 do not overlap (they almost seem mutually exclusive), one would expect them to have similar profiles. Similarly, NDD1 regulates S-phase genes but the TFA does not overlap with the HTB expression shown in Figure 3.

Reviewer #3:

This paper by Gresham, Bonneau and colleagues presents to date the largest single cell RNA-seq datasets in yeast using a novel deletion and barcoding strategy that enables them to measure individual cells under different genetic perturbations of transcription factors and environmental conditions. The study is focused on better understanding the regulatory network in nitrogen starvation however it could be broadly applied across multiple conditions. Some findings are: the genotypes tend to be generally uniformly present in all conditions except RTG1 and 3 and GLN3; there is a co-regulated set of genes regulated by cell cycle and nitrogen TFs; multi-task learning is a viable approach for network inference in scRNAseq data. The paper is a significant contribution to the field providing a novel dataset to yeast and general gene regulation community.

I have some comments, which I think are minor and can strengthen the messages of the paper.

1) In Figure 5C, is the single task network inferred by merging all the data and learning a single network or by learning separate networks with single tasking and aggregating the results? If not, how does the single task per condition followed by aggregation perform?

2) The authors don't get much into the context-specificity of the inferred networks. They interpret only the final aggregated network. It would be useful to know how similar the individual condition-specific networks are and if there is a conserved core used by multiple conditions. The only comparison of context specificity is being done at the level of AUPR, it might be helpful to do this comparison just by comparing the inferred networks.

3) Some discussion about the variation in the AUPRs would be helpful. Is it because the gold standard is biased towards the conditions on which the AUPR is high. It seems the AUPR for the MMEtOH network is close to what is inferred by the multi-task learning, and some explanation of why this might be is helpful.

4) A comparison of the AUPR of the single task condition-specific networks and the multi-task condition specific network could further show the advantage of the multi-task learning framework.

5) It would be helpful to emphasize if and how the multi-task learning approach used here was from extended from the Castro, 2019 paper.

6) The Discussion could be strengthened. The authors present some results about the interplay between cell cycle and nitrogen response. It was not clear why this is interesting to study beyond that there is a shared regulatory program. This might be worth bringing up in the Discussion to tie back to the initial goal of inferring a network for nitrogen metabolism and the TOR signaling pathway and the general role of cell cycle and stress response.

7) The authors don't find a substantial impact of TF knockout on gene expression under different conditions (I assume the comparisons were done while controlling for the conditions). How does this compare to bulk data? How much of this observation could be due to the sparsity of scRNAseq data versus the redundancy of TFs.
