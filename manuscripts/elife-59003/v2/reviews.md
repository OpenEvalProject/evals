# Peer review - Round 1

Editors:
- Anne E West, Duke University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59003.sa1](https://doi.org/10.7554/eLife.59003.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Extensive and spatially variable within-cell-type heterogeneity across the basolateral amygdala" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Laura Colgin as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Benjamin W Okaty (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

The BLA is known to participate in a wide range of behaviors and neurons of the BLA are already known through tracing to connect to different regions. Here the authors ask whether there is heterogeneity in gene expression within different neurons of the BLA and conclude that these differences in gene expression may define neurons that participate in different BLA functions. Using scRNA-seq with in situ validation, the authors find transcriptomic separation of lateral from basal amygdala neurons as well as identifying less distinctly spatially segregated subpopulations of neurons in each of the two subdivisions. Overall this dataset will be helpful to researchers studying amygdala function.

Essential revisions:

The reviewers concurred on three points that they felt should be strengthened through text revision or data analysis to fully support the conclusions of the manuscript. I have included the full text of the reviewers' comments on these points including suggestions for further data or analyses because they offer insight into the nature of the concerns. These are just suggestions, however, and we invite the authors to decide how to respond.

1) The authors need to further justify the clustering parameters used.

One review said, "While I recognize it is not a trivial problem to identify clustering parameters to fully capture cell type diversity, I am concerned that the number of cells is in the dataset may be too low, which is limiting cluster resolution. Alternatively, the clustering parameters used for Figure 2 and beyond may not be optimized to capture more granular transcriptionally distinct cell types. Methods such as IKAP (https://www.biorxiv.org/content/10.1101/596817v1) have been developed to identify clustering parameters based on the particular dataset. Did the authors use this or some other method to arrive at their clustering parameters? Can they scientifically justify the parameters they chose?"

A second suggested, "Did the authors make any attempt to cluster cells based on mFISH CPA values of all 12 genes? If so, what did that look like; i.e. how well does this particular set of 12 genes serve to classify all six clusters identified by scRNAseq? Might it be possible to use this mFISH data to further characterize anterior/posterior or dorsal/ventral bias of finer-scale subclusters, rather than based solely on single marker genes? While the correlation analysis does a nice job of showing graded spatial heterogeneity, it would still be informative to see some sort of quantification of spatial bias of all the scRNA-seq subclusters, as inferred by mFISH."

2) A central and critical theme of the manuscript is the idea of continuous gradients of gene expression. However this concept raised two different sets of questions – one about the definition of cell types and one about the concept of continuous distributions in space.

a) While transcriptomic cell-typing is a powerful tool for neuron classification, cells that exist along a continuum in gene expression space may nonetheless constitute functionally distinct subtypes in ways that are not fully "reducible" to well-separated transcriptomic boundaries alone. Moreover, continuous expression gradients may become discretized at higher levels of regulation (e.g. a critical mRNA expression threshold may be required for protein expression, or gene/protein expression level may have some nonlinear relationship with higher-order cell phenotypes etc.). Could the authors perhaps give a more nuanced discussion of these possibilities? Specifically, I think it's important to explicitly make the distinction between transcriptomically defined neuron subtypes and subtypes defined by other criteria.

Certainly a desirable goal is to have a comprehensive measure of cell identity that subsumes multiple levels of description, and in ideal circumstances cellular transcriptome and other phenotypes may overlap in a clear-cut way. However, that may not always be the case. For example – when describing the results of Kim et al., 2016 with respect to there being functionally distinct subtypes of BLA neurons marked by expression of Ppp1r1b or Rspo2, the authors state: "In the context of our results here, we interpret these previous results as analyzing opposite extremes of a continuum; indeed, in our scRNA-seq data Ppp1r1b and Rspo2 are enriched in opposite ends of the BA transcriptomic spectrum and do not conform to distinct subtypes. Thus, results predicated on analyzing these two populations may reflect relatively arbitrary divisions of a continuum, rather than examination of well-separated subtypes."

Ppp1r1b and Rspo2 appear to be expressed at the highest levels in clusters BA1 and BA4, respectively. While the boundary between BA1 and BA4 in tSNE-space is more graded than discrete, these clusters are nonetheless separable by Louvain clustering, and random forest classification of subsampled data appears to fail mostly at the interface of these clusters, not at the "opposite extremes". Thus, if these two genes are enriched in "opposite ends of the BA transcriptomic spectrum", is it truly "arbitrary" to use these genes to parse BLA neurons into different subtypes? Moreover, Kim et al., 2016 found that neurons marked by one or the other gene exhibited different spatial biases, responded to different stimuli, and regulated different behaviors, all of which suggests that these indeed represent functionally distinct neuron subtypes.

b) My only concern relates to the way the authors discuss the concept of spatial gradients. I find the wording confusing both with respect to gene expression and with respect to the projections. One example is where the authors refer to a "continuous spectrum" of cell types defined by gene expression across the LA. This emerges again where it says "both the BA and LA exhibit variable cell-type identity that transformed continuously in space". However, especially since the authors are looking at one gene at a time, it is not clear it is quite continuous – which along with the word "graded" sounds to me like it goes from high to low so quantification would be required. With respect to the gene expression data that are analyzed by the multi-color in situ (which is a powerful experiment) it was unclear when the authors refer to "graded" versus "discrete" do they take into account levels of expression or is this just a +/- call above threshold? This is certainly a quantitative method but it is not clear in Figure 6 that the quantitative data were used. This would be nice to see and would likely make this concept more clear.

3) Two of the reviewers raised questions about BLA interneurons. The reviewers agreed that exploring interneuron transcriptomes was not essential in this paper but suggested that the authors clarify the following points:

a) The authors say they use a manual approach "that facilitates capture of excitatory neurons" but the methods offer no description of how that selectivity would be achieved other than via a careful dissection of a brain region primarily composed of those neurons. This should be clarified.

b) The paper largely ignores interneuron populations in and around the BLA. Including pericapsular GABAergic clusters. This is despite these cells being an integral component of BLA circuitry. To make the paper more comprehensive, the authors could include data from the 51 interneurons they collected, and provide some description of the cell types. If the authors cannot provide these data, it should be made explicitly clear in the text that these data are not included.

c) Subsection “Discrete separation in gene expression maps onto the lateral vs. basal amygdala nuclei” and Figure 3—figure supplement 1: If the authors want to make the strong statement that the "spill-over" is interneurons, they need to show that with double labeled in situ, not just argue that the pattern of expression is similar in number and general spatial distribution.
