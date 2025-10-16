# Peer review - Round 1

Editors:
- Arvind Murugan, University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67455.sa1](https://doi.org/10.7554/eLife.67455.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper shows how a common biochemical motif enables an organism to learn parameters describing the statistical structure of environmental fluctuations. The inferred parameters (here, the mean and variance) can be used to mount an adaptive response. The work shows a simple design principle to achieve control over phenotype, homeostasis and growth.

Decision letter after peer review:

Thank you for submitting your article "A simple regulatory architecture allows learning the statistical structure of a changing environment" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Rami Pugatch (Reviewer #1); Guillaume Lambert (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

1) How would results change if the threshold-linear model is replaced by a Hill function? Some discussion is currently in the SI. More discussion is needed in the main text of how all results would change if a hill function is used throughout.

2) A unified compact discussion of self-activation, non-linearity and regulator excess in the main text.

3) Discuss the cost/benefits of the proposed learning mechanisms if the environment doesn't fit the internal model discussed here – e.g., requires more than a binary on-vs-off response or environmental statistics varies very fast.

Reviewer #1:

My recommendation is a to reorganize the paper according to the following comments:

Weaknesses:

The first weakness I wish to discuss is the oversimplification of the model. The authors assume a set of parameters Di (demand) has to be tracked by a set of internal parameters Pi and define a quadratic penalty term, (which happens to be the only choice that is amenable to analytical treatment in control theory). To motivate this modeling approach they give two examples, one of which is the expression of a costly metabolic pathway that ideally should track the relevant nutrient. The problem with this model is the assumption that there is only one optimal solution P→=D→. This I think is too simplistic since (i) the dimension of the internal set of parameters π at least in the metabolic example is typically larger than the state parameters Di (even if they represent the demand for a metabolite there are typically multiple alternative supply pathways) ; (ii) The possibility of multiple solutions P1,…, Pm which are equally optimal is ignored.

For example, absence amino-acid requires expression of proteins that can metabolize these amino-acids from an inorganic nitrogen source. However, presence of both amino-acids and inorganic nitrogen source poses a dilemma to the cell, and a solution that optimize say growth rate depends subtly on both the relative concentration of the inorganic nitrogen source vs. the concentration and availability of external amino-acids, as well as the protein investment in transporting vs. making the amino-acids from scratch. If these relative concentrations fluctuate, an optimal solution in terms of growth rate can either be to ignore the amino-acids, or to ignore the inorganic nitrogen source or to express a mixture of both and this is not captured by the model presented by the authors. And there are other cases where multiple alternative pathways in metabolism are present to satisfy a given demand.

As the great William Feller used to tell his students, the best in science consists of the general embodied in the concrete. I like the general result but I urge the authors to take Feller's challenge and find a concrete example to demonstrate the merit of their approach and use it in the paper.

This biological concreteness will also solve a second weakness I found in the paper, namely the form of the nonlinear response used by the authors in the main text and in preparing the main figures (to my understanding). The nonlinearity is of the form of 'threshold-linear' response. This is not biologically feasible as there is always some upper saturation in the response. I expected to see the results presented in the main text in terms of a Michaelis-Menten (MM) or Hill function form which saturate both at low and at high concentrations. Although such cases were analyzed in the SI, it wasn't clear to me whether the main conclusions would change if such functions were used instead throughout the paper.

Since the author emphasize the role of (i) excess of regulators, (ii) self-activation, and (iii) non-linearity of the regulators, I think it is appropriate to analyze their importance in the main text. For some reason the role of self-activation was deferred to the SI.

Also, I would have liked to understand their relative importance (with realistic MM or Hill non-linearity) keeping in mind that proteins are costly for the cell to make, so a minimal excess is perhaps better.

Finally, I would expect a discussion of an hypothetical experiment, where such excess is deliberately removed by say gene deletion by the experimenter – what would be the simplest experiment that will ascertain the effect you predict be? Will a simple up-shift / down-shift will do the job?

Another more technical weakness is the statistical model being a Gaussian process. The authors claim their result is more general so I wonder how their result change for processes without time scale or to processes with power-law correlations?

