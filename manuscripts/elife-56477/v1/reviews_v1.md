# Peer review - Round 1

Editors:
- Thorsten Kahnt, Northwestern University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56477.sa1](https://doi.org/10.7554/eLife.56477.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

How individuals convert private mental states into context-dependent public reports is an important but open question. This study tackles this issue in an elegant and novel way, using functional imaging and perceptual reports as an example. The results show that lateral frontal pole supports the mapping of private information to public reports, providing novel insights into the brain areas supporting social behavior.

Decision letter after peer review:

Thank you for submitting your article "Private-public mappings in human prefrontal cortex" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Michael Frank as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Steve W C Chang (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. In recognition of the fact that revisions may take longer than the two months we typically allow, until the research enterprise restarts in full, we will give authors as much time as they need to submit revised manuscripts.

Summary:

This study examines context-dependent mapping from "private" to "public" confidence in the human brain using combined univariate and multivariate approaches to fMRI data. The authors used a social perceptual decision task with 4x4 factorial design, which enabled the separation of an internal sense of confidence from an explicit public report. The authors found that subjects considered the social context for making their public confidence ratings. Imaging data was analyzed in medial-lateral divisions of the prefrontal cortex, motivated by previous studies. Univariate fMRI analyses show that pgACC and dACC tracked the formation of an internal sense of confidence, while FPl is involved in mapping it to a public report that reflects the contextual requirement. Finally, multivariate analysis using RSA further support the idea that FPI is involved in contextualizing private confidence by carrying a representation of different state conditions in the task space.

How the brain translates private information into the public domain is an important question, and all reviewers agreed that this study makes an important contribution to this topic. There were also a number of concerns that the authors should address in a revised version of this manuscript.

Essential revisions:

1) There were multiple comments regarding the analyses and results surrounding Figures 3 and 4. These need to be clarified.

1.1) The choice of modeling BOLD for Figure 3 only when the player was revealed seems arbitrary. Other studies looking at "internal" confidence ratings have typically looked at neural signals locked on the type I response onset. Please report the results of modeling BOLD at the response onset of the private and public decision with the same parametric regressors.

1.2) Relatedly, why does pgACC and dACC track the formation of an internal sense of confidence (although each showed the response profile of encoding different measures of it) only after being presented with the social context, but not at the time of making an individual decision (no effects of private confidence seemed to be present before the revelation of the context in Figure 4B)? Is this what the authors expected or is this driven by not having any task marker associated with the time when subjects internally decided on a response?

1.3) The authors report areas that track subjective confidence as well as those that may be involved in private-to-public mapping, but it is unclear which (if any) areas tracks the variable that is ultimately being reported? Figure 4 suggests that dACC activity would be a good candidate. Does dACC correlate with publicly reported confidence (more so than subjective confidence) if an analytical approach akin to Figure 3 is used?

1.4) For all parametric fMRI analyses in Figure 3, please compare the goodness of fit between the linear and quadratic models, to assess the necessity of adding a quadratic expansion. For the conclusions to be warranted, a quadratic term should improve goodness of fit in FPI but not other regions.

1.5) "an indicator of the degree of behavioral deviation from a default policy" – If this statement were true, shouldn't the connectivity between FPl and dACC correlate with the absolute value of the difference between private and public confidence, reflecting the same rationale for using the quadratic context term as parametric regressor?

1.6) There were no explanations for why there might be two significant time periods of PPI effects in Figure 4C. There are to two independent peaks, one right after the context revelation and the other, a more pronounced peak on average, occurring from 6 sec and 8 sec. Please explain these patterns, which are also seen even for the FPI-pgACC panel.

2) Reviewers wondered if the contrast between internal and explicit confidence is contaminated by the choice of time-locking event. That is, are the results really specific to private-to-public mapping, or do they rather reflect the sequential nature of this task, and comparable findings would be observed in a number of processes involving two different states? This question has implications for the novelty of the current study. That is, if the results are not specific for private-public mapping, as opposed to a serial stage, implicit-explicit, etc. type of processes, then the novelty of the neural data would decrease profoundly (e.g., the idea of internal processing to be more medially and external processing to be more laterally localized in the PFC has been around for quite some time).

3) Confidence model.

3.1) It would be important to add a description of the model leading to confidence estimates irrespective of context, as it seems rather mysterious in the present form. Regarding the analysis strategy, please compare this modeling approach with a simpler strategy, e.g., applying mixed-effects ordinal regression on confidence with perceptual evidence and context as fixed effects.

3.2) In order to make sure that the confidence model and its out-of-sample prediction of private confidence estimates are reliable, it would be necessary to validate the accuracy of the model within the data it fitted to. Please report cross-validation accuracy within the data from the behavioral session.

3.3) What is the correlation between motion coherence and the model-derived estimates of private confidence? It was unclear why dACC did not encode the linear term for coherence as in Figure 3C but did track the model-derived estimates of private confidence, although both are the indirect measures of private confidence. Please explain what each of these measures differentially represent with regards to the subject's private state. Also, it was not clear why dACC would only encode one of private confidence measures.

4) Reviewers were concerned that because the current study addresses a novel question with a novel approach and there was no pre-registration, that there was quite a bit of analytical freedom, for instance in the selection of ROIs, which might have biased results. To help mitigate these concerns, it would be important to (a) clearly state the a priori rational that went into the selection of ROIs, (b) fully report the results of the analyses regarding different time points (essential revision 1.1), and (c) show that the results of the ROI analyses converge with the whole-brain results. In this regard, please move the whole-brain univariate results to the main text and discuss it more thoroughly. For the RSA analysis, please conduct a searchlight to provide whole-brain results that can be compared with the ROI findings as well.

5) The manuscript does not contain any statistical results in the main text to support the claims. Some statistical thresholds are reported in the figure legends, but some figures (for instance Figures 4 and 5) do not contain any statistical information. Please include all statistical tests, t, f, and exact p-values in the main text.
