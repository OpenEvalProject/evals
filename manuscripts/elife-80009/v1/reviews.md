# Peer review - Round 1

Editors:
- Kelly Swarts, https://ror.org/05twjp994 Gregor Mendel Institute of Molecular Plant Biology Austria

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80009.sa0](https://doi.org/10.7554/eLife.80009.sa0)

Teff (Eragrostis tef), a small-market domesticate native and commonly grown in Ethiopia and the Horn of Africa, is comprehensively characterized for genetic, ecological and phenotypic variation in this ambitious and interdisciplinary publication. Integration of small holder farmers in phenotyping the collection, with an emphasis on gender considerations, elevates the characterization of Ethiopian teff. This paper provides a solid foundation to accelerate teff breeding for a changing climate, and provides an excellent model for the characterization of novel and underused crops.


---

# Peer review - Round 1

Editors:
- Kelly Swarts, https://ror.org/05twjp994 Gregor Mendel Institute of Molecular Plant Biology Austria

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80009.sa1](https://doi.org/10.7554/eLife.80009.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "Data-driven, participatory characterization of farmer varieties discloses teff breeding potential under current and future climates" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Bela Teeken (Reviewer #2); Laura Morales (Reviewer #3).

Comments to the Authors:

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife.

There was a lot of enthusiasm for the work in principle, but the common judgment was that revision would be considerably more extensive than commonly expected for eLife. Nevertheless, while we cannot formally invite revision, we remain very interested in the work. If you resubmit a suitably revised version, it would be treated as a new submission, but we would aim to recruit the same editors and reviewers to critique the work.

All of the reviewers were enthusiastic about the comprehensive scope of the manuscript but they raised concerns regarding a number of the analyses. The reviewers make specific recommendations regarding these concerns that should be addressed in a future submission. Critically, two of the reviewers highlight methodological issues with the choice of 6 clusters that were used for the diversity analyses that underlie a number of the subsequent analyses.

Reviewer #1:

Overall summary

"Data-driven, participatory characterization of farmer varieties discloses teff breeding potential under current and future climates" by Woldeyohannes and colleagues is a fascinating, interdisciplinary approach for understanding genetic, ecological and phenotypic variation in teff (Eragrostis tef), a small-market domesticate native and commonly grown in Ethiopia and the Horn of Africa. They assess genetic variation in traditional (landrace) and improved breeding varieties from a germplasm collection representing the diverse ecological zones of Ethiopia, attempting to link genetic with environmental variation. The collection was evaluated in two diverse locations by the authors for breeder phenotypes but also by smallholder teff farmers. Heritability for farmer traits is high and also highly correlated with breeder traits. Interestingly, men and women, while they mostly agree on the best varieties, have slightly different preferences. The authors conduct a GWAS but present very few results, mostly based on a few randomly chosen QTN. Finally, the authors present an interesting analysis using a gradient forest predictive model to understand the impact of environmental gradients of genomic variation, which will help identify vulnerable areas under climate change. This is an important topic that is outside of my field.

While the data collection, methodology and aims of the paper are very compelling, it suffers from some important interpretation and analytical issues in the characterization of genetic diversity. Specifically, clustering analysis used throughout the paper was not appropriate based on the data presented. The authors present some tantalizing results associating genetic diversity of environmental diversity, but these analyses could be clarified, tightened and streamlined. The authors attempt characterize genetic diversity in terms of social interactions but I did not find the proxy used for social interaction convincing. The phenotypic analysis, especially with respect to farmer selections was very clear and compelling but it would have been nice to see more follow-up on the GWAS analyses associated with these traits.

Introduction

The authors do a good job of introducing the market importance of teff and its role in small-holder agriculture but I would have liked more information on teff biology. Line 89 states that it's a tetraploid, but is it auto or allo? Is the ancestor also tetraploid? What was it domesticated from? Naturally outcrossing or inbreeding? What were historical effective population sizes (in the landraces and the breeding material)?

Results

Teff farmer varieties harness broad genetic diversity

This section showcases the genetic relationships between accessions and is associated with figure 1. The genetic material includes landraces, breeding lines and outgroup wild relatives on RADseq markers, which is only clear from looking at the associated methods and a summary here would be welcome. While the Admixture and PCA analyses are performed correctly, there are serious issues with the interpretation of outputs.

Admixture results (K = 2-10) are presented as well as a PCA plot colored based on the DAPC clustering for the same PCA. The DAPC clustering results are then shown in geographic space, according to altitude and to agroecological zone.

Buried in supplementary material 4 are the metrics for evaluating model fit for the admixture as well as the DAPC clustering. The lowest cross-validated error rate (best predictive accuracy in leave-one-out) is for K = 20, but the authors state the K = 6 is the "best" K. Likewise, the lowest BIC (model fit) value for the DAPC clustering is 10, not 6 as the authors state.

The authors decision to promote six clusters is not supported and the main figure 1 and all subsequent uses will need to be updated to reflect the best fit values (DAPC 10; admixture 20). It would also be informative to contrast breeding material with landraces as this is one of the main aims of the study.

The distribution of teff genetic variation is associated with geographic and environmental factors.

This section, associated with Figure 2, seeks to contextualize teff genetic variation within environmental and social variation. Overall, the aim of contextualizing genetic variation ecologically and socially is a good one and the ecological associations are interesting and appropriate but I don't find the social proxies convincing and some of the analyses – the neighbor joining plot with outgroups in S2, and perhaps the FST analysis in 2E – are out of place.

2A is a PCA of bioclimatic variation from interpolated weather data assigned to each landrace and there are interesting patterns with respect to DAPC cluster groups (which will need to up updated), which are highlighted in the text. 2-C and D show FST values, presumably based on populations assigned by regional political district as in part E but this is not explained, against geographic and environmental (the average of orthogonal bioclimatic variables and altitude) difference. The regional districts are supposed to be a proxy for social connections and markets (lines 185-187) but there is no citation or presented evidence for why this is a reasonable proxy.

The main conclusion (lines 188-192), that both isolation by geographic distance and environmental distance contribute to genetic differentiation, is not surprising to since the populations used for FST were defined geographically and the geographical and environmental distance are likely fairly highly correlated. 2E shows the F¬ST matrix, which shows that samples from Tigray are the most genetically isolated, while those from Amhara and Oromia are relatively more admixed. F2-S1 are boxplots of the bioclimatic values clustered by the DAPC groups, which, with updated DAPC clustering, are an interesting look at genetic and spatial differentiation, especially the bottom row with the values for the bioclimatic PCs.

Participatory evaluation of the teff diversity prioritizes genetic materials for breeding

This section, associated with figure 3, explores the participatory evaluation results, comparing scores between men and women and between the farmer and breeder evaluations. There was generally very high agreement between breeders and farmers and some intriguing insight into gender-based differences in evaluation criteria. The phenotypic models were appropriate and data presented and textual discussion was overall clear and well-supported.

Participatory, climatic, and agronomic diversity identify candidate loci for teff breeding

The approaches used for GWAS analysis are appropriate based on that reported in the methods but there are no supporting figures. At the least, I would expect Q-Q plots to assess population structure correction and Manhattan plots in the supplemental. For the specific genes that the authors focus on it would be good to also see the local Manhattan and LD information. However, the litanies of linked gene models could also probably be dropped or minimized in the text (it may still be an important resource for future studies to have in the public record). I think the authors could have done more with the GWAS results.

Teff cultivation is vulnerable to climate change

This section, associated with figure 4, uses a gradient forest predictive model to understand the impact of environmental gradients of genomic variation, which will help identify vulnerable areas under climate change. These are not analyses I am familiar with and I do not feel qualified to review this section in detail.

Conclusion

The conclusions are pertinent and help motivate future directions.

Methods

The methods are generally well described. As the methods are situated after the results, it would be useful to reiterate some of the key points from the methods under results to help situate the reader.

Specific comments and suggestions

It would be good to give the whole manuscript a copy edit. There were a number of small grammatical and word choice issues I noted, a few of which are below, along with additional suggestions.

127 what is the difference between moist and humid? Citation?

132 what kind of libraries? There should be a short statement of library choice and associated biases.

163-165 This statement is probably true if you're deeply familiar with the germplasm and the environments, but it's not clear to someone with no prior knowledge based on the figure. It's actually better supported by figure 2A.

174-175 Figure S1-5 does not support this statement. Beyond the fact that the K was chosen at random, as were the DAPC clusters, admixture is not quite the right evidence. A better line of support for this statement would be something along the lines of "Limited population stratification, as evidenced by less than 15% of the total genetic variance explained by the first three principal components (Figure 1-B-C)…".

200-204 You can refer back to other figures to connect dots – it would make more sense for the pop gen to be presented together.

207 What environments are these trial locations in? More description.

218-220 Define shorthand phenotypes here (the ones used in figure 3)

Figure 1: It is not completely clear from the legend in Figure 1, but I believe these figures include the landraces and breeding material (except panel D – this must be clarified). I would suggest that rather than the current panels it might be more informative to just see admixture (K = 20) ordered by breeding vs landrace, altitude or agroecological zone rather than based on unsupervised clustering (admixture). Likewise PCA plots colored based on independent values (altitude, improvement status, etc) may be more informative than using the DAPC cluster assignments (K = 10), although I like Figure S1-6 and the boxplots in 1E are probably more informative than just coloring based on altitude would be. There is nothing about improvement status in this figure – it would also be interesting to highlight the genetic relationships between the breeding and landrace material (S3 suggests that much of the breeding material clusters)

Figure 2: I would rethink the social proxy (market analyses? Ethnicity?) and clarify the analyses performed for the bioclimatic associations. I think S1 (the last row) would be a good analysis to include in the main figure. I would put S2 with Figure 1, maybe I'm missing something but I'm not sure why it's there. I also don't understand why the correlations between the climate variables and the PCs are presented in B – this is clearly visible from the eigenvectors in A – but if it is informative I would suggest more discussion.

Figure 3: Very interesting. It might be interesting to see the correlation plot in A separated by men and women.

What happened to the GWAS analysis?

Methods:

Plant Materials: seems reasonable and sufficiently described.

Sequencing and Variant Calling: I'm not very familiar with RADseq calling pipelines but it seems reasonable. This is a well-established approach though and if the authors are following a previously published processing pipeline it would be good to cite.

Spatial and bioclimatic characterization: It's not clear to me when the different datasets are used, and why you would use one over the other.

470 Why use the highest resolution for something like a landrace that has a km rather than meter resolution?

More information on the grow-out locations would be welcome.

Reviewer #2:

In the context of teff production and consumption in Ethiopia the authors advocate breeding initiatives to strengthen this crop that is important for the livelihoods of the many small holders in Ethiopia by highlighting the limited yields, the limited breeding efforts made in this crop and the anticipated impactful climate change. By using genetic, climatic, geographic and participatory variety selection, gene pools are identified that would best inform parents to use for future breeding initiatives. This goes even further and shows the possibility to identify crucial genetic markers needed for breeding focus.

With convincing strength, the authors employ genetic analysis of landraces collected all over the country and link this to the different agro-ecological regions and niches as well as the different ethnic traditions and to the climatic data including a forecast of climatic factors based on an extrapolation of historic climate data. Although overwhelming at first, the large amount of figures well illustrate the argument and well satisfy if one wants to get some deeper understanding (supplementary figures). A great innovative strength is the proposition of a standard toolbox to combine the different data to provide product profiles for teff breeding.

The authors rightly state that the suitability of varieties does not only depend on ecological, climatic and product data but also on socio-cultural variables and they take this into account by stating that the regions coincide with the different ethnic groups in the country. These ethnic groups could however be named and their differences with regard to teff related practices and preferences highlighted and related to the two different groups of farmers chosen for the participatory variety selection. The selection strategy of the farmers could also be provided.

A little more discussion could be provided on the representativeness of the two PVS and phenotyping sites and the farmers evaluating those. In the conclusion the authors cite the TRICOT approach as a way forward to decentralize PVS and get better systematic and representative testing of the genetic resources. The limitation of the only two sites in which the genetic collections were grown and the possible G x E influence on the phenotyping of the varieties could also be highlighted. However, the fact that with the two locations such great results were obtained in linking all the datasets shows the potential of the approach taken.

321 landraces from 3850 Provide were selected for the study. It will be important to provide the selection strategy used to get to the 321 varieties. This selection strategy could also be highlighted outside of the methodology. The selection strategy might also be related to the time of collection of the varieties. Are these 321 chosen in a way to simply represent the largest genetic diversity in the collection or is the time of collection of the samples also included: to represent the varieties that are currently still cultivated?

With regards to choosing men and women and comparing them separately there is not discussion on why one would expect differences. Only in the conclusion Weltzien et al. is cited in this respect but this needs more attention and reference to some more literature, especially in relation to the Ethiopian context. What is especially needed is an explanation of the different tasks (roles) of men and women in Ethiopia with regards to teff cultivation and possibly processing. This should be provided in general and in relation to the two study sites. This could also provide the background to a short discussion to interpret the similarities and the difference observed (appreciation being more related to biomass yield and panicle weight for women while for men it was plant height and grain filling period, could this be explained by women using plant parts for animal feed or any other activity in which they more feature?). I know that this is not the main focus of the paper but the fact that men and women's preferences were analyzed and discussed separately demands a discussion with regards to the results and the strategy used to select the men and women.

This work is not only relevant to under NUS crops but also for breeding in general and especially for public sector breeding. In this respect the authors could open up this approach to be more generally applied to other crops and could highlight the importance of their approach for customer and product profiling and especially for customer profiling with which especially public breeding is tasked to achieve social impact as cost effective as possible.

Figures

With regards to figures 1 and 2: it is great to have all these figures close to each other for good cross referencing, however in that case it will be very important to have extremely good resolution. A solution could be to arrange the figures in a way that the now smaller figures in Figure 1 become bigger and the larger figure (Figure 1 D) become a little smaller so that the PCs are better visible, this is minor work to arrange. Also, the legenda with the colored dots indicating the DAPC clusters could be made much bigger for easier determination of the colors. The same counts for figure 2.

Please verify the Y axe on figure 3E. Should this not be PA instead of PL? It was panicle appreciation that was evaluated with the farmers not panicle length?

Reviewer #3:

The authors have conducted an interdisciplinary characterization of a valuable teff diversity panel using well-supported methods, except for the selection of genetic clusters. Although the methodology itself is not novel, the interdisciplinary nature of the study sheds light on a wide range of Ethiopian teff germplasm characteristics, from environmental adaption to gender preference.

Strengths:

The incorporation of farmer's knowledge and gender preferences in the genotypic and phenotypic analysis of the germplasm was well done and nicely presented. This kind of information is absolutely necessary for the improvement and intensification of NUS, especially in smallholder farmer systems. Few germplasm characterization studies, both on NUS and staple crops, have reported such a broad range of characteristics.

Weaknesses:

Although many of the analyses rely on the differentiation of genetic clusters, the authors have inappropriately selected the optimal number of clusters (K). The authors conducted a cross-validated error analysis of various ADMIXTURE K values and a similar analysis of BIC statistics of various DAPC K values. Figure 1—figure supplement 4 clearly demonstrates that K=20 for ADMIXTURE and K=10 for DAPC, as these values of K have the lowest cross-validated error and BIC, respectively. However, the authors claim to have chosen K=6 because (a) there is a slight flattening of the ADMIXTURE error curve after K=6 and (b) K=6 has the lowest DAPC BIC statistic, neither of which are supported by the results.

Although the authors reported high broad-sense heritability (H2) for several agronomically important traits, variance components for the terms (genotype, environment, GxE, gender, error, etc.) used to estimate H2 were not shown. A table including H2, variance components, and the numbers of levels and observations for each term is necessary to assess the validity of these results. This information would also shed light on the relative influence of genetics, environment, gender, etc. on trait variation.

As stated above the methods used to select K=6 as the optimal number of clusters was statistically inappropriate. Although K=20 had the lowest cross-validated ADMIXTURE error, this value seems too high. I would suggest using K=10, as this value of K had the lowest DAPC BIC, showed a more clear flattening in the ADMIXTURE error curve, and is closer to your desired value of K=6. Did K=6 correspond to some prior knowledge on the diversity panel, for example from breeders' knowledge? If so, perhaps this could be stated or incorporated in some way to support your choice of K=6.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Data-driven, participatory characterization of farmer varieties discloses teff breeding potential under current and future climates" for further consideration by eLife. Your revised article has been evaluated by Detlef Weigel (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Essential revisions:

1) Further explicate the relative contributions of genotype, environment and GxE for the traits evaluated, per the more detailed suggestions of reviewers 1 and 3. This may be supported by the Oryza research suggested by reviewer 2.

