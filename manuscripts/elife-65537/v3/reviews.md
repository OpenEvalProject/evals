# Peer review - Round 1

Editors:
- Hao Yu, National University of Singapore & Temasek Life Sciences Laboratory Singapore

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65537.sa1](https://doi.org/10.7554/eLife.65537.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In this study, the authors examined the function of the RNA-binding protein FPA through analyzing its protein interactome and its global impact on gene expression using a combined approaches of Nanopore DRS, Helicos DRS, and short-read Illumina RNA-Seq. The combined datasets and new computational approaches developed by the authors showed a predominant role of FPA in promoting poly(A) site choice. The authors further revealed that FPA mediates widespread premature cleavage and polyadenylation of the transcripts of NLR genes, which act as important plant immune regulators. Overall, this study suggests that control of transcription termination processes mediated by FPA provides an additional layer of the regulatory dynamics of NLRs in plant immune responses.

Decision letter after peer review:

Thank you for submitting your article “Widespread premature transcriptiontermination of Arabidopsis thaliana NLR genes by the spen protein FPA” for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Hao Yu as the Reviewing Editor and Detlef Weigel as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Chae Eunyoung (Reviewer #1); Blake C Meyers (Reviewer #3).

Essential Revisions:

While there was agreement that the topic is timely and the findings relevant, there were some concerns regarding manuscript structure, inconsistency among some results, and interpretation of biological relevance of the data, as listed below, that need to be addressed to support the conclusions.

1. The manuscript presents an extensive body of studies in analyzing FPA interacting proteins and its potential RNA targets including NLRs. Although the overall results cover a series of observations, many of them are descriptive and divert the audience's attention from understanding the novelty and significance of the findings. Thus, we suggest that the authors re-organize the manuscript into a more coherent story and focus on the most important data pertaining to NLR control as shown in the title and the abstract.

2. The authors should address or explain some inconsistencies in the results as mentioned by reviewers. For example, the authors found that at least for some pathogens, "loss of FPA function does not reduce plant resistance". This is not consistent with the hypothesis that FPA is important for regulating NLR immune response genes, and the observation that premature exonic termination of RPP7 caused by FPA has a functional consequence for Arabidopsis immunity against Hpa-Hiks1.

3. The significance of this study will be strengthened by analysis of the biological relevancy of the alternative polyadenylation events mediated by FPA pertaining to NLR functions. We suggest that the authors consider either providing new experimental data or clearly interpreting existing results, such as those relevant to regulation of RPP7, to provide better insights into biological significance of the data presented in this manuscript.

Please also take into consideration the other specific comments from the reviewers below to revise the manuscript.

Reviewer #1:

The manuscript by Parker and colleagues presents an extensive body of work on characterizing the role of FPA in the choice of polyadenylation sites in transcripts of A. thaliana. Investigation on the mechanistic details that FPA engages on the mRNA processing was first initiated with the in vivo pull-down followed by LC-MS/MS, which revealed the its protein interactome relevant for 3'-end processing. The main dataset pertaining to the manuscript title comes from the comparative transcriptome analysis of Col-0, fpa-8 mutant and the overexpressor of FPA, 35S:FPA:YFP. The strength of this work lies in the use of nanopore DRS by demonstrating the layers of FPA-dependent transcripts, including its own, and its comparison to datasets by Illumina RNA-Seq and Helicos DRS. The systematic analysis uncovered unexpected complexity in the A. thaliana NLR transcriptome under the control of FPA and thus delivers a new insight on NLR biology. Several studies anecdotally have reported the importance of using genomic DNA, but not a single cDNA species, for addressing full functionality of NLR genes. Recent advances in NLRome sequencing from multiple genomes of a species and NLR structure/function studies also highlight the importance of understanding modular nature of NLR. As alluded with the modular diversity of NLRs kept in the genomes of a species in recent studies, NLR genes are prone to reshuffle in the genome to generate different variants, including partial entities with the loss of some parts of the proteins or even chimeras, supposedly maximizing the repertoire for defense. This work adds the level of transcript diversity on that of genomic diversity; FPA, an essential factor for transcription termination determinant, targets numerous NLRs to control the layers of NLR transcriptome of an individual plant. Although it is yet to be clarified for the regulatory significance of FPA-mediated NLR transcript changes under biotic or abiotic conditions, the authors succeeded in employing fine genetic schemes utilizing FPA-defective vs. -overexpressing lines along with long-read nanopore DRS technology for the first time to uncover the breadth of differential transcript generation focused on 3'-end choices. This work is timely and impactful for NLR research owing to the above-mentioned recent advances in NLR field.

As this work is the first of its kind in utilizing nanopore DRS to address NLR transcriptome, several technical concerns can be addressed to corroborate the claims made in the manuscript, which authors can find in the following section (1-8). Regarding the organization of the manuscript, the authors may consider to rebalance the two parts: FPA interactome vs. FPA targets and NLRs. Overall, the manuscript can be seen as combining two stories; first to characterize FPA function in 3'-end processing of transcripts inferred by interacting proteomes and meta-analysis of ChIP-seq data; second part includes detailed analysis of NLR transcripts and others. Although the first half of the analysis is a necessary prelude to the following NLR analysis, the current title and academic novelty mainly lies, or were intended by the authors, on the NLR analysis. However, current manuscript has relatively enlarged section of the first with NLR analysis packed into a series of supplementary dataset. If authors wishes to opt for highlighting NLR analysis, the following suggestions would help (9-14).

1) Earth mover distance (EMD) has been applied to identify a locus with alternative polyadenylation. What is the basis of using EMD value of 25 as a cutoff? According to Figure 4 B,D, EMD can range from 0-4000. One would also wonder if the distance unit equals bp.

In addition, EMD values of some genes (e.g. FPA and representative NLRs) can be specified in the main dataset so that significance of the cut-off values shall be appreciated.

2) Regarding the manual annotation of alternatively polyadenylated NLR genes (L1160-):

