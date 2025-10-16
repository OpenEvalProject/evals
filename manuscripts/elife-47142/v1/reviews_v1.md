# Peer review - Round 1

Editors:
- Thomas Serre, Brown University United States

Reviewers:
- James Haxby, Dartmouth College United States
- Dirk Bernhardt-Walther

## Review text

DOI: [10.7554/eLife.47142.020](https://doi.org/10.7554/eLife.47142.020)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The nature of the animacy organization in human ventral temporal cortex" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Thomas Serre as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Michael Frank as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: James Haxby (Reviewer #2); Dirk Bernhardt-Walther (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This is a timely manuscript that seeks to explain the animacy continuum found in the Ventral Temporal Cortex (VTC). The authors used computational and behavioral methods to parameterize a set of stimuli used for an fMRI experiment to disentangle visual categorizability vs. agency. While these two measures have been confounded in previous work, the present study uses a stimulus set in which visual categorizability and agency are dissociated based on representations derived from convolutional neural networks and behavioral experiments. A linear model which incorporates both measures fully explains the continuum found in the fMRI experiment. A subsequent spotlight search shows that categorizability and agency are actually represented in separate clusters of voxels further strengthening the main result.

The reviewers unanimously agreed that the paper is of sufficient interest, quality, and novelty to merit accepting it for publication in eLife. The reviewers all agreed that no additional experiments are needed. A revision is however needed to clarify some of the methods and concepts used as well as to provide additional data analyses. We have the following suggestions to improve the manuscript.

Essential revisions:

The reviewers suggest further analyses and figures to clarify how the representation of visual categorization and of agency are structured. Is the animacy continuum based both on visual features and agentic properties, or are there two animacy continua or a gradient reflecting a transition from a representation of visual information that lays the foundation and a representation of agency? Should the term "animacy continuum" refer to an amalgam of visual features and agency, or should it be reserved for semantic content?

One suggestion includes a multidimensional scaling analysis similar to the analyses and figures of Connolly et al. (2016). In the original paper, the authors showed gradients of changes in representational geometry that (a) disentangled representation of animal taxonomy vs. visual appearance in VTC and (b) disentangled predacity from visual appearance and taxonomy along the STS. A similar method could be used to help clarify exactly how the animacy continuum in VTC reflects both visual categorizability and agency. They seem to be dissociable, and the anatomical and conceptual aspects of this dissociation could be explored and explicated more thoroughly.

In a similar vein, the authors pose the question "How can such a seemingly high-level psychological property as agency affect responses in visual cortex?" Why the need to assume VTC is purely visual? This assumption carries with it the assertion that semantic information must come from elsewhere in a large-scale network. It seems quite possible that IT cortex makes the same computations to extract this critical feature from the constellation of visual features and learned associations that could be calculated elsewhere in a network, and direct and automatic extraction of this information in VTC may be more efficient and adaptive, as the authors acknowledge later in the Discussion. Are such computations "visual" or should VTC be characterized as something more than "visual"? The authors cite numerous papers that show the influence of nonvisual information on representation in VTC, and clearer incorporation of these facts in their reasoning could help here. Incidentally, the discussion of nonvisual activation of VTC should include a paper by Fairhall et al. (2017), who show representation in VTC of agentic properties conveyed by voices in the congenitally blind.

With regard to using a CNN as a measure of visual categorizablity, the authors write, "Because this measure was based on a feedforward transformation of the images, we label this measure image categorizability." This statement may not be completely accurate. The training of a CNN uses millions of semantically-labeled images, meaning that semantics are incorporated in the development of feature spaces that afford view-invariant, lighting-invariant, and most importantly exemplar-invariant labeling of new images. Thus, characterizing this CNN as solely feedforward overlooks the fact that it is trained with semantic labels and produces semantic labels. This gray area between "visual categorizability" and semantic classification needs to be clarified. The current manuscript tries to make a binary distinction between visual categorizability and semantic judgment of agency, when in fact it is more complicated insofar as both the CNN and behavioral criteria for visual categorizability can be influenced by semantics – the CNN in how it is trained and the behavioral task in terms of the role that automatic activation of semantic features and categories may influence response times.

The reviewers suggest a rework of the Materials and methods section as they found it difficult to decipher what exactly had been done in the experiment and in the data analysis. Below is a list of clarifications or requests for missing information.

Clarifications regarding methods for using the CNN are also requested:

1) Please confirm/clarify that the network was not specifically fine-tuned for animal/non-animal categorization. An SVM is trained for animal vs. non-animal categorization on top of features extracted from a pre-trained CNN.

2) More generally, when using a CNN to get a visual categorizability score per image, the choice of the final layer as "feature representation" is somewhat odd because units are already category selective and responses across category units tend to be very sparse. For these kinds of transfer learning tasks, people normally consider layers below. Prior work (see Eberhardt et al., 2016) has shown that the best correlation between layer outputs and human decisions for rapid animal/non-animal categorization was actually in the higher convolutional layers. Please comment.

3) In the statement: "Training accuracies were quantified using 6-fold cross-validation. The training accuracy was 92.2%." The authors probably meant "average test or validation accuracy", right (i.e., by training using 5 folds and testing on the remaining one and averaging over 6 rounds)? Please confirm.

4) The image categorizability of an object was defined as the distance to the representation of that object from the decision boundary of the trained classifier. Please confirm that this is distance when the image is used as a test.

5) There is a methodological difference in the way categorizability scores are derived for CNNs and humans. Why? It would have been better to use the cross-validation method for both but obviously, there are constraints on how perceptual measures can be derived. Why not then use the same method for CNNs as for the human experiment of categorizability?

Clarifications regarding human experiments:

1) Which classifier was used for the animacy decoding?

2) What is the "animacy continuum"? Is it the unthresholded decision value of the classifier that was trained on the localizer run?

3) The authors introduced two separate measures of categorizability, which turn out to be correlated. How do these two separate measures of categorizability interact with animacy?

4) The linear relationship between animacy, agency, and categorizability could be investigated solely based on behavioral data. What was the scientific contribution that we obtained from the fMRI data? There is no question that there is one, but we would like to see this worked out better.

5) There is no statement about informed consent for the psychophysics experiments.

6) The image used differ across experiments: sometimes images are grayscale, sometimes color and sometimes unspecified. Please comment.

7) The subsection about "Comparing visual categorizability with the animacy continua" is confusing. As written, the statistical analysis tests whether the model correlation with the animacy score is lower than that of the human to human correlation. If the corresponding p-value is <.05 as stated, then the model is indeed lower than the noise ceiling not at the noise ceiling? Please clarify. At the very least the wording should be such as to remove any source of ambiguity about the null hypothesis etc.

8) It is said that "Animacy classifiers were trained on the BOLD images obtained from the animate and inanimate blocks of the localizer experiment and tested on the BOLD images obtained from the main experiment." How do you then get a p-value for significance for above chance classification for each sphere as reported in the subsection “Searchlight details”?
