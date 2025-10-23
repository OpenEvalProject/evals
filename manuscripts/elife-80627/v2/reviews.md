# Peer review - Round 1

Editors:
- Claus Hilgetag, https://ror.org/01zgy1s35 University Medical Center Hamburg-Eppendorf Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80627.sa0](https://doi.org/10.7554/eLife.80627.sa0)

Your intriguing and original study investigates how the characteristic architecture of human brain networks leads to specific features of global neural dynamics. Your paper addresses a question that is of wide interest and provides a significant advance in understanding how connectomic features underlie aspects of the neural dynamics of human versus non-human (chimpanzee) brains. Moreover, the present approach showcases a powerful computational strategy for identifying structural factors that may help explain specific cognitive abilities of humans.


---

# Peer review - Round 1

Editors:
- Claus Hilgetag, https://ror.org/01zgy1s35 University Medical Center Hamburg-Eppendorf Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80627.sa1](https://doi.org/10.7554/eLife.80627.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Evolutionary shaping of human brain dynamics" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor (Claus Hilgetag) and Christian Büchel as the Senior Editor.

The following individual involved in the review of your submission has agreed to reveal their identity: Bratislav Misic (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this summary to help you prepare a revised submission.

Essential revisions:

1) Both reviewers commented that the observed species differences of simulated brain dynamics bring up the question of the topological differences of the human versus the nonhuman primate connectomes that result in these brain dynamics. Therefore, relevant topological features should be identified, substantiated by additional analyses, and presented more prominently in the paper.

2) Major concerns particularly of Reviewer 2 concern the functional interpretation of the computational modeling results, concretely the inferred dynamic ranges for the nonhuman and human connectomes. Please clarify and substantiate the given functional interpretations, such as the claims regarding facilitated co-activation, functional integration, computational capacity, and decision-making performance, ideally with additional quantitative arguments.

Generally, demonstrate more convincingly, and if possible by quantitative arguments, how the simulated brain dynamics for the human brain confer particular functional advantages. As a test, if one did not know which one was the human connectome, which of the different connectomes would we actually expect to have the best cognitive performance?

Reviewer #1 (Recommendations for the authors):

This is an important conceptual advance on the idea that anatomical architecture shapes and constrains neural dynamics. Namely, the authors show that evolutionary differences in connectivity can lead to dynamic differences that support fundamentally different types of communications. These findings are sure to be of wide interest to the field.

The work is rigorous and carried out at a high technical standard: the authors have taken great care to ensure that the connectomes from different species are comparable, that the results hold using multiple methodological approaches, and that they can be replicated in multiple datasets. I also commend the authors for making their code publicly available.

1. "validated biophysical models" These models are certainly realistic and can qualitatively replicate many empirical phenomena, but are they strictly-speaking "validated"?

2. "Specifically, anterior regions (e.g., frontal regions known to be expanded in humans compared to chimpanzees [3,4]) show neural dynamics with higher (more diffuse) dynamic ranges, while posterior regions (e.g., occipital cortex known to be relatively similar in size across the two species) have lower (sharper) dynamic ranges."

Could the authors verify by comparing this map with the evolutionary expansion map from Hill and colleagues?

3. A recent paper from Shafiei and colleagues has investigated empirical patterns of time series features – including several measures of dynamic range – and may be of interest:

Shafiei, G., Markello, R. D., De Wael, R. V., Bernhardt, B. C., Fulcher, B. D., and Misic, B. (2020). Topographic gradients of intrinsic dynamics across the neocortex. eLife, 9, e62116.

4. I was surprised that timescale and dynamic range are positively correlated (Figure 4). My intuition would be that time series that have lower autocorrelation fluctuate more rapidly and therefore would assume a greater range of values.

5. I was surprised that the result in Figure S12 was relegated to the supplement. The main finding – that inter-species differences in connectivity give rise to different dynamics – is rather beautiful and interesting, and naturally raises the question of whether any specific topological features of structural connectivity can explain the resulting inter-species differences and regional heterogeneity. The findings are very convincing and could be presented more prominently.

Reviewer #2 (Recommendations for the authors):

