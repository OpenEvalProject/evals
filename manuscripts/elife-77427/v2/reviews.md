# Peer review - Round 1

Editors:
- Patricia Bassereau, https://ror.org/04t0gwh46 Institut Curie France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77427.sa0](https://doi.org/10.7554/eLife.77427.sa0)

This paper presents a method to identify membrane proteins in native cell membranes based on a combination of single molecule AFM and an unsupervised clustering procedure to identify clusters of single-protein curves. This original approach represents a definitive step forward for AFM technology and methodology, which can generally only be used to characterize purified biomolecules of known identity.


---

# Peer review - Round 1

Editors:
- Patricia Bassereau, https://ror.org/04t0gwh46 Institut Curie France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77427.sa1](https://doi.org/10.7554/eLife.77427.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Unfolding and identification of membrane proteins in situ" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Richard Aldrich as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Aaron T Blanchard (Reviewer #2); Rafael Tapia-Rojo (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

The 3 reviewers and I have considered that your approach represents a very interesting method to identify proteins in a native membrane environment. We suggest some points that should be improved to reinforce your manuscript, but we do not request new experiments.

Essential revisions:

1. The utility of the technique should be better motivated. Its advantages, limitations and future directions (in particular, considering the low yield) should be discussed more thoroughly.

2. Although we think that the computational analysis does effectively take care of some issues listed below, could you explicitly address the following points in your discussion:

a) Can you confirm that shortened traces are discarded at the computational stage, eliminating those corresponding to attachment at arbitrary positions or loss of tip-protein interaction during the experiment? How do you take care of discrepancies between the contour length and the length measured by mass spectroscopy?

b) What happens if the protein has different conformations corresponding to different force traces?

c) What happens if the protein interacts with other proteins, which could influence the traces?

3. Some concerns were raised about the reproducibility of the technics. The number of samples, number of cantilevers, number of curves for each sample, number of clustered curves found by the computational algorithm, etc… should all be reported explicitly in the supplementary information.

Reviewer #1 (Recommendations for the authors):

Statistical reporting should be improved. For each clustered dataset that is presented, the number of total curves, filtered curves, curves of various classes etc… should all be reported.

The software/code for the clustering and analysis algorithms should be made publicly available, along with the raw datasets.

Figure S2: the precise method for cell 'unroofing' should be schematically diagrammed better so as to allow others to attempt to reproduce it. The exact procedure is not clear to me.

Figure S4 shows force (y axis) vs. contour length (x-axis). What is the equation they use for this transformation? It should be reported or a reference provided

Figure S11: How is the cutoff on the number of clusters decided? i.e., for DRG why were the top 15 clusters taken and not the top 10 or top 18?

Reviewer #2 (Recommendations for the authors):

To be more specific about my general critiques: The introduction does not paint a particularly clear vision of the specific types of new knowledge that could be gained from this technique that could not be obtained from existing approaches. As such, I did not feel particularly excited until I reached the Results section. Furthermore, by the end of the Results section, I didn't feel convinced that the unique capabilities of the technique had been demonstrated. The subsection at the end of the Results section, titled "structural insights from SMFS", provides one interesting insight using the large dataset. However, in my opinion, the authors don't effectively link this insight to their new technique. How did this new technique lead to this structural insight in a way that wouldn't have been possible otherwise? Furthermore, for a study that unveils a new method such as this, I would expect one or two more subsections that illustrate additional pieces of knowledge that could be obtained thanks to this new approach. I don't think that the insight presented is interesting or useful enough to stand alone as the only new piece of scientific knowledge presented in this paper.

Reviewer #3 (Recommendations for the authors):

I believe that the manuscript deserves publication. I have some comments, mostly related to recognizing the method's limitations and envisioning potential directions to overcome (or at least mitigate) them. The manuscript would benefit from a richer discussion in this direction.

1. The authors constantly speak about protein unfolding or rupture peaks, but I believe that this is not correct or at least precise. Different from in vitro experiments pulling on proteins tethered to the substrate, here, the mechanical resistance arises from pulling helical groups out of their native membrane environment. This should be specified. Further, there is very little (or almost no) comment on how the magnitude of the force peaks correlate with the expectations (if there can be any expectation). For example, in Fig. 6, the expected "rupture regions" are guessed based on the contour length increments arising from pulling out that protein fragment, right? Do the observed forces relate to the expected forces, given that some proteins exhibit a considerable heterogeneity of peak heights (for example, TRPC6). Can the authors elaborate on the mechanical dimension of their identification method? Can this information be combined with the contour length increments to deliver an additional parameter for protein identification?

2. The authors mention that a limitation of the pipeline is the possibility of merging in the same cluster of different proteins that could exhibit similar force-extension patterns. I think that, in addition to this, another limitation could arise from proteins that exhibit heterogeneous patterns, meaning that they can be pulled out of the membrane in different ways. Have the authors accounted for this or observed protein clusters that could correspond to the same protein species? I guess that this situation could be identified by inspecting clusters with the same total contour length and maybe recurrent patterns (perhaps this heterogeneity can arise only when pulling out a fraction of the protein, likely those involving lower forces). Please comment on this.

3. As the authors acknowledge, a limitation of the method is the very low yield, as they can only identify a tiny fraction of the total membrane proteome. Can the authors comment on potential ways to improve this? Developing some chemical strategies for achieving specific pickups could help in this direction. Non-specific AFM is highly ineffective, and there are many developments to overcome this limitation in single-molecule experiments. For example, proteins can be covalently anchored to substrates from their N-terminus with the appropriate chemistry. By implementing a similar strategy with their cantilever, the fraction of membrane proteins pulled from their N-terminus could be dramatically enriched. I'm not asking that the authors do this, but at least comment on how the experimental procedure could be improved to achieve a higher experimental yield.

4. Could this pipeline be extended to identify cytoplasmatic proteins? Can the authors discuss this possible future direction?
