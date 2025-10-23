# Peer review - Round 1

Editors:
- Jörn Diedrichsen, https://ror.org/02grkyz14 Western University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74478.sa0](https://doi.org/10.7554/eLife.74478.sa0)

Using data from an tetraplegic individual, the authors show that the neural representations for attempted single finger movements after multiple years after the injury is still organized in a way that is typical for healthy participants. They also show that the representational structure does not change during task training on a simple finger classification task – and that the representational structure, even without active motor outflow or sensory inflow, switches from a motor representation to a sensory representation during the trial. The analyses are convincing, and the results have important implications for the use and training of BCI devices in humans.


---

# Peer review - Round 1

Editors:
- Jörn Diedrichsen, https://ror.org/02grkyz14 Western University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74478.sa1](https://doi.org/10.7554/eLife.74478.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Preserved motor representations after paralysis" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Jörn Diedrichsen as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Richard Ivry as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) One important question to address clearly in the revision is the mismatch of the representational structure of the recorded PPC site with the SPLa ROI from the imaging studies (and the match with M1). Reviewer #1 raises the important questions that fMRI ROI is likely not equivalent to the recorded site and should be modified and the finding reinvestigated. If the discrepancy persists after the reanalysis, Reviewer #2, and #3 make suggestions for a clearer discussion of the findings. Overall, the claim of the stability of pre-injury organization probably needs to be tempered a bit.

2) The stability of representations across learning is an interesting finding, but Reviewer #2 and #3 both made the valid request that you should more clearly discuss possible reasons for why the basic manifold of neural activity was preserved, by comparing it to previous studies that have found "off-manifold" learning (delayed feedback, recalibration, training protocol – see reviews). In this context you should also discuss the limitations of having N=1. Although the reviewers agree that case studies in this scenario can be valuable, the limitations in generalization should be noted and discussed adequately.

3) All reviewers agreed also that the temporal change of the representational structure was a very interesting point. Please address the specific comments raised in the reviews for this analysis. As this is likely the most novel contribution of the paper, we believe it should be more explicitly mentioned in the abstract / introduction and more clearly discussed at the end of the paper.

Reviewer #1 (Recommendations for the authors):

I found the investigation very interesting and illuminating. Personally, I believe that the third result (i.e., the time-dependency of the representational structure) is one of the most interesting results of the paper, and should be mentioned in the abstract / introduction.

My only main comment concerns the first result – the comparison of the representational structure with previous fMRI results. Judging from Figure 1 – supp 1, the implantation site is located right on the boundary between the postcentral gyrus and posterior parietal cortex, seemingly ~5mm anterior to the peak of activation observed during grasping (AIP). Thus, based on the ROI definition used in both Ejaz et al., (2015) and Kieliba at al., (2021), it would be right on the boundary between SPLa and S1 – and cycto-architectonically, right on the boundary between BA2 and BA5. The SPLa ROI in Kieliba at al. extends substantially posterior to this. Thus, it is not clear whether the observed mismatch between neuronal recordings and fMRI reveals a real discrepancy (see Arbuckle et al., 2020), a function of the low reliability of the SPLa RDM (as discussed), or the mismatch in location. To improve this analysis, I would be happy to provide an RD from a more tightly matched ROI from the Ejaz et al., (2015) data, if needed.

Reviewer #2 (Recommendations for the authors):

Suggestions:

1) As described in the public review, the claim that motor representations are preserved after paralysis needs to be revised and described with more nuance to reflect the complex results that were presented in the manuscript. These revisions should be made to the title and throughout the discussion.

2) The third hypothesis (that pre-injury motor representations could have de-specialized) references Figure 2C, but that same figure panel was referenced for the second hypothesis (that the PC-IP representation would match that from SPLa in the imaging studies). It seems that the third hypothesis is not represented in Figure 2 so it should be added.

