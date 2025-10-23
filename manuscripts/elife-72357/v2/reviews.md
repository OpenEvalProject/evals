# Peer review - Round 1

Editors:
- Belinda Nicolau, McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72357.sa0](https://doi.org/10.7554/eLife.72357.sa0)

Using data from the 1970 British Birth Cohort study, the authors demonstrated the utility of Generalized Additive Models for Location, Scale and Shape (GAMLSS) to investigate the association of three risk factors (sex, socioeconomic circumstances, and physical inactivity) with body mass index and mental wellbeing. This work provides empirical evidence for why we should consider how risk factors influence the variability and not just the mean of outcomes. From the perspective of developing personalized medicine, it is important to know whether interventions have response heterogeneity as the first step. If such heterogeneity is identified, the next step will be to identify the factors associated with the heterogeneity (or those who will be benefitted from the intervention). Therefore, this study contributes to the first step by investigating the possibility of response heterogeneity.


---

# Peer review - Round 1

Editors:
- Belinda Nicolau, McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72357.sa1](https://doi.org/10.7554/eLife.72357.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Risk factors relate to the variability of health outcomes as well as the mean" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Carmen Tekwe (Reviewer #3).

As is customary in eLife, the reviewers have discussed their critiques with one another. What follows below is the Reviewing Editor's edited compilation of the essential and ancillary points provided by reviewers in their critiques and in their interaction post-review. Please submit a revised version that addresses these concerns directly. Although we expect that you will address these comments in your response letter, we also need to see the corresponding revision clearly marked in the text of the manuscript. Some of the reviewers' comments may seem to be simple queries or challenges that do not prompt revisions to the text. Please keep in mind, however, that readers may have the same perspective as the reviewers. Therefore, it is essential that you attempt to amend or expand the text to clarify the narrative accordingly.

Essential revisions:

The authors claim that the primary aim of this work is "exploring factors affecting outcome variability in an epidemiological context." This aim seems to be very broad, and it is unclear how one would address this aim in a single manuscript. We suggest defining the aims of the manuscript clearly in terms of the objectives the authors want to achieve. For instance, what would the audience gain by reading the manuscript (objective of a tutorial type of manuscript)? Or what is the research question the authors aim to investigate (objective of a non-tutorial type of manuscript)?

In the field of epidemiology, it is well understood that an exposure may change different parameters of the outcome distribution in the population (1). For example, a population intervention focusing only on a high-risk group would increase the right skewness of the outcome distribution in that population after implementation. Further, it is unclear how using a model that already assumes that independent variables may affect the variability of the outcome (by parameterizing this relationship) can alone provide empirical support for the that notion. Instead, having used such a model, the authors could report on the effect estimates of the risk factor on the variability of the outcome measures. In other words, more clarity is needed regarding the takeaway message of the manuscript.

We suggest that the authors make this manuscript a tutorial; if they agree with our suggestion, the following additions would considerably improve the manuscript:

i) Clearly annotated R and Stata codes to replicate the analysis. This would provide potential users of the proposed technique t with hands-on exercise.

ii) Clear examples of interpretation within epidemiological context. For example, how should one interpret the percentage point difference in SD and the uncertainty around it?

iii) Comparison between the results of GAMLSS and a technique that does not model the variance and further elaboration on the advantages of fitting this complex model over a simple model.

iv) Explanations answering the following questions: What do we learn from comparing the descriptive kernel density estimates to the unadjusted estimates? Are they supposed to be very similar? If yes, why?

v) Discussions on or recommendation for addressing the on challenges in choosing the type of outcome distribution in GAMLSS within epidemiological context.

(1) Rose G. Sick individuals and sick populations. Int J Epidemiol. 2001 Jun 1;30(3):427-32.
