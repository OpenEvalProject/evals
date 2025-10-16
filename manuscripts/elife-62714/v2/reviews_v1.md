# Peer review - Round 1

Editors:
- Marcel P Goldschen-Ohm, https://ror.org/00hj54h04 University of Texas at Austin United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62714.sa0](https://doi.org/10.7554/eLife.62714.sa0)

The authors develop a Bayesian approach to modeling signals arising from ensembles of ion channels that can incorporate multiple simultaneously recorded signals such as fluorescence and ionic current. For simulated data from a simple ion channel model where ligand binding drives pore opening, they show that their approach enhances parameter identifiability and/or estimates of parameter uncertainty over more traditional approaches. The developed approach provides a valuable tool for modeling macroscopic time series data including data with multiple observation channels.


---

# Peer review - Round 1

Editors:
- Marcel P Goldschen-Ohm, https://ror.org/00hj54h04 University of Texas at Austin United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62714.sa1](https://doi.org/10.7554/eLife.62714.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Bayesian selection of Hidden Markov models for multi-dimensional ion channel data" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Marcel P Goldschen-Ohm as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Richard Aldrich as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Lorin S Milescu (Reviewer #2); Colin Kinz-Thompson (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require additional discussion or a modest amount of additional analysis, as they do with your paper, we are asking that the manuscript be revised to address the points raised by the reviewers.

Our expectation is that the authors will eventually carry out the additional analyses and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

Extracting ion channel kinetic models from experimental data is an important and perennial problem. Much work has been done over the years by different groups, with theoretical frameworks and computational algorithms developed for specific combinations of data and experimental paradigms, from single channels to real-time approaches in live neurons. At one extreme of the data spectrum, single channel currents are traditionally analyzed by maximum likelihood fitting of dwell time probability distributions; at the other extreme, macroscopic currents are typically analyzed by fitting the average current and other extracted features, such as activation curves. Robust analysis packages exist (e.g., HJCFIT, QuB), and they have been put to good use in the literature.

Münch et al. focus here on several areas that need improvement: dealing with macroscopic recordings containing relatively low numbers of channels (i.e., hundreds to tens of thousands), combining multiple types of data (e.g., electrical and optical signals), incorporating prior information, and selecting models. The main idea is to approach the data with a predictor-corrector type of algorithm, implemented via a Kalman filter that approximates the discrete-state process (a meta-Markov model of the ensemble of active channels in the preparation) with a continuous-state process that can be handled efficiently within a Bayesian estimation framework, which is also used for parameter estimation and model selection.

With this approach, one doesn't fit the macroscopic current against a predicted deterministic curve, but rather infers – point by point – the ensemble state trajectory given the data and a set of parameters, themselves treated as random variables. This approach, which originated in the signal processing literature as the Forward-Backward procedure (and the related Baum-Welch algorithm), has been applied since the early 90s to single channel recordings (e.g., Chung et al., 1990), and later has been extended to macroscopic data, in a breakthrough study by Moffatt (2007). In this respect, the study by Münch et al. is not necessarily a conceptual leap forward. However, their work strengthens the existing mathematical formalism of state inference for macroscopic ion channel data, and embeds it very nicely in a rigorous Bayesian estimation framework.

The main results are very convincing: basically, model parameters can be estimated with greater precision – as much as an order of magnitude better – relative to the traditional approach where the macroscopic data are treated as noisy but deterministic (but see comments below). Estimated uncertainty can be further improved by incorporating prior information on parameters (e.g., diffusion limits), and by including other types of data, such as fluorescence.

The manuscript is well written and overall clear, and the mathematical treatment is a rigorous tour-de-force. However, the reviewers raised a number points that need further clarification, better discussion or amendment. These concerns are likely to be addressable largely by changes to the main text and software documentation along with some additional analyses. Once addressed, a revised version of this manuscript would likely be suitable for publication in eLife. That said, the study is very nice and ambitious, but clarity is a bit impaired by dealing with perhaps too many issues. The state inference and the bayesian model selection are very important but completely different issues. The authors should consider whether they may be better treated separately, or even perhaps in a more specialized journal where they can be developed in more detail.

Essential revisions:

1. Tutorial-style computational examples must be provided, along with well commented/documented code. The interested readers should be able to implement the method described here in their own code/program. The supplied code is not well documented, and it is unclear whether it is applicable beyond the specific models examined in the paper. It was supplied as.txt files, but looks like C code, and is unlikely to be easily adaptable by others to their own models.

