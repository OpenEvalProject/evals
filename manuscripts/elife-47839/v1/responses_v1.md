# Author response - Round 1

Authors:
- Jooyoung Park ([ORCID: 0000-0001-8557-641X](https://orcid.org/0000-0001-8557-641X))
- Brinda Selvaraj
- Andrew C McShan ([ORCID: 0000-0002-3212-9867](https://orcid.org/0000-0002-3212-9867))
- Scott E Boyken ([ORCID: 0000-0002-5378-0632](https://orcid.org/0000-0002-5378-0632))
- Kathy Y Wei ([ORCID: 0000-0002-8794-1385](https://orcid.org/0000-0002-8794-1385))
- Gustav Oberdorfer
- William DeGrado
- Nikolaos G Sgourakis ([ORCID: 0000-0003-3655-3902](https://orcid.org/0000-0003-3655-3902))
- Matthew J Cuneo ([ORCID: 0000-0002-1475-6656](https://orcid.org/0000-0002-1475-6656))
- Dean AA Myles ([ORCID: 0000-0002-7693-4964](https://orcid.org/0000-0002-7693-4964))
- David Baker ([ORCID: 0000-0001-7896-6217](https://orcid.org/0000-0001-7896-6217))

## Response text

DOI: [10.7554/eLife.47839.sa2](https://doi.org/10.7554/eLife.47839.sa2)

[…]

Essential revisions:

1) How general is this design approach? The manuscript describes in detail one designed binder; were others attempted but failed? Was there anything to learn from these failures about the designed proteins' expression, stability or ligand binding?

In total, we attempted 70 designs. There were varying levels of expression, stability, and ligand binding, the details of which have now been added to the Results section. We have also elaborated on our learnings in the Discussion section:

“Our results suggest two major bottlenecks to the goal of an amantadine-inducible trimerization system based on amantadine binding at a helical bundle three-fold interface: 1) Amantadine, given its small size, does not provide strong driving force for trimerization. 2) Well behaved monomers in the absence of amantadine are hard to achieve given the extensive exposed subunit interaction surface. Success in designing protein homo-trimerization systems will likely require smaller subunit interfaces and higher affinity binding sites, perhaps using larger C3 molecules.”

2) The main concern in the manuscript is the determination of the binding affinity. There is no doubt that amantadine binds, but with the high ligand concentrations used in crystallography (and some of the NMR experiments) also very weakly interacting molecules could bind. The affinity is determined using NMR line shape analysis with only 4 ligand concentrations. This is less than the number of fitting parameters in the model. In comparison, in the TITAN publication, the experimental data were analyzed using 23 ligand concentrations. Beyond the graphical display in Figure 2—figure supplement 2 (which is difficult to evaluate) there is no presentation of the quality of fit. Also, the lowest used ligand concentration is almost 3 times more than the presented KD. Given that the system is in slow exchange it should be possible to fit the KDto the chemical shift values directly rather than through a line shape analysis, which is considerably more complex and difficult to validate. In any case, 4 conditions are too few for a reasonable KDdetermination and more concentrations should be tested.

The reviewer is correct. First, we note that the exact value of the measured KD is not central to the conclusion of our manuscript. While indeed amantadine may bind weakly (estimated KD of 24.1 μM by NMR and measured KD of 39.8 μM by ITC (see below)), the stability of the amantadine-ABP complex was sufficient to observe it also by X-ray crystallography and neutron scattering. Second, to provide corrorborating evidence to the KD estimated by solution NMR, we have determined the KD by an analogous method, ITC, as mentioned below.

Because of the important points raised by the reviewer, in the updated manuscript we have revised the Results section to place less emphasis and significance to the KD value estimated by solution NMR.

“An NMR line shape fitting of the three most significantly affected ABP methyl resonances (> 0.1 ppm chemical shift deviation between free and bound states) using TITAN, suggests a dissociation constant (KD) of 24.1 ± 2.7 μM and upper limit for off-rate constant (koff) of 60.7 ± 5.6 s-1 (on-rate constant of 2.5 x106 M-1 s-1) (Figure 2—figure supplement 2), which is within a factor of two of the KD value of 39.8 ± 3.1 μM estimated by ITC (Figure 2—figure supplement 3).”

Alternatively, it should also be straightforward to use a complementary method like ITC on this system to determine KD. The CD data also suggests weak binding with Kd:s higher than reported. It is suggested in the manuscript that the presence of 1 mM amantadine does not alter the CD temperature denaturation. Binding to a folded state always results in increased stability, see for example Cimmperman et al., 2008. If there is no change in Tm upon addition of amantadine this should, therefore, be commented on.

As suggested by the reviewer, we have additionally used an alternative method (ITC) to measure the binding between ABP and amantadine. We find that the determined KD between ABP and amantadine, in corroboration of our solution NMR experiments, is 39.8 μM. These new findings have been incorporated as Figure 2—figure supplement 3 and the Results section.

3) The fact that the ligand does not interact via the designed hydrogen-bond network adds to other reports in the literature on the difficulty of designing hydrogen-bond networks in functional sites. Are there any lessons to learn on how to improve the chances of accurately designing hydrogen-bond networks in binding sites?

The greatest lesson was the fact that including explicit water molecules in the Rosetta design calculations could contribute to generating a protein that can bind amantadine with higher affinity. As a result, the lab is focusing Rosetta development efforts in this area specifically, which we hope will expand the scope of computational protein design. Despite being a “negative result,” we hope the sharing of this information will encourage readers to consider and employ explicit water molecules in future research efforts. We have updated the text in the Results section to elaborate on this lesson.

[Editors’ note: the author responses to the second round of peer review follow.]

[…]

Reviewer #1:

[…]

In particular they provided additional data for binding in form of an ITC titration. This data is, however, not supportive of binding. There is no stoichiometric binding phase that allows determining deltaH, and N(sites) is calculated to be 0.1 which would mean that only 10% of the protein bind the ligand. No KDcan be deduced from such data, and this titration cannot be used as supporting evidence. Maybe the binding affinity is below what is measurable by ITC, but this would be rather in the mM and not μM range.

We agree the ITC data are inconclusive. This is likely because the enthalpy of binding is very small due to the small size of the compound. We should not have included it in the original revised manuscript and have removed it in the current revision.

Considering that NMR and Thermofluor are giving a different signal in the presence of amantadine then in its absence, while the CD spectra and Tmelt show no difference with and without ligand, it remains unclear how the designed protein behaves. If it is molten globule like as discussed with respect to the Thermofluor data, then this is expected to be observable in CD as well.

This is simply not correct – CD reports on secondary structure, not tertiary structure, and there is a very long history of designed proteins with highly helical CD spectra with molten cores. In our case, since only the region around the amantadine binding site is likely to be molten in the apo state, one would expect very little change in the CD signal.

If the binding affinity is in the μM range then it should be measurable with alternative methods, too. Or the binding constant from NMR data is overfitted after all. So unfortunately some of my concerns still remain after the revision.

It is not straightforward to measure binding constants for small molecules to proteins in the μM range. NMR line shape analysis provides a sensitive approach to do this. In the current revision, we have included a titration curve with amantadine which suggests a KD in the reported range (Figure 2E).

To explore the accuracy of our estimated dissociation constant, we performed independent fits of the same NMR line shapes using a fixed KD to values 2x above and below the free-fitted value (Supplementary file 3); these fits resulted in an increase in residuals.

We also performed an independent analysis of the same NMR titrations by plotting the relative intensity of the bound state resonance (in slow exchange with the free form) (Figure 2D). This complementary analysis of our data which does not account for exchange contributions to the NMR line shape yielded an upper limit for the KD of 55 μM, also taking into account the fit error. This is consistent with the 24 μM KD obtained from the line shape analysis.

[Editors’ note: the author responses to the third round of peer review follow.]

In addition to the changes indicated in the revised manuscript provided with the appeal, the description of the KD determined in the NMR titration should be toned down slightly to indicate that it is an apparent KD. The fact that ABP monomers adopt a variety of conformers almost certainly confounds the NMR line shape analysis used to derive the KD. In addition, the appeal letter notes that the ITC data were removed but are still in the revised manuscript supplied.

We have made the following requested minor additional changes to the description of the KD determined in the NMR titration:

1) “An NMR line shape fitting … suggest an apparent dissociation constant (KD) of 24.1 ± 2.7 μM …” (subsection “Solution NMR analysis of amantadine binding”)

2) “Together, these data suggest that amantadine likely binds to ABP with an apparent KD in the low μM range.” (subsection “Solution NMR analysis of amantadine binding”)
