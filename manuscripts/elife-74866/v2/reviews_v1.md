# Peer review - Round 1

Editors:
- Wenying Shou, https://ror.org/02jx3x895 University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74866.sa0](https://doi.org/10.7554/eLife.74866.sa0)

This is a multifaceted study of the epithelial to mesenchymal transition (EMT) in live cells. EMT is relevant for cancer, development, and wound healing. The authors were able to discern two possible cell transition path categories without multi-color labeling or other advanced experimental approaches, which could be impactful for other studies. The study draws on a wide range of experimental, data science, and modelling tools and techniques.


---

# Peer review - Round 1

Editors:
- Wenying Shou, https://ror.org/02jx3x895 University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74866.sa1](https://doi.org/10.7554/eLife.74866.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Epithelial-to-mesenchymal transition proceeds through directional destabilization of multidimensional attractor" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Gabor Balazsi (Reviewer #1); Michael Stumpf (Reviewer #2); Jian Liu (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Overall, all three reviewers are positive about your work. However, there are items that need to be addressed, which are summarised below. Note that the three reviews are attached in their entirety to assist your revision.

Essential points to be addressed:

1. How the existence of multiple reaction paths is or is not robust to e.g. multiplicative noise and other factors in the analysis.

2. What is the method's applicability to other cell lines, proteins, and cellular transitions.

3. Whether a simpler analysis would have given the same results.

4. Clearly state what the advance this paper has over the previous Science Advance paper (Ref. 11).

5. Improve clarity of your writing, including tidying up typos and references, explaining to biology audience the difference between Langevin and Fokker-Planck equations, providing justification of using Langevin, discussing how this system's transition is different from the typical analysis, explaining the plethora of computational methods deployed, and providing better illustration of morphological and textural features.

Reviewer #1 (Recommendations for the authors):

(1) In the Introduction, the definition of the saddle-node bifurcation is unusual. Specifically, the saddle-node bifurcation is described here as both the appearance of a saddle point and a new steady state, and then the merger of the saddle point with the original steady state. Typically, however, these are considered two different saddle-node bifurcations. In fact, there are systems exhibiting a single saddle-node bifurcation, when the saddle point never merges with the original steady state, so the system remains bistable even as the bifurcation parameter tends to infinity. See the wild-type circuit in PMID: 31754027 for an example.

(2) The way the system's transition is induced here is different from the way typical bifurcations are realized mathematically. Specifically, in mathematics the system's steady states are investigated while a bifurcation parameter is scanned – but each particular value of the bifurcation parameter is considered fixed. In contrast, in this experimental system the bifurcation parameter is time-dependent: intracellular TGF-β concentrations change as they equilibrate with the extracellular TGF-β levels. This difference should be mentioned and discussed, regarding the influx rate of TGF-β and membrane permeability. About how long does it take for intracellular and extracellular TGF-β to equilibrate?

(3) Related to the previous point, an experiment closer to the mathematical studies would keep cells in microfluidic chambers, perfusing media with constant TGF-β concentration that does not depend on time but may increase from chamber to chamber. This should be mentioned as a possibility for future studies.

(4) The analysis involves a plethora of computational and mathematical methods: PCA, active shape model, Haralick features, SOM, Dijkstra algorithm, Onsager-Machlup action, dynamics time warping, Focker-Planck equation, pseudopotential, Voronoi partitioning, finite temperature string method, etc. While all of this is impressive, there is a concern. Some parts of the text are difficult to follow, and the overall procedure is not easy to comprehend. To make this approach really useful to the EMT community, a knowledgeable biologist should be able to comprehend and reproduce the results. So, is it possible to get to the same conclusion with fewer and/or simpler computational steps? Are all the steps employed here necessary to uncover the two cell transition path categories? Moreover, how transferable is the methodology to other cell lines, other CPTs and other proteins? A highly sophisticated, multistep approach is probably less likely to transfer and generalize than a simpler one. All of this should be at least discussed, and possibly addressed by an attempt to simplify the steps, accordingly simplifying the text of the manuscript by reducing some of the jargon.

(5) Most of the methods are introduced and similar conclusions about the CPT paths are reached in the earlier Science Advances paper (Ref. 11.) using the same cell line, the same markers, and the same CPT. The authors should clearly state what is distinguishingly novel in this manuscript compared to their earlier publication.

(6) A more intuitive illustration of the morphology and texture features is needed. What cellular aspects do the main Principal Components contain? Are any morphology and texture aspects overrepresented in the first PCs? For example, it would be very helpful to illustrate the morphology and texture extracted, along with their computational analysis to obtain the numbers for a few cells: (i) in the E state; (ii) in the M state; (iii) in mid-transition with vimentin increases first; (iv) in mid-transition with concordant increase. This could be addressed by altering the current Figure 4, similar to Figures 3 and 4 in the Science Advances paper (Ref. 11.).

(7) The Langevin approach assumes uncorrelated Gaussian noise. However, most fluctuations of cellular molecules are neither Gaussian, nor uncorrelated. Moreover, the noise properties can depend on the deterministic components of the Langevin approach: F, x and t. What justifies the applicability of the approach? This should be discussed.

