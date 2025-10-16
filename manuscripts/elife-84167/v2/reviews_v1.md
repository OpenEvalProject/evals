# Peer review - Round 1

Editors:
- Ben S Cooper, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84167.sa0](https://doi.org/10.7554/eLife.84167.sa0)

This important study presents a machine learning-based classifier that can accurately determine the geographic origin of a Salmonella enterica sample from its whole-genome sequencing data in under five minutes leading to actionable public health insights. Applying the method to 2,313 whole genome sequences collected in the United Kingdom and several external validation datasets, the authors provide convincing evidence that Salmonella genomic data can be used to identify the likely geographic source of a food-borne outbreak and, in most cases, correctly identify the country of origin of an infection acquired overseas. The work presents an excellent case for the potential utility of routine genomics coupled with machine learning for public health microbiology and the methods are likely to be applicable to other pathogens besides Salmonella enterica.


---

# Peer review - Round 1

Editors:
- Ben S Cooper, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84167.sa1](https://doi.org/10.7554/eLife.84167.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Rapid geographical source attribution of Salmonella enterica serovar Enteritidis genomes using hierarchical machine learning" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Neil Ferguson as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Nicole E Wheeler (Reviewer #2); Leonid Chindelevitch (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. It would be helpful expand on the comparison with existing methods giving more background on current state-of-the-art for geographic source attribution prior to this paper.

2. The training dataset appears to be only based on infections acquired overseas. It would be helpful to discuss the limitations in using this data source to investigate infections due to imported contaminated food.

3. More clearly communicating when a prediction is uncertain could be helpful in dealing with isolates from countries or food transport networks where it is hard to make a reliable determination. It would be helpful to consider this in the discussion.

4. There is a need for a discussion of limits to the utility of the tool due to exclusion of UK Salmonella isolates.

5. There is a need to improve the clarity of Figure 5, in particular increasing the resolution of the trees.

6. The authors should elaborate on the plausibility of missing data on multi-country trips and their frequency based on available travel data.

7. Any corrections made in the analysis for increased travel during the summer months should be stated.

8. Consider expanding the discussion on the poor predictions in the outbreak due to Polish eggs.

Reviewer #1 (Recommendations for the authors):

1. It would have been nice to see more background on state-of-the art for geographic source attribution prior to this paper. Currently there is just one sentence and two references (line 73-77).

2. Should define "SNP" on first use (line 109) also please explain "5-SNP cluster by SNP Address".

3. line 165: "was made up of 15 " or 16?

4. For a general audience (including public health professionals) it would be helpful to spend more time explaining key terminology eg "multi-class classifier", 'F1 score" etc. The work should be of wide interest, including to public health professionals, and explaining terminology would likely help increase impact of the paper.

5. line 166-167 "were predictable" What does this mean?

6. line 331 "Variation in classification accuracy was negatively associated with both low sample number and increasing within-class genetic diversity" is this the intended meaning or is what is meant "classification accuracy was negatively associated with both low sample number and increasing within-class genetic diversity" (i.e. is the association with classification accuracy or with variation in classification accuracy?).

Reviewer #2 (Recommendations for the authors):

Overall, this was an excellent paper to read. One thing I wish the authors had given more real estate to in the introduction is allowing the reader to understand how (if at all) the same determinations re: geographic origin are made today – how long does it take? Is there a big cost to an investigation? Are there regulatory or political hurdles?

I struggled to interpret Figure 5, and it is quite important for understanding this algorithm's capabilities. The main issue is the resolution of the trees, plus their size makes it difficult to discern how much overlap there is between the public and UKHSA data. The Microreact view makes this easier to explore and could be leveraged to create clearer figures. What I want to see in this figure is how interspersed the outbreak isolates are with UKHSA ones, which requires a close view and high resolution, and how interspersed isolates from different countries are for these outbreaks. When looking at the Poland/Spain mix-up in panel B on Microreact, it becomes very clear why this has happened when you look at the country of travel associated with each sample and the dataset each sample comes from.

Useful additional metadata columns on the Microreact tree would be the individual country of origin predictions and their associated probabilities – it would be helpful to see how confidence levels change across the tree and with more geographically interspersed clades.

Usually, I find F1 to be the best measure of accuracy, but here the % accurate calls would also be interesting, as this has direct public health implications, and there is a relationship between the total number of infections originating in a country and the accuracy of classification.

Reviewer #3 (Recommendations for the authors):

In addition to the concerns outlined above, here are a few typos that should be corrected; a non-exhaustive list:

– line 105: replace "from" by "to".

– line 247: providing.

– line 348: "before BEING passed ON to".

Also, just because a country has fewer than 10 samples in the collection does not mean it is "low incidence"; technically, this only means that it is "low incidence in UK tourists". Please clarify your statement accordingly.

The data and code are fully available, in compliance with eLife's policies.
