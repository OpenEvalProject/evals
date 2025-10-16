# Peer review - Round 1

Editors:
- Stephanie E Palmer, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.52599.sa0](https://doi.org/10.7554/eLife.52599.sa0)

This valuable work shows similarities between a multilayer, convolutional neural network trained to predict its next input and physiological features of visual processing in the brain. These solid results build on the authors' previous work and compare the match to real visual processing obtained by a hierarchical predictive network to that obtained by several other popular artificial neural networks. This work will be of interest to systems neuroscientists as well as computer scientists looking to make connections between normative theories of neural organization and training objectives in machine learning.


---

# Peer review - Round 1

Editors:
- Stephanie E Palmer, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.52599.sa1](https://doi.org/10.7554/eLife.52599.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Hierarchical temporal prediction captures motion processing along the visual pathway" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Joshua Gold as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Dan Yamins (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper expands on a predictive-coding-like unsupervised learning procedure and applies it to natural videos, training a multilayer, convolutional neural network with the objective of predicting the next input. The resulting network is qualitatively compared to several known neurophysiological features of the (dorsal) visual pathway, focusing on V1, but also comparing model results to receptive field properties of the LGN and area MT. The authors find center surround, simple, and complex cell behavior like that found in the retina, LGN, and V1. They also find units sensitive to drifting plaids. Matches between the predictive performance of this network are better than for a basic autoencoder and also better than several other models that ablate aspects of the proposed encoding rule. The paper hypothesizes that prediction might be a fundamental principle of self-organization in the visual system.

Essential revisions:

This paper advances a reasonable hypothesis about a very important goal: developing an unsupervised neural network model of the visual system. However, the current draft is not ready for publication because empirical validation of the model and comparison to equally reasonable alternatives are weak. The following revisions were deemed essential by the reviewing team:

1) Key controls are missing: a comparison between the results of the present work and other obvious alternative hypotheses should be included. Here are five comparisons that should be made, in order of increasing power:

a) A sparse autoencoder. A stacked autoencoder is tested, but it's not said whether this model was regularized with an activity sparsity penalty on the bottleneck or not. If not, this should be done.

b) A model based on temporal continuity / slowness rather than predictability. It's likely that pretty much the same spatial tuning properties would emerge, but that subtle differences in the temporal dynamics would be detectable. This would be particularly interesting in the light of a recent paper by Weghenkel and Wiskott [1] (2018, Neural Computation), which has shown no advantage of predictability over slowness on a large set of real world data sets.

c) A Gabor-wavelet-based model of V1. A good example of that is the Berkeley Wavelet Transform (BTW) in Willmore et al. [2]. Obviously this might not have the temporal processing facets of the authors' model, but the main comparisons made to data in Figure 6 don't require this. A very basic question is: how much better (or worse?) is the authors' model as a model of V1, as compared to the hard-coded (non-learned) "standard" model of V1 that the BWT represents?

d) The PredNet [3] and PredRNN [4] and PredRNN++ [5] models. These are predictive coding models similar to the one the authors propose. The authors of course do cite [3], but do not compare to its results. They definitely should. Merely noting that Prednet "has not been demonstrated [to] capture the phenomena that we describe …. " does not mean that PredNet *wouldn't* capture these phenomena. Being fairly familiar with PredNet , we imagine that it could indeed capture these features. Showing that it does not, and that the current proposal is thus a better fit to the data, is a burden that is clearly on the authors in the case. The code for prednet is publicly released and could easily be downloaded and run by the authors (trained on their training set). We also suggest strongly that the authors look at PredRNN as well, which may be substantially better than PredNet.

e) The early layers of a supervised deep neural network. This is an important baseline -- how much better (if at all) are these authors' models at matching V1 data than the supervised network, which is (as the authors correctly point out) obviously trained in a deeply unbiologial way? Work such as that of Cadena et al. [6] clearly shows that the supervised network actually gives very reasonable results in V1 -- in fact, it's the state-of-the-art model of V1 in the literature, at least to our knowledge. How much better is their unsupervised network than this model at matching V1? If it's not better, then how big is the gap, and why would it exist? (If a supposedly much more biologically-correct model isn't substantially better than the unbiological one at matching biology data, has it really contributed a major advance?)

One thing that will naturally come up in making a comparison like this is that the authors have chosen a particular imageset (moving animals) for training. Perhaps it will arise that their model is not trained in a sufficiently general way to compare favorably with a model trained on a large dataset like ImageNet. (Of course, this is still a fair comparison since neither their model nor the deepnet model would have been trained on the set used for testing, e.g. oriented gratings, or some other set of natural or naturalistic stimuli.) To claim that a major advance in modeling V1 has been made, something along these lines needs to be included. Perhaps the authors could use large video datasets like Kinetics [7] or Moments in Time [8] or the Chicago Motion Database (https://cmd.rcc.uchicago.edu) as a replacement for their animals dataset.

2) The comparisons to neural data are weak and qualitative. Improving that w.r.t. V1 *or* MT would be a major and sufficient revision for publication. The network learns mostly center surround, simple and complex cell behavior, which is conventionally assigned to retina/LGN/V1, but other features of V1 and higher-order visual neurons are not observed. No end- or side-inhibition has been observed, and no object-sensitive units. Only a very small fraction of units sensitive to drifting plaids were found in the 4th stack/layer. Given that, billing the model as a candidate for explaining the whole visual system seems much overstated. The authors could capitalize more on the dynamics of the receptive fields in V1 or MT, which was an interesting result not so often obtained by other models, but that has been investigated much less and was not compared to experimental data (apart from motion sensitivity). In whichever way possible, more detailed comparisons to V1 or MT data are needed. Our suggestions are:

