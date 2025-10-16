# Peer review - Round 1

Editors:
- Bruce Stillman, Cold Spring Harbor Laboratory United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62161.sa1](https://doi.org/10.7554/eLife.62161.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The manuscript characterizes the chromatin binding of two ORC subunits and two subunits of the MCM2-7 hexamer that are required for the initiation of DNA replication in different domains of the genome that are defined by the timing of DNA replication during S phase, early versus late. The binding of ORC and MCM subunits was compared with replication fork direction, transcription and replication timing profiles in human cells and subtle changes in the densities of these proteins in the different chromatin regions were observed. The distribution of these subunits, however, does not determine replication timing. The distribution in the genome of the histone H4K20me3 modification was also examined, indicating that it facilitates origin licensing in late-replicating regions. The authors suggest that factors other than the density and distribution of pre-Replicative Complexes determine the timing of the initiation of DNA replication during S phase.

Decision letter after peer review:

Thank you for submitting your article "Human ORC/MCM density is low in active genes and correlates with replication time but does not delimit initiation zones" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Bruce Stillman as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Kevin Struhl as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments and analysis are required before it will be re-considered for publication.

Summary:

The authors have performed an extensive analysis of the binding or ORC2 and ORC3 subunits of the Origin Recognition Complex (ORC) and the MCM3 and MCM7 subunits of the MCM2-7 helicase subunits by chromatin immunoprecipitation and then compared the data to replicating timing patterns throughout the genome of human Raji cells. Based on previous studies, some of which derive from the authors' labs, they have identified different regions of the genome that replicate at different times and these are associated or not with transcription start sites (TSS; early replicating), with non-transcribed DNA and regions that replicate unidirectionally or have no preference in a population of cells. Now the authors correlate the MCM2-7 and ORC binding with the replication timing and the various categories of chromatin.

They conclude that ORC and MCM binding correlates with each other in G1 phase, which is not surprising, and then that early replicating regions are more associated with domains enriched in ORC/MCM binding, and uniquely, that there are large regions of homogeneous distributions of ORC/MCM. They conclude that ORC/MCM correlates with replication timing but not the probability of replication initiation. They also demonstrate that histone H4K20me3 location is localized with ORC/MCM and that a certain late replicating DNA has higher H4K20me3 binding.

The paper contains a great deal of work and is of interest to those in the DNA replication field, adding to what is already known. There are some papers that are either not discussed well or not even mentioned and this should be corrected. However, before the paper can be re-considered for publication, the authors need to address some major concerns:

Essential revisions

1) One major issue relates to the small enrichments of ORC/MCM they observe in early versus late replicating DNA and the possibility that this represents a DNA isolation bias rather than a real correlation or cause (see specific points 4, 5 and 6 below). The paper does not address this issue which, given the small differences in ORC/MCM between early and late replicating regions (1.4 fold), this needs to be addressed. It is understood that genome-wide mapping of pre-RC components in mammalian cells is challenging. In all of the studies to date, the ChIP enrichment is very modest and not confined to tight peaks that are typical of transcription factor binding. The weak and broad patterns of localization and their enrichment at hypersensitive and transcription start sites may be a technical artifact or is reflective of the underlying biology. While the signals they are observing are likely biological, it is still very difficult (as the authors allude to in the Discussion) to disentangle causation and correlation with the observed patterns and enrichment at transcription start sites and DNase HS sites. What would make this story much stronger is to demonstrate that the MCM2-7 signal is dynamic – that is that the enrichment patterns they observe in G1 should be very different from the patterns in late S-phase or G2 when replication forks have displaced most of the MCMs. The authors need to perform ChIP-seq on the cells elutriated at 80 ml/min. The ORC profile may also change due to the dynamic nature of ORC in human cells, but the MCM definitely should only be enriched in late replicating regions of the genome in late S phase and this comparison is needed.

2) As shown in Figure 1A, stochastic variation can be observed for MCM3/7 and ORC2/3 ChIP-seq replicates, it's reasonable to speculate that the input signal can also fluctuate randomly among replicates. Moreover, most of the conclusions in this manuscript are based on the input normalized signals. However, as shown by Figure 1A and the record for ENA PRJEB32855, no replication is performed for the input. Thus, we suggest that the authors provide replicates for the input, and normalize the ChIP signal to pooled input signals.

