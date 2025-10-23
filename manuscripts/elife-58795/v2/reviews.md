# Peer review - Round 1

Editors:
- Nahum Sonenberg, McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58795.sa1](https://doi.org/10.7554/eLife.58795.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The paper describes novel findings that show that TOR controls translation of mRNAs containing a 5′TOP (5' terminal oligopyrimidine tract) in plants (Arabidopsis) via LARP1. It also shows that LARP1 feeds back to control TOR activity, growth, and photosynthesis. While the major conclusion of the paper is that the TOP-LARP1-TOR axis is evolutionarily conserved, they show that additional pathways, which are responsible for ribosome biogenesis have co-opted this pathway for regulation.

Decision letter after peer review:

Thank you for submitting your article "Parallel global profiling of plant TOR dynamics reveals a conserved role for LARP1 in protein translation" for consideration by eLife. Your article has been reviewed by James Manley as the Senior Editor, Nahum Sonenberg as the Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Oded Meyuhas (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as part of a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

The paper describes experiments that show that TOR controls translation of 5′TOP mRNAs in Arabidopsis, via LARP1. It also shows that LARP1 feeds back to control TOR activity, growth, and photosynthesis. The authors demonstrated that transcription start sites (TSS) of Arabidopsis contain 5′TOP mRNAs and that their translation is specifically sensitive to TOR, like in mammals.

While the major conclusion of the paper is that the TOP-LARP1-TOR axis is evolutionarily conserved, they show that additional pathways, which are responsible for ribosome biogenesis have co-opted this pathway for regulation.

Essential revisions:

There are several issues that need to be addressed by experimentation or better explanation. Below please find some major comments that need to be addressed. The full reviews are also included to better explain these points:

1) The TSS analysis should be better presented. Figure 5B is hard to decipher -- a simple barplot indicating the number of CAGE reads at each position would help.

2) You need to confirm the TSS for some of the mRNAs using a different approach (e.g. primer extension, 5' RACE) as CAGE data quality can vary.

3) Because of the significant off-target effects on other major kinases of Torin 2 the results might not reflect the involvement of TOR signaling. It is therefore necessary to validate the findings using either a genetic approach or other inhibitors with a better selectivity profile (e.g. rapamycin, AZD8055).

4) You need to confirm that AtLARP1-target mRNAs are recognized through their 5' TOP sequence possibly by using reporter mRNAs that contain or lack TOP motifs and testing TOR regulation of their translation.

5) Figure 3 shows the LARP1 deletion slows growth. This is paradoxical given that LARP1 functions as a translation repressor. How can this be explained?

6) Does LARP1 control the stability of TOP mRNAs in plants like in mammals? You need to determine whether steady-state levels of putative TOP mRNAs are decreased in AtLARP1-deficient plants.

7) Since only a handful of cytosolic RP mRNAs have 5' TOP motifs, how is the coordinated synthesis of all rps achieved in plants? What could be the other mechanism(s) that ensure, if at all, the stoichiometric accumulation of all rps?

Reviewer #2:

The manuscript by Scarpin et al., reports the TOR-associated LARP1-dependent translation regulation of transcripts encoded by terminal oligopyrimidine mRNAs in Arabidopsis. The major conclusion of this paper is that the TOP-LARP1-TOR axis is evolutionarily conserved, although pathways additional to that responsible for ribosome biogenesis have coopted this method of translation regulation in plants. The authors performed a comprehensive analysis of transcriptome, ribosome footprint, and phosphoproteome levels in seedlings in the presence and absence of TOR inhibition and in larp1 deletion mutants. This study is of high enough quality and interest to warrant publication in eLife, as it will be of interest to a broad range of scientists and provides nice evolutionary perspective using a different model system than that typically used to assess TOR signaling. Furthermore, it bridges molecular studies with organismal studies, providing a nice perspective of the biological readout of the variables they choose to test. Finally, it annotates TOPs in plants and defines core TOPs.

Overall, the manuscript reads very well. The introduction is very nicely written, clearly outlining the progress of the field, the importance of the study, and how the work moves the field forward. The authors do a nice job of acknowledging the caveats of their observations. There are two major issues with this paper that should be addressed:

1) The breadth of the study is both a major strength and a weakness. While it is important to document and discuss the non-RP TOPs and how they are regulated, the amount of information provided makes reading these parts of the Results section tedious, yet is not enough to make these sections feel complete (each section is enough for one or two additional papers!). It reads as reporting on something first, rather than providing a sophisticated discussion of the biological underpinnings of their findings; nearly all of these sections conclude with a statement like "future investigations…" etc.

