# Peer review - Round 1

Editors:
- Naama Barkai, Weizmann Institute of Science , Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.21415.019](https://doi.org/10.7554/eLife.21415.019)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Multiple input pathways improve perception in a MAP kinase network by enabling distributed tasks" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Naama Barkai as the Senior Editor and Reviewing Editor. The following individual involved in review of your submission has agreed to reveal his identity: Stefan Hohmann (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors use single-cell analysis to study the role of the two branches of the high osmolarity response in budding yeast. Following results of careful experiments, they suggest differential roles for the two branches: the Sln1 branch is fast and inaccurate and the Sho1 branch is slow but accurate. All reviewers found the work interesting and important.

Essential revisions:

1) Improve the writing. In particular, discuss the relation of the study with previous theoretical study (Brandman et al). In addition, the logical flow and rational for the different should be better described, so that the conclusions leading to the final model is easier to understand. Alternative explanations (e.g. extending dynamics range) should also be mentioned and discussed.

2) Test a Pbs2 over-expression strain as a way to test the assumed key role of competition between the branches for limited Pbs2.

3) Relate to the possible discrepancies mentioned in the reviews. This includes assumptions used in the model that may contrast data from literature, and possible inconsistencies between figures.

Reviewer #1:

"Multiple input pathways improve perception in a MAP kinase network by enabling distributed tasks" by Granados et al. explores the role of the two branches of the high osmolarity response in budding yeast. The authors provide evidence and suggest a model that support differential roles for the two branches of the pathway – the Sln1 branch is fast and inaccurate and the Sho1 branch is slow but accurate. They perform a number of careful single cell observations in well-controlled dynamic environments to support these claims and then extend the work by show the ramification of these effects in physiologically plausible environments. On the whole I enjoyed this work and believe it is a worthwhile contribution towards understanding the design of signaling networks and the emergent properties that can result for certain network designs. I have several points that I would be interested in seeing the authors address.

1) When I first read the Abstract of this paper I thought the authors were going to extend from the work of Brandman et al. (Science 2005). The claims in this paper are similar to the theoretical argument put forth by Brandman et al. for the potential behavior of interlinked negative feedback loops. While not emphasized, a critical feature for the Brandman paper was the need for saturation between the fast and noisy branch and the slow and accurate branch. This paper is a nice advance in that it provides a model and evidence for a practical implementation of this constraint. The authors should evaluate and discuss their contribution in relation to this paper.

2) The authors focus on the kinetics and accuracy of the two responses. Maybe, naively, it seems to me that an equally plausible explanation for the results is that the Sln1 branch responds to large deviations, while the Sho1 branch responds to small deviations – the point of the two pathways is to extend the range of concentrations over which the pathway can work. I would like to see the authors address this alternate possibility and if possible provide evidence against this alternative possibility.

3) Experimentally, it seems like the authors should be able to overexpress Pbs2. Overexpression should be able to eliminate the competition between the two branches of the pathway and the WT response would now become the linear addition of the two pathways.

4) While out of scope of this paper, it would be interesting to see what kinase dead versions of each branch of the pathway did to the overall response.

Reviewer #2:

This single cell analysis of yeast HOG pathway osmostress signalling addresses the role and collaboration of the two branches that sense osmostress and signal to the MAPKK Pbs2 and eventually the MAPK Hog1. The two branches are controlled, respectively, by the Sln1 phosphorelay system and the Hkr1-Msb2-Sho1 complex. The authors define the different branches as fast but inaccurate and slow but accurate and they provide data from well-designed microfluidic experiments as well as simulations from mathematical modelling that support this notion.

The study seems to be well performed, both experimentally and in terms of mathematical modelling. Data analysis also seems to be well developed and appropriate. The results seem to be well documented. My comments mainly concern some conceptional considerations that at least should be discussed.

The role of the two branches has been studied previously and those papers are cited. The present study adds novel information, especially with respect to the above-mentioned idea of different tasks for quick responses to acute stress versus more accurate responses to gradual changes of external osmolarity.

It seems that the authors do not mention that it has been shown that the two branches seem to have different threshold levels for osmostress.

The study suffers from the same limitations as previous studies. One of those refers to the fact that the two branches are studied in isolation, i.e. when the other branch is inactivated by mutation. Probably the two branches behave differently in such a situation. This notion is supported by the data presented here. It is still not known how the two branches operate in wild type cells because reagents to monitor Pbs2 phosphorylation/activity do not exist; it appears in fact that the Sho1 branch contributes little if anything, at least under the scenarios so far studied. This is addressed by the authors in their ramp scenario as well as their mathematical model. But the relevance of the conclusions to the actual wild type situation remains elusive.

Another limitation concerns the fact that the activity of the Slt2 pathway, which responds to opposing osmotic stress treatments and may modulate intracellular glycerol levels, is ignored in the present study (see Talemi et al. 2016). While the HOG and Slt2 pathway do not seem to directly communicate they may do so via control of glycerol accumulation (see for instance Ahmadpour et al. 2016, Baltanas et al. 2013); the Slt2 pathway hence may affect the behaviour of HOG and especially the two branches when they operate in isolation.

The study is also based on some assumptions that do not seem to be supported by data reported in the literature. For instance (Introduction, seventh paragraph) it has been reported that HOG feedback coincides with the onset of volume recovery, i.e. as soon as the cells start to recover volume, the HOG signal falls rapidly back to basal. This implies, that the sensors sense changes in volume rather than absolute volume. See for instance Babazadeh et al. 2013.

Results, first paragraph: there are additional single cell studies, some are cited elsewhere, some not: Schaber et al. 2012, Babazadeh et al. 2013, Sharifian et al. 2015 to name a few.

