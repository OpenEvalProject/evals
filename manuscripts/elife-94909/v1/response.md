# Author response - Round 1

Authors:
- Jérome Dockès ([ORCID: 0000-0002-5304-2496](https://orcid.org/0000-0002-5304-2496))
- Kendra M Oudyk ([ORCID: 0000-0003-4087-5402](https://orcid.org/0000-0003-4087-5402))
- Mohammad Torabi ([ORCID: 0000-0002-4429-8481](https://orcid.org/0000-0002-4429-8481))
- Alejandro I de la Vega ([ORCID: 0000-0001-9062-3778](https://orcid.org/0000-0001-9062-3778))
- Jean-Baptiste Poline ([ORCID: 0000-0002-9794-749X](https://orcid.org/0000-0002-9794-749X))

## Response text

DOI: [10.7554/eLife.94909.2.sa4](https://doi.org/10.7554/eLife.94909.2.sa4)

Thank you for the reviews and the eLife assessment. We want to take this opportunity to acknowledge the weaknesses pointed out by the reviewers and we will make small changes to the manuscript to account for these as part of the Version of Record.

The tools are command-based and store outcomes locally

We consider this to be an advantage of our ecosystem, which is intended for the case of individuals or small groups of authors. These features facilitate easy installation and integration with other tools. Further, our tool labelbuddy is a graphic user interface. Our tools may also be integrated into web-based systems as backends. Pubget is already being used in this way in the NeuroSynth Compose platform for semi-automated neuroimaging meta-analyses.

pubget only gathers open-access papers from PubMed Central

We recognize this as a limitation, and we acknowledge it in the original manuscript (in the discussion section, starting with "A limitation of Pubget is that it is restricted to the Open-Access subset of PMC"). We chose to limit the scope of our tools in order to ensure maintainability. Further, we are currently expanding pubget so it will also be able to access the abstracts and meta-data from closed-access papers indexed on PubMed. Future research could build other tools to work alongside pubget, to access other databases.

Logic flow is difficult to follow

We thank the reviewer for this feedback. Our paper describes an ecosystem of literature mining tools which does not lend itself to narrative flow nor does readily fit into the standard "Intro, Results, Discussion, Methods" structure that is typical in the scientific literature. We have done our best to conform to this expected format, but we have also provided detailed section and subsection headings to enable the reader to digest the paper nonlinearly. Each of the tools we describe also has detailed documentation on github that we update continuously.

Results were not validated

For the example where we automatically extracted participant demographics from papers, we validated the results on a held-out dataset of 100 manually-annotated papers. For the example with automatic large-scale meta-analyses (neuroquery and neurosynth), these methods are described together with their validation in the original papers. If this ecosystem of tools is integrated into other workflows, it should be validated in those contexts. We recognize that validating meta-analyses is a difficult problem because we do not have ground truth maps of the brain.

Efficiency was not quantified

Creators of tools do not always do experiments to quantify their efficiency and other qualities. We have chosen not to do this here, first because it is outside the scope of this paper as it would necessitate to specify very precise tasks and how efficiency is measured, and second because at least for the data collection part, the benefit of using an automated tool over manually downloading papers one by one is clear even without quantifying it. Compared to the approach of re-using existing datasets, our ecosystem is not necessarily more or less efficient. But it has other advantages, such as providing datasets that contain the latest literature, whereas the existing datasets are static and quickly out-of-date.

We do not highlight the strength of AI functions

We provide an example of using our tools to gather data and manually annotate a validation set for use with large language models (in our case, GPT). We are further exploring this domain in other projects; for example, for performing semi-automated meta-analyses using the NeuroSynth Compose platform. However, we did not deem it necessary to include more AI examples in the current paper; we only wanted to provide enough examples to demonstrate the scope of possible use cases of our ecosystem.

We thank the reviewers for their time and valuable feedback, which we will keep in mind in our future research.
