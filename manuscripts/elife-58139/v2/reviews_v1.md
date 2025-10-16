# Peer review - Round 1

Editors:
- Ammie K Kalan, Max Planck Institute for Evolutionary Anthropology Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58139.sa1](https://doi.org/10.7554/eLife.58139.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study presents an important contribution to comparative animal cognition research. Using an experimental paradigm that was originally used to test prosociality in primates, this study tests prosociality across eight species of corvids. Of particular interest is the finding that the species-specific traits of cooperative breeding and colonial nesting effect prosocial behavioural tendencies but do so to varying degrees for males and females. This work therefore provides valuable insight into the potential evolutionary pathways and drivers of prosociality.

Decision letter after peer review:

Thank you for submitting your article "Sex-specific effects of cooperative breeding and colonial nesting on prosociality in corvids" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Reviewing Editor and Detlef Weigel as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional analyses are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

The authors present an interesting study on the prosocial tendencies of eight bird species within the Corvid family, using species-specific predictors of colonial nesting and cooperative breeding. Importantly, the study replicates an experimental paradigm used to test prosociality in several species of primates. The authors show that cooperative breeding and colonial nesting affect prosocial behaviors, with interesting interactions by sex, apparently driven by female cooperative breeders and male colonial nesters.

Essential revisions:

The reviewers all found the comparative approach to be worthwhile and the paper to be well written and easy to follow for the most part, but all three had major concerns with the analyses. There were also some concerns with the experimental procedure, which might be addressed by simply modifying or adding analyses. The authors should also include a file with all the R code used to run and interpret the models and all other analyses (e.g, Pielou's J), as well as the source files for figures when submitting a revision.

1) It is not clear why the authors chose to apply different criteria for different parts of the analyses. In particular, passing the last criteria (test vs controls) appears to be crucial to establish prosociality in these species (and actually is a test in itself). We agree with the authors that there are reasons why birds might not have passed (e.g. as discussed lacking cooperation by receiving birds), but at the very least, we would like see the results of an analysis for just the birds that passed the criterion and how these results compare to the presented ones (as the authors did for percentage of provided food). Of course, this will drastically reduce sample size but such an analysis would be especially important considering the percentage of birds passing the criteria was high in the cooperatively breeding and/or colonial species.

2) Why were test and control sessions conducted on alternating days (rather than pseudo-randomly distributing them throughout the session, or even better on a trial level)? With the current design we are concerned that the data is not independent within a day. (The same applies, albeit to a lesser degree as it is only the habituation phase to phase I). Given that this can't be changed anymore, can it be accounted for in the models?

3) Many of the effects observed for each species are driven by very few individuals, which casts doubt on how well the results reflect true species generalizations rather than individual personalities. For example, the species where more than one group could be tested showed a lot of variation, presumably due to the presence of particular individuals. Could the authors (1) clarify in the manuscript that for all models/analyses that only one data point per individual was used? (2) Could the authors provide more discussion about possible inter-individual differences and how this could effect their results?

4) Why was a phylogenetic generalized linear mixed model (pglmm) not used, especially considering the variation in relatedness among the 8 species (seen in Figure 2)? Please provide clear justification or else re-run using a pglmm framework.

5) The model selection approach is problematic for a number of reasons. Firstly, the candidate set of models was not clear (this should be included clearly with the code for the paper) and where did the intercept only model fall relative to the others when ranked by AIC? This needs to be explicitly discussed in the Results section. Second, the p values being reported (e.g., Table 2) are not understandable, are they from two different models? An average? Why are you reporting them at all and not instead model-weighted averages (e.g., summed akaike weights) of the different predictors, including group size, considering you are using an information theory-based approach with AIC? With relatively few predictors and strong theoretical support for each, such as in this study, selecting the best models (delta AIC <2) seems arbitrary and leads to removing potentially important variables, like group size, based on this threshold (note Burnham et al., 2010 also note ' Models where Δ is in the 2-7 range have some support and should rarely be dismissed'). A more parsimonious approach is to use a model set and model weighted averages of coefficients and SEs and Akaike weights to assess covariate support (see Mundry, 2011 and Burnham et al., 2011 for best practices associated with multimodel inference and how to report results).

6) Table 2 of the main results is somewhat misleading since reporting coefficients and p values of main effects when their interaction is significant are problematic (see for example Brambor, Clark and Golder, 2006). It is fine to demonstrate via plotting the unconditional effects of the two factors, but Table 2 on its own is confusing since the interaction tells us that the main effects are conditional upon one another.

7) The Introduction suggests sex ratio of groups may be an important predictor of prosocial tendencies in some species. Considering that sex ratio varies among the social groups of birds tested, this should be included as a predictor in the models. Similarly, is there any reason to suspect variation according to age, i.e., juveniles and adults? If so, should this not also be included?

8) The sex-specific models with only 25/26 data points suggests these models may be incredibly unstable, and there is no mention of group ID or species being included. If these terms were dropped from these models this should have been tested as you did with the full data set but we could not find this mentioned anywhere. Moreover, can you provide some measure of how robust and stable the results of the sex-specific models are? For example, check how much variation there is in your coefficients if one species is removed at a time? A similar exercise would also add credibility to your results for the full data set.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Sex-specific effects of cooperative breeding and colonial nesting on prosociality in corvids" for further consideration by eLife. Your revised article has been evaluated by Detlef Weigel (Senior Editor) and a Reviewing Editor.

The manuscript has been significantly improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) Regarding our previous major concern, point #2, we understand that day is confounded with test condition, but could the authors not simply add day as a random effect (intercept only, no slopes needed to keep the model simple)? We would like the authors to consider this approach if possible, to fit.

2) Regarding the model stability check for the single sex models and for the full model, we suggest the authors add a short description of how they did this to the section titled 'Data analysis' and when reporting the results, especially for the single sex models, explicitly state in the manuscript that the female model is less robust/stable (similar to what you wrote in your response) and that in general the single sex model results are very preliminary due to the low sample size. More data are definitely needed here.

3) We appreciate the authors checking whether they obtained similar results when using a cut off of AIC<7 for 'top models'. We would suggest that for transparency, the authors also add that they did this additional check (subsection “Data Analysis”) and add Table R1 (in the response letter) as a supplementary table. Since the results do differ slightly, we think it is worthwhile to provide the reader with all possible information.
