# Peer review - Round 1

Editors:
- Job Dekker, University of Massachusetts Medical School United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.47980.sa1](https://doi.org/10.7554/eLife.47980.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study describes development of a inducible insulator cassette, STITCH, that can act as boundary element that blocks long-range chromatin interactions. This can be a very valuable tool to dissect rules of long-range promoter – enhancer communication, and chromosome folding through mechanisms such as loop extrusion.

Decision letter after peer review:

Thank you for submitting your article "Controlling gene activation by enhancers through a drug-inducible topological insulator" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Job Dekker as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Jessica Tyler as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this paper, the authors present a new tool to modify chromosome structure and enhancer-promoter interactions. The major advance over previously identified insulators is that this tool (STITCH) is designed to include not only divergent tandem arrays of CTCF sites to create a boundary, but also interspersed tetO arrays to allow inducible regulation of CTCF binding. The tetO arrays are added between the CTCF sites such that with the addition of a tetR-KRAB transgene to the cell line, CTCF binding can be disrupted by inducing heterochromatin formation at STITCH in a doxycycline repressible manner. Disruption of CTCF binding to STITCH leads to increased interactions and enhancer-promoter contacts across the STITCH insertion site, and can modify gene expression. Therefore, STITCH is an inducible insulating element, which would be a broadly useful tool in the field of chromosome structure and beyond, such as in genome editing applications.

Essential revisions:

1) Given that STITCH is presented as a tool, all reviewers felt that the approach should be used for 2-3 case studies, ideally in at least 2 different cell types. This will help show how generally applicable the tool is and how robust the results are.

2) All reviewers felt that the PCA analysis was confusing and did not make a critical contribution. Please thoroughly revise the corresponding text and figures, or remove this analysis from the manuscript.

3) It is critical to show whether TetR binding alone, without the KRAB domain, affects CTCF binding and/or CTCF-mediated insulation.

4) The H3K27 ChIP experiments need to be repeated to provide better statistics to support the conclusion that changes in the levels of this mark can be accurately quantified. There are concerns this data set is not of high quality. Also, in Figure 4C-D positive and negative controls should be added.

5) The transcriptional analysis In Figure 2 could be improved. The cutoffs used to identify differentially expressed genes with DESeq2 are very loose (adjusted p-value = 0.1, no limitation is imposed on fold changes). We suggest to repeat the analysis with more than one clone per condition.

6) Please extend the discussion about the relationship between structural changes induced by STITCH and potential new loops induced by the ectopic CTCF sites in the light of the current understanding of CTCF orientation (and loop extrusion?). Reciprocal 4C viewpoints based on endogenous CTCF sites could also help clarifying this matter.

7) Upon publication we feel it is critical that the tools are made available to the community (e.g. putting plasmids on AddGene).

Reviewer #1:

The authors overstate the novelty of their results with respect to insulating elements. Insulating elements have been previously identified, and usually contain CTCF sites, similar to the STITCH sequence (Bell et al., (1999); Liao et al., (2018); Emery, (2011)). This should be more adequately referenced and introduced. In addition, it has already been shown that CTCF sites that form TAD boundaries will block enhancer-promoter interactions, yet this is presented as a novel result (subsection “Titrating blocking activity of STITCH by serial mutations of the CTCF binding sites”) (Hou et al., (2008); Guo et al., (2015); Braikia et al., (2017)).

The conclusion that the enhancer blocking activity and chromosome interaction activity are due to separate mechanisms is not sufficiently explained or supported. It is unclear why loop extrusion and enhancer blocking are introduced as separate mechanisms (Introduction), when the current understanding in the field is that enhancer blocking by CTCF sites is likely due to the creation of new TAD boundaries, which are formed by loop extrusion being blocked by CTCF sites (Recently reviewed in Schoenfelder and Fraser, (2019)).

Similarly, there appears to be confusion about the various mechanisms of long-range chromatin interactions in the Discussion section. Subsection “Mechanism of the STITCH insulation and its control by heterochromatin induction”, second papragraph is very confusing. In the current work CTCF is removed, from the locus, but cohesin is not. Therefore, there is now unblocked loop extrusion throughout the locus. Given that the interaction between the enhancer and MYC is blocked by CTCF, it is much more likely that the increased interaction between the super-enhancer and MYC when CTCF is removed is driven by loop extrusion.

