# Peer review - Round 1

Editors:
- Upinder Singh Bhalla, https://ror.org/03ht1xw27 Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82502.sa0](https://doi.org/10.7554/eLife.82502.sa0)

This computational study provides fundamental insights into the relationship between odors, demonstrating that perceptual similarity is related to proximity in metabolism. The authors use a compelling machine-learning analysis trained on human datasets, which turns out to generalize well across diverse species. The work will be of particular interest to olfactory neuroscientists and researchers looking at sensory representations.


---

# Peer review - Round 1

Editors:
- Upinder Singh Bhalla, https://ror.org/03ht1xw27 Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82502.sa1](https://doi.org/10.7554/eLife.82502.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Metabolic activity organizes olfactory representations" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Andrew King as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The reviewers agreed that the framing of the problem is interesting, and the idea that odor perceptual distance relates to metabolic proximity is worth exploring. Can the authors cite a highly relevant PhD thesis that also discussed this many years ago: Chee-Ruiter (https://thesis.library.caltech.edu/7595/)

2. A comparison of neural data for a range of presented molecules would greatly strengthen the current argument which is mostly based on human perceptual classification.

3. Can the authors more closely compare the POM distance vs the Modred descriptor, especially indicating correlations between the measures?

4. Can the authors provide substantially more detail about the technical details of the GNN and how readers can access the data and run the calculations? The code should be open source.

Reviewer #1 (Recommendations for the authors):

Can the authors place their findings in context with numerous prior attempts to come up with an odorant perceptual space, typically using PCA and similar methods? The authors mention some studies very briefly. It would be interesting to understand where the current approach diverges from the findings of earlier work.

The description of the methods is inadequate, especially since this is a general biology readership. The authors should provide considerably more detail on the GNN architecture, and the training methodology, and refer the reader to the source code. If the authors have done an additional level of curation/organization of the data, that too should be made freely accessible. For computational studies, it is preferable to provide user-downloadable scripts to generate key figures.

Can the authors explain some of the theoretical and ANN-field background of the approach to taking a subset of a GNN as an embedding that encapsulates the dataset referred to as POM in this study.

Can the authors spend substantially more time explaining the features of the POM: Its size, number of parameters, and how it is interrogated in the various analyses carried out in this study?

The authors make a very interesting link to metabolism by comparing the odor distances with the metabolic distances. Again, for reproducibility and further work it would be good to provide the database of these extracted metabolic distances.

Reviewer #2 (Recommendations for the authors):

1. In much of the paper, it is claimed that models such as neural networks resemble brain representations (eg second paragraph of Intro: "Representations of the sensory world learned by training predictive models thus often recapitulate nature."). Increasingly, there are counterexamples and arguments against the generality of this assertion. The discovery of internal structure in "such models may be more strongly driven by particular, non-fundamental, and post hoc implementation choices than fundamental truths about neural circuits or the loss function(s) they might optimize." (Quoted from https://www.biorxiv.org/content/10.1101/2022.08.07.503109v1)

2. There are additional data sets that might be worth analyzing. Of course, the authors have plenty already, but I wonder why no mouse receptor or glomerular data were used (given that many groups have produced tons of data on this) – just this reviewer's curiosity.

3. For historical reasons, the authors may consider citing a PhD thesis on the relationship between metabolic similarity and perceptual similarity by Chee-Ruiter (https://thesis.library.caltech.edu/7595/). I'm not sure if that work was ever published in a peer-reviewed journal.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Metabolic activity organizes olfactory representations" for further consideration by eLife. Your revised article has been evaluated by Andrew King (Senior Editor) and a Reviewing Editor.

The manuscript has been substantially improved but there are some remaining issues that need to be addressed, as outlined below:

1. Can the authors provide a more complete explanation of the analysis methods for Figure 4 supplement 1? There are very brief accounts in the methods section on pages 15 and 16. How does one go from ORN responses to regression targets and thence to neural distance?

2. The authors may wish to put some of the key points about Mordred vs POM measures from their responses to the reviews, into the text or discussion.

3. Some fixes needed in the text:

Page 12: "…in Figure 4 we computed distance metrics upon it is the distance between two components of an essential oil."

4. Figure 4 supplement 1: Carey et al. plot seems to be missing bars for cFP – edit distance.

5. Figure 4 supplement 1: Chae et al. seem to have a much smaller rank shift. Is this correct? Is it just due to the number of odors in the sample, or does it relate to the difference in the scoring function as described (very briefly) in the text?

6. Figure 4 supplement 1: No stats to compare the bars?

7. Tanimoto distance should be spelled throughout with a capital T.
