# Peer review - Round 1

Editors:
- Satyajit Rath, Indian Institute of Science Education and Research (IISER) India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53704.sa1](https://doi.org/10.7554/eLife.53704.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Comprehensive analysis of antiviral adaptive immunity formation and reactivation down to single-cell level" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Satyajit Rath as the Senior and Reviewing Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Benjamin Chain (Reviewer #1); Philip Bradley (Reviewer #2).

The reviewers have discussed the reviews with one another and with the Reviewing Editor. Clearly, the study is interesting and worthy of publication, despite the limitation that it is based on only two individuals. However, the manuscript is poorly constructed, and hence very hard for a non-specialist to understand the message. Substantial revision and focusing are essential. Both reviewers have made these points in specific ways. Therefore, instead of a synthesised decision, both reviews are being provided in full below for ease of specific addressing to help you prepare a revised submission. The major issues raised by both reviewers must be substantively addressed in order to increase enthusiasm for publication.

Reviewer #1:

This paper contains a descriptive study of TCR sequencing and some single cell RNAseq on one primary, and two secondary responses to yellow fever vaccination in humans. There are definitely some interesting and intriguing observations here, although the study essentially remains a case-report, with many results supported by data from one single individual. How strongly these findings will generalise remains to be determined. The impact of the paper is weakened by a very loose and anecdotal writing style, and an attempt to include a large number of disparate findings. The paper could be much improved by more effort to clearly identify a small number of key messages and support them with data.

The authors focus on large clonal expansions (>32 times frequency post-primary mmunisation) and show that the secondary response contains many fewer large clone expansions than the primary response. Interestingly, a large proportion of clones expanded in primary responses can be resampled in the secondary. Almost as an aside they claim they can pair α and β chains by timecourse similarity alone (but see comment below). I found the PCA analysis and the clone pairing extraneous to the message of the paper, and merely a distraction.

They next demonstrate that most YF-specific clones switch from EM to EMRA phenotype post immunisation. This is an intriguing observation, given that the bulk population of EM is much larger than the EMRA one, but this observation is not followed up at all. Strangely there are no CD8 CM cells. Next, the authors analyse TCRs specific to the immunodominant epitope, which they show accounts for 60% of the total number of CD8 clones responding in primary immunisation. Next the authors analyse the TCR sequences of the immunodominant epitope, which they demonstrate fall into at least two distinct clusters of sequences. They support their claim that the two sets of TCRs bind via different modes by using some homology modelling, although this is buried in the supplementaries, and it is not clear how much weight to give to these results. Finally the authors use sc RNAseq to look at these clones, and show that they are heterogeneous, and specific clones are biased towards specific phenotypes.

Specific points:

I didn't follow exactly how the authors defined responding TCRs. They mention both a p value, and a cut-off of 32 fold enrichment. How are these related ?

The Y-axis in many panels is given as% YF_responding cells. This is very ambiguous – do they mean the fraction of cells which respond as a proportion of all cells ? Do all panels mean the same thing. This needs clarification.

In the section of TCR pairing, the authors state that they can correctly identify a large proportion of scTCRs using this approach on bulk sequences. But they also say, they pair each α with five nearest betas. So what do they mean by "correct paring": one of the five they computationally pair is the correct pair as determined by scTCR ? This is all very unclear.

Reviewer #2:

This manuscript reports a detailed characterization of T cell responses to Yellow Fever vaccination in two individuals, one over the course of primary and secondary (after 18 months) vaccination, and one a secondary vaccination 30 years after initial vaccination. The main strengths of the study are (1) the detailed, longitudinal characterization of the TCR repertoires (unpaired α and β chain) in bulk PBMCs as well as sorted T cell subsets (>15 time points over the two individuals), (2) bulk α/β and paired TCRseq data for T cells that bind an immunodominant A*02:01-restricted YFV epitope (NS4B), (3) paired scTCRseq and scRNAseq data for several thousand T cells positive for NS4B from one of the donors prior to their secondary vaccination, and (4) new and interesting analytical approaches for TCR repertoire analysis (time-course clustering, computational α/β pairing, scRNAseq profiles of T cell clonotypes). In my view the main weaknesses are the small number of donors and the mostly confirmatory nature of the biological results in light of the existing literature on YFV vaccination. Nonetheless I am enthusiastic about the study: the repertoire and RNAseq data will benefit others working in this area, and the new methods look like they will have a wide range of applications. I have a few questions/clarifications/potential typos, as detailed below.

– Clonotypes were assigned CD4/CD8 according based on the subset in which they had the highest frequency: did any clones span both the CD4+CD8 compartments, robustly (in terms of UMI counts)? Would you attribute these to sorting noise?

– My read of the paper is that for donor M1, YFV-responding clonotypes were defined in terms of their counts in the primary response. These clonotypes were then used to assess the magnitude of the secondary response. This begs the question of whether any new clonotypes were recruited into the secondary response. Are any new YFV-responding clonotypes identified by edgeR in the secondary response? Or are the frequency changes just too low to call new responding clones?

– How many of the NS4B-specific clones were called as YFV-responding by edgeR? Were there "genuine" NS4B-binders that did not expand? And did they have any special features? If so, were TRAV12 and TRAV27 NS4B+ clonotypes equally likely to be called as responding by edgeR?

– "Overall the dynamics and the magnitude of this response was very similar to the response to the booster vaccination after 18 months we observed in donor M1", maybe this is splitting hairs but to me the P30 response looks a little slower. Is this true/significant?

– I'm a little confused by the memory subset sorting. Where would plain old T effector cells show up here? How would they be distinguished from the memory subsets? Is there also CD45RO data? Or is there an assumption about composition based on the timepoints analyzed?

– "Interestingly, we found that the largest YF-specific CD8+ clones did not expand in response to the booster vaccine. Instead, the most expanded clonotypes were rare prior to the booster immunization (Figure 2—figure supplement 3A).", I think this should be "Figure 2—figure supplement 3B" if you are really talking about CD8 here.

– "While for most CD8+ clonotypes in the total repertoire EM/EMRA phenotypes were stable between day 15 and day 45 (Figure 3B, and Figure 3—figure supplement 2A, C), the distribution of CD8+ YF-responding clones between memory subsets was significantly shifted towards the EMRA phenotype (Figure 3C)." I don't see "CD8" in Figure 3B/C or Figure 3—figure supplement 2 (figure or legends), are there labels missing? Or are Figure 3C/Figure 3—figure supplement 2 actually PBMC?

– Figure 3A, legend, typo: "EM (CD45RA-CCR7+)"

– "Prior to dimensionality reduction, data were scaled so that the mean expression was 1 and the variance equals to 1", I think maybe this should say "mean expression was 0"?
