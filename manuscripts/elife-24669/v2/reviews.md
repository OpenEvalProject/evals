# Peer review - Round 1

Editors:
- Wenying Shou, Fred Hutchinson Cancer Research Center , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.24669.043](https://doi.org/10.7554/eLife.24669.043)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Evolution of bacterial motility through a porous environment" for consideration by eLife. Your article has been favorably evaluated by Diethard Tautz (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision. Given the additional extensive revisions that the reviewers argue must be accomplished, we feel that we must reject the current submission. Under the circumstances, we would understand if you now chose to submit this work elsewhere. However, if you feel you are able to address the concerns expressed by the reviewers, you may wish to have us consider this work again in which case we would be happy to consult the same reviewers on such a new submission.

Summary:

"Evolution of bacterial motility through a porous environment" suggests that bacteria can evolve faster motility in a porous environment by executing shorter runs (avoiding collision with agar), swimming faster, and reducing cell-to-cell variability (the evolved populations had a lower growth rate than the ancestor population). The experiment was done through selecting for edge (faster-migrating) cells migrating through low-percentage agar. Given that it has been known for a long time that shorter run durations are advantageous in a porous environment (Migration of bacteria in semisolid agar. A J Wolfe and H C Berg.Proc Natl Acad Sci USA, 1989 vol. 86 (18) pp. 6973-6977), the conclusions are not surprising. Thus, we would like you to put less emphasis on this less novel aspect and acknowledge so (e.g. explicitly stating that the result is as expected). Reduction in cell-to-cell variability is potentially interesting, but we are not sure whether this is a direct consequence of faster motility. Moreover, the significance of this result seems to depend on the dataset that the observations came from (see reviewer 3 comments below).

While the authors identified some candidate mutations to explain the observed changes in behavior, they did not test any of them in an ancestral background. Thus, we don't know which mutations were necessary for the altered phenotypes. It would be very interesting to know, for example, whether one mutation was sufficient to reduce variance in the population, while another was sufficient to reduce run duration, etc. This kind of analysis would provide an obvious step forward because it would provide an understanding of how motility can be rapidly altered by selective pressures at the molecular/genetic level.

Reviewer #1:

1) Does the evolution of faster motility require a porous environment? If you propagate E. coli in a well-mixed environment (e.g. in a chemostat selecting for faster growth), will you see faster motility as a byproduct of faster growth (mutations can be pleiotropic)? More critically, if you inject E. coli in the middle of a static broth environment (no agar) and select for cells at the peripheral for >50 generations, do you expect to see faster motility? If you see faster motility, will cells not show shorter runs?

2) The authors need to do a better job characterizing growth phenotypes, especially since E. coli experience a range of growth conditions in a spatially-structured environment. I suspect that the observation that Gen 15 evolved cells show slower growth rate than ancestral cells in abundant nutrients is linked to the possibility that they may grow better than ancestral cells in limited nutrients. This kind of fitness tradeoff has been seen in many systems. You can do a chemostat competition experiment to test this. Thus, evolved cells may "beat" ancestors in two ways: they can arrive at abundant LB first, so their slower growth in abundant LB will not make much difference; and they can also grow better than the ancestor when stuck at the inner region. This may help explain how quickly they come to fixation.

Reviewer #2:

1) I particularly like the approach taken by the authors to measure single-cell swimming behavior, but wonder how the authors keep track of cells if they move out of focus. Do the authors focus on cells near glass surface? In that case cell-surface interaction will cause cells to swim in circles and suppress tumbling, which may obscure the results.

2) The authors identify tumbles based on angular velocity, "Tumbles were initiated whenever ω(t) > 6 rad s−1 and continued until ω(t) < 3.9 rad s−1. These two thresholds on ω were determined by eye and resulted in average run and tumble durations in accordance with previously published values." This criterion is different from that used in some other publications, such as Berg and Brown, 1972, where tumbles were identified by both abrupt change of velocity direction and reduction of speed (due to complete or partial loss of propulsive force when flagellar bundle disassembles). The authors obtained a mean run time of 0.42 ± 0.005 s for WT cells, almost half as much as that obtained in Berg and Brown, 1972 (0.86 s) for AW405 cells swimming in bulk fluids. I suppose this two-fold difference in run time could not be attributed to strain difference, but most likely due to the difference in definition of tumbles.

