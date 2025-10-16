# Peer review - Round 1

Editors:
- YM Dennis Lo, https://ror.org/02zhqgq86 The Chinese University of Hong Kong Hong Kong

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72792.sa0](https://doi.org/10.7554/eLife.72792.sa0)

The authors have described an innovative application of ATAC-Seq for genome-wide analysis of the chromatin state at single myofiber resolution.


---

# Peer review - Round 1

Editors:
- YM Dennis Lo, https://ror.org/02zhqgq86 The Chinese University of Hong Kong Hong Kong

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72792.sa1](https://doi.org/10.7554/eLife.72792.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Application of ATAC-Seq for genome-wide analysis of the chromatin state at single myofiber resolution" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Y M Dennis Lo as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Nora Yucel (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. The majority opinion of the group is that the article would potentially be suitable as a Tools and Resources article in eLife.

Essential revisions:

1) The authors state multiple times that this technique gives good sequencing depth. As such, information should be provided regarding number of high quality reads per sample, and whether replicates were downsampled before peak calling.

2) In Figure 1—figure supplement 1A, the x-axis label is not showing the correct size of the library.

3) Can the authors provide the smfATAC-Seq genome tracks for Myod1 and Myog loci to illustrate the chromatin accessibility changes in uninjured and injured myofibers since these two genes are essential for muscle regeneration?

4) In Line 169, remove redundant "can be" in the sentence.

5) The gene names in Figure 5C are not shown clearly.

6) The authors should consider a deeper analysis of the differential chromatin accessibility peaks (subdivided as promoters and distal regions), including prediction of TFs binding sites and integration with other appropriate datasets exploring epigenetic mechanisms (such as histone marks). In addition, the differential ATAC-seq peaks (mainly the ones overlapping putative promoters) should be combined with similar datasets exploring transcriptional changes and used to better infer gene networks characterizing the experimental groups. For example, by generating smfATAC-seq data from a slow-twitching muscle (Soleus), they could take advantage of available transcriptomic (https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0016807) and proteomic (https://www.embopress.org/doi/full/10.15252/embr.201439757) datasets.

7) Chromatin accessibility analysis in satellite cells was performed by isolating cells from the mouse hindlimb. However, these data were compared to the smfTAC-seq from EDL myofibers. The authors should acknowledge the limitation of this comparison.

8) If the authors intend for smfATACSeq to be performed broadly, it might be helpful to put it on a resource like https://www.protocols.io/ for other researchers to easily use and add notes.

9) It would be valuable to systematically compare enrichment at non-myogenic promoters to emphasize the myonuclear enrichment. This could be shown by overlaying TSS enrichment plots for genes that are characteristic of myogenic, vs immune vs vascular cells.

10) Total skeletal muscle ATAC-Seq has been previously published (Ramachandran, et al., PLoS Biology, 2019) in a variety of skeletal muscle types (including EDL vs soleus). How does smfATAC data compare to this ATACSeq data-- in particular are EDL-specific peaks also observed?

11) The authors should include motif analysis of differential chromatin regions (uninjured vs injured, mdx vs WT, using unchanged regions as background). The authors state (line 341) that "Despite the increase in chromatin accessibility during injury, the accessible chromatin regions in both injured and uninjured fibers are associated with genes involved in similar biological processes." Motif analyses may in this case more be informative than GO, and could identify transcription factors with differential activity in the various experimental conditions.

Reviewer #1 (Recommendations for the authors):

1) The authors claim that the smfATAC-seq provides a high sequencing depth that allows for peak calling and differential peak analysis. Can the authors provide the exact sequencing depth in the method section?

2) In Figure 1—figure supplement 1A, the x-axis label is not showing the correct size of the library.

3) The concordance of the smfATAC-Seq data does not seem very good. In Figure 3, only 2 replicates are provided for uninjured fibers and they seem entirely separate. In Figure 6D, WT fibers also do not cluster very well. The authors should provide more replicates for the same condition to show the reproducibility of the approach.

4) In Figure 3F, there are very few unique peaks in uninjured fibers compared with MuSCs. Does it mean the uninjured fibers are less accessible than MuSCs, or is it due to the different nuclei number input for ATAC-seq? This comparison is not simple and the authors should use the same nuclei number input for different samples.

5) Can the authors provide the smfATAC-Seq genome tracks for Myod1 and Myog loci to illustrate the chromatin accessibility changes in uninjured and injured myofibers since these two genes are essential for muscle regeneration?

6) In MDX mice, the myofibers undergo regeneration and degeneration cycles. Currently, the authors only compare the uninjured WT myofibers and the MDX myofibers. Can the authors also provide a detailed comparison between the CTX injured myofibers and the MDX myofibers to illustrate the difference in the chromatin accessibility profiles of the two conditions, if any? Alternatively, when is the peak of regeneration and degeneration cycles during the life of an MDX mouse? Again, the current study lacks depth and shows no biological insight.

7) In Line 169, remove redundant "can be" in the sentence.

8) The gene names in Figure 5C are not shown clearly.

Reviewer #2 (Recommendations for the authors):

The authors should consider a deeper analysis of the differential chromatin accessibility peaks (subdivided as promoters and distal regions), including prediction of TFs binding sites and integration with other appropriate datasets exploring epigenetic mechanisms (such as histone marks).

In addition, the differential ATAC-seq peaks (mainly the ones overlapping putative promoters) should be combined with similar datasets exploring transcriptional changes and used to better infer gene networks characterizing the experimental groups. For example, by generating smfATAC-seq data from a slow-twitching muscle (Soleus), they could take advantage of available transcriptomic (https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0016807) and proteomic (https://www.embopress.org/doi/full/10.15252/embr.201439757) datasets.

Reviewer #3 (Recommendations for the authors):

The authors have done a good job in demonstrating data quality, and making it available through GEO. The methods are also quite clear. If the authors intend for smfATACSeq to be performed broadly, it might be helpful to put it on a resource like https://www.protocols.io/ for other researchers to easily use and add notes. Other specific points in no particular order:

– In Figure 3B PCA is done on MuSCs vs uninjured vs injured fibers. It looks like the MuSCs are driving the differences in PC1, perhaps compressing the differences in fibers. Does injury segregate samples by PCA when the MuSCs are removed? On a similar note, in figure 6D, if injured fibers are included in the PCA along with mdx fibers (normalizing for what I assume are different sequencing preparations), are they intermediate to the mdx fibers, as stated in lines 384-386?

– It would be valuable to systematically compare enrichment at non-myogenic promoters to emphasize the myonuclear enrichment. This could be shown by overlaying TSS enrichment plots for genes that are characteristic of myogenic, vs immune vs vascular cells.

– Total skeletal muscle ATAC-Seq has been previously published (Ramachandran, et al., PLoS Biology, 2019) in a variety of skeletal muscle types (including EDL vs soleus). How does smfATAC data compare to this ATACSeq data-- in particular are EDL-specific peaks also observed?

– The authors should include motif analysis of differential chromatin regions (uninjured vs injured, mdx vs WT, using unchanged regions as background). The authors state (line 341) that "Despite the increase in chromatin accessibility during injury, the accessible chromatin regions in both injured and uninjured fibers are associated with genes involved in similar biological processes." Motif analyses may in this case more be informative than GO, and could identify transcription factors with differential activity in the various experimental conditions.

– The authors state multiple times that this technique gives good sequencing depth. As such, information should be provided regarding number of high quality reads per sample, and whether replicates were downsampled before peak calling.
