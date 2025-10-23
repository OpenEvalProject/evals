# Peer review - Round 1

Editors:
- Detlef Weigel, Max Planck Institute for Developmental Biology Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61973.sa1](https://doi.org/10.7554/eLife.61973.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The work teaches us how to optimize oligo-conjugated antibodies for droplet-based scRNA-seq studies (CITE-seq). This study provides a careful assessment of oligo-conjugated antibody signal in CITE-seq, testing several relevant variables, and clearly demonstrating that antibody titration is a crucial step to optimize a CITE-seq panel.

Decision letter after peer review:

Thank you for submitting your article "Improving oligo-conjugated antibody signal in multimodal single-cell analysis" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by Michael Eisen as the Senior and Reviewing Editor. The following individuals involved in review of your submission have agreed to reveal their identity: José Ordovas-Montanes (Reviewer #1); Johan Duchene (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

In the study by Buus et al., the authors set out to address an important need to understand how oligo-conjugated antibodies should be optimally utilized in droplet-based scRNA-seq studies. These techniques, often referred to as CITE-seq, complement techniques such as flow cytometry and mass cytometry yet also further extend them by the ability to jointly measure intra-cellular RNA-based cell states together with antibody-based measurements. As is the case with flow cytometry, manufacturers provide staining recommendations, yet encourage users to titrate antibodies on their specific samples in order to derive a final staining panel. Based on the ability to stain with hundreds of antibodies jointly, few studies to date have assessed how the antibodies present in these pre-made staining panels respond to a standard titration curve. In order to address this point, this study tests two dilution factors, staining volume, cell count, and tissue of origin to understand the relationships between signal and background for a commercially available antibody panel. They arrive at the general recommendation that these panels could be improved, grouping various antibodies into distinct categories.

This study is of general interest to the scRNA-seq and CITE-seq communities as it draws attention to this important aspect of CITE-seq panel design. However, given the title is "improving oligo-conjugated antibody in multi-modal single cell analysis", the manuscript would be substantially improved by not only providing suggestions but also testing at least one, if not more, of their suggestions from Supplementary Table 2, and preferably performing experiments using more technical replicates or biological replicates. As it stands now, the study is largely based on one PBMC and one lung sample, that were stained once with each manipulation as far as can be gathered from the Methods.

Recombinant antibodies are the most common and powerful reagents in life science research to identify and study proteins. Yet, every single antibody should always be validated and carefully tested for its relevant application, to ensure constructive and reproductive scientific endeavor. I was thus extremely pleased to review the manuscript of Terkild Buus et al., as it provides a careful assessment of oligo-conjugated antibody signal in CITE-seq. The authors tested four variables (antibody concentration, staining volume, cell numbers and tissue origin) and clearly showed that antibody titration is a crucial step to optimize CITE-seq panel. The authors found that, as a general rule, concentration in the 0.625 and 2.5 µg/mL range provides the best results while recommended concentrations by vendors, 5 to 10 µg/mL range, increase background signal.

Essential revisions:

1. The starting concentration used for each antibody was based on historical experience and assumptions about the abundance of the epitopes. This approach may not be ideal, and the optimal concentration may have been missed. Do the authors think that a proper titration would be an advantage? Maybe this could be discussed in the text.As a means of testing, we suggest a full titration curve of selected antibodies, perhaps one from each of the categories, but if cost is a concern at least two or three antibodies, to identify how titration impacts antibodies, and especially those in categories labeled as in need of improvement. Relatedly, if the idea is that if antibodies (such as gD-TCR) do not have a cognate receptor leading to general background spread, does spiking in a cell that is a known positive in increasing ratios remedy this issue by acting as a target for the antibodies? Does adding extra washes help to remedy these issues of background?

2. Another way of improving these panels is through reducing the costs spent on both staining but perhaps more importantly the sequencing-based readouts. Several times in the manuscript (at line 77 for example or line 277) it is alluded to that the background signal of antibodies can make up a substantial cost of sequencing these libraries. However, no formal data on cost is presented, which would be important to formalize the author's points. It would be important to provide cost calculations and recommendations on sequencing depth of ADT libraries based on variation of staining concentration. Relatedly, in the methods, sequencing platform and read depth for ADT libraries was not discussed, nor is the RNA-seq quality control metrics provided other than a mention of ~5,000 reads/cell targeted. This is important to report in all transcriptomic studies, and especially a methods development study.

3. One of the powerful elements of joint multi-modal profiling, as mentioned in the title, is to be able to measure protein and RNA from a single cell. This study does not formally look at correlation of protein and RNA levels, and whether a decrease in concentration of antibody either improves or diminishes this correlation. This would be important to test with in this study to ensure that decreasing antibody levels does not then adversely affect the power of correlating protein with RNA, and whether it may even improve it.

Relatedly, the authors showed by testing four variables (see above) that they could define the optimal conditions to reduce background signal and increase sensitivity of antibodies and thus this way improves CITE-seq outcome. Nevertheless, the authors rely on the fact that all antibodies used in their panel are specific for their targeted antigens. It is not necessary to experimentally test the specificity of every single antibody used in the study as this would be a colossal amount of work. But I feel that this aspect should be discussed in the manuscript, especially when an "uncommon" antibody is intended to be used in the CITE-seq panel; the specificity of this antibody should be indeed tested prior to its use.

4. How was the lack of antibody binding determined for Category E? CD56 is frequently detected on NK cells in peripheral blood, CD117 should be detected on mast cells in lung, and CD127 should be found on T cells, particularly CD8+ T cells. From inspecting Figure 1E, it appears as if all three of these markers are detected on small but consistent cell subsets. As the clusters are only numbered and no supplementary table is provided to help to reader in their interpretation, it is difficult to determine if these represent rare but specific binding, or have not bound with any specificity.

5. References: At 14 references, the paper overall could benefit from a more comprehensive citation of related literature including flow cytometry and/or CyTOF best practices for antibody staining and dealing with background, and joint RNA and protein measurement from single cells.
