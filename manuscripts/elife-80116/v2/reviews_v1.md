# Peer review - Round 1

Editors:
- Patrícia Beldade, https://ror.org/01c27hj86 University of Lisbon Portugal

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80116.sa0](https://doi.org/10.7554/eLife.80116.sa0)

Through genetic mapping and analysis of WGS data, the authors identify a gene duplication co-segregating with a color polymorphism in males of the aposematic tiger moth. They name the new gene valkea and investigate its expression and function in relation to wing pigmentation. Using CRISPR to disrupt valkea, they observe changes in wing color. However, because valkea was not the only gene edited, its causal role in the color polymorphism cannot be unambiguously established.


---

# Peer review - Round 1

Editors:
- Patrícia Beldade, https://ror.org/01c27hj86 University of Lisbon Portugal

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80116.sa1](https://doi.org/10.7554/eLife.80116.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Colour polymorphism associated with a gene duplication in male wood tiger moths" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Christian Landry as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers provided very thorough individual reviews and have also validated each other's comments. The Reviewing Editor has subsequently drafted this to help you prepare a revised submission.

Essential revisions:

1) To frame it in terms of "supergene entailing reduced recombination", the work requires quantification of "lower recombination" within the duplicated segment, and more detailed characterization of the 5' end of that segment. Alternatively, claims of "supergene"-like behavior should be explicitly stated as a hypothesis. In terms of "supergene" pleiotropic effects, it seems that the association between duplication and polymorphism is shown directly only for pigmentation, and not any other phenotypes that covary with that. The association to other traits should also be presented as hypothetical.

2) Definite proof that valkea, and not something else in the duplicated region (e.g. regulatory sequence responsible for expression differences between morphs for other genes in that linkage group), is responsible for the white phenotype requires functional analysis. Possibly, the more accessible type of analysis would involve using CRISPR-Cas9 to knock-out valkea from a white morph background. That being impossible, showing spatial patterns of valkea (and other genes in that linkage group?) expression (e.g. using in situ hybridization) in developing wings of the white morph would at least already associate valkea to that specific region of the wing and add support to it being involved in the COLOR (not scale maturation, for example) polymorphism.

3) Provide more details on the methods, including making replication and data structure clearer in the gene expression analysis (and plotting actual data points in Figure 2B).

Reviewer #1 (Recommendations for the authors):

Line:125-126. "likely to be mapping errors". What do the authors mean by 'mapping errors'? greater specificity is needed. Importantly, I would like to see some attempt to document what you think is going on. If you filter your mapping using MAPQ > 30, when mapping across to the entire genome, does this region lose more reads in the yellow samples than what you show in Figure 2? Do all of the while individuals show this higher coverage, compared to yellow? Not clear in Figure 2 if the read depth here is the total for all of the individuals in your collection. Did you look at other regional samples that you sequenced?

The genomic region flanking valkea is not very well characterized in the manuscript. Figure 2 is only showing a cartoon, while there are perfectly good methods for aligning these two regions and showing computationally inferred orthology for this region. More specifically, while the downstream region of yellow-g, yellow-e both look orthologous, the upstream region appears to have different loci (ie. jg6744, jg1307). This suggests that this simplified cartoon is masking a lot more complexity, and I am asking for that to be presented clearly and empirically, as this is currently … glossed over/ignored in the relevant section of the results (lines:112-126).

Lines:150-151: I can understand your reasoning, but this is because I understand quite a bit about the temporal dynamics of color deposition in Lepidoptera wings. Most readers will not. Please provide more of your reasoning here, in terms of thinking that this color change is not due to patterning genes (though nearly all, or all?, aforementioned genes associated with Lep wing color changes, as not associated with color biosynthesis genes, but regulatory/patterning genes). So, your logical step here is quite a departure from the literature, please justify edifying the reader.

Gene expression patterns. I greatly appreciate that you provide an overview via a PCA-like plot to see the clustering of your samples. But.. Figure S3: is this an MDS plot (as per Edger), or something else? You do not describe how you generated this figure in the methods and that should be clarified. Also, in the relevant main text, lines: 160-161, you make a very qualitative statement, and I can't tell if that's just the authors "eye-balling" the PCA-like plot.

