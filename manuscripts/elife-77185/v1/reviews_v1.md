# Peer review - Round 1

Editors:
- Dasa Zeithamova, https://ror.org/0293rh119 University of Oregon United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77185.sa0](https://doi.org/10.7554/eLife.77185.sa0)

This article will be of interest to a broad audience of cognitive neuroscientists interested in learning and memory, especially those who study the computations of the hippocampus in human and animal models. This work offers compelling evidence in support of a role for the computations theorized to occur within the hippocampus in category learning more generally. The well-conducted and rigorous computational simulations support the key conclusions and offer a novel theoretical entry into characterizing human learning.


---

# Peer review - Round 1

Editors:
- Dasa Zeithamova, https://ror.org/0293rh119 University of Oregon United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77185.sa1](https://doi.org/10.7554/eLife.77185.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A neural network model of hippocampal contributions to category learning" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Michael Frank as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Distinction from Schapiro et al., 2017: It is key to distinguish the current work from the simulations and findings in Schapiro et al. (2017). Although Reviewers were convinced that demonstrating that C-HORSE naturally accounts for category learning across a broad range of categorization tasks is novel and a worthy contribution, but how this is different from the senior author's prior work is not well argued in the current manuscript. In particular, the authors should address the conceptual differences between statistical/inferential learning (as is the focus in the 2017 paper) and category learning to highlight the novelty of the current work.

2. Apparent disconnect with established findings from unit recordings in CA1 and CA3: One concern, best described by Reviewer 2, is that in accounting for both statistical and category learning effects, C-HORSE may be unable to account for the more well-established body of empirical findings from unit recordings of hippocampal subfields. For example, it is not clear if the type of place and concept coding in hippocampal cells from rodents and humans are amenable to the predictions of C-HORSE. The Reviewers thought that this should be directly addressed by reviewing the literature which describes the response of single cells in CA1 and CA3 and considering how this corresponds to the predictions of the model, noting limitations where appropriate. Relatedly, Reviewer 3 noted that although the discussion of the CA1 vs. CA3 as it relates to functional differences in anterior vs. posterior hippocampus is an interesting point, the authors should soften their language here. Certainly, the C-HORSE findings coupled with anterior-posterior differences in subfields offers a compelling avenue for reconciling these viewpoints, but the matter is not as resolved as the discussion currently implies.

3. Situating C-HORSE in the literature: As a neurobiologically inspired model that provides insight into higher-level cognition, C-HORSE is broadly relevant to several research domains and existing theoretical frameworks (e.g., CLS, formal models of category learning, etc.). However, the Reviewers felt that it was not clear how to best place the proposed model in the literature. A formal comparison of C-HORSE to extant models seems beyond the scope of the current work. But, as a proof-of-concept alternative framework, the current work demonstrates how a single brain structure (i.e., hippocampus) can support both memory generalization and specificity. As such, the Reviewers suggest that making this proof-of-concept aspect explicit will help resolve confusion as to how C-HORSE in its current state should be considered alongside related theories/models.

4. Clarifying claims: In discussing the implications of their findings, the authors make several claims that over generalize their findings. For example, it is noted multiple times that MSP is "critical" and "responsible" for detecting regularities that support category generalization. It is true that MSP is clearly supporting this sort of generalization and more so than TSP, yet the simulation results also clearly show that the TSP-only model is still capable of above-chance categorization. The Reviewers suggest that the authors revise these statements to better align with the findings.

5. Directly characterizing the nature of representations in simulated tasks: The RSA approach is leveraged only in simulation 1, but would be helpful to consider for the other two simulations as well. In particular, many of the general versus specific claims made are based on indirect inferences from learning measures, when a direct characterization of the representations and how they change over learning could be made with RSA. The authors should consider adding these analyses for all simulations to better support their conclusions or provide a rationale for why they are not necessary.

