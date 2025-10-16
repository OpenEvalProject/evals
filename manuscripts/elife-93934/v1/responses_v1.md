# Author response - Round 1

Authors:
- Mathias Fynbo Jensen ([ORCID: 0009-0004-6664-448X](https://orcid.org/0009-0004-6664-448X))
- Morten Nielsen ([ORCID: 0000-0001-7885-4311](https://orcid.org/0000-0001-7885-4311))

## Response text

DOI: [10.7554/eLife.93934.3.sa3](https://doi.org/10.7554/eLife.93934.3.sa3)

The following is the authors’ response to the original reviews.

We thank the editor and reviewers for their valuable feedback and comments. Below we have addressed all points carefully and have, when needed, revised the manuscript accordingly.

Note that we have taken the opportunity to correct minor typos and unclear text in the revised manuscript.

Of importance to the editors and reviewers, we detected a few minor factual errors in the method section, which we have now corrected. The first error was that we wrongfully stated that our final dataset had 6358 unique TCRs, whereas it was in fact 6353 unique TCRs. The second error was that we stated that the maximum length of CDR1ꞵ was 5, where it was in fact 6. The last error was that we stated that we used a Levenshtein distance of at least 3 to discard similar peptides when swapping the TCRs to generate negatives. This should have been a Levenshtein greater than 3, to match the script we used to generate negatives (though no peptides had a Levenshtein distance of exactly 3).

eLife assessment

This important study reports on an improved deep-learning-based method for predicting TCR specificity. The evidence supporting the overall method is compelling, although the inclusion of real-world applications and clear comparisons with the previous version would have further strengthened the study. This work will be of broad interest to immunologists and computational biologists.

It is not fully clear to us what is meant by “clear comparisons with the previous version”. In the manuscript we consistently compare the performance of each novel approach introduced to that of the ancestor NetTCR-2.1. Further, we concluded the manuscript with a performance to a large set of current state-of-the-art methods by training and evaluating the novel modeling framework on the IMMREP22 benchmark data.

We agree that the manuscript can be improved by including a brief discussion of real-life applications of models for prediction of TCR specificity, and have included a brief text in the introduction.

Reviewer #1 (Recommendations For The Authors):

It was a great pleasure to read this article. All the concepts and motivations are clearly defined. I have just a few questions.

What was the motivation behind employing a 1:5 positive-negative ratio? Could it be the cause of worse performance in the case of outliers?

The ratio 1:5 is based on results from earlier work [36561755]. In this work, negatives were constructed as a mix of swapped and true (i.e measured) negatives with a ratio 1:5 for each. This work demonstrated a slight gain when including both types of negatives compared to only using swapped. In a subsequent publication [https://doi.org/10.1016/j.immuno.2023.100024], it demonstrated that optimal performance was obtained when only including swapped negatives (again in a ratio 1:5). Given this, we maintained this approach in the current work. It is clear that this choice is somewhat arbitrary, and that further work is needed to fully address this issue and the general issue of how to best generate negatives for ML of TCR specificity. Such work is in our view however beyond the scope of the current manuscript.

Why is the patience of 200 epochs for peptide-specific models and 100 epochs for pan-specific and pre-trained models used in the context of the early stopping mechanism?

We observed that the loss curve was overall very stable in the case of pan-specific training, likely due to the large amount of data included in this training. Therefore, these models were less likely to become stuck in a local minimum during training, meaning that a lower patience for early stopping would not prevent the model from learning optimally. In contrast, we found for some peptides that the loss curve was very erratic, and would sometimes become stuck in a local minimum for an extended time. To resolve this, the patience was increased from 100 to 200, which resulted in a better chance to escape these minima, as well as a better overall performance.

Why is weight 3.8 used in the weighted loss function in the pan-specific model?

The weighted loss was scaled with a division factor (c) of 3.8, in order to get an overall loss that was comparable to training without sample weights. This was primarily done to better compare the two approaches (scaling and no scaling) in terms of loss, and not so much to improve the training itself, as we already use a relatively conservative sample weight scaling based on log2. We have added a brief sentence to clarify this in the manuscript.

Reviewer #2 (Recommendations For The Authors):

This work is the evolution of previous studies that developed the NetTCR platform, and in a previous paper cited in this study, the authors explore the paired dataset approach with "paired α/β TCR sequence data". In this manuscript, the authors should make clear what advances were made when compared to the previous study. This is not clear, although extensive reference is made to NetTCR 2.0 and 2.1. Differences are scattered throughout the manuscript, so I would suggest a section or paragraph clearly delineating the advances in model architecture and training when compared to previous versions recently published.

It is not clear to us when the reviewer is referring to when stating “the authors should make clear what advances were made when compared to the previous study”. Throughout the manuscript we consistently compare the performance of each novel approach introduced to that of the ancestor NetTCR-2.1. In addition, we briefly discuss all of the changes to the architecture and training at the start of the discussion section. Further, we concluded the manuscript with a performance to a large set of current state-of-the-art methods by training and evaluating the novel modeling framework on the IMMREP22 benchmark data. It is correct that the advances are described progressively by introducing each novel approach one by one, i.e. refining the machine learning model architecture and training setup, data denoising in terms of outlier identification in the training data, new model architectures combining the properties of a pan- and peptide-specific model, and integration of similarity based approach to boost model performance. We believe this helps better justify the relevance of each of the novel approaches introduced.

In Figure 3, the colors have labels, but they are not explained in the legend or in the text. This makes it very difficult to understand the data in the various columns. Also, since it represents the Mean AUC, the data would be best displayed with a boxplot or a mean and bars for variance.

We agree, and have changed Figure 3 and its corresponding AUC 0.1 figure (Supplementary Figure 1) into a boxplot. We also further clarified what the different models were in the figure text.

Given the potential impact of this work on bioengineering and biotechnology, I would suggest adding a paragraph or section to the discussion where potential applications of the current model, or examples of applications of previous (or competing) models have been used to further biological research.

We agree and have added a brief sentence in the introduction to outline biotechnological applications of models for prediction of TCR specificity.
