# Peer review - Round 1

Editors:
- Damon A Clark, https://ror.org/03v76x132 Yale University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83289.sa0](https://doi.org/10.7554/eLife.83289.sa0)

This useful article describes a sensitive method for identifying the contributions of different behavioral and stimulus parameters to neural activity. The method has been convincingly validated using simulated data and applied to example state-of-the-art datasets from mouse and zebrafish. The method could be productively applied to a wide range of experiments in behavioral and systems neuroscience.


---

# Peer review - Round 1

Editors:
- Damon A Clark, https://ror.org/03v76x132 Yale University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83289.sa1](https://doi.org/10.7554/eLife.83289.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A model-free approach to link neural activity to behavioral tasks" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers were positive about the paper's approach. Below are several points agreed upon by the reviewers that would be important to address before potential publication.

1) R1 had several critiques of the comparison to STA/STC. All reviewers agree that a more complete exposition of the differences between this method and STA/STC would benefit the paper. This could include synthetic cases where the proposed methods works better than STA/STC (for instance requiring less data) or real examples from the datasets where the proposed method is better at classifying cell response types. This paper should describe or show the advantages of this type of analysis over prior ones, ideally using good apples-to-apples comparisons.

a. Relatedly, R1 was also skeptical of the utility of the linear methods shown in Figure 1; the other reviewers convinced R1 that the limited linear models used were in keeping with standard methods in the zebrafish field. The authors should better describe why these particular (limited) linear models were used, and perhaps cite examples from the field in support of these sorts of models.

2) The paper was a bit dense in some sections. The reviewers recommend moving some more mathematical details to the supplement and focusing on the most important results in the main text. (An example might be the curvature metric, which was a little opaque and did not seem central.)

3) The authors should draw finer distinctions between their method and some other, similar, prior methods, like the Ganguli/Baccus papers that used convolutional networks to fit retinal ganglion cell responses, in an approach that seems similar in some ways to the one used here. This relates also to several reviewer comments about what method exactly is being referred to as 'MINE'.

4) Figure 7: The authors should explain the significance of the result in Figure 7 with respect to signal processing. Are the authors saying that higher order interactions occur deeper in processing? This complexity analysis may also be an example of an approach that is possible with what is presented here but not with STA/STC.

Reviewer #1 (Recommendations for the authors):

1) In MINE's first mention (line 43) and in showing that it can capture various response features, the authors seem to imply that MINE is simply the idea of using ANNs to model neural activity as function of either independent or dependent variables. But surely this has already been done many times. I'm having some trouble seeing what precisely is claimed as new in MINE. My thought was that it is also the first and second order interpretation, but that does not come through in the early descriptions of the method.

2) Related to this, in L55, the authors remark "Aside from network architecture and initialization conditions MINE is essentially model-free." This is a pretty big constraint, by the model architecture, choice of activation function, etc. STA and STC and systems identification methods more generally seem far more truly model free. This suggests that the framing and title here might need significant reconsideration.

3) The authors make several claims about linear models in Figure 1 that I cannot figure out. In particular, at L137, the authors say that the linear model cannot learn the dynamics of the calcium indicator. But why not? If the stimulus is s_t, the kernel is k_t, and the response is r_t = (s*k)_t + eta_t, then this is exactly what a linear model should be able to learn perfectly, directly from the data through a least squares fit at each time point. I don't understand why an expanded linear model should be required to learn the calcium kernel. In 1F, why is the LM not working as well as the ANN for S1 and M2? Those appear to both be simple linear transformations where r_t = (s*k)_t + eta_t: perfect for a linear model and least squares fitting. (In fact, with Gaussian noise, no model should be able to outperform the least squares fit linear model to estimate k, given sufficient data.) Similarly, dS1/dt is still just a linear transformation of S1 and should be easily learned by a linear model, since it's now just r_t = (s*k')_t + eta_t, where k' is the derivative of the calcium kernel. These results – that the authors' linear model is not capturing linear transformations that exactly match the form of the linear model – are truly puzzling.

4) One of the big proposed advances of this paper is the interpretability of the fitted ANN model. By doing "Taylor expansion" on the model, the authors pull out linear and quadratic terms that describe the dependency of neurons on different non-neural variables (dependent and independent) in these experiments. I have a few comments on this, some more critical than others. Overall, I was not left with a strong sense of what the benefit is, if any, of this method over standard systems identification approaches.

a. This sort of expansion of a functional has more typically been called a Volterra expansion, and there exists a giant literature on estimating Volterra kernels for nonlinear systems. It would be appropriate to cite some of that work and adopt the terminology used in prior work in the field.

