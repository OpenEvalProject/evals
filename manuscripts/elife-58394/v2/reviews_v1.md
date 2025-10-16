# Peer review - Round 1

Editors:
- Naama Barkai, Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58394.sa1](https://doi.org/10.7554/eLife.58394.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your work entitled "Effective dynamics of nucleosome configurations at the yeast PHO5 promoter" for consideration by eLife. Your article has been reviewed by three peer reviewers and the evaluation has been overseen by Naama Barkai as the Senior and Reviewing Editor.

There are some issues that need to be addressed before acceptance, as outlined below:

As you will see below, the reviewers appreciated the work and the simplified theoretical treatment. However, the reviewers have concerns about the gap between the modelling results and the biological discussion. It is important that the Discussion will be revised to be more a simplified and "user friendly" Discussion and highlight key experimental predictions. in particular, it is important to explain in more detail how the "assembly-centric" suggestion in the Discussion may be experimentally tested in the light of your models.

In addition, please revise the paper to account for all points mentioned in the point-to-point reviews below.

Reviewer #1:

The manuscript under consideration puts forward a beautiful Markovian model of promoter regulation via nucleosome assembly/disassembly/sliding. The model is applied to the yeast PHO5 promoter, for which experimental measurements are available and are being used to specify the final models from the space of possible ones. The final models agree on certain features, and these constitute the result of the analysis. The modeling process is clean and parsimonious. The authors' claim of an unbiased process is indeed convincing in that only likelihood distinguishes from among many alternatives.

There is one issue which requires clarification. The likelihood ratio is used to select preferable models. However, the models compared have different number of parameters. Why not use a penalized likelihood, e.g., BIC or AIC? The underlying problem is that the large number of models has a downside: While it avoids modeling bias, it introduces an unwanted multiple testing problem.

Overall, the paper is technically very convincing and the integration of the experimental data into the modeling process is excellent.

Figures are clear and informative.

In terms of language, the authors speak of "fit parameter". It would be better to use "fitted" to avoid possible confusion with "fit" like in "fitness".

Reviewer #2:

In this work, authors study dynamics nucleosome configurations in the promoter region of yeast PHO5 gene. Authors examine published experimental data describing positioning of three nucleosomes in PHO5 promoters. A few years ago, experiments by Brown et al. and Small et al. have quantified probabilities of finding eight possible nucleosome configurations when the gene is in different states like active or repressed. There are a few existing mathematical and computational models that examine PHO5 gene regulation in the context of this data.

In this work, authors present a comprehensive and systematic approach towards enumerating all possible models, given the data, and have classified the models based on their agreement with the experimental data. Authors consider dynamics of nucleosomes among the 8 discrete states via assembly, disassembly and sliding of the 3 nucleosomes in the promoter region. They show that there are seven models (out of several thousand "models") that agree well with the data. They discuss the interesting features observed in these 7 models.

Even though earlier studies have attempted a similar approach, this is a nice work as it is comprehensive and systematic. However, there are some concerns and some suggestions that could improve the paper.

(1) Authors account only those eight promoter nucleosome configurations that are presented in the Brown et al/Small et al. experiments. However, to understand gene regulation, binding of other transcription factors (like Pho4) too are crucial. Binding of these factors are coupled with nucleosome dynamics. Can the model provide biologically relevant predictions without accounting for these factors? This is not clear from the current manuscript.

(1a) Authors find that certain sliding events are crucial. However, binding of Pho4 would provide steric hinderance and prevent many of the sliding moves. How would you reconcile this given the results presented here.

(1b) Are there known mechanisms for directed sliding of nucleosomes? It is mentioned that the sliding speed is consistent with SWI/SNF, RSC remodelling complexes. But are any of these enzymes known to slide nucleosomes in a specific direction?

(2) Even though experiments have measured positioning of only three nucleosomes, isn't it possible that the positioning of these nucleosomes is influenced by the 4th nucleosome (N-4) or even the +1 nucleosome? It is known that positioning of neighbouring nucleosomes are correlated (due to their steric exclusion). Will extending the model with the 4th nucleosome (or +1 nucleosome) provide more insights about the dynamics of the 3 observed nucleosomes? If possible, that would be a new contribution beyond all the existing models.

(3) Given that many studies on this topic exist, what are the new testable predictions from this study? Please write a small subsection on the new testable predictions.

(4) Some suggestions to bring more clarity to the manuscript:

(4a) It is good to clearly define what is a "model". In this context, typically, a master equation would define a model. When authors talk about several models, it is good to mention how precisely they define a model. Readers need to understand how did authors enumerate all the models and whether the list is exhaustive or not.

(4b) Please precisely define what do authors mean by "overwrite" and "overrule". It is often mentioned that some processes can overwrite/overrule other processes. It is not clear what is the precise meaning of this. For example, in Figure 3, it is written that S3-4 overrules S2* but both the arrows are present in the figure.

(4c) This overruling appears a bit arbitrary. A given process can overrule many other processes. Has all such possibilities been considered?

(4d) Please also explain why certain nucleosome assembly/disassembly/sliding processes are called "regulated" or "constitutive".

Reviewer #3:

This paper offers a well-written analysis of nucleosome dynamics at the classical yeast PHO5 promoter. It sets out a hierarchical maximum-likelihood scheme for successively fitting coarse-grained models to heterogeneous datasets, while avoiding the parametric morass, building on the work of Blasi et al., 2016. The main results (Figure 5), draw attention to patterns of fluxes between nucleosome configurations which are common among classes of the best-fitted models. Overall, this is a well-conducted study in the art of rigorous model fitting to complex data. The biological implications, however, are relegated to the Discussion. On the one hand, this presents an informed review of the experimental literature; on the other hand, the main suggestion, to reconsider the role of nucleosome assembly (Discussion), does not seem sufficiently well supported by the actual results (below). I therefore feel that the paper may be better suited to a more specialised audience in computational biology. I believe peer review is improved by transparency and therefore do not wish to remain anonymous.

(1) "We suggest to reconsider the common view for the case of the PHO5 promoter". The models considered in the paper are coarse-grained Markov processes describing nucleosome configurations and transitions between them. In particular, neither transcription factors like PHO4 nor nucleosome remodellers are explicitly represented. Without further analysis, it is not straightforward to draw well-founded conclusions about what may, or may not, be happening at this more detailed level. To put this in perspective, if one started from a detailed Markov process model, which included, for instance, nucleosome remodellers, and attempted to construct from that a more coarse-grained model, then the latter may not even be Markovian. It is reasonable to draw conclusions at the level of abstraction of the models themselves, as in Figure 5, but to assume that this also gives insight into what is happening at a more detailed level seems to require careful justification, which is not provided here.

(2) Surprisingly, the paper does not use the fitted models to suggest experiments which could determine the relative roles of assembly and dis-assembly at the PHO4 promoter. This would have been a more compelling way of drawing biological significance from the modelling. Lurking behind this suggestion is the broader issue as to what should be expected from a model in biology. This is a matter on which much has been written, so I feel it is only fair to acknowledge my own bias in this respect. I believe models are not descriptions of biological reality but, rather, descriptions of our assumptions about reality (PMID 24886484). From this perspective, a model in biology does not offer predictive capability, as it does in physics or engineering but, rather, a test of its assumptions. The best test of any assumptions are data from new kinds of experiments. I was disappointed that such experiments were not suggested here.
