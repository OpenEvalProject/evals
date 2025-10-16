# Peer review - Round 1

Editors:
- Michael J Frank, Brown University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.23763.018](https://doi.org/10.7554/eLife.23763.018)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The computational nature of memory modification" for consideration by eLife. Your article has been reviewed by two peer reviewers, Marc Howard (Reviewer #1) and Brandon Turner (Reviewer #2), and the evaluation has been overseen by Michael Frank as the Reviewing Editor and Richard Ivry as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The present article develops and extensively tests a new computational theory of memory modification. Here, memory traces are modified based on a structural learning mechanism involving the inferred latent causes. The simulations they present show that the model can account for many of the experimental effects while holding a set of model parameters constant (for the most part). The idea of latent causes that are autocorrelated in time, and that modulate associations is an intriguing hypothesis that has the potential to make sense of a broad range of behavioral phenomena, and reconsolidation has been a topic of much recent interest.

Essential revisions:

1) All involved were largely enthusiastic about the contribution, but there was some concern about the relevance of the work to the biological sciences (neuroscience). One reviewer was concerned that there wasn't enough links, noting that there was no modeling of neural data or a serious mapping between the components of the model and neural circuits (even though some ideas along these lines are presented in the Discussion), and that it is not clear how the model would be implemented by biological neurons. The other reviewer noted that the section on neural implementation was highly speculative and could potentially be removed to cut down on space. It would be helpful to clarify the extent to which you think your work interfaces with the neurosciences and if appropriate, further emphasize the link and describe predictions relevant for neural manipulations and/or interpretation of recordings etc., if there are indeed clear predictions.

2) We thought it would be helpful to establish a closer connection to empirical data. You do an excellent job in reviewing the basic experimental effects, but this feels very abstract. Given that so much emphasis is directed at the relative differences in "CR" (isn't this P(CR)?) across conditions, it would be great to know what strengths of each effect should be expected. (This is not a model fitting expedition, so we are not expecting impressive model fits or anything, but some guidelines for the magnitude of the effects would be helpful.) For example, you could base a statistic of these other studies cited, something simple like probability of CR, overlaid with data and model, to ensure that the model is at least on par with the data. The issue is that you relate the simulations to data via statements like “high recovery of fear was observed in a test on the following day”, whereas you could just calculate what the recovery was (i.e., a probability) and use this as a guide in interpreting say, Figure 5.

3) One reviewer noted that the first few pages of the Introduction assumed too much prior knowledge of the reader (especially for a general journal). Could you elaborate on the basic details of the experimental paradigms? As someone who is unfamiliar with this literature, it was hard to follow the description of the experimental effects because the experiment itself had not been described. For example, section 1.1 reads beautifully and sets up the subsequent discussion nicely, but the first few pages seem to be predicated on this later section.

4) It is unclear why the EM algorithm is used here. It seems like an overly complicated assumption that really isn't justified well. You cite this Friston (2005) article, but can something more be done to explain why this choice was made (as opposed to others?)

5) Maybe some code could be provided to produce some of the simulations? The models seem pretty easy to set up, but it might be better for dissemination purposes to offer up a link to a simple simulation of the model.

6) It would be helpful to know more about the model parameters, and specifically what the model can predict and cannot predict. It was stated in the manuscript that the parameters were chosen 'heuristically' but that the basic patterns were observed for many other values of the parameters. Can more be said within the manuscript about which combination of model parameters fail to produce the desired effects? The critical question is whether the predictions from the model are consistent with the data because of its architecture itself, or is it just one specific version of the model that happens to work?
