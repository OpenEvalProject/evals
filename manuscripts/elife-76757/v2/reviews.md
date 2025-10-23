# Peer review - Round 1

Editors:
- Felix Campelo, The Barcelona Institute of Science and Technology Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76757.sa0](https://doi.org/10.7554/eLife.76757.sa0)

This article contributes to an important and largely unexplored topic in cell biology: the understanding of glycosylation. The authors introduce a mathematical model of glycosylation in the Golgi apparatus and use the model to investigate how the complexity (diversity) and fidelity of the plasma membrane glycan distribution depend on parameters such as the number of Golgi cisternae or enzyme specificity. The article is well written and makes the effort to present a rather complex topic in an accessible way by leaving some of the details in the appendices.


---

# Peer review - Round 1

Editors:
- Felix Campelo, The Barcelona Institute of Science and Technology Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76757.sa1](https://doi.org/10.7554/eLife.76757.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Glycan processing in the Golgi – optimal information coding and constraints on cisternal number and enzyme specificity" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

This manuscript presents a clever approach to study from a theoretical point of view how glycosylation reactions occurring at the Golgi membranes define a cell-specific glycan profile. In particular, by optimizing a metric, the authors find that larger number of enzymes and/or compartments (Golgi cisternae) are required for increasingly complex glycan profiles. In addition, they found that enzymes should not be very specific nor too sloppy. This manuscript touches upon an important topic in cell biology (origin of glycan diversity and link to Golgi complex architecture), which has been relatively unexplored in the past. However, although there are no major concerns about the validity of the model presented in the paper (see separate reviews for more detailed comments), there is a general consensus among the reviewers that there are some key points that this manuscript should resolve before opting for publication at eLife. Since these points will most likely require an extensive revision of the manuscript, we decided to proceed with a rejection at this moment. We encourage you, if you wish, to resubmit a stronger new paper in the future; or to opt for submission elsewhere for its timely publication.

The main concerns raised by the reviewers are the following:

1) It is not clear what new biology we learn from the results of this paper (see e.g. Rev. 1's report). It's been suggested that the reason for stacking is to give proteins enough time to undergo proper glycosylation and that cisternae number correlates with the complexity of glycans. Since the paper does not include any new experimental evidence on how the complexity of cellular glycans leads to more cisternae in the Golgi stack, it would be very valuable for a biological audience if the authors could present a list of model predictions that could be experimentally tested.

2) For the results of the model to be more robust and probably to also learn a bit more about cell specific glycobiology, a more systematic study of available glycan profiles would very much improve the story (see in particular, Rev. 2, point 2; and also Rev. 3, point 3).

3) The manuscript is very complex for non theorists, since it is presented as a rather technical manuscript. It is well written and organized for specialists. However, it is not clear whether this manuscript, in the current form, will be of interest for a broad biological audience. Along these lines, the conclusions and discussion might need to be toned down, given the large number of simplifications of the model (which is fine for a theoretical audience, but could be over-assumed by a non-specialist biological audience) (see Rev. 3, point 1).

Reviewer #1:

The manuscript by Yadav et al. uses a theoretical model of glycan processing to investigate the constraints placed on the enzymatic modification process in order to achieve the complex final glycan distribution. The authors introduce a multi-compartment, many-species model of chemical modifications and develop an optimization algorithm to minimize the divergence between the resulting glycan distribution and that observed from data on immune cells. The authors find that a minimum number of enzymes and reactions chambers (cisternae) are necessary to recapitulate the complex features of the experimental distribution. They also find that enzymes should have an optimal specificity: they should not be too specific to only one particular substrate, nor should they be too "sloppy" by interacting with all substrates with similar rates. Finally, the authors elucidate control parameters of their model that maximize the diversity of glycans.

