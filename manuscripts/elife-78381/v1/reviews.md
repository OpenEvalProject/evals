# Peer review - Round 1

Editors:
- Vatsala Thirumalai, https://ror.org/03gf8rp76 National Centre for Biological Sciences India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78381.sa0](https://doi.org/10.7554/eLife.78381.sa0)

This important study investigates how neural activity states contribute to and shape sensory responses using a combination of neuronal activity imaging and computational modeling. They show that recurrent connectivity in networks can shape sensory responses in an experience-dependent manner and can be used to explain variability in experimentally-observed neuronal responses to sensory stimuli.


---

# Peer review - Round 1

Editors:
- Vatsala Thirumalai, https://ror.org/03gf8rp76 National Centre for Biological Sciences India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78381.sa1](https://doi.org/10.7554/eLife.78381.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A recurrent network architecture explains tectal activity dynamics and experience-dependent behaviour" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Ronald Calabrese as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Benjamin Cowley (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Rewrite the manuscript to place a clear emphasis on the overall message of the manuscript.

2) Please include more model validations/comparisons (such as the effect of removing inhibition).

Reviewer #1 (Recommendations for the authors):

1. The abstract, introduction, and discussion need thorough revision so that the readers can understand the main take-home message. In its current shape, it is unclear whether the emphasis is on the utility of the LNP model or the proposal of slow, long-range inhibition between neurons in the tectum. I recommend emphasizing the latter aspect, given that the second half of this paper primarily focuses on its role. I agree that they show an excellent network model, but this is still a hypothetical product and the authors did not perform a thorough comparison with other types of models which may fit equally well.

2. I advise the authors to revise the last paragraph of Page 20 and the next one in the Discussion section that starts from "However, this study calls these assumptions into question." I agree that the author's LNP model explains some critical aspects of tectal bursting dynamics (that are defined by the authors), but they did not perform any analyses or model comparison to exclude previously proposed nonuniformities in the connections between neurons. This is an unfair argument and likely provokes unneeded drawbacks from colleagues in the field.

Also, there are existing results and unpublished studies showing that there are heterogeneities in neurotransmitter types in the tectal population that are nonuniformly distributed. Therefore, I advise the authors to rewrite this section to discuss how the potential uniform connectivities between neurons, which are probably shaped through proximity-based mechanisms, co-exist with connectivities that are shaped by other mechanisms to support diverse functionalities in the optic tectum.

3. I advise the authors to dig into the property of the LNP model a bit more to emphasize the importance of hypothetical inhibitory connectivities. It would help the reader to see, for example, how different temporal and distance coefficients of inhibitory connections will alter the nature of spontaneous bursts. Figure 3 uses a space to explain how EMOO process works, but this is distracting and should be moved to the supplementary figure.

4. I recommend having a main figure panel that explains how the authors calculate the "linear drive". It is written in the methods, but this "linear drive" measure is everywhere in the manuscript and it is better to have a dedicated panel.

Reviewer #2 (Recommendations for the authors):

Overall, I enjoyed the paper, and I think it will be a nice addition to the community trying to model trial-to-trial neural variability. In the public review, I basically veiled the analyses I think would solidify the work. Namely, making sure the model is thoroughly evaluated, shoring up some questions I had about the data results, and perhaps linking bursting to the stimulus-evoked activity analyses in some way. I think the claim that a uniform recurrent connectivity motif can also explain bursting (versus assemblies) is fine, but it is not as strong as "better explains the data than an assemblies model". Right now, the reader is left with the question that different models can explain bursting but no definitive answer on which one is correct. If there is a formally-proposed assemblies model, a model comparison would address this issue. More importantly, compare the gaussian distance model with other possible fall-offs (such as other radial basis functions and as a baseline – a uniform model with no distance fall-off) and check the assumption that each neuron falls off at the same rate (i.e., compare σx and σy across neurons). Considering Pillow et al., 2008 was an inspiration for the model, reporting prediction performance R2 (or log-likelihood as in Pillow 2008) for different models (e.g., with/without an inhibitory gain) would provide strong evidence for your claims. Fitting the parameters of a GLM and also showing this gaussian fall-off would show strong support. A key difference between a GLM and the distance model is that a GLM can take into account correlations between the neighboring neurons whereas the distance model assumes all neighboring neurons are independent. In other words, linear regression may take advantage of correlations in input features X (e.g., by subtracting one neuron's activity from another), but the distance model cannot (and thus may not be able to remove spurious noisy signals).

The reported R2s (Figure 4D and 7H, blue distributions) are really weak (R2 ~ = 0.05 for most). Please come up with a null R2 distribution (e.g., reverse time, flip signs) and compare the actual R2 distribution to the null. This ensures there is some signal (even if tiny).

[Editors’ note: further revisions were suggested prior to acceptance, as described below. Please see the Author Response section below for the authors responses to these requests. ]

Thank you for resubmitting your work entitled "Recurrent network interactions explain tectal response variability and experience-dependent behaviour" for further consideration by eLife. Your revised article has been evaluated by Timothy Behrens (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

The revised version seems to have addressed many of the points raised by the reviewers, yet no new modeling has been done as suggested in the original reviews. Some points that were raised during the consultation were:

"…some basic ablations/model comparisons would go a long way. E.g., how useful is the surround inhibition? What if you were to fit σE and σI for each ROI (versus assuming the same σE and σI across ROIs)? If computation time is a problem, they can always subsample. As it stands, their model of "linear drive" explains ~1-2% of the variability (Figure 4e)…which suggests something is missing."

"I did not see the authors' serious efforts in improving the rigor of their LNP model and its comparison with other models. We pointed them out as major concerns, and some of them are not so difficult to address. "

Please take these comments into consideration while preparing the revision.

Reviewer #2 (Recommendations for the authors):

I accept this manuscript for publication. I have read the rebuttal and reviewed the manuscript. Although the authors did not try any further modeling as recommended by this reviewer, this simple model may be of use to the zebrafish field as an instantiation of "nearby neurons do similar things". The low performance in predicting residuals (Figure 4E, < 2% explained variance) suggests there is much room for improvement in modeling these interactions.
