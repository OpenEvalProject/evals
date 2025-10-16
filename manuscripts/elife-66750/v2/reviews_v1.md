# Peer review - Round 1

Editors:
- Danelle Devenport, Princeton University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66750.sa1](https://doi.org/10.7554/eLife.66750.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper addresses the interesting problem of understanding how complex metazoan forms can be so robust and tolerant to perturbation. The authors have created a new landmark-free approach to morphological analysis of complex developmental structures (here, the fly wing) and use it to describe variation across individuals in a population and in response to weak genetic and environmental perturbations. Their finding that morphological variation amongst individuals follows along a low-dimensional, but spatially non-intuitive, mode is a fundamental result. The landmark-free analysis should be broadly applicable to other structures and developmental systems.

Decision letter after peer review:

Thank you for submitting your article "Global Constraints within the Developmental Program of the Drosophila Wing" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

1) It's not entirely clear what is the 'true' answer when comparing phenotypes, and whether the dominant principle component in the data sets could just reflect the mapping method and choices made to delineate the wing. Can the authors test for this by intentionally augmenting wing shape and reference points and ask how these map to the disk? Please see reviewer2 point #1, #2, and #4 for specific recommendations.

2) The data support the notion that there is a low-dimensional character to the magnitude of variation amongst individuals in terms of developmental phenotype. It would be important to include a discussion addressing how is the size of such variations is related to fitness of individuals of a species. Could it be that weaker modes that carry less of the overall variation still are under strong selective pressure in certain environments and indeed, are strongly relevant for organismal fitness? Or is the argument that the global mode simply defines the most broadly conserved aspects of fitness? If the latter, then it is interesting to understand how much of the wing developmental program is captured in the top mode of variation.

3) The key technical feature of this work lies in the mapping of images of wing morphology to a fixed-sized disc and alignment over the ensemble of images. Could the authors discuss whether such a transform is guaranteed for any sort of structures during development? This may help readers understand how general the method developed here might be for enabling similar studies in other developmental systems.

4) Please address questions regarding technical aspects of the method – see reviewer2 point #3, #7.

Reviewer #1:

This paper addresses the interesting problem of understanding how the seemingly complex and even baroque developmental processes of metazoan forms can be so robust and tolerant to perturbation. The essence of the idea is to propose that there are hidden simplicities that are not obvious but that can be discovered in a data-driven manner using statistical reasoning. With this premise, the authors claim (1) they have created a new landmark-free approach to morphological analysis of complex developmental structures (here, the fly wing) in which ensembles of images are processed to identify the boundary of the structure, then mapped onto a disc while maintaining local geometry, and then aligned, (2) that this stack of aligned structures can be then statistically analyzed for pixel-by-pixel positional entropy, providing a high-dimensional feature space within which each image is embedded, (3) that the landmark-free analysis is superior to existing low-dimensional landmark-dependent approaches, (4) that eigenvalue decomposition of the ensemble shows that most of the variation amongst individuals is accounted for in just the top mode, (5) that the top modes of variation are different from what is learned by the traditional landmark-dependent approach, (6) that subtle genetic variations due to mutations or natural outbred variations project onto the top mode of this analysis, and (7) that significant perturbations due to temperature during development and or dietary fluctional largely excites variations along the same top mode. From this, the authors propose (1) that there are global, low-dimensional constraints within the development of the fly wing such that random, genetic, and environmental perturbations are largely forced to cause variations along a single mode of variation, and (2) that this mode is not obvious in traditional ways of analyzing morphological data.

In general, this is a very interesting and topical body of work. The question is important, and the specific findings seem well supported by the data presented. The finding that morphological variation amongst individuals follows along a low-dimensional (but spatially non-intuitive) mode is a fundamental result, especially if the approach of landmark-free analysis inspires other developmental biologists to check and verify the claims in many other systems. The finding that genetic and environmental variations also follow along the same global mode is a potentially deep statement about the relative simplicity underlying the vast apparent complexity of molecular mechanisms and more naively observed phenotypes associated with development. If the results of this work can be extended, it could represent an approach for a more general and simpler description of developmental processes and a route to better characterize the underlying mechanisms.

A couple specific points that the authors may wish to consider:

