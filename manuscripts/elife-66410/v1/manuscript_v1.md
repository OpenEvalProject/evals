# Fast deep neural correspondence for tracking and identifying neurons in C. elegans using semi-synthetic training

## Authors

- Xinwei Yu<sup>1</sup>
- Matthew S Creamer<sup>2</sup>
- Francesco Randi<sup>1</sup>
- Anuj Kumar Sharma<sup>1</sup> ([ORCID: 0000-0001-5061-9731](https://orcid.org/0000-0001-5061-9731))
- Scott W Linderman<sup>3</sup> ([ORCID: 0000-0002-3878-9073](https://orcid.org/0000-0002-3878-9073))
- Andrew Michael Leifer<sup>4</sup> ([ORCID: 0000-0002-5362-5093](https://orcid.org/0000-0002-5362-5093)) †

### Affiliations

1. Department of Physics Princeton University Princeton United States
2. Princeton Neuroscience Institute Princeton University Princeton United States
3. Department of Statistics Stanford University Stanford United States
4. Department of Physics and Princeton Neuroscience Institute Princeton University Princeton United States

† Corresponding author

## Abstract

We present an automated method to track and identify neurons in C. elegans, called 'fast Deep Neural Correspondence' or fDNC, based on the transformer network architecture. The model is trained once on empirically derived semi-synthetic data and then predicts neural correspondence across held-out real animals. The same pre-trained model both tracks neurons across time and identifies corresponding neurons across individuals. Performance is evaluated against hand-annotated datasets, including NeuroPAL [1]. Using only position information, the method achieves 79.1% accuracy at tracking neurons within an individual and 64.1% accuracy at identifying neurons across individuals. Accuracy at identifying neurons across individuals is even higher (78.2%) when the model is applied to a dataset published by another group [2]. Accuracy reaches 74.7% on our dataset when using color information from NeuroPAL. Unlike previous methods, fDNC does not require straightening or transforming the animal into a canonical coordinate system. The method is fast and predicts correspondence in 10ms making it suitable for future real-time applications.
