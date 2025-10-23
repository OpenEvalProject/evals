# Peer review - Round 1

Editors:
- Andrew Fuglevand, University of Arizona, USA

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55177.sa1](https://doi.org/10.7554/eLife.55177.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This mammalian muscle spindle is a central player in the sense of proprioception. It is a complex biological device that is generally sensitive to changes in the length of the skeletal muscle within which it resides. Yet it's response properties (i.e., firing rates of its sensory afferents) are oftentimes inexplicable in terms of it operating as a simple muscle-length sensor. This paper represents a major step forward in understanding the basis of the elegant intricacies of the muscle spindle. The authors have used a cross-bridge based model of the intrafusal fibers of the muscle spindle to accurately predict (and provide insight into) Ia afferent responses to a host of mechanical stimuli. As illuminated by the simulations, Ia afferent activity is shaped by interactions among multiple mechanical and neural factors. While some questions remain as to the nature of the transduction process itself, this work offers a key advance in deciphering the enigmatic muscle spindle.

Decision letter after peer review:

Thank you for submitting your article "Diverse muscle spindle firing properties emerge from multiscale muscle mechanics" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Andrew Fuglevand as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by John Huguenard as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Arthur Prochazka (Reviewer #2); Gerald Loeb (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional simulations are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is 'in revision at eLife'. Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

The muscle spindle is one of the most thoroughly studied sensory receptors in the somatosensory system, yet much is still unknown about how it works. Commendably, the authors have attempted to model the responses of spindle sensory afferents using a biophysical model of intrafusal muscle fibers. The model was shown to mimic experimentally recorded afferent activity in a number of situations. Indeed, it is encouraging to see attention being paid again to the elegant complexities of spindle receptors after years of over-simplification in control models. Nevertheless, there are concerns (detailed in the essential revisions below) about those aspects that were left out.

Essential revisions:

1) The assumption that extrafusal muscle force can serve as a proxy for intrafusal fiber force needs to be fully addressed. Indeed, there are well known situations for which an assumed correspondence between extrafusal and intrafusal forces would seem to fail to reproduce experimental results. For example, the classical experimental signature used to identify Ia afferents is a cessation in their discharge during an evoked twitch in the extrafusal muscle fibers. Likewise, the model would seem to fail to reproduce spindle afferent responses during imposed length changes with and without concomitant homonymous extrafusal muscle contractions (e.g. Elek, Prochazka, Hulliger, Vincent. In-series compliance of gastrocnemius muscle in cat step cycle: do spindles signal origin-to-insertion length? J. Physiol., 429, 237-258, 1990). The authors need to include additional simulations of these fundamental experimental phenomena and to fully address the outcome in the Discussion.

2) The authors suggest that their model provides a unifying biophysical framework for understanding muscle spindle activity, yet there was little attention paid to how intrafusal force or yank is transduced into a receptor potential. Such a unifying framework would need to include mechanisms of transduction by mechanically-gated ion channels. As such, the role that sensory transduction mechanisms play in shaping spindle afferent activity needs to be addressed – either in the model or in the Discussion.

3) The role that intrinsic properties and associated time-varying conductances (e.g. such as those underlying spike-frequency adaptation) in muscle spindle afferents may play in influencing firing dynamics needs to be addressed in the model or in the Discussion.

4) There needs to be more clarity in the description of the model and what aspects of the model were original and what aspects were based on previous work, for example, that of Campbell et al. (2014) and MyoSim.

5) The simulated response (i.e. the driving potential) of the biophysical model depicted in Figure 6A to repeated triangular length changes (without pauses) does not resemble the experimental firing rate data to repeated triangular length changes shown in Figure 2B. In particular, the model exhibits marked abbreviation of the responses to the 2nd and 3rd length changes that are not evident in the experimental data of Figure 2. This disparity between experimental and simulated findings needs to be discussed.

6) Any general model that aims to account for the activity of spindle afferents during natural activities must account for the well-documented independence among α, γ dynamic and γ static activation patterns and kinematics, whose different effects on Ia activity have been simulated, measured or inferred in a variety of experiments and integrated into previous models (see Mileusnic et al., 2006). The Discussion should identify which scenarios have not been simulated and which might be problematic for their general thesis.
