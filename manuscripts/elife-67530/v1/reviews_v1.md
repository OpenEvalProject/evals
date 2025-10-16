# Peer review - Round 1

Editors:
- Megan C King, Yale School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67530.sa1](https://doi.org/10.7554/eLife.67530.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This work combines experiments and simulations together with previously reported biophysical and structural observations to develop a structure-based model that provides mechanistic insight into the two functions of cohesin: cohesion and loop extrusion. This intriguing and informative manuscript will be of broad interest to those working in the fields of chromatin structure, chromosome biology and molecular machines.

Decision letter after peer review:

Thank you for submitting your article "A Brownian ratchet model for DNA loop extrusion by the cohesin complex" for consideration by eLife. Your article has been reviewed by 4 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) There was a consensus that the manuscript needs to be extensively edited to better introduce the reader to the structures described in the prior work from the group published in 2020. One approach suggested by the reviewers would be to present a series of increasingly complex representations that would help to position the reader to better understand the work, starting with a global structural view of the cohesin complex first that introduces the key elements: hinge, ATPase domains, kleisin and loading factors. From this point representations akin to the current Figure 1—figure supplement 1 will position the reader to fully understand Figure 1. Similarly, introduction of the key terms (e.g. "N gate", the geometry of "entering/exiting the cohesin ring") at the start and ensuring that the helpful general/fission nomenclature is used throughout the text and all Figures would be helpful. Last, clear articulation of what structures arise from high-resolution data versus structural modeling should be clarified.

2) Please clarify what assumptions are made and/or are implicitly defined in the modeling. Specifically, is the sequence of changes between DNA binding and cohesin conformation prescribed and are there any assumptions on whether DNA binding to the hinge domain is dependent (i.e. temporally linked) to the ATPase cycle? How are chemical kinetics combined with the bead dynamic simulation?

3) A common thread in the reviews relates to questions regarding the position, bending, binding and release of the DNA, which need to be addressed. DNA bending is mentioned in the text but it is not discussed quantitatively (and in the context of to the persistence length) particularly with regards to the initiation of loop extrusion. DNA conformation is also not communicated well in the Figures. Further clarification is needed to address what occurs upon DNA release – whether there are concerns about tangling – and discussing what prevents the DNA loop from sliding outwards from the cohesin ring to release the bending strain. Last, the authors should address what rules out the random binding of the DNA to the hinge module in the unfolded cohesin state, which upon locking the hinge and head together could result in a "backward" sliding with DNA being pushed back through the head domain.

4) The authors should discuss how their model impinges on (or is influenced by) the discrepancy between the rates of loop extrusion and measured ATPase activity.

5) The authors should include further discussion of how their work informs on other models for cohesin and loop extrusion. There is value in evaluating these other models more critically based on the findings reported in the manuscript.

6) The authors should address two issues related to the FRET measurements, namely 1) concerns over the sensitivity of the proximity of Scc3-C and Scc2-N and how this impinges on the modeling and 2) the functionality of the SNAP/CLIP-tagged proteins.

Reviewer #1 (Recommendations for the authors):

1. The manuscript will benefit from a clearer articulation of what information arises from previously described structures (for example conformation in the "gripping state") and what is structural modeling based on the available separated structural data. These details could be deduced from the description in the Materials and methods but it will help the reader appreciate the authors' arguments if it is stated in the main text.

2. Regarding the mechanism of the loop extrusion, there are some aspects that remain unclear. First, are there any assumptions on whether DNA binding to the hinge domain is dependent (i.e. temporally linked) to the ATPase cycle steps happening at the head domain? This question is relevant, as one might think that absolutely random independent binding of the DNA to the hinge module could also result in DNA binding to the hinge domain in the unfolded cohesin state, in which case locking the hinge and head together may result in a "backward" sliding with DNA being pushed back through the head domain.

3. Related to Point 2, what, if any, assumptions were made about the sequence of changes between DNA binding and cohesin conformation in the Monte-Carlo simulations? In the text, it is stated (ln 384-389) "When we then allow DNA to detach from the Scc3-hinge module and switch cohesin back to the gripping state, the system readily resets and primes itself for the next cycle (Figure 4D). Our simulations reveal that repeated rounds of the states: "gripping → slipping → DNA detachment from the Scc3-hinge module → gripping" results in continuous extrusion of DNA with an average loop size increase of ~ 30 nm per cycle". It is crucial to clarify whether the sequence of events described here was explicitly imposed or whether independent stochastic "gripping-slipping" and "DNA binding/detachment" were also considered in some simulations. In the latter case, what prevents the DNA thread from sliding back? Perhaps a discussion on what sets the directionality of the DNA translocation would help: is it DNA bending, timing of DNA binding at the hinge module, etc?

4. While the authors provide detailed descriptions of the simulations there are some aspects that would benefit from further clarification. For the Monte Carlo simulations, it is not clear how chemical kinetics was combined with the bead dynamic simulation: (1) DNA binding – what determines/switches which D bead is "currently interacting" with hinge or with head beads, (2) ATPase cycle – what determines the timing of switching from gripping to slipping state, (3) do the head beads change their interaction with the hinge bead, and if so what determines the switch? If not, some explanation for how random folding-unfolding results in directed translocation would be very helpful. Regarding the Monte Carlo steps, it is not clear what were allowed as random moves, i.e. from a given state how a new state was generated. For the diffusion-based model, a more detailed description (and perhaps a cartoon of the simulation model) would be helpful. Would it be correct to say that this model has two spatially fixed points through which a DNA polymer can perform a 1D random walk for "diffusion only", with a constant directed polymer translocation through one of the points was added in "diffusion plus ratchet"?

