# Peer review - Round 1

Editors:
- Jessica K Tyler, Weill Cornell Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68745.sa0](https://doi.org/10.7554/eLife.68745.sa0)

This paper is likely to be of broad interest to researchers in the chromosome biology field. With specific loading sequences identified, the Condensin dosage compensation complex studied here provides an elegant system to investigate the in vivo activities of SMC complexes. Combining Hi-C, ChIP-seq and RNA-seq, the authors reveal that the complex spreads along the chromosome to create chromosome loops.


---

# Peer review - Round 1

Editors:
- Jessica K Tyler, Weill Cornell Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68745.sa1](https://doi.org/10.7554/eLife.68745.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Condensin DC spreads linearly and bidirectionally from recruitment sites to create loop-anchored TADs in C. elegans" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jessica Tyler as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

The reviewers and the Reviewing Editor agree that the manuscript has potential, but extensive revision and new experiments and analysis are needed to make the case for publication in eLife and move forward. The reviewers raised concerns about (i) the novelty of the study (as compared to Albritton et al. 2018, and Anderson et al. 2019, and other studies); and (I) validity of the conclusions drawn from presented data. Nevertheless, the study is unique in its approach of inserting rex sites into largely DCC-free autosomes, and can be improved and developed to become an impactful publication.

Reviewers and the Reviewing Editor feel that suggested mechanisms, i.e. (i) loading of DCC at rex sites, and (ii) function of rex sites as extrusion boundaries, cannot fully explain presented data. While ChIP-seq data support the loading of DCC but less of its spreading, the Hi-C data indicates the boundary role and shows no indication of the loading. I.e. Hi-C and ChIP-seq data are hard to reconcile with each other. If DCC indeed loads at integrated rex sites, one would expect to see accumulation at these sites in ChIP-seq (that may to some extent be present) and stripes emanating from rex sites on Hi-C as observed at condensin loading sites in bacteria (in the case of bidirectional extrusion) or as computed in simulation (Banigan et al. eLife 2020;9:e53558). Such stripes are clearly absent in presented data, putting the loading at rex in question. Reviewers didn't find the author's explanations coherent and convincing.

Essential Revisions:

1) If the authors want to pursue the double-function of rex sites they need to find support for the loading process in Hi-C. Potential ways of doing this would be to generate Hi-C data for single insertions. To increase the effect, authors may want to insert a strong rex site into an autosome. Or insert many rex sites (~5-10) spaced far from each other and examine an average Hi-C map at rex sites. Deeper sequencing and high-quality Hi-C (new MNase-involving or similar protocols) can help to reveal patterns of loading. Horizontal or 45-degree lines or other structures emanating from rex sites would be indicative of loading.

(*) The Reviewing Editor would also recommend considering a possibility of depleting non-DCC condensin I (or other suspected SMCs) that may be abundant at autosomes and masks the effect of DCC loading. In fact, abundance of another SMC may explain apparent disagreement between ChIP-seq and Hi-C: i.e. rex sites of DCC loading would block extrusion by another SMC, while having little effect on Hi-C maps otherwise. It's presence could be quantified by IP for another component of the condensin complex. And relative abundance of DCC and non-DCC condensin I could reveal loading.

2) The authors should consider the alternative that peaks on DCC ChIP-seq are mere reflection of stopping at rex rather than loading there. Demonstrating spreading of DCC from rex is essential. The Reviewing Editor suggests examining the level of DCC at non-rex sites, proximal to rex: an increasing level of DCC at such non-rex sites upon insertion of more and more potent rex sites would support loading at rex. Perhaps a series of single-site insertions could be better than inserting two sites as they could be mutually blocking each other.

3) Analysis: ChIP-seq analysis and quantification appears to have several issues. The scale on ChIP-seq plots appear to be insistent and disagree with each other (Figure 1A: Y scale goes to 1.5 and peaks at rex are <1.5, while in the inset up to 3, and several peaks exceed 3.) Figure S1A is more telling as it shows X-chromosome on the same scale. Quantitative ChIP-seq (with spike-in) may be the best solution for comparative analysis, but authors could use signal (peaks or total) on X-chromosome for normalization of non-X signals, making non-X ChIP-seq data comparable with each other. Figure 3B ChIPseq also appears all on different Y-scales, normalizing the distal part of X-chromosome can help with comparative analysis. Similarly, reviewers were concerned about quantification of 4C, its agreement with Hi-C. Analysis on Figure 4B wasn't clear and raised several concerns. It was also surprising that visual inspection of Hi-C in Figure 4A doesn't indicate or support findings in Figure 4B.

4) The reviewers raised concerns with results and interpretation of dCas9-targeted boundary. The lack of the insulation on Hi-C argues against not in favor of the stopping function of dCas9-recruited proteins. Accumulation of DCC without insulation would argue for either (a) loading of DCC at the DNA that because more accessible due to nucleosome eviction by the dCas9-recruitment, and/or (b) over-ChIPability of such regions when they become more accessible -- a well-known artifact of ChIP-seq.

5) Presentation: presenting Hi-C in grayscale is suboptimal as colors would allow one to see the dynamic range of the data. In addition, statistics for Hi-C need to be provided.

Reviewer #1 (Recommendations for the authors):

It would be interesting to see more quantification of the effects of condensin recruitment and spreading on the genome conformation. Particularly, Figure 2 may benefit from (a) a ratio map of contact frequencies in 3 rex/WT and (b) a plot of average contact frequency vs genomic separation in the affected region. In Figure 4, a zoom-in on the affected portion of the chromosome V (17.5-20Mb of the fusion chromsome) may more convincingly support the claims. Finally, in my experience, the curve in Figure 4B seems surprisingly noisy for the quality and amount of generated data. I would recommend the authors to double check the procedure by which they generated these curves.

This manuscript may benefit from a stronger and more focused statement on how it improves the state of the knowledge in the field. Many of the claims – insulation by individual rex sites, formation of loops/dots between rex sites on Hi-C maps, spreading of condensins on autosomes fused with the chromosome X – were already made in or could be inferred from the previous studies (e.g. Anderson et al. 2019, Crane et al. 2015). Of course, the authors do cite these studies in a complete and honest fashion; moreover, if I understand correctly, this study for the first time showed the effect of rex site insertions into a "clean slate" of an autosome, which is an important achievement. However, for a person who is not deeply engaged with the field of dosage compensation in C. elegans, the novelty of this paper may not be immediately obvious.
