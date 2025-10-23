# Peer review - Round 1

Editors:
- Jeff Gore, Massachusetts Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.34862.026](https://doi.org/10.7554/eLife.34862.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Shearing in flow environment promotes evolution of social behavior in microbial populations" for consideration by eLife. Your article has been evaluated by a Senior Editor and three reviewers, one of whom, Jeff Gore (Reviewer #3), served as Reviewing Editor. Our decision has been reached after consultation between the reviewers.

The referees appreciated that the study allows for a principled way of thinking about how spatial structure could arise. However, there were several significant concerns that were expressed regarding the presentation, conceptual framing, and technical implementation of the model. We do believe that the approach has potential, so if you can address all the concerns of the referees, we would consider a new manuscript.

Major issues that would have to be addressed:

* Framing of the question in terms of spatial structure vs. group selection

* Clarify how heterogeneity is analyzed in the population

* Does the social strain actually evolve / spread in the model?

* Show what happens with fixed strategies with and without flow and with and without the Turing pattern and then explore the effect of evolution

* Was there an error in the implementation of the model? (See reviewer #2's comments.)

Reviewer #1:

The manuscripts considers the problem of how cooperation survives in the presence of cheaters. The explanation is based on the Simpson's paradox (paper by Stan Leibler is not cited and the mechanism is not discussed). The novelty is that the metacommunity dynamics emerge from the governing equations rather than being externally imposed.

Specifically, the production of public good and waste are set up to produce a Turing instability, which creates patches of high population density separated by voids. These act as local communities in a meta community. Within each patch cooperators are outcompeted, but patches with many cooperators grow faster than patches with few cooperators. As a result, cooperators persist.

The key factor in the above argument is that the competition occurs between different patches. It seems to me that, for this to happen, the patches need to be constantly reformed. Reforming could occur due to breaking of the Turing patters by the flow. I think this mechanism is very important, but it is not discussed in the manuscript in any detail. Instead, a lot of the Discussion is focused on the enhancement of the cluster growth rate due to flow. While this enhancement plays a role, it is not clear whether this or the above mechanism is the dominant force. This seems to be a major point to address.

Other comments. The first half of the paper restates the standard results from Turing pattern formation and is better suited for Supplementary Information. I don't think these derivations are necessary to understand the main results and will probably be skipped by most readers. The simulation methods need to be better discussed. The following paper could also be relevant, Drescher, Knut, et al., 2014.

Overall, this seems to be a solid research paper. As far as potential impact, there are three distracting factors:

1) Simpson's paradox is pretty well established.

2) Turing patterns are known to occur in ecological models and possibly real ecosystems. The fact that inhomogeneous spatial densities due to Turing patterns affect species interactions is also well known. There is a lot of literature on this. See for example Wilson, Morris and Bronstein, 2003.

3) It is not clear whether the specific model is applicable to any specific ecosystem or that the Turing mechanism is robust and present in actual microbial communities.

Reviewer #2:

In this paper, the authors show that advection in the spatial population dynamics of microbes can lead to the assortment that is necessary to maintain cooperation (in the form of public good production).

This is potentially interesting, but I find the background and Introduction of the paper conceptually flawed. Moreover, the basic model seems to contain an error.

For me, the conceptual problems start with the first sentence of the Abstract: "It is advantageous for microbes to form social aggregates when they commonly benefit from secreting a public good." This is the wrong premise: whether it is advantageous to form groups is a question, not a fact.

Similarly, in the Introduction the authors state: "… until the lack of public goods compromise the fitness of the entire group". This sounds like it is already known how this plays out, but that's exactly the problem: it is generally not known how this plays out. The way the authors are stating this, the outcome would be a matter of the relative strength of individual vs. group selection.

However, despite the fact that they are vaguely referring to "group fitness" and "species fitness" throughout the paper, their model does not have reproducing groups, and hence they are not talking about group selection (see also below). In fact, they are talking about individual selection, and in particular they are talking about a particular mechanisms, advection, that can lead to assortment of cooperative types and thereby the maintenance of cooperation.

In general, the Introduction doesn't make much conceptual sense to me. For example, I don't see how quorum sensing falls into the category of mechanism where altruism is a consequence of a self-serving trait. With quorum sensing, the problem is shifted onto the production of the sensing signal, which becomes itself a public good. Judging from the literature cited, the authors do not seem to be up to date with group selection theory: Simon et al., 2012, 2013 have shown that kin selection is not closely linked to kin selection, as claimed by the authors in the third paragraph of the Introduction.

