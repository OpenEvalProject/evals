# Peer review - Round 1

Editors:
- Jennifer Flegg, The University of Melbourne Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64670.sa1](https://doi.org/10.7554/eLife.64670.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript reports on a significant update to a leading model of the burden of yellow fever and the impact of vaccination. It provides estimates of the global burden of yellow fever in 2018 and the impact of vaccination activities in Africa. This paper is of interest to a broad range of researchers and public health practitioners engaged in the management of yellow fever.

Decision letter after peer review:

Thank you for submitting your article "The global burden of yellow fever" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Jennifer Flegg as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Miles Davenport as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Alex Perkins (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Summary:

This manuscript reports on a significant update to a leading model of the burden of yellow fever and the impact of vaccination. Some of the major updates include extending it from Africa to also include South America, and accounting for model uncertainty with different combinations of spatial covariates. Some differences with this update of the model are reported and explained, and the impact of mass vaccination campaigns is quantified. This paper is of interest to a broad range of researchers and public health practitioners engaged in the management of yellow fever. It provides estimates of the global burden of yellow fever in 2018 and the impact of vaccination activities in Africa. Given the limited volume and quality of data available on yellow fever epidemiology, the modelling approach is appropriate and supports the study conclusions.

Essential Revisions:

1) Novelty.

The novelty of the method is oversold, particularly in the Abstract. It is not accurate to say that this manuscript "develops a novel framework" or "newly developed methodology" given that it is an update of an existing framework by Garske et al. The exact novelty of the framework should be made clear. Please cite the Garske et al. paper where you first mention the framework in the Materials and methods.

2) Data.

Insufficient details are provided on some model inputs. The authors should provide further details on the YF occurrence data used in the analysis. In particular, details on how cases were diagnosed, and discuss the potential impact of diagnostic uncertainties on the study results. Further details and justification should also be provided on the non-human primate covariate. For example:

– YF occurrence data. Please summarise the number of occurrence records used in the analysis by geographic region and time. Briefly summarise how occurrences of YF were diagnosed. PCR? Serology? Clinically? If serological and /or clinically diagnosed cases are included, please comment on the potential impact of misdiagnosed cases (e.g. due to cross-reactivity with other flaviviruses such as dengue) and how this may have impacted your results and conclusions.

– NHPs data. What is the difference between habitat suitability and occurrence of non-human primates? Also, I suggest that you do not refer to the species range maps provided by IUCN as "species distributions" as these are not modelled species distributions (as the authors point out in the Discussion). Perhaps refer to them as "range maps". Please clarify what you mean by "species richness". Did you count the number of species range maps covering at least 10% of each province? Which NHPs did you include and what was the justification?

– Vector data. Ae aegypti is the main vector for urban yellow fever transmission, please justify why you included Ae Albopictus as a potential covariate.

3) Materials and methods.

Some of the methods are unclear and it is not obvious which data is used to inform which model parameters. For example, it is unclear how were severe infections and deaths estimated from transmission intensity surface. Please provide details in the Materials and methods section. Consider including a workflow diagram to help the reader to follow more easily what you have done. Please justify the choice of priors (e.g. prior on force of infection seems fairly small and strong) as well as choice to sample proportional to AUC.

4) Presentation of results.

Please provide additional information to help readers understand the tables and figures without referring back to the text. For example:

– Table 1. Please add more informative column and row labels. Describe what 1s and 0s represent in the figure legend.

– Table 3. These are not all environmental covariates as the legend suggests – there appears to be reservoir and vector species included here. Please re-produce the table with more informative descriptions of each covariate and provide references.

– Table 4. Please define each parameter in the table legend.

– Figure 2. Please provide more descriptive labels for each plot.

– Figure 4. Are these estimates for 2018? Please state in the legend.

– Figure 5. Please provide more informative labels on each of the plots. Please describe what the dots and bars represent in the figure legend.

– Figure 6. Are these estimates for 2018? Please state in the legend.

The AUCs of the models are essentially all the same, in which case it doesn't look like there was much success in discriminating among them and the ensemble is essentially a simple average of the component models – can the authors comment?

Please define what you mean by "potential" deaths in the Materials and methods and/or Results section. You mention it in the Discussion, but it should be earlier. Conceptually this was a bit confusing because "potential" could be interpreted as assuming no vaccination.

5) Discussion – for the explanation for the discrepancy in force of infection spatially as compared to Garske et al. -- can we really be convinced that this is the correct interpretation (i.e., lower FOI in West Africa) or if we should consider this to be a sensitivity of the model?

6) Please discuss why you only estimated vaccination impact in Africa and not South America.

Reviewer #1:

This paper presents a mathematical estimation of the burden of yellow fever in Africa and South America, using multiple types of data. Results are presented based on ensemble model predictions. While the paper presents results of public health interest, I'm not convinced of the novelty of the approach, this is rather an extension of an existing methodology to more data and regions. For this reason, I feel like this work would be better suited in a specialist journal.

1) I'm not convinced that the contribution of this paper is novel enough for publication in eLife. The model framework was already largely in place, as was most of the data. I think the Abstract oversells the novelty of the methodology.

2) The first mention of a temporal component to the models was in the Results. I found the lack of introduction of the temporal nature of the models quite confusing.

3) What was done for serological surveys in South America, since there were none available? How were the serological data representative of the whole population? Can this be justified more?

