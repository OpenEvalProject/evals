# Peer review - Round 1

Editors:
- Qiang Cui, Boston University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.100282.3.sa0](https://doi.org/10.7554/eLife.100282.3.sa0)

In this potentially important study, the authors conducted atomistic simulations to probe the salt-dependent phase separation of the low-complexity domain of hnRN-PA1 (A1-LCD). The authors have identified both direct and indirect mechanisms of salt modulation, provided explanations for four distinct classes of salt dependence, and proposed a model for predicting protein properties from amino acid composition. There is a range of opinions regarding the strength of evidence, with some considering the evidence as incomplete due to the limitations in the length and statistical errors of the computationally intense atomistic MD simulations.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.100282.3.sa1](https://doi.org/10.7554/eLife.100282.3.sa1)

Summary:

The authors examined the salt-dependent phase separation of the low-complexity domain of hnRN-PA1 (A1-LCD). Using all-atom molecular dynamics simulations, they identified four distinct classes of salt dependence in the phase separation of intrinsically disordered proteins (IDPs), which can be predicted based on their amino acid composition. However, the simulations and analysis, in their current form, are inadequate and incomplete.

Strengths:

The authors attempt to unravel the mechanistic insights into the interplay between salt and protein phase separation, which is important given the complex behavior of salt effects on this process. Their effort to correlate the influence of salt on the low-complexity domain of hnRNPA1 (A1-LCD) with a range of other proteins known to undergo salt-dependent phase separation is an interesting and valuable topic.

Weaknesses:

Based on the reviewer's assessment of the manuscript, the following points were raised:

(1) The simulation duration is too short to draw comprehensive conclusions about phase separation.

(2) There are concerns regarding the convergence of the simulations, particularly as highlighted in Figure 2A.

(3) The simulation begins with a protein concentration of 3.5 mM ("we built an 8-copy model for the dense phase (with an initial concentration of 3.5 mM)"), which is high for phase separation studies. The reviewer questions the use of the term "dense phase" and suggests that the authors conduct a clearer analysis depicting the coexistence of both the dilute and dense phases to represent a steady state. Without this, the realism of the described phenomena is doubtful. Commenting on phase separation under conditions that don't align with typical phase separation parameters is not acceptable.

(4) The inference that "Each Arg sidechain often coordinates two Cl- ions simultaneously, but each Lys sidechain coordinates only one Cl- ion" is questioned. According to Supplementary Figure 2A, Lys seems to coordinate with Cl- ions more frequently than Arg.

(5) The authors are requested to update the figure captions for Supplementary Figures 2 and 3, specifying which system the analyses were performed on.

(6) It is difficult to observe a clear trend due to irregularities in the data. Although the authors have included a red dotted line in the figures, the trend is not monotonic. The reviewer expresses concerns about significant conclusions drawn from these figures (e.g., Figure 2C, Figure 5A, Supplementary Figure 1).

(7) Given the error in the radius of gyration (Rg) calculations, the reviewer questions the validity of drawing conclusions from this data.

(8) The pair correlation function values in Figure 5E and supplementary figure 4 show only minor differences, and the reviewer questions whether these differences are significant.

(9) Previous reports suggest that, upon self-assembly, protein chains extend within the condensate, leading to a decrease in intramolecular contacts. However, the authors show an increase in intramolecular contacts with increasing salt concentration (Figure 2C), which contradicts prior studies. The reviewer advises the authors to carefully review this and provide justification.

(10) A systematic comparison of estimated parameters with varying salt concentrations is required. Additionally, the authors should provide potential differences in salt concentrations between the dilute and condensed phases.

(11) The reviewer finds that the majority of the data presented shows no significant alteration with changes in salt concentration, yet the authors have made strong conclusions regarding salt activity.

The manuscript lacks sufficient scientific details of the calculations.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.100282.3.sa2](https://doi.org/10.7554/eLife.100282.3.sa2)

This is an interesting computational study addressing how salt affects the assembly of biomolecular condensates. The simulation data are valuable as they provide a degree of atomistic details regarding how small salt ions modulate interactions among intrinsically disordered proteins with charged residues, namely via Debye-like screening that weakens the effective electrostatic interactions among the polymers, or through bridging interactions that allow interactions between like charges from different polymer chains to become effectively attractive (as illustrated, e.g., by the radial distribution functions in Supplementary Information). However, this manuscript has several shortcomings: (i) Connotations of the manuscript notwithstanding, many of the authors' concepts about salt effects on biomolecular condensates have been put forth by theoretical models, at least back in 2020 and even earlier. Those earlier works afford extensive information such as considerations of salt concentrations inside and outside the condensate (tie-lines). But the authors do not appear to be aware of this body of prior works and therefore missed the opportunity to build on these previous advances and put the present work with its complementary advantages in structural details in the proper context. (ii) There are significant experimental findings regarding salt effects on condensate formation [which have been modeled more recently] that predate the A1-LCD system (ref.19) addressed by the present manuscript. This information should be included, e.g., in Table 1, for sound scholarship and completeness. (iii) The strengths and limitations of the authors' approach vis-à-vis other theoretical approaches should be discussed with some degree of thoroughness (e.g., how the smallness of the authors' simulation system may affect the nature of the "phase transition" and the information that can be gathered regarding salt concentration inside vs. outside the "condensate" etc.).

Comments on revised version:

The authors have adequately addressed my previous concerns and suggestions. The manuscript is now significantly improved. The new results and analyses provided by the authors represent a substantial advance in our understanding of the role of electrostatics in the assembly of biomolecular condensates.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.100282.3.sa3](https://doi.org/10.7554/eLife.100282.3.sa3)

Summary:

This study investigates the salt-dependent phase separation of A1-LCD, an intrinsically disordered region of hnRNPA1 implicated in neurodegenerative diseases. The authors employ all-atom molecular dynamics (MD) simulations to elucidate the molecular mechanisms by which salt influences A1-LCD phase separation. Contrary to typical intrinsically disordered protein (IDP) behavior, A1-LCD phase separation is enhanced by NaCl concentrations above 100 mM. The authors identify two direct effects of salt: neutralization of the protein's net charge and bridging between protein chains, both promoting condensation. They also uncover an indirect effect, where high salt concentrations strengthen pi-type interactions by reducing water availability. These findings provide a detailed molecular picture of the complex interplay between electrostatic interactions, ion binding, and hydration in IDP phase separation.

Strengths:

• Novel Insight: The study challenges the prevailing view that salt generally suppresses IDP phase separation, highlighting A1-LCD's unique behavior.

• Rigorous Methodology: The authors utilize all-atom MD simulations, a powerful computational tool, to investigate the molecular details of salt-protein interactions.

• Comprehensive Analysis: The study systematically explores a wide range of salt concentrations, revealing a nuanced picture of salt effects on phase separation.

• Clear Presentation: The manuscript is well-written and logically structured, making the findings accessible to a broad audience.

Weaknesses:

• Limited Scope: The study focuses solely on the truncated A1-LCD, omitting simulations of the full-length protein. This limitation reduces the study's comparative value, as the authors note that the full-length protein exhibits typical salt-dependent behavior. However, given the much larger size of the full-length protein, it is acceptable to omit it given the current computing resources available.

Overall, this manuscript represents a significant contribution to the field of IDP phase separation. The authors' findings provide valuable insights into the molecular mechanisms by which salt modulates this process, with potential implications for understanding and treating neurodegenerative diseases.
