# Peer review - Round 1

Editors:
- Michael Breakspear, QIMR Berghofer Medical Research Institute Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.38844.023](https://doi.org/10.7554/eLife.38844.023)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A prediction model of working memory across health and psychiatric disease using whole-brain functional connectivity" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Monica Rosenberg (Reviewer #2); Xi-Nian Zuo (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The central findings – transdiagnostic WM prediction – builds nicely on recent work on fingerprinting, prediction and transdiagnostic analyses. It is actually quite surprising that training a model on such a small set of healthy subjects generalizes across diagnoses and demographics that lie well outside the training data, but therein lies the value of the paper. While the relatively "dirty" acquisition and cohort details may not be ideal from a pure research perspective, it probably adds to the ecological validity and clinical translatability.

The paper has had two very thorough, excellent technical reviews. All major concerns are reasonable and should be addressed. Four concerns warrant specific commentary:

1) Reviewer 2's first point regarding the greater specificity of 2-back over 0-back to working memory and whether there are other cognitive processes at play.

2) Reviewer 3's first point regarding test-retest reliability. Ideally, you could pursue the reviewer's request here, although I note he has offered alternatives if this is not possible.

3) Much of the model (~34%) relies on left FP self-correlation – some sort of proxy for the internal coherence of that ICA map. None comes from the right FP – a slightly odd dependence on one feature and an asymmetry. It would be reassuring if this stood up to the test retest reliability analyses.

4) Given that you use parametric test statistics, it is not obvious why you also employed resampling to ascertain significance.

Reviewer #2:

In a training sample of 17 healthy adults, the authors built a model to predict d' on a 3-back task from between- and within-network resting-state functional connectivity. They applied the model to resting-state data from an independent sample of 474 healthy adults from the Human Connectome Project dataset and found that model predictions were significantly correlated with n-back task performance when controlling for fluid intelligence and motion, significantly (inversely) correlated with fluid intelligence when controlling for n-back performance and motion, and not significantly correlated with motion when controlling for n-back performance and fluid intelligence. They applied the model to a second independent sample of resting-state data from 58 individuals with schizophrenia and found that predictions were correlated with a working memory measure when controlling for general cognitive ability and age. Based on these external validation results they argue that the model is generalizable and specific to working memory abilities.

They next applied the model to three additional datasets with patient and control populations. They found that predicted degree of working memory impairment relative to matched controls was greatest for patients with schizophrenia followed by patients with major depressive disorder, obsessive compulsive disorder, and autism spectrum disorder. This ordering replicates the degree of working memory impairments reported by previous meta-analyses.

Overall this paper is a rigorous example of neuroimaging-based predictive modeling based on the generalization to two external validation datasets and between-group comparisons in three additional independent samples. My enthusiasm for the work is only slightly dampened by questions about the patient-vs.-control analyses, the specificity of the working memory model, and the feature importance analysis.

1) The authors take steps to show that model predictions are related to working memory ability specifically rather than cognitive ability more generally, but additional analyses would strengthen this claim. First, the measure of working memory in the HCP dataset includes 0-back task performance, which indexes sustained attention and attentional control rather than working memory. Are model predictions more closely related to 2-back than to 0-back task accuracy? Furthermore, because even 2-back and 3-back tasks measure a number of processes beyond working memory (Kane et al. 2007, J Exp Psychol Learn Mem Cogn), it would be informative to test whether model predictions are related to another measure of working memory such as performance on the NIH toolbox list-sorting task. Second, in the group-level analyses, are predicted working memory deficits more similar to working memory deficits observed in meta-analyses than they are to deficits observed in fluid intelligence or other cognitive domains (in terms of effect size or relative ordering across disorders)?

