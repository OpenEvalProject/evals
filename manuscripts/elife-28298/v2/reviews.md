# Peer review - Round 1

Editors:
- Bruno Lemaître, Ecole Polytechnique Fédérale de Lausanne Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.28298.032](https://doi.org/10.7554/eLife.28298.032)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Stochastic variation in the initial phase of bacterial infection predicts the probability of survival in D. melanogaster" for consideration by eLife. Your article has been favorably evaluated by Wendy Garrett (Senior Editor) and three reviewers, one of whom, Bruno Lemaître (Reviewer #1), is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: Andrea Graham (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This elegant and thorough study provides rigorous quantitative dissection, under controlled environmental conditions, of the contributions of host and pathogen genetics plus random individual variation – in this case, stochasticity in the infection process itself – to the dynamics and outcome of infection. The authors make excellent use of the tools available for Drosophila, including isogenic lines and immune knockouts, as well as a wide array of bacterial species. They are therefore able to quantify variation among pathogen species in odds of killing the host, in the set point bacterial load, and in the consistent bacterial burden at which death occurs (regardless of the time at which that threshold burden is reached, interestingly). Likewise, their extensive empirical data show variation among host species and isogenic lines in bacterial load upon death, which appear independent of inoculum size and immune deficiency. The authors go on to show that stochastic variation within many of their host-pathogen pairings leads to bimodal outcomes: death or chronic infection. The authors explain this bifurcation as a race between rates of bacterial proliferation and immune response induction. The evolutionary implications of this are clear – e.g., selection on rates of immune response induction or bacterial proliferation. Indeed, evolutionary biologists, ecologists, microbiologists, physiologists, and immunologists working in all sorts of biological systems will be intrigued and inspired by this array of findings.

There are, however, a number of important issues to clarify before considering this paper for publication.

Essential revisions:

1) Impact of initial conditions:

A) In particular, the overall conclusion is that variations in the timing of initiating the humoral immune response (tc) determine the ultimate fate of infected animal – either death or survival with chronic infection. One trivial possibility that is not directly addressed is that (small) differences in initial inoculation (with little or no variation in the tc) are actually responsible. This would be consistent with data present in Figure 2—figure supplement 1, and the mathematical model presented, without postulating variation in tc. It seems that empirically determined initial dose is only reported in one figure panel (Figure 5D). Given the variation in the pulled capillary needle and the injection device, how can the authors be certain small variations don't tip the balance?

1B) While it looks like that all individual flies were treated identically, another parameter that is clearly different for each individual fly is the exposure to CO2 during manipulations/injection. It is probable that those flies that were injected first (had lower exposure to CO2) in the end were survivors, while those injected last (had longer exposure to CO2) succumbed. This should be experimentally addressed, considering that CO2 is known to increase Drosophila sensitivity to infections (Helenius et al., 2009).

Collectively, the authors should provide more information to support their statements that this is not small variation in the initial condition that explain the stochasticity. While the influence of CO2 might be easily tested, the impact of differences in the initial dose could be better characterized by adding more measurement of the initial dose for several bacteria. Another way could be to monitor stochasticity in infected flies with two related doses in the same setting (Dose 1 being always slightly superior of Dose 2) and see the existence of flies that die faster with Dose 2 compared to Dose 1).

2) Analysis of Immune response and bacterial growth:

The analysis of Imd signaling (Dpt induction) on single flies is a key part of this paper, yet is massively under-developed. Only one time point is shown, and given that transcript is measured, when mature AMP is the functional output, it is not at all clear that this one time point is relevant. Then, in the next panel, a different time point is examined to argue that Dipt levels do not correlate with bacterial loads. It can be argued that an earlier time point, such as 2 hours, is really the most relevant, as the model argues that the timing of the initiation of the response is deterministic, and perhaps at the initiating time point a correlation between load and response would be observed. Did the authors try to analyze immune response and bacterial growth in live flies using adequate fluorescent reporter (Dpt-mcherry, P. rettgeri GFP) ? While being less quantitative, this could bring another set of data that support their main conclusions.

