# Unsupervised detection of fragment length signatures of circulating tumor DNA using non-negative matrix factorization

## Authors

- Gabriel Renaud<sup>1</sup>
- Maibritt Nørgaard<sup>2</sup>
- Johan Lindberg<sup>3</sup>
- Henrik Grönberg<sup>3</sup>
- Bram De Laere<sup>3</sup>
- Jørgen Bjerggaard Jensen<sup>4</sup>
- Michael Borre<sup>5</sup>
- Claus Lindbjerg Andersen<sup>2</sup>
- Karina Dalsgaard Sørensen<sup>2</sup>
- Lasse Maretty<sup>2</sup> †
- Søren Besenbacher<sup>2</sup> ([ORCID: 0000-0003-1455-1738](https://orcid.org/0000-0003-1455-1738)) †

### Affiliations

1. Department of Health Technology Technical University of Denmark Kongens Lyngby Denmark
2. Department of Molecular Medicine Aarhus University Aarhus N Denmark
3. Department of Medical Epidemiology and Biostatistics Karolinska Institute Stockholm Sweden
4. Department of Urology Regional Hospital of West Jutland Holstebro Denmark
5. Department of Urology Aarhus University Hospital Aarhus Denmark

† Corresponding author

## Abstract

Sequencing of cell-free DNA (cfDNA) is currently being used to detect cancer by searching both for mutational and non-mutational alterations. Recent work has shown that the length distribution of cfDNA fragments from a cancer patient can inform tumor load and type. Here, we propose non-negative matrix factorization (NMF) of fragment length distributions as a novel and completely unsupervised method for studying fragment length patterns in cfDNA. Using shallow whole-genome sequencing (sWGS) of cfDNA from a cohort of patients with metastatic castration-resistant prostate cancer (mCRPC), we demonstrate how NMF accurately infers the true tumor fragment length distribution as an NMF component - and that the sample weights of this component correlate with ctDNA levels (r=0.75). We further demonstrate how using several NMF components enables accurate cancer detection on data from various early stage cancers (AUC=0.96). Finally, we show that NMF, when applied across genomic regions, can be used to discover fragment length signatures associated with open chromatin.
