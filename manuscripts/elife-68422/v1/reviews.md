# Peer review - Round 1

Editors:
- Stephanie E Palmer, The University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68422.sa0](https://doi.org/10.7554/eLife.68422.sa0)

This is a thorough study showing that long-range correlations in the brain can arise without common input drive or long-range anatomical connections. These long-range correlations are modulated by the animal's behavioral state, a surprising finding that suggests a computational role for control of this kind of correlation. The paper details some analytical methods for modeling this behavior in disordered systems. The work will be of broad interest to neuroscientists, computational biologists, and biophysicists.


---

# Peer review - Round 1

Editors:
- Stephanie E Palmer, The University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68422.sa1](https://doi.org/10.7554/eLife.68422.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Global organization of neuronal activity only requires unstructured local connectivity" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Timothy Behrens as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The scenario put forward by the authors describe the data well, but a major drawback is that it needs fine tuning for the network to be close to the critical point. There are multiple other, and perhaps simpler, scenarios that could reproduce the data described by the authors, but they are not adequately discussed in this paper:

A: Fluctuating and broadly divergent external inputs could in principle generate the observed correlation structure. The authors quickly dismiss this scenario in the discussion: 'In such a scenario, covariances have been shown to be predominantly generated locally rather than from external inputs (4,15)'. It was not clear where this is shown in these papers. The authors should explain much more clearly why they believe the external input scenario is unlikely (see also issue #5).

B: Recurrent connectivity correlated with neuronal selectivity, as in visual cortex, but with salt-and-pepper organization. This would be a scenario similar to what has been proposed in multiple visual cortex models (see old work by Tsodyks, Sompolinsky, and more recently ref (14)). The authors also dismiss this scenario because of the lack of patchiness of the correlation structure in M1, but we would not expect any patchiness if selectivity is salt-and-pepper.

C: Long range connectivity within M1. The existence of horizontal long range connectivity has been demonstrated in multiple cortical areas, and in particular motor cortex (see DeFelipe et al., 1984). Such a long range connectivity could in principle give rise to the long-range correlations found by the authors.

D: Can this work be connected to the findings in Schwab et al., PRL 2014? If latent variables can give rise to signatures of criticality but do not require fine tuning of the brain's network state, might this not be a more biologically plausible origin for the long-range correlation observed here?

2) The main text is sorely lacking any details of the model analyzed and simulated by the authors. The reader has to go to p.47 of the Supplementary Material to finally understand the authors simulated a rate model with threshold-linear (ReLU) transfer functions. The model should be explained in the main text when it is first introduced, and the equations should be described in the Methods of the paper, and not confined in the Supplementary Material.

3) A related issue is that it remains unclear how general these theoretical results are. There are several places in the paper where the authors hint that their results are more general than the analyzed rate model, but it remains unclear whether this is the case, and in particular whether their results could also apply to networks of spiking neurons. This issue needs to be discussed more clearly.

4) Stationarity claims are not well substantiated. Figures 2 and 3 in the Appendix show that the population averaged activity is approximately stationary for different sessions. However, single neuron activity could be highly dynamic, but these fluctuations of activity could be washed out at the population level. It would be helpful to check whether trial-averaged single unit activity is indeed stationary during these epochs. If it is, then it should be shown in the Appendix. If the authors are not able to demonstrate stationarity at the single neuron level, then some of their conclusions should be toned down (in particular, the last paragraph of the Discussion). Note that this issue is strongly related to issue #1, scenario A.

5) There are claims of 'strong' spike count covariances at several points in the paper, but the covariances by themselves tell us nothing about the strength of correlations if we don't know the respective variances. In that respect, plotting correlations instead of covariances (as is done in many other studies of correlation structures in brain networks) would be much more informative about the strength of correlations between neurons. An example of why using covariances is problematic to assess strength of correlation is given by a comparison between Figures5 and 6: In Figure 5 covariances are of order 0.01, but they are of order 1 in Figure 6, likely because of a difference in mean rates of a factor 10 between the two.

6) The most interesting and compelling section of the paper is arguably the dependence of correlation on behavioral state. This result, though, seems a bit weak in magnitude. Are there other data to shore this up, or a null model to reveal how surprising this change is? A direct quantification of the covariance pattern change between epochs in Figure 6B, for example, would be good to see.
