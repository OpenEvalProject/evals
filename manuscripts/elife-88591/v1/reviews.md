# Peer review - Round 1

Editors:
- Juan Alvaro Gallego, Imperial College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.88591.4.sa0](https://doi.org/10.7554/eLife.88591.4.sa0)

This work will be of interest to the motor control community as well as neuroAI researchers interested in how bodies constrain neural circuit function. The authors present "MotorNet", a useful software package to train artificial neural networks to control a biomechanical model of an effector. The manuscript provides solid evidence that MotorNet is easy to use and can reproduce past results in the field, both at the neural and behavioural levels. Validation is limited to planar arm-like plants or point-masses, so future work exploring three-dimensional movements and other types of plants would strengthen the impact of the tool.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88591.4.sa1](https://doi.org/10.7554/eLife.88591.4.sa1)

Summary:

Codol et al. present a toolbox that allows simulating biomechanically realistic effectors and training Artificial Neural Networks (ANNs) to control them. The paper provides a detailed explanation of how the toolbox is structured and several examples demonstrating its utility.

Main comments:

(1) The paper is well-written and easy to follow. The schematics facilitate understanding of the toolbox's functionality, and the examples give insight into the potential results users can achieve.

(2) The toolbox's latest version, developed in PyTorch, is expected to offer greater benefits to the community.

(3) The new API, being compatible with Gymnasium, broadens the toolbox's application scope, enabling the use of Reinforcement Learning for training the ANNs.

Impact:

MotorNet is designed to simplify the process of simulating complex experimental setups, enabling the rapid testing of hypotheses on how the brain generates specific movements. Implemented in PyTorch and compatible with widely-used machine learning toolboxes, including Gymnasium, it offers an end-to-end pipeline for training ANNs on simulated setups. This can greatly assist experimenters in determining the focus of their subsequent efforts.

Additional context:

The main outcome of the work, a toolbox, is supplemented by a GitHub repository and a documentation webpage. Both the repository and the webpage are well-organized and user-friendly. The webpage guides users through the toolbox installation process, as well as the construction of effectors and Artificial Neural Networks (ANNs).


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88591.4.sa2](https://doi.org/10.7554/eLife.88591.4.sa2)

MotorNet aims to provide a unified interface where the trained RNN controller exists within the same TensorFlow environment as the end effectors being controlled. This architecture provides a much simpler interface for the researcher to develop and iterate through computational hypotheses. In addition, the authors have built a set of biomechanically realistic end effectors (e.g., a 2 joint arm model with realistic muscles) within TensorFlow that are fully differentiable.

MotorNet will prove a highly useful starting point for researchers interested in exploring the challenges of controlling movement with realistic muscle and joint dynamics. The architecture features a conveniently modular design and the inclusion of simpler arm models provides an approachable learning curve. Other state-of-the-art simulation engines offer realistic models of muscles and multi-joint arms and afford more complex object manipulation and contact dynamics than MotorNet. However, MotorNet's approach allows for direct optimization of the controller network via gradient descent rather than reinforcement learning, which is a compromise currently required when other simulation engines (as these engines' code cannot be differentiated through).

The paper has been reorganized to provide clearer signposts to guide the reader. Importantly, the software has been rewritten atop PyTorch which is increasingly popular in ML and computational neuroscience research.