a-i) For V1, the comparisons in Figure 6 are fine, and represent a good first step at comparing models to the data in a gross way. However, it would be great if a slightly more quantitative approach was taken -- e.g. measuring model-similarity in some quantified way, especially to compare between the author's preferred model and the controls suggested in 1) above.

a-ii) Also for V1: A much stronger comparison would be to do something as in Cadena et al. [6]. Specifically, Cadena et al. build a neuron-by-neuron regression model from their model to real V1 neurons, on a large set of real-world and naturalistic images. That work shows that, on this type of high-resolution comparison, there is something substantially better as a model of V1 than the standard hand-coded gabor BWT -- namely, the early intermediate layer of a categorization-trained deepnet. The state of the field has now moved to a point where models are being separated not by coarse measures like what is shown in Figure 6, but rather these much more detailed, real-world-stimulus-based metrics. We think the authors need to address comparisons at this level of resolution, or else it's really hard to know whether their model has made any substantive advance. It's not clear whether the data from Cadena et al. is readily available (though we suspect that Andreas Tolias, the data generator for that paper, would provide it for this purpose if asked). However, there is (or at least used to be) publicly available data from the Neural Prediction Challenge -- definitely worth getting this or similar data from Jack Gallant at Berkeley. (Or any other source that would allow for a much more direct model-to-neuron prediction assessment across naturalistic stimuli.)

b) For MT: the comparison here is quite thin. What the authors have done seems to barely support the claim that their hierarchical model "can capture how tuning properties change across multiple levels of the visual system". More needs to be done here. Several papers have shown such things, mostly (as the authors note) based on supervised models. E.g [9-11] show comparisons of various intermediate layers of a NN to V1, V4, PIT, AIT areas in the ventral visual pathway. An unsupervised model that did the equivalent of this would be a significant advance. To make a claim like what the authors are saying in this draft, there needs to be some equally strong data comparison, but with MT data. Shinji Nishimoto and Jack Gallant have collected data that would be useful for this comparison, but it's not clear whether it would be easy to get access to that or similar MT data.

Comparing to coding in the ventral stream might be an alternative if MT data are not available. V4 and IT data is easily available from Jim DiCarlo (e.g. the data for [9-10]). The authors could definitely check out how well their higher model layers regressed those data and see if they could sustain a claim about matching "multiple levels of the visual system". (But perhaps it would be an unfair comparison? Do the authors think their model would have any power for describing the ventral pathway?)

If these more detailed comparisons cannot be made, the claims about matching "multiple levels of the visual system" must be removed or significantly modified.

[1] Weghenkel, Björn, and Laurenz Wiskott. "Slowness as a proxy for temporal predictability: An empirical comparison." Neural computation 30, no. 5 (2018): 1151-1179.

[2] Willmore, Ben, Ryan J. Prenger, Michael C-K. Wu, and Jack L. Gallant. "The berkeley wavelet transform: a biologically inspired orthogonal wavelet transform." Neural computation 20, no. 6 (2008): 1537-1564.

[3] Lotter, William, Gabriel Kreiman, and David Cox. "Deep predictive coding networks for video prediction and unsupervised learning." arXiv preprint arXiv:1605.08104 (2016).

[4] Wang, Yunbo, Mingsheng Long, Jianmin Wang, Zhifeng Gao, and S. Yu Philip. "Predrnn: Recurrent neural networks for predictive learning using spatiotemporal lstms." In Advances in Neural Information Processing Systems, pp. 879-888. 2017.

[5] Wang, Yunbo, Zhifeng Gao, Mingsheng Long, Jianmin Wang, and Philip S. Yu. "Predrnn++: Towards a resolution of the deep-in-time dilemma in spatiotemporal predictive learning." arXiv preprint arXiv:1804.06300 (2018).

[6] Cadena, Santiago A., George H. Denfield, Edgar Y. Walker, Leon A. Gatys, Andreas S. Tolias, Matthias Bethge, and Alexander S. Ecker. "Deep convolutional models improve predictions of macaque V1 responses to natural images." PLoS computational biology 15, no. 4 (2019): e1006897.

[7] https://deepmind.com/research/open-source/kinetics

[8] http://moments.csail.mit.edu/

[9] Yamins, Daniel LK, Ha Hong, Charles F. Cadieu, Ethan A. Solomon, Darren Seibert, and James J. DiCarlo. "Performance-optimized hierarchical models predict neural responses in higher visual cortex." Proceedings of the National Academy of Sciences 111, no. 23 (2014): 8619-8624.

[10] Nayebi, Aran, Daniel Bear, Jonas Kubilius, Kohitij Kar, Surya Ganguli, David Sussillo, James J. DiCarlo, and Daniel L. Yamins. "Task-Driven convolutional recurrent models of the visual system." In Advances in Neural Information Processing Systems, pp. 5290-5301. 2018.

[11] Khaligh-Razavi, Seyed-Mahdi, and Nikolaus Kriegeskorte. "Deep supervised, but not unsupervised, models may explain IT cortical representation." PLoS computational biology 10, no. 11 (2014): e1003915.