4) It would be good to be clearer about which model parameters go where and which data is used to inform which parameters. E.g. a workflow diagram would help the reader to follow more easily what you have done.

5) Why is BIC used for model selection? That's not exactly a natural choice for Bayesian models since it does not consider the effect of the choice of priors.

Reviewer #2 :

Abstract – It is not accurate to say that this manuscript "develops a novel framework" or "newly developed methodology" given that it is an update of an existing framework by Garske et al. This issue is handled appropriately elsewhere in the manuscript, but here it is not.

Materials and methods – The prior on force of infection seems fairly small and strong. How was this choice made, and how sensitive are the results to it?

Materials and methods – For the ensemble predictions, is there a specific rationale or precedent for sampling proportional to AUC? It sounds reasonable, but also somewhat arbitrary without better justification.

Results – The AUCs of the models are essentially all the same, in which case it doesn't look like there was much success in discriminating among them and the ensemble is essentially a simple average of the component models. Am I missing I anything with that assessment?

Discussion – The explanation for the discrepancy in force of infection spatially as compared to Garske et al. is appreciated. I wonder if we can really be convinced that this is the correct interpretation (i.e., lower FOI in West Africa) or if we should consider this to be a sensitivity of the model. I'm not sure whether we can say without some sort of out of sample test of the predictions of these two models.

Reviewer #3:

Gaythorpe et al. estimated the global burden of yellow fever and the impact of mass vaccination activities in Africa in 2018. A previously published Bayesian modelling framework was extended and applied to a range of new and updated data sources. First, the authors updated an existing dataset of yellow fever occurrences (from 1987 to 2018). These data were used, along with a range of geospatial covariate data, to estimate the probability of yellow fever being reported in each first administrative region (i.e. province) within yellow fever risk zones. Measures of climatic and environmental variables and the presence of non-human primate reservoir species and mosquito vector species, among other factors, were included as model covariates. Data from a number of serological surveys was used to account for under-reporting and to estimate transmission intensity across the study region. Next, the authors updated an existing dataset of vaccination activities and used these data to calculate the number of deaths attributable to yellow fever at a province level, globally, and to estimate the number of deaths averted by vaccination in Africa. The authors estimated that in 2018, there were 51,000 (95%CrI[31,000-82,000]) deaths globally due to yellow fever, with 90% of the burden in Africa. Further, they estimated that vaccination averted 10,000 (95%CrI[6,000-17,000]) deaths in Africa in 2018. The study did not estimate the impact of vaccination in South America. The data available for studying global YF epidemiology is limited in volume and quality, which means that analyses such as the one presented here are inherently uncertain. This study considered uncertainty from estimation and model structure, but did not account for other key sources of uncertainty, i.e., in estimates of vaccination coverage or model covariates. Nonetheless, the study demonstrates a useful approach to estimating disease burden and vaccination impact over broad geographic areas. The data and approach seem appropriate to support the study's conclusions. However, in the manuscript's current state, some aspects of the analysis and model inputs need to be further clarified and justified:

1) The authors claim that they have developed a novel framework for estimating disease burden and vaccine impact. However, the study appears to make a number of extensions (e.g. incorporating new geographic regions, new covariates, updated data) to previously published methods. The authors should make the novelty of the framework more clear.

2) Limited details are provided on some model inputs. The authors should provide further details on the YF occurrence data used in the analysis. In particular, details on how cases were diagnosed, and discuss the potential impact of diagnostic uncertainties on the study results. Further details and justification should also be provided on the non-human primate covariate. For example, which NHP species were included and why.

3) The authors should provide information on the data and approach used to estimate the number of severe infections and deaths from the estimates of transmission intensity.

4) The authors claim that they developed a novel framework. However, the work appears to make a number of extensions (e.g. incorporating new geographic regions, new covariates, updated data) to previously published methods. Please make the novelty of the framework more clear.

5) Limited information on the model inputs are provided in the Materials and methods section. Where the authors point to previously published methods or dataset, they should at least provide a brief summary of the method/dataset. For updated or new datasets, more detailed descriptions should be provided. For example:

– YF occurrence data. Please summarise the number of occurrence records used in the analysis by geographic region and time. Briefly summarise how occurrences of YF were diagnosed. PCR? Serology? Clinically? If serological and /or clinically diagnosed cases are included, please comment on the potential impact of misdiagnosed cases (e.g. due to cross-reactivity with other flaviviruses such as dengue) and how this may have impacted your results and conclusions.

– NHPs data. What is the difference between habitat suitability and occurrence of non-human primates? Also, I suggest that you do not refer to the species range maps provided by IUCN as "species distributions" as these are not modelled species distributions (as the authors point out in the Discussion). Perhaps refer to them as "range maps". Please clarify what you mean by "species richness". Did you count the number of species range maps covering at least 10% of each province? Which NHPs did you include and what was the justification?

– Vector data. Ae aegypti is the main vector for urban yellow fever transmission, please justify why you included Ae Albopictus as a potential covariate.

6) How were severe infections and deaths estimated from transmission intensity surface? Please provide details in the Materials and methods section.

7) Please define what you mean by "potential" deaths in the Materials and methods and/or Results section. You mention it in the Discussion, but it should be earlier. Conceptually this was a bit confusing because "potential" could be interpreted as assuming no vaccination.