Group selection is an altogether different mechanism than selection at the individual level, of which kin selection is an example. In general, all individual-level explanations for cooperation, including kin selection, can be understood on the basis of assortment (Fletcher and Doebeli 2009). Group selection is a conceptually different mechanism that involves differential birth and death of groups with different type compositions, as well as (possibly) interactions between groups (Simon et al., 2013). In particular, it seems clear that the mechanism for the evolution of cooperation proposed by the authors is an example of (spatial) assortment, and not of group selection as they claim. They mention that in their model, spatial groups form and "reproduce", but this is simply an emergent property of the model, and the significance of the differential reproductive success of different groups is not investigated in the paper. My guess is that even if these "groups" would not reproduce, cooperation would still be maintained due to the assortment caused by advection. Overall, it is therefore not clear that the authors fully understand the conceptual underpinnings of the evolution of cooperation, and how their model fits with existing theory and concepts.

Perhaps more importantly, I think the basic model 1-3 may contain a fundamental flaw. Specifically, in Equation 2 the term -ns1 does not seem to make sense, since this represents only the public good produced by those microbes whose cooperation level is s1. This term should be replaced by an integral over s1, thus measuring the contribution to the public good of all types. Similarly, the term -ns2 in Equation 3 seems wrong, as here the term n should be replaced by an integral over all types s1, i.e., n should be replaced by the total number of all microbes living at a given location. (Note that the model does not assume only a single type s1 at any given location; otherwise the second derivative with respect to s1 in Equation 1, i.e., diffusion in s1 space, would not make sense.) Given that the basic equations may be wrong, I am uneasy about the rest of the analysis in the paper.

Reviewer #3:

Overall, I found this to be an intriguing combination of two rather different fields. As the authors describe, there is a long history of theory and experiment probing the conditions required for the evolution of cooperative behaviors, and some of this work has focused on spatial structure. However, little of the work has considered interesting flow fields with shear. I very much like the idea of a public good and a public bad, each of which is secreted. Then, if the public bad diffuses faster than the public good it is possible to have Turing instabilities.

My primary concern is that I didn't understand how the dynamics between cooperation and cheating took place in terms of distribution and abundance of the different strategies. How much cooperation was present in the various flow situations? Was there heterogeneity in the population? What would happen if there were a (non-evolving) fixed cooperator and another genetic cheater?

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "Shearing in flow environment promotes evolution of social behavior in microbial populations" for further consideration at eLife. Your revised article has been evaluated by Arup Chakraborty (Senior Editor), and three reviewers, one of whom served as Reviewing Editor

The manuscript has been improved but there are remaining issues that need to be addressed before the manuscript can be considered for acceptance, as outlined below:

Two of the three reviewers are still uncomfortable with your treatment of heterogeneity in the population. Even if a cheater will quickly take over a local population, it does not mean that there cannot be heterogeneity of different levels of cooperation within each local population or within the broader metapopulation, where different groups could have different levels of cooperation. As far as we can tell, this sort of heterogeneity was never analyzed in the paper, but we think that it is very important for a complete understanding of the system. As indicated below in more detail, this is not simply a question of "notation." It seems that the integral was added into the model description but that no analysis of this heterogeneity was actually done.

Please consider the following points in revising your manuscript:

1] The authors state that "It is well known that evolution of altruism in species strongly depends on the individuals being discrete (Durrett and Levin (1994)). This would seem to imply that deterministic models, e.g. involving differential equations for frequencies of different types, would never lead to cooperation, which is of course not true. Furthermore, the argument in Simon et al. (2012) for why group selection is different from kin selection is not primarily based on the asynchrony of individual-level and group-level events. Rather, it is a consequence of the fact that assortment (or, equivalently, relatedness) may have no influence on certain group level events, such as games between groups.

2] The authors' statement in the rebuttal letter that "This change in notation does not affect our results or analysis, since in our simulations we start the population with a fixed secretion rate." is unclear to us. First, starting with a fixed secretion rate would not make the original equations correct, because mutation would quickly lead to a situation in which secretion rates are variable. Second, what is meant by "a change in notation does not affect our results"? Of course, a change in notation does not affect anything, apart from the notation in itself. The question is whether the simulations were carried out correctly, i.e., with the integral (summation) term taken into account. Have the simulations been carried out according to the new, correct equations?

3] The authors' finding that without advection, cooperation cannot be maintained in their system is curious. This seems contrary to previous work by Hauert and colleagues (Wakano et al., 2009), which shows that cooperation is maintained in public goods reaction-diffusion systems. I am wondering about the cause of the different outcomes in these models. Is it due to the continuous nature of the secretion trait considered in the present study? If so, this might be important to point out in the Discussion.
