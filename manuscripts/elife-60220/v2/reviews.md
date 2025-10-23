# Peer review - Round 1

Editors:
- Michael B Eisen, University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60220.sa1](https://doi.org/10.7554/eLife.60220.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This research advance builds on the author's previous work on predicting the molecular function of intrinsically disordered from amino acid sequence and evolutionary dynamics. This is an emerging and important field and the author's contribution helps lay key foundations for how this question can be addressed. In addition novel scientific insight, a new online tool, the authors provide a detailed walk-through of the underlying statistical analysis performed.

Decision letter after peer review:

Thank you for submitting your article "Identifying molecular features that are associated with biological function of intrinsically disordered protein regions" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Michael Eisen as the Senior and Reviewing Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

The work presented offers a promising advancement for understanding protein function in general and of IDRs in particular. The manuscript presents the theoretical model development, experimental validation, and a protein engineering effort to further understand the results. A refreshing, pertinent discussion of potential shortcomings of the model is included throughout the manuscript. The manuscript is well-written but given its interdisciplinary nature, it appears overwhelmingly dense in details at times.

In general, it would be nice to have a less mathematical overview of the model workflow as a figure. What are the used features and the resulting predictions? Give more specific examples from the 82 features in Zarin et al., 2019.

Some specific comments raised by the reviewers:

Results/equations

"An interpretable regularized probabilistic model to predict function from IDR features" – I believe the LHS of Equation 1, P(Y=1|Z,b), does not match the description in the preceding paragraph. I think the issue is due to the lack of an “I” subscript for the “Y” variable. Since “I” corresponds to the specific protein, excluding the subscript and writing "P(Y=1)" seems to represent the probability that all proteins in the dataset have a particular functional annotation, while "P(Yi=1)" represents the probability that a particular protein has a particular functional annotation. This discrepancy causes the equivalency in Equation 1 to not be true ("all proteins have annotation" and "no proteins have annotation" are not the only two cases). This same issue extends into Equation 2. I don't believe there is any issue with the underlying approach of FAIDR, but it seems the equations (as written here) are not quite correct. It would be extremely useful to include a more detailed derivation in an Appendix in order to better explain the math behind the approach. Specifically if, this could be mathematically derived and explained in “laymans” terms this would, I think, significantly improve the utility of the manuscript, as for those less familiar with statistical inference/Bayesian analysis the mathematics as they stand basically just have to be trusted (which, having gone through they should, and clearly Dr. Moses is perhaps literally the world authority on this topic, BUT, never-the-less from a pedagogical standpoint it would do a great service to the field to provide a more accessible explanation of how the model is constructed).

Potential major concerns:

"IDR function can be predicted from protein-level annotations and IDR sequence properties" – As far as I can see the authors never indicate which specifics are used to derive their dataset, only that it is the "yeast proteomes". Depending on the source of the proteins in their dataset, it is possible that they have sequences with high similarity to one another in their dataset? This could be problematic. Since if they have two similar sequences with similar functional annotations, and the sequences are divided (since it's random) into the training and test sets, their predictions (and ROC curves) could be inflated and not a true measure of how accurate their method is. I.e., if the proteomic dataset they are using has already accounted for sequence similarity, then this is not a problem.

Results – The test of mitochondrial targeting is consistent with the authors analysis, but it's not clear to me if it's a particularly convincing demonstration of a novel approach, and perhaps the stated conclusions are a little strong given the evidence.

Some general concerns regarding the experiments:

There is no true negative control (i.e. completely redesign the sequence while maintaining pI and hydrophobicity), only the WT Cox15 pos control and various mutant sequences that are relatively similar (other than pI/hydrophobicity).

It is difficult to definitively conclude that the "sim IDR high pI" protein is localizing to the mitochondria from the image without concurrent labelling of mitochondria, only that it is localizing somewhere.

Not enough mutant sequences were tested to reach the conclusion that the localization must be due to high pI and/or high hydrophobicity of the sequence. For both primary mutants, less than 10% of the residues were mutated, so it's impossible to pinpoint what the exact cause of the loss of function is from. For example, given mitochondrial targeting signals have historically been described as amphipathic helices, is loss/gain of helicity a confounding variable? What about loss/gain of a cleavage site (as is commonly associated with targeting sequences).

All this said, the experiments do provide strong evidence for their conclusions, but I don't believe as high of confidence is warranted.

The features identified and then modified are known to be associated with mitochondrial targeting (in fact, represent how these sequences were historically identified, although predictions have now progressed somewhat).

To take a region that has a set of features that had already been identified as correlating with function and then modifying those features is – at least in principle – something that could have been done with the expected outcome without any of the authors methodologies. This of course does not invalidate the authors approach (and does strengthen the case) but it is in my mind not a well-defined “test”. This is not actually a huge problem in terms of publication, but perhaps something worth discussing. In defense of this section, the actually systematic approach the authors take to IDR mutation/evolution/rescue is great and I think a really useful blueprint for how one might test the importance of sequence features.

A sort of important question – is the Cox15 N-terminal IDR actually an IDR? It is not strongly predicted to be disordered (see http://d2p2.pro/view/sequence/up/P40086), and traditionally mitochondrial targeting sequences have been shown to form amphipathic helices (with a positive face). There may be experimental data demonstrating the disordered nature of this region, but it seems odd to select a demonstration example which it is (at least to me?) unclear if it meets the specific requirement for the approach to work. That said, a way to flip this is that as a prediction tool it is fundamentally assessing solvent-accessible residues, and any structural constraints imposed on those residues is perhaps less important than the mean-field chemical composition that the sequence provides. This might be a useful line of explanation (and has the added bonus of broadening the scope of the tool).
