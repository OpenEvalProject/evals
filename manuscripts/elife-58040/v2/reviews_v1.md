# Peer review - Round 1

Editors:
- Mone Zaidi, Icahn School of Medicine at Mount Sinai United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58040.sa1](https://doi.org/10.7554/eLife.58040.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

We understand that the mechanism through which SARS-CoV-2 interacts with human tissues is at best unclear. In that regard, both the nferX platform and your scientific findings are topical and are likely to be of wide-ranging interest to physicians, physician-scientists and scientists, as well as to a broader readership.

Decision letter after peer review:

Thank you for submitting your article "Knowledge synthesis of 100 million biomedical documents augments the deep expression profiling of coronavirus receptors" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Mone Zaidi as the Reviewing Editor and Matthias Barton as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments and/or clarifications are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

This study examines single cell sequencing datasets for the expression of SARS-CoV-2 receptors in cell subsets from 25 tissues and considers potential roles in the disease. The study also connects these datasets to a novel machine learning method to additionally measure the literature associations in an unbiased manner that map back onto the single cell sequencing data. The analysis provides a deep analysis of the expression of SARS-CoV-2 receptors and allows for many interesting tissue type specific hypotheses to be entertained.

Summary:

Overall, the reviewers considered the approach to be novel and to facilitate a characterization of cells with the potential to be SARS-CoV-2 targets. The study further provides a useful resource that examines many tissues in considerable depth. Notably, the authors accurately suggest that with expanding availability of complex datasets, there is an increasing need for integrative tools that will assimilate the available information. In this respect, they use ACE2 and other putative coronavirus receptors and profile their expression across a spectrum of body tissues. The idea that this may become a broader resource for all genes was thus considered a welcome one. With that said, there are considerable issues with the analysis and integration that need to be resolved satisfactorily before further consideration.

Essential revisions:

1) The analyses seem to be confirmatory of existing literature and this approach is unable to resolve discordance between tissue expression and pathological phenotypes. As an example, while the authors demonstrate renal and intestinal hot spots of ACE2 expression with relatively lower ACE2 expression in the lungs, it is increasingly clear that the lung is the organ that drives the majority of the disease pathogenesis. Their approach is thus unable to provide novel information that could explain this discrepancy. For example, are there explorable differences between the co-expression of tissue proteases such as TMPRSS2 and ACE2 between the kidney, lung and intestines?

2) The authors describe the ambitious approach to pan-tissue profiling of ACE2 expression by applying neural network platform and triangulating with the available transcriptome/proteome data. Throughout the analysis, however, local context score and global context score did not help in identifying the correlation of ACE2 expression with the COVID-19 pathogenicity except for kidney proximal tubular cells (local context score > 3). A well-known SARS-CoV-2 reservoir, respiratory tissue, was scored insignificant which is raising the question about the platform's performance. Is there room to improve the performance of the nferX based on this study, and

do the authors think that the nferX platform is still crucial for the analysis compared to the transcriptome/proteome analysis alone other than identifying underappreciated tissue/cell types?

3) In the same context, the authors were not able to prove the synergetic performance of unsupervised machine learning from unstructured text data and the big data analysis yet trying to oversell their "deep learning" platform. They should revise the performance of their neural network platform or re-structure the manuscript without the integrating the neural network platform.

4) The authors state that hypothesis-free profiling of ACE2 expression was conducted, yet respiratory tissues were prioritized despite the low ACE2 expression and insignificant local scores (local context score < 3) derived from the neural network platform. Do the authors now consider the manual curation of clinical information necessary for the understanding of the pathogenesis?

5) Concern arises from the author's statement that even low ACE2 expression in lung cells may be sufficient for the pathogenesis. The obvious analysis would need a look at the expression in the spatial context and determine if the ACE2 expression level differs based on the location within the respiratory tissue.

6) Please discuss the findings in relation to the Cell paper (April 27).

7) The authors should consider comparing scRNAseq data and single cell proteomics data and examine the expression discrepancy. This will considerably strengthen the manuscript.
