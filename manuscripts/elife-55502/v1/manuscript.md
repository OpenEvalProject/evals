# Revealing architectural order with quantitative label-free imaging and deep learning

## Authors

- Syuan-Ming Guo<sup>1</sup>
- Li-Hao Yeh<sup>1</sup> ([ORCID: 0000-0003-2803-5996](https://orcid.org/0000-0003-2803-5996))
- Jenny Folkesson<sup>2</sup> ([ORCID: 0000-0002-4673-0522](https://orcid.org/0000-0002-4673-0522))
- Ivan E Ivanov<sup>1</sup>
- Anitha P Krishnan<sup>2</sup>
- Matthew G Keefe<sup>3</sup>
- Ezzat Hashemi<sup>4</sup>
- David Shin<sup>3</sup>
- Bryant B Chhun<sup>1</sup>
- Nathan H Cho<sup>5</sup>
- Manuel D Leonetti<sup>5</sup>
- May H Han<sup>4</sup>
- Tomasz Nowakowski<sup>3</sup>
- Shalin B Mehta<sup>1</sup> ([ORCID: 0000-0002-2542-3582](https://orcid.org/0000-0002-2542-3582)) †

### Affiliations

1. Computational Microscopy Chan Zuckerberg Biohub San Francisco United States
2. Data Science Chan Zuckerberg Biohub San Francisco United States
3. Anatomy UCSF School of Medicine San Francisco United States
4. Department of Neurology Stanford University Stanford United States
5. Cell Atlas Chan Zuckerberg Biohub San Francisco United States

† Corresponding author

## Abstract

We report quantitative label-free imaging with phase and polarization (QLIPP) for simultaneous measurement of density, anisotropy, and orientation in unlabeled live cells and tissue slices. We combine QLIPP with deep neural networks to predict fluorescence images of diverse cell and tissue structures. QLIPP images reveal anatomical regions and axon tract orientation in prenatal human brain tissue sections that are not visible using brightfield imaging. We report a variant of UNet architecture, multi-channel 2.5D U-Net, for computationally efficient prediction of fluorescence images in three dimensions and over large fields of view. Further, we develop data normalization methods for accurate prediction of myelin distribution over large brain regions. We show that experimental defects in labeling the human tissue can be rescued with quantitative label-free imaging and neural network model. We anticipate that the proposed method will enable new studies of architectural order at spatial scales ranging from organelles to tissue.
