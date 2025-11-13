# Peer review - Round 1

Editors:
- Peter Koo, Cold Spring Harbor Laboratory United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.107454.3.sa0](https://doi.org/10.7554/eLife.107454.3.sa0)

This valuable study introduces a modern and accessible PyTorch reimplementation of the widely used SpliceAI model for splice site prediction. The authors provide convincing evidence that their OpenSpliceAI implementation matches the performance of the original while improving usability and enabling flexible retraining across species. These advances are likely to be of broad interest to the computational genomics community.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.107454.3.sa1](https://doi.org/10.7554/eLife.107454.3.sa1)

Summary:

Chao et al. produced an updated version of the SpliceAI package using modern deep learning frameworks. This includes data preprocessing, model training, direct prediction, and variant effect prediction scripts. They also added functionality for model fine-tuning and model calibration. They convincingly evaluate their newly trained models against those from the original SpliceAI package and investigate how to extend SpliceAI to make predictions in new species. Their comparisons to the original SpliceAI models are convincing on the grounds of model performance and their evaluation of how well the new models match the original's understanding of non-local mutation effects. However, their evaluation of the new calibration functionality would benefit from a more nuanced discussion of the limitations of calibration.

Strengths

(1) They provide convincing evidence that their new implementation of SpliceAI matches the performance and mutation effect estimation capabilities of the original model on a similar dataset while benefiting from improved computational efficiencies. This will enable faster prediction and retraining of splicing models for new species as well as easier integration with other modern deep learning tools.

(2) They produce models with strong performance on non-human model species and a simple well well-documented pipeline for producing models tuned for any species of interest. This will be a boon for researchers working on splicing in these species and make it easy for researchers working on new species to generate their own models.

(3) Their documentation is clear and abundant. This will greatly aid the ability of others to work with their code base.

Weaknesses

(1) Their discussion of their package's calibration functionality does not adequately acknowledge the limitations of model calibration. This is problematic as this is a package intended for general use and users who are not experienced in modeling broadly and the subfield of model calibration specifically may not already understand these limitations. This could lead to serious errors and misunderstandings down the road. A model is not calibrated or uncalibrated in and of itself, only with respect to a specific dataset. In this case they calibrated with respect to the training dataset, a set of canonical transcript annotations. This is a perfectly valid and reasonable dataset to calibrate against. However, this is unlikely to be the dataset the model is applied to in any downstream use case, and this calibration is not guaranteed or expected to hold for any shift in the dataset distribution. For example, in the next section they use ISM based approaches to evaluate which sequence elements the model is sensitive to and their calibration would not be expected to hold for this set of predictions. This issue is particularly worrying in the case of their model because annotation of canonical transcript splice sites is a task that it is unlikely their model will be applied to after training. Much more likely tasks will be things such as predicting the effects of mutations, identification of splice sites that may be used across isoforms beyond just the canonical one, identification of regulatory sequences through ISM, or evaluation of human created sequences for design or evaluation purposes (such as in the context of an MPSA or designing a gene to splice a particular way), we would not expect their calibration to hold in any of these contexts. To resolve this issue, the authors should clarify and discuss this limitation in their paper (and in the relevant sections of the package documentation) to avoid confusing downstream users.

(2) The clarity of their analysis of mutation effects could be improved with some minor adjustments. While they report median ISM importance correlation it would be helpful to see a histogram of the correlations they observed. Instead of displaying (and calculating correlations using) importance scores of only the reference sequence, showing the importance scores for each nucleotide at each position provides a more informative representation. This would also likely make the plots in 6B clearer.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.107454.3.sa2](https://doi.org/10.7554/eLife.107454.3.sa2)

Summary:

The paper by Chao et al offers a reimplantation of the SpliceAI algorithm in PyTorch so that the model can more easily/efficiently be retrained. They apply their new implementation of the SpliceAI algorithm, which they call OpenSpliceAI, to several species and compare it against the original model, showing that the results are very similar and that in some small species pre-training on other species helps improve performance.

Strengths:

On the upside, the code runs fine and it is well documented.

Weaknesses:

The paper itself does not offer much beyond reimplementing SpliceAI. There is no new algorithm, new analysis, new data, or new insights into RNA splicing. There is not even any comparison to many of the alternative methods that have since been published to surpass SpliceAI. Given that some of the authors are well known with a long history of important contributions, our expectations were admittedly different. Still, we hope some readers will find the new implementation useful.

Update for the revised version:

The update includes mostly clarifications for tech questions/comments raised by the other two reviewers. There is no additional analysis/results that changes our above initial assessment of this paper's contribution.