Genes with alternative polyadenylation were identified and the ending location was supported when there were minimum four DRS reads. It would be relevant to provide the significance of "the four" based on read coverage statistics, for example, with average read number covering an annotated NLR transcript with the specification of an average size.

3) Figure 4E shows that Ilumina-RNAseq dataset detects the number of loci with a different order of magnitude compared with the other two methods. Reference-agonistic pipeline shall be appreciated, however, the method engaged might have elevated the counting of paralogous reads mapped to different locations than they should be. Along with paralogous read collapsing, this is always a problem with tandemly repeated genes, such as NLRs by and large. For example, NLR paralogs in a complex cluster with conserved TIR/NBS but diversified LRRs would have higher coverage in the first two domains but drop in the diversified parts. The authors need to specify their bioinformatic consideration to avoid such problems.

Although the tone of the Illumina read section was careful and the main 3'-end processing conclusion was made by nanopore DRS, the authors are also advised to clearly state the limitation of using Illumina-RNAseq to address alternative polyadenylating sites at the beginning of the section, for example what to be maximally taken out from Figure 4 E and 4F. This will give relative weights to each dataset generated by different methods. One advantage of using Illumina data would be that the expression level changes can be associated with changes in processing, it seems.

4) At the RPP7 locus, At1g58848 is identical in sequences with At1g59218 as is At1g58807 with At1g59214 (two twins in the RPP7 cluster by tandem duplication). It would be good to check whether the TE At1g58889 readthrough indeed occurs in the sister duplicate with a potential TE in the downstream of At1g59218. If not, it can be used as an example of duplication and neofunctionalization through an alternative polyadenylation site choices.

5) HMM search shall be revisited to confirm if they are to detect the TIR domain. Given that a large proportion of NLRs in A. thaliana carry TIR at their N-terminal ends and the specified examples included TIR-NLR, it is surprising to see no TIR domain in Figure 5.

6) L659-668: how does the new data relate to the previously TAIR annotated At1g58602.1 vs At1g58602.2 (Figure 6, Inset 1)? It would be good to see these clearly stated in the main text as compared to newly identified ones. From the nanopore profiling, At1g58602.2 appears to be the dominant form.

7) One thing to note is that in the overexpressor of which Hiks1 R is suppressed, there was hardly any At1g58602.1 produced in addition to the large reduction of At1g58602.2. Thus, relative functional importance of the two transcripts shall be discussed in line with the Hpa resistance data. Accordingly, L740-741 phrasing shall be revised to include the possibility of absolute or relative "depletion" of functional transcript(s) contributing to the compromise in Hpa resistance.

8) It would be necessary to state in the main text the implication of phosphorylation on the two Ser residues on Pol II at L245. A clear description distinguishing the effect of the two phosphorylation and the specificity of the antibodies is desirable, as the data was interpreted as if the two sites made differences, such that Ser2 was heavily emphasized (e.g. subtitle). Albeit low level, Ser5 data also shows an overlap with FPA ChIP-seq coverage at the 3' end. If there is a statistical significance to be taken account to interpret the coverage, please state it. Given that elongation occurs progressively, I wonder how much should be taken out from the distinction.

