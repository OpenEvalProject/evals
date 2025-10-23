# Peer review - Round 1

Editors:
- Anne E West, Duke University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55159.sa1](https://doi.org/10.7554/eLife.55159.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In this manuscript the authors identify functions in postmitotic neurons for the chromatin structural protein CapG, which is part of the condensin I complex. Condensin is well known to play a role in chromosome condensation and loop extrusion in recently divided cells. However its functions in postmitotic cells have been less clear. The idea that nuclear architectural proteins might be repurposed in non-dividing cells for transcriptional regulatory purposes is interesting, and this manuscript provides a solid set of data for establishing that there are non-mitotic function of CapG in neurons.

Decision letter after peer review:

Thank you for submitting your article "Condensin I subunit Cap-G is essential for proper gene expression during the maturation of post-mitotic neurons" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by K VijayRaghavan as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript the authors identify functions in postmitotic neurons for the chromatin structural protein CapG, which is part of the condensin I complex. Condensin is well known to play a role in chromosome condensation and loop extrusion in recently divided cells. However its functions in postmitotic cells have been less clear. The authors became interested in CapG in neurons when they found it binding a neuronal transcription factor by yeast two-hybrid. Here they show CapG is expressed in postmitotic neurons and then studied phenotypes in flies where CapG was knocked out in neurons and used the TaDa DamID method to study CapG binding in neurons.

All three reviewers found the idea that nuclear architectural proteins might be repurposed in non-dividing cells for transcriptional regulatory purposes to be compelling, and they felt that this manuscript provides a solid set of data for establishing that there are non-mitotic function of CapG in neurons. However there were several significant technical concerns raised, some of which may be addressed with text revisions, but in particular the interpretation of TaDa data require additional validation.

Essential revisions:

Essential revisions fall into three areas relating to 1) the TaDa peak calling, 2) the relationship of CapG binding to chromatin and gene expression, 3) the interpretation of the elav and nsyb phenotypes.

1) Although the reviewers agreed that the TaDa approach was a good one for mapping CapG binding in neurons, all expressed some concerns about the details of the TaDa data. The reviewers noted that peak calling using the TaDa approach is challenging since the signal to noise is very modest compared to high quality ChIP-seq signals. Furthermore for CapG the signals appear to be very broad, which makes them poorly amenable to traditional peak calling. The reviewers agreed that the authors should either systematically validate their peak calling of TaDa datasets with replicates as they have done in a separate ELife paper published recently, or adapt their computational analyses to reflect the broader binding patterns of CapG compared to transcription factors. This was a topic of substantial discussion among the reviewers during the commentary period. Specific comments from the reviewers on this point are below. We include this information so the authors can see the kinds of concerns that were raised and we encourage them to offer what they feel is the strongest response either with the addition of more data or with a revised analysis approach.

• Figure 4A: What fraction of TaDa peaks are statistically detected in all replicates for each condition? Reproducibility between replicates is important for understanding how much of the differences between conditions is due to biological or technical variability. Could the author please show the individual replicates for all examples in 4A? Rigorous analyses using multiple replicates (as the authors performed in Sen et al. eLife 2019) would be necessary.

• Alternatively, using "aggregate" computational analyses such as in Figure 4D-F would be acceptable, if the peak analyses proved to be not reproducible across replicates for individual genomic loci. I would leave the biological replicate experiments up to the authors, who may find it useful for statistical analyses comparing the genetic lines and possibly to strengthen/convince us that their peak calling is the accurate way to characterize CapG binding.

• Condensin may not bind in the same manner to chromatin as transcription factors or histone modifications, which often show sharp peaks. Based on the examples presented in Figure 4A, the observed negative-going "valleys" may be also meaningful signal. Using the aggregate Cap-G TaDa signal across the entire gene body might be yet another alternative statistical method for comparing between conditions and across replicates (this is a common strategy for RNA-Seq statistical analyses).

