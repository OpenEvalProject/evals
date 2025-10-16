# Peer review - Round 1

Editors:
- Maarten van Lohuizen, The Netherlands Cancer Institute Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.40854.028](https://doi.org/10.7554/eLife.40854.028)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for sending your article entitled "Genome-wide Estrogen Receptor-α activation is sustained, not cyclical" for peer review at eLife. Your article is being evaluated by Jessica Tyler as the Senior Editor, a Reviewing Editor, and three reviewers.

The existence of oestrogen receptor cycling has become a debated matter in recent years. Previously it was shown that ERa and its cofactors bind to response elements in a co-ordinated cyclical fashion, but recent data has questioned these findings. In this study, Holding et al., have performed a high number of replicates and included a number of controls as well as a new normalization protocol to demonstrate that ERa binds to DNA rapidly and remains bound, rather than cycling on and off of DNA. If substantiated, this would be an important addition to the understanding of ER biology and regulation. However, substantial criticisms have been raised by several referees around whether cycling indeed does not occur that would need to be addressed in detail.

Essential revisions:

1) The authors normalised the ER ChIP-seq data over CTCF ChIP-seq data, aiming to minimise noise in the analyses. The authors claim that other papers that have described a cyclic behaviour of ER are describing an artefact due to low sample numbers and noisy data. However, the current dataset is quite heavily pre-processed, rendering it impossible to assess whether the hypothesis is correct (cyclic ER pattern, due to noise). The authors should visualise and use the individual datastreams (ER ChIP-seq, CTCF ChIP-seq) and determine whether the ER ChIP-seq data alone would have the cyclic behaviour, or that individual replicates may have that. I find this a key issue.

2) The paper is quite strongly TFF1-focussed, while full genome ER ChIP-seq data is available. With that, I believe the study should be re-positioned, making use of the actual genome-wide information instead.

3) Figure 1: The authors conclude that the data does "not demonstrate evidence of oscillatory binding…" while noting, "there is significantly more variance (F-test, time points >= 10 minutes, p-value < 1 × 10−10) in the ER binding data than in CTCF binding between replicates." However, even allowing for this, as seen in Figure 1, there does appear to be cyclical, dynamic changes in ER binding, particularly when compared to the profile seen for the CTCF control, which appears to be relatively constant. The pattern suggests low ER binding at 20,40 and 60 minutes, and higher binding at 30, 50 and 70 minutes. While not pronounced, this pattern appears to have been lost following analysis. Related to this, is CTCF a good control in this setup? ER and CTCF have been described to cooperate (Ross-Innes et al., 2011). With a biological and functional connection between both proteins, is it really justified to use CTCF to normalise ER data?

4) Over time, some replicates are substantially more variable at specific time points as compared to others, e.g. Figure 1—figure supplement 4 (20, 40, 70, 90 minutes highly variable, while 10, 30, 80 minutes have hardly any variation). Wouldn't this actually support a cyclic patterns in the data? Why would specific time points have a larger variation than others?

5) Figure 2: In addition to the general increase in binding across all sites in response to E2, Part A shows blocks of distinct high affinity ER binding sites that change during the time course. These blocks can still be seen when normalized for CTCF binding, as seen in Part B. The significance of these blocks, particularly in relation to their appearance during the time-course are not adequately discussed.

Figure 2: In addition to the general increase in binding across all sites in response to E2, Part A shows examples of binding sites which appear to exhibit cyclical binding ER in the time-course. These can still be seen when normalized for CTCF binding, as seen in Part B, although, these are difficult to see here, as the normalization appears to dampen the dynamic range for ER binding. The significance of these sites particularly as regards the overall conclusions of the paper are not adequately discussed.

6) I am concerned with the analyses carried in subsection "Quantitative re analysis of independent studies", some of which relies on image analysis of published figures. Unless these analyses were carried out on the primary image data, I would not expect this to be a reliable approach. Also, as the authors themselves point out, there are notable differences in the way the time-course experiments have been carried out in the current study, when compared to the older studies considered in this section. Related to this, In the work by Metivier et al., (2003), the group used α-amanitin to synchronise the cells and strip ERa from response elements. This harsher synchronisation of the cells may result in a clearer cycling of ERa. To be able to compare the data presented here to this previous work, I feel that it will be necessary to perform a ChIP time course for the TFF1 promoter +/- α-amanitin to see if this explains the difference in results.

Reviewer #1:

In the field of Estrogen Receptor genomics, an often-reported phenomenon is that ER is cycling on the genome upon E2 stimulation. The authors now claim this is not the case, and the original observations may be related to lower number of replicates and noise in the analyses. Even though this is a compelling concept, I am personally not convinced this is the case, based on the data that are being presented in this manuscript.

