# Bi-channel Image Registration and Deep-learning Segmentation (BIRDS) for efficient, versatile 3D mapping of mouse brain

## Authors

- Xuechun Wang<sup>1</sup>
- Weilin Zeng<sup>1</sup>
- Xiaodan Yang<sup>2</sup>
- Chunyu Fang<sup>1</sup>
- Yunyun Han<sup>2</sup> †
- Peng Fei<sup>1</sup> ([ORCID: 0000-0003-3764-817X](https://orcid.org/0000-0003-3764-817X)) †

### Affiliations

1. School of Optical and Electronic Information Huazhong University of Science and Technology Wuhan China
2. School of Basic Medicine Tongji Medical College, Huazhong University of Science and Technology Wuhan China

† Corresponding author

## Abstract

We have developed an open-source software called BIRDS (bi-channel image registration and deep-learning segmentation) for the mapping and analysis of 3D microscopy data and applied this to the mouse brain. The BIRDS pipeline includes image pre-processing, bi-channel registration, automatic annotation, creation of a 3D digital frame, high-resolution visualization, and expandable quantitative analysis. This new bi-channel registration algorithm is adaptive to various types of whole-brain data from different microscopy platforms and shows dramatically improved registration accuracy. Additionally, as this platform combines registration with neural networks, its improved function relative to other platforms lies in the fact that the registration procedure can readily provide training data for network construction, while the trained neural network can efficiently segment incomplete/defective brain data that is otherwise difficult to register. Our software is thus optimized to enable either minute-timescale registration-based segmentation of cross-modality, whole-brain datasets or real-time inference-based image segmentation of various brain regions of interest. Jobs can be easily submitted and implemented via a Fiji plugin that can be adapted to most computing environments.
