# Peer review - Round 1

Editors:
- Job Dekker, University of Massachusetts Medical School United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.27024.036](https://doi.org/10.7554/eLife.27024.036)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Chromatin-associated RNA sequencing (ChAR-seq) maps genome-wide RNA-to-DNA contacts" for consideration by eLife. Your article has been favorably evaluated by Kevin Struhl (Senior Editor) and three reviewers, one of whom, Job Dekker (Reviewer #1), is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This is an interesting manuscript describing a new approach for mapping RNA-chromatin interactions genome-wide. It has the potential to be a major improvement over existing methods. Three patterns of RNAs linked to chromatin are identified in flies: 1) those of nascent transcript next to their genes, 2) RNAs in trans across all genome, and 3) those on X chromosome for male cells. The method could be an important approach for the study of how RNA modulates the genome and is therefore of interest to many. Several issues related to reproducibility, sensitivity and specificity need to be addressed, as outlined below.

Essential revisions:

The authors need to address the following main points:

1) Compare CharSeq performance in more detail to previously published MARGI and ChIRP-Seq methods: what are the key difference, improvements? Can you quantify this?

2) Can you add metrics describing sensitivity and specificity of the method?

3) Please clarify concerns about how many times experiments were performed and add details on statistical analysis of reproducibility of data and analyses.

4) Can you make the results available in a more user-friendly way, i.e. make the results available as a list of RNAs and loci they associate with.

5) Explore RNAs interacting with heterochromatin, rDNA etc. These are repetitive DNA sequences, but a meta-analysis of RNAs associating with defined repeats is of considerable interest and would enhance the paper.

Reviewer #1:

This is an interesting manuscript describing a new approach for mapping RNA-chromatin interactions genome-wide. It has the potential to be a major improvement over existing methods. I missed a more deep quantification of background, sensitivity and signal to noise ratios and how these relate to expression levels.

Reviewer #2:

The manuscript by Bell et al., presents a sequencing method to map all RNA-chromatin/DNA contacts in a genome: Chromatin-Associated RNA sequencing (ChAR-seq) a proximity ligation and sequencing method. The approach is utilized mainly to examine what RNAs are interacting with chromatin in Drosophila melanogaster CME-Wl-cl8+ (male) wing disc cells. Some work is also done using female Kc167 cells. Three patterns of RNAs linked to chromatin are identified: 1) those of nascent transcript next to their genes, 2) RNAs in trans across all genome, and 3) those on X chromosome for its inactivation. This last group, as expected, does not show up in the female cell line. The data obtained via ChAR-seq are in agreement with those obtained by Quinn et al., 2014 using ChIRP-seq. The ChAR-seq appears as a more sensitive method because it captures all RNA-DNA contacts. Authors also use their data to provide novel insights about the function of the various RNAs that they found to have abundant association with chromatin. The application of ChRA-seq in this study have revealed many snoRNA molecules interacting with chromatin in the heterochromatin form.

1) Overall, the authors show that ChRA-seq works well to identify both RNAs that are nascent and thus still connected with DNA in cis, and RNAs that do not directly interact with DNA, but rather with chromatin factors in trans. The ChRA-seq approach is validated with the RNAs that are known to be functioning in chr. X dosage compensation, in fact these RNAs (roX1 and roX2) are found to bind chr. X chromatin in the Drosophila male cells but not in the female cells. In addition to the similarity of the ChRA-seq approach to the ChIRP-seq by Quinn et al., Nat Biotech 2014, which although is limited to RNA-chromatin interactions, as pointed out by the Authors, ChRA-seq is almost identical to the method used in Sridhar et al., 2017in vivo. Thus, the novelty of the study by Bell et al. is in part reduced because of this recent publication, which exploits a very similar ligation method to capture sites of RNA interaction with chromatin and DNA.

Other points:

2) What is described in the first paragraph of Results does not match perfectly with Figure 1A, because the RT step in the figure is shown after the bridge is ligated to DNA, while in the text it is described before the bridge is ligated to DNA. The text should match the figure description.

3) It would be good to add the polarity of the RNA molecule in red in the Figure 1A. It would be good also to explain that the approach captures the 3' RNA ends of RNA molecules. Also Figure 1A should be bigger to clearly show which RNA end is ligated to the bridge, to clearly indicate the polarity of ends and the structure at the junction. If the App has a free 3' end, and this is ligated to 3' end RNA, is this a 3'-3' ligation? Or is the App removed in the ligation process? This should be explained well because it is not evident.

4) The statement "the 5'-adenylated end (5'App) enables increased ligation specificity for 3'-terminated ssRNA" is not clear: 'increased specificity' relative to what?

5) Is the sequence of RNA and DNA oligos presented in Figure 1—figure supplement 2 provided? It is not clear what the molar excess of DNA over RNA is, please clarify. Also the legend of this figure should explain what is shown in every lane. In lane 1 there is a high mw band, what is this, what is its size? The ladder sizes are provided only for the bottom part of the gel, they should be provided also for the top part, considering that there is a high mw band. How many times was this experiment repeated? Is there any statistical analysis of these data? This, possibly, should be explained in the legend.

