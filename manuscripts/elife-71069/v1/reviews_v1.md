# Peer review - Round 1

Editors:
- C Daniela Robles-Espinoza, International Laboratory for Human Genome Research Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71069.sa1](https://doi.org/10.7554/eLife.71069.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

In this manuscript, Piccolo and collaborators provide a detailed overview of the Common Workflow Language (CWL) for beginner bioinformaticians, and perhaps more experienced workers that may not be up-to-date with the latest developments in reproducible research. They also provide a tool, ToolJig, to create CWL documents without needing to install any software nor to learn the specifications of the format. Written in the form of a tutorial, its major strengths are that explanations are very clear, and are accompanied by illustrative figures and examples in a Github repository. As science is currently undergoing a major reproducibility crisis, we think that it is crucial that detailed and accessible pieces such as this one are published to teach scientists to create fully reproducible code.

Decision letter after peer review:

Thank you for submitting your article "Simplifying the development of portable, scalable, and reproducible workflows" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including C Daniela Robles-Espinoza as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor.

This is an accessible tutorial that illustrates the basics of Common Workflow Language (CWL), intended both for students beginning their scientific formation and for more experienced bioinformaticians that have not adopted this community standard yet. The adoption of CWL has the potential to help alleviate the reproducibility crisis ongoing in scientific publishing. The reviewers have agreed that the figures are very clear, and the examples available on Github are helpful and they go from simple tasks to illustrating a more complex biological analysis. A webtool is also provided for easily creating CWL documents. There are a few revisions that the reviewers have recommended to make the work clearer before publication:

1. There is some confusion regarding the usage of containers in regards to the location of the workflow manager (production vs publication workflows). A container with all required analysis software, CWL document and a workflow manager seems well suited for distribution with a publication for reproducible calculations. However for production needs, a modular design with various containers and a workflow manager outside of the containers seem a better choice. It's hard to distinguish these two usages in the manuscript. Can a few lines be devoted to making these clarifications, please?

2. A reviewer notes, "I think it would be useful to beginners to see more information on the benefits of using CWL over some of the alternatives (Nextflow, Snakemake). There are quite a few ways of handling bioinformatic pipelines and in my experience I been overwhelmed by the decision of having to choose one over the rest.". Can a few lines be devoted to discussing the benefits/weaknesses of these other alternatives?

3. There is no mention of the benefits of error handling and restarts when using a workflow manager. For production environments this is a key benefit, so could this be incorporated please?

4. A reviewer mentions. "The manuscript does a good exposition of Docker and containers. However, I didn't find much mention of Docker Hub. Being that Docker Hub was a key element in the prominence of containers I think there should be a bit more details about it on the paper.". Could some lines about Docker Hub be incorporated please?

5. About figures 1 and 2 – should the name of the program in the yellow square be changed to match the .yml found in the GitHUb repository?

6. Would it be possible to add a button to ToolJig that would populate the fields, as a pre-filled example? It may be easier for beginners to illustrate how the information should be input. Perhaps following the example of one of the ones that are already in the GitHub repository so it's more easily comparable.

7. Could you please specify If the YAML document created by a user is saved by ToolJig, or is it deleted when the user closes the webpage?
