# Peer review - Round 1

Editors:
- Margaret L Schlichting, University of Toronto Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.88608.3.sa0](https://doi.org/10.7554/eLife.88608.3.sa0)

This paper presents important computational modeling work that provides a mechanistic account for how memory representations become integrated or differentiated (i.e., having distinct neural representations despite being similar in content). The authors provide convincing evidence that simple unsupervised learning in a neural network model, which critically weakens connections of units that are moderately activated by multiple memories, can account for three empirical findings of differentiation in the literature. The paper also provides insightful discussion on the factors contributing to differentiation as opposed to integration, and makes new predictions for future empirical work.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88608.3.sa1](https://doi.org/10.7554/eLife.88608.3.sa1)

Ritvo and colleagues present an impressive suite of simulations that can account for three findings of differentiation in the literature. This is important because differentiation-in which items that have some features in common, or share a common associate are less similar to one another than are unrelated items-is difficult to explain with classic supervised learning models, as these predict the opposite (i.e., an increase in similarity). A few of their key findings are that differentiation requires a high learning rate and low inhibitory oscillations, and is virtually always asymmetric in nature.

This paper was very clear and thoughtful-an absolute joy to read. The model is simple and elegant, and powerful enough to re-create many aspects of existing differentiation findings. The interrogation of the model and presentation of the findings were both extremely thorough. The potential for this model to be used to drive future work is huge.

The authors have been very responsive to my previous reviews and I have no further concerns and identify no major weaknesses.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88608.3.sa2](https://doi.org/10.7554/eLife.88608.3.sa2)

Summary:

This paper addresses an important computational problem in learning and memory. Why do related memory representations sometimes become more similar to each other (integration) and sometimes more distinct (differentiation)? Classic supervised learning models predict that shared associations should cause memories to integrate, but these models have recently been challenged by empirical data showing that shared associations can sometimes cause differentiation. The authors have previously proposed that unsupervised learning may account for these unintuitive data. Here, they follow up on this idea by actually implementing an unsupervised neural network model that updates the connections between memories based on the amount of coactivity between them. The authors use their modeling framework to simulate three recent empirical studies, showing that their model captures aspects of these findings that are hard to account for with supervised learning.

Overall, this is a strong and clearly described work that is likely to have a positive impact on computational and empirical work in learning and memory. While the authors have written about some of the ideas discussed in this paper previously, a fully implemented and openly available model is a clear advance that will benefit the field. It is not easy to translate a high-level description of a learning rule into a model that actually runs and behaves as expected. The fact that the authors have made all their code available makes it likely that other researchers will extend the model in numerous interesting ways, many of which the authors have discussed and highlighted in their paper.

Strengths:

The authors succeed in demonstrating that unsupervised learning with a simple u-shaped rule can produce results that are qualitatively in line with the empirical reports. In each of the three models, the authors manipulate stimulus similarity (following Chanales et al.), shared vs distinct associations (following Favila et al.), or learning strength (a stand-in for blocked versus interleaved learning schedule; following Schlichting et al.). In all cases, with hand-tuning of additional parameters, the authors are able to produce model representations that fit the empirical results, but that can't easily be accounted for by supervised learning. Demonstrating these effects isn't trivial and a formal modeling framework for doing so is a valuable contribution. Overall, the work is very thorough. The authors investigate many different aspects of the learning dynamics (learning rate, oscillation strength, hidden layer overlap etc) in these models and produce several key insights. Of particular value are their demonstrations that when differentiation occurs, it occurs very quickly and asymmetrically and results in anti-correlated representations, as well as the distinction between symmetric and asymmetric integration in their model. The authors thoroughly acknowledge the relative difficulty of producing differentiation in their models relative to integration, and are now more clear about why they don't necessarily view this as mismatch with the empirical data. The authors are also more clear about the complicated activation dynamics in their model and why critical ranges for some parameters can't be given -- the number of interacting parameters mean that there are many combinations that could produce the critical activation dynamics and thus the same result. Despite this complexity, the paper is very clearly written; the authors do a good job of both formally describing their model as well as giving readers a high level sense of how many of their critical model components work.

Weaknesses:

Though the u-shaped learning rule is essential to this framework, the paper doesn't do any formal investigation of this learning rule or comparison with other learning rules. The authors do have a strong theoretical interest in this rule as well as experimental precedent for testing this rule, which they now thoroughly discuss in the paper. Still, a stronger argument in support of the non monotonic plasticity hypothesis could have been made by comparing this learning rule to alternatives. Additionally, the authors' choice of strongly prewiring associations makes it difficult to think about how their model maps onto experimental contexts where associations are only weakly learned. However, the authors thoroughly acknowledge why this was necessary and discuss this limitation in the paper.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88608.3.sa3](https://doi.org/10.7554/eLife.88608.3.sa3)

This paper proposes a computational account for the phenomenon of pattern differentiation (i.e., items having distinct neural representations when they are similar). The computational model relies on a learning mechanism of the nonmonotonic plasticity hypothesis, fast learning rate and inhibitory oscillations. In the revised paper, the authors justified the initialization of the model, added empirical evidence supporting the use of two turning points in the NMPH function and provided details of the learning mechanisms of the model. The relatively simple architecture of the model makes its dynamics accessible to the human mind. Furthermore, using similar model parameters, this model produces simulated data consistent with empirical data of pattern differentiation. The authors also provide insightful discussion on the factors contributing to differentiation as opposed to integration.
