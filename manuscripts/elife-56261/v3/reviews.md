# Peer review - Round 1

Editors:
- Timothy O'Leary, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56261.sa1](https://doi.org/10.7554/eLife.56261.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The problem of relating dynamical models to data pervades science and is particularly challenging in neuroscience due to high uncertainty in model parameters, model structure and inherent biological variability. This study presents an approach to performing model parameter inference based on large scale simulation and deep neural networks that permits efficient querying of model behaviour and underlying parameter distribution once simulations have been performed. The usefulness is demonstrated on a number of challenging and relevant models.

Decision letter after peer review:

Thank you for submitting your article "Training deep neural density estimators to identify mechanistic models of neural dynamics" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and John Huguenard as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Mark S. Goldman (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

This is a generally well written paper showcasing methodology for inferring model parameter distributions that are compatible with specified behaviours. The methodology uses recent advances in machine learning to approximate a likelihood function over model parameters that can be reused to perform inference. The method is applied to a number of informative examples. Benchmarks provide a favourable comparison against some existing methods (approximate bayesian computation/sampling) and the required computational resources are described.

Some of the reviewers found the methodology hard to follow in places; certain details were lacking. Although the authors pointed out limitations, there were also queries about potential failure modes of this methodology and whether there were methodological heuristics that are non-obvious but important, such as a means of assessing how many samples might be required for a particular model.

The reviewers agreed that a brief revision addressing specific points on methodological clarity (outlined in the reviewer's comments) and commenting on these other points would be worthwhile.

Reviewer #1:

General Assessment: This paper introduces a machine learning technique which generalizes Bayesian approaches to mechanistic models which are complex, multiparameter, and which do not necessarily have probability distributions as their key outputs. This is an interesting and likely productive direction to investigate. They claim their method is scalable and adaptable and the paper applies it to several problems of increasing complexity. However, I am unable to judge their method, because almost no details are given. This is the case even for very general questions such as what they use in place of the likelihood function for Bayes rule, and what they mean by a trained density estimator. The method in this paper may or may not be worthy of publication, but – since it is a method paper – I think the paper would need to be rewritten in a manner that readers can understand both in generality and in detail what their method accomplishes.

Review of Goncalves et al.:

The authors introduce a machine learning technique for finding ensembles of parameter values of mechanistic models which are consistent with experimental data.

The core of their method is the “Sequential Neural Posterior Estimation” (SNPE) which takes in a mechanistic model, a (thing which resembles a) prior and summary data, does some mysterious machine-learning processing and spits out something like a posterior probability distribution.

I agree with the authors that large unwieldy mechanistic models likely require machine learning to find parameter ensembles. I also agree that it should be possible to develop Bayesian like approaches for models which are not naturally probabilistic, a problem they pose nicely, and which I have come across but not quite realized was of such importance. I also find their results on the gastric circuit interesting- particularly the finding that the many disparate parameter values that can all fit data seem to lie on a single plateau, rather than on distinct minima

However, I don't really know where to begin in evaluating SNPE. It feels as if there is a section missing- the Introduction talks in generalities about large mechanistic models and the need to address their difficulties, and then it jumps to discussing the particular applications of SNPE.

I don't know what the authors mean by posterior and prior, nor what they mean when they say their method works without a likelihood.

There is muddling of what their output is and what they do to achieve it, and I don't find either sufficiently explained. For example, machine learning could be used to approximate a posterior in the usual Bayesian sense. Still I would want to know what prior they are using what their likelihood function is and what posterior they are approximating, even if there is a black box in the middle. I don't understand what their p(θ|x) is an approximation to.

Reviewer #2:

General assessment

This is a really clear and well written paper with practical solutions for an important problem in theoretical neuroscience. In addition, the authors provide high quality code and documentation making it fairly straightforward for other groups to make use of these tools. I would expect that these tools would become widely adopted in the community. Indeed, I would love to have had this for many previous modelling studies and will certainly use it in the future.

Major comments

1) My main issue is that applying this method depends on how well the deep network does its job of estimating the density (which depends partly on the user specifying the correct architecture and parameters). The authors do discuss this under limitations, but it might be interesting to see what a failure would look like here and what are the scientific consequences of such a failure. I suspect the answer might partly be that you should always verify the resulting posterior distributions, but how practical is this in a 31-dimensional setting, for example? When the authors were working on the examples for this manuscript, how much work did it take to make sure that there were no failures (assuming they verified this) and how did they detect them? (For example, in subsection “Functional diversity of ion channels: efficient high-throughput inference” it's implied that the only failures in this example were because the Omnimodel wasn't able to fit some data.)

2) Would it be possible to use SNPE to automatically suggest the optimal experiment that would give the narrowest posterior distribution over parameters? This might already be what was suggested when citing papers that "automatically construct informative summary features", I wasn't entirely sure.

