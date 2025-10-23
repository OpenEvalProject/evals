# Peer review - Round 1

Editors:
- Alex Fornito, https://ror.org/02bfwt286 Monash University Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68531.sa0](https://doi.org/10.7554/eLife.68531.sa0)

This valuable work proposes new network-based algorithms for brain seizure characterisation that could improve the effectiveness of existing clinical treatment paradigms. The approach is supported by solid evidence. If validated and compared against existing biomarkers, it could shed light on mechanisms of disease progression. This work will be of interest to clinicians and researchers in epilepsy alike.


---

# Peer review - Round 1

Editors:
- Alex Fornito, https://ror.org/02bfwt286 Monash University Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68531.sa1](https://doi.org/10.7554/eLife.68531.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Multilayer brain networks can identify the epileptogenic zone and seizure dynamics" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Mangor Pedersen (Reviewer #2); Christian Benar (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The prediction of the EZ seems to be completely within-sample. Please provide some indication of cross-validated out-of-sample prediction accuracy.

2. Please evaluate network properties with respect to appropriate null models. An important component of assessing the presence of network structure is to evaluate whether that same structure or nodal importance is not evident in null model where the underlying network structure is randomized. This is key to making sure that clustering results are not just sensitive to random fluctuations in the data. One suggestion is to use a phase-randomization of the voltage trace before computation of HFS to help better evaluate the null distribution of the mlEVC metric. A related reference is: https://pubmed.ncbi.nlm.nih.gov/22343126/

3. The authors may consider that at least one recent study has discussed the challenges and considerations of different recording and electrode sampling techniques on network metrics. And may explain discrepancies in the findings across studies: https://pubmed.ncbi.nlm.nih.gov/32537538/

4. The methods used in this study are complex, and rationale behind the series of steps used to perform the study are not provided. Given that this paper is primarily showcasing a novel method, the authors may want to consider incorporating more methodological details and rationale in-line with the Results.

5. Providing intuition behind abstract mathematical concepts would be helpful. For example (lines 139-141): Help the reader interpret the hierarchical unsupervised clustering applied to the left singular vectors of the concatenated and quantized mlEVC.

6. Line 96: Consider describing the concepts of graph/super-graph, and single/multi-layer in a general sense, first, as this is the first use of these terms in the manuscript.

7. Line 262: Typo, should "EZ-RnRZ" read "EZ-RnEZ".

8. The seizure evolution and state transition plots can be difficult to follow, due to the combination of colors and hues. Please consider a flow field or separate plots per seizure help demonstrate the overlapping and non-overlapping dynamics between seizures?

9. The authors may want to consider incorporating additional details in Table 1, pertaining to: (a) size of the network; (b) number of nodes overlapping with the resected tissue; (c) durations of the seizures; (d) seizure type.

10. One previous study motivated the application of phase and lagged-based connectivity metrics on the analytical amplitude of the broadband signal to avoid computing phase relationships within the asynchronous broadband range of the voltage signal. See: https://pubmed.ncbi.nlm.nih.gov/12631571/. Note that this is distinct from applying phase-based connectivity metrics directly to the high-frequency broadband component of the voltage signal or to high-frequency narrowbands (such as HFOs).

11. If I understand the methodical approach correctly, the authors generate an ordinal graph optimal when using fast intracranial electrophysiological data (500 or 1000Hz). It would be interesting to see a correlation plot between the current eigenvector centrality with an ordinal coupling parameter and cross-correlation of this data at multiple time-lags. In addition to tuning the coupling strength, the current work would be improved to quantify the optimal time interval between matrix 'layers'. It would be useful for the authors to consider/discuss this point in detail.

12. Related to the previous comment, it would be good to head further why the authors choose to use the Phase Lag Index for slow frequency estimation, a measure that does not operate proximately to the zero-lag.

13. A clearer rationale for using a spatiotemporal graph if warranted in this paper. The authors outline and justify the use of multilayer graphs from a methodological point of view, but it would also be good to hear why the authors choose this methodology from a clinical point of view. i.e., what can multilayer metrics tell us about epilepsy that single-layer cannot?

14. Related to the previous point, have the authors thought about comparing eigenvector centrality between multilayer and single-layer graphs, to see whether the results differ between the two?

15. Please provide more details about the filtering procedure, conducted before the Hilbert transform, including the type (and order) of filtering, how the DC offset was accounted for and whether the Hilbert transform in the given frequencies satisfy the Bedrossian's criteria for narrow-band frequency estimation (Xu and Yan, 2006).

16. It would have been nice to see in more detail examples from one or two patients with the actual resection area and the detected networks in volume. Figure 1 would benefit from an intuitive description of the method.

