# Peer review - Round 1

Editors:
- Caleb Kemere, Rice University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67846.sa0](https://doi.org/10.7554/eLife.67846.sa0)

The importance of carefully-considered animal behavior to systems neuroscience cannot be overstated. Despite this, flexible tools for carefully monitoring and controlling behavioral apparatuses have often required significant new development by individual laboratories. The open source pyControl software and hardware toolbox is an excellent exemplar of a robust and reliable platform for experiments, with a simple interface, good performance, excellent documentation, and a growing an engaged user community. This work benchmarks and documents pyControl and hopefully will serve as a useful introduction to an even broader community.


---

# Peer review - Round 1

Editors:
- Caleb Kemere, Rice University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67846.sa1](https://doi.org/10.7554/eLife.67846.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for sending your article entitled "pyControl: Open source, Python based, hardware and software for controlling behavioural neuroscience experiments" for peer review at eLife. Your article is being evaluated by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation is being overseen by Kate Wassum as the Senior Editor.

The reviewers were unanimous in recognizing that the pyControl hardware/software suite is a useful tool. Indeed, the impressive list of current users makes that point. However, we felt that in order for the manuscript to merit publication, it needed to be more clear and transparent in presentation such that readers who are not current users would be convinced (by the material presented) that its usability – when compared with alternatives – is such that they should adopt it. By usability, we mean both (i) how easy it is to use for actual tasks and (ii) whether there are scenarios where task parameters or coding naivety make it fragile.

Reviewer #1:

Positives:

Most behavior systems take one of two broad approaches to the system configuration: run the task logic and data I/O through the host computer, which is connected to peripherals; or run the task logic and data I/O through an integrated external breakout board and microcontroller. Here, the authors have opted for the latter approach, arguing that it confers several advantages: 1) inexpensiveness, 2) flexibility, 3) user-friendliness, and 4) parallelism.

Certainly, microcontrollers (and their commercial or custom breakout boards) are a less expensive counterpart to desktop computers, albeit at the expense of lower processing power and memory. For experiments that require more computation, this platform may not be the best fit, which the authors acknowledge in their discussion. However, for many experiments, a microcontroller is sufficient, and thus the approach pyControl takes is reasonable.

The flexibility of the system is apparent in both the hardware and software. The custom breakout board offers a mixture of digital and analog I/O ports, as well as power supply lines for different peripheral devices. On the software side, the choice of state machine logic allows it to be broadly applicable. The ability to save both input/output streams and internal variables with timestamps is important.

Major Concern:

pyControl is a combination of hardware, API code, "task code", and control-computer code. For publication, a paper should go beyond merely showing a few tasks where code was used – it needs to not only demonstrate utility, but also document the system in ways beyond a user guide. While demonstrating the efficacy and reliability of the "task code" is the primary goal of this paper, it fails to do so convincingly.

0) Given the advantage of microcontroller-based behavioral control, the primary question facing this paper is: "Why should a lab deal with pyControl rather than rolling their own solution?" It seems like the easiest way to demonstrate this would be to show, e.g., an Arduino solution and a pyControl solution side by side so that it can be seen how obviously easier it is.

1) Figure 1 is confusing to the reader where it appears:

Figure 1 shows an example of running a simple "blink LED" task, and while the right panel is a nice visual complement to the task code, the actual task definition code on the left is at first unclear. Where is the "button_press" event (or any other event) defined when it becomes input to the task functions? Where do Digital_input() and Digital_output() come from? How are "entry" and "exit" events defined? (As an aside, it is usually best to avoid "import *" statements, as they can at best be confusing and at worst cause namespace conflicts. In this case, it is unclear which of the other module classes/functions came from "pyControl.utility" vs. "devices".) Perhaps it would be best to first introduce the overall organization of the hardware (Figure 2, 3), and then explain the task logic that is running on the microcontroller, which itself requires an understanding of how hardware is defined in the first place.

2) Hardware is given short shrift. The hardware definition examples in the supplementary figures seem superfluous. The configuration diagram are useful visuals for understanding how components are wired together, but the code underneath is mostly repetitive and can be left for the interested reader to find in the online documentation. Critically, what is missing is a broader explanation of how hardware devices are defined – both from an API perspective and in terms of the physical connection – that would allow the user to design their own.

3) Links to documentation do not belong in a scientific paper: Choosing a higher-level language like (micro)python makes the system user-friendly and separate from proprietary software like MATLAB. Additionally, the use of a GUI facilitates understanding of the task code and logic. The authors have clearly spent time building an extensive online documentation that is valuable for reaching a broad user base. However, the assumption of the reviewer is that our journal is more reliably archival than random sites on the internet. So anything that is relevant to understanding the paper should be included. (It may be possible to archive the code base along with the paper, which would solve this issue.)

