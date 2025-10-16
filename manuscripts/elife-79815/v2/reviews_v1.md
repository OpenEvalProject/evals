# Peer review - Round 1

Editors:
- Petra Anne Levin, https://ror.org/01yc7t268 Washington University in St. Louis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79815.sa0](https://doi.org/10.7554/eLife.79815.sa0)

This study develops a rigorous resource allocation model for E. coli growing under steady-state conditions. Validated by comparison with a compiled data set, the model highlights the complex nature of the relationship between metabolites, growth rate, and yield which is significantly more complex than the one-to-one-one relationship that has generally been assumed. The work will be of interest not only to investigators interested in basic questions of bacterial physiology but also to those working on applied problems in biotechnology.


---

# Peer review - Round 1

Editors:
- Petra Anne Levin, https://ror.org/01yc7t268 Washington University in St. Louis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79815.sa1](https://doi.org/10.7554/eLife.79815.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Resource allocation accounts for the large variability of rate-yield phenotypes across bacterial strains" for consideration by eLife. Our sincere apologies for the delay in returning the decision.

Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

While other reviewer concerns as detailed below should be considered, the authors need to address different assumptions for ϕq in order for the study to be complete.

Reviewer #1 (Recommendations for the authors):

Proposed points of improvement.

Rationalize bounds. In Figure 2 I would like to better understand what are the reasons for the bounds. What gives the "P" shape? What are the trends with different allocation trade-offs? etc. Possibly some analytical insight is possible here [maybe with a simplified version of the model], leading to more transparent theoretical insight.

Rationalize (and show) trends. Figure 3 seems particularly uninformative. It would be much more instructive to see trends of uptake and secretion rates vs the other variables as 2D plots, compared with the model predictions (particularly for panels AB, panels CD show a complex trend, but this is precisely what I would like to get more insight on). It is not clear how the prediction of Figure 3C is produced by the model since the parameters are not fixed as the allocation changes.

Figure 4. I got lost with this figure, which was particularly uninformative to me (and graphically lacks proper labeling). Looking at the plots, I only see different degrees of agreement between the model and data. Reading the connected Results paragraph, there are a lot of qualitative considerations "under the hood" that seem very interesting but are not accessible/transparent. This could be my own limitation, and it's possible that this paragraph is accessible to a different audience (e.g. more expert than me on metabolic models). However, my impression was that this paragraph/figure could be made more accessible, although I did not gain enough access to give specific recommendations, other than giving the reader some insight on the model predicted trends that we are discussing here.

Where are the optima? In Figure 2 one can explore what the model gives if one tries to optimize (1) growth rate at fixed yield (2) yield at fixed growth rate or (3) looks at Pareto optima of both. I agree that optimization of one or both quantities may not be the goal, but still, it is important to understand where optimization would bring theoretically, and how the data points cluster with respect to these theoretical optima.

Comparison with other frameworks.

A more detailed comparison with other "reference" frameworks would be useful here.

I would propose: Erickson 2017, Basan 2015, Maitra 2015 [but other choices are possible]

[see below]

The definition of yield should be explained much more clearly in the main text, both in the model and in the data. Model: Explain why Equation 2 represents the fraction of carbon going into biomass. Data: explain how the quantity is measured and how the measured quantity relates to the model.

I am confused by some sort of implicit identification that the authors make between allocation (e.g. the fraction of ribosome making ribosomes) and partitioning (e.g. the fraction of proteins or total mass that is ribosomes). In particular, for ribosomes, I am not sure that their equations (e.g. Eq (6) in SI regarding ribosomes) are equivalent to the framework of Erickson 2017 (which I use as a reference). At steady state (the condition that is relevant for this study), this might be irrelevant, since allocation and partitioning coincide (Scott 2010), but then for clarity, it might be better to present the framework as steady-state relations (as in Scott 2010) and not by ODE.

Related to this point, or this may be the same point, I think the notation is confusing for the parameters v_x, m_x. These are extensive quantities and I am not clear how they are set. For example, v_r ~ R, which is also a necessary condition to get exponential growth (see above). I found this mentioned only on line 642 of the appendix.

