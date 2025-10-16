# Peer review - Round 1

Editors:
- Sheila McCormick, University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.57088.sa1](https://doi.org/10.7554/eLife.57088.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work is an exciting and critical study that speaks to the field of evolutionary developmental biology beyond plant biology. It focuses on life cycle evolution in green plants, where the haploid-dominant life cycle in green algae evolved into the diploid-dominant one in land plants. The thorough analysis of molecular phylogeny, and a detailed investigation of developmental expression provides a comprehensive account of entire TALE class proteins, and is more than expected in a single study.

Decision letter after peer review:

Thank you for submitting your article "Gamete-specific expression of TALE class HD genes activates the diploid sporophyte program in Marchantia polymorpha" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Sheila McCormick as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Christian Hardtke as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Jae-Hyeok Lee (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript of Dierschke et al., represents an exciting and critical study that speaks to the field of evolutionary developmental biology beyond plant biology. It focuses on life cycle evolution in green plants, where the haploid-dominant life cycle in green algae evolved into the diploid-dominant one in land plants. TALE class HD TF KNOX and BELL subfamilies have been implicated in the haploid-to-diploid transition in the green lineage, in the unicellular Chlamydomonas and in Physcomitrella. The authors therefore investigated the function of TALE class homeodomain transcription factors in the liverwort M. polymorpha. The authors use a range of molecular genetics and genomic approaches to demonstrate that MpBELL234 are expressed in male gametophyte cells (antheridia), while MpKNOX1 is expressed in the female egg cell before fertilization and during sporophyte development. They provide evidence that maternally supplied MpKNOX1 is required for later sporophyte development and that paternally supplied MpBELL234 is required for zygotic development. They found two distinct heterodimeric complexes of TALE class proteins, MpKNOX1 plus MpBELL2/3/4 and MpKNOX2 plus MpBELL1. They used BiFC to demonstrate the interaction between BELL and KNOX. Finally, they suggest that Polycomb, a repressive chromatin modifying complex, is required to repress the MpBELL1 and MpKNOX2 genetic program during gametophyte development. The thorough analysis of molecular phylogeny, and a detailed investigation of developmental expression by combining RNA-seq and ChIP-seq, provides a comprehensive account of entire TALE class proteins, and is more than expected in a single study.

Essential revisions:

We have major concerns about the ChIP-seq approach that was used to demonstrate the absence of H3K27me3 on the target loci. It appears that the ChIP-seq was not replicated, and the presence/absent of histone PTMs on the loci under study has not been verified by other means. Normally the claims made in the manuscript would need to be backed up by either another replication of the ChIP-seq experiment or with validation using ChIP-qPCR. More details are presented below. In the event that this is not possible now, the phrasing should be changed to emphasize that this needed data is missing (i.e. qualify the claims).

Furthermore, the first part of the paper (p. 5-19) is about gene structure and phylogeny and we don't get to the knockdown experiment until p. 20. As these aspects are not represented in the abstract, we suggest that this section of the paper is minimized. In the discussion the phylogeny is not discussed until the end, again giving the impression that it is not that important. The lengthy molecular phylogeny section would need to be further elaborated into a significant finding or provided as a brief supplement for improving the narrative's focus. The discussion is about 8 pages and probably could be condensed to the main points.

1. This manuscript reports that KNOX2 and BELL1 form heterodimers, whose functional study may await an analysis of their knockout plants. While the authors consider KNOX2/BELL1 unlikely to be involved in the haploid-to-diploid transition, KNOX2 in the moss, Physcomitrella, plays a critical role in preventing gametophyte development from resuming in diploid sporophytes. Thereby, a de-repressed KNOX2/BELL1 heterodimer may produce aberrant phenotypes during gametophyte development in Marchantia.

2. The authors investigated if the repression of TALE-HD (MpBELL1 and MpKNOX2) in the vegetative gametophyte occurs via PRC2. They use an inducible system with miR to knockdown MpE(z). The expectation is that E(z) knockdown will decrease PRC2 activity and hence reduce overall H3K27me3 marks within the genome. It's a rather 'brutal' approach because it is likely that many loci genome-wide will be de-repressed. But the manuscript gives no information about the overall genomic landscape after the E(z) miR knockdown. If available, describe phenotypes of the amiR-MpE(z)1 plants following 17-b-estradiol treatment in addition to the TALE gene expression. For the two experiments using transgenic plants harboring conditional amiR-MpE(z) or ectopically expressed MpKNOX1 or MpBELL3, the effects of the transgenes may differ between male and female gametophytes. Please indicate whether both or single-sex plants were analyzed.

3. Detailed analysis of MpBELL2/3/4 knockouts in the male gametophytes indicates their essential role in post-fertilization sporophyte development. However, the two observed phenotypes, zygotic, or early embryonic arrest, may be due to the expression of BELL2/3/4 from the female nucleus, as indicated by the authors (P44 L6). Since both Mpbell2/3/4 male and female plants were reported, it is reasonable to ask for the phenotypes of the sporophytes produced by Mpbell2/3/4 knockout male and female.

4. The authors state on page 21 "Compared to the overall H3K27me3 landscape in wild-type gametophytic tissue, the number and amplitude of methylation peaks are consistently reduced after 48h of down-regulation of MpE(z)1." What is meant by "consistently"? This statement needs to be backed up with data and proper statistical analysis. This requires at least one replicate experiment, and certainly no claims can be made about "amplitude" of the peaks (to compare ChIP-seq peaks quantitatively 'spike in' experiments are needed, etc., etc, – not a trivial task). One option could be to take a few dozen loci and carry out ChIP-qPCR experiments.

It is stated that MpKNOX2 and MpBELL1 show altered H3K27me3 patterns (which provides the basis for the conclusion that polycomb is required to repress BELL1 and KNOX2 but not KNOX1 and BELL234). The validation of ChIP-seq data using another replicate of ChIP-seq or ChIP-qPCR is also crucial to back up the following sentence "The three primarily gametophyte-expressed KNOX1 genes were neither marked with H3K27me3 nor induced in the amiR-MpE(z)1 background".

5. Details of the ChIP-seq data (sequencing stats, coverage, %uniquely mapped reads, n. reads, was more than one peak caller used, FRip values, n. peaks, etc). Is the GEO reference for the ChIP-seq data missing? In the methods section the authors mention MACS as a peak caller. A table should be provided with loci/peaks that have been called before/after induction.

Revisions expected in follow-up work:

Another replication of the ChIP-seq experiment or validation using ChIP-qPCR.
