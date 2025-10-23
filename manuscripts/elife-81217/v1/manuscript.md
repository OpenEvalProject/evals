# A generalizable brain extraction net (BEN) for multimodal MRI data from rodents, nonhuman primates, and humans

## Authors

- Ziqi Yu<sup>1</sup> ([ORCID: 0000-0001-8201-5481](https://orcid.org/0000-0001-8201-5481))
- Xiaoyang Han<sup>1</sup> ([ORCID: 0000-0002-3007-6079](https://orcid.org/0000-0002-3007-6079))
- Wenjing Xu<sup>1</sup>
- Jie Zhang<sup>1</sup>
- Carsten Marr<sup>2</sup> ([ORCID: 0000-0003-2154-4552](https://orcid.org/0000-0003-2154-4552))
- Dinggang Shen<sup>3</sup>
- Tingying Peng<sup>4</sup> †
- Xiao-Yong Zhang<sup>1</sup> ([ORCID: 0000-0001-8965-1077](https://orcid.org/0000-0001-8965-1077)) †
- Jianfeng Feng<sup>1</sup> ([ORCID: 0000-0001-5987-2258](https://orcid.org/0000-0001-5987-2258))

### Affiliations

1. Institute of Science and Technology for Brain-Inspired Intelligence Fudan University Shanghai China
2. Institute of AI for Health Helmholtz Zentrum München Neuherberg Germany
3. School of Biomedical Engineering ShanghaiTech University Shanghai China
4. Helmholtz AI Helmholtz Zentrum München Neuherberg Germany

† Corresponding author

## Abstract

Accurate brain tissue extraction on magnetic resonance imaging (MRI) data is crucial for analyzing brain structure and function. While several conventional tools have been optimized to handle human brain data, there have been no generalizable methods to extract brain tissues for multimodal MRI data from rodents, nonhuman primates, and humans. Therefore, developing a flexible and generalizable method for extracting whole brain tissue across species would allow researchers to analyze and compare experiment results more efficiently. Here, we propose a domain-adaptive and semi-supervised deep neural network, named the Brain Extraction Net (BEN), to extract brain tissues across species, MRI modalities, and MR scanners. We have evaluated BEN on 18 independent datasets, including 783 rodent MRI scans, 246 nonhuman primate MRI scans, and 4,601 human MRI scans, covering five species, four modalities, and six MR scanners with various magnetic field strengths. Compared to conventional toolboxes, the superiority of BEN is illustrated by its robustness, accuracy, and generalizability. Our proposed method not only provides a generalized solution for extracting brain tissue across species but also significantly improves the accuracy of atlas registration, thereby benefiting the downstream processing tasks. As a novel fully automated deep-learning method, BEN is designed as an open-source software to enable high-throughput processing of neuroimaging data across species in preclinical and clinical applications.
