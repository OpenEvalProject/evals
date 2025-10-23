# Peer review - Round 1

Editors:
- Lukas Folkman

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.93242.4.sa0](https://doi.org/10.7554/eLife.93242.4.sa0)

This valuable study presents a machine learning model to recommend effective antimicrobial drugs from patients' samples analyzed with mass spectrometry. The evidence supporting the claims of the authors is convincing. This work will be of interest to computational biologists, microbiologists, and clinicians.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.93242.4.sa1](https://doi.org/10.7554/eLife.93242.4.sa1)

De Waele et al. framed the mass-spectrum-based prediction of antimicrobial resistance (AMR) prediction as a drug recommendation task. Neural networks were trained on the recently available DRIAMS database of MALDI-TOF (matrix-assisted laser desorption/ionization time-of-flight) mass spectrometry data and their associated antibiotic susceptibility profiles (Weis et al. 2022). Weis et al. (2022) also introduced the benchmark models which take as the input a single species and are trained to predict resistance to a single drug. Instead here, a pair of drugs and spectrum are fed to two neural network models to predict a resistance probability. In this manner, knowledge from different drugs and species can be shared through the model parameters. Questions asked: What is the best way to encode the drugs? Does the dual neural network outperform the single spectrum-drug network?

The authors showed consistent performance of their strategy to predict antibiotic susceptibility for different spectrum and antibiotic representations (i.e., embedders). Remarkably, the authors showed how small datasets collected at one location can improve the performance of a model trained with limited data collected at a second location. The authors also showed that species-specific models (trained in multiple antibiotic resistance profiles) outperformed both the single recommender model and the individual species-antibiotic combination models.

Strengths:

• A single antimicrobial resistance recommender system could potentially facilitate the adoption of MALDI-TOF based antibiotic susceptibility profiling into clinical practices by reducing the number of models to be considered, and the efforts that may be required to periodically update them.

• The authors tested multiple combinations of embedders for the mass spectra and antibiotics while using different metrics to evaluate the performance of the resulting models. Models trained using different spectrum embedder-antibiotic embedder combinations had remarkably good performance for all tested metrics. The average ROC AUC scores for global and species-specific evaluations were above 0.8.

• Authors developed species-specific recommenders as an intermediate layer between the single recommender system and single species-antibiotic models. This intermediate approach achieved maximum performance (with one type of the species-specific recommender achieving a 0.9 ROC AUC), outlining the potential of this type of recommenders for frequent pathogens.

• Authors showed that data collected in one location can be leveraged to improve the performance of models generated using a smaller number of samples collected at a different location. This result may encourage researchers to optimize data integration to reduce the burden of data generation for institutions interested in testing this method.

Weaknesses:

• Authors do not offer information about the model features associated with resistance. While reviewers understand that it is difficult to map mass spectra to specific pathways or metabolites, mechanistic insights are much more important in the context of AMR than in the context of bacterial identification. For example, this information may offer additional antimicrobial targets. Thus, authors should at least identify mass spectra peaks highly associated with resistance profiles. Are those peaks consistent across species? This would be a key step towards a proteomic survey of mechanisms of AMR. See previous work on this topic (Hrabak et al. 2013, Torres-Sangiao et al. 2022).

References:

Hrabak et al. (2013). Clin Microbiol Rev 26. doi: 10.1128/CMR.00058-12.

Torres-Sangiao et al. (2022). Front Med 9. doi: 10.3389/fmed.2022.850374.

Weis et al. (2022). Nat Med 28. doi: 10.1038/s41591-021-01619-9.
