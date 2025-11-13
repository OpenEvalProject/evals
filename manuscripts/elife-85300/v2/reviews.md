# Peer review - Round 1

Editors:
- Tatyana O Sharpee, https://ror.org/03xez1567 Salk Institute for Biological Studies La Jolla United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85300.sa0](https://doi.org/10.7554/eLife.85300.sa0)

This valuable study examines the principles according to which neurons connect to each other in vitro. The authors show solid evidence that data could be best explained by the homophillic wiring principle where neurons preferentially connect to neurons within overlapping groups.


---

# Peer review - Round 1

Editors:
- Tatyana O Sharpee, https://ror.org/03xez1567 Salk Institute for Biological Studies La Jolla United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85300.sa1](https://doi.org/10.7554/eLife.85300.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Homophilic wiring principles underpin neuronal network topology in vitro" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Panayiota Poirazi as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

Both Reviewers appreciate the scope and importance of the study in both experimental and modelling components. There was also a consensus among Reviewers that it is necessary to

1) clarify the separation between functional and structural connectivity;

2) provide the actual optimized model parameters in addition to the rough overview in plots like Figure 3C;

3) clarify differences between "more structured" vs. "more random" networks

4) make an effort to control for different amounts of data across datasets. For example, for a larger dataset, analyses could be carried out on a subset of the data to show how results might depend on the dataset size.

Reviewer #1 (Recommendations for the authors):

First a list of apparent inconsistencies and minor points of the presentation:

Figure 2b: Is reported to be from network recordings, but seems to have only ~28 nodes based on the histograms. That is lower than reported in S1.

Figure 2b: Why are values for betweenness > 100? Would not expect that, given the equation in the methods. Looks more like the total number of shortest paths is reported, rather than a fraction.

Figure 2d: The list puts models 3-7 as degree-based, and 8-12 as clustering-based; the boxplot has it inverse.

Figure 3f: Maybe more of a question: Why does DIV 7 correspond to 50% of "simulated time"? According to Supp Figure S2, DIV 14 has a median density of around 7% and DIV7 has < 1%. Is simulated time not the fraction of edges placed?

Figure 5: What exactly is "matching" that is depicted in the 6th row and column of the correlation matrices? It is explained in the methods as a measurement related to pairs of nodes, but I would expect a per-node-level measurement.

Figure 6: Aren't the P_ij values a bit high? The way I understand the generative algorithm after reading this manuscript and Akarca et al., 2021, is at each step a single edge is selected and placed according to P_ij. So the value should add up to 1.0. Even if more than one is selected at a time, with a median value around 0.2, we would reach an edge density of 0.2 in a single step, so that can't be it.

Figure 7: Caption for panels b and c swapped

Line 592: The case of "no principle being implemented" is listed as being indicated by high energy for all models. Yet, random null models in S5b all have very low energy. (As expected, just set both wiring parameters to 0.)

Line 1198: The explanation of global efficiency as depicted uses Euclidean distance (d_ij) and is independent of the graph structure.

Global efficiency is explained in the methods, but not the local efficiency that is used in Supp Figure S6.

Supp Figure S11b: I am not sure I understand the plot. the x-axis is labeled "log10", but the tick labels are also logarithmically spaced. Also, is the unit really in ms?

General notes:

Overall, a number of powerful and interesting methods and analyses are employed. But their selection seems a bit random. Between Figure S6 and S9 "participation" is swapped for "matching". The "topological fingerprint" is used to evaluate model match for sparse and dense cultures, but not for the GABA block case. In the GABA block case, the internals of the generative model is inspected, but not for dense vs sparse. And more. This makes the whole work seem disconnected.

I think Figure 5 belongs before Figure 4 as it provides further data supporting the idea that the "matching" algorithm builds networks comparable to the in vitro data. Branching off to the case of denser cultures is separate from that.

