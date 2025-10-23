# Peer review - Round 1

Editors:
- Douglas L Black, University of California, Los Angeles , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.10421.040](https://doi.org/10.7554/eLife.10421.040)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Regulatory consequences of nELAVL binding to coding and non-coding RNAs in human brain" for peer review at eLife. Your submission has been favorably evaluated by a Senior Editor, and two reviewers, one of whom, Douglas Black, is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

This paper from the Darnell group examines the RNA binding sites of the nELAVL family in human brain. The authors perform CLIP analysis and RNAseq in the BA9 region of the prefrontal cortex. They identify a large set of RNA binding sites and presumed target transcripts. They define the nELAVL binding motif as similar to the previously defined motif for the mouse and show that there is strong overlap between the targets seen in mouse and human. They show that nELAVL knockdown in human neuroblastoma cells causes reduced expression of mRNAs that exhibit 3' UTR binding. Similarly, exons with adjacent nELAVL binding show altered splicing with knockdown. Interestingly, both positively and negatively regulated exons exhibit enriched binding upstream, and thus do not present the same correlation of binding position with positive or negative regulation as seen with some other splicing regulators. Earlier results had made a connection of nELAVL proteins and Alzheimer's disease, and the authors next analyzed splicing and nELAVL binding in AD brains, finding some exons and binding events that differ between AD and control brains. The most significant change was a greatly increased level of nELAVL binding to a subset of Y RNAs in the AD brains. Y RNAs are a class of small noncoding RNAs in eukaryotic cells that affect RNA scavenging and quality control pathways. A subset of these RNAs contain an nELAVL binding site. Cellular stress is known to relocalize ELAV proteins to the cytoplasm, and they find that stressing tissue culture cells with low UV doses also increases nELAV/Y RNA binding as measured by CLIP. This is accompanied by changes in nELAV dependent splicing, presumably due to reduced nuclear protein.

This is a novel study of a topic with broad interest. The nELAV proteins have been widely studied. The extension of these analyses to the human system and to AD is significant, with the connection of nELAVL proteins to the Y RNAs being potentially very important. The authors present a large amount of work and the datasets generated will be a valuable resource for further studies. However, the analysis does not extend past identifying broad correlations between datasets, leaving the biological or mechanistic conclusions unclear. A number of unaddressed issues regarding the identified nELAV/Y RNA interaction make its significance hard to judge. The paper is also difficult to digest. It is hard to follow what was actually done in the various statistical comparisons, what the results mean, and the authors conclusions often seem vague. They often point to rather weak correlations as being "consistent" with a particular model. Sometimes they use abbreviations and acronyms that don't seem to have been defined (for example, is dI the same as delta PSI?). There are a number of places where the analytical methods used could be improved or at least better explained.

Major issue:

1) The most significant finding in the study is the binding of nELAVL to the Y RNAs, but this is not taken far enough to draw many conclusions. Is it the increased Y RNA binding that is causing the change in splicing or is it a consequence of increased cytoplasmic protein that is the result of cellular stress? How much Y RNA is there relative to nELAVL? What percent of the nELAVL is actually bound by the Y RNAs? Are the amounts sufficient to sequester most of the ELAVL and thus have an effect? Why do so many Y RNAs without ELAVL binding motifs also appear to be binding? Can the authors connect the splicing or expression changes observed in the UV treated IMR32 cells to those seen in AD? Without this, it is difficult to make the case that the cytoplasmic relocalization of the nELAVL proteins is relevant to AD. The reviewers all felt that the authors should work to make some of these mechanistic connections between the Y RNAs and AD and thus strengthen this most interesting finding.

Issues regarding the analytical methods:

1) The peak finding in the CLIP analysis needs to be better described. The authors refer to Licatalosi (2012), but that paper describes a relatively outmoded method of defining peaks above a gene specific background, as well as the use of the much better CIMS analysis from the Darnell and Zhang groups. It doesn't appear that CIMS analysis was used here, so what exactly was done?

2) Similarly, MEME-ChIP has been shown to not work well for RBP motif finding. Stating that the motif identified in human is in excellent agreement with that found in mouse is not very meaningful since both studies used the same MEME-ChIP analysis. The authors should investigate the use of newer tools such as Graphprot (Maticzka et al. Genome Biology 2014) or Zagros (Bahrami-Samani et al., NAR, 2015) for motif discovery.

3) In Figure 1D, are the peak numbers in different regions normalized for the lengths of the different types of sequences?

4) There are also normalization questions regarding figure 1E and other plots. These plots show correlation between CLIP peaks and tags with mRNA abundance as measured by sequence reads per gene. This is problematic on several levels. First, both CLIP and RNAseq reads will be strongly affected by gene length. A better comparison is to use CLIP clusters per unit length of gene vs RPKM from RNAseq, which will normalize both values by gene length. Second even with length normalization, CLIP clusters will automatically vary strongly with gene expression level. A true comparison would need to look at the distributions of sequence density for genes in the CLIP and RNAseq datasets.

5) The authors use the human genome release hg18 for their alignments, although the conclusions do not likely depend on the genome release. Most people in the field are using the now 6-year-old hg19 and it would make it much easier for others to use these results if the authors were to update their pipelines to hg19.
