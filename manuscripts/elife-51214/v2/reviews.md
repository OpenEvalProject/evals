# Peer review - Round 1

Editors:
- Arjen Stolk, Donders Centre for Cognitive Neuroimaging Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.51214.sa1](https://doi.org/10.7554/eLife.51214.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The HNN provides an intuitive way for thinking about and linking cellular- and circuit-level mechanisms in the neocortex to (source-reconstructed) neural data. Combined with the worked examples that demonstrate the application of the tool to current issues, the reviewers unanimously agreed on its relevance and potential for opening up new possibilities for the field to advance our understanding of cellular and network origins of MEG/EEG data.

Decision letter after peer review:

Thank you for submitting your article "Human Neocortical Neurosolver (HNN), a new software tool for interpreting the cellular and network origin of human MEG/EEG data" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Arjen Stolk as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Richard Ivry as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Sarang S. Dalal (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

All reviewers and editors agreed on the methodological sophistication and relevance of your software tool. However, several concerns were raised, which are summarized below. We are aware that these may be challenging to address within the usual timeframe but we all agreed that if these issues can be addressed satisfactorily, the paper would substantially improve.

Essential revisions:

1) MEG is generally considered to arise from intracellular currents, with EEG arising from extracellular currents (e.g., section 2.1 https://www.sciencedirect.com/science/article/pii/S0896627313009203). In the case of MEG, the volume currents largely cancel out, which is thought to leave intracellular currents as the main contributor to MEG signals. But volume currents are supposed to be a dominating factor in EEG, so this theoretically leads to its bias towards extracellular currents. However, the manuscript and software appear to address only intracellular currents, while MEG and EEG are discussed as if they are equivalent. This may be a necessary compromise, or the authors may disagree with the premise of MEG from intracellular and EEG from extracellular currents. However, they should be clear on their position and how this issue is handled in HNN.

2) It is a bit unsatisfying that the "Gamma rhythms" example does not use real data, given its importance to the community. Even if the authors' own experiments have not yielded data with strong gamma, there are many examples in the literature that could perhaps be obtained, and even some appropriate datasets are publicly available. For example, FieldTrip's gamma source localization tutorial provides one:

http://www.fieldtriptoolbox.org/tutorial/beamformingextended/

3) The HNN framework seems well-suited for evoked responses that are phase-locked across trials. However, gamma oscillations are often "induced", i.e., not phase-locked across trials. Does HNN provide tools to model/simulate the origins of such phase variance? If so, this should be clarified, and if not, perhaps described as a limitation.

4) There appears to be a distinction between narrowband and broadband gamma in terms of their neural underpinnings, with broadband gamma suggested to be closely linked to spiking activity (e.g. Whittingstall and Logothetis, 2009 among others). Likewise, this should be described if HNN can model this, and otherwise addressed as a limitation.

5) The "jet" colormaps for the spectrograms (Figures 6 and 7) have been heavily criticized in recent years for being extremely biased perceptually (see, e.g., https://predictablynoisy.com/makeitpop-intro). In the case of Figure 6, this results in yellow patches that "pop" somewhat misleadingly. New releases of neuroscientific software should be especially cognizant of this and ideally provide a perceptually uniform colormap as the default. See https://matplotlib.org/3.1.1/tutorials/colors/colormaps.html and https://matplotlib.org/cmocean/ for some ideas on divergent colormaps.

6) The manuscript refers to previous work by the authors for details of the biophysical model. However, it is not clear from the present manuscript how well these models compare to actual experimental data and from which species the data was obtained. For example, because the model appears to use reduced and simplified neuronal morphologies, and only a single type of inhibitory interneuron, it would be very informative to provide some assessment of whether any potential inaccuracies in the generated field potentials could exist due to reduced dendritic morphology, and whether incorporation of additional inhibitory circuitry could expand the scope of questions that could be addressed via HNN.

7) The manuscript refers several times to source localization, but the presented model appears to be of a single cortical column, and presumably, this means that it is currently not possible to study questions related to the spatial distribution of field potentials. While I have no doubt that the methods of HNN will scale well to networks of multiple cortical columns, some clarity is necessary in manuscript regarding the current capability of HNN with regards to spatially distributed networks and source localization features, and what plans are made for future releases.

8) While the manuscript addresses related work by other authors, there are now several published large-scale biophysical neural models that incorporate some form of approximated LFP computation that aids the study of neural oscillations. It would be very informative to include at least a brief comparison with e.g. the methods developed by Reimann et al., 2013, and in what ways HNN is an improvement.
