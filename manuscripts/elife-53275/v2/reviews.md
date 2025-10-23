# Peer review - Round 1

Editors:
- Mone Zaidi, Icahn School of Medicine at Mount Sinai United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53275.sa1](https://doi.org/10.7554/eLife.53275.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

We feel that the study is important as it touches on an emerging area of data sharing, provenance and reproducibility – a nascent movement towards achieving rigor and transparency that is being adopted by funding agencies, journal editors and industry alike. Applying the concept of synthetic datasets, in this case using SynthpopR, is seen as innovative and applicable to a wide range of investigations, importantly to those where full data and identity disclosure are not possible. The tool is likely to be utilized widely in translational and clinical research.

Decision letter after peer review:

Thank you for submitting your article "Synthetic datasets: A primer for the biobehavioural sciences to promote reproducibility and hypothesis-generation" for consideration by eLife. Your article has been reviewed by Christian Büchel as the Senior Editor, Mone Zaidi as the Reviewing Editor, and two reviewers. The following individual involved in review of your submission has agreed to reveal their identity: Dorothy VM Bishop (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Creation of synthetic datasets has been adopted in some areas of social science where large survey datasets are used, and where full anonymisation is difficult or impossible. Here, the author demonstrates the usefulness of the synthpop R package for generating synthetic data in a different field, where datasets are typically smaller and simpler.

While the paper does not add new empirical observations or analysis approaches, it is, as its title indicates, a primer for others who might wish to try this approach. It highlights the benefits of synthetic datasets as compared to open research data. Importantly, the use of synthetic datasets shows reliable general utility in terms of data reproducibility of original findings. As long as the risk of identity disclosure is eliminated, synthetic datasets can and should be employed given the reproducibility of scientific data in biomedical sciences is a growing issue. The inclusion of oxytocin data re-analyzed in the synthetic datasets is a strength. The data are strong and well presented. The manuscript is clearly written for the most part and delivers a straightforward message that would be useful to a general readership. Nonetheless several areas need improvement and further analysis.

Essential revisions:

1) It would be preferable to have more diversity in the illustrative datasets – perhaps even demonstrating a case when synthpop does not perform as well. In particular, questions were raised regarding data with unusual distributions, evident outliers, or a hierarchical structure, for example, those with a code for family, and then family members.

2) There is mention in the Discussion section about cases where the synthetic dataset has poor utility. Perhaps, this cannot be predicted in advance, but it would be interesting to test this with datasets that may have the kinds of characteristics that are noted in point 1 (above). Indeed, this would all get rather meta, but one could simulate data that has specific features, such as striking outliers or non-normal distributions, to determine how far synthpop could retain its utility in such situations. Maybe this would be a better use of the second demonstration (see point 3). Would it be possible to take the original dataset and throw in some outliers or transform distributions to push synthpop to determine how well it stands up to non-normal data and the likes.

3) The three illustrative cases seem repetitive. Examples 1 and 3 show how the package worked with relatively large and small datasets, respectively, but example 2 seemed unnecessary. It is suggested that this part of an online appendix or is utilized it as noted in point 2 (above).

4) There is the issue about discarding data points that happen to replicate a real individual by chance. It is mentioned in the Introduction, again in Results section and in the Discussion section. A reviewer isn't sure about the logic of removing these. How would the individual – or anyone else – know this was their data? There is a problem with de-identification in a real dataset. For example, one knows that someone is a 55-year-old, left-handed woman, and there is only one of those in the sample. But if one knows that a dataset is synthesized, one could not be confident that the remainder of the data in that row came from this person.

5) It would be critical to model missing data. This might have an impact on fidelity of the synthetic data.
