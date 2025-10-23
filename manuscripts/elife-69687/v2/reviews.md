# Peer review - Round 1

Editors:
- Ilaria Testa, KTH Royal Institute of Technology Sweden

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69687.sa1](https://doi.org/10.7554/eLife.69687.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript provides a new tool to study multi-protein interaction in living cells based on fluorescence fluctuation spectroscopy. The paper includes a reliable validation and description of the method as well as a proof of principle application and assessment of potential limitations.

Decision letter after peer review:

Thank you for submitting your article "Multi-color fluorescence fluctuation spectroscopy in living cells via spectral detection" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewers, and the evaluation has been overseen by Anna Akhmanova as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Erdinc Sezgin (Reviewer #2); Thorsten Wohland (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The manuscript is well written and the data very diligently analysed. There remain mainly technical questions and some points that should be discussed to ensure consistency of the results.

1. Figure 1: It seems like the time resolution of the measurements are on the order of several milliseconds. But the diffusion time measured are on the order of ~9 ms. With the time resolution relatively close to the measured diffusion time, did the authors check whether diffusion times are biased?

2. Page 11: Why are correlation amplitudes limited to positive values? The authors mention this also in the supplement but don't explain why that is necessary. For true correlations, only positive values should be obtained. And I assume that is so in their case, if not that should be addressed. Any negative values would be a clear indication that the correlation just indicates noise. This could also be compared with the actual correlation times measured. For correlations of noise, it is not only the amplitude that varies strongly but also the correlation times typically vary widely and mostly do no coincide with expected or reasonable values. The authors might be able to use that criterion to identify non-correlated data and thus avoid the positive amplitudes which are artifacts of the restrictions of the fitting parameters.

3. Page 11 and 12: It would be interesting if the authors could determine whether the observed correlation amplitudes are consistent with the probability of the different FPs (mEGFP, mEYFP, mCherry2 with rel cc amplitudes ranging from 0.45-0.79). If FRET influences these amplitudes, the authors might be even able to extract FRET efficiencies and demonstrate FRET. Another possibility would be to measure fluorescence lifetimes to determine FRET?

4. Page 19/20: The diffusion coefficient for the hetero-tetramer is only about half of the one determined for hetero-dimers. As these are membrane probes with the fluorescent proteins not expected to interact with the membrane, is there an explanation for the factor 2?

5. Did the authors determine the various observation volumes, given the concentrations they measure and the probability of fluorescence of the fluorescent proteins they determined? And is this consistent with the difference in diffusion coefficient they see for the hetero-oligomers?

6. Page 22: The authors indicate that they normalize their RSICS brightness data to measurements of monomers on the same day. It would be interesting if the authors could comment on the day-to-day variability of their calibrations.

7. Figure 3. M2 protein oligomerize but its interacting partner LC3 does not, does that mean each single LC3 associates with multiple M2 protein? Can authors confirm this by looking at the diffusion coefficients from the FCs curves?

8. The authors provided a validation of the method in HEK cells expressing the three Fluorescent Proteins in the plasma membrane in different oligomerization states (Figure 3C). I'm wondering how relatively changes in concentration/expression i.e. fluctuations within the 3 species of probes would influence the observable. Several applications might aim to study interaction within proteins of different abundance, it is important to understand the relative concentration range where the method can be used and provide reliable results. I suggest the authors to provide further experiment and eventually simulation to characterize such dynamic range.

9. The authors applied SFSCS to study how the Influenza A virus matrix protein 2 interact with the autophagy protein LC3 and the tetraspanin CD9. They found that IAV preferentially interact LC3 but not with CD9 (Figure 3). How the position of the label influences the cross-correlation studies?

10. For this technique to be applicable by other researchers, the data analysis tool should be openly available to others. Can authors put their software in an open repository?

11. Since it is a new technique all the limitations of the technique can be discussed in a "limitations" subsection. That would give the readers a clear picture what can and cannot be done with this new technique.

Reviewer #1 (Recommendations for the authors):

Multiplexing methods focusing on dynamic studies are challenging yet very important to understand cellular mechanism at the molecular level. Usually such studies are complex and done on specialized system, this work presents a method easily translatable to commercial system and compatible with standard fluorophores with a well-described analysis pipeline.

Therefore, it can open up several new dynamic studies with 3-4 fluorophores simultaneous read-out.

The choice of fluorophores, its dimerization tendency and the relative labeling densities of each species might influence the cross-correlation observable so a careful validation should be considered and discussed to validate the general applicability of the methodology in various biological applications.

To the author:

1 – The authors provided a validation of the method in HEK cells expressing the three Fluorescent Proteins in the plasma membrane in different oligomerization sates (Figure 3C). I'm wondering how relatively changes in concentration/expression i.e. fluctuations within the 3 species of probes would influence the observable. Several applications might aim to study interaction within proteins of different abundance, it is important to understand the relative concentration range where the method can be used and provide reliable results. I suggest the authors to provide further experiment and eventually simulation to characterize such dynamic range.

2 –The authors applied SFSCS to study how the Influenza A virus matrix protein 2 interact with the autophagy protein LC3 and the tetraspanin CD9. They found that IAV preferentially interact LC3 but not with CD9 (Figure 3). How the position of the label influences the cross-correlation studies?

Reviewer #2 (Recommendations for the authors):

In this paper, the authors developed a new modality of multi-color FCS using spectral detection to investigate stoichiometry of multi-component complexes in live cells. They showed the proof-of-principle with tandem proteins. Furthermore, they showed the biological application of their methodology by investigating Influenza virus components. This will be a useful addition to live cell spectroscopy tools to study protein-protein interactions. The authors' claims are supported by the data throughput the manuscript. The data is analyzed carefully, and results were reported clearly. This method is likely to be used by cell biologists to determine the stoichiometry of multi-protein complexes.

– Figure 3. M2 protein oligomerize but its interacting partner LC3 does not, does that mean each single LC3 associates with multiple M2 protein? Can authors confirm this by looking at the diffusion coefficients from the FCs curves?

– For this technique to be applicable by other researchers, the data analysis tool should be openly available to others. Can authors put their software in an open repository?

– Since it is a new technique all the limitations of the technique can be discussed in a "limitations" subsection. That would give the readers a clear picture what can and cannot be done with this new technique.

Reviewer #3 (Recommendations for the authors):

This manuscript is a carefully conducted study of multi-color fluorescence fluctuation spectroscopy as applied to plasma membranes. By using two-wavelength excitation and spectral detection in a scanning mode the authors show that they can determine the cross-correlation between up to four different probes in a single measurement. In addition, they build on their earlier work and show that the collected data can be analysed by Number and Brightness analysis, providing access to biomolecular stoichiometry. The authors use a range of protein constructs that include between one to four fluorescent proteins, which they use in different compositions to demonstrate that they can analyse all possible interactions of four probes in a single measurement. They then apply the technique to the interaction of influenza A proteins. They show that the influenza A virus (IAV) matrix protein 2 (M2) interacts more strongly with LC3 compared to CD9, both host cell factors. As they measure multiple probes simultaneously, the authors can go beyond binary correlations. Using triple correlations the authors show that they can detect the interaction of the proteins PA, PB1, and PB2 of the IAV polymerase complex. The extension of FCS to four probes, the demonstration of triple correlations and the application to a biological context provides important progress in fluorescence fluctuation spectroscopy and will allow the measurements of complex interactions at the cellular membranes.

The manuscript is well written and the data very diligently analysed. There remain mainly technical questions and some points that should be discussed to ensure consistency of the results.

1. Figure 1: It seems like the time resolution of the measurements are on the order of several milliseconds. But the diffusion time measured are on the order of ~9 ms. With the time resolution relatively close to the measured diffusion time, did the authors check whether diffusion times are biased?

2. Page 11: Why are correlation amplitudes limited to positive values? The authors mention this also in the supplement but don't explain why that is necessary. For true correlations, only positive values should be obtained. And I assume that is so in their case, if not that should be addressed. Any negative values would be a clear indication that the correlation just indicates noise. This could also be compared with the actual correlation times measured. For correlations of noise, it is not only the amplitude that varies strongly but also the correlation times typically vary widely and mostly do no coincide with expected or reasonable values. The authors might be able to use that criterion to identify non-correlated data and thus avoid the positive amplitudes whioch are artefacts of the restrictions of the fitting parameters.

3. Page 11 and 12: It would be interesting if the authors could determine whether the observed correlation amplitudes are consistent with the probability of the different FPs (mEGFP, mEYFP, mCherry2 with rel cc amplitudes ranging from 0.45-0.79). If FRET influences these amplitudes, the authors might be even able to extract FRET efficiencies and demonstrate FRET. Another possibility would be to measure fluorescence lifetimes to determine FRET?

4. Page 19/20: The diffusion coefficient for the hetero-tetramer is only about half of the one determined for hetero-dimers. As these are membrane probes with the fluorescent proteins not expected to interact with the membrane, is there an explanation for the factor 2?

5. Did the authors determine the various observation volumes, given the concentrations they measure and the probability of fluorescence of the fluorescent proteins they determined? And is this consistent with the difference in diffusion coefficient they see for the hetero-oligomers?

6. Page 22: The authors indicate that they normalize their RSICS brightness data to measurements of monomers on the same day. It would be interesting if the authors could comment on the day-to-day variability of their calibrations.
