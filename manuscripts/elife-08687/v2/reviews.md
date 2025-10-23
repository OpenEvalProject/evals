# Peer review - Round 1

Editors:
- Frank Jülicher, Max Planck Institute for the Physics of Complex Systems , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.08687.018](https://doi.org/10.7554/eLife.08687.018)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled "Reconstructing the in vivo dynamics of hematopoietic stem cells from telomere length distributions" for peer review at eLife. Your submission has been favorably evaluated by Naama Barkai (Senior Editor) and three reviewers, one of whom is am member of our Board of Reviewing Editors.

The reviewers have discussed the reviews and the Reviewing Editor has drafted this decision to help you prepare a revised submission. The referees find the work very interesting and of high quality. Using simple models for symmetric and asymmetric stem cell divisions, key parameter that characterizes the in vivo dynamics of telomere length distributions are reconstructed from measured telomere length distributions.

Before the manuscript could be accepted, several points raised by the referees should be addressed and clarified in a revised manuscript. These concern in particular the possibility to use a likelihood based inference approach and questions about the relationship between measured data (telomere length) and model states (numbers of stem cell divisions).

Reviewer #1:

The authors study the length distributions of telomeres in hematopoietic stem cells. Using simple stochastic models of telomere shortening during cell division, parameters characterizing the in vivo dynamics of hematopoietic stem cells are reconstructed.

This work is elegant and very interesting. Overall the paper is based on a simple and elegant idea. It provides information on stem cell dynamics in humans. However, when reading the manuscript it remains unclear to me how robust and sound the conclusions and results are. There are a number of points that need to be addressed by the authors before the strength of the work can be fully appreciated.

Major points:

A basic problem I have when reading the manuscript is that the models of telomere length reduction address the telomere length distribution in the stem cell population. However the telomere length data is obtained for the cell population taken from blood or bone marrow that contains differentiated cells. So in order to analyze the data it appears that one would need a model for the telomere length distribution of those cells found in the samples. Why should this distribution correspond to the one of the stem cell pool described by the model? This is quite unclear.

A related point is that the authors discuss very simple scenarios where only one step of differentiation from the stem cell pool is considered. In practice, differentiated blood cells could arise via several differentiation steps in a more complex scheme. This might change the telomere length distribution of the circulating cells. Such issues are not addressed in the paper.

A question arises from the statement in that "a cell loses typically 30 to 50kbp telomeric repeats per cell division" (subsection “In vivo measurements of telomere length suggest an increasing number of hematopietic stem cells during human adolescence”). This implies that the loss of repeats per division is itself a stochastic variable with mean and variance. In this case the distribution of telomere length differs from the distribution of cell states i. This is not discussed. Rather, the distinction is blurred by a confusing mix of language. For example in the subsection “Proliferation properties of stem cells differ during adolescence and adulthood”, the units of r/N0 are given as kbp/year even though by definition r/N0 is a rate with units 1 over time.

The presentation of the work is sometimes confusing because of imprecise language and confusing terminology. For example, in the subsection “The model predicts characteristic telomere length distributions for different ratios of symmetric and asymmetric stem cell divisions” you state: "Each stem cell proliferates randomly with a rate r". Again, in the subsection “Asymmetric cell divisions”: "r represents the proliferation rate of a cell". However looking carefully at Equation (S1) suggests that the parameter r is not what the authors say it is. The proliferation rate per cell rather appears to be given by the ratio r/N0 when using the terminology of the authors. Similarly, for the case with symmetric divisions, the proliferation rate per cell is r/(rpt+N0). This is consistent with the statement that the proliferation rate of a stem cell decreases with time but is inconsistent with the definition of r in the text.

The statement "the assumption of strictly asymmetric divisions fails to explain the pronounced loss of telomere in infants" is unclear. What exactly is the evidence for a pronounced loss in infants? If one fits a linear law to the data in Figure 2 there would be a lot of variability at young age but not a "pronounced loss".

Related to this last point is the statement in the caption to Figure 2: "The decrease of the average telomere length slows down in children and becomes almost linear in adults." I do not understand how this statement follows from the data shown. The data does not appear to support this statement.

The statement of fact that the "increased loss" of telomere length at young age is "an immediate consequence of an expanding stem cell population" is a strong statement, without a clear reasoning. It rather seems to be a suggestion based on the model that is here stated as plain fact. Also, the evidence for an "increased loss" is not compelling, as it is not easily seen in the data in Figure 2. I do not understand where this claim stems from. The statement about "increased loss… during adolescence" is unclear too. Which part of the data is meant here?

The distinction of two phases discussed in Figure 4 is not very convincing and seems a bit arbitrary. Also, in Figure 4, it is unclear what data was analyzed with the Bayesian method. What problem is solved by introducing the distinction between two phases? The Bayesian approach also becomes conceptually puzzling when the probability p is now itself becoming distributed by a very broad probability distribution in phase 1 (Figure 4 h). What does this mean?

The linear fits to the data in Figure 6 are not really compelling as the data seems to be consistent with widely varying linear behaviors.

Reviewer #2:

In their manuscript entitled 'Reconstructing the in vivo dynamics of hematopoietic stem cells from telomere length distributions' Werner et al. use a simple mathematical model of symmetric/asymmetric stem cell divisions and link it telomere length distributions measured experimentally in hematopoietic cells. Studying the properties of the model, they identify qualitative differences in the resulting telomere distribution between a strictly asymmetric and a mixed symmetric/asymmetric model of cell division. Fitting the model to the data, they claim that during childhood stem cell divisions are predominately symmetric leading to an expanding stem cell pool, while during adulthood stem cell divisions are mostly asymmetric.

The manuscript is well written, the theoretical results/calculations are well explained, sometimes maybe even in too much detail in the Introduction but definitely sound, and the application of the model to experimental data reveals interesting insight into (individual) human stem cell dynamics.

I very much liked that the authors took a Bayesian approach to model estimation, because the indeterminacies in the model need to be quantified. My main criticism (details below) however revolves around some modeling aspects and the precise inference method used to fit the model to the experimental data.

Before publication, I encourage the authors include the following improvements/clarification into the manuscript:

Major points:

The applied inference approach (termed 'Bayesian inference method') seems to be very simplistic. The authors essentially apply Approximate Bayesian Computation (ABC) rejection sampling (this term should be mentioned in the manuscript). These likelihood-free methods are usually applied when the likelihood function of the model is intractable. However, the authors show (e.g. S10, S20) that they can solve for the relevant quantities of their model. Hence a likelihood based inference approach is possible (e.g. maximum likelihood estimation + profile likelihoods, or full MCMC for posterior distributions) and should be used (in order to avoid the pitfalls associated with ABC). In fact, fitting S10 is just a linear regression problem.

You consider three different models of increasing complexity: 1) strictly asymmetric, 2) mixed symmetric/asymmetric, and 3) a two-phase model. Obviously, more complex model can fit the data better. However, can you show that the more complicated models are indeed necessary using some model selection techniques? Especially model 3) might be hard to justify: Looking at Figure 2, one cannot really observe two different phases and model 2) seems to do fairly well already. Here I strongly suggest to do Bayesian model selection e.g. using Bayes factor – recently it has been shown that this can be efficiently calculated e.g. using thermodynamic integration also in the context of biological dynamical systems.

