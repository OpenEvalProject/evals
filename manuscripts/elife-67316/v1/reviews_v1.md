# Peer review - Round 1

Editors:
- Agnese Seminara, University of Genoa Italy

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67316.sa1](https://doi.org/10.7554/eLife.67316.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The authors present a study on the cohesion maintenance of E. coli during collective migration in a self-generated gradient. They performed experiments and complemented the study with a predictive model and simulation to understand how bacteria with different phenotype are able to move as a cohesive group and how the individual bacterium defines its own position within the group. Particularly interesting aspects of the study are the use of titration of behavior with chemoreceptor abundance and the use of potential wells to model the attraction of bacteria to the center of their cohesive group. This approach will be of interest to physicists and biologists interested in collective motility and migration.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Spatial modulation of individual behaviors enables collective decision-making during bacterial group migration" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

We are sorry to say that, after consultation with the reviewers, we have decided that your work will not be considered further for publication by eLife.

In this paper, Bai et al. investigate through experiments and agent-based modelling how cohesion is maintained in bacterial waves on chemotactic landscapes created by nutrient consumption. The manuscript confirms that the behavior of individuals is modulated in such a way that makes cells converge towards the center of the group. Behavioral modulation in different phenotypes ensures an ordered spatial arrangement of the phenotypes. All reviewers appreciate the careful experiments and data analysis as well as the introduction of a number of technical advancements (e.g. the titration of behavior with the chemo receptor abundance, and the formalization of bacterial attraction as a potential well). However, the main results appear to confirm previous findings (Saragosti et al. 2011, Fu et al. 2018). Thus, the level of insight provided by the analysis is not sufficient to grant publication in eLife.

Reviewer #1:

In this paper, Bai et al. investigate in experiments and simulations how cohesion is maintained in chemotactic travelling waves of bacteria. These waves emerge from the bacterial population consuming an attractant, thus carving a gradient which they follow chemotactically. This paper builds up on previous work of some of the authors (Fu et al., Nat Commun 2018), which found that in these waves bacteria with varying degree of chemotactic sensitivity organize spatially in the band, which allows for its cohesiveness despite varying phenotypes. The authors investigate here an additional element for the cohesiveness of the wave: because the sharpness of the gradient increases from the front to the back of the wave, 'late' cells catch up via a stronger chemotactic response, and front cells slow down via a weaker one. This had been already postulated in earlier work on the phenomenon (Saragosti et al. PNAS 2011), but here the authors investigate how this applies to cells with varying chemotactic sensitivity. They also performed agent-based simulations of the cells behavior in the gradient and developed a model of the motion in the gradient. The latter maps the spatial dependence of the gradient steepness onto an effective travelling potential which keeps the cells together in a group as the gradient and the wave propagate. Importantly, the effective potential is predicted to be tighter for cells with higher chemotactic sensitivity, in agreement with the cell behavior they observe in experiments where the chemotactic sensitivity is artificially modulated. This suggests that weakly chemotactic cells are more weakly bound to the group and have a higher chance of being left behind. This last part is interesting in the context of range extension in semi-solid agar, where bacteria are known to be spatially organized and selected according to their chemotactic motility (Ni et al., Cell reports 2017, Liu et al. Nature 2019).

This paper builds its strengths on the extensive experimental characterization of the system and a variety of modeling approaches and makes a fairly convincing case for the way of understanding the mechanism of cohesion maintenance they propose.

From a methodological perspective, only a few points need to be addressed:

Control experiments need to quantify the cell-to-cell variability of the induction level of Tar by tetracycline.

Chemical attraction to cues released by other cells is a well-documented way to create cohesive large scale structures in E. coli (Budrene and Berg Nature 1995, Park et al. PNAS 2003, Jani et al. Microbiology 2017, Laganenka et al. Nat commun 2016). The cohesion of the wave have never been analyzed in this optic, despite being a possible alternative explanation to the gradient shape. Since the authors main claim is about the wave cohesion, they should provide evidence that such an explanation can be ruled out or considered secondary.

Possible effects of physical interactions between cells on the chemotactic response are not accounted for. The consequences should be better discussed, because they are known to influence chemotactic motility at the densities encountered in the present experiments (Colin et al. Nat commun 2019).

Additionally, the paper could better emphasize the new results and separate them from the confirmations of previous results.

1. I would highly recommend a thorough correction of the English language. Although some parts are quite fine and require only minor fix, others can be very hard to read and understand. Even when the English is fine, streamlining the presentation of the results could also improve the read considerably.

2. The discussion and the abstract are the places to better separate between confirmation of previous results and new finding, to emphasize the new findings.

3. For the possible effect of chemical cues, simulations or experiments in a Tar-only strain could be good tests.

4. The maximal density in the peak seems to be about 1% volume fraction (10^10 cells/mL, Figure 1) in the experiments. At these densities, chemotaxis is known to be affected by physical interaction between cells (Colin et al. Nat commun 2019). I would suggest additional simulation were \chi is modulated according to local density following (Colin et al. Nat commun 2019) to test whether an effect is present.

5. I would suggest to explain why agent based simulations are necessary (memory effects, etc) after the particle based simulation.

6. L216 it would be a good idea to explain the conceptual difference between VD(z) and VI(z)(=VG), and why they differ, since this is central to the analysis, and might not be obvious to all readers.

Reviewer #2:

The manuscript by Bai et al. explores the single-cell motility dynamics within a chemotactic soliton wave in E. coli. They tracked individual cells and measured their trajectory speed and orientation distributions behind and ahead of the wave. They showed cells behind the wave were moving in a more directed fashion towards the center of the wave compared to cells ahead of the wave. This behavior explains the stability of group migration, as confirmed by numerical simulations.

I do not recommend this manuscript for publication in eLife since it basically reproduces and deepens previous published works. In particular, Saragosti et al. (2011) already provided exactly what the authors claim to do here : "How individuals with phenotypic and behavioral variations manage to maintain the consistent group performance and determine their relative positions in the group is still a mystery." (Line 75-77) (See the last sentences from Saragosti et al. : "This modulation of the reorientations significantly improves the efficiency of the collective migration. Moreover, these two quantities are spatially modulated along the concentration profile. We recover quantitatively these microscopic and macroscopic observations with a dedicated kinetic model.")

What is novel here is the titration of the behavior with chemo-receptor abundance, but I believe the scope is not wide enough for publication in eLife. I suggest the authors to submit in a more specialized journal.

The authors should make more explicit what is really new in their work, compared to what is already known. In the present form, it is hard to pinpoint exactly the novelty of this research.

Reviewer #3:

The authors present a study on the collective behaviour of E. coli during migration in a self-generated gradient. Taking into account phenotypic variation within a biological population, they performed experiments and complemented the study with a predictive model used for simulation to understand how bacteria can move as a group and how the individual bacterium defines its own position within the group.

They observed experimentally that phenotype variation within the bacterial population causes a spatial distribution within the chemotactic band that is not continuous but formed by subpopulations with specific properties such as run length, run duration, angular distribution of trajectories, drift velocity. They attribute this behaviour to the chemotaxis ability, which varies between phenotypes and defines a potential well that anchors each bacterium in its own group. This was proven by the subdiffusive dynamics of the bacteria in each subgroup. Many cases were studied in the experiments and the authors present many controls to clearly demonstrate their hypothesis.

These are interesting results that prove how a discretised distribution can produce continuous collective behaviour. It presents also an interesting example in the field of active matter about collective behaviour on a large scale that is generated by a different behaviour of individuals on a much smaller scale. However, it is not clear how the subpopulations can be held together in the group. Moreover, a link between bacterial dynamics and the biological necessary mechanism is not clear.

They formulate a theoretical description based on the classical Keller-Segel model. Langevin dynamics was used to describe bacterial activity in terms of drift velocity for simulation, which agrees very well with experimental observations.

One can appreciate the interesting results of the study describing Ecoli chemotaxis as a mean-reversion process with an associated potential, but it is not clear to what extent the results can be generalised to all bacteria or rather relate to the strain the authors investigated.

1) In the Results section, lines 93-181, the authors show the results of their experiments, which essentially confirm the results of previous studies in terms of the average speed of the group and the distribution of running length and running duration from back to front within the group, as well as the angular distribution of running length. I have difficulty seeing the differences between this work and the previous studies. In fact, other studies already showed the persistence of the cell migration pathway from the back to the front as well as cells migrating faster in the back and slower in the front.

