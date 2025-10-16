# Peer review - Round 1

Editors:
- Jennifer Flegg, https://ror.org/01ej9dk98 The University of Melbourne Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72626.sa0](https://doi.org/10.7554/eLife.72626.sa0)

This paper presents a mathematical model for prioritizing drugs for prostate cancer patients based on signal network database. The manuscript is of broad interest to the field of oncology and precision medicine. The methodology developed is sophisticated and relevant to real patient prostate cancer data. The predictions from the model are validated in an experimental setting and provide suggestions for the personalisation of prostate cancer treatment. The study can serve as a roadmap for future development of predictive, personalized models.


---

# Peer review - Round 1

Editors:
- Jennifer Flegg, https://ror.org/01ej9dk98 The University of Melbourne Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72626.sa1](https://doi.org/10.7554/eLife.72626.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Patient–specific Boolean models of signaling networks guide personalized treatments" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Réka Albert (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The main limitation is that the bioinformatics conclusion was validated using only one cell line experimentally. The authors might consider how to consolidate the general utility of this model.

2. Another major limitation is that this model points to the existing drug targets as highlighted in the signal databases. Is it possible to identify new drug targets? When there are multiple reagents hitting the same drug target, can it advise which chemical to use? The authors should comment on this limitation.

3. The authors should comment on the contribution of tumor microenvironment, and whether this model could address this issue since it seems mainly built on signaling in tumor cells.

4. The author used Monte–Carlo kinetic algorithm to generate the time trajectories for the state transition graph and set a maximum time to ensure an asymptotic solution. It would be better to provide more detail of situations if an asymptotic solution cannot be found or such solution can always be found and converge to the same result.

5. The author has not mentioned enough detail about the transition probability between states (e.g., does the transition probability based on prior knowledge, will the transition probability, will the transition probability change when constructing a personalized Boolean model, and how does it change if it changes). It will be good if the authors can provide a transition probability matrix as an example, and any influence from prior knowledge.

6. In the supplementary information, "Personalized Boolean model of prostate cell lines" section, the plots (S19/S20) used simulation result from random initial condition, does that mean the result is independent of the choice of initial condition? It would be helpful if the author could analyze the influence of the model output with different initial conditions (e.g., whether it will converge to the same results or different ones).

7. Why does the cell viability increase with drug (e.g. 2nM) compared to no drug (i.e. 0 nM) in Figure 7? Do the drugs promote proliferation in small doses?

8. It would be good to test the drug concentration cell viability experiment for larger doses of drug so we can actually see the maximal efficacy of these drugs. It seems for some of the drugs they don't even achieve their half–effect in the doses tested. Is there a reason for this choice?

9. Indicating the general criteria for the logical rules and giving an example in the Appendix would help a lot.

10. Text queries/suggestions:

– Figure 2, when the authors say phenotypes, is this also the 6 variable outputs that they mention in the text? If so, it might be good to say this in the caption so it's clear to readers.

– It's challenging to really fully grasp the full model, I think the readers would benefit from more reference to appropriate sections of the supplementary material.

– Can you elaborate on how the combined perturbations for already–developed drugs was performed? How was the model changed for a given drug combination?

– What is EGF, FGF, TGF etc? Are these acronyms? Since they are "physiological conditions of interest" it might be good for the readers to know what these represent.

– When you say "the final model accounts for 133 nodes and 449 edges" can this be linked to its biological counterpart. i.e. Is this then 133 proteins and 449 protein–protein pathways/interactions?

– '…such data can only be obtained with non–standard procedures such as microfluidics from patients' material ': The authors should make it clear about what kind of information is missing from those data making those mode unavailable.

– The author should clearly specify the number of pathways, genes, and cross–talks involved in their models. It is unclear how many components were integrated into the network to obtain the final network containing 133 nodes and 449 edges. Please also specify how many drugs and drug combinations participated in personalised drug prediction. The authors should clarify the number of drug and drug combination instead of the word of " several".

11. Figures queries/suggestions:

– Figure S1 the text cannot be read; it needs to be larger and the graphic needs to be higher quality.

– Figure 2 should also be much bigger, it's too difficult to make out the blue rectangles and in turn most of the paths are difficult to discern.

– Meaning for acronyms in Figure 4 should be given before they are used, i.e. PCA and GG.