3) In figure 3a, it does appear that the single unit model became slightly less similar to the M1 model over time and in Figure 3c, the MDS plot suggests that the activity associated with each finger became slightly more variable (larger standard deviation) in the later sessions. While not a dramatic effect, could this be indicative of learning? The BCI performance should be shown for each session. Was there any trend in the overall success rate or error pattern over time?

4) The somatotopic model fit appeared to be stronger (in terms of model coefficient) than the muscle or usage model. Is this surprising given the interpretation that the somatotopic representation is primarily driven by sensory feedback, and this is a covert task. Might one expect the feedforward efferent signal to be stronger? Further, the discussion mentions that there is no topography in PPC, These seem to be in conflict. This may require a more nuanced discussion of the limitations of fMRI temporal resolution that may impact the ability to measure a consistent pattern. Further, the authors reference a previous study, Chivukula et al., as evidence of touch representations in PPC.

5) The discussion about limitations in the learning aspects of the study should be expanded as described in the weaknesses section of the public review. In addition, please comment on how the choice of the decoding window and features should impact the results given that there appears to be two temporally distinct representations measured in parietal cortex. Perhaps the participant converged on a strategy that was essentially a compromise between these two patterns, which both would have been included during the decoding window. Nevertheless, that no learning was observed in the current study is an important finding worthy of dissemination.

Reviewer #3 (Recommendations for the authors):

I'll avoid repeating concerns from the public review; most of those can be addressed by adding additional caveats or changing the introduction framing. As just one specific example, the manuscript would thus be substantially improved by appropriately narrowing the scope of claims. E.g., the last line of the Introduction would be only marginally longer, but would much better reflect the overall state of knowledge, if it were edited to say "Our results reveal that adult motor representations are preserved **in PPC** even after years without use".

Page 26 line 481: I really didn't understand this paragraph about estimating noise ceiling (and thus also I struggled to assess the claim that the model fit was "close to the theoretical maximum" on page 8 line 125). I understand at a high level what you're trying to do, but there are a lot of ways to estimate what even a perfect fit would look like given the single trial / spike measurement noise present. Can you explain the motivation/specific approach more (what do you mean by noise of the RDM?) and in more detail explain this calculation? Both more explanatory text, and adding the equations to Methods, would help. In general I found that the Methods could be more clear throughout and would recommend asking a colleague in a different systems neuroscience lab to read the Methods and explain what you did back to you (to reveal places where a reader would not be able to replicate the steps).

Page 26 line 491: Can you first briefly explain what the "directional hypothesis" is? Or else the reader would have had to read the Ejaz et al., methods to follow this section.

Can authors explain how hypothesis #1 (RSA structure matches natural statistics of use, as per ref 14) is distinct from hypothesis #2 (the BCI finger representation in PC-IP might instead match the representation of able-bodied individuals in the same brain area")? Couldn't #1 and #2 describe the same RSA structure (it seems that in fact they are highly correlated)? Was there past work showing they are different? Is there a reference to help unpack hypothesis #2? Right now hypothesis #1 vs #2 are really just illustrated by the two different RSA matrices in Figure 2b vs 2c, but that's asking the reader to squint and judge how different those matrices are. Some more hand-holding up front of where these hypotheses differ (and why) would help set the stage for this key question and result.

"In the first human BCI study of neural-population plasticity" (page 18, line 330) is a questionable claim (and unnecessarily provocative, in my view). For example, Wodlinger et al., (2015) examined BCI control of a robot arm over many sessions across ~250 days of use (Figure 5, and "showing that learning took place consistently over a long period of time") – this would seem to be an arm BCI learning study (asking, does neural activity change in a way that would lead to improved performance over time, by examining the decoder output which is, by definition, the task-relevant readout of the motor cortical population). That is not that different from how this study examines finger BCI learning. Another example is Eichenlaub, Jarosiewicz et al., (2020), which looked at learning-associated replay events in a BCI-controlled sequence task.

The page 18 line 331-332 sentence (about handwriting) also puzzled me: didn't that study explicitly find that yes, handwriting remains preserved through at least a decade of injury? Perhaps the present manuscript can be more specific about what future studies should ask about these complex motor skills
