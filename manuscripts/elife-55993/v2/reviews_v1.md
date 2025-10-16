# Peer review - Round 1

Editors:
- Volker Grimm, Department of Ecological Modelling, Helmholtz Centre for Environmental Research – UFZ Leipzig Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55993.sa1](https://doi.org/10.7554/eLife.55993.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Your coral reef model uses traits and functional types of corals to represent not only taxonomic but also functional diversity. The supplement includes a comprehensive description of the design, calibration and testing of the model. Your work is an impressive demonstration of how it is possible to combine existing data in a systematic way, test a model at multiple levels, and thus demonstrate that trait-based agent-based models allow us to model the role of functional diversity. The model will be useful for addressing applied questions and, probably requiring some more development, for addressing theoretical questions regarding coexistence and the role of diversity for resilience.

Decision letter after peer review:

Thank you for submitting your article "A spatially explicit and mechanistic model for exploring coral reef dynamics" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Volker Grimm as the Guest Editor and Reviewer #1, and the evaluation has been overseen by Ian Baldwin as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Hauke Reuter (Reviewer #2).

The reviewers have discussed the reviews with one another and the Guest Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged, your manuscript is of interest, but as described below, additional information is required before it is published. Therefore, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is 'in revision at eLife'. Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This manuscript presents a new agent-based model of coral reefs that is designed to answer questions about the response of coral reefs to multiple stressors in a mechanistic, bottom-up way. The model uses traits and functional types of corals and algae to represent not only taxonomic but also functional diversity. The manuscript includes a very impressive description of the design, calibration and testing of a coral reef model. The authors have used the ODD protocol (to some degree), calibration of 12 model parameters for three empirical locations in the Caribbean, hierarchically structured validation, and global sensitivity analysis. Spatial interactions between corals and algae are represented in detail and allow to analyze relations between traits and functional responses and thus to depict realistic trajectories of reefs under different scenarios of external forcing.

Agent-based models are often criticized because of their complexity, which makes them difficult to parameterize, calibrate, test, and understand. This manuscript is an impressive demonstration of how it is possible to combine all relevant existing data in a systematic way, test a model at multiple levels, and thus demonstrate that, yes indeed, trait-based agent-based models allow us to model the role of diversity (see also this review: Zhakarova et al., 2019).

Essential revisions:

1) The Introduction takes a lot of space in discussing challenges to coral reefs. I guess virtually all papers about coral reefs start like this. It should be shortened, also because it raises the expectation that you are going to tackle these questions, which is not the case. Rather, this is a methods paper and you should come to this point more directly and perhaps list the challenges to ABMs for exploring diversity (see above) as the key challenge addressed in this manuscript.

2) If you say, in the Abstract, that the model “provides a virtual platform": Where can we download the software? Is there a manual describing the workflow needed for running the model and all its data scripts? Is the model description in the supplements complete? If not, this article would not really provide a tool. You might have a look at two examples where ABMs were presented, in journal articles, as tools. In both cases there was a full model description, a manual, and a download site: Becher et al., (2014) and Hradsky et al., (2019).

3) Subsection “Sources and software”: It is impressive to see all those packages and tools you used, but, ideally, you would also provide all, or the most important, scripts you wrote to run these packages and tools. If others are to use your virtual laboratory, they very likely would fail immediately because they would not know how to actually handle all those tools and data sources. I know that there is no culture yet to provide all relevant scripts, but – I think we should go there.

4) The ODD model description in the main text is not bad, but just a verbal summary description while the intention of ODD is to provide all information that is needed to re-implement the model. I understand that much of these details are in the Appendices, e.g. about Initialization and Submodels? It would be good if this link would be made more explicit by having a full ODD in the supplement, as a separate file. It would contain an augmented copy of the ODD of the main text and then just provide, in all detail, the information required for the seven elements of ODD. Why? Because the point of a standard is to follow it exactly so that readers, who either know the standard or learn about it, can easily find certain kinds of information at certain places in the model description. Currently, this is finding of relevant information is made unnecessarily complex. Examples of complete ODDs of complex model are provided by Ayllón et al., (2018) and Nabe-Nielsen et al., (2019).

For producing a complete ODD, please note that a new version of ODD has been published, which in particular has very detailed guidance, in the supplement, about ODD itself, summary ODDs, model narratives, etc.: Grimm et al., (2020). All that said, please note that we certainly do not require that you use ODD (because I am the main proponent of ODD), but any format, that compiles all information needed so that it is easy to find the kinds of information listed in ODD protocol, would be acceptable.

5) Scales: The model applications relate to a space of 5x5 m (25m2). I am not sure if such a small space allows for realistic dynamics if single corals grow large (> 2-3 m diameter) as then only a very low number of individuals would be present in the simulations potentially leading to artifacts in results. It is a pity that the spatial output of the model is not shown (except one specific figure in Appendix 5). I also see a discrepancy between the very high spatial (1cm) and the low temporal resolution (6 months). The time span within half a year could e.g. cover a mild bleaching event or other disturbances as well as processes of reef recovery leading to a different species composition and thus change the reef trajectory without being considered in the present model. I do not see that it is an argument, that the field data are only available in a low resolution of approx. 6 months. A comparison with model processes stays possible even if it is resolved higher.

6) It is apparent that all model runs cover only a very short time span of around ten years (21 simulation steps). This is extremely short for coral reefs which frequently undergo dynamics based on larger time scales. Thus, emerging dynamics and states, e.g., resulting from the sensitivity analysis, should be discussed with much care.

7) Overfitting? The model is very impressive, as it is possible to very closely possible represent the dynamics of measured reefs. However, I am not sure if this actually results from some overfitting. The model (runs) include some very strong and very specific influences of external drivers. For example, at the end of a time step certain values for grazing or sand cover are enforced. At least the impact of grazing results from a feedback with different reef processes. Thus, at least much of the trajectories in the model are the result of external drivers and it becomes difficult to analyze self-organization processes in the reef. In short: you cannot claim that a model is producing realistic dynamics due to a realistic representation of its internal organization if in fact the match between model output and observations is imposed by external drivers. A similar case occurred with honeybee colony models, where often the yearly time series of colony size was compared to data to claim that the model was realistic, but that time series was largely driven by the time series of the queen's egg-laying rate (Becher et al., 2013).

8) A major question thus is whether the authors believe that their model can better address large scale questions about coral reefs, such as their resilience to regime shifts from disturbances and climate change, than 'minimal' models, such as that of van de Leemput et al., (2016)?

9) In Carturan, Parrott and Pither, (2018) coral functional traits are classified as 'resistance' and 'recovery'. In the current manuscript, the terms 'stress tolerant', 'ruderal', and 'competitive' species (Grimes' classification) is used. Do 'resistance' species and 'recovery' species of Carturan et al., (2018) correspond to 'stress tolerant' and 'ruderal', respectively?

10) The Title is suboptimal: "mechanistic" and "spatially explicit" applies to hundreds of model, if not more, including coral reef models. The novelty of you work lies in merging the individual-based and trait-based approaches to represent functional diversity. The title should reflect this (but please observe eLife's guidance on titles).
