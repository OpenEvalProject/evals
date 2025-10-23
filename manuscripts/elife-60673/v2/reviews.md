# Peer review - Round 1

Editors:
- Morgan Barense, University of Toronto Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60673.sa1](https://doi.org/10.7554/eLife.60673.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The paper describes an exciting and innovative method of bridging post-mortem cytoarchitecture with in vivo functional MRI, allowing for a powerful and compelling investigation of micro-architecture in the medial temporal lobe (MTL). This work has important implications for how information transfer occurs through macro-structural circuits across the whole brain as well as more local brain circuits in the MTL.

Decision letter after peer review:

Thank you for submitting your article "Convergence of cortical types and functional motifs in the mesiotemporal lobe" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Timothy Behrens as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: James M Shine (Reviewer #1); Rosanna Olsen (Reviewer #2); Edward Hogan (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

All three reviewers saw great merit in your work and were enthusiastic about its potential. Nonetheless, each reviewer raised several substantive concerns, which much be addressed in a revision. The individual reviews are provided below. Broadly speaking, we see the essential revision as (1) providing additional clarity with respect to methods, (2) further unpacking of some of the results, as well as conducting a few targeted statistical analyses (i.e., to test for differences in slopes), and (3) clearer positioning of the current work as it relates to the existing literature. We hope you find these reviews helpful as you revise the manuscript, and we look forward to reading the revision.

Reviewer #1:

Thank you for inviting me to review this manuscript by Paquola and colleagues, in which the authors used a combination of high-resolution anatomical data, machine learning, spectral DCM and resting functional connectivity measures to interrogate the relationship between structural and functional gradients of organization within the mesial temporal lobe.

The study is broken into four related sections. In the first section, the authors analysed vertices within a set of mesial temporal lobe structures using a random-forest algorithm, which identified a set of microstructural profiles across the structure. They then interrogated these profiles for evidence of an iso-to-allometric axis, which is a principle known to characterise the transition from 6-layered isocortex (in entorhinal cortex) to 3-layer allocortex (in the hippocampal formation). The authors found evidence consistent with this transition in the BigBrain data, particularly with respect to the skewness of the distribution of thickness across the layers.

In the second section, the authors use Spectral DCM on resting state data from a group of 40 individuals. They then relate the results of the spectral DCM model to the gradients identified using structural anatomy. This section was well-motivated and conducted.

In the third section, the authors compare the structural gradient to resting state functional connectivity with vertices within the cerebral cortex. The results here were quite compelling, showing a dissociation between the iso- and allo-cortical poles in the MTL in which the iso-cortex was correlated with fluctuations in the lateral dorsal attention and frontoparietal networks, whereas the allo-cortical pole was correlated with vertices in the default mode and medial occipital regions.

In the final section, the authors conducted a number of checks of their analysis, including an SNR test to ensure that the temporal lobes (a notorious site for MRI signal dropout) were adequate, and a substantial replication analysis. They should be commended for these steps, and also for making their code freely available.

Comments

1) Section 1: I wonder whether the manuscript might benefit from the unpacking of the random forest results. Is there an intuitive way to characterize skewness that may benefit the reader – such as a particularly uneven spread of thickness distributed across the layers? And is this finding something that we might expect, given the hypothesized gradient of iso-to-allocortex in the MTL?

2) Section 1: Along these lines, is it fair to single out an individual measure from the random-forest regression as being the most salient? From my understanding (which might be mistaken), the weights on a particular variable in a regression need to be viewed in context of the performance of the whole model.

3) Section 2: One minor comment is that it might helpful for the reader if the "in" and "out" effective connectivity directions were incorporated into the matrix in Figure 2A.

4) Section 2: I wasn't sure that I followed the logic of the experiment in which the authors split the MTL data into thirds to test for the consistency of their results. Were each of these sufficiently powered to allow for direct comparison with the main effect? Did the boundaries between these models cut across known regional areas? Perhaps a different way to achieve the same ends would be to use bootstrapping in order to provide a confidence interval around the relationship between structure and function?

5) Section 3: Did the authors hypothesize the iso vs. allo-cortical relationship to resting state networks a priori, or was it discovered upon exploration of the data. Either is fine, in my opinion, but I think it would benefit the reader to have these results placed in the context of the known literature.

6) Section 3: Do the authors expect that the patterns identified in the MTL will relate to subcortical gradients identified in other structures, such as the cerebellum (Guell et al., 2018), thalamus (Müller et al., 2020, and basal ganglia (Stanley et al., 2019)? See also Tian et al., 2020 for general subcortical gradients.

Reviewer #2:

This paper does a very good job of underscoring the importance of characterizing the structural organization of the cortex at a deep level in order to inform functional organization. The authors present an exciting and innovative method of bridging post-mortem cytoarchitecture with in vivo functional MRI, allowing for a powerful and compelling investigation of MTL micro-architecture. This work has important implications for how information transfer occurs through macro-structural and more local brain circuits. The two major findings regarding the allo-iso and the anterior-posterior gradient are supported by the previous literature, but so far characterization of this organization in humans in vivo has been somewhat limited. Most of my suggestions below are regarding points that could be clarified or methods that were unclear.

1) Was there an a-priori prediction regarding the "multi-demand" network? This part of the narrative seemed to come out of the blue and could use more background.

