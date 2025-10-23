# Peer review - Round 1

Editors:
- Claire Wyart, Hôpital Pitié-Salpêtrière, Sorbonne Universités, UPMC Univ Paris 06, Inserm, CNRS France

Reviewers:
- Claire Wyart, Hôpital Pitié-Salpêtrière, Sorbonne Universités, UPMC Univ Paris 06, Inserm, CNRS France
- Marco Beato, University College London United Kingdom

## Review text

DOI: [10.7554/eLife.47837.027](https://doi.org/10.7554/eLife.47837.027)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Spinal V2b neurons reveal a role for ipsilateral inhibition in speed control" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Claire Wyart as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Ronald Calabrese as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Marco Beato (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Callahan et al. present evidence that in the zebrafish larval spinal cord spinal V2b inhibitory interneurons control locomotor speed. This is a very exciting finding as V2b are ipsilateral, descending, and inhibitory interneurons. This finding, along with the recent publication on V1 neurons involved in enhancing speed (Kimura and Higashijima, 2019), provide more evidence that speed control is distributed across many interneurons in the spinal cord and not only restricted to excitatory interneurons.

Their approach relies on novel BAC transgenic lines where gata3 drives the expression in V2b neurons, together with cerebrospinal fluid-contacting neurons (CSF-cNs, ipsilateral ascending neurons originating from p3 and pMN). However, since in contrast, CSF-cNs innately increase locomotor speed during the escape (Bohm et al., 2016), the increase in locomotor speed observed when suppressing activity of V2b and CSF-cNs together should be due to V2b intrinsically reducing locomotor speed.

Furthermore, the manuscript provides proof of anatomical segregation of the axons of two distinct classes of V2b interneurons, one purely glycinergic and one with mixed GABAergic-Glycinergic phenotype and indicates some novel rules of connectivity, with fast MNs receiving mostly glycinergic inhibition and slow motoneurons receiving mixed inhibitory input. Optogenetic silencing of both classes of V2b neurons results in increased tail beat frequency, leading to the hypothesis that V2b neurons might have a role in controlling locomotor speed. The methodology is sound, all results are clearly represented and the major findings are fully supported by the data. While a role of V2b interneurons in controlling the speed might not come as a complete surprise, the authors give a first functional proof of direct connectivity of V2b and motoneurons, as well as (rather more surprisingly) of connectivity between V2b interneurons themselves.

As raised by two of the reviewers, the ultimate goal would be to be able to activate/silence the two classes of V2b separately, as well as establishing their rules of connectivity between themselves. Such experiments would require complex intersectional genetics, which would take time and therefore would be better suited for a separate study.

V2b interneurons appear to act as a break on the central pattern generator (CPG), but it is not clear how they do so. In order to specify the underlying mechanisms, it would be interesting to add to this study two experiments that should be doable in two months:

1) Optogenetic activation of V2b using an excitatory opsin in the Tg(gata3:gal4) line during locomotion to test whether it would slow down locomotion:

While the authors show the neat result of increased tail beat frequency upon silencing of V2b interneurons, they do not show what happens when such interneurons are activated during tail beat. This would be a relatively simple experiment to perform and would add some information on the potential function of V2b interneurons.

2) Recordings of MNs in V-Clamp and C-Clamp with optogenetic control of V2b to elicit single spike in order to resolve the properties of the V2b-MN synapses and test how gaba+ versus gaba- V2b firing impact the firing of slow versus fast MNs:

By increasing the selectivity of the light stimulation to single neuron/single spike (using short pulses of 5ms instead of 20-50ms as previously done), the authors could calibrate the light to get 'unitary' responses in motoneurons, evoke firing in motoneurons (by current injection) and see how activation of one or a group of V2b would alter the firing. Following that, the authors could verify whether the input is mixed or purely glycinergic (and onto fast or slow motoneurons). This should be quite elegant, informative and not too complicated.

With these two experiments added, this study should lay solid basis for future studies aimed at understanding how the differential connectivity onto fast and slow motoneurons of mixed and pure glycinergic V2b interneurons might affect the function of the locomotor network. The finding of a recurrent disinhibitory loop between V2bs raises interesting possibility of complex interactions and modulations within the premotor network.

