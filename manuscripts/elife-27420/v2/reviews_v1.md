# Peer review - Round 1

Editors:
- Scott Keeney, Howard Hughes Medical Institute, Memorial Sloan Kettering Cancer Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.27420.015](https://doi.org/10.7554/eLife.27420.015)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Transcription of a 5' extended mRNA isoform directs dynamic chromatin changes and interference of a downstream promoter" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jessica Tyler as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. As you will see from the comments below, there was enthusiasm for this manuscript as a companion to the co-submitted manuscript from Chen et al. However, there were also several important weaknesses that need to be addressed before the paper can be published in eLife. We realize that we are requesting a substantial amount of work to strengthen the experiments and their conclusions, but given that your manuscript is a co-submission, we considered that it was fairer to give you the opportunity to revise the paper rather than to reject it and keep the door open to a resubmission at a later date.

Summary:

In this manuscript, the authors provide mechanistic insight into how an mRNA that initiates ~500bp upstream of the NDC80 gene represses transcription from the NDC80ORF promoter. In the accompanying manuscript, basic features of the NDC80 regulatory system were described, including demonstration that the long mRNA, termed NDC80luti, and the ORF mRNA appear anti-correlated and that blocking transcription from the NDC80luti promoter derepresses the ORF transcript. In this manuscript, the authors find support for a transcriptional interference mechanism in which transcription from the upstream start inhibits PIC assembly at the ORF promoter and establishes a histone modification pattern at the ORF promoter (enrichment of H3K4me2 and H3K36me3) that has been previously associated with recruitment of two well characterized yeast HDACs, Set3C and Rpd3S. The authors extend their work by showing that the NDC80 regulatory system is reversible, when cells are switched from sporulation to growth media, and tunable, when the levels of the NDC80luti transcript are systematically elevated through a lexA-ER system.

Demonstration of the molecular basis of the repression mechanism is a valuable complement to the accompanying paper by Chen et al. However, as the authors acknowledge, involvement of cis-repression of a promoter by an overlapping non-coding transcript via transcription-coupled histone methylation and establishment of repressive chromatin is not a novel mechanism, being established at several other genes in yeast. In addition to the examples for this cited by the authors, there is the case of the upstream ncRNA that represses SER3 by promoting nucleosome assembly over the SER3 promoter, and antisense transcripts that mediate histone methylation of the promoter for the sense transcript at FLO11. Other studies, including recent work from the Buratowski lab on a genome-wide scale, showed that noncoding transcription across promoters leads to enrichment of H3K4me2 and H3K36me3 and repression of the promoters. With that said, the study does provide insight into an interesting example of regulated transcriptional interference.

In addition to the need for a more thorough coverage of relevant precedents for similar examples of gene regulation (see above), there are some important control experiments lacking, notably a failure to measure by ChIP the total H3 levels in the NDC80ORF promoter – to distinguish nucleosomes from non-histone chromatin protein occupancy, and to normalize changes in methylation for changes in H3 occupancy – and lack of quantification of changes in the NDC80ORF transcript, which is required to firmly establish the role of Set2/Set3 in repressing this promoter. In addition, there are a number of instances where direct experimental evidence is insufficient to support mechanistic claims made; these instances need to be remedied by inclusion of more data or by significant rewriting of text to soften conclusions and make them more nuanced. Statistical analysis of replicate data is missing for measurements of mRNA levels by northern analysis. Loading and normalization controls are lacking in multiple figures.

Essential revisions:

1) The increase in MNase-resistance in the NDC80ORF promoter region is not necessarily due to nucleosomes as it has been shown that non-histone protein binding in NDRs can also confer MNase-resistance (PMID: 28157509). For this reason, a ChIP of the MNase-resistant chromatin with histone antibodies is required to establish nucleosome versus non-histone protein occupancy.

2) In Figure 2C changes in nucleosome occupancy are inferred upon repression of the downstream promoter (at -100), but there is no evidence for loss of nucleosomes accompanying activation of the upstream promoter. Is this because the upstream promoter is nucleosome free even when repressed or is there another explanation?

3) Figure 2. Some information on the sequences of the promoters should be presented. Does the Sua7 occupancy profile make sense with respect to positions of core promoter elements? Why is the highest Sua7 signal detected 400bp upstream of the NDC80luti TSS?

4) Figure 2. How were the nucleosome positioning data normalized? Typically these data are normalized to a known, highly occupied nucleosome position (for example, Sekinger et al. Mol Cell 18: 735). Also control gels should be included to show the MNase digestion profile.

5) ChIP with histone antibodies is also required to normalize the H3-K36me3 and H3-K4me2 ChIP signals in Figure 3A-D and Figure 3—figure supplement 1 in order to establish that the amount of methylation per nucleosome is increased over the NDC80ORF promoter in a manner dependent on the luti promoter. K4me2 levels should be included in Figures 3C and 3D.