2) The lack of working memory measures presents challenges for the between-group comparisons in the patient samples. Although within each site the samples are matched on age and sex, the groups differ along a number of dimensions beyond working memory (e.g., medication status and potentially IQ and other cognitive abilities), and it's not clear whether patients and controls were scanned under the same protocols at each site, or whether protocols differed between sites. Limitations due to these potentially confounding factors should be clearly outlined in the manuscript. Related to this, are there working memory scores for the controls in the schizophrenia sample? If so, did predicted impairment reflect observed impairment in that sample, and does the model hold when applied to this full sample of patients and controls together?

3) It appears that the measure of general cognitive ability in the schizophrenia dataset includes a verbal memory measure. How correlated are working and verbal memory scores in this sample, and what is the justification for including it in the general cognitive ability score rather than treating it as a variable of interest?

4) Why was the HCP 500-subject release (2014) used rather than the 900-subject release (2015) or the 1200-subject release (2017)? Although the external generalization results are strong I would find it even more convincing if the model generalized to the full sample of HCP individuals.

5) The analysis of model weights and functional connectivity alterations between patient and control groups is somewhat confusing. Why does Figure 2 visualize the product of mean FC values and model weights (which will change depending on an individual's unique FC values) rather than just the raw model coefficients? Why do the patient/control difference scores incorporate model weights, rather than simply reflect changes in FC networks predicting working memory? It would be helpful to explain these choices in greater detail.

6) More details about the scrubbing procedure applied would be useful. Were frames before and after high-motion volumes excluded? What was the distribution of number of excluded volumes in each dataset? Did this differ by dataset or group?

7) The manuscript is lacking a discussion of predictive network anatomy, anatomy of networks that change vs. stay consistent between disorders, and implications for cognitive psychology or cognitive neuroscience. What do the current findings tell us about working memory and the functional networks that support it from a basic science perspective?

Reviewer #3:

The authors performed predictive models to examine FC-WMA across psychiatric diseases using a verbal 3-back task. This work was done using a set of data cohorts. The predicted effect size estimates on verbal WMA impairment were comparable to previous meta-analysis results. I personally enjoyed reading this manuscript. This is a very nice sample for reproducible brain-behavior association studies. I would be happy to support its acceptance of a publication in the eLife journal. However, I still have several concerns, which need to be fully addressed before the publication.

Summary of concerns:

1) It is highly important for studies using clinical patients to choose a measurement tool with high test-retest reliability. The authors employed ICA-derived networks as spatial profiles for whole brain FC modeling, however none of any references was given to support its reliability reaching to the clinically recognized request (ICC > 0.8). Is there any possibility of performing a test-retest analysis using public test-retest datasets (e.g., Consortium for Reliability and Reproducibility) to demonstrate the reliability matched to the level in clinic. At least, the literature on test-retest reliability of rfMRI metrics should be carefully documented if you cannot do it in the reasonable time frame (e.g., < 2months), see a review on this topic from my lab (PMID: 24875392). Meanwhile, dual regression with group ICA has been a highly reliable method, and the authors compared it with the FC method for the predictive modeling?

2) Head motion: Power et al. recently (PMID: 28880888) demonstrated that the order of performing preprocessing rfMRI data has effects on the performance of head motion removal. Of important relevance here is that the data should not be corrected for slice timing differences before the head motion estimated and reduced. The authors should check if their findings are influenced by such a change. Regarding the preprocessing, it is worth noting that ways of dealing with motion are different across data cohorts. How will this have an impact on reproducibility of the findings?

3) Demographical factors: It is widely known that age and sex have effects on FC, and how these two affect the observations reported here?

4) Figures: In Figure 1C, it is quite confusing that all the drawings of the graphical brain are the same across different clinical diagnoses (SCZ, MDD, OCD and ASD).

5) The authors have done a good work on dealing with head motion. However, just a curious point, several work also demonstrated potentially meaningful factors embedded in head motion as trait of human beings. At this point, interesting points related to the current work are: 1) Is there any relationship between motion and WMA? 2) Is there any correlation between global signal and WMA? 3) If so, what is the causal relationship among the four (motion, global signal, WMA and FC)?

6) Is there any plan in place to share the data publicly?
