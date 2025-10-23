# Peer review - Round 1

Editors:
- Goutham Narla, University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65543.sa1](https://doi.org/10.7554/eLife.65543.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

The authors have developed and validated an important tool for the scientific community specifically those interested in drug development and experimental therapeutics. Additional analysis using several comparative analyses on the golden standard sets of drug metabolism, drug toxicities, and drug targets, that further demonstrate the advantage of NICEdrug.ch over similar methods in the field have now been provided. Furthermore, they have now prepared a detailed user-guide that walks through NICEdrug.ch interface step by step using screenshots that visually explain to users how they can navigate the website. In addition, they have addressed the issue of open access to their platform.

Decision letter after peer review:

Thank you for submitting your article "NICEdrug.ch: a workflow for rational drug design and systems-level analysis of drug metabolism" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Mone Zaidi as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Adil Mardinoglou (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

As the authors can see there was significant enthusiasm for the work but several of the concerns raised by the reviewers need to be addressed.

Essential Revisions (for the authors):

1) Address the issue raised about the lack of quantitative assessment of the pipeline.

2) Address the issue of usability.

3) Address the open access issue raised by the reviewer.

Reviewer #1 (Recommendations for the authors):

Some concerns are listed below:

1. Validation is performed by using PubChem Bioassays database. The authors may include additional literature validation to support their findings.

2. How the authors handle the predictions of enzymes with more than one EC number? Please provide additional information.

3. How the authors handle the discrepancies while collecting information from different databases?

4. "We assumed an enzyme is druggable when the NICEdrug.ch score between the drug and the enzyme's native substrate is above 0.3." Similarly, throughout the study, NICEdrug.ch threshold score was 0.5. How is this 0.3 and thresholds settled? What is the rationale behind this?

5. It is necessary to have no significance control (p-value or FDR) to remove the false positive when predicting drug-enzyme/target pairs. The authors should provide additional information about it.

6. A benchmarking is performed with a chosen tool named Biotransformer, however an extension of comparison with commonly used methodologies would improve the value of this paper.

Reviewer #2 (Recommendations for the authors):

1) Two of the most critical drawbacks are, first, the lack of quantitative assessment of the abilities of the service and its analysis pipeline. Use cases provide valuable information; however, it is not possible to assess the overall value of any computational tool/service without large-scale quantitative analyses. One analysis of this kind has been done and explained under "NICEdrug.ch validation against biochemical assays" and "Comparison of NICEdrug.ch predictions and biochemical assays"; however, this is not sufficient as both the experimental setup and the evaluation of results are quite generic (e.g., how to evaluate an overall accuracy of 0.73 without comparing it to other computational methods that produce such predictions, as there are many of them in the literature). Also, similar quantitative and data-driven evaluations should be made for other sections of the study as well.

2) The second critical issue is that, in the manuscript, the emphasis should be on NICEdrug.ch, since most of the underlying computational methods have already been published. However, the authors did not sufficiently focus on how the service can actually be used to conduct the analysis they mention in the use cases (in terms of usability). Via use cases, authors provide results and its biological discussion (which actually is done very well), but there is no information on how a potential user of NICEdrug.ch (who is not familiar with this system before and hoping to get an idea by reading this paper) can do similar types of analyses. I recommend authors to support the textual expressions with figures in terms of screenshots taken from the interface of NICEdrug.ch at different stages of doing the use case analyses being told in the manuscript. This will provide the reader with the ability to effectively use NICEdrug.ch.

3) "NICEdrug.ch identifies toxic alerts in the anticancer drug 5-FU and its products from metabolic degradation."

This is quite nice and informative as a case study; however, to indicate the effectiveness of NICEdrug.ch in identifying toxic alerts in general (rather than on just drug), I recommend authors to carry out a quantitative analysis using a tox-based benchmark dataset and calculate the performance of their method on this dataset, and discuss the results (this can be read as a part of issue 1).

4) "Furthermore, we filtered molecules based on Lipinski rules (Lipinski et al., 2001)"

This filtering operation probably causes the discarding of many drugs. For example, there are roughly 10000 unique small molecule drug entries in DrugBank (investigational/experimental + approved). Here, only 3716 have been selected. It is also known that some of the approved drugs do not obey Lipinski rules. So, this application probably filtered out those approved drugs. Wouldn't it be better to keep, at least, all approved drugs in the database of NICEdrug.ch and to provide the functionalities of the service for those molecules? I presume many users would be interested to query those drugs.

5) Requesting the "Molecule NICEdrug ID" to start a query is highly impractical. Each time the user should go and check the id, then come back to paste it to the box to start the search. I highly recommend authors to add the functionality of searching with name, well-known database ids, and SMILES/InChIKey in these fields.

6) In today's scientific research, open science is one of the most important aspects, and sharing tools, datasets and scripts/source codes/implementations is an important part of it. I observed that authors share their studies/findings/methods over a nicely prepared website/service, considering both the included functionalities and usability; however, requesting registration for letting people use the resource, and doing this via writing an email to the team is not a good practice in my opinion. Many journals that support the open-science movement do not allow the registration requirements for the tools/databases/services published in their journal.

I believe authors have done this just to yield control over who uses their service (i.e., for allowing academic researchers to use the services/tools/databases freely, but not allowing commercial users). However, I believe this is not a good solution. I recommend authors to let access to NICEdrug.ch without the requirement of registration.
