# Peer review - Round 1

Editors:
- Benjamin R Kanter, Norwegian University of Science and Technology Norway

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.95733.3.sa0](https://doi.org/10.7554/eLife.95733.3.sa0)

This important paper provides solid evidence for an alternative conceptualization of the functional role of the place and grid cell network in the medial temporal lobe for memory as opposed to spatial processing or navigation. The theory is extensive, tightly integrating data on various spatial cell types. It accounts for many experimental results and generates strong predictions for future studies that will be of interest to researchers in this field. The impact of the work would be strengthened if future experiments reveal that grid cells do indeed encode specific nonspatial features.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.95733.3.sa1](https://doi.org/10.7554/eLife.95733.3.sa1)

Huber proposes a theory where the role of the medial temporal lobe (MTL) is memory, where properties of spatial cells in the MTL can be explained through memory function rather than spatial processing or navigation. Instantiating the theory through a computational model, the author shows that many empirical phenomena of spatial cells can be captured, and may be better accounted through a memory theory. It is an impressive computational account of MTL cells with a lot of theoretical reasoning and aims to tightly relate to various spatial cell data.

In general, the paper is well written, and has been greatly improved after revision for clarity and situating the model in the context of the literature. Below are a few responses to the author's rebuttal.

(2 & 3) In response to my previous review point 2 and 3, the author has now added "According to this model, hexagonally arranged grid cells should be the exception rather than the rule when considering more naturalistic environments." It is good to know that it captures data that show non-grid like responses in more complex and realistic environments. However, the model still focuses on explaining the spatial firing aspect of grid cells even though they are not supposed to be spatial. I noted in my previous review, "If it's not encoding a spatial attribute, it doesn't have to have a spatial field. For example, it could fire in the whole arena". The author notes inhibitory drive and habituation. Habituation happens, but then spatial cell responses are supposed (or assumed) to be still strong after many visits to that environment. More generally, I am more convinced that grid-like and spatial coding are a special case - both in navigation and memory. In a way I believe the author agrees, though the work here focuses on capturing spatial properties (which is understandable given the literature). In conclusion, though there may be theoretical disagreements, I find the points the author raises fair.

(4) The difference between mEC and lEC or PRC for encoding non-spatial vs spatial attributes is still not clear to me - though not crucial for the point of this paper.

(5) Thank you for providing a video - this makes it extremely clear how learning occurs.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.95733.3.sa2](https://doi.org/10.7554/eLife.95733.3.sa2)

The author presents a novel theory and computational model suggesting that grid cells do not encode space, but rather encode non-spatial attributes. Place cells in turn encode memories of where those specific attributes occurred. The theory accounts for many experimental results and generates useful predictions for future studies. The model's simplicity and potential explanatory power will interest others in the field. There are, however, a few weaknesses outlined below which undermine the theory.

Main criticisms:

(1) A crucial assumption of the model is that grid cells express grid-like firing patterns if and only if the content of experience is constant in space. It is difficult to imagine a real world example that satisfies this assumption. Odors and sounds are used as examples. While they are often more spatially diffuse than an object on the ground, odors and sounds have sources that are readily detectable and thus are not constant in space. Animals can easily navigate to a food source or to a vocalizing conspecific. This assumption is especially problematic because it predicts that all grid cells should become silent when their preferred non-spatial attribute (e.g. a specific odor) is missing. I'm not aware of any experimental data showing that grid cells become silent. On the contrary, grid cells are known to remain active across all contexts that have been tested, including across sleep/wake states. Unlike place cells, grid cells have never been shown to turn off. Since grid cells are active in all contexts, their preferred attribute must also be present in all contexts, and therefore they would not convey any information about the specific content of an experience. The author lists many attributes that could in theory be constant in a laboratory setting, but there is no data I'm aware of that shows this is true in practice. As it stands, this crucial assumption of the model remains mere speculation.

(2) The proposed novelty of this theory is that other models all assume that grid cells encode space. This is not quite true of models based on continuous attractor networks, the discussion of which is essentially absent. More specifically, attractor models focus on the importance of intrinsic dynamics within entorhinal cortex in generating the grid pattern. While this firing pattern is aligned to space during navigation and therefore can be used a representation of that space, the neural dynamics are preserved even during sleep. Similarly, it is because the grid pattern does not strictly encode physical space that grid-like signals are also observed in relation to other two-dimensional continuous variables.

(3) The use of border cells or boundary vector cells as the main (or only) source of spatial information in the hippocampus is not well supported by experimental data. Border cells in entorhinal cortex are not active in the center of an environment. Boundary-vector cells can fire farther away from the walls, but are not found in entorhinal cortex. They are located in the subiculum, a major output of the hippocampus. While the entorhinal-hippocampal circuit is a loop, the route from boundary-vector cells to place cells is much less clear than from grid cells. Moreover, both border cells and boundary-vector cells (which are conflated in this paper) comprise a small population of neurons compared to grid cells.

Minor comments:

(1) There is substantial theoretical and experimental work supporting the idea that grid cell modules instantiate continuous attractor networks, yet this class of models is largely ignored:

p. 7 "In contrast, most grid cell models (Bellmund et al., 2016; Bush et al., 2015; Castro & Aguiar, 2014; Hasselmo, 2009; Mhatre et al., 2012; Solstad et al., 2006; Sorscher et al., 2023; Stepanyuk, 2015; Widloski & Fiete, 2014) are domain specific models of spatial navigation"

The following references should be added:

McNaughton, B. L., Battaglia, F. P., Jensen, O., Moser, E. I. & Moser, M.-B. Path integration and the neural basis of the 'cognitive map'. Nat. Rev. Neurosci. 7, 663-678 (2006).

Fuhs, M. C. & Touretzky, D. S. A spin glass model of path integration in rat medial entorhinal cortex. J. Neurosci. 26, 4266-4276 (2006).

Burak, Y. & Fiete, I. R. Accurate path integration in continuous attractor network models of grid cells. PLoS Comput. Biol. 5, e1000291 (2009).

Guanella, A., Kiper, D. & Verschure, P. A model of grid cells based on a twisted torus topology. Int. J. Neural Syst. 17, 231-240 (2007).

Couey, J. J. et al. Recurrent inhibitory circuitry as a mechanism for grid formation. Nat. Neurosci. 16, 318-324 (2013).

(Note: the Bellmund et al. (2016) citation is likely a mistake and was intended to be Bellmund et al. (2018).)

(2) The author claims in two places that this model is the first to explain that grid cell population activity lies on a torus. While it may be the first explicit computational account of why grid cell activity is mapped onto a torus, these claims should be moderated for clarity, for example by adding "but see McNaughton et al. (2006) and others".

Box 1. Results Uniquely Explained by this Memory Model - the population code of grid cells lies on a torus

p.11 "In addition, this simplifying assumption allows the model to capture the finding that the population of grid cells lies on a torus (Gardner et al., 2022), although I note that the model was developed before this result was known."

(3) Lateral entorhinal cortex is largely ignored in this memory model. It should be considered that the predominance of spatial representations reported in the literature is due to historical reasons. Namely, the discovery of hippocampal place cells spurred interest in looking upstream for the source of spatial information, which was later abundantly clear in medial entorhinal cortex. Lateral entorhinal cortex is relatively understudied, but is known to encode odors, objects, and time in a way that medial entorhinal cortex does not. It is therefore confusing to assume that these attributes are instead encoded by grid cells.
