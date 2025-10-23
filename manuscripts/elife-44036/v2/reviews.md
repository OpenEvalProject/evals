# Peer review - Round 1

Editors:
- Gail Mandel, Oregon Health and Science University United States

Reviewers:
- Claude Desplan, New York University United States
- Michael B Eisen, University of California, Berkeley United States

## Review text

DOI: [10.7554/eLife.44036.025](https://doi.org/10.7554/eLife.44036.025)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Neuroblast-specific chromatin landscapes allow integration of spatial and temporal cues to generate neuronal diversity" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Gail Mandel as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Kevin Struhl as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Claude Desplan (Reviewer #2); Michael B Eisen (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

This work describes an elegant application of a recently developed technique (targeted DAMID) to determine chromatin changes mediated by transcription factors that regulate spatiotemporal gene expression in Drosophila neuroblasts. Authors provide results suggesting that the chromatin changes mediated by the spatial factors establish a permissive environment for activity of the temporal factors important in lineage control (intersection of spatial and temporal identify mechanisms).

There were few major concerns identified by all three reviewers, who were very enthusiastic about the novelty and rigor in the technique application and the importance of the question. These concerns are easily addressed and don't require further experimentation (please see attached reviews). However, one concern that merits more attention is that the data in Figure 7, the crux of the conclusion for integration of the chromatin signaling, does not appear to be to the same level of rigor as the technical aspects. Authors need to address this point, by providing either more convincing data in Figure 7 or, minimally, providing more details in the results and interpretation of Figure 7 data, as well as toning down wording in the title, Abstract and Discussion that they have proven intersection, as opposed to generating data that is consistent with this conclusion.

Essential revisions: Figure 7 data and toning down language if no more data is provided.

Reviewer #1:

This work is meant to address the intersection of temporal and spatial information leading to neuronal diversity (distinct neuroblast lineages), an intersection that has received very little traction. The work takes advantage of the huge breadth of knowledge of the spatial transcription factors (STFs) and hunchback transcription factor (TFF) cascades for neuronal lineage control in Drosophila. The study also applies a new method of binding site identity (DAMID) that has not been applied previously for small numbers of cells or for addressing this specific question. Applying this method, apart from the question of integration signaling, the authors have identified 100 new targets that could potentially contribute importantly to neuronal specification.

Shown in an elegant manner is that STF Gsb and DamHb bind within open chromatin, defined by DAM analysis, in a neuroblast-specific manner. Because Gsb binds prior to Hb, authors propose a sequential model wherein open chromatin induced by Gsb binding is required for subsequent binding of Hb. However, their data in support of this model (Figure 7) falls short of showing causality and doesn't seem to be done at the same level of rigor as in the prior experiments, leading to somewhat of an anticlimax. For example, there is no direct evidence presented that the STF open chromatin is sufficient for binding of Hb, only that the binding of the two factors is enriched in close proximity in open chromatin. Additionally, the data in Figure 7B is not completely convincing – the binding enrichment curves are quite broad and appear very noisy, suggesting that the n value of # peaks is very small, although the Monte Carlo analysis shows significance (throughout the figures authors should provide an n value in their plots). While I think the work represents a clever adaptation of the technique, rigor for establishing the technique, first demonstration of in vivo binding of Hb, identification of potentially new factors important in specification, and setting the stage for attacking an important unanswered question, I think the question is still, well, an open question. In their Discussion, authors indicate that experiments to determine causality of Gsb binding/open chromatin for Hb binding lie outside the scope of the paper. Agreed, such studies would involve further work, but as it stands the current study doesn't support the bold title that the chromatin landscape allows integration. The Abstract wording is more accurate, but saying in the Impact statement and Introduction that the integration is due to and support (as opposed to consistent with) the sequential model, and asking whether similar mechanisms occur in vertebrates, seems overstated based on the current data.

Unless I missed it, authors do not state explicitly precisely how close the Hb and STF sites of enrichment are? Related to this, in terms of strengthening the correlative data, authors might consider plotting the distributions of distances of the closest Gsb peaks (or motifs) from the peak center of the Dam:Hb peaks and doing the same for other "control" STF or TFFs/motifs Chip data. Authors indicate that they didn't see any other motifs close to Hb sites but it wasn't clear whether the analysis was genome wide? It might also be optimal for authors to perform their own ChIP experiments to make this critical point. Regarding the Discussion. How does Gsb open chromatin – must be recruiting enzymes? Anything known about a Gsb complex? Are the Gsb binding sites associated with enhancer chromatin marks?

Reviewer #2:

This a very carefully crafted manuscript that analyzes how spatial and temporal information are integrated in neural stem cells to generate the large diversity of neurons in the ventral nerve cord of Drosophila.

The authors wanted to assay the mechanisms of molecular integration between the two sets of transcription factors (TFs).

They chose to look at the binding sites for the best known temporal TF, Hunchback (Hb) in two spatially distinct neuroblasts. Because of the very small number of neurons available in each embryo, the authors chose to use a very clever method initially developed in Andrea Brand's lab, TaDa. This method relies on the specific expression of a Dam methylase fused to the TF to test in specific cell types, but requires difficult adjustments as Dam can be very toxic even at low concentrations.

What makes this paper special is the very careful evaluation of the Gal4 lines used to mark two specific neuronal lineages, but more importantly the evaluation of how Dam-Hb functions. This allowed the authors to evaluate the differential binding of Hb to its targets in the two lineages. These differ significantly, suggesting that spatial information instructs the ability of Hb to bind to its (important) targets, likely through opening of chromatin, which they tested.

For this purpose, they also used Dam without its targeting moiety: even with the minuscule number of cells, they could see that there is a correlation between differential open chromatin and Hb binding. It is quite amazing that they got this to work but the controls appear to be fine. If this works that well, others should use this approach before single cell ATACseq becomes available!

The spatial transcription factor Gsb expressed early in the lineage appears to be responsible for this opening.

In conclusion, the use of the very powerful and highly focused TaDa technique allowed the authors to propose a model where chromatin is differentially opened by spatial TFs which allow the same temporal TFs to define distinct lineages. I am impressed by the technical sophistication of the paper and the care with which this has been done, which led to this important conclusion.

Of course, I would have liked to see other spatial and other temporal TFs being tested but in keeping with the spirit of eLife, I think that the paper makes an important enough contribution to be published without much change.

Reviewer #3:

The meat of this paper is the use of cell-type specific DamID to compare Hunchback (Hb) binding in two populations of neuroblasts distinguished by the expression of different spatial transcription that both respond to a pulse of Hb expression to make distinct neurons. The authors establish through a set of control experiments and comparisons to other data the efficacy of using specific expression of Dam:Hb to identify Hb target sites, and the viability of the neuroblast specifically expression Dam:Hb using cell-type specific drivers. The results are pretty straightforward: Hb binds to different targets in these two neuroblast subpopulations. They then show that this differential binding corresponds to differential chromatin accessibility, leading to their primary conclusion, that the differential binding of Hb (and presumably other temporal transcription factors) is due to the establishment of distinct chromatin states. They present data suggesting that the spatial transcription factors Gsb might be responsible for establishing these differential states in one subpopulation, lending support for a general model for neuroblast specification in which spatial transcription factors create a unique chromatin state that shapes how temporal transcription factors create identity.

I found the data generally compelling and don't have any major issues. Of course this is just binding, measured indirectly with a technique that whose pitfalls are not well established, and the evidence for STF involvement in establishing chromatin states is based on one factor. But as a first pass it's good data of great interest that warrants publication.

One thing confused me. The Abstract says:

"Profiling chromatin accessibility showed that each neuroblast had a distinct chromatin landscape: Hunchback-bound loci in NB5-6 were in open chromatin, but the same loci in NB7-4 were in closed chromatin."

I assume this is just poorly worded since it seems to contradict what's said in the paper (The data show that Hb binding in NB7-4 is in open chromatin in NB7-4)? I'm putting this in the major comments section since having an Abstract that says the opposite of the paper isn't good.
