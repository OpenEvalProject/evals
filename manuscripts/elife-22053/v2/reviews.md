# Peer review - Round 1

Reviewers:
- Oliver Brady, London School of Hygiene and Tropical Medicine , United Kingdom

## Review text

DOI: [10.7554/eLife.22053.016](https://doi.org/10.7554/eLife.22053.016)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Data-driven identification of potential Zika virus vectors" for consideration by eLife. Your article has been reviewed by three peer reviewers and the evaluation has been overseen by a Reviewing Editor and Prabhat Jha as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Anthony Wilson (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Overall, the feedback from this round of reviews was positive and all reviewers agreed that this is a novel approach to the identification of Zika's mosquito vectors. However, following a discussion among all three reviewing editors, some key themes emerged that we would like to see addressed before making a final decision on this manuscript. While we would like to see you address all of the major and minor comments of the reviewers, in particular we would like to see you pay particular attention to:

1) More rigorous model evaluation- from a statistical point of view, yes the model AUCs seem reasonable, but we all felt that this alone, was not enough to judge how effective these predictions were. A key assumption of the approach is that vector competence is associated with the kinds of traits that are readily observable and comparable. In addition to this, many key indicators that might be important for this are not included/considered, e.g. sub-species of vectors, evolutionary changes in vector competence. Judging by the top model predictors, it seems that there are very few traits that offer much explanatory power in this respect and perhaps a more nuanced explanation of why the model predict each of these new Zika vector species is required. Additionally we would like to see validation against a known outcome, e.g. if the vector-virus pairs of dengue, yellow fever or West Nile were left out of the fitting set what vector species would be predicted for each of these?

2) The caveats of this particular study need to be more appropriately articulated. The main output of this model is a list of candidate vector species to be tested experimentally for Zika virus competence (and ideally prioritised by likelihood of competence as predicted by the model and public health importance- i.e. additional population at risk, none of which is currently done in the paper). As it has been demonstrated many times that vector competence does not equate to sufficient vectorial capacity to cause outbreaks, let alone sustain transmission, it is perhaps premature to suggest that new risk assessments need to include other vector species at this stage. Please revise this and consider refocusing on providing useful recommendations for follow up studies.

Essential revisions:

Reviewer #1:

Evans and colleagues have submitted a manuscript detailing a novel and well conducted analysis that addresses a timely question of international public health importance. While, at times, the manuscript does overstate the significance of the findings and omits some important limitations, it is fundamentally an exciting study that could be of interest to a broad range of readers.

I am struggling to reconcile the parallel findings of high model performance (as demonstrated by AUC) and the finding that subgenus and continental range (two variables with extremely limited degrees of freedom, especially where Zika is concerned) contribute a high amount of the models' power. It seems that these very general and non-specific covariates would naturally lead to low specificity- how does the model AUC vary when predicting vector virus pairs for viruses with different characteristics – are very limited geographic scope viruses much easier to predict? If so, is there a more appropriate model evaluation measure for a broadly distributed disease such as Zika (and thus differing thresholds)? It would at least be useful to explain what features of Zika lend it to such a high number of predicted vectors relative to, say dengue.

This analysis quite rightly restricts its predictions to binary endpoint of vector competence. There is, however, a big difference between a competent vector and a vector that presents a true epidemiological risk. This is exemplified by Ae. aegypti vs Ae. albopictus in dengue with the former being responsible for the vast majority of transmission (see Lambrechts et al. 2010 PLoS NTDs). While I agree with the authors that these findings warrant further investigation of the competence of these species, to suggest that they need to be included in Zika risk maps makes too many assumptions (e.g. epidemiological significance, that other species will not outcompete their role as a vector, etc.) that are not supported by analysis in this manuscript. I would suggest re-wording to reduce the emphasis on this suggestion and including more limitations on why these vector species may not ultimately be epidemiologically significant.

Reviewer #2:

This study used data-driven, machine-learning algorithms to identify potential vectors of Zika virus. Although the premise of the study is good, several shortcomings of the approach make it difficult to ascertain the relevance of the results, which could be largely misleading. Some of the most important shortcomings are listed below.

The authors set out to "address the problem of identifying potential vector candidates in a suitable time frame" because "the amount of time required for analyses can delay decision making". However, identifying candidate Zika virus vectors would not preclude their subsequent empirical validation. So it is unclear what is the applied value of this modeling exercise.

A strong, unjustified assumption underlying the approach is that "the propensity of mosquito species to associate with Zika virus is statistically associated with common mosquito traits".

Documented implication of a given mosquito species in the transmission cycle of an arbovirus does not necessarily imply the universal importance of a vector species in the transmission cycle of this arbovirus. Vectorial capacity results from the combination of several factors, so that in certain local conditions (e.g., high mosquito population density, high temperature) even a poorly competent vector could play a significant role in transmission.

Vector status of a mosquito species for a given arbovirus cannot be permanently defined. Vector status is a dynamic process that can rapidly evolve (e.g., recent adaptation of chikungunya virus to Aedes albopictus).

Intra-species variation, which can be substantial for several mosquito traits, was ignored.

There was no empirical validation of the modeling approach.

Reviewer #3:

Vector-borne pathogens are emerging with increased frequency. This manuscript presents an interesting and potentially useful approach to the incrimination of vectors of novel emerging pathogens and I believe it to be worthy of publication. I have a couple of queries and suggestions, detailed below.

Results section, third paragraph: I suspect one criticism of this approach will be that it results in overly broad predictions (although even if true that would not mean it will not be useful in suggesting targets for epidemiological study). I would like the authors to add the result of applying the same method to 'predict' the vectors of dengue virus, yellow fever and West Nile virus when information on the respective viruses is removed from the training data.

Discussion section, first paragraph: could the authors elaborate on the additional regions or populations at risk from transmission based on their expanded 'worst case' vector list – or, even better, which newly-incriminated vectors make most difference to this? This should be possible using the dataset they have already collected (with the caveat that this is a worst-case scenario, and vector density and local environmental conditions also affect the potential for transmission).
