# Author response - Round 1

Authors:
- Alison G Cole ([ORCID: 0000-0002-7515-7489](https://orcid.org/0000-0002-7515-7489))
- Tamar Hashimshony ([ORCID: 0000-0002-4786-838X](https://orcid.org/0000-0002-4786-838X))
- Zhuo Du ([ORCID: 0000-0002-6322-4656](https://orcid.org/0000-0002-6322-4656))
- Itai Yanai ([ORCID: 0000-0002-8438-2741](https://orcid.org/0000-0002-8438-2741))

## Response text

DOI: [10.7554/eLife.87099.3.sa5](https://doi.org/10.7554/eLife.87099.3.sa5)

The following is the authors’ response to the original reviews.

Reviewer #1 (Recommendations For The Authors):

1. In general given several of the "equivalence groups" were distinguished from each other in Packer et al's annotation, can the authors comment more on why they aren't able to distinguish them? Are the markers listed for those cell states in Packer not expressed appropriately in these data? Or are they expressed but the states are not different enough to form discrete clusters? I suggest the possibility that the analysis choices of 20 "initial dimensions" or 1000 most variable genes filtered out some of these differences which may be encoded in later principle components, or that the use of t-SNE projection is not sufficient to resolve these distinct states.

1. I was a bit confused by the spatial gene expression analysis. Several distinct ideas appear to be posed in the text. These ideas aren't really supported by any quantitative analysis, just the visual patterns in Figure 4B/C which I'm not sure I always agree with.

For example, ceh-43 expression is mentioned as having "physically proximate" expression. But it is well established that different lineages form specific spatial territories (e.g. Schnabel et al 1997). Thus it seems logical that genes with specific lineage patterns will have specific spatial patterns as well. If the claim is that the observed patterns are more clustered along the A-P axis than expected by chance given their lineal complexity then I'm not sure this is shown. Maybe some comparison with control lineage patterns of similar complexity of non-TFs or non-HD TFs could get whether these genes specifically are more spatially patterned? Visually it looks to me like some patterns are more like "blobs" or even lateral or D-V specific patterns than they are like "stripes."

In addition there is a long history in the literature discussing the origin of position-specific patterns in C. elegans - most I'm aware of support the idea that positional information arises primarily from intrinsic lineage mechanisms (e.g. Cowing and Kenyon 1996). Perhaps the authors are making this same argument here, but if so this isn't clear from the text.

Or maybe the authors are trying to make the argument that combinations of TFs encode more precise position than individual TFs? This seems more likely to me from the images presented still not well-supported without quantitative or statistical analyses.

1. The comparison with Drosophila is interesting but also under-developed. I think all I would feel comfortable claiming from the data as shown is that genes that are spatially patterned in early fly development are also usually patterned in the C. elegans lineage. But to even say this is an enrichment over expectation would require more analysis.

Minor comments:

Methods: some statement about temperature control during cell isolation would be useful. In other words were embryos continuing to develop or put at low temperature such as in a cold room to prevent temporal differences between the first and last cells collected from a given embryo?

Current links to data at GEO are incorrect and link to Levin et al 2016 instead. I was not able to access the raw single cell data, just the processed data in Table S6.

The standardization of expression in embryos isn't well explained - would be good to expand a little on the types of batch effects being addressed and how this approach was chosen or a relevant citation.

Page 2: Including P0 and cell deaths there are 1,341 branches in the hermaphrodite lineage (2n-1 for 671 terminal cells including deaths).

-"as their each have" (grammar error)

-"very large nuclear hormone receptor domain" (add "family")

Page 3: As noted Packer et al largely missed cells prior to the 50-cell stage as described - but the reason for this is likely that the use of 10 micron filters or centrifugation to remove undissociated embryos also removes early stage cells.

-"few new expressions occur" (grammar). Also, in both Tintori and Hashimshony datasets there well over 1000 newly expressed genes detectable (see for example Sivaramakrishnan et al 2021 biorxiv).

Figure S1 would be easier to interpret with a legend explaining what fates are represented by each color

Some genes listed as markers in Figure S2 are not included in the marker table such as flh-3, oma-2, sma-9.

"New markers were required" - this is plural but only F19F10.1 is mentioned. Were other markers examined this way or should it be singular?

In Figure S2 the lower ("robustness") plots are nice but could be explained more clearly. What is the nature of the "cell similarity score"? How many (if any) cells were excluded due to not being most similar to their own cluster?

"transcriptomically very similar shortly after division" - can the authors comment on any information they have about how long after division the cells were collected?

GFP reporter lineaging - the methods are minimally described (what brand of microscope, which strains/transgene/CRISPR configurations etc). And data are not presented. If these embryos are all incorporated into Ma et al 2021, that is fine, but should be clearly cited. Otherwise it is important in my view to include some way to access the quantitative values from the lineaging and understand these details.

"as illustrated for ceh-43, dmd-4 and unc-30" - were there other examples as suggested from this wording? I'd also note that similar fluorescent reporter imaging data have been published previously for all three genes listed (Walton et al 2015 for UNC-30, Ma et al 2021 for DMD-4 and CEH-43 protein reporters, Murray et al 2012 for dmd-4 and ceh-43 promoter reporters).

Zacharias and Murray are cited as promoting "continuous symmetry breaking" but actually that review argued for a "non-monophyletic" architecture similar to that supported by the data .

The text and figure don't always agree. For example mec-3 expression is listed in the text as part of one of the stripes, but mec-3 is not labeled on the figures.

The stage of each embryo in figure 4B/C should be explicitly labeled (and maybe also given specific figure panel designations to clarify what statements in the text correspond to which figures).

In the discussion it is unclear what the numbers "97 to 104" refer to

The scRNA-seq reads were mapped to a relatively old genome build and annotation set (WS230) - thus current users may find discrepancies with current gene names in WormBase. Also, since the CEL-seq data are 3' biased, it is worth noting that Packer et al found that a substantial number of genes (~1000) in a slightly later annotation set (WS260) were undercounted (sometimes dramatically) with the similarly biased 10x data due to incomplete 3'UTR annotations. While I would be reluctant to ask for a requantification for the purposes of the manuscript given the challenges of repeating the various analyses, it is worth explicitly mentioning whether this was dealt with.

Reviewer #2 (Recommendations For The Authors):

The writing was otherwise good, at least to my eye, and the data was presented very well and made freely available to other researchers. I am not as well-versed in the statistical methods and will leave comments on these to a better-equipped reviewer(s).

Fig. 1 legend 'P' should be P4 (subscript 4).

p. 9 'ceh-51' should be italicized.Only one factor seems to have been confirmed by smFISH, F19E10.1. There are available reporters, did they show a similar pattern? From CGC website: RW12347F19F10.1(st12347[F19F10.1::TY1::EGFP::3xFLAG]) V endogenous tagged reporter; RW11620 unc-119(tm4063) III; stIs11620 [F19F10.1::H1-wCherry + unc-119(+)] array reporter.

Reviewer #3 (Recommendations For The Authors):

Typo: on page 11, where it says nanog it should read nanos.

Reviewer #4 (Recommendations For The Authors):

I found some sentences and paragraphs to be a bit unclear. There are no page or line numbers in the manuscript, so I point in the general direction, and hope the authors find what I am referring to.

2nd paragraph of the Introduction - "their" should be "they", but the sentence as a whole is not clear.

3rd para. of the Intro. - The last sentence of this paragraph doesn't make sense. Please rephrase and/or break up into shorter sentences.

1st Para. of Results - "the maternal deposit" is not clear. Perhaps "maternally deposited transcripts" or something similar.

1st Para. after Figure 3. The last sentence "Thus, continuous symmetry breaking..." is unclear. What is "continuous symmetry breaking"? Please define and expand.

Fig. 4 - the genes seem to be listed from posterior to anterior. The common way of presenting Hox gene lists and other regionally expressed genes is from anterior to posterior.

For the benefit of the non-C. elegans crowd, please give names of Drosophila homologs where relevant (e.g., when comparing to Drosophila expression patterns)

In a few places there are citations of popular science books or general textbooks (e.g., Carrol et al., 2004; Wolpert et al., 2019) . I think it would be better to cite review papers from the scientific literature or relevant primary papers.

We thank the four reviewers for their thoughtful and constructive comments. In light of their comments we made important revisions that are integrated in the final version, including also the correction of several typographical errors.
