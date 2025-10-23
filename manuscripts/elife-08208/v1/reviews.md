# Peer review - Round 1

Editors:
- Wenying Shou, Fred Hutchinson Cancer Research Center, United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.08208.016](https://doi.org/10.7554/eLife.08208.016)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled “Predicting the dynamics of microbial communities using genome-based metabolic models” for peer review at eLife. Your submission has been favorably evaluated by Naama Barkai (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

This manuscript presents (a) a computational pipeline for calibrating genome-scale models of metabolism through fitting to experimental data and (b) the application of calibrated E. coli models to the study of a previously published evolutionary experiment, in which two mutants were found to coexist, after outcompeting the ancestral strain. What have we learned? From the point of view of this biological system, this paper provided yet another piece of data to the many already existing that the niche for FS emerges after the SS rise in frequency, but does not go to fixation. This has been known for quite a while, but it is nice to see the model agree with this finding. The calibration of individual genome scale models prior to studying communities seems a nice addition to existing frameworks, in fact one that should become a standard approach, whenever possible, for ecosystem-level modeling. The modeling and calibration software developed by the authors seems very well documented.

Shared major concerns:

1) Your paper did not explicitly compare model predictions with experiments. We would like to see a comparison of predicted metabolic and population dynamics with experimental coculture dynamics. There are no new experiments to test any predicted effect of perturbations. To at least test that FS can't invade alone is totally easy. Presumably one could also find an acetate concentration that would have been high enough to obviate the need for SS to come first (or a shorter duration or larger dilution that would have left enough acetate by the time of the transfer to have had the same effect). Another major prediction – that was pretty cool – is that acetate is excreted during a short window of time. This would be an excellent experiment to validate the model's predictions. Finally, you have to actually show us the comparison of predicted fluxes and mRNA that is supposed to be such a great fit. If it really is that good, we'd be rather impressed, for there is a huge literature about how this is not the case.

2) MCM seems to be sold too hard and does not responsibly acknowledge other DFBA platforms for communities like COMETS that do nearly everything mentioned here except the statistical fitting of parameters. We rather like that extension, but it seems to be advertised as more than it is.

3) Given that the authors propose their approach as broadly applicable to studying microbial communities, we think it may be important for them to comment on the realistic applicability of the method beyond E. coli wild type and mutants, or other well-annotated models. Would their method be useful, for example, for improving models that lack precision not just at the level of uptake kinetics, but at the level of the stoichiometry itself?

Specific major concerns:

Reviewer 1:

1) I don't understand Figure 3. If SS released acetate under oxygen limitation (∼1/4 day after daily dilution, Figure 3 i,j), then why should acetate be accumulated that quickly – immediately after daily dilution (Figure 3f)?

2) The Introduction should clearly discuss where the field stands currently and how MCM pushes the field forward. I am not sure how, for example, COMETS of the Segre group could have predicted the spatial-temporal dynamics in microbial communities if they had not somehow calibrated their model. Only after I talked to an expert did I realize that usually parameter choice is done through looking for values in literature, which leaves a few tunable parameters. Then, parameters are adjusted manually to fit experimental dynamics. This is because some of these parameters may not be directly measured experimentally. A thoughtful discussion on this will be helpful.

3) The end of conclusion mentioned that parameter estimation does not necessarily require monoculture measurements. This is a critical point, and should be formally demonstrated (rather than hidden in a supplementary file). For example, the authors could model the three-member community with parameters derived from cocultures of two members starting at arbitrary initial compositions. This is to mimic cases (e.g. soil microbes) where many species are not individually culturable.

4) The flow of the paper is suboptimal, especially to an outside reader. For example, you can move “MCM overview” to immediately after the Introduction. You may also want to add concrete examples to your figures to demonstrate how MCM works in reality.

Reviewer 2:

1) The novelty of this work is mainly in the combination of different approaches and data, rather than in the approaches and data themselves. I find fascinating that the model recapitulates the observations, and that model-predicted fluxes are consistent with previously measured gene expression data. However, it is not clear to me what aspects of the insight provided by the model were not known or suspected before, given that extensive work was done on this system.

2) As mentioned above, I like the calibration approach. However, I think that some important information is missing. First, there should be a table (fine as supplementary) detailing the values of fitted parameters, and any available comparative values from the literature (only a few examples are provided in the Methods section). Also: is the fitted ATP maintenance the value for the non-growth associated maintenance, or the coefficients of growth-associated maintenance? Second, it would important for readers to know whether the solutions found by the fitting algorithm are unique, and how sensitive the result are to parameter precision. Sensitivity analyses are discussed in the user manual, and seem to have been applied to a different microbial community. I think it would be particularly important to know whether the main result of stable coexistence is sensitive to the choice of fitted parameters.

Reviewer 3:

1) The text reads that “these observations are in exact agreement with microarray transcriptional profiles”. Given the strength of “exact agreement”, I was very surprised that there was no display of experiment versus model. This was a major finding, but no figures or statistical analysis of what “exact” means.

