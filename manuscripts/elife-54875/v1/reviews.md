# Peer review - Round 1

Editors:
- Timothy O'Leary, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54875.sa1](https://doi.org/10.7554/eLife.54875.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study thoroughly addresses a long-standing question in cortical neurophysiology, namely the extent to which cortex resides in an inhibition stabilised regime. Using careful experiments and mathematical modelling the authors reveal several hallmarks of this regime in multiple cortical areas, including so-called paradoxical inhibition of inhibitory interneuron firing rate, in both awake and anaesthetised states. Together, these results provide further compelling evidence of the role of inhibition in stabilising neural activity.

Decision letter after peer review:

Thank you for submitting your article "Inhibition stabilization is a widespread property of cortical networks" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by John Huguenard as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Hillel Adesnik (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

This work address whether excitatory cortical activity is stabilised by rapid inhibitory feedback across cortical areas. One important prediction of such a model is so-called paradoxical suppression of inhibitory neurons in response to inhibitory stimulation. This prediction is validated experimentally and analysed with mathematical modelling.

The reviewers broadly agree that the study is thorough, well executed and well presented. Several issues were raised, including the need to show/quantify more raw data and population data. There are also some potential experimental confounds, explained in detail below, that should be addressed either by appropriately adjusting conclusions or if possible, by reanalysis or modelling. Finally, for the wide readership eLife caters for, the authors should make more effort to explain the importance and relevant functional consequences of the ISN regime.

Reviewer #1:

This is a well written paper without any major deficiencies. The authors address the question whether the activity of excitatory neurons is stabilised by rapid inhibitory feedback, and how common this feature is across cortical areas. The hypothesis that such inhibition-stabilised networks (ISN) would display the so-called 'paradoxical suppression' is intuitive and nicely backed up by a Wilson-Cowan model. The data does indeed show the paradoxical suppression, supporting the ISN hypothesis nicely.

The authors also address another possible explanation of the paradoxical suppression, namely the suppression of inhibition-to-inhibition coupling, and explain why this is less convincing, again supported by data. They also go into some depth on the strength of the coupling, which seems to be moderate, rather than very strong.

It would help the wider readership if the authors could go into more depth on why this question is important. It seems self-evident that cortical networks are stabilised by inhibition: few other mechanisms are rapid enough and moderate loss of inhibition generically leads to seizures.

For example, what are the computational benefits of an ISN? This is only briefly touched upon in the end of the Discussion section at the moment, and could be elaborated upon in the Introduction more.

Reviewer #2:

The paper of Sanzeni et al., demonstrates that the firing rate of inhibitory cells expressing ChR2 is suppressed at low light intensity but as intensity increases firing rate return and then becomes even higher. This is a paradoxical behavior since we expect that firing rate will increase monotonically with light intensity. The results are in a good agreement with predictions made by inhibition-stabilized network (ISN) models. Such behavior was found in superficial and deep layers of different cortical areas of awake mice and also in anesthetized mice.

The methods of the experiments are straightforward and were conducted with high standards. The presentations of the results are clear and nice. For example, the classification of cells into inhibitory and excitatory cells based on different methods is convincing. The virus vs. transgenic experiments are also clear and important. The comparisons of the effect of light before and after addition of synaptic blockers are important and help in clarification of the experiments. Finally, the demonstration of the effect in deep layers and under anesthesia are crucial. Thus, the experimental work, regardless the model, is interesting and important.

However, this study is not novel enough as similar conclusions were shown in previous studies and in particular in the 2018 study of Moore et al., from Wehr lab which presented a paradoxical increase of PV firing rate when these cells were optogenetically suppressed (the authors cite this study). Since Moore's paper includes a substantial modeling of ISN network, I am not sure if this under review study introduces novel concepts (the major difference is that in this study inhibitory cells were activated and in the 2018 paper the cells were inactivated).

As an experimentalist I have some concerns related to some experimental aspects. Unlike the previous studies, no direct measurements of excitatory and inhibitory currents were made in this study and thus my enthusiasm was reduced. Yet, the study can benefit from pharmacology, which can be better trusted compared to optogenetics.

Essential revisions:

1) Unlike the light-inactivation of inhibitory cells using Arch, illumination of the cortex of VGAT-ChR2 mice can directly cause synaptic release from the terminals, regardless the firing of the cells. I mention this issue although I don't think that it is fully understood. In other words, it is unclear if the firing of the cells directly reports the effect of light in the network (which could be better assessed using patch recordings). Ideally this could be addressed by limiting the expression of ChR2 to cell bodies. Since none of my proposed experiments are realistic for a revision, I propose to discuss this issue in detail or even try to model it.

