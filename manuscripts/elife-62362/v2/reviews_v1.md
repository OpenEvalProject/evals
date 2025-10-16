# Peer review - Round 1

Editors:
- Upinder Singh Bhalla, Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62362.sa1](https://doi.org/10.7554/eLife.62362.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

FlyBrainLab is a resource for driving connectomic analyses of the Drosophila brain and for carrying out computational modeling based on multiple data sources. It supports 3D visualization of datasets published in the worldwide literature, and a number of libraries for integrating anatomical, sensory and physiological data with published and exploratory computational models. It will be useful for a wide range of activities, from exploring the content and intersection of datasets, to comparing circuit models in the same computational setting, to running massively parallel circuit simulations.

Decision letter after peer review:

Thank you for submitting your article "FlyBrainLab:Accelerating the Discovery of the Functional Logic of the Drosophila Brain in the Connectomic/Synaptomic Era" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Ronald Calabrese as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Padraig Gleeson (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This manuscript outlines the FlyBrainLab platform, which brings together a number of software packages from the authors to provide a unified interface for viewing data and simulating neuronal activity related to Drosophila. The reviewers felt that the paper had promise but there was substantial work still to be done.

Essential revisions:

1) Could the authors provide substantially more detail on how an experimentalist would use the package? It should be clear why they would want to do so.

2) The manuscript must provide transparency on the data processing and

integration.

3) The package would be far more user-friendly if it had much simpler installation. Detailed instructions would help too.

4) Users would benefit from a process to keep the packages up-to-date, such as for the “hemibrain” module.

In addition, the reviewers have provided many helpful comments to help the authors with their revision.

Reviewer #1:

This manuscript outlines the FlyBrainLab platform, which brings together a number of software packages from the authors to provide a unified interface for viewing data and simulating neuronal activity related to Drosophila.

The application is well described and examples of its use are given. The code for the application components is open source and installation instructions and documented are provided. The suite of components clearly work well together providing a very good example of a user focussed computational neuroscience application for working with advanced data and models.

1) While much of the technical/implementation detail is reserved for the Materials and methods section, the main body of the manuscript would benefit from a high level diagram of the structure of the application (like Supplementary figure 1, or even simpler), or a table defining/summarising the various components mentioned in the main text (NeuroMinerva/CxCircuit/NeuroArch etc.) and how they related to each other.

Reviewer #2:

FlyBrainLab by Lazar et al. provides the ability to set up, execute, and analyze Drosophila neural circuits, while integrating/exploring connectomics data, in a single platform. Such a unified framework has the potential to advance our understanding of the functional logic of the fly brain. The authors show that FlyBrainLab tools can be used to execute models developed previously in the literature. What is missing, however, is a clear demonstration that the platform can be used for de novo exploration and guidance on how the tools offered by the platform will enable new discoveries. In particular, the case is not made that using this library provides an easier path to discovery than the normal ad-hoc approach. The work does not fully describe what a user needs to do to deploy it for their own studies, nor does it clearly show how its own examples were generated.

1) Across the circuit examples supplied in the manuscript, it is not clear what features need to be manually coded up for the particular circuit/question of interest vs. what features can be pulled from FlyBrainLab and directly used. At present, the discussion of the different libraries in the supplement lists capabilities, but there is no guidance or examples of how the libraries can be used in practice. We could not find documentation for CXcircuits, EOScircuits, and MolTrans online. Similarly, the supplementary video illustrates the interactive capabilities of the platform, but the manuscript does not guide the user in replicating these capabilities on their own. To fix this, we advise the authors to include the notebooks used to generate all of the figures/analysis in the main results as supplementary files, with detailed annotation so that a user can use them as starting points for their own analyses.

2) More must be included in the manuscript to describe how the tool can be used for exploratory analysis. Consider including a simple annotated code walkthrough that, starting with some list of neurons, perhaps from the Hemibrain, answers what utilities are available/what code is needed to visualize neuron morphologies, what code is needed to generate an interactive circuit diagram, what code is needed to set up a simple leaky integrate and fire model, what is needed to execute a circuit, and whether resultant firing rate outputs look reasonable. The panels in Supplementary figure 3 are close, but they show the results of the above workflow, and there is no demonstration on how one can get there. Such an example need not (and perhaps is better not to) focus on a well-characterized circuit. The simple examples found in FlyBrainLab/Neuroballad are promising.

3) More work can be done to lower the barrier of entry for FlyBrainLab. Even as a researcher with a few years of Python experience that is currently using the Hemibrain to set up, run, and analyze neural circuits, I had difficulty installing FlyBrainLab and knowing what steps to take to replicate the examples shown in the manuscript. In particular, the installation instructions seem inconsistent/not fully developed on https://github.com/FlyBrainLab/FlyBrainLab. It took hours to figure out which instructions to follow to end up with a Jupyter Lab configuration that resembles the supplementary video, with a notebook, a morphology viewer, and a circuit viewer in the same window. The installation instructions within NeuroMinerva, built on JupyterLab version >2, helped get me to that point, but the instructions on FlyBrainLab, built on JupyterLab version <2, did not get me to that point. In addition, the "Starting Up FlyBrainLab" section on https://github.com/FlyBrainLab/FlyBrainLab should have material on what to do if you do not see an FFBO section or cannot run the example notebook, perhaps in some troubleshooting page.

