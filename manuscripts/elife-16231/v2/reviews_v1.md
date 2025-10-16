# Peer review - Round 1

Editors:
- Benjamin S Glick, The University of Chicago , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.16231.012](https://doi.org/10.7554/eLife.16231.012)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Stacking the odds for Golgi cisternal maturation" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom, Benjamin Glick, also guest edited the paper, and the evaluation has been overseen by Randy Schekman as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Alberto Luini (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper explores the dynamic organization of the Golgi by a theoretical modeling of Boolean networks. The simplicity of the approach enables the authors to perform an unbiased survey of a large number of possible vesicle trafficking scenarios. A surprising and striking result is that many of the networks display the properties of compartmental maturation. Thus, the evolution of Golgi maturation can be viewed as a natural outcome of the intrinsic properties of vesicle trafficking systems. According to this view, the transport of large secretory cargo molecules was probably an adaptation that took advantage of an existing process.

Essential revisions:

The reviewers and reviewing editor had an interesting discussion about your paper. Multiple concerns were raised, and initially it seemed likely that the decision would be to decline the submission. In the end, we agreed that the story is interesting enough to merit a request for resubmission after major revisions. There is no guarantee that the revised version will pass muster, so you will need to decide whether the effort is worthwhile.

There is general agreement that the idea of approaching this problem with Boolean networks is creative and novel, and that the results are an important step forward if the approach is sound. But the following issues need to be addressed.

1) Your model assumes that compartment identity is determined by transmembrane and luminal components, which are necessarily exchanged by means of transport vesicles. But in reality, components recruited from the cytosol, such as GTPases and adaptors/coats and phosphoinositide modifying enzymes, play an important and perhaps central role in defining compartment identity. In some cases, Rab cascades are thought to regulate compartmental maturation. While your model necessarily is necessarily a simplified representation of reality, overlooking this fundamental property of the endomembrane system seems hard to justify.

2) The focus of your analysis is on the subset of networks that include maturation chains. But the majority of the networks do not show maturation. The neglect of those other outcomes is surprising. For example, how often is the traditional vesicle shuttle model replicated? What can be learned from analyzing the full set of networks?

3) The assumption that vesicles unable to find a target undergo homotypic fusion is troubling. This process may reflect the actual behavior of some vesicle types in cells, but why is homotypic fusion the default assumption? Does this feature predispose the model to generate maturing networks? Why wouldn't orphan vesicles fuse heterotypically, like other vesicles do?

4) The treatment of spatiotemporal aspects of membrane traffic raised two issues:

The description of virtual stacking (Figure 4) is not at all compelling. What is the justification for modeling vesicle fluxes as attractive springs while modeling compartments as repelling charges? That representation does not seem to correspond to any realistic picture of membrane traffic. This part of the story weakens the paper, and should probably be omitted unless it can be revised in a way that makes sense.

One of the reviewers was quite troubled by the lack of spatiotemporal parameters in your model (transport coefficients, distances, compartment sizes, etc). The other two reviewers were of the opinion that the cytoplasm is well mixed, so it is reasonable to assume that vesicles will reach any potential destination. But to convince the skeptical reviewer and other readers, you should explain why spatiotemporal parameters can be ignored for the purposes of your simulation. In particular, the markers used in your simulation reach a steady-state homeostatic distribution, but is it automatically true that all of the other components, such as lipids, will also undergo balanced flows in a given network? Does your model require the unrealistic assumption that every compartment generates the same number and size of vesicles per unit time? Is it obvious that movement between compartment is fast relative to formation and fusion of vesicles, so that spatial aspects can be neglected?

5) In general, the descriptions and discussion need to be expanded significantly to address the questions that will be raised by cell biologists. Perhaps it would be useful to rewrite the paper with input from a cell/membrane biologist. Here are examples of issues that should be addressed:

The introduction is too generic. It does not even mention the Boolean modeling approach, and does not describe either the power and limitations of this approach or the reasons for choosing it to address this particular topic.

The difference between actual and randomized networks in Figure 2A–C is confusing, and the significance of Figure 2D,E is hard to understand. Similarly, in Figure 3, what is the difference between special pairs and random pairs? The parameters and assumptions should be clearly described in terms that will make sense to cell biologists.

The phenomenon of compartments becoming richer in compositional complexity over time has not been described experimentally, and doesn't seem to make biological sense. Can you comment on this discrepancy?

