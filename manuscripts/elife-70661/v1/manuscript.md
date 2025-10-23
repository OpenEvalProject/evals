# Minian an open-source miniscope analysis pipeline

## Authors

- Zhe Dong<sup>1</sup>
- William Mau<sup>1</sup> ([ORCID: 0000-0002-3233-3243](https://orcid.org/0000-0002-3233-3243))
- Yu Feng<sup>1</sup>
- Zachary T Pennington<sup>1</sup>
- Lingxuan Chen<sup>1</sup>
- Yosif Zaki<sup>1</sup>
- Kanaka Rajan<sup>1</sup>
- Tristan Shuman<sup>1</sup> ([ORCID: 0000-0003-2310-6142](https://orcid.org/0000-0003-2310-6142))
- Daniel Aharoni<sup>2</sup> ([ORCID: 0000-0003-4931-8514](https://orcid.org/0000-0003-4931-8514)) †
- Denise J Cai<sup>1</sup> ([ORCID: 0000-0002-7729-0523](https://orcid.org/0000-0002-7729-0523)) †

### Affiliations

1. Nash Family Department of Neuroscience Icahn School of Medicine at Mount Sinai New York United States
2. Department of Neurology University of California, Los Angeles Los Angeles United States

† Corresponding author

## Abstract

Miniature microscopes have gained considerable traction for in vivo calcium imaging in freely behaving animals. However, extracting calcium signals from raw videos is a computationally complex problem and remains a bottleneck for many researchers utilizing single-photon in vivo calcium imaging. Despite the existence of many powerful analysis packages designed to detect and extract calcium dynamics, most have either key parameters that are hard-coded or insufficient step-by-step guidance and validations to help the users choose the best parameters. This makes it difficult to know whether the output is reliable and meets the assumptions necessary for proper analysis. Moreover, large memory demand is often a constraint for setting up these pipelines since it limits the choice of hardware to specialized computers. Given these difficulties, there is a need for a low memory demand, user-friendly tool offering interactive visualizations of how altering parameters at each step of the analysis affects data output. Our open-source analysis pipeline, Minian (Miniscope Analysis), facilitates the transparency and accessibility of single-photon calcium imaging analysis, permitting users with little computational experience to extract the location of cells and their corresponding calcium traces and deconvolved neural activities. Minian contains interactive visualization tools for every step of the analysis, as well as detailed documentation and tips on parameter exploration. Furthermore, Minian has relatively small memory demands and can be run on a laptop, making it available to labs that do not have access to specialized computational hardware. Minian has been validated to reliably and robustly extract calcium events across different brain regions and from different cell types. In practice, Minian provides an open-source calcium imaging analysis pipeline with user-friendly interactive visualizations to explore parameters and validate results.
