# Peer review - Round 1

Editors:
- Rohit V Pappu, Washington University in St Louis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67176.sa1](https://doi.org/10.7554/eLife.67176.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

The concept of solubility products will likely be useful as a tool for experimentalists studying the prospect of buffering via condensate formation in systems driven by heterotypic interactions.

Decision letter after peer review:

Thank you for submitting your article "Solubility product governs the concentration threshold for formation of biomolecular condensates" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by José Faraldo-Gómez as the Senior Editor. All reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions (for the authors):

1. Please refocus the title, abstract and scope to highlight the proposal/finding that the solubility product "rescues" the concept of buffering even in systems where heterotypic interactions drive phase transitions. The consensus is that the solubility product might be rather useful, if it can be readily calculated, to set expectations regarding thresholding/buffering in systems with heterotypic interactions, i.e., all biomolecular condensates.

2. Please improve the overall scholarship to place the work in the appropriate context. Please note that Choi et al., previously explained why the dilute phase concentrations of specific components need not stay fixed when phase separation is driven by heterotypic interactions. Please see Figure 12 and the accompanying discussion in https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007028.

Please also note that Deviri and Safran have introduced a physical theory for how buffering can be achieved when phase separation is driven by heterotypic interactions. Please see, please cite, and please include a suitable discussion of:

https://www.biorxiv.org/content/10.1101/2021.01.05.425486v1.

3. Please eliminate all remarks about freshman chemistry or high school chemistry.

4. Please provide a mechanistic explanation for the implications of solubility products setting thresholds.

5. The consensus is that the section on the effects of linkers detracts from the focus of the manuscript. A detailed and rigorous treatment of this subject has been published in eLife by Harmon et al.,. We recommend that the revised manuscript exclude all results beyond Figure 7. This, we believe, will sharpen the focus, highlight novel aspects, and avoid overlap with work that has come before.

6. The reviewers have raised specific concerns and weaknesses regarding the solubility product. It is a useful concept that touches base with percolation transitions, but not necessarily with the rigor of concepts underlying phase transitions. Specifically, the connections between solubility products and slopes of tie lines needs to be established. We believe that this is beyond the scope of the current manuscript, but it will be very helpful to discuss this issue in a revised Discussion section. Please also note that formal order parameters are not being used in either simulation paradigm for defining phase separation.

7. Please provide a synthesis to explain how either simulation paradigm and the calculation of solubility products can be used to analyze experimental data. In doing so, please spell out the type of experimental data that will come in handy in testing the hypothesis that the solubility product sets an upper limit in systems with heterotypic interactions, thereby enabling the field to assess where the buffering capacity lies in distinct multicomponent systems.

8. And please consider presenting analyses in terms of amplitudes of fluctuations. These will likely help in paring down the number of panels that one presents for each system.

Reviewer #1 (Recommendations for the authors):There, unfortunately, are far too many concerns to be raised with regard to the technical and theoretical aspects of this work. A lot of new jargon terms are introduced without connecting to established terminology. The work on linkers is a minimalist redux of that of Harmon et al. The "dimer trap", also explained by Harmon et al., is a redux of the work of Wingreen and colleagues. The unique insight here has to do with the finding / proposal that the solubility product sets an upper limit on the joint concentrations, and hence appears to rescue the concept of buffering in systems with heterotypic interactions. Recent work from Deviri and Safran and from at least one other lab have introduced the concept of heterotypic buffering and provided rigorous thermodynamic descriptions, in the language and formalism of slopes of tie lines, focusing on chemical and mechanical equilibria to explain the full range of buffering capacities realizable as a consequence of the interplay between homotypic and heterotypic interactions. If we remove all the parts of the current manuscript that are best described as redux, then we are left with the solubility product and the rescue of buffering as the novel insight. What is lacking is a rigorous connection to the concepts of phase separation and percolation, achievable only through the calculation of full phase diagrams or at least coexisting curves and the demonstration that the solubility product is invariant along tie lines, and it should be true for all tie lines.

Reviewer #2 (Recommendations for the authors):

– The resolution of the cluster sizes is quite low for the non-spatial simulations, showing only 4 bins, whereas it is much higher for the spatial ones. Why so low?

– The movies are helpful in observing the dynamics, but what are the Spring constants?

– Does Ksp still hold in Figure 5 when the Stoichiometry of components is not 5:3?

– In Figure 6, what is the fit function to the dots?

– Do all sites retain excluded volume, even when they are bound to other sites?

– What rate constants were used? What was the integration time-step? Are the results sensitive to these choices?

– I think mentioning freshman/high school chemistry once in the paper is enough. The repeated references in the discussion to the age at which we all should have learned this start to sound like a failure of the field. A text book reference could instead emphasize that the concept is old and well established.

Reviewer #3 (Recommendations for the authors):The authors claim that the solubility product is a simple yet useful concept to study the phase boundary, but in fact, the solubility product is a specific realization of a much more general concept of the reaction quotient (Q) and the equilibrium constant (K), which is also from freshman chemistry. Hence, their simulation data just show that at low concentrations Q is smaller than K, and after Q reaches K, it remains constant. What is the benefit of using Ksp instead of more general K?

Unfortunately, it seems to me that there are almost no new findings relevant to the field of phase separation biology. Importance of the linker flexibility and the sticker spacing in phase separation have been known for a while, and the valency effect as well. However, the technical advancement (or applications) might be useful to the computational field, so I strongly recommend this paper for publication in a more technical journal for computational work. I don't think that this manuscript meets the eLife criteria.