The manuscript would benefit greatly from a clear comparison between the authors' results and the previous studies.

2) However, they noted that the tumble bias is constant and not spatially modulated. This is the first difference compared to the previous studies cited, and it would be useful to have a guess or speculation about the physiological significance of this. Is the tumble bias related to the bacterial strain? Shouldn't the tumble bias be a strategy of the organism to scan the environment? Do the authors believe that tumble bias is intrinsic to the system and cannot be influenced by physiological priorities such as receptor occupancy and foraging? In the previous study, tumble bias caused faster migration in the posterior region and slower migration in the anterior region. The authors observed that in their case, the faster migration in the back and slower migration in the front was due to drift speed. How do they explain this difference in these observations?

Such aspects should be clarified if the authors intend to claim that their outcomes advance the knowledge in the field of bacterial migration otherwise they are rather considering a subcase, a special Ecoli bacteria strain.

3) The authors propose a discretisation of the chemotactic band into subgroups whose dimension is defined by the chemotactic ability with an inverse relationship to the SD γ of the bacterial distribution. Based on this idea, they suggest that each group represents a potential well. Although the idea is very interesting, it is not entirely clear to me how the bacteria can reverse to the mean of the group just because they rely on the molecular migration pathway. How is the attraction to each group generated? Would it make sense to think about the mechanism of quorum sensing, which Ecoli bacteria are known to use for population sensing? This would also explain how the exit of each group is avoided: the chemotactic ability pulls the bacteria towards the gradient, but the quorum sensing, e.g. a population sensing, drives the mechanism towards the group. This means that the driving force that causes the group to move together is the sum of at least two contributions.

