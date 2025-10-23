# Peer review - Round 1

Editors:
- Hao Yu, National University of Singapore & Temasek Life Sciences Laboratory Singapore

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65537.sa1](https://doi.org/10.7554/eLife.65537.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

In this study, the authors examined the function of the RNA-binding protein FPA through analyzing its protein interactome and its global impact on gene expression using a combined approaches of Nanopore DRS, Helicos DRS, and short-read Illumina RNA-Seq. The combined datasets and new computational approaches developed by the authors showed a predominant role of FPA in promoting poly(A) site choice. The authors further revealed that FPA mediates widespread premature cleavage and polyadenylation of the transcripts of NLR genes, which act as important plant immune regulators. Overall, this study suggests that control of transcription termination processes mediated by FPA provides an additional layer of the regulatory dynamics of NLRs in plant immune responses.

Decision letter after peer review:

Thank you for submitting your article "Widespread premature transcription termination of Arabidopsis thaliana NLR genes by the spen protein FPA" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Hao Yu as the Reviewing Editor and Detlef Weigel as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Chae Eunyoung (Reviewer #1); Blake C Meyers (Reviewer #3).

Essential Revisions:

While there was agreement that the topic is timely and the findings relevant, there were some concerns regarding manuscript structure, inconsistency among some results, and interpretation of biological relevance of the data, as listed below, that need to be addressed to support the conclusions.

1. The manuscript presents an extensive body of studies in analyzing FPA interacting proteins and its potential RNA targets including NLRs. Although the overall results cover a series of observations, many of them are descriptive and divert the audience's attention from understanding the novelty and significance of the findings. Thus, we suggest that the authors re-organize the manuscript into a more coherent story and focus on the most important data pertaining to NLR control as shown in the title and the abstract.

2. The authors should address or explain some inconsistencies in the results as mentioned by reviewers. For example, the authors found that at least for some pathogens, "loss of FPA function does not reduce plant resistance". This is not consistent with the hypothesis that FPA is important for regulating NLR immune response genes, and the observation that premature exonic termination of RPP7 caused by FPA has a functional consequence for Arabidopsis immunity against Hpa-Hiks1.

3. The significance of this study will be strengthened by analysis of the biological relevancy of the alternative polyadenylation events mediated by FPA pertaining to NLR functions. We suggest that the authors consider either providing new experimental data or clearly interpreting existing results, such as those relevant to regulation of RPP7, to provide better insights into biological significance of the data presented in this manuscript.

Please also take into consideration the other specific comments from the reviewers below to revise the manuscript.

Reviewer #1 (Recommendations for the authors (required)):

Comments on reference, figure/legend and typesets

1. The reference style shall be uniform. Currently, there seem to be two different formats with two author presentation in the parenthesis earlier in the document and with one author later in the document (e.g. Takagi, Iwamoto et al., 2020 vs Takagi et al., 2020). In addition, there are several articles missing full citation information (e.g. Parker MT et al., 2020a (not found by search, supposedly hen2-2 data according to main text), 2020b; Nat Communications citation format to be checked).

2. L844: Barragan et al., 2020 MBE is a good one to add as this work identifies a truncated NLR as the culprit of autoimmunity in an A. thaliana hybrid.

3. L846: One of highly appreciated works on TIR-only protein is by Nishimura et al., 2017 PNAS 114 (10): E2053-62 on RBA1, which should be cited.

4. L919: RPP7 locus spawning recurrent risk alleles was exemplified with later cases reported by Chae et al., 2014 (Cell) and Barragan et al., 2019 (PLoS Genetics). A proper term for RPP7 is "NLR genes at the RPP7 locus" as to consider allelic diversity. L924: hybrid "necrosis" should be used in this case instead of weakness.

5. It will be of interest how many of NLRs with alternative 3'-end processing detected in this study reside in a multi-gene cluster. As tandem repeats of highly similar genes tend to create problems in informatic analysis, this notion shall be carefully visited. Not only the technical side but also related to discussion on evolutionary dynamics, this notion can be related to the authors' proposition of cryptic transcript variation affecting evolutionary dynamics.

6. In all figures, the proportion of the panel pointer text (e.g. A, B) and actual text shall be modified. As compared to the panel pointer, actual texts seem disproportionately small and sometimes hard to read.

7. In the insets in Figures 6 and 8, there are transcripts arrow-pointed to indicate alternative 3'UTR or non-stop transcripts. I believe those are also present in other genotypes, most importantly in Col-0. Please be advised to point all the affected transcripts instead of pointing the ones in mutant genotypes. Using asterisk heads would be an option.

8. AGI locus identifier (At2gXXXXX) is conventionally not italicized. The authors may check with the journal for the final typesetting.

9. Data and code availability shall be updated on the XXX marked areas.

10. L73-74: italicize the gene name in full and abbreviation, as was done for RPP7 in L78-79.

11. L460: add hyphen (-) between nucleotide and binding.

12. L460: the wording should be genes encoding NB-ARC, Rx-like CC, OR LRR. Otherwise, it indicates genes encoding the three domains all together, which is not the data presented in Figure 5.

13. Figure 5 A, B: what is the difference between Rx-like CC and Rx N-terminal? If the HMM analysis picked up ZAR1 CC (latest structure of CNL), using ZAR1 will attract a broad audience in the NLR field.

14. L470: CCR shall be properly abbreviated or replaced with RPW8-like CC.

15. L474: indicate how many out of 206 NLRs were reannotated instead of using "some". Suggested table would help (see above comments).

16. Figure 5-Sup1: fix the typos in AGI identifiers in the bolded faced title (typos in both).

17. L883: meant for trials or trailing?

Reviewer #2 (Recommendations for the authors (required)):

This is an interesting piece of work. However, there are some essential data and analyses required to support the conclusions.

1. If the authors would like to tie the story with NLR regulation, the physiological functions of FPA in relation to plant defense response should be shown. Right now the disease resistance-related phenotypes of the loss of function mutant fpa-8 and the overexpressor 35S::FPA:YFP are quite weak.

2. The authors should clarify whether there could be additional mutations in fpa-8 as they have suggested.

3. For the MS experiments, a YFP-only control is essential to reduce the noise due to false positives. Validation of interactions to selected key target interacting partners are important to confirm the accuracy of the findings.

4. If the authors really want to discuss the functional relationship between FPA and IBM, IBM2 could be more relevant in this study.

5. The authors should provide a better explanation/model for the observation that a quantitative shift toward the selection of distal poly(A) sites in the loss-of-function fpa-8 mutant and a strong shift to proximal poly(A) site selection when FPA is overexpressed (35S::FPA:YFP) in some cases (Figure 3, Figure 5, Figure 8). But the situation could be kind of reversed in other cases (Figure 6).

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Widespread premature transcription termination of Arabidopsis thaliana NLR genes by the spen protein FPA" for further consideration by eLife. Your revised article has been evaluated by Detlef Weigel (Senior Editor), Hao Yu (Reviewing Editor) and three reviewers who reviewed the last version of the manuscript.

We feel that this revised manuscript has been significantly improved, but there are some remaining issues that need to be addressed, as indicated in the following comments given by Reviewers 1 and 2.

Reviewer #1 (Recommendations for the authors):

The authors made great efforts to reorganize the manuscript to address comments from all three reviewers. Current manuscript supports the main claim on FPA modulating the NLR regulation with a series of graphic illustration as main figures with supporting supplements. These encompass the breadth of regulatory roles of FPA on different NLR genes, in particular. Their quantitative assessment of the FPA effects on clustered or hypervariable NLR genes have been performed in a sound way, taking on the latest research outcomes (2020-2021 publications) on NLR diversity and evolution.

Reviewer #2 (Recommendations for the authors):

Overall, it is a piece of interesting research supported with rich data. The authors have addressed much of the concerns in the revised version and through further explanations. Some remaining questions could be addressed via clarification, strengthened comparison, and additional discussions.

1. In relation to my original Question 1. Since the title of this manuscript is "Widespread premature transcription termination of Arabidopsis thaliana NLR genes by the spen protein FPA" and some NLR gene expressions are responsive to pathogen attack, the readers may be interested to know the changes in NLR genes under pathogen attack conditions that are regulated by FPA. If the authors have these data, it will be great to share.

2. In relation to my original Question 2 and Question 5. Since overexpression of FPA only partially reduces the level of functional RPP7 transcripts, is it possible that FPA overexpression also acts on other NLR transcripts that leading to loss of resistance?

3. In relation to my original Question 4. Is it possible to make a comparison directly between the 35S::FPA:YFP line versus the fpa-8 mutant to investigate see whether all disappeared pre-mature transcriptional terminations have returned to the level of Col-0 or even more?

4. In relation to my original Question 6. The authors showed that overexpression FPA will decrease the overall FLC transcripts. Is the FPA acting on the pre-mature transcriptional termination of FLC too? Any data to support this?

5. In relation to my original Question 7. Does the anti-FPA chip data match well with the proximal APA in Col-0?

6. In relation to my original Question 9 and Question 10. IBM1 is a common target of FPA and EDM2, indicating the possible coordination of the FPA and EDM2 functions. There have been several studies on EDM2, could the authors compare the target of FPA and EDM2, and also address whether FPA also targets TEs in introns of function genes similar to that of EDM2?

Reviewer #3 (Recommendations for the authors):

I am satisfied with the authors' response to the reviewers, including the valuable points raised by the other reviewers. The extensive changes that the authors made to the manuscript have substantially improved the work.