2) Figure 5B; the presentation of the data is not intuitive. It looks like CYDCD3;2, RACK1, el15b, PABP8, PIN1, and IAA26 might not be canonical TOPs. Could tracks be shown (like in Philippe, 2020) so that the predominant TSS for each TOP is apparent? Additionally, can the authors provide an example TOPscore calculation for CYCD3;2? By eye, it looks like +1G followed by a long stretch of pyrimidines. There are also examples that look like they are interrupted by purines, but their TOPscores do not seem to match.

Reviewer #3:

The manuscript of Scarpin and colleagues summarizes a very comprehensive attempt to establish the landscape of the downstream effectors of TOR and the respective affected processes in Arabidopsis. They conducted high throughput analyses in order to monitor the consequences of inhibiting TOR at global RNA (by RNA-seq) and protein (by proteomics) levels, as well as translation efficiency (by Ribo-seq) and protein phosphorylation (by phosphoproteomic). These experiments have yielded a broad, fundamental and timely picture of the engagement of TOR in a variety of processes common to a wide range of multicellular organisms, as well as ones unique to plant physiology.

Being aware of mTOR's positive role in the translational control of mammalian TOP mRNAs via LARP1 repression (as proposed by several reports), the authors set out to examine whether a similar mechanism is also applicable to plant cells. Surprisingly, their findings indeed support, at least partially, such an evolutionary conservation, as exemplified by the following observations: (a) the plant TOR appeared to control the translation of mRNAs, for some of which the vertebrate orthologues are bona fide TOP mRNAs; (b) LARP1 is a downstream target of TOR; (c) LARP1 deficiency prevented the repressive effect of TOR inhibition on a subset of mRNAs; and (d) some of these mRNAs are also equipped with a 5'TOP motif. These observations seem to expand the landscape of TOP mRNAs beyond the animal kingdom and shed some light on their evolutionary development. In addition, they lay the ground for future studies on the evolution of the structural attributes of TOP mRNAs and the mechanism underlying their translational control. Nevertheless, this manuscript still requires several clarifications and changes, as detailed below:

1) Introduction: " only a handful of cytosolic RP mRNAs themselves have 5.TOP motifs." What might be the explanation for the lack of a 5'TOP motif in the majority of rp mRNAs? How is the coordinated synthesis of all rps achieved in Arabidopsis if only a handful of them are subjected to translational control via the mTOR-LARP1 axis? What might be the other mechanism(s) that ensure, if at all, the stoichiometric accumulation of all rps?

2) Subsection “TOPscore analysis reveals conserved TOR-LARP1-5′TOP signaling axis”: the definition of TOPscore is quite permissive relative to that characterized the 5'TOP element in vertebrate or even in Drosophila. Namely, it may start with any pyrimidine, rather than the mandatory C residue at position +1 in TOP mRNAs in Drosophila and vertebrates. Moreover, the term 5'TOP motif, as used by the authors in the Arabidopsis context, seems somewhat elusive. Thus, how come the TSSs of IAA26 and of PIN1 (TSS1) mRNAs start with an A residue (Figure 5B), yet they have significantly higher TOPscore (5.5 and 7.8, respectively) than that of PABA8 (5.5) or TCTP1, that have a TSS at a C residue followed by 5 or 4 consecutive pyrimidines. These observations raise a question mark over the inclusion of the two former mRNAs as bona fide TOP mRNAs, especially when compared with the stringent definition of 5'TOP sequence that does not allow a purine at the cap site.

Readers that are familiar with definition of vertebrate 5'TOP motif are likely to be misled by the data as presented here. Hence, the authors should present a table in the Results that will replace Figure 5B, and will include all mRNAs that conform with the structural attributes of Drosophila and vertebrate 5'TOP motifs. This table should include all three columns of Figure 5B, as well as the second and third columns of Figure 5—figure supplement 1.

It should be pointed out, however, that the term ∆TE, as appears in Figure 5—figure supplement 1, is not well defined, at least not in the figure legend. Thus, it is not clear whether the value of -1.02 (is it on a log2 scale?) assigned for eEF1Bbeta1 in WT plants is considered as repression, nor what the value of -0.34 for the LARP1 plant mutant means. Does it represent an elimination of repression? In other words, this is not a 'user friendly' way to provide the reader with a clear picture of whether a given mRNA is subject to translational repression upon Torin 2 treatment and whether this repression is prevented in a LARP1 deficient mutant. The authors should consider the presentation of the data by a fold change in a non-logarithmic scale, which might make it easier for the reader to perceive, at a glance, the magnitude of the effects.

