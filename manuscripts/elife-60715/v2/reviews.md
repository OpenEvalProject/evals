# Peer review - Round 1

Editors:
- Toby W Allen, RMIT University Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60715.sa1](https://doi.org/10.7554/eLife.60715.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript reports advanced molecular dynamics simulations to describe

β2 adrenergic receptor modulation, expanding significantly on existing knowledge. The study has made use of an atomistic string method to measure the effects of agonists, antagonists and inverse agonists and to understand how ligands affect GPCR activity. The authors have presented sufficient analysis to demonstrate statistical significance of the data and have made connections to experimental measurements that are well described in the revised manuscript. Overall, this is a high-level computational study of biological significance that will be impressive to many eLife readers.

Decision letter after peer review:

Thank you for submitting your article "Identification of ligand-specific G protein-coupled receptor states and prediction of efficacy via data-driven modeling" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by José Faraldo-Gómez as the Senior Editor. The reviewers have opted to remain anonymous.

Based on the reviews received, which are enclosed below, as well as a follow-up discussion amongst reviewers and editors, we regret to inform you that we cannot publish your manuscript in its current form. However, the reviewers have agreed to re-evaluate a revised version of the manuscript that convincingly addresses the concerns raised. While we encourage you to submit a revision, please note that a positive outcome is not guaranteed.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

The reviewers have appreciated many aspects of the string method solution for the allosteric modulation of the β2 adrenergic receptor, but were concerned about the reliability of the simulations, their connections to experiments and the absence of discussion on the relationship to past GPCR activation studies. Concern is expressed about the use of Emax as the sole proxy for activated conformation, as well as a lack of connection of free energy calculations to experiments. A critical point to address is the absence of a description of the statistical reliability and error estimates from the string method solutions, as well as the dependence of the converged solutions on the starting conformation. This necessitates at least one demonstration that reliable results emerge with a very different initial structure. A significantly revised manuscript would need to adequately address the above concerns to the satisfaction of the reviewers.

Essential revisions:

The full reviews have been included below. Essential revisions include:

* Proof of independence of string solutions on starting structure.

* Proof of statistical reliability and error estimates.

* Improved connections to experiments that do not rely solely on Emax values.

* Improved relationship to past studies.

Reviewer #1:

This manuscript reports advanced MD simulation to describe the allosteric modulation of the β2 adrenergic receptor, expanding on the authors' recent simulations (Biochemistry 2020, 59:880-891) that explored communication of ligand binding to the G protein-binding site via "microswitches" within the protein. This study uses the same string method to examine the effects of full and biased agonists, antagonists and inverse agonists using previously solved Xray structures. The study also calls on a series of data-based analysis methods to seek answers to the question of how different ligands communicate their changes and affect GPCR activity. Observation of stabilization of active states for agonists and inactive states for other ligands is an important achievement for MD simulation, even if reproducing known experimental results. Also, characterizing how the distribution of kinetically stabilized (active-like) states are controlled by ligands, and correlations between microswitch expectation values and cAMP response experiments are important. However, the manuscript is highly technical and jargon-based such that many readers will not follow the analysis. The statistical reliability and dependence of the converged string solutions on starting conformation do not appear to have been tested. Finally, relationship between this and the previous manuscript (Fleetwood et al., 2020), as well as how results distinguish themselves from knowledge in the field could be made more clear.

String methods are notorious for depending on starting structure as well as the number and choice of collective variables, and may converge slowly on the optimal path, if at all. The authors do not show plots of convergence (how each PMF changes over #iterations), and do not appear to undertake tests for reproducibility. i.e. Starting from very different initial structures to show that the same final pathways emerge, leading to consistent free energy profiles. For example, starting again with an initial structure for an inverse agonist instead of one for an agonist and show the same results are computed. I note that in the Discussion it is said that several simulation replicas were used to reduce error. But to what does this apply (apparently not to the swarms)? Also, collective variables (CVs) are those defined in the previous study (Fleetwood et al., 2020) but what if the set of CVs is changed or the number of CVs is reduced/increased? While I do not suggest redoing with a different set, how does the reader judge the robustness of the CV-reliant results?

The method for free energy calculation uses a transition matrix on a CV grid with stationary solution. In the subsection “Free energy estimation”, the authors cite Pan, Sezer and Roux, 2008 (and Fleetwood et al., 2020), but it is not clear that Pan, Sezer and Roux, 2008, did this, and in fact I think the first to do this from a swarms of trajectories solution was Lev et al., 2017 (see also Flood, et al., 2019), not cited here.

Having computed free energy projections along collective variables, receptor stability in relation to efficacy instead relies on estimation values for variables and not free energies, and the justifications for this could be improved. The authors write that the width and depth of the basins determine the most probable state projected into that space. This sentence is not clear, but its meaning is important, because ultimately the relative values of free energies are discussed. If the 2D maps are valid projections of the full configurational space (albeit with sampling guided/biased by the string), then Boltzmann integrals over each basin should yield a valid equilibrium constant. I presume the concern is that projections along different pairs of CVs can lead to different apparent free energies, because different CVs map out different proportions of phase space, and potentially envelop multiple states of the system, but does this mean a Boltzmann integral over a site is not a true thermodynamic quantity? In the Discussion, the authors return to add that examination of one projection can overlook what is happening in other coordinates/switches, but more discussion/justification is needed. Related, the authors state that they have "accurately captured the relative stability of states", but this is confusing given the relative stability of states from the maps appears to have been discredited.

Instead of using free energies, the authors correlate "expectation values" of their CVs to experiments in the bottom of Figure 2. I assume a plot against free energy was abandoned as it was not working as planned? Ideally one would want to see free energies plotted against experimental efficacy, because estimation values of variables such as TM5…, may correlate to efficacy, but not uniquely map to shifting state equilibrium.

Many analysis tasks were completed by existing packages for which the meanings are not obvious. e.g. Demystifying, Scikit-learn… Materials and methods, even if accepted, deserve a sentence to explain and motivate. e.g. CVs were short inverse inter-residue distances used to train a restructured Boltzmann machine (the principles of this machine could be explained simply). The subsection “Data driven analysis reveals that ligands stabilize unique states” is highly technical and not well explained. While many will know about PCA, less will be known about MDS and T-SNE. The ability to identify signaling hotspots in Figure 4 is impressive, leading to a model for allosteric communication. But the machine learning approaches used come across as black box and require better physical interpretation.

Reviewer #2:

This manuscript describes the use of enhanced sampling molecular dynamics to calculate free energy landscapes for the β2 adrenergic receptor. A particular focus is the conformational dynamics and thermodynamics of microswitches that change conformation upon receptor activation. A variety of ligands are investigated to identify shared and divergent features of receptor conformational modulation. Unbiased methods are shown to identify known conformational switches as key regulators of receptor activation.

Overall the manuscript is interesting and clearly written. Figures are very clear and well presented. The subject matter has been very extensively studied in the GPCR family as a whole and in the β2 receptor in particular, and the results presented here largely align with existing understanding of GPCR activation and conformational regulation by ligands. A major concern is the question of whether the results presented here truly enhance our understanding of GPCR activation, or simply confirm things that are already known. Many groups have published detailed analysis of similar questions to those presented here, including the Dror, Nagarajan, and McCammon groups, among others. There is very little discussion of this prior work, which makes it difficult to see how the present manuscript fits within the broader context of GPCR activation molecular dynamics analysis.

A significant technical concern is the reliance on cAMP Emax values as the sole experimental validation. A prospective experimental test of hypotheses generated here would significantly enhance the manuscript. Barring this, a more extensive comparison of computational results with experimental data is essential in my view. The cAMP pathway is highly amplified, which may confound analysis linking Emax values directly to conformational equilibria. Manglik et al., 2015, presents an actual biophysical analysis of conformational equilibria (albeit with fewer ligands) and comparison to this would be helpful. Do relative energy predictions match these experimental observations?

A smaller issue is that the utility of the results presented here appears to be a bit overstated. For example, it is claimed (Introduction) that the results provide insight into how ligands with specific efficacy profiles can be designed. To support this statement, the authors should present examples of compounds they have designed based on their results, together with experimental data confirming these molecules have the intended efficacy profiles.

Reviewer #3:

This is an interesting paper, and I like to attempt to connect analysis of allostery to function. However, I'm extremely concerned about statistical uncertainty - it's not really discussed, and it would be easy to chalk all of the results up to limited sampling. It will be important for the authors to demonstrate this isn't the case.

Basically, my concern is that there's essentially no mention of statistical uncertainty or convergence anywhere in the document. One of the major claims is that the different agonists each populate a distinct substate - this is an incredibly important and interesting observation if true, but could also be explained by saying each simulation wandered in its own space and didn't have time to explore anywhere else. If it were run again, it might wander into a totally different place. I don't have a great feel for how rapidly swarms explore, but I do know the total sampling time of 1.4 µs per ligand sounds awfully small. There are examples in the literature showing that conventional simulations several times this length are not converged as far the configurations in the ligand binding pocket go (for example, Leioatts et al., Biophysical Journal, 2015, or some of the work from Dror's group).

I have a couple of ideas for how the authors could convince me this isn't just a sampling artifact. The best would probably be to pick one ligand and redo the whole calculation 4 more times, start to finish - looking at the variation between those replicates would be a decent estimate of the uncertainty. Ideally, they'd do this for all of the ligands, but I recognize that's not a reasonable request, which is why I suggest doing it for 1 ligand.

A weaker test would be to break the individual ligand calculations into blocks, somehow - I'm not totally sure how to do it - and show that the blocks are self-similar. If they're all wandering through the whole of the blob in Figure 3, you're more likely to be ok. If each block populates a discrete chunk of the blob (and the overall swarm data doesn't revisit), then there's a big problem.

I'd want to see error estimates on the free energies in Figure 2, plus a redo of the dimension reduction in Figure 3 to see if the ligands still separate more than the replicates of 1 ligand.

On a more minor note, the use of p-values in the subsection “Ligands control efficacy by reshaping microswitches’ probability distributions”, isn't really correct. The point the authors are trying to make is that the computed value doesn't predict the experiment (for good reason), and the correlation coefficients make that point for you.
