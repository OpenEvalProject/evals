# Gated recurrence enables simple and accurate sequence prediction in stochastic, changing, and structured environments

## Authors

- Cédric Foucault<sup>1</sup> ([ORCID: 0000-0002-7247-6927](https://orcid.org/0000-0002-7247-6927))
- Florent Meyniel<sup>2</sup> ([ORCID: 0000-0002-6992-678X](https://orcid.org/0000-0002-6992-678X)) †

### Affiliations

1. INSERM, CEA, Université Paris-Saclay Gif sur Yvette France
2. NeuroSpin CEA, Sorbonne Université Gif sur Yvette France

† Corresponding author

## Abstract

From decision making to perception to language, predicting what is coming next is crucial. It is also challenging in stochastic, changing, and structured environments; yet the brain makes accurate predictions in many situations. What computational architecture could enable this feat? Bayesian inference makes optimal predictions but is prohibitively difficult to compute. Here, we show that a specific recurrent neural network architecture enables simple and accurate solutions in several environments. This architecture relies on three mechanisms: gating, lateral connections, and recurrent weight training. Like the optimal solution and the human brain, such networks develop internal representations of their changing environment (including estimates of the environment's latent variables and the precision of these estimates), leverage multiple levels of latent structure, and adapt their effective learning rate to changes without changing their connection weights. Being ubiquitous in the brain, gated recurrence could therefore serve as a generic building block to predict in real-life environments.
