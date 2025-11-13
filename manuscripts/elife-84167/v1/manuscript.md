# Rapid geographical source attribution of Salmonella enterica serovar Enteritidis genomes using hierarchical machine learning

## Authors

- Sion C Bayliss<sup>1</sup> ([ORCID: 0000-0002-5997-2002](https://orcid.org/0000-0002-5997-2002)) †
- Rebecca K Locke<sup>2</sup>
- Claire Jenkins<sup>3</sup>
- Marie Anne Chattaway<sup>3</sup>
- Timothy J Dallman<sup>4</sup>
- Lauren A Cowley<sup>2</sup>

### Affiliations

1. Bristol Veterinary School University of Bristol Bristol United Kingdom
2. Life Sciences Department University of Bath Bath United Kingdom
3. Gastrointestinal Reference Services UK Health Security Agency London United Kingdom
4. Institute for Risk Assessment Sciences Utrecht University Utrecht Netherlands

† Corresponding author

## Abstract

Salmonella enterica serovar Enteritidis is one of the most frequent causes of Salmonellosis globally and is commonly transmitted from animals to humans by the consumption of contaminated foodstuffs. In the UK and many other countries in the Global North, a significant proportion of cases are caused by consumption of imported food products or contracted during foreign travel, therefore making the rapid identification of the geographical source of new infections a requirement for robust public health outbreak investigations. Herein, we detail the development and application of a hierarchical machine learning model to rapidly identify and trace the geographical source of S. Enteritidis infections from whole genome sequencing data. 2,313 S. Enteritidis genomes, collected by the UKHSA between 2014-2019, were used to train a 'local classifier per node' hierarchical classifier to attribute isolates to 4 continents, 11 sub-regions and 38 countries (53 classes). The highest classification accuracy was achieved at the continental level followed by the sub-regional and country levels (macro F1: 0.954, 0.718, 0.661 respectively). A number of countries commonly visited by UK travellers were predicted with high accuracy (hF1: >0.9). Longitudinal analysis and validation with publicly accessible international samples indicated that predictions were robust to prospective external datasets. The hierarchical machine learning framework provided granular geographical source prediction directly from sequencing reads in <4 minutes per sample, facilitating rapid outbreak resolution and real-time genomic epidemiology. The results suggest additional application to a broader range of pathogens and other geographically structured problems, such as antimicrobial resistance prediction, is warranted.
