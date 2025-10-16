# Peer review - Round 1

Editors:
- Arne Traulsen, MPI Ploen , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.07361.013](https://doi.org/10.7554/eLife.07361.013)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “The effects of a deleterious mutation load on patterns of influenza A/H3N2's antigenic evolution in humans” for consideration at eLife. Your article has been favorably evaluated by Ian Baldwin (Senior Editor) and three reviewers, one of whom served as Guest Reviewing Editor.

The paper by Koelle and Rasmussen treats the effects of deleterious mutations in the evolution of the influenza virus. This is an important aspect of influenza evolution, because traditional theory and data analysis of influenza evolution has focused on antigenic effects alone and neglected other evolutionary forces such as the genetic load caused by deleterious mutations. The dynamics analysed in this paper are complex, because they are shaped by the interplay of beneficial antigenic mutations, deleterious background mutations, and by large fluctuations in population size and absolute fitness caused by the epidemiology of the virus. The main findings are that deleterious mutations (a) change the speed and character of antigenic evolution, and (b) affect the epidemiology of influenza; in particular, they can explain the linear shape of the influenza tree.

Explaining the elegant ladder-like (‘spindly’) phylogenetic pattern of H3N2 evolution in humans has been a prize aim of infectious disease modelers for at least a decade. The authors present a thought-provoking model that emphasizes the importance of considering key antigenic substitutions within the context of a high background deleterious mutation load. The need for a very fit mutation (that causes a large antigenic change) to overcome a deleterious background also explains the punctuated nature of antigenic changes.

Some parts of the article are quite difficult to follow, and it is not clear if it is possible to reproduce the results without further explanation. Please provide a more thorough description of the model.

Essential revisions:

1) Connection to the theory of asexual evolution:

The results in the first part of the paper should be put in context of the general theory of asexual evolution. In light of this theory, the result that deleterious mutations reduce the probability of fixation for beneficial mutations is well known. This effect is contained in the theory of background selection (e.g. in the work of B. Charlesworth), as well as in travelling wave models: deleterious mutations generate fitness variance, which makes the fixation probability of a beneficial mutation strongly background-dependent (Good et al., Distribution of fixed beneficial mutations and the rate of adaptation in asexual populations, PNAS 2012). Beneficial mutations with effect size below a certain threshold fix with a reduced rate close to neutral mutations, which results in an increased average effect of fixed mutations (Good et al., PNAS 2012; Schiffels et al., Emergent neutrality in adaptive asexual evolution, Genetics 2011); specifically for influenza, the reduction of the adaptive rate due to linked deleterious mutations in non-adaptive sequence has also been observed in Strelkowa and Lässig, 2012.

It would also be good to discuss the possible consequences of epistasis in this context (if applicable).

2) Stressing the interplay between evolution and epidemiology:

In view of 1), it would be good to focus the paper more on the interplay between the evolutionary and the epidemiological dynamics, which is the novel and most interesting part of the paper. In particular, the authors find that the reduced rate and increased average effect of antigenic mutations may contribute to the linear shape of the influenza tree and to increased attack rates. However, it should become clearer that a strong pruning of antigenic mutations by the joint dynamics with deleterious mutations requires that the latter contribute a substantial fraction of the average fitness variance in the population. This may be the case in model simulations (and the results on tree shape should be compared with the relative contributions of mutation classes to fitness variance). But it is not clear for the actual system. Furthermore, we suggest the authors juxtapose their finding of the influence of deleterious mutations on tree shape with previous explanations of this characteristic.

3) The effect of deleterious mutations:

In the Discussion, the authors argue that the presence of deleterious mutations reduce clonal competition compared to populations without mutational load. We think this argument is incorrect. According to all models cited above, deleterious mutations should add to the fitness variance in the population and, hence, increase the amount of interference selection. This does not contradict the suggested pruning of antigenic mutations, because in the joint model, antigenic competition is no longer equivalent to fitness competition. The antigenic variance in the population may decrease with increasing rate or effect of deleterious mutations, even if the total fitness variance increases.

4) Connection to empirical observations and previous models:

One concern is that the model is not particularly data-driven. Although empirical trees are presented in Figure 4 to illustrate 3 pathways to antigenic change that are consistent with the model, these trees are more useful as illustrative of concepts than as good evidence for the model. The authors should stress the illustrative character of that figure.