2) Some of the methods are not fully described and are hard to understand. For example, the surface models that are used to sample and model the properties of the microstructure at different cortical depths could be described in more detail. I was also having trouble understanding two things about the "confluence" or "intersection" between the allocentric and isocentric cortices. I was left wondering if the intersection is defined as a plane in surface space, demarcating the separation between hippocampus and entorhinal cortex? Is the confluence/intersection defined based on the manual hippocampal subfields (i.e. medial boundary of the subiculum) or is it defined some other way using the surface profiles/features? Finally, how is geodesic "distance" computed? I would suggest adding a figure to give an overview of these aspects of the methods.

3) Related to the point above, I get the impression that these data show there is no strict boundary between the allo and iso-cortex but rather that there is a somewhat smooth gradient. This point could be made more clear in the Abstract and Discussion. What implications does this particular finding have for theories of MTL subregion function?

4) When r-values are reported to differ for different gradients (e.g. iso versus allo) it is important to test for a significant difference in the slopes (e.g. Fisher r-to-z transform or similar) to know if the relationships are statistically different from one another.

5) This paper builds nicely on other work by DeKraker and colleagues (2019) that has analyzed the microstructural properties of the hippocampus. I think the readers of this paper would appreciate a brief description of how this investigation is similar/different from that work. For example, are the "features" identified here largely overlapping with those identified by DeKraker, and if not, how do they differ here?

6) In the effective connectivity analysis of the MTL, how is variability of the MTL anatomy taken into account? For example, the fusiform and parahippocampal regions of interest will contain highly variable anatomical structures across subjects (e.g. different folding patterns of the collateral sulcus). Given that the focus on anatomical specificity is a major strength of this paper, I would be curious to know how anatomical variability/specificity is accounted for when the data are morphed into MNI152 volume space.

7) I was unsure which analyses were replicated in the Human Connectome Project (HCP) dataset. It is stated that the isocortical functional gradients were re-generated within the HCP cohort and that results were "highly similar" to the original dataset. Was this similarity formally tested?

Reviewer #3:

General assessment of the work: The authors report a study of the mesial temporal lobe (MTL), particularly focusing on structural/functional changes related to transition regions from six layer isocortex to three layered allo-cortex. This group uses their expertise in imaging processing techniques to define the anatomical regions of the mesial temporal lobe transition from isocortex to allocortex using the BigBrain high-resolution histological reconstruction. Using this single high-resolution histological image, they show intensity changes which correlate with the isocortex/allocortex transition. They then use this high resolution reconstruction to coregister to rs-fMRI, and define effective connectivity within the mesiotemporal lobe. Finally, they show variation rs-fMRI global patterns in relationship to the iso-to-allocortical axis, as well as the mesial temporal a/p axis.

Substantive concerns:

This is an interesting study which shows novel relationships between mesial temporal structures and whole brain functional organization. As the authors point out, the novel part of the study involves defining cytoarchitectural regions, and correlating these changes with both local and global function as defined by BOLD fMRI. This is a novel study examining the iso-allocortical transitions with the MTL, and correlating them with local and global rs-fMRI changes. As the authors state, the global rs-fMRI findings related the anterior-posterior axis of the MTL are not new, but add complimentary findings in comparison the iso-allocortical transition findings. Given this, I will focus my comments on the use of the BigBrain image, and definition of the MTL transitions for use in defining regions in the rs-fMRI images.

1) With the BigBrain data, only the right hippocampus was used for segmentation, due to a rip in the histopathological sections of entorhinal cortex on the left. It is therefore assumed that the right MTL segmentations were inverted and also used for the left MTL rs-fMRI analysis. If this is the case, it should be more clearly stated in the Materials and methods. Also, discussion should be added to the possible implications for results, both in respect to replicating the histological intensity findings (which could be tested in two hippocampi if both right and left were processed) and the known structural differences between the right and left hippocampi.

2) I had concerns that using the higher resolution BigBrain image as a template for the 8 nodes in the MTL for the much lower resolution rs-fMRI images would be problematic for signal to noise ratio. However, the authors have convincingly shown consistent findings when controlling for signal to noise ratios.

3) The authors mention (and reference) the correlation of histopathological cellular staining intensities with cellular densities and soma size in the Materials and methods section. Given the centrality of this concept to their findings of the BigBrain data, some addition to the discussion about this concept and the underlying evidence for correlation of staining intensity and cellular densities and soma size would be helpful.
