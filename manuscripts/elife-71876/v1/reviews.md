# Peer review - Round 1

Editors:
- Caleb Kemere, https://ror.org/008zs3103 Rice University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71876.sa0](https://doi.org/10.7554/eLife.71876.sa0)

This work describes a new device for controlling the positioning of chronically-implanted movable electrodes in the brain. Potentially replacing microscrew-based devices with a cunningly-engineered electromechanical system, this highly accurate yet low-cost alternative could be an important milestone for systems neuroscientists currently using microdrives. While the design and demonstration of the system are solid and generated significant excitement, the limited demonstration of the robustness of the device in long term many electrode configurations was perhaps incomplete. On the whole, this promising study suggests that methodological advances may yet revolutionize neuroscience utilizing arrays of movable electrodes.


---

# Peer review - Round 1

Editors:
- Caleb Kemere, https://ror.org/008zs3103 Rice University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71876.sa1](https://doi.org/10.7554/eLife.71876.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for sending your article entitled "Robotic Multi-Probe-Single-Actuator Inchworm Neural Microdrive" for peer review at eLife. Your article is being evaluated by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation is being overseen by Laura Colgin as the Senior Editor.

There was consensus among the reviewers that three items seemed to have significant relevance to the potential impact of the work. First, there was concern that the mechanism for gripping the electrodes might damage them (potentially explaining the small number of chronic recording electrodes). Second, there was concern that the heating process might damage the brain due to induced currents or heat transfer. Third, there was concern that the very limited data on cross-talk in electrode motion might neglect important variability in this effect. Finally, as mentioned above, it is our general policy not to ask for significant new experiments. That said, given that the inch-worm drive would most likely find its primary use in chronic experiments, it was disappointing that there was so little chronic data (in terms of analysis and/or animals). This concern is secondary to the previously mentioned 3 items.

Please see the full reviews below:

Reviewer #1 (Recommendations for the authors):

Despite some efforts to find alternative approaches, most neuroscience experiments using chronically-implanted movable electrodes rely on screws with a pitch (travel distance for one complete turn) of 200-320 um. A careful experimentalist can probably adjust a screw in tenths of a turn, meaning that the minimal repeatable level of positional change is 20-30 um. Given that this is comparable to the size of the soma of a rodent neuron, precise positioning of electrodes is very challenging. While the advent of nanofabricated arrays of densely spaced electrodes (e.g., the Neuropixel) enables "electrical steering", dozens, if not hundreds of labs around the world still regularly rely on screw-based microdrives using an array of tetrodes or other small-channel-count electrodes.

This work presents a new concept for micropositioning electrodes in chronic neural recording. The "Inchworm Neural Microdrive" uses temperature-dependent phase change materials to grip electrodes at two locations along their axis. By releasing the gripper at the top or bottom, and using a piezo actuator to shift the separation between the grippers with high precision, an electrode can be slowly – but with 5 μm accuracy! – advanced. The authors do an excellent job of describing the manufacturing and characterization of their system for arraying grippers to form a multi-electrode microdrive. They also present preliminary data showing functionality in vivo in both an acute preparation and chronically implanted on a rat. As presented, it is a beautiful exposition of a potentially exciting new technology.

Full enthusiasm is diminished unfortunately by some concerns about usability. In particular, the grippers rely on heating elements in a printed circuit board. It appeared from the design that these formed a coil around the via that might create magnetic fields that would potentially induce currents in the electrodes that could be noisy (making it impossible to evaluate electrode movement using feedback) or even damage the brain tissue. Addressing this concern is probably vital for the future of this technology. There are secondary concerns that are probably less critical. First, one nice thing about a screw is that both rapid and slow advances are possible. In contrast, with the inchworm, it might be so slow to advance the electrodes that maintaining an awake animal quietly in an appropriate behavioral state might be challenging. Second, it was unclear from the preliminary data whether the grippers were damaging the electrodes by removing insulation.

There are 4 concerns outlined in the last paragraph that probably should be addressed. Thoughts about how these could (or could not) be addressed in existing data:

1) Does actuating an electrode induce a current in it or adjacent electrodes that causes damage?

Potential response – if you have histology of heated versus unheated electrodes, that might very easily address this. (The absence of a microlesion being the critical observation.) Of course, localizing electrodes *without* lesioning is challenging, so this may or may not be trivial.

2) Does actuating an electrode induce a current in it or adjacent electrodes that prohibits recording during advancement?

Potential response – if you have this data, please show it. And it's worth commenting about usability – maybe if it is too noisy, you could talk about how long it would take to move an array of electrodes from the corpus callosum to stratum pyramidale, and what fraction of time you would use for feedback versus movement. Also, if its not noisy during movement then there is almost certainly no lesioning current to worry about, I would think?

3) Is 9 μm per step so much slower as to be non usable?

Relatedly, we typically advance our electrodes 3-4 mm in a rat (from above the brain to CA1 or CA3) *after* implant. I know some labs will implant the drive with the electrodes already extended, but I suspect we are not unique. With screws, we typically go a few mm the first day and then more slowly. I think discussing what can be done in 20 minutes or an hour or some limited period, comparing screws and your system, would be ideal. Figure 6 could be easily extended to show how long the timeline *without gaps* is!

4) The single chronic animal had only 4 tetrodes of data.

