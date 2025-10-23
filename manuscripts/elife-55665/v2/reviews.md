# Peer review - Round 1

Editors:
- Alejandro Sánchez Alvarado, Stowers Institute for Medical Research United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55665.sa1](https://doi.org/10.7554/eLife.55665.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

By coupling modeling with experimental data using FUCCI technology to visualize cell cycle dynamics in vivo, the authors demonstrate that spinal cord regeneration in the axolotl is likely to occur in response to a signal that recruits synchronously cycling ependymal cells shortly after injury. These data help elucidate important aspects of spinal cord regeneration.

Decision letter after peer review:

Thank you for submitting your article "Modeling the spatiotemporal control of cell cycle acceleration during axolotl spinal cord regeneration" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by Alejandro Sánchez Alvarado as the Reviewing Editor and Marianne Bronner as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Carsten Marr (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is 'in revision at eLife'. Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

E.Cura Costa et al. present a spatio-temporal modeling approach to describe cell cycle acceleration during Axolotl spinal cord regeneration. The model is based on previous in vivo observations and reveals spatial and temporal intracellular coordination with an optimal parameter set. The model is calibrated with experimental data and predicts that a signal that comes into play 24 hours post-amputation and recruits cells located within one millimeter anterior to the injury site could explain the spatiotemporal pattern of cell proliferation after injury. The model further allows assessing the individual contributions of S and G1 phase shortening required to explain the experimentally observed outgrowth dynamics. The idea and necessity of this model are nicely motivated by previous in vivo findings and are explained understandably along with the figures. The mathematical predictions could help to identify possible signals in spinal cord regeneration in the future. However, we think that the evidence for this model hypothesis is not convincing. In particular, other model hypotheses are not quantitatively rejected. In its current form, it simply says that a particular hypothesis about G1 and S phase changes fits the data, but many other models would probably do so as well. Experimental validation of the assumptions made and predictions of the model would make the paper stronger.

Essential revisions:

1. Model comparisons should be more rigorous.

– The comparison of different hypotheses in Figure 4 is only qualitative. No proper parameter fitting is involved.

– Parameter fitting should also consider the variance (not only the mean) of experimental measurements.

– We are not convinced that the outgrowth dynamics suffices to compare the different G1/S shortening hypotheses. Can you prove that these parameters are indeed identifiable?

2. The mathematical model is based on simplifying assumptions, i.e. the spinal cord is modeled as a row of rigid spheres representing the cells. Here, the question arises whether the quantitative values provided are indeed representative of the in vivo situation and will, therefore, have a significant impact on future studies on the mechanisms of spinal cord regeneration. So far, the existence of the proposed signal has only been evaluated through mathematical predictions but has not been confirmed experimentally.

3. How likely is the fact that a single signal as mathematically introduced here is actually the driving force for spinal cord regeneration? Couldn't it also be a combination of different factors?

4. It should be better emphasized which experimental data were used for fitting and which were used to validate the model. For instance, it seems like the experimental switchpoint data were used for fitting, while the agreement with experimental outgrowth in Sox2 knock-out axolotls can be regarded as a validation. Emphasizing how the model draws together different data sets will highlight the predictive power of the model and enhance the reader's trust in the model predictions.

5. The model assumptions are not always well-motivated.

– Why is the cell cycle normally distributed, giving in principle also rise to negative values? A log-normal or lag-exponential dist. would be more intuitive.

– Is 'we assumed that recruited cells whose cell cycle coordinates belong to G2 or M when t = τ will continue cycling as before' substantiated by the data? Why shouldn't all cells in the zone change their cell cycle? Or a random fraction? Can we rule out these possibilities with model comparison?

6. The optimal set of parameters is obtained through a brute-force sampling approach over a certain parameter domain and subsequent evaluation of least-squares. How sensitive are results with respect to the different parameters? How were the parameter domains and corresponding step sizes chosen? Without this information, it is difficult to judge the robustness of the results.

7. Predictions should be experimentally verified.

– Why not show the 1mm zone with e.g. BrdU staining (experiments seems to have been done already in Rodrigo Albors et al., 2015) or AxMLP staining?

– Is there evidence in the data that substantiates 'partial synchronization of cells transiting through G1'? This would be a strong indication that the assumed G1 mechanism is indeed in place.
