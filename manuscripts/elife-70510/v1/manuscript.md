# Pupil diameter is not an accurate real-time readout of locus coeruleus activity

## Authors

- Marine Megemont<sup>1</sup>
- Jim McBurney-Lin<sup>1</sup>
- Hongdian Yang<sup>1</sup> ([ORCID: 0000-0002-5203-9519](https://orcid.org/0000-0002-5203-9519)) †

### Affiliations

1. Department of Molecular, Cell and Systems Biology, University of California, Riverside Riverside United States
2. Neuroscience Graduate Program, University of California, Riverside Riverside United States

† Corresponding author

## Abstract

Pupil diameter is often treated as a noninvasive readout of activity in the locus coeruleus (LC). However, how accurately it can be used to index LC activity is not known. To address this question, we established a graded relationship between pupil size changes and LC spiking activity in mice, where pupil dilation increased monotonically with the number of LC spikes. However, this relationship exists with substantial variability such that pupil diameter can only be used to accurately predict a small fraction of LC activity on a moment-by-moment basis. In addition, pupil exhibited large session-to-session fluctuations in response to identical optical stimulation in the LC. The variations in the pupil–LC relationship were strongly correlated with decision bias-related behavioral variables. Together, our data show that substantial variability exists in an overall graded relationship between pupil diameter and LC activity, and further suggest that the pupil–LC relationship is dynamically modulated by brain states, supporting and extending our previous findings (Yang et al., 2021).

## Introduction

Fluctuations of brain states, such as arousal and attention, strongly impact sensory processing, decision-making, and animal behavior (Harris and Thiele, 2011; Lee and Dan, 2012; Thiele and Bellgrove, 2018; Petersen, 2019; McCormick et al., 2020). It is thus critical to understand the neural substrates of brain states and how state changes can account for the variability embedded in neuronal and behavioral data (Cano et al., 2006; Poulet and Petersen, 2008; Polack et al., 2013; Fu et al., 2014; Zagha and McCormick, 2014; Lee et al., 2020). Changes in pupil diameter under constant luminance are tightly linked to states of arousal and attention (McGinley et al., 2015a; Joshi and Gold, 2020). Dynamic pupil responses are associated with membrane potential fluctuations, sensory evoked responses, salience detection, error estimation, decision-making, and task performance (Kahneman and Beatty, 1966; Bijleveld et al., 2009; Nassar et al., 2012; de Gee et al., 2014; de Gee et al., 2020; Reimer et al., 2014; Vinck et al., 2015; McGinley et al., 2015b; Lee and Margolis, 2016; Schriver et al., 2018; Schriver et al., 2020; Kucewicz et al., 2018; Ebitz and Moore, 2019). As a result, pupil diameter has been widely used to monitor brain states and their neural substrates.

A multitude of neural circuits have been implicated in mediating brain state and pupil size changes, most notably the neuromodulatory systems (Yu and Dayan, 2005; Lee and Dan, 2012; Thiele and Bellgrove, 2018; Joshi and Gold, 2020). The locus coeruleus (LC)–noradrenergic system has long been thought to play a critical role in controlling arousal and attention (Aston-Jones et al., 1999; Berridge and Waterhouse, 2003; Aston-Jones and Cohen, 2005; Sara, 2009; Sara and Bouret, 2012), and LC activity closely tracks brain states and cognitive processes (Foote et al., 1980; Aston-Jones and Bloom, 1981; Berridge and Foote, 1991; Aston-Jones et al., 1994; Rajkowski et al., 1994; Usher et al., 1999; Takahashi et al., 2010; Carter et al., 2010; Eschenko et al., 2012; Vazey and Aston-Jones, 2014; Kalwani et al., 2014; Varazzani et al., 2015; Bouret and Richmond, 2015; Fazlali et al., 2016; Swift et al., 2018). Importantly, work mainly in the past decade has provided correlative and causal evidence linking pupil size changes to LC activity (Rajkowski et al., 1994; Murphy et al., 2014; Varazzani et al., 2015; Joshi et al., 2016; Reimer et al., 2016; de Gee et al., 2017; Liu et al., 2017; Breton-Provencher and Sur, 2019; Hayat et al., 2020; Privitera et al., 2020), leading to the increased utilization of pupil diameter as a noninvasive readout of LC (Aston-Jones and Cohen, 2005; Gilzenrat et al., 2010; Preuschoff et al., 2011; Konishi et al., 2017; Gelbard-Sagiv et al., 2018; Zhao et al., 2019; Aminihajibashi et al., 2020; Clewett et al., 2020). However, a few recent studies demonstrated that the correlation between pupil and LC could be neuron- and task epoch-specific (Joshi et al., 2016; Breton-Provencher and Sur, 2019; Yang et al., 2021), raising the possibility that pupil diameter can be dissociated from LC activity. To the best of our knowledge, we do not know to what extent pupil diameter is linked to LC activity. More importantly, we do not know whether and how pupil diameter can be used to make accurate inferences of LC activity on a moment-by-moment basis.

To address these questions, we recorded spiking activity from optogenetically tagged LC neurons simultaneously with pupil diameter in head-fixed mice trained to perform a tactile detection task (McBurney-Lin et al., 2020; Yang et al., 2021). We established a graded relationship between pupil and LC, where pupil dilation increased monotonically with LC spiking activity. However, this relationship exists with substantial variability such that pupil size changes can only accurately predict a small fraction of LC spiking on a moment-by-moment basis. Using optogenetics to activate LC neurons, we showed that pupil responses exhibited large session-to-session fluctuations to identical optical stimulation, despite stable LC responses. Notably, decision bias-related behavioral variables explained the variations in the pupil–LC relationship. Together, our data show that substantial variability exists in an overall positive relationship between pupil diameter and LC activity, and that only under limited conditions can pupil be used as an accurate real-time readout of LC. Our work further suggests that brain states dynamically modulate the coupling between pupil and LC.

## Results

We recorded spiking activity from optogenetically tagged single units in the LC together with pupil diameter in head-fixed mice during behavior (Figure 1a). To quantify a graded relationship between pupil size changes and LC spiking, we first grouped adjacent spikes into individual clusters (Hahn et al., 2010; Yu et al., 2017) based on each unit’s median interspike interval (Figure 1b, Figure 1—figure supplement 1, Methods). The magnitude of pupil responses following a spike cluster (quantified in a 6-s window from cluster onset) progressively increased with cluster size (the number of spikes in a cluster, Figure 1c, d). The latency of peak pupil diameter did not systematically vary with cluster size and ranged between 2.5 and 4 s (Figure 1—figure supplement 2). This latency is consistent with our previous report (Yang et al., 2021). Overall, we found a positive, monotonic relationship between peak pupil diameter and LC cluster size in the majority of paired recordings (linear regression R2 > 0.6 in 13 out of 19 paired recordings, Figure 1e), in line with previous findings in nonhuman primates (Varazzani et al., 2015; Joshi et al., 2016). Similar relationships held when pupil responses were quantified as % changes from baseline (Cazettes et al., 2021) or the time derivatives of pupil (Reimer et al., 2016; Yang et al., 2021; Figure 1—figure supplement 3). However, substantial variations existed in the relationship (linear slopes ranging from 0.12 to 0.51. 0.24 ± 0.11, mean ± standard deviation [SD], n = 13), indicating variable couplings between pupil and LC neurons.

![Figure 1.](https://cdn.elifesciences.org/articles/70510/elife-70510-fig1-v1.jpg)

**Figure 1.:** (a) Left: schematic of experimental setup for simultaneous pupil and LC recording/optical stimulation in head-fixed mice. Lightning bolt: light pulse. Right: expression of ChR2 in a DBH;Ai32 mouse (dopamine beta hydroxylase, DBH; ChR2-EYFP: green; tyrosine hydroxylase, TH: red). (b) Example simultaneously recorded LC spike raster and z-scored pupil diameter. Vertical black lines represent individual spikes. Horizontal magenta lines indicate spike clusters. (c) Example LC spike cluster-triggered pupil responses for cluster sizes 1, 4, and 7. (d) Mean LC cluster-triggered pupil responses (± standard error of the mean [SEM]) for cluster sizes 1 through 8 with occurrence (%) indicated in an example recording. (e) Left: the relationship between peak pupil diameter and LC cluster size for each paired recording. Curves with linear regression R2 > 0.6 are in black (n = 13), <0.6 in red (n = 4). Two recordings with limited cluster sizes (<3) were not suitable for linear regression and not included here. Right: histogram of the linear slopes for curves with R2 > 0.6. For f–h, the 13 recordings with R2 > 0.6 were included. (f) Histograms of area under the curve (AUC) values when using peak pupil diameter to predict the associated cluster sizes 1, 4, and 7. Magenta dot: mean. (g) Group mean AUC values when using peak pupil diameter to predict the associated cluster sizes 1 through 8. (h) Replot of (g) by showing the occurrence (abscissa) associated with each cluster size (gray scale).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/70510/elife-70510-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (a) Distribution of interspike interval, spike waveform (top) and spike sorting diagram (bottom) of three example recordings with median interspike interval (ISI, left to right: 0.20, 0.29, and 0.36 s) and spike duration (left to right: 0.23, 0.84, and 1.25 ms). Spike duration was quantified from trough to peak afterhyperpolarization (AHP). (b) Distribution of median interspike interval for 19 recordings. (c) Distribution of R2 values from linear regressing pupil–LC relationship in Figure 1e (n = 17, two recordings with limited cluster sizes [<3] were not suitable for linear regression and not included).

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/70510/elife-70510-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** c.c., Pearson correlation coefficient.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/70510/elife-70510-fig1-figsupp3-v1.jpg)

**Figure 1—figure supplement 3.:** The relationship between pupil size changes and LC spike cluster when pupil responses were quantified as % changes from baseline (a), time derivative (b), or using a shorter time window (3 s, c). Curves with linear regression R2 > 0.6 are in black, <0.6 are in red. Specifically, 13 recordings were identified with R2 > 0.6 in (a), and all were the same as the 13 recordings with R2 > 0.6 in Figure 1e; 9 recordings were identified with R2 > 0.6 in (b), and 8 out of 9 were from the 13 recordings in Figure 1e; 12 recordings were identified with R2 > 0.6 in (c), and all were from the 13 recordings in Figure 1e. In addition, only in 1 out of the 13 recordings (with R2 > 0.6 in Figure 1e) did the number of spikes occurring after a given cluster (in-between spikes) significantly correlate with LC cluster size or peak pupil diameter, and overall in-between spikes did not strongly correlate with LC cluster size (correlation coefficient = 0.35, p = 0.39) or peak pupil diameter (correlation coefficient = 0.29, p = 0.48). Together, these results strongly suggest that in-between spikes did not significantly contribute to the variability of the pupil–LC relationship.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/70510/elife-70510-fig1-figsupp4-v1.jpg)

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/70510/elife-70510-fig1-figsupp5-v1.jpg)