(8) For the 1 ng/mL TGF-β treatment, what would the actual reaction path look like (compared to the 4 ng/mL treatment)? Here the new trajectories are projected onto the RCs for the 4 ng/mL treatment "for comparison". What does this projection imply compared to a separate analysis of the 1 ng/mL treatment? What if the reverse is done: the trajectories of the 4 ng/mL treatment are projected onto the RCs of the 1 ng/mL treatment?

(9) Related to the above question, it is interesting that the new M attractor for 1 ng/mL treatment is closer to the E state. Does this mean that the attractor-based definition of the "M" state is stimulus-dependent? So how can we be sure there is an "E" and an "M" state if their definition changes according to the environment? Shouldn't these states be independent of the environment?

(10) It is interesting that some cells become mesenchymal in low TGF-β, and possibly even without TGF-β. Do any of these cells revert? It is understood that high TGF-β prevents reversion, but the plateau in Figure 5 implies that reversions may be possible at low or zero TGF-β.

(11) Are there any "early signs" of cells that will become mesenchymal? Could this be predicted based on the values, or fluctuations of numerical features or their correlation analysis?

(12) This manuscript is about environment-induced CPTs. On the other hand, CPTs can also occur stochastically in a constant environment. This distinction would be worth making to place the research in context, citing PMID:21414483.

(13) A reference is needed for TPT in line 151 and also for the Onsager-Machlup action in line 200.

(14) The phrase "round polygon" probably means convex polygon?

(15) CPT appears in the Abstract without a prior definition.

(16) References (16) and (17) are identical.

(17) Please watch the grammar! There are some missing or extra words, e.g., "instant OF time", "towards TO", etc.

Reviewer #2 (Recommendations for the authors):

Specific points:

Figure 1: The figure legend could be made clearer. The figure might give the impression that the data is sufficient to distinguish between saddle node and pitchfork bifurcation.

line 135: I would like to see an outline of what Haralick features are.

line 199-200: It would help to define in general terms what an action is.

line 203: reference 22 has nothing to do with reaction coordinates as far as I can make out. Did the bibliography get mixed up here?

line 262: in 1D all dynamical systems are gradient systems. References 28 and 29 are not the most appropriate references in this context. Most introductory dynamical systems books would suffice.

line 283-284: It may help some readers to learn more about the differences between Langevin and Fokker-Planck equations. Schnoerr et al., Journal of Physics A (2017) 50:093001 is a reference that I find very useful.

line 287: Is it possible to do better than "matches reasonably well"? Are there statistical measures by which this can be quantified? Or is it possible to explain why there is a mismatch.

line 319-323: I found the discussion about the intermediate states fascinating: I was wondering if this could be extended to include some of the arguments of PMC6238957 or similar? More generally, mathematically, for the systems considered here (in a deterministic regime) the Palais-Smale conditions or the mountain pass theorem would hold. MacLean et al., make such arguments less formally and more intuitive.

Finally, most other previous authors appear to have used the term quasi-potential to denote landscapes of differentiating systems. In solid-state theory and chemistry pseudo-potential appears to be favoured to describe e.g. effective electron potentials. I would recommend the terminology "quasi-potential" here.

Reviewer #3 (Recommendations for the authors):

1. The writing needs to be greatly improved. While some parts are arguably a subject of style/taste, the rest of the manuscript is littered with grammar mistakes. For instance, the "CPT" in Abstract needs to be defined first. On Lines 37-38: "different function, morphology, …" should be "different functions, morphologies…". On Line 48-49: "A cell is a dynamical system, and understanding a CPT process from dynamical systems theory …" should be something like "Considering cell as a dynamical system, understanding a CPT process from dynamical systems theory…".

2. Any results from deep learning critically hinge on the quality of the training set; otherwise, the automation can easily go wrong. In automatically characterizing the live-cell time-lapsed images, the authors need to provide the necessary baseline or the control in their deep learning method. If it is already done in their previous work, then the authors need to explicitly state and refer to it in the current paper. If not, then such a control measure in deep learning needs to be included in the Method.

3. Using time-lapsed images to reconstruct pseudopotential is a great improvement over the previous work. The question: How does the number of images points or the time-resolution along the reaction coordinate affect the reconstructed potential? The authors need to at least discuss the potential effects.

4. With the high-dimensional parameter space, the authors reconstructed the common transition paths of EMT. It is well known that cells exhibit large heterogeneity in terms of gene expression and dynamics. The question is: How can we reconcile the two opposing features?

5. The authors demonstrated the two parallel pathways in EMT with the same starting and ending states (e.g., Figure 3e). While the reaction coordinates of transition state along one pathway (vimentin PC1 and morphology PC1) are intermediate between the E and the M states (the right panel of Figure 3e), those along the other pathway are not (the left panel of Figure 3e). What is the physical nature of this largely non-monotonic change? And if possible, what is the functional role? In perspective, cell operates in the multi-dimensional parameter space. What the authors have characterized is only the subset. Possibly, there exist additional but essential parameters that remain to be explored. This way, the non-monotonic change in the reaction coordinates may reflect the projection from a higher dimensional space onto the two-dimensional parameter plane. For instance, cell mechanics may be another set of key parameters that underlie EMT, which has been demonstrated to display non-monotonic changes during EMT (see Margaron et al., Biophysical properties of intermediate states of EMT outperform both epithelial and mesenchymal states (bioRxiv, 2019)). I'd suggest the authors discuss the finding in a broader context.
