# Peer review - Round 1

Editors:
- Miriam Spering, The University of British Columbia Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64278.sa1](https://doi.org/10.7554/eLife.64278.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper provides compelling evidence for a new explanation of how post-saccadic visual information could shape sensorimotor learning processes that keep perceptual and motor functions accurate and in sync. It is based on the intriguing idea that learning is driven by updating a pre-saccadic target position by subtracting the corollary discharge signal of the saccade that was just executed from the post-saccadic location of the target. This idea of a postdictive learning signal runs counter to the currently dominant view that saccade adaptation aims to reduce errors in the prediction of post-saccadic target locations. Critically, it explains empirical findings regarding both saccadic adaptation and trans-saccadic localization.

Decision letter after peer review:

Thank you for submitting your article "Visuomotor learning from postdictive motor error" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Miriam Spering as the Reviewing Editor and Tirin Moore as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Martin Rolfs (Reviewer #1) and Thérèse Collins (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

This paper provides evidence for a new explanation of how post-saccadic visual information could shape sensorimotor learning processes that keep perceptual and motor functions accurate and in synch. It is based on the idea that learning is driven by updating a pre-saccadic target position by subtracting the corollary discharge signal of the saccade that was just executed from the post-saccadic location of the target. This idea of a postdictive learning signal runs counter to the currently dominant view that saccade adaptation aims to reduce errors in the prediction of post-saccadic target locations. Critically, it explains empirical findings regarding both saccadic adaptation and trans-saccadic localization. The beauty of the approach is to model three different gains (visual, motor, and corollary discharge gains) in the sensorimotor system at the same time. To achieve this, the authors measure saccade accuracy as well as perceptual localization both before (during fixation) and after saccades at different points in time in the learning process, and in four different adaptation conditions (inward vs outward; constant visual error vs constant target step). In combination, these measures allow the authors to differentiate predictive from postdictive learning regimes as well as their consequences for saccade adaptation and trans-saccadic perception in a single paradigm. The authors then show how their account offer explanations of a range of additional findings repeatedly reported in the literature, based on a simple sensorimotor learning process. These additional phenomena include steady states of adaptation achieved when the error signal in nullified, persistent saccade hypometria, incomplete learning given consistent feedback, and differences between inward- and outward learning.

All reviewers commended the authors on the clarity of the results, and the novelty and importance of their approach. A few substantive concerns were discussed, but these mainly pertain to terminology and some suggestions regarding model assumptions and applications.

Revisions:

1) The most substantive concern shared amongst reviewers regards terminology, specifically, the definition of corollary discharge (CD), a central concept in the report.

First, is CD an estimate of the motor command, or is it a copy of the motor command (Figure 2)? The Wurtz Lab seems to vacillate somewhat on this issue as well so maybe this reflects a confusion in the field (Cavanaugh et al. 2016 say it is a "close copy of the actual movement command"; Cavanaugh et al., 2020 say "…CD is a copy of a neuronal command…"). Related to this, there is also some confusion over what to call the input to the internal model vs. the output of the model. The authors call the output of the internal model CD, so what would the input be called? Lastly, the authors introduce the concept of efference copy which adds to the confusion. The name given to a non-causal copy of the motor command is efference copy or corollary discharge (Crapse and Sommer, 2008, Nature Reviews Neuroscience). CD is then used by the forward model to generate a prediction about the sensory consequences of the movement. Using "CD" as a term for the output of the forward model is unusual and may lead to confusion for readers.

In sum, the reviewers consider this an opportunity to provide clarification of the terminology for the field in the context of the current proposed model.

2) Further to the issue of terminology, the reviewers suggest that the authors call the "internal estimate of the saccade vector" a "visual estimate of saccade vector". Indeed, the estimated saccade vector is a visual representation, i.e. a translation the motor command into an estimate of the distance, in visual space, they eyes have travelled. This makes perfect sense as the output of a forward model, but calling the output a "saccade vector" suggests something motor, and this is confusing.

3) There is also a lack of explicit predictions (tested or suggested) generated by the model, as well as minimal tests of its robustness which are required to show that the results generalize beyond the task. The reviewers think that the manuscript could be more compelling if the authors used the postdictive model and their framework to generate predictions beyond their data set. The reviewers are not asking for follow-up experiments but merely to discuss these ideas for future testing (behaviorally or neurophysiologically). This could be done either as an additional section in the Discussion, or the predictions could be presented as the results are explained in the Results section.

4) How does the postdictive model generalize to natural visual behavior, if at all? The authors touch on this issue, but I am specifically interested in any thoughts on whether the results depend on (arguably unnatural) repeated saccades with the same direction and amplitude in complete darkness.

5) The reviewers would like to see a plot of individual subjects' data. Perhaps use for the format of Figure 3B to separately show the results of two groups of 16 subjects?

6) Finally, the reviewers discussed the possibility of broadening the scope of the paper to another very similar visuo-spatial saccade task in which CD use has been theorized to be crucial: saccadic suppression of displacement (SSD). It seems that extending their model to SSD would be rather easy, and such a generalization would lend credence to it.

The reviewers also suggest that the modeling code is made available, commented with clear references to corresponding equations in the manuscript, and that complete data files of all 32 subjects be made available.