17. P7 It seems to me the term 'primary organization' has to be credited to Talairach and Bancaud. Also, early work on network organization were performed by Wendling and Bartolomei and could be cited (including the desynchronization at seizure onset in Wendling et al. 2003).

18. P8 it is very interesting to see that in a few patients one method fails whereas the other gives good results. This pleads for a complementarity of strategies to cope with inter-patient variability. Can the authors make hypotheses on which signal features/seizure patterns could explain the difference in results across methods and patients?

19. P11 « false positives from the EZ » this really depends on the definition of the EZ. If this is the minimum of cortex to be resected to render the patient seizure free, then the statement may hold. If this is the « primary region of organization of seizures » (definition of Bancaud, given p7), it is possible that not all these regions need to be resected. It would be useful to clarify the two definitions.

20. p17 it would be very interesting to perform a comparison of HF and LF synchrony in predicted the EZ. Moreover, as mentioned below too, part of the HF synchrony can arise from trains of sharp spikes that have energy in all frequencies, which would not be synchrony of high frequency oscillations but an emphasis on the sharp part of ictal spikes. This is not a problem per se, but more an issue of interpretation of the results.

21. Is data processing on monopolar or bipolar montage? Please clarify

22. Is it possible that part of the synchrony arises from filtered spikes? Can the authors provide a (normalized across frequencies) time-frequency representation of a representative seizure in order to assess the relative contribution of oscillations and spikes?

23. P25, eigenvalue centrality. While the rank of the matrix is likely to be T, wouldn't one expect some kind of temporal correlation across points (arising from both the high overlap and some actual temporal persistence of the networks), which would result in an elbow in the eigenvalues after some dimension? If it is not the case, and each time point is independent from the other ones (linear eigenvalue spectrum), what is the added power of multilayer method? Wouldn't a more simple method as summing the degrees across time be equivalent? Please clarify.

24. It would be interesting to visualize the eigenvalues of a representative example in order to measure this. Also, and importantly, it would be useful to compare the multilayer method to a simple mean degree across time (Wilke et al. 2010, van Mierlo et al. 2013, Courtens et al. 2016, Li et al. 2016, Balatskaya et al. 2020).

References:

Kramer, M.A., Eden, U.T., Kolaczyk, E.D., Zepeda, R., Eskandar, E.N., Cash, S.S., 2010. Journal of Neuroscience. 30, 10076-10085.

Schindler, K.A., Bialonski, S., Horstmann, M.-T., Elger, C.E., Lehnertz, K., 2008. Chaos 18, 033119.

Xu, Y and Yan, D, 2006. Proceedings of the American Mathematical Society 134, 2719-2728

Reviewer #1:

In this study, Shahabi and colleagues develop a new computational algorithm based on graph theory to study changes in brain network connections during drug-resistant, epileptic seizures. The structure and organization of these network connections have been the subject of many studies over the past two decades with the principal purpose of mapping seizures and identifying targets for resective surgery. A novel analysis of distributed brain network interactions between the local epileptogenic zone and remote, healthy brain areas outside of this zone is facilitated by invasive stereo-electroencephalographic (sEEG) recordings, which are a key asset to the present study. The authors construct time-dependent functional brain networks based on inter-areal synchrony in the high-frequency band and combine a new graph theory metric called multilayer eigenvector centrality (mlEVC) to quantify the changing pattern of connectivity amongst brain areas within and outside the epileptogenic zone. Using their innovative technique, the authors recapitulate a widely reported result that seizure progression invokes a robust alteration in network organization in which connectivity between the epileptogenic zone and healthy brain areas desynchronize. However, a key contribution of the present study is that the network nodes in the epileptogenic zone whose subsequent surgical resection led to seizure freedom could be predicted using unsupervised machine learning. These findings suggest that nodes involved in desynchronization during seizures may serve as putative surgical targets for epilepsy treatment. The authors also demonstrate that if patients are left untreated, then this abnormal desynchronization process during seizures intensifies with age and duration of epilepsy. This is a compelling scientific advancement in the field that begins to tackle the long-standing question of whether seizures beget seizures.

Generally, the study and analysis are presented as exploratory and proof-of-principle. A major strength of this study is the development of a new methodology to describe complex properties of seizures. However, I have concerns regarding possible overfitting of the data as no cross-validation nor testing was performed. Key claims could be better motivated with concrete hypotheses that are contextualized by prior work. My specific comments are detailed below:

1. Key questions posed in the study are provided and/or stated in the introduction but in many cases the importance or relevance in the broader context are not fully developed. Examples below:

a. Lines 50-52: "It has also been suggested that ictal periods can be delineated by a steady series of states(Burns et al., 2014), although whether this is true in all patients remains controversial."

