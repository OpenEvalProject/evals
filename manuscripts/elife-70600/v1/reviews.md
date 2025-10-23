# Peer review - Round 1

Editors:
- Jesse H Goldberg, https://ror.org/05bnh6r87 Cornell University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70600.sa0](https://doi.org/10.7554/eLife.70600.sa0)

The extreme memory capacities of food-caching birds provide untapped opportunities for studying mechanisms of memory formation and retrieval. Here, Applegate and Aronov develop an automated animal and cache-site tracking system in which moments of seed deposits, retrievals, and checks are measured continuously alongside the animal's spatial positions. Probabilistic models reveal idiosyncratic spatial preferences in individual birds and also identify flexible memory usage – in which a single memory of past seed deposition can differentially guide spatial trajectories depending on if the bird is in engaged in retrieving or storing seeds. The rigorous behavioral tracking and modeling sets the stage for dissection of neural mechanisms underlying memory storage and retrieval.


---

# Peer review - Round 1

Editors:
- Jesse H Goldberg, https://ror.org/05bnh6r87 Cornell University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70600.sa1](https://doi.org/10.7554/eLife.70600.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Flexible use of memory by food-caching birds" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Laura Colgin as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) All reviewers agreed that the paper overstates the novelty of the behavioral findings. Please address issues raised below.

A main concern is to what extent this paper truly offers an original behavioral result with respect to the flexibility of memory. It is known that birds can remember seed caches and the major gains of the present manuscript are not revealing a new faculty but rather describing a method by which to study that faculty in the laboratory. Also, the sample size is rather small (N = 7 to 17) and variable across figures and analyses. For example, many readers will be familiar with decades-old studies by Sherry, Clayton, and Shettleworth that showed similar flexible memory use by caching birds (e.g. Raby et al., 2007; Shettleworth, 1990; Clayton et al., 2003). As is, the current introduction simply states that flexible memory is 'a matter of debate' in animals – but those familiar with previous studies of caching would likely disagree. The authors should re-write the introduction and abstract to be as generous as possible to past field work, to specify precisely what was previously known, and what is the truly new behavioral finding (if any) in the present work. For example, it's conceivable that this paper could be framed differently, i.e. "it has long been known that caching birds exhibit flexible memory that enable them to target specific sites differentially for depositing versus retrieving seeds, here we leverage this flexible memory capacity to quantify precisely how remembered cache locations influence foraging on a moment to moment basis." (or something like this…)

As in, a potential strength of the paper is the behavioral modeling which identifies the precise candidate considerations (parameters) that influence moment by moment aspects of foraging. This model has the potential to provide an algorithmic level description of the task, which in turn provides numerical values that could conceivably be identified in neural signals in future recording studies (see point 2 below to shore up this potential). It's one thing to show that caching birds have flexible memory (as past work has shown), but what seems uniquely new about this paper is that it leverages this past work towards a model that makes instant by instant predictions for how 'special' places influence behavior in a space- and time-dependent way. This algorithmic level description of the behavior is what could be novel, which should therefore be emphasized in the abstract/intro.

(2) If, as the reviewers suggest, the focus of the paper shifts from a descriptive account of the behavior in the new preparation to an emphasis on the validity of the statistical models, then more needs to be done to motivate the modeling decisions. It is currently not convincing that the parameters of the model are dissociable, especially since birds can continually cache and retrieve and recache.

Here are some unanswered questions that should be addressed if we are to take the quantitative parameter estimates of the models seriously, rather than the overall goodness of fit revealing the existence of some feature of the behavior (e.g. behavior is spatially autocorrelated).

(2.1.) Is log-linear interaction of the parameters appropriate or are there more complex dependencies?

(2.2) Is a Gaussian spatial autocorrelation function appropriate? Is the standard deviation fixed across space? Across strategy?

(2.3) Is time-dependent forgetting tested/modeled appropriately? There was an odd mismatch between the statement about preference for re-caching and the lack of a forgetting curve. What is the longest the animals will have a benefit from remembering caches? If only during one session, is this then perhaps a weakness in the task since one would expect birds in the wild to cache for longer time periods? Given that birds are rechecking single sites every 2.4 minutes, the authors should provide a more convincing argument how this unstructured task addresses the issue of memory decay.

(3) Please clarify how the spatial biases identified for individual birds affect caching strategy.

Currently the authors separately present first that birds have individual spatial biases and later on with a modelling approach show that previous visits and general proximity also biases the animals search and caching behaviour. But how do the two aspects relate to each other? One would assume that a general individual bias would decrease the number of possible locations the animal in general has to look at and therefore it is perhaps a mix of memories being used: the bias memory as well as the episodic memory of caching food. If one would include the bias as well as the principles that the animals have a proximity preference, how much variance will still be explained by the episodic memory? Or is the individual bias a result of the proximity bias? It would be good if the authors could create one major model which includes all identified factors to see how much which factor contributes.

(4) Please provide supplemental videos and increased clarity of the experimental timeline.

Further, it would help readers to understand the details of the behaviour if for example videos of the bird behaviour are provided with the manuscript for the different types of trials. That would help the reader understand in which times scales the animal is remembering and deciding. Further, an overall schematic of the timeline for the birds would be helpful. How long were they trained and habituated on what? How many sessions per day? How many days/weeks in total? For example days/weeks could go to the right and then down would be time within a day since multiple sessions were done per day. Then it can also be marked which data was included for analysis.

(5) Several technical points, if addressed, could make the statistics a bit stronger.

First, for the description of spatial biases, it appears that the same data is used to assign cluster membership and then quantify cluster separation. Some sort of cross-validation should be used throughout the analyses plotted in Figure 2 (Panel 2E notwithstanding).