Since the RNAseq analysis was working with WW vs. yy individuals, how do the authors envision the expression threshold of valkea to give rise to a dominant phenotype? Stated another way, if white individuals still arise from Wy males, and in those the expression of valkea is going to be much lower … how do they envision the functioning of their new gene in a heterozygous background giving rise to a binary trait?

Figures. I was surprised to see that none of the figures had a general header before the subpanels were described (i.e. a one-sentence overview). I find this very strange and suggest the authors do this.

Figure 3 could benefit from more clarity. A is I guess a restructuring of all your RNAseq data to only look at differences between the two color morphs only, grouping all tissues together? This was not really clear in the main text and is not clarified here. I assume B is only looking at valkea expression across all time points … but this should be made clear.

Line 179: this analysis is fine, but I am rather unhappy with calling this pooling of all tissues and looking for only morph differences, as 'genome-wide analysis of RNAseq' … as all of your analyses are looking at RNAseq data mapped to the genome.. there is nothing unique here compared to what was done previously, expect that tissues are pooled by morph -- but this is not described clearly in the methods (lines: 447-457). Please, revise your methods for greater clarity of your two-step approach, and revise your main text, and figure legends accordingly. Perhaps more importantly, what do you gain by doing this two-step approach? I can see the logic, that even with this type of dev stage grouping, valkea clearly an outlier. This perspective should be shared with the reader. Having that come before the tissue-specific result works, but currently, you present the tissue-specific, then the pooled tissue, and then the figure panels are in the wrong order … it could be more linear and clear. Please revise.

Topology approach. This section appears rather rushed and should be introduced with greater clarity for the reader. Also, why are you only doing this for such a narrow region of the chromosome? Why are you not doing this for the whole region flanking the valkea insertion region? Where is the actual location of yellow-e in this figure? Again, it brings up the strange part this manuscript, in that the authors appear again to be avoiding their 5' flanking region of the duplication … why? That should be mirroring this pattern, which would strengthen the message here, but it is not presented. In sum, one can only really appreciate S5 if you can see the larger region, the flanking loci, the repeated patterns, and some proper phylogeny explaining the alternative topologies (as I find the text description alone lacking proper clarity for the topology alternatives). Does this arise due to the low coverage of your individual WGS data?

Recombination. I find it rather strange that you discuss the potential for recombination suppression as a result of the duplication, yet conduct no measures of LD. Why? You have many whole-genome datasets from a sufficient number of individuals for some preliminary analyses at least, to provide quantitative evidence. But, upon closer reading, is this because you have too little depth per individual for this? This brings up the issue that average read depth per individual is not clearly reported, and that needs to be changed in the main text.

Where is the table of the data generated per individual, for RAD and WGS? Their genomic coverage after mapping? In the area of the text where I expected this, I found instead % of reads mapping.. that doesn't convey depth, which conveys accuracy of WGS data … please make a table for these standard metrics common to QTL and GWAS papers.

Reviewer #2 (Recommendations for the authors):

This study truly is a fantastic effort to identify the locus responsible for adaptive color polymorphism in tiger moths. In general, the paper is well-written and the figures communicate the main results quite well. Following are suggestions, concerns, and/or questions I have about the study that I believe could improve the study and paper.

As mentioned in the public review, I have concerns with the hypotheses the authors use to frame the paper. I see this study as a quite well-executed effort to identify the genetic and phenotypic basis of wing color polymorphism in these tiger moths. I do clearly see how the study was designed to distinguish between the involvement of "large structural variants" versus "sing gene mutations". I think this could be addressed through some revisions in the Introduction. Along the same lines, I don't see any need to introduce the concept of supergenes, as I don't see any efforts to directly test if a co-adapted gene complex is involved. Again, this can be addressed through limited text editing.

This study would be greatly strengthened by additional gene expression and/or functional data. Spatial expression data of valkea and yellow-e in developing hindwings could provide critical evidence of these genes involved in the color pattern differences. Such data has been critical in the implication of other color pattern genes involved in Heliconius and Bicyclus wing development. Even further, functional confirmation, through methods such as CRISPR-cas9 editing has proven to be extremely successful to confirm the role of candidate genes in butterfly wing pattern development ( see examples from Heliconius, Bicyclus, Colias, and other butterflies), including successful CRISPR edits of yellow to study gene function in other butterfly species. Recent other studies of butterfly color pattern genetics published in eLife have included such spatial expression data and/or functional data. I remain unconvinced from the tree topology analyses that valkea alone at this locus is involved in generating the color differences, or that valkea acts as the genetic switch for the color polymorphism. To find the results of this study as convincing as those other recent studies, I would need to see comparable evidence.

