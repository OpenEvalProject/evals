# Peer review - Round 1

Editors:
- Tobias Reichenbach, Imperial College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54172.sa1](https://doi.org/10.7554/eLife.54172.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Our perception is notoriously inaccurate, and estimating the uncertainty of a percept is an important task of our brain. The present paper shows for the first time that our brain uses past history in the estimation of the uncertainty of a current percept. It opens up further research questions including those related to the role of learning in perception.

Decision letter after peer review:

Thank you for submitting your article "Using the past to estimate sensory uncertainty" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Tobias Reichenbach as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Andrew King as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Luigi Acerbi (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Beierholm et al. present a well-executed psychophysical study in which participants judged the location of a conflicting visual-auditory stimulus under varying degrees of visual noise. Unlike other studies in this field, the visual noise was varied slowly, enabling participants to take advantage of this fact by incorporating estimates of uncertainty from the recent past into their current cue-weighting strategy. The authors then compare the data to three computational models: a simple learner that does not use past information, a Bayesian learner, and an exponential learner that accounts for past information at a fixed learning rate. The conclusion of the paper is that subjects' estimate of visual variability is influenced by the past history of visual noise.

While we find these results intriguing, and the experiment and analysis thorough, we have several major comments that we would like the authors to address.

Essential revisions:

1) The current analysis does not consider the effect that past visual locations, in addition to the uncertainty in the visual signal, may have on the estimate of the current location. In particular, if the location at t-1 is the same or close to the location at time t, it might be that past estimates of location get integrated (in fact, this becomes another causal inference problem). This effect might be further related to the question investigated here, because, if present, it might be modulated by the visual noise in the previous trial. Have you investigated whether this effect is present, and if so, how did you account for it in your analysis?

2) The authors currently refer to a preprint of this manuscript on bioarxiv for a full derivation of both model components for the Bayesian learner. Instead, please provide the full model derivation in the supplementary information in a self-contained form. Please also make the code for the modelling and the analysis as well as the data publicly available.

3) In the sinusoidal condition the bins had a duration of only 1.5 s, but the trials were 1.4 to 2.8 s apart. It therefore appears as if there were either 1 or 0 (or very rarely 2) responses in each bin. How did you handle the zero-response bins? And how can weights – presumed to vary smoothly between 0 and 1 – be reliably estimated from a single behavioural response?

4) The computational model makes certain assumptions that appear to differ from the experiment. We would like the authors to comment on these discrepancies. First, the computational model assumes that the auditory signal follows a normal distribution around a particular mean – . However, in the experiment, the location of the sound was either +5 degrees or -5 degrees away from the mean of the visual signal. Second, regarding the computational model, the authors write that "the dispersion of the individual dots is assumed to be identical to the uncertainty about the visual mean, allowing subjects to use the dispersions as an estimate of the uncertainty about the visual mean". But in the experiment there is no notion of an uncertainty (noise) in the visual mean. Third, the authors write that all probabilities, except for one, are Gaussian. As for the first point raised above, in the experiment, this only seems true for the distribution of the dots around the mean, but not for the other distributions. In particular, the mean of the visual signal is sampled from a discrete uniform distribution that encompasses only five different locations. Fourth, each dot location Vi,t is drawn from a normal distribution with mean Ut, but Ut is drawn from another distribution with mean SV,t – are the variance of these two distributions the same? Wouldn't Ut simply be the location (-10, -5, etc) on that trial, and wouldn't this mean instead that the dot positions are doubly stochastic? If so, why? The actual dispersion (not to mention the observers' estimates thereof) would be very noisy if dot locations were simply resampled at 5 Hz from a fixed distribution for a given trial. Doesn't resampling the SD at 5 Hz just complicate the modeling even more than it already is? Please also explain the purpose of the log random walk.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your article "Using the past to estimate sensory uncertainty" for consideration by eLife. Your revised article has been reviewed by three peer reviewers, including Tobias Reichenbach as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Andrew King as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Luigi Acerbi (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

The authors have addressed our previous comments well in their extensively revised version of the manuscript. We only have a few remaining queries.

Revisions:

Difference in STD between current and previous bin predicts auditory weight, would that be expected given the autocorrelation of the STD sequence? Our intuition is that the null hypothesis (no impact of previous bin) would only be valid if STDs were (temporally) conditionally independent. In other words, if it were only the current STD that affected the weight, you might still see an apparent influence of the previous STD simply because STD of bin N is highly correlated with STD of bin N-1 (for the sinusoids at least).

This logic may only apply if the regression was on the absolute STDs, not the difference between current and previous STD, which is what the authors did. So perhaps it's not an issue. But if it is, we think one could perform a nested model comparison to test whether adding the previous time bin significantly improves the fit enough to justify the extra parameter. (It could also be that the current analysis is effectively doing this.)

Alternatively, one could perform this analysis separately for the first half vs. second half and see whether you observe a change in the regression coefficient for the δ-STD. If the authors' interpretation is correct, the coefficient should systematically change (sign flip?) when STD is increasing vs decreasing, whereas if the autocorrelation were driving its significance, it should not depend on increasing vs decreasing.
