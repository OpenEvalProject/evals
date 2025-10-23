# Peer review - Round 1

Editors:
- Saskia Haegens, Columbia University College of Physicians and Surgeons United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.47035.031](https://doi.org/10.7554/eLife.47035.031)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Acceptance summary:

In this study, Hermes and colleagues develop and test a computational model that predicts oscillatory gamma band responses for various visual stimuli. A narrowband gamma response as measured with intracranial recordings in humans was elicited only by a specific subset of stimuli (i.e., visual gratings), in contrast with the broadband and fMRI responses that were observed for a much wider range of images. The authors suggest that gamma band oscillations might reflect gain control. This study adds to the growing line of research challenging the purported role of gamma oscillations in information communication, at least, in the visual system. Overall this topic is timely, interesting, and sure to generate discussion regarding the mechanistic role of gamma band oscillations. The work is therefore of interest to both cognitive and systems neuroscientists.

Decision letter after peer review:

Thank you for submitting your article "An image-computable model for the stimulus selectivity of gamma oscillations" for consideration by eLife. Your article has been reviewed by four peer reviewers, including Saskia Haegens as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Laura Colgin as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Hesham ElShafei (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this study, Hermes and colleagues develop (and test) a computational model that predicts gamma responses for various visual stimuli. In comparison to broadband ECoG gamma and fMRI BOLD responses, a narrowband ECoG oscillatory gamma response was elicited by a specific subset of stimuli, i.e., visual gratings. This study adds to the growing line of research challenging the purported role of gamma oscillations in information communication, at least in the visual system.

Essential revisions:

Overall this topic is timely, interesting, and sure to be controversial (in a good way!). Both the experimental part of the study and the modeling part are of high quality in terms of conceptualization, design, implementation and results, and the manuscript is generally well written. That being said, all reviewers agreed that the authors would have to tone down some of the fairly strong/conclusive arguments, connect to the wider literature on gamma, do some more explicit model comparisons, include statistics on the brain data, and separate induced from evoked activity. We detail these suggestions below.

Regarding fairly strong conclusions (i.e., that gamma is a biomarker for gain modulation and cannot support binding/communication/etc):

1) As with all negative findings, one essentially cannot exclude type-2 error, i.e., that the effect was there but the experiment failed to measure it. This is a universally acknowledged limitation of negative findings. Related to this, it would actually be essential that the authors provide statistical significance for the% signal change. The scale of gamma signal change goes up to 2000%, whereas the BOLD only goes up to 5%. It remains unclear how much response-change would be significant, i.e., would a 5% response-change in narrowband gamma response be considered significant or noise?

2) Even if there was no significant% signal change in the gamma band for many stimuli, this still does not mean that gamma oscillations do not play a role in cortical function. See the classic work by the group of Stefano Panzeri on natural images (for instance Belitski et al., 2008) where gamma carries information about the stimulus. Also see more recent work by Besserve et al., 2015, where they show that other observables such as gamma phase convey information transfer. Similarly, there are even reports of neurons locking to gamma oscillations in the absence of visual stimuli (e.g., Vinck et al., 2013). In fact, gamma oscillations have first been described as spontaneous (in the absence of stimuli) oscillations in thalamocortical circuits (see classical work by Steriade et al). Thus, while it is clear that these oscillations are indeed strongly stimulus specific, the fact that not all stimuli here induce large gamma oscillations does not mean that gamma oscillations do not exist or play a general role in cortical function. Furthermore, the authors should discuss how their conclusions fit in with previous reports of narrowband gamma modulation during the anticipation of a stimulus or the maintenance of some of its features. Related, while we are aware this paper deals with gamma oscillations in the visual cortex, it would be relevant to discuss whether the authors believe this (potential) functional role of gamma generalizes to other sensory (e.g., auditory and somatosensory cortices) and non-sensory areas (e.g., prefrontal areas). The general discussion would benefit from such an outlook.

3) This study itself (Figure 9) produces interesting insights into when these oscillations will be prominent, e.g., in grating-like structures where there is some spatial homogeneity (in addition to temporal homogeneity). Thus, there can be more microscopic gamma activity (e.g., at the scale of spiking or LFP receptive fields) in response to image parts that effectively stimulate gamma. The fact that this activity is not strong enough to drive the more macroscopic ECoG signal does not mean that the activity is absent or that other aspects of the activity such as its phase or the locking of neurons to it are not functionally important. What if the dynamic range of gamma -responses is just very high, with high responses for gratings, but with also existing responses for other types of stimuli, which sometimes constitute the majority of the broadband response (e.g., see Electrode 7/8 for curve patterns)?

Regarding the time-windows of analysis:

4) First, why did the authors opt for a baseline interval that could potentially be contaminated by early responses to the images? In addition to pooling all trials to compute this baseline, this might render any conclusion on the magnitude of gamma responses somewhat circular, i.e., weak gamma responses to circular patterns would be even weaker when computed relative to stronger gamma responses to gratings.

5) Evoked responses could potentially confound not only the broadband but also the gamma estimation. The time period that is used for computation of the broadband and gamma response includes the time window (0-200/250ms) of these visual evoked responses. Do the authors differentiate between evoked and induced responses? Do these contribute equally to the narrow- and broadband responses? The inclusion of phase-locking plots would be insightful as these components might reflect different processes.

Regarding model testing and comparison:

6) The SOC model was trained on broadband responses, which also include the narrowband gamma-band, which was used for the OV model. What information is present in activity which does not include the gamma-band? What is the relationship between the two presented models? Can the SOC model be fit to broadband without gamma activity and still yield high R2?

7) While the authors show data for all 15 electrodes, the quantification of model output could be improved. While in the natural image simulation study, the models are contrasted against each other explicitly (Figure 9), this is not the case for experimental work. Currently only the mean R2 is reported for each model, not the dispersion. That is, the authors should perform explicit model comparisons: run the SOC model on the gamma response and the OV model on the broadband response and show that the SOC model predicts broadband better than gamma and vice versa. Additionally, it is not clear a straight linear regression is the best approach here; what do the fits look like if a non-parametric Spearman correlation is used?

8) "Note that R2 is defined here with respect to zero, rather than with respect to the mean response (similar as in (Kay et al., 2013b)…" This needs to be elaborated as this is crucial for the conclusions. Furthermore, it would be good to see some statistical significance of the accuracies with respect to chance level.
