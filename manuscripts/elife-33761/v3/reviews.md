# Peer review - Round 1

Editors:
- Bernard de Massy, Institute of Human Genetics, CNRS UPR 1142 France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.33761.031](https://doi.org/10.7554/eLife.33761.031)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: this article was originally rejected after discussions between the reviewers, but the authors were invited to resubmit after an appeal against the decision.]

Thank you for submitting your work entitled "Covalent linkage of the DNA repair template to the CRISPR/Cas9 complex enhances homology-directed repair" for consideration by eLife. Your article has been evaluated by a Senior Editor and three reviewers, one of whom is a member of our Board of Reviewing Editors. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

The paper by Savic et al., "Covalent linkage of the DNA repair template to the CRISPR/Cas9 complex enhances homology directed repair" reports a novel approach to improve the efficiency of HR relative to NHEJ upon Cas9 induced DSB. The strategy relies on the assumption that enhancing the spatial proximity or local concentration of DNA used as template for HR would increase the use of this pathway. This is achieved by generating covalently coupled Cas9-oligonucleotide. An increased efficiency of HR is observed which could be interesting for some applications if confirmed.

However all reviewers have identified several problems in the manuscript that could only be solved pending designing a whole new set of experiments. This additional work extends beyond a revision and the manuscript cannot therefore be accepted for publication in eLife.

The major issues raised by the reviewers are:

- The effect observed with the coupled substrate does not demonstrate that it is due to bringing the oligonucleotide in proximity to the DSB.

- The effect observed should be validated on several genomic target sites, first to extend the observation to a genomic site and second to show the reproducibility of the effect on different targets.

- The assay used does not allow distinguishing the NHEJ and HR pathways as claimed by the authors.

Reviewer #1:

This paper reports a novel approach to improve the efficiency of HR relative to NHEJ upon Cas9 induced DSB. The strategy relies on the assumption that enhancing the spatial proximity or local concentration of DNA used as template for HR would increase the use of this pathway. This is achieved by generating covalently coupled Cas9-oligonucleotide. The increased efficiency of HR observed could be interesting for some applications.

The experiments are well designed and presented. However several aspects require clarifications as indicated below. Although the increased efficiency of HR is convincing the interpretation is open to several alternatives (i.e. proximity of oligo or stability of oligo). Two additional experiments could clarify this important point.

1) Figure 2A. The figure should be understandable with help of the legend and several pieces of information are missing:

What is 2A ? What is c.190_191delinsCT? (Use a more generic term; specific construct name can be provided in Materials and methods).

I assume the “X” labels the mutation and/or the Cas9 DSB?

I assume the mutant RFP is a substitution?

One needs to see exactly where the substitution is, where the guide maps and where the DSB is introduced and whether the guide would still be able to induce Cas9 cleavage after HR (is the PAM mutated?). One reason is that depending on where the DSB is, more or less end processing will be needed for HR.

2) Figure 2B lower panel (IF): indicate the channels used. Most of the cells seem to be GFP negative in the central panel. How could this be as the FACS indicate 16%? Single channels and overlays should be provided.

What is the percentage of GFP positive among the RFP positive cells? (Close to 100% expected).

It should be noted that the% of edited cells is underestimated since in frame indels (one third ?) can generate a GFP positive cell.

3) Figure 3A. Explain the lane no BG coupling?

4) Figure 4. The same data should not be plotted twice in panel B and C: Panel C should be removed (same comment for Figure 4F and G).

The main question about the use of SadCas9 is to determine whether the difference with SpCas9 is statistically significant. The tests should be performed (Figure 4E, between RNPD coup and RNP-RNPD coup) and if not significant the conclusions should be revised.

A map showing the positions of the different SadCas9 guides used (1 to 4) should be shown.

5) Two experiments are required to describe the effect observed: In order to know if the effect observed is due to coupling the oligo to Cas9, a control should be performed with the oligo coupled to BG but not to Cas9. Clearly at least part of the effect observed could be due to stabilization of the oligo rather than proximity to DSB per say. To distinguish these possibilities the authors should test an oligo coupled to SadCas9 but without the corresponding guide.

