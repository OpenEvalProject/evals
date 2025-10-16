# Peer review - Round 1

Editors:
- Marius V Peelen, Radboud University Nijmegen Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.98351.3.sa0](https://doi.org/10.7554/eLife.98351.3.sa0)

This important study presents an original and promising approach to combine convolutional neural networks of visual processing with evidence accumulation models of decision-making. While the methodological approach is technically sophisticated and the evidence is solid, there is still a gap between the model and the behavioral data. The study will be of interest to researchers working in the fields of machine learning and cognitive modeling.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98351.3.sa1](https://doi.org/10.7554/eLife.98351.3.sa1)

Summary:

This paper introduces a new approach for modeling human behavioral responses using image-computable models. They create a model (VAM) that is a combination of a standard CNN coupled with a standard evidence accumulation model (EAM). The combined model is then trained directly on image-level data using human behavioral responses. This approach is original and can have wide applicability. However, many of the specific findings reported are less compelling.

Strengths:

(1) The manuscript presents an original approach of fitting an image-computable model to human behavioral data. This type of approach is sorely needed in the field.

(2) The analyses are very technically sophisticated.

(3) The behavioral data are large both in terms of sample size (N=75) and in terms of trials per subject.

Weaknesses:

(1) The main advance here thus appears to be methodological rather than conceptual. It's really cool that VAMs are image computable and are also fit to human data. But what we learn about the mind or brain is perhaps more modest.

(2) In the approach here, a given stimulus is always processed in the same way through the core CNN to produce activations v_k. These v_k's are then corrupted by Gaussian noise to produce drift rates d_k, which can differ from trial to trial even for the same stimulus. In other words, the assumption built into VAM appears to be that the drift rate variability stems entirely from post-sensory (decisional) noise. In contrast, the typical interpretation of EAMs is that the variability in drift rates is sensory. In response to this concern, the authors responded that one can imagine an additional (unmodeled) sensory process that adds variability to the drift rates. However, this process remains unmodeled. The authors motivate their paper by saying "EAMs do not explain how the visual system extracts these representations in the first place" (second sentence of the Abstract). VAM is definitely a step in this direction but there's still a gap between the current VAM implementation and sensory systems.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98351.3.sa2](https://doi.org/10.7554/eLife.98351.3.sa2)

In An image-computable model of speeded decision-making, the authors introduce and fit a combined CCN-EAM (a 'VAM') to flanker-task-like data. They show that the VAM can fit mean RTs and accuracies as well as the congruency effect that is present in the data, and subsequently analyze the VAM in terms of where in the network congruency effects arise.

I have mixed feelings about this manuscript, as I appreciate the innovative efforts to combine CNNs with EAMs in a new class of cognitive models, while also having some reservations from an EAM perspective. The idea of combining these approaches has great potential, and I'm excited to see where this research will lead. However, I do have some concerns about the quality of fit between the behavioral data and the model. Specifically, the RT distributions, delta plots, and conditional accuracy function don't appear to be well-matched by the VAM. The conflict effects on behavioral data are well-established and typically considered crucial to understanding the underlying cognitive process. Unfortunately, it seems that these parts of the data don't fit well with the proposed model.

This disparity is not entirely surprising. The EAM literature suggests that LBA models might not be suitable for conflict tasks, and the presented results seem to confirm this concern. Conflict EAMs, including the DMC (e.g., Ulrich et al., 2015; Evans & Servant, 2022; Lee & Sewell 2024), propose dynamic drift rates with a fast automatic process that is gradually withdrawn from evidence accumulation over time. This approach results in congruency effects arising from temporal dynamics, not spatial representations.

In contrast, the VAM imposes static drift rates in the LBA model, leading to an effect between drift rates that translates to changes in representations. However, this account does not adequately explain the behavioral data, and the proposed representational geometry explanation is therefore limited.

My concerns are addressed in the revised manuscript, but I struggle to understand why the authors distinguish between explaining mean effects across individuals and congruency effects within individuals. These concepts seem related, and issues at the individual level could propagate to the group mean. Furthermore, I find it challenging to accept that dynamics merely act 'in concert' with the orthogonalization mechanism, as it seems possible that an account that uses a time-varying EAM may not require any orthogonalization mechanism in the first place. The orthogonalization mechanism might have arisen because the model does not have the possibility to account for the conflict effect from temporal effects, instead of spatial effects. I could envision a CNN-DMC in which conflict effects arise only at the level of the choice model (e.g., as a time-varying filter that changes which information is read out from the visual system, rather than due to changes in the representations in the visual system itself). This possibility should be acknowledged in the paper, and it would be interesting to discuss how such an account would be tested.

While I appreciate the technological advancement presented in this paper, my concerns are not about implementation details but rather about the choice of models and their consequences. I believe that a more in-depth exploration of which conclusions can be drawn, and which model comparisons would be required to reach a final conclusion.
