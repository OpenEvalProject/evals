# Peer review - Round 1

Editors:
- Dominique C Bergmann, Stanford University/HHMI , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.26023.029](https://doi.org/10.7554/eLife.26023.029)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Topological analysis of multicellular complexity in the plant hypocotyl" for consideration by eLife. Your article has been favorably evaluated by Christian Hardtke (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this work Jackson et al. provide a general framework to study cellular networks in plant tissues. They show that different cell types have different network properties in Arabidopsis, and that this holds, to some extent, across different Arabidopsis ecotypes and (to a lesser extent) between species. These results present an interesting methodological advance, and the potential to uncover previously unseen patterns, if a number or technical and presentation issues are addressed.

Major issues:

1) eLife papers describing new techniques or analysis approaches like this one should be accessible and interesting to a wide audience. Several reviewers felt that the authors did not yet make a persuasive case that they are discovering general principles here, and for this work to be useful for the developmental biology community, the connection between the detailed measurements and biological problems must be made very clearly. This "Major issues" section enumerates what they considered to be necessary changes to be made in the revision:

A) The connection between what is measurable and what can be interpreted as the biological significance of the measurement needs to be done with some care. For example, the authors interpret BC as meaning that "atrichoblast cell files are topologically poised to mediate the optimized movement of information" and "having the capacity to control information movement through a limited number of local interacting partners". This is a leap. For example, BC may highlight nodes that form the sole pathway between two otherwise disconnected parts of the network. In that case the argument that BC signifies the potential to control flow (of information, or anything else) is justified. However, BC can be high in many other contexts. In the cellular contact network in particular there will be many ways that information can pass between cells, as this network resembles a lattice. A high BC node therefore could lie on a slightly shorter path, but there will be many other paths, perhaps even of similar length. The equivalence between high BC and a capacity to control is therefore much less obvious. The authors should put less emphasis on this interpretation of BC. They may still have a point here, but at present the manuscript is overstating the connection between BC and control. This is linked to a general feeling that the equivalence of cellular networks and networks of directed information flow (based on the evidence presented in this paper), is overstated.

B) Several reviewers felt there was not a clear path between the technique described here and genuine insight into developmental biology. The clearest way to show that this technique can lead to new biological insights is to provide such an insight. This may be achieved by revisiting old experiments in the literature that had some contradictory or hard to understand elements and showing how the approach presented in this paper can explain the discrepancy/discordance in the data. Alternatively, an observation made here should be predictive of a behavior; for example, the authors describe a difference in connectivity between atrichoblasts or trichoblasts: what would you predict are different properties of a hormone or Ca or physical signal sent through one or the other of these cell types? And how would you confirm this experimentally?

C) The rationale explaining how the authors picked the different plant species and the different mutants are not crystal clear. For the flow of the ideas and the understanding of the reader, it would be nice to include two paragraphs explaining the general concept and why the authors chose these plant species (first paragraph) and mutants (second paragraph).

D) There needs to be a more coherent section at the end summarizing precisely what principles hold across ecotypes, species, and mutants (backed up by statistical significance measures). A more rigorous set of conclusions of this kind would provide an adequate justification for the rather strong and general claims made in the abstract. The question that needs to be clearly answered in this summary is: What can network measures predict about plant cells?

E) There are some technical issues in the way data are presented or interpreted. For example, weighted BC (subsection “Topological analysis of the wild-type Colombia Arabidopsis hypocotyl”, tenth paragraph). Generalisations of BC to weighted networks are not entirely straightforward, as there is more than one way to interpret path length in weighted networks. One way for example is to use the reciprocal of the weight as the contribution that a link makes to the overall path length. The authors should clarify what version of weighted BC they are using. It seems that the inverse of the connecting cell wall area was used as the weight itself, but weighted path length calculations often use the reciprocal of the weight, which means that there might be a double reciprocal here? In any case the definition of the weight and the exact algorithm should be made explicit.

2) In general, arguments throughout the manuscript rely a lot on visual comparisons of distributions, which are not always convincing. There are plenty of rigorous statistical tools for comparing two distributions, which would return a measure of significance for the difference between the distributions. Calculating such significance values for all the relevant comparisons of distributions in the paper would make the authors' arguments much stronger (providing the statistics support their claims). In addition, since you are able to study many different parameters extracted from the plant tissues (e.g. cell characteristics, node characteristics and edge characteristics, the statistical relationships (correlation or else) between these values need to be provided; overall and within the different cell types. Certain parameters are likely to be trivially linked, but this may report important aspects of the cellular networks organizations that are currently ignored in this version of the manuscript. In particular, which are the local (cell parameters) that influence BC-is a cell able to control in some ways its own BC?

3) The Discussion is focused narrowly, and mostly on the authors own work. The Discussion would be more valuable if it were expanded to consider: a) other plant tissues and other work in the field of plant tissue patterning, b) animal cell organization (embryo patterning in C. elegans, D. melanogaster, Neurons…) where cell migration is operating and how the authors see cell networks in this dynamical context.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Topological analysis of multicellular complexity in the plant hypocotyl" for further consideration at eLife. Your revised article has been favorably evaluated. Improvements on the clarity of the writing, statistical measurements and inclusion of functional data on atrichoblast vs. trichoblast files have made this version much stronger.

We intend to recommend this manuscript be accepted, but a few changes to the explanation of the fluorescein experiment (in Figure 3) would be helpful. The names of atrichoblast and trichoblast cell files (while not incorrect) are somewhat confusing because these files, in the hypocotyl, do not produce hairs. Experiments involving uptake of substances from the media will immediately make people think about hair and non-hair cells of the root, and it is natural to begin to think that. Rewording or putting in an additional sentence to explain that the difference in movement in the cells you are monitoring is not due to morphological differences in these cells themselves (and that they are some distance from the site of uptake) would eliminate this confusion.