2. The authors should clearly discuss the types of data and experimental paradigms that can be optimally handled by this approach, and they must explain when and where it fails or cannot be applied or becomes inefficient in comparison with other methods. One must be aware that ion channel data are very often subject to noise and artifacts that alter the structure of microscopic fluctuations. It seems that the state inference algorithm would work optimally with low noise, stable, patch-clamp recordings (and matching fluorescence recordings) in heterologous expression systems (e.g., HEK293 cells), where the currents are relatively small, and only the channel of interest is expressed (macropatches?). In contrast, it may not be effective with large currents that are recorded with low gain, are subject to finite series resistance, limited rise time, restricted bandwidth, colored noise, contaminated by other currents that are (partially) eliminated with the P/n protocol with the side effect of altering the noise structure, power line 50/60 Hz noise, baseline fluctuations, etc. This basically excludes some types of experimental data and experimental paradigms, such as recordings from neurons in brain slices or in vivo, oocytes, etc. Of course, artifacts can affect all estimation algorithms, but approaches based on fitting the predicted average current have the obvious benefit of averaging out some of these artifacts.

The discussion in the manuscript is insufficient in this regard and must be expanded. The method should be tested under non-ideal but commonly occurring conditions, such as limited bandwidth and in the presence of contaminating noise. For example, compare estimates obtained without filtering with estimates obtained with 2, 3 times over-filtering, with and without large measurement noise added (whole cell recordings with low-gain feedback resistors and series resistance compensation are quite noisy), with and without 50/60 Hz interference. How does the algorithm deal with limited bandwidth that distorts the noise spectrum? How are the estimated parameters affected? The reader will have to get sense of how sensitive is this method to artifacts. Also, fluorescence data in particular is usually of much lower temporal resolution than current measurements. How does this impact its benefit to parameter estimation?

3. Even more emphasis on the approximation of n(t) as being distributed according to a multivariate normal, and thus being continuous, should be placed in the main text. It seems that this may limit the applicability of the method to data with > ~100s of channels; although the point is not investigated. In Figure 3, the method is only benchmarked to a lower limit of ~500 channels. As shown in Milescu et al., 2005, fitting macroscopic currents is asymptotically unbiased. In other words, the estimates are accurate, unless the number of channels is small (tens or hundreds), in which case the multinomial distribution is not very well approximated by a Gaussian. What about the predictor-corrector method? How accurate are the estimates, particularly at low channel counts (10 or 100)? Since the Kalman filter also uses a Gaussian to approximate the multinomial distribution of state fluctuations, I would also expect asymptotic accuracy. Parameter accuracy should be tested, not just precision.

4. Achieving the ability to rigorously perform model selection is very impressive aspect of this work and a large contribution to the field. However, the manuscript offers too many solutions to performing that model selection itself along with a long discussion of the field (for instance, line 376-395 could be completely cut). Since probabilistic model selection is an entire area of study by itself, the authors do not need to present underdeveloped investigations of each of them in a paper on modeling channel data (e.g., of course WAIC outperforms AIC. Why not cover BIC and WBIC?). The authors should pick one, and maybe write a second paper on the others instead of presenting non-rigorous comparisons (e.g., one kinetic scheme and set of parameters). As a side note, it is strange that the authors did not consider obtaining evidence or Bayes factors to directly perform Bayesian model selection – for instance, they could have used thermodynamic integration since they used MC to obtain posteriors anyway (c.f., Computing Bayes Factors Using Thermodynamic Integration by Lartillot and Philippe, Systematic Biology, 2006, 55(2), 195-207. DOI: 10.1080/10635150500433722)

5. Regarding model selection for the PC data in Figure 7, why does the RE model with BC appear to provide a visually better identification of the true model than the KF model with BC if the KF model does a better job at estimating the parameters and setting non true rates to zero? Doesn't this suggest that RE with cross validation is better than the proposed KF approach in regards to model selection? In terms of parameter estimates (i.e. as shown in Figure 3), how does RE + BC stack up?

6. A better comparison with alternative parameter estimation approaches is necessary. First of all, explain more clearly what is different from the predictor-corrector formalism originally proposed by Moffatt (2007). The manuscript mentions that it expands on that, but exactly how? If it is only an incremental improvement, of interest to a very limited audience, a specialized, technical journal, is more appropriate.

