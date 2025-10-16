# Peer review - Round 1

Editors:
- Sacha B Nelson, Brandeis University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.31220.036](https://doi.org/10.7554/eLife.31220.036)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Salient Experiences are Represented by Unique Transcriptional Signatures in the Brain" for consideration by eLife. Your article has been favorably evaluated by Aviv Regev (Senior Editor) and three reviewers, one of whom, Sacha Nelson, is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: Pavel Osten (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors use real-time PCR from dissected brain regions to assess the immediate early gene (IEG) transcriptional responses to a variety of rewarding and aversive experiences including drugs of abuse, feeding, foot shock and gastric distress. Results show specific transcriptional signatures for each experience, enabling decoding of the experience. Moreover, transcriptional codes appeared to primarily reflect the valence of the event, with experiences of neutral or negative valence showing opposing patterns of transcriptional activity. This is an interesting and novel approach akin to efforts to decode experience from brain imaging and neural recordings.

Essential revisions:

1) Increasing the rigor of Feature Selection: There is a fundamental issue with the number of features considered in the analyses and how they were selected from what was measured. Initially, 152 IEGs are measured in 7 brain areas (=1064 features). Then, the number of IEGs is reduced to 78 (>1.25-fold induction). From these, 5 are selected (Arc, Egr2, Egr4, Fos and Fosb), but this step is not well described or justified. Potentially, some of the reduction could be attributed to a priori assumptions based on the literature, but these should be orthogonal to the tested hypotheses (see below) and need to be justified.

In addition, some analyses only consider a smaller number of brain areas, without clear justification. All of these choices can be extremely impactful and may strongly affect the results and ultimately the conclusions drawn from the data. Most importantly, criteria for these choices need to be orthogonal to the tested hypothesis (they cannot depend on differences in IEGs between experiences). If feature selection is non-independent, subsequent analyses will be biased and produce invalid results. The authors need to describe what criteria were used for feature selection (regions and IEGs) and whether these criteria were orthogonal to comparisons among individual experiences. For example, the formal feature selection procedure conducted for results reported in Figure 3 is non-independent, resulting in biased (invalid) classification accuracies. The problem is that the same data were used to select features (estimate "support") and also to evaluate classifier performance, which is circular. Feature selection must be based on nested cross-validation within the training data only. For instance, the algorithm should start with all 1064 features (or 78 x 7 = 546 features) and use nested cross-validation to select a feature set that is then used to determine classifier accuracy in the left-out test data.

2) Controlling for multiple comparisons – this is required for all tests.

3) Statistical testing is needed for many results presented in the manuscript. No statistical tests are reported for any of the results summarized in the sentence "The representation of rewarding experiences are characterized by robust transcriptional induction in the LCtx, NAc, DS, and VTA, while the representations of aversive experiences are dominated by transcriptional induction in the Amy". There are also no tests for whether transcriptional signatures of different experiences with the same or different valence are positively or negatively correlated. All descriptive statements should be backed by appropriate statistical tests within the manuscript.

4) The authors contrast the idea of a "transcriptional code" with the idea of IEG expression as simply "molecular markers for labelling neuronal populations that undergo plastic changes." The issue of the degree to which differences in which genes are transcribed vs. where in the brain they are transcribed is not satisfyingly analyzed. Encoding that matches different experiences to different transcripts would be a transcriptional code in the sense that many might assume from use of the term. On the other hand, encoding that matches different experiences to different brain regions would be quite akin to the "molecular marker" model the authors wish to reject. In between these two extremes, and probably closer to the data is the view that different experiences activate different brain regions, but that different brain regions also have different preferred mixtures of IEGs to activate. Gene-structure pairs are treated as features, but the relative degree to which this is a "spatial" code across brain regions vs. a genetic code across genes is unclear. The authors should attempt to separate these two contributing factors to more precisely specify what kind of "neural code embedded in transcription" they are talking about. It looks from Figure 2B, for example, like there is a strong "shape similarity" across experiences within a region. This would seem to imply that relative activation of the 4 genes tested is more a function of the region than of the experience (e.g. LH and VTA have relatively little activation of Arc). On the other hand, overall magnitude is more related to the interaction between the experience and the structure (cocaine for VTA and DS; foot shock for hipp).

5) The current findings suggest that transcriptional signatures for individual experiences are primarily driven by salience and valence. However, this could simply be a consequence of the (reward-related) brain regions considered here. It is possible that transcriptional signatures in other brain areas are not related to valence, and this should be discussed.

6) Title: it is convention for eLife papers to include some reference to the preparation used. This could be achieved by including the word "rodent" or at least "mammalian" before the word "brain" in the title.
