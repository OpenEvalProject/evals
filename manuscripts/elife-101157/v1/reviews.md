# Peer review - Round 1

Editors:
- Nils Kolling, Stem-cell and Brain Institute (SBRI), U1208 Inserm France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.101157.3.sa0](https://doi.org/10.7554/eLife.101157.3.sa0)

This important study addresses the question of how large-scale events such as the COVID-19 pandemic can change people's beliefs and their updates. Using a well-validated task, the authors find that belief updating becomes less optimistically biased during COVID-19 compared to before it. In this revision, due to the addition of more model-based analyses and power calculations, they have generated convincing evidence for their primary claim that the pandemic significantly impacted people's belief updating away from optimistic belief updating. As with many manipulations outside the experimenters' control, it remains unclear which psychological factor impacted by the pandemic drives the group differences, and sample sizes are, by necessity, on the smaller side as data cannot readily be acquired. However, the authors are commended for doing power analyses, showing their sensitivity, and recognizing the limitations of their study.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101157.3.sa1](https://doi.org/10.7554/eLife.101157.3.sa1)

This manuscript uses a well-validated behavioural estimation task to investigate the degree to which optimistic belief updating was attenuated during the 2020 global pandemic. Online participants estimated how likely different negative life events were to happen to them in the future and were given statistics about these events. Belief updating (measured as the degree to which estimations changed after viewing the statistics) was less optimistically biased during the pandemic (compared to outside of it). This resulted from reduced updating from "good news" (better than expected information). Computational models were used to try to unpack how statistics were integrated and used to revise beliefs. Two families of models were compared - an RL set of models where "estimation errors" (analogous to prediction errors in classic RL models) predict belief change and a Bayesian set of models where an implied likelihood ratio was calculated (derived from participants estimations of their own risk and estimation of the base rate risk) and used to predict belief change. The authors found evidence that the former set of models accounted for updating better outside of the pandemic, but the latter accounted for updating during the pandemic. In addition, the RL model provides evidence that learning was asymmetrically positively biased outside of the pandemic but symmetric during it (as a result of reduced learning rates from good news estimation errors).

Strengths

Understanding whether biases in learning are fixed modes of information processing or flexible and adapt in response to environmental shocks (like a global pandemic or economic recession) is an important area of research relevant to a wide range of fields, including cognitive psychology, behavioural economics, and computational psychiatry. The study uses a well-validated task, and the authors conduct a power analysis to show that the sample sizes are appropriate. Furthermore, the authors test that their results hold in both a between-group analysis (the focus of the main paper) and a within-group analysis (mainly in the supplemental).

The finding that optimistic biases are reduced in response to acute stress, perceived threat, and depression has been shown before using this task both in the lab (social stress manipulation), in the real world (firefighters on duty), and clinical groups (patients with depression). However, the work does extend these findings here in important ways:

(1) Examining the effect of a new real-world adverse event (the pandemic).

(2) The reduction in optimistic updating here arises due to reduced updating from positive information (previously, in the case of environmental threat, this reduction mainly arose from increased sensitivity to negative information).

(3) Leveraging new RL-inspired computational approaches, demonstrating that the bias - and its attenuation - can be captured using trial-by-trial computational modelling with separate learning rates for positive and negative estimation errors.

The authors now take great care to caveat that the findings cannot directly attribute the observed lack of optimistically biased belief updating during lockdown to psychological causes such as heightened anxiety and stress.

The authors have added model recovery results. Whilst there are some cases within a family (RL or Bayesian) of models where they can be confused (e.g., Bayesian model 10-the winning model during the pandemic-sometimes gets confused with Bayesian model 9), there is no confusion between families of models (RL models don't get confused with Bayesian models and vice versa), which is reassuring.

Weaknesses

The authors now conduct model recovery (SI Figure 5) and show how the behaviour of the two best-fitting models (Rational Bayesian model and optimistically biased RL-like model) approximates the actual data observed by showing them alongside each other (Figure 1b). It seems from Figure 1b that the 2 models predict similar behaviour for bad news but diverge for good news, with the optimistically biased RL-like model predicting greater updates than the rational Bayesian model. However, it is difficult to tell from the figure (partly because of the y-axis scale) how much of a divergence this is and how distinctive a pattern relative to the other models. I think the interpretation could be improved further by a clearer sense of the behavioural signatures of each model, enabling them to be reliably teased apart from one another in the model recovery.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101157.3.sa2](https://doi.org/10.7554/eLife.101157.3.sa2)

The authors investigated how experiencing the COVID-19 pandemic affected optimism bias in updating beliefs about the future. They ran a between-subjects design testing participants on cognitive tasks before, during and after the lift of the sanitary state of emergency during the pandemic. The authors show that optimism bias varied depending on the context in which it was tested. Namely, it disappeared during COVID-19 and it re-emerged at the time of lift of sanitary emergency measures. Via advanced computational modelling they are able to thoroughly characterise the nature of such alterations, pinpointing specific mechanisms underlying the lack of optimistic bias during the pandemic.

Strengths pertain to the comprehensive assessment of the results via computational modelling, and from a theoretical point of view, the notion that environmental factors can affect cognition. Power analysis was conducted to ensure that the study was powered to observe the effect of interest despite the relatively small sample size.

As the authors also noted, a major impediment to the interpreting the findings pertains to the lack of additional measures. While information on, for example, risk perception or need for social interaction were collected from participants during the pandemic, the fact that these could not be included in the analysis hindered the interpretation of findings. While the interpretation of the findings remains challenging, this work offers an example of the influence of real-life conditions on the belief-updating process.
