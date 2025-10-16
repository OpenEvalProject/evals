# Peer review - Round 1

Editors:
- Thomas S Churcher, Imperial College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67018.sa1](https://doi.org/10.7554/eLife.67018.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This paper nicely highlights the huge amount of data needed to understand the complexities of vector borne disease transmission and control. It produces an elegant framework to rigorously bring together disparate sources of data from multiple hosts and vectors and the results give clear policy relevant results for the control of Ross River Virus in Brisbane.

Decision letter after peer review:

Thank you for submitting your article "Physiology and ecology together regulate host and vector importance for Ross River virus and other vector-borne diseases" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Miles Davenport as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Gregory Albery (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

The manuscript represents a considerable body of work and brings together disparate sources of data in a single framework for understanding the relative importance of different vector and host species. This is a welcomed approach to allow the relative contributions (and importantly, the relative uncertainties) to be explicitly investigated.

Essential revisions:

1 – Title should be revised. Though I would agree that physiology and ecology regulate other vector borne diseases this is not shown in this manuscript. The authors should therefore consider removing "and other vector-borne diseases" from the title.

2 – Could the authors explain the rationale for using the ranking framework over something more quantitative such as the use of the basic reproduction number (R0). Ranking systems have the potential to hide considerable nuance, especially when parameterisation is unclear.

3 – The authors mention many of the uncertainties in the discussion, but this is largely ignored in the abstract and results where point estimates which rely on small sample datasets are presented (see comments 1.1 and 1.2 in particular). Given the inevitable lack of good quality data to parameterise the model uncertainty is always likely to be underestimated. Nevertheless, it would be great if the uncertainties could be more fully reflected, including statistical analyses if these were thought to be appropriate. Reviewer 1 highlights that this could be done in a single Bayesian framework. If this is not possible perhaps a figure (along the lines of Figure 1) highlighting the uncertainty of the result would be appropriate. Either way, the abstract and conclusions should be tempered to reflect this.

4 – The model appears to be parameterised for an endemic setting but the multigenerational model highlights invasion dynamics. Why were generations 1,3 and 5 chosen to highlight? The authors state that vector control is conducted in Brisbane to control the disease though this doesn't appear in the parameterisation. Why was this the case and would it not influence the conclusions i.e. it is more likely to target anthropophagic vectors so could reduce their importance.

5 – The paper could be shorted substantially given some of the repetition in the introduction and discussion (a ~10% reduction should be easily possible). Could the authors also considering adding a few sentences of to the results very briefly outlining the methods used in each section (see reviewers comment 2.1).

Reviewer #1 (Recommendations for the authors):

The manuscript proposed an interesting approach for an important and famously hard problem. There was much I liked about it, such as approaching the vector-host system in both directions for investigating the complete transmission cycle. I also like the attempt to integrate different sources of data and the results figures were very clear. However, I found the manuscript poorly written (too long, repetitive and not very clear) and there were important gaps in the description of the data that raised concerns about the validity of the methods and strength of the results. I expand on this and provide other suggestions below.

Major concerns (gaps in data and methods description)

1.1 – Methods. It would be important to add statistical support to the results. In particular Figure 2 and 3. Without it the rank results are based on visual observations but with the confidence intervals overlapping so much, they are only very weakly supported. To me, in most cases there is no "winning" host/vector. Humans also have such wide confidence intervals that strong conclusions about it are difficult.

1.2 – Samples sizes. There are no mention of samples sizes. These need to be added for all data. It is particularly important to determine the validity of some results, for example:

– Are the points in Figure Sm3 the data points for vector competence? If so, how can a model be fitted to a single data point and the uncertainty in the predictions is not even wider than for other species with more data? Same seem to occur in Figure Sm5.

– How many bird species and are their competences not variable?

1.3 – Origin of data. Where and how each data type was obtained is never explained. This needs to be clarified for all data. For example, the metric used for physiological competence are titers but how they are obtained?. I assume these are viral titers from titration assays and not PCRs. Are the assays equally sensitive for all species? Are they from vertebrate blood samples and vector saliva? Where do these data come from? Provide references. Perhaps a data section would be helpful.

1.4 – Parameter values. There are multiple assumptions/values that seem taken from literature included in the models that are never described/explained. E.g., infectious period of each host, host abundance, expected average number of infections etc. I appreciate that some data have been previously described, such as vertebrate abundance but a summary here would help understand some of the differences in the results e.g. weighted and non weighted AUCs. Perhaps expansion of Table 1.

1.5 – The use of the term "reservoir" for vector-borne diseases is more confusing than helpful. Who is the reservoir, the vertebrate host or the vector? Maintenance and transmission can't happen without either. Is the complex host-vector the reservoir then? I would suggest avoiding this term throughout for clarity.

1.6 – The first part of the introduction (first 5-6 paragraphs) is mostly redundant and ends up being a repetition of itself and the discussion. Could be reduced to a single paragraph and then straight to the RRV case study, which is an interesting system in itself. The wide applicability of the method is much better explained in the discussion.

1.7 – Figure 1. I didn't find this Figure helpful. On the contrary. It has too many elements that are too small to be visible and understood. Are the graphs from real data or are they make up curves and numbers? I agree that it would be useful to understand where each type of data was used for each step and what model was applied to it. But this Figure is not helping me with that. I would suggest a simplified version, for example in a diagram or schematic without images but that explains the framework, perhaps more like a workflow.

1.8 – Throughout the manuscript the authors mention "the model" to refer to the methodology or framework they develop. This is confusing because there are many models within 'the model' and the model is not actually a model per se… I suggest updating this terminology for clarity.

1.9 – The results seem to fully hang on the definition and estimation of physiological competence. The implications should be well explained.

1.10 – Why was "study" not included as random effect in the models?

1.11 – Why do a single Bayesian model for the mosquito feeding behaviour but not for the other models, and why leave out the rest of the transmission cycle? The approach is piece-meal like with multiple predictions from different GLMMs that are disconnected with one another and their summary statistics are put together at the end. Could these be put into a single Bayesian framework that allows uncertainties and data be propagated throughout the different model components?

1.12 – Bayesian model not defined, what was the likelihood and the priors? Provide reference for priors too.

1.13 – With the size of the human confidence intervals, can we make any statements about the role of human to community transmission?

1.14 – First paragraph of discussion is repetition of introduction.

1.15 – Table S1. Add disease associated with study.

1.16 – Data does not seem available in the GitHub and the model codes need to be organised. Is the Bayesian model missing?

Reviewer #2 (Recommendations for the authors):

The work presents a formidable amount of data and I particularly liked the distinction between half cycles and full cycles, and the explicit differentiation between physiological competence and exposure/behavioral processes. The finding that physiological competence may not align with epidemiological salience is an important one for vector-borne pathogens in general, and a useful lesson going forward. The paper falls short a bit on its description of the modelling process in relating them to the results, and the novelty of the finding that physiological competence does not fully explain epidemiological importance needs to be clarified, but overall this is a solid and useful contribution. The following points should be addressed

2.1 If the paper is going to be in results-first format, the results need a bit more description of the models to facilitate understanding. I found myself wondering how exactly these results were being produced, and needing to flit back and forth from the results to the methods, which isn't ideal. Including the right level of detail (i.e. without recapitulating the methods) is tricky in a results-first Results section, but I think this paper could definitely do with including more information. A few sentences at the start of each section giving a bit of background on the model formulation and how the answers were produced would do the job.

2.2 The models are doing a very heavy lift here (particularly the NGM's), and I appreciate the authors' decision to include model limitations fairly prominently in their discussion. I have no personal experience with models like these, but they appear to have been conducted well.

2.3 Although the authors' reference to host species' ecology as an important determinant of their epidemiological role is useful, the discussion particularly could do with zeroing in more precisely on what aspects of the hosts' ecology are driving the disparity between physiological competence and epidemiological importance (i.e., behaviors, vector biting preferences, and population dynamics). The findings in the paper are definitely novel, but without clarifying what might be going on to drive this disconnect there's a risk of reinventing the wheel of behavioral competence a bit. These processes are all decomposed in Cynthia Downs and colleagues' 2019 competence paper in Trends in Parasitology (for example), and I think the paper should be a bit more explicit in the introduction and discussion that there are well-appreciated reasons that we might not expect physiology to paint the whole picture of competence. For example, it is relatively unsurprising that very rare hosts are epidemiologically unimportant in the system irrespective of their physiological competence. Is it possible that humans' role in these dynamics could be reduced to "there are lots of humans, so they end up being important"? The fact that physiological competence is only one component is in the introduction (lines 54-58), but a more detailed outline of the traits (behavioral and demographic) that could override it is necessary. This will then set the stage for the findings of the models.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Physiology and ecology combine to determine host and vector importance for Ross River virus" for consideration by eLife. Your article has been reviewed by 1 peer reviewer, and the evaluation has been overseen by a Reviewing Editor and Miles Davenport as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The revised manuscript is much clearer and nicely highlights the huge amount of data needed to understand the complexities of vector borne diseases. We feel that the article is very close to being acceptable for publication but would like to clarity on points 4 and 5 highlighted by Reviewer #1 below before we proceed. This would allow clarity on the fitting process and would improve interpretation of the titre data (no changes needed to model, just discussion). When preparing the final manuscript, the authors are encouraged to consider the other points highlighted below by Reviewer #1 which could provide further clarification to the reader.

Reviewer #1 (Recommendations for the authors):

The authors seem to have put a lot of thought in the revised manuscript and have addressed most of my concerns well. Thank you. However, this is a very dense manuscript and I still find the methods confusing in places.

1 – Figure 1 is much more informative now but perhaps could be expanded to also provide an indication of the type of model used in each parameter to show the workflow.

2 – On previous comment 1.1. I appreciate the revisions and the more honest presentation of the results. All much clearer. I also welcome the explanation of propagation of uncertainty, this is an important feature that I have missed. One of my key points here though was that regardless of how uncertainty is estimated, a formal quantitative way of comparing the densities estimated (such as z-test, Wilcoxon or Kolmogorov tests?) could strengthen the outcomes.

3 – On previous comment 1.11. I don't agree with the reasons mentioned for not using a single Bayesian model instead of the piece-meal approach – 2/3 are considered advantages of Bayesian modelling and the less-friendly approach is debatable (indeed the framework proposed in this manuscript does not seem very user-friendly for empiricists either). That said, although I would approach it differently, I cannot say it is incorrect – though I raise here the concern about how Bayesian and ML-type outcomes are combined in the NGM. The outcomes of a Bayesian model are fundamentally different from those so-called frequentist approaches. All your parameters are 'frequentist' apart from feeding behaviour. Are these being incorporated in a comparable way?

4 – Titre profiles. I have two standing concerns with these. Not sure if problems or if they just need to be explained and discussed.

4.1. Titration values tend to be highly variable within species, let alone between species. Given the small differences in the results, how confident can we be in that the results are meaningful at the ecological scale used?

4.2. The analysis are based on peak titre but considering the different profiles this could be problematic. E.g. in the example shown (Appendix 2 Figure 7: A) where one species has a marked high peak and the other has a constant titre lower than the peak of the other species. How can we link this to an infection/transmission probability? Especially the short time frame of the experiments.

5 – Appendix 1 Figure 4: Still don't understand how these curves are generated. I appreciate that a baseline curve is being generated from all the data combined (all studies and species). But then how can you differentiate among species. A species random effect is added but, on most occasions, there is 1 transmission value for 1 time point for a single species. Did the model pass validation diagnostics? There is also some confusion with the use of dose: the legend first mentions that dose was used as a fixed effect and then a few lines down says it couldn't be used as fixed effect. This also raises issue about the meaning of the transmission probability, especially post ~15 days as all is driven by a single species (no data for all others).

6 – Appendix 1 Table 1: swap word 'reservoir' for 'host' to be consistent with main text.

7 – Figure 2 add sample sizes from each species.

– L98-100. cattle, horses and flying foxes seem all pretty similar to me