For the pigment analyses, after the pheomelanin is extracted from yellow wings, do the wings appear white instead of yellow? I would be curious to see an image of what the extracted wings looked like, so I could directly connect the HPLC differences with a change in yellow versus white coloration.

I feel the paper could be strengthened through some integration of the genetic and phenotypic results. The authors have a rich RNA-seq dataset that can be used to characterize clusters and networks of genes expressed in development, and differences between the color morphs. There is also a well-resolved melanin pathway, with some knowledge of specific gene functions from Drosophila and other butterfly studies. In this regard, I feel the authors have missed an opportunity to integrate their gene expression data with their phenotypic data. For instance, what other genes do valkea and yellow-e cluster with (e.g. show correlated expression pattern with) in the RNA-seq data? These clusters would reflect the network of genes that are differently expressed between color morphs. I would in interested in knowing what these genes are and if there are any genes with interesting functions or known to be in developmental pathways that involve yellow genes, or are involved in pigmentation. In the melanic pathway, it could be powerful to visualize where in the pathway the authors propose that valkea may be impacting pheomelanin production. I would urge the authors to revisit Matsuda and Monteiro 2020 as an example of how such data can be integrated to give the reader a more clear and integrated understanding of how the genetic changes identified may be impacting the phenotype.

I quite like that the authors highlight gene duplication as a structural variant that is largely unable to properly recombine with haplotypes lacking the duplicated region. I would urge the authors to cite other examples where such duplications have been implicated in wing pattern development and adaptive evolution. For example, gene duplicates have been implicated in the adaptive evolution of pollen feeding in Helcinius butterflies (Smith et al. 2020) and sexually dimorphic color pattern development in Zerene butterflies (Rodriguez et al. 2021). This paper has an opportunity to highlight the increasing evidence of recent gene duplications in evolutionary diversification.

