# Peer review - Round 1

Editors:
- Niel Hens, Hasselt University & University of Antwerp Belgium

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65297.sa0](https://doi.org/10.7554/eLife.65297.sa0)

In their work, the authors combine clinical data and mathematical modelling to shed light on the role of hepatocytes in HCV clearance. This manuscript will be of interest to clinicians in organ transplantation centers and to translational hepatitis virus researchers given that it provides a rare and carefully collected dataset of hepatitis C virus blood titers during and after liver transplantation. The manuscript is also of potential interest to modelers interested in HCV infection and more broadly infectious disease specialists.


---

# Peer review - Round 1

Editors:
- Niel Hens, Hasselt University & University of Antwerp Belgium

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65297.sa1](https://doi.org/10.7554/eLife.65297.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article “Modeling hepatitis C virus kinetics in vivo and in vitro reveals the role of hepatocytes in virus clearance“ for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Niel Hens as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Päivi Ojala as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Melanie Prague (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is “in revision at eLife“. Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

Using mathematical modeling applied to a precise collection of blood samples in 5 patients, Shekhtman et al. evaluate the kinetics of hepatitis C viral load during and after liver transplantation. The data suggest that anhepatic (absence of liver) and early post-reperfusion phases of liver transplantation do not have similar HCV clearance rates, and therefore that the liver plays a major role not only in HCV production but also in HCV clearance. It shows indeed, in a fraction of the patients, maintenance of unchanged viral load during the anhepatic phase followed by a prompt decrease of HCV RNA titers upon reperfusion of the new liver graft. This drop could not be attributed to the transfusion of blood products and dilution of the virus load. In fact, the authors report a biphasic decrease of the viral load early after liver reperfusion, with a first abrupt drop in viremia in the first 20 minutes, attributed to HCV uptake in the new liver, and a subsequent slower decline in viral titers in the next 6 hours, suggested to correspond to the physiological HCV clearance rate in absence of new virus production, and in adequation with previous estimates.

This study consolidates previous reports on HCV viremia during liver transplantation, with a limited number of patients (5) but more extensive and precise sampling. The hepatic clearance of HCV is not completely surprising given the high vascularization of the liver. Also, as the authors point out, similar findings were reported by Ganesan et al. for adenovirus clearance, although in this latter study the liver sinusoidal endothelial cells were involved. The study emphasizes the need to clear HCV before performing a liver transplantation in order to prevent the infection of the liver graft. The conceptual advance is limited by the lack of mechanistic study but the authors share a unique dataset. Furthermore, some parts of the manuscripts need to be clarified and the in vitro aspect of the study needs to be better controlled and deepened to support the authors' claims.

Essential revisions:

1) Mathematical model.

Motivation: A clear motivation for the use of the mathematical model as is presented now is missing. The logical flow is there but how did the authors arrive to this model and not to another model as such. The authors should also highlight the novelty of their model as compared to previously published models on the same question. The mathematical modelling resembles in some ways the models by Powers K et al. (PMID 16447184) and Neumann et al. (PMID 9756471). Adequate references should be included and novelties in the proposed model highlighted. They could also comment on the use of the complete body fluid volume rather than the blood volume in their mathematical model; it is not clear for the non-initiated reader whether the HCV titer is the same in the different body fluids and whether all are affected in the same way by the transfusions and blood losses during surgery.

Description: The equation used could be made more accessible for a broad range of readers by introducing more thoroughly the variables (e.g. please introduce V already for equation 1) and including the dimensional analysis for each equation (e.g. [L][T]-1, etc. do c and P correspond to HCV RNA concentrations produced per unit of time?). Please provide a clear description of how t1/2 is derived from Equations 3-4.

Statistical methodology:

a. The description of statistical methods for calibration and fitting is very poor. P5 last paragraph. How do parameters in Table 1-3 relate to equation 2-3-4? Which ”regression models“ did the author fit? Authors also mentioned that they fitted model from equation 4, please provide the method. Is it simple least mean square? Why did the author did not adopt a population fitting approach such as described in Guedj et al. 2013 (https://doi.org/10.1073/pnas.1203110110) using (for example) the Monolix software (R package saemix could also be relevant)?

b. In the result section, I am confused how section 1, 2 and 3 relate? Can you explain better what is the added value of ”Viral kinetics before and during the anhepatic phase“ and ”Viral kinetics after graft reperfusion“, when a clearer/deeper description of the results in the “Modeling HCV kinetics“ would probably carry the same information? Please clarify the analysis done (as e.g. fitting individual data) and present the parameter values (effect sizes in Table 2; please do not use a median based on decreasing slopes only) etc. To what extent is the model well specified and parameters identifiable? It is disturbing to change the model of analysis because of data (see example of patient 5) – i.e. conditioning the model structure on data observation. If the model is flexible enough, it should be possible to fit the data assuming some parameters such as c very large. Being able to keep the same dynamical model for all patients would help warranting its validity. I strongly believe that analyzing jointly all the observed course of trajectories (before AH, during AH and after RP) will have a strong added value.

2) The in vitro evidence is weak and lack controls. Because it relies on a hepatoma cell line rather than primary cells and does not include any other cell type as a comparison the depicted assay does not support a larger role of hepatocytes as compared to other liver or non-liver cell types in HCV uptake. Furthermore, controls are missing that should show the complete block in viral RNA secretion in this system. In particular, liver sinusoidal endothelial cells were proposed by Ganesan and colleagues as playing a major role in virus uptake in the liver, and the role of this cell type should be tested if the authors want to make a claim on the cell type responsible for the post-transfusion decline in HCV titers. Also, there seems to be a confusion between technical and biological replicates in this in vitro data.

