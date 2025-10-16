# Peer review - Round 1

Editors:
- Upinder Singh Bhalla, https://ror.org/03ht1xw27 Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79535.sa0](https://doi.org/10.7554/eLife.79535.sa0)

This study describes the use of artificial neural network (ANN) methods to accurately replicate the biophysical behavior of detailed single-neuron models. The method has the potential to greatly increase the speed of neuronal modeling compared to conventional differential equation-based modeling, and scales particularly well for large network models. The authors demonstrate the fidelity of their ANN model cells over a wide range of stimulus and recording conditions including electrical and optical readouts.


---

# Peer review - Round 1

Editors:
- Upinder Singh Bhalla, https://ror.org/03ht1xw27 Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79535.sa1](https://doi.org/10.7554/eLife.79535.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Ultrafast Simulation of Large-Scale Neocortical Microcircuitry with Biophysically Realistic Neurons" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board if Reviewing Editors, and the evaluation has been overseen by Joshua Gold as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Andrew P. Davison (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The reviewers all felt this was a potentially exciting advance for speeding up neuronal simulations.

2. Can the authors more clearly compare the accuracy of NEURON and ANN network simulations, especially as a function of the duration of simulation? Current injection comparisons would also be useful.

3. It would help to have more detail on how the approach would scale in network simulations, especially as the synaptic connectivity is increased, and more cell types are introduced.

4. The reviewers all would like to see better software documentation and tutorials for the various steps in model implementation.

5. The reviewers would like to see a clearer comparison between NEURON and the ANN on different architectures.

6. Can the authors include details on the process and computational resources required to train the ANN? One expects that this is extensively documented in the code repository, but there should be a good starting account of this in the body of the paper.

7. Can the authors place their work in a somewhat better context? The reviewers pointed out some prior work by Beniaguev et al., and would like to see more detail on how the method might handle some existing complex simulations.

Reviewer #1 (Recommendations for the authors):

1. The authors state that the code will be available upon publication. This precludes the ability of the reviewers to test the code, comment on its usability, and see how well it is documented. For a methods paper, this is a surprising omission and I cannot complete the review without full code availability. Ideally, this should be in an anonymous form such as uploaded to the Journal website or provided as a package for pip install.

2. Can the authors more completely document the (a) process and (b) the computational resources required for training the ANN? Ideally (a) should be packaged in a manner where the user gives the system a model specified in NEUROML or Neuron code, and it generates the ANN a few minutes later. Maybe the authors could even provide a web resource to do this. (b) is also important to know – do we need a supercomputer to train the ANN, even if it subsequently runs on a laptop? Can the authors properly benchmark this, just as they have benchmarked runtime resource requirements? For example, what does it take to train a multicompartmental model? How does it scale with the number of compartments and variety of ion channels?

Specific points

3. Figure 5 seems to show that the ANN does indeed have an internal representation of the input placement and its effect on somatic potential. It would be very useful to see if additional readouts could report dendritic potential and Ca levels. Is there a way to read out a couple of things that would be of great interest to people studying dendritic computation?

– The membrane potential at different points on the dendrites.

– The calcium levels at different points on the dendrites.

4. Can the authors provide a readout in terms of Ca fluorescent signals?

This is now one of the major ways of monitoring large numbers of neurons in vivo in networks.

5. Can the authors explain what changes in NEURON with initialization? This seems to be used as an optional step in the comparisons with the ANN neuronal mode.

Reviewer #2 (Recommendations for the authors):

My main comments are mostly driven by practical considerations. If one wants to use the method and the code, one would like to know the following.

– What happens if more synapses are added? For example, the L5 PC case is presented with 200 synapses. What if one needs to use 2,000 or 20,000 synapses, which is a more realistic scenario – will one need to re-train the ANN, or will it work out of the box?

– How does the model performance change with time beyond the NEURON-simulated period that ANN is trained on? I assume that after some time the voltage trace generated by the ANN will diverge from the NEURON-simulated one, especially with respect to the timing of APs. Can the authors show a figure where such divergence is characterized as a function of time? For example, if one trains the ANN for 1 second of a NEURON simulation, how well does the ANN simulation compare to the NEURON simulation at 5 seconds? How about 10 or 100 seconds?

