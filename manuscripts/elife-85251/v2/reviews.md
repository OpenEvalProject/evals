# Peer review - Round 1

Editors:
- Patrik Verstreken, https://ror.org/05f950310 KU Leuven Belgium

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85251.sa0](https://doi.org/10.7554/eLife.85251.sa0)

Wu et al. have provided a revised manuscript that presents important new findings that start to explain cell type vulnerability and the types of transcriptional changes that occur in the context of neurodegenerative diseases. They cleverly use Drosophila for this as they have access to numerous brain cells and exquisite genetic control. They present compelling evidence of transcriptional deregulation and affected pathways in relation to Tau toxicity in a well-controlled study. They also tested if affected pathways modify toxicity but were not successful, however, as pointed out, this can have different reasons. This paper is of broad interest to those in the field of neurodegeneration and neuronal disease and from a methodological point of view to single-cell biologists.


---

# Peer review - Round 1

Editors:
- Patrik Verstreken, https://ror.org/05f950310 KU Leuven Belgium

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85251.sa1](https://doi.org/10.7554/eLife.85251.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Tau polarizes an aging transcriptional signature to excitatory neurons and glia" for consideration by eLife and please accept our apologies for the longer than usual reviewing time. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Claude Desplan as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Simon G Sprecher (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Given that all vulnerable cell types were already lost at day 1, the reviewers were unclear whether the model assesses age-dependent neurodegeneration. This may also be developmental toxicity. There should be a balanced discussion on this or alternatively, data could be included making use of models that show defects only at older age.

2) There were some concerns about genetic background (cf rev 1) and controls (cf rev 2): ie is there a possibility to include wt-tau or carefully discussing this; likewise, given the depth of analysis one achieves with single cell seq approaches, genetic background issues can be real confounding factors. Was this addressed in the experimental design.

3) The finding of involvement of the NFkB pathway is interesting, but causality has not been shown. All reviewers thought it would be rather simple to put the idea to test by genetically modulating this pathway and assessing if neuronal loss is rescued.

4) the last comment by reviewer 2 was also deemed important. The comparison between species and of an FTD-Tau mutation with AD needs to be toned down.

5) the other issues can likely be addressed by textual changes or added discussion.

Reviewer #1 (Recommendations for the authors):

I have these points that would improve the paper:

– Can the authors test whether the neuronal loss in their model is due neurodegeneration rather than developmental toxicity to tau.

– Given that they find the NFkB pathway to be involved in tauopathy in a model organism, it would be fascinating if they put this idea to test and show causality by genetically modulating this pathway and rescuing neuronal loss.

– Can the authors please mention the genetic background of all lines used in the Methods. Where UAS-tau and the wild-type fly that was crossed to elav-Gal4 to serve as a control in the same genetic background?

– The authors should include in the counting step whatever 3' UTR the tau transformation vector had that was used for generating the fly model, since the fast majority of reads should map there rather than in the tau sequence. For now, it seems that NM_016834.5:151-1302 (Methods) represents the CDS.

– Figure S6B and S10D are missing a quantification. In addition, for 10D it would be helpful to add a negative control to see how specific the signal is, such as a control fly without the endogenous GFP tag.

– It is interesting that glia seem to react strongly to tau. However, it is not clear whether this is cell autonomous – because they also express tau – or as a reaction of the neuronal tau expression. Is the promoter they use neuronal and would we expect any expression in glia? Can they maybe add a panel to Figure S8 with a boxplot showing tau expression levels in glia cell types and neurons.

– It is interesting how the authors find multiple regulons (some with >2x larger coefficients than the Rel regulon) to be associated with the degree of vulnerability. For the curious reader it would be helpful to at least point them out and briefly mention the underlying biology.

– Why were in Figure S7 KEGG pathways only annotated for few cell types. This should be explained in legend or annotated more widely, e.g. in all cell types that are lost.

– In Figure S9B not all cell-types shown. Does this mean that no pathways were found in those, maybe they could add this to the legend? And why are the KEGG terms in Figure S7B for a'/b'-KC different than in S9B?

Also a typo is in this legend: 'including pathways that are actively in cell-type specific vs. more global patterns'

– Figure S8 should add whether this is counts or log-scale.

– Figure 4D can the authors add explicitly whether this is control and tau cells pooled?

Reviewer #2 (Recommendations for the authors):