Technical details and biological conclusions are not adequately explained in the text throughout this manuscript. The manuscript would benefit from improving the explanations of why specific analyses are used, and what the results signify biologically, beyond just stating the observations. In particular, the explanations of PCA analysis, component loading plots, and power law scaling between gene expression and 4C-seq contact frequency should be clarified. As it is presented now it is entirely unclear what the PCA analysis really adds. Additional technical details of the computational methods used to analyze the sequencing data is also needed, preferably an online repository for the code used to generate the plots and run the statistical tests should be included with the manuscript.

While 4C-seq is a useful technique for studying the specific interactions between MYC and surrounding loci, it would be beneficial to also compare this to an all-by-all or many-by-many chromosome conformation capture method such as Hi-C or 5C to show the endogenous organization of this region. Putting the STITCH insertion in the context of the landscape of genomic architecture (where are TADs or compartments found in this region?) would strengthen the manuscript and might help to understand how the different directionalities of the CTCF motifs in STITCH are working, as the current explanation is unclear. In addition, it would strengthen the manuscript to compare the contact frequency changes in the STITCH mutants at the MYC locus to changes in the endogenous TZ locus with similar modifications from previous publications by these authors, to determine how variable this behavior is at different genomic loci.

Reviewer #2:

The role of CTCF, cohesin, TADs and 3D genome organization in regulating gene expression and enhancer-promoter (E-P) contacts is currently being intensely studied. In particular, whether CTCF sites and TADs really regulate E-P contacts and gene expression has recently become controversial, with some studies claiming that CTCF and TADs have no role in regulating gene expression (e.g. see https://www.biorxiv.org/content/10.1101/609941v1).

Most studies (including the preprint above) have taken a "deletion" approach to this issue: take a natural E-P pair and TAD and then go in and start deleting or inverting etc. CTCF binding sites and see how gene expression is affected. What is nice about this study is that they take the opposite approach – a kind of "addition" approach. They add the STICH array of CTCF binding sites to the MYC gene at different locations and see how contact frequency (4C) and gene expression (qPCR) of MYC in hiPSCs is affected. The 2 most important points in my opinion are:

1) CTCF sites really can block E-P contact and strongly (~20-fold) affect gene expression. At least for the MYC gene.

2) Histone modifications can be used to turn ON and OFF CTCF insulation with quite high temporal resolution.

I believe the authors get about as close to causality as is realistic with the current tools of molecular biology, which is nice.

Beyond some important but addressable concerns (poor writing, at times confusing figures and presentation, occasionally poor referencing, tool availability), my major concern is this: The authors report STICH as a tool. 2 key features in a tool that are desirable to have are: (1) robustness and (2) generality. But because the authors only apply STICH to one locus (MYC) in one cell type, we cannot really tell if STICH is likely to block E-P contacts in general and robustly in many other loci and other cell types. The impact of STICH would have been greatly increased if the authors could have applied it to 2-3 case studies, ideally in at least 2 different cell types.

So overall, I believe this is a nice contribution with some really important insights, but that the general interest and impact could have been substantially improved if the authors had applied STICH to at least 2-3 different systems and if they can improve their presentation.

Specific issues:

Writing: the paper is for the most part reasonably written, but there are at least >25 cases of poor English and/or syntax/grammar issues. This is too many for a reviewer to fix and I suggest that the authors go through and clean up the issues.

