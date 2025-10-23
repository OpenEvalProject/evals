# Peer review - Round 1

Editors:
- Michael T Laub, Massachusetts Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.47534.055](https://doi.org/10.7554/eLife.47534.055)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Evolution of (p)ppGpp-HPRT regulation through diversification of an allosteric oligomeric interaction" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Michael Marletta as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript, the authors investigated the inhibition of HPRT, a key enzyme for the salvage of purine nucleotides, by the bacterial alarmone (p)ppGpp. They purified recombinant HPRT homologs from a broad spectrum of organisms for in vitro analysis, and revealed a significant variation of their affinities to (p)ppGpp. They then performed in-depth studies of pppGpp-sensitive HPRT homologs from Bacillus species using a combination of structural, biophysical and biochemical techniques. Surprisingly, although the binding site of pppGpp almost completely overlaps with that of HPRT substrates, substrate binding leads to the dissociation of HPRT tetramer, which exists in apo- or pppGpp-bound states, into dimers. By comparing sequences, structures, and oligomerization properties of HPRT homologs sensitive or refractory to (p)ppGpp inhibition, the authors concluded that tetramerization of HPRT triggers structural rearrangements to enhance (p)ppGpp binding, and that a dimer-dimer interface supporting tetramerization is the defining feature of (p)ppGpp sensitivity among HPRT homologs. They call this interplay between oligomeric state and ligand affinity "oligomeric allostery". Using ancestral protein reconstruction, the authors also suggested that the emergence of the dimer-dimer interface is likely coupled to the evolution of (p)ppGpp sensitivity.

Although there was enthusiasm for the work, the reviewers collectively raised a number of concerns, some about the work itself and some about the interpretation or presentation of the data. Some of these concerns should be straightforward to address experimentally. Others may be more involved, particularly points 4-5 and the broader issue of whether this mechanism is relevant in vivo given the physiological concentrations of the molecules in question. If the authors feel that all of the issues could be addressed, the reviewers would welcome a revision.

Essential revisions:

1) The authors cited others' work and their own ITC data and claimed that HPRT is not an allosteric enzyme. In fact, apo-HPRT is likely a tetramer at the working concentration for ITC (45 μM) so that the experiment is not expected to reveal cooperativity. Conversely, it is possible that apo-HPRT falls apart into dimers when diluted to ~100 nM for biochemical assays so that the cooperativity for pRpp was not observed. Nonetheless, if pRpp binding dissociates HPRT tetramers into dimers, ITC of HPRT with pRpp should reveal cooperativity, and the [pRpp]-Vi relationship should deviate from the Michaelis-Menten model when HPRT concentration is sufficient to maintain a tetrameric configuration in the apo-form. The authors should present these data as important supporting evidence for their oligomeric allostery model.

2) Throughout the second half of the manuscript, the authors emphasize the significance of tetramerization on tight (p)ppGpp binding, but touched very little on the other side of the allostery, namely, how tetrameric vs dimeric HPRT affects the enzyme activity? For instance, is HPRT made constitutively tetrameric (e.g., crosslinked with disulfides) less active? And can the phylogenetic studies be used not to break a tetrameric HPRT (as is already done) but to make a normally dimeric HPRT tetrameric and thus subject to ppGpp-based regulation?

3) Subsection “(p)ppGpp regulation of HPRT is conserved across bacteria and beyond”: "these results suggest significant inhibition of HPRT under physiological, basal levels of (p)ppGpp" Provided that inhibition by (p)ppGpp is competitive with respect to pRpp, the magnitude of inhibition also depends on the physiological level and Km for pRpp. In other words, it's difficult to say in vivo what the effect of ppGpp will be (especially at low concentrations) unless one also knows the concentration of pRpp and the enzyme's Km for pRpp. Can these values be measured? If not, it may significantly impact what can be concluded about the level of inhibition by ppGpp in vivo.

4) In the end, it's not clear how important the ppGpp-driven stabilization of a tetramer is for inhibition. In the chimera experiment in Figure 4, the authors disrupt tetramerization and the affinity for ppGpp decreases 20-fold. But is this chimera no longer inhibited by ppGpp or does it just take higher levels? As the authors point out, ppGpp levels can get into the mM regime, so how much does a change in affinity from 1 to 20 μm matter in vivo? Related to this, the authors only examine enzyme inhibition in Figure 1 at one concentration: 25 uM. Maybe some of the enzymes, like the L. pneumophila enzyme used in creating the chimera in Figure 4, are more fully inhibited at even slightly higher concentrations. We wouldn't expect the authors to examine enzyme inhibition in detail for every organism's HPRT, every mutant, and the chimera in Figure 4, but in a few select cases (especially the chimera and a couple of the orthologs) it seems essential to do so.

5) What are the in vivo consequences of not forming a tetramer in B. subtilis, with respect to GTP homeostasis?

6) Ancestral reconstruction

The ancestral reconstruction method used was not correct and needs to be redone. This is a critical problem, as they authors do not establish that the branching pattern of their phylogeny is correct for the deepest nodes (Anc 1-7). If the branching pattern was different, these ancestors simply would not have existed. As a result, it is not clear whether the ancestor was a dimer that became a tetramer (as they claim) or was instead a tetramer that became a dimer.

The solution to these issues would be to do the reconstruction using established methods (see below) using a much larger set of sequences than the 141 chosen. It may be that their conclusions are robust to a better reconstruction, but they must establish this before publication.

