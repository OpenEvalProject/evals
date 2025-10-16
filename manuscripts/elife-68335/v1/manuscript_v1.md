# A deep learning algorithm to translate and classify cardiac electrophysiology

## Authors

- Parya Aghasafari<sup>1</sup>
- Pei-Chi Yang<sup>1</sup>
- Divya C Kernik<sup>2</sup>
- Kazuho Sakamoto<sup>3</sup>
- Yasunari Kanda<sup>4</sup> ([ORCID: 0000-0003-2527-3526](https://orcid.org/0000-0003-2527-3526))
- Junko Kurokawa<sup>3</sup>
- Igor Vorobyov<sup>5</sup> ([ORCID: 0000-0002-4767-5297](https://orcid.org/0000-0002-4767-5297))
- Colleen E Clancy<sup>1</sup> ([ORCID: 0000-0001-6849-4885](https://orcid.org/0000-0001-6849-4885)) †

### Affiliations

1. Physiology and Membrane Biology University of California Davis Davis United States
2. Biomedical Engineering Washington University in St. Louis St. Louis United States
3. Bio-Informational Pharmacology University of Shizuoka Shizuoka Japan
4. Division of Pharmacology National Institute of Health Sciences Kanagawa Japan
5. University California Davis Davis United States

† Corresponding author

## Abstract

The development of induced pluripotent stem cell-derived cardiomyocytes (iPSC-CMs) has been a critical in vitro advance in the study of patient-specific physiology, pathophysiology and pharmacology. We designed a new deep learning multitask network approach intended to address the low throughput, high variability and immature phenotype of the iPSC-CM platform. The rationale for combining translation and classification tasks is because the most likely application of the deep learning technology we describe here is to translate iPSC-CMs following application of a perturbation. The deep learning network was trained using simulated action potential (AP) data and applied to classify cells into the drug-free and drugged categories and to predict the impact of electrophysiological perturbation across the continuum of aging from the immature iPSC-CMs to the adult ventricular myocytes. The phase of the AP extremely sensitive to perturbation due to a steep rise of the membrane resistance was found to contain the key information required for successful network multitasking. We also demonstrated successful translation of both experimental and simulated iPSC-CM AP data validating our network by prediction of experimental drug-induced effects on adult cardiomyocyte APs by the latter.