6) The statement: "This RNase-treatment dramatically reduced in the number of bridge molecules identified, demonstrating that bridge ligation is indeed RNA-dependent (Figure 1—figure supplement 5)" is not strongly supported by the data shown in this figure. In addition to a typo in this statement, looking at the figure, there seems to be a factor of six reduction, which does not represent a 'dramatic' reduction. Importantly, there appears to be no repeats of this experiment and no statistical analysis of the data. Was this experiment reproducible, are there repeats that can be shown?

7) Legend to Figure 1E has a typo: "Zoomed in region of shown".

8) Typo in Results: "we performed RNA-seq to for".

9) The correlation between expression level of the RNA and FPKM contacts is not very clear, because in Figure 2—figure supplement 1 and 2 this does not seem to be the case.

Reviewer #3:

This manuscript presents a very important new technique (CHAR-seq) developed to identify chromatin-associated RNAs. The major benefit of this method in contrast to previously used techniques is the use of proximity dependent ligation to generate sequences from ssRNAs linked to nearby DNA, which allows relatively unbiased assessments of associations across much of the genome. The authors demonstrate very nicely that application of ChAR-seq to Drosophila cultured cells identifies a spectrum of chromatin-associated RNAs, including chromosome-specific, nascent mRNAs, and sn/sno RNAs. The utility and novelty of ChAR-seq makes it completely appropriate for publication in eLife; I am very enthusiastic about acceptance once some issues about the presentation and analyses are addressed / clarified.

1) Data completeness and transparency:

To provide a more complete resource for the community, all potentially interesting RNAs should be named/identified in a table, including those that were initially included but didn't match criteria for 'chromatin associated'.

a) There should be a table listing the 1797 RNAs (Figure 2D), and relevant information, such as% and numbers of cis and trans contacts, RNA expression level, RNA-DNA contacts, and a way to access information about their genomic distributions, etc. – essentially anything that may be of use to scientists interested in whether or not their favorite RNA is present, or in performing their own analyses of the data.

b) I assume Figure 2E shows all 1797 as 'included', but the 'chromatin associated' RNAs in Figure 2E should be listed in a table. My impression is that some (73) but not all are listed in Figure 2—figure supplement 1 – are these the red dots in 2E? Even if all red dots are listed in the supplement, readers should be able to access identity and other data for all 1797, and especially the grey dots that are RNA-DNA contact outliers with high expression (I suspect that normalization to expression levels eliminates interesting candidates, see statistics discussion below). Similarly, there appear to be RNAs with low expression that may be chromatin enriched, yet are not highlighted in red.

2) Genomics, Analysis and Statistics:a) Figure 1D, 2A and elsewhere. I could not find a description of what the black circles and darker grey areas on the chromosome graphics indicate. I assume black=centromere, but the rest is unclear.

b) Why was release 5 used, given that the more complete release 6 has been available for at least a year? In addition, genomes from the cell lines used have not been assembled, and are likely rearranged (plus other variation, including DNA copy number) relative to the reference sequence, so the positions shown in the figures are likely to be incorrect, though we don't know where. No, the authors do not need to assemble the clone8 or Kc genomes, but they should acknowledge this issue.

c) It is unclear what parts of the genome assembly were included, for example were heterochromatic regions included, and if so where is that data presented? This information would help with the interpretations, especially in Figure 4D.

d) A related point, for Figure 4D it would be helpful to report the genomic locations (middle of euchromatin? Pericentromeric? X vs. autosomes?) for RNAs whose chromatin contacts show strong correlation with specific chromatin marks. Also, please explain how the correlation signals were aggregated in Figure 4D – the methods described using 2kb bins while the figure showing 100kb bins.

e) Can the authors discuss how the use of PCR to amplify ligated RNA/DNA contacts, combined with normalization to expression levels, could exclude RNAs with lower transcription levels, even if they have many (potentially important) DNA contacts? I think they are being appropriately conservative, but as with all such screens, and to help others who will certainly try it themselves, it would be good to have a brief discussion about the tradeoffs.

f) Some of the statements need quantitative support, such as:

- Figure 2E – what is the threshold for identifying RNAs with more than expected chromatin interaction (how was the expectation calculated?

- How were p-values for rox1 and rox2 (7.6 fold and 8.1 fold enrichment) calculated?

- Figure 3E: correlation between the DNA contact locations from ChIRP and ChAR- seq –.is this simply the Pearson correlation coefficient?

- Figure 4—figure supplement 1: how was the base sequence similarity calculated and used to aggregate signals for different snRNAs?

g) Using the correlations between ChIRP and ChAR-seq to assess the resolution of ChAR-seq does not seem to be appropriate, since the preparation of sequencing libraries may be very different between these two datasets. (Also, the curve actually goes down as window size increases?!) The authors should provide more reasoning for this approach.

How were the replicates analyzed?.Were they merged? What are the correlations between replicates?

h) How was the z-score was calculated? It seems like it is calculated as comparing between the values in each bin vs. the rest of the genome. If this is the case, there may be no need to calculate a z-score as every window will have the same denominator, and it may be just as informative as using the read counts. Also, it may be informative to use the chromosome-specific mean (instead of whole genome mean) to further identify interesting local events (the current analysis may be mainly identifying between chromosome differences).
