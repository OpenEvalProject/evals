# Peer review - Round 1

Editors:
- Deborah M Gordon, Stanford University United States

Reviewers:
- James D Crall, Harvard University United States
- Jacob Davidson, Max Planck Institute of Ornithology United States

## Review text

DOI: [10.7554/eLife.38473.026](https://doi.org/10.7554/eLife.38473.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Ant colonies maintain social homeostasis in the face of decreased density" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Ian Baldwin as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: James D Crall (Reviewer #1); Jacob Davidson (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This reports on how interaction networks in ants depend on spatial patterns of movement and local density.

Essential revisions:

The manuscript reports on an impressive amount of data and asks interesting questions. The reviewers raise many issues with statistical analysis and interpretation of the results. A revised version should respond to all of these questions. Without further clarification it is not possible to evaluate the novelty and broad interest of the results.

Reviewer #1:

This paper presents a rich and interesting dataset on the location and movements of uniquely identified ants (Camponotus pennsylvanicus) within chambers of varying sizes to investigate the regulation of social interactions as a function of density. The subject is an interesting and timely one, and I think the results will be of broad interest to the social insect and collective behavior communities. Making such a large, manually annotated dataset available on ant movements and locations has the potential to also be an important resource.

I do, however, think there are important points that need to be addressed, that would help strengthen the manuscript, and clarify its interpretation. Perhaps most importantly, I think the authors need to do some work to clarify the hypothesis they are testing, and how their results support/refute this hypothesis. Specifically, the authors find that interaction rate doesn't decrease when density (defined as chamber size) increases. This could result from either (a) a functional change in local density (i.e., interaction rates are a product of local density, but local density is actively regulated by the ants), or (b) a change in interaction behavior that is independent of local, realized density. I don't think the current Results and discussion section clearly distinguishes between these possibilities, but the data collected here offer an opportunity for a more explicit test.

Specifically, I would suggest that the authors use their rich dataset to generate some quantitative estimates of local density, as opposed to overall density within the chambers. This could provide a more explicit test of whether ants are maintaining a consistent local density after the increase in chamber size. There are plenty of approaches for this, including spatial/temporal binning, etc. Gordon et al., 1993, which the authors cite, has some good examples of such an approach (including local v overall interaction rate).

It's also a bit unclear to me what the potential surface modeling (vs. just the intermediate step of motility surface modeling), adds to the paper's conclusions. It seems like the motility surfaces (e.g., in Figure 1—figure supplement 2) provide sufficient support for most of the conclusions in the Results and discussion section (e.g. that ants move fast through the middle chambers, which are lower density and used primarily for transit). In addition, the estimated potential surfaces from this modeling approach appear to show significant variation, both locally within chambers, and between colonies (Figure 1—figure supplement 3), suggesting this approach might be prone to errors and/or sensitive to noise. If there are key conclusions that can only be supported by the potential surface modeling approach, I think these need to be clarified.

Finally, most of the framing of the paper is around a lack of expected change (i.e. we'd expect decreased density to reduce social interaction rate, but we don't find that). The authors in fact found evidence that there was a significant shift after chamber rearrangement, just that this was an increase in interaction rate with decreased density. I think this result needs a bit more interpretation, as well as addressing the sources of variation in interaction rate between colonies driving this pattern.

Reviewer #2:

This study impresses primarily in its scope, and the labour required to generate its conclusions. I think that the results may be of general interest to ant and social insect researchers, but do not consider myself an interaction network specialist.

Specific comments:

Results and discussion section: while the labour involved in this is impressive, it would be good to highlight the use of machine vision and machine learning approaches to this kind of study, at least to inform others lest they believe the only way of generating such datasets is manually! Markerless techniques exist, e.g. idtracker.ai (Polavieja Lab), and with markers such as the QR codes used in the present study, e.g. Mersch et al., (cited); it would be good to discuss why automated approaches were not used or, if they were tried, why they failed.

Results and discussion section: for a possible comparator dataset for this hypothesis, on involvement in an emigration task (T. albipennis) see Richardson et al., (2018).

Results and discussion section: is it possible that trophallaxis interaction rates not increasing with density is explainable by identified cliques of ants not finding each other in the crowd?

Results and discussion section: please provide a reference for claimed dyadic nature of trophallaxis.

Subsection “Classification algorithms for the spatial groups”: I found the purpose of the 'bootleg' networks, and their nature, quite opaque – please provide more explanation both of the what and the why.

Subsection “Data availability”: is there a reason why some code is available from the author on request while the remainder is on a repository? It would seem best practice to put all the code there.

Reviewer #3:

In this work the authors analyze the movement and trophallaxis interactions of ants after manipulating the density by introducing extra chambers into the nest. The authors find that the ants adjust their movement to maintain a similar local density and trophallaxis rates following the nest restructuring. Before the change in nest structure, the ants in the nest separated into two groups, and after the change the ants maintained the same group membership structure. I think the results are interesting and should be published. I have some comments of additional points to improve the discussion in the manuscript, and several technical points that need to be addressed prior to publication.

Technical points:

- Subsection “Classification algorithms for the spatial groups”, bootleg. The technical terms in this section are incorrect. I think the authors meant to refer to the "bootstrap" method, instead of the "bootleg" method. However, the procedure they describe is not bootstrapping – it is a method to ask how sensitive the results of the community detection algorithm are to added noise/uncertainty. The procedure they describe is a reasonable way to do this – but it needs to be referred to appropriately.

- Subsection “Stochastic differential equation modeling of tracking data”, SDE coefficients. The authors say "..allow c(x) to vary as a motility function that controls absolute speed." From the equation, this is incorrect – c(x) controls the magnitude of random changes in speed, while mu(x) controls the (spatially-varying) average speed.

Discussion and clarification

- Density and interactions, Results and discussion section. The authors downplay the relationship between spatial movement/density and interactions. Ants cannot interact unless they are close to each other, so this is a clear constraint on possible interactions. Thus, "interaction assortivity" based on spatial locations should be expected, with anything else being surprising. The authors should mention this when they introduce the assortivity measures. Davidson and Gordon, 2017 deals with the distinction between local density and interaction – this could be an interesting comparison for future work with this dataset.

- Mechanisms of maintaining interactions rates with decreased density, Results and discussion section. The authors suggest two possible mechanisms – physiological limitations, and change in spatial structure. The authors confuse density and interaction and implicitly refer to the them as the same thing. There is no evidence otherwise, so I think this is correct. However, it should be made explicit, so that the assumptions are transparent. E.g. "..ants indeed formed spatially separated clusters to maintain an approximately constant local density, such that trophallaxis rates were approximately the same."

- Trophallaxis versus antennal contact. In Gordon et al., 1993, antennal contact is considered when the density is changed. In this paper, the authors analyze trophallaxis events. Did the tracking distinguish events where only antennal contact and not trophallaxis (transfer of liquids) occurred? This might be a point specific to this species of ants. It would be good to mention/clarify this distinction so that previous work can be compared. Also, would the same trends be seen if the analysis used just antennal contact, instead of trophallaxis?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Ant colonies maintain social homeostasis in the face of decreased density" for further consideration at eLife. Your revised article has been favorably evaluated by Ian Baldwin (Senior Editor), a Reviewing Editor, and three reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance. Both reviewers 1 and 3 suggest further analyses to test whether the rate of trophallaxis depends on local density. They suggest different approaches. A revised version should include some way of addressing these concerns.

Reviewer #1:

Overall, I think the authors have made substantial improvements to the manuscript; in addition to small changes throughout, the authors have done a good job of highlighting the key questions of the manuscript, and how they're answered by these experiments.

However, I think this clarity also highlights some concerns about the specific, central claims of the paper that need to be addressed. In particular, I've got concerns about the data supporting both of the major claims in the introduction. Specifically, the authors now claim that local density (in addition to global density) is reduced in the "low density" treatment. I thank the authors for including the new data, which is very helpful for interpreting results. The authors do a good job of addressing potential temporal autocorrelation in these data, but I don't think a lack of temporal auto-correlation is sufficient evidence for observations from a single colony to be considered independent, since temporal auto-correlation isn't the only source of bias/correlation in these data. As in the analyses of interaction rate (see comments below), I also think it's important to include treatment*colony interactions in statistical models, given that there are clear systematic differences between colonies for other metrics.

Given the rich dataset the authors have collected, I think there may be an alternative analysis that more explicitly addresses what I interpret as the authors' key claim; that ants behaviorally regulate the rate of trophallaxis independent of changes in local density. Specifically, I think the authors could (a) use their data to estimate the probability of a trophallaxis event as a function of pairwise distance between ants (possibly as a logistic regression?), and which should essentially by definition have a strong relationship, and then (b) test whether this relationship differs between density treatments. This would be an explicit test of the hypothesis that trophallaxis behavior varies independent of spatial proximity/local density, and I believe would provide a more convincing test of the authors' key hypotheses.

Reviewer #2:

I think the authors have done a reasonably thorough job of revising the manuscript in light of the three reviewers' comments. However, I feel tracking is very likely to work well for with a state-of-the-art technique for these group sizes, especially given the insects are marked; e.g. idTracker.ai should be cited so for possible validation of these results in the future, and considered by the authors for future work – that group is going as far as automating analysis of interaction networks (http://idtracker.ai/). From my perspective, apart from this issue, I am happy to endorse publication.

Reviewer #3:

Although the authors have addressed many of the issues brought up with the first comments, there are still several remaining points that I feel need to be addressed before publication.

- The authors added the calculation of local density, which I think is a very interesting comparison. However, I feel that the paper currently does not include enough evidence to claim that "ants maintain trophollaxis rates by changing behavior, not by maintaining local density". I would like to see (1) the distribution of local density for individual ants, perhaps according to spatial group, not just the average over the whole group, (2) the correlation between an individual's local density and its trophollaxis rate (e.g. plotting local density versus trophollaxis rate for individual ants), and (3) the results when difference distance cutoffs (both higher and lower than 15mm) are used in the calculation. Regarding (1), because it is mentioned that most ants stay either on one side or the other side, with only a few going back and forth, I might expect that the ants going back and forth are the "density outliers" which bring down the average in the low density treatment case, whereas ants that stay in either area actually have about the same local density in the high vs low density cases. Calculating group local density using the median, and comparing it the current results that use a mean, is another way to see if this may be true. Whether ants change their behavior can be further investigated by (2), because if ants that experience lower local densities change their behavior to maintain trophollaxis rates, there should be no correlation between an ant's average local density and its average trophollaxis rate. Then, to get an idea if the overall interpretation depends on the function used to define local density, it will strengthen the results if the local density calculation is done with different radii. Or if this is not done, the authors should provide justification for the why 15mm is used, and an argument for why the results would not be expected to change if a different distance cutoff, or function for density measurement, is used.

- About the potential surfaces, e.g. Figure 1E. I agree with reviewer 1's comments about the potential surfaces, and that the main conclusions about movement can be obtained more clearly from the motility surface (e.g. Figure 1D). I find the potential surface confusing to look at, because as the authors mention, what it is actually showing is the difference between ants going one direction versus the other direction. I think the trend of moving faster in the middle area is shown well by the motility, and that the potential surface should either be omitted, or calculated separately depending on the departure location (i.e. to calculate two surfaces, one for ants starting from the left side, and one for ants starting from the right side). Without the separation, it seems like because direction and acceleration/deceleration are expected to have opposite trends if going left-right versus right-left, it is not clear to me for example if a moderate value of the potential surface for acceleration/deceleration is representative of actual motion, or is due to averaging. Or if I am interpreting this wrong, please let me know.

- Regarding the spatial groups. There are two or three spatial groups identified by the community detection algorithm, and Figure 2—figure supplement 1 shows nicely how these correspond to the location of trophollaxis locations. However, since the spatial groups are defined by the history of the ants motion, not by the trophollaxis events, it would be informative to show the spatial movement signature associated with each group. For example, something like Figure 4A of Mersch et al., 2013. Without this, I am tempted to use the Figure 2—figure supplement 3 to understand how the different groups have different spatial signatures, but this would actually be incorrect.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Ant colonies maintain social homeostasis in the face of decreased density" for further consideration at eLife. Your revised article has been favorably evaluated by Ian Baldwin (Senior Editor), a Reviewing Editor, and three reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Reviewer #1:

Overall, I think the additional data and revisions provide and interesting new insight, which will be helpful for interpretation of the paper's key results. However, I think there are a few key points that still need to be addressed, outlined below.

Abstract: The language here suggests that the main finding is a lack of change in interaction rate that is resilient to changes in density. But there's quite strong support for changes in interaction rate, even if in an unexpected direction (either an overall decrease, or divergent effects across colonies, depending on the statistical interpretation, discussed below).

Results and discussion section: I think these new data are really interesting. Am I right that this new analysis, by showing a significant main effect of treatment (Table 2), provides direct support for the idea that the relationship between local density and interaction rate differs between density treatments (suggesting a change in behavior independent of density)? If that interpretation is correct, I think this should be highlighted more clearly in this section, since it provides direct support for a central claim.

Figure 3: I think this figure caption should be expanded to improve interpretability. Are these values derived from the same model estimates in Table 2? If so, specify this in the figure caption. Also, either include units or an expanded discussion of how to interpret the axes.

Table 1: In general, my understanding is that it's not really kosher to interpret overall main effects (e.g., "treatment" or "colony" separately) in the presence of a significant interaction (treatment*colony). In the Results and discussion section (and repeated in the Abstract), the authors suggest that these data support a significant main effect (reduction of interaction rate in high density). Beyond the statistical details, the data Figure 2C clearly suggest substantial differences between colonies in the effect of densities. In light of this, it might be best to clarify why the claim that there is a coherent overall reduction in trophallaxis is justified given these divergent trends across colonies, or remove that claim from the manuscript.

Reviewer #2:

I remain satisfied with the manuscript, but note that the other reviewers have concerns.

Reviewer #3:

I am happy to see that the authors have included an analysis of how trophollaxis rates depend on local density. I think the newly included analysis is a very interesting and important addition to the paper, and is needed to support the claim about regulating trophollaxis rates dependent on density. However, from the methods, I could not follow exactly how this analysis was done. Before publishing, more detail needs to be included in the newly added subsection "Comparing ant trophallaxis rates with local density using different radii", so that the methods can be reproduced.

Here are some questions and my description of how I understood the methods:

Where does the 'inhomogeneous Poisson point process' come into the calculation? I agree that this is a good starting model of trophollaxis events, but I couldn't follow how the calculations were done. The authors say pairs of ants were considered, at times when a neighboring ant (call it N, for neighbor), came into 20 mm of a focal ant (call if F). Then they measured local density around different radii of F, mentioning that they have second-to-second calculations for the different radii. The only way I could think of how a calculation with this description to proceed is to consider all trophollaxis events between F and N, measure the time (call it T_init) from when N reached 20mm of F to when the trophollaxis event occurred, and then to consider the "initiation rate" as 1/T_init. Then, the average local density at the different radii could be used in a regression model to predict initiation rate, given colony, treatment, and local density measurements. Is this what was done? If so, then how does the calculation "For each second in which they were within this proximity to each other," (subsection “Quantitative estimate of local density”), come into play? Wouldn't an average of this local density in the time proceeding the trophollaxis event need to be used? And where does the Poisson process model come into the analysis?

Also, was the neighbor ant N included in the local density counts at the different radii? Since by definition N needs to be close (<5mm) to F in order to perform trophollaxis, it seems more consistent to not include N in the density counts, to avoid any artifacts due to spatial constraints. I think this is what was done, as described (subsection “Quantitative estimate of local density”, "…number of additional ants..")

If the calculation was indeed done as I described above, I would naiively always expect negative effects of density at all radii, due to crowding, i.e. if there are fewer ants around then F and N will find each other and initiate a trophollaxis event quicker. So, then the positive effect of having ants in the "close by" radius of 5mm, which is shown in the paper now, is indeed interesting.
