# Author response - Round 1

Authors:
- Alfredo Llorca ([ORCID: 0000-0001-5555-2839](https://orcid.org/0000-0001-5555-2839))
- Gabriele Ciceri
- Robert Beattie
- Fong Kuan Wong
- Giovanni Diana ([ORCID: 0000-0001-7497-5271](https://orcid.org/0000-0001-7497-5271))
- Eleni Serafeimidou-Pouliou
- Marian Fernández-Otero
- Carmen Streicher
- Sebastian J Arnold
- Martin Meyer
- Simon Hippenmeyer ([ORCID: 0000-0003-2279-1061](https://orcid.org/0000-0003-2279-1061))
- Miguel Maravall ([ORCID: 0000-0002-8869-7206](https://orcid.org/0000-0002-8869-7206))
- Oscar Marin ([ORCID: 0000-0001-6264-7027](https://orcid.org/0000-0001-6264-7027))

## Response text

DOI: [10.7554/eLife.51381.sa2](https://doi.org/10.7554/eLife.51381.sa2)

Reviewer #2:

[…] 1) Both in the title ("cytoarchitectures"), the Abstract and the Introduction, the authors highlight that their findings explain how heterogeneous laminar organizations can be generated across cortical areas. While the second model they use indeed suggests that rules identified in S1 may apply in V1, the data provided are not sufficient to support the claims related to inter-areal diversity. Also, stochastic control over cell fate is not a "novel mechanism" and has been described in multiple settings. These elements of the text should be corrected to better reflect available data.

We agree that our data is insufficient to provide conclusive evidence regarding the generation of region-specific laminar ratios of PCs. Our mathematical model, however, is capable to explain the genesis of different regional cytoarchitectures using a stochastic program. This suggests that the origin of region-specific lamination may not require region specific molecular programs, but rather the precise tuning of a general stochastic mechanism. Nevertheless, following the suggestion of the reviewer we have edited the Title, Abstract and Introduction to avoid any confusion regarding this matter. Following the reviewer’s advice, we also avoided the use of the word “novel” when referring to the stochastic mechanisms described in the manuscript.

Actions taken:

- We have modified the text in the Title, Abstract and Introduction to address the reviewer’s concern.

- We have removed the word “novel” from the Abstract.

2) It would be very interesting to perform an analysis based on the radial position of cells in a clone rather than on their laminar position. Indeed the division of clones into "deep", "superficial" and "translaminar" is arbitrary and whether a cluster analysis of the clones would unbiasedly reveal such categories is unclear. This would allow for normalized inter-areal comparisons in clone behavior, and assess the extent to which laminar identity drives clonal distribution.

Although the proposed idea is certainly interesting, such analysis would require the re-annotation of all the clones based on the distance of the neurons from the pial or ventricular surfaces. This would need to be done manually and will likely take several months. Consequently, we believe this is out of the scope of our present study. In our study, laminar identity is a proxy (which we know it is imperfect) of neuronal identity. In addition, we use common molecular markers to identify type identity beyond laminar fates. Therefore, the specific radial position of the observed cells was not included in our original analysis since it does not provide additional information about cell fate.

3) The authors should provide an annotated Excel table containing the laminar position (and, ideally, the radial position, see point 2 above) for each of the neurons of every clone used for the study. This manuscript represents an impressive amount of work and providing this raw data would add a remarkable "database" component to the existing findings.

We thank the reviewer for his kind consideration of the amount of data reported in this manuscript. The revised version of this manuscript include annotated source files, as requested by the reviewer and consistent with eLife editorial recommendations.

Action taken:

- Raw data for which the analyses described in the manuscript are derived are now provided in Excel format as source files.

Reviewer #3:

[…] I have several comments for consideration.

1) The overall conclusion of the retrovirus lineage tracing is sound, but there are some limitations that could be mentioned. First, retroviruses are injected for lineage tracing at E12.5. It is conceivable that some lineage restriction of progenitors could occur shortly after E12.5. This would be missed in the current analysis. Second, the authors assume that none of the mapped lineages go back to self-renewing progenitor divisions. It is formally possible that some retroviruses infect a self-renewing progenitor that in the next division produced two progenitors, each of which is lineage restricted. One of these progenitors could generate (for example) layer 5-6 neurons, one layer 2-4 neurons, or other layer combinations. This pattern could still be compatible with a clone size of 6-8 offspring. Overall, these caveats indicate that the study provides a minimal estimate of the number of lineage restricted progenitors.

2) Similar limitations apply to the Cre lineage tracing studies.

We thank the reviewer for pointing this interesting possibility. It is true that fate restriction could happen shortly after E12.5, and this vision is compatible with bot retroviral and Cre fate-mapping results. However, the MADM dataset is not consistent with this view. If two complementary fate-restricted progenitors were to arise from E12.5 progenitor divisions, we should have recovered an important fraction of symmetric lineages containing two laminar-restricted sub-lineages larger than two cells. This configuration is virtually absent from the MADM dataset, so we think this possibility is unlikely. We have now addressed this point in the Discussion.

Action taken:

- We have now referred to this issue in the Discussion under the heading “Diversity of neocortical lineages”.

3) The data in the paper are not consistent with the conclusions reached in the paper by Gao et al., 2014, which proposed a deterministic model of progenitor behavior based on MADM studies. The current paper seems to avoid to clearly spell out that there is a serious discrepancy between the two papers. There are two major problems. First, the Gao paper and the current paper used the same MADM strategy for lineage studies, but they got different results. Second, the additional strategies used in the current paper are inconsistent with the conclusions reached by the previously reported MADM results. I will address this in more detail:

i) MADM strategy: in the previous paper, 2% of clones or less were restricted at E12-E13 to deep layers, and 10% were restricted to upper layers. In the current paper, 7% of the clones were restricted to deep layers and none to upper layers. While the numbers seem small, the fold difference is large. It might reflect the limitations of the MADM strategy. MADM experiments are complex and involve elaborate crossing schemes, data collection strategies and interpretation. Thus, small variations in experiments (for example a slight difference in the timing of Cre) significantly can affect the outcome of the experiments. MADM might capture major events but miss important pieces of the overall picture.

The Gao paper concluded that progenitors deterministically and sequentially generated neuronal subtypes (on average 8) for all neuronal layers. Data in Figure 5—figure supplement 1J directly contradict these data and demonstrate that MADM clones do not span all layers.

ii) Retroviruses and Cre strategies: the results obtained with retrovirus lineage tracing and Cre strategies are remarkably consistent, and they contradict the conclusions previously reached by Gao et al. The data show a wide variation in clonal size (Figure 5E, Figure 5—figure supplement 1I). Furthermore, like the MADM studies, they provide evidence that single progenitors generate neurons for different layers, but the clones do not cover all layers (Figure 5F). The data also show that a significant number of progenitors appear to produce a similar subtype of projection neurons (e.g. CCPNs) even if they are in different layers (Figure 5H), suggesting some kind of restriction in the fate potential of progenitors.

These are major discrepancies to the Gao study. I think it is important to discuss this clearly and to point out that the current data contradict the conclusions reached by Gao.

We agree with the reviewer that our study reports important discrepancies with Gao et al., 2014. In addition to the matters pointed by the reviewer, superficial restricted lineages are not reported by Gao and colleagues when labelling at E12.5. We believe that the reason for the observed discrepancies are mainly technical, as discussed in the text. Another major discrepancy with the cited paper is the interpretation of progenitor output as “deterministic” and “predictable” considering the huge heterogeneity described in our manuscript. We have now more clearly stated these discrepancies in the Discussion.

Action taken:

- A sentence has been added in the Discussion that highlights the main discrepancy of our study with Gao et al., 2014.
