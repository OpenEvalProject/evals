# Peer review - Round 1

Editors:
- Oliver Hobert, Howard Hughes Medical Institute, Columbia University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59610.sa1](https://doi.org/10.7554/eLife.59610.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Odd-paired is a late-acting pioneer factor coordinating with Zelda to broadly regulate gene expression in early embryos" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Erik Clark (Reviewer #3).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work can not be considered for publication in eLife in its present form. While all reviewers agreed that this work was of general interest, they all raised a number of concerns that require substantial additional experimentation that we think is outside the presently required 2 month time window. Given the general interest of the study, we do encourage you to consider these requested experiments. Should you be able to address these concerns we would be interested in seeing a substantially revised version of the paper submitted as a new submission.

Reviewer #1:

Kormila et al. build on prior publications demonstrating that Runt activity at the sog distal enhancer transitions from a repressor to an activator by identifying Odd-paired (Opa)-binding to this regulatory element. They use live-embryo imaging to show that Opa-binding sites are required for late activation from this regulatory element and, using ChIP-seq and ATAC-seq analysis, they argue that Opa is a pioneer factor essential for a late wave of zygotic genome activation. While interesting, the genomic data as presented are somewhat superficially analyzed and do not support a clear role for Opa in driving chromatin accessibility, a defining feature of pioneer transcription factors.

1) The ChIP data would benefit from additional analysis. To determine biologically meaningful differences between the various ChIP peaks, the authors should analyze the relative peak heights for the 16,085 peaks. For example, are there any differences in relative peak heights for the peaks bound by Opa alone, Opa and Zld, or Zld alone? In Figure 3—figure supplement 1, it appears that the peaks uniquely bound by Opa at a single developmental time point (3h vs. 4h) are lower than the peaks shared between time points (assuming color indicates relative peak heights). If this is the case, these differences in binding may actually reflect variability in ChIP efficiencies for these lower peaks rather than meaningful biological changes. Relative peak heights can then be used in the analysis of the ATAC-seq to determine if those regions with the highest ChIP signal are correlated with accessibility.

2) For the ATAC-seq data statistical methods (i.e. DESeq2 or edgeR) should be used to identify significant changes in accessibility between wild-type and shRNA (opa or zld) embryos. How many regions lose accessibility overall? Once significant changes are identified, the overlap between these regions and binding of Zld and Opa can be directly tested. Are the regions that change in accessibility upon knockdown those with the highest ChIP-seq signal for the identified factor?

3) Better confirmation needs to be demonstrated for the shRNA knockdown. Given that the authors use anti-Opa and anti-Zld antibodies in Figure 1C to demonstrate protein expression this should be used on shRNA embryos to demonstrate protein knockdown and not just a decrease in the amount of RNA. Alternatively, western blots on bulk embryos should be used to demonstrate a decrease in levels of the protein products of the genes being targeted. In addition, because the Zld antibodies used in this manuscript have not been previously published information regarding antibody production and a demonstration of specificity needs to be included in the Materials and methods. Also, the staging of the single embryos used for the ATAC-seq should be noted.

4) The data presented alone do not allow the conclusion that Opa is a pioneer factor and thus the title for Figure 5 and some of the conclusions must be softened or additional data provided. There is no data presented that demonstrates that Opa establishes accessibility by accessing previously nucleosome-bound regions. In addition, there is a limited demonstration that the accessibility that is lost in an opa mutant has direct effects on either the ability of additional transcription factors to bind or gene expression. The prior analysis of Runt binding to the sog distal enhancer provides a mechanism for them to directly test the requirement for Opa-mediated accessibility in facilitating Runt binding. ChIP-qPCR for Runt on the sog distal enhancer reporter with the mutated Opa binding sites (Figure 1) and/or in the shRNAi knockdown would begin to address whether Opa has these additional defining features of a pioneer factor. In addition, the global effect of Opa-mediated accessibility on gene expression could be analyzed by RNA-sequencing.

5) There are a number of citations that should be added to the manuscript.

Kwasnieski et al., 2019 should be included with Ali-Murthy and Lott.

Xu et al., 2014 and Yanez-Cuna et al., 2014 should be included with Harrison, Liang and Nien.

