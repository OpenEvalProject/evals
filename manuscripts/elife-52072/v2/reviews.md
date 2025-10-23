# Peer review - Round 1

Editors:
- Anna Akhmanova, Utrecht University Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.52072.sa1](https://doi.org/10.7554/eLife.52072.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper provides an interesting analysis of the climate and environmental factors driving the vector occurrence for Chagas disease, a tropical disease that is transmitted by insects of the Triatominae subfamily and affects several million people worldwide. The topic and the results of this research are relevant, novel and with important public health implications for a global vector surveillance effort.

Decision letter after peer review:

Thank you for submitting your article "Modelling the climatic suitability of Chagas disease vectors on a global scale" for consideration by eLife. Your article has been reviewed by Neil Ferguson as the Senior Editor, a Reviewing Editor, and two reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Zulma Cucunubá (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper provides an interesting analysis of the climate and environmental drivers of Chagas vector occurrence, and comments on the implications for surveillance.

Both reviewers found the paper of interest but identified major limitations which need to be addressed. Given the nature of some comments, acceptance of a revised manuscript is not guaranteed.

Essential revisions:

Refer to the full reviews for details but the following are the most critical issues:

- the source data – both reviewers comment that it is not very current. More recent occurrence data should be included if at all possible. Why was the Cecarelli, 2018 dataset not used? More detail on the data is also needed (see reviewer 2).

- pseudo absence points – comments of reviewer 1 need to be fully addressed, including the lack of absence points in the validation dataset.

- validation set – data from only one species was used (see reviewer 1) – again, the rationale for this needs to be given, and I would prefer to see spatially stratified model selection and cross-validation used (e.g. spatial block bootstrap).

- model choice and settings used – these need to be justified and sensitivity analyses undertaken (see reviewer 1). In general, more detail of the modelling (including the ensemble approach) is needed – see both reviews.

Reviewer #1:

Overall, an interesting topic with some relevant approaches applied. Currently some serious lack of detail and rigour in the modelling approach that prevents this from being a valuable addition to the literature and may not be feasible to address in reasonable timescales. This makes the results and their significance difficult to interpret.

Essential revisions:

The occurrence data from these models come from a single source published in 1998 (Carcavallo et al., 1998). Surely there must be more up-to-date data on occurrence of these species? Particularly with the advent of services like GBIF (which the authors cite for one species). The robustness of these maps could be substantially improved if more modern data were included.

The "validation set" is comprised of data from a literature review for Triatoma rubrofasciata and appears to cover a more modern time period (citations dated 2006-2009). Why was this only done for one species? Doing a prospective evaluation of the ENM is certainly one approach, but the limitations of this validation approach should be explored, e.g. confirmation bias (are people just doing surveys in areas where the atlas indicates presence?), important changes in the distribution over time, etc, etc.

Pseudo-absence and lack of absence data in validation set. The choice of random pseudo absence generation when combined with non-systematically sampled occurrence data is problematic for both accuracy metrics and overprediction and has been discussed at length (e.g. Chefaoui and Lobo, 2008) – effectively it means you map surveillance effort not occurrence of the species. I don't think random pseudo absence data is a suitable choice for this approach given the variable surveillance effort. Also including Arctic and Antarctic areas and generally areas that are a long way away from presence points is a good way to artificially boost your AUC – is anyone really hypothesising that these species can spread to these regions? The lack of absence data in the "validation set" is also problematic and leads the models to prioritise sensitivity over specificity. Arguably this should be the other way around as the primary use for the maps is to target surveillance to areas where importation may be a problem. The authors should consider a more nuanced approach to absence data. Could occurrence points for other species be indicative of surveillance effort?

Subsection “Species distribution modelling”, "All algorithms were run with default settings" – these are a complex set of methods with a large number of tuneable hyperparameters. I'm not sure it is a fair comparison to just leave them with default settings, nor is it a good way to optimise fit. I'd like to see a clear rationale for why these classes of methods were chosen, relevant choices for hyperparameters and ideally some experiments to validate these choices.

Reviewer #2:

The manuscript reports a niche modelling predicting the global climatic suitability of eleven triatomine species (competent Trypanosoma cruzi vector).

The topic and the results of this research are very relevant, novel and with important public health implications for a global vector surveillance effort, especially regarding Triatoma rubrofasciata. The paper also provides a comprehensive discussion. However, the manuscript lacks some methodological details to help the reader understand how the analysis was conducted and which are the limitations and implications of both the methodological approach and therefore the results.

Occurrence records:

The section describing the data should be extended. I acknowledge the authors have used a dataset of 4155 unique points, most of them already collated by other authors (Fergnani et al., 2013) who in turn extracted the data from another publication (Carcavallo et al., 1998). But some basic information is needed in order to assess what the dataset encompasses.

Was there any quality control used for data extraction?

Are there any concerns about biases in data collection?

Did the data undertake any time standardisation?

What are the potentials concerns of not having occurrence data beyond 1999 for the American triatomine species?

It would be important to have a figure showing the distribution of the data points per species, even if it is just on the Supplementary materials.

Very important, some of the authors from the main source of information (Fergnani et al., 2013), published a data paper (Ceccarelli et al., 2018) with 21815 georeferenced triatomine records updated until 2017. What are the implications of using (or not using) a more updated dataset like this one?

Results section:

I acknowledge this is a prediction effort at a global scale, but I found hard to understand how the model predicts about 70% of climatic suitability for some species across very large areas that include the highlands (above 2500 MAMSL) in South America (i.e. R. prolixus or P. geniculatus in Bogota). This even considering the model does not include a climate change scenario. Also, when compared to previous publications on climatic suitability in the Americas I found concerning differences for some species such as R. prolixus in Colombia (Parra-Henao et al., 2016) or P. megistus in Brazil (Gurgel-Gonçalves et al., 2012).

From the maps it seems this work tends to predict a much larger distribution of some of these species in the Americas than previous works did. Not having high resolution maps and the absence of country boundaries makes it harder to tell about potential problems in the predictions at a smaller scale.

It is interesting to see that although for some species the number of records is very scarce (i.e. Rhodnius ecuadoriensis n = 31) the AUC values are still very high. There is no mention about the limitations regarding the data on the Discussion section.

On Figure 1A 'consensus model' is mentioned. But the basic details about this model have not been mentioned on the Materials and methods section.

Discussion section:

The authors mention "we were able to divide the considered species roughly into three groups dependent on their climatic habitat preferences". I did not find clearly which are those three groups and which were the methods to identify them.

To put this work into context, it would be important to include a discussion point about the highly effective vector control and other factors (i.e. housing conditions) that would potentially determine environmental suitability, beyond the climatic suitability.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Modelling the climatic suitability of Chagas disease vectors on a global scale" for consideration by eLife. Your article has been reviewed by Anna Akhmanova as the Senior Editor, a Reviewing Editor, and two reviewers. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. In recognition of the fact that revisions may take longer than the two months we typically allow, until the research enterprise restarts in full, we will give authors as much time as they need to submit revised manuscripts.

The reviewers agreed that the paper has been substantially improved, but also identified some remaining points that need to be addressed. No collection of new data will be needed to address reviewer comments.

Essential revisions:

1) Please add additional detail about the data used, how they were extracted, curated and filtered prior to analysis to the Materials and methods section of the manuscript.

2) Running the models with default parameter values only – both reviewers felt this point was insufficiently addressed. Please conduct further dataset-specific analyses to support your choice of model parameters.

