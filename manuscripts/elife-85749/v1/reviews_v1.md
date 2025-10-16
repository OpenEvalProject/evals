# Peer review - Round 1

Editors:
- Marisa Nicolás, https://ror.org/0498ekt05 Laboratório Nacional de Computação Científica Brazil

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85749.sa0](https://doi.org/10.7554/eLife.85749.sa0)

This landmark study presents MetaPathPredict, a method that uses deep neural networks to predict the presence or absence of KEGG modules based on annotated features in the genome. The evidence supporting the conclusions is compelling, with a tool that allows for the prediction of KEGG modules in sparse gene sequence datasets.


---

# Peer review - Round 1

Editors:
- Marisa Nicolás, https://ror.org/0498ekt05 Laboratório Nacional de Computação Científica Brazil

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85749.sa1](https://doi.org/10.7554/eLife.85749.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "MetaPathPredict: A machine learning-based tool for predicting metabolic modules in incomplete bacterial genomes" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Bavesh Kana as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions (for the authors):

Reviewer #1 (Recommendations for the authors):

I have only a few questions and comments about the paper:

1. It's possible the training set itself will have some incomplete modules dues to a mixture of novel gene families, poor gene calls, or annotation error. What steps were taken to address this possibility? Were "nearly complete" modules considered "complete", and what was the threshold?

2. The "KofamScan command line tool" was used to annotate the training set for this method. Of course, other annotation methods (e.g. DRAM) may render significant differences in the resulting functional annotations. Did the authors test if the KofamScan-trained classifiers show similar accuracy/performance when applied to annotations from DRAM or some other competing tool?

3. Would it be possible to train the method on KEGG reaction IDs so other approaches that annotate reactions directly could be applied to the method? Not suggesting the authors do this work, but it might be worth mentioning in the discussion.

4. Did the authors look at the features chosen by the classifiers for various modules? It would be interesting to know how often the top-ranking features lie within the module or outside, and when outside, what kind of feature is used?

5. The link in the PDF to the git repo (https://github.com/d-mcgrath/MetaPathPredict) is corrupted somehow and doesn't work. I suspect the "-". Manually entering the address does get me to the repo.

Reviewer #2 (Recommendations for the authors):

Observation 1: Figures 2-5 present compelling evidence of MetaPathPredict's predictive capabilities. However, the authors have not discussed the potential mechanisms that could be discovered using the stacked ensemble of neural networks. In lines 171-173, the authors mentioned that MetaPathPredict's models incorporate information from genes outside of KEGG modules, but they have not elaborated on how such information can be interpreted. While predictive power is a commendable goal, machine learning models usually trade off explanatory power for predictive power. Therefore, the authors should discuss whether the stacked ensemble of neural networks could provide biological insights (https://doi.org/10.1038/s42256-019-0048-x).

Observation 2: The authors have primarily focused on predicting the presence of complete KEGG modules, which may result in predictions that are overly conservative regarding gene essentiality. For example, some KEGG modules may have functionally redundant reactions, and an incomplete KEGG module could still lead to a viable set of metabolic reactions. To address this issue, the authors could predict gene essentiality, carbon source, or metabolic product. (For further information, see https://doi.org/10.1186/s13059-021-02295-1.)