3) RP437 and AW405 strains were selected for spreading and chemotaxis capability in swimming agar plates from E. coli K-12 strain. Do RP437 or AW405 behave similarly to the evolved strains in the paper (i.e. executing runs with faster speeds but with reduced duration compared to MG1655)?

Reviewer #3:

1) In general, I enjoyed the writing style and the attention to detail in the manuscript. In particular, the experiments were solid and the controls were thorough, especially for Figure 2. However, I have trouble understanding why the authors did not propagate all lines to 15 rounds since it only involves doing 5 more plates for each line. This is especially important since a lot of subsequent analysis is carried out using the "evolved strain" that harvested from that single line of evolution after 15 rounds. Having more lines would also indicate whether or not the reduction in diversity is a general feature.

2) The modeling provides nice qualitative support to the findings about the relationship between front speed and geometry and the cells parameters but maybe takes too much place in the paper since many of the parameters were poorly constrained or taken from experiments done on other strains in different conditions. The authors are up front about this, and do a good job explaining the model, but it seems that the model is just used to say that the observed changes are probably not due to changes in growth (which they show experimentally anyway), and that there are probably other factors not accounted for in the model that are responsible for improved performance. Space could be used instead for addressing concerns mentioned above.

3) In Figure 1.the profile of intensity appears to get gradually lower from the center, and then abruptly lower to form the outer ring. I don't see how this can be compared to the simulated profile, which appears to gradually increase in intensity from the center, before forming an abruptly higher intensity ring. Is this why the profiles in Figure 3—figure – supplement 1A and D look so different from one another? Can you account for these differences? Is it due to uneven illumination in the experiment? Did the authors use an inverse scaling for the Figure 4A (dark is more cells rather than light is more cells)?

4) In the Results, the authors say that "the increase in s was reproducible across independent selection experiments", but it is hard to tell without showing the trajectory of each experiment. Figure 2D shows that on average, s increased. This is especially interesting because in Figure 3B, the round where one experiment is missing has a much smaller error bar than the other rounds. This suggests that one of the experiments was quite different from the others. Was the missing observation from the experimental replicate that had a different mutational trajectory?

5) Since tracks were cut when cells interacted with the boundary, how where the runs that were not terminated on both ends by tumbles treated (or tumbles that were not terminated on both ends by runs)? These runs (tumbles) would be of undefined length. Was the data analyzed without these undefined events?

