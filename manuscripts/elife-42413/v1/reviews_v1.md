# Peer review - Round 1

Editors:
- Pekka Lappalainen, University of Helsinki Finland

Reviewers:
- Pekka Lappalainen, University of Helsinki Finland
- R Dyche Mullins, University of California, San Francisco United States

## Review text

DOI: [10.7554/eLife.42413.025](https://doi.org/10.7554/eLife.42413.025)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Reconstitution of the equilibrium state of dynamic actin networks" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Pekka Lappalainen as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Anna Akhmanova as the Senior Editor. The following individual involved in review of your submission has also agreed to reveal their identity: R Dyche Mullins (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The effects of various actin-binding proteins on the dynamics of individual actin filaments have been extensively studied, but much less in known about how they regulate physiological networks of actin filaments. Earlier study by Boujemaa-Paterski et al., 2017, revealed that both width and density of the Arp2/3-nucleated networks affect their growth rate and steering in vitro. Here, Manhart et al., applied similar in vitro reconstitution and mathematical modeling approaches to study the effects of ADF/cofilin on the network dynamics. Most importantly, they reveal that: i). ADF/cofilin disintegrates the actin network into micron size fragments, ii). Local depletion of ADF/cofilin by binding to actin filaments results in wider networks growing longer, and iii). ADF/cofilin can control steering of heterogenous branched actin networks.

Although this study is an "extension" of a previous work, all three reviewers found it novel and interesting, and addressing issues that are often brought up but never directly examined, especially not in controlled conditions like here. However, the reviewers identified several important points that need to be addressed in the revised version of the manuscript. These are significant issues, but many of them are conceptual and could be handled without new experiments.

Essential revisions:

1) It seems that, as filaments become decorated by cofilin (eventually reaching saturation, or at least a steady-state level of decoration) the amount of F-actin available to drive further depletion decreases. This seems essential but is never taken into account, nor discussed. In Equations 1 and 2, the binding of cofilin stays proportional to A, which is the total (including already decorated) actin filament density. It is not clear that certain conclusions would hold without this extreme simplification. For instance, beyond a certain network length, the filaments would be saturated and no longer contribute to cofilin depletion. This issue should be thoroughly addressed.

2) The in vitro experiments were performed by using very thin experimental chambers to make the networks flat, similar to the lamellipodial actin filament networks. The 'lengths' of the reconstituted (lamellipodial) actin networks e.g. in Figure 2C are 50 – 90 um, whereas the 'length' of a lamellipodium in most migrating cells, apart from fish keratinocytes, is approximately 1-4 um. Moreover, the sizes of fragments disintegrating from the network (e.g. Figure 4) are often larger than the 'length' of a typical lamellipodium of a migrating cell. Thus, the authors should better discuss whether local depletion of ADF/cofilin by binding to actin filament networks can indeed have major effects on the disassembly/geometry of similar (lamellipodial) actin filament networks also in cells. Moreover, they should discuss whether similar stochastic fragmentation of actin filament networks into small pieces can also occur in cellular actin filament structures (which are much smaller in size, and where ADF/cofilin cooperates with many 'co-factors' such as Aip1 and Srv2/CAP in actin filament disassembly).

3) In their experiments, the authors used yeast cofilin and rabbit muscle actin. We know that this will be a lot less efficient at decorating and severing filaments than if they had used mammalian cofilin. This may explain why such long networks were observed. Moreover, the authors may be in a regime where the filaments are mostly far from cofilin saturation, which would partially validate the crude approximation they make regarding the depletion of cofilin (neglecting the decrease in the number of available sites for cofilin binding on actin filaments; see point 1 above). Therefore, this aspect should be discussed.

4) There are some elements of the mathematics that don't quite make sense. For example, Equation 7 describes the network curvature, using a parameter, "kappa", which is usually defined as the inverse of the radius of curvature. The units of kappa should, therefore, be 1/µm. According to Equation 7, however, the units for kappa are µm. This issue also appears in Figure 6B, where the y-axis is labeled "Curvature Radius" but the units of the dashed line are clearly 1/µm.

More generally, the mathematical modeling assumes that stiffness varies as A^2.5 (subsection “ADF/Cofilin regulates steering of heterogeneous networks”, second paragraph), a result that is derived from the study of random, entangled or crosslinked actin networks. Others have reported a very different concentration dependence for branched actin networks assembled under the sort of boundary conditions used here, namely A^0.5. This much weaker dependence on concentration is consistent with the assumptions made in the previous paper (Boujemaa-Paterski, 2017), and mentioned in the aforementioned paragraph. The authors have the opportunity to use their curvature measurements to independently judge the concentration dependence of the stiffness of branched actin networks.

Minor points follow.

Reviewer #1:

