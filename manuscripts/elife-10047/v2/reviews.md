# Peer review - Round 1

Editors:
- Uwe Ohler, Duke , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.10047.017](https://doi.org/10.7554/eLife.10047.017)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Active Machine Learning-driven Experimentation to Determine Compound Effects on Protein Patterns" for peer review at eLife. Your submission has been favorably evaluated by Aviv Regev (Senior editor), Uwe Ohler (Reviewing editor), and three reviewers.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Summary:

The reviewers all agreed with the premise of the manuscript, that there is a need to integrate laboratory automation and active learning to speed up the generation of biological knowledge. Rather than the traditional approach of trying to infer cellular mechanisms, the authors suggest that we turn the problem over to machine learning to choose experiments based on sound statistics. The manuscript thus has the potential to be a valuable contribution highlighting the potential of machine learning for automated experimental design. The authors convincingly demonstrate that active learning improved prediction performance, and one reviewer was impressed by the significant technical achievement of physically implementing 30 rounds of active learning.

The paper should be of interest to a broad readership and could potentially be of significant impact. However, all reviewers also agreed that the structure, description and presentation need to be greatly improved to make the paper reasonably self-contained; in its current state, it was simply too difficult to follow.

The strongest need was perceived for the explanation of the methods: The description of the machine learning methodology is completely absent; the reader is largely referred to the previous paper of Naik et al. (2013). Given the central importance of machine learning in the manuscript, sufficient description of the methodology should be included. The authors need to greatly clarify their approach and rationale, including specific examples of what they are trying to do.

The precise definition of the problem and criteria how to evaluate are unclear in several places.

In turn, the Results section could convey the same amount of information in far less space, and the Discussion section was seen as bloated.

We provide below the essential revisions.

Essential revisions:

Specific condensed comments from reviewer one:

1.1) Are images in a quad actually the same image (as seems to be implied in the subsection “Efficiency of Learning”), or do they correspond to biological replicates (as seems to be the in the subsection “Identifying Perturbations”)? Please clarify.

1.2) Is the number of clusters fixed at the outset? Could it be varied when e.g. new treatments result in unexpected patterns? This would be worth discussing as one of the strengths of the approach is the absence of a need for defining the number of classes.

1.3) In the fourth paragraph of the subsection “Efficiency of Learning”: Explain more explicitly the regression model proposed so that we understand what the regression coefficients mean exactly.

1.4) In the second paragraph of the subsection “Robustness of Learning to Imperfect Phenotype Identification”: the discussion of confused quads is quite confusing.

1.5) In the second paragraph of the subsection “Identifying Perturbations”, the assessment of prediction of effect is convoluted, first discretising, and then evaluating an auROC. Why not directly regress/correlate real effect magnitude with predicted effect magnitude?

1.6) Earlier examples of active learning in a biological context should be referenced, e.g. Romero, Krause and Arnold, PNAS 110, no. 3, 2013.

Specific condensed comments from reviewer three:

2.1) The basic definition of a "correct" prediction is obscure:

"We defined correctness of a predicted phenotype for an experiment to be when the plurality of observations for that experiment is most similar to the examples the learner used to construct that phenotype (see Materials and methods)."

The use of the word "plurality" is unclear. It sounds like the correctness is defined relative to the training data, which seems very unlikely to generalize as new phenotypes are included.

The authors should give a specific example of what a prediction looks like (something like a subcellular localization class? or set of classes? or feature vector?) along with an unseen observation and explain how they decide if the prediction is accurate or not.

There is a Methods section entitled "Accuracy Assessment by Classification of Predictions", which has some discussion of nearest-neighbour classification, but it is unclear how the "correct" vs. "incorrect" decision is made.

2.2) Apparently, the authors duplicate their data, but hide this from the learning algorithm.

"The goal of the duplication was to provide some guaranteed basis for the learner to be able to predict at least some results without performing all possible experiments."

"From the design of the study, each unique combination of drug and clone corresponds to four potential 19 experiments in the 96x96 space (which we refer to as a quad)."

However, the claim in the Abstract is:

"The results represent the first practical demonstration of the utility of active learning-driven biological experimentation in which the set of possible phenotypes to be learned is unknown in advance."

This seems contradicted by the "hidden" duplication structure of the data, and is made unclear by the terminology ("quad"). Is the "duplication" scientific "replication" (in the sense of doing the same experiment twice)? Are the same clones reimaged (technical replicates)? Is the experiment performed independently (biological replicates)?

If there are replicates, why not use this to improve the statistical analysis, or hold out some of the replicate data to evaluate the accuracy of the approach? For example, why not run the learner on two replicates independently and see how well the results agree.

