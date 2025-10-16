# Peer review - Round 1

Editors:
- Markus Meister, California Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58516.sa1](https://doi.org/10.7554/eLife.58516.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This article reveals "what the monkey's eye tells the monkey's brain". The authors show how one can reconstruct the visual image on the retina based on the spike signals from optic nerve fibers. Taking advantage of recordings from nearly complete populations of retinal neurons, they explore how the different types of retinal ganglion cell interact in shaping the visual message sent to the brain. The resulting rules are pleasingly simple, which may well be a design principle for the retinal code.

Decision letter after peer review:

Thank you for submitting your article "Reconstruction of natural images from responses of primate retinal ganglion cells" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Joshua Gold as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Hiroki Asari (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional data or analysis, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Summary:

This paper regards visual signaling by the macaque retina, specifically as viewed from the perspective of visual centers in the brain. The question is how one should interpret spike trains from retinal ganglion cells in order to reconstruct the visual image shown to the animal. Based on the established method of linear reconstruction, the authors explore how the reconstruction quality and the cells' reconstruction filters depend on the types and numbers of cells used for the reconstruction. They further study how noise correlations, nonlinear response transformations, and interactions between cells may contribute to the reconstruction. The presentation is very clear and pleasantly easy to follow, despite the technical material. The results have implications for an understanding of neural processing in the retina, and perhaps more so for the design of future retinal prostheses. In this regard the study draws particular value from using the macaque retina, which is close in function to our own.

Essential revisions:

At the same time this work comes on the background of a well-developed "standard model" of the retina that spells out how retinal ganglion cells encode the visual scene with spikes. Much of what is described here is fully expected based on that standard model. Some of the specific analyses have been done before in other species. Most of the comparison between optimal filters and single-cell receptive fields can be understood based on purely linear processing. A few other items require Linear-Nonlinear processing, which is also part of the standard model. Much of the report reads like elegant and rigorous confirmation of the conventional picture. The authors should take a clear position on the relation of their findings to the background knowledge. The reviewers can envision two possible outcomes:

A) We tried everything, but actually the optimal decoding filters are just as expected from a simple LN picture of retinal encoding. Even the noise correlations that we reported on before don't make any difference. This is good news for creating retinal prostheses because one doesn't have to engage in any sophisticated encoding.

B) We tried everything and found some interesting deviations from the conventional model of retinal function. Here they are specifically, along with the magnitude of their contributions. We expect that these deviations will have to be emulated by retinal prostheses.

In our reading, outcome (A) seems more likely, but either way the authors should choose a position.

Some specific impressions, organized by the claims in the Abstract:

1) "Each cell's visual message, defined by the optimal reconstruction filter, reflected natural image statistics, and resembled the receptive field only when nearby, same-type cells were included" This is as observed previously when reconstructing natural signals that include strong correlations. Much of the effect can be explained based on linear processing.

2) "Each cell type revealed different and largely independent visual representations, consistent with their distinct properties." This is similar to previous observations on RGCs. Independence of On and Off representations is largely explained by the opposite rectification in On and Off cells. But note midgets and parasols are not "largely independent" by this criterion. In fact the midget filter is more affected by including parasols than by including other midgets (Figure 5B). That is a deviation from the conventional idea of independent channels. On the other hand, one would predict these effects on the filters from the previously reported spike correlations among these types (Greschner, 2011).

3) "Stimulus-independent correlations primarily affected reconstructions from noisy responses." These noisy responses were created artificially by ignoring most of the spikes. That is not a relevant condition for actual vision. It would have been more interesting to experiment at low light levels, where prior work has shown the importance of noise. The present results seem to say that at high light levels the retinal noise is not limiting for reconstruction.

4) "Nonlinear response transformation slightly improved reconstructions with either ON or OFF parasol cells, but not both." Again the small effects seen here for On or Off cells alone are expected from the LN model. But because one has to include both On and Off cells anyway just to get the basic reconstruction correct, one can conclude that overall the nonlinear transformations don't matter for reconstruction.

5) "Inclusion of ON-OFF interactions enhanced reconstruction by emphasizing oriented edges, consistent with linear-nonlinear encoding models." These are the tiniest effects in the whole report: Δρ=0.009±0.023. The mean effect is just half of what was called "slightly improved" in point (4). It is also half of the standard deviation. Often the effect is negative, i.e. the reconstruction is worse even though the model has many more parameters; this hints at overfitting. Figure 9G is not impressive.

6) "Spatiotemporal reconstructions revealed similar spatial visual messages." A useful but "limited test" of generalization to real vision. One claim is that the spatio-temporal filters had "high space-time separability". But this leaves on the table 22% of explainable variance in the filter, which is >20 times the effect size in point (5) that got covered at great length. If, in fact, it turned out that space-time separable filters are just fine for reconstruction of videos, that would be an interesting departure from conventional wisdom, where different time course of RF center and surround have figured prominently since the 1960s.

Detailed suggestions:

7) To test which properties of retinal encoding contribute to the reconstruction filters, the authors could replace the experimental data with simulated spike trains. They have done this before to great effect using spiking LN or GLM neurons. Is reconstruction performance the same? If not, what are the important differences? Are certain aspects of visual scenes reconstructed better or worse by real cells than model cells?

8) Parasol cells are very spatially nonlinear in their responses to natural scenes (Turner and Rieke, 2016), and both ON and OFF parasols are highly motion sensitive (Manookin et al., 2018). So their use for a linear reconstruction of a static scene requires justification. Is it possible that their true role will become more apparent when reconstructing movement within the visual scene (Frechette et al., 2005)?

9) Related to 8: the conclusion that different RGC types "conveyed different and largely independent features of the visual scene" might be inappropriate when comparing midget and parasol cells. Apart from a slight difference at higher spatial frequencies, the reconstructed features of the two cell types actually seem quite similar (Figure 7).

10) More regarding the interaction between parasol and midget signals: Did adding parasol responses to midget responses aid in reconstruction simply because parasols filled in gaps in the midget mosaics? To test this, perhaps one could artificially fill in the midget mosaics with LN model cells.

11) Quality of midget vs. parasol reconstructions: RGC density is a dominant factor in image reconstruction (Results), and images reconstructed from midgets cover a wider spatial-frequency range than parasols (Figure 7D; Results). However, the reconstruction from denser midget cells is worse than that from sparser parasol cells (Figure 7C; Results). Why?

12) For the analysis that included a nonlinear, logarithmic transformation of responses, was the transformation taken into account when re-computing the weight matrix W. Also, what happened with the logarithm for bins with R=0?

13) Statistical tests: For key claims, authors should perform statistical tests to clarify the significance and better interpret the d(rho): e.g., smoothed vs. non-smoothed images, spike-counts vs. latency coding, etc.

14) Figure 13: Unclear how the reconstruction boundary relates to the RF mosaics. 'Parasol+midget' looks most like the RFs for OFF midget alone.

15) All figures: Scale bars, e.g. in degrees of visual angle, would be useful at least in key places. Also were the stimuli sized for a particular viewing distance?

16) Figure 4C: How many data points?

17) Figure 7D: What are the 3 different curves for each set? Also maybe show the 'parasol+midget' result in black?
