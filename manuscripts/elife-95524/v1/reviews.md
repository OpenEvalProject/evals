# Peer review - Round 1

Editors:
- Tracey L Weissgerber, Berlin Institute of Health (BIH) at Charité Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.95524.3.sa0](https://doi.org/10.7554/eLife.95524.3.sa0)

In this important study, the authors manually assessed randomly selected images published in eLife between 2012 and 2022 to determine whether they were accessible for readers with deuteranopia, the most common form of color vision deficiency. They then developed an automated tool designed to classify figures and images as either "friendly" or "unfriendly" for people with deuteranopia. Such a tool could be used by journals or researchers to monitor the accessibility of figures and images, and the evidence for its utility was solid: it performed well for eLife articles, but performance was weaker for a broader dataset of PubMed articles, which were not included in the training data. The authors also provide code that readers can download and run to test their own images, and this may be of most use for testing the tool, as there are already several free, user-friendly recoloring programs that allow users to see how images would look to a person with different forms of color vision deficiency. Automated classifications are of most use for assessing many images, when the user does not have the time or resources to assess each image individually.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.95524.3.sa1](https://doi.org/10.7554/eLife.95524.3.sa1)

The authors of this study developed a software application, which aims to identify images as either "friendly" or "unfriendly" for readers with deuteranopia, the most common color-vision deficiency. Using previously published algorithms that recolor images to approximate how they would appear to a deuteranope (someone with deuteranopia), authors first manually assessed a set of images from biology-oriented research articles published in eLife between 2012 and 2022, as well as an additional hold-out set of 2000 articles selected randomly from the PubMed Central Open Access Subset. The researchers identified 636 out of 4964 images as difficult to interpret ("unfriendly") for deuteranopes in the eLife dataset. In the PubMed Central dataset 104 out of 1191 non-grayscale images were identified as unfriendly. The results for the eLife dataset show a decrease in "unfriendly" images over time and a higher probability for articles from cell-oriented research fields to contain "unfriendly" images.

The researchers used the manually classified images from eLife to develop, train, and validate an automated screening tool. They also created a user-friendly web application of the tool, where users can upload images and be informed about the status of each image as "friendly" or "unfriendly" for deuteranopes.

Strengths:

The authors have identified an important accessibility issue in the scientific literature: the use of color combinations that make figures difficult to interpret for people with color-vision deficiency. The metrics proposed and evaluated in the study are a valuable theoretical contribution. The automated screening tool they provide is well-documented, open source, and relatively easy to install and use. It has the potential to provide a useful service to the scientists who want to make their figures more accessible. The data are open and freely accessible, well documented, and a valuable resource for further research. The manuscript is well-written, logically structured, and easy to follow.

Weaknesses:

(1) The authors themselves acknowledge the limitations that arise from the way they defined what constitutes an "unfriendly" image. There is a missed chance here to have engaged deuteranopes as stakeholders earlier in the experimental design. This would have allowed to determine to what extent spatial separation and labelling of problematic color combinations responds to their needs and whether setting the bar at a simulated severity of 80% is inclusive enough. A slightly lowered barrier is still a barrier to accessibility.

(2) The use of training images from a single journal limits the generalizability of the empirical findings as well as of the automated screening tool itself. This is evidenced by a decrease in performance of the tool on the holdout dataset from PubMed Central. Machine-learning algorithms are highly configurable but also notorious for their lack of transparency and for being easily biased by the training data set. A quick and unsystematic test of the web application shows that the classifier works well for electron microscopy images but fails at recognizing the classical diagnostic images for color-vision deficiency (Ishihara test images) as "unfriendly". A future iteration of the tool should be trained on a wider variety of images, ideally enriched with diagnostic images found in scientific publications.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.95524.3.sa2](https://doi.org/10.7554/eLife.95524.3.sa2)

Summary:

An analysis of images in the biology literature that are problematic for people with a color-vision deficiency (CVD) is presented, along with a machine learning-based model trained on an eLife dataset to identify such images and a web application that uses the model to flag problematic images. Their analysis reveals that about 13% of the images could be problematic for people with CVD and that the frequency of such images decreased over time. Their best model (convolutional neural network, CNN) yields 0.89 AUROC score and 0.77 AUPRC on held-out eLife articles, but lower scores (0.78 and 0.39, respectively). It is proposed that their approach could help making biology literature accessible to diverse audiences.

Strengths:

The manuscript focuses on an important yet mostly overlooked problem and makes contributions both in expanding our understanding of the extent of the problem and in developing solutions to mitigate the problem. The paper is generally well-written and clearly organized. Their CVD simulation combines five different metrics. The dataset has been assessed by two researchers and is likely to be of high-quality. Machine learning algorithm used (CNN) is an appropriate choice for the problem. The evaluation of various hyperparameters for the CNN model is extensive.

Weaknesses:

While the study has significant strengths, it also has some limitations. Specifically, the focus on one type of CVD (deuteranopia) and selecting images from a single journal (eLife) for training limit the generalizability of the models. This is, to some extent, shown by applying the model to PMC articles, which yields lower performance. "Probably problematic" and "probably okay" classes are excluded from the analysis.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.95524.3.sa3](https://doi.org/10.7554/eLife.95524.3.sa3)

Summary:

This work focuses on accessibility of scientific images for individuals with color vision deficiencies, particularly deuteranopia. The research involved an analysis of images from eLife and PubMed Central published in 2012-2022. The authors manually reviewed nearly 7,000 images, comparing them with simulated versions representing the perspective of individuals with deuteranopia, and also evaluated several methods to automatically detect such images including training a machine-learning algorithm to do so, which performed the best. The authors found that nearly 13% of the images could be challenging for people with deuteranopia to interpret. There was a trend toward a decrease in problematic images over time, which is encouraging.

After the first round of review, the addition of a random sample of biomedical articles in the evaluation set strengthens the generalizability of the algorithm, and the change to evaluate articles at the article level to address pseudoreplication is appropriate.
