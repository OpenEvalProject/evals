# Peer review - Round 1

Editors:
- Erin L Rich, https://ror.org/04a9tmd77 Icahn School of Medicine at Mount Sinai United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75910.sa0](https://doi.org/10.7554/eLife.75910.sa0)

This manuscript describes three decision biases in value-based choice paradigms. Building on previous work from the lab, the authors focus on neural coding of decision variables in the orbitofrontal cortex of rhesus monkeys, and convincingly argue that different biases arise at different stages of the decision-making process. The reviewers found the study rigorous and believe that the results will be of broad interest. Understanding the neural mechanisms that produce biases in decision-making is an important goal for the field of decision-making and neuroeconomics, and also has relevance to conditions that involve disordered decision-making.


---

# Peer review - Round 1

Editors:
- Erin L Rich, https://ror.org/04a9tmd77 Icahn School of Medicine at Mount Sinai United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75910.sa1](https://doi.org/10.7554/eLife.75910.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Neuronal origins of reduced accuracy and biases in economic choices under sequential offers" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Veit Stuphorn (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Overall, reviewers found the study convincing and the results a significant advance in understanding circuit-level computations underlying decision-making. However, they raised multiple important issues to improve the clarity and specificity of the claims. The most important points to be addressed in revision are listed below, and the reviewers' individual comments are attached in full to provide additional context and suggestions.

Essential revisions:

1. The main topic that arose in reviewer consultation was the degree to which the conclusions rely on the lab's previous work parsing neural responses into discrete categories. Whereas this work has shown the reliability of these categories within the lab's own data, other literature has found conflicting results. Given that the degree to which categorical boundaries can be set within a continuum of response profiles is debatable, the reviewers think it's important to include discussion of the issue and acknowledgement of the explicit assumptions of the authors' methods and framework. Importantly, it's not just the categorization that the interpretation relies on: it's the assumption that each plays specific decision roles (valuation vs. comparison). (R1/R2/R3)

2. Conceptualizing the two tasks as computationally identical may not be accurate. The authors should discuss potential roles of working memory in task 2, and assess their model fits to behavior in each task independently. (R2/R3)

3. The idea of optimality, bias, and what constitutes reduced accuracy was also raised, and should be addressed by clarifications of the text: e.g. describe how exactly the different choice effects are 'detrimental', whether effects should be considered biases versus stochasticity, and how the findings here relate to classic effects in economic choice. (R2)

4. Please describe the rationale behind the order bias calculation, as opposed to using the a4 coefficient. In addition, consider how the signs of the neural order biases predict a consistent behavioral order bias. (R1/R2)

5. Please address why output signals do not reflect the reduced value sensitivity of the input signals. (R3)

Reviewer #1 (Recommendations for the authors):

1. The core premise of their interpretation/model is that the functional cell types they define (offer value, chosen value cells) are (mostly?) non-overlapping populations, if they contribute to distinct aspects of behavior. Is that strictly true, or are there subsets of cells that belong to both groups? In the methods section, it sounds like they force neurons to belong to only one group ("Tuned cells were assigned to the cell class that provided the maximum |sum(sR2 )final|"). This decision seems arbitrary but central to the interpretation that these really are different functional cell types.

2. On page 7, they define the order bias as ε = 2 ρTask2 a4/a3. Why don't they just evaluate the magnitude of the a4 coefficient? If it were 0, wouldn't that indicate no order bias? The sign would indicate the bias for first vs. second, and the magnitude the strength of the bias? Perhaps I am missing something, but that seems like a much more straightforward way to obtain an estimate of order bias from this model.

3. The authors show that offer value cells exhibit reduced responses for sequential compared to simultaneous offers. Is this true for both offer1 and offer2? They show an example neuron for both offer1 and offer2, but the population activity pools those responses together.

