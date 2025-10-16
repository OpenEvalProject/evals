# Peer review - Round 1

Editors:
- Bernhard Schmid, University of Zurich Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.52787.sa1](https://doi.org/10.7554/eLife.52787.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Five categories of land-use that could be ranked according to increasing human impact showed strong linear declines in the majority of 17 invertebrate soil animal groups. These negative impacts were best detected when phylogenetic rarity was used as a measure whereas other diversity measures were less responsive and may therefore be less useful indicators. The comprehensive assessment of the soil invertebrate communities was made possible by the use of DNA metabarcoding.

Decision letter after peer review:

Thank you for submitting your article "Endemism is a better indicator of soil invertebrate biodiversity loss with land use change than richness or diversity" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Bernhard Schmid as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Ian Baldwin as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Marc Cadotte (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript represents a major effort to use DNA barcoding in analyzing soil communities at 75 sites across New Zealand. More than 11'000 taxa could be identified and assigned to different groups of invertebrates and microbes. The hypothesis is that diversity decreases along a gradient of land-use intensity represented by five land-use categories natural forest -> planted forest -> low-producing grassland -> high-producing grassland -> perennial cropland. This hypothesis is confirmed, especially if species are weighted by the reciprocal of the number of sites at which they occur, suggesting that they are habitat specialists and therefore respond most strongly to land use.

Essential revisions:

The manuscript should be improved in three respects:

First, there are several terms that are not well defined in the manuscript. "Land use" is sometimes considered as a state of an ecosystem and then called land-use category (please always use the hyphen when "land-use" is an adjectival noun) but sometimes considered as land-use change or intensification etc. Please use consistent terms throughout and make sure you define them well. In this context and related to the second main point I suggest that you put the five land-use categories explicitly into a linear sequence from one to five and call it land-use intensity.

Endemism is defined in the Materials and methods, but all reviewers would prefer a more generic term such as rare species because you cannot extrapolate from 75 sites to the entire area of your country, which would be necessary to know if a species that only occurred at 1 or 2 sites was geographically restricted. You should also mention the caveat that some of your rare species could just be "sink" or "passenger" species not adapted to the site conditions, while your hypothesis assumes that they are habitat specialists. One reviewer suggests in this context that you could actually do a sensitivity analysis without the rarest species that only occur at one site.

Second, you should get much more from your data if you expand your analyses. In principle, you selected your five categories such that they can be ordered along a gradient. Best would be if you could calculate some value for land-use intensity for each category or even each site, but even in the absence of this you are allowed to simply assign land-use intensity values from 1-5 and use this linear contrast in all ANOVA (the easiest way is to code land-use categories from 1-5 and use it as continuous variable LUI and factor LUC: then fit LUI+LUC in this order and you get a stronger test of your main hypothesis, namely the linear contrast LUI, and a test for deviations from the linear contrast, which is measured by LUC when fitted after LUI). Please replace all box-plots with means +/- standard errors. In addition, you could show regression lines for the LUI-gradient wherever it is significant. There would be the more sophisticated method of isotonic regression (Gaines, Steven D., and William R. Rice. 1990. Analysis of Biological Data When there are Ordered Expectations. The American Naturalist 135: 310-317.), but clearly the simpler method indicated above is also valid.

The above will remove the need for the excessive use of pairwise comparisons which are statistically not independent and ill-suited to test ordered hypotheses. A further reduction of unnecessary repeats and more comprehensive analysis is to compare the responses of the different taxa to LUI(+LUC) in a single ANOVA by putting the metrics for the different taxa into a single column and add a column with the taxa identities (or even two, one for phyla and one for classes/orders). You can then fit the following ANOVA-model:

Metric ~ LUI+LUC+phylum+order+LUI:phylum+LUC:phylum+LUI:order+LUC:order, or more simply without LUC terms and only using phylum or order. The interactions indicated by ":" test if the different taxonomic groups respond differently. Using the above you can exchange Figure 3—source data 1B and omit Supplementary Table 4. There is still the problem of comparing the R2 values (or better just use %SS, which are increments in multiple R2) mentioned by one reviewer and we ask you to consider their suggestions. It also seems you analyzed R2 values as (meta-)data; this requires explanation and justification in the Materials and methods, because R2 values will have a special distribution that deviates from normal.

Furthermore, as noted by one reviewer, from your Figure 6 it appears that the land-use categories are not well "randomized" across space and thus covariates could explain some of your results. You could include some of these first in the fitting sequence of ANOVAs, but we accept that you don't want to put in too many covariates because there are not so many sites to test more complicated models and sometimes correction for covariates can be unjustified if they are not a "true cause" of an observed effect.

One reviewer also suggests that you should try phylogenetic metrics that are not mathematically related to richness.

Your suggestion that the results imply homogenization needs to be tested statistically, which in fact can be done quite easily e.g. by calculating β diversities. You also use a term "heterogeneity", which obviously is taken from output of an R function. However, you cannot expect readers to check this up but rather need to give a clear definition of heterogeneity and how it is calculated.

Third, the Introduction and Discussion sections contain many repetitive statements and statements that lead the reader away from the main story line. The Introduction should focus on the effects of land-use intensity on soil organisms that here have been studied with DNA barcoding, offering a new level of resolution. Your focus and hypothesis on differences in responses between common and rare taxa is really secondary and less "a priori" than the main hypothesis that land-use intensity reduces soil biodiversity. The Discussion contains many speculations, in part related to this secondary hypothesis, that weaken the stronger results regarding the main hypothesis. Generally, we find it very difficult to say rare taxa can "better" indicate biodiversity responses to land-use intensity, because obviously you don't know what the "true biodiversity" is, which you implicitly use as reference.

Reviewer #1:

See above summary.

Reviewer #2:

In this paper the authors use meta barcoding to assess the diversity of soil invertebrates and relate diversity to land use. They find that more intensively managed habitats contain a lower diversity of soil fauna and, in particular, a lower diversity of rare (narrowly distributed) species. The diversity declines are consistent across groups: all groups decline or don't respond to land use, none increase. I think the paper is valuable in looking at soil fauna, which are poorly studied, and the results are interesting in showing that land use change has large effects on these taxa. It is also interesting that it is the rare species that decline with land use, as has been found in other organism groups. However, I have some reservations about the analysis and the framing of the study in terms of endemism.

1) The study aims to show the effect of land use change (conversion of native forests into grassland or perennial cropping) on soil fauna diversity. However, there is no attempt to correct for confounding factors. How were the sites chosen? Was there an attempt to ensure no confounding between land use and environmental factors such as altitude, soil type etc.? All that is said in the Materials and methods is that the sites were distributed across New Zealand. The Discussion mentions some possible confounding, as it is said that native forests are in more "rugged and less accessible areas". In addition, from Figure 6 it appears that many of the native forests are on the west coast of the South Island and there may therefore be climatic differences from the other sites? Currently there is no attempt to correct for confounding factors in the analysis: land use type is the only factor included in the models. I think it would be worth trying to fit some covariates in these models: climate variables and altitude would make sense and some soil variables such as soil type or pH would be good to consider too. This would make the analysis much more robust in showing that land use is the driver of soil fauna diversity, after correcting for soil and climate. It would also add interesting information on the other drivers of soil fauna diversity.

2) I found the term "endemism" confusing in the context of this study. There are no actual data on whether any of these taxa are endemic to a given area, as these data do not exist for soil fauna. Instead endemism is defined as the number of sites occupied by an OTU. Taxa occurring on few sites are therefore considered "endemic" but there is no information on whether they really are endemic or whether they occur elsewhere, e.g. outside New Zealand. Also, if a taxa is found in only two sites it would be considered endemic here but if those two sites were far apart, e.g. it was found in a northern and southern sample, it might not have a restricted distribution, it might simply be rare throughout the range. I therefore think that it would be clearer to talk about rare species and mention that here rarity is based on site occupancy. The situation may be even more problematic for phylogenetic endemism as in the original paper Rosauer et al., 2009, state that phylogenetic endemism values will be biased if closely related species occurring in other areas are missing from the sample (which is highly likely to be the case in this study).

