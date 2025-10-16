# Peer review - Round 1

Editors:
- Sierra Cullati, https://ror.org/02vm5rt34 Vanderbilt University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85328.sa0](https://doi.org/10.7554/eLife.85328.sa0)

This important study investigates the dynamic activation mechanism of a key mitotic kinase complex, Aurora B/INCENP. The method of generating specifically phosphorylated forms of the complex is elegant, supporting a compelling experimental and computational analysis of how these sites synergistically activate Aurora B and providing insight into the dynamics underlying the activation mechanism. This work will be of interest to cell biologists and biochemists studying cell division and kinase regulation.


---

# Peer review - Round 1

Editors:
- Sierra Cullati, https://ror.org/02vm5rt34 Vanderbilt University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85328.sa1](https://doi.org/10.7554/eLife.85328.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "The structural basis of the multi-step allosteric activation of Aurora B kinase" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Volker Dötsch as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Richard Bayliss (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Overall, the reviewers feel quite positively about the manuscript and agree that this work advances our understanding of Aurora B activation. The greatest strength is the strategy to prepare and study enzyme complexes with specific phosphorylation sites occupied, either the activation loop or the TSS sites. The emphasis on changing Aurora B/IN-box dynamics is also a valuable addition to the existing structural models. The primary weakness, detailed by Reviewer 2, is in the MD simulations, and these should be the focus of revisions:

1. It would be instructive to model the interactions of the phosphorylated INCENP with Aurora B using the structure of Aurora C/IN-box (6GR8) as a template. Is it the same or different than the results presented, which start with Aurora B/IN-box (4C2W)?

2. Please compare and contrast the MD models with the Aurora C/IN-box crystal structure, especially regarding the interactions between the IN-box and the activation loop, and hypothesize what could lead to the observed differences.

3. Please discuss the challenges of modeling phosphorylated proteins and how these limitations might affect interpretation of the MD results.

Reviewer #1 (Recommendations for the authors):

Reviewer comments from a previous submission were thoroughly addressed, including important controls for unphosphorylated F845C AURKB, continued binding of INCENP to AURKB during HDX, the kinetic contributions of T248 and TSS phosphorylation, and disruption of the AURKB motif by R847 mutation.

To expand more specifically on the point about statistical analysis from the public review:

1. In Figure S1, please indicate the concentration of substrate peptide, the number of replicates, and some measure of experimental variability.

2. In the RMSF plots in Figure 2 and Figure S6, is there a way to statistically test if the distributions are significantly different? The difference is apparent in Figure 2E, but more subtle in Figure 2F, so it would be more convincing with statistical evidence.

3. Please add error bars to Figure S9B.

4. What is the difference between Figure S16B and Figure 5E? Also, please indicate the number of replicates and experimental variability for these figures.

Reviewer #2 (Recommendations for the authors):

p.4 EX1 kinetics and EX2 kinetics are technical terms that should be defined and explained.

p.5 Using the 4C2W as a starting point for simulation is justified, as a model for Aurora-B. However, for modelling the interactions of the phosphorylated INCENP, the structure of Aurora-C/pINCENP (6GR8) would be a better option. Because the sequences of Aurora-B and -C are very similar, it would be straightforward to make an Aurora-B/phos-INCENP starting model, which could be "dephosphorylated" in silico to then probe the roles of the different phosphorylation states.

p.6 The comparison of the Aurora-B/IN-box model from MD with the crystal structure of Aurora-C/IN-box is incomplete because there are major differences between them in the IN-box interaction with the kinase activation loop. These should be described and an explanation provided for why the MD simulation leads to a different result from the experimental crystal structure. For example;

– In the Aurora-C/IN-box crystal structure, there are no direct interactions between the IN-box and the phosphate group on the activation loop threonine. In the Aurora-B/IN-box models, either Arg847 or Arg843 forms a direct interaction with the phosphate on the activation loop threonine.

– In the Aurora-C/IN-box crystal structure, the phosphate groups attached to the TSS motif interact directly with Aurora-C, whereas in the Aurora-B/IN-box model they do not, instead they are pointing out into solvent.

– The residues equivalent to Aurora-B/IN-box model Arg847 and Arg843 in the Aurora-C/IN-box structure participate in the interface, but have different interactions. This is important for interpreting the results of mutating these residues because they would be expected to affect binding/activity in either model.

p.9 The rapid formation of very stable salt-bridge interactions between the TSS and adjacent positively charged residues indicates that the modelling parameters may not be optimized for phosphorylated proteins. As these interactions are non-native (i.e. not in the crystal structure of Aurora-C/IN-box), their stability prevents the simulation from reaching the native conformation. Simulation of phosphorylated proteins is challenging, with interactions of the phosphate groups being artificially strong in some standard force field models (e.g. 10.1021/acs.jctc.5b00967, and 10.1021/acs.jcpa.8b04418 for improved polarisable modelling of phosphate). The potential limitations of this aspect of the study should be discussed.

p.10 The loss of activity of the Lys846Asn-Arg847Gln mutant is difficult to understand, what is the rationale? Is this simply a poorly-behaved protein, or how else do these residues contribute to Aurora-B autophosphorylation? Perhaps the individual residue mutations would shed some light on this?

p.11 The sentence mid-way through the first paragraph, that starts "For [Aurora B/IN-box]no-P" is very difficult to understand and is structured with too many commas. It should be rewritten.

p.11 The analysis of global movements is interesting, but the authors should be more cautious about the interpretation because the simulations are of relatively short duration, and the changes may be overly influenced by initial conformational changes as the protein responds to the in silico phosphorylation. The analysis would be improved by including a plot against time/RMSD of the occupancy of the major conformational states.

p.12 Analysis of the EX1-like kinetics suggesting that the helices in the IN-box might be only partially formed whilst the proteins are interacting is very interesting. It would be helpful to the reader to explain this analysis more clearly for a non-expert, perhaps with reference to previous examples in the literature.

p.15 Does one biological replicate really mean a single sample, or does it mean two samples (in which case, two replicates/samples would be more accurate).

p.17 Which software was used for the modelling? Which phosphoryl group model was used (e.g. TP2)?

Supplementary:

p.9 (Figure S5) part C, the phosphoserines are mislabelled pT

p.13 (Figure S8) is there a reason why the quality of one spectrum in each of the spectra sets in Figure S8 is poor?