b. In comparing their methods to spike-triggered analyses, Figure 4 is not a fair comparison, since it has not decorrelated the stimuli in time, as has been in wide practice in systems identification for quite a while (see Korenberg in the 1990s, Baccus and Meister, 2002). Thus the fair comparison is with S4, and 4 should not be viewed as comparable and quite likely removed.

c. In the comparison between the Jacobian/Hessian of the ANN and the STA/STC equivalents in Figures4 and S4, I don't understand the authors' choice of nonlinearities, which are described after line 1105. In particular, g_sta(x) has a first derivative at x=0, but it's second derivative evaluated at x=0 is also non-zero. By adding this to the other function and putting them through a ReLU (equation 19), there will be both linear and quadratic components for both RFa and RFv, even if g_stc is symmetric, simply because the ReLU is approximated by a linear + quadratic (+ higher) terms. This means that with these functions, I would expect the STA to be a linear combination of the two linear projections (RFa and RFv) and I would expect the STC matrix to have eigenvectors spanning the 2-dimensional space of RFa and RFv. It's less clear why this isn't happening in the simulations. RFa could dominate the STA. In Figure 4B, it seems clear that the STC is contaminated by the STA, and given the analysis above, that is not surprising. Is that what is lowering the cosine similarity for the STC analysis in S4? Is only the first eigenvector being considered? If so, it's frequently the case that the STC dimensions also include the STA dimension; often, one reports only the STC components after the STA has been subtracted off. (See for instance Aljadeff et al., 2016.) It looks here as though the authors just report the eigenvector with largest eigenvalue. Is the STC really not working well, or is it just including components of the other filter (appropriately)? It's hard to believe that STC applied to a point nonlinearity acting on two projections of the stimulus would not return eigenvectors that span those two projections of the stimulus.

d. This brings up a conceptual point. The decomposition that the authors perform of the ANN into zeroth, first, second, and higher order terms in Figure 7D could just as easily be written for the raw responses of the neurons. In such a case, with an excellent model, the two expansions should be closely related to one another, and in some cases equivalent. The low-order terms in the Volterra series, when estimated experimentally, depend on higher order terms. (For instance a cubic Volterra term would show up in the linear filter.) Wiener series are typically estimated instead, since these produce an orthogonalized basis, so that this dependence is eliminated (for a given amplitude of inputs X). When computing the STC, one can eliminate the linear component first; that would then be the Wiener estimate of the second order kernel. The second order kernel computed as the Hessian of an ANN is not orthogonalized in the same way, so it might produce different results from STC, but it is not clear that this is what the authors show, or intend to show.

e. The authors on L346 say that higher order terms are contained in the ANN, so that the Jacobian will be different from spike triggered covariance analysis. I think this is correct. However, I'm not sure that makes the Hessian or Jacobian in the ANN a better analysis than the systems identification approaches. In my mind, this is potentially the only advantage of doing this ANN method over STA and STC; but if that's the advantage, then I'd want to be shown very clearly an example where this occurs and where the insight into the system was improved by using the Jacobian/Hessian rather than STA/STC. I imagine that such benefits could accrue when the fitted ANN is close to the true set of transformations of the system, but that would reduce the advantages of being able to do this with any old ANN. Overall, these comments get to the point of: under what conditions would the Jacobian/Hessian/ANN method be better or somehow more informative than STA/STC? And why fit to the ANN if one is going to interpret it with methods equivalent to STA/STC that could be performed directly on the data?

Reviewer #2 (Recommendations for the authors):

While the paper could certainly be published in the current form, there are some points that as a reader I would like to have seen addressed further. I therefore offer some comments and suggestions that the authors might like to consider.

I believe there is a mistake in the formulae given for the Taylor metric in the Methods. Since the R^2 Full is always greater than the R^2 with fewer parameters, the formulae, as written, appear to give a number between 0 and -infinity, whereas I think the intention is that they should give a number between 0 and 1 (as appears in the paper).

An important consideration when comparing approaches to modeling neuronal responses is how much data is required to fit the model. In the comparison with regression models, or with the spike-triggered average it would be useful to show how the performance of each approach develops with the length of recording.

The paper could be improved, and the method made more appealing, by more clearly showing qualitative improvements that their approach offers over variations of linear regression methods. In the zebrafish part, there is a convincing argument made that the method allows more neurons to be fit at some threshold, but direct comparison of the outputs of both approaches is restricted to counting the numbers of ROIs identified in various classes. One possible explanation could be that these differences arise because the model-free method has greater sensitivity for identifying neurons within the same classes that are found with the LM method, but it would be more interesting if the model free method finds particular types of neurons that are clearly missed by the LM method. What could be compelling to see, for example, would be (1) differences in the spatial distributions of neuron classes found with the two methods, e.g. regions where neurons are only found with the model-free method or (2) Evidence that there are specific functional classes that are missed with the LM method – e.g. do the RF clusters vary in how well they are picked up by the LM?