In your model, cells are distinguished according to the number of times they have divided (the states i). In the experiment you can only observe telomere length for a cell, not number of divisions.

How are those two quantities related in your model (what's your observation/error model for the data)? This seems nontrivial, e.g. because a certain state i in the model doesn't correspond to a fixed observed telomere length (you mention that each division yield a loss of ~30-50bp) and this uncertainty will propagate with each division. Hence, based on a measured telomere length inferring the number of divisions is probably not unique (e.g. what about a measurement of telomere length = 55? It could have divided once, losing 55bp at once. Or it might have divided twice losing a bit less then 30bp each time). Please discuss these non-uniqueness using either Bayesian credible intervals or more so identifiability analysis using profile likelihood/posterior methods.

According to the stochastic model, you implicitly assume that cell-cycle times (in your case the waiting times in state i) are distributed exponentially (which they are clearly not in the real stem cell system). Please discuss if/how this assumption impacts on the results. Alternatively people nowadays often use delayed models by having the cell go through multiple states before actually dividing – then the Poisson model would be replaced by a log normal in the limit I believe. Here comparison to actual cell cycle distributions would be helpful.

For the section "Proliferation properties of stem cells during adolescence and adulthood" it remains unclear what data is actually fitted with this procedure. Are the same data shown in Figure 2? If so, it seems strange that you already discuss the fitted model in a previous paragraph and describe this 'Bayesian inference method' only later.

In the next section (“A single sample of telomere length distribution…”) you analyze the entire telomere distribution instead of only looking at the average. First, it is worth mentioning that these data correspond to the open symbols in Figure 2 (which of course shows only the mean again). Second, did you refit the model to those distributions? If so, how was this done?

Reviewer #3:

The authors develop a mathematical model in order to interpret data of telomere length shortening in hematopoietic stem cells from a relatively large number of patients. The mathematical model is used to infer dynamic properties of stem cell populations from data on telomere length distributions. Such analysis could quantify parameters of telomere dynamics from a single blood sample of a person. The model can be used as a tool to retrospectively infer stem cell dynamics, which could become useful in the personalized diagnosis and prognosis of disease.

I think that this is a very nice paper and of very high impact for the field. It is a show-case for how biologically realistic mathematical models can be coupled with clinical data in order to arrive at clinically useful insights, with potential to influence disease understanding and diagnosis. Therefore, I think that the quality of the paper is definitely suitable for a high-impact journal, such as eLife, and I recommend that this paper is published in the journal after some revisions.

I think that revisions could improve the paper further, and my suggestions are given as follows:

Following the Introduction, you have a section on "Modeling telomere length dynamics". I think that this could be improved. In particular, it is hard to get a detailed enough picture of the exact modeling approach from this section. Some of the details that I was missing in this section are explained in the Results section. So perhaps, all model description could be placed in a modeling section, and the Results section could just describe the results. This might make it easier to read the paper. Of course, a detailed and clear model description is given in the supplementary materials, so my comment is just about the readability of this particular section in the main text

I have a question regarding the model structure, and it might be useful to discuss this somewhere in the paper. With a certain probability, asymmetric division occurs, where stem cell division leads to one stem daughter cell and one differentiating cell. With the opposite probability, symmetric division was assumed to occur, where division gives rise to 2 stem cells. This is a biologically reasonable model. However, it is also possible to formulate this differently. For example, you can assume that with a certain probability, a stem cell divides to give rise to 2 stem daughter cells, and with the opposite probability, it divides to give rise to 2 differentiated daughter cells. In this way, you then probably would need to include feedback mechanisms to obtain stable and realistic dynamics. Would such a difference influence your results or not? I am not suggesting analyzing further models, but a discussion on model robustness might be useful for the paper.

Along similar thoughts, it could be helpful for the Discussion to include some text that discusses whether the reported results could change if different mathematical formulations or assumptions are used.

For clarity, the Abstract could point out more strongly that data have been collected for this and experimental procedures were used.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Reconstructing the in vivo dynamics of hematopoietic stem cells from telomere length distributions" for further consideration at eLife. Your revised article has been favorably evaluated by Naama Barkai (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.. The manuscript has been significantly improved and the points of the referees have been taken into account. There is one technical comment of referee two that the authors should consider before acceptance, as outlined below. The new Figure 2—figure supplement 1 clarifying the difference between the two models is very useful and might be well suited as a main figure.

Reviewer #1:

The authors have carefully addressed the reviewer comments. The issues raised in my first report have been clarified and the text is now much clearer.

Reviewer #2:

In revised version of their manuscript "Reconstructing the in vivo dynamics of hematopoietic stem cells from telomere length distributions", the authors have incorporated the comments and suggestions of the three reviewers, increasing the quality of the manuscript considerably. Especially some confusion due to inconsistent nomenclature has been sorted out and makes the manuscript much easier to read.

In particular, the authors responded to all my concerns/issues and could sort out most of them. However, I would like to comment on some specific points and ask for additional clarification if possible.

Fitting procedure:

I have the feeling that it is a bit confusing/redundant now; to summarize this is what I found as fitting setup:

1) You fit your models in the section "In vivo measurements of telomere length…" giving some parameter estimates;

