# Peer review - Round 1

Editors:
- Tricia R Serio, The University of Massachusetts, Amherst United States

Reviewers:
- Kevin Morano, Department of Microbiology and Molecular Genetics University of Texas Medical School, Graduate School of Biomedical Sciences Houston United States
- David Pincus, University of Chicago United States

## Review text

DOI: [10.7554/eLife.47791.028](https://doi.org/10.7554/eLife.47791.028)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Cytoplasmic protein misfolding titrates nuclear Hsp70 to activate Hsf1" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by David Ron as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Kevin Morano (Reviewer #2); David Pincus (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The transcription factor Hsf1 is conserved in eukaryotes and induces expression of molecular chaperones following heat shock and other environmental stresses. Despite the deep conservation of this transcriptional circuit, the biochemical mechanisms that control Hsf1 activity have remained unclear. The Hsp70-Hsf1 regulatory circuit has been the subject of renewed interest in the last few years, and this report addresses several less well understood features of control of the ancient heat shock response (HSR) in yeast through biochemical reconstitution and in vivo analyses. The studies seek to add three important contributions to the field: (1) Hsf1 can bind Hsp70 and DNA at the same time; (2) Hsf1 is a typical Hsp70 client; (3) Excess Hsp70 removes Hsf1 from DNA; (4) Cytosolic misfolded proteins are primary Hsf1 agonists. The reviewers are in agreement, however, that additional experimental support is necessary to support these interpretations.

Essential revisions:

1) Hsf1 can bind Hsp70 and DNA at the same time:

a) A direct demonstration of Hsp70 in DNA bound complexes is essential to draw this conclusion. Specifically, Hsp70 association with Hsf1 at target gene promoters in cells by ChIP to the Ssa2 or HSC82 promoter under non heat shock conditions and/or supershift of the DNA bound complexes assessed by EMSA in vitro would significantly strengthen this interpretation.

b) It is also not clear how the stoichiometry between Hsf1 and Hsp70 was determined to be 3:1. (The complex is 620 kDa; Hsf1 = 115 kDa; Hsp70 = 70 kDa. 3*115+70 = 415). A 3:3 stoichiometry, at 555 kDa would also be consistent with the apparent mobility. Based on the UV crosslinking, a denatured monomer of Hsf1 binds to Hsp70, so what is the evidence that a trimer only has a single Hsf1 bound?

c) The data that ATP relieves Ssa1-mediated inhibition of DNA binding is less compelling. There appears to be no effect at the 5X Ssa1 excess condition, and only minimal at 10X.

2) Hsf1 is a typical Hsp70 client:

a) The interpretation of the experiments is unclear on this point. Do the authors consider the observed effects to be due to Sse1 modulating Ssa1 nucleotide status and SBD binding to Hsf1 or to substrates in general (i.e., direct or indirect)? It is possible both scenarios are true, but they have not been distinguished. Clarification and direct experimental support, such as UV crosslinking to measure the interaction between Hsp70 and Hsf1 in WT cells treated with AzC, in Sse1-NLS cells under control conditions, and in fes1∆ cells under control and heat shock conditions, are needed to solidify this component of the model.

b) The subcellular site of competition for Hsp70 is unclear. The authors favor the nucleus, but no experimental support is offered. Either the model should be directly tested, or this strong interpretation should be removed from the manuscript.

c) Figure 4: the effects of AzC on both the HSR and the Msn2/4-mediated ESR have been well-established and it is not clear where the novelty lies in these experiments. Likewise the Hsp104-GFP behavior with CHX is well known – repetition/confirmation in this figure is probably unnecessary. However the leucine starvation experiments are a nice touch. Based on these data, it would be expected that Hsp104 would also not localize to puncta after leucine starvation – the authors should demonstrate this to complete the orthogonal validation of the nascent chain misfolding hypothesis.

3) Excess Hsp70 removes Hsf1 from DNA:

The data that ATP relieves Ssa1-mediated inhibition of DNA binding is less compelling. There appears to be no effect at the 5X Ssa1 excess condition, and only minimal at 10X. The lack of statistical treatment of these data (and indeed the entire manuscript) further reduces confidence in possible effects.

What is not clear is how the addition of excess Ssa1 modifies this complex to reduce DNA binding as shown in Figure 1E. What is the difference between the DNA binding-competent complexes and the so-called latency complexes? Does the molar excess of Ssa1 lead to supercomplexes with Hsf1 that could be detected by SEC or native PAGE? Does Hsf1 remain trimerized and bound to the same amount of Hsp70 after dissociating from DNA?

4) The manuscript also explore the impact of impaired cytosolic Hsp70 client release on the degree of Hsf1 de-repression. Reviewer support for this line of inquiry was significantly less enthusiastic given the fact that the authors' lab and others have previously demonstrated that cells lacking Fes1 constitutively activate the HSR specifically through Hsf1. Based on the input from reviewers, this aspect of the manuscript should be removed or alternatively extended:

a) The physiological relevance of this effect is unclear. Is there evidence that wildtype cells access this gene expression program with different levels and/or types of stress?

b) Why is this hyperactivation happening, and what are the genes that are differentially expressed and what is special about them besides the GO assignments?

c) The presentation of the RNA-seq data should be improved. The number of genes called as upregulated and downregulated seems to be an arbitrary choice of the z-score threshold, and the heat map clusters are unlabeled and therefore uninformative. A less opaque analysis would be two volcano plots showing all genes in the genome, where fold change of fes1∆/WT (in control and heat shock conditions) on the x-axis and a p-value for the significance based on the biological replicates on the y-axis. This will more clearly show across the genome how different the two strains are in the two conditions.

d) The authors should also examine the full sets of functionally-defined Hsf1 and Msn2/4 target genes (Pincus et al., 2018 for Hsf1, Solis et al., 2016 for Msn2/4) rather than just cherry picking 5 genes. The major result of the RNA-seq seems to be that the same genes are induced in WT and fes1∆, but just to a greater magnitude in the fes1∆ cells. This suggests that Hsf1 is just on to a higher gear – i.e., fully dissociated from Hsp70 – but not doing anything qualitatively different. A prediction here is that RNA seq in heat shocked ssa1/2∆ double mutant would look the same as fes1∆. If the authors want to claim that Hsf1 has an expanded target gene repertoire in this situation, they will have to provide further evidence (e.g., ChIP Hsf1 to these new genes).

e) Figure 5J: the observation that additional Hsp70 (or at least a protein migrating near 70 kD – no antibody verification of the presumed chaperone band is provided) associates with the pellet in heat-shocked fes1∆ mutants is intriguing but incomplete. Namely, how much of the material observed is due to new synthesis vs. additional aggregating substrate? More importantly, is the soluble pool of Hsp70 visibly reduced? The experiment tracks input and concentrated pellet, which gives the impression that much of the Hsp70 has partitioned to the pellet. However the soluble pool composed of Ssa1/2 and the newly induced Ssa3/4 may not change.
