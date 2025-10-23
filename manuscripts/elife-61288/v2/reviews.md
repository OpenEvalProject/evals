# Peer review - Round 1

Editors:
- Andreas Buttenschoen, University of British Columbia Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61288.sa1](https://doi.org/10.7554/eLife.61288.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This well written paper presents Artistoo, a software package allowing tissue simulations using the Cellular Potts framework, that fills an interesting niche: interactive, real-time simulations of complex multicellular systems that can run in a web browser, without any need for users to install or configure software. This enables new modes of education, science communication, research and multidisciplinary collaboration. This fully open-source software is impressive, and the supplied examples and tutorials are clean and beautifully fluid. The work should be of considerable interest to the eLife readership, particularly computational biologists and educators. The addition of markup language support both Morpheus to Artistoo and vice versa is fantastic. This will undoubtedly increase the adoption of Artistoo by the community. This is to my knowledge the first example of standardization across open-source CPM software packages.

Decision letter after peer review:

Thank you for submitting your article "Artistoo: build, share, and explore simulations of cells and tissues in the web browser" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Paul Macklin (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our policy on revisions we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

This is a well written paper that presents a software allowing tissue modelling using the Cellular Potts framework filling an interesting niche: interactive, real-time simulations of complex multicellular systems that can run in a web browser, without any need for users to install or configure software. As the authors describe, this enables new modes of education, science communication, and multidisciplinary collaboration. The software itself is impressive, and the supplied examples are clean and beautifully fluid. It is eye-opening that Javascript can run these models so well. The authors also did a fantastic and complete job in sharing their full source code, from the overall software down to individual scripts used to generate figures. The work should be of considerable interest to the eLife readership, particularly computational biologists and educators.

Essential revisions:

1. Suitability of the software for researchers:

a. Artistoo simulations do not appear to have any method to save data for external manipulation and archival. This makes their use somewhat less applicable to robust simulation-driven investigations, particularly where postprocessing and further analyses are required.

b. It is unclear if Artistoo-based models can be exported into other cellular Potts (CP) frameworks such as CC3D or Morpheus. This may leave researcher end users without a clear "upgrade path" after exploring model ideas in Artistoo and moving to larger simulations (e.g., larger or more complex domains), running simulations in high throughput on HPC resources, or adapting approximate Bayesian techniques for parameter estimation that require automating many simulation runs. Without an upgrade path, such users may wish to immediately begin in research-focused platforms rather than start with Artistoo and re-implement in another framework later.

c. Similarly, it is unclear if a model developed in Morpheus or CC3D can be directly imported into Artistoo. If such an import were possible rather than re-implementing models in Artistoo, research-focused users would be more likely to use Artistoo for scientific communication and outreach.

d. It would be fantastic if Artistoo would support the same markup language as Morpheus, allowing non-expert users to assemble complex models without writing a single line of code. If Artistoo would support the Morpheus ML, this would make all existing ``Morpheus models' also ``Artistoo models', meaning that Artistoo would become the standard for sharing CPM models with collaborators. Finally, adopting a common markup language between projects would be the first example of standardization across open-source CPM software packages.

2. Need for improved educational scaffolding:

The examples provided in the paper are excellent. However, they lack context on what the parameters mean or do. (For example, what are maxact and λact in the cell migration model?) This may limit the educational impact because users will be unclear on what to change, and how the parameters relate to cell biophysical processes.

The authors should include more background information with each model, define parameters, and give end users some idea of what to expect when parameters are changed. We have also found it useful to help guide a new user's exploration of a model by suggesting parameter sets and describing what they should see. This can serve as an educational scaffolding to help learners build and grow.

The authors' sample models should serve as a template to Artistoo users on best practices for communicating models to diverse audiences.

3. New developments in online cellular Potts simulators:

The authors should note that CompuCell3D has recently been ported to run interactively online in a web browser. See https://nanohub.org/resources/compucell3d. This recent development should be addressed in the paper.

4. Narrow review of interactive, "zero install" simulation frameworks:

The authors focus too narrowly by only comparing Artistoo with other cellular Potts frameworks, while the main use case for Artistoo is for interactively sharing and communicating complex simulation models online.

The authors should discuss non-CP frameworks that worked towards this, such as CC3D on nanoHUB (see above), online Tellurium (https://nanohub.org/resources/tellurium), current practice to share R models online as Shiny apps, and recent work to use xml2jupyter to automatically convert research-focused (command line) PhysiCell models to interactive Jupyter notebooks that can be shared as interactive webapps on nanoHUB (e.g., https://nanohub.org/tools/pc4cancerimmune). All of these serve similar purposes of creating zero-install, interactive versions of models for science education and communication. The authors should briefly discuss these to further contextualize their work.

5. While this is a more minor point, I would feel more comfortable if the supplementary information had convergence and accuracy testing. Are there limits on computational step sizes for numerically accurate simulations, particularly for large energies or when including diffusion processes?
