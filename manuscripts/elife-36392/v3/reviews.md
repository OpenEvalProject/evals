# Peer review - Round 1

Editors:
- Trisha N Davis, University of Washington United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.36392.024](https://doi.org/10.7554/eLife.36392.024)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Measuring NDC80 binding reveals the molecular basis of tension-dependent kinetochore-microtubule attachments" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Anna Akhmanova as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

General assessment:

This is a well-written and clearly presented manuscript describing a powerful assay to quantitatively measure the interaction between the kinetochore and kinetochore microtubules and address a central question about the molecular mechanism of error correction at kinetochores. This manuscript provides the first glimpse at the dynamic nature of the interaction between the NDC80 complex, the principle microtubule-binding interface of the eukaryotic kinetochore, and the microtubule lattice. The authors develop a sophisticated data acquisition and analysis system to obtain high quality FLIM-FRET information about the proximity of the NDC80 complex to the tubulin lattice.

Central conclusions:

Using this system, the authors make a number of novel observations:

1) They propose that ~ 35% of the Ndc80 molecules in a metaphase kinetochore are bound to the microtubule lattice at steady state.

2) The bound fraction of Ndc80 molecules increases from prometaphase to metaphase. The authors propose that the observed increase reflects chromosome-autonomous error correction processes.

3) The authors also find that the Ndc80 bound fraction correlates with centromere tension, and that this correlation requires the activity of the centromere-bound Aurora B kinase.

4) Finally, the authors propose a simple mathematical model (using a previously established model from the Grishchuck lab) to integrate their observations into a mechanistic framework.

The authors are to be commended on developing a state of the art FLIM-FRET assay and also a large-scale simulation approach in order to maximize their ability to obtain biologically relevant insight in terms of the bound fraction of Ndc80 molecules. The extensive efforts represent really the first measurement of this critical parameter.

Altogether, the work is technically impressive and an important contribution to our understanding of the architecture and dynamics of the mammalian kinetochore-microtubule interface. The paper is well written and the data overall is presented clearly, and in particular the authors do a good job relating their measurements to other ones in the field.

Essential revisions:

The reviewers raise a number of concerns that must be adequately addressed before the paper can be accepted. Some of the required revisions likely require further experimentation within the framework of the presented studies and techniques.

1) What is a "bound" versus "unbound" NDC80 complex? The difficulty in classification arises because Ndc80 can bind to the microtubule via its CH-domain as well as the 80 amino acid long unstructured tail. The authors monitor the binding of the CH-domains, but not that of the N-terminal tail. This is problematic, because the unstructured tail contributes to microtubule binding both in vitro and in vivo as shown by studies from Sophie Dumont's lab (Long et al., Current Biology 2017). It is reasonable to expect that the tail can extend to lengths of 5-10 nm while maintaining attachment to the lattice. This would place the CH-domain out of FRET range with the tubulin lattice even as the Ndc80 molecule is bound. The authors might have to address this ambiguity via both experimentation and simulation. Specifically, they could use phosphomutants of Ndc80 to explicitly define the FRET signature of unbound and bound Ndc80 molecules.

2) Is the Ndc80 bound fraction on a per kinetochore basis or a per kMT basis? This is a significant issue that is not discussed; it will nonetheless have significant bearing on the interpretation of the data. The calibration simulations used here are based on Ndc80 molecules binding to the microtubule lattice. But the experiments measure Ndc80 binding on a per kinetochore basis. This distinction is important to consider. Given a microtubule in its proximity, the binding of Ndc80 to the lattice is subject only to phosphoregulation (this is the implicit focus of the manuscript). However, the measured fraction of Ndc80's per kinetochore is also dependent on how many microtubules are attached. If the number of microtubules per kinetochore increases (this is known to happen from prometaphase to metaphase in other model systems), then the bound fraction of Ndc80 molecules will increase even in the absence of any chromosome-autonomous regulation of Ndc80 affinity. Without studying whether and how the number of kinetochore-bound microtubules changes, the authors cannot conclude that the bound-fraction increase is the result of an active regulatory mechanism.

Along the same lines, it is known that the human kinetochore binds ~ 20 microtubules in metaphase, but it has the capacity to bind ~ 25 microtubules. Therefore, it will contain a fraction of Ndc80 molecules that are always unbound. This will introduce an offset in their discussions of the bound fraction. The authors should note this in their Discussion.

3) Figure 2: One possible contribution to the variability of the FRET ratio for the "off-centered" pairs are that kinetochores in this population may have different attachment geometries (lateral vs. end-on), or be regulated by different biochemical systems (e.g. AurA) in different locations. The authors should comment on these possibilities as they can impact the "chromosome autonomous" conclusion.

4) In Figure 2D, it appears that for "centered" kinetochores, the NDC80 FRET fraction continuously increases throughout mitosis. However, it seems to me that NDC80 itself is required to generate centromere tension, by linking the dynamic microtubule plus-ends to the centromere. Therefore, does this imply that average kinetochore-kinetochore distances would also tend to increase continuously as more NDC80 molecules bind, perhaps recruiting additional kinetochore microtubules? If so, is this observed experimentally? If not, it would be useful to explain what effect a continuous increase in NDC80 binding would have on the centered sister kinetochore pairs, which would not affect the off-centered pairs.

5) Similarly, in Figure 3D, could the linear increase of NDC80 fraction with increasing K-K distance reflect a dependency of K-K distance on NDC80 fraction – e.g., as more NDC80 molecules bind, the K-K distance tends to be larger because additional kinetochore microtubules contribute pulling forces? The taxol-treated cells have reduced K-K distance and reduced NDC80 FRET fractions, but this result may be difficult to interpret since Taxol suppresses microtubule plus-end dynamics, and may change the flexural rigidity of the microtubules themselves, and so may alter NDC80 binding by itself. Thus, I worry that the conclusion that "tension is a primary regulator of NDC80-kMT binding during error correction" is perhaps not well established by the data in Figure 3D. It would be ideal if K-K distance could be disrupted without altering kinetochore microtubule plus-end dynamics (e.g., perhaps at the minus-ends?), and then data collected on NDC80 FRET fraction.

6) Centromeric tension and lagging versus leading kinetochores: This is an interesting and counterintuitive aspect of the data that went unremarked. The authors show that the bound fraction is a function of tension as well as the status of the kinetochore as lagging versus leading. This observation is counter-intuitive, because a pair of sister kinetochores should be under the same centromeric tension, but one of them is lagging while the other one leading for the vast majority of times. The observation likely hints at two different tension-bearing/force generating interfaces in the kinetochore, which was probably alluded to by the Sophie Dumont study from several years ago. It is important, because the presence of two load-bearing attachments forces one to think of the phosphoregulation of both.

7) Figure 5 and related text: The authors show that haspin inhibition abolishes the relationship between FRET ratio and K-K distance (centromere tension) without affecting steady-state levels of NDC80 binding. It would be stronger if they could specifically rescue tension-dependent in a 5-ITu inhibited context by force-localizing Aurora B to the centromere, if possible to do in a reasonable time frame. As a related point, in general this figure and section of the paper still do not directly show that Aurora B is directly responsible for tension dependence. Are there Aurora B inhibition data points across at least a few different amounts of centromere tension that could be plotted on Figure 5C to show this? It may help to move Figure 5—figure supplement 1 into the main figure since a lot of the interpretation in the text hinges on the comparison between 5-ITu and ZM treatment on the Ndc80 FRET ratios.
