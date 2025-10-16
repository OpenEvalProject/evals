# Author response - Round 1

Authors:
- Sofya A Kasatskaya
- Kristin Ladell
- Evgeniy S Egorov
- Kelly L Miners
- Alexey N Davydov
- Maria Metsger
- Dmitry B Staroverov
- Elena K Matveyshina ([ORCID: 0000-0003-4641-4906](https://orcid.org/0000-0003-4641-4906))
- Irina A Shagina
- Ilgar Z Mamedov
- Mark Izraelson
- Pavel V Shelyakin
- Olga V Britanova
- David A Price ([ORCID: 0000-0001-9416-2737](https://orcid.org/0000-0001-9416-2737))
- Dmitriy M Chudakov ([ORCID: 0000-0003-0430-790X](https://orcid.org/0000-0003-0430-790X))

## Response text

DOI: [10.7554/eLife.57063.sa2](https://doi.org/10.7554/eLife.57063.sa2)

This study uses T cell receptor sequencing to probe the structure of the functional T cell pool in healthy human blood. In particular, the manuscript reports a characterization of TCR α and β repertoire features for eight effector/memory CD4+ T cell subsets defined by flow cytometry across 5 donors, and of several naive CD4 subsets across 12 donors. The key findings are (1) distinctive physicochemical, recombinational, and clonality characteristics for many of the repertoires, and (2) conserved and stereotyped patterns of clonal sharing between the subsets within the donors and of public amino acid chains between donors. All reviewers agree that the results shed significant new light on how T cell dependent immunity is organized. However, there are still some points that we would like to see addressed in the manuscript.

1) It would be beneficial to the readers if the authors could rewrite parts of the manuscript to make the story more coherent. Currently, the manuscript reads as very descriptive, and there is little by the way of hypothesis (except perhaps that Tregs are antigen-selected in the thymus more than are Teff). As a result, the study reads a bit like a series of disconnected observations, and it is hard to build up a clear unified message. Perhaps the authors could also add a table or cartoon of the novel classification suggested by the paper, in which the TCR properties and the repertoire overlaps are matched as much as possible. Currently, the first and the second part of the paper are disconnected, and if both parts are true, these results should be related and suggest a similar classification.

Thank you for the deep comment.

We worked through the whole manuscript to add our considerations where appropriate, and to some extent to better link the effector and naive parts of the manuscript.

We have also included a new section on experimental logic and workflow in the Results, which includes a graphical summary (new Figure 1).

However, it looks like we cannot currently build exact correlations between naive and effector subsets beyond Tregs and, to some extent, CXCR3-positive subsets. We also do not think that we could provide better classification and visualization compared with the current Figures 2, 4, and 5.

2) There is a lack of clarity about the statistical analysis of the differences between the populations which weakens the impact of the conclusions. For example, in Figure 1, it is difficult to get an indication of the extent of the variation that exists, and the biological amplitude of the effect. It is not clear if the parametric ANOVA is the right test here. It would be interesting to do a non-parametric test, based on shuffling of the repertoire labels, for example, and see the extent of variation observed by chance. It would be interesting also to see the results using unique sequences only (not weighted for frequency), perhaps a supplemental data. The magnitude of the effects is quite small – in the order of half a nucleotide length, for example. It would be useful to get a much better feel for the real variation in the population. Similar points apply to other figures.

Effects are relatively small, that’s correct, and so it is important that we observe the very same differences in unrelated healthy donors. To describe the level of deviation from the normal distribution, we built QQ plots for chosen physicochemical CDR3α/β characteristics, Author response image 1. Here we used the comparison to all samples as a post-hoc test instead of multiple pairwise comparisons among the subset groups. This analysis shows that the distribution is normal for most parameters, and thus ANOVA should be the right test.

Non-parametric post-hoc test had little difference from the pairwise assessment of groups with a parametric post-hoc test.

3) The strikingly lower diversity of TH22 and Th2a in Figure 2 seems interesting. Could the authors provide a bit more detail on what is driving these changes? A few very large clones? A different clonal distribution? Or, fewer singlets?

As indicated in the text: “Prominent clonal expansions, reflected by low normalized Shannon-Wiener indices, were apparent in the Th22 and Th2a subsets, indicating focused antigen-specific proliferation.”

4) With regard to the sequence characteristics that differ between subsets: it would be good to confirm that these are not due to differences in V/J gene usage, since the J gene in particular can contribute substantially to the CDR3 and the location of the 5 residue “central” window will overlap to varying degrees with this germline-derived sequence depending on the CDR3 length. It would also be good to rule out the possibility that there are recurrent, semi-invariant amino acid motifs present in the sequences, as opposed to generic sequence biases arising from physicochemical differences.

Several approaches could be utilized to estimate the contribution of recurrent or semi-invariant sequences/motifs. For one, the prevalence of semi-invariant sequences could be reflected in the analysis of CDR3 length and N insertions, as shorter sequences appear in repertoires with higher frequencies. The distribution of N inserted nucleotides is shown in Figure 2A. Another approach could be to search for functional invariant sequences. We performed a search for classical TRA CDR3 described previously for human iNKT and MAIT cells:

iNKT:

CVVIDRGSTLGRLYF, CVVSDRGSTLGRLYF

MAIT:

CAVKDSNYQLIF, CAGMDSNYQLIF, CASIDSNYQLIF, CAAMDSNYQLIF, CAAEDSNYQLIF, CAVVDSNYQLIF, CAVRDSNYQLIF, CAVMDSSYKLIF, CAVMDSSYKLIF, CAVMDSSYKLIF, CAVRDGDYKLSF, CAVSDSNYQLIF, CAVMDSNYQLIF, CAFMDSNYQLIF

Cumulative frequencies of such invariant TRA CDR3s in repertoires were 0.17% for MAIT and 0.14% for the iNKT cells. There were no significant differences in frequencies among subsets. Therefore, this analysis did not reveal any substantial bias in invariant TCRs distribution between functional subsets.

Also, we have initially spent substantial time trying to find any dependencies in V and J usage between the subsets, and have not found any. In general, V and J usages are distributed randomly across the subsets, so this should not be a prominent contributing factor:

5) With regard to differential clonal dynamics: How can the authors rule out the possibility that the apparent differences in clonality arise from differences in mRNA expression of the TCR chains, leading to varying numbers of cDNA templates per cell?

Thank you for the comment. We cannot formally completely exclude this possibility, but it seems unlikely, given that each subset was sorted rigorously on defined phenotypic parameters.

Hypothetically, distinct TCR mRNA expression levels between clones could to some extent influence the apparent differences in observed clonality, which remains beyond the scopes of the current work. However, in reality, all our experience with UMI-based TCR profiling shows that such influence should be negligible.

We would prefer not to overload the manuscript with these considerations, but ready to add the appropriate comment to the manuscript if Editor considers it appropriate.

6) The sharing data (e.g. Figure 3) is a central point of the paper, and is everywhere interpreted as evidence for plasticity, which is not necessarily true. Alternatively, the results could also mean that populations which share more sequences are derived form a common progenitor – in other words a lineage tree effect. It is not clear how the authors distinguish between these two possibilities, and a more detailed discussion would be helpful with this regards.

Formally, we cannot distinguish between these alternative scenarios in our analysis. However, we believe that sharing between the top-2000 most frequent clonotypes is much more likely explained by the current plasticity. Long-term evolution from a common progenitor would most probably result in prominent clonal expansions observed in a particular subset, so that we would not sample the same clone among dominating in two distinct subsets.

As well as with previous question, we are ready to add the appropriate comment to the manuscript if Editor considers it appropriate.

7) With regard to sharing, could the author discuss possibility for convergent recombination to lead to identical nucleotide sequences and hence apparent clone sharing, particularly for sequences that are close to germline. Also, are V/J genes included in the definition of "nucleotide clonotypes" or just the CDR3 sequence?

