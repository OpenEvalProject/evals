# Peer review - Round 1

Editors:
- Aleksandra M Walczak, École Normale Supérieure France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66711.sa1](https://doi.org/10.7554/eLife.66711.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

The paper proposes a model, which studies an often-neglected aspect of cellular differentiation and division of labour. While the model is relatively simple, the premise and the findings are thought-provoking and this study can potentially provide the groundwork for further investigation.

Decision letter after peer review:

Thank you for submitting your article "Evolution of irreversible somatic differentiation" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: E. Yagmur Erten (Reviewer #1); Guy Cooper (Reviewer #2); George Constable (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

All reviewers found value in your work, stressed the simplicity and elegance of your model, and appreciated the insights and intuitions it provides. This elegance, however, comes at a cost. Your model relies on a key assumption, namely that cell divisions within an individual are synchronous, and that there does not seem to be within-host fitness differences between the different cell types. Reviewers questioned the biological relevance of the assumption, and we think it would be profitable to investigate further its impact on the model's results.

The discussion among reviewers also highlighted that the presentation of the model lacks details, and would need to be more precise and formalized. Reviewer #3, in particular, provides specific suggestions for the formalization of the model and leads for its analysis. I would like to encourage you to try and analyse the model, and at least to provide in the paper all elements necessary to fully understand it (in the form of equations, but also links to code). Notation should also be clarified, especially for the difference between time and cell generations, and add information about time in the notation (especially in the definition of c). The results are appealing and make intuitive sense, but careful readers need to be able to fully understand the model, and this is not the case with the current presentation of the manuscript. As the model is clarified, new questions may arise, which is why I am not making a recommendation for acceptance at this stage.

I encourage the authors to address all the comments made by the reviewers.

Reviewer #1 (Recommendations for the authors):

1. Lines 64-67: In what way the current study (model, assumptions etc.) differs from Cooper and West (2018), such that irreversible somatic differentiation is observed in this study but not in Cooper and West (2018)?

2. Lines 80-81: It is unclear at this point through what mechanism somatic cells accelerate growth. Do the organisms grow faster because somatic cells themselves divide at a faster rate, so having more of them means shorter development time? Or do the somatic cells contribute to overall resources available to all cells and every cell (including germ-role ones) divides faster? It becomes clearer later on and I think in their particular model it would not make a difference. But it would help to at least indicate that more explanation will come later.

3. Lines 125-128: The authors use a functional form (Equation 2) to determine soma cells' contribution to the growth rate. As their results depend on the shape of this function, I am wondering if there are empirical studies that support one type of form or the other. For instance, under what conditions would soma cells work better alone (Line 128)? In other words, which of these functional forms we are more likely to encounter in nature? This is later discussed to some extent, but references to the relevant literature (e.g. other models) could be useful in the Methods section as well, if a reader wanted to check other related approaches.

4. The authors refer to Appendix 3 for the first time at line 177, whereas while reading the results up to this point, I kept wondering what the fractions of the other strategies (RSD and NSD) were. In case adding the figures for RSD and NSD to the main text distracts from the main message, I think at least mentioning that they are at Appendix 3 much earlier in the Results section would help the readers.

5. Line 565: Here the authors say that large b favours ISD and a very large one promotes RSD, whereas in the main text they say "neither extremely large, nor extremely small" b favours ISD (Lines 208-209), which I found somewhat inconsistent.

6. It is not clear to me why the evolution of irreversible somatic differentiation requires a large enough organismal size. Also, in the main text, the authors do not mention what instead evolves in smaller organisms (RSD or NSD? This is later found in Appendix 3, but is not referred to or discussed in the main text). The authors later link their results about body size to some empirical examples in the Discussion section, but again, they do not discuss what might underlie these empirical observations or their findings about body size.

7. The second paragraph of the Discussion seems out-of-place as it is. I also cannot follow the logic; why do these cell numbers indicate organismal synchronicity? And what about cell death?

Reviewer #2 (Recommendations for the authors):

I like the model, it is simple and easy to interpret, providing predictions that make sense. However, it is not as general a model as the discussion implies in some cases. The predictions of the model are likely to depend on modelling assumptions that may be unrealistic in different systems, including the examples often cited in the paper.

My biggest request is that I would like more of a discussion of the limits that arise due to the these assumptions. In particular, to what extent are the predictions contingent on the fact that soma provide benefits continuously as the group grows? This is not the case for many of the systems cited in the work, such as in the Volvocine algae and in fruiting body formations such as in Dictyostelium. Furthermore, one could also imagine that differentiation probabilities are density dependent, or that germ cell fecundity depends on the number of soma cells in the last generation. I suspect that predictions 2 and 3 would not necessarily hold in these scenarios, which could explain for instance why many Volvocine species have a very large number of somatic cells. Acknowledging and discussing exactly how the predictions hinge on these assumptions would make the analysis much stronger.

Secondly, I think some definitions could be clearer in the introduction. For instance, if soma do not replicate at all, does it even make sense to speak of irreversible soma vs reversible soma? Many of the models cited have sterile soma that do not replicate (most Michod models, and Cooper and West model at least). Similarly, what if separation between germ and soma only occurs in one-generation of the group life cycle? What does the distinction between irreversible vs reversible soma mean in this case? Is irreversible soma just the same as soma sterility? How does all of this compare to the germline sequestration question, which readers may be more familiar with? These distinctions could be much clearer, which would help to set up the key question of the paper and make its scope more obvious.

Finally, I think some aspects of the presentation of the results could be improved. I found Figure 2A in isolation difficult to fully interpret. There are three outcomes in this model, ISD, RSD, and NSD, and the frequency of each outcome is only shown in Appendix 3. I would suggest including the frequency of the two other strategies in the main text. The same applies to Figure 4. You can't infer from just looking at the frequency of ISD alone to what extent the patterns are driven by irreversible soma being favoured over reversible soma vs no soma being favoured at all.

Reviewer #3 (Recommendations for the authors):

I very much enjoyed this paper, and only have a few suggestions with respect to the model.

I think potential conceptual limitations of the model lie in the assumptions of synchronous cell division and constant development strategy.

It may be possible to address the first of these issues (and thus the initial concern of Dr. Walczak) with some illustrative supplementary simulations (e.g. preliminary results to demonstrate the extent to which maturation time is affected by such asynchronicity). These might even take the form of some simple continuous time ODE models.

However the second of these issues would be a highly difficult task, and lies well outside the scope of the current paper. While exploring this question might certainly serve as a nice extension to the current work, I would not expect the authors to tackle this in the current context, where it would merely muddle the story presented.

Finally, while I like the model in general, there are some points of clarification I think could be made. Although I feel I have understood the core elements, there are some points of ambiguity where it is possible that I may be mistaken, and ironing out these potential misconceptions in the appendices would be beneficial for readers.

As I understand it:

The fraction of soma and germ cells in an organism are given by g(t) and s(t) in Equation 7, with s(t)=x in the main text (see Equation 2 – this should be made consistent?).

Note that 't' here refers to the generation t=1,2,…,n

These dynamics are independent of the costs of differentiation, cg and cs.

However, the division time for cells in the organism during growth is dependent on these costs (see 't' in Equation 1 – note that 't' here is the continuous doubling time, which has an inconsistent notation with Equations 4-8).

Writing Tgen(t) for the doubling time at generation t, we have

Tgen(t)=Fdiff * Fcomp

= (1+<c> )*( 1 – b + b ( ( x1 – s(t) )/( x1 – x0 ) ))\α

(when x0<s(t)<x1 – for simplicity I won't write out the other conditions)

At this point I'm not 100% sure how <c> is defined. I'd assume the following:

<c> = 1+s(t)*cs*(sgs + 2 sgg)+g(t)*cg*(ggs + 2 gss)

(Is this correct?)

At this point I have Tgen(t) as a function of t (having substituted for g(t) and s(t) from Equation 7). This allows me to write the maturation time (time to reach a size 2n) as

Tmat = \sumt=1n Tgen(t)

Finally, the fitness of an organism with a particular developmental strategy is given by the rate of gamete production (i.e. the number of gametes at maturity divided by the time taken to reach maturity)

W = g(n) / Tmat

Working out the evolutionary optimal strategy is then a matter of maximising W with respect to sgs, sss, ggs and gss.

Is this all correct?

If so, it may be possible to make analytical progress on this problem by replacing the discontinuous function in Equation 1 with a continuous approximation, e.g.

1 – (1 – b) x\β / ( x\β + (1 – x)\β )

I mainly mention this latter point as a potential area of future investigation. However with respect to the model details, I would recommend the authors clarify the points above in one of the appendices.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Evolution of irreversible somatic differentiation" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Aleksandra Walczak as the Senior and Reviewing Editor. The following individuals involved in review of your submission have agreed to reveal their identity: E. Yagmur Erten (Reviewer #1); Guy Cooper (Reviewer #2); George Constable (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

All reviewers note that the paper has greatly improved. However they still would like to see some small changes made to improve clarity (no new research is required). Here is a summary but please go through the reviews attached below for concrete points:

– Clarify the details of the new models, as suggested by reviewer 1;

– Define soma and germ cells clearly, as noted by reviewer 2;

– Provide more discussion on the assumption of fixed strategies, as noted by reviewer 2;

– Add clarifications as suggested by reviewer 3.

Reviewer #1 (Recommendations for the authors):

I thank the authors for their responses and clarifications, as well as for extending their model to include risky differentiation and asynchronous cell division. I very much enjoyed reading the revised version of their manuscript, but I have the following questions about the new models they included.

Risky cell differentiation (Appendix 6): I don't exactly follow why the authors multiply the frequency and not the number of cell differentiations with per differentiation death risk. Maybe I am misunderstanding something, but isn't this implicitly assuming that deadly differentiation errors, if they happen in larger organisms, will have less probability to have an impact than in smaller organisms? Or in other words, the effect of deadly differentiation will be larger in smaller organisms? If true, this assumption might still be realistic, e.g. one deadly cell within 32 cells compared to 1024 can plausibly have a larger organismal level effect. But one can also argue that if one cell becomes a mutant and acquires a growth advantage, the overall size of the organism might not matter, especially e.g. if the mutant occurs early in the development or has a very high cell proliferation/resource uptake rate. Although this might not change the results in the main text qualitatively, as there the authors use one maturity size (210) in their calculations.

Cell division asynchrony (Appendix 7): seeing the results of the cell division asynchrony, it seems like synchrony is almost a necessary condition for the evolution of irreversible differentiation in their model, just like those conditions summarized in Lines 335-339 albeit perhaps not as strict as them (since, although rarely, irreversible strategies still evolve). Perhaps it should be acknowledged as such earlier and more explicitly, rather than at the end of Discussion? Particularly given the fact that the authors looked at one of the most favourable conditions for irreversible strategies (c (s-> g) >> c(g->s)) and found that the evolution of irreversible differentiation is very rare.

Reviewer #2 (Recommendations for the authors):

I think this model and analyses are very good and so I won't comment too much on these (with the exception of a thought on the asynchrony model). I think a few things need to be clarified but I am otherwise happy to endorse the paper for publication.

My main comments will concern the introduction and framing of this study as I think that there are still things that need to be made clear, which will really help the reader right from the start.

I think some very clear definitions of different terms are needed and as early as possible in the introduction. From what I can gather across different sections of the introduction: the soma cells are those that contribute to vegetative functions (sustaining the overall organism) but cannot act as a seed/propagule/spore for founding of a new organism. In contrast, germ cells are those that do not contribute to vegetative functions but can act as such a spore. The authors distinguish between terminally differentiated soma that do not divide such as in cyanobacteria and non-terminally differentiated soma that can divide such as in the Volvocales. They then ask the question in what conditions do the latter kind of soma (non-terminally differentiated) become irreversibly differentiated (that is when they can only divide and produce more soma). If the above is correct, I would suggest making these definitions and distinctions clearer and more localised rather than having bits of each definition spread across the introduction in a way that needs piecing together (perhaps a glossary type table could also help?)

If the above is correct, then the definitions need to be applied more consistently throughout the manuscript. For instance, the "somatic" cells that exist during the growth of the "higher" Volvocales do not qualify as somatic cells per the author's definition as they do not contribute to vegetative functions. In this case only the last generation of flagella beaters are "soma", none of which divide and so the distinction between reversibly and irreversibly differentiated does not apply here. The authors have added a paragraph about this in the discussion but they lean on the Volvocales so much in the introduction and discussion of their work that this mismatch needs to be flagged much sooner in the paper.

A similar issue applies to the discussion of Cooper and West 2018. Much as I would like to pretend that this paper could potentially cover all possibilities, group growth is not explicitly modelled here and so the distinction between reversible and irreversibly differentiated soma does not apply here (one can imagine that in this model there are no cooperative interactions as the group grows and that division of labour then may occur but only in the last generation of the group life cycle before spore dispersal much like for the Volvocales). If non-sterile helpers count as soma then this might be a different issue as sterile cells may be considered irreversible soma and non-sterile helpers as reversible soma, but then these non-sterile helpers can "seed" the next generation so I don't think they really qualify as soma per the author's definition? Having clearer definitions will help resolve these confusions.

Otherwise, I feel that the authors have sidestepped the potential impact of non-static traits in their model by saying in their response to reviewers that they have plans for a future paper on this. That is great and I am very much looking forward to what they find but this issue still needs to be discussed in this paper as many of their results here could be explained as arising directly from the assumption of static strategies as the group grows. I would suggest mentioning this at least once or twice as they go through the results (around lines 238-242 would be good) and then a whole paragraph on this in the discussion is warranted (can also mention plans for future work on this here). For instance, the need for just a few somatic cells that provide large benefits seems to arise directly from the fact that germ cells can't modulate the number of soma cells they spawn once these become too numerous, or that they can't have a time based strategy that produces many soma earlier but fewer later as the group grows.

I think the results they have found in the asynchronous model is really good but needs more explanation/discussion of why ISD can't seem to work here. They have modelled a time to replication cost as arising from the different differentiation costs. I find it strange in that case that RSD is not the worst affected strategy as the authors have established that this is the strategy with the most differentiation. I otherwise would have thought that having soma cells that divert their energy to vegetative functions as the slower replicator might have been a natural way to introduce asynchrony.

Finally, I think a word of caution on the discussion of "convex" shapes and how this favours division of labour/terminal differentiation/irreversible differentiation (lines 323-332). In several of the models cited (if not all), the convexity at issue is the relationship between an individual's investment in a public good/vegetative function and the fitness return to the group. In the authors' paper, the convexity is between the number/proportion of "helpers/soma" in the group and the fitness return to the group. These are very different things (one has to do with synergy from internal efficiencies whereas as the other comes from synergies from between individual interactions) and so should not be treated as the same prediction.

Reviewer #3 (Recommendations for the authors):

The authors have made substantial changes to the manuscript that appear to have addressed many of the concerns of the reviewers.

In their response, the reviewers clarified some details of the model, and I now feel I have a better understanding as to how it works. However that has led to another couple of small suggestions on my part that I believe would help readers.

In my original review I stated:

"Note that 't' here refers to the generation t=1,2,…,n

…

However, the division time for cells in the organism during growth is dependent on these costs (see 't' in Equation 1 – note that 't' here is the continuous doubling time, which has an inconsistent notation with Equations 4-8)"

I now see that under the costless differentiation assumed in Appendix 2 , t becomes an integer which helps simplify the subsequent analysis. It's worthwhile to make a note of this fact (before the sentence "Then, the expected fractions.…" would be an obvious potential place to mention this).

The authors response also makes clear at multiple points that cell divisions are stochastic:

"Since the differentiation program is stochastic, the costs of differentiation depend on the actual number of differentiation events happened in the course of growth, rather than probabilities like ggs.",

"Since the differentiation strategy is stochastic, the time to reach maturity (Tmat) and the number of offspring at the last stage (g(n)) are random values, which we sample by repeatedly simulating the process of growth."

"However, since the outcomes of cell divisions are stochastic, the sampling of developmental trajectories has to reflect that and in our case it is done numerically."

I understand this. My comments, which I may not have articulated clearly in my initial review, were more aimed at asking how much understanding could be gained from alternatively taking a mean field approach. Indeed, this is precisely the approach the authors themselves take in Appendix 2, where they "consider the mathematical expectation of the composition". This leads to the obvious question – why can't a similar approach be used when differentiation is not costless?

Of course, I completely understand that stochasticity could be very important in a model such as this (where initial cell numbers are low), and it may be that such a mean-field approach leads to misleading results with respect to the prediction of the mean population growth rate. If this is the case, I think the authors should make a statement of this fact somewhere, perhaps with a reference to results in Gao et al., 2019 with respect to the differences between mean field and stochastic predictions.

Otherwise the authors have done a good job of clarifying my questions and addressing my concerns.
