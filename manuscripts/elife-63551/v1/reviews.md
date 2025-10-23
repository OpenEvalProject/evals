# Peer review - Round 1

Editors:
- Marius V Peelen, Radboud University Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63551.sa1](https://doi.org/10.7554/eLife.63551.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper reports the novel finding that fMRI activity patterns in the left TPJ distinguish between stories in which an agent endogenously versus exogenously attends to an object. The experimental design is straightforward and elegant, using tightly-controlled comparisons. The findings suggest that brain regions implicated in theory-of-mind represent a model of another person's attentional state.

Decision letter after peer review:

Thank you for submitting your article "Temporo-Parietal Cortex Involved in Modeling One's Own and Others' Attention" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Michael Frank as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Anthony Atkinson (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Summary:

This fMRI study tested whether theory-of-mind (ToM) regions differentially represent information about endogenous and exogenous attention of the self and of another person. Participants read short passages that described themselves or another person deliberately attending to or having their attention drawn to an object. The main finding was that activity patterns in left TPJ allowed for decoding endogenous vs. exogenous attention (collapsed across self and other). This finding indicates a role for the left TPJ in modelling attentional states.

Revisions for this paper:

Motivation and interpretation:

1) Considering that the study decodes mental states (here: attentional states) in ToM areas, as described in stories, please review work similarly decoding mental states in these regions (e.g., work by Koster-Hale, Saxe). How is your study similar or different from previous work decoding mental states? Do results follow from these previous studies? I also missed a review of (and integration with) the literature on endogenous vs exogenous attention itself (e.g., ventral vs dorsal attention network).

2) It was not clear from the Introduction why you hypothesized that exo vs endo attention should be decodable in TPJ. Is this where eye gaze direction – which appeared to have motivated the study – can be decoded from? The study cited for this hypothesis (Kelly et al., 2014; reanalysed in Igelstrom et al., 2016) showed that univariate activity in TPJ reflected the difficulty of social attribution, which does not obviously lead to the current hypothesis.

3) Does the main finding reflect a model of others' attention or differences in mental state attribution: sentences describing endogenous attention focus the reader more on the mental act of attending and might also induce further mentalizing (e.g., the reader may wonder: "why would he decide to look for that object?"). In exogenous sentences, the focus of the sentence is instead more strongly on the attention-grabbing object (e.g., "the bright red tie"). Can this alternative interpretation be excluded?

4) Searchlight analysis for exogenous v. endogenous attention: Is the cluster centred at -59, -47, 5, labelled left posterior STS (TPJ), really TPJ? It is, after all, squarely in the temporal lobe and some distance (22mm) from the centre of the left TPJ ROI, the latter being in left angular gyrus (areas PGa and PFm). Do you have some independent justification for the labelling of the location of this cluster as TPJ? For example, perhaps it lies within the anterior TPJ (TPJa) subregion identified by Mars et al. (Cerebral Cortex 2012)? The posterior STS area from the searchlight analysis seems to fall into the "gaze-following patch" in the posterior STS as reported by Marquardt et al., 2017. Since this cortical area is not generally considered to be a part of the theory of mind network, the seeming involvement of this area potentially changes the interpretation of the results.

Additional analyses:

5) Please report and compare accuracy and RTs for the response to the probe statement. If either differs between conditions, then that becomes a potential confound for the between condition contrasts in the MVPA analyses, considering that the BOLD response to the story and probe events could not be separated.

6) The TPJ is introduced in the context of theory of mind and social cognition, but it has also been implicated in attentional orienting. Could it be the case that participants simulate such orienting when reading the stories, leading to the above-chance decoding in TPJ? If this is the case, one may similarly expect above-chance decoding in areas that have been implicated in endogenous attention. This should be tested by including dorsal attention network ROIs. Above-chance decoding in such attention regions may inform the interpretation of the TPJ results.

7) Please provide univariate activity estimates, both in the ROIs and in whole-brain contrasts. This may help to interpret the multivariate results.

Further support for main finding:

8) The reported decoding accuracy values are really quite small and close to 50% (chance), especially for the endogenous vs. exogenous and self vs. other contrasts, even those values that are statistically significant. Please report appropriate effect sizes and the confidence intervals around those effect sizes (for all your reported t-tests, not just those that are statistically significant). It would also be informative if you were to include in your graphs the individual subject data (e.g., mean decoding accuracy per subject for each ROI) and/or plots of the effect sizes and their distributions. For more on effect sizes, their CIs and associated plots, I point you to the following sources and the references therein:

https://thenewstatistics.com/itns

https://thenewstatistics.com/itns/2019/05/20/reply-to-lakens-the-correctly-used-p-value-needs-an-effect-size-and-ci/

https://www.estimationstats.com/

9) The authors computed the attentional state decoding separately for "self" and "other". These decoding accuracies did not differ. Please also provide and test the accuracies of self and other separately; this would shed light on the reliability of the main result (which was collapsed across the two conditions) and might also indicate whether the decoding was more reliable (less variable) in self or other.