b. Lines 52-55: "It remains unclear how the degree of desynchronization is correlated with physiological parameters such as age and duration of epilepsy(Van Diessen et 55 al., 2013a)"

2. Much of the introduction focuses on high frequency oscillations and pros/cons of their utility in localizing seizure foci. The authors present ictal high frequency synchronization as a phenomenon of interest, but to the general audience the differences between HFO and HFS are not concretely provided. The rationale for studying ictal HFS over HFOs is also not provided. Are these the same phenomenon? Are they distinct? Why do authors deem HFS analysis important for this study?

a. Lines 75-77: "While HFOs have been employed in analyzing functional(Schindler et al., 2010) and propagation(González Otárula et al., 2019) networks, the spatiotemporal dynamics of ictal high frequency synchronization (HFS) at macroscopic scales remain largely unknown."

b. Lines 238-240: A later point conflates HFOs and HFS as the same phenom: "Early-onset and late ictal HFOs have been considered biomarkers for seizure onset zone identification (Weiss et al., 2013), with the latter found to be a more reliable metric (Modur et al., 2011). Our EZ localization technique considers both features."

3. The interpretation of connectivity in the high-frequency broadband is unclear in the context of previous studies that demonstrate that the broadband activity is due to asynchronous, non-oscillatory neural firing (see references below). Consequently, it is unclear how one should interpret the notion of "synchronization" in the broad 80-200 Hz frequency range.

a. https://pubmed.ncbi.nlm.nih.gov/23283342/

b. https://pubmed.ncbi.nlm.nih.gov/29167419/

4. Was a null network model employed to ascertain whether the clustering procedure and the mlEVC metric identified target epileptogenic zone areas more reliably than chance?

5. What was the trade-off in the sensitivity and specificity of the EZ prediction algorithm? A receiver-operator curve analysis would help here.

6. One concern is that the analysis corresponding to the prediction of the epileptogenic zone is performed at the population level – aggregating nodes across all patients (line 160). What was the mean and standard error of the performance across patients?

7. The comparison between the present method and Fingerprinting method is of great value here. However, a clear conclusion regarding the comparison is not provided because the two algorithms provided results that only partially overlapped. How do these results compare to more conventional measures of the epileptogenic zone such as HFOs or spikes derived from the same dataset?

8. Results regarding the occurrence of different states of connectivity during the ictal period (lines 177-180) are certainly very interesting, but it is not clear how this finding advances previous studies:

a. https://pubmed.ncbi.nlm.nih.gov/20668192/

b. https://pubmed.ncbi.nlm.nih.gov/23366973/

9. A related worry regarding statistical power of the study is reflected in the stereotypy analysis (lines 192-195). To what extent is the stereotypy / lack of stereotypy in the network a function of the dimensionality of the feature space and overfitting of the data? Specifically, as the number of features / complexity of the model increases, are you more likely to find that each seizure event network is different from the others? A cross-validation and out-of-sample prediction approach would help mitigate these concerns.

10. The finding that stereotypy does not necessarily occur at high-frequencies is very interesting (lines 206-209), but the claim is not supported by any statistical testing. Furthermore, the explanation provided "the brain experiences divergent topologies, which might be the result of dissimilar EEG recordings" (line 209) is rhetorical as the topologies are based on features derived from the EEG recordings.

11. Why was the mid-seizure period used to normalize network measures for age/epilepsy duration-related analysis? How is this baseline period more advantageous than a pre-seizure baseline?

12. Were any other connection groups tested as being predictive of age or duration of epilepsy? In particular, is it possible that prolonged epilepsy might reorganize areas that are purely outside the EZ? Was there any relationship between the size of the EZ and age/duration?

13. Can the authors be sure that the emergence in low-frequency connectivity is not related to an increase in the rate or amplitude of ictal spiking? Are they independent phenomena?

14. How are the phases of the seizure (pre-termination, termination, early-seizure) defined? Are they based on the state analysis or on expert ratings of the seizures? A clear definition of these periods would be helpful.

15. Specific steps and choice of parameters in the unsupervised clustering pipeline described in the Methods are not justified. Such as

a. Usage of just the first four singular vectors

b. Limited combinations of the singular vectors

c. Determination of the rank T for the A matrix

d. How the mlEVC approach compares to the traditional EVC approach similar to that studies in the Burns et al. (2014).

Reviewer #2:

The authors combines intracranial EEG data with multilayer network modelling to delineate the seizure onset zone and spatiotemporal network activity during seizures. The major strength of this study is that the networks in this study incorporates spatial and temporal connectivity during seizures, and the relative importance of different intracranial electrodes. This is a novel and interesting approach that is likely to have an impact in the field. Below I discuss two topics (near zero-lag connectivity and previous research in the field) that is worth bearing in mind regarding the current manuscript.

