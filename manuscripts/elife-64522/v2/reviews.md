# Peer review - Round 1

Editors:
- Sandeep Krishna, National Centre for Biological Sciences‐Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64522.sa1](https://doi.org/10.7554/eLife.64522.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper provides a detailed analysis of the master regulatory network involved in small cell lung cancer. Using multiple mathematical tools, the authors transform a complex, highly connected network into a small, easy-to-interpret reduced form. The reduced network provides insight into the topological features – here the existence of two "teams" of genes that inhibit each other – that determine the non-genetic phenotypic plasticity in these cancer cells. The concordance between the reduced network and experimental knowledge from the field suggest that these methods may be useful more broadly to make sense of complex regulatory networks elsewhere.

Decision letter after peer review:

Thank you for submitting your article "Topological signatures in regulatory network enable phenotypic heterogeneity in small cell lung cancer" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Jean Clairambault (Reviewer #1); David Wooten (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The reviewers appreciated your detailed analysis of the regulatory network involved in small cell lung cancer. However, they also raise some concerns that are expressed in the reviews appended below. In your revision, please try to address the concerns of the reviewers, in particular please expand your analysis and comparison to similar results in literature (Reviewer 2) and discuss how your methods could be generalized to apply to other networks (Reviewer 3).

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Reviewer #1:

Detailed study of the master regulatory network of SCLC by probabilistic methods, focusing on the two genes ASCL1 and NEUROD1. Supports by up-to-date literature reports and sound gene expression analysis the non-genetic phenotypic plasticity of SCLC cells. May be a major step forward in understanding non-genetic phenotype plasticity in cancer.

Firstly, let me say that the technical aspects of this very detailed study go far beyond my field of expertise. I will evaluate it from an external eye, and according to the contribution it brings to the investigation of non genetic phenotype plasticity in cancer, here focusing on small cell lung cancer (SCLC). Plasticity in cancer cells is indeed a major field of research nowadays, resulting in metastasis and drug persistence/tolerance, and especially SCLC has escaped efficacious treatments until now.

As far as I could understand the analysis, by two different methods, one based on Boolean networks, the other on elementary (nevertheless of great dimensionality) ordinary differential equations, the authors statistically “shake” the possible parameters of the regulatory network of genes found “masterly” expressed in SCLC, according to a study of 2017 (Udyavar et al., 2017), network in which one can recognize 3 of the 4 Yamanaka genes, MYC, KLF4 and SOX2.

Rather than on the Yamanaka genes, the authors focus on the two genes ASCL1 and NEUROD1, for both of which they find marked differential expression (high/low), resulting in 4 different coupled phenotypes at the gene expression level, which, as “patterns of steady states seen in influence and correlation matrices”, correlate with experimental results collected from experimental data on SCLC. Indeed, ASCL1 and NEUROD1 had already been identified as master regulators of the salient gene network of SCLC, ASCL1 being a neuroendocrine marker and NEUROD1 being associated with mesenchymal markers susceptible of inducing metastasis, i.e., two markers of plasticity.

The design of this analysis relies on an apparently complete analysis of the scientific literature on both the subject of non-genetic phenotypic heterogeneity and the particular case go gene expression studies on SCLC. The results reported by the authors support by gene expression analyses the idea that within the same genomic status of SCLC cells, different steady states in gene expression lead to different phenotypic states (multistability) that are found experimentally. Although no clear therapeutic perspective for SCLC emerges from this study, it is an interesting step to better understand the plasticity of SCLC cells, possibly resulting in their drug tolerance and thus escaping treatments so far.

For these reasons, I propose that this study be published as it is in eLife.

Reviewer #2:

This paper will be of interest to researchers working on the origins of cellular heterogeneity in cancer. Using network and gene expression analysis, previous known findings on the potential role of topology in generating four broad cellular states in small cell lung cancer (SCLC) are confirmed here. Interestingly, it is observed that both discrete and continuous gene expression models can give rise to similar steady states. Two modules of genes inhibiting each other are found to lead to the four emergent states in SCLC. However, these results are not well compared and contrasted in the context of prior literature.

Chauhan, et al. investigate the origins of cellular heterogeneity in Small Cell Lung Cancer. Previous experimental work has classified four major states based upon the expression levels of Ascl1 and Neurod1 genes, along with other states. Previous computational work based on Boolean networks (Wooten et al., 2019 and Udyavar et al., 2017) suggested these four states may arise naturally as the steady states of the underlying gene-interaction network in SCLC.

Here the authors re-analyze the SCLC gene-interaction network based on a Boolean framework with an underlying Ising hamiltonian. They show that the four major states based on Ascl1 and Neurod1 can be recovered from dynamic simulations of the 33 node 357 edge network. While not surprising in the light of prior work, the authors successfully demonstrate that a somewhat different Boolean framework leads to similar results, suggesting the underlying topology is indeed important for generating cellular heterogeneity. However, it is not clear whether this formalism based upon the Ising Model improves upon the previously used Boolean framework (Wooten et al. and Udyavar et al) in any way.

The authors then model the dynamics of the gene network using ODEs, allowing continuous values for the expression levels of the nodes. 4 of the top 10 frequent steady states corresponded to the 4 states found earlier. However, these 4 states have much lower frequency (adding up to only about 22%) whereas in the Boolean framework the frequencies added up to almost 100%. The identity and frequencies of the remaining 6 out of 10 frequent states is not discussed.

Using a pairwise correlation strategy for all the nodes, the authors then uncover an interesting result: the nodes fall into two modules that repress each other. This also seems to be true in two publicly available gene expression datasets. Surprisingly, Neurod1 did not appear in these modules and it is unclear why, given the four main states are defined based on Neurod1 and Ascl1 expression levels. The two modules are also distinct from the higher number of modules found earlier (Wooten et al., 2019), and it is unclear why these differences arise.

Finally, using a series of clustering algorithms (hierarchical and K-means clustering, UMAP) on gene expression datasets, the authors show that not only the 4 states based on Neurod1 and Ascl1, but also further states based on Pou2f3 and Yap1 expression levels can be recovered. However, the authors use only a few genes of interest in performing the clustering and it is not clear why all the available genes were not used.

In my opinion, the most significant area where this manuscript needs to be strengthened is in providing critical comparisons with prior literature and results (primarily Wooten et al and Udyavar et al). Discussions on what advances have been made in this paper with respect to what was already known earlier, need to be highlighted. I found it quite hard to judge this manuscript and place it in context, since a lot of the methods and datasets used here are very similar to the previous works. Detailed suggestions along these lines as well as some possible new analyses are provided below:

1) It would be good to know why the authors chose an Ising Model – based Boolean simulation strategy as compared to the Boolean model used in Wooten at al. Is there some difference in the statistics expected from these two different formalisms? Is there some limitation of the previous work that the authors wanted to address here? Given that Wooten et al. showed that the 4 SCLC states can be recapitulated, is it surprising that the authors get the same 4 states using their Boolean method on an identical network?

2) For the ODE method, the frequency of the four states add up to only about 22%. It would be interesting to see a full list of the top ten states with their frequencies, and a discussion on why these other states appear in the ODE but not in the Boolean formalism and its biological implications.

