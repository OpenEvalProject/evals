# Selecting the most appropriate time points to profile in high-throughput studies

## Authors

- Michael Kleyman<sup>1</sup>
- Emre Sefer<sup>1</sup>
- Teodora Nicola<sup>2</sup>
- Celia Espinoza<sup>3</sup>
- Divya Chhabra<sup>3</sup>
- James S Hagood<sup>3</sup>
- Naftali Kaminski<sup>4</sup>
- Namasivayam Ambalavanan<sup>5</sup>
- Ziv Bar-Joseph<sup>1</sup> ([ORCID: 0000-0003-3430-6051](https://orcid.org/0000-0003-3430-6051)) †

### Affiliations

1. Machine Learning and Computational Biology, School of Computer Science Carnegie Mellon University Pittsburgh United States
2. Department  of Pediatrics, Division of Neonatology University of Alabama at Birmingham Birmingham United States
3. Department of Pediatrics, Division of Respiratory Medicine University of California, San Diego La Jolla United States
4. Section of Pulmonary, Critical Care and Sleep Medicine, School of Medicine Yale University New Haven United States
5. Department of Pediatrics, Division of Neonatology University of Alabama at Birmingham Birgmingham United States

† Corresponding author

## Abstract

Biological systems are increasingly being studied by high throughput profiling of molecular data over time. Determining the set of time points to sample in studies that profile several different types of molecular data is still challenging. Here we present the Time Point Selection ( TPS ) method that solves this combinatorial problem in a principled and practical way. TPS utilizes expression data from a small set of genes sampled at a high rate. As we show by applying TPS to study mouse lung development, the points selected by TPS can be used to reconstruct an accurate representation for the expression values of the non selected points. Further, even though the selection is only based on gene expression, these points are also appropriate for representing a much larger set of protein, miRNA and DNA methylation changes over time. TPS can thus serve as a key design strategy for high throughput time series experiments.
