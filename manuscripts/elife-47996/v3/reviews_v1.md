# Peer review - Round 1

Editors:
- Timothy O'Leary, University of Cambridge United Kingdom

Reviewers:
- Jordi Soriano, Universitat de Barcelona

## Review text

DOI: [10.7554/eLife.47996.030](https://doi.org/10.7554/eLife.47996.030)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Self-organization of modular network architecture by activity-dependent neuronal migration and outgrowth" for consideration by eLife. Your article has been reviewed by Eve Marder as the Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Jordi Soriano (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This is a combined experimental and modeling study on neurite growth and migration of cultured neurons. The authors investigate experimentally neural network development with pharmacologically decreased (PKC-), normal (PKCN) and increased (PKC+) neural migration. They find that a higher tendency to migrate leads to higher network clustering but to smaller dendrite sizes and numbers of synaptic partners of a neuron. The results and modelling provide insights into activity-dependent regulation of neuronal growth and are consistent with the notion of an internal set-point in activity.

Essential revisions:

Elements of this work appear to have been reported previously – J Neurosci (2017) and in Front Neurosci (2019). The authors need to fully discuss the relationship of the current findings and study to this previous work, noting any key advances. Abstract concepts such as modularity and clustering need to be unambiguously defined and distinguished. More in-depth analysis of clustering is suggested. There were general concerns about clarity, citations and presentation, outlined in the reviews. These must be addressed.

Reviewer #1:

In this manuscript the authors study the development of a network of cortical neurons grown in vitro on multi-electrode arrays (MEAs) allowing to assess many electrophysiological and morphological parameters of the cultures. Cultures were grown in control medium and in the presence of an activator or an inhibitor of Protein Kinase C (PKC). The authors suggest that the activation and inhibition of PKC is stimulating and inhibiting neuronal migration. They find that with PKC stimulation a network with a high degree of neuronal clustering develops. In contrast, with inhibition of PKC, very little neuronal clustering was observed. These findings correspond to simulations based on the van Ooyen model which yield comparable results for network formation with strong and weak neuronal migration. The highly clustered networks show strong spontaneous bursting activity which is rather rare in weakly clustered networks. In contrast, the peak firing rates during the bursts were much higher in weakly clustered networks, suggesting that the net calcium influx was similar in both types of cultures.

The experiments are well done and well documented, and the findings regarding network development with stronger and weaker neuronal migration are very interesting.

There are two issues with this manuscript which, however, could be resolved by the authors with reasonable effort.

1) The manuscript is an extension of previous work by the authors which was published in J Neuroscience previously (Okujeni et al., 2017). In this previous manuscript many of the principle findings reported in the present manuscript were already reported, for example the increased clustering with activation of PKC, the increased spontaneous burst activity with activation of PKC, the increased synaptic density with inhibition of PKC and the different average and peak firing rates with activation and inhibition of PKC. The major novel aspects of the present manuscript are that the development of the network was assessed at different time points revealing the development of the different states. My problem is that the authors do very little to clearly spell out which are new findings and which are extensions or replications of the published work. The authors should reorganize the manuscript such that it becomes clear which data are novel and should much more clearly focus on the novel aspects contained in this manuscript.

2) Based on the simulation experiments, the authors attribute the effects seen with PKC stimulation mostly to the inhibition and promotion of neuronal migration, and interpret the other aspects (as dendritic growth and synaptic density) as a consequence of the change of neuronal migration based on their modified van Ooyen model. While it is attractive to postulate that neuronal migration is the major difference between the three culture conditions, this may not reflect the actual situation. Protein kinase C activity was shown previously to directly affect dendritic development and is known to regulate postsynaptic changes responsible for LTP and LTD in addition to actions on many other target molecules. Reducing the multifaceted effects of PKC to neuronal migration appears to be unrealistic.

Reviewer #2:

The paper presents an interesting combined experimental and modeling study on neurite growth and migration of cultured neurons. The authors investigate experimentally neural network development with pharmacologically decreased (PKC-), normal (PKCN) and increased (PKC+) neural migration. They find that a higher tendency to migrate leads to higher network clustering but to smaller dendrite sizes and numbers of synaptic partners of a neuron. Particularly interesting is also the quadratic increase of the number of synapses per neuron with dendrite size, suggesting that axons follow a similar growth rule as dendrites. The authors further analyze the activity of the neuronal cultures and the resulting calcium influx. They find qualitatively different activity for different migration strengths and an exponential dependence of calcium influx on peak firing rate. Remarkably, the long-term calcium influx becomes constant suggesting calcium-dependent homeostasis. On the basis of the experiments, a model is developed that combines an established neuronal outgrowth model with a new model for neuronal migration. It allows simulation of scenarios with decreased, normal and increased neural migration and finds a remarkable similarity in the final network clustering.

While my overall impression of the paper is positive, there are some major questions and points that need to be addressed:

1) An extension of the neuritic field model incorporating neural migration already exists: Eglen, van Oojen and Willshaw (2000). It assumes repulsion between neurons, but is otherwise similar to the present one. It thus needs to be cited and discussed.

2) In the Results section, first the model is presented, then the experiments. According to the Discussion (where the order is reversed), the model has been developed on the basis of the experiments. A reverse order of presentation in the Results section would not be clearer?

