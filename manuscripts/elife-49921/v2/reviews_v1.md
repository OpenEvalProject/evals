# Peer review - Round 1

Editors:
- Brad Davidson, Swarthmore College United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.49921.sa1](https://doi.org/10.7554/eLife.49921.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This article provides fundamental insights regarding regulatory mechanisms that dictate precise gene expression and thus ensure proper cell fate specification. By leveraging an exceptionally well-characterized heart and pharyngeal muscle lineage gene network in an invertebrate chordate model, this study provides profound insights into principles governing reliable and accurate network deployment. The authors employ in-depth, comprehensive chromatin accessibility profiling and extensive functional manipulations to generate substantive support for a novel "combined enhancer" model. According to this model, precise regulation of crucial transcription factors is mediated by heterologous combinations of regulatory elements with distinct inputs and chromatin accessibility profiles. Strikingly, these heterologous elements function synergistically as a regulatory unit to generate a single, precise spatio-temporal expression pattern. The authors convincingly demonstrate that removal of individual elements within these combinatorial units or deployment of homologous combinations disrupt expression and can lead to improper specification. Should future studies indicate that such combinatorial regulatory elements are broadly deployed, this would have wide-ranging implications regarding gene network architecture as well as the potential impact of non-coding mutations in the context of evolution and disease.

Decision letter after peer review:

Thank you for submitting your article "Combinatorial chromatin dynamics foster accurate cardiopharyngeal fate choices" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Didier Stainier as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

There was a strong consensus among the reviewers that this paper contains findings that are of broad general interest and are appropriate for publication in eLife once revisions have been made to more clearly align their data with their conclusions. In particular, the reviewers were impressed by the broad scope of their ATAC-seq analysis, the innovative application of this technique to Ciona, some of the more in-depth findings regarding specific regulatory elements and some of the insights provided by this analysis in regards to more general principles of regulatory logic.

However, the reviewers had a number of critical concerns including a lack of clarity in some key definitions and figures, some questions regarding interpretation of specific assays and experiments and a lack of sufficient support for some of their major conclusions including the proposed combined enhancer model.

The was also a consensus that these concerns can be addressed in two ways. The authors can either modify their conclusions to better match their current data or they can conduct further experiments to more robustly support their current conclusions.

Reviewer #1:

In this study, Racioppi, Wiechecki and Christiaen have deployed an impressive series of genome-wide analyses complemented with CRISPR/Cas9-mediated genome editing. The study addresses chromatin accessibility profiles during early development of cardiopharyngeal lineages in Ciona. In this lineage, three rounds of asymmetric cell divisions, which are controlled by differential activation of FGF-MAPK signals in a reiterative manner, lead to generation of four cell types, first heart precursor (FHP), second heart precursor (SHP), atrial siphon muscle precursor (ASMP) and anterior tail muscle (ATM). The Christiaen laboratory is one of the major players in deciphering the underlying transcriptional and signalling control of the cardiopharyngeal lineage segregation. The current study reveals another layer of such regulatory mechanisms, in particular, chromatin accessibility, by deploying ATAC-seq on isolated cardiopharyngeal lineage cells. The study contains a huge amount of bioinformatic analyses, which, to be honest, are very hard for me to digest. Nonetheless, I really appreciate the last part of their study highlighted in Figures 5, Figure 5—figure supplements 1 and 2, which focuses on chromatin accessibility profiles of two key genes of cardiopharyngeal fate choices, Ebf and Tbx1/10. It reveals convincingly that these genes are controlled by multiple cis-regulatory elements with distinct temporal chromatin accessibility profiles and distinct TF-binding motif compositions. This finding indeed represents the main message of the current study.

I have a few comments (questions):

1) For Figure 5A and Figure 5—figure supplement 2A, it would be informative to include the ATAC-seq dataset of FoxF(CRISPR)-10 hpf.

2) I assume that changes in chromatin accessibility between FGFR(DN)-10 hpf and FoxF(CRISPR)-10 hpf would exhibit a certain degree of correlation since FoxF is transcriptionally activated by FGF signals in TVCs. It would be nice if the authors could conduct a correlation test. There seems to be such a correlation for the peak ID KhL20.169 within Gata4/5/6 locus (Figure 3—figure supplement 2A and Figure 3—figure supplement 4D).

3) Why do the authors call MyoD905>GFP cells as mesenchymal cells? Aren't they muscle cells (Christiaen et al., 2008)?

