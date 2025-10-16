# Peer review - Round 1

Editors:
- Ronald L Calabrese, Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.33281.018](https://doi.org/10.7554/eLife.33281.018)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Structural and functional properties of a probabilistic model of neuronal connectivity in a simple locomotor network" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom, Ronald Calabrese is a member of our Board of Reviewing Editors and the evaluation has been overseen by Timothy Behrens as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript reports on a modeling approach for building network models based on connectomics data. Using a developmental (anatomical) model of the Xenopus hatchling tadpole spinal cord connectome, the authors generated 1,000 conectomes from which they derive a complete probability matrix of connections in the spinal cord. From this probability matrix (probabilistic model) they then generate ensembles of 100 connectomes (model instances) to simulate based on previous functional models of swimming activity. They find that these instances of the probabilistic model are indeed functional and more robust that models based on developmental model connectomes, which they attribute to lower variance among connectomes for the probabilistic model. They then analyze these model instances to determine functional properties of the swim network, for example showing that the network does not appear to have hub neurons as an organizing principle and explicating how activity in a hemi-network arises. The technique may applicable to connectomics data and provide valuable insights that could benefit both modelers and experimentalists in the field.

Essential revisions:

The reviewers had partially overlapping concerns, which we have tried to combine as much as possible, but some overlap will still be noted in the required revisions below that represent a strong consensus. All minor concerns from the expert reviewers should also be addressed.

1) Both introduction and discussion mention the probabilistic model extracts fundamental structural features. However, the model consists of a cell-level probability matrix, which suggests these structural features may not be so fundamental but specific to the particular assumptions in this circuit model. Furthermore, since the probabilistic model is derived from another model (the anatomical) and not directly from experimental data, it is not clear whether it might just be capturing properties of this anatomical model that don't really generalize to the real system. Moreover, because the probabilistic description is cell-wise, it may just reflect an overfitting to the anatomical model. The authors should provide further justification of (1) how well the anatomical model captures the real system, and (2) why/how the probability model is capturing fundamental structure features, despite being at a cell-level granularity. This will also help determine how significant/valid the analyses and predictions made by the model are.

2) The analysis of generative models of neuronal networks is a promising avenue to explore links between development, structure and function. However, we find it difficult to understand the results of this paper relative to the Roberts et al., 2014 work on which it builds. We encourage the authors to either restructure the paper in a way that clarifies not only the differences from the previous model, but the advances in the current work and whether they arise from new computational experiments or the new modeling approach.

Once this clarification is achieved then it will be important to show the significance of some of the conclusions. For example, the fact that all connectomes achieve swimming or "this pathological mid-cycle spiking is significantly reduced in probabilistic connectomes" need to be contextualized. Since the probability matrix was directly extracted by averaging over anatomical model instances (all of which showed swimming and no pathologies), perhaps it is not surprising that they show similar properties.

3) While the Bernoulli trial formulation in principle admits more analytical analysis, it is primarily used to compute in- and out-degrees that could just as easily be computed from direct consideration of the results of the anatomical model. As a result, the probabilistic model is a particularly complex null model that captures many aspects of dynamics and not others, but in ways that are only weakly controlled.

In particular, it is not clear why it is better to analyze the ensemble average properties of individual nodes from the probabilistic model rather than analyze the distribution of results from the previous anatomical model. The strongest observation is in subsection “Functional properties of the model: reliable swimming”, effectively relating the swim period to the variance in in-degree of cINs. In the probabilistic model, the use of a binomial distribution implicitly links mean and variance in a way that clearly isn't true of the anatomical model and is shown meaningful impact on the resulting dynamics. This result could be greatly strengthened, if the authors used a random process where variance could be defined separately from the mean and thus this relationship explored explicitly.

4) The last paragraph in the Discussion section makes it seem as if the authors are proposing a novel methodology. However, this novelty is not clear since employing probability matrices to define models is a standard practice: it’s a feature included in several major neural simulators (NEST, Brian, Moose,.…), and many existing models (e.g. on ModelDB) employ prob matrices, either at a population-level or cell-level (for small networks and when enough exp data is available).

5) Authors should include more details about the functional model employed since this is crucial for understanding the results (e.g. low connection weights can drastically alter the effect of high connection probabilities). A table with the main parameters used in the functional model should be included. Additionally, authors must share all the model and analysis code -- this is common practice nowadays in computational neuroscience to ensure replicability and reproducibility.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Structural and functional properties of a probabilistic model of neuronal connectivity in a simple locomotor network" for further consideration at eLife. Your revised article has been favorably evaluated by Timothy Behrens (Senior editor), a Reviewing editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) The explanation of why the probabilistic model is an advance over the anatomical model is not yet convincing. Looking at both the response to the reviewers and the argument in the Introduction, it still seems that the same results could have been obtained by consideration of the distribution of networks generated by the anatomical model. The authors must clarify why they emphasize the need to construct the probabilistic matrix as a new step in the analysis process, otherwise averaging the outcome of an existing model and putting into a simple probabilistic framework is a modest and intuitive extension of the previous work without added value.

2) The authors have not fully addressed the issue of why the cell-level probabilistic model is capturing general/fundamental structural features of the tadpole network and not overfitting.

Without addressing these two issues more thoroughly, the impact of the paper rides on its scientific results, connecting the structure of the model to key aspects of its functional output and the authors' emphasis on method is misplaced. Some clarifying points from the expert reviews are presented below.

Reviewer #3:

I don't think the authors have addressed the issue of why the cell-level probabilistic model is capturing general/fundamental structural features of the tadpole network and not overfitting. They argue that it is the result of averaging over 1000 anatomical model connectomes, but these are still a model, e.g. they have a fixed number of neurons for each population, which is not the case for real tadpole networks, and so describing the structure at the cell-level prevents it from being applicable to specimens with a different number of neurons. They also argue that all connectomes achieve reliable swimming, but I fail to see how this is relevant. I think the paper still has value despite this limitation, but I think it should be clearly stated in the paper.
