# Peer review - Round 1

Editors:
- Qiang Cui, Boston University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.100284.3.sa0](https://doi.org/10.7554/eLife.100284.3.sa0)

In this important study, the authors employed three types of theoretical/computational models (coarse-grained molecular dynamics, analytical theory and field-theoretical simulations) to analyze the impact of salt on protein liquid-liquid phase separation. These different models reinforce each other and together provide convincing evidence to explain distinct salt effects on ATP mediated phase separation of different variants of caprin1. The insights and general approach are broadly applicable to the analysis of protein phase separation. Still, modeling at the coarse-grained level misses key effects that have been revealed by all-atom simulations, including salt-backbone coordination and strengthening of pi-type interactions by salt.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.100284.3.sa1](https://doi.org/10.7554/eLife.100284.3.sa1)

Summary:

The authors used multiple approaches to study salt effects in liquid-liquid phase separation (LLPS). Results on both wild-type Caprin1 and mutants and on different types of salts contribute to a comprehensive understanding.

Strengths:

The main strength of this work is the thoroughness of investigation. This aspect is highlighted by the multiple approaches used in the study, and reinforced by the multiple protein variants and different salts studied.

Weaknesses:

(1) The multiple computational approaches are a strength, but they're cruder than explicit-solvent all-atom molecular dynamics (MD) simulations and may miss subtle effects of salts. In particular, all-atom MD simulations demonstrate that high salt strengthens pi-types of interactions (ref. 42 and MacAinsh et al, https://www.biorxiv.org/content/10.1101/2024.05.26.596000v3).

(2) The paper can be improved by distilling the various results into a simple set of conclusions. By example, based on salt effects revealed by all-atom MD simulations, MacAinsh et al. presented a sequence-based predictor for classes of salt dependence. Wild-type Caprin1 fits right into the "high net charge" class, with a high net charge and a high aromatic content, showing no LLPS at 0 NaCl and an increasing tendency of LLPS with increasing NaCl. In contrast, pY-Caprin1 belongs to the "screening" class, with a high level of charged residues and showing a decreasing tendency of LLLPS.

(3) Mechanistic interpretations can be further simplified or clarified. (i) Reentrant salt effects (e.g., Fig. 4a) are reported but no simple explanation seems to have been provided. Fig. 4a,b look very similar to what has been reported as strong-attraction promotor and weak-attraction suppressor, respectively (ref. 50; see also PMC5928213 Fig. 2d,b). According to the latter two studies, the "reentrant" behavior of a strong-attraction promotor, CL- in the present case, is due to Cl-mediated attraction at low to medium [NaCl] and repulsion between Cl- ions at high salt. Do the authors agree with this explanation? If not, could they provide another simple physical explanation? (ii) The authors attributed the promotional effect of Cl- to counterion-bridged interchain contacts, based on a single instance. There is another simple explanation, i.e., neutralization of the net charge on Caprin1. The authors should analyze their simulation results to distinguish net charge neutralization and interchain bridging; see MacAinsh et al.

(4) The authors presented ATP-Mg both as a single ion and as two separate ions; there is no explanation of which of the two versions reflects reality. When presenting ATP-Mg as a single ion, it's as though it forms a salt with Na+. I assume NaCl, ATP, and MgCl2 were used in the experiment. Why is Cl- not considered? Related to this point, it looks ATP is just another salt ion studied and much of the Results section is on NaCl, so the emphasis of ATP "Diverse Roles of ATP" in the title is somewhat misleading.

Comments on revisions:

This revision addressed all my previous comments.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.100284.3.sa2](https://doi.org/10.7554/eLife.100284.3.sa2)

Summary:

In this paper, Lin and colleagues aim to understand the role of different salts on the phase behavior of a model protein of significant biological interest, Caprin1, and its phosphorylated variant, pY-Caprin1. To achieve this, the authors employed a variety of methods to complement experimental studies and obtain a molecular-level understanding of ion partitioning inside biomolecular condensates. A simple theory based on rG-RPA is shown to capture the different salt dependencies of Caprin1 and pY-Caprin1 phase separation, demonstrating excellent agreement with experimental results. The application of this theory to multivalent ions reveals many interesting features with the help of multicomponent phase diagrams. Additionally, the use of CG model-based MD simulations and FTS provides further clarity on how counterions can stabilize condensed phases.

Strengths:

The greatest strength of this study lies in the integration of various methods to obtain complementary information on thermodynamic phase diagrams and the molecular details of the phase separation process. The authors have also extended their previously proposed theoretical approaches, which should be of significant interest to other researchers. Some of the findings reported in this paper, such as bridging interactions, are likely to inspire new studies using higher-resolution atomistic MD simulations.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.100284.3.sa3](https://doi.org/10.7554/eLife.100284.3.sa3)

Authors first use rG-RPA to reproduce two observed trends. Caprin1 does not phase separate at very low salt but then undergoes LLPS with added salt while further addition of salt reduces its propensity to LLPS. On the other hand pY-Caprin1 exhibits a monotonic trend where the propensity to phase separate decreases with the addition of salt. This distinction is captured by a two component model and also when salt ions are explicitly modeled as a separate species with a ternary phase diagram. The predicted ternary diagrams (when co and counter ions are explicitly accounted for) also predict the tendency of ions to co-condense or exclude proteins in the dense phase. Predicted trends are generally in line with the measurement for Cparin1. Next, the authors seek to explain the observed difference in phase separation when Arginines are replaced by Lysines creating different variants. In the current rG-RPA type models both Arginine (R) and Lysine (K) are treated equally since non-electrostatic effects are only modeled in a mean-field manner that can be fitted but not predicted. For this reason, coarse grain MD simulation is suitable. Moreover, MD simulation affords structural features of the condensates. They used a force field that is capable of discriminating R and K. The MD predicted degrees of LLPS of these variants again is consistent with the measurement. One additional insight emerges from MD simulations that a negative ion can form a bridge between two positively charged residues on the chain. These insights are not possible to derive from rG-RPA. Both rG-RPA and MD simulation become cumbersome when considering multiple types of ions such as Na, Cl, [ATP] and [ATP-Mg] all present at the same time. FTS is well suited to handle this complexity. FTS also provides insights into the co-localization of ions and proteins that is consistent with NMR. By using different combinations of ions they confirm the robustness of the prediction that Caprin1 shows salt-dependent reentrant behavior, adding further support that the differential behavior of Caprin1, and pY-Caprin1 is likely to be mediated by charge-charge interactions.

Comments on revisions:

The authors addressed my comments and it is ready for publication.
