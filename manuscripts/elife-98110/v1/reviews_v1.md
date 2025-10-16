# Peer review - Round 1

Editors:
- Detlef Weigel, Max Planck Institute for Biology Tübingen Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.98110.3.sa0](https://doi.org/10.7554/eLife.98110.3.sa0)

This important manuscript describes a creative approach using dual-component gRNAs to create a new class of molecular proximity sensors for genome editing. The authors demonstrate that this tool can be coupled with several different gene editing effectors, showing convincingly that the tool functions as intended. This study not only introduces a first-of-its kind approach, but through careful measurements also enables future further development of the technology.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98110.3.sa1](https://doi.org/10.7554/eLife.98110.3.sa1)

Summary:

The manuscript by Choi and co-authors presents "P3 editing", which leverages dual-component guide RNAs (gRNA) to induce protein-protein proximity. They explore three strategies for leveraging prime-editing gRNA (pegRNA) as a dimerization module to create a molecular proximity sensor that drives genome editing, splitting a pegRNA into two parts (sgRNA and petRNA), inserting self-splicing ribozymes within pegRNA, and dividing pegRNA at the crRNA junction. Among these, splitting at the crRNA junction proved the most promising, achieving significant editing efficiency. They further demonstrated the ability to control genome editing via protein-protein interactions and small molecule inducers by designing RNA-based systems that form active gRNA complexes. This approach was also adaptable to other genome editing methods like base editing and ADAR-based RNA editing.

Strengths:

The study demonstrates significant advancements in leveraging guide RNA (gRNA) as a dimerization module for genome editing, showcasing its high specificity and versatility. By investigating three distinct strategies-splitting pegRNA into sgRNA and petRNA, inserting self-splicing ribozymes within the pegRNA, and dividing the pegRNA at the repeat junction-the researchers present a comprehensive approach to achieving molecular proximity and reconstituting function. Among these methods, splitting the pegRNA at the repeat junction emerged as the most promising, achieving editing efficiencies up to 76% of the control, highlighting its potential for further development in CRISPR-Cas9 systems. Additionally, the study extends genome editing control by linking protein-protein interactions to RNA-mediated editing, using specific protein-RNA interaction pairs to regulate editing through engineered protein proximity. This innovative approach expands the toolkit for precision genome editing, demonstrating the feasibility of controlling genome editing with enhanced specificity and efficiency.

Weaknesses:

The initial experiments with splitting the pegRNA into sgRNA and petRNA showed low editing efficiency, less than 2%. Similarly, inserting self-splicing ribozymes within pegRNA was inefficient, achieving under 2% editing efficiency in all constructs tested, possibly hindered by the prime editing enzyme. The editing efficiency of the crRNA and petracrRNA split at the repeat junction varied, with the most promising configurations only reaching 76% of the control efficiency. The RNA-RNA duplex formation's inefficiency might be due to the lack of additional protein binding, leading to potential degradation outside the Cas9-gRNA complex. Extending the approach to control genome editing via protein-protein interactions introduced complexity, with a significant trade-off between efficiency and specificity, necessitating further optimization. The strategy combining RADARS and P3 editing to control genome editing with specific RNA expression events exhibited high background levels of non-specific editing, indicating the need for improved specificity and reduced leaky expression. Moreover, P3 editing efficiencies are exclusively quantified after transfecting DNA into HEK cells, a strategy that has resulted in past reproducibility concerns for other technologies. Overall, the various methods and combinations require further optimization to enhance efficiency and specificity, especially when integrating multiple synthetic modules.

Comments on revisions:

I think the authors have successfully addressed the initial concerns. Their adaption of the main text and discussion makes the limitations of P3 editing much clearer.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98110.3.sa2](https://doi.org/10.7554/eLife.98110.3.sa2)

Choi et al. describes a new approach for enabling input-specific CRISPR-based genome editing in cultured cells. While CRISPR-Cas9 is a broadly applied system across all of biology, one limitation is the difficulty in inducing genome editing based on cellular events. A prior study, from the same group, developed ENGRAM - which relies on activity-dependent transcription of a prime editing guide RNA, which records a specific cellular event as a given edit in a target DNA "tape". However, this approach is limited to detection of induced transcription, and does not enable the detection of broader molecular events including protein-protein interactions or exposure to small molecules. As an alternative, this study envisioned engineering the reconstitution of a split prime editing guide RNA (pegRNA) in a protein-protein interaction (PPI)-dependent manner. This would enable location- and content-specific genome editing in a controlled setting.

Strengths:

The strengths of this paper include an interesting concept for engineering guide RNAs to enable activity-dependent genome editing in living cells in the future, based on discreet protein-protein interactions (either constitutively, spatially, or chemically induced). Important groundwork is laid down to engineer and improve these guide RNAs in the future (especially the work describing altering the linkers in Supplementary Figure 3 - which provides a path forward).

Weaknesses:

In its current state, the editing efficiency appears too low to be applied in physiological settings. Much of the latter work in the paper relies on a LambdaN-MCP direction fusion protein, rather than two interacting protein pairs. Further characterizations in the future, especially varying the transfection amounts/durations/etc of the various components of the system, would be beneficial to improve the system. It will also be important to demonstrate editing at additional sites; to characterize how long the PPI must be active to enable efficient prime editing; and how reversible the reconstitution of the split pegRNA is.

In the revised version, the authors clearly describe the present limitations of the system in the discussion section, and also highlight specific actions and potential approaches for improving the efficiency of the system for application in biological systems. They also add further insight into why it is advantageous to design engineered guideRNAs, as opposed to engineered Cas9 enzymes, to improve the modularity of the system in the future.
