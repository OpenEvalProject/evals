# Author response - Round 1

Authors:
- Inokentijs Josts ([ORCID: 0000-0002-8235-2397](https://orcid.org/0000-0002-8235-2397))
- Katharina Veith
- Henning Tidow ([ORCID: 0000-0002-4702-9332](https://orcid.org/0000-0002-4702-9332))

## Response text

DOI: [10.7554/eLife.48528.024](https://doi.org/10.7554/eLife.48528.024)

Essential revisions:

1) How do these results bear upon the functional mechanism in the bacteria? Is the statement that "The FoxA transporter can form a constitutive complex with TonB, even in the absence of ferrioxoamine B" necessarily true in vivo? This depends on relative concentrations of TonB, FoxA, and "competition" for TonB by the multiple other TonB-dependent transporters present in the OM. These questions should at least be discussed in the manuscript. If data concerning concentrations are available they should also be included.

These are very valid questions that are difficult to answer given the large number of variables in this system. Regarding the relative concentrations of TonB and FoxA, it is known that FoxA expression could only be observed under iron-restricted conditions in the presence of ferrioxamine B (Llamas et al., 2006). As the FoxA gene contains a Fur box in its promoter region, the expression of FoxA is most likely repressed via regulation by the Fur repressor protein under iron-rich conditions (Llamas et al., 2006). Thus, under resting conditions the TonB concentration should always dominate over the FoxA levels.

On the other hand, if FoxA gets upregulated via a signaling cascade involving binding of ferrioxamine B to FoxA, signal transmission to FoxR (anti-sigma factor) and increased activity of FoxI (sigma factor), its total concentration (like that of many other TBDT) can reach 100-fold of that of TonB (Klebba, 2003). This results in two populations of TBDT in the outer membrane: active transporters associated with TonB and inactive transporters unassociated with it (Newton, Trinh, and Klebba, 2010, J Biol Chem). Whether the “activated” ferrioxamine B-bound FoxA then indeed binds to TonB depends on the relative affinities of TonB to the different TBDT (which seem to be very similar) and their expression levels. In the presence of ferrioxamine B, the production of other siderophores is downregulated (Galet et al., 2015), which would result in fewer “active” TBDTs other than FoxA and thus reduced competition by TonB-binding to other TBDTs.

We have now revised the manuscript and in particular the conclusion section to discuss these aspects in more details. Given the above-mentioned facts, the “left half” of the proposed mechanism of TonB-mediated ferrioxamine B uptake via the FoxA transporter as shown in Figure 5 might be the dominating path in vivo under iron-limiting conditions and in the presence of ferrioxamine B. This path is also favored by the significantly higher affinity of TonBCt to “activated” FoxA/FoaB (compared to all other affinities along the reaction circle).

2) Since TonB binds to apo FoxA with ~100nM Kd, were any crystallization experiments attempted with this binary complex?

We have indeed tried very hard to crystallize the binary FoxA/TonBCt-complex as this would be the last missing puzzle piece in the variety of structural states adopted by FoxA during TonB-mediated ferrioxamine B uptake. Unfortunately, despite very pure and stable samples, we never obtained any crystals.

3) The error propagation in the ITC experiments is not clear. For example, how can a 75% fractional error in Kd lead to only a 2% fractional error in ΔH (and no stated error for TΔS)? What was the number of replicates?

In the previous version of the manuscript, the reported errors were fitting errors for a single measurement each, and thus quite large. We have now repeated all measurements to obtain triplicates and report the errors as standard deviations (SD) obtained from averaging Ka-values and converting them to Kd-values with error propagation. Errors for all other thermodynamic parameters are also given as SD now and included in Table 2 in Supplementary file 1. We have included the information about number of replicates and error propagation in the Materials and methods section now.

4) Likewise, errors are missing for the Trp quenching experiments. This should be provided.

As stated above, we have now performed all binding experiments in triplicates and reported the dissociation constant (Kd) as average ± SD. For the Trp quenching experiments shown in Figure 4—figure supplement 1C, this results in a Kd of 100 ± 10 nM.

5) For ITC determination of TonB binding to FoxA/ferrioxamineB, FoxA appears to have been "pre-loaded" with ferrioxamine B. Please provide more information on how this was done, and how estimated occupancy could affect the observed results. For example, given an ITC determination of ferrioxamine Kd for FoxA of 180 +/- 140 nM (78% fractional error), a 1:1 complex of FoxA:ferrioxamineB at 15uM will be ~90% occupancy, so the determined thermodynamic parameters are a combination of +/- substrate-bound FoxA.

The reviewer is correct. For the ITC titration of TonB into FoxA/FoaB, we “pre-loaded” FoxA with ferrioxamine B by dialyzing FoxA in nanodiscs against 1 mM (excess) FoaB. We have added this information to the Materials and methods section now.

Given a Kd of 100-200 nM for the binding of FoaB to FoxA (from fluorescence or ITC measurements, respectively) this excess of FoaB during the “pre-formation” of the FoxA/FoaB complex ensures that > 99.9% of FoxA is substrate-bound. This enables a clear distinction of binding parameters between binding of TonB to apo FoxA vs. TonB-binding to the FoxA/FoaB complex.

The errors of all ITC measurements have been updated according to our new triplicate repeat measurements (see Table 2 in Supplementary file 1). Initially, we reported fitting errors of single experiments. Now we report SD errors from triplicate titrations, which result in much lower fractional errors.

6) The term "novel insights" should be eliminated from the title (and elsewhere in the text). Instead the emphasis should be more on this being the first ternary structure (transporter/substrate/TonB[C-terminal periplasmic domain]) for a transporter with an N-terminal signaling domain – and a novel orientation of TonB.

We followed the suggestion of the reviewer/editor and eliminated the term “novel insights”. We have changed the title to “Ternary structure of the outer membrane transporter FoxA with resolved signaling domain provides insights into TonB-mediated siderophore uptake”. This title now puts further emphasis on the fact that the structure presented in this manuscript is the first ternary structure of a TBDT including a signalling domain.

This aspect as well as the different orientation of the TonBCt (compared to previous studies) has also been emphasized in the Results section:

“Overall, the structure of the ternary FoxA-ferrioxamineB-TonBCt complex presented in this work reveals both the structure of the N-terminal signalling domain as well as a markedly different orientation of the TonBCt relative to the TBDT compared to previously determined ternary structures of FhuA and BtuB (Pawelek, Croteau et al., 2006, Shultis, Purdy et al., 2006).”
