# Peer review - Round 1

Editors:
- Michael Doebeli, University of British Columbia Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.36273.029](https://doi.org/10.7554/eLife.36273.029)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Trade-off shapes diversity in eco-evolutionary dynamics" for consideration by eLife. Your article has been reviewed by four peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Yaroslav Ispolatov (Reviewer #3).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that we have decided to reject your paper. However, we would like to offer the possibility of resubmission of a substantially revised manuscript. Our detailed assessment is as follows.

The paper has been carefully read by four expert reviewers. All of the reviewers found your paper thought provoking and potentially interesting. However, three reviewers raised substantial concerns. Two reviewers question the biological relevance of the models considered in the paper, and they think the model is too abstract to be useful for biologists thinking about long-term evolution. Since eLife is a "generalist" journal, it is imperative that papers have a high relevance not only for a narrow theoretical audience, but also for a general audience, in this case primarily in ecology and evolution. The reviewers also raised concerns that the work was not put into the context of existing theoretical work. In particular, one reviewer was concerned that a very similar approach has been taken in a previous paper, which is cited in the manuscript, but not discussed at all. All these concerns would need to be addressed in a revision. Specifically, the authors need to convince a mainly biological audience that the work presented is interesting and relevant, and they need to be clear about what advances the current work represents over previous work. Consequently, a serious effort would be required for revising the paper, and there is no guarantee for a positive outcome. Should you choose to resubmit a revised version, you would also need to take into account all the other reviewer comments in a constructive manner.

If you feel you can make the necessary revisions, we will make every effort to return a new version of the manuscript to the same editors and reviewers. Please note that this would be treated as a new submission.

Reviewer #1:

This is an interesting paper presenting a "minimal" model for the evolution of diversity in communities governed by competitive interactions. The model is minimal in the sense that only the outcome of interactions is modelled, but not their mechanistic basis, which greatly simplifies the description.

I have two main concerns, and a number of more technical points.

Essential revisions:

1) The work presented appears to be very similar to the theory presented in Shtilerman et al., (2015). The authors need to clarify to what extent their work is novel compared to that earlier paper.

2) In fact, I think the logistic equations presented by the authors in the appendix are similar to the ones used in Shtilerman et al., 2015. I think the authors need to consider using these equations, rather than their individual-based simulations, to derive their results. It appears to be straightforward to implement the evolutionary dynamics based on the deterministic logistic equations, with one differential equation per species, and with evolution being implemented by adding new equations to the system (and deleting those ones in which the frequency falls below a threshold). This would yield a computationally more efficient model, whose salient features would nevertheless be essentially the same as in the individual-based model (perhaps barring the nearly neutral variation within species clusters). If the results are not the same, then this needs to be known, as it would probably point to an important role of stochasticity. I think this line of analysis is necessary to obtain a complete picture of the system studied by the authors, which is required for eLife.

Essential revisions:

– Subsection “Model”: the procedure for the individual-based model is not clear: the text states that "we try 𝑁𝑖𝑛𝑑(𝑡) (number of individuals at that time step) replications of randomly selected individuals. Each selected individual of a strain 𝛼 can replicate with rate r_α…" this is imprecise; what does is it mean that an individual that has already been selected for replication replicates with a rare r_\α? Isn't it rather the case that individuals get selected to produce an offspring with a probability that is proportional to r_α?

– Also, it is not clear how the discreteness of time is dealt with exactly. For example, the paper says that each offspring is assigned a randomly selected site, then competes against the occupant of the site and probabilistically takes over. What if one offspring takes over, but then a second offspring is chosen (by chance) to compete for the same site? Is that second offspring then competing against the previous occupant, or against the new occupant, i.e., the offspring that has already taken over from the previous occupant?

– And when do individuals die? Before or after offspring production?

– The authors mention the existence of rock-paper-scissor interactions, but it is not at all clear what the importance of such interactions are for the overall dynamics of the system. Are such interactions very common, essential, just a quirk?

– Subsection “Impact of trade-off and lifespan on diversity”: it is not clear what "average cycle strength" is. Which cycles were used to calculate the average of what?

– Subsection “Impact of trade-off and lifespan on diversity”: shouldn't the average interaction strength, i.e. the average values of all I's, be ca. 0.5?

– I failed to understand Figure 2. Please explain better.

– Subsection “Impact of trade-off and lifespan on diversity”: the Darwinian demon doesn't really make sense: with no diversification, there is only one strain present, and it is impossible to say what kind of competitive ability this strain has, because no other strain is present… so what are you actually trying to say?

– I don't find the section about the relationship between tradeoff and productivity very convincing, because it is too vague. I think the authors need to be more specific and detailed here.

