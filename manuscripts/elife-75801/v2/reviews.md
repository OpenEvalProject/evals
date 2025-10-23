# Peer review - Round 1

Editors:
- Taraz Lee, https://ror.org/00jmfr291 University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75801.sa0](https://doi.org/10.7554/eLife.75801.sa0)

This paper provides a fundamental account of the role associative learning plays in sensorimotor adaptation. In a compelling result, the authors show that by pairing movement-related feedback with conditioning cues in the form of neutral auditory or visual contextual cues can be used to differentiate between sensorimotor perturbations/states. This work nicely integrates multiple literatures surrounding the processes supported by the cerebellum and solves a long-standing puzzle of exactly how and when arbitrary cues can serve to shape motor adaptation.


---

# Peer review - Round 1

Editors:
- Taraz Lee, https://ror.org/00jmfr291 University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75801.sa1](https://doi.org/10.7554/eLife.75801.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Contextual effects in sensorimotor adaptation adhere to associative learning rules" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) More evidence for the temporal specificity of results. The authors advance the idea that the key difference between the current results and previous work that has failed to find evidence of associative learning is the temporal relationship between cues and feedback. However, no experimental evidence is provided that this timing is fundamental. There is a need for new data showing the importance of the temporal relationship to support many of the conclusions drawn in the article. (See comments from reviewer 2 below.)

2) There are many instances of places in the manuscript that lacked clarity and could benefit from more exposition and inclusion of some of the supplementary analyses. These include a better explanation of the task, how the various stimuli (US, CS, etc) map onto the task, the inclusion of Supp. Figure 1 in the main text, and (See comments from both reviewers below.)

3) More discussion about the models considered and their similarities/differences and their diverging predictions.

Reviewer #1 (Recommendations for the authors):

I recommend writing a clearer explanation of the associative learning approach investigated here and the relationship between standard ways of looking at visuomotor rotation and associative learning and making the notation for the latter clear and concise

I suspect some of the readers of this article will be more familiar with VR rotation and dynamic learning as less so with classical conditioning. The task could certainly be explained more clearly.

It would help to have a more explanation of how the current study operates as a standard visuo motor rotation task. Then explain how this is related to a classical conditioning task. There are lots of abbreviations including CS+, CS- etc. it would be helpful to have a table to illustrate the analogous link between conditioning and VR learning.

Figure 1 could be explained better. Suggest having a bigger schematic of the task since understanding this is key to understanding the article. maybe have it as a single figure

Simulations of the RW models are carried out. However only their basic formulas are stated (Equations 1 and 2). It would be better to show more details in the methods (by providing the equations) for how precisely experiments 1 and 2 were simulated. pseudocode for explaining simulations would also be nice.

There is a mention of simple state space models not being able to deal with contextual effects. It would be useful to elaborate on this with reference to the equations that describe these models. It would also be helpful to discuss the differences between RW model and state space models, And also the deficiencies of both.

Supplementary figures are used. I would suggest it's better to fully explain them and include them as part of the main document.

The Github supplementary materials appears to be a clone of the author's working directory for simulations of this project and it is also hard to follow. There is of course no need for all this detail, but it's fine to provide it. I would however suggest that the main scripts for critical simulations for Experiments 1 and 2 are made easy to identify and run, if readers wish to do so.

Reviewer #2 (Recommendations for the authors):

Temporal specificity of results: The authors predict and conclude that the key parameter for observing associative learning when using arbitrary stimuli as contextual cues is the temporal relationship of these cues to the feedback. They provide compelling evidence of associative learning however at present provide no evidence of the importance of this temporal relationship. Considering this is assumed to be the key difference between the current results and previous work who have failed to find an effect, I believe the article requires additional work (maybe by introducing a delay between CS and movement) that examines the importance of this temporal relationship. Providing evidence that the associative learning effect is dependent on the timing between the cue and feedback being between 100-500ms is fundamental to support some conclusions made in the article.

Exp 1 probe phase results: Whilst not significant (n-1 x n interaction), there seemed to be a clear difference between CS+ trials within the different trial n-1 contexts (Figure 1D). In fact, this difference seems bigger (and as consistent) as the meaningful/significant differences which are focused on. Interestingly, the RW model predicts a clear n-1 x n interaction however it is not discussed why (Figure 1F). To me it seems that the behaviour (at least partially) and model reflect an interaction between trial n-1 and n during probe trials however this is currently not discussed. Could the authors elaborate on this result and include this in the article?

Magnitude of effect (supplementary S1 figure): Suppl Figure 1 needs to be in the main article as it provides context and some 'raw' data. It would also be beneficial to have in the main article a similar figure but with the CS+ and CS- trial types separated. Suppl Figure 1 is important as it highlights that the conditioning effects are relatively small. This needs to be explained/mentioned in the results i.e., that the differences between CS+ vs CS- (1-degree) are approx. 6% of the total adaptation that occurred (15-degrees). I suppose this is referred to within the final exp 1 analysis (Figure 2B) but its not explicit. Although I believe the results are important, the article currently reads as if these conditioning effects were large when in fact other people might conclude that conditioning had little impact on adaptation (as similar adaptation (approx. 15-degrees) was observed across both contexts (assumed as this is not shown) and performance looks very similar to exp 2 where there was no 0-degree context). There needs to be some acknowledgement of the fact that while these conditioning effects appear meaningful, they were small (with most participants showing less than a 1-degree difference between contexts).

Exp 2 results: It was unclear to me why the RW model would predict a negative heading angle within the single CS conditions (Figure 3C)? I understand that a weaker conditioning response would be expected due to compound conditioning, but would you not expect this still to be positive? Why would the model predict extinction to occur and why is this seen in the behaviour? The details of this result (and the predictions of the model) are currently not discussed in sufficient/any detail.

What is the CS (confusion between results and discussion)? Between lines 395-410 the authors describe the primary CS as being the heading angle ('the movement plan itself, rather than the target cue, that constitutes the primary CS'), however in the results (lines 74-96) they describe the CS as being the arbitrary cue ('When considered through the lens of classical conditioning, the arbitrary cues are the conditioned stimuli (CSs)') and the CR being the heading angle ('the conditioned response (CR) would be the movement heading angle elicited by a CS'). As a result of this discrepancy, I found this section of the discussion very confusing (lines 387-410 and then again from line 433). Are the authors saying that sometimes the heading angle/plan is the CS and other times it is the CR…? How does this all align? One can see why a suggestion for a figure showing this mechanism visually is suggested below.

Link between this work and recent contextual inference model by Heald et al.,: Could the authors provide a more direct comparison between the current work and the contextual inference model by Heald et al., (in discussion)? The authors currently say 'their model suggests that spontaneous recovery and consistency effects emerge due to contextual inferences that likely interact with deliberate changes in explicit strategies' however does this align with the current work? How does contextual inference align/differ with these conditioning mechanisms? In future work, the authors seem to want to explain the phenomena (spontaneous recovery etc) recently explained by this model and I am interested to know whether these are competing explanations or are explaining the same mechanism or are different but complementary?

Use of supplementary figures: Why did the authors decide to put so much of the important detail into the supplementary? In my opinion, all of this should be in the main article.

Normality of data and presentation of individual data: There is no mention of any assessment of data normality, was the data normally distributed? In addition, a greater amount of individual data should be shown rather than mean +- SEM.

Figure to represent conditioning mechanism: I would find it very helpful if an additional figure was added which showed the US, UR, CS and CR visually. I kept forgetting how each of them were proposed to be represented in the task.
