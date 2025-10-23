# Peer review - Round 1

Editors:
- Marisa Nicolás, Laboratório Nacional de Computação Científica Brazil

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.88833.2.sa0](https://doi.org/10.7554/eLife.88833.2.sa0)

This valuable study presents a screening pipeline (SPICE) for detecting DNA motif spacing preferences between TF partners. SPICE predicts previously known composite elements, but experiments to elucidate the nature of the predicted novel interaction between JUN and IKZF1 are incomplete. These experiments would benefit from more rigorous approaches using other databases to explore additional relevant data. The work will be of broad interest to those involved in dissecting the regulatory logic of mammalian enhancers and promoters.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88833.2.sa1](https://doi.org/10.7554/eLife.88833.2.sa1)

The authors report a new bioinformatics pipeline ("SPICE") to predict pairwise cooperative binding-sites based on input ChIP-seq data for transcription factor (TF)-of-interest, analyzed against DNA-binding sites (DNA motifs) in a database (HOCOMOCO). The pipeline also predicts the optimal distance between the paired binding sites. The pipeline correctly predicted known/reported transcription factor cooperations, and also predicted new cooperations, not yet reported in literature. The authors choose to follow up on the predicted interaction between Ikaros and Jun. Using ChIP-seq in mouse B cells, they show extensive overlap in binding regions between Ikaros and Jun in LPS+IL21 stimulated cells. In a human B-lineage cell line (MINO) they show that anti-Ikaros Ab can co-immunoprecipitate Jun protein, and that the MINO cell extracts contain protein(s) that can bind to the CNS9 probe (conserved region upstream of IL10 gene), and that binding is lost upon mutation of two basepairs in the AP1 binding motif, and reduced upon mutation of two basepairs in the non-canonical Ikaros binding motif. Part of this protein complex is super-shifted with an anti-Jun antibody, and more DNA is shifted with addition of an anti-Ikaros antibody.

The authors perform EMSA showing that recombinant Jun can bind to the tested DNA-region (IL10 CNS9) and that addition of recombinant Ikaros (or anti-Ikaros antibody in Fig 3E) can enhance binding (increase amount of DNA shifted). The authors lastly show that the IL10 CNS9 DNA region can enhance transcription in B- and T-cells with a luciferase reporter assay, and that 2 bp mutation of the Ikaros or Jun DNA motifs greatly reduce or abolish this activity.

This is interesting work, with two main contributions: The SPICE pipeline (if made available to the scientific community), and the report of interaction between Ikaros and Jun. However, the distinction between DNA motifs, and the proteins actually binding and having a biological function, should be made clear consistently throughout the manuscript. The same DNA motifs can be bound by multiple factors, for instance within transcription factor families with highly homology in the DNA-binding regions of the proteins.

Some specific points:

SPICE: It is unclear if this is uploaded somewhere to be available to the scientific community.

It was unclear if Ikaros-Jun interaction was initially found from primary Jun ChIP-seq (and secondary Ikaros motif from HOCOMOCO) or from primary Ikaros CHIP-seq (and secondary Jun motif from HOCOMOCO). And - what were the two DNA motifs (primary and secondary, and their distance) from the SPICE analysis?

Authors have mostly careful considerations and statements. One additional comment is that binding does not equal function (Fig 2D), and that opening of chromatin (by any other factor(s)) can give DNA-binding factors (like Ikaros and Jun) the opportunity to bind, without functional consequence for the biological process studied.

Figure 2E: Ikaros is reported to be expressed at baseline in murine B cells, yet the Ikaros ChIP-seq in unstimulated cells had what looks to be no significant or low peaks. LPS stimulation induced strong Ikaros ChIP-seq signal. A western blot showing the Ikaros protein levels in the 3 conditions could help understand if the binding pattern is due to protein expression level induction. Similar for Jun (western in the 3 conditions), which seemed to mainly bind in the LPS+IL21 condition. Furthermore, as also suggested below, tracks showing Ikaros and Jun binding from all conditions (unstimulated, LPS only and LPS+IL21 stimulated cells), at select genomic loci, would be helpful in illustrating this difference in signal between the different cell conditions. This is relevant in regards to the point of cooperativity of binding.

ChIP-seq in mouse B cells showed that Ikaros bound strongly in LPS stimulated cells, in the (relative) absence of Jun binding (Fig. 2C). However, in EMSA (Fig 3C), there is no binding when the AP1 site is mutated, and the authors describe this as Ikaros binding site. What does the Ikaros binding look like at this genomic location in LPS (only) stimulated cells? The authors could show the same figure as in Fig 2F but show Ikaros and Jun ChIP-seq tracks at IL10 CNS9 locus from all conditions to compare binding in unstimulated, LPS and LPS+IL21 cells.

Also: How does this reconcile with the luciferase assay in Fig 4E, where LPS (only) stimulation is used, which in Fig 2E only/mainly induced Ikaros, and not Jun ChIP-seq signal (while EMSA indicate Ikaros cannot bind the site alone, but can enhance Jun-dependent binding).

Comment on statements in results section: The luciferase assays in B and T cells do not demonstrate the role of the proteins Ikaros or Jun directly (page 10, lines 208 and surrounding text). The assay measures an effect of the DNA sequences (implying binding of some transcription factor(s)), but does not identify which protein factors bind there.

Lastly, the authors only discuss Ikaros (using the term IKZF1 which is the gene symbol for the Ikaros protein). There are other Ikaros family members that have high homology and that are reported to bind similar DNA sequences (for instance Aiolos and Helios), which are expressed in B-cells and T-cells. A discussion of this is of relevance, as these are different proteins, although belonging to the same family (the Ikaros-family) of transcription factors. For instance, western for Aiolos and Helios will likely detect Aiolos in the B cells used, and Helios in the T cells used.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88833.2.sa2](https://doi.org/10.7554/eLife.88833.2.sa2)

The study is performed with old tool Spamo (12 year ago), source data from Encode (2010-2012), even peak caller tool version MACS is old ~ 2013. De novo motif search tool is old too (new one STREME is not mentioned). Any composite element search tool published for the recent 12 years are not cited, there are some issues in data analysis in presentation. Almost all references are from about 8-10 year ago (the most recent date is 2019)

The title is misleading

Instead of

A new pipeline SPICE identifies novel JUN-IKZF1 composite elements

It should be written as

Application of SpaMo tool identifies novel JUN-IKZF1 composite elements

It reflects the pipeline better but honestly shows that the novelty is missed.

The study was performed on too old data from ENCODE, authors mentioned 343 Encode ChIP-Seq libraries, but authors even did not care even about to set for each library the name of target TF (Figure 1E, Figure S2, Table 2).


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88833.2.sa3](https://doi.org/10.7554/eLife.88833.2.sa3)

The authors of this study have designed a novel screening pipeline to detect DNA motif spacing preferences between TF partners using publicly available data. They were able to recapitulate previously known composite elements, such as the AP-1/IRF4 composite elements (AICE) and predict many composite elements that are expected to be very useful to the community of researchers interested in dissecting the regulatory logic of mammalian enhancers and promoters. The authors then focus on a novel, SPICE predicted interaction between JUN and IKZF1, and show that under LPS and IL-21 treatment, JUN and IKZF1 in B cells have significant overlap in their genomic localization. Next, to know whether the two TFs physically interact, a co-immunoprecipitation experiment was performed. While JUN immunoprecipitated with an anti-IKZF1 antibody, curiously IKZF1 did not immunoprecipitate with an anti-JUN antibody. Finally, EMSA and luciferase experiments were performed to show that the two TFs bind cooperatively at an IL20 upstream probe.

Major strengths:

1. SPICE was able to recapitulate previously known composite elements, such as the AP-1/IRF4 composite elements (AICE).

2. Under LPS and IL-21 treatment, JUN and IKZF1 in B cells have significant overlap in their genomic localization. This is very good supporting evidence for the efficacy of SPICE in detecting TF partners.

Major weaknesses:

1. The authors fail to convincingly show that IKZF1 and Jun physically interact. A quantitative measurement of their interaction strength would have been ideal.

2. The super-shift experiment to show that the proteins bound to their EMSA probe were indeed IKZF1 and JUN are not very convincing and would benefit from efforts to quantify the shift (Figure 3E). Nuclear extracts from cells with single or double CRISPR knock outs of the two TFs would have been ideal.

3. There is a second band beneath the more prominent band in the EMSA experiment with recombinant IKZF1 and JUN (Figure 4C). This second band is most probably bound by IKZF1 because it becomes weaker when the IKZF1 site is mutated and is completely absent when only JUN is added. This is completely ignored by the authors. Therefore, experiments with EMSA fail to convincingly show that IKZF1 and Jun bind cooperatively. They could just as well bind independently to the two sites.
