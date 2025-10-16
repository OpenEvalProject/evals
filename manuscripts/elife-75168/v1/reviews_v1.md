# Peer review - Round 1

Editors:
- Nicola Segata, https://ror.org/05trd4x28 University of Trento Italy

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75168.sa0](https://doi.org/10.7554/eLife.75168.sa0)

This paper introduces an elegant mathematical and ecological framework to model the fluctuations of microbial abundances in microbiomes along time series. The modeling approach considers consumer-resource properties and is regulated by few parameters. Applied to time-series microbiome data the model suggests the existence of recurrent patterns of microbial dynamics that are quite dependent on resource competition.


---

# Peer review - Round 1

Editors:
- Nicola Segata, https://ror.org/05trd4x28 University of Trento Italy

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75168.sa1](https://doi.org/10.7554/eLife.75168.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "Competition for fluctuating resources reproduces statistics of species abundance over time across wide-ranging microbiotas" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Sean Gibbons (Reviewer #1).

Comments to the Authors:

We are very sorry to share that, after extensive consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife. Both reviewers and the editor think that the mathemathical model proposed is of potential great relevance for the field, but despite the elegant formulation and the interesting results fo some of the analyses, quite a significant amout of additional work would be needed to address most of the reviewers' points and be considered for publication in eLife (see below). We are sorry to convey this negative decision, as we addressing the points of the reviewers most likely goes beyond the usual effort for a revision at eLife. We are, however, open to considering a substantially revised manuscript in the future.

Reviewer #1:

The authors propose a simple consumer-resource (CR) model, where the dynamics of microbial communities are governed by fluctuations in external resources and by competition for these resources between taxa. The model is elegant in its simplicity, while also being biologically intuitive and subtly clever in its implementation. The authors show how the model accurately predicts many of the macroecological patterns found in microbiome time series. Unlike many papers I've read that focus on macroecological patterns (with some exceptions), the authors do a great job connecting model parameters to measured properties of microbial ecosystems and show how these parameterizations of real-world ecosystems can provide potential mechanistic insights into the ecology of the system. I really enjoyed reading this manuscript. The writing is clear, as are the formalisms and the analyses. The model provided many expected results, but also revealed some surprising insights. This is a promising approach for generating novel hypotheses for how microbial ecosystems behave. Overall, I think this is a valuable contribution. My only caveat is that many different mechanistic models can be constructed to explain a given phenomenon -- so I suggest the authors remain somewhat humble about whether or not 'fluctuating resources' are the major drivers of these complex dynamics. They might be! The fact that such a simple model makes so many predictions is promising. But in the end, this is just one possible model among many.

Major Strengths/Weaknesses:

1) I like the simplicity of the CR model. More than this, I like the subtlety with which you handled community dynamics. Many prior studies have erroneously treated microbiome time series as if they directly represent growth curves of all the taxa in the system (e.g. fitting LV models to human gut time series). Your method simulates serial dilution and growth of microbial taxa over several cycles to approximate a steady-state community composition for each sample time point. This fits with my biological intuition.

2) One minor weakness in the data processing was that the most resolved taxonomic level that was analyzed was the family level. Why not start with genus-level? Genus-level annotations can usually be estimated from 16S reads. Another question that I had was whether or not the model assumes absolute or relative abundances? I'm guessing absolute, in which case, I found the rarefaction and renormalization of the counts to frequencies to be a slight concern. I'd suggest the authors perform a centered log-ratio (CLR) transform (or some other form of isometric log-ratio transform) on the non-rarified count data, and only remove low-frequency taxa after the transformation. I doubt this will substantially impact the results, but this is considered best practice.

3) The 'origins of distinctive statistical behaviors…' section is really great. The authors do a great job mapping their model parameters to features that can be estimated directly from the empirical time series (i.e. α-div and the β-slope constrain N, M, and S, while δ-l and s-i constrain σ and k). However, I'm not sure I understood your explanation for why low-sparsity leads to a steeper Taylor's Law slope, and how this is essentially equivalent to a competition-free mode. Naively, I'd expect competition to be greater at low sparsity, due to multiple species consuming the same sets of resources.

4) The non-interacting null model is an appropriate null. However, the authors should be humble about whether or not their competition model is capturing the mechanisms driving community dynamics. For example, direct microbe-microbe killing (antimicrobials or type VI secretion systems) is not captured. Host antimicrobials and immune-system interactions aren't captured. Diet is implicitly captured with the nutrient fluctuations. That being said, I think the model is still reasonable and the insights should be fairly robust -- the environmental fluctuations in the model probably capture a lot of this system-scale variance (in a statistical mechanics kind of way -- the averaging together of a lot of different factors giving rise to a predictable statistical outcome).