4) The authors mention "cardiopharyngeal markers" that include TVC progenitor markers, primed cardiac markers, primed ASM markers, de novo cardiac markers, de novo ASM markers and ATM markers. The definition for these different markers is supposed to be described in supplementary text. I imagine that the authors are meaning that in the "Gene Set Enrichment Analysis (GSEA)" section but it doesn't help me to understand the definition. A clearer definition, together with gene lists for the different categories of cardiopharyngeal markers as a supplementary table, would be helpful.

Reviewer #2:

This manuscript by Racioppi et al. performs the first ATAC-seq experiments in the early heart cell lineages of Ciona in order to find enhancers that are accessible in sublineages of the heart. This paper creates a very valuable resource for the heart and ciona communities. I don't feel that the authors make the most of their data and the value of this work is skipped over to focus on the combined enhancer. Overall I find there are too many interpretations/extrapolations without sufficient evidence and these detract from the excellent quality and substantial value of this dataset for understanding heart development. I would recommend that the authors focus on their data and what it tells us about the regulatory networks and developmental programs of the heart rather than the concept of combined enhancers.

Combined enhancers:

A major claim of the paper, that "combined enhancers" foster spatially and temporally accurate fate choices, by increasing the repertoire of regulatory inputs that control gene expression, through either accessibility and/or activity" is only supported by a study of only one locus shown in Figure 6, and I have issues with how the experiment is designed. The authors do an experiment in Figure 6 where they multimerize a weak enhancer (1x, 2x, 3x) and find that when 3 copies of the weak enhancer are put next to each other in a certain way, they find ectopic expression by reporter assay. They then say that this, coupled with evidence that many weak enhancers in the genomic context do not cause ectopic expression, show that these "combined enhancers" foster spatially and temporally accurate fate choices. However, this is comparing apples (3 identical enhancers with non-endogenous spacing together on a plasmid reporter) to oranges (3 unique endogenous enhancers with endogenous spacing in the genome). Since spacing between enhancers and genomic context can affect transcriptional output, I would believe this more if they put the 3 unique weak enhancers from the genomic context into a synthetic construct with spacings like the 3x multimerized enhancer and showed that these constructs did not yield ectopic expression. Even if this experiment were to show that the different inputs led to specific expression, I don't understand how this type of enhancer is different from enhancers using different inputs turning on at different times and space during a developmental program.

Definition of Shadow enhancer: The authors state that "shadow enhancer promotes robust transcription through the actions of multiple elements mediating similar regulatory inputs". Based on the literature I wasn't able to find a consensus that shadow enhancers have to use similar inputs, indeed it is very hard to pin down exactly what the inputs for many shadow enhancers are. Perry, 2011/Hong, 2008.

Reviewer #3:

In this manuscript, Racioppi et al. investigate the temporal dynamics of chromatin accessibility during the different steps of cardiopharyngeal progenitor specification in larvae of the chordate Ciona. They sample different cell types at different time points post fertilization, ranging from Mesp1+ founder cells after 6 hours to first and second heart progenitors, as well as atrial syphon precursors and anterior tail muscle cells after 18 hours. They show that global accessibility decreases with time, and that most enhancers are opened early during the process, in multipotent progenitors, even though their associated genes are mostly activated later. Using CRISPR-mediated deletions and reporter assays, they demonstrate that the enhancers they identify are necessary and sufficient to activate gene expression with temporal and spatial specificity. They then identify putative regulators of stage- and cell-type specific enhancer accessibility and confirm Foxf as a driver of enhancer accessibility in the cardiac lineage. Then, they study the locus of Ebf, where multiple enhancers are necessary for its expression in atrial muscle precursors. Finally, they study combinatorial effects of Ebf enhancers using a reporter assay and find that multiple copies of the same enhancer increase transcription efficiency, at the cost of precocious activation, whereas one copy of a combined enhancer construct recapitulates gene expression with greater temporal fidelity.

In this well-conducted study, the authors present solid data to back their conclusions, which are interesting for the field of development. Some points could be addressed to strengthen their claims:

- Does their reporter assay recapitulate enhancer accessibility or activity? This is unclear because the loss of the genomic context may cause an enhancer to be more easily activated. What is the timing of activation of the reporter gene in regard to the timing of chromatin accessibility and gene transcription activation?

- For the enhancers they define as being dependent on Foxf, does the knockout of Foxf impede their activation in a reporter assay? Or are enhancers containing mutated Foxf sites inactive (endogenously or in a reporter essay)?

- The authors could use histone marks to assess if the decoupling between accessibility and gene activation is also seen between gene activation and accumulation of histone marks typical of active genetic elements, such as histone 3 lysine 27 acetylation, if it is technically possible for them with their low number of cells.

- Figure 4A-C and the corresponding text are unclear. It is difficult to understand how the later comparison of FGF-MAPK perturbation relates to the rest of the paper.
