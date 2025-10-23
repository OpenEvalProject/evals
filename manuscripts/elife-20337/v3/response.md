# Author response - Round 1

Authors:
- Jing Qiu
- Jamie McQueen
- Bilada Bilican
- Owen Dando
- Dario Magnani
- Karolina Punovuori ([ORCID: 0000-0003-0297-1225](https://orcid.org/0000-0003-0297-1225))
- Bhuvaneish T Selvaraj
- Matthew Livesey
- Ghazal Haghi
- Samuel Heron
- Karen Burr
- Rickie Patani
- Rinku Rajan
- Olivia Sheppard
- Peter C Kind
- T Ian Simpson ([ORCID: 0000-0003-0495-7187](https://orcid.org/0000-0003-0495-7187))
- Victor LJ Tybulewicz ([ORCID: 0000-0003-2439-0798](https://orcid.org/0000-0003-2439-0798))
- David JA Wyllie ([ORCID: 0000-0002-4957-6049](https://orcid.org/0000-0002-4957-6049))
- Elizabeth MC Fisher
- Sally Lowell ([ORCID: 0000-0002-4018-9480](https://orcid.org/0000-0002-4018-9480))
- Siddharthan Chandran
- Giles E Hardingham ([ORCID: 0000-0002-7629-5314](https://orcid.org/0000-0002-7629-5314))

## Response text

DOI: [10.7554/eLife.20337.021](https://doi.org/10.7554/eLife.20337.021)

[…] Essential revisions:

1) From the data shown it remains unclear how gene expression from human and mouse compare with each other under basal conditions, without KCl treatment. This information is important for understanding whether the conservation and divergence between species is observed only after KCl treatment or in both treated and untreated conditions. One way the authors could answer this question is to perform cluster analyses and PCA or similar analyses as in Figure 2H on untreated samples; they could also focus on the genes that show divergence (DRI different from 1 cf Figure 1—figure supplement 1E) and show whether their baseline levels are also divergent or conserved.

We have performed several analyses to address the extent of divergence in basal gene expression across different neuronal preparations and species, as well as whether there is any relationship between differential responsiveness to KCl stimulation, and differential basal gene expression.

Comparison of basal expression levels between Hum-ESCCORT-neurons and mouse neurons (DIV10 Mus-PRIMCORT-neurons, DIV4 Mus-PRIMCORT-neurons, and Mus-ESCCORT-neurons) revealed correlation coefficients of 0.714, 0.711, and 0.710 (Figure 2—figure supplement 1B-D). This correlation is substantially stronger than the that observed when comparing gene fold-change after KCl stimulation (0.480, 0.526,.595, Figure 1D, 2G, Figure 1—figure supplement 1G). Moreover, we performed a similar clustering analysis as in Figure 2H which illustrates this graphically: i.e. the basal expression profile of Hum-ESCCORT-neurons clusters far more closely to the three mouse neuronal populations (new Figure 2I) compared to the activity-dependent gene responsiveness (Figure 2H). Therefore, basal neuronal gene expression shows less divergence than the responsiveness of genes to depolarisation.

We also investigated whether gene differential responsiveness to KCl (DRI) in human vs. mouse neurons has any relationship with the relative basal expression of that gene in human vs. mouse neurons. For each of the 11,302 orthologous pairs, we plotted the Log2(DRI) Hum-ESCCORT-vs. DIV10 Mus-PRIMCORT-neurons (i.e. DRIs from Figure 1—figure supplement 1E) against the Log2(DBEI), where DBEI (differential basal expression index) is defined as the ratio of basal expression in Hum-ESCCORT-vs. DIV10 Mus-PRIMCORT-neurons (Figure 2—figure supplement 1E). As can be seen, there is no link between a gene's relative responsiveness to depolarisation in human vs. mouse neurons, and its relative basal expression levels in human vs. mouse neurons. Moreover, if we consider the 657 genes where Log2(DRI)>1, the standard deviation of their respective Log2(DBEI), 1.45, is similar to the standard deviation of Log2(DBEI) across all 11,302 genes (1.39), suggesting that there is no dramatic change in divergence of basal gene expression regardless of direction, in genes where DRI>1. Thus, evolutionary differences in activity-dependent gene responsiveness are not substantially attributable to differences in basal expression.

All source data for these calculations is included in the revised source data files.

2) A great potential value of this manuscript is that it could serve as a database for future studies. To facilitate this, the authors should display in each data table the identity of the genes that show divergence between conditions (those that have DRI different from 1). For instance, there should be more explicit naming of the genes in the data set excel file linked to Figure 1—figure supplement 1E, which is arguably constitute one of the most interesting lists. In addition, the columns could be more clearly labeled (for instance what is LN2 vs. DRI?).

We have ensured that the identity of the gene is included in all the source data tables. We have also reviewed the column labels and edited them to make their meaning is clearer to the reader.
