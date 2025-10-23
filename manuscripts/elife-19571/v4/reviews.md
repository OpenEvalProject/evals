# Peer review - Round 1

Editors:
- Colin A Russell, University of Cambridge , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.19571.020](https://doi.org/10.7554/eLife.19571.020)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Global mapping of highly pathogenic avian influenza H5N1 and H5Nx clade 2.3.4.4 viruses with spatial cross-validation" for consideration by eLife. Your article has been favorably evaluated by Wendy Garrett (Senior Editor) and three reviewers, one of whom served as a guest Reviewing Editor. One of the three reviewers, Richard J Webby, has agreed to share his name.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript describes the development of global risk maps for H5N1 and H5NX viruses. Building on previous work mapping risk by country and by region, the authors sought to build parsimonious global suitability models based on host and environmental factors. In order to discriminate among models incorporating different variables the authors used boosted regression trees and identified human and animal population densities as key factors influencing risk (as supported by previous work). While the basic factors identified are perhaps not unexpected, refinement and improvement to mapping practices are needed to help support global preparedness and response.

All reviewers agree that the data shed light on an important and interesting problem. However, before we can recommend acceptance, a number of issues should be addressed.

Essential revisions:

1) It is not clear why the distinction was made between clade 2.3.4.4 viruses and all H5 viruses others. As pointed out, the 2.3.3.4 viruses did have different neuraminidases and did transmit to North America, but there is no convincing evidence that we are aware of that supports the authors assumption that "they may have different phenotypic characteristics leading to different transmission patterns". There are very likely different risk factors combined in the "other clade" category. For example, clade 2.2 and clade 2.3.2.1 viruses spread out of Asia much like 2.3.4.4 (with obvious exception of migration to Americas) and at least appeared more associated with wild bird spread. Were any other subclade analyses done? Is there evidence, or at the least practical reason, to support clumping all other clades together?

2) The use of human population distribution for pseudo-absence generation needs to be better justified. Given that the purpose of pseudo-absence generation is to reflect the bias in sampling or reporting effort present, it is not obvious that human population density best reflects this difference. We suggest the authors consider approaches that integrate other strains of avian influenza as direct absence locations. Given EMPRESi as a data source, this should at least be feasible at least for H7 viruses. Otherwise, the authors need to provide more context for why such testing would scale with human population; it could be argued that testing could scale with avian distributions better than it does humans (e.g. in the United States). There may also exist other, more appropriate, high resolution proxies for this reporting bias.

3) As pointed out in the Methods section, the inference of pseudo-absences can be biased by the fact that the pathogen has not been introduced into a region. This is undoubtedly true but the assertion that this bias is likely to be stronger for H5Nx than H5N1 viruses is peculiar. The suitability maps in Figure 4 differ substantially for North America, presumably because of the lack of H5N1 infections and thus inferred absence. However, as in comment 1 above, we are unaware of evidence to suggest that there are phenotypic differences between the H5N1 and H5Nx viruses that would make North America suitable for H5Nx viruses but unsuitable for H5N1 viruses. It could be argued that H5N1 has also not yet had the opportunity to explore its full potential range.

4) In the sixth paragraph of the Results the authors discuss the results of Chinas inclusion in the high suitability zone, but essentially only when the IsChina variable was removed. What exactly does this mean regarding the influence of this variable? It is obviously clear China is very much a high suitability zone for these viruses. Along similar lines, if IsChina is meant to account for mass poultry vaccination in China, why have similar variables been ignored for other countries that have or have had mass vaccination campaigns – particularly Indonesia, Egypt, and Vietnam?

5) The authors produce predictions that are many miles away from any previously reported occurrences – whilst the dotted lines on Figure 4 help the reader be aware of this, the authors should also consider a multivariate environmental similarity surface approach to gauge the extent to which these records are extrapolation, and where predicted values fall within environmental space already considered by the presence points already in place. There is an example of its usage in Elith et al. 2010 http://onlinelibrary.wiley.com/doi/10.1111/j.2041-210X.2010.00036.x/full

6) We are concerned about the independence of the occurrence points, particularly with respect to secondary spread rather than an inherent feature of the underlying environment in these locations. An example of where this is problematic would be charting the progress of Nipah outbreaks in Malaysia in 1998 – pigs and humans over a widespread area were infected yet in terms of environmental suitability, only one location, where the index case arose, is suitable for inclusion. All other cases are more appropriately modelled by understanding the nature of swine connectivity via livestock trade and human-animal interactions. To what extent are these influenza cases located, and to what extent are they environmentally driven?

7) This exposes a broader issue relating to the inclusion of the poultry layers in the model. Niche maps are simply reflections on the potential for presence of the pathogen – by using data from poultry and then including poultry measures as predictors it is therefore unsurprising that they have a high explanatory power within the model, particularly where there may be ineffective control for the biasing effects this may have. As a consequence, the maps may be a more accurate prediction of where outbreaks are more likely to occur (or be reported) rather than an accurate depiction of potential occurrence (i.e. anything from singular cases to very many). It was interesting therefore to see how the inclusion/exclusion of different covariates impacted this – even exploring what impact that has when converted into a map would be interesting to see, particularly an output based just upon Sets 2 and 3 alone.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Global mapping of highly pathogenic avian influenza H5N1 and H5Nx clade 2.3.4.4 viruses with spatial cross-validation" for further consideration at eLife. Your revised article has been favorably evaluated by Wendy Garrett (Senior editor), a Reviewing Editor, and one of the original reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Reviewer #2:

The authors response to reviewer comments have clarified some initial concerns as well as provided interesting additional analyses. However, I do have some still outstanding issues, as well as some newly raised concerns given the authors response.

It was interesting to note the use of gazetteers to approximate disease occurrence since this adds an additional concern as to how reliable this classification is, and if in doubt, what steps were taken to mitigate (e.g. turning specific lat longs into larger polygons capturing such uncertainty).

The authors state that different pseudo-absence models produced "similar results", but provide no means for reviewers to gauge that similarity.

The clarification the authors present that these outputs are depicting suitability for infection, including secondary spread, to my mind is problematic, since this requires mixing different types of data together within the same model. It is therefore unclear to me how the disparate effects of environment (likely influencing primary infection) and human/movement/transmission networks (likely influencing secondary infection) will be disaggregated. Whilst the cross-validation may mitigate the potential clustering that primary and secondary cases have, I'm still not 100% convinced that this differing process can be adequately captured simultaneously. To my mind a more powerful demonstration of difference (or indeed lack of) would be a comparison of primary and secondary data alone.

It was good to see the inclusion of Set 2 and Set 3 results – what was disappointing however was that there was no discussion of the differences this produces (sometimes considerable e.g. India for HPAI). How much of this variation is due to differences in ratios of primary v. secondary cases considered as occurrence records across the different geographies for instance? I found it very interesting to see such a different picture result when the human/host variables were dropped.