Reviewer #3:

This paper addresses a major issue in fitting neuroscience models: how to identify the often degenerate, or nearly degenerate, set of parameters that can underlie a set of experimental observations. Whereas previous techniques often depended upon brute force explorations or special parametric forms or local linearizations to generate sets of parameters consistent with measured properties, the authors take advantage of advances in deep networks for use in estimating probability densities to address this problem. Overall, I think this paper and the complementary submission have the potential to be transformative contributions to model fitting efforts in neuroscience, and the ability of this work to handle cases that are not continuous is a plus. However, I think the paper needs to clarify/quantify how much of an advance this is over brute force methods (plus simple post-hoc analyses on the simulated database), given the heavy brute force aspect of generating the training set, and also whether there are biases in the method. Also, the writing could benefit from more focus on methodology (rather than on examples) to ease adoption of the method.

Substantive concerns:

1) In the example of Figure 1, the Appendix 1—figure 1A (which should appear in the main figure rather than the supplement) appears to show that the SNPE's mean temporal filter is considerably off from the true temporal value. Why is this the case? More generally, this suggests that more “ground truth” examples with direct side-by-side comparisons should be provided to assure that the estimates provided by this method are not significantly biased. For example, Figure 5 is wonderful in showing a sloppy/insensitive direction in parameter space that has sharp curvature. Could one do something similar to this and directly compare (for an example with smaller number of parameters, e.g. 4 or 5) the estimated probability distribution to a “ground truth” generated through a sufficiently dense grid search, for different numbers of training samples.

2) The authors need to clarify, quantitatively, how much of a benefit this is over simple post-hoc analysis of results of brute force methods that just randomly (uniformly) sample parameters, especially given that there is a lot of brute force work in this method as well in generating the samples for the deep network training. For such brute force methods (e.g. rather than a grid, some studies just uniformly randomly generate parameters to use in the simulations), one can also just post-hoc fit the results to a mixture of Gaussians or similar classical density estimator so that other values can be interpolated from the obtained data. How much is the deep network approach needed? My guess is that it does help, potentially a huge amount, but the authors need to show this in a carefully controlled comparison.

3) Related to #1, given that this paper is primarily a methodological advance, I think the authors could spend more time laying out the essence of the basic algorithm in the beginning of the Results. For example, it's not clear in Figure 1 exactly what is being input and output from the neural density estimator deep network. More generally, it's worth describing more about the algorithm, perhaps in less technical language, in the main results.

Within the Materials and methods, since the authors indicated some playing around with parameters was needed, it would help a lot for the adoption of this method by others to have more explanation of different features of the method and more intuition behind choices. For example, what is the loss function used after the initial round? Are there any basic constraints on what shape the deep network should have (e.g. should it fan out in the middle layers, fan in, or be approximately uniform in width)? What is the basic idea behind a masked autoregressive flow (MAF) and when should that be chosen versus the mixture of Gaussians model? The algorithm's description could also be expanded (or a short version could be in the main and expanded version in the Materials and methods).

4) Is there some way to ballpark estimate, or post-hoc characterize, how many samples may be needed? Seemingly, the fact that this works with less than one sample per dimension says something about the geometry of the solution space and its effective dimensionality. (If this seems too hard, the authors can punt on it).

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your article "Training deep neural density estimators to identify mechanistic models of neural dynamics" for consideration by eLife. Your revised article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and John Huguenard as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Mark S Goldman (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary

This is methodology is of potentially wide interest, and although the authors have made efforts to explain the interpretation, applicability and caveats of the methodology, one reviewer feels that the manuscript could benefit from further clarification on:

1) How one should interpret “posterior probability density” in cases where there is a deterministic relationship between parameters and behaviour, e.g. in extreme cases where there might be a single solution.

