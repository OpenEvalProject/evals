# Peer review - Round 1

Editors:
- Woo-Young Ahn, Seoul National University Republic of Korea

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54051.sa1](https://doi.org/10.7554/eLife.54051.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Neural Arbitration between Social and Individual Learning Systems" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Michael Frank as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Jan Gläscher (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

While the reviewers find the topic interesting and think your paper is well-written, they raised several major concerns regarding the contribution of the work and the interpretation of the findings.

I will not repeat the reviewer's other comments here, but will highlight some of them.

There is a major concern about the novelty of the work given that the task used in this work is just a small modification of a task used many times before (reviewer #3). Reviewers #1 and #3 also question whether the task actually measures the 'arbitration' between social and individual information. Relatedly, the reviewers think it remains unclear if the participants truly believed the social information was coming from other people. I also suggest authors further discuss the neural findings in the context of social vs. non-social information. Lastly, reviewer #3 questions if the wager truly reflects arbitration between multiple information.

Reviewer #1:

Diaconescu and colleagues examined the computational and neural correlates of arbitration between self-gathered information and advice from others ('social' information). To enable a factorial analysis of information source and volatility, authors used 2x2 design (low vs. high volatility phases x two sources of information). Thirty eight individuals participated in a probabilistic learning task where they predicted the outcome of a lottery and hierarchical gaussian filter (HGF) was used to model the choice behavior. Behaviorally, authors found that volatility affected choice accuracy and amount of points wagered, which was consistent with existing literature. Model-based fMRI results showed that arbitration based on self-gathered information activated the midbrain and DLPFC whereas arbitration based on advice from others activated the amygdala and the vmPFC.

This is an elegant application of HGF to investigate the arbitration between multiple sources of information. I think the paper is well-written and authors rigorously compared multiple computational models and overall their methodology is strong.

1) As the authors also acknowledged in the subsection “Conclusions”, it is unclear if authors could examine the arbitration between non-social vs. 'social' information. In Diaconescu et al., 2014, from which authors adopted and modified a task, a pair of participants were invited to study decision-making in social interaction but in this study, it was not like that and I'm not sure if we can call it 'social information'. So, the findings reported in this work might be just related to arbitration between self-gathered information and self-perception of reliability of another source of information, which hampers my enthusiasm about this work.

2) Related to the previous comment, it would be useful to know how many participants actually believed they are playing with a human advisor. Also, please provide the instructions given to participants (e.g. were they told under what circumstances advisor is incentivized to give wrong/correct advice?)

Reviewer #2:

The authors describe a study that utilizes a variant of the "Advisor task", which was presented in a previous publications (PLoS CB, 2014 and SCAN, 2017) and which involved the binary decision for one of two lotteries in the presence of social advice. In this variant the author introduce a wager on the decision, which is affected by the volatility and the source of the information (card, i.e. own experience vs. advisor, i.e. social information). In a model-free analysis they show that the these two factors affect the decision, the advice-taking behavior and the wager that they place on their decision, which directly influence the trial-by-trial payoffs. The general finding was that decision accuracy was better during stable reward contingencies, whereas the same effect was more pronounced for advice-taking and wager size for the social information from the advisor. Using Hierarchical Gaussian Filters (HGF), the authors report that a fully hierarchical Level-3 HGF provide the best fit to the data. Several of the model's internal variables (amongst others the belief uncertainty, the arbitration between the different sources of information) were submitted to a model-based fMRI analysis, which identified a wide-spear network of brain regions that correlated with the arbitration signal. Further analyses suggested that arbitration in favor of the own experience correlated with activity in the amygdala and OFC, whereas arbitration in favor of the social information correlated activity in substantia nigra, DLPFC, insula and occipito-temporal and inferior temporal cortex. A separate ROI analysis constrained to neuromodulatory nuclei in the mid-brain also showed correlations with the arbitration signal.

The paper employs a task that is well-suited for dissociating the influence of different sources of information and renders itself well for computational modeling using the HGF. The findings are timely given recent report on the arbitration of model-free and model-based RL in the ventrolateral PFC. The paper is well-written and should if interest to the wide and sophisticated readership of eLife.

I only have a few suggestions for improvements of the manuscript:

1) Upon my first read-through, I found myself wondering what "prediction accuracy" (subsection “Behaviour: Prediction accuracy and wager size”) was referring to. In Figure 1, the choice of the subject is framed as a "decision", and it is only in the legend that this is referred to as prediction of a lottery. I think it would help the read to straighten out the terminology in the task description.

2) The BOLD time courses in Figure 7B look strange as they show the inverted shape from the normal BOLD response. Can the authors explain what is going on here?

3) The swoosh as the color bar is mostly meaningless in all the figures as one can only see the thresholded maximum value in the SPMs. I suggest to remove them (though I admit that they look cool).

4) The ROI analysis of mid-brain neuromodulatory nuclei needs to be better justified. The analysis pops up almost out of nowhere. It is clearly a relevant finding, but it should be stated more explicitly, why arbitration signals in these mid-brain nuclei are relevant for the current research question.

Reviewer #3:

Diaconescu et al. use a small modification of a previous task used many times before (Diaconescu et al., 2014, 2017; Behrens et al., 2008; Cook et al., 2019, to name a few studies) to examine the arbitration between individual and social advice learning. They test a good sample size of participants, and the addition of a trial by trial wager is interesting. However, I feel with the paradigm has been used so many times before that the study does not tell us anything particularly new. There is also a lot of visual activation in the individual learning condition and the Introduction and Discussion seem a bit disjointed. The fMRI results are also not particularly anatomically motivated, and just read like a long list of brain areas.

Does a model that was able to capture behaviour in the original task the authors used, with a dynamic learning rate (Behrens et al., 2007; 2008) perform worse than the behaviour estimated by the HGF? Moreover, there is an increasing appreciation that model comparison should not be the only way to decide between different models, but the parameters from the winning model should also be recoverable (Palminteri et al., 2017). Are the different model parameters recoverable?

In the Introduction the authors only discuss a putative role in the task for the dlPFC, TPJ and dmPFC, but very similar versions of the task have shown other areas to be involved, such as ventral striatum and different portions of the cingulate cortex. I feel the predictions about potential brain areas should relate more closely to the previous literature.

What are the correlations between the different time periods and parametric modulators in the GLM?

The authors justify not having a non-social control, but it is very difficult to interpret the results as they are not subtracted from another matched condition in the main analysis. This seems to be a general problem with the task itself that makes it very difficult to dissociate self and other relevant information. Indeed, studies by Cook et al. suggest a key difference between the social and non-social components in the task is that the social component represents an additional source of information to learn about, so is not just different in the social vs. non-social nature.

I am not convinced that this task measures the 'arbitration' between social and individual information. The authors state that the number of points wagered reflects 'arbitration' but does this measure not reflect confidence in the judgement? Also, as participants are not making separate wagers about the reliability of the reward and social information it is hard to know what precisely is influencing their decision.

How do the authors know that the participants believed the social information was from real other people?
