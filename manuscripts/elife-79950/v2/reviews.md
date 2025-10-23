# Peer review - Round 1

Editors:
- Gordon J Berman, https://ror.org/03czfpz43 Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79950.sa0](https://doi.org/10.7554/eLife.79950.sa0)

This paper is an important study that is of interest to neuroscientists studying the organization of neural activity and behavior. The authors present compelling evidence to link the apparently scale-free distributions of behavioral metrics with scale-free distributions of neural activity. They then explore computationally mechanistic models that could account for these observations. The simulations of mechanistic models are provocative and suggest interesting network-connectivity hypotheses to test in future experiments.


---

# Peer review - Round 1

Editors:
- Gordon J Berman, https://ror.org/03czfpz43 Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79950.sa1](https://doi.org/10.7554/eLife.79950.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Scale-free behavioral dynamics directly linked with scale-free cortical dynamics" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Ronald Calabrese as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Keith B Hengen (Reviewer #1).

The reviewers have discussed their reviews with one another, and although there were some concerns, there was general enthusiasm for the approach and for the ideas presented in the work. Accordingly, the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The reviewers would like to see a detailed and thoughtful reflection on the role that 3 Hz Ca imaging might play in the conclusions that the authors derive. While the dataset in question offers many neurons, this approach is, from other perspectives, impoverished – calcium intrinsically misses spikes, a 3 Hz sampling rate is two orders of magnitude slower than an action potential, and the recordings are relatively short for amassing substantial observations of low probability (large) avalanches. The potential concern is that some of this disconnect may reflect optophysiological constraints. One argument against this is that a truly scale free system should be observable at any temporal or spatial scale and still give rise to the same sets of power laws. This quickly falls apart when applied to biological systems which are neither infinite in time nor space. As a result, the severe mismatch between the spatial resolution (single cell) and the temporal resolution (3 Hz) of the dataset, combined with filtering intrinsic to calcium imaging, raises the possibility that the conclusions are influenced by the methods.

2. Another reservation expressed by the referees has to do with the generality of the conclusions drawn from the mechanistic model. One of the connectivity motifs identified appears to be i+ to e- and i- to e+, where potentially i+/i- are SOM and VIP (or really any specific inhibitory type) cells. The specific connections to subsets of excitatory cells appear to be important (based on the solid lines in Figure 8). This seems surprising: is there any experimental support for excitatory cells to preferentially receive inhibition from either SOM or VIP, but not both? More broadly, there was concern that the neat diagrams drawn here are misleading. The sample raster, showing what appears to be the full simulation, certainly captures the correlated/anti-correlated pattern of the 100 cells most correlated with a seed cell and 100 cells most anti-correlated with it, but it does not contain the 11,000 cells in between with zero to moderate levels of correlation. We probably expect that the full covariance matrix has similar structure from any seed (see Meshulam et al. 2019, PRL, for an analysis of scaling of coarse-grained activity covariance), and this suggests multiple cross-over inhibition constraints, which seem like they could be hard to satisfy. The motifs identified in Figure 8 likely exist, but I am left with many questions of what we learned about connectivity rules that would account for the full distribution of correlations. Would starting with an Erdos-Renyi network with slight over-representation of these motifs be sufficient? How important is the homogeneous connection weights from each pool assumption – would allowing connection weights with some dispersion change the results?

3. Putting 2) another way, it's unclear why the averaging is required in the first place. This operation projects the entire population down in an incredibly lossy way and removes much of the complexity of the population activity. Second, the authors state that it is highly curious that subsets of the population exhibit power laws while the entire population does not. While the discussion and hypothesizing about different e-i interactions is interesting, it is possible that there's a discussion to be had on a much more basic level of whether there are topology independent explanations, such as basic distributions of correlations between neurons that can explain the subnetwork averaging. Specifically, if the correlation to any given neuron falls off, e.g., with an exponential falloff (i.e., a Gaussian Process type covariance between neurons), it seems that similar effects should hold. This type of effect can be easily tested by generating null distributions existing code bases. This is an important point since local (broadly defined) correlations of neurons implying the observed subnetwork behavior means that many mechanisms that have local correlations but don't cluster in any meaningful way could also be responsible for the local averaging effect.

