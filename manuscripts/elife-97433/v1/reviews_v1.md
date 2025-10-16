# Peer review - Round 1

Editors:
- Caleb Kemere, Rice University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.97433.3.sa0](https://doi.org/10.7554/eLife.97433.3.sa0)

Bowler et al. present a software/hardware system for behavioral control of navigation-based virtual reality experiments, particularly suited for pairing with 2-photon imaging but applicable to a variety of techniques. This system represents a valuable contribution to the field of behavioral and systems neuroscience, as it provides a standardized, easy to implement, and flexible system that could be adopted across multiple laboratories. The authors provide compelling evidence of the functionality of their system by reporting benchmark tests and demonstrating hippocampal activity patterns consistent with standards in the field. This work will be of interest to systems neuroscientists looking to integrate flexible head-fixed behavioral control with neural data acquisition.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97433.3.sa1](https://doi.org/10.7554/eLife.97433.3.sa1)

Summary:

Bowler et al. present a thoroughly tested system for modularized behavioral control of navigation-based experiments, particularly suited for pairing with 2-photon imaging but applicable to a variety of techniques. This system, which they name behaviorMate, represents an important methodological contribution to the field of behavioral and systems neuroscience. As the authors note, behavioral control paradigms vary widely across laboratories in terms of hardware and software utilized and often require specialized technical knowledge to make changes to these systems. Having a standardized, easy to implement, and flexible system that can be used by many groups is therefore highly desirable.

Strengths:

The present manuscript provides compelling evidence of the functionality and applicability of behaviorMate. The authors report benchmark tests for high-fidelity, real-time update speed between the animal's movement and the behavioral control, on both the treadmill-based and virtual reality (VR) setups. The VR system relies on Unity, a common game development engine, but implements all scene generation and customizability in the authors' behaviorMate and VRMate software, which circumvents the need for users to program task logic in C# in Unity. Further, the authors nicely demonstrate and quantify reliable hippocampal place cell coding in both setups, using synchronized 2-photon imaging. This place cell characterization also provides a concrete comparison between the place cell properties observed in treadmill-based navigation vs. visual VR in a single study, which itself is a valuable contribution to the field.

Weaknesses: None noted.

Documentation for installing and operating behaviorMate is available via the authors' lab website and Github, linked in the manuscript.

The authors have addressed all of my requests for clarification from the previous round of review. This work will be of great interest to systems neuroscientists looking to integrate flexible head-fixed behavioral control with neural data acquisition.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97433.3.sa2](https://doi.org/10.7554/eLife.97433.3.sa2)

The authors present behaviorMate, an open-source behavior control system including a central GUI and compatible treadmill and display components. Notably, the system utilize the "Intranet of things" scheme and the components communicate through local network, making the system modular, which in turn allows user to configure the setup to suit their experimental needs. Overall, behaviorMate is a useful resource for researchers performing head-fixed VR imaging studies involving 1D navigation tasks, as the commercial alternatives are often expensive and inflexible to modify.

One major utility of behaviorMate is an open-source alternative to commercial behavior apparatus for head-fixed imaging studies involving 1D navigation tasks. The documentation, BOM, CAD files, circuit design, source and compiled software, along with the manuscript, create an invaluable resource for neuroscience researcher looking to set up a budget-friendly VR and head-fixed imaging rig. Some features of behaviorMate, including the computer vision-based calibration of treadmill, and the decentralized, Android-based display devices, are very innovative approaches and can be quite useful in practical settings.

behaviorMate can also be used as a set of generic schema and communication protocols that allows the users to incorporate recording and stimulation devices during a head-fixed imaging experiment. Due to the "Intranet of things" approach taken in the design, any hardware that supports UDP communication can in theory be incorporated into the system. In terms of current capability, behaviorMate supports experimental contingencies based on animal position and time and synchronization with external recording devices using a TTL start signal. Further customization involving more complicated experimental contingencies, more accurate recording synchronization (for example with ephys recording devices), incorporation of novel behavior and high-speed neural recording hardware beyond GPIO signaling would require modification of the Java source and custom hardware implementation. Modification to the Java source of behaviorMate can be performed with basic familiarity with object-oriented programming using the Java programming language, and a JavaFX-based plugin system is under development to make such customizations more approachable for users.

In summary, the manuscript presents a well-developed and useful open-source behavior control system for head-fixed VR imaging experiments with innovative features.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97433.3.sa3](https://doi.org/10.7554/eLife.97433.3.sa3)

In this work, the authors present an open-source system called behaviourMate for acquiring data related to animal behavior. The temporal alignment of recorded parameters across various devices is highlighted as crucial to avoid delays caused by electronics dependencies. This system not only addresses this issue but also offers an adaptable solution for VR setups. Given the significance of well-designed open-source platforms, this paper holds importance.

Advantages of behaviorMate:

The cost-effectiveness of the system provided.

The reliability of PCBs compared to custom-made systems.

Open-source nature for easy setup.

Plug & Play feature requiring no coding experience for optimizing experiment performance (only text based Json files, 'context List' required for editing).
