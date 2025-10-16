# Peer review - Round 1

Editors:
- Michael B Eisen, University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55301.sa1](https://doi.org/10.7554/eLife.55301.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper is successful example of an emerging trend in medicine in which machine learning algorithms are employed to integrate clinical data in a rigorous and consistent manner in ways that outperform trained medical specialists in making critical decisions – in this case selecting embryos for implantation following in-vitro fertilization.

Decision letter after peer review:

Thank you for submitting your article "Performance of a deep-learning based neural network in selection of human blastocysts for implantation" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Eisen as the Senior and Reviewing Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional work is required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

In this work, the authors demonstrate a CNN-based algorithm for the selection of embryos at 113 hours post-insemination. Although a number of machine learning algorithms for embryo classification have been reported, the value of this work is that it demonstrated improved selection of embryos at 113 hpi.

There were, however, several important issues raised during review and discussion that need to be addressed in a revised manuscripts.

1) There are several types of classification and inference performed in the study, but it was often hard to follow the order and logic of each classification. It would help immensely to have a figure that outlines the overall logic of the classification process – what the objective of the classification/inference is and how it fits into the overall embryo selection process. As it is, Figure 1 doesn't really accomplish this, and it made it difficult to follow the manuscript in places.

2) In the Introduction, discussion on the importance of evaluating embryos based on transfer outcomes needs to be strengthened. In the current version, the authors discuss on the lack of time-lapse imaging systems in fertility clinics to justify for the novelty of the work. However, to me, the major contribution of this work is the application of CNN for evaluating embryo quality at 113 hpi.

3) There was not a clear justification for why 113 hpi was used or what would be expected if other times were used.

4) It was not fully clear to the reviewers how the ground truth was established and whether there is any data on how good this ground truth is. Similarly it was not entirely clear whether any of the human annotation was used in the predictions as opposed to in training. We assume not as the authors describe this as a fully automated system, but this needs to be clarified.

5) The description of the images used should be strengthened. As it is the central data for the paper is not adequately described, with respect to image quality, completeness, etc…

6) The authors distinguish between 5 classes: 1-2 are non-blastocyst and 3-5 are blastocyst classes. They claim 90% accuracy in separating these. This should be a trivial task unless many embryos are between Morula and Early Blast (classes 2 and 3), but they don't provide a table to show the class distribution. A confusion matrix would be informative.

7) For 113 hpi blastocyst selection, the authors only report the accuracy values for both SET and DET. However, it is important to know whether the algorithm marks an embryo as blastocyst when it really is not (i.e. false positive) or as not-blastocyst when it really is (i.e. false negative). So, can the authors add a confusion matrix to show the data for all 4 cases?

8) The authors use a genetic algorithm (GA) to rank embryos. While the supplement provides a clearer description of what they do, the "genetic algorithm" part of Figure 1A is a bit misleading. In general, the Genetic Algorithm is not described well. To calculate the ranking, they multiply the probability scores from the CNN with a 5x1 weight matrix. The GA is used to optimize the weight matrix, and is not used during inference. It would be interesting to see the trained weights of this matrix – it would explain how much each class contributes to ranking.

9) It is unclear why the 5 classes were reduced to 2 for some of the analyses.

10) There is inconsistent naming of models. Early on they use a CNN, they later combine the CNN and genetic algorithm (subsection “Evaluation of embryo selection based on embryo quality”, first paragraph) and after that begin using the term system. It's not clear whether the latter two are the same or different.

11) They have an undefined term HQB which makes it hard to understand how experiments in the last paragraph of the subsection “Evaluation of embryo selection based on embryo quality” different from each other.

12) In the subsection "Evaluation of selection using implantation outcomes", they do not provide any rationale for using only fresh embryos. They simply state that they do, and alter combine the dataset with frozen embryos.

13) They aren't clear about what the implantation potential is, possibly the probability from the softmax of the CNN.

14) 5 embryos originally selected by the model had known outcome in a subsequent frozen transfer, and 4 of them led to successful implantation. This is nice, but what about the remaining 49 with an unknown outcome. I don't think any conclusion can be drawn based on the 5 with known outcomes. More data like this is needed.

15) In the Materials and methods section, the authors write that 3469 recorded videos of embryos were collected. How have the images at fixed time-points been obtained from these videos? Have you processed the images in any manner? The authors should describe more in detail how the data (i.e. images) were processed prior to feeding them to CNN for training.

16) Some of the acronyms (HQB, 3CC) appear in the Results section without full names. Although they are written in the Materials and methods sections, considering the order of the manuscript (Results then Materials and methods as currently it is), they should appear in the Results section.

17) In the Discussion, it would be helpful if the authors commented, based on their results, on the potential advantage or limitation of using a single static image for this purpose, as opposed to several images or a video clip.

18) The authors should cite and discuss the publication by Tran et al., 2019, and compare/contrast how this current submission differs and or adds to the existing literature.

19) The sentences near the end of the subsection “Evaluation of Euploid embryos based on their implantation potential” are important but are grammatically incorrect and therefore hard to understand. I get what they are trying to say but it's just poorly worded. On this note, there are a number of grammatical errors throughout the paper.

20) Citations basically stop at the Discussion section and there are some statements that definitely need literature support.
