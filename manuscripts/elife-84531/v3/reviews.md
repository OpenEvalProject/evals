# Peer review - Round 1

Editors:
- Peter Latham, https://ror.org/02jx3x895 University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84531.sa0](https://doi.org/10.7554/eLife.84531.sa0)

This fundamental study provides important insight into coding strategies in sensory areas. The study was well done, and the analysis and simulations were highly convincing. This study should be of particular interest to anybody who cares about efficient coding.


---

# Peer review - Round 1

Editors:
- Peter Latham, https://ror.org/02jx3x895 University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84531.sa1](https://doi.org/10.7554/eLife.84531.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Are single-peaked tuning curves tuned for speed rather than accuracy?" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Panayiota Poirazi as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Stefano Panzeri (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

While this paper makes an extremely important point, one that should definitely be communicated to the broader community, in our opinion it suffers from two (relatively easily fixable) problems:

I. Unless one is an expert, it's very hard to extract why multi-peaked tuning curves lead to catastrophic errors.

II. It's difficult to figure out under what circumstances multi-peaked tuning curves are bad. This is important, because there are a lot of neurons in sensory cortex, and one would like to know whether periodic tuning curves are really a bad idea there.

And here are the fixes:

I. Figure 1c seems like a missed opportunity to explain what's really going on, which is that on any particular trial the positions of the peaks of the log likelihood can shift in both phase and amplitude (with phase being more important). The reason it's a missed opportunity is that Figure 1c shows the average log likelihood, which makes it hard to understands why there are catastrophic errors. It would really help if Figure 1c were expanded into its own large figure, with sample log likelihoods showing catastrophic errors for multi-peaked tuning curves but not for single-peaked ones. You could also indicate why, when multi-peaked tuning curves do give the right answer, the error tends to be small.

II. What the reader really wants to know is: would sensory processing in real brains be more efficient if multi-peaked tuning curves were used? That's certainly hard to answer in all generality, but you could make a comparison between a code with single-peaked tuning curves and a _good_ code with multi-peaked tuning curves. Our guess is that a good code would have λ_1=1 and c around 0.5 (but not, of course, exactly 1/2; you could use the module ratio the grid cell people came up with -- we think 1/sqrt(2) -- although we doubt if it matters much). What would be great would be a relatively simple relation, possibly fitted empirically to simulations, that told us when multi-peaked tuning curves are better than single-peaked one, given the number of neurons, background and peak firing rates, and dimensionality. Of course, this may be impossible, but if so it's important to state that up front, so that people know how difficult this is.

In addition, we have a number of comments, all designed to improve the paper. Feel free to disagree with any of them; we don't feel massively strongly about them. Also, if you implement them, no reason to provide a reply -- we're sensitive to the fact that replies to the reviewer are becoming longer than the paper!

Reviewer #1 (Recommendations for the authors):

1. When catastrophic errors are possible, we agree that it's very hard to find a good measure of error. RMS error clearly isn't very good. However, it's not clear minimal decoding time is any better, since it'd defined in terms of RMS error. Finding a good measure seems critical when comparing codes, given that Fisher info can change by 5 orders of magnitude while decoding time changes by only 1 (e.g., Figure 4d). Moreover, we could be wrong, but our intuition is that when λ_1=1, catastrophic errors aren't much of an issue. Is that correct? If so, time to threshold (defined to be time for the RMS error to be twice that predicted by the inverse of the Fisher info) could be a bad measure.

Here we don't have any really great suggestions. But you might try something like [<(error)^k>/((2k-1)!!)]^{1/k} for k larger than 2 and even (the factor of (2k-1)!!) makes this equal to the RMS error for Gaussian distributions. But other measures are possible.

2. Are you using periodic boundary conditions? Tuning curves are clearly periodic, but decoding near the boundaries is a bit tricky. For instance, the ML estimator can put the decoded value outside the range [0, 1). This should be clarified.