Specific comments:

1) All V2b are glycinergic but some are also GABAergic – overall slightly more ventral with more ventral projections. This mixed neurotransmitter release should slow down IPSCs on their targets. Accordingly, there is a correlate with the projection from V2b onto slow and fast types of MNs. How does the fast glycinergic inhibition impact the firing of fast motoneurons? and reciprocally the slow GABAergic inhibition the firing of slow motoneurons? By doing so, can the authors speculate on how these ipsilateral ascending neurons can slow down the rhythm?

2) Summary:

Specify more how V2b project onto different motoneuron (MN) types ("differential targeting to slower and faster circuits"). It would be nice to go further by presenting how the projections and neurotransmitter types together with circuit disinhibition can enable the modulation of speed observed.

3) Figure 1B: What are the ventral-most cells in this panel (2-3 per segment)? They appear in the V3 domain but do not look like CSF-cNs on the image, could V3 or V2c interneurons also be in the line?

4) Filled cells in Figure 4 refer to segments 14-18. However, according to the data in Figure 1E, those are among the shortest axon (shorter that the 10-11 group), so I am wondering whether the same neat dorsoventral separation is also seen in higher level segments, especially for the V2b with longest axons (segments 10-11, judging from Figure 1E).

5) Figure 4, use same Y-scale for F,G and H.

6) Please report concentrations of strychnine and gabazine. None of the two drugs is selective. While there is no doubt on the qualitative results of Figure 5, knowing the concentrations would allow to judge them quantitatively. Also, how was the extent of block measured? The text reports conductances, so I would assume that the peak was measured. However, since the responses in Figure 5 and 6 originate from multiple spikes in multiple pre-synaptic neurons, the integral of the trace might be more appropriate.

7) Figure 7: Light activation seems to depolarize the cell (opposite to what shown in Figure 6—figure supplement 2). It is highly possible that chloride gradients vary among cells and that minor change in resting potential could change the effect. Is the difference observed between Figure 7 and Figure 6—figure supplement 2 coming from different resting potentials in the two cells shown? In both cases the increased anion conductance causes a large shunt, so there is no doubt about the silencing of neurons. Still, it would be better to have a label with the resting membrane potential.

8) The spikes represented in Figures 6E and 7B are rather small (10-15 mV amplitude). Overall, it seems that action potentials in V2b interneurons do not have a classical shape, while AP in CSF-cN neurons recorded in the same conditions do (Figure 7 and Figure 6—figure supplement 2). Are these representative recordings? Is it a specific feature of these neurons? Can you comment on that?

9) Introduction, paragraph two: the statement that premotor neurons only belong to five superclasses is not 100% correct. Of the 10 subfamily, at least Di3 have been shown to contact motoneurons (Bui et al., 2013).

10) Consider moving the 'in situ hybridization' section, table and figure to the Materials and methods or supplementary information. It is a necessary control, but interrupts the flow of information while reading the paper.

11) Results, second paragraph, and Figure 1: I was wondering whether illustrating the position of the soma of V2b interneurons with a coronal view would be more readable. Indeed, I found the use of false color depth-coded image in panel B difficult to read. Is the red background corresponding to the other half of the spinal cord? Because the color scale states L to R (supposedly left to right), while in the text it is written from medial to lateral. Showing a projection for a full segment for example on a coronal slice would help the reader.

12) Subsection “Neurotransmitter expression defines subpopulations of V2b neurons”: would it be possible to provide data showing the expression of both GABA and glycine in the same neuron? Are purely GABAergic neurons existing? What is the functional consequences of having a co-release of GABA and glycine?

13) Figure 7: the panel E is not easy to read and as such does not provide any obvious info. Is this panel really necessary?

14) Please correct the opening sentence in subsection “V2b axons extend throughout the spinal cord” (probably a mix between two version of the same sentence).

15) Paragraph three subsection “Neurotransmitter expression defines subpopulations of V2b neurons”: please correct sunclasses

16) Subsection “Axonal morphology varies by subpopulation identity”: please define VeLD (this is done in the Discussion but not here)

17) Figure 6—figure supplement 2: panel A the time scale on top might be wrong as the stim duration is 20ms while the scale indicates 0.4 sec?
