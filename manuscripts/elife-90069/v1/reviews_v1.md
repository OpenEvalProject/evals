# Peer review - Round 1

Editors:
- Adrien Peyrache, McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.90069.3.sa0](https://doi.org/10.7554/eLife.90069.3.sa0)

This study presents a new and important theoretical account of spatial representational drift in the hippocampus. The evidence supporting the claims is convincing, with a clear and accessible explanation of the phenomenon. Overall, this study will likely attract researchers exploring learning and representation in both biological and artificial neural networks.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90069.3.sa1](https://doi.org/10.7554/eLife.90069.3.sa1)

The authors start from the premise that neural circuits exhibit "representational drift" -- i.e., slow and spontaneous changes in neural tuning despite constant network performance. While the extent to which biological systems exhibit drift is an active area of study and debate (as the authors acknowledge), there is enough interest in this topic to justify the development of theoretical models of drift.

The contribution of this paper is to claim that drift can reflect a mixture of "directed random motion" as well as "steady state null drift." Thus far, most work within the computational neuroscience literature has focused on the latter. That is, drift is often viewed to be a harmless byproduct of continual learning under noise. In this view, drift does not affect the performance of the circuit nor does it change the nature of the network's solution or representation of the environment. The authors aim to challenge the latter viewpoint by showing that the statistics of neural representations can change (e.g. increase in sparsity) during early stages of drift. Further, they interpret this directed form of drift as "implicit regularization" on the network.

The evidence presented in favor of these claims is concise, but on balance I find their evidence persuasive, at least in artificial network models. This paper includes a brief analysis of four independent experiments in Figure 3, which corroborates the main claims of the paper. Future work should dig deeper into the experimental data to provide a finer grained characterization. For example, in addition to quantifying the overall number of active units, it would be interesting to track changes in the signal-to-noise ratio of each place field, the widths of the place fields, et cetera.

To establish the possibility of implicit regularization in artificial networks, the authors cite convincing work from the machine learning community (Blanc et al. 2020, Li et al., 2021). Here the authors make an important contribution by translating these findings into more biologically plausible models and showing that their core assumptions remain plausible. The authors also develop helpful intuition in Figure 5 by showing a minimal model that captures the essence of their result.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90069.3.sa2](https://doi.org/10.7554/eLife.90069.3.sa2)

Summary:

In the manuscript "Representational drift as a result of implicit regularization" the authors study the phenomenon of representational drift (RD) in the context of an artificial network which is trained in a predictive coding framework. When trained on a task for spatial navigation on a linear track, they found that a stochastic gradient descent algorithm led to a fast initial convergence to spatially tuned units, but then to a second very slow, yet directed drift which sparsified the representation while increasing the spatial information. They finally show that this separation of time-scales is a robust phenomenon and occurs for a number of distinct learning rules.

This is a very clearly written and insightful paper, and I think people in the community will benefit from understanding how RD can emerge in such artificial networks. The mechanism underlying RD in these models is clearly laid out and the explanation given is convincing.

It still remains unclear how this mechanism may account for the learning of multiple environments, although this is perhaps a topic for future study. The non-stationarity of the drift in this framework would seem, at first blush, to contrast with what one sees experimentally, but the authors provide compelling evidence that there are continuous changes in network properties during learning and that stationarity may be the hallmark of overfamiliarized environments. Future experimental work may further shed light on differences in RD between novel and familiar environments.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90069.3.sa3](https://doi.org/10.7554/eLife.90069.3.sa3)

Summary:

Single unit neural activity tuned to environmental or behavioral variables gradually changes over time. This phenomenon, called representational drift, occurs even when all external variables remain constant, and challenges the idea that stable neural activity supports the performance of well-learned behaviors. While a number of studies have described representational drift across multiple brain regions, our understanding of the underlying mechanism driving drift is limited. Ratzon et al. propose that implicit regularization - which occurs when machine learning networks continue to reconfigure after reaching an optimal solution - could provide insights into why and how drift occurs in neurons. To test this theory, Ratzon et al. trained a recurrent neural network (RNN) trained to perform the oft-utilized linear track behavioral paradigm and compare the changes in hidden layer units to those observed in hippocampal place cells recorded in awake, behaving animals.

Ratzon et al. clearly demonstrate that hidden layer units in their model undergo consistent changes even after the task is well-learned, mirroring representational drift observed in real hippocampal neurons. They show that the drift occurs across three separate measures: the active proportion of units (referred to as sparsification), spatial information of units, and correlation of spatial activity. They continue to address the conditions and parameters under which drift occurs in their model to assess the generalizability of their findings to non-spatial tasks. Last, they investigate the mechanism through which sparsification occurs, showing that flatness of the manifold near the solution can influence how the network reconfigures. The authors suggest that their findings indicate a three stage learning process: (1) fast initial learning followed by (2) directed motion along a manifold which transitions to (3) undirected motion along a manifold.

Overall, the authors' results support the main conclusion that implicit regularization in machine learning networks mirrors representational drift observed in hippocampal place cells. Their findings promise to open new fields of inquiry into the connection between machine learning and representational drift in other, non-spatial learning paradigms, and to generate testable predictions for neural data.

Strengths:

(1) Ratzon et al. make an insightful connection between well-known phenomena in two separate fields: implicit regularization in machine learning and representational drift in the brain. They demonstrate that changes in a recurrent neural network mirror those observed in the brain, which opens a number of interesting questions for future investigation.

(2) The authors do an admirable job of writing to a large audience and make efforts to provide examples to make machine learning ideas accessible to a neuroscience audience and vice versa. This is no small feat and aids in broadening the impact of their work.

(3) This paper promises to generate testable hypotheses to examine in real neural data, e.g., that drift rate should plateau over long timescales (now testable with the ability to track single-unit neural activity across long time scales with calcium imaging and flexible silicon probes). Additionally, it provides another set of tools for the neuroscience community at large to use when analyzing the increasingly high-dimensional data sets collected today.

Weaknesses:

The revised manuscript addresses all the weaknesses outlined in my initial review. However, there is one remaining (minor) weakness regarding how "sparseness" is used and defined.

Sparseness can mean different things to different fields. For example, for engram studies, sparseness could be measured at the population level by the proportion of active cells, whereas for a physiology study, sparseness might be measured at the neuron level by the change in peak firing rate of each cell as an animal enters that cell's place field. In this manuscript, the idea of "sparseness" is introduced indirectly in the last paragraph of the introduction as "...changes in activity statistics (sparseness)...", but it is unclear from the preceding text if the referenced "activity statistics" used to define sparseness are the "fraction of active units," or their "tuning specificity," or both. While sparseness is clearly defined in the Methods section for the RNN, there is no mention of how it is defined for neural data, and spatial information is not mentioned at all. For clarity, I suggest explicitly defining sparseness for both the RNN and real neural data early in the main text, e.g. "Here, we measure sparseness in neural data by A and B, and by the analogous metric(s) of X and Y in our RNN..." This is a small but important nuance that will enhance the ease of reading for a broad neuroscience audience.
