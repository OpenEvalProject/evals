# Peer review - Round 1

Editors:
- Armita Nourmohammad, University of Washington United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56915.sa1](https://doi.org/10.7554/eLife.56915.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The manuscript assesses the intra-host effective population size of influenza based on longitudinal deep sequencing data from a chronic influenza B infection. Using principles modeling and statistical approaches, the authors show that the short length of a typical influenza infection is the key limiting factor upon selection at the within-host level. The topic is important, as it sheds light on the interplay between the two scales of selection within- and between-host in shaping the evolution of influenza virus.

Decision letter after peer review:

Thank you for submitting your article "A large effective population size for within-host influenza virus infection" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Georgii A. Bazykin (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

The manuscript presents a study on within-host population genetics of influenza virus and in particular, inference of effective population size during chronic infection in immunocompromised patients. The topic is important as it explores the interplay between the two scales of selection: within-host and between-host selection that shape the evolution of influenza. Based on the analysis of sequence polymorphism, authors infer a relatively large effective population size ~107 during chronic infection, in contrast to previously inferred values of ~102 or less during transmission and in acute infections. All of the reviewers agree that the findings in this manuscript are interesting and a large effective population would have significant implications for efficacy of selection during within-host evolution of influenza. However, there are still some concerns regarding methodology, interpretation and presentation of the results which we would like to see addressed.

Essential revisions:

1) Comparison between chronic and acute infections:

The authors analyzed data from chronic influenza infections and concluded that the effective population size of the virus is high, including during acute infections. For instance, the authors argue that "the observed lack of within-host variation in typical cases of influenza can be explained by the short period of infection; the stochastic effects of genetic drift do not limit the impact of positive selection". It is however not evident that the authors' estimates of effective population size from chronic infections apply to acute infections given the exponential increase and decrease of viral load that dominate the course of acute infections. In fact, it's not clear that effective population size is even a very useful concept in this case.

Also, McCrone et al., 2018, and Xue and Bloom, 2020, have both shown that within-host variation in acute infections is dominated by non-synonymous mutations, and Xue and Bloom, 2020, also document stop-codon mutations within acute infections that are rarely found at appreciable frequencies in chronic infections. These observations suggest that selection is inefficient within hosts in acute infections, contrary to the authors' claims.

Moreover, McCrone et al. see radical changes in variant frequencies over the course of a few days (Figure 2E in that work) – but lineages in chronic infections (this work) persist for many months. If the authors think that Ne is comparable between acute and chronic infections, how do they explain the lack of diversity observed in acute infections? One way to explain this is to maintain a high Ne but with strong transmission bottleneck to impose stochasticity. But as point out above, "Ne" is really not a well-defined quantity in this case. Alternatively, could the difference imply a lower census size in acute infections, and if so, is this consistent with differences in viral load? This issue is important in view of the proposed relevance of high Ne for long-term influenza evolution (e.g., last phrase of the Abstract and the last phrase of the Introduction).

Overall, the authors should acknowledge the differences between acute and chronic infections, and discuss their estimates in light of the previous observations. Moreover, it may also be helpful to revise the title to indicate that the manuscript focuses on chronic infections.

2) High Ne is inferred from small drift and a small rate of "substitutions" (which under the authors' terminology also account for minor changes in allele frequencies). In other words, the authors are inferring a large Ne based on the longer-term coexistence of multiple lineages within a host. Therefore, it would be important that the manuscript also discusses alternative explanations that could lead to such patterns of polymorphism. Importantly, as Ne in the manuscript is inferred from a Wright-Fisher (WF) model, violations in the underlying assumptions of the model can bias the results. For example, one can imagine that demographic effects like population structure could be responsible for long-term coexistence and survival of lineages, e.g., if each of the samples represents a mixture of persistent subpopulations? The authors seem to suggest this by analyzing clades A and B separately, Results and Discussion, second paragraph. Alternatively, could balancing selection in the host be responsible for maintaining this polymorphism (seems unlikely, but still a formal possibility)? A discussion and/or analysis of such alternative scenarios would be useful in assessing the robustness of the manuscript's findings.

3) Robustness of the analysis and proposed statistics:

