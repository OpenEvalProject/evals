# Peer review - Round 1

Editors:
- Andreas Martin, University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54387.sa1](https://doi.org/10.7554/eLife.54387.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Using an elegant combination of peptide arrays, mutagenesis, protein engineering, and various biochemical assays, this study investigates the mechanisms and molecular determinants that control the recognition and partial mechanical unfolding of aminolevulinic acid synthase (ALAS) by mitochondrial ClpX (mtClpX) to promote PLP cofactor incorporation. The authors provide important new insights into the principles underlying non-proteolytic functions of ClpX and related motors of the AAA+ ATPase family.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Mitochondrial ClpX activates an essential metabolic enzyme through partial unfolding" for consideration by eLife, and our apologies for the delay in providing you with reviews.

Your article has been reviewed by three peer reviewers, including Andreas Martin as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the reviews, we regret to inform you that your manuscript can not be considered for publication in eLife in its current form, but we encourage re-submission after the reviewers' major criticism has been addressed.

All three reviewers agreed that this manuscript describes technically challenging, sophisticated, and well executed biophysical analyses of ALAS activation by mtClpX, that the presented data are clear, elegant, and compelling, and that the manuscript is well written. However, even though this study provides new insights into mtClpX's recognition motif and initiation site for partial ALAS unfolding, there were concerns about the degree of conceptual novelty and advance compared to your previously published papers on mtClpX-mediated ALAS activation. The reviewers felt that the results did not yet converge into a coherent story, and the conclusions did not extend substantially beyond the mechanisms previously described by your group for ClpXP in general or mtClpX's action on ALAS in particular. A clearer picture of mtClpX's action, especially identifying the reasons for its arrest during ALAS unfolding and translocation, would make this a much stronger manuscript and more appropriate for publication in eLife. We would therefore recommend that you consider re-submission to eLife after those mechanistic questions have been addressed in more detail.

Major point:

What primarily limits the impact of this study is the lack of mechanistic understanding on why mtClpX stops unfolding and translocation of ALAS. As a first step, the authors should therefore attempt to identify the position of mtClpX stalling in more detail.

In their HDX-MS analyses, the authors observed a short sequence at the alpha1 / beta1 junction that exhibited no mtClpX-induced exchange, and they speculated that this may represent the stall site of mtClpX. However, it seems unlikely that the interactions of the ALAS polypeptide with pore-1 loops of a stalled yet ATP-hydrolyzing mtClpX are static and "tight" enough to prevent HD exchange to a similar extent as amide-proton protection in a hydrophobic core or when involved in H-bonds of secondary structures. Based on previous biochemical experiments and recent structures of related AAA+ motors with bound substrates, pore-loop interactions with substrate are expected to be mostly steric in nature and thus to not strongly interfere with hydrogen exchange.

With the presented data, it is difficult to predict a potential stall site for mtClpX. For instance, there is no information about cooperativity in the unfolding of ALAS' N-terminal region, and it is not ruled out that mtClpX only tugs on the N-terminus, translocates only a few residues, or dislodges alpha1 etc. HDX-MS experiments analyzing the foldedness and dynamics of N-terminally truncated ALAS variants could give insights into how disrupting individual secondary structures affects the conformation around the active site. Alternatively, and more obvious for the Baker lab, the authors could consider using ClpXP to more reliably identify the stall site through partial degradation (similar to their previous studies on partial degradation of GFP-fusion proteins by E. coli ClpXP in the presence of ATPgS). This information about an approximate stall site may point towards the underlying mechanism, for instance reduced grip on a low-complexity sequence etc., which can then be tested in additional experiments. The authors comment that, unlike what is proposed for the proteasomal degradation of NFkB precursors, mtClpX does not stop at an inter-domain boundary in ALAS. Perhaps there is a kinetic rather than a thermodynamic barrier to unfolding in ALAS. It would be interesting to delve more deeply into the structural features of ALAS that may block further unfolding by mtClpX, for instance using a ALAS-destabilizing mutation.

1) The authors used a peptide array to identify mtClpX-binding regions of ALAS, which are shown mapped on the ALAS dimer structure in Figure 1A. However, how do the authors envision mtClpX simultaneous interaction with regions 1, 2, 4, and 5 (and maybe 6), given their distance and differential orientation/accessibility from a particular side? Is it possible that the N-terminus of PLP-free ALAS is in a different conformation compared to the holo-enzyme? The authors mention later that the beta1-3 sheet is unresolved in the PLP-free crystal structure. This should be brought up earlier and more explicitly, as it may indeed suggest an alternative conformation for the N-terminal region of PLP-free ALAS. The HDX-MS analysis of hydroxylamine-treated, PLP-depleted ALAS (data in the Supplementary file 1) seems to show increased accessibility up to residue ~ 80 compared to holoenzyme. Either way, the authors should consider including these data for the deuterium uptake of ALAS-hxl as a main-text figure, because unfolding of apo-ALAS by mtClpX for PLP-incorporation is expected to be even more relevant than unfolding of the ALAS holoenzyme.

