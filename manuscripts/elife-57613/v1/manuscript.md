# Accurate and versatile 3D segmentation of plant tissues at cellular resolution

## Authors

- Adrian Wolny<sup>1</sup>
- Lorenzo Cerrone<sup>2</sup>
- Athul Vijayan<sup>3</sup>
- Rachele Tofanelli<sup>3</sup> ([ORCID: 0000-0002-5196-1122](https://orcid.org/0000-0002-5196-1122))
- Amaya Vilches Barro<sup>4</sup>
- Marion Louveaux<sup>4</sup>
- Christian Wenzl<sup>5</sup>
- Sören Strauss<sup>6</sup>
- David Wilson-Sánchez<sup>6</sup>
- Rena Lymbouridou<sup>6</sup>
- Susanne Steigleder<sup>4</sup>
- Constantin Pape<sup>1</sup>
- Alberto Bailoni<sup>2</sup>
- Salva Duran-Nebreda<sup>7</sup>
- George Bassel<sup>7</sup>
- Jan U Lohmann<sup>5</sup> ([ORCID: 0000-0003-3667-187X](https://orcid.org/0000-0003-3667-187X))
- Miltos Tsiantis<sup>6</sup>
- Fred Hamprecht<sup>5</sup>
- Kay Schneitz<sup>3</sup> ([ORCID: 0000-0001-6688-0539](https://orcid.org/0000-0001-6688-0539))
- Alexis Maizel<sup>5</sup>
- Anna Kreshuk<sup>1</sup> ([ORCID: 0000-0003-1334-6388](https://orcid.org/0000-0003-1334-6388)) †

### Affiliations

1. Cell Biology and Biophysics Unit EMBL Heidelberg Germany
2. Heidelberg Collaboratory for Image Processing Heidelberg University Heidelberg Germany
3. School of Life Sciences Weihenstephan Technical University of Munich Freising Germany
4. Centre for Organismal Studies Heidelberg University Heidelberg Germany
5. Department of Stem Cell Biology, Centre for Organismal Studies Heidelberg University Heidelberg Germany
6. Department of Comparative Development and Genetics Max Planck Institute for Plant Breeding Research Cologne Germany
7. School of Life Sciences University of Warwick Coventry United Kingdom

† Corresponding author

## Abstract

Quantitative analysis of plant and animal morphogenesis requires accurate segmentation of individual cells in volumetric images of growing organs. In the last years, deep learning has provided robust automated algorithms that approach human performance, with applications to bio-image analysis now starting to emerge. Here, we present PlantSeg, a pipeline for volumetric segmentation of plant tissues into cells. PlantSeg employs a convolutional neural network to predict cell boundaries and graph partitioning to segment cells based on the neural network predictions. PlantSeg was trained on 1xed and live plant organs imaged with confocal and light sheet microscopes. PlantSeg delivers accurate results and generalizes well across different tissues, scales, acquisition settings even on non plant samples. We present results of PlantSeg applications in diverse developmental contexts. PlantSeg is free and open-source, with both a command line and a user-friendly graphical interface (https://github.com/hci-unihd/plant-seg).
