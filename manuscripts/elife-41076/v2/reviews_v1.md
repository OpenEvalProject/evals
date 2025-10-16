# Peer review - Round 1

Editors:
- Leon Glass, McGill University Canada
- Arup K Chakraborty, Massachusetts Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.41076.017](https://doi.org/10.7554/eLife.41076.017)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: this article was originally rejected, but the authors appealed and revised for further consideration.]

Thank you for submitting your work entitled "Optogenetics enables real-time spatiotemporal control over spiral wave dynamics in an excitable cardiac system" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Gil Bub (Reviewer #2).

Our decision has been reached after consultation between the reviewers, the Reviewing Editor, and the Senior Editor. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

The work shows the ability to move spirals waves of cardiac activity in tissue culture using optogenetic methods to hyperpolarize and modify excitability in localized regions of the culture. The optogenetic techniques were used by the same group in earlier papers to terminate spiral waves. However, this specific technique to move the core location of spiral wave rotation in cardiac tissue had not been used previously. Motion of the spiral to the boundary of a region is a novel finding. The experimental work is accompanied by simulations that show similar behaviors to the experiments. These results do appear to be valid, but they could have been expected based on earlier work in this field by this group and others.

The paper also did not provide adequate citation to other work dealing with control of spirals in excitable medium, and did not develop ways in which the work could be implemented in vivo to help control arrhythmia in people.

After a good deal of back and forth, and consultation with an eLife Senior Editor concerning eLife editorial policies, the consensus opinion is that this is not sufficiently novel to merit publication in eLife.

Reviewer #1:

The authors use patterned optogenetic stimulation to drag spiral wave cores in cultured monolayers of cardiomyocytes. They call the protocol the "Attract-Anchor-Drag" (AAD) technique. The authors combine experiments with extensive numerical simulations of a conductance-based cardiac model. They explore the conditions under which the spiral core follows the optical stimulus, by varying (in silico) the radius, duty cycle, and timing of the illumination pulses relative to the rotor circulation. They show that spiral waves can be suppressed either by mutual annihilation of two counter-rotating waves or by dragging a wave to an inexcitable boundary.

Technical merits:

From a technical perspective, this work is a modest variation on several other published works on optogenetic control of excitable cells. The authors cite their own prior work (Feola et al., 2017), but not with sufficient prominence to make clear that the entire technical setup has already been published. The authors neglect to cite several other closely related works:

From the authors' group:

Bingen et al., 2014.

From other groups:

Burton et al., 2015.

Entcheva and Bub, 2016.

The authors cite a work by Zhang et al. on optical electrophysiology in HEK cells, but that paper did not have any spatial control. A more appropriate citation would be:

McNamara et al., 2016.

Scientific merits:

The scientific justification for the study is the experimental demonstration that spiral waves can be manipulated by dragging an inexcitable core. The authors portray this as an important discovery, but in truth the degree of surprise here is limited: given that a spiral wave can anchor at an inexcitable defect, one should not be surprised that gradual motion of the defect will drag the spiral wave.

While the authors are to be commended for exploring (in silico) the impact of the size, timing, and motion parameters of the spot on the spiral wave motion (Figure 3), all results are reported in physical units, giving little insight into how these parameters might change in a different system, e.g. real cardiac tissue where conduction velocity and gap junction coupling are very different from in vitro. It is not clear what generalizable insights can be gained from these results.

The other experimental results demonstrate that spiral waves can be annihilated by dragging to the boundary of a dish (Figure 2), or by coalescing two counter-propagating waves (Figure 4). These results are interesting, but also not particularly surprising and of uncertain relevance to treatment of spiral wave defects in vivo.

Overall, the experimental work and analysis seems thin and anecdotal, comprising video stills from three videos (Figures 1, 2, 4). It is disappointing that the simulations in Figure 5 are not accompanied by experiments.

The broader scientific justification is a general statement that these techniques "could have significant meaning in terms of a better mechanistic understanding of cardiac arrhythmias and improvement of existing and development of new treatment modalities." (stated again at the end of the Introduction and Discussion). While it is generally true that optical control of cardiac dynamics is an interesting topic, these statements seem to be insufficiently justified by the present work. It is not clear how one would apply the learning from the present experiments to work in vivo or to improved therapies.

Previous work from the senior authors showed that widefield optogenetic stimulation could eliminate spiral wave patterns (Bingen et al., 2014). If the authors want to emphasize the utility of their new approach for spiral wave abolition, they should discuss the relative advantages or limitations of these two strategies. Moreover, many examples of AAD spiral wave elimination described here rely on colliding the spiral core with a boundary. It is not obvious how such a strategy would be implemented in vivo.

The simulation work in Figure 4 (Video 4) is beginning to approach interesting questions, e.g. under what circumstances does combining two spirals lead to multiarm spirals vs. elimination? If brought together and released, how do rotors interact with each other? How does this interaction depend on phase offset, direction of circulation, and number of arms? A more thorough experimental exploration of these questions would considerably improve the overall scholarship and impact of the work.

Reviewer #2:

The article by Majumder et al. demonstrate a novel control method for steering spiral waves in a biological excitable medium. The experiments and theory are convincing.

My only major concern is that the authors may have misstated the impact of previous studies. The authors state in their final paragraph:

"Previous studies also demonstrated alternative methods to 'control' spiral-wave dynamics in excitable media, for example,… However, the principal limitation of these methods is that they are indirect, giving reasonable control over the initial and final states of the system, with little or no control in between."

I don't agree with this statement. First, the submitted work does not show a higher degree of control than other published studies as the authors apply a perturbation and observe the results as opposed to using closed loop feedback control. The authors may mean that previous control systems rely on delivering timed pulses which fall in defined phases of the spiral wave (but I don't see why this indicates a lack of control of the system). Also, there are un-referenced published examples of feedback control of spiral wave motion (e.g. Schlesner et al., 2008; Sakurai et al., 2002) that show very precise spiral wave control. In addition, the general idea of anchoring a spiral with light has been demonstrated in an experimental system which would require relatively small modification to show spiral wave steering (Steinbock and Muller, 1993).

The figures should be clarified. For example, in Figure 2, panels are shown without indicating the precise timing (i.e. B1, B2, B3 etc.), which would help readers understand the observed dynamics. Also, exactly how the spiral translates linearly is unclear from the figure, as the speed of the moving spot is unknown. It would be helpful to note the speed of the spot relative to the speed of wave propagation.
