# Peer review - Round 1

Editors:
- Sacha B Nelson, Brandeis University United States

Reviewers:
- Sacha B Nelson, Brandeis University United States
- Niraj Desai, Stony Brook University United States

## Review text

DOI: [10.7554/eLife.40231.018](https://doi.org/10.7554/eLife.40231.018)

In the interests of transparency, eLife includes the editorial decision letter, peer reviews, and accompanying author responses.

[Editorial note: This article has been through an editorial process in which the authors decide how to respond to the issues raised during peer review. The Reviewing Editor's assessment is that all the issues have been addressed.]

Thank you for submitting your article "Real-time experimental control using network-based parallel processing" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Sacha B Nelson as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Michael Frank as the Senior Editor. The following individual involved in review of your submission has also agreed to reveal their identity: Niraj Desai (Reviewer #2).

We strongly encourage you to revise your manuscript to deal with the issues raised in the reviews. As you can see, the reviewers feel that the present version does not live up to the claims you make for it, and we hope that you revise it to come far closer to a more useful contribution. As you know, these reviews and your responses will be published with the manuscript, as well as the editors' assessment of how responsive your revision is to the reviews.

Summary:

This is a description of a software package intended to generalize the problem of real time acquisition and control of rapidly changing signals, such as might be encountered in neuroscience experiments relating neurobiological signals to behavior. Although this is a potentially highly useful undertaking, the paper describes only a single use case involving primate vision experiments and many of the features of the described software seem highly specialized for this application with little information about the true generality of the described tool. In addition, reviewers were concerned that the overall approach lacked novelty and so a mere "proof of principle" was of limited value.

Major concerns:

As you can see in the reviews below, the reviewers largely agree on these central recommendations:

1) Maximize the generality of the described tool/resource by demonstrating application to multiple diverse experimental settings and by providing information on how to customize the software for any of a range of applications. This could be achieved, for example, by briefly describing the application to the psychophysics experiments alluded to, and by collaborating with another lab to tailor the system to their acquisition/control needs in a very different (ideally non-vision) setting.

2) Describe the performance in more general terms (e.g. as is done in Figure 5), rather than in terms specific to the major use case for which it was developed. This also applies to the discussion, which is now very focussed on software for monkey vision experiments.

3) Think through and describe the resources needed to support application of the software to other use cases. This includes a plan for maintenance of the software (e.g. via GitHub) as well as much more detailed supplementary instructions for modification and use.

4) Clearly state existing limitations to the generality. State what has and has not been tested and what is and is not possible with the existing software.

5) Although the issue of novelty of the approach was raised by one of the reviewers, and this view is shared, it will likely not be helpful to try to rewrite the manuscript to stress the novelty. Taking steps to ensure the usefulness and then highlighting them will probably be more fruitful in terms of improving the manuscript.

Separate reviews:

Reviewer #1:

The authors describe a new software suite for data acquisition in neurophysiology experiments. The intriguing features promised in the early parts of the paper are that it is highly modular, agnostic to coding language and operating system, and hence broadly applicable to many types of real time data acquisition and control experiments. The authors achieve high performance in terms of simultaneously computing stimuli, monitoring behavior and acquiring neurophysiological signals by segregating tasks and running them on separate processors linked by internet protocols, augmented by standard digital IO.

The rest of the paper is somewhat disappointing in that it mainly describes applicability to a single type of experiment (visual stimulation and recording of eye position and extracellular action potentials in behaving primates). Hence it is not likely to be obvious to most readers not performing very similar experiments, how they might configure the system for very different experiments. Ideally, a paper describing a general purpose system would apply it to more than one system. The figures are mostly devoted to the performance relevant to their specific experiment and so will not interest many readers. Figure 5 gives some idea of the performance in a general sense of the interaction between components, but Figures 3,4,6,7,8 are highly specific to the particular project and so are really not especially relevant to most readers interested in a more general tool. These figures would mostly be better as supplements to figures that measure performance or describe capabilities in a more general way. This lack of generality is exacerbated by the fact that the link to the downloads related to the software is nonfunctional.

Readers would want to know things like: which operating systems were actually tested? Which coding languages were used? Which acquisition hardware was tested? What aspects of the GUI are configurable and which are hard coded? They would want examples of experiments performed that are of multiple types involving different types of signals and different control paradigms. Otherwise, this publication would really be much more appropriate for a more specialized audience (e.g. the monkeyLogic paper was published in J. Neurophysiol. the Psychophysics Toolbox paper was in Spatial Vision and an update was published in Perception).

Finally, the discussion contains comparisons to other systems, but these comparisons are again formulated in terms of a very specific experiment's requirements (e.g. 240 Hz visual stimulus presentation) rather than in more generic terms of bandwidth for acquisition and control.

Additional data files and statistical comments:

The support for the software is a critical part of publication and of evaluation of the manuscript. The web site allowing access to the User Manual and other downloads was not accessible, even though these were included with the submission. As noted above, a User Manual for modifying the software and applying it to other kinds of experiments is also needed.

Reviewer #2:

