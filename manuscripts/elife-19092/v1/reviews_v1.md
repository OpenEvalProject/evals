# Peer review - Round 1

Editors:
- Yijun Qi, Tsinghua University , China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.19092.037](https://doi.org/10.7554/eLife.19092.037)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Long Non-coding RNA Produced by RNA Polymerase V Determines Boundaries of Heterochromatin" for consideration by eLife. Your article has been favorably evaluated by Detlef Weigel (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal her identity: Rebecca Mosher (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Using RNA Immunoprecipitation coupled to high-throughput sequencing (RIP-seq), you have globally identified transcripts of RNA polymerase V (Pol V). You have further analyzed the correlations between Pol V transcription and Pol V binding, DNA methylation, siRNA accumulation and genomic features. Your analyses clarify several key questions regarding Pol V transcription and RNA-directed DNA methylation. You propose that Pol V transcription plays an important role in the determination of heterochromatin boundaries.

The reviewers agreed that such findings should in principle be published at the highest level. While the reviewers furthermore agreed that the data presented are clear, they also agreed that some conclusions went considerably beyond what the data showed directly. To bring the interpretation more in line with the data, they asked you to tone down your claims, and also to perform additional analyses to support your claims.

Essential revisions:

1) Analyze whether gene body methylation can direct Pol V transcription. This analysis can be easily done using the already available datasets and will address the question whether methylation alone is sufficient to direct Pol V.

2) The conclusion that AGO4 interacts with RNA exiting Pol V is not supported by sufficient data. Tone down this claim by rewording as reviewers #1 and #2 suggested or provide new data to strengthen it.

3) Examine the role of Pol IV in targeting RdDM to TE edges by performing analyses as done for Pol V. Alternatively, tone down the claim that Pol V is the main determinant for RdDM targeting and do not exclude the possibility that Pol IV also plays a similar role.

We have included the full reviews, which mention separate points for essential revisions. Reviewer #1 suggested web-lab experiments to validate some of your genome-wide analyses, but after discussion, we agree that these experiments are unnecessary. Meanwhile, we agree that other suggestions raised by reviewers #1 and #2 are valuable and most of them can be addressed by rewording. We ask you to take them into account as well.

Reviewer #1:

In the RNA-directed DNA methylation pathway, Pol V transcripts have been proposed as scaffold RNAs that recruit AGO4/siRNA effector complexes through base-pairing between the transcripts and siRNAs. In this manuscript, the authors present a comprehensive study that provides new evidence supporting previously proposed model for the role of Pol V transcripts at the effector stage of RdDM. Some of the findings advance the current understanding of RdDM and should be of general interest as well. My major criticism is that many statements made by the authors are too bold and not supported by sufficient data. The author should be more careful with interpretation of their seq data analyses.

1) The first two sections of Results can be organized in a more concise way. The authors should note the difference between "Pol V-associated RNA" and "Pol V transcript". For an example, in the first section, the authors mentioned that a considerable number of Pol V-associated RNAs were not Pol V-dependent, but in the second section, they concluded: "Pol V-associated RNAs are produced by Pol V".

2) The authors have not successfully identified the promoters of Pol V, thus the use of "The Pol V promoter" as the subtitle of the third section of Results is inappropriate.

3) The authors analyzed Pol V transcripts in ago4 mutant and found that 1) the levels of Pol V transcripts were reduced in ago4 and 2) average length of Pol V transcripts in ago4 was similar to that in Col-0. As the authors mentioned, the reduction in Pol V transcript level in ago4 could be from an indirect effect of ago4 mutation on Pol V transcription. Thus, the authors should not conclude that AGO4 and IDN2 stabilize Pol V transcripts and use it as the subtitle of the section. The authors also concluded that Pol V transcripts are not sliced by AGO4, solely based on the data showing that average length of Pol V transcripts in ago4 was similar to that in Col-0. The authors should consider an alternative interpretation of the data: the cleavage products of AGO4/siRNA were small and not detected by Pol V RIP-seq in Col-0 as there are many siRNAs that cover the entire region of a Pol transcript.

4) The seq data described in the section "siRNAs base pair with RNA exiting Pol V" basically supported a correlation between AGO4 binding to Pol V transcripts and RdDM but cannot be used to exclude the possibility that AGO4 binds to DNA. The authors provided an explanation for how AGO4 is prevented from binding to heterochromatin but did not explain how AGO4 is guided to regions outside heterochromatin. It is a bit strange that AGO4 was not ChIPed to RdDM regions. If AGO4 binds to Pol V transcripts, one would also expect AGO4 to be ChIPed onto Pol V transcribed regions through its binding to Pol V transcripts. In my opinion, without more biochemical data, it is premature to conclude that AGO4- associated siRNAs base pair with RNA exiting Pol V.

5) The authors found enrichment of Pol V transcription on the edges of longer transposons and concluded that Pol V is the main determinant for RdDM targeting the edges of transposons. As matter of fact, as the authors noted, Pol IV-dependent siRNAs were also enriched on the edges. Thus, Pol IV could also be a determinant.

6) In the third section of Results, the authors indicated that Pol V transcribed both strands and the transcription levels on both strands were correlated. However, in the last section of Results, strand preferences were detected for 5'-ends and 3'-ends of transposons. This needs to be clarified.

