# Peer review - Round 1

Editors:
- Andrea Musacchio, Max Planck Institute of Molecular Physiology Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.38356.021](https://doi.org/10.7554/eLife.38356.021)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Structural basis for Scc3-dependent cohesin recruitment to chromatin" for consideration by eLife. Your article has been reviewed by Andrea Musacchio as the Senior Editor, a Reviewing Editor, and three reviewers.. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. We hope you will be able to submit the revised version within two months.

Summary:

Li et al., describe a crystal structure of Scc3 (slightly truncated at both ends and designated Scc3T) with a fragment of Scc1 ("Scc1K") bound with a 19bp fragment of dsDNA. The structure, which closely resembles a corresponding condensin DNA complex published last year by Haering's group, shows that DNA binds along a groove created by the curvature of the Scc3 heat repeats. Mutations of residues at points of contact with DNA backbone diminish affinity in vitro and (in appropriate combination) prevent loading in vivo, as shown by ChIP-qPCR and by tetrad analysis of strains ectopically expressing wt or mutant versions of Scc3 in an SCC3/scc3Δ background. The biochemical and structural work clearly identify the molecular basis of an interaction between Scc3 and DNA and demonstrate that a fragment of Scc1 enhances this interaction. While not entirely unsurprising, the results add to our understanding of how cohesin might function mechanistically. With appropriate revision, the MS can be made suitable for publication in eLife.

Essential revisions:

1) In the Discussion section (first paragraph), the authors set up a straw man. The only alternative to direct protein-DNA contacts (either by a cohesin subunit or by some adaptor protein) is that cohesin is snapping open and closed all the time and should it happen to entrap DNA, it somehow sticks. That silly alternative is obviously hugely improbable. Thus, the real conclusion is that "these findings provide evidence for a site of DNA contact, probably during the initial step in chromosome entrapment" – or something like that. See also point 3, below. Incidentally, "topological principles" don't "drive" anything in biology – they explain various mechanisms or activities and suggest why they may have evolved, but biology is never "driven" by "principles" other than natural selection (except in the minds of the unreconstructed Cartesians still running around in France).

2) The anisotropy of the crystals, presumably due to a less than optimal DNA length, limits the accuracy and the information content of the structure. Did the authors, seeing the result, take the obvious next step of trying to get better crystals with other DNA lengths (e.g., 20 or 21 bp)? (That is, were all DNAs in Supplementary file 2 used in crystallization trials, or just for FP measurements? If the former, why not also 20 bp?) In this reviewer's view, that would have been an easier and better path than the one they took by validating the Scc1 trace with SeMet. In any case, Figure 3—figure supplement 1 should show either the DNA density in the initial MR map or (if the MR is good enough – it might not be) an Fo-Fc map after that initial step (i.e., phases from MR but 2Fo-Fc, showing in principle what's missing). In any case, a map with the final 2Fo-Fc phases, which included this DNA contributions, is not helpful. Incidentally, in Supplementary file 1, the Rmerge in the last bin is truly miserable. Was there an "elliptical" (i.e., anisotropic) cutoff, or did the meaningless reflections in the "bad" directions contribute? If the latter, then please recalculate with the correct anisotropic cutoff for each frame or set of frames, so that pure noise doesn't contribute to the data used. Also, "3.99" is 4.0 in my book, not "3.9".

3) The text overstates some of the biological and mechanistic conclusions. Although the correlation of affinity in vitro with function in vivo does permit the inference that the observed interaction is part of the DNA docking mechanism, the results do not rule out the participation of other contacts. Indeed, were those contacts strengthened by compensating mutations, it is possible that this contact would not be "indispensible", as the Abstract states.

4) The most useful conclusion is the similarity with condensin. For understandable "psychological" reasons, the authors do not mention the Kschonsak et al. (2017) paper in the Introduction. They should do so, as it surely guided their strategy at some point, either consciously or otherwise. Is the peptide loop definitely absent here, or could its absence be a consequence of truncating Scc1?

5) At the end of the Discussion section, the authors write that the mechanism they describe would enable cohesin to entrap a second DNA helix without releasing the first, etc. Not obvious to this reader why or how, perhaps because Figure 4C is so vague and incomprehensible.

6a) Is K363 on Scc1 important for the DNA binding ability of the complex? It would also be useful to highlight this residue on Figure 2. This experiment is required to confirm the in vivo relevance of the enhancement of DNA association by the Scc1 fragment in the in vitro experiments.

6b) Scc1 is clearly required for the DNA-binding activity of Scc3-Scc1. The structure suggests that Scc1 K363 might contact DNA. Does Scc1 K363E reduce the binding of Scc3-Scc1? Related to this, even though the authors cannot see any density of the N-terminal region of Scc1K, this region might contribute to DNA binding. This should be experimentally tested. In the human SA2-Scc1K structure, the corresponding region in Scc1K forms a helix that is located at the base of the "nose" of SA2. Can the authors build a model of the SA2-Scc1-DNA complex and see if this N-terminal region of Scc1K might be close to DNA?

NOTE: Concern on the function of K363 was raised by two reviewers and is reported here in its original wording as points 6a and 6b.

7) The ChIP-qPCR is essential for the conclusions of the paper but there are some issues with the presented experiment in Figure 3D. A minimum of 3 biological repeats are required to compute standard deviation, so the error bars here are not appropriate and should be removed. The authors could show the data for the two biological replicates side by side without error bars as an indication of reproducibility or, better, repeat the experiment a third time and calculate standard deviation. What do the percentages mean above the bars? How did the authors analyse the heptamutant given that it is not viable? Do the cells also carry endogenous Scc3? In this case, do all the strains in this experiment carry untagged Scc3 in addition to the tagged wild type or mutant protein? The fact that patch 2 mutants still bind DNA in vitro predicts that the patch 2 mutant protein should also associate with the chromosome in vivo, but this was not tested.

8) The authors are proposing that the reported interactions are required for cohesin loading. However, an alternative possibility is that "core" cohesion can load but that Scc3 fails to associate with it. This should be tested by assessment of the association of other "core" cohesin subunits (Smc1/Smc3/Scc1) with chromosomes in the patch 3 mutant cells.

9) What is the effect of the observed mutations on sister chromatid cohesion? The authors should test this using the TetR-GFP or LacI-GFP system.

10) Hara et al. (2014) showed that mutating conserved basic residues in the N-terminal and middle regions of Scc1K did not affect Scc1K binding to SA2. These regions may transiently dissociate from SA2/Scc3 while the C-terminal region of Scc1K is still anchored to SA2/Scc3. It is thus possible that Scc3-Scc1K form a topological embrace of DNA, similar to the condensin sub-complex. This possibility needs to be discussed, especially if the N-terminal region of Scc1K is required for DNA binding (see point 6b).

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting your article "Structural basis for Scc3-dependent cohesin recruitment to chromatin" for consideration by eLife.

I have now examined your resubmission and I am happy to inform you that I consider it essentially ready for acceptance. However, before formal acceptance, I would like to note the following three points:

1) You seem to be using two somewhat different color schemes for Scc3 in the different figures, more bluish in Figure 2 and Figure 4, and more violet in Figure 1. May I suggest that you make the colours more uniform?

2) In Figure 2—figure supplement 1E, the right hand panel appears to be a composite of pasted lanes. If this is the case, could you please clearly mark this on the figure with a black vertical line and add a short reference to lane pasting in the legend?