2) Reassess the discussion of the GWAS results in the text and supporting material, particularly DM and PC2_bio. Per comments by reviewer 1, the QQ plots show that these traits are highly impacted by residual population structure and thus subject to an excess of false positives.

3) Provide a bit more discussion of gendered roles in agricultural production, taking into account comments by reviewer 2.

Reviewer #1:

The authors in their responses have addressed most of my concerns and I think the paper reads much more clearly now. I only have two additional comments:

With respect to the GWAS results, these can now be evaluated with the inclusion of the QQ plots. All traits except bio14 are somewhat confounded with population structure (genome-wide deviation from expectation of no association, or deviation from the line in the QQ plot) and DM and PC2_bio are very correlated with structure and the QQ plot suggests that neither of these traits have truly associated loci in this study. The authors discuss results from especially DM a great deal and I think the discussion of these results should be reevaluated.

The authors also state in the conclusion that "Multi-location trials are needed to capture the range of genotype by environment (G x E) interactions that influence agronomic performance of teff, which we could only partially characterize" but they do have two locations and are able to model GxE (although, more locations would certainly lead to better estimates). For a genomic resource paper, it would be very beneficial to report the impact of GxE directly (and how the landraces and improved varieties may differ, as has been found in other crops).

Reviewer #2:

The authors have done a great job in revising the manuscript, which is much easier to read and figures and tables. The organisation has also improved. As far as my expertise allows the authors have also well approved the technical analysis part of the manuscript.

