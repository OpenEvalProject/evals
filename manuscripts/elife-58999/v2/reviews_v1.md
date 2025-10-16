# Peer review - Round 1

Editors:
- Detlef Weigel, Max Planck Institute for Developmental Biology Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58999.sa1](https://doi.org/10.7554/eLife.58999.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study revisits an old debate in the ecology literature dating back to the 1940s: Does diversity promote or constrain diversity at different levels, and how is diversity maintained? These questions have been investigated in communities of macroorganisms, but this is probably the first high-level analysis of a large microbiome dataset to explore how species interactions influence microbial diversity. The authors found support for the "Diversity Begets Diversity" (DBD) hypothesis in habitats with lower overall diversity, while in habitats with higher overall diversity, the "Ecological Controls" (EC) hypothesis appeared to more closely describe patterns of microbial diversity. The paper has a great mix of modern tools, historical ideas, and interdisciplinary science. It is clearly written and the analyses are generally carefully executed and presented.

Decision letter after peer review:

Thank you for submitting your article "Does diversity beget diversity in microbiomes?" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Detlef Weigel as the Reviewing and Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Eric Kemen (Reviewer #1); Benjamin E Wolfe (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

Madi and colleagues revisit an old debate in the ecology literature dating back to the 1940s: Does diversity promote or constrain diversity at different levels, and how is diversity maintained? On one hand, having more species to interact with can create new niches and promote diversity. On the other hand, more species might mean more competition that would limit additional gains in diversity. While these hypotheses make opposite predictions, they are not mutually exclusive and likely act in tandem during community assembly. As the authors note, these questions have been asked in communities of macroorganisms, but this is probably the first high-level analysis of a large microbiome dataset that explores how species interactions influence microbial diversity.

The authors found support for the "Diversity Begets Diversity" (DBD) hypothesis in habitats with lower overall diversity, while in habitats with higher overall diversity, the "Ecological Controls" (EC) hypothesis appeared to more closely describe patterns of microbial diversity.

There are many caveats when inferring microbial interactions and other dimensions of microbial diversity from 16S rRNA amplicon data, but this work provides a great jumping point for many future studies to experimentally test some of the conclusions of this analysis.

The paper has a great mix of modern tools, historical ideas, and interdisciplinary science. It is clearly written and the analyses are generally carefully executed and presented.

However, there are also several significant concerns, which we hope the authors will be able to address.

Essential revisions:

1) A third significant hypothesis is missing that makes predictions about how diversity can affect net rates of diversification, The Neutral Theory of Biodiversity and Biogeography (NT). The pattern the authors observed – decreased diversity slopes within clades embedded within more diverse communities – can be explained by a neutral model devoid of ecological interactions. Let us consider a simple neutral model that has a rate of diversification intrinsic to each unique taxonomic unit (new taxa emerging per generation per unique taxonomic unit) and a rate of stochastic extinction that is proportional to the population size of each taxonomic unit. The probability that any taxa diversifies would be uniform throughout the community, however, as the diversity increases, this increases the number of unique units that can yield new taxa and thus the rate of influx of new taxa. At some tipping point, however, the community will become so diverse that the population size of any given taxa will be low and susceptible to stochastic loss. This will cause the net diversification rate to drop in more diverse communities. This is just a simple example and it does not consider migration, which is important for shaping microbial diversity; however, it demonstrates that other forces outside of the ecologically-based models of DBD and EC may be acting to produce the patterns under investigation. It is important to rule out NT's parsimonious predictions before moving on to testing sophisticated ecological theories.

2) Following from the NT discussion, there is likely an important role for extinction in shaping these patterns. The discussion of hypotheses focused on the production of diversity and not the net balance of production and loss. This omission is a major weakness of the paper; some discussion of the role of extinction in these patterns would strengthen the interpretations.

