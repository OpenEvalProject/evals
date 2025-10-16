# Peer review - Round 1

Editors:
- Rachel Perry, Yale United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69456.sa1](https://doi.org/10.7554/eLife.69456.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper will be of interest to clinicians who provide care for persons with diabetes, educators who prepare these clinicians, as well as persons with diabetes who wish to be proactive participants in their own care. The calculation for an adjusted Hemoglobin A1c proposed by the authors can correct for individual red blood cell lifespan variations that can lead to misrepresentation of glycemic control. With the addition of a data-driven comparison to other means of assessing glycemic control, the adjusted HbA1c has the potential to improve care and subsequently decrease morbidity and mortality for persons with diabetes.

Decision letter after peer review:

Thank you for submitting your article "HbA1c and Red Blood Cell Lifespan: Addressing shortfalls of the laboratory measure" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Nancy Carrasco as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Agnieszka Szadkowska (Reviewer #2); Masashi Kameyama (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) A more complete description of the derivation of the model – more detail is required as to how the computations were done.

2) A comparison to other methods of assessing glycemic control (CGM, A1c). While assessment of how the authors' model predicts complications will not be required, a comparison (or at the very least, detailed discussion) of how it can compare to standard means of assessing glycemic control is necessary.Reviewer #1:

The strengths of this paper include that it builds on previous research and its sample size. However, the calculation for the individual RBC turnover rate, k age, is not included. The calculation for the adjusted HbA1c is too unwieldy for the clinician to use in practice where there is increased pressure to see many patients on a timely basis. If a "calculator" could be formulated allowing the clinician to plug in the relevant values and get the adjusted HbA1c, this could be widely used to improve patient care at the point of care which is the ultimate goal of this research.

The author's claims of a proposed adjusted HbA1c which is more accurate in predicting adverse outcomes due to diabetes is supported by the data.

There is a model to estimate RBC lifespan using reticulocyte count: Brodsky, R. A. Diagnosis of hemolytic anemia in the adult. In J. S. Timauer (Ed.) UpToDate, Retrieved February 17, 2020 from https://www.uptodate.com/contents/diagnosis-of-hemolytic-anemia-in-the-adult?search=hemolytic%20anemia&source=search_result&selectedTitle=1~150&usage_type=default&display_rank=1.Reviewer #2:

Laboratory HbA1c values are routinely used to assess glycemic control, but differences in red blood cell lifespan can affect hemoglobin glycation and HbA1c values. The authors developed a formula for adjusted HbA1c to account for red blood cell lifespan, which would better represent hemoglobin glycation and thus could better estimate the risk of disease complications.

The authors based their formula for aHbA1c calculation on laboratory measurements of HbA1c and CGM data performed with FreeStyle Libre. When using CGM systems, we often see falsified results for the duration of hypoglycemia, especially at night, due to sensor compression. The authors did not address these technical problems that may affect the aHbA1c result.

Using CGM we now have simple parameters to assess metabolic control of diabetes on the basis of CGM: TIR, GMI, CV. What I miss is a comparative analysis between these parameters and aHbA1c to convince readers that aHbA1c will be a better parameter for long term assessment for risk of complications.

The authors achieved their goal, and the results support their conclusions.

The use of aHbA1c in daily practice can be difficult because usually the clinician wants a ready result, but for research purposes, especially in patients with shorter red blood cell lifespans, it could be useful.

It will be interesting to see if its usefulness in estimating the risk of complications will be greater than TIR or GMI with CV.

Some comments on the methods and results:

Methods:

1. The study is based on CGM performed with FreeStyle Libre. From experience, we know that patients often have false hypoglycemia at night due to compression of the sensor. Has this been taken into account in the analysis?

2. Currently we use TIR and GMI to assess metabolic control in CGM users. Since aHbA1c, a new parameter will require additional calculations from me as a clinician, does it have advantages over these parameters in assessing the risk of chronic complications. It may be worth doing additional analysis comparing aHbA1c with these parameters.

3. As this is proof of concept, the details of creating the equation should be described, probably in some supplement. In addition, the idea behind the mathematical formula might help explain the equation to the readers. Secondly, the equation presented here is not clear in terms of units, and additionally operates slightly differently than the one in executed in provided excel file. The units for HbA1c here must be better emphasized. For example, if we assume HbA1c 9%, HbA1c in the numerator is treated as is (9%, % as a unit is preserved), but HbA1cs in the denominator have their units dropped (changed from 9% to 0.09). In parallel, the formula in excel does the same but multiplies the nominator by 100 (9% -> 900 %) and leaves HbA1cs in the denominator as is (and 1 becomes 100%). This creates some confusion and should be better explained, or an example calculation could be shown.

Results:

1. I think, that any characteristics of this group in needed. They come from already-reported cohorts but this is only a subgroup, so some basic clinical characteristics (if available) would be welcome.

2. Ad Figure 2 May be it should be consider adding a scatter plot showing individual patients or HbA1c measurements. Or, for simplicity, mark how many patients (N, %) had their HbA1c adjusted by up to 1, 1-2, 2-3 and >3%. This will provide a good estimate as to the range of applicability of your equation.

Reviewer #3:

The authors tried to adjust HbA1c to remove influence of erythrocyte lifespan. I admit the need for the adjustment, however, the study seems to lack the confirmation of their method.

1. The authors did not confirm the usefulness of their aHbA1c. The best way may be to confirm future diabetes complications as they mentioned, but it takes many years. I recommend to compare aHbA1c and average glucose derived by CGM.

2. The method requires complicated calculation from CGM data. I am not sure if the method is better than the simple average glucose derived CGM. Maybe, the kinetic method does not require steady state.

3. The value of kgly was not stabilized; from 4.04E-6 to 9.95E-6. kgly is a constant of non-enzymic process. It was estimated to be 6-10E-6, but the most recent one was 7.0E-6 (Kameyama et al. 2021). The average value of 5.86E-6 is smaller than the previously estimated value. I think that this instability is attributable to the nature of the calculation asking both kgly and kage.

4. The value of HbA1c should be converted to IFCC value.

"While the National Glycohemoglobin Standardization Program (NGSP) is used to express HbA1c in many clinical research and medical care settings, NGSP is measured by an old standardized method and at the time of conception, HPLC was not able to distinguish true HbA1c from other products. HPLC technology later advanced, however the derived HbA1c value is adjusted to NGSP in the interest of consistency. IFCC provides a strict definition of iA1c as hemoglobin with a glycated valine in the N-terminal β-chain. Thus, iA1c value is preferred value for estimation of hemoglobin glycation." (Kameyama et al., 2021)

5. The authors chose random destruction model of erythrocytes, however "unlike some other species including mice, all normal human RBCs have about the same lifespan and thus exhibit non-random removal ( Franco, 2009 )." Kameyama et al., (2018) provided erythrocyte model based on Γ-distribution by Shrestha et al., (2016). Program Modification from random destruction model to the uniform distribution of RBC ages model (Γmodel requires 2 parameters, so model that every RBC dies at the same age would be better to program) may be troublesome, but I think it is worth.

6. Equation 1 needs the derivation. i.e. d HbA1c/dt = 0; -kage HbA1c + kgly AG(1-HbA1c) = 0, -kageref HbA1c + kgly AG(1-HbA1c) = 0

Kameyama M, et al., Estimation of the hemoglobin glycation rate constant. Sci Rep. 2021 Jan 13;11(1):986. doi: 10.1038/s41598-020-80024-7.

Franco RS. The measurement and importance of red cell survival. Am J Hematol. 2009 Feb;84(2):109-14. doi: 10.1002/ajh.21298.

Kameyama M, Takeuchi S, Ishii S. Steady-state relationship between average glucose, HbA1c and RBC lifespan. J Theor Biol. 2018 Jun 14;447:111-117. doi: 10.1016/j.jtbi.2018.03.023.

Shrestha RP et al. Models for the red blood cell lifespan. J Pharmacokinet Pharmacodyn. 2016 Jun;43(3):259-74. doi: 10.1007/s10928-016-9470-4.

I think that the merit of the author's method is to obtain the erythrocyte lifespan. It would be interesting to compare mean erythrocyte age by Kameyama's equation (Mrbc = HbA1c / ((1-(2/3)HbA1c)kg AG)) and kage.