3) Subsection “Newly identified 5′TOP mRNAs in plants”: The authors suggest that "the direct control of RP translation 5′TOP motifs to coordinate ribosome biogenesis evolved later in an ancestor of vertebrates." Hence, they have to provide a reasonable explanation as to why, therefore, the 5'TOP motif evolved at all in some of the plant rps?

Reviewer #4:

TThe mTOR signaling pathway controls cell growth and is conserved throughout eukaryotes. Many mTOR effectors control the translation of mRNAs, but their functions have mostly been studied in yeast and mammalian cells. This manuscript from Scarpin et al., extends this analysis to plants. Through a combination of proteomic and transcriptomic methodologies, they identify key features of this system that are conserved in Arabidopsis, and others that are plant-specific. In particular, they show that AtTOR controls the translation of a class of mRNAs that contain 5' terminal oligopyrimidine (TOP) motifs through an RNA-binding protein called LARP1, as it does in vertebrates. This is surprising because, although LARP1 is conserved in plants, many of the classical TOP mRNAs (e.g. RP mRNAs) appear to lack TOP motifs. The authors conduct an unbiased analysis of plant 5' sequence data to show that some classical non-RP TOP mRNAs are unexpectedly conserved, and further identify other plant-specific TOP mRNAs.

Overall, this manuscript provides a comprehensive overview of AtTOR regulation of mRNA translation in plants and offers new insights into the evolution of this system. My primary concern is that the manuscript is often unfocused and without sufficient validation of claims. The strongest conclusion is that an ancestral version of TOR regulation of TOP mRNA translation via LARP1 is conserved in plants. However, many of the results and discussion are tangential to these findings. In particular, the phosphoproteomic analysis identifies some potentially new substrates, but these are not validated and the one that is most relevant to this study, AtLARP1, was already identified in a previous screen (Van Leene et al., 2019). Nonetheless, with suitable revisions, this manuscript would significantly contribute to our understanding of the conservation and function of TOR signaling across eukaryotes.

Essential revisions:

1) Torin 2 has significant off-target effects on other major kinases, including ATM, ATR, and DNA-PK (Liu, 2013). Some of the results presented here may therefore reflect the activity of other kinases. This is especially problematic for the phosphoproteomic analysis but might also affect transcription and translation results. The authors need to acknowledge this in the text, and, more importantly, validate the relevant findings using either a genetic approach or other inhibitors with a better – or at least different – selectivity profile (e.g. rapamycin, AZD8055) to repress TOR signaling. Are cytosolic and mitochondrial mRNA levels still repressed? Is the translation of plastidial RP mRNAs still repressed? Is the phosphorylation of proteins without obvious mTOR-regulate mammalian homologues (e.g. TOPLESS) still affected?

2) Many of the results and discussion related to the phosphoproteomic screen seem tangential to the main point of this manuscript, which focuses on LARP1. This is particularly true given that a recent phosphoproteomic study from Van Leene et al., (2019) also identified LARP1 as an mTOR target in plants. Other targets are interesting, but it's hard to assess their significance given the selectivity concerns described above. I recommend that this section be substantially reduced, or to focus more on translation targets.

3) The authors need to confirm that AtLARP1-target mRNAs are recognized through their 5' TOP sequence. This reviewer is not a plant biologist, but experiments would ideally involve introducing reporter mRNAs that contain or lack TOP motifs and testing TOR regulation of their translation.

4) Does LARP1 also control the stability of TOP mRNAs in plants? This is an important function in mammalian systems, although its stability function in plants may be more complex (see Merret et al., 2013). The authors should at least test whether steady-state levels of putative TOP mRNAs are decreased in AtLARP1-deficient plants, as this data has already been generated. This simple analysis would reveal whether this major function of AtLARP1 is also conserved.

5) Results from Figure 3 indicate that LARP deletion retards growth. This is paradoxical given that LARP1 functions as a translation repressor. How do the authors explain this? One possibility is that under the growth-promoting conditions used here, LARP1's translation functions are largely inactive. LARP1 may instead be acting primarily as an mRNA stabilizer, as mentioned above. The authors need to address this in the text based on results from comment #3.

6) The authors make the interesting observation that the translation of RP mRNAs is TOR-regulated, but through a LARP1-independent mechanism. Are there other features of At RP mRNAs that might account for this regulation? There seems to be an opportunity to identify new mechanistic signatures. Conversely, the authors show that LARP1 is not required for TOR-control of cytosolic RP mRNA translation, but what about plastidial ribosome mRNAs? These were shown to be TOR-regulated in Figure 1D.
