# Peer review - Round 1

Editors:
- Ziyue Gao, Columbia University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84874.3.sa0](https://doi.org/10.7554/eLife.84874.3.sa0)

This important paper reports recent improvements and extensions to stdpopsim, a community-driven resource that is built on top of powerful software for performing simulations of population genomic data and provides a catalog of species with curated genomic parameters and demographic models. In addition to describing the new features and species in stdpopsim, the authors provide a set of practical guidelines for implementing realistic simulations. Overall, this convincing manuscript serves as an excellent overview of the utility, challenges, common pitfalls, and best practices of population genomic simulations. It will be of broad interest to population, evolutionary, and ecological geneticists studying humans, model organisms, or non-model organisms.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.84874.3.sa1](https://doi.org/10.7554/eLife.84874.3.sa1)

stdpopsim is an existing, community-driven resource to support population genetics simulations across multiple species. This paper describes improvements and extensions to this resource and discusses various considerations of relevance to chromosome-scale evolutionary simulations. As such, the paper does not analyse data or present new results but rather serves as a general and useful guide for anyone interested in using the stdpopsim resource or in population genetics simulations in general.

Two new features in stdpopsim are described, which expand the types of evolutionary processes that can be simulated. First, the authors describe the addition of the ability to simulate non-crossover recombination events, i.e. gene conversion, in addition to standard crossover recombination. This will allow for simulations that come closer to the actual recombination processes occurring in many species. Second, the authors mention how genome annotations can now be incorporated into the simulations, to allow different processes to apply to different parts of the genome - however, the authors note that this addition will be further detailed in a separate, future publication. These additions to stdpopsim will certainly be useful to many users and represent a step forward in the degree of ambition for realistic population genetics simulations.

The paper also describes the expansion of the community-curated catalog of pre-defined, ready-to-use simulation set-ups for various species, from the previous 6 to 21 species (though not all new species have demographic models implemented, some have just population genetic parameters such as mutation rates and generation times). For each species, an attempt was made to implement parameters and simulations that are as realistic as possible with respect to what's known about the evolutionary history of that species, using only information that can be traced to the published literature. This process by which this was done appears quite rigorous and includes a quality-control process involving two people. Two examples are given, for Anopheles gambiae and Bos taurus. The detailed discussion of how various population genetic and demographic parameters were extracted from the literature for these two species usefully highlights the numerous non-trivial steps involved and showcases the great deal of care that underlies the stdpopsim resource.

The paper is clearly written and well-referenced, and I have no technical or conceptual concerns. The paper will be useful to anyone interested in population genetics simulations, and will hopefully serve as an inspiration for the broader effort of making simulations increasingly more realistic and flexible, while at the same time trying to make them accessible not just to a small number of experts.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.84874.3.sa2](https://doi.org/10.7554/eLife.84874.3.sa2)

Lauterbur et al. present a description of recent additions to the stdpopsim simulation software for generating whole-genome sequences under population genetic models, as well as detailed general guidelines and best practices for implementing realistic simulations within stdpopsim and other simulation software. Such realistic simulations are critical for understanding patterns in genetic variation expected under diverse processes for study organisms, training simulation-intensive models (e.g., machine learning and approximate Bayesian computation) to make predictions about factors shaping observed genetic variation, and for generating null distributions for testing hypotheses about evolutionary phenomena. However, realistic population genomic simulations can be challenging for those who have never implemented such models, particularly when different evolutionary parameters are taken from a variety of literature sources. Importantly, the goal of the authors is to expand the inclusivity of the field of population genomic simulation, by empowering investigators, regardless of model or non-model study system, to ultimately be able to effectively test hypotheses, make predictions, and learn about processes from simulated genomic variation. Continued expansion of the stdpopsim software is likely to have a significant impact on the evolutionary genomics community.

Strengths:

This work details an expansion from 6 to 21 species to gain a greater breadth of simulation capacity across the tree of life. Due to the nature of some of the species added, the authors implemented finite-site substitution models allowing for more than two allelic states at loci, permitting proper simulations of organisms with fast mutation rates, small genomes, or large effect sizes. Moreover, related to some of the newly added species, the authors incorporated a mechanism for simulating non-crossover recombination, such as gene conversion and horizontal gene transfer between individuals. The authors also added the ability to annotate and model coding genomic regions.

In addition to these added software features, the authors detail guidelines and best practices for implementing realistic population genetic simulations at the genome-scale, including encouraging and discussing the importance of code review, as well as highlighting the sufficient parameters for simulation: chromosome level assembly, mean mutation rate, mean recombination rate or recombination map if available, effective size or more realistic demographic model if available, and mean generation time. Much of these best practices are commonly followed by population genetic modelers, but new researchers in the field seeking to simulate data under population genetic models may be unfamiliar with these practices, making their clear enumeration (as done in this work) highly valuable for a broad audience. Moreover, the mechanisms for dealing with issues of missing parameters discussed in this work are particularly useful, as more often than not, estimates of certain model parameters may not be readily available from the literature for a given study system.

Weaknesses:

An important update to the stdpopsim software is the capacity for researchers to annotate coding regions of the genome, permitting distributions of fitness effects and linked selection to be modeled. However, though this novel feature expands the breadth of processes that can be evaluated as well as is applicable to all species within the stdpopsim framework, the authors do not provide significant detail regarding this feature, stating that they will provide more details about it in a forthcoming publication. Compared to this feature, the additions of extra species, finite-site substitution models, and non-crossover recombination are more specialized updates to the software.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.84874.3.sa3](https://doi.org/10.7554/eLife.84874.3.sa3)

Lauterbur et al. present an expansion of the whole-genome evolution simulation software "stdpopsim", which includes new features of the simulator itself, and 15 new species in their catalog of demographic models and genetic parameters (which previously had 6 species). The list of new species includes mostly animals (12), but also one species of plant, one of algae, and one of bacteria. While only five of the new animal species (and none of the other organisms) have a demographic model described in the catalog, those species showcase a variety of demographic models (e.g. extreme inbreeding of cattle). The authors describe in detail how to go about gathering genetic and demographic parameters from the literature, which is helpful for others aiming to add new species and demographic models to the stdpopsim catalog. This part of the paper is the most widely relevant not only for stdpopsim users but for any researcher performing population genomics simulations. This work is a concrete contribution towards increasing the number of users of population genomic simulations and improving reproducibility in research that uses this type of simulations.