Second, for the model fitting, a point estimate is used. It would be good to know the confidence around these point estimate and here a Bayesian framework would be helpful perhaps using Markov chain Monte Carlo methods to finds highest density intervals for likely parameter estimates (e.g. Annis and Palmeri 2017, doi: 10.1002/wcs.1458; Kruschke 2013 DOI: 10.1037/a0029146).Reviewer #1 (Recommendations for the authors):

Applegate and Aronov develop an automated animal and cache-site tracking system to study foraging strategies in chickadees. A key strength of this system is that each moment of seed deposit, retrieval, and 'checks' is marked alongside the animal's spatial position. Tracking animals and their caching presents tremendous opportunities for the study of memory storage and retrieval. The paper's main strength is the quantitative modeling of the caching behavior, which is elegant and has explanatory power over moment-to-moment navigation decisions. The paper's main weakness is overstatement of the novelty of the discovery of flexible memory use by caching birds. This paper need not 'discover' flexibly memory use to be of general interest for eLife readership. Leveraging this very unique behavioral capacity for the generation of highly predictive foraging models is sufficient on its own to make a large impact.

(1) The setup of this paper unnecessarily overstates the novelty of the behavior and understates the utility of the behavioral modeling for future mechanistic studies.

A main concern is to what extent this paper truly offers an original behavioral result with respect to the flexibility of memory. For example, many readers will be familiar with decades-old studies by Sherry, Clayton, and Shettleworth that showed similar flexible memory use by caching birds (e.g. Raby et al., 2007; Shettleworth, 1990; Clayton et al., 2003). As is, the current introduction simply states that flexible memory is 'a matter of debate' in animals – but those familiar with previous studies of caching would likely disagree. The authors should re-write the introduction and abstract to be as generous as possible to past field work, to specify precisely what was previously known, and what is the truly new behavioral finding (if any) in the present work. For example, it's conceivable that this paper could be framed differently, i.e. "it has long been known that caching birds exhibit flexible memory that enable them to target specific sites differentially for depositing versus retrieving seeds, here we leverage this flexible memory capacity to quantify precisely how remembered cache locations influence foraging on a moment to moment basis." (or something like this…)

As in, the strength of the paper is the behavioral modeling which identifies the precise candidate considerations (parameters) that influence moment by moment aspects of foraging. This model provides an algorithmic level description of the task, which in turn provides numerical values that could conceivably be identified in neural signals in future recording studies. It's one thing to show that caching birds have flexible memory (as past work has shown), but what seems uniquely new about this paper is that it leverages this past work towards a model that makes instant by instant predictions for how 'special' places influence behavior in a space- and time-dependent way. This algorithmic level description of the behavior is what's novel, which should therefore be emphasized in the abstract/intro.

Discussion paragraph lines 375-387 provides the most accurate description of the contribution of the present work.Reviewer #2 (Recommendations for the authors):

In this article the authors present a new behavioural task in birds and combine it with a modelling approach to show that birds can use food-caching memories to guide both the retrieval of cached food as well as to guide the decision where to cache new food. Overall this is an interesting study and with mainly only minor issues.

The authors claim in the abstract that they could show that a single memory can be used for at least two unrelated goals. However, in this case the goals are not really unrelated, in my view. Caching new food and retrieving old food is still part of one behavioural aspect/goal of the animal.

Currently the authors separately present first that birds have individual spatial biases and later on with a modelling approach show that previous visits and general proximity also biases the animals search and caching behaviour. But how do the two aspects relate to each other? One would assume that a general individual bias would decrease the number of possible locations the animal in general has to look at and therefore it is perhaps a mix of memories being used: the bias memory as well as the episodic memory of caching food. If one would include the bias as well as the principles that the animals have a proximity preference, how much variance will still be explained by the episodic memory? Or is the individual bias a result of the proximity bias? It would be good if the authors could create one major model which includes all identified factors to see how much which factor contributes.

Further, it would help readers to understand the details of the behaviour if for example videos of the bird behaviour are provided with the manuscript for the different types of trials. That would help the reader understand in which times scales the animal is remembering and deciding. Further, an overall schematic of the timeline for the birds would be helpful. How long were they trained and habituated on what? How many sessions per day? How many days/weeks in total? For example days/weeks could go to the right and then down would be time within a day since multiple sessions were done per day. Then it can also be marked which data was included for analysis.

The authors did not provide adequate statistical information related to each reported p-value. Example: Line 117 → "In all birds, entropy was lower than expected by chance p < 0.001", they did not clarify what is the chance probability and which statistical test they used to compute the p-value. I assume they computed it based on the shuffling analysis (lines 629 and 630) but it needs to be clearly and more adequately described.Reviewer #3 (Recommendations for the authors):

In this manuscript Applegate and Aronov used statistical modeling to study the food caching strategies of the black-capped chickadee in the laboratory setting. The authors show that in a modest sample of birds a subset prefer the center of their arena (61cm x 61cm). Birds tended to have spatially autocorrelated behaviors and remembered cached locations as evidenced by avoiding locations that contain a seed while caching and seeking baited locations when retrieving. Birds would often retrieve and recache seeds and these were preferred as were the last seeds cached. In short, the authors can replicate important aspects of natural behaviors in their experimental preparation.

The presented findings clearly set the ground work for careful behavioral analyses of future studies linked to a more mechanistic understanding of why the birds behave as they do. In the present form, the statistical modeling is rather descriptive and the insights gained will likely relate to a rather narrow audience interested in laboratory assessments of spatial memory. In addition, it is known that birds can remember seed caches and the major gains of the present manuscript are not revealing a new faculty but rather describing a method by which to study that faculty in the laboratory. Also, the sample size is rather small (N = 7 to 17) and variable across figures and analyses.
