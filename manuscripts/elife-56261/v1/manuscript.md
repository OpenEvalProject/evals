# Training deep neural density estimators to identify mechanistic models of neural dynamics

## Authors

- Pedro J Gonçalves<sup>1</sup> ([ORCID: 0000-0002-6987-4836](https://orcid.org/0000-0002-6987-4836)) †
- Jan-Matthis Lueckmann<sup>2</sup> ([ORCID: 0000-0003-4320-4663](https://orcid.org/0000-0003-4320-4663)) †
- Michael Deistler<sup>2</sup> †
- Marcel Nonnenmacher<sup>2</sup>
- Kaan Öcal<sup>3</sup> ([ORCID: 0000-0002-8528-6858](https://orcid.org/0000-0002-8528-6858))
- Giacomo Bassetto<sup>1</sup>
- Chaitanya Chintaluri<sup>4</sup> ([ORCID: 0000-0003-4252-1608](https://orcid.org/0000-0003-4252-1608))
- William F Podlaski<sup>5</sup> ([ORCID: 0000-0001-6619-7502](https://orcid.org/0000-0001-6619-7502))
- Sara A Haddad<sup>6</sup>
- Tim Vogels<sup>6</sup>
- David S Greenberg<sup>2</sup>
- Jakob H Macke<sup>7</sup> ([ORCID: 0000-0001-5154-8912](https://orcid.org/0000-0001-5154-8912)) †

### Affiliations

1. Max Planck Research Group Neural Systems Analysis Center of Advanced European Studies and Research (caesar) Bonn Germany
2. Department of Electrical and Computer Engineering Technical University of Munich Munich Germany
3. University of Bonn Mathematical Institute Bonn Germany
4. Department of Physiology, Anatomy and Genetics University of Oxford Oxford United Kingdom
5. Physiology Anatomy and Genetics University of Oxford Oxford United Kingdom
6. Neural Systems and Coding Max-Planck Institute for Brain Research Frankfurt Germany
7. Excellence Cluster Machine Learning University of Tübingen Tübingen Germany

† Corresponding author

## Abstract

Mechanistic modeling in neuroscience aims to explain observed phenomena in terms of underlying causes. However, determining which model parameters agree with complex and stochastic neural data presents a significant challenge. We address this challenge with a machine learning tool which uses deep neural density estimators- trained using model simulations- to carry out Bayesian inference and retrieve the full space of parameters compatible with raw data or selected data features. Our method is scalable in parameters and data features, and can rapidly analyze new data after initial training. We demonstrate the power and flexibility of our approach on receptive fields, ion channels, and Hodgkin-Huxley models. We also characterize the space of circuit configurations giving rise to rhythmic activity in the crustacean stomatogastric ganglion, and use these results to derive hypotheses for underlying compensation mechanisms. Our approach will help close the gap between data-driven and theory-driven models of neural dynamics.
