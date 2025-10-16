# Development and evaluation of a live birth prediction model for evaluating human blastocysts: a retrospective study

## Authors

- Hang Liu<sup>1</sup> ([ORCID: 0000-0001-7948-4236](https://orcid.org/0000-0001-7948-4236))
- Zhuoran Zhang<sup>2</sup>
- Yifan Gu<sup>3</sup>
- Changsheng Dai<sup>1</sup>
- Guanqiao Shan<sup>1</sup>
- Haocong Song<sup>1</sup>
- Daniel Li<sup>1</sup>
- Wenyuan Chen<sup>1</sup>
- Ge Lin<sup>3</sup> †
- Yu Sun<sup>1</sup> ([ORCID: 0000-0001-7895-0741](https://orcid.org/0000-0001-7895-0741)) †

### Affiliations

1. Department of Mechanical Engineering University of Toronto Toronto Canada
2. School of Science and Engineering Chinese University of Hong Kong, Shenzhen Shenzhen China
3. Institute of Reproductive and Stem Cell Engineering Central South University Changsha China

† Corresponding author

## Abstract

Background: In infertility treatment, blastocyst morphological grading is commonly used in clinical practice for blastocyst evaluation and selection, but has shown limited predictive power on live birth outcomes of blastocysts. To improve live birth prediction, a number of artificial intelligence (AI) models have been established. Most existing AI models for blastocyst evaluation only used images for live birth prediction, and the area under the receiver operating characteristic (ROC) curve (AUC) achieved by these models has plateaued at ~0.65. Methods: This study proposed a multi-modal blastocyst evaluation method using both blastocyst images and  patient couple's clinical features (e.g., maternal age, hormone profiles, endometrium thickness, and semen quality) to predict live birth outcomes of human blastocysts. To utilize the multi-modal data, we developed a new AI model consisting of a convolutional neural network (CNN) to process blastocyst images and a multi-layer perceptron to process patient couple's clinical features. The dataset used in this study consists of 17,580 blastocysts with known live birth outcomes, blastocyst images, and patient couple's clinical features. Results: This study achieved an AUC of 0.77 for live birth prediction, which significantly outperforms related works in the literature. Sixteen out of 103 clinical features were identified to be predictors of live birth outcomes and helped improve live birth prediction. Among these features, maternal age, the day of blastocyst transfer, antral follicle count, retrieved oocyte number, and endometrium thickness measured before transfer are the top five features contributing to live birth prediction. Heatmaps showed that the CNN in the AI model mainly focuses on image regions of inner cell mass and trophectoderm (TE) for live birth prediction, and the contribution of TE-related features was greater in the CNN trained with the inclusion of patient couple's clinical features compared with the CNN trained with blastocyst images alone. Conclusions: The results suggest that the inclusion of patient couple's clinical features along with blastocyst images increases live birth prediction accuracy. Funding: Natural Sciences and Engineering Research Council of Canada and the Canada Research Chairs Program.
