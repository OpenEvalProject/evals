# Peer review - Round 1

Editors:
- Anne-Florence Bitbol, Ecole Polytechnique Federale de Lausanne (EPFL) Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69756.sa1](https://doi.org/10.7554/eLife.69756.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Bacteria often produce toxins to fight competitors. There has been strong interest in understanding the molecular mechanisms of toxin production, release and mode of actions. Less well understood are the costs and benefits of toxin production and how natural selection acts on regulatory circuits controlling toxin production. The paper tackles this problem. Using computer simulations, the authors show that regulated toxin production is generally a better strategy than constitutive toxin production, and reciprocication is fundamental in competitions. Interestingly, reciprocication doesn't evolve into peaceful coexistence, but a strenuous battle.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your article "The Evolution of Strategy in Bacterial Warfare" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Rolf Kümmerli (Reviewer #3).

Our decision has been reached after consultation between the reviewers. Based on these discussions, we regret to inform you that we cannot accept your work for publication in eLife at present. However, if you address all the major concerns below through in-depth changes to the manuscript and new computations, we will be happy to consider a suitably revised manuscript as a new submission, that will be sent back to the same referees. Suggestions below were synthesized from the 3 reviews by the Reviewing Editor.

Summary:

Bacteria typically produce toxins to fight competitors. There has been strong interest in understanding the molecular mechanisms of toxin production, release and mode of actions. Less well understood are the costs and benefits of toxin production and how natural selection should act on regulatory circuits controlling toxin production. The paper tackles this problem. Using computer simulations, the authors show that regulated toxin production is generally a better strategy than constitutive toxin production, and reciprocication is fundamental in competitions. Interestingly, reciprocication doesn't evolve into peaceful coexistence, but a strenuous battle.

All Reviewers and the Reviewing Editor found that the paper makes important and interesting conclusions, and agreed that the model is relevant. However, there were significant reservations about methodology, and about whether the approach fully warrants the conclusions of the paper.

Essential revisions:

1) Because of the computational approach of searching parameter space of a quite complex ODE model, a clear quantitative understanding is not provided, but rather an intuition for the observed results. While the model captures the different toxin regulatory systems, which may be complicated to tackle analytically, some analytical insight would really help to demonstrate the generality of the conclusions.

For instance, an analytical model contrasting constitutive vs. regulated traits (first part of the paper), would build a stronger foundation.

2) The authors should clarify why the local versus global analysis is required. This is all the more true that the effect of spatial structure was not explored in the current paper.

If all competitions are pair-wise and the main focus are strategies that invade all other strategies and cannot be reinvaded, why is a metapopulation analysis necessary? Also, the concept is presented is presented in Figure 1, but it is not farther discussed.

The strategies that win/lose locally, but lose/win globally should be discussed to shed light on the importance of this metapopulation analysis. This might matter with regards to possible extensions of the model to spatial settings.

3) The connection to (evolutionary) game theory appears superficial. The authors should clarify this point and be particularly careful about wording when they explain the bases of their model.

In particular, the sentence "we combine evolutionary game theory with differential equation modelling" (line 20) is unfortunate. Evolutionary game theory is primarily differential equation modelling, as for instance, the replicator and replicator mutator equations are ordinary differential equations. (One exception regards finite population analysis, where tools from statistical physics enter.)

In addition, invasion analysis by itself is static game theory. It implies dynamics from stability of fixed points, but not the actual dynamics itself which is taken into account when studying evolutionary games.

4) Are the initial frequencies of the two competing populations important for the final outcome? This is related to the previous question regarding different outcomes between local and global. Also, while the model is currently deterministic, in real case scenarios noise plays a big role, so it would be good to briefly discuss this.

5) In the regulated models, the parameter constraints allow f_induced and f_initial to range between 0 and 1. But because of how the model is set-up, this means that it can happen (and it definitely does looking at Figure 2) that f_initial+f_induced=f is outside the [0,1] range, which is though the constrained range for the f of the constitutive competing strain. This might cause strange model behavior and definitely an unfair competition, so these parameters should be removed/checked.

1) The model developed in the manuscript captures the toxin regulatory system in bacteria, which is very interesting. However, the title of the manuscript and the abstract should be revised to better reflect the specific system under study.

2) The population dynamic equations in eq set 1 could be analysed further to get some analytical handle to promote our understanding. The authors could start from the following paper Vasconcelos, P., Rueffler C., 2020, How Does Joint Evolution of Consumer Traits Affect Resource Specialization? The American Naturalist 195: 331-348.

In addition, the final biomass densities used in the calculation of the invasion fitness (Eq. 2) could be further simplified by focusing on the equilibrium solutions of Eqs. 1 (perhaps under which assumptions the solutions are possible could already be interesting). Providing an expression for the invasion fitness would be a real plus.

3) Please clarify the rationale for choosing parameters in the simulations, and discuss robustness, beyond the statement "parameters of the algorithm […] are chosen to achieve short simulation times and good convergence behaviour as determined by visually inspecting the distribution of population parameters over time." (727-730)

