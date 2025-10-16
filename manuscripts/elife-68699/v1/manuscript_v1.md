# Multi-syndrome, multi-gene risk modeling for individuals with a family history of cancer with the novel R package PanelPRO

## Authors

- Gavin Lee<sup>1</sup> ([ORCID: 0000-0003-2659-1163](https://orcid.org/0000-0003-2659-1163))
- Jane W Liang<sup>2</sup>
- Qing Zhang<sup>3</sup>
- Theodore Huang<sup>2</sup>
- Christine Choirat<sup>1</sup>
- Giovanni Parmigani<sup>2</sup>
- Danielle Braun<sup>2</sup> ([ORCID: 0000-0002-5177-8598](https://orcid.org/0000-0002-5177-8598)) †

### Affiliations

1. Swiss Data Science Center ETH Zürich and EPFL Lausanne Switzerland
2. Biostatistics Harvard T.H. Chan School of Public Health Boston United States
3. Getz Laboratory Broad Institute of MIT and Harvard Cambridge United States

† Corresponding author

## Abstract

Identifying individuals who are at high risk of cancer due to inherited germline mutations is critical for effective implementation of personalized prevention strategies. Most existing models focus on a few specific syndromes; however recent evidence from multi-gene panel testing shows that many syndromes are overlapping, motivating the development of models that incorporate family history on several cancers and predict mutations for a comprehensive panel of genes. We present PanelPRO, a new, open-source R package providing a fast, flexible back-end for multi-gene, multi-cancer risk modeling with pedigree data. It includes a customizable database with default parameter values estimated from published studies and allows users to select any combinations of genes and cancers for their models, including well-established single syndrome BayesMendel models (BRCAPRO and MMRPRO). This leads to more accurate risk predictions and ultimately has a high impact on prevention strategies for cancer and clinical decision making. The package is available for download for research purposes at https://projects.iq.harvard.edu/bayesmendel/panelpro.
