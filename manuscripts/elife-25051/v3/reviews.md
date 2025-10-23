# Peer review - Round 1

Editors:
- Bruce Levin, Emory University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.25051.050](https://doi.org/10.7554/eLife.25051.050)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "The validity of pairwise models in predicting community dynamics" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor, Bruce R. Levin, and a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

This review and editorial decision, has two elements. Part 1 has been put together by the Reviewing editor but is the product of a discussion between the editor and the reviewers. Part 2 are the separate comments and suggestions of the reviewers. There is a fair amount of overlap. BRL agrees with all of the critical comments and suggestions of the reviewers. Following our discussion, BRL sent the first part of this recommendation to the reviewers. Save for a typo, they approved of this collective review and recommendation.

Part 1.

Recommendation:

The subject of this report is right on. In addition to the considerable industrial and ecological and medical interest in bacterial communities, thanks to the "microbiome mania" the need to understand the processes that determine and maintain the structure of these communities has become increasingly important. Central to acquiring this understanding will doubtless be mathematical and/or computer simulations models of the population and evolutionary dynamics of bacteria and the interactions between these populations and the physical, chemical and biotic factors that determine their densities and relative frequencies in communities. How to construct and analyze the properties of these models is not at all clear at this time; the long-standing fissure between population and community ecology has yet to be breached. This report considers the problems of modeling bacterial populations and communities.

As trendy and important as this subject is, we don't consider this report to be of sufficient general interest to be published in ELife. Although it may be of interest to some theoreticians, we believe it would be of little interest and utility to population and evolutionary biologists and biometricians doing experimental or other empirical research with bacteria and bacterial communities. It is too abstract and doesn't address specific questions. Some readers may also see it as a complex, equation illustrated rant telling them what they already know about the limitations of pairwise models. We believe it would be more suitable for a fine but more specialized journal like PLoS Computational Biology, where the readers will be more attune to mathematical modeling of the sort considered in this report.

Collective comments and suggestions:

1) – We agree with the George Box adage, "All models are wrong, some are useful". However, we don't see how their pairwise models would be useful for understanding the processes that determine "distribution and abundance" of bacterial strains and species in communities. To be sure, even without understanding the mechanisms responsible, it would be useful to be able to predict the distribution and abundance of species from empirical estimates of the parameter of these "pairwise" models. But as we see this report as a cautionary tale saying that it is unlikely that pairwise models will be able to achieve these ends much beyond three species and if that. Moreover, even if it were possible to provide predictive pairwise models for specific simple communities, perhaps the macrobiotic of yogurt, there would be little or no generality, like to cheese or bread starters, much less natural communities.

2) Arguably (not to BRL) mechanistic models are most useful when they are wrong, when there are substantial qualitative rather than just small quantitative differences between the predictions of the model and observations in the empirical studies. That way one knows that there are fundamental errors in the biological, chemical and environmental assumptions upon which the model was based. In the best of cases, a wrong mechanistic model will point to the biological and other assumptions that have to be modified to obtain a better fit and thereby increase our understanding of the mechanisms responsible for the phenomenon under study. It is not clear how the pairwise models of the sort they are considering could achieve this end when they fit or don't fit.

3) What one means by a "mechanistic model" and mechanisms in general is in the eyes, mind and perspective of the beholder. The authors can do a better job of providing the readers with a clear distinction between what they mean by pairwise rather than mechanistic models. They present the logistic model and its extensions, like the Gause competition models, as pairwise rather than mechanistic models. We agree, but some may not. These models make the reasonable assumption that the rate of growth of populations decline as they approach the point of saturation of the environment, the parameter K. But the authors and most others interpret that parameter to reflect resource limitation, which seems mechanistic albeit not explicit in the model. Moreover, the ecological nature of the equilibrium in Logistic models and its extensions is not defined. Is that equilibrium, K, the density at stationary phase in batch culture? Or is the population at equilibrium in an environment in which resources are continually made available and bacteria and wastes are continually being removed, like a chemostat or turbidostat?

4) There is a real need to develop models that deal with the inconvenient reality of the physical structure of real habitats of bacteria. The ODE mechanistic and pairwise models considered in this report do not address this reality, which doubtless contributes to the distribution and abundance of species and strains of bacteria in natural communities.