4) Some of the findings are intuitive, as the authors acknowledge. E.g. regulated traits outperform non-regulated traits, but others are more surprising and very interesting. For example, many toxins are quorum-sensing regulated (e.g. phenazines in P. aeruginosa). But the authors show that this is not an ideal mechanism because a strain might be killed before it's reaching a high enough density to switch on QS-regulated toxins. I'd like to see a more detailed discussion on this putative mismatch. Related to this, my intuition is that the three mechanisms might work in concert, i.e. a toxin is QS controlled, but the threshold for QS activation is lowered by competition sensing. This would be interesting to discuss.

5) The conclusion on lines 32-35 is strong. It might apply to mixed conditions as simulated here. However, in spatially structured habitats reciprocal fighting might lead to co-existence as competitors manage to defend their 'territories' and fighting only occurs at the borders. The swift elimination of competitors is maybe less common than assumed in real-world set ups.

6) The argument is that toxin sensing works best as the winner switches off toxin production once the competitor is eliminated. However, toxins might outlast their producers, such that the switching off might take longer than assumed. Can the authors comments on this?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your revised article "The evolution of strategy in bacterial warfare: quorum sensing, stress responses, and the regulation of bacteriocins and antibiotics" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Rolf Kümmerli (Reviewer #2).

Both reviewers are very positive about your revised manuscript and recommend publication. However, both reviewers and the reviewing editor agree that one revision would improve your manuscript. Therefore, we would like to ask you to do this revision before we accept your manuscript for publication.

Essential revision:

While the motivation for the local vs. global analysis is well explained, the results from this analysis should be clarified. In figure 1, interesting examples are proposed of strategies that might win/lose locally and then lose/win globally. These are very interesting cases that point at non-trivial competition dynamics. It would be important to add a figure or table (perhaps in the supplement) and an associated discussion paragraph where it is shown that doing this additional meta-population analysis is necessary and adds something to the local competition part. The aim of this addition would be to address the following question: Would the optimal strategy change if one didn't do the global competition step? Some statistics of counter-intuituive scenarios explored, based on their classification in figure 1d, would address this point.

Reviewer #1 (Recommendations for the authors):

The manuscript puts forward exciting hypotheses about the strategies of toxin production in bacteria, which would be very interesting to test experimentally. Also, future work that tries to shed deeper analytical insight in the results would undoubtedly be very interesting.

I think the work is definitely worth publication. I find the presentation of the results sometimes difficult to follow, partially because the details of the models, which is very helpful to understand the results, is detailed at the end of the paper in the methods. But probably this is unavoidable given the format.

I believe the current version of the manuscript reads better and clarifies some of the misunderstandings in previous versions. There are, however, some criticisms that have not, in my opinion, been well addressed.

1) I appreciate the complexity of the model and the strengths that come with including this complexity. The new analytical work carried out to investigate stability of the fixed points helps towards the analytical interpretation of the results. I think, however, the criticism previously raised by the reviewers was trying to determine whether a simpler model, analytically tractable, would be able to reproduce some of the results showed here, while giving more analytical insight. I don't think the manuscript currently addresses this issue. On the other hand, I also think that it can be left to future work as it is a very interesting and challenging research direction.

2) I am satisfied with the motivation behind the local versus global analysis, which I think is very important, especially in potential future applications to spatial settings of this work. The motivation behind the analysis was never in question. What I don't understand are the results from this analysis. In figure 1, interesting examples are proposed of strategies that might win/lose locally and then lose/win globally. These are very interesting cases that point at non-trivial competition dynamics that would be interesting to investigate further in future work, but I don't see these cases discussed anywhere in the results. I understand that the results of the algorithm come from a sequence of local competition, dispersal, seeding, etc…, that include this metapopulation competition, but I would like to see a figure/paragraph/discussion where it is shown that doing this additional meta-population analysis adds something to the local competition part. Would the optimal strategy change if one didn't do the global competition step? If the answer is yes, which I imagine it is, where do I see this?

Reviewer #2 (Recommendations for the authors):

The authors have done a very good job in revising their paper. The main issue that arose during the first round of reviewing was the lack of an analytical model to establish a stronger foundation of the principles of competition sensing. Although it was not me who brought up this issue, I have consulted the authors' responses, edits in the main paper and extra analysis in the supplements with great care. My opinion is that the authors have convincingly solved the debate. There is simply no possibility to device an analytical model that captures even the simplest regulatory circuits involved in competition sensing and toxin production. The most important thing is that the authors have not only used verbal arguments to make their point, but have immensely invested in analytical modelling to show why the approach does not work. I believe that the strength of the paper is its biological realism and the fact that it generates predictions that can be empirically tested.

Moreover, the authors have adequately addressed my own comments. The discussion on interactions between regulatory mechanisms and the role of ecology have significantly improved the paper. The addition on local vs. global interactions is also important, especially for non-specialist readers.
