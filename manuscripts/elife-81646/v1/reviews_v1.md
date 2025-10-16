# Peer review - Round 1

Editors:
- Tony Ng, https://ror.org/0220mzb33 King's College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81646.sa0](https://doi.org/10.7554/eLife.81646.sa0)

This important study documents the use of computational models and protein design to enhance antibody binding. The new method could have a broad and immediate impact on a variety of diagnostic procedures that use antibodies as sensitivity is often an issue in these kinds of experiments. The evidence produced is highly compelling through demonstration of the substantial sensitivity enhancement achieved in two test cases. This manuscript will likely be of interest to researchers who use antibodies for diagnostic and therapeutic purposes.


---

# Peer review - Round 1

Editors:
- Tony Ng, https://ror.org/0220mzb33 King's College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81646.sa1](https://doi.org/10.7554/eLife.81646.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Noncovalent antibody catenation on a target surface drastically increases the antigen-binding avidity" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Tony Ng as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Regarding experiments:

1) There needs to be a negative control for the affinity measurements, such as incorporating a dimerization-defective variant of the SDF-1alpha catenator and seeing if the avidity effect disappears.

2) The experimental assessment focuses solely on the binding affinity and no other aspects of the antibodies, such as purity and solution properties. If the catenator negatively impacts purification, that is information that should be included in the manuscript. The behavior of the antibodies in the solution is particularly important. You want the catenation to be highly dependent on the presence of the target antigen. The catenator could induce the antibodies to form an essentially infinite array and/or large aggregates. Aggregates tend to be highly immunogenic, so if any potential targets of this method are intended to be injected into animals or people, unwanted immune responses could be a serious issue. Gel filtration and dynamic light scattering are two potential methods that can assess the size of the antibodies +/- catenator and +/- antigen to ensure that the antibodies exhibit the desired behavior.

3) It should be stated that the two antibodies, Trastuzumab(N30A/H91A) and glCV30, were selected for weakened antigen-binding affinities.

4) On page 12, line 246, SDF-1α KD was 150 uM; on page 14, line 299, SDF-1α KD was 150 nM. Which one is correct?

5) What is the physiological expression and function of SDF-1α? Would injection of IgG fused with SDF-1α disturb the physiological function of SDF-1α?

6) What are the expression yields of catenator-fused antibodies? How do the yields compare to those of the unmodified antibodies?

7) It would greatly improve the implications of IgG catenation if relevant antibody functional assays can be performed for the two tested antibodies. For example, an in vitro assay to compare the function of Trastuzumab(N30A/H91A), cat-Trastuzumab(N30A/H91A), and Trastuzumab. Likewise, a SARS-CoV-2 neutralization assay to compare glCV30, cat-glCV30, and CV30.

Regarding computations:

8) The simulations could be improved. The third major step in the simulations seems to favor the binding ability of catenated IgGs. If so, in any means the simulations will yield a higher binding affinity for the catenated homodimeric IgG. This should be clarified.

9) What is the role of the concentration of IgGs on the binding behavior? Would it be possible somehow to include this in the simulations and also link it to the experiments?

10) While the results render the enhanced binding affinity of the catenated homodimeric IgGs, the study would benefit from a more elaborated interpretation and discussions of the results.

(10a) One interesting base of discussion may include how the fusion of the catenator may likely affect the binding behavior, the intrinsic binding behavior, and/or on the global structural changes of IgGs per se, beyond its proximity-driven contribution. Please refer both to the monomeric and homodimeric (catenated) forms. Would it lead to a more restricted structure in the mobility in the unbound states so as to decrease the entropic cost for the binding and thus increase the binding avidity/affinity (in addition to external proximity-driven association)? In other words, what would be the role of entropy in the free energy of binding, given that the enthalpic contributions remain the same? Possible effects of the length of the catenator should also in parts be related to the entropy. For example, if a longer and more flexible catenator is considered, what would the resulting observation be? Both experimentally and computationally.

(10b) On the other side, simple simulation approaches have a high value with a level of abstraction while still keeping the physical and biological relevance. In the simulations, i.e., in the sampling of various states, three main terms/rules to govern the behavior are implemented. One is a term favoring an increase in the ability to bind (preventing unbinding) to the surface upon the catenation of IgGs. This may need to be substantiated for the simulations not imposing a presumed ability to increase the binding (or decrease the unbinding) ability upon catenation.

(10c) The weakly homodimerizing state of the catenator appears as one of the important aspects of the proposed design strategy. Would it also be possible that the experimental observations may readily also imply the higher binding ability of the catenator fused IfgG without the homodimerization on the surface (due to the reduced entropic cost for the binding)? The presentation of the evidence of the homodimerization of the catenator and the catenated IgGs on the surface would strengthen the findings and discussions.
