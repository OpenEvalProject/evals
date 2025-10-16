# Peer review - Round 1

Editors:
- Saad Jbabdi, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77215.sa0](https://doi.org/10.7554/eLife.77215.sa0)

This is a valuable paper investigating hemispheric asymmetries in brain functional connectivity. The authors quantify this asymmetry using a solid methodology that capitalises on recent developments in functional gradients, and they further ask if these asymmetries are heritable and how they compare between humans and macaque monkeys. The results suggest a genetic underpinning of brain functional asymmetry, particularly in areas supporting unique human functions. These findings may help further our understanding of brain asymmetries.


---

# Peer review - Round 1

Editors:
- Saad Jbabdi, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77215.sa1](https://doi.org/10.7554/eLife.77215.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Asymmetry of cortical functional hierarchy in humans and macaques suggests phylogenetic conservation and adaptation" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Saad Jbabdi as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Timothy Behrens as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

There are two important points to address in your revisions:

1) The theoretical point raised by reviewer 1 regarding interpretation of localised changes in the embedding space. This seems to be a fundamental limitation of the method.

2) The point raised by reviewer 2 about insight gained by this study.Reviewer #1 (Recommendations for the authors):

The paper is very well written, the question is interesting, and the analyses are innovative. However, I do have concerns about the overall approach. My main concern is about looking at asymmetries in the low dimensional representation of connectivity. A secondary concern has to do with looking at the parcellated connectome. I explain these concerns in succession below.

