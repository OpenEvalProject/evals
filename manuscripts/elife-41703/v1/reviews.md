# Peer review - Round 1

Editors:
- Michael J Frank, Brown University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.41703.026](https://doi.org/10.7554/eLife.41703.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for sending your article entitled "Computational mechanisms of curiosity and goal-directed exploration" for peer review at eLife. Your article is being evaluated by Michael Frank as the Senior Editor and Reviewing Editor, and two reviewers.

Summary:

The authors explore the computational mechanisms of curiosity/information-seeking, focusing particularly on the distinction between two forms of goal-directed exploration. In particular they clarify through theoretical analysis and simulations the distinction between active inference (to reduce uncertainty about which world model is valid) and active learning (reducing uncertainty about the parameters of that model; e.g., outcome distributions or state transition probabilities), both within a framework of free energy reduction. The authors also outline circumstances in which active learning and/or active inference may be exposed as a function of the environment's structure and parameterization. Overall this is original work and the topics are timely.

Essential revisions:

Despite the strengths of the manuscript, the reviewers both had substantial reservations that would need to be addressed in a revision. The two reviewer points are consolidated below.

1) The reviewers were both concerned about the lack of connection of the analysis to empirical data that could be used to constrain or falsify it. They felt that the simulations are simple enough that there should be some data out there that could corroborate their model's predictions, and that for a life sciences (instead of purely computational) journal this is important.

- For example, the authors outline clear behavioral patterns that should be observed when an animal begins a simple t-maze task with risky options, or an experiment with a disambiguating cue. Are there existing data that could help support the model's claims here? Some evidence showing that rats preferentially sample from a risky option early, but switch to the low-risk option over time would certainly seem to be available in the corpus of animal behavior literature. In so doing, the reviewers also agreed that it would be important to compare your model to some alternatives, even if not doing formal model comparison with quantitative fitting, but at least qualitatively.

2) They also both agreed that there was very little connection to neural mechanisms despite various work that has been conducted in this domain. One reviewer noted "The decision to sample a cue to infer a hidden state involves cost-benefit tradeoffs relying on specific neural substrates but these are not mentioned at all. It also involves active sensing behaviors – such as whisking, about which a lot is known – but there is no real mention of any active sensing literature. The simulations in Figure 3 predict clear-cut risk aversion but there is no discussion of the fact that animals show mixtures of risk seeking and risk aversion when tested in these conditions. Active learning and active inference are associated with different neural substrates and behaviors but this is never mentioned when discussing the two mechanisms."

3) Technically, there were also a few important concerns that would have to be addressed:

- One concern was the flexibility of the free-energy framework, and how sensitive/robust it might be with respect to initial conditions and priors. For example, the agent in the first simulation takes an initialization as specified in Figure 2. Given that the agent is tasked with updating A, how dependent are these results on the initialization of A (a0 in this case). In particular, how robust are these results to variation in the a0 prior. From the prior used here, it appears as though the agent already has some knowledge of what to expect when it samples the risky option.

- Further to the issue of the prior – how robust are these results to the reward prior specified in matrix c? Can the authors justify the use of zero reward in all non rewarding states, but a -2 reward for a state that omits a reward? Do results depend on this initialization? More traditional models would encode the omission of a reward as zero – would punishment be encoded any differently (e.g. small foot shock instead of reward omission)?

- If the model is to be used for quantification of real datasets (i.e., fitting), then it would be necessary to verify that its parameters are recoverable / identifiable.

4) Other scenarios regarding the generality of the conclusions:

- The results outlined in Figure 10 show that the agent adapts to the consistent structure found in the environment, opting not to sample the informative cue once it has determined that the risky outcome will in fact be found reliably. If the environment were switched to offer a high reward 25% of the time once the agent was confident that it would get a reward 75% of the time would it resample the cue? That is, can the agent adapt its active inference to accommodate environments with low volatility periods?

- Behavior is often associated with some cost, which complicates the decision as to whether a cue should be sampled prior to reward pursuit. Does the model behave reasonably if there's a cost associated with sampling the cue?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Computational mechanisms of curiosity and goal-directed exploration" for further consideration at eLife. Your revised article has been favorably evaluated by Michael Frank (Senior Editor), a Reviewing Editor, and two reviewers.

As you will see the two reviewers had polarized views on the merits of the paper. The main concern is that some of the connections to empirical data are misleading, and that the paper is difficult to read. After discussion with them, and reading it myself, I think the latter concern partially reflects the fact that you thoroughly responded to original concerns during the triage process and those in the reviews, which may have made the case more compelling but also the paper became a little unwieldy (and part of that is to be expected for technical papers). Thus, I am asking that you again revise the paper, but this time mostly for clarity.

Essential revisions:

My first suggestion is thus that you take a full editing pass through the paper again (perhaps offering to an arms-length colleague for comments) to try to streamline the readability – I will leave it up to you how to do this. My second suggestion is to also try to tighten up the language in reference to the empirical data that reviewer 2 found to be 'vague'. Finally, it is great that you made all code accessible so that anyone can test the properties of the model themselves, but if there are additional ways you can expose key falsifiable predictions of the theory (beyond those that are postdictions of existing data) that would be useful.

Reviewer #1:

I feel that the authors sufficiently addressed most issues that we raised with the initial manuscript. They don't offer a demonstration that model parameters are recoverable, but I agree with their argument that perhaps this isn't necessary here. My only remaining issue is that, as a paper, it feels a bit long winded and somewhat fragmented – but this is more a matter of taste than it is of publishability.

Reviewer #2:

This is a revision of a paper that tries to explain the free energy framework and its significance for exploration and exploitation. The authors responded to the requests from the previous round of reviews to include a discussion of how their data can capture empirical observations by adding 7 (!) new figures, bringing the total to 21 (!) figures in the main text.

I am afraid that, although I do appreciate their effort, this revision does little to address my concerns. This, in my view, remains an engineering paper, concerned primarily on how to make a system that generates exploration and exploitation. It is not a paper that carefully considers – or even understands – empirical work, or that provides a model that makes *falsifiable* predictions or can be tested against *competing* models of empirical results.

The discussion of empirical results that the authors added is riddled with vague and meaningless – and often entirely wrong statements. Let me give just one example from subsection “Active inference and active learning in behavior”: "This is in line with previous work on curiosity and exploration, where attention and salience have been identified as central mechanisms that modulate curiosity.…" I am quite familiar with the papers that are cited and I am positive that they said very little about how "attention" and "salience" "modulate" curiosity. I wonder what the authors mean by this. Do they mean that the papers manipulated attention and tested if people were more curious when attention was diverted one way or another? (This was not the case). Did they mean that those papers manipulate salience and test how this produces curiosity? (Again, not the case.) And so on.

This is but one example – but the paper is *full* of such statements, to the extent that I find it, quite frankly, unreadable. I am very sorry to be so negative, especially since I appreciate the work the authors put in. I return to my original opinion – this time with even more conviction after this review – that this paper is simply not suitable for an empirical journal – it is a paper about computer science and engineering.
