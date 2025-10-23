# Peer review - Round 1

Editors:
- Wenying Shou, Fred Hutchinson Cancer Research Center United States

Reviewers:
- Wenying Shou, Fred Hutchinson Cancer Research Center United States
- Steven S Andrews, Fred Hutchinson Cancer Research Center United States

## Review text

DOI: [10.7554/eLife.33617.034](https://doi.org/10.7554/eLife.33617.034)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Signaling pathways as linear transmitters" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Wenying Shou as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Steven S Andrews (Reviewer #2).

Our decision has been reached after consultation between the reviewers. We all found your work interesting, but we all had problems with the precise meaning of "physiological ranges".

Reviewer #1:

Nunns and Goentoro examined the conserved cores of three signaling pathways (Wnt, ERK, and TGFb). Using mathematical modeling, they found that despite differences in pathway architecture, the three pathways all behaved like linear signal transmitters within physiological ranges. Using experiments to test two pathways (Wnt and ERK), they indeed found linear input-output relationship.

I like how they used dimensionless analysis to gain insights on mechanisms of linearity. My major comments are:

1) They need to describe more carefully the "physiology range": what do they mean by physiological? Moreover, I assume that every parameter has its own range, and dimensionless numbers comprising many parameters probably have a quite large range. What are their ranges? Does most of the range fall within "physiological range"?

2) On a related note, for ERK which is known to sometimes exhibit switch-like responses, how would those parameters and inputs fare in your analytics? Would they have told you that the response will be non-linear?

3) Is there any way to make the wiring diagrams more intuitive and the important points more obvious? Perhaps color coding those parameters in α or γ? More details in legend? For example, why α represents β-catenin degradation by DC is not clear: k11 – which I assume means degradation of phosphor β catenin – is not in α. Why not? The information might already be in supplementary data, but intuition about an expression should be in the main text if you want to appeal to a broad audience.

Reviewer #2:

The authors used modeling and then experiment to show linear input-output relations in several model signaling pathways, which were the canonical Wnt, ERK, and Tgf-β pathways. The modeling started with established ODE-based models and reduced them to simplified analytical expressions that related output to input; these expressions did not show linear relationships in general but did in physiologically relevant parameter regimes. The experiments showed linearity in the Wnt and ERK pathways, and that this linearity was reduced through system perturbations.

This is very good work on an important problem. The methods and analysis were appropriate, and the paper is well written.

1) It should be clarified whether the authors are referring to linear signal transmission relative to the signaling pathway ligand concentrations, or to the fraction of bound receptors. This issue arises because the authors show linearity relative to the ligand concentrations in the model analysis portion of this work, but then linearity relative to the fraction of bound receptors in the experimental work on the Wnt pathway. More specifically, it appears that the use of Wnt as the x-axis in Figure 2D contradicts statements in subsection “Linearity in the Wnt and ERK pathways was observed experimentally”, which say that "linearity does not extend upstream to Wnt dose".

2) My experience with cell signaling pathway ODE models is that they capture the known biological interactions reasonably correctly, they agree well with a specific set of test data, and they get the signaling dynamics qualitatively correct, but they are rarely accurate enough for quantitative predictions on untested problems. However, this work uses three models for quantitative predictions. On the one hand, I applaud this approach because it fulfills a major objective of modeling research. On the other hand, I feel that more work is required to convince the reader that the models are in fact accurate enough to warrant the conclusions that are reached from them. This includes the models having sufficient accuracy over both the parameter and time ranges that are considered. For example, if the grey lines in Figure 3 were model calculations (without any additional fitting), I would have greater trust in the models.

3) A persistent concern that I had is that most dose-response functions for cell signaling can be modeled well by Hill functions, and Hill functions are linear relationships in the small dose regime. Is the linearity observed here simply an observation of Hill functions in the small dose regime? If so, then all of these results are reasonably trivial. As part of addressing this issue, it would help if the authors could give the physiologically typical concentration ranges for Wnt, EGF, and Tgf-β.

Reviewer #3:

This manuscript aims to test whether signaling pathways have linear input-output response characteristics. A simplification of existing mathematical models indicates this being the case for the canonical Wnt, ERK and TGF-β pathways, despite striking differences in core network architectures among these pathways. It is interesting to see how different complex pathways can be approximated by linear systems. The manuscript concludes by experiments (Western Blots) testing the theoretical results, as well as the breakdown of linearity as some key features of the pathways are altered.

In summary the major point here seems to be that in many of these diverse, complicated, pathways, a linear dose-response can be observed as an approximation, and this might be borne out in experimental conditions as well. In fact, not only can the linear dose response be observed, it appears rather robust to perturbations until you exceed some critical value. While these results are potentially interesting, there are major weaknesses that should be addressed before the manuscript could be considered for publication in eLife.

