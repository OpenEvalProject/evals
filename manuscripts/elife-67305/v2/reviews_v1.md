# Peer review - Round 1

Editors:
- Torben Heick Jensen, Aarhus University Denmark

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67305.sa1](https://doi.org/10.7554/eLife.67305.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "ZC3H4 restricts non-coding transcription in human cells" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by James Manley as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Joan Steitz (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The manuscript by Estell et al. investigates the impact of the protein ZC3H4 on RNA levels in human cells. The authors first perform a screen aiming at the identification of factors involved in transcription termination, by identifying proteins in the vicinity of Pol II in a WT context compared to the rapid depletion of the Cpsf30 subunit of the cleavage and polyadenylation complex. The poorly characterised paraloguous proteins ZC3H4 and ZC3H6 display reduced signal upon Cpsf30 depletion. These proteins are then depleted, demonstrating that ZC3H4 depletion gives rise to clear alterations in RNA expression profiles. Based on this, and additional bioinformatics analysis, the authors focus on the impact of ZC3H4 on RNA levels at protein coding genes, PROMPTs and enhancers. It is concluded that ZC3H4 acts as a terminator of transcription for the latter two categories of transcription units. The observed effects are then compared to those of the Integrator complex, that also acts as an early transcription terminator at such loci, which leads to the suggestion that these proteins act on different substrates. Moreover, it is determined that ZC3H4 binds chromatin at regions corresponding to the targeted RNAs. Finally, using a reporter system, the authors further show that ZC3H4 targeting to a transcript reduces its expression level.

The identification of a previously uncharacterized factor involved in transcription regulation is interesting. However, the reported results lack in-depth analysis. Most statements are quite general and would benefit from further analyses.

1. ZC3H4 binds to Pol II in a CPSF30-dependent manner. Moreover, ZC3H4 appears to share similar functions with the Integrator complex. Therefore, the relationship between ZC3H4 and CPSF30 on the one hand and ZC3H4 and Integrator on the other would benefit from further elucidation and exploration. For example:

i. Analyze the connection between ZC3H4 and pA sites e.g by measuring whether ZC3H4-sensitive transcripts are enriched for PASs.

ii. What's the exact number of protein-coding genes demonstrating increased downstream transcription upon depletion of ZC3H4, and how are these distinguished from non-sensitive genes? What is the overlap between CPSF30 and ZC3H4-dependent protein-coding genes?

iii. What are the genes included in the metagene analysis comparing the effects of CPSF30 and ZC3H4 in Figure 3B? Are genes that are read-through in the absence of either CPSF30 or ZC3H4 plotted in the Figure? Or is this a metaplot of the 1795 protein-coding genes demonstrating read-through upon CPSF30 depletion as in Figure 1C?

iv. Comparison of INTS1 and/or ZC3H4-dependent protein-coding genes (related to Figure 4G). Are there any characteristics (e.g. GO processes, gene length, PAS/intron density, expression levels, etc) of the genes upregulated upon depletion of INTS1 or ZC3H4 or both?

v. What is the overlap between the non-coding loci (PROMPTs and SEs) affected by depletion of INTS1 or ZC3H4?

vi. Because the performed screen is related to transcription termination and pA site RNA processing, the described effects of ZC3H4 are predicted to be at the level of transcription termination. However, the possibility that ZC3H4 acts on transcription or RNA stability is not addressed. The usage of the DIS3 depleted samples only serves the purpose of mapping exosome sensitive locations.

2. ZC3H4 versus ZC3H6: Providing a sequence alignment of ZC3H4 and ZC3H6 (or the statistics from such an alignment; %identity/similarity) would yield a better appreciation of the similarity between the two proteins. Overall, this whole panel would be more fitting as a supplementary figure.

3. Figure 4: The comparison of RNA-seq and chromatin-seq is not optimal. This is exemplified in panel E where the two controls display different profiles, leading to a strong effect of Ints1 depletion and no effect of ZC3H4 depletion.

4. Figure 5: While affirming the phenotype also upon rapid depletion of ZC3H4 represents an important control, these data do not bring any new information and should probably be considered supplementary.

5. Figure 6: Considering the weak affinity of the ZC3H4 antibody in ChIP, displaying an input track would help estimate the specificity of the signal. In the same vein: To ensure that the peaks presented in the IGV tracks are not background, one could normalize ChIP-seq data to input DNA and plot the tracks as the ratio of ChIP/Input.

6. Figure 7: While the tethering assay nicely demonstrates that recruitment of ZC3H4 negatively regulates the reporter RNA, additional explanation or experiment is warranted. In their discussion of chromatin-associated RNA, it is unclear how the reporter RNA is found in the chromatin fraction? Do the authors mean chromatin formed on the plasmid or the host chromatin? If the latter, how does the reporter associate with the chromatin? Is detection of uncleaved RNA at the BGH poly A site a faithful readout of nascent RNA? ZC3H4 also affects read-through. Can other methods be used to quantify nascent RNA? The tethering experiment should be performed on at least one endogenous target of ZC3H4 (that was upregulated upon its depletion). Does ZC3H4 over-expression rescue the effect of its depletion or is this not sufficient?

7. Clarification of Figures and Figure legends: Despite presenting interesting experiments, the figures require thorough revision to ensure clarity.

a. Please specify the direction of all genes in the IGV browser tracks in a more visible manner.

b. Adequately label all axes and scales (e.g. Figure 1F, 6A-D, 6G). When referring to fold change, specify of what.

c. When presenting normalized data, include a control in the graph even if its set to 1. (eg. Figure S1C; S3A).

d. Figure 1D: Label CPSF30 green.

e. Figure 2A should be supplementary to Figure 1.

f. Figure 3B: How many genes are being plotted?

g. 3E: Where is MYC SE on the track?

h. Figure 5C and S4: Explain the 5´ and 3´ primer probes (e.g. ITPRID2 5´, ITPRID2 3´).

i. Figure 7D: Both bars should be colored red.

8. Discussion: Several paragraphs in the discussion feel disconnected to the findings presented in the manuscript and how they tie in with the current knowledge regarding transcription termination (eg. Lines 382-395). The authors should revise this section to present a stronger argument highlighting the importance of the findings presented in their manuscript.
