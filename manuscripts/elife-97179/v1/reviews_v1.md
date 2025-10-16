# Peer review - Round 1

Editors:
- Wei Yan, Washington State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.97179.3.sa0](https://doi.org/10.7554/eLife.97179.3.sa0)

This important study reports findings on the GnRH pulse generator's role in androgen-exposed mouse models, providing further insights into PCOS pathophysiology and advancing the field of reproductive endocrinology. The experimental data were collected using cutting-edge methodologies and are solid. The findings, while interesting, are primarily applicable to mouse models, and their translation to human physiology requires cautious interpretation and further validation. This work will be of interest to endocrinologists and reproductive biologists.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97179.3.sa1](https://doi.org/10.7554/eLife.97179.3.sa1)

Summary:

The authors aimed to investigate the functionality of the GnRH (gonadotropin-releasing hormone) pulse generator in different mouse models to understand its role in reproductive physiology and its implications for conditions like polycystic ovary syndrome (PCOS). They compared the GnRH pulse generator activity in control mice, peripubertal androgen (PPA) treated mice, and prenatal androgen (PNA) exposed mice. The study sought to elucidate how androgen exposure affects the GnRH pulse generator and subsequent LH (luteinizing hormone) secretion, contributing to the pathophysiology of PCOS.

Strengths:

(1) Comprehensive Model Selection: The use of both PPA and PNA mouse models allows for a comparative analysis that can distinguish the effects of different timings of androgen exposure.

(2) Detailed Methodology: The methods employed, such as photometry recordings and serial blood sampling, are robust and allow for precise measurement of GnRH pulse generator activity and LH secretion.

(3) Clear Results Presentation: The experimental results are well-documented with appropriate statistical analyses, ensuring the findings are reliable and reproducible.

(4) Relevance to PCOS: The study addresses a significant gap in understanding the neuroendocrine mechanisms underlying PCOS, making the findings relevant to both basic science and potentially clinical research.

Weaknesses

(1) Model Limitations: While the PNA mouse model is suggested as the most appropriate for studying PCOS, the authors acknowledge that it does not completely replicate the human condition, particularly the elevated LH response seen in women with PCOS.

(2) Complex Data Interpretation: The reduced progesterone feedback and its effects on the GnRH pulse generator in PNA mice add complexity to data interpretation, making it challenging to draw straightforward conclusions.

(3) Machine Learning (ML) Selection and Validation: While k-means clustering is a useful tool for pattern recognition, the manuscript lacks detailed justification for choosing this specific algorithm over other potential methods. The robustness of clustering results has not been validated.

(4) Biological Interpretability: Although the machine learning approach identified cyclical patterns, the biological interpretation of these clusters in the context of PCOS is not thoroughly discussed. A deeper exploration of how these clusters correlate with physiological and pathological states could enhance the study's impact.

(5) Sample Size: The study uses a relatively small number of animals (n=4-7 per group), which may limit the generalisability of the findings. Larger sample sizes could provide more robust and statistically significant results.

(6) Scope of Application: The findings, while interesting, are primarily applicable to mouse models. The translation to human physiology requires cautious interpretation and further validation.

Comments on revised version:

I did not find the response to my main concerns regarding justification for the choice of the number of clusters (k) and providing evidence of cluster robustness satisfactory at all. It sounds contradictory to me to state that the authors have used unsupervised ML approach when at the same time had clear understanding of the data and the features they wanted to capture. Unsupervised approaches are meant to reveal features that are not apparent by eye... however in their response the authors state, "...our aim was to develop an unsupervised approach that would automatically detect the onset and existence of the key features of pulse generator cyclicity that were apparent by eye...". This sounds like a rather supervised ML approach to me.

Furthermore, I am still unsure why did the authors choose k=5, i.e. assumed there are 5 clusters in the data, and did they explore other possible values for k?

- If not why not? How does this fit with the claims that their ML approach is unsupervised, in other words purely data-driven without making any assumptions?

- If yes did they compare the robustness of their clustering results obtained for different values of k?


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97179.3.sa2](https://doi.org/10.7554/eLife.97179.3.sa2)

Summary:

Zhou and colleagues elegantly used pre-clinical mouse models to understand the nature of abnormally high GnRH/LH pulse secretion in polycystic ovary syndrome (PCOS), a major endocrine disorder affecting female fertility worldwide. This work brings a fundamental question of how altered gonadotropin secretion takes place upstream within the GnRH pulse generator core, which is defined by arcuate nucleus kisspeptin neurons.

Strengths:

Authors use state-of-the-art in vivo calcium imaging with fiber photometry and important physiological manipulations and measurements to dissect the possible neuronal mechanisms underlying such neuroendocrine derangements in PCOS. The additional use of unsupervised k-means clustering analysis for the evaluation of calcium synchronous events greatly enhances the quality of their evidence. The authors nicely propose that neuroendocrine dysfunction in PCOS might involve different setpoints through the hypothalamic-pituitary-gonadal (HPG) axis, and beyond kisspeptin neurons, which importantly pushes our field forward toward future investigations.

Weaknesses:

The reviewer agrees that the authors provide important evidence and have improved the quality of the manuscript following first-round revisions. However, they seem resistant to show frequency and amplitude averages in Figure 1 or as supplemental data. Whether the amplitude is dependent on fiber position and its influences on the analysis should be a point of discussion and not data omission. A more detailed analysis of frequency data would enhance the quality of their manuscript.

Comments on revised version:

This comment is related to Reviewer 3's comment # 2 (major) response:

The response does not justify why authors could simply show frequency and amplitude averages in Figure 1 or as supplemental data. Whether the amplitude is dependent on fiber position and its influences on the analysis should be a point of discussion and not data omission.