4) There is significant concern about performance and reliability. What happens if two state transitions are triggered simultaneously? There is a description of an event queue: does the queue generation code automatically infer whether queued events are still valid – are race conditions possible? (Simple example – a triggered state transition that should occur if a timer has not elapsed, but a different set of states occurs if the timer has elapsed. What happens if the timer elapses and the trigger occur nearly simultaneously?)

5) There is concern about the choice of Micropython rather than a compiled language. In particular, it is unclear whether the performance testing adequately explored garbage collection. For example, if a naive user instantiates a timer in a state that is executed repeatedly, garbage collection will be regularly required to delete the relevant heap memory. If garbage collection is slow, this could result in unexpected loss of responsiveness or missed logging of data.

6) From the text, it appears that data are timestamped at 1 kHz, but the figures depict microsecond resolution. How fast can events occur? Most experiments will have events on the scale of second or 100s of milliseconds, but a naive user might instantiate a state tracking licks, which can occur much more rapidly when a mouse licks in a bout.

Reviewer #2:

The authors have presented a novel hardware/software solution called pyControl for coordinating common types of inputs and outputs in rodent behavioral experiments. It can be also be used to program tasks with other model organisms, including humans, but many of the peripheral devices (such as the nose-poke and lickometer) are specifically designed for use with rodents.

A key advantage of pyControl over other solutions in this space is the ability to program both the software and the embedded firmware in the same high-level language, Python. This allows users to have precise control of the system behavior without the need to learn a lower-level programming language, such as C++. It is also a highly cost effective solution, especially in comparison to closed-source platforms with similar functionality.

A major selling point of the pyControl ecosystem is the wide range of commercially available peripheral devices. For those considering adopting pyControl for their own work, it would be helpful if this manuscript included a more thorough characterization of the existing peripherals. Some of these devices are described in the "application examples" section, but there is almost no information about their specifications. It would also be useful to see an outline of the steps required to build a custom peripheral device.

To characterize the performance of pyControl, the authors have measured its response latency and timing accuracy under both "low load" and "high load" conditions. Even under conditions of high load (monitoring two highly active digital inputs and sampling two analog inputs at 1 kHz), the overwhelming majority of latencies were <1 ms, which is sufficient for most applications. In cases where very precisely timed stimuli are required, pyControl can be easily configured to send triggers to external devices.

Overall, pyControl is a welcome addition to the ever-growing list of tools for coordinating behavioral tasks. Labs that currently rely on undocumented, DIY solutions may find that pyControl provides the impetus to switch to a standardized, open-source platform. And researchers that depend on closed-source tools have the opportunity to save many thousands of dollars per year by using pyControl for their future rigs.

This manuscript will be a great resource for researchers that are considering adopting pyControl. I have a few suggestions for making it even better:

I'd like to see a more candid discussion of the limitations of pyControl for various types of experiments. For example, running everything on a microcontroller precludes the display of complex visual stimuli. Therefore, pyControl would not be suitable for most visual physiology experiments. Similarly, the pyControl Audio Player peripheral can only deliver stimuli up to 48 kHz, which limits its utility for rodent auditory physiology. pyControl of course includes general-purpose output ports that can be used to trigger any auxiliary devices, so these limitations could be overcome with some customization.

The authors should include more details about the pyboard microcontroller, since this is an essential component of the platform. What are the specifications, approximate cost, etc.? Is there a plan to take advantage of the pyBoard's wireless capabilities? This could be helpful for coordinating massively parallel experiments.

The "Karpova Lab" is mentioned out of context. Readers will likely want more information about what this means.