I assume S. aureus was used such as to design a distinct guide specific for S. aureus and not bound by S. pyogenes, if so, this should be explained in the text.

6) Figure 4—figure supplement 1.

What is the interpretation for the decrease of percentage of edited cells with oligo coupled to SadCas9 ? (Figure 4—figure supplement 1D).

Legend of Figure 4—figure supplement 1C and D: RNP-RNP unco is grey but should be hatched grey box.

7) Two-tailed tests should be used not one-tailed since there is no reason to assume a priori that the coupled protein would be more efficient.

8) Subsection “Expression and purification of Cas9-SNAP”, missing word: "The was further purified…"

Reviewer #2:

The authors show that covalent linkage of the DNA repair template to the CRISPR/Cas9 complex enhances HDR efficiency. They conclude this based on the use of a traffic light HDR reporter system, transiently transfected into HEK293 cells.

Although this is interesting and aspects of the study are really clever (e.g. the use of the sa-dCAS9 linked template to prove that physical proximity is the key), the work strikes me as quite preliminary as the increases are only shown in this transient reporter system using only one target site.

Without more thorough testing of the improvement in a real experimental system, I can't recommend acceptance of this study in its current form at eLife. My recommendations to improve the impact of this publication would be to demonstrate real efficiency improvements using a targeted edit within a genomic target site. In this respect, the existing work using transient reporter system would be excellent preliminary data for a real proof-of-concept – namely the increased efficiency in a real experimental genome engineering project e.g. to create a point mutation.

In addition, the CRISPR field has been populated by numerous claims showing positive perturbations to shift the balance of repair pathway from NHEJ to HDR (alterations in experimental design, NHEJ inhibitors, etc.). Frequently these claims have been made on the basis of data from manipulation of a single target site. Reproducibility of these studies has proven to be low, as when applied by other labs at different target sites, the reported improvements are frequently not replicated. To avoid this occurring, I would recommend that the authors address several different genomic target sites and report the level of improvement in HDR seen in these various experimental settings.

Figure 4E presents data which suggests that the positioning of the sgRNA (and hence the DSB) away from the target nucleotide to be mutated (0 bp, 52 bp, 61 bp, 83 bp and 128bp) has little influence on the correction efficiency. This is significantly at odds with experimental data from genomic target sites, and should be discussed. In addition, I wonder whether this is a curious artefact of using transient plasmids and thus provides support for my recommendation of addressing a single copy genomic target site or sites to validate their approach in a real experimental setting.

The work is very similar to a recent bioRxiv report by Janet Rossant's group (https://doi.org/10.1101/204339) who demonstrated that covalent attachment of the repair template to the CRISPR/Cas9 complex enhanced HDR rates, reporting data from fluorescent cassette insertions at 5 genomic target sites. Although this paper hasn't been peer reviewed, it's tempting to speculate that the authors of this manuscript have submitted what is essentially a preliminary study to eLife to compete with this more thorough study, which is presumably in review at another journal.

Reviewer #3:

Gene targeting constitutes a promising approach for the generation of novel biological models and for future gene therapy strategies. The capacity to generate targeted cleavage by the CRISPR-CAS9 system raised many hopes. However, targeted gene replacement still remains to too low levels. In the present work the authors design a strategy aiming at delivering the correcting DNA in the vicinity of the cleaved site. They covalently bound the correction oligonucleotide to the CAS9 itself via "click chemistry", using the SNAP-tag technology. Then they assemble in vitro the complex with the RNA-guide and transfected cells (HEK293). This strategy is elegant and promising. However, many concerns should be addressed.

The main problem is the fact that the authors used only on system to monitor HR; and that the designing of this substrate is based on wrong considerations on HR and NHEJ.

