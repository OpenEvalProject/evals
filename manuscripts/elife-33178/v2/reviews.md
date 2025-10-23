# Peer review - Round 1

Editors:
- Rachel Green, Johns Hopkins School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.33178.036](https://doi.org/10.7554/eLife.33178.036)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "ICE1 promotes the link between splicing and nonsense-mediated mRNA decay" for consideration by eLife. Your article has been favorably evaluated by James Manley (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We have received comments from three experts in the field all of whom found the manuscript to present new and important information about the protein ICE1 revealed in the high throughput screen for factors critical for degradation of NMD substrates. Despite broad enthusiasm, the reviewers agree that several issues need to be addressed experimentally, in addition to changes in the text to rephrase the conclusions drawn from the experiments more cautiously. In case of modest effects, softer wordings such as "the data indicate/are consistent with/support the view" seem more appropriate than "demonstrate". Most critically, while it is clear that ICE1 impacts the amount of NMD-target mRNAs in the cell disproportionately relative to non-NMD-target mRNAs, the mechanism for this effect is not wholly clear. The reviewers recommend that the authors establish that ICE1 depletion does not alter splicing or block export from the nucleus, thus stabilizing the mRNA, and that mRNA stability is impacted and not simply overall levels (i.e. a decay experiment needs to be performed).

All reviewers had issues with Figure 4A (see detailed reviews). Finally, the reviewers had concerns about the magnitude and correlation of effects on mRNAs in UPF1 and ICE1 depletes. It seems likely that if the proposed mechanism is true (that ICE1 is involved in deposition of the EJC complex) then the RNA-seq data of the ICE1-delete should be even better correlated with that of the UPF3B-deplete than with the UPF1-deplete.

We hope these comments are helpful in revising your manuscript.

Reviewer #1:

In the current work, Baird et al. present the results of a shRNA-based genetic screen for genes involved in nonsense-mediated mRNA decay (NMD) of a luciferase reporter. While a number of their top hits are the same as those found in a previous CRISPR based screen using a fluorescent reporter, most of the hits are non-overlapping. Among the novel candidate NMD factors that they identify is ICE1, which they go on to characterize further. Depletion of ICE1 clearly leads to stabilization of NMD targets making it an exciting novel player in NMD. Further experiments suggest that ICE1 may act by aiding recruitment of the NMD factor UPF3B to the exon junction complex. While the authors make some headway in determining ICE1's mechanistic role in NMD (interactions with UPF3B in part through the MIF4G domain), it is still not clear that ICE's role in the process is direct. This work is an important advance, but some of the experiments require additional controls, and the evaluation of their mechanistic claims will likely hinge on these additional experiments.

1) Where are the UPF proteins in Figure 1C?

2) I found Figure 4A nearly impossible to interpret. What are the bands in the anti-flag panel blot in the anti-flag IP? Non-specific bands should be indicated as well as specific ones in both sides of the panel. It looks like the mock and 3XF-MIF4GICE1 lanes are identical, meaning that there's no evidence that the pulldown worked (or else this is a non-specific band which is lower in the 3XF-UPF3B lane). This is the only evidence for sufficiency of the MIF4G domain for interaction with eIF4AIII, so this figure needs to be clarified – and if these are the main data, the interaction is quite weak. Is MATRIN3 a control for non-specific association?

3) In Figure 5B, the total amount of GFP-UPF3B is not presented, only the nuclear/cytoplasmic ratio. Are the overall levels of UPF3B affected?

4) For the scatterplot in Figure 3—figure supplement 1A, both axes are normalized to the same siNT control dataset, which makes them poor evidence for similarity of UPF1 and ICE1 effects. For 3 arrays generated from a normal distribution (A, B, C), log(A/C) and log(B/C) will be highly correlated most of the time.

5) The last paragraph of the subsection “ICE1 depletion increases abundance of transcripts with NMD-inducing features” overinterprets the data in Figure 2E and Figure 2—figure supplement 1C. I think the simplest explanation for the differences in siICE and siUPF1 would be differences in knockdown efficiency, or perhaps differences in concentration requirements for activity. I don't think that these data represent evidence for a UTR-length dependent activity difference.

6) In Figure 4—figure supplement 1, it seems that there is some residual IP of UPF3B with ICE when UPF3B lacks the EJC-binding domain. Do these mutants display residual EJC binding? Some additional controls, perhaps with EJC factors or interacting proteins are required.

7) The authors argue that the activity of ICE1 is entirely through recruitment of UP3B to the EJC. The ideal experiment to test this would be an epistasis experiment, which may not be possible given the essentiality of the NMD machinery. However, it might be a start to check by RNA-seq that the genome-wide effects of UPF3B knockdown on NMD are similar to the effects of ICE1 on NMD. As it is, all of the genome-wide analysis presented is with comparisons of ICE to UPF1 knockdown.

8) In the Discussion: "interference with ICE1 function leaves the UPF2-UPF3B interaction intact". It is not clear to me from Figure 5A that this statement is true. The UPF3B/UPF2 interaction was not tested upon ICE1 depletion (or not presented). It seems like UPF2 may be more depleted at the EJC than UPF3b upon ICE1 depletion, but this was not quantified.

Reviewer #2:

