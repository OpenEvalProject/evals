# Peer review - Round 1

Editors:
- Diego Vidaurre, University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67400.sa1](https://doi.org/10.7554/eLife.67400.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This paper addresses the relationship between the electrophysiological and the anatomical connectomes, utilising a method to describe avalanches of activity. In these rapid events brain activity cascades across cortex. The current paper shows that these avalanches follow the routes of anatomical connections. The result also implies more spatial precision that most would assume possible, which makes the manuscript particularly interesting to M/EEG researchers. The reviewers therefore agree that the paper has broad interest.

Decision letter after peer review:

Thank you for submitting your article "The structural connectome constrains fast brain dynamics" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Diego Vidaurre as a Reviewing Editor and Timothy Behrens as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Andrew J Quinn (Reviewer #1); George O'Neill (Reviewer #2).

Essential Revisions:

1. Resolve if the results are fundamentally driven by leakage

2. Determine the influence of the region size and SNR on the results.

3. Clarify the description of the method

4. Frame the work into the current literature

Reviewer #1 (Recommendations for the authors):

1) The following matlab code illustrates my concern with volume conduction (written in version R2019a). This generates a simple aperiodic signal and linearly weights it into 20 regions before computing an approximation of the avalanches analysis.

%%

rng(42);

a = poly(0.98);

x = filtfilt(1,a,randn(5000,1));

x = x(500:4500); % trim filter edges

% Add two larger pertubations

x(1000:2000) = x(1000:2000) + 400*sin(2*pi*linspace(0,0.5,1001)');

x(2500:3000) = x(2500:3000) + 1000*sin(2*pi*linspace(0,0.5,501)');

% Create + apply linear weights vector

weights = [linspace(0,1,10), linspace(1,0,10)].^3;

y = x * weights;

% Add noise, z-transform and smooth

y = y + randn(4001,1)*60;

y = zscore(y);

y = movmean(y,41,1);

% Illustrate

threshold = 1; % bit low but for illustration

figure;

subplot(211);hold on

plot(y);

plot([0 4001],[threshold threshold],'k:')

plot([0 4001],[-threshold -threshold],'k:')

axis('tight')

title('Linearly mixed signals')

subplot(212)

imagesc(abs(y)'>threshold)

colormap('bone')

title('Avalanches');

%%

Note that in panel 2 on the bottom the onset of the 'active' periods is temporally lagged across regions – sometimes by up to 10s or 100s of samples. The combination of amplitude weighting, noise and z-transforming can therefore induce apparent time-lagged interactions. I don't know how much of the main effect in the paper is driven by this effect but it absolutely must be explored and accounted for. It is not sufficient to say that "The introduction of a time-lag makes it unlikely that our results can be explained trivially by volume conduction"

2) A lot of discussion about the results uses quite forceful causal language.

line 25 "We find that the structural connectome profoundly shapes rapid spreading of neuronal avalanches"

line 100 "We show that the spatial unfolding of neural dynamics at the millisecond scale is shaped by the network of large-scale axonal projections comprising the connectome, thereby constraining exploration of the brain's putative functional repertoire."

Whilst I agree that a structure->function relationship is perhaps the more likely interpretation, this is a correlational study which does not assess whether structure shapes function or vice versa – simply that there is an association. The writing would be improved by acknowledging this and adopting a more cautious interpretation.

3) Some parts of the methods writing is unclear, perhaps as the whole manuscript is so short. For example, I do not understand the second method for estimating transition probabilities outlined here:

"After the initial time-bin of an avalanche, we kept track of what other regions were recruited after the first perturbation. Importantly, we did not scroll through the avalanche in time, as previously described, so as to include time delays as long as the avalanche itself."

4) I am unsure how to interpret the finding that the results are almost completely unchanged by band-pass filtering the data – α, β and γ even have identical R-values. On one hand this could indicate that the results rest completely on wide broadband effects but given the large and well established functional and topographical differences between these oscillations it seems likely that we would expect at least some difference. Particularly as similar past papers do show different structure-function relationships between different MEG frequency bands (https://www.sciencedirect.com/science/article/abs/pii/S1053811918320603). It would be useful for the authors to discuss this point and its potential meaning in more detail.

5) It would be good to see full use of the large datasets presented here. For instance, do the results have test-retest reliability across the two scans analysed per participant? Why only reproduce the finding using the HCP DWI data but not the HCP MEG data?

6) The data appears to be available from the authors 'upon request and conditional on ethics approval' but the analysis code does not appear to be available online.