Since Bonsai does not itself encompass any hardware interfaces, a more accurate comparison would be with the combination of Bonsai and Harp (https://www.cf-hw.org/harp). Unfortunately, Harp doesn't have a publication associated with it, nor much online documentation. But the main advantages are shared timestamps (within 44 µs) across all devices, and tight integration with Bonsai software. The authors should mention the availability of Harp in their discussion of Bonsai.

Another behavior control platform that should be cited is Autopilot (https://www.biorxiv.org/content/10.1101/807693v1), which looks promising for certain applications, despite its relative immaturity.

A detailed characterization of closed-source commercial hardware is beyond the scope of this manuscript, but the authors should consider presenting at least a high-level comparison of these tools (in terms of order-of-magnitude cost, available features, and customizability). The discussion seems to be targeted at users choosing between various open-source solutions, but convincing researchers to adopt pyControl in favor of closed-source hardware is a much more important goal.

Reviewer #3:

Akam et al. detail an open-source system called pyControl, that is intended to be used to control behavioral neuroscience experiments. The authors nicely highlight the current problem of reproducibility in behavioral neuroscience, describing the difficulty of standardizing or understanding code and behavioral tasks across labs. It is quite clear the project is setting new standards, especially in the open-source neuroscience field, by addressing many pitfalls of previous behavioral systems and platforms. Thus, the major strength of the paper is the open-source manner with which the authors detail their system. The hardware and software provided in an open manner allows for researchers to streamline their behavioral tasks in a cost-effective manner while still maintaining the flexibility needed to perform specific experiments. The authors provide rather straightforward documentation of how to program and run behavioral experiments using pyControl software and the related GUI, as well as how the hardware is generally set up. The authors then validate the use of pyControl in three different behavioral tasks that are widely used in neuroscience research.

Strengths: The pyControl system itself serves the purpose of having one streamlined behavioral setup that can provide reproducibility across research labs, the system can seemingly be used by "novice" researchers with a beginner level skill set in both hardware and computer programming, and comes at a cheaper price than commercial (or other open source) behavior platforms. The project's website, user forum, and github are evidence of a well-supported project that is already being used across many research labs. The documentation is written in a tutorial-style manner, providing many examples and references between hardware and software, and making it easy to follow.

The authors additionally show convincing evidence of the robustness of the pyControl system with respect to the different behavioral paradigms it is capable of supporting. Many other behavior systems are limited in what tasks they can be used with, and the evidence of a flexible steup across different experiments in the manuscript is quite convincing. An added benefit of the system is its ability to time synchronize to electrophysiological or imaging platforms for optimal data analysis. The system, as a whole, is a "one-stop shop" for programming, running, and visualizing experiments in real time, and then open-source nature of the system allows researchers to (mostly) pick and choose how they'd like to utilize the system. The project has already gained steam with many different labs using it currently, and has the potential for improving rigor and robustness of understanding behavioral data across research labs.

Weaknesses: While the manuscript claims that pyControl is a flexible device, it is not clear how other devices could interact with the pyControl hardware. Many labs already have behavior devices (such as lickometers or solenoids or odor delivery ports, for example), either custom-built or from commercial vendors that already work well, but the researchers may instead be looking for a way to run their tasks in a simpler or well-documented manner. It is stated that it is 'straightforward' to make a pyControl compatible device but this is unclear within the manuscript how much work this would take, or the ease of using one's own devices. While the system is intended to have everything that anyone needs, the benefit of an open-source framework is that people are allowed to flexibly choose which aspects might work optimally for their research question. It would be best to at least detail how people could adapt their own devices. In the same realm, it is a bit unclear of the extent of capabilities of the system, with respect to data processing or memory storage, running multiple animals at once, or platform dependency, for example.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Open source, Python based, hardware and software for controlling behavioural neuroscience experiments." for further consideration by eLife. Your revised article has been evaluated by Kate Wassum (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below from Reviewer 1. The reviewers agreed that it is important that the manuscript be largely self-contained.Reviewer #1:

A journal paper is meant to document the past for reproduction, not advertise some potential future. The ephemeral nature of online documentation is not conducive to this. However, assuming the documentation is archived with the paper, I am satisfied that this can be addressed.

There is no reason not to adequately document the RJ-45 connector interface within the paper. It represents the current state of the hardware as opposed to some hypothetical future flexibility, requires minimal text, and represents a clear critical specification for users who wish to design their own modules. I see no reason for the authors not to do this.

The authors link to their help documentation to reply to our concern about "from pyControl.utility import *" and "from devices import *". This documentation essentially admits that unless one has completely understood the pyControl codebase (e.g., one of the developers) to know all of the functions and objects in the namespace, one is hopeless to avoid having collisions. This seems to directly contradict the claim that they have built a broadly useful tool.

Reviewer #2:

The revised manuscript is much improved, and the authors have addressed all of my concerns. This manuscript, in combination with the online documentation, will be an excellent resource for learning about pyControl.

Reviewer #3:

The authors have adequately responded to the reviews and provided a thorough and improved manuscript. I do not believe any additional work is required to the updated manuscript. I also agree with the authors that, as discussed around lines 673 in the author comments document, it is not necessary to include the additional panels for figure 7 as it would be repetitive to what is already in the figure.