– How well can the trained ANN mimic responses of the neuron to current injections? Current injections (e.g., with synaptic inputs blocked) are often used to probe intrinsic properties of neurons, and there's much data available from such experiments. These data provide a natural way for model builders to test how well their neuron models are working. Furthermore, realistic perturbations that one may want to model – such as optogenetic perturbations – can often be represented rather well as an injection of positive or negative current to a cell. Can the authors demonstrate that their ANN correctly reproduces a voltage response of a NEURON-simulated cell, for example, to a step current injection?

Additional comments:

– Figure 1 (and the rest of the manuscript): the variance explained for the "winning" ANN is ~50%, which doesn't sound high. However, the ANN trace looks very close to the NEURON trace. The authors may want to elaborate on the way the agreement is quantified as the variance is explained. Maybe it will help if they compute the variance explained for the voltage traces with APs clipped. Will the variance explained be much higher in that case? It might be worth reporting that along with the variance explained for the traces that include APs (as shown currently in Figure 1).

– Figure 5 – the variance explained, precision, and recall are only shown for L5 PC, but not for L2/3, L4, and L6 PC. The precision and recall for these cells are summarized in the text, combined for the 3 neurons. It would be important to show all 3 quantities individually for each neuron, just like they are shown here for the L5 PC.

– Figure 6 – As far as I can tell, these are not connected networks. Simulating 5,000 disconnected cells is very different from 5,000 highly interconnected cells, and the speed-ups can be drastically different. This is OK for the purposes of this manuscript, but the description should be clear about what's being done. The text mentions "network" everywhere in this section, including its title. The authors should change it and make it clear that simulations involve 50 or 5,000 disconnected cells. Or, if I got this wrong, and these are indeed simulations of connected networks with 50 or 5,000 cells, then please provide the description of the network connectivity, synaptic weights, etc. (In Methods, I only see the description of a 150-neuron network for Figures 7 and 8.)

– Figure 6 – also, the authors may want to say something here about the comparison of an ANN on GPU vs. NEURON on 1 CPU is not perfect. Ideally, one would run the ANN and NEURON simulations on the same parallel hardware and compare the performance as a function of the number of parallel cores used. I understand that is hard to achieve, so it is fair that the authors do not show such a comparison. However, it is instructive to consider the following thought experiment. Even if one ran the NEURON simulation of 5,000 cells on 5,000 CPUs, the performance would likely be about the same as that for one cell on one CPU. But even then, the time of the NEURON simulation would be ~185 s (for the L5 PC), whereas the time of the CNN simulation on a SINGLE GPU is ~12 s. So, the CNN is over 10 times more efficient on a single GPU than one expects NEURON to be on 5,000 CPUs.

– Simulations of the Rett syndrome model – it might be useful to give a little more detail about the network used for these simulations in the Results (otherwise one has to check Methods for all the details). The important piece to mention is that the network does not have any inhibitory cells, and instead, inhibition is provided as external inputs together with excitation. In other words, it is a feedforward inhibition model (if I understood it correctly).

– Figure 7c, parameter mapping – I assume the bar for NEURON is interpolation?

– Page 22, "which means that a complete cortical area can be simulated using only 17 ANNs" – I am not sure this is correct. The Billeh et al., model used about 100 distinct neuronal models belonging to 17 cell types. So, simulation of this model would require about 100 ANNs, rather than 17. Of course, this is still a huge improvement relative to the hundreds of thousands of neurons in the original NEURON model.

– Discussion – the authors almost do not mention the closely related work by Beniaguev et al., (Neuron, 2022), though they do cite that paper. I believe the work by Olah et al., is sufficiently different and novel, and it offers many interesting new insights as well as opportunities for computational neuroscientists who might want to use this method and code. I would suggest that the authors add a paragraph to the Discussion and describe how their work differs from Beniaguev et al., and what their unique contributions are.

– Data and software availability – the GitHub link doesn't work. I assume the authors plan to make it public upon paper publication. But it would be nice to provide the code to the reviewers, to get some idea about the completeness of the code, since it represents one of the main results of this paper. It is also important to mention that the code shared with the community should include the functions and procedures for training the ANNs. That is one of the most valuable contributions, which will be of great interest to many neuroscientists.

