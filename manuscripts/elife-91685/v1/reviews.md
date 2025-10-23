# Peer review - Round 1

Editors:
- Srdjan Ostojic, École Normale Supérieure - PSL France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.91685.3.sa0](https://doi.org/10.7554/eLife.91685.3.sa0)

The study makes a valuable empirical contribution to our understanding of visual processing in primates and deep neural networks, with a specific focus on the concept of factorization. The analyses provide convincing evidence that high factorization scores are correlated with neural predictivity. This work will be of interest to systems neuroscientists studying vision and could inspire further research that ultimately may lead to better models of or a better understanding of the brain.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91685.3.sa1](https://doi.org/10.7554/eLife.91685.3.sa1)

Summary:

The dominant paradigm in the past decade for modeling the ventral visual stream's response to images has been to train deep neural networks on object classification tasks and regress neural responses from units of these networks. While object classification performance is correlated to variance explained in the neural data, this approach has recently hit a plateau of variance explained, beyond which increases in classification performance do not yield improvements in neural predictivity. This suggests that classification performance may not be a sufficient objective for building better models of the ventral stream. Lindsey & Issa study the role of factorization in predicting neural responses to images, where factorization is the degree to which variables such as object pose and lighting are represented independently in orthogonal subspaces. They propose factorization as a candidate objective for breaking through the plateau suffered by models trained only on object classification. They show the degree of factorization in a model captures aspects of neural variance that classification accuracy alone does not capture, hence factorization may be an objective that could lead to better models of ventral stream. I think the most important figure for a reader to see is Fig. 6.

Strengths:

This paper challenges the dominant approach to modeling neural responses in the ventral stream, which itself is valuable for diversifying the space of ideas.

This paper uses a wide variety of datasets, spanning multiple brain areas and species. The results are consistent across the datasets, which is a great sign of robustness.

The paper uses a large set of models from many prior works. This is impressively thorough and rigorous.

The authors are very transparent, particularly in the supplementary material, showing results on all datasets. This is excellent practice.

Weaknesses:

The authors have addressed many of the weaknesses in the original review. The weaknesses that remain are limitations of the work that cannot be easily addressed. In addition to the limitations stated at the end of the discussion, I'll add two:

(1) This work shows that factorization is correlated with neural similarity, and notably explains some variance in neural similarity that classification accuracy does not explain. This suggests that factorization could be used as an objective (along with classification accuracy) to build better models of the brain. However, this paper does not do that - using factorization to build better models of the brain is left to future work.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91685.3.sa2](https://doi.org/10.7554/eLife.91685.3.sa2)

Summary:

Object classification serves as a vital normative principle in both the study of the primate ventral visual stream and deep learning. Different models exhibit varying classification performances and organize information differently. Consequently, a thriving research area in computational neuroscience involves identifying meaningful properties of neural representations that act as bridges connecting performance and neural implementation. In the work of Lindsey and Issa, the concept of factorization is explored, which has strong connections with emerging concepts like disentanglement [1,2,3] and abstraction [4,5]. Their primary contributions encompass two facets: (1) The proposition of a straightforward method for quantifying the degree of factorization in visual representations. (2) A comprehensive examination of this quantification through correlation analysis across deep learning models.

To elaborate, their methodology, inspired by prior studies [6], employs visual inputs featuring a foreground object superimposed onto natural backgrounds. Four types of scene variables, such as object pose, are manipulated to induce variations. To assess the level of factorization within a model, they systematically alter one of the scene variables of interest and estimate the proportion of encoding variances attributable to the parameter under consideration.

The central assertion of this research is that factorization represents a normative principle governing biological visual representation. The authors substantiate this claim by demonstrating an increase in factorization from macaque V4 to IT, supported by evidence from correlated analyses revealing a positive correlation between factorization and decoding performance. Furthermore, they advocate for the inclusion of factorization as part of the objective function for training artificial neural networks. To validate this proposal, the authors systematically conduct correlation analyses across a wide spectrum of deep neural networks and datasets sourced from human and monkey subjects. Specifically, their findings indicate that the degree of factorization in a deep model positively correlates with its predictability concerning neural data (i.e., goodness of fit).

Strengths:

The primary strength of this paper is the authors' efforts in systematically conducting analysis across different organisms and recording methods. Also, the definition of factorization is simple and intuitive to understand.

Weaknesses:

Comments on revised version:

I thank the authors for addressing the weaknesses I brought up regarding the manuscript.