Part 2.

Reviewer #1:

In this work, the authors study the validity of utilizing phenomenological models of pairwise interactions to describe the dynamics of ecological communities. To do so, they employ theory and simulations to compare the dynamics of detailed mechanistic models to the ones of appropriately parameterized pairwise models.

Improving our understanding of the capabilities and limitations of pairwise models is an important and timely goal, especially given their recent popularity in modeling microbial communities. I also appreciate the authors' approach of trying to delineate the types of mechanistic situations in which the pairwise approximation is valid.

However, the aspects of the problem that the authors focused on are not always the ones I feel are the most interesting and useful. Specifically, the authors focused on identifying situations in which a specific pairwise model can provide an exact description of the community dynamics. It is not surprising that phenomenological pairwise models often fail to capture exactly the dynamics of more complex mechanistic models. Nonetheless, there may be many situations where they are still useful, either by providing approximate description of the dynamics, or by capturing important qualitative features, such as the existence of oscillations, the set of coexisting species, presence of alternative stable states, etc. To me, understanding the conditions under which pairwise models are not even approximately correct, or make qualitatively wrong prediction is one of the important outstanding challenges in community modeling. I would encourage the authors to use their approach to provide insight into these questions, but, at the very least, they should clarify the difference between different failures of pairwise models. Additionally, they should be more explicit about cases in which no pairwise model would capture the community dynamics (e.g. in cases of interaction modification, or higher order interaction), versus ones in which the pairwise model that was considered wasn't adequate, but there may be a different one that is.

The authors also do not consider cases where interactions are mediated by externally supplied, abiotic mediators, rather than ones produced by the species themselves. The author's model is an extension of MacArthur's competition model, whose link to pairwise models have been extensively studied (e.g. Chesson, P. "MacArthur's Consumer Resource Model." Theoretical Population Biology 37, no. 1 (1990): 2638.).

What is not captured is competition of abiotic resources, such as the models common in David Tilman's work. The authors should make these distinctions clear, and put their work in the context of previous work. I also believe that extending the work to include competition for abiotic resources would add significant value to the work.

Reviewer #2:

The work of Momeni et al. "The validity of pairwise models in predicting community dynamics" explores conditions under which mechanistic models of species interacting via chemical mediators can be reduced to pairwise models. Pairwise models do not require a full mechanistic understanding of the nature of interactions within the community and thus use fewer parameters, which is why they are often used. The authors report that in many cases, pairwise models fail to predict, quantitatively or qualitatively, the dynamics of many species communities, which is why they should be used with caution. The authors do a good job in exploring the various scenarios under which pairwise models are not sufficient to capture these dynamics.

A point that deserves more attention however is how these results are immediately relevant for past and future studies of microbial communities? The authors provide references to several studies that employed pairwise models to simulate community dynamics. However, many of those do not model chemically mediated interactions, but rather direct interactions, such as the predator prey examples mentioned in the introduction and are thus not directly relevant to what is studied here. Can the authors provide more specific examples of works that employ pairwise models to model chemically mediated interactions?

The authors clearly describe several regimes under which pairwise models fail. However, to identify whether the community being modeled falls into these regimes, one often needs to have a quite detailed mechanistic understanding of the interactions within the community in the first place. What would then be the advantages of using a pairwise model, given that this information is available? Also, it is not clear if this is an exhaustive list of regimes that they look at or are there other regimes out there to be explored? Thus, we are left with a conundrum that the work does not address: why the results are useful for systems where we do not know all the details of the interactions?

In general, for dynamical systems it is not at all surprising that 'the devil is in the details' of interactions for many a system, as weak couplings can often have important roles. Especially for systems that are under evolutionary pressure I can see how small couplings can be essential. Thus, models with underdetermined number of parameters will often fail, especially as long as the main state variables of a system are unknown, or when these tend to shift in importance from system to system.

Thus, to me the strong 'punch' in the message of the paper is missing, especially for a wider audience outside of the ecology crowd.

As a reviewer I am part of this outside audience I am not an ecologist nor am I a theorist.
