# Peer review - Round 1

Editors:
- Ronald N Germain, National Institute of Allergy and Infectious Diseases , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.10134.049](https://doi.org/10.7554/eLife.10134.049)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Affinity and Dose of TCR Engagement Yield Proportional Enhancer and Gene Activity in CD4+ T Cells" for peer review at eLife. Your submission has been favorably evaluated by Tadatsugu Taniguchi (Senior editor), a Reviewing editor, and three reviewers.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Your paper has been seen by a Reviewing Editor and three expert referees. While all believe that the topic is of importance and that the data sets you have generated are of substantial value to the field, there are major concerns about the core conclusions of your study that prevent the paper from being accepted in its present form. Because all the reviews contain important comments and specific requests for new studies, in two cases to clarify the central issue of how T cells respond to various strengths of stimulation (variation per cell in response or variation in the fraction of responding cells) and in another to strengthen the genomic/epigenetic analyses, we have included these reviews verbatim rather than in the usual eLife integrated format.

If new experiments and data can be generated to address these issues and a revised paper submitted within the 2 month-window permitted by eLife policy, it will be reviewed as a revised submission. If the new work and resubmission takes longer, the paper will be considered a new paper, but we will endeavor to have the same individuals examine the new manuscript to provide consistency in the evaluation process. It may be helpful to address a letter to the Senior Editor addressing what you believe you can achieve in a reasonable length of time to address the criticisms raised by the reviewers.

Reviewer #1:

In this manuscript the authors use a well-studied model system in which primary mouse CD4+ T cells expressing the transgenic AND TCR are stimulated with antigen presenting cells presenting pigeon cytochrome c (PCC) or variant peptides with a range of affinities for the TCR. While several aspects of T cell activation have been described as digital or analog, the authors contend that this dichotomy is too simple. They show at a single time point that the MFI of CD69 and CD25 of responding cells correlated with the relative strengths of TCR stimulation. To determine how titration of ligand affinity affected the transcriptional responses, the authors used RNA-seq and principal component analysis to identify a subset of "activation signature genes" which responded in a graded manner to peptide affinity and dose. ChIP-seq was used to compare the extent of epigenetic tagging of enhancers and showed that the degree of H3K4me2 tagging of activation signature genes increased in a graded manner in response to changes in TCR stimulation strength. Motif analysis also revealed that enhancers that became more active with TCR signal strength were enriched for AP-1 and NFkB sites. To determine how this subset of activation signature genes responded to perturbation of the Ras/Raf/Mek/Erk pathway, the authors performed ChIP-seq analysis on T cells stimulated with partial Mek inhibition. Consistent with the top 10% of PC1 genes having a bias toward genes containing AP-1 sites, the activation signature genes were appreciably more susceptible to Mek inhibition than the bottom 10%. The authors conclude that the ERK pathway is responsible for translating varying strengths of TCR stimuli into similarly graded enhancer activity.

In this article the authors raise an important question. However, the conclusions drawn in this study, while plausible, lack sufficient supporting experimental evidence.

1) The major design flaw of the RNA-seq and ChIP-seq experiments is that the source RNA or DNA analyzed was pooled from an entire population of stimulated cells (including for example both CD69- and CD69+ cells). As a result, it is not possible to determine whether the graded gene expression/epigenetic changes occur due to graded responses homogenously in every cell, or due to decreasing frequencies of responding cells as the affinity of stimulating peptide is decreased. In Figure 1 the authors demonstrate this heterogeneity at a single cell level that decreasing the potency of TCR stimulus decreases the frequency of cells that express CD69 and CD25. This is not to say that there may be graded responses amongst the responding cells. The data generated by flow cytometry in Figure 1 and Figure 6A demonstrate that the MFI of CD25, CD69 and phospho-ERK can be dose dependent, when gated on the responding cells. One should note, however, that they only do their flow analysis at a single time point and it is not clear that maximal responses have been reached at lower doses of peptides or with weaker peptides. Regardless, however, RNA-seq and ChIP-seq analyses on bulk populations cannot formally discriminate whether the signals detected come from each cell equally or from a subpopulation of cells. A more informative experiment would involve sorting the CD69+ cells after stimulation with varying concentrations/affinities of peptide, and then performing RNA-seq or ChIP-seq.

2) The Abstract and the Discussion imply that ERK activation is the predominant pathway that accounts for inducing graded enhancer activity. However, this ignores other known pathways that are likely to contribute to activation signature gene transcription, such as NFAT and NFkB. Indeed, NFkB sites appeared to be enriched in the activation signature genes as well (Figure 4E).