4) Linked to the previous question: How are the different subpopulations kept together? Is a difference in drift velocity within a range between the back and the front sufficient to prevent the entire chemotactic group from disintegrated? Have the authors tested other drift velocity ranges to see if there is a threshold for these group dynamics? What about accounting for a molecular response?

5) In line 360, the authors claim to obtain the same subdiffusive behaviour of the bacteria when the migratory ability is influenced by the adaptation time or the basal CheY protein level. From the supplementary material, one can understand that this was the result of the simulation. For this reason, the authors should be very careful when claiming that they have observed how different proteins influence the modulation of behaviour. It is not clear from the simulation how this result can be clearly attributed to the specific protein CheY. One can choose a different protein and simulate the behaviour and get the same result without having any connection to the biological real state. I suggest that the authors explain more about this point or remove it from the text and just leave it in the supplementary material with a clear explanation about the missing connection with the biology and clarify that this is a speculation.

6) In line 104, the authors explain that the band forms after centrifugation. Their simulation shows that this happens after 20 min. What about the experiments? Is there consistency between simulation and experiments?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Spatial modulation of individual behaviors enables an ordered structure of diverse phenotypes during bacterial group migration" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

The revised manuscript addresses more clearly the novelty of the work. However, some concerns remain over novelty and new concepts introduced within the revision.

Essential revisions:

1) One main novelty the authors claim with respect to Fu et al. is they propose a mechanism for the ordering. Please clarify whether this is different from the mechanism proposed by Fu et al.

2) Explain that the wave travels because of attractant consumption. Verify with numerical simulations that the ordering persists even when the gradient is continuously modified by consumption.

