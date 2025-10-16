# Author response - Round 1

Authors:
- Yang Tan ([ORCID: 0009-0004-7261-1705](https://orcid.org/0009-0004-7261-1705))
- Bingxin Zhou ([ORCID: 0000-0002-3897-9766](https://orcid.org/0000-0002-3897-9766))
- Lirong Zheng ([ORCID: 0000-0001-6803-5048](https://orcid.org/0000-0001-6803-5048))
- Guisheng Fan
- Liang Hong ([ORCID: 0000-0003-0107-336X](https://orcid.org/0000-0003-0107-336X))

## Response text

DOI: [10.7554/eLife.98033.4.sa3](https://doi.org/10.7554/eLife.98033.4.sa3)

The following is the authors’ response to the previous reviews.

Response to Reviewer 1

Thank you for your recognition of our revised work.

Response to Reviewer 2

It would be useful to have a demonstration of where this model outperforms SaProt systematically, and a discussion about what the success of this model teaches us given there is a similar, previously successful model, SaProt.

As two concurrent works, ProtSSN and SaProt employ different methods to incorporate the structure information of proteins. Generally speaking, for two deep learning models that are developed during a close period, it is challenging to conclude that one model is systematically superior to another. Nonetheless, on DTm and DDG (the two low-throughput datasets that we constructed), ProtSSN demonstrates better empirical performance than SaProt.

Moreover, ProtSSN is more efficient in both training and inference compared to SaProt. In terms of training cost, SaProt uses 40 million protein structures for pretraining (requiring 64 A100 GPUs for three months), whereas ProtSSN requires only about 30,000 crystal structures from the CATH database (trained on a single 3090 GPU for two days). Despite SaProt’s significantly higher training cost, its pretrained version does not exhibit superior performance on low-throughput datasets such as DTm, DDG, and Clinvar. Furthermore, the high training cost limits many users from retraining or fine-tuning the model for specific needs or datasets.

Regarding the inference cost, ProtSSN requires only one embedding computation for a wild-type protein, regardless of the number of mutants (n). In contrast, SaProt computes a separate embedding and score for each mutant. For instance, when evaluating the scoring performance on ProteinGym, ProtSSN only needs 217 inferences, while SaProt needs more than 2M inferences. This inference speed is important in practice, such as high-throughput design and screening.

Please remove the reference to previous methods as "few shot". This typically refers to their being trained on experimental data, not their using MSAs. A "few shot" model would be ProteinNPT.

The definition of "few-shot" we used here is following ESM1v [1]. This concept originates from providing a certain number of examples as input to GPT-3 [2]. In the context of protein deep learning models, MSA serves as the wild-type protein examples.

Also, Reviewer 1 uses the concept in the same way.

“Readers should note that methods labelled as "few-shot" in comparisons do not make use of experimental labels, but rather use sequences inferred as homologous; these sequences are also often available even if the protein has never been experimentally tested.”

In the main text, we also included this definition as well as the reference of ESM-1v in lines 457-458.

“We extend the evaluation on ProteinGym v0 to include a comparison of our zero-shot ProtSSN with few-shot learning methods that leverage MSA information of proteins (Meier et al., 2021).”

(1) Meier J, Rao R, Verkuil R, et al. Language models enable zero-shot prediction of the effects of mutations on protein function. Advances in Neural Information Processing Systems, 2021.

(2) Brown T, Mann B, Ryder N, et al. Language models are few-shot learners. Advances in Neural Information Processing Systems, 2020.

Furthermore, I don't think it is fair to state that your method is not comparable to these models -- one can run an MSA just as one can predict a structure. A fairer comparison would be to highlight particular assays for which getting an MSA could be challenging -- Transcription did this by showing that they outperform EVE when MSAs are shallow.

We recognize that there are often differences in the definitions and classifications of various methodologies. Here, we follow the definitions provided by ProteinGym. As the most comprehensive and large scale open benchmark in the community, we believe this classification scheme should be widely accepted. All classifications are available on the official website of ProteinGym (https://proteingym.org/benchmarks), which categorizes methods into PLMs, Structure-based models, and Alignment-based models. For example, GEMME is classified as an alignment-based model, and MSA Transformer is considered a hybrid model combining alignment and PLM features.

We believe that methodologies with different inputs and architectures can lead to inherent unfairness. Also, it is generally believed that models including evolutionary relationships tend to outperform end-to-end models due to the extra information and efforts involved during the training phase. Some empirical evidence and discussions are in the ablation studies of retrieval factors in Tranception [3]. Moreover, the choice of MSA search parameters can introduce uncertainty, which could have positive or negative impacts.

We showcase the impact of MSA depth on model performance with an additional analysis below. Author response image 1 visualizes the Spearman’s correlation between the scores of each model and the number of MSAs on 217 ProteinGym assays, where each point represents one of 217 assays. The summary correlation of each model with respect to all assays are reported in Author response table 1. These results demonstrate no clear correlation between MSA depth and model performance even for MSA-based models.

(3) Notin P, Dias M, Frazer J, et al. Tranception: protein fitness prediction with autoregressive transformers and inference-time retrieval. International Conference on Machine Learning, 2022.

The authors state that DTm and DDG are conceptually appealing because they come from low-throughput assays with lower experimental noise and are also mutations that are particularly chosen to represent the most interesting regions of the protein. I agree with the conceptual appeal but I don't think these claims have been demonstrated in practice. The cited comparison with Frazer as a particularly noisy source of data I think is particularly unconvincing: ClinVar labels are not only rigorously determined from multiple sources of evidence, Frazer et al demonstrates that these labels are actually more reliable than experiment in some cases. They also state that ProteinGym data doesn't come with environmental conditions, but these can be retrieved from the papers the assays came from. The paper would be strengthened by a demonstration of the conceptual benefit of these new datasets, say a comparison of mutations and signal for a protein that may be in one of these datasets vs ProteinGym.

In the work by Frazer et al. [4], they mentioned that

"However, these technologies do not easily scale to thousands of proteins, especially not to combinations of variants, and depend critically on the availability of assays that are relevant to or at least associated with human disease phenotypes."

It points out that the results of high-throughput experiments are usually based on the design of specific genes (such as BRCA1 and TP53.) and cannot be easily extended to thousands of other genes. At the same time, due to the complexity of the experiment, there may be problems with reproducibility or deviations from clinical relevance.

This statement aligns with our perspective that high-throughput experiments inherently involve a significant amount of noise and error. It is important to clarify that the noise we discuss here arises from the limitations of high-throughput experiments themselves, instead of from the reliability of the data sources, such as systematic errors in experimental measurements. This latter issue is a complex problem common to all wetlab experiments and falls outside the scope of our study.

Under this premise, low-throughput datasets like DTm and DDG can be considered to have less noise than high-throughput datasets, as they have undergone manual curation. As for your suggestion, while valuable, unfortunately, we were unable to identify datasets in DTM and DDG that align with those in ProteinGym after a careful search. Thus, we are unable to conduct this comparative experiment at this stage.

(4) Frazer J, Notin P, Dias M, et al. Disease variant prediction with deep generative models of evolutionary data. Nature, 2021.