A weakness in the analysis of the benefit of having such mechanisms for 'learning' the statistics of the environment requires some attention. If the environments statistics changes rapidly, or if the environment poses more complex challenges that require a response which is not all-or-none I would expect a reduction in the benefit of such a mechanism. An example that was discussed, is the case where the environment statistics varies too fast compared to the time-scale for learning a new environment statistic. It would be nice to see a simple summary of when the authors predict such a system will be advantageous for cells, considering e.g. the excess cost of building and maintaining such machinery. This naturally leads to a discussion of possible experimental verification as mentioned before.

More importantly, if we consider an ensemble of cells with such control mechanisms, their mutual interaction can lead to complex dynamics, and it is not clear if in such a setting where each cell response to the global change caused by all other cells, there is still benefit for learning the statistics which now become intertwined with the behavior of the average of all cells.

Finally, I find a weakness in the modeling of the "nominal" product feedback inhibition (PFI). It is not fair to compare to a naïve single-step PFI since actual PFI's are not single step and there is much work on the topic, see in particular the set of papers by Ned Wingreen from Princeton and his collogues.

I like the paper, and I think my comments benefits the paper. I also understand that doing it all over again might require too much effort, so I leave it to you and to the editor to think what it the best way to address my concerns. Perhaps (hopefully) some of my comments are already taken care of, and the only change is to better explain what you already did. I apologize in advance if I misread or misunderstood parts of the paper and because of that made an unnecessary comment.

I suggest you take a look at the following work:

Goyal, Sidhartha, et al., "Achieving optimal growth through product feedback inhibition in metabolism.". PLoS Comput Biol 66 (2010):, 6, 6, e1000802. Web and the PRL they cite.

I also vaguely recall Stanislas Leibler had a PNAS paper on learning with Bin Kan Xue as first author, perhaps it is relevant too.

I too had a paper that is somewhat relevant (That Kobayashi which you cite, cites in his paper) --- https://arxiv.org/abs/1308.0623

Please do not cite it unless you find it relevant, I only mention it because after reading your work I realized that I can use your method to test my formula..

Regarding the prediction issue (that such a system predicts the future and respond to the prediction which it constantly updates). This sound to me a lot like model predictive control. So I think a comparison with model predictive control literature might be in place. In particular, a clear discussion of how do you experimentally differ between non-predictive to predictive control schemes, given that most if not all of the internal variables are not measured in a typical experiment seems necessary.

Reviewer #2:

Overall, I recommend the publication of this manuscript as long as the authors address the following minor comments and suggestions.

1. A piecewise linear model for the regulator activity like the one presented in Eqn. 2c and 4c may not be biologically realistic. Although it is clear that the linear model was chosen because of the ubiquity of linear activation functions in neural networks, the authors may need to better justify why they chose a linear function, or whether it matters at all what the activity function looks like. Indeed, the authors do look into using a Hill-like function to describe the regulation of biochemical activity in section S8.2, it would be illuminating to emphasize this observation and discuss the role of choosing a specific activity function.

2. Line 389: "...but maintaining such a perfect regulatory system would presumably be costly;". Please explain why or provide a citation supporting this claim.

3. Line 777: (typo) "...acts as a senor"

Fig. 1A: Not sure what this panel is trying to show (even from the figure caption). Perhaps show a third panel above the other two where the information about the exterior is removed but the cell "sees" the same environmental composition?

Fig. 2C: The subscripts for a1 and a2 are missing.

Fig. 2E: It is unclear what the x-axis and y-axis labels are. X = and Y =

Fig. 3H: the "H" label for panel 4H is not there.

Fig. 3I+J: It is unclear how the regulator levels map back to the environment. Perhaps show a small ellipse with the correct orientation alpha (ie. -60, +30, -30, +60) in each sector, at the top of the graph, with the corresponding magnitude of each vector \sigma?.

Fig. 3J: Similarly, the main message of this panel is not very clear: several lines overlap and it is difficult to track a single one over time. Split that panel into 5 graphs arranged vertically, each showing the trace of a single regulator?

Fig. 4: Panel labels "A" and "B" are missing
