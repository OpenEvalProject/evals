# Peer review - Round 1

Editors:
- Kenichi Tsuda, Huazhong Agricultural University China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.105185.3.sa0](https://doi.org/10.7554/eLife.105185.3.sa0)

This study presents an important discovery regarding the diversity and evolution of gall-forming microbial effectors. Supported by convincing computational structural predictions and analyses, the research provides insights into the unique mechanisms by which gall-forming microbes exert their pathogenicity in plants. This study also offers guidance that is of value for future studies on pathogen effector function and co-evolution with host plants.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105185.3.sa1](https://doi.org/10.7554/eLife.105185.3.sa1)

Summary:

This manuscript presents a comprehensive structure-guided secretome analysis of gall-forming microbes, providing valuable insights into effector diversity and evolution. The authors have employed AlphaFold2 to predict the 3D structures of the secretome from selected pathogens and conducted a thorough comparative analysis to elucidate commonalities and unique features of effectors among these phytopathogens.

Strengths:

The discovery of conserved motifs such as 'CCG' and 'RAYH' and their central role in maintaining the overall fold is an insightful finding. Additionally, the discovery of a nucleoside hydrolase-like fold conserved among various gall-forming microbes is interesting.

Weaknesses:

Important conclusions are not verified by experiments.

Comments on revisions: I acknowledge the authors' revision efforts.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105185.3.sa2](https://doi.org/10.7554/eLife.105185.3.sa2)

Summary:

Soham Mukhopadhyay et al. investigated the protein folding of the secretome from gall-forming microbes using the AI-based structure-modeling tool AlphaFold2. Their study analyzed six gall-forming species, including two Plasmodiophorid species and four others spanning different kingdoms, along with one non-gall-forming Plasmodiophorid species, Polymyxa betae. The authors found no effector fold specifically conserved among gall-forming pathogens, leading to the conclusion that their virulence strategies are likely achieved through diverse mechanisms. However, they identified an expansion of the Ankyrin repeat family in two gall-forming Plasmodiophorid species, with a less pronounced presence in the non-gall-forming Polymyxa betae. Additionally, the study revealed that known effectors such as CCG and AvrSen1 belong to sequence-unrelated but structurally similar (SUSS) effector clusters.

Strengths:

(1) The bioinformatics analyses presented in this study are robust, and the AlphaFold2-derived resources deposited in Zenodo provide valuable resources for researchers studying plant-microbe interactions. The manuscript is also logically organized and easy to follow.

(2) The inclusion of the non-gall-forming Polymyxa betae strengthens the conclusion that no effector fold is specifically conserved in gall-forming pathogens and highlights the specific expansion of the Ankyrin repeat family in gall-forming Plasmodiophorids.

(3) Figure 4a and 4b effectively illustrate the SUSS effector clusters, providing a clear visual representation of this finding.

(4) Figure 1 is a well-designed, comprehensive summary of the number and functional annotations of putative secretomes in gall-forming pathogens. Notably, it reveals that more than half of the analyzed effectors lack known protein domains in some pathogens, yet some were annotated based on their predicted structures, despite the absence of domain annotations.

Weaknesses:

(1) The effector families discussed in this paper remain hypothetical in terms of their functional roles, which is understandable given the challenges of demonstrating their functions experimentally. However, this highlights the need for experimental validation as a next step.

Authors' response: Thank you. Yes, there is a lot of work to do in the coming years.

Reviewer's response: Incorporating experimental validation substantially strengthened the manuscript. Did you try the AlphaFold-Multimer prediction of the interaction between PBTT_00818 and the GroES-like protein? Does the model indicate a high-confidence interface?

(2) Some analyses, such as those in Figure 4e, emphasize motifs derived from sequence alignments of SUSS effector clusters. Since these effectors are sequence-unrelated, sequence alignments might be unreliable. It would be more rigorous to perform structure-based alignments in addition to sequence-based ones for motif confirmation. For instance, methods described in Figure 3E of de Guillen et al. (2015, https://doi.org/10.1371/journal.ppat.1005228) or tools like Foldseek could be useful for aligning structures of multiple sequences.

Authors' response: In Fig. 4e, we highlight the conserved cysteine residues. While there is no clearly conserved overall motif, the figure illustrates that despite the high sequence divergence, the key cysteines involved in disulfide-bridge formation are consistently conserved across the sequences.

Reviewer's response: Understood. Nevertheless, if a reliable sequence alignment can indeed be generated, I would interpret this to mean that the CCG effectors constitute a highly diversified family rather than being truly sequence unrelated. By comparison, members of the MAX effector family share a common fold, yet their sequences are so divergent that sequence alignment is impossible.

(3) When presenting AlphaFold-generated structures, it is essential to include confidence scores such as pLDDT and PAE. For example, in Figure 1D of Derbyshire and Raffaele (2023, https://doi.org/10.1038/s41467-023-40949-9), the structural representations were colored red due to their high pLDDT scores, emphasizing their reliability.

Authors' response: Thank you for the observation. Due to the restrictive parameters used in our analysis, over 90 % of the structure would appear red. For this reason, we chose not to include the color scale, as it would not provide additional informative value in this context.

Reviewer's response: Understood.