A) None of the nodes they reconstructed (Anc 1-7) have bootstrap values above 90. They do not report the support values for these nodes, but I suspect that the support for these nodes is very low (see D below). Even though the posterior probabilities on the reconstruction of ancestral amino acids are high for the sites they identify as important, the authors have not convinced me that these nodes actually existed historically. Maybe the lineage lacking the dimer-dimer motif evolved later, representing a loss of ancestral tetramerization. This possibility cannot be distinguished from the hypothesis they present on the basis of their tree.

B) They constructed their tree using the WAG+G+I substitution model, but then reconstructed their ancestors using the JTT model. This mismatch is not correct and likely changed their reconstructed ancestral amino acid states. This should be re-done using consistent models.

C) They never justified the substitution models they chose (usually done using something like ProtTest or a manual AIC calculation). This should be done.

D) If the branch length unit shown on their tree (Figure 5A) is substitutions per site (as it usually is), their placement of the S. cerevisiae protein is highly suspect. By eye, that branch accumulated ~1.5 subs/site, indicating it likely aligned very poorly. All one can see from the tree is that the bootstrap value for this placement is <90 – but likely it is much lower. There are several strategies they could/should employ to get around this. First, build a much larger alignment that includes multiple representative sequences from the outgroup clade. This should better resolve the phylogeny. Second, report support values on all nodes-particularly the nodes that they use for reconstruction studies. If the support for these nodes remains low, strong claims about the order of branching and order of evolution of dimerization and tetramerization cannot be made.

E) They show a branch length label of "0.2" on their tree (Figure 5A), but do not define it in the legend. This should be done.

F) They did not describe what method they used for the reconstruction. They cite Jones, 1992, but this is the JTT substitution model, not the reconstruction method. Presumably they are using a marginal probability reconstruction (e.g. Yang, 1995). This should be stated.

G) To ensure reproducibility, the authors should publish their alignment in the supplement.

7) "Oligomeric Allostery"

The authors spend significant time in the discussion arguing that their work reveals a new phenomenon they call "oligomeric allostery." It does not seem it was ever defined precisely in the text; however, as we understood it, it is a change in oligomeric state that controls ligand specificity. They point out in numerous places that they think is a new and important observation (Discussion section).

We do not think it is new. The authors note that there are many instances in which ligand binding controls oligomeric state (e.g. subsection “Protein oligomerization allosterically alters ligand specificity”). But, from the perspective of linkage thermodynamics, this is equivalent to saying ligand binding controls oligomeric state. The earliest thinking regarding allostery and cooperativity was informed by studies of oligomeric states (Perutz, MWC, etc.).

In our view, this framing hurts the manuscript, but not the underlying study. We think they could recast the work without relying on this dubious premise. The authors would be better served to argue that ligand binding and oligomeric states are often tightly linked to one another. They could then describe their work as a cool way that this interplay enables evolutionary change (in their case, by allowing mutations to accumulate away from a conserved binding pocket to promote a change in specificity).

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting your article "Evolution of (p)ppGpp-HPRT regulation through diversification of an allosteric oligomeric interaction" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Michael Marletta as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The reviewers were generally satisfied with your responses to the initial set of concerns raised. There are, however, a couple of remaining issues that you should address in a revision.

1) The first is that the reviewers were not entirely convinced by the proposed mechanism. If we understood it correctly, you are still proposing a cooperative mechanism but have no data supporting cooperativity. This came out most directly in the revision cover letter, where you suggest that cooperativity would not arise if (1) a single (p)ppGpp is sufficient to lock the tetramer in place and (2) four PRPP molecules are necessary to cause dissociation into a dimer. But this did not make sense to the reviewers – one of them even pieced together a set of linkage equations compatible with your verbal model and explored them on a computer and could not find any parameters that did not display cooperativity in PRPP. Your revision should clarify your proposed mechanism and whether cooperativity is a key feature and if so, what results support that interpretation.

2) It was difficult to assess your revisions as you did not always state whether the individual points had given rise to textual changes or not. Some were obvious, but others less so. In your next revision, please address the following:

a) How is the oligomeric state of each structure assessed? While it is clear that the PRPP + 9- deazaguanine bound form is dimeric from the packing in the supplied PDB file, the tetramer observed in the other two structures could in theory be a result of crystal packing. Usually, a tool like PISA is used to assess the validity of proposed multimers in crystal structures, but the authors make no reference to this. Please confirm that PISA agrees with the conclusions about oligomeric state.

Thank you for including the PISA analysis in the response to reviewers, this is quite clear. I also notice that you now mention PISA in the Materials and methods section. However, I believe it will be of value to the readers to have this information also at the relevant place in the Results section, i.e. whenever you conclude on oligomeric state, I suggest you say that this is supported by PISA analysis.

b) Subsection “(p)ppGpp binds the conserved active site of HPRT and closely mimics substrate binding”. Have the authors considered that the pppGpp preparation could contain a ppGpp contamination that crystallised with the protein? Would it be possible to check for this?

Could the authors please indicate whether this has resulted in any changes to the manuscript?

c) Subsection “(p)ppGpp prevents PRPP-induced dissociation of HPRT dimer-of-dimers” and Figure 3. What is the reason for excluding 9-deazaguanine during gel filtration and cross- linking? The comparison to the crystal structure would be more direct if both substrates were present. Is it possible that the oligomeric state of the protein only in the presence of PRPP is different?

Could the authors please indicate whether this has resulted in any changes to the manuscript? In this case I would suggest that you include this additional experiment as supplementary data in case other readers wonder.

d) Subsection “Dimer-dimer interaction allosterically positions loop II for potentiated (p)ppGpp binding”. Can the authors exclude that the structural variations observed in loop II to some extent are induced by crystal contacts?

Did this give rise to textual changes?
