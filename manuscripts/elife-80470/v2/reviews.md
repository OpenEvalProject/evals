# Peer review - Round 1

Editors:
- Stephen Liberles, https://ror.org/03vek6s52 Harvard Medical School United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80470.sa0](https://doi.org/10.7554/eLife.80470.sa0)

This paper investigates how odors are represented in the olfactory bulb of the brain. Classical studies have revealed a 'combinatorial code' for odorant recognition, with individual odorants represented by combinations of broadly tuned and low affinity olfactory receptors. Here, the authors perform a large scale analysis of odor responses across glomeruli, and surprisingly observe that odorant receptors instead generally display remarkably narrow tuning profiles.


---

# Peer review - Round 1

Editors:
- Stephen Liberles, https://ror.org/03vek6s52 Harvard Medical School United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80470.sa1](https://doi.org/10.7554/eLife.80470.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Mapping odorant sensitivities reveals a sparse but structured representation of olfactory chemical space by sensory input to the mouse olfactory bulb" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Stephen Liberles as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Reviewing Editor and Piali Sengupta as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Bettina Malnic (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers were enthusiastic about the manuscript, but there were a few requests to solidify the data. We have included the full reviewer comments below, and encourage you to focus your revision on a few items.

1) In preparing the revision, it was encouraged to focus on resolving technical questions related to the imaging preparation and associated interpretations. This pertains to the major comments of reviewer #3 and the second and third comments of reviewer #2.

2) We recognize that it may not be feasible to link glomerulus identity to OR identity. Any information that can be provided without additional experiments would strengthen the manuscript considerably but is not a requirement for publication.

Reviewer #2 (Recommendations for the authors):

Many Figure legends are incomplete and do not describe well the Figure for the general reader. For example:

Figure 2B – The name of the odorants depicted in the figure should be described in the Figure legend.

Table S2 – Explain in the legend what the anterior-posterior and mediolateral positions mean.

Citation of some primary work is missing, for example:

Benjamin D. Rubin, Lawrence C. Katz, Optical Imaging of Odorant Representations in the Mammalian Olfactory Bulb, Neuron, Volume 23, Issue 3, 1999.

https://doi.org/10.1016/S0896-6273(00)80803-X

This is a work in rats, but one of the first to visualize the functional responses in the bulb in living animals, to show that glomeruli were tuned to detect particular molecular features and that maps of similar molecules were highly correlated.

Gilles Sicard, Andre´ Holley, Receptor cell responses to odorants: Similarities and differences among odorants, Brain Research, Volume 292, Issue 2, 1984, Pages 283-296,

https://doi.org/10.1016/0006-8993(84)90764-9

This is in frogs, but one of the first comparing odorant structural features in single olfactory neuron responses.

Reviewer #3 (Recommendations for the authors):

In "Mapping odorant sensitivities reveals a sparse but structured representation of olfactory chemical space by sensory input to the mouse olfactory bulb", Burton et al., aim to functionally map odorant responses across the olfactory bulb dorsal surface. The authors characterized glomerular responses to a large odorant panel at low concentration ranges and derived a robust map of 25 glomeruli that are sensitive to a primary odorant. This manuscript represents an important resource to the community, however, there are some points of interpretation/analysis that require revision.

1. In the current analyses, the rationale for not fold-normalizing to the baseline is not adequately provided (given biological heterogeneity e.g., reporter expression); importantly, the δ F alone could be misleading in subsequent PCA analyses (lines 607-608). We recommend converting to a dF/F in this report.

2. The main observation that the authors emphasize is the high dimensionality of the glomerular responses to a large panel of low-concentration odorants. There are a couple of important points here. First, it is not surprising that at low concentrations dimensionality should rise, given what we know about how GPCRs work – in this sense, it is perhaps best to state this as an obvious prediction that is borne out by the data. Second, the dimensionality of neural responses to odors is the consequence of two separate things: odor concentration and the set of odors tested. The authors repeatedly point out that what they are observing is higher dimensional than what has been observed by others, despite the fact that the data being compared are nearly always querying different parts of odor space at different levels of resolution. Some clarity over this point as in the results and Discussion section would be useful – and perhaps most useful would be apples-to-apples comparisons where these authors have looked at the same odors as others. In the absence of that, it is difficult to disentangle whether the reason for the high dimensionality is because of concentration or differences in odor identity across the odor set.

3. Lines 697-700: The authors assessed how well each of these odorant-descriptor distances predict the glomerular responses. In the methods, the "model" part of this analysis is not clearly described – it seems like the authors are asking how, across glomeruli and odors, the rank order of glomerular activity observed relates to the rank order of odor distances given an odor distance metric (quantified using an auROC). If I'm understanding this correctly, this is not a "model" in the sense that nothing is fit, nothing is held out, and there is no statistical metric generated that shows the "model" output is not a consequence of chance. I'm actually cool with this way of capturing neural activity-odor distance relationships, but more description and perhaps a change in language are important for clarity. More importantly, however, the author seems to be looking at cosine distances of each descriptor set and then judging descriptor quality, despite the fact that each of these descriptor sets has its own covariance structure and thus variation in information about odor relationships is differentially distributed across dimensions. The authors mention using 20 PCs (which account for some amount of variance) for one of the odor descriptor sets. The key question here is: given an equal amount of variance captured, how do odor descriptor sets compare? It is not possible to know that answer without PCA being applied to all the descriptor sets (in the same manner that it was for that one odor set) and to then look at performance a. as a function of PCs and b. as a function of variance explained; if the 42 element SMARTS set outperforms DRAGON given an equal amount of chemical variance explained, it would mean that SMARTS is fundamentally more informative than DRAGON. Absent this kind of normalization it is hard to know why one odor descriptor set outperforms another.