Reviewer #2 (Recommendations for the authors):

I think you are definitely onto something here, but I am not quite sure if this is necessarily the full picture – yet. It's not too difficult to remedy I imagine, but I think on a technical level I'd like to query two main points on this.

I realise that this is a short communication, but it does appear to assume that no work in the M/EEG field on relating structure and function exists, any previous work been done using fMRI. I think it might be important to just give a bit more context where in the literature this might sit? Just looking around for a couple of quick examples of relating white matter tractography data to functional connectivity, there's a study relating EEG connectivity to structural connectivity (Glomb et al., 2020, Network Neurosci. 4 (3): 761-787) And plenty of modelling papers which trying to look at how structure would generate observable M/EEG connectomes (eg. Tewarie et al., 2019 NeuroImage 186). I think a slightly wider look at the literature on this would be really helpful. Crucially, it's not that I don't think that this isn't novel, but rather it seems to currently seems to not acknowledge the exitance of previous work in the M/EEG field?

The use of neuronal avalanches method, is it as invariant to leakage as you initially think it is? Leakage is a product of signal variance (c.f. O'Neill et al., 2015 Phys. Med. Biol R217). So if a signal is stronger in amplitude, the leakage increases and can propagate further. So in principle, if a seed area reaches over a threshold z-score, it could continue to raise in amplitude such that a test area might also then reach a threshold? Could other (i guess more established) connectivity metrics be able to resolve this also? I was wondering even if you assume stationary variance in your signal, you might be able to analytically estimate 'leakage' between two areas (see the O'neill paper above for an analytic expression). Could you then (potentially) have a leakage connectome and see how well that predicts your avalanches perhaps? If its considerably less than the structural, I'd be a lot more confident in what I am seeing.

Reviewer #3 (Recommendations for the authors):

Is the in-house software written in Interactive Data Language (used for calculating the number of streamlines connecting each pair of ROIs and the corresponding mean tract length) publicly available? If so, please provide a web link to it.

A bit of extra information about the MEG scanner would also be useful, in addition to reporting the actual number of channels that were manually removed.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "The structural connectome constrains fast brain dynamics" for further consideration by eLife. Your revised article has been evaluated by Timothy Behrens (Senior Editor) and Diego Vidaurre (Reviewing Editor).

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

As you can see, all Reviewers are satisfied with the responses, but Reviewer #1 requests some further clarifications on the simulations, and a possible improvement. Since this seems very relevant to the contents of the manuscript, we would like to ask you to go through one more revision.

Reviewer #1 (Recommendations for the authors):

Many thanks to the authors for a clear and thorough response to my queries. Overall, the revised manuscript is greatly improved and the changes largely address my concerns.

I must ask for one final clarification, and possible addition, to the simulation scheme looking at leakage. The revision doesn't state whether any noise is added at the sensor level between projection through the leadfields and subsequent beamforming – is any noise added here? If so, please in include any details (and my apologies if I missed this detail somewhere)

If not, then this additional step should be added to the pipeline. As it stands, the simulation without sensor noise creates unusually favourable conditions for the beamformer. Environmental and sensor noise have their own dynamics and can be correlated in time and across sensors, these correlations mask neuronal signals and can be tricky for the beamformer to completely remove.

A gold standard would be to add sensor noise from an empty room recording, or if this is impractical then some modestly scaled noise whose sensor x sensor covariance matrix an example empty room recording.

The correlations of both the 'coupled' and 'uncoupled' simulations are substantially lower than the observed value in the 'correlation of lineally mixed surrogates' figure. I suspect this is partially due to favourable beamforming from missing sensor noise, as it stands the beamformer is able to remove nearly all spurious events. Including the sensor noise would likely induce some more spurious connections in both the coupled and uncoupled cases, it would be a very strong validation of the method to demonstrate that these are still distinguishable from the observed effects.

Reviewer #2 (Recommendations for the authors):

The authors have met my initial concerns with the submission. Assuming other reviewers feel the same I am happy with this being published.

Reviewer #3 (Recommendations for the authors):

Thank you very much for your revisions. My comments have been addressed satisfactorily.
