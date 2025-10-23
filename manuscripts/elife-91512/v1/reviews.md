# Peer review - Round 1

Editors:
- Volker Dötsch, Goethe University Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.91512.4.sa0](https://doi.org/10.7554/eLife.91512.4.sa0)

This article presents H3-OPT, a deep learning method that effectively combines existing techniques for the prediction of antibody structure. This work, supported by convincing experiments for validation, is important because the method can aid in the design of antibodies, which are key tools in many research and industrial applications.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91512.4.sa1](https://doi.org/10.7554/eLife.91512.4.sa1)

This work provides a new tool (H3-Opt) for the prediction of antibody and nanobody structures, based on the combination of AlphaFold2 and a pre-trained protein language model, with a focus on predicting the challenging CDR-H3 loops with enhanced accuracy than previously developed approaches. This task is of high value for the development of new therapeutic antibodies. The paper provides an external validation consisting of 131 sequences, with further analysis of the results by segregating the test sets in three subsets of varying difficulty and comparison with other available methods. Furthermore, the approach was validated by comparing three experimentally solved 3D structures of anti-VEGF nanobodies with the H3-Opt predictions

Strengths:

The experimental design to train and validate the new approach has been clearly described, including the dataset compilation and its representative sampling into training, validation and test sets, and structure preparation. The results of the in silico validation are quite convincing and support the authors' conclusions.

The datasets used to train and validate the tool and the code are made available by the authors, which ensures transparency and reproducibility, and allows future benchmarking exercises with incoming new tools.

Compared to AlphaFold2, the authors' optimization seems to produce better results for the most challenging subsets of the test set.

Weaknesses:

None


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91512.4.sa2](https://doi.org/10.7554/eLife.91512.4.sa2)

Summary:

The manuscript introduces a new computational framework for choosing 'the best method' according to the case for getting the best possible structural prediction for the CDR-H3 loop. The authors show their strategy improves on average the accuracy of the predictions on datasets of increasing difficulty in comparison to several state-of-the-art methods. They also show the benefits of improving the structural predictions of the CDR-H3 in the evaluation of different properties that may be relevant for drug discovery and therapeutic design.

Strengths:

The authors introduce a novel framework, which can be easily adapted and improved. Authors use a well-defined dataset to test their new method. A modest average accuracy gain is obtained in comparison to other state-of-the art methods for the same task, while avoiding testing different prediction approaches. Although the accuracy gain is mainly ascribed to easy cases, the accuracy and precision for moderate to challenging cases is comparable to the best PLM methods (see Fig. 4b and Extended Data Fig. 2), reflecting the present methodological limit in the field. The proposed method includes a confidence score for guiding users about the accuracy of the predictions.
