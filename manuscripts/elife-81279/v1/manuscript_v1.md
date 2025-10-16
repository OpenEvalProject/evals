# Granger causality analysis for calcium transients in neuronal networks, challenges and improvements

## Authors

- Xiaowen Chen<sup>1</sup>
- Faustine Ginoux<sup>2</sup>
- Martin Carbo-Tano<sup>2</sup> ([ORCID: 0000-0002-1936-7174](https://orcid.org/0000-0002-1936-7174))
- Thierry Mora<sup>1</sup> ([ORCID: 0000-0002-5456-9361](https://orcid.org/0000-0002-5456-9361)) †
- Aleksandra M Walczak<sup>1</sup> ([ORCID: 0000-0002-2686-5702](https://orcid.org/0000-0002-2686-5702)) †
- Claire Wyart<sup>2</sup> ([ORCID: 0000-0002-1668-4975](https://orcid.org/0000-0002-1668-4975)) †

### Affiliations

1. Laboratoire de physique de l'École normale supérieure CNRS Paris France
2. Spinal Sensory Signaling team Institut du Cerveau Paris France

† Corresponding author

## Abstract

One challenge in neuroscience is to understand how information flows between neurons in vivo to trigger specific behaviors. Granger causality (GC) has been proposed as a simple and effective measure for identifying dynamical interactions. At single-cell resolution however, GC analysis is rarely used compared to directionless correlation analysis. Here, we study the applicability of GC analysis for calcium imaging data in diverse contexts. We first show that despite underlying linearity assumptions, GC analysis successfully retrieves non-linear interactions in a synthetic network simulating intracellular calcium fluctuations of spiking neurons. We highlight the potential pitfalls of applying GC analysis on real in vivo calcium signals, and offer solutions regarding the choice of GC analysis parameters. We took advantage of calcium imaging datasets from motoneurons in embryonic zebrafish to show how the improved GC can retrieve true underlying information flow. Applied to the network of brainstem neurons of larval zebrafish, our pipeline reveals strong driver neurons in the locus of the mesencephalic locomotor region (MLR), driving target neurons matching expectations from anatomical and physiological studies. Altogether, this practical toolbox can be applied on in vivo population calcium signals to increase the selectivity of GC to infer flow of information across neurons.
