# Peer review - Round 1

Editors:
- Jan-Marino Ramirez, Seattle Children's Research Institute and University of Washington , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.27342.023](https://doi.org/10.7554/eLife.27342.023)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A spiral attractor network drives rhythmic locomotion" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom, Jan-Marino Ramirez (Reviewer #1), is a member of our Board of Reviewing Editors and the evaluation has been overseen by Eve Marder as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Rune W Berg (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors explore the population dynamics that controls fictive locomotion in the pedal ganglion network of Aplysia. The locomotor activity is a relatively simple escape response, which is elicited by a brief electrical stimulation to the tail nerve. The use of fast voltage sensitive dyes and optical imaging allows the authors to gain insights into the activity of individual neurons, while simultaneously recording the activity from 120-180 neurons, which represents approximately 10% of the entire ganglion population. This unique preparation is ideal to address fundamental questions in neuronal networks. In particular the question of how populations of neurons control behavior is difficult to address in larger networks, such as those of the mammalian nervous system.

The authors find that the population dynamics can best be described as an attractor dynamics (spiral attractor) with a low dimension, whereas the higher dimensional activity is variable from trial to trial as well as from animal to animal and therefore not attributed the same importance in the generation of the motor pattern. Interestingly, the authors found that the individual participation in the dynamics could change substantially from bout to bout, while the population dynamics was more stable. This is consistent with the property of mammalian networks in which single neurons show also large variability, while the output is rather regular (see e.g. Carroll and Ramirez, 2013).

There are several other important and interesting findings in this study. This small network investigation is simple enough to restrict the unknown variables yet rich enough to address interesting questions of neuronal network behind motor behavior. It is truly a rare and noteworthy study and the authors go through great efforts to analyze and interpret the complexity that even such a simple animal has. The paper is well written, but it would help to try to further simplify the language and better explain the terms used. The study is innovative as the authors provide tools for analysis, in particular the recurrence analysis. Thus, this study will undoubtedly inspire future investigation in attractor dynamics of neuronal networks.

Essential revisions:

1) The study is well written, but it needs to be adjusted to a more general readership. The method is innovative, but it needs to be better explained, in particular for a reader who is not familiar with the terminology used in this study. The authors should provide e.g. a better explanation in the text how eigenvalues for the population recordings were calculated.

2) We would be interested to hear some of your answers to the questions raised below. The authors could consider addressing these questions in the Discussion section, since the general readership might arrive at similar questions. But, we won't insist that the authors include each of the following issues in the text.

2a) Please comment: There seems to be only one attractor in the state space – or two if you count the spontaneous state, which seems rather trivial, as an attractor. Although this arrangement would provide robustness to the system and prevent unintended pathological activities, it seems to be contrary to the general notion of neuronal networks having multiple stable states – e.g. the classical Hopfield memory networks. Further, it was documented in an early report that (even) the neuronal network in the Aplysia abdominal ganglion could participate in at least 3 different behaviors, see

J-Y Wu, LB Cohen, CX Falk, "Neuronal activity during different behaviors in Aplysia: a distributed organization?" Science 263, 820-823, 1994

Is the pedal ganglion network not able to perform more motor behaviors or is it not possible to induce other behaviors experimentally? I know the authors make great effort to map the basin of attraction, but can you comment more on this issue of lack of multi-stability?

2b) Please comment: What is the role of the rest of the population in bringing back the dynamics to the attractor? I don't fully see to what extent the perturbation affects all the neurons, or only some. Could it be that the response to the perturbation (Figure 1F) and the decay back to the attractor is really the alignment of the recorded/perturbed neurons with the rest of the unperturbed population?

2c) Please comment: Discussion and other places: "Testing the idea that high-dimensional population activity contains a low-dimensional signal […]" How would the activity look if it were a high dimensional activity without a low dimensional signal, i.e. the contrary situation? Would it just be random chaotic spiking? Would it even be possible to have a rhythmic low dimensional motor output without having that same low-dimensional component in the neuronal population?

2d) Emergence. The authors discuss in a couple of places the interesting and profound issue:

"These results suggest that the pedal ganglion's pattern generator is not driven by neurons that are endogenous oscillators, as they would be expected to participate equally in every response. Rather, this variation supports the hypothesis that the periodic activity is an emergent property of the network. "

