# Author response - Round 1

Authors:
- Susanne Gerndt
- Cheng-Chang Chen ([ORCID: 0000-0003-1282-4026](https://orcid.org/0000-0003-1282-4026))
- Yu-Kai Chao ([ORCID: 0000-0002-1202-2448](https://orcid.org/0000-0002-1202-2448))
- Yu Yuan
- Sandra Burgstaller
- Anna Scotto Rosato
- Einar Krogsaeter ([ORCID: 0000-0001-8232-5498](https://orcid.org/0000-0001-8232-5498))
- Nicole Urban
- Katharina Jacob
- Ong Nam Phuong Nguyen
- Meghan T Miller
- Marco Keller
- Angelika M Vollmar
- Thomas Gudermann
- Susanna Zierler ([ORCID: 0000-0002-4684-0385](https://orcid.org/0000-0002-4684-0385))
- Johann Schredelseker ([ORCID: 0000-0002-6657-0466](https://orcid.org/0000-0002-6657-0466))
- Michael Schaefer
- Martin Biel
- Roland Malli ([ORCID: 0000-0001-6327-8729](https://orcid.org/0000-0001-6327-8729))
- Christian Wahl-Schott
- Franz Bracher
- Sandip Patel
- Christian Grimm ([ORCID: 0000-0002-0177-5559](https://orcid.org/0000-0002-0177-5559))

## Response text

DOI: [10.7554/eLife.54712.sa2](https://doi.org/10.7554/eLife.54712.sa2)

Essential revisions:

1) The currents produced by TPC2-A1-N and NAADP are quite small, which makes Vrev particularly prone to errors from leak current contamination. For example, TPC2-A1-N activates a H+ current (Figure 4L). If this current is subtracted from the total current in Figure 2K, the Vrev will shift to a more negative value and the calculated PCa/PNa will be much smaller than that shown in Figure 2Q. A similar argument applies to the NAADP-activated current. This problem could be ameliorated by repeating the TPC2-A1-N and NAADP measurements using larger currents. This may be achievable by recording from L11A/L12A mutant channels in the plasma membrane. If this is not possible, the authors should qualify their estimates of the selectivity for TPC2-A1-N and NAADP accordingly. To strengthen the statistics, it would also be useful to increase the numbers of recordings used to calculate PCa/PNa (currently only 4 in Figure 2Q). Finally, it would be informative (though not absolutely essential) to show the time course of current activation.

We want to clarify that the measurements in Figure 2K cannot be directly compared with the measurements shown in Figure 4L. In Figure 2K endolysosomal patch-clamp experiments were performed using bi-ionic conditions. While the conditions in Figure 4L are not bi-ionic. But we agree with the concern regarding the proton effect. Based on the data that we showed in old Figure 2—figure supplement 1A-D, where we used a pipette solution with mixed Ca/Na, we can conclude that it is indeed the calcium leading to the shift in Erev not protons. See also new Figure 2—figure supplement 1D-F.

(A) Agonist-evoked cation currents from enlarged endo-lysosomes isolated from HEK293 cells stably expressing human TPC2 using the following conditions: luminal solution containing 114 mM Na+ and 30 mM Ca2+, pH 4.6; bath solution containing 160 mM Na+, pH 7.2 (n = 3, each). (B) Expanded view of A. (C-D) Statistical analyses of Erev (C) and permeability ratio (PCa/PNa) (D) using either bi-ionic conditions as shown in Figure 2K-S or conditions as used in A and B.

We appreciate the suggestion to measure NAADP currents in the PM. Unfortunately however, NAADP measurements using the plasma membrane variant of TPC2 consistently failed in our hands, possibly due to lack of an accessory protein necessary for the NAADP effect.

To strengthen the statistics, we have now increased the numbers of recordings used to calculate PCa/PNa in Figure 2K-Q from n = 4 and 6 to n = 9 and 10.

2) That the compounds fail to activate TRPML channels shows a degree of selectivity, but to use these compounds to probe TPC channel function in vivo it is important to know whether the compounds are specific for TPC2 over TPC1. This is especially true given the use of TPC2 in the names of these compounds. This should be tested.

We absolutely agree with the reviewers and now provide new data using endolysosomal patch-clamp showing that neither TPC2-A1-P nor TPC2-A1-N has an activating effect on TPC1. See new Figure 1—figure supplement 7.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) Essential revision #1: The point the reviewers were making is that contamination of the TPC2-A1-N-induced current by H+ current may have shifted the reversal potential in the positive direction, which would overestimate the relative PCa/PNa. Since the currents are quite small, the effect of H+ current contamination could be significant. You have explained that it is not possible to record larger currents from PM-targeted channels, which would have minimized the contamination effect. That is fine, but there should be some estimate in the paper about the possible size of the error from H+ current contamination. This could be done by subtracting the average H+ current I/V from the average TPC2-A1-N and NAADP current I/Vs, and recalculating Vrev and PCa/PNa. The question is, how much would it affect the result?

We have updated the representative I-V plots of Figure 2K, L and O based on the increased n numbers that are now available in this dataset. Please note, the luminal pH of the bi-ionic measurements was 4.6 while the luminal pH of the H+ conductance measurements was 4.4. Hence, there is an almost two-fold difference in proton concentration. The composition of the applied solutions in these two series of experiments are also different: high concentration of Na+ and Ca2+ were applied for bi-ionic measurements versus Na+/Ca2+-free in NMDG+/H+ experiments.

Nevertheless, we now account for the H+ current “contamination” by subtracting the average H+ current I/V from the average current IVs for TPC2-A1-N and TPC2-A1-P as requested (see Author response image 2). The difference of PCa/PNa between TPC2-A1-P and TPC2-A1-N is not affected (0.44 for TPC2-A1-N and 0.06 for TPC2-A1-P). To clarify this we have now added the following sentence:

“Proton permeability did not substantially change our estimates of relative Ca2+ and Na+ permeability as PCa/PNa values were similar when proton currents were subtracted from currents obtained under bi-ionic conditions (0.44 for TPC2-A1-N and 0.06 for TPC2-A1-P).”

(A) I-Vs from Figure 2K/L (Na+/Ca2+ bi-ionic condition) and Figure 4L/M (NMDG+/H+ condition). (B) Expanded views of I-Vs after subtracting the average H+ current from the average Na+/Ca2+ currents from A. (C) Relative cationic permeability ratios (PCa/PNa) calculated from data in B.

2) The equation that was added to the Materials and methods for calculating PCa/PNa under non-bi-ionic conditions should have correction factors for Na+ and Ca2+ activity coefficients (as in the bi-ionic equation). The PCa/PNa values in Figure 2—figure supplement 1F should be replotted using the corrected values). Please provide a reference for the non-bi-ionic equation. Also, use a consistent term for reversal potential in the two equations (e.g., Erev).

We corrected the equation as follows:

PCaPNa=γNaγCa∙Nai∙expErevFRT-Nao4Cao∙expErevFRT+1

A reference is cited now: Jackson, 2006.

3) The new values of PCa/PNa for TPC2-A1-N under bi-ionic conditions (Figure 2—figure supplement 1F) do not agree with results of the bi-ionic equation. With Vrev=-17 mV, Nai=160 mM, Cao=105 mM, PCa/PNa is 0.42, not 0.65 as in the figure.

We have increased the n numbers to 9 and 10, respectively. In the supplementary figure this had not been adapted yet. We have now corrected and updated this figure. 0.65 is correct.

Also, the text refers to 140 mM Na+ but the Figure 2 shows 160 mM Na+.

We have corrected this in the text. 160 mM Na+ is correct.

In Figure 2P Vrev for TPC2-A1-N is -12 mV, but -17 mV in Figure 2—figure supplement 1E. Are these different datasets, and if so, why? To avoid confusion, it would be best to consolidate all the bi-ionic measurements and make sure the values in Figure 2P, Q and Figure 2—figure supplement 1E, F are the same. Text should be edited accordingly.

We have increased the n numbers to 9 and 10, respectively. In the supplementary figure this had not been adapted yet. We have now corrected and updated this figure.

4) The error bar in Figure 2—figure supplement 1F for TPC2-A1-P goes below zero, which is not physically possible. Please check the calculations.

We have recalculated this and corrected accordingly.