3) Clarify what a pushed wave precisely is.

Please address all other points raised by the individual referees as you see fit.

Reviewer #1:

In their appeal, the authors have rewritten the text to make it significantly clearer and put the work better in context with previous publications. They also addressed my technical concerns. The main reason for rejection was however the lack of sufficient novelty. The two main points of the paper are:

1) Bringing evidence of a mechanism of wave coherence at fixed chemotactic sensitivity by an increased drift of the late cells and a reduced drift for the early ones thanks to the shape of the gradient, which the authors called mean-reversion or now pushed wave-front. This mechanism was already heavily suggested by the results of Saragosti et al. 2011 and proposed as a mechanism in that paper. On this point, I acknowledge that the presentation and analysis of the cell behavior in this paper does a better and more thorough job at demonstrating the phenomenon than the previous one, and the authors do show that this coherence holds for different values of the chemotactic sensitivity. It however remains that the results simply confirm the previously inferred mechanism, using the same experimental technique.

2) Explaining how spatial ordering allows the reconciliation of phenotypic variability and a coherent wave-front. On this point, I do not think the authors bring any new information compared to Fu et al. (2018). For instance, the mechanism for spatial ordering of the mean position of the various spatial phenotypes is already very well illustrated by Figure 3a of that paper.

The authors also reemphasized the importance of the gradient shape in maintaining the coherence of the wave. Here, and contrary to Fu 2018, they however systematically took the gradient shape as a given during simulations and did not investigate its emergence from consumption by the heterogeneous population. This diminishes the interest of the paper by this much.

All in all, I maintain my appreciation that this is technically a work of quality but its findings still remain fairly incremental, and I think it could be best suited for a more specialist journal.

Reviewer #2:

In the revised version of the manuscript, the authors satisfactorily added significant pieces of data to the whole story. They explained why their work differs from previously published data (Saragosti at all, 2011).

They improved the logical flow of the text (presentation of tracking data, stochastic modeling, agent-based modeling, titration), which now better pinpoints what is novel. They added a stochastic model to better understand the mechanisms underlying group migration.

Therefore, I recommend this manuscript for publication in eLife, provided that the authors can answer the following point.

Could the authors explain what a pushed wave is? Pushed wave/pulled wave have a clear meaning in the context of traveling waves (FKPP reaction and variants). Briefly, a pulled wave is when the per capita growth rate is the highest at the edge of the front. A pushed wave is when the per capita growth rate is the highest behind the front. Here, cells move but do not divide. This should be clarified.

Reviewer #3:

In this new version of the manuscript, authors Bai et al. offer a rewording of the text that greatly improves the understanding of their study.

They provide a new abstract that helps to explain the innovation of their results and their relevance to the biological event of cell migration.

They expand the text by adding details about their experiments, how they confirm the theoretical model and how these can improve our knowledge on collective motion of bacteria. They explain why their results are able to answer the open questions left by the studies of Saragosti 2011 and Fu 2018. In this way they discuss the differences between their study and the previous ones.

Overall, the text and the improved figures allow one to appreciate the originality of her study. Specially on the following points:

1) The analysis at the level of the individual cell and how individual behaviour can lead to collective migratory behaviour;

2) The importance of decreasing drift velocity within the chemotactic band for the collective migration of bacteria as a group;

3) The coexistence of phenotypic variability within the same migratory population and the formulation of the potential well hypothesis to explain group cohesion;

5) The adequacy of the titrated phenotype control experiment, which may also suggest a possible molecular pathway involved in the process.

The new version is able to convey the importance of the study, which is robust from an experimental point of view, with several control experiments that leave no doubt about the hypothesis that the authors draw from their observations and that are used to confirm their theoretical model. All the concerns I expressed were satisfactorily addressed.

I would suggest improving the text further so that some repetitions and mistakes are removed to make it more easy to read, and then I would suggest the manuscript for publication.
