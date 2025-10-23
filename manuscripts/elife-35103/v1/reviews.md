# Peer review - Round 1

Editors:
- Bernhard Schmid, University of Zurich Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.35103.037](https://doi.org/10.7554/eLife.35103.037)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Plant diversification contributes to ecological intensification of mega-urban agriculture" for consideration by eLife. Your article has been evaluated by a Senior Editor and three reviewers, one of whom, Bernhard Schmid (Reviewer #1), is a member of our Board of Reviewing Editors.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

As mentioned at the pre-submission stage, we found your study potentially very relevant and interesting for a broad readership because it seems to show that farm-level plant diversity may increase crop protection by encouraging predators of pests such that less chemical pest control will be necessary without yield losses.

However, our problems with the full submission are still the same as with the pre-submission, namely that you do not clearly enough explain the lack of randomization in the 15-year study and you continue to use inappropriate, simple statistics. These problems unfortunately were seen by all reviewers, who in addition point out further issues, in part related to the lack of appropriate analysis. In particular, one reviewer mentions the possibility that the causality between reduced insecticide use and increased predator level could go either direction.

I hope that with the extensive comments of the reviewers you can further improve your manuscript for submission to another journal.

Reviewer #1:

As mentioned at the pre-submission stage, I find this study potentially very relevant and interesting for a broad readership because it shows that farm-level plant diversity may increase crop protection by encouraging predators of pests such that less chemical pest control will be necessary without yield losses.

My problems with the full submission remain, namely that the authors do not clearly enough explain the lack of randomization in the 15-year study (was it their choice not to randomize or was it because they met a "natural experiment" that had been started by others with lack of knowledge about statistical design) and use inappropriate, simple statistics. The first problem may be resolved by explaining in more detail who prepared the study and why it was not randomized. The second problem can be easily resolved by requesting the help of someone who knows how to properly analyze data from such experiments as the authors carried out.

One possible statistical model for the 15-year study is:

y ~ farm type + farm identity within farm type

+ year linear contrast + year as factor

+ farm type x linear year + farm identity x linear year

+ farm type x factorial year

Here "farm identity within farm type" is a random-effects term and must be included in the model to serve as an error term for "farm type" (which is now tested wrongly against the residual). Similarly, "farm identity x linear year" can be used as error term to test "farm type x linear year" if the authors decide to make this probably useful linear contrast.

It seems the authors also used t-tests in which they used the year-averages of y for the two farm types. However, this is not allowed because those are repeated measures of the same set of control and treatment farms. It is like comparing the height of a single tree given nutrients with that of a single control tree, using 15 years of growth data as replicates to test if there are significant effects of nutrients on tree height in more than the two particular tree individuals.

The same problem occurs with the randomized experiment, where the paired-sample t-test is again wrongly applied and the 2-way Anova too simplistic because it ignores "hierarchical structure", i.e. farm identity as random-effects factor. Here a possible statistical model is:

y ~ site + farm type + farm identity within farm type

+ year + farm type x year

Also, several speculative statements in the Discussion could be supported with more sophisticated statistical analysis of the data. In particular, the authors should use the fact that they have evaluated different variables at the same farms to calculate multiple linear regressions or include co-variates in the above models and perhaps integrate these analyses all into a structural equation model, that will allow the authors to explore their hypotheses how the different variables affected each other in a path-analytic diagram. At present these are speculations, even though the authors often present them as facts in the Discussion.

Reviewer #2:

Nian-Feng Wan and colleagues studied the impact of diversified rice cropping on pests, their predators and yield (including economic benefit) in 34 community farms in Shanghai, China. They found that rice fields with ridges planted by soybean and guards surrounding the crop area planted by maize, eggplant and Chinese cabbage, i.e. diversified crop fields, showed reduced pest infestation, higher predator abundance, less pesticide use and occasionally even higher yield. Economically, the diversified crop fields where more beneficial than conventional ones.

The study is based on an impressive dataset, including over 10 years of data from all the community farms, with high temporal and spatial resolution. Furthermore, due to the non-random distribution of the two farming types in Shanghai, the authors also performed a well-designed experiment to test if the results obtained from the long-term farm observations hold under experimentally controlled conditions. I therefore think that this is a very well conducted and extremely well-written manuscript. I enjoyed reading and I think this could be of interest to a wide audience of researchers and stakeholders, and therefore be potentially of high impact.

My main concerns are related to (1) the selection of the farms, (2) the set-up of the diversified farms, and (3) the insecticide use.

1) It is not clear to me how the farms were selected for this study. Some more information on the selection procedure would be highly appreciated. The sampling design is very unbalanced (28 conventional vs. 6 diversified farms) and not well distributed across Shanghai (the 6 diversified farms were all located on Chongming Island whereas none of the 28 conventional farms was located in this suburb). I guess there must be a good reason for this, which would clarify this slightly awkward sampling design.

