# Peer review - Round 1

Editors:
- Eduardo Franco, McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.51773.sa1](https://doi.org/10.7554/eLife.51773.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work presents a new agent-based, spatial model of malaria transmission to explore determinants of mass drug administration success in Southeast Asia. It has the potential to inform policymaking towards malaria elimination in specific areas.

Decision letter after peer review:

Thank you for submitting your article "Not all MDAs should be created equal-determinants of MDA impact and designing MDAs towards malaria elimination" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Eduardo Franco, acting as Reviewing Editor and Senior Editor. The reviewers have opted to remain anonymous.

As is customary in eLife, the reviewers have discussed the reviews with one another. What follows below is my edited compilation of the essential and ancillary points provided by reviewers in their critiques and in their interaction post-review. Some of the reviewers' comments may seem to be simple queries or challenges that do not prompt revisions to the text. Please keep in mind, however, that readers may have the same perspective as the reviewer. Therefore, it is essential that you attempt to amend or expand the text to clarify the narrative accordingly.

Summary:

This work presents a new agent-based, spatial model of malaria transmission to explore determinants of mass drug administration (MDA) success in a Southeast Asian setting. The authors especially emphasize the following aspects as previously underexplored or unexplored in other theoretical and model-based MDA studies: the role of gradual implementation of MDA due to realistic logistical constraints of finite MDA teams and how drug resistance affects optimal choice of implementation options. Other factors such as initial prevalence, interaction of MDA with other interventions such as case management and vector control, and timing relative to the transmission season are also considered here as they have been considered by a diverse set of other models. In all, this work has the potential to inform policymaking towards malaria elimination in specific areas.

Title:

Except for well-recognized acronyms and abbreviations, technical terms must be spelled out in manuscript titles. Every acronym must be spelled out at the first instance it is used. Once introduced, it may be used throughout. This rule applies to the Abstract and main text independently. Do not introduce an acronym or abbreviation if it will not be used again (Abstract and main text considered independently). An acronym must represent a minimum of three words.

Essential revisions:

1) Issues related to the model formulation:

The authors' conclusions on speed of implementation and role of resistance in determining optimal implementation strategy are rather subtle points. At the same time, I believe this is a previously unpublished model and thus its introduction in the literature should also contain a rigorous demonstration of its ability to recapture field data, particularly epidemiological data. While there are plots in the supplemental material that show model outputs around some basic epidemiological quantities (incidence by age and prevalence, for example), I did not see any comparison with field data, which is surprising since the authors are close collaborators with excellent field researchers specializing in malaria in Southeast Asia. Absent these basic comparisons with field and clinical data, it is difficult to assess whether the model's structure and parametrization adequately capture key phenomena to the point that claims around speed of malaria resurgence after MDA, and response of wild type and resistance infections to drug treatments (and thus selection pressure on these parasites) are to be believed.

In addition, there appears to have been a lost opportunity to further capture actual malaria transmission and historical MDA implementation in this set of villages. While the authors consider 3 possible distributions of transmission intensity across their village population, it would also be helpful to parameterize each village's transmission intensity based on field data collected in these villages, or at least to compare the actual distribution against the 3 modelled options (especially since outcomes were somewhat dependent on the nature of this distribution). Similarly, it is unclear to what extent the modelled MDA implementation (selection of random villages to begin, then moving MDA teams to adjacent untreated villages) resembles the actual implementation of the MDA in Karen State. As a naïve outsider I would guess that teams perhaps started in villages at one end of the area and worked their way together toward the other end (?), which seems logistically simpler for supply chain and transportation. Since this paper is about making models of interventions more operationally realistic, it would be great to include even more realism.

Questions on model structure and parameterization:

I'm curious about the decision not to model non-infected, non-infectious mosquitoes and how that could affect model outcomes, particularly around vector control effect size.

On immunity, my understanding is that individual acquire immunity to clinical symptoms but no other kind of immunity, such as to high-density asexual infections. Thus, the infectiousness of asymptomatic individuals is identical. Is this an accurate assumption?

Similarly, the parameterization of symptomatic and asymptomatic infectiousness as equal is curious and seems to contradict some field data. Can the authors point to evidence that this is a reasonable choice for their setting?

The authors mention a 5-year initialization phase of their model and that to begin with, there is no immunity in the population. Looking at Figure 1—figure supplement 2, middle panel, it doesn't look to me like 5 years of initialization is sufficient to reach an equilibrated population immunity structure.