It would be helpful to have some more information about the choice of network architecture, and how this was optimized. For example, 80 features in the convolutional layer seems like a lot for these relatively simple data sets, and it would be good to understand better how this number was chosen and how this choice can affect the outcome.

Intuitively, it seems like the temporal effects of the calcium indicator response would ideally be applied downstream of the computation of the neural response, but, in the text, this step is described as happening in the first layer of linear convolutional filters. Is this a constraint of the network design, and are there any practical consequences for the possible computations captured by the model?

I don't like that the distributions of neuronal types seem to be shown in the form of renderings of anatomical masks highlighting regions of enrichment. This rather obscures the true distributions, and makes them appear more cleanly separated than they are. For me, these visualizations don't offer much information that goes beyond the tabulation of regions. A direct representation of the density of different functional classes, as is often used in the field, would be richer in information, and might be a way to highlight qualitative differences between the populations identified using the LM and model-free approaches. Even if it is the case that there are not strong differences in the distributions of functional types, this by itself would be an interesting observation that merits discussion.

I would like to see more discussion of how the neural network models could be explored or leverage to give more insight into the responses of individual neurons. For example, having identified the relevant variables, and model complexity, could this information be used to explore simpler models in a more constrained way? Could visualization approaches like those used in Heras et al. 2019 https://doi.org/10.1371/journal.pcbi.1007354, be used to explore how the network is combining task variables?

Since the function is scalar valued, I believe that what is referred to in the paper as the Jacobian is also simply the gradient of the function. Perhaps this could be mentioned explicitly to aid understanding for a broad audience.

Overall, I congratulate the authors on developing this useful method, and I look forward to seeing it published.

Reviewer #3 (Recommendations for the authors):

1. Overall, as mentioned in my Public Review section, I believe the paper is very valuable and merits publication in eLife. I do think that it would be a pity if the manuscript was not carefully re-read and rewritten to make it more accessible for the average reader who may want to implement this analysis on their data. An option would be to shift more material to the Methods and use the main text to convey the method and compare it with the available ones for the 3 datasets that are treated.

2. It would help to understand the various thresholds that appear throughout. I am, for example, not sure what to conclude from the sentence that starts on line 224 or how to interpret the red dashed line in Figure 5B (line 421).

3. Given that the zebrafish experiments were performed by the authors, could they comment on the reliability (across animals) in finding the functional activity described in Figures 6 and 7?

4. The code and data availability is exemplary.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A model-free approach to link neural activity to behavioral tasks" for further consideration by eLife. Your revised article has been evaluated by Michael Frank (Senior Editor) and a Reviewing Editor.

The manuscript has been much improved, but there is one large and a few small remaining issues that need to be addressed, as outlined below:

There is only one issue that remains, and it is the issue of calling this a "model-free" approach, noted by R1. Since no analysis is truly model free, there is a spectrum of how much constraint a model puts on an analysis. There are other approaches discussed in the paper that are closer to the model free end than this one (like STA, STC, MID), so this term does not seem like the right one to use in this case. The authors should find a more accurate description of what their method brings to field.

Reviewer #1 (Recommendations for the authors):

I appreciate the care that the authors have taken in addressing the concerns raised in the first round. I believe that the major hurdles were cleared in the revision. However, I do have a few comments that I believe should be addressed before final acceptance/publication.

1) This method is definitely not "model free". It is a relaxed model requirement, or potentially a very general model, or a model with few assumptions, but I don't think it's just a matter of opinion as to whether it's "model-free". Especially in comparison with STA and STC and Maximally informative dimensions, which all have even less of an underlying model framework… At a very basic level, the title and acronym must be accurate. Later in the paper, the authors argue that this method's model is actually providing important regularizing power in computing STC, etc. So it is definitely not model free, and the authors must find a different description for the title (and the acronym). I'm sure they can do this, but some suggestions: "Flexible INE"? CNNINE? "Canine"? "Convolutional neurAl Network Identification of Neural Encoding"? Something else? "Model-agnostic"?

2) Figure 7BC. The temporal kernels found by this method are a bit weird and seem not very biological – much of the power lies at 0 and 10 seconds, the two ends of the filter… Is this because the filters aren't long enough? These look quite different from true filters I'd expect to find in neurons, both in their duration and shape. I think this deserves some kind of explanation. I apologize that I didn't note this on the first round – I clearly got distracted by some other parts of the analysis.