5. The authors suggest that their mechanism generally results in an asymmetric loop extrusion (Figure 6A left). Once DNA unbinds from the hinge module, what prevents the DNA loop from sliding outwards from the cohesin ring to release the bending strain?

6. In the introduction, the authors described three proposed models for loop extrusion; in the discussion it would be helpful to "circle" back and compare the presented model with these prior considerations to highlight commonalities and incompatibilities.

7. The authors describe the role of kleisin position relative to the DNA much later in the text rather than introducing the concept with the slipping state. Explaining it earlier will help in better understanding the terminology and the key difference between the "topological entry" and "loop extrusion" modes.

8. Bars in Figure 2 might be somewhat misleading as their height does not represent values. I would suggest using a scatter plot instead.

9. A few points on terminology: 1) "Loop extrusion by biased Brownian fluctuations" (l.41) – it seems that fluctuations are not biased, but instead repeatedly get caught in one "loaded" conformation, relaxation of which drives the directed translocation. I would consider more precise wording to highlight the beauty of the mechanism. 2) 'kleisin path' (l.318) – perhaps, 'kleisin chain' as path is used to refer to temporal changes in conformations throughout the paper.

Reviewer #2 (Recommendations for the authors):

1. In higher eukaryotes, chromatin seems to have clusters of nucleosomes (e.g., PMID: 32967822; PMID: 28712725; PMID: 30044984), but not stretched nucleosome fiber. It might be better to discuss that this nucleosome clustering can be a more severe issue for cohesin's loop extrusion activity.

2. Page 11. "Maturation of the bent DNA in the gripping state.… Brownian motion will have.…" These sentences are unclear to me and should be rephrased.

3. The reference (Suhas et al., 2017) should be Rao et al., 2017 (PMID: 28985562 ).

Reviewer #3 (Recommendations for the authors):

1. Please provide a global structural view of the cohesin complex first. It is provided in figure supplement 1 but it has its own problem (see below), and I could not understand Figure 1 until I spent a long time staring at figure supplement 1. For those who are not up to date on cohesin structures (such as me), cohesin is a ring that can open and close at the hinge and at the ATPase domain and DNA passage through the gap in ATPase domain is modulated by kleisin and cohesin loader, and I could not understand figure 1 description and figure 1 because I could not place different parts in the cohesin complex in my imagination.

2. Figure 1 supplement is probably still too complex. Colors are confusing because Rad21 is shown in pink and its color coding is shown above the figure but Psc3 is shown in a similar color and its color coding is missing in the color guide above the figure. Also, fission yeast names are used here instead of the helpful genericfission naming scheme used elsewhere in the paper so it is very challenging to connect figure 1 to figure 1 supplement. The authors should try to reduce mental gymnastics on the part of the readers!

3. Line 272. "The DNA path shown in Figure 3A, panel a, highlights the position of such a bend, based on our DNA-protein crosslink mass spectrometry data (Higashi et al., 2020)."

– Bending of DNA is mentioned but the figures do not make DNA bending obvious. It is not clear where the bend is, looking at the figure. Some quantification is needed to aid the reader in their assessment of this statement, whether there is a significant degree of bending as the authors claim.

4. Line 280. "ATP hydrolysis, resulting in ATPase head gate opening and Scc3-hinge and Scc2-head module uncoupling. This will initiate a swinging motion of the Scc3-hinge module and proximal coiled coil, with a pivot point at the elbow"

– There appears to be a logical jump here. Why would this cause a swinging motion? In addition, a subsequent sentence refers to this movement as Brownian motion, which is even more confusing. Statement such as 'energizing the swinging motion' is not helpful because it is not precise enough.

5. Line 293. 'fast DNA off-rate'. Rate is high or low, not fast or slow, because it is a quantity.

6. I found some of the terminologies confusing. I suspect the readers will have difficult in understanding what an N gate is, for example.

7. Figure 3 description should make it explicit that DNA loop is inserted into the cohesin channel.

8. Figure 3Aa, it appears to me here that DNA is behind both of the yellow protein segments, going up and down, and panel Ab shows a yellow arrow that suggest that something happens so that now one of the yellow segments is not behind the DNA. However, their model, after considering staring at the figures on my part, seems to assume that DNA is simply bent to form a loop and this loop is inserted so that there is no DNA segment behind the yellow protein segments. Figure 3Aa should be redrawn to avoid misleading the readers. Also, what the yellow arrow means needs to be explained.

9. They need to confirm that SNAP/CLIP tags and labeling do not perturb proteins' function. They may have done this in their 2020 Mol Cell paper that introduced the tagged constructs for FRET analysis and if they have done so, it should be mentioned in this manuscript still.

10. Other models for loop extrusion are mentioned in Introduction but it is difficult to tell how they are different among themselves and from the model proposed here just from reading the text. In addition, the authors do not attempt to evaluate other models based on the findings reported here, and that seems to be a missed opportunity for the discussion sect

Reviewer #4 (Recommendations for the authors):

The wording "Enter/Exit cohesin ring" is unclear. The authors should explain which side is "enter" and "exit" in the text and/or corresponding figure.