2b) Related to this, I think it is important to mention in the Discussion that rarity is defined here relative to the sites sampled. Some of the species considered rare in this analysis might not be rare at all if they are common in habitats or areas not sampled in this study. There is nothing the authors can do about it this and I think the approach they have used is completely reasonable, but this limitation ought to be acknowledged in the Discussion.

3) How much is the measure of "endemic richness" affected by OTUs occurring in a single site? I could imagine that the distribution of these singleton taxa is quite stochastic and I wonder if it would be worth recalculating the index without them to check that they are not driving the whole pattern.

4) I am not really convinced that the analysis of R2 values (Figure 4) is valid. The R2 values for the different groups are not independent of each other as diversities of different taxa are likely to be correlated due to shared environmental responses or interactions between the groups. I am not sure that this analysis is really needed anyway, it is clear from Figure 3A that rare and phylogenetically distinct species respond more strongly to land use. However, if it is retained the authors should justify it and test the robustness of the analysis, perhaps with bootstrapping?

5) It would be useful to report the correlations between the diversities of different groups, in the supplementary information, to show which respond similarly.

6) The evidence that phylogenetic diversity responds more strongly than species richness is very weak. The R2 values and effect size of land use do not seem to differ between taxonomic and phylogenetic richness or endemism and phylogenetic endemism. The points in the fourth paragraph of the Discussion are therefore not supported by the analysis. If the authors want to check whether phylogenetic diversity does respond more strongly to land use then they should calculate measures of phylogenetic diversity uncorrelated with richness. This could be done in two ways: 1) by randomizing species between sites, whilst maintaining site richness values, and calculating expected phylogenetic diversity for the random communities. A standardized effect size would show if the observed phylogenetic diversity values are greater or lower than expected by chance (Webb et al., 2002). 2) the authors could extract residuals for phylogenetic diversity after correcting for taxonomic diversity and analyse the residuals. I imagine these approaches could also be used to correct phylogenetic endemism values. Also see Winter et al., 2013.

