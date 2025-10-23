# Peer review - Round 1

Editors:
- Benjamin J Blencowe, University of Toronto Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.46919.sa1](https://doi.org/10.7554/eLife.46919.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "FMRP has a cell-type-specific role in CA1 pyramidal neurons to regulate autism-related transcripts and circadian memory" for consideration by eLife. Your article has been reviewed by Huda Zoghbi as the Senior Editor, a Reviewing Editor, and three reviewers. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This study aims to identify neuronal cell-type specific functional roles of FMRP with implications in FXS pathophysiology. The authors take advantage of their elegant cTag CLIP approach to endogenously tag FMRP with AcGFP in CA1 pyramidal neurons or cerebellar granule cells and perform CLIP-Seq to determine FMRP direct targets in these cell types in the mouse brain. The cTag CLIP-seq data are compared with TRAP data from the same cell types in WT and Fmr1 deficient mice to assess effects of loss of FMRP binding on gene expression. Analysis of these data resulted in several interesting observations including that FMRP stabilizes targets and that FMRP targets are enriched for autism- as well as circadian-related transcripts, particularly in CA1 pyramidal neurons. The authors complement these observations with behavioural analyses revealing that FMRP deficiency has differential effects on memory depending on the state of the circadian cycle. Overall, this is an interesting study that provides timely cell type-specific insights into FMRP function in vivo. However, there are several technical concerns and additional comments that the authors are requested to address before their manuscript can be considered further.

Essential revisions:

1) The authors' approach of using CA1-specific TRAP data may be problematic for assessing transcript abundance for the purpose of normalizing FMRP-binding. This is especially a concern given evidence of reduced ribosome occupancy over transcripts bound with high affinity by FMRP (e.g. Sharma et al., 2019). We recommend that the authors perform the following experiment to address this concern, or at the very least more clearly explain the caveats/justification of their approach and how it may affect interpretations.

Perform FACS of CA1 labelled neurons, followed by RNA-seq to assess transcript abundance and use these data to normalize FMRP cTag CLIP signal. A significant correlation between FMRP targets detected by this approach and those detected using TRAP data would provide more confidence in the current results.

2) The Cre-lox dependent tagging of FMR1 could affect downstream interpretation since Fmr1 harbours alternative last coding exons and other processing events (eg. Zimmer et al., 2016; Tseng et al., 2017). It is recommended that the authors provide RT-PCR and western evidence from FMRP-tagged as well as wild type animals to show that the Cre-lox tagging strategy captures the majority of FMRP isoforms.

3) Figure 1B. Related to (2), it is recommended that the authors perform immunofluorescence microscopy with an antibody against FMRP to confirm whether the GFP tagged protein co-localizes with endogenous protein.

4) The authors use unpublished data (cited as Van Driesche et al., in submission) in their manuscript, yet the corresponding methods are not described, and their paper is not available in BioRxiv. As such, analyses involving these data (especially in the section "Comparison of CLIP across cell types") are difficult to interpret and assess. The authors are requested to provide a more detailed description of these data and methods, and their paper should be made available to the reviewers. Related to this, the reviewers have several questions/concerns about the data analysis which the authors are requested to address.

5) In the CLIP score calculation, the formula for RPKM used by the authors (which is somewhat unclear because of how it is typed out in the methods section) appears to be as follows:

〖RPKM〗_i = ((〖CrePos Counts〗_i-〖CreNeg Counts〗_i)(1000000)) / ((L/1000)(CrePos Total Counts-Cre Neg Total Counts))

where i is a specific transcript, L is the CDS length, and all counts originate in the CDS. It is recommended that Equation Editor is used to write the equation, but there is no way to do this in the review submission site, so just for clarity:

Numerator = (〖CrePos Counts〗_i-〖CreNeg Counts〗_i)(1000000)

Denominator = ((L/1000)(CrePos Total Counts-Cre Neg Total Counts))

This formula seems strange because if the Cre+ and Cre- samples are sequenced to the same depth (which is probably what the authors would attempt to do), then the denominator would be zero. I'm guessing that the actual formula probably comprises two separately normalized terms for the Cre+ and Cre- counts, but I could be misunderstanding something. Please clarify.

6) The authors use a linear regression model to identify high-affinity binding targets for FMRP based on their CLIP score analysis. This seems problematic because the data used as input are counting data, and this analysis does not appear to take counting noise and overdispersion into account. It is also unclear whether any statistical test was applied to this analysis. In order to compute the cumulative histograms in, for example, Figure 2, the authors used the generalized linear model in DESeq2 and applied it in a sophisticated way that takes sample pairing into account. Why not apply this same approach to the CLIP analysis (after taking into consideration the issues with normalization raised in point 1)? In principle, DESeq2 will account for coverage differences between samples and genes, account for overdispersion, and provide a test statistic for each transcript.

7) The authors show a handful of cell type-specific transcripts on a volcano plot in Figure 2A to demonstrate the cell type-specificity of their TRAP experiments. The authors should consider an unbiased and systematic assessment with larger gene sets using gene set enrichment analysis (GSEA), which the authors deployed in other parts of the paper. There are now numerous sources of cell type-specific gene sets for various neuronal and glial cell types from both bulk RNA-seq (e.g. from Barres and colleagues) and single-cell RNA-seq (e.g. from Linnarsson, McCarroll, and others).

8) The authors are requested to clarify how they controlled for possible length biases in their calculations. This is especially important when determining the validity of the observations in Figure 3E. The use of RPKM is valid as long as transcript length is stable (i.e. FMRP is not affecting transcript length).

9) In the section investigating FMRP regulation of circadian rhythm transcripts, the authors should describe the background and cutoffs used in their functional analysis. This section would be strengthened if the authors could address whether FMRP affects the circadian-dependent changes in the expression of these genes by performing RT-(q)PCR and western blotting (as they have in Figure 2D-F).

10) At present it is unclear whether the circadian genes regulated by FMRP are only expressed and/or bound in CA1 or whether such binding occurs in other brain regions important for circadian regulation. It is also unclear whether there are alterations in the rhythmic expression of clock genes in the hippocampus of Fmr1 KO mutants (related to point 9). At present, evidence relies heavily on the behavioural read-outs reported in the manuscript, which can be confounded by various factors affecting behaviours that are independent of FMRP's role in the regulation of circadian genes in the CA1 region. These caveats should be discussed.