The sampling of the PVS participants has been described satisfactorily and the reason why to include gender has been articulated. I can imagine that the authors did not find any literature or resources to explain the difference observed between women and men. I highlighted that a reason could be that women are tasked with animal feeding and look at the plant's vegetative parts also as a resource of animal food while men would not focus on that so much because it might be out of their gendered roles. The authors could quickly consider this issue and see if there is any probability in this being the case or any other reason that could be mentioned to explain the differences observed between women and men. Any little clue or hypothetical phrase would give the gender dimension just a little more depth and clue for further investigation, rather than just saying that differences are to be expected.

The authors nicely made the link to general breeding and the development of customer and product profiles in (public) breeding that are more and more expected to deliver on social impact in line with the sustainable development goals

The issue I raised with regards to the representativeness of the PVS trial locations has also been resolved satisfactorily.

This is now a really strong paper and needs to be published so I will be able to share it as a good example of transdisciplinary data driven research.

Please correct on line 161-162: reference is made to two figures (as the word 'and' is written) but only figure 6 is mentioned.

Furthermore, I would like to point the authors to the following publications based on work on the under researched African rice (Oryza glaberrima) and how farmers long trajectories of selection resulted in selecting 'robust' varieties that are adapted to change and dynamics (social as well as climatic) rather than narrow local localities. Any reference to this body of work could be made, although the manuscript stands strong as it is without referring to this body of work.

