# Peer review - Round 1

Editors:
- Neil M Ferguson, Imperial College London United Kingdom

Reviewers:
- Edward A Wenger, Institute for Disease Modeling United States
- Oliver Brady, London School of Hygiene & Tropical Medicine United Kingdom

## Review text

DOI: [10.7554/eLife.43481.028](https://doi.org/10.7554/eLife.43481.028)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The geography of malaria elimination in Bangladesh: combining data layers to estimate the spatial spread of parasites" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Neil Ferguson as the Senior Editor and Reviewing Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Edward A. Wenger (Reviewer #1); Oliver Brady (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The authors provide a logical framework for combining multiple data sources relating to travel history and parasite genetics, resulting in a single updated risk map for the Chittagong Hill Tracts region of Bangladesh. This updated map is informative of source-sink dynamics beyond simple prevalence/incidence measures produced by traditional epidemiological approaches and is therefore likely to be useful to NMEPs. Combining data layers in this way is a non-trivial problem due to the idiosyncrasies of different types of travel data and the complex signal in Plasmodium genetic data, and so this represents a significant step forward in terms of demonstrating the applied utility of Plasmodium genetic data over large spatial scales.

The manuscript is clear and well-written. Nevertheless, we have some comments that should be addressed:

First, this paper would benefit from more context in the presentation and interpretation of genetic signatures:

a) How do complex infections or inferred within-sample diversity vary among samples and between geographic regions? Does this tell a complementary story to the parasite pairwise relatedness?

b) Does presenting the relatedness information as a graph structure rather than bulk properties of pairwise relatedness provide any additional insights?

c) Can the authors give more context for choices of relatedness thresholds – 10% "nearly identical" (subsection “The association between genetic data, travel survey, and mobile phone data” last paragraph) and 17.5% similarity (subsection “Genetic analysis”, last paragraph). How do these relate to e.g. 1 or 2 outcrossing events with random parents drawn from population-level minor allele frequencies?

The big difference in coverage of travel survey and mobile phone data makes the assessment of their comparability / complementariness quite difficult to assess as a reader. While we appreciate there is not much the authors can do to change this, there are changes to the way the data are presented that could improve this, e.g. Figure 4 would be easier to interpret differences between the two data sources if only areas for which both travel survey and mobile phone data were available. The discussion could also elaborate more on the implications of this disparity in coverage.

Given the huge amount of work that has gone into this analysis, the final risk map (Figure 5D) is disappointingly non-specific. To what extent is this east-west flow of parasites a new result, or is it already known to some degree? If resources were limited, what would be the suggestion about how best to use them? Can top importation routes be predicted, and how much of total importation would they account for?

We have some concerns about the new genetic mixing index. This is presented as an odds ratio on samples being in near vs. far spatial unions given their level of genetic similarity, but does this not have the "exposure" and the "outcome" the wrong way around, i.e. what we observe is genetic similarity as a function of distance, not the converse? The symmetry property of odds ratios means that numerically swapping these round (i.e. Prob (genetically similar | far)) would result in the same final value, but would seem to make more intuitive sense.

There are many ways of constructing a statistic to measure the relationship between geographic and genetic distance, and so some statistical justification is needed for the use of an odds ratio. I'm sure the authors are aware that odds ratios are typically avoided in general due to frequent misinterpretation as risk ratios and their extreme behaviour in some parts of the parameter space (a small difference in probabilities could lead to a very small or very large difference in odds). For example, if the "rare disease" assumption is being used to justify this statistic then this should be stated. If no justification can be given then perhaps a risk-ratio would be more appropriate.

Some representation of uncertainty in the genetic mixing index should be given, either analytically or by simulation. Extreme uncertainty is another known weakness of odds ratios, hence it needs to be addressed.

There is a tendency to swap between talking about genetic similarity as a function of distance (e.g. subsection “Genetic and model-based evidence of transmission in low incidence areas”) and distance as a function of genetic similarity (e.g. Figure 3A) without appreciating that this involves a transformation. For example, when talking about the probability of geographic distance between parasite pairs (Figure 3) there must have been an application of Bayes' rule with a particular prior on distance, but this is not formally stated. Note that using the raw counts without a prior is equivalent to assuming a uniform prior on distance, which is almost certainly not appropriate here (we would not expect points to be uniformly separated a priori).

How sensitive are values of the genetic mixing index to non-uniform sampling of clinical infections or genetic sequences from different transmission regions or subpopulations?

Note – we understand and appreciate the intent of the genetic mixing index and feel it could be a valuable addition to the analytical toolbox, but it does need to pass certain basic statistical checks to avoid issues later on.

Reviewer #1:

This an important body of work, combining different sources of mobility data – travel surveys, mobile-phone records, parasite genetics – to quantify epidemiological and programmatic endpoints.

1) This paper would benefit from significantly more context in the presentation and interpretation of genetic signatures.

a) How do complex infections or inferred within-sample diversity vary among samples and between geographic regions? Does this tell a complementary story to the parasite pairwise relatedness?

b) Does presenting the relatedness information as a graph structure rather than bulk properties of pairwise relatedness provide any additional insights?

c) Can the authors give more context for choices of relatedness thresholds – 10% "nearly identical" (subsection “The association between genetic data, travel survey, and mobile phone data” last paragraph) and 17.5% similarity (subsection “Genetic analysis”, last paragraph). How do these relate to e.g. 1 or 2 outcrossing events with random parents drawn from population-level minor allele frequencies?

2) How sensitive are mixing-metric values to non-uniform sampling of clinical infections or genetic sequences from different transmission regions or subpopulations?

Reviewer #2:

The authors provide a logical framework for combining multiple data sources relating to travel history and parasite genetics, resulting in a single updated risk map for the Chittagong Hill Tracts region of Bangladesh. This updated map is informative of source-sink dynamics beyond simple prevalence/incidence measures produced by traditional epidemiological approaches, and is therefore likely to be useful to NMEPs. Combining data layers in this way is a non-trivial problem due to the idiosyncrasies of different types of travel data, and the complex signal in Plasmodium genetic data which is just starting to be leveraged effectively. This manuscript therefore represents a significant step forward in terms of demonstrating the applied utility of Plasmodium genetic data over large spatial scales.

One potential point of weakness in the analysis is the presentation of the new genetic mixing index. This statistic is presented as an odds ratio on samples being in near vs. far spatial unions given their level of genetic similarity. First, does this not have the "exposure" and the "outcome" the wrong way round, i.e. what we observe is genetic similarity as a function of distance, not the converse? The symmetry property of odds ratios means that numerically swapping these round (i.e. Prob (genetically similar | far)) would result in the same calculation, but would seem to make more intuitive sense.

Second, there are many possible ways of constructing a statistic to measure the relationship between geographic and genetic distance, and so some statistical justification is needed for the use of an odds ratio. I'm sure the authors are aware that odds ratios are typically avoided in general due to frequent misinterpretation as risk ratios and their extreme behaviour in some parts of the parameter space (a small difference in probabilities could lead to a very small or very large difference in odds). For example, if the "rare disease" assumption is being used to justify this statistic then this should be stated. If no justification can be given then perhaps a risk-ratio would be more appropriate. Some representation of uncertainty should also be given, as again this is a weakness of odds ratios. Keep in mind that this statistic may well be taken up by the community and applied/interpreted in other scenarios, and therefore it is important to ensure statistical robustness at this stage.

On a similar note, there is a tendency to swap between talking about genetic similarity as a function of distance (e.g. subsection “Genetic and model-based evidence of transmission in low incidence areas”) and distance as a function of genetic similarity (e.g. Figure 3A) without appreciating that this involves a transformation. For example, when talking about the probability of geographic distance between parasite pairs (Figure 3) there must have been an application of Bayes' rule with a particular prior on distance to obtain this. Note that using the raw counts without a prior is equivalent to assuming a uniform prior on distance, which is almost certainly not appropriate here.

I could not find a reference or SI detailing the 101 SNP barcode used. Are all these SNPs in linkage equilibrium? Given that other investigators are likely to apply the genetic mixing index on larger data sets, some comment on the effect of LD on this statistic would be welcome.

Other than these statistical issues I have no major concerns with the manuscript, which is well-written and makes a significant contribution to the field.

Reviewer #3:

This manuscript by Chang et al. details an interesting assessment of the combination of travel and genetic data to assess malaria elimination strategy in Bangladesh. It is highly novel, timely and interesting as well as being well described and reproducible. I have only a few comments on what I found an interesting, if a little difficult to follow, analysis.

In the first part of the results it is shown that human movement is important for defining the network of parasite similarity. However in the second part, the authors use a genetic similarity index that only uses simple geographic distance. I understand that the authors want to propose a easily calculatable index, but it would be nice to see the best risk map possible for Bangladesh given the data available.

The big difference in coverage of travel survey and mobile phone data makes the assessment of their comparability / complementariness quite difficult to assess as a reader. While I appreciate there is not much the authors can do to change this, there are changes to the way the data are presented that could improve this, e.g. Figure 4 – would be easier to interpret differences between the two data sources if only areas for which both travel survey and mobile phone data were available. The discussion could also elaborate more on the implications of this disparity in coverage.

Given the huge amount of through work that has gone into this analysis, the final risk map (Figure 5D) is disappointingly non-specific. If resources were limited, what would be the suggestion about how best to use them? Can top importation routes be predicted, and how much of total importation would they account for?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Mapping imported malaria in Bangladesh using parasite genetic and human mobility data" for further consideration at eLife. Your revised article has been favorably evaluated by Neil Ferguson as the Senior and Reviewing Editor, and three reviewers.

The manuscript has been improved but two reviewers require some remaining issues to be addressed before acceptance, as outlined below.

I would also concur with reviewer 2 that the SNP positions need to be included in this paper or a citation given to a published source. A preprint on bioRxiv would suffice. However, if a preprint is not yet published, please include the positions here.

Reviewer #1:

Thanks to the authors for the welcome additions and responses to reviewer feedback.

A reiteration of the substantial concern that publishing SNP positions with genetic sequences is an integral part of the work, especially in a journal dedicated to "improv[ing] research communication through open science and open technology innovation".

Reviewer #2:

I am happy that the new version does a good job of addressing the initial concerns, and I appreciate the work done by the authors.

My only remaining concern is with the application of Bayes rule to obtain Prob (distance | similarity). First, I agree with the choice to swap Figures 3 and Figure 3—figure supplement 1. But the main text reads that there was "no prior" on geographic distance – there was a prior, it was uniform as stated in the Materials and methods section. It is impossible to apply Bayes rule without the use of a prior, and a uniform prior does not represent no information, it actually represents quite specific information. If the intention is to let the genetic data "speak" and not worry about the prior probability of edges being a certain distance then perhaps it would be better to report this as a raw likelihood, i.e. Prob (similarity | distance). Alternatively if the authors really want to stick with the inverted probability then this could be smoothed over with a statement to the effect of "a uniform prior allows the genetic data alone to speak, and more realistic priors can be incorporated by weighting based on the known sampling distances". At the moment it is unfortunately misleading, because the probability of a randomly chosen pair of samples being a given distance apart based on their genetic similarity almost certainly is not given by Figure 3—figure supplement 1.

Reviewer #3:

The reviewers have sufficiently addressed all my comments in this revision
