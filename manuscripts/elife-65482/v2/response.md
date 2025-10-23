# Author response - Round 1

Authors:
- Brian R Lee ([ORCID: 0000-0002-3210-5638](https://orcid.org/0000-0002-3210-5638))
- Agata Budzillo ([ORCID: 0000-0002-2723-3272](https://orcid.org/0000-0002-2723-3272))
- Kristen Hadley
- Jeremy A Miller ([ORCID: 0000-0003-4549-588X](https://orcid.org/0000-0003-4549-588X))
- Tim Jarsky ([ORCID: 0000-0002-4399-539X](https://orcid.org/0000-0002-4399-539X))
- Katherine Baker
- DiJon Hill
- Lisa Kim
- Rusty Mann ([ORCID: 0000-0002-0226-2069](https://orcid.org/0000-0002-0226-2069))
- Lindsay Ng
- Aaron Oldre
- Ram Rajanbabu
- Jessica Trinh
- Sara Vargas
- Thomas Braun ([ORCID: 0000-0002-1416-2065](https://orcid.org/0000-0002-1416-2065))
- Rachel A Dalley
- Nathan W Gouwens ([ORCID: 0000-0001-8429-4090](https://orcid.org/0000-0001-8429-4090))
- Brian E Kalmbach
- Tae Kyung Kim
- Kimberly A Smith
- Gilberto Soler-Llavina
- Staci Sorensen
- Bosiljka Tasic ([ORCID: 0000-0002-6861-4506](https://orcid.org/0000-0002-6861-4506))
- Jonathan T Ting
- Ed Lein
- Hongkui Zeng ([ORCID: 0000-0002-0326-5878](https://orcid.org/0000-0002-0326-5878))
- Gabe J Murphy
- Jim Berg ([ORCID: 0000-0002-3300-5399](https://orcid.org/0000-0002-3300-5399))

## Response text

DOI: [10.7554/eLife.65482.sa2](https://doi.org/10.7554/eLife.65482.sa2)

Essential revisions:

1) The authors should be entirely transparent within the paper about which (if any) data are being reported for the first time and which have been previously described. The same is true for the resources provided (e.g. the software) and for the methodological conclusions. It is fine to include material/ideas etc that were previously reported but these must be clearly indicated with phrases like "as previously reported." In general it is important to make the case that new details are provided which significantly improve the ability of others to carry out the technique, over and above the material already provided as part of publication of the other papers in this series.

Throughout the manuscript we have clarified where data have been previously described. We have added a column to the cell database to indicate if that cell has been included in a previous study focused on morpho-electric-transcriptomic cell types in the mouse visual cortex or human temporal cortex. We added a first paragraph to the Results section that clarifies the overlap in cells that are included in this manuscript versus the previous studies, including a Venn diagram as a supplement to figure 1.

We have also more clearly clarified how the techniques presented here differ from those mentioned in the methods portion of previous manuscripts. Specifically, we highlighted the data that drove the decision to pursue nucleated patches as well as the analysis functions built on top of the MIES electrophysiology system that allows for fast, high quality data acquisition.

2) The authors should comment on the similarities and differences between the current protocol and others recently published.

We have added commentary on recently published Patch-seq protocols and how the approach we present is similar and different.

3) The issue of the granularity of cell type identification should be quantitatively addressed. Was it possible to identify all cells included in terms of the finest divisions identified in prior RNAseq studies including those in this current series? To the extent that this was not possible the reasons should be addressed. There are valid reasons to expect that the reduced sampling provided by patch seq may not be able to match the granularity of whole cell studies, but this is an important issue to address in detail, given the more complete scope of the data provided.

We have added a new figure that addresses the mapping success of Patch-seq cells, and how that mapping success relates to objective measures of transcriptomic quality.

Originally, we avoided including mapping as a metric in this study in the interest of presenting a protocol that is independent of the transcriptomic landscape of the target region. However, the point that we can use the mapping quality as a measure of the objective transcriptomic quality metrics is valid, and the manuscript is much improved with this addition.

The new panels in figure 4 show the relationship between an objective measure of transcriptomic data quality, the normalized marker sum (NMS) and a measure of mapping quality used in Gouwens et al., 2020 A new supplement to figure 4 shows a side-by-side comparison of the mapping of Patch-seq (Gouwens et al., 2020) vs FACS data (Tasic et al., 2019).

4) Criteria used to make classifications (e.g. such as cell health) should be specified.

We have added to the methods section to describe the subjective criteria used to classify the health of cells. Additionally, we have included representative images of the different cell health scores in Figure 6—figure supplement 2.