Another related point, I did not understand if the model makes more or less implicit flux-balance assumptions (or more in general whether at some point it assumes relationships between fluxes). It should not but at some point, I had this impression. In general, it would be interesting to have some insight into the relationships between the different fluxes (in particular those in consecutive chains) for different values of the resource allocation vector.

Around line 240, the authors discuss that the trend in Figure 3AB is a consequence (through Equation 2) of (population average) density homeostasis (in this case across different strains growing in the same conditions, which is perhaps not the usual way this parameter is considered). Do we then need to think that the model prediction is trivial in this case [as pointed out above, seeing this section of the data and the model prediction would be very instructive here]?

Figure S1 could be presented with Figure 3 (although, see above, probably more is needed). Here one sees the points that do not agree with the model and the authors can comment on those. In particular, those outliers laying near the x-axis of Figure S1B seem potentially interesting to explain/rationalize.

Technical point: How do the predictions depend on the data point used for calibration of the model?

Other points raised after discussion with our group

It seems that the interpretation of the C sector might be different from the canonical one. c → ** Central carbon metabolites **, that is, catabolic products of the carbon source substrate (glucose, glycerol, …) taken up from the medium. What about catabolic enzymes?. Also, enzymes in amino acid metabolism, that are necessary for protein synthesis seem to end up in the R sector (?).

Not clear what the ρ are in dc/dt, and why they must be > 1.

The main result statements of the study are either quite generic or cannot be understood from the main figures. This can probably be improved by reengineering both figures and statements (from abstract):

- very good quantitative agreement between the predicted and observed variability in rates and yields, acetate flow does not correlate with the growth rate.

- resource allocation is a major explanatory factor of the observed variety of growth rates and growth yields across different bacterial strains.

- differences in enzyme activity need to be taken into account to explain variations in protein abundance.

Cmmol seems like a very unintuitive and non-standard unit. Has this been used before? Can a better solution be proposed? Does this hide something related to protein length in the different sectors?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Resource allocation accounts for the large variability of rate-yield phenotypes across bacterial strains" for further consideration by eLife. Your revised article has been evaluated by Michael Eisen (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed. In particular:

1. Please address the reviewer's request that some predictions based on the model be added to the text so the reader can better understand how the model works. (i.e. make it less of a black box).

2. To clarify the model and results and how they differ from those of Basan, 2015 please revise the text to address the differences between the results of this study and those of the Basan study in detail. (The reviewer included a list of questions that should ideally be answered in any such comparison in their review below.)

Reviewer #1 (Recommendations for the authors):

The authors made considerable revisions and provided a detailed and clear reply to all the points raised. I maintain my opinion on the fact that the work is timely and the theoretical framework is very interesting.

Having said this, I also have to say that the results remain somewhat non-transparent, as the authors were not able to derive a mathematical or qualitative rationale for the main results or analyze the model in terms of simpler one-dimensional relationships, and the comparisons with data remain non-stringent. However, they have provided additional figures and analyses that do contribute towards clarity, as well as clarifying many of the model assumptions and definitions.

I think the manuscript should appear on eLife, in view of the contribution towards rationalizing a more complex relationship between growth and yield than the simple trade-off assumed by most. If this could be the central point of this study (I find it interesting and I think it might have some impact), then I have some remarks to clarify the message.

First, the message could emerge more clearly in the abstract.

Second, it might be possible to characterize (without comparing to data, making some simple assumptions on the parameters) the variation of mu_max, y_max (and maybe also some "central values") across conditions, to study and visualize their relationship with resource allocation parameters. Perhaps these predictions are not verified or directly comparable to data (and I am not asking to perform any comparison), but they might help the reader understand how the model works (as I said I think the weakest point of this study remains the "black box" feeling about all the main results).

Third, a more stringent comparison with the data/model of Basan et al. 2015 seems important to clarify the results. What brings those authors to conclude towards a trade-off between protein cost and energy efficiency? Would the model in this study describe the Basan et al. data and how? Would this comparison lead to different conclusions? Are there crucial differences in the modeling choices of the two studies? Are there (according to the authors' model) regimes with/without strong trade-offs and how can they be characterized? These seem like questions worth addressing.