I am torn about this study because while the approach is elegant and principled and the results sensible and interpretable, the scope is rather technical and therefore I am skeptical as to whether this will have the broad audience and impact that is expected for eLife. The work combines elements from several fields (cell biology, chemical modeling, computational optimization, information theory), which is commendable, well-presented, and appropriate for an interdisciplinary audience. At the same time, however, I found myself wondering what we really learn at the end of the day. That the components must be complex (sufficient number of enzymes and compartments) in order for the result to be complex (many-peaked glycan distribution) seems unavoidable. That the specificity must be moderate also seems expected in order to not be limited by a one-to-one matching between enzyme and glycan product, but also not produce a broad, sloppy distribution. Part of the problem may also be that it is unclear what contribution is made in terms of predictions for new experiments (which is often a necessary criterion for a high-impact theoretical study): apart from using actual data as an optimization target, the study largely recapitulates and rationalizes existing features of the glycan machinery, rather than suggesting perturbations for, or placing quantitative limits on, new experimental investigations. My inclination is therefore to suspect that this work may be more suitable for a more specialized journal, e.g. on cell biology or chemical physics.

Reviewer #2:

The manuscript "Glycan processing in the Golgi – optimal information coding and constraints on cisternal number and enzyme specificity" by Yadav et al. presents a model for glycan production by the Golgi cisternae. Glycans serve various cellular functions, such as markers for cell identity, and it is important that a function-specific profile (distribution) of glycans is obtained at the end of the production process. The authors show how to choose the reaction constants in their model to reach a target profile (distribution) of glycans. They discuss how the adequacy between the target and model profiles depend on the physico-chemical features of the reactants.

While the problem studied by the authors is interesting and their analysis reports valuable qualitative results, e.g. on the consequence of enzyme specificity on the profile statistics, I list below various points that I think would require further studies and discussions:

1. The writing of the manuscript is quite technical in some sections, in particular around equation (5) and (6), and involves superfluous notations: what is the added value in introducing V, M, L with respect to the already defined omega, P, …? I would recommend the authors to simplify the writing and really emphasize what is important here. Several definitions or assumptions remain vague and not discussed. For instance, equation (3) define the binding probability between enzyme α and substrate k in terms of "shape" vectors. On line 250 these shape vectors are defined as scalars, in particular the shape of enzyme k is identified with the index itself. Why is this a good choice (apart from reducing the dimension of the parameter space), and how could one test the validity this apparently quite strong hypothesis?

2. The manuscript is mostly theoretical with limited connections with experimental data and validations. It would be nice to have a systematic study of available glycan profiles and comparison of the corresponding inferred model parameters. In addition, it is necessary to validate the inference/optimization procedure on synthetic profiles generated by stochastic simulations of some prescribed network, to check that the correct network parameters are correctly recovered (or some other solutions giving back the same profile, see point 4 below).

3. While the KL divergence (7) is a reasonable measure of dissimilarity between two distributions the relevance of the ratio (9) on page 10 is not at all clear to me. More precisely, I do not see why the entropy of the target distribution is the relevant quantity here. Rather the KL divergence between the model and target distribution could be compared to the mean value of the KL divergence between any two glycan profiles resulting from the noisy production steps.

4. Since the function of the minimize over, see eq. (8) is non convex, there may exist many local minima. The authors report in Appendix 8 they perform grid-like search. How close are those minima in terms of the objective function? This question is important as the model studied here seems to be overparametrized, in particular when N_c is large. It may also be relevant in terms of evolution. More precisely, how were some glycan profiles and the corresponding biochemical networks selected in the course of evolution? On top of selection pressure to "orthogonalize" the profiles is it possible that some distributions are (approximately) realized by more networks than others and were therefore entropically favored?

Reviewer #3:

The paper by Yadav et al. contributes to an important and largely unexplored topic in Life Sciences, namely, to the understanding of glycosylation. The authors introduce a mathematical model of glycosylation in the Golgi apparatus and use the model to investigate how the complexity (diversity) and fidelity of the plasma membrane glycan distribution depends on parameters such as the number of Golgi cisternae or enzyme specificity. The paper is well written and makes the effort to present a rather complex topic in an accessible way by leaving some of the details in the appendices.