1) Besides the three pathways chosen, there are other pathways that are similarly well studied, both experimentally as well as mathematically. The NF-kappaB pathway is a good example. Why was the NF-kappaB pathway or any other pathway not considered? You could make a statement that proving the generality of this finding will require investigating additional pathways in the future.

2) A linear input-output relationship due to negative feedback has already been described for a MAP Kinase pathway, see PMID:19079053. How are the current results novel compared to these earlier findings (besides studying a human MAPK pathway)?

3) The claims of linearity in this manuscript are mainly based on visual examination. However, there are rigorous ways to measure linearity, based on the L1-norm, as described in PMID:19279212 and PMID:23385595, which should be cited. It would be necessary to apply the L1-norm throughout all figures of the manuscript to make computational and experimental claims of linearity quantitative.

4) For deriving formula [4], apha/u>>1 is necessary. However, based on the SI, α/u=11, and it is actually smaller for some of the range plotted in Figure 2. Then the linearity arises from 'α / u >> 1 + γ'. One could/should explore when α = (1+γ)/u * S where S is a scaling factor set to say, 0.9, 1, 1.1, 2, 10, and 100. At 10 and 100, one might expect the condition to hold, but at S around 1 the simplification probably fails. Do we then see lack of linearity? One can then re-arrange the terms for each of the other terms (u or γ) and explore similarly. The same argument can be made for the Erk and Tgf[β] pathways.

4) How robust is linearity? To answer this question, two modifications are needed: (i) extend the range of u for each plot in Figure 2, showing the nonlinearity of the curves, then indicate the linear range on such nonlinear curves, e.g. with a different color; (ii) Change a parameter and plot a family of curves, indicating the linear range (determined based on the L1-norm) on each individual curve. This can be done for a couple of parameters, but it is especially important for the parameters mediating interactions that cause linearity to break down (described in subsection “Linearity in the Wnt and ERK pathways is modulated by perturbation to parameters”).

5) If linear responses indeed help cellular signal processing as a result of convergent evolution then linearity should probably occur in single cells that process inputs. Unfortunately, the Western Blots in Figure 3 only test linearity at the population average level. The linearity of the average does not imply linearity in single cells. So, are single cell input-output response characteristics linear? This should be checked at least for one signaling pathway, possibly by new experiments or otherwise using data by others, see for example PMID:25504722. In fact, recent papers indicate that some pathways' responses are dynamic/oscillatory, noisy or bimodal at the single cell level. All of this should be addressed/discussed. Where is then the linearity?

6) What defines a "physiological range"? As noted, ultrasensitivity has been described for the ERK pathway's input response. Ultrasensitivity seems contradictory to linearity. Is then ultrasensitivity not physiological? Moreover, what is physiological in a given tissue or organism (from yeast to frog eggs to worms to humans) might not be physiological in another one. All of this should be discussed and clarified.

7) Considering the importance of fold-change detection in biology, it would be important to assess the number of decades over which linearity holds for each pathway. In fact, any nonlinear function can be approximated by a linear relationship except near extremum points (this is the essence of the Taylor approximation). Are these observations more than Taylor expansion? Maybe we can tell based on the decades over which linearity holds.

8) The data in Figure 3 should be expanded into the domains of nonlinearity/saturation and then the range of linearity should be indicated on top of such curves (linearity measured using the L1-norm). This should be done for all panels. In fact, without showing the full curve (including the nonlinear parts), panel 3C does not indicate that linearity is lost or that its range shrinks.

9) What ranges on the theoretical plots do the experimental results correspond to? Theory and experiment should be better connected.

10) Experimental verification is not trivial in these systems. First, the "quantitative' Western blots are not truly quantitative, despite ensuring that fluorescent antibodies are within linear range, etc. Western blots, by their very nature, are notoriously noisy, and therefore require a lot of "normalization" which might artifactually introduce the appearance of linearity. If, for example, the denominator is very large for normalization, the signal can appear more linear. Say, if you compare y=x and y=x^2, but then divide by a large factor K such that within the range of 'x' being explored K>>y, then both equations will be nearly 0 and will likely show a "linear" response (also true according to the Taylor expansion near 0).

11) The variability in the Western blots is borne out in Figure 3A where the various 'Wnt' doses have very variable pLRP5/6 response (input). Likewise, in Figure 3B, for EGF. These few points do not necessarily demonstrate linearity other than the fact that the linear approximation can be applied to just about any relationship. In addition, comparing Figure 3A with Figure 3D where linearity breaks down with a Raf mutation preventing feedback, it still appears linear until 3ng/mL, a dose that is not reported for the wild-type (Figure 3A). In fact, examining both plots between 0 to 2ng/mL, one could conclude instead that both systems are 'linear'.

12) Same with the Wnt pathway. Here it is already recognized that linearity was not lost, but this is attributed to side effects of the drug used – something that could be tested perhaps with a different drug or a mutation similar to the Erk pathway analysis.