3) In the experiments, the calcium influx depends exponentially on the peak firing rate (Figure 6B,D,E). In the model, however, the average firing rate is identified with calcium influx (Figure 2F). What would a plot like Figure 6B,D,E look like for the model dynamics? Might it be suitable to introduce a calcium variable as in Rohrkempter and Abbott (2007) but with a strongly nonlinear accumulation effect? It seems important to carefully relate the migration dynamics in the model (subsection “Network growth model”) to the calcium dynamics suggested by the experiment (Figure 6B,D,E).

4) In the model "connectivity, input activity and firing rates eventually converged to the same levels for different migration conditions" (subsection “Migration and neurite outgrowth shape network architecture”). This point is discussed surprisingly little. Is it not a most severe discrepancy to the experiment? Might it be possible to modify the model with an additional calcium variable to improve it (see point 3)?

5) The dendrite size in the experiments (Figure 3C) shows only a small overshoot, if any. How does this fit with the model dynamics, where the overshoot in neurite size is prominent (Figure 2D)? How does Figure 3J,K fit with the model?

6) It would be good to discuss some of current findings in more detail in the context of previous work on cultured neurons. For example: Figure 5C suggests that there is only an overshoot in activity for PKC- networks. How does this fit with Tetzlaff et al. (2010)? For the axons, previous work has often assumed a growth mechanism opposing that for the dendrites. Does the observation in Figure 3G provide evidence against such a mechanism? Do the authors find critical avalanche dynamics?

7) It is important to discuss how the in vitro results might transfer to in vivo conditions.

Reviewer #3:

This is a very interesting study that combines numerical simulations and experiments in in vitro neuronal networks. The study addresses the complex interplay between neuronal spatial arrangement and dynamics due to homeostatic regulation. The manuscript is well structured and written, and it will be definitively of interest for all the scientific community working in neuronal networks, both numerically and experimentally.

Below I list some concerns that should be addressed before publication:

1) In the Introduction, the authors write "we found that developmental clustering boosted SBE". A relatively recent study (Tibau et al., 2018) investigated the impact of aggregation on activity and functional connectivity in neuronal cultures, and pinpointed the importance of neuronal spatial arrangement. Supported by simulations, the authors showed that aggregation promoted activity and connectivity. Since Tibau's study supports the observations of the present work, I think the authors should take a look at it and mention in the Introduction or Discussion section.

2) Although the study of the authors focuses in modularity promoted by self-organization, I think they could mention the efforts in neuroengineering to shape modularity and, in turn, dictate the occurrence of SBE or the richness of activity patterns (see e.g. Bisio et al., 2014; Yamamoto et al., 2018). The fact that aggregation fosters modularity and, in turn, breaks SBE, shaping some sort of spatially-fragmented dynamics, has been observed in engineered networks (Yamamoto et al., 2018) and in self-organized aggregated networks (Teller et al., 2014). These studies can also help enriching the Discussion section.

3) Modularity is a central aspect of the present study. However, the authors do not show any modularity analysis. In the simulations, they can extract the adjacency matrix and then use the freely available Brain Connectivity Toolbox to compute the modularity index Q or similar magnitudes (see the Clustering and Community Structure section of the Brain Connectivity Toolbox). Experimentally, the authors can use the cross-correlation values of neuronal pairs interactions to build a proxy of the functional network and then compute modularity. I am aware that such an analysis may take time. Thus, if they cannot carry it out for the present article, it could be an interesting future direction.

4) In subsection “Simulating activity-dependent neurite growth and migration” (and the Materials and methods section), the authors' model is constructed by seeding neurons on the surface of a torus. I think that it is not clear for the readers the use of such a surface, particularly when trying to compare with the experiments on a 2D flat substrate. I imagine that the torus is used as a 'mathematical construction' to promote local connectivity, but it needs clarification and more details.

5) Related to this, the authors should be aware of the work by Hernández-Navarro et al. (2017), who presented a model and numerical simulations on the impact of neuronal aggregation and neurite length in shaping network connectivity, and the importance of spatial correlations inherited by neuronal spatial proximity. I think the authors should refer to that study, e.g. in the context of the explanations provided in the Results section.

6) In subsection “Migration and neurite outgrowth shape network architecture”, the authors introduce the Clustering Index CI for the first time. They need to define CI here and explain what it means. The fact that CI=1 corresponds to a homogeneous system (and 0 to a clustered) is very confusing, since "clustering index" itself suggests the opposite. The authors should at least clarify the meaning of CI and its range of variability as soon as possible in the text. I also note that the authors also use the term "degree of clustering" (e.g. in subsection “Differences in PFR reflect variations of network recruitment during SBEs”) which is 1-CI. Overall, reading can be difficult.

7) In subsection "Clustering promoted SBE initiation and increased AFRs" the authors explain the link between SBE and aggregation. This relation is very interesting. I wonder whether the experimental data can provide evidences of important differences in the spatial foci of initiation (e.g. as in Orlandi et al., 2013) in homogeneous/aggregated networks, or in the structure of propagating fronts. Can the authors elaborate on this interesting link between activity initiation and aggregation? How the structure of the spatiotemporal activity fronts change with aggregation?

8) Related to this, the authors state that SBE decreases with aggregation. This is interesting. Have the authors observed a transition from whole-network activation to partial dynamics (e.g. as in Yamamoto et al., 2018 or Teller et al., 2014)?