2) You perform ABC-rejection sampling in the next section, giving some idea about the posterior parameter distribution and uncertainties;

3) You do maximum likelihood estimates of the parameters (+ confidence intervals), again giving some idea about the uncertainties.

So, you fit the same data, with three different methods (actually I'm not sure what the difference between 1 and 3 is). This seems unnecessary and confusing. Why doing basically the same thing three times? Is this for different models, or for comparison? What’s the difference between 1 and 3?

One observes that the estimates a (slightly) different, e.g. telomere_loss_ABC = 0.071 vs telormere_loss_MLE=0.075. Is this difference due to the different "error measure", i.e. R2 for ABC and quadratic distance/Gaussian error for MLE? Since you do ABC to get a handle on the uncertainties, you should report them (as you did for the MLE), i.e. the boundaries of the credibility intervals.

One major advantage of having the full posterior is that you can look at correlations of parameters. The one-dimensional confidence/credibility intervals (or an approximation) you can also obtain from MLE. Consider showing e.g. pairwise scatter-plots of the posterior samples to show whether there are some correlations/dependencies.

This whole subject discussed above should be straightened out in the final manuscript. Choose one suitable method and stick to it (I would suggest MCMC + Bayes factors, which gives you posterior uncertainties and model comparison or the ABC version). Otherwise the reader will get lost.

Model selection:

Thanks for incorporating some model selection. Any particular reason why you choose AIC and not BIC? Does the BIC select the same model? Since the multiphase model is inferior to model 2, you should be careful not to interpret this model too much.

Figure 2:

Thanks for showing the fits in Figure 2—figure supplement 1. This helps a lot to see why model 1 doesn't explain the data so well. Is there any reason not to put this figure into the main manuscript (instead of the old Figure 2 which doesn't show the linear fit)?

About my question on exponential waiting times:

My question was about cell cycle times, i.e. the time from a cell's "birth" (the division of its mother cell) until it divides. From what I understood when reading the supplement section "Connections to the Normal and Lognormal distribution", you look at the "distribution" N(i)(t), i.e. the number of cells across states, which is Poisson (model 1) or generalized Poisson (model 2). These can then be approximated by normals/lognormals.

However, to me this is fundamentally different from a normal/lognormally distributed cell cycle time. The cell cycle time tells us when a single cell is going to divide. Your N(i)(t) tells us how a population of states spreads over the states i. I don't see an immediate connection between those to quantities. Please comment on that.

Reviewer #3:

The authors have addressed all of my comments and improved the manuscript accordingly. I think it should be accepted for publication in the current form.