The first concern is to me quite a fundamental issue: looking at connectivity in a low dimensional space, that of the laplacian eigenvectors. There are two issues with this. The first one, which is less important than the second, is that the authors have a reference embedding to which they align other embeddings using a procrustes method with no scaling. While the 3D embedding is still optimally representing the connectivity (because distances don't change under rotations), we can no longer look at one axis at a time, which is what the authors do when they look at G1. In this case, G1 is representative of the connectivity of the reference matrix (LL), but not the others.

But even if the authors only projected their matrices onto a single G1 dimension with no procrustes (and only sign flipping if necessary), there is still a major issue. One implicit assumption of this whole approach is that if there is a change in connectivity somewhere in the original matrix, the same "nodes" of the matrix will change in the embedding. This is not the case. Any change in the original matrix, even if it is a single edge, will affect the positions of all the nodes in the embedding. That is because the embedding optimises a global loss function, not a local one.

To make this point clear, consider the following toy example. Say we have 4 brain regions A,B,C,D. Let us say that we have the following connectivity:

In the Left Hemisphere: A-B-C-D

In the Right Hemisphere: A-B=C-D

So the connection between B and C is twice as strong in the right hemi, and everything else remains the same.

The low dimensional embedding of both will look like this:

Left:

… A … B ……. C … D …

Right

A… … … B … C … … … D

Note how B,C are closer to each other in the RIGHT, but also that A,D have moved away from each other because the eigenvector has to have norm 1.

So if we were to calculate an asymmetry index, we would say that:

A is higher on the LEFT

B is higher on the RIGHT

C is higher on the LEFT

D is higher on the RIGHT

So we have found asymmetry in all of our regions. But in fact the only thing that has changed is the connection between B and C.

This illustrates the danger of using a global optimisation procedure (like low-dim embedding) to analyse and interpret local changes. One has to be very careful.

My second concern is about interpreting the brain asymmetry as differences in connectivity, as opposed to differences in other things like regional size. The authors use a parcellated approach, where presumably the parcels are left-right symmetric. If one area is actually larger in one hemisphere than in the other, the will manifest itself in the connectivity values. To mitigate this, it may be necessary to align the two hemispheres to each other (maybe using spherical registration) using connectivity prior to applying the parcellation.

Figure 1. Please explain what "explained variance" means. The gradients represent a low dimensional version of the connectivity matrix. they are not explaining variance?Reviewer #2 (Recommendations for the authors):

Using recently-developed functional gradient techniques, this study explored human brain hemispheric asymmetry. The functional gradient is a hot technique in recent years and has been applied to study brain asymmetries in two papers of 2021. Compared to previous studies, the current study further evaluated the degree of genetic control (heritability) and evolutionary conservation for such gradient asymmetries by using human twin data and monkey's fMRI data. These investigations are of value and do provide interesting data. However, it suffers from a lack of specific hypotheses/questions/motivations underlying all kinds of analyses, and the rich observational or correlational results seem not to offer significant improvement of theoretical understanding about brain asymmetries or functional gradient. In addition, given the limited number of twins in HCP project (for a heritability estimation), the limited number of monkeys (20 monkeys), and the relatively poor quality of monkeys' resting functional MRI data, the results and conclusion should be taken cautiously. Below are the concerns and suggestions.

The gradient from resting-state functional connectome has been frequently used but mainly at the group level. The current study essentially applied the gradient comparison (i.e., gradient score) at the individual level. Biological interpretation for individual gradient score at the parcel level as well as its comparability between individuals and between hemispheres should be resolved. This is the fundamental rationale underlying the whole analyses.

Only the first three gradients are used but why? What about the fourth gradient? Specific theoretical interpretation is needed. At the individual level, is it ensured that the first gradients of all individuals correspond to each other? In this study, it is unclear whether we should or should not care about the G2 and G3. The results of G2 and G3 showed up randomly to some degree.

The intra-hemispheric gradient is institutive. However, it is hard to understand what the inter-hemispheric gradient means. From the data perspective, yes you can do such gradient comparison between the LR and RL connectome but what does this mean? Why should we care about such asymmetry? From the introduction to the discussion, the authors simply showed the data of inter-hemispheric gradients without useful explanation. This issue should be solved.

When aligning intra-hemispheric gradient, choosing averaged LL mode as the reference may introduce systematic bias towards left hemisphere. Such an issue also applies to LR-RL gradient alignment as well as cross-species gradient alignment. This methodological issue should be solved.

The sample size of monkey (i.e., 20) is far less than human subjects (> 1000). Such limitation raises severe concern on the validity of the currently observed gradient asymmetry pattern in the monkey group, as well as the similarity results with human gradient asymmetry pattern. Despite the marginal significance of G1 inter-hemisphere gradient between humans and monkeys, I feel overall there is no convincingly meaningful similarity between these two species. However, the authors' discussion and conclusion are largely based on strong inter-species similarity in such asymmetry. The conclusion of evolutionary conservation for gradient asymmetry, therefore, is not well supported by the results.

For human gradient asymmetry, only t values were provided; For monkey gradient asymmetry, only Cohen-d values were provided. These two should be provided for both species.

Figure 3b, it is hard to believe that such a scatter plot can reach a significant correlation of R>0.3. In addition, such a scatter plot does not match the text (i.e., correlation between the "absolute" AI and heritability)

Figure S3, why should we care about these cross-gradient correlations?

More detailed description for fMRI post-processing for functional connectome and gradient analyses could be added in the supplementary information.

DK atlas is not a good validation parcellation for a functional MRI study like this.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Heritability and cross-species comparisons of asymmetry of human cortical functional organization" for further consideration by eLife. Your revised article has been evaluated by Timothy Behrens (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewer #1 (Recommendations for the authors):

Thanks for your replies to my comments, and sorry for the delay in getting this response to you.

Regarding my first comment, i.e. interpretation of a change in position along the gradients: I am not sure I understand your reply. You agreed that it is difficult to interpret these changes, given that they can represent changes occurring outside the region where the change is reported, but then the analysis you have done does not address this concern. Instead, you calculated some other measure (which I am not sure what it is as it is not well described) and reported the asymmetry index using this new measure. If this new measure is more interpretable, then why do you need to use gradients? What information from the gradients is useful for the study of asymmetries? And how can we interpret changes in positions along the gradients? Simply saying that "interpretation for asymmetry of areas is under a global context" seems to me like sweeping the issue under the rug.

Regarding the issue of using the Procrustes to the template and how that makes the gradients a worse representation of connectivity for the non-template matrices: I don't understand the reply here either. What is meant by joint alignment and how exactly does this address my concern?

If I may add a couple of additional points:

– I said in my original review that this was a well-written paper, but it looks like the writing has gotten worse in this revised paper. I am not sure why that is, but I really invite the authors to re-read the paper, particularly the new sections/paragraphs, and ensure that the arguments make sense (and I don't just mean the English).

– Some of the captions are way too short. They are often comprised of just a few words, which is ok for a caption "title", but not for a caption. A caption needs to explain what is shown avoiding reference to the main text.

– The code provided is poorly organised and not documented. I encourage the authors to improve on that.
