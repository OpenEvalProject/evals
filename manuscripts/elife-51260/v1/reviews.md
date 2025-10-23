# Peer review - Round 1

Editors:
- Samuel J Gershman, Harvard University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.51260.sa1](https://doi.org/10.7554/eLife.51260.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The reviewers and I agree that this work offers important new data bearing upon the role of dopamine in exploration. We appreciated the thoroughness of the modeling and data analysis.

Decision letter after peer review:

Thank you for submitting your article "Dopaminergic modulation of the exploration/exploitation trade-off in human decision-making" for consideration by eLife. Your article has been reviewed by Michael Frank as the Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Samuel J Gershman (Reviewer #1); Bruno B Averbeck (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper reports a new drug and neuroimaging dataset using a multi-armed bandit task previously studied by Daw et al., (2006), who also used fMRI (albeit with a smaller sample size). The main new results here come from the drug treatment (L-dopa and haloperidol), since the models studied here are nominally the same (though the authors use a more sophisticated hierarchical Bayesian estimation scheme). Consistent with (some) earlier work, models incorporating both directed exploration (in the form of an exploration bonus tied to bandit arm uncertainty) and perseveration (a tendency to repeat a previous choice) outperform models lacking each of these effects. The main novel finding is that L-dopa reduces the strength of the uncertainty bonus in exploratory choice. While fMRI contrasts between explore and exploit trials did reveal differences in line with previous literature, there were no drug effects that reached statistical significance, save for one exploratory analysis at a reduced threshold. The authors should be commended for comprehensively reporting both positive and null effects. The reviewers also agreed that the paper is for the most part technically well-executed and provides much-needed data on an important set of questions in the reinforcement learning literature.

Essential revisions:

1) The model comparison includes sensible models (it's also nice to see consistent model ordering across conditions). One thing that's missing (as noted in the Discussion section) is a model of random exploration dependent on "total uncertainty" (see Gershman, 2018, 2019), which should theoretically act as a gain modulator of the values. In fact, what's called the "overall uncertainty" is almost identical to this quantity, and is used in later analyses but apparently not in the choice rule.

2) It doesn't quite make sense to link the neural representation of "overall uncertainty" to the uncertainty-based exploration strategy formalized in this paper, because that strategy uses an uncertainty bonus, which means that the critical quantity is *relative* not *overall* (or "total" in the terminology of Gershman, 2018) uncertainty (relative and total uncertainty have been distinguished by previous imaging studies: Badre et al., 2012; Tomov et al., 2019). One approach, as suggested above, would be to build uncertainty-based random exploration into the behavioral model, and then connect the quantities in that model to the neural and drug data. Another (not mutually exclusive) approach is to look for neural correlates of relative uncertainty (i.e., the difference between uncertainties). For example, using the uncertainty of the chosen option relative to the average uncertainty of the unchosen options.

3) The manuscript is quite long and has a lot of detail that could be relegated to supplemental or summarized. Each subtopic received at least a page in the Discussion, comprising one paragraph of discussion of results followed by lengthy literature review and speculation about its relation to other findings. All of the detail is interesting to a small percentage of expert readers. However, for most readers it makes it hard to get at the main results. As many of the outcomes are null findings, this is even more of an issue. For example, Figure 3 could be removed and replaced with some text indicating means and 95% Cis. Figure 4 is too much detail. Also, the paragraph that discusses how the inclusion of the perseverative coefficient in the model increases sensitivity for directed exploration could be in supplemental (this is worth pointing out, since the original Daw study did not find evidence for this, but this will be of interest to a small number of people, especially since several other studies have now found evidence for an uncertainty bonus). Also, the paragraph that shows no evidence for U-shaped dopamine effects and similarly the figure showing RPE effects in the ventral-striatum could go to supplemental. And correspondingly, a bit more behavioral data might be useful. For Figure 2, is there a way to show a summary figure, across subjects? One of the issues with the original Daw study, was that it was very hard for the participants to learn. How well are the participants able to track the values, and find the best option? Is there a way (might be very hard) to illustrate the effect of L-dopa on directed exploration by directly plotting behavioral data?