a) It would be useful to have a clearer sense of the sensitivity of Ne to the cutoffs used. While a lot of care has gone into the choice, some diagrams showing the sensitivity of Ne to cutoff choice would better demonstrate the degree to which it is a function of low frequency variants in a straightforward way.

b) To estimate how Ne affects changes in allele frequencies, the authors simulate a single generation of Wright-Fisher evolution using initial allele frequencies from a randomly selected sample from the infection. As the equation in the subsection “Summary” indicates, populations with high-frequency alleles will experience larger changes in allele frequency at a given effective population size, so the initial distribution of allele frequencies from this randomly chosen sample can have a major effect on the expected change in allele frequencies. The authors show in Figure 2—figure supplement 1 that mutations can reach frequencies of 20-30% in neuraminidase, and in the influenza A patients analyzed in Figure 2—figure supplement 3, many mutations reach these and even higher frequencies, particularly at later points in the infection. The authors should run their Wright-Fisher simulations with different initial allele frequencies to evaluate how this choice of allele frequencies may affect estimates of effective population size.

c) The authors design statistic D to assess their estimation of Ne. This statistic is a sum of changes in variant frequencies across sites (subsection “Calculation of evolutionary rates”), which is then compared between data and Wright-Fisher simulations for different Ne values. The authors seem to suggest that D should be more robust to noise (subsection “Summary”), without providing any evidence. In particular, the authors should clearly state how the assumptions they made about recombination structure in WF simulation could impact the statistics D and the interpretation of the inferred Ne. From the manuscript it is not clear whether WF simulations are done at the site-wise, segment-wise, or genome-wise level, which would impact the correlation between changes in variant frequencies. For example, simulations done with high (free) recombination would expect a lower variance D compared to the case with strong linkage (data), for the same Ne. These points should be better clarified.

4) In Figure 1A, it is clear (and the authors also mention) that the patient's viral load drops to undetectable levels for over a month of the infection, and viral load also varies substantially while the patient is continually infected. Effective population size and census population size are not always directly related, but the authors should discuss how changing population sizes affect their estimate of effective population size and whether a single effective population size is adequate to represent the infection.

5) The authors calculate sequence distance between every pair of sequenced timepoints to reduce the influence of noise from sequencing error, but as a result, the points in Figure 2A are non-independent and may contribute to a tighter confidence interval around the evolutionary rate than is realistic. In particular, changes in variant frequencies that take place during the middle of the infection will be overcounted in these pairs and will disproportionately influence the overall estimate of evolutionary rates. When the authors estimate the evolutionary distance between consecutive timepoints and divide by the number of days between them, how well does the estimate correspond to the estimates in Figure 2? What is the variance in these estimates?

6) The regression performed in Figure 2A, C, and analogous figures may be especially influenced by the few points at the right end of the distribution, which represent evolutionary distances between points spaced further apart in time. How robust is the estimate of evolutionary rate to removal of these points, or by calculation of evolutionary rate as suggested in comment 4?

7) The authors chose to infer effective population size using variants and haplotypes on the neuraminidase and hemagglutinin segments. This is an odd choice since these regions tend to experience the strongest selection, which can strongly influence the estimates of effective population size. Selection can act on linked haplotypes across the genome in some cases, but have the authors tested to see if these results hold for other gene segments as well?

8) Why are the effective population size estimates for the clade B samples calculated separately from the clade A samples? It's not evident from the SAMFIRE inference of haplotypes that clades A and B constitute separate subpopulations; it seems that they could be distinct genotypes in a well-mixed population as well, as might result from a coinfection.

9) The authors assume the generation time of 10 hours per generation for influenza B. However, if generations are longer in immunocompromised individuals, the analysis would lead to an overestimation of Ne. Given that the main result in this manuscript is that Ne is high, this possibility should at least be discussed.