http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0034801

http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0085953

http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0007335

https://link.springer.com/article/10.1007/s10745-012-9528-x

Reviewer #3:The authors have done a nice job revising the manuscript using 10 genetic clusters, following the recommendations of the reviewers.I would suggest incorporating the information in Supplementary file 1C into Tables 1 and 2. For example, columns for variance explained by genotype, location, rep, error, etc. could be added to these tables.

I also recommend discussing the results in Supplementary file 1C (or Tables 1-2, if the authors choose to merge this information) further. The experimental design appears to have allowed for high estimation of heritability, which the authors have already stated in the first and latest versions of the manuscript. However, as a plant breeder, I would like to know more about the relative contributions of genotype, environment, GxE on the different traits measured in this germplasm. For example, it is interesting that (a) for BPR, location explains 75% of the variance, while genotype explains a 18% of the variance and there is no GxE effect, which contrasts to (b) CDF, which has large GxE variance (66%) and relatively smaller proportions of the variance are explained by genotype (7%) and location (19%). There are likely some trends/comparisons among traits that can be discussed, such as which traits tend to have high GxE vs traits that have high location effects vs traits with high genetic variance.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Data-driven, participatory characterization of farmer varieties discloses teff breeding potential under current and future climates" for further consideration by eLife. Your revised article has been evaluated by Detlef Weigel (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1) Both reviewers 1 and 3 are still concerned with the interpretation of the GWAS. Please see especially reviewer 1's lengthy explanation to help clarify interpretation. Please take these concerns into account when interpreting GWAS results and reporting significant loci.

