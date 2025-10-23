# Peer review - Round 1

Editors:
- Stephen C Harrison, Harvard Medical School , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.07574.054](https://doi.org/10.7554/eLife.07574.054)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for sending your work entitled "Mapping the Conformational Landscape of a Dynamic Enzyme by Multitemperature and XFEL Crystallography" for consideration at eLife. Your article has been favorably evaluated by Michael Marletta (Senior Editor) and two reviewers, Stephen C Harrison and A Joshua Wand. The former is a member of our Board of Reviewing Editors.

This manuscript, a major technical achievement, gives an initial glimpse from a new perspective on several long-standing issues and controversies in protein biophysics. There are two significant observations – that local (mostly side chain) conformations are heterogeneous and in many cases show strong temperature dependence and that the temperature dependence is also heterogeneous.

Essential revisions:

A vast amount of work has gone into this report, and the reviewers agreed that it is a tour de force of experimental and computational effort. In its current form however, the manuscript makes it difficult to tease out where it leads. There seem to be two problems, both of which stem from efforts to fit the work into a framework that does not do it justice. Firstly, the authors interpret the results in terms of a transition at 200o even when the data seem to show that there is no such sharp distinction. More importantly, the authors fail to draw obvious conclusions from the heterogeneity of the apparent temperature dependence and try to force it into an old model that seems to be disproven. Secondly, the inclusion of the XFEL experiments is unjustified.

Problem 1:

There are no data between 180° and 240°, the largest jump in the temperature range. This jump exaggerates the apparent break in the curves in Figure 5B-C, and the relatively small (and imprecisely determined) occupancies of minor states at 180° below makes including those points in the "pseudo Van't Hoff" plots awkward. But within the large error bars that would obtain, many of the plots could probably include the lower temperature data and remain essentially linear (certainly true for my own hand replotting of Figure 5C as lnK vs. 1/T). In any case, it would seem that the heterogeneous response does not support the slaving model of Fraunfelder et al., since the natural thermal dependence of motion at individual sites will, as shown by Lee and Wand, give an average response typical of the scattering studies of old that started the dynamical transition and slaving models.

Problem 2:

The XFEL data are in many ways "scooped" by the 1.2 Å synchrotron data. In several figures, the XFEL points are lonely dots that simply fall on the expected curve. The one justification for inclusion of the XFEL data is the assertion that the dataset is damage free. But Figure 1–figure supplement 1 asserts that damage is minimal across data collection temperatures. There is some increase in R as exposure progresses, and the data were collected to avoid damage differences at different temperatures. Nonetheless, over the whole range of temperatures, the resolution is always better than that of the XFEL data, and had the synchrotron data been cut off at 1.75 Å spacing, it is possible that there would have been no evidence for any damage at any temperature.

Both these problems can most likely be addressed with some thorough reorganization and considerable rewriting of the manuscript, along the lines outlined below.

1) The Introduction should be about the real point of the paper (and the reason that it would be interesting to eLife readers): the internal dynamics of a protein. It should be addressed to someone interested in protein structure, but who is not acquainted with the earlier Frauenfelder and Petkso work, who has not read Lee and Wand (but needs to know about it), and who would like to understand whether the authors agree or disagree with the interpretations given by Kern to her studies of CypA dynamics. In its current form, the Introduction provides an unclear description of the inadequacies of current methods and the promise of XFEL data collection, and the paper then leaves a careful reader believing that the paper has in no way demonstrated that promise and if anything shown that current synchrotrons do better. Only around the fourth paragraph does the Introduction use the possibility of temperature jump (not used for any of the experiments here) as a reason to segue into what are (for the uninitiated) obscure references to Frauenfelder, Lee and Wand, and Eisenmesser et al.

2) In the presentation of Results, the same forced effort to justify the XFEL experiment shows through. For example, in the third paragraph, the failure of the XFEL data alone clearly to show the Leu98 alternative conformation gives rise to the argument "oh well, in the future, with less hardy crystals, we'll need it". We suggest at the end of this set of points how to include the XFEL data more modestly.

3) The Results are written for an "insider". What is "Ringer analysis", for example? If "Ringer" is the name of a program, it should be in all uppercase (like HKL2000, RELION, CHARMM, etc.). Surely there is a two or three word phrase that can summarize sampling the density for evidence of variation of torsion around chi1. Likewise, sentences like "our multiconformer models separate harmonic from non-harmonic contributions to flexibility" will be clear to MD savvy folks, but not to a sufficient fraction of the eLife readership to justify the journal as a good venue for a paper written this way.

4) As already mentioned, the interpretation of a sharp divide above and below 200° K seems forced. Sure, above 200° multiple conformations provide a better explanation than does a single one, but if two conformations are evident at 240, and the occupancy of the minor is not evident at 180°, that does not convince at least one reviewer that there is anything special about 200° or that there is something going on that is different from a smooth decrease in the minor state occupancy that simply falls below the detection threshold somewhere between 240° and 180°, but not in any way that suggests an abrupt transition (at least for the whole protein). This is the key point, both for presentation and analysis of the data and for the conclusions.

5) The paragraph about CypA in HIV is not particularly relevant, and the throw-away remark about an "arms race" should be rethought. Some evolutionary relationship between loop states and Gag binding might hold, but there are no lineage data cited even to hint at such a possibility.

6) A diagram is needed to explain what is meant by "tiered energy landscapes" – or at least what Frauenfelder meant by it. It is important to note that the tiers of Fraunfelder are related in timescale yet the heterogeneity of rotamer distributions seen here have been shown by many NMR studies to be on the same sub-nanosecond timescale.

7) To what extent are these data more or less consistent with the notions put forth by Lee and Wand, by Tilton et al, by Kern and coworkers, and ideally also with the (not mentioned) "sectors" analyzed by Ranganathan?

8) The reviewers are comfortable with inclusion of the XFEL data, but simply as another dataset. Some modest remark is of course justified, about how valuable the new postrefinement methods are for a good dataset, but Figure 8 should be removed.

Minor points:

Figure 6 fails to get across that the conformational heterogeneity and its temperature dependence are in direct opposition to the global "glass transition" popularized by the physics community. It is implied but not made explicit that this heterogeneous temperature dependence predicts the 200 K inflection using data obtained 100 degrees above it. In other words it is a direct consequence of the thermal behavior of internal motion of proteins in solution and has nothing really to do with a global concerted glass transition driven by the freezing of solvent.

The authors talk a lot about "dynamics", but this is not what they observe. Rather they observe presumably (near) equilibrium distributions. What is missing is a strong acknowledgement of timescale. For CypA, they somewhat casually link distributions to slower time scales (i.e. us-ms) rather than the ps-ns motions that actually govern side chain rotamer interconversion. The work of Fraser and Wright (Fenwick et al. 2014) addresses this point somewhat, but that work is only summarized in the present manuscript. Further to this point, the "hierarchical" model (beyond the tautological) is not necessarily consistent, since it requires higher "tiers" of motion to occur on increasingly slower timescales, which is something that this work cannot really address (although the NMR studies say it is not consistent, since the various classes of side chain motion observed occur on the same timescale).

The idea of frustration is overworked. In ubiquitin, one of only two proteins where an extensive temperature dependence of NMR-detected fast motion has been done, it has been shown by pressure perturbation that the coupling (effectively the source of frustration) between side chains is very limited.