5) There seem to be two assumptions regarding time in your model. First, I think you need to be operating within a stationary/stable system (i.e. where there's no long-term drift), correct? I think that's fine but wanted to clarify. The second assumption is that you're sampling from a steady-state end-point of fast internal growth dynamics within the system. I think this is an excellent assumption in the human or mouse gut, but you might want to think about the timescales of sampling and microbial growth in the various systems you are sampling. If you are sampling within the timescales of the faster dynamics (e.g. possible for in vitro systems…maybe in the vaginal system?), how would this impact your results? You mention that your k values were between 0.5 and 1.0, suggesting that internal dynamics were faster than sampling timescales. Due to the ecological steady-state assumption of your modeling, would it be possible for your parameters to tell you that dynamics were slower than sampling timescales?

Overall, I think the authors achieve their aims and that their conclusions are supported by their results. This is an elegant and useful modeling framework that should have a sizable impact on the field and provide potential mechanistic insight into existing and future longitudinal microbiome data sets. I found many of the model predictions to be intuitive, and a few to be surprising, which is always a good sweet spot. I'd like to commend the authors on writing a nice manuscript that clearly communicates their results with a set of beautiful and easy-to-read figures.

Reviewer #2:

This paper discusses a consumer-resource model, where microbial families are considered consumers and their nutrients are resources. The model is used to simulate microbial abundances over time: batch feeding events allow populations to grow, dilutions in between feeding events reduce populations. Coefficients of the model, such as the number of resources and the rates at which each family can consume them, are fit to data from different microbiomes by comparing summary statistics of simulated and observed time series. Different microbiome time series, e.g. from mice or humans, have different summary statistics. The model can be optimized to simulate time series with summary statistics similar to each of those from different microbiome data sets.

The model is very simple, allowing the reader to easily understand what is going on. This is a strength of the manuscript. The overlap in resources consumed between consumers in this model is revealed as a crucial parameter because it exhibits the most interesting changes when fitting different microbiome data sets. However, in the model there is no trade off between the rate at which a species may consume a resource and the number of resources it can consume. Therefore, the more different nutrients a species can consume, the fitter it will be. It may be interesting to re-evaluate the major results when this assumption is changed.

A weakness of the paper is that it overstates the implications of the theoretical findings. Simulated timelines from the presented model can generate summary statistics that look like those in real data sets. This will also be possible with other models, even simpler ones or more complex ones. The article ought to include a more critical discussion and validation with simpler (e.g. pairwise interaction) or more complex (e.g. saturating growth kinetics) models.

The article is also poorly referenced, e.g. Niehaus et al. 2019 develop a resource driven model for microbial populations (doi.org/10.1038/s41467-019-10062-x), and Momeni et al. 2017 discussed the importance of resource mediated interactions (doi.org/10.7554/eLife.25051).

Finally, the article is not very carefully put together. I received two figures labeled as "Figure 1". The methods appear unfinished.

I recommend reducing the amount of fluff terms throughout the manuscript. For example, the sentence from the abstract:

"Our coarse-grained model parametrizes the intrinsic consumer-resource properties of a community using a small number of macroscopic parameters, including the total number of resources, typical resource fluctuations over time, and the average overlap in resource-consumption profiles across species"

would read fine without the ill-defined filler words:

"Our model parametrizes the consumer-resource properties of a community using parameters that include the total number of resources, resource fluctuations over time, and the average overlap in resource-consumption profiles across species."

In my opinion, simplicity and clarity strengthen theoretical papers, increasing their impact.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Competition for fluctuating resources reproduces statistics of species abundance over time across wide-ranging microbiotas" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Wendy Garrett as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Sean Gibbons (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The paper has improved with the revision and it meets the standard for publication in eLife. However, the paper is rather technical and in some parts there is the risk of misinterpretation or overestimating/over-interpreting the potential of the model. The authors should better highlight the intrinsic limitations and strong assumptions of the model throughout the paper, starting – for example – from the abstract. It is not a problem of the model or the data per se, but it is rather the way it is communicated considering that the large majority of the readership will have different backgrounds and cannot necessarily understand the limitations directly. Thus, we would like to see a revised manuscript addressing these specific issues as soon as possible.

Reviewer #1:

The authors have done a commendable job responding to the reviewer comments. The additional analyses and model simulations have greatly strengthened their work. The authors have provided their code in a more accessible format. And, they have made the suggested improvements in how they discuss their results. I have no further concerns or comments.

Reviewer #2:

My main concern remains: a simulation of timeseries is presented that has summary statistics as observed in data. Upon revision, based on my comment that this is not special to the model presented, another model is used; this also reproduces summary statistics similar to those from data. This is not a broad impact result and will, with the current narrative, be easily misunderstood by a non-specialist readership.

In my opinion, such timeseries summary statistics offer little insight and have limited biological meaning. Thus, my original opinion has not shifted much.
