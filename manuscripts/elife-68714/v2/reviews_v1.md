# Peer review - Round 1

Editors:
- Arduino A Mangoni, Flinders Medical Centre Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68714.sa1](https://doi.org/10.7554/eLife.68714.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study presents a deep learning approach plus iPSC-based high-throughput screening data for risk assessment of cardiotoxicity in the early phase of drug discovery. The authors demonstrate reasonable accuracy using a library of 1,280 bioactive compounds. Overall, this is an interesting study which provides potential tools for risk assessment of cardiotoxicity the early phase of drug discovery if broadly applied.

Decision letter after peer review:

Thank you for submitting your article "Deep Learning Predicts Patterns of Cardiotoxicity in a High-Content Screen Using Induced Pluripotent Stem Cell-Derived Cardiomyocytes" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Dr. Feixiong Cheng (Reviewer #2).

The Reviewers and Editors have discussed their reviews with one another, and this decision letter is to help you prepare a revised submission.

Essential Revisions:

1) The article lacks practical discussion, considerations and recommendations on how to validate the cardiotoxicity score when aiming to predict clinical drug cardiotoxicity, which will require comparing with clinical data.

2) This reviewer recommends the authors to read the review manuscript by Walker and colleagues published in 2020 in the journal Archives of Toxicology and entitled "The evolution of strategies to minimise the risk of human drug‑induced liver injury (DILI) in drug discovery and development" to understand how the pharmaceutical industry uses image-based data to predict clinical toxicity. Despite describing applications in liver toxicity, since it focuses extensively on image-based approaches, the practical approaches of the article can be easily translatable to the predictive effort of the neural network method in the cardiotoxicity arena.

3) This reviewer especially recommends considering Cmax or Cmax unbound of tested drugs and investigating IC50 cutoff values for predicting drug safety ranges in relation to the proposed cardiotoxicity score.

4) It is not clear how the deep learning approach outperform traditional approaches, such as doi: 10.1126/scitranslmed.aaf2584.

5) For deep learning models, it is not clear how the authors perform hyperparameter tuning, a key issue for deep learning models.

6) The authors are suggested to compared iPSC-based image-based deep learning models with traditional chemoinformatics approaches, such as random forest-based structure-activity relationships approach.

7) The reviewer is confused why the authors presented ProBNP assays. The authors only show negative results of ProBNP; yet, how it related to the deep learning models in current manuscript.

8) Cardiotoxicity is highly time-dependent and dose-dependent. How the authors address time-dependent and dose-dependent cardio-toxicity in their deep learning models.

9) The authors presented transcriptomics and metabolism analysis. How these omics layers can be integrated into deep learning models in the future studies?

10) The codes and data should be provided in public domains, such as GitHub or other open source websites.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Deep Learning Predicts Patterns of Cardiotoxicity in a High-Content Screen Using Induced Pluripotent Stem Cell-Derived Cardiomyocytes" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Matthias Barton as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Feixiong Cheng (Reviewer #2).

Essential Revisions:

Comment 1– It is difficult to understand how this method (cardiotoxicity score) is predictive of clinical cardiotoxicity if the score is dependent on the training data and drugs used because clinical cardiotoxicity due to drug-induced effects will occur for drugs independently of what would be the surrogate of training data or reference drugs in clinical trials. Probably authors could avoid stating this method as predictive, but instead should present it as an approach for comparing potential cardiotoxic effects between new drugs and reference drugs without predicting clinical safety ranges. A drug can be safe if the range of efficacious concentrations is safely below the toxic range. If the authors still aim to demonstrate that the presented method is predictive of clinical data, a more reflected response to this comment is recommended, taking in consideration the current approaches in the field to test the clinical predictiveness of in vitro data. Since so much clinical and animal data is publicly available for several of the used drugs, it is unconceivable for approaches that aim to be predictive of clinical data to ignore these.

Comments 2 and 3 – There is no proof of principle results or proposed/ described comprehensive strategy or recommendations to predict clinical data from the results derived from this method. In line with the previous comment, the authors seem to be pretending that most of the used drugs are new drugs and that no clinical data is available. The authors also seem to pretend that clinical data is not currently predicted from in vitro cellular data to estimate safety ranges of drug concentration. The authors should rethink their response, especially when considering that some of the used drugs have been used for so long clinically. These are not investigational drugs. If authors want to "pitch" this method as predictive, please add information on how to predict clinical data from it considering how other authors in the field already predict clinical toxic drug effects (safety ranges) from in vitro cellular data. The results from at least one drug should be demonstrated to be predictive and not false-positives or false-negatives. Alternatively, this effort will not be necessary if authors remove from the manuscript any claims that this method is predictive of drug cardiotoxicity.
