# Peer review - Round 1

Editors:
- Michael L Dustin, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83659.sa0](https://doi.org/10.7554/eLife.83659.sa0)

This work provides an important finding, that aspects of clinical outcomes can be predicted by a random search to an immunological synapse-based computational model for T cells directed by specific engagers. It provides solid evidence based on in vitro synapse formation measurements using imaging flow cytometry. The work will be of interest to investigators in the still-expanding immunotherapy field, and also as an example of how biologic drugs interface with endogenous cellular resources in a patient.’


---

# Peer review - Round 1

Editors:
- Michael L Dustin, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83659.sa1](https://doi.org/10.7554/eLife.83659.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Population Dynamics of Immunological Synapse Formation Induced by Bispecific T-cell Engagers Predict Clinical Pharmacodynamics and Treatment Resistance" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Michael L Dustin as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Xiling Jiang (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Cell adhesion molecules are regulated by TCR are not explicitly included in the model. Do the author feel that BITEs are not triggering these mechanisms or that their action is directly related to BiTE mediated interactions that are explicitly modelled such that the contributions of adhesion are included in the contributions of the BiTE interactions.

2. T cell movements in tissue is not a random walk, but is scaffolded by stromal cells and extracellular matrix to generate a variety of search strategies, which have been reported in the literature. Do any of the surprising results from the model potentially arise from known, non-Brownian aspects of T cell migration in tissues (or from aspects of cell adhesion in tissues that are not linear related to BiTE mediated interactions).

Reviewer #1 (Recommendations for the authors):

The authors use Jurkat-Raji combination for imaging flow cytometry. Jurkat is likely to use the CD2-CD58 adhesion system to engage Raji and this could be investigated with antibodies to CD2 or CD58. It is not clear to me how the simple use of blinatumomab bridge formation can correctly model the adhesion process. I suspect this works because the CD2-CD58 system is likely to be a constant and the frequency of blinatumomab Bridges is controlling signaling that promoted CD2-CD58 interaction to mediate conjugate formation and observed actin polymerisation. So the modelling may be correct in predicting the bell shape, but would not hold up if the physical requirements for synapse formation were correctly modelled. So the inclusion of CD2-CD58 and other adhesion systems may not change some aspects of the models, but it would provide another escape route for the tumour- through CD58 loss rather than CD19 loss.

Understanding the competition between adhesion and motility in the tumour may be important to understand the dissociation process. So chemokinesis may be an important thing to consider that may different in different settings. Due to chemokine like CXCL12 and CCL19/21 it may be very strong in lymphoid tissues, but bone marrow and other tissues may have very different landscapes of chemokine and thus the drive to disengage from a target may be lower or higher.

In terms of search models, the actual movement pattern will depend upon the underlying stroma. In a lymph node this network allows for frequent turns and exploration of the 3D space, where in some tumours the stroma may be more oriented and may convey T cells toward or away from the tumour. In the CNS, Lévy flight was found to be more efficient than a random walk would have been. Can this complexity explain any situation where the model predictions didn't hold?

Reviewer #2 (Recommendations for the authors):

1. What is the major purpose of modeling the immune synapse variants? Are they expected to have clinical significance (e.g., increase /decrease in efficacy, induce tumor antigen escape)?

2. In page 10 Figure 3, the incubation system was defined with X x 10E6 cells/mL, does this refer to total cell numbers (i.e., E + T cells), effector cells numbers or target cell numbers, please clarify in the figure legend for each respective experimental condition (e.g., Figure 3h and 3i, when you have different E:T ratios).

3. In page 10 Figure 3h, I would like recommend separation of effector cells and target cells, given that engagement of target cells is expected to be more clinically relevant.

4. In page 12 line 233, it was stated that "IS formation was optimized when the E:T ratio was around 1". Given that a lot of in vitro studies a conducted using E:T ratio 5:1 or 10:1, do you think your simulation results can be used to modify the in vitro study experimental condition towards better outcome?

5. Page 15 Figure 5c and 5d, do you have any observed data to verify the model simulated reduction in CD19 expression level following blinatumomab treatment?

6. Page 15 Figure 5e and 5f, one major concern for me is that your model simulation suggested that the bispecific is more effective in spleen and bone marrow compared to that in bone marrow, which generally against the clinical observation (e.g., the expected efficacious dose of blinatumomab for Acute Lymphoblastic Leukemia [major site of action is bone marrow] and Non-Hodgkin's Lymphoma [major site of action is lymph node] are 15 ug/m2/day vs. 60 ug/m2/day, respectively), and animal data (e.g., MGD-011 showed much strong B cell depletion effect in bone marrow compared to that in spleen and lymph node, PMID: 27663593). This may be associated with the heterogenous distribution of T cells and B cells in the lymph node and spleen (https://www.google.com/url?sa=iandurl=https%3A%2F%2Fimmunox.ucsf.edu%2Fsites%2Fimmunox.ucsf.edu%2Ffiles%2Fpdf%2FMicro204_Anat_IR%2520v2018.pdfandpsig=AOvVaw0qOMQka3SNN7k762B84FYDandust=1670808103053000andsource=imagesandcd=vfeandved=0CBAQjhxqFwoTCLC0za2z8PsCFQAAAAAdAAAAABAd). Please update your model simulation and associated context accordingly.

7. Page 17 Figure 6. Same issue as Figure 5e and 5f, with the model simulated regimen, we are not supposed to expect more B cell depletion in lymph node and spleen compared to that in bone marrow.

8. Page 20 Figure7. You may consider alternative regimens (e.g., high dose intensive treatment initially, followed by lower dose, less intensive treatment for consolidation) given that E:T ratio is expected to increase substantially following initial treatment.

9. Figure 5—figure supplement 3C. I'm not sure if the conclusion that "bidirectional effect was shown by increasing B cell density, owing to enhanced probability of cell-cell encounter and then insufficient BiTE concentration" hold true, given that for each individual B cell, the opportunity of encounter blinatumomab and T cells should be the same even at lower B cell concentrations.

10. Figure 4—figure supplement is missing

11. Given that you have 17 supplementary figures, please include a separate file where all the figures and the respective figure legends will be arranged together when you submit the revised article.

Reviewer #3 (Recommendations for the authors):

1. More details regarding the estimation of model parameters should be provided. Specifically, details of the type of the cost function used, confidence intervals, and the sensitivity of the in vivo dosage strategies to the chosen parameter values. It was not clear if a killing rate for tumors was used and whether it was estimated. Do the T cells proliferate/die in the in vivo model? A clear discussion of the data that were used to train the model (e.g., to estimate parameters) and test predictions should help.

2. It might help to further evaluate the importance of the cell population level interactions added in the model if one of the existing models in the literature was compared against the model developed here for describing the in vitro and in vivo experiments.

3. I think an experimental test of the surprising results in supplementary Figure 3a will substantially increase the confidence in the model.

4. It will help the readers to follow the model if model parameters were shown in the figures (e.g., Figure 5a).
