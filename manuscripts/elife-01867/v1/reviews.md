# Peer review - Round 1

Editors:
- Jody C Culham, University of Western Ontario , Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.01867.013](https://doi.org/10.7554/eLife.01867.013)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Fast transient networks in spontaneous human brain activity” for consideration at eLife. Your article has been favorably evaluated by a Senior editor and 3 reviewers, one of whom, Jody Culham, is a member of our Board of Reviewing Editors.

The Reviewing editor and the reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

All three reviewers described your manuscript as “interesting” and highlighted its novelty. One external reviewer stated, “Overall this is an excellent paper. The topic is important and timely. The results are provocative.”

While all three reviewers agreed that the paper will make a substantive contribution, there was also a consensus that the manuscript requires revisions to resolve several issues.

The following four main revisions are required (with further details from the reviewers appended for reference):

1) Discuss (or provide additional data to address) what the extracted states are reflecting in terms of network processing, particularly the degree to which they reflect stationarity and independence of networks.

2) Directly address the discrepancies between these results and fMRI RSC networks. Address the concern that some of the differences arise from the constraint that the networks not overlap (such that “hubs” like the precuneus aren't found).

3) Provide greater methodological detail and justification for the analytic choices made, particularly with respect to the rationale for choosing eight states and collapsing across subjects.

4) Do not overstate the links to EEG microstates.

Point 1

Reviewer 2:

Electrophysiological data are nonstationary, and periods of oscillatory activity are particularly so, as frequency and amplitude of neural oscillations are quite dynamic; in fact, nonstationarity can be regarded as a characteristic of oscillatory activity (Mäkinen, May, & Tiitinen, 2005). Since each extracted state was multivariate normal, the HMM technique as applied here might be detecting the most-stationary epochs in resting MEG data, which would suggest that rather than detecting networks, it is detecting epochs during which minimal oscillatory (i.e., network) activity is present in a given region. One simple means to assess this would be to describe the characteristic frequency of each of the 8 detected states using e.g., a Fourier transformation at the center of mass for each network as presented in Figure 2. If this would constitute too much additional work, the authors should provide a substantial and well-referenced limitations section. Given that HMM is also an effective method of spike detection in M/EEG data (Ossadtchi, Mosher, Sutherling, Greenblatt, & Leahy, 2005) the authors should describe in detail the methodological differences between HMM for spike detection and HMM as used in the present study.

Reviewer 3:

1. The method identifies states that are mutually exclusive. In order to study interactions between networks by definition the networks must be coupled. The authors propose to study interactions by analyzing the time course of the fractional occupancy. While this may be reasonable, the pros and cons of this approach, and how much traction we get biologically, must be clearly stated. At one extreme one could argue that given the methodology allows to tracks the temporal alternation of unique and independent states, it does not tell us anything about across–network interactions.

2. The identification of the brain states is driven using a fairly simple model. What is the justification for Gaussian models in building the posterior and non informative priors? Should there not be some prior validation on real data?

3. Relationship RSNs - brain states: please explain whether the approach is somehow circular: from MEG envelope - > PCA - > only 8 brain states and then again the authors compare the states with the data via correlation?

4. The HMM procedure to identify brain states exclude, by definition, cortical hubs, i.e., nodes involved in more systems (see for example the absence of PCC in DMN). How does this limit the interpretation of results?

Reviewer 3:

DMN-DAN anticorrelation. The transition between the states DMN-DAN does not relate to their anti-correlation in my view. It is just telling us that when the DMN is coupled the DAN is not and vice versa but this is obvious based on the HMM state extraction. This is true to some extent for all pairs of networks since again the states are mutually exclusive. The argument is based on the time course of the fractional occupancy (limitations noted above apply here).

Even if the nets were free to overlap, the results indicate that the transition between DMN and DAN are infrequent. This is in contrast with the fMRI literature where these two networks are strongly coupled, so should show correlated alternations according to this method. I think that the observed infrequent transitions are actually in favor of the opposite hypothesis, namely that these two networks are not correlated. Furthermore, the issue of anti-correlation between DMN and DAN should not be over-emphasized given that even in fMRI there are significant questions with regard to their biological significance.

Point 2

Reviewing Editor:

One keystone of the paper is the finding that at fine time scales as well as the coarser scale measured by fMRI, activation in the default mode network (DMN) is negatively correlated with activation in the dorsal attention network (DAN). However, the networks measured here show only partial overlap with the standard networks measured by fMRI. For example, the putative DMN network shown here does not include activation in the precuneus and the putative DAN only coarsely overlaps with the fMRI DAN. These discrepancies should be explicitly discussed.

Reviewer 3:

1. The RSN topographies do not seem standard even according to the authors' prior work:

a) DMN is missing posterior cingulate;

b) VIS is split in 3 separate states;

c) The parietal network is quite diffuse, and important nodes such as FEF are not seen? More importantly, what is the meaning of a state that is negatively correlated with the power envelope time course? Does the diffusiveness of the maps may suggest that these states are not truly within-network, but by themselves reflecting across network interactions? What is the actual spatial correlation between RSN measured on slow envelope and HHM states?

d) Previous work emphasizes bilateral networks, while here some networks are bilateral while other are more unilateral (e.g., temporal). Please comment.

2. If the brain states efficiently capture all dynamic states, one could expect that all of the brain is covered. What percentage of gray matter is covered by the network states? Are the holes, e.g., PCC potentially reflecting 'hub' like activity?

Point 3

Reviewer 2:

Significant methodological detail is omitted. No rationale is given for the number of states selected. It is unclear whether all states occurred in all subjects, and no rationale is given for temporal concatenation across subjects. As currently presented, it remains possible that the detected states are subject-specific. It is also unclear whether the authors used existing beamformer code (e.g., Fieldtrip; Oostenveld, Fries, Maris, & Schoffelen, 2011) or created their own. In addition, no details are given on possible interactions between beamforming and HMM. Finally, the authors state that after beamformer projection, downsampling, enveloping, and concatenation, the envelopes were pre-whitened into 40 principal components. Some information on the topography of these components should be provided.

Reviewer 2:

Some details are incorrect. For example, in their discussion of ICA in the section headed “Relationship with functional connectivity at slower time scales”, the authors state that “...two regions will tend to be strongly represented in the same component (“network”) if their time courses exhibit a strong time-averaged correlation over all time points.” This is true for spatial ICA as typically applied to fMRI data, but not for temporal ICA which would ordinarily be applied to MEG data.

Point 4

Reviewer 2:

The posited relationship to EEG microstates is conjecture, unsupported by the presented data. It is also unclear how infrequent bursts of neural activity underlying transient microstates would explain the sustained changes in blood oxygenation required to produce the BOLD timecourses observed in RSNs.

Reviewer 3:

The discussion points to a paper by Mantini et al 2007 showing that fMRI timeseries in DAN/DMN respectively were negatively/positively correlated with alpha/beta EEG power. However that relationship with EEG does not say anything about their mutual coupling.