2) The authors use alanine and aspartate mutations in their peptide array analyses to investigate mtClpX interactions with the various N-terminal regions of ALAS, and propose a multivalent recognition site. However, it remains unclear what the contributions of regions 2-6 in the ALAS context actually are, because, according to Figure 1D, alpha1 alone placed on the N-terminus of a DHFR-ALAS fusion is as good as the delta57 N-terminus in supporting mtClpX catalyzed PLP binding. In this case, regions 2-6 are expected to not contribute to mtClpX binding due to their spatial separation from alpha1 and the translocation initiation site. The authors may consider a more detailed Michaelis-Menten analysis of the alpha1-DHFR-ALAS construct to assess the Km and Vmax effects of separating alpha1 from the rest of the ALAS N-terminus. Compared to the mutations in various binding regions, this separation of alpha1 has the advantage of preventing ClpX binding to regions 2-6 without potentially destabilizing the N-terminal region through mutations.

3) All kinetic measurements of PLP binding and the comparisons between ALAS constructs presented in Figure 1 were performed at concentrations well below the Km of mtClpX for the respective constructs, and therefore allow only tentative conclusions. For instance, that E. coli ClpX shows a rate of λ-O-ALAS unfolding (PLP binding) that is similar to the rate for mtClpX unfolding of wild-type ALAS may be just a coincidence (unless the Km values of mtClpX for ALAS and E.c. ClpX for λ-O are indeed almost the same).

According to the Michaelis-Menten analyses presented in Figure 2, the authors can produce sufficiently high concentrations of ALAS and should therefore be able to also perform the kinetic experiments presented in Figure 1 under saturating conditions and compare Vmax values.

4) The co-IP assays for mtClpX (EQ) binding various ALAS mutants (Figure 3) shows a higher amount of pulled-down delta57-ALAS compared to delta34-ALAS, despite its > 2-fold higher KM. The authors should try to explain this observation. Do the extra 23 residues at the N-terminus of delta34-ALAS lead to a steric hindrance and interfere with mtClpX binding? How can this be compatible with the lower KM for delta34-ALAS? Could this be a consequence of the hydrolysis-dead EQ mutant, in which ATP-hydrolysis-dependent engagement of an extended tail cannot contribute to substrate affinity?

5) The authors propose a model on how heme binding to the flexible N-terminal extension of vertebrate ALAS may switch ClpX activity from partial to complete unfolding for proteolysis. However, it is unclear how effector binding to the flexible initiation region, which is threaded (and thus stripped of anything bound to it) well before ClpX reaches its stall site, could affect the outcome of ClpX translocation. Of course, the authors can only speculate, but they should try to make this proposed model on the effects of heme more consistent with their own findings of ClpX threading ALAS from the N-terminus and stalling further downstream.

6) Besides partial unfolding for PLP incorporation, mtClpX also seems to regulate ALAS protein levels. How can these two observations be reconciled? Is there an ALAS population that is fully unfolded by mtClpX? This would result in a fraction of molecules that is fully deprotected. Or does mtClpX use a different recognition motif for targeting ALAS to degradation?

7) In the second paragraph of the Discussion section, the authors state that: "its (tail) deletion increased Vmax of mtClpX rather than the avidity…".

Presumably "deletion" should be replaced with "extension", or "increased" should be changed to "decreased".