As for (virtually) all theoretical models, it is possible that the patterns in the trees could alternatively be explained by other mechanisms. For example, in the BE92 to WU95 cluster transition, the 145N to 145K substitutions that did not take off globally (that are dead-ends) could have occurred in locations that are thought to not be global source regions (i.e. could the failure of those viruses to persist globally despite beneficial mutations relate to their emergence in less inter-connected non-source regions (i.e., other than SE Asia))? A more thorough discussion of the limits of the model would be in place. For example, in the WU95-SY97 transition, would a scenario not predicted by the model be a longer branch length? How long?

It's useful to explore how robust a flu model is to other subtypes and hosts, and the authors make an admirable attempt to consider their model in the context of influenza B and swine. However, the most natural comparison would be with seasonal H1N1, and its omission is striking here. The authors also mistakenly assume that H3N2 has similar mutation rates in different hosts, and as a result miss the opportunity to examine how well their model works in a system such as swine (a particularly good example because versions of the human H3N2 virus also circulates in pigs) which have evolutionary rates that are higher than in humans for non-surface proteins (Worobey paper) and should carry a higher mutational load than humans (Discussion, third paragraph). The swine comparison raises ecological considerations that may also relate to human demography.

In the Discussion, it would be important to describe in more detail if the competing models have fundamental issues in capturing the current knowledge or if they would be valid for other parameter choices. It seems odd to write “2%” (Discussion, first paragraph) for a model that is not described in detail and that has presumably free parameters.

5) Technical issues:

In general, it is difficult to follow the mathematical description of the model. The description is not particularly complete. For example, in Equation 3: Why does the general background death rate lead to a positive term for the change in the number of susceptible hosts? Or is it only the background death rate of infected individuals? Why does recovery not lead to a positive term here? Another example is the definition of R0,k =0, which differs from the inverse of Equation 5 only by a factor in the exponential function, or Equation 13, which is not a mere modification of Equation 6, but an extension.

The statement in the last paragraph of the subsection “Model parameters” is problematic. Equation 14 is a set of (deterministic) ODEs and thus does not give a stochastic model. It is well known that many stochastic models can be the basis of a single ODE model, so there is no unique model that the authors simulate. Are the rates in Equation 14 directly used, i.e. for a Gillespie algorithm? Or do they reflect net rates that describe the net effect of several rate processes?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled “The effects of a deleterious mutation load on patterns of influenza A/H3N2's antigenic evolution in humans” for further consideration at eLife. Your revised article has been favorably evaluated by Ian Baldwin (Senior Editor), a Reviewing editor, and two reviewers. The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

In the revised version, the authors have successfully addressed most of the comments. In particular, they have substantially improved the population-genetic side of their findings, which was one of the main concerns of the reviewers.

However, we ask the authors to be more explicit about some of the assumptions in their model. The success or failure of a beneficial antigenic mutation is a complex process, and while the authors do not need to incorporate all aspects into their model, they should be explicit about what is not being factored in:

1) The authors refer to selection as occurring on a ‘strain’, whereas in reality mutations are occurring within a swarm (quasi species) of intrahost diversity. The frequency of mutation as well as back-mutation within this swarm means that beneficial and deleterious mutations are not only arising but also being removed. The impact of a mutation on viral fitness is therefore also a product of the frequency of that mutation within the swarm. The potential bottleneck at transmission also means that not all variants, particularly low-frequency variants, will be transmitted between hosts.

2) We believe the authors are also assuming in this model a consistent immune landscape, for simplicity, which does not reflect variation in immune responses and prior exposures among hosts that affect the fitness of antigenic mutations.

Host variation can have a profound effect on the fitness of a particular mutation (as evidenced nicely by the antigenic mutations in receptor binding sites, which have very different fitnesses in hosts with different immune profiles based on whether antigenic escape or binding avidity is more important.

3) Successful H3N2 antigenic variants most frequently are produced in Southeast Asia before spreading globally. The spatial ecology of the virus has pronounced effects on which mutations succeed on a global scale and which are not sustained. It would have been simple to examine the proportion of early 145K mutations that arose in SE Asia on the phylogeny (suggested in the original reviewer comments), but short of that the importance of spatial ecology in the global success of a particular variant should be discussed (no additional analysis is required).

4) The authors should clarify that/why beneficial non-antigenic mutations were not included in the model.

5) There is still a lack of clarity and the role of competition between antigenic variants in the model. We find it hard to agree with the argument that 'rather, we propose that many of these circulating antigenic variants ultimately decline from the accumulation of deleterious mutations in the context of an only slowly changing herd immunity landscape”.
