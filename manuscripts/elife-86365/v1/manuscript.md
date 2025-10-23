# BrainPy, a flexible, integrative, efficient, and extensible framework for general-purpose brain dynamics programming

## Authors

- Chaoming Wang<sup>1</sup>
- Tianqiu Zhang<sup>1</sup>
- Xiaoyu Chen<sup>1</sup>
- Sichao He<sup>2</sup>
- Shangyang Li<sup>1</sup>
- Si Wu<sup>1</sup> ([ORCID: 0000-0001-9650-6935](https://orcid.org/0000-0001-9650-6935)) †

### Affiliations

1. School of Psychological and Cognitive Sciences Peking University Beijing China
2. Beijing Jiaotong University Beijing China

† Corresponding author

## Abstract

Elucidating the intricate neural mechanisms underlying brain functions requires integrative brain dynamics modeling. To facilitate this process, it is crucial to develop a general-purpose programming framework that allows users to freely define neural models across multiple scales, efficiently simulate, train, and analyze model dynamics, and conveniently incorporate new modeling approaches. In response to this need, we present BrainPy. BrainPy leverages the advanced just-in-time (JIT) compilation capabilities of JAX and XLA to provide a powerful infrastructure tailored for brain dynamics programming. It offers an integrated platform for building, simulating, training, and analyzing brain dynamics models. Models defined in BrainPy can be JIT compiled into binary instructions for various devices, including Central Processing Unit (CPU), Graphics Processing Unit (GPU), and Tensor Processing Unit (TPU), which ensures high running performance comparable to native C or CUDA. Additionally, BrainPy features an extensible architecture that allows for easy expansion of new infrastructure, utilities, and machine-learning approaches. This flexibility enables researchers to incorporate cutting-edge techniques and adapt the framework to their specific needs
