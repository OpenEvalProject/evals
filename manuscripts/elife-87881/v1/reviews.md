# Peer review - Round 1

Editors:
- Juan Alvaro Gallego, Imperial College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87881.4.sa0](https://doi.org/10.7554/eLife.87881.4.sa0)

This study presents a useful method for the extraction of behaviour-related activity from neural population recordings based on a specific deep learning architecture, a variational autoencoder. Although the authors performed thorough benchmarking of their method in the context of decoding behavioural variables, the evidence supporting claims about encoding is incomplete as the results may stem, in part, from the properties of the method itself.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87881.4.sa1](https://doi.org/10.7554/eLife.87881.4.sa1)

This work seeks to understand how behaviour-related information is represented in the neural activity of the primate motor cortex. To this end, a statistical model of neural activity is presented that enables a non-linear separation of behaviour-related from unrelated activity. As a generative model, it enables the separate analysis of these two activity modes, here primarily done by assessing the decoding performance of hand movements the monkeys perform in the experiments. Several lines of analysis are presented to show that while the neurons with significant tuning to movements strongly contribute to the behaviourally-relevant activity subspace, less or un-tuned neurons also carry decodable information. It is further shown that the discovered subspaces enable linear decoding, leading the authors to conclude that motor cortex read-out can be linear.

Strengths:

In my opinion, using an expressive generative model to analyse neural state spaces is an interesting approach to understand neural population coding. While potentially sacrificing interpretability, this approach allows capturing both redundancies and synergies in the code as done in this paper. The model presented here is a natural non-linear extension of a previous linear model (PSID) and uses weak supervision in a manner similar to a previous non-linear model (TNDM).

Weaknesses:

This revised version provides additional evidence to support the author's claims regarding model performance and interpretation of the structure of the resulting latent spaces, in particular the distributed neural code over the whole recorded population, not just the well-tuned neurons. The improved ability to linearly decode behaviour from the relevant subspace and the analysis of the linear subspace projections in my opinion convincingly demonstrates that the model picks up behaviour-relevant dynamics, and that these are distributed widely across the population. As reviewer 3 also points out, I would, however, caution to interpret this as evidence for linear read-out of the motor system - your model performs a non-linear transformation, and while this is indeed linearly decodable, the motor system would need to do something similar first to achieve the same. In fact to me it seems to show the opposite, that behaviour-related information may not be generally accessible to linear decoders (including to down-stream brain areas).

As in my initial review, I would also caution against making strong claims about identifiability although this work and TNDM seem to show that in practise such methods work quite well. CEBRA, in contrast, offers some theoretical guarantees, but it is not a generative model, so would not allow the type of analysis done in this paper. In your model there is a para,eter \alpha to balance between neural and behaviour reconstruction. This seems very similar to TNDM and has to be optimised - if this is correct, then there is manual intervention required to identify a good model.

Somewhat related, I also found that the now comprehensive comparison with related models shows that the using decoding performance (R2) as a metric for model comparison may be problematic: the R2 values reported in Figure 2 (e.g. the MC_RTT dataset) should be compared to the values reported in the neural latent benchmark, which represent well-tuned models (e.g. AutoLFADS). The numbers (difficult to see, a table with numbers in the appendix would be useful, see: https://eval.ai/web/challenges/challenge-page/1256/leaderboard) seem lower than what can be obtained with models without latent space disentanglement. While this does not necessarily invalidate the conclusions drawn here, it shows that decoding performance can depend on a variety of model choices, and may not be ideal to discriminate between models. I'm also surprised by the low neural R2 for LFADS I assume this is condition-averaged - LFADS tends to perform very well on this metric.

One statement I still cannot follow is how the prior of the variational distribution is modelled. You say you depart from the usual Gaussian prior, but equation 7 seems to suggest there is a normal prior. Are the parameters of this distribution learned? As I pointed out earlier, I however suspect this may not matter much as you give the prior a very low weight. I also still am not sure how you generate a sample from the variational distribution, do you just draw one for each pass?

Summary:

This paper presents a very interesting analysis, but some concerns remain that mainly stem from the complexity of deep learning models. It would be good to acknowledge these as readers without relevant background need to understand where the possible caveats are.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87881.4.sa2](https://doi.org/10.7554/eLife.87881.4.sa2)

Li et al present a method to extract "behaviorally relevant" signals from neural activity. The method is meant to solve a problem which likely has high utility for neuroscience researchers. There are numerous existing methods to achieve this goal some of which the authors compare their method to-thankfully, the revised version includes one of the major previous omissions (TNDM). However, I still believe that d-VAE is a promising approach that has its own advantages. Still, I have issues with the paper as-is. The authors have made relatively few modifications to the text based on my previous comments, and the responses have largely just dismissed my feedback and restated claims from the paper. Nearly all of my previous comments remain relevant for this revised manuscript. As such, they have done little to assuage my concerns, the most important of which I will restate here using the labels/notation (Q1, Q2, etc) from the reviewer response.

(Q1) I still remain unconvinced that the core findings of the paper are "unexpected". In the response to my previous Specific Comment #1, they say "We use the term 'unexpected' due to the disparity between our findings and the prior understanding concerning neural encoding and decoding." However, they provide no citations or grounding for why they make those claims. What prior understanding makes it unexpected that encoding is more complex than decoding given the entropy, sparseness, and high dimensionality of neural signals (the "encoding") compared to the smoothness and low dimensionality of typical behavioural signals (the "decoding")?

(Q2) I still take issue with the premise that signals in the brain are "irrelevant" simply because they do not correlate with a fixed temporal lag with a particular behavioural feature hand-chosen by the experimenter. In the response to my previous review, the authors say "we employ terms like 'behaviorally-relevant' and 'behaviorally-irrelevant' only regarding behavioral variables of interest measured within a given task, such as arm kinematics during a motor control task.". This is just a restatement of their definition, not a response to my concern, and does not address my concern that the method requires a fixed temporal lag and continual decoding/encoding. My example of reward signals remains. There is a huge body of literature dating back to the 70s on the linear relationships between neural and activity and arm kinematics; in a sense, the authors have chosen the "variable of interest" that proves their point. This all ties back to the previous comment: this is mostly expected, not unexpected, when relating apparently-stochastic, discrete action potential events to smoothly varying limb kinematics.

(Q5) The authors seem to have missed the spirit of my critique: to say "linear readout is performed in motor cortex" is an over-interpretation of what their model can show.

(Q7) Agreeing with my critique is not sufficient; please provide the data or simulations that provides the context for the reference in the fano factor. I believe my critique is still valid.

(Q8) Thank you for comparing to TNDM, it's a useful benchmark.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87881.4.sa3](https://doi.org/10.7554/eLife.87881.4.sa3)

I am a new reviewer for this manuscript, which has been reviewed before. The authors provide a variational autoencoder that has three objectives in the loss: linear reconstruction of behavior from embeddings, reconstruction of neural data, and KL divergence term related to the variational model elements. They take the output of the VAE as the "behaviorally relevant" part of neural data and call the residual "behaviorally irrelevant". Results aim to inspect the linear versus nonlinear behavior decoding using the original raw neural data versus the inferred behaviorally relevant and irrelevant parts of the signal.

Overall, studying neural computations that are behaviorally relevant or not is an important problem, which several previous studies have explored (for example PSID in (Sani et al. 2021), TNDM in (Hurwitz et al. 2021), TAME-GP in (Balzani et al. 2023), pi-VAE in (Zhou and Wei 2020), and dPCA in (Kobak et al. 2016), etc). However, this manuscript does not properly put their work in the context of such prior works. For example, the abstract states "One solution is to accurately separate behaviorally-relevant and irrelevant signals, but this approach remains elusive", which is not the case given that these prior works have done that. The same is true for various claims in the main text, for example "Furthermore, we found that the dimensionality of primary subspace of raw signals (26, 64, and 45 for datasets A, B, and C) is significantly higher than that of behaviorally-relevant signals (7, 13, and 9), indicating that using raw signals to estimate the neural dimensionality of behaviors leads to an overestimation" (line 321). This finding was presented in (Sani et al. 2021) and (Hurwitz et al. 2021), which is not clarified here. This issue of putting the work in context has been brought up by other reviewers previously but seems to remain largely unaddressed. The introduction is inaccurate also in that it mixes up methods that were designed for separation of behaviorally relevant information with those that are unsupervised and do not aim to do so (e.g., LFADS). The introduction should be significantly revised to explicitly discuss prior models/works that specifically formulated this behavior separation and what these prior studies found, and how this study differs.

Beyond the above, some of the main claims/conclusions made by the manuscript are not properly supported by the analyses and results, which has also been brought up by other reviewers but not fully addressed. First, the analyses here do not support the linear readout from the motor cortex because (i) by construction, the VAE here is trained to have a linear readout from its embedding in its loss, which can bias its outputs toward doing well with a linear decoder/readout, and (ii) the overall mapping from neural data to behavior includes both the VAE and the linear readout and thus is always nonlinear (even when a linear Kalman filter is used for decoding). This claim is also vague as there is no definition of readout from "motor cortex" or what it means. Why is the readout from the bottleneck of this particular VAE the readout of motor cortex? Second, other claims about properties of individual neurons are also confounded because the VAE is a population-level model that extracts the bottleneck from all neurons. Thus, information can leak from any set of neurons to other sets of neurons during the inference of behaviorally relevant parts of signals. Overall, the results do not convincingly support the claims, and thus the claims should be carefully revised and significantly tempered to avoid misinterpretation by readers.

Below I briefly expand on these as well as other issues, and provide suggestions:

(1) Claims about linearity of "motor cortex" readout are not supported by results yet stated even in the abstract. Instead, what the results support is that for decoding behavior from the output of the dVAE model -- that is trained specifically to have a linear behavior readout from its embedding -- a nonlinear readout does not help. This result can be biased by the very construction of the dVAE's loss that encourages a linear readout/decoding from embeddings and thus does not imply a finding about motor cortex.

(2) Related to the above, it is unclear what the manuscript means by readout from motor cortex. A clearer definition of "readout" (a mapping from what to what?) in general is needed. The mapping that the linearity/nonlinearity claims refer to is from the *inferred* behaviorally relevant neural signals, which themselves are inferred nonlinearly using the VAE. This should be explicitly clarified in all claims, i.e., that only the mapping from distilled signals to behavior is linear, not the whole mapping from neural data to behavior. Again, to say the readout from motor cortex is linear is not supported, including in the abstract.

(3) Claims about individual neurons are also confounded. The d-VAE distilling processing is a population level embedding so the individual distilled neurons are not obtainable on their own without using the population data. This population level approach also raises the possibility that information can leak from one neuron to another during distillation, which is indeed what the authors hope would recover true information about individual neurons that wasn't there in the recording (the pixel denoising example). The authors acknowledge the possibility that information could leak to a neuron that didn't truly have that information and try to rule it out to some extent with some simulations and by comparing the distilled behaviorally relevant signals to the original neural signals. But ultimately, the distilled signals are different enough from the original signals to substantially improve decoding of low information neurons, and one cannot be sure if all of the information in distilled signals from any individual neuron truly belongs to that neuron. It is still quite likely that some of the improved behavior prediction of the distilled version of low-information neurons is due to leakage of behaviorally relevant information from other neurons, not the former's inherent behavioral information. This should be explicitly acknowledged in the manuscript.

(4) Given the nuances involved in appropriate comparisons across methods and since two of the datasets are public, the authors should provide their complete code (not just the dVAE method code), including the code for data loading, data preprocessing, model fitting and model evaluation for all methods and public datasets. This will alleviate concerns and allow readers to confirm conclusions (e.g., figure 2) for themselves down the line.

(5) Related to (1) above, the authors should explore the results if the affine network h(.) (from embedding to behavior) was replaced with a nonlinear ANN. Perhaps linear decoders would no longer be as close to nonlinear decoders. Regardless, the claim of linearity should be revised as described in (1) and (2) above, and all caveats should be discussed.

(6) The beginning of the section on the "smaller R2 neurons" should clearly define what R2 is being discussed. Based on the response to previous reviewers, this R2 "signifies the proportion of neuronal activity variance explained by the linear encoding model, calculated using raw signals". This should be mentioned and made clear in the main text whenever this R2 is referred to.

(7) Various terms require clear definitions. The authors sometimes use vague terminology (e.g., "useless") without a clear definition. Similarly, discussions regarding dimensionality could benefit from more precise definitions. How is neural dimensionality defined? For example, how is "neural dimensionality of specific behaviors" (line 590) defined? Related to this, I agree with Reviewer 2 that a clear definition of irrelevant should be mentioned that clarifies that relevance is roughly taken as "correlated or predictive with a fixed time lag". The analyses do not explore relevance with arbitrary time lags between neural and behavior data.

(8) CEBRA itself doesn't provide a neural reconstruction from its embeddings, but one could obtain one via a regression from extracted CEBRA embeddings to neural data. In addition to decoding results of CEBRA (figure S3), the neural reconstruction of CEBRA should be computed and CEBRA should be added to Figure 2 to see how the behaviorally relevant and irrelevant signals from CEBRA compare to other methods.

References:

Kobak, Dmitry, Wieland Brendel, Christos Constantinidis, Claudia E Feierstein, Adam Kepecs, Zachary F Mainen, Xue-Lian Qi, Ranulfo Romo, Naoshige Uchida, and Christian K Machens. 2016. "Demixed Principal Component Analysis of Neural Population Data." Edited by Mark CW van Rossum. eLife 5 (April): e10989. https://doi.org/10.7554/eLife.10989.

Sani, Omid G., Hamidreza Abbaspourazad, Yan T. Wong, Bijan Pesaran, and Maryam M. Shanechi. 2021. "Modeling Behaviorally Relevant Neural Dynamics Enabled by Preferential Subspace Identification." Nature Neuroscience 24 (1): 140-49. https://doi.org/10.1038/s41593-020-00733-0.

Zhou, Ding, and Xue-Xin Wei. 2020. "Learning Identifiable and Interpretable Latent Models of High-Dimensional Neural Activity Using Pi-VAE." In Advances in Neural Information Processing Systems, 33:7234-47. Curran Associates, Inc https://proceedings.neurips.cc/paper/2020/hash/510f2318f324cf07fce24c3a4b89c771-Abstract.html.

Hurwitz, Cole, Akash Srivastava, Kai Xu, Justin Jude, Matthew Perich, Lee Miller, and Matthias Hennig. 2021. "Targeted Neural Dynamical Modeling." In Advances in Neural Information Processing Systems. Vol. 34. https://proceedings.neurips.cc/paper/2021/hash/f5cfbc876972bd0d031c8abc37344c28-Abstract.html.

Balzani, Edoardo, Jean-Paul G. Noel, Pedro Herrero-Vidal, Dora E. Angelaki, and Cristina Savin. 2023. "A Probabilistic Framework for Task-Aligned Intra- and Inter-Area Neural Manifold Estimation." In . https://openreview.net/forum?id=kt-dcBQcSA.