Second, the method proposed by Celentano and Hawkes, 2004, is not a predictor-corrector type but it utilizes the full covariance matrix between data values at different time points. It seems that the covariance matrix approach uses all the information contained in the macroscopic data and should be on par with the state inference approach. However, this method is only briefly mentioned here and then it's quickly dismissed as "impractical". We all agree that it's a slower computation than, say, fitting exponentials, but so is the Kalman filter. Where do we draw the line of impracticability? Computational speed should be balanced with computational simplicity, estimation accuracy, and parameter and model identifiability. Moreover, that method was published in 2004, and the computational costs reported there should be projected to present day computational power. We are not saying that the authors should code the C&H procedure and run it here, but should at least give it credit and discuss its potential against the KF method.

The only comparison provided in the manuscript is with the "rate equation" approach, by which the authors understand the family of methods that fit the data against a predicted average trajectory. In principle, this comparison is sufficient, but there are some issues with the way it's done.

Table 3 compares different features of their state inference algorithm and the "rate equation fitting", referencing Milescu et al., 2005. However, there seems to be a misunderstanding: the algorithm presented in that paper does in fact predict and use not only the average but also – optionally – the variance of the current, as contributed by stochastic state fluctuations and measurement noise. These quantities are predicted at any point in time as a function of the initial state, which is calculated from the experimental conditions. In contrast, the KF calculates the average and variance at one point in time as a projection of the average and variance at the previous point. However, both methods (can) compare the data value against a predicted probability distribution. The Kalman filter can produce more precise estimates but presumably with the cost of more complex and slower computation, and increased sensitivity to data artifacts.

Figure 3 is very informative in this sense, showing that estimates obtained with the state inference (KF) algorithm are about 10 times more precise that those obtained with the "rate equation" approach. However, for this test, the "rate equation" method was allowed to use only the average, not the variance.

Considering this, the comparison made in Figure 3 should be redone against a "rate equation" method that utilizes not only the expected average but also the expected variance to fit the data, as in Milescu et al., 2005. Calculating this variance is trivial and the authors should be able to implement it easily (reviewers are happy to provide feedback). The comparison should include calculation times, as well as convergence.

7. The manuscript nicely points out that a "rate equation" approach would need 10 times more channels (N) to attain the same parameter precision as with the Kalman filter, when the number of channels is in the approximate range of 10^2 … 10^4. With larger N, the two methods become comparable in this respect.

This is very important, because it means that estimate precision increases with N, regardless of the method, which also means that one should try to optimize the experimental approach to maximize the number of channels in the preparation. However, it should be pointed out that one could simply repeat the recording protocol 10 times (in the same cell or across cells) to accumulate 10 times more channels, and then use a "rate equation" algorithm to obtain estimates that are just as good. Presumably, the "rate equation" calculation is significantly faster than the Kalman filter (particularly when one fits "features", such as activation curves), and repeating a recording may only add seconds or minutes of experiment time, compared to a comprehensive data analysis that likely involves hours and perhaps days. Although obvious, this point can be easily missed by the casual reader and so it would be useful to be mentioned in the manuscript.

8. A misunderstanding is that a current normalization is mandatory with "rate equation" algorithms. This is really not the case, as shown in Milescu et al., 2005, where it is demonstrated clearly that one can explicitly use channel count and unitary current to predict the observed macroscopic data. Consequently, these quantities can also be estimated, but state variance must be included in the calculation. Without variance, one can only estimate the product i x N, where i is unitary current and N is channel count. This should be clarified in the manuscript: any method that uses variance can be used to estimate i and N, not just the Kalman filter. In fact, the non-stationary noise analysis does exactly that: a model-blind estimation of N and i from non-equilibrium data. Also, one should be realistic here: in some circumstances it is far more efficient to fit data "features", such as the activation curve, in which case the current needs to be normalized.

9. It's great that the authors develop a rigorous Bayesian formalism here, but it would be a good idea to explain – even briefly – how to implement a (presumably simpler) maximum likelihood version that uses the Kalman filter. This should satisfy those readers who are less interested in the Bayesian approach and will also be suitable for situations when no prior information is available.