3) The analysis of the relationship between genome size and DBD in the context of the Black Queen Hypothesis is not convincing. As the authors acknowledge, there are serious limitations with assuming that the genome size from one strain/species within a genus can fully represent the genome size of that genus. The authors do not provide an estimate of how much error might result from this approach (for example, by looking at several genera where many genome sizes exist and seeing how that impacts their analyses). They also do not fully explain their rationale for some aspects of this analysis; for example, why was the largest genome size available used? Why would having more precise genome data make the positive relationship stronger?

We suggest that this part of the analysis is removed in the revision. You may refer to it in the Discussion as speculation.

If you decide to discuss genome size and how this could correlate with more metabolic functions, you should elaborate further on this. Generally genome size correlates to repeats rather than additional metabolite clusters. You could use the available genomes to annotate genome clusters (using e.g. antiSMASH).

4) One of the major findings is the evidence for DBD being strongest in less diverse biomes and weaker in more diverse biomes. However, some of these biomes also suggest a correlation with total microbial load. For example, the animal distal gut is a less diverse biome but an extremely densely populated biome, whereas the soil biome is exceptionally diverse but has a lower total microbial density than the distal animal gut. Do the authors have access to any data about the population density in these different biomes? Does population density also correlate with the DBD-EC continuum? If the authors do not think that total microbial load factors into the DBD-EC continuum, they should provide an explicit rationale why not. Note that we do not expect that microbial population size data are available for the entire data set, but perhaps there is a subset for which this is available and that could be analysed.

5) For model validation for GLMMs, it would be useful if the authors could report goodness of fit for all their models (differences between the observed values and the model's predicted) using the Akaike's Information Criterion (AIC) or the Bayesian Information Criterion (BIC). Further, using cross validation (dividing data to train and test) might be useful to estimate the error rate of the models and could be used to confirm the accuracy of the models.

Additional major comments:

6) The measures for diversity vary over the paper and it is not always clear when which measurement is used, which makes it difficult to compare the analyses. Where the measures differ, this should be justified.

For example, this is clear in Figures 1, 4 and 5, but not in Figure 2. Similarly, Figure 2—figure supplement 1, which show the number of focal taxa as a function of the number of non-focal taxa, but in Figure 3 the diversity slope was estimated from a GLMM using taxonomic ratio for the community diversity, without mentioning what diversity measure was used for focal lineage. More generally, are taxonomic ratios a good measures of lineage diversity? Please explain why you used these measures of diversity instead of others. You mention that you also tried others such as Shannon index that are also robust but did not follow up on this.

7) In the very beginning of the Results, the authors note that a null model was used to assess the slopes from their GLMMs (subsection “Quantifying the DBD-EC continuum in prokaryote communities”), but details are provided only later in the Materials and methods. We think the paper would be very much improved if the authors spent a paragraph explaining the null model early in the Results section and if a data figure (or figures) from the null model were moved to the main body of the text from the supplementary information. This would help the reader understand how support for significance of the slopes was determined as they move through the rest of the paper. More importantly, the paper would have greater readability and impact for a broader audience if the authors explained the development and rationale of their null model in very simple terms.

8) The term ASV is used throughout, but the downloaded databases contain mainly OTUs. This of course could affect the outcome of an analyses depending if OTUs and ASVs are mixed or either OTUs or ASVs are used. Please explain in more detail what was used and how it was calculated.

9) A major limitation that is not acknowledged is a sole focus on prokaryotic taxa. Many of the ecosystems sampled in the EMP dataset have diverse and abundant fungi, protists, and other types of microbes. It is likely that these other microbial taxa interact with the target bacteria studied in this work in diverse ways (as numerous previous studies have shown). The authors should acknowledge this major limitation and explore briefly how it may impact their findings in the Discussion of the text. For example, fungi may play disproportionate roles in some environments that explain some of the variation observed here (e.g. the rhizosphere).

10) Subsection “Abiotic drivers of diversity”, last two paragraphs: These two paragraphs contain two analyses that essentially contradict each other. These varying results are interesting – could you please expand a little more on why these two analyses might be showing different results? In particular, the last sentence suggests that diversity levels in soil and other communities with a DBD plateau are predominantly controlled by abiotic factors. However, this is the first mention of those specific biomes in this paragraph. Could you add a little more about this observation?
