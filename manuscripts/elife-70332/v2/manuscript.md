# Partial response electromyography as a marker of action stopping

## Authors

- Liisa Raud<sup>1</sup> ([ORCID: 0000-0003-2355-4308](https://orcid.org/0000-0003-2355-4308)) †
- Christina Thunberg<sup>2</sup>
- René J Huster<sup>2</sup>

### Affiliations

1. Center for Lifespan Changes in Brain and Cognition, Department of Psychology, University of Oslo Oslo Norway ([ROR:01xtthb56](https://ror.org/01xtthb56))
2. Cognitive and Translational Neuroscience Cluster, Department of Psychology, University of Oslo Oslo Norway ([ROR:01xtthb56](https://ror.org/01xtthb56))
3. Multimodal Imaging and Cognitive Control Lab, Department of Psychology, University of Oslo Oslo Norway ([ROR:01xtthb56](https://ror.org/01xtthb56))

† Corresponding author

## Abstract

Response inhibition is among the core constructs of cognitive control. It is notoriously difficult to quantify from overt behavior, since the outcome of successful inhibition is the lack of a behavioral response. Currently, the most common measure of action stopping, and by proxy response inhibition, is the model-based stop signal reaction time (SSRT) derived from the stop signal task. Recently, partial response electromyography (prEMG) has been introduced as a complementary physiological measure to capture individual stopping latencies. PrEMG refers to muscle activity initiated by the go signal that plummets after the stop signal before its accumulation to a full response. Whereas neither the SSRT nor the prEMG is an unambiguous marker for neural processes underlying response inhibition, our analysis indicates that the prEMG peak latency is better suited to investigate brain mechanisms of action stopping. This study is a methodological resource with a comprehensive overview of the psychometric properties of the prEMG in a stop signal task, and further provides practical tips for data collection and analysis.

## Introduction

Response inhibition, or the ability to stop actions, is a core construct of cognitive control and is widely studied among cognitive and clinical neuroscientists. Most of our knowledge about inhibitory capability is derived from a single behavioral measure, the stop signal reaction time (SSRT), which quantifies the time the stopping process needs to countermand an already initiated action. SSRTs are slower in patients with attention deficit/hyperactivity disorder, obsessive compulsive disorder, drug abuse, schizophrenia, Parkinson’s disease, and Tourette syndrome among others (Jahanshahi et al., 2015; Lipszyc and Schachar, 2010; Smith et al., 2014; Snyder et al., 2015; Wylie et al., 2013; Yaniv et al., 2017). However, accumulating evidence suggests that SSRT estimations may be unreliable in many practical settings (Bissett et al., 2021b; Bissett and Logan, 2014; Matzke et al., 2017; Skippen et al., 2019; Verbruggen et al., 2013). Here, we scrutinize electromyography (EMG) recordings from the muscles that are successfully stopped as a potential physiological marker to capture individual differences in action stopping.

The stop signal task is among the most common experimental tasks used to study inhibition, with more than 7000 publications using the task in the last years (Verbruggen et al., 2019). The principle of the task is very simple: participants react repeatedly to a go signal with a button press but need to inhibit this response when a stop signal appears after the go signal with a variable delay (stop signal delay, SSD). The resulting go reaction time distribution, probability of responding despite stop signal presentation, and the resulting SSDs are the necessary variables for calculating the SSRT.

The SSRT estimation is based on the independent race model (or horse race model), in which go and stop processes independently race against each other, and whichever process wins this race, determines whether a planned action will be executed or not (Band et al., 2003; Logan and Cowan, 1984). The theoretical basis of the model is well established and an extension of this model also has biological plausibility (Boucher et al., 2007). However, recent work indicates that SSRT estimates may be inaccurate in many practical cases, for example due to extensive slowing of go responses (Verbruggen et al., 2013), violations of the independence assumptions at short SSDs (Bissett et al., 2021b), or failures to initiate the stop process (Skippen et al., 2019). The available solutions focus on the derivation of putatively improved SSRT estimates, either by refining the estimation method (Verbruggen et al., 2019), discarding participants or trials that show obvious violations of the model assumptions (Bissett et al., 2021a; Bissett et al., 2021b), or by proposing alternative modelling approaches (Heathcote et al., 2019; Matzke et al., 2017; Matzke et al., 2013). However, the field has been in a remarkable standstill when it comes to the development of complementary measures that could potentially bypass issues related to model assumptions in the first place.

A notable exception is the proposition to derive a more direct measure of the stopping latency from EMG. Specifically, EMG recorded at the effector muscles that generate the response can be used to capture the time-point when the motor activity begins to decline in the muscles. In many successfully stopped trials (trials without a registered response), surface EMG recordings still capture small bursts of muscle activity. These bursts are presumably responses initiated after the go signal that are stopped before the muscle activity culminates in a button press. We have termed these responses partial response EMG (prEMG; see Box 1 for visualization and reflections on the naming). The proposition to use the peak latency of the prEMG as an indicator of an individual’s stopping speed seems to have originated independently in two different laboratories (Atsma et al., 2018; Raud and Huster, 2017). Raud and Huster used surface EMG from thumb muscles in a selective stop signal task and measured the prEMG peak latency to be about 150 ms, which was significantly shorter than the corresponding SSRT of about 200 ms. Atsma et al. used intramuscular recordings of the upper-limb muscle during reaching movements. They reported a prEMG offset latency (the time-point when muscle activity returned to the baseline level) at 165 ms, compared with an SSRT of 244 ms. While their methods and goals were different, both studies showed that the EMG-derived stopping latency was much faster than that of the model-based SSRT.

While using the prEMG latency as an index of stopping capability is a relatively recent suggestion, recording EMG in a stop signal task is not particularly novel by itself. Earlier work identified that muscle activity can be stopped at any time before the movement is completed, and additionally focused on the time-courses of different electrophysiological measures, that is EMG, electrocardiography, and electroencephalography (EEG; de Jong et al., 1990; Jennings et al., 1992; van Boxtel et al., 2001). These studies identified the motor cortex as a site of inhibition, yet they showed that the peripheral nervous system is affected as well. Several studies have attempted to interpret the prEMG within the context of the horse race model. For instance, trials with prEMG seem to roughly correspond to the middle part of the go-RT distribution, indicating that these trials have a relatively fast go process that nonetheless is slow enough to be suppressed by the stop process (de Jong et al., 1990; van Boxtel et al., 2001). Furthermore, the occurrence of the prEMG is dependent on the SSD, as prEMG frequency declines and its amplitude increases with increasing SSD (Coxon et al., 2006). Interestingly, EMG in unsuccessful stop trials may be affected by the stop process as well, as these trials exhibit lower EMG amplitudes, but prolonged motor times (the time between EMG onset and the registered response) compared with standard go responses (van de Laar et al., 2014). This violates the assumption of independence underlying the independent horse race model, which states that unsuccessful stop trials are drawn from the distribution of fast go responses and should therefore be unaffected by the stop signal. The dependence of go and stop processes was recently directly shown by Raud et al., 2020a who found a positive correlation between go-locked prEMG onsets and stop-locked prEMG peak latencies at the level of single stop trials.

The earlier timing of the prEMG peak latency compared to the SSRT has been replicated in a number of independent studies (Hannah et al., 2020; Jana et al., 2020; Raud et al., 2020a; Raud et al., 2020b; Sundby et al., 2021; Tatz et al., 2021; Thunberg et al., 2020). However, while the existence of the prEMG is relatively well established, its characteristics and utility have not been explored sufficiently. We therefore present a thorough investigation of the prEMG in the stop signal task. Importantly, we treat prEMG as a marker of action stopping only, without specifically linking it to inhibitory brain mechanisms, as mechanisms other than active inhibition may cause cessation in muscle activity too. This separation between action stopping and response inhibition holds for the SSRT as well, but is often overlooked in the literature, in which the stop runner in the horse race model is frequently interpreted as an active process to counteract the go process. Nonetheless, as the SSRT and the prEMG have been previously associated with the same underlying neural mechanisms, we benchmark the prEMG peak latency against the SSRT and the existing horse race model framework; investigate potential relationships between response onset, stopping, and the SSD at a single-trial level; present novel information about stopping variability; and estimate the reliability of the EMG measures. We additionally provide practical tips for data collection and analysis, accompanied by publicly available analysis code that can easily be adjusted to new datasets. With that, we demonstrate the full potential of prEMG with the aim to encourage and accelerate future studies to adopt it as a standard outcome measure of supposed inhibition tasks.

## Results

### Behavior and EMG in a stop signal task

We analyzed surface EMG recorded over the thumb muscles (abductor pollicis brevis) from 46 healthy young adults who performed a standard stop signal task. The primary task was a choice reaction time task where participants had to respond to a go signal either with a left or right hand button press (Figure 1A). In 24% of the trials, a stop signal occurred instructing the participants to stop their response. The full analysis pipeline was additionally applied to a publicly available dataset provided by Jana et al., 2020 to replicate the current results. The main difference between these two datasets was the proportion of trials with prEMG of successful stop trials, which was relatively low (~20%) in the discovery, but higher (~60%) in the replication dataset. With a few minor exceptions, the results were the same in both datasets. Therefore, we report the results obtained on the discovery dataset, and only report the replication results when these deviate from the discovery dataset results. The complete replication results are available in Appendix 1.

![Figure 1.](https://cdn.elifesciences.org/articles/70332/elife-70332-fig1-v2.jpg)

**Figure 1.:** (A) Task depiction; (B, C) electromyography (EMG) time-courses, time-locked to (A) go signal onset, (B) EMG onset, and (C) stop signal onset. The lines depict averaged activity and the shaded areas depict 95% confidence intervals across participants. sstop – successful stop; ustop – unsuccessful stop.

The behavioral results (Table 1) were in line with previous studies, with stopping accuracies at 50% and an SSRT (integration method with RT replacement for go omissions) of 199 ms. We also estimated behavioral parameters using the Bayesian Ex-Gaussian Estimation of Stop Signal Distribution approach accounting for go and trigger failures (BEESTS; Matzke et al., 2019; Matzke et al., 2013), which resulted in an SSRT of 202 ms (Table 1).

**Table 1.**
 Behavioral and BEESTS parameters summary statistics.Table 1—source data 1.Behavioral data.Table 1—source data 2.BEESTS data.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Mean</th>
      <th>sd</th>
      <th>Median</th>
      <th>min</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Behavior</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Go accuracy (%)</td>
      <td>97.92</td>
      <td>2.21</td>
      <td>98.76</td>
      <td>91.23</td>
      <td>100.00</td>
    </tr>
    <tr>
      <td>Go errors (%)</td>
      <td>0.69</td>
      <td>0.88</td>
      <td>0.37</td>
      <td>0.00</td>
      <td>5.12</td>
    </tr>
    <tr>
      <td>Go omissions (%)</td>
      <td>1.40</td>
      <td>1.95</td>
      <td>0.73</td>
      <td>0.00</td>
      <td>8.04</td>
    </tr>
    <tr>
      <td>Go RT (ms)</td>
      <td>545.28</td>
      <td>77.11</td>
      <td>549.04</td>
      <td>398.29</td>
      <td>715.24</td>
    </tr>
    <tr>
      <td>SSD (ms)</td>
      <td>347.50</td>
      <td>97.59</td>
      <td>349.53</td>
      <td>155.71</td>
      <td>551.60</td>
    </tr>
    <tr>
      <td>SSRT (ms)</td>
      <td>198.99</td>
      <td>29.63</td>
      <td>202.00</td>
      <td>120.05</td>
      <td>263.97</td>
    </tr>
    <tr>
      <td>Stop accuracy (%)</td>
      <td>49.88</td>
      <td>1.84</td>
      <td>50.46</td>
      <td>43.06</td>
      <td>54.17</td>
    </tr>
    <tr>
      <td>Unsuccessful stop RT (ms)</td>
      <td>480.47</td>
      <td>70.85</td>
      <td>496.64</td>
      <td>351.11</td>
      <td>671.92</td>
    </tr>
    <tr>
      <td>BEESTS parameters</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Go failures (%)</td>
      <td>1.56</td>
      <td>2.18</td>
      <td>0.76</td>
      <td>0.04</td>
      <td>9.12</td>
    </tr>
    <tr>
      <td>Trigger failures (%)</td>
      <td>1.27</td>
      <td>1.62</td>
      <td>0.51</td>
      <td>0.28</td>
      <td>8.94</td>
    </tr>
    <tr>
      <td>Go RT (mean; ms)</td>
      <td>546.51</td>
      <td>78.83</td>
      <td>548.71</td>
      <td>396.93</td>
      <td>722.25</td>
    </tr>
    <tr>
      <td>Go RT (sd; ms)</td>
      <td>113.52</td>
      <td>28.97</td>
      <td>112.25</td>
      <td>65.57</td>
      <td>167.46</td>
    </tr>
    <tr>
      <td>SSRT (mean; ms)</td>
      <td>201.83</td>
      <td>21.39</td>
      <td>200.03</td>
      <td>166.22</td>
      <td>248.85</td>
    </tr>
    <tr>
      <td>SSRT (sd; ms)*</td>
      <td>30.70</td>
      <td>13.38</td>
      <td>27.69</td>
      <td>14.94</td>
      <td>86.55</td>
    </tr>
  </tbody>
</table>

EMG bursts were identified automatically using a threshold-based algorithm (see Box 2 and Materials and methods for details). EMG bursts were detected in 99% of go trials and 98% of unsuccessful stop trials. Note that while 100% detection rate is expected in those trials, variations in signal quality (increased baseline muscle tone, unrelated movement artifacts, etc.) led to slight conservative bias in the detection algorithm. PrEMG was detected in 23% of successful stop trials.

Averaged EMG waveforms for each trial type are shown in Figure 1 and the summary statistics are presented in Table 2. When time-locked to go signal onset, the trials with a registered button press showed large EMG activity (Figure 1B). Note that go-locked averaging over varied SSDs causes a smeared waveform for prEMG. We used Bayesian hypothesis testing to compare the EMG onset latencies and peak amplitudes between trial types. This confirmed that the EMG onsets were earlier in unsuccessful stop trials than in go trials (BF = 1.32 × 1024) and that prEMG onset latencies were similar to the EMG onset latencies in go trials (BF = 0.28). When time-locked to the EMG onset (Figure 1C), the rising flanks of the EMG waveforms were remarkably similar across all trials but reached very different amplitudes. The peak amplitudes in successful stop trials were considerably smaller than in go (BF = 2.77 × 1029) and unsuccessful stop trials (BF = 1.91 × 1027). Interestingly, EMG amplitudes in unsuccessful stop trials were also smaller than those in go trials (BF = BF = 2.32 × 107), suggesting that the former were affected by stop signal processing despite the registered button press.

**Table 2.**
 Means (and standard deviations in brackets) of the electromyography (EMG) variables.Table 2—source data 1.EMG summary data.


<table>
  <thead>
    <tr>
      <th>Variable</th>
      <th>Go</th>
      <th>Succ. stop</th>
      <th>Unsucc. stop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Count</td>
      <td>655 (25)</td>
      <td>23 (13)</td>
      <td>106 (5)</td>
    </tr>
    <tr>
      <td>Percentage</td>
      <td>99 (2)</td>
      <td>23 (14)</td>
      <td>98 (2)</td>
    </tr>
    <tr>
      <td>Onset latency (ms)</td>
      <td>487 (81)</td>
      <td>481 (91)</td>
      <td>422 (74)</td>
    </tr>
    <tr>
      <td>Peak latency* (ms)</td>
      <td>NA (NA)</td>
      <td>165 (31)</td>
      <td>99 (37)</td>
    </tr>
    <tr>
      <td>Peak amplitude (z)</td>
      <td>12 (1)</td>
      <td>4 (1)</td>
      <td>11 (1)</td>
    </tr>
    <tr>
      <td>Motor time (ms)</td>
      <td>57 (13)</td>
      <td>NA (NA)</td>
      <td>58 (14)</td>
    </tr>
    <tr>
      <td>Rise time (ms)</td>
      <td>52 (10)</td>
      <td>19 (5)</td>
      <td>48 (9)</td>
    </tr>
    <tr>
      <td>AUC (z)</td>
      <td>142 (18)</td>
      <td>31 (12)</td>
      <td>125 (16)</td>
    </tr>
  </tbody>
</table>

When time-locked to stop signal onset, a very clear prEMG waveform appeared (Figure 1D), which started declining at 165 ms after the stop signal. A similar decline also occurred in unsuccessful stop trials, although they peaked slightly earlier at 99 ms after the stop signal (BF = 3.47 × 1012). Speculatively, the steep decline of the falling flank seen in unsuccessful stop trials may suggest that unsuccessful stop trials were also affected by the processes triggered by the stop signal around the same time as the prEMG decline in successful stop trials.

We additionally quantified motor time, that is the difference between the EMG onset and the RT, and the rise time, that is the duration of the EMG burst from its onset to peak (relative to go signal). Even though the differences are numerically small (Table 2), the motor time was longer in unsuccessful stop trials than in go trials (BF = 5.94; replicating the finding of van de Laar et al., 2014). When go trials were divided into fast, medium, and slow trials (see paragraph about the assessment of contextual independence for details on this division), the motor times increased with increasing RTs, so that slow go-trial motor times were equivalent to unsuccessful stop trial motor times (BF = 0.16). The motor time results deviated somewhat in the replication dataset, which had generally much longer motor times at 118 ms. While motor times still increased with increasing RT in go trials, the unsuccessful stop trial motor times were equivalent with the medium part of the go distribution (BF = 0.39), resulting in equivalence also with the full distribution (BF = 0.17). The absolute rise times were also longer in the replication dataset (ranging between 30 and 60 ms for different conditions), but they were shorter in unsuccessful stop trials than in go trials in both datasets (discovery BF = 1.16 × 106; replication BF = 3.93 × 105). Altogether, these results indicate different response dynamics in unsuccessful stop trials and go trials, suggesting that unsuccessful stop trials may be affected by the stop process as well. However, this may be contingent on task procedure and even on the response device mechanics. Here, we used a response device with very little resistance to produce a button press, resulting in very small motor times and low proportion of trials with prEMG. Nonetheless, the replication dataset with longer motor times and a higher prEMG proportion still indicates different response dynamics in go and unsuccessful stop trials.

### Associations of prEMG peak latency and frequency with behavior

In many studies, the SSRT has been reported as a single behavioral outcome measure of the stop signal task, purportedly reflecting the speed of response inhibition. However, recent evidence indicates that both SSRTs and prEMG peak latencies are related to go RTs, potentially due to behavioral adaptations beyond response inhibition (Huster et al., 2020). We therefore investigated the correlational structure of the prEMG and other behavioral measures, both across individuals in the current study and across different experiments by performing a meta-analysis. Given that the major caveat of the prEMG is that it is only present in a portion of successful stop trials, we further investigated whether its peak latency is affected by the proportion of available trials.

Firstly, goRTs correlated strongly with the SSRTs (r = −0.61, p = 1.62 × 10−5) and moderately with the prEMG latencies (r = −0.33, p = 0.027). Secondly, goRTs correlated moderately with the prEMG detection frequency (r = −0.35, p = 0.018). The relationships between prEMG frequency and stopping latency indices were not significant (SSRT r=0.23, p = 0.127; prEMG peak latency r = 0.27, p = 0.065). In sum, persons who responded fast had more prEMG trials and longer stopping latencies, likely due to a strategic trade-off between going and stopping. Noticeably, this trade-off seems to be best captured by the associations between the goRT and the SSRT.

Next, we quantified these relationships across 21 different experiments or conditions as reported in 10 studies (Figure 2). Despite the large variability of goRTs across the studies (range 246 ms), the prEMG peak latency was surprisingly stable (range 35 ms) and averaged to 158 ms with an average detection frequency of 49% (see Table 3 for more descriptive statistics). Given that most articles reported several experiments or task conditions, relationships between prEMG and behavior were tested using general mixed models with article as a random variable (but the relationships were the same if the average value across conditions and experiments was used for each study; Figure 2E). The strong negative association between go RTs and SSRTs seen across individuals was also evident across studies (b = −2.08, t(19) = −2.65, p = 0.012), as was the smaller association between the go RTs and prEMG peak latencies (b = −1.33, t(11) = −2.21, p = 0.049). Similarly, studies with faster go RTs reported higher prEMG detection frequencies (b = −2.03, t(15) = −2.96, p = 0.010). Interestingly, while every single study reported a positive correlation between the prEMG and the SSRT with an average correlation of r = 0.64 (standard deviation covering the range from 0.44 to 0.78 across studies after Student z- and retransformation; Figure 2D), this relationship was not particularly strong across studies, reaching significance only after discarding an obvious outlier (b = 0.34, t(11) = 2.29, p = 0.044). Most importantly, while prEMG detection frequency varied considerably across studies (between 23% and 70% of stop trials), it was not associated with its peak latency (b = 0.14, t(19) = 0.91, p = 0.375).

![Figure 2.](https://cdn.elifesciences.org/articles/70332/elife-70332-fig2-v2.jpg)

**Figure 2.:** (A–D) Means and standard deviations (error bars) of each entry, ordered by go RTs. The error bars around the y-entry ‘Mean’ represent standard deviations across studies. (E) Associations between behavioral and EMG variables across studies. The dots reflect each separate condition/experiment study, color coded by the studies they originate from. The dashed gray lines represent bivariate regression lines, and the solid black lines represent the fixed effects of the general linear mixed model, accounting for the fact that single studies have more than one entry. The regression lines for the stop signal reaction time (SSRT)-prEMGlat plot are calculated excluding the outlier at top left. Note that the entry marked Raud et al., 2021 represent the data from current study.

**Table 3.**
 Meta-analysis behavioral and electromyography (EMG) values across 21 different conditions or experiments in 10 independent studies. prEMG = partial response electromyography; SSRT = stop signal reaction time.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Mean</th>
      <th>sd</th>
      <th>Median</th>
      <th>min</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Go RT (ms)</td>
      <td>486</td>
      <td>79</td>
      <td>493</td>
      <td>400</td>
      <td>646</td>
    </tr>
    <tr>
      <td>SSRT (ms)</td>
      <td>217</td>
      <td>16</td>
      <td>216</td>
      <td>194</td>
      <td>259</td>
    </tr>
    <tr>
      <td>prEMG frequency (%)</td>
      <td>49</td>
      <td>16</td>
      <td>47</td>
      <td>23</td>
      <td>70</td>
    </tr>
    <tr>
      <td>prEMG peak/offset latency (ms)</td>
      <td>158</td>
      <td>11</td>
      <td>160</td>
      <td>139</td>
      <td>174</td>
    </tr>
    <tr>
      <td>SSRT and prEMG latency difference (ms)</td>
      <td>60</td>
      <td>18</td>
      <td>57</td>
      <td>35</td>
      <td>120</td>
    </tr>
  </tbody>
</table>

### Comparison of prEMG peak latency and different SSRT estimates

There are several different ways to calculate the SSRT. The two state-of-the-art techniques are the integration method with replacement of go omissions (Verbruggen et al., 2019), and the Bayesian parametric approach (Heathcote et al., 2019; Matzke et al., 2013), which has been extended to incorporate go errors and failures to trigger both the go and the stop process (Matzke et al., 2019; Matzke et al., 2017). Where some studies show prevalent trigger failures and considerably faster BEESTS-SSRTs than integrations-SSRTs (Skippen et al., 2020; Skippen et al., 2019), others find a lower incidence of trigger failures and correspondingly little change in SSRT estimates (Jana et al., 2020). In line with the latter, we found the different SSRT estimates to be comparable in this dataset (BF = 0.34). Both were considerably slower than the prEMG peak latency (integration BF = 9.6 × 105, BEESTS BF = 2.6 × 109). Both SSRTs correlated moderately with the prEMG peak latency (integration r = 0.51; BEESTS r = 0.57 for prEMG derived from single trials, but see Box 2 for differences in correlations with different prEMG peak latency estimations). Consistent with previous studies, the delay between the prEMG and the SSRT (integration) was 33 ms (sd = 33). This did not correlate with the prEMG detection frequency (r = 0.04).

### Comparison of behavior- and EMG-based inhibition functions

Having established the basic summary characteristics and their (non-)correspondence with the SSRT, we set out to investigate how the prEMG relates to the framework of the horse race model of going and stopping. A feature of the stop signal task is that the SSD varies, most commonly due to an online tracking algorithm that adapts the SSDs to each participant’s performance. The purpose of this is to capture the SSD where participants manage to stop their response for about 50% of the time. A key assumption of this approach is that the probability of unsuccessful stopping (p(button press|stop)) is low (approaching zero) at short SSDs, increases steeply at mid-SSDs, and approaches one at long SSDs. With EMG, this would correspond to the probability of producing EMG at any given stop trial (i.e., p(EMG|stop)), as this implies that the go process was at least initiated before stopping process. This probability thus includes all stop trials with detectable EMG, and is conceptually the sum of unsuccessful stop trials and successful stop trials with prEMG. Thus, by definition, the function of p(EMG|stop) should be shifted to the left from the function of p(button press|stop). In addition, assuming that the successful stop trials with prEMG are drawn uniformly from the distribution of successful stop trials, we would expect the two functions to run in parallel. However, preliminary evidence suggests that prEMG occurs more often at short SSDs (Coxon et al., 2006; de Jong et al., 1990). Given that p(EMG|stop) represents the sum of unsuccessful stop trials and successful stop trials with prEMG, this would lead to larger differences between the two functions at short than in long SSDs.

The empirical inhibition functions are depicted on Figure 3. To capture the expected nonlinear shape of the functions, we fit a generalized additive mixed model (GAMM), predicting the probability of responding (p(button press|stop)) or producing EMG (p(EMG|stop)) despite a stop signal as a function of SSD (model R2 = 0.64); this model thus also allows for the assessment of the interaction of response type (button, EMG) and SSD. The effect of SSD was significant (df = 3.18, F = 213.91, p < 2 × 10−16), as was the parametric effect of response type (b = 0.07, t = 9.52, p < 2 × 10−16). Further, the interaction term was significant (df = 1.00, F = 6.795, p = 0.009), as the difference between detecting a button press compared to an EMG response was larger at smaller SSDs. Since p(EMG|stop) contains p(button press|stop) as well successful stop trials with prEMG, these effects indicate that prEMG was more common in trials with short SSDs.

![Figure 3.](https://cdn.elifesciences.org/articles/70332/elife-70332-fig3-v2.jpg)

**Figure 3.:** Error bars represent 95% confidence intervals. Note that the error bars are calculated across all trials and participants, ignoring that each participant has several data points.

### Context independence of going and stopping

A key assumption of the horse race model is that the go and stop processes are independent of each other. In particular, the context independence assumption states that the stop process does not affect the primary go process, thus the distribution of the go-finishing times (estimated by go RTs) is identical in the go and stop trials (Band et al., 2003). We applied two tests of this assumption to both the behavioral and EMG data.

The most common test compares the mean go RT with the mean RT of unsuccessful stop trials. If response activation is identical in the go and stop trials, the unsuccessful stop trial distribution is censored at the right side; it thus follows that the mean RTs should be shorter in unsuccessful stop trials than in go trials. This was true in our data both for RTs (BF = 1.53 × 1024) and EMG onset latencies (BF = 1.32 × 1024).

However, a more stringent test directly compares the equivalence of the corresponding portions of the response time distributions in go and stop trials. Dividing the go-RT distribution at the percentile corresponding to p(button press|stop, SSD) gives an estimate of the distribution of trials for a given SSD in which the go process would or would not escape the stop process. Specifically, the portion at the left of this division are the fast go trials that would escape inhibition, and the portion on the right are slow go trials that would be stopped. We found that the mean unsuccessful stop trial RTs were not equivalent to the mean of the left side of the go-RT distribution (mean = 470 ms, sd = 72; BF = 1542). Since the means of the fast go-RT portions may misrepresent the central values, we repeated the analysis using median values instead. Here, we did find the participant-specific medians of the left side of the go-RT distribution equivalent to the unsuccessful stop trial RTs in the discovery set (BF = 0.53), but not in the replication dataset (BF = 34,849).

This test has been extended to the EMG onset latencies, deriving an additional division line using the percentile corresponding to p(EMG|stop, SSD) (de Jong et al., 1990; Jennings et al., 1992; van Boxtel et al., 2001). Figure 4 explains the key expectations. Adhering to the independent horse race model, we expected EMG onsets in unsuccessful stop trials to match fast go-EMG onsets. Then, as the p(EMG|stop) is larger than p(button press|stop), there is a second division line derived from the percentile corresponding to p(EMG|stop), which is shifted to the right. The trials between those two lines should correspond to successful stop trials with prEMG. Consequently, the mean go-EMG onset latencies from trials between these two division lines should be equal to the prEMG onsets. Lastly, the go-EMG onsets to the right of the second dividing line should be slower than the prEMG onsets.

![Figure 4.](https://cdn.elifesciences.org/articles/70332/elife-70332-fig4-v2.jpg)

**Figure 4.:** The histogram depicts the distribution of EMG onsets in go trials, and the vertical lines mark (from left to right) the go signal onset, stop signal onset (mean stop signal delay [SSD]), percentile corresponding to the probability of producing a response and to the probability of producing EMG in stop trials. Assuming stochastic independence of go and stop trials, unsuccessful stop trials should correspond to the fast go trials (left side of the distribution between go signal and p(press|stop)), while partial response electromyography (prEMG) should correspond to the middle partition of the go distribution in between the p(press|stop) and p(EMG|stop).

The EMG onset latencies, averaged over all trials within each partition of the go-EMG distribution, are listed in (Table 4). The data indicate a deviation from the independence assumption already for the left side of the distribution, as the average EMG onset in unsuccessful stop trials was slower than the average EMG onset in fast go trials (BF = 2.67 × 109). Secondly, the average prEMG onsets were faster than the corresponding average onset of the middle partition of the go-EMG distribution (BF = 2.17 × 104), which contrasts the prediction that these should be roughly equivalent. Lastly, the slow go-EMG onsets occurred later than the prEMG onsets, as expected (BF = 2.81 × 1021). These patterns remained the same if medians were used instead of means. To confirm that the results are not affected by sampling differences due to having more go trials than stop trials, we repeated this analysis by randomly sampling matching numbers of fast go and medium go trials for each participant and doing t-tests on these subsamples (on average 105 and 23 trials, correspondingly) 1000 times. The pattern of results stayed the same every single time. These results indicate that extending the horse race model to the EMG is not applicable and, consequently, estimating the SSRT based on go-EMG distributions should be avoided.

**Table 4.**
 EMG onsets in go trials divided into fast (between go onset and p(press|stop)), medium (between p(press|stop) and p(EMG|stop)) and slow (> p(EMG|stop)) trials.Table 4—source data 1.prEMG onset data.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Mean</th>
      <th>sd</th>
      <th>Median</th>
      <th>min</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>goEMG_fast</td>
      <td>401</td>
      <td>67</td>
      <td>410</td>
      <td>260</td>
      <td>555</td>
    </tr>
    <tr>
      <td>goEMG_medium</td>
      <td>506</td>
      <td>80</td>
      <td>500</td>
      <td>347</td>
      <td>678</td>
    </tr>
    <tr>
      <td>goEMG_slow</td>
      <td>608</td>
      <td>108</td>
      <td>582</td>
      <td>416</td>
      <td>844</td>
    </tr>
    <tr>
      <td>usEMG</td>
      <td>422</td>
      <td>74</td>
      <td>430</td>
      <td>272</td>
      <td>596</td>
    </tr>
    <tr>
      <td>prEMG</td>
      <td>481</td>
      <td>91</td>
      <td>474</td>
      <td>290</td>
      <td>701</td>
    </tr>
  </tbody>
</table>

Even though the EMG onset patterns do not seem to be in accordance with the assumption of the horse race model, it is important to determine the prEMG characteristics across all SSDs to establish whether stopping estimates based on the prEMG are representative of the overall stopping behavior. Based on previous findings, we expected the prEMG frequency to decline and its amplitude to increase with increasing SSD. Further, as go RTs tend to correlate positively with the SSDs, we expected that the prEMG onset latencies (calculated relative to the go signal) would increase with SSDs as well. Note that the prEMG peak latency, in contrast, is calculated relative to the stop signal and thus reflects the speed of the stop process. Critically, it has never been asked whether the prEMG peak latency remains stable at different SSDs.

We fit four GAMMs to predict the prEMG probability, onsets, amplitudes, and peak latencies from the SSDs (Figure 5). As expected, prEMG probability decreased with the SSD (df = 1.92, F = 24.28, p = 2.47 × 10−10, R2 = 0.09). Similarly, we found increased EMG onsets with increasing SSD (df = 2.60, F = 420.7, p < 2.00 × 10−16, R2 = 0.36). The prEMG peak latencies decreased with SSD (df = 2.29, F = 11.77, p = 9.71 × 10−6, R2 = 0.06), indicating that stopping may be slower at short SSDs. PrEMG amplitudes increased slightly with longer SSDs, with the smooth term at the border of significance (df = 1.66, F = 4.16, p = 0.056, R2 = 0.02).

![Figure 5.](https://cdn.elifesciences.org/articles/70332/elife-70332-fig5-v2.jpg)

**Figure 5.:** The upper panels represent empirical data across all participants. Green lines represent the group average with 95% confidence intervals and gray lines represent each participant. The lower panels depict the model fit of the generalized additive models with 95% confidence intervals. Note the different y-axes between empirical data and model fits.

### prEMG peak latency as a function of time on task

Another important question is whether prEMG remains stable across the experiment. It is possible that inhibition becomes automatic over time and loses its cognitive control element (Best et al., 2016; Verbruggen et al., 2014; Verbruggen and Logan, 2008). Consequently, prEMG peak latency may decrease after practice. We tested this by fitting a GAMM model predicting prEMG peak latency by trial order while controlling for SSD (model R2 = 0.04), but we found no evidence that the trial order would affect prEMG peak latency (df = 1.173, F = 0.11, p = 0.843). We also tested whether the trial order affected prEMG frequency by predicting the existence of prEMG in a given trial from the trial order using logistic regression (while controlling for the SSD), but this model yielded no trial order effects either (df = 1.00, χ2 = 0.87, p = 0.350). Note that these results do not exclude that stopping may be automatic to begin with nor that automatism affects underlying processing (Raud et al., 2020b; Verbruggen et al., 2014), but simply indicates that stopping performance did not change with practice in a single session.

### Single-trial associations of prEMG onset latency, peak latency, and area under the curve

A clear advantage of the prEMG is that it allows to study the dynamics of going and stopping at a single-trial level. A simplified set of predictions outlining different dependencies between going and stopping are depicted in Figure 6, based on prEMG onset latencies (go-locked), peak latencies (stop-locked), and areas under the curves (AUC) from onset to peak. The AUC integrates the latency and amplitude of each prEMG burst and was calculated as the cumulative sum of point-wise amplitudes from onset to peak latency. Note that these scenarios are constructed assuming stable SSDs. This simplification helps to delineate the expected outcomes for different a priori hypotheses regarding the dependencies between going and stopping at the single-trial level.

![Figure 6.](https://cdn.elifesciences.org/articles/70332/elife-70332-fig6-v2.jpg)

Scenario 1 represents the independent horse race model, where there is considerable variability of the go process, but a constant and independent stop process. In this case, earlier prEMG onset leads to a larger AUC, but peak latencies are stable and independent of the onsets and AUCs.

Scenario 2 represents a case where delayed prEMG onset is associated with delayed prEMG peak latencies (as reported in Raud et al., 2020a), resulting in stable AUCs. This could be due to instances like competing resources for go and stop processes or attentional lapses that delay overall processing.

Scenario 3 represents a different dependency between the go and stop processes, in which more potent motor responses (i.e., earlier onsets and larger AUC) are associated with delayed stopping. This would result in a negative relationship between prEMG onset and peak latencies and between the onset latencies and AUCs, but a positive relationship between the peak latencies and the AUCs.

We tested these scenarios by fitting GAMMs predicting (1) peak latency from onset latency, (2) peak latency from AUC, and (3) onset latency from AUC. Onset latencies and SSDs correlated highly at the single-trial level (r = 0.88). To account for this, we predicted onsets from the SSDs for each participant and used the residuals instead of original onset values. AUCs were log transformed since the original values were extremely skewed toward low values.

The data showed evidence for scenario 2 (Figure 7) with a strong positive relationship between onset and peak latencies (estimated degrees of freedom [edf] = 3.47, F = 1957, p < 2 × 10−16, R2 = 0.72). There was also a small negative association between onset latencies and the AUCs (edf = 1.00, F = 29.25, p = 7.93 × 10−8, R2 = 0.03). In the discovery dataset, there was no relationship between peak latencies and AUCs (edf = 1.00, F = 0.09, p = 0.77, R2 < 0.001), while the replication dataset showed a very small negative association (edf = 1.00, F = 12.96, p = 0.0003, R2 < 0.001). As such, there was strong evidence for dependencies between going and stopping at the single-trial level, where delayed going was associated with delayed stopping. Note that none of these relationships were significant at the group level (i.e., taking the mean for each variable for each participant and fitting the same models), thus these results apply for single-trial data only.

![Figure 7.](https://cdn.elifesciences.org/articles/70332/elife-70332-fig7-v2.jpg)

**Figure 7.:** The dots represent single trials from all participants. The black lines represent the fixed effect model fits from generalized additive mixed models, where the individual variability was modeled as separate intercepts for each participant. The shaded areas represent 95% confidence intervals.

### prEMG variability

Until now, most previous studies focused on a single estimate of the peak latency of the prEMG. However, prEMG allows for the calculation of the standard deviation of the peak latency for each individual; we can therefore empirically capture the variability of single-trial stopping latencies for each individual (Jana et al., 2020). A caveat here is that that we detect prEMG only in a fraction of the trials, hence the variability estimates are truncated and likely biased. Nonetheless, the prEMG standard deviations show a considerable variability across participants and may therefore be informative of individual differences (Figure 8A). The average individual standard deviation was 31 ms (group-level sd = 21) and varied from 7 to 90 ms. Note that four outliers with values above two interquartile ranges were discarded from this analysis (see Appendix 2—figure 1 for visualization of the outliers).

![Figure 8.](https://cdn.elifesciences.org/articles/70332/elife-70332-fig8-v2.jpg)

**Figure 8.:** (A) Density functions of prEMG peak latency across all trials and participants (left panel) and separately for group of participants with low, medium, and large individual standard deviations (sd; right panels). (B) Correlation matrix between individual prEMG standard deviations (prEMGsd), number of prEMG trials (prEMGn), go reaction time standard deviations (goRTsd), average root mean square EMG amplitudes during the intertrial interval −200 to 0 before go stimulus onset (RMSmean), and standard deviations of the stop signal reaction time (SSRT) calculated through the BEESTS method (SDbeest). The diagonal shows the histograms for each variable together with the density functions, the lower diagonal shows the scatterplots, and the upper diagonal shows the Spearman correlation coefficients. prEMG reliability.

To understand the variability measure better, we first considered whether the between-participant variability could be driven by nuisance factors, such as the number of prEMG trials per person or the amount of baseline noise in the EMG. Secondly, it is possible that the variability of the stopping latency simply reflects variability in general processing, which can simply be assessed through the analysis of plain go responses without any need for a stopping variability measure. Therefore, we correlated the variability of the prEMG peak latency with the variability of the go RTs, where a low correlation would indicate that stopping variability gives information beyond the variability seen in go responses. The correlation matrix is depicted in Figure 8B. Note that we are reporting all correlation coefficients from this exploratory analysis with p values uncorrected for multiple comparisons, as the effect sizes are more informative about potential relationships than their significance.

The individual variability in prEMG peak latency correlated moderately with the number of prEMG trials (r = 0.30, p = 0.05), but showed no associations with baseline EMG noise (r = 0.06, p = 0.72) or go-RT variability (r = −0.01, p = 0.94). Lastly, we replicated the moderate positive correlation reported by Jana et al., 2020 between the prEMG variability and the variability of the SSRT calculated using the BEESTS method (r = 0.40, p = 0.01). The correlational structure did not change if four outliers were included in the data, nor when the analysis was confined to participants with more than 10 prEMG trials. The data thus suggest that an individual’s standard deviation of the prEMG peak latency provides complementary information on individual differences in stopping behavior.

### prEMG reliability

An important question for individual differences research is whether we can reliably estimate the prEMG characteristics despite the varying number of available trials per participant. We therefore estimated the split-half reliability of the prEMG-based latency and amplitude measures (Table 5), using a permutation-based split-half reliability approach (Parsons et al., 2019). Using all available trials and participants, we found high reliability for latency measures (0.94 and 0.87 for the prEMG onset and peak latency, respectively) but somewhat lower reliability for the prEMG peak amplitude and AUC (0.51 and 0.48, respectively). The same pattern was observed in the replication dataset, with even higher reliability coefficients for latency measures (0.98 and 0.92 for onset and peak latency, respectively).

**Table 5.**
 Split half reliability estimates for prEMG characteristics, including mean, standard deviation, and percentiles derived from the permutation distributions that correspond to the 95% confidence intervals.Table 5—source data 1.Reliability data.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Mmean</th>
      <th>sd</th>
      <th>2.5th</th>
      <th>97.5th</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Onset latency (ms)</td>
      <td>0.94</td>
      <td>0.01</td>
      <td>0.91</td>
      <td>0.97</td>
    </tr>
    <tr>
      <td>Peak latency (ms)</td>
      <td>0.87</td>
      <td>0.05</td>
      <td>0.75</td>
      <td>0.94</td>
    </tr>
    <tr>
      <td>Peak RMS amplitude (z)</td>
      <td>0.51</td>
      <td>0.13</td>
      <td>0.22</td>
      <td>0.71</td>
    </tr>
    <tr>
      <td>AUC (z)</td>
      <td>0.48</td>
      <td>0.11</td>
      <td>0.24</td>
      <td>0.68</td>
    </tr>
  </tbody>
</table>

A critical question for further research is how many trials and participants are necessary for reliable prEMG estimates. For instance, it may seem reasonable to exclude participants with few prEMG trials from further analysis. Yet, this could be harmful for the overall power due to increased standard errors across participants. We therefore repeated the split-half reliability analysis, sampling the lowest number of trials available for all participants and increasing the number of trials while excluding participants if they did not have the necessary number of trials available. This procedure resulted in incremental reliability estimates starting with 46 participants with 6 trials and ending with 12 participants with 32 trials (Figure 9). Interestingly, the reliability estimates for prEMG onset latency remained high (above 0.8) no matter the reduction in the number of trials and/or participants. prEMG peak latency reliability increased with the number of trials and reached a plateau around 0.77 after around 13 trials (with increased confidence intervals as the number of participants decreased). As before, the reliability estimates for amplitude measures did not show good reliability, with values hovering around 0.25 and decreasing even further with fewer participants.

![Figure 9.](https://cdn.elifesciences.org/articles/70332/elife-70332-fig9-v2.jpg)

**Figure 9.:** Green shaded areas represent 95% confidence intervals for the reliability estimates, and the black dashed horizontal line represent a reliability value of 0.7 for reference. Note the different y-axes for latency and amplitude measures. AUC = area under the curve from prEMG onset to peak.

In sum, we conclude that the latency measures of prEMG have overall good reliability, while amplitude-based measures do not. While reliability measures are affected by the specifics of each dataset, our data suggest an optimal minimal number of trials to be around 15, and more is always better. However, the reliability estimates were highest when all participants (even those with less than 10 trials) were included. Thus, excluding participants based on low number of available trials is not strictly necessary and may cause more harm by increasing the group-level standard errors and thereby reducing statistical power.

## Discussion

We analyzed prEMG from a standard stop signal task to investigate its utility and reliability as a marker of action stopping. We compared it thoroughly to the best-established marker of stopping latency, the SSRT. Further, we evaluated whether prEMG supports the horse race model that underlies the SSRT estimation in nearly all studies using the stop signal task. We also provided practical tips for EMG data acquisition and analysis (Box 2 and Box 3). We found that prEMG provides unique information about stopping and that assumptions of the horse race model may not regularly be met, questioning the broad and often undifferentiated use of the SSRT as a single indicator of stopping performance.

### The independent horse race model and prEMG

Several results from our analysis indicate incompatibility of the prEMG with the horse race model. On the one hand, we replicated the results from de Jong et al., 1990, who demonstrated that prEMG trials correspond to trials in the go-trial distribution that are fast enough to initiate muscle activity, but slow enough to not outrun the stopping process. On the other hand, neither unsuccessful stop trials nor successful stop trials with prEMG matched the corresponding partitions of the go-EMG distributions. This indicates that the horse race model framework should not be extended to the go-EMG distribution. Furthermore, prEMG peak latency varied with the SSD, indicating that stopping latency is not stable. Lastly, the single-trial analysis indicated a major violation of the horse race model independence assumption, as the go process (measured by the go-locked prEMG onset latency) and the stop process (measured by the stop-locked prEMG peak latency) share about 70% of variance if the SSD is accounted for. Together, these results add to the increasing pool of evidence which suggests that the independent horse race model is not an appropriate approximation of the stopping performance in practice.

### Comparison of the prEMG peak latency and the SSRT

There are three main findings when comparing the prEMG with the SSRT. First, the prEMG peak latency occurs earlier than the SSRT. Second, the prEMG correlates moderately to highly with the SSRT. Third, prEMG frequency and latency distributions show that the horse race model assumptions do not hold in practice, particularly in trials with short SSDs. This begs the question of whether prEMG and SSRT reflect the same underlying mechanism, and if not, how should these measures be interpreted?

The most parsimonious explanation would be that the prEMG and the SSRT capture the same conceptual construct – action stopping – but they simply reflect different stages in the cascade of events. The prEMG peak latency leads the SSRT by 60ms with an average correlation of r = 0.64 across studies. The 60ms delay between the myographic (prEMG peak latency) and behavioral (SSRT) measures may reflect the final ballistic component of the movement, the so-called point of no return, after which initiated movements are unaffected by any higher-order control mechanism (Osman et al., 1986). In this case, the prEMG may simply reflect the inertia in the neuromuscular system and response device presiding after the prepared movement has been stopped in the cortex (Gopal and Murthy, 2016; Jana et al., 2020). However, several lines of evidence challenge this explanation. First, such ‘leakage’ EMG has been shown to have a milder rising slopes compared to the normal go-EMG responses (McGarry and Franks, 2003; McGarry and Franks, 1997). In the current study, the EMG onset slopes were identical for all trial types (Figure 1B). Second, even with a moderate-to-strong association across all studies, correlation of prEMG and SSRTs varies considerably between studies. With explained variances ranging from about 10% to 60%, there remains plenty of unexplained variance even for the studies with the highest correlations. Third, the correlational structure with other behavioral and electrophysiological measures derived from the stop signal task differ greatly between the prEMG and the SSRT, where the latter exhibits a correlational structure indicative of an association with a trade-off between fast going and accurate stopping (Huster et al., 2020).

To account for the observed differences between the prEMG and the SSRT, we propose that both reflect the latency of action stopping to some degree, but that the SSRT is additionally affected by behavioral strategies and is thus more dependent on the task context. In support of this, the SSRT correlates negatively with go RTs, both across individuals in a single study, as well as across different studies. Whereas the prEMG detection frequency is also affected by task characteristics, evidenced by the correlations with go RTs, the primary outcome of interest, the peak latency, is relatively stable across different studies.

In sum, the prEMG peak latency captures action stopping speed and its variability across single trials. The SSRT likely captures action stopping to some degree but it is further affected by strategic behavioral adaptations and inaccuracies due to violations of the horse race model’s assumptions.

### Generalizability of the prEMG peak latency

The generalizability of the prEMG is potentially hampered by the fact that it appears only in a fraction of trials. The prEMG latency distribution is a truncated representation of the distribution of the underlying stopping process, lacking trials in which actions were stopped cortically before muscle activation or in which go process was not initiated in the first place. The prEMG distribution is thus affected by two interacting processes – action generation and action stopping. The current dataset does not allow us to test which of these processes is dominating.

To estimate the potential effect of the missing trials, we tested whether the prEMG frequency is associated with other behavioral and EMG measures across participants and studies. First, participants and studies with faster RTs produced more prEMG trials, but there was no relationship between the prEMG frequency and peak latency. Of note, faster RTs were associated with longer stopping latencies, and this relationship was particularly strong for the SSRT. Second, whereas prEMG was detected only in a minority of 20% trials in our data, most of our results were replicated in an independent dataset where 60% of successful stops contained prEMG. Third, the split-half reliabilities of the prEMG latency measures were high even for a small number of trials. Altogether, the fact that the prEMG distribution is truncated does not invalidate its use as a marker of action stopping, since the peak latencies are relatively stable despite the varying number of trials available for its estimation.

Nonetheless, as the contribution of the missing prEMG trials is unknown, it may still be argued that the available trials do not represent ‘typical’ stop trials. However, stopping actions may be achieved by different underlying mechanisms across different tasks, as well as within the same task across different trials. As such, whether there exists a ‘typical stop-trial’ is an empirical question that the prEMG can provide answers to. This can be achieved by (1) optimizing task design to produce more prEMG trials, for example by encouraging fast responding, using a response device with stiff buttons, or using an anticipated response task that discourages response slowing (Coxon et al., 2006; MacDonald et al., 2014); (2) requiring multicomponent movements and/or using antagonist muscle onsets as proxy of stopping latency in each trial (Goonetilleke et al., 2012; Goonetilleke et al., 2010; De Havas et al., 2020); (3) combining EMG with other parametric approaches in which action stopping can be measured on a continuous scale, for example measuring movement trajectories (Atsma et al., 2018; De Havas et al., 2020) or response force (Nguyen et al., 2020). If properly validated, parametric approaches may eventually outperform EMG measures, especially in clinical samples where obtaining clean EMG signals may be challenging.

Another unsettled question regarding the generalizability is whether prEMG trials could be qualitatively different from other successful stop trials. McGarry and Franks, 1997 designed a stop signal task with untypically short SSDs, and found that they could differentiate between trials with early and late stopping mechanisms based on the shape of the prEMG rising slope (see Box 1 about interrupted response for details), although it has been disputed that the same pattern could result from the differential recruitment times of motor neurons with different sizes (van Boxtel and Band, 2000). Further, EEG studies have found that prEMG trials show decreased lateralized readiness potentials and increased frontal negativities (de Jong et al., 1990; van Boxtel et al., 2001). Increased frontal negativities have also been related to awareness of the prEMG in response conflict tasks (Ficarella et al., 2019). However, whether these cortical changes reflect qualitatively different mechanisms or merely a continuous variation in the strength of the underlying processes is unresolved (van Boxtel et al., 2001).

Finally, does prEMG latency generalize across different contexts? While it has been shown that the SSRT becomes increasingly unreliable in more complex stop signal tasks and its use is thus discouraged (Bissett and Logan, 2014), prEMG can still be recorded in such task settings (Raud et al., 2020a; Raud and Huster, 2017). Further, (pr)EMG is not limited to the stop signal task, but can be recorded in any task that requires overt responses, as well as tasks that require more complex movements activating several muscle groups (Tao et al., 2018). As such, EMG can provide highly sought-after physiological measures that are comparable across different contexts and is currently the most useful approach for investigating putative response inhibition in tasks that rely on the absence of overt behavior as the primary outcome measure. For example, one study using this approach found that the prEMG peaked significantly later in the go/no-go task than in the stop signal task. This was also paralleled by differences in cortical activity, suggesting that these tasks may recruit different mechanisms (Raud et al., 2020b). Similarly, Tatz et al., 2021 showed that EMG activity declines after any infrequent salient stimulus, highlighting the interdependence between attentional capture and inhibitory control constructs. Thus, comparisons of prEMG characteristics and their driving mechanisms in different contexts provide a rich ground for future research on motor and cognitive control.

### Response inhibition and prEMG

While prEMG can be considered an assumption-free physiological measure in its implementation, it is not free from assumptions in its interpretation. The most urgent unresolved question is whether prEMG captures the latency of inhibitory mechanisms in the brain. On the one hand, prEMG decline unequivocally indicates stopping of muscle activity, so it is safe to presume that the peak latency represents the latency of action stopping. On the other hand, the actual mechanisms that cause this EMG decline cannot be derived from prEMG alone. Alternative explanations to cortical active inhibition mechanisms include activation of antagonist muscles triggering peripheral lateral inhibition, an initial subthreshold activation of the go response, or cessation of the invigoration of the go response by the motor system. Several studies have investigated whether stopping of specific muscle activity could be caused by the activation of antagonist muscles and found that agonist stopping occurs before antagonist activation; thus, the former cannot be caused by the latter (Atsma et al., 2018; Corneil et al., 2013; Goonetilleke et al., 2012; Goonetilleke et al., 2010; Scangos and Stuphorn, 2010). It is also unlikely that prEMG represents initial subthreshold go activations, as such stimulus-locked responses are typically <100 ms after stimulus onset (Pruszynski et al., 2010), while prEMG onsets are closer to 300–500 ms. However, it remains to be seen whether prEMG declines because of a reduction in response maintenance (e.g., by restoring the inhibitory state of the cortical-basal ganglia–thalamic loop during rest), or because of an active inhibition mechanism that blocks ongoing motor activity (e.g., by blocking the direct pathway output by increased inhibition via the subthalamic nucleus, or by direct inhibitory influences on M1; e.g., Hynd et al., 2021). Complementary simultaneous data from brain imaging and neural stimulation studies are necessary to understand the neural mechanisms that cause the halt in muscle activity.

### Conclusions

Based on the synthesis of previous work together with a comprehensive analysis of prEMG characteristics in an independent dataset, we conclude that prEMG is a useful and reliable measure of action stopping. PrEMG is not limited to specific muscles, stimulus modalities, or task contexts, so it provides a comparative physiological measure for a range of different scenarios. Even though there are some similarities between the SSRT and the prEMG, these two measures should not be used interchangeably, but rather complementarily. The SSRT benefits from decades of research and is therefore well characterized across different contexts and sample populations. Yet, it is founded on assumptions that are not always met in empirical data, and it seems to be more strongly affected by behavioral strategies than the prEMG. In contrast, prEMG is directly observable and provides action stopping latencies at a single-trial level. Its peak latency is relatively stable even though design choices may limit the number of available trials. Importantly, neither the SSRT nor the prEMG peak latency is an unambiguous marker of response inhibition in the brain, but since the prEMG is directly observable, it has stronger potential for guiding research on brain mechanisms underlying action stopping.

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
      <td>Software, algorithm</td>
      <td>E-prime</td>
      <td>Psychology Software Tools, Pittsburgh, PA</td>
      <td>Version 2.0</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Matlab</td>
      <td>The Math Works, Inc MATLAB</td>
      <td>9.4.0.949201 (R2018a)</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Eeglab</td>
      <td>Delorme and Makeig, 2004</td>
      <td>14.1.1b</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>R</td>
      <td>R Core Team, 2019;</td>
      <td>3.6.2 (2019-12-12)</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>BEESTS; Dynamic Models of Choice</td>
      <td>Matzke et al., 2019; Matzke et al., 2013Heathcote et al., 2019</td>
      <td>BEESTS2-GF</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Sample

Data were analyzed from 46 healthy young adults (mean age = 23.7, sd = 5.5, 30 females, 3 left-handed). Initially, data were collected from 52 participants, but four were discarded due to technical issues with the response device and another two were discarded as statistical outliers (above two interquartile ranges) based on EMG onset and peak latencies. Participants gave written informed consent prior to data collection, and everyone received monetary compensation for their participation. The study was conducted in accordance with the Helsinki declaration, and was approved by the internal review board of the University of Oslo (ref. 1105078).

### Stop signal task and behavioral variables

All participants performed a choice-reaction time task and a stop signal task presented in alternating blocks (six blocks in total). Task presentation was controlled by E-prime 2.0 (Psychology Software Tools, Pittsburgh, PA). For this analysis, we focus on the stop signal task exclusively. The primary task was to respond with a button press using the thumb of the left or right hand to an arrow pointing to the left or right, correspondingly. In 24% of the trials, a stop signal appeared after a variable SSD, instructing participants to stop their initiated response. In total, there were 684 go trials and 216 stop trials, equally distributed between left- and right-hand trials.

Each trial started with a black fixation cross (duration jittered between 500 and 1000 ms), followed by a colored arrow as a go signal, presented for 100 ms. In stop trials, a second arrow of a different color was presented after the SSD. The SSD could vary between 100 and 800 ms and was adjusted based on an adaptive tracking procedure collapsed across both hands: The initial SSD was set to 250 ms, and then increased or decreased by 50 ms following successful and unsuccessful stop trials, respectively. Responses were collected up to 1000 ms after the go stimulus and potential responses after this window were treated as omissions. All stimuli were presented centrally against a gray background and the stimulus color assignments (green, orange, or blue) were counterbalanced across participants. Trial order within a block was randomized, except for the first block, which always started with a minimum of 10 go trials. Short pauses (9 s) were given after every 75 trials, and a longer break with a duration of roughly 5 min was allowed halfway through the task.

Prior to the experiment, the participants completed a short training block (20 trials, 50% stop trials) with computerized trial-by-trial feedback. In addition, participants were told that it was important to be both fast and accurate, that they were not supposed to wait for the stop signal, and that it was not possible to successfully stop in all stop trials. Automated feedback was presented on screen after every 75th trial. Here, participants were instructed to be faster if their average goRT was above 600 ms, and to be more accurate if the average stop accuracy was below 40%. If neither of these applied, they received the feedback ‘Well done!’.

The following behavioral variables were extracted based on task performance: go accuracies, error, and omission rates, go reaction times, stop accuracies, unsuccessful stop reaction times, average SSD, and SSRTs. These were calculated using the integration method, where corresponding go reaction time distributions included choice errors, and omissions were replaced by the maximum reaction time (Verbruggen et al., 2019).

We also estimated SSRTs and their variability using a Bayesian parametric approach (BEESTS; Matzke et al., 2019; Matzke et al., 2013). We chose the BEESTS2-GF model due to the low amount of choice errors in our sample. This model assumes a single go process as well as a stop process, and that both the go and SSRTs can be approximated by an ex-Gaussian distribution, defined by the μ and τ parameters and a standard deviation of σ2 + τ2. As this model only fits one go process, choice errors were removed prior to analysis. We also removed outlier trials, defined as trials with RTs ± 3 SDs away from each participant’s mean. Estimation was run using the Dynamic Models of Choice toolbox (Heathcote et al., 2019) in R Studio (version 1.3.1093) where models were fitted to each participant individually. Parameter priors were defined as weakly informative truncated normal distributions (Heathcote et al., 2019; Skippen et al., 2019). Specifically, we set the mean to 500 ms (μgo and μstop), 200 ms (σgo and τgo), and 100 ms (σstop and τstop), and the standard deviations to 1000ms. The priors for go and trigger failures had a mean of 1.5 (probit scale) with a standard deviation of 1. We ran 24 chains, 3 for each estimated parameter. All rhat-values were <1.1, indicating chain convergence. Posterior distributions were updated well, suggesting that priors were largely uninformative. Plots showing the prior relative to posterior distributions, chains, and posterior predictive model checks can be found in the accompanying materials on OSF (Raud et al., 2021).

### EMG acquisition

Two surface EMG electrodes were placed on the skin above the abductor pollicis brevis in parallel to the belly of the muscles on each hand using bipolar Ag/Ag-Cl montages. Corresponding ground electrodes were placed on each forearm. The recordings were performed using a BrainAmp ExG extension for bipolar recordings (Brain Products GmbH, Germany) with an online low-pass filter of 1000 Hz, a sampling rate of 5000 Hz, and a 0.5 µV resolution.

### EMG preprocessing and burst detection

EMG preprocessing and variable extractions were performed with custom scripts in MATLAB (The Math Works, Inc MATLAB, version 2018a) and eeglab (Delorme and Makeig, 2004; version 14.1.1b) and are publicly available on the OSF (Raud et al., 2021; https://osf.io/rqnuj/). The EMG signal was bandpass filtered between 20 and 250 Hz using a second-order butterworth filter and resampled to 500 Hz. Data epochs were extracted for all trials from −0.2 to 1.6 s relative to go signal onset. Trials were rejected at this stage if the average baseline activity was larger than 100 μV (across all participants, this led to the rejection of 206 trials, i.e., roughly 0.5 %).

The data epochs were transformed by taking the root mean square over a moving average window or ±5 data points, and normalized to baseline by dividing the full time-course by the average of the baseline period (−0.2 to 0 s relative to the go signal). For each participant and each hand, epochs were then concatenated and z-scored block-wise.

EMG bursts were identified in a trial if any data point exceeded a threshold of 1.2 (in standard deviation units, taking into account all trials). This threshold was confirmed visually and has been held constant across several recent studies (Huster et al., 2020; Raud et al., 2020a; Raud et al., 2020b; Thunberg et al., 2020). The peak latency was defined as the time-point of the highest amplitude in a trial. Onset latency was determined by tracking amplitude values backwards in time, starting at the peak latency, up until continuous data points of 8ms were below amplitude threshold. Lastly, peak latencies of the EMG in stop trials were recalculated relative to the stop signal onset by subtracting the SSD. All variables were averaged over left- and right-hand trials.

### Statistical analyses

Statistical analyses were performed using R (R Core Team, 2019) and the package collection of tidyverse (Wickham et al., 2019) and custom scripts in MATLAB. All figures were created either in MATLAB or in R using the packages ggplot2 (Wickham, 2020), ggpubr (Kassambara, 2020), and psych (Revelle, 2021).

The trial differences between EMG amplitudes and peaks were tested by means of t-tests and analyses of variance within the Bayesian framework using the R package BayesFactor (Morey et al., 2018). The evidence was quantified using the Bayes factor, with values greater than 1 indicating support for the alternative and values below 1 for the null hypothesis (with >3 and <0.3 often considered indicators of strong evidence toward alternative or null, respectively).

We further tested whether the prEMG characteristics (inhibition functions, probability, onset latency, peak latency, and peak amplitude) varied across SSDs. To account for individual variability in SSDs, we centralized the SSDs per participant instead of using the absolute values. The mode of each participant’s SSD distribution was treated as zero and we extracted the values ±3 SSD steps around the mode. The prEMG characteristics were averaged per SSD, so that each participant had one value per SSD, given that they had any trials with prEMG at that specific SSD.

The relationships between the prEMG characteristics and the prEMG were expected to be nonlinear with the exact shape unknown. Therefore, these were tested by the GAMMs using the R package gamm4 (Wood and Scheipl, 2020). GAMM includes the possibility of adding a smooth term to the model, which is a linear sum of several splines. The degree of nonlinearity (or wiggliness) of the resulting model fit is determined by the edf and the corresponding F and p values, together with the estimated lambda factor that penalizes for overfitting. For example, in cases where linear fit is the best fit, the edf will be close to one; in case of second-order polynomial fit, the edf will be close to 2, etc. We considered smooth parameters with a p value below 0.05 as indicative of a significant effect.

Single-trial analysis. The single-trial analysis was done on prEMG (successful stop trials) only, using prEMG onset latencies, peak latencies, and AUC from onset to peaks. These were calculated as a cumulative sum of the amplitudes from onset to peak. AUC thus integrates the duration and amplitude of the prEMG bursts before their decline. As the bivariate correlations with the SSD at a single-trial level were high for the onset latencies (r = 0.88), they were orthogonalized for the SSD by predicting onsets from the SSD for each participant and using the residuals instead of original values. AUCs were log transformed since the original values were extremely skewed toward low values. Additional data cleaning was applied, in which trials were excluded if the peak latency occurred before the stop signal or if the onsets (go-locked) or peaks (stop-locked) exceeded two interquartile ranges of the individual participant’s data. Three separate GAMMs were performed predicting peak latency from onset latency, AUC from peak latency, and AUC from onset latency.

Variability. Individual prEMG variability was estimated as the standard deviation of the prEMG peak latencies across trials for each participant. As some participants had implausibly large variability estimates, we identified and excluded four outliers who exceeded two interquartile ranges. One of these was also an outlier for the standard deviation of the SSRT, calculated by the BEESTS method. Bivariate Pearson rank-ordered correlation coefficients and (uncorrected) p values were used to identify relationships between prEMG variability and the number of prEMG trials per participant, go reaction time standard deviations, average root mean square amplitudes during the intertrial interval of −20 to 0 ms before go stimulus, and standard deviation of the SSRT calculated by the BEESTS method. The scatterplots with the outliers included are in Appendix 1—table 2.

Reliability. We estimated the internal consistency of the different prEMG metrics (onset latencies, peak latencies, peak amplitudes, and AUCs from onset to peak) using a permutation-based split-half approach (Parsons et al., 2019). After the same level of additional data cleaning as in the single-trial analyses, we split the data for each participant into two random halves and calculated the mean of each half. These estimates for each half were then correlated across participants and the correlations were corrected using the Spearman-Brown prophecy formula (Brown, 1910; Spearman, 1910). This process was repeated 10,000 times, thus resulting in a distribution of reliability estimates. We used the mean of this distribution as our summary reliability estimate, and 2.5th and 97.5th percentiles as the upper and lower limits of the confidence intervals.

Initially, all trials from all participants were used for the reliability estimates. Next, we repeated the analysis iteratively using an equal number of trials per participant and excluding all participants who did not have enough trials available for a specific iteration. We started with 6 trials per participant (lowest number of trials available for all participants) and increased the number of trials per iteration by one until we were left with 32 trials per participant (with 12 participants remaining). We repeated this process 1000 times, thus getting a distribution of reliability estimates at each trial count.

### Meta-analysis

Three databases (Pubmed, Scopus, and Google Scholar) were searched with keywords (‘EMG’ OR ‘electromyography’) AND (‘stop signal’ OR ‘countermanding’ OR ‘antisaccade’ OR ‘anticipated response’) on 11/21/2021. The abstracts of 158 entries were screened and included in the meta-analysis if they reported prEMG peak or offset latencies relative to the stop signal onset. Most studies reported data from more than one experiment or experimental condition. All experiments/conditions were included as separate entries, except for Thunberg et al., 2020, from which we only included the three baseline sessions (and excluded the remaining six peri- and post-TDCS sessions, not to bias the results toward a single study with nine entries). Studies that reanalysed data already included in the meta-analysis were excluded. This resulted in 21 conditions/experiments from 10 different studies. In case of missing values, authors were contacted, and all authors provided the required values. We calculated the averages and standard deviations of the go RTs, SSRTs, prEMG detection frequencies, and peak/offset latencies, the differences between the SSRT and prEMG peak latencies, and correlations between the prEMG and SSRT. For the correlation coefficients, the means and standard deviations were calculated on Student z-transformed data, and then retransformed into correlation coefficients. The associations between the behavioral and EMG measures were tested with general mixed models with ‘study’ as a random variable, using the R package lme4 (Bates, 2022). The spreadsheet with extracted data for all included studies is uploaded in the accompanying OSF page (Raud et al., 2021).