3) Please review the manuscript figures to make it clearer how well the model prediction matches the data and be more explicit how uncertainty was calculated and represented and include this in the main text when discussing findings.

Please see below the individual comments from each reviewer for a more detailed explanation of issues related to each of the above points. All reviewer points will need to be addressed point-by-point in your revised submission.

Reviewer #1:

I'd like to thank the authors for their detailed responses and additions to this work in regards to the majority of my points raised. I think all but one of these have now been adequately addressed. On point 6 [running models with default parameters only] – I don't think this particular comment has been addressed. Suggesting that such parameters have been "optimised by the biomod2 development team" is not realistic given the breadth of problems that these algorithms are applied to. To take one example, in the documentation for GAMs in the "mgcv" package (that biomod2 calls) there is extensive advice on basis dimension choice for smooths and the explicit statement "The choice of the basis dimension (k in the s, te, ti and t2 terms) is something that should be considered carefully" and a range of model diagnostic statistics and plots are suggested to tune such parameters. This is one example of many and, as a reader, I do not have great confidence in the work if some of these model flexibility parameters are not at least explored. What makes the issue worse is that a reader currently has no way of diagnosing what impact this oversight might have as there are no model coefficients or effects plots presented in the manuscript. I appreciate that this is a common oversight in many ML modelling applications, but even a basic sensitivity analysis would be a big improvement over using the default values.

