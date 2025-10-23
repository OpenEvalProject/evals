# Peer review - Round 1

Editors:
- Joaquín M Espinosa, University of Colorado at Boulder , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.09225.010](https://doi.org/10.7554/eLife.09225.010)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled “A simple method for generating high‐resolution maps of genome wide protein binding” for peer review at eLife. Your submission has been reviewed by James Manley (Senior editor) and a Reviewing editor. We feel the work as it stands is not yet fully developed to a level that we could consider for publication as a Research Advance in eLife. However, if you are able to address these concerns with additional data and significant revisions of the text to include more detail, we would be prepared to consider a resubmission on this topic that would be evaluated by the same editors.

The authors present modifications to the widely used ChIP-seq technique as a new method entitled X-ChIP-seq. These modifications simply involve the addition of a micrococcal nuclease digestion step to reduce background DNA fragments and a size-selection step to enrich for short fragments prior to sequencing. It is claimed that these modifications both greatly reduce background and increase resolution, relative to conventional ChIP-seq.

The authors highlight the simplicity of their modifications and bioinformatic analysis relative to other recent modifications to ChIP-seq such as ChIP-exo and ChIP-nexus, making this of interest to the field. The authors aim to show the superiority of X-ChIP-seq through limited comparisons to other datasets (such as conventional ChIP, ChIP-exo, 3'NT, and DNaseI footprinting).

The major areas of concern are:

1) The claim that X-ChIP-seq provides “near base-pair resolution” is not convincingly supported and several of the comparisons with other datasets are incomplete (as detailed below), making it difficult to directly compare the X-ChIP-seq data with other techniques.

2) There is a severe lack of information provided on methods used for the processing and analysis of sequencing data. This makes it difficult to verify the validity of methods used and does not support the claim of “simple bioinformatic processing”.

Main text, first paragraph: Clarify the reasoning/evidence that this is “near base-pair resolution”? This is not clearly established in Skene et al. 2014 and is not readily apparent from Figure 1; Although the positioning in Figure 1B looks different from conventional ChIPseq, the width (resolution) of the peak looks very similar; Are the authors arguing that it is higher resolution because it is a closer match to the 3'NT data which is nucleotide resolution? (This should actually be called accuracy).

Related to Figure 1: Would it not be better to demonstrate the resolution if this technique at a single locus (rather than averaging all TSS) and/or with a DNA-binding protein that has a more defined position on DNA? See Figure3 CTCF.

What do ChIP-exo and ChIP-nexus look like for PolII?

Figure 1–figure supplement 1: It would be very helpful to show end positions for 1st reads of X-ChIP input for comparison. This would allow for clear demonstration of any reduction in of bias. Also, it is unclear if this analysis uses reads aligned to both strands; this could change interpretation of lower half of figure; left shift of + strand reads would correspond to a right shift of - strand reads. How would this affect the plots?

Main text, third paragraph: How would adding this step alter conventional ChIPseq? I.e. what fraction of reads from conventional ChIPseq are within these size ranges and what happens to resolution/accuracy when only these are analyzed? Again there is insufficient comparison between new and old technique. This is important for demonstrating an improvement and/or less bias.

Main text, fourth paragraph: clarify “unbiased approach” (at least in Methods) How many sites were used? What was their average size etc. (some of this information is in Figure 3 legend). Give source for DNase data.

Main text, fourth paragraph: clarify or show data to support the claim that “shorter fragments gave the highest resolution and smallest range in peak widths”; Again this would be better supported with a comparison of both X-ChIP-seq and conventional ChIP-seq (at least by bioinformatically selecting shorter insert sizes).

Main text, fifth paragraph: Clarify “achieve single nucleotide resolution” and comment on offset between the two techniques.

Main text, last paragraph: It would be helpful to see more analysis of low background as in many cases (i.e. transcription-related proteins that do not directly bind DNA) this could be as important as the claimed increase in resolution.
