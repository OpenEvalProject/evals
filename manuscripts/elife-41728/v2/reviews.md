# Peer review - Round 1

Editors:
- Inna Slutsky, Tel Aviv University Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.41728.030](https://doi.org/10.7554/eLife.41728.030)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Neuronal morphologies built for compact computing in a rhythmic motor circuit" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Ronald Calabrese as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Gilles Laurent (Reviewer #1).

Summary:

This nice paper is the continuation of a series of studies from the Marder lab investigating the functional consequences of STG neuron morphology in the passive regime. The authors combine an exploration of parameter space by compartmental modeling with experimental tests, contrasting dendritic integration in neurites with large taper (as in STG neurons) with integration in dendrites with low taper (as is typical of cortical neurons, often used as "typical" or representative examples). The basic claim is that the geometry of the dendrites in this system makes the neurons act virtually as a single compartment even though they have a very elaborate dendritic structure. The authors claim that this is a result of substantial tapering of the dendrites and conduct compartmental simulations to support their conclusion. The paper is well written and the experimental sample size impressive. It seems to do a good job in considering and testing different cases with simulation and matching experimental data to simulations which is the gold standard in this type of studies. Nevertheless, we ask the authors to address several concerns, as listed below, to strengthen the conclusions of this work.

Essential revisions:

1) Reading the manuscript gives the feeling a negative result (synaptic inputs seem to be location independent) is turned into a feature. However, there may be methodological reasons why location dependence of some features is found to be weak (see below) and even if it is true, it does not justify consideration as a special mechanism. There are many neurons even in mammalian CNS where apparently there is not much dendritic integration (e.g. cerebellar granular cells).

2) Figure 1 – the authors perform many simulations to test the effect of change in diameter on voltage attenuation along the dendrites. They make the point that geometry can affect attenuation along the dendrites even when all other parameters are kept the same.

a) While the results are presented as a surprise, the understanding that dendritic geometry affects voltage attenuation is at the heart of cable theory and is present already in Rall's 59 paper.

b) In addition, the specific case of tapering is analytically covered in the papers of Schierwagen (admittedly very difficult to read): Schierwagen, A.K., A non-uniform equivalent cable model of membrane voltage changes in a passive dendritic tree, J. Theor. Biol. (1989) 141, 159-179, which is not even cited.

c) The simulated case assumes sealed end boundary condition at both sides of the cable, while in fact the relevant case is that there is a large "load" (e.g. killed end boundary condition) on the side with large diameter, because the rest of the dendritic tree is connected to that part. This might have a significant effect on the conclusions.

d) The authors have both the experimental data of the geometry of the neurons (which they studied in detail in the first paper) and the physiological properties (allowing them to extract the biophysical properties of the membrane). They could simulate the specific neuron they record from, rather than choose to simulate simplified models, which might fail to capture the intricate properties of the real geometry.

3) The authors use sharp electrode recordings and in fact two of them at the soma, which indeed makes the current clamp better. However, it is accepted that sharp electrode recordings may fundamentally change the estimate of membrane parameters and may create a significant conductance leak in the recording location. On top of that, most of the relevant integration happens near the location of synaptic inputs and far away from the recording site. So, it is difficult to escape the alternative explanation in which all the input looks similar at the recording point because they all very far from it, especially when the inputs are very slow (0.5 s rise time, voltage attenuation is far smaller for steady state inputs as compared to transients, and here the inputs are so slow that they are virtually steady state).

4) The authors find a fit for the data with effective space constant of order of magnitude of 1mm with total dendritic length of > 10mm. This means that there are certainly points that are quite far from each other, and still they claim that the neuron acts as a single compartment.

5) The measurements of Erev in their hands shows almost no sensitivity to dendritic location of the activation. This together with simulation that shows that under certain condition (short space constant) Erev estimation should be sensitive to location is taken as an indication that the space constant is long. However, for this the authors are only using very simplified models, which we suspect are very different in terms of boundary conditions than their experimental setup (see above).

6) The individual responses presented in Figure 5—Figure supplements 1, 2 and especially 3, seem to have different shape indices (i.e. rise time and decay time, consistent with classical cable theory of inputs arriving from different locations along the dendrites) and inconsistent with a single compartment scenario.