Kim and colleagues present a parallel processing framework to integrate electrophysiological (or other neural) measurements, stimulus generation, and behavioral control. Their basic idea is that complex experiments can be run in a flexible manner if different tasks are spread out between different CPUs, which communicate with each other via standard internet protocols (TCP and UDP). The idea is intriguing and the implementation the authors themselves use is an excellent proof of principle. The major weakness is that the authors offer very little guidance to researchers who have different equipment or study a different experimental system, or simply have different experimental objectives and constraints. The project as it stands – the manuscript, the supplementary software examples, and the (under construction) website – is too particular to the authors' own work; it would be difficult for others to generalize from this.

Strengths:

1) The basic idea is clever: breaking up complex experiments into modules definitely seems like a good way to combine flexibility, computationally-intensive processes, and temporal fidelity. And exploiting existing protocols for network communication should make integration of these processes seamless. Many types of experimental programs could benefit from the general approach.

2) The kinds of experiments these authors themselves do – awake monkeys, complex visual stimuli, real-time control – are very technically challenging. Their success in using the general approach in this particular case is therefore reassuring, and their software likely will help others who do the same kinds of experiments.

Weakness:

3) But what about everybody else? The authors make broad claims for their framework:

"Since the only constraint on incorporating specialized software or hardware is that network interfacing is supported, a broad range of devices for stimulus presentation (visual displays, speakers, pellet droppers, etc.), behavioral measurement (button presses, eye movements, biometrics, location, etc.), and other experimental needs (stimulator, osmotic pump, etc.) can be used out of the box. Such flexibility allows the framework to be adapted to a broad range of experimental preparations (in vitro, anesthetized, or awake-behaving) and neuroscience research domains (sensory, cognitive, motor, etc.), and makes it agnostic to the type of neural data recorded (electrophysiological, optical, magnetic resonance imaging, etc.)."

I suspect these claims are true, but I also think that the authors haven't demonstrated that they're true. Their vision experiment is the only implementation described and the only example given. In fact, the authors' separate work on "perceptual learning studies with adolescents with autism" is alluded to, but not described.

More importantly, the authors never really explain – in detail – how to implement the framework. The descriptions are either too particular to the authors' own equipment or too general and/or vague to be useful. The manuscript assures readers that implementation is straightforward in language that is, perhaps, meant to be reassuring but comes off as glib: "Other acquisition systems that support network interfacing can be substituted with minimal effort.… The default GUI contains interfaces to control eye calibration and receptive field mapping, but these can be easily substituted with other tools." A reasonable reader response: "Okay.… sure.… if you say so.… but how do I do this?!"

In making this criticism, I'm motivated by the question of what a methods paper is for. My view is that the best methods papers offer not only a proof of principle but serve as a how-to guide. In the Introduction, the authors indicate that they hope their framework will benefit labs that lack the technical skills to design complex experimental systems themselves. That is a valuable goal – and a feasible one – but, in my opinion, they haven't reached that goal here. In fact, even labs with a lot of technical expertise but different equipment will need to "reinvent the wheel" to get this working.

What I would suggest is that the authors describe – perhaps in supplementary material so as not to disrupt the flow of the main text too much – how they built their system step by step by step. How both physically and in software do you connect a piece of hardware with a CPU using TCP? How do you set up a network interface card? Maybe show screen captures or pictures of the equipment. Do something to make this more tangible.

A related point: the software examples are not enough. Reading code written by someone else is one of life's great miseries, no matter the talent of the original programmer, and in this case is not especially helpful in understanding how the REC-GUI framework works.

Minor Comments:

1) The Introduction promises something very broad – a general system that can be used easily without great technical investment. Unless and until the rest of the manuscript fulfills this promises, it should be toned down. It should state more clearly and narrowly what is actually in the paper.

2) The project should live on Github or someplace similar. One reason open-source projects fail to gain traction is when they are seen as too proprietary. REC-GUI will only be important if it is adopted by a wide community, outside of the originating lab. The software shouldn't live on that lab's website. Also, the authors write: "We will maintain the REC-GUI framework as an open-source project.…." What does that mean exactly? Maintain it for a year? For five years? 10? 20? Things change in the life of a lab; people graduate and move on. If this project is to be real, it can't be tied to one lab.

3) Although the Abstract and Introduction talk about being independent of a particular operating system, but the website indicates that the Ubuntu version of Linux is "highly recommended" for the GUI. That is a real limitation and should be mentioned explicitly in the manuscript.

Reviewer #3:

The authors describe a UDP/TCP approach for coordinating eye tracking, electrophysiology, and behavioral input across multiple computers. The loop interval is about 5ms. The authors can transmit information among the various CPUs, and presumably more CPUs could be integrated into this system. The authors have done a good job of writing down and describing their system. It is faster than most, with a 5ms cycle time.

My biggest problem with the article is that there really isn't any novelty. Every lab I've been in has solved this problem similarly, with multiple CPUs and some communication across them via the network. Some labs I know use some combination of UDP/TCP, file systems, and digital TTL signals. In my opinion, this article doesn't belong in eLife, I don't think it will appeal to its broad readership. It's not novel enough.

At the same time, not to discourage the authors, I applaud the fact that they have written this down and have made it available to other groups.
