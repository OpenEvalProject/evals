# Peer review - Round 1

Editors:
- Patricia J Wittkopp, University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.35471.061](https://doi.org/10.7554/eLife.35471.061)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Genetics of trans-regulatory variation in gene expression" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript makes use of an elegant experimental design to investigate how genetic variation influences gene expression in cis and trans. Using over a thousand genotyped segregants from a cross between two yeast strains, the authors investigate how inherited genetic variation accounts for differences in gene expression levels as measured by RNA-seq. The eQTL catalogue is fairly exhaustive and explains over 70% of the heritability in gene expression levels. The authors report that while 50% of genes harbor local, relatively large-effect cis-eQTLs, the aggregate effect of trans-acting eQTLs typically outweigh that of local variation. Those trans-eQTLs cluster in a small number of hotspots that are responsible for the majority of gene expression variation, likely due to reverberating indirect effects through the cell machinery. The study involves a large amount of experimental work and seems to have been designed with great care.

Concerns were raised about the novelty of many of the findings in this study relative to prior work, but the reviewers and editor were ultimately swayed to support publication based on the advance in rigor and resolution provided by this work combined with some new findings for the field. There were also other issues raised, however, that we think can be successfully addressed in a revision within the next 2 months.

Essential revisions:

1) Figures are quite poorly designed. Figure 5 is a particularly egregious example: panel B would be more readable as a violin plot, and there is definitely a better way to present panel A than grey lines of variable width with no legend. Color heatmaps such as used for chromosome contacts data come to mind. Similar concerns stand for Figure 1B and D, Figure 2A and Figure 4.

2) Most of the biological interpretation on trans-eQTLs hotspots relies on Gene Ontology analyses, and is rather weak and speculative. Considering that these hotspots contain variants with the ability to reverberate through the gene expression network and influence many genes, a more thorough analysis would have been appreciated: are some transcription factor binding sites overrepresented in those hotspots overall? How do these hotspots relate to the 3D structure of the genome? Do they exhibit special features relative to gene organization? During our discussion, we were unable to identify a particular set of analyses that would best address this point, however, so are passing along this comment for your consideration only.

3) The analysis on eQTLs with epistatic effects fell very short considering that, as the authors note, this study design is one of the few that can identify such interactions. Please expand the discussion and, if necessary, analyses in this section.

4) Relating these findings in yeast to human cells may be more complicated than suggested in the text. Please either better justify or tone down this extrapolation. Some differences articulated by one of the reviewers:

Much throughout the text, the authors draw links between the genetic architectures of gene expression levels in yeasts and in humans. While there are indeed similarities in the numbers, e.g. the median heritability of gene expression levels, or trans-variants accounting for 2-3X more expression variation than cis-variants, I do not think that there is enough evidence that the conclusions and observations made in this work applies to human cells (which I felt was implicit in the text). In fact, I do not think that the observations here apply to humans:

For example, there is limited to no evidence from current human data that trans-eQTLs cluster in a very small number of genomic regions. Even with the few number of trans-eQTLs that were found in data from GTEx (100-500 per tissue, I believe?), we would expect to see significant clustering. I am not sure if anyone has looked into this or seen this? The authors write that "the limited number of human trans-eQTL discovered to date also tend to influence the expression of multiple genes […] suggesting that a similar hotspot-dominated architecture could underlie human expression variation" but I find that quite unconvincing.

From Figure 1C, it seems that distant (trans) eQTLs explain typically 0.5-1X as much gene expression level variation compared to cis-eQTLs. I believe that in humans, the difference is much larger, i.e. trans eQTLs explain only 0.01 times to 0.05 times as much gene expression level variation as cis-eQTLs. Because the trans vs cis contributions are similar between humans and yeast, this could imply that trans-eQTLs for human genes are distributed far more uniformly than for yeast genes.

Furthermore another difference is that we would expect a strong enrichment for coding variants for the human trans-eQTLs that were found in previous studies, which does not seem to be case. Might there be strong selection against trans-variants with ubiquitous effects in humans?

For these reasons, I would suggest either the author to provide evidence that their conclusions apply to human, or explicitly caution readers against this interpretation.
