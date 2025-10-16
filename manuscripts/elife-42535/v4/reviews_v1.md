# Peer review - Round 1

Editors:
- Antonis Rokas, Vanderbilt University United States

Reviewers:
- Iker Irisarri, Uppsala University Sweden

## Review text

DOI: [10.7554/eLife.42535.031](https://doi.org/10.7554/eLife.42535.031)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "An updated phylogeny of the Alphaproteobacteria reveals that the Rickettsiales and Holosporales have independent origins" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Patricia Wittkopp as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal his identity: Iker Irisarri (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Muñoz-Gómez et al. performed phylogenomic analyses to resolve evolutionary relationship of deeply branching lineages in Alphaproteobacteria. This is a challenging job, as different lineages within Alphaproteobacteria have very different genomic base and amino acid compositions, and also have very different evolutionary rates. The authors figured out that the compositional heterogeneity is the major factor that makes the estimate of Alphaproteobacteria phylogeny so difficult. They presented a number of new evolutionary relationships that differ from the previous results. Among these new observations, the most significant one is that Rickettsiales and Holosporales may have independent origins, which contradicts the well-established concept that these two intracellular symbiotic lineages shared a common ancestor which transited to intracellular lifestyle only once. The relative branching of the different alphaproteobacteria are tested with several sensitivity analyses, culminating in a consensus that is reflected into a new taxonomy.

Essential revisions:

1) While the new hypothesis of independent origins of the two intracellular lineages is interesting, this manuscript appears to have created more controversies of the evolutionary relationships among other important lineages in Alphaproteobacteria that have been discussed extensively in recent years. Perhaps the most important change is that Pelagibacterales becomes sister to the Rhodobacterales, Caulobacterales and Rhizobiales in the present study. Pelagibacterales takes a free-living lifestyle, but it shares a number of genomic and evolutionary traits (genome size, genomic GC content, and genomic evolutionary rate) with the above two intracellular lineages. This makes the phylogenetic placement of Pelagibacterales and the intracellular lineages in Alphaproteobacteria interesting but challenging. There have been several hypotheses for the phylogenetic placement of Pelagibacterales, most of which were proposed in studies that were not designed to resolve this phylogenetic controversy or did not use the correct evolutionary models to control for the intrinsic bias in the genome sequences. In the present study, to support their argument the authors only cited the results from the studies that show the similar phylogenetic placement of Pelagibacterales, but ignored other more relevant studies including a study published in 2015 (https://www.ncbi.nlm.nih.gov/pubmed/25431989) which provided the first conclusive evidence that compositional heterogeneity causes the difficulty in placing Pelagibacterales in the Alphaproteobacteria tree, based on which that paper was able to reject alternate hypotheses including the one that is shown in the present manuscript and the papers it cited.

We do not mean that the new hypothesis of independent origins of the two intracellular lineages must be wrong, but we think it is essential that, before reaching this exciting conclusion or proposing this attractive hypothesis, the authors should be able to repeat some of the important evolutionary relationships which have already had excellent progress (like the evolutionary position of Pelagibacterales, though it remains controversial) or should provide strong evidence against it if their new finding disagrees with it. Without this, any new significant proposal like the independent origins of the two intracellular lineages is not convincing.

2) There are a few places where the authors state results whose "data [are] not shown". The authors should either remove these statements or show the supporting data.

3) The authors test the position of long-branched lineages (Rickettsiales, Holosporales, Pelagibacterales) by removing two of them at a time. However, one hypothesis that was not tested is whether the position of Rickettsiales might be the product of a long-branch attraction to the distant outgroup. Please perform an analysis including Rickettisales (but not Holosporales and Pelagibacterales) and no outgroup and see if the position of Rickettsiales varies relative to the other lineages, which would suggest its position is the product of a long-branch attraction. Similarly, the reviewers were not convinced (or the text was not clear) by the conclusion that Holosporales are derived within Rhodospirillales (e.g. Discussion paragraph one, also shown in Figure 3). This totally depends on the position of Alphaproteobacterium HIMB 59, which is also unstable across the analyses. For example in Figure 2B, Holosporales + Alphaproteobacterium is the sister group of Rhodospirillales and not derived within. This is particularly important since the authors propose to lower the rank of Holosporales in their taxonomy.

4) Dataset assembly. The authors use the Wang and Wu, 2013, and complement it with recently sequenced species for completeness. But was this done using the Phyla-AMPHORA pipeline, or using another ad-hoc pipeline? First of all, it appears that the authors did not perform any kind of data curation to make sure that the new species did not include contaminations, deep paralogy or LGT issues, and in our opinion this is a must. Likewise, there is no information about the alignment algorithm and trimming (if performed).

5) Regarding phylogenetic analyses, it seems the LG replacement matrix was chosen without even comparing its better fit statistically (e.g. AIC or BIC). The authors use +R6 and +R8 to account for among-site rate heterogeneity in different analyses, but without an apparent reason for that. Lastly, please provide information on the ESS values for Bayesian runs to have a better grasp on the chain convergence.

6) One of aspects why the phylogeny of alphaproteobacteria is of broad interest is the mitochondrial lineage. We wonder why the authors did not try to place the mitochondria into their analyses. We assume this would bring additional biases into an already difficult dataset, but we think we could have gotten an interesting insight given the vast amount of analyses performed with various strategies to reduce systematic errors.

7) Abstract: it would be best to remove the fifth sentence, given that the support for these findings is not definitive. Additionally, it is important that you add that this study proposes an updated taxonomy for alphaproteobacteria, which is one of the major outcomes of your study.

8) Conclusions: please remove the last two sentences of the conclusion. The one before last could be said for every study ever done. The last sentence is a bigger topic but including a single sentence in the conclusions fails to do it justice. If you want to discuss this issue, please include a paragraph in the discussion – as is, it comes out of the blue (and it's not clear why phylogenetic inference will be improved; if additional sampling keeps adding long branches, it may very well be that more uncertainty is introduced).

Introduction, third paragraph: It is generally well accepted that these three factors (few taxa, few genes, and models with poor fit) lead to systematic error. But your claim that previous studies were compromised by one or more of these factors in this section seems very hand-wavy. Can you give specific examples? Simply saying taxon sampling / model usage was poor in this or that study seems subjective – please give specific information as to why these studies had suboptimal designs (e.g., how many taxa were included, which of the major groups were sampled, why the model was a poor fit, etc.)

Subsection “Compositional heterogeneity appears to be a major confounding factor affecting phylogenetic inference of the Alphaproteobacteria”, second paragraph: please briefly introduce in a short paragraph how you built the data matrix before you start describing how you analyzed it.

Subsection “The Holosporales is unrelated to the Rickettsiales and is instead most likely derived within the Rhodospirillales” and “The Geminicoccaceae might be basal to all other free-living alphaproteobacteria (the Caulobacteridae)”: there are no page (or supplement size) restrictions, so please show the data.

Figure 3: the figure lists taxonomy family names (e.g., Holosporales) but the legend discusses order family names (e.g., Holosporaceae) and what the triangles correspond to is not explained. Please clearly annotate the figure.

Figures 2 and 3: the color-coding scheme of the different clades doesn't appear consistent. Please revise.
