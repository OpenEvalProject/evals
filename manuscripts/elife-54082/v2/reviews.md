# Peer review - Round 1

Editors:
- Michael B Eisen, University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54082.sa1](https://doi.org/10.7554/eLife.54082.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper is amongst the first to show how computational network analyses based on protein-protein interactions can be successfully used to augment genetic screens to identify genes involved in essential developmental processes.

Decision letter after peer review:

Thank you for submitting your article "Topology-driven protein-protein interaction network analysis detects genetic modules regulating reproductive capacity" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Michael Eisen as the Senior and Reviewing Editor The following individuals involved in review of your submission have agreed to reveal their identity: Felipe Aguilera (Reviewer #2); Luke Lambourne (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to proceed without manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

This work aims to predict protein-protein interaction in a developmental context with a combination of approaches drawn from developmental genetics and system biology. This work represents an elegant study that combines computational biology and molecular developmental biology to explain how organ systems are formed.

Although it is our usual practice to combine the reviews into a single consensus, in this case I think the independent reviews offer distinct takes on the manuscript and suggestions for revisions and stand better on their own, although to expedite your revisions, I will summarize the main issues to address here:

Analysis:

Several issues were raised by reviewer 3 and during discussion:

1) Additional analysis is needed to support claim of non-random modules

In particular, the results of Figure 4 show that the positive pairs in the screen on average, tend to have higher degree in the network, which could be responsible for the higher connectivity of the seed genes, rather than them forming modules. This should be addressed with some form of control analysis.

2) Module separation

As a general rule, it is not surprising that the connectivity is higher within the output of the SCA algorithm, which returns a subnetwork of connected nodes, to the connectivity between two different SCA produced sub-networks. This is expected to happen with random lists of seed genes, and does not prove that functionally separate sub-networks have been identified. The claim is confusing given that there are shared subnetworks (V, VI, VII) which seems to contradict the idea of separate modules. Reviewer 3 offers several suggestions for how to make this analysis more convincing.

Writing and presentation:

1) In addition to suggestions about presentation in the reviews below, during discussion all three reviewers highlighted the value of the overall approach and felt that the manuscript merits publication in eLife. However there is a sense that the manuscripts lacks a clear take home message. This is not required for publication per se, but we all feel the manuscript could be made stronger in revisions by attempting to distill a take home message for readers.

2) The experimental validation results are not presented clearly. That section could benefit from more clarity in what specific aspects of the predictions are being tested and how the specific tests address them.

Reviewer #1:

In this study, the authors investigate the signaling pathways that regulate Drosophila ovary development and the rate of egg production. An earlier study from this lab identified a role for hippo signaling in these processes. Here, they performed an RNAi-based screen through 463 candidate genes involved in signal transduction to identify genetic modifiers of the hippo[RNAi] phenotype as well as genes that regulate the rate of egg laying through a potentially hippo-independent mechanism. The screens were well-designed and produced quantitative data that the authors could use to rank-order genes according to the strength and direction of the phenotype. Their strategy for assessing the rate of egg laying is in line with standard approaches in the field and their method of counting ovariole number is entirely appropriate. These screens identified a long list of genes, and they took a systems biology approach to assess the individual and combinatorial contributions of these genes to ovary development and function. These types of analyses are outside my area of expertise so I could not assess whether the appropriate computational methods were chosen and applied correctly. However, the writing of this section was clear to a non-expert and, taking their claims at face value, the data seem to support their interpretations.

In the final section of the manuscript they describe how their network analysis identified additional genes not uncovered by their screens and show that RNAi knockdown of these additional genes do, indeed, cause phenotypes in egg laying rates and ovariole number. This is a nice validation of the approach. As a minor point, the data presented in Figure 7 only summarize how many genes in the list showed a phenotype in each category but did not indicate what the genes are, which ones are associated with which phenotype, or what the z-scores were in each case (I could not find this information in the supplemental material either, though perhaps I missed it). If it has not been included already, the authors should provide this for completeness and to allow comparison to the other data in the study.

Overall, I think this study will be a useful though perhaps somewhat limited contribution to the field. The results of the screens provide a large amount of data for the field to build on and I appreciate their holistic approach to describing the interplay between genes and pathways in the regulation of processes as complex as development and oogenesis. At the same time, I struggled a bit to extract the most important take-away messages that change how I think about these processes. For example, they state in the Discussion that the core module consists of housekeeping genes and hedgehog pathway genes, but this could have largely been predicted from previous publications on this topic. Likewise, terminal filament formation is known to involve cell migration and, consistent with this, they find that several genes involved in cytoskeletal dynamics are important for proper specification of ovariole number. Though some of these genes have not been studied in this context, their involvement here is not too surprising. Nonetheless, it may be that the main innovation of this study is in the systems biology approach they have used to analyze the data, so I look forward to the online discussion with the other reviewers who have more expertise in this area.

Reviewer #2:

A general assessment of the work

This manuscript aims to predict protein-protein interaction in a developmental context. By using tissue-specific RNAi screening and systems biology approaches, the authors found known and unknown genes involved in ovarian development and function. A plethora of unknown genes was functionally tested, giving support to the topology-driven network analysis conducted, and the developmental regulatory modules found. This work represents an elegant study that combines computational biology and molecular developmental biology to explain how organ systems are formed.

