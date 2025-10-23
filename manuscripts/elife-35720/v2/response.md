# Author response - Round 1

Authors:
- Ramasubramanian Sundaramoorthy ([ORCID: 0000-0003-4895-0980](https://orcid.org/0000-0003-4895-0980))
- Amanda L Hughes ([ORCID: 0000-0002-1976-6634](https://orcid.org/0000-0002-1976-6634))
- Hassane El-Mkami
- David G Norman ([ORCID: 0000-0002-7658-7720](https://orcid.org/0000-0002-7658-7720))
- Helder Ferreira
- Tom Owen-Hughes ([ORCID: 0000-0002-0618-8185](https://orcid.org/0000-0002-0618-8185))

## Response text

DOI: [10.7554/eLife.35720.047](https://doi.org/10.7554/eLife.35720.047)

Essential revisions:

1) For Figure 1, there are some concerns about whether the resolution of the 3D reconstruction is overestimated. Normally, in maps with resolution higher than 5 Å, bulky side chains become visible and β strands become separated, but such features cannot be recognized from the reconstruction, even in Figure 1—figure supplement 5. The local resolution estimation for the core histones is also shown to be ~4 Å resolution in Figure 1—figure supplement 4, however it appears lower than 4 Å. One way the authors can address this concern idea by using the high-resolution noise substitution method (Chen et al., Ultramicroscopy, 2013) in RELION. The authors should compare among the FSC curves of the masked FSC, the unmasked FSC, the phase-randomized FSC, and the masking-effect-corrected FSC.

FSC curves generated using the high resolution noise substitution method confirm our original assessment of overall average resolution as 4.5 Å (new Figure 1—figure supplement 4A). There is a masking effect and the unmasked FSC is lower at 6.5 Å (new Figure 1—figure supplement 4A). The phase randomised FSC indicates there is no overfitting. We removed the text “close to 4Å” to avoid the potential for over interpreting areas of higher local resolution. The colour scheme in the original Figure 1—figure supplement 4 did not clearly distinguish resolution in the range 4-5 Å, the revised version includes an improved colour map of the unfiltered envelope with and additional view. We have included an example illustrating that some bulky side chains fit the unsmoothed density map (new Figure 1—figure supplement 5). This is comparable to the fit observed in the 4.5 Å structure of 53BP1 bound to a nucleosome (PDB:5KGF) and not as good as that observed in the 3.9 Å structure (EMDB 8140).

2) The authors need to show multiple views of the final reconstructions, because Figure 1—figure supplement 4B is the only view from the top. It is easier to understand the 3D structure, if multiple views are presented. In particular, locations of the ubiquitin at the unwrapped and wrapped sides of the nucleosome are important points in this manuscript, both of which are missing in this figure.

Additional views are now presented in the new Figure 1—figure supplement 4B.

3) Regarding local resolution estimation in Figure 1—figure supplement 4B, the authors mentioned that "The resolution varies within the map, with resolution close to 4 Å in the region occupied by the nucleosome and ATPase lobes and lower resolution in the vicinity of the DNABD and ubiquitin peptides (Figure 1—figure supplement 4B)." However, I cannot recognize the ubiquitin peptides in the map with local resolution. The authors need to change the contour level of the map to allow visualization of the ubiquitin peptides on the local resolution estimation map.

Density for the ubiquitin peptides is visible in the revised figure.

4) The FSC curve of the 2:1 Chd1-nucleosome complex (Figure 2—figure supplement 1E, no indication for X-Y axis) does not appear healthy enough to determine the resolution of the 3D reconstruction. According to the book chapter written by Pawel Penczek (Resolution Measures in Molecular Electron Microscopy, Methods in Enzymology, p73-p100, 2010), "Artifactual "rectangular" FSC: remains one at low frequencies, followed by a sharp drop, in high frequencies oscillates around zero. Typically, it is caused by a combination of alignment of noise and a sharp filtration during the alignment procedure. The FSC never drops to zero in the entire frequency range. Normally, this means that the noise component in the data was aligned, the results are artifactual and the resolution is undetermined." To avoid the artifactual reconstruction from noise, as performed by Mao et al. (PNAS, 2013; also see Henderson, PNAS, 2013), for example, the authors need to reprocess the data to obtain a reliable FSC for the 3D reconstruction.

We appreciate the concerns raised. The data has been reprocessed as suggested. The revised FSC curves are much healthier allowing resolution to be estimated at 11 Å.

5) There were a few concerns about the reasoning used by the authors to suggest that singly bound structure is the active conformation.

The structures of Chd1 bound nucleosomes present a conundrum as the directionality inferred from the structures is opposite to what is anticipated based on the known biochemical properties of Chd1. The comments below have been thought provoking and we have revised and shortened this part of the discussion substantially.

i) The authors do not explain how the published DNA gaps data can be reconciled with the cross-gyres conformation being the active conformation as opposed to the same-gyres conformation.

The gaps data are presented as evidence for ATPase binding to the SHL2 location on the same gyre as the entry DNA.

ii) Previous work has shown that Chd1 can move nucleosomes by 23-29 base-pairs without a stall, which is more than the 7 bp that is contacted by the DBD. The authors use this data as evidence against the cross-gyres conformation. This reasoning is not clear because the ISWI ATPases (Deindl et al., 2013) have step sizes as assessed by smFRET that are not correlated with the amount of DNA that is contacted by their DBDs. Further depending on the processivity of the enzyme the amount of DNA moved before a stall could be several multiples of 7 bp.

This is a good point, the difference in the initial and subsequent step sizes observed in the Deindl paper is mentioned in the revised Discussion.

iii) In the Discussion, the authors say: "This is anticipated if the DNA binding domain acts to generate an active conformation, but not if sensing of exit linker DNA is repressive." However, the ATPase data from Nodelman et al. (2017) shows a repressive effect of exit linker DNA. This should be discussed.

This data is mentioned in the revised Discussion.

iv) In the Discussion, the authors say: "Thirdly, the activity of chimeric Chd1 proteins in which DNA binding is provided via a heterologous domain is greatest when the cognate binding site is placed in the entry linker mimicking the arrangement observed in the Chd1-nuceosome structure". While this data is consistent with the cross-gyres conformation being the active conformation, the data is also consistent with the same-gyres conformation being active if what is being trapped by EM is the inactive state. In other words this prior data does not rule out the same-gyres conformation being the active conformation.

This is a good point we removed this section.

6) A few straightforward biochemical tests are required to test the mechanistic significance of the structural data. The authors can investigate the functional effects on nucleosome sliding of mutating the Chd1 lobe II residues that make contacts with the H3-alpha1 helix and the 25 N-terminal residues that are hypothesized to contact the unpeeled DNA.

New data has been added showing that deleting the lobe II residues abolishes Chd1 activity in nucleosome sliding (Figure 2—figure supplement 5). The truncation of the H3 tail to K36 unexpectedly stimulates Chd1 activity quite strongly. However, deletion to 26 has no effect. This indicates that the interaction of the N-terminal region of the tail with DNA is not required for it to exert a repressive effect. This shows an important role for the histone H3 N-terminal tail in Chd1 action. The new data is included as Figure 8—figure supplement 1.