3. It should be clear that the expression for Fisher info (Equation 3) applies when a_i=a and b=0.

4. Figure 1a: it would be helpful to indicate the location of s_1 and s_2 in the top panel.

Also, isn't Figure 1a a bit misleading? The problem isn't a small number of spikes; it's a phase shift in the log likelihood.

5. l 99-100: "For the largest mode of the joint likelihood function to also be centered close to the true stimulus condition, the distance δ between s^(1)_ML and s^(2)_ML must be smaller than between any other pair of modes of Q_1 and Q_2." We can see why this might be reasonable, but it's not totally obvious that the distance between the modes is the only thing that matters. This needs to be shown.

6. l 100-101: "Thus, to avoid catastrophic errors, δ must be smaller than some largest allowed distance δ* (see Methods for calculation of δ*)." This makes it seems like δ* is something complicated. But in fact it's exactly half the smallest distance between any other pair of modes. Why not say so?

7. l 120-1: "estimates can cause catastrophic shifts in the joint likelihood function. For single-peaked tuning curves (λ_1 = 1), however, only small scale factors c can pose such problems." Should "For single-peaked tuning curves" be "When the first mode has a single peak". If not, we're lost.

8. l 128: "Furthermore, only populations with unambiguous codes over the stimulus interval were included [22]." Can't parse.

9. Equation 8 seems unlikely to be correct, given that it doesn't depend on c, which we know is critical (as shown in Figure 1e). However, if you do keep it, it would be helpful to express it in terms of the average firing rate. If you do that, lots of terms go away.

10. Figure caption 2c: "colored lines show the estimated minimal decoding time from simulations and the black lines show the fitted theoretical predictions". Presumably the description of the fitted lines was given on on l. 178. However, we can't tell from this description what you actually did. Equations are needed.

And presumably this also comes up on l. 211: "ratios of fitted regressors K1 were approximately 1.69 and 1.72 for D = 1 and D = 2, respectively".

11. l. 179: "Within this range of scale factors". Within what range?

12. l 184-5: "As suggested by Figure 2d, there is also a strong correlation between Fisher information and minimal decoding time again indicating a speed-accuracy trade-off." There's certainly a tradeoff between Fisher info and minimal decoding time, but, as mentioned in point 1, minimal decoding time isn't always a great measure. You should be up front about this.

13. The tables should be moved to the main text -- the parameters (especially the number of modules) are highly relevant. Or what would be even more useful would be to put the parameters in the figure captions.

14. Figure 5: by "Gaussian pop." and "Periodic pop." do you mean "Single peaked" and "multi-peaked"? If so, this should be clear.

15. l 303: "Thus, minimal decoding time should set a bound on the number of features a population can jointly encode reliably." Very interesting prediction! Which you point out on lines 325-7: "Our work gives a compelling reason to understand whether and how biological brains can reliably encode high-dimensional stimuli at behaviorally relevant time scales." But this should be quantified; see point 1.

Reviewer #2 (Recommendations for the Authors):

The paper makes a simple but important point. It is also remarkably well explained especially considering the complexity of the calculations. For once, I do not feel the need to make many suggestions for improvement.

One point that could be better addressed regards the justification of speed of encoding based on data on sensory cortex. The introduction seems heavy on the visual system based on the results of Thorpe and colleagues. In the discussion (lines 288-289) the authors point out (though the sentence is not very strongly linked to the overall text flow) that the first few spikes carry significant information in the visual and olfactory system. While the point of raising the importance f speed of encoding in sensory areas is valid, I am not sure that it should privilege the visual system or the visual and olfactory system. I think that somatosensory modalities encode information faster and earlier than visual modalities, including with regard to the prominence of first spikes (see e.g. Panzeri et al. Neuron 2001). If anything, visual cortical data show encoding in longer time scales. It would be nice to have a more precise introduction to and discussion of these topics to motivate this work and to evaluate its implications.