(1) The data support the notion that there is a low-dimensional character to the magnitude of variation amongst individuals in terms of developmental phenotype. But how is the size of such variations related to fitness of individuals of a species? Could it be that weaker modes that carry less of the overall variation still are under strong selective pressure in certain environments and indeed, are strongly relevant for organismal fitness? Or is the argument that the global mode simply defines the most broadly conserved aspects of fitness? If the latter, then it is interesting to understand how much of the wing developmental program is captured in the top mode of variation.

(2) The key technical feature of this work lies in the mapping of images of wing morphology to a fixed-sized disc and alignment over the ensemble of images. Perhaps the authors could indicate whether such a transform is guaranteed for any sort of structures during development. This may help readers understand how general the method developed here might be for enabling similar studies in other developmental systems.

Reviewer #2:

The authors implement a novel method for quantifying phenotypic variation in flat two dimensional structures that consists in mapping the entire image into a standard shape (a disk) by an angle preserving transformation. It eliminates the need for preselecting fiducial marks and projecting onto the space of their relative positions. They analyze the Drosophila wing, which is nicely two dimensional, and well-studied by other means, thus a good benchmark. The authors find that variation within a population and in response to various weak genetic mutations predominately fall along the same principle component.

It's not entirely clear what is the 'true' answer when comparing phenotypes, and whether the dominant principle component in the data sets could just reflect the mapping method and choices made to delineate the wing. Nevertheless, the authors new method is provocative and deserves to reach a wide audience, who can try it on other data sets.

1. It's difficult to design a data set in this area where the 'ground truth' is known, so that the degree an algorithm discovers that truth is a measure of its quality. The worry then is the authors analysis inserts some variability in a particular way and the primary principle component just 'discovers', the variability that was inserted. I do not know how to definitively test for this, but to check for the obvious things, can the authors:

i. Intentionally augment the outer boundary of the wing, and analyze as in Figure 5. Is R >> σ. What if some ripple was added to the boundary, what would that look like mapped to the disk?

ii. The authors need to rely on a reference feature to map to the origin of the disk. Assume the position of that was randomized by a few pixels, how would that display in Figure 5?

iii. Same set of questions for the way the authors separate the wing from the hinge

2. In Figure 2d most of the variation is in common for male-females under the landmark free methods while with landmarks the largest PCA component discovers sex. The authors claim this is a vindication of their method, but could it in fact be a problem (as suggested in 1.) Also the data in 2d seems to be bipartite, any explanation?

3. Can the authors take their conformal mapped and registered images, and extract the coordinates of the Procrustes reference points. What is the relation of the principle components based on the Procrustes variables versus their pixel based measures. It's not entirely clear to me what feature their dominant PC picks up. If I shift a vein normal to itself a lot of pixels change, but the movement is less consequential viewed as an operation on a vein. Thus as usual an information theory measure can be misleading.

4. A key finding is that genetic perturbations fall along the same PC as does intrapopulation variation. In the case of the gene tkv the authors remark that their analysis picks up the same feature displacement in the weak heterozygote as in the homozygote. Is the same true for the other mutants they examine, in particular N. The N mutants are readily visible, if they are processed as in Figure 5b,c would they fall along the primary PC? If the authors consider it too onerous to measure on new flies, can they just by photoshop impose a comparable mutation on a few of their current images and process?

5. With their environmental perturbations the authors could ascertain when in development the wings are sensitive to the environment, ie does a molt reset the phenotype of the wing?

6. The ultimate test of the unique principle component, is to measure the wings on a closely related species of Drosophila (as the authors remark at the end of their discussion). Would this be a big increment in work over what has already been done? Just 10's of individuals from a stock collection of D. simulans, D. schellia or whatever is easiest. Some of these species make sterile hybrids with D. melanogaster, so it would be interesting to know how close the wings are.

7. Some technical remarks about the mapping to the disk

i. Is there a reflection among the rotations to align the right and left wings?

ii. Is it obvious one should do PCA directly on the pixel variables, (ie not log transformed for instance). Not many pixels change, but those that do may change their gray scale by a factor of 2-10 (depending on how you are treating background). Does this matter?

The paper is clearly written and should be published after the above questions and those from other referees are addressed. If it's wrong, it's at least interesting.
