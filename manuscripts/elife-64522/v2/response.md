# Author response - Round 1

Authors:
- Lakshya Chauhan ([ORCID: 0000-0002-5851-507X](https://orcid.org/0000-0002-5851-507X))
- Uday Ram
- Kishore Hari
- Mohit Kumar Jolly ([ORCID: 0000-0002-6631-2109](https://orcid.org/0000-0002-6631-2109))

## Response text

DOI: [10.7554/eLife.64522.sa2](https://doi.org/10.7554/eLife.64522.sa2)

Reviewer #2:

In my opinion, the most significant area where this manuscript needs to be strengthened is in providing critical comparisons with prior literature and results (primarily Wooten at al and Udyavar et al). Discussions on what advances have been made in this paper with respect to what was already known earlier, need to be highlighted. I found it quite hard to judge this manuscript and place it in context, since a lot of the methods and datasets used here are very similar to the previous works. Detailed suggestions along these lines as well as some possible new analyses are provided below:

1) It would be good to know why the authors chose an Ising Model – based Boolean simulation strategy as compared to the Boolean model used in Wooten at al. Is there some difference in the statistics expected from these two different formalisms? Is there some limitation of the previous work that the authors wanted to address here? Given that Wooten et al. showed that the 4 SCLC states can be recapitulated, is it surprising that the authors get the same 4 states using their Boolean method on an identical network?

We thank the reviewer for this important question. Udyavar et al., 2017 – the precursor manuscript to Wooten et al., 2019 – had also used the Ising model-based Boolean simulation strategy. Thus, as far as Figure 1B is concerned, these are for the same circuit (Figure 1A) and modeling strategy as in Udyavar et al.

Wooten et al. have used a different network than what was used in Udyavar et al. and also a different modeling strategy (BooleaBayes) which depends on inferring logical relationships between nodes in gene regulatory networks using gene expression data and using a “Bayes-like adjustment approach”. Therefore, the network Wooten et al. arrived at using BooleaBayes (Figure 7A) is different from the one we and Udyavar et al. have used. Hence, obtaining 4 states in this network may not necessarily be surprising as far as SCLC phenotypes are concerned. However, obtaining only four states from such a complex network (33 nodes, 357 edges) was very intriguing to us, which drove further our investigations in network topology-based analysis.

The key message in our manuscript is not that this network has only four states, but the reasons for why only four states are seen in this complex and large network (33 nodes, 357 edges). We have deciphered a “latent” design principle in SCLC network, and have offered a conceptual framework to decode similar design principles hidden in other regulatory networks.

Moreover, in addition to running Ising model based simulations for the network, we have used a parameter-agnostic approach – RACIPE – and notice at least a semi-quantitative agreement in terms of dominance of the four states identified via Ising model. This agreement strengthens our key point that network topology alone can contain enough information about its dynamics. We have now added a paragraph in the Discussion section highlighting these salient points.

2) For the ODE method, the frequency of the four states add up to only about 22%. It would be interesting to see a full list of the top ten states with their frequencies, and a discussion on why these other states appear in the ODE but not in the Boolean formalism and its biological implications.

We thank the reviewer for this subtle observation and raising this important question. We have now performed a detailed analysis of top 20 states obtained by RACIPE whose frequencies add up to 54%, and observed that these 20 states are very similar to the top 4 states obtained by Boolean (X1-X4 in Figure 1B), with a difference noted in only one or two nodes (i.e. node value = 0 in Boolean state and 1 in RACIPE state or vice versa).

It is not surprising to see that the RACIPE output has a much larger number of states than Boolean output, given its continuous nature, an observation we made in our previous manuscript as well (Hari et al., 2020) and is now included in a new paragraph in the Discussion.

Conceptually speaking, given that the sizes of the two “groups” identified are 22 and 10 nodes, a difference in values of one or two nodes are not very likely to give rise to a completely different biological phenotype. Thus, these “close-enough” states can be thought of as “micro-states” that overall constitute a biological “macro-state” or phenotype.

3) Following up on point (2) above, was there a reason for using two separate axes for the same quantity (frequency) in Figure 1D i ? I found this quite confusing, because for example, at first sight it seems like the S2 steady state has similar frequencies in RACIPE vs Boolean. But the frequencies are in reality very different, right? I would therefore suggest to plot both RACIPE and Boolean results using just one axis, to avoid confusion.

Thanks to the additional analysis performed (mentioned in response to point (2)); we have now replaced Figure 1D i to address this point.

4) The observation of two "modules" using pair-wise correlations is interesting. However, it was unclear to me why Wooten et al. find 17-18 modules, though their WGCNA method also uses a pair-wise gene correlation technique. A detailed discussion on this would be very helpful for readers in my opinion.

The WGCNA method gives us correlation data from all the genes whose expression values are used as an input to the algorithm. It is a statistical method that works on threshold based correlation, and does not use any mechanistic information embedded in a network topology. Because network topology information is not required, Wooten et al. were able to start with a much larger set of genes and obtain a large number of modules. Not surprisingly, we found that the 33 genes considered here were spread across different modules. This is not surprising or contradictory because any of these 33 genes can still be correlated strongly with any other gene not in the network simulated here, and those genes may belong to different modules. It should be noted that two genes can show a good correlation in their gene expression values without any of them directly or indirectly affecting each other, say transcription factor activates gene B but inhibits gene C, thus, B and C are most likely to be negatively correlated. In brief, our analysis is based on network topology, not transcriptomic data that is input to WCGNA. This point is now included in a new paragraph added in the Discussion section.

5) Related to the pair-wise correlation method, I was surprised to see that Neurod1 does not seem to be part of any module in Figure 2. In the Discussion, the authors mention that Ascl1 and Neurod1 don't fall in the same team, but it seems to me from Figure 2 that Neurod1 doesn't belong to any team! This seems to be contradictory to the rest of the results, unless I have misunderstood something here. A discussion on these lines seems warranted.