If I understood correctly that different wiring parameters (η and γ) are optimized for the same model but different cultures of the same type, then it should be attempted to explain the differences. (Not just for the GABA block case.) Do they depend on the size of the model? Age? Density? Average activity level?

I am curious why the main point of the paper is based on the sparse cultures and the dense cultures are much less prominently featured, although the sparse case has n=6 and the dense case n=12.

Overall, I am surprised by which data are shown in the main figures, and which ones are supplementary.

Reviewer #2 (Recommendations for the authors):

General:

I am a little confused about how the statistics of the different generative networks are computed. Sometimes it mentions "top performing simulated networks", sometimes "top 10" or "top 50", others "top n=1", and "top n=99 and average". I do not understand why several results are based on the "top n=1 performing simulated networks". These are probabilistic models for small networks, how is the best simulation representative of the underlying wiring principle? The original methodological paper (Betzel, Neuroimage 2016) appears to report the top 1% of energies (100 networks).

Similarly, it is often difficult to understand how significance was assessed across many figures and tables. For example for the anovas, and cohens effects on the energies. Sometimes energies are presented with 4 groups, others with 13. It is unclear if the same procedure was always followed.

Line-based:

159: It is very difficult to relate the reported plating densities with densities reported in other studies. It'd be much better to report real densities (in cells/ mm2) measured at the time of recording (or after staining). See for example the works by Potter, Segal, Moses, labs, and others.

171: After the whole-array activity scan, how were the 4x4 blocks selected? I assume one ends up with 64 independent 4x4 blocks, was the distance between them consistent? Was the ranking procedure from 1103 also used? Given that each 4x4 block can identify more than 1 cell, it is unclear why the number of tracked units in the sparse and dense cultures is so similar. Could it be that the electrode selection procedure was biased?

190: Regarding the jittering procedure, it is unclear whether it involved a random shift of either + or – 10 ms? or any value within that range (uniform distribution?)

310: Based on all the energy/exponent maps (e.g., Figure 2d right), the relevant range of exponents is always between -1 and 1 (or -3,3 at best). It is very difficult to read the value of the exponents based on the actual maps (e.g., Figure 3c). Maybe the authors could report the actual exponents somewhere (as they did in Sup Figure 14c for example). These values might help the interpretability of the results (for example, whether the exponents are positive or negative could be quite relevant).

357: What "large topological changes" do the authors refer to? Figure S2 only reports an overall increase in the number of connections. Also, is the network density measured as "total degree / (1/2*N*(N-1))" ? Or is there an extra factor of 2 somewhere? I'm trying to relate the values in S2a S2c, and supp Table 1.

374: Regarding "homophily performs best when approximating empirical networks, but not randomized networks", how did the authors measure that? The full random case in S5b has the lowest energy of all, and lower energy would mean a better fit if I'm not mistaken. Or were the authors only talking about the "randmio" procedure? If so, the authors might want to plot S5b in the same range as the figure it has to be compared with (0 to 0.6).

375: I don't understand how the staining panel relates to the rest of this figure.

376: F3C, to which of the 13 generative models does this plot correspond to? If I'm not mistaken, the exponents are calculated independently for each of the 13 models and 4 time points.

415: Unsure what the R2, r and p measures mean. Is this just pearson on F3e,f right panels, and its p-value?

442: Same as the comment on L159, the authors should report the density at the time of recording. It is also worth noting that there are many more processes affecting the final density than just apoptosis.

444: I'd like to point out a few important references on this matter. Ivenshitz and Segal, J Neurophysiol 2010. Cohen et al., Brain Research 2008. They looked in detail at how different densities affect activity and network connectivity in cultures.

455: Related to L171. I have difficulties understanding the relationship between plating densities, the number of recorded cells, the distance between cells, and inferred connectivity. From S3, the distribution of Euclidean distances for the two plated densities looks very similar. And the number of tracked units in S1 is also very similar. However, S7 reports functional connectivity with smaller edge lengths and higher clustering. This would be consistent if the higher plating density just resulted in more "cells/mm2" and the activity being invariant. But that doesn't seem the case. The authors should clarify that.

