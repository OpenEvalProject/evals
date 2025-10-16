# Peer review - Round 1

Editors:
- Qiang Cui, https://ror.org/05qwgg493 Boston University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82447.sa0](https://doi.org/10.7554/eLife.82447.sa0)

Using state-of-the-art molecular dynamics simulations, the authors discuss the potential binding sites of drug molecules to the flaviviral envelope. Moreover, using constant pH simulations, they discuss the functional relevance of a cluster of ionizable residues in a cryptic site at the domain interface. These results have provided novel mechanistic insights into the pH-dependent conformational changes of the envelope protein and cryptic binding sites in the envelope protein that can be targeted for inhibiting viral infection.


---

# Peer review - Round 1

Editors:
- Qiang Cui, https://ror.org/05qwgg493 Boston University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82447.sa1](https://doi.org/10.7554/eLife.82447.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A pH-dependent cluster of charges in a conserved cryptic pocket on flaviviral envelopes" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen José Faraldo-Gómez as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Jana Shen (Reviewer #2); Mikael Lund (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) A more thorough analysis of the constant pH simulations, especially whether the cryptic binding site(s) identified with fixed-protonation-state simulations is (are) likely to change when pH dependence is included. Analysis of charge capacitance is also recommended.

2) Further clarification of some methodological details, such as the treatment of membrane.

Reviewer #1 (Recommendations for the authors):

Overall, the study has been conducted and analyzed rather carefully. I have only a few questions.

1. Glycan has been shown to be important in several recent SARs-Cov-2 spike protein simulations. The authors didn't include the glycan component explicitly. It will be useful to further comment on potential technical challenges that motivated this approximation and its limitations.

2. Many viral envelop proteins (e.g. the HIV) contain a rather high concentration of cholesterol, which appears to play a major role in modulating not only the membrane property but also the structure and assembly of the envelope proteins. The authors didn't include cholesterol in their model. It will be useful to comment on the potential implications.

3. The cryptic binding sites were characterized mainly by the SASA values. Are there other characterizations that might be more relevant for future drug design, such as the volume of the cavity?

Reviewer #2 (Recommendations for the authors):

– A major weakness of the paper appears to be the flawed design of the simulation. The benzene mapping simulations were conducted using fixed protonations which are not specified in the paper, and thus they do not address any pH response. Why wouldn't the authors conduct the constant pH simulations first to determine protonation states and then use these protonation states to conduct conventional MD with benzenes?

– Another major weakness is that the conclusions are not very clear at least in my assessment. The authors claimed the α pocket to the cryptic pocket, but this conclusion can not be discerned from the presented figures. In fact, in Figure 2, 3 and others, the y values of the region around residue 144 is discontinuous. Not sure why. The conclusion of the constant pH part is very vague, and I can't understand what it is exactly.

– Overall, there are too many plots that are tangentially relevant. I suggest they can be moved to SI and instead focus the plots on the data that support the conclusions.

– It is unclear what exactly the histidine switch hypothesis is. The discussion needs to be more specific. Related to this, it is unclear how the determined protonation states address the hypothesis.

– The convergence of protonation state sampling should be included in the SI.

Reviewer #3 (Recommendations for the authors):– p5, line 32. One or two commas would elevate readability– p6, line 4. I wonder if "mixed-solvent" is the right term here. The benzene concentration is 0.6 M and is, compared to >50 M water, rather a co-solute.

– Membrane curvature: Curvature is imposed by MD constraints as detailed in the Method section. I understand that the membrane is not the focus of the analysis, but how does this curvature co-exist with the PBC of the simulation box? The scheme implies that the membrane + raft is surrounded by replicas.

– Figure 2A: Why do the +bnz plots initially drift? If part of the equilibration, I would have expected them to start at the -bnz levels.

– Figure 4C: It's not obvious how to interpret the "violin" plots: the distributions have no scale; and showing two mirrored halves seems redundant. The same comment applies to Figure 6A.

p13-14. Here I suggest revising the use of "rate(s)" as it took me a while to realise that the discussion is not about kinetics, but statics. I suspect that to many readers, "rate" would imply a dynamic property. Perhaps "ratio", "quotient", or "fraction" could be alternatives.

– Figure 6: This plot is packed with information and is used to support a detailed discussion about the role of the found charge cluster. I think that it works well. At pH is data in Fig6a obtained? I understand that the PCA is based on the indicated residue-residue distances. Another way to describe charge-charge interactions is via an electric multipole expansion of the cluster charges. Perhaps an analysis involving the dipole and quadrupole moment could be revealing. Merely a thought.

– Cluster response to pH changes. Figure 6a/b analyses the net-charge of the cluster which probes the overall protonation state. To judge how a pH change would affect the cluster, the charge capacitance, C=-^2 should be straightforward to extract. Measuring the charge fluctuations, it can be directly linked to a charge response due to a pH change. See e.g. doi:10.1017/S003358351300005X. Along the same lines, I wonder of fluctuations in SASA or Rg would reveal information of how easily the cluster is perturbed. Finally, I would have liked to see how the PCA would change in the presence of benzene.

p22, line 19: I think it would be useful to know exactly how many benzene molecule. Is it sufficient to saturate the protein surfaces? Or is there a deficit which could affect the number of observed contacts.

p22, Section 4.1.1. I would prefer to have slightly more information about the setup: "semi-isotropic" could be more specific as well as details about update intervals of the barostat and thermostat.

p24, line 17: Does this mean that solvent and other solutes are not part of the (de)protonation acceptance criterion? That is, is all explicit solvent replaced by a continuum? If so, could one not use a much cheaper constant pH scheme for conformational sampling?

p26, line 13: I much appreciate that the authors have made the effort to deposit the electronic material on Zenodo. This is a nice and very helpful gesture to the community!