2) The fairness of comparisons with ABC/sampling – are these alternatives being compared in an even-handed way?

3) It may be helpful to have a very explicit example of the results SNPE returns on a problem where “ground truth” of feasible parameters are known. This could be a simple model dynamical system, used for illustration.

Full reviewer comments are included below, for reference.

Reviewer #2:

I'm very happy with the reviewers response to my previous review, and congratulate them on a great paper!

Reviewer #3:

The authors have clarified the methods in a way that I think should be helpful, and I remain optimistic that this will be a very valuable technique for the field. However, I think some of the other concerns raised about rigorously demonstrating the technique, and clarifying the method conceptually were not addressed. I will try to re-state these concerns in a broader scope that I hope strengthens the paper, clarifies potential issues, and gets at some key conceptual and rigor issues that need to be addressed

1) Conceptual question: The manuscript and reply heavily emphasize that SNPE performs Bayesian inference, as compared to approaches that only are applicable to deterministic modeling (like classic brute force approaches). However, outside of the very simple illustrative example of Figure 2, it appears that all of the remaining examples are done on deterministic models. This leads to a fundamental conceptual question: how should one interpret the resulting posteriors resulting from SNPE?

To be concrete, if one used the precise output of a simulation (rather than summary statistics), then the actual posterior probability over parameter values is a δ function (assuming the model if identifiable). If there are nearby solutions, this wouldn't change the true posterior probability, i.e. despite being nearby, they would have posterior probability of zero. Thus, while the authors criticize other methods for using “user defined” criteria of being close to a solution, this example illustrates that if one found the exact posterior probability (as the authors state in their reply that the method should ideally do if it works correctly), all information about the existence of nearby (i.e. almost, but not entirely, degenerate) solutions would be lost. I'm guessing the density estimator will somehow tradeoff “posterior probability large” for “close to the correct solution”, but this then requires some interpretation of how “closeness to the correct simulation output” is translated to “posterior probability”. Put in this light, at least a user defined criterion of closeness for a deterministic model, as done in traditional fitting methods, is explicit and easy to interpret. Can the authors justify or provide users with an explanation for how to interpret SNPE when applied to deterministic simulations-my guess is that, when SNPE is working well, it's some sort of smoothed version of the true, very spiky posterior, but is there a way for users to interpret the solution, e.g. how would a user know if there are nearby solutions if the SNPE did a great job of finding the true posterior and therefore didn't indicate these nearby solutions? And how should the user interpret “probabilities” in a deterministic model where there may only be 1 true solution?

Note: when summary statistics are used rather than exact simulation output, this will likely create some degeneracies. However, this still may end up creating a razor thin slice in parameter space that corresponds to truly, exactly matching the summary statistics, which would then be represented by the true posterior. This scenario then returns to the same fundamental questions of: a) how to interpret the posterior from SNPE, and b) how to interpret a simulation output that is very close to the summary statistics but not equal to them and therefore perhaps lost if SNPE is finding the true posterior of the deterministic model.

2) On the one example that is stochastic (Figure 2), I am still confused by the results shown. Specifically, in Figure 2C, the posterior samples consistently and systematically undershoot the true receptive field for intermediate parameter values. This is a simple LN model for which classic maximum likelihood models usually doing an excellent job finding the true receptive field, at least with enough data. If one ran standard maximum likelihood estimation on this, would it miss? If so, why? Is this reflecting that the authors are using too broad a prior and it is not converging to the true posterior or that too few samples are used (the number of samples is not indicated)-if the latter, can the authors run with more samples and show that their method then converges to the correct answer? Or is it something else (e.g. see next paragraph)?

In addition, the authors state that their method works because it gets the same answer as MCMC. However, I'm wondering if both might be making errors due to the use of the Polya-Γ sampling scheme since, at least in the Pillow and Scott article cited, this was used not for a standard LN model but rather to model more complex models in which the variance was greater than for a Poisson spike count. In any case, it seems worth explaining where the systematic error in the posterior samples is coming from, given that the LN model is such a simple classic model fit whose parameters have been successfully identified by simpler maximum likelihood methods.

