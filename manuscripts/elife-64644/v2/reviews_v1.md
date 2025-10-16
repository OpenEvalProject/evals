# Peer review - Round 1

Editors:
- Upinder Singh Bhalla, Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64644.sa1](https://doi.org/10.7554/eLife.64644.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

It is interesting how a few molecules, such as the protein kinase ERK, act as a convergence points for multiple pathways in synaptic plasticity. In this study the authors show how ERK not only acts like a hub for many inputs, but also selectively responds to different time-patterns of inputs depending on which combination of inputs are active.

Decision letter after peer review:

Thank you for submitting your article "Temporal pattern and synergy influence activity of ERK signaling pathways during L-LTP induction" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Ronald Calabrese as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional simulations and analyses are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This study takes on the question of the roles of the many pathways leading to ERK activation in long-term potentiation. This is an advance since few models consider timing roles of more than a couple of input pathways to ERK or in plasticity. The authors consider two aspects: how pathways sum to give strong responses, and distinct temporal pattern selectivity. They show that both summation linearity, and pattern selectivity, are strongly governed by which pathways are engaged in driving the response.

Essential Revisions:

A key point discussed by the reviewers was whether the temporal pattern selectivity represented sufficient interest and novelty. Could the authors make a strong case for this? In addition the reviewers felt that the following points would be essential to address in a revision:

1. Could the authors provide extensive comparisons to experiment? All the reviewers felt that the parameterization was inadequately validated, specially as the model was a significant change from its original sources.

2. Could the authors bring a more complete account of activation of the chosen pathways by synaptic input? It should be possible to simulate how all the pathways are triggered, presumably in an overlapping way, by different kinds of input.

3. While ERK is important, there are numerous other pathways that play a key role in plasticity. The authors should specify the role of ERK and relate it to other pathways.

4. The analyses of summation and linearity should be done in a more statistically complete manner.

5. The authors should provide better documentation of their reaction system through diagrams and standard formats.

6. What testable predictions does the model make?

In addition, the reviewers brought up other relevant points in their individual reviews.Reviewer #1:

This study takes on the question of the roles of the many pathways leading to ERK activation in long-term potentiation. This is an advance: few models consider more than a couple of input pathways. The authors consider two aspects: how pathways sum to give strong responses, and distinct temporal pattern selectivity.

The model and analysis is potentially interesting, but the paper would be much strengthened if there were more convincing validation of the properties of the model by way of simulations to compare with experiments. I also bring up a couple of points about how better to link synaptically-driven responses to the properties of the model.

1. I was looking to see some model validation before diving into the predictions of the model. Specifically, it would have been useful to compare the model ERK responses to each of the individual stimulation pathways that the authors implement.

Around line 531 the authors describe how parameters were chosen. These seem to rely on previous work or on steady-state levels in the absence of stimulation. Since the model is quite different from the source models, it is important to provide additional validation. Further, time-series responses and dose-response curves give far tighter constraints on system behavior than single-point steady-state readouts. A figure with a range of such validation runs would be very helpful.

1b. There is a nice analysis (Table 2) of effects of KO on responses. Surely there are physiological experiments to compare with this? In the para around line 137 several experiments are mentioned but it would be useful to show simulations to compare with the data.

2. What is the relative strength of contributions by each of the proposed 5 pathways to ERK regulation? How was this ascertained?

3. It is interesting to see differences in linearity between cAMP and Ca pathways. However, these are themselves downstream of the synaptic input. Could the authors explore how these differences would manifest upon synaptic input to a typical synapse having AMPAR, NMDAR, and mGluR? Won't they be rather overlaid on each other?

4. While it is nice to see a model with as many as 5 pathways driving ERKII, I am curious about the choice of these input pathways. From synaptic input one would expect to see an mGluR component. Do the authors envision that this folds into Gbg? Further, one sees other signals such as BDNF as major players in plasticity.

4b. I bring this up also in the context of the reported time-courses. Experimental time-courses of other pathway inputs can be quite different from those explored here, BDNF tending to be quite slow.

Reviewer #2:

There are, however, a couple of points that I feel should be addressed, in order for me to enthusiastically recommend this manuscript for publication.

1. There needs to be additional technical detail on how the original models were expanded. The model presented here was developed by merging Jȩdrzejewska-Szmek et al., 2017 and Jain and Bhalla, 2014 models. These models were developed based on experimental data and validated with independent experimental datasets in a rigorous manner. It is not clear how the combining these two models, and the additional molecules and reactions added have affected the dynamics of ERK activation, and how comparable they are to the original experimental data used for model development in the previous modeling efforts. It is not clear if the model was reparametrized.

2. Beyond the ERK activation traces, it would be useful for clarity sake to also include the simulated traces for the activation of the upstream molecules (PKA, RAS, RAP, etc). Given how additional changes have been made additional information should be provided to ensure that the contribution of each pathway is accurately represented.

Reviewer #3:

This paper is primarily about modeling the ERK pathway during the induction of synaptic plasticity. This pathway has been previously modeled, and this is cited in the paper. The main addition here is the addition of the effect of SynGap which is necessary in some form of LTP. This is a very detailed study, and what it seems to primarily show is that the ERK pathway favored spaced vs. massed stimulation protocols. This is a very detailed paper, but no conceptually new ideas are presented here. The paper adds to an existing foundation, but fails to make the case that this is a very significant addition. What is the significant consequence at a higher level of these added details?

The ERK pathway is just one component of a much larger set of pathways that control synaptic plasticity, how much do we learn from studying this pathway in isolation? Also, the paper cites the importance of this pathway to L-LTP, is it the induction phase of L-LTP? It seems so because ppRRK decays in less than an hour. How then does this pathway contribute to the maintenance of L-LTP, these processes such as a possible upregulation of protein synthesis are not part of this model either.

This paper studies in detail different pathways that influence ERK activation is synapses. This is a very detailed study, but how many details do we actually know? For a detailed paper though it seems that many of the details are missing. Is there a detailed diagram of reactions, or set of equations for all these reactions? Some coefficients are named in figure 1, and this might be sufficient for a schematic description of the model in the paper, however there must be somewhere a detailed description of all reactions. How many species are there here, how many coefficients? How are coefficient values known? How many coefficients are directly estimated? The paper does carry out an extensive robustness analysis, though it is not well explained.

What are the major takeaways from this paper, and what experiments could test this model?

To summarize, the paper is very detailed carefully constructed and executed, it fails to convince that the problem it addresses is very significant, and it makes no conceptual breakthroughs.

The induction protocols seem to include not only calcium pulses, but also cAMP and g-protein coupled pulses, what is the cellular origin of these other pulses? Is the G protein activation due to β-adrenergic activation, is this activation necessary for plasticity? What is the cellular origin of the cAMP and Gi activation in slice? Similarly, what primarily activated cAMP in real synapses?

Is ERK required for all forms of LTP? Some references indicate it might not be. Is ERK necessary for early LTP induced by 100Hz stimulation?

I get lost in the details of the introduction, description of different pathways should be in results and relate to figure 1. It looks like a shopping list, why is this significant?

Why is it important that this is a stochastic diffusion reaction model rather than a deterministic model? Nothing about fluctuations, except for small error bars are mentioned in this paper.

Do not reference Zhang et al. Nature Neuro 2012, its' not a mammalian LTP model, still there are similarities (and differences), especially as ERK pathways are studied and since it relates to spaced learning.

229 – where do we see autophosphorylation in figure 3F?

Figure 6B – hard to see shape of symbols.

No model diagrams or equations here, for example how in CaMKII autophosphorylation implemented? Figure 6C – what is old CaMKII? They give a reference, but we do not know what the new model is.

Narrow picture by looking only at ERK. – For example, increasing PP1 can enhance ppERK, however it might reduce overall LTP due to dephosphorylation of AMPA receptors. What wins?

Figure 7 – what in figure 7 shows super linearity? It's in the title, where else? This applies to paragraph starting in line 368 as well. Where do we see these results. We can try to eyeball it. It would be useful to show a plot of combined model/(sum of individual models). By eyeballing this it seems (but might be wrong) that the super-linearity is minimal.

403 – the first time random-forest was mentioned in line 403, and this method is not explained or defined prior to this or even in this paragraph. For eLife type of readers this needs to be explained in simple terms.

423 – typo – "Molecules were randomly simultaneous(ly)"

What to weights in table 5 mean? This relates to the random forest analysis which is not explained.

Similar problems with figure 8, what is shown here? What is the analysis used here? This is totally unclear. Are molecules here changed one at a time? How much are they changed? Is this the 10% discussed earlier? It would also be more instructive to show relative range changes.

How is this paper related to the recent Maki-Marttunen paper from the same lab which appeared recently (https://www.biorxiv.org/content/10.1101/2020.01.27.921254v1.abstract), it is not referenced here. That is a more general paper but seems to exclude ERK. If ERK is so significant how can it be excluded in one paper and included in another from the same lab?

Discussion starts OK, but again devolves into excessive details.

Does this model possibly explain induction of L-LTP, or its maintenance phase? It seems the prior since ppERK activity returns to baseline; these should be distinguished.

In summary – this paper fails to convince that it is of general interest beyond a narrow community. However, the comments in this section show that there are changes to be made even for the specific community of scientists interested in the signaling pathways of LTP.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Temporal pattern and synergy influence activity of ERK signaling pathways during L-LTP induction" for further consideration by eLife. Your revised article has been evaluated by Ronald Calabrese (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Summary points from the previous decision:

Point 1: Comparisons to experiments and validation of parameterization.

The authors have partly addressed this point, with comparisons of simulations to several additional experiments. They have also provided tables of data sources but many parameters are linked to previous models rather than to experiments. It would be helpful if the authors could explicitly address the point about _parameter_ validation, and to what extent systems level experiments provide validation for rate terms.

Point 2: Activation of pathways by synaptic input.

Here the authors use the model from their 2017 paper to generate Ca and cAMP waveforms, and report results consistent with experiments. It is just a single figure though, and only reports ppERK. We don't see the upstream pathways and their responses. Since the authors have now added these upstream pathways, it would be good to see the time-courses for upstream key molecules indicated in figure 1. These include Ca, Gbg, cAMP, as well as CaMKII, PKA, synGap, Ras and Rap1. It would be useful to have a figure with these time-courses for the major stimulus patterns used in the figures. In Figure 8 – supplementary Figure 2B the authors provide some time-courses for a few molecules. A complete set would be desirable.

Point 4: Linearity. Here the authors report ANCOVA analysis for figures 3, 5, 6. This addresses the point.

Point 5: Source data now provided. Unfortunately it isn't in SBML. If the authors can apply a conversion program to their model, an SBML version would be valuable.

Point 6: Predictions: These are now provided.

Responses to reviewer 1: OK.

Responses to reviewer 2: OK

Responses to reviewer 3: We recommend that the response to the point about induction protocols would be best addressed with graphs of the time-courses mentioned above in Point 2.

Also, the response to the reviewer's point about the use of a stochastic method would be good to include in the text. We did not see this statement there.