10) Replicate results in one or multiple additional ToM TPJ ROIs. Reviewers raised two suggestions: 1) Surface-based ROI: the TPJ is a highly anatomically variable cortical region that isn't well approximated by a single volume ROI (see Croxson et al., 2017). There are many surface-based ROIs now available that mitigate the effect of this variability, including ones from the authors' own lab. 2) Use a different meta-analysis: The used meta-analysis defines “theory of mind” solely in terms of false-belief tasks (van Veluw and Chance, 2014), which may not be appropriate for delineating the ROIs and their exact locations in your study. Different types of ToM task reliably activate different brain areas, as well as common ones (mPFC and bilateral TPJ: Molenberghs et al., Neuroscience and Biobehavioral Review 2016). Consider using the results of a different meta-analysis, e.g., one that identifies regions based on the conjunction of multiple types of theory-of-mind tasks (e.g., Mar, Annual Review of Psychology 2011; Molenberghs et al., 2016; Schurz et al., Neuroscience and Biobehavioral Reviews 2014).

11) In previous work (Kelly et al., 2014), the authors were interested in an overlap between attention in self and other. Here, this could be addressed in a cross-decoding analysis, training a classifier on exo vs endo in the "self" stories and testing this on the "other" stories. Above-chance classification in this analysis would strengthen the evidence for lTPJ involvement and would provide additional information that would help interpreting the TPJ findings.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Temporo-Parietal Cortex Involved in Modeling One's Own and Others' Attention" for consideration by eLife. Your article has been reviewed by two peer reviewers, one of whom is a member of our Board of Reviewing Editor, and the evaluation has been overseen by Michael Frank as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Summary:

Both reviewers noted that many of their concerns were addressed. However, they each had one remaining concern that would need to be addressed.

Essential Revisions:

1) Please report and analyze the univariate activity in the ROIs

2) More fully report (in main Results section) and discuss the searchlight results.

Reviewer #1:

The authors have addressed many of my concerns. In particular, the additional TPJ ROIs and the demonstration of self-other cross-decoding increased my confidence in the main finding of attention state decoding in lTPJ.

One comment has not been sufficiently addressed, however: it would be highly relevant and informative to see the average univariate activity for each of the conditions in the 6 original ROIs, plotted in a graph. The endo>exo contrast should be tested, correcting for the 6 ROIs, similar to how the decoding accuracies are tested (i.e., with the same p<0.05 cut-off). This ROI-based univariate analysis is also interesting for other comparisons, e.g. to test whether the social conditions gave higher activity than the non-social condition, as would be expected based on previous work. Thus, please provide a full univariate analysis on average ROI activity.

There is a lot of interesting information in the Supplementary figures (e.g., searchlight, additional ROIs), which will not be visible when viewing or printing pdfs. You could consider moving some of this to the main text, or add panels to existing figures where you include some of this information.

Reviewer #2:

In this revised manuscript, the authors have greatly clarified some key points, most important of which was how well matched the behavior was across all of the conditions. While there is still a potential confound in the social vs. non-social contrast given the difference in reaction time, (a) the confound effects are likely negligible in size, (b) the end result matches the previous literature, and (c) the contrast was only a control analysis and doesn't greatly affect the main point of the paper. However, the handling of the left posterior STS result in the searchlight analysis remains problematic, both in the manuscript and in the author's response.

pSTS response and discussion: The main point of the manuscript is to examine whether known theory of mind areas contain information that differentiates between the endogenous vs. exogenous story conditions. The revised manuscript makes quite clear that the answer is yes, activity in the L TPJ differentiates between the two conditions, albeit with a relatively low decoding accuracy. The fact that multiple versions of the L TPJ ROI produces the same result is particularly reassuring. The spotlight analysis, however, finds that there is potentially more discriminatory information to be found in the posterior STS/middle temporal gyrus, and this is where the manuscript runs into problems.

In the revised manuscript, this result is simply not mentioned, though it clearly has implications for the interpretations of the result as mentioned in the previous round of reviews. In addition, in the response to the reviewers' comments, the authors give a very convoluted and confusing argument based on MNI coordinates that somehow this focus is somehow (a) part of the TPJ and (b) may be a part of the attention-related TPJa as opposed to their TPJp ROI. In the process of saying that the surface projections are misleading, they state that the focus as falling on the STG on the surface projection, when it is really on the MTG. In addition, they base their arguments on MNI coordinates, but MNI coordinates are notoriously inaccurate in comparing results from different studies, so the author's attempts to justify their conclusions using these coordinates falls flat. The authors own volume images very clearly show the focus as being in the STS and not on either the angular gyrus or supramarginal gyrus that Mars, Corbetta, and others have generally shown the TPJp and TPJa to fall on. And even if this focus was in the TPJa, as the authors seem to hint at, they do not discuss the implications of this result.

The authors' defensiveness around this point is frankly puzzling. The searchlight results do not seem to invalidate their main point, only potentially augment it. The fact that the posterior STS (and what seem to be the right FEF and iPCS areas) exhibit higher discriminability between the endo and exo conditions may not be shocking given that the theory of mind areas are likely involved in many operations in this task, whereas the pSTS and right hemisphere areas likely may only be involved in just the imagined attention/sensory processing aspects of the task. It is possible that these areas are "reading out" the differing attentional conditions from the L TPJ. Whatever the explanation may be, the authors seem to be trying to bury this result to shoehorn the results into fitting their a priori model, which is a disservice and misleading to the readers, and needs to be rectified before the manuscript can be published. My recommendation is to at least mention the searchlight results in the main Results section, then add a paragraph to the Discussion discussing the implications of these results. Better yet would be to quantify the discrimination accuracy within each of the foci uncovered in the spotlight analyses.
