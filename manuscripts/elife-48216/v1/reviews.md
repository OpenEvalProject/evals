# Peer review - Round 1

Editors:
- Claude Desplan, New York University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.48216.043](https://doi.org/10.7554/eLife.48216.043)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Cis-regulatory basis of sister cell type divergence in the vertebrate retina" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor. The reviewers have opted to remain anonymous.

The paper has been reviewed by three excellent reviewers who have entered into an intense discussion about its strength and limitations.

As you will be able to see below, the reviewers find the comparison in transcription factor binding site usage between photoreceptors and bipolar cells to be of significant interest and worth publishing. However, the reviewers were also concerned about potential problems with the profiling of ON vs. OFF bipolar cells and the impact of the paper might depend on how well you can separate the ON and OFF bipolar cells. Only the Grm6-GFP, but not the YFP version that you have used, labels the ON BCs. If the data indeed are based on mixed ON/OFF populations, then this needs to be clearly stated in the manuscript that currently seems to implicate that the separation is perfect.

One suggestion would be to remove the entire ON vs. OFF portion of the manuscript, but in this case, the paper would be significantly weakened unless the comparison of photoreceptor to bipolar could be enhanced. The other alternative might be to combine the Shekhar et al. single cell data into ON and OFF pools and then compare them against your RNA-seq data to see if they are well correlated. If this were to be feasible, and the data were to support the separation, this would significantly strengthen the model. As for now, the comparison in Figure 2 is neither quantitative nor visually clear.

Reviewer #1:

In order to compare the cis-regulatory features of vertebrate photoreceptors and bipolar cells, Murphy et al. analyze the transcriptomes and open chromatin landscapes of these sister cell types. The authors find that the transcriptomes are very different, while there are similarities in the usage of cis-regulatory motifs, especially K50 motifs. Interestingly, bipolar cell-specific enhancers exhibit an enrichment of E-box motifs that are bound by bHLH TFs, while photoreceptor-specific enhancers exhibit an enrichment of Q50 motifs that are bound by Q50 homeodomain TFs. Murphy et al. demonstrate that a reporter, which labels both photoreceptors and bipolar cells, can be made photoreceptor-specific by mutating its K50 to Q50 motifs. They propose that such conversion and partitioning of cis-regulatory motifs, together with the emergence of transcriptional repressors (such as VSX2 that binds to Q50 motifs), were critical steps in the evolutionary divergence of photoreceptors and bipolar cells as separate sister cell types.

This rigorous and well-written manuscript should be of interest for a broad readership, as it proposes an exciting model for how closely related cell classes are distinguished during evolution and provides a great resource for the retina community.

- Is there anything special concerning the expression and/or function subset of genes that use dimeric Q50 motifs (Figure 4)? Do they have anything else in common?

- In the first paragraph of the Discussion section: “Thus, in both retina and spinal cord, expression of VSX2 promotes interneuron fate at the expense of the alternative 'effector' neuron (photoreceptor or motor neuron) cell type.” The wording is confusing, as a photoreceptor is not an effector neuron.

Reviewer #2:

In their manuscript, Murphy et al. describe a study which combines expression (with RNA-seq) and open chromatin (with ATAC-seq) profiling of the ON-bipolar (BC) and OFF-BC cells in the mouse retina. The aim is to identify TF binding motifs that function to differentiate the bipolar cells and the photoreceptors (PRs) and then ON-BCs from OFF-BCs. I have very mixed feelings about this paper for reasons outlined below.

Authors performed RNA-seq and ATAC-seq on cells FACS-sorted based on Otx2-GFP and Grm6-YFP to obtain BCs and to subdivide them into ON and OFF subclasses (Otx2-GFP/Grm6-YFP +/+ and +/- respectively, that can be discriminated based on brightness). However, according to Schubert et al. (2008), which describes the Grm6-YFP mice, "YFP is expressed in a subset of on-bipolar cells", i.e. sparsely, which allows them to do electrophysiology on these cells. If I read this correctly, this means that Otx2-GFP+/Grm6-YFP- population should contain a significant number of ON-BCs which did not express Grm6-YFP. Why Grm6 RT-PCR is clean is not clear, but other markers should also be used to rule out that ON is contaminating OFF population. Next, Shekhar et al. (2016) also found that one of the ON-BC subtypes (BC5D) expresses Grm6 at low levels if at all, probably resulting in little or no YFP expression and thus these cells would sort with the OFF population. Grm6 is expressed in the Rod BCs (RBCs) which authors here group with ON-BCs for their analysis. Yet, according to Shekhar et al. transcriptomicly ON- and OFF-BCs are more closely related to each other than ON-BCs are related to RBCs. This is pretty obvious from Figure 2, left panel. All of these issues have a strong potential to muddle the ON vs. OFF comparisons and should be addressed by the authors.

Indeed, perhaps the above issues are the reason why authors find that the relationship between chromatin accessibility and gene expression in the ON- and OFF-BCs is "complex". Yet in Figure 5—figure supplement 1C these are pretty clearly negatively correlated, a puzzling result. It would be nice to see this shown as in Figure 5C. Furthermore, this negative correlation would be interesting to explore for both, the BC vs. PRs as well as ON vs. OFF BCs. Thus, to me it seems that the strategy used in the second to last section of the Results (subsection “Photoreceptor- and bipolar-specific open chromatin regions are positively correlated with cell class-specific gene expression”) should be also applied to the ON vs. OFF, and also perhaps to be modified for the anti-correlated genes.

It is not clear to me why the authors did not use the single cell expression data from Shekhar et al. instead of their own RNA-seq data for comparison with the accessible chromatin regions. (By the way, authors' point that their pooled RNA-seq is somewhat more sensitive is a bit hollow given Shekhar et al. effort to optimize the tradeoff between the sequencing depth and the sequenced cell number.) Would it be possible to classify genes based on their expression in a particular cell type (or cell type pool) and to use the accessibility information simply to know where to look for the TF binding sites (i.e. without worrying about the enrichment of the accessibility)? If this were possible, authors could try to go deeper down the branches of the transcriptional relatedness tree from Shekhar et al., then just the first ON vs. OFF branch. A related question to this is whether (and how frequently) authors found different accessible chromatin regions for the same gene that were enriched in different cell classes?

I would remove Figure 2 (at least the right side) and Figure 2—figure supplement 2. They seem to be just reprinted Shekhar et al. data reordered according to RNA-seq "lowest adjusted p-value" of the present study. If authors want to compare the gene expression from the two studies, they need to find a way to pool Shekhar et al. data into PR, ON and OFF classes.

Regarding the electroporation experiments: While it is a nice idea to replace useless Q50 sites with K50 and show transcriptional repression, this experiment does not address the hypothesis posed in the second paragraph of the subsection “Photoreceptor and bipolar cells employ closely related yet distinct cis-regulatory grammars”, i.e. it does not show whether the presence of K50 makes chromatin inaccessible. Also, in the rest of the paper a distinction is made between enhancers and promoters, and the analysis of TF binding sites was done with enhancers, yet the electroporation experiment was done with a promoter (by their definition of <1000bp from a transcription start site) and in fact raises doubt whether the enhancer/promoter partition used by the authors in their analysis was the biologically relevant one. Finally, this experiment relies on pairing of two different TF binding sites, while sequence analysis showed that there is no enrichment of specific pairs in PR vs. BC comparison. In fact, it is not obvious to me why the authors did not find differential enrichment of the TF binding site pairs where one site is a differentially enriched TF binding site (Q50 and E-box).

In the Discussion, the evolutionary hypothesis is a nice touch, however, given that there are no experiments actually addressing it, does it deserve such a prominent role? Meanwhile, the many interesting observations (e.g. why there is no enrichment of TF binding pairs) remain unaddressed.

Finally, a major concern is that the paper is difficult to follow and was not written with a broad readership in mind. The authors reasoning is often not clear (e.g. subsection “Bipolar cells have a more accessible chromatin landscape than either rods or cones”, first paragraph), the definitions of the terms used are hard to find (promoter vs. enhancer is defined in the legend of a figure supplement, the fact that they use "TSS-distal" and "enhancer" as synonyms is also hidden in figure legends), figure legends are not clear (e.g. Figure 4—figure supplement 1) and sometimes it is just not clear what authors mean (what are "replicates" in the first sentence of Figure 3A legend). Finally, the entire paper needs some re-organization (e.g. the way PR vs. BC and ON vs. OFF comparisons are written up should parallel each other).

To sum up, while I am not against the publication of at least part of this data in eLife, the paper would need a major overhaul. There are seemingly large issues to address and the analysis feels superficial.

Reviewer #3:

In this manuscript, Murphy and colleagues examine the regulatory logic governing photoreceptor- and bipolar cell-specific gene expression. They generate a considerable amount of new data to describe the transcriptome and the open chromatin regions within bipolar cells. Murphy and colleagues then compare their results with prior data from photoreceptors. Interestingly, this revealed that photoreceptor and bipolar cell genes were enriched for different types of transcription factor binding sites. In one example, they show that subtly changing the type of binding site will restrict a broader expression pattern to be only made by photoreceptors. From their data, they then extrapolate a model to explain how bipolar cells evolved from a photoreceptor ancestral state. The experiments and data analysis in this manuscript are rigorous and compelling, but would be improved by some minor modifications. While the discussion about the evolution of photoreceptors is of high interest, the manuscript would be strengthened by additional discussion of the cis-regulatory findings. Specific recommendations are listed below:

1) A couple modifications to the data analysis and figures would improve the manuscript.

a) The authors mention that zinc finger transcription factor sites are more common in photoreceptors. However, this binding site preference data is not shown in Figure 4 (except for CTCF). Showing a zinc finger example in Figure 4 would improve the clarity of the manuscript.