3) Following up on point (2) above, was there a reason for using two separate axes for the same quantity (frequency) in Figure 1D i ? I found this quite confusing, because for example, at first sight it seems like the S2 steady state has similar frequencies in RACIPE vs Boolean. But the frequencies are in reality very different, right? I would therefore suggest to plot both RACIPE and Boolean results using just one axis, to avoid confusion.

4) The observation of two "modules" using pair-wise correlations is interesting. However, it was unclear to me why Wooten et al. find 17-18 modules, though their WGCNA method also uses a pair-wise gene correlation technique. A detailed discussion on this would be very helpful for readers in my opinion.

5) Related to the pair-wise correlation method, I was surprised to see that Neurod1 does not seem to be part of any module in Figure 2. In the Discussion, the authors mention that Ascl1 and Neurod1 don't fall in the same team, but it seems to me from Figure 2 that Neurod1 doesn't belong to any team! This seems to be contradictory to the rest of the results, unless I have misunderstood something here. A discussion on these lines seems warranted.

6) Given that the dynamical simulations were carried out with 33 genes, why did the authors choose to perform all the clustering analyses with only a handful of genes? This may be problematic, for example, if sets of 2 or 4 randomly chosen genes are used for clustering the expression datasets, how likely are we to find a few well separated clusters? If we find that random gene subsets also separate into clusters, how biologically meaningful is it to see clusters with Ascl1 and Neurod1?