3) As shown in Figure 1—figure supplement 2A, the input signals at "DNase hypersensitive (HS)" is lower than those at "no HS"; and in Figure 1—figure supplement 3E, the ChIP signals of MCM3/7 and ORC2/3 at "HS" are higher than those in "no HS". Thus, when the ChIP signals of MCM3/7 and ORC2/3 are normalized to the input, will the difference of ChIP signals of McCM3/7 or ORC2/3 at "HS" and "no HS" be amplified artificially?

Additional comments related to the above major comments described above:

1) In Figure 1, the authors show a convincing correlation between the ChIP-seq profiles of ORC2 and ORC3, as well as between MCM3 and MCM7. Miotto et al. had published ORC2 ChIP-seq data using asynchronous K562 human erythroid cells. The data in the Kirstein et al. paper reports ChIP data of ORC2 form Raji lymphoblastoid cells. Although the cell types and cell cycle stage are different, it would be valuable to show a Pearson correlation between the two different ORC2 sets. This should be shown as a Supplement to Figure 1. The authors could also comment on the data of ORC1 ChIP from Dellino et al., 2013 and Long et al., 2019 (see point 8 below) whether these ORC patterns correlate with the other ORC ChIP data.

2) Figure 5A and Figure 4—figure supplement 2B. The results show that ORC is 1.4 times more frequently found in early versus late replicating regions. It is possible that the chromatin in early replicating regions is more accessible to the ChIP procedure than late replicating regions, which are likely more compact and hence difficult to access using antibodies. How have the authors excluded the possibility that extraction of DNA fragments in early versus late replicating regions could explain the difference in ORC binding? It should be noted that the authors previous papers and the Discussion in this paper claims accessibility to chromatin by replication factors may explain replication timing, yet they have assumed that the sonication and antibodies used for ChIP analysis are equally accessible. It is known that heterochromatic regions of the genome form phase transitions that may behave completely differently than actively transcribed and "accessible" regions of the genome.

3) Figure 5E. The same concern outlined in comment 2 above could explain the small, albeit statistically significant difference between H4K20me3 high and low regions of the genome.

4) Figure 6A and related text. The very slight differences in H4K20me3 levels could also be explained by extraction artIfact.

5) “However, potential origins are defined by assembled MCM-DHs, not by ORC”. This statement that potential origins are determined by the MCM2-7 DH and not by ORC is not logical because MCM2-7 DH is loaded by ORC and other factors. The idea that it correlates with ORC is dismissed a few lines later, but none of these statements are justified. What is the evidence that access of firing factors to MCM2-7 DH are regulated by chromatin access?

6) In a significant paper describing ORC ChIP and replication initiation, it was shown that ORC binding correlates with histone H2AZ and this could explain early replication origin activity. This paper is not even cited, much less discussed, and it should be (see Long et al., 2019.

7) The authors have dismissed the replication timing model proposed by Miottto et al., 2016, but it is not clear why. This model should be discussed in relationship to the model in Figure 7.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Human ORC/MCM density is low in active genes and correlates with replication time but does not delimit initiation zones" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Bruce Stillman as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Kevin Struhl as the Senior Editor.

The reviewers have discussed your response to the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission that addresses one issue.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

The revised paper has incorporated new data that compares the abundance of ORC2, ORC3, MCM3 and MCM7 protein at two difference stages of the cell division cycle and raises some interesting observations. The authors have extensively addressed all of the original reviewer comments and provide new analysis. The differences in MCM and ORC levels at the different classes of gene expression, except for the gene bodies, are very modest but nonetheless statistically significant.

The general conclusion is that ORC is wide spread on the genome in G1 phase and MCM localizes with sites of initiation of DNA replication, and that histone H3K4me3 is correlated with late origin firing. At all locations, the exact site of initiation of DNA replication is stochastic.

One paradox needs explaining that arises from the new data presented in the revised paper compared to data in the literature.

1) The data in Figure 4—figure supplement 2C show that MCM3 and MCM7 levels are reduced in S-G2-M cells compared to G1 cells, but there remains a difference between early versus late replication timing domains in both cell cycle stages. In contrast, ORC is high in early RFDs and low in late RFDs at both stages. Perhaps the authors should discuss the significance of this result, in light of the fact that ORC1 is degraded in human cells at the G1-S transition and should not be present later in the cell cycle util it is re-synthesized. Does this mean ORC2 and ORC3 remain chromatin bound during the cell cycle and what does this mean.

We suggest that the authors address this issue in the Discussion of a revised manuscript which can then proceed.
