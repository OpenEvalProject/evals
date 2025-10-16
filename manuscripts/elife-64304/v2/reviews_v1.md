# Peer review - Round 1

Editors:
- Aaron Frank, University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64304.sa1](https://doi.org/10.7554/eLife.64304.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Using molecular dynamics simulations, along with some structural and bioinformatics analyses, the authors of this manuscript try to explain why two closely related GTPase homologs, RND1, and RhoD, have antithetic effects on plexin regulation. Because plexin signaling regulates several critical biological processes and several diseases are associated with disrupted plexin signaling, understanding the basis of plexin inhibition and activation could provide key molecular insights into this plexin-mediated pathway; as a result, this work will have a broad audience. The model put forward in this work is a valuable framework for generating additional structure-based hypotheses aimed at teasing out further insights into the antithetic effects of RND1 and RhoD on plexin regulation.

Decision letter after peer review:

Thank you for submitting your article "The structural mechanism underlying the antithetic effect of homologous RND1 and RhoD GTPases in plexin regulation" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by José Faraldo-Gómez as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Alex Dickson (Reviewer #2); Matthieu Chavent (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

Using molecular dynamics simulations, along with some structural and bioinformatics analyses, the authors of this manuscript try to explain why two closed related GTPase homologs, RND1, and RhoD, have antithetic effects on plexin regulation. Because plexin signaling regulates several critical biological processes and several diseases are associated with disrupted plexin signaling, understanding the basis of plexin inhibition and activation could provide key molecular insights into this plexin-mediated pathway; as a result, this work will have a broad audience. However, the reviewers have some reservations that the manuscript's strong claims are based on limited simulation data of a large multi-component molecular system whose structure was built using homology modeling. Therefore, aspects of the structure determination and modeling need to be clarified to fully support the authors' claims. The reviews have also suggested several improvements that could make the paper more readable and make the statistical analysis of the molecular dynamics simulations more rigorous.

The reviews' consensus was that the work presented here is potentially suitable for publication; the combination of X-ray crystallography with extensive modeling appears to provide new insights into the molecular basis for the interaction of plexin with each GTPase. However, as the structural effects described are quite subtle, additional analyses and modeling will be necessary to fully validate the mode of association of these two GTPases with both the membrane and the plexin dimer.

We request that the authors make a note of and respond to the following comments, in addition to the essential revisions listed below:

Essential revisions:

1. The primary concern of the reviews is the quality and built-in uncertainties of the initial models. Currently, the manuscript lacks consideration and discussion of the sensitivity of the results presented to the initial models. As the authors are most likely aware, the effect of the initial structure on the observations made on an MD trajectory can extend beyond the trajectory itself, depending on its length and the type of observable considered. Based on the data provided, it is unclear whether the conclusions are insensitive to the assumptions made in the construction of the initial homolog model. As such, the reviewers request that the authors carry out additional simulations with alternative models that are similarly plausible and yet meaningfully different from the models used in current version of the manuscript.

2. On a related note, the authors should comment and include a discussion in the updated manuscript on the validity of the domain-swapped X-ray structure.

3. The simulations are short relative to the state of the art, which is especially important for such large systems. To achieve full convergence, longer simulations or enhanced sampling is techniques may be required. Is there a reason why enhanced sampling methods were not employed? What metrics were employed to ascertain the statistical significance of the results presented.

4. The conclusions are declarative, but simulation results can only make predictions, and they should be stated as such. For instance, the authors state in the last sentence of the first paragraph in the Discussion that: "In short, we reveal an allosteric mechanism that regulates plexin dimerization involving cell membranes, the regulatory GTPases, the RBD domain, and the buttress segment (Figure 5F)." At best, one can say that "…we reveal a possible allosteric mechanism." Even if the additional modeling requested above demonstrates that the conclusions are robust to the initial models, the authors will need to soften their claims and update the title accordingly to reflect that these are just predictions. Otherwise, their simulation data on its own are not strong enough to support their claims.

5. As mentioned by the authors in the Discussion section, the inner leaflet of the membrane is constituted by different negatively charges lipids which are known to have a role in signaling. One can cite especially the PIP2/3 lipids. Here, the authors have used a membrane composed on 7:3 ratio of POPC:POPS. It would be useful for the reader to explain this choice and maybe to run new simulations to see the action of the PIP2/3 lipids on the plexin/GTPases complex. It would also be valuable for the reader to see if negatively charged lipids may be differently attracted by RhoD and RND1. This may reinforce the authors' hypothesis and also inform the readership on how protein may drive the formation of lipid nanoclusters, which may have consequences for GTPases signaling.

6. The system models were constructed with a membrane composed of POPC in the outer leaflet and of a ratio of 7:3 POPC:POPS for the inner leaflet. While POPS lipid can be seen as a proxy for negatively charged lipids, there are quite important negatively charged lipids missing, such as PIP2 and PIP3. It is now quite clear that these lipids can play a role in cell signaling. Thus, adding PIP2/3 lipids into the model may further validate the authors' claims with a more biologically relevant membrane.

7. The author claims that the movement of RhoD alpha helix αi is due to allosteric changes. Displaying the full unit cell shows crystal packing contacts, which may affect the position of this αi helix. Atomistic simulations may help to assess the stability of the structure of RhoD-RBD complex in solution and confirm the position of the αi helix.

8. It is unclear how the authors have chosen the orientation of RND1 and RhoD towards the membrane. Are there specific references mentioning the position of RND1 and RhoD – or other homologous GTPases – towards the membrane? Would it be possible to randomly position these structures away from the membrane and perform MD simulations (maybe using low-resolution representations such as CG models to save computing time) to assess the preferred positioning of the respective structures?

9. Given the manuscript's bold claim, the authors must include a discussion about the testable hypotheses the emerge from their work and how they can be tested.

10. A key point of this study is that what differentiates RND1 and RhoD are the lengths and the number of positively charged residue in the C-terminal tail, all of which the author could obtain from the bioinformatic analysis as presented in Figure 6, without requiring simulations. Could the reviewers comment on the value added by the simulations?

11. The structures of the different models considered should be made available on a citable website such as ZENODO. This would be useful to other research teams (both computational and experimental) to continue to develop new hypotheses from this work and continue to build further experiments. This will be beneficial both for the modeling community (to expand on this work) and the authors (to be credited beyond the results presented in this manuscript).
