# Peer review - Round 1

Editors:
- John Stamatoyannopoulos, University of Washington , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.02626.030](https://doi.org/10.7554/eLife.02626.030)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Multi-species, multi-transcription factor binding highlights conserved control of tissue-specific biological pathways” for consideration at eLife. Your article has been favorably evaluated by Stylianos Antonarakis (Senior editor) and 2 reviewers (Drs Mike Beer and Ross Hardison).

The Senior editor and the reviewers discussed their comments before we reached this decision, and the Senior editor has assembled the following comments to help you prepare a revised submission.

There are several major points that need to be addressed in the revised document (please see below). In addition both reviewers have suggested a reorganization of the display items.

Reviewer 1:

1) A main result is that most CRMs “are evolving rapidly”, but to be precise, what “conserved” means here is that the sequences are not “alignable by EPO.” This is naively in conflict with Figure 1 showing that TFBS are conserved in all species. It seems that the authors have the ability to investigate what is evolving, either: 1) CRM TFBS composition (binding sites evolving in our out), 2) TFBS linear arrangement (binding sites reordered), or 3) CRM-gene association (entire CRMs relocating and losing synteny). Another possibility is that all 3 of these features are conserved, but what is called lack of conservation is simply a failure of EPO alignment to detect the conserved TFBS arrangement and composition. There are computational approaches specifically designed for this case (where PWMs and TFBS are known) which outperform EPO for this task (compared in Su Teichman Down 2010) and something along the lines of Kim, He, Sinha 2009; Sinha, He 2007; He, Ling, Sinha 2010; all in PLOS Comp Bio, should be utilized.

2) Details of CRM construction are too sparse, and it is not very clear what CRM composition is until Supplemental Table 2C, which should be in Figure 1, and numbers of singletons should be added, not buried in the supplementary material. If a CRM changes its TFBS composition across species, but the sequence is alignable, is it still considered conserved?

3) How sensitive are the results to the specific cutoffs used for ChIP-seq signal to quantify a binding event vs. non-event? The analysis should be performed on different replicates to test this. How many CRMs change their composition using only one repl to build them vs. the other? Also, it seems a bit inconsistent to say that the ENCODE quality control standards are used for the replicates if later only the replicate which gives the most peaks is used for downstream analysis. If both replicates don't give similar results, how robust are the conclusions?

4) Motif detection is good, but enrichment should be quantified. The fraction of CRM sequences which have motifs present above some cutoff PWM score for each of the 4 PWMs should be reported for all CRMs and singletons. E.g., how many singleton HNF4A binding regions have a PWM instance above some cutoff, compared to how many singleton sites for the other 3 factors have a HNF4A PWM score above that same cutoff?

Reviewer 2:

The current manuscript is difficult to read and understand. I have several recommendations for revisions, starting with some major re-organization.

1) The logical flow is fairly strong in the Results, but the data referred to are dispersed across many pages of Figures and Figure supplements. Also the order of the main figures does not fit with the presentation in the Results: it really is not used until the third section. I strongly recommend re-organizing the figures. Start with some of the current Figure 1 supplements, specifically Figure 1–figure supplement 3, 4, 5 to show the basic data, and how you constructed the CRMs, and the amount of conservation for TF bound sites and CRMs. Then go to the current Figure 1, which describes how the CRMs are categorized by extent of conservation.

2) Figure 2 and the many supplemental figures have multiple problems. The authors have developed an excellent way of displaying the GREAT results, but they flood the reader with too much information. A better-digested and focused set of key results needs to be featured. The text does have a good focus; however, the text and figures are not closely aligned. The specific examples of significant enrichments in the text are not listed in the main Figure 2, and the reader has to scan through four or five pages of figure supplements to find the data being discussed. One figure highlighting the key enrichments needs to be refined from all this material. Also, the method for assigning likely target genes is not stated in the main text. This is a very important point for interpreting the data, and it should be stated in the Results as well as in the Methods.

3) The description and interpretation of the data in Figure 4 need to be more accurate. The data in panel B are over-interpreted in the legend and in the Results. The expression of presumptive targets is not limited to liver (“uniquely expressed”) but the expression levels are higher there. The text says “Unlike CRMs, conserved singletons do not show a strong increase in liver-specific gene expression.” In fact, presumptive targets of singletons show a similar pattern to the presumptive targets of CRMs, but the levels of expression are lower. Is the decrease in signal for deeply shared singletons significant, or is this related to a small number of targets to examine? Also, the legend should specify the RNA-seq data used in panel A. The top comparison in Figure 4A seems to be between the expression levels of presumptive targets for deeply conserved CRMs and lineage-specific singletons, but it has a surprisingly high p-value; this should be clarified.

4) Figure 6 main and Figure 6–figure supplement 1: The authors are making a critical point but the connections between the text and the Figures are not stated clearly. In the Results, the authors give p-values for enrichment of about 0.005 to 0.008 and refer to Figure 6. However, those p-values are MUCH smaller, and correspond to the analysis in the next sentence, after separation by conservation categories. However, the reader is referred to Supplemental File 4, whereas they really need to look at Figure 6! The fact that the enrichments are robust to different ways of dealing with potentially functional SNPs in proximity or LD is a strong point and accurately stated in the Results. However, the titles to the figure legends (Figure 6 vs. Figure 6–figure supplement 1) are the same, and it takes some careful reading to figure out what is different about the two figures.

5) The Discussion should address what is missed by focusing on only combinatorial binding, only conserved binding, and both. Clearly, many fewer bound sites are examined by doing this filtering, but the enrichment for likely function is substantial. What are the potential costs of taking this approach?

6) I would like to see a paragraph in the Discussion comparing the advantages of filtering vs integration. Are there integrative approaches that would emphasize the features shown to be useful here (combinatorial binding and conservation) while not completely excluding other binding sites?

7) What is the null model for the tests of enrichment for GWAS SNPs in CRMs, singletons (Figure 6)? In previous studies, the null model was restricted to SNPs on the genotyping array that were not associated with a trait but were matched to the trait-associated SNPs in several important ways, e.g. allele frequency, position relative to gene structure, and proximity to the transcription start site.
