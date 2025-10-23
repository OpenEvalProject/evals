# Peer review - Round 1

Editors:
- Jeffrey Settleman, Calico Life Sciences United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.29702.032](https://doi.org/10.7554/eLife.29702.032)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "CD95L derived si- and shRNAs and the CD95L mRNA kill cancer cells through an RNAi mechanism by targeting survival genes" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Charles Sawyers as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: John G Doench (Reviewer #1); Gregory J Hannon (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Previously, the authors conducted a study that described DICE ("Death induced by CD95R/L elimination"), in which they show that depletion of these genes by RNAi results in cell death across a dozen cancer cell lines (Hadji et al., 2014). Here, they follow-up on this observation by fine-mapping the cause of DICE and show that the viability effect triggered by these RNAi reagents is actually not dependent on the target genes, but rather on a seed-based (i.e. microRNA-like) off-target effect of the RNAi reagents, leading to a new acronym, DISE (death induced by survival gene elimination).

Essential revisions:

1) The consensus view among reviewers is that the emphasis in the manuscript is misplaced. It is largely about off-target effects of RNAi reagents, and has little to do with CD95 or CD95L. If the conclusion of this manuscript is that some seeds are more likely to have viability effects than others, then the focus should be on that conclusion. As written, the manuscript is very CD95-centric, which implies that there is something special about this gene.

2) Since this manuscript is really about generic off-target effects, then there are additional resources that could be used to better analyze this phenomenon. For example, the TRC library has been screened against hundreds of cell lines and those data are available (Cowley et al., Sci. Data, 2014), and it would be important to thoroughly analyze those data to see if these observations here generalize well.

3) Additionally, as mentioned in the last paragraph of the subsection “DISE is caused by loading of the guide strand of toxic si/shRNAs into the RISC”, the inactivity of miR-30 backbone shRNAs to produce this response deserves much more treatment than a "data not shown." If the off-target effects arise because of something specific to the TRC shRNAs used, that mechanism needs to be characterized. If it is purely an expression-level difference, that needs to be documented. One potential experimental approach could use transient transfection of siRNAs – which can be used at different doses, or with pools of siRNAs to represent the different Dicer products of TRC shRNAs.

4) The authors produced 3 different target deletions (ΔsiL3, ΔshL3 and ΔshR6) in 293T or HeyA8 cells to show that expression of the si or shRNAs, even in the absence of the target, is still lethal. The deletions seem to produce frame-shift mutations in the coding sequence (as the nt deleted are not a multiple of 3). The authors indeed show that ΔshR6 produces a protein knockout, which they use for a different experiment (Figure 1—figure supplement 3). This provokes the question of whether this is also the case for ΔsiL3 and ΔshL3 and whether it is appropriate to call them "target site" mutants if they are indeed functional knockouts. The authors state in their Introduction "after deleting the CD95 gene tumors barely grew in vivo (Chen et al., 2010; Hadji et al., 2014)" so maybe they could comment on the fact that HeyA8 ΔshR6, being a functional knockout and not exclusively a target site mutant grows similar to the parental cell line (Figure 1H).

5) In Figure 6 enforced expression of the CD95L mRNA is toxic in HeyA8 cells. However, in Figure 1—figure supplement 2, the CD95L-WT ORF is expressed (together with a scramble shRNA) and there is no observable increase in% subG1 compared to expression of vector only (together with a scramble shRNA) in either NB7 cells (panel D) or MCF-7 (panel G). Could the authors please comment on whether there are any other variables we should take into account or whether this is a cell type-specific phenotype. It is difficult to understand that NB7 lack caspase-8 but if they show the toxicity phenotype upon expression of the si/shRNAs and if over-expression of the CD95L is mediating the same phenotype, the model would predict CD95L would still cause lethality of this cell line.

6) The authors perform a pooled screen to identify the most toxic sequences in the CD95 and CD95L genes (Figure 5). The pool screen analysis is performed comparing the final time points to the plasmid pool. This is concerning as virus production and infection could also lead to biases in the shRNA representation. As it stands, it could very well be that many of the "depleted" shRNAs were never present in the cells to begin with. This leads to particular concern about the results in the absence of doxycycline. The authors state that the depletion observed without adding dox is most likely due to leakiness in the Tet-on system (subsection “Identification of toxic shRNAs in the CD95L and CD95 mRNAs”, second paragraph). However, in their initial experiments (Figure 1G) they expressed the highly toxic shRNA shL3 in 293T without any evidence of toxicity for at least 4 days. Thus, it would be very important to show the depletions observed in this pooled screen are indeed biological. Since the authors do not seem to have an initial post-infection time point to compare to, they could produce virus following the same set up and show that plasmid representation roughly corresponds to the shRNAs cloned from cells right after infection.

7) Regarding the analysis of AGO-bound small RNAs that align to the CD95L, does the analysis take into account the possibility of PCR duplicates? Also, strand information is essential if the model is that this CD95L derived small RNAs are mediating knockdown of survival genes. The analysis text does not specify whether BLAST was run with any strand specificity so it would be essential for the authors to clarify.
