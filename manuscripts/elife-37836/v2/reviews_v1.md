# Peer review - Round 1

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.37836.017](https://doi.org/10.7554/eLife.37836.017)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: the authors were asked to provide a plan for revisions before the editors issued a final decision. What follows is the editors’ letter requesting such plan.]

Thank you for sending your article entitled "Competition for synaptic building blocks shapes synaptic plasticity" for peer review at eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Eve Marder as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

In particular, the relevance, novelty and main conclusions of the manuscript may be undermined by previous work that was not cited:

Earnshaw and Bressloff, 2006 and Earnshaw and Bressloff,.2008.

The second paper concludes, "even given a number of simplifying assumptions, it does not appear possible to obtain a global multiplicative scaling of synaptic receptor numbers along a dendrite from a simple up or down regulation of constitutive recycling." This contradicts the present study's main conclusion. See reviewer #2's comments for additional details.

Please examine these previous studies carefully and prepare a response, outlining whether these disparities can be addressed and whether the present study offers insights, results or an approach that is more relevant than this previous work.

Reviewer #1:

This paper proposes a novel mathematical model that explains the heterosynaptic plasticity in local dendrite after the induction of LTP and/or LTD. The model comprises four processes at the cellular and molecular level, which are the binding and unbinding of receptors to and from slots on postsynaptic membrane, and the addition and removal of free receptors to and from the local pool in the dendrite. The model is biophysically sound and analysed in detail to reveal how it predicts/accounts for a variety of higher level effects. For example, by quantifying the number of filled slots and the size of local pool on short timescales (i.e. shorter that biosynthesis), the model successfully predicts that:

1) On short time scales the redistribution of receptors between synapses is multiplicative, a phenomenon commonly known as synaptic scaling.

2) The amount of heterosynaptic plasticity is inversely related to the size of local receptor pool.

Transient heterosynaptic plasticity has rarely been modelled in systematically from the perspective of receptor trafficking, or in a way that highlights the role of timescale separation. This paper is accessible to experimentalists and will aid in forming experimental predictions. In particular, the model suggests that synaptic scaling can happen locally, and independently of biosynthesis on the timescales it is typically studied in experiments. In other words, synaptic scaling is simply an unavoidable consequence of having a pool of receptors with constitutive trafficking.

Issues:

To improve the presentation, the authors should reduce the number of predictions they made (some of them are almost tautologies!) to make the most important prediction stand out. These and other specific issues that should be clarified/addressed are outlined below:

- Subsection “Formulation of the model”: Need to briefly explain the physical meaning of involving p in the term αp(si – wi).

- Table 2 Scaling II: The prediction is only true in steady-state (or on average).

- Subsection “Competition for Synaptic Building Blocks Induces Multiplicative Scaling”, fifth paragraph: Three predictions may be reduced to one otherwise it could be difficult to grasp your key point. They all come from the same Equation 7 in fact, so you could keep one most important prediction in Table 2 and leave others as part of your analysis in this section.

- Subsection “Fast redistribution of receptors between synapses is multiplicative”, first paragraph: should read "the steady state solution of fast time scale".

- Subsection “Fast redistribution of receptors between synapses is multiplicative”, second paragraph: "As above" is inaccurate. F* here is clearly different from F in Equation 7, as γ=0 can no longer serve as a denominator.

- Subsection “Fast redistribution of receptors between synapses is multiplicative”, second paragraph: Articulate more explicitly. This is one of the most important predictions and therefore deserves a detailed explanation. For example, add the mathematical relationship between the size of local receptor p and the synaptic efficacy w in the quasi steady-state:

w*=p*p+p*si

- Subsection “Competition for receptors induces transient heterosynaptic plasticity”, first paragraph: Motivate it better for changing the number of slots. It is a bit out of the blue here, because until now s has never been assumed to be a temporal variable in your model.

- Subsection “Time course of homosynaptic LTP and accompanying heterosynaptic LTD”, first paragraph: Explain/justify "not reflect biological reality well".

- Suggest a clear distinction between α modulation and s modulation.

Reviewer #2:

This study fleshes out the implications of an existing idea, that multiplicative synaptic scaling of synapses could be due to competition for shared synaptic resources, identified by the authors as e.g. AMPARs.

I very much like the approach but am wary of two of the main conclusions and predictions (and also the novelty of the findings), for the following reasons:

