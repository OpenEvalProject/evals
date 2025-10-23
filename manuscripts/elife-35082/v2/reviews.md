# Peer review - Round 1

Editors:
- Laurence Tudor Hunt, Oxford University United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.35082.sa1](https://doi.org/10.7554/eLife.35082.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Changes in global brain connectivity in LSD-induced altered states are attributable to the 5-HT2A receptor" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Laurence Hunt as the Reviewing Editor and Timothy Behrens as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The study examines the effect of 100 micrograms oral LSD administration on resting-state functional MRI data. This has significant effects on Global Brain Connectivity, a measure used to index changes in functional connectivity between regions. The study's key contribution is to pinpoint the pharmacological mechanism of this effect, by showing that it is largely removed by co-administration of 40mg oral administration of the 5-HT2A receptor antagonist ketanserin. Results show that both the subjective and the connectivity changes associated with LSD were blocked fully by ketanserin. Global brain connectivity patterns associated with LSD were also closely linked to gene expression maps of 5-HT2A receptors.

All reviewers were in agreement that this is an unusual and interesting dataset, in terms of the sophisticated 5-HT pharmacology and comparison with gene expression profiles. The reviewers applaud the authors for their use of advanced HCP pipelines. By investigating the 5-HT2A receptor contributions of LSD-induced rsfMRI signal changes, the authors address a relevant topic in psychiatric diseases such as psychosis.

However, all reviewers raised questions about some of the results and interpretations, particularly with respect to the effects of global signal regression on their conclusions.

Essential revisions:

1) The authors show that LSD effects on GBC differ considerably depending on whether global signal regression (GSR) is used during preprocessing. This finding is interpreted to suggest that the results after global signal regression are "correct". The reviewers had concerns about this interpretation. The argument about GSR is not settled, and therefore statements to the effect that GSR "is key for separating signal and noise" are incorrect.

If LSD increases the BOLD signal amplitude in large regions of the brain, this interacts with global signal regression and can drive changes in connectivity. For example, the simulation below shows that whole brain positive-negative effects in GBC that appear very similar to the results presented in Figure 1A can be introduced by the interaction between amplitude changes and global signal regression (note that results without GSR are identical because correlation is scale invariant). It is known that large amplitude changes are found in altered states of consciousness (e.g. during sleep, see Horovitz et al., 2008). It is also likely that the subjects' level of arousal is something that would be expected to change in this LSD study.

% Matlab code for simulation:

T1 = rand(1000,100);

T1 = T1 – repmat(mean(T1),1000,1);% demean

T1_GSR = T1-mean(T1,2)*(pinv(mean(T1,2))*T1);

T2 = [T1(:,1:50).*repmat(2,1000,50) T1(:,51:end)];

T2 = T2 – repmat(mean(T2),1000,1);% demean

T2_GSR = T2-mean(T2,2)*(pinv(mean(T2,2))*T2);

GBC = [mean(corr(T1)); mean(corr(T1_GSR)); mean(corr(T2)); mean(corr(T2_GSR))];figure; set(gcf,'Position',[0 0 1000 400])plot(GBC'); xlabel('voxel'); ylabel('GBC'); title('Simulations to test interaction between amplitude changes and GSR');legend({'Original','Original after GSR','increased amp','increased amp after GSR'})set(gca,'fontsize',16)

A key motivation given for using GSR is that it removes potential respiration artefacts. However, the authors have already removed such artefacts using WM and CSF regression. This lends further evidence to the idea that the global signal in this context may actual represent important global neural activity. All results presented in the manuscript must be interpreted in this context; the effects of any large scale changes in neural activity are not visible with GSR and only focal changes above and beyond these main effects remain.

Given this, and the strong effect of global signal regression on the findings, the reviewers suspect that the results are strongly influenced by underlying changes in amplitude. It is very important to disambiguate these effects, as they would fundamentally change both the interpretation of the LSD effect and the interpretation regarding global signal regression. Therefore, the reviewers argue that a detailed investigation of amplitude changes is absolutely critical for this work.

Lastly, the reviewers find the emphasis on GSR in the manuscript misplaced, and detracting from the core study presented in this work. While they applaud the authors for including results with and without GSR, this work is not well placed to draw generalizable conclusions regarding this preprocessing procedure (particularly given the potential confounds of amplitude changes and hemodynamic coupling changes).

The reviewers' concrete recommendations would therefore be as follows:a) Test directly for amplitude effects (i.e. voxel-wise test for temporal standard deviation, or related measure such as fALFF, between conditions).

b) Continue to present pre and post GSR results, but give them equal weight.

c) Remove all interpretations of GSR-related differences, and instead clarify that this dataset is not well-suited for the purpose of drawing conclusions regarding GSR.

2) One further issue is that without GSR, changes in connectivity are left lateralised whereas with GSR they are not. If the global signal only represents artefacts which are by definition global, then why when leaving it in the data are the connectivity changes confined to one hemisphere? Similarly, it is unclear how the data in Figure 5 can be used to support the idea that GSR is desirable. Indeed, it appears that when comparing session 1 vs. session 2 values that the connectivity values are more repeatable without GSR. In the DMN and the limbic network when using GSR, connectivity values are of opposite sign in the Pla and Ket+LSD conditions when comparing across sessions suggesting the GSR is detrimental to the repeatability of the measure in this data.

3) Are there any known effects of LSD on hemodynamic coupling? While it is challenging to control for such effects in this study, this topic warrants further discussion.

4) The comparison against gene expression maps is a strong element of this paper, however it is presented almost as an afterthought in much of the manuscript. One reviewer felt that the authors could emphasize this aspect more strongly in the paper (although another reviewer cautioned that the correlations are fairly low). The authors may wish to emphasise this part of their manuscript more strongly.

5) The effects of the 5-HT2A receptor are investigated (both pharmacologically and in terms of gene expression). However, the authors list a number of other receptors that LSD binds to. Therefore, a more critical discussion (in a limitations section) of the scope of this paper and the potential role of other receptors is warranted.

6) Changes in subjective drug effects over time are presented (Figure 3). Can the authors comment on test-retest reliability of these questionnaire measures please. For example, what was the change over time in the placebo group for subjects that took part in the placebo session as the first study session?

7) The first derivative of the global signal is also included as a regressor, which is quite uncommon. Please include a (mathematical or empirical) justification for this.

8) One reviewer commented that the barplots and distributions in Figure 1B, Figure 4B and others like them should be removed and not relied upon for interpretation, as they present circular reasoning (Kriegeskorte et al., Nat Neuro 2009). Plotting the average connectivity in areas that are defined by looking for differences in connectivity will always lead to significantly different barplots.
