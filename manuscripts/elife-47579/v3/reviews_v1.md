# Peer review - Round 1

Editors:
- Stephanie Palmer, University of Chicago United States

Reviewers:
- Fred Rieke, University of Washington United States

## Review text

DOI: [10.7554/eLife.47579.sa1](https://doi.org/10.7554/eLife.47579.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Measured perceptual nonlinearities show how ON-OFF asymmetric processing improves motion estimation in natural scenes" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Ronald Calabrese as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Fred Rieke (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper takes a close look into the natural scene statistics that influence behavior. In particular, the work investigates the importance of second- and third-order stimulus correlations on motion sensing in flies. Second-order correlations have been emphasized in past work, and a few past studies have suggested that third-order correlations also contribute, but this work provides the first comprehensive treatment of the issue. The paper presents an analysis of fly behavioral responses to moving patterns based on rigid rotations of static natural scenes, either with fully natural statistics, or modified parametric stimuli that retain the skewness in the contrast distribution of natural scenes. Analysis of behavioral responses to these stimulus variants indicates that the fly uses third -order computations effectively to counter some of the systematic (and well-known) variations introduced by the second-order computations prescribed by canonical motion detection models. Both the experiments and the analysis are presented clearly, and the authors make a convincing case for their conclusion that the third-order term improves velocity estimation in natural scenes. The computational strategies discovered here likely extend to other visual systems. The stimulus construction algorithm developed here could also be used for other model systems and analyses.

Essential revisions:

1) As pointed out in the Discussion section, the Volterra kernel approximation represents a general and systematic approach to the identification of nonlinear systems (with practical caveats, as also mentioned). But there is also a more fundamental issue: Volterra kernels are essentially high dimensional polynomial approximations, and as such, although they are general, they are extremely inefficient in describing compressive nonlinearities (and biological systems are essentially always compressive in their typical range of operation). Motion estimation by correlation is a second-order Volterra operation, and therefore diverges quadratically. To counter that divergence, the system must somehow normalize the response to the contrast variance, such as in contrast normalization. And this is what seems to happen in biological motion detectors: It is well known that motion responses saturate as a function of contrast.

In this light, the finding that the third-order Volterra kernel improves velocity estimates can then be simply seen as a corollary of the fact that the third-order kernel is essentially a "fitting parameter" which is necessarily better than a fit to second-order. Alternatively, as noted in the paper, the third-order behavior could be due to more or less fixed asymmetries in processing, or even due to nonlinear behavior in early vision. Something along these lines was proposed by Bulthoff and Goetz (Bulthoff and Goetz, 1979) to explain a motion illusion in human and fly vision (and that should be cited in this paper).

These points should be addressed fully in the text of the paper, both in the Results and in the Discussion.

2) Response predictions and quantification. The kernel approach estimates behavioral responses, but the predictions are then compared directly to image velocity. Implicit in this (at least not clearly stated in the text of the manuscript) is that the behavior is linearly related to the image velocity – or at least that the two can be swapped in the analysis. It would be good to clarify this issue somewhere around the second paragraph of the subsection “Third-order kernel improve velocity estimation in moving natural scenes” where this analysis is described. At present, the text could be misread to indicate that image velocity is being estimated directly.

3) In the Discussion section:

- The interpretation of the main result (that the third-order term improves velocity estimation in natural scenes) feels a bit narrow; the authors should remedy that in the Discussion section.

- Ties to neural data need to be made a bit more extensive and detailed. Is there evidence to suggest that the kinds of optimal temporal filters derived here are found in the fly brain? Perhaps suggest a few other places to look, beyond what's already discussed (measuring T4/T5 kernels).

- Comment a bit more on the limitations/advantages of considering only rigid rotations applied to static natural or naturalistic scene stats. Perhaps also comment on using walking versus flight, and note that flies spend most of their time walking.

- Comment a bit more on the potential behavioral relevance of the magnitude of the effect of the improvement from third-order filter input to second-order processing.

- How prevalent is positive skewness in different natural scenes? Are there scenes/environments where one should expect more or less skewness? Would visual systems that operate in specialized niches be expected to have different nonlinearities in their motion processing as a result, or will all visual systems require some amount of compensation in their second-order motion detectors?

Title revisions:

Replace "perceptual" with "behavioral"

Suggested stylistic revisions:

The papers dives into contrast-polarity sensitivity right away, before sufficiently motivating the research approach as a whole. It also seems like this feature might require a more intuitive figure to explain the effect to the uninitiated. Perhaps a few more words about the behavioral advantages of this level of careful motion dissection would be useful.

In the last paragraph of the Introduction, it would be good to broaden the perspective a bit on how filters are usually computed in behavioral and neural recording experiments, how this relates to other filter-finding techniques, and what the third-order kernels might reveal. For a broad audience, it might also be good to remind the reader what a Volterra expansion is and add a note about adding kernels to the expansion versus static nonlinearities, along the lines discussed above.

Here and there the paper reads a bit too much like a travel journal – a few examples:

- The paragraphs in the subsection “The structure of natural scenes induces noise in second-order motion estimates” all have something like "We did something…Then we observed something, etc."

- The legend to Figure 3 is full of "we did this or that".

Consider revising the text to make the language just a bit more formal and deliberate in guiding the reader through the major scientific findings in the paper, by motivating and previewing the steps taken in this careful and thorough work.

There are a number of typos that need to be corrected, through a close reading of the text.
