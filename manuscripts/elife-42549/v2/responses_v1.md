# Author response - Round 1

Authors:
- Martin Wegner ([ORCID: 0000-0001-6403-3926](https://orcid.org/0000-0001-6403-3926))
- Valentina Diehl
- Verena Bittl
- Rahel de Bruyn
- Svenja Wiechmann
- Yves Matthess ([ORCID: 0000-0003-4040-1258](https://orcid.org/0000-0003-4040-1258))
- Marie Hebel
- Michael GB Hayes
- Simone Schaubeck
- Christopher Benner
- Sven Heinz
- Anja Bremm ([ORCID: 0000-0003-1386-0926](https://orcid.org/0000-0003-1386-0926))
- Ivan Dikic ([ORCID: 0000-0001-8156-9511](https://orcid.org/0000-0001-8156-9511))
- Andreas Ernst
- Manuel Kaulich ([ORCID: 0000-0002-9528-8822](https://orcid.org/0000-0002-9528-8822))

## Response text

DOI: [10.7554/eLife.42549.044](https://doi.org/10.7554/eLife.42549.044)

Four areas of concern are highlighted below:

1) There was general enthusiasm for the library generation strategy and as well as the value of an alternate approaches to create high diversity complex libraries. That said there were concerns that the comparison to alternate PCR-based approaches may not fairly represent how well those approaches can work when carefully implemented. Although there were some differences on this point, it seems that the most conservative and time efficient way to respond to these concerns would be to generally emphasize the capabilities of the present strategy and avoid relative comparisons unless they are directly substantiated by side-by-side comparisons. Additionally, since this is primarily a methods paper, it was felt that a better description of the workflow, including time and reagent requirements would be important to address in revision. For example, in the text or as a table/figure, the workflow Figure 1A could be fleshed out to provide more specifics about time and yields.

Area#1 (relative comparisons):We thank the reviewers for pointing out that we have made relative comparisons. In the revised version of the manuscript, we avoid comparable statements where not appropriate. As a result, the text has been reworded and Supplementary Figure 3C showing NGS comparisons of previously reported reagents with our 3Cs-DUB library has been removed.

Area#2 (visualization of workflow):The reviewers pointed out that a better visualization of the workflow that includes times, yields and reagent requirements is necessary. As this is primarily a methods paper, we are thankful for this critical comment and provide a new Figure 1A in which the molecular biology of 3Cs reactions is put into context of phage, ssDNA and final library generation. We highlight possible break points in the protocol, at which users can pause or reagents be long-term stored. Furthermore, to better illustrate the general time frame, we provide time estimates for total and hands-on time and, when appropriate, provide reagent yields. In addition, we now provide a comprehensive list of all reagents and equipment required to perform 3Cs in the Materials and methods section of the revised manuscript, as well as in the key_resource_table.xlsx file.

2) There was concern that, while the underlying quality of the DUB screen may be high, that the analysis strategy is not well validated. The raw sequencing data output of the screen should be analyzed by one or more of the established hit-calling methods (e.g. MAGeCK) to provide a better sense of the robustness of the hits as well as the real world performance of this library.

Area#3 (MAGeCK analysis of DUB data):To provide a better sense of the robustness of the hits as well as the real-world performance of the DUB library, the reviewers pointed out to use the well-established MAGeCK algorithm. We are thankful for raising this critical point and followed the reviewer’s suggestion. As such, we have extensively adapted text and Figure 3 to reflect log2-fold changes and their associated p-values for individual proliferative DUB phenotypes. Even though not asked for, we provide shRNA-mediated validation of positive and negative proliferative DUB phenotypes as new experimental support for the performance of the gRNA library. Furthermore, one reviewer pointed out that our initial gene-ontology (GO) analysis does not add much to the conclusions drawn from this section. In light of the overall manuscript, we agree with the reviewer and have removed the GO analysis part from the text and Figure 3.

3) There is considerable concern about the conclusions from the TGW screens. While there is an appreciation for the innovative nature of the approach, the quality of the results, both in terms of the completeness and false positive rates, is difficult to evaluate given the data presented. Short of what would likely be a major experimental and analytical effort, the authors should tone down the claims and present this as an exploratory effort. For example, limitations such as very low reproducibility and the need to allow multiple mismatches to map sgRNAs should be discussed alongside the need for extensive validation.

Area#4 (deemphasizing TGW screens):In order to put conclusions drawn from our TGW screens into a better perspective, the reviewers asked to tone down general conclusions drawn from this section and emphasize limitations as very low reproducibility, the need to allow mismatches in order to identify target sequences, and the need for extensive validations. We thank the reviewers for stressing this topic and have substantially changed the Results and Discussion section to better reflect the limitations associated with the TGW screens. Furthermore, we now highlight the fact that the TGW screen has been an exploratory effort, provide a more careful examination on the shortcomings of library and screen and make clear that doxorubicin resistance-associated target regions will need extensive future validations.

To better reflect the overall criticism and enable an unbiased evaluation of the 3Cs technology in the future, we also provide a shortened manuscript title “Circular synthesized CRISPR/Cas gRNAs for functional interrogations in the coding and noncoding genome” in which we avoid “high-fidelity”.
