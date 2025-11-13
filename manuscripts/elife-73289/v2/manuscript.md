# Corticofugal regulation of predictive coding

## Authors

- Alexandria MH Lesicko<sup>1</sup> ([ORCID: 0000-0003-4766-2258](https://orcid.org/0000-0003-4766-2258))
- Christopher F Angeloni<sup>2</sup>
- Jennifer M Blackwell<sup>1</sup>
- Mariella De Biasi<sup>4</sup>
- Maria N Geffen<sup>1</sup> ([ORCID: 0000-0003-3022-2993](https://orcid.org/0000-0003-3022-2993)) †

### Affiliations

1. Department of Otorhinolaryngology, University of Pennsylvania Philadelphia United States ([ROR:00b30xv10](https://ror.org/00b30xv10))
2. Department of Psychology, University of Pennsylvania Philadelphia United States ([ROR:00b30xv10](https://ror.org/00b30xv10))
3. Department of Neurobiology and Behavior, Stony Brook University Stony Brook United States ([ROR:05qghxh33](https://ror.org/05qghxh33))
4. Department of Psychiatry, University of Pennsylvania Philadelphia United States ([ROR:00b30xv10](https://ror.org/00b30xv10))
5. Department of Systems Pharmacology and Experimental Therapeutics, University of Pennsylvania Philadelphia United States ([ROR:00b30xv10](https://ror.org/00b30xv10))
6. Department of Neuroscience, University of Pennsylvania Philadelphia United States ([ROR:00b30xv10](https://ror.org/00b30xv10))
7. Department of Neurology, University of Pennsylvania Philadelphia United States ([ROR:00b30xv10](https://ror.org/00b30xv10))

† Corresponding author

## Abstract

Sensory systems must account for both contextual factors and prior experience to adaptively engage with the dynamic external environment. In the central auditory system, neurons modulate their responses to sounds based on statistical context. These response modulations can be understood through a hierarchical predictive coding lens: responses to repeated stimuli are progressively decreased, in a process known as repetition suppression, whereas unexpected stimuli produce a prediction error signal. Prediction error incrementally increases along the auditory hierarchy from the inferior colliculus (IC) to the auditory cortex (AC), suggesting that these regions may engage in hierarchical predictive coding. A potential substrate for top-down predictive cues is the massive set of descending projections from the AC to subcortical structures, although the role of this system in predictive processing has never been directly assessed. We tested the effect of optogenetic inactivation of the auditory cortico-collicular feedback in awake mice on responses of IC neurons to stimuli designed to test prediction error and repetition suppression. Inactivation of the cortico-collicular pathway led to a decrease in prediction error in IC. Repetition suppression was unaffected by cortico-collicular inactivation, suggesting that this metric may reflect fatigue of bottom-up sensory inputs rather than predictive processing. We also discovered populations of IC units that exhibit repetition enhancement, a sequential increase in firing with stimulus repetition. Cortico-collicular inactivation led to a decrease in repetition enhancement in the central nucleus of IC, suggesting that it is a top-down phenomenon. Negative prediction error, a stronger response to a tone in a predictable rather than unpredictable sequence, was suppressed in shell IC units during cortico-collicular inactivation. These changes in predictive coding metrics arose from bidirectional modulations in the response to the standard and deviant contexts, such that the units in IC responded more similarly to each context in the absence of cortical input. We also investigated how these metrics compare between the anesthetized and awake states by recording from the same units under both conditions. We found that metrics of predictive coding and deviance detection differ depending on the anesthetic state of the animal, with negative prediction error emerging in the central IC and repetition enhancement and prediction error being more prevalent in the absence of anesthesia. Overall, our results demonstrate that the AC provides cues about the statistical context of sound to subcortical brain regions via direct feedback, regulating processing of both prediction and repetition.

## Introduction

Sensory systems differentially encode environmental stimuli depending on the context in which they are encountered (De Franceschi and Barkat, 2020; Herrmann et al., 2015; Jaramillo et al., 2014; Pakan et al., 2016; Takesian et al., 2018; Zhai et al., 2020). The same physical stimulus can elicit distinct neuronal responses depending on whether it is predictable or unexpected in a given sensory stream (Weissbart et al., 2020; Yaron et al., 2012). Neurons in select regions of the central auditory system are sensitive to statistical context, responding more strongly to a tone when it is presented rarely (a ‘deviant’) than when it is commonplace (a ‘standard’) (Ulanovsky et al., 2003). This phenomenon, known as stimulus-specific adaptation (SSA), is prevalent in the auditory cortex (AC) (Natan et al., 2015; Ulanovsky et al., 2003). Weaker SSA is present in regions peripheral to the AC, including the auditory midbrain, or inferior colliculus (IC), and the auditory thalamus, or medial geniculate body (MGB) (Anderson et al., 2009; Antunes et al., 2010; Duque and Malmierca, 2015; Malmierca et al., 2009; Taaseh et al., 2011; Ulanovsky et al., 2003). Subdivisions in IC and MGB that receive descending projections from AC exhibit relatively higher SSA levels than their lemniscal counterparts (Antunes et al., 2010; Duque et al., 2012), suggesting that SSA may be generated de novo in AC and subsequently broadcast to subcortical structures via corticofugal projections (Nelken and Ulanovsky, 2007). Silencing of AC through cooling, however, has been shown to modulate, but not abolish, SSA in IC and MGB of anesthetized rats (Anderson and Malmierca, 2013; Antunes and Malmierca, 2011).

Recent studies have implemented additional control tone sequences to further decompose the traditional SSA index into two distinct underlying processes: repetition suppression and prediction error (Harms et al., 2014; Parras et al., 2017; Ruhnau et al., 2012). Repetition suppression is characterized by a decrease in firing rate to each subsequent presentation of a standard tone, whereas prediction error signals an enhanced response to a deviant tone (Auksztulewicz and Friston, 2016; Parras et al., 2017). Hierarchical predictive coding posits that prediction errors signal the mismatch between predictions, formed based on prior experience with repeated presentations of the standard, and actual sensory input in the presence of a deviant (Friston, 2009; Friston and Kiebel, 2009). These predictions are generated at higher levels of the sensory hierarchy and broadcast to lower stations to minimize processing of redundant input and maximize coding efficiency (Friston, 2009; Friston and Kiebel, 2009). Prediction error has been proposed to underlie true deviance detection, while repetition suppression is thought to potentially reflect synaptic depression (Parras et al., 2017; Taaseh et al., 2011). Prediction error increases along the auditory hierarchy and is more prevalent in regions of IC and MGB that receive cortical feedback (Parras et al., 2017), suggesting that these subcortical regions may engage in hierarchical predictive coding, with AC potentially providing predictive cues to IC and MGB. However, how feedback projections from AC shape predictive processing in subcortical targets has never been directly assessed. In fact, virtually all models of hierarchical predictive coding to date have focused on intracortical connections, with the massive system of descending corticofugal projections remaining unexplored (Asilador and Llano, 2020; Bastos et al., 2012).

Here, we investigated how inputs from AC to IC, the first station in the auditory system in which prediction error is found, shape metrics associated with predictive coding and deviance detection (Parras et al., 2017). To test this, we optogenetically inactivated cortico-collicular feedback while recording neuronal responses in IC and found that prediction error, negative prediction error, and repetition enhancement in IC are altered in the absence of cortical input. Our results suggest that the cortico-collicular pathway sends cues from AC to IC regarding the statistical context of auditory stimuli.

## Results

### Experimental design

We used a Cre/FLEX viral injection strategy to selectively express the inhibitory opsin, ArchT, in cortico-collicular neurons of four mice by injecting a retroAAV-Cre-GFP construct into IC and an AAV9-FLEX-ArchT-tdTomato construct into AC (Figure 1A, left). The retroAAV-Cre-GFP construct is transported in a retrograde fashion and expressed in neurons that project to IC (Blackwell et al., 2020). The genes encoded in the AAV9-FLEX-ArchT-tdTomato construct can only be expressed in neurons containing the Cre construct, thereby limiting ArchT expression to neurons in AC that project to IC. In the presence of green light, ArchT, a light-driven outward proton pump, mediates rapid, reversible inactivation of the neurons in which it is expressed (Han et al., 2011).

![Figure 1.](https://cdn.elifesciences.org/articles/73289/elife-73289-fig1-v2.jpg)

**Figure 1.:** (A) Cre/FLEX dual injections for selective ArchT expression in cortico-collicular neurons. Recordings were performed in the inferior colliculus (IC) while inactivation was mediated by a 532 nm laser connected to cannulas implanted over the auditory cortex (AC). (B) Oddball stimuli consisted of pairs of pure tones separated by 0.5 octave with a 90:10 standard-to-deviant ratio. Two sequences were constructed such that each frequency is represented as both the standard and the deviant. (C) Cascade sequences consisted of 10 evenly spaced tones separated by 0.5 octaves, with both frequencies from the oddball sequence included in the sequence. Responses to tones in the cascade context were compared to responses in the standard and deviant context to analyze repetition and prediction effects, respectively. (D) A positive index of neuronal mismatch (iMM) (top diagram) indicates a stronger response to the deviant than the standard (adaptation), while a negative iMM (bottom diagram) indicates a stronger response to the standard than to the deviant (facilitation). The iMM can be further decomposed into an index of prediction error (iPE) and an index of repetition suppression (iRS). Positive iPE values represent prediction error, and negative values convey negative prediction error. Positive iRS indices indicate repetition suppression, while repetition enhancement is represented by negative values.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/73289/elife-73289-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Expression of the retroAAV-Cre-GFP construct at the injection site is restricted to the inferior colliculus (IC) (top left). tdTomato-labeled axons are found in a pattern matching the known topographical distribution of cortico-collicular neurons in IC (left bottom). Somatic AAV9-FLEX-ArchT-tdTomato expression is present in layers 5 and 6 of the auditory cortex (AC) (right, inset). (B) Experimental design for recording from AC to confirm the presence of inactivated units. (C) Example of an inactivated unit (i.e., putative cortico- collicular unit) exhibiting a strong reduction in firing during silence and during the presentation of pure tones. (D) Population data demonstrating reduced firing rates during silence and in response to pure tone stimuli in putative cortico-collicular units. Dots represent recorded units. Bar plots represent means over the population n = 20 CC units. Error bars are standard error of the mean.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/73289/elife-73289-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) Experimental design for awake inferior colliculus (IC) recordings in the central and shell regions of IC. (B) Linear fits for best frequency vs. depth in central (left) and shell (right) IC. (C) Sparseness vs. R2 value for linear fit. K-means clustering was performed using these parameters to classify recording sites as either in the shell or central nucleus of IC. Each dot represents a recording site. (D) Left: DiA labeling from an electrode penetration in a recording site classified as a central site. Atlas image overlay confirms that the dye track runs through the central IC (CIC) (Paxinos and Franklin, 2019). Right: DiD labeling from an electrode penetration in a recording site classified as a shell site. Atlas image overlay confirms that the dye track runs through the shell IC (here denoted as ECIC/DCIC). (E) Example raster plots and peristimulus time histograms showing different firing types in the awake IC. Examples of inhibited and mixed types are from single units, while all others are from multiunits. (F) Example tuning curves in central (left) and shell (right) IC. (G) Example of a tuning curve with inhibited side bands.

We implanted cannulas over AC in mice injected with the Cre/FLEX constructs and a 532 nm laser was used to provide green light illumination to the region, allowing for inactivation of cortico-collicular neurons (Figure 1A, right). The mice were head-fixed and a 32-channel probe was lowered into IC to perform awake extracellular recordings (Figure 1A). Auditory stimuli consisted of oddball sequences of two repeated pure tones, presented at a 90:10 standard-to-deviant ratio and half-octave frequency separation (Figure 1B). On a subset of trials, presentations of either the deviant or the last standard prior to the deviant were coupled with activation of the green laser (Figure 1B, right).

Units that displayed a significantly higher response to the deviant than the standard were designated as ‘adapting’ units, while those that exhibited a significantly higher response to the standard than the deviant were categorized as ‘facilitating’ units (Figure 1D). The difference in firing rate to the standard and deviant was quantified with an index of neuronal mismatch (iMM), which is equivalent to the SSA index used in previous studies (Parras et al., 2017).

A cascade stimulus consisting of 10 evenly spaced tones, including the tone pair from the oddball sequence, was presented to further decompose the neuronal mismatch between the responses to the standard and deviant (Figure 1C and D). This stimulus is unique in that each tone occurs with the same likelihood as the deviant tone in the oddball stimulus (10%), but it contains no true statistical deviants: each tone has the same likelihood of presentation, and the tone sequence overall follows a regular and predictable pattern (Parras et al., 2017). Therefore, the response to a given tone when it is embedded in the cascade can be compared to the response when it is a deviant in order to isolate prediction error effects (Figure 1C and D, top). A neuron exhibits prediction error if it fires more strongly to a tone when it is a deviant than when it is presented in the cascade sequence (Figure 1D, top). Conversely, if a neuron responds more strongly to a tone presented in the cascade sequence than when it is a deviant, the neuron encodes negative prediction error (Figure 1D, bottom). This phenomenon is quantified using an index of prediction error (iPE), with positive indices indicating prediction error and negative indices representing negative prediction error (Figure 1D).

The cascade sequence is also free from repetition effects since adjacent tone presentations never include a tone of the same frequency (Figure 1C). Therefore, the response to a given tone embedded in the cascade sequence can be compared to the response generated when that tone is a standard. The difference in response indicates either repetition suppression (stronger response to the tone in the cascade) (Figure 1D, top) or repetition enhancement (stronger response to the tone as a standard) (Figure 1D, bottom). These contrasting processes are quantified by the index of repetition suppression (iRS), with a positive index indicating repetition suppression and a negative index representing repetition enhancement (Figure 1D).

### Cre/FLEX viral injection strategy enables selective inactivation of cortico-collicular neurons

Examination of fixed tissue from injected mice revealed that expression of the retroAAV-Cre-GFP construct was restricted to IC (Figure 1—figure supplement 1A, top left). Somatic expression of GFP (indicating the presence of Cre) was restricted to layer 5 and deep layer 6 of AC, which contain cortico-collicular cell bodies, and was broadly distributed throughout the rostro-caudal extent of AC (Figure 1—figure supplement 1A, right) (Bajo et al., 2007; Schofield, 2009; Yudintsev et al., 2019). Expression of tdTomato was found in the soma and processes of neurons in layers 5 and 6, with additional apical dendritic labeling observed in the upper cortical layers (Figure 1—figure supplement 1A, right). The laminar expression of tdTomato is consistent with previous studies and suggests that AAV9-FLEX-ArchT-tdTomato expression is Cre-dependent and not due to nonspecific labeling (Blackwell et al., 2020). Axons and terminals labeled with tdTomato were distributed in IC in a manner matching the known projection pattern of this pathway, with dense, ‘patchy’ labeling in shell regions of IC (Figure 1—figure supplement 1A, bottom left) (Herbert et al., 1991; Lesicko et al., 2016; Saldaña et al., 1996; Torii et al., 2013). These data confirm that our viral injection strategy leads to selective transfection of cortico-collicular neurons.

Extracellular recordings in AC of injected mice revealed a reduction in firing rate during the duration of the laser stimulus in several units (Figure 1—figure supplements 1B and 2C). In these putative cortico-collicular units, laser-induced inactivation led to a mean ~60% reduction in firing rate at baseline (Figure 1—figure supplement 1C, left; Figure 1—figure supplement 2D, top; Table 1; p=1.9e-06, Wilcoxon signed-rank test) and an average ~45% reduction in firing during presentation of pure tone stimuli (Figure 1—figure supplement 1C, right; Figure 1—figure supplement 2D, bottom; Table 1; p=1.9e-06, Wilcoxon signed-rank test). These results indicate that our optogenetic parameters significantly suppress cortico-collicular units.

**Table 1.**
 Statistical comparisons for experimental data.


<table>
  <thead>
    <tr>
      <th>Comparison</th>
      <th>Figure</th>
      <th>Mean</th>
      <th>Median</th>
      <th>SD</th>
      <th>SEM</th>
      <th>CI (±)</th>
      <th>Test</th>
      <th>Test statistic</th>
      <th>N</th>
      <th>df</th>
      <th>p</th>
      <th>Effect size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Response of putative cortico-collicular units in silence (laser OFF vs. ON)</td>
      <td>Figure 1—figure supplement 1D (top)</td>
      <td>OFF: 11ON: 4.1</td>
      <td>OFF: 9.0ON: 3.5</td>
      <td>OFF: 8.9ON: 3.5</td>
      <td>OFF: 2.0ON: 0.78</td>
      <td>OFF: 4.2ON: 1.6</td>
      <td>Wilcoxon signed-rank test</td>
      <td>V = 0</td>
      <td>20</td>
      <td>NA</td>
      <td>1.9e-06</td>
      <td>0.88</td>
    </tr>
    <tr>
      <td>Response of putative cortico-collicular units to pure tones (laser OFF vs. ON)</td>
      <td>Figure 1—figure supplement 1D (bottom)</td>
      <td>OFF: 18ON: 9.6</td>
      <td>OFF: 8.8ON: 4.3</td>
      <td>OFF: 24ON: 12</td>
      <td>OFF: 5.4ON: 2.7</td>
      <td>OFF: 11ON: 5.6</td>
      <td>Wilcoxon signed-rank test</td>
      <td>V = 0</td>
      <td>20</td>
      <td>NA</td>
      <td>1.9e-06</td>
      <td>0.88</td>
    </tr>
    <tr>
      <td>iMM central (awake vs. anesthetized)</td>
      <td>Figure 2B</td>
      <td>Aw: 0.050An: 0.25</td>
      <td>Aw: 0.045An: 0.28</td>
      <td>Aw: 0.21An: 0.49</td>
      <td>Aw: 0.024An: 0.074</td>
      <td>Aw: 0.047An: 0.15</td>
      <td>Wilcoxon rank-sum test</td>
      <td>W = 952.5</td>
      <td>Aw: 78An: 43</td>
      <td>NA</td>
      <td>8.8e-05</td>
      <td>0.36</td>
    </tr>
    <tr>
      <td>iPE central (awake vs. anesthetized)</td>
      <td>Figure 2C</td>
      <td>Aw: –0.13An: 0.077</td>
      <td>Aw: –0.11An: 0.098</td>
      <td>Aw: 0.17An: 0.53</td>
      <td>Aw: 0.019An: 0.081</td>
      <td>Aw: 0.038An: 0.16</td>
      <td>Student’s t-test</td>
      <td>t = –2.5</td>
      <td>Aw: 78An: 43</td>
      <td>38</td>
      <td>0.017</td>
      <td>0.52</td>
    </tr>
    <tr>
      <td>iRS central (awake vs. anesthetized)</td>
      <td>Figure 2D</td>
      <td>Aw: 0.18An: 0.18</td>
      <td>Aw: 0.17An: 0.30</td>
      <td>Aw: 0.17An: 0.56</td>
      <td>Aw: 0.019An: 0.085</td>
      <td>Aw: 0.039An: 0.17</td>
      <td>Wilcoxon rank-sum test</td>
      <td>W = 1444</td>
      <td>Aw: 78An: 43</td>
      <td>NA</td>
      <td>0.21</td>
      <td>0.12</td>
    </tr>
    <tr>
      <td>iMM shell (awake vs. anesthetized)</td>
      <td>Figure 2E</td>
      <td>Aw: 0.095An: 0.27</td>
      <td>Aw: 0.090An: 0.27</td>
      <td>Aw: 0.31An: 0.35</td>
      <td>Aw: 0.025An: 0.022</td>
      <td>Aw: 0.050An: 0.043</td>
      <td>Wilcoxon rank-sum test</td>
      <td>W = 12,502</td>
      <td>Aw: 147An: 254</td>
      <td>NA</td>
      <td>3.5e-08</td>
      <td>0.28</td>
    </tr>
    <tr>
      <td>iPE shell (awake vs. anesthetized)</td>
      <td>Figure 2F</td>
      <td>Aw: 0.15An: 0.018</td>
      <td>Aw: 0.15An: –0.0075</td>
      <td>Aw: 0.33An: 0.39</td>
      <td>Aw: 0.027An: 0.025</td>
      <td>Aw: 0.053An: 0.049</td>
      <td>Wilcoxon rank-sum test</td>
      <td>W = 23,368</td>
      <td>Aw: 147An: 254</td>
      <td>NA</td>
      <td>2.6e-05</td>
      <td>0.21</td>
    </tr>
    <tr>
      <td>iRS shell (awake vs. anesthetized)</td>
      <td>Figure 2G</td>
      <td>Aw: –0.056An: 0.25</td>
      <td>Aw: –0.085An: 0.29</td>
      <td>Aw: 0.36An: 0.33</td>
      <td>Aw: 0.029An: 0.020</td>
      <td>Aw: 0.058An: 0.040</td>
      <td>Wilcoxon rank-sum test</td>
      <td>W = 9501.5</td>
      <td>Aw: 147An: 254</td>
      <td>NA</td>
      <td>2.5e-16</td>
      <td>0.41</td>
    </tr>
    <tr>
      <td>iMM central adapting (laser OFF vs. ON)</td>
      <td>Figure 3D (top)</td>
      <td>OFF: 0.26ON: 0.21</td>
      <td>OFF: 0.24ON: 0.19</td>
      <td>OFF: 0.096ON: 0.13</td>
      <td>OFF: 0.013ON: 0.019</td>
      <td>OFF: 0.027ON: 0.037</td>
      <td>Wilcoxon signed-rank test</td>
      <td>V = 1083</td>
      <td>52</td>
      <td>NA</td>
      <td>0.00034</td>
      <td>0.50</td>
    </tr>
    <tr>
      <td>iPE central adapting (laser OFF vs. ON)</td>
      <td>Figure 3D (middle)</td>
      <td>OFF: 0.0077ON: –0.029</td>
      <td>OFF: 0.036ON: 0.0041</td>
      <td>OFF: 0.16ON: 0.16</td>
      <td>OFF: 0.022ON: 0.022</td>
      <td>OFF: 0.043ON: 0.044</td>
      <td>Wilcoxon signed-rank test</td>
      <td>V = 907</td>
      <td>52</td>
      <td>NA</td>
      <td>0.048</td>
      <td>0.28</td>
    </tr>
    <tr>
      <td>iRS central adapting (laser OFF vs. ON)</td>
      <td>Figure 3D (bottom)</td>
      <td>OFF: 0.25ON: 0.24</td>
      <td>OFF: 0.24ON: 0.24</td>
      <td>OFF: 0.16ON: 0.16</td>
      <td>OFF: 0.023ON: 0.022</td>
      <td>OFF: 0.046ON: 0.045</td>
      <td>Wilcoxon signed-rank test</td>
      <td>V = 832</td>
      <td>52</td>
      <td>NA</td>
      <td>0.19</td>
      <td>0.18</td>
    </tr>
    <tr>
      <td>iMM shell adapting (laser OFF vs. ON)</td>
      <td>Figure 3E (top)</td>
      <td>OFF: 0.34ON: 0.31</td>
      <td>OFF: 0.32ON: 0.28</td>
      <td>OFF: 0.19ON: 0.20</td>
      <td>OFF: 0.017ON: 0.019</td>
      <td>OFF: 0.035ON: 0.037</td>
      <td>Wilcoxon signed-rank test</td>
      <td>V = 4283</td>
      <td>113</td>
      <td>NA</td>
      <td>0.0023</td>
      <td>0.29</td>
    </tr>
    <tr>
      <td>iPE shell adapting (laser OFF vs. ON)</td>
      <td>Figure 3E (middle)</td>
      <td>OFF: 0.15ON: 0.14</td>
      <td>OFF: 0.12ON: 0.10</td>
      <td>OFF: 0.30ON: 0.30</td>
      <td>OFF: 0.028ON: 0.028</td>
      <td>OFF: 0.056ON: 0.056</td>
      <td>Wilcoxon signed-rank test</td>
      <td>V = 3963</td>
      <td>113</td>
      <td>NA</td>
      <td>0.034</td>
      <td>0.20</td>
    </tr>
    <tr>
      <td>iRS shell adapting (laser OFF vs. ON)</td>
      <td>Figure 3E (bottom)</td>
      <td>OFF: 0.19ON: 0.17</td>
      <td>OFF: 0.19ON: 0.16</td>
      <td>OFF: 0.24ON: 0.24</td>
      <td>OFF: 0.023ON: 0.023</td>
      <td>OFF: 0.045ON: 0.045</td>
      <td>Paired t-test</td>
      <td>t = 1.6</td>
      <td>113</td>
      <td>112</td>
      <td>0.11</td>
      <td>0.15</td>
    </tr>
    <tr>
      <td>iMM central facilitating (laser OFF vs. ON)</td>
      <td>Figure 3G (top)</td>
      <td>OFF: –0.32ON: –0.13</td>
      <td>OFF: –0.31ON: –0.11</td>
      <td>OFF: 0.16ON: 0.19</td>
      <td>OFF: 0.042ON: 0.050</td>
      <td>OFF: 0.090ON: 0.11</td>
      <td>Paired t-test</td>
      <td>t = –3.5</td>
      <td>14</td>
      <td>13</td>
      <td>0.0036</td>
      <td>0.95</td>
    </tr>
    <tr>
      <td>iPE central facilitating (laser OFF vs. ON)</td>
      <td>Figure 3G (middle)</td>
      <td>OFF: –0.20ON: –0.17</td>
      <td>OFF: –0.24ON: –0.20</td>
      <td>OFF: 0.20ON: 0.17</td>
      <td>OFF: 0.054ON: 0.044</td>
      <td>OFF: 0.12ON: 0.095</td>
      <td>Paired t-test</td>
      <td>t = –1.2</td>
      <td>14</td>
      <td>13</td>
      <td>0.25</td>
      <td>0.32</td>
    </tr>
    <tr>
      <td>iRS central facilitating (laser OFF vs. ON)</td>
      <td>Figure 3G (bottom)</td>
      <td>OFF: –0.12ON: 0.036</td>
      <td>OFF: –0.092ON: 0.069</td>
      <td>OFF: 0.18ON: 0.24</td>
      <td>OFF: 0.049ON: 0.064</td>
      <td>OFF: 0.11ON: 0.14</td>
      <td>Paired t-test</td>
      <td>t = –3.7</td>
      <td>14</td>
      <td>13</td>
      <td>0.0026</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td>iMM shell facilitating (laser OFF vs. ON)</td>
      <td>Figure 3H (top)</td>
      <td>OFF: –0.29ON: –0.19</td>
      <td>OFF: –0.24ON: –0.15</td>
      <td>OFF: 0.15ON: 0.16</td>
      <td>OFF: 0.024ON: 0.026</td>
      <td>OFF: 0.048ON: 0.052</td>
      <td>Wilcoxon signed-rank test</td>
      <td>V = 159</td>
      <td>38</td>
      <td>NA</td>
      <td>0.0016</td>
      <td>0.50</td>
    </tr>
    <tr>
      <td>iPE shell facilitating (laser OFF vs. ON)</td>
      <td>Figure 3H (middle)</td>
      <td>OFF: –0.026ON: 0.033</td>
      <td>OFF: 0.011ON: 0.023</td>
      <td>OFF: 0.26ON: 0.29</td>
      <td>OFF: 0.042ON: 0.047</td>
      <td>OFF: 0.085ON: 0.096</td>
      <td>Wilcoxon signed-rank test</td>
      <td>V = 227</td>
      <td>38</td>
      <td>NA</td>
      <td>0.037</td>
      <td>0.34</td>
    </tr>
    <tr>
      <td>iRS shell facilitating (laser OFF vs. ON)</td>
      <td>Figure 3H (bottom)</td>
      <td>OFF: –0.26ON: –0.23</td>
      <td>OFF: –0.29ON: –0.23</td>
      <td>OFF: 0.32ON: 0.33</td>
      <td>OFF: 0.052ON: 0.054</td>
      <td>OFF: 0.11ON: 0.11</td>
      <td>Wilcoxon signed-rank test</td>
      <td>V = 254</td>
      <td>38</td>
      <td>NA</td>
      <td>0.093</td>
      <td>0.27</td>
    </tr>
    <tr>
      <td>iMM central nonadapting (laser OFF vs. ON)</td>
      <td>Figure 4C (top)</td>
      <td>OFF: 0.022ON: 0.072</td>
      <td>OFF: 0.023ON: 0.065</td>
      <td>OFF: 0.12ON: 0.14</td>
      <td>OFF: 0.0094ON: 0.011</td>
      <td>OFF: 0.019ON: 0.022</td>
      <td>Wilcoxon signed-rank test</td>
      <td>V = 3419</td>
      <td>155</td>
      <td>NA</td>
      <td>2.7e-06</td>
      <td>0.38</td>
    </tr>
    <tr>
      <td>iPE central nonadapting (laser OFF vs. ON)</td>
      <td>Figure 4C (middle top)</td>
      <td>OFF: –0.096ON: –0.081</td>
      <td>OFF: –0.098ON: –0.093</td>
      <td>OFF: 0.19ON: 0.19</td>
      <td>OFF: 0.015ON: 0.015</td>
      <td>OFF: 0.030ON: 0.030</td>
      <td>Wilcoxon signed-rank test</td>
      <td>V = 5327</td>
      <td>155</td>
      <td>NA</td>
      <td>0.20</td>
      <td>0.10</td>
    </tr>
    <tr>
      <td>iRS central nonadapting (laser OFF vs. ON)</td>
      <td>Figure 4C (middle bottom)</td>
      <td>OFF: 0.12ON: 0.15</td>
      <td>OFF: 0.12ON: 0.15</td>
      <td>OFF: 0.15ON: 0.17</td>
      <td>OFF: 0.012ON: 0.013</td>
      <td>OFF: 0.024ON: 0.027</td>
      <td>Wilcoxon signed-rank test</td>
      <td>V = 4224</td>
      <td>155</td>
      <td>NA</td>
      <td>0.0011</td>
      <td>0.26</td>
    </tr>
    <tr>
      <td>iRS &gt; 0 central nonadapting (laser OFF vs. ON)</td>
      <td>Figure 4C (bottom)</td>
      <td>OFF: 0.17ON: 0.19</td>
      <td>OFF: 0.16ON: 0.18</td>
      <td>OFF: 0.10ON: 0.15</td>
      <td>OFF: 9.1e-03ON: 0.013</td>
      <td>OFF: 1.8e-02ON: 0.026</td>
      <td>Wilcoxon signed-rank test</td>
      <td>V = 3313</td>
      <td>127</td>
      <td>NA</td>
      <td>0.071</td>
      <td>0.16</td>
    </tr>
    <tr>
      <td>iRS &lt; 0 central nonadapting (laser OFF vs. ON)</td>
      <td>Figure 4C (bottom)</td>
      <td>OFF: –0.13ON: –0.012</td>
      <td>OFF: –0.10ON: –0.017</td>
      <td>OFF: 0.11ON: 0.15</td>
      <td>OFF: 0.021ON: 0.029</td>
      <td>OFF: 0.044ON: 0.060</td>
      <td>Wilcoxon signed-rank test</td>
      <td>V = 30</td>
      <td>25</td>
      <td>NA</td>
      <td>0.00012</td>
      <td>0.71</td>
    </tr>
    <tr>
      <td>iMM shell nonadapting (laser OFF vs. ON)</td>
      <td>Figure 4D (top)</td>
      <td>OFF: 0.0053ON: 0.023</td>
      <td>OFF: 0.0062ON: 0.028</td>
      <td>OFF: 0.13ON: 0.16</td>
      <td>OFF: 0.0081ON: 0.010</td>
      <td>OFF: 0.016ON: 0.020</td>
      <td>Wilcoxon signed-rank test</td>
      <td>V = 12,765</td>
      <td>243</td>
      <td>NA</td>
      <td>0.076</td>
      <td>0.11</td>
    </tr>
    <tr>
      <td>iPE shell nonadapting (laser OFF vs. ON)</td>
      <td>Figure 4D (middle)</td>
      <td>OFF: 0.053ON: 0.072</td>
      <td>OFF: 0.059ON: 0.061</td>
      <td>OFF: 0.21ON: 0.20</td>
      <td>OFF: 0.013ON: 0.013</td>
      <td>OFF: 0.026ON: 0.026</td>
      <td>Wilcoxon signed-rank test</td>
      <td>V = 13,474</td>
      <td>243</td>
      <td>NA</td>
      <td>0.22</td>
      <td>0.079</td>
    </tr>
    <tr>
      <td>iRS shell nonadapting (laser OFF vs. ON)</td>
      <td>Figure 4D (bottom)</td>
      <td>OFF: –0.048ON: –0.049</td>
      <td>OFF: –0.042ON: –0.041</td>
      <td>OFF: 0.23ON: 0.22</td>
      <td>OFF: 0.015ON: 0.014</td>
      <td>OFF: 0.029ON: 0.028</td>
      <td>Wilcoxon signed-rank test</td>
      <td>V = 14,344</td>
      <td>243</td>
      <td>NA</td>
      <td>0.66</td>
      <td>0.028</td>
    </tr>
    <tr>
      <td>FR change standard central adapting</td>
      <td>Figure 5A</td>
      <td>2.1</td>
      <td>2.0</td>
      <td>5.6</td>
      <td>0.78</td>
      <td>1.6</td>
      <td>One-sample t-test</td>
      <td>t = 2.7</td>
      <td>52</td>
      <td>51</td>
      <td>0.0092</td>
      <td>0.38</td>
    </tr>
    <tr>
      <td>FR change cascade central adapting</td>
      <td>Figure 5A</td>
      <td>–0.38</td>
      <td>0.67</td>
      <td>6.9</td>
      <td>0.95</td>
      <td>1.9</td>
      <td>One-sample t-test</td>
      <td>t = –0.40</td>
      <td>52</td>
      <td>51</td>
      <td>0.69</td>
      <td>0.056</td>
    </tr>
    <tr>
      <td>FR change deviant central adapting</td>
      <td>Figure 5A</td>
      <td>–2.3</td>
      <td>–2.2</td>
      <td>5.6</td>
      <td>0.78</td>
      <td>1.6</td>
      <td>One-sample t-test</td>
      <td>t = –2.9</td>
      <td>52</td>
      <td>51</td>
      <td>0.0054</td>
      <td>0.40</td>
    </tr>
    <tr>
      <td>FR change standard shell adapting</td>
      <td>Figure 5B</td>
      <td>0.64</td>
      <td>0.89</td>
      <td>5.3</td>
      <td>0.50</td>
      <td>0.98</td>
      <td>One-sample Wilcoxon test</td>
      <td>V = 3760</td>
      <td>113</td>
      <td>NA</td>
      <td>0.035</td>
      <td>0.20</td>
    </tr>
    <tr>
      <td>FR change cascade shell adapting</td>
      <td>Figure 5B</td>
      <td>0.50</td>
      <td>0.44</td>
      <td>7.3</td>
      <td>0.68</td>
      <td>1.4</td>
      <td>One-sample t-test</td>
      <td>t = 0.74</td>
      <td>113</td>
      <td>112</td>
      <td>0.46</td>
      <td>0.069</td>
    </tr>
    <tr>
      <td>FR change deviant shell adapting</td>
      <td>Figure 5B</td>
      <td>–1.8</td>
      <td>–1.3</td>
      <td>7.4</td>
      <td>0.69</td>
      <td>1.4</td>
      <td>One-sample Wilcoxon test</td>
      <td>V = 2040</td>
      <td>113</td>
      <td>NA</td>
      <td>0.0057</td>
      <td>0.26</td>
    </tr>
    <tr>
      <td>FR change standard central facilitating</td>
      <td>Figure 5C</td>
      <td>–6.3</td>
      <td>–7.3</td>
      <td>5.8</td>
      <td>1.6</td>
      <td>3.4</td>
      <td>One-sample t-test</td>
      <td>t = –4.1</td>
      <td>14</td>
      <td>13</td>
      <td>0.0013</td>
      <td>1.1</td>
    </tr>
    <tr>
      <td>FR change cascade central facilitating</td>
      <td>Figure 5C</td>
      <td>–0.44</td>
      <td>–0.89</td>
      <td>4.1</td>
      <td>1.1</td>
      <td>2.4</td>
      <td>One-sample t-test</td>
      <td>t = –0.40</td>
      <td>14</td>
      <td>13</td>
      <td>0.69</td>
      <td>0.11</td>
    </tr>
    <tr>
      <td>FR change deviant central facilitating</td>
      <td>Figure 5C</td>
      <td>1.5</td>
      <td>1.3</td>
      <td>3.4</td>
      <td>0.92</td>
      <td>2.0</td>
      <td>One-sample t-test</td>
      <td>t = 1.7</td>
      <td>14</td>
      <td>13</td>
      <td>0.12</td>
      <td>0.45</td>
    </tr>
    <tr>
      <td>FR change standard shell facilitating</td>
      <td>Figure 5D</td>
      <td>–2.7</td>
      <td>–3.1</td>
      <td>5.4</td>
      <td>0.87</td>
      <td>1.8</td>
      <td>One-sample t-test</td>
      <td>t = –3.1</td>
      <td>38</td>
      <td>37</td>
      <td>0.0042</td>
      <td>0.50</td>
    </tr>
    <tr>
      <td>FR change cascade shell facilitating</td>
      <td>Figure 5D</td>
      <td>0.36</td>
      <td>0.44</td>
      <td>5.1</td>
      <td>0.84</td>
      <td>1.7</td>
      <td>One-sample t-test</td>
      <td>t = 0.43</td>
      <td>38</td>
      <td>37</td>
      <td>0.67</td>
      <td>0.070</td>
    </tr>
    <tr>
      <td>FR change deviant shell facilitating</td>
      <td>Figure 5D</td>
      <td>2.6</td>
      <td>2.7</td>
      <td>4.5</td>
      <td>0.74</td>
      <td>1.5</td>
      <td>One-sample t-test</td>
      <td>t = 3.5</td>
      <td>38</td>
      <td>37</td>
      <td>0.0013</td>
      <td>0.57</td>
    </tr>
    <tr>
      <td>FR change standard central nonadapting</td>
      <td>Figure 5E</td>
      <td>–2.5</td>
      <td>–2.2</td>
      <td>6.2</td>
      <td>0.50</td>
      <td>0.99</td>
      <td>One-sample Wilcoxon test</td>
      <td>V = 2995</td>
      <td>155</td>
      <td>NA</td>
      <td>1.4e-06</td>
      <td>0.38</td>
    </tr>
    <tr>
      <td>FR change cascade central nonadapting</td>
      <td>Figure 5E</td>
      <td>–0.68</td>
      <td>–0.44</td>
      <td>6.3</td>
      <td>0.51</td>
      <td>1.0</td>
      <td>One-sample t-test</td>
      <td>t = –1.3</td>
      <td>155</td>
      <td>154</td>
      <td>0.18</td>
      <td>0.11</td>
    </tr>
    <tr>
      <td>FR change deviant central nonadapting</td>
      <td>Figure 5E</td>
      <td>0.57</td>
      <td>0.0</td>
      <td>5.8</td>
      <td>0.47</td>
      <td>0.93</td>
      <td>One-sample t-test</td>
      <td>t = 1.2</td>
      <td>155</td>
      <td>154</td>
      <td>0.22</td>
      <td>0.098</td>
    </tr>
    <tr>
      <td>FR change standard shell nonadapting</td>
      <td>Figure 5F</td>
      <td>–0.63</td>
      <td>–0.44</td>
      <td>5.3</td>
      <td>0.34</td>
      <td>0.68</td>
      <td>One-sample Wilcoxon test</td>
      <td>V = 11,050</td>
      <td>243</td>
      <td>NA</td>
      <td>0.035</td>
      <td>0.14</td>
    </tr>
    <tr>
      <td>FR change cascade shell nonadapting</td>
      <td>Figure 5F</td>
      <td>–0.51</td>
      <td>–0.44</td>
      <td>5.1</td>
      <td>0.32</td>
      <td>0.64</td>
      <td>One-sample Wilcoxon test</td>
      <td>V = 12,157</td>
      <td>243</td>
      <td>NA</td>
      <td>0.15</td>
      <td>0.089</td>
    </tr>
    <tr>
      <td>FR change deviant shell nonadapting</td>
      <td>Figure 5F</td>
      <td>–0.059</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>0.32</td>
      <td>0.64</td>
      <td>One-sample t-test</td>
      <td>t = –0.18</td>
      <td>243</td>
      <td>242</td>
      <td>0.86</td>
      <td>0.012</td>
    </tr>
    <tr>
      <td>FR central facilitating (first vs. last standard)</td>
      <td>Figure 6C</td>
      <td>First: 31Last: 36</td>
      <td>First: 29Last: 31</td>
      <td>First: 15Last: 16</td>
      <td>First: 3.9Last: 4.4</td>
      <td>First: 8.5Last: 9.5</td>
      <td>Wilcoxon signed-rank test</td>
      <td>V = 0</td>
      <td>14</td>
      <td>NA</td>
      <td>0.0017</td>
      <td>0.87</td>
    </tr>
    <tr>
      <td>FR shell facilitating (first vs. last standard)</td>
      <td>Figure 6D</td>
      <td>First: 53Last: 57</td>
      <td>First: 38Last: 42</td>
      <td>First: 38Last: 42</td>
      <td>First: 6.2Last: 6.8</td>
      <td>First: 13Last: 14</td>
      <td>Wilcoxon signed-rank test</td>
      <td>V = 92</td>
      <td>38</td>
      <td>NA</td>
      <td>9.3e-05</td>
      <td>0.64</td>
    </tr>
    <tr>
      <td>FR central adapting (cascade vs. many standards)</td>
      <td>Figure 3—figure supplement 2B (left)</td>
      <td>Casc: 61MS: 63</td>
      <td>Casc: 50MS: 52</td>
      <td>Casc: 38MS: 40</td>
      <td>Casc: 5.2MS: 5.6</td>
      <td>Casc: 10MS: 11</td>
      <td>Wilcoxon signed-rank test</td>
      <td>V = 595</td>
      <td>52</td>
      <td>NA</td>
      <td>0.39</td>
      <td>0.12</td>
    </tr>
    <tr>
      <td>FR central facilitating (cascade vs. many standards)</td>
      <td>Figure 3—figure supplement 2B (right)</td>
      <td>Casc: 29MS: 31</td>
      <td>Casc: 26MS: 28</td>
      <td>Casc: 14MS: 16</td>
      <td>Casc: 3.8MS: 4.3</td>
      <td>Casc: 8.2MS: 9.3</td>
      <td>Wilcoxon signed-rank test</td>
      <td>V = 41</td>
      <td>14</td>
      <td>NA</td>
      <td>0.49</td>
      <td>0.19</td>
    </tr>
    <tr>
      <td>FR shell adapting (cascade vs. many standards)</td>
      <td>Figure 3—figure supplement 2C (left)</td>
      <td>Casc: 64MS: 66</td>
      <td>Casc: 43MS: 41</td>
      <td>Casc: 61MS: 68</td>
      <td>Casc: 5.7MS: 6.4</td>
      <td>Casc: 11MS: 13</td>
      <td>Wilcoxon signed-rank test</td>
      <td>V = 2653</td>
      <td>113</td>
      <td>NA</td>
      <td>0.46</td>
      <td>0.064</td>
    </tr>
    <tr>
      <td>FR shell facilitating (cascade vs. many standards)</td>
      <td>Figure 3—figure supplement 2C (right)</td>
      <td>Casc: 43MS: 45</td>
      <td>Casc: 24MS: 28</td>
      <td>Casc: 41MS: 52</td>
      <td>Casc: 6.6MS: 8.4</td>
      <td>Casc: 13MS: 17</td>
      <td>Wilcoxon signed-rank test</td>
      <td>V = 264.5</td>
      <td>38</td>
      <td>NA</td>
      <td>0.41</td>
      <td>0.14</td>
    </tr>
    <tr>
      <td>Central iMM OFF (single vs. multiunit)</td>
      <td>Figure 3—figure supplement 3 (left)</td>
      <td>Single: 0.045Multi: 0.057</td>
      <td>Single: 0.048Multi: 0.064</td>
      <td>Single: 0.15Multi: 0.18</td>
      <td>Single: 0.052Multi: 0.013</td>
      <td>Single: 0.12Multi: 0.025</td>
      <td>Wilcoxon rank-sum test</td>
      <td>W = 825</td>
      <td>Single: 8Multi: 213</td>
      <td>NA</td>
      <td>0.88</td>
      <td>0.010</td>
    </tr>
    <tr>
      <td>Central iMM ON (single vs. multiunit)</td>
      <td>Figure 3—figure supplement 3 (left)</td>
      <td>Single: 0.087Multi: 0.092</td>
      <td>Single: 0.085Multi: 0.086</td>
      <td>Single: 0.17Multi: 0.16</td>
      <td>Single: 0.059Multi: 0.011</td>
      <td>Single: 0.14Multi: 0.022</td>
      <td>Student’s t-test</td>
      <td>t = –0.093</td>
      <td>Single: 8Multi: 213</td>
      <td>7.5</td>
      <td>0.93</td>
      <td>0.034</td>
    </tr>
    <tr>
      <td>Shell iMM OFF (single vs. multiunit)</td>
      <td>Figure 3—figure supplement 3 (right)</td>
      <td>Single: 0.035Multi: 0.081</td>
      <td>Single: 0.028Multi: 0.055</td>
      <td>Single: 0.18Multi: 0.25</td>
      <td>Single: 0.022Multi: 0.014</td>
      <td>Single: 0.045Multi: 0.027</td>
      <td>Wilcoxon rank-sum test</td>
      <td>W = 9832</td>
      <td>Single: 67Multi: 327</td>
      <td>NA</td>
      <td>0.19</td>
      <td>0.067</td>
    </tr>
    <tr>
      <td>Shell iMM ON (single vs. multiunit)</td>
      <td>Figure 3—figure supplement 3 (right)</td>
      <td>Single: 0.046Multi: 0.091</td>
      <td>Single: 0.045Multi: 0.072</td>
      <td>Single: 0.21Multi: 0.23</td>
      <td>Single: 0.026Multi: 0.013</td>
      <td>Single: 0.051Multi: 0.025</td>
      <td>Wilcoxon rank-sum test</td>
      <td>W = 9883</td>
      <td>Single: 67Multi: 327</td>
      <td>NA</td>
      <td>0.21</td>
      <td>0.064</td>
    </tr>
  </tbody>
</table>

_iRS: index of repetition suppression; iPE: index of prediction error; iMM: index of neuronal mismatch; Aw: awake; An: anesthetized; casc: cascading; MS: many standards._

### Parsing of recording sites into central and shell locations

Shell and central regions of IC differ in their tuning, degree of adaptation, and amount of input from AC, and may also play distinct roles in predictive processing (Aitkin et al., 1975; Bajo et al., 2007; Blackwell et al., 2020; Duque et al., 2012; Herbert et al., 1991; Stebbings et al., 2014; Syka et al., 2000). We quantitatively parsed our recording sites by exploiting known differences in the sharpness of tuning and direction of frequency gradients between shell and central regions: shell IC neurons tend to have broader frequency tuning (low sparseness) than central IC neurons, and the central IC is characterized by a highly stereotyped tonotopic gradient with depth (Figure 1—figure supplement 2A; Aitkin et al., 1975; Chen et al., 2012; Malmierca et al., 2008; Stiebler and Ehret, 1985; Syka et al., 2000). Similar to previously established procedures used in human and monkey IC research, we performed clustering analysis using the mean sparsity and variation in best frequency with depth from each recording site to determine whether it was from the central nucleus or shell regions of IC (Figure 1—figure supplement 2B and C; Bulkin and Groh, 2011; Ress and Chandrasekaran, 2013). In a subset of recordings, we also marked the recording electrode with a lipophilic dye to histologically confirm the recording location (Figure 1—figure supplement 2D).

![Figure 2.](https://cdn.elifesciences.org/articles/73289/elife-73289-fig2-v2.jpg)

**Figure 2.:** (A) Experimental design for recording in the awake and isoflurane anesthetized IC in the same population of units. (B) Distribution of index of neuronal mismatch (iMM) in the awake vs. anesthetized central IC. Bar plots represent means over the population of n = 39 units. Error bars are standard error of the mean. (C) Index of prediction error (iPE) distribution in the awake vs. anesthetized central IC. (D) Index of repetition suppression (iRS) distribution in the awake vs. anesthetized central IC. (E) Distribution of iMM in the awake vs. anesthetized shell IC. Bar plots represent means over the population of n = 165 units. Error bars are standard error of the mean. (F) iPE distribution in the awake vs. anesthetized shell IC. (G) iRS distribution in the awake vs. anesthetized shell IC. Data is from four recording sessions in one mouse.

IC units in both regions exhibited multiple response types to pure tone stimuli (Figure 1—figure supplement 2E). In addition to excitatory responses (e.g., onset and sustained responses), inhibited and offset responses were common, as has previously been characterized in IC of awake animals (Figure 1—figure supplement 2E, top right, bottom middle; Duque and Malmierca, 2015). Consistent with previous findings, tuning curves from central regions were sharp and narrow, whereas units in shell regions exhibited broad frequency tuning (Figure 1—figure supplement 2F, left vs. right; Aitkin et al., 1975; Syka et al., 2000). Inhibited side bands were common in tuning curves from both regions, and some inhibited tuning curves were observed (Figure 1—figure supplement 2G). These data confirm that our experimental parameters elicit sound responses and tuning properties characteristic of central and shell regions of the awake IC (Aitkin et al., 1975; Duque and Malmierca, 2015; Syka et al., 2000).

### IC units encode different aspects of prediction and repetition in awake and anesthetized states

Much of the research regarding SSA and deviance detection in IC to date has been performed in anesthetized animals, with few studies recording from awake subjects (Duque and Malmierca, 2015; Parras et al., 2017). Given that neuronal responses to sound depend on the state of anesthesia of the subject, it is possible that there are differences in predictive coding metrics between the awake and anesthetized states (Fontanini and Katz, 2008; Gaese and Ostwald, 2001; Schumacher et al., 2011). While previous studies have characterized how anesthesia affects SSA, it remains unknown whether its component repetition and prediction metrics differ with anesthetic state (Duque and Malmierca, 2015). Therefore, we first characterized how anesthesia affects these predictive coding metrics in a subset of animals. We first performed awake recordings and then repeated our experimental procedures, leaving the animal head-fixed and the probe in place, after anesthetizing the mouse with isoflurane (Figure 2A). This protocol allowed us to compare how metrics of predictive coding differ between the awake and anesthetized preparations in the same population of units.

In the central IC, the mean iMM in the anesthetized condition was positive, indicative of prevalent adaptation (Figure 2B). The iMM values under anesthesia were significantly higher than those obtained while the animal was awake (Figure 2B, Table 1; p=8.8e-05, Wilcoxon rank-sum test). To better understand what prediction or repetition effects underlie iMM in each condition, the iMM for both distributions was further decomposed into an iPE and iRS. In the anesthetized condition, the mean iPE value of 0.077 indicated the presence of modest prediction error, while a mean iPE of –0.13 indicated that negative prediction error is significantly more prevalent in the awake condition (Figure 2C, Table 1; p=0.017, Student’s t-test). Under both anesthetized and awake conditions, prominent repetition suppression was observed in the central IC (Figure 2D).

Similar to the central IC, the mean iMM was significantly more positive in shell regions during anesthesia (Figure 2E, Table 1; p=3.5e-08, Wilcoxon rank-sum test). A greater proportion of units in the awake condition had a negative iMM compared with the anesthetized distribution, indicating that facilitation (a greater response to the standard than the deviant context) is more common in the awake than the anesthetized condition (Figure 2E). The iPE values in shell IC suggest that prediction error is significantly higher in the awake compared to the anesthetized condition (Figure 2F, Table 1; p=2.6e-05, Wilcoxon rank-sum test). Although the distribution for the iRS under anesthesia had a positive mean of 0.25, indicating prevalent repetition suppression, the awake distribution exhibited a significant leftward shift by comparison (Figure 2G). Interestingly, the mean iRS for the awake condition was negative (mean = −0.056), indicating that repetition enhancement, rather than suppression, is present in the awake shell IC (Figure 2G, Table 1; p=2.5e-16, Wilcoxon rank-sum test). These results point to differences between predictive coding metrics in the awake and anesthetized states, with previously undescribed metrics such as repetition enhancement and negative prediction error more prominent in awake animals.

### Adapting and facilitating units are differentially affected by cortico-collicular inactivation

We next performed recordings in IC of awake mice to determine how neuronal mismatch and its component repetition and prediction metrics were affected by cortico-collicular inactivation (Figure 3A). To inactivate cortico-collicular feedback, we shined light over AC in subjects that expressed a suppressive opsin in cortico-collicular neurons. We segregated the population of recorded units according to those that exhibited a significantly stronger response to the deviant than the standard (adapting units; Figure 3B, blue; Figure 5C), those that exhibited a significantly stronger response to the standard than the deviant (facilitating units; Figure 3B, red; Figure 5F), and those that responded equally to both stimulus contexts (nonadapting units; Figure 3B, green) for recordings in both central and shell regions of IC (Figure 3B, left vs. right).

![Figure 3.](https://cdn.elifesciences.org/articles/73289/elife-73289-fig3-v2.jpg)

**Figure 3.:** (A) Experimental design for recording in awake IC during laser inactivation of the cortico-collicular pathway. (B) Categorization of units according to whether they displayed significant adaptation, facilitation, or neither (nonadapting). (C) Average peristimulus time histogram for adapting units in central (top) and shell (bottom) IC. Green = during laser inactivation. (D) Index of neuronal mismatch (iMM) (top), index of prediction error (iPE) (middle), and index of repetition suppression (iRS) (bottom) for adapting units in the central nucleus. Dots represent recorded units. Bar plots represent means over the population of n = 52 units. Error bars are standard error of the mean. (E) iMM (top), iPE (middle), and iRS (bottom) for adapting units in shell regions of IC. Dots represent recorded units. Bar plots represent means over the population of n = 113 units. Error bars are standard error of the mean. (F) Average peristimulus time histogram for facilitating units in central (top) and shell (bottom) IC. Green = during laser inactivation. (G) iMM (top), iPE (middle), and iRS (bottom) for facilitating units in the central nucleus. Dots represent recorded units. Bar plots represent means over the population of n = 14 units. Error bars are standard error of the mean. (H) iMM (top), iPE (middle), and iRS (bottom) for facilitating units in shell regions of IC. Dots represent recorded units. Bar plots represent means over the population of n = 38 units. Error bars are standard error of the mean.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/73289/elife-73289-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Experimental design for control experiments. All procedures were performed identically to the experimental group, except with the omission of ArchT from the viral construct injected in the auditory cortex (AC). (B) Comparison of the index of neuronal mismatch (iMM) distribution for control (navy) and experimental (light blue) groups in central (left) and shell (right) inferior colliculus (IC). (C) iMM (top), index of prediction error (iPE) (middle), and index of repetition suppression (iRS) (bottom) for control adapting units in the central nucleus. Dots represent recorded units. Bar plots represent means over the population of n = 18 units. Error bars are standard error of the mean. (D) iMM (top), iPE (middle), and iRS (bottom) for control adapting units in shell regions of IC. Dots represent recorded units. Bar plots represent means over the population of n = 35 units. Error bars are standard error of the mean. (E) iMM (top), iPE (middle), and iRS (bottom) for control facilitating units in the central nucleus. Dots represent recorded units. Bar plots represent means over the population of n = 4 units. Error bars are standard error of the mean. (F) iMM (top), iPE (middle), and iRS (bottom) for control facilitating units in shell regions of IC. Dots represent recorded units. Bar plots represent means over the population of n = 21 units. Error bars are standard error of the mean. (G) iMM (top), iPE (middle), and iRS (bottom) for control nonadapting units in the central nucleus. Dots represent recorded units. Bar plots represent means over the population of n = 55 units. Error bars are standard error of the mean. (H) iMM (top), iPE (middle), and iRS (bottom) for control nonadapting units in shell regions of IC. Dots represent recorded units. Bar plots represent means over the population of n = 63 units. Error bars are standard error of the mean.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/73289/elife-73289-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A) The many standards sequence consists of the same 10 tones found in the cascade sequence, but the tone order is random. Responses to the cascade and many standards sequences were compared to assess whether cross-frequency adaptation or global stimulus regularity affects responses to the cascade condition. (B) Firing rates of adapting units (left) and facilitating units (right) in the central inferior colliculus (IC) to tones in the cascade and many standards contexts. Dots represent recorded units. Bar plots represent means over the population of n = 52 adapting and n = 14 facilitating units. Error bars are standard error of the mean. (C) Firing rates of adapting units (left) and facilitating units (right) in the shell IC to tones in the cascade and many standards contexts. Dots represent recorded units. Bar plots represent means over the population of n = 113 adapting and n = 38 facilitating units. Error bars are standard error of the mean.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/73289/elife-73289-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** The iMM for laser OFF (x-axis) and laser ON (y-axis) trials for each region of the IC separated by single- (displayed in teal) and multiunits.

The iMM for adapting units in the central nucleus significantly decreased with laser inactivation of cortico-collicular neurons (Figure 3D, top; Table 1; p=0.00034, Wilcoxon signed-rank test). The iMM at baseline for adapting units predominantly represents repetition suppression (Figure 3D, bottom) and a small amount of prediction error (Figure 3D, middle). Prediction error was abolished during laser inactivation (Figure 3D, middle; Table 1; p=0.048, Wilcoxon signed-rank test), while repetition suppression remained unaffected (Figure 3D, bottom). Adapting units in shell regions of IC exhibited a similar pattern to those in the central nucleus. At baseline, these units encoded both prediction error and repetition suppression (Figure 3E, middle and bottom). A significant decrease in iMM during laser inactivation (Figure 3E, top; Table 1; p=0.0023, Wilcoxon signed-rank test) was driven by a decrease in prediction error (Figure 3E, middle; Table 1; p=0.034, Wilcoxon signed-rank test), whereas repetition suppression remained unaffected (Figure 3E, bottom). Combined, these results suggest that removing cortical feedback reduced prediction error but not repetition suppression in adapting units.

Prior studies of deviance detection in IC have focused exclusively on adapting units. However, given the relative prevalence of facilitating units discovered in the awake versus anesthetized IC (Figure 2), we further investigated this population of units to determine whether facilitation reflects prediction or repetition effects. In the central nucleus, cortico-collicular inactivation led to a significant decrease in facilitation in facilitating units (Figure 3G, top; Table 1; p=0.0036, Student’s t-test). At baseline, the iMM for facilitating units represents a combination of negative prediction error and repetition enhancement (Figure 3G, middle and bottom). During inactivation, negative prediction error remained unaffected (Figure 3G, middle), while repetition enhancement was nearly abolished (Figure 3G, bottom; Table 1; p=0.0026, Student’s t-test). Facilitating units in the shell IC were also significantly affected by cortico-collicular inactivation (Figure 3H, top; Table 1; p=0.0016, Wilcoxon signed-rank test). In this case, however, the change in iMM was driven by the near abolishment of negative prediction error (Figure 3H, middle; Table 1; p=0.037, Wilcoxon signed-rank test), while repetition enhancement was unaffected (Figure 3H, bottom).

These data suggest that adaptation and facilitation in the awake IC are composed of distinct underlying processes: adapting populations in both central and shell regions of IC exhibit prediction error and repetition suppression, while facilitating populations are characterized by negative prediction error and repetition enhancement. In adapting units in both central and shell regions, cortico-collicular inactivation significantly decreases prediction error. Facilitating units in the central IC display decreased repetition enhancement with cortico-collicular inactivation, while those in shell regions exhibit decreased negative prediction error. To ensure that the laser-induced changes described above were opsin-mediated, we performed control experiments in two mice with identical manipulations to the experimental group, but in the absence of ArchT (Figure 3—figure supplement 1A). At baseline, the control group exhibited a similar distribution of iMM values to the experimental group in both the central and shell regions of IC (Figure 3—figure supplement 1B, Table 2). Similar proportions of adapting/facilitating/nonadapting units were also found in the control (central: 23% adapting, 5% facilitating, 71% nonadapting; shell: 29% adapting, 18% facilitating, 53% nonadapting) and experimental groups (central: 24% adapting, 6% facilitating, 70% nonadapting; shell: 29% adapting, 9% facilitating, 62% nonadapting). We found no significant differences between baseline and laser trials for either adapting (Figure 3—figure supplement 1C and D, Table 2) or facilitating (Figure 3—figure supplement 1E and F) units in either region. This experiment confirmed that the observed effects of cortico-collicular inactivation were indeed due to opsin-mediated inactivation of the cortico-collicular projection neurons.

**Table 2.**
 Statistical comparisons for control data.


<table>
  <thead>
    <tr>
      <th>Comparison</th>
      <th>Figure</th>
      <th>Mean</th>
      <th>Median</th>
      <th>SD</th>
      <th>SEM</th>
      <th>CI (±)</th>
      <th>Test</th>
      <th>Test statistic</th>
      <th>N</th>
      <th>df</th>
      <th>p</th>
      <th>Effect size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>iMM central (control vs. experimental)</td>
      <td>Figure 3—figure supplement 1B (left)</td>
      <td>Con: 0.092Exp: 0.057</td>
      <td>Con: 0.086Exp: 0.064</td>
      <td>Con: 0.16Exp: 0.18</td>
      <td>Con: 0.011Exp: 0.012</td>
      <td>Con: 0.022Exp: 0.024</td>
      <td>Wilcoxon rank-sum test</td>
      <td>W = 7919</td>
      <td>77 (control)221 (exp.)</td>
      <td>NA</td>
      <td>0.37</td>
      <td>0.052</td>
    </tr>
    <tr>
      <td>iMM shell (control vs. experimental)</td>
      <td>Figure 3—figure supplement 1B (right)</td>
      <td>Con: 0.083Exp: 0.073</td>
      <td>Con: 0.069Exp: 0.053</td>
      <td>Con: 0.23Exp: 0.24</td>
      <td>Con: 0.012Exp: 0.012</td>
      <td>Con: 0.023Exp: 0.024</td>
      <td>Wilcoxon rank-sum test</td>
      <td>W = 22,364</td>
      <td>119 (control)394 (exp.)</td>
      <td>NA</td>
      <td>0.45</td>
      <td>0.034</td>
    </tr>
    <tr>
      <td>iMM central adapting (laser OFF vs. ON)</td>
      <td>Figure 3—figure supplement 1C (top)</td>
      <td>OFF: 0.35ON: 0.33</td>
      <td>OFF: 0.35ON: 0.32</td>
      <td>OFF: 0.11ON: 0.15</td>
      <td>OFF: 0.026ON: 0.034</td>
      <td>OFF: 0.054ON: 0.072</td>
      <td>Wilcoxon signed-rank test</td>
      <td>V = 124</td>
      <td>18</td>
      <td>NA</td>
      <td>0.099</td>
      <td>0.40</td>
    </tr>
    <tr>
      <td>iPE central adapting (laser OFF vs. ON)</td>
      <td>Figure 3—figure supplement 1C (middle)</td>
      <td>OFF: 0.16ON: 0.19</td>
      <td>OFF: 0.10ON: 0.081</td>
      <td>OFF: 0.39ON: 0.40</td>
      <td>OFF: 0.091ON: 0.094</td>
      <td>OFF: 0.19ON: 0.20</td>
      <td>Paired t-test</td>
      <td>t = –1.1</td>
      <td>18</td>
      <td>17</td>
      <td>0.30</td>
      <td>0.25</td>
    </tr>
    <tr>
      <td>iRS central adapting (laser OFF vs. ON)</td>
      <td>Figure 3—figure supplement 1C (bottom)</td>
      <td>OFF: 0.19ON: 0.14</td>
      <td>OFF: 0.24ON: 0.14</td>
      <td>OFF: 0.38ON: 0.37</td>
      <td>OFF: 0.090ON: 0.087</td>
      <td>OFF: 0.19ON: 0.18</td>
      <td>Paired t-test</td>
      <td>t = 1.9</td>
      <td>18</td>
      <td>17</td>
      <td>0.077</td>
      <td>0.44</td>
    </tr>
    <tr>
      <td>iMM shell adapting (laser OFF vs. ON)</td>
      <td>Figure 3—figure supplement 1D (top)</td>
      <td>OFF: 0.38ON: 0.38</td>
      <td>OFF: 0.35ON: 0.38</td>
      <td>OFF: 0.19ON: 0.22</td>
      <td>OFF: 0.032ON: 0.037</td>
      <td>OFF: 0.065ON: 0.075</td>
      <td>Paired t-test</td>
      <td>t = –0.0013</td>
      <td>35</td>
      <td>34</td>
      <td>0.99</td>
      <td>0.00022</td>
    </tr>
    <tr>
      <td>iPE shell adapting (laser OFF vs. ON)</td>
      <td>Figure 3—figure supplement 1D (middle)</td>
      <td>OFF: 0.16ON: 0.14</td>
      <td>OFF: 0.12ON: 0.15</td>
      <td>OFF: 0.24ON: 0.26</td>
      <td>OFF: 0.041ON: 0.044</td>
      <td>OFF: 0.083ON: 0.090</td>
      <td>Paired t-test</td>
      <td>t = 0.58</td>
      <td>35</td>
      <td>34</td>
      <td>0.56</td>
      <td>0.099</td>
    </tr>
    <tr>
      <td>iRS shell adapting (laser OFF vs. ON)</td>
      <td>Figure 3—figure supplement 1D (bottom)</td>
      <td>OFF: 0.22ON: 0.24</td>
      <td>OFF: 0.24ON: 0.20</td>
      <td>OFF: 0.23ON: 0.22</td>
      <td>OFF: 0.040ON: 0.038</td>
      <td>OFF: 0.081ON: 0.077</td>
      <td>Paired t-test</td>
      <td>t = –0.78</td>
      <td>35</td>
      <td>34</td>
      <td>0.44</td>
      <td>0.13</td>
    </tr>
    <tr>
      <td>iMM central facilitating (laser OFF vs. ON)</td>
      <td>Figure 3—figure supplement 1E (top)</td>
      <td>OFF: –0.37ON: –0.33</td>
      <td>OFF: –0.36ON: –0.37</td>
      <td>OFF: 0.15ON: 0.18</td>
      <td>OFF: 0.077ON: 0.090</td>
      <td>OFF: 0.25ON: 0.29</td>
      <td>Paired t-test</td>
      <td>t = –1.1</td>
      <td>4</td>
      <td>3</td>
      <td>0.34</td>
      <td>0.57</td>
    </tr>
    <tr>
      <td>iPE central facilitating (laser OFF vs. ON)</td>
      <td>Figure 3—figure supplement 1E (middle)</td>
      <td>OFF: –0.043ON: 0.030</td>
      <td>OFF: –0.0047ON: 0.077</td>
      <td>OFF: 0.47ON: 0.45</td>
      <td>OFF: 0.24ON: 0.22</td>
      <td>OFF: 0.75ON: 0.71</td>
      <td>Paired t-test</td>
      <td>t = –0.93</td>
      <td>4</td>
      <td>3</td>
      <td>0.42</td>
      <td>0.47</td>
    </tr>
    <tr>
      <td>iRS central facilitating (laser OFF vs. ON)</td>
      <td>Figure 3—figure supplement 1E (bottom)</td>
      <td>OFF: –0.33ON: –0.36</td>
      <td>OFF: –0.49ON: –0.53</td>
      <td>OFF: 0.55ON: 0.60</td>
      <td>OFF: 0.27ON: 0.30</td>
      <td>OFF: 0.87ON: 0.95</td>
      <td>Paired t-test</td>
      <td>t = 0.49</td>
      <td>4</td>
      <td>3</td>
      <td>0.66</td>
      <td>0.24</td>
    </tr>
    <tr>
      <td>iMM shell facilitating (laser OFF vs. ON)</td>
      <td>Figure 3—figure supplement 1F (top)</td>
      <td>OFF: –0.38ON: –0.31</td>
      <td>OFF: –0.32ON: –0.30</td>
      <td>OFF: 0.22ON: 0.20</td>
      <td>OFF: 0.048ON: 0.043</td>
      <td>OFF: 0.10ON: 0.090</td>
      <td>Wilcoxon signed-rank test</td>
      <td>V = 63</td>
      <td>21</td>
      <td>NA</td>
      <td>0.070</td>
      <td>0.40</td>
    </tr>
    <tr>
      <td>iPE shell facilitating (laser OFF vs. ON)</td>
      <td>Figure 3—figure supplement 1F (middle)</td>
      <td>OFF: –0.090ON: –0.094</td>
      <td>OFF: –0.11ON: –0.081</td>
      <td>OFF: 0.18ON: 0.20</td>
      <td>OFF: 0.040ON: 0.044</td>
      <td>OFF: 0.083ON: 0.093</td>
      <td>Wilcoxon signed-rank test</td>
      <td>V = 109</td>
      <td>21</td>
      <td>NA</td>
      <td>0.84</td>
      <td>0.050</td>
    </tr>
    <tr>
      <td>iRS shell facilitating (laser OFF vs. ON)</td>
      <td>Figure 3—figure supplement 1F (bottom)</td>
      <td>OFF: –0.29ON: –0.21</td>
      <td>OFF: –0.28ON: –0.15</td>
      <td>OFF: 0.24ON: 0.21</td>
      <td>OFF: 0.053ON: 0.047</td>
      <td>OFF: 0.11ON: 0.097</td>
      <td>Paired t-test</td>
      <td>t = –1.8</td>
      <td>21</td>
      <td>20</td>
      <td>0.091</td>
      <td>0.39</td>
    </tr>
    <tr>
      <td>iMM central nonadapting (laser OFF vs. ON)</td>
      <td>Figure 3—figure supplement 1G (top)</td>
      <td>OFF: 0.021ON: 0.060</td>
      <td>OFF: 0.014ON: 0.050</td>
      <td>OFF: 0.24ON: 0.23</td>
      <td>OFF: 0.032ON: 0.031</td>
      <td>OFF: 0.064ON: 0.063</td>
      <td>Paired t-test</td>
      <td>t = –1.8</td>
      <td>55</td>
      <td>54</td>
      <td>0.075</td>
      <td>0.24</td>
    </tr>
    <tr>
      <td>iPE central nonadapting (laser OFF vs. ON)</td>
      <td>Figure 3—figure supplement 1G (middle)</td>
      <td>OFF: 0.12ON: 0.14</td>
      <td>OFF: 0.034ON: 0.092</td>
      <td>OFF: 0.34ON: 0.35</td>
      <td>OFF: 0.046ON: 0.047</td>
      <td>OFF: 0.092ON: 0.095</td>
      <td>Paired t-test</td>
      <td>t = –1.2</td>
      <td>55</td>
      <td>54</td>
      <td>0.23</td>
      <td>0.16</td>
    </tr>
    <tr>
      <td>iRS central nonadapting (laser OFF vs. ON)</td>
      <td>Figure 3—figure supplement 1G (bottom)</td>
      <td>OFF: –0.095ON: –0.083</td>
      <td>OFF: –0.064ON: –0.072</td>
      <td>OFF: 0.31ON: 0.29</td>
      <td>OFF: 0.042ON: 0.038</td>
      <td>OFF: 0.084ON: 0.077</td>
      <td>Paired t-test</td>
      <td>t = –0.57</td>
      <td>55</td>
      <td>54</td>
      <td>0.57</td>
      <td>0.077</td>
    </tr>
    <tr>
      <td>iMM shell nonadapting (laser OFF vs. ON)</td>
      <td>Figure 3—figure supplement 1H (top)</td>
      <td>OFF: 0.063ON: 0.051</td>
      <td>OFF: 0.040ON: 0.031</td>
      <td>OFF: 0.16ON: 0.22</td>
      <td>OFF: 0.021ON: 0.027</td>
      <td>OFF: 0.042ON: 0.054</td>
      <td>Wilcoxon signed-rank test</td>
      <td>V = 1133</td>
      <td>63</td>
      <td>NA</td>
      <td>0.39</td>
      <td>0.11</td>
    </tr>
    <tr>
      <td>iPE shell nonadapting (laser OFF vs. ON)</td>
      <td>Figure 3—figure supplement 1H (middle)</td>
      <td>OFF: 0.053ON: 0.027</td>
      <td>OFF: 0.0ON: 0.0</td>
      <td>OFF: 0.25ON: 0.26</td>
      <td>OFF: 0.031ON: 0.032</td>
      <td>OFF: 0.063ON: 0.065</td>
      <td>Paired t-test</td>
      <td>t = 0.88</td>
      <td>63</td>
      <td>62</td>
      <td>0.38</td>
      <td>0.11</td>
    </tr>
    <tr>
      <td>iRS shell nonadapting (laser OFF vs. ON)</td>
      <td>Figure 3—figure supplement 1H (bottom)</td>
      <td>OFF: 0.011ON: 0.024</td>
      <td>OFF: 0.028ON: 0.041</td>
      <td>OFF: 0.27ON: 0.28</td>
      <td>OFF: 0.034ON: 0.035</td>
      <td>OFF: 0.068ON: 0.071</td>
      <td>Paired t-test</td>
      <td>t = –0.43</td>
      <td>63</td>
      <td>62</td>
      <td>0.67</td>
      <td>0.054</td>
    </tr>
    <tr>
      <td>iRS &gt; 0 central nonadapting (laser OFF vs. ON)</td>
      <td>N/A</td>
      <td>OFF: 0.21ON: 0.18</td>
      <td>OFF: 0.20ON: 0.16</td>
      <td>OFF: 0.12ON: 0.16</td>
      <td>OFF: 0.026ON: 0.034</td>
      <td>OFF: 0.054ON: 0.070</td>
      <td>Paired t-test</td>
      <td>t = 1.5</td>
      <td>22</td>
      <td>21</td>
      <td>0.16</td>
      <td>0.31</td>
    </tr>
    <tr>
      <td>iRS &lt; 0 central nonadapting (laser OFF vs. ON)</td>
      <td>N/A</td>
      <td>OFF: –0.31ON: –0.26</td>
      <td>OFF: –0.27ON: –0.27</td>
      <td>OFF: 0.21ON: 0.21</td>
      <td>OFF: 0.036ON: 0.037</td>
      <td>OFF: 0.074ON: 0.075</td>
      <td>Paired t-test</td>
      <td>t = –1.7</td>
      <td>32</td>
      <td>31</td>
      <td>0.099</td>
      <td>0.30</td>
    </tr>
  </tbody>
</table>

_iRS: index of repetition suppression; iPE: index of prediction error; iMM: index of neuronal mismatch._

### Adapting and facilitating units respond similarly to the cascade and many standards controls

Though the cascade sequence is free of repetition effects between adjacent tone pairs, it does exhibit global repetition across the entire tone sequence. To assess whether global stimulus regularity affects the response to the cascade context, we used a shuffled version of the cascade sequence, known as the ‘many standards’ sequence, as an additional control stimulus (Figure 3—figure supplement 2A). The many standards sequence contains the same 10 tones as the cascade but presented in random order (Figure 3—figure supplement 2A). This reduces the potential for adaptation across adjacent frequency channels and also eliminates the global predictability of the stimulus, both of which could lead to suppression of responses to tones in the cascade context and potentially affect the calculations of iMM, iPE, and iRS. We compared the responses of adapting and facilitating units in both central and shell regions of IC to tones in the cascade versus the many standards context (Figure 3—figure supplement 2A). We found no significant differences in firing rates to the cascade versus the many standards contexts (Figure 3—figure supplement 2B and C, Table 1), suggesting that the global structure of the cascade sequence does not significantly affect how units in IC respond to this stimulus, as has been shown in other structures (Casado-Román et al., 2020; Parras et al., 2021).

### iMM distribution does not differ between single- and multiunit types

The analysis of changes in predictive coding metrics is performed on pooled single- and multiunit responses of IC units. To determine whether the expression of neuronal mismatch differs between these unit types, we plotted the iMM for laser OFF and ON conditions for each of the subgroups in the central and shell regions of the IC separated by single- (displayed in teal) and multiunits (Figure 3—figure supplement 3). We observed no differences in the distributions of these unit types in central or shell IC (Table 1; central OFF: p=0.88, Wilcoxon rank-sum test; central ON: p=0.93, Student’s t-test; shell OFF: p=0.19, Wilcoxon rank-sum test; shell ON: p=0.21, Wilcoxon rank-sum test). We therefore combined data from both single- and multiunits for the analyses of predictive coding metrics.

### Nonadapting units also display top-down repetition enhancement

The majority of units in both central and shell IC do not exhibit either adaptation or facilitation but respond similarly to tones when they are presented as a standard or deviant (Figure 4A). However, since both negative and positive metrics are included in the calculation of iMM, it is still possible that these units exhibit predictive processing that may not be reflected in the overall iMM value. We further characterized these nonadapting units (Figure 4B) and tested how they are affected by cortico-collicular inactivation. Nonadapting units in the central nucleus exhibited a significant increase in iMM during inactivation (Figure 4C, top; Table 1; p=2.7e-06, Wilcoxon signed-rank test), whereas those in the shell IC were unaffected (Figure 4D, top). The change in iMM for nonadapting units in the central nucleus was driven by a significant increase in iRS (Figure 4C, bottom middle; Table 1; p=0.0011, Wilcoxon signed-rank test). To determine whether this reflected a change in repetition suppression or enhancement, we further segregated central nonadapting units according to whether their baseline iRS values were negative or positive (Figure 4C, bottom). Only those units with negative baseline iRS values (i.e., those units showing repetition enhancement) were significantly affected by cortico-collicular inactivation (Figure 4C, bottom; Table 1; p=0.00012, Wilcoxon signed-rank test). In control experiments without ArchT, no significant changes were observed in nonadapting units (Figure 3—figure supplement 1G and H, Table 2). These results indicate that, similar to central facilitating units, central nonadapting units display repetition enhancement, and that input from the cortex is critical for expression of this phenomenon.

![Figure 4.](https://cdn.elifesciences.org/articles/73289/elife-73289-fig4-v2.jpg)

**Figure 4.:** (A) Distribution of adapting types (adapting, facilitating, and nonadapting) for units in central (left) and shell (right) regions of the inferior colliculus (IC). (B) Average peristimulus time histogram for nonadapting units in central (top) and shell (bottom) IC. (C) Index of neuronal mismatch (iMM) (top), index of prediction error (iPE) (middle), and index of repetition suppression (iRS) (bottom) for nonadapting units in central regions of IC. Dots represent recorded units. Bar plots represent means over the population of n = 155 units. Error bars are standard error of the mean. (D) iMM (top), iPE (middle), and iRS (bottom) for nonadapting units in shell regions of IC. Dots represent recorded units. Bar plots represent means over the population of n = 243 units. Error bars are standard error of the mean.

### Standard and deviant responses are bidirectionally modulated by cortico-collicular inactivation

The observed changes in repetition metrics with cortico-collicular inactivation could reflect an effect on either the standard or cascade context. Similarly, the shift in prediction metrics observed with inactivation could be due to altered responses to either the cascade or deviant contexts. We next determined whether the laser-induced changes in the iMM, iPE, and iRS for adapting units reflect changes in the firing rates to the standard, deviant, or cascade contexts. We found that adapting units in the central nucleus increased responses to the standard (Figure 5A, Table 1; p=0.0092, one-sample t-test) and decreased responses to the deviant (Figure 5A, Table 1; p=0.0054, one-sample t-test) during inactivation. These results explain the decrease in iMM for this population during the laser stimulus (Figure 3D, top): the firing rate to the cascade stimulus did not change during cortico-collicular inactivation, which means that the decrease in firing rate to the deviant alone underlies the decrease in prediction error observed for this population (Figure 3D, middle). Adapting units in the shell exhibited the same pattern of bidirectional changes to the standard (Figure 5B, Table 1; p=0.035, one-sample Wilcoxon test) and deviant (Figure 5B, Table 1; p=0.0057, one-sample Wilcoxon test), similarly accounting for their decrease in iMM and prediction error (Figure 3E), with no change in response to the cascade condition (Figure 5B). These data suggest that inactivation of the cortico-collicular pathway induces bidirectional changes in firing rates to the standard and deviant for adapting units in both central and shell regions of IC.

![Figure 5.](https://cdn.elifesciences.org/articles/73289/elife-73289-fig5-v2.jpg)

**Figure 5.:** (A) Responses to the standard (left), cascade (middle left), and deviant (middle right) for adapting units in central regions of the inferior colliculus (IC) under baseline and laser conditions. Change in firing rate between the laser and baseline condition for each stimulus (right). Dots represent recorded units. Bar plots represent means over the population of n = 52 units. Error bars are standard error of the mean. (B) Responses to the standard (left), cascade (middle left), and deviant (middle right) for adapting units in shell regions of IC under baseline and laser conditions. Change in firing rate between the laser and baseline condition for each stimulus (right). Dots represent recorded units. Bar plots represent means over the population of n = 113 units. Error bars are standard error of the mean. (C) Responses to the standard (left), cascade (middle left), and deviant (middle right) for facilitating units in central regions of IC under baseline and laser conditions. Change in firing rate between the laser and baseline condition for each stimulus (right). Dots represent recorded units. Bar plots represent means over the population of n = 14 units. Error bars are standard error of the mean. (D) Responses to the standard (left), cascade (middle left), and deviant (middle right) for facilitating units in shell regions of IC under baseline and laser conditions. Change in firing rate between the laser and baseline condition for each stimulus (right). Dots represent recorded units. Bar plots represent means over the population of n = 38 units. Error bars are standard error of the mean. (E) Responses to the standard (left), cascade (middle left), and deviant (middle right) for nonadapting units in central regions of IC under baseline and laser conditions. Change in firing rate between the laser and baseline condition for each stimulus (right). Dots represent recorded units. Bar plots represent means over the population of n = 155 units. Error bars are standard error of the mean. (F) Responses to the standard (left), cascade (middle left), and deviant (middle right) for nonadapting units in shell regions of IC under baseline and laser conditions. Change in firing rate between the laser and baseline condition for each stimulus (right). Dots represent recorded units. Bar plots represent means over the population of n = 243 units. Error bars are standard error of the mean.

We also investigated how responses to each stimulus context changed with cortico-collicular inactivation for facilitating units. For central facilitating units, only the firing rate to the standard context changed during inactivation (Figure 5C, Table 1; p=0.0013, one-sample t-test), explaining the observed change in repetition enhancement for this population (Figure 3G). For shell facilitating units, a decreased response to the standard (Figure 5D, Table 1; p=0.0042, one-sample t-test) and an increased response to the deviant (Figure 5D, Table 1; p=0.0013, one-sample t-test) were elicited on laser trials, accounting for changes in the iMM and the abolishment of negative prediction error (Figure 3H). These changes are directionally opposite to the observed firing rate changes observed for adapting units under inactivation, with a decrease to the standard context for both central and shell units and an increase to the deviant context for shell units.

For nonadapting units, a significant decrease in response to the standard context was observed in both central (Figure 5E, Table 1; p=1.4e-06, one-sample Wilcoxon test) and shell (Figure 5F, Table 1; p=0.035, one-sample Wilcoxon test) regions of IC. The decrease was only significant enough to produce an effect on the iMM in central regions (Figure 4C, top), leading to an increase in repetition suppression (Figure 4C, bottom).

For adapting and facilitating units, these data exhibit that IC responses to the standard and deviant contexts in the absence of cortical input are bidirectionally modulated, such that neurons respond more similarly to both contexts rather than firing differentially to each. For nonadapting units, the response to the standard context alone is diminished during cortico-collicular inactivation, causing these units to become more adapting. These changes suggest that under normal conditions AC provides information regarding sound context to neurons in IC.

### IC units have distinct combinations of iPE and iRS

To determine whether IC units exhibit particular combinations of repetition suppression/enhancement and prediction error/negative prediction error, we plotted the iPE values against the iRS values for each unit in the adapting, facilitating, and nonadapting groups. Both the adapting and nonadapting groups in the central IC contained units with significant values for both iPE and iRS, most often resulting from a combination of negative prediction error and repetition suppression (Figure 6A, maroon dots). In the shell IC, a greater variety of response combinations was observed. All three groups contained units with both significant negative prediction error and repetition suppression, as well as a separate population exhibiting significant prediction error and repetition enhancement (Figure 6B, maroon dots). Some shell adapting units also exhibited a combination of both repetition suppression and prediction error (Figure 6B, left). These results suggest that the units in IC exhibit distinct combinations of repetition suppression/enhancement and prediction error/negative prediction error.

![Figure 6.](https://cdn.elifesciences.org/articles/73289/elife-73289-fig6-v2.jpg)

**Figure 6.:** (A) Distribution of both iRS and iPE in adapting (left), facilitating (middle), and nonadapting (right) units in central IC. (B) Plots of distributions of both iRS and iPE in adapting (left), facilitating (middle), and nonadapting (right) units in shell IC. (C) Response to three subsequent standards prior to or following the deviant in facilitating units in central IC. Comparison between the last standard before and the first standard after the deviant demonstrates significant repetition enhancement. Bar plots represent means over the population of n = 14 units. Error bars are standard error of the mean. (D) Response to three subsequent standards prior to or following the deviant in facilitating units in shell IC. Comparison between the last standard before and the first standard after the deviant demonstrates significant repetition enhancement. Bar plots represent means over the population of n = 38 units. Error bars are standard error of the mean.

### Facilitating units exhibit true repetition enhancement

Facilitating units in both central and shell regions of IC exhibited repetition enhancement at baseline, as defined by the difference in firing rate to the last standard and the same tone embedded in the cascade sequence (Figure 3G and H). We sought to further characterize the response to the standard context to determine whether the repetition enhancement captured by the iRS indicates true repetition enhancement (an incremental increase in firing rate on subsequent presentations of the standard) or simply a net increase in firing rate to the standard versus cascade condition. We calculated the mean firing rate for each of the three standards before the deviant and each of the three standards after the deviant (Figure 6C and D). The progression of standards by position exhibited subsequent enhancements in firing rate that was plateaued by the second to last standard before the deviant for both central (Figure 6C) and shell facilitating units (Figure 6D). The firing rate to the last standard was significantly higher than the first in both regions (Figure 6C, Table 1; p=0.0017, Wilcoxon signed-rank test; Figure 6D, Table 1; p=9.3e-05, Wilcoxon signed-rank test). These data provide evidence that facilitating units in IC exhibit true repetition enhancement.

## Discussion

### Summary of findings

The results of this study indicate that AC is critically involved in regulating both repetition and prediction effects in the awake IC, providing evidence for the implementation of predictive coding in cortico-subcortical networks. Adapting and facilitating units were bidirectionally modulated by cortico-collicular inactivation, with adapting units becoming less adapting and facilitating units becoming less facilitating on laser trials (Figure 3). The decrease in adaptation for adapting units was driven by a decrease in prediction error for units in both central and shell regions of IC ( Figure 3D, Figure 5E, Figure 7, pink arrows). For facilitating and nonadapting units in the central nucleus, inactivation-driven changes were caused by a decrease in repetition enhancement (Figure 3G, Figure 7, gold dashed arrows). The decrease in facilitation in the shell IC, however, was caused by the abolishment of negative prediction error (Figure 3H, Figure 7, pink dashed arrows).

![Figure 7.](https://cdn.elifesciences.org/articles/73289/elife-73289-fig7-v2.jpg)

**Figure 7.:** Laser inactivation led to the abolishment of repetition enhancement in central facilitating units and the abolishment of negative prediction error in shell facilitating units. Prediction error decreased during inactivation for adapting units in both shell and central regions of the inferior colliculus (IC). Repetition suppression remained unaffected during cortical inactivation, suggesting that it may reflect fatigue of bottom-up sensory inputs.

In adapting units, these changes were modulated by an increased response to the standard and decreased response to the deviant, while the opposite pattern was true for facilitating units (Figure 5). Overall, these bidirectional changes indicate that, without input from AC, IC responds more similarly to tones in the standard and deviant contexts. These findings demonstrate that AC provides critical contextual cues about the statistics of the auditory environment to targets in IC under normal conditions. We further discuss these results in the context of a hierarchical predictive coding framework below.

### iMM in the awake versus anesthetized IC

Our results include the first investigation of how the repetition and prediction processes that underlie deviance detection in the awake IC compare to the anesthetized condition. Our data suggest that while iMM values are higher under anesthesia, they almost entirely reflect repetition suppression, with only a small contribution of prediction error (Figure 2). In the central IC, modest prediction error is present under anesthesia, but negative prediction error becomes dominant when the animal is awake. In the shell IC, the same units exhibit drastically different iPE and iRS values for the awake versus the anesthetized condition. Prediction error is substantially higher in the awake IC, and repetition enhancement, rather than repetition suppression, is observed (Figures 2F and 4G). These findings suggest that the iMM values in the awake and anesthetized brain reflect different underlying processes, and that anesthesia induces bidirectional changes in metrics of repetition and prediction.

### Facilitating units in IC

We also provide here the first analysis of facilitating units in IC. Previous studies that have investigated iMM have focused selectively on the positive side of the iMM distribution since these units display adaptation. However, facilitation seems to be enriched in the awake IC (Figures 2B and 4E) and reflects other potentially interesting parameters, such as repetition enhancement (represented as a higher response to the standard than the cascade sequence) (Figure 2G) and negative prediction error (represented as a higher response to the cascade than the deviant) (Figure 2C).

### Repetition enhancement and repetition suppression in IC

Because previous studies that have applied a predictive coding framework to decompose neuronal mismatch have focused exclusively on adapting neurons, the repetition enhancement found here in facilitating units has not been previously described (Parras et al., 2017). However, it is well-documented in fMRI literature that repetition enhancement is a common phenomenon in humans, existing either alongside or in place of repetition suppression (de Gardelle et al., 2013; Müller et al., 2013; Segaert et al., 2013). Interestingly, repetition enhancement has been proposed to reflect novel network formation and consolidation of novel sensory representations (Segaert et al., 2013). Once new representations have been formed, repetition suppression is hypothesized to take over, reflecting the minimization in prediction errors that occurs when new representations give rise to accurate predictions (Auksztulewicz and Friston, 2016; de Gardelle et al., 2013; Friston and Kiebel, 2009). Though the repetition enhancement described in human studies differs drastically on spatial and temporal scales from the phenomenon described here, we find that it similarly involves a sequential enhancement in the response to subsequent presentations of the standard (Figure 6C and D). Repetition enhancement has also been observed in the MGB in response to temporally degraded stimuli that are hypothesized to engage top-down resources to compensate for bottom-up acoustic information loss (Cai et al., 2016; Kommajosyula et al., 2019). Interestingly, this enhancement is reversed when cortico-thalamic pathways are blocked, further suggesting that repetition enhancement in the auditory system reflects a top-down phenomenon (Kommajosyula et al., 2021).

While repetition suppression can be understood from a predictive coding framework, it can also be viewed from the perspective of neuronal fatigue, whereby the incremental decrease in firing rate to a repeated standard tone is simply explained by synaptic depression (Escera and Malmierca, 2014; Taaseh et al., 2011). Interestingly, we did not find any effect on repetition suppression during cortico-collicular inactivation, suggesting that it may reflect fatigue of bottom-up sensory inputs rather than an active predictive process (Figures 3D and 5E, Figure 7, gold arrows). While these data do not provide definitive proof of either perspective, they do suggest that the processes that underlie repetition suppression in IC do not involve top-down cortical signals. This notion is supported by the fact that repetition suppression was much more prevalent when animals were under anesthesia, a state in which the auditory responsiveness in the cortex is compromised (Figure 2G; Brugge and Merzenich, 1973; Katsuki et al., 1959).

### Prediction error in IC

In both central and shell populations that exhibited prediction error at baseline, cortico-collicular inactivation led to a decrease, or complete abolishment, of prediction error (Figures 3D and 5E). According to models of hierarchical predictive coding, higher-order stations generate predictions that they broadcast to lower centers (Friston and Kiebel, 2009). These predictions are compared with representations of the actual sensory input, and if there is a mismatch, a prediction error is generated and forwarded up the hierarchy (Friston and Kiebel, 2009). Under this framework, the inactivation of top-down inputs would interfere with communication of predictions, leading to dysfunction in the prediction error response, as seen in our data. Another possibility is that prediction errors are directly backpropagated from AC to IC. While this contradicts canonical predictive coding models, evidence for prediction error has been found in deep layers of the cortex in which feedback neurons reside (Asilador and Llano, 2020; Rummell et al., 2016). Though the precise mechanism underlying the generation of prediction error in IC remains unclear, our data show that feedback from AC plays a critical role in this process.

### Negative prediction error in IC

In addition to units with prediction error, we found that units in IC that responded more strongly to the cascade than the deviant context (Figure 3G and H), consistent with previous reports (Parras et al., 2017). A stronger response to a tone in the cascade sequence compared to the context in which it is a deviant could simply reflect a relative lack of cross-frequency adaptation; the oddball stimulus consists of repeated tone presentations of two neighboring frequencies, making it more likely to generate cross-frequency effects than the cascade stimulus, which cycles through repetitions of 10 evenly spaced frequencies (Parras et al., 2017; Taaseh et al., 2011). Previous studies that have investigated the effective bandwidth for cross-frequency adaptation, however, have found that it occurs between channels with a frequency separation of a third of an octave or less (Taaseh et al., 2011). The stimuli used in this study had a half-octave frequency separation, indicating that cross-frequency effects should be minimized. Therefore, it is unlikely that the negative prediction error responses observed in this study simply reflect cross-frequency adaptation to the oddball stimulus.

A stronger response to a tone when it is embedded in a completely predictable sequence, such as the cascade sequence, than when it is a deviant could also signify that a neuron encodes predictions, rather than prediction errors. In hierarchical predictive coding, both predictions and prediction errors are generated at every level of the hierarchy, with prediction errors being forwarded to ascending sensory centers and predictions being backpropagated (Friston and Kiebel, 2009). In the shell IC, the region that receives the vast majority of descending cortical input, evidence for negative prediction error was abolished during cortico-collicular inactivation (Figure 3H), consistent with the notion that feedback from the cortex may carry predictions to IC (Bajo et al., 2007; Herbert et al., 1991; Saldaña et al., 1996; Stebbings et al., 2014). Interestingly, negative prediction error in the central nucleus remained unperturbed during inactivation of cortical feedback (Figure 3G). Given that only a small fraction of cortico-collicular fibers terminate in the central nucleus, it is likely that it receives predictions from another source (Bajo et al., 2007; Herbert et al., 1991; Saldaña et al., 1996; Stebbings et al., 2014). An intriguing potential candidate for this source of predictions could be the shell IC, given the extensive network of intracollicular connections in IC (Lesicko et al., 2020; Saldaña and Merchán, 1992; Saldaña and Merchán, 2005). Future studies will be required to determine whether the negative prediction error metric described here captures the type of top-down predictions described in canonical predictive coding models.

### Technical considerations

One limitation of this study is that laser inactivation achieved only partial and not complete inactivation of the cortico-collicular pathway. Given that light itself can have a modulatory or toxic effect on neurons, these types of optogenetic experiments require a careful titration between using enough power to substantially affect the population of interest without causing nonspecific light or heat-based perturbations (Tyssowski and Gray, 2019). Though other techniques, such as chemogenetic approaches or cooling, provide more complete inactivation, they do not allow for rapid and reversible inactivation (English and Roth, 2015). With our laser power parameters, we found a mean 60% reduction in firing in putative cortico-collicular neurons at baseline and a 45% reduction during presentation of pure tone stimuli (Figure 1—figure supplement 1D). This reduction produced clear effects on repetition and prediction processing in IC, in several cases with the severe reduction or complete abolishment of certain metrics of deviance detection, such as prediction error and repetition enhancement in the central nucleus and negative prediction error in the shell IC (Figure 3). The interpretation of these results should bear in mind that they reflect only partial and not complete inactivation.

The analyses in this study were performed on pooled single- and multiunit data. Although we observed no differences in the iMM distribution between single- and multiunits (Figure 3—figure supplement 3), the results of this study should be interpreted with this limitation in mind, namely, photosuppression-induced changes in these units may not reflect changes in single neurons.

Whereas this study focuses on changes specific to the cortico-collicular pathway, it should be noted that cortico-collicular neurons are known to branch to additional subcortical targets besides the IC, including the MGB, caudal regions of the dorsal striatum, and the lateral amygdala (Asokan et al., 2018). The fact that our photo-suppression experiments produce short-latency effects in the IC (Figure 3C and F) indicates that the observed changes are likely due to direct, monosynaptic AC to IC pathways, and that multisynaptic effects from other collateral sites are unlikely. Nevertheless, the potential contribution from these additional downstream targets cannot be definitely ruled out and should be factored into the interpretation of the results.

### Conclusions

Our findings indicate that deviance detection and predictive coding in IC involve additional complexity than has been previously described. We provide here the first description of facilitating units in IC, as well as evidence for the existence of repetition enhancement and negative prediction error in these units. We show that AC regulates these metrics and is also involved in the generation of prediction error in IC. Repetition suppression is unaffected by inactivation of cortical input to IC, providing evidence that this process may reflect bottom-up fatigue rather than top-down predictive processing. These results demonstrate the role of AC in providing contextual cues about the auditory stream to targets in IC.

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
      <td>Strain, strain background (Mus musculus)</td>
      <td>Cdh23 mice</td>
      <td>Jackson Laboratories</td>
      <td>Cdh23tm2.1Kjn/J;RRID:IMSR_JAX:018399</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>AAV9-CAG-FLEX-ArchT-tdTomato</td>
      <td>UNC Vector Core</td>
      <td>Addgene_28305</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>RetroAAV2 hSyn Cre-GFP</td>
      <td>In-house</td>
      <td></td>
      <td>Vector generated and maintained in the di Biasi lab</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Kilosort2</td>
      <td>Marius Pachitariu</td>
      <td>https://github.com/MouseLand/Kilosort; RRID:SCR_016422</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MATLAB</td>
      <td>MathWorks</td>
      <td>https://www.mathworks.com/; RRID:SCR_001622</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ImageJ</td>
      <td>NIH</td>
      <td>RRID:SCR_003070</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Animals

We performed experiments in six adult Cdh23 mice (Cdh23tm2.1Kjn/J, RRID:IMSR_JAX:018399; four males and two females, age 3–8 months). This mouse line has a targeted point reversion in the Cdh23 gene that protects against the age-related hearing loss common to C57BL/6 strains (Johnson et al., 2017). Animals were housed on a reversed 12 hr light–dark cycle with water and food available ad libitum. All procedures were approved by the University of Pennsylvania IACUC (protocol number 803266) and the AALAC Guide on Animal Research. We made every attempt to minimize the number of animals used and reduce pain or discomfort.

### Virus injection

Mice were continuously anesthetized with isoflurane and mounted in a stereotaxic frame. Buprenex (0.1 mg/kg), meloxicam (5 mg/kg), and bupivicane (2 mg/kg) were injected subcutaneously for preoperative analgesia. We performed small craniotomies bilaterally over AC (−2.6 mm caudal to bregma, ±4.3 mm lateral, +1 mm ventral) and IC (−4.96 mm caudal to bregma, ±0.5 mm lateral, +0.5 mm ventral and −4.96 mm caudal to bregma, ±1.25 mm lateral, +1.0 mm ventral). A glass syringe (30–50 μm diameter) connected to a pump (Pump 11 Elite, Harvard Apparatus) was used to inject modified viral vectors (AAV9-CAG-FLEX-ArchT-tdTomato or AAV9-CAG-FLEX-tdTomato; 750 nL/site; UNC Vector Core) into AC and a retroAAV construct (retro AAV-hSyn-Cre-GFP; 250 nL/site) into IC (Figures 1A and 2A, Figure 3—figure supplement 1A). Large viral injections were performed to broadly target cortico-collicular neurons throughout all regions of the AC. We implanted fiber-optic cannulas (Thorlabs, Ø200 μm Core, 0.22 NA) bilaterally over AC injection sites (0.4 mm ventral to brain surface) and secured them in place with dental cement (C and B Metabond) and acrylic (Lang Dental). IC injection sites were covered with a removable silicone plug (Kwik-Sil). A custom-built headplate was secured to the skull at the midline and a ground-pin was lowered into a small craniotomy over bregma. We injected an antibiotic (5 mg/kg Baytril) subcutaneously for 4 days postoperatively. Virus injection sites were confirmed postmortem for all animals included in the study.

### Extracellular recordings

We performed recordings a minimum of 21 days after virus injection surgeries to allow adequate travel time for the viral constructs (Figure 1A). Recordings were carried out inside a double-walled acoustic isolation booth (Industrial Acoustics) or a custom-built table-mounted acoustic isolation booth. For IC recordings, mice were briefly anesthetized to remove the silicone plug over IC virus injection sites. Following recovery from anesthesia, the headplate was clamped within a custom base to provide head-fixation. We lowered a 32-channel silicon probe (Neuronexus) vertically into IC during presentation of broadband noise clicks and monitored sound responses online to confirm localization within IC (Figure 1A). In a subset of animals (seven recording sites in two mice), the probe was first coated in a lipophilic dye (DiD or DiA; Invitrogen) to aid in post hoc reconstruction of recording sites. In each animal, two recordings were performed per IC (four total recording sessions bilaterally). We attempted to target both shell and central IC regions in each animal, and our post hoc analysis of recording sites (see details in ‘Analysis’ section) revealed that all but one animal was recorded from in both regions. Recordings that did not show significant sound responsiveness were removed from the analysis. Following completion of all IC recording sessions, we recorded the activity of neurons in AC using the same procedure (Figure 1—figure supplement 1B). We performed a square craniotomy (2 mm × 2 mm) over AC and oriented the probe vertically to the cortical surface (35° angle of the stereotaxic arm). Electrophysiological data were filtered between 600 and 6000 Hz to isolate spike responses and then digitized at 32 kHz and stored for offline analysis (Neuralynx). For a subset of recordings, the experimental procedures were repeated while recording from the same units after the animal had been anesthetized with isoflurane (Figure 2A). We performed spike sorting using Kilosort2 software (https://github.com/MouseLand/Kilosort; RRID:SCR_016422, version 2). Both single and multiunits were included for all analyses (experimental IC: 50 single units, 354 multiunits; control IC: 17 single units; 111 multiunits; anesthetized: 10 single units, 129 multiunits; AC: 95 single units, 300 multiunits; putative cortico-collicular: 9 single units; 11 multiunits).

### Laser inactivation

We inactivated cortico-collicular neurons using a 532 nm DPSS laser (GL532T3-300, Slocs lasers, 3 mW power at cannula tip or OptoEngine, MGL-III-532, 15 mW power at cannula tip) connected via optical fibers to the implanted cannulas (Figures 1A, 2C and D). Data collected using either laser was pooled together as no significant differences were observed in the strength of inactivation in AC during silence (p=0.054, Wilcoxon rank-sum test) or the presentation of pure tone stimuli (p=0.072, Wilcoxon rank-sum test) between the two lasers. Square laser pulses were timed to coincide with tone onset and lasted for 100 ms. Evidence of inactivation in putative cortico-collicular units (infragranular AC units with a minimum 30% reduction in both baseline and sound-evoked neuronal activity) was confirmed for all animals included in the study.

### Stimuli

We generated an initial frequency response function from a sequence of 50 pure tones, 1–70 kHz, repeated 20 times at 70 dB SPL in pseudo-random order. This response function was generated online to select suitable frequencies for the oddball stimuli, that is, frequencies that would fall into the average response area for units in a given recording. Each tone was 50 ms duration (1 ms cosine squared ramps) with an inter-stimulus interval of 200 ms and presentation rate of 4 Hz. A similar tuning curve stimulus, with eight amplitude levels (35–70 dB, 5 dB increments) and five repetitions, was used to further characterize the tuning properties of each unit (Figure 1—figure supplement 2E, F).

Oddball tone pairs were chosen to fit within the average response area for units from a given recording. Given the prevalence of inhibited regions in the tuning curves, and the fact that this often led to differences in the response profile of the unit to each frequency in the oddball tone pair, the responses to each frequency were analyzed separately (Figure 1—figure supplement 2G). Oddball stimuli consisted of a frozen sequence of two pure tones (with the same tone parameters as those used in the initial frequency response functions) with a 90:10 standard-to-deviant ratio and half-octave frequency separation. The number of standards interleaved between two deviants was counterbalanced and varied between 3 and 17 standards. The stimuli were divided into blocks (with the end of a block defined by the presentation of a deviant), and tone type and laser pairings were alternated on subsequent blocks. For example, on the first block the laser stimulus was paired with the deviant, on the second block it was paired with the last standard, and the corresponding tones in the third block served as baseline controls, with no laser stimulus. The number of preceding standards in the blocks was balanced for all three laser conditions (deviant, last standard, and baseline). Each block type (laser + standard, laser + deviant, no laser) was presented 45 times, and the total number of tones in each sequence was 1250. Two oddball sequences were created, both with the same frozen pattern, but with the frequencies of the standard and the deviant switched.

Cascade sequences consisted of either an ascending or descending set of 10 evenly log-spaced (half-octave separation) pure tones (same tone parameters as described above) (Figure 1C). The two tones used in the oddball sequences were always included as adjacent tones in the cascade sequences, though their position within the cascade was varied. To generate the many standards control sequence, we shuffled the cascade sequences using an algorithm that does not allow for repetition of tones of the same frequency on subsequent presentations.

### Analysis

To distinguish between shell and central IC recording locations, we plotted the best frequency for each unit from a given recording against its depth and fit the data with a robust linear regression model (Figure 1—figure supplement 2B). Additionally, we computed the mean sparseness for all units from a given recording site to quantify the sharpness of tuning. The R2 metric from the linear fit and the mean sparseness from each recording were used to perform k-means clustering with two groups. Each recording was assigned to a location (either central or shell) according to the k-means output, with central sites typically having high sparseness and high R2 values and shell sites having low sparseness and low R2 metrics (Figure 1—figure supplement 2C).

Sound response profiles were categorized quantitatively from analysis of the combined responses to the standard and deviant tones using MATLAB’s ‘findpeaks’ function with a minimum peak height set to the mean of the baseline period (50 ms before tone onset) ± 3 SDs. Units that did not display maxima or minima during the tone duration period (0–50 ms) or in the 50 ms after (the ‘offset window’) were labeled as sound unresponsive and were removed from the analysis. Units that showed only a single minimum (‘inhibited’ units) or only a response in the offset window were similarly removed from the analysis. Units that showed at least one maxima during the tone duration period were included in the analysis and further categorized as either onset (single maxima in the first 10 ms after tone onset), sustained (single maximum after the first 10 ms after tone onset), E-I or I-E (units that displayed both a maximum and minimum during the tone duration period), biphasic (units that displayed two maxima during the tone duration period), or mixed (units with greater than two maxima and/or minima during the tone response period). It was common for units to display a response both during the tone duration window and the offset window, and in these cases a combined response profile was assigned (e.g., onset/offset, sustained/inhibited offset). Units with only inhibited or offset responses were removed from the dataset.

Significant adaptation or facilitation for each unit was assessed with a Wilcoxon rank-sum test between the trial-by-trial firing rates to the standard and deviant on the 45 baseline trials. The iMM, identical to the traditional SSA index, was further deconstructed into an iPE and an iRS such that iMM = iPE + iRS. The raw firing rates to the standard, cascade, and deviant conditions were normalized by dividing by the Euclidean norm, N = $\sqrt{FR_{Dev}^{2}+ FR_{Casc}^{2}+ FR_{Stan}^{2}}$ . The iPE was calculated as the difference in normalized firing rate to the deviant and cascade conditions (iPE = $\frac{FR_{Dev}}{N}$ - $\frac{FR_{Casc}}{N}$), while the iRS was calculated as the difference in normalized firing rate to the cascade and standard conditions (iRS = $\frac{FR_{Casc}}{N}$ - $\frac{FR_{Stan}}{N}$). Predictive coding metrics for the laser condition were calculated similarly, but using trials from laser + standard, laser + cascade, and laser + deviant pairings.

### Statistical analysis

Shapiro–Wilk tests were used to assess normality. For normally distributed data, Student’s t-tests were performed. When the assumption of normality was violated, Wilcoxon rank-sum tests were used for nonpaired data and Wilcoxon signed-rank tests were used for paired data. Cohen’s d was calculated as a measure of effect size for t-tests. For Wilcoxon tests, the effect size r was calculated as the z statistic divided by the square root of the sample size.
