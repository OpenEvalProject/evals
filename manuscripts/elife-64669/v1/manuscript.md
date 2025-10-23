# Detecting adaptive introgression in human evolution using convolutional neural networks

## Authors

- Graham Gower<sup>1</sup> ([ORCID: 0000-0002-6197-3872](https://orcid.org/0000-0002-6197-3872)) †
- Pablo Iáñez Picazo<sup>1</sup>
- Matteo Fumagalli<sup>2</sup> ([ORCID: 0000-0002-4084-2953](https://orcid.org/0000-0002-4084-2953))
- Fernando Racimo<sup>1</sup> ([ORCID: 0000-0002-5025-2607](https://orcid.org/0000-0002-5025-2607))

### Affiliations

1. Lundbeck GeoGenetics Centre, Globe Institute University of Copenhagen Copenhagen Denmark
2. Imperial College London London United Kingdom

† Corresponding author

## Abstract

Studies in a variety of species have shown evidence for positively selected variants introduced into a population via introgression from another, distantly related population - a process known as adaptive introgression. However, there are few explicit frameworks for jointly modelling introgression and positive selection, in order to detect these variants using genomic sequence data. Here, we develop an approach based on convolutional neural networks (CNNs). CNNs do not require the specification of an analytical model of allele frequency dynamics, and have outperformed alternative methods for classification and parameter estimation tasks in various areas of population genetics. Thus, they are potentially well suited to the identification of adaptive introgression. Using simulations, we trained CNNs on genotype matrices derived from genomes sampled from the donor population, the recipient population and a related non-introgressed population, in order to distinguish regions of the genome evolving under adaptive introgression from those evolving neutrally or experiencing selective sweeps. Our CNN architecture exhibits 95% accuracy on simulated data, even when the genomes are unphased, and accuracy decreases only moderately in the presence of heterosis. As a proof of concept, we applied our trained CNNs to human genomic datasets - both phased and unphased - to detect candidates for adaptive introgression that shaped our evolutionary history.