Although pupil diameter exhibited an overall monotonic relationship with LC spiking, it did not necessarily warrant pupil diameter being an accurate readout of LC activity. We tested the extent to which pupil size changes can be used as a proxy for LC activity, that is, can we use pupil diameter to make accurate inferences of LC spiking on a moment-by-moment basis? We asked how well an ideal observer (Green and Swets, 1966) can predict LC cluster size given the associated peak pupil responses (Methods). Receiver-operating-characteristic (ROC) analysis showed that as cluster size increased, peak pupil diameter can better predict LC activity (Figure 1f, g, Figure 1—figure supplement 4). However, only peak pupil diameter associated with large clusters (≥5–6 spikes) can achieve a performance threshold of d′ = 1 (translates to ~0.75 area under the curve Simpson and Fitter, 1973, Figure 1g). Since larger clusters occurred less frequently (Figure 1d, h, Figure 1—figure supplement 5), our data suggest that pupil dilation cannot accurately represent the majority of LC spiking activity but can serve as a good proxy for the infrequent (<10%) and strong LC activity in real time (Figure 1h).

Perhaps what is more interesting (and useful) is to assess whether we can directly use pupil diameter to infer the ‘ground truth’ – LC activity, without recording from LC. To do so, we first detected pupil dilation events based on zero-crossings of pupil derivatives (Joshi et al., 2016; Figure 2a) and quantified LC spike counts immediately preceding each dilation event (Methods). Compared with the analyses in Figure 1, this method did not require prior knowledge of LC activity for identifying pupil responses and yielded a similar pupil–LC relationship (Figure 2—figure supplement 1). Overall, LC spike counts were monotonically associated with pupil dilation amplitudes (Figure 2b–d). However, a wide range of spike counts preceded pupil events of similar sizes (Figure 2b, c). We asked how well an ideal observer can predict pupil dilation events given the associated LC activity and found that as pupil dilations became larger, LC spike counts could make better predictions on a moment-by-moment basis. However, only LC activity preceding the infrequent (<10%), large dilation events (>1.5–2 SD, Figure 2—figure supplement 2) performed beyond 75% threshold (Figure 2e). Finally, we tested how well we can use the detected pupil dilation events to predict LC activity. Similar to the previous results (Figure 1g), we found that only large pupil events can achieve good predictions (Figure 2f). Taken together, our data show that pupil diameter and LC spiking are well correlated in a graded manner and that the infrequent (<10%) but strong (>1.5–2 SD) pupil dilation events can be used to accurately and reliably predict LC activity in real time.

