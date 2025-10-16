# Peer review - Round 1

Editors:
- Luis F Larrondo, https://ror.org/04teye511 Pontificia Universidad Católica de Chile Chile

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73832.sa0](https://doi.org/10.7554/eLife.73832.sa0)

This important study reveals, with exquisite temporal resolutions, critical transcriptional events that take place as Candida glabrata infects macrophages, providing convincing analyses that enhance our current understanding of the underlying sequential transcriptional changes, including a previously uncharacterized transcription factor (CgXbp1), which plays an important role in modulating the temporal responses in macrophages, impacting C. glabrata survival and virulence and, notably, also fluconazole resistance. The work would benefit from additional experiments that could provide a more mechanistic understanding of the key events leading to successful infection yet, in its current form it should be of interest to a broad audience interested in host-pathogen interactions, fungal biology, and transcriptional mechanisms at large.


---

# Peer review - Round 1

Editors:
- Luis F Larrondo, https://ror.org/04teye511 Pontificia Universidad Católica de Chile Chile

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73832.sa1](https://doi.org/10.7554/eLife.73832.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Temporal transcriptional response of Candida glabrata during macrophage infection reveals a multifaceted transcriptional regulator CgXbp1 important for macrophage response and drug resistance" for consideration by eLife. Your article has been reviewed by 4 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Kevin Struhl as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions (for the authors):

- While the ChIP-seq on Xbp1 is interesting, it is obtained in a condition different from the macrophage infection and makes both datasets difficult to compare, as pointed by three of the reviewers. As commented by one of them, information obtained in quiescent cells can not be easily translated to the highly dynamic macrophage environment. Perhaps this is one of the major technical issues of the work as the comparisons of the datasets may (or may not) be yielding relevant information. Potential ways to solve this would be to (i) successfully repeat the Xbp1 ChipSeq analyses in macrophages or (ii) obtain PolII-ChipSeq data from quiescent cells. Of course, the first one is the preferred one as it would really help to elucidate the role of Xbp1 during early times of infection.

A plausible reason of why the authors obtained little correlation in such Chip experiments is that Xbp1 levels are rather low and therefore hard to analyze, which could (indirectly) suggest that Xbp1 may not have an important role in this process. This should be addressed/discussed.

- The relevance of the identified DNA motifs should be further analyzed, particularly as one of them appears quite different from what has been reported in yeast (which could be addressed by having proper PolII data of equivalent datasets, or experimental validation of the motifs through EMSA, DNA footprinting or reporter systems)

- As indicated by the reviewers it is important to better assess the relevance and real significance of the observed fluconazole resistance: i.e MIC, the strength of the phenotype, etc.

- It is also suggested to strengthen some of the conclusions derived from the gene expression data with some experimental validations (i.e at 30 minutes, are C. glabrata actually internalized or just associated?, which may explain the difference in adherence genes at early time points). The paper contains interesting datasets that could provide hints of relevant biological events. It becomes important to explicitly distinguish which are suggested mechanisms (only inferred from expression signatures) to likely mechanisms (combining expression data with data that could help validate such ideas)

There are several other issues pointed out that could be addressed by modifying/editing the text (i.e including relevant references, indicating the new lessons emerging from the dataset, compared with existing microarray datasets, better explaining cut-off values) and that should not require additional experiments.

Reviewer #1 (Recommendations for the authors):

While the datasets are valuable and several observations are interesting, it is important to be cautious as the direct targets of CgXbp1 were characterized under one particular condition and the transcriptional analyses were obtained in another condition, one shown to be highly dynamic. Therefore, several inferred targets may or may not be under CgXbp1 control during macrophage infection. Most importantly, as it is, the study does not provide a clear parallel between one list of genes and the other one, to get a glimpse of such concepts. Since CgXbp1 shows to recognize distinct binding motifs, it becomes relevant to understand whether one group behaves differently from the other one in the absence of CgXbp1.

1. Line 180: "similar number of genes were transcribed in the mutant during macrophage infection (1,471 versus 1,589 genes in Cgxbp1Δ and wildtype, respectively) (Supplementary File 5) and ~90% of the transcribed genes are common between wildtype and the mutant (Figure 2—figure supplement 1C), suggesting that CgXbp1 has little effect on the overall set of genes transcribed during macrophage infection"

A relevant question that emerges here, is which are the genes that fail to appear activated in the CgXbp1 mutant. Such analysis is not clearly described in the Results section.

.- Line 265: "While the TCGAG motif is similar to the consensus recognition sequence of S. cerevisiae Xbp1 ([TCGA], Mai and Breeden, 1997)"

Please further compare the obtained sequence with other reported consensus sequences for Xbp1, some of which actually share the entire TCGAG core, see

http://cisbp.ccbr.utoronto.ca/TFreport.php?searchTF=T012464_2.00

3. Line 269: "Interestingly, the two motifs have different occurrence among the target promoters bound by CgXbp1MYC with the STVCN7TCT motif occurring approximately three times more frequent than the TCGAG sequence"

While it is true that the authors are performing their ChIP-seq studies in a condition that is quite different from the ones involved in macrophage invasion, it is important to establish some correlative data regarding how these (potentially) two types of promotors behave.

The ideal experiment would be for them to generate PolII-ChIP-seq data from quiescent cells (or if not then RNAseq data), in order to clearly establish co-regulation patterns among the genes of interest, comparing both WT and CgXbp1 mutant.

In addition, one would expect to detect that the genes allegedly being direct targets of CgXbp1 would show a certain level of co-regulation in the existing PolII-ChipSeq data, particularly the groups exhibiting similar cis-elements.

4. Line 332: "at this immediate stage (0.5 h) relative to the other time points (Group 6 genes in Figures 1CandD), indicating global suppression of gene expression in C. glabrata upon macrophage phagocytosis. A recent study showed that the fungal pathogen Cryptococcus neoformans also down-regulate translation during exposure to oxidative stress and suggested that translation suppression may facilitate the degradation of irrelevant transcripts during stress"

Please notice that the commented strategies imply different mechanisms compared with what the authors observed. Thus, while the authors evidenced decreased overall transcriptional rates (as measured by PolII-ChipSeq), the cited work exemplifies decreased translation which appears to also affect the stability of some mRNAs. Most importantly, the authors are not measuring steady-state levels of transcripts (as would be determined by RNAseq) and therefore for transcripts that exhibit medium to long half-lives, a decrease in transcriptional rates may not be causing a dramatic effect in reduced time scales (as compared with highly unstable transcripts).

5. Line 351: "In addition, the ChIP-seq experiment revealed that CgXbp1 directly binds to the promoter of many TFs including 10 carbon catabolite regulators (Figure 5G, Supplementary File 11), suggesting that CgXbp1 indirectly represses the activation of many gene regulatory networks. This probably explains the delayed activation of the carbon catabolic pathway genes"

a. Herein the authors should acknowledge the limitation of their studies as their Xbp1 chip data was obtained under a particular condition, quite different from the dynamic and multi-stimuli environment of a macrophage. Therefore, the identified targets may (or may not) be relevant when interacting with the macrophage.

b. The authors do not discuss whether these 10 genes appear (i) misregulated (higher expression) in the Xbp1 mutant and (ii) what is their behavior during the time course

6. Line 357: "Our overall findings suggest a regulatory model in which global transcriptional repression is established at the early infection stage to withhold transcriptional activation of certain genes whose functions are only required at later stages (Figure 7)"

While this is an interesting model, it is not straightforward to recognize in the dataset that the Xbp1 targets are indeed showing increased expression in the KO during the early stages of infection.

While Xbp1 binding to promoters is an important observation that strongly suggests that such target genes will be subjected to its repressive effect, it can also occur that some targets may not exhibit major changes upon Xbp1 deletion, It is key that the authors compare their Xbp1 Chipseq dataset with the transcriptional data (Pol II for both WT and mutant). As indicated earlier the most straightforward comparison would be to compare Chip and transcriptomic datasets obtained under the same experimental condition.

7. Line 380: "Interestingly, the latter motif (STVCN7TCT) was found at a higher frequency (~3 fold) than the common TCGAG motif from the CgXbp1MYC binding sites, suggesting that CgXbp1 can also form a dimer with another transcription factor that recognizes the STVCN7TCT sequence and that this hetero-dimer controls a larger number of genes than by CgXbp1 alone"

This is an interesting observation and raises the valid question of whether the cohort of genes differing in the type of cis-element present in their promoter show different transcriptional profiles regulated by Xbp1.

8. The discussion does not analyze the reduced virulence observed in Galleria mellonella.

Reviewer #2 (Recommendations for the authors):

This manuscript describes the temporal transcriptional response of Candida glabrata during macrophage infection and characterizes the role of the transcriptional repressor CgXbp1 the process. The manuscript is well written, the experiments were well conducted and the subject is very interesting.

However, a few issues should be addressed to improve the quality of the manuscript.

Lines 241-244 – It's difficult to understand the author's justification for failing to obtain reliable ChIP-seq results for Xbp1, when they got them for RNA PolII in the same "ever changing macrophage microenvironment during macrophage infection". The option for defined media makes it difficult to compare with the RNA PolII dataset. Please discuss this issue more thoroughly and, eventually, try again to obtain reliable ChIP-seq results for Xbp1 during macrophage infection.

Line 263 – the two "over-represented motifs" are very different from one another, making it hard to believe that they are both functional. I believe that some demonstration (SPR, EMSA, DNA footprinting, or even something simpler as assessing the effect of promoter mutations in Xbp1 effect on reporter gene expression) of which one works, would be really an important addition to the manuscript.

Line 285 – This section lacks standard MIC determination, to have a clear notion on the impact on fluconazole resistance. Also, the biphasic nature of the fluconazole growth curve is highly unusual. CFU determination conducted along the growth curve would help to assess whether the initial OD variation corresponds to real cell duplication or just changes in cell volume or aggregation.

Reviewer #3 (Recommendations for the authors):

The authors should include additional information on how the relative fold-change was calculated, and how the Z-score was determined. Without this information, it is hard to determine whether the upregulation is specific to macrophages, media change, temperature, etc., and therefore the comparator should be clearly defined.

The in-house script should be made available (either methods or github link)

Line 81-83, the way that it is written obscures the fact that 70% of the genes were not bound by PolII during infection. What does this mean for the ability of this technique to identify lowly transcribed genes that may nonetheless play important roles in biology?