9) Figures presentation for RPP4 and RPP7 are great in detailing the FPA-dependent NLR transcript complexity. To make the functional link more evident, the authors may consider bringing up parts of the Figure 5-supplement to a main Figure to detail the revised annotation of NLRs. Given recent advances in NLR structure and function studies, extra domain fusion, fission and truncated versions of NLRs require a great deal of attention. For example, potential functional link to the NMD-mediated autoimmunity and revised annotation of At5g46470 (RPS6) needs a clear visual guidance preferably with a main figure (Figure 5-Sup3).

10) The section "FPA controls the processing of NLR transcripts" includes dense information and can be broken down to several categories. To this end, Supplement File 3 (NLR list) shall be revised to deliver the categorical classes and further details and converted to a main table.

For NLR audience, for example, it would be important to associate the information to raw reads to assess where the premature termination would occur. At least, the ways to retrieve dataset or to curate the termination sites shall be guided.

On the contrary, there is no need to include other genes in Figure 4-Figure Supplement 4-8 under this section. They are not NLRs.

11) Figure 7 and IBM1 section can be spared to supplement.

12) The list of "truncated NLR transcripts" in particular, either by premature termination within protein-coding or with intronic polyadenylation, should be made as a main table. The table can be preferably carrying details in which degree the truncation is predicted to be made. With current sup excel files, it is difficult to assess the breadth of the FPA effect on the repertoire of NLRs and their function. This way, functional implication of differential NLRs transcriptome can be better emphasized.

13) FPA-mediated NLR transcript controls, as to promote transcript diversity, is expected to exert its maximum effect if FPA level or activity is subject to the environmental stresses, such as biotic or abiotic stresses. The discussion on effectors targeting RNA-binding proteins (L909-918) is a great attempt in broadening the impact of this research. In addition, if anything is known to modulate FPA activity, such as biotic or abiotic stresses or environmental conditions, please include in the discussion.

14) NLR transcript diversity as source of cryptic variation contributing to NLR "evolution" is an interesting concept, however, evolutionary changes require processes of genic changes affecting transcript layers or stabilizing transcriptome diversity. In the authors' proposition in looking into accessions, potential evolutionary processes can be further clarified.

Reviewer #2:

Parker et al attempted to show that the FPA protein functions to regulate the widespread premature transcription termination of the Arabidopsis NLR genes. Using in vivo interaction proteomic-mass spectrometry, FPA was shown to co-purified with the mRNA 3' end processing machinery. Metagene analysis was used to show that FPA co-localized with Pol II phosphorylated at Ser2 of the CTD heptad repeat at the 3' end of Arabidopsis genes. Using a combination of Illumina RNA-Seq, Helicos, and nanopore DRS technologies, FPA was found to affect RNA processing by promoting poly(A) site choice, and hence controls the processing of NLR transcripts whereas such process is independent of IBM1.

Overall, it is a potentially important research. The data is rich and could be useful. However, the biological stories described are not thoroughly supported by the data presented, especially when the authors tried to touch on several aspects without some important validations and strong connections among different parts. Some special comments are provided below:

(1) The title of this manuscript is "The expression of Arabidopsis NLR immune response genes is modulated by premature transcription termination and this has implications for understanding NLR evolutionary dynamics". Therefore, the readers will expect some functional connections between the FPA and the novel NLR isoforms due to premature transcription termination. However, the transcript levels of plant NLR genes are under strict regulation (e.g. Mol. Plant Pathol. 19:1267). Since the functions of NLR genes are related to effector-triggered immunity, it is more important to study the function of FPA on premature transcription termination when the plants are challenged with pathogens. In this manuscript, most transcript analyses are based on samples under normal growth conditions. It is therefore a weak link between the genomic studies and the functional aspects. For instance, it is more important to identify unique NLR isoforms produced upon pathogen challenges that are regulated by FPA. The authors will need to provide some of these data to fill this gap.

(2) Since the function of FPA is to regulate NLR immune response genes, we should expect a change in plant defense phenotype in FPA loss-of-function mutants. Could the authors provide more information on this? On the contrary, in line 728 of this manuscript, the authors found that at least for some pathogens, "loss of FPA function does not reduce plant resistance". It is not consistent with the hypothesis that FPA is important to regulate NLR immune response genes.

