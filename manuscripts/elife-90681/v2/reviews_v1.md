# Peer review - Round 1

Editors:
- Armita Nourmohammad, https://ror.org/00cvxb145 University of Washington United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.90681.sa0](https://doi.org/10.7554/eLife.90681.sa0)

This important work presents evidence that evolved biophysical compatibility between T cell receptors (TCRs) and MHC molecules is possible and a potential solution to the question of how TCRs could be biased towards MHC proteins given the massive diversity in both receptor and ligand. The evidence supporting the claims of the authors is solid, although the nature of these evolutionary questions makes it difficult to confidently answer some of the raised questions. The work will be of interest to immunologists, structural biologists, and evolutionary biologists.


---

# Peer review - Round 1

Editors:
- Armita Nourmohammad, https://ror.org/00cvxb145 University of Washington United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.90681.sa1](https://doi.org/10.7554/eLife.90681.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

[Editors' note: this paper was reviewed by Review Commons.]

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "Conserved Biophysical Compatibility Among the Highly Variable Germline-Encoded Regions Shapes TCR-MHC Interactions" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Eric Huseby (Reviewer #2); Brian Baker (Reviewer #3).

Comments to the Authors:

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife.

All reviewers agree that this study addresses an important topic, namely the sequence determinants of TCR-MHC binding modes. The sequence analysis in the study illustrates that the diversity of CDR loops and MHC contact surfaces is likely incompatible with hard-wired interaction motifs. However, the reviewers argue that the subsequent claims about the true origins of TCR:MHC docking orientations, and speculation about the origins of self-reactive TCRs, are based on flawed and unconvincing analyses. The reviews provide detailed suggestions as to how to improve the analyses to test the claims. We believe the substantial steps needed to address these reviews go beyond the scope of this manuscript but if the authors decide to expand on these suggestions, they can submit the manuscript as a new submission.

Reviewer #1 (Recommendations for the authors):

The authors investigate the origins of TCR:MHC docking orientation using information-theoretic sequence analysis simplified biophysical scoring, and inter-atomic contact analysis of solved TCR:pMHC ternary complexes. First, the authors show that the TCR CDR loops are more variable in sequence and in biophysical properties than the surface-exposed regions of the MHC. They conclude that "This mismatched diversity between the TCR germline-encoded CDR loops and the MHC α-helices suggests that conserved germline-encoded interactions are unlikely to exist for every possible molecular combination". Though not conclusive, this is consistent with the observed variability in the solved ternary structure databases, which show smoothly varying binding orientations rather than discrete recurring binding solutions. The authors also claim to see very little mutual information between TCR and MHC sequence positions, but they appear to be matching them up randomly (rather than using established TCR:MHC pairings from epitope-specific TCRs, for example, or TCRs from HLA-typed individuals), so it's not clear how this analysis could possibly find any covariation.

The heart of the study relies on a simplified 20x20 amino acid interaction matrix that is meant to capture basic biophysical interaction propensities. The sign of the values in the matrix is chosen to accord with intuition (opposite charges are favorable, like charges are unfavorable, etc), but the absolute values of the matrix values seem pretty arbitrary (all either 0, 0.5, 1, or 2). All matrix values for alanine and glycine are zero, despite their frequent involvement in tight hydrophobic packing interactions. The core calculation is to take all the residues in a given CDR1 loop (regardless of orientation: pointing toward MHC or toward the core of the TCR), and look up the interaction matrix scores for all surface residues (or maybe even all residues, period, it's hard to tell) of an MHC molecule, and sum up all the interaction scores. This single number (averaged over all HLA alleles) then reports the "interaction propensity" for that CDR1 loop sequence; if it's negative, then the loop/V gene has "severely limited interaction potential with HLA molecules". Despite the obvious problems with this – that the matrix is crude and arbitrary, that the sum involves many pairs of residues that couldn't possibly interact, etc, etc – the authors take these summed interaction scores as the basis for subsequent conclusions. For example, Figure 4 shows that TRBV7-2 and 7-3 have limited interaction potential (which appears to be related to them having glycine and alanine in their loops) with class I MHC; this finding is linked by the authors to the fact that these V genes are enriched in certain epitope-specific responses in celiac disease and multiple sclerosis, despite these enrichments being found in CD4 T cells. I looked at several TRBV7-2/7-3 containing ternary complexes (4mji, 5eu6, 5d2l, 4grl, 4ozh) and in fact, the TRBV7 segments are making extensive MHC contacts, dominating the TRAV segments in every case (4grl is a great example). It seems doubtful that the interaction scores derived from all pairwise residue matrix values are telling us anything about the intrinsic binding properties of the TCR V genes.

Next is a section entitled "Structural Data Validate Interaction Scores", in which they analyze atomic contacts in ternary complexes. Figure 5A certainly looks impressive at first glance, with tall bars for "predicted binders" and short or non-existent bars for "predicted NonBinders". But the problem is that there is no correction for the number of "nonbinder" V genes, and for example for CDR1A there only appear to be only 2 or 3 (Figure 4B), which may or may not have contributed to the database of solved structures. Thus the preponderance of observed contacts coming from "predicted binders" could just be due to the structural database composition, with binder and non-binder V genes making interactions at the same rate. The other problem with this analysis is that the contact analysis itself is flawed: the distance threshold is too small for hydrophobic interactions (4.5A would be better); there are too few total contacts being found (average of 1.35 per structure) the atom types included (referring here to the jupyter notebook https://github.com/ctboughter/PRESTO/blob/main/AIMS_interact_compare.ipynb) don't look right, since oxygen-oxygen and nitrogen-nitrogen can both form an H-bond donor-acceptor pair, and there's no evidence that hydrogens are being added to the structure; and the rules for counting "productive" contacts are too prescriptive (no carbon-carbon hydrophobic contacts allowed between polar or charged residues, even arg and lys with their long side chains). This latter has the consequence that the comparison to interaction scores becomes a little circular because the contact counting is driven by the same simplified biochemical intuition embodied in the pairwise interaction matrix. Much better would be to combine unbiased contact analysis (including backbone atoms) with an orthogonal measure such as buried surface area, and then look to see if predicted non-binder V genes really do make fewer interactions with MHC.

The remainder of the manuscript uses these interaction-matrix sums to investigate the determinants of the TCR:MHC docking mode. This is just not convincing, for the reasons outlined above, and also because there appear to be logical inconsistencies here. The concept is that MHC surfaces of "low interaction potential" (ie, alanine and glycine) define guardrails that limit the binding mode. Figure 8E has a nice cartoon showing the central ala/gly region in the class I alpha2 helix. The problem is that there are actually contacts throughout and on both sides of that "guardrail", which can be seen from Figure 7C, lower panel (161,164,165) or from a cursory examination of a few ternary complex structures. It's also not clear why, for class I α helix 2, MHC positions 143 and 144 have such low interaction scores (Figure 7C, upper panel) when in the alignment in Figure 8C those positions look similar to other R/K-containing positions.

On the positive side, the authors make their analysis scripts and notebooks very easily accessible, which is a big plus for reproducibility and transparency.

A few additional comments:

"The exposed residues on the α2-helix of HLA class I molecules are enriched in alanine and glycine relative to the α1- helix, which is highly unlikely to be involved in a specific, orientation-altering productive interaction" – alanine and glycine can be involved in highly specific packing interactions. Glycine, for example, can create pockets into which other side chains fit.

"Every crystallized TCR-HLA class II complex solved thus far adopts the canonical docking orientation whereby the TCR β-chain binds to the HLA α-chain helix, while the TCR α-chain binds to the HLA β-chain helix" – this is not correct, see 4y19 and 4y1a from the Rossjohn group.

"…obviating the need for a more precise approach" – do you mean "highlighting"?

This part of the methods is super-confusing (and I couldn't find it in the code): "Further, given that any single pair of amino acids on adjacent interfaces of protein binding partners can potentially form strong interactions without being meaningful for the formation of a given complex, we require that any productive interaction include a triad of at least weakly interacting residues".

As mentioned above, the whole mutual information analysis seems bonkers. How could there be any mutual information if the pairing between TCR and MHC is random/arbitrary? Please explain this part better:

"…every TCR should interact with every HLA allele. Humans largely possess the same TRAV and TRBV alleles, but each individual possesses a maximum of 12 HLA alleles. We expect that specific alleles that are unable to enforce the supposed evolutionary rules for canonical docking will not be allowed to persist in the population. Continuing from this assumption we then subsample the data and calculate the mutual information on this subsampled dataset. Each TRAV and TRBV allele (the input) is matched with a single HLA allele (the output), and the mutual information is calculated for these pairings".

Reviewer #2 (Recommendations for the authors):

The authors take an all-encompassing computational approach to analyzing TCR CDR – MHC interactions with the goal of identifying repetitive use of complementary protein-protein interaction events. On a first pass, there does not appear to be a significant contribution (to the T cell repertoire) of truly conserved pairwise interactions that drive MHC restriction. In contrast, their 'whole repertoire-wide approach' strongly supports the general concept that TCRs find opportunistic ways to bind pMHC using biochemically similar interactions.

First, I want to state that I really enjoyed reading this paper. I think it is written very well, which is quite important for papers on this topic as it can be a struggle even for seasoned immunologists to comprehend how there might be 'rules of engagement' when both the TCR and MHC/HLA are highly variable proteins. My comments will largely focus on issues that may help the authors provide the readers with a better understanding of the background and what their program does, and does not do. I will use statements within the manuscript to highlight these challenges.

In the abstract, "The formation of the TCR-peptide-MHC complex (TCR-pMHC) can be broken into two types of interactions, one between the hypervariable TCR CDR3α/β loops and the presented peptide and the second between germline-encoded regions of the TCR and MHC. "

– This is not an accurate statement. There are significant interactions between the CDR3 and MHC, as well as CDR1 and peptides. E.g., CDR1a often engages p-1 and p2 peptide residues, CDR3b almost always engages at some level, MHC-IIa61 area, and CDR3a with MHC-IIb 60area. Within the manuscript, the authors back off a bit from their hyper-simplistic statement, however, having such a blunt untrue statement in the abstract is not reasonable.

"Instead, binding properties such as the docking orientation is defined by regions of biophysical compatibility between these loops and the MHC surface."

– The authors spend a lot of effort working through certain variables that contribute to the binding reaction. I am wondering if the authors took account of shape complementarity (e.g., PMID: 9628472) and CDR loops that carry different types of conserved canonical structures (e.g., PMID: 10656805). One could imagine that based on the protein folding requirements of CDR regions, certain residues are in the interface whereas others are internal to the CDR structure and cannot actually contribute directly to binding.

"We selected a key hydrogen bonding network in the KIR2DL2-HLA-C*07:02 interface [50] and compared this to the evolutionarily conserved YXY motif of CDR2β [19, 21]".

– This is a good example to discuss the point above. it is important to know structurally, where each residue is. For example, the first Y (46 or 48 depending upon the nomenclature, above) often does not directly contribute to pMHC binding but may be important for the "outline structure" of the CDR loop itself. In addition, the authors do not discuss Van der Waals interactions really at all. Much of the TCR-pMHC interface (binding affinity) is driven by the exclusion of water, a property that is very difficult to assess on an amino acid-amino acid pairwise allotment of interaction energy. I was hoping that once the authors started to discuss "areas of binding potential" the contribution of non-side chain to side chain interactions would be discussed. It is unclear to this reviewer if these types of interactions are accounted for within their algorithm or if they are largely ignored.

In discussing the interaction potential, of amino acids, the authors cite and discuss a single manuscript.

42. P. Nandigrami, F. Szczepaniak, C.T. Boughter, F. Dehez, C. Chipot, and B. Roux. Computational assessment of protein-protein binding specificity within a family of synaptic surface receptors. Journal of Physical Chemistry B, 2022.

There is of course an empirical and computational field of study for how proteins bind one another as well as for TCRs and pMHC (e.g., PMID: 10410805, PMID: 16193038, PMID: 18946038, PMID: 27348411). Some more inclusive discussion of past ideas about how proteins interact with one another and whether old ideas remain accurate could add to the overall discussion.

"Figure 4: Interaction score between every TRBV (A) or TRAV (B) sequence and HLA allele for all four germline-encoded CDR loops. "

– Why are alanine and glycines assumed to be zero/non-interacting? Does a binding reaction care if a contact is a side chain-side chain, backbone-backbone, or mix? Indeed, when the authors "counted the contacts" I assume many of the side chains were indeed interacting with backbone atoms. It has also been suggested that some side chains can contribute negatively to interfaces (e.g., PMID: 17041605). Another question, perhaps for the algorithm used, does it take into account the frequency at which say X and Y amino acids actually occur at a possible site of interactions. It is mentioned that autoimmune-prone T cell repertoires are biased for certain TCR usage, does this bias include matching/non-matching HLA areas of recognition? There was some discussion on this but a clearer picture (if there is one) could be spelled out for the non-expert.

The interaction potentials also succeed in predicting TCR complexes that will not make contact with MHC. 20 of the 22 structures predicted to have poor CDR2β binding make no contact with MHC, while the last two only make one contact with MHC (Figure 5C). Further, all 8 structures predicted to have poor CDR1β binding make no contact with MHC. (Figure 5C). Again, this prediction accuracy is lower for class II predictions (Figure 5D).

– This is a super interesting idea that may unlock a lot of what is going on. One wonders how much of this is random chance, i.e., if a different TCR-pMHC with the same V genes and HLA would behave similarly. Also, do these structures preclude (or are driven by) CD1-peptide contacts, or are the structures carry such a different docking orientation as to completely preclude the CDR1 and CDR2 regions from being part of the binding interface?

The exposed residues on the α2-helix of HLA class I molecules are enriched in alanine and glycine relative to the α1- helix, which is highly unlikely to be involved in a specific, orientation-altering productive interaction.

– In practice, it is this reviewer's understanding that there are exit contributions of Van der Waals interactions at these sites. Indeed, early ideas suggested that the diagonal area of pMHC (MHCa 61, MHCb73) used this divot for shape complementary purposes.

It is important to note that these interaction potentials take an unbiased approach, calculating every possible interaction between TCR and MHC residues to produce this final score.

– It was unclear if the authors mean position by position, or did they weigh whether a residue was actually surface exposed and capable of being part of the binding interface.

productive side-chain interactions between CDR loops and the solvent-exposed residues of the MHC helices.

– There does seem to be an (over) emphasis on side-chain interactions. And less so on the clustered ability for VDW and/or inhibitory interaction.

– In general, there are quite a number of T cell development citations with actually very little discussed the role of thymic selection in and/or clonal T cell responses in skewing the TCR-pMHC interface to conform to selective pressures. E.g., TCRs can't be too good/cross-reactive or they would undergo central tolerance.

"In calculating the interaction score, we assume that productive contacts are only made by the side chains of the interacting residues. This simplification does not capture all TCR-pMHC complex contacts, but here we are looking for selectivity enforced by specific TCR-MHC interactions mediated by side-chains."

– Though stated as a caveat, perhaps some effort could be made to include side-chain to the backbone, etc interactions.

Reviewer #3 (Recommendations for the authors):

Boughter and Meier-Schellersheim describe an analysis of TCR-peptide/MHC complexes, aiming to gain an understanding of the underpinnings of the "common" TCR binding geometry. This is fundamental to understanding the MHC restriction of TCRs and how T cells scan and readout peptides. They begin with a comprehensive bioinformatics approach, move to a structural analysis to help interpret the informatics, and bring in biophysical computations. The overall conclusion that specific contacts between TCR genes and MHC proteins are not necessarily pre-programmed and that traditional TCR binding geometries emerge from biophysical compatibility is supported by the data and consistent with recent findings. In general, the work and the conclusions are an advance and place recent findings into perspective. However, the strength of evidence is weakened by choices made in characterizing structures, computing energies, and a strained reliance on "roles" played the parts of the interface which have been discounted many times yet persist in the literature. The latter in particular weakens the discussion and how the authors view the impact of their work.

The major strength of the paper is the approach taken; I found the comparative analysis of TCR and MHC genetic variability at the sequence level particularly compelling. Bringing in KIRs as a control was also a strong way to support the arguments. There is one major technical weakness in that, as far as is clear from the methods, interatomic interactions were considered with a 3.5 Å cutoff. This is woefully inadequate. Electrostatic interactions can be strong at long distances, which the authors really need to consider – say, going out to 6 Angstroms or so (there is much-published literature on short- and long-range electrostatics in protein interfaces). The importance of long-range electrostatics in TCR-peptide/MHC complexes has been demonstrated previously, particularly in prior work that aimed to address the same problem studied here. The authors also fall victim to the common immunology trope that CDR3-peptide interactions drive specificity, leaving CDR1/CDR2 to bind MHC proteins, i.e., the CDR loops have "roles" in binding. In the very first high-resolution structure of a TCR-peptide/MHC complex, CDR3 interactions with a class I MHC were noted and remarked on, as were CDR1 and CDR2 interactions with the peptide. Later work showed that these CDR3-MHC and CDR2-peptide interactions were critical for binding. These findings have been replicated several times now. The authors' introduction of this perspective of different loops of the TCR playing evolved roles (CDR3->peptide, CDR1/2->MHC), and their interpretation of their findings in light of it, weakens the papers' conclusions and impact, and it is a missed opportunity that can be addressed with the authors' approach.

The authors also should consider other literature for a greater impact on their work. For example, they also exclude backbone interactions – this is a curious omission from a biophysical perspective, and others in the field have published on the importance of backbone-mediated interactions (hydrogen bonds mostly) in stabilizing TCR interfaces. The authors also mention but fail to address T cell selection and the role of selection (and possibly coreceptor) in 'enforcing' what we get and have seen structurally (i.e., the idea that pre-selection TCRs bind all over the place, but selection ensures we get ones that bind right and work). Much has been written about this and it should be included.

1) The very first high-resolution crystal structure of a TCR-pMHC complex by Garboczi and Wiley in the 90s (PMID 8906788) showed CDR3 contacts to the MHC and germline CDR1/2 contacts to the MHC. Later biophysical studies by our own group showed these were crucial for binding (PMID 23736024). Other work has shown the same. Thus, although it is common to say that diverse CDR3 loops bind peptide and germline-encoded CDR1/2 loops bind the MHC, this is not supported at the atomic or energetic level. It actually plays INTO the authors' argument about opportunism/compatibility, but curiously the authors do not discuss it. They should. These observations and the idea that "roles" are not hardcoded into the TCR CDR loops play right into the authors' opportunistic argument introduced at the end of the paper.

2) A 3.5 Å cutoff is far too limited and ignores long-range electrostatics. Our own work addressing the same problem (which also introduced the notion of opportunism/compatibility) found signals for some "sloppy" evolved compatibility but only if we moved to longer ranges (PMID 26884163). The authors should re-evaluate their energetic analysis using longer-range cutoffs. To avoid greatly complicating the analysis, longer ranges could be done only with charged side chains. It was also very curious to omit main chain interactions, something which the authors might want to work back in (see PMID 17041605).

3) The authors should really address the question of how thymic education influences what we see. For example, we recently published a TCR that binds with an outlier geometry (not reverse) which signals just fine – an example of a class-mismatched TCR (emerged from a CD4+ T cell but binds a class I). This TCR is a bit weird in that it has an unusually long CDR3b loop that contacts both peptide and MHC (point 1 again). We also concluded that this is a weird TCR that somehow escaped normal thymic selection, implying that maybe the pre-selection repertoire has TCRs that bind crazily and one role of thymic selection is to filter these, giving us TCRs that are somehow "better" biologically (maybe they signal better, or possess lower x-reactivity, etc.). The authors need to work this thinking in. Relevant papers are PMID 36424374 and PMID 30833553.

4) The authors use "compatibility" and "opportunistic" to describe TCR binding from a biophysical perspective, contrasting this with the hard-coded model. These are not new concepts though, and although the authors have greatly expanded on the topic (albeit with the limitations above), they should make note of this. They do reference some of the appropriate literature, but clarifying how they are expanding on the topic would strengthen the impact of the work.

[Editors’ note: further revisions were suggested and these were then sufficiently addressed prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Conserved Biophysical Compatibility Among the Highly Variable Germline-Encoded Regions Shapes TCR-MHC Interactions" for further consideration by eLife. Your revised article has been evaluated by Tadatsugu Taniguchi (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Essential revisions:

As you can see from the report, the reviewers appreciate the changes done for revision. After an extensive discussion, the overall consensus of the reviewers is that while the concept of evolved biophysical compatibility is possible and a potential solution to the question of how TCRs could be biased towards MHC proteins given the massive diversity in both receptor and ligand, it is a concept that is exceptionally difficult to demonstrate and the paper still has some wishful thinking. For this manuscript to move forward, we request that you tone down the paper, remove the claims highlighted by reviewer #1, and present the concept as an interesting possibility for which some evidence is offered but no solid proof (see report from reviewer #1 for details).

We also had a discussion with regards to the suggestion of reviewer #2 to perform a similar analysis on BCRs to verify that the signal is not spurious. We acknowledge that this might be beyond the scope of the current paper. However, if the authors chose to do this analysis, it can help solidify some of the claims.

Reviewer #1 (Recommendations for the authors):

I recognize the time and effort that the authors have invested in responding to the reviews of the first version of the manuscript. It is appreciated that they recognized the circularity of the original Figure 5 and removed it, adjusted the distance thresholds and sequence-filters for contacts analysis, and that they have also removed references to the origin of self-reactive TCRs.

My concerns with regard to the claims about V-gene interaction potential and determinants of the binding mode still stand, since the relevant text hasn't been modified and the author's responses are not convincing. For example, the detailed analysis of the TRBV7-2 containing complexes provided by the authors in the response appears to disprove the AIMS-based prediction that this gene has low interaction potential: "Certainly PRESTO agrees with these structural interpretations, suggesting CDR2B dominates the germline interactions here, with 13/15 SC-SC contacts." The contorted logic that the authors produce to explain this disconnect doesn't really make sense: "However, yet again we have an abnormally high number of CDR2B backbone-backbone interactions, 14, suggestive of nonspecific tight packing not driven by TCRB specific interactions". What exactly is "nonspecific tight packing"?

The authors also continue to over-sell their findings in the newly introduced text. For example, in describing the new Figure 5, the authors state: "This comparison shows exceptional agreement between our bioinformatic results and structural analyses". But when one compares Figure 5a and 5b, for example, the agreement is pretty dubious. And in 5d, *none* of the differences are significant, and many show the wrong directionality, for example, the median value for "Weak TRBV" is always greater than or equal to the median value for "Moderate TRBV". And in the new text describing the AIMS potential: "The AIMS interaction potential, which can swiftly analyze thousands of sequences, has significantly outperformed more physically detailed and computationally expensive models. In a binary classification of a large database of structurally similar protein complexes, the AIMS interaction potential was capable of distinguishing binders and non-binders to an accuracy of 80%, whereas calculations run on over 45µs of simulated all atom trajectories could only distinguish to an accuracy of 50%. " I looked back at this reference, and what the authors neglect to mention is that the 80% performance comes from a highly parameterized model based on a linear discriminant analysis fitting a weight for each pair of residues in the interface-- it's not at all analogous to the calculation here in which AIMS scores are directly summed up. It's also a single family of interacting proteins.

Reviewer #2 (Recommendations for the authors):

With regards to the manuscript in general, in some places, the authors seem to want to have their cake and eat it too. Particularly, the idea that TCRs are evolutionarily biased to recognize MHC, included stating support for the "codon model" while at others suggesting that CDR1s and CDR2s have only minimal (complementary) roles in binding. With the extension suggesting that some TRAVs and TRBVs have no (or very minimal) MHC/HLA binding potential. This later argument would suggest that antibodies, fully capable of creating diverse CDR3s, should similarly have a (modest, strong) ability to bind pMHC ligands. I suppose a computational test of the general idea the authors are putting forward would be to use their AIMs platform with human antibody CDR1s and CDR2s to see if these were all net no-binding or negative binding with MHC. However, I do not like the idea of bringing up additional questions/tests of the model during a re-review.
