# Peer review - Round 1

Editors:
- Johannes Herrmann, University of Kaiserslautern Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.99572.3.sa0](https://doi.org/10.7554/eLife.99572.3.sa0)

This convincing study advances our understanding of the physiological consequences of the strong overexpression of non-toxic proteins in baker's yeast. The findings suggest that a massive protein burden results in nitrogen starvation and a shift in metabolism likely regulated via the TORC1 pathway, as well as defects in ribosome biogenesis in the nucleolus. The study presents findings and tools that are important for the cell biology and protein homeostasis fields.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99572.3.sa1](https://doi.org/10.7554/eLife.99572.3.sa1)

Summary:

The study "Impact of Maximal Overexpression of a Non-toxic Protein on Yeast Cell Physiology" by Fujita et al. aims to elucidate the physiological impacts of overexpressing non-toxic proteins in yeast cells. By identifying model proteins with minimal cytotoxicity, the authors claim to provide insights into cellular stress responses and metabolic shifts induced by protein overexpression.

Strengths:

The study introduces a neutrality index to quantify cytotoxicity and investigates the effects of protein burden on yeast cell physiology. The study identifies mox-YG (a non-fluorescent fluorescent protein) and Gpm1-CCmut (an inactive glycolytic enzyme) as proteins with the lowest cytotoxicity, capable of being overexpressed to more than 40% of total cellular protein while maintaining yeast growth. Overexpression of mox-YG leads to a state resembling nitrogen starvation probably due to TORC1 inactivation, increased mitochondrial function, and decreased ribosomal abundance, indicating a metabolic shift towards more energy-efficient respiration and defects in nucleolar formation.

Weaknesses:

While the introduction of the neutrality index seems useful to differentiate between cytotoxicity and protein burden, the biological relevance of the effects of overexpression of the model proteins is unclear.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99572.3.sa2](https://doi.org/10.7554/eLife.99572.3.sa2)

Summary:

In this manuscript, Fujita et al. characterized the neutrality indexes of several protein mutants in S. cerevisiae and uncovered that mox-YG and Gpm1-CCmut can be expressed as abundant as 40% of total proteins without causing severe growth defects. The authors then looked at the transcriptome and proteome of cells expressing excess mox-YG to investigate how protein burden affects yeast cells. Based on RNA-seq and mass-spectrometry results, the authors uncover that cells with excess mox-YG exhibit nitrogen starvation, respiration increase, inactivated TORC1 response, and decreased ribosomal abundance. The authors further showed that the decreased ribosomal amount is likely due to nucleoli defects, which can be partially rescued by nuclear exosome mutations.

Strengths:

Overall, this is a well-written manuscript that provides many valuable resources for the field, including the neutrality analysis on various fluorescent proteins and glycolytic enzymes, as well as the RNA-seq and proteomics results of cells overexpressing mox-YG. Their model on how mox-YG overexpression impairs the nucleolus and thus leads to ribosomal abundance decline will also raise many interesting questions for the field.

Weaknesses:

The authors concluded from their RNA-seq and proteomics results that cells with excess mox-YG expression showed increased respiration and TORC1 inactivation. I think it will be more convincing if the authors can show some characterization of mitochondrial respiration/membrane potential and the TOR responses to further verify their -omic results.

In addition, the authors only investigated how overexpression of mox-YG affects cells. It would be interesting to see whether overexpressing other non-toxic proteins causes similar effects, or if there are protein-specific effects. It would be good if the authors could at least discuss this point considering the workload of doing another RNA-seq or mass-spectrum analysis might be too heavy.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99572.3.sa3](https://doi.org/10.7554/eLife.99572.3.sa3)

Summary:

Protein overexpression is widely used in experimental systems to study the function of the protein, assess its (beneficial or detrimental) effects in disease models, or challenge cellular systems involved in synthesis, folding, transport, or degradation of proteins in general. Especially at very high expression levels, protein-specific effects and general effects of a high protein load can be hard to distinguish. To overcome this issue, Fujita et al. use the previously established genetic tug-of-war system to identify proteins that can be expressed at extremely high levels in yeast cells with minimal protein-specific cytotoxicity (high 'neutrality'). They focus on two versions of the protein mox-GFP, the fluorescent version and a point mutation that is non-fluorescent (mox-YG) and is the most 'neutral' protein on their screen. They find that massive protein expression (up to 40% of the total proteome) results in a nitrogen starvation phenotype, likely inactivation of the TORC1 pathway, and defects in ribosome biogenesis in the nucleolus.

Strengths:

This work uses an elegant approach and succeeds in identifying proteins that can be expressed at surprisingly high levels with little cytotoxicity. Many of the changes they see have been observed before under protein burden conditions, but some are new and interesting. This work solidifies previous hypotheses about the general effects of protein overexpression and provides a set of interesting observations about the toxicity of fluorescent proteins (that is alleviated by mutations that render them non-fluorescent) and metabolic enzymes (that are less toxic when mutated into inactive versions).

Weaknesses:

The data are generally convincing, however in order to back up the major claim of this work - that the observed changes are due to general protein burden and not to the specific protein or condition - a broader analysis of different conditions would be highly beneficial.

Major points:

(1) The authors identify several proteins with high neutrality scores but only analyze the effects of mox/mox-YG overexpression in depth. Hence, it remains unclear which molecular phenotypes they observe are general effects of protein burden or more specific effects of these specific proteins. To address this point, a proteome (and/or transcriptome) of at least a Gpm1-CCmut expressing strain should be obtained and compared to the mox-YG proteome. Ideally, this analysis should be done simultaneously on all strains to achieve a good comparability of samples, e.g. using TMT multiplexing (for a proteome) or multiplexed sequencing (for a transcriptome). If feasible, the more strains that can be included in this comparison, the more powerful this analysis will be and can be prioritized over depth of sequencing/proteome coverage.

(2) The genetic tug-of-war system is elegant but comes at the cost of requiring specific media conditions (synthetic minimal media lacking uracil and leucine), which could be a potential confound, given that metabolic rewiring, and especially nitrogen starvation are among the observed phenotypes. I wonder if some of the changes might be specific to these conditions. The authors should corroborate their findings under different conditions. Ideally, this would be done using an orthogonal expression system that does not rely on auxotrophy (e.g. using antibiotic resistance instead) and can be used in rich, complex mediums like YPD. Minimally, using different conditions (media with excess or more limited nitrogen source, amino acids, different carbon source, etc.) would be useful to test the robustness of the findings towards changes in media composition.

(3) The authors suggest that the TORC1 pathway is involved in regulating some of the changes they observed. This is likely true, but it would be great if the hypothesis could be directly tested using an established TORC1 assay.

(4) The finding that the nucleolus appears to be virtually missing in mox-YG-expressing cells (Figure 6B) is surprising and interesting. The authors suggest possible mechanisms to explain this and partially rescue the phenotype by a reduction-of-function mutation in an exosome subunit. I wonder if this is specific to the mox-YG protein or a general protein burden effect, which the experiments suggested in point 1 should address. Additionally, could a mox-YG variant with a nuclear export signal be expressed that stays exclusively in the cytosol to rule out that mox-YG itself interferes with phase separation in the nucleus?

Minor points:

(5) It would be great if the authors could directly compare the changes they observed at the transcriptome and proteome levels. This can help distinguish between changes that are transcriptionally regulated versus more downstream processes (like protein degradation, as proposed for ribosome components).
