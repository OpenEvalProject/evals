# Peer review - Round 1

Editors:
- Apurva Sarin, Institute for Stem Cell Science and Regenerative Medicine India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.91422.3.sa0](https://doi.org/10.7554/eLife.91422.3.sa0)

This valuable study significantly enhances our understanding of how various ligands and receptors interact within the Notch signaling pathway. By developing novel cell-based assay systems, the authors systematically analyzed the effects of different ligand-receptor combinations on pathway activation. The convincing data reveal intriguing and unexpected differences and provide a foundation for interpreting Notch signalling in both normal and disease-related contexts.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91422.3.sa1](https://doi.org/10.7554/eLife.91422.3.sa1)

Summary:

The Notch signaling pathway plays important roles in many developmental and disease processes. Although well-studied there remain many puzzling aspects. One is the fact that as well as activating the receptor through a trans-activation, the transmembrane ligands can interact with receptors present in the same cell. These cis-interactions are usually inhibitory, but in some cases, as in the assays used here, they may also be activating. With a total of 6 ligands and 4 receptor there are potentially a wide array of possible outcomes when different combinations are co-expressed in vivo. Here the authors set out to make a systematic analysis of the qualitative and quantitative differences in the signaling output from different receptor ligand combinations, generating sets of "signaling" (ligand expressing) and "receiving" (receptor +/- ligand expressing cells).

The readout of pathway activity is transcriptional, relying on the fusion of GAL4 in the intracellular part of the receptor. Positive ligand interactions result in proteolytic release of Gal4 that turns on expression of H2B-citrine. As an indicator of ligand and receptor expression levels, they are linked via TA to H2B mCherry and H2B mTurq expression respectively. The authors also manipulate expression of the glycosyltransferase Lunatic-Fringe (LFng) that modifies the EGF repeats in the extracellular domains impacting on their interactions. The testing of multiple ligand receptor combinations at varying expression levels is a tour de force, with over 50 stable cell lines generated, and yields valuable insights although as a whole, the results are quite complex.

Strengths:

Taking a reductionist approach to test systematically differences in the signaling strength, binding strength and cis-interactions from the different ligands in the context of the Notch1 and Notch 2 receptors (they justify well they choice of players to test via this approach) produces a baseline understanding of the different properties and leads to some unexpected and interesting findings. Notably:

- Jag1 ligand expressing cells failed to activate Notch1 receptor although were capable of activating Notch2. Conversely, Jag2 cells elicited the strongest activation of both receptors. The results with Jag1 are surprising also because it exhibits some of the strongest binding to plate bound ligands. The failure to activate Notch1 has major functional significance and it will be important in future to understanding the mechanistic basis.

- Jagged ligands have the strongest ciis-inhibitory effects and the receptors differ in their sensitivity to cis-inhibition by Dll ligands. These observations are in keeping with earlier in vivo and cell culture studies. More referencing of those would better place the work in context but it nicely supports and extends previous studies that were conducted in different ways.

- Responses to most trans-activating ligands showed a degree of ultrasensitivity but this was not the case for cis-interactions where effects were more linear. This has implications for the way the two mechanisms operate and for how the signaling levels will be impacted by ligand expression levels.

- Qualitatively similar results are obtained in a second cell line, suggesting they reflect fundamental properties of the ligands/receptors.

Weaknesses:

One weakness is that the methods used to quantify the expression of ligands and receptors rely on co-translation of tagged nuclear H2B proteins. These may not accurately capture surface levels/correctly modified transmembrane proteins. In general, the multiple conditions tested partly compensate for the concerns - for example as Jag1 cells do activate Notch2 even if they do not activate Notch1 some Jag1 must be getting to the surface. But even with Notch2, Jag1 activities are on the lower side, making it important to clarify, especially given the different outcomes with the plated ligands. Similarly, is the fact that all ligands "signalled strongest to Notch2" an inherent property or due to differences in surface levels Notch 2 compared to Notch1?.. The results would be considerably strengthened by calibration of the ligand/receptor levels (and ideally their sub-cellular localizations). Assessing the membrane protein levels would be relatively straightforward to perform on som eof the basic conditions because their ligand constructs contain Flag tags, making it plausible to relate surface protein to H2B, and there are antibodies available for Notch1 and Notch2

In the revised version this has been addressed to some extent. A figure showing the relationship between co-translated mTurquiose and surface receptor expression for some clones (Figure 1-figure supplement 1B) goes some way to address the concerns that differences in Notch1 and Notch 2 could be due to the receptor levels. The data analyzing surface ligand levels is more equivocal, (a Western blot for biotinylated surface proteins), as the levels detected vary substantially between Dll1 and Dll4 (the latter barely detectable). But as a signal for surface expression of Jag1 was obtained this rules-out one concern that this ligand was failing to reach the surface. A discussion of the caveats of the approach is warranted, to make clear the limitations.

Cis-activation as a mode of signaling has only emerged from these synthetic cell culture assays raising questions about its physiological relevance. Cis-activation is only seen at the higher ligand (Dll1, Dll4) levels, how physiological are the expression levels of the ligands/receptors in these assays? Is it likely that this would make a major contribution in vivo? Is it possible that the cells convert themselves into "signaling" and "receiving" sub-populations within the culture by post-translational mechanism. Again some analysis of the ligand/receptors in the cultures would be a valuable addition to show whether or not there are major heterogeneities.

It is hard to appreciate how much cell to cell variability in the "output" there is. For example, low "outputs" could arise from fewer cells becoming activated or from all cells being activated less. As presented, only the latter is considered. That maybe already evident in their data, but not easy for the reader to distinguish from the way they are presented. For example, in many of the graphs, data have been processed through multiple steps of normalization. Some discussion/consideration this point is needed.

Impact:

Overall, cataloguing of the outcomes from the different ligand-receptor combinations, both in cis and trans, yields a valuable baseline for those investigating their functional roles in different contexts. There is still a long way to go before it will be possible to make a predictive model for outcomes based on expression levels, but this work gives an idea about the landscape and the complexities. This is especially important now that signaling relationships are frequently hypothesised based on single cell transcriptomic data. The results presented here demonstrate that the relationships are not straightforward when multiple players are involved.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91422.3.sa2](https://doi.org/10.7554/eLife.91422.3.sa2)

Summary:

In this manuscript the authors extend their previous studies on trans-activation, cis-inhibition (PMID: 25255098) and cis-activation (PMID: 30628888) of the Notch pathway. Here they create a large number of cell lines using CHO-K1 and C2C12 cells expressing either Notch1-Gal4 or Notch2-Gal4 receptors which express a fluorescent protein upon receptor activation (receiver cells). For cis-inhibition and cis-activation assays, these cells were engineered to express one of the four canonical Notch ligands (Dll1, Dll4, Jag1, Jag2) under tetracycline control. Some of the receiver cells were also transfected with a Lunatic fringe (Lfng) plasmid to produce cells with a range of Lfng expression levels. Sender cells expressing all of the canonical ligands were also produced. Cells were mixed in a variety of co-culture assays to highlight trans-activation, cis-activation, and cis-inhibition. All four ligands were able to trans-activate Notch1 and Notch 2, although Jag1 transactivated Notch1 weakly. Lfng enhanced trans-activation of both Notch receptors by Dll1 and Dll4, and inhibited both receptors by Jag 1 and Jag2. Cis-expression of all four ligands were predominantly inhibitory, but Dll1 and Dll4 showed strong cis-activation of Notch2. Interestingly, cis-ligands preferentially inhibited trans-activation by the same ligand, with varying effects on other trans-ligands.

Strengths:

This represents the most comprehensive and rigorous analysis of the effects of canonical ligands on cis- and trans-activation, and cis-inhibition, of Notch1 and Notch2 in the presence or absence of Lfng so far. Studying cis-inhibition and cis-activation is difficult in vivo due to the presence of multiple Notch ligands and receptors (and Fringes) that often occur in single cells. The methods described here are a step towards generating cells expressing more complex arrays of ligands, receptors and Fringes to better mimic in vivo effects on Notch function.

In addition, the fact that their transactivation results with most ligands on Notch1 and 2 in the presence or absence of Lfng were largely consistent with previous publications provides confidence that the author's assays are working properly.

Weaknesses:

In the original version, there was a major concern about quantifying the amount of Notch receptors and ligands on the cell surface (especially Jag1) based on total fluorescence. The authors have added data to demonstrate that most of the receptors and ligands are on the cell surface, allaying most of these concerns.