Nonsense-mediated mRNA decay (NMD) detects and promotes the degradation of transcripts containing premature termination codons and other NMD-inducing features (i.e. long 3' UTRs, uORF translation). In metazoans, the efficiency of NMD is significantly enhanced by the presence of an exon junction complex (EJC) downstream of the terminating ribosome. The association of NMD protein UPF3 with EJCs is thought to underlie enhanced NMD by promoting recruitment of UPF2, which together stimulate UPF1 activity on the upstream terminating ribosome.

In this work, the authors perform a genome-wide RNAi screen in HEK-293 cells to identify novel factors required for degradation of NMD substrates, and identify ICE1, a protein previously characterized in promoting snRNA transcription. Notably, RNA-Seq analysis of cells depleted for ICE1 revealed a small increase in abundance of PTC-containing RNAs (over normal mRNA) and a modest elevation of transcripts harboring uORFs and particularly long 3' UTRs. Co-immunoprecipitation experiments demonstrate that ICE1 can interact with EJC core components in an RNA-independent manner, and that this interaction is mediated through a putative MIF4G domain within the C-terminus of the protein.

The authors propose that ICE1 depletion impairs the nuclear assembly of UPF3B into EJCs, resulting in impaired EJC-enhanced degradation of NMD substrates in the cytoplasm. Three pieces of evidence support this model. First, depletion of ICE1 results in the reduced association between UPF3B and EJC-core protein CASC3 by CoIP. Second, in ICE1 knock-down cells, there is an increased accumulation of UPF3B in the nucleus. Third, NMD activity in ICE1-depleted cells is partially rescued by overexpression of UPF3B.

This work proposes a novel function for ICE1 in promoting UPF3 assembly into EJCs and the downstream EJC-enhanced degradation of NMD substrates. While the model is consistent with experimental evidence, is not robustly supported by the data or directly tested. Moreover, additional interpretations could account for the experimental observations.

1) There are a number of pieces of data to suggest that ICE1 may have an independent or additional function in mRNA metabolism outside of promoting UPF3B association with EJCs.

a) While depletion of ICE1 appears to cause a reproducible reduction (but not elimination) in UPF3B association with core EJC components, its depletion increases the abundance of two characterized NMD substrates 4-fold greater than depletion of the core NMD factor, UPF1 (Figure 4B). This is completely unexpected if ICE1 function on these transcripts is through NMD.

b) While over-expression of UPF3B completely restores its ability to associate with EJCs (as measured by CASC3 CoIP; Figure 6A), the abundance of several NMD-sensitive mRNAs is only partially restored (~50%; Figure 6B) – indicating that abrogation of NMD in ICE1-depleted cells is not caused entirely by impaired interaction between UPF3B and the EJC.

c) A function for ICE1 in EJC assembly/remodeling is unexpected given its absence from past biochemical characterizations of EJC components.

2) It is never tested whether ICE1 function on NMD-substrate abundance is directly mediated through the NMD pathway. For example, ICE1 depletion should not alter mRNA levels in cells also inhibited for NMD (e.g. depleted also for UPF1).

3) The authors present evidence that the putative MIF4G domain of ICE1 is itself sufficient for mediating an interaction with EJC proteins and that over-expression of this domain can partially inhibit NMD (Figure 4). To further demonstrate of the importance and requirement of this domain and to help preclude an independent role for ICE1 in mRNA metabolism (through its activity in snRNA transcription, for example), the authors should examine the requirement of ICE1 lacking its putative MIF4G domain for interaction with EJCs and the observed reduction in NMD activity.

4) Experiments directly assessing a role for ICE1 in EJC assembly should be provided to support the main conclusion of this work. For example, the ability of UPF3B to assemble into EJCs in vitro should be evaluated in the presence and absence of ICE1 (with and without its MIF4G domain).

5) Given that the EJC composition is altered and that UPF3B is retained in the nucleus upon ICE1 depletion, the authors should provide evidence that NMD inhibition is not due to retention of mRNA in the nucleus or inhibition of translation in the cytoplasm.

6) Depletion efficiencies for the various factors are generally not reported (Figure 2D and 5A are notable exceptions) and controls are often lacking. Note that depletion of ICE1 in Figure 5A is quite poor.

Reviewer #3:

In a genome-wide siRNA screen using a Luciferase-based NMD reporter, Baird and colleagues identified – apart from some of the well-known NMD factors and the EJC core components – ICE1 as a new NMD factor. While the identification only one new NMD factor from such a "tour de force" approach may be somewhat disappointing, the authors did a nice job in investigating the role of ICE1 in NMD. So far, very little was known about ICE1 apart from an involvement in the assembly of the small elongation complex, which plays a role in snRNA transcription. Using a combination of knockdowns, overexpressions, RNA-seq, NMD reporter assays and IPs, the authors provide compelling evidence that ICE1 facilitates the assembly of UPF3B with the EJC core and thereby promotes EJC-enhanced NMD.

Before publication, the following two points should be addressed:

1) Figure 4A: It seems that the FLAG antibody failed to pull down the 3XF-MIF4G ICE1 construct. Instead you have a strong unspecific band (also present in the mock) that is detected with the FLAG antibody. Nevertheless, eIF4AIII is only detected in the IP of the cells expressing the ICE1 MIF4G but not in the mock. Something is not kosher with this IP; please explain.

2) Discussion: The authors state that ICE1 may be involved in degradation of a subset of 3'UTR-mediated decay targets. I wonder if this subset might be 3'UTRs that contain a spliced intron, and by inference an EJC, and thus belong to the EJC-enhanced class of NMD targets. Were the 3' UTR transcripts used for the analysis in Figure 2E filtered for transcripts lacking annotated introns in the 3' UTRs or could the observed effect originate from such "EJC-enhanced" NMD targets with 3' UTR introns? Consistent with my suggestion, the long 3' UTR of SMG5 mRNA is a NMD-inducing feature and contains no annotated intron, and this transcript was not affected by ICE1 knockdown (Figure 6B). Re-analyzing the RNA-seq data could perhaps solve this important question.
