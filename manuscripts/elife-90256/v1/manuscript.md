# Emergence of brain-like mirror-symmetric viewpoint tuning in convolutional neural networks

## Authors

- Amirhossein Farzmahdi<sup>1</sup> ([ORCID: 0000-0001-6926-546X](https://orcid.org/0000-0001-6926-546X))
- Wilbert Zarco<sup>1</sup> ([ORCID: 0000-0002-3599-0476](https://orcid.org/0000-0002-3599-0476))
- Winrich A Freiwald<sup>1</sup> ([ORCID: 0000-0001-8456-5030](https://orcid.org/0000-0001-8456-5030))
- Nikolaus Kriegeskorte<sup>2</sup> ([ORCID: 0000-0001-7433-9005](https://orcid.org/0000-0001-7433-9005))
- Tal Golan<sup>2</sup> ([ORCID: 0000-0002-7940-7473](https://orcid.org/0000-0002-7940-7473)) †

### Affiliations

1. Laboratory of Neural Systems Rockefeller University New York United States
2. Zuckerman Mind Brain Behavior Institute Columbia University New York United States

† Corresponding author

## Abstract

Primates can recognize objects despite 3D geometric variations such as in-depth rotations. The computational mechanisms that give rise to such invariances are yet to be fully understood. A curious case of partial invariance occurs in the macaque face-patch AL and in fully connected layers of deep convolutional networks in which neurons respond similarly to mirror-symmetric view (e.g., left and right profiles). Why does this tuning develop? Here, we propose a simple learning-driven explanation for mirror-symmetric viewpoint tuning. We show that mirror-symmetric viewpoint tuning for faces emerges in the fully connected layers of convolutional deep neural networks trained on object recognition tasks, even when the training dataset does not include faces. First, using 3D objects rendered from multiple views as test stimuli, we demonstrate that mirror-symmetric viewpoint tuning in convolutional neural network models is not unique to faces: it emerges for multiple object categories with bilateral symmetry. Second, we show why this invariance emerges in the models. Learning to discriminate among bilaterally symmetric object categories induces reflection-equivariant intermediate representations. AL-like mirror-symmetric tuning is achieved when such equivariant responses are spatially pooled by downstream units with sufficiently large receptive fields. These results explain how mirror-symmetric viewpoint tuning can emerge in neural networks, providing a theory of how they might emerge in the primate brain. Our theory predicts that mirror-symmetric viewpoint tuning can emerge as a consequence of exposure to bilaterally symmetric objects beyond the category of faces, and that it can generalize beyond previously experienced object categories.