• Looking at their few examples, it appears CapG binds more like chromatin regulators that have broad gene-body distributions (i.e. elongation regulators, MECP2). Peak callers like MACS2 used in this study would not be appropriate in this scenario and alternative computational methods are more appropriate. If the authors wish to use peak calling, they must use replicates with statistical measures to validate peak calling reproducibility.

• In the examples in 4A, it is unclear how to interpret the results. For example, for the dacapo gene, the peaks upstream of the gene appear preserved in all experiments (even if peak calling may be different between conditions due to statistical thresholds). However, there is no mention of these upstream peaks. Another example are the peaks identified in the genebody of unc-89, which are somewhat randomly distributed across the various conditions. Are the differences between conditions biological or due to technical variability? Finally, for the bruchpilot gene, the authors state that Cap-G binding is stronger in NSCs than mature neurons. However, there are several positive signals along the gene body of bruchpilot that are conserved in both the elav-GAL4 and nsyb-GAL4 neurons and, although distinct, appear to have equal amplitude as the "statistically-significant" peaks in the wor-GAL4 condition. Together, if these examples represent the typical peak calling, this reviewer is concerned about interpretability of subsequent analyses that rely on peak calling (4B, 4C).

Finally, one reviewer also raised an independent point about these data, saying: "The DamID data suggest there are different binding patterns of CapG in NSCs, immature neurons and mature neurons. Might there be differences in expression in the different lines that could make apparent differences in binding? Also are the DamID lines functional overexpressors of CapG? If so, how do the authors know the binding of the transgene is representative of the endogenous gene?"

2) A second major concern raised by the reviewers regards the comparison of CapG binding to open chromatin and gene expression.

For Figure 4D-E, the methods for how the authors identified putative enhancers or open chromatin is missing (authors only indicate from REDFly). Are these putative enhancers and open chromatin curated from all cells or matched to the specific cell types and developmental stages they are studying? If the vast majority of enhancers and "open" chromatin regions are largely inactive in bulk populations of cells, then the observed results would reflect Cap-G preferentially binding to open chromatin, but only in cell type-specific manners. The authors should perform the same analyses using active enhancers and bonafide open chromatin regions specifically from their tested cell stages. If they have done so, they should clearly state how they did this.

With respect to how this relates to gene expression, the reviewers were not convinced by the arguments in the text. How do the authors propose that CapG bind only to repressive chromatin, but upon knockdown of CapG, then downregulated genes are localized to active chromatin? The authors need to comment on this, particularly since they are arguing CapG is directly regulating both the upregulated and downregulated genes via its binding to both groups of genes. As another reviewer stated, It is unclear from their data why equal numbers of genes are up and down regulated. If Cap-G preferentially binds to repressive chromatin, as the authors argue in Figure 4, how does loss of Cap-G leads to the downregulation of neuronal genes, which should be regulated by active chromatin in neurons? I think that the authors should comment on: a) the low number of overlapping genes up- and down-regulated in nsyb- and elav-driven CapG knockouts and b) on the huge difference between the up- and down-regulated genes between the 2, which could be very interesting.

3) The reviewers raised concerns that elav can be expressed in progenitors and thus felt that the authors cannot use the elav line as definitive evidence for postmitotic functions of CapG.

They indicated that addition of a dividing cell marker (such as Dpn) in Figure 1—figure supplement 1A would be needed to validate that CapG is not reduced in dividing cells. Given that the authors show convincing behavioral data using the nsyb-KD line that indicates a function for Condensin in neurons, the conclusions based on the elav line could be toned down to admit possible expression in progenitors without undermining the story that the authors with to tell here.

With respect to the behavioral phenotypes in the nsyb line, although the reviewers were convinced that there were phenotypes (confirming functions of CapG in neurons) they did not think that detailed description of these phenotypes was highly meaningful given the survival deficits. Thus the commentary on CapG functions in behavior could also be written back.