Reviewer #2:

Understanding how T lymphocytes respond to antigens of varied doses or quantities remains a critical issue in immunology. Indeed, much biochemical effort has been focused on the first minutes of T cell activation (e.g. biophysics of TCR/pMHC interaction, or dynamics of signaling response or synapse formation). In these settings, T cell activation (as measured by NFAT translocation or ERK phosphorylation among others) was found to be essentially digital, with the frequency of cells getting activated increasing with increasing doses or increasing quality of antigens. On the other hand, the typical degree of activation (amongst activated cells, as measured by the mode of ppERK or NFAT activation) was found to be essentially constant on short timescale (e.g. t<30min), although recent work in the EGFR pathway argued for frequency encoding of activation strength (Albeck et al., 2013). T cell activation and regulation of immune responses occur over longer timescales (> hr): this opens up opportunities for T cells to register, in an analog manner, quantity and quality of antigens, while short-term responses were essentially digital.

In this article, Allison et al. report that early cellular markers of T cell activation (e.g. CD25 and CD69 upregulation) are indeed bimodal yet, the mode of protein abundances amongst activated T cells tracks the strength of antigen stimuli (quality and quantity). Subsequent analysis tracks alterations in the landscape of epigenetic marks to demonstrate their correlation with the strength of antigenic stimulation.

One key issue in this study is that changes in the amplitude of response amongst activated cells (analog mode) occur concomitantly with changes in the frequency of cells getting activated (digital mode), for different antigen strength (cf Figure 1). The authors argue that the dominant mode of regulation is the amplitude of signaling amongst activated cells. This conclusion is supported qualitatively by the application of MEK inhibitors (Figure 6), although the authors fail to report that the impact of MEK inhibition is solely on the mode of ERK phosphorylation and not on the frequency of T cell activation. Yet, most outputs are measured in bulk (e.g. by sequencing of a population of sorted cells) except for Tbet and Irf4 (Figure 2). Thus changes in gene regulation may be dominated by the changes in frequency of activated cells rather than by changes in the modes of activated cells. Overall, a direct quantitative test of this observation is not carried out: changes in frequency of activated T cells and mode of gene upregulation are confounding consequences of antigenic activation that must be better deconvolved at the individual cell level.

The paper also makes a strong case about the ability of T cells to register the strength of antigenic stimuli in terms of gene regulation. Using publicly available data and new datasets acquired in-house, the authors derive a gene signature that encompasses the dominant mode of variation of gene up/down regulation in T lymphocytes. Surprisingly, a single score derived from a simple principal component analysis is shown to encompass almost completely the variability of T cell gene regulation (at homeostasis or under activation). Moreover, this PCA score is shown to report back the strength of activation in different settings (with/without costimulation, with/without involvement of Trim28 etc.): this result is striking as it implies that T cell activation can be quantified as the sum of input signal -a similar result was recently reported by the Hodgkin group (Marchingo et al., 2014). The results and analysis presented here by Allison et al. in terms of gene regulation is very exhaustive and adds to our quantitative understanding of T cell activation.

Allison et al. also report that constitutive levels of activation amongst CD4+ T cells (isolated from different mouse strains) vary dramatically and a hierarchy among them can be established based on the universal PCA score derived from T cell activation. This is an interesting observation that would require further investigation: does it imply stronger or weaker responsiveness to antigen stimulation? This issue of potential tuning to constitutive TCR stimulation is long standing (Mandl et al., 2013), and possibly beyond the scope of this study. Still, a more quantitative analysis is warranted to test the strength of this quantitative correlation e.g. using partial least square regression to identify the latent variables (antigen quantity and quality, frequency of response, mode of response) that best account for the measured variability in gene output (Kemp et al., 2007).

Overall, this study reports interesting observations related to quantitative aspects of T cell activation in terms of global gene regulation. Additional effort to rigorously quantify the impact of antigen strength would help deconvolve how frequency and mode of activation impact overall gene regulation at the individual cell level.

References:

Albeck, J.G., Mills, G.B., and Brugge, J.S. (2013). Frequency-modulated pulses of ERK activity transmit quantitative proliferation signals. Molecular cell 49, 249-261.

Kemp, M.L., Wille, L., Lewis, C.L., Nicholson, L.B., and Lauffenburger, D.A. (2007). Quantitative network signal combinations downstream of TCR activation can predict IL-2 production response. Journal of immunology 178, 4984-4992.

