# Peer review - Round 1

Editors:
- Kristine Krug, Otto-von-Guericke University Magdeburg Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.98345.3.sa0](https://doi.org/10.7554/eLife.98345.3.sa0)

The fundamental study by Ding and colleagues identifies subpopulations of neurons recorded in the monkey subthalamic nucleus (STN) with distinct activity profiles and causal contributions during perceptual decision-making. The combination of neuronal recording, microstimulation, and computational methods provides convincing evidence for a heterogenous neural population that could support multifaceted roles in decision formation. This study should be of wide interest to computational and experimental neuroscientists interested in cognitive function.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98345.3.sa1](https://doi.org/10.7554/eLife.98345.3.sa1)

This study uses single-unit recordings in the monkey STN to examine the evidence for three theoretical models that propose distinct roles for the STN in perceptual decision-making. Importantly, the proposed functional roles are predictive of unique patterns of neural activity. Using k-means clustering with seeds informed by each model's predictions, the current study identified three neural clusters with activity dynamics that resembled those predicted by the described theoretical models. The authors are thorough and transparent in reporting the analyses used to validate the clustering procedure and the stability of the clustering results. To further establish a causal role for the STN in decision-making, the researchers applied microsimulation to the STN and found effects on response times, choice preferences, and latent decision parameters estimated with a drift-diffusion model. Overall, the study provides strong evidence for a functionally diverse population of STN neurons that could indeed support multiple roles involved in perceptual decision-making. The manuscript would benefit from stronger evidence linking each neural cluster to specific decision roles in order to strengthen the overall conclusions.

The interpretation of the results, and specifically, the degree to which the identified clusters support each model, is largely dependent on whether the artificial vectors used as model-based clustering seeds adequately capture the expected behavior under each theoretical model. The manuscript would benefit from providing further justification for the specific model predictions summarized in Figure 1B. Further, although each cluster's activity can be described in the context of the discussed models, these same neural dynamics could also reflect other processes not specific to the models. That is, while a model attributing the STN's role to assessing evidence accumulation may predict a ramping up of neural activity, activity ramping is not a selective correlate of evidence accumulation and could be indicative of a number of processes, e.g., uncertainty, the passage of time, etc.. This lack of specificity makes it challenging to infer the functional relevance of cluster activity and should be acknowledged in the discussion.

Additionally, although the effects of STN microstimulation on behavior provide important causal evidence linking the STN to decision processes, the stimulation results are highly variable and difficult to interpret. The authors provide a reasonable explanation for the variability, showing that neurons from unique clusters are anatomically intermingled such that stimulation likely affects neurons across several clusters. It is worth noting, however, that a substantial body of literature suggests that neural populations in the STN are topographically organized in a manner that is crucial for its role in action selection, providing "channels" that guide action execution. The authors should comment on how the current results, indicative of little anatomical clustering amongst the functional clusters, relates to other reports showing topographical organization.

Overall, the association between the identified clusters and the function ascribed to the STN by each of the models is largely descriptive and should be interpreted accordingly. For example, Figure 3 is referenced when describing which cluster activity is choice/coherence dependent, yet it is unclear what specific criteria and measures are being used to determine whether activity is choice/coherence "dependent." Visually, coherence activity seems to largely overlap in panel B (top row). Is there a statistically significant distinction between low and high coherence in this plot? The interpretation of these plots and the methods used to determine choice/coherence "dependence" needs further explanation.

In general, the association between cluster activity and each model could be more directly tested. At least two of the models assume coordination with other brain regions. Does the current dataset include recordings from any of these regions (e.g., mPFC or GPe) that could be used to bolster claims about the functional relevance of specific subpopulations? For example, one would expect coordinated activity between neural activity in mPFC and Cluster 2 according to the Ratcliff and Frank model. Additionally, the reported drift-diffusion model (DDM) results are difficult to interpret as microsimulation appears to have broad and varied effects across almost all the DDM model parameters. The DDM framework could, however, be used to more specifically test the relationships between each neural cluster and specific decision functions described in each model. Several studies have successfully shown that neural activity tracks specific latent decision parameters estimated by the DDM by including neural activity as a predictor in the model. Using this approach, the current study could examine whether each cluster's activity is predictive of specific decision parameters (e.g., evidence accumulation, decision thresholds, etc.). For example, according to the Ratcliff and Frank model, activity in cluster 2 might track decisions thresholds.

Review of revision

The authors have sufficiently addressed the concerns raised in the initial reviews and have revised their manuscript accordingly. We commend the authors for these efforts and feel that the revisions have strengthened the major claims of the manuscript.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98345.3.sa2](https://doi.org/10.7554/eLife.98345.3.sa2)

Summary:

The authors provide compelling evidence for the causal role of the subthalamic nucleus (STN) in perceptual decision-making. By recording from a large number of STN neurons and using microstimulation, they demonstrate the STN's involvement in setting decision bounds, scaling evidence accumulation, and modulating non-decision time.

Strengths:

The study tested three hypotheses about the STN's function and identified distinct STN subpopulations whose activity patterns support predictions from previous computational models. The experiments are well-designed, the analyses are rigorous, and the results significantly advance our understanding of the STN's multi-faceted role in decision formation.

Weaknesses:

While the study provides valuable insights into the STN's role in decision-making, there are a few areas that could be improved. First, the interpretation of the neural subpopulations' activity patterns in relation to the computational models should be clarified, as the observed patterns may not directly correspond to the specific signals predicted by the models. Second, a neural population model could be employed to better understand how the STN population jointly contributes to decision-making dynamics.
