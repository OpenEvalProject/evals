# Peer review - Round 1

Editors:
- Shelly B Flagel, https://ror.org/00jmfr291 University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.104833.3.sa0](https://doi.org/10.7554/eLife.104833.3.sa0)

This manuscript describes a novel approach for assessing cognitive function in freely moving mice in their home-cage, without human involvement. The authors provide convincing evidence in support of the tasks they developed to capture a variety of complex behaviors and demonstrate the utility of a machine learning approach to expedite the acquisition of task demands. This work is important given its potential utility for other investigators interested in studying mouse cognition.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.104833.3.sa1](https://doi.org/10.7554/eLife.104833.3.sa1)

Summary:

This is a new and important system that can efficiently train mice to perform a variety of cognitive tasks in a flexible manner. It is innovative and opens the door to important experiments in the neurobiology of learning and memory.

Strengths:

Strengths include: high n's, a robust system, task flexibility, comparison of manual-like training vs constant training, circadian analysis, comparison of varying cue types, long-term measurement, and machine teaching.

Weaknesses:

I find no major problems with this report.

Comments on revisions:

My concerns have been addressed now.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.104833.3.sa2](https://doi.org/10.7554/eLife.104833.3.sa2)

Summary:

The manuscript by Yu et al. describes a novel approach for collecting complex and different cognitive phenotypes in individually housed mice in their home cage. The authors report a simple yet elegant design that they developed for assessing a variety of complex and novel behavioral paradigms autonomously in mice.

Strengths:

The data are strong, the arguments are convincing, and I think the manuscript will be highly cited given the complexity of behavioral phenotypes one can collect using this relatively inexpensive ($100/box) and high-throughput procedure (without the need of human interaction). Additionally, the authors include a machine learning algorithm to correct for erroneous strategies that mice develop which is incredibly elegant and important for this approach, as mice will develop odd strategies when given complete freedom.

Weaknesses:

A limitation to this approach is that it requires mice to be individually housed for days to months. This is now adequately addressed in the discussion.

A major issue with continuous self-paced tasks such as the autonomous d2AFC used by the authors is that the inter-trial intervals can vary significantly. Mice may do a few trials, lose interest and disengage from the task for several hours. This is problematic for data analysis that relies on trial duration to be similar between trials (e.g., reinforcement learning algorithms). The authors now provide information regarding task engagement of the mice across a 24 hour cycle (e.g., trials started, trials finished across a 24 h period).

Movies - it would be beneficial for the authors to add commentary to the video (hit, miss trials). It was interesting watching the mice but not clear whether they were doing the task correctly or not. The new videos adequately address these concerns.

The strength of this paper (from my perspective) is the potential utility it has for other investigators trying to get mice to do behavioral tasks. However, not enough information was provided about the construction of the boxes, interface, and code for running the boxes. If the authors are not willing to provide this information through eLife, GitHub, or their own website then my evaluation of impact and significance of this paper would go down significantly. This information is now available to readers.

Minor concerns

Learning rate is confusing for Figure 3 results as it actually refers to trials to reach criterion, and not the actual rate of learning (e.g., slope). This has been modified in the manuscript.

Comments on revisions:

The authors have addressed all my concerns regarding this very exciting manuscript.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.104833.3.sa3](https://doi.org/10.7554/eLife.104833.3.sa3)

Summary:

In this set of experiments, the authors describe a novel research tool for studying complex cognitive tasks in mice, the HABITS automated training apparatus, and a novel "machine teaching" approach they use to accelerate training by algorithmically providing trials to animals that provide the most information about the current rule state for a given task.

Strengths:

There is much to be celebrated in an inexpensively constructed, replicable training environment that can be used with mice, which have rapidly become the model species of choice for understanding the roles of distinct circuits and genetic factors in cognition. Lingering challenges in developing and testing cognitive tasks in mice remain, however, and these are often chalked up to cognitive limitations in the species. The authors' findings, however, suggest that instead we may need to work creatively to meet mice where they live. In some cases it may be that mice may require durations of training far longer than laboratories are able to invest with manual training (up to over 100k trials, over months of daily testing) but that the tasks are achievable. The "machine teaching" approach further suggests that this duration could be substantially reduced by algorithmically optimizing each trial presented during training to maximize learning.

Weaknesses:

Cognitive training and testing in rodent models fill a number of roles. Sometimes, investigators are interested in within-subjects questions - querying a specific circuit, genetically defined neuron population, or molecule/drug candidate, by interrogating or manipulating its function in a highly trained animal. In this scenario, a cohort of highly trained animals which have been trained via a method that aims to make their behavior as similar as possible is a strength.

However, often investigators are interested in between-subjects questions - querying a source of individual differences that can have long term and/or developmental impacts, such as sex differences or gene variants. This is likely to often be the case in mouse models especially, because of their genetic tractability. In scenarios where investigators have examined cognitive processes between subjects in mice who vary across these sources of individual difference, the process of learning a task has been repeatedly shown to be different. The authors recognize that their approach is currently optimized for testing within-subjects questions, but begin to show how between-subjects questions might be addressed with this system.

The authors have perhaps shown that their main focus is highly-controlled within-subjects questions, as their dataset is almost exclusively made up of several hundred young adult male mice, with the exception of 6 females in a supplemental figure. It is notable that these female mice do appear to learn the two-alternative forced choice task somewhat more rapidly than the males in their cohort, and the authors suggest that future work with this system could be used to uncover strategies that differ across individuals.

Considering the implications for mice modeling relevant genetic variants, it is unclear to what extent the training protocols and especially the algorithmic machine teaching approach would be able to inform investigators about the differences between their groups during training. For investigators examining genetic models, it is unclear whether this extensive training experience would mitigate the ability to observe cognitive differences, or select for the animals best able to overcome them - eliminating the animals of interest. Likewise, the algorithmic approach aims to mitigate features of training such as side biases, but it is worth noting that the strategic uses of side biases in mice, as in primates, can benefit learning, rather than side biases solely being a problem. However, the investigators may be able to highlight variables selected by the algorithm that are associated with individual strategies in performing their tasks, and this would be a significant contribution.

A final, intriguing finding in this manuscript is that animal self-paced training led to much slower learning than "manual" training, by having the experimenter introduce the animal to the apparatus for a few hours each day. Manual training resulted in significantly faster learning, in almost half the number of trials on average, and with significantly fewer omitted trials. This finding does not necessarily argue that manual training is universally a better choice, because it led to more limited water consumption. However, it suggests that there is a distinct contribution of experimenter interactions and/or switching contexts in cognitive training, for example, by activating an "occasion setting" process to accelerate learning for a distinct period of time. Limiting experimenter interactions with mice may be a labor saving intervention, but may not necessarily improve performance. This could be an interesting topic of future investigation, of relevance to understanding how animals of all species learn.