The cell culture experiment does not seem valid to test the author´s hypothesis and more specifically quantify the role of hepatocytes, as indicated by the authors. Additional controls and details would be instructive.

a. Are the hepatoma cells confluent (can one exclude virus adsorption to the dish)? Is the control condition (absence of cells, Figure 4A) in a tube or a cell culture-coated dish?

b. Why using HCV-infected cells in Figure 4B? The authors mentioned they want to avoid any initial rapid binding and influx of HCV as expected if using Huh7 cells, but wouldn´t this in fact mimic the situation of the reperfusion of a naive liver graft? Why not incubating the virus stock used in A on different (non-infected) cell culture dishes: empty dish (control for virus / viral RNA adsorption to plastic dish) vs. dish containing confluent monolayers of different cell types (different hepatocyte-derived cells, other liver cell types, non-liver cells…). This would be much easier to interpret than the proposed assay, where it is not clear whether virus production is directly abrogated at t=0 post-treatment. The authors should test other liver cells and liver-unrelated cells since they propose that “hepatocytes in particular“ play a major role in circulating HCV clearance. Ideally, the authors should test primary human hepatocytes and LSECs in parallel.

c. The authors should verify that their inhibitors indeed completely block HCV RNA secretion in the conditions tested (for instance by performing a medium change in similarly infected wells at t=0, after which the virus titer in the supernatant should remain at 0 if HCV RNA secretion is blocked). This is unlikely the case, at least for Naringerin: according to Goldwasser et al. (PMID 21354229), 200 μm Naringerin merely decreased 4 fold HCV RNA secretion.

3) Other essential revisions:

– Blood transfusion, which is an important confounder in the in vivo study, is not sufficiently described and discussed. Can you comment on the relevance of accounting for other covariates (from Table 1 put also possibly the length of HCV infection, type of treatments…). I bet there may be a lack of power in the study but a discussion of possible confounder could be added.

– The authors should discuss the potential role of extrahepatic HCV reservoirs in their study.

– Magnitude of results between in vivo and in vitro study should be better described and compared.

– Can you clarify why you did not model phase D i.e. >4h post RP, see Figure 2?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled “Modeling hepatitis C virus kinetics during liver transplantation reveals the role of the liver in virus clearance“ for further consideration by eLife. Your revised article has been evaluated by Päivi Ojala (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Both reviewers have acknowledged the authors' efforts in providing a revision of their work addressing most of their comments raised. There is, however, some more work needed to clarify some outstanding issues.

Reviewer #2:

The validity of the approach still suffers from several pitfalls:

1. HCV cell culture systems are mostly limited to cancer cell lines and a particular HCV genotype, hence justifying the approach used by the authors. These systems have proven very useful to dissect HCV replication cycle, however, it is not clear whether they are helpful to support the specific authors conclusions. In particular, the virus genotype, lipoprotein coat and most importantly specific infectivity is different in the cell culture system and might affect HCV genome stability and uptake. Indeed, the authors quantify HCV RNA as a readout for HCV half time. This is coherent with the in vivo readout (where infectivity is difficult to assess) but this RNA might be in completely different forms in JFH1 HCVcc as compared to infected patient serum. In fact, Lindenbach and colleagues, PNAS 2006, reported a 100x lower specific infectivity for cell culture virus as compared to virus retrieved from animals. The relative proportions of subgenomic, naked, encapsidated, enveloped, lipoviroparticle-associated, exosome-associated viral RNA might be completely different from what is found in patient serum samples. On the other hand, the cancer cell lines in culture might behave differently than hepatocytes in clearing HCV genome, whether by uptake or RNase degradation inside or outside the cells. Would any other cancer cell line give the same clearance effect? If yes, how does it support the authors’ point: does the liver clear many viruses simply because it is very vascularized?

2. I agree that the definition of biological replicates is problematic and subject to interpretation in particular with cell lines. However, as stated in the authors’ response, biological replicates refer to “biologically distinct samples“. If I understood well, the “biological duplicates“ described in Figure 4 are replicate wells of the Huh7 cell line that were seeded, treated and infected in parallel, with the same cell passage, virus and inhibitor stocks, on the same day, which to me does not quality as biologically distinct samples, and the variation observed between these wells is mostly technical (as opposed to different mice in an animal experiment for instance). I therefore recommend removing “biological duplicate“ from the figure legend. Since the data shown is representative of 2 experiments, the conclusion would be stronger by averaging the 2 independent experiments.

Given the low impact of the cell culture experiment on the authors conclusions and its strong limitations, I recommend the authors significantly reinforce the in vitro evidence and discuss the remaining limitations more in detail (as discussed above and in the previous review: testing other cell types, checking infectivity in addition to genome copies, etc).

Reviewer #3:

Figure 1 could be made of 2 figures: 1/ the existing one 2/ a zoom in in the first few hours.
