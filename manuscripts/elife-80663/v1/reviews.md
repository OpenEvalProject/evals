# Peer review - Round 1

Editors:
- Michael J Frank, https://ror.org/05gq02987 Brown University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80663.sa0](https://doi.org/10.7554/eLife.80663.sa0)

This theoretical work is important in that it bridges neural mechanisms within the hippocampus with the abstract computations it is thought to support for reinforcement learning. The study offers a potential mechanism by which spike timing dependent plasticity and theta phase precession within spiking neurons in CA3 and CA1 can yield successor representations. The simulations are compelling in that they continue to hold even when some of the simple but less realistic assumptions are relaxed in support of more realistic scenarios consistent with biological data.


---

# Peer review - Round 1

Editors:
- Michael J Frank, https://ror.org/05gq02987 Brown University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80663.sa1](https://doi.org/10.7554/eLife.80663.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Rapid learning of predictive maps with STDP and theta phase precession" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Michael E. Hasselmo (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Significantly more discussion of the work's relationship to relevant prior models of the hippocampus (as described by Reviewer #1)

2) New simulations that address Reviewer 2's concerns about biological plausibility.

3) Analysis that sheds light on why theta sequences + STDP approximates the TD algorithm (as described by Reviewer #2).

The second essential revision above may involve significant restructuring of the modeling approach. If the authors wish to undertake this, we will be happy to consider the substantially revised version for publication in eLife.

Reviewer #1 (Recommendations for the authors):

Page 4 – top line – "in the successor representation this is because CA3 place cells to the left…". I think this is confusing as the STDP model essentially generates the same effect. I think this should say: "In the network trained by Temporal Difference learning this is because CA3 place cells to the left…". This better description is used further down where the text says "between STDP and TD weight matrices". Throughout the manuscript

Page 4 – end of the first paragraph – "potentially becoming negative" – it is disconcerting to have this discussion of the idea of synaptic weights going from positive to negative in the context of the STDP model. One of the main advantages of this model is its biological realism, so it should not so casually mention violating Dale's law and having the synapse magically switch from being glutamatergic to GABAergic. This is disturbing to a neuroscientist.

Page 4- "is an essential element of this process." – The importance of theta phase precession to sequence learning with STDP has been discussed in numerous previous papers. For example, in a series of four papers in 1996, Jensen and Lisman describe in great detail a buffer mechanism for generating theta phase precession, and show how this allows encoding of a sequence. This is also explicitly discussed in Koene, Gorchetnikov, Cannon, and Hasselmo, Neural Networks, 2003, in terms of a spiking window of LTP less than 40 msec that requires a short-term memory buffer to allow spiking within this window.

Page 4 – "our model and the successor representation" – again this is confusing and should instead contrast "our model and the TD trained successor representation"

Page 6 – "in observed" – is observed.

Page 6 – "binding across the different sizes" – This needs to be stated more clearly in the text as it is very vague. I would suggest adding the phrase: "regardless of the scale difference".

Figure 4D – "create a physical barrier" – this is very ambiguous as it recalls a physical barrier in the environment as between two rooms – should instead say "created an anatomical segregation".

Page 8 – "hallmarks of successor representations" – there should be citations for what paper shows these hallmarks of the successor representation.

Page 8 – "arrive in the order" – Here is a location where citations to previous papers on the use of a phase precession buffer to correctly time spiking for STDP should be added (i.e. Jensen and Lisman, 1996; Koene et al. 2003).

Page 8 – "via Hebbian learning alone" – add "without theta phase precession" to be clear about what is not being included (since it could be anything such as other aspects of a learning rule).

Page 9 – "for spiking a feedforward network" – what does this mean – do they mean "for spiking in a feedforward network"? Aren't these other network mechanisms less biological realistic than the one presented here? I'd like to see some critical comparison between the models.

Page 9 – "makes a clear prediction…should impact subsequent navigation and the formation of successor features" – This is not a clear prediction but is instead circular – it essentially says – "if successor representations are not formed successor representations will not be observed" This is not much use to an experimentalist. This prediction should be stated in terms of a clear experimental prediction that refers only to physical testable quantities in an experiment and not circularly referring to the same vague and abstract concept of successor representations.

Page 9 – "to reach a hidden goal" – A completely different hippocampal modeling framework was used to model the finding of hidden goals in the Morris water maze in Erdem and Hasselmo, 2012, Eur. J. Neurosci and earlier work by Redish and Touretzky 1998, Neural Comp. To clarify the status of the successor representation framework relative to these older models that do not use successor representations, it would be very useful to have a few sentences of discussion about how the successor representation differs and is somehow either advantageous or biologically more realistic than these earlier models.

Page 9 "Lesions of the medial septum" – inactivation of the medial septum has also been shown to impair performance in Morris water maze (Chrobak et al. 2006).

Page 9 – "physical barrier to binding" – this is again very confusing as there is no physical barrier in the hippocampus. They should instead say "anatomical segregation"

Citation 32 – Mommenejad and Howard, 2018 – This is a very important citation and highly relevant to the discussion. However, I think it should just be cited as BioRXiv. It is confusing to call it a preprint.

Reviewer #2 (Recommendations for the authors):

This is an interesting study, and I enjoyed reading it. However, I have a number of concerns, particularly regarding the biological plausibility of the model, that I believe can be addressed with additional simulations and analysis.

– I had a number of concerns regarding the biological plausibility of the model and the choice of parameter settings, especially:

1) Mapping from rates to rates. The CA3 neurons act on CA1 neurons via their firing rate rather than their spikes, but the STDP rule acts on the spikes. What happens if the CA1 neurons are driven by the synaptically-filtered CA3 spikes rather than the underlying rates? How does the model perform, and how does the performance vary with the number of CA3 neurons (since more neurons may be required in order to average over the stochastic spikes)?

