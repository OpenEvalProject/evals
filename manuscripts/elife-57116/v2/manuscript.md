# shinyDepMap, a tool to identify targetable cancer genes and their functional connections from Cancer Dependency Map data

## Authors

- Kenichi Shimada<sup>1</sup> ([ORCID: 0000-0001-8540-9785](https://orcid.org/0000-0001-8540-9785)) †
- John A Bachman<sup>1</sup>
- Jeremy L Muhlich<sup>2</sup> ([ORCID: 0000-0002-0811-637X](https://orcid.org/0000-0002-0811-637X))
- Timothy J Mitchison<sup>3</sup> ([ORCID: 0000-0001-7781-1897](https://orcid.org/0000-0001-7781-1897))

### Affiliations

1. Department of Systems Biology and Laboratory of Systems Pharmacology Harvard Medical School Boston United States
2. Laboratory of Systems Pharmacology Harvard Medical School Boston United States
3. Department of Systems Biology Harvard Medical School Boston United States

† Corresponding author

## Abstract

Individual cancers rely on distinct essential genes for their survival. The Cancer Dependency Map (DepMap) is an ongoing project to uncover these gene dependencies in hundreds of cancer cell lines. To make this drug discovery resource more accessible to the scientific community we built an easy-to-use browser, shinyDepMap (https://labsyspharm.shinyapps.io/depmap). shinyDepMap combines CRISPR and shRNA data to determine, for each gene, the growth reduction caused by knockout/knockdown and the selectivity of this effect across cell lines. The tool also clusters genes with similar dependencies, revealing functional relationships. shinyDepMap can be used to 1) predict the efficacy and selectivity of drugs targeting particular genes; 2) identify maximally sensitive cell lines for testing a drug; 3) target hop, i.e., navigate from an undruggable protein with the desired selectivity profile, such as an activated oncogene, to more druggable targets with a similar profile; and 4) identify novel pathways driving cancer cell growth and survival.