4. Related to point #1, it sounds like they combine data from task 1 and task 2 when they determine whether a cell is an "offer cell" or a "chosen cell." Are most of the offer value cells categorized based on their task 1 responses (i.e., is the maximum |sum(sR2 )final| the task1 offer value)? I am wondering the following: because there is a pre-stimulus cue at the beginning of each trial that tells the monkey which task it is performing, it's possible that the monkey/OFC treats them as two different tasks, and that slightly different populations of neurons encode offer value in each case. If that were the case, then using the task 1 responses to define the cells as encoding offer value could trivially result in the first finding, that there are reduced offer value responses in task 2. What if the authors determined whether cells were offer value cells based on the task 2 responses only? Does the result hold that the offer value responses are reduced, relative to task 1?

5. Figure 4F, the correlation is not very compelling. Is there something different about the sessions in which the sigmoid steepness and δ activity range go in opposite directions (i.e., the upper left and lower right quadrants?)

6. Throughout the paper, it is hard to remember what the different Greek letters refer to. For instance, on page 13, when ε reappears, I couldn't remember what that referred to. When possible, for clarity it might help to use interpretable terms when possible (e.g., order bias instead of ε).

Reviewer #2 (Recommendations for the authors):

Much of my feedback can likely be gleaned from the public review, but I'll be specific (and probably repetitive) here:

(1) It would be helpful if the authors provided a more detailed framing of existing behavioral economic choice biases and how the current choice effects relate. For terminology, it is a bit confusing that these previous findings are labelled "biases" but that one of the effects discussed here is increased stochasticity (reduced accuracy) rather than a bias – can the authors find some way of being more general about choice effects?

(2) For the analysis of choice behavior and the use of probit regression, it would help if the authors could quantify the goodness of fit of their choice functions (probit model using log amount ratios), specifically against alternative models (logit, and/or models with amount difference rather than log ratio). The big issue is that the relevant measures (accuracy, order bias, preference bias) depend largely on parameters derived form these fits, so it is important to see that the fits good and the model is appropriate. for the order effect in particular, have the authors examined the data while relaxing the assumption of a constant sigmoid?

(3) Re: the documentation of the preference bias, I would like the authors to be clearer in the text about the statistical test of the basic preference effect (higher rho in Task 1 vs. Task 2) – the effect is rather strong, and just needs to be clearly conveyed in the text. I do think that the dependence of the effect on relative value (i.e. rotation of the ellipse) seems to be less well supported: beyond clearing up the presentation of the significance of the results, perhaps this could be places in a clearer context vis a vis the basic preference bias – I don't think it is necessary to the general findings.

(4) Please be clearer about how exactly the different effects are detrimental. I think this point related directly to the initial framing about the difficulty of characterizing the optimality of value-based choice using behavior alone.

(5) Regarding the interpretation of OFC activity within the Rustichini/Wang modeling framework, I realize that the authors have good reason (and past data) to adopt this interpretation – I think it would be fair to at least acknowledge the explicit assumptions for the general reader.

(6) One interpretation issue that remains is whether the OFC neural effects are causal or correlational (particularly the accuracy and order effects, which can be seen in OFC activity). One issue that points towards the latter, at least in the order bias, is the sign of the neuronal effects (Figure 5C, Figure 6C). While the behavioral order bias is overwhelming positive, the neural effects (difference in AB vs BA rhos, circuit inhibition) do not on average differ from zero, even if they are correlated with the behavioral effect. If these neural effects drive the bias, shouldn't hey also be biased in the correct direction? Can the authors provide an interpretation?

(7) Additional points:

– How exactly is the preferred item (A vs. B) defined – across both tasks combined?

– Given the initial framing, it seems to me that these data – especially the preference bias effect – provides insight into the goods versus action based choice discussion (and relates to some previous work like Cai and Padia-Schioppa). Perhaps it would be relevant to discuss this briefly at the end of the paper.

– A conceptual question: given that all three effects are presented as suboptimal, why should this be the case given the initial framing that sequential decisions are the prevalent, natural form of choices?

Reviewer #3 (Recommendations for the authors):

The paper is written very clearly and the underlying logic for the different analysis is very well described. The results are for the most part convincing, albeit sometimes of a weak effect size.