7) How well does the meta barcoding approach work to recover the species present in the sample? Are there data showing that it accurately recovers the species present? Did you check that species present in the Tullgren extracts were also recovered by the meta barcoding? It would be reassuring if there were some data on the robustness of the approach.

8) It is interesting that the authors find such a large effect of land use change on the soil fauna. Other studies in Europe have found that soil fauna are quite insensitive to land use intensification (Gossner et al., 2016). I imagine that this is because they looked at land use intensification within a habitat (i.e. within grasslands) while this study considers land conversion from forests to grassland and cropland. I think it would be worth commenting on this in the Discussion.

9) I feel it would be better to show plots of model predictions and standard errors, rather than the raw data boxplots currently used. If the models include covariates to correct for environmental confounders then this would allow the authors to plot the effect of land use after correcting for other factors.

10) Discussion, fifth paragraph: Collembola also seem resistant to land use change.

11) Table 1 should not be in the main text and could go to the supplement. If you want to use these post hoc tests then you could use letters in the figures to distinguish the land use types that differ from each other.

12) In Figure 3—source data 1B, it would be good to show effects (coefficients) from the models, rather than only showing the SS and F values.

Reviewer #3:

The paper by Dopheide and colleagues examines the effect of land use on soil faunal diversity. Overall, it is a nice analysis and examines a particularly under-studied community type, and I think it will be of value to the broader community. I do have some reservations about the presentation and to my mind, the most important concern of mine is #3 below.

1) There is quite a bit about homogenization in the inference in the Discussion, but this isn't actually tested for. You could do an analysis of β diversity measures (taxonomic and phylogenetic) to determine if communities are in fact more homogeneous in agricultural settings than in forests – see Swenson 2011 PloS ONE 6: e21264 and Jin et al. 2015, J. Ecol. 103: 742-749.

2) The metrics analyzed are good for comparing amongst one another, but I think another needs to be assessed. PD will be highly correlated with richness, and phylogenetic-endemism will pick up on phylogenetic distinctiveness as well as range size -two different possible responses to land use. I would recommend assessing MPD as well to see how land use influences the relatedness of species in communities independent of range size.

