# Peer review - Round 1

Editors:
- Sara Mitri, University of Lausanne Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56801.sa1](https://doi.org/10.7554/eLife.56801.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper presents a computational model of horizontal gene transfer (HGT) in bacteria that explores the parameter space that would allow it to evolve. Interestingly, their model shows that even when costly, HGT is most like to evolve for genes with slight benefits to their hosts, which would be lost in the absence of HGT. HGT for these genes required a spatial context to evolve, but once these conditions were fulfilled, it evolved even in the presence of selfish genetic elements, which carry no benefit to their hosts.

Decision letter after peer review:

Thank you for submitting your article "Slightly beneficial genes are retained by collectives evolving Horizontal Gene Transfer despite selfish elements" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Patricia Wittkopp as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Paul G Higgs (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

This study uses a combination of two modelling approaches (differential equation models and IBMs) to ask how HGT can evolve de novo, and what kind of genes will allow for selection and maintenance of HGT. The analysis reveals that depending on the benefit (or harm) they provide, genes can be categorised into indispensable, enrichable, rescuable, unrescuable or selfish. They analyse these different gene types and show that HGT is more likely to evolve and be maintained for "enrichable" genes that have a small benefit to their carriers or for both enrichable and rescuable genes if a spatial version of the model is considered.

Essential revisions:

All reviewers agreed that this is a very interesting paper that gives some useful ways to think about HGT (the gene categories) and important insights into its evolution. We also agreed that the modelling approaches used were interesting, informative and appropriate. The paper is well-written, in particular the figures, which are very visually appealing.

A first key point is clarifying what mechanism of HGT the model is capturing: how is transfer occurring? What does the cost represent and how are genes acquired or lost? The paper contains mixed messages as to whether HGT occurs through plasmids or by transformation. According to the definition of "additive HGT", it should be through plasmids, and not by transformation, which requires recombination (Introduction paragraph two). But then other parts of the model (like acquiring genes from cells a certain distance away) suggest transformation. This choice will be important in determining the model structure, the rate of loss of the genetic element and its costs and benefits as detailed below.

Regarding the cost, what does it represent, and why is the cost proportional to the rate of transfer (ch) rather than just a constant cost (c)? If the HGT mechanism is conjugation, there is a cost of replicating the plasmid inside the cell, but the cost is constant – it doesn't depend on how fast the genes are transferred, just on how many plasmids are in the cell. Alternatively, if fragments of DNA are taken up from the environment, maybe there is a small cost to expressing uptake genes, and this might be proportional to h, although one would expect the main fitness benefits and costs are associated with the genes/junk/SGEs that are acquired by HGT rather than simply from having the ability to acquire genes by HGT.

Regarding gene loss, how it is modelled will also depend on the mechanism of HGT. If the gene is on a chromosome, then loss could be deletion of a gene during genome replication, or deleterious mutation that stops the function of the gene. On the other hand, if the beneficial gene is on a plasmid, loss of the beneficial gene is loss of the plasmid. This will clearly also affect the magnitude of the parameter value. In Equation 3, the loss rate from C- is the same as the loss rate from C+, which would be true if the gene is on a chromosome. But if that is the case, the gene that allows HGT should also be on the chromosome (contradicting with the additive HGT assumption) and it should also be lost sometimes, in which case a C+ could change to a C-, or an N+ to an N-. Another way to say this is "where does the C- come from?" If the beneficial gene were gained by HGT then it must have been gained by a + cell, then the C- was created by deletion of the gene that previously allowed HGT.

Another way to view the model is that the C+ represents a cell where the beneficial gene is on a plasmid that can be transferred by conjugation, whereas the C- represents a cell where the beneficial gene is already on a chromosome and cannot be transferred. In that case the loss rate from the chromosome by deletion should be different from the loss by losing the plasmid. Losing the plasmid means losing the benefit and the cost and the ability to transfer all at the same time. There is an interesting paper of Bergstrom that discusses the conditions for maintenance of a plasmid with a beneficial gene (Bergstrom et al., 2000). It would be useful to discuss similarities and differences of the present model with the Bergstrom model. An important part of the Bergstrom model is the transfer of the beneficial gene to the chromosome. This seems to be analogous to the mutation of a C+ to a C- in this model. In Equation 3 the rate of gain of the beneficial gene is hN+(C- + C+). This means that C- cells can donate the gene. This would apply if the gene is acquired by transformation, rather than conjugation. How would this change in the conjugation case? The rate of gain would be hN+C+ only. The N+ cannot gain from the C-. Does that mean the plasmid cannot spread? I think the assumption that the cost of HGT is proportional to h is relevant here. If the cost were a constant c (not ch) then a plasmid with high enough h would invade whatever the cost to the cells.

Finally on loss, the current choice of parameter for the rate of loss is odd. The authors claim that their results hold for more realistic values (subsection “Parameters used”) but making the parameter-region where HGT is adaptive for the host cells narrower. Is the parameter region large enough to be biologically relevant?

A second point that caused confusion is that the model assumes that each gene will either have a beneficial or a deleterious effect all the time. In reality, of course, MGEs lie on a parasitism-mutualism continuum relationship with the host bacterium because the “beneficial” gene will not be beneficial all the time (see Harrison et al., 2015, Discussion paragraph two). The same MGE transferring the beneficial gene may be an SGE depending on the bacterial host or the environment. The model thus considers a rather artificial case in which a single gene always has the same effect on its host. We see that it is a valid simplification to simulate each gene benefit individually, understand the conditions in which it may spread, and thereby infer that as long as genes with such benefits exist, then HGT should evolve. But this last logical step is not spelled out clearly enough in the paper.

Whether or not the gene is beneficial may also change the mechanism of transfer, where genes that are beneficial in the long term are more likely to integrate on the chromosome and reducing the rate of loss possibly by orders of magnitude. This last point is crucial, because if the rate of loss is low enough then slightly beneficial genes could be maintained in the absence of HGT. In other words, the authors may want to consider a case where the rate of loss differs depending on the costs and benefits of the gene in a given context.

A related point is how deleterious can SGEs become without disrupting HGT? This seems to be explored in Appendix 1—figure 5B and C. Is the result that SGEs would simply disappear if they are too deleterious? There seems to be a suggestion in the supplement that grid size may change this result. It would also be good to expand on this in the main text.

In sum, in order for the manuscript to be accepted in eLife, we ask the authors to at least do the following:

1) Include a detailed discussion at the beginning of the paper about the assumptions of the model and which biological situation is represented. Are you simulating HGT by conjugation or transformation? Who decides whether transfer is possible – the donor, the receiver, or both?

2) The authors should more explicitly explain where their parameter choices for costs, benefits, rates of loss, etc. and how they relate to the chosen mechanism of HGT. Also, why is it reasonable to assume that they are independent of each other?

3) Revise the choices of cost, benefit and rates of loss according to the biological situation and taking into account the ideas discussed above. Will the conclusions hold and will they be biologically relevant (if the parameter range is very small, is HGT likely to evolve)?

4) More fully cite the relevant literature on HGT costs and how they arise (TREE 2013 and San Millan and MacLean, Microbiology Spectrum 2017)

5) Flesh out what happens if SGEs are more deleterious.