3) Related to the Figure 2 example, I was struck by the huge errors and nearly zero correlation for the ABC methods. Is this fundamental to ABC or is this because the authors are hamstringing the ABC method by applying it in a very naïve manner that isn't how someone using ABC would apply it. Specifically, from the methods, it looks like the authors are considering every parameter to be independent, with no smoothing or regularization. I would think that someone using ABC methods would apply regularizations or the like that might dramatically reduce the effective dimensionality of the problem, so it's not clear if the comparison shown in the manuscript is fair. This isn't to say that SNPE won't still work much better than ABC methods, but it's worth checking to make sure the ABC methods are being applied in a realistic manner if the comparison is to be made.

4) Ground truthing. The authors suggest that they can't ground truth the technique due, in part, to the stochastic nature of it. While I appreciate there may be some challenges, a lot could be done, especially since most of the manuscript focuses on deterministic examples that are easier to check. For example, in Figures 3-5, parameter estimation results that may or may not be correct are shown and the reader is left to assume they are correct by looking at a single or very small number of examples. While I fully expect that it does work reliably, it would be nice to actually run a large set of simulations for posterior checks (even if, e.g., only the mode of the distribution was checked) and then report some statistics.

5) Related to ground truthing, in Figure 5D and the highlighted 2-D plot of Figure 5C, I am confused as to whether the example shows the success or partial failure of the method. Specifically, the point labeled "2" in the Figures 5C and 5D appears to be in a bright (and therefore presumably high probability?) region of the parameter space, both in an absolute sense and possibly (it's hard to tell) compared to the light purple circle simulation (and also relative to going further down below this light purple trace). However, the authors use point 2 to make the point that the simulation looks very far off from the reference trace. This suggests, possibly, that similar probabilities being output by SNPE is on the one hand (values close to the light purple circle) leading to a very good fit and on the other hand (red point 2) leading to a very bad fit – thus, this suggests that one perhaps can't trust “bright” regions in the SNPE posterior to correspond to “good” fits. Can the authors check this and address the more general concern. I'm guessing this may relate to my larger conceptual question of interpreting the “probabilities” for SNPE in my reviewer comment #1 above.

6) Difference from “brute force methods”. I thank the authors for trying to generate a comparison to brute force methods by showing a rejection method. However, I don't think this is necessary and I think it's confusing as I don't think “brute force” and “rejection” are the same (i.e. I'd remove this from the paper as being more confusing than helpful). To me at least, “brute force” methods simply generate many example simulations into a database. This is separable from the problem of “what does one then do with this database afterwards”. My point was simply that I think SNPE can be interpreted as being either within the class of brute force searches in generating a very large database of simulations (e.g. ~20 million for Figure 5), or if one focuses on the density estimation component, as being a method that is complementary to the brute force database generation step by addressing the “what does one then do with this database afterwards” component of the problem. For the “what does one do with this database” question, one can certainly imagine many things-one can simply visualize the parameter space through various slices, effectively marginalizing over certain variables and illustrating for example where bifurcations occur that might be difficult to identify mathematically, or can (as the authors highlight has often been done previously…but this should not be equated with parameter search methods, as it's just one possible post-search thing that can be done) implement some sort of selection/rejection criterion. One might also want to interpolate/extrapolate, asking for an estimate of what a new set of parameters would lead to, for which a density estimator such as SNPE would excel.

This is less a criticism of the approach and more of a clarification for placing the method within existing work. I agree with the authors that current use of brute force generation of databases has not taken advantage of better methods of post-database-generation analysis, as SNPE offers, leading to the likely (and potentially dramatically, as demonstrated in Figure 5) incorrect implicit assumption that one needs to generate many samples per dimension to well-characterize the space. I just wanted to separate the notion of generating a database of many examples (which doesn't need to be done on a grid), from the notion of how one post-hoc analyzes it. And overall, this focus on the power of post-database-generation analysis is why I still think SNPE, and the more general focus on use of density estimators, is a potentially transformative contribution for the practice of model building (in addition to SNPE's applicability to stochastic problems that is already well emphasized in the manuscript).