Discuss results in context: First sentence of the Abstract and in the Introduction suggest that "regulation of gene-enhancer interaction is better understood,". I would argue that this is not true. In fact, recently several people (e.g. https://www.biorxiv.org/content/10.1101/609941v1) have begun arguing that CTCF plays essentially no role in the regulation of gene expression. The fact that the authors see such clear results on MYC, in my opinion only increases the impact and value of this study. Therefore, it would be nice if the authors could discuss their MYC result a little bit more clearly in the Discussion section in the context of the many recent studies arguing that CTCF plays no or only a minor role in regulating E-P contacts and gene expression.

Key resources should be available: First of all, my apologies if the authors already did this. But I tried to find this information and was unable to. The authors must put the key STICH plasmids on AddGene for the community, since the value of a tool is largely derived from it being readily accessible for the community. The DNA sequences of STICH must also be available with the paper. I could not find the DNA sequences of the full STICH sequence nor could I find the sequences of the specific CTCF binding sites. These must be available.

RNA-seq Results: The RNA-Seq studies in Figure 2 were really nice. But I could not understand why the STICH +30kb cell line would have ~2-3x more deregulated genes than the del(30-440) cell line. Although STICH is powerful, deleting the enhancer should still have a stronger effect on expression than just blocking it. Could the authors better explain this?

PCA-analysis: In Figure 3A-B, the analysis of how 4C reads in the different regions depend on the STICH construct was really nice. It was also very interesting to see the highly non-linear scaling between 4C contact frequency and gene expression (Figure 3I-J). Both of these are really important contributions in my opinion.

But the PCA-analysis was extremely confusing and convoluted. I really tried to follow the text and the figures, but it was very difficult for me to understand what the point was. In the Results section, the authors spend a lot of text and a huge number of figure panels on this, but I really could not understand it. My suggestion would be to remove all the figures and text pertaining to PCA or at least radically simplify the figures and the text to make it easier to understand. What is the major biological insight coming from this PCA analysis? What is component loading?

Subsection “Insulation and deletion of the enhancer resulted in similar transcriptome profiles”: authors out-of-the-blue reference VP-MYC1 and VP-MYC2, without any figure REF. I could not understand this.

tetR-KRAB studies: The Tet-R KRAB studies were very nice. I may have missed prior studies, but to my knowledge this is the first clear and causal demonstration that histone modifications can turn OFF CTCF insulation. However, one control I was missing was a DNA-binding control. TetR-KRAB binding could disrupt CTCF binding and insulation through 2 ways: DNA-binding competition (e.g. TetR-binding outcompetes CTCF binding) or KRAB-deposition of histone modifications. I would have liked to see a control showing that TetR binding alone – without the KRAB-domain – does not affect CTCF-mediated insulation.

But pretty neat to see that STICH insulation directly affects cell proliferation (subsection “Titrating blocking activity of STITCH by serial mutations of the CTCF binding sites”).

Figure 6. F and G have errors bars, but Figure 6 C, D, and E do not. Need to add errors bars to these.

Otherwise, the time-course results were also pretty cool.

Reviewer #3:

The manuscript describes a strategy to modulate chromosomal contacts in the vicinity of the endogenous MYC gene in human iPS cells through the ectopic insertion of an array of CTCF sites. The approach (named STITCH) seems to be able to alter MYC transcription levels, which correlates with changes in interaction frequencies between the MYC locus and a super-enhancer region downstream. The authors further monitor chromatin states at the engineered locus upon the induction of H3K9 trimethylation by targeted recruitment of a KRAB domain at the STITCH cassette, which is shown to disrupt CTCF binding and restore wild-type chromosomal contacts. The authors conclude that CTCF-mediated modulation of chromosome interactions is the driver of transcriptional changes.

The study is interesting and well designed, and has the potential to bring insight into how gene expression could be modulated by manipulating chromosome structure. However, it suffers from several major drawbacks that should be thoroughly addressed.

1) Many of the native ChIP-seq experiments in the manuscript are difficult to interpret and it is often difficult to agree with the authors on the changes they describe. The zoom level in all Figures is way too low to visually appreciate any local changes at the MYC locus, the STITCH cassette and the neighboring region. More importantly, some crucial experiments (notably the H3K27ac and H3K27me3 ChIP-seq reported in Figure 1, Figure 4 and Figure 4—figure supplement 1) appear to be strongly suboptimal. It is hard to imagine that a local increase of ~2 counts in a 0-6 range as reported in Figure 1 and Figure 4 really does correspond to a specific enrichment as opposed to technical noise.

The authors should perform new H3K27ac/me3 ChIP-seq experiments, provide statistics to support the notion that changes in these chromatin marks can really be quantified and discuss their findings in the light of the new experiments. Crosslinking ChIP-seq would be a viable option in this context – in fact I found it quite unclear why native ChIP was required in this particular study.

