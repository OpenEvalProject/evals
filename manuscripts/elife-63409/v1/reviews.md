# Peer review - Round 1

Editors:
- Jesse D Bloom, Fred Hutchinson Cancer Research Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63409.sa1](https://doi.org/10.7554/eLife.63409.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This publication describes covidcg.org, which is a useful interface for tracking and visualizing mutations that have appeared in sequenced SARS-CoV-2 isolates. It provides complementary functionality to a variety of other interfaces, and together these platforms aid in the important task of tracking the emergence and potential impacts of mutations in SARS-CoV-2.

Decision letter after peer review:

Thank you for submitting your article "COVID-19 CG enables SARS-CoV-2 mutation and lineage tracking by locations and dates of interest" for consideration by eLife. Your article has been reviewed by two peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Miles Davenport as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

Devermen and colleagues describe COVID-19 CG, a resource for information on SARS-CoV-2 data. They present several use cases demonstrating the utility of this resource. Given the nature of the pandemic, integration of datasets in easy to find and analyzable formats are of significant importance. While many other tools provide similar functionalities, covidcg is clearly useful to researchers and likely easier to use and more intuitive in specific use cases. Indeed, we note that one of us has made use of it for the specific purpose of tracking mutations by geographic location.

Essential revisions:

We had the following suggestions that we think you should find easy to address in a revised version:

The current interface / setup seems designed for the situation when there are relatively few mutation (e.g., you get a list of all mutations in a region and click on mutation of interest). This seems like it will become increasingly unwieldy as more and more mutations reach appreciable frequencies as the virus evolves. What is the plan to deal with this? Some mention of this point might be helpful in the Discussion.

The Abstract should have a link to the website: https://covidcg.org. This will make the resource easier to find and allow users to interact with it while reading the paper.

The authors should note many of the existing sequence resources available including: the UCSC SARS-CoV-2 browser (https://genome.ucsc.edu/covid19.html) , the Wash U Genome browser (https://virusgateway.wustl.edu/), Nextstrain (https://nextstrain.org/) as well as the COG-UK efforts (https://www.cogconsortium.uk/, including CoV-GLUE and Pangolin which is cited, but only in the Materials and methods). These other tools are not competitors but rather complementary and researchers should be encouraged to use the tool that is easiest for them to use and makes the most sense for a specific analysis. Thus "cannot be found in other public browsers" should be reworded.

Suggested citations:

https://www.nature.com/articles/s41588-020-0700-8

https://www.nature.com/articles/s41588-020-0697-z

https://europepmc.org/article/ppr/ppr177298

https://academic.oup.com/bioinformatics/article/34/23/4121/5001388

Related to the above point, overall this is a useful resource, but the authors should be clear that many other resources are available and that the scientific community should use the best tools for a particular task to combat this pandemic. In that respect, any additional discussion weighing the strengths and uses of various above resources would probably be useful.

With regard to the mutations that might disrupt primer binding sites the authors should compare them to problematic/masked sites that are almost certainly due to sequencing/assembly error (e.g. within ARCTIC primers) as they do not obey expected evolutionary patterns. A full list has been collected by the community here: https://github.com/W-L/ProblematicSites_SARS-CoV2/ and is discussed in this paper (https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1009175); see also here (https://virological.org/t/issues-with-sars-cov-2-sequencing-data/473/14). The authors should, in addition to their recommendation that scientists check mutation rates at primer binding sites, also reiterate Vanaerschot et al.'s suggestion to interrogate multiple target genes and compare Ct values.

Subsection “Case study of SNVs in the receptor binding domain (RBD) of the SARS-CoV-2 Spike”: Although Baum et al. identified mutations by deep sequencing both in and out of the RBD, they only validated that mutations in the RBD affected binding by Regeneron antibodies. The others are likely hitchhikers, and should not be referred to as possible escape mutants in the absence of direct functional testing