2) All of the reviewers have made small, specific comments that should be addressed.

3) A final copy-edit after changes have been made.

Reviewer #1:

The paper reads much better and I am satisfied with the incorporation of GxE analysis. I still have concerns with the interpretation of the GWAS results and would recommend a final copy edit to fix the grammatical errors introduced in the editing process.

Statistically significant p-values are detected as deviations from the expectation of no-association based on statistical linkage between the causal association and the tested SNP (there are likely no causal loci tested in this limited marker set). The foundational assumption in GWAS is that these associations will be in local LD based on limited recombination in the region surrounding the causal polymorphism, allowing the researcher to zoom in on the loci underlying trait variation. This is visualized on an QQ plot as most dots on the diagonal of no-association with a small deviation associated with only the most significant SNPs (bio14 is a good example of this). On a Manhattan plot, these will for a localized peak around causal loci, characterized by the extent of the haplotype block associated with the causal polymorphism and the sampled marker density.

However, linkage can also exist between causal polymorphism and loci across the genome, even on other chromosomes, because selection is not random or evenly applied across a species or population. When populations differ due to drift processes, and selection is nested within randomly varying genetic structure, GWAS tests for the trait under selection will also find associations with the variants associated with differentiation between populations. For example, one population lives in a cold, highland environment and one lives in a tropical, lowland context. The highland population has a shorter growing season and consequently flowers earlier to ensure that the grain can mature in time before frost. The populations were already a bit different due to distance and chance, but now that the flowering window is non-overlapping for these populations it ensures that gene flow is basically stopped and that the populations will move further apart. If one were to do a GWAS for days to flowering or maturity (or for temperature or growing season variation) across these two populations the resulting QQ and Manhattan plot would look like the ones in the analysis for PC_bio2 or for DM; an early a persistent deviation from the expectation of no association in the QQ that localizes all over the genome in a Manhattan plot. This is not to say that there are not real associations (the peak on 6A is likely associated with a real causal locus for DM), but they are confounded with underlying structure and "statistically significant" associations are no longer a good way to identify truly associated loci. A better way to think of GWAS with these qualities is that the top SNPs are enriched for linked causal associations but any given association is suspect.

