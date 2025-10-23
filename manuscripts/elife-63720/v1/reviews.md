# Peer review - Round 1

Editors:
- Gordon J Berman, Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63720.sa1](https://doi.org/10.7554/eLife.63720.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Segalin and colleagues present a pair of open-source software tools – MARS and BENTO – for automatic pose detection, social behavior detection, and interactive neural/behavior visualization in mice. MARS builds on previous tools for social behavior annotation, but now eliminating the need for two cameras and for a depth signal, incorporating deep learning, and building in robustness to neural implants. BENTO further extends this work by adding a suite of tools for annotating video frames, visualizing neural activity, and performing simple operations on the neural activity data such as event-triggered averaging. Importantly, Segalin and colleagues also share a large-scale dataset to train this system. Together, these tools will be useful for researchers studying the neural underpinnings of rodent social behavior, in particular with the resident intruder assay.

Decision letter after peer review:

Thank you for submitting your article "The Mouse Action Recognition System (MARS): a software pipeline for automated analysis of social behaviors in mice" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Kate Wassum as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Asaf Gal (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Segalin and colleagues present a pair of open-source software tools – MARS and BENTO – for automatic pose detection, social behavior detection, and interactive neural/behavior visualization in mice. MARS builds on previous tools for social behavior annotation, but now eliminating the need for two cameras and for a depth signal, incorporating deep learning, and building in robustness to neural implants. BENTO further extends this work by adding a suite of tools for annotating video frames, visualizing neural activity, and performing simple operations on the neural activity data such as event-triggered averaging. Importantly, Segalin and colleagues also share a large-scale dataset to train this system. Together, these tools will be useful for researchers studying the neural underpinnings of rodent social behavior, in particular with the resident intruder assay.

The reviewers were generally enthusiastic about this submission, but would like to see several revisions before recommending for acceptance in eLife. An additional point, however, was the reviewers thought that this article was more suitable as a "Tools and Resources" article (see guidelines here: https://reviewer.elifesciences.org/author-guide/types ), so we ask the authors to make their revisions with this classification in mind.

Essential revisions:

1) The authors promise at several points that features will become available in the future, including:

(1) A Python implementation of BENTO (MARS is already implemented in Python, whereas BENTO is currently implemented in Matlab);

(2) The ability the ability to detect behaviors in pairs of mice with the same coat color;

(3) The ability to train MARS on one's own behavior annotations.

While features 1 and 2 can, of course, wait – software takes time to develop – the absence of feature 3 is a little more confusing. BENTO appears to include an interface for annotating frames. Is it not possible for MARS to read these annotations and to include a framework in which a new classifier is trained? This is important because the repertoire of behaviors captured by the MARS classifier is limited. The previous rodent social behavior detection papers cited by the authors (e.g. refs 29,30 and 33) include a much richer menu of behavior labels (for example SimBA [ref 33] includes "attack, pursuit, lateral threat, anogenital sniffing, allogrooming normal, allogrooming vigorous, mounting, scramble, flee, and upright submissive"). Moreover, the authors have richer annotations available within their own training data. In the Methods, the authors note that many of the original video annotations used for this study actually did include a much higher resolution of labels, but that these labels were collapsed for training MARS. For example, the frames labeled "close investigation" are actually the union of five different labeled categories. "Sniff face, Sniff genitals, Sniff body, Attempted attack, Attempted mount. Why were these combined, given that I would expect them to have very different neurobiological correlates. For example "attempted attack" would appear to have more in common with "Attack" than with "Sniff body".

2) The authors argue at several points that supervised classification can benefit the neuroscience community by creating a common definition of social behaviors would be interoperable between labs, that could, for example "facilitate comparison of behavioral results between labs, fostering large‐scale screening of social behaviors within a common analysis platform." This paper would be stronger if the authors could spell out a formula for finding consensus between annotators; given these principles, perhaps MARS could be trained to reflect this consensus. Perhaps trained MARS models could contain one or more tuning parameters, so that every annotator could be captured by some value(s) of the parameters, thus providing a unified framework while accommodating individual variation in annotation habits?

3) Multiple datasets are provided, one particularly novel one is the 10 x 10min videos of resident intruder assays, annotated by 8 individuals. It would be spectacular if those videos could be annotated a second time by the same individuals. Mainly, to see if individuals are consistent with themselves (stable style). This would nicely complement the dataset. In the description of the datasets, the relationships are sometimes not clear, e.g. is the person that annotated the large-scale dataset of ~14h also one of the 8 individuals and if yes, then which one?

4) The reviewers wanted to make sure that the 14 hour dataset will be shared (this was not clear from the manuscript). Moreover, when the reviewers attempted to download the dataset it was corrupted (this was replicated by two reviewers and the reviewing editor). In addition, the reviewers wanted to make sure that the data contains all the appropriate meta-data (e.g., annotation images/videos, which genotype the mice have, when the data was recorded, camera type, etc. )

5) The analyzed datasets and training data were all collected in the same lab, using the same standard setup, under very similar conditions that do not capture the variability expected across the many labs that use this assay. In order to be useful to other users, the conditions at which the method will work must be explicitly discussed. This is especially concerning, as the version of MARS presented in the paper does not allow users to define their own pipelines or to fine-tune the supplied one with new data. Furthermore, the feature list of the behavioral classifiers contains features that are very setup specific (e.g., distance to arena wall, absolute coordinates etc.), or organism-line specific (e.g. mouse size/area). If the authors indeed aim at creating a standardized behavior classification pipeline, which can be compared across labs, it is essential to show/discuss how the method gives consistent results across at least some of the different experimental variants of this assay.

6) Although the paper describes the algorithm well, if was hard for the reviewers to judge the actual usability and quality of the tool without access to it. The software should be made available to the reviewers (with documentation).

7) While a direct comparison to other social tracking methods (e.g., maDLC, SLEAP, others) is not necessary here, it is important to have a more comprehensive error analysis of the tracking (while the animals are in the bounding box, minimally).

8) Please ensure full statistical reporting in the main manuscript (e.g., t, F values, degrees of freedom, p value, etc.).