3) Phylogenetic-endemism needs to be clarified. How was endemism estimated? Was it across all 75 samples or within each land use type? Further, and this needs to be commented on in the manuscript, estimating endemism from 75 samples is dubious at best and better reflects habitat specialization than endemism per se. Forest specialists can be extremely widespread and not at all endemic. So, you need to be cautious about language and inference. I would recommend getting rid of 'endemism' altogether, except for the methods when describing the metrics, and instead refer to 'habitat specialists'.

4) Further, the comparison between individual species phylogenetic-endemism and community level aggregation can provide more insight as well. You could look at the distribution of species values and how these scale up to the community e.g., see Cadotte and Davies 2010 Div and Dist 16: 376-385 and R function in Pearse et al. 2015 Bioinformatics btv277. Though this latter suggestion is a recommendation and not a requirement since I have a vested interest, so feel free to ignore.

Detailed thoughts:

Abstract:

– There's no real scientific setup or overarching problem statement, just a statement that the authors want to compare something.

– It is not clear what 'community change' refers to. Externally driven or natural fluctuation or succession? I see Land-use later on, the first we see this is with the Results sentence. Needs a better set up. The first sentence of the Abstract should be about land-use driving diversity change and the need to adequately assess community sensitivity to land use.

Introduction:

Does a nice job of setting up the importance of the study, however, paragraph #1 is long and seems to make a number of different points. I prefer short and concise paragraphs that have single subjects and communication goals.

Results:

Subsection “Overall community composition”, last paragraph – it is not clear what heterogeneity refers to.

Figure 2: this is a difficult figure to distil meaningful information. Is there another way to show how lands alters abundance?

Figure 3B and C: can be moved to supplementary material if space is an issue.

Table 1: not needed, significant differences can be indicated on Figure 3A.

Overall, the results are strong and clearly support the major inferences.

Discussion:

Overall good and clear. Again 'heterogeneity' is unclear, please set this up better since it appears to be an important result. Further, there is little biology in the Discussion. Much of it is about the metrics and it would benefit from more discussion of the biology of the systems.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your revised article "Rarity is a more reliable indicator of land-use impacts on soil invertebrate biodiversity than richness or diversity" for consideration by eLife. Your revision and response letter has been assessed by Bernhard Schmid as Reviewing Editor and Ian Baldwin as the Senior Editor.

The agreement was that we cannot yet proceed with the revision until you have more fully incorporated the major suggestions from the first round of reviews. You did provide extensive responses in your response letter, but did not add important items to you revision. These items are, again:

1) Make a linear contrast for the a priori hypothesis that is so pervasive throughout your paper, namely that there is a sequence in which you can put your five land-use categories (you even use this sequence in figures). There is nothing circular and statistically this is much more justified than multiple comparison. As mentioned before, making such a contrast is as valid as any other contrasts, and we can assure you that it will make a much stronger message. The way you can present it, is that you have a term with the five categories and four degrees of freedom and then the alternative of the linear contrast and the remainder with 1 and 3 degrees of freedom. The total of the SS of the two latter will equal the SS of the former but the MS for the linear contrast will be large. We don't mind if you only put this into the supplementary material, but we do want to see it.

Once your a-priori hypothesis that there is an effect of a continuous increase along the five categories, in spite of the inability to measure this continuity, has been tested highly significant, and the remainder, which tests for deviation from the a-priori hypothesis may even be far from significant, you will have a very strong message as you formulated it before but without statistical backing. To fit the linear contrast, just make an explanatory variable LUI with values 1, 2, 3, 4 and 5 for the land-use categories (LUC). Then fit LUI+LUC sequentially. Compare this with the fit of LUC without the linear contrast.

2) Add the analysis with rarest species excluded to the supplement.

3) We disagree with your statement "We think that this test overlooks important aspects of the results, namely the direction of biodiversity differences(as opposed to their consistency among taxa), and which taxa do or do not respond consistently. It is these aspects that the pairwise comparisons are intended to demonstrate." We believe the contrary is true. But it is your paper and we only would like to see the alternative analysis ((Metric ~ LUI+LUC+phylum+order+LUI:phylum+LUC:phylum+LUI:order+LUC:order) in the supplementary material. Note that the LUI-by-taxa interactions are exactly testing differences in direction of biodiversity responses to land-use categories!

4) Add an analysis with environmental covariates to the supplement.

Once we can see these items, we will progress with reviewing.
