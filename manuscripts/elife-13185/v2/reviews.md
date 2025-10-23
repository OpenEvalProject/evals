# Peer review - Round 1

Editors:
- Upinder S Bhalla, National Centre for Biological Sciences , India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.13185.019](https://doi.org/10.7554/eLife.13185.019)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Spike-timing-dependent dynamics of 2-arachidonoylglycerol gates endocannabinoid-mediated LTP and LTD" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors. The evaluation has been overseen by the Reviewing Editor and Eve Marder as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper proposes a model involving pre and postsynaptic signaling components involved in corticostriatal synaptic plasticity. Key components of the model include presynatpic endocannabinoid signaling with three thresholds for different forms of plasticity, and a signaling network depending on calcium for the postsynaptic network. The paper is distinctive in presenting several high-level tests of the signaling model, including some non-obvious predictions. The authors present MAGL activity as a key controller of synaptic plasticity, and suggest that endocannabinoid receptors may be important in bidirectional regulation of plasticity.

Essential revisions:

1) The reviewers appreciated the experimental and theory combination of approaches to study plasticity.

2) The model assumes a number of model free parameters such as sharp thresholds for plasticity. The authors should test model outcomes of shallow thresholds to see if the results still hold, and also conduct parameter sensitivity analysis to examine how sensitive these parameters are.

3) The predictions should extend to a somewhat broader range of stimulus cases, such as modification of pairing frequencies and number.

4) All reviewers had questions on the details of the model pathways and role of sub-parts of the overall model. The authors should clarify this, with special attention to stating which pathways are really needed for which outcome of the model.

Reviewer #1:

1) A key assumption in the model is the presence of three thresholds for LTD start, LTD stop, and LTP start, for the endocannabinoid system. The key step here (thresholding) is not implemented biophysically or biochemically, but by a mathematical threshold. I think this weakens their case for a mechanistic account of STDP. The authors discuss this and have a schematic in Figure 9—figure supplement 1, but I don't feel that the proposed sharp thresholds are physiological. I would have liked to see a chemical implementation of the thresholds. Specifically, I am concerned that the presence of a shallow (more chemical-like) turn on rather than a sharp all-or-none threshold may invalidate the results. The authors should address this.

2) A related point from Figure 3 C1: The threshold positioning and the extra bump by CB1R at the start is quite finicky. I am dubious about the dependence on such fine-tuning. Even a small shift of either the threshold or the response would invalidate the prediction that such a mechanism could account for the properties of eCB-tLTP. Here, in fact, a shallower activation function to replace the threshold might prove to be more robust, but less precise.

3) Figure 4 is impressive in its match to experiments. I wonder if it is possible for the authors to achieve a similar match for Figure 6,Figure 7,Figure 8, which also test a series of model predictions. All look good but the prediction is just a single time-point. In all cases it would be nice if the simulations went the extra step to match the experimental time-course, rather than just predict amplitude of LTP or LTD.

4) The authors should comment on what stochasticity would do to their analysis. I am concerned that this would further weaken any analysis depending on sharp thresholds.

5) The CaMKII activity seems to be a bit of an orphan in the study. It turns on for sufficient pairings for pre-post pairings, but how does this impact the plasticity? I was not able to clearly see where this happened.

6) The authors get CaMKII to turn on (Figure 2) but I don't see that the LTD stimulus (or any other) gets it to turn off. This seems incomplete.

7) ModelDB does not seem to have this model. It isn't really possible to assess the implementation without it. The authors should present the model and any simulation files needed to generate the figures, as supplementary material.

Reviewer #2:

Cui et al. use a phenomenological, but quantitative model to increase the understanding of activity patterns leading to LTP/LTD. The model predictions agree with experiments. The main contribution is to illustrate how 2AG can control both LTP and LTD.

There are things which can strengthen the study, and make the model more transparent. The latter issue is important as others then can further improve it.

1) The experimental paradigm builds on repetition with 1 Hz pre- and postsynaptic pairings in different orders/delays. As the model mechanisms for 'many-pairing' LTP builds on successive activation of CamKII while the 'many-pairing' LTD builds on 2AG production with presynaptic effects. For the latter, postsynaptic depletion of ER_Ca and presynaptic receptor desensitization contribute, thus it would be interesting to see what is predicted if 1 Hz pairing frequency is modified to e.g. 2 or 0.1 Hz. From Figure 3C the ER depletion seems significant after only 20 pairings, is that realistic? Also is this depletion needed for the model to work?

2) It seems that the model free parameters are fitted to reproduce experimental outcome (see subheading “Parameters”), thus the model is not predicting the LTP and LTD results (since the LTP and LTD outcome is used to tune the model), but rather the model can work as a quantitative hypothesis on important subcellular mechanisms. Please specify which model parameters are considered free and their sensitivity to variations.

3) Details on the model that need to be made more transparent are, for example:

A) The activation of DAGL. A Ca dependent phosphorylation reaction assumed but is it not a more direct Ca activation of DAGL and presence of DAG sufficient to produce 2AG for example? Likely no consequences for the outcome but please clarify;

B) Which and how different Ca sources (NMDA_Ca, Ca via TRPV1R, ER_Ca, L_Ca, etc.) contribute to the total pool of Ca used to activate CamKII, DAGL, etc. (add e.g. a supplementary figure following Figure 2 or Figure 3 showing how the total Ca elevation is the sum of several sources). How is the 'unintuitive' result achieved that Ca is larger if post-pre stimulation is used compared to pre-post? If only NMDA_Ca is considered pre-post should give rise to more Ca influx into the cell as compared to post-pre;

C) Please plot separately the Wpre and Wpro to see how it compares to Wtotal plotted in several figures;

D) In paragraph three, subheading “Postsynaptic element” the postsynaptic model from Graupner and Brunel is adjusted for MSNs and it is assumed that PKA is indirectly activated by Ca via PP2A, motivate this or maybe remove the Ca dependency of PKA as it is hard to see how the AC5-PKA reactions is effectively stimulated by Ca in MSNs, even in the presence of DARPP75 disinhibition via PP2A). That CaMKII is activated following a sufficient number of pairings in MSNs is reasonable, but it probably happens in a slightly different way as in hippocampus.