10. The Bayesian formalism is not the only way of incorporating prior knowledge into an estimation algorithm. In fact, the reader may have more practical and pressing problems than guessing what the parameter prior distribution should be, whether uniform or Gaussian or other. More likely one would want to enforce a certain KD, microscopic (i)reversibility, an (in)equality relationship between parameters, a minimum or maximum rate constant value, or complex model properties and behaviors, such as maximum Popen or half-activation voltage. A comprehensive framework for handling these situations via parameter constraints (linear or non-linear) and cost function penalty has been recently published (Salari et al/Navarro et al., 2018). Obviously, the Bayesian approach has merit, but the authors should discuss how it can better handle the types of practical problems presented in those papers, if it is to be considered an advance in the field, or at least a usable alternative.

11. The methods section should include information concerning the parameter initialization choices, HMC parameters (e.g. number of steps) and any burn-in period used in the analyses used in Figures 3-6. For example, how is convergence established? How many iterations does it take to reach convergence? How long does it take to run? How does it scale with the data length, channel count, and model state count? How long does it take to optimize a large model (e.g., 10 or 20 states)? Provide some comparison with the "rate equation method".

12. In the section on priors, the entire part concerning the use of a β distribution should be removed or replaced, because it is a probabilistic misrepresentation of the actual prior information that the authors claim to have in the manuscript text. The max-entropy prior derived for the situation described in the text (i.e., an unknown magnitude where you don't know any moments but do have upper and lower bounds; the latter could be from the length from the experiment) is actually P(x) = (ln(x_{max}) – ln(x_{min}))^{-1} * x^{-1}. Reviewers are happy to discuss more with the authors.

13. Here and there, the manuscript somehow gives the impression that existing algorithms that extract kinetic parameters by fitting the average macroscopic current ("fitting rate equations") are less "correct", or ignorant of the true mathematical description of the data. This is not the case. Published algorithms often clearly state what data they apply to, what their limitations are, and what approximations were made, and thus they are correct within that defined context and are meant to be more effective than alternatives. Some quick editing throughout the manuscript should eliminate this impression.

14. The manuscript refers to the method where the data are fitted against a predicted current as "rate equations". However, it is not completely clear what that means. The rate equation is something intrinsic to the model, not a feature of any algorithm. An alternative terminology must be found. Perhaps different algorithms could be classified based on what statistical properties are used and how. E.g., average (+variance) predicted from the starting probabilities (Milescu et al., 2005), full covariance (Celentano and Hawkes, 2004), point-by-point predictor-corrector (Moffatt, 2007).

15. The manuscript needs line editing and proofreading (e.g., on line 494, "Roa" should be "Rao"; missing an equals sign in equation 13). Additionally, in many paragraphs, several of the sentences are tangential and distract from communicating the message of the paper (e.g., line 55). Removing them will help to streamline the text, which is quite long.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Bayesian inference of kinetic schemes for ion channels by Kalman filtering" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Marcel P Goldschen-Ohm as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Richard Aldrich as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Colin Kinz-Thompson (Reviewer #3); Lorin Milescu (Reviewer #4).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Reviewer #1 (Recommendations for the authors):

The authors develop a Bayesian approach to modeling macroscopic signals arising from ensembles of individual units described by a Markov process, such as a collection of ion channels. Their approach utilizes a Kalman filter to account for temporal correlations in the bulk signal. For simulated data from a simple ion channel model where ligand binding drives pore opening, they show that their approach enhances parameter identifiability and/or estimates of parameter uncertainty over more traditional approaches. Furthermore, simultaneous measurement of both binding and pore gating signals further increases parameter identifiability. The developed approach provides a valuable tool for modeling macroscopic time series data with multiple observation channels.

The authors have spent considerable effort to address the previous reviewer comments, and I applaud them for the breadth and depth of their current analysis.

1. The figure caption titles tend to say what analysis or comparison is being presented, but not what the take home message of the figure is. I suggest changing them to emphasize the latter. This will especially help non-experts to understand what the figures are trying to convey to them.

2. I very much appreciate the GitHub code and examples for running your software. However, I feel that a hand-holding step-by-step explicit example of running a new model on new data is likely necessary for many to be able to utilize your software. Much more hand-holding than the current instructions on the GitHub repo.

3. Figure captions sometimes do not explain enough of what is shown. I appreciate that many of these details are in the main text, but data that is displayed in the figure and not concretely described in the caption can makes the figures hard to follow. e.g. Figure 4a – "With lighter green we indicate the Euclidean error of patch-clamp data set." But what data set do the other colors reflect? It is not stated in the caption. Again, I realize this is described in the main text, but it also needs to be defined in the caption where the data is presented. Figure 4d – Please spell out what "both algorithms" intends. Also, a suggestion: instead of having to refer to the caption for the color codes (i.e. RE vs. KF, etc.) it would speed figure interpretation to have a legend in the figures themselves. Few other examples: Box 1. Figure 2. – Please define the solid vs. dashed lines in the caption. Figure 3c – Please define the solid vs. dashed lines in the caption. Figure 12 – "We simulated 5 different 100kHz signals." What kind of signals? Fluorescence I assume, but this needs to be explicitly defined. I'd check all figures for similar.

Reviewer #3 (Recommendations for the authors):

In this revised manuscript, the Münch et al. have addressed all of my original concerns. It is significantly revised, though, and includes many new investigations of the algorithm's performance. Overall, the narrative of this manuscript is now to introduce an approximation to the solution for a Bayesian Kalman Filter, and then spend time demonstrating that this approximation is reasonable and even better than previous methods. In my opinion, they successfully do this, although, as they mention in their comments, their manuscript is very long.

I am not 100% certain, but the approximation that the author's make seems to be equivalent (or at least similar to) an approximation of the chemical master equation using just the 1st and 2nd moments, which is just the Fokker-Planck equation. The authors should discuss any connection to this approximation, as there is a great deal of literature on this topic (e.g., see van Kampen's book).