![Figure 2.](https://cdn.elifesciences.org/articles/70510/elife-70510-fig2-v1.jpg)

**Figure 2.:** (a) Example pupil–LC traces showing the detected pupil dilation events (blue arrows) based on zero-crossing of pupil derivatives. (b) Probability distributions of LC spike counts associated with pupil dilation events of similar sizes in an example recording. Magenta dot: mean. Pupil dilation events were binned every 0.3 standard deviation (SD). (c) Group mean probability distributions of LC spikes associated with pupil dilation events of similar sizes. Mean occurrences (%) of pupil dilation events were indicated. (d) Group mean relationship between LC spike counts and pupil dilation events binned every 0.3 SD from 0 to 3 SD. (e) Group mean area under the curve (AUC) values when using LC spike counts to predict the associated pupil dilation events binned every 0.3 SD from 0 to 3 SD. (f) Group mean AUC values when using the detected pupil dilation events to predict the associated LC spike counts 1 through 8, similar to Figure 1g.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/70510/elife-70510-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** Group mean relationship between peak pupil diameter and LC spike counts based on (1) clustering LC spikes then identifying the associated peak pupil responses (blue, Figure 1), and (2) detecting pupil dilation events then identifying the preceding LC spike counts (red, Figure 2).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/70510/elife-70510-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** Pupil dilation events were binned every 0.3 standard deviation (SD).

Our data presented so far were based on paired pupil–LC recordings, each consisting of a single opto-tagged LC unit. Next, we sought to test whether pupil size changes better reflect population-level LC activity instead of single neurons. To this end, we optogenetically activated groups of LC neurons and quantified the evoked pupil responses. Based on the stimulation parameters, we estimated an excitable volume on the order of 0.05–0.1 mm3, containing hundreds of LC neurons (Figure 3a, b, Figure 3—figure supplement 1, Methods). In a subset of experiments, the putatively same LC units were tracked (typically 1–5 days), based on opto-tagging, spike clustering, and waveform comparison (Figure 3c, d). Waveforms from the putatively same units were more similar than the waveforms from the putatively different units (Figure 3e–g). These putatively same units responded similarly to optical stimulation in different sessions (Figure 3h), suggesting a consistent transduction of optical stimulation to LC spiking activity. In contrast to stable LC responses, the same pupil exhibited variable dilations to optical stimulation under awake, nontask performing conditions (Figure 4a, b). Importantly, baseline pupil diameters were similar (0.71 vs. 0.75 mm, Figure 4—figure supplement 1) and thus cannot explain the differences in evoked pupil responses. Group data from multiple mice further demonstrated that significant session-to-session fluctuations of pupil responses were prevalent but not directional (solid lines in Figure 4c, d), that is, pupil responses in an earlier session (session 1) were not consistently higher or lower than in a later session (session 2). Therefore, such session-to-session fluctuations were not observable from group comparisons (Figure 4—figure supplement 2, Privitera et al., 2020). To further test whether the variable pupil responses were due to (1) weak LC stimulation with 10 ms pulses, or (2) strong spontaneous pupil fluctuations during wakefulness, we performed the following experiments. First, we evoked pupil responses with stronger stimulation (50 ms pulses instead of 10 ms) in the awake condition. While baseline pupil diameters were similar between sessions, evoked pupil responses still fluctuated significantly (Figure 4e, f). In a subset of experiments, pupil exhibited substantial fluctuations in two sessions just several hours apart (4–6 hr, magenta arrows in Figure 4c–f). Further analysis showed that across-session variability of pupil responses was comparable to within-session variability (Figure 4—figure supplement 3, Methods). In addition, for the paired sessions that exhibited significantly different responses to optical stimulation (solid lines in Figure 4c–f), only a small subset exhibited larger across-session variability than within-session variability (2 pairs out of 12 under 10 ms condition, and 3 pairs out of 11 under 50 ms condition, Methods). Next, we stimulated LC with 10 ms pulses under anesthesia (2% isoflurane) to minimize spontaneous pupil fluctuations (Figure 4—figure supplement 4). Evoked pupil responses were noticeably larger compared with the awake condition in the example recordings, possibly due to a more constricted baseline pupil size under anesthesia (Figure 4g, h, left vs. Figure 4a, b, 0.3 vs. 0.7 mm). Nevertheless, pupil responses to optical stimulation exhibited substantial session-to-session fluctuations (Figure 4g, h). Additional examples of a simultaneously recorded LC unit and pupil diameter in responses to optical stimulation are in Figure 4—figure supplement 5. In summary, pupil responses showed large session-to-session fluctuations to identical LC stimulation.

![Figure 3.](https://cdn.elifesciences.org/articles/70510/elife-70510-fig3-v1.jpg)

**Figure 3.:** (a) Example LC histological section illustrating optical fiber implant and the estimated excitable volume (light gray cone). Estimates were based on 10-mW laser power, 2.5 mW/mm2 excitation threshold, 1.4 refractive index, and a 30° cylindrical cone. (b) Example spiking activity (vertical lines) from an opto-tagged LC unit in response to 10-ms blue pulse trains at different frequencies. (c) Example traces (top, middle) and waveforms (bottom) from a putatively same LC unit in response to optical stimulation (cyan bars) in two different sessions (3 days apart). Black and blue indicate an earlier and a later session (sessions 1 and 2), respectively. Waveforms from the two sessions were highly similar with Pearson correlation coefficient (c.c.) = 0.97. (d) Spike sorting diagrams corresponding to the two sessions shown in (c). The unit was identified in Ch1. (e) Waveforms from another putatively same unit in two sessions (1 day apart, waveform c.c. = 0.95). (f) Waveforms from the 2 units shown in (c) and (e) were less similar (session 1 unit 1 vs. session 1 unit 2, c.c. = 0.75). (g) Among the tracked 5 units, waveforms from the putatively same units in sessions 1 and 2 (Same) were more similar than waveforms from the putatively different units in session 1 (Different. Same vs. Different, Pearson correlation coefficient (c.c.), 0.96 ± 0.02 vs. 0.82 ± 0.07, mean ± standard deviation (SD), p = 6.6e−4, two-tailed rank sum test). Gray dots: individual pair. Black dots: group mean. (h) Responses from the putatively same units to optical stimulation (S1 vs. S2) during awake, nontask performing (4 units, left) and anesthetized (5 units, right) conditions. p > 0.05 for each S1 vs. S2 comparison, permutation test. Evoked spike counts were quantified in response to (1) single 50 ms pulse (solid black line, 4 units); or (2) four 10 ms pulses at 10 Hz (solid gray line, 2 units); or (3) eight 10 ms pulses at 5 Hz (dashed gray line, 2 units).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/70510/elife-70510-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** The number of evoked spikes from an opto-tagged LC unit in response to optical stimulation using different laser power (single 10 ms pulse; left), or different pulse width (single pulse; right). Error bars may be too small to be visible.

![Figure 4.](https://cdn.elifesciences.org/articles/70510/elife-70510-fig4-v1.jpg)

**Figure 4.:** (a) Example responses from the same pupil to LC stimulation in two awake, baseline pupil-matched sessions (left and right) aligned to the onset of optical stimulation of four 10 ms pulses at 10 Hz. Thin curves: individual responses; thick curves: mean. Baseline pupil diameter S1 vs. S2, 0.71 vs. 0.75 mm. p values were based on permutation test. (b) Same as in (a), except that optical stimulation was eight 10 ms pulses at 10 Hz. (a, b) were from the same recording. (c) Group data showing pupil responses to optical stimulation of four 10 ms pulses at 10 Hz in awake, baseline pupil-matched sessions (12 paired sessions from 6 mice). To aid visualization, pupil responses in session 2 were normalized to session 1. Unnormalized data in Figure 4—figure supplement 2. Dots: mean peak pupil responses. Vertical lines: 95% confidence interval. Solid lines indicate significant difference (p < 0.05, permutation test). Session 1 always preceded session 2. Magenta arrows indicate same-day comparison. (d) Group data showing pupil responses to optical stimulation of eight 10 ms pulses at 10 Hz in awake, baseline pupil-matched sessions (11 paired sessions from 7 mice). Unnormalized data in Figure 4—figure supplement 2. Conventions are as in (c). (e, f) Left: example pupil responses from one recording. Conventions are as in (a, b), except that optical stimulations consisted of 50 ms pulses instead of 10 ms, and that pupil responses from the two sessions were overlaid. Baseline pupil diameter S1 vs. S2, 0.83 vs. 0.80 mm. Right: group pupil responses as in (c, d), except that optical stimulations consisted of 50 ms pulses instead of 10 ms. 9 paired sessions from 7 mice in (e), and 9 paired sessions from 7 mice in (f). Magenta arrows indicate same-day comparison. (g, h) Left: example pupil responses from one recording. Conventions are as in (a, b), except that the mouse was under anesthesia (2% isoflurane), and that pupil responses from the two sessions were overlaid. Baseline pupil diameter S1 vs. S2, 0.31 vs. 0.35 mm. Right: group pupil responses as in (c, d), except that mice were under anesthesia. 7 paired sessions from 3 mice in (g), and 8 paired sessions from 3 mice in (f).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/70510/elife-70510-fig4-figsupp1-v1.jpg)

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/70510/elife-70510-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** Session-to-session fluctuations were not observable from group comparisons. p = 0.38, n = 12 for (a) and p = 0.63, n = 11 for (b). Magenta arrows indicate same-day comparison.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/70510/elife-70510-fig4-figsupp3-v1.jpg)

**Figure 4—figure supplement 3.:** (a) p = 0.53, p = 0.58. (b) p = 0.22, p = 0.15. Two-tailed rank sum test. Across-session variability was estimated by resampling pooled trials from all sessions in each condition. The iteration of resampling matched the number of sessions in that condition.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/70510/elife-70510-fig4-figsupp4-v1.jpg)

