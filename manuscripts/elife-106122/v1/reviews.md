# Peer review - Round 1

Editors:
- Jean-Paul Noel, University of Minnesota United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.106122.3.sa0](https://doi.org/10.7554/eLife.106122.3.sa0)

This important study evaluates a model for multisensory correlation detection, focusing on the detection of correlated transients in visual and auditory stimuli. Overall, the experimental design is sound and the evidence is compelling. The synergy between the experimental and theoretical aspects of the article is strong, and the work will be of interest to both neuroscientists and psychologists working in the domain of sensory processing and perception


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.106122.3.sa1](https://doi.org/10.7554/eLife.106122.3.sa1)

Summary:

Parise presents another instantiation of the Multisensory Correlation Detector model that can now accept stimulus-level inputs. This is a valuable development as it removes researcher involvement in the characterization/labeling of features and allows analysis of complex stimuli with a high degree of nuance that was previously unconsidered (i.e. spatial/spectral distributions across time). The author demonstrates the power of the model by fitting data from dozens of previous experiments including multiple species, tasks, behavioral modality, and pharmacological interventions.

Strengths:

One of the model's biggest strengths, in my opinion, is its ability to extract complex spatiotemporal co-relationships from multisensory stimuli. These relationships have typically been manually computed or assigned based on stimulus condition and often distilled to a single dimension or even single number (e.g., "-50 ms asynchrony"). Thus, many models of multisensory integration depend heavily on human preprocessing of stimuli and these models miss out on complex dynamics of stimuli; the lead modality distribution apparent in figure 3b and c are provocative. I can imagine the model revealing interesting characteristics of the facial distribution of correlation during continuous audiovisual speech that have up to this point been largely described as "present" and almost solely focused on the lip area.

Another aspect that makes the MCD stand out among other models is the biological inspiration and generalizability across domains. The model was developed to describe a separate process - motion perception - and in a much simpler organism - drosophila. It could then describe a very basic neural computation that has been conserved across phylogeny (which is further demonstrated in the ability to predict rat, primate, and human data) and brain area. This aspect makes the model likely able to account for much more than what has already been demonstrated with only a few tweaks akin to the modifications described in this and previous articles from Parise.

What allows this potential is that, as Parise and colleagues have demonstrated in those papers since our (re)introduction of the model in 2016, the MCD model is modular - both in its ability to interface with different inputs/outputs and its ability to chain MCD units in a way that can analyze spatial, spectral, or any other arbitrary dimension of a stimulus. This fact leaves wide-open the possibilities for types of data, stimuli, and tasks a simplistic neutrally inspired model can account for.

And so it's unsurprising (but impressive!) that Parise has demonstrated the model's ability here to account for such a wide range of empirical data from numerous tasks (synchrony/temporal order judgement, localization, detection, etc.) and behavior types (manual/saccade responses, gaze, etc.) using only the stimulus and a few free parameters. This ability is another of the model's main strengths that I think deserves some emphasis: it represents a kind of validation of those experiments - especially in the context of cross-experiment predictions.

Finally, what is perhaps most impressive to me is that the MCD (and the accompanying decision model) does all this with very few (sometimes zero) free parameters. This highlights the utility of the model and the plausibility of its underlying architecture, but also helps to prevent extreme overfitting if fit correctly.

Weaknesses:

The model boasts an incredible versatility across tasks and stimulus configurations and its overall scope of the model is to understand how and what relevant sensory information is extracted from a stimulus. We still need to exercise care when interpreting its parameters, especially considering the broader context of top-down control of perception and that some multisensory mappings may not be derivable purely from stimulus statistics (e.g., the complementary nature of some phonemes/visemes).


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.106122.3.sa2](https://doi.org/10.7554/eLife.106122.3.sa2)

Summary:

Building on previous models of multisensory integration (including their earlier correlation-detection framework used for non-spatial signals), the author introduces a population-level Multisensory Correlation Detector (MCD) that processes raw auditory and visual data. Crucially, it does not rely on abstracted parameters, as is common in normative Bayesian models," but rather works directly on the stimulus itself (i.e., individual pixels and audio samples). By systematically testing the model against a range of experiments spanning human, monkey, and rat data - the authors show that their MCD population approach robustly predicts perception and behavior across species with a relatively small (0-4) number of free parameters.

Strengths:

(1) Unlike prior Bayesian models that used simplified or parameterized inputs, the model here is explicitly computable from full natural stimuli. This resolves a key gap in understanding how the brain might extract "time offsets" or "disparities" from continuously changing audio-visual streams.

(2) The same population MCD architecture captures a remarkable range of multisensory phenomena, from classical illusions (McGurk, ventriloquism) and synchrony judgments, to attentional/gaze behavior driven by audio-visual salience. This generality strongly supports the idea that a single low-level computation (correlation detection) can underlie many distinct multisensory effects.

(3) By tuning model parameters to different temporal rhythms (e.g., faster in rodents, slower in humans), the MCD explains cross-species perceptual data without reconfiguring the underlying architecture.

(4) The authors frame their model as a plausible algorithmic account of the Bayesian multisensory-integration models in Marr's levels of hierarchy.

Weaknesses:

What remains unclear is how the parameters themselves relate to stimulus quantities (like stimulus uncertainty), as is often straightforward in Bayesian models. A theoretical missing link is the explicit relationship between the parameters of the MCD models and those of a cue combination model, thereby bridging Marr's levels of hierarchy.

Likely Impact and Usefulness

The work offers a compelling unification of multiple multisensory tasks-temporal order judgments, illusions, Bayesian causal inference, and overt visual attention-under a single, fully stimulus-driven framework. Its success with natural stimuli should interest computational neuroscientists, systems neuroscientists, and machine learning scientists. This paper thus makes an important contribution to the field by moving beyond minimalistic lab stimuli, illustrating how raw audio and video can be integrated using elementary correlation analyses.