In Figures 3A and 4D, it is unclear to me what is plotted for the RE and classical Kalman filter (i.e., how is there a posterior if they are not Bayesian methods)? Perhaps it is buried in the methods or appendices, but, if so, it needs to at least be clarified in the figure captions.

The Bayesian statistical tests devised to determine success (e.g., on pgs. 12-13) seem a little ad hoc, but are technically acceptable. I do not see a need for additional metrics.

Line 939: Equation 61 is absolutely not "close to uniform distribution". The α and β parameters of 100.01 are much larger than 1. It is incredibly peaked around 0.5. Perhaps this is a typo?

Line 942: The allowed small breaking of microscopic reversibility in the prior is an interesting idea that I wish the authors would expound upon more.

Line 712: The authors state that the simulation 'code will be shared up-on request'. They should include it with their github pages tutorials for running the examples in case others wish to check their work and/or use it. There is no reason to withhold it.

Line 707: 'Perspectively' is not a commonly used word.

Reviewer #4 (Recommendations for the authors):

The authors have addressed all my comments and suggestions. The manuscript is nice and extremely comprehensive, and should advance the field.

Nevertheless, the manuscript is also very long (but justifiably so), and certain statements could be a little clearer. Most of these statements refer to the comparison with the so-called rate equation (RE) methods, with which I'm more familiar. For example:

Abstract: "Furthermore, the Bayesian filter delivers unbiased estimates for a wider range of data quality and identifies parameters which the rate equation approach does not identify."

The first part of this statement is not quite true, as Figure 4 shows clearly that the Bayesian estimates are biased (and the authors acknowledge this elsewhere in the manuscript). If they are biased in one "range of data quality", that probably means they are always biased, just to different degrees. This is not surprising, because the Kalman filter is a continuous state approximation to a discrete state process, and the overall estimation algorithm makes a number of approximations to intractable probability distributions. It would definitely be correct to say that the estimates are very good, but not unbiased.

Second, this statement is also ambiguous. Are you referring to the theoretical non-identifiability caused by having more parameters in the model than what the combination of estimator+experimental protocol can extract from data? In this case, it's not a matter of certain parameters that cannot be identified, but a matter of how many can be identified uniquely. The more information is extracted from the data, the more unique parameters can be identified, so the Kalman filter should do better. Or, alternatively, are you referring to specific parameters that are poorly identified because, for example, they refer to transitions that are rarely undertaken by the channel? In this case, it would be a matter of obtaining looser or tighter estimates with one method or another, but the parameters should be intrinsically identifiable, I imagine, regardless of the algorithm. In any case, it's not clear that the better identifiability is the result of the Bayesian side, or of the predictor-corrector state inference filter. I would guess it is the Kalman filter, but I'm not sure.

