# Peer review - Round 1

Editors:
- Arup K Chakraborty, Massachusetts Institute of Technology , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.10785.024](https://doi.org/10.7554/eLife.10785.024)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Simple biophysical model explains the conformational transitions of the unfolded proteins of the Nuclear Pore Complex" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and John Kuriyan as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

This paper develops a self-consistent-field theory for a model of transport through nuclear pores. The model is properly formulated based on well-established and long-standing concepts in polymer physics. Though several theoretical models have been previously published attempting to describe the biophysical nature of nuclear transport, the model presented here has the considerable attraction that it is less inclined than these other models to try to pitch a particular mechanism – rather, it sets up a computational framework that can be adapted and added to upon additional data, giving researchers a computational framework for a more rigorous analysis of data. To demonstrate the effectiveness of the model, it is used to perform a new set of analyses of previously published work from two of the co-authors, Kapinos and Lim. The model re-capitulates certain previously puzzling behaviors seen for FG nups and provides a biophysical hypothesis for these behaviors. This model could therefore be a valuable new tool. However, our enthusiasm for the paper is considerably diluted by two issues.

Firstly, the manuscript oversells itself as having resolved the controversies, and furthermore, the comparisons with experiment are qualitative. Qualitative comparisons are fine, but rephrasing some of the text so that it accurately reflects the accomplishments is essential.

Secondly, and more importantly, to establish itself as a useful computational platform, additional work is necessary. In the paper, the model is fit to existing data from some of the co-authors. To make a compelling case that the model indeed captures the essential features of nuclear pore transport, it is necessary to show that the model is predictive – that is, take published data from several groups (not the co-authors') that was explicitly not included in building the model, and without re-adjusting the parameters used to fit the authors' data, show that the model describes these additional data. Without demonstrating this capability, the model cannot be considered predictive or explanatory. We suggest that you consider describing the data presented in the following references: 1) Strawn et al., 2004: can the model describe the observation here that so much of the FG mass can be deleted without completely disrupting transport? 2) Yamada et al.: can the model explain why might there are two classes of cohesiveness as suggested in this paper? 3) Popken et al., 2015: Compare the coarse grained simulations and data in this paper with those described in the manuscript. 4) Patel et al., 2007: which also contains interesting data. Of course, you could choose other data sets that you believe are illustrative.

Some additional detailed points that need to be addressed are listed below.

1) The model completely ignores sequence information and electrostatic interactions. The problem with this is that there is clear evidence from bioinformatics studies (see ref. 68) and theory (see ref. 50) that clearly show the need to consider the role of electrostatics. These studies seem to consider similar screening conditions as that in the present manuscript. Moreover, ref. 50 (a theoretical study) shows that smearing the sequence leads to qualitatively different behavior. Therefore, these points need to be mentioned explicitly as refs. 68 and 50 suggest that it may be difficult to describe the NPC using minimal models adequately, as is claimed in the last sentence of the manuscript.

2) If the minimal model provides an excellent description of nuclear pores, why can synthetic systems not recapitulate the behavior of nuclear pores? The manuscript should emphasize that the model describes some universal features, and more details will have to be added upon considering additional data – this point might become more vivid or refuted by addressing the second major point made above.

3) Figure 2 presents well known results, as is noted in the manuscript, but the original work of Alexander is not cited. Also use of the term "cross-link" here is misleading since this is just a model van der Waals interaction.

4) Figure 3 shows the two limits that a brush can have from maximal repulsion (stretching) to completely compact. The fact that the experimental observations fall between these two asymptotic limits is expected. But, why is the same nup at different grafting densities suggesting very different values of χ?

5) It appears that the model assumes macroscopic uniform planar layers grafted with one type of FG repeat. Does the model also make accurate predictions for geometries that more accurately resemble the NPC i.e. nanoscopic pores, or mixtures of different FG repeat types?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Simple biophysics underpins collective conformations of intrinsically disordered proteins of the Nuclear Pore Complex" for further consideration at eLife. Your revised article has been favorably evaluated by John Kuriyan as Senior editor, a Reviewing editor, and one reviewer. The revised manuscript is much improved, and most of the points we raised previously have been fully addressed. If the remaining points detailed below can be addressed, we think that there is a very good chance that the paper will be accepted for publication.

1) In the Abstract, we still feel "These results reconcile some of the outstanding controversies…" is strong, given that this work does not concretely reconcile, but rather suggest solutions, to the current controversies. Perhaps "These results address some of the outstanding controversies…" would be better.

2) In the Discussion, the sentence "The suggests how the ‘brush’ and… effects" is grammatically incorrect and unclear – can you please re-write?

3) On use of data by others: You addressed our comments by including a work that focuses only on Nup98, which represents only one type of FG, one that can form gels in vitro, but are not necessarily representative of others. Even if an experiment is not possible, could you still replicate computational findings by others, if not at a quantitative, at a qualitative level? In the absence of an independent test, again, we would recommend a more cautious approach on claims that the current work resolves different findings. Instead, perhaps emphasize rather that this work presents a tool of utility to future studies.

4) On the omitting of some aspects of FGs, etc.: A) Sequence: the explanation about the randomized AA sequence is much improved. However, it would be nice to have a demonstration of the thesis in a case with a simple heterogeneity in sequence, such as in Nsp1 (i.e. difference in property in N-terminal and C-terminal regions). Such a demonstration would also reinforce the paper by possibly recapitulating the computational finding in Yamada et al. (difference in expected structure on N and C-termini). B) On the geometry of FG grafts: Although further computational investigation of this topic may be beyond the scope of this paper, it is worth discussing the limitations of the current presentation of the simple monolayer geometry and the possible differences/changes in FG behavior/conformation (and/or lack thereof) that could arise from change in geometry (e.g. grafting them in a pore lumen, etc.).

5) In the Abstract, there is a sentence: "NPC transport relies on the conformational transitions of assembly…". It is true that the conformation is known to change in in vitro experimental setups, but is there any evidence in NPC-context that supports this statement (i.e. conformational transitions)?

6) Figure 1 is rather crudely rendered, and does not accurately represent the positions of the FG nups indicated. Krull et al., 2004 can be used for Nups98 and 153, while recent crystallographic work (Chug et al., 2015) indicates the position of Nup62 to be symmetric and immediately adjacent to Nup93 (Krull et al., 2004). Also, the lower two panels as they stand don't really help readers understand what you call the "experimental situation." This figure should be polished further.

7) For Figure 2, it can be guessed from the context that different curves correspond to different χs, but it's better to specify which curve correspond to what value (or add some direction like an arrow with "increasing χ," etc.)

8) For Figure 3, please consider omitting "experimental evidence of cohesiveness" from the figure title. Strictly speaking, it should go something like "polymer model based on cohesion theory fits well with the data" and it's not really evidence for cohesiveness.
