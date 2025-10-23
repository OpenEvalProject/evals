# Peer review - Round 1

Editors:
- Daeyeol Lee, Johns Hopkins University United States

Reviewers:
- Alex C Kwan, Yale University United States
- Christopher H Donahue, Gladstone Institutes United States

## Review text

DOI: [10.7554/eLife.48810.028](https://doi.org/10.7554/eLife.48810.028)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Balancing model-based and memory-free action selection under competitive pressure" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Alex C Kwan (Reviewer #1); Christopher H Donahue (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Authors conducted a set of experiments using the variants of matching pennies game to understand how multiple decision and learning strategies might be arbitrated and influenced by the previous choice outcomes. They found that the strategy changed depending on whether the previous choice produced positive or negative outcomes. In addition, this was also reflected in the EEG signals recorded from the mid-frontal regions. A strength of this study is how by systematically varying the simulated opponents' switching probability the authors were able to reveal convincing behavioral evidence that a more global model-based strategy was used more strongly after wins vs. losses. The conclusions are well supported by the data.

Essential revisions:

1) The writing should be improved and some additional details should be provided in the Results. For example:

1a) The different experiments (i.e., Experiments 1, 2, 3, 4a, 4b, and 5) need to be explained better. In the main text, the reasons that motivate each Experiment are provided, however, there lack details to understand what is changed in the actual task design. Some additional explanation in the main text would help the readers so they don't have to refer to the Materials and methods each time. Then, in the Materials and methods section, the description of the Experiments is poor. Right now, the authors chose to describe a step and say it applies to Experiments 1, 3, 4, and then another step and say it applies to Experiment 2, 5, etc. A clearer approach would be to put each Experiment in its own section in the Materials and methods. For example, for the sake of clarity, when describing Experiment 2, some steps can be repeatedly describe and then also explain how it differs from Experiment 1. As a result, it is quite difficult to know exactly what the players were doing in the main part of the manuscript, so Experiment 3 (where they switch to traditional matching pennies) was confusing without reading through the Materials and methods. The description in "overview" just sounds like traditional matching pennies, but there is no indication there that every experiment except Experiment 3 used four response keys.

The authors should explain better why exactly the paradigm was altered in this manner. The authors' link it to "voluntary task switching" paradigms, but that logical connection and the implications are unclear. The logic surrounding this seems to be spelled out as allowing the distinction between "two potential sources of stochasticity", but this was still hard to follow. Was this added level of executive demand expected to impede the employment of model-based strategies on loss trials, selectively? Another justification for this choice of paradigm is that it "recreates executive control demands" in competitive scenarios. But what is such an example of an executive control demand that is selectively present for switching rather than staying with a choice, that is not capture by mapping actions onto different keys?

1b) From Experiment 1, for 80% opponent switch rate, the win rate is relatively low according to Figure 2—figure supplement 2. This is consistent and related to the fact that although subject adapts a model-based like strategy, the subjects still switch only ~60% given the opponent is switching at 80%. The subjects should switch at a higher rate post-win to gain further advantage. However the subject seems to be better at gaining this leverage at the low end of opponent switch rate. What may cause this asymmetry?

1c) The authors should clarify the relationship between choice inputs and noise, and how that can be dissociated based on response time and error rates. Currently it is taken as evidence that RT and error rates do not change that it is the choice inputs that have been reduced. But presumably noise is always present in the brain's decision-making system. So, any reduction in choice input means that the relative influence of noise is increased which would impact response time and noise. The authors are making some assumptions, and those should be stated in this interpretation.

1d) The Materials and methods should contain more details about how the computer opponent is implemented. Relatedly, for the computer opponent, it seems that the current implementation means that the computer does not consider the choice and reward history. What if the computer opponent takes some of that into account for its current decision? How would that influence the use of model-based versus memory-free strategy?

2) Another weakness is in regards to their EEG analysis which seems preliminary. The regression model used in the analysis seems to be missing some important factors related to sensory and motor information, but the interpretation of the psychophysical interaction analysis relies so heavily on this step. It is important to control for sensory and motor information when analyzing the EEG data. The authors should include regressors related to the position of the circle as well as the motor response (up vs. down). It may also be useful to show the time course of these regressors aligned to stimulus onset and the motor response.

3) There are some questions about the PPI analysis. In Figure 5, the time course of the regression coefficient for the interaction term looks to be almost identical to the one for the opponent's switch rate. Is it necessary to include this interaction term? Would AxC or even an interaction between A and a random vector look similar? In addition, the only data supporting the conclusion that the asymmetries in feedback representations are related to the next action vs. preceding actions appears to be the PPI analysis (Discussion, fourth paragraph), but this is not very convincing and the conclusion needs more support. Although there are important differences in task design which may make comparison difficult, results from recordings in non-human primates (Donahue, Seo, and Lee, 2013, Figure 5) clearly demonstrate the opposite.

4) Regarding Figure 4, is there an explanation for why some of the coefficients related to longer trial lags (n-3) do not decay to zero? Is there something important in the behavior that this model is not capturing?

5) Equation 1 is confusing. Does it miss a sign? For example, if we assume that the opponent behaves randomly (setting os=0), then including a positive pe term would actually lead to more switching in the model as written.

6) The manuscript does not appear to include the definition of an error. Are they omissions? Incorrect button presses?