Case management rate in villages with malaria posts (0.6) seems low. I believe in many SE Asian villages, a clear reduction in malaria incidence is observable after the introduction of malaria posts, suggesting they have a considerable effect on reducing transmission. Does this also happen on the same timescale in the model, with case management rate as low as 0.6?

2) Issues related to interpretation:

My main comment is that the results presented did not quite show what is stated in the Abstract: "We conclude that mass drug interventions can be an invaluable tool towards malaria elimination in the right context, specifically when paired with effective vector control" because:

a) It overstates the impact of MDA given that the probability of malaria elimination is extremely small unless done in a very low transmission setting

b) To justify this conclusion, the authors need to show a slightly different outcome – the 'increase in probability of elimination when MDA is carried out'. I.e. there is the issue that in many models the probability of stochastic elimination of the parasite without any interventions is significant in low transmission areas. So, the absolute probability of elimination in the presence of MDA is not that informative, it's better to know the increase in probability. The authors need to check the probability of elimination without MDA in their model and present those results in comparison to simulations in which MDA is included, which I believe is achievable within the timeframe of the journal's revision process.

Another key point is that although the authors nicely include variation in exposure to malaria across different villages, it's well quantified that this variation exists also within a village and has a strong effect on R0 and elimination probability – was this included in the model? (e.g. see Goncalves 2018 eLife: https://www.ncbi.nlm.nih.gov/pubmed/29357976 and Woolhouse 1997 PNAS: https://www.ncbi.nlm.nih.gov/pubmed/8990210). It would be relatively straightforward to put this into an individual based model, by setting the force of infection to have a distribution around the mean, instead of being the same for each individual.

As a general comment the labelling of figures needs tightening up – e.g. lines, abbreviations, units on the axes are often not clearly defined (see below for specific comments). Ideally these should be understandable without going back to the main text and Materials and methods. It would be a shame if the interesting messages of the analysis did not get through because of being hard to interpret. Also, the model parameters need more justification and documentation in places (immunity, age structure, relative infectiousness of asymptomatic and symptomatic infections). It would be hard to reproduce the model from the description, although the code is provided. Some though not all of these could impact the MDA results.

3) Section-specific concerns:

The Abstract and Introduction read as if the paper is extremely general. Most of the time malaria, not a specific species, is discussed. In the second paragraph of the Introduction, falciparum is mentioned and many of the parameters seem to relate to falciparum. Furthermore, in the fifth paragraph the authors state that the "modular simulation platform that is customizable to any malaria transmission setting" but then in the Materials and methods first paragraph "likely not applicable to Africa."

Inconsistent terminology makes the results unclear.

– MDA rounds refer to two things in the paper. Results first paragraph, it seems "MDA rounds" means MDA campaigns. This occurs again in the Discussion second paragraph. At other times in the same paragraph, what appears to be campaigns are referred to as sets, as in this case sets of rounds are discussed. Is MDA rounds here related to campaigns or the 3 standard rounds of implementation.

– Results paragraph one, how does Figure 2—figure supplement 5 relate to artemisinin spread. Further, what is "outcome" in this figure? It is not clear from the text or caption.

– Results paragraph two, how is "a more static population" defined? Mobility is not well defined in the main text. A brief description is finally given in the second paragraph of the Discussion. Furthermore, mobility is described both as a fraction and as a decimal, which makes it difficult to compare across figures. How does connectivity relate to mobility? How does "well-connected" relate to mobility? Discussion paragraph four, does "low connectivity" mean low mobility?

– Results paragraph two, what constitutes "little difference"? Many of the curves in Figure 3—figure supplement 1 seem to be separated.

– In the same paragraph what are the "transmission heterogeneity distributions"? later in the paragraph "the other two" are mentioned but not named. They are not described anywhere clearly. Figure 4 is referenced here as a comparison between distributions but only uses a single distribution.

– At the end of paragraph two, how is the "significant correlation" measured? There appear to be no statistical tests mentioned.

– Results paragraph three, how has vector control "greatly improved"? Is this measured? Visually they appear similar.

– Discussion paragraph two, how are the mentioned factors a distant second and third? Where is this quantified?

– How is a slower MDA implementation optimal? The solid line often appears to exceed the dashed line.

More information is needed in the Materials and methods.

– In paragraph seven mobility is briefly defined but referred to the main text, where there is not a good description. How are the nights chosen in the simulation? How does seasonal and long-term migration occur in the simulation? Does this effect the biting rate in places?

