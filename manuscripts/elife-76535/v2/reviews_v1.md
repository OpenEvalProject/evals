# Peer review - Round 1

Editors:
- Sandeep Krishna, https://ror.org/03ht1xw27 National Centre for Biological Sciences­‐Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76535.sa0](https://doi.org/10.7554/eLife.76535.sa0)

This important article identifies topological metrics in gene regulatory networks that potentially predict the kinds of phenotypic steady states that the network allows. In particular, for epithelial–mesenchymal plasticity, the authors show compellingly that the relevant gene regulatory networks are structured as ‘teams’ that may be ‘strong,’ yielding stable phenotypes, or ‘weak,’ yielding unstable phenotypes prone to plasticity. The work would be of interest to researchers interested in systems biology and the nonlinear dynamics of biological systems, as well as biologists interested in gene regulatory networks and their (mis)functioning in cancer cells.


---

# Peer review - Round 1

Editors:
- Sandeep Krishna, https://ror.org/03ht1xw27 National Centre for Biological Sciences­‐Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76535.sa1](https://doi.org/10.7554/eLife.76535.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Landscape of epithelial mesenchymal plasticity as an emergent property of coordinated teams in regulatory networks" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Jean Clairambault (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Both reviewers found the results interesting and deserving of publication, but have also raised some concerns that require revisions in the manuscript. Most importantly:

1. The paper becomes very technical and will not be accessible to as general a readership as it deserves. To address this the reviewers have made some suggestions, such as defining terms and parameters more carefully and providing a better explanation of team identification in a general gene regulatory network. Please see the suggestions of Reviewer 2 in this regard. The authors should also consider moving some of the more technical discussion to supplementary material, and where they choose to keep the technical part in the main text they should try to explain more pedagogically the meaning of the equations and the connection to the biology.

2. It is not clear how generalizable the results are to other gene regulatory networks. Therefore, the authors should extend their studies to other networks, not just those relevant for epithelial-mesenchymal plasticity. For instance, they could examine small cell lung cancer and melanoma networks. In addition, the authors should try to comment, even if speculatively, on the implications of their results for the interplay between cooperation and competition in cellular populations both in unstructured colonies as well as multicellular organisms (please see the comments of Reviewer 1).

Reviewer #1 (Recommendations for the authors):

The authors here – and this is absolutely normal – focus on their main usual topic, EMP, which has been reported to be physiologically present in development and wound healing (going as far as limb regeneration in axolotl), but is most often studied in cancer. Could the authors sketch possible studies in other fields in which tissue indetermination and plasticity have been reported, e.g., cases of de-differentiation or transdifferentiation in cancer?

Other (teleologically conceptual) words for coordination are compatibility and cooperativity, two features that are inherent to cohesive multicellularity, yielding effective division of labour in a healthy organism. In this respect and in their present study, the authors have shown that organisation of GRNs in 'strong' teams contributes to the stability of terminal phenotypes. This may account for the separation of phenotypes in different tissues. However, the nature of compatibility within GRNs in cells of a given tissue seems to be absent from their analyses. Similarly, the intensity of links between teams of GRNs in different tissues, producing cooperation, would be another step forward to study the cohesion of a multicellular organism, which must reject plasticity in general, and MEP in particular. Could the authors suggest extensions of their well-designed methodology to study such aspects of cohesion in multicellular organisms?

Other teams of researchers have studied differentiation from the point of view of the emergence of multicellularity, which is a fundamental question in developmental biology, with solutions that may be recapitulated by cancer cell populations showing EMP. In particular, Kunihiko Kaneko's lab in Tokyo (https://doi.org/10.7551/mitpress/10525.003 of 2016) has developed a conceptual representation of the stability of phenotypes related to stationarity of expression of genes in collections, and instability related to oscillatory solutions, that might be made close to the present manuscript. Of course, their interest is more devoted to induced pluripotent stem cells (iPSCs) and the Yamanaka genes Sox2, Klf4, Oct4, and c-Myc (see arXiv:2109.04739v2 of 2021); however, the idea of 'strong' and 'weak' teams of GRNs might also be investigated from this point of view. Could the authors comment on this suggestion?

Reviewer #2 (Recommendations for the authors):

This paper has great theoretical potential in the context of Systems Biology. However, it becomes too technical too quickly, and some mathematical concepts are not properly defined. This might "scare" some readers away and makes it difficult to identify the most important take-home messages in each section. I hope that with the more detailed comments below, I can help the authors improve the quality of their manuscript so that it will get the full deserved attention from any reader willing to learn more about Systems Biology. The authors could consider also shortening the paper.