After defining the quantitative measures for complexity and fidelity of glycan distributions, the paper builds a general model of glycosylation in the Golgi by assuming Michaelis-Menten type reactions and by taking into account parameters such as the number, specificity and distribution of enzymes across cisternae. However, the parameter space becomes so large that, before solving it numerically, the authors need to reduce it by making a number of simplifications (they linearize the distortion energy; assign one enzyme specificity σ to all reactions …). The authors then ask the question how different parameters influence the outcome and what are the optimal parameters for a given target glycan distribution. Finally, the authors explore the strategies to achieve high glycan diversity.

My comments are listed below:

1. The authors should be more careful (modest?) with the generalization of their results and conclusions. The results are obtained by a very simplified model and it is not obvious that they can be generalized.

For example, in the Abstract they state: "We find that to synthesize complex distributions, such as those observed in real cells, one needs to have multiple cisternae and precise enzyme partitioning in the Golgi." However, this is only true within the simplified model. Maybe, complex distributions could be obtained even with a small number of cisternae if one allowed biochemistry that is more complex. The statement above would be more accurate if it was turned around, e.g., "we show that multiple cisternae and precise enzyme partitioning in the Golgi can lead to complex glycan distributions."

The readers of a mathematical journal would very well understand that the results are not general but should be interpreted within the model proposed. On the other hand, the readers of eLife could be misled by statements which are too general. This is even more true for this paper, which starts with a rather general and complex model and then simplifies it on the go. While the authors do summarize the simplifications in the Discussion, an inexperienced reader could still miss them and take the results too literally. I would suggest that the authors amend the whole paper according to this comment to avoid possible misinterpretations.

2. An interesting result of the modeling is that the role of parameters NE and NC can be rather symmetrical – the fidelity of glycan distribution can be improved in a similar way by increasing either of these parameters (Figure 4). Why is that? Is this a consequence of a symmetrical role of these parameters in the reduced (simplified) parameter space, or can this symmetry be generalized and can have a biological merit?

3. The paper mentions examples of cells that have a complex Golgi and a complex glycan distribution. Is the opposite also true, e.g., that cells with a simple Golgi do not have complex glycan distributions? Or can a complex Golgi sometimes result in a low glycan complexity?

4. One wonders how robust the glycosylation process is according to the model proposed? Figure 5b neatly shows that large enzyme repartitioning can lead to a completely different glycan distribution. But how do small variations of the optimal reaction distribution affect the outcome? Would it be possible to quantify the robustness and analyze it systematically (not just show a few random examples)? How is robustness affected by the number of cisternae and enzymes? What are biological implications of this result?

5. Figure 5b shows that a complex Golgi can also lead to a simple glycan distribution. This implies that having a large NC and NE is not sufficient for a complex glycan distribution. Could the authors discuss this? What are additional requirements that are needed for a complex glycan distribution?

6. What is "likelihood," which is used in some of the graphs? Is it related to the minimum achievable Kullback-Leibler (KL) divergence according to Kullback-Leibler metric defined in Eq. 7 (and used in Figures 3, 4 and 5)? If so, the authors could use only one measure of likelihood/divergence in all the graphs.

7. Why does the mouse glycan distribution have a lower "likelihood" than the human one, even with an increasing number of GMM (Figure 1b)? Is this a coincidence or can this be generalized?

8. The paper would be easier to read if all the parameters were listed in one place, and if one letter was not used to denote different things (e.g., "k" denotes complexity, but it is also used as the index for glycosylation reactions).

9. Is the final distribution of glycans on PM presented on the right in Figure 2 conceptually the same as the glycan distributions presented in Figure 1? If so, use the same notation (and axes labels) everywhere.