1) The authors normalised the ER ChIP-seq data over CTCF ChIP-seq data, aiming to minimise noise in the analyses. The authors claim that other papers that have described a cyclic behaviour of ER are describing an artefact due to low sample numbers and noisy data. However, the current dataset is quite heavily pre-processed, rendering it impossible to assess whether the hypothesis is correct (cyclic ER pattern, due to noise). The authors should visualise and use the individual datastreams (ER ChIP-seq, CTCF ChIP-seq) and determine whether the ER ChIP-seq data alone would have the cyclic behaviour, or that individual replicates may have that. I find this a key issue.

2) The paper is quite strongly TFF1-focussed, while full genome ER ChIP-seq data is available. With that, I believe the study should be re-positioned, making use of the actual genome-wide information instead.

3) Is CTCF a good control in this setup? ER and CTCF have been described to cooperate (Ross-Innes et al., 2011). With a biological and functional connection between both proteins, is it really justified to use CTCF to normalise ER data?

4) Over time, some replicates are substantially more variable at specific time points as compared to others, e.g. Figure 1—figure supplement 4 (20, 40, 70, 90 minutes highly variable, while 10, 30, 80 minutes have hardly any variation). Wouldn't this actually support a cyclic pattern in the data? Why would specific time points have a larger variation than others?

Reviewer #2:

The existence of oestrogen receptor cycling has become a debated matter in recent years. Previously it was shown that ERa and its cofactors bind to response elements in a co-ordinated cyclical fashion, but recent data has questioned these findings. In this study, Holding et al., have performed a high number of replicates and included a number of controls to demonstrate that ERa binds to DNA rapidly and remains bound, rather than cycling on and off of DNA. This is important because it furthers our understanding of how nuclear receptors, such as ERa, regulate target gene expression.

The paper is generally sound, but I have one main concern. In the work by Metivier et al., (2003), the group used α-amanitin to synchronise the cells and strip ERa from response elements. This harsher synchronisation of the cells may result in a clearer cycling of ERa. To be able to compare the data presented here to this previous work, I feel that it will be necessary to perform a ChIP time course for the TFF1 promoter +/- α-amanitin to see if this explains the difference in results.

Reviewer #3:

The interaction of transcripiton factors with DNA and chromatin are considered to be highly dynamic. This conclusion has been supported by numerous studies, including studies examining nuclear receptor dynamics, such as those previously carried out for Estrogen Receptor α (ER). Both direct evaluation of ER binding by Chromatin Immunopreciptation (ChIP) methods and imaging in live cells have supported a paradigm of rapid and continuous exchange events with the DNA. These highly dynamic interactions are a property of both DNA-protein and protein- protein interactions and are inherent to the transcriptional response.

The paper by Holden et al. seeks to use ChIPseq analysis for the estrogen receptor, in the MCF7 estrogen responsive breast cancer cell line, in order to further investigate ER transcriptional dynamics. Their analysis has used a parallel factor ChIP (pfChIP) normalization methodology, recently published by the lead author. Using this analysis, the authors observe that, rather than cycling at binding sites, a sustained increase in binding (affinity) is seen, together with a class of estrogen (E2) independent binding sites.

The study describes a set of ChIPseq time course data for estrogen receptor, which defines a potentially useful resource. The analysis using pfChIP normalization is interesting. Comments are as follows;

1) Figure 1: The authors conclude that the data does "not demonstrate evidence of oscillatory binding…" while noting, "there is significantly more variance (F-test, time points >= 10 minutes, p-value < 1 × 10−10) in the ER binding data than in CTCF binding between replicates." However, even allowing for this, as seen in Figure 1, there does appear to be cyclical, dynamic changes in ER binding, particularly when compared to the profile seen for the CTCF control, which appears to be relatively constant. The pattern suggests low ER binding at 20,40 and 60 minutes, and higher binding at 30, 50 and 70 minutes. While not pronounced, this pattern appears to have been lost following analysis.

2) Figure 2: In addition to the general increase in binding across all sites in response to E2, Part A shows blocks of distinct high affinity ER binding sites that change during the time course. These blocks can still be seen when normalized for CTCF binding, as seen in Part B. The significance of these blocks, particularly in relation to their appearance during the time-course are not adequately discussed.

3) Figure 2: In addition to the general increase in binding across all sites in response to E2, Part A shows examples of binding sites which appear to exhibit cyclical binding ER in the time-course. These can still be seen when normalized for CTCF binding, as seen in Part B, although, these are difficult to see here, as the normalization appears to dampen the dynamic range for ER binding. The significance of these sites particularly as regards the overall conclusions of the paper are not adequately discussed.

4) I am concerned with the analyses carried in subsection "Quantitative re analysis of independent studies", some of which relies on image analysis of published figures. Unless these analyses were carried out on the primary image data, I would not expect this to be a reliable approach. Also, as the authors themselves point out, there are notable differences in the way the time-course experiments have been carried out in the current study, when compared to the older studies considered in this section.
