# Peer review - Round 1

Editors:
- Detlef Weigel, Max Planck Institute for Developmental Biology Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64541.sa1](https://doi.org/10.7554/eLife.64541.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study addresses an important topic of broad ecological interest and provides important insights into the role of local-scale processes in shaping patterns of species diversity, in order to (i) assess if there is a global latitudinal diversity gradient (using α diversity) of rocky shore organisms and its functional groups and, (ii) whether there are any large scale or local environmental predictors of richness patterns. The strength of this paper is the global coverage of studies analyzed, showing for the first time that rocky shore richness does not appear to peak in the tropics – in contrast to many other studies of marine and terrestrial systems.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Global gradients in intertidal species richness and functional diversity" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Phillip Fenberg (Reviewer #2).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

Your manuscript asks important questions related to the global distribution of intertidal marine biodiversity. Both reviewers and editors agreed that the global scope of the manuscript was interesting and that it could be a significant addition to the literature. Nonetheless, one of the external reviewers found important gaps in the statistical treatment of the data, and both external reviewers identified gaps in the literature review that can potentially affect your dataset and the outcomes arising from its analysis. We think however that a new improved version (addressing comments below) could be resubmitted to eLife. Please note that it would be treated as a new submission, but that we would try to recruit the same outside experts for evaluation.

Reviewer #1:

This manuscript tests for consistent latitudinal gradients in species richness, including in the species richness of some specified functional groups. The question is interesting and important, and has not been investigated extensively in rocky shore systems as far as I can tell (but see below). The authors' approach is to extract raw richness values (counts of species) from the literature, and then test for relationships between richness and a range of explanatory variables including latitude, using GLMs, GLMMs, and GAMs. I am not certain, but I think only univariate relationships are fitted to the data. The northern and southern hemispheres are tested separately as well as together, but different coastlines (e.g., E Pacific vs W Pacific vs W Atlantic) appear to be lumped together for analysis. Spatial structure (I think) is accounted for by establishing 5-degree "bins" and then putting random effects on those bins. I don't know if sites in the same latitudinal bin but different parts of the world (e.g., Chile vs Australia) are put in the same bin or different bins, but I think they are the same. Some recommendations I have for improvement of the study are related to the following:

1. One of the paper's stated aims is to study functional diversity. However, functional diversity (i.e., the breadth of functional space occupied by a biota, or the number of distinct functions represented by a biota) is not actually investigated in the paper. Rather, the authors analyze overall species richness, and then analyze species richness separately for a few different functional groups.

2. One previous study, by Cruz-Motta et al. 2010, is cited by the manuscript but its approach and findings are not discussed at all, which is surprising since the underlying questions are very similar. Another of which I'm aware of is Rivadeneira et al. (2015, DOI 10.1111/geb.12328) focus on gastropods only, but is also a very extensive study of the eastern Pacific latitudinal gradient. That paper is not cited in the current manuscript. The paper does not clearly explain how the current study improves upon those earlier studies or provides complementary insights, nor is there any explicit comparative discussion of the findings.

3. Presumably the species lists considered represent a very heterogeneous body of studies that differ substantially in their sampling effort and potentially their focal taxa (i.e., some studies may count all species in some unit of area, and others only species from certain taxa). Was there any consistency applied in study selection, such as: a set of focal taxa was identified by the authors, and a study was only included if it identified species comprehensively from each of those focal taxa? Sampling effort would no doubt have varied substantially as well, but there does not appear to be any standardization for sampling effort, either through the application of a richness estimator such as Chao1 or the jackknife, or rarefaction, or including some measure of sampling effort as a covariate in the analysis. Lastly, this is technically a meta-analysis, but meta-analytical methods (which would account for, say, differences in sampling variance among replicates in estimates of richness) do not appear to be employed. Given a large number of study sites, I doubt this would make a huge difference, relative to the other issues, so it is less of a concern to me than the other points.

4. There is a lot of important information missing from the description of the methods.

a. For example, how the random effects structure was imposed isn't entirely clear, although my best guess is that a random effect was placed on every 5 degrees latitudinal band. This isn't really an ideal way of coping with spatial autocorrelation, given that adjacent latitudinal bands are also likely to have some autocorrelation – and dealing with it is complicated by the fact that one of the explanatory variables is latitude (one way of modeling spatial autocorrelation is to use spatial coordinates as a trend surface, so in a sense, at least a specific form of the latitudinal component of spatial autocorrelation is in fact what is being tested for).

b. A "passion distribution" (I presume the authors mean Poisson?) was used to test the salinity model, but a negative binomial error distribution was used for the other model fits. This is confusing because the error distribution should depend on the behavior of the response variable (richness), not the explanatory variables. Moreover, the authors then talk about checking for normality and homoscedasticity which is confusing since a negative binomial distribution of residuals (presumably what was modeled) is neither normal nor homoscedastic.

c. It appears but was not clearly stated that only univariate relationships were tested. Why was there no model selection conducted investigating the potential for multiple variables to independently or interactively influence richness? Also, what are the statistical relationships among the potential explanatory variables? To what extent could variables that have statistically meaningful relationships with richness be coincidental, and due to the fact that they are spatially correlated with other variables that play a more causal role?

d. There are references in the text to global versus "regional" analyses, but what exactly these regions are isn't clear. Is it just northern and southern hemisphere data analyzed separately?

My suggestion for addressing the methods issues would be a more comprehensive presentation (or at least investigation and detailed description) of the model fit diagnostics, such as spatial correlograms of both residuals and random effects estimates for the different model fits. Structure in either would indicate something important missing. I would encourage the authors to revisit model diagnostics for models with non-normal error structures. Especially for things like the negative binomial, interpreting standard model diagnostic plots is extremely difficult and non-intuitive, and I'm concerned from the text about how much the authors dug into this. If the authors aren't sure where to start here, one option is to simulate data from a fitted model, and compare the distribution of the residuals from the model fitted to the real data with what the residuals look like when data are simulated to conform exactly to model assumptions. R package DHARMa will do that. Obviously, though that's not the only way forward. If there's evidence of lack of fit, the authors might consider some models with multiple explanatory variables. I am also surprised the authors didn't consider a model accounting for the potential effects of different coastlines. Along those lines, one way to account for "region" is to include it as a categorical factor in the original analysis, rather than do a completely different analysis. For example, E Pacific, W Pacific, E Atlantic, W Atlantic, etc. Hemisphere effects could be considered in this way also. If not, I would want to see that there is no such structure in the residuals (e.g., if one color-coded residual or random-effects estimates according to the coastline, for example, they would not be grouped together).

5. My overall take on the Discussion was that the study did not permit very strong conclusions to be drawn – for instance, the authors conclude that there is a mid-latitude peak in richness in mid-latitudes in the northern hemisphere but not the southern, and they attribute this to ice scour in the far north and desiccation and temperature at the equator. However, the authors don't clearly link this causal attribution to their analyses – the temperature effect looks non-significant, and the ice scour effect small in magnitude, which does not seem to support the authors' conclusion. My broad recommendation for the Discussion is for the causal inferences to be linked more concretely to the results of the analyses. A more thorough set of analyses that addresses some of the concerns that I raised in the previous points might make this somewhat easier.

Reviewer #2:

I really enjoyed reading this paper as it is very much within my area of expertise. The largely held belief that the latitudinal diversity gradient is a common pattern held across all major ecosystems is mostly substantiated by the literature. However, as you correctly state in your paper, it is rarely studied at the global scale in rocky shore systems. If it has been, then it is usually done using a coarse scale (e.g. 5 latitudinal bins) that also includes shallow sub-tidal environments, and/or using species richness based on overlapping geographic ranges (but see Rivadeneira et al. 2015 along the entirety of the eastern Pacific…below). Your findings suggest that there is no clear latitudinal gradient using α diversity on a global scale. While this is true based on your existing dataset, I do have one major comment that should help in your revision of the article:

There is a clear sampling gap in tropical latitudes (based on your figure 1). While this is partly because the rocky shore is sparse within tropical latitudes (e.g. Fenberg and Rivadeneira 2019; Ecology Letters), you are missing some regions in your dataset that clearly have papers on the α diversity of tropical rocky shore ecosystems. For example, along the eastern Pacific coast, you have no data points along the mainland Pacific coast of Mexico. Please have a look at Figure 3b in Rivadeneira et al. 2015 Global Ecology and Biogeography. This paper (which I am a co-author on) is based on rocky shore gastropods using literature sources across the whole of the eastern Pacific coast. While there are fewer examples of sites within the tropics compared to the temperate regions, there is a clear increase in species richness within the tropical latitudes (and this is just for gastropods). This runs counter to your argument that there is no gradient in α diversity, so you could include it in your paper as a potential outlier. Related to the above: see the following papers: the Revillagigedo Islands in Mexico, in Mille-Pagaza et al. 2002 ("Abundancia y diversidad de los invertebrados litorales de isla Socorro,Archipiélago Revillagigedo, México") they find 161 species of marine invertebrates (across a few different sites). The paper is written in Spanish, so it may have escaped your search terms. Here are a couple of other papers showing high diversity along the pacific rocky coast of Mexico:

Hendrickx et al. 2019: "Moluscos litorales (Bivalvia, Gastropoda, Polyplacophora, Cephalopoda) de playas

rocosas de la región de Guaymas, golfo de California, México" find 113 species.

Flores-Rodríguez, P., et al. (2014) Mollusks of the Rocky Intertidal Zone at Three Sites in Oaxaca,

Mexico. Open Journal of Marine Science, 4, 326-337.

These are just a few examples of Mexican papers that you have missed (that seem to fit your search criteria).

You also have missed tropical papers along the coast of eastern Africa: Tanzania: Hartnoll Estuarine and Coastal Marine Science (1976)

Somalia: Chelazzi and Vannini (1979) "Zonation of Intertidal Molluscs on Rocky

Shores of Southern Somalia".

And it appears that you have missed papers from New South Wales (your example from Figure 1 appears to be in Queensland): Underwood 1981 "Structure of a rocky intertidal community in New South Wales: patters of vertical distribution and seasonal changes".

Benkendorff and A.R. Davis (2002): "Identifying hotspots of molluscan species richness on rocky intertidal reefs"

These are just a few examples of tropical papers that seem to fit your search criteria but are missing in your analysis. The point I am trying to make here is that while there may indeed be fewer papers in the tropical regions, there are definitely more to be found. While this may not change the overall results of your paper, I think you should adjust your search criteria as you are likely missing quite a few from tropical rocky shores. Some of the papers will be in different languages (especially the Spanish papers from Mexico and Latin America), but they should not be discounted in my opinion because some of them clearly show high levels of α diversity within the tropical latitudes. In conclusion, I really do like this paper and I feel like it will make a valuable contribution – but I feel like the dataset is incomplete and would benefit from a more thorough search for papers within tropical rocky shores.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Global gradients in intertidal species richness and functional groups" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by Detlef Weigel as the Senior and Reviewing Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Phillip Fenberg (Reviewer #1); Lisandro Benedetti-Cecchi (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This study addresses an important topic of broad ecological interest and provides important insights into the role of local-scale processes in shaping patterns of species diversity, aiming to (i) assess if there is a global latitudinal diversity gradient (using α diversity) of rocky shore organisms and its functional groups and, (ii) whether there are any large scale or local environmental predictors of richness patterns. The strength of this paper is the global coverage of studies analyzed, showing for the first time that rocky shore richness does not appear to peak in the tropics – in contrast to many other studies of marine and terrestrial systems. These outcomes are not specific for rocky intertidal systems, with an increasing number of studies showing that the search for global ecological patterns may be elusive. While sampling in the tropics and the polar regions is poor (acknowledged by the authors), this should be viewed as a call for further research in these regions – not as a weakness of the paper per se. There are also some reservations on how the analysis has been conducted, including the lack of standardization of sampling effort and other details (e.g., size of sampling units) to derive a comparable measure of diversity across sites.

Essential revisions:

The latitudinal gradient of diversity has been studied and confirmed in many aquatic and terrestrial habitats and species across the globe. In the vast majority of cases, richness increases towards the tropics. Using an impressive global dataset of latitudinal diversity gradients in 433 rocky intertidal assemblages of algae and invertebrates from the Arctic to the Antarctic, Thyrring and Peck show that rocky shore ecosystems may not follow this general pattern. The authors show that there is no clear latitudinal gradient for rocky shore organisms using alpha diversity - as posited by prevailing theories - although some functional groups exhibit contrasting patterns. Diversity within functional groups of predators, grazers and filter-feeders decreased towards the poles, whereas the opposite was observed for macroalgae. Correlation with environmental drivers highlighted the importance of local-scale processes in driving spatial patterns of diversity in rocky intertidal assemblages. The paper is well written and the many of the analyses are well done, but there is the concern, which the authors acknowledge, that sampling within tropical latitudes is sparse and needs to be carefully considered when interpreting the results of this paper.

1. The relevant data to standardize species richness may not be available from the primary literature. However, it should be possible to employ relevant standardization methods within the 5{degree sign} latitudinal bands in which the data have been aggregated. An analysis based on standardized data, at least for the more data-rich latitudinal bands, must be added.

2. Employ models that allow assessing unimodality, which is stated but untested. At the bare minimum, a quadratic relationship with latitude should be included in the GLMM. As implemented here, the GLMM employed to relate diversity to latitude can only detect linear trends, but not unimodal patterns and the mid-latitude peak suggested by LOESS for the northern hemisphere. To provide a formal test for unimodality, models with or without a quadratic term could be contrasted using standard model comparison procedures. Alternatively, GAM could be used to evaluate nonlinear effects.

3. Clarify whether p-values are relevant or not. As is, it is confusing. For example, the legend of Table 1 mentions p-values, but these are not reported. Materials and methods indicate that 95% confidence intervals are used to take decisions on null hypotheses, suggesting that p-values are not used in the analysis (lines 436-439). Nevertheless, p-values are reported in Table 2.

4. Provide a rationale for distinguishing between canopy and other algal forms (the distinction is compelling, but it is not explained).

5. We like the conclusion on the importance of local-scale processes. This should be placed in the context of previous studies that have quantified patterns and processes at multiple scales reaching the same conclusion.

6. We could not access the data repository indicated in ref. 91, so we could not assess whether the analysis may have missed potentially relevant papers.

7. Provide the number of studies available for each band in an Appendix.

8. The analysis on macroalgae (e.g., Figure 5) distinguished between canopy and no-canopy algae. This is probably correct, but the rationale for this distinction has not been provided. I think some context is needed, especially to clarify the role of algal canopies in maintaining diversified understory assemblages.

9. The overall conclusion that more studies are needed to assess the magnitude and influence of physical and biotic drivers across multiple scales is important and appropriate. However, many studies have examined processes across scales in rocky intertidal systems (including canopy-removal and limpet-exclusion experiments) and many descriptive studies have quantified variation across multiple spatial scales, emphasizing the importance of small-scale variability in pattern of distribution, abundance and diversity of species on rocky shores. A more thorough discussion of this literature (e.g., Underwood & Chapman, Benedetti-Cecchi, Denny, Coleman, Martins, Fraschetti, etc) would be welcome.

10. In the abstract please say something about more sampling being needed in the tropics. Perhaps line 34.

11. Line 85: What do you mean by "inadequate estimates of intertidal areas"? Inadequate in what way? And in what sense are you talking about area?

12. Line 96: Replace "controlled" by "predicted".

13. Figure 2: where are the R2 values on this plot? How do you get an R2 from a LOESS fit…?

14. Salinity is a local and a regional variable in your analyses, please briefly explain why (Figure 3 and 4).

15. Figure 5: hard to see the box plots, consider making them a different colour or shade.