(3) Furthermore, the authors mentioned in lines 729-731 "Greater variability in pathogen susceptibility was observed in the fpa-8 mutant and was not restored by complementation with pFPA::FPA, possibly indicating background EMS mutations affecting susceptibility." Does it mean that fpa-8 contains other mutations? Will these additional mutations complicate the results of the RNA processing? Could the authors outcross the fpa-8 mutation to a clean background?

(4) In line 318, the authors found 285 and 293 APA events in the fpa-8 mutant and the 35S::FPA:YFP construct respectively, but only 59 loci (line 347) exhibited opposite APA events (about one fifth). The low overlapping frequency suggests that some results could be false positive.

(5) In line 732-736: "In contrast, 35S::FPA:YFP plants exhibited a similar level of sporulation to the pathogen-sensitive Ksk-1 accession (median 3 sporangiophores per plant). This suggests that the premature exonic termination of RPP7 caused by FPA has a functional consequence for Arabidopsis immunity against Hpa-Hiks1." It is contradictory to the statement in line 728 that "loss of FPA function does not reduce plant resistance". Is it possible that overexpression of FPA:YFP had generated an artificial condition that is not related to the natural function of FPA?

(6) The fpa-8 mutant has a delayed flower phenotype (Plant Cell 13:1427). Could the 35S::FPA:YFP fusion protein construct reverse this phenotype and the plant defense response phenotype? It is important to interpret the data when the 35S::FPA:YFP construct was used to represent the overexpression of FPA.

(7) Under the subheading "FPA co-purifies with the mRNA 3' end processing machinery". The results were based on in vivo interaction proteomics-mass spectrometry. MS prompts to false positives and will need proper controls and validations. Have the authors added the control of 35S:YFP instead of just the untransformed Col-0? At least for the putative interacting partners in Figure 1A, could the authors perform validations of some important targets, using techniques such as reverse co-IP, or to show direct protein-protein interaction between FPA to a few of the important targets by in vitro pull-down, BiFC, or FRET, etc.

(8) In Fig. 3, the data show that the last exon of the FPA gene is missing in the FPA transcripts generated from the 35S::FPA:YFP construct. Will the missing of this exon affect the function of the transcript and the encoded protein?

(9) The function of FPA is still ambiguous. There was a quantitative shift toward the selection of distal poly(A) sites in the loss-of-function fpa-8 mutant and a strong shift to proximal poly(A) site selection when FPA is overexpressed (35S::FPA:YFP) in some cases (Fig. 3, Fig. 5, Fig. 8). But the situation could be kind of reversed in other cases (Fig. 6). What is the mechanism behind it?

(10) Under the subheading: "The impact of FPA on NLR gene regulation is independent of its role in controlling IBM1 expression". IBM1 is a common target of FPA and IBM2. Indeed, FPA and IBM2 share several common targets (Plant Physiol. 180:392). It may be more meaningful to compare the impact of FPA and IBM2 on NLR gene instead.

(11) In lines 423-425, the authors described "Consistent with previous reports, the level of mRNA m6A in the hypomorphic vir-1 allele was reduced to approximately 10% of wild-type levels (Parker et al., 2020b; Ruzicka et al., 2017) (Figure 4-figure supplement 3)." This data could not be found.

(12) In line 426: "However, we did not detect any differences in the m6A level between genotypes with altered FPA activity." Which data this statement is referring to?

Reviewer #3:

In the article "Widespread premature transcription termination of Arabidopsis thaliana NLR genes by the spen protein FPA", the authors describe the function of FPA as a mediator of premature cleavage and polyadenylation of transcripts. They also focused their study on NLR-encoding transcripts, as that was their most novel observation, describing an additional layer of control.

In general, the article is well written and clear. The experimental design is good, they didn't seem to over-interpret the results, the controls were solid, and the nanopore data were quite informative for their work. It is rather descriptive maybe bordering on dry in parts - but the results will be helpful for those working on NLRs, and demonstrate the utility of bulk long-read transcript data. The authors were able to string together a number of descriptive observations or vignettes into an informative paper. Overall, it is solid science, but maybe not monumental.

One minor complaint is that the authors don't focus on NLRs starting on line 436, and then they have extensive results on NLRs; by the time I got to the discussion, I'd forgotten about the early focus on the M6A. While the first part of the article is necessary, I would suggest a more concise results section to give the paper more focus on the NLR control (since that is emphasized in the abstract and the title of the manuscript).

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
