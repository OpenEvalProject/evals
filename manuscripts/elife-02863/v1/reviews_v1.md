# Peer review - Round 1

Editors:
- Detlef Weigel, Max Planck Institute for Developmental Biology , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.02863.043](https://doi.org/10.7554/eLife.02863.043)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Buffered Qualitative Stability explains the robustness and evolvability of transcriptional networks” for consideration at eLife. Your article has been favorably evaluated by Detlef Weigel (Senior editor) and 3 reviewers.

The editor and the other reviewers discussed their comments before we reached this decision, and the Senior editor has assembled the following comments to help you prepare a revised submission.

Specifically, a major condition for ultimately accepting the work would be to demonstrate that the observation of GRNs in the current setup containing very few long paths does not simply follow from the observation in the Luscombe et al. reference, that most regulatory interactions in response to a change in “exogenous” conditions will be fast and the underlying paths thus very short. This is also critical with respect to the influence of time delays. In this context, one needs to know how the size of the GRN in this work compares with that in other studies.

Another critical aspect of the work is the comparison to randomized networks. The naive randomization used has been shown to yield networks that are fundamentally different from real networks. Why did you not use a degree-preserving model? The Alon lab has already reported on the apparent lack of cycles in the GRN of E. coli, but found it to be non-significant when using degree-preserving randomization (Shen-Orr et al., Nature Genet. 31:64, 2002).

Similarly, while three stability rules are mentioned, it seems that only one is tested, and another one, that the sign matrix should be invertible, is not considered. In addition, it should be shown why this one property is sufficient for robustness. Along these lines, stability is a necessary, but not sufficient requirement for robustness. This should be discussed as well.

In general, the reviewers found the work in places difficult to follow; it is recommended to show at least one large GRN in E. coli in some detail, and explain how exactly you determine that there are at most three links in any loop.

Some aspects of cellular physiology certainly require destabilizing motifs (e.g. oscillations, switches). Have you by any chance found physiologically significant destabilizing motifs?

Finally, please correct the figures about numbers of IFLs (any IFL of size k should also be an IFL of size k-1), or clarify the definition of an IFL.

Comments in full:

Reviewer #1:

The authors analyze GRNs for stability using rules from the theory of qualitative stability, particularly verifying that they do not contain directed cycles of length >= 3 and derivatives of this property. They conclude that GRNs under normal conditions are designed for stability.

The authors mention three stability rules, however they test only one (the third) and seem to omit a fourth one (the sign matrix should be invertible – see e.g. the May 1973 ref). The authors should justify the omission and better argue for not testing the other two. Their arguments about further (post-transcription) forces beyond regulation are not convincing as they would also imply that testing for the third rule (no cycles with >= 3 vertices) ignores such post-transcriptional effects (in fact Shen Orr et al justify the lack of cycles in this way exactly in their Nature Genet 31:64, 2002 paper). Not less important would be to prove why the network could be robust (under the qualitative stability theory) if only this one property is satisfied.

The observation that GRNs contain very few long paths underlies many of the results in this paper. Could this property follow from the observation in the Luscombe et al. ref. that most regulatory interactions are involved in “exogenous” conditions in which the transcriptional response should be fast and the underlying paths are very short?

A critical aspect of the manuscript is the comparison to randomized networks. The authors use a naive randomization (ER) which has been shown to yield networks that are fundamentally different from real networks. Instead I recommend the authors use the more-or-less standard degree-preserving model as e.g. used in the publications of the Alon lab. Notably (see also above) the Alon lab has already reported on the lack of cycles in the GRN of E. Coli, but found it to be non-significant when using the degree-preserving randomization (Shen-Orr et al., Nature Genet. 31:64, 2002).

Regarding the networks themselves – no details are given about their sizes – could it be that the larger the network the more it deviates from the stability criterion just by mere chance (and regardless of biological considerations)?

There is a rich literature on network motifs and the results of this paper should be contrasted to it, clarifying what are the new observations here and how they relate to previous ones. For example, the authors claim to find no cycles in the yeast GRN. However, the Luscombe et al. paper also studied this network and reports on a cell-cycle related cycle (Figure 3) where the TFs of each phase regulate the subsequent one. Another example is the Shen-Orr paper mentioned above.

There seems to be a problem with counting IFLs in random networks as an IFL of size k is also an IFL of size 2...k-1, hence the bars should decrease in height as happens for real networks (Figure 2).

The authors should backup their claim about constitutively expressed TFs with gene expression data showing that this is the case.

Reviewer #2:

First, let me say that I want eLife to publish this paper ultimately. It is one of the few papers that make a serious physics-based approach to a fundamental biological problem, the stability of biological networks, I think eLife, if it is supposed to represent a new approach to biology, needs these kinds of papers. You should accept it.

That said, I also do appreciate that it is essential that physics-based approaches to biology problems have to reach out to biologists. Although I am an experimental physicist doing biological problems, I found this paper a tough read and I think the authors could make more of an effort to make this accessible to both biologists and physicists.

In the course of teaching a grad level course on biological physicist I deliberately went off the beaten path to look at areas that are not normally covered by biological physics textbooks but are actually very important to biology. The subject of this paper, gene regulatory networks and their fundamental stability, is something I dipped into, before I had seen this MS. I don't think the present MS. really does justice to the already quite extensive literature out there, very physics based, on GRN and this needs to be addressed at the outset. The authors might claim too much credit for what they have discovered. I found that the review in Nature Genetics by Albert-László Barabási and Zoltán N. Oltvai “Network Biology: Understanding the cell’s functional Organization” to be an excellent introduction and to have it characterized as “predominantly descriptive, rather than predictive” to be rather harsh. Buffered Qualitative Stability (BQS) may be an interesting subject (since it is qualitative and not quantitative really I could lump it into the “predominantly descriptive” category as well). I think more credit has to be given to the ideas of scale-free networks, hierarchical architecture and hub connectivity.

Next, the results here somewhat appear by magic from some huge (I guess huge) computer code which I don't think the authors really explain. Figure 1 is really makes quite remarkable claims, saying that real biological networks have far-far fewer feed-back loops than a randomly generated graph. But when I look at the biological networks that I am familiar with, such as the SOS network in E. coli, an organism which is one of the test cases (Figure 1A), it is by no means obvious to me that there are just 3 at most links to that network: it is quite complicated. We looked at some other networks, and again we found many links to a loop. Large loops actually seem common to the naive eye.

So, it would be extraordinarily useful if the authors slowed down a bit and showed one large GRN in E. coli in some detail, and explain how exactly they determine that there are under 3 links to the loop! I am not sure that the SOS response qualifies as a GRN, but I am curious how this works out, and I think that giving a test example in some detail would help what seems to be a powerful idea which seems to be actually new works out in practice.

It would be great if BQS could be applied to cancer cells, as the authors’ claim. But they are frank to admit that the data isn't really there. But I don't think you need analysis of ALL the GRNs, I think that is hopeless. Certainly a critical stress-response like p53 must have a huge data set in various cells. Why not examine that and tell us if it actually is compromised for stability via BQS in cancer cells? And show us how the analysis is done, so we can try to repeat it?

In sum, a fascinating and potentially very important paper, but maybe a bit too boastful, and not very clear to the pedestrian, so that may really blunt it's impact.

Reviewer #3:

This is a very interesting manuscript which analyses the robustness and the evolvability of Genetic Regulatory Networks (GRN) in bacteria, yeast and human cells including a transformed one. The authors use the theory of qualitative stability analysis developed originally in economics. The theory summarized briefly in the Materials and Methods section of the manuscript provides necessary conditions for stability of a system of interacting components based on the sign of the elements in the 'community matrix'. Briefly, the system is stable against perturbations if it lacks positive, double-negative and long feedback loops. By comparative and statistical analysis of cellular and random networks, the authors show that GRN's seem to avoid the destabilizing network motifs. The only exception to this rule is the analysed transformed cell line. The paper is well written and I recommend it for publication but I would like to hear the comments of the authors for the following points:

1) The authors’ argument somehow implies that stability equals robustness. I think that stability is a necessary requirement for robustness but not sufficient. After perturbation the system might move to a completely different state even if it is stable. It would be useful to comment on this issue.

2) The theory of qualitative stability analysis is developed for autonomous systems. The cellular GRN has characteristic time-delays because of transcription and translation. It is true that in bacteria these two processes are overlapping but in eukaryotes the time-delay could be very significant. There is a short note about time-delay in the manuscript, but it would be useful to expand how it could influence these results.

3) Certain aspects of cellular physiology certainly require destabilizing motifs (e.g. oscillations, switches). I wonder whether the algorithm used by the authors has found any physiologically significant destabilizing motif