Reviewer #3:

Lazar and colleagues present a platform, FlyBrainLab that integrates Drosophila neuron and circuit modelling data with neuroanatomy, from morphology to synaptic resolution information. Their desktop system is modular and stand-alone, providing the ability to query, run and visualise particular circuits and models. To demonstrate the functionality of their platform they present 3 specific examples that cover the use of published models, light and electron-microscopy (EM) data and the comparison between larva and adult.

Although the need their platform is addressing is real, the manuscript does not present the work in a compelling way, particularly for this journal's audience. Furthermore, the methods used to integrate data, and how data are used are not described properly. If a system such as this aims to become a standard analytical tool for neuroscientists, it is essential that data integration and processing are transparent.

Please find below a number of concerns. I do not comment on the technical details of the FlyBrainLab platform modules, as that is not my expertise.

1) The structure of the manuscript and the way the examples are presented are not compelling for the average neuroscientist that wants to start using the public data (models, connectome and synaptome). Especially if the one of the main draws of this type of platform is for neuroscientists to start testing models based on real data. The main reason for this is that very little information is given on how experimental data is curated and integrated (see below for more).

2) What neuroanatomical data is being used and in what way is completely opaque. It is assumed that different modalities of data will have been processed in different ways, but very little information is given in this regard. How is the light-level FlyCircuit data processed to infer connectivity and how is this process validated? How are cell types identified and validated, in FlyCircuit and the hemibrain? How many neurons and types are used for each use case?

For example, regarding the CX circuit example, the authors say, "The innervation pattern of each neuron was visually examined in the NeuroNLP window and a standard name assigned according to the naming scheme adopted in the CXcircuit Library." How do these standard names relate to the cell type names used by the community? Identifying cell types from morphological data requires expertise when this is done to the highest resolution, and thus this process should be described in detail. In addition, it becomes very difficult to assess the use cases presented when there is no clarity on what neurons and types are being used.

3) Related to the point above, the authors list the hemibrain data used is from version 1.0.1 (gs://hemibrain-release/neuprint/hemibrain_v1.0.1_neo4j_inputs.zip). However, a new version of the data (1.1) was released online in May, with the data dumps available at least from the end of June (according to https://dvid.io/blog/release-v1.1/). The latest version significantly improves the cell typing that had been released (see https://docs.google.com/document/d/1vae3ClHR8z8uekqwrOHtqiux3oY5-Y_xw6W2srCi3PI/edit?usp=sharing). The authors should update their manuscript to use the latest version of data. This should highlight issues of how data can be kept up to date in these types of platforms and how integration of versions can be achieved. The authors should comment on the processes they use for this.

4) Presenting this platform as a Resource, it becomes essential that it is easy to install. I attempted to install FlyBrainLab according to the instructions in https://github.com/FlyBrainLab/FlyBrainLab. Using miniconda on macOS, which I already had installed for other purposes, I unfortunately ran into errors, and the installation was unsuccessful (seemingly caused by msgpack not being found). The instructions mention that the platform has only been tested in Ubuntu but that it "should work" in other platforms. I understand that it is not possible to test for and avoid, all possible errors, but the authors should test the installation in at least one other OS, if they want the average neuroscientist to start using it.

The tutorials listed in https://github.com/FlyBrainLab/Tutorials are certainly a very useful introduction, although they suffer from the issues in points 2 and 3.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Accelerating with FlyBrainLab the Discovery of the Functional Logic of the Drosophila Brain in the Connectomic Era" for consideration by eLife. Your article has been overseen by a Reviewing Editor and Ronald Calabrese as the Senior Editor.

The Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional work is required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

The revised manuscript has addressed some of the technical issues, but has not addressed the core issues of readability of the manuscript , and usability of the software, by a regular fly neurobiologist. This was stated in the Essential revisions, point 1: "1. Could the authors provide substantially more detail on how an experimentalist would use the package? It should be clear why they would want to do so."

While the authors have responded with some limited explanations in the cover letter, the required changes are not evident in the manuscript, and it is there that these essential points of usability must be clarified. Again, it is not sufficient to refer the reader to the website to do this. The appendices, and much of the text, still mostly tell the reader what can be done, rather than how to do it. This should be rather early in the manuscript to motivate what follows.

Similarly, on essential point 2, the reviewers would like to know how their data goes in and is manipulated, and how they can be confident that what the program does is faithful to the original. Issues of installation, which have been presented, are relevant, but of secondary technical importance.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Accelerating with FlyBrainLab the Discovery of the Functional Logic of the Drosophila Brain in the Connectomic Era" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Ronald Calabrese as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Padraig Gleeson (Reviewer #1); Danylo Lavrentovich (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

The reviewers and I felt that the paper and FlyBrainLab provide a userful resource for the field. The revised version is considerably improved and the reviewers would like to suggest a few essential but straightforward revisions to make it even more accessible to the readers and users of this resource.

