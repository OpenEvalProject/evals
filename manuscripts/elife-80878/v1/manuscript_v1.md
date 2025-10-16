# Towards a more informative representation of the fetal-neonatal brain connectome using variational autoencoder

## Authors

- Jung-Hoon Kim<sup>1</sup> ([ORCID: 0000-0003-3032-8827](https://orcid.org/0000-0003-3032-8827))
- Josepheen De Asis-Cruz<sup>1</sup>
- Dhineshvikram Krishnamurthy<sup>1</sup>
- Catherine Limperopoulos<sup>1</sup> ([ORCID: 0000-0003-1735-0069](https://orcid.org/0000-0003-1735-0069)) †

### Affiliations

1. Developing Brain Institute Children's National Hospital Washington United States

† Corresponding author

## Abstract

Recent advances in functional magnetic resonance imaging (fMRI) have helped elucidate previously inaccessible trajectories of early-life prenatal and neonatal brain development. To date, the interpretation of fetal-neonatal fMRI data has relied on linear analytic models, akin to adult neuroimaging data. However, unlike the adult brain, the fetal and newborn brain develops extraordinarily rapidly, far outpacing any other brain development period across the lifespan. Consequently, conventional linear computational models may not adequately capture these accelerated and complex neurodevelopmental trajectories during this critical period of brain development along the prenatal-neonatal continuum. To obtain a nuanced understanding of fetal-neonatal brain development, including non-linear growth, for the first time, we developed quantitative, systems-wide representations of brain activity in a large sample (>500) of fetuses, preterm, and full-term neonates using an unsupervised deep generative model called Variational Autoencoder (VAE), a model previously shown to be superior to linear models in representing complex resting state data in healthy adults. Here, we demonstrated that non-linear brain features, i.e., latent variables, derived with the VAE pretrained on rsfMRI of human adults, carried important individual neural signatures, leading to improved representation of prenatal-neonatal brain maturational patterns and more accurate and stable age prediction in the neonate cohort compared to linear models. Using the VAE decoder, we also revealed distinct functional brain networks spanning the sensory and default mode networks. Using the VAE, we are able to reliably capture and quantify complex, non-linear fetal-neonatal functional neural connectivity. This will lay the critical foundation for detailed mapping of healthy and aberrant functional brain signatures that have their origins in fetal life.
