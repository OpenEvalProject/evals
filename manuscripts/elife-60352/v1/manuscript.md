# A statistical framework for assessing pharmacological response and biomarkers using uncertainty estimates

## Authors

- Dennis Wang<sup>1</sup> ([ORCID: 0000-0003-0068-1005](https://orcid.org/0000-0003-0068-1005)) †
- James Hensman<sup>2</sup>
- Ginte Kutkaite<sup>3</sup>
- Tzen S Toh<sup>4</sup>
- Ana Claudia Paulo Galhoz<sup>3</sup>
- Jonathan R Dry<sup>5</sup>
- Julio Saez-Rodriguez<sup>6</sup>
- Mathew J Garnett<sup>7</sup>
- Michael P Menden<sup>8</sup> †
- Frank Dondelinger<sup>9</sup> ([ORCID: 0000-0003-1816-6300](https://orcid.org/0000-0003-1816-6300)) †

### Affiliations

1. Sheffield Institute for Translational Neuroscience University of Sheffield Sheffield United Kingdom
2. PROWLER.io Cambridge United Kingdom
3. Computational Biology Helmholtz Zentrum Muenchen Munich Germany
4. The Medical School University of Sheffield Sheffield United Kingdom
5. AstraZeneca Boston United States
6. Heidelberg University Heidelberg Germany
7. Translational Cancer Genomics Wellcome Sanger Institute Hinxton United Kingdom
8. Institute of Computational Biology Helmholtz Zentrum München Neuherberg Germany
9. Lancaster University Lancaster United Kingdom

† Corresponding author

## Abstract

High-throughput testing of drugs across molecular-characterised cell lines can identify candidate treatments and discover biomarkers. However, the cells' response to a drug is typically quantified by a summary statistic from a best-fit dose-response curve, whilst neglecting the uncertainty of the curve fit and the potential variability in the raw readouts. Here, we model the experimental variance using Gaussian Processes, and subsequently, leverage uncertainty estimates to identify associated biomarkers with a new Bayesian framework. Applied to in vitro screening data on 265 compounds across 1,074 cancer cell lines, our models identified 24 clinically established drug response biomarkers, and provided evidence for 6 novel biomarkers by accounting for association with low uncertainty. We validated our uncertainty estimates with an additional drug screen of 26 drugs, 10 cell lines with 8 to 9 replicates. Our method is applicable to any dose-response data without replicates, and improves biomarker discovery for precision medicine.
