# Peer review - Round 1

Editors:
- Richard A Neher, University of Basel Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62719.sa1](https://doi.org/10.7554/eLife.62719.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Sheinman and colleagues investigate long stretches of identical sequences found in genome assemblies of bacteria across genera. They show that such shared identical sequence fragments exist even between evolutionarily very distant species and that the length distribution of these stretches follows a universal form given by an inverse third power. This dependence can be explained by a model assuming that identical stretches originating from horizontally transferred segments are broken up into smaller fragments by point mutations. This original approach to an important topic in bacterial evolution has to potential to shed new light on prokaryotic diversity.

Decision letter after peer review:

Thank you for submitting your article "Identical sequences found in distant genomes reveal frequent horizontal transfer across the bacterial domain" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Richard A Neher as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Gisela Storz as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional analyses are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option.

Summary:

Sheinman and colleagues investigate long stretches of identical sequences found in genome assemblies of bacteria across genera. They show that such shared identical sequence fragments exist even between evolutionarily very distant species and that the length distribution of these stretches follows a universal form given by an inverse third power. This dependence can be explained by a model assuming that identical stretches originating from horizontally transferred segments are broken up into smaller fragments by point mutations. The inferred rate of exchange shows systematic patterns and is higher between taxonomically closer species.

Essential revisions:

All reviewers agreed that this manuscript presents an interesting and original approach to an important topic in bacterial evolution, but raised a number of concerns regarding the robustness of the results that need to be addressed and suggested how the presentation of the results could be improved.

1) Robustness to phylogenetic correlations and biased sampling. A heavily sampled species might contain many vertically inherited identical stretches that will be compared to each other and to a potential horizontal transfer in a different species. Such correlations and oversampling can therefore inflate the estimated transfers. It is hence critical that the authors investigate and discuss how their conclusions depend on phylogenetic relationships, diversity, and sampling density in their data set.

2) Plasmids and assembly artefacts: The manuscript contains a brief section on a restricted data set encompassing only contigs longer than 1 Mb to effectively exclude plasmids and misassigned short contigs. In this data set, the authors also find long-distance HGT. But it remains unclear whether the statistical patterns described for the full data set are consistent with this smaller data set. We would like to see a quantitative assessment of the contribution of plasmids and assembly artefacts. Furthermore, you seem to sometimes find identical sequences fragments longer then 300 kb shared between distant species. These should be spot-checked.

3) The enrichment analysis for functional categories should be done more systematically. It is by now routine to assign genes in genomes to Gene Ontology categories (e.g. using Interpro or Pfam) in a systematic manner, which would give statistics for all gene ontology categories.

4) The 1/r3 dependence of match length distribution is central part of the analysis and needs to be better explained. Currently, it is left to reader to go through the math in the methods section, look up the reference, and develop an intuition for the behavior. A discussion (and possibly illustration) of the process through which the 1/r3 distribution emerges would make the manuscript much more self-contained and help the reader to assess the robustness of the conclusions.

Reviewer #2:

I just have one main comment. This calculation of the probability of obtaining the exact DNA match in a pair of genomes (lines 46-48) obviously does not account for selection. If we are dealing with a highly conserved genetic region (eg, a ribosomal RNA protein), the chances of observing an identical DNA fragment are going to be much higher different. According to my rough calculations, they should be of the order of 1e-10, hence it still shouldn't really affect the results, but it took me a while to come to this conclusion. I would ask the authors to make it more explicit in the article why the trick of looking at exact matches overcomes this problem.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Identical sequences found in distant genomes reveal frequent horizontal transfer across the bacterial domain" for further consideration by eLife. Your revised article has been evaluated by Gisela Storz (Senior Editor) and a Reviewing Editor.

The manuscript has been improved and you have addressed most concerns the were raised in the review but there are some remaining issues that need to be addressed, as outlined below:

1) Please explain the abbreviations G/F, F/O etc.

2) The methods need more documentation. You provide a single matlab script without comments and hard coded paths that only covers a fraction of the analysis. This is not an acceptable standard of reproducibility for a computational biology paper.

– What are the exact options Mummer was run with? On what set of genomes?

– Scripts need commenting and explanation what input they take and what output they produce.

– Enrichment analysis use a number of tools, but no details are given how exactly they are run and how the output is processed into the figures and tables in the manuscript.
