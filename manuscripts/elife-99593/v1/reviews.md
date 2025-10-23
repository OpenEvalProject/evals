# Peer review - Round 1

Editors:
- Babak Momeni, https://ror.org/02n2fzt79 Boston College United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.99593.3.sa0](https://doi.org/10.7554/eLife.99593.3.sa0)

This manuscript offers valuable theoretical predictions on how horizontal gene transfer (HGT) can lead to alternative stable states in microbial communities. Using a modeling framework, solid theoretical evidence is provided to support the claimed role of HGT. However, given that the model has many degrees of freedom, a more comprehensive analysis of the role of different parameters could strengthen the study. Additionally, potential interactions between plasmids that carry out HGT are not discussed in the model. This paper would be of interest to researchers in microbiology, ecology, and evolutionary biology.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99593.3.sa1](https://doi.org/10.7554/eLife.99593.3.sa1)

Summary:

In this work, the authors use a theoretical model to study the potential impact of Horizontal Gene Transfer on the number of alternative stable states of microbial communities. For this, they use a modified version of the competitive Lotka Volterra model-which accounts for the effects of pairwise, competitive interactions on species growth-that incorporates terms for the effects of both an added death (dilution) rate acting on all species and the rates of horizontal transfer of mobile genetic elements-which can, in turn, affect species growth rates. The authors analyze the impact of horizontal gene transfer in different scenarios--such as bistability between pairs of species and multistability in communities--over an extended range of parameter values. In almost all these cases, the authors report an increase in either the number of alternative stable states or the parameter region (e.g. growth rate values) in which they occur.

Understanding the origin of alternative stable states in microbial communities and how often they may occur is an important challenge in microbial ecology and evolution. Shifts between these alternative stable states can drive transitions between e.g. a healthy microbiome and dysbiosis. A better understanding of how horizontal gene transfer can drive multistability could help predict alternative stable states in microbial communities, as well as inspire novel treatments to steer communities towards the most desired (e.g. healthy) stable states. In my opinion, this manuscript is a solid theoretical approach to the subject.

Strengths:

- Generality of the model: the work is based on a phenomenological model that has been extensively used to predict the dynamics of ecological communities in many different scenarios.

- The question of how horizontal gene transfer can drive alternative stable states in microbial communities is important and there are very few studies addressing it.

Weaknesses:

- In the revised version of the manuscript, the authors significantly extended the analyzed region of parameter values. Still, the model has many parameters and the analysis is typically done by changing one or two parameters at a time. Thus, the work shows how HGT can indeed promote multistability, but it remains hard to grasp whether it consistently does so across a large region of the parameter values space.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99593.3.sa2](https://doi.org/10.7554/eLife.99593.3.sa2)

Hong et al. used a model they previously developed to study the impact of plasmid transfer on microbial multispecies communities. They investigated the effect of plasmid transfer on the existence of alternative stable states in a community. The model most closely resembles plasmid conjugation, where the transferred genes confer independent growth-related fitness effects and different plasmids do not affect each other's transfer or growth effects. For this process, the authors find that increasing the rate of plasmid transfer leads to an increasing number of stable states, as long as the model includes a constant death/dilution term.

This is an interesting and important topic, and I welcome the authors' efforts to explore these topics with mathematical modeling. The addition of sensitivity analyses also strengthens the usefulness for quantitative microbial ecologists. However, the additional sections have made the main text harder to read. Between the effect of the dilution rate, the increase in subpopulations with HGT, and the modulation of interspecies competition, the reviewers have suggested a number of factors that may explain the way plasmid transfer modulates multistability. I think it would be helpful if the authors could summarize some of these effects/interactions between different parameters in their model more. I personally continue to find the model very unintuitive, especially in the way it averages over subpopulations carrying more than one foreign plasmid. Additional sentences that give the reader intuition for the sensitivity analyses and how these interplay with the results would be good.

Specific points

(1) The model makes strong assumptions about the biology of HGT, that could be spelled out even more. Since the model is primarily applicable to HGT driven by the exchange of plasmids, I believe the abstract (and perhaps even the title of the paper) should be updated to reflect that.

(2) I am not surprised that a mechanism that creates diversity will lead to more alternative stable states. Specifically, the null model for the absence of HGT is to set gamma to zero, resulting in pij=0 for all subpopulations (line 454). This means that a model with N2 classes is effectively reduced to N classes. It seems intuitive that an LV-model with many more species would also allow for more alternative stable states. For a fair comparison one would really want to initialize these subpopulations in the model (with the same growth rates - e.g. mu1(1+lambda2)) but without gene mobility.

[Update:] It is good that it seems that initializing pij with non-zero abundance did not seem to affect the conclusion that higher amounts of HGT increases multi stability. However, rather than listing it as one control for a specific condition, I would argue that this is the appropriate null model across the board (where HGT rate is varied from 0 to a high value), including figures S9 and S10.

(3) The possibility that the same cell may be counted in different pij runs counter to all intuition that researchers coming from a background of compartmental /epidemiological modeling may have. The associated assumption that plasmids do not affect each other's dynamics or (growth/interaction) effects at all is also a very strong assumption. This should be signaled much earlier in the manuscript, possibly already in line 106 when the model is introduced.