6. Logic of initial vs. settled representations: In the RSA results of simulation 1, initial and settled representations are presented and compared, yet there is no logic provided as to why this is an important comparison to make (or even what initial vs. settled representations are, see point 7 below). The authors should provide a rationale for this analysis in terms of the learning mechanisms and information flow in the model.

7. Relationship to human learning findings: For each simulation, the qualitative fit between C-HORSE and end-of-learning behaviour from the prior work is mentioned in the main text to demonstrate a qualitatively "good fit" between model and human. Reviewer 1 suggested that these comparisons are expanded to (1) include behavioural measures across learning where appropriate and (2) include depictions of these behavioural effects in the figures. To be clear, quantitative fits of the model to empirical data are not expected, but that learning trajectories and end of learning performance in both model and human participants are more thoroughly considered in the text and figures.

8. Details of model and modelling approach: Although C-HORSE has been described in more detail in a prior paper (Schapiro et al., 2017), the Reviewers felt that more of these details should be included in the current work, especially since this will potentially reach an audience unfamiliar with the originating paper. In particular, important model mechanisms like learning rates, unit numbers across the layers, rationales for differences in TSP and MSP weights, cycles, and clamping should be further described and motivated.

9. More focused discussion: Although the discussion offers a comprehensive view on the role of hippocampus in category learning more broadly, it is not always connected back to the main conclusions of the paper. Reviewers suggested streamlining the discussion to include only those sections most relevant (see Reviewers 1 and 2 for specifics).

10. Clarity suggestions: The Reviewers also had several other suggestions that might increase the clarity of the methods, results, and discussion. The authors should please consider these suggestions and implement if they see fit.

Reviewer #1 (Recommendations for the authors):

I think this work is very exciting and compelling. However, I am certainly an insider in this field and am familiar with category learning research in general and relating hippocampal-based memory functions to learning behaviour. As such, it took a few reads to realize that the manuscript as is perhaps assumes to much knowledge of the reader. I think the contribution could be greatly strengthened if:

– More model details were provided. A citation is provided to the Schapiro et al., 2017 study, but important elements of the model that speak to key learning constructs are omitted (e.g., what is a cycle? what are initial and settled representations?)

– The authors should consider either directly evaluating the predictive power of C-HORSE relative to other models or recognizing the need for such an evaluation in future work as an important point for the discussion.

– Overall, the discussion could be refocused (and likely shortened) to put greater emphasis on the implications of the current findings to the broader themes in the literature.

– The RSA approach utilized in simulation 1 to characterize subfield representations should be used for all simulations potentially for both intact and lesion-variants of the model. Although the authors' main conclusions (MSP=detecting regularities, TSP=encoding items) can be inferred from the generalization and recognition performance of the lesion simulations, adding a more detailed and direct exploration of the model would strengthen the contribution significantly.

– The behaviour signatures of the original studies were described and depicted. Although there is some effort to describe how each of the three tasks capture distinct components of category learning, more description of these original studies in terms of their key behavioural patterns and what they reveal about category learning would be helpful. End of learning behavioural performance is sometimes provided in the main text, but it would help clarify the degree of fit from C-HORSE if these average accuracy measures from the prior work were plotted alongside the model results.

– In systematically varying the typicality of exemplars, the third simulation offers an interesting testbed for characterizing the contribution of MSP and TSP. And, in the analyses provided, there are hints at this. Recognition is better for TSP than MSP with increasing atypical exemplars. And, it is compelling that MSP matches TSP recognition with 1-2 atypical features. What I found most intriguing about this simulation is that the intact model offers the best performance. How is the information from both pathways combined in the model to drive good recognition? Characterizing this aspect of the model dynamics would potentially provide some insight into how the so-called complementary hippocampal functions are actually complementary.

– Relatedly, although the simulation results are interesting in this third study, I was left wondering how well they matched human performance. As suggested above, demonstrating the degree that C-HORSE actually matches human performance is key to understanding how well this new model truly accounts for human learning. As is, it is difficult to evaluate with this explicit comparison.

Reviewer #2 (Recommendations for the authors):

