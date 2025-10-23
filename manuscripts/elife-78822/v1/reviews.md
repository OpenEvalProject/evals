# Peer review - Round 1

Editors:
- Babak Momeni, https://ror.org/02n2fzt79 Boston College United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78822.sa0](https://doi.org/10.7554/eLife.78822.sa0)

This article models the evolution of simple multicellular life cycles using evolutionary game theory. The authors discuss natural selection between different life cycles by modeling growth, fragmentation, and interactions between propagules, discovering conditions for selection of a single life cycle or coexistence of multiple ones. Overall, the model is biologically intuitive, the results are rigorous, and the implications for the evolution of multicellularity are interesting.


---

# Peer review - Round 1

Editors:
- Babak Momeni, https://ror.org/02n2fzt79 Boston College United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78822.sa1](https://doi.org/10.7554/eLife.78822.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Eco-evolutionary dynamics of clonal multicellular life cycles" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Denis Tverskoi (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. Overall, the reviewers found the manuscript informative and interesting, but have the following suggestions to improve the presentation and clarity of the manuscript. In addition to the consolidated essential revisions listed below, we would highly recommend that you address all the reviewers' comments in your revision.

Essential revisions:

1) Please comment on the impact of the mechanism of interaction and discuss the forms of interactions that might be more relevant in the modeling. In the discussions, it would also be helpful to mention real biological systems that the models represent.

2) Please revise the terminology (e,g, "projection matrix", "linear dynamics", and stationary state") to avoid confusion with technical math definitions.

3) In the discussion "Similarities between models with and without group competition," please include results from models without competition as well to make the comparisons clearer for the reader.

4) Please include additional quantitative discussions and elaborate on the effect of kernel on the outcomes.

5) Please highlight the primary takeaways of the paper among many results that are derived to underscore the main findings. The reviewers suggest that you frame these questions at the beginning of your paper to help your reader follow the modeling and results.

6) Please reorganize the Discussion section to include a recap and improve its flow for your readers.

7) Please double-check the equations for accuracy and address the concerns raised by reviewer #3.

Reviewer #1 (Recommendations for the authors):

I have few comments and suggestions to improve the quality of the work:

1. The model is very clearly stated and a connection between current model and previous works has been established. The generalization of interaction between different groups are quite interesting and significant improvement in the modeling approach to the evolution of multicellular life cycles. However, it would be more instructive if the authors identify what form of interactions might be more relevant in the modeling, beside victim and killer. Also, it would be pedagogical if the above is compared, in a couple of sentences or a paragraph, with other frameworks in evolutionary game theory. To me, the model in the absence of interactions is a quasi-species equation where each group is a trait and every growth terms is similar to mutation to a new trait. A given life cycle is a mutational pathway in this analogy. The interaction term is interaction between the different types/traits. It would be instructive if authors, by making such connections with theoretical evolution literature, discuss what qualitative or qualitative changes they already expect from introducing the interactions kernel.

2. The model has a complex form, inevitably. There are several mechanisms interplaying with each other. Growth rates of groups, fragmentation patterns, interaction between groups of the same life cycle, and interaction between groups belonging to different life cycles and most often the latter two are indistinguishable. Even though the model is complex, the paper is well written and the results are clearly enough stated. However, it would be very important to improve the significance of the work by highlighting a few main messages of the paper among many results that are derived to highlight the main findings. This is the part I found somewhat unclear in the current manuscript.

3. Regarding the above comment, I want to suggest that the authors highlight, from the beginning, what questions they are trying to answer and what quantities can be calculated from the model. In principle, I expect the model says the condition for selection of a life-cycle against other ones (invasion of rare) and how it relates to model parameters. Similarly conditions for coexistence between different life cycles. Finally, the steady state values of each group abundances. These are all discussed in the paper to some extent. I just suggest highlighting the main quantities you are calculating and questions you are aiming to answer a little clearer.

4. In the case of two competing life cycles, it is not clear, to me, what is the qualitative result. The kernel is introduced in four forms suggested by the authors (Figure 2). It is concluded that depending on whether one has a killer kernel or victim kernel one life cycle wins and in other cases there might be coexistence. Are there further results? For example can one in principle states the condition for ESS or selection advantage of one life cycle?

5. (Similar to the previous comment) How does different kernels (victim or killer) improve or modify condition for selection of one life cycle while competing with another? The answer is detailed but it is useful to sum up the overall behavior cycles.

6. I want to comment that the three life cycle competition results was interesting and the analogy with rock-paper-scissor game was clarifying the findings.

7. Does the introduction of kernel term overall promotes coexistence between two life cycles?

8. While the paper has a theory approach and the generality of results justifies it, it would be very useful to connect the general finding with the observations in experimental evolution of multicellularity. For example, discuss cases where there are unique life cycles and when there are more than one.