6) Variance in the S dataset is in general greater than it is for the L dataset. The authors explain that this is due to sampling fewer run-tumble events for each individual in the S dataset. From the description, S individuals were observed for ~5 min, while L individuals were observed for ~10 min. However, there were at least 6x more individuals in S. Could the larger population size account for the increased variance? In general to assess cell-to-cell variability one should measure many cells rather than a few cells for a very long time. On a related note, the reduction in variance seems to be only significant (according to Figure 6E-H for one of the two datasets in two of the three measured parameters for which a reduction in variance is claimed (S for run speed, L for run time). Ideally, the significance of the reduction should not depend on the dataset.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for submitting your article "Environment determines evolutionary trajectory in a constrained phenotypic space" for consideration by eLife. Your article has been favorably evaluated by Diethard Tautz (Senior Editor) and three reviewers, one of whom, Wenying Shou (Reviewer #1), is a member of our Board of Reviewing Editors. The following individuals involved in review of your submission have agreed to reveal their identity: Yilin Wu (Reviewer #2), and Thierry Emonet and Adam Waite (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Fraebel et al. selected E. coli for faster migration through porous environment (low% agarose) in rich or minimal medium. Their qualitative mathematical model predicted that faster growth rate and faster run speed during chemotaxis are the most important elements in achieving faster migration through agar. They observed an evolutionary tradeoff between run speed and growth rate. In rich medium, mutations leading to improved run speed at the cost of slower growth are selected, whereas in minimal medium, mutations leading to improved growth rate at the cost of slower run speed are selected. Single mutations display these tradeoffs, suggesting antagonistic pleiotropy. Their mathematical model suggests that in rich versus minimal medium, the relative variances of the two phenotypes (growth rate and run speed) differ, which causes different evolutionary trajectories.

We all feel that the work is solid and interesting. However, we all feel that your narratives can be modified to achieve a greater level of clarity, especially regarding model-experiment comparison. We are all aware of the difficulty in modeling biological systems (especially dynamics of biological systems). Thus, a lack of great fit is not too surprising, but we do expect well thought-through explanations or even speculations on what your model explains or fails to explain.

Thus, we invite you to revise your writing in accordance with our suggestions.

Reviewer #1:

Although tradeoff between run speed and growth rate has been observed before, I do like the contrast between different outcomes in different environments. Overall, I find the paper solid and interesting. However, their narratives can be modified to achieve a greater level of clarity. I list a few examples below.

1) Authors claimed that in both rich and minimal media, their five lines evolved similarly. I am not sure that I agree with their assessment, although without error bars in graphs (Figure 1), it is tough to tell one way or another. I suggest authors add error bars (or an estimation of errors). Authors could also simply write something like "migration rates increased in all lines, though the extent of improvement differed along lines".

2) In some lines, despite selection, migration rate seemed to decline at later stages. Is that caused by genetic drift, as described by for example "Genetic drift at expanding frontiers promotes gene segregation" by Hallatschek et al.? This is a striking feature of the graph, and in my opinion, should be touched upon even if briefly.

3) You often claimed that your model qualitatively captured experiments (e.g. Figure 2—figure supplement 1). I am not sure which qualities you are referring to, especially with respect to rich medium experiments. The agreement is pretty poor in my opinion, unless I am missing something.

Reviewer #2:

This manuscript aims to address how constraints on phenotypic variation may limit the capacity of organisms to adapt to the multiple selection pressures, using Escherichia coli colony expansion in a porous environment as a model system. The authors found that a trade-off between swimming speed and growth rate that depends on the environment (rich medium versus minimal medium, in this case). They further showed that the trade-off is mediated by antagonistic pleiotropy through mutations that affect negative regulation. The paper is well-written and the results are clearly presented.

Evolutionary dynamics under multiple selection pressures have been investigated by a number of studies, some of which were cited in the manuscript. The main novelty of this paper, as the authors pointed out, is in that the selection process here involves multiple stresses simultaneously. In this regard, I hope the following point could be clarified: By selecting populations at migration front, one clearly imposes selection pressure on migration rate; but it is less clear to me whether a selection pressure on growth rate exists. Having a higher or lower growth rate does not necessarily guarantee whether a subpopulation can reach the edge, or for the specific population at colony edge, growth rate and migration rate could be uncoupled. Escherichia coli colony spreading through soft agar indeed depends on both motility and growth, but this is at the level of entire colony. Another way to impose selection pressures simultaneously on growth rate and migration rate would be: (a) grow many plates in parallel; (b) select the plate with largest colony size; (c) pool all cells on that plate for next round of propagation and selection. (Reviewing editor's comments: you can discuss that in Discussions).

Reviewer #3:

The authors have done a good job addressing my concerns from their initial submission. They have made an initially strong and interesting paper even stronger and more interesting. I am especially impressed by the thoroughness of their controls.

In general I find the comparison between model and data to be difficult to follow throughout the paper. I found myself repeatedly lost jumping between main figures and sup figures. The end result is that I had the impression that the model was vaguely useful. I think authors could do a better job at clearly explaining what the model does and does not explain.
