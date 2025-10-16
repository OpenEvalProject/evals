# Peer review - Round 1

Editors:
- Frank Chan, University of Groningen Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.97764.3.sa0](https://doi.org/10.7554/eLife.97764.3.sa0)

This study provides a valuable new resource to investigate the molecular basis of the particular features characterizing the pipefish embryo. The authors found both unique and shared gene expression patterns in pipefish organs compared with other teleost fishes. The solid data collected in this unconventional model organism will give new insights into understanding the extraordinary adaptations of the Syngnathidae family and will be of interest in the domain of evolution of fish development.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97764.3.sa1](https://doi.org/10.7554/eLife.97764.3.sa1)

Syngnathid fishes (seahorses, pipefishes, and seadragons) present very particular and elaborated features among teleosts and a major challenge is to understand the cellular and molecular mechanisms that permitted such innovations and adaptations. The study provides a valuable new resource to investigate the morphogenetic basis of four main traits characterizing syngnathids, including the elongated snout, toothlessness, dermal armor and male pregnancy. More particularly, the authors have focused on a late stage of pipefish organogenesis to perform single-cell RNA-sequencing (scRNA-seq) completed by in situ hybridization analyses to identify molecular pathways implicated in the formation of the different specific traits.

The first set of data explores the scRNA-seq atlas composed of 35,785 cells from two samples of gulf pipefish embryos that authors have been able to classify into major cell types characterizing vertebrate organogenesis, including epithelial, connective, neural and muscle progenitors. To affirm identities and discover potential properties of clusters, authors primarily use KEGG analysis that reveals enriched genetic pathways in each cell types. After revisions, the authors have provided extended supplementary files to well interpret the dataset and some statements have been clarified. I thank the authors for the revisions/completions of ISH results compared to initial submission.

To conclude, the scRNA-seq dataset in this unconventional model organism will be useful for the community and will provide clues for future research to understand the extraordinary evolution of the Syngnathidae family.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97764.3.sa2](https://doi.org/10.7554/eLife.97764.3.sa2)

Summary:

The authors present the first single-cell atlas for syngathid fishes, providing a resource for future evolution & development studies in this group.

Strengths:

The concept here is simple and I find the manuscript to be well written. I like the in situ hybridization of marker genes >> this is really nice. I also appreciate the gene co-expression analysis to identify modules of expression. There are no explicit hypotheses tested in the manuscript, but the discovery of these cell types should have value in this organism and in the determination of morphological novelties in seahorses and their relatives.

Weaknesses:

I think there are a few computational analyses that might improve the generality of the results.

(1) The cell types: The authors use marker gene analysis and KEGG pathways to identify cell types. I'd suggest a tool like SAMap (https://elifesciences.org/articles/66747) which compares single cell data sets from distinct organisms to identify 'homologous' cell types -- I imagine the zebrafish developmental atlases could serve as a reasonable comparative reference.

(2) Trajectory analyses: Authors suggest that their analyses might identify progenitor cell states and perhaps related differentiated states. They might explore cytoTRACE and/or pseudotime-based trajectory analyses to more fully delineate these ideas.

(3) Cell-cell communication: I think it's very difficult to identify 'tooth primordium' cell types, because cell types won't be defined by organ in this way. for instance dental glia will cluster with other glia, dental mesenchyme will likely cluster with other mesenchymal cell types. so the histology and ISH in most convincing in this regard. having said this, given the known signaling interactions in the developing tooth (and in development generally) the authors might explore cell-cell communication analysis (e.g., CellChat) to identify cell types that may be interacting.

Comments on revisions:

I feel essentially the same about this manuscript. it's a useful resource for future experimental forays into this unique system. The team made improvements to deal with comments from other reviewers related to quality of confirmatory in situ hybridization. This is good.

Regarding their response that one can't use CellChat if you're not working in mice or human, this is inaccurate. the assumption one makes is that ligand-receptor pairs and signaling pathways have conserved functions across animals (vertebrates). It's the same assumption the authors make when using the KEGG pathway to score enrichment of pathways in clusters. CellChat used in fishes in Johnson et al 2023 Nature Communications | (2023) 14:4891.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97764.3.sa3](https://doi.org/10.7554/eLife.97764.3.sa3)

Summary:

This study established a single-cell RNA sequencing atlas of pipefish embryos. The results obtained identified unique gene expression patterns for pipefish-specific characteristics, such as fgf22 in the tip of the palatoquadrate and Meckel's cartilage, broadly informing the genetic mechanisms underlying morphological novelty in teleost fishes. The data obtained are unique and novel, potentially important in understanding fish diversity. Thus, I would enthusiastically support this manuscript if the authors improve it to generate stronger and more convincing conclusions than the current forms.

Weakness:

Regarding the expression of sfrp1a and bmp4 dorsal to the elongating ethmoid plate and surrounding the ceratohyal: Are their expression patterns spatially extended or broader compared to the pipefish ancestor? Is there a much closer species available to compare gene expression patterns with pipefish? Did the authors consider using other species closely related to pipefish for ISH? Sfrp1a and bmp4 may be expressed in the same regions of much more closely related species without face elongation. I understand that embryos of such species are not always accessible, but it is also hard to argue responsible genes for a specific phenotype by only comparing gene expression patterns between distantly related species (e.g., pipefish vs. zebrafish). Due to the same reason, I would not directly compare/argue gene expression patterns between pipefish and mice, although I should admit that mice gene expression patterns are sometimes helpful to make a hypothesis of fish evolution. Alternatively, can the authors conduct ISH in other species of pipefish? If the expression patterns of sfrp1a and bmp4 are common among fishes with face elongation, the conclusion would become more solid. If these embryos are not available, is it possible to reduce the amount of Wnt and BMP signal using Crispr/Cas, MO, or chemical inhibitor? I do think that there are several ways to test the Wnt and/or BMP hypothesis in face elongation.