4. In general, the discussion of "two networks" seems like it relies on the correlation plot of Figure~7B. The decay away from the peak correlation is sharp, but there does not seem to be significant clustering in the anti-correlation population, instead a very slow decay away from zero. The authors do not show evidence of clustering in the neurons, nor any biophysical reason why e and i neurons are present in the imaging data. The alternative explanation (as mentioned in (b)) is that the there is a more continuous set of correlations among the neurons with the same result. In fact one of the reviewers tested this themself using code to generate some data with the desired statistics, and the distribution of events seems to also describe this same observation. Obviously, the full test would need to use the same event identification code, and so it is quite important that the authors consider the much more generic explanation for the sub-network averaging effect. We recommend assessing the possibility that broader explanations, e.g., in the form of the distributions of correlations accounts for the observed phenomenon. Even with 10K neurons, there are many other forces at play influencing the observed network and while it is nice that e-i networks are one explanation, much less constraining explanations that are still biophysically feasible should be discussed and compared against. I have provided one possible approach (see PDF for code and example figure: https://submit.elifesciences.org/eLife_files/2022/05/19/00107349/00/107349_0_attach_6_474_convrt.pdf).

5. Another important aspect here is how single neurons behave. It was not clear if single neurons were stated to exhibit a power law. If they do, then that would help in that there are different limiting behaviors to the averaging that pass through the observed stated numbers. If not, then there is an additional oddity that one must average neurons at all to obtain a power law. We recommend the authors show the full curve so that the readers get a more detailed sense of how averaging effects the power-law interpretation of the data.

6. There is something that seems off about the range of \β values inferred with the ranges of \tau and $\α$. With \tau in [0.9,1.1], then the denominator 1-\tau is in [-0.1, 0.1], which the authors state means that \β (found to be in [2,2.4]) is not near \β_{crackling} = (\α-1)/(1-\tau). It seems as this is the opposite, as the possible values of the \β_{crackling} is huge due to the denominator, and so \β is in the range of possible \β_{crackling} almost vacuously. Was this statement just poorly worded?

7. It is not clear if there is more to what the authors are trying to say with the specifics of the scale free fits for behavior. Apparently, these results are used to motivate the neural studies, but aside from that, the details of those ranges don't seem to come up again. Given that the primary connection between neuronal and behavioral activity seems to be Figure 4. The distribution of points in these plots seem to be very lopsided, in that some plots have large ranges of few-to-no data points. It would be very helpful to get a sense of the distribution of points that are a bit hard to see given the overlapping points and super-imposed lines. We recommend that the authors add distribution information to the plots in Figure 4B to give a sense of how points are spread through the [correlation with behavior]-by-[power law range] space. Potential plots might be a co-located histogram, or perhaps an uncertainty estimate as a function of correlation based on the number of points and variance. This would help show significance of the curves in a way that accounts for the uneven spread of datapoints.

8. Neural activity correlated with some behavior variables can sometimes be the most active subset of neurons. This could potentially skew the maximum sizes of events and give behaviorally correlated subsets an unfair advantage in terms of the scale-free range. In a similar vain to 8), what are the typical dynamic ranges for subsets correlated and uncorrelated with behavior? We recommend showing a number of these to see if those dynamic ranges are impacting the possible ranges in the [correlation with behavior]-by-[power law range] plots. Perhaps something like curve in each plot showing the minimum maximum value of the power law range per correlation range. In general, the reviewers struggled with the interpretation of Figure 4b in the sense that there seems to be such variability between mice. How much do the authors feel that this is a difference in neural populations imaged, vs changes in imaging conditions (illumination, window clarity, optical alignment) or differences in mouse activity levels?

Reviewer #1 (Recommendations for the authors):

This paper feels highly polished and thorough in its presentation. I truly enjoyed reading it and believe it will be of value to the community.

A nuanced question: mouse #5 and mouse #6 consistently seems to break the rules implied by the rest of the dataset. The behavioral descriptors look normal in figure 2, but neural structure is notably different from the rest of the group in 3E, 4B, 6C, 7E, and S4 (that one is behavior). Is there anything meaningfully different about these recordings (n cells, mean event rate, anatomical location etc)?

Reviewer #2 (Recommendations for the authors):

Comments, questions, and technical issues for the authors.

1. The values of tau (size exponent) from neural avalanches are surprisingly low. For instance, in the Ma et al. (Hengen) 2019 Neuron paper, tau ranged from 1.5 to 1.9, sometimes more than 2, but never less than 1. I am wondering how the imaging preprocessing affects the estimate of tau. For instance, if you started with simulated spiking activity that has avalanches with size pdf that go as a power law with exponent tau, and then use a forward model to generate "calcium imaging," and then apply deconvolution, z-scoring, and low-pass filtering, and then measure the avalanches again: what is the new tau?

2. This may be an ignorant question (apologies). The power law range is quantified in decibels (dB) throughout the paper; do you actually mean decades?