Sun et al. Genome Research 2015 should be included with Schulz.

Some mention of Li et al., 2008 and the included demonstration that A/P factors bind D/V enhancers should be included.

Papers from which ChIP-seq data sets were analyzed should be cited.

Harrison et al., 2010 should be substituted for Schulz et al., 2015.

Reviewer #2:

Based on the finding that the transcription factor opa, primarily known for its function during A/P segmentation, regulates the expression of a D/V enhancer (sog) at late stages, the authors question the role of opa at a whole genome scale. By performing opa ChIP-seq experiments as well as ATAC-seq in wt and embryos depleted for opa, the authors identify a new set of cis-regulatory regions bound by opa and whose accessibility is opa-dependent. By comparing these accessibility profiles to Zelda-dependent ones, the authors propose that opa acts a pioneer factor to control the timing of gene expression.

While the finding that opa controls accessibility and could act as a general timing factor during MBT that acts subsequently to Zld-mediated activation is novel and exciting, I have some reservations concerning the evidence supporting this finding. While the overall manuscript is promising, there are some issues with precision and rigor the authors should address. If these revisions are made, I would recommend this work for publication in eLife.

General comments:

The title is “Odd-paired is a late acting pioneer factor…”. The defining properties of a pioneer factor are: a) protein binding to nucleosomal DNA; b) retention of the protein during mitosis; c) a general requirement for establishing/maintaining accessibility of the genome; d) cis-regulatory element binding prior to target gene activation; and e) a general function in reprogramming. While not all of these properties strictly need to be met to declare a TF a pioneer factor, the current manuscript only demonstrates that opa is necessary for accessibility. The title requires nuance, and the authors should discuss similarities and differences between opa and other pioneer factors within the body of the manuscript.

The claim that opa acts as a timing factor is not fully supported by the data. Zelda-mediated activation timing has been demonstrated by accelerating activation with extra Zld sites or delaying it via deletion of Zld sites (Foo et al., Crocker et al., Dufourt et al., Yamada et al., etc.). To support opa regulation of timing, similar experiments would strengthen this claim immensely. Alternatively, the authors could drive maternal expression of opa and examine the change in temporal behavior on their existing Sog-MS2 transgene.

Specific comments:

1) Analysis of opa regulation of SogD-MS2 transgene

– In Figure 1A, a hole could be indicative of an unhealthy embryo. Moreover, Video 1 presented in the supplementary data does not correspond to these still images. The authors should provide images from a healthy embryo and show the corresponding video.

– In Figure 1, the number of videos should be indicated. Their quantification in terms of % of activation should be moved from the supplementary data to the main figure.

-In Figure 1—figure supplement 1, the authors should add the corresponding sog_unmutated control panels and the quantification of each genotype in terms of % activation.

– The images in Figure 1B suggest that reporter expression abnormally persists in the mesoderm of sogD_ΔOpa at nc14a. If true, the authors should comment on this result. Did the authors check that the opa mutations do not affect twi or sna binding sites?

2) ChIP-seq comparison of Zelda vs. opa

– The reference for the Zelda ChIP-seq data should be indicated (subsection “Assay of overrepresented sites associated with Opa ChIP-seq peaks”). In particular, are opa ChIP 3h samples compared to an equivalent Zelda 3h dataset (and opa 4h to Zelda 4h)?

3) Investigating the role of opa vs. Zelda for chromatin accessibility

– The authors did not justify the need for single embryo ATAC-seq. Single embryo studies are most useful if the exact developmental timing is known. If the authors did precisely time their experiment, this value should be reported with the data.

– The authors should explicitly state that they used the same Gal4 driver for RNAi Zelda and RNAi opa. (subsection “Global changes in chromatin accessibility result upon knock-down of Opa”)

– To underline that opa-bound enhancers are active later than Zelda-only enhancers, the authors should show RNA-seq tracks for the genes exemplified in Figure 3 A-H

– The authors mention that the opa1 mutant phenotype is comparable to that of opa RNAi embryos, but this is not shown or cited from another publication. Figure Sup4 should be complemented by similar FISH/immunolabeling in opa RNAi embryos.

