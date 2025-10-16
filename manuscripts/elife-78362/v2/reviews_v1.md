# Peer review - Round 1

Editors:
- Laura L Colgin, https://ror.org/00hj54h04 University of Texas at Austin United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78362.sa0](https://doi.org/10.7554/eLife.78362.sa0)

This manuscript provides an overview of an important project that proposes a common language to share neurophysiology data across diverse species and recording methods, Neurodata Without Borders (NWB). The NWB project includes tools for data management, analysis, visualization, and archiving, which are applicable throughout the context of the entire data lifecycle. This paper will help raise awareness of this endeavor and should be useful for many researchers across a broad range of fields who are interested in analyzing diverse neurophysiology datasets.


---

# Peer review - Round 1

Editors:
- Laura L Colgin, https://ror.org/00hj54h04 University of Texas at Austin United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78362.sa1](https://doi.org/10.7554/eLife.78362.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "The Neurodata Without Borders ecosystem for neurophysiological data science" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Senior Editor.

Comments to the Authors:

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife.

Reviewers agreed that Neurodata Without Borders (NWB) has merit and that the field will benefit greatly from this type of initiative. However, reviewers agreed that the paper in its present form reads more like a press release or an advertisement than a technical paper. Reviewers agreed that this language and style is inappropriate for an eLife paper. Reviewers felt that a more appropriate focus would have been to explain how NWB works and which advantages it provides over previous attempts at data standardization- to compare it more fairly with other similar attempts- rather than to advertise their success in an unbalanced manner. The paper lacks proof-of-concept of the advantages of this system and lacks benchmarks against existing or alternative systems/platforms. The technical innovations of this endeavor were unclear in this paper. It is unclear what makes NWB unique and novel and why scientists should adopt this format over other possible formats. Reviewers felt that the impact of this endeavor will be greatly limited if it is not broadly adopted, and this paper was not viewed as providing a compelling case as to why a diverse range of neuroscientists should adopt this platform.

Reviewer #1:

In general, providing new resources to enable the principles of FAIR data in the neuroscience community is an important and worthwhile effort. It has been addressed by many national funding and research institutions through issuing clear guidelines, summarized in Data Management Plans. Many labs have implemented this and their publications give clear instructions on how to access the source data. It seems likely that data searching and sharing will always heavily rely on reading scientific papers and interacting personally with the authors to discuss the datasets. Still, to have a common archive for a larger community can further simplify exchange and sharing of data, and also guide the design of novel experiments.

However, I currently do not think that this manuscript meets the standards for Tools and Resources article in a scientific journal as eLife. The article is a peculiar mix of meta-language that reads more as an advertisement rather than as a way to provide "exploratory or proof-of-concept" experiments on a new methodology. Also, there are statements about past efforts in the field that, in my view, do not adequately represent the situation and thus cannot be accepted as a "thorough benchmark against existing technology". Finally, the writing contains Jargon from computer language and over-synthesized figures that make me think that the manuscript should be edited by a neuroscientist for better access to the target public. There are additional major gaps, such as clear guidelines for the researchers and explicit statements of the added values of adding data to NWB, and a plan on whether/how data will be safeguarded and curated in the mid- and long-term future.

1) On p.6, it is said that data become useless when the individual who generated that data leaves the lab. I do not think that this adequately represents the current situation given that many labs tightly follow data management plans in which this very problem is addressed.

2) I do not understand the choice of experiments used in Figure 1 that seems rather arbitrary. As a Tools and Resources article, I am not sure whether such loose assembly figures that seem mostly there to provide a visual illustration are really necessary.

3) The abstract should state that all software presented here is open-source.

4) The work cites previous efforts to organize large-scale data in the context of the US brain initiative or the Human Brain Project. Then it is asked why these were "not successful". I do not understand this question because it implies that being successful means only being used by many people. This is not an appropriate representation of the success of these efforts.

5) As an experimental neuroscientist, I do not understand the description of current data as "standard, monolithic" (p.8). I find this an unnecessary pejorative characterization.