Reviewer #3:

This work by Chauhan et al. finds order from complexity. Using multiple mathematical tools, they transform a complex, highly connected network into a small, easy-to-interpret reduced form. The concordance between their reduced network and experimental knowledge from the field support the insights they gained from their analysis here, and that their methods may be useful more broadly to make sense of complex networks elsewhere.

The final findings (Figures 4-5) on experimental data, which show that just a few genes can reproduce the full-spectrum of known SCLC heterogeneity seem to strongly support the authors' primary conclusions. Specifically, a system which is well classifiable using a few nodes closely matches my expectation for a network that can be reduced to a few tightly connected groups of nodes.

The agreement between Boolean and RACIPE greatly strengthen their results.

The J metric is interesting, and while it would be beyond the scope of this work, I would be very interested in seeing it applied to other networks to see how generalizable its interpretation is. However, the definition is tightly coupled to the 33 genes in this network, and their pattern of expression in the steady states. Discussion about how the metric could generalized would strengthen the manuscript.

I found it very interesting that not only Neurod1, but also Elf3 was pulled out as an individual node in the reduced form. In another work (Wooten et al., 2019), the authors identified ELF3 as a master regulator of one of their subtypes (NEv2). The identification of this node through topological features here also lends further credence to the influence matrix.

The authors state that "These results suggest that influence matrix is a better representation of network topology as compared to the interaction matrix.". However, since the influence matrix comes from the interaction matrix, it seems like it necessarily contains less information. The authors make this claim based on the fact that a network reduction based on influence matrix more closely represents the steady state distributions than a similar reduction based on interaction matrix. But it is not clear how much this conclusion is specific to this particular network, or reduction strategy.

The correspondence of the steady states with expression data appears quite promising! However, the fact that Neurod1 is the sole gene that distinguishes S1 from S4, or S2 from S3, makes me suspect other genes must also contribute to the difference? Are there other genes in the literature that the authors think could be included into new versions the network that could give a broader picture of the differences between S1 vs S4, or S2 vs S3? Given the other 31 nodes in the network, do their steady state values more closely match one or another cluster from Figure 4B?

When introducing the Font-Clos si(t+1) equation, I recommend to describe what happens if si=0, rather than just including that info in supplement.

Figure 1B should have a legend indicating dark=off, blank=on (even though it is in the caption)

I do not see what test / method was used to find the +/- % confidence intervals in Figure 1B, nor what size interval they represent (e.g., 95%?)

The reference in-text to Figure 1C, i, regarding swapping random edges, seems to actually refer to both i and ii

In the text, the connection between the larger number of steady states of "random" networks to the true network's topology lacks a relevant reference to Figure 1C, iii

The text introducing the J metric should describe what the indices are, rather than requiring the reader to search the figure.

The introduction of influence matrix was very hard to follow, the grammar is confusing, and "lmax" is not clearly described in the main text, even though it is used several times.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Topological signatures in regulatory network enable phenotypic heterogeneity in small cell lung cancer" for further consideration by eLife. Your revised article has been evaluated by Aleksandra Walczak (Senior Editor) and a Reviewing Editor.

The reviewers are happy with the revisions you have made and the paper is almost ready for acceptance, but one substantive point raised by Reviewer 2 remains (see below). Please try to perform clustering analysis for randomly chosen sets of 2 genes (other than ASCL1 and NEUROD1). If these don't result in well-separate clusters it strengthens your result, but if they do then you can modify your statements accordingly, for instance by expanding on other biological reasons to focus on ASLC1 and NEUROD1 based clustering. Alternatively, if you feel such clustering based on randomly chosen genes is not useful, please provide some reasons why you think so.

Reviewer #2:

The authors have now satisfactorily responded to most of the comments/queries.

Their response to point (6) that I had raised is not entirely satisfactory however, since they do not seem to have addressed the randomization point that I had raised. If random sets of two (or more) genes are chosen for the clustering analysis, how often do we see well separated clusters? It seems to me an important point to analyze and understand, in order to put the ASCL1 and Neurod1 based clustering in perspective. I would strongly urge the authors to include this analysis, unless they feel this is not a sensible question to address, in which case it would be good to hear their arguments against this.

Reviewer #3:

The revised manuscript addresses my original comments, and I support its publication.
