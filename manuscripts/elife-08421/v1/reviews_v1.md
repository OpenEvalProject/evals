# Peer review - Round 1

Editors:
- Taekjip Ha, Johns Hopkins University School of Medicine , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.08421.018](https://doi.org/10.7554/eLife.08421.018)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled "Single molecule compression reveals intra-protein forces drive cytotoxin pore formation" for peer review at eLife. Your submission has been favorably evaluated by Michael Marletta (Senior editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Czajkowsky et al. present a study that combines MD simulations and single-molecule AFM experimental data to analyze Perfringolysin O (PFO) pore-forming protein. The conformational changes responsible for the pre-pore to pore transition were previously known. The authors themselves published an article in 2004 in EMBO journal that uses the same di-sulfide-linked mutant in combination with AFM imaging with or without DTT to observe the shrinking of the pore heights due to pore formation. Here, the new contribution is that compressive AFM is used to induce pore formation. Also, steered MD simulations are performed to complement experiments. Importantly, they are able to obtain the transition probability as a function of force magnitude and duration, allowing them to fit the data to a two state model and deduce the distance to the transition state (and less clearly) the free energy barrier. If indeed this is the first time such analysis has been performed, this would be a significant contribution regardless of the novelty and biological significance of the findings themselves. In the physiological context, the force will be applied between D3 and the membrane, largely driven by hydrophobic force, and the compressive force is proposed to mimic this force, which is reasonable. MD simulations provide molecular accounting and some quantitative comparisons. The experiments were performed in an expert fashion, and the data is highly original and of high quality. Because we are not aware of any prior publication measuring a certain rate as a function of compressive force from a single molecule, this work could be a significant contribution even without important biological insights as long as the authors can address important technical issues raised, including a major concern about the validity of the construct used for the study. In addition, the work presents possible mechanisms underlying the transition from prepare to pore of PFO.

Essential revisions:

1) The pore-forming complex used in the AFM studies is a covalently-locked disulfide mutant that known from the authors' previous work not to form pores. They also state the compressive forces applied by the AFM tip are too low to break these disulfide bonds. Based on these two facts, it follows that the mechanism of pore collapse in their AFM experiment must be very different than the natural conformational change in the protein. This undermines their claim that "targeted application of compressive forces can recapitulate a critical step" of the pore-formation. How can they obtain a pore-like conformation in the presence of disulfide bond? There is no evidence presented that shows that a pore-like conformation can be obtained without breaking the disulfide bond between D2 and D3. We suggest that the authors perform MD simulations with the disulfide bond present and present evidence that the force results in pore-like conformations of D2 and D3 even in the presence of disulfide bond.

2) The authors assume that the compressive force is applied equally to all subunits. But they do not provide any evidence. What if the conformational change occurs efficiently only when the force is applied to primarily one subunit? Is their AFM free of lateral drift enough to be sure that the tip is pushing down in the middle of the pore? What is the AFP tip is not symmetrically shaped? What was the tip radius of the cantilever they used for AFM imaging and compression experiments? If the authors could please provide an SEM image of the cantilever tip so the reader can make a comparison to the pore size, it would improve the manuscript.

3) The tensile pulling geometry in the MD simulations does not mimic that found in the experiment, where compression is applied to the pore from above. The specific geometry will of course play a major role in determining the mechanical response of the protein pores. Additionally, the lipid membrane is not simulated in the MD trajectories. These dissimilarities between MD and experiment are too large to make any quantitative comparisons between the two results.

4) Perhaps the biggest issue with the MD simulations is that the authors performed MD simulations using one monomer, not as part of the complex. How does the conformational change in one PFO trigger the pre-pore to pore transition for all the PFOs in the pore complex? This is a major limitation because subunit interactions are likely to be important in determining the force response and conformational changes.