With this in mind, I would suggest a bit more discussion of confounded structure. Perhaps a way to frame it is in the context of local adaptation, tying in the GF models and variance analysis of GxE for the various traits.

331-336: The accepted associations for DM and PC2_bio are still very lax and based on the QQ plots heavily confounded with underlying population structure. This underlying structure is almost certainly driving association with the gradient forest model and I think that the conclusion that this association "support the importance of phenology in teff adaptation and geographic distribution" is reasonable, but not because of genetics underlying days to maturity per se. If the authors were to include a statement to this effect the overall interpretation is reasonable.

341-343: Again, when two traits are both heavily confounded with underlying structure it is not surprising that they would colocalize (via the third variable of structure), and I would be especially sceptical of colocalized regions between these traits.

349-355: Agree that this peak is likely real because of the very strong local LD. Not convinced of anything else

Reviewer #3:

The authors have done a nice job including more information about GxE, genetic variance, etc.

I am still not convinced of the GWA results for DM and PC2_bio, which show a very large deviation from the expected p-value distribution. The abundance of false positives cannot merely be dismissed with the authors' statement that "some of the associated traits…showed some statistical inflation on QQ plots likely contributed by residual population structure". A large proportion of all SNPs tested were deemed significant (assuming that the significance cut-off was approximately -log10p = 3.5) for DM and PC2_bio. I would suggest that the authors use a secondary threshold based on a visual assessment of the QQ plots. For DM, I would suspect that the ~5 SNPs with -log10p > 4.8 are truly significant (QTL on chromosome 6A). Similarly for PC2_bio, the 2 SNPs at the tail of the distribution are likely significant.

With respect to the gender aspects of this manuscript, I would recommend including references from similar work done by the NextGen Cassava project. Here are two examples:

https://doi.org/10.1007/s12231-018-9421-7

https://doi.org/10.1002/csc2.20152
