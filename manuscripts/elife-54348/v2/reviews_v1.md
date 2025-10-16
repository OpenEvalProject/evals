# Peer review - Round 1

Editors:
- Raymond E Goldstein, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54348.sa1](https://doi.org/10.7554/eLife.54348.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The evolution of germ-soma differentiation is one of the most fundamental questions in evolutionary biology, and the present paper investigates the consequences of altering one of the most basic assumptions: the traditional (symmetric) division of labor that has been studied from biology to economics. The authors consider a diversity of network structures and fitness functions and they find that sparser networks lead to higher levels of specialization.

Decision letter after peer review:

Thank you for submitting your article "Topological constraints in early multicellularity favor reproductive division of labor" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Diethard Tautz as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Pierrick Bourrat (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This is a very interesting paper on the evolution of germ-soma differentiation in which the authors consider the topology of interactions between the cells that make up the whole. They find that classical considerations about the convexity or concavity of certain functions characterizing the advantages of specialization no longer hold when the network topology is nontrivial. And such topologies are indeed found in nature. The reviewers were generally very supportive of the work but raised a number of points that need to be addressed in a revised manuscript.

Essential revisions:

1) The authors use a notion of fitness in which clonal cells can have different fitnesses, or more accurately, clonal groups can have different fitness. We know that there are some precedents in the literature, but this notion of fitness does not correspond to the notion of fitness one can associate with natural selection. To illustrate why, consider the following plant example. Take a single genet with two ramets in two environmental patches, one rich and one poor. Each ramet might adopt a very different developmental strategy from the other, considering the ecological constraints it is subjected to. These two strategies would nevertheless not be heritable in the sense that two offspring ramets put in the same environmental patch would develop the same developmental strategies (excluding noise). Thus, the differential success of each ramet is not an evolutionary success that can be associated with natural selection. This is a case analogous to the one presented by the authors. The notion of fitness they refer to seems to be rather the notion of realized fitness. This has no implications for the author's results per se but instead leads to an interpretation in which natural selection is not at work for explaining the division of labor in situations of concavity.

2) Related to the previous point, there seems to be a tension between, on the one hand, the claim that a concave function can lead to an increase in reproductive specialization, and on the other hand, claims that it has something to do with fitness. Fitness is about expected values, and in a situation of concave function, two or more cells specializing would yield a lower collective fitness than when not specializing. From a purely analytical point of view (i.e., Fisher's fundamental theorem), this seems impossible. So my question to the authors is whether there is not hidden somewhere a convex function, which is the relevant one for the evolutionary dynamics observed. Otherwise, what is the ecological explanation of such a result? There must be some ecological constraints that give rise to this phenomenon, and it would be good to know what the authors think they are.

3) There are well-known cases presented in the population genetics literature in which Fisher's fundamental theorem seems violated, but this is because of the environment (including the social environment) changes over time, such as frequency-dependent effects on an individual's success. We wonder if the results of the authors could not related to this literature in some way.

4) The model description is a bit abstract and occasionally hard to follow. It would be great to have fecundity and viability defined, and even better to have some real biological example of what returns on viability might mean and how they might be shared (I don't find the filamentous fungi example informative, at least not in the way it is written). That would also help the reader understand why there are returns on viability but not on fecundity. That the vi vector is the "group investment strategy" also comes as a surprise and takes a bit for the reader to put it all together. Similarly, the existence of both a general adjancecy matrix and of a special case one that uses the β, is somewhat confusing the way it's described. If the authors anyway only work with the special case of equal sharing with the non-self neighbors then why not define the 1-β+β/ni quantities as cij when they appear in the text, and then write a fourth eqn for W in [1] that explicitly uses the β. That would certainly help the reader a lot.

5) Results subsection “Fixed resource sharing” first paragraph, we may be getting confused, but how can you vary β in the case when, as is now written, individual i "shares equally among interaction and self terms"? Doesn't this mean that β = 1?

6) “We conjecture that the troughs in Figure 3C, where specialization occurs for the lowest values of, occur when connectivity is just large enough so that a spanning tree is more likely to connect all individuals in the group than not”, we don't fully understand that conjecture: do the authors simply mean that the troughs occur when the random graph becomes connected with probability > 50%? (A spanning tree connects all individuals by definition.)

7) The authors suggest sparsity is the main determinant of whether a network supports reproductive specialization. But, their examples in 1B and 1C (where a ring is sparser than the bipartite network) to us suggest that it is not so much about "sparsity" as it is about "bipartiteness" – or how easy it is to subdivide the nodes into two classes such that most edges go between these two classes (that's what you'd want for specialization anyway, we guess), and that sparse graphs simply have a tendency to be close to bipartite. We suspect that a ring graph with an odd number of vertices will be less conducive to specialization (although you could still alternate germ/soma cells except at one point), and that a star graph where there is one node of degree n-1 and all the others have degree 1 may be an example of a sparse graph where evolving specialization is not so easy (because for this graph it's not clear how to divide the vertices into germ and soma).

8) Related to the previous point: we would be interested if the authors have considered what happens when the optimal strategy is not 1:1 but, say, 1:2. Does that make specialization more difficult? Here we think that, with a few additional simulations, the authors could add a lot to the paper in terms of the ability to connect properties of the graph (beyond comparing some explicit topologies and random graphs of varying sparsity) to its ability to support the evolution of reproductive specialization.

9) Finally, it would be nice to see how the different specialists are distributed on these networks (at least when the specialization is equal to 1). One can infer it, but we think it would visually help the reader to get the gist of how the model works very quickly.
