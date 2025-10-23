# Peer review - Round 1

Editors:
- Ronald L Calabrese, Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54183.sa1](https://doi.org/10.7554/eLife.54183.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Spatiotemporally precise optogenetic manipulation in freely moving animals" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Ronald Calabrese as the Senior Editor and Reviewing Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this Advance to their recent eLife publication, DeAngelis and colleagues describe a new method for sparse optogenetic stimulation using a DLP projector. Specifically, they use the DLP system to randomly-scatter light at the wavelength necessary for optogenetic activation, and then, after the experiment, isolate the behavioral effects of stimulating as a function of where on the body the light hit. This method is cheaper and easier than more complicated methods that require real-time tracking and targeting for specific body parts. They first activate mechanosensory bristles in different parts of fly's body: stimulating the abdomen makes the fly speed up; stimulating the head, forelimbs, and thorax makes the fly slow down; activation on one side causes contralateral turning. They then activate sweet taste receptors (gr5a); here, flies tended to slow down when the head and body was stimulated, and slow down and turn toward the side of stimulation when legs were targeted. The paper qualifies nicely as an Advances article, as it produces novel results and methods important in directing future research.

Essential revisions:

While the reviewers were generally supportive there were concerns. First, the work appears presented more as a methods development than a scientific advance, leading to some confusion by the reviewers. Reviewer #1's confusion regarding the manuscript type would be best addressed by making clear that this is not a Tools and Resources paper but a scientific Advance. Second, the authors should more explicitly integrate this work with the previous publication – the continuous attractor dynamics play almost no role here. Some additional measurements (e.g., phase response curves, adaptation estimates, display of full variation rather than 95% c.i. of mean, etc.) would go a long way towards increasing the impact of the article. Reviewer #2's concerns should be fully addressed.

While reporting rigorous 95% CI's of the mean is certainly appropriate for many of the comparisons made some graphical presentation and quantification of the actual variation in the data would be useful for assessment of method applicability. We like the raw data plots of the fly body at the top of each figure, but it is hard to glean a number or distribution from this.

Reviewer #1:

In this Tools and Resources manuscript the authors build on their recent ELife publication to report a method for obtaining spatially and temporally selective optogenetic stimulation without real-time tracking or implanted devices. The key insight is to use patterned light and post-hoc analysis of high-speed video combined with extensively stochastic sampling. My major concerns are the lack of benchmarking and quantitative comparison to other methods and whether the methodology goes significantly beyond what might be appropriate for a Materials and methods section in a standard research article. The limitations of the proposed methods, common to many optogenetic approaches, are clearly articulated. The test cases are themselves a nice addition to the literature, enough so that this paper might be more appropriate as a research study in a more focused journal.

It is certainly a clever insight to use random sampling and post-hoc analysis to determine what category the stimulation fell under. However, this type of approach is certainly not unprecedented in other conditions such as multi-unit electrophysiology (e.g. Martin et al., 2015.). I have not seen it applied before in an optogenetics context, although I have not systematically looked, and it clearly does help in this situation. I think it quite evident that such method was useful in this case. However tools and techniques papers typical pose approaches that significantly improve upon existing data in a way that might resolve many open questions in the field. Combined with the lack of precise patterning of spikes, I am worried that the use cases here might be somewhat narrow.

eLife's guidelines for a new method in a Tools and Resources papers says "…the new method should be properly compared and benchmarked against existing methods used in the field."

This seems like a reasonable request, especially for this paper. Specifically, I would very much like to see a quantification of precision and the degree of selectivity that this technique can provide. It clearly can distinguish between legs and body, but is that the limit? The figures suggest it may be more precise given the localization of the target, but how far outside of this region does the physiological activation extend? What are the typical levels of activation that are achieved when light passes through the exoskeleton? For the specific application here, these questions did not require answers because the authors examined the differential response between body and leg stimulation. However, for general methodology these characterizations seem necessary.

Reviewer #2:

In this update to their recent eLife publication, DeAngelis and colleagues describe a new method for sparse optogenetic stimulation using a DLP projector. They first activate mechanosensory bristles in different parts of fly's body: stimulating the abdomen makes the fly speed up; stimulating the head, forelimbs, and thorax makes the fly slow down; activation on one side causes contralateral turning. They then activate sweet taste receptors (gr5a); here, flies tended to slow down when the head and body was stimulated, and slow down and turn toward the side of stimulation when legs were targeted.

Overall, I think this short paper provides a reasonable update to the previous publication.

This update could be better integrated with the original publication. For example, the authors' previous submission contained a figure showing that activation of forelimb bristle neurons resulted in turns that appear distinct from spontaneous turning behavior. Including that data here would help to link these new results to those in the original paper.

It would be useful to construct a phase response curve of optogenetic stimulation to understand whether and how flies respond to perturbations at different phases of the step cycle. It would also be helpful to know when the leg is stimulated within the step cycle. It is likely that the random stimulation induces a bias in the phase that the leg gets stimulated at. In particular, I would expect that the legs get stimulated more when they are extended than when contracted.

For clarity, the authors need to provide more information about the distribution of bristle and gr5a neurons across the flies body. Without this information, it is difficult to interpret the behavioral results. Given that this is already described in the literature, it could be simply included on each figure in schematic form. For example, are there a similar number of Gr5a expressing neurons in each leg? What about on the abdomen? If not, why does the fly slow down when the abdomen is stimulated? Does this reveal something about the spatial resolution of the method?

Reviewer #3:

In this Advances article, the authors build upon their previous publication from last year, describing a method for analyzing the effects of location-specific optogenetic manipulations in a post hoc manner. Specifically, they use a DLP system to randomly-scatter light at the wavelength necessary for optogenetic activation, and then, after the experiment, isolate the behavioral effects of stimulating as a function of where on the body the light hit. This method is cheaper and easier than more complicated methods that require real-time tracking and targeting for specific body parts. As a proof of concept, the authors show sensible effects for stimulating two different types of neurons: bristle sensory neurons and Gr5a taste receptors.

On the whole, I think that this method, while having its limitations (all clearly stated in the Discussion), would be an important tool in the fly behavioral neuroscience toolbox, and I encourage acceptance of the article (especially as more of a methods paper). I am somewhat skeptical of the bristle mechanoreceptor results, as there appear to be non-specific targeting – looking back at the original paper – but I think that the results are compelling enough to serve as a proof-of-concept here. This is a caveat that I think needs to be made explicit in the final version, but, again, I think that this is a solid advance, and I encourage publication.
