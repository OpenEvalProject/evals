# Correction: Emergent periodicity in the collective synchronous flashing of fireflies

## Authors

- Raphael Sarfati
- Kunaal Joshi ([ORCID: 0000-0002-8001-1230](https://orcid.org/0000-0002-8001-1230))
- Owen Martin
- Julie C Hayes
- Srividya Iyer-Biswas
- Orit Peleg ([ORCID: 0000-0001-9481-7967](https://orcid.org/0000-0001-9481-7967)) †

† Corresponding author

## Dataset corrections

After the acceptance of the paper, we discovered that one of the firefly flash recordings had been accidentally mislabeled. The problematic dataset in question involved an experiment with 20 fireflies. On the evening of June 7, 2020, members of the Peleg lab conducted two separate tent experiments simultaneously, one of which involved a set of LEDs. This setup was not part of the experiment reported in the paper. The LEDs were programmed to mimic the interburst intervals (Tb) observed in wild fireflies, incrementally adjusting the Tb parameter value to determine an optimal value for entrainment. This triggered us to carefully review our data, including the raw movies, the flash-time series, interburst interval (Tb) values, and our field notes, and we found the following corrections are required.

We include below Figure 1, which provides a visual comparison of the original and corrected datasets, as well as a table summarizing the corrected dataset (Table 1) and the original dataset (Table 2). We also include both the original and corrected datasets themselves, for transparency.

![Figure 1.](https://cdn.elifesciences.org/articles/109449/elife-109449-fig1-v1.jpg)

**Figure 1.:** A), 5ff (B), 10ff (C), 15ff (D), and 20ff (E), before and after making corrections to the dataset.Please note that the distributions of 5, 10, and 15ff remain unchanged. The bin size is set to 3 seconds.

## Theoretical model validation

As a first sanity check, we have compared the original theory outputs to the original dataset minus the problematic data recordings (i.e., trimming 06072020 u to 15 minutes, and removing 06102021 c). As expected, the comparison between theory and experimental data is still robust (Figure 2).

![Figure 2.](https://cdn.elifesciences.org/articles/109449/elife-109449-fig2-v1.jpg)

**Figure 2.:** A), 10ff (B), 15ff (C), 20ff (D), and the resulting standard deviation of the interburst interval (Tb) (E), after removing the affected data points from the original dataset.The removal has no effect on the main conclusions.

Next, based on the revised single-firefly interburst intervals, we regenerated the input envelope used in the analytical theory. We have updated Figure 3 with the new theoretical distributions generated from this revised input envelope (Figure shown below).

## Computational model correction

We discovered that Figure 7 erroneously displayed the difference in medians between distributions instead of the intended two-sided Kolmogorov–Smirnov (K-S) test statistic.

During our review, we also found a minor error in the Methods section, Agent-based simulation, Simulation parameters and in the original caption of Figure 7, which stated that ten simulation trials were conducted. In fact, thirty trials were run in all cases, both in the published and updated figures.

## Updates to text and figures

Methods section, Experimental data:

Corrected text:

We observed 10 individual fireflies alone in the tent, over durations between 5 min and 85 min. We observed that although these fireflies produced flash trains at a frequency of about 2 Hz, the delay between successive trains was apparently randomly distributed, from a few seconds to tens of minutes. Then, we carried out three sets of experiments with 5, 10, 15, and 20 fireflies, using the segments between 9 minutes and 15 minutes. As previously reported, collective burst flashing only appears at about 15 fireflies.

Original text:

We observed 10 individual fireflies alone in the tent, over durations between 30 min and 90 min. We observed that although these fireflies produced flash trains at a frequency of about 2 Hz, the delay between successive trains was apparently randomly distributed, from a few seconds to tens of minutes. Then, we carried out 3 sets of experiments where the number of fireflies was increased to 5, then 10, then 15, then 20, each condition being maintained between 15 min and 30 min. As previously reported, collective burst flashing only appears at about 15 fireflies.

Methods section, Experimental data correction:

Added text:

After the paper’s acceptance, a small subset of data points was updated for the reasons described in the Supplementary Appendix. We repeated all analyses and confirmed that the findings are unaffected. Both the original and corrected datasets are publicly available.

Original text: n/a

Methods section, Agent-based simulation, Simulation parameters:

Corrected text:

For each set of parameters, we ran simulations for thirty trials of 200,000 timesteps each.

Original text:

For each set of parameters, we ran simulations for ten trials of 200,000 timesteps each.

Discussion and concluding remarks section:

Corrected text:

As shown in Fig. 3, the chosen values for beta, the additional fitting parameter introduced in the agent-based simulation, are: β=0.16, 0.16, 0.20 and 0.30 respectively for N=5, 10, 15, 20.

Original text:

As shown in Fig. 3, the chosen values for beta, the additional fitting parameter introduced in the agent-based simulation, are: β=0.18, 0.13, 0.12 and 0.64 respectively for N=5, 10, 15, 20.

Figure 7 Caption:

Corrected text:

The best values for each N=5,10,15,20 are β=0.16, β=0.16, β=0.20, β=0.30.

Original text:

The best values for each N=5,10,15,20 are β=0.18, β=0.13, β=0.12, β=0.64.

The corrected Figure 1 is shown here (only panel D was updated):

![Figure](https://cdn.elifesciences.org/articles/109449/elife-109449-fig3-v1.jpg)

The originally published Figure 1 is shown for reference:

![Figure](https://cdn.elifesciences.org/articles/109449/elife-109449-fig4-v1.jpg)

The corrected Figure 3 is shown here:

![Figure](https://cdn.elifesciences.org/articles/109449/elife-109449-fig5-v1.jpg)

The originally published Figure 3 is shown for reference:

![Figure](https://cdn.elifesciences.org/articles/109449/elife-109449-fig6-v1.jpg)

The corrected Figure 5 is shown here:

![Figure](https://cdn.elifesciences.org/articles/109449/elife-109449-fig7-v1.jpg)

The originally published Figure 5 is shown for reference:

![Figure](https://cdn.elifesciences.org/articles/109449/elife-109449-fig8-v1.jpg)

The corrected Figure 7 is shown here:

![Figure](https://cdn.elifesciences.org/articles/109449/elife-109449-fig9-v1.jpg)

The originally published Figure 7 is shown for reference:

![Figure](https://cdn.elifesciences.org/articles/109449/elife-109449-fig10-v1.jpg)

The article has been corrected accordingly.
