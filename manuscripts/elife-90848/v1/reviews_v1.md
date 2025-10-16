# Peer review - Round 1

Editors:
- Detlef Weigel, Max Planck Institute for Biology Tübingen Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.90848.3.sa0](https://doi.org/10.7554/eLife.90848.3.sa0)

This is a valuable study of the role that life history differences might play in determining population size and demography. While concerns about generation times and population structure leave the evidence for the claims in parts incomplete, the work is of considerable interest to anyone who tries to understand evolutionary consequences of life history changes.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90848.3.sa1](https://doi.org/10.7554/eLife.90848.3.sa1)

Summary:

This interesting study applies the PSMC model to a set of new genome sequences for migratory and nonmigratory thrushes and seeks to describe differences in the population size history among these groups. The authors create a set of summary statistics describing the PSMC traces - mean and standard deviation of Ne, plus a set of metrics describing the shape of the oldest Ne peak - and use these to compare across migratory and resident species (taking single samples sequenced here as representative of the species). The analyses are framed as supporting or refuting aspects of a biogeographic model describing colonization dynamics from tropical to temperate North and South America.

Strengths:

* This is a creative use of PSMC to test explicit a priori hypotheses about season migration and Ne. The PSMC analyses seem well done and the authors acknowledge much of the complexity of interpretation in the discussion.

* We appreciate the test-of-hypothesis design of the study and the explicit formulation of three main expectations to test. The data analysis has been done with appropriate available tools.

Key weaknesses from the original round of review:

* Short of developing some novel theory deep in the PSMC model, I think readers would need to see simulations showing that the analyses employed in this paper are capable of supporting or refuting their biogeographic hypothesis before viewing them as strongly supporting a specific biogeographic model. Tools like msprime and stdpopsim can be used to simulate genome-scale data with fairly complex biogeographic models. Running simulations of a thrush-like population under different biogeographic scenarios and then using PSMC to differentiate those patterns would be a more convincing argument for the biogeographic aspects of this paper. The other benefit of this approach would be to nail down a specific quantitative version of the taxon cycles model referenced in the abstract, and it would allow the authors to better study and explain the motivation behind the specific summary statistics they develop for PSMC posthoc analysis.

* The authors hypothesized that the wider realized breeding and ecological range characterising migrants versus resident lineages could be a major drive for increased effective population size and population expansion in migrants versus residents. I understand that this pattern (wider range in migrants) is a common characteristic across bird lineages and that it is viewed as a result of adapting to migration. A problem that I see in their dataset is that the breeding grounds range of the two groups are located in very different geographic areas (mainly South versus North America). The authors could have expanded their dataset to include species whose breeding grounds are from the two areas, regardless of their migratory behaviour, as a comparison to disentangle whether ecological differences of these two areas can affect the population sizes or growth rates.

* As I understand from previous literature, the time-scale to population growth and estimates of effective population sizes considered in the present paper for the resident versus migratory clades seem to widely predate the times to speciation for the same lineages, which were reported in previous work of the same authors (Everson et al 2019) and others (Termignoni-Garcia et al 2022). This piece of information makes the calculation of species-specific population size changes difficult to interpret in the light of lineages' comparison. It is unclear what the authors consider to be lineage-specific in these estimates, as the clades were likely undergoing substantial admixture during the time predating full isolation.

* Regarding the methodological difficulties in interpreting the impact of population structure on the estimates of effective population sizes with the PSMC approach, I would think that performing simulations to compare different scenarios of different degrees of structured populations would have helped substantially understand some of the outcomes.

* The authors use an average generation time for all taxa, but the citations imply generation time is known for at least some of them. Are there differences in generation time associated with migration? I am not a bird biologist, but quick googling suggests maybe this is the case? (https://doi.org/10.1111/1365-2656.13983). I think it important the authors address this, as differences in generation time I believe should affect estimates of Ne and growth.

[Editors' note: the original reviews in full are here: https://elifesciences.org/reviewed-preprints/90848/reviews. The reviewers were not available to comment on the latest version of the submission.]