– In the abstract, the authors talk about SCLC without previous definition. In the first sentence, they use the concept of coordinated "teams" of nodes, but nodes per se are never defined.

– What is the biological difference between the 5 networks used to describe epithelial-mesenchymal plasticity?

– It might be that the legend of the color bar in the adjacent matrix in Figure 1B (left) is wrong, and the authors are displaying the "adjacency" value. From the plot, I understand that this parameter can take only the values +1,-1 and 0. However, I did not find it defined anywhere in the main text. In addition, it would be helpful to indicate what is the difference between the nodes annotated in the y tick (input node of an edge?) and the x tick (output node of an edge?).

– When the authors introduce the equation for the "influence" in Figure 1B (left), most parameters are left undefined (by the end of reading the manuscript I found some description in section 4, however, I did not manage to understand the calculation). Is not Adj_{max}^{l} always equal to 1? How is Adj^{l} (or J^l according to Equation (5)) calculated? Are all the possible paths connecting two nodes considered in the Equation? It would make sense to refer to section 4 when the equation for "influence" appears for the first time and spend more text making all the proper definitions.

– Why do VIM, TCF3 and KLF8 not cluster with FOXC2 etc, and why does CDH1 not cluster with miR101 et al. according to the Influence profile in Figure 1B (right) (or according to correlation in Figure 1D,1E)? Do I read it correctly when I say that CDH1 is not influencing any other node in the network? Is its value then important to define phenotypes? Can we accordingly remove this node from the network without any consequence of the phenotype frequency? Can this be used as an approach to simplify network topology?

– How is the number of node groups identified in the different WT and randomized networks? Is it always equal to 3 (input/output, and 2 types of core nodes)? I imagine this to be a crucial aspect of the calculation of the group strength (Figure 1B, right). In addition, what is the parameter n_{II} in Figure 1B, bottom-right?

– I think that in the last paragraph of section 2.1, the authors need to cite together Figure 1D and 1E, and where they cite Figure 1E they refer to Figure 1F.

– In section 2.2, the authors state that the presence of two strong distinct teams can contribute to bimodal distributions in SSF plots. Based on the observations obtained from Chauhan et al., 2021, there two strong teams give rise to four strong stable phenotypes. Therefore, I wonder how generalizable the statement is. Can the authors comment on this?

– In the 3rd paragraph of section 2.2, the authors refer to the Methods section while describing the concept of frustration. However, I could not find any explanation of frustration in the Methods.

– I do not understand how much the analysis of frustration values is adding to the steady-state frequency. Intuitively, these two concepts are intimately related: less stable steady-state has higher frustration. The authors could consider removing one of the two to simplify the paper. From my point of view, SSF is a better measurement, since the authors can see that low frustration values can have practically any SSF while high frustration values only have low SSF (Figure 2D, 2F). Therefore, it seems to me that SSF provides more information.

– In Figure 2B, the authors again provide some equations that lack definitions. What are W_{ij} and si? What do "ON" and "OFF" mean?

– In Figure 2B, I would use SSF consistently when indicating steady-state frequency values. Is Frequency in panel D the same steady-state frequency as in panel A?

– How do the other networks look like when plotting "Frustration" versus "SFF" (Figure 2F)?

– In Figure 3A, it would be helpful to explain what read and blue means, and what would be the value of coherence in this particular sketch.

– I find it surprising that some steady states have a very high coherence and a very low frequency (Figure 3E). Can the authors comment on that?

– Figure 4Aii (S5B) is very important: it shows for the first time that the mean group strength value might indeed be related to the bimodality of steady-state types. However, as it is right now, the distribution of frustration+coherence values for the high mean group strength networks is not seen. I suggest the authors show the distributions of frustration, coherence, and frustration+coherence values for high and low mean group strength networks in different panels, and then they explain how are they obtaining the composite (maybe this magnitude should be introduced before and merge Figure 2 and 3 into one). I find the histograms of frustration+coherence for 57N113E, 20N40E and 26N100E provided in Figure S5B doubtful.

– The equation of strength of a state, in Figure 4B, should be better explained. What is si?

– Are the capital S in Equation (8-10) the same as the small s in Equation 7?

– Network 57N113E is persistently giving less clear results. Can the authors identify whether the way the network was constructed has some defect? In other words, could their theoretical approach help validate experimentally determined gene regulatory networks?
