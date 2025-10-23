# Peer review - Round 1

Editors:
- John Rinzel, Courant Institute of Mathematical Sciences, New York University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61581.sa1](https://doi.org/10.7554/eLife.61581.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In a computational model of perceptual bistability, here binocular rivalry, a novel hierarchical structure includes an evidence accumulation stage and a competition stage that together support continuous decision-making and perceptual alternations, and account for the statistics of percept durations and serial dependencies, as well as Levelt's four propositions in the study's behavioral data. Of particular interest, feedback inhibition from the perceptual competition to the sensory evidence accumulation stage provides a gating mechanism on sensory units so that decision-making is based on evidence against the current percept.

Decision letter after peer review:

Thank you for submitting your article "Instability of visual perception reveals the dynamics of decision-making in a volatile world" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Joshua Gold as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: James Rankin (Reviewer #1); Chris Klink (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below address clarity and presentation, including some toning down of over-generalization.

This paper presents valuable advances to the modeling of perceptual bistability, here applied to binocular rivalry. The novel hierarchical structure includes an evidence accumulation stage and a competition stage that together support continuous decision-making and perceptual alternations. Importantly, the study is used to account for the statistics of percept durations and as well as Levelt's four propositions in the behavioral data.

Summary:

This paper presents an original hierarchical model for the perceptual dynamics of binocular rivalry. The model separates a stage of perceptual evidence accumulation from a stage of dominance competition and implements feedback inhibition from the competition to the evidence accumulation stage. This feedback provides a gating mechanism on sensory units so that decision-making is based on evidence against the current percept. The study demonstrates a potential neural mechanism that builds on previous models of decision-making and rivalry. Decision making in the model is continuous and leads to alternations that mimic statistical properties of behavioral perceptual bistability, including correlations from percept to percept. The authors effectively extract explanatory value from their model and its mechanisms, using analytic approximations based on statistical dynamics.

The study brings together, in the context of binocular rivalry, two existing strands of modelling perceptual bistability: capturing the statistical properties of dominance durations (a universal distribution shape independent of stimulus parameters, correlations etc) and capturing their dependence on input strengths (Levelt's propositions for binocular rivalry). The results presented go substantially beyond a long-established modelling literature.

The paper is well written and the figures clearly presented. The core results are described in a suitable style so as to keep the paper accessible to a wide readership. The later and supporting figures become more technical but this is necessary to draw out a deeper understanding as to why the model works.

We offer the following suggestions to improve the manuscript.

Essential revisions:

1. The presentation has a tone of over-generalized claims. Please keep closer to the Results – to what has been done. For example, statements about normative constraints and volatile world can be toned down. The paper does not directly assess the model's performance or auto-adjustment in dynamic and unpredictable ('volatile') environments as would be with normative modeling. Such statements do not reflect primary results and should be restricted primarily to the Discussion. They should not be in the paper's title. Please have the title refer to Binocular Rivalry. Also note: the journal eLife discourages 2-part titles with ":".

Additional data/experiments are not required if the authors drop the over-generalizations. However, if they do want to make more general claims, these should be backed up.

2. Re: Robustness of the simulation results. Some indication of model robustness should be provided to demonstrate whether all these nicely fitting dynamics do crucially depend on a precise set of parameters. Presumably in different parameter regions the model could also produce negative lag-2 correlations. Is it not just luck that the best-fit fell in a region with positive lag-2 correlations as in the data. On the other hand, are the authors able to show that if the lag-2 data is included in the fit function for the alternative model it is incapable of producing the positive correlations? These issues could be addressed in the Discussion.

Additional data/experiments are not required if the authors drop the over-generalizations. However, if they do want to make more general claims, these should be backed up..

3. Re: perceptual bistability is restricted here to binocular rivalry. Topics for the Discussion:

a. The occurrence of piecemeal or mixed percepts are not addressed. In the experiments, such perhaps are identified (with released keys) but they're not analyzed, nor modeled. Instead, bistable assemblies are assumed binary. Phenomenologically, this is definitely not the case and given existing research on mixed percepts, this should at least be discussed.

b. How does the model deal with other known binocular rivalry phenomena like flash suppression, or priming, intermittent presentation, or different time-scales? These are phenomena that were previously modeled with a strong role for adaptation. Are there any unexpected prediction the model makes beyond currently known binocular rivalry dynamics that can be tested experimentally?

c. Can the authors discuss their framework in the context of the visual system and competition between binocular and feature representations of the stimuli (in the vein of Wilson 2003)?

d. Another hierarchical model (Li, H.-H.; Rankin, J.; Rinzel, J.; Carrasco, M. and Heeger, D. Attention model of binocular rivalry P Natl Acad Sci, 2017, 114), building on the framework proposed by the cited Wilson 2003 study, proposes a descending feature-based excitation as a proxy for exogenous attention (in contrast with feedback suppression proposed here). Can the authors comment on the features of their data that this alternative mechanism might fail to capture. How could the effects of attention (or its absence) be explained by the model presented here?

4. Modeling aspects:

a. Perceptual bistability for perceptual grouping (as for ambiguous auditory stimuli) has been modeled explicitly as evidence accumulation against the current percept; please discuss and relate your approach to these: Barniv and Nelken (2015), Nguyen, Rinzel and Curtu (2020)

b. The model assumes two sets of independent bistable feature detectors. Please relate this assumption to potential brain areas and evidence that units with similar receptive fields may operate independently, as uncoupled units. (c) What other experiments on decision making (perceptual or otherwise) might this framework be able to speak to?

5. Re: specific conclusions: From one reviewer: Whilst I clearly understand what has been achieved I found it hard to pin down the specific conclusions from this study. State them explicitly, at the end of the discussion? Do not omit more specific conclusions based on this model and binocular rivalry before any other more general conclusions that draw from a wider literature.

6. The authors should post/link their model codes to a well-documented software repository. Interested readers could then see the model in action and inspect what happens internally.
