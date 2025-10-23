# Peer review - Round 1

Editors:
- Ronald L Calabrese, Emory University United States

Reviewers:
- Robert M Brownstone, University College London United Kingdom

## Review text

DOI: [10.7554/eLife.43587.013](https://doi.org/10.7554/eLife.43587.013)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Computational modeling of brainstem circuits controlling locomotor frequency and gait" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Ronald L Calabrese as the Reviewing Editor and Reviewer #1. The following individuals involved in review of your submission have also agreed to reveal their identity: Robert M Brownstone (Reviewer #2); Maxim Bazhenov (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript advance, the authors extend their previous model of the spinal circuitry underlying locomotor rhythm generation, and speed and gait control in mice that is based on physiological, behavioral, and genetic studies of identified neuron classes in spinal cord. Here they propose a connectome of the brainstem-spinal circuitry and suggest a mechanistic explanation of the operation of brainstem structures (CnF and PPN of the MLR and downstream LPGi of the caudal RF) and their roles in controlling speed and gait. Their model predicts that brainstem control of locomotion is mediated by two pathways, one controlling locomotor speed via connections to rhythm generating circuits in the spinal cord and the other providing gait control by targeting commissural and long propriospinal interneurons. Specifically they predict that the projections from the PPN target only LPGi-Glu-1 populations (responsible for control of locomotor frequency, but not gait), whereas the projections from the CnF affect both LPGi populations (LPGi-Glu-1 and LPGi-Glu-2) and hence can control locomotor speed and provide speed-dependent control of locomotor gait. This advance should arouse interest in the community studying the neural control of locomotion.

Essential revisions:

1) With respect to the CnF/PPN: the authors are basing their studies mainly on the paper out of the Kiehn lab, while they mention the work from the Bretzner lab. I think the strength of the computational work is the strong support it has from the 2 labs, and the authors could stress this throughout – from the Introduction through the Discussion. That is, there is strong evidence about the roles of these nuclei (the study of which go back decades in many labs). In contrast, the data supporting the LPGi are not as strong, and the authors have relied on a single study that has minimal support, with most previous studies pointing towards the GRN proper as being critical for locomotion (eg Noga, Mori labs). In my view, the specific location(s) of reticulospinal neurons for locomotion thus remains an open question. Having said that, I don't think this detracts from the computational study which does not rely on the specific locations of the neurons. In fact, this study predicts 2 different types of descending systems – must they both be in LPGi? Perhaps one reason for the discrepancies in the literature is that both LPGi and GRN are involved and are home to these different descending families of neurons? I think it could be useful if the authors explored this. (Also, statements like "pivotal role of LPGi" cannot be supported by this study for the same reason.)

2) Where is the dIni population located, and is there evidence to support this prediction?

3) Section on PPN inactivation, second paragraph of subsection “Frequency-dependent gait expression and the effects of PPN inactivation” – I found it very difficult to follow the logic here – which centres on what happens if you don't activate the Glu-1 population. Perhaps it would be clearer to state what happens when you do activate it? I am having trouble relating this to gait transition.

4) As the known connectome of the spinal cord and brainstem expands, one wonders if this process of expanding the model can continue without the models becoming so complicated and contain so many unknown connection weights that they are no longer heuristic. This unfortunate side effect of the process of model building for complicated networks has not overwhelmed the message and insights of this paper but future models building on this one may suffer that fate. Can the authors discuss this potential limitation of their approach?