Wu et al. conducted longitudinal single-nucleus RNA sequencing in a Drosophila transgenic line expressing pathogenic tau (Arg406 ->Trp) and control to study presenile degenerative dementia with bitemporal atrophy. Their data is consistent with previous findings on Tau neurotoxicity, which significantly affects excitatory neurons in human brain samples and transgenic mice. Intriguingly, intracellular transgenic Tau induced strong transcriptional signatures, aging-like signatures, and an innate immune response, including the NFKB pathway, in the transgenic animals. This dataset provides a valuable resource for exploring dynamic, age-dependent gene expression changes at a cellular level. The authors propose that innate immune signatures may serve as predictors of neuronal subtype vulnerability in tauopathies. However, the observed skewing of cell proportions in day-1 animals necessitates stronger evidence to support this hypothesis, which is currently lacking in the manuscript. The paper is primarily descriptive and lacks mechanistic insights. Furthermore, the identified pathways/genes presented in the paper lack orthogonal validation.

1. About the controls: Authors compared Tau transgenic line (Arg406 ->Trp) with the control (GAL4 expressing animals) but not with wt-tau line. They may potentially lead to misinterpretation. Although Wittmann et al. 2001 noted toxicity when wt-tau is expressed, the toxicity is much less compared to Tau transgenic line. Or would another alternative be to use mutant tau animals lacking aggregation-prone regions?

2. It is striking to see the drastic cell proportion changes on day-1 (figure 2B), which may reflect the deficits in neuronal development. Did authors check the expression of transgene expression levels across neuronal subtypes to make sure the vulnerability is not due to a difference in the Tau transgene expression?

3. Figure 2B-D, although authors admit that the difference is likely due to the "increase in glial cell abundance from scRNAseq is likely a consequence of proportional changes in single cell suspensions due to neuronal loss," is there a way to quantitatively assess this? Especially authors know the amount of neuronal loss and increase in the glial cells through scRNAseq.

4. Line 204-205, authors claim, "93% of tau-induced differentially expressed genes were also triggered by aging in control flies". However, figure 3A does not reflect the 93% similarity. There are more DEGs in age-specific conditions compared to the Tau. The same holds true for the Figure 2B. Moreover

5. Figure 2B, the number of DEG in cluster Lai and Kenyon cells is highly skewed in the Tau transgenic lines. I find it is intriguing to see high number of DEGs in the cells that are degenerating. Since these plots don't tell much about whether they are up or down, it would be good to mention what proportion of the genes are up and down.

6. The authors claim that among non-neuronal cell types, ensheathing glia, cortex glia, astrocyte-like glia, and hemocytes have the highest number of tau-driven DEGs, but this is not clear from the UMAP in Figure 3C. Additionally, Figure 3C lacks a scale bar, making it difficult to interpret and compare the figure with Figure 3B.

7. In line 249, the authors claim 90% concordance with previously published datasets, but the data representing this is missing in the paper. Additionally, performing DEG with pseudo-bulk from different clusters and performing DEG to find the concordance may not be very informative. For example, did the authors find consistent gene signatures per cluster when compared with previous datasets? This data should be provided.

8. Authors have created an excellent data resource, and it would be interesting to explore the resilience of inhibitory neurons or the vulnerability of excitatory neurons to gain more insights into the cell-type-specific vulnerability or resilience mechanisms. The authors should present a couple of volcano plots showing the differentially expressed genes between important clusters, such as LAI, Kenyon cells, ensheathing glia, etc.

9. It would be beneficial for the authors to explore these pathways in greater depth and perform further experimental validation to strengthen the findings using orthogonal approaches. For instance, a rescue experiment where NFKB/Relish is knocked out to see if this modifies Tau toxicity.

10. In Figure 5, the authors compared cell-type-specific transcriptional signatures between human Alzheimer's disease (AD) and Drosophila. However, some readers may find this comparison difficult to comprehend as the two species differ vastly. Moreover, the Tau mutation that the authors investigated is not associated with AD. Also, in AD, amyloid pathology significantly drives gene expression in immune cells, which is absent in Drosophila. Authors should consider taking the relevant dataset derived from the Arg406 ->Trp patients or from the iPSC-derived cells to validate the observations.

Reviewer #3 (Recommendations for the authors):

As mentioned above, I feel this is an elegant and nicely described study. It provides a further example of the power of single-cell transcriptomic to assess disease genes, showing that in such a fashion one can assess the impact of cell-types, but also the actual genes that are altered. It also shows that the findings can be transferred to patient tissue, thus integrating previous published human sc-data.

There are a few points that I feel might be important to take into account.

– The authors show that ratios of cells are changed in response to tau-GOF, however no explanation is given. What is the basis of this alteration? Cell-death, changes of differentiation/proliferation (it seems the GOF is throughout development in "elav" cells).

– The integration and comparison of fly/human data is a bit short, I could not follow the process of how this was achieved, what framework the authors used etc.

– Conceptually, I think it is nice to see the in-silico analysis of the tau-GOF and aging, however I feel some in vivo validation might have been beneficial to support the claims of affected cell-types and differential expressed genes.

While I fully agree that an extensive genetic analysis may be beyond the scope of the current paper, a proof-of-concept analysis would have been supportive of the validity of the data.