1) A similar model was studied by Earnshaw and Bressloff across two papers (not cited in the current study):

Earnshaw and Bressloff, 2006. and Earnshaw and, 2008. The 2008 paper is particularly relevant because they studied a model that included receptor diffusion along the dendrite, where synapses competed for the same shared pool of receptors. They concluded that "even given a number of simplifying assumptions, it does not appear possible to obtain a global multiplicative scaling of synaptic receptor numbers along a dendrite from a simple up or down regulation of constitutive recycling.". The current study may have not found this for two reasons: first the Bressloff model is nonlinear, and second the Bressloff model includes space. Can the authors comment on this discrepancy? Does it undermine their whole study?

2) I find it surprising that the model predicts (Equation 6) that the total number of receptors in the pool is independent of synapse number, slot number, and receptor binding and unbinding rates (α and β). The maths makes sense – due to linearity of the model – but it would be nice if the authors could comment on the likely validity of this prediction/assumption if non-linearities were to be introduced. For example, there may be two types of receptor state within the synapse, trapped and not trapped.

Reviewer #3:

This paper represents an important intermediate level of modeling between purely abstract views of normalization and homeostasis of synapse strength and detailed biological modeling, something that is still impossible at this scale but which is being attempted in the context of the individual spine.

The authors do a good job of reaching up (top-ward) to the abstract formulation but make less of an effort to reach down (bottom-ward) to the biology. The down-reach is more difficult and will necessarily be speculative but I would encourage the authors to make this effort. This represents the essence of such a level-of-investigation bridging model: from the problem level (normalization), to algorithms, to implementations.

"In the limit of large receptor numbers" – please justify. What are the estimated numbers? What numbers are required to avoid substantial variability due to stochastics? There is brief discussion of this in the Discussion section that could be moved up.

Predictions are the eventual goal of modeling and should be given more attention. Please move the predictions of Table 2 into a major textual section and indicate how each prediction could currently (or with some imagined technical advance in the future) be tested experimentally.

Implementations determines algorithms determines problems (inverse of the Marr procedure). In this case, what is the role of catabolism of damaged receptors? Are most receptors actually returned to the pool or do many need to be replaced? What are estimates of the metabolic requirements for such replacement? How are receptors within the dendritic pool mobilized into spines? What is the involvement of endoplasmic reticulum, rough ER?

"Spreading from [nucleus by] slow diffusion process" is not really accurate; what is putative interplay of microtubules and actin vs. role of diffusion in bringing receptors into play? How might these factors relate to the role of pool mobilization in synaptic tagging and capture (STC)? Does the sudden increase in pool size in Figure 4 represent a 'capture' event?

[Editors’ note: formal revisions were requested, following approval of the authors’ plan of action.]

Thank you for sending a revision plan for your article entitled "Competition for synaptic building blocks shapes synaptic plasticity" for peer review at eLife. We are pleased to accept a final, revised version of your manuscript conditional on the essential changes outlined in the revision plan and the comments below.

Your revision plan for this article has been evaluated by 3 peer reviewers, and the evaluation is being overseen by a Reviewing Editor and Eve Marder as the Senior Editor. In addition to the revisions you have outlined, we request, in line with reviewer comments, that you address the following important issues, which were raised in the evaluation:

- "The authors should make more explicit throughout the manuscript that the analysis does not predict global synaptic scaling. This is especially important in the discussion, which links their findings to the global synaptic scaling as studied by Turrigiano et al. It seems another component of the model would need to be added to make this link; perhaps something linking the receptor pools between dendrites, or between dendrites and the soma."

- "One small point - Bressloff et al didn't assume a non-uniform distribution of synaptic receptors, that was a prediction from the model and indeed was one of the reasons that they claimed multiplicative scaling was tricky."

- "Finally there are empirical reasons to challenge the authors' assumption that synaptic receptor expression is flat within even a single dendrite. This might be OK as a simplifying assumption for a local analysis but it needs to be put in context of experimental evidence e.g. Spruston and Burrone labs have found that synaptic protein content seems to decrease from proximal to distal portions of single dendrites in hippocampal pyramidal neurons (Menon et al, Neuron, 2013; Bloss et al, Neuron, 2016; Walker et al, PNAS, 2017)."

Please resubmit a revised manuscript with the changes outlined in your revision plan as well as addressing the comments above.
