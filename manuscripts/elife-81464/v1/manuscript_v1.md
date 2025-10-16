# Applying causal discovery to single-cell analyses using CausalCell

## Authors

- Yujian Wen<sup>1</sup>
- Jielong Huang<sup>1</sup>
- Shuhui Guo<sup>1</sup>
- Yehezqel Elyahu<sup>2</sup>
- Alon Monsonego<sup>2</sup>
- Hai Zhang<sup>3</sup> †
- Yanqing Ding<sup>4</sup> †
- Hao Zhu<sup>1</sup> ([ORCID: 0000-0001-7384-3840](https://orcid.org/0000-0001-7384-3840)) †

### Affiliations

1. Bioinformatics Section Southern Medical University Guangzhou China
2. The Shraga Segal Department of Microbiology, Immunology and Genetics Ben-Gurion University of the Negev Beer-Sheva Israel
3. Network Center Southern Medical University Guangzhou China
4. Department of Pathology Southern Medical University Guangzhou China

† Corresponding author

## Abstract

Correlation between objects is prone to occur coincidentally, and exploring correlation or association in most situations does not answer scientific questions rich in causality. Causal discovery (also called causal inference) infers causal interactions between objects from observational data. Inferred causal interactions in single cells provide valuable clues for investigating molecular interaction and gene regulation, identifying critical diagnostic and therapeutic targets, and designing experimental and clinical interventions. The report of causal discovery methods and generation of single-cell data make applying causal discovery to single-cells a promising direction. However, how to evaluate and choose causal discovery methods and how to develop workflow and platform remain challenges. We report the workflow and platform CausalCell (http://www.gaemons.net/causalcell/causalDiscovery/) for performing single-cell causal discovery. The workflow/platform is developed upon benchmarking four kinds of causal discovery methods and is examined by analysing multiple scRNA-seq datasets. Our results suggest that different situations call for different methods and the constraint-based PC algorithm plus kernel-based conditional independence tests suit for most situations. Relevant issues are discussed and tips for best practices are recommended.