1) Update key references (indicated in the detailed reviews).

2) Clarify Figures and their legends, especially Figure 2 and 3.

There are several further important suggestions by the reviewers to strengthen the presentation and improve the accessibility of the paper and resource for readers. These are provided in the detailed reviewer comments below.

Reviewer #1:

This new version of the manuscript has a better layout and will be a more useful introduction to the application for new users. However there are still some issues with how the structure of the application is presented which may be difficult for readers.

Figure 2, especially the legend is quite minimal and there is nothing here to give a reader the key idea that this is a graphical application which a user would interact with through their browser. I suggest to move the screenshot of the application from Appendix 1—figure 2 to a panel in the main figure 2, and make sure these panels are well integrated and explained, e.g. NeuroMynerva in the top panel is what you see in the bottom. Refer the reader here to Appendix 1—figure 1 for more details (some of the colors of the blocks match between the simplified/full versions, e.g. green NeuroArch, there's no reason they all shouldn't for ease of readability).

NeuroNLP and NeuroGFX (window) are mentioned in the text without any context. These need to be shown/explained in Figure 2 and also described briefly where NeuroMynerva etc. are first defined in the Introduction. I would suggest highlighting all important component names in bold where they are first introduced so a user can go back to the definition as they are discussed later in the text.

It is strange that the actual short English language queries used for Figure 3 are not mentioned in the legend or main text. This is an important feature of the application and adding (at least some of) the sequence of commands for one of the panels (e.g. 3a, "show T4a", "color red", "add cholinergic presynaptic neurons" etc.) in another panel/table in the figure would be quite informative for readers. In the main text "(see also Materials and methods)" could be replaced with something better like: (the full sequence of queries which created this panel can be found in the Materials and methods). Also explain that the panels in Figure 3 are screenshots of the NeuroNLP window in Figure 2B, etc.

It is good having a section in the Materials and methods for each of other figures related to the main use cases/examples, but these could be tied together better also, making it clearer that the details of how the figure panels were generated can be found in the Materials and methods. Also some parts of the Materials and methods do not refer back to the figures, e.g. "Model A [26], Model B [27] and Model C [28]" could refer to Figure 6A, B, C etc. Small things like this would improve the readability of the paper significantly.

It might also be worth numbering the use cases/analysis types, e.g. Use Case 1-6, and adding these to subheadings to make it easier to move between the main text and Materials and methods.

Overall the manuscript is a good introduction to the range of features FlyBrainLab offers and is structured such that a user can see what can be accomplished, and is given some guidance how they would achieve it themselves.

Reviewer #2:

The text is clearer and more inviting for a general audience. The enumeration of capabilities in the Introduction is effective. The Results section is structured well, displaying different use cases of FlyBrainLab. The accompanying tutorials online serve as good launching points for researchers.

Thank you to the authors for the additions in the main text, the code walkthroughs in the appendices, and the improved installation instructions. The basic tutorials are simple to follow. My only suggestion on the code side is to be more verbose in the introduction to the lamina cartridge executable circuit notebook and in the limitations of the user-side-only installation.

Reviewer #3:

The revised version of the manuscript addresses many of the concerns previously reported. Thank you to the authors for providing much clearer information about the data that is ready to use in the FlyBrain Lab platform, how it can be used, installed and the components of the FlyBrainLab. There are still some corrections that are needed regarding the source of some of the datasets.

Throughout the paper, reference 4 (Xu et al., 2020) is used as the citation for the hemibrain dataset. This is a preprint that has been superseded by the publication in September 2020 of the peer-reviewed paper (Scheffer et al., 2020, https://doi.org/10.7554/eLife.57443). It also needs updating in GitHub (https://github.com/FlyBrainLab/Datasets#ref-1)

The reference to the larval L1EM dataset also needs correcting. For example this is given as reference 2 (Berck et al., 2016). The correct reference, as correctly shown in https://github.com/FlyBrainLab/Datasets#ref-3, is Ohyama et al., 2015 (reference 69). There might be other instances in the text that use the wrong citation.

The section added to the beginning of the Results, which includes Figure 3, provides readers with some examples on how they can start exploring the data in the platform (published datasets) using plain English queries. However, I do not think the added Figure 3 currently presents the data in a way that makes it easy for readers to link the relevant text and figure legend that describe the connectivity, to the panels. Each of the 4 examples (a-d) displays a neuron plot (left) and a connectivity matrix (right); other than reading each of the row/column names it is not possible to link the neurons plotted on the left to the data plotted on the right. Adding a colored annotation bar or even coloring the row/column names of the connectivity matrices according to the neuron plots would certainly help, or perhaps adding some clustering.

Example 2 refers to a possible direct connection between the mushroom body and the fan-shaped body ("raising the question whether the two memory centers are directly connected"). Some of the neurons directly connecting these 2 neuropils (and possible pathways for visual information in addition to reference 17), have been described already, in Li et al., 2020 (December 2020, https://doi.org/10.7554/eLife.62576), one of the recent papers based on the hemibrain dataset. Could the authors please rephrase?