2) The correlation between MYC transcription levels and contact frequencies with the super-enhancer region (Figure 3) in mutant STITCH cell lines are interesting, and well supported by the large number of independent clones analyzed. Unfortunately, the structural changes induced by ectopic CTCF sites were not correlated with the position and orientation of endogenous CTCF sites. MYC itself is highly bound by CTCF, as can be more or less seen (again at regrettably low resolution) in Figure 5F. I would suggest the authors to thoroughly discuss the relationship between structural changes induced by STITCH and potential new loops induced by the ectopic CTCF sites in the light of the current understanding of CTCF orientation (and loop extrusion?). Reciprocal 4C viewpoints based on endogenous CTCF sites could also help clarifying this matter.

3) It is unclear how many copies of the STITCH cassette have been integrated at the MYC locus. The authors should provide evidence that a single insertion of 6 CTCF sites is actually responsible for the observed structural changes, as opposed to multiple tandem repeat insertions (especially since lipofection -and hence large amounts of DNA per cell- was used to generate the Cas9 assisted knock-in).

4) The transcriptional analysis In Figure 2 could be improved. The cutoffs used to identify differentially expressed genes with DESeq2 are very loose (adjusted p-value = 0.1, no limitation is imposed on fold changes). In the absence of differential gene expression analysis on more than one STITCH and del(30-440) clones, it is difficult to assess what the >1000 genes detected as differentially expressed under these loose criteria actually represent. I would suggest to repeat the analysis including more than one clone per condition and using more stringent criteria (e.g. padj<0.01, |log2(FC)|>1) in order to identify mis-regulated genes more robustly and reliably. Also, a qPCR validation of significantly up- or down-regulated genes is missing.

Finally, there is no explanation for the fact that the effect on transcription in the deletion mutant is smaller than in the STICH mutant. If the changes are indeed due to the insulation of the super-enhancer region from the MYC gene, then deletion of the super-enhancer region should lead to an even stronger effect on transcription.

5) It would be nice to prove that transcriptional changes in the STITCH and del(30-440) lines are really caused by downregulation of MYC, which could be done notably by overexpressing MYC and testing if normal expression programs are rescued.

6) The PCA analysis is Figure 3 is in principle interesting and laudable as an attempt to quantify differences in 4C profiles in a quantitative and unbiased way. However, the text is somewhat obscure and panels 3C-H are difficult to interpret. It is unclear why the results shown in Figure 3E-H, where PCA is performed on a subset of the data, are so different from panel 3D. These differences are acknowledged in the main text but I did not understand how they are interpreted by the authors. I would actually suggest that the text relative to Figure 3 is entirely re-written and clarified (e.g. please explain what "component loading" means in this context). In addition, the PCA results should be integrated with a discussion of whether they correlate or not with the position and orientation of endogenous CTCF sites (see point 2 above).

7) Transcriptional downregulation of MYC is attributed to changes in contact frequencies due to the presence of ectopic CTCF sequences at the STITCH cassette, which is supported by the strong correlation observed in Figure 3I. If this is really the case, and is due to CTCF looping from STITCH onto endogenous CTCF sites, then it should be possible to recapitulate the phenotype by deleting the endogenous partner CTCF sites. This would significantly strengthen the interpretation of the data.

8) in Figure 4C-D, negative and positive controls are missing (i.e. one or more regions where H3K4me3 should not be detected, and a region that is heavily bound by H3K27me, such as a poised gene, or a Hox gene). This is a very important control though, because one of the most interesting observations in the manuscript is that the transcriptional downregulation of MYC correlates with higher H3K27me3 levels. However, how much H3K27me3 is deposited? How does it compare with poised and/or inactive loci?

9) In Figure 5, it is impossible to understand which changes are occurring at the MYC promoter in terms of H3K9me3 and CTCF levels. This is nonetheless crucial to interpret the gene expression changes upon Dox induction and how they are related to targeted recruitment of KRAB. It seems that the CTCF signal is decreased also in the MYC promoter in the absence of Dox, and not only at the STITCH region. A zoom-in and quantification of ChIP-seq experiments (peak calling, integrated intensities of signals) should be provided, and the results should be discussed accordingly.

10) Along the same line, in Figure 6 a crucial missing information is how CTCF binding evolves in time at the STITCH cassette and at the MYC locus.

