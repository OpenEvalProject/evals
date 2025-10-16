# Peer review - Round 1

Editors:
- Niel Hens, Hasselt University & University of Antwerp Belgium

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62177.sa1](https://doi.org/10.7554/eLife.62177.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript makes an important point for studies of contagion in both human and animal populations. This paper provides a way of characterising heterogeneity in social systems. Furthermore, the proposed measure of social fluidity can be used to distinguish between different types of animal social systems. Hence, the measure is of relevance for studies of human and animal social networks.

Decision letter after peer review:

Thank you for submitting your article "Social fluidity mobilizes contagion in human and animal populations" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Niel Hens as the Reviewing Editor and Reviewer #3, and the evaluation has been overseen by Miles Davenport as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Jari Saramaki (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Please pay particular attention to the comments by Reviewer #1: items 1 and 2 and Reviewer #3: item 1 which focus on the relevance of this work. The other comments address punctual issues and/or clarifications; they should be looked at carefully and it would be good to organise your reply based on topics rather than a point-by-point reply.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Reviewer #1:

This is a well written paper on an interesting and important topic, characterizing the social contact frequency and network degree into a single measure, social fluidity. The concept is explained and mathematically derived, then applied to an analysis of 50 network data sets spanning 13 human and animal species. The authors then apply that parameter into a mathematical model for infectious disease dynamics to characterize its impact on transmission potential, via R. This is useful in developing understanding of the measure, and demonstrating its applicability in epidemiology. I have only relatively minor suggestions, mostly related to clarifying ideas and terms in the manuscript.

1. The main concern is the treatment of time within the data and fluidity measure. The authors appropriate note this as a limitation in the Discussion section. Because the inputs to fluidity depend on degree and within-node contacts, the measurement time frame for both in each dataset is critical. The authors cite a paper to support the idea that degree scales with the observation length (citation 59), but that is a limited analysis of 3 human networks (2 of which were online convenience samples) that may not apply more broadly. It would be helpful to have more clarification on the range of time frames for data collection across the datasets to understand whether weighted cross-sectional networks are the best modeling approach here (versus modeling dynamic networks of edge formation and dissolution). This may be important in the comparative analysis of different contact types (aggression contacts versus grooming contacts).

2. The authors establish the importance of the fluidity measure for comparative empirical research well, but It would also be helpful to have further clarity on its advantages for modeling over current approaches that might model network structure with two or more parameters. What are the broader benefits of this approach?

3. It was not clear how the contact types (aggression versus grooming, eg) were defined. Were these a component of the secondary data, or did the current authors use a classification scheme? Some further details on the measurement of the data would be helpful.

4. What are the implications of treating the system as closed and the network consisting only of non-isolates on the empirical comparisons and the epidemic modeling? These are assumptions required by the data, but not always realistic and could have a meaningful impact on the outcomes (e.g., non-differential misclassification for aggression contacts that may change the network structure, or include many isolates). The importance of these assumptions may depend on the measurement timeframe (i.e., less important if short observations).

Reviewer #2:

This manuscript makes an important point for studies of contagion in both human and animal populations: the heterogeneity of contact frequencies matters a lot. The individual-level heterogeneity of weights/contact frequencies in egocentric networks is nicely captured by the concept of social fluidity and the model parametrised by $\phi$ whose fitted values clearly differ for datasets from different species (Figure 2). Finally, the spreading model shows that $\phi$ has clear effects on R0 – the effect of ego-network weight heterogeneity on disease transmission is something that I have hypothesised myself as well, so I congratulate the authors for getting there first!

In my view, this paper makes several important contributions: in addition to the context of contagious disease, it provides a way of characterising heterogeneity in social systems and shows that it even works for distinguishing human contact networks under different circumstances (the Sociopatterns data sets). Furthermore, the proposed measure of social fluidity can be used to distinguish between different types of animal social systems. Hence, the measure is of relevance for studies of human and animal social networks.

As the science is solid, the results are important, and the manuscript is well and clearly written, I recommend publishing it, after some fairly straightforward clarifications/modifications.

1) Would it be possible to justify the choice of the power-law form for Equation (2)? And would the results be sensitive to this choice – would using something like a log-normal or stretched exp yield similar results? (Intuitively, my expectation is that the exact form of the distribution should not matter too much as N is fairly low in all studied cases, so whatever is mathematically the most convenient distribution should be fine).

2) page 3, bottom left column: "There is no significant correlation between the mean number of interactions per individual (s) and social fluidity…" Has r^2 been calculated over all datasets or separately for one species over their respective data sets?

"…which implies that sampling bias does not affect the estimation of social fluidity". How this is to be interpreted depends on the answer to the above, but I am not certain if one can make this statement, at least if the correlation is over all species/datasets. I would think that it is difficult to escape some sampling bias (as for most network measures…), unless one has several samples of different size for the same species under the same circumstances, and can show in those samples that $\phi$ doesn't depend on N.

"Similarly, network size does not correlate with $\phi$…" Again, is the correlation over all species?

3) In the subsection "Numerical validation using empirical networks" it is stated that "Since a large edge weight implies a high frequency of repeated interactions, networks with a higher mean weight tend to have lower basic reproductive number. Furthermore, variability in the distribution of weights…"

Would the variability not be a requirement for a higher mean weight leading to lower R0, so that the cause of the lower R0 is the combination of higher weights and high variability? If one considers two networks with uniform weights that are otherwise identical but one has twice the mean weight, would that one not have a *higher* R0?

4) Discussion: "We see, for example, how the relationship between mixing and disease risk scales with population density. For social systems that have high values of social fluidity, $R_0^\phi$ is highly sensitive to changes in N…" Is N conceptually the same as population density? Would, under the network paradigm, the average degree be a better proxy of population density?

Reviewer #3:

The authors define the concept of social fluidity to better define how social behaviour influences contagion process in human and animal populations. Whereas I believe the manuscript is well written, its current version requires a few clarifications.

1. I think it's important to mention that the concept of social fluidity hasn't been tested in relation to infectious disease data. Does it provide a good/better fit to infectious disease data as compared to assumptions of frequency and density dependent mass action etc.

2. In the social behavior model: the authors use frequency for the edge weight; should weighing not be done on the basis of risk assessment of these interactions?

3. Please better motivate the use of the power-law form in equation (2). Have the authors considered alternatives?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Social fluidity mobilizes contagion in human and animal populations" for further consideration by eLife. Your revised article has been evaluated by Miles Davenport (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

– In terms of the authors' reply on 'Was this relationship linear … ': Given that a Pearson correlation coefficient assumes linearity holds, one cannot measure strength of association in case of non-linearity. Please verify or use an alternative measure (see e.g. https://www.pnas.org/content/111/9/3354).

– The authors use 100 bootstraps to quantify the uncertainty of phi; this seems small to me; why not use 1000 bootstraps (as well as assessing whether or not estimates of 5% and 95% percentiles are stable for that number)?