It is claimed that NHEJ is error-prone. This is wrong. There are two kinds of end-joining processes, the canonical NHEJ (which is not error-prone, but conservative) and the Alternative end-joining (alt-NHEJ, MMEJ, B-NHEJ), which is mutagenic and error-prone. Therefore mutagenic repair does not automatically imply NHEJ. Second it is said in the Introduction that HR and NHEJ directly compete. This is also wrong; in fact things happen in two phases: first competition between cNHEJ and single-strand DNA resection, second on resected DNA extremities, competition between HR and alternative end-joining. Finally, HR can also generate mutagenesis. Therefore many concerns exist on the strategy used here (which is the sole assay used) because mutagenic repair can arise by many other processes than NHEJ.

Moreover, is correction with oligonucleotides (65, 81 b) an actual HR mechanism? This is not consistent with concept of MEPS.

The authors should first genetically validate their reporter system, in cells mutated for HR or NHEJ.

The authors should also verify their strategy with natural endogenous target sequences, instead of the reporter.

There are no data on the transfection efficiency. Especially, comparing the CAS9 with the engineered one.

Similarly, does the two CAS9 cleave with similar efficiency?

Does the modification of the CAS9 affect its cleavage specificity?

Are there any off-target effects? (off-target cleavage, off-target integration of the oligo).

The authors should test different RNA guides for a common target.

The author should test different cell lines.

It is not clear what is actually measured. Where are the mutagenic repair (pseudo-NHEJ) measurements? Is it the frequency of HDR or the ratio HDR/pseudo-NHEJ?

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "Covalent linkage of the DNA repair template to the CRISPR-Cas9 nuclease enhances homology-directed repair" for further consideration at eLife. Your revised article has been favorably evaluated by Diethard Tautz (Senior Editor) and the Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

The authors provide convincing answers to all reviewers' comments. Importantly, the authors show that the main improvement achieved by their experimental approach is due to enhanced targeting of the oligonucleotides to the nucleus rather that its targeting to the specific target genomic site. This could also be highlighted in the Abstract.

A few points need to be clarified:

1) Source data 6 refers to Figure 4—figure supplement 2 (not 3?) should be registered as Figure 4—source data 3.

2) Source data 5 refers to Figure 4—figure supplement 1 (not 2?) should be registered as Figure 4—source data 2.

3) Figure 2B requires clarification (and in the legend as well). Legend says "the mutation substitutes… CT.. to TA". This is ambiguous because TA is wild type. It would clarify to draw in Figure 2, the wild type and mutated genomic sequences (with the codon substitution) and the sequence of the guide (also can be confusing as drawn because the guide has CT not TA).

4) Figure 5: In Figure 5, only the reference is shown. Mutated variant should be indicated. For instance, on 5A, at HBB, the DNA sequence shown should be the one after correction (to be consistent with Figure.2B) ? However it is identical to guide sequence?

Please explain the correction efficiency values, obtained after correction for transfection efficiency? If so, provide transfection efficiencies, otherwise read data from Supplementary file 2 cannot be understood: i.e. 27% at Rosa 26, how was this obtained? In addition, since no HR reads is detected at Rosa26 (why is this?), the authors should comment in the main text on the difference uncoupled/coupled from Figure 5B for this locus.

5) Figure 6A requires clarifications both in the main text and in the presentation of the figure. The authors summarize in one sentence all the NGS data (Results and Discussion, eighth paragraph). There is a lot of data in this analysis and it would be better to present the analysis step by step and not to refer to all panels 6A, B, D, E, F at once. Reporter locus could be presented first, with comments about percentage of corrected reads and other events (legend should explain the nomenclature, for instance -7:7D, and also what are I, II and III: triplicates I assume). Then results at other loci should be briefly discussed (and referred to Supplementary file 2). Also indicate in Supplementary file 2 that the variants called "SNV" are the ones predicted after repair by HR. An interesting information is also the relative proportion of HR versus non HR events. In Figure 6, it seems that this proportion is about 30% in experiment I (5.63/(100-85.19)). Is this correct? It could be discussed in the main text.