The paper by Pang et al., demonstrates a promising technique for inferring functionally relevant information from connectome data, which in turn can be used to compare humans with other primates. Such comparisons facilitate the formation of evolutionary hypotheses to account for the particularities of human behavior and cognition.

This paper is a good example of the use of dynamical modeling to distill interpretable information from neuroimaging data. The results are qualitatively clear: the differences between humans and other primates are visible in the figures. The findings related to a gradient of dynamic ranges along the anterior-posterior axis are also of wide interest and can be readily compared with studies on anatomical and physiological gradients. The study involves validation using a second computational model, enhancing the robustness of the results. The connection with computational capacity is also very interesting. Further, the model is used to make specific predictions about functional connectivity, which are verified. The results will be of interest to several subdisciplines within neuroscience: in particular, the link between connectivity and computational capacity has the potential to dovetail with more fine-grained types of data collected in other species, as well as with computational models of decision-making and evidence-accumulation.

The primary weakness of the paper lies in the difficulty of interpreting the broader meaning of the results. Readers may not readily understand what the behavioral and psychological consequences of high and low dynamic ranges are. Some further elaboration of this concept, perhaps with examples from perception and decision-making, will increase the potential readership. Additional explanation of why responses to changes in global recurrent strength are relevant to the local dynamic ranges of each cortical region/network will also be helpful.

The interpretability issue also arises for the treatment of computational capacity: some elaboration of the differences and trade-offs when comparing accuracy in humans and chimpanzees will help with readability. The concept of "decision accuracy of the whole brain" is also somewhat obscure: it is not obvious why a decision should be construed as the result of independent drift-diffusion processes. It may also be helpful to comment briefly on how such a framework can be extended when a decision process is not a two-alternative forced choice.

The nature of the anatomical difference between humans and other primates is also somewhat unclear. The results are described as suggesting evidence for structural changes over the course of evolution. The difference in dynamic range distribution between humans and other primates serves as indirect evidence of these structural changes. But the results do not seem to include a direct comparison of the structural data (prior to modeling, using descriptive statistics) across the various primate species. In addition to this empirical question, the model suggests the possibility of generating specific hypotheses regarding the trajectory of human evolution. Is increased speed/myelination the key factor, or does the overall magnitude of connection weights matter too? What alterations of the chimpanzee connectivity dataset would bring the dynamic range distribution in line with that of humans? The information required to suggest answers to such questions seems to be in the paper, but it is not easy for the reader to piece it together.

Given that the methods come at the end, some comments on terminology would be helpful in the introduction and/or the results. It is not clear why the term "gating" is used instead of "output" or "response". A reader without a computational background may not be familiar with this term.

Why would neuromodulation only affect recurrent strength and not the off-diagonal terms of the connection matrix (matrix A)?

The drift-diffusion model may not be sufficient to account for certain aspects of decision-making, such as urgency (e.g., Carland et al., 2015), or direct inhibition-mediated competition between alternatives. The differences in speed between humans and chimpanzees could conceivably point to differences in the amount and/or timescale of inhibition. Inhibition seems to be higher in humans than in other mammals: this may be relevant to the slower integration of evidence. Even in a model that lumps excitation and inhibition together as positive and negative connection weights, it may be illuminating to know if the E/I ratio sheds light on the speed of arriving at the decision threshold. This is not essential, but inhibition-related inferences would greatly enhance the interest of the paper.

Using the term "diffuse" for high dynamic range seems a bit confusing without further elaboration.

Figure 1. A qualitative explanation of the sigmoidal shape would be useful. How can we interpret the two knee points of the sigmoid, as well as the slope? Is a very steep sigmoid (or a step function) equivalent to an all-or-nothing response to the crossing of a threshold in recurrent activity?

Page 1 Line 13: Some examples of topological properties would be useful.

Page 3 line 10: "Brain regions with similar dynamic ranges are more likely to coactivate, allowing efficient region-to-region integration of neural processes." Why are they more likely to coactivate? Is there a probabilistic argument? One might assume instead that brain regions with high/diffuse dynamic ranges would be more likely to coactivate, since there are more opportunities for them to become active in the first place.

Reference

Carland, M. A., Thura, D., and Cisek, P. (2015). The urgency-gating model can explain the effects of early evidence. Psychonomic Bulletin and Review, 22(6), 1830-1838.
