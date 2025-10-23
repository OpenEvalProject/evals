# Peer review - Round 1

Reviewers:
- Olga Boudker, Weill Cornell Medical College , United States

## Review text

DOI: [10.7554/eLife.19088.018](https://doi.org/10.7554/eLife.19088.018)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Cellular encoding of Cy dyes for single-molecule imaging" for consideration by eLife. Your article has been favorably evaluated by Richard Aldrich (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In the manuscript, Ahern and colleagues describe genetic encoding of cyanine dyes as non-canonical amino acids. Such encoding provides orthogonal fluorescent labeling of any protein in a living cell. The method, presented in considerable detail, is discussed in the context of performing single molecule fluorescence studies with particular emphasis on single-molecule FRET of membrane proteins. This first demonstration of incorporation of cyanine dyes as ncAAs in eukaryotic expression systems is significant because these dyes are some of the best single-molecule analysis of protein dynamics and should considerably improve the analysis of stoichiometry in protein complexes. The present study is of a broad and potentially general interest to diverse scientists. The manuscript is well organized, appropriately referenced and well written. All three reviewers were positive regarding potential publication of the manuscript, but raised a considerable number of concerns that should be addressed by the authors. These are largely focused on the lack of clarity in the manuscript as to how applicable the method is to possible practical questions and what are reservations and limitations.

Essential revisions:

In particular, an apparently confusing aspect of work is that the efficiency of tRNA acylation and the efficiency of the downstream events (including labeled amino acid incorporation into proteins and biological activity of the labeled proteins) were not separated. For example, Figure 2B (and 2C) would appear to suggest that there are significant differences in channel activity depending on the dye used. However, the point of these panels is that the extent of channel activity observed correlates with the extent to which the tRNA underwent successful ligation in vitro prior to its injection. Why weren't the full-length tRNAs purified prior to injection to control for this variable? Published protocols are available from a number of groups including (Blanchard et al. PNAS 2004). The reviewers feel that it is important to address this question and suggest that at the very least the experiment shown in Figure 1B is redone with acylated tRNA purification prior to cell-free translation to establish the efficiency with which labeled amino acids (compared to unlabeled) are incorporated into proteins. The results shown in other figures (particularly Figure 2) should then be explicitly discussed in terms of which processes contribute to the observed differences.

Additional comments (some of which may be related to the above mentioned issue) are compiled below.

Reviewer 1:

First, it seems that incorporation efficiency drops with the size of the dye, such that Cy5-FA and Cy3-based LD550-FA are incorporated with lower efficiency than Cy3-FA. For example, Figure 1B shows that in 2 out of 3 experiments little protein was made with incorporation of Cy5-FA. What kind of levels of incorporation would make the approach practical? If one wanted to conduct FRET experiments, what levels would be sufficient?

Second, it is unclear what fraction of the label remains fluorescent at the end of the biosynthetic process in an oocyte. This question should be directly investigated, particularly since the presented data suggest that the fraction is significantly less than 1. For example, in Figure 4, half of CLC0 dimers photo-bleach in a single step. Considering that the total number of observed particles is significantly higher than in the mock experiments, the observation suggests that a fraction of the dye molecules in the dimers are no longer fluorescent. Alternatively, it is possible that a significant fraction of CLC0 proteins are not properly assembled into dimers. Either of these possibilities would compromise experimental design. Similarly, only a small fraction of Cy5 labeled proteins in Figure 3A co-localized with Cy3 label. Since Cy3-FA is incorporated with higher efficiency, one would expect that most of CLC0 dimers would contain either 2 Cy3-s or Cy3/Cy5. However, Cy5-only particles seem to dominate in Figure 3A, right panel.

Finally, I was confused about molecules that photo-bleach in more than 2 steps. Are they higher-order assemblies? What fraction of total molecules do they constitute? In other words, if we did not know that CLC0 were a dimer, could we determine its stoichiometry from these experiments? If not, what are the main challenges that need to be resolved to make this method applicable in straightforward way?

Reviewer 2:

The authors should address several questions about the approach and results to help the reader to understand how well it may work for various membrane proteins.

1) Why is Cy3 fluorescence so much thinner a ring at the outer end of the fatter GFP ring in Figure 1C?

