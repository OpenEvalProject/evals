# Peer review - Round 1

Editors:
- Goutham Narla, University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68699.sa1](https://doi.org/10.7554/eLife.68699.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The authors have done an admirable job responding to the reviewers and editorial board members. They have increased the number of cases/pedigrees analyzed using this novel modeling tool. They have also outlined how to practically use this program for users.

Decision letter after peer review:

Thank you for submitting your article "PanelPRO: An R package for multi-syndrome, multi-gene risk modeling for individuals with a family history of cancer" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Editors have drafted this to help you prepare a revised submission.

Essential Revisions:

Overall the reviewers felt that this is outstanding manuscript with potential broad impact in the cancer genetics and oncology community as highlighted in the reviews below. There are a couple of key revisions that are recommended prior to the manuscript being acceptable for publication.

1) Additional examples of cases and the output from the analysis performed on these example cases with comparison when appropriate to existing programs.

2) More details about the practical uses of the program in the clinic and discussion about the ability to import data from existing clinical platforms into PanelPRO.Reviewer #1:

This is an outstanding paper that develops and validates a new germline analysis tool for inputting family history and germline sequencing data into a user friendly interface that can be then used to calculate the risk architecture of a given family based upon both ascertained family history information as well as DNA sequencing results.

There are a number of strengths in this manuscript including:

1. The work and program generated here is novel and has a number of advantages to the existing software / platforms currently available to the cancer genetics community – it is more comprehensive in genes that can be inputted and in the family history architecture that can be ascertained.

2. The paper is well written and is able to clearly followed with the methods laid out thoroughly and comprehensively.

3. The impact of this work to the cancer genetics and oncology community will be immediate and I can envision and predict widespread adoption of this software platform in the near term.

One weakness to be noted is that more example cases could be included as test and validation examples and to show the results from the analysis being performed. When appropriate and relevant perhaps a comparison of the results to currently available platforms to analyze germline sequencing data would be of value and strengthen the paper.

Reviewer #2:

This work describes an R package called PanelPRO that seeks to assist in identifying individuals at increased risk of cancer due to inherited germline mutations in multiple genes. This tool integrates pedigree data and, importantly, has the ability to be updated as new cancer predisposition genes are discovered and peer-reviewed data on cancer risk becomes available. Patient factors such as risk-reducing surgeries and tumor biomarkers can also be incorporated as part of the risk evaluation. This allows for more personalized risk predictions compared to existing risk prediction models.

Strengths:

This R package offers many advantages over existing programs with similar intended uses. The authors highlight this by noting the limited cancer types and genes considered by existing tools and contrasting this to the capabilities of PanelPRO. Specifically, the authors provide clear examples of this software's ability to incorporate family histories with several different cancer types and to provide an output for prediction of finding a germline pathogenic variant in multiple genes as well as individualized future cancer risk. It also allows users to include individual level risk factors and biomarkers, resulting in a more personalized risk assessment when compared to existing tools. There are several other features that can be changed based on user preference, providing users with a high level of customization. The flexibility to make updates to the R package to reflect changes in the field of cancer genetics is another strength of this work. PanelPRO is designed to be compatible with an existing risk-modeling package, BayesMendel.

The authors provide a clear workflow explaining the use of the package and provide the necessary information to access it in its currently available form. The different variables, notations, and customizable features of the program are clearly explained in the manuscript. Many important variables from the family history that cannot be included in risk assessments using currently available tools can be incorporated into PanelPRO. There are several examples showing different features and capabilities of the program that improve on existing tools. Instructions for use with pedigree information appear to be clear for those familiar with R software. Some limitations of the technology are noted but suggestions to address the described limitations are included.

Weaknesses:

While the strengths of the PanelPRO package are evident, discussion around its use in practice is lacking. By excluding this aspect, potential limitations related to implementation and use are not addressed here, but are key in determining the potential impact of this software in the field. It is not noted if this new package is intended for use in clinical practice, research, or both. Proposed users include users of the existing BayesMendel package, so providing information about users of the BayesMendel package (clinicians versus researchers, volumes, etc) could help readers determine possible applicability of PanelPRO to their own practice. While the authors posit new users may be interested in this software due to its enhanced abilities, further information on new potential users is not included. Due to the absence of discussion of use of this package in a clinical and/or research setting, the likely uptake and impact of this work on the field is difficult to determine. Broader audiences may benefit from more context surrounding existing cancer risk models and their use in cancer genetics to better appreciate the improvements noted here compared to traditional risk modeling programs.

One of the strengths of PanelPRO is the capability for software updates as new knowledge about hereditary cancer syndromes and associated pathogenic variants becomes available. Although this software has the ability to customize the allele frequency and penetrance for a requested gene, meaning it can accommodate predictions for genes not built into its software, built-in gene data relies on published, peer-reviewed data for allele frequencies and penetrance. Additional context surrounding how new genes get added to PanelPRO would help readers understand the significance of the work.

While the improvements compared to existing programs are clear, context around the current use of available risk models in practice, and specific examples of intended use, would help the reader better appreciate the potential significant impact of PanelPRO in clinical and/or research cancer genetics settings. Information about the ability to import data directly from popular pedigree programs would also help determine the potential uptake and impact.