Mandl, J.N., Monteiro, J.P., Vrisekoop, N., and Germain, R.N. (2013). T cell-positive selection uses self-ligand binding strength to optimize repertoire recognition of foreign antigens. Immunity 38, 263-274.

Marchingo, J.M., Kan, A., Sutherland, R.M., Duffy, K.R., Wellard, C.J., Belz, G.T., Lew, A.M., Dowling, M.R., Heinzel, S., and Hodgkin, P.D. (2014). T cell signaling. Antigen affinity, costimulation, and cytokine inputs sum linearly to amplify T cell expansion. Science 346, 1123-1127.

Reviewer #2 (Additional data files and statistical comments):

Better statistical tests to deconvolve frequency and mode of activation and their impact on gene regulation are warranted.

Reviewer #3:

In this study, Allison et al. characterize gene expression and histone modifications in CD4+ T-cells subjected to varying levels TCR engagement. The authors use PCA to identify an "activation gene signature" and define an "activation score", concordant with traditional measures of T-cell activation level, and use their enrichment score to re-analyze existing data sets. They also use this approach to analyze the consequence of TCR activation in different mouse strains. They find antigen concentration-dependent variation in histone modification (H3K27ac, H3K4me2) near activation signature genes. Finally, the authors find that MEK inhibition specifically reduces the expression of activation genes. The authors conclude that whereas TCR engagement can be viewed as a digital signal, the ERK pathway translates TCR activation to graded gene activation.

The manuscript reports one of the first genome-wide studies of transcriptional regulation in response to varying levels of stimulation coupled with associated epigenetic changes. As such, this will be of interest to both the T-lymphocyte and broader transcriptional regulation communities, and will also be a useful resource for future investigation. However, there are a number of issues that should be resolved.

For many of the authors’ observations, the authors should present a control where expression levels (or fold-change upon stimulation) are considered. For example, when comparing properties of the top 10% vs bottom 10% of PC1 genes (e.g., histone modification levels, super-enhancer levels, or the effect of MEK inhibition), an alternative to the authors' conclusion that activation signature genes are functionally distinct from non-activation genes is that these features are simply proportional to expression level. Another example of this potential confounding effect is the AP-1 motif frequency in the top-10% vs. bottom-10% of PC1 genes – this might reflect expression level.

To account for differences in expression level, the authors could sample from the set of top and bottom activation genes such that their distributions of expression levels match, and then compare the genomic features between these expression-controlled samples. Some of the reported effects arise from differences in expression level and that some of the authors' observations recapitulate well-established relationships between histone modification levels and expression levels.

In principle, the activation score could be a useful tool; however, what is the evidence that the activation score is a more accurate measure than expression levels of individual well-established activation markers (e.g. CD69, CD25, etc.)? In what way is it superior to these other markers?

Why is a T-cell-specific ontology term not found in the "activation gene signature"? What are the terms enriched in the bottom 10% of activation signature genes? The details of the ontology search should be clarified: did the authors compare annotations of the top-10% to those of the bottom-10% genes? or top-10% genes vs. all genes – in which case there will of course be a bias towards T-cell function because they imposed a minimum expression threshold (10 RPKM) before performing PCA to select signature genes. The authors should also provide sufficient details about the specific random model used whenever they describe a p-value to assess the significance of an observation.

It is well-appreciated in the T cell activation literature that peptide concentration influences Th1/Th2 skewing (e.g. Rogers and Croft, 1999). It is curious that the authors did not choose to examine this outcome. Were "Th2" genes preferentially enriched with low-dose, low-affinity peptides? Likewise, some mouse strains are more Th2-ish than others. Was this evident in the transcriptomes?

The strategy to isolate naïve T cells is problematic. It's not a problem generally since TCR transgenic mice are used. However, it probably is a problem for the experiment shown in Figure 3E. This experiment may very well reflect contaminating memory cells. Presumably, these represent cells directly analyzed following isolation. The authors should show their isolation technique results in a truly naïve population of cells.

It is not clear from the Methods how many replicates were obtained in RNA-seq and ChIP-seq experiments. In general, the figure legends and Methods should more clearly state the replicates and independent experiments performed.

The histone ChIP-seq experiments refer to "across the five conditions". Presumably this refers to unstimulated cells and the two concentrations of the two peptides. However, the preceding figure includes lots of conditions; this will be confusing for readers. There is no presentation of global data depicting responses to both peptides and doses. More information on numbers of peaks, quality control and overlap (Venn diagrams etc.) would be of interest.