509: Why did the authors choose a dissimilarity measure based on the Euclidean norm? Distances between correlation matrices are non-euclidean (see for example Venkatesh et al., Neuroimage 2020).

625: If I understood this measure correctly, the STP is asymmetric STP(i->j) != STP(j->i). If that's the case, did the putative inhibitory connections cluster around specific input cells? i.e., following Dale's rule? That would be an interesting check.

904: How was this replication of the results with TE-based methods quantified? S5b only shows a similar trend as those in Figure 3, but no quantification. Was this measured on the sparse networks only? And were the properties of the TE-based network and the STTC ones similar regarding their topological properties and fingerprint?

1119: How many cultures were treated with gabazine? Here it mentions "Three". But F6 and the text mention n=9 (6 of them with washout).

1172: A significance value of p < 0.01 was chosen for the connectivity. If I understood it correctly, that means, that on average at this threshold, there's a 0.01 probability the observed SSTC value comes from the surrogate distribution. That would result in a 1% network density just from the false positive rate. That's in line with the values reported in S2a at 7 DIV where the network is probably not yet formed. But does that mean that at 14 DIV the expected number of false positives in the inferred connectivity is ~ 20%? Are the inferred networks robust to changes in the binarization threshold?

Figures:

Figure 2d. Energy. The Clustering and Degree labels might have been swapped.

Figure 3c. Is this for a representative network? Or averaged across the networks?

Figure 6d. How is the shift in the probability distribution related to the wiring becoming more random across all timepoints? Not sure what the authors mean by this.

Figure 6d. There's a mention of SF13e,f, which doesn't exist. Could it be S14c,d?

Figure 7c. Why does the tsne plot only include the dense DIV 28 primary cultures? The other datapoints should also be included, e.g., sparse DIV 14 and gabazine experiments.

Supplementary:

Figure 3. left/right panels should be top/bottom panels.

Figure 10. This figure mentions the dense cultures at DIV 14. Why do they report n=6 when dense cultures are n=12? Or is this figure for sparse cultures instead? The caption also mentions "Distributions are plotted for each […]." There are no distributions in this figure.

Figure 11. It would be beneficial to also add a representative raster (panel a) for the washout case. Results in c report a very high firing rate but no bursting rate for the washout case. What does that look like in the raster?

Figure 11b. The axis should read ISI (it's already in the log scale). Caption mentions a tri-modal distribution for gabazine. Very hard to see when the washout distribution is on top.

Figure 12c. Why is the network size so different between controls, gabazine, and washouts? This is never explained, yet several other measures might depend on this value, e.g., total degree.

Figure 15. Why were only the n=12 DIV 14 dense cultures included here?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Homophilic wiring principles underpin neuronal network topology in vitro" for further consideration by eLife. Your revised article has been evaluated by Panayiota Poirazi (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewer #2 (Recommendations for the authors):

The authors have addressed the points I listed in my original recommendations for the authors. I thank them for the effort.

With respect to my point about "random" vs. "specific" wiring in the context of the GABA block I now have an additional concern:

I now understand that the Pi,j values are not direct probabilities, but just indicate relative preferences for edge placement. In that case, I am not sure a direct comparison of distributions in Figure 6d, and of their means is very meaningful. If all values for Pi,j of a given model were multiplied by a constant >1 then it would not affect the model wiring, as the relative preferences remained unchanged. But in a plot such as 6d it would stretch the distribution out and increase its mean.

Besides, after reading the authors' reply where they elaborate on 6d, I now wonder if there is some confusion about the following two potential ways to plot Pi,j: First, where all potential edges are along the x-axis and Pi,j along the y-axis. Here, an ER network has a uniform distribution. Second, where Pi,j values are along the x-axis and their frequency along the y-axis, as in Figure 6. Here, an ER network shows a single δ peak -- as far away from a uniform distribution as possible.
