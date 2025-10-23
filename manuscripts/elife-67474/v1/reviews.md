# Peer review - Round 1

Editors:
- José D Faraldo-Gómez, https://ror.org/01cwqze88 National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67474.sa0](https://doi.org/10.7554/eLife.67474.sa0)

A computational approach is proposed to identify mutations in enzymes that might impact their interactions with substrates. For one enzyme, in particular, the predictions are validated through experiments, using multiple techniques. Taken together, these data lead to non-trivial conclusions in regard to the nature of allosteric effects, albeit it remains unclear whether these conclusions will apply more broadly when other enzymes are examined.


---

# Peer review - Round 1

Editors:
- José D Faraldo-Gómez, https://ror.org/01cwqze88 National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67474.sa1](https://doi.org/10.7554/eLife.67474.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Design of novel CV-N variants by modulation of binding dynamics through distal mutations" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Nir Ben-Tal as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Michael Marletta as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Kazan and colleagues have developed a computational approach to identify distal/remote residues that allosterically modulate dynamics of binding sites. They have utilized a combined bioinformatics (statistical analysis of coevolution) and structural dynamics (looking for dynamic coupling) approach to achieve this. The work that is done to analyze and rationalize the effects of mutations at position 34 f the cyanovirin-N protein are comprehensive and the results are interesting. However, this is not sufficient to test a new technique or approach. There should be a considerably higher number of tests, at different positions and in different proteins, and it should have as a control tests with residues selected through coevolutionary analysis alone, or solely through structural analysis (or picked at random). This would help to understand how or why the approach works (or if it is comparably effective to simply selecting residues at consensus positions). We would also suggest some statistical analysis to estimate how accurate the approach is. The concern is essentially that with n=1, as is the case here, we cannot properly test the hypothesis that the approach as outlined in the paper is effective. We feel it is an interesting paper, but simply needs more data – without it, it is very speculative.

The explanation in terms of entropy is overly simplistic and is focused fully on the protein dynamics. The ITC measures the binding thermodynamics of the systems, which includes solvent. In this case it is likely the entropy reflects release of bound waters – without understanding how the solvation of the protein changes, especially in the binding site upon ligand binding a significant part of the explanation is missing. This could in fact help explain some of the differences in effects of the mutations. This could be looked at through the MD simulations.

In summary, the main strength is that the predictions, obtained by combining various computational tools, guided experiments, again using multitude of techniques. It all converged to interesting conclusion about allosteric effects of mutations on substrate binding which are not trivial. However, there are some unclear and open-ended issues that should be dealt with.

Essential revisions:

Summary

A computational approach is used to suggest mutations in a remote site of a sugar binding protein which alter its interaction with the substrate. Encouragingly, the predictions, obtained by combining various computational tools, are validated in experiments, again using multitude of techniques. It all converge to non-trivial conclusions about allosteric effects of mutations on substrate binding. The ability to rationally design remote mutations to modulate ligand binding would be very useful to the field. However, while the single example in this paper is interesting, it is not sufficient to ascertain whether the method is reproducible or estimate how accurate or effective it is.

1. Significantly increasing the number of positions tested in the protein. Positions that are conserved (coevolved) as well as unconserved, at a range of distances from the binding site. This would produce a sufficiently large dataset to draw conclusions relating to whether the approach works (n=1 does not allow this) and importantly, why it works.

The authors prioritize evolutionary coupling scores with an ad-hoc approach, considering somehow all the scores of three servers. Otherwise, it is not min DFI and max DCI. Even with slight changes of EV scores, more favorable DFI and DCI cases would have been chosen. Figure 1 shows many residues near I34 (e.g., along the same b-stand and in the b-strand below it) which are equally rigid and coupled. So why was this particular position selected? The text argues that because it also emerged from coevolution analysis, and was over 15 Ang from the active site. However, the decision on a threshold of a distance of 15 Ang from the binding site seems arbitrary. With 10-11 Ang distance, there are amino acid positions with lower DFI and higher DCI values. Also, farther than 15 Ang distance, there are also cases that would be of importance. What is the significance (or somehow confidence levels) of variations in each of these scores (in each of coevolution scores) as well as in DFI and DCI?

