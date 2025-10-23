# Peer review - Round 1

Editors:
- Robert H Singer, Albert Einstein College of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.52224.sa1](https://doi.org/10.7554/eLife.52224.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The authors develop a useful Deep Learning Neural Network to classify heterogeneous single-particle motion from live-cell imaging data. They apply their model to infer fractional Brownian motion from both simulated and cellular data, and show that it out-performs competing approaches such as MSD-based averaging and exponent inference, accurately predicting Hurst exponents in as few as 7 steps.

Decision letter after peer review:

Thank you for submitting your article "Deciphering anomalous heterogeneous intracellular transport with neural networks" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Hyeyoon Park (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The authors develop a useful Deep Learning Neural Network to classify heterogeneous single-particle motion from live-cell imaging data. They apply their model to infer fractional Brownian motion from both simulated and cellular data, and show that it out-performs competing approaches such as MSD-based averaging and exponent inference, accurately predicting Hurst exponents in as few as 7 steps. Their article is well written and presented.

Summary:

All the reviewers see the merit in the approach, although there is some concern that it is not particularly novel and the approach may be biased.

Essential revisions:

The authors should either explain or illustrate how training their model solely on the class of models they seek to infer, rather than a broader set of models, may bias their inference procedure. For example, could they perform a test of this potential bias directly by training the neural network by including other models that are not fBm, and show how this impacts their results, particularly in the case of cellular datasets?

Limited comparison would be helpful for the cellular datasets in particular in order to illustrate to the reader how/why application of the fBm to infer single-particle trajectory data from living systems is useful for inferring molecular/other mechanism of dynamical molecular motion in living systems.

It would be helpful if the authors could elaborate a bit further on how their fBm and Hurst exponents are useful to infer motion mechanism.

The authors need to offer a bit more biological/cellular insight into their preceding findings on vesicular motion?

Reviewer #1:

The authors provide an algorithmic approach for evaluating cellular transport distinct from MSD based approaches. The useful feature is that presumably fewer points are needed for predictive value. This is important since photobleaching is a major limitation in particle tracking, the more information that can be extracted from limited data, the better.

I feel this approach may be useful, but it is not clear how this compares to the current standard HMM analysis in a head to head matchup. Also, it seems a bit cumbersome so anything they can do to make it user friendly would be appreciated.

Reviewer #2:

The authors develop a useful Deep Learning Neural Network to classify heterogeneous single-particle motion from live-cell imaging data. They apply their model to infer fractional Brownian motion from both simulated and cellular data, and show that it out-performs competing approaches such as MSD-based averaging and exponent inference, accurately predicting Hurst exponents in as few as 7 steps. Their article is well written and presented.

Training the neural networks on a fractional Brownian motion (fBm) model alone must effectively "bias" the inference procedure towards this model, acting analogous to a prior in Bayesian inference. Can the authors either explain or illustrate how training their model solely on the class of models they seek to infer, rather than a broader set of models, may bias their inference procedure? For example, could they perform a test of this potential bias directly by training the neural network by including other models that are not fBm, and show how this impacts their results, particularly in the case of cellular datasets?

In this vein, the authors cite HMM-based models that infer diffusion and directed motion from single-particle trajectories, but they do not compare their procedure with these methods. Some limited comparison would be helpful for the cellular datasets in particular in order to illustrate to the reader how/why application of the fBm to infer single-particle trajectory data from living systems is useful for inferring molecular/other mechanism of dynamical molecular motion in living systems.

Related to this, it would also be helpful if the authors could elaborate a bit further on how their fBm and Hurst exponents are useful to infer motion mechanism, immediately before Conclusions, where the authors write:

"This implies that the vesicles may have a biological mechanism to prioritise certain interactions within the complex cytoplasm, similar to how human dynamics are often heavy tailed and bursty Barabasi, (2005)."

Given the rather large difference between human dynamics and molecular, organelle, or vesicular dynamics, could the authors offer a bit more biological/cellular insight into their preceding findings on vesicular motion?

For a wide application of this analysis tool in biology, can the authors provide a directly executable GUI software?

Reviewer #3:

This paper describes an analysis tool for particle trajectory data. The authors used a deep learning feedforward neural network (DLFNN) to extract a stochastic Hurst exponent H(t) from a trajectory. They found that the neural network is a more sensitive method to characterize fractional Brownian motion (fBM) than previous statistical tools such as mean squared displacement (MSD), rescaled range, and sequential range methods. They applied this tool to analyze the trajectories of lysosome and endosomes in live cells. The topic is interesting, but the novelty and impact of the work are not very clear. Also, the software is based on Python, which may limit the application of the tool by a wide range of researchers in cell biology. A user-friendly, standalone software would be more helpful.

1) As the authors mentioned in the Introduction, exponent estimation using neural networks has been already demonstrated. The authors claimed a novelty in that the local H(t) is used to segment single trajectories into persistent and anti-persistent sections. However, the manuscript is lacking comparison with the existing methods using hidden Markov models and rolling windowed analysis. The authors also claimed that "fBM with a stochastic Hurst exponent is a new intracellular transport model". However, this section is rather brief, and some notations are not clearly defined. I think stronger impact and novelty are required for publication in eLife.

2) For a wide application of this analysis tool in biology, can the authors provide a directly executable GUI software?

3) It is unclear whether users can apply the pre-trained model for a broad range of data with different time and spatial scales. Or do users have to train the neural network for their own data set? More detailed instruction for the training is required. In the subsection “DLFNN structure and training”, the last sentence needs more explanation.

4) In Figure 1E, it is counterintuitive that the error (σH) increases as the SNR increases. In subsection “The DLFNN is more accurate than established methods”, 'Gaussian noise with increasing signal-to-noise ratio" needs to be revised. Please use a different term for this parameter or revise the figure with a commonly used definition of SNR.

5) It would be informative if the authors also show the Hurst exponent estimated from the TAMSD method in Figure 2.

6) Heavy-tailed distributions have been observed not only in human dynamics but also in many biological systems. Some of the relevant review and original articles are listed below.

-Reynolds and Rhodes, (2009)

-Ariel, et al., (2015)

-Song et al., (2018)

-Chen et al., (2015)
