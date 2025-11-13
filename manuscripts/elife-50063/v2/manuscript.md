# Drosophila PSI controls circadian period and the phase of circadian behavior under temperature cycle via tim splicing

## Authors

- Lauren E Foley<sup>1</sup> ([ORCID: 0000-0001-7635-7338](https://orcid.org/0000-0001-7635-7338))
- Jinli Ling<sup>1</sup>
- Radhika Joshi<sup>1</sup>
- Naveh Evantal<sup>2</sup>
- Sebastian Kadener<sup>2</sup> ([ORCID: 0000-0003-0080-5987](https://orcid.org/0000-0003-0080-5987))
- Patrick Emery<sup>1</sup> ([ORCID: 0000-0001-5176-6565](https://orcid.org/0000-0001-5176-6565)) †

### Affiliations

1. Department of Neurobiology University of Massachusetts Medical School Worcester United States
2. Hebrew University of Jerusalem Jerusalem Israel
3. Brandeis University Waltham United States

† Corresponding author

## Abstract

The Drosophila circadian pacemaker consists of transcriptional feedback loops subjected to post-transcriptional and post-translational regulation. While post-translational regulatory mechanisms have been studied in detail, much less is known about circadian post-transcriptional control. Thus, we targeted 364 RNA binding and RNA associated proteins with RNA interference. Among the 43 hits we identified was the alternative splicing regulator P-element somatic inhibitor (PSI). PSI regulates the thermosensitive alternative splicing of timeless (tim), promoting splicing events favored at warm temperature over those increased at cold temperature. Psi downregulation shortens the period of circadian rhythms and advances the phase of circadian behavior under temperature cycle. Interestingly, both phenotypes were suppressed in flies that could produce TIM proteins only from a transgene that cannot form the thermosensitive splicing isoforms. Therefore, we conclude that PSI regulates the period of Drosophila circadian rhythms and circadian behavior phase during temperature cycling through its modulation of the tim splicing pattern.

## Introduction

Circadian rhythms are the organism’s physiological and behavioral strategies for coping with daily oscillations in environment conditions. Inputs such as light and temperature feed into a molecular clock via anatomical and molecular input pathways and reset it every day. Light is the dominant cue for entraining the molecular clock, but temperature is also a pervasive resetting signal in natural environments. Paradoxically, clocks must be semi-resistant to temperature: they should not hasten in warm summer months or lag in the winter cold (this is called temperature compensation), but they can synchronize to the daily rise and fall of temperature (temperature entrainment) (Pittendrigh, 1960). Not only can temperature entrain the clock, it also has a role in seasonal adaptation by affecting the phase of behavior (see for example Majercak et al., 1999).

Molecular circadian clocks in eukaryotes are made up of negative transcriptional feedback loops (Dunlap, 1999). In Drosophila, the transcription factors CLOCK (CLK) and CYCLE (CYC) bind to E-boxes in the promoters of the clock genes period (per) and timeless (tim) and activate their transcription. PER and TIM proteins accumulate in the cytoplasm where they heterodimerize and enter the nucleus to feedback and repress the activity of CLK and CYC and thus downregulate their own transcription (Hardin, 2011). This main loop is strengthened by a scaffolding of interlocked feedback loops involving the transcription factors vrille (vri), PAR domain protein 1 (Pdp1) and clockwork orange (cwo). Post-translational modifications are well-established mechanisms for adjusting the speed and timing of the clock (Tataroglu and Emery, 2015).

Increasing evidence indicates that post-transcriptional mechanisms controlling gene expression are also critical for the proper function of circadian clocks in many organisms. In Drosophila, the post-transcriptional regulation of per mRNA has been best studied. per mRNA stability changes as a function of time (So and Rosbash, 1997). In addition, per contains an intron in its 3’UTR (dmpi8) that is alternatively spliced depending on temperature and lighting conditions (Majercak et al., 1999; Majercak et al., 2004). On cold days, the spliced variant is favored, causing an advance in the accumulation of per transcript levels as well as an advance of the evening activity peak. This behavioral shift means that the fly is more active during the day when the temperature would be most tolerable in their natural environment. The temperature sensitivity of dmpi8 is due to the presence of weak non-canonical splice sites. However, the efficiency of the underlying baseline splicing is affected by four single nucleotide polymorphisms (SNPs) in the per 3’UTR that vary in natural populations and form two distinct haplotypes (Low et al., 2012; Cao and Edery, 2017). Also, while this splicing is temperature-sensitive in two Drosophila species that followed human migration, two species that remained in Africa lack temperature sensitivity of dmpi8 splicing, (Low et al., 2008). Furthermore, Zhang et al. (2018) recently demonstrated that the the trans-acting splicing factor B52 enhances dmpi8 splicing efficiency, and this effect is stronger with one of the two haplotypes. per is also regulated post-transcriptionally by the TWENTYFOUR-ATAXIN2 translational activation complex (Zhang et al., 2013; Lim et al., 2011; Lim and Allada, 2013a; Lee et al., 2017). This complex works by binding to per mRNA as well as the cap-binding complex and poly-A binding protein. This may enable more efficient translation by promoting circularization of the transcript. Interestingly, this mechanism appears to be required only in the circadian pacemaker neurons. Non-canonical translation initiation has also been implicated in the control of PER translation (Bradley et al., 2012). Regulation of PER protein translation has also been studied in mammals, with RBM4 being a critical regulator of mPER1 expression (Kojima et al., 2007). In flies however, the homolog of RBM4, LARK, regulates the translation of DBT, a PER kinase (Huang et al., 2014). miRNAs have emerged as important critical regulators of circadian rhythms in Drosophila and mammals, affecting the circadian pacemaker itself, as well as input and output pathways controlling rhythmic behavioral and physiological processes (Tataroglu and Emery, 2015; Lim and Allada, 2013b).

RNA-associated proteins (RAPs) include proteins that either bind directly or indirectly to RNAs. They mediate post-transcriptional regulation at every level. Many of these regulated events – including alternative splicing, splicing efficiency, mRNA stability, and translation – have been shown to function in molecular clocks. Thus, to obtain a broad view of the Drosophila circadian RAP landscape and its mechanism of action, we performed an RNAi screen targeting 364 of these proteins. This led us to discover a role for the splicing factor P-element somatic inhibitor (PSI) in regulating the pace of the molecular clock through alternative splicing of tim.

## Results

### An RNAi screen for RNA-associated proteins controlling circadian behavioral rhythms

Under constant darkness conditions (DD) flies have an intrinsic period length of about 24 hr. To identify novel genes that act at the post-transcriptional level to regulate circadian locomotor behavior, we screened 364 genes, which were annotated in either Flybase (FB2014_03, Thurmond et al., 2019) or the RNA Binding Protein Database (Cook et al., 2011) as RNA binding or involved in RNA associated processes, using period length as a readout of clock function (Supplementary file 1: RAP Screen Dataset). We avoided many, but not all, genes with broad effects on gene expression, such as those encoding essential splicing or translation factors. When possible, we used at least two non-overlapping RNAi lines from the TRiP and VDRC collections. RNAi lines were crossed to two different GAL4 drivers: tim-GAL4 (Kaneko et al., 2000) and Pdf-GAL4 (Renn et al., 1999) each combined with a UAS-dicer-2 transgene to enhance the strength of the knockdown (Dietzl et al., 2007). These combinations will be abbreviated as TD2 and PD2, respectively. tim-GAL4 drives expression in all cells with circadian rhythms in the brain and body (Kaneko et al., 2000), while Pdf-GAL4 drives expression in a small subset of clock neurons in the brain: the PDF-positive small (s) and large (l) LNvs (Renn et al., 1999). Among them, the sLNvs are critical pacemaker neurons that drive circadian behavior in DD (Renn et al., 1999; Stoleru et al., 2005). In the initial round of screening, we tested the behavior of 4–8 males for each RNAi line crossed to both TD2 and PD2 (occasionally, fewer males were tested if a cross produced little progeny). We also crossed some RNAi lines to w1118 (+) flies (most were lines selected for retest, see below). We noticed that RNAi/+ control flies for the TRiP collection were 0.3 hr shorter than those of the VDRC collection (Figure 1A). Furthermore, the mean period from all RNAi lines crossed to either PD2 or TD2 was significantly shorter for the TRiP collection than for the VDRC collection (Figure 1A) (0.2 hr, TD2 crosses; 0.5 hr, PD2 crosses). We also found that many of the VDRC KK lines that resulted in long period phenotypes when crossed to both drivers contained insertions in the 40D locus (VDRC annotation), although this effect was stronger with PD2 than TD2. It has been shown that this landing site is in the 5’UTR of tiptop (tio) and can lead to non-specific effects in combination with some GAL4 drivers, likely due to misexpression of tio (Vissers et al., 2016; Green et al., 2014). Indeed, when we crossed a control line that contains a UAS insertion at 40D (40D-UAS) to PD2, the progeny also had a ca. 0.6 hr longer period relative to the PD2 control (Figure 1B). Thus, in order to determine a cutoff for candidates to further investigate, we analyzed the data obtained in our screen from the TRiP, VDRC, and the 40D KK VDRC lines independently (Figure 1C). These data are represented in two overlaid histograms that show period distributions: one for the TD2 crosses (blue) and one for the PD2 crosses (magenta). We chose a cutoff of two standard deviations (SD) from the mean period length for each RNAi line set. RNAi lines were selected for repeat if knockdown resulted in period lengths above or below the 2-SD cutoff. We also chose to repeat a subset of lines that did not pass the cutoff but were of interest and showed period lengthening or shortening, as well as lines that were highly arrhythmic in constant darkness (DD) or had an abnormal pattern of behavior in a light-dark cycle (LD). After a total of three independent experiments, we ended up with 43 candidates (Table 1) that passed the period length cutoffs determined by the initial screen; 31 showed a long period phenotype, while 12 had a short period. One line showed a short period phenotype with PD2 but was long with TD2 (although just below the 2-SD cutoff). Although loss of rhythmicity was also observed in many lines (Supplementary file 1), we decided to focus the present screen on period alterations to increase the probability of identifying proteins that regulate the circadian molecular pacemaker. Indeed, a change in the period length of circadian behavior is most likely caused by a defect in the molecular pacemaker of circadian neurons, while an increase in arrhythmicity can also originate from disruption of output pathways, abnormal development of the neuronal circuits underlying circadian behavioral rhythms, or cell death in the circadian neural network, for example.

![Figure 1.](https://cdn.elifesciences.org/articles/50063/elife-50063-fig1-v2.jpg)

**Figure 1.:** (A–B) Background effect of TRiP and VDRC collections on circadian period length. Circadian period length (hrs) is plotted on the y axis. RNAi collection and genotypes are labeled. Error bars represent SEM. (A) Left group (black bars): Patterned bars are the average of period lengths of a subset of RNAi lines in the screen crossed to w1118 (TRiP/+ N = 17 crosses, VDRC/+ N = 46 crosses, 40D KK VDRC/+ N = 20 crosses). Solid bar is the w1118 control (N = 20 crosses). Middle group (blue bars): Patterned bars are the average of period lengths of all RNAi lines in the screen crossed to tim-GAL4, UAS-Dicer2 (TD2) (TRiP/TD2 N = 151 crosses, VDRC/TD2 N = 340 crosses, 40D KK VDRC/TD2 N = 61 crosses). Solid bar is the TD2/+ control (N = 35 crosses). Right group (magenta bars): Patterned bars are the average of period lengths of all RNAi lines in the screen crossed to Pdf-GAL4, UAS-Dicer2 (PD2) (TRiP/PD2 N = 176 crosses, VDRC/PD2 N = 448 crosses, 40D KK VDRC/PD2 N = 69 crosses). Solid bar is the PD2/+ control (N = 36 crosses). One-way ANOVA followed by Tukey’s multiple comparison test: *p<0.05, ***p<0.001, ****p<0.0001. Note that the overall period lengthening, relative to wild-type (w1118), when RNAi lines are crossed to TD2 or PD2 is a background effect of our drivers (see main text), while the period differences between the TRiP (shorter) and VDRC (longer) collections is most likely a background effect of the RNAi lines themselves. There is also a lengthening effect of the 40D insertion site in the VDRC KK collection that cannot be explained by a background effect, as it is not present in the RNAi controls (Left panel). Instead the lengthening was only observed when these lines were crossed to our drivers. A modest effect was seen with TD2 (middle panel) and a larger effect was seen with PD2 (right panel). (B) The period lengthening effect of the VDRC 40D KK lines is likely due to overexpression of tio, as we observed lengthening when a control line that lacks a RNAi transgene, but still has a UAS insertion in the 40D (40D-UAS) locus was crossed to PD2. N = 32 flies per genotype, ****p<0.0001, Unpaired Student’s t-test. (C) Histogram of period lengths obtained in the initial round of screening. Number of lines per bin is on the y axis. Binned period length (hrs) is on the x axis. Bin size is 0.1 hr. TD2 crosses are in blue and PD2 crosses are in magenta. Dashed lines indicate our cutoff of 2 standard deviations from the mean. Number of crosses that fell above or below the cutoff is indicated. Top panel: TRiP lines. 0 lines crossed to TD2 and 2 lines crossed to PD2 gave rise to short periods and were selected for repeats. four lines crossed to TD2 and 10 lines crossed to PD2 gave rise to long periods and were selected for repeats. Middle panel: VDRC lines. eight lines crossed to TD2 and 5 lines crossed to PD2 gave rise to short periods and were selected for repeats. 12 lines crossed to TD2 and 20 lines crossed to PD2 gave rise to long periods and were selected for repeats. Bottom panel: VDRC 40D KK lines. one line crossed to TD2 and 1 line crossed to PD2 gave rise to short periods and were selected for repeats. two lines crossed to TD2 and 3 lines crossed to PD2 gave rise to long periods and were selected for repeats.

**Table 1.**
 Circadian behavior in DD of screen candidates


<table>
  <thead>
    <tr>
      <th>Gene</th>
      <th>RNAi Line</th>
      <th>Driver</th>
      <th>n</th>
      <th>% of Rhythmic Flies</th>
      <th>Period Average ±SEM</th>
      <th>Power Average ±SEM</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Atx-1</td>
      <td>GD11345</td>
      <td>TD2</td>
      <td>24</td>
      <td>75</td>
      <td>26 ± 0.1</td>
      <td>61.5 ± 4.1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>17</td>
      <td>76</td>
      <td>26.4 ± 0.1</td>
      <td>50.7 ± 5.6</td>
    </tr>
    <tr>
      <td></td>
      <td>KK108861</td>
      <td>TD2</td>
      <td>24</td>
      <td>79</td>
      <td>25.7 ± 0.1</td>
      <td>49.1 ± 4.7</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>23</td>
      <td>74</td>
      <td>26.2 ± 0.1</td>
      <td>61.8 ± 4.5</td>
    </tr>
    <tr>
      <td>barc</td>
      <td>GD9921</td>
      <td>PD2</td>
      <td>20</td>
      <td>75</td>
      <td>26.5 ± 0.2</td>
      <td>46.9 ± 5.6</td>
    </tr>
    <tr>
      <td></td>
      <td>KK101606**</td>
      <td>TD2</td>
      <td>6</td>
      <td>83</td>
      <td>25.3 ± 0.5</td>
      <td>55.4 ± 12.7</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>16</td>
      <td>75</td>
      <td>27 ± 0.4</td>
      <td>43.9 ± 5.1</td>
    </tr>
    <tr>
      <td>bsf</td>
      <td>JF01529</td>
      <td>TD2</td>
      <td>24</td>
      <td>88</td>
      <td>25.8 ± 0.1</td>
      <td>68.4 ± 4.6</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>24</td>
      <td>67</td>
      <td>25.7 ± 0.1</td>
      <td>47.6 ± 4.1</td>
    </tr>
    <tr>
      <td>CG16941</td>
      <td>GD9241</td>
      <td>PD2</td>
      <td>8</td>
      <td>0</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>HMS00157</td>
      <td>PD2</td>
      <td>24</td>
      <td>4</td>
      <td>23.4</td>
      <td>28.3</td>
    </tr>
    <tr>
      <td></td>
      <td>KK102272</td>
      <td>PD2</td>
      <td>8</td>
      <td>0</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CG32364</td>
      <td>HMS03012</td>
      <td>PD2</td>
      <td>24</td>
      <td>88</td>
      <td>25.7 ± 0.1</td>
      <td>58.9 ± 3</td>
    </tr>
    <tr>
      <td>CG42458</td>
      <td>KK106121</td>
      <td>TD2</td>
      <td>23</td>
      <td>35</td>
      <td>26.5 ± 0.2</td>
      <td>38.3 ± 4.9</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>22</td>
      <td>82</td>
      <td>26.2 ± 0.1</td>
      <td>71 ± 4.1</td>
    </tr>
    <tr>
      <td>CG4849</td>
      <td>KK101580</td>
      <td>TD2</td>
      <td>1</td>
      <td>0</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>24</td>
      <td>63</td>
      <td>27.3 ± 0.2</td>
      <td>48.8 ± 4.1</td>
    </tr>
    <tr>
      <td>CG5808</td>
      <td>KK102720*</td>
      <td>TD2</td>
      <td>23</td>
      <td>70</td>
      <td>27.4 ± 0.1</td>
      <td>45.3 ± 5.1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>24</td>
      <td>54</td>
      <td>28.5 ± 0.6</td>
      <td>34.8 ± 2.7</td>
    </tr>
    <tr>
      <td>CG6227</td>
      <td>GD11867</td>
      <td>TD2</td>
      <td>1</td>
      <td>0</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>16</td>
      <td>63</td>
      <td>26.7 ± 0.2</td>
      <td>51.4 ± 7</td>
    </tr>
    <tr>
      <td></td>
      <td>KK108174</td>
      <td>TD2</td>
      <td>4</td>
      <td>0</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>20</td>
      <td>30</td>
      <td>24.2 ± 0.4</td>
      <td>30.9 ± 3.5</td>
    </tr>
    <tr>
      <td>CG7903</td>
      <td>KK103182*</td>
      <td>TD2</td>
      <td>24</td>
      <td>8</td>
      <td>23.6</td>
      <td>26.3</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>24</td>
      <td>75</td>
      <td>26.4 ± 0.2</td>
      <td>49.1 ± 3.7</td>
    </tr>
    <tr>
      <td>CG8273</td>
      <td>GD13870</td>
      <td>TD2</td>
      <td>24</td>
      <td>83</td>
      <td>25.9 ± 0.1</td>
      <td>47.3 ± 4.6</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>14</td>
      <td>100</td>
      <td>25.4 ± 0.1</td>
      <td>51.2 ± 4.8</td>
    </tr>
    <tr>
      <td></td>
      <td>KK102147</td>
      <td>TD2</td>
      <td>24</td>
      <td>58</td>
      <td>25.5 ± 0.1</td>
      <td>41.1 ± 5</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>23</td>
      <td>100</td>
      <td>25.7 ± 0.1</td>
      <td>64.3 ± 3.9</td>
    </tr>
    <tr>
      <td>CG8636</td>
      <td>GD13992</td>
      <td>PD2</td>
      <td>12</td>
      <td>50</td>
      <td>26.9 ± 0.2</td>
      <td>36 ± 6.4</td>
    </tr>
    <tr>
      <td></td>
      <td>KK110954</td>
      <td>TD2</td>
      <td>1</td>
      <td>0</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>19</td>
      <td>63</td>
      <td>26.3 ± 0.3</td>
      <td>51.4 ± 5.6</td>
    </tr>
    <tr>
      <td>CG9609</td>
      <td>HMS01000</td>
      <td>PD2</td>
      <td>24</td>
      <td>46</td>
      <td>26.3 ± 0.2</td>
      <td>46.1 ± 6.5</td>
    </tr>
    <tr>
      <td></td>
      <td>KK109846</td>
      <td>TD2</td>
      <td>23</td>
      <td>78</td>
      <td>25.3 ± 0.1</td>
      <td>48.5 ± 4.2</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>23</td>
      <td>91</td>
      <td>26.3 ± 0.1</td>
      <td>56.4 ± 3.9</td>
    </tr>
    <tr>
      <td>Cnot4</td>
      <td>JF03203</td>
      <td>TD2</td>
      <td>23</td>
      <td>26</td>
      <td>23.7 ± 0.1</td>
      <td>39.8 ± 6</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>31</td>
      <td>77</td>
      <td>23.9 ± 0.1</td>
      <td>51.1 ± 3.2</td>
    </tr>
    <tr>
      <td></td>
      <td>KK101997</td>
      <td>TD2</td>
      <td>32</td>
      <td>47</td>
      <td>23.9 ± 0.1</td>
      <td>37.3 ± 2.9</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>27</td>
      <td>93</td>
      <td>25 ± 0.1</td>
      <td>48 ± 4.1</td>
    </tr>
    <tr>
      <td>Dcp2</td>
      <td>KK101790</td>
      <td>TD2</td>
      <td>22</td>
      <td>64</td>
      <td>26 ± 0.1</td>
      <td>49.7 ± 5.3</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>24</td>
      <td>92</td>
      <td>25.9 ± 0.1</td>
      <td>62.5 ± 4.1</td>
    </tr>
    <tr>
      <td>eIF1</td>
      <td>KK109232*</td>
      <td>PD2</td>
      <td>24</td>
      <td>4</td>
      <td>23.2</td>
      <td>68.9</td>
    </tr>
    <tr>
      <td>eIF3l</td>
      <td>KK102071</td>
      <td>TD2</td>
      <td>24</td>
      <td>21</td>
      <td>26 ± 0.2</td>
      <td>28.9 ± 2.4</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>23</td>
      <td>100</td>
      <td>25.7 ± 0.1</td>
      <td>62.5 ± 3.9</td>
    </tr>
    <tr>
      <td>Hrb98DE</td>
      <td>HMS00342</td>
      <td>PD2</td>
      <td>22</td>
      <td>91</td>
      <td>25.8 ± 0.1</td>
      <td>60.2 ± 4.1</td>
    </tr>
    <tr>
      <td>l(1)G0007</td>
      <td>GD8110</td>
      <td>PD2</td>
      <td>24</td>
      <td>63</td>
      <td>26.3 ± 0.2</td>
      <td>42.4 ± 3.7</td>
    </tr>
    <tr>
      <td></td>
      <td>KK102874</td>
      <td>TD2</td>
      <td>24</td>
      <td>17</td>
      <td>26.9 ± 0.4</td>
      <td>32.6 ± 5.5</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>23</td>
      <td>48</td>
      <td>26.7 ± 0.2</td>
      <td>48 ± 6.1</td>
    </tr>
    <tr>
      <td>LSm7</td>
      <td>GD7971</td>
      <td>PD2</td>
      <td>22</td>
      <td>36</td>
      <td>28 ± 0.4</td>
      <td>43.5 ± 5.6</td>
    </tr>
    <tr>
      <td>ncm</td>
      <td>GD7819</td>
      <td>PD2</td>
      <td>8</td>
      <td>0</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>KK100829*</td>
      <td>PD2</td>
      <td>19</td>
      <td>32</td>
      <td>23.3 ± 0.1</td>
      <td>34.4 ± 5.6</td>
    </tr>
    <tr>
      <td>Nelf-A</td>
      <td>KK101005</td>
      <td>TD2</td>
      <td>24</td>
      <td>63</td>
      <td>26.4 ± 0.1</td>
      <td>52.9 ± 4.4</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>23</td>
      <td>74</td>
      <td>24.8 ± 0.1</td>
      <td>59.4 ± 4.5</td>
    </tr>
    <tr>
      <td>Not1</td>
      <td>GD9640</td>
      <td>PD2</td>
      <td>23</td>
      <td>4</td>
      <td>22.6</td>
      <td>43.6</td>
    </tr>
    <tr>
      <td></td>
      <td>KK100090</td>
      <td>PD2</td>
      <td>10</td>
      <td>30</td>
      <td>23.8 ± 0.3</td>
      <td>39.4 ± 4.7</td>
    </tr>
    <tr>
      <td>Not3</td>
      <td>GD4068</td>
      <td>PD2</td>
      <td>8</td>
      <td>0</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>KK102144</td>
      <td>PD2</td>
      <td>21</td>
      <td>14</td>
      <td>23.6 ± 0.1</td>
      <td>30.8 ± 2.1</td>
    </tr>
    <tr>
      <td>Patr-1</td>
      <td>KK104961*</td>
      <td>TD2</td>
      <td>23</td>
      <td>30</td>
      <td>26.3 ± 0.2</td>
      <td>33.6 ± 3</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>24</td>
      <td>63</td>
      <td>27.1 ± 0.2</td>
      <td>38.3 ± 3.6</td>
    </tr>
    <tr>
      <td>Pcf11</td>
      <td>HMS00406</td>
      <td>PD2</td>
      <td>8</td>
      <td>13</td>
      <td>24</td>
      <td>20.1</td>
    </tr>
    <tr>
      <td></td>
      <td>KK100722</td>
      <td>PD2</td>
      <td>24</td>
      <td>21</td>
      <td>23.3 ± 0.1</td>
      <td>35.4 ± 5</td>
    </tr>
    <tr>
      <td>pcm</td>
      <td>GD10926</td>
      <td>TD2</td>
      <td>16</td>
      <td>63</td>
      <td>25.7 ± 0.1</td>
      <td>36.6 ± 4.1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>20</td>
      <td>55</td>
      <td>26.3 ± 0.2</td>
      <td>40.4 ± 3.8</td>
    </tr>
    <tr>
      <td></td>
      <td>KK108511</td>
      <td>TD2</td>
      <td>24</td>
      <td>21</td>
      <td>25.7 ± 0.2</td>
      <td>40.7 ± 7.8</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>24</td>
      <td>17</td>
      <td>27.7 ± 0.6</td>
      <td>32.9 ± 6.1</td>
    </tr>
    <tr>
      <td>Psi</td>
      <td>GD14067</td>
      <td>TD2</td>
      <td>48</td>
      <td>79</td>
      <td>23.7 ± 0.07</td>
      <td>49.6 ± 3.0</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>32</td>
      <td>84</td>
      <td>24.2 ± 0.1</td>
      <td>53.3 ± 4.1</td>
    </tr>
    <tr>
      <td></td>
      <td>HMS00140</td>
      <td>TD2</td>
      <td>24</td>
      <td>100</td>
      <td>24 ± 0.1</td>
      <td>61.8 ± 4.2</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>20</td>
      <td>85</td>
      <td>24.5 ± 0.1</td>
      <td>52.9 ± 5.6</td>
    </tr>
    <tr>
      <td></td>
      <td>JF01476</td>
      <td>TD2</td>
      <td>24</td>
      <td>92</td>
      <td>24 ± 0.1</td>
      <td>64.7 ± 4.9</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>24</td>
      <td>92</td>
      <td>24.3 ± 0.1</td>
      <td>53.2 ± 4</td>
    </tr>
    <tr>
      <td></td>
      <td>KK101882</td>
      <td>TD2</td>
      <td>35</td>
      <td>77</td>
      <td>23.6 ± 0.06</td>
      <td>61.9 ± 3.7</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>47</td>
      <td>89</td>
      <td>24.7 ± 0.06</td>
      <td>56.3 ± 3.4</td>
    </tr>
    <tr>
      <td>Rga</td>
      <td>GD9741</td>
      <td>TD2</td>
      <td>24</td>
      <td>21</td>
      <td>26.2 ± 0.1</td>
      <td>32.8 ± 3.2</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>22</td>
      <td>36</td>
      <td>25.4 ± 0.2</td>
      <td>36.1 ± 4.7</td>
    </tr>
    <tr>
      <td>RpS3</td>
      <td>GD4577</td>
      <td>PD2</td>
      <td>14</td>
      <td>57</td>
      <td>26.4 ± 0.2</td>
      <td>48.9 ± 5.9</td>
    </tr>
    <tr>
      <td></td>
      <td>JF01410</td>
      <td>PD2</td>
      <td>24</td>
      <td>50</td>
      <td>25.6 ± 0.2</td>
      <td>34.9 ± 2.3</td>
    </tr>
    <tr>
      <td></td>
      <td>KK109080</td>
      <td>PD2</td>
      <td>8</td>
      <td>38</td>
      <td>26 ± 1.3</td>
      <td>34.5 ± 6.3</td>
    </tr>
    <tr>
      <td>Rrp6</td>
      <td>GD12195</td>
      <td>PD2</td>
      <td>10</td>
      <td>10</td>
      <td>24.5</td>
      <td>27.2</td>
    </tr>
    <tr>
      <td></td>
      <td>KK100590</td>
      <td>PD2</td>
      <td>21</td>
      <td>10</td>
      <td>23.6</td>
      <td>43.2</td>
    </tr>
    <tr>
      <td>sbr</td>
      <td>HMS02414</td>
      <td>TD2</td>
      <td>13</td>
      <td>85</td>
      <td>26.8 ± 0.2</td>
      <td>48.7 ± 5.3</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>21</td>
      <td>100</td>
      <td>24.9 ± 0.1</td>
      <td>57.2 ± 4.6</td>
    </tr>
    <tr>
      <td>Set1</td>
      <td>GD4398</td>
      <td>TD2</td>
      <td>20</td>
      <td>90</td>
      <td>25.8 ± 0.1</td>
      <td>52.1 ± 4.2</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>13</td>
      <td>77</td>
      <td>25.3 ± 0.1</td>
      <td>42.1 ± 5.5</td>
    </tr>
    <tr>
      <td></td>
      <td>HMS01837</td>
      <td>TD2</td>
      <td>23</td>
      <td>78</td>
      <td>25.6 ± 0.1</td>
      <td>47.9 ± 3.6</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>24</td>
      <td>92</td>
      <td>24.8 ± 0.1</td>
      <td>50 ± 3.8</td>
    </tr>
    <tr>
      <td>SmB</td>
      <td>GD11620</td>
      <td>PD2</td>
      <td>13</td>
      <td>69</td>
      <td>26.2 ± 0.1</td>
      <td>52.1 ± 8</td>
    </tr>
    <tr>
      <td></td>
      <td>HM05097</td>
      <td>PD2</td>
      <td>24</td>
      <td>58</td>
      <td>25.6 ± 0.1</td>
      <td>45.2 ± 4.4</td>
    </tr>
    <tr>
      <td></td>
      <td>KK102021</td>
      <td>PD2</td>
      <td>2</td>
      <td>100</td>
      <td>25.6</td>
      <td>67.1</td>
    </tr>
    <tr>
      <td>SmE</td>
      <td>GD13663</td>
      <td>PD2</td>
      <td>24</td>
      <td>58</td>
      <td>25.7 ± 0.3</td>
      <td>37.3 ± 3.3</td>
    </tr>
    <tr>
      <td></td>
      <td>HMS00074</td>
      <td>PD2</td>
      <td>8</td>
      <td>100</td>
      <td>24.5 ± 0.1</td>
      <td>55.1 ± 7.4</td>
    </tr>
    <tr>
      <td></td>
      <td>KK101450</td>
      <td>PD2</td>
      <td>15</td>
      <td>67</td>
      <td>26.5±</td>
      <td>51.3 ± 7.8</td>
    </tr>
    <tr>
      <td>SmF</td>
      <td>JF02276</td>
      <td>PD2</td>
      <td>24</td>
      <td>75</td>
      <td>25.8 ± 0.1</td>
      <td>46.3 ± 3.9</td>
    </tr>
    <tr>
      <td></td>
      <td>KK107814</td>
      <td>PD2</td>
      <td>21</td>
      <td>57</td>
      <td>27.3 ± 0.3</td>
      <td>45.4 ± 4.2</td>
    </tr>
    <tr>
      <td>smg</td>
      <td>GD15460</td>
      <td>PD2</td>
      <td>24</td>
      <td>58</td>
      <td>26.5 ± 0.2</td>
      <td>39 ± 3.5</td>
    </tr>
    <tr>
      <td>Smg5</td>
      <td>KK102117</td>
      <td>TD2</td>
      <td>23</td>
      <td>52</td>
      <td>23.7 ± 0.1</td>
      <td>38.9 ± 3.7</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>24</td>
      <td>79</td>
      <td>23.9 ± 0.1</td>
      <td>58.5 ± 4.3</td>
    </tr>
    <tr>
      <td>Smn</td>
      <td>JF02057</td>
      <td>TD2</td>
      <td>3</td>
      <td>67</td>
      <td>24.2</td>
      <td>25.9</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>24</td>
      <td>54</td>
      <td>25.7 ± 0.1</td>
      <td>47.2 ± 3.6</td>
    </tr>
    <tr>
      <td></td>
      <td>KK106152</td>
      <td>TD2</td>
      <td>24</td>
      <td>67</td>
      <td>25.3 ± 0.1</td>
      <td>39.7 ± 3.5</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>24</td>
      <td>96</td>
      <td>26.3 ± 0.2</td>
      <td>48.7 ± 2.7</td>
    </tr>
    <tr>
      <td>snRNP-U1-C</td>
      <td>GD11660</td>
      <td>PD2</td>
      <td>11</td>
      <td>82</td>
      <td>25.7 ± 0.1</td>
      <td>56.5 ± 6.1</td>
    </tr>
    <tr>
      <td></td>
      <td>HMS00137</td>
      <td>PD2</td>
      <td>24</td>
      <td>92</td>
      <td>25.8 ± 0.1</td>
      <td>55.9 ± 4.1</td>
    </tr>
    <tr>
      <td>Spx</td>
      <td>GD11072</td>
      <td>PD2</td>
      <td>14</td>
      <td>64</td>
      <td>26.5 ± 0.2</td>
      <td>56.1 ± 7.4</td>
    </tr>
    <tr>
      <td></td>
      <td>KK108243</td>
      <td>TD2</td>
      <td>4</td>
      <td>100</td>
      <td>24 ± 0.2</td>
      <td>47.5 ± 10.2</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>19</td>
      <td>79</td>
      <td>26.9 ± 0.3</td>
      <td>56.4 ± 5</td>
    </tr>
    <tr>
      <td>Srp54k</td>
      <td>GD1542</td>
      <td>PD2</td>
      <td>5</td>
      <td>0</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>KK100462</td>
      <td>PD2</td>
      <td>24</td>
      <td>17</td>
      <td>23.7 ± 0.4</td>
      <td>31.3 ± 6</td>
    </tr>
    <tr>
      <td>Zn72D</td>
      <td>GD11579</td>
      <td>TD2</td>
      <td>28</td>
      <td>89</td>
      <td>26.3 ± 0.1</td>
      <td>46.1 ± 4.6</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>22</td>
      <td>82</td>
      <td>26.4 ± 0.1</td>
      <td>59.4 ± 6.9</td>
    </tr>
    <tr>
      <td></td>
      <td>KK100696</td>
      <td>TD2</td>
      <td>26</td>
      <td>73</td>
      <td>26.8 ± 0.1</td>
      <td>57 ± 3.6</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PD2</td>
      <td>24</td>
      <td>83</td>
      <td>26 ± 0.1</td>
      <td>57 ± 4.5</td>
    </tr>
  </tbody>
</table>

_*Line contains insertion at 40D.** Unknown if line contains insertion at 40D._

Among the 43 candidate genes (Tables 1 and 2), we noticed a high proportion of genes involved or presumed to be involved in splicing (17), including five suspected or known to impact alternative splicing. Perhaps not surprisingly, several genes involved in snRNP assembly were identified in our screen. Their downregulation caused long period phenotypes. We also noticed the presence of four members of the CCR4-NOT complex, which can potentially regulate different steps of mRNA metabolism, including deadenylation, and thus mediate translational repression. Their downregulation mostly caused short period phenotypes and tended to result in high levels of arrhythmicity. Rga downregulation, however, resulted in a long period phenotype, suggesting multiple functions for the CCR4-NOT complex in the regulation of circadian rhythms. Interestingly, two genes implicated in mRNA decapping triggered by deadenylation, were also identified, with long periods observed when these genes were downregulated. Moreover, POP2, a CCR4-NOT component, was recently shown to regulate tim mRNA and protein levels (Grima et al., 2019). Another gene isolated in our screen, SMG5, was also recently found to impact circadian behavior (Ri et al., 2019). This validates our screen.

**Table 2.**
 Predicted or known functions of screen candidates


<table>
  <thead>
    <tr>
      <th>Gene</th>
      <th>Molecular function (based on information from Flybase) (Thurmond et al., 2019)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Atx-1</td>
      <td>RNA binding</td>
    </tr>
    <tr>
      <td>barc</td>
      <td>mRNA splicing; mRNA binding; U2 snRNP binding</td>
    </tr>
    <tr>
      <td>bsf</td>
      <td>mitochondrial mRNA polyadenylation, stability, transcription, translation; polycistronic mRNA processing; mRNA 3'-UTR binding</td>
    </tr>
    <tr>
      <td>CG16941/Sf3a1</td>
      <td>alternative mRNA splicing; RNA binding</td>
    </tr>
    <tr>
      <td>CG32364/tut</td>
      <td>translation; RNA binding</td>
    </tr>
    <tr>
      <td>CG42458</td>
      <td>mRNA binding</td>
    </tr>
    <tr>
      <td>CG4849</td>
      <td>mRNA splicing; translational elongation</td>
    </tr>
    <tr>
      <td>CG5808</td>
      <td>mRNA splicing; protein peptidyl-prolyl isomerization; regulation of phosphorylation of RNA polymerase II C-terminal domain; mRNA binding</td>
    </tr>
    <tr>
      <td>CG6227</td>
      <td>alternative mRNA splicing; ATP-dependent RNA helicase activity</td>
    </tr>
    <tr>
      <td>CG7903</td>
      <td>mRNA binding</td>
    </tr>
    <tr>
      <td>CG8273/Son</td>
      <td>mRNA processing; mRNA splicing; RNA binding</td>
    </tr>
    <tr>
      <td>CG8636/eIF3g1</td>
      <td>translational initiation; mRNA binding</td>
    </tr>
    <tr>
      <td>CG9609</td>
      <td>transcription; proximal promoter sequence-specific DNA binding</td>
    </tr>
    <tr>
      <td>Cnot4</td>
      <td>CCR4-NOT complex</td>
    </tr>
    <tr>
      <td>Dcp2</td>
      <td>deadenylation-dependent decapping of mRNA; cytoplasmic mRNA P-body assembly; RNA binding</td>
    </tr>
    <tr>
      <td>eIF1</td>
      <td>ribosomal small subunit binding; RNA binding; translation initiation</td>
    </tr>
    <tr>
      <td>eIF3l</td>
      <td>translational initiation</td>
    </tr>
    <tr>
      <td>Hrb98DE</td>
      <td>translation; alternative mRNA splicing; mRNA binding</td>
    </tr>
    <tr>
      <td>l(1)G0007</td>
      <td>alternative mRNA splicing; 3'−5' RNA helicase activity</td>
    </tr>
    <tr>
      <td>LSm7</td>
      <td>mRNA splicing; mRNA catabolic process; RNA binding</td>
    </tr>
    <tr>
      <td>ncm</td>
      <td>mRNA splicing; RNA binding</td>
    </tr>
    <tr>
      <td>Nelf-A</td>
      <td>transcription elongation; RNA binding</td>
    </tr>
    <tr>
      <td>Not1</td>
      <td>translation; poly(A)-specific ribonuclease activity; CCR4-NOT complex</td>
    </tr>
    <tr>
      <td>Not3</td>
      <td>translation; transcription; poly(A)-specific ribonuclease activity; CCR4-NOT complex</td>
    </tr>
    <tr>
      <td>Patr-1</td>
      <td>cytoplasmic mRNA P-body assembly; deadenylation-dependent decapping of mRNA; RNA binding</td>
    </tr>
    <tr>
      <td>Pcf11</td>
      <td>mRNA polyadenylation; transcription termination; mRNA binding</td>
    </tr>
    <tr>
      <td>pcm</td>
      <td>cytoplasmic mRNA P-body assembly; 5'−3' exonuclease activity</td>
    </tr>
    <tr>
      <td>Psi</td>
      <td>alternative mRNA splicing; transcription; mRNA binding</td>
    </tr>
    <tr>
      <td>Rga</td>
      <td>translation; transcription; poly(A)-specific ribonuclease activity; CCR4-NOT complex</td>
    </tr>
    <tr>
      <td>RpS3</td>
      <td>DNA repair; translation; RNA binding; structural constituent of ribosome</td>
    </tr>
    <tr>
      <td>Rrp6</td>
      <td>chromosome segregation; mRNA polyadenylation; nuclear RNA surveillance; 3'−5' exonuclease activity</td>
    </tr>
    <tr>
      <td>sbr</td>
      <td>mRNA export from nucleus; mRNA polyadenylation; RNA binding</td>
    </tr>
    <tr>
      <td>Set1</td>
      <td>histone methyltransferase activity; nucleic acid binding; contains an RNA Recognition Motif</td>
    </tr>
    <tr>
      <td>SmB</td>
      <td>mRNA splicing; RNA binding</td>
    </tr>
    <tr>
      <td>SmE</td>
      <td>mRNA splicing; spliceosomal snRNP assembly</td>
    </tr>
    <tr>
      <td>SmF</td>
      <td>mRNA splicing; spliceosomal snRNP assembly; RNA binding</td>
    </tr>
    <tr>
      <td>smg</td>
      <td>RNA localization; translation; mRNA poly(A) tail shortening; transcription; mRNA binding</td>
    </tr>
    <tr>
      <td>Smg5</td>
      <td>nonsense-mediated decay; ribonuclease activity</td>
    </tr>
    <tr>
      <td>Smn</td>
      <td>spliceosomal snRNP assembly; RNA binding</td>
    </tr>
    <tr>
      <td>snRNP-U1-C</td>
      <td>mRNA 5'-splice site recognition; mRNA splicing, alternative mRNA splicing</td>
    </tr>
    <tr>
      <td>Spx</td>
      <td>mRNA splicing; mRNA binding</td>
    </tr>
    <tr>
      <td>Srp54k</td>
      <td>SRP-dependent cotranslational protein targeting to membrane; 7S RNA binding</td>
    </tr>
    <tr>
      <td>Zn72D</td>
      <td>mRNA splicing; RNA binding</td>
    </tr>
  </tbody>
</table>

### Knockdown of Psi shortens the period of behavioral rhythms

A promising candidate to emerge from our screen was the alternative splicing regulator PSI (Labourier et al., 2001; Siebel et al., 1992). Knockdown of Psi with both TD2 and PD2 crossed to two non-overlapping RNAi lines from the VDRC collection (GD14067 and KK101882) caused a significant period shortening, compared to the TD2/+ and PD2/+ controls (Figure 2A–E, Table 3), which the experimental flies need to be compared to since the GAL4 drivers in the TD2 and PD2 combination cause a previously reported dominant ca. 0.8 hr period lengthening (Figure 2C, left panel (TD2/+ compared to w1118); Kaneko et al., 2000; Renn et al., 1999; Zhang and Emery, 2013; Zhang et al., 2013). Importantly, the RNAi lines did not cause period shortening on their own (Figure 2C left panel, Table 3). While most experiments were performed at 25°C, we noticed that at 30°C, TD2/+ control had a period of ca. 24 hr (Figure 2C). We could thus meaningfully compare TD2/RNAi flies to both RNAi/+ and TD2/+ control at that temperature. The period of the experimental flies was significantly shorter than both controls (Figure 2C). Two additional lines from the TRiP collection (JF01476 and HMS00140) also caused period shortening when crossed to TD2 (Table 1). Interestingly, HMS00140 targets only the Psi-RA isoform, indicating that the RA isoform is important for the control of circadian period (Figure 2A). Since four RNA lines caused a similar phenotype and only two of them partially overlapped (Figure 2A), we are confident that the period shortening was not caused by off-target effects. Moreover, both the KK101882 and GD14067 lines have been shown to efficiently downregulate Psi (Guo et al., 2016), and we confirmed by quantitative Real-Time PCR (qPCR) that the RNAi line KK101882, which gave the shortest period phenotype with TD2, significantly reduced Psi mRNA levels in heads (Figure 2—figure supplement 1). This line was selected for most of the experiments described below as it gave the strongest period phenotype.

![Figure 2.](https://cdn.elifesciences.org/articles/50063/elife-50063-fig2-v2.jpg)

**Figure 2.:** (A) Schematic of Psi isoforms and position of the long and short hairpins used in this study. Adapted from Ensembl 94 (Zerbino et al., 2018). (B–E) Knockdown of Psi shortens the behavioral period. (B) Double-plotted actograms showing the average activities during 3 days in LD and 5 days in DD. Left panel: TD2/+ (control) flies. Right panel: TD2/PsiRNAi (Psi knockdown) flies. Note the short period of Psi knockdown flies. n = 8 flies/genotype. (C–E) Circadian period length (hrs) is plotted on the y axis. Genotypes are listed on the x axis. Error bars represent SEM. Solid black bar is w1118 (WT) control; solid blue, magenta and gray bars are driver controls; patterned bars are Psi knockdown with two non-overlapping RNAi lines: GD14067 (PsiRNAiGD) and KK101882 (PsiRNAiKK). *p<0.05, ***p<0.001, ****p<0.0001, one-way ANOVA followed by Tukey’s multiple comparison test (C) Dunnett’s multiple comparison test (D and E). (C) Knockdown in all circadian tissues. Left panel 25°C, right panel 30°C. Note that even at 25°C, the experimental flies are shorter than their respective RNAi/+ control, despite the dominant period lengthening caused by TD2 (D) Knockdown in PDF+ circadian pacemaker neurons. (E) Knockdown in PDF- circadian tissues. In D and E, only the driver controls are shown, since they are the controls which the experimental flies need to be compared to because of the dominant period lengthening caused by PD2 and TD2. (F–H) Overexpression of Psi lengthens the behavioral period and decreases rhythmicity. Left panels: Circadian period length (hrs) is plotted on the y axis. Error bars represent SEM. Right panels: Percent of flies that remained rhythmic in DD is plotted on the y axis. Both panels: Genotypes are listed on the x axis. Not significant (ns)p>0.05, *p<0.05, ****p<0.0001, one-way ANOVA followed by Tukey’s multiple comparison test. (F) Overexpression of Psi in all circadian tissues lengthened the circadian period and decreased the percent of rhythmic flies. (G) Overexpression of Psi in PDF+ circadian pacemaker neurons caused a slight but non-significant period lengthening compared to the driver control (PG4/+), which is the relevant comparison because of the dominant period lengthening caused by PG4. Rhythmicity was slightly reduced compared to PG4/+ but not compared to UAS-Psi/+. (H) Overexpression of Psi in PDF- circadian tissues lengthened the circadian period and decreased rhythmicity.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/50063/elife-50063-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Psi mRNA expression does not cycle in DD. Relative expression of Psi mRNA (normalized to the average of all Psi knockdown time points) in heads on the y axis measured by qPCR. Circadian time (CT) on the x axis. Error bars represent SEM. Gray line: driver control. Black line: RNAi control. Dashed line: Psi knockdown. Controls, N = 3. Psi knockdown, N = 5. Both driver and RNAi control relative to Psi knockdown, two-way ANOVA followed by Tukey’s multiple comparison test: *p<0.05. (B) Knockdown of Psi with RNAiKK causes a significant reduction in Psi mRNA levels relative to both driver and RNAi controls. Since no cycling of Psi was observed, all time points were pooled to increase statistical strength. Relative expression of Psi mRNA (normalized to the average of all Psi knockdown time points) in heads on the y axis measured by qPCR. Genotypes are on the x axis. Error bars represent SEM. Gray bar: driver control. Black bar: RNAi control. Patterned bar: Psi knockdown. Both driver and RNAi control relative to Psi knockdown, one-way ANOVA followed by Tukey’s multiple comparison test: ****p<0.0001.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/50063/elife-50063-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) Period length (hrs) of light output generated from luciferase rhythms of ptim-TIM-LUC in whole flies. 9–24 wells/run (with one exception for control genotype PsiRNAiKK/+; ptimTIMLUC/+), three flies/well. N = 6 runs. *p<0.05, ***p<0.001, one-way ANOVA followed by Tukey’s multiple comparison test. Error bars represent SEM. Gray bar: driver control. Black bar: RNAi control. Blue patterned bar: Psi knockdown. (B) Representative traces from (A) Markers are raw data and lines are 6 hr moving averages. Gray marker (triangle) and gray line: driver control. Black marker (circle) and black line: RNAi control. Blue marker (diamond) and blue dashed line: Psi knockdown. Luciferase signal (arbitrary units, AU) on the y axis and time (hrs) from start of experiment on the x axis. 72 hr = start of DD. (C) Period length (hrs) of average light output generated from luciferase rhythms of BG-LUC in whole flies. 12–30 wells/run, three flies/well. N = 4 runs. Error bars represent SEM. Gray bar: driver control. Black bar: RNAi control. Blue patterned bar: Psi knockdown. (D) Representative traces from (C) Markers are raw data and lines are 6 hr moving averages. Gray marker (triangle) and gray line: driver control. Black marker (circle) and black line: RNAi control. Blue marker (diamond) and blue dashed line: Psi knockdown. Luciferase signal (arbitrary units, AU) on the y axis and time (hrs) from start of experiment on the x axis. 72 hr = start of DD.

**Table 3.**
 PSI affects circadian behavior


<table>
  <thead>
    <tr>
      <th>Genotype</th>
      <th>Period ±SEM</th>
      <th>Power ±SEM</th>
      <th>n</th>
      <th>% of Rhythmic Flies</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="5">Psi downregulation and overexpression at 25°C</td>
    </tr>
    <tr>
      <td>TD2/+</td>
      <td>24.8 ± 0.04</td>
      <td>48.2 ± 2.3</td>
      <td>71</td>
      <td>82</td>
    </tr>
    <tr>
      <td>TD2/PsiRNAiGD</td>
      <td>23.7 ± 0.07</td>
      <td>49.6 ± 3.0</td>
      <td>48</td>
      <td>79</td>
    </tr>
    <tr>
      <td>TD2/PsiRNAiKK</td>
      <td>23.6 ± 0.06</td>
      <td>61.9 ± 3.7</td>
      <td>35</td>
      <td>77</td>
    </tr>
    <tr>
      <td>PD2/+</td>
      <td>24.9 ± 0.04</td>
      <td>50.4 ± 2.1</td>
      <td>77</td>
      <td>83</td>
    </tr>
    <tr>
      <td>PD2/PsiRNAiGD</td>
      <td>24.2 ± 0.06</td>
      <td>53.3 ± 4.1</td>
      <td>32</td>
      <td>84</td>
    </tr>
    <tr>
      <td>PD2/PsiRNAiKK</td>
      <td>24.7 ± 0.06</td>
      <td>56.3 ± 3.4</td>
      <td>47</td>
      <td>89</td>
    </tr>
    <tr>
      <td>TD2/+; PdfGAL80/+</td>
      <td>24.5 ± 0.07</td>
      <td>49.4 ± 2.8</td>
      <td>40</td>
      <td>75</td>
    </tr>
    <tr>
      <td>TD2/PsiRNAiGD; PdfGAL80/+</td>
      <td>23.8 ± 0.17</td>
      <td>45.8 ± 5.5</td>
      <td>24</td>
      <td>50</td>
    </tr>
    <tr>
      <td>TD2/PsiRNAiKK; PdfGAL80/+</td>
      <td>24.0 ± 0.05</td>
      <td>71.9 ± 4.0</td>
      <td>39</td>
      <td>95</td>
    </tr>
    <tr>
      <td>w1118</td>
      <td>24.1 ± 0.03</td>
      <td>84.8 ± 2.5</td>
      <td>70</td>
      <td>99</td>
    </tr>
    <tr>
      <td>PsiRNAiGD/+</td>
      <td>24.2 ± 0.04</td>
      <td>58.9 ± 2.9</td>
      <td>63</td>
      <td>94</td>
    </tr>
    <tr>
      <td>PsiRNAiKK/+</td>
      <td>24.0 ± 0.04</td>
      <td>67.1 ± 3.7</td>
      <td>55</td>
      <td>96</td>
    </tr>
    <tr>
      <td>TG4/+</td>
      <td>25.2 ± 0.05</td>
      <td>52.5 ± 2.2</td>
      <td>68</td>
      <td>88</td>
    </tr>
    <tr>
      <td>TG4/+; UAS-Psi/+</td>
      <td>25.9 ± 0.07</td>
      <td>31.3 ± 1.2</td>
      <td>302</td>
      <td>16</td>
    </tr>
    <tr>
      <td>PG4/+</td>
      <td>25.0 ± 0.05</td>
      <td>66.0 ± 3.5</td>
      <td>26</td>
      <td>96</td>
    </tr>
    <tr>
      <td>PG4/+; UAS-Psi/+</td>
      <td>25.2 ± 0.07</td>
      <td>44.0 ± 2.7</td>
      <td>48</td>
      <td>77</td>
    </tr>
    <tr>
      <td>TG4/+; PdfGAL80/+</td>
      <td>24.6 ± 0.06</td>
      <td>42.8 ± 2.8</td>
      <td>37</td>
      <td>84</td>
    </tr>
    <tr>
      <td>TG4/+; PdfGAL80/UAS-Psi</td>
      <td>24.9 ± 0.19</td>
      <td>31.3 ± 2.8</td>
      <td>116</td>
      <td>11</td>
    </tr>
    <tr>
      <td>UAS-Psi/+</td>
      <td>24.2 ± 0.04</td>
      <td>46.4 ± 1.8</td>
      <td>80</td>
      <td>79</td>
    </tr>
    <tr>
      <td colspan="5">Psi downregulation at 20°C</td>
    </tr>
    <tr>
      <td>TD2/+</td>
      <td>24.9 ± 0.10</td>
      <td>42.0 ± 3.1</td>
      <td>39</td>
      <td>59</td>
    </tr>
    <tr>
      <td>TD2/PsiRNAiGD</td>
      <td>23.6 ± 0.07</td>
      <td>52.2 ± 4.7</td>
      <td>44</td>
      <td>66</td>
    </tr>
    <tr>
      <td>TD2/PsiRNAiKK</td>
      <td>23.7 ± 0.08</td>
      <td>43.8 ± 5.5</td>
      <td>44</td>
      <td>36</td>
    </tr>
    <tr>
      <td>PsiRNAiGD/+</td>
      <td>24.0 ± 0.09</td>
      <td>46.0 ± 3.7</td>
      <td>32</td>
      <td>72</td>
    </tr>
    <tr>
      <td>PsiRNAiKK/+</td>
      <td>23.8 ± 0.08</td>
      <td>39.1 ± 4.9</td>
      <td>32</td>
      <td>38</td>
    </tr>
    <tr>
      <td colspan="5">Psi downregulation at 30°C</td>
    </tr>
    <tr>
      <td>TD2/+</td>
      <td>23.7 ± 0.07</td>
      <td>48.2 ± 2.9</td>
      <td>39</td>
      <td>87</td>
    </tr>
    <tr>
      <td>TD2/PsiRNAiGD</td>
      <td>23.1 ± 0.13</td>
      <td>38.3 ± 3.8</td>
      <td>42</td>
      <td>40</td>
    </tr>
    <tr>
      <td>TD2/PsiRNAiKK</td>
      <td>22.8 ± 0.15</td>
      <td>43.1 ± 4.2</td>
      <td>41</td>
      <td>41</td>
    </tr>
    <tr>
      <td>PsiRNAiGD/+</td>
      <td>23.6 ± 0.04</td>
      <td>43.2 ± 3.4</td>
      <td>32</td>
      <td>75</td>
    </tr>
    <tr>
      <td>PsiRNAiKK/+</td>
      <td>23.5 ± 0.03</td>
      <td>63.0 ± 3.7</td>
      <td>31</td>
      <td>90</td>
    </tr>
    <tr>
      <td colspan="5">TIM-HA suppression of PSI's effect on circadian behavior</td>
    </tr>
    <tr>
      <td>TG4/PsiRNAiKK; UAS-Dcr2/+</td>
      <td>23.4 ± 0.04</td>
      <td>59.5 ± 4.3</td>
      <td>57</td>
      <td>75</td>
    </tr>
    <tr>
      <td>TG4/+; UAS-Dcr2/+</td>
      <td>24.9 ± 0.04</td>
      <td>59.4 ± 3.1</td>
      <td>36</td>
      <td>92</td>
    </tr>
    <tr>
      <td>tim0,TG4/tim0; UAS-Dcr2/timHA</td>
      <td>24.9 ± 0.07</td>
      <td>44.3 ± 4.0</td>
      <td>28</td>
      <td>75</td>
    </tr>
    <tr>
      <td>tim0,TG4/tim0,PsiRNAiKK; UAS-Dcr2/timHA</td>
      <td>24.8 ± 0.06</td>
      <td>50.0 ± 2.9</td>
      <td>38</td>
      <td>79</td>
    </tr>
  </tbody>
</table>

The phenotype caused by Psi downregulation was more pronounced with TD2 than with PD2 (Figure 2C–D, Table 3). This was unexpected since the sLNvs - targeted quite specifically by PD2 - determine circadian behavior period in DD (Stoleru et al., 2005; Renn et al., 1999). This could happen if PD2 is less efficient at downregulating Psi in sLNvs than TD2, or if the short period phenotype is not solely caused by downregulation of Psi in the sLNvs. To distinguish between these two possibilities, we used Pdf-GAL80 combined with TD2 to inhibit GAL4 activity specifically in the LNvs (Stoleru et al., 2004), while allowing RNAi expression in all other circadian tissues. With this combination, we also observed a significant period shortening compared to TD2/+; Pdf-GAL80/+ controls, but the period shortening was not as pronounced as with TD2 (Figure 2E, Table 3). We therefore conclude that both the sLNvs and non-PDF cells contribute to the short period phenotype caused by Psi downregulation (see discussion).

### Psi overexpression disrupts circadian behavior

Since we observed that downregulating Psi leads to a short period, we wondered whether overexpression would have an inverse effect and lengthen the period of circadian behavior. Indeed, when we overexpressed Psi by driving a UAS-Psi transgene (Labourier et al., 2001) with the tim-GAL4 (TG4) driver, the period length of circadian behavior increased significantly by about 0.7 hr compared to the TG4/+ control (Figure 2F, Table 3). Interestingly, we also observed a severe decrease in the number of rhythmic flies. When we overexpressed Psi with Pdf-GAL4 (PG4), period was not statistically different from control (PG4/+), and rhythmicity was not reduced compared to the UAS-Psi/+ control (Figure 2G). Overexpression of Psi with the tim-GAL4; Pdf-GAL80 combination caused a severe decrease in rhythmicity but caused only a subtle period lengthening compared to TG4/+; Pdf-GAL80/+ controls (Figure 2H, Table 3). The effect of Psi overexpression on period is in line with the knockdown results, indicating that PSI regulates circadian behavioral period through both PDF+ LNvs and non-PDF circadian neurons. However, the increase in arrhythmicity observed with Psi overexpression is primarily caused by non-PDF cells.

### Psi downregulation also shortens the period of body clocks

We wanted to further examine the effect of Psi knockdown on the molecular rhythms of two core clock genes: period (per) and timeless (tim). To do this, we took advantage of two luciferase reporter transgenes. We downregulated Psi with the TD2 driver in flies expressing either a TIM-LUCIFERASE (ptim-TIM-LUC) or a PER-LUCIFERASE (BG-LUC) fusion protein under the control of the tim or per promoter, respectively. We estimated period of luciferase activity rhythms over the first two days in DD, because oscillations rapidly dampened. Fully consistent with our behavioral results, the period of LUC activity was significantly shortened by about 1–1.5 hr compared to controls when Psi was downregulated in ptim-TIM-LUC flies (Figure 2—figure supplement 2A and B). Knockdown of Psi in BG-LUC flies resulted in a similar trend, although differences did not reach statistical significance (Figure 2—figure supplement 2C and D). Period was however shorter in experimental flies compared to both control genotypes in all four independent experiments performed with BG-LUC (and all six with ptim-TIM-LUC). Since the luciferase signal in these flies is dominated by light from the abdomen (Lamba et al., 2018; Stanewsky et al., 1997), this indicates that Psi knockdown, shortens the period of circadian clocks in peripheral tissues as well as in the brain neural network that controls circadian behavior.

### Alternative splicing of two clock genes, cwo and tim, is altered in Psi knockdown flies

PSI has been best characterized for its role in alternative splicing of the P element transposase gene in somatic cells (Labourier et al., 2001; Siebel et al., 1992). However, it was recently reported that PSI has a wider role in alternative splicing (Wang et al., 2016). Wang et al. reported an RNA-seq dataset of alternative splicing changes that occur when a lethal Psi-null allele is rescued with a copy of Psi in which the AB domain has been deleted (PSIΔAB). This domain is required for the interaction of PSI with the U1 snRNP, which is necessary for PSI to mediate alternative splicing of P element transposase (Labourier et al., 2002). Interestingly, Wang et al. (2016) found that PSIΔAB affects alternative splicing of genes involved in complex behaviors such as learning, memory and courtship. Intriguingly, we found four core clock genes listed in this dataset: tim, cwo, sgg and Pdp1. We decided to focus on cwo and tim, since only one specific splicing isoform of Pdp1 is involved in the regulation circadian rhythm, (Pdp1e) (Zheng et al., 2009), and since the sgg gene produces a very complex set of alternative transcripts. After three days of LD entrainment, we collected RNA samples at four time points on the first day of DD and determined the relative expression of multiple isoforms of cwo and tim in Psi knockdown heads compared to driver and RNAi controls.

CWO is a basic helix-loop-helix (bHLH) transcriptional factor and is part of an interlocked feedback loop that reinforces the main loop by competing with CLK/CYC for E-box binding (Matsumoto et al., 2007; Lim et al., 2007; Kadener et al., 2007; Richier et al., 2008). There are three mRNA isoforms of cwo predicted in Flybase (Figure 3—figure supplement 1A) (Thurmond et al., 2019). Of the three, only cwo-RA encodes a full-length CWO protein. Exon two is skipped in cwo-RB, and in cwo-RC there is an alternative 3’ splice site in the first intron that lengthens exon 2. Translation begins from a downstream start codon in cwo-RB and -RC, because exon two skipping or lengthening, respectively, causes a frameshift after the start codon used in cwo-RA. The predicted start codon in both cwo-RB and cwo-RC would produce an N-terminal truncation of the protein, which would thus be missing the basic region of the bHLH domain and should not be able to bind DNA. The cwo-RB and cwo-RC isoforms may therefore encode endogenous dominant negatives.

We found that the level of the cwo-RB isoform was significantly reduced compared to both controls at CT 9 (Figure 3—figure supplement 1C). The cwo-RA isoform was also reduced compared to both controls at CT9 (Figure 3—figure supplement 1B). This reduction was significant compared to the TD2/+ control (p=0.0002) but was just above the significance threshold compared to the PsiRNAiKK/+ control (p=0.0715). Conversely, cwo-RC isoform expression was significantly increased at CT 15 (Figure 3—figure supplement 1D). The overall expression of all cwo mRNAs in Psi knockdown fly heads was significantly reduced at both CT 9 and CT 15, indicating that the RC isoform’s contribution to total cwo mRNA levels is quite modest (Figure 3—figure supplement 1E).

We then analyzed alternative splicing of tim in Psi knockdown heads compared to controls. Specifically, we looked at the expression of three temperature-sensitive intron inclusion events in tim that all theoretically lead to C-terminal truncations of the protein (Figure 3A). The tim-cold isoform, which is not annotated in Flybase (Thurmond et al., 2019), is dominant at low temperature (18°C) and arises when the last intron is retained (Boothroyd et al., 2007). We found that tim-cold is elevated in Psi knockdown heads at peak levels under 25°C conditions (CT15, Figure 3D). Similarly, we found that another intron inclusion event, tim-sc (tim-short and cold) which has also been shown to be elevated at 18°C and is present in the tim-RN and -RO isoforms (Martin Anduaga et al., 2019), is significantly increased at 25°C in Psi knockdown heads at CT15 (Figure 3B). Thus, interestingly, two intron inclusion events that are upregulated by cold temperature are also both upregulated in Psi knockdown heads at 25°C. In contrast, we found that an intron included in the tim-RM and -RS isoforms (tim-M, for tim-Medium) and shown to be increased at high temperature (29°C, Martin Anduaga et al., 2019; Shakhmantsir et al., 2018) is significantly decreased at CT 9, 15 and 21 in Psi knockdown heads at 25°C (Figure 3F). In the case of tim-sc, it should be noted that the intron is only partially retained, because a cleavage and poly-adenylation signal is located within this intron, thus resulting in a much shorter mature transcript (Martin Anduaga et al., 2019). Based on PSI function, the most parsimonious explanation is that PSI reduces production of tim-sc by promoting splicing of the relevant intron. However, we cannot entirely exclude that PSI regulates the probability of premature cleavage causing the RNA polymerase to undergo transcription termination soon after passing the poly-adenylation signal.

![Figure 3.](https://cdn.elifesciences.org/articles/50063/elife-50063-fig3-v2.jpg)

**Figure 3.:** (A) Schematic of tim isoforms. Flybase transcript nomenclature on left, intron retention events studied here on right (tim-L refers to tim transcripts that do not produce C-terminal truncations of TIM via intron retention). Arrows indicate the location of retained introns: blue, upregulated at cold temperature; red, upregulated at warm temperature. The retained intron that gives rise to the tim-cold isoform is not annotated in Flybase (Thurmond et al., 2019). It is possible that multiple tim-cold transcripts may exist due to alternative splicing and alternative transcription/translation start sites in the 5’ region of the gene (dashed box). However, for simplicity, we depict this region of tim-cold using the most common exons. Adapted from Ensembl 94 (Zerbino et al., 2018). (B, D, F) Relative expression of tim mRNA isoforms at 25°C (normalized to the average of all Psi knockdown time points) in heads on the y axis measured by qPCR. Circadian time (CT) on the x axis. Error bars represent SEM. Gray line: driver control. Black line: RNAi control. Dashed line: Psi knockdown. Controls, N = 3. Psi knockdown, N = 5 (3 technical replicates per sample). Both driver and RNAi control compared to Psi knockdown, two-way ANOVA followed by Tukey’s multiple comparison test: *p<0.05, **p<0.01, ***p<0.001, ****p<0.0001. (C, E, G) Relative expression of tim mRNA isoforms at 18°C and 29°C (normalized to the average of all Psi knockdown time points). Solid line: RNAi control. Dashed line: Psi RNAi knockdown. Blue indicates flies were transferred to 18°C at CT0 (start of subjective day) on the first day of DD. Red indicates flies were transferred to 29°C. N = 3 (3 technical replicates per sample). 18°C samples compared to 29°C samples, *p<0.05, **p<0.01, ***p<0.001, ****p<0.0001, two-way ANOVA followed by Tukey’s multiple comparison test. (C) Blue asterisks refer to RNAi control compared to Psi knockdown.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/50063/elife-50063-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Schematic of cwo isoforms. Adapted from Ensembl 94 (Zerbino et al., 2018). (B–D) Relative expression of cwo mRNA isoforms (normalized to the average of all Psi knockdown time points) in heads on the y axis measured by qPCR. (E) Relative expression of total cwo mRNA on the y axis. (B–E) Circadian time (CT) on the x axis. Error bars represent SEM. Gray line: driver control. Black line: RNAi control. Dashed line: Psi knockdown. Driver control, N = 3. RNAi control, N = 4. Psi knockdown, N = 6 (3 technical replicates per sample). Both driver and RNAi control compared to Psi knockdown, two-way ANOVA followed by Tukey’s multiple comparison test: *p<0.05, **p<0.01.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/50063/elife-50063-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A) Eductions showing the average activity of flies during 3 days of LD (days 2–4). Left panels: flies were entrained at 20°C. Center panels: flies were entrained at 25°C. Right panels: flies were entrained at 30°C. Top panels: TD2/PsiRNAiKK (Psi knockdown) flies. Middle panels: TD2/PsiRNAiGD (Psi knockdown) flies. Bottom panels: TD2/+ (control) flies. Note that, similar to the TD2/+ control, Psi knockdown flies advance the phase of their evening activity at 20°C and delay the phase of their evening activity at 30°C. Psi knockdown flies also show reduced morning activity and increased evening activity at 20°C, and increased morning activity and decreased evening activity at 30°C, similar to the TD2/+ control. (B) Quantification of the morning and evening anticipation phase score indicates that the phase of behavior in LD (day 2–3) is not affected by knockdown of Psi. Genotypes are on the x axis. Error bars represent SEM. Gray bar: driver control. Patterned bars: Psi knockdown. One-way ANOVA followed by Tukey’s multiple comparison test: p>0.05 for all comparisons. N = 3–5 runs (6–16 flies per genotype in each run).

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/50063/elife-50063-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** Behavioral phase response curve to brief 5 min 1500 lux light pulses. Behavioral phase shifts are on the y-axis. The time of the light pulse administration is on the x-axis. N = 4 for all time points except ZT23 where N = 3. For each genotype, 16 flies per timepoint were tested in each run. No significant effect of genotype was detected, two-way ANOVA. Note that the phase of the Psi knockdown curve is slightly shifted to the left, which probably reflects the short period of Psi knockdown flies.

Collectively, these results indicate that, in wild-type flies, PSI shifts the balance of tim alternative splicing events toward a warm temperature tim RNA isoform profile at an intermediate temperature (25°C). This could be achieved either by altering the temperature sensitivity of tim introns, or by promoting a ‘warm temperature splicing pattern’ independently of temperature. We therefore also measured tim splicing isoforms at 18°C and 29°C (Figure 3C,E,G). We entrained flies for 3 days in LD at 25°C to maintain similar levels of GAL4 expression and thus of Psi knockdown (the GAL4/UAS system’s activity increases with temperature, Duffy, 2002). We then shifted them to either 18°C or 29°C at CT 0 on the first day of DD and collected samples at CT 3, 9, 15 and 21. We found that both the tim-cold intron and the tim-sc introns were elevated at 18°C in both Psi knockdown heads and controls (Figure 3C and E). Thus, Psi knockdown does not block the temperature sensitivity of these introns. tim-M levels were unexpectedly variable in DD, particularly in the Psi knockdown flies, perhaps because of the temperature change. Nevertheless, we observed a trend for the tim-M intron retention to be elevated at 29°C (Figure 3G), further supporting our conclusion that Psi knockdown does not affect the temperature sensitivity of tim splicing, but rather determines the ratio of tim mRNA isoforms, and it does this at all temperatures.

As expected from these results, Psi downregulation did not affect the ability of flies to adjust the phase of their evening and morning peak to changes in temperature (Figure 3—figure supplement 2). We also tested whether Psi knockdown flies responded normally to short light pulses, since TIM is the target of the circadian photoreceptor CRY (Emery et al., 1998; Stanewsky et al., 1998; Lin et al., 2001; Busza et al., 2004; Koh et al., 2006). These flies could both delay or advance the phase of their circadian behavior in response to early or late-night light pulses, respectively (Figure 3—figure supplement 3). We noticed however a possible slight shift of the whole Phase Response Curve toward earlier times. This would be expected since the pace of the circadian clock is accelerated.

### PSI controls the phase of circadian behavior under temperature cycle

Since PSI regulates thermosensitive tim splicing events, we wondered whether it might have an impact on circadian behavioral responses to temperature. As mentioned above, Psi downregulation does not affect Drosophila’s ability to adjust the phase of their behavior to different constant ambient temperatures, under a LD cycle (Figure 3—figure supplement 2). Psi knockdown did not appear to affect temperature compensation, as these flies essentially responded to temperature in a similar way as their TD2/+ control, with shorter period at 29°C (Figure 4—figure supplement 1). However, we found a striking phenotype in flies with Psi downregulation under temperature cycle (29/20°C). Once flies had reached a stable phase relationship with the entraining temperature cycle (Busza et al., 2007), the phase of the evening peak of activity was advanced by about 2.5 hr in TD2/PsiRNAi, compared to controls, and this with two non-overlapping dsRNAs (Figure 4). Controls included TD2/+ or TD2/VIE-260B (KK host strain), RNAi/+, as well as TD2 crossed to a KK or GD RNAi line that did not produce a circadian phenotype. Importantly, no such phase advance was observed under LD (Figure 3—figure supplement 2), indicating that the short period phenotype does not account for the evening-peak advanced phase under temperature cycle. Rather, the phase advance is specific to temperature entrainment. The morning peak was difficult to quantify as it tended to be of low amplitude.

![Figure 4.](https://cdn.elifesciences.org/articles/50063/elife-50063-fig4-v2.jpg)

**Figure 4.:** (A) Eductions showing the average activity of flies during 4 days of 12:12 29°C(red)/20°C(blue) temperature entrainment (days 7–10) in DD. Top panels: (driver controls) TD2/+ (left), TD2/VIE-260B (right). Middle panels: (RNAi controls) PsiRNAiGD/+ (left), PsiRNAiKK/+ (right). Bottom panels: (Psi knockdown) TD2/PsiRNAiGD (left), TD2/PsiRNAiKK (right). Note that, Psi knockdown flies advance the phase of their evening activity by about 2.5 hr relative to controls. (C–D) Evening peak phase relative to an internal control in each run (w1118) (hrs) is plotted on the y axis. Genotypes are listed on the x axis. Error bars represent SEM. ***p<0.001, ****p<0.0001, one-way ANOVA followed by Tukey’s multiple comparison test. N = 3–5 runs (C) Quantification of PsiRNAiGD knockdown and controls. Note additional RNAi controls: larpRNAiGD/+ (black bar, gray border) and TD2/larpRNAiGD (patterned bar, gray border). larpRNAiGD (GD8214) is an RNAi line from the GD collection that targets a RAP from our screen that was not a hit. (D) Quantification of PsiRNAiKK knockdown and controls. Note additional RNAi controls: VIE260B/+ (white bar, black border), TD2/VIE260B (gray bar), Rbp9RNAiKK/+ (black bar, gray border) and TD2/Rbp9RNAiKK (patterned bar, gray border). VIE260B is a KK collection host strain control containing the 30B transgene insertion site. Rbp9RNAiKK (KK109093) is an RNAi line from the KK collection targeting a RAP from our screen that was not a hit.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/50063/elife-50063-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Circadian period length (hrs) is plotted on the y axis. The temperature at which the experiment was conducted is listed on the x axis. Error bars represent SEM. Gray line and triangle marker is the driver control. Black lines and circle markers are the RNAi controls (top, PsiRNAiGD/+; bottom, PsiRNAiKK/+). Dashed lines and diamond markers are Psi knockdown (top, PsiRNAiGD/TD2; bottom, PsiRNAiKK/TD2). **p<0.01, ****p<0.0001 two-way ANOVA followed by Tukey’s multiple comparison test.

### tim splicing is required for PSI’s regulation of circadian period and circadian behavior phase under temperature cycle

Because tim is a key element of the circadian transcriptional feedback loop and its splicing pattern is determined by the ambient temperature, we wondered whether PSI might be regulating the speed of the clock and the phase of the evening peak through its effects on tim splicing. We therefore rescued the amorphic tim allele (tim0) with a tim transgene that lacks the known temperature sensitive alternatively spliced introns as well as most other introns (timHA) (Figure 5A) (Rutila et al., 1998). Importantly, the tim0 mutation is a frame-shifting deletion located upstream of the temperature-sensitive alternative splicing events (Myers et al., 1995), and would thus truncate any TIM protein produced from the splice variants we studied. Strikingly, we found that knockdown of Psi in timHA rescued tim0 flies had no impact on the period of circadian behavior (Figure 5B–C, Table 3). Likewise, the evening peak phase under temperature cycles was essentially insensitive to Psi knockdown in timHA rescued tim0 flies (Figure 5D–E). This indicates that PSI controls circadian period in DD and the phase of the evening peak under temperature cycle through tim splicing.

![Figure 5.](https://cdn.elifesciences.org/articles/50063/elife-50063-fig5-v2.jpg)

**Figure 5.:** (A) Schematic of timHA transgene. The tim promoter is fused upstream of the transcription start site (TSS). Two introns remain in the 5’UTR, upstream of the start codon; however, they are not, to our knowledge, temperature sensitive. A C-terminal HA tag is fused to full length tim cDNA, which lacks any of the introns that are known to be retained at high or low temperatures. (B) Knockdown of Psi with tim-GAL4 and a UAS-dcr2 transgene inserted on the 3rd chromosome also causes period shortening. We used this insertion to more easily generate stocks in a tim0 background, since the tim gene is on the second chromosome, instead of the TD2 combination that has both the tim-GAL4 and UAS-dcr2 transgenes on the 2nd chromosome. ****p<0.0001, Student’s t-test. (C) Period shortening in response to Psi knockdown with tim-GAL4 and UAS-dcr2 is abolished in tim0, ptim-timHA flies that can only produce the full length tim isoform. ns, p=0.1531, Student’s t-test. (B, C) Circadian period length (hrs) is plotted on the y axis. Genotypes are listed on the x axis. Error bars represent SEM. (D) Knockdown of Psi with tim-GAL4 and a UAS-dcr2 3rd chromosome transgene also causes a phase advance in a 12:12 29°C/20°C temperature cycle. (E) The phase advance is abolished in tim0, ptim-timHA flies that can only produce the full length tim isoform. (D, E) Evening peak phase relative to an internal control in each run (w1118) (hrs) is plotted on the y axis. Genotypes are listed on the x axis. Error bars represent SEM. **p<0.01, one-way ANOVA followed by Tukey’s multiple comparison test. N = 3 runs.

## Discussion

Our results identify a novel post-transcriptional regulator of the circadian clock: PSI. PSI is required for the proper pace of both brain and body clock, and for proper phase-relationship with ambient temperature cycles. When Psi is downregulated, the circadian pacemaker speeds up and behavior phase under temperature cycles is advanced by 3 hr, and these phenotypes appear to be predominantly caused by an abnormal tim splicing pattern. Indeed, the circadian period and behavior phase of flies that can only produce functional TIM protein from a transgene missing most introns is insensitive to Psi downregulation. We note however that cwo’s splicing pattern is also affected by Psi downregulation, and we did not study sgg splicing pattern, although it might also be controlled by PSI (Wang et al., 2016). We therefore cannot exclude a small contribution of non-tim splicing events to PSI downregulation phenotypes, or that in specific tissues these other splicing events play a greater role than in the brain.

Interestingly, Psi downregulation results in an increase in intron inclusion events that are favored under cold conditions (tim-sc and tim-cold), while an intron inclusion event favored under warm conditions is decreased (tim-M). However, the ability of tim splicing to respond to temperature changes is not abolished when Psi is downregulated (Figure 3C,E,G). This could imply that an as yet unknown factor specifically promotes or represses tim splicing events in a temperature-dependent manner. Another possibility is that the strength of splice sites or tim’s pre-mRNA structure impacts splicing efficiency in a temperature–dependent manner. For example, suboptimal per splicing signals explain the lower efficiency of per’s most 3’ splicing event at warm temperature (Low et al., 2008).

How would the patterns of tim splicing affect the pace of the circadian clock, or advance the phase of circadian behavior under temperature cycles? In all splicing events that we studied, intron retention results in a truncated TIM protein. It is therefore possible that the balance of full length and truncated TIM proteins, which may function as endogenous dominant-negatives, determines circadian period. For example, truncated TIM might be less efficient at protecting PER from degradation, thus accelerating the pacemaker, or affecting its phase. Consistent with this idea, overexpression of the shorter cold-favored tim isoform (tim-sc) shortens period (Martin Anduaga et al., 2019). Strikingly, Psi downregulation increases this isoform’s levels and also results in a short phenotype. Shakhmantsir et al. (2018) also proposed that production of tim-M transcripts (called tim-tiny in their study) delays the rate of TIM accumulation. Such a mechanism could also contribute to the short period we observed when Psi is downregulated, since this reduces tim-M levels, which may accelerate TIM accumulation. Another interesting question is how PSI differentially affects specific splice isoforms of tim. One possibility is that the execution of a specific tim splicing event negatively influences the probability of the occurrence of other splicing events. For example, PSI could downregulate tim-sc and tim-cold by enhancing splicing and removal of the introns whose retention is necessary for production of these isoforms. This could indirectly reduce splicing of the intron that is retained in the warm tim-M isoform and result in tim-M upregulation. Conversely, PSI could directly promote tim-M intron retention and indirectly downregulate production of tim-sc and tim-cold.

Other splicing factors have been shown to be involved in the control of circadian rhythms in Drosophila. SRm160 contributes to the amplitude of circadian rhythms by promoting per expression (Beckwith et al., 2017), while B52/SMp55 and PRMT5 regulate per’s most 3’ splicing, which is temperature sensitive (Zhang et al., 2018; Sanchez et al., 2010). Loss of PRMT5 results in essentially arrhythmic behavior (Sanchez et al., 2010), but this is unlikely to be explained by its effect on per’s thermosensitive splicing. B52/SMp55 knockdown flies show a reduced siesta, which is controlled by the same per splicing (Zhang et al., 2018). With the identification of Psi, we uncover a key regulator of tim alternative splicing pattern and show that this pattern determines circadian period length, while per alternative splicing regulates the timing and amplitude of the daytime siesta. Interestingly, a recent study identified PRP4 kinase and other members of tri-snRNP complexes as regulators of circadian rhythms (Shakhmantsir et al., 2018). Downregulation of prp4 caused excessive retention of the tim-M intron. PSI and PRP4 might thus have complementary functions in tim mRNA splicing regulation, working together to maintain the proper balance of tim isoform expression.

An unexpected finding is the role played by both PDF neurons and other circadian neurons in the short period phenotype observed with circadian locomotor rhythms when we knocked-down Psi. Indeed, it is quite clear from multiple studies that under constant darkness, the PDF-positive sLNvs dictate the pace of circadian behavior (Stoleru et al., 2005; Yao and Shafer, 2014). Why, in the case of Psi downregulation, do PDF negative neurons also play a role in period determination? The explanation might be that PSI alters the hierarchy between circadian neurons, promoting the role of PDF negative neurons. This could be achieved by weakening PDF/PDFR signaling, for example.

While we focused our work on PSI, several other interesting candidates were identified in our screen (Tables 1 and 2). We note the presence of a large number of splicing factors. This adds to the emerging notion that alternative splicing plays a critical role in the control of circadian rhythms. We have already mentioned above several per splicing regulators that can impact circadian behavior. In addition, a recent study demonstrated that specific classes of circadian neurons express specific alternative splicing variants, and that rhythmic alternative splicing is widespread in these neurons (Wang et al., 2018). Interestingly, in this study, the splicing regulator barc, which was identified in our screen and which has been shown to causes intron retention in specific mRNAs (Abramczuk et al., 2017), was found to be rhythmically expressed in LNds. Moreover, in mammals, alternative splicing appears to be very sensitive to temperature, and could explain how body temperature rhythms synchronize peripheral clocks (Preußner et al., 2017). Another intriguing candidate is cg42458, which was found to be enriched in circadian neurons (LNvs and Dorsal Neurons 1) (Wang et al., 2018). In addition to emphasizing the role of splicing, our screen suggests that regulation of polyA tail length is important for circadian rhythmicity, since we identified several members of the CCR4-NOT complex and deadenylation-dependent decapping enzymes. Future work will be required to determine whether these factors directly target mRNAs encoding for core clock components, or whether their effect on circadian period is indirect. Interestingly, the POP2 deadenylase, which is part of the CCR4-NOT complex, was recently shown to regulate tim mRNA levels post-transcriptionally (Grima et al., 2019). It should be noted that while our screen targeted 364 proteins binding or associated with RNA, it did not include all of them. For example, LSM12, which was recently shown to be a part of the ATXN2/TYF complex (Lee et al., 2017), was not included in our screen because it had not been annotated as a potential RAP when we initiated our screen.

In summary, our work provides an important resource for identifying RNA associated proteins regulating circadian rhythms in Drosophila. It identifies PSI is an important regulator of circadian period and circadian phase in response to thermal cycles, and points at additional candidates and processes that determine the periodicity of circadian rhythms.

## Materials and methods

**Key resources table**


<table>
  <thead>
    <tr>
      <th>Reagent type (species) or resource</th>
      <th>Designation</th>
      <th>Source or reference</th>
      <th>Identifiers</th>
      <th>Additional information</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>Psi</td>
      <td></td>
      <td>FLYB:FBgn0014870</td>
      <td>Flybase name:P-element somatic inhibitor</td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>tim</td>
      <td></td>
      <td>FLYB:FBgn0014396</td>
      <td>Flybase name: timeless</td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>tio</td>
      <td></td>
      <td>FLYB:FBgn0028979</td>
      <td>Flybase name: tiptop</td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>per</td>
      <td></td>
      <td>FLYB:FBgn0003068</td>
      <td>Flybase name: period</td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>cwo</td>
      <td></td>
      <td>FLYB:FBgn0259938</td>
      <td>Flybase name:clockwork orange</td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>RpL32</td>
      <td></td>
      <td>FLYB:FBgn0002626</td>
      <td>qPCR control Flybase name:Ribosomal protein L32</td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>larp</td>
      <td></td>
      <td>FLYB:FBgn0261618</td>
      <td>Flybase name: La related protein</td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>Rbp9</td>
      <td></td>
      <td>FLYB:FBgn0010263</td>
      <td>Flybase name:RNA-binding protein 9</td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>Dcr-2</td>
      <td></td>
      <td>FBgn0034246</td>
      <td>Flybase name: Dicer-2</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>tim-GAL4</td>
      <td>Kaneko et al., 2000</td>
      <td>FLYB:FBtp0010385</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>Pdf-GAL4</td>
      <td>Renn et al., 1999</td>
      <td>FLYB:FBtp0011844</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>Pdf-GAL80, Pdf-GAL80</td>
      <td>Stoleru et al., 2004</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-Dcr2</td>
      <td>Dietzl et al., 2007</td>
      <td>FLYB:FBti0100275 RRID:BDSC_24650</td>
      <td>Chromosome 2</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-Dcr2</td>
      <td>Dietzl et al., 2007</td>
      <td>FLYB:FBti0100276</td>
      <td>Chromosome 3</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>PsiRNAi KK101882</td>
      <td></td>
      <td>FLYB:FBal0231542</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>PsiRNAi GD14067</td>
      <td>Dietzl et al., 2007</td>
      <td>FLYB:FBst0457756</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-Psi</td>
      <td>Labourier et al., 2001</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>BG-LUC</td>
      <td>Stanewsky et al., 1997</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>ptim-TIMLUC</td>
      <td>Lamba et al., 2018</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>timHA</td>
      <td>Rutila et al., 1998</td>
      <td>FLYB:FBal0143160</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>tim0</td>
      <td>Sehgal et al., 1994</td>
      <td>FLYB:FBal0035778</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>VIE260B</td>
      <td></td>
      <td>VDRC_ID: 60100</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>larpRNAi GD8214</td>
      <td>Dietzl et al., 2007</td>
      <td>VDRC_ID: 17366</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>Rbp9RNAi KK109093</td>
      <td></td>
      <td>VDRC_ID: 101412</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>w1118</td>
      <td></td>
      <td>VDRC_ID: 60000</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>40D-UAS</td>
      <td></td>
      <td>VDRC_ID: 60101</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>RpL32-forward</td>
      <td>Dubruille et al., 2009</td>
      <td>PCR primers</td>
      <td>ATGCTAAGCTGTCGCACAAA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>RpL32-reverse</td>
      <td>Dubruille et al., 2009</td>
      <td>PCR primers</td>
      <td>GTTCGATCCGTAACCGATGT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>psi-forward</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>GGTGCCTTGAATGGGTGAT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>psi-reverse</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>CGATTTATCCGGGTCCTCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>tim-M-forward</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>TGGGAATCTCGCCCGAAAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>tim-M-reverse</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>AGAAGGAGGAGAAGGAGAGAGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>tim-sc-forward</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>ACTGTGCGATGACTGGTCTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>tim-sc-reverse</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>TGCTTCAAGGAAATCTTCTG</td>
    </tr>
    <tr>
      <td>Sequence- based reagent</td>
      <td>tim-cold-forward</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>CCTCCATGAAGTCCTCGTTCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>tim-cold-reverse</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>ATTGAGCTGGGACACCAGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>cwo-foward</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>TTCCGCTGTCCACCAACTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>cwo-reverse</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>CGATTGCTTTGCTTTACCAGCTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>cwoRA-forward</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>TCAAGTATGAGAGCGAAGCAGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>cwoRA-reverse</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>TGTCTTATTACGTCTTCCGGTGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>cwoRB-forward</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>GTATGAGAGCAAGATCCACTTTCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>cwoRB-reverse</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>GATGATCTCCGTCTTCTCGATAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>cwoRC-forward</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>GTATGAGAGCCAAGCGACCAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>cwoRC-reverse</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>CCAAATCCATCTGTCTGCCTC</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Direct-zol RNA MiniPrep kit</td>
      <td>Zymo Research</td>
      <td>Zymo Research: R2050</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>iSCRIPT cDNA synthesis kit</td>
      <td>Bio-RAD</td>
      <td>Bio-RAD: 1708891</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>iTaq Universal SYBR Green Supermix</td>
      <td>Bio-RAD</td>
      <td>Bio-RAD: 1725121</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>D-Luciferin, Potassium Salt</td>
      <td>Goldbio</td>
      <td>Goldbio: LUCK-1G</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>TRIzol Reagent</td>
      <td>Invitrogen</td>
      <td>ThermoFisher Scientific:15596026</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>FaasX software</td>
      <td>Grima et al., 2002</td>
      <td></td>
      <td>http://neuro-psi.cnrs.fr/spip.php?article298&amp;lang=en</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MATLAB (MathWorks) signal-processing toolbox</td>
      <td>Levine et al., 2002</td>
      <td>MATLAB RRID: SCR_001622</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MS Excel</td>
      <td></td>
      <td>RRID: SCR_016137</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GraphPad Prism version 7.0 c for Mac OS X</td>
      <td>GraphPad Software, La Jolla, CA USA</td>
      <td>RRID: SCR_002798</td>
      <td>www.graphpad.com</td>
    </tr>
  </tbody>
</table>

### Fly stocks

Flies were raised on a standard cornmeal/agar medium at 25°C under a 12 hr:12 hr light:dark (LD) cycle. The following Drosophila strains were used: w1118 -- w; tim-GAL4, UAS-dicer2/CyO (TD2) (Dubruille et al., 2009) -- y w; Pdf-GAL4, UAS-dicer2/CyO (PD2) (Dubruille et al., 2009) -- y w; Tim-GAL4/CyO (TG4) (Kaneko et al., 2000) -- y w; Pdf-GAL4 (PG4) (Renn et al., 1999) -- w;; UAS-dcr2 (Dietzl et al., 2007) -- y w;; timHA (Rutila et al., 1998) -- yw; TD2; Pdf-Gal80, Pdf-GAL80 (Zhang and Emery, 2013). The following combinations were generated for this study: y w; TG4; Pdf-GAL80, Pdf-GAL80 -- w; tim-GAL4/CyO; UAS-dicer2/TM6B -- tim0,TG4/CyO; UAS-Dcr2/TM6B -- tim0, PsiRNAiKK/CyO; timHA/TM6B. TD2, ptim-TIM-LUC and TD2, BG-LUC transgenic flies expressing a tim-luciferase and per-luciferase fusion gene respectively, combined with the TD2 driver, were used for luciferase experiments. The TIM-LUC fusion is under the control of the tim promoter (ca. 5 kb) and 1st intron (Lamba et al., 2018), BG-LUC contains per genomic DNA encoding the N-terminal two-thirds of PER and is under the control of the per promoter (Stanewsky et al., 1997). RNAi lines (names beginning with JF, GL, GLV, HM or HMS) were generated by the Transgenic RNAi Project at Harvard Medical School (Boston, MA) and obtained from the Bloomington Drosophila Stock Center (Indiana University, USA). RNAi lines (names beginning with GD or KK) and control lines (host strain for the KK library containing landing sites for the RNAi transgenes, VIE-260B, and tio misexpression control strain, 40D-UAS) were obtained from the Vienna Drosophila Stock Center. UAS-Psi flies were kindly provided by D. Rio (Labourier et al., 2001).

### Behavioral monitoring and analysis

The locomotor activity of individual male flies (2–5 days old at start of experiment) was monitored in Trikinetics Activity Monitors (Waltham, MA). Flies were entrained to a 12:12 LD cycle for 3–4 days at 25°C (unless indicated) using I-36LL Percival incubators (Percival Scientific, Perry IA). After entrainment, flies were released into DD for five days. Rhythmicity and period length were analyzed using the FaasX software (courtesy of F. Rouyer, Centre National de la Recherche Scientifique, Gif-sur-Yvette, France) (Grima et al., 2002). Rhythmicity was defined by the criteria – power >20, width >1.5 using the χ2 periodogram analysis. Actograms were generated using a signal-processing toolbox implemented in MATLAB (MathWorks), (Levine et al., 2002). For phase-shifting experiments, groups of 16 flies per genotype were entrained to a 12:12 LD cycle for 5–6 days at 25°C exposed to a 5 min pulse of white fluorescent light (1500 lux) at different time points on the last night of the LD cycle. A separate control group of flies was not light-pulsed. Following the light pulse, flies were released in DD for six days. To determine the amplitude of photic phase shifts, data analysis was done in MS Excel using activity data from all flies, including those that were arrhythmic according to periodogram analysis. Activity was averaged within each group, plotted in Excel, and then fitted with a 4 hr moving average. A genotype-blind observer quantified the phase shifts. The peak of activity was found to be the most reliable phase marker for all genotypes. Phase shifts were calculated by subtracting the average peak phase of the light-pulsed group from the average peak phase of non-light pulsed group of flies. Temperature entrainment was performed essentially as described in Busza et al. (2007). Flies were entrained for 4–5 days in LD followed by 11 days in an 8 hr phase advanced temperature cycle. Behavior was analyzed between day 7 and day 10 of the temperature cycle. Actograms were used to ensure that all genotypes had reached – as expected from Busza et al. (2007) – a stable phase relationship with the temperature cycle. The phase of the evening peak of activity was determined as described for the phase response curve above. Because, under a LD cycle, the evening peak tend to be truncated by the light off transition, we used the approach described in Harrisingh et al. (2007), which compares the percent of activity between ZT17.5–23.5 that occurs between ZT20.5–23.5 (Morning anticipation phase score), or the percent of activity between ZT5.5–11.5 that occurs between ZT8.5–11.5 (Evening anticipation phase score). If phase is advanced, and activity increases earlier than normal, this percent will decrease.

### Statistical analysis

For the statistical analysis of behavioral and luciferase period length, Student’s t-test was used to compare means between two groups, and one-way analysis of variance (ANOVA), coupled to post hoc tests, was used for multiple comparisons. Tukey’s post hoc test was used when comparing three or more genotypes and Dunnett’s post hoc test was used when comparing two experimental genotypes to one control. For the statistical analysis of qPCR and the behavioral phase-shifting experiments, two-way ANOVA, coupled to Tukey’s post hoc test, was used for multiple comparisons. Statistical analyses were performed using GraphPad Prism version 7.0 c for Mac OS X, GraphPad Software, La Jolla California USA, www.graphpad.com. P values and 95% Confidence Intervals are reported in data source files ‘Figure statistics’.

### Luciferase experiments

The luciferase activity of whole male flies on Luciferin (Gold-biotech) containing agar/sucrose medium (170 μl volume, 1% agar, 2% sucrose, 25 mM luciferin), was monitored in Berthold LB960 plate reader (Berthold technologies, USE) in l-36LL Percival incubators with 90% humidity (Percival Scientific, Perry IA). Three flies per well were covered with needle-poked Pattern Adhesive PTFE Sealing Film (Analytical sales and services 961801). The distance between the agar and film was such that the flies were not able to move vertically. Period length was determined from light measurements taken during the first two days of DD. The analysis was limited to this window because TIM-LUC and BG-LUC oscillations severely dampened after the second day of DD. Period was estimated by an exponential dampened cosinor fit using the least squares method in MS Excel (Solver function).

### Real-time quantitative PCR

Total RNA from about 30 or 60 fly heads collected at CT 3, CT9, CT15 and CT21 on the first day of DD were prepared using Trizol (Invitrogen) and Zymo Research Direct-zol RNA MiniPrep kit (R2050) following manufacturer’s instructions. 1 μg of total RNA was reverse transcribed using Bio-RAD iSCRIPT cDNA synthesis kit (1708891) following manufacturer’s instructions. Real-time PCR analysis was performed in triplicate (three technical replicates per sample) using Bio-RAD iTaq Universal SYBR Green Supermix (1725121) in a Bio-RAD C1000 Touch Thermal Cycler instrument. A standard curve was generated for each primer pair, using RNA extracted from wild-type fly heads, to verify amplification efficiency. Data were normalized to RpL32 (Dubruille et al., 2009) using the 2-ΔΔCt method. Primers used: RpL32-forward ATGCTAAGCTGTCGCACAAA; RpL32-reverse GTTCGATCCGTAACCGATGT; psi-forward GGTGCCTTGAATGGGTGAT; psi-reverse CGATTTATCCGGGTCCTCG; tim-M-forward TGGGAATCTCGCCCGAAAC; tim-M-reverse AGAAGGAGGAGAAGGAGAGAGG; tim-sc-forward ACTGTGCGATGACTGGTCTG; tim-sc-reverse TGCTTCAAGGAAATCTTCTG; tim-cold-forward CCTCCATGAAGTCCTCGTTCG; tim-cold-reverse ATTGAGCTGGGACACCAGG; cwo-foward TTCCGCTGTCCACCAACTC; cwo-reverse CGATTGCTTTGCTTTACCAGCTC; cwoRA-forward TCAAGTATGAGAGCGAAGCAGC; cwoRA-reverse TGTCTTATTACGTCTTCCGGTGG; cwoRB-forward GTATGAGAGCAAGATCCACTTTCC; cwoRB-reverse GATGATCTCCGTCTTCTCGATAC; cwoRC-forward GTATGAGAGCCAAGCGACCAC; cwoRC-reverse CCAAATCCATCTGTCTGCCTC.
