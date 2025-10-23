# Author response - Round 1

Authors:
- Tung D Phan ([ORCID: 0000-0001-5957-7566](https://orcid.org/0000-0001-5957-7566))
- Jessica A Wachter
- Ethan A Solomon ([ORCID: 0000-0003-0541-7588](https://orcid.org/0000-0003-0541-7588))
- Michael J Kahana

## Response text

DOI: [10.7554/eLife.42950.026](https://doi.org/10.7554/eLife.42950.026)

Reviewer #1:

[…] While their approach is intriguing in places, and the inference of multivariate couplings is indeed an open topic in the field, I have several considerations that limit my enthusiasm. I would request the authors to address these in detail before reconsidering the manuscript.

First, the authors introduce a novel method for estimating model parameters without showing many of its central properties. Most importantly, the data-sensitivity of multivariate approaches is not explored here (although the authors do acknowledge it in the Introduction): how does the variability of their method depend on the amount of data? Appendix 1—table 1 does not address these problems. Furthermore, the three example studies are not a systematic proof of the consistency of the estimate. What happens, for example, if the largest eigenvalue of the coupling matrix is close to 1, i.e. close to a phase transition?

Second, in this light the authors should at least compare their method to established pair-wise quantities (cross-correlations, synchronization, information theoretic measures) and show that the observed decoupling is not equally visible in these well-established (and more data-efficient) methods.

Third, there is considerable literature on multivariate time series analysis, including volatility. For example, ARCH and GARCH models are rather frequently used. One reference that I am aware of (although this is just the tip of the iceberg) is Galka et al. (2010). The authors should relate their work to the established models, show how they differ and what benefit their novel approach yields.

Equation 1: I do not really understand why the model is constructed this way. I understand that the modeled variance enters exponentially, but do the authors have a justification for this approach? Second, the approach presented here only correlates the variance over time, while ϵjty is still drawn from a normal distribution. If I am not mistaken, yt will hence look like Gaussian noise with changing amplitude. Does the data look like this? I would expect a more pronounced autocorrelation of the raw EEG signals. It might help if the authors showed (and clearly marked, see below about Figure 1) example data that they try to fit.

We apologize for not providing enough details on the construction of the MSV model. The exponential term is actually the variance process, which is always positive. We model the log-variance using a vector autoregressive process since the variance is approximately log-normally distributed as demonstrated in the “Volatility of IEEG is Stochastic” section. In addition, we work with the detrended timeseries (after removing autoregressive components) instead of the original voltage series. The new Figure 1 demonstrates the process of going from the raw iEEG data to the volatility timeseries.

Figure 1: I find panel C inconsistent and incomprehensible in many respects. (i) Why are there 1 second intervals shown in the Countdown period? Why is this panel shown at all, given there are no data? (I guess this indicates that these data were not analyzed?). (ii) In the encoding period, why are there pauses between the words? These pauses are not mentioned in the description of the experiment. Are they included in the analysis or not? If not, why are the data still shown, given no data are shown for the Countdown period? Also, the label indicating the length of the intervals is rather hidden, given all other scales are at the top of the diagrams. Last, what does REM / Not REM mean? It can be guessed but is not explained anywhere. (iii) A distractor task following the encoding is mentioned in the text but not shown in the figure. (iv) The free-recall diagram is not explained at all. Was it analyzed (so far, the text says otherwise)? If not, why are data still shown, and what do the intervals indicate? Also there is no length scale for the white intervals. (v) The panel does not state what the plots show. The (very small, and unintuitively placed) label "Compute volatility" seems to indicate that it is the time series yt,i of two channels, from which the volatility is then computed? (vi) I think readers could greatly benefit from an illustration of the workflow from y to theta and x, for example incorporating elements from Appendix 1—figure 1.

We replace Figure 1 in the previous manuscript with Figure 2 in the current manuscript. Figure 2 now includes the three relevant phases of the free-recall task, the recording locations, and the work flow of the MSV model.

Subsection “Relation to Spectral Power”: This whole paragraph is imprecise in the details. (i) What is an "encoding event"? If it is each single word during any encoding period, this would imply a data length of 1.6 seconds each. How would this fit with the Introduction, which states that fitting a multivariate model is hard for limited data? (ii) The Materials and methods say that averaging was done per subject. So does Figure 2 show exemplary results for one subject? If so, this should be indicated, and the generalization to all subjects discussed.

We apologize for not being clear. An encoding event is just a single word event. We apply the MSV model to the combined dataset of all encoding events with the assumption that these events share the same set of parameters which govern their volatility processes. This assumption is also stated in the Materials and methods section. Figure 2 in the previous manuscript now becomes Figure 3. In Figure 3, we clearly state that the confidence bands are constructed across subjects. Since each subject has multiple sessions of recordings, we run a separate MSV model for each session within a subject and the results are averaged across sessions.

Subsection “Classification of Subsequent Memory Recall”: I get that the authors want to show the predictive power of volatility. However, to make this point it would suffice to show that it is above chance level. I do not see the significance of comparing it to the predictive power of methods based on the power spectrum. Furthermore, why does the classifier only take into account each band of the power spectrum? Should a classification based on all bands simultaneously not be much more powerful?

We compare the performance of volatility to that of spectral power at a specific frequency in predicting subsequent memory recall to ensure that the two classifiers have the same number of features, thus making it a fair comparison. As you suggested, the classifier based on all bands yields a higher performance due to having a lot more information. What our manuscript suggests is that volatility contains more information than each of the individual frequencies.

Subsection “Directional Connectivity Analysis”: While I understand the approach by the authors, the results are displayed in a way that I find hard to comprehend. (i) The authors should indicate the inferred values for the coupling matrix and discuss its significance for the dynamics of the process (intrinsic timescales etc.). (ii) The authors first state that directed connections between left HC and PRC decrease, but then also say that the difference between directional connections between these areas is not significant. Do they refer to the difference between HC → PRC and PRC → HC? If yes, do the reported p-values refer to the R or NR set of items?

(i) The inferred values reflect the lag-one correlations among different locations in the brain, which are explained in the construction of the MSV model. (ii) Yes, the reviewer is correct. We compare the difference between HC→ PRCand PRC→ HC. However, each connection itself is a contrast between the recalled-item network and the non-recalleditem network. We simply want to test to see whether the directional connections between these two regions are symmetric.

The first three paragraphs of the Discussion are a mere introduction or repetition of results, and should hence be included in the Introduction or be omitted.

We have fixed the first three paragraphs.

Discussion, fourth paragraph: Why is the decoupling only found in the left hemisphere? This striking difference is completely neglected by the authors. Although I am not too familiar with the cited study by Fell et al. (2006), it does not appear to confirm this difference between hemispheres. As this limitation to the left hemisphere will probably be very obvious to many readers, the authors should discuss it.

We include several citations in the Discussion section to explain this lateralization effect. In particular, the coupling only found in the left hemisphere is in line with neuroanatomical, electrophysiological, and imaging studies that found an association between verbal memory and the left MTL.

Discussion, last paragraph: The authors suggest that fellow researchers can use and extend their method. With this in mind, it would be very beneficial if the authors made their code publicly available.

The code has now been made available on GitHub.

Reviewer #2:

[…] The authors do a good job of placing the MSV model in the context of non-parametric methods such as spectral analysis and provide a means to link the two together. Through this linkage the authors are able to show that the correlation between volatility and spectral power is nearly proportional to the analysis frequency in the spectrum. This suggests that neural activity in the gamma band is more volatile than at lower frequencies. This result is of interest because it suggests that the conflicting reports in the literature about the nature and function of gamma band activity in neural activity may in part be due to the application of non-parametric methods that require that the time series be stationary over the data periods of interest.

One improvement here would be if the authors also included the analysis of the neural activity during a time window other than the encoding phase. For example, if the countdown phase was also submitted to the same MSV modeling, the hippocampus and perirhinal cortex should show a different functional connectivity than what was reported for successful encoding of words. The authors should also comment on whether the MSV modeling can be applied to a network that includes 20 distinct sites, instead of just 4, as was done in the paper.

As suggested by reviewer 2, we ran a connectivity analysis to compare the connections within the MTL region between the resting state period and the encoding period (including both recalled and non-recalled items). However, we did not find any significant connections after correcting for multiple comparisons (see Author response image 1). This suggests that the contrast between recalled and non-recalled items is perhaps stronger than the contrast between the resting state period and the encoding period.

Reviewer #3:

This is excellent work and directs us away from looking at directional measure of influence based on pure autoregressive models (which focus on the conditional mean). Rather interest is focused on the conditional variance, which is shown in a clear way to have advantages over traditional Granger Causality measures. I am convinced by the evidence presented.

The paper would benefit by clarifying the sub-types of stochastic volatility models. There is some confusion in the field. The authors seem to be applying a type of GARCH model, sometimes proposed as distinct from SV and sometimes a subtype.

I do suggest that some prior work be cited properly. The Wong paper is cited in a way that suggests that it is relevant for emphasizing non-stationary when in reality is also a multivariate stochastic volatility model. The same group even attempted source localization in Galka, Yamashita and Ozaki (2004). This is all well covered in the book by Ozaki on time series modeling of neuroscience data.

Finally in the Discussion I would suggest a discussion with combined AR type models and those with stochastic volatility: see Mohamadi et al. (2017).

I also do not see if the code will be made publicly available.

We add a literature review of volatility models in the “Volatility is Stochatic” section which includes a discussion of the GARCH-type models. In addition, we cite applications of GARCH models to EEG as suggested by reviewer 3. Furthermore, the MSV approach does incorporate AR-type model with stochastic volatility since we detrend the raw voltage timeseries first using an AR model and then apply the MSV model to the residual timeseries. The code of this study is now available on GitHub.