Readers may find Figure 4E confusing. The text refers to AP1 motifs and the figure depicts BATF. BATF, of course, is a member of the AP1 family; however, not all readers may immediately understand this. The figure legend is clear, but the text may still be confusing. The text also tacitly equates AP1 and Batf, but this is obviously not the case. Fos/Jun are players in TCR signaling. It is understandable that the authors have used existing Batf ChIP-seq data, but other AP1 family members undoubtedly contribute to activation.

Figure 4H is also confusing. Readers may not understand right away that the legend indicates solid and dashed lines. It is an important piece of data, so the authors should make it easier for readers to get this right away. The choice of colors is also confusing (purple refers to Batf and CTCF). This figure is more complicated than it needs to be. Is 0.1 μm PCC used? Is 1 μm PCC not used in Figure A? The authors should check all the figures for labeling errors, e.g.: Figure 1A,B: green 100 μm curve is labeled PCC instead of K99A. Figure 1E: x-axis labels are missing decimal points. The choice of CTCF is also of interest, insofar as one would not necessarily expect that it would be a TF that would be responsive to graded signals.

Other points:

In Figure 2F it would be desirable to show both MFI and% positive cells. Given the effect of peptide concentration on Th1/Th2 skewing, showing GATA3 as well might be illuminating.

Figure 5 – more explanation of Pleckstrin homology genes and the potential relevance to T cell activation is warranted.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Affinity and Dose of TCR Engagement Yield Proportional Enhancer and Gene Activity in CD4+ T Cells" for further consideration at eLife. Your revised article has been favorably evaluated by Tadatsugu Taniguchi (Senior editor), a Reviewing editor, and three reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Two of the reviewers felt that some primary data were needed to help the readers evaluate important new studies now included in the revised manuscript. There were also some important discussion issues that should be addressed.

Reviewer #1:

In the original manuscript by Allison et al., a major experimental design flaw pointed out by two reviewers was that the source material for the RNA-Seq and ChIP-seq data studies was from a mixed population of responding (CD69+) and non-responding (CD69-) T cells, rather than a purified population of responding (CD69+) cells. In the revised manuscript, the authors have added new experimental data that address this major concern. Figure 3A shows graded expression of a single example, Irf4 transcripts, amongst the CD69+ cells that respond to APC/peptides of varying affinity, and the rest of Figure 3 shows RNA-Seq data from the CD69+ cells sorted from a bulk population of activated T cells. The results of both approaches are consistent with the authors' conclusions that there can be graded transcriptional signatures on a per-cell basis. Whereas the RNA-Seq data largely satisfy this concern, there is still some uncertainty about the results presented by the RNA-flow in Figure 3A. The authors should include data in the figure for some "loading control" type controls, or alternatively, other examples. Specifically, the concern is whether most or all transcripts exhibit a similar pattern (graded, and increases with increased peptide affinity) using this technique, which is relatively new and not yet widely used in the field.

Two other concerns about the manuscript that could be addressed in the Discussion:

1) The authors should discuss the work in Huang et al., 2013 a bit more in which the Davis lab showed that single T cell engagement of different numbers of identical peptide agonists (titration of signal strength) resulted in digital responses read out as increasing numbers of T cells producing the same amount of cytokine. Different levels of responses were seen when naïve cells were compared with blast cell responses – at the single cell level.

Second, the authors seem not to have considered different temporal responses. Analysis at a single time point eliminates the potential for the cumulative effects of weak signaling, particularly if there is asynchrony in the population. Strong signals tend to be more synchronous.

Reviewer #2:

This resubmission includes an additional set of experiments that goes a long way towards addressing the previous reviews. The authors use RNAseq on activated/sorted T cells to demonstrate that gene regulation does scale with TCR activation, even within cells that are activated.

The authors attempted to resolve the issue of digitalness/analogness of the response by performing RNA flow cytometry (e.g. measuring IRF4). It reads like the dynamics range and signal-to-noise ration of detecting irf4 mRNA was insufficient to rule out bimodality. Still the trick of sorting and analyzing single cells does go a long way towards establishing the ability of activated T cells to scale their response to the strength of antigen activation.

I would recommend that the histograms or cumulative distribution function for irf4 mRNA should be presented to let readers assess the lack of bimodality. I am surprised that the 10 fold increase (between activation with no peptide activation or with PCC at 10µM – Figure 3A) is not sufficient for resolution.

I appreciate the care and additional work carried out since the last submission.

Reviewer #3:

The revised manuscript satisfactorily addresses my concerns.
