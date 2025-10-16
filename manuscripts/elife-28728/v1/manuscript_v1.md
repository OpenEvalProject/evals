# Efficient and accurate extraction of in vivo calcium signals from microendoscopic video data

## Authors

- Pengcheng Zhou<sup>1</sup> ([ORCID: 0000-0003-1237-3931](https://orcid.org/0000-0003-1237-3931)) †
- Shanna L Resendez<sup>2</sup>
- Jose Rodriguez-Romaguera<sup>2</sup>
- Jessica C Jimenez<sup>3</sup>
- Shay Q Neufeld<sup>4</sup>
- Andrea Giovannucci<sup>5</sup>
- Johannes Friedrich<sup>5</sup> ([ORCID: 0000-0002-1321-5866](https://orcid.org/0000-0002-1321-5866))
- Eftychios A Pnevmatikakis<sup>5</sup>
- Garret D Stuber<sup>2</sup> ([ORCID: 0000-0003-1730-4855](https://orcid.org/0000-0003-1730-4855))
- Rene Hen<sup>3</sup>
- Mazen A Kheirbek<sup>6</sup>
- Bernardo L Sabatini<sup>4</sup>
- Robert E Kass<sup>1</sup>
- Liam Paninski<sup>7</sup>

### Affiliations

1. Center for the Neural Basis of Cognition and Machine Learning Department Carnegie Mellon University Pittsburgh United States
2. Department of Psychiatry University of North Carolina at Chapel Hill Chapel Hill United States
3. Department of Neuroscience Columbia University New York United States
4. Department of Neurobiology Harvard Medical School Boston United States
5. Center for Computational Biology Flatiron Institute, Simons Foundation New York United States
6. Department of Psychiatry University of California, San Francisco San Francisco United States
7. Department of Statistics Columbia University Columbia United States

† Corresponding author

## Abstract

In vivo calcium imaging through microendoscopic lenses enables imaging of previously inaccessible neuronal populations deep within the brains of freely moving animals. However, it is computationally challenging to extract single-neuronal activity from microendoscopic data, because of the very large background fluctuations and high spatial overlaps intrinsic to this recording modality. Here, we describe a new constrained matrix factorization approach to accurately separate the background and then demix and denoise the neuronal signals of interest. We compared the proposed method against previous independent components analysis and constrained nonnegative matrix factorization approaches. On both simulated and experimental data recorded from mice, our method substantially improved the quality of extracted cellular signals and detected more well-isolated neural signals, especially in noisy data regimes. These advances can in turn significantly enhance the statistical power of downstream analyses, and ultimately improve scientific conclusions derived from microendoscopic data.
