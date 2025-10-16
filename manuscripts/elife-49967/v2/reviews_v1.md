# Peer review - Round 1

Editors:
- David Kleinfeld, University of California, San Diego United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.49967.sa1](https://doi.org/10.7554/eLife.49967.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Hansel and colleagues investigate the role of feedback in the stabilization of neuronal activity in cortex. The simplest models for feedback involve two populations of neurons, a single population of inhibitory neurons and a population of excitatory neurons. This class of models is sufficient to explain seeming paradoxical effects within the realm of cortical circuits, such as decreased overall inhibitory cell activity upon excitatory perturbation of inhibitory neurons. However, the authors show that "two population" models fail to offer robust solutions for the responses they observe in new, optogenetic perturbation experiments on neuronal dynamics in mouse sensory and motor cortices. Rather, a more complex model, with feedback among three classes of inhibitory neurons and associated constrained connectivity, along with a population of excitatory neurons, is needed. The "four population" models give rise to a second-order feature, disynaptic inhibition, to achieve stabilization of neuronal activity.

Decision letter after peer review:

Thank you for submitting your article "Mechanisms underlying the response of mouse cortical networks to optogenetic manipulation" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: David Golomb (Reviewer #1); Misha Tsodyks (Reviewer #3).

The reviewers have discussed the reviews with one another and the Senior Editor has drafted this decision to help you prepare a revised submission.

Summary:

The "paradoxical effect" is the phenomenon that stimulation of an inhibitory neuronal population decreases the average firing activity of neurons in that population. The conditions for its existence have been under debate, and the mechanistic impacts of various types of inhibitory interneurons has not been elucidated. The manuscript of Mahrach et al. addresses these two important issues, and is a big step forward in understanding cortical dynamics. The authors present new experimental data collected from PC and PV neurons in the anterior lateral motor cortex (ALM; layer 2/3 and layer 5) and the barrel cortex (S1; layer 5) during photostimulation of PV neurons. The data show paradoxical effects in layer 5 (i.e., at a low light intensity, increasing the stimulus decreases PV firing rates proportionally to that of PC cells), while showing non-paradoxical effects in layer 2/3. The results are novel and contradict the widespread notion that the paradoxical effect is an evidence for stabilization by inhibition, and the modeling suggests an architecture consistent with the results.

Essential revisions:

1) The manuscript is based on the analytical calculations, and it is expected that readers will try to replicate them. Therefore, it is important that their description will be as clear and as detailed as possible, which will enhance the readability of the paper.

2) Overall the paper rests on comparing how photostimulation of PV neurons drives population-wide rate activity between experiments and several different models. The paper would be strengthened if the authors used statistical tests to show that layer 2/3 is significantly different than layer 5, as well as showing that the proportional decrease of PV and PC cells is a robust observation. We would like to see some actual statistical comparisons between the data and the models. More to the point, the distribution of firing rates for baseline vs. photostimulation in Figure 2 (experiment) should be compared in some statistical way to those in Figure 6 (Model 1, JEE>JEE*), Figure 8 (Model 1, JEE<JEE*), and Figure 11 (Model 2). The pie charts in Figures 6, 8, 11 are nice but they should have some confidence bounds and then compared to the equivalent pie charts of Figure 2. This will go a long way in helping the narrative of the paper where models are accepted or rejected based on the three datasets shown in Figures 1-2.

3) The data are used to assess, dismiss, and propose possible network architectures. Using analytical results derived from a balanced network framework and simulations, they settle on significantly different architectures for each layer. However, some of the reviewers were not convinced that the more complex networks capture enough of the properties present in the data, and were not persuaded by their argument that Model 1 should be dismissed with regards to layer 5, and wary of the presence of inhibitory population 'X' in Model 2.

The dismissal of Model 1 with regards to layer 5 needs additional details. Currently, the authors dismiss Model 1 since it cannot robustly capture the fact that PC and PV activity decreases proportionally in the paradoxical regime.

a) Attaching some quantitative measures to the phrase "decreasing proportionally" would assist with this argument. Figure 7A and Figure 1B lower right potentially look similar "enough".

b) Further, Figure 7—figure supplement 3 shows that the right parameters yield a great proportional decrease. I believe that this parameter regime is potentially small, but ideally it would be nice to include a figure showing how small (to my knowledge, one like Figure 3—figure supplement 3 doesn't exist for this parameter regime).

4) Relatedly, the authors propose a series of improved network architectures over the traditional E,I-two population model that incorporate known interneuron subclasses (PV, SOM, and VIP). However, with every improvement the more complex models bring, I find additional questions regarding the data that is not captured.

a) For example, Model 1 provides a network that is able to provide a non-paradoxical response such that PV neurons increase in rate at low light stimulations. This is not achievable by the E,I network. However, the heterogeneity of neurons seen as a function of stimulus strength in Model 1 seems different than experimental results (relevant figures for comparison: Figure 1B, Figure 3C, and Figure 5A), and is not discussed in the text. I would've hoped that adding such a large change in the network would've been able to better capture the data.

b) I would also like to directly compare Figure 2 (left column) with Figure 6 (left or right column). The distribution of variability of firing rates seems different between Model 1 and the experimental results. However, the strength of stimulus is different in Figure 2 than in Figure 6 (0.5 for the experiments than 0.3 and 0.9 for the simulations), so I would request that Figure 2 be remade with one of these stimulation strengths. Having a similar pie chart appear in Figure 2 would also be helpful. Lastly, marginal histograms in both figures would assist with comparison.

Also, in regards to Figure 6, the authors comment that "Remarkably, even for 0.9 mW/mm2, some of the PCs show an activity increase." However, this was not observed in experiments.

5) To capture the final missing piece of the data (i.e., the proportional decrease of PC and PV cells), the authors propose an entirely new network architecture with inhibitory interneuron 'X'.

a) In addition to this new type of neuron, the authors must also add a connection from PV to SOM cells (otherwise, rE = 0 in the large network limit). While the authors suggest that 'X' may be chandelier cells, they do not discuss why this added connection from PV to SOM would be present in layer 5 but not layer 2/3.

b) Similar to my above comment, I would expect that such a drastic change in the network would be able to capture additional features of the experimental data, but the heterogeneity present in Figure 10A is drastically different than Figure 1B, right column.

Simulations must be made publicly available.
