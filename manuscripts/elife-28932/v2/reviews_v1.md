# Peer review - Round 1

Editors:
- Charles L Sawyers, Memorial Sloan-Kettering Cancer Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.28932.037](https://doi.org/10.7554/eLife.28932.037)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: this article was originally rejected after discussions between the reviewers, but the authors were invited to resubmit after an appeal against the decision.]

Thank you for submitting your work entitled "Diagnostic potential for a serum miRNA neural network for detection of ovarian cancer" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

Although all reviewers acknowledge the strengths of the topic of predicting early stage disease and the analysis, the consensus is that the work lacks sufficient novelty for the general audience of eLife. Specifically, there are a couple of prior publications on miR detection in serum of ovarian cancer patients, and we are not persuaded that the machine learning algorithms used here represent the level of innovation we require. Second, the biological underpinnings of the predictive miR signature are not addressed, nor is the source of the miRs (are they from tumor cells?). Third, in the absence of a biological hypothesis, we would expect further work to eliminate many of the caveats raised about clinical utility, tumor samples with various histologies, further validation, etc.

Reviewer #1:

The authors present a paradigm for serum detection of ovarian cancer. They employ a neural network to discriminate between cancer and noncancer specimens and demonstrate specificity with published data. The paper has many strengths including a range of ovarian cancer specimens of various histologic subtypes and stages. There is very nice demonstration of training, test and external validation. Enthusiasm is somewhat weakened, due to:

1) Multiple statistical algorithms are tested leading to some concern for overfitting during creation of the original model.

2) There is little to no detail about the histology and stage of the external validation specimens and the small sample size of only 15 ovarian cases for external validation remains hidden within the methods. It would be good to know the histology and stage and more details about the collection methods for the external validation samples.

3) It is not clear how the samples were collected in Keller et al. and whether they were all from newly diagnosed patients prior to treatment.

Overall, this seems like a very promising signature, but past experience would suggest some additional externally validated samples should be included.

Reviewer #2:

Elias and colleagues have evaluated the utility of circulating miRNA as a potential tool to assist in the diagnosis of ovarian cancer. They identify miRNAs and an algorithm that distinguishes individuals without ovarian cancer from patients with cancer.

There are many publications describing miRNAs as a biomarker in ovarian cancer. Although the authors mention some of these previous studies examining circulating miRNAs in the Introduction, it is unclear whether the miRNAs utilised in the neural network algorithm overlap with those described in previous studies. It would strengthen the manuscript to compare the findings to previous work more explicitly.

The manuscript could also be strengthened by examining the potential of the algorithm and miRNAs to predict prognosis, as a biomarker that can be utilised for diagnosis and prognosis is very desirable.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for choosing to send your work entitled "Diagnostic potential for a serum miRNA neural network for detection of ovarian cancer" for consideration at eLife. Your letter of appeal has been considered by a Senior Editor and a Reviewing Editor, and we are prepared to consider a revised submission with no guarantees of acceptance.

We are particularly interested in the inclusion of data regarding the biological underpinnings of the miR signature and additional external validation on another cohort of patients. It will also be important to emphasize the novelty relative to prior published analyses of serum miRs in ovarian cancer. As a dataset but without a biological rationale for the set of enriched miRNAS, this work appears to be more appropriately considered as a Tools and Resources paper, rather than as a Research Article.
