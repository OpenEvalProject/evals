# Peer review - Round 1

Editors:
- Laurent Keller, University of Lausanne Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55395.sa1](https://doi.org/10.7554/eLife.55395.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Your analyses of social interaction with information theory are very interesting and pave a new way for the study of the organisation of social organisms. We are therefore pleased to publish your paper.

Decision letter after peer review:

Thank you for submitting your article "Revealing the structure of information flows discriminates similar animal social behaviors" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Christian Rutz as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Jean-Louis Deneubourg (Reviewer #1).

On the basis of the three reviews, which are appended below, the Reviewing Editor has drafted this decision letter to help you prepare a revised submission. In recognition of the fact that revisions may take longer than the two months we typically allow, until the research enterprise restarts in full, we will give authors as much time as they require to submit revised manuscripts.

We agree with the three reviewers that this well-written paper presents interesting work that should be of interest to a general audience. The three reviewers made valuable comments, which all need to be addressed carefully. We agree in particular with their concern that it is not easy to make robust comparisons across species, given differences in their biology and the experimental procedures used, so this point requires particular attention.

Reviewer #1:

The Valentini et al.'s work is highly original and opens new perspectives for better understanding how animal communicate. This paper presents highly original methods (based on the information theory) and results (interaction between social insects) as to justify its publication in eLife. In short, I strongly recommend its publication.

Valentini et al. show that non-invasive information-theoretic tools reveal the communication protocol by measuring simultaneous flows of different information between social individuals. The authors demonstrate the power of their approach/method by showing that the tandem recruitment of ants and termites are governed by different communication protocols. They also stress – and I share their statements – the fact that their method is non-invasive (based only on observational data from many repeated interactions) and does not rely on a priori assumptions (model-free). The subject is not only an issue concerning biology of social insects but it is of interest to a wide readership including specialists in social behaviour, collective phenomena, complex systems, etc.

More specifically, one of the interesting results – and it is surprising – is the difference concerning the transfer of information (in tandem recruitment) from follower to leader between ants and termites.

The Abstract summarizes well the content of the paper. The Introduction does a good job summarizing the biological challenges (function of tandem running behaviour) and the theoretical background (information theory). The manuscript is very well-written and very pleasant to read. The goals of the work are clearly set out, the methods (and theoretical tools) are very well explained and the results are impressive and convincing.

Reviewer #2:

This paper provides an information-theoretic explanation for the different purposes of tandem running in ants and termites. In agreement with the literature, while followers in ants participate in the tandem runs to learn a route, and followers in termites simply help explore the region the authors reveal different directionalities of information transfer between these species. These different purposes manifest in the form of how leader-follower relationships emerge within seemingly similar trajectory data. Symbolic time-series representation is used to encode different behaviors within the tandem run. The paper is well written and the results are impactful providing a mathematical interpretation to complex behaviors. The authors have taken care to ensure that the results are robust through a detailed sensitivity analysis.

I have few questions/comments regarding the methodology:

1) I was not able to understand how exactly the behaviors were encoded? Is there a manual step or is it all automatic. The para starting from 267 gets somewhat involved and does not explain how exactly the authors went from trajectory data to symbols. What exactly do the authors mean by 10th percentile of a sequence. The next paragraph on rotation was clearer but there too I was wondering if there were any thresholds to distinguish collinear motion from rotational motion.

2) Related to above, how did the authors determine the length of a sequence to be encoded? Was it a moving window?

3) What was the size of the dataset? How many instances of behaviors were compared for each species?

4) Is the leader ant always the one moving in front. This should be explicitly noted somewhere because it may not be true for all species. Perhaps the authors can consider renaming front-back ants/termites to not confuse with leader-follower which term is use to imply a causal relationship in itself.

5) What were the reasons for selecting different sampling periods and history lengths for the same species. For the ant for example the values are very far apart. The authors can either (a) pick similar values where they can, or (b) discuss why they think information transfer is maximized at different scales for the same species for different behaviors.

6) I couldn't find any statistics on the rotation bars in Figure 1D.

Reviewer #3:

The paper demonstrates an interesting model-free methodology for extracting and interpreting qualitatively different behaviors in pairs of insects moving together in a nominally similar way (i.e. tandem running). The experiments and analytical tools are generally well explained. However, I have a fundamental concern about the conclusions that are drawn as they relate to the species tested, but not acknowledging the dramatic differences in the experimental procedures used for ants versus termites.

1) My major concern is that the experiments used to gather the data from the ants and the two species of termites seem very different. The ants are recorded when the whole colony is perturbed and seeks to move to a new nest. The termites are sexed pairs exploring their environment in a featureless petri dish. I am not an expert in social insects, but I would imagine either one of these species would behave differently in the two different experiments. I think a strong argument must be made if that's not the case. If that is the case, I think the work here is still very valuable. However, the conclusion which can be drawn from the results may be not so much about differences between species, but instead about how the information-theoretic methodology is able to extract qualitatively different strategies that the animals may be using.

2) Another concern is the lack of detail provided about the correction factor used as a control condition. The authors scramble the data from matched pairs of insects and rerun the analysis to measure a "baseline" information flow which simply is the result of these animals moving in the same space and responding to the same global cues. This is a really important part of the study in my opinion, since it is known that transfer entropy cannot distinguish between "x causes y" and "z causes x and y". The correction factor which is computed should be reported, and statistical tests should be performed to say that the measured effect is significantly more than this control. Perhaps this was done by the authors, but I was not able to tell from the text.
