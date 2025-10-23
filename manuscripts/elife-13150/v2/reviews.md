# Peer review - Round 1

Editors:
- Axel T Brunger, Stanford University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.13150.015](https://doi.org/10.7554/eLife.13150.015)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Pre-transition effects mediate forces of assembly between transmembrane proteins" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Reviewing Editor and Richard Aldrich as the Senior Editor. Two of the three reviewers, Gerhard Hummer and Siewert-Jan Marrink, have agreed to share their identity. The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

This work introduces a new concept to understand membrane protein associations. It suggests that clustering of membrane proteins may not be a consequence of inter-protein or protein-lipid "mismatches" (e.g., membrane thickness as suggested by Milovanovic et al. Hydrophobic mismatch sorts SNARE proteins into distinct membrane domains. Nat Commun 6:5984. doi: 10.1038/ncomms6984, 2015), but rather by the differences in membrane thickness in difference "phases" of a membrane. If transmembrane domains are shorter than the thickness of a particular phase, they would then prefer to be in a phase that matches the length of the transmembrane domains, hence clustering in these areas. Thus, clustering of certain membrane proteins (such as SNAREs) may be a consequence of this "order-phobic" (but see comment 6 below) effect.

More specifically, in this work, simulations of coarse-grained lipid membrane models and of membrane/protein models show that (1) transmembrane proteins can induce a local order/disorder transition in a lipid membrane at conditions close to phase coexistence, and (2) that such local phase separation can drive protein association by a reduction of the interfacial free energy between the ordered and disordered lipid phases. These effects should be general in lipid membranes at conditions close to an order/disorder transition. By using orientational order parameters, the phase boundary in the membrane could be clearly resolved, enabling a characterization of its properties. In particular, the fluctuations of the length and shape of the boundary are shown to follow a capillary wave model down to almost molecular length scales. The observation of nanoscale phase separation induced by transmembrane proteins perturbing the local structure should be of interest not only to the physico-chemical community but also to bioscientists. In particular, it may play a role in lipid-mediated assembly of integral membrane protein complexes and supercomplexes.

While the reviewers and editors found this work interesting, concerns were raised as outlined below that need to be addressed in a revised version before a decision can be made. In particular, the authors are asked to respond to the concern about the biological relevance of the particular phase transition. If possible the authors are encouraged to perform a simulation that is more relevant to biology.

1) The authors mention in the Introduction a number of papers (Nishimura et al., 2006; Polozov et al., 2008; Swamy et al., 2006; Munro, 2003; Thewalt and Bloom, 1992; Owen et al., 2012) that supposedly provide evidence for the physiological relevance of gel domains. Either the referenced papers deal with situations in which membranes are being cholesterol depleted or thermally quenched, or they talk about liquid-ordered domains, not gel domains. In fact, in Munro, 2003 it literally states "The solid gel phase is not thought to be of physiological relevance". Please change the Introduction accordingly.

2) The demonstration of the attraction between proteins in this manuscript concentrates on proteins that induce local disorder in an otherwise ordered phase. In biological membranes the disordered phase is expected to dominate, to ensure fluidity and facile transport. The authors may thus want to discuss the reversed situation in a bit more detail (which should be quite symmetric). Ideally, the authors are encouraged to consider a simulation that is more relevant for the biological situation.

3) The authors may want to discuss in more depth the relation to the lipid raft model. Lingwood and Simons (Lingwood and Simons, 2010) argue that proteins segregate into domains of preferred lipid phase, ordered or disordered. Once such segregation has occurred, would the association force described in this paper effectively disappear? Can the two processes, segregation into domains of preferred phases (at coexistence), and attraction between proteins within mismatched phases, be reconciled (or are they the equivalent)? Could the effect presented here be a driver for raft formation? In such a process, "mismatched" proteins in a membrane close to phase separation would aggregate into clusters, and entropic effects would then push the phase boundary out.

4) Molecular determinants. What would make a protein orderphilic, beyond having low hydrophobic mismatch with the ordered phase? Are there ways to modulate the strength and the range of the interaction?

5) Membrane remodeling. The authors briefly discuss a possible role in membrane fusion. Interestingly, lipid phase separation has been suggested to play a central role in ESCRT-protein induced coat-free vesicle budding (Rozycki et al., PLoS Comp Biol 8, e1002736, 2012).

6) It would be instructive to include the definition of h(x) in Figure 1B.

7) The use of the word 'ordered' in both the Abstract and Introduction is misleading in the context of biomembranes. What the authors probably mean is solid-ordered, or gel, and not liquid-ordered. This distinction should be made from the beginning to avoid misunderstanding.

8) The final paragraph on the possible importance of the "order-phobic" force should be revised in light of the above comments.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Pre-transition effects mediate forces of assembly between transmembrane proteins" for further consideration at eLife. Your revised article has been favorably evaluated by Richard Aldrich (Senior editor), a Reviewing editor, and two reviewers. The manuscript has been improved but there are some minor remaining issues that need to be addressed before acceptance, as outlined below.

Reviewer #2:

The authors have largely addressed my concerns. Introduction Introduction and sections establish the biological relevance more clearly, without hiding the simplifications of the simulation model compared to biological membranes. Even if the new simulations of orderphilic proteins in a liquid-disordered membrane are only at a preliminary stage, the observed behavior clearly mirrors that of orderphobic proteins in a solid-ordered membrane, as would be expected. In my opinion, the new data strengthen the paper considerably, and I thus suggest including them.

Despite the simplifications compared to real biological membranes, the work provides strong evidence that the perturbation of lipid phase behavior by integral membrane proteins can create substantial driving forces for assembly. The paper should attract attention also by the experimental community and stimulate further explorations of the role of phase behavior. I recommend publication in eLife.

Reviewer #3:

My main previous concern, the biological relevance of the findings, is now much more clearly discussed in the revised paper.

There are two remaining aspects that still require some discussion:

1) The authors write "The orderphobic effect should be a general consequence of a first-order transition, whether the transition is between solid-ordered and liquid-disordered phases as considered explicitly herein, or between liquid-ordered and liquid-disordered phases as in multicomponent membrane systems". I strongly doubt that the transition between liquid-ordered and liquid-disordered phases is a first order transition. The experimental work of Veatch, Keller and co-workers (e.g. Veatch et al., ACS Chem Biol, 2008; Honerkamp-Smith et al., BBA Biomem, 2009), clearly shows that, upon cooling of a lipid extract (either from real plasma membranes or model membranes), the system shows critical behavior. I urge the authors to cite this work and discuss the implications thereof.

2) The authors should discuss the connection between their work and the work of Schäfer et al. (Shäfer et al., 2011) in more detail. The simulation studies of Schafer et al., based on the same (Martini) model that is used here, demonstrate that proteins are expelled from liquid-ordered domains as a result of 'orderphobicity'. Although the term orderphobic is not used, the driving forces for the partitioning of proteins into disordered domains are shown to be a direct consequence of the protein-induced perturbation of order in the liquid-ordered domains. In a subsequent study (Domanski et al., BBA Biomem, 2012), it is actually shown that these driving forces can lead to protein-induced domain formation. In the context of the biological significance of the current work, these studies should be properly discussed.