6) Figure 4A: RNA loading controls are needed in the northern blots. Quantification of the mRNA from replicates with a loading control is needed to establish that the NCD80ORF transcript is elevated reduced in prophase in the double mutant relative to WT, as this seems to be limited to the 3hr timepoint, and even this increase is not evident in Figure 4D. Perhaps the only meaningful increase in terms of Ndc80p expression occurs at 4-5hr.

7) Figure 4G. How many repetitions were done to calculate the relative Ndc80 levels? Also, the levels of the Hxk1 loading control seem to be changing both in this panel and in Figure 4—Figure supplement 1. This is perhaps not surprising given the change in carbon source in this experiment and the known connections of Hxk1 to carbon metabolism.

8) The accompanying Chen et al. paper provides evidence that Ndt80 is required for induction of the short NDC80ORF mRNA. If so, how can it be induced in the experiment of Figure 5A conducted with an ndt80 mutant?

9) Figure 5. Panel B lacks an RNA loading control and quantitation. The data in panel E need to be normalized to total H3 levels.

10) Figure 6B needs to be accompanied by measurements of Ndc80 protein to confirm that the requirement for Set2/Set3 in Ndc80p repression have been bypassed. Similarly for Figure 6C.

11) Figure 7. The figure does not add very much to the discussion. The vertical red lines are not defined. The nucleosomes look more like Pol II molecules with modified CTDs. Please modify accordingly.

12) In the Discussion, the authors conclude that their data show the "co-transcriptional recruitment of Set1/Set3C and Set2/Rpd3S is essential for establishing a repressive chromatin state and inhibiting NDC80ORF transcription". Recruitment of none of these factors was tested and therefore the text needs to be modified accordingly.

Non-essential revisions:

1) Figure 2 provides the main data supporting a transcriptional interference mechanism. As presented, the data are insufficient to support the stated conclusions. First, additional factors should be assayed by ChIP, beyond Sua7. In particular, how does NDC80luti expression influence Ndt80 occupancy in the NDC80 promoter region? Second, what is the effect of blocking NDC80luti transcription on Sua7 and Ndt80 occupancy? What is the effect of blocking NDC80luti on nucleosome occupancy? Note: the additional ChIP experiments suggested in this point are encouraged, but are not considered essential for publication. However, if the authors choose not to strengthen this part of the study, it is essential that they substantially modulate the strength of their statements in the text to be in line with what the data actually demonstrate.

2) Figure 4. The authors use set2∆ as a proxy for removing Rpd3S. The HDAC could be directly tested by performing similar northern and western blots with an rco1∆ strain. The authors argue that loss of the two HDAC systems alleviates transcriptional interference. This could be tested by ChIP of Sua7 in the HDAC mutant strains. Surprisingly, the authors show effects of deleting SET2 and SET3 on nucleosome occupancy but not histone acetylation levels at the ORF promoter. Their model should be tested more directly with better choices of mutants and ChIPs. Note: the additional ChIP experiments suggested in this point are encouraged, but are not considered essential for publication. However, if the authors choose not to strengthen this part of the study, they need to substantially modulate the strength of their statements in the text to be in line with what the data actually demonstrate. For example, without directly testing recruitment of HDACs, which can be tricky to do, they cannot say that their data show recruitment of HDACs via H3K36me3 and H3K4me2. They can merely describe this as a likely scenario. However, they could provide more support for this model by measuring histone acetylation levels, which is not hard to do.

3) Figure 1 essentially recapitulates the same or similar experiments described in the accompanying paper by Chen et al., with somewhat different promoter replacements or termination insertions for the NDC80luti transcript. Given this redundancy, the authors should consider omitting this figure. If they prefer to retain the figure, substantial improvements are needed. Here, the corresponding Ndc80 protein data are lacking for these promoter and termination constructs; although the quality of the northern data is better here for the terminator construct. However, mRNA loading controls and quantification of the northern data from replicates is lacking and should be provided.

4) It's surprising in Figure 2C that the nucleosome peak at ~-500, which is probably the +1 nucleosome for the luti mRNA promoter doesn't decline in prophase on induction of this transcript. This deserves some comment.

5) Figure 2B: It's surprising that TFIIB binding increased the most during prophase at -800, >300 bp upstream of the TSS for the luti transcript, raising questions about the location of the luti promoter. This deserves some comment.

6) Integrate Figure 3—figure supplement 1 data into Figure 3, and add premeiotic and S-prophase labels to data key.

7) Subsection “Gene repression by NDC80luti transcription is tunable”, last paragraph: "repression" should probably be "expression".

8) Subsection “NDC80luti mediated repression of NDC80ORF is dynamic”, end of first paragraph: it would be helpful to cite explicitly the data that supports this statement.

9) It would be nice to see a northern analysis to examine both long and short NDC80 mRNAs in Figure 6A. This would provide support for the last two sentences in the first paragraph of the subsection “Gene repression by NDC80luti transcription is tunable”.