11) It is unclear what 'control' in Figure 7 refers to.

12) One very interesting observation is that MYC gains H3K27me3 upon STITCH insertion, which correlates with the observed level of insulation in the various mutants and with transcriptional activation/deactivation in time course experiments. However why is it so? If this happens as a consequence of physical insulation from the super enhancer, how do the authors interpret it? An alternative explanation is that PRC2 is recruited by sequences in the STITCH cassette, and helps repressing transcription. The delay observed between MYC deactivation/reactivation and the corresponding differences of H3K27me3 are not large enough to exclude this second hypothesis. Based on the experiment shown in Figure 7J it cannot be excluded that H3K27me3 levels are unchanged upon treatment with EPZ, in the absence of a carefully quantified ChIP experiment.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Controlling gene activation by enhancers through a drug-inducible topological insulator" for consideration by eLife. Your article has been reviewed by Jessica Tyler as the Senior Editor, a Reviewing Editor, and two reviewers. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This study describes development of a inducible insulator cassette, STITCH, that can act as boundary. This can be a very valuable tool to dissect rules of promoter – enhancer communication, and chromosome folding through mechanisms such as loop extrusion.

We request that the authors address the following issues.

Essential revisions:

1) The authors were requested to put the structural changes induced by STITCH in the context of the overall CTCF binding patterns in the MYC region. They addressed this point on the one hand by performing new 4C experiments using the STITCH sequence as a viewpoint. These experiments, now in Figure 1, unfortunately do not seem to reveal how the various endogenous CTCF sites could be used to make new connections with the ectopic STITCH cassette and even a re-analysis of the 4C data with the MYC promoter as a viewpoint are inconclusive. The authors conclude vaguely that "It might be extrapolated from these previous results that there are not very specific endogenous regions that singly form loops with STITCH to organize the conformational changes induced by STITCH". The interpretation of the data in the rebuttal is also highly speculative and does really not address the reviewers' request that structural changes are evaluated in the light of a more global view of chromosome contacts such as the one provided by Hi-C data. In 4C it is always hard to detect loop extrusion-associated structural features such as loops and stripes (or flares), and it is not surprising that specific connections between CTCF sites might be missed without performing matched Hi-C or 5C experiments. The authors need to at least these limitations of their 4C-based analyses.

2) In the new Figure 8, new experiments are provided to support the applicability of STITCH to additional contexts. However, the data do not appear to fully support the conclusion that STITCH-mediated modifications of chromosome interactions are at the basis of the observed transcriptional effects. First, 4C experiments in panel F do not allow to conclude in any manner that STITCH alters conformation at the targeted allele. Certainly, the presence of the wild-type allele confounds the readout, but even considering this, the fluctuating small-% differences observed do not seem to be robust (also, information on replicates is not provided unless I am mistaken). The right experiment to address this point would have been to perform 4C from the STITCH cassette itself, which would allow to detect mainly contacts within the mutant allele and which is apparently technically possible given that similar experiments are reported in the new version of Figure 1. It would be important to add such 4C analysis.

Second, it appears that NEUROG2 downregulation is only shown for one population of cells following piggyBac-mediated insertion of the TetR-KRAB transgene. It is unclear whether these results would hold true if the transposition of the transgene is repeated in independent experiments. Given that piggyBac insertions typically occur in multiple genomic locations simultaneously in every cell, a possibility that cannot be excluded is that the transcriptional effect on NEUROG2 is a secondary effect of mis-regulation of one or more upstream genes that are accidentally targeted by the transposon. This should be discussed.

3) Introduction and Discussion section: the authors seem to confuse several concepts of loop extrusion, insulation and contact domains. Insulation by CTCF is the result of its ability to block loop extrusion. Insulation does not necessarily involve CTCF sites to loop with each other (in fact such loops barely insulate). Insulation and contact domains can occur even when interactions are not strictly divergent at boundaries: insulation can occur in only one direction when CTCF sites are all in the same direction. Such unidirectional insulation can demarcate contact domains. The authors are asked to consider these issues when revising the Introduction and Discussion section.

4) All reviewers found the manuscript extremely difficult to read. Please do not use track changes. The manuscript should be carefully edited.

5) All plasmids should be made available through AddGene.
