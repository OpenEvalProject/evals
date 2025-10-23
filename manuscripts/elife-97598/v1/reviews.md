# Peer review - Round 1

Editors:
- Leopoldo Petreanu, Champalimaud Center for the Unknown Portugal

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.97598.4.sa0](https://doi.org/10.7554/eLife.97598.4.sa0)

The paper reports the important discovery that the mouse dorsal inferior colliculus, an auditory midbrain area, encodes sound location. The evidence supporting the claims is solid, being supported by both optical and electrophysiological recordings. The observations described should be of interest to auditory researchers studying the neural mechanisms of sound localization and the role of noise correlations in population coding.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97598.4.sa1](https://doi.org/10.7554/eLife.97598.4.sa1)

Summary:

In this study, the authors address whether the dorsal nucleus of the inferior colliculus (DCIC) in mice encodes sound source location within the front horizontal plane (i.e., azimuth). They do this using volumetric two-photon Ca2+ imaging and high-density silicon probes (Neuropixels) to collect single-unit data. Such recordings are beneficial because they allow large populations of simultaneous neural data to be collected. Their main results and the claims about those results are the following:

(1) DCIC single-unit responses have high trial-to-trial variability (i.e., neural noise);

(2) approximately 32% to 40% of DCIC single units have responses that are sensitive to sound source azimuth;

(3) single-trial population responses (i.e., the joint response across all sampled single units in an animal) encode sound source azimuth "effectively" (as stated in the title) in that localization decoding error matches average mouse discrimination thresholds;

(4) DCIC can encode sound source azimuth in a similar format to that in the central nucleus of the inferior colliculus (as stated in the Abstract);

(5) evidence of noise correlation between pairs of neurons exists;

and (6) noise correlations between responses of neurons help reduce population decoding error.

While simultaneous recordings are not necessary to demonstrate results #1, #2, and #4, they are necessary to demonstrate results #3, #5, and #6.

Strengths:

- Important research question to all researchers interested in sensory coding in the nervous system.

- State-of-the-art data collection: volumetric two-photon Ca2+ imaging and extracellular recording using high-density probes. Large neuronal data sets.

- Confirmation of imaging results (lower temporal resolution) with more traditional microelectrode results (higher temporal resolution).

- Clear and appropriate explanation of surgical and electrophysiological methods. I cannot comment on the appropriateness of the imaging methods.

Strength of evidence for the claims of the study:

(1) DCIC single-unit responses have high trial-to-trial variability -

The authors' data clearly shows this.

(2) Approximately 32% to 40% of DCIC single units have responses that are sensitive to sound source azimuth -

The sensitivity of each neuron's response to sound source azimuth was tested with a Kruskal-Wallis test, which is appropriate since response distributions were not normal. Using this statistical test, only 8% of neurons (median for imaging data) were found to be sensitive to azimuth, and the authors noted this was not significantly different than the false positive rate. The Kruskal-Wallis test was not reported for electrophysiological data. The authors suggested that low numbers of azimuth-sensitive units resulting from the statistical analysis may be due to the combination of high neural noise and a relatively low number of trials, which would reduce the statistical power of the test. This is likely true and highlights a weakness in the experimental design (i.e., a relatively small number of trials). The authors went on to perform a second test of azimuth sensitivity-a chi-squared test-and found 32% (imaging) and 40% (e-phys) of single units to have statistically significant sensitivity. However, the use of a chi-squared test is questionable because it is meant to be used between two categorical variables, and neural response had to be binned before applying the test.

(3) Single-trial population responses encode sound source azimuth "effectively" in that localization decoding error matches average mouse discrimination thresholds -

If only one neuron in a population had responses that were sensitive to azimuth, we would expect that decoding azimuth from observation of that one neuron's response would perform better than chance. By observing the responses of more than one neuron (if more than one were sensitive to azimuth), we would expect performance to increase. The authors found that decoding from the whole population response was no better than chance. They argue (reasonably) that this is because of overfitting of the decoder model-too few trials were used to fit too many parameters-and provide evidence from decoding combined with principal components analysis which suggests that overfitting is occurring. What is troubling is the performance of the decoder when using only a handful of "top-ranked" neurons (in terms of azimuth sensitivity) (Fig. 4F and G). Decoder performance seems to increase when going from one to two neurons, then decreases when going from two to three neurons, and doesn't get much better for more neurons than for one neuron alone. It seems likely there is more information about azimuth in the population response, but decoder performance is not able to capture it because spike count distributions in the decoder model are not being accurately estimated due to too few stimulus trials (14, on average). In other words, it seems likely that decoder performance is underestimating the ability of the DCIC population to encode sound source azimuth.

To get a sense of how effective a neural population is at coding a particular stimulus parameter, it is useful to compare population decoder performance to psychophysical performance. Unfortunately, mouse behavioral localization data do not exist. Instead, the authors compare decoder error to mouse left-right discrimination thresholds published previously by a different lab. However, this comparison is inappropriate because the decoder and the mice were performing different perceptual tasks. The decoder is classifying sound sources to 1 of 13 locations from left to right, whereas the mice were discriminating between left or right sources centered around zero degrees. The errors in these two tasks represent different things. The two data sets may potentially be more accurately compared by extracting information from the confusion matrices of population decoder performance. For example, when the stimulus was at -30 deg, how often did the decoder classify the stimulus to a lefthand azimuth? Likewise, when the stimulus was +30 deg, how often did the decoder classify the stimulus to a righthand azimuth?

(4) DCIC can encode sound source azimuth in a similar format to that in the central nucleus of the inferior colliculus -

It is unclear what exactly the authors mean by this statement in the Abstract. There are major differences in the encoding of azimuth between the two neighboring brain areas: a large majority of neurons in the CNIC are sensitive to azimuth (and strongly so), whereas the present study shows a minority of azimuth-sensitive neurons in the DCIC. Furthermore, CNIC neurons fire reliably to sound stimuli (low neural noise), whereas the present study shows that DCIC neurons fire more erratically (high neural noise).

(5) Evidence of noise correlation between pairs of neurons exists -

The authors' data and analyses seem appropriate and sufficient to justify this claim.

(6) Noise correlations between responses of neurons help reduce population decoding error -

The authors show convincing analysis that performance of their decoder increased when simultaneously measured responses were tested (which include noise correlation) than when scrambled-trial responses were tested (eliminating noise correlation). This makes it seem likely that noise correlation in the responses improved decoder performance. The authors mention that the naïve Bayesian classifier was used as their decoder for computational efficiency, presumably because it assumes no noise correlation and, therefore, assumes responses of individual neurons are independent of each other across trials to the same stimulus. The use of a decoder that assumes independence seems key here in testing the hypothesis that noise correlation contains information about sound source azimuth. The logic of using this decoder could be more clearly spelled out to the reader. For example, if the null hypothesis is that noise correlations do not carry azimuth information, then a decoder that assumes independence should perform the same whether population responses are simultaneous or scrambled. The authors' analysis showing a difference in performance between these two cases provides evidence against this null hypothesis.

Minor weakness:

- Most studies of neural encoding of sound source azimuth are done in a noise-free environment, but the experimental setup in the present study had substantial background noise. This complicates comparison of the azimuth tuning results in this study to those of other studies. One is left wondering if azimuth sensitivity would have been greater in the absence of background noise, particularly for the imaging data where the signal was only about 12 dB above the noise.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97598.4.sa2](https://doi.org/10.7554/eLife.97598.4.sa2)

In the present study, Boffi et al. investigate the manner in which the dorsal cortex of the of the inferior colliculus (DCIC), an auditory midbrain area, encodes sound location azimuth in awake, passively listening mice. By employing volumetric calcium imaging (scanned temporal focusing or s-TeFo), complemented with high-density electrode electrophysiological recordings (neuropixels probes), they show that sound-evoked responses are exquisitely noisy, with only a small portion of neurons (units) exhibiting spatial sensitivity. Nevertheless, a naïve Bayesian classifier was able to predict the presented azimuth based on the responses from small populations of these spatially sensitive units. A portion of the spatial information was provided by correlated trial-to-trial response variability between individual units (noise correlations). The study presents a novel characterization of spatial auditory coding in a non-canonical structure, representing a noteworthy contribution specifically to the auditory field and generally to systems neuroscience, due to its implementation of state-of-the-art techniques in an experimentally challenging brain region. However, nuances in the calcium imaging dataset and the naïve Bayesian classifier warrant caution when interpreting some of the results.

Strengths:

The primary strength of the study lies in its methodological achievements, which allowed the authors to collect a comprehensive and novel dataset. While the DCIC is a dorsal structure, it extends up to a millimetre in depth, making it optically challenging to access in its entirety. It is also more highly myelinated and vascularised compared to e.g., the cerebral cortex, compounding the problem. The authors successfully overcame these challenges and present an impressive volumetric calcium imaging dataset. Furthermore, they corroborated this dataset with electrophysiological recordings, which produced overlapping results. This methodological combination ameliorates the natural concerns that arise from inferring neuronal activity from calcium signals alone, which are in essence an indirect measurement thereof.

Another strength of the study is its interdisciplinary relevance. For the auditory field, it represents a significant contribution to the question of how auditory space is represented in the mammalian brain. "Space" per se is not mapped onto the basilar membrane of the cochlea and must be computed entirely within the brain. For azimuth, this requires the comparison between miniscule differences between the timing and intensity of sounds arriving at each ear. It is now generally thought that azimuth is initially encoded in two, opposing hemispheric channels, but the extent to which this initial arrangement is maintained throughout the auditory system remains an open question. The authors observe only a slight contralateral bias in their data, suggesting that sound source azimuth in the DCIC is encoded in a more nuanced manner compared to earlier processing stages of the auditory hindbrain. This is interesting because it is also known to be an auditory structure to receive more descending inputs from the cortex.

Systems neuroscience continues to strive for the perfection of imaging novel, less accessible brain regions. Volumetric calcium imaging is a promising emerging technique, allowing the simultaneous measurement of large populations of neurons in three dimensions. But this necessitates corroboration with other methods, such as electrophysiological recordings, which the authors achieve. The dataset moreover highlights the distinctive characteristics of neuronal auditory representations in the brain. Its signals can be exceptionally sparse and noisy, which provide an additional layer of complexity in the processing and analysis of such datasets. This will undoubtedly be useful for future studies of other less accessible structures with sparse responsiveness.

Weaknesses:

Although the primary finding that small populations of neurons carry enough spatial information for a naïve Bayesian classifier to reasonably decode the presented stimulus is not called into question, certain idiosyncrasies, in particular the calcium imaging dataset and model, complicate specific interpretations of the model output, and the readership is urged to interpret these aspects of the study's conclusions with caution.

I remain in favour of volumetric calcium imaging as a suitable technique for the study, but the presently constrained spatial resolution is insufficient to unequivocally identify regions of interest as cell bodies (and are instead referred to as "units" akin to those of electrophysiological recordings). It remains possible that the imaging set is inadvertently influenced by non-somatic structures (including neuropil), which could report neuronal activity differently than cell bodies. Due to the lack of a comprehensive ground-truth comparison in this regard (which to my knowledge is impossible to achieve with current technology), it is difficult to imagine how many informative such units might have been missed because their signals were influenced by spurious, non-somatic signals, which could have subsequently misled the models. The authors reference the original Nature Methods article (Prevedel et al., 2016) throughout the manuscript, presumably in order to avoid having to repeat previously published experimental metrics. But the DCIC is neither the cortex nor hippocampus (for which the method was originally developed) and may not have the same light scattering properties (not to mention neuronal noise levels). Although the corroborative electrophysiology data largely alleviates these concerns for this particular study, the readership should be cognisant of such caveats, in particular those who are interested in implementing the technique for their own research.

A related technical limitation of the calcium imaging dataset is the relatively low number of trials (14) given the inherently high level of noise (both neuronal and imaging). Volumetric calcium imaging, while offering a uniquely expansive field of view, requires relatively high average excitation laser power (in this case nearly 200 mW), a level of exposure the authors may have wanted to minimise by maintaining a low number of repetitions, but I yield to them to explain. Calcium imaging is also inherently slow, requiring relatively long inter-stimulus intervals (in this case 5 s). This unfortunately renders any model designed to predict a stimulus (in this case sound azimuth) from particularly noisy population neuronal data like these as highly prone to overfitting, to which the authors correctly admit after a model trained on the entire raw dataset failed to perform significantly above chance level. This prompted them to feed the model only with data from neurons with the highest spatial sensitivity. This ultimately produced reasonable performance (and was implemented throughout the rest of the study), but it remains possible that if the model was fed with more repetitions of imaging data, its performance would have been more stable across the number of units used to train it. (All models trained with imaging data eventually failed to converge.) However, I also see these limitations as an opportunity to improve the technology further, which I reiterate will be generally important for volume imaging of other sparse or noisy calcium signals in the brain.

Transitioning to the naïve Bayesian classifier itself, I first openly ask the authors to justify their choice of this specific model. There are countless types of classifiers for these data, each with their own pros and cons. Did they actually try other models (such as support vector machines), which ultimately failed? If so, these negative results (even if mentioned en passant) would be extremely valuable to the community, in my view. I ask this specifically because different methods assume correspondingly different statistical properties of the input data, and to my knowledge naïve Bayesian classifiers assume that predictors (neuronal responses) are assumed to be independent within a class (azimuth). As the authors show that noise correlations are informative in predicting azimuth, I wonder why they chose a model that doesn't take advantage of these statistical regularities. It could be because of technical considerations (they mention computing efficiency), but I am left generally uncertain about the specific logic that was used to guide the authors through their analytical journey.

In a revised version of the manuscript, the authors indeed justify their choice of the naïve Bayesian classifier as a conservative approach (not taking into account noise correlations), which could only improve with other models (that do). They even tested various other commonly used models, such as support vector machines and k-nearest neighbours, to name a few, but do not report these efforts in the main manuscript. Interestingly, these models, which I supposed would perform better in fact did not overall - a finding that I have no way of interpreting but nevertheless find interesting.

That aside, there remain other peculiarities in model performance that warrant further investigation. For example, what spurious features (or lack of informative features) in these additional units prevented the models of imaging data from converging? In an orthogonal question, did the most spatially sensitive units share any detectable tuning features? A different model trained with electrophysiology data in contrast did not collapse in the range of top-ranked units plotted. Did this model collapse at some point after adding enough units, and how well did that correlate with the model for the imaging data? How well did the form (and diversity) of the spatial tuning functions as recorded with electrophysiology resemble their calcium imaging counterparts? These fundamental questions could be addressed with more basic, but transparent analyses of the data (e.g., the diversity of spatial tuning functions of their recorded units across the population). Even if the model extracts features that are not obvious to the human eye in traditional visualisations, I would still find this interesting.

Although these questions were not specifically addressed in the revised version of the manuscript, I also admit that I did not indent do assert that these should necessarily fall within the scope of the present study. I rather posed them as hypothetical directions one could pursue in future studies. Finally, further concerns I had with statements regarding the physiological meaning of the findings have been ameliorated by nicely modified statements, thus bringing transparency to the readership, which I appreciate.

In summary, the present study represents a significant body of work that contributes substantially to the field of spatial auditory coding and systems neuroscience. However, limitations of the imaging dataset and model as applied in the study muddles concrete conclusions about how the DCIC precisely encodes sound source azimuth and even more so to sound localisation in a behaving animal. Nevertheless, it presents a novel and unique dataset, which, regardless of secondary interpretation, corroborates the general notion that auditory space is encoded in an extraordinarily complex manner in the mammalian brain.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97598.4.sa3](https://doi.org/10.7554/eLife.97598.4.sa3)

Summary:

Boffi and colleagues sought to quantify the single-trial, azimuthal information in the dorsal cortex of the inferior colliculus (DCIC), a relatively understudied subnucleus of the auditory midbrain. They accomplished this by using two complementary recording methods while mice passively listened to sounds at different locations: calcium imaging that recorded large neuronal populations but with poor temporal precision and multi-contact electrode arrays that recorded smaller neuronal populations with exact temporal precision. DCIC neurons respond variably, with inconsistent activity to sound onset and complex azimuthal tuning. Some of this variably was explained by ongoing head movements. The authors used a naïve Bayes decoder to probe the azimuthal information contained in the response of DCIC neurons on single trials. The decoder failed to classify sound location better than chance when using the raw population responses but performed significantly better than chance when using the top principal components of the population. Units with the most azimuthal tuning were distributed throughout the DCIC, possessed contralateral bias, and positively correlated responses. Interestingly, inter-trial shuffling decreased decoding performance, indicating that noise correlations contributed to decoder performance. Overall, Boffi and colleagues, quantified the azimuthal information available in the DCIC while mice passively listened to sounds, a first step in evaluating if and how the DCIC could contribute to sound localization.

Strengths:

The authors should be commended for collection of this dataset. When done in isolation (which is typical), calcium imaging and linear array recordings have intrinsic weaknesses. However, those weaknesses are alleviated when done in conjunction - especially when the data is consistent. This data set is extremely rich and will be of use for those interested in auditory midbrain responses to variable sound locations, correlations with head movements, and neural coding.

The DCIC neural responses are complex with variable responses to sound onset, complex azimuthal tuning and large inter-sound interval responses. Nonetheless, the authors do a decent job in wrangling these complex responses: finding non-canonical ways of determining dependence on azimuth and using interpretable decoders to extract information from the population.

Weaknesses:

The decoding results are a bit strange, likely because the population response is quite noisy on any given trial. Raw population responses failed to provide sufficient information concerning azimuth for significant decoding. Importantly, the decoder performed better than chance when certain principal components or top ranked units contributed but did not saturate with the addition of components or top ranked units. So, although there is azimuthal information in the recorded DCIC populations - azimuthal information appears somewhat difficult to extract.

Although necessary given the challenges associated with sampling many conditions with technically difficult recording methods, the limited number of stimulus repeats precludes interpretable characterization of the heterogeneity across the population. Nevertheless, the dataset is public so those interested can explore the diversity of the responses.

The observations from Boffi and colleagues raises the question: what drives neurons in the DCIC to respond? Sound azimuth appears to be a small aspect of the DCIC response. For example, the first 20 principal components which explain roughly 80% of the response variance are insufficient input for the decoder to predict sound azimuth above chance. Furthermore, snout and ear movements correlate with the population response in the DCIC (the ear movements are particularly peculiar given they seem to predict sound presentation). Other movements may be of particular interest to control for (e.g. eye movements are known to interact with IC responses in the primate). These observations, along with reported variance to sound onsets and inter-sound intervals, question the impact of azimuthal information emerging from DCIC responses. This is certainly out of scope for any one singular study to answer, but, hopefully, future work will elucidate the dominant signals in the DCIC population. It may be intuitive that engagement in a sound localization task may push azimuthal signals to the forefront of DCIC response, but azimuthal information could also easily be overtaken by other signals (e.g. movement, learning).

Boffi and colleagues set out to parse the azimuthal information available in the DCIC on a single trial. They largely accomplish this goal and are able to extract this information when allowing the units that contain more information about sound location to contribute to their decoding (e.g., through PCA or decoding on their activity specifically). Interestingly, they also found that positive noise correlations between units with similar azimuthal preferences facilitate this decoding - which is unusual given that this is typically thought to limit information. The dataset will be of value to those interested in the DCIC and to anyone interested in the role of noise correlations in population coding. Although this work is first step into parsing the information available in the DCIC, it remains difficult to interpret if/how this azimuthal information is used in localization behaviors of engaged mice.
