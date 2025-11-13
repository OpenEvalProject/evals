# Neutrophil-mediated fibroblast-tumor cell il-6/stat-3 signaling underlies the association between neutrophil-to-lymphocyte ratio dynamics and chemotherapy response in localized pancreatic cancer: A hybrid clinical-preclinical study

## Authors

- Iago de Castro Silva<sup>1</sup> ([ORCID: 0000-0002-3898-6173](https://orcid.org/0000-0002-3898-6173))
- Anna Bianchi<sup>1</sup>
- Nilesh U Deshpande<sup>1</sup>
- Prateek Sharma<sup>1</sup>
- Siddharth Mehra<sup>1</sup>
- Vanessa Tonin Garrido<sup>1</sup>
- Shannon Jacqueline Saigh<sup>3</sup>
- Jonathan England<sup>4</sup>
- Peter Joel Hosein<sup>3</sup>
- Deukwoo Kwon<sup>6</sup>
- Nipun B Merchant<sup>1</sup>
- Jashodeep Datta<sup>1</sup> ([ORCID: 0000-0003-2869-1571](https://orcid.org/0000-0003-2869-1571)) †

### Affiliations

1. Department of Surgery, University of Miami Miller School of Medicine Miami United States ([ROR:02dgjyy92](https://ror.org/02dgjyy92))
2. Department of Surgery, University of Nebraska Medical Center Omaha United States ([ROR:00thqtb16](https://ror.org/00thqtb16))
3. Sylvester Comprehensive Cancer Center Miami United States ([ROR:0552r4b12](https://ror.org/0552r4b12))
4. Department of Pathology, University of Miami Miami United States ([ROR:02dgjyy92](https://ror.org/02dgjyy92))
5. Department of Medicine, University of Miami Miami United States ([ROR:02dgjyy92](https://ror.org/02dgjyy92))
6. Department of Public Health Sciences, The University of Texas Health Science Center at Houston Houston United States ([ROR:03gds6c39](https://ror.org/03gds6c39))

† Corresponding author

## Abstract

Background:Partial/complete pathologic response following neoadjuvant chemotherapy (NAC) in pancreatic cancer (PDAC) patients undergoing pancreatectomy is associated with improved survival. We sought to determine whether neutrophil-to-lymphocyte ratio (NLR) dynamics predict pathologic response following chemotherapy in PDAC, and if manipulating NLR impacts chemosensitivity in preclinical models and uncovers potential mechanistic underpinnings underlying these effects.Methods:Pathologic response in PDAC patients (n=94) undergoing NAC and pancreatectomy (7/2015-12/2019) was dichotomized as partial/complete or poor/absent. Bootstrap-validated multivariable models assessed associations between pre-chemotherapy NLR (%neutrophils÷%lymphocytes) or NLR dynamics during chemotherapy (ΔNLR = pre-surgery—pre-chemotherapy NLR) and pathologic response, disease-free survival (DFS), and overall survival (OS). To preclinically model effects of NLR attenuation on chemosensitivity, Ptf1aCre/+; KrasLSL-G12D/+;Tgfbr2flox/flox (PKT) mice and C57BL/6 mice orthotopically injected with KrasLSL-G12D/+;Trp53LSL-R172H/+;Pdx1Cre(KPC) cells were randomized to vehicle, gemcitabine/paclitaxel alone, and NLR-attenuating anti-Ly6G with/without gemcitabine/paclitaxel treatment.Results:In 94 PDAC patients undergoing NAC (median:4 months), pre-chemotherapy NLR (p<0.001) and ΔNLR attenuation during NAC (p=0.002) were independently associated with partial/complete pathologic response. An NLR score = pre-chemotherapy NLR+ΔNLR correlated with DFS (p=0.006) and OS (p=0.002). Upon preclinical modeling, combining NLR-attenuating anti-Ly6G treatment with gemcitabine/paclitaxel—compared with gemcitabine/paclitaxel or anti-Ly6G alone—not only significantly reduced tumor burden and metastatic outgrowth, but also augmented tumor-infiltrating CD107a+-degranulating CD8+ T-cells (p<0.01) while dampening inflammatory cancer-associated fibroblast (CAF) polarization (p=0.006) and chemoresistant IL-6/STAT-3 signaling in vivo. Neutrophil-derived IL-1β emerged as a novel mediator of stromal inflammation, inducing inflammatory CAF polarization and CAF-tumor cell IL-6/STAT-3 signaling in ex vivo co-cultures.Conclusions:Therapeutic strategies to mitigate neutrophil-CAF-tumor cell IL-1β/IL-6/STAT-3 signaling during NAC may improve pathologic responses and/or survival in PDAC.Funding:Supported by KL2 career development grant by Miami CTSI under NIH Award UL1TR002736, Stanley Glaser Foundation, American College of Surgeons Franklin Martin Career Development Award, and Association for Academic Surgery Joel J. Roslyn Faculty Award (to J. Datta); NIH R01 CA161976 (to N.B. Merchant); and NCI/NIH Award P30CA240139 (to J. Datta and N.B. Merchant).

## Introduction

Modern multi-agent chemotherapy delivered in the neoadjuvant setting for localized pancreatic ductal adenocarcinoma (PDAC) is an increasingly popular treatment sequencing strategy (Datta and Merchant, 2021). Our group has previously reported that major pathologic response following neoadjuvant chemotherapy (NAC) is associated with improved overall survival (Macedo et al., 2019). A major unmet need that remains is the discovery of biomarkers of pathologic response as well as subsequent disease trajectories in patients who undergo resection following NAC.

Neutrophil-to-lymphocyte ratio (NLR) has emerged as a promising biomarker in localized and advanced PDAC. Beyond its prognostic value in advanced unresectable disease (Iwai et al., 2020), recent evidence implicates the value of pre-surgery NLR in forecasting recurrence in patients undergoing upfront pancreatectomy (Nywening et al., 2018), as well as pre- and post-treatment NLR in predicting pathologic response following neoadjuvant chemoradiotherapy (Hasegawa et al., 2016; Kubo et al., 2019). However, the precise relationship between NLR dynamics during neoadjuvant treatment and pathologic response and/or survival in localized PDAC patients undergoing pancreatectomy has not been previously explored.

Emerging evidence implicates stromal inflammation in the PDAC tumor microenvironment (TME)—predominantly through inflammatory polarization of cancer-associated fibroblasts (iCAF) and CAF-derived secretion of IL-6 (Öhlund et al., 2017)—as a major driver of chemoresistance in PDAC (Hosein et al., 2020). Furthermore, prior work from our group has revealed that CAF-derived IL-6 engages in tumor-permissive crosstalk by activating STAT3 signaling within tumor cells (Nagathihalli et al., 2016), and that heightened CAF-tumor cell IL-6/STAT-3 signaling crosstalk is a central mediator of chemoresistance in PDAC (Dosch et al., 2021). As such, how tumor-permissive inflammatory cues such as neutrophil-lymphocyte balance intersect with such signaling mechanisms underlying therapeutic resistance in PDAC remains critically underexplored.

In a cohort of patients with operable PDAC undergoing modern multi-agent NAC, we sought to determine if NLR dynamics predict pathologic response following NAC in patients undergoing curative-intent pancreatectomy. We further investigated if pharmacologically modulating NLR dynamics in preclinical models of PDAC would impact chemosensitivity and uncover potential immunologic- and stromal-mediated mechanisms underlying these effects in vivo.

## Materials and methods

**Key resources table**


<table>
  <thead>
    <tr>
      <th>Reagent type (species) or resource</th>
      <th>Designation</th>
      <th>Source or reference</th>
      <th>Identifiers</th>
      <th>Additional information</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cell line (Mus musculus)</td>
      <td>Pancreatic Tumor Cells from KrasLSL-12D/+;Trp53R172H/+;Pdx1Cre (KPC) mouse</td>
      <td>Ben Stanger/UPenn</td>
      <td>KPC6694c2</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Mus musculus)</td>
      <td>Tumor associated fibroblasts from KPC mouse</td>
      <td>Nagathihalli et al., 2016</td>
      <td>KPC CAFs</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Ptf1aCre/+;KrasLSL-G12D/+;Tgfbr2flox/flox</td>
      <td>Datta et al., 2022</td>
      <td>PKT</td>
      <td>Genetically engineered mouse</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Ly6G (Rat monoclonal) reactive to mouse</td>
      <td>BioXcell</td>
      <td>Clone 1A8Catalog# BE0075-1</td>
      <td>25 μg/dose</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-IL-1β neutralizing antibody (E. coli, polyclonal)</td>
      <td>R&amp;D Systems</td>
      <td>Catalog# AF-401-NA</td>
      <td>1:80</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Cxcl1 (Rabbit, monoclonal) Reactive to human and mouse</td>
      <td>Abcam</td>
      <td>Catalog# ab86436</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Podoplanin (Mouse, monoclonal) Reactive to human</td>
      <td>Cell Signalling</td>
      <td>Catalog# 26981</td>
      <td>1:200</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Podoplanin (Syrian hamster, monoclonal) Reactive to mouse</td>
      <td>Abcam</td>
      <td>Catalog# ab92319</td>
      <td>1:200</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CD3 (170Er, Human, monoclonal) 3170019D</td>
      <td>Fluidigm</td>
      <td>3170019D</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CD11B (149Sm, Human, monoclonal)</td>
      <td>Fluidigm</td>
      <td>3149028D</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>α-SMA (141Pr, Human, monoclonal)</td>
      <td>Fluidigm</td>
      <td>314017D</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Pan-Cytokeratin (148Nd, Human, monoclonal)</td>
      <td>Fluidigm</td>
      <td>3148022D</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CD15 (164Dy, Human, monoclonal)</td>
      <td>Fluidigm</td>
      <td>3164001B</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CD8 (146Nd, Human, monoclonal)</td>
      <td>Fluidigm</td>
      <td>3146001B</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Anakinra</td>
      <td>SOBIPharmaceuticals</td>
      <td>α-IL-1R1 inhibitor</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Cxcl1 Primer - Mouse</td>
      <td>Qiagen</td>
      <td>Gene ID - QT00115647</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Il6 Primer - Mouse</td>
      <td>Qiagen</td>
      <td>Gene ID - QT00098875</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Cytokine array - Mouse</td>
      <td>R&amp;D Systems</td>
      <td>ARY006</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Clinical analysis

Patients with localized PDAC who received NAC with either mFOLFIRINOX, gemcitabine/abraxane, or both and underwent pancreatectomy between July 2015 and December 2019 at a tertiary academic center (n=101) were enrolled. Patients were excluded if annotated pathologic response information was unavailable (n=5) or if they underwent R2 resection (n=2; Figure 1A; Appendix 1—table 1). Pathologic response (PR) in resected specimens was dichotomized as ‘partial/complete’ or ‘poor/absent’ response based on established College of American Pathologists guidelines (Washington et al., 2010). For each patient, the proportion of neutrophils and lymphocytes were obtained from complete blood counts accrued at two timepoints—pre-NAC and pre-surgery (for details, see Appendix). NLR was defined as %neutrophils÷%lymphocytes. Both the absolute NLR prior to initiation of NAC (pre-NAC aNLR) as well as dynamic changes in NLR during NAC, defined as ΔNLR (=pre-surgery aNLR minus pre-NAC aNLR; Park et al., 2020), were correlated with PR. Multivariable models assessed the independent association of aNLR and ΔNLR metrics (dichotomized into high vs. low) with partial/complete PR. Area under receiver-operating curves (AUCs) were estimated for three models (aNLR only, ΔNLR only, combined aNLR+ΔNLR), internally validated using bootstrap logistic regression, and an ‘NLR score’ comprising product of regression coefficients and aNLR/ΔNLR ( = 10.45–2.9224*aNLR - 2.13*ΔNLR) was generated to stratify disease-free (DFS) and overall survival (OS) via Kaplan-Meier estimates. All tests were two-sided and statistical significance designated as p≤0.05.

![Figure 1.](https://cdn.elifesciences.org/articles/78921/elife-78921-fig1-v2.jpg)

**Figure 1.:** (A) STROBE diagram for selection of study-eligible patients with potentially operable pancreatic ductal adenocarcinoma undergoing neoadjuvant chemotherapy and curative-intent pancreatectomy, stratified by pathologic response; (B) Comparison of pre-chemotherapy absolute NLR (aNLR) between resected PDAC patients who demonstrated partial/complete pathologic response (n=66) and poor/absent pathologic response (n=28) following neoadjuvant chemotherapy. Median (IQR) values are plotted; (C) Waterfall plot depicting the delta-NLR (ΔNLR = pre-surgery NLR—pre-chemotherapy NLR) of all study-eligible patients, stratified by partial/complete (blue) or poor/absent (red) pathologic response. Dotted lines indicate median ΔNLR in each cohort, and adjoining p-value represents the comparison of these median values; (D) Forest plot showing predictors of pathologic response following NAC in a multivariable logistic regression model. Adjusted log odds ratios (ORs) and corresponding 95% confidence intervals are plotted on the x-axis; (E) Stratification of disease-free survival (top) and overall survival (bottom) by ‘NLR score’, calculated as the product of regression coefficients and aNLR/ΔNLR. The NLR score was dichotomized at ≤0 or>0 based on its efficiency at prognosticating DFS and OS. Number of patients at risk at each time point shown in adjoining tables.

### In vivo experiments

To recapitulate systemic NLR attenuation in preclinical models of PDAC, C57BL/6 mice orthotopically injected with 50x103 syngeneic KrasLSL-G12D/+;Trp53LSL-R172H/+;Pdx1Cre PDAC cells (KPC6694c2, provided by Ben Stanger/UPenn, mycoplasma negative) were treated with increasing doses of neutralizing anti-Ly6G antibody (BioXcell; 25 μg, 100 μg, 200 μg) to attenuate—but not deplete—circulating Ly6G+:CD3+ ratios for further experiments.

C57BL/6 mice were then orthotopically injected with 50x103 KPC6694c2 (henceforth KPC) cells and randomized into four groups starting 10 days after tumor inoculation (n=8–10/arm): vehicle control, NLR-attenuating anti-Ly6G alone (25 μg/dose) q3 days starting day 10, gemcitabine (100 mg/kg) and paclitaxel (10 mg/kg) once weekly starting day 14, and gemcitabine/paclitaxel treatment (day 14) following a ‘priming’ phase of anti-Ly6G attenuation starting day 10 (for details, see Appendix). Mice were sacrificed following 3 weeks of treatment, tumor burden and metastatic outgrowth evaluated, and tumor samples subjected to histological analysis, immunohistochemistry (Ly6G/Gr1, phosphorylated STAT3, cleaved caspase-1, and CD31), flow cytometric CAF and immune phenotyping, and enzyme-linked immunosorbent assay (ELISA; IL-6 and IL-1β; Park et al., 2020). A similar series of experiments were performed in Ptf1aCre/+;KrasLSL-G12D/+;Tgfbr2flox/flox (PKT) genetically engineered mice (Datta et al., 2022) to validate observations from the orthotopic KPC model (for details, see Appendix).

### Imaging mass cytometry (IMC) in human PDAC tumors

We retrieved FFPE blocks of 6 pre-treatment PDAC specimens from localized PDAC patients who underwent neoadjuvant chemotherapy and surgical resection, and stratified these post-hoc into partial/complete (n=3) or poor/absent (n=3) pathologic response. For detailed clinical annotation of these specimens, see Appendix 1—table 2. A board-certified GI pathologist selected regions of interest (ROI) from each slide comprising tumor cells, fibroblasts, and immune cells by correlating with corresponding H&E-stained sections. This slide was stained with an IMC panel of 10 metal-conjugated antibodies and a cell intercalator (Appendix). Prior to acquisition, Hyperion mass cytometry system (Fluidigm) was autotuned using a 3-element tuning slide and detection threshold of >700 mean duals of 175Lu was used according to manufacturer protocol. ROIs (1.8–3 mm2) were ablated and acquired at 200 Hz. Data were exported as MCD files and analyzed for single-cell segmentation analysis using Visiopharm software. For details, refer to Appendix.

### Ex vivo co-culture experiments

Tumor-infiltrating Ly6G+F4/80- neutrophils from orthotopic KPC tumor-bearing mice were isolated from fresh tumor suspensions using the Myeloid Derived Suppressor Cell Isolation Kit and QuadroMACS Separator (Miltenyi Biotech), and: (1) subjected to multiplex cytokine arrays using Proteome Profiler Mouse Cytokine Array Kit (R&D Systems, Minneapolis, MN); and (2) co-cultured with KPC CAFs with or without concurrent treatment with anti-IL-1β neutralizing antibody (Thermofisher, Waltham, MA) and IL-1R1 inhibitor Anakinra (SOBI Pharmaceuticals, Sweden). KPC tumor cells were incubated with conditioned media harvested from ex vivo co-cultures of intratumoral neutrophils and CAFs, either alone or with anti-IL-1β or anti-IL-6 neutralizing antibodies (Thermofisher, Waltham, MA), and ensuing protein lysates blotted for phosphorylated STAT-3 (pSTAT3). For complete details of all preclinical, in vivo, and in vitro experiments, see Appendix.

## Results

### NLR dynamics during NAC as biomarker of pathologic response and survival

Of 94 eligible patients (mean age 67, 58% female, 6% with germline homologous recombination deficiency genotype [BRCA2, n=5; PALB2, n=1]), 78% had borderline resectable or locally advanced disease. Patients received a median of 4 months of NAC (range 2–14), 52% received mFOLFIRINOX, and a minority of patients (6%) received neoadjuvant radiotherapy. Following NAC, partial/complete PR was achieved in 70% (66/94) while 28 patients (30%) demonstrated poor/absent PR (Appendix 1—table 1). Median pre-NAC aNLR was significantly lower in patients with partial/complete PR compared with poor/absent PR (2.53 vs 3.97; p<0.001) (Figure 1B). Moreover, a net attenuation in ΔNLR was observed in patients demonstrating partial/complete PR compared with a net increase in ΔNLR in poor/absent PR (median –0.38 vs. +0.21; p=0.01 respectively; Figure 1C). Of note, median aNLR or ΔNLR did not differ significantly between patients who received neoadjuvant mFOLFIRINOX vs. gemcitabine/nab-paclitaxel (3.00 vs 3.09, p=0.47; –0.02 to –0.25, p=0.16).

On multivariable modeling, higher aNLR (OR 0.02, 95% CI 0.003–0.15; p<0.001 [Ref: low aNLR]), higher ΔNLR (OR 0.06, 95% CI 0.01–0.33; p=0.002 [Ref: low ΔNLR]), and any %decline in CA19-9 during NAC (OR 1.82, 95% CI 0.001–3.74; p=0.05 [Ref: any %increase in CA19-9])—but not NAC duration, BMI, resectability status, or use of neoadjuvant radiotherapy—were independent predictors of achieving partial/complete PR following NAC (Figure 1D, Appendix 1—table 3). Bootstrap-validated AUC-derived analysis revealed that a combined NLR model encompassing both aNLR and ΔNLR most efficiently predicted PR with an AUC of 0.96 (Appendix 1—figure 1). This combined NLR model also effectively estimated bootstrap-validated time-dependent AUC for both DFS (2 year: 0.61, 95% CI 0.56–0.65) and OS (2 year: 0.60, 95% CI 0.55–0.67) in this cohort (Appendix 1—figure 2A–C).

At a median follow-up of 30 (IQR 7–49) months, 2 year and 5 year survival in this selected cohort of patients undergoing resection were 59% and 34%, respectively. An NLR score comprising the product of regression coefficients and aNLR/ΔNLR dichotomized at <0 and≥0 provided strongest discrimination of DFS and OS. Patients with an NLR score ≤0 demonstrated improved DFS (median 1.4 vs 0.7 years; p=0.006) and OS (median 3.6 vs 2.1 years; p=0.002) compared with patients with an NLR score >0 (Figure 1E).

### Attenuation of NLR potentiates chemosensitivity in murine PDAC

To model NLR attenuation in preclinical models of PDAC, treatment of orthotopic KPC tumor-bearing mice with neutrophil-attenuating 25 μg anti-Ly6G dosing achieved approximately 50% attenuation in circulating Ly6G+:CD3+ NLR ratio compared with vehicle treatment (Appendix 1—figure 3A); treatment with gemcitabine/paclitaxel, however, did not significantly decrease Ly6G+:CD3+ ratios (Appendix 1—figure 3B). While gemcitabine/paclitaxel treatment expectedly decreased PDAC tumor size compared with vehicle and anti-Ly6G alone treatments, concurrent treatment of tumor-bearing mice with gemcitabine/paclitaxel +anti-Ly6G further significantly decreased pancreatic tumor weight (Figure 2A) and metastatic outgrowth, graded by the presence of tumor deposits at six extra-pancreatic sites (Figure 2B). Importantly, mice treated with combination gemcitabine/paclitaxel +anti-Ly6G treatment did not incur additional systemic toxicity during treatment as measured by mouse weights (Appendix 1—figure 4A) and systemic ALT levels (Appendix 1—figure 4B).

![Figure 2.](https://cdn.elifesciences.org/articles/78921/elife-78921-fig2-v2.jpg)

**Figure 2.:** (A) Schematic of in vivo experimental design, illustrating treatment groups utilized (vehicle, anti-Ly6G [αLy6G] alone, gemcitabine/paclitaxel alone, and gemcitabine/paclitaxel+αLy6G), treatment timing, and schedules/regimens in KPC orthotopic model (top). Representative images (n=5 biologic replicates) from primary pancreatic tumors at endpoint analysis in each treatment group and adjoining histogram demonstrating differences in whole pancreas weights between treatment groups (n=8–10 mice/arm) at sacrifice are depicted (bottom); (B) Metastatic outgrowth in KPC orthotopic models of PDAC is graded by presence of tumor deposits at six extra-pancreatic sites; a representative example from a vehicle-treated mouse in these experiments is shown. Adjoining histogram depicts comparison of the frequency of extra-pancreatic metastatic involvement (values 1 through 6 for each mouse) across treatment groups (n=8–10 mice/group); (C) Representative images of tumor sections from each treatment group stained by H&E to demonstrate tumor area (all 20 x; scale bar = 50 μm), with high-magnification insets (40 x) indicating relevant areas on these representative sections. Slides from each treatment group were blinded, and %tumor area quantified by a board-certified pathologist (n=5 from each treatment group). This comparison is depicted in adjoining histogram; (D) Representative images of tumor sections stained for cleaved caspase-3 (CC-3) and CD31 from each treatment group (n=5; all 20 x; scale bar = 200 μm). Dotted circles and arrows represent areas of positive staining. Adjoining histograms show quantification of cleaved caspase-3 and CD31 staining across treatment groups (n=5 mice/group); (E) Representative images from primary pancreatic tumors at endpoint analysis in indicated treatment groups in the Ptf1aCre/+;KrasLS-L-G12D/+;Tgfbr2flox/flox (PKT) genetically engineered mouse (GEM) model. Adjoining histogram shows differences in whole pancreas weights between treatment groups (n=5 mice/arm) at sacrifice; (F) Representative images of tumor sections from indicated treatment groups in PKT GEM experiments stained by H&E to demonstrate tumor area (all 20 x, error bar = 20 μm), with comparisons between groups depicted in adjoining histogram. Arrows in the Gem/Pac+αLy6G group show non-malignant epithelial structures. All in vivo experiments were repeated once for reproducibility, and all data points represent biologic replicates. All between-group statistics represent multiple comparison testing using Tukey’s post-hoc instrument in one-way ANOVA.

Compared with gemcitabine/paclitaxel alone, NLR attenuation with anti-Ly6G improved chemosensitivity as evidenced by significantly decreased tumor area by H&E staining (p=0.01; Figure 2C) as well as increased cleaved caspase-3 and microvessel (CD31) density (Figure 2D) in gemcitabine/paclitaxel +anti-Ly6G treated mice compared with all other treatment groups.

To validate these observations in a spontaneous PDAC mouse model, we treated 4-week-old PKT mice with vehicle, gemcitabine/paclitaxel alone, and gemcitabine/paclitaxel plus anti-Ly6G combinations for 2 weeks. In this model as well, NLR attenuation with anti-Ly6G improved chemosensitivity vs. chemotherapy alone as evidenced by decreased primary tumor weights (p=004; Figure 2E) and tumor area by H&E staining (P=0.008; Figure 2F) at endpoint analysis.

### NLR attenuation during chemotherapy promotes anti-tumor adaptive immunity

In tumor-bearing animals, NLR attenuation significantly reduced—but did not abolish—circulating Ly6G+Ly6CdimF4/80- neutrophilic cells, although a compensatory increase in Ly6ChiLy6G-F4/80- monocytic cells was observed via flow cytometry from splenocyte-derived CD11b+ cells (Figure 3A). As expected, NLR attenuation—either alone or in combination with gemcitabine/paclitaxel—significantly decreased tumor-infiltrating Ly6G/Gr1+ neutrophilic myeloid derived suppressor cells in the PDAC TME (Figure 3B). Flow cytometric analysis revealed that treatment with gemcitabine/paclitaxel +anti-Ly6G significantly increased infiltration of both intratumoral CD4+ and CD8+ T-cells, as well as augmented antigen experience (PD-1+) and degranulating capacity (CD107a+) specifically in the CD8+ T-cell compartment (Figure 3C), compared with gemcitabine/paclitaxel alone, anti-Ly6G alone, or vehicle arms. Interestingly, increased infiltration in both CD4+ and CD8+ central memory (CD44+CD62L+CD103-), but not effector (CD44+CD62L-) or tissue-resident memory (CD44+CD62L-CD103+), T-cells were observed in gemcitabine/paclitaxel +anti-Ly6G-treated tumors compared with gemcitabine/paclitaxel alone, anti-Ly6G alone, or vehicle-treated tumors (Figure 3D).

![Figure 3.](https://cdn.elifesciences.org/articles/78921/elife-78921-fig3-v2.jpg)

**Figure 3.:** (A) viSNE maps depicting comparison of splenocyte-derived circulating Ly6G+ (left) and Ly6C+ (right) MDSCs gated within Cd11b+F4/80 cells in NLR-attenuating anti-Ly6G (25 μg) vs. vehicle-treated KPC orthotopic tumor-bearing mice (n=3 mice/arm). Asterisks representing p-values denoting comparisons between anti-Ly6G and vehicle treatment are indicated in the top right left of graph, and quantified in the adjacent histogram; (B) Representative images from orthotopic KPC tumor sections in each treatment group stained for Ly6G/Gr1 (all 20 x; scale bar = 200 μm). Ly6G/Gr1+ cells per field are quantified and depicted in the adjacent histogram. High-magnification insets (40 x) indicate relevant areas on these representative sections; (C) viSNE maps of total intratumoral CD4+ and CD8+ T-cells gated within CD45+/CD11b-/CD3+ T cells across treatment groups (top), and viSNE maps of PD-1+ and CD107a+ in total CD45+/CD11b-/CD3+ T-cells, stratified by CD4+ (black dotted outline) and CD8+ (grey dotted outline) T-cells by flow cytometry across treatment groups (bottom; n=8–10 mice/group). Asterisks representing p-values denoting comparisons between each treatment group and vehicle treatment are indicated in the bottom left of graph. Post-hoc Tukey analysis from one-way ANOVA comparisons between treatment groups for each cell subset are shown in adjoining histograms; (D) Violin plots depicting the number of intratumoral effector memory (CD44+CD62L-), central memory (CD44+CD62L+CD103-), and tissue-resident memory (CD44+CD62L-CD103+) cells in CD4+ (left) and CD8+ (right) T-cell compartments across the four treatment arms (n=8–10 mice/group). All experiments were repeated once for reproducibility, and all data points represent biologic replicates; *, p<0.05; **, p<0.01; ***, p<0.001.

### NLR attenuation during chemotherapy reprograms inflammatory CAF polarization in the PDAC TME

Prior work from our group and others have revealed that inflammatory CAF (iCAF)-derived IL-6 engages in tumor-permissive crosstalk by activating STAT3 signaling with tumor cells (Nagathihalli et al., 2016), and that the CAF-tumor cell IL-6/STAT-3 signaling axis is a central mediator of chemoresistance in PDAC (Hosein et al., 2020; Dosch et al., 2021). Therefore, we investigated if NLR attenuation during chemotherapy improves chemosensitivity by reprogramming iCAF skewness and dampening IL-6/STAT-3 signaling in the TME. Compared with vehicle treatment, concurrent treatment with gemcitabine/paclitaxel +anti-Ly6G (P=0.006)—but not anti-Ly6G alone (p=0.12) or gemcitabine/paclitaxel alone (p=0.49) treatment—significantly reduced iCAF (CD45-CD31-PDPN+Ly6C+ MHCII-):myofibroblastic CAF (myCAF; CD45-CD31-PDPN+Ly6C-MHCII-) cellular ratios in vivo (Figure 4A; Appendix 1—figure 5A). Furthermore, leveraging the near-exclusive expression of PDPN/Pdpn in human and murine PDAC-associated CAFs via scRNAseq (Datta et al., 2022; Steele et al., 2020) (5B&C) and widespread use of PDPN as a pan-CAF marker in multiple PDAC-related studies (Dominguez et al., 2020; Steele et al., 2021; Elyada et al., 2019; Biffi et al., 2019; Neuzillet et al., 2019), we observed significant reduction in co-expressing PDPN+CXCL1+ stromal cells—presumed iCAFs—in tumors from PKT genetically engineered mice treated with gemcitabine/paclitaxel +anti-Ly6G compared with gemcitabine/paclitaxel alone (p=0.02; Figure 4B), validating findings from the KPC orthotopic model.

![Figure 4.](https://cdn.elifesciences.org/articles/78921/elife-78921-fig4-v2.jpg)

**Figure 4.:** (A) Representative contour plots of CD45-CD31-PDPN+ cancer-associated fibroblasts (CAF) gated on Ly6C and MHC-II across vehicle, NLR-attenuating αLy6G, gemcitabine plus paclitaxel (Gem/Pac) alone, and Gem/Pac+ αLy6G treatment groups in orthotopic KPC tumor-bearing mice (n=8–10 mice/group) based on percentages of parental cell populations. Inflammatory (iCAF: Ly6C+MHC-II-), myofibroblastic (myCAF: Ly6C-MHC-II-) and antigen-presenting (apCAF: Ly6C-MHC-II+) sub-populations are indicated in their respective quadrants. Relative ratios of iCAF/myCAF subsets are quantified in adjacent box-and-whisker plots across treatment groups; (B) Immunofluorescent staining for Pdpn (marking CAF), Cxcl1, and merged images (all 20 x; scale bar = 20 μm) from representative tumor sections in PKT mice treated with vehicle, Gem/Pac and Gem/Pac + αLy6G (n=5 mice/arm). Arrows indicate regions with co-localized stromal Pdpn and Cxcl1 staining, with adjacent histogram quantifying % area per section from each biologic replicate with co-localized stromal Pdpn and Cxcl1 staining; (C) Schematic representation of imaging mass cytometry (IMC) workflow to provide spatially resolved single-cell phenotypes of human PDAC tumors derived from pre-treatment specimens which underwent neoadjuvant chemotherapy and ultimately demonstrated partial/complete or poor/absent pathologic response (n=3 each); (D) Single-cell segmentation of CD11b+CD15+ neutrophils and CD3+CD8+ T-cells mapped onto representative tissue section from tumors showing poor/absent and partial/complete response, with epithelial (PanCK) and stromal (α-SMA) territories also shown. Adjacent violin plot (top) quantifies tissue-level neutrophil-to-lymphocyte (NLR) across three tumors in each group, calculated as #CD11b+CD15+÷ #CD3+CD8+ cells (normalized to 5000 total single cells), while histogram (bottom) tabulates mean pixel intensity of α-SMA expression in stromal cells across three tumors each in partial/complete vs. poor/absent responder cohorts; (E) Immunofluorescent staining for PDPN (marking CAF), CXCL1, and merged images (all 20 x) in representative sections from the same tumors shown in (D) stratified by poor/absent vs. partial/complete response. White arrows indicate regions with co-localized stromal PDPN and CXCL1 staining, with adjacent histogram quantifying % area with co-localized stromal PDPN and CXCL1 staining. For the latter comparison, three separate sections from each biologic replicate (n=9 total sections) were used for latter comparison; (F) Quantification of IL-6 ELISA (pg/ml) from whole tumor protein lysates across vehicle, αLy6G-treated, gemcitabine +paclitaxel (Gem/Pac) alone-treated, and Gem/Pac+αLy6G-treated orthotopic KPC tumor-bearing mice (n=8–10 mice/group); (G) Representative images from tumor sections in each treatment group (n=5 mice/group) stained for phospoSTAT3 (all 20 x; scale bar = 200 μm), and adjacent bar graph showing quantification of % positive area of pSTAT3 in the epithelial compartment per field. All between-group statistics represent multiple comparison testing using Tukey’s post-hoc instrument in one-way ANOVA. When absolute p-values not provided: *, p<0.05; **, p<0.01.

### Reduced tissue-level NLR correlates with chemotherapy response, CAF density, and stromal inflammation at single-cell resolution in human PDAC

To examine the association between tissue-level NLR, stromal density/inflammation, and chemotherapy response (partial/complete [n=3], poor/absent [n=3]) in human PDAC tumors (Appendix 1—table 2) at single-cell resolution, pathologist-selected regions of interest (ROI) from each tumor section probed with metal ion-conjugated antibodies for pancytokeratin (PanCK:epithelial), α-smooth muscle actin (α-SMA:fibroblast), CD11b and CD15 (neutrophil), and CD3 and CD8 (T-cell) were laser-ablated, and atomized ions were acquired using time-of-flight mass cytometry (cyTOF) (Figure 4C). Image segmentation and quantification revealed significantly higher ratio of CD11b+CD15+ to CD3+CD8+ cells (NLR; normalized to 5000 total single cells) in pre-treatment tumors from PDAC patients who demonstrated poor/absent pathologic response compared with partial/complete response (15.8±2.8 vs 7.4±3.9; p=0.039) following neoadjuvant chemotherapy (Figure 4D). Interestingly, increased NLR in patients with poor/absent pathologic response correlated with significantly higher mean intensity of α-SMA expression (41.9±26.6 vs 18.4±16.6 pixels/cell; p<0.001) in—but not absolute density of—cancer associated fibroblasts in tumor ROIs (Figure 4D), as well as relative abundance of co-expressed PDPN+CXCL1+ iCAF populations in corresponding tumor sections (29.7 ± 8.8% vs 18.4 ± 7.4% tumor area; p<0.001; Figure 4E).

### NLR attenuation during chemotherapy dampens L-6/STAT-3 signaling in the PDAC TME

The reprogramming of iCAF polarization following NLR attenuation during chemotherapy in the preclinical models was reflected in decreased intratumoral IL-6 and CXCL-1 (data not shown) levels following treatment with gemcitabine/paclitaxel +anti-Ly6G (p=0.0002), but not anti-Ly6G alone (p=0.06) or gemcitabine/paclitaxel alone (p=0.08) treatment, compared to vehicle treatment (Figure 4F). In parallel with these findings, compared with vehicle, anti-Ly6G alone, or gemcitabine/paclitaxel alone, gemcitabine/paclitaxel +anti-Ly6G treatment resulted in significantly lower pSTAT3 expression in the tumor cell/epithelial compartment in vivo (p<0.01; Figure 4G).

### Neutrophil-derived IL-1β induces pancreatic CAF-tumor cell IL-6/STAT-3 signaling

To explore a mechanistic link between tumor-infiltrating neutrophils and iCAF-mediated IL-6/STAT-3 signaling in the PDAC TME, we characterized the secretome of tumor-infiltrating Ly6G+F4/80- neutrophils isolated from orthotopic KPC tumors, revealing IL-1β as the most robustly secreted cytokine (Figure 5A). Systemic NLR attenuation with anti-Ly6G treatment—with or without chemotherapy—resulted in significant diminution of IL-1β secretion in tumor lysates compared with vehicle or chemotherapy treatment in vivo (ANOVA p<0.001; Figure 5B), likely due to its incident reduction in systemic and tumor-infiltrating Ly6G+ cells (see Figure 3).

![Figure 5.](https://cdn.elifesciences.org/articles/78921/elife-78921-fig5-v2.jpg)

**Figure 5.:** (A) Bubble plot representing multiplex cytokine array performed on condition media from column-sorted Ly6G+F4/80- neutrophils (24-hr culture) derived from whole pancreata of KPC orthotopic mice. The chemiluminescent intensity of the six most robustly expressed cytokines is quantified as mean pixel density; (B) Quantification of IL-1β ELISA (pg/ml) from whole tumor protein lysates from vehicle, NLR-attenuating αLy6G, gemcitabine plus paclitaxel (Gem/Pac) alone, and Gem/Pac+ αLy6G treatment groups in orthotopic KPC tumor-bearing mice (n=9 mice/group); (C–D) Schematic of experimental design illustrating ex vivo co-culture of KPC CAFs with intratumoral column-sorted Ly6G+F4/80 cells from whole pancreata of KPC orthotopic mice, with or without pre-treatment of CAFs with anakinra (α-IL1R1 antibody) or pre-treatment of neutrophils with α-IL-1β neutralizing antibody (left); (C) qPCR analysis representing relative fold change in Il6 gene expression, and (D) quantification of IL-6 ELISA (pg/ml) from conditioned media collected from co-culture conditions comparing CAFs alone with CAFs co-cultured with intra-tumoral neutrophils with or without anakinra or α-IL-1β antibody pre-treatment. Results show mean ± SEM of three biologic replicates; (E) Western blot analysis of pSTAT3Y705 and total STAT3 (tSTAT3) levels from KPC tumor cell lysates following incubation with conditioned media (CM) from ex vivo intratumoral neutrophil (NP)-CAF co-cultures, either alone or treated with anti-IL-1β or IL-6 neutralizing antibodies. All experiments were repeated once for reproducibility, and all data points represent biologic replicates. All between-group statistics represent multiple comparison testing using Tukey’s post-hoc instrument in one-way ANOVA; (F) Graphical summary of proposed neutrophil-CAF-tumor cell IL-1β/IL-6/STAT-3 signaling axis that underlies the associated between NLR dynamics and chemotherapy response in PDAC. When absolute p-values not provided: *, p≤0.05; **, p≤0.01; ***, p≤0.001.

Next, we ascertained if neutrophil-derived IL-1β was contributory to CAF-tumor cell IL-6/STAT-3 signaling. Ex vivo co-cultures of KPC CAFs with tumor-infiltrating Ly6G+F4/80- neutrophils derived from orthotopic tumor-bearing KPC mice induced a nearly 20-fold increase in CAF-intrinsic Il6 transcription (p<0.0001), which was significantly abrogated by either neutralization of IL-1β (p<0.0001) or by pre-incubation of CAFs with IL-1R1 inhibitor Anakinra (Nagathihalli et al., 2016; p<0.0001; Figure 5C). These results were validated by IL-6 ELISA, which demonstrated a dramatic increase in IL-6 secretion from CAF-neutrophil co-cultures, and was significantly rescued with either IL-1β or IL-1R1 inhibition (all p<0.0001; Figure 5D). Cxcl1 transcription in CAFs—another key iCAF marker—was similarly induced nearly 22-fold following co-culture with tumor-infiltrating neutrophils, and significantly abrogated with either IL-1β or IL-1R1 inhibition (all p<0.0001; Appendix 1—figure 6).

Finally, KPC tumor cells demonstrated significantly higher pSTAT3 expression when incubated with conditioned media (CM) from intratumoral neutrophil-CAF co-cultures alone compared with CM from neutrophil-CAF co-cultures treated with either anti-IL-1β or anti-IL-6 neutralizing antibodies (Figure 5E). Together, these data reveal a role for neutrophil-derived IL-1β in promoting iCAF polarization and inducing CAF-tumor cell IL-6/STAT3 signaling in the PDAC TME, which is a central mediator of chemoresistance (Figure 5F).

## Discussion

In selected patients with operable pancreatic cancer undergoing curative-intent pancreatectomy following modern chemotherapy, we identify for the first time that NLR dynamics during NAC correlate strongly with pathologic response, and an NLR score encompassing these dynamics is prognostic of disease-free and overall survival. While these novel findings warrant large-scale multi-institutional validation to strengthen and/or reconcile data from heterogeneous PDAC populations (Hasegawa et al., 2016; Kubo et al., 2019; Strong et al., 2022), the present data indicate that both baseline NLR and NLR dynamics may be promising metrics of response and overall disease trajectory in patients with localized PDAC, recapitulating evidence from other gastrointestinal cancers (Sato et al., 2012).

The relationship between systemic chemotherapy, ensuing cytotoxicity/tumor-cell death and its immune repercussions, neutrophil mobilization and trafficking, adaptive immune dysfunction, and clinical outcomes in solid tumors is complex (Banerjee et al., 2013). Notwithstanding, since systemic chemotherapy does not appear to impact tumor-infiltrating neutrophils (Nywening et al., 2018) or circulating NLR in our preclinical studies, these data also suggest that therapeutic strategies to attenuate NLR during NAC may improve pathologic response in operable PDAC.

While the etiologies underlying the attenuation of endogenous NLR in patients demonstrating decreasing ΔNLR during NAC in this study are undoubtedly complex and remain unclear, modeling this phenomenon in preclinical models suggests that a ‘priming’ phase in which the systemic NLR is actively dampened improves chemosensitivity and is associated with heightened adaptive anti-tumor immunity in the PDAC TME. In our preclinical modeling, attenuation of NLR immediately preceding and during gemcitabine/paclitaxel chemotherapy not only improved CD4+ T-helper and CD8+ T-effector cell trafficking, but also amplified CD4+/CD8+ central memory skewness as well as CD8+ T-cell antigen experience and degranulating capacity. Our data add nuance to previous findings indicating that depletion of Ly6G+ neutrophilic myeloid-derived suppressor cells unmasks adaptive immunity (Stromnes et al., 2014), or that ablation of CXCR2+ tumor-associated neutrophils augments IFN-γ+CD8+ T-cell infiltration to potentiate FOLFIRINOX responses in PDAC models (Nywening et al., 2018). Given that systemic neutrophilic silencing is not only clinically impractical, but also drives a compensatory and dynamic myelopoiesis (e.g. of CCR2+ macrophages) that thwarts anti-tumor immunity (Nywening et al., 2018), the chemosensitizing and immune-potentiating effects of NLR attenuation in our model may be related to the disruption of specific tolerogenic functions inherent to tumor-associated neutrophils. Indeed, ongoing investigation in our laboratory is focused on deciphering and targeting neutrophil-intrinsic tolerogenic mechanisms that orchestrate immunosuppressive tumor-stromal-immune crosstalk and promote therapeutic resistance in PDAC.

One such potential mechanism governing therapeutic resistance unveiled in the present study is the previously unrecognized role of neutrophil-derived IL-1β in driving iCAF polarization and CAF-tumor cell IL-6/STAT-3 signaling in the PDAC TME. As such, the improved chemosensitivity associated with NLR attenuation in our preclinical models suggest that combining chemotherapy with therapeutic strategies to mitigate neutrophil-stromal-tumor cell IL-1β/IL-6/STAT-3 signaling in PDAC patients may be advantageous. Results from the Precision PromiseSM trial investigating anti-IL-1β antagonism in combination with gemcitabine/nab-paclitaxel and PD-1 inhibition in patients with advanced PDAC (NCT04581343) are eagerly awaited. Ultimately, decoding the intersection between NLR dynamics, the balance between tumor-permissive inflammation and anti-tumor adaptive immunity, and tumor-stromal-immune cellular crosstalk that perpetuates chemoresistant signaling circuitries in PDAC may lay the foundation for novel interventions to overcome chemotherapy resistance and improve contemporary outcomes in this lethal malignancy.

### Grant support

Supported by KL2 career development grant by Miami CTSI under NIH Award UL1TR002736, Stanley Glaser Foundation, American College of Surgeons Franklin Martin Career Development Award, and Association for Academic Surgery Joel J. Roslyn Faculty Award (to J. Datta); NIH R01 CA161976 (to N.B. Merchant); and NCI/NIH Award P30CA240139 (to J. Datta and N.B. Merchant).