– The RNAi stock used to deplete opa is not homozygous viable (given the stock described in the Materials and methods), possibly suggesting off-target effects of the RNAi. To circumvent this possibility, the authors should perform single embryo ATAC-seq on opa1 mutants. If the accessibility results are similarly affected to those in opa RNAi then it would strengthen their conclusions.

– The author seems to have performed new ATAC-seq experiments on RNAi Zld, but the driver employed needs to be specified. Could the authors compare their results with published single embryo ATAC-seq in Zelda mutants (Hannon, 2017)?

– To be rigorous, the authors should have used a RNAi-white crossed with the same MTD-gal4 line as a control and not WT embryos. However, I think this experiment is less important than performing ATAC-seq in opa1 mutants.

4) opa and chromatin accessibility

– Figure 4D suggests that accessibility seems much higher for Zelda/Opa common targets than for each TF target independently. Accessibility seems also higher for opa peaks compared to Zelda peaks. Is this data quantitative or semi-quantitative at all, and is there a way to explain that within the text? Can these curves be statistically compared? Can the authors produce similar graph at earlier and later stages?

– The accessibility results of Figure 4 should be complemented with Zelda and opa ChIP-seq tracks and organized to better emphasize the 3 groups of accessibility identified by the authors.

– It would be interesting to compare the opa peaks that are accessible independently of Zld to the genes that remain accessible in Zld mutants (Harrison, 2010, Schultz, 2015, Hannon, 2017).

I found figures 4 and 5 to be confusing. If the central idea of Figure 4 is to show that opa is responsible for chromatin accessibility, the authors should only present WT vs. opa RNAi. Then in Figure 5, they could add the Zelda RNAi comparison.

– Subsection “Opa-only occupied peaks require Opa to support their accessibility at mid-nc14”/Figure 4G: the tracks give no information on whether Zelda binds the eve LE enhancer. The authors could add the ChIP-seq tracks as performed in Figure 4—figure supplement 2A-B to clarify this. Additionally, the loss of accessibility in Zelda RNAi at this enhancer is shown but not commented on in the text.

– Also the panels of figures mentioned in the text are confusing and need revising. For example: Figure 3 is mentioned even though it does not show any accessibility data. Figure 4—figure supplement 1F does not exist.

– Subsection “Opa-only occupied peaks require Opa to support their accessibility at mid-nc14” paragraph three: The authors use the term opa1 mutant, when in fact they are looking at opa RNAi-mediated transcript depletion, which is significantly different.

Reviewer #3:

Opa is a zinc finger TF that is expressed broadly in Drosophila embryos during the latter part of cellularisation, gastrulation, and GBE. Koromila and colleagues use Opa ChIP-seq along with ATAC-seq from wt and opa RNAi embryos to show that Opa binds to thousands of regions across the Drosophila genome and is required for chromatin accessibility at many of them. The case study of the sog enhancer sog_Distal links these phenomena with effects on gene expression: mutating Opa binding sites present within this enhancer reduces the expression of a reporter gene at timepoints when Opa is expressed. The paper argues that Opa is an important pioneer factor that ushers in a second major wave of zygotic gene expression, separate and later than the one brought about by a different (and more extensively studied) zinc finger TF, Zelda. This is an important discovery, and along with a recent study from the Blythe lab that reaches similar conclusions, this paper will surely cause many researchers to investigate whether and how Opa is regulating their gene/developmental process of interest, in Drosophila and beyond.

I do have some concerns about the staging of the embryos. In particular, the central claim of the paper is that Opa coordinates with Zelda in regulating gene expression, because it binds to many of the same genomic regions, and for some of these regions, opa knockdown and zld knockdown both affect accessibility. Simultaneous Opa+Zld binding is inferred by comparing Opa ChIP-seq peaks to a published Zld ChIP-seq dataset. However, the Zld dataset uses embryonic stages (nc13 and early nc14) from before Opa is expressed, meaning that the possibilities of simultaneous binding vs. sequential binding cannot be distinguished. If possible, I would have the authors re-run their analysis using the "late nc14" dataset from the same paper instead, which seems a more appropriate comparison for their purposes. As an optional extension, explicit comparison between the early and late Zld datasets could also give interesting hints as to the nature of any Opa/Zld interaction – for example when Opa starts binding to the genome in late nc14, does this cause Zld binding at these loci to increase or reduce, relative to other Zld-bound loci where Opa is absent?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Odd-paired is a pioneer-like factor that coordinates with Zelda to control gene expression in embryos" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor (Oliver Hobert) and Kevin Struhl as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Erik Clark (Reviewer #1).