6) At the same place, I find the wording of a "conceptual departure from a traditional notion of a … data standard" one of the many, many examples of a metadata language that relies on unsubstantiated wording without providing the reader with useful information.

7) In a Tools and Resources article, is it really necessary to speak about prizes and recognitions of significance? The entire text around Figure 2 would be more suited for a flyer or home page advertisement of a technology rather than for an article in a scientific journal aiming to provide tools and resources to the readers.

8) What justifies the word "ecosystem"? What is the factual evidence for it?

9) Every new subchapter in the Results part re-initiates on basic considerations circling around challenges of data organization, heterogeneity of data, multiple streams of data, generating data at an unprecedented scale…. I think these considerations should be part of the introduction and it would be sufficient to declare them once. Then, the introduction could also be freed of even more basic considerations on the "immense diversity of life on earth".

10) As indicated in the guidelines for Tools and Resources, the manuscript should provide exploratory or proof-of-concept examples/experiments demonstrating that NWB has provided real advances and new biological insights because of the facilitated access to data.

11) What is the decision tree the researcher should go through before deciding to upload his data to NWB? What are the legal constraints? Can NWB replace local repositories and who takes the responsibility for stored data? How is appropriate referencing done once data uploaded by one researcher are downloaded by another one?

12) There should be quantification of data uploading and sharing between current users and an evaluation on how this has affected their research.

13) There should be a discussion of the current limits of NWB, limits from the simple indication of data size up to the fact that often nowadays neurophysiology is combined with multiple parallel analysis, ranging from genetics to varied behavioral manipulations that include animal handling, housing, husbandry, circadian entrainment, etc.

Reviewer #2:

This work details the ways in which the developed Neurodata Without Borders (NWB) ecosystem tackles the challenges of Findability, Accessibility, Interoperability, and Reusability (FAIR) for neurophysiological data. From a technical standpoint, this work clearly describes how NWB can serve as a flexible but sustainable data standard for neurophysiological data. This work discusses the software stack of NWB, the individual components, and how users and developers can interact with the ecosystem, and provides a high-level overview of how data can be interoperable between common programming languages used in neuroscience. The work also describes the ability of the NWB standard to accommodate multimodal neural and behavioral data, with infrastructure in place to allow for the integration of novel experiment paradigms and data formats. The authors describe internal- and community-based review processes to potentially integrate these novel formats into the core of the NWB standard. Furthermore, this work discusses existing integration with certain data acquisition systems and current efforts to expand the list of compatible acquisition systems and describes tools and efforts to convert data from legacy systems. Finally, this work describes a developed data repository, DANDI, that uses the NWB standard, and how it overcomes existing issues with current repositories in the context of findability and reusability. From a sociological standpoint, this work shows evidence of its growing user base and adoption with references to further efforts to increase adoption through events, workshops, resources, etc. Overall, this is not a traditional scientific paper, and is rather a description of the NWB platform that is meant to raise awareness among neuroscience researchers.

Details and Comments:

To expand on the components, for the purposes of data modeling and standardization, the authors developed the NWB format schema and specification language, which are both based on the existing Hierarchical Data Modeling Framework (HDMF). For the purpose of data storage, they have developed software that translates NWB-formatted data primitives to common backend storage formats such as HDF5. For the translation and use of data by end-users, they have developed application programming interfaces (APIs) for both matlab and python. These APIs allow end-users to load, visualize, analyze, and save NWB-formatted data. These two APIs are also interoperable, meaning that files created in one can be read by the other, thereby allowing increased collaboration between organizations that use different programming languages. In order to allow the neuroscience community to extend the functionality of NWB, the authors have released a set of templates and tools that allow for the development of Neurodata Extensions (NDX) by end-users. These extensions allow users to add support for specific types of data that may not be supported by the NWB core. Lastly, the authors have developed the Distributed Archives for Neurophysiology Data Integration (DANDI), a web-based data archive for NWB datasets. This archive is currently in early-access, and contains 18 TB of data across 71 datasets.

