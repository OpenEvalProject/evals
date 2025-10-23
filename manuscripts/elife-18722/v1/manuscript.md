# Accelerated cryo-EM structure determination with parallelisation using GPUs in RELION-2

## Authors

- Dari Kimanius<sup>1</sup>
- Björn O Forsberg<sup>2</sup>
- Sjors HW Scheres<sup>3</sup> ([ORCID: 0000-0002-0462-6540](https://orcid.org/0000-0002-0462-6540)) †
- Erik Lindahl<sup>1</sup> ([ORCID: 0000-0002-2734-2794](https://orcid.org/0000-0002-2734-2794)) †

### Affiliations

1. Department of Biochemistry and Biophysics, Science for Life Laboratory Stockholm University Stockholm Sweden
2. Department of Biochemistry and Biophysics, Science for Life Laboratory Stockholm University Stockholm Sweden
3. MRC Laboratory of Molecular Biology Cambridge United Kingdom

† Corresponding author

## Abstract

By reaching near-atomic resolution for a wide range of specimens, single-particle cryo-EM structure determination is transforming structural biology. However, the necessary calculations come at increased computational costs, introducing a bottleneck that is currently limiting throughput and the development of new methods. Here, we present an implementation of the RELION image processing software that uses graphics processors (GPUs) to address the most computationally intensive steps of its cryo-EM structure determination workflow. Both image classification and high-resolution refinement have been accelerated more than an order-of-magnitude, and template-based particle selection has been accelerated two orders-of-magnitude on desktop hardware. Memory requirements on GPUs have been reduced to fit widely available hardware, and we show that the use of single precision arithmetic does not adversely affect results. This enables high-resolution cryo-EM structure determination in a matter of days on a single workstation.