Regarding the maturation chains, one reviewer wrote: "However, these striking observations are not clearly interpretable. The authors should provide much more detail on the characteristics of these chains, on the dynamics of their development, and on the number of the chains that possess these particularly complex features. They should also describe the networks that do not contain maturation chains, which actually represent the majority of the outcomes. They should discuss which parameters lead to realistic maturation chains, and which preclude maturation. What is interesting to me is not the fact that they observe maturation as this outcome is expected, but the fact that the maturation networks are so complex and so similar to the real ones, and so frequent. Again they should thoroughly describe the maturation chains, the alternative outcomes and the conditions where they obtain. Without this description we cannot judge the value of the simulations."

Do the authors wish to argue that their simulations reflect a potentially simpler situation early in evolution, and are therefore not constrained to incorporate features of currently existing trafficking systems? If so, they should make this point explicitly.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Stacking the odds for Golgi cisternal maturation" for further consideration at eLife. Your revised article has been favorably evaluated by Randy Schekman (Senior editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Once again the reviewers had an extended discussion of your manuscript. As before, one of the reviewers remains deeply concerned about the lack of spatiotemporal parameters in the simulations, while the other two reviewers feel that your approach makes sense and yields intriguing insights. After judging these arguments, I am prepared to accept your manuscript if you can address the following remaining issues either by revising the paper or by explaining why a revision is not warranted.

1) Even though the basic patterns of compartmental formation and communication can be described by the Boolean network approach, spatiotemporal parameters are clearly important in real cells to ensure that the membrane traffic machinery is efficient enough to support life. This point should be given further emphasis.

More generally, you should discuss the limitations of the described approach. Does the model make testable, falsifiable predictions? I suspect that this one can be addressed by the presentation. For example, if you predicted that maturation chains could have evolved without specific selection for the transport of large cargo, then the modeling matches this prediction. But are other aspects of membrane traffic not captured by your simple model?

2) The authors should discuss how to arrive at the Boolean network approach from a set of (partial) differential equations (similar to Heinrich/Rapoport's model or starting from overdamped Fokker-Planck equations). In particular: Which rates and transport coefficients are considered large or limiting w.r.t others, i.e. which quasi-equilibria are used for setting up the model from more fundamental approaches?

3) The biological meanings of the propensity parameters for budding and fusion are still unclear. Please provide an explanation. For example, does propensity to fuse reflect the spatial proximity of vesicle donor and acceptor compartments?

4) The assumption that orphan vesicles fuse homotypically continues to be troubling. You may not have fully understood the concern raised during the initial submission, so let's try again.

Vesicles are normally expected to fuse heterotypically. If a vesicle fails to find a target compartment, why should it then fuse homotypically? Why couldn't a vesicle of one type fuse heterotypically with a vesicle of another type? A priori, such heterotypic vesicle fusion may be more likely than homotypic vesicle fusion given that vesicles normally undergo heterotypic fusion with a target compartment.

The concern is that if homotypic vesicle fusion is programmed into the model as the default fallback option, then the model may be biased toward compartment formation and subsequent maturation.

5) Designating a GTPase that cycles through the cytoplasm as being formally equivalent to a vesicle is confusing. If your formalism treats a vesicle and a reversibly associating peripheral membrane protein as being equivalent, you should consider a term other than "vesicle". Maybe "carrier" would be more generic, and "membrane traffic" could be used rather than "vesicle traffic"?

6) At least some lipids can actually move via nonvesicular as well as vesicular pathways. The discussion of lipids may now be overly complex. The bottom line is that some components can only exchange between compartments via membrane vesicles (e.g., transmembrane proteins), some components could exchange either in vesicles or through the cytoplasm (e.g., certain lipids), and some components probably exchange only through the cytoplasm (e.g., certain GTPases).

7) Relevant to #7 above: does the model take into account the fact that the various components traveling from one particular compartment to another could travel at different times and at different rates? Maybe this point is implicit in the model, but it's hard to tell.

8) I didn't understand the discussion in the Results section about large global structures and shuffling the edges of a network. Is this issue important? If so, it should be explained better. If not, it should be omitted.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Stacking the odds for Golgi cisternal maturation" for further consideration at eLife. Your revised article has been favorably evaluated by Randy Schekman (Senior editor) and a Reviewing editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

This manuscript has been extensively revised and extended, and is now a substantial contribution that will stimulate thinking in the field. I see no benefit in putting it through another round of review because the key concerns have been addressed. But I will ask the authors to address a few very minor comments about the new "Orphan vesicles and homotypic fusion" section.

1) In cells, many compartments fuse homotypically. For clarity, you should state the assumption that compartments cannot fuse heterotypically with one another.

2) The first paragraph in this section is now perhaps more complex than necessary, and is a bit confusing as a result. For example, I have trouble figuring out what this sentence means: "This is rare: in almost all instances we explored, at least some fusion products of orphans were themselves orphans; in the majority of instances even the initial orphans could not fuse with one-another."

3) "one another" is two words.

Please make these changes and submit a final version.