– Section "Frequency-dependent selection": I think a more mechanistic explanation for differences of speciation and extinction rates compared to Poisson processes is needed. What is the cause of these differences? When is this mechanism at play, and when not? In particular, why do speciation rates increase with the diversity in the system? Shouldn't this only happen at certain intermediate levels of diversity, because when the community reaches a high-level diversity, speciation rates presumably decline?

– I would like to bring the authors' attention to the recent paper by Doebeli and Ispolatov, (2017), which also presents models for community assembly and evolution of diversity are presented, with some parallels to the work discussed here. These parallels could be taken up in the Discussion section.

Reviewer #2:

The authors present a model for studying diversification dynamics as an outcome of, as they claim, competition for a single resource. I have substantial concerns regarding the insight that could be gained from this work, mainly due to the type of model and the lack of a mechanistic interpretation.

Subsection “Model” and subsection “Frequent-dependent selection”: Your trait space is Nsp-dimensional, where Nsp is the number of extant strains. In particular, the trait space grows explicitly with every strain added. Is it surprising that you get coexistence of Nsp strains in an Nsp-dimensional trait space? Further, is it surprising that "emergence of new species increases the probability for generation of further species"? It seems to me that this is quite expected, given your model. This also explains why you get these mass extinction events; there's a positive feedback loop between speciation rate and species number that is easy to recognize even without simulations.

Subsection “Generation of Diversity”: Please explain how you define "functional diversity" in your model at first mention. Appendix 6 was uninformative. The only information I found was in the caption of Figure 1, where you define functional diversity "in terms of the size of minimum spanning tree (SMST) in trait space". But your trait space is continuous ([0,1]Subsection “Generation of Diversity”: Please explain how you define "functional diversity" in your model at first mention. Appendix 6 was uninformative. The only information I found was in the caption of Figure 1, where you define functional diversity "in terms of the size of minimum spanning tree (SMST) in trait space". But your trait space is continuous ([0,1]Subsection “Generation of Diversity”: Please explain how you define "functional diversity" in your model at first mention. Appendix 6 was uninformative. The only information I found was in the caption of Figure 1, where you define functional diversity "in terms of the size of minimum spanning tree (SMST) in trait space". But your trait space is continuous ([0,1]Subsection “Generation of Diversity”: Please explain how you define "functional diversity" in your model at first mention. Appendix 6 was uninformative. The only information I found was in the caption of Figure 1, where you define functional diversity "in terms of the size of minimum spanning tree (SMST) in trait space". But your trait space is continuous ([0,1]^Nsp) so a priori there is no tree structure connecting species (apart from phylogeny). So how do you define a spanning tree, and how is this spanning tree not a function purely of the number of strains?

Subsection “Generation of Diversity”: Related to the previous point. What is a "functional niche" in your model? Since you did not discuss mechanisms underlying the interaction matrix, it is not clear what a function is.

Subsection “Generation of Diversity”: Saying your model has no geographical isolation nor resource partitioning sounds meaningless. You have not specified the underlying mechanisms for your "interaction trait", so it is hard to draw a comparison to other more mechanistic models (i.e. where the physiological/metabolic traits are explicit).

Subsection “Model”: Since replication is non-sexual, what is the purpose of defining "species" separately from "strain" in your model? In Appendix-I you mention that you define "species" operationally based on divergence time and using some arbitrary cutoff threshold, so this sounds a bit analogous to operational taxonomic units (OTUs) in microbiology. However, you model mutation/selection/growth dynamics at the strain level. Please explain early on what additional insight one may get from counting "species".

Discussion section: You claim that modeling in terms of interaction traits (which in your case means in terms of outcome probabilities of local competitive exclusion) "coarse-grains these complex systems in a natural, biologically meaningful way.". But many of your interpretations and comparisons to other models or data require translating your Abstract "interaction traits" to functions or life histories. You did not discuss at all what real traits could possibly give rise to your interaction trait matrix. Your interaction matrix seems to loosely represent competitive interactions; but then it can only explain diversity within a single trophic level (e.g. in the case of animals) or a single metabolic niche (e.g. in the case of bacteria); yet, you keep referring to "functional diversity".

Discussion section: Related to the previous comment. You say that your formulation was "chosen to reflect reasonable properties" and that you "have assumed a single, limiting resource in a well-mixed system". However, you did not provide any plausible mechanism for how such an interaction matrix could arise from competition for a single resource in a well-mixed system. This is actually a big question: how can one obtain a Nsp-dimensional trait space through competition for a single resource pool?

Reviewer #3:

The manuscript "Trade-off shapes diversity in eco-evolutionary dynamics" presents a quite original evolutionary-ecological individual-based model based on a compromise between growth rate and competitiveness. The model is simple but exhibits quite rich evolutionary properties, which, while being not entirely unpredictable, are intriguing and provide useful insights and generalizations. This combination of simplicity of the rules and relevance of the dynamics usually distinguishes successful and long-living models from the rest and makes them understandable and appealing to a wide audience. Besides, I cannot see any potentially "hidden" flaws in the model and interpretation of results that could cast doubts on the main conclusions. Thus, in my opinion, the manuscript may be published in eLife after the following and, perhaps, other comments are addressed:

1) The complexity of algebra in (3) and subsequent definition of s is definitely unwarranted by an otherwise quite accessible level of math in the rest of the paper. Furthermore, it apparently confuses even the Authors when they classify the domains of weak and strong trade-offs:

It looks like the definitions of high-tradeoff (\δ ~ 1) and intermediate trade-off (\δ ~ 1/2) are misleading. The strongest dependence of r on C appears to be when \δ=1/2, which also follows from Figure 1. The phrase "In high-trade-off phase III, any small change in C changes r drastically" is simply wrong for all but very small C. I would call both the \δ=1 and \δ=0 limits as small tradeoffs as they look perfectly symmetric, or, even better, choose another, more heuristic and transparent, form of parametrization of r vs. C.

2) Would it be possible to say anything about population dynamics of "species"? Is it cyclic?

3) At least qualitatively, what are mechanisms of mass extinction?

