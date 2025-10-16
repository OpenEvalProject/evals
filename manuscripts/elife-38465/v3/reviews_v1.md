# Peer review - Round 1

Editors:
- José D Faraldo-Gómez, National Heart, Lung and Blood Institute, National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.38465.030](https://doi.org/10.7554/eLife.38465.030)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Simulation of spontaneous G protein activation reveals a new intermediate driving GDP unbinding" for consideration by eLife. Your article has been favorably reviewed by two peer reviewers, and the evaluation has been overseen by José Faraldo-Gómez as the Reviewing Editor and John Kuriyan as the Senior Editor. Both reviewers have agreed to reveal their identity: Alan Grossfield and Madan Babu.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Sun et al. from the Bowman group report the findings from the simulation of spontaneous G protein activation. Specifically, they provide detailed molecular insights into the process by which G protein activation drives GDP release and highlight that tilting of helix 5 has an important role in the kinetics of GDP release. The study is based upon sophisticated computational methods and seeks to understand an important biological problem. The manuscript is well-written and the data are presented clearly.

Essential revisions:

1) Earlier studies have demonstrated the influence the specific ligand-receptor complex and receptor conformation on G protein dynamics and kinetics (e.g. Furness et al., 2016). Those earlier findings ought to be discussed and contrasted with the authors' proposal. The authors' approach appears to be based, by design, on a conformational selection perspective of the G protein. It is however a concern whether simulations of an isolated G protein can capture the range of conformational states accessible in the context of the receptor. It would be informative to analyze the analogous tilting/twisting angles in recently published structures of receptor-G protein complexes.

2) It is key that the manuscript is revised to make clear that the observations made are for Gαq (from the Abstract onwards), and that it remains to be shown whether they are applicable to other G proteins. The authors are however encouraged to discuss whether they anticipate their findings to be universal, and their rationale. On a related note, the authors are asked to revise the manuscript as needed to ensure a fair characterization of previous proposals. For example, Flock et al. (2015) discuss a mechanism they see as common but also incomplete, thus requiring other elements that might vary among G proteins. Specifically: "While the conserved residue contacts are crucial for Gα activation, non-conserved positions can still be important for allosteric activation in distinct Gα proteins. […] Thus, the conserved universal mechanism probably represents the 'skeleton' that can be incorporated into different contexts in different Gα proteins to maintain a conserved mechanism of allosteric activation and yet permit specific binding to the receptor".

3) On a technical note, how was the per-residue maximum Shannon entropy estimated? Is it just the entropy for evenly distributing probability across all bins? And what is the justification for simply summing entropies? That would be correct if each individual dihedral were independent of all others, but that is not the case (that information precisely is used elsewhere). Please provide an estimate for the error introduced by this approximation (or an appropriate reference if this issue has been discussed elsewhere).