2) Weights are initialised as Wij=deltaij, meaning a 1-1 correspondence from CA3 to CA1 cells. This would have been ok, except that the weights are not updated during learning – they are held fixed during the entire learning phase and only updated on aggregate after learning. Thus, during the entire learning process each CA1 cell is driven by exactly 1 CA3 cell, and therefore simply inherits (or copies) the activity of that CA3 cell (according to equation 2). If either 1) a more realistic weight initialisation were used (e.g., random) or 2) weights were updated online during learning, it seems likely that the proposed mechanism would no longer work.

3) Lack of discussion of phase precession in CA1 cells. What are the theta firing patterns of CA1 (successor) cells in the model? Do they exhibit theta sequences and/or phase precession? We are never told this. The spike phase of the downstream CA1 cell is extremely important for STDP, as it determines whether synapses associated with past or future events are potentiated or suppressed (see Figure 8 of Chadwick et al. 2016, eLife). Based on my understanding, in the current setup CA1 place cells should produce phase precession during learning (before weights are updated), but only because each CA1 cell copies the activity of exactly one CA3 cell, which is unrealistic. Moreover, after the weights are updated, whether they produce phase precession is no longer clear. It is important to determine whether the proposed mechanism works in the more realistic scenario in which both CA3 and CA1 cells exhibit phase precession, but CA1 cells are driven by multiple CA3 cells.

4) Related to the preceding comment, there is a phase shift/delay between CA3 and CA1 (Mizuseki, Buzsaki et al., 2010). This doesn't seem to have been taken into account. Can the model be set up so that i) CA1 cells receive inputs from multiple CA3 cells ii) both CA3 and CA1 cells exhibit phase precession iii) there is the appropriate phase delay between CA3 and CA1?

5) Dependence of learning on the noisiness of phase precession. The hyperparameter sweep seems to omit some of the most important variables, such as the spread paramaeter (kappa) and the place field width and running speed (see next comment). Since the successor representation is shown to be learned well when kappa=1 but not when kappa=0 (i.e. when phase precession is removed), this leaves open the question of what happens when kappa is bigger than or small than 1. It would be nice to see kappa systematically varied and the consequences explored.

6) Wide place fields and slow speeds. Place fields in the model have a diameter of 2 metres. This is quite big – bigger than typical place field sizes in the dorsal hippocampus (which often have around 30 cm diameter, or 15 cm radius). Moreover, the chosen velocity of 16 cm/s is quite slow, and rats often run much faster in experiments (30 cm/s and higher). With the chosen parameters, it takes the rodent 12.5 s to traverse a place field, which is unrealistically long. My concern is that this setup leads to a large number of spikes per pass through a place field and that this unrealistic setting is needed for the proposed mechanism to learn effectively in a reasonable number of laps. What happens when place fields are smaller and running speeds faster, as is typically found in experiments? How many laps are required for convergence?

7) Running speed-dependence of phase precession and firing rate. The rat is assumed to run at a fixed speed – what happens when speed is allowed to vary? Running speed has profound effects on the firing of place cells, including i) a change in their rate of phase precession ii) a change in their firing rate (Huxter et al., 2003). More simulations are needed in which running speed varies lap-by-lap, and/or within laps.