On this line, the notion that the methods used here demonstrate bacterial growth in an individual fly (see language in Figure 3 legend) is grossly overstated. Clearly, as a population, the evidence clearly demonstrates bacterial growth in vivo. However, the bacterial growth within any individual fly cannot be assessed by these methods.

3) Clarity of the text and relevant information:

Many parameters affect infection such a temperature, sex, injection methods…. This information should be in the Results section not hidden in the Materials and methods. It is not clear what each survival graph shows, is it a representative result? How many times was it repeated? How many flies? Males or females? For bacterial load graphs, were all individual flies taken from one experiment (one biological replicate) or is it pooled from several replicates? It is often difficult to know how the experiments were done. All these details should be provided. Moreover, we could not exclude batch effect. This is actually suggested by Figure 4B with the new bacteria appearing more virulent.

4) All the data should be made publicly available to allow other scientists to use them. I would suggest to include all the raw data in excel sheets (bacterial count, survival data; biological repeats…).

5) The idea that the bacteria proliferate at the same rate in LB medium and flies should be documented for other strains.

6) Description of the model: more information on the model should be included to the main text. As it is written it is hard to understand this section of the paper. Moreover, even as written it is not fully and clearly explained to a non-expert in the field of modeling. For example, the meaning and import of mini graph of "Frequency vs. tc was unclear to one reviewer, and the relationship of Pc to the area below "the" curve was likewise unclear, as there are 2 curves presented. Some parameters are introduced but described later: Vc is shown in the figure but mentioned only in the Discussion. The confusion on the description of the model stem partly because of the high density at which series of hypotheses, tests and results are presented, and different sets of empirical results invoked (e.g., the third paragraph of the subsection “A mixture model to capture within-host bacterial growth dynamics”, which covers huge terrain very rapidly). Perhaps greater use of paragraph breaks or subheadings would help the reader navigate.

Globally, a longer paragraph with the model, the definition of each parameter could improve the impact of this paper.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Stochastic variation in the initial phase of bacterial infection predicts the probability of survival in D. melanogaster" for further consideration at eLife. Your revised article has been favorably evaluated by Wendy Garrett (Senior Editor), a Reviewing Editor, and one reviewer.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Both the external reviewer and the reviewing editor found that the authors have adequately answered to most of reviewers’ comments. As you can see from the reviewer 3, there is regret that the paper does not include in vivo monitoring of antimicrobial peptide gene expression to back up the model. Nevertheless, it is true that GFP reporters are slow and might not be the appropriate tool to monitor the immune dynamic at early time point. To address this in particular, we would recommend that you adjust your text, in both the Results and the Discussion, to make it explicitly clear that you are inferring a variance in the initiation of response, but do not (yet) have tools available to demonstrate it.

Reviewer #3:

This remains one of the most thought provoking papers I have read in recent years. I think it will be a landmark in the field.

That being said, I continue to struggle with the big issue, which is not directly addressed by the revisions. In short, the authors have inferred that the differences in the timing or strength of the initial immune response following infection determine the outcome (death at BLUD or chronic infection at SPBL). Surprisingly, they write in the rebuttal that they have been unable to measure AMP induction via fluorescent protein reporters at these early time points, at least in intact flies. Ideally, I would love some type of data that can probe this inference.

Another more significant issue, is (still) the presentation of the mathematical model. Lots is made of the probability calculation in Figure 6 and beyond, but the way this probability is determine is not explained in the Results section. It is presented in detail in the Materials and methods, but frankly the math is over my head. I would prefer some discussion of this computation directly in the Results section so as to make sense of Figure 6B, for example.

Finally, the rationale for the time points used in 7B (4 hour) and 7C (8 hours) is presented, and argued compellingly, in the rebuttal but this logic is still missing from the actual text of the article. I would recommend including.