The authors have also developed NWB's organizational structure, as well as community outreach in order to increase the adoption of NWB by the neuroscience community. The authors have developed an organizational structure for the purposes of data governance and community engagement, which will promote the longevity and sustainability of their platform. They have additionally developed a formal review process whereby community members can suggest changes to the NWB core, which will ideally allow NWB to evolve with the needs of the community. The authors have shown that their outreach efforts have so far been successful by listing scientists and institutions that have adopted the NWB format and have contributed to the DANDI data archive.

In summary, the authors have described the goals and functionality of the NWB ecosystem, and have shown that its adoption by the neuroscience committee is promising. The primary purpose of this work seems to be to raise awareness of the NWB platform in the neuroscience community, and the authors have demonstrated its viability as a unifying framework that has the potential to improve collaboration between neuroscientists. The success of NWB as a unifying platform will ultimately depend on whether the broader community will further embrace and adopt it.

I believe the paper sufficiently describes the goals and approaches of NWB. My only main comment for the authors is to clarify the technical/technological innovations of this work better, compared to previous attempts at data standardization within the neuroscience community, if any. The authors do not seem to mention any other data standards by name other than their previous NWB version. Are there any technological innovations here compared to previous attempts? Or is it that there have been no previous coordinated attempts at this scale for writing and organizing the software such that it can facilitate future additions, and mechanisms that allow this work to evolve with what's new in the field? Is the innovation mainly in the software to facilitate these aspects and community engagement?

Reviewer #3:

The manuscript starts by outlining the motivation, development and dissemination of NWB. These sections are interesting, but they extend too long and include excessive digressions into rather philosophical or historical aspects that dilute the main message of the paper. I believe some of this space would be better used to describe in more detail other technical aspects of NWB. The following sections describe with some level of detail the different components of the NWB 'ecosystem'. While it is understandable that such a large project cannot be fully described in a paper format, I would be useful to expand the description (perhaps in supplemental material) of some concrete examples of its application (as the one described in Figure 4). The last section described a repository of NWB dataset, DANDI, aimed at collaborative research. This is an important complement to the NWB pipeline; however, it is not completely clear how does it differ from other existing and successful repositories for neurophysiology (e.g. CRCNS). In this regard, vague statements (e.g. 'few data archives today support a collaborative research model') should be substituted by specific arguments.

The manuscript is well articulated and clearly explains the motivation and implementation of NWB in an accessible manner for the general reader. However, it has, in my opinion, a significant flaw. I believe that the goal of this paper should be not only to showcase the impressive progress of the NWB initiative, but also to convince other researchers to adopt it. While the former was largely achieved, a better effort could be done towards the later. The cost of adopting a new data standard is quite large for an individual laboratory. The NWB community has done an excellent effort to ease this process, through workshops, tutorials, etc. On the other hand, they still have in the first place to convince individual researchers that adopting NWB is worth the effort. In this regard, the description of NWB adoption seems overstated in the paper. While it is impressive the reach shown in hackathons and workshops, the labs in Table 1 have perhaps contributed with some test datasets to NWB or participated somehow in the initiative, but are not using NWB as their internal data standard (at least not many of them). In my view, a way of achieving this, would be to offer and array of tools from which labs adopting NWB can immediately benefit. There are many examples in Neuroscience and beyond of data analysis toolboxes that have been tremendously successful and wide-spread and a data format was adopted as a consequence of this. I believe that, if NWB would put a stronger emphasis in the development of tools around their data format, that will offer a better incentive for many potential adopters. In the manuscript, the description of such tools or plans for their future development is nearly absent, with the exception of tools for converting data formats or visualizing NWB files. The tools described to manipulate and visualize NWB are an important development, but in themselves do not offer much incentive for would-be adopters. This is a long process and perhaps beyond the scope of the current manuscript. What should be done in the present manuscript, is to more clearly outline the short-term advantages for individual researchers, especially those generating data, of adopting NWB. So far the long-term advantages for the broad community or the immediate advantages for scientist looking for open datasets to analyze are clear. But if NWB is really to succeed it needs to also convince the individual groups and researchers that already work with their own data formats and use other platforms to share their data, that adopting NWB has unique and concrete advantages for their daily research activities.