4) An explicit plot of diversity vs. system size (perhaps just for the δ optimal for diversity) and, ideally, an estimate of corresponding scaling, would be very revealing.

5) Similarly, how the level of diversity and the typical number of traits in a species depends on the mutation amplitude m?

6) For a general reader of eLife, the MDS algorithm needs to be explained and properly referenced. It plays a major role in interpreting the results, however, is presented only by the name of the corresponding function in R.

7) A qualitative explanation about the minimal spanning tree analysis would help as well.

Reviewer #4:

I've carefully read the paper "Trade-off shapes diversity in eco-evolutionary dynamics" by Farnoush Farahpour and colleagues. In it, they use an individual-based eco-evolutionary model to understand the emergence of community structure based on evolving interactions. The model produces some interesting patterns, such as clustering in trait-space and the evolution of intransitive competitive loops.

There are a number of aspects of this paper that I liked: the focus on evolution of interactions, the emergence of intransitive loops, the dimension reduction applied to the vector-valued traits, and the comparison with a neutral model variant. These are all creative contributions to the modeling literature.

While I was intrigued by the idea of modeling the evolution of interactions directly, it was hard for me to connect it to real ecological systems. The interactions between species are not determined by phenotypic traits of the organisms but evolve independently. It's based on an unstated assumption that species interactions are totally idiosyncratic and unpredictable. I feel that evolution in this model is too unconstrained, despite the trade-off between competitive ability and reproduction, resulting in the prevalence of intransitive loops. As a complex-systems researcher, I'm fascinated, but as an evolutionary ecologist, I'm skeptical.

The authors need to do a better job putting their work in the context of the extensive literature on eco-evolutionary dynamics. The text had many statements that had me scratching my head. Examples:

1) Framing the problem in terms of resources, but in the model there are no actual resources.

2) The competitive exclusion principle only holds at equilibrium (Armstrong, Levins) and must count resources plus shared predators (Levin, 1970).

3) The "eco-evolutionary models" cited in the Introduction seem to be just ecological models.

4) In the Introduction, the "observed eco-evolutionary dynamics" cited that the model "closely resembles" aren't empirical patterns observed in real systems, but just results of other models.

5) Discussion of speciation overlooks that the species here are clonal, so what's hard about speciation?

Also, some of the sentences throughout were hard to understand the meaning of. E.g., "Evolutionary changes at the genetic level influence ecology if they cause phenotypic variations that affect biotic or abiotic interactions of species which in turn changes the species composition and occasionally forces species to evolve their strategies."

Some of the details of the model implementation weren't clear. For example:

How exactly do births happen (subsection “Model”)?

Is mu a mutation "rate" or probability of mutation during a replication event (subsection “Model”)?

Why is lifespan drawn from a Poisson distribution (Subsection “Model”) and how can that be infinite (Figure 2)?

If each individual stays in a site, is it really well-mixed?

Does mutation of one species' interaction coefficients end up changing another species' reproduction rate through the trade-off (2)?