A related point: it is claimed that “MCM also makes predictions about gene densities” because each flux is associated with an enzyme. This is actually a fairly ludicrous claim. There have been paper after paper showing that, not only can there be a lack of correlation between flux and enzyme activity, they can even be negatively correlated. This is a central tenet of Metabolic Control Analysis, and has been well documented and commented upon by folks such as Dan Fraenkel (2003, Current Opinion in Microbiology) and Hans Westerhoff (Rossell et al., 2006. PNAS). This possibility must be addressed to make the reader aware that there should never be the assumption that flux is proportionally related to enzyme levels for all enzymes. If that were so, every enzyme would have a control coefficient of 1, which is absolutely impossible because the sum of control coefficients from the entire cell is 1.

Returning to the point above, then, if there really is a good quantitative correlation between the array data from the Le Gac work and the DFBA model here – for matching timepoints as the mRNA was harvested – it would be quite a nice finding. This analysis is absolutely essential to the paper.

2) An advance stated is MCM itself. I am not sold upon exactly how this is really a major advance beyond a variety of other DFBA approaches, including prior work on communities. For example, a very large number of MCM features that are described in a way that comes across as them being novel also exist in COMETS (2014, Cell Reports). At the very least, acknowledge where this is so, and use it as an opportunity to more precisely say where this goes above and beyond. For example, I like the inherent fitting of data and perhaps more could be made of exactly how this works. COMETS does not use fitting to each substrate, and frankly an objective means to parameterize when canonical parameters fail to work well is a nice step.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled “Calibration and analysis of genome-based models for microbial ecology” for further consideration at eLife. Your revised article has been favorably evaluated by Naama Barkai (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Reviewer 1:

For this to be a useful Tools and Resources article, I'd still like to see a discussion on MCM's limitations and requirements in the main text. For example, what is enough data for calibrating a model? Under what situations will MCM give you several solutions and what do you do in this case? What should be avoided or advocated when using MCM? You probably discussed these in the manual, but it will be helpful to summarize the main points in the text.

Reviewer 2:

The authors have overall addressed my concerns, partially by answering the issues raised, partially by transforming their work into a Tools and Resources article.

There are still two points that need some revision:

1) Even if biological insight is no more the main focus of the paper, I still think that the authors could explain a little bit in the Introduction why people may care about the specific example they study. For example, I like the following rebuttal of the authors to one of the questions: “While most of the results have been found experimentally over the course of several years, it is only now that a mechanistic model has managed to unify many of them in such a clear, unambiguous and synergistic manner. These modeling results provide very strong credence to a large body of experimental work that was done in our lab over the course of roughly a decade.” I think that a slightly expanded version of this text would help orient the broad readership towards understanding why their example is interesting (in addition to the fact that it works).

2) Most importantly, I think that in talking about their software, as well as previous tools, the authors should be very careful to clearly distinguish between features that ere possible (currently or in principle) in the different tools, vs. features that are actually presented in detail and tested in the manuscript. I am referring in particular to the last paragraph in the subsection “Model”, which is quite problematic in a number of ways. For example, regulation (both allosteric and transcriptional) in FBA models is notoriously a very tricky, overall unresolved problem. MCM has the potentially useful feature of allowing users to set rules to limit fluxes as a function of other parameters. This feature, described in one page in the user manual, is oversold in the main text as a capacity of MCM to include regulation. Similarly superficial is the description of the inclusion of phages in the model. Again, this is described shortly in the user manual with no justification or testing. All these features are unnecessarily used as a way of contrasting MCM with previous software, leading to unjustified conclusions, e.g. that COMETS “offers limited model versatility in terms of uptake kinetics” (COMETS does allow different parameters for different molecules and organisms, even if parameters were chosen to be equal in the specific simulations presented in the COMETS paper), that COMETS “seems limited to Petri dishes”, whereas “MCM can be used to understand the dynamics of realistic microbial communities, ranging from the soil or groundwater to artificial communities and bioreactors”. Both COMETS and MCM, after all, were based on the same underlying modeling framework, and tested on laboratory systems. I think the authors should definitely mention (with added accuracy) – perhaps in the Discussion – the additional features of their software that are not described and tested in detail in the main text. At the same time, I think they should limit their claims of major innovation to the components that are actually tested and presented in detail. The capacity to perform calibration on individual organisms, followed by proof of predictive capacity of the global dynamics on a highly interesting system is elegant and brilliant, and I think it is unnecessarily weakened by these other dubious claims.

Reviewer 3:

First off, I strongly agree with Reviewer 2's comments above. They have done much to improve the paper to show more and fix much of the language. As noted, however, saying why this matters in the paper as well as they did in the rebuttal would be great, and they still need to back down from hyping a large series of bells and whistles that may be great features but are not demonstrated here. There are plenty of nice advances in their method and they should stick to these.

As for my own concerns, the direct comparison to data and clarification that expression and flux should not be expected to perfectly correlate is a massive relief. The qualitative agreement is not bad in Figure 6c and d, and can rest on its own laurels. The figures are also particularly improved in their clarity.

I still find the concept of an “average flux” over such a dynamic experiment to be strange, but at least it is now explained. Using the same time point as the RNA data is far better.
