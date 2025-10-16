# Peer review - Round 1

Editors:
- Sara Mitri, https://ror.org/019whta54 University of Lausanne Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78530.sa0](https://doi.org/10.7554/eLife.78530.sa0)

This paper analyses meta-genomic human gut microbiome data to understand how biodiversity arises and can be maintained. It makes an important contribution by strengthening the diversity-begets-diversity hypothesis and linking it to signatures of gene loss expected from the Black Queen hypothesis. While only correlative data is used to draw conclusions, the methods are solid and alternative hypotheses are clearly outlined.


---

# Peer review - Round 1

Editors:
- Sara Mitri, https://ror.org/019whta54 University of Lausanne Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78530.sa1](https://doi.org/10.7554/eLife.78530.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Community diversity is associated with intra-species genetic diversity and gene loss in the human gut microbiome" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Detlef Weigel as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Djordje Bajić (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Three main weaknesses of the work were pointed out that would require extensive work to address, which would be beyond the scope of the current paper. The reviewers are requesting instead that these weaknesses be made very clear in the manuscript. The first is that DBD is only one possible process that can explain the observed patterns, and alternative hypotheses are not sufficiently outlined. The second is that the sequencing depth of the analyzed samples is little for gut microbiomes and hence allows only to look at a fraction of the strain-level diversity present. Third, it is not clear what the mechanism would link the BQH and DBD. Based on these points, it would be important to

(i) tone down the conclusions,

(ii) elaborate on certain concepts,

(iii) discuss these limitations of your study, and

(iv) consider whether any further analyses of your data might address these points (more detail below).

Reviewer #2 (Recommendations for the authors):

The study is purely correlative, some of the correlations are weak or not significant, only a subset of the analysed species shows a significant positive correlation, and when changing the method to assess the diversity not the same species are being identified to have a positive correlation (diversity-SNV analysis) or opposite trends are being observed (diversity-strain number). This means that the detected patterns are not very robust. The authors refer to a recent pre-print (Estrela et al) that provides experimental support for DBD. However, the environmental conditions in that study were very different from the one found in the gut, in that only a single carbon source was provided. DBD is only one possible process that may explain the observed patterns (see above). Therefore, I recommend the authors tune down their conclusions, discuss their findings more critically, i.e. offer alternative explanations, or argue better why these alternative explanations are less likely than DBD to explain the observed patterns.

From the discussion, it is not clear what would explain the DBD at finer taxonomic scale. It would be great to have a bit more insights about how the authors believe that diversity at e.g. the species, genus, or even family level could influence strain-level diversity within an individual species. What type of niches can be created by the presence of additional families? And how can these niches be occupied by distinct strains of the same species? Although it is true that some strains may be ecologically distinct, I would still assume that most strains occupy similar niches and are competing for similar nutrients. Moreover, wouldn't we expect that there is so much functional redundancy in the gut microbiome already that a slight increase in taxonomic diversity would not necessarily create new metabolic niches from which closely related strains with similar metabolic capacities would profit? I think it would help to explain a bit more how the DBD should work out at the strain level and to what extent there is evidence that the increased strain-level diversity can really be adaptation to new niches created by other microbes in the system.

The HMP1-1 and Poyet samples were rarified to 20 and 5 mio reads. This seems very little sequencing depth considering the high amount of genus/species level diversity in the human gut microbiome and the fact that the authors want to look at strain-level diversity. I have my doubts that this amount of data will allow to quantitatively assess diversity at the strain level in these samples, which may in part explain the not very robust correlations observed. How much of the total diversity is assessed with this number of reads? Rarefaction curves of SNVs or genes per species discovered when sub-setting the datasets across samples would be helpful. In addition to the low overall sequencing depth, only polymorphisms with a frequency of 0.2-0.8 were considered, which further limits the number of strains that can be detected. What was the idea behind applying this cut-off?

Why was only one species analysed across the entire Poyet dataset? If this is a general pattern it should be observable for more species than just B. vulgatus. While I acknowledge that read coverage may not be high enough for all samples for other species, there should be enough consecutive timepoints with sufficient coverage for some species. Unless there is a good reason why such analysis can only be done for B. vulgatus, I strongly recommend to extend this analysis to other community members to find further support for DBD-like patterns.

Along the same lines, the Poyet dataset would offer an opportunity to follow how diversity of B. vulgatus changes over more timepoints than just two in response to the species/genus/family diversity (e.g. over the entire 18 months?). This could provide interesting new insights that may help to understand how diversity changes over time at different levels. Why not look at changes in diversity across all timepoints? Would we expect that DBD continues over a longer period of time or would we see some type of negative feedback, because of ecological control kicking in at one point leading to oscillations of diversity?

The figures with the correlations should be improved. Specifically, Figure 2, 3, and 5 include too many data points of different species on top of each other. It is impossible to look at the distribution of the data of individual species and appreciate the existence of correlations. In panel A of Figure 2, I see only one data point for Dialister invisus. Why? Is the color legend missing next to panel B in Figure 3?

For the StrainFinder analysis, it was assumed that species for which no site passed the 20x threshold are presented by a single strain. This seems wrong in my opinion. Such data should be excluded as the shallow sequencing simply does not allow assessing the number of strains of that species in these samples.

Out of 68 species only 15 or 18 show a significant slope. This means that there are more species that display either EC or no correlation (as EC may not always detectable). This takes away from the conclusion that just DBD explains the patterns of diversity found in the gut microbiome, and should be acknowledged.

Line 148: What is the overlap of the 15 and 18 detected positive correlations between Shannon and richness analysis? From comparing the legends of Figure 2A and B, it seems that the overlap is not great. It would be helpful if the authors could state the overlap in their paper and discuss it.

Line 147: Significance of the correlations should be corrected for multiple testing. Would the identified correlations still be significant?

How does the method to identify gene loss/gene gain differentiate between gene loss and strain-level dynamics? That is, we do not know whether a certain genome lost genes or a strain lacking those genes happened to dominate the community. If such strain happened to migrate into the community for example, this would not be evidence for the BQH.

Reviewer #3 (Recommendations for the authors):

The paper is very well written and generally well-integrated with previous work by the group and by others.

I found the main novelty of the present work to be the usage of time series data to enquire about how present microbiome community diversity may influence within species polymorphism at a future time point, motivated by the mechanism underlying the Black Queen Hypothesis (BQH) put forward ten years ago.

There are however several points that I think need to be revised:

1. It was not clear to me in the authors' introduction and discussion if and how the DBD hypothesis is integrated with the BQH.

Do the authors consider these two hypotheses to be independent? What sort of mechanisms do the authors envisage to drive a positive association between community diversity and polymorphism? And is the mechanism underlying the BQH assumed to result in the fixation of a gene loss within the focal species or may it also result in polymorphism as in Morris, Papoulis and Lenski 2014 Coexistence of evolving bacteria stabilized by a shared black queen function?

I think clarifying these points would strengthen the manuscript.

2. Another issue that was not clear to me was why the authors compute the polymorphism rates with only synonymous sites. If there is a reason to exclude non-synonymous sites it should be mentioned in the manuscript. In addition, the abstract and the conclusions should precisely state that the significant correlations are with polymorphism rates at synonymous sites.

3. The manuscript emphasizes the finding of a positive correlation in several species but does not emphasize that for the majority of species no correlation was found. Thus, the conclusion that DBD prevails (pg. 7 line 150 and abstract) looks a bit exaggerated.
