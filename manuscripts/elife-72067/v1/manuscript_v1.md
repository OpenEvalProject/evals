# Shallow neural networks trained to detect collisions recover features of visual loom-selective neurons

## Authors

- Baohua Zhou<sup>1</sup>
- Zifan Li<sup>2</sup>
- Sunnie Kim<sup>2</sup> ([ORCID: 0000-0002-8901-7233](https://orcid.org/0000-0002-8901-7233))
- John Lafferty<sup>2</sup> †
- Damon A Clark<sup>1</sup> ([ORCID: 0000-0001-8487-700X](https://orcid.org/0000-0001-8487-700X)) †

### Affiliations

1. Department of Molecular, Cellular and Developmental Biology Yale University New Haven United States
2. Department of Statistics and Data Science Yale University New Haven United States

† Corresponding author

## Abstract

Animals have evolved sophisticated visual circuits to solve a vital inference problem: detecting whether or not a visual signal corresponds to an object on a collision course. Such events are detected by specific circuits sensitive to visual looming, or objects increasing in size. Various computational models have been developed for these circuits, but how the collision-detection inference problem itself shapes the computational structures of these circuits remains unknown. Here, inspired by the distinctive structures of LPLC2 neurons in the visual system of Drosophila, we build anatomically-constrained shallow neural network models and train them to identify visual signals that correspond to impending collisions. Surprisingly, the optimization arrives at two distinct, opposing solutions, only one of which matches the actual dendritic weighting of LPLC2 neurons. Both solutions can solve the inference problem with high accuracy when the population size is large enough. The LPLC2-like solutions reproduces experimentally observed LPLC2 neuron responses for many stimuli, and reproduces canonical tuning of loom sensitive neurons, even though the models are never trained on neural data. Thus, LPLC2 neuron properties and tuning are predicted by optimizing an anatomically-constrained neural network to detect impending collisions. More generally, these results illustrate how optimizing inference tasks that are important for an animal's perceptual goals can reveal and explain computational properties of specific sensory neurons.