V-genes were included in the analysis. We have added a note to the legend of Figure 4. We cannot completely exclude the possibility of convergent recombination here. However, its input should be negligible, especially in the top-2000 clonotypes. Please note that increased plasticity is observed predominantly between the subsets with long CDR3s and high count of added N nucleotides (Th22-Th2-Th2a-Th17). i.e. this is not about convergence.

8) Figure 4 is very pretty but unfortunately, very opaque. The legend does not really explain at all what is being shown, or what it purports to show.

Thank you. We do have the high resolution figures and will definitely take care of the quality during the final stages of manuscript preparation together with the Editors. We have also worked on the figure legend to make it more informative.

9) A general question: Are the TCR differences between the phenotypes large enough to classify a cell based upon its TCR into a phenotype? Probably not, which would mean that the results are (very interesting) trends.

No, of course not, not only because the differences are small, but also because it is a clone-specific story. This only works as average characteristics of the subset-specific repertoires, likely reflecting other factors that determine fate decisions, including the context of antigen presentation, as highlighted in the Introduction.

As we indicate now in the text (first chapter of Results):

“It should be noted that the above characteristics were observed for the averaged, cumulative portrait of many TCR variants representing each subset. Each particular T cell with low number of N-added nucleotides and strongly interacting aminoacids in the middle of short CDR3 may belong to any Th subset, but more probably to Tfh, Th1, or Th1-17.”