2) It is unclear to me, how the 6 diversified farms were selected, in particular if these farms were set-up as such through an initiative by those farmers before the observations started or if they were set up specifically for this study through initiative of the researchers. In the latter case, the selection would be highly questionable and could potentially confound most of the results.

3) The results of the insecticide use (in particular the number of sprays) seem awkward, given that farmers "applied pesticides according to pest forecast information offered by the Plant Protection Station". I guess this forecast is the same for all farmers and would therefore suggest the same application regime for all farms. I therefore wonder to what extent the differences in pesticide use are simply caused by the contrasting interests of the different farmer communities. A proper pesticide use study would rather apply similar amounts of pesticide and assess their impact on the pest or reduce the pest to similar amounts and quantify pesticide use. However, in this study it seems that both pesticide use and pest abundance varied among farming types, resulting in difficulties to infer sound conclusions.

Reviewer #3:

The study analyses a long-term dataset of functional arthropod groups of herbivores and predators (herbivores: three different species of specialist herbivores on rice crop; predators: three generalist predators groups, namely ladybird beetles, lacewings and spiders), replicated over multiple farms and several years. In addition, they have data on insecticide use and yield. The core idea is to test whether a diversified farming system leads to an increased top-down control compared to a monoculture situation, followed by a reduced insecticide use and increased yield. They analysed a total of 6 diversified farms and compared it to 28 control farms. One farm was approximately 2 ha in size. The diversified farm consisted of 9 rice fields surrounded by a stripe of soybeans and an adjacent stripe of another crop. Accordingly, the monoculture farms had 9 rice fields which were surrounded by bare ground. I agree with the authors that we have a lack of knowledge on factors driving ecological intensification in urban systems. However, I have a couple of major concerns with the study.

First, the authors claim that the reduced insecticide use on diversified farms was a consequence of the increased top-down control due to increased predator densities. I wonder how they can rule out that it is not the opposite mechanism, namely that there was a reduced insecticide use on the diversified farms and as a consequence there was an increased predator density which then led to increased top-down control? In other words, how can they rule out that the result they find is not simply a consequence of reduced insecticide use but an effect of having multiple crops on a farm (i.e. diversified farm)?

A second major concern is the statistical approach used. First, the data are clearly time-series with nicely oscillating densities indicating lag-effects (Figure 2). In addition to lag-effects, the models should include more variables. For example, for explaining predator densities it would be important to incorporate the prey densities in the model. Second, the model (no matter whether it is a time-series analysis or an ANOVA) needs to incorporate the fact that repeated measures were obtained from the same location. Also, to analyse long-term data with multiple t-tests (for each year one test) is not appropriate. Third, the description of the statistical methods is confusing and incomplete.

A third major concern is that the main conclusion of higher predator control is not inferred from an experiment (for example, by exposing a standardized number of prey to predators) but based on a correlation.

Finally, the Introduction should be more put into a theoretical context, i.e. why and how do diversified farming systems drive biodiversity and ecosystem functioning. Further, the quality of the literature cited should be improved and all literature cited should be included in the reference list, e.g. Tscharntke et al., 2005.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "Plant diversity promotes biocontrol services, reduces insecticide use and increases rice yield in urban agriculture" for further consideration at eLife. Your revised article has been evaluated by Ian Baldwin (Senior editor), a Reviewing editor, and two reviewers.