Now, let us consider an extreme view: that, from some unknown reason, coevolution provides all the information. For the sake of argument, let us examine the following criteria: high evolutionary coupling scores and distance over 15 Ang. That is, taking the dynamics out of the equation. If it would lead to the same choice then dynamics is not necessarily at play.

2. Greater analysis of the role of solvation water and changes on ligand binding could help rationalize the ITC data. Enthalpy-entropy compensation is common when binding proteins are mutated, previous studies on this should be consulted and referenced.

3. That dynamic coupling underlay allostery is intuitive. However, the link between allostery and evolutionary coupling is not. How would evolutionary coupling between a remote site and the binding site be related to allostery? Mechanistically, evolutionary coupling means that variations in amino acids in one position are compensated by complementary changes in another position. So why would a variation in position I34 be necessarily compensated by variations in the binding site? Why not in other positions? Evolutionary coupling pathways between regulatory sites (e.g., where an effector would bind) and the binding site have been shown, and make sense (evolution 'works' to maintain the required allostery). But why I34? Is it a known regulatory site? What biological function does it facilitate? The authors should at least discuss this. Or, better, examine the possibility of designing mutations without the evolutionary coupling consideration.

4. The choice of the mutations. Table S2 appears to show that the most frequent amino acids in position I34 (in addition to I) are L and F, rather than Y. So how was Y selected?

Further on this, "We also selected K as a mutant, because it is the only positively charged amino acid observed at position 34": That much is true, but why aiming for a positive charge in this position? Perhaps a better argument is that this position features aromatic and hydrophobic residues, making K unique.

5. Binding energy prediction. The -6.0 kcal/mol threshold looks magical. The various cases are assigned scores within a range of ~-6.0 +/- 0.5 kcal/mol. With that, all mutants with binding scores more negative than -6.0 really bind in experiments (dG around -5.5 kcal/mol), while the I34K mutant with a score of -5.85, 0.15 kcal/mol above the threshold, does not bind at all. Not even weakly. The most likely explanation is that the authors were lucky… They should acknowledge that.

It is noteworthy that the binding energies were calculated with the docked poses, presumably before having the crystal structures. However, maybe now, that the crystal structures of the holo and apo protein (and the simulations) are available, it is possible to improve the calculations. Maybe that would give a chance to improve the prediction values? And why having only unbound MD simulations although the authors obtained crystals of the complex structure in unbound and bound states? That is, to carry out MD analysis in both unbound and bound states on both wildtype and mutant (complex AB – (chain A + chain B)) to dissect fully what the story is in the allosteric modulation. By the way, since the authors have the crystal structure of the complex, it makes sense to compare the observed binding poses to the most favorable poses from docking.

6. Entropy gain. To show the entropy gain with the mutation (to interpret the ITC experiments), it should be important to comparatively analyze the unbound and bound wildtype and mutant MD simulations. Is it true that only binding site residues are responsible for this entropy gain? The authors observed changes in the volume of the binding cavity in unbound wildtype vs. mutant structures. But what about changes in the DFI values of binding site residues? If the DFI values are similarly restricted in the unbound and bound states of the mutant structure, and similarly relaxed in bound and unbound states of the wildtype, that would mean that they are not responsible for the entropy gain measured in the experiments.

With allosteric mutations, the redistribution of fluctuations may lead to entropic gain, which would not be fully explained with only considering binding site behavior. The whole structure should be analyzed.

7. Presentation. Title: What is "CV-N"? Maybe other readers also do not know of the top of their heads? Is it possible to avoid using this term in the title? Abstract: "Our results point to a novel approach to identify and substitute distal sites by integrating evolutionary inference with protein dynamics in glycan-binding proteins to improve binding affinity." Overselling. This statement would be legitimate after successful design of, say, 20 mutations in several different proteins. So far there are only 3 mutations in a single position in one protein.