7) Most of the conclusions were drawn from genome-wide data analyses. The authors should use alternative approaches to validate at least some of the key points. For instance, the lengths of transcripts generated by internal Pol V transcription at some representative loci should be examined by RT-PCR analysis. Strand preference of Pol V transcription at selected loci should be confirmed by qRT-PCR. AGO4 binding to Pol V transcripts or DNA should be validated by RIP-RTPCR or ChIP-qPCR.

Reviewer #2:

In the manuscript entitled "Long Non-coding RNA Produced by RNA Polymerase V Determines the Boundaries of Heterochromatin" submitted to eLife, Böhmdorfer et al. perform RIP-seq of Pol V interacting RNAs in wild-type and pol v mutants. This dataset thus defines the transcripts that Pol V produces. The authors perform several analyses connecting their dataset to ChIP, RNA-seq and sRNA-seq datasets either already published or that they have produced themselves. This analysis shows that their dataset of Pol V transcripts is higher-resolution compared to Pol V ChIP previously published. The authors also use their dataset and informatic prowess to address several key questions in the RdDM field. Overall, this manuscript is very carefully written. I have split my comments into major concerns and analyses to be performed.

Major concerns:

1) The production and analysis of the Pol V-RIP dataset represents a technical accomplishment. However, my major concern for this manuscript is what has been biologically learned that we did not already know? This higher resolution data has improved our detection, but what was learned about RdDM? I think it will be important for the authors to highlight the strong conclusions from their dataset in the Abstract, and remove the Abstract parts that focus on the production of the dataset.

2) I found certain sections of the Methods lacking in critical detail. Were mock-IPs of any sort performed? Was mRNA or rRNA depleted in any way before library production? Most importantly, how were multi-mapping reads handled? Much of Pol V RNA comes from repetitive DNA, and how this is informatically handled will have large consequences on the observed data. This is particularly important for the data in Figure 7.

3) One of the strongest conclusions that could be made is that there is absolutely no evidence from this dataset that Pol II can substitute for Pol V in a pol v mutant. I think the authors should make this strong agreement to improve the conclusions they are drawing in this manuscript compared to their Pol V ChIP publication.

Analyses to be performed:

1) Subsection “The Pol V Promoter”: “Pol V transcripts were enriched on transposable elements in gene-rich environments”. I do not see evidence of this in Figure 2C. First, the r2 value is very low. Second, the analysis performed does not look at gene-rich or poor environments, but rather at mRNA production (mRNA/TE), which is not the same thing. This analysis should be repeated in a more direct manner.

2) The evidence in Figure 2D makes me think that all regions regulated by MET1 are transcribed by Pol V. Does this include CG-context methylated genes? I think the investigation of these genes is critical to understanding Pol V. If they are transcribed by Pol V, then methylation alone, and not histone modification / heterochromatin is responsible for directing Pol V. If CG methylated genes are not transcribed, then methylation alone is not sufficient to direct Pol V. Either way, these genes should be explicitly examined as they are methylated regions that should not be targeted for RdDM nor formed into heterochromatin.

3) Subsection “AGO4 Binds Most Pol V Transcripts”: “…suggesting that AGO4 associates with most if not all Pol V transcripts.” I am not convinced of this claim by the data presented. Could the authors use a Venn diagram to determine the overlap and support this claim?

4) I do not like the display of Figure 4. If the authors wish to compare the RIP data in the ago4 mutant, I suggest creating a scatter plot of each of the Pol V transcripts they annotated as dots, and then plot their RPM RIP values for wt on the X-axis and ago4 on the Y axis. This will display the dataset in a more useful way than the boxplots or metaplot. See the following reference for an example: Panoramix enforces piRNA-dependent cotranscriptional silencing.

5) In the subsection “siRNAs Base Pair with RNA Exiting Pol V” the authors investigate strand bias. This is a worthwhile analysis, but it only informs the siRNA base pairing with RNA due to the models proposed, and does not directly test the "RNA exiting Pol V" per se. I would write this section strongly from the strand-bias point of view, but then only suggest that this supports an RNA-RNA interaction at a distance from the polymerase.

6) In the section on edges of heterochromatin, it seems to me that the combined activity of both Pol IV and Pol V function to create this edge enrichment. I would be interested to see if the analysis performed in Figure 7C-D repeated with data from Pol IV would show the same thing of transcription in from transposable element ends. I think this is particularly important, as this is a major conclusion that could be newly drawn from this dataset, and the title reflects this discovery as well.

Reviewer #3:

In this manuscript, Böhmdorfer and colleagues address the important question of Pol V activity by describing transcripts produced by RNA Pol V in Arabidopsis. They identify these transcripts through Pol V RIP-seq and further assess them in various ways, including assessment via qRT-PCR in nrpe1 mutants or RIP-seq in ago4 and idn2 mutants, comparison of sense/antisense transcripts, and correlations with Pol V ChIP, DNA methylation, siRNA accumulation, and genomic features (TEs, histone modifications). The authors make a number of conclusions regarding Pol V activity and the larger mechanisms of RdDM. While some of their conclusions are based on indirect evidence, they are always careful to state alternative hypotheses. The data in this manuscript are of the highest quality and will undoubtedly be highly influential. The authors should be commended on a really beautiful piece of science – meticulous experimentation, thoughtful analysis, careful interpretation, clear writing, and beautiful figures.
