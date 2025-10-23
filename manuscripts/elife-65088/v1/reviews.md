# Peer review - Round 1

Editors:
- Peter Turnbaugh, University of California, San Francisco United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65088.sa1](https://doi.org/10.7554/eLife.65088.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Beghini and co-authors here present bioBakery 3, a platform that integrates a number of software tools for carrying out taxonomic and functional profiling of microbial communities from a wide range of environments. Together, these tools will accelerate microbiome research and be of broad utility to researchers across many fields.

Decision letter after peer review:

Thank you for submitting your article "Integrating taxonomic, functional, and strain-level profiling of diverse microbial communities with bioBakery 3" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: C Titus Brown (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

Beghini and co-authors here present bioBakery 3, a platform that integrates a number of software tools for carrying out taxonomic and functional profiling of microbiota from a wide range of environments. These tools are already well-established in the community, some even with their third versions publicly available. The authors describe updates to ChocoPhlan, MetaPhlan, HUMAnN, PhyloPhlan, StrainPhlan and PanPhlan, which all carry out specific tasks for analysing shotgun metagenome and metatranscriptome data. Perhaps the most significant improvement is related to a significantly updated database of reference sequences (ChocoPhlan), although algorithmic updates also allow for faster read mapping. It would be useful with more information on to what degree the updated database is responsible for the improved performance, and whether users are able to update this themselves.

The (many) benchmarking results and data analyses presented are of high caliber. For example, MetaPhlAn3 and HUMAnN are benchmarked using the state-of-the-art CAMI and perform well. We also applaud the inclusion of memory and CPU time numbers in the results.

The utility and versatility of the bioBakery tools is further demonstrated by deeper investigations into CRC and IBD metagenomes/transcriptomes, identifying a comparatively large number of potentially disease-associated taxa and genes, respectively. These include not previously reported oral species and TMA-producing genes that may be linked to CRC. Further studies based on complementary datasets and methodologies will be needed to confirm these.

Overall, the comparative tests and methodology descriptions are well described and supported by submitted data. The bioBakery 3 updates should improve meta-omic analysis and become a very useful resource for microbiome studies of a wide range of environments.

Essential revisions:

This seems like an excellent software package that could be further improved through the following additions:

1. The validation looks impressive but is unfortunately qualitative throughout. I would like to see the appropriate statistics included for all of the relevant contrasts (e.g., Figures 1b-d, Pg. 12 final paragraph, etc.) used to validate these methods throughout the manuscript.

2. It remains unclear why the performance of these different tools has been improved. Multiple ideas are mentioned in the text, including a more extensive database, improvements to parts of the algorithms, etc. The paper and field would benefit from a more targeted analysis to test what aspect of the update mattered most or alternatively if the improved performance is the aggregate result of a lot of little changes. At a minimum, it seems important to test how much these improvements are due to the expanded database as opposed to the tool itself. Could you get the same result with the version 2 tools and the up-to-date set of [meta]genomes?

MetaPhlan 3 has clearly improved precision compared to the 2nd versions. It would be useful to know to what degree this is solely due to the updated ChocoPhlan database. A couple of algorithm improvements are mentioned. This would be possible with the introduction of "Metaphlan 3 with db 2 (or 2.7) ", at least in a subset of the comparisons in displayed in Figure 1? This should answer what role the algorithmic improvements played.

3. The figures and legends could use some polishing to enable clarity. For example, Figure 1d shows multiple bars/box plots, but it's unclear what they represent due to the lack of x axis labels. Figure 2a includes lots of different colors indicating study that are impossible to distinguish due to the massive number of red samples, the legend to Figure 2c is missing, and the countries in Figure 4a are impossible to see any pattern.

4. The use cases of these updated tools are underwhelming and not clearly compared to the prior literature. The CRC analysis shown in Figure 2 highlight multiple bacterial species, one α diversity metric, and one gene (cutC) distinct from the healthy controls in this meta-analysis. It remains unclear which of these findings are new and if they are new, whether or not the new findings are better or worse than what was previously published. Similar issues affect the re-analysis of the IBD data (Figure 3) and the pan-genome data (Figure 4). While these figures provide a nice example of the analyses that can be done, it's unclear if anything new has been learned and if bioBakery 3 was necessary to run these analyses. These analyses also take up the majority of the main figures (3 out of 4), distracting from the main goal of the paper, which is to explain the improvements that have been made and to compare these updated tools to their previous versions.