3. Related to the set-up of the model, was there a reason that there are no adaptation mechanisms in this network model, as there often are in mechanistic models for avalanche criticality (including past work by the authors of this paper, e.g. Shew's 2015 Nature Physics paper)? Also, there appears to have been an error with the reference manager, as this reference shows up twice in the reference list.

4. It would be helpful the authors could elaborate on predictions that their results make for future studies. Maybe this is rather technical, but can you tell us when you expect to find a power-law distribution as a function of how much of the population is sampled and for how long? What if you were analyzing Neuropixels data, where you lose the extensive spatial sampling (and the restriction to pyramidal cells only) but you gain 3 orders of magnitude in temporal resolution?

5. On page 8, you ask "are all behavioral events equally correlated to their concurrent neural events, or are certain neural events from certain subsets of neurons more strongly related to behavioral events?" I don't understand the question. What does it mean for all behavioral events to be equally correlated to concurrent neural events? Aren't "concurrent neural events" in specific subsets of neurons?

Reviewer #3 (Recommendations for the authors):

1. Limits of calcium imaging: My recommendation is to assess mathematically the potential impact of missing data on the range and power-law slope estimates, which are the primary values used throughout the paper.

2. Correlations and power-laws in subsets.

2a-c. My recommendation is to assess the possibility that broader explanations, e.g., in the form of the distributions of correlations accounts for the observed phenomenon. Even with 10K neurons, there are many other forces at play influencing the observed network and while it is nice that e-i networks are one explanation, much less constraining explanations that are still biophysically feasible should be discussed and compared against. I have provided one possible approach (see PDF for code and example figure: https://submit.elifesciences.org/eLife_files/2022/05/19/00107349/00/107349_0_attach_6_474_convrt.pdf) that I hope will be useful to the authors.

2d. I recommend the authors show the full curve so that the readers get a more detailed sense of how averaging effects the power-law interpretation of the data.

3. Please check that this calculation and interpretation is correct.

4. Connection between brain and behavior:

4b. I recommend that the authors add distribution information to the plots in Figure~4B to give a sense of how points are spread through the [correlation with behavior]-by-[power law range] space. Potential plots might be a co-located histogram, or perhaps an uncertainty estimate as a function of correlation based on the number of points and variance. This would help show significance of the curves in a way that accounts for the uneven spread of datapoints.

4c. In a similar vein, what are the typical dynamic ranges for subsets correlated and uncorrelated with behavior? I recommend showing a number of these to see if those dynamic ranges are impacting the possible ranges in the [correlation with behavior]-by-[power law range] plots. Perhaps something like curve in each plot showing the minimum maximum value of the power law range per correlation range.

4d. In general I'm struggling with the interpretation of Figure~4b in the sense that there seems to be such variability between mice. How much do the authors feel that this is a difference in neural populations imaged, vs changes in imaging conditions (illumination, window clarity, optical alignment) or differences in mouse activity levels?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Scale-free behavioral dynamics directly linked with scale-free cortical dynamics" for further consideration by eLife. Your revised article has been evaluated by Timothy Behrens (Senior Editor) and a Reviewing Editor.

The manuscript has been improved, and the reviewers concurred that an eventual acceptance is likely, but there are some remaining issues that need to be addressed. Specifically, the reviewers think that it's important that you address the points raised by Reviewer #3 (see below) regarding the "Mechanisms vs. Statistics" questions.

Reviewer #1 (Recommendations for the authors):

The authors have responded effectively to previous reviews both in the updated writing (discussion and intro) as well as the models and results.

Reviewer #2 (Recommendations for the authors):

Overall the authors addressed my concerns adequately. The paper has important results and makes a valuable contribution.

Reviewer #3 (Recommendations for the authors):

I appreciate your time and effort to respond to my review points. I believe the majority of my points have been addressed. The main weakness I still see is the lack of discussion about the broader mechanisms beyond the basic structures described that could account for the observations (see below).

Mechanisms vs. Statistics

I would like to clarify my reason for bringing up this "statistical" viewpoint that I believe may have been lost in translation. The paper as it stands makes the following logical steps (in terms of the mechanistic model) 1) The data exhibits power law scaling under certain binning of neurons (effect E) and 2) One way to account for this effect E is to consider certain e-i models. This is reasonable, but the overall search for possible mechanisms seems to be a combination of intuition and trial and error. Different architectures were tried and either "passed" or "failed".

The purpose of bringing up the statistical properties needed was to hopefully raise a conversation around what core properties are needed to replicate this effect. As activity statistics and connectivity are intimately related in mechanistic models, such a characterization would point to how broad or narrow the family of mechanisms that are possible is: i.e. how significant is it that the given sampling of models in the papers points to certain configurations. The closest I can see is the discussion point here that I think fails to completely address this point:

"One possibility suggested by our model is that the scale-free dynamics we observe occur at the boundary between winner-less switching and single-winner locked-in dynamics (the red dashed line in Figures8E and F). Additional theoretical efforts are necessary to more fully explore how the traditional criticality hypothesis relates to the competitive criticality suggested by our model."

On the author's distinction between mechanisms and statistics, I do not believe the two are independent paths to choose between. Mechanisms have statistical signatures (so-called "statistical model") and data statistics inform which mechanisms are possible given data. At the end of the day, these are mathematical models that need to connect core concepts to data. My point for this particular paper, which I will try to say more clearly and succinctly now is that there are many possible mechanisms that could explain observed effect E. I was hoping in my prior review to spark a slightly longer discussion on what overall properties would such a family of mechanisms share. I fail to see how identifying core statistics that would pare down the possible mechanisms is at odds with looking for a mechanism that explains an effect.
