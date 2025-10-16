# Peer review - Round 1

Editors:
- Aleksandra M Walczak, École Normale Supérieure France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.49900.sa1](https://doi.org/10.7554/eLife.49900.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The paper addresses experimentally and theoretically the question of clone size distributions in T-cell repertoires. While we have known for a while that these distributions have long tails, experimental data has often not been extremely careful in correcting for biases and a careful measurement of different repertoire subsets is useful. Combining this with a model that tries to explain the origin of this distribution is an important element of the paper.

Decision letter after peer review:

Thank you for submitting your article "The naive T-cell receptor repertoire has an extremely broad distribution of clone sizes" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Satyajit Rath as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Mikhail V Pogorelyy (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

All reviewers agree that the topic of the paper is interesting and important, however the consensus is that in its current form the paper will not appeal to a broad readership, since it is not very conclusive. At the same time the expert reader would be happier seeing all the biases clearly quantified and error bars clearly presented and discussed. As a result, the reviewers are calling for a really major revision (they provide concrete suggestions) and only if they are convinced the message of the paper is clear (e.g. predict observed bulk naive repertoire clone size distributions from a model, discuss differences subsets) will they recommend publication.

In general, the reviewers (the full reviews are attached for clarity on the details) make comments on presentation (citing previous work, putting this work in context for the general reader), being very quantitative and clear about biases and the experimental approach (see comments by reviewer 1) and (comments by reviewer 1 and 3) about the lack of conclusive modeling. Currently the reviewers feel the conclusion of the paper is "the naive T-cell receptor repertoire has an extremely broad distribution of clone sizes" but "we do not have a model that explains it". The reviewers understand that coming up with a completely conclusive model and ruling out all others is probably impossible. However, a more thorough theoretical discussion is needed, considering other models and arriving at one that fits the data (even if it may not be the only one that fits the data).

Finally, the reviewers make concrete suggestions to focus the manuscript on the most interesting aspects of this study worth developing further: a more detailed quantitative analysis of the CD4/CD8 and TCRα/TCRβ repertoires, the reported differences between TCRα and TCRβ, and the differing role of generation probability.

Reviewer #1:

The manuscript by de Greef et al. presents a computational framework to infer the clone size distribution of naive T cells. The main conclusion from this work is that there are large clones in the naive repertoire, the emergence of which could not be explained by the neutral model.

I think both methodology and data are interesting, but additional analysis is needed to address possible concerns outlined below.

1) The first dataset authors use consists of TCRA and TCRB repertoires of FACS-sorted naive and memory cells. As the authors note, FACS is not precise, and a result, naive subpopulation could be contaminated with abundant memory clonotypes. It would be useful to quantify the extent of this contamination. One way to visualize this is to make scatterplots of concentrations of each clonotype (both overlapping and non-overlapping) in naive vs. memory repertoire. As a control, such plots could also be done for naive and memory subsets of different individuals: there should be little correlation between clone frequencies and small overlap, since there should be no contamination on FACS in this case.

2) The end of the subsection “Abundant TCR sequences are frequently shared between naive and memory populations, and are enriched for high VDJ recombination probabilities”:

"if the overlap were the result of contamination only, the P(σ) of the [overlapping] sequences would be expected to reflect those of the memory subsets. Since the overlap is markedly enriched for high generation probabilities, most of it cannot be caused by contamination"

However, green dashed line (which is P(σ) of overlapping sequences) on Figure 1A for β chains (especially for CD8 in volunteer 2) seems to be very close to red lines (probs for memory clonotypes), suggesting that most overlap observed in β repertoires is caused by the contamination between two cell samples on FACS. I suggest modifying the text to avoid contradiction. Also, I think it would be useful to add theoretical prediction for the distribution of generative probabilities of overlapping sequences between mem and naive. If both memory and naive seqs have the same distribution of probs P(σ), then for overlapping(=recombined twice) sequences it should be P(σ) squared, if there is no contamination on FACS. Another way to obtain a prediction for the probability of overlapping sequences in the absence of contamination during FACS is to plot P(σ) for naive sequences of volunteer 1 overlapping with memory of volunteer 2 (and vice versa).

3) In the Discussion section, authors suggest that abundant clones in naive compartment could correspond to naive-like antigen-experienced subpopulation. It might be interesting to look for TCR amino acid sequences of these clones in existing databases of antigen-specific TCRs, such as VDJdb and McPAS.

4) Authors made additional experiment with splitting naive cells into three parts before the mRNA extraction to avoid the potential noise introduced by variance in TCR expression by different cells. Is it possible to quantify, how much bias is removed by using this design? E.g., what happens if we computationally join these three independently sequenced replicates back together, and then randomly assign each of UMIs to one of 3 portions? Are there many clones with elevated TCR transcription levels and thus inflated counts in bulk repertoires? Is this variance in TCR expression different for α and β chains? I think answers for these questions would be interesting for many groups sequencing TCR repertoires with RNA-based technology.