The evolution of multicellular life cycles is a central process in the course of the emergence of multicellularity. The model suggested by authors connects evolution of multicellular life cycles to evolutionary game theory. The introduction of the interaction terms seems to be a great modeling way to discuss under what circumstances different life cycles can coexist or when one life cycle is chosen among other potential ones due to a natural selection among life cycles. The results are discussed in some details but due to complexity in some cases examples are used. I recommend this work for publication in Journal eLife after revision. It is a new model with high impact on the field of evolution of multicellular structures.

Reviewer #2 (Recommendations for the authors):

1) The first paragraph does not contain any references to back up the claims presented by the authors. It would be good to address this and add appropriate references.

2) In Figure 1 it would be good to explicitly state in the caption what the different colors for the groups mean.

3) In the discussion "Similarities between models with and without group competition "it would be good to explicitly refer to results from results from models without competition (which I think are only seen in Figure 2A) to make the comparisons clearer for the reader.

Reviewer #3 (Recommendations for the authors):

Please find my detailed recommendations for the authors below

Page 7, line 142: “The projection matrix $A$…” It is not clear to me what the authors mean by “projection matrix”. From a mathematical point of view, a square matrix $P$ is called a projection matrix if it is equal to its square, i.e. if $P^2=P$. However, it does not seem that in general $A^2 = A$.

Page 10, line 219: “Unlike the resident dynamics, the dynamics of the invader population is linear…” This dynamics is linear only if $x^{(R)}$ is constant (e.g., at equilibrium). Therefore, it would be helpful to use different notations for the function $x^{(R)}(t)$ and its value at the equilibrium $x^{(R,*)}$ in formulas 11-12 describing these dynamics.

Page 11, lines 245-246: “Numerical simulations show that an isolated life cycle always comes to the same stationary state $x^*$ from any initial distribution of group sizes.” Could you please add more details about these numerical simulations? What kind of life cycles were considered? What birth and death rates have been chosen? How was the competition matrix generated?

Throughout the text, the authors discuss the results on various special types of a competition matrix (constant, killer kernel, victim kernel). These special cases are used to obtain analytical conclusions that cannot be drawn in a general case. This helps readers deepen their intuition about this model. However, I wonder if there are any real biological systems that can be described by these special kernels? If so, it would be very helpful to include the corresponding discussion in the text.

Page 25, line 515: “In the linear model, the stationary state is an exponentially growing population…” From a mathematical point of view, a stationary state of a system is a state with all observables independent of time. Therefore, I am not sure if it is appropriate to use the term “stationary state” here.

Page 25, lines 526-529. It is not clear what does the index $s$ mean in the corresponding formulas.

Appendix A1. As was shown in the previous work, the solution to Equation (14) depends on the leading eigenvalue $\λ^*$ of the matrix $A$ and the corresponding eigenvector $w^*$. After refreshing that, the authors showed that a stationary state of the dynamics governed by Formula (21) (i.e., by Equation (14) in the case of the killer kernel) depends on $\λ^*$ and $w^*$ (see Formula (22)). This is correct. However, for each eigenvalue $\λ$ and each corresponding eigenvector $w$, Formula (22) produces a stationary state of the dynamics governed by Formula (21). It is not clear to me why, in the case of the killer kernel, the authors consider only the leading eigenvector? If such a conclusion is made on the basis of the above results for the linear case, please explain why these results can be generalized to the killer kernel.

And the last question. Is it possible that the leading eigenvalue $\λ$ has an eigenspace of dimension higher than 1 so that stationary states (22) form a “line” of equilibria?

Page 25, line 528. I guess, it should be $x_{s,j}^*$ instead of $x_{s,j}$.

Page 27, line 551-552. What is $N_0$? How is it related to $N^*$?

Section 3.2. The authors state that the dynamics are very complex in the case of competition between multiple life cycles, and therefore consider these dynamics only in some special cases. I agree that the dynamics are complex. However, as a reader, I have no intuition about how the model works in the general case, which is the most interesting question for me. Therefore, it would be helpful to add some numerical simulations exploring the above dynamics in the general case. It would also be useful to present some statistics illustrating the average number of different life cycles presented in a stationary state as well as the number of extinct ones. Maybe some life cycles are rarely observed in a stationary state, while others are widespread under a broad range of parameters and initial conditions?

Page 16, Figure 3D. If possible, could you please mark in different colours trajectories approaching different stationary states?

Lines 450-451. “Yet, it is possible to introduce a linear transformation $x \rightarrow Cy$, where $C$ is a matrix, which will make the linear term in our model diagonal.” Where is a proof that the matrix $A$ can be diagonalized?

I think the structure of the Discussion section could be improved. For example, I do not understand why you put paragraph 2 (lines 431-442) at the beginning of the Discussion? This paragraph is about a generalization of your model and its results, and it is strange to discuss the generalization of the results before discussing the results themselves. Second, it might be helpful to add a brief recap of the problem under study, and a brief overview of the model at the beginning of the Discussion section before discussing the position of your study in various contexts, and related results (lines 443-505).
