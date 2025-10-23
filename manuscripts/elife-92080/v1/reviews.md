# Peer review - Round 1

Editors:
- Jessica Dubois, Inserm Unité NeuroDiderot, Université Paris Cité France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.92080.4.sa0](https://doi.org/10.7554/eLife.92080.4.sa0)

This study presents valuable framework and findings to our understanding of the brain cortex as a fractal object. Based on detailed methodology, the evidence provided on the stability of its shape property within 11 primate species is convincing, as well as the scale-specific effects of ageing on the human brain. This study will be of interest to neuroscientists interested in brain morphology, and to physicists and mathematicians interested in modeling the shapes of complex objects.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92080.4.sa1](https://doi.org/10.7554/eLife.92080.4.sa1)

In this manuscript, the authors analyze the shapes of cerebral cortices from several primate species, including subgroups of young and old humans, to characterize commonalities in patterns of gyrification, cortical thickness, and cortical surface area. The authors state that the observed scaling law shares properties with fractals, where shape properties are similar across several spatial scales. One way the authors assess this is to perform a "cortical melting" operation that they have devised on surface models obtained from several primate species. The authors also explore differences in shape properties between brains of young (~20 year old) and old (~80) humans. A challenge the authors acknowledge struggling with in reviewing the manuscript is merging "complex mathematical concepts and a perplexing biological phenomenon." This reviewer remains a bit skeptical about whether the complexity of the mathematical concepts being drawn from are justified by the advances made in our ability to infer new things about the shape of the cerebral cortex.

(1) The series of operations to coarse-grain the cortex illustrated in Figure 1 produces image segmentations that do not resemble real brains. The process to assign voxels in downsampled images to cortex and white matter is biased towards the former, as only 4 corners of a given voxel are needed to intersect the original pial surface, but all 8 corners are needed to be assigned a white matter voxel. The reason for introducing this bias (and to the extent that it is present in the authors' implementation) is not provided. The authors provide an intuitive explanation of why thickness relates to folding characteristics, but ultimately an issue for this reviewer is, e.g., for the right-most panel in Figure 2b, the cortex consists of several 4.9-sided voxels and thus a >2 cm thick cortex. A structure with these morphological properties is not consistent with the anatomical organization of typical mammalian neocortex.

(2) For the comparison between 20-year-old and 80-year-old brains, a well-documented difference is that the older age group possesses more cerebral spinal fluid due to tissue atrophy, and the distances between the walls of gyri becomes greater. This difference is born out in the left column of Figure 4b. It seems this additional spacing between gyri in 80 year olds requires more extensive down-sampling (larger scale values in Figure 4a) to achieve a similar shape parameter K as for the 20 year olds. The authors assert that K provides a more sensitive measure (associated with a large effect size) than currently used ones for distinguishing brains of young vs. old people. A more explicit, or elaborate, interpretation of the numbers produced in this manuscript, in terms of brain shape, might make this analysis more appealing to researchers in the aging field.

(3) In the Discussion, it is stated that self-similarity, operating on all length scales, should be used as a test for existing and future models of gyrification mechanisms. Given the lack of association between the abstract mathematical parameters described in this study and explicit properties of brain tissue and its constituents, it is difficult to envision how the coarse-graining operation can be used to guide development of "models of cortical gyrification."

(4) There are several who advocate for analyzing cortical mid-thickness surfaces, as the pial surface over-represents gyral tips compared to the bottoms of sulci in the surface area. The authors indicate that analyses of mid-thickness representations will be taken on in future work, but this seems to be a relevant control for accepting the conclusions of this manuscript.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92080.4.sa2](https://doi.org/10.7554/eLife.92080.4.sa2)

Summary: Through a rigorous methodology, the authors demonstrated that within 11 different primates, the shape of the brain followed a universal scaling law with fractal properties. They enhanced the universality of this result by showing the concordance of their results with a previous study investigating 70 mammalian brains, and the discordance of their results with other folded objects that are not brains. They incidentally illustrated potential applications of this fractal property of the brain by observing a scale-dependant effect of aging on the human brain.

Strengths:

- New hierarchical way of expressing cortical shapes at different scales derived from previous report through implementation of a coarse-graining procedure

- Investigation of 11 primate brains and contextualisation with other mammals based on prior literature

- Proposition of tool to analyse cortical morphology requiring no fine tuning and computationally achievable

- Positioning of results in comparison to previous works reinforcing the validity of the observation.

- Illustration of scale-dependance of effects of brain aging in the human.

Weaknesses:

- The notion of cortical shape, while being central to the article, is not really defined, leaving some interpretation to the reader

- The organization of the manuscript is unconventional, leading to mixed contents in different sections (sections mixing introduction and method, methods and results, results and discussion...). As a result, the reader discovers the content of the article along the way, it is not obvious at what stages the methods are introduced, and the results are sometimes presented and argued in the same section, hindering objectivity.

To improve the document, I would suggest a modification and restructuring of the article such that: (1) by the end of the introduction the reader understands clearly what question is addressed and the value it holds for the community, (2) by the end of the methods the reader understands clearly all the tools that will be used to answer that question (not just the new method), (3) by the end of the results the reader holds the objective results obtained by applying these tools on the available data (without subjective interpretations and justifications), and (4) by the end of the discussion the reader understands the interpretation and contextualisation of the study, and clearly grasps the potential of the method depicted for the better understanding of brain folding mechanisms and properties.