The reviewers greatly appreciate the revisions, compared to an earlier version of the manuscript that you had submitted and all agree that the study is now almost ready for acceptance. A few minor editorial issues remain and are listed below in the reviewers comments. Once those are fixed we expect the manuscript to be acceptable for publication.

Reviewer #1:

The manuscript has been significantly improved by its revisions. My key concerns have both been addressed by the authors – by 1) clarifying that the onset of Opa expression happens at nc14b and by 2) additionally comparing their Opa ChIP-seq dataset to a later Zld dataset, as requested. The authors have also carried out a considerable amount of new experiments and analysis (despite their current lab shutdown), and these new data strengthen their proposal that Opa is a key timing factor in the early Drosophila embryo. The authors' responses to my original comments are reasonable. I don't think any further experiments or analyses are necessary but the text could be further edited for clarity. I felt that the first half of the paper read well, but the second half of the paper lacked the same degree of polish and was sometimes hard to follow.

Reviewer #2:

This is a much improved manuscript that has worked to address many of the significant concerns from the prior submission. The additional data strengthen the conclusions of the manuscript. Furthermore, the focus on the Opa (3h) data successfully streamline the manuscript such that the focus remains on the conclusions most robustly supported by the data. We have only minor issues that should be addressed prior to publication.

1) The additional data with the ATAC-seq upon precocious expression of Opa and the analysis on nucleosome distance reported in Figure 5 are nearly identical to experiments published by Soluri et al., 2020. As such, this publication must be briefly discussed and cited. It is gratifying to show that these results are robust across laboratories and acknowledgement of this fact does not decrease the impact of this publication. We feel that this addition to the manuscript is necessary for acceptance.

2) Figure 3D is confusing as it appears that only a very small handful of genes are bound by Opa. This is obviously not the case as shown in Figure 3—figure supplement 1F, but the authors should consider a different way of highlighting specific genes. As it is, the black dots are labelled "Opa only" but these are clearly only a small fraction of the Opa only bound genes in this volcano plot. Similarly for the yellow Opa/Zld genes. It could be useful to report on the plot the % of down- and up-regulated genes that are proximal to an Opa binding site.

3) For the various heat maps, the order in which peaks are ranked should be clearly indicated. For example, in Figure 4F it is unclear whether each heat map is ranked separately or whether one can compare across heat maps. Similarly, the method for ranking peaks should be provided for Figure 5A and B.

4) There are a few typos/ formatting errors.

- Results paragraph three, the authors state that Opa expression is reduced at nc14c for a mutant reporter. It is not clear whether the authors mean Opa expression in this case.

- In many of the figures, the symbol for α in antibody staining is an "a".

- The authors state that there is a "significant increase in chromatin accessibility across Ope-bound regions (Figure 5A)." While these data are compelling, the word significant implies some sort of statistical analysis. If such an analysis was performed this should be reported. Otherwise, a change in word choice should suffice.

- The citation (Blythe, 2016) in paragraph three of the Discussion should presumably be Blythe and Wieschaus, 2016.

- In the legend for Figure 1I “Mus musculus" should have the genus name capitalized and should be italicized.

- The inclusion of Su(H) in Figure 6E is confusing and should be removed.

Reviewer #3:

The manuscript has been significantly improved.

The authors have answered the vast majority of my concerns and requests.

They have conducted extra experiments (such as paired-end ATAC-seq and single embryo RNA-seq in control and Opa RNAi backgrounds).

The notion of a “pioneer factor” was more thoroughly discussed. The new data/analysis concerning Opa-driven nucleosome signatures supports the notion that Opa exhibits the properties of a pioneer factor.

The text has been extensively revised, as well as the organization of the figures.

Given this pandemic period, revisions must not have been simple to perform, and I therefore highly congratulate the authors for their work. The revised manuscript is now suitable for publication.