This model does come from a long 'lineage of models developed to account for episodic memory phenomena', and those should be more extensively cited (rather than only including papers authored or co-authored by Randy O'Reilly). I would suggest Marr (1971) Phil Trans B at the very least, and I think Gluck and Myers (1993) Hippocampus is also particularly relevant

The Discussion is far too long (thirteen and a half pages, about half of the total length of the manuscript). Please try and reduce the word count by sticking to the most pertinent issues

The authors state that the "monosynaptic pathway … was responsible for detecting the regularities that define category structure" and, later, that "the MSP was critical for learning the regularities underlying category structure and was responsible for generalization of knowledge to novel exemplars", but their results show that simulations with the TSP alone consistently perform better than chance on tests of either function (e.g. Figure 3A-C, 4B, 5B). As such, these statements appear to misrepresent the results. Please clarify

Reviewer #3 (Recommendations for the authors):

1. The one analysis that seems missing is analysis of generalization in Task 3 based on typicality. It would be informative, especially given that the training data showed interesting dissociations based on typicality.

2. I did not understand the relationship between time and performance during test in Task 1 and Task 3, where there are distinct training and test phases. I thought there are no labels and no weight adjustments at this stage. Why is the already trained network starting at chance at generalization test and then improve? How can we reconcile it with human performance that does not show such test accuracy pattern?

3. The clarity and flow of writing was exceptional, further enhancing interesting content, making this one of my favorite reviews this year. I did find a few challenging sentences, which perhaps could use rewording for clarity. I also found a couple of details that I would like clarified.

– Lines 66-69 could be split into two sentences, one defining complementary learning systems, another noting it may exist within hippocampus itself in distinct pathways. As written, it was confusing.

– Consider whether TSP and MSP abbreviations are necessary or if the words trisynaptic and monosynaptic could be spelt out each time instead (I am aware of the frequency, so this is just for consideration).

Methods details:

– Line 149 could add rationale for the distinct number of units in the different hidden layers

– Line 151 could mention the weight constraints

– Line 173 could explain "clamped" in non-technical terms

– Line 333/388 could explain why each category was represented by 2 units/5 units

– The additional task visualizations for task 2 and task 3 in Figure 2 were very helpful (the outcomes and %chance for cards combinations, the feature value visualization using the circles in task 3). Perhaps they could be explained more in the legend.

4. Connection to other work:

Line 53 puts up the idea that hippocampus may be well suited for category learning after all. It may be worth referencing a couple recent review papers that made the same point (e.g., Mack et al. 2018; Zeithamova and Bowman, 2020).

Line 293-296 Big Loop Recurrence could reference Koster et al., 2018.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A neural network model of hippocampal contributions to category learning" for further consideration by eLife. Your revised article has been re-reviewed by one of the original reviewers and evaluated by Michael Frank (Senior Editor) and a Reviewing Editor.

We found that you were highly responsive to the previous comments and the manuscript has been significantly improved. There are only a couple of remaining issues that should be addressed, as outlined below:

1. The representation of exemplars and common features in your network could be made more intuitively understandable with the help of an illustration. For example, you could add another row to Figure 2A (or possibly 2B) that shows activity in the input layer to EC_in (which is clamped throughout learning), illustrating the activity pattern for each exemplar in one category. This is currently given in Supplementary Table 1A, but it would be useful to have it in the main text. Illustration of just one category would be sufficient to illustrate the pattern of activity across exemplars and perhaps also get a better idea of how the "classification" performance is evaluated in the network. This would complement the symbolic illustration of the exemplars, unique features and shared features from the three categories this is already a helpful part of Figure 2A. Alternatively, more information can be provided in the text.

2. The category structure effects are relatively subtle in Figure 4e and would benefit from a summary representation that more explicitly highlights their presence or absence in the different subfields. Adding a visual or numerical summary report of within-category vs. between-category similarity would be beneficial.

3. The Koster et al., 2018 citation was only added in the response letter but not the revised manuscript.
