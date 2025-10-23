# Peer review - Round 1

Editors:
- Samara L Reck-Peterson, University of California, San Diego United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.48627.027](https://doi.org/10.7554/eLife.48627.027)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Remote control of microtubule plus-end dynamics and function from the minus-end" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Vivek Malhotra as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In eukaryotic cells, intracellular components are positioned in space and time in part due to the microtubule cytoskeleton. Cellular microtubules are functionally diverse, despite being formed from a common pool of tubulin dimers. In asymmetrically dividing cells the microtubules associated with the old and new centrosome are often functionally distinct. However, mechanistically what leads to these distinctions is not well understood in any system. In the current work, Chen and Widmer et al. use a combination of in vivo imaging in S. cerevisiae and mathematical modelling to determine that the differing cargoes and plus end dynamics of bud-microtubules and mother-microtubules is specified at their minus ends (found anchored in the spindle pole body (SPB)). They find that old SPBs recruit the kinesin Kip2 to the minus end in a manner that depends on Bub2 and Bfa1 as well as the phosphorylation state of Kip2. Kip2 then translocates to the plus end, transporting dynein to the bud and promoting microtubule extension. The authors conclude this rigorously performed study by proposing a model for how microtubule organizing centers could differentially specify the plus end behavior of the microtubules emanating from them.

Essential revisions:

1) One of the authors' main conclusions from their modeling is that Kip2 starts its runs from the b-SPB and ends them at the microtubule plus end. However, this is really difficult to visualize in the experimental kymograph shown in Figure 3A (right) and Figure 2—figure supplement 1A (middle). Specifically, in Figure 3A, some runs appear to be truncated halfway (e.g. 5th arrowhead from the left in the experimental kymograph). Some speckles appear to start in the microtubule lattice, not from SPB, although it is difficult to interpret from the blurry kymograph. Additionally, the synthetic kymograph does not closely resemble the experimental kymograph, as stated by the authors in the first paragraph of the subsection “Kip2 runs start from SPBs”. Thus, the claim "the initiation of Kip2 runs is restricted to the minus-ends" is weak. Clearer kymographs or additional experimental evidence is necessary to support this claim. Intensity line scans at different time points could help to more clearly distinguish individual motor runs in space and time.

2) Related to the first point, additional information should also be added to the Materials and methods describing how runs were determined. If multiple people analyzed this data, did they come to the same conclusions about what to consider a run? Was this data blinded in some way to account for potential bias in the analysis? Automated detection of runs would ease concerns that runs are being mis-assigned.

3) Mutating G374 in Kip2 is a nice second independent test for whether Kip2 starts its runs from the microtubule minus-ends (subsection “Kip2 runs start from SPBs”, first paragraph). However, if Kip2 is indeed different from Kip3 with regard to where it initiates runs, then mutating the corresponding residue in Kip3 (G343 based on the alignment in Figure 3—figure supplement 1) would be a good control to perform. The mutated Kip3-G343 would be predicted to decorate along the microtubule length and not accumulate at the b-SPB like Kip2. This would strengthen the argument that loading at SPBs and initiating runs at the minus end is a Kip2-specific phenomenon.

4) In Figure 5B, the authors show that bfa1 and bub2 deletions lowered the levels of Kip2-G374A on the b-SPB by nearly 50%, while the signal on the m-SPB was unchanged. Similarly, in Figure 5F, the levels of Kip2 on b-microtubules lowered to nearly m-microtubules levels, while the signals on the m-microtubules remained unchanged compared to wild type. These decreases might indicate that there is actually less total Kip2 in bfa1 and bub2 null cells. The authors should determine the expression levels of Kip2 by western blot to exclude the possibility that the decreases are not due to a reduction in Kip2's expression or protein stability.

5) In a related point, following the analysis of Kip2-S63A-G374A in Figure 6C, D, E, the authors conclude that both SPBs recruited more of the hypo-phosphorylated, ATPase deficient protein and that the distribution was still asymmetric in cells with correctly oriented SPBs. However, based on Figure 6D, it seems that the enhancement in both SPBs indicates that the total amount of Kip2 in the cell might have increased significantly because of the S63A mutation. The authors should compare the levels of Kip2-S63A-G374A to Kip2-G374A to exclude the possibility that dephosphorylation of Kip2's N-terminus enhances the stability of the protein, thereby giving the observed effects.

6) The authors' main conclusions concern Kip2's distribution profile in metaphase. However, they selected spindles for analysis and decided which spindles were in metaphase based on the shape of cells and the size of spindles (subsection “Image and data analysis”, first paragraph). The standard in the field for examining cells in metaphase is to perform cdc20 depletion (such as Khmelinskii et al., 2009). Given that metaphase is not strictly defined by the length of the spindle, it would be more appropriate to refer to preanaphase instead of metaphase.

7) Kip2 hypo-phosphorylation caused an increase in the levels of Kip2 on the plus ends of both b- and m-microtubules compared to wild type, based on Figure 6J versus Figure 4E, but the levels of dynein to the b-microtubules, a cargo of Kip2, did not appear to increase based on the images shown in Figure 7C (comparing the dynein dots in KIP2 vs. KIP2-S63A images). On the other hand, in Figure 7D, the authors report that dynein distribution at the tip of b- and m-microtubules was randomized when Kip2 phosphorylation is prevented (i.e. in KIP2-S63A mutant cells). Please clarify how randomization occurred when there is no apparent change in dynein intensity?

8) Related to the modeling.

- The presented model addresses binding, unbinding and stepping rates of the kinesin. However, it does not consider dynamic microtubules (e.g. compare left vs. right kymographs in Figure 3A, where the plus end clearly grows in the experimental condition, but not in the model). Addition of plus end dynamics and showing that the regulation of Kip2 loading at the minus ends affects it would make the model predictions much stronger. For instance, how would the model predict observations presented in Figure 4?

- The total intensity at the tip corresponds to a defined accumulation of motors at the end. How many are there? (The number of occupied sites should be set by the ratio of minus-end loading and plus-end off rate; and can thus also be directly predicted from the model parameters.)

9) Points to discuss:

- Is it possible to exclude direct end-targeting of Kip2 (e.g. through Bim1 binding or another mechanism)? In principle, such a model would also produce a non-microtubule-length dependent Kip2 profile, here the ron would be the on rate of direct binding to the tip.

- If enhanced loading to the SPB is a specific mechanism for the b-SPB and not the m-SPB, the prediction would be that the distribution of Kip2 intensities is length-dependent on m-SPB-emanating microtubules. Is that true?