Numbered summary of any substantive concerns

This article is generally well-structured, the data analysis is performed in a proper fashion, and the results are nicely presented, giving support to the major conclusions. I have no major concerns with regard to this manuscript, only some minor edits.

1) I am wondering if authors can give more detail regarding the paragraph starting "To choose candidates.…" I might be wrong, but have the feeling that this approach might produce bias in the results obtained by the authors.

2) In Figure 4—figure supplement 2, the authors show a comparison of Zgene scores of positive candidate genes sorted by centrality metrics. However, I wonder why the authors did not calculate p-values (significance level) between 1st and 5th quantile comparisons of Zgene scores shown in this figure? Significance levels in these comparisons might give strong support to the weak prediction of a gene that would affect a specific phenotype.

3) In Figure 6, for the sake of clarity, it is necessary to show the sloppy paired 1 gene in the meta-network analysis (Figure 6A). As is now shown in this figure, readers cannot see easily the importance of this gene within sub-network VII, which I think is one point that the authors want to highlight.

4) In step 3 in the protein-protein interaction network (PPI) building section (“Method Details” subsection), authors indicate that a custom python script was created to download and reads each of the PPI tables from DroID database, but I could not find this python script in the Github repository in the paper. Please, can authors upload this script in the repository?

Reviewer #3:

The authors present a novel study integrating the results of performing screens for regulators of reproduction in Drosophila with protein-protein interaction networks. Highly interesting, interdisciplinary work lying at the intersection of developmental and network biology. They identify genes regulating ovariole number and egg laying and analyze those genes in the context of PPI networks, predicting and experimentally testing additional novel reproductive regulatory genes with some success. However there are serious issues with the analysis supporting key claims in the manuscript related to network topology.

1) The claim of non-random modules is not supported by the analysis.

– The claim in the section title "Genes regulating egg laying and ovariole number regulation form non-random interaction modules" (L260-L261) is supported by Figure 5—figure supplement 4. In that figure both the seed genes and results from the SCA algorithm are compared to the subnetworks formed by randomly selected genes from the initial screen. This is a sensible comparison for the seed genes but not for the output of the SCA algorithm, since that algorithm builds a LCC (see Figure 5A) and so will obviously have a much larger LCC and be much more connected than randomly selected genes from the network.

– The results of Figure 4 show that the positive pairs in the screen on average, tend to have higher degree in the network, which could be responsible for the higher connectivity of the seed genes, rather than them forming modules. To account for this, the seed genes could be compared to a null distribution of degree-controlled randomized networks.

– The text reads "decreased average shorted path" (L331) but it is increased in 7 of 8 cases in the figure.

2) The claim of separate modules is not supported by the analysis.

– Similarly to point 1, it is not surprising that the connectivity is higher within the output of the SCA algorithm, which returns a subnetwork of connected nodes, to the connectivity between two different SCA produced sub-networks, that will happen with random lists of seed genes, it does not prove that functionally separate sub-networks have been identified.

– There are sizable shared subnetworks (V, VI, VII) which seems to contradict the idea of separate modules.

– The heat-map Figure 6B, shows very low edge density within the groups (diagonal squares), in contradiction to what is written in the text. This appears to be due to a miscalculation in the file 08_MetaModule_Analysis.ipynb in the Github repository: within the group the number of edges should be divided by (x2 – x) / 2 where x is the number of nodes in the group (assuming self-interactions are not considered), the edge density calculations between the different groups are correct.

– An alternative approach to this analysis could be to look at the connectivity of only the seed genes and not the connector genes in the different groups and comparing to a random assignment of group.

– Identifying modules of genes which affect one phenotype and not another is presumably made more difficult by the decision to filter candidate genes for two of the phenotypic screens based on the results of the first screen.

– The prediction results do not appear to be consistent with separate modules (see point 3 below).

3) The results of experimentally testing the predictions are presented in an unclear way, making it difficult for the reader to assess their accuracy.

The results in Figure 7A/B/C appear to show that the predictions from the modules are just as good for the phenotypes not associated with the module as for those associated with the module, e.g. for the EL phenotype there is one correct prediction from both the Core and EL modules and 9 correct predictions from the hpo[RNAi] ON/EL modules, with a similar number of predictions. So it would seem that these results suggest that, although there is positive predictive value overall relative to the initial signaling genes list, that the separate modules predicting their associated phenotype separately from the others is not supported by the data. This is not discussed in the text.

– From what I could understand, the fractions for the initial signaling gene lists for the EL and hpo[RNAi] ON phenotypes are not exactly consistent with the compared fractions of the predictions, due to the filtering applied on the hpo[RNAi] of |Z| > 1, for the initial screens. Perhaps the fractions for the 2 affected bars in Figure 7C could also be calculated with this threshold applied to remove genes?

– There are no p-values calculated, comparing the predictions to the original screens and no error bars shown in Figure 7.

– The title of Figure 7C could be changed to make it clearer that this contains predictions from all modules.

– There is no “All screens” column in either Figure 7C or Figure 7D for comparison.
