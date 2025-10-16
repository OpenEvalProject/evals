# Peer review - Round 1

Editors:
- Tatyana O Sharpee, https://ror.org/03xez1567 Salk Institute for Biological Studies United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86547.sa0](https://doi.org/10.7554/eLife.86547.sa0)

This important study investigates thalamocortical communication and cross-frequency coupling in human and animal models under anesthesia, seizures, and the effects of the serotonergic psychedelic compound 5-MeO-DMT. These findings are exciting and compelling because they put different perturbations of brain functions – anesthesia, seizures, and psychedelic stimulation – into a single modeling framework demonstrating how these opposing perturbations reduce and enhance thalamocortical communication at specific frequencies. The evidence is compelling because it comes from multiple animal models and also incorporates a state-of-the-art neural mass model to investigate critical brain dynamics.


---

# Peer review - Round 1

Editors:
- Tatyana O Sharpee, https://ror.org/03xez1567 Salk Institute for Biological Studies United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86547.sa1](https://doi.org/10.7554/eLife.86547.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Criticality supports cross-frequency cortical-thalamic information transfer during conscious states" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Timothy Behrens as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Michael Wibral (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The manuscript is exciting but there are several technical issues that need to be addressed:

Both reviewers make suggestions for improving statistical analyses. These are most important to address.

It is also important to place the work in proper context by discussing prior work on neural mass models and the impact of a particular choice of dosage for the psychedelic.

Reviewer #1 (Recommendations for the authors):

My recommendations to improve this paper are the following:

1. Is there any behavioral information that could indicate the onset of psychedelic-like effects in the animal model? (e.g. head twitch response). Was the serum concentration of 5-MeO-DMT measured? Reporting this information could be useful to understand the effects of the dose of 5-MeO-DMT received by the animals.

2. Discuss in detail the novelty of the approach over previous studies, beyond the investigation of the 5-MeO-DMT condition, focusing on the model implementation and commonalities/differences.

3. Can channels be identified and excluded based on the presence of abnormal background activity indicative of seizures and/or tremors? Perhaps the authors could establish that the selected data did not present abnormalities that could, by themselves, drive some of the results.

4. Either perform the correction or justify why this is not needed. et al.

Reviewer #2 (Recommendations for the authors):

I would like to focus here on methodological and technical issues, as there are some of these that prevent a final interpretation of the results. To be clear, I do not strongly expect the main results to change dramatically, yet the way the novel Pinzuti et al. method is used here is not up to best practices and could indeed set an unfortunate example for future studies. Such difficulties in using a brand-new approach are fully understandable but nevertheless need to be corrected

1. Formula 16 on page 22: The considered variables of the random process X need not necessarily start at t-1; due to physical delays they may be found further in the past, i.e a t-δ, and then stretch to t-L. This δ can (and should) be optimized – also according to the literature that the authors cite. Also, the variables considered for the past of the random process Y need not extend to the same temporal depth L – more, or less, random variables may be the optimal choice here. From what the authors write further down, I deduce that they actually did optimize at least the delay δ; it's just that formula 16 does not properly reflect this.

2. The 'Schreiber history length' is given as k=1. There are two issues here: One minor issue is that this history length is not linked back to formula 16, thus the reader does not know which parameter in the above formula is chosen here. The second, and way more important issue is that a history length of k=1 is almost never a reasonable choice. For reasons explained for example in Wibral et al.. PLOS One, 2013 this choice of history length typically strongly underestimates the information already present in the history of the target random process (Y in formula 16); this leads to an overestimation of the transfer entropy – as explained also in detail and graphically in Lindner et al., BMC Neuroscience, 2011. Available Transfer entropy toolboxes (including Lizier's jidt, if I am not mistaken) offer ways to recursively, and automatically determine the variables that have to be considered. Also, in the original publication of Pinzuti et al., one prerequisite of using the spectrally-resolved TE is to already have an established set of the relevant variables in the source and the target random process (and not to just set k=1). I would suggest rerunning the analysis with an adapted history length. (Question: Did the authors potentially mean the Theiler exclusion length parameter (kth in the idtxl java code, I think)? )

4. What was the number of nearest neighbours K used in the analysis?

5. For all statistical tests involving Pinzuti's method it would be good to actually show the obtained surrogate-data based null distributions.

6. To me it is unclear how the initial exploratory analysis and the confirmatory statistical analysis relate. If these analyses were done on the same data, with the second analysis using a statistical test on a feature selected from the exploratory analysis of the same data with the same question (as manuscript lines 150-153 imply), then we have a clear case of so-called "double-dipping", or a circular analysis. For an explanation of this problem see Kriegeskorte et al., Circular analysis in systems neuroscience: the dangers of double dipping, Nature Neuroscience, 2009. Double dipping is considered not permissible in statistical data analysis. One solution would be to split the data – determine the feature (here: the frequency combination of interest) on a (small) subset of the data, and then run a confirmatory analysis on the remaining data. Another option would be to forego statistical testing of the cross-frequency TE and to just test and report the modulation of the spectral TE at the exploratorily chosen frequency combination by the experimental conditions. This way, the claim of having 'found' a specific and highly conserved frequency combination for thalamocortical communication would have to be dropped, but the claim to have found a modulation of frequency-specific information transfer could be upheld. A third possibility would be to not do an exploratory pre-analysis but to directly analyse the data for significant spectrally-specific TE across all relevant (see explanation below) frequency combinations, including a correction for multiple comparisons (multiple testing) performed in that case. All three possibilities for fixing this issue would be acceptable to me.

If there is a misunderstanding of the exploratory data analysis and the data used therein, please explain.

(Explanation of the use of 'relevant frequency combinations', above:) The authors claim that prohibitive computational cost made the direct statistical analysis of all frequency combinations impossible, as the number of combinations is quadratic in the number of frequencies. This statement is correct, but such an analysis is actually not necessary at all. Rather, it would suffice to first only scan the possible source frequencies for significant senders, and the target frequencies for significant receivers separately – as it is done in the original publication of Pinzuti. This problem is linear in the number of frequencies and appears tractable. After this step, only the combination of the significant source and target frequencies must be investigated with the SOSO test, again likely a low number. (Following Pinzuti et al.'s recommendation strictly, it would be only necessary to apply the SOSO test to the combination of the most significant source and the most significant target frequency, as the presence of multiple source and target frequencies leads to an assignment problem of the partial information decomposition type.; but in practice, it should be OK.)

7. If the statistical procedures were implemented by the authors themselves it would be good to know whether the original data were included once as one realization in the surrogate-data based distribution. This is good practice to mitigate the detrimental effects of two little surrogate data (like 100 used here).

8. Also, in my opinion just using 100 surrogate data for the randomiaztion test is very much on the low end of the permissible spectrum. I would much rather like to see 250+ surrogate data sets. Maybe the authors could rerun one of their most important analyses with a (much) higher number of surrogates?

9. Introduction: There are different types of critical points in neural dynamics like transitions from order to chaos, or from stable to runaway activity. Both types of transitions have received a lot of attention in neuroscience, with the first one possibly being more important for cognitive processing, while the latter seems to play a role in relation to epilepsy. It would be good if the authors made it very clear in their introduction that both types of critical transitions are topics in neuroscience and that they focus exclusively on the order-to-chaos transition. This will prevent misunderstandings.