Reviewer #3 (Recommendations for the authors):

I think this study is very nice. As noted above in the Public Review, however, I think the manuscript would be greatly improved and its impact increased by (i) showing an accuracy comparison of the results obtained with NEURON and those obtained with the ANN network for the Rett syndrome circuit model, (ii) adding performance measures for the GeNN simulator, or some other simulator that is designed to run on GPUs, at least for the point neuron model.

The availability of the source code is very welcome. However, it is not well documented. The impact of this study would be increased by providing at least a README explaining the structure of the repository, and ideally by providing instructions for reproducing at least some of your results (e.g. generating the training data, training the ANNs, using the trained networks to generate predictions, etc.)

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Ultrafast Simulation of Large-Scale Neocortical Microcircuitry with Biophysically Realistic Neurons" for further consideration by eLife. Your revised article has been evaluated by Joshua Gold (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

The authors have substantially addressed most issues raised by the reviewers.

I would like to come back to several points in the revised version where more details in the text would greatly improve the accessibility of the study.

1. One of the key earlier reviewer points has to do with scaling with connected network size, especially with very large numbers of synapses. While the authors have responded, I was not able to understand this, and hence ask for a more complete explanation in the text so that it becomes more accessible to the readers.

The authors say:

"We thank the reviewers for pointing this out. This issue is now added to the discussion. Briefly, synaptic connectivity has no impact on simulation runtimes as the matrix transformations necessary for implementing connections take place regardless of whether two given cells are connected or not. On the other hand, inclusion of additional cell types linearly increases simulation times (assuming comparable cell numbers per cell type), as every cell type warrants the execution of additional artificial neural nets every time step."

Can the authors explain this matrix transformation step and its mapping to synaptic connectivity? I did not find an explanation in either the text or the responses to the reviewers. Possibly it may help if I were to reiterate the synaptic connectivity bottleneck in conventional simulations.

2. Each individual synaptic projection introduces a distinct delay in how long it takes for the source action potential to reach the postsynaptic synapse. This delay can be up to 10ms or sometimes longer depending on axon fiber type and length. 2. Each postsynaptic synapse is usually implemented as a conductance change obeying a single or dual α function of time. such as gSyn = gPeak * 1/tp * exp(1 -t/tp) where t is time since spike arrived at synapse and tp is time of peak of synaptic conductance.

The common observation in large spiking network models is that the combination of these calculations can lead to quite large demands, including in managing the event queues to implement the synaptic delays, since the delays may be long enough to permit multiple action potentials. The synaptic dynamics of the α functions also introduce a computational cost. Since the number of synaptic connections is very large, in some large simulations the computation time is dominated by synaptic transmission.

It would be helpful if the authors can respond by addressing a few specific points, and include the information in the text.

a. Confirm and elaborate on how their method indeed accomplishes the same computations as this, both the distinct synaptic delay for each synapse, and the equivalent of α function synapses.

b. Explain how their matrix transform addresses the two computational bottlenecks that occur with the conventional simulation approach,

c. The authors on the one hand state (line 594) "the number of contact sites directly correlates with simulation runtimes and memory consumption.", and on the other they say that synaptic connectivity has no impact on simulation runtimes. Please clarify what is different here.

3. Could the authors move some further details of the ANN training into the paper? For example, I did not see the time taken to train the ANN (~24 hours from the response to reviewers) stated in the paper. It would be very helpful for people trying to implement such networks to know what to expect in terms of training resources and time, not to mention the learning curve for the researchers themselves to figure out how to do the training.

A related point: the data availability statement explains how to access the generated models. I did not see a clear mention of the code and resources used to build the ANNs from the training set.

I understand we are still in the early days of the use of this method. It took several years after the development of the underlying matrix calculation code for neuronal calculations before there were a couple of standard simulators that helped with many things from standard libraries to graphical interfaces. Nevertheless, it would be very helpful if the authors could provide a more complete indication in the paper of what it would take for users to do such model building for themselves.