The Reviewing editor and the reviewer who have seen the previous manuscript agree that the new submission has been improved. It was difficult to find a replacement for one of the previous reviewers but we did get a review of an expert with a similar research area, i.e. with knowledge about the more zoological aspects of your study. This new reviewer has similar concerns to the previous zoological reviewer about lack of detail in the methods description. We hope that you can add all the requested detail in a revision. Please also check the further comments by the Reviewing Editor and the previous reviewer as outlined below.

Reviewing Editor (Reviewer #1):

This resubmission of a previously rejected manuscript has been drastically improved by considering the reviewer comments and obtaining professional statistical help from two additional co-authors. Thus, the main message of the paper, that diverse margins around rice fields can reduce pests, increase predators, reduce insecticide use, marginally increase rice yield and increase economic benefit is now well supported by data and analysis. This is a very important contribution to the new topic of "ecological intensification" in the new field of "urban agriculture".

I have no further major comments. It would be good if co-author Jacob Weiner could have a very careful look at the manuscript before the revised version is uploaded again.

Reviewer #2:

The revised version of this manuscript is clearly improved and, in my opinion, the authors satisfactorily addressed the previous concerns by all the reviewers. I think this is an interesting study on the benefits of diversification in urban agriculture and shows results of an impressive amount of data. The design of the observational study is not perfect, but the authors managed to alleviate my main concerns with this. I therefore have no further major comments.

Reviewer #3:

General comments:

The topic of the paper is very important. The paper basically states that if plants (in fact, other crops) are planted around rice fields on the dams surrounding the fields, this reduces the need to use insecticides.

I concur with the reviews on the first version of the manuscript – the details of the study, in particular the experimental design and the statistical analysis were unclear. I did not assess the statistical analysis in detail.

Main points:

1) I find the title of the paper misleading. The manuscript does not analyse if increasing plant species richness increases biocontrol services etc., because the authors did not analyse diversity in the surroundings of the rice fields. Basically, they show that going away from the monoculture can be beneficial. Thus, the title should be "diversifying agriculture…" or "planting border crops enhances…"

2) Nowhere in the Results are a test statistic or the number of replicates are given.

3) Materials and methods: it is unclear how information on insecticide use was obtained.

4) Materials and methods: unfortunately, I find that still many details are unclear in the revision, see below.

5) Results: the effect on yield is only marginally significant and should not be overstated. Also, the authors provide no mechanism why yield was higher – do the insecticides not work?

Materials and methods:

Subsection “Monitoring sites”: the entire section should be restructured, the design of the diversified fields is described twice (first and third paragraphs), the same is true for other information. Start with the region, then describe the farms, then how rice is grown and then the different treatments.

Subsection “Monitoring sites”, first paragraph: please provide a drawing of a diversified field, and a photograph, how large is the area where other crops are grown.

Subsection “Monitoring sites”, second paragraph: the pest control guidance by SATESC is not known to the reader – what are the insecticides used, what active ingredients etc.?

Subsection “Monitoring sites”, last paragraph: what is a "Z" subplot? Again, use a drawing.

Subsection “Common location experiments”, first paragraph: design unclear: what is the replicate – a block, i.e. three pairs of?

Subsection “Common location experiments”, fourth paragraph etc.: Please provide more detail of the pest assessments: I assume the light kills insects attracted to the light? Were they collected in alcohol? Who identified the species? Why was the interval for the planthopper different if the same lamp in the same field is used? When you say each rice field, do you mean one in each of 9 plots per farm, or just one?

Subsection “Monitoring and sampling methods”, last paragraph: did you only count predators on plants?

Subsection “Common location experiments”, fourth paragraph: what is the correlation between number of pests and number of predators? I assume it is positive? Did you also count lacewing larvae?

I also do not understand how the farmers decided when to spray – you state that there are economic thresholds, so there must be data on how often the threshold was reached? Were the pest data used for the threshold analysis the same that you used?

Figures:

Figure 1: I thought the 28 farms were mono-rice and only 6 diversified, not the other way round?

Figure 2: were pest insects sampled all year round, or only from June onwards? This is not stated in the manuscript. In the first paragraph of the subsection “Monitoring and sampling methods” it states sampling was done May to September (April to September).

Figure 5: 9-14 kg insecticide per hectare is a lot – what is this number referring to, the liquid that is brought to the field? Details on the insecticides should be given and the amount plotted in active ingredient rather than some other unit.
