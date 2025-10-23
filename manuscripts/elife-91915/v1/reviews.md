# Peer review - Round 1

Editors:
- Gordon J Berman, Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.91915.3.sa0](https://doi.org/10.7554/eLife.91915.3.sa0)

This valuable paper introduces Heron, lightweight scientific software that is designed to streamline the implementation of complex experimental pipelines. The software is tailored for workflows that require coordinating many logical steps across interconnected hardware components with heterogeneous computing environments. The authors convincingly demonstrate Heron's utility and effectiveness in the context of behavioral experiments, addressing a growing need among experimentalists for flexible and scalable solutions that accommodate diverse and evolving hardware requirements.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91915.3.sa1](https://doi.org/10.7554/eLife.91915.3.sa1)

Summary:

The authors provide an open-source graphic user interface (GUI) called Heron, implemented in Python, that is designed to help experimentalists to:

(1) Design experimental pipelines and implement them in a way that is closely aligned with their mental schemata of the experiments

(2) Execute and control the experimental pipelines with numerous interconnected hardware and software on a network.

The former is achieved by representing an experimental pipeline using a Knowledge Graph and visually representing this graph in the GUI. The latter is accomplished by using an actor model to govern the interaction among interconnected nodes through messaging, implemented using ZeroMQ. The nodes themselves execute user-supplied code in, but not limited to, Python.

Using three showcases of behavioral experiments on rats, the authors highlighted four benefits of their software design:

(1) The knowledge graph serves as a self-documentation of the logic of the experiment, enhancing the readability and reproducibility of the experiment,

(2) The experiment can be executed in a distributed fashion across multiple machines that each has different operating system or computing environment, such that the experiment can take advantage of hardware that sometimes can only work on a specific computer/OS, a commonly seen issue nowadays,

(3) The users supply their own Python code for node execution that is supposed to be more friendly to those who do not have a strong programming background,

(4) The GUI can also be used as an experiment control panel for users to control/update parameters on the fly.

Strengths:

(1) The software is light-weight and open-source, provides a clean and easy-to-use GUI,

(2) The software answers the need of experimentalists, particularly in the field of behavioral science, to deal with the diversity of hardware that becomes restricted to run on dedicated systems. It can also be widely adopted in many other experimental settings.

(3) The software has a solid design that seems to be functionally reliable and useful under many conditions, demonstrated by a number of sophisticated experimental setups.

(4) The software is well documented. The authors pay special attention to documenting the usage of the software and setting up experiments using this software.

Comments on revisions: The authors have addressed my concerns from the initial review.
