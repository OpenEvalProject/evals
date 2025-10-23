# High resolution species assignment of Anopheles mosquitoes using k-mer distances on targeted sequences

## Authors

- Marilou Boddé<sup>1</sup> †
- Alex Makunin<sup>2</sup>
- Diego Ayala<sup>3</sup> ([ORCID: 0000-0003-4726-580X](https://orcid.org/0000-0003-4726-580X))
- Lemonde Bouafou<sup>3</sup>
- Abdoulaye Diabaté<sup>4</sup>
- Uwem Friday Ekpo<sup>5</sup> ([ORCID: 0000-0002-0543-5463](https://orcid.org/0000-0002-0543-5463))
- Mahamadi Kientega<sup>4</sup>
- Gilbert Le Goff<sup>3</sup>
- Boris Kevin Makanga<sup>6</sup>
- Marc F Ngangue<sup>7</sup>
- Olaitan Olamide Omitola<sup>5</sup> ([ORCID: 0000-0003-3827-6320](https://orcid.org/0000-0003-3827-6320))
- Nil Rahola<sup>3</sup> ([ORCID: 0000-0003-4067-6438](https://orcid.org/0000-0003-4067-6438))
- Frederic Tripet<sup>8</sup>
- Richard Durbin<sup>1</sup>
- Mara KN Lawniczak<sup>2</sup> ([ORCID: 0000-0002-3006-2080](https://orcid.org/0000-0002-3006-2080)) †

### Affiliations

1. Department of Genetics University of Cambridge Cambridge United Kingdom
2. Wellcome Sanger Institute Hinxton United Kingdom
3. MIVEGEC, IRD, CNRS Institut de Recherche pour le Développement Montpellier France
4. Institut de Recherche en Sciences de la Santé Bobo-Dioulasso Burkina Faso
5. Federal University of Agriculture Abeokuta Nigeria
6. Institut de Recherche en Ecologie Tropicale Libreville Gabon
7. Centre International de Recherches Medicales de Franceville Franceville Gabon
8. Centre for Applied Entomology and Parasitology Keele University Newcastle United Kingdom

† Corresponding author

## Abstract

The ANOSPP amplicon panel is a genus-wide targeted sequencing panel to facilitate large-scale monitoring of Anopheles species diversity. Combining information from the 62 nuclear amplicons present in the ANOSPP panel allows for a more nuanced species assignment than single gene (e.g. COI) barcoding, which is desirable in the light of permeable species boundaries. Here, we present NNoVAE, a method using Nearest Neighbours (NN) and Variational Autoencoders (VAE), which we apply to k- mers resulting from the ANOSPP amplicon sequences in order to hierarchically assign species identity. The NN step assigns a sample to a species-group by comparing the k -mers arising from each haplotype’s amplicon sequence to a reference database. The VAE step is required to distinguish between closely related species, and also has sufficient resolution to reveal population structure within species. In tests on independent samples with over 80% amplicon coverage, NNoVAE correctly classifies to species level 98% of samples within the An. gambiae complex and 89% of samples outside the complex. We apply NNoVAE to over two thousand new samples from Burkina Faso and Gabon, identifying unexpected species in Gabon. NNoVAE presents an approach that may be of value to other targeted sequencing panels, and is a method that will be used to survey Anopheles species diversity and Plasmodium transmission patterns through space and time on a large scale, with plans to analyse half a million mosquitoes in the next five years.