Reviewer #2:

I acknowledge the authors have made substantial improvements to the original version of the manuscript following the reviewers' recommendations. The modifications imply a remarkable change on the original predicted distributions. However, some considerations in terms of the methodology and the presentation of the results remain.

About the data:

My main worry is that the methods section remains limited in the details and particularly in terms of the data that has been used, which makes very difficult to understand all the work that has been done. I suggest the authors consider adding a sub-section on the Materials and methods section dedicated exclusively to explain where the data come from.

For example, the authors mention as data source the "Atlas of Chagas disease vectors in the Americas (Carcavallo et al., 1998) which were digitised at a 0.1o x 0.1o resolution by Fergnani et al. (2013)". What does exactly "digitised" mean? Is it Fergnani already a modelling work on the Atlas data? What is the difference between Carcavallo and Fergnani data? This becomes even more important as Carcavallo is a book with restricted access so that it is difficult to trace the original source.

This is further confusing later when the authors cite Supplementary file 4 as the occurrence data, citing Carcavallo and not Fergnani.

In subsection “Occurrence data” they mention that "In total, 4155 unique occurrence points were collected ranging from 31 for Rhodnius ecuadoriensis to 1180 for Panstrongylus geniculatus (Table 1)." Were these points collected by the authors? This is somehow contradictory to the use of already collected data from Carcavallo/Fergnani.

Further on the same topic, the authors mention on their reply to the reviewers that they have "We carefully compared both datasets and plotted them in ArcGIS. It turned out that the Ceccarelli as well as the GBIF occurrence records are completely covered by the Atlas data". This should be explicitly mentioned in the Materials and methods section and the comparison map added as supplementary information.

Also, the authors mention (subsection “Occurrence data”) that "Additional global occurrences of Triatoma rubrofasciata from an intensive literature search were used". However, in the Materials and methods section there is not mention to the details of the review process followed to obtain such data (which databases, which quality control, which languages, which temporal filter they have used, etc). If the data for Triatoma rubrofasciata is used as data points, how different is the methodology for this species compared to the other species?

About the statistical methods:

In subsection “Species distribution modelling”, the authors mention "All algorithms were run with default settings except for MAXENT, GLM and GBM." In response to a reviewer's comment about what those default setting imply, the authors mention that "We have carefully examined the different parameters and changed the information criteria for the stepwise selection procedure in GLM to 'Akaike Information Criteria (AIC)' and the number of terminal nodes in GBM to 6 as it is recommended by Friedman (2002)". I believe the reasoning behind the "default settings" has not been clarified yet.

About the Results section and Discussion section:

In Supplementary file 4 there is not needed to show the background colours but simply the distribution of the data. The background does not really help to see the data.

Could you please explain why in the Global validation it was possible to estimate sensitivity but not specificity for T. rubrofasciata?

In the Results section it is mentioned several times some agreements and disagreements between the model and the data for various species. For example, in the Discussion section "the models appear to slightly overestimate the potential distribution as it could be noted in the modelling of T. dimidiate". However, it is actually hard for the reader to note exactly where these potential overestimates are occurring. It will be great if you can have a figure (even if it is a set of figures in Supplementary file) where you show both the model predictions with the occurrence data on top so the reader can judge and understand where the model is fitting well and not that well, as you have done for T. rubrofasciata on Figure 2.

In Figure 1 (and also Figure 2) it is mentioned that "Hatched areas indicate regions where the projection is uncertain". There are two problems with this uncertainty:

- The size of the panels makes the figures so small that it is impossible to actually see the hatched areas.

- What does it mean "uncertain"? It should be clearly explained in the Materials and methods section how such uncertainty was estimated. Is there a metric for such uncertainty?

These problems with showing uncertainty in both Figure 1 and Figure 2 could be solved by having other similar figures exclusively for uncertainty.

To avoid confusion, I encourage authors to use a more cautious language when referring to climate suitability rather than actual presence of a particular species. For example in subsection “Potential distribution under current climate conditions” they mention "T. brasiliensis prefers dry and wet savannah climate as found in eastern Brazil and southern West Africa, northern and southern Central Africa and East Africa". But, in reality T. brasiliensis hasn't ever been found in Africa.