1) The authors state in the 'Discussion' that by using their formulas they can estimate the lamellipodial length in motile cells of intermediate size. Given that their equations do not include other actin filament disassembly factors (e.g. Aip1, coronin, Srv2/cofilin, twinfilin), and other F-actin binding proteins that affect filament disassembly (tropomyosins, filament cross-linking proteins), this does not seem feasible. Therefore, the authors should either omit this part of the discussion or alternatively provide better explanation for how these additional factors were taken into account in these estimations.

2) Many figures are quite complex and thus somewhat difficult to follow. For example, Figure 3 would benefit if the authors would try to simplify it (e.g. by moving any 'non-essential' panels to supplementary information, and by providing more information about each panel in the legend). Moreover, especially the chapters 'Rate of ADF/cofilin binding decreases with time' and 'ADF/cofilin is locally depleted by binding to the growing actin network' would benefit from extensive rewriting to make the conclusions better accessible to a 'non-specialist' reader.

3) ADF/cofilin binds both F-actin and G-actin. Was this taken into account in simulations performed in this study?

4) Definition of the error bar is missing from the legend to Figure 4A.

Reviewer #2:

1) In the simulations (Figure 3D) the amount of free ADF/cofilin in the network decreases only. Is that because the model assumes that the number of binding sites on actin remains constant (see essential point 1)?

2) Subsection “ADF/Cofilin is locally depleted by binding to the growing actin network”, third paragraph; Depletion is computed by considering the global balance over the whole network, in order to describe what happens near the leading edge. This cannot be right, since there are important local variations.

3) In Figure 3A, the initial slopes decrease, but the green curve also seems to plateau much lower than the blue curve. How can that be?

4) Since this work deals with the establishment of steady-state, this aspect should be documented a bit more. The authors mention the increase of the network length, which goes on regularly without ADF/cofilin but reaches and equilibrium length in the presence of ADF/cofilin. The authors should show measurements of L as a function of time.

5) The experimental observation regarding the actin profile, which is relatively constant and plunges only near the trailing edge is somewhat surprising. It can be reproduced by the model, which (as the authors clearly state) crudely simplifies the action of cofilin: network nodes are removed beyond a certain threshold of decoration. The authors discuss (…subsection “Relation to previous studies”, second paragraph) that this is consistent with previous reports on debranching at low cofilin concentrations, however it is well established in the literature that the maximum severing is reached for intermediate levels of cofilin decoration. Also, I believe previous reports on the actin-based propulsion of beads or droplets generally find a more progressive decrease in actin density. This should be discussed more.

6) Some statements in the text are exaggerated: e.g., "this provides a direct demonstration…" (a model matching experimental data does not provide a direct demonstration that the hypothesis is what is actually going on), or, "we made the novel observation that heterogeneous networks grow curved" (already reported in Boujemaa-Paterski, 2017).

Reviewer #3:

1) The title is misleading and should be changed. Firstly, "equilibrium" suggests that the authors are studying a thermodynamic equilibrium rather than a quasi-steady state network treadmilling that carries on for as long as the ATP in the system remains high. Secondly, the title suggests that the novelty of the paper lies in the "reconstitution" of steady-state actin network turnover. As the authors note, this has been reconstituted many times before. The novelty lies in the quantitative approach and some of the mechanistic details that emerge from it.

2) I cannot find any information on the nucleation promoting factor that is patterned on the glass surface and used to generate branched actin networks in this study. In the text and figure captions the molecule is simply described as "an NPF." I don't see it in the Materials and methods either. It might be buried somewhere in the manuscript, but it should be prominent in text and noted in all of the captions for figures containing experimental data. This is important for several reasons: (1) different NPFs have different cellular functions and stimulate different rates of nucleation and polymerization, and (2) it is unclear which domains are in the construct (full-length protein? PWCA? WCA?). In a previous paper (Bougemaa-Paterski, 2017) the authors described their immobilized NPF construct as a GST-pWCA. If this is the same construct, the dimeric nature of the GST would also be significant.

3) Figure 1 demonstrates that micro-patterns with different densities of (an unknown construct of an unknown) NPF promote different velocities of network growth. The result is striking and believable but should be described in more detail. For example, what are the relative densities of the micro-patterned NPFs corresponding to "low," "medium," and "high" densities?

4) On a related note, I disagree with the authors' explanation for the correlation between network density and velocity. They state that: "higher NPF density that causes greater actin density and a moderate depletion of monomeric actin in the vicinity of the growing barbed ends, also leads to an optimization of the micro-architecture of the network, which translates polymerization into the network elongation more effectively for denser networks". I see no evidence to support this claim in either this paper or their previous work (Boujemaa-Paterski, 2017). My (admittedly biased) interpretation is based on the fact that we recently demonstrated that NPF's have a potent polymerase activity that accelerates elongation of nearby filaments. This results in a growth velocity that is directly proportional to the NPF surface density.
