# Author response - Round 1

Authors:
- Deryck J Mills
- Stella Vitt
- Mike Strauss
- Seigo Shima
- Janet Vonck

## Response text

DOI: [10.7554/eLife.00218.022](https://doi.org/10.7554/eLife.00218.022)

1. The main concern of the reviewers is the quality of our map. We recognize that the figures in the original manuscript did not do justice to the map. Following a comment by the reviewers, we have estimated the B-factors of the maps and used these to sharpen the maps. This improved the map appearance greatly. We have included new figures of the sharpened maps in Figure 2, of larger regions than before, and showing many more side chains. We anticipate the reviewers will now be convinced of the validity of our model.

The appearance of the map is not unlike the icosahedral map in X. Zhang et al., 2008, which the reviewers ask us to compare, although clearly not as good as their 13-fold averaged map that was estimated as 3.8 Å resolution by comparison with an x-ray map. Comparison with a map calculated from our model at different resolutions suggest a resolution of ∼4.5 Å for the best regions.

We have carried out the suggested calculations and added the results to the manuscript, including a new figure (Figure 10) showing the different Fourier shell correlation plots.

For the gold standard FSC we have used the procedure now available in EMAN2, the program used for refinement. This procedure, e2refine-evenodd, randomizes the phases of the starting model from a user-defined cut-off resolution and then refines two half-data sets against this model. Afterward the FSC between the two resulting maps is calculated. As there are features in our map indicating better than 5-Å resolution (separation of β-strands) we chose a cut-off resolution of 6 Å; the FSC between the resulting half-data maps reached 5.5 Å at 0.143 FSC.

Our model was refined using torsion angle, planar peptide, and Ramachandran restraints and thus did not use many degrees of freedom. The map-model FSC was determined as 5.8 Å at 0.5 FSC, with positive correlation to ∼4 Å. Since this concerns a model derived from our EM map and not an independently determined x-ray model, as was the case in the Zhang and Scheres & Chen papers, this number is not a reliable measure of the quality of the map or the “correctness” of the model. The majority of the helices show groves with 5.4 Å spacing, and β-strands are clearly resolved in the best parts of the map (see Figure 5) showing that the local resolution in these map regions is evidently better than 4.8 Å. The overall resolution estimate is therefore an average of these well-resolved protein regions and other regions that are less well resolved, especially those at the periphery of the complex. We expect that a resolution test in which only the best map regions are considered would indicate significantly better resolution. However, this would only serve to provide a better number, without improving the map or aiding its interpretation. The correctness of our trace can only be judged by a detailed analysis of the model, as described below.

2. The rotavirus map (X. Zhang et al., 2008) indeed provides a good comparison. The authors estimated the map of the icosahedrally (60-fold) averaged and then 13-fold averaged VP6 protein as 3.8 Å by comparison with an x-ray map. The FSC of this map indicated 4.5/4.1 Å at FSC 0.5 and 0.143, respectively. The same map with the icosahedral but not the 13-fold symmetry applied showed 6.5 resp. 5.1 Å. Our 12-fold symmetric, tetrahedral map indicates 6.7 resp. 5.5 Å with the gold-standard procedure, which is not dramatically different from the icosahedrally averaged VP6 protein. As mentioned above, we estimate the best regions of our map as ∼4.5 Å by comparison with a map calculated from the model.

There are many indications that our tracing is correct, involving either features of the model that agree with known general protein structure properties or specific properties of the Frh subunits.

A. As described in the text, conserved residues of FrhB and the FrhB family of F420-binding proteins are found near the cofactors.

B. Similarly, large side chains fall in densities that occur in every map and cannot be due to noise.

C. All predicted secondary structure elements were confirmed in the final model. In the case of FrhB, this was not the case for an earlier incorrect tracing based on a lower-resolution preliminary map; after noticing the mistake all helices and strands were accounted for, giving us confidence in the tracing.

D. All three proteins follow the rule that hydrophobic residues form the core of the protein and charged residues face the outside. We found several pockets lined with hydrophobic side chains, not just in FrhA and FrhG, where these features are shared with the bacterial protein used as a template for modelling, but also in FrhB. FrhB also contains a highly hydrophobic helix (27GIVTGLLAYAL), which is buried completely inside the subunit.

E. At some places there are breaks in extended protein stretches. After the whole complex was fitted, we noticed that most of these breaks coincide with a glycine residue (FrhA: G15, G17, G42, G217, G275, G322, G329; FrhG: G50, G56; FrhB: G44, G51, G71, G98).

F. One of the helices of the four-helix bundle has a pronounced kink. This helix was interpreted as FrhA 166–193 and a proline residue (Pro180) was found exactly at the position of the kink.

G. In the ferredoxin domain of FrhG residues 235–244 form a β-hairpin with Gly240 at the turn. The two β-strands were predicted and the hairpin is clearly visible in the density.

H. A predicted three-stranded β-sheet in FrhB (148–172) fits nicely in density. The only conserved region of this sheet, 163IGKGK, forms a turn close to the position of the isoalloxazine ring of F420. The location suggests that one or both of the lysine residues may interact with the F420 phosphate group.

I. The long α-helix on the surface that was interpreted as the C-terminal helix of FrhB is not very well resolved. The residues in the helix are mostly not conserved in FrhB, except at the N-terminal end. In our model, these residues are located at the access channel of the substrate F420 (near the loop 164GKGK mentioned above) and may be involved in substrate binding.

All the points mentioned above have been integrated in the manuscript, if they were not there already, either in the Results or the Discussion, where they were most appropriate. We have also added a movie (Video 5) showing the location of conserved residues in the de novo traced molecule, FrhB.
