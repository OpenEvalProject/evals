# Peer review - Round 1

Editors:
- Breck A Duerkop, University of Colorado School of Medicine

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60608.sa1](https://doi.org/10.7554/eLife.60608.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This exciting and rigorous study utilizes a modified HiC method to increase metagenome assembled genome (MAG)-phage contig connections and the resulting data supports phage modulation of bacterial populations within the gut microbiota. This work lays the foundation for metagenomic applications that will advance our understanding of how phages impact their hosts and thus the microbiota both in the gut and in microbiotas other than the gut. This work is broadly applicable to many fields of research where microbial communities are studied.

Decision letter after peer review:

Thank you for submitting your article "Phages-bacteria infection network of the healthy human gut" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Breck A Duerkop as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Wendy Garrett as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Christopher Quince (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

In this study, the authors apply chromosome conformation capture (3C) library preparation methods to ten fecal samples from healthy individuals. 3C allows physically collocated DNA molecules to be identified. It is well established for resolving genomic structure but its application to metagenomes is more novel. Here, the authors focus on its application to link bacteriophages in the human microbiome to their hosts. They determine that about 25% of the phages are lytic, whereas ~50% of the phages are dormant lysogens. They use this methodology to identify human phages belonging to an emerging family of viruses, CrAss phages, greatly extending the predicted host range of these phages. Overall, this paper largely supports previously observed biology of intestinal phages. What makes this new and of broad interest is the ability to increase metagenome assembled genome (MAG)-phage contig connection using a modified eHiC method, coupled with some innovative computational analysis to correlate MAG replication to phage contig abundances that suggest phage modulation of bacterial populations within the microbiome. The techniques outlined here have the potential to provide profound understanding of how phages impact their hosts and thus the microbiota beyond just the human gut.

The revisions below come from three independent reviewers, each who deemed this work important and of high quality. However, there was consensus that revisions are needed to improve the work, including more rigorous statistical analyses and the inclusion of more scientific detail. This study came across like a proof of principle exploring the alternate 3C methods and their effectiveness in this context rather than dramatically novel science. Taking this into consideration, it was our collective opinion that the methods themselves are still sufficiently novel that even as a proof of principle this is an interesting study that could provide guidance to future larger scale studies utilizing these methods. Additionally, we commend the authors for establishing their tools on a GitHub repository. The readme document contained within was very helpful in describing the scripts as well as what was used in this manuscript. This resource will be valuable to the field as a whole.

Essential revisions:

1) A major concern is the number of replicates used to verify the superiority of the eHiC technique to that of the HiC or 3C method. Only one sample is used to make this conclusion. Ideally the author's would have performed this on a few more samples and then compared these to several replicates of just metaHiC and meta3C. The authors say they identified 81 high-quality genomes. Are these the same as what was identified via the metaHiC and meta3C? This is a critical result to support the utility of this developed assay. Since the authors have already published that 3C technology can make phage-bacteria connections, the real novelty here is that the eHiC method greatly increases the number of connections that can be made. However, this should be more rigorously proven.

2) From these data, a major observation is reinforced, that temperate phages seem to dominate the virome. If most phages are temperate then is Hi-C actually needed to make valid and in depth host connections?

3) The authors indicate that they verified their connections via CRISPR matching; however, they do not show the data. This is important to include for two reasons: 1) they indicate that it complements their current analysis and 2) CRISPR matching is often thought to be state of the field for making connections and it is implied that this method works better. Additionally, an explanation of why 15% validation with CRISPR is reasonable.

4) The association between MAG taxonomy and the phylogeny of their associated phages. This is presented graphically in Figure 3C by comparing the phage phylogeny with the order level assignment of a MAG. There does appear to be an association, but this needs to be quantified. This could be demonstrated with a permutation ANOVA of the phylogenetic distance between phages against their order assignment (using adonis in vegan for example). It could then be determined if this association breaks down at higher MAG taxonomic resolution. Similarly, the data in Figure 3B could be used in a Mantel test to determine strength of association between MAG distance and phage distance.

5) Why were the “category B” phages excluded from the analysis. The distribution of their contacts across MAGs would be a good sanity check for the methodology. Ignoring these results seems inappropriate.

6) Simply observing twofold higher coverage for a phage than the host is not definitive evidence that the phage is lytic since multiple factors influence sequence coverage, the phage could be multicopy, it could be near the origin of replication, or possess a sequence composition biased to higher coverage. The authors need to demonstrate that the phage sequences have significantly higher coverage than expected given these sources of variation. Since they are using growth estimation methods they could look at position in the genome and compare with non-viral contigs that are at a similar point. It would be helpful if the authors could pull out specific phage-host pairs as examples of what these patterns look like.

7) When discussing the novelty of MAGs, this should really be placed in the context of the recent large-scale binning surveys (e.g. Pasolli et al., 2019) which similarly observed most novel diversity in the Clostridia.

8) Was there any taxonomic signal in the number of phages associated with a MAG?

9) Without a cell harvesting step; intra cellular crosslinking, digestion and ligation; or a large ligation reaction volume, how is random proximity ligation and / or crosslinking of extracellular DNA avoided following a freeze thaw cycle of sample with no storage buffer? This may not be an issue as the data seems to suggest a small degree of contamination in the fused reads, yet this was not explicitly tested experimentally with mock communities. Having the molarity, copy number or even mass of DNA entering the ligation step would likely help as it is suspected it is quite dilute in the 1.1 ml volume.

10) Overall the manuscript indicates that two method derivatives are developed, but only meta-eHiC is discussed. The Materials and methods list the procedures for preparing the meta-Hi-C and meta-eHiC libraries so one can deduce the differences in the methods, but the Results should take a moment to explain these two derivatives. Is not developing them a result of this study? This would frame the results and interpretation of this work for the reader.

11) What is the correlation supposedly presented in Supplementary Figure 2, Results? A statistic is needed to support this claim.

12) For VIBRANT and VIrSorter results clarification is needed concerning uniqueness. Are those considered unique between the two tools or unique across samples (and possibly also between the two tools)? Also, were all category 1-3 VirSorter phages included or were just category 1 or category 1 and 2 (like VIBRANT does)? This detail should be included in the Materials and methods.

13) By looking just at the active phage population (Class A), one could speculate that they were lytic/infectious which may be reducing bacterial population numbers. But the ori/ter ratio is not really providing insight into their population spread rather just their replication rate. It is unclear how the authors draw their conclusion of an inverse correlation from Figure 4A, right panel. Is there a statistic to quantify this observation?
