# Peer review - Round 1

Editors:
- Yibing Shan, DE Shaw Research United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.31715.021](https://doi.org/10.7554/eLife.31715.021)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Energetics and Conformational Pathways of Functional Rotation in the Multidrug Transporter AcrB" for consideration by eLife. Your article has been favorably evaluated by Richard Aldrich (Senior Editor) and two reviewers, one of whom, Yibing Shan (Reviewer #1), is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Aiming to elucidate the detailed structural mechanism of AcrB RND transporter, this study applied the string method for conformational free-energy calculations on a supercomputing platform to identify the minimum free energy pathway of the functional rotation of AcrB. The all-atom simulations follow the conformational change of the transporter including the travel of the drug molecule (minocycline) from the binding pocket through the gate and finally release of the drug molecule, showing that the protonation of Asp408 in a transmembrane helix of the Binding protomer drives the process. This work represents potentially important progress in our understanding of the molecular mechanism of the transport process in AcrB.

Major points:

Given the readership of eLife, the manuscript should include a brief and high level description of the simulation techniques (the string method, the umbrella sampling, and the alchemic free energy calculation) in the main text in terms that a reader unfamiliar with molecular dynamics simulations can relate to. What are the basic ideas and premises behind the approach? The manuscript should explain the free energy reported in Figure 2, stating clearly that this is the free energy for the whole system if that's the case.

The specific procedure should also be explained in more detail as is it is difficult to follow. It would also help if the references to the string method in the last paragraph of the Introduction were made in a more structured way – with explanations, rather than the current lumping together of a large number of very diverse papers ranging from mathematical principles all the way to practical applications.

This work only attempts to distinguish two possible schemes. In realty the process of the functional rotation is probably more complicated, possibly involving protonation of not only Asp408. For instance, Asp924 is located in a quite hydrophobic local environment and its protonation is conceivable. The proton could even be passed from Asp408 to Asp924 by the single water file connecting them. Ideally some new simulations should be performed to address this. At the very least this possibility should be more carefully discussed.

The explanation for the increase in free energy after the minima (Figure 2A) invoking drug release without uptaking new drug molecule without offering any reasoning or evidence seems casual. The reviewers suggest that the apparent high free energy might be due to the fact that any change of protonation state is not accounted for in the simulations. The authors should consider deprotonation of Asp408, which should occur at the end of the extrusion phase according to the proposed scheme (Figure 6). The authors should also consider, as aforementioned, protonation of other residues (e.g. Asp924) following Asp408 deprotonation (a single water file seems to connect Asp408 and Asp924).

Why is the drug released from the BEA complex in System 1, if the protonation of the original E protomer stabilizes the whole complex, as shown in the image 5 of Figure 2A? How is the BEA configuration changed to EAB after protonation of the second protomer as suggested by Figure 1E?

The analysis concerning the dynamics coupling of the transmembrane domains and the porter and the funnel domains (Figure 5) is too preliminary and very unintuitive. Some abstract metric of share conformation may show that the coupling is present, which is hardly surprising, but biologically it is much more interesting to discuss/demonstrate what interactions are behind the coupling.
