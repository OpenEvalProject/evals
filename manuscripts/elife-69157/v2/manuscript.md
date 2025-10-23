# The use of non-functional clonotypes as a natural calibrator for quantitative bias correction in adaptive immune receptor repertoire profiling

## Authors

- Anastasia O Smirnova<sup>1</sup>
- Anna M Miroshnichenkova<sup>2</sup>
- Yulia V Olshanskaya<sup>2</sup>
- Michael A Maschan<sup>2</sup>
- Yuri B Lebedev<sup>1</sup> ([ORCID: 0000-0003-4554-4733](https://orcid.org/0000-0003-4554-4733))
- Dmitriy M Chudakov<sup>1</sup> ([ORCID: 0000-0003-0430-790X](https://orcid.org/0000-0003-0430-790X))
- Ilgar Z Mamedov<sup>1</sup>
- Alexander Komkov<sup>1</sup> ([ORCID: 0000-0001-9113-698X](https://orcid.org/0000-0001-9113-698X)) †

### Affiliations

1. Department of Genomics of Adaptive Immunity Shemyakin-Ovchinnikov Institute of Bioorganic Chemistry Moscow Russian Federation
2. Laboratory of Cytogenetics and Molecular Genetics Dmitry Rogachev National Medical and Research Center of Pediatric Hematology, Oncology and Immunology Moscow Russian Federation

† Corresponding author

## Abstract

High-throughput sequencing of adaptive immune receptor repertoires is a valuable tool for receiving insights in adaptive immunity studies. Several powerful TCR/BCR repertoire reconstruction and analysis methods have been developed in the past decade. However, detecting and correcting the discrepancy between real and experimentally observed lymphocyte clone frequencies is still challenging. Here we discovered a hallmark anomaly in the ratio between read count and clone count-based frequencies of non-functional clonotypes in multiplex PCR-based immune repertoires. Calculating this anomaly, we formulated a quantitative measure of V- and J-genes frequency bias driven by multiplex PCR during library preparation called Over Amplification Rate (OAR). Based on the OAR concept, we developed an original software for multiplex PCR-specific bias evaluation and correction named iROAR: Immune Repertoire Over Amplification Removal (https://github.com/smiranast/iROAR). The iROAR algorithm was successfully tested on previously published TCR repertoires obtained using both 5' RACE (Rapid Amplification of cDNA Ends)-based and multiplex PCR-based approaches and compared with a biological spike-in-based method for PCR bias evaluation. The developed approach can increase the accuracy and consistency of repertoires reconstructed by different methods making them more applicable for comparative analysis.