Could you not get at the same questions more efficiently using deterministic Lotka-Volterra dynamics?

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "Trade-off shapes diversity in eco-evolutionary dynamics" for further consideration at eLife. Your revised article has been evaluated by Ian Baldwin (Senior editor), a Reviewing editor, and 4 reviewers (the same reviewers as for the initial submission, reports below).

The reviewers agree that substantial effort was put into the revision. However, there are a number of remaining issues that call for a further in-depth revision. Reviewers 1, 2 and 3 (who was previously reviewer 4) still have substantial concerns about aspects of the paper. These concerns are all related to issues raised in the initial reports and will need to be addressed in a constructive manner if the paper is to be published in eLife.

Essential revisions:

1) Individual-based vs deterministic systems: both reviewer 1 and 4 (formerly reviewer 3) point out that it is not at all clear that these different approaches would yield different results. In other words, it is not clear that salient results reported in the paper depend crucially on the presence of noise, as appears to be the contention of the authors. This needs to be explored at least to some extent. This issue cannot be dealt with by simply "citing it away".

2) The assumption of independent evolution of the elements of the interaction matrix needs to be discussed in more detail and clarity, and in the context of biological realism. This point was raised by both reviewers 1 and 3 (formerly reviewer 4).

3) The "single resource" issue is related to point 2, and also needs a revised treatment.

4) I am sympathetic with reviewer 3's (formerly reviewer 4) concern about some of the references to previous work, particularly with regard to tradeoffs.

5) Please also address the remaining points, e.g. the definition of "species" raised by reviewer 2, as well as other minor points.

Reviewer #1:

The authors did a very good and thorough job in revising their paper. Almost all of my concerns have been addressed satisfactorily. The one remaining issue is that I don't buy the authors case for only using individual-based simulations (my original comment 2). The authors state in their rebuttal that "It has been extensively discussed in the literature that continuum approaches are unsuitable in cases of non-equilibrium dynamics,.…", and they somehow conclude from this that the deterministic Lotka-Volterra description (which in my mind is the same as a "logistic" description) would not be appropriate for the problem at hand. But that is exactly the question: in some general sense, one would expect that in the limit of large population sizes, the individual-based model used by the authors would converge to some deterministic model, and my guess is that this model would be at least close to the "mean-field" Lotka-Volterra model. It then becomes important to understand just which features of the individual-based models can be understood by studying the much simpler mean-field model. The authors present no arguments why there even are *any* features of their individual-based model that could not be observed in the deterministic model. They refer to near-neutrality, but that's exactly one of the features that was observed in similar deterministic Lotka-Volterra models by Shtilerman et al., (2015). I am not convinced that the salient results reported in this paper could not also be obtained with deterministic models. Just claiming that some results cannot be obtained in that way on general grounds does not make it true in this particular case. The obvious advantage of using deterministic models would be that such models are much more tractable analytically (e.g. from a statistical physics point of view), and it is therefore important to know how far one can get using them. I think it would not be too onerous to at least do some tests using the deterministic models to either confirm or refute the claim that they can produce similar results as the individual-based models. The question is: does stochasticity really play a major role in producing the results reported in this paper? If so, then this would be important to know (but this point would need to be made based on more than just a vague statement that their "system falls into the category of those better modeled by individual- based models"). If not, then the deterministic models should do a good job reproducing these results.

Reviewer #2:

The authors have partly addressed my concerns and those of the other reviewers. I do however still have two major concerns:

1) I agree that a low-dimensional phenotype space (e.g. pertinent to exploitation of/competition for a single resource) can give rise to an Nst x Nst interaction matrix that encodes the competitive interaction between strains. However, the crucial assumption of the authors is that each term in this matrix (well, half of the terms) can vary independently. How this could come about in reality is unclear to me.

In other words, if "P" is the underlying phenotype space (solely related to consumption of/competition for the common resource) and "I" is the space of possible interaction matrices, what could the mapping f:P->I possibly look like, such that f(P) is an Nst x Nst/2 dimensional manifold?

I strongly recommend:

(a) Avoid any comparison to "single resource" models or real systems.

(b) Acknowledge early on that an important assumption of the model is that the terms of the interaction matrix (well, half of them) can in principle vary independently (i.e. are not constrained explicitly due to genetics or ecology). Whether this assumption is met in reality is an open question.

(c) Clarify in the discussion that this paper does not address the important question of how such a high-dimensional interaction trait space (i.e. with Nst x Nst/2 independent axes) might arise, or provide a plausible example.

2) The definition of "species" by the authors is still confusing and of questionable relevance. The authors define "species" operationally based on a cutoff threshold in phylogenetic distance. While this is common practice in microbial ecology (where such clusters are called Operational Taxonomic Units), few would claim that the emergence and disappearance of OTUs is comparable to "speciation" dynamics in sexually reproducing organisms.

