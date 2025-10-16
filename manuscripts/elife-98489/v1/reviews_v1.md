# Peer review - Round 1

Editors:
- Peter Latham, University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.98489.3.sa0](https://doi.org/10.7554/eLife.98489.3.sa0)

This study introduces a useful extension to a recently proposed model of neural assembly activity. The extension was to add recurrent connections to the hidden units of the Restricted Boltzmann Machine. The authors show solid evidence that the new model outperforms their earlier model on both a simulated dataset and on whole-brain neural activity from zebrafish.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98489.3.sa1](https://doi.org/10.7554/eLife.98489.3.sa1)

Summary:

Understanding large-scale neural activity remains a formidable challenge in neuroscience. While several methods have been proposed to discover the assemblies from such large-scale recordings, most of previous studies do not explicit modeling the temporal dynamics. This study is an attempt to uncover the temporal dynamics of assemblies using a tool that have been establish in other domains.

The authors previously introduced the compositional Restricted Boltzmann Machine (cRBM) to identify neuron assemblies in zebrafish brain activity. Building upon this, they now employ the Recurrent Temporal Restricted Boltzmann Machine (RTRBM) to elucidate the temporal dynamics within these assemblies. By introducing recurrent connections between hidden units, RTRBM could retrieve neural assemblies and their temporal dynamics from simulated and zebrafish brain data.

Strengths:

The RTRBM has been previously used in other domains. Training the model has been already established. This study is an application of such model to neuroscience. Overall, the paper is well-structured and the methodology is robust, the analysis is solid to support the authors claim.

Weaknesses:

The overall degree of advance is very limited. The performance improvement by RTRBM compared to their cRBM is marginal, and insights into assembly dynamics are limited.

(1) The biological insights from this method are constrained. Though the aim is to unravel neural ensemble dynamics, the paper lacks in-depth discussion on how this method enhances our understanding of zebrafish neural dynamics. For example, the dynamics of assemblies can be analyzed using various tools such as dimensionality reduction methods once we have identified them using cRBM. What information can we gain by knowing the effective recurrent connection between them? It would be more convincing to show this in real data.

(2) Including predicted and measured neural activity traces could aid readers in evaluating model efficacy. The current version only contains comparison of the statistics, such as mean and covariance.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98489.3.sa2](https://doi.org/10.7554/eLife.98489.3.sa2)

Summary:

In this work, the authors propose an extension to some of the last author's previous work, where a compositional restricted Boltzmann machine was considered as a generative model of neuron-assembly interaction. They augment this model by recurrent connections between the Boltzmann machine's hidden units, which allow them to explicitly account for temporal dynamics of the assembly activity. Since their model formulation does not allow the training towards a compositional phase (as in the previous model), they employ a transfer learning approach according to which they initialise their model with a weight matrix that was pre-trained using the earlier model so as to essentially start the actually training in a compositional phase. Finally, they test this model on synthetic and actual data of whole-brain light-sheet-microscopy recordings of spontaneous activity from the brain of larval zebrafish.

Strengths:

This work introduces a new model for neural assembly activity. Importantly, being able to capture temporal assembly dynamics is an interesting feature that goes beyond many existing models. While this work clearly focuses on the method (or the model) itself, it opens up an avenue for experimental research where it will be interesting to see if one can obtain any biologically meaningful insights considering these temporal dynamics when one is able to, for instance, relate them to development or behaviour.

Weaknesses:

For most of the work, the authors present their RTRBM model as an improvement over the earlier cRBM model. Yet, when considering synthetic data, they actually seem to compare with a "standard" RBM model. This seems odd considering the overall narrative and that when considering whole-brain zebrafish data, the comparisons were made between RTRBM and cRBM models. For that, the RTRBM model was initialised with the cRBM weight matrix to overcome the fact that RTRBM alone does not seem to converge to a compositional phase, so to cite the latter as reason does not really make sense.

Furthermore, whether the clusters shown in Figure 3E can indeed be described as "spatially localized" is debatable. Especially in view of clusters 3 and 4, this seems a stretch. If receptive fields are described as "spatially localized", arguably, one would expect that they are contained in some small (compared to the overall size of the brain) or specific anatomical brain region. However, this is clearly not the case here.

In addition, the performance comparison for the temporal dynamics of the hidden units actually suggests that the RTRBM (significantly) underperforms where the text says (Line 235f) it outperforms the cRBM model.
