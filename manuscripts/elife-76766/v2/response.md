# Author response - Round 1

Authors:
- Ali A Kermani
- Olive E Burata ([ORCID: 0000-0002-8450-8930](https://orcid.org/0000-0002-8450-8930))
- B Ben Koff ([ORCID: 0000-0003-3276-143X](https://orcid.org/0000-0003-3276-143X))
- Akiko Koide
- Shohei Koide
- Randy B Stockbridge ([ORCID: 0000-0001-8848-3032](https://orcid.org/0000-0001-8848-3032))

## Response text

DOI: [10.7554/eLife.76766.sa2](https://doi.org/10.7554/eLife.76766.sa2)

Essential revisions:

We would appreciate more discussion of two points:

1. The L10 monobody has provided a valuable tool to facilitate structure determination of SMR family members, and we agree the EmrE mutations are likely not functionally significant. However, we would appreciate more discussion of the potential impact of monobody interaction itself on the EmrE structure, particularly in the loop regions.

We have added a comment to this paragraph commenting on the loops explicitly:

“However, two lines of evidence disfavor the possibility that the monobody-bound state is aberrant. First, we showed that monobody binding has only a minor effect on transport function, and second, our model corresponds closely to the helix density in the EM dataset, which was obtained without exogenous binding proteins(Ubarretxena-Belandia et al., 2003). Although local perturbations at the monobody-binding interface of loops 1A and 1B cannot be ruled out, the position of loop 1A is consistent with prior spectroscopic data, which indicated that in the major solution conformation, F27A packs against the B subunit with its sidechain oriented towards the substrate binding site. Loop 1B is located on the open side of the transporter and does not form any intra-transporter contacts. Therefore, even if monobody does stabilize a less-prevalent conformation of loop 1B, this would not change the major interpretations of the present structures.”

This was discussed in more detail in the prior Gdx-Clo structure paper from the Stockbridge group, but revisiting this is important here because of the role the loops play in closing off the transporter on one side of the membrane. Also, can this structure provide insight into how the L51I (and I62L) mutation near the end of TM2 (Lehninger eLife 2019;8:e48909) preferentially stabilizes EmrE in an open-to-one side conformation?

We have added the following paragraph to the discussion:

“Our results also provide some insight into the observation that a single L51I or I62L mutation in one subunit of the EmrE dimer prevents conformational exchange (Leninger et al., 2019). Both residues are located on transmembrane helices and are buried at protein interfaces in one monomer and accessible in the other (L51 to the aqueous binding pocket and I62 to the membrane). For Gdx-Clo, we previously posited that differential packing of the two monomers in the N-terminal half of helix 3 contributes to structural frustration and the resulting conformational exchange (Kermani et al., 2020). In EmrE, I62 is located in this same crucial region, and its mutation in only one monomer presumably disturbs the well-matched competition that occurs in the homodimer.”

2. What is the exact pH at which each of the substrate-bound crystal structures were determined? The methods state that the substrate-bound structures (drug-like-substrate, proton is also a substrate) were crystallized at pH 6.5 or pH between 7.1-7.3 depending on the buffer. But we do not see the exact pH listed in the tables for each of the different crystal forms or discussed in the text. This information is important because of the proton-coupled transport mechanism.

The results state "To understand how different substrates interact with EmrE, we screened a variety of transported compounds in crystallization trials at pH values {greater than or equal to}6.5, where the E14 sidechains are expected to be deprotonated, favoring binding of the positively charged substrates." This is incorrect.

We have added the crystallization conditions for each structure to the data collection and refinement table (Table 1).

We have removed this sentence from the results. In the discussion, we elaborated on the interplay of pH and substrate binding as follows:

“In addition to a substrate-free, pH 5.2 structure, we solved structures of EmrE with methyl viologen, harmane, Me-TPP+, TPP+, and benzyltrimethylammonium at pH values between 6.3 and 7.5. Experiments with EmrE in bicelles have suggested that a proton can bind simultaneously with TPP+ with a pKa of 6.8 (Robinson et al., 2017). In the NMR model, under conditions that favor simultaneous substrate and proton binding, F-TPP+ is positioned higher in the binding pocket, 2 Å closer to E14B than protonated E14A (Shcherbakov et al., 2021). In contrast, in our TPP+-bound structure, which was obtained at a pH of 7.25, TPP+ is situated lower in the binding pocket and within 0.5 Å of the midpoint between the glutamates. It is thus probable that this crystal structure represents the doubly-deprotonated, substrate-bound state. It is also likely that both glutamates are deprotonated in the methyl viologen-bound structure, since this substrate bears a +2 charge, making glutamate protonation more electrostatically unfavorable than in the presence of a monovalent substrate.

Protonation of the central glutamates has not been evaluated in the presence of monovalent substrates other than TPP+, and the E14 pKa values are likely to vary according to factors such as binding pocket solvation or charge delocalization on the substrate. For the Me-TPP+, harmane, and benzyltrimethylammonium-bound structures (pH 6.5, 7.1, and 7.25, respectively), the contribution of a substrate+proton-bound population cannot be ruled out. However, the positioning of each of these substrates centered close to the midpoint between the E14 carboxylate groups, similar to TPP+, implies that in the major component of the population, both glutamates bear a negative charge.”