- The authors generate an ordinal graph (connectivity between two adjacent time-points) to quantify spatiotemporal connectivity from intracranial electrophysiological data with a high sampling rate. An ordinal graph computes the connectivity between two adjacent time points, which may represent synchronicity close to a zero-lag in this data. It is worth bearing in mind graphs with connectivity data where time-points that are further apart, and how this may reflect neuronal connectivity at different time-scales.

- The current set of findings are interesting and they show good clinical accuracy at predicting the seizure onset zone. Spatio-temporal connectivity during seizures in this study also align with previous graph theoretical research using intracranial electrophysiological with single-layer graphs. Previous studies show distinct time-varying peri-seizure changes in the clustering coefficient and path length metrics. During seizure initiation and propagation, there is an increase of clustering coefficient and shortest path length, resembling a regularized, or isolated, network topology (Kramer et al., 2010; Schindler et al., 2008). In a network that is regularized, local clusters of neurons may isolate themselves from the rest of the network. It would be good to evaluate the current findings in the context of previous graph theoretical research using intracranial electrophysiological data in epilepsy.

Reviewer #3:

This manuscript introduces a new method for identifying the epileptogenic zone from intracerebral EEG data, based on graph measures in high frequency bands, multilayer graph analysis and clustering.

Graph measures and multivariate methods are promising tools in the electrophysiological characterization of the epileptogenic zone; the strategy proposed here falls within this timely topic. The strength of the approach is to be fully automatic, and to rely on multivariate measures that can capture the overall structure of the data better than the usual monovariate measures. The method identified electrodes within the resected area in 88% of the patients, with only few contacts detected outside of the resection.

It could be interesting to also test the method versus the clinician EZ, as the resected area may be larger this would be consistent with the fact that the 'target' area found by clustering is much smaller that the resected contacts. This would be a further probe of the sensitivity of the method. Another interesting measure would be to probe whether the proportion of contacts outside the resected area increase in non seizure-free patients. Yet another interesting test would be to see whether the multivariate method outperforms more classical measures such as graph strength. In other words, it what does the multilayer approach add to the single layer measures?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Multilayer brain networks can identify the epileptogenic zone and seizure dynamics" for further consideration by eLife. Your revised article has been evaluated by Michael Frank (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below. Please address these comments comprehensively in your response.

1. In their response and amendments to the main text, the authors claim that their method does not require cross-validation and testing over independent datasets since the approach does not involve training the model parameters across patients and does not access information regarding the resection zone. While it is true that the method is applied to each patient, separately, the methodological choices including, but not limited to, functional connectivity metrics, frequency band selection, percentile threshold selection, still effectively "train" the general algorithm and may be highly specific to the cohort studied here. This issue presents itself as a driver of inter-patient variability, as demonstrated by the conflicting findings between the mlEVC method and Fingerprint method. While this limitation detracts from the methodological advances put forth by this study, but some caution in making the claim that cross-validation/testing is not necessary is warranted. Specifically, the manuscript should include a rationale for why cross-validation was not applied in this context, coupled with an acknowledgement that such an approach in future will be important to verify the current results.

2. The relationship between the coupling parameter and network time-scale should be further elaborated, given the importance of this parameter to the authors' claim that patients may have different rates of network change. Please present data examining how sensitive the findings of the EZ are to the choice of this parameter. Please also provide examples of how different coupling parameters would yield more insight into the different time-scales of network change

3. The findings comparing a single-layer model to the multi-layer model should be explicitly quantified to concretely justify the claim in the Discussion section that single-layer models yielded poorer EZ identification than multi-layer models. How much more accurate was the multi-layer model to the single-layer model?

4. More attention should be paid in the text to the risk of contamination of high frequency synchrony by two processes: (1) Filtering of spikes; and (2) Harmonics of non-sinusoidal oscillations. These topics are addressed in the following study, which could be cited in support of the discussion.

Pitfalls of high-pass filtering for detecting epileptic oscillations: a technical note on "false" ripples. Bénar CG, Chauvière L, Bartolomei F, Wendling F. Clin Neurophysiol. 2010 Mar;121(3):301-10

5. The time frequency figures should be accompanied by a presentation of the signal time course in order to fully appreciate the presence/absence of spikes. While there indeed seems to be spikes in the preictal period (vertical lines) , they present much less energy than the high frequency activity during the seizure. This large increase is quite blurred and indistinct and it is not clear what this actually represents. The original signal time course would help understand which seizure pattern this corresponds to.A consideration of the potential effect of harmonics would also be helpful.