However, in their model the network oscillation frequency is set by the membrane time constant of the single neuron. This seems at odds with the notion that the rhythm is an emergent network phenomenon. Usually "emergence" is a property that cannot be identified on the single cell level. And if so, why is the network oscillation so robust and independent on the participation of individual neuron? Is the network oscillation frequency some sort of weighted average of the time constants of different cells? This is a very important issue and has caused considerable discussion e.g. in the field of mammalian respiration, and thus, it would be great to include your considerations in the discussion. We will further elaborate on your conclusion with regards to the emergent property below.

3) The authors use recurrence analysis, which is adapted from the analysis of dynamical systems, and they provide some evidence that population activity in the pedal ganglion fulfills some criteria of attractor dynamics: A) the cyclical periodic orbit is rapidly reached from a more diverse state during the initial stimulation. B) After spontaneous perturbations, the system recovers rapidly returning to the manifold. Moreover, C) they show that across the entire recorded neuronal population, individual neurons can change in the weight by which they contribute to the low dimensional state. Based on C), they conclude that the low dimensional dynamical system is an emergent property of the neuronal population and more robust / reproducible than the high dimensional neuronal population activity; in conclusion, a stable motor output is produced besides the variability seen in individual neurons.

The use of recurrence analysis for single cell resolution neuronal population data is innovative. While this manuscript will be interesting to a large community of neuroscientists, the manuscript needs some clarifications. Most importantly, C) is a very strong statement that really would change views of how population dynamics in the pedal ganglion work; however, C) is not sufficiently supported by the analysis provided and thus could be misleading. Additional analyses should be done to either revise or solidify this conclusion.

4) Along these lines: there might be an oscillatory sub-population of neurons, or even smaller CPG unit, that generates in a very robust and reproducible manner a recurrent and periodic pattern; this view is already somewhat supported in Figure 8. In addition, other pedal ganglion neurons contribute to a more complex overall population state by exhibiting more variable activity patterns, that might be transiently recruited to this recurrently active subpopulation. If this is the case, the main statement (C) does not hold and should be revised.

5) If the dataset in Figure 1C is representative, it is obvious that PCA will lead to at least two modes that describe a dominant periodic orbit. The authors should provide more direct quantification of what type of neurons have the most variable contributions and in which way. In their previous work, the authors devised a method to classify neuronal subpopulations as non-oscillators, oscillators, bursters, pausers (Bruno et al., 2015); see also Figure 1C. First, the authors should perform their analyses on these subpopulations separately; one might expect that the oscillatory neurons show much less variable contributions and that the variability comes from the other neuronal classes. Or is there even a very small set of highly non-variable neurons? In this case, one could argue that recurrence, periodicity and stable motor output generation is not an emergent property of the pedal ganglion but the robust output of a smaller subpopulation / CPG subunit.

6) PCA results, especially in the higher dimensions can be quite variable from dataset to dataset, or even within datasets, when performed on subsections. The authors use the eigenvectors to measure each neuron's contribution to the low dimensional signal. However, as they also state, this variability can come from variable signal amplitudes or variable synchrony. If signal amplitude is the main source of variability, I would argue that the main periodic (or recurrent) feature of these neurons is robust and preserved throughout the 3 programs in each recording; it just appears variable in the eigenvectors. So, the authors should show that the main source of variability is indeed variable synchrony.

7) An essential aspect of recurrence analysis described in Marwan et al., 2007 is the addition of time delay dimension to the data; here recurrent points are similar not only in their instantaneous distances but also in their time history. This step is not mentioned in the manuscript. Please provide an explanation why this was not needed for the analysis of their data.

8) Detailed information is lacking about how many PC dimensions were used in each analysis and dataset. Were always the top 4 dimensions used as described for Figure 2D, or always as many dimensions that explain 80% of variance? Was this the same for all analyses throughout the paper? This choice makes a difference in how to interpret the data. Please provide this detailed information.

9) Please discuss what the function of variability might be. For example, is the size principle described for the Aplyisa motor system, i.e. do variable recruitment patterns are functional for different loads on the motor apparatus? Etc.