– In subsection “Simulation Protocol”, what other co-infecting parasites are considered?

– What drugs are used?

– Subsection “Model Initialisation”, do the data describe the initial properties of things like age, transmission status, etc.?

– Subsection “Model Initialisation” paragraph two, two different implementations of how human agents are assigned is given, which is it?

– Subsection “Human Properties”, are cumulative number of exposures and immunity level set to 0 for humans of all ages? This seems unrealistic.

– Subsection “Village Properties” is the calibration of biting rate stable when you introduce mobility and change malaria prevalence?

– Subsection “Implementation of malaria relevant dynamics”, the implementation is unclear. A random number is drawn to see if there is an event and then random number are drawn to see if there are each of several events. Does this mean that an individual could be infected and treated and die all in the same day? If so, why go through the earlier event draw?

– Subsection “Human Population Dynamics”, when death happens, are individuals replaced by an infant or by an individual of any age? If the latter, how are their initial properties chosen.

– Subsection “Human Population Dynamics”, moi, cml, and lvl are not in Table 2. Could a table be created for parameters that change over time with an individual?

– Can individuals be infectious immediately with program 1/sigma? This seems unrealistic. Why not use a fixed time delay?

– “Parasite killing rates depend on the person’s transmission status (𝑠), with parasite clearance”, s is not in Table 2. Similar comment to above.

– “Susceptibility/Infectiousness”, why include phic if the value is set to 1 (no increased/decreased relative infectiousness)?

– Subsection “Mosquito Dynamics – Survival”, it appears these values are inverted.

– "uncommon for any female to reach multiparity" Is this quantified?

– How does immunity work? It's not discussed in detail, although some figures pertain to it.

Figures/Tables are hard to interpret due to missing information.

– Figure 1: In A what are σ, ε, and ω? In C, what are the immunity levels? Is 1 higher or lower than 4?

– Figure 2: x-axis is not labeled.

– Figure 3: Lots of things are varied but none are mentioned in the caption.

– Figure 4: What is varied is not evident from the caption, nor is the distribution apparent.

– Figure 1—figure supplement 1: Why cut off the distribution prior to 80 if that is the max?

– Figure 1—figure supplement 2: What is "mean immunity level"? Why does it go up and down with age?

– Figure 2—figure supplement 1: The size of the dots makes it hard to tell how far the lines go.

– Figure 2—figure supplement 2: What is outcome here?

– Figure 2—figure supplement 3: What is outcome here?

– Figure 2—figure supplement 5: What is outcome here?

– Table 2: What does variable mean for parameters such as beta, previ, resit, vcefficacy? Can these be listed somewhere?

– Table 2: Parameter 37 – 50 are never mentioned in the manuscript.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your revised article "Not all MDAs should be created equal-determinants of MDA impact and designing MDAs towards malaria elimination" for consideration by eLife. Your article has been re-reviewed by the original peer reviewers, and overseen by Eduardo Franco as the Reviewing Editor and Senior Editor.

We are happy to see the effort you made at amending the paper to accommodate the concerns and suggestions from the reviewers. Once again, we are unable to accept it in its present form for publication. However, we are willing to consider a new revised version if you can address the additional concerns and suggestions below.

Essential revisions:

It is difficult to discern from the manuscript what things are functionally in the model and what are used in the analyses presented. These seem to be justified in the response to the reviewer but not clearly in the manuscript.

Attempt to capture realistic operational conditions, given that the paper is about the impact of actual operational conditions on MDA outcome. The MDA distribution structure and its implication on the authors' results are still not clear. The authors are adamant that they are not attempting to model an actual MDA distribution, but it seems that randomly selecting starting villages with which to seed MDA teams is unlikely to be how MDA is actually implemented, and potentially there are interactions between the spatial pattern of MDA implementation and the role of migration in MDA outcome. The authors must either show that their method of random selection of starting villages is how someone has operationalized MDA, or that a more operationally realistic village visitation order does not impact their findings.

Infectivity: it is true that there is much that we do not understand quantitatively about infectivity/infectiousness. However, the simplifying assumption that all infected individuals, symptomatic and asymptomatic, have the same infectivity seems a little strong, especially since the authors note that changing phic does impact the effectiveness of MDA. Might it not also impact how the outcome of the MDA depends on the logistical, demographic, and transmission factors explored in this paper?