The duplicated region at the mapped locus needs to be further resolved. At a minimum, the authors should finely annotate the duplicated region. For instance, are there any TE insertions? Are the entire duplicate regions reflect a single recent duplication? Or, are there regions duplicated more than once, and this region appears to have experienced several instances of unequal crossovers and potential insertion/deletion events? Is the regulatory region (e.g. 5' UTR, etc.) duplicated? Does the regulatory region show elevated divergence relative to the other duplicated regions?

Similarly, further analysis of valkea would strengthen the paper. Does valkea show any evidence of adaptive molecular evolution? Are there non-synonymous substitutions with yellow-e? How old/recent is the gene duplication event?

Further analyses to address these questions could provide further resolution to the evolution and potential role of valkea in the color polymorphism.

Figure 2D. I have some reservations on interpreting the read-coverage as evidence the duplicated region is missing in all yellow samples. For instance, yellow-g shows a similar mapped reads pattern as the region just 3' of valkea in the duplicated region, yet yellow-g is not considered to be within the duplicated region. Are the regions in the duplicated region with high coverage for yellow samples potentially repetitive regions of the genome, such as TEs? If so, an annotation of this region would improve our ability to interpret the read coverage results.

Also, did the authors attempt to map RNA-seq reads from yellow individuals to a white reference genome to see if any reads mapped to valkea? This would be a quick and direct way to confirm that valkea is not present/expressed in any yellow genomes. In the methods section, it does not state which A. plantaginis genome the RNA-seq gata was mapped to. If RNA-seq data for yellow individuals was only mapped to a yellow reference genome that lacks valkea, then we can not be sure if valkea transcripts are actually absent from yellow RNA-seq samples (I honestly assume the authors are aware of the bias introduced by mapping yellow RNA-seq data to a yellow reference genome only, but I just need to check since I couldn't discern from the methods).

Reviewer #3 (Recommendations for the authors):

Specific comments to the authors:

Line 26: the limitation of recombination does not necessarily imply a supergene architecture. Furthermore, your results point a pleiotropic effect of a single gene rather than to a combined effect of several genes, therefore departing from the classical 'supergene' hypothesis. I would recommend rephrasing this part.

Line 40: it is unclear to me what you mean by 'selection is context-dependent, this needs to be explained in more detail.

Line 49: in mimetic butterflies, there is also a series of inversions at the supergene controlling colour pattern polymorphism in H. numata (Jay et al. 2021 Nature Genetics).

Line 59: it is unclear what you mean by 'in an ecological context', you may explain the key ecological features involved in the persistence of the polymorphism in this species.

Line 70: What is causing the mating advantage? Is it linked to female preference? If so, this raises the question of the selection promoting the evolution of such preference?

Figure 1: it this the frequency of MALE colour patterns shown on panel A?

Line 131: In my opinion figure S2 should be in the main document, it is very important to infer the ancestral state and the origin of the duplicated region. I would prefer moving panel D of figure 2 into the supplementary if space is missing.

In figure 2 panel D, I guess you compared YY HOMOZYGOUS males with WY HETEROZYGOUS males? This would be useful to provide this genotypic information in the legend.

Line 148: you may be precise that the RNAseq was performed on the wing disk. Did you investigate the expression patterns in hindwings and forewings separately? This might be interesting since the level of yellow colour seem to be higher in the hindwing than in the forewings (at least from what I can see in figure 1).

Line164: This suggests that there is not major shift in expression patterns between morphs even within the wing disk tissue. This is in apparent contradiction with the 99 DE genes found at the genomic level (lines 180-181). I think I misunderstood something here, these first expression analyses were restricted to genes located within the QTL region? This should be clarified.

Line 170-171: Did the overexpression of yellow-e occur at the same developmental stage as the overexpression of valkea (i.e. premelanin stage)? This is important to infer the putative developmental pathway inducing white colour pattern development.

Figure S5: The position of the yellow-e gene and of the valkea gene are not indicated in the figure, so it is difficult to draw conclusions from this figure at this point.

Line 196: This provides quite indirect evidence for ruling out the effect of yellow-e on the switch between white and yellow colour pattern development. The overexpression of yellow-e at the pre-melanin stage could be caused by variation in the (non-coding) regulatory region, and therefore explaining why variation in the yellow-e sequences is not specifically associated with colour pattern variation.

Line 291: In line with your conclusions, the dominance of the 'white' allele over the 'yellow' one is consistent with the white allele being a derived haplotype that invaded an ancestrally yellow population. Such invasion of a new adaptive allele is facilitated when the invading allele is dominant over the ancestral one because it is then expressed at a heterozygous state (i.e. Haldane's sieve effect).

Line 297: I have some trouble reconciling the 'neofunctionalization hypothesis' with the fact that valkea seems to be a truncated gene. Is there any example where a truncated yellow gene gained a new function in the melanin developmental pathway?

The overexpression of the valkea gene could stem from a lack of regulation of a gene with a loss of function. In that case, the switch in colour pattern might stem from variation in the non-coding region affecting the expression of other genes, like yellow-e. Is there a way you can rule out this alternative hypothesis?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Colour polymorphism associated with a gene duplication in male wood tiger moths" for further consideration by eLife. Your revised article has been evaluated by Christian Landry (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

The CRISPR experiment is important but lacks a more detailed description, as well as earlier and more explicit acknowledgement of its limitations, including that it failed to conclusively demonstrate that valkea (and not yellow-e) is responsible for the white/yellow switch. This uncertainty should be referred to earlier on (abstract?).

Relative to standard butterfly color pattern analysis, more information is necessary regarding the UV analysis (methods and wildtype phenotype), and regarding the use of "eumelanin" and "pheomelanin" which are usually reserved for vertebrates.

Reviewer #2 (Recommendations for the authors):

I have reviewed the revisions, and the authors have sufficiently addressed my previous concerns and suggestions. However, the authors' inclusion of additional CRISPR data is lacking critical information and analyses, which I detail below.

Lines 217 and 218 states that whole genome sequences of mutants were used to confirm mutants. However, there is no description of the methods used, nor can I find that those data are made available. Please add a description of the methods used for whole genome sequencing and confirming the presence of mutant alleles. I am also interested in what methods were used to test for off-target effects. It is particularly important to examine for potential off-target edits to other yellow genes.

Ln 220. Only one female survived to adulthood, and this had a mosaic phenotype. "This individual had one yellow forewing, similar to the male mutants, with the rest of the body and wings being wildtype (Figure 4 —figure supplement 1)." It is not at all clear that this female has one mutant wing. Both wings appear much more yellow than a white wildtype. I need some further phenotypic evidence (spectrophotometer readings or pigment analyses) as the phenotypic variation is not evident in the images provided. It would be ideal to see that the colors in mosaic mutant phenotypic regions are significantly different from wildtype (this can be done using spec readings from multiple wildtype wings and mutant wings). Second, there needs to be sequence verification of the mutations included in the manuscript, as previously mentioned.

Figure 4 —figure supplement 2 shows images UV. However, there are no methods provided for how these UV data were collected. Without some details of the imaging setup, I am unable to discern that images reflect differences in UV reflection, or may be due to variations in the imaging procedure. If possible, spectra analyses of the wings are an easy and cost-effective approach to quickly confirming changes in UV brightness on lepidoptera wings.

There is also no background information given for the wildtype UV. Lines 212-213 suggest the UV is a result of scale structures. What is the reference or evidence for this? Variation in UV reflection is known to be influenced by pigment composition in Pieris butterflies, not necessarily scale structures. To make assertions of UV being associated with scale structures, I would be interested in seeing the characterization of the putative UV related scale structures in wildtypes and mutants. This type of scale characterization (e.g. SEM and/TEM of wing scales in wildtype and mutants) is routinely included with other functional genomic studies of similar wing colorations (for examples see Ficarrotta et al. 2022, Livraghi et al. 2022, Concha et al. 2019, Matsuoka and Monteiro 2018). At a minimum, a detailed description/characterization of the wildtype UV should be given to the readers. Along these lines, I am curious to know if the UV may be iridescent. If so, some descriptive info on the iridescence would be needed (i.e. angle of incidence). Also, if iridescent, the differences in UV between wildtype and mutants should be examined further to determine if the image differences between wt and mutants are due to changes in the angle of incidence.

Ln 335-336. I am unclear what evidence supports yellow-e having a forewing-specific effect.

Ln 337-338 The authors state that yellow-e was "likely also knocked out…". I think this is misleading, as lines 218-219 states "All samples also showed evidence of editing at the corresponding yellow-e exons, which mainly involved insertions". Based on this it seems more than "likely", and actually confirmed yellow-e coding was disrupted in ALL samples.

Reviewer #3 (Recommendations for the authors):

The revised version of the manuscript successfully addresses most of my previous concerns.

Results from CrispR/cas9 experiments targeting the valkea gene were added to the manuscript in order to validate the role of this gene in the developmental switch from the yellow to the white morph. Such CrispR/cas9 experiments are challenging and obtaining high number of mutant adults is usually difficult in Lepidoptera.

Here a few male mutants and one female mutant were successfully obtained. Nevertheless, the lack of specificity of the CrispR guides resulted in modifications in both valkea and yellow-e genes in the few mutant individuals that reached the adult stage, therefore preventing the full characterisation of the respective functional implications of these two genes in the development of hind and forewing colour patterns in males and females.

From what I understood, the main argument for ruling out yellow-e as causing the white/yellow switch in male hindwings is the phenotype observed in a single mutant female showing in panel E of the supplementary figure 4. The sentences line 221-224 are not entirely convincing to me. The phenotype of the mutant female is used to point at the putative role of yellow-e on forewing colour in female. Does it lead to hypothesize a role of yellow-e on forewing colour in both sexes? And thus to a role of valkea in male hindwing colour? This indirect argument should be made clearer, and further discussion on the respective roles of these two genes in hind and forewing coloration is needed.

In the supplementary figure 4 (referred to as Figure 4 —figure supplement 1): the panel E shows the phenotype of the mutant female but picture of the wild-type female would be useful to fully evaluate the impact of the CrispR treatment on phenotypic variation.

Line 213: This is quite interesting, did you observe differences in scale structure between wild-type yellow and white scales, and in the wild-type yellow vs. mutant yellow scales? Such observations on the respective role of pigments and scale structure in the reflected colours are also relevant to understand the developmental bases of wing colour variations.