– Provided more details of what is mean by Cell index (a.u.) in Figure 8 and Figure 9 in the caption.

– A figure summarising the combined treatment effects for the different patients with a figure to demonstrate how AKT was the top hit in Gleason Groups 1, 2 and 3 and so on, would be helpful.

– What is the strange dynamic occurring at about 15 hours where the points shift down and then jump back up?

– Figure3: Why there were a sharp increase of several elements before the decay for those output with 0 activities in the final states? Why the kinetics of decaying varied across different nodes? Any interpretation?

– Figure 4: The correlation between the Gleason scores and Proliferation score is not clear by the graphics. Any other means to show this?

– Figure 8/9 BCD/FGH seem redundant with Figure 8/9 A/E. You can combine the two types of figures. Also, there seems a discontinuous segment in Figure8/9A/E. Is it an editing error of images? You may consider integrate them as a whole panel.

Reviewer #1 (Recommendations for the authors):

Below are some queries/comments I have for the authors.

General queries:

– Why does the cell viability increase with drug (e.g. 2nM) compared to no drug (i.e. 0 nM) in Figure 7? Do the drugs promote proliferation in small doses?

– It would be good to test the drug concentration cell viability experiment for larger doses of drug so we can actually see the maximal efficacy of these drugs. It seems for some of the drugs they don't even achieve their half-effect in the doses tested. Is there a reason for this choice?

Text queries/suggestions:

– Figure 2, when the authors say phenotypes, is this also the 6 variable outputs that they mention in the text? If so, it might be good to say this in the caption so it's clear to readers

– It's challenging to really fully grasp the full model, I think the readers would benefit from more reference to appropriate sections of the supplementary material

– Can you elaborate on how the combined perturbations for already-developed drugs was performed? How was the model changed for a given drug combination?

– What is EGF, FGF, TGF etc? Are these acronyms? Since they are "physiological conditions of interest" it might be good for the readers to know what these represent

– When you say "the final model accounts for 133 nodes and 449 edges" can this be linked to its biological counterpart. i.e. Is this then 133 proteins and 449 protein-protein pathways/interactions?

Figures queries/suggestions:

– Figure S1 the text cannot be read; it needs to be larger and the graphic needs to be higher quality

– Figure 2 should also be much bigger, it's too difficult to make out the blue rectangles and in turn most of the paths are difficult to discern.

– Meaning for acronyms in Figure 4 should be given before they are used, i.e. PCA and GG.

– Provided more details of what is mean by Cell index (a.u.) in Figure 8 and Figure 9 in the caption

– A figure summarising the combined treatment effects for the different patients with a figure to demonstrate how AKT was the top hit in Gleason Groups 1, 2 and 3 and so on, would be helpful

– What is the strange dynamic occurring at about 15 hours where the points shift down and then jump back up?

Reviewer #2 (Recommendations for the authors):

Indicating the general criteria for the logical rules and giving an example in the Appendix would help a lot.

Reviewer #3 (Recommendations for the authors):

1. The main limitation is that the bioinformatics conclusion was validated using only one cell line experimentally. The authors might consider how to consolidate the general utility of this model.

2. Another major limitation is that this model points to the existing drug targets as highlighted in the signal databases. Is it possible to identify new drug targets? When there are multiple reagents hitting the same drug target, can it advise which chemical to use? The authors should comment on this limitation.

3. The authors should comment on the contribution of tumor microenvironment, and whether this model could address this issue since it seems mainly built on signaling in tumor cells.

4. The author used Monte-Carlo kinetic algorithm to generate the time trajectories for the state transition graph and set a maximum time to ensure an asymptotic solution. It would be better to provide more detail of situations if an asymptotic solution can not be found or such solution can always be found and converge to the same result.

5. The author has not mentioned enough detail about the transition probability between states (e.g., does the transition probability based on prior knowledge, will the transition probability, will the transition probability change when constructing a personalized Boolean model, and how does it change if it changes). It will be good if the authors can provide a transition probability matrix as an example, and any influence from prior knowledge.

6. In the supplementary information, "Personalized Boolean model of prostate cell lines" section, the plots (S19/S20) used simulation result from random initial condition, does that mean the result is independent of the choice of initial condition? It would be helpful if the author could analyze the influence of the model output with different initial conditions (e.g., whether it will converge to the same results or different ones).