The authors should run the active learner in a practical scenario, and then evaluate the accuracy of the findings. The real test of the methodology may be the extent and efficiency with which the active learner discovers the most interesting unknown drug effects on phenotypes. Presumably very rare or subtle effects are harder to find and more interesting, and if the learner can find these, it must be doing well. This is not convincingly demonstrated (or explained) in the paper.

2.3) It is unclear why the accuracy is not evaluated on the held out data:

"Assuming that the same accuracy per coverage model holds for random samples (that is, that the accuracy of the model can be accurately predicted from just the distribution of quad samplings)".

The authors report that the number of phenotypes increases with more data. How would the accuracy stay the same as more data is collected (especially if the accuracy is evaluated relative to the data seen so far)?

2.4) "These distances were then thresholded by fitting a two-class Gaussian mixture model which 10 set ~25% of the experiments as significantly perturbed. Perturbation of model predicted phenotypes was defined similarly by pooling data within phenotypes instead. Using these we constructed a receiver operator curve; the area under this curve (AUC) was 0.68, which suggests overall agreement in what may reasonably be considered significantly perturbed experiments in a post-hoc analysis."

In this evaluation, the authors define a clear measure of accuracy. However, this seems like a different problem than the one they set out to answer. The Abstract states:

"To our knowledge this is the first series of active learning-driven prospective biological experiments where the possible answers (e.g., what phenotypes might be observed) were not"

This sounds as if the general aim is to predict the actual phenotypes (or at least phenotype classes) – but here the question is simply whether the image is different from vehicle. This alone would be a very interesting (and difficult) problem, and it would be fine to center the paper around these results.

2.5) "The generally increasing number of phenotypes the model identified as more data were collected (Figure 3)."

An exciting aspect of this work is the application in situations where the phenotypes were unknown in advance. However, there is no evaluation of how well the learner is doing at recognizing the localization phenotypes. Figure 3 shows that there might be as many as 50 phenotypes. What are these phenotypes? Are they biologically relevant? Imaging artefacts? Overfitting the data?

2.6) "To confirm and illustrate one of the top-ranked predictions…"

What was the precise prediction – that Fa2H was localized to the ER-Golgi? That cyclohexamide and econazole have opposite effects? Or that the drugs would have effects at all? Either way, the authors should show more than one cell in the panels and give statistical measurements of the patterns. As it stands, it is unclear what Figure 5 is meant to demonstrate.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Active Machine Learning-driven Experimentation to Determine Compound Effects on Protein Patterns" for further consideration at eLife. Your revised article has been favorably evaluated by Aviv Regev (Senior editor), a Reviewing editor, and one reviewer.

The manuscript has been substantially improved but there are some remaining issues that need to be addressed before acceptance. Please look at the comments from the remaining reviewer and respond and revise your paper to clarify the two points raised. We emphasize (1) that the paper needs to be written in a manner accessible to the eLife readership of biologists; this can be done with better writing, and is imperative; (2) the authors cannot wave away the possibility of technical artifacts; and (3) proper validation, with appropriate statistics should be addressed in the new phenotype.

Reviewer #3:

The authors have done a great job improving the clarity of their paper. However, I still believe that it will be very difficult for a general biology audience to understand. The authors still use a lot of non-standard terminology and convoluted exposition to describe their work.

The authors addressed most of my comments, although I was not satisfied with their responses to two major points:

1) In my first comments, I wrote:

Figure 3 shows that there might be as many as 50 phenotypes. What are these phenotypes? Are they biologically relevant? Imaging artefacts? Overfitting the data?

The authors answered:

“We thank the reviewer for raising this useful point. We have clarified our goal regarding phenotypes in the Introduction, and have extensively revised the section "Identifying Perturbations." We believe that the most direct answer is that it is reasonable to consider as "biologically relevant" phenotypes that are statistically significant and when predicted to be observed for as yet untested combinations of drugs and targets match subsequently corrected images.”

I strongly disagree with the authors on this point. In my experience, technical artifacts typically show the strongest statistical significance in automated microscopy image analysis. The authors should show convincing examples of the phenotypes they believe are "biologically relevant" or remove the claims that their approach can identify new phenotypes.

2) I also asked for clarification and improvement of their validation of a new phenotype in Figure 5. The authors have done a good job to clarify the explanation of their independent test of a prediction in Figure 5. However, they still only show one cell in each panel, provide no statistical evidence that these patterns are actually different from the vehicle, nor do they show that the changes observed in these new images are consistent with the images that were used by the active learner. I therefore find this "validation" unconvincing.