I know that a new graduate student takes time to learn how to spin and load tetrodes without causing shorts or non-connected channels, but the significant reduction from 12 tetrodes worth of gripper space to 4 tetrodes raised the concern that perhaps 12 were loaded and only 4 worked because, e.g., the gripper damages them. Assuming this is *not* the case, some sort of information about electrode reliability over time or over multiple grip/release cycles would be valuable. Ideally there would be more than one chronically implanted animal, as this, finally, is the use case that the readers care about.

Reviewer #2 (Recommendations for the authors):

Smith et al. present a novel and potentially useful new design to improve neural microdrives by using a single electrical actuator to independently control multiple probes of various types. Broadly in neural recordings, electrodes of various types must be placed in a target location in the brain with micron precision. In standard microdrives, either one actuator moves a group of coupled electrodes or each electrode has its own actuator. Both approaches have significant disadvantages. If all electrodes are coupled, the experimenter is severely limited in how they adjust each, leading to some electrodes ending up off-target. If each electrode has an actuator, this adds significant weight and complexity to the drive. In both cases, electrodes are typically moved manually, a laborious process that can stress the animal and lead to microdrive damage because of the many fragile components involved. The authors inchworm approach uses a single piezo to move multiple electrodes by selectively releasing each electrode via heating of a phase-change material that holds the top and bottom of the electrode. The authors characterize the range, accuracy, and independence of electrode movement with this device. They show this approach generalizes to glass electrodes. They also demonstrate successful tetrode recordings from a 16-tetrode acute experiment and a 4-tetrode chronic experiment. Overall, this approach is potentially useful to many using microdrives. Some clarifying questions remain about how generalizable and readily adoptable this approach is and if the resulting recordings are high quality, high yield, and stable.

Overall I found the approach novel and potentially impactful with careful characterization of the device.

– Does this approach generalize to silicone probes, as these are also widely used in the field, especially with the adoption of neuropixels and probes with integrated optical fibers or LEDs? These could fail in this design because they are very brittle and breakable and/or because they have large adapters that would interfere with each other. Even if the authors do not build and test a silicone probe drive, if they could work out whether this is feasible based on their knowledge of the device and typical probes that would go a long way to demonstrating even broader utility and generalizability.

– How readily buildable is the device and readily available are the materials for a typical lab? Is this something a lab would have to buy or build? If long does building take for a novice or expert?

– Brain heating can cause damage at high levels or alter neural activity at low levels. How much heat does the implant generate at the brain surface or at the animal's head, especially when moving many electrodes long distances? Do the electrodes get heated and if so how might that effect their function? Would a cooling system or limits on how long the actuator can run at a time be required?

– The authors carefully characterize accuracy and reliability of forward motion but little is discussed about lateral motion of the electrode while moving. Lateral motion can damage cells and cause inflammation. What is the typical lateral motion of the electrode that is moved?

– The authors demonstrate their inchwork Microdrive in acute and chronic tetrode recordings. Electrophysiologists will want to see as much detail as possible on these recordings to be convinced to adopt this approach. What is the typical cell yield per tetrode and cluster quality using this approach? How stable are the recordings, eg how long is a single cell cluterable? Please show more zoomed in (on x axis) images of recording traces in Figure 6c. Please show single waveforms and clusters in Figure 7d.

– The authors state the 4 tetrode microdrive weighed 4.5 g. How does that compare to a standard 4 tetrode Microdrive? How much does the inchworm actuator add in weight to any standard Microdrive? Weight is especially important for the potential to use this approach in mice, where microdrives must be much lighter than for rats.

– How robust is the system, especially in a chronic implant where the animal may bang the implant often? What are potential failure points and are they fixable in an implanted animal?

Reviewer #3 (Recommendations for the authors):

In the current manuscript, Smith et al. describe a system to remotely control the advancement of wires or similarly shaped materials into the brain for in vivo recording. The system combines a single piezo actuator with phase change material on two separate boards to allow multiple wires to be independently controlled via a single actuator, reducing the overall weight of the implant. The system is quite clever and, to my knowledge, novel.

I am very enthusiastic regarding this technology, as I believe it will meaningfully advance tetrode recording quality. Although many labs in the field have moved to silicon probe technology, there are many advantages of tetrodes, which the authors mention in the manuscript. If this method is relatively easy to implement or can be packaged as a purchasable product, I foresee broad adoption of this technology.

The manuscript itself is well-written and the logic and manufacturing process was easy to follow.

I only have a few requests for the authors:

First, I would like to see the repeatability, accuracy, and cross-talk tests repeated on multiple tetrodes. My understanding from the text and the data in Figure 4 is that these values were tested on only a single tetrode (or two tetrodes for the cross-talk test). Specifically, I would like to know whether the inevitable variability in the manufacturing process (different amounts of PCM, differences in the heat coil construction, etc.) contributes to changes in repeatability/accuracy/cross-talk. Basically, I would like the data in Figure 4 to have an N greater than 1 (N=3 would be fine).

Second, I would like some discussion regarding the reusability of the boards. Can a tetrode that has been in the brain (and is now at least partially covered in CSF and blood) be pulled back through the PCM so that the board and PCM can be reused? Does the PCM need to be completely cleaned from the board for the next implant construction? If so, are there methods to do this?

Third, can the authors comment on what they think is a practical limit on the diameter of a cylindrical object that can be moved via this technology? It seems that at a certain size, a cylinder would require so much PCM that it might not be able to all be melted quickly enough. Can this method be used to move 200 um-diameter optic fibers? 400 um-diameter? I'm not asking the authors to rigorously test these different sizes, but rather to give some general guidance based on their experience/knowledge.