8) Two-dimensional phase precession. There is debate over how 2D environments are encoded in the theta phase (Chadwick et al. 2015, 2016; Huxter et al., 2008; Climer et al., 2013; Jeewajee et al., 2013). This should be mentioned and discussed – how much do the results depend on the specific assumptions regarding phase precession in 2D? For example, Huxter et al. found that, when animals pass through the edge of a place field, the cell initially precesses but then processes back to its initial phase, but this isn't captured by the model used in the present study. Chadwick et al. (2016) proposed a model of two-dimensional phase precession based on the phase locking of an oscillator, which reproduces the findings of Huxter et al. and makes different predictions for phase precession in two dimensions than the Jeewajee model used by the authors. It would be nice to test alternative models for 2D phase precession and determine how well they perform in terms of generating successor-like representations.

9) Modelling the distribution of place field sizes along the dorsoventral axis. Two important phenomena were omitted that are likely important and could alter the conclusions. First, there is a phase gradient along the dorsoventral axis, which generates travelling theta waves (Patel, Buszaki et al., 2012; Lebunov and Siapas, 2009). How do the results change when including a 180 (or 360) phase gradient along the DV axis? The authors state that "A consequence of theta phase precession is that the cell with the smaller field will phase precess faster through the theta cycle than the other cell – initially it will fire later in the theta cycle than the cell with a larger field, but as the animal moves towards the end of the small basis field it will fire earlier" – this neglects to consider the phase gradient along the DV axis (see also Leibold and Monsalve-Mecado, 2017). Second, the authors chose three discrete place field sizes for their dorsoventral simulations. How would these simulations look if a continuum of sizes were used reflecting the gradient along the dorsoventral axis? Going further, CA1 cells likely receive input from CA3 cells with a distribution of place field sizes rather than a single place field size – how would the model behave in that case?

– There is no theoretical analysis of why theta sequences+STDP approximates the TD algorithm, or when the proposed mechanism might/might not work. The model is simple enough that some analysis should be possible. It would be nice to see this elaborated on – can a reduced model be obtained that captures the learning algorithm embodied by theta sequences+STDP, and does this reduced model reveal an explicit link to the TD algorithm? If not, then why does it work, and when might it generalise/not work?

– The comparison of successor features to neural data was qualitative rather than quantitative, and often quite vague. This makes it hard to know whether the predictions of the model are actually consistent with real neural data. It would be much preferred if a direct quantitative comparison of the learned successor features to real data could be performed, for example, the properties of place fields near to doorways.

– Statistical structure of theta sequences. The model used by the authors is identical to that of Chadwick et al. (2015) (except for the thresholding of the Gaussian field), and so implicitly assumes that theta sequences are generated by the independent phase precession of each place cell. However, the authors mention in the introduction that other studies argue for the coordination of place cells, such that theta sequences can represent alternative futures on consecutive theta cycles (Kay et al.). This begs the question: how important is the choice of an independent phase precession model for the results of this study? For example, if the authors were to simulate a T-maze, would a model which includes cycling of alternative futures learn the successor representation better or worse than the model based on independent coding? Given that there now is a large literature exploring the coordination of theta sequences and their encoded trajectories, it would be nice to see some discussion of how the proposed mechanism depends on/relates to this.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Rapid learning of predictive maps with STDP and theta phase precession" for further consideration by eLife. Your revised article has been evaluated by Michael Frank (Senior Editor) and the Reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1. Spiking model. We all agree with you that a full spiking model would be much too complex. However, since you already generate spikes using a Poisson process, it would be useful to see a simulation where the Poisson rate of CA1 cell is determined by the integration of the incoming CA3 spikes (perhaps with many incoming CA3 neurons). If this doesn't work, you should discuss why this is the case and what the implications are for the model.

2. CA3 => CA1 projections. CA1 cells still receive input from just one CA3 cell for each place field in the updated model (at least in the majority of simulations). This allows precise theta timing of the pre and post -synaptic neurons which appears to be critical for the plasticity rule to function. For example, the mathematics of Geisler et al. 2007 shows that, if the CA1 cell would receive input from a set of phase precessing CA3 cells with spatially offset place field and a Gaussian weight profile (the most common way to model CA3-CA1 connections), then the CA1 cell would actually fire at the LFP theta frequency and wouldn't phase precess, and as a consequence the STDP mechanism would no longer learn the successor representation. This suggests strong constraints on the conditions under which the model can function which are currently not being adequately discussed. This should be investigated and discussed, and the constraints required for the model to function should be plainly laid out.

