# Peer review - Round 1

Editors:
- Qiang Cui, Boston University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.94029.3.sa0](https://doi.org/10.7554/eLife.94029.3.sa0)

The authors report how a previously published method, ReplicaDock, can be used to improve predictions from AlphaFold-multimer (AFm) for protein docking studies. The level of improvement is modest for cases where AFm is successful; for cases where AFm is not as successful, the improvement is more significant, although the accuracy of prediction is also notably lower. The evidence for the ReplicaDock approach being more predictive than AFm is particularly convincing for the antibody–antigen test case. Overall, the study makes a valuable contribution by combining data- and physics-driven approaches.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94029.3.sa1](https://doi.org/10.7554/eLife.94029.3.sa1)

Summary:

The authors wanted to use AlphaFold-multimer (AFm) predictions to reduce the challenge of physics-based protein-protein docking.

Strengths:

They found two features of AFm predictions that are very useful. (1) pLLDT is predictive of flexible residues, which they could target for conformational sampling during docking; (2) the interface-pLLDT score is predictive of the quality of AFm predictions, which allows the authors to decide whether to do local or global docking.

Weaknesses:

(1) As admitted by the authors, the AFm predictions for the main dataset are undoubtedly biased because these structures were used for AFm training. Could the authors find a way to assess the extent of this bias?

(2) For the CASP15 targets where this bias is absent, the presentation was very brief. In particular, I'm interested in seeing how AFm helped with the docking? They may even want to do a direct comparison with docking results w/o the help of AFm.

Comments on revisions:

This revision has addressed my previous comments.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94029.3.sa2](https://doi.org/10.7554/eLife.94029.3.sa2)

Summary:

In short, this paper uses a previously published method, ReplicaDock to improve predictions from AlphaFold-multimer. The method generated about 25% more acceptable predictions than AFm, but more important is improving an Antibody-antigen set, where more than 50% of the models become improved.

When looking at the results in more detail, it is clear that for the models where the AFm models are good, the improvement is modest (or not at all). See, for instance, the blue dots in Fig 6. However, in the cases where AFm fails, the improvement is substantial (red dots in Fig 6), but no models reach a very high accuracy (Fnat ~0.5 compared to 0.8 for the good AFm models). So the paper could be summarized by claiming, "We apply ReplicaDock when AFm fails", instead of trying to sell the paper as an utterly novel pipeline. I must also say that I am surprised by the excellent performance of ReplicaDock - it seems to be a significant step ahead of other (not AlphaFold) docking methods, and from reading the original paper, that was unclear. Having a better benchmark of it alone (without AFm) would be very interesting.

These results also highlight several questions I try to describe in the weakness section below. In short, they boil down to the fact that the authors must show how good/bad ReplicaDock is at all targets not only the ones where AFm fails. In addition, I have several more technical comments.

Strengths:

Impressive increase in performance on AB-AG set (although a small set and no proteins).

Weaknesses:

The presentation is a bit hard to follow. The authors mix several measures (Fnat, iRMS, RMSDbound, etc). In addition, it is not always clear what is shown. For instance, in Fig 1, is the RMSD calculated for a single chain or the entire protein? I would suggest that the author replace all these measures with two: TM-score when evaluating the quality of a single chain and DockQ when evaluating the results for docking. This would provide a clearer picture of the performance. This applies to most figures and tables. For instance, Fig 9 could be shown as a distribution of DockQ scores.

The improvements on the models where AFm is good are minimal (if at all), and it is unclear how global docking would perform on these targets, nor exactly why the plDDT<0.85 cutoff was chosen. To better understand the performance of ReplicaDock, the authors should therefore (i) run global and local docking on all targets and report the results, (ii) report the results if AlphaFold (not multimer) models of the chains were used as input to ReplicaDock (I would assume it is similar). These models can be downloaded from AlphaFoldDB.

Further, it would be interesting to see if ReplicaDock could be combined with AFsample (or any other model to generate structural diversity) to improve performance further.

The estimates of computing costs for the AFsample are incorrect (check what is presented in their paper). What are the computational costs for RepliaDock global docking?

It is unclear strictly what sequences were used as input to the modelling. The authors should use full-length UniProt sequences if that were not done.

The antibody-antigen dataset is small. It could easily be expanded to thousands of proteins. It would be interesting to know the performance of ReplicaDock on a more extensive set of Antibodies and nanobodies.

Using pLDDT on the interface region to identify good/bas models is likely suboptimal. It was acceptable (as a part of the score) for AlphaFold-2.0 (monomer), but AFm behaves differently. Here, AFm provides a direct score to evaluate the quality of the interaction (ipTM or Ranking Confidence). The authors should use these to separate good/bad models (for global/local docking), or at least show that these scores are less good than the one they used.

Comments on revisions:

The inclusion of the DockQ improved the paper. No further comments.