2) Pharmacology: the effect of GABAr blockers should be tested before blocking excitatory transmission. Adding such blockers at low concentration to partially reduce the effect of inhibition perhaps will result with a similar (but opposite) effect to the optogenetic and perfusion of 3 or 4 concentrations in an increasing manner may work.

3) It is not clear if and where the population distribution of the paradoxical reduction in the firing rate of inhibitory cells is presented in the paper. It is possible that firing rate of excitatory cells is suppressed due a small fraction of inhibitory cells for which firing rate increases monotonically with light intensity.

4) As far as I understand the model is not a conductance based model. I think that providing predictions for currents can greatly help in illustrating the mechanisms (simply feed the firing rates of the cells into a single cell model).

5) The roles of short-term synaptic plasticity were not discussed or checked both in the model and in the experiments. Both depression and facilitation can contribute. Different levels of depression/facilitation of inhibitory synapses due to their activation may contribute to the effect. Without modeling them it is hard to predict their contributions.

6) Rather than changing light intensity the authors should consider increasing the surface area that is illuminated. I think that the model will predict that this will result with similar effect to that for increasing light intensity. I believe that this approach is better.

Reviewer #3:

Sanzeni et al., present a compelling new data set supporting the notion that neocortical areas operate in the inhibition stabilized regime in which recurrent inhibition is needed to balance recurrent excitation to stabilize the network. This had been theoretically proposed more than 20 years ago by Tsodyks and colleagues, and experimental data to support it was originally put forward by Ferster, Miller and colleagues in 2009 using whole cell recording in anesthetized cats. Subsequently, additional whole cell recordings in awake mice in A1 and V1 supported this model. What has been lacking was a direct test of a core prediction of the ISN model: that direct excitation of inhibitory neurons (I cells) would paradoxically lead to a net suppression of I cells at the steady state (followed by a transient increase in I cell activity). It should be clear this result was indirectly shown by measuring synaptic inhibition in the Ferster and Miller paper. The current study elegantly and rigorously used direct optogenetic stimulation of I cells in transgenic mice to show that 'paradoxical' prediction is borne out in mouse V1. The authors then go on to repeat this core result in S1 and M1 and in deeper cortical layers of these areas. Overall, I find the study well performed and the arguments sound. I previously already subscribed to this view based on the existing data, but the data in this study really is the nail in the coffin. For this reason, this study is timely and warrants publication, with eLife a suitable journal.

I do have some questions for the authors to address (both conceptual and methodological). While I agree with almost all of the authors conclusions, I would like them to address a few points in which I will act as a devil's advocate. I'd like them to conceptually, experimentally, or theoretically rule out alternative explanations for the data, however less likely they might seem than the ISN model.

1) Could it be that a very small subset of PV+ interneurons are extremely photo-excitable (perhaps a subtype that suppresses all other cell types across all layers in cortex) and that these cells are in fact responsible for the suppression of most other I cells? These cells might be so rare (inhibitory 'hub' cells) that they would be very hard to catch with extracellular recording (or they might have small spikes that are below the noise threshold). Perhaps they have a slightly delayed response to optogenetic stimulation which explains the transient increase in I cell activity prior to its suppression?

2) Could a pure feed-forward model explain their results coupled with the possibility that L4 interneurons could be more photo-excitable than L2/3 interneurons, despite being deeper in the brain? In this scenario, the 'paradoxical' I cell suppression in L2/3 could be entirely explained by loss of feedforward excitation from L4. It seems like in the data set some I cells didn't show paradoxical effects (and most of the authors data comes from above L4), so maybe this is the case?

3) In any case, the authors should show much more raw data (rather than just average data) in the main figures. I agree it's the average that matters to test the ISN model, but it would be helpful to the reader to see the distribution across units for the various effects: transient activation, shape of 'paradoxical response' etc. Some of this is in the supplement, but not much.