3. A similar concern holds with the phase offset between CA3 and CA1 found by Mizuseki et al. The theta+STDP mechanism learns the successor representation because the CA1 cells inherit their responses from a phase-precessing upstream CA3 cell, so the existence of a phase lag is troubling, because it suggests that CA1 cells are not driven causally by CA1 cells in the way the model requires. You may be right that, if some external force were to artificially impose a fixed lag between the CA3 and CA1 cell, the proposed learning mechanism would still function but now with a spatial offset. However, the Reviewer was concerned that the very existence of the phase lag challenges the basic spirit of the model, since CA1 cells are not driven by CA3 cells in the way that is required to learn causal relationships. At the very least, this needs to be addressed and discussed directly and openly in the Discussion section, but it would be better if the authors could implement a solution to the problem to show that the model can work when an additional mechanism is introduced to produce the phase lag (for example, a combination of EC and CA3 inputs at different theta phases?)

4. DV phase precession. The Reviewer would still like to see you introduce DV phase lags, which could be done with a simple modification of the existing simulations. At minimum, it is critical to remove/modify the sentence "A consequence of theta phase precession is that the cell with the smaller field will phase precess faster through the theta cycle than the other cell – initially it will fire later in the theta cycle than the cell with a larger field, but as the animal moves towards the end of the small basis field it will fire earlier." As R2 noted in their original review, this is not the case when DV phase lags are taken into account, as was shown by Leibold and Monsalve-Mercado (2017). Ideally, it would be best to update simulations updated to account for the DV phase lags and the discussion updated to account for their functional implications

Reviewer #1 (Recommendations for the authors):

I am satisfied with the response of the authors to the reviewer's comments.

Reviewer #2 (Recommendations for the authors):

While the reviewers have undertaken a number important additional analyses which address some of the concerns raised in the review, several of the most pressing concerns regarding biological plausibility have not been addressed. In particular, each CA1 place field is still inherited by exactly 1 CA3 place field in the updated protocol, and cells still interact via their firing rates with spikes only being used for the weight updates. Moreover, the authors chose not to address concerns regarding quantitative comparisons between the model and data. Overall, while the authors correctly point out that their primary contribution should be viewed as illustrating a mechanism to learn successor representations via phase precession and STDP, this message is undermined if the proposed mechanism can't function when reasonable assumptions are made regarding the number of cells and their mode of interaction.

Detailed points below:

1) In the updated protocol where CA1 cells receive inputs from multiple CA1 cells, the model still copies CA3 place fields to CA1 place fields in a 1-1 manner. This is not biologically plausible, since receptive fields in the brain are formed by integration of thousands of synaptic inputs from cells with spatially offset but overlapping receptive fields. Moreover, neurons in the model still interact from rates to rates, with plasticity instead acting only on spikes. The authors could have addressed these two concerns jointly by having CA1 cells integrate input from a large number of spiking CA3 neurons with spatially overlapping place fields and plastic synapses, but since the authors chose not to do so, I can only assume that the model doesn't work when realistic assumptions are incorporated. Such an approach needn't involve simulating a full spiking network as the authors suggest – rather, a GLM/LNP style model can be used to model CA1 spikes in response to CA3 spiking input. Moreover, I do not see any reason why this should complicate the comparison to the TD successor representation as suggested by the authors, as the model would still have a continuous rate underlying the Poisson process that could be used to this end. If the proposed model can't be made to work with realistic numbers of CA3 neurons (with realistic firing rates and plastic synapses), then the proposed mechanism is not a plausible learning rule for the hippocampus, which undercuts the central message of the study.

2) The authors chose not perform a quantitative comparison of the model to experimental data (e.g., clustering of place fields around doorways etc.), leaving a central concern unaddressed. While I understand that theories of the hippocampal successor representation more generally have been compared to data, the lack of quantitative comparison of the particular model proposed in this study is still troubling to me.

3) Many other concerns were not addressed, such as:

– The phase shift between CA3 and CA1. While the authors may be correct that, if a phase shift were artificially imposed on the model, this would entail a spatial shift along the track, the model as it stands is premised on the notion that CA1 cells inherit their activity entirely from upstream CA3 cells, and the model predicts that the two regions are in phase with one another. If a phase shift were imposed by another mechanism (e.g. EC input), then CA1 cells would no longer inherit their responses from CA3, and the proposed mechanism for learning the successor representation would no longer function. Thus, it seems essential to the proposed model that CA3 and CA1 are in phase, in contrast to experimental data.

– The phase shift along the DV axis and its impact on phase relationships. In the revised manuscript, the authors still say "A consequence of theta phase precession is that the cell with the smaller field will phase precess faster through the theta cycle than the other cell – initially it will fire later in the theta cycle than the cell with a larger field, but as the animal moves towards the end of the small basis field it will fire earlier.", but as pointed out in the original review (and shown by Leibold et al.), this is not true when the DV phase shift is included. I see no reason why unrealistic assumptions should be made in the model regarding DV phase precession.