Perhaps it would be clearer if you said that the KF method produces good estimates and generally improves parameter identifiability compared to other methods, as it extracts more information from the data?

Introduction:

32: I'm not sure, but if the intention here is to cite mathematical treatments for estimation, you may add references to the "macroscopic" papers by Celentano, Milescu, Stepaniuk and perhaps a few others that use "rate equations". Also, you may cite Qin et al., 1996, as a single channel paper describing a method used in hundreds of studies.

Pg. 3:

51: I remain skeptical that it is a good idea to use "rate equations" (RE) as a term to refer to those methods that are fundamentally different from the approach described here (also see my comment to the first submission). The rate equations must always be used to predict a future state from a past or current state, by all methods, explicitly or implicitly, because REs simply describe the channel dynamics. In this very manuscript, Equation 3, central to the Kalman filter formalism, is nothing but a deterministic rate equation with a stochastic term added to approximate the stochastic evolution of an ensemble of channels. In fact, there are some old papers by Fox and some more recent by Osorio (I'm not exactly sure of the name and I don't remember the years) that discuss that approximation and its shortcomings – perhaps that is the source of bias?

Whether that prediction is then corrected, as in the Kalman filter approach, with a corrector step is irrelevant, as far as the rate equations. Furthermore, it's all a matter of degree. For example, the Milescu et al. approach, which is classified here under the RE umbrella, predicts future states as a mean + variance (or as a mean only), but only using the initial state. There is no correction at each point, as with the Kalman filter method, but there is a correction of the initial state from one iteration to the next (by the way, it's not clear if you implemented that feature here, which would make a big difference). Then, because it considers the stochastical aspect of the data, the Milescu et al. approach should also be considered a stochastic method, just one that doesn't use all the information contained in the data (and so it is fast). Imagine a situation where you ran the same stimulation protocol multiple times, but each time you record only one data point, further and further away from the beginning of the stimulation protocol. A "stochastic" algorithm applied to this type of data would be exactly as described in Milescu et al. Of course, in reality all points are recorded in sequence, but that doesn't mean that the approach is not stochastic, just that it 's simplifying and discarding some information to gain speed. All methods (such as the Kalman filter described here) make some compromises to reduce complexity and increase speed.

The bottom line is that there is the most basic approach of solving the rate equations deterministically, without considering any variance whatsoever, and then there is everything else.

58: "Thus, a time trace with a finite number of channels contains, strictly speaking, only one independent data point."

I don't understand this sentence. Could you please clarify?

74: "The KF is the minimal variance filter Anderson and Moore (2012). Thus, instead of excessive analog filtering of currents with the inevitable signal distortions Silberberg and Magleby (1993) one can apply the KF with higher analysing frequency on less filtered data."

Yes, but I'm not sure why should we use excessive filtering? Where is this idea coming from?

131: "However, even with simulated data of unrealistic high numbers of channels per patch, the KF outperforms the deterministic approach in estimating the model parameters."

It is clearly true from your figures, but please give a number as to what is unrealistic (10,000? 100,000?). Also, outperforms, but by how much? As I commented above and below, all methods tested here seem to produce good estimates under the conditions they were designed for (and even outside), and one might argue that it's not worth adding the additional computational complexity and running time for a possibly small increase in accuracy. How is one to judge that increase in accuracy?

276: Has the RE method been used with the mean + variance or mean only? Also, how was the initial probability vector calculated with the RE method? If you used the mean + variance, then (as mentioned above), you can't call it deterministic. If you used only the mean, then it is indeed a deterministic method, but it's not the approach described in Milescu et al. Please explain.

229: "added, in Equation 9 to the variance … which originates (Equation 38d) from the fact that we do not know the true system state"

Which noise are you referring to? The state noise or the measurement noise?

326: Which are the two algorithms?

278: "Both former algorithms are far away from the true parameter values with their maxima and also fail to cover the true values within reasonable tails of their posterior."

I think the authors might have gotten a little carried away when they made this statement. There is no doubt that the Kalman/Bayesian method produces more accurate estimates, but the other two methods (KF and RE) are very reasonable as well. I see estimates that are within 5, 10, or 20% from the true values, for most parameters. This is not "failure" by any stretch of the imagination. Most people would call this quite good, given the nature of the data.

