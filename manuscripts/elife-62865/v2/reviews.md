# Peer review - Round 1

Editors:
- Karen E Sears, University of California, Los Angeles United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62865.sa1](https://doi.org/10.7554/eLife.62865.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript presents cutting edge data to compare the development of shark fin and mouse limb and an important discovery – the existence of a conserved mid-developmental stage in paired appendage development. This study is timely and important, and will make an excellent publication to eLife.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Developmental hourglass and heterochronic shifts in fin and limb development" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Jose Luis Gomez-Skarmeta (Reviewer #2).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

While the general scope of the paper is potentially suitable for eLife, it requires substantial additional analyses and discussion, as outlined in the reviews. In particular, it would be important to show the pattern of expression of Shh and its main targets in the bamboo shark to sustain the conclusions in Figure 2. Given that these experiments would likely take longer than the normal revision times for eLife papers, we reject the current version for now, but would consider a substantially revised new version.

Reviewer #1:

In this manuscript, to identify differences between limbs and fins, the authors generate and compare the temporal transcriptomes of mouse forelimb and bamboo shark pectoral fins. The comparison reveals a notable heterochrony of gene expression between limbs and fins. The analysis of distances of transcriptome profiles indicate stronger conservation at intermediate stages (hourglass-shaped conservation). Next the authors generate the ATAC-seq profiles of developing limb buds and find that conserved regulatory sequences are most active during mid-stage limb development.

This is an interesting study that requires some additional analysis and discussion to better sustain the conclusions reached.

Major concerns:

A major concern regarding this work is the use of the whole limb/fin for the transcriptomic and ATAC analyses. The limb bud is very heterogenous, even more as it develops, and this makes it difficult to extract conclusions using this kind of bulk analysis, more taking into account that late processes such as chondrogenic differentiation may greatly vary between mouse and shark.

Another concern is the scaling (maximum TPM=1, minimum TPM=0). While I agree that this helps capturing the dynamics of gene expression, it does not reflect the magnitude of the change and could lead to misleading interpretations. I think this may happen with the interpretation of the Shh pathway

1) Figure 2A: More information on the list of genes in each of the categories after gene-by-gene comparison of expression dynamics should be provided and discussed rather than only mentioning a couple of genes. The list should also be provided (i.e. excel). Particularly interesting is the inverse behavior of some genes in the "Heterochrony" group that are downregulated over time in the mouse limb bud being upregulated in the shark fin.

2) Figure 2D-E- I think that some hybridizations for Shh and its main targets in the bamboo shark are required to sustain the conclusions from these two panels. It may be that the sustained expression in the mouse corresponds to later chondrogenic stages that have already started at E12.5 and the whole heterochrony responding to different time resolution as mentioned by the authors. I don't agree with the authors in that the expression dynamics of HoxA/D genes is similar in both species, at least for the 5' members.

3) The consideration of ATAC sequences as active sequences should be softened as this is not always hold true. My interpretation is that most changes happen between 9.5 and 10.5, rather than conserved sequences being more active at E10.5

Reviewer #2:

This is an interesting study which aims to identify differences between fins and limbs. Performing transcriptomic comparison between pectoral fins from a non-model Chondricthyan species and forelimbs from mouse across a series of developmental stages, Onimaru et al. show that a noteworthy number of genes shows a heterochronic shift, alias a reverse temporal dynamic of expression between the two species. Moreover, they present an hourglass-shaped conservation of gene expression, but also of active regulatory regions in middle stages of development. Interestingly, in these stages they also detect more tissue- and stage-specific enhancers leading to the hypothesis that the middle developmental stages are evolutionary constrained by the increased regulatory complexity over pleiotropic genes.

This work shows how comparing distant species constitutes a good approach to understand how morphological novelties occur or are constrained during evolution and hints towards some of the changes that might have occurred during fin-to-limb transition. The data that Onimaru et al. have produced are also a good resource for the scientific community and the overall work leads to many interesting follow-up questions. Due to all the above reasons, I support the publication of this article in eLife.

However, the analyses presented are not always described as clearly or in-depth as desired and few observations are overstated. Therefore, I recommend the implementation of the comments below to strengthen the reliability, to enrich the content of the data presented and to prevent any confusion for the reader.