What I also found confusing is that in their "response to reviewers", the authors explain that "species" are "well-separated non-transient clusters in trait space". This does not align with the definition provided in their manuscript (Appendix 1), where species are defined as "clusters of strains separated by long-lasting gaps in a phylogenetic tree". Are these definitions equivalent in your model?

While the emergence of clusters in trait space is indeed interesting, I would recommend not calling these clusters "species", since clusters in trait space need not always be monophyletic and could in principle also consist of distantly related strains that happen to have converged in trait space.

Reviewer #3:

This is reviewer 4 from the original submission again. This remains an interesting yet frustrating manuscript. The authors resisted many of the good suggestions from the other reviewers and myself in how they can place their manuscript in the broader context. In the end, it's the authors' manuscript, but I still think they could do a better job in the introduction and discussion to not confuse potential readers.

To me, the most interesting part of the manuscript is the idea that species interactions might be so high dimensional that it is best to focus on interaction traits that summarize many idiosyncratic phenotypes. This is described in the discussion but should also be highlighted more in the Introduction. The relationship between phenotypic traits and interaction traits should be clarified to better address comments 1 and 6-7 of reviewer 2. Maybe could be described as a rugged "phenotype-interaction map", in analogy to the idea of "genotype-phenotype maps"? By the way, this is a big assumption of the model, not an established empirical fact, but still an interesting basis for the theory.

Reviewer 2 and I were confused by statements about limiting resources and the competitive exclusion principle. In the revision, the authors still make statements like "GLV equations model competition over renewable resources" (Subsection “Model”), "we observe high diversity in a well-mixed homogenous system without violating the competitive exclusion principle" (subsection “Trade-off anchors eco-evolutionary dynamics in physical reality”) and "we have assumed a single, limiting resource" (Subsection “Power and limitations of ITEEM”). Such statements will misdirect many readers into thinking about resource competition, R* rules, and the impossibility of coexistence of more species than resources. This is not appropriate, because in this model, the species interactions are direct (interference competition) and idiosyncratic. Allelopathy among plants or microbes would be a more relevant example than resource competition. The authors should remove all mentions about resources in the paper, because they will only confuse readers.

Concerning my previous comment 4, please don't portray other theoretical results as empirical support for your new model. Keep them clearly distinct.

It's a big stretch to say claim "life-history trade-offs" are a missing ingredient in existing theory (Introduction). Almost all existing eco-evolutionary theory is built around trade-offs. Models without trade-offs are the exception, not the rule.

The references cited in subsection “Model”, do not represent current, mainstream ecological thinking.

Reviewer #4:

I think that the authors addressed the main points from my previous review, just a few minor issues remain.

I still disagree with the definition of “strong' and “weak' tradeoff limits, seeing, for example, plots in Figure 1 as completely symmetric. In my opinion, the strongest dependence of birthrate on competitiveness happens at the line in the middle of the plot, presumably for δ=0.5. I guess it's more a terminological discussion, however, I find the definition of the strong tradeoff adopted by the Authors rather confusing.

Caption to Figure 2, “Disc diameter scales with total abundance of species' Does it mean that it scales with the number of individuals in a species? Or the number of species in the system? What kind of scaling is it?

Subsection “Generation of diversity”, “Occasionally diversity collapses from medium levels abruptly to very low levels, usually followed a recovery”, should it read “by a recovery”?

Appendix 1 (Eq.8) Is γ the index of summation, running from one to N_st? If not, what is the index?

I don't know if I should dwell on that, yet I also strongly disagree with the Authors' reply to the second comment of the first reviewer, and especially, with the apparent misuse of the term “mean field'.

In short, I believe that both implementations of this process, the individual-based and continuous-populations models should yield very similar phenomenology. Both those implementations are mean field in their nature as neither has any spatial correlations (in phenotypic or geographical space) or long temporal memory. The only difference between those is the presence of some stochasticity or noise in the individual-based model. If the Authors truly believe that such noise is the necessary source of the observed phenomenology, it should be clearly stated in the manuscript. Which, I believe, would have strongly depreciated the generality of conclusions. However, I don't think this is the case; on contrary, a continuous population version of this model would have enabled one to get “cleaner' results, speeding up the simulations and expanding the scaling range by including more species. The main distinct features that the model develops, such as temporal changes in the population, interaction cycles, speciations, etc., do not appear to be fluctuation-dominated. A minor related comment, contrary to what is said int he appendix, the per capita death rate can be included into the continuous description (which is often also called the logistic model as all elements of matrix A are negative) by simply reducing the birth rate.