We apologize for a potential semantic confusion caused. The two statements – “NEUROD1 does not belong in the same team as ASCL1” and “NEUROD1 does not belong to either of the two teams” – are not contradictory to one another. We have performed further analysis based on CCLE and GSE73160 gene expression values and see that NEUROD1 levels do not align with the patterns seen in the expression values of members of two groups (Figure 4—figure supplement 2).

6) Given that the dynamical simulations were carried out with 33 genes, why did the authors choose to perform all the clustering analyses with only a handful of genes? This may be problematic, for example, if sets of 2 or 4 randomly chosen genes are used for clustering the expression datasets, how likely are we to find a few well separated clusters? If we find that random gene subsets also separate into clusters, how biologically meaningful is it to see clusters with Ascl1 and Neurod1?

Our reason to include ASCL1 and NEUROD1 based clustering was purely based on available experimental literature suggesting these two nodes as key markers and/or inducers of phenotypic heterogeneity in SCLC. In the latter half of our analysis (Figure 5), we have used YAP1 and POU2F3 in addition to ASCL1 and NEUROD1 to classify CCLE SCLC cell lines, but we do not have either of them as a part of the network in the first place. Again, their choice was made based on available literature in SCLC heterogeneity as mentioned by Wooten et al.

Reviewer #3:

[…]

The authors state that "These results suggest that influence matrix is a better representation of network topology as compared to the interaction matrix.". However, since the influence matrix comes from the interaction matrix, it seems like it necessarily contains less information. The authors make this claim based on the fact that a network reduction based on influence matrix more closely represents the steady state distributions than a similar reduction based on interaction matrix. But it is not clear how much this conclusion is specific to this particular network, or reduction strategy.

We are grateful to the reviewer for encouraging remarks and we share the excitement about agreement in Boolean and RACIPE results, as well as a broader application of influence matrix. We have already seen preliminary evidence showing the two “teams” regulating phenotypic heterogeneity in other cancer-related signaling networks (for instance, see Figure 2 in Jia et al., 2020 – https://www.oncotarget.com/article/27651/text/). Because these additional networks are not directly related to SCLC, we are not including those results in this manuscript, but influence matrix based analysis will be the focus of our upcoming manuscript(s).

The correspondence of the steady states with expression data appears quite promising! However, the fact that Neurod1 is the sole gene that distinguishes S1 from S4, or S2 from S3, makes me suspect other genes must also contribute to the difference? Are there other genes in the literature that the authors think could be included into new versions the network that could give a broader picture of the differences between S1 vs S4, or S2 vs S3? Given the other 31 nodes in the network, do their steady state values more closely match one or another cluster from Figure 4B?

We have included additional analysis (Figure 4—figure supplement 2) highlighting the expression of other nodes besides ASCL1 and NEUROD1. As expected, the two groups identified via influence matrix largely show similar trends, i.e. as compared to A-N- and A-N+ subgroups, members of group A (ASCL1 is one of them) have higher expression levels in A+N- and A+N+ samples while members of group B have lower expression levels in these two subgroups. This analysis suggests that while other genes could play a role in defining the subtypes, their contribution might not possess the distinguishing power of ASCL1 and NEUROD1.

When introducing the Font-Clos si(t+1) equation, I recommend to describe what happens if si=0, rather than just including that info in supplement.

We have now included the same.

Figure 1B should have a legend indicating dark=off, blank=on (even though it is in the caption)

We have included this legend in Figure 1B.

I do not see what test / method was used to find the +/- % confidence intervals in Figure 1B, nor what size interval they represent (e.g., 95%?)

We have now clarified it in the figure legend. The +/- % represent mean and standard deviation of the frequencies obtained across three independent Ising-model replicates.

The reference in-text to Figure 1C, i, regarding swapping random edges, seems to actually refer to both i and ii

We have now referred to both i and ii.

In the text, the connection between the larger number of steady states of "random" networks to the true network's topology lacks a relevant reference to Figure 1C, iii

We thank the reviewer for pointing this out and have now included a reference to Figure 1C, iii.

The text introducing the J metric should describe what the indices are, rather than requiring the reader to search the figure.

In the main text, we have now described what the indices and the corresponding matrix is.

The introduction of influence matrix was very hard to follow, the grammar is confusing, and "lmax" is not clearly described in the main text, even though it is used several times.

We apologize for the confusion caused, and thank the reviewer for pointing it out. We have now expanded on the introduction of influence matrix both in the Materials and methods section and in the main text.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Reviewer #2:

The authors have now satisfactorily responded to most of the comments/queries.

Their response to point (6) that I had raised is not entirely satisfactory however, since they do not seem to have addressed the randomization point that I had raised. If random sets of two (or more) genes are chosen for the clustering analysis, how often do we see well separated clusters? It seems to me an important point to analyze and understand, in order to put the ASCL1 and Neurod1 based clustering in perspective. I would strongly urge the authors to include this analysis, unless they feel this is not a sensible question to address, in which case it would be good to hear their arguments against this.

We thank the reviewer for this constructive comment, and have performed the randomization analysis as well now. We find that the ASCL1-NEUROD1 gene pair is among the top 1% of all possible gene pairs (33C2 = 528) in terms of defining four SCLC phenotypes experimentally reported (Figure 4—figure supplement 3). In other words, approximately 99% of all gene pairs considered here do not offer such well-segregated biologically relevant phenotypic distinction.