b) In Figure 5C (and Figure 5—figure supplement 1D), it would help the reader to label some of the dots in these plots. For example, showing a few examples of known photoreceptor and bipolar genes. Highlighting a few discordant (black dots, e.g., Grik1) genes would help the reader as well.

c) In Figure 6D, the categorical format provides a nice summary of the data. However, a plot or table showing quantitative data and statistics would make a much stronger case that the type of binding site affects gene expression.

2) While the discussion about the evolution of photoreceptors and bipolar cells and Figure 7 are done well, it may be hard for readers to link the cis-regulatory data to the evolutionary model. In addition, there are some regulatory findings that are not discussed. The manuscript would benefit from a brief expansion of the Discussion section to address the cis-regulatory grammar findings in more detail. Addressing the following items would strengthen the manuscript:

a) Why is overall chromatin accessibility different between photoreceptors and bipolars? Does it impact the evolutionary model?

b) If bHLH factors are important for photoreceptor formation or maintenance, why are these cites depleted from mature photoreceptors? Are there differences between developmental and homeostatic/mature cis-regulatory networks? Are the cis-regulatory changes expected to be the same in a developmental context?

c) Why are bZIP sites (e.g., Nirl) strong in green cones and modest in rods (Figure 4)?

d) Why do some genes (e.g., Grik1) behave in a discordant fashion?
