# Small conductance Ca2+-activated K+ channels induce the firing pause periods during the activation of Drosophila nociceptive neurons

## Authors

- Koun Onodera<sup>1</sup> ([ORCID: 0000-0002-4203-9865](https://orcid.org/0000-0002-4203-9865))
- Shumpei Baba<sup>1</sup>
- Akira Murakami<sup>2</sup>
- Tadashi Uemura<sup>1</sup> ([ORCID: 0000-0001-7204-3606](https://orcid.org/0000-0001-7204-3606))
- Tadao Usui<sup>1</sup> ([ORCID: 0000-0002-0507-1495](https://orcid.org/0000-0002-0507-1495)) †

### Affiliations

1. Graduate School of Biostudies Kyoto University Kyoto Japan
2. Faculty of Science Kyoto University Kyoto Japan
3. Graduate School of Informatics Kyoto University Kyoto Japan

† Corresponding author

## Abstract

10.7554/eLife.29754.001 In Drosophila larvae, Class IV sensory neurons respond to noxious thermal stimuli and provoke heat avoidance behavior. Previously, we showed that the activated neurons displayed characteristic fluctuations of firing rates, which consisted of repetitive high-frequency spike trains and subsequent pause periods, and we proposed that the firing rate fluctuations enhanced the heat avoidance (Terada et al., 2016). Here, we further substantiate this idea by showing that the pause periods and the frequency of fluctuations are regulated by small conductance Ca 2+ -activated K + (SK) channels, and the SK knockdown larvae display faster heat avoidance than control larvae. The regulatory mechanism of the fluctuations in the Class IV neurons resembles that in mammalian Purkinje cells, which display complex spikes. Furthermore, our results suggest that such fluctuation coding in Class IV neurons is required to convert noxious thermal inputs into effective stereotyped behavior as well as general rate coding.

## Introduction

Animals sense diverse environmental inputs, including noxious ones, by using specific sensory organs. In principle, sensory neurons convert the intensity of stimuli into the magnitude of firing rates upon sensory transduction (Adrian, 1926). For instance, mammalian C-fiber nociceptors convert gentle touch stimuli into relatively low firing rates, whereas injurious forces elicit higher rates (Delmas et al., 2011). The ‘rate coding’ is valuable for sensory transduction, particularly with regard to stimulus intensity; however, the firing rate has an intrinsic upper limit because interspike intervals (ISIs) cannot be shorter than refractory periods, when the membrane is unable to respond to another stimulus (Berry and Meister, 1998; Hodgkin and Huxley, 1952). This implies that firing rates should saturate at high intensities, at which point the sensory inputs are no longer converted properly in an intensity-to-firing rate correspondence. Therefore, we assume that some sensory neurons may use other coding mechanisms that are employed in the central nervous system (Avissar et al., 2013; Haddad et al., 2013).

In Drosophila larvae, Class IV dendritic arborization neurons (Class IV neurons) are primary nociceptive neurons that respond to multiple stimuli, including high temperature, strong mechanical force, and short-wavelength light (Hwang et al., 2007; Tracey et al., 2003; Xiang et al., 2010). When the neurons are activated by noxious thermal stimuli, for instance, their sensory transduction provokes heat avoidance behavior where larvae rotate around the long body axis in a corkscrew-like manner. A large number of genes responsible for the neuronal activation were identified by evaluating behavioral phenotypes and monitoring Ca2+ dynamics in mutant strains (Lee et al., 2005; Neely et al., 2011; Tracey et al., 2003; Zhong et al., 2012); however, there have been few studies which have investigated the coding mechanism of the nociception by recording electrical activity (Terada et al., 2016; Xiang et al., 2010).

Previously, we built a measurement system using a 1460 nm infrared (IR) laser as a local heating device (Figure 1—figure supplement 1A) and found that Class IV neurons responded to noxious thermal stimuli with evoked characteristic fluctuations of firing rates, which consisted of repetitive high-frequency spike trains and subsequent quiescent periods (Terada et al., 2016). The occurrence of such ‘burst-and-pause’ firing patterns was coordinated with large Ca2+ increments over the entire dendritic arbors (designated as dendritic Ca2+ transients here) and was mediated by L-type voltage-gated Ca2+ channels (VGCCs). Knocking down L-type VGCCs in neurons abolished the burst-and-pause firing patterns, and the knockdown larvae displayed delayed heat avoidance behavior. Therefore, we hypothesized that the burst-and-pause firing patterns should be output signals transducing high intensity stimuli and provoking the robust avoidance behavior. However, the regulatory mechanism of the firing patterns remained unclear because L-type VGCCs produce depolarizing currents but not hyperpolarizing ones, which should underlie ‘pause’ periods. Here, we show that the pause period and the number of the burst-and-pause firing patterns are regulated by small conductance Ca2+-activated K+ (SK) channels, and that SK knockdown larvae display relatively fast heat avoidance. Furthermore, we show that one of the downstream neurons dramatically changes the response to two optogenetic activations of the Class IV neurons which have distinct numbers of burst-and-pause firing patterns. These findings strengthen the hypothesis and suggest that the ‘fluctuation coding’ is required to convert high intensities of noxious thermal stimuli into the robust, appropriate avoidance behavior as well as general rate coding.

## Results

## Dendritic Ca2+ transients precede unconventional spikes

To understand the molecular mechanism that generates burst-and-pause firing patterns in response to thermal stimuli, we first examined the temporal relationship with dendritic Ca2+ transients, whose occurrence was coordinated with the specific firing patterns in an all-or-none fashion. The temporal relationship between the Ca2+ transients and unconventional spikes (USs; Figure 1A) was unclear because the temporal resolution of monitoring Ca2+ dynamics was 30 Hz in our previous work (Terada et al., 2016), which was lower than the minimum frequency required to measure differences between spike timings (100–500 Hz; Lütcke et al., 2013). Therefore, we monitored Ca2+ dynamics with higher temporal resolution (100 Hz) by using a genetically encoded Ca2+ indicator GCaMP5G (Akerboom et al., 2012), which was brighter than the ratiometric indicator TN-XXL (Mank et al., 2008) as employed in our previous work (Terada et al., 2016). We then found that all the dendritic Ca2+ transients occurred concurrently with USs (Figure 1B,C and D). In contrast, when no US occurred or before the first US occurred, Ca2+ transients were never observed. To accurately measure the onset of Ca2+ transients with stochastic fluctuations, we used an event detection algorithm based on a Schmitt trigger approach (Grewe et al., 2010; Lütcke et al., 2013) and fit each transient to exponential curves. We then found that the onset of Ca2+ transients preceded first-US timings and that the Ca2+ transients with multiple USs were stepwise (Figure 1E and F; Δt = − 50.3 ± 9.2 ms, mean ± s.e.m.). We also found that the peak amplitudes of Ca2+ transients displayed a positive linear correlation with the number of USs (Figure 1G; p=1.0 × 10−11, rho = 0.82, Spearman’s rank correlation test). Furthermore, ISIs were shorter before onsets of pauses (Figure 1H; p<0.05, paired-sample t-test with Bonferroni correction).

We hypothesized that the Ca2+ influx mediated by L-type VGCCs amplifies membrane depolarization, which narrows down ISIs of bursts and also induces subsequent pauses. Therefore, we searched for ion channels responsible for generating inhibitory currents that could hyperpolarize membrane potentials during pause periods. We anticipated that activities of such channels must be regulated by intracellular Ca2+ concentration ([Ca2+]i) either directly or indirectly.

## Electrophysiological screen of Cl− channels and K+ channels

To elucidate the regulatory mechanism of the pause, we screened ion channels that might generate hyperpolarizing currents: such channels include outward K+ and inward Cl− channels. The direction of passive transport of each ion through channels is dependent on the electrochemical gradient across the plasma membrane, but the intracellular Cl− concentration ([Cl−]i) is largely different among cells (Kaila et al., 2014) and the direction of Cl− transport in Class IV neurons was unclear. We therefore monitored Cl− dynamics by a genetically encoded FRET-based Cl− indicator, SuperClomeleon (Grimley et al., 2013; Figure 2A) and found that the FRET ratio increased at both somata and distal dendrites upon IR-laser irradiation (Figure 2B and C). Because the FRET ratio of SuperClomeleon rises as the [Cl−]i falls, we expected that the [Cl−]i should decrease upon stimulation. These results suggest that the passive Cl− transport in Class IV neurons is outward and generates depolarizing currents but not hyperpolarizing ones. In parallel, we investigated the role of one of the Ca2+-activated Cl− channels, Subdued (Jang et al., 2015), and showed that it can contribute to membrane excitation in the neurons (Figure 2—figure supplement 1). Thus, we excluded Cl− channels as candidate sources of hyperpolarizing currents.

Next, we focused on the roles of various K+ channels as mediators of hyperpolarization. The Drosophila melanogaster genome has 29 genes that encode pore-forming subunits of K+ channels, including 11 voltage-gated K+ channels (Sh, eag, etc.), 11 two-pore domain K+ channels (Task6, sand, etc.; Pimentel et al., 2016) and others (Figure 2—source data 1). We first knocked down each of the candidate genes in Class IV neurons and recorded electrical activities of the knockdown neurons upon IR-laser irradiation, and examined the properties of burst-and-pause firing patterns. We found that the number of USs was significantly increased in five different gene knockdown neurons (Sh, Shal, SK, Irk2, and Task7; Figure 2D and E; p<0.05, Wilcoxon rank sum test). The five knockdown neurons also exhibited an increased number of ‘peaks’ (Figure 2—figure supplement 2; p<0.05, Wilcoxon rank sum test), as defined in our previous study (Terada et al., 2016). Furthermore, although knocking down L-type VGCC abolishes dendritic Ca2+ transients (Terada et al., 2016), the five K+ channel knockdowns did not decrease the amplitudes of the Ca2+ transients (Figure 2F). These results suggested that these candidates participate in an unknown mechanism downstream of the Ca2+ influx. Notably, SK encodes a small conductance Ca2+-activated K+ channel, which can be activated by dendritic Ca2+ influx, and therefore could be one of the major factors underlying hyperpolarization. Thus, we explored how SK channels contributed to shaping the burst-and-pause firing patterns.

## SK channels generate pause periods

To investigate the physiological roles of SK channels, we stimulated the knockdown neurons with different IR-laser powers. We then found that SK knockdown increased the firing properties, including the US number, peak number and maximum firing rate, even with low laser powers (Figure 3A–D, Figure 3—figure supplement 1A). Importantly, the SK knockdown shortened the pause periods (Figure 3E; median of pause period: [ppk-Gal4] 103.9 ms, [UAS-SK RNAi] 112.9 ms, [ppk>SK RNAi] 46.75 ms; p<0.001, Student’s t-test with Holm correction), which suggested that SK-dependent current regulates the pause period. Similar firing changes were also observed in two additional SK knockdown neurons, targeting two different sequences in the SK gene (Figure 3—figure supplement 2A–D, Figure 3—figure supplement 1B). We speculated that SK channels would be dramatically activated by the sudden increase in [Ca2+]i through L-type VGCCs, and would generate a transient hyperpolarizing K+ current. Nevertheless, it was important to rule out a more trivial explanation for the changes in firing patterns in the SK knockdown neurons, which might possibly be due to altered dendritic architecture. We quantified the dendritic morphology of SK knockdown neurons and concluded that the altered physiological responses were not due to morphological defects in the dendritic arbors (Figure 3—figure supplement 3).

We hypothesized that the burst-and-pause firing patterns should be output signals provoking robust heat avoidance behavior. To test this hypothesis, we examined how SK knockdown larvae responded to thermal stimulation, and we found that they displayed significantly faster onsets of responses; moreover, the response rate was increased upon moderate stimulation (44°C, Figure 3F and G; 42°C, Figure 3—figure supplement 2E F). These results suggested that the enhanced behavioral responses are induced either by the increment in the US number or by the changes in the other firing properties (pause period and maximum firing rate, etc.). We previously reported that the L-type VGCC knockdown abolished the burst-and-pause firing patterns and provoked a delayed response to thermal stimuli (Terada et al., 2016). Consistent with these findings, we propose that the burst-and-pause firing patterns should be output signals provoking the robust avoidance behavior.

We also examined heat avoidance behavior of larvae, where one of the other three candidate genes (Shal, Irk2, and Task7) was knocked down; however, the respective knockdown larvae did not show any difference in the response rate of avoidance (Figure 3—figure supplement 4A and B). Interestingly, the frequencies of spontaneous spikes were significantly increased in the three knockdown Class IV neurons but not in SK knockdown ones (Figure 3—figure supplement 4C and D). Notably, a recent study revealed that the activation of Class IV neurons during larval development inhibited the synaptic transmission to second-order neurons via serotonergic feedback signaling and suppressed the avoidance behavior (Kaneko et al., 2017). In addition, the topographic projections of Class IV neurons are partially dependent on the levels of neuronal activity, including spontaneous spikes (Kaneko and Ye, 2015; Yang et al., 2014). Thus, the elevated basal neuronal activity during development might decrease the efficacy of synaptic transmission and/or remodel synaptic connections of the neurons, which would tend to counteract the effect of the increment of firing rate fluctuations on the avoidance behavior of these knockdown animals.

The downstream circuitry of the Class IV neurons has been identified through functional and anatomical approaches (Chin and Tracey, 2017; Hu et al., 2017; Ohyama et al., 2015; Vogelstein et al., 2014; Yoshino et al., 2017). To explore any differences in the responses of that circuitry when Class IV neurons evoked various firing patterns, we examined the neuronal activity of Goro neurons in response to optogenetic activations of Class IV neurons (Figure 3—figure supplement 5A). We first investigated firing patterns induced by optogenetic activations in Class IV neurons and found that the numbers of burst-and-pause patterns were significantly different between continuous and intermittent illuminations (Figure 3—figure supplement 5B–D; p<0.001, Wilcoxon signed-rank sum test). Importantly, the total spike numbers and maximum firing rates were comparable between the two conditions (Figure 3—figure supplement 5E and F). We then examined whether the activity of the downstream neurons should be differentially induced with the type of optogenetic manipulation. We found that the maximum amplitude of Ca2+ rises in Goro neurons was larger upon activation accompanied with more burst-and-pause firing patterns in Class IV neurons (Figure 3—figure supplement 5G and H; [continuous] Fpeak = 11.3 ± 1.8%, [intermittent] Fpeak = 19.4 ± 2.2%, mean ± s.e.m.; p<0.01, Welch’s t-test). The results suggested that firing rate fluctuations were decoded in downstream circuits separately from the firing rate itself. Although the mechanism by which burst-and-pause firing patterns are read out as downstream electrical signals is still unknown, we can address this question by examining the activities of the other neurons in the circuitry.

## Discussion

Although the increased number of USs in SK knockdown neurons may initially seem counterintuitive, it can be explained comprehensively by two states of SK channels, at low and high activation levels (Figure 4A): (i) Before USs occur, most SK channels are in the steady state because the Ca2+/calmodulin association is restricted at low [Ca2+]i, and the SK current slightly inhibits the incidence of firings during burst periods. Therefore, SK knockdown attenuates the inhibition of firings, which raises the occurrence rate of USs. (ii) In contrast, after USs occur with dendritic Ca2+ transients, the channels are shifted to the activation state by high [Ca2+]i, and the current greatly promotes after-hyperpolarization, which generates the pause periods. Thus, the knockdown dramatically decreases the pause periods, which shortens the time requiring one burst-and-pause firing pattern. Due to the two impacts on firings, the US number per unit time would be expected to increase upon SK knockdown.

We hypothesize that the burst-and-pause firing patterns in Class IV neurons are regulated by functional coordination between L-type VGCCs and SK channels as follows (Figure 4B): (1) Thermosensitive channels including dTrpA1 and Painless (Luo et al., 2017; Neely et al., 2011; Tracey et al., 2003; Zhong et al., 2012) are activated by high-temperature stimulation and elicit the initial membrane depolarization in the dendritic arbors. (2) Once the membrane potential of soma exceeds a certain threshold by the prolonged stimulation, the neurons evoke action potentials and then increase firing rates with the intensity of stimulation (‘rate coding’). (3) When L-type VGCCs in the dendritic arbors are activated by the high-order depolarization, they induce a large Ca2+ influx, which rapidly activates SK channels. (4) The activated SK channels produce a hyperpolarizing current, thereby generating the pause periods (‘fluctuation coding’). We also suggest that other K+ channels may slightly contribute to the generation of pauses, because the pause periods were not completely abolished in SK knockdown neurons (Figure 3E, Figure 3—figure supplement 2D). Although the other candidate channels, such as Sh and Shal, are not activated by the [Ca2+]i rise, most of them are voltage-dependent and hence hyperpolarize the membrane potential to some degree after depolarization, regardless of dendritic Ca2+ influx. Because the hyperpolarization suppresses the probability of firing, including US, the knockdown of those channels should lead to the increment of the US number.

In the mammalian cerebellar cortex, climbing fiber inputs evoke complex spikes of Purkinje cells, which induce a dendritic Ca2+ influx through Ca2+ spikes and subsequent pauses (Davie et al., 2008; Kitamura and Häusser, 2011; Llinás and Sugimori, 1980; Mathews et al., 2012). The pause periods of post-complex spikes are regulated by dendritic Ca2+ spikes, which are dependent on P/Q-type VGCCs (Davie et al., 2008), and are modulated by after-hyperpolarization, which is largely dependent on SK2 channels (Grasselli et al., 2016). Considering these observations, the regulatory mechanism of complex spikes is remarkably similar to that of burst-and-pause firing patterns in Class IV neurons (Figure 4—figure supplement 1A).

In principle, sensory neurons convert the intensity of stimuli into the magnitude of firing rates (Adrian, 1926). This form of rate coding also occurs in Class IV neurons at relatively low temperatures, and it is mediated by thermosensitive channels and many types of voltage-gated ion channels (Figure 4B, Figure 4—figure supplement 1B and C). At higher temperature, however, L-type VGCCs and SK channels modulate the firing, transitioning from continuous high-frequency patterns into burst-and-pause patterns. Thus, we propose that the firing-rate-fluctuation coding allows sensory neurons to transmit strong stimuli not covered in rate coding, thereby provoking robust avoidance behavior.

## Materials and methods

## Drosophila mutant and transgenic strains

The transgenic line expressing the FRET-based Ca2+ indicator TN-XXL (Mank et al., 2008) in Class IV neurons was 3×[ppk-TN-XXL] (attP40) from our previous work (Terada et al., 2016). Mutants of one of the Anoctamin family channels, Subdued, were subduedΔ5265 and Df(3R)Exel6184, from C. Kim. A transgenic line expressing the split Gal4 was R72F11_AD; R52F07_DBD from T. Ohyama. A transgenic line expressing the FRET-based Cl− indicator SuperClomeleon was UAS-SuperClomeleon (FBst0059847; Haynes et al., 2015) from the Bloomington Stock Center. Transgenic lines expressing channel RNAi were from the Bloomington Stock Center and Vienna Drosophila Resource Center (see also Figure 2—source data 1). Other transgenic lines were pickpocket (ppk)-Gal4 (FBst0032078), 20 × UAS-GCaMP5G (FBst0042037), UAS-Dcr-2 (FBst0024651), TrpA1-QF (FBst0036348), R69F06-Gal4 (FBst0039497), 10XQUAS-ChR2.T159C-HA (FBst0052259), and 20XUAS-IVS-NES-jRCaMP1b-p10 (FBst0063793), from the Bloomington Stock Center.

Exact genotypes of individual animals used in figures are described below:

## Figure 1

ppk-Gal4/20 × UAS-GCaMP5G (attP40)

## Figure 2

(B–C) ppk-Gal4/20 × UAS SuperClomeleon (attP40)

(D–F) ppk-Gal4, 3×[ppk-TN-XXL] (attP2), UAS-each channel RNAi (see Figure 2—source data 1)

## Figure 3

w1118; ppk-Gal4/+; 3×[ppk-TN-XXL] (attP2)/+ (‘ppk-Gal4’)

UAS-SK RNAiHMJ21196/+; 3×[ppk-TN-XXL] (attP2)/+ (‘UAS-SK RNAi’)

ppk-Gal4/UAS-SK RNAiHMJ21196; 3×[ppk-TN-XXL] (attP2)/+ (‘ppk>SK RNAi’)

## Figure 1—figure supplement 1

(B) ppk-Gal4/20 × UAS-GCaMP5G (attP40)

## Figure 2—figure supplement 1

(A–F) 3×[ppk-TN-XXL] (attP40)/+ (‘WT’)

3×[ppk-TN-XXL] (attP40)/+; subduedΔ5265/Df(3R)Exel6184 (‘subdued’)

(G–H) ppk-Gal4/20 × UAS SuperClomeleon (attP40); subduedΔ5265/Df(3R)Exel6184

## Figure 2—figure supplement 2

ppk-Gal4, 3×[ppk-TN-XXL] (attP2), UAS-each channel RNAi (see Figure 2—source data 1)

## Figure 3—figure supplement 2

w1118; ppk-Gal4/+; UAS-Dcr-2/+ (‘Control’)

w1118; ppk-Gal4/+; UAS-Dcr-2/UAS-SK RNAiGD12601 (‘SK RNAiGD’)

w1118; ppk-Gal4/UAS-SK RNAiKK107699; UAS-Dcr-2/+ (‘SK RNAiKK’)

## Figure 3—figure supplement 1

(A) w1118; ppk-Gal4/+; 3×[ppk-TN-XXL] (attP2)/+ (‘ppk-Gal4’)

UAS-SK RNAiHMJ21196/+; 3×[ppk-TN-XXL] (attP2)/+ (‘UAS-SK RNAiHMJ’)

ppk-Gal4/UAS-SK RNAiHMJ21196; 3×[ppk-TN-XXL] (attP2)/+ (‘ppk>SK RNAiHMJ’)

(B)w1118; ppk-Gal4/+; UAS-Dcr-2/+ (‘Control’)

w1118; ppk-Gal4/+; UAS-Dcr-2/UAS-SK RNAiGD12601 (‘ppk>SK RNAiGD’)

w1118; ppk-Gal4/UAS-SK RNAiKK107699; UAS-Dcr-2/+ (‘ppk>SK RNAiKK’)

## Figure 3—figure supplement 3

w1118; ppk-Gal4/+; 3×[ppk-TN-XXL] (attP2)/+ (‘ppk-Gal4’)

UAS-SK RNAiHMJ21196/+; 3×[ppk-TN-XXL] (attP2)/+ (‘UAS-SK RNAi’)

ppk-Gal4/UAS-SK RNAiHMJ21196; 3×[ppk-TN-XXL] (attP2)/+ (‘ppk>SK RNAi’)

3×[ppk-TN-XXL] (attP2)/UAS-Sur RNAiGL00506

ppk-Gal4/+; 3×[ppk-TN-XXL] (attP2)/UAS-Sur RNAiGL00506

## Figure 3—figure supplement 4

w1118; ppk-Gal4/+; 3×[ppk-TN-XXL] (attP2)/+ (‘ppk-Gal4’)

ppk-Gal4, 3×[ppk-TN-XXL] (attP2), UAS-each channel RNAi (see Figure 2—source data 1)

## Figure 3—figure supplement 5

(B–F)

TrpA1-QF 10XQUAS-ChR2.T159C-HA/R72F11_AD; 20XUAS-IVS-NES-jRCaMP1b-p10/R52F07_AD

(G–H)

TrpA1-QF 10XQUAS-ChR2.T159C-HA/+; 20XUAS-IVS-NES-jRCaMP1b-p10/R69F06-Gal4

(‘Class IV>ChR2, Goro>jRCaMP’)

## Electrophysiology and IR-laser irradiation

Preparation of larvae and extracellular recording were performed as previously described (Terada et al., 2016, Figure 1—figure supplement 1A). The foci of the infrared (IR)-laser irradiation were targeted onto the proximal dendritic arbors, essentially as described in our previous analyses. The time window for the experimental irradiation was 1 s except for data for Figure 2—figure supplement 1C (30 mW IR, 5 s) and Figure 3A (36-mW IR, 5 s), which were quantified during the initial 1 s. Quantification of the maximum firing rate and the peak number of firing rate fluctuations was performed as previously described (Terada et al., 2016) with slight modifications (see Figure 2—figure supplement 2A). For quantification of the pause period, we excluded USs that had occurred around the shutdown of IR-laser irradiation and were not accompanied by additional spikes during the irradiation.

## Ca2+ imaging

We used a TN-XXL indicator except for Figure 1 because it allowed more robust quantitative analysis in the presence of perturbations along Z-axis motions by larval body wall muscles. Ca2+ imaging of TN-XXL-expressing Class IV neurons was performed as previously described (Terada et al., 2016). ΔR is the change of fluorescence ratio and ΔRpeak is defined as the maximum. Ca2+ imaging of GCaMP5G was performed on filet preparations. GCaMP5G was excited with a 445 nm diode laser (CUBE 445–40C, Coherent, Santa Clara, CA). Images were acquired at 128 × 128 pixels with 1 × 1 binning, in a 14-bit dynamic range, and with 10 ms exposure time. The fluorescence signal was captured by the imagers with 100 Hz through 578/105 bandpass filters (Semrock, Lake Forest, IL). The fluorescence change was defined as:Δ F/F0=(Fn-F0)/F0

where Fn is the fluorescence at time point n, and F0 is the average fluorescence before starting IR-laser irradiation (time window 100 ms). Fpeak is defined as the maximum amplitude of ΔF/F0. The fluorescence itself declined during IR-laser irradiation, so the decay was subtracted for quantification.

## Estimation of the onset timing of Ca2+ transients by curve fitting

Estimation of onset timings of Ca2+ transients was performed as previously described (Grewe et al., 2010; Lütcke et al., 2013) with slight modifications:fCa(t)=A(1−e−(t−t0)/τon)⋅e−(t−t0)/τoff , for t>t0fCat=0,                      for t≤t0

Here, t0 denotes the onset of Ca2+ transients, τon the onset rise time constant, τoff the decay time constant, and A an amplitude scale parameter. τon and τoff were manually adjusted for precise curve fitting in each trial (τon=50–500 ms, τoff = 1.5–10 s). The value of A is dependent on the maximum of each Ca2+ transient. Before fitting, a baseline offset was subtracted from the trace segment. We used MATLAB scripts provided in Lütcke et al. (2013).

## Cl− imaging

Cl− imaging of SuperClomeleon-expressing Class IV neurons was performed on whole-mount preparations. The data acquisition system was the same as for Ca2+ imaging of TN-XXL (Terada et al., 2016). The ratio of SuperClomeleon was defined as:RatioSuperClomeleon= YFPunmasked-YFPmasked/CFPunmasked-CFPmasked

where YFPunmasked and CFPunmasked are signals of outlined cellular regions, and YFPmasked and CFPmasked are those of background.

## Thermal behavioral assay

Animals were raised at 25˚C in an incubator with 12 hr light/dark cycles, and humidity was manually controlled (75–80%). Wandering third-instar larvae were gently picked up from the vial, washed three times with deionized water, and transferred to a 140 × 100 mm petri dish with fresh 2% agarose. Excessive water was removed from the animals. For acclimation, animals were allowed to rest on the plate for at least 5 min before testing. The response latency was measured as the time interval from the point at which the larva was first contacted by the probe until it initiated the first 360˚ rotation. The time window was 5 s when we could maintain the contact more precisely than the general time window (10 s). About 20 larvae in the control and experimental groups were tested on the same day, and the assays were repeated for several days.

## Image acquisition and quantification of dendritic morphology

Imaging ddaC neurons in whole-mount larvae was done as previously described (Shimono et al., 2014), with slight modifications. Wandering third-instar larvae were gently picked up from the vial, and washed once with 0.7% NaCl and 0.3% Triton X-100, and three times with deionized water. They were mounted in 50% glycerol on slides, between spacers made of vinyl tape. Images of YFP fluorescence in TN-XXL were acquired using a Nikon C1 laser-scanning confocal microscope. Original images of each neuron were composed of maximum intensity projections of confocal micrographs.

Dendritic coverage was quantified as previously described (Honjo et al., 2016) with appropriate modifications (Figure 3—figure supplement 3A). Original images were inverted with black and white, and the images were converted through a Laplacian filter to enhance the edge contrast and the VanderBrug operator (Vanderbrug, 1976; VanderBrug, 1977) to enhance the line contrast. The images were binarized to detect the enhanced parts. The images were converted through a maximum filter to interpolate between separated dendrites. Spotted noise was removed by labeling. The images were overlaid with a grid of 34 × 34 pixel squares (14 × 14 µm), and squares containing signals were counted to calculate the dendritic coverage score. The preceding quantification steps were automatically processed with a MATLAB script. After that, false-positives and false-negatives were manually corrected on a MATLAB application using a graphical user interface (GUI).

## Optogenetic neural activation

Optogenetic activation of Class IV neurons was performed as previously described (Terada et al., 2016). Larvae expressing the ChR2 variant in Class IV neurons driven by TrpA1-QF (attP40) (Petersen and Stowers, 2011; Yoshino et al., 2017) were grown on fly food containing all trans-retinal (R2500; Sigma-Aldrich) at a final concentration of 0.5 mM. For optogenetic activation, a single long pulse (continuous illumination) or multiple cycles of 100 ms pulses followed by 100 ms pause intervals (intermittent illumination) were applied by using a collimated LED light lamp (M470L3-C1; ThorLabs, Newton, NJ) with an emission peak at around 470 nm (0.37 mW/mm2). Each cell was stimulated by two illumination patterns temporally separated by a pause interval of at least 1.5 min. The first stimulus was a continuous pattern, and the second was an intermittent one in half of the trials; and the sequence of stimulus patterns was reversed in the other half. We did not find any differences of neuronal activities dependent on the order of the two types of illuminations.

Ca2+ imaging of jRCaMP-expressing Goro neurons was performed on optimized filet preparations as follows: (i) After basic preparations on a glass slide, anterior thoracic epidermis was cut off. (ii) Epidermis under the larval brain was slit vertically from the anterior side, and the brain was gently pinned on the slide. (iii) The samples were incubated with 7 mM monosodium glutamate (Nacalai, Kyoto, Japan) for 8 min to prevent muscle contractions and eliminate motor feedback to the sensory circuits by saturating glutamate receptors at the neuromuscular junction (Kaneko et al., 2017).

Imaging was done as previously described (Arata et al., 2017), with slight modifications. Data were collected on an IX71 microscope (Olympus) equipped with an objective (UPLSAPO60XS NA 1.3, Olympus), Nipkow disk confocal system (CSU10, Yokogawa Electric, Tokyo, Japan), and an EM-CCD camera (iXonEM+ DU-888, Andor Technology, Belfast, UK). jRCaMP was excited with a 561 nm diode laser (Sapphire, Coherent, Santa Clara, CA), and was captured by the imagers at 1.5 s intervals through 610/60 bandpass filters (Chroma Technology, Bellows Falls, VT). The above imaging system was controlled by MetaMorph software (Molecular Devices, Sunnyvale, CA). Each sample was stimulated once either by continuous illumination or by intermittent illumination. Quantification of the fluorescence change was the same as for Ca2+ imaging of GCaMP5G.

## Statistics

Data were analyzed and plotted using ImageJ (National Institutes of Health, Bethesda, MD), MATLAB (The MathWorks, Natick, MA), and Microsoft Excel (Microsoft Corporation, Redmond, WA). Details for each figure are shown in source data. To prevent misinterpretation as outliers in some figures (Figure 2E and F; Figure 2—figure supplement 2), p<0.05 and p<0.01 are indicated by double and triple asterisks, respectively.

## Abbreviations

[Ca2+]i, intracellular Ca2+ concentration; [Cl−]i, intracellular Cl− concentration; GUI, graphical user interface; IR, infrared; ISI, interspike interval; K2P, Two-pore domain K+ channel; KCa, Ca2+-activated K+ channel; Kir, Inward rectifier K+ channel; Kv, voltage-gated K+ channel; NR, no response group; ns, not significant; ppk, pickpocket; SK channel, small conductance Ca2+-activated K+ channel; US, unconventional spike; VGCC, voltage-gated Ca2+ channel.
