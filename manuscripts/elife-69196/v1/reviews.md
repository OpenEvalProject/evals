# Peer review - Round 1

Editors:
- Christian Rutz, University of St Andrews United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69196.sa1](https://doi.org/10.7554/eLife.69196.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This article will be of interest to behavioural ecologists studying aggression, within-group conflict, communication, and the use of social information. The study elegantly combines well-designed experiments with field observations to investigate the effects of within-group conflict on social behaviour. Specifically, it expands our understanding of social dynamics in group-living species by providing evidence that bystanders of within-group conflict may play a role in maintaining group cohesion. The findings provide a valuable contribution, and contrast, to existing work in this field.

Decision letter after peer review:

Thank you for submitting your article "Experimental evidence for delayed post-conflict management behaviour in wild dwarf mongooses" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Safi Darden as the Reviewing Editor and Christian Rutz as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Melanie Mirville (Reviewer #1).

The reviewers and editors have discussed their evaluations with one another, to reach a consensus recommendation. While we normally combine reviewer feedback into a consolidated set of essential revision requests, we have decided on this occasion to provide the reviewers' full reports below. In addition to addressing their detailed and constructive comments, please consider the following points when revising your article:

(1) We felt that an evaluation of the effects of increased vigilance on foraging success (satiation) would help support the conclusions drawn. If these additional analyses are impossible or impractical at this stage, we suggest acknowledging this and toning down language accordingly.

(2) We believe that terminology can be refined in places. For example, the temporal scale mentioned in the abstract and introduction is somewhat unclear – what exactly is the "delay" and what is its biological significance/justification? For example, what is known about physiological stress responses in this species (e.g., peak response and recovery time)? Furthermore, it may be more helpful to use the word "target", as opposed to "victim", as it is more neutral – we don't know anything about the psychology of the individuals involved in aggressive interactions.

(3) Please add more detail about the recording and playback equipment used (e.g., frequency response range) and provide information on whether there has been a comparison of stimulus spectrum and spectrum following playback (i.e., at 1 m), as it is important to demonstrate that these match, especially for the acoustic features thought to be biologically important.

(4) Please note that eLife has recently adopted the STRANGE framework, to help improve reporting standards and reproducibility in animal behaviour research. In your revision, please consider scope for sampling biases and potential limitations to the generalizability of your findings:

https://reviewer.elifesciences.org/author-guide/journal-policies

https://doi.org/10.1038/d41586-020-01751-5

Reviewer #1 (Recommendations for the authors):

Overall, the research is novel and presents unique results of interest to those studying social species. I believe that the manuscript would benefit greatly from including more information on the importance of interactions between individuals specific to mongooses to highlight the significance of changes in these behaviours, e.g. to set up why changes in grooming is important, what function does grooming have in mongooses specifically? why observe only bystanders in experiment 1, etc. I think the research is meaningful, but the overall cohesion of information presented in the introduction, results and discussion could be improved to increase the significance of this particular study.

Methods throughout – use consistent measurement terms, i.e. seconds, OR s, OR sec, same for minutes, hours, etc. Same with the use of numbers- spelled or use of numeric form.

Line 48 – is anxiety an anthropomorphised word? Is there another way of saying fear of conflict having occurred or for the potential to occur?

Line 51, 70, 89, 287 – perhaps specify post intragroup conflict throughout, as post-conflict could include intergroup which does have literature on longer-term outcomes on intragroup behaviour in social species.

Line 58 – suggest could be written more clearly, for example "were more likely to offer support in aggressive interactions to individuals they had groomed earlier, evidenced by differential movement towards grunt call playbacks during conflict."

Line 84 – what kind of valuable information i.e. specify the possible function of these calls?

Line 89 – suggest remove experimentally.

Line 103 – can you explain how vocalisations can act as reward to individuals?

Line 104 – can you explain the importance behind testing behaviour in only bystanders/subordinates, and not individuals involved in the conflict? Since this is your main hypothesis, I think more build up for the importance of this specific question is needed, i.e. highlight why we should know more about the effects of intragroup conflict on bystanders and their behaviour in the aftermath, what significance does this have?

Line 111, 119: prior to this, you mainly mention testing the delayed behavioural outcomes of intragroup conflict on individuals. I would suggest adding a results summary paragraph followed by subheadings with more specific results pertaining to each hypothesis, i.e. subheading 1 "experiment 1: "testing immediate behaviour outcomes of intragroup conflict on bystanders" lines 109-168 and subheading 2 "experiment 2: "testing delayed behaviour outcomes of intragroup conflict on bystanders" lines 168 onwards.

Line 125/420 – what is the function of a close call, can you explain how this is non-aggressive?

Line 160 – what is grooming at a distance? Did you measure this?

Line 195 – did you test grooming in those involved (i.e. the individuals used for the simulated vocalisations) vs bystanders?

Line 238, 243, 272 – change wording 'proportion of time' to 'time'.

Lines 241-248 – This can be written more succinct to make result clearer, suggest you combine the results for conflict and control evenings, i.e. 'less grooming among individuals on conflict evenings (evidenced by less time, state results, and fewer individuals, state results).

Line 253-261, 279-283 – move to discussion.

Line 295 – how did you decide that a conflict was not resolved?

Line 341 – new paragraph starting 'Alternatively…'

Line 349 – it may be cognitively demanding, but it also may not serve as much purpose to identify subordinate responses to aggressors. In other words, there may be a higher selective pressure to discriminate aggressive vocalisations due to the importance on individual relationships/social status, rather than subordinate responses.

Lines 359-364 – these statements are really important to highlight the significance of your findings, and I would suggest spending more time discussing these in your discussion to highlight the originality of your research.

Lines 365-368 – this statement about cognitive ability and intelligence comes somewhat out of the blue and may not be the best statement to end your article if you are intending to summarise the significance of this particular research, unless the link between post-conflict behaviour and social animal intelligence is discussed prior.

Reviewer #2 (Recommendations for the authors):

1. The modelling framework used to analyse the proportion of time grooming and the rate of grooming in linear models is not the most appropriate given the distribution of the data. Neither of these variables are normally distributed by definition (proportion time is bounded by 0 and 1, and a rate is a count of occurrences per unit time), and so log-transforming them is a bit like crowbarring them into a normal distribution. A more appropriate model to use for the proportion time data is one with a β error distribution which accommodates bounded variables (e.g. Smithson and Verkuilen 2006 https://doi.org/10.1037/1082-989X.11.1.54). Similarly, for the rate of grooming, a more appropriate model is one with a Poisson error structure that includes an offset (use 'offset' in R) of the exposure time (the time available to groom, log transformed) as an additional fixed effect. (See Crawley MJ. 2007. The R book, and numerous online forums).

2. Could means +/- SE for the treatment and control data be included in the results for Wilcoxon tests so that the reader can more easily evaluate the strength of the effect. Similarly, although you have provided output from linear models that includes effect estimates in a table, could you also include model estimates +/- SE in text with results, rather than just a chi-sq and p-value?

3. Can more information be provided on the Monte Carlo resampling method employed to generate P-values? This seems like an important part of analyses and subsequent interpretation of data (P-values are used to determine significance) and so more detail is needed on how this was performed.

4. It is not clear why you refer to using Akaike Information Criteria to evaluate fixed effects (L546) when there is no reporting of any AIC values for full and null models. Throughout the study, P-values are used to determine the significance of effects and so to also use AIC values conflates two very distinct statistical approaches. Can you remove reference to AIC values to avoid confusion?

5. L550 – you are testing a difference in the probability of grooming rather than 'number of adults that participated in grooming'?

6. It would help the reader to include short titles on panels of figures to quickly convey what the figure shows (or provide more informative y-axes titles). Currently some panels in the same plot are exactly the same in terms of axes (e.g. figure 5) and so it is not clear on first look what each panel shows and how it is different from others.

7. Was the focal individual in natural observations always unable to see the displacement (natural observations) or see the aggressor/victim in the playback (experiment 1)? Similarly, was the aggressor/victim in earshot when the playback of their calls was made (experiment 2)? Can you convince the reader a little more than your statement at L294-297 that hearing an interaction that does not match what an individual sees, or hearing yourself in an interaction you know you weren't involved in, does not change the behaviour of bystanders or simulated aggressors/victims.

8. The use of language like 'strong' and 'compelling' evidence (e.g. L287, L236) is a little overstated given the small sample sizes in the study; effects and p-values are likely to be very sensitive to sample size.

9. A little more information on why vigilance was measured as a behavioural response to within-group conflict would be welcome. The set up for measuring affiliative behaviour (grooming) was much clearer but why vigilance was used was less so. Does vigilance indicate being wary of conspecifics? How could you tease apart vigilance for predators versus that for conspecifics? Vigilance was also not measured as a delayed response as grooming was. Why was this? If because dwarf mongooses are very rarely vigilant for conspecifics at their sleeping refuge before they go down for the night, why was grooming measured during foraging in experiment 1 when it was noted that mongooses rarely groom in this context? Also, the increased vigilance result is comparatively neglected in the discussion of results compared to that of grooming, which feels unbalanced given that it is the primary result from the first set of natural observations and experiments.