It appears that the authors do not explicitly mention that they chose sorbitol as osmostress agent. Most previous studies employed NaCl. The authors should justify their chose for the agent and the concentrations employed.

Reviewer #3:

The paper by Granados et al. fundamentally asks the question of how the two branches of the osmo-stress pathways coordinate to produce a rapid, yet accurate, response. The paper presents intriguing data that argues for temporal "hand-over control" from the fast (Sln1/Ssk1) branch to the slow (sho1) branch. As mentioned, the Sln1/Ssk1 is fast and dominates the early response through a bigger share of a common resource of the pathway (PBS2) and when this fast response weans away, PBS2 is liberated for the second branch, the slow one which is now handed the reins. Evidently, the presence of integral control in the slow branch is instrumental to this story, given that it is responsible for matching the perceived stress to the actual stress. As a result, this slow branch might be the major driver of response "accuracy", a hypothesis supported by some data in this manuscript.

I will jump to the bottom line here: Above is the story that I extracted from the paper after reading it multiple times, trying to circumvent distractions to this narrative such as inter-spaced descriptions of step and ramp responses, and also a meager description of the computational modeling, which in my opinion should play a more prominent role in explaining the data. The data is not intuitively obvious, and the paper as written leaves the conclusion to the imagination of the reader. The narrative is ridden with jargon ("accuracy" is such a term), and crucial primary data is not shown (the volume time trajectories, rather a correlation plot between data features that the reader never sees is shown in a major figure that is actually the most important one of this work). There is obviously important information in these data not explicitly shown, since the correlation between volume recovery and Hog1 response seems to be changing with time and the Hog1 response shown for the ssk1 mutant has a rather intriguing biphasic recovery shape at high salt concentration (Figure 3 and accompanying supplementary figures). In light of these and other confusing elements, I found myself entranced by the narrative and model proposed by the authors, but confused as to 1) whether I am interpreting it correcting, or projecting my own partial understanding), 2) if I am understanding it correctly, then the data presented and explanations provided only partially corroborate this model and 3) I truly didn't know what to do with the ramp input data, was it there to make a point that supports the model or to argue that different branches of the pathway are instrumental in different conditions?. So, my rather unorthodox recommendations are:

1) Rewrite the paper to focus on a clear narrative. What is exactly the model that the authors are proposing? Present that clearly (including why the computational model explains the data), and present the data in the order and logical sequence that actually support this model.

2) Present all the data for volume recovery, the same as presenting the data for the Hog1 nuclear residence, not summary statistics of it.

3) Bring the computational modeling to the forefront. For example, if the model I extracted out of the paper is correct, then I don't intuitively understand why the Ste11 mutant would have an identical Hog1 response to WT. I would have expected it to have the same initial response, maybe the same or similar Hog1 peak, but then the adaptation phase to be different. Why is it not? I am sure there is an explanation, but it is nowhere to be found in the manuscript. This is not a superficial point, this goes to 1) assessing the rigor and robustness of conclusions and 2) actually giving the reader information that they understand, and therefore trust.

Suggestions above only give a partial list of changes that are needed. I intended to write those as a motivation for the authors to take a deeper look at their very intriguing and beautifully collected data, and extract the most robust story out of it.

A few other concrete questions:

1) In Figure 2A, the fast activation Hog1 localization is virtually indistinguishable from the WT; however, in Figure 3A, the fast mutant loses accuracy as the recovery continues. Since the fast mutant's nuclear import of Hog1 is virtually identical to the WT, and synthesis of Gpd1 and Gpp1 has been demonstrated to be the single most important factor towards recovery (Babazadeh et al., 2014), one would expect the resulting glycerol synthesis to be similar, but this argues differently. At what point in the stress perception does this "knee-jerk" reaction fail the cell? The authors use the recovery in volume as a proxy for actual stress recovery, but this is the secondary effect from Hog1's interaction with its binding partners and glyercol production. In addition to the change in volume, I would like to see a representative promoter's activity (e.g. pSTL1-YFP) to directly observe where the breakdown in cellular perception occurs. Given the argument that the slow mutant gains in accuracy over time, I would expect to see different promoter dynamics in the two mutants in their optimal environments. This could substantiate the author's claim of the two roles the pathways play.

2) In Figure 5 (and Figure 5—figure supplement 2), the authors demonstrate an osmostress terrain that should favor the pathway that is able to integrate better – and subsequently demonstrate the "fast" pathway's disadvantage. How were these terrains chosen? Both ramps loosely resemble (and therefore could be interpreted as) ramps, and it's surprising to find the "fast" mutant at nearly a 2X disadvantage (Figure 6A). This may be something more appropriate for the supplemental, but it would be nice to see a more examples of "complex" environments that are more distinct from a classical incline ramp to really cement the accuracy vs. speed argument. What are the corresponding volume (and promoter?) dynamics, and how to they correlate with the Hog1 localization shown in Figure 5D?

3) Mitchell et al. (2015) touched upon how various waveforms are interpreted by the Hog1 pathway (i.e. high frequency is a single step; moderate frequency is a staircase; and low frequency is moderate staircase). This seems very relevant to the model the authors propose; How does the model proposed in Mitchell et al. and their work reconcile?

4) In the Discussion, the authors state "…this 'passing on' of control occurs predominately through competition for Pbs2." This is a crucial aspect of the model proposed. While this was explicitly modeled, and the resulting Hog1 dynamics matched the predictions, the sharing model of Pbs2 was never experimentally tested. The authors propose that the different spatial localizations of Sho1 and Sln1 could aid in sequestering Pbs2. Since Sho1 localizes to the region of polarized growth, they should tag Pbs2 and Sho1 and observe co-localization at the onset of osmostress. If not possible within a reasonable timeframe, then the authors should spend some time providing evidence from literature supporting this aspect, or if none exists, state that explicitly in order to set the record straight.
