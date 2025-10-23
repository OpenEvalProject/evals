# Peer review - Round 1

Editors:
- Antonis Rokas, Vanderbilt University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.90656.3.sa0](https://doi.org/10.7554/eLife.90656.3.sa0)

This important study revises the evolutionary history of Heliconius butterflies, a well-established model system for understanding speciation in the presence of gene flow between species. Using a convincing statistical phylogenetic approach that relies on the multispecies coalescent, the authors reconstruct the evolution of the lineage, including the timing of speciation events and the history of gene flow. The new phylogeny will be of interest to all researchers working on Heliconius butterflies, and the phylogenetic approach to investigators aiming to understand the history of lineages that have experienced extensive gene flow.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90656.3.sa1](https://doi.org/10.7554/eLife.90656.3.sa1)

Summary:

This study aims to further resolve the history of speciation and introgression in Heliconius butterflies. The authors break the data into various partitions and test evolutionary hypotheses using the Bayesian software BPP, which is based on the multispecies coalescent model with introgression. By synthesizing these various analyses, the study pieces together an updated history of Heliconius, including a multitude of introgression events and the sharing of chromosomal inversions.

Strengths:

Full-likelihood methods for estimating introgression can be very computationally expensive, making them challenging to apply to datasets containing many species. This study provides a great example of how to apply these approaches by breaking the data down into a series of smaller inference problems and then piecing the results together. On the empirical side, it further resolves the history of a genus with a famously complex history of speciation and introgression, continuing its role as a great model system for studying the evolutionary consequences of introgression. This is highlighted by a nice Discussion section on the implications of the paper's findings for the evolution of pollen feeding.

Weaknesses:

The analyses in this study make use of a single method, BPP. The analyses are quite thorough so this is okay in my view from a methodological standpoint, but given this singularity, more attention should be paid to the weaknesses of this particular approach. Additionally, little attention is paid to comparable methods such as PhyloNet and their strengths and weaknesses in the Introduction or Discussion. BPP reduces computational burden by fixing certain aspects of the parameter space, such as the species tree topology or set of proposed introgression events. While this approach is statistically powerful, it requires users to make informed choices about which models to test, and these choices can have downstream consequences for subsequent analyses. It also might not be as applicable to systems outside of Heliconius where less previous information is available about the history of speciation and introgression. In general, it is likely that most modelling decisions made in the study are justified, but more attention should be paid to how these decisions are made and what the consequences of them could be, including alternative models.

• Co-estimating histories of speciation and introgression remains computationally challenging. To circumvent this in the study, the authors first estimate the history of speciation assuming no gene flow in BPP. While this approach should be robust to incomplete lineage sorting and gene tree estimation, it is still vulnerable to gene flow. This could result in a circular problem where gene flow causes the wrong species tree to be estimated, causing the true species tree to be estimated as a gene flow event. This is a flaw that this approach shares with summary-statistic approaches like the D-statistic, which also require an a-priori species tree. Enrichment of particular topologies on the Z chromosome helps resolve the true history in this particular case, but not all datasets will have sex chromosomes or chromosome-level assemblies to test against.

• The a-priori specification of network models necessarily means that potentially better-fitting models to the data don't get explored. Models containing introgression events are proposed here based on parsimony to explain patterns in gene tree frequencies. This is a reasonable and common assumption, but parsimony is not always the best explanation for a dataset, as we often see with phylogenetic inference. In general, there are no rigorous approaches to estimating the best-fitting number of introgression events in a dataset. Likewise, the study estimates both pulse and continuous introgression models for certain partitions, though there is no rigorous way to assess which of these describes the data better.

• Some aspects of the analyses involving inversions warrant additional consideration. Fewer loci were able to be identified in inverted regions, and such regions also often have reduced rates of recombination. I wonder if this might make inferences of the history of inverted regions vulnerable to the effects of incomplete lineage sorting, even when fitting the MSC model, due to a small # of truly genealogically independent loci. Additionally, there are several models where introgression events are proposed to explain the loss of segregating inversions in certain species. It is not clear why these scenarios should be proposed over those in which the inversion is lost simply due to drift or selection.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90656.3.sa2](https://doi.org/10.7554/eLife.90656.3.sa2)

Thawornwattana et al. reconstruct a species tree of the genus Heliconius using the full-likelihood multispecies coalescent, an exciting approach for genera with a history of extensive gene flow and introgression. With this, they obtain a species tree with H. aoede as the earliest diverging lineage, in sync with ecological and morphological characters. They also add resolution to the species relationships of the melpomene-silvaniform clade and quantify introgression events. Finally, they trace the origins of an inversion on chromosome 15 that exists as a polymorphism in H. numata, but is fixed in other species. Overall, obtaining better species tree resolutions and estimates of gene flow in groups with extensive histories of hybridization and introgression is an exciting avenue. Being able to control for ILS and get estimates between sister species are excellent perks. One overall quibble is that the paper seems to be best suited to a Heliconius audience, where past trees are easily recalled, or members of the different clades are well known.

Overall, applying approaches such as these to gain greater insight into species relationships with extensive gene flow could be of interest to many researchers.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90656.3.sa3](https://doi.org/10.7554/eLife.90656.3.sa3)

The authors use a full-likelihood multispecies coalescent (MSC) approach to identify major introgression events throughout the radiation of Heliconius butterflies, thereby improving estimates of the phylogeny. First, the authors conclude that H. aoede is the likely outgroup relative to other Heliconius species; miocene introgression into the ancestor of H. aoede makes it appear to branch later. Topologies at most loci were not concordant with this scenario, though 'aoede-early' topologies were enriched in regions of the genome where interspecific introgression is expected to be reduced: the Z chromosome and larger autosomes. The revised phylogeny is interesting because it would mean that no extant Heliconius species has reverted to a non-pollen-feeding ancestral state. Second, the authors focus on a particularly challenging clade in which ancient and ongoing gene flow is extensive, concluding that silvaniform species are not monophyletic. Building on these results, a third set of analyses investigates the origin of the P1 inversion, which harbours multiple wing patterning loci, and which is maintained as a balanced polymorphism in H. numata. The authors present data supporting a new scenario in which P1 arises in H. numata or its ancestor and is introduced to the ancestor of H. pardilinus and H. elevatus - introgression in the opposite direction to what has previously been proposed using a smaller set of taxa and different methods.

The analyses were extensive and methodologically sound. Care was taken to control for potential sources of error arising from incorrect genotype calls and the choice of a reference genome. The argument for H. aoede as the earliest-diverging Heliconius lineage was compelling, and analyses of the melpomene-silvaniform clade were thorough.

The authors have demonstrated the strengths of a full-likelihood MSC approach when reconstructing the evolutionary history of "difficult" clade. This approach, however, can quickly become intractable in large species complexes where there is extensive gene flow or significant shifts in population size. In such cases, there may be hundreds of potentially important parameters to estimate, and alternate introgression scenarios may be impossible to disentangle. This is particularly challenging in systems unlike Heliconius, where fewer data are available and there is little a priori knowledge of reproductive isolation, genome evolution, and the unique life history traits of each species.