294: "The small advantage of our algorithm for small … over Moffatt (2007) is due to the fact that we could apply an informative prior in the formulation of the inference problem … by taking advantage of our Bayesian filter. "

This is an interesting and important statement. I interpret it as saying that the Bayesian aspect itself makes only a small contribution to the quality of the estimates, when comparing it with the Moffatt method, which is a Kalman filter as well. The only issue with the Moffatt method is the lack of an explicit formalism for the excess state noise (which could presumably be added). It also suggests to me that any method that tries to use the noise may run into difficulties when the noise model is unknown (typical real-life scenario). The Moffatt method is confronted with unknown noise and it fails. What about when the Bayesian method is confronted with unknown noise? There are some comments in the manuscript, but nothing tangible. Could you please comment?

Figure 3: There are no data sets in the figure. What data were analyzed here?

Is there a typo regarding the colors in a? What are the red, blue, black, green symbols? Please verify.

Assuming the red is KF, there is something very curious about its estimates, which are very different in distribution from the Bayesian estimates. Could there be a coding problem? If red is actually RE, then it would make more sense. Could you explain? Is this the effect of the "excessive" open state noise? If so, I find this situation a bit unfair, because then the 2007 KF algorithm is tested with data that it is not meant to work with.

Also, I think it would be more interesting to have a comparison between the original KF and the newer Bayesian approach, so we can understand what Bayesian estimation does. In any case, I can't really interpret the data until you clarify the colors.

The legend is unclear overall.

303: What means "singular"?

324: What shaded area in Figure 1a? Perhaps you mean Figure 4a?

Figure 4: I don't see any light green.

368: "The estimated true success rate by the RE approach (blue) is ≈ 0.15 and therefore far away from the true success probability. In contrast, the posterior (green) of the true success probability of the KF resides with a large probability mass between the lower and upper limit of the success probability of an optimal algorithm (given the correct kinetic scheme)."

I'm really a bit puzzled here: yes, the KF is more accurate (given the correct kinetic scheme), but what I see in this figure is that both algorithms are biased, yet both are generally within 10% (and quite a bit better for KF) of the true values. If one would plot the log of the rates, to transform into δ Gs, the differences would be even smaller. I would bet that experimental artifacts would contort the estimates to a greater degree anyway.

It's very nice that the RE approach was embedded and tested within a Bayesian framework, but it would still be interesting to know what is the contribution of the Bayesian aspect (unless I missed this point in the manuscript).

436: "…while their error ratio (Figure 7a) seems to have no trend to diminish with increasing NCh".

This would be unexpected, because the Kalman filter will always use more information than RE. Why would the KF approach become relatively more erroneous at higher Nc? I don't see any reason. To me, an important question is when do the overall errors become dominated by external factors, such as recording artifacts, using the wrong model, etc.

511: "Thus, transferring the unusually strictly applied algebraic constraint Salari et al. (2018) of microscopic-reversibility to constraint with scalable softness we can model the lack information if microscopic-reversibility is exactly fulfilled Colquhoun et al. (2004) by the given ion channel instead of forcing it upon the model."

I'm not sure I understand what you mean here. I think it is very usual to constrain microscopic reversibility EXACTLY, whether through the SVD method (Qin et al., Plested et al., Milescu et al., Salari et al), or through some other algebraic method (Plested et al). It's not "forcing" it on the channel, but simply testing the data for that condition. Of course, one could test the condition where there is no reversibility enforced at all (i.e., it's "given by the channel"), or anything in between.

675: "With our algorithm we demonstrate (Figure 3c and 7) that the common assumption that for large ensembles of ion channels simpler deterministic modeling by RE approaches is on par with stochastic modeling, such as a KF, is wrong in terms of Euclidean error and uncertainty quantification (Figure 5a-c and Figure 6a-b)".

I find this statement a little subjective. I think anyone who cares about stochastic vs. deterministic modeling knows enough that any method that uses more information from data should produce better estimates, regardless of the number of channels. I would say that the more likely assumption is that deterministic estimators produce poor estimates with small numbers of channels, perfect estimates with infinitely many channels, and anything in between. In fact, the KF method behaves exactly the same way, just with overall higher accuracy. Looking at the tests in this manuscript, I would say that all the previous studies that modeled macroscopic data using deterministic methods are safe. They don't need to be redone. The future, of course, is a different matter.