2) How effective is the suppression compared to expression of the normal (wildtype) protein? E.g. in the case of ClC, as shown in Figure 2, how much current is generated if wildtype cRNA is injected in the same quantity? It is also not very clear how much the expression level was reduced (especially for the Na channel and the cell-free system), which makes it difficult to evaluate how useful this method can be on other poorly expressed channels. Authors should discuss factors that may contribute to lower expression levels in the most optimal case of suppression (e.g. with Phe). The manuscript did not address the relationship between the incorporation efficiency and the amount CyX-tRNA used. What are the concentrations that lead to maximum suppression of nonsense mutation? How does the incorporation efficiency change with different concentrations of cRNA and/or CyX-tRNA?

3) The cold ligation temperature does not seem to be suitable for cells. Will the increased susceptibility to hydrolysis be a problem even after the CyX-tRNA is injected (e.g. when the oocytes are incubated at 16°C)?

4) While injecting nonacylated tRNA with CLC-0 E166TAG is said to yield no functional channels, the reversal potential of CLC-0 E166TAG with no AA is still at -30mV. Is it possible that there was some expression? Additionally, it is surprising that having a bulky dye in the middle of the open pore did not generate any blocking effect, while it is shown in the literature that many E166 mutants of CLC-0 (E166 mutants) can be blocked by fatty acids and amphilic blockers much more easily than the WT. Can the authors provide more evidence to show that it is indeed Cl- current carried by CLC-0 E166TAG incorporated with CyX? Does the property of the pore change in comparison to the Phe incorporation alone (such as blocker affinity)?

5) To estimate random colocalization the authors rotate the image by 90 degrees. Could they also use the spatial resolution of their microscope and a calculation of chance overlap at the experimental densities to obtain a second estimate?

6) In Figure 3A Cy3 spots vary greatly in brightness. A) Does this mean that the dim ones are single channels and bright ones are clusters? B) Is this the highest density obtainable (would higher expression mean a bigger difference between encoded and mock)?

7) In Figure 4 some mock spots have 2 bleaching steps. Is this compatible with explanation for what mock may be (e.g. tRNAs, etc.)?

8) In Figure 4 the encoded spots include ones with more than 2 bleaching steps that are attributed to ClC clusters. Is there any patch clamp data or other data that supports clustering of channels? Bar graphs only show up to 2 steps: what is the relative frequency of higher step spots?

9) One prediction for co-incorporation of Cy3 and Cy5 is that the dimmest spots with single Cy3 bleach steps should have only a single Cy5 bleach step. Is this the case? Alternatively, if only Cy3 were incorporated, the dimmest spots should have 2 steps and there should be no single steps. It would be good to show if one or both of these expectations is satisfied.

10) Any speculation on the effects of Cy-tRNA labeling on the native TAG codon of other channels? Will that be an issue when using this technique for single molecule imaging/subunit counting?

Reviewer 3:

1) It is difficult to discern from the data in Figure 1C whether the extent of Cy3 and Cy5 labeling is quantitative, which one would presume to be the case. While stoichiometric labeling with Cy5 seems to have occurred based on the image shown, this does not appear to be the case for Cy3. Was the image chosen scaled differently?

2) The site of labeling chosen for ClC-0 is somewhat odd given that the chosen position is a transmembrane residue in the ion permeation pathway (Results and Discussion, fourth paragraph). Although this is evidently not the case based on the functional data shown in Figure 2, I would imagine the bulky dye addition would cause issues in buried positions. Indeed, there does seem to be some variance in the different dyes employed (Figure 2C). The authors may wish to clarify further why they chose this position versus one that is solvent exposed.

3) None of the dye structures shown in Scheme 1 are correct. They should either be corrected or, as their inclusion is not germane to the findings of the paper, removed.
