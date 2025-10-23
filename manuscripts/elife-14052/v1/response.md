# Author response - Round 1

Authors:
- Shatanik Mukherjee
- Vera Jansen
- Jan F Jikeli
- Hussein Hamzeh
- Luis Alvarez
- Marco Dombrowski
- Melanie Balbach
- Timo Strünker
- Reinhard Seifert
- U Benjamin Kaupp
- Dagmar Wachten

## Response text

DOI: [10.7554/eLife.14052.017](https://doi.org/10.7554/eLife.14052.017)

1) The authors should extend the range of changes in Kd for cAMP binding to pH 8, since this can be achieved in alkaline environments in sperm flagella.

We have performed additional cAMP binding studies at pH 8 to determine the Kd. The Kd at pH 8 is 50 ± 13 nM, indicating that the affinity for cAMP increases upon alkalization. Of note, it has been reported for other CNBDs that the affinity for cAMP depends on the pH (Gordon et al., 1996; Kaupp & Seifert, 2002). The information has also been included in the manuscript and the text has been changed accordingly.

Also the results with 25mM NaHCO3 are ambiguous. Figure 2F indicates a strange pH sensitivity of the reporter, and it's not certain how pH changes upon NaHCO3 addition. A control experiment to measure pH upon NaHCO3 treatment, and an independent test of FRET changes of mlCNBD-FRET using a maneuver known to change pH in a defined manner (e.g. NH3 or lactate) would be helpful. Does the cAMP-insensitive mlCNBD-FRET-R307Q respond to NaHCO3?

To test whether NaHCO3 evokes a change in the intracellular pHi, we measured changes in pHi using BCECF in wild-type mouse sperm after stimulation with NaHCO3 and after stimulation with NH4Cl as a control. Stimulation with NH4Cl evoked a pronounced alkalization and, in turn, decreased the FRET ratio (Figure 5—figure supplement 1A, B). The kinetics of both changes were similar, indicating that the change in FRET is evoked by the change in pHi. In contrast, stimulation with NaHCO3 only evoked a miniscule and slow change in pHi (Figure 5—figure supplement 1A) that was not comparable to the rapid changes in FRET ratio after bicarbonate stimulation (see Figure 6C). These results support the notion that the changes in FRET evoked by NaHCO3 reflect changes in cAMP rather than pHi.

One reviewer noted that in Figure 7B, D, in the experiments where [Ca2+]o is manipulated, the authors interpret the changes of FRET signals as changes in [cAMP]. It is possible that the reduction/increase in [Ca2+]o also changes intracellular pH or [Ca2+], which in turn affects the FRET signal independent of changes in [cAMP] (Figure 2F). A simple "negative" control is perhaps to repeat the experiment in the presence of NKH477. The inhibitor presumably should also block the FRET changes induced by increases in [Ca2+]o.

To test whether [Ca2+]o affects the intracellular pH, we measured pHi using BCECF in wild-type mouse sperm after increasing or decreasing [Ca2+]o. As a control, sperm were stimulated with NH4Cl, which evoked a pronounced alkalization and, in turn, decreased the FRET ratio (Figure 5—figure supplement 1A, B). Reducing [Ca2+]o to 443 nM by addition of 3 mM BAPTA did not change the intracellular pH (Figure 7F).

We are sorry, but we do not understand the suggestion using NKH477. NKH477 is an activator (not inhibitor) of tmACs that are absent in sperm flagella; NKH477 has no effect on sperm cAMP levels (see Figure 6B).

2) The data presented indicate that mlCNBD-FRET has quite high affinity for cAMP (66nM purified protein, 73nM in situ in cells) and is saturated at around 3µM cAMP. Of note, the probe also has relatively high affinity for cGMP (504nM), which is similar to some other reporters designed expressly for this purpose. The high affinity for cAMP is very useful for assessing subtle variations in resting cAMP, but is buffering of cAMP a problem? Although Prm1-mICNBD-FRET males were fertile, was flagellar beating altered by the expression of mlCNBD-FRET?

This argument is well taken. As the reviewer also pointed out, Prm1-mlCNBD-FRET males are fertile, indicating that sperm function is not severely altered by the sensor. The flagellar beat frequency of wild-type and transgenic sperm was similar: wild-type: 8.4 ± 2.1 Hz, n = 8, 58 cells total; mlCNBD -FRET: 7.3 ± 3.0 Hz, n = 4, 40 cells total. The information has been added to Figure 4—source data 1.

3) Figure 3 demonstrates that the biosensor works well when expressed in HEK cells. However, only maneuvers expected to saturate the sensor are shown. Since low affinity probes based on Epac are also saturated by these treatments that produce massive amounts of cAMP (probably 50- 100µM), it is not surprising that mICNBD-FRET also becomes saturated. It would be nice to see the response to physiological stimulation with sub-maximal agonist concentrations, and also the reversibility of the probe (not by permeabilization with digitonin, but through PDE activity).

We agree. Accordingly, we performed a dose-response relationship for stimulation with NKH477 to activate the tmACs. The EC50 for NKH477 is 3.6 ± 0.6 µM (n = 4). This data set has been included in Figure 3—figure supplement 1F.

To show the reversibility of the sensor, we have alternatingly stimulated cells with isoproterenol followed by a wash-out with buffer. After wash-out, the FRET ratio was lowered and increased again after stimulation with isoproterenol, demonstrating the reversibility of the sensor. This data set has also been included in Figure 3—figure supplement 1G.

Figure 3G shows that the cAMP-insensitive mlCNBD-FRET-R307Q also demonstrates a modest decrease when digitonin is applied, calling into question whether the decreased baseline shown for the parent sensor reflects a true decrease in cAMP/cGMP below baseline.

The mlCNBD-FRET-R307Q mutant has been generated as a control to visualize any unspecific effects on the FRET ratio that are independent of cAMP. The small decrease in baseline for the mlCNBD-FRET-R307Q mutant is probably due to a permeabilization artefact. However, Figure 3G shows a larger decline of the FRET ratio after permeabilization with digitonin from the plateau that is reached after stimulation with NKH477.

4) The FLIM data are weak, with cerulean lifetime changes only from 2.44+/-02 to 2.38 +/-04 ns after large change in free cAMP. We suggest stating the FLIM data, but pointing out that it is not very suited to FLIM, unless the authors are able to obtain much more data supporting this claim. Thus that section of the figure can be removed.

Although the changes in cerulean lifetime in the FLIM measurements are relatively small, they are nonetheless significant. To the best of our knowledge, such FLIM measurements with cAMP FRET sensors have not yet been reported. Thus, we prefer to leave this figure as it is. However, we have rephrased the text to: “In summary, mlCNBD-FRET is an exquisitely sensitive biosensor for measuring cAMP dynamics in the nanomolar range, preferably using fluorescence intensity techniques, but also using lifetime-based techniques.”