5) Authors fit parameters for different clone size distributions using this additional experiment with splitting naive repertoire into three parts. It would be interesting to compare resulting best fit prediction for clone size distributions to clone size distributions observed in bulk naive repertories of two volunteers, which are analyzed in the first part of the paper (e.g. rank-frequency scatterplots for model vs. data).

6) Another potential explanation for large naive clonotypes may be in the early repertoire development: it is known that TdT is not working, and thus first T-cells lack N-insertions. Previously our group have shown (see Figure 3 in Pogorelyy et al., 2017), that most abundant TCRβ from naive and cord blood (but not memory) repertoires are enriched with zero insertion clonotypes. It would be interesting to see, if abundant naive clonotypes observed in this study are also enriched with zero-insertion clonotypes (e.g. Figure 1B analog with some estimate of total number of N-insertions in each bin on y-axis).

Reviewer #2:

In this manuscript de Greef et al. study the clone size distribution in human naive T-cell receptor repertoires. They do it by a combination of data analysis of TCRA and TCRB sequences and computational modelling. After using FACS to sort the cells they utilized an UMI approach to sequence α and β chains of TCRs from naive and memory compartments of CD4 and CD8 cells. They first make a series of very interesting observations about the differences and commonalities between the generation probabilities (calculated by IGoR) in each cell type (CD4/CD8; naive/memory).

To explain these observations they adapt an ecological neutral model to T cell repertoires. By using this model they come to a surprising conclusion that the clone size distribution in naive T cells is not consistent with a neutral model and nor with a power law distribution. Instead they find that a subset of very large clones in the naive repertoire is essential to explain the data. They discuss an experimental potential artifact that could cause these observations and reason that this is likely not the case. Hence, their final conclusion and strong result is that naive T cell repertoires include a sub-population of very large clones. This conclusion opens a door to an undiscovered biology that determines the construction and dynamics of naive T cell repertoires.

I believe that this manuscript is of high interest to the whole immunology field.

Reviewer #3:

This work investigates potential determinants of the distributions of naïve CD4 and CD8 T cell clone sizes using computational analysis and mathematical modelling of high-throughput TCRα and TCRβ sequence data.

There are several major concerns about this manuscript:

1) Although this work improves on previous studies by considering both TCRα and TCRβ sequences in naive CD4 and CD8 T cell populations and using potentially more accurate quantification of clone sizes (using UMIs), the main conclusion of the manuscript, that the naïve TCR repertoire has a broad distribution of clone sizes, is not substantially novel. Heterogeneous clone sizes in naïve T cell repertoires have been reported, and investigated, in many previous studies (e.g. Robins et al., 2009, Quigley et al., 2010, Venturi et al., 2011, Qi et al., 2014, Pogorelyy et al., 2017). Previous studies have also reported substantial overlap of TCR sequences between naïve and memory CD8+ T cell compartments that is enriched for high abundance TCR sequences that have limited numbers of n-additions (e.g. Robins et al., 2010, Venturi et al., 2011). Furthermore, many studies have previously investigated the associations between V(D)J recombination / TCR production probability, naïve TCR clone size and inter-individual sharing of TCRs (e.g. Robins et al., 2009, Robins et al., 2010, Quigley et al., 2010, Venturi et al., 2011, Li PNAS 2014, Pogorelyy et al., 2017). Importantly, this manuscript has not acknowledged this substantial body of previously published and highly relevant research.

2) While the various models of the naïve T cell clone sizes may be novel, they did not provide sufficient new insights into the primary mechanisms driving the naïve T cell distribution. This was largely due to the fact that no one model considered by the authors could fully explain the observed TCR clone size distributions. One possible reason for this is the growing evidence for developmental- and age-linked heterogeneity in naïve T cell populations (e.g. Hogan et al., 2015, Rane et al., 2018, Reynaldi et al., 2019). Although the authors show model results for a range of parameters, this analysis does not account for the potential impact on the adult T cell repertoire of changes in naïve T cell dynamics over the lifespan of an individual. For example, it has been recently suggested that high abundance zero n-addition TCRs in the adult naïve repertoire have survived since early development and their high abundance is due to different homeostatic pressures in the peripheral repertoire during early development (Pogorelyy et al., 2017). This previous relevant research has not been considered in this manuscript.

3) A potentially interesting conclusion in this study is the limited association between TCRβ abundance, TCRβ production probability, and TCRβ sharing. This result is not consistent with the findings of many previous studies focused on TCRβ repertoires (listed above for concern #1). However, this discrepancy with previous studies was not discussed in the manuscript. Moreover, the authors have not undertaken further investigation to determine the robustness of this result to various parameters/assumptions in the computational analysis or potential explanations for this discrepancy.