**Figure 4—figure supplement 4.:** (a) The amplitude of spontaneous pupil dilation events in awake, nontask performing condition was larger than in anesthetized condition (five sessions from three mice in each condition, p = 0.0079, two-tailed rank sum test). Gray dots: individual sessions. Red and black dots: group mean. (b) The frequency of significant spontaneous pupil dilation events (>0.3 standard deviation [SD]) was higher in awake, nontask performing condition than in anesthetized condition (5 sessions from 3 mice in each condition, p = 0.0079, two-tailed rank sum test). Gray dots: individual sessions. Red and black dots: group mean.

![Figure 4—figure supplement 5.](https://cdn.elifesciences.org/articles/70510/elife-70510-fig4-figsupp5-v1.jpg)

**Figure 4—figure supplement 5.:** Simultaneous recording of an LC unit waveform (a), spike responses (b), and pupil diameter (c) during optogenetic stimulation (10 ms pulse train: four pulses at 10 Hz [top] and eight pulses at 5 Hz [bottom] under anesthesia). Baseline pupil diameter S1 vs. S2, 0.34 vs. 0.32 mm.

![Figure 4—figure supplement 6.](https://cdn.elifesciences.org/articles/70510/elife-70510-fig4-figsupp6-v1.jpg)

**Figure 4—figure supplement 6.:** (a, b) ISI distribution and spike waveform from all recordings, ranked by increasing median ISI. Pupil–LC relationship with R2 > 0.6 (as in Figure 1e) in (a, n = 13), and the remaining in (b, n = 6). All waveforms were plotted on the same scales as shown in the first panel. Each trial lasted 5–6 s, which likely contributed to the peak on the right side of some ISI distributions (e.g., magenta arrow in the last panel of (b)). (c) Average firing rate vs. spike duration (trough to peak AHP). Black dots represent the group in (a), gray dots represent (b). We note that both narrow and wide waveforms were present, supporting recent work (Totah et al., 2018). We did not quantify the width of four waveforms in (a, indicated by *) as their reversed polarity with prominent initial positive deflection indicated that the recording sites were in the more distal axonal or dendritic regions of neurons where mixed-ion capacitive current became more profound (Barry, 2015; Gold et al., 2006; Rall and Shepherd, 1968; Sun et al., 2021). Their firing rates were between 1 and 3 spikes/s.

What may underlie the variable pupil responses? We found that the variations in the relationship between peak pupil diameter and LC cluster size (as in Figure 1e) were strongly correlated with hit rate and decision bias during task performance (Figure 5a). This effect was not likely due to linear fitting of nonlinear relationships (all linear fits are of R2 > 0.85. 0.92 ± 0.05, mean ± SD, n = 9), and the results held when the analysis of pupil–LC relationship was restricted to nonlicking periods only (Figure 5b, Methods). Therefore, although mice licked more during sessions of higher hit rate and lower decision bias, the results cannot be fully explained by a potentially stronger pupil–LC coupling during licking periods. Based on these findings, we conclude that decision bias-related behavioral variables could explain, at least in part, the variations in the pupil–LC relationship. Since fluctuations of these behavioral variables reflect state changes such as impulsivity, motivation, and task engagement (Dickinson and Balleine, 1994; Mayrhofer et al., 2013; Berditchevskaia et al., 2016; Allen et al., 2019; McBurney-Lin et al., 2020), our results suggest that the coupling between pupil and LC is state dependent.

![Figure 5.](https://cdn.elifesciences.org/articles/70510/elife-70510-fig5-v1.jpg)

**Figure 5.:** (a) The variations in the relationship between peak pupil diameter and LC cluster size (linear slopes in Figure 1e) were strongly correlated with Hit rate (left) and decision bias (right, n = 9). c.c., Pearson correlation coefficient. (b) The relationships in (a) held when pupil–LC slopes were quantified in nonlicking periods only.

## Discussion

In the current study, we have shown that pupil diameter has an overall positive and monotonic relationship with LC spiking activity. However, substantial variability exists in this relationship that only the infrequent and large pupil dilation events (>1.5–2 SD amplitude, <10% occurrence) can accurately predict LC spiking on a moment-by-moment basis. In addition, pupil responses exhibit large session-to-session fluctuations to identical optical stimulation in the LC. Decision bias-related behavioral variables could explain the variations in the pupil–LC relationship. Together, our results strongly caution treating pupil dilation as a real-time readout of LC activity. Averaging multiple repeats/trials of similar pupil responses would yield a much more accurate prediction of LC activity.

We used two methods to establish the pupil–LC relationship: detecting LC activity then linking to the following pupil responses (Figure 1); and detecting pupil dilation then linking to the preceding LC activity (Figure 2). Both methods yielded similar pupil–LC relationships with the conclusion that only the infrequent, large pupil responses can accurately predict LC spiking on a moment-by-moment basis. Large pupil or LC responses have been reported to correlate with a variety of task-related processes, including sensory cue, decision formation, positive feedback, choice bias, and action (Rajkowski et al., 1994; Usher et al., 1999; Kalwani et al., 2014; Bouret and Richmond, 2015; de Gee et al., 2017; de Gee et al., 2020; Schriver et al., 2020; Yang et al., 2021). In light of this, our work suggests that the infrequent but strong pupil dilation events can be used as an accurate inference of LC activation in response to sensory stimuli and decision-making processes. However, as discussed below, in general pupil and LC likely respond to task-related processes differently, leading to variations in their relationship.

Recent evidence has uncovered considerable heterogeneity within the LC nucleus, including molecular compositions, physiological properties, released transmitters, and projection targets (Robertson et al., 2013; Chandler et al., 2014; Chandler et al., 2019; Schwarz and Luo, 2015; Schwarz et al., 2015; Kempadoo et al., 2016; Hirschberg et al., 2017; Uematsu et al., 2017; Totah et al., 2018; Borodovitsyna et al., 2020). Our data support these findings (Figure 4—figure supplement 6). Therefore, it is possible that pupil diameter is dynamically coupled with different LC subgroups that are differentially engaged during cognitive processes. However, this is insufficient to explain the session-to-session fluctuations of pupil responses to LC stimulation, since we likely activated a heterogenous group of LC neurons that exhibited similar session-to-session responses to optical stimulation.

The fact that the putatively same neurons tracked across days exhibited similar responses to optical stimulation cannot fully establish the long-term stability of population LC response because slow changes in the tissue due to tetrode/optical fiber implant (gliosis, inflammation, etc.) could alter light transmission to the neurons that were not recorded. However, several lines of evidence in our study did not favor this possibility: (1) Pupil responses in a later session did not systematically or progressively differ from an earlier session (e.g., consistently larger or smaller, Figure 4—figure supplement 2); (2) Significant pupil response variability can be observed in sessions that were a few hours apart (Figure 4); (3) Across-session variability of pupil responses was largely comparable to within-session variability (Figure 4—figure supplement 3). However, optogenetic stimulation tends to synchronize neuronal activity, which may not reflect the physiological condition (Totah et al., 2018). Future experiments with the ability to record from multiple opto-tagged LC neurons simultaneously will further investigate the relationship between pupil diameter and population-level LC activity.

During wakefulness, the state of the brain is constantly fluctuating, both in the presence and absence of external stimuli (Kenet et al., 2003; Fox et al., 2006; Fox and Raichle, 2007; Sakata and Harris, 2009; Luczak et al., 2009; Berkes et al., 2011; Harris and Thiele, 2011; Mohajerani et al., 2013; Romano et al., 2015; Petersen, 2019; McCormick et al., 2020). Pupil response profiles can reflect different behavioral processes (Schriver et al., 2020), and pupil responses also can be dissociated from cognitive processes (Podvalny et al., 2019). Our data extend these observations, supporting that LC and pupil respond to behavioral and cognitive variables differently (Yang et al., 2021).

Fluctuations of hit rate and decision bias reflect state changes such as impulsivity, motivation, and task engagement (Dickinson and Balleine, 1994; Mayrhofer et al., 2013; Berditchevskaia et al., 2016). Although mice licked more during high motivation or high engagement trials (Berditchevskaia et al., 2016; Allen et al., 2019; McBurney-Lin et al., 2020), our data show that licking alone cannot account for the tight correlation between the variations of the behavioral variables and the variations in the pupil–LC relationship (Figure 5), suggesting that pupil–LC coupling is brain state dependent.

How may brain states modulate pupil–LC coupling? Pupil size changes have been linked to activity in other brain areas and neuromodulatory systems, including the medial prefrontal cortex, the inferior colliculus, and cholinergic signaling (Joshi et al., 2016; Reimer et al., 2016; Okun et al., 2019; Kucyi and Parvizi, 2020; Pais-Roldán et al., 2020; Sobczak et al., 2021). A recent study found that pupil responses to dorsal raphe stimulation exhibited task uncertainty-dependent variations (Cazettes et al., 2021). Therefore, it is possible that in high motivation/engagement states, multiple circuits including the LC synergistically influence pupil size changes, resulting in the apparently stronger pupil–LC coupling. Future experiments are needed to elucidate how pupil and LC interact with these brain circuits during different behavioral contexts and cognitive processes.

Another possibility is that higher engagement states may be intimately associated with more ‘uninstructed’ movements as revealed by recent work (Musall et al., 2019), which can drive robust neuronal activity throughout the brain (Musall et al., 2019; Steinmetz et al., 2019; Stringer et al., 2019; Salkoff et al., 2020). Future studies with comprehensive movement monitoring will determine whether more frequent movements, both task-related and task-unrelated, during periods of high motivation/engagement underlie the stronger pupil–LC coupling.

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
      <td>Strain, strain background (M. musculus)</td>
      <td>DBH-Cre</td>
      <td>MMRRC</td>
      <td>RRID:MMRRC_036778-UCD</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (M. musculus)</td>
      <td>Ai32</td>
      <td>JAX</td>
      <td>RRID:IMSR_JAX:012569</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>BControl</td>
      <td>Princeton University</td>
      <td>https://brodylabwiki.princeton.edu/bcontrol</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>WaveSurfer</td>
      <td>HHMI Janelia</td>
      <td>http://wavesurfer.janelia.org/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Matlab</td>
      <td>MathWorks</td>
      <td>RRID:SCR_001622</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Janelia eye tracker</td>
      <td>HHMI Janelia</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>StreamPix</td>
      <td>Norpix</td>
      <td>RRID:SCR_015773</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Illustrator</td>
      <td>Adobe</td>
      <td>RRID:SCR_010279</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Camera</td>
      <td>PhotonFocus</td>
      <td>DR1-D1312-200-G2-8</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Telecentric lens</td>
      <td>Edmund Optics</td>
      <td>55–349</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Tetrode drive</td>
      <td>Cohen et al., 2012</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-TH primary antibody</td>
      <td>Thermo Fisher</td>
      <td>OPA104050 RRID:AB_325653</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Secondary antibody</td>
      <td>Thermo Fisher</td>
      <td>A11008 RRID:AB_2534079</td>
      <td>1:500</td>
    </tr>
  </tbody>
</table>

All procedures were performed in accordance with protocols approved by UC Riverside Animal Care and Use Committee. Mice were DBH-Cre (B6.FVB(Cg)-Tg(Dbh-cre) KH212Gsat/Mmucd, 036778-UCD, MMRRC); Ai32 (RCL-ChR2(H134R)/EYFP, 012569, JAX), or DBH-Cre injected with AAV5-EF1α-DIO-hChR2(H134R)-EYFP (UNC Vector Core), singly housed in a vivarium with reverse light–dark cycle (12 hr each phase). Male and female mice of 8–12 weeks were implanted with titanium head posts as described previously (Yang et al., 2016). Procedures for microdrive construction and LC recording have been described previously (Yang et al., 2021). Briefly, custom microdrives with eight tetrodes and an optic fiber (0.39 NA, 200 µm core) were built to make extracellular recordings from LC neurons. Microdrive was implanted in the left LC. LC neurons were identified by optogenetic tagging of DBH+ neurons expressing ChR2, tail pinch response, and post hoc electrolytic lesions (Yang et al., 2021). For Figures 1 and 2, 19 single unit recordings (cluster quality measure Lratio: 0.01 ± 0.005; firing rate: 1.65 ± 0.25 spikes/s; percent ISI <10 ms: 0.11% ± 0.1%) from 7 mice performing the single-whisker detection task (see below) were extracted using MClust (Redish, 2014), among which six recordings were from our previous dataset (Yang et al., 2021). For Figure 3, 5 units from 5 mice were tracked over time (between 1 and 5 days). For Figure 4, 68 pupil sessions (34 baseline pupil-matched session pairs) to LC stimulation were acquired from 8 mice, 4 of which were implanted with an optical fiber only (0.39 NA, 200 µm core), and the time between sessions 1 and 2 was 4.4 ± 0.9 days. At the conclusion of the experiments, brains were perfused with PBS followed by 4% paraformaldehyde, postfixed overnight, then cut into 100-μm coronal sections and stained with anti-tyrosine hydroxylase antibody (Thermo Fisher OPA1-04050).

Behavior task was controlled by BControl (C. Brody, Princeton University) or custom-based Arduino hardware and software as described previously (Yang et al., 2016; Yang et al., 2021; McBurney-Lin et al., 2020). In brief, mice were trained to perform a head-fixed, Go/NoGo single-whisker detection task, in which mice reported whether they perceived a brief deflection (0.5 s, 40 Hz or 0.2 s, 25 Hz sinusoidal deflection) to the right C2 whisker by licking toward a water port. A 0.1-s auditory cue (8 kHz tone, ~80 dB SPL) was introduced starting 1–1.5 s before stimulus onset. During all sessions, ambient white noise (cutoff at 40 kHz, ~80 dB SPL) was played through a separate speaker to mask any other potential auditory cues associated with movement of the piezo stimulator. Video of the left pupil (ipsilateral to LC recording and stimulation) was acquired at 50 Hz using a PhotonFocus camera and StreamPix 5 software, or at 20 Hz using a Basler acA1300-200 µm camera and Pylon software. 450 nM blue diode lasers (UltraLasers, MDL-III-450–200 mW) controlled by WaveSurfer (https://www.janelia.org/open-science/wavesurfer) were used for optogenetic stimulation. Electrophysiology, pupil tracking, and optogenetic stimulation were synchronized via a common TTL pulse train. The mating sleeve connecting two ferrules was covered with black tape to prevent light leak. An ambient blue LED was used to constrict the pupil and to mask any potential light leak. <15 mW (RMS) of blue light was measured at the tip of optical fiber. We estimated an excitable volume on the order of 0.05–0.1 mm3 for a 30° cylindrical cone based on 10-mW light power, 2.5 mW/mm2 excitation threshold and 1.4 refractive index of brain tissue (Boyden et al., 2005; Sun et al., 2012) (brain tissue light transmission calculator: https://web.stanford.edu/group/dlab/cgi-bin/graph/chart.php), containing hundreds of neurons in the LC. Stimulation patterns were delivered every 10–30 s and randomized.

For Figure 1, in each recording if the interval between two adjacent spikes was shorter than median inter-spike interval of that unit, the spikes were grouped into a single cluster. Using other time windows (0.1–0.5 s) to group spikes did not affect this analysis for the majority of recordings (data not shown). Peak pupil dilation was defined as the absolute maximum value in a 6-s window following the onset of each cluster (time of the first spike). ROC analysis in Figure 1f–h was performed between peak pupil diameter associated with clusters of a given size and number-matched, randomly selected pupil diameter. For Figure 2, pupil traces were first smoothed with a 500-ms window to avoid false-positive slope detections. Pupil slopes were then estimated every 200 ms, and a pupil dilation event was defined as the maximum pupil size between sequential positive zero-crossings of the slopes (Joshi et al., 2016). For each dilation event, LC spikes were quantified in a −2 to −4 s window from the event. Using a −1 to −3 s window did not affect this analysis (data not shown). Pupil dilation events falling in a bin of 0.3 SD were considered of similar sizes. ROC analysis in Figure 2e was performed between LC spike counts associated with pupil dilation events of a similar size and LC spike counts associated with number-matched, randomly selected pupil sizes. ROC analysis in Figure 2f was performed the same way as in Figure 1. For Figure 4, pupil responses in each session were first bootstrapped 100 times with replacement to estimate the mean and confidence interval.Pupil responses to the same optical stimulation were pooled from the two different sessions, and then randomly assigned to session 1 or 2 with replacement. The reported p value represented the proportion of iterations where mean peak pupil responses from the two permutated sessions exceeded the observed difference from 1000 iterations. For Figure 5, 9 recordings (out of 13 shown in Figure 1e) from 4 mice during behavior were included with >100 trials and R2 > 0.6. For Figure 5b, LC clusters occurring within ±0.5 s from each licking event were excluded from analyzing the pupil–LC relationship as in Figure 1e. This window was chosen based on previous results that LC spiking peaked within a few hundred milliseconds of licking onset (Yang et al., 2021). For Figure 4—figure supplement 3, across-session variability (standard deviation of peak pupil responses) was estimated by resampling trials pooled from all sessions in each condition. The iteration of resampling matched the total number of sessions in that condition. To test whether within-session variability was similar to across-session variability for individual session pairs which exhibited significantly different pupil responses, we first estimated the distribution of across-session variability by resampling trials pooled from both sessions for 1000 iterations and examined whether the variability of individual sessions fell outside 5% of the distribution.

Data were reported as mean ± standard error of the mean unless otherwise noted. We did not use statistical methods to predetermine sample sizes. Sample sizes are similar to those reported in the field. We assigned mice to experimental groups arbitrarily, without randomization or blinding.