1) In Figure 2A, using hierarchical clustering the authors show that there is a heterochronic shift in gene expression between mouse limbs and shark fins. However, this group consists of different subclusters which not all follow exactly the general trend that the authors describe in their results. Could the authors discuss on these genes that still show different temporal dynamics of expression between sharks and mouse, but do not show opposite -timewise- trend than in mouse?

2) The authors should provide individual tables for each cluster described in Figure 2A (fin-specific, limb-specific, stable, conserved/late, heterochronic) instead of the Supplementary file 3, which is quite confusing in its current form.

3) In Figure 5, which are the GO terms associated to the genes for these clusters? What are the enriched motifs in cluster 8, largely specific to E9.5, and the GOs of the associated genes? The full list of motifs and associated genes for each cluster should be available. Moreover, is the conservation degree of the ATAC peaks different for each cluster?

4) As far as the HOMER analysis is concerned in Figure 5, why the authors used the extended sequence length of 1400 bp to perform TF motif analysis? Also, did they perform the enrichment analysis with default HOMER options? If so, random genomic regions were used as a statistical background. Can these results be replicated when using a more biologically relevant background? For example, the peaks of Cluster5 are enriched in CTCF when compared to random regions of the DNA (the default HOMER approach), but are they also enriched in CTCF when compared to all the open chromatin regions that were detected during development?

5) Results first paragraph: the figure supplement 4, not 1, refers to the details of RNA-seq data.

6) Have the authors used all three replicates in the transcriptomic analyses? We could assume that due to the last sentence referring to that in Figure 1—figure supplement 4, but it should be clearly stated.

7) Could the authors explain why they used only one of the replicates for the ATAC-seq hierarchical clustering in Figure 5A and comment whether the ATAC-seq peaks tested were present in all 3 replicates?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Developmental hourglass and heterochronic shifts in fin and limb development" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Detlef Weigel as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Gunter Wagner (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below primarily address clarity and presentation.

Summary:

The authors present a detailed RNAseq and ATACseq comparison of mouse limb development and bamboo shark pectoral fin development. This study provides a wealth of functional genomic data leading to an important discovery: the existence of a mid – developmental "hour glass like" constrained stage of limb development. This is a significant discovery because it suggests a mechanistic basis for conserved developmental identities as the sub-organismal level. The homology of paired fins and limbs is not in question since upwards of 200 years, but understanding the developmental/mechanistic basis for this fact is a still unresolved issue in biology. This paper makes an important step in resolving this issue.

Revisions:

Given the recent publication of Dr. Woltering (https://pubmed.ncbi.nlm.nih.gov/32875118/), the authors may want to comment on this paper in relation with the Shh, Hox expressions they report.

We suggest that the authors indicate, at least in Materials and methods, their failure to detect Shh expression by ISH. Knowing this may be of help for other researchers.

Results paragraph three: Figure 1—figure supplement 7 instead of 8?

Introduction: the expression of Hoxa11 and Hoxa13 is actually not conserved in fin development, because the critical spatial exclusion of their expression domains is NOT seen in fins, even though a distal bias of Hoxa13 expression is shared. Please correct.

It is surprising to find 16,442 orthologs between shark and mouse, given that 1-1 orthologs among a sample of 10 eutherian species finds only <8,000 orthologs. A comment on this finding might be in order.

Results paragraph three: a non-colinear relationship in Hoxd gene expression levels also applies to chicken wings, where Hoxd12 is higher expressed than all the others, but I am not sure that was ever published. This could point to a scenario where mouse limb development is not as paradigmatic as it often seems.

Subsection “Comparison of SHH signaling pathways in limb and fin buds”: it is hard to see how Shh delayed onset can be supported without a rigid mapping of developmental stages between fin and limb development.

Discussion paragraph three: Please add reference to Piasecka et al., 2013.

Discussion paragraph four: We think it is important to be precise here. The correct statement is that mutations affecting this stage have more dramatic fitness consequences, rather than that it is less susceptible to mutation. What creates this impression is that the substitution rate is less not necessarily the mutation rate, as the authors note in the next sentence.
