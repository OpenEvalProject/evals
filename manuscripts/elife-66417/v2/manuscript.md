# Adult stem cell-derived complete lung organoid models emulate lung disease in COVID-19

## Authors

- Courtney Tindle<sup>1</sup>
- MacKenzie Fuller<sup>1</sup> ([ORCID: 0000-0001-6781-8710](https://orcid.org/0000-0001-6781-8710))
- Ayden Fonseca<sup>1</sup>
- Sahar Taheri<sup>3</sup>
- Stella-Rita Ibeawuchi<sup>4</sup>
- Nathan Beutler<sup>5</sup>
- Gajanan Dattatray Katkar<sup>1</sup>
- Amanraj Claire<sup>1</sup>
- Vanessa Castillo<sup>1</sup> ([ORCID: 0000-0002-4182-8846](https://orcid.org/0000-0002-4182-8846))
- Moises Hernandez<sup>6</sup> ([ORCID: 0000-0002-7651-2673](https://orcid.org/0000-0002-7651-2673))
- Hana Russo<sup>4</sup>
- Jason Duran<sup>7</sup>
- Laura E Crotty Alexander<sup>8</sup> ([ORCID: 0000-0002-5091-2660](https://orcid.org/0000-0002-5091-2660))
- Ann Tipps<sup>4</sup>
- Grace Lin<sup>4</sup>
- Patricia A Thistlethwaite<sup>6</sup>
- Ranajoy Chattopadhyay<sup>1</sup> †
- Thomas F Rogers<sup>5</sup> †
- Debashis Sahoo<sup>3</sup> ([ORCID: 0000-0003-2329-8228](https://orcid.org/0000-0003-2329-8228)) †
- Pradipta Ghosh<sup>1</sup> ([ORCID: 0000-0002-8917-3201](https://orcid.org/0000-0002-8917-3201)) †
- Soumita Das<sup>2</sup> ([ORCID: 0000-0003-3895-3643](https://orcid.org/0000-0003-3895-3643)) †

### Affiliations

1. Department of Cellular and Molecular Medicine, University of California San Diego San Diego United States
2. HUMANOID CoRE, University of California San Diego San Diego United States
3. Department of Computer Science and Engineering, Jacobs School of Engineering, University of California San Diego San Diego United States
4. Department of Pathology, University of California San Diego San Diego United States
5. Department of Immunology and Microbiology, The Scripps Research Institute La Jolla United States
6. Division of Cardiothoracic Surgery, University of California San Diego San Diego United States
7. Division of Cardiology, Department of Internal Medicine, UC San Diego Medical Center San Diego United States
8. Pulmonary Critical Care Section, Veterans Affairs (VA) San Diego Healthcare System La Jolla United States
9. Division of Pulmonary and Critical Care, Department of Medicine, University of California, San Diego La Jolla, CA United States
10. Cell Applications Inc. La Jolla, CA United States
11. Division of Infectious Diseases, Department of Medicine, University of California, San Diego La Jolla United States
12. Department of Immunology and Microbiology, The Scripps Research Institute La Jolla United States
13. Department of Pediatrics, University of California, San Diego La Jolla, CA United States
14. Department of Medicine, University of California, San Diego La Jolla, CA United States

† Corresponding author

## Abstract

Background:SARS-CoV-2, the virus responsible for COVID-19, causes widespread damage in the lungs in the setting of an overzealous immune response whose origin remains unclear.Methods:We present a scalable, propagable, personalized, cost-effective adult stem cell-derived human lung organoid model that is complete with both proximal and distal airway epithelia. Monolayers derived from adult lung organoids (ALOs), primary airway cells, or hiPSC-derived alveolar type II (AT2) pneumocytes were infected with SARS-CoV-2 to create in vitro lung models of COVID-19.Results:Infected ALO monolayers best recapitulated the transcriptomic signatures in diverse cohorts of COVID-19 patient-derived respiratory samples. The airway (proximal) cells were critical for sustained viral infection, whereas distal alveolar differentiation (AT2→AT1) was critical for mounting the overzealous host immune response in fatal disease; ALO monolayers with well-mixed proximodistal airway components recapitulated both.Conclusions:Findings validate a human lung model of COVID-19, which can be immediately utilized to investigate COVID-19 pathogenesis and vet new therapies and vaccines.Funding:This work was supported by the National Institutes for Health (NIH) grants 1R01DK107585-01A1, 3R01DK107585-05S1 (to SD); R01-AI141630, CA100768 and CA160911 (to PG) and R01-AI 155696 (to PG, DS and SD); R00-CA151673 and R01-GM138385 (to DS), R01- HL32225 (to PT), UCOP-R00RG2642 (to SD and PG), UCOP-R01RG3780 (to P.G. and D.S) and a pilot award from the Sanford Stem Cell Clinical Center at UC San Diego Health (P.G, S.D, D.S). GDK was supported through The American Association of Immunologists Intersect Fellowship Program for Computational Scientists and Immunologists. L.C.A's salary was supported in part by the VA San Diego Healthcare System. This manuscript includes data generated at the UC San Diego Institute of Genomic Medicine (IGC) using an Illumina NovaSeq 6000 that was purchased with funding from a National Institutes of Health SIG grant (#S10 OD026929).

## Introduction

SARS-CoV-2, the virus responsible for COVID-19, causes widespread inflammation and injury in the lungs, giving rise to diffuse alveolar damage (DAD) (Andrea Valeria Arrossi and Farver, 2020; Damiani et al., 2021; Borczuk et al., 2020; Li et al., 2021; Roden, 2020), featuring marked infection and viral burden leading to apoptosis of alveolar pneumocytes (Hussman, 2020), along with pulmonary edema (Bratic and Larsson, 2013; Carsana et al., 2020). DAD leads to poor gas exchange and, ultimately, respiratory failure; the latter appears to be the final common mechanism of death in most patients with severe COVID-19 infection. How the virus causes so much damage remains unclear. A particular challenge is to understand the out-of-control immune reaction to the SARS-CoV-2 infection known as a cytokine storm, which has been implicated in many of the deaths from COVID-19. Although rapidly developed preclinical animal models have recapitulated some of the pathognomonic aspects of infection, for example, induction of disease, and transmission, and even viral shedding in the upper and lower respiratory tract, many failed to develop severe clinical symptoms (Lakdawala and Menachery, 2020). Thus, the need for preclinical models remains both urgent and unmet.

To address this need, several groups have attempted to develop human preclinical COVID-19 lung models, all within the last few months (Duan et al., 2020; Mulay et al., 2020; Salahudeen et al., 2020). While a head-to-head comparison of the key characteristics of each model can be found in Table 1, what is particularly noteworthy is that most of the models do not recapitulate the heterogeneous epithelial cellularity of both proximal and distal airways, that is, airway epithelia, basal cells, secretory club cells, and alveolar pneumocytes. Although induced pluripotent stem cells (iPSC)-derived AT2 cells be differentiated into proximal and distal cell types, including AT1, ciliated, and club cells (Kawakita et al., 2020; Dye et al., 2015; Huang et al., 2020), these iPSC-derived models lack propagability and cannot be reproducibly generated for biobanking; nor can they be scaled up in cost-effective ways for use in drug screens. More specifically, adult lung organoid models that can be grown in a sustainable mode and are complete with proximo-distal epithelia are yet to emerge. Besides the approaches described so far, there are a few more approaches used for modeling COVID-19: (i) 3D organoids from bronchospheres and tracheospheres have been established before (Hild and Jaffe, 2016; Rock et al., 2009; Tadokoro et al., 2016) and are now used in apical-out cultures for infection with SARS-COV-2 (Suzuki, 2020); (ii) the most common model used for drug screening is the air-liquid interphase (ALI model) in which pseudo-stratified primary bronchial or small airway epithelial cells are used to recreate the multilayered mucociliary epithelium (Mou et al., 2016; Randell et al., 2011); (iii) several groups have also generated 3D airway models from iPSCs or tissue-resident stem cells (Dye et al., 2015; Wong et al., 2012; Ghaedi et al., 2013; Konishi et al., 2016; McCauley et al., 2017; Miller et al., 2019); (iv) others have generated AT2 cells from iPSCs using closely overlapping protocols of sequential differentiation starting with definitive endoderm, anterior foregut endoderm, and distal alveolar expression (Gotoh et al., 2014; Jacob et al., 2017; Jacob et al., 2019; Yamamoto et al., 2017; Chen et al., 2017; Huang et al., 2014); and (v) finally, long-term in vitro culture conditions for pseudo-stratified airway epithelium organoids, derived from healthy and diseased adult humans suitable to assess virus infectivity (Sachs et al., 2019; van der Vaart and Clevers, 2021; Zhou et al., 2018), have been pioneered; unfortunately, these airway organoids expressed virtually no lung mesenchyme or alveolar signature. What remains unclear is if any of these models accurately recapitulate the immunopathological phenotype that is seen in the lungs in COVID-19.

**Table 1.**
 A comparison of current versus existing lung organoid models available for modeling COVID-19.


<table>
  <thead>
    <tr>
      <th rowspan="2">Author</th>
      <th rowspan="2">Source of stem cells</th>
      <th rowspan="2">Propagability</th>
      <th colspan="6">Cell types</th>
      <th rowspan="2">SARS-COV-2 infection</th>
      <th rowspan="2">Demonstrated reproducibility using more than one patient</th>
      <th rowspan="2">Cost-effective (use of conditioned media)</th>
      <th rowspan="2">Notes</th>
    </tr>
    <tr>
      <th>AT1</th>
      <th>AT2</th>
      <th>Club</th>
      <th>Basal</th>
      <th>Ciliated</th>
      <th>Goblet</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Zhou et alPMID: 29891677</td>
      <td>Small pieces of normal lung tissue adjacent to the diseased tissue from patients undergoing surgical resection for clinical conditions.</td>
      <td>Long term culture &gt; 1 y</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>Infection with H1N1 pandemic Influenza virus</td>
      <td></td>
      <td></td>
      <td>Proximal differentiation (PD) of human Adult Stem Cell-derived airway organoid (AO) culture. Differentiation conditions (PneumaCult-ALI medium) increase ciliated cells. Serine proteases known to be important for productive viral infection, were elevated after PD.</td>
    </tr>
    <tr>
      <td>Sachs et alPMID: 30643021</td>
      <td>Generation of normal and tumor organoids from resected surplus lung tissue of patients with lung cancers.</td>
      <td>long term culture for over 1 year</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>Not clearly mentioned</td>
      <td></td>
      <td></td>
      <td></td>
      <td>airway organoid (AO) expressed no mesenchyme or alveolar transcripts. Strongly enriched for bulk lung and small airway epithelial signature limited to basal, club, and ciliated cells Withdrawal of R-spondin terminated AO expansion after 3–4 passages similar to the withdrawal of FGFs</td>
    </tr>
    <tr>
      <td>Duan et alPMID: 32839764</td>
      <td>hPSC derived lung cells and macrophages</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>Low</td>
      <td>SARS-CoV-2 infection mediated damage onset by macrophages.</td>
      <td></td>
      <td></td>
      <td>Co-culture of lung cells and macrophages. Protocol followed enables alveolar differentiation process, although described presence of almost all lung cell types.</td>
    </tr>
    <tr>
      <td>Salahudeen et alPMID: 33238290</td>
      <td>Cells sorted from human peripheral lung tissues.</td>
      <td>Distal Lung organoid with possibility of long-term culture</td>
      <td>From differentiation of AT2</td>
      <td></td>
      <td>After diff of basal cells</td>
      <td></td>
      <td></td>
      <td></td>
      <td>Infection and presence of dsRNA and nucleocapsid</td>
      <td></td>
      <td></td>
      <td>No RNA seq of infected samples to compare with COVID Differentiation to different cell types SARS CoV2 infection in apical-out organoids (not polarized monolayers). The combination of EGF and the Noggin was optimal, without any additional growth-promoting effects of either WNT3A or R-spondin</td>
    </tr>
    <tr>
      <td>Han et alPMID: 33116299</td>
      <td>hPSC-derived lung organoids</td>
      <td>Organoids were generated by 50 days of differentiation</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>SARS-CoV-2 and SARS-CoV-2-Pseudo-Entry Viruses.</td>
      <td></td>
      <td></td>
      <td>AT1, AT2, stromal cells, low number of pulmonary neuroendocrine cells, proliferating cells, and airway epithelial cells were reported. Mostly AT2 based ACE2 receptor was used for virus infection. High throughput screen using hPSC-derived lung organoids identified FDA-approved drug candidates, including imatinib and mycophenolic acid, as inhibitors of SARS-CoV-2 entry.</td>
    </tr>
    <tr>
      <td>Youk et alPMID: 33142113</td>
      <td>Adult alveolar stem cells isolated from distal lung parenchymal tissues by collagenase, dispase and sorting</td>
      <td>Multiple passages upto 10 months</td>
      <td>From AT2; Lost in higher passages</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>In the organoid form</td>
      <td></td>
      <td></td>
      <td>Single cell transcriptomic profiling identified two clusters and type I interferon signal pathway are highly elevated at three dpi</td>
    </tr>
    <tr>
      <td rowspan="2">Mulay et alPMID: 32637946doi.org/10.1101/2020.06.29.174623</td>
      <td>Alv organoids with distal lung epithelial cells with lung fibroblast cells</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>In the organoid form</td>
      <td></td>
      <td></td>
      <td>Infection of AT2 cells trigger apoptosis that may contribute to alveolar injury. Alteration of innate immune response genes from AT2 cells</td>
    </tr>
    <tr>
      <td>Proximal airway ALI with heterogenous cells</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>Infection of ciliated and goblet cells Two separate models for SARS-CoV2 infection</td>
    </tr>
    <tr>
      <td>Huang JPMID:32979316</td>
      <td>iPSC derived AT2 cell ALI model</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>Bulk RNA seq after day 1 and day four infection. The infection induces rapid inflammatory responses.</td>
    </tr>
    <tr>
      <td rowspan="2">Abo et alPMID: 32577635doi: 10.1101/2020.06.03.132639</td>
      <td>iPSC derived basal cells as oranoids or 2D ALI</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td rowspan="2">iPSCs transcripts match human lung better than cancer cell lines. iPSC AT2 cells express host genes mportant for SARS-CoV-2 infection.</td>
    </tr>
    <tr>
      <td>iPSC AT2 cells as organoids or 2D ALI</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Rock et alPMID: 19625615</td>
      <td>Bronchospheres were isolated from human lung tissue.</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>Bronchospheres derived from human lung can act as stem cells and can differentiate into other cell types.</td>
    </tr>
    <tr>
      <td>Lamers et alPMID: 33283287</td>
      <td>Lung organoids derived from fetal Lung epithelial bud tips and differentiated ALI model.</td>
      <td>14 passages</td>
      <td></td>
      <td></td>
      <td>Detected SCGB3A2(ATII/club marker)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>2 subjects were mentioned</td>
      <td></td>
      <td>Organoid model derived from fetal lung bud tip tissue consists primarily of SOX2+ SOX9+ progenitor cells. Differentiation under ALI conditions is necessary to achieve mature alveolar epithelium. ALI model was found to contain mostly ATII and ATI cells, with small basal and rare neuroendocrine populations. SFTPC + Alveolar type II like cells were most readily infected by SARS-CoV-2. The infectious virus titer is much higher (five log) compared to other established model.</td>
    </tr>
    <tr>
      <td>Suzuki et aldoi: https://doi.org/10.1101/2020.05.25.115600</td>
      <td>Commercially available adult HBEpC cells were used to generate human bronchial organoids.</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>In the organoid form</td>
      <td></td>
      <td></td>
      <td>Organoids derived from HBEpC cells undergo differentiation process to achieve mature phenotype. Organoids are lacking distal epithelial cell types SARS-CoV-2 infection was performed on organoids and only the basolateral region came in to contact with the virus. Treatment with a TMPRSS2 inhibitor prior to infection demonstrated a reduction in infectivity.</td>
    </tr>
    <tr>
      <td>Tiwari et alPMID: 33631122</td>
      <td>Differentiated human iPSCs into lung organoids.</td>
      <td>80 days</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>In the organoid form</td>
      <td></td>
      <td></td>
      <td>Organoids originated from iPSC cells and have proximal and distal epithelial cells. Infected organoids with SARS-CoV-2 and pseudovirus. SARS-CoV-2 pseudovirus entry was blocked by viral entry inhibitors.</td>
    </tr>
    <tr>
      <td>Tindle et al [Current study]</td>
      <td>Deep lung tissue sections surgically obtained from patients undergoing lobe resections for lung cancers.</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>RNA Seq and cross-validation of COVID-19 model. Single model with all the cells types and infection of SARS-CoV2 in the 2D form with Apical accessibility that close to physiologic state.</td>
    </tr>
  </tbody>
</table>

_ACE2: angiotensin-converting enzyme II; ALI: air-liquid interphase; TMPRSS2: transmembrane serine protease 2.Blue color cells denote the presence of the features.Red color cells denote the absence of the features.Grey color cells denote information not found._

We present a rigorous transdisciplinary approach that systematically assesses an adult lung organoid model that is propagable, personalized, and complete with both proximal airway and distal alveolar cell types against existing models that are incomplete, and we cross-validate them all against COVID-19 patient-derived respiratory samples. Findings surprisingly show that cellular crosstalk between both proximal and distal components is necessary to emulate how SARS-CoV-2 causes diffuse alveolar pneumocyte damage; the proximal airway mounts a sustained viral infection, but it is the distal alveolar pneumocytes that mount the overzealous host response that has been implicated in a fatal disease.

## Results

### A rationalized approach for creating and validating acute lung injury in COVID-19

To determine which cell types in the lungs might be most readily infected, we began by analyzing a human lung single-cell sequencing dataset (GSE132914) for the levels of expression of angiotensin-converting enzyme II (ACE2) and transmembrane serine protease 2 (TMPRSS2), the two receptors that have been shown to be the primary sites of entry for the SARS-CoV-2 (Hoffmann et al., 2020). The dataset was queried with widely accepted markers of all the major cell types (see Table 2). Alveolar epithelial type 2 (AT2), ciliated and club cells emerged as the cells with the highest expression of both receptors (Figure 1A, Figure 1—figure supplement 1A). These observations are consistent with published studies demonstrating that ACE2 is indeed expressed highest in AT2 and ciliated cells (Mulay et al., 2020; Zhao et al., 2020; Jia et al., 2005). In a cohort of deceased COVID-19 patients, we observed by H&E (Figure 1—figure supplement 1B) that gas-exchanging flattened AT1 pneumocytes are virtually replaced by cuboidal cells that were subsequently confirmed to be AT2-like cells via immunofluorescent staining with the AT2-specific marker, surfactant protein C (SFTPC; Figure 1B, upper panel, Figure 1—figure supplement 1C, top). We also confirmed that club cells express ACE2 (Figure 1—figure supplement 1C, bottom), underscoring the importance of preserving these cells in any ideal lung model of COVID-19. When we analyzed the lungs of deceased COVID-19 patients, the presence of SARS-COV-2 in alveolar pneumocytes was also confirmed, as determined by the colocalization of viral nucleocapsid protein with SFTPC (Figure 1B, lower panel, Figure 1—figure supplement 1D). Immunohistochemistry studies further showed the presence of SARS-COV-2 virus in alveolar pneumocytes and in alveolar immune cells (Figure 1—figure supplement 1E). These findings are consistent with the gathering consensus that alveolar pneumocytes support the interaction between the epithelial cells and inflammatory cells recruited to the lung; via mechanisms that remain unclear, they are generally believed to contribute to the development of acute lung injury and acute respiratory distress syndrome (ARDS), the severe hypoxemic respiratory failure during COVID-19 (Hou et al., 2020; Spagnolo et al., 2020). Because prior work has demonstrated that SARS-CoV-2 infectivity in patient-derived airway cells is highest in the proximal airway epithelium compared to the distal alveolar pneumocytes (AT1 and AT2) (Hou et al., 2020), and yet, it is the AT2 pneumocytes that harbor the virus, and the AT1 pneumocytes that are ultimately destroyed during DAD, we hypothesized that both proximal airway and distal (alveolar pneumocyte) components might play distinct roles in the respiratory system to mount the so-called viral infectivity and host immune response phases of the clinical symptoms observed in COVID-19 (Chen and Li, 2020).

**Table 2.**
 Markers used to identify various cell types in the lung.


<table>
  <thead>
    <tr>
      <th>Cell type</th>
      <th>Markers</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AT1</td>
      <td>AQP5*$, PDPN*$$, Carboxypeptidase M, CAV-1, CAV-2, HTI56, HOPX, P2R × 4*$$, Na+/K + ATPase$, TIMP3*++, SEMA3F PDPN* AQP5* P2R × 4* TIMP3* SERPINE*</td>
    </tr>
    <tr>
      <td>AT2</td>
      <td>ABCA3*$$, CC10 (SCGB1A1*)+, CD44v6, Cx32, gp600++, ICAM-1++, KL-6, LAMP3*$$, MUC1, SFTPA1*$$, SFTPB*$, SFTPC*+, SFTPD*, SERPINE1</td>
    </tr>
    <tr>
      <td>Club</td>
      <td>CC10 (SCGB1A1*)+, CYP2F2*, ITAG6*$$, SCGB3A2*$$, SFTPA1*$$, SFTPB*$, SFTPD*</td>
    </tr>
    <tr>
      <td>Goblet</td>
      <td>CDX-2*, MUC5AC*, MUC5B*, TFF3*, UEA1+</td>
    </tr>
    <tr>
      <td>Ciliated</td>
      <td>ACT (ACTG2*)$, BTub4 (TUBB4A*), FOXA3*++, FOXJ1*, SNTN*</td>
    </tr>
    <tr>
      <td>Basal</td>
      <td>CD44v6 (CD44*), ITGA6*$$, KRT5*$, KRT13*, KRT14*, p63 (CKAP4*), p75 (NGFR*)$$</td>
    </tr>
    <tr>
      <td>Generic Lung Lineage</td>
      <td>Cx43 (GJA1*), TTF-1 (TTF1*; Greatest in AT2 &amp; Club), EpCAM (EPCAM*)</td>
    </tr>
  </tbody>
</table>

_*Markers used for single-cell gating (Figure 1A).$ denotes markers used in this work for Immunofluorescence (IF).$$ denotes markers used in this work for qPCR.+ denotes markers used in both IF and qPCR.++ denotes obscure markers (Not a lot of research relative to lung)._

![Figure 1.](https://cdn.elifesciences.org/articles/66417/elife-66417-fig1-v2.jpg)

**Figure 1.:** A) Whisker plots display relative levels of angiotensin-converting enzyme II (ACE2) expression in various cell types in the normal human lung. The cell types were annotated within a publicly available single-cell sequencing dataset (GSE132914) using genes listed in Table 1. p-values were analyzed by one-way ANOVA and Tukey’s post hoc test. (B) Formalin-fixed paraffin-embedded sections of the human lung from normal and deceased COVID-19 patients were stained for SFTPC, alone or in combination with nucleocapsid protein and analyzed by confocal immunofluorescence. Representative images are shown. Scale bar = 20 µm. (C) Schematic showing key steps generating an adult stem cell-derived, propagable, lung organoid model, complete with proximal and distal airway components for modeling COVID-19-in-a-dish. See Materials and methods for details regarding culture conditions. (D) A transcriptome-based approach is used for cross-validation of in vitro lung models of SARS-CoV-2 infection (left) versus the human disease, COVID-19 (right), looking for a match in gene expression signatures.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/66417/elife-66417-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Whisker plots display relative levels of TMPRSS2 expression in various cell types in the normal human lung. The cell types were annotated within a publicly available single-cell sequencing dataset (GSE132914) using genes listed in Table 2. p-values were analyzed by one-way ANOVA and Tukey’s post hoc test. (B) Formalin-fixed paraffin-embedded (FFPE) sections of the human lung from deceased COVID-19 patients were analyzed by H&E staining. Representative fields are shown. Images on the right are magnified areas indicated with boxes on the left. Arrows indicate alveolar type II pneumocyte hyperplasia. (C, D) FFPE sections of the human lung from normal and deceased COVID-19 patients were stained for AT2 and club cell markers and either ACE2 or viral nucleocapsid protein and analyzed by confocal immunofluorescence. Representative images are shown. Scale bar = 50 µm. (E) FFPE sections of the human lung from normal and deceased COVID-19 patients were stained for viral nucleocapsid antibody. Representative images are shown. Arrows indicate infected cells.

Because no existing lung model provides such proximodistal cellular representation (Table 1), and hence, may not recapitulate with accuracy the clinical phases of COVID-19, we first sought to develop a lung model that is complete with both proximal and distal airway epithelia using adult stem cells that were isolated from deep lung biopsies (i.e., sufficient to reach the bronchial tree). Lung organoids were generated using the work flow outlined in Figure 1C and a detailed protocol that had key modifications from previously published (Sachs et al., 2019; Zhou et al., 2018) methodologies (see Materials and methods). Organoids grown in 3D cultures were subsequently dissociated into single cells to create 2D monolayers (either maintained submerged in media or used in ALI model) for SARS-CoV-2 infection, followed by RNA seq analysis. Primary airway epithelial cells and hiPSC-derived alveolar type II (AT2) pneumocytes were used as additional models (Figure 1D, left panel). Each of these transcriptomic datasets was subsequently used to cross-validate our ex vivo lung models of SARS-CoV-2 infection with the human COVID-19 autopsy lung specimens (Figure 1D, right panel) to objectively vet each model for their ability to accurately recapitulate the gene expression signatures in the patient-derived lungs.

### Creation of a lung organoid model, complete with both proximal and distal airway epithelia

Three lung organoid lines were developed from deep lung biopsies obtained from the normal regions of lung lobes surgically resected for lung cancer; both genders, smokers and non-smokers, were represented (Figure 2—figure supplement 1A; Table 3). Three different types of media were compared (Figure 2—figure supplement 1B); the composition of these media was inspired either by their ability to support adult-stem cell-derived mixed epithelial cellularity in other organs (like the gastrointestinal [GI] tract [Miyoshi and Stappenbeck, 2013; Sato et al., 2009; Sayed et al., 2020c]) or rationalized based on published growth conditions for proximal and distal airway components (Gotoh et al., 2014; Sachs et al., 2019; van der Vaart and Clevers, 2021). A growth condition that included conditioned media from L-WRN cells that express Wnt3, R-spondin, and Noggin, supplemented with recombinant growth factors, which we named as ‘lung organoid expansion media,’ emerged as superior compared to alveolosphere media-I and II (Jacob et al., 2019; Yamamoto et al., 2017) (details in Materials and methods), based on its ability to consistently and reproducibly support the best morphology and growth characteristics across multiple attempts to isolate organoids from lung tissue samples. Three adult lung organoid lines (ALO1-3) were developed using the expansion media, monitored for their growth characteristics by brightfield microscopy and cultured with similar phenotypes until P10 and beyond (Figure 2—figure supplement 1C and D). The 3D morphology of the lung organoid was also assessed by H&E staining of slices cut from formalin-fixed paraffin-embedded (FFPE) cell blocks of HistoGel-emb`edded ALO1-3 (Figure 2—figure supplement 1E).

**Table 3.**
 Characteristics of patients enrolled into this study for obtaining lung tissues to serve as source of stem cells to generate lung organoids.


<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Date of surgery</th>
      <th>Age</th>
      <th>Sex</th>
      <th>Smoking history</th>
      <th>Reason for surgery</th>
      <th>Histology</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ALO1</td>
      <td>4/17/2020</td>
      <td>64</td>
      <td>Male</td>
      <td>Current, chronic smokerPacks/day: 0.50Years: 53Pack years: 26.5</td>
      <td>Lung carcinoma</td>
      <td>Invasive squamous cell carcinoma, non-keratinizing</td>
    </tr>
    <tr>
      <td>ALO2</td>
      <td>4/17/2020</td>
      <td>59</td>
      <td>Male</td>
      <td>Non-smoker</td>
      <td>Lung carcinoma</td>
      <td>Invasive adenocarcinoma</td>
    </tr>
    <tr>
      <td>ALO3</td>
      <td>7/7/2020</td>
      <td>46</td>
      <td>Female</td>
      <td>Non-smoker</td>
      <td>Left lower lobe nodule</td>
      <td>Invasive adenocarcinoma</td>
    </tr>
  </tbody>
</table>

To determine if all the six major lung epithelial cells (illustrated in Figure 2A) are present in the organoids, we analyzed various cell-type markers by qRT-PCR (Figure 2B–H and Figure 2—figure supplement 2A-H). All three ALO lines had a comparable level of AT2 cell surfactant markers (compared against hiPSC-derived AT2 cells as positive control) and a significant amount of AT1, as determined using the marker AQP5. ALOs also contained basal cells (as determined by the marker ITGA6, p75/NGFR, TP63), ciliated cells (as determined by the marker FOXJ1), and club cells (as determined by the marker SCGB1A1). As expected, the primary normal human bronchial epithelial cells (NHBE) had significantly higher expression of basal cell markers than the ALO lines (hence, served as a positive control), but they lacked stemness and club cells (hence, served as a negative control).

![Figure 2.](https://cdn.elifesciences.org/articles/66417/elife-66417-fig2-v2.jpg)

**Figure 2.:** (A) Schematic lists the various markers used here for qPCR and immunofluorescence to confirm the presence of all cell types in the 3D lung organoids here and in 2D monolayers later (in Figure 3). (B–H) Bar graphs display the relative abundance of various cell-type markers (normalized to 18S) in adult lung organoids (ALO), compared to the airway ( normal human bronchial epithelial cell [NHBE]) and/or alveolar (AT2) control cells, as appropriate. p-values were analyzed by one-way ANOVA. Error bars denote SEM; n = 3–6 datasets from three independent ALOs and representing early and late passages. See also Figure 2—figure supplement 2 for individual ALOs. (I, J). H&E-stained cell blocks were prepared using HistoGel (I). Slides were stained for the indicated markers and visualized by confocal immunofluorescence microscopy. Representative images are shown in (J). Scale bar = 50 µm. (K) 3D organoids grown in 8-well chamber slides were fixed, immunostained, and visualized by confocal microscopy as in (J). Scale bar = 50 µm. See also Figure 2—figure supplement 2. Top row (ACE2/KRT5-stained organoids) displays the single and merged panels as max projections of z-stacks (top) and a single optical section (bottom) of a selected area. For the remaining rows, the single (red/green) channel images are max projections of z-stacks; however, merged panels are optical sections to visualize the centers of the organoids. All immunofluorescence images showcased in this figure were obtained from ALO lines within passage #3–6. See also Figure 2—figure supplements 3–5 for additional evidence of mixed cellularity of ALO models, their similarity to lung tissue of origin, and stability of cellular composition during early (#1–8) and late (#8–15) passages, as determined by qPCR and flow cytometry.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/66417/elife-66417-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Schematic displaying the key demographics of the patients who served as donors of the lung tissue as a source of adult stem cells for the generation of organoids. Three organoid lines were generated, ALO1-3. ALO, adult lung organoids. (B–D) Bright-field microscopy of organoids in 3D culture grown in different media/conditions (B), imaged serially over days (C), and at different passages (D). Scale bar = 100 µm. (E) Serial cuts of HistoGel-embedded organoids were analyzed by H&E staining. Scale bar = 50 µm.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/66417/elife-66417-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) Schematic lists the various markers used here for qPCR and immunofluorescence to confirm the presence of all cell types in the 3D lung organoids here and in 2D monolayers later (in Figure 3). (B–H) Bar graphs display the relative abundance of various cell-type markers (normalized to 18S) in adult lung organoids (ALO), compared to the airway ( normal human bronchial epithelial cell [NHBE]) and/or alveolar (AT2) control cells, as appropriate. p-values were analyzed by one-way ANOVA. Error bars denote SEM; n = 3–6 datasets. (I) 3D organoids grown in 8-well chamber slides were fixed, immunostained, and visualized by confocal microscopy, as in Figure 2K. Scale bar = 50 µm.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/66417/elife-66417-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** (A, B) Schematics depict the study goal in this figure, that is, analysis of cell-type-specific transcripts in ALO vs. ALT. (C–L) Bar graphs display the relative abundance of various cell-type markers (normalized to 18S) in adult lung organoids from early passage (ALO), compared to the adult lung tissue (ALT) from which they were derived. p-values were analyzed by one-way ANOVA. Error bars denote SEM; n = 3–6 datasets. Statistically significant differences were not noted in any of the transcripts analyzed.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/66417/elife-66417-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** (A, B) Schematics depict the study goal in this figure, that is, analysis of cell-type-specific transcripts in early (E) vs. late (L) passages of ALO1-3 lines. (C–K) Bar graphs display the relative abundance of various cell-type markers (normalized to 18S) in adult lung organoids from either early (E) or late (L) passages of ALO lines 1–3. p-values were analyzed by one-way ANOVA. Error bars denote SEM; n = 3–6 datasets. Statistically significant differences were not noted in any of the transcripts analyzed.

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/66417/elife-66417-fig2-figsupp5-v2.jpg)

**Figure 2—figure supplement 5.:** Lung monolayers were dissociated into single cells and analyzed using flow cytometry. Gating strategy depicted in (A), isotype controls in (B) and (C) show various lung cell types. Numbers denote %.Table in (D) lists marker-positive cell fractions in ALO1-3, presented either as averaged over both early and late passages combined (column 2), or separated into early (column 3) or late (column 4) passages. These findings are consistent with others’ findings by multichannel FACS (Bonser et al., 2021) showing that although many of these markers are highly expressed in a certain cell type, they are shared at lower levels among other cell types.

The presence of all cell types was also confirmed by assessing protein expression of various cell types within organoids grown in 3D cultures. Two different approaches were used—(i) slices cut from FFPE cell blocks of HistoGel-embedded ALO lines (Figure 2I and J) or (ii) ALO lines grown in 8-well chamber slides were fixed in Matrigel (Figure 2K), stained, and assessed by confocal microscopy. Such staining not only confirmed the presence of more than one cell type (i.e., mixed cellularity) of proximal (basal-KRT5) and distal (AT1/AT2 markers) within the same ALO line, but also, in some instances, demonstrated the presence of mixed cellularity within the same 3D structure. For example, AT2 and basal cells, marked by SFTPB and KRT5, respectively, were found in the same 3D structure (Figure 2J, interrupted curved lines). Similarly, ciliated cells and goblet cells stained by Ac-Tub and Muc5AC, respectively, were found to coexist within the same structure (Figure 2J, interrupted box; Figure 2K, arrow). Intriguingly, we also detected 3D structures that co-stained for CC10 and SFTPC (Figure 2J, bottom panel) indicative of mixed populations of club and AT2 cells. Besides the organoids with heterogeneous makeup, each ALO line also showed homotypic organoid structures that were relatively enriched in one cell type (Figure 2J, arrowheads pointing to two adjacent structures that are either KRT5- or SFTPB-positive). Regardless of their homotypic or heterotypic cellular organization into 3D structures, the presence of mixed cellularity was documented in all three ALO lines (see multiple additional examples in Figure 2—figure supplement 2I). It is noteworthy that the coexistence of proximal and distal epithelial cells in lung organoids has been achieved in one another instance prior; Lamers et al. showed such mixed cellular composition in fetal lung bud tip-derived organoids Lamers et al., 2021. However, their model lacked ciliated and goblet cells (Lamers et al., 2021), something that we could readily detect in our 3D organoids.

Finally, using qRT-PCR of various cell-type markers as a measure, we confirmed that the ALO models overall recapitulated the cell-type composition in the adult lung tissues from which they were derived (Figure 2—figure supplement 3) and retained such composition in later passages without significant notable changes in any particular cell type (Figure 2—figure supplement 4). The mixed proximal and distal cellular composition of the ALO models and their degree of stability during in vitro culture was also confirmed by flow cytometry (Figure 2—figure supplement 5).

### Organoid cellularity resembles tissue sources in 3D cultures but differentiates in 2D cultures

To model respiratory infections such as COVID-19, it is necessary for pathogens to be able to access the apical surface. It is possible to microinject into the lumens of 3D organoids, as done previously with pathogens in the case of gut organoids (Engevik et al., 2015; Forbester et al., 2015; Leslie et al., 2015; Williamson et al., 2018), or FITC-dextran in the case of lung organoids (Porotto et al., 2019), or carry out infection in apical-out 3D lung organoids with basal cells (Salahudeen et al., 2020). However, the majority of the researchers have gained apical access by dissociating 3D organoids into single cells and plating them as 2D-monolayers (Duan et al., 2020; Mulay et al., 2020; Huang et al., 2020; Sachs et al., 2019; Zhou et al., 2018; Han et al., 2020a; Han et al., 2020b. As in any epithelium, the differentiation of airway epithelial cells relies upon dimensionality (apicobasal polarity); because the loss of dimensionality can have a major impact on cellular proportions and impact disease-modeling in unpredictable ways, we assessed the impact of the 3D-to-2D conversion on cellularity by RNA seq analyses. Two commonly encountered methods of growth in 2D monolayers were tested: (i) monolayers polarized on trans-well inserts but submerged in growth media (Figure 3A and Figure 3—figure supplement 1A-D) and (ii) monolayers were grown at the air-liquid interface (popularly known as the ‘ALI model’; Prytherch et al., 2011; Dvorak et al., 2011) for 21 days to differentiate into the mucociliary epithelium (Figure 3A and Figure 3—figure supplement 1E-G). The submerged 2D monolayers had several regions of organized vacuolated-appearing spots (Figure 3—figure supplement 1D, arrow), presumably due to morphogenesis and cellular organization even in 2D. Consistent with this morphological appearance, the epithelial barrier formed in the submerged condition was leakier, as determined by relatively lower transepithelial electrical resistance (TEER; Figure 3—figure supplement 1B) and the flux of FITC-dextran from apical to basolateral chambers (Figure 3—figure supplement 1C), and corroborated by morphological assessment by confocal immunofluorescence of localization of occludin, a bona fide TJ marker. We chose occludin because it is a shared and constant marker throughout the airway that stabilizes claudins and regulates their turnover McGowan, 2014 and plays an important role in maintaining the integrity of the lung epithelial barrier Liu et al., 2014. Junction-localized occludin was patchy in the monolayer, despite the fact that the monolayer was otherwise intact, as determined by phalloidin staining (Figure 3—figure supplement 1H and I). Our finding that ALO 3D organoids differentiating into monolayers in submerged cultures (where alveolar differentiation and cell flattening happens dynamically as progenitor cells give rise to AT1/2 cells) are leaky is in keeping with prior work demonstrating that the TJs are rapidly remodeled as alveolar cells mature Schlingmann et al., 2015; Yang et al., 2016. By contrast, and as expected Rayner et al., 2019, the ALI monolayers formed a more effective epithelial barrier, as determined by TEER (Figure 3—figure supplement 1F), and appeared to be progressively hazier with time after air-lift, likely due to the accumulation of secreted mucin (Figure 3—figure supplement 1G).

![Figure 3.](https://cdn.elifesciences.org/articles/66417/elife-66417-fig3-v2.jpg)

**Figure 3.:** (A, B) Samples collected at various steps of lung organoid isolation and expansion in culture, and from the two types of monolayers prepared using the lung organoids were analyzed by bulk RNA seq and the datasets were compared for % cellular composition using the deconvolution method, CYBERSORTx. Schematic in (A) shows the workflow steps, and bar plots in (B) show the relative proportion of various lung cell types. (C, D) hiPSC-derived AT2 cells and alveolospheres (C) were plated as monolayers and analyzed by RNA seq. Bar plots in (D) show % cellular composition. (E, F) Submerged adult lung organoids (ALO) monolayers in transwells (E) or monolayers were grown as air-liquid interphase (ALI) models (F) were fixed and stained for the indicated markers and visualized by confocal immunofluorescence microscopy. The representative max projected z-stack images (left) and the corresponding orthogonal images (right) are displayed. Arrows in (E) indicate AT2 cells; arrowheads in (E) indicate club cells; asterisk in (F) indicates bundles of cilia standing perpendicular to the plane of the ALI monolayers; arrowheads in (F) indicate bundles of cilia running parallel to the plane of the ALI monolayers. Scale bar = 20 µm. (G) Monolayers of ALO1-3 were challenged with SARS-CoV-2 for indicated time points prior to fixation and staining for KRT5, SARS-COV2 viral nucleocapsid protein and DAPI and visualized by confocal microscopy. A montage of representative images are shown, displaying reticulovesicular network patterns and various cytopathic effects. Scale bar = 15 µm. (H) Monolayers of ALO, hiPSC-derived AT2 cells, and other alternative models (see Figure 3—figure supplements 1–2) were infected or not with SARS-CoV-2 and analyzed for infectivity by qPCR (targeted amplification of viral envelope, E gene). See also Figure 3—figure supplement 3B, C for comparison of the degree of peak viral amplification across various models. (I) ALO monolayers pretreated for 4 hr with either vehicle (DMSO) control or EIDD-parent (NHC) or its metabolite EIDD-2801/MK-4482 were infected with SARS-CoV-2 and assessed at 48 hpi for infectivity as in (H). Line graphs display the relative expression of E gene. Error bars display SEM. p value **<0.01; ***<0.001.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/66417/elife-66417-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A–G) Two different types of 2D polarized monolayers are prepared using adult lung organoids. Schematics in (A) and (E) show growth as submerged or air-liquid interphase (ALI) models, respectively. Panel (B) shows bar graphs with transepithelial electrical resistance (TEER) across submerged monolayers grown in transwells. Panel (C) shows bar graphs for relative fluorescence unit (RFU) of the FITC-labeled dextran flux from the apical to basolateral chambers of a submerged monolayer. (D) Brightfield images show representative fields of submerged monolayers grown on transwells. Scale bar = 100 µm. Arrows indicate self-organized vacuolar regions were seen. (F) Bar graphs with TEER across ALO-derived monolayers grown as ALI models. (G) Brightfield images show representative fields of ALI monolayers at two different time points during culture. Scale bar = 100 µm. (H, I) Submerged monolayers of ALO were fixed with methanol (H) or paraformaldehyde (I) prior to co-staining with DAPI (blue; nuclei) and either occludin (green [H] or phalloidin [red; I]). Scale bar = 20 µm. (J) ALO monolayers were grown as ALI models were fixed and co-stained for SFTPC (red), Ac-Tub (green), and DAPI (blue; nuclei) and visualized by confocal immunofluorescence microscopy. Scale bar = 20 µm. (K, L) Schematic in (K) shows the study design for challenging submerged monolayers with 500 ng/ml LPS, followed by TEER measurement. Bar graphs in (L) display the % change in TEER observed with or without LPS treatment normalized to the baseline TEER. p-values were analyzed by one-way ANOVA. Error bars denote SEM; n = 3–6 datasets. **p< 0.01.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/66417/elife-66417-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A–D) Monolayers of primary airway epithelial cells (small airway epi; A B; bronchial epi; C, D) were visualized by bright field microscopy (A, C) or by fixing, staining, and visualizing by confocal microscopy (B, D). Representative images in (B) and (D) are presented as maximum projected z-stacks on the left and as an orthogonal view on the right. (E–G) hiPSC-derived AT2 cells, prepared using the i-HAEpC2 cell kit, were grown in monolayers on transwell inserts to form a polarized. Brightfield images are shown in (F). Monolayers were fixed and stained for several markers and analyzed by confocal microscopy. Representative images are shown in (G). Scale bar = 20 µm.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/66417/elife-66417-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** (A) Monolayers of ALO1-3 were challenged with SARS-CoV-2 for indicated time points prior to fixation and staining for KRT5 (red) and viral nucleocapsid protein (green) and DAPI (blue; nuclei) and visualized by confocal microscopy. Representative images are shown, displaying various cytopathic effects. Scale bar = 15 µm. (B) Monolayers of adult lung organoids (ALO) (either transwell submerged models or air-liquid interphase [ALI], left) and monolayers of hiPSC-derived AT2 cells (right) were infected or not with SARS-CoV-2 and analyzed for viral envelope gene (E gene). Bar graphs display the relative expression of E gene in infected ALO monolayers, indicative of viral infection. (C) Line graphs show the change in E gene expression in infected monolayers over 24 hr period (from 48 hpi to 72 hpi) where values at 72 hpi are normalized to that at 48 hpi. Data is presented as SEM of three independent repeats.

RNA seq datasets were analyzed using the same set of cell markers, as we used in Figure 1A (listed in Table 2). Consistent with our morphological, gene expression, and FACS-based studies showcased earlier (Figure 2 and Figure 2—figure supplements 2–5), cell-type deconvolution of our transcriptomic dataset using CIBERSORTx (https://cibersortx.stanford.edu/runcibersortx.php) confirmed that cellular composition in the human lung tissues was reflected in the 3D ALO models and that such composition was also relatively well-preserved over several passages (Figure 3B, left); both showed a mixed population of simulated alveolar, basal, club, ciliated, and goblet cells. When 3D organoids were dissociated and plated as 2D monolayers on transwells, the AT2 signatures were virtually abolished with a concomitant and prominent emergence of AT1 signatures, suggesting that growth in 2D monolayers favors differentiation of AT2 cells into AT1 cells Shami and Evans, 2015 (Figure 3B, middle). A compensatory reduction in proportion was also observed for the club, goblet, and ciliated cells. The same organoids, when grown in long-term 2D culture conditions in the ALI model, showed a strikingly opposite pattern; alveolar signatures were almost entirely replaced by a concomitant increase in ciliated and goblet cells (Figure 3B, right). These findings are consistent with the well-established notion that ALI conditions favor growth as pseudo-stratified mucociliary epithelium Prytherch et al., 2011; Dvorak et al., 2011. As an alternative model for use as monolayers for viral infection, we developed hiPSC-derived AT2 cells and alveolospheres (Figure 3C), using established protocols Huang et al., 2020. Because they were grown in the presence of CHIR99021 (an aminopyrimidine derivate that is a selective and potent Wnt agonist) Jacob et al., 2019; Yamamoto et al., 2017; Abdelwahab et al., 2019, which probably inhibits the AT2→AT1 differentiation, these monolayers were enriched for AT2 and devoid of AT1 cells (Figure 3D).

The multicellularity of lung organoid monolayers was also confirmed by immunofluorescence staining and confocal microscopy of the submerged and ALI monolayers, followed by the visualization of cell markers in either max-projected z-stacks (Figure 3E, left) or orthogonal views of the same (Figure 3E, right). As expected, markers for the same cell type (i.e., SFTPB and SFTPC, both AT2 markers) colocalize, but markers for different cell types do not. Submerged monolayers showed the prominent presence of both AT1 (AQP5-positive) and AT2 cells. Compared to the 3D organoids, the 2D organoid cultures, especially the ALI model, showed a significant increase in ciliated structures, as determined by acetylated tubulin (compare Ac Tub-stained panels in Figure 2J and K with Figure 3E and F). The observed progressive prominence of ciliary structures from 3D to 2D models is in keeping with the fact that 3D ALOs that are yet to form lumen represent the least differentiated state, whereas 2D submerged monolayers are intermediate and the 2D ALI monolayers are maximally differentiated; differentiation is known to establish apicobasal polarity, which is essential for the emergence of mature cilia on the apical surface. This increase in ciliated epithelium was associated with a concomitant decrease in KRT5-stained basal cells (Figure 3F). Such loss of the basal cell marker KRT5 between submerged monolayers and the ALI model can be attributed to and the expected conversion of basal cells to other cell types (i.e., ciliated cells) Gras et al., 2017; Khelloufi et al., 2018. The presence of AT2 cells, scattered amidst the ciliated cells in these ALI monolayers, was confirmed by co-staining them for SFTPC and Ac-Tub (Figure 3—figure supplement 1J).

Finally, we sought to confirm that the epithelial barrier that is formed by the submerged monolayers derived from ALO is responsive to infections. To this end, we simulated infection by challenging ALO monolayers with LPS. Compared to unchallenged controls, the integrity of the barrier was impaired by LPS, as indicated by a significant drop in the TEER (Figure 3—figure supplement 1K and L), which is in keeping with the known disruptive role of LPS on the respiratory epithelium Kalsi et al., 2020.

Taken together, the immunofluorescence images are in agreement with the RNA seq dataset; both demonstrate that the short-term submerged monolayer favors distal differentiation (AT2→AT1), whereas the 21-day ALI model favors proximal mucociliary differentiation. It is noteworthy that these distinct differentiation phenotypes originated from the same 3D organoids despite the seeding of cells in the same basic media composition (i.e., PneumaCult) prior to switching over to an ALI maintenance media for the prolonged growth at ALI; the latter is a well-described methodology that promotes differentiation into ciliated and goblet cells Rayner et al., 2019.

### Differentiated 2D monolayers show that SARS-CoV-2 infectivity is higher in proximal than distal epithelia

Because the lung organoids with complete proximodistal cellularity could be differentiated into either distal-predominant monolayers in submerged short-term cultures or proximal-predominant monolayers in long-term ALI cultures, this provided us with an opportunity to model the respiratory tract and assess the impact of the virus along the entire proximal-to-distal gradient. We first asked if ALO monolayers are permissive to SARS-CoV-2 entry and replication and support sustained viral infection. Confocal imaging of infected ALO monolayers with anti-SARS-COV-2 nucleocapsid protein antibody showed that submerged ALO monolayers did indeed show progressive changes during the 48–72 hr window after infection (Figure 3G): by 48 hpi, we observed the formation of ‘reticulovesicular patterns’ that are indicative of viral replication within modified host endoplasmic reticulum (Knoops et al., 2008; Figure 3G, left), and by 72 hpi we observed focal cytopathic effect (CPE) (Kaye, 2006) such as cell-rounding, detachment, and bursting of virions (Figure 3G, right, Figure 3—figure supplement 3A).

We next asked how viral infectivity varies in the various lung models. Because multiple groups have shown the importance of the ciliated airway cells for infectivity (i.e., viral entry, replication, and apical release [Hou et al., 2020; Milewska et al., 2020; Zhu et al., 2020; Hui et al., 2020]), as positive controls, we infected monolayers of human airway epithelia (see the legend, Figure 3—figure supplement 2A-D. AT2 cells, which express high levels of viral entry receptors ACE2 and TMPRSS2 (Figure 1A, Figure 1—figure supplement 1A), have been shown to be proficient in the viral entry but are least amenable to sustained viral release and infectivity (Hou et al., 2020; Hui et al., 2020). To this end, we infected monolayers of hiPSC-derived homogeneous cultures of AT2 cells as secondary controls (see the legend, Figure 3—figure supplement 2E-G). Infection was carried out using the Washington strain of SARS-CoV-2, USA-WA1/2020 (BEI Resources NR-52281 Rogers et al., 2020). As expected, the 2D lung monolayers we generated, both the submerged and the ALI models, were readily infected with SARS-CoV-2 (Figure 3—figure supplement 3B), as determined by the presence of the viral envelope gene (E gene; Figure 3H); however, the kinetics of viral amplification differed. When expressed as levels of E gene normalized to the peak values in each model (Figure 3H), the kinetics of the ALI monolayer model mirrored that of the primary airway epithelial monolayers; both showed slow beginning (0–48 hpi) followed by an exponential increase in E gene levels from 48 to 72 hpi. The submerged monolayer model showed sustained viral infection during the 48–72 hpi window (Figure 3—figure supplement 3B, left). In the case of AT2 cells, the 48–72 hpi window was notably missing in monolayers of hiPSC-derived AT2 cells (Figure 3H and Figure 3—figure supplement 3B, right). When we specifically analyzed the kinetics of viral E gene expression during the late phase (48–72 hpi window), we found that proximal airway models (human bronchial airway epi [HBEpC]) showed high levels of sustained infectivity than distal models (human small airway epi [HSAEpC] and AT2) to viral replication (Figure 3—figure supplement 3C); the ALO monolayers showed intermediate sustained infectivity (albeit with variability). All models showed extensive cell death and detachment by 96 hr and, hence, were not analyzed. Finally, using the E gene as a readout, we asked if ALO models could be used as platforms for preclinical drug screens. As a proof of concept, we tested the efficacy of nucleoside analog N4-hydroxycytidine (NHC; EIDD-parent) and its derivative pro-drug, EIDD-2801; both have been shown to inhibit viral replication, in vitro and in SARS-CoV-2-challenged ferrets (Cox et al., 2021; Sheahan et al., 2020). ALO monolayers plated in 384-wells were pretreated for 4 hr with the compounds or DMSO (control) prior to infection and assessed at 48 hpi for the abundance of E gene in the monolayers. Both compounds effectively reduced the viral titer in a dose-dependent manner (Figure 3I), and the pro-drug derivative showed a better efficacy, as shown previously.

Taken together, these findings show that sustained viral infectivity is best simulated in monolayers that resemble the proximal mucociliary epithelium, that is, 2D monolayers of lung organoids grown as ALI models and the primary airway epithelia. Because prior studies conducted in patient-derived airway cells (Hou et al., 2020) mirror what we see in our monolayers, we conclude that proximal airway cells within our mixed-cellular model appear to be sufficient to model viral infectivity in COVID-19. Findings also validate optimized protocols for the adaptation of ALO monolayers in miniaturized 384-well formats for use in high-throughput drug screens.

### Differentiated 2D monolayers show that host immune response is higher in distal than proximal epithelia

Next, we asked if the newly generated lung models accurately recapitulate the host immune response in COVID-19. To this end, we analyzed the infected ALO monolayers (both the submerged and ALI variants) as well as the airway epithelial (HSAEpC) and AT2 monolayers by RNA seq and compared them all against the transcriptome profile of lungs from deceased COVID-19 patients. We did this analysis in two steps of reciprocal comparisons: (i) The actual human disease-derived gene signature was assessed for its ability to distinguish infected from uninfected disease models (in Figure 4). (ii) The ALO model-derived gene signature was assessed for its ability to distinguish healthy from diseased patient samples (in Figure 5). A publicly available dataset (GSE151764) Nienhold et al., 2020, comprising lung transcriptomes from victims deceased either due to noninfectious causes (controls) or due to COVID-19, was first analyzed for differentially expressed genes (DEGs; Figure 4A and B). This cohort was chosen as a test cohort over others because it was the largest one available at the time of this study with appropriate postmortem control samples. DEGs showed an immunophenotype that was consistent with what is expected in viral infections (Figure 4C, Table 4, and Figure 4—figure supplement 1) and showed overrepresentation of pathways such as interferon, immune, and cytokine signaling (Figure 4D, Table 5, and Figure 4—figure supplement 2). DEG signatures and reactome pathways that were enriched in the test cohort were fairly representative of the host immune response observed in patient-derived respiratory samples in multiple other validation cohorts; the signature derived from the test cohort could consistently classify control (normal) samples from COVID-19-samples (receiver operating characteristics area under the curve [ROC AUC] 0.89–1.00 across the board; Figure 4E). The most notable finding is that the patient-derived signature was able to perfectly classify the EpCAM-sorted epithelial fractions from the bronchoalveolar lavage fluids of infected and healthy subjects (ROC AUC 1.00; GSE145926-Epithelium Liao et al., 2020), suggesting that the respiratory epithelium is a major site where the host immune response is detected in COVID-19. When compared to existing organoid models of COVID-19, we found that the patient-derived COVID-19-lung signature was able to perfectly classify infected vs. uninfected late passages (>50) of hiPSC-derived AT1/2 monolayers (GSE155241) Han et al., 2020a and infected vs. uninfected liver and pancreatic organoids (Figure 4F). The COVID-19-lung signatures failed to classify commonly used respiratory models, for example, A549 cells and bronchial organoids, as well as intestinal organoids (Figure 4F). A similar analysis on our own lung models revealed that the COVID-19-lung signature was induced in submerged monolayers with distal-predominant AT2→AT1 differentiation, but not in the proximal-predominant ALI model (ROC AUC 1.00 and 0.50, respectively; Figure 4G). The ALI model and the small airway epithelia, both models that mimic the airway epithelia (and lack alveolar pneumocytes; see Figure 3B), failed to mount the patient-derived immune signatures (Figure 4H, left). These findings suggested that the presence of alveolar pneumocytes is critical for emulating host response. To our surprise, induction of the COVID-19-lung signature also failed in hiPSC-derived AT2 monolayers (Figure 4H, right), indicating that AT2 cells are unlikely to be the source of such host response. These findings indicate that both proximal airway and AT2 cells, when alone, are insufficient to induce the host immune response that is encountered in the lungs of COVID-19 patient.

![Figure 4.](https://cdn.elifesciences.org/articles/66417/elife-66417-fig4-v2.jpg)

**Figure 4.:** (A–C) Publicly available RNA seq datasets (GSE151764) of lung autopsies from patients who were deceased due to COVID-19 or noninfectious causes (healthy normal control) were analyzed for differential expression of genes (B). The differentially expressed genes (DEGs) are displayed as a heatmap labeled with selected genes in (C). See also Figure 4—figure supplement 1 for the same heatmap with all genes labeled. (D) Reactome-pathway analysis shows the major pathways up- or downregulated in the COVID-19-afflicted lungs. See also Figure 4—figure supplement 2 for visualization as hierarchical ReacFoam. (E) Bar plots display the ability of the DEGs in the test cohort (GSE151764) to classify human COVID-19 respiratory samples from four other independent cohorts. (F) Bar plots display the ability of the DEGs in the test cohort (GSE151764) to classify published in vitro models for SARS-CoV-2 infection where RNA seq datasets were either generated in this work or publicly available. (G, H) Bar (top) and violin (bottom) plots compare the relative accuracy of disease modeling in four in vitro models used in the current work, as determined by the induction of COVID-19 lung signatures in each model. (G) Monolayer (left) and air-liquid interphase (ALI) models (right) prepared using adult lung organoids (ALOs). (H) Primary human small airway epithelium (left) and hiPSC-derived AT2 monolayers (right). Table 6 lists details regarding the patient cohorts/tissue or cell types represented in each transcriptomic dataset.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/66417/elife-66417-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Publicly available RNA seq datasets (GSE151764) of lung autopsies from patients who were deceased due to COVID-19 or noninfectious causes (normal lung control) were analyzed for differential expression of genes and displayed as a heatmap.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/66417/elife-66417-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Reactome-pathway analysis of the differentially expressed genes shows the major pathways upregulated in COVID-19-affected lungs. Top: visualization as flattened (left) and hierarchical (right, insets) reactome. Bottom: visualization of the same data as tables with statistical analysis indicative of the degree of pathway enrichment.

![Figure 5.](https://cdn.elifesciences.org/articles/66417/elife-66417-fig5-v2.jpg)

**Figure 5.:** (A–C) Adult lung organoid monolayers infected or not with SARS-CoV-2 were analyzed by RNA seq and differential expression analysis. Differentially expressed genes (DEGs; B) are displayed as a heatmap in (C). While only selected genes are labeled in panel (C) (which represent overlapping DEGs between our organoid model and publicly available COVID-19 lung dataset, GSE151764), the same heatmap is presented in Figure 5—figure supplement 1 with all genes labeled. (D) Reactome-pathway analysis shows the major pathways upregulated in SARS-CoV-2-infected lung organoid monolayers. See also Figure 5—figure supplement 2 for visualization as hierarchical ReacFoam. (E) A Venn diagram showing overlaps in DEGs between model (current work; B) and disease (COVID-19 lung dataset, GSE151764; Figure 4). (F) Bar plots display the ability of the DEGs in infected lung monolayers to classify human normal vs. COVID-19 respiratory samples from five independent cohorts. (G–I) Bar (top) and violin (bottom) plots compare the accuracy of disease modeling in three publicly available human lung datasets, as determined by the significant induction of the DEGs that were identified in the SARS-CoV-2-challenged monolayers. See also Table 6, which enlists details regarding the patient cohorts/tissue or cell types represented in each transcriptomic dataset.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/66417/elife-66417-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Adult lung organoid (ALO)-derived grown in transwells as submerged monolayers were infected or not with SARS-CoV-2 were analyzed by RNA seq and differential expression analysis. Differentially expressed genes are displayed as a heatmap.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/66417/elife-66417-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** Reactome-pathway analysis of the differentially expressed genes shows the major pathways upregulated in SARS-CoV-2-infected lung organoid monolayers. Top: visualization as flattened (left) and hierarchical (right, insets) ReacFoam. Bottom: visualization of the same data as tables with statistical analysis indicative of the degree of pathway enrichment.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/66417/elife-66417-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** (A) Venn diagrams show the number of overlapping and nonoverlapping DEGs (both up- and downregulated genes) between our organoid model and four human COVID-19 patient-derived samples (left). GSE151764 represents postmortem COVID-19 and normal lung tissues; GSE156063 represents upper airway samples from patients with COVID-19; GSE145926 represents sorted epithelial population from bronchoalveolar lavage fluid (BALF) derived from patients with varying severity of COVID-19; GSE157526 represents tracheal-bronchial cells infected with SARS-Cov2. (B) Venn diagrams as in (A), comparing a publicly available SARS-Cov2-infected human lung organoid model (GSE160435) and the same four human COVID-19 respiratory cohorts as in (A). (C) Venn diagrams show the DEGs between our organoid model and the publicly available lung organoid model. The comparison was carried out by calculating the percentage of the common up/down DEGs represented within the total up/down DEG for the two models in each Venn diagram.

**Table 4.**
 Upregulated genes and pathways: healthy vs COVID-19 lung (GSE151764).


<table>
  <thead>
    <tr>
      <th>Genes</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>BRCA2</td>
      <td>XAGE1B</td>
      <td>CDK1</td>
      <td>SNAI2</td>
      <td>CXCL11</td>
    </tr>
    <tr>
      <td>CYBB</td>
      <td>CCR5</td>
      <td>GBP1</td>
      <td>IFITM1</td>
      <td>IFI27</td>
    </tr>
    <tr>
      <td>KRT5</td>
      <td>CCR2</td>
      <td>HLA-G</td>
      <td>GZMB</td>
      <td>IFI35</td>
    </tr>
    <tr>
      <td>C1QB</td>
      <td>ALOX15B</td>
      <td>IDO1</td>
      <td>CD163</td>
      <td>TDO2</td>
    </tr>
    <tr>
      <td>FCGR1A</td>
      <td>CMKLR1</td>
      <td>ISG20</td>
      <td>CD38</td>
      <td>GZMA</td>
    </tr>
    <tr>
      <td>IL10</td>
      <td>MX1</td>
      <td>LAG3</td>
      <td>BST2</td>
      <td>OAS3</td>
    </tr>
    <tr>
      <td>IL6</td>
      <td>TNFRSF17</td>
      <td>MAD2L1</td>
      <td>BUB1</td>
      <td>POU2AF1</td>
    </tr>
    <tr>
      <td>CD44</td>
      <td>CCR1</td>
      <td>CXCL9</td>
      <td>CCL20</td>
      <td>CXCL13</td>
    </tr>
    <tr>
      <td>CD276</td>
      <td>CXCR3</td>
      <td>MKI67</td>
      <td>CCNB2</td>
      <td>GNLY</td>
    </tr>
    <tr>
      <td>DMBT1</td>
      <td>SLAMF8</td>
      <td>IFIT2</td>
      <td>TNFSF18</td>
      <td>IFIT3</td>
    </tr>
    <tr>
      <td>DDX58</td>
      <td>IL21</td>
      <td>IFIT1</td>
      <td>ISG15</td>
      <td>TOP2A</td>
    </tr>
    <tr>
      <td>TNFAIP8</td>
      <td>FOXM1</td>
      <td>CXCL10</td>
      <td>CDKN3</td>
      <td>LILRB1</td>
    </tr>
    <tr>
      <td>LAMP3</td>
      <td>IFIH1</td>
      <td>IRF4</td>
      <td>C1QA</td>
      <td>HERC6</td>
    </tr>
    <tr>
      <td>KIAA0101</td>
      <td>IFI6</td>
      <td>PSMB9</td>
      <td>OAS1</td>
      <td>TNFSF13B</td>
    </tr>
    <tr>
      <td>MELK</td>
      <td>PDCD1LG2</td>
      <td>CCL18</td>
      <td>OAS2</td>
      <td>IFI44L</td>
    </tr>
    <tr>
      <td>Pathways</td>
      <td></td>
      <td></td>
      <td></td>
      <td>STAT1</td>
    </tr>
    <tr>
      <td>Name</td>
      <td>p-value</td>
      <td>FDR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Interferon signaling</td>
      <td>1.11E-16</td>
      <td>1.11E-14</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Interferon alpha/beta signaling</td>
      <td>1.11E-16</td>
      <td>1.11E-14</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Cytokine signaling in immune system</td>
      <td>1.11E-16</td>
      <td>1.11E-14</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Immune ssystem</td>
      <td>1.11E-16</td>
      <td>1.11E-14</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Interleukin-10 signaling</td>
      <td>9.85E-13</td>
      <td>7.88E-11</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Interferon gamma signaling</td>
      <td>9.26E-12</td>
      <td>6.11E-10</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemokine receptors bind chemokines</td>
      <td>1.08E-10</td>
      <td>6.17E-09</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Signaling by interleukins</td>
      <td>6.81E-09</td>
      <td>3.41E-07</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Insulin-like growth factor-2 mRNA binding proteins (IGF2BPs/IMPs/VICKZs) bind RNA</td>
      <td>1.27E-07</td>
      <td>0.000005581122619</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Antiviral mechanism by IFN-stimulated genes</td>
      <td>0.000001933058349</td>
      <td>0.00007732233398</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CD163 mediating an anti-inflammatory response</td>
      <td>0.000007798676169</td>
      <td>0.0002807523421</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>OAS antiviral response</td>
      <td>0.00001020870997</td>
      <td>0.0003368874291</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide ligand-binding receptors</td>
      <td>0.00001714057687</td>
      <td>0.0005142173062</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Interleukin-4 and Interleukin-13 signaling</td>
      <td>0.0001014948661</td>
      <td>0.002841856252</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Cyclin A/B1/B2-associated events during G2/M transition</td>
      <td>0.0001887816465</td>
      <td>0.00490832281</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>G0 and early G1</td>
      <td>0.0003607121838</td>
      <td>0.009017804596</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Interleukin-6 signaling</td>
      <td>0.0004656678444</td>
      <td>0.01071036042</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>ISG15 antiviral mechanism</td>
      <td>0.0008313991988</td>
      <td>0.01745938317</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Regulation of APC/C activators between G1/S and early anaphase</td>
      <td>0.0008313991988</td>
      <td>0.01745938317</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Polo-like kinase-mediated events</td>
      <td>0.001110506513</td>
      <td>0.02221013026</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>APC/C-mediated degradation of cell cycle proteins</td>
      <td>0.001308103581</td>
      <td>0.02354586446</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Regulation of mitotic cell cycle</td>
      <td>0.001308103581</td>
      <td>0.02354586446</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>G2/M DNA replication checkpoint</td>
      <td>0.001750156332</td>
      <td>0.02975265764</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Class A/1 (rhodopsin-like receptors)</td>
      <td>0.002355063045</td>
      <td>0.03537666782</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Interleukin-6 family signaling</td>
      <td>0.002358444521</td>
      <td>0.03537666782</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>TNFs bind their physiological receptors</td>
      <td>0.002358444521</td>
      <td>0.03537666782</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Table 5.**
 Downregulated genes and pathways: healthy vs COVID-19 lung (GSE151764).


<table>
  <thead>
    <tr>
      <th>Genes</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
    <tr>
      <th>CX3CR1</th>
      <th>JAML</th>
      <th>KLRB1</th>
      <th>GRAP2</th>
      <th>CD226</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ARG1</td>
      <td>CX3CR1</td>
      <td>LY9</td>
      <td>MMP9</td>
      <td>CD160</td>
    </tr>
    <tr>
      <td>MPO</td>
      <td>HLA-DQB2</td>
      <td>CCL17</td>
      <td>RORC</td>
      <td>FOXP3</td>
    </tr>
    <tr>
      <td>IL2</td>
      <td>TNFRSF9</td>
      <td>CCL22</td>
      <td>CCR4</td>
      <td>CRTAM</td>
    </tr>
    <tr>
      <td>BCL2</td>
      <td>CXCR5</td>
      <td>TCF7</td>
      <td>IRS1</td>
      <td>CCR6</td>
    </tr>
    <tr>
      <td>CA4</td>
      <td>CD1C</td>
      <td>CXCR4</td>
      <td>ITK</td>
      <td>CEACAM8</td>
    </tr>
    <tr>
      <td>IGF1R</td>
      <td>CD69</td>
      <td>CD83</td>
      <td>KLRG1</td>
      <td>PTGS2</td>
    </tr>
    <tr>
      <td>Pathways</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Name</td>
      <td>p-value</td>
      <td>FDR</td>
    </tr>
    <tr>
      <td>Chemokine receptors bind chemokines</td>
      <td>2.85E-11</td>
      <td>4.98E-09</td>
    </tr>
    <tr>
      <td>Immune system</td>
      <td>1.25E-10</td>
      <td>1.09E-08</td>
    </tr>
    <tr>
      <td>Interleukin-4 and interleukin-13 signaling</td>
      <td>2.82E-09</td>
      <td>1.64E-07</td>
    </tr>
    <tr>
      <td>RUNX1 and FOXP3 control the development of regulatory T lymphocytes (Tregs)</td>
      <td>4.31E-07</td>
      <td>0.00001853717999</td>
    </tr>
    <tr>
      <td>Peptide ligand-binding receptors</td>
      <td>6.71E-07</td>
      <td>0.00002348305743</td>
    </tr>
    <tr>
      <td>Signaling by Interleukins</td>
      <td>0.000001503658493</td>
      <td>0.0000436060963</td>
    </tr>
    <tr>
      <td>Cytokine signaling in Immune system</td>
      <td>0.00002606505855</td>
      <td>0.0006516264636</td>
    </tr>
    <tr>
      <td>Dectin-1-mediated noncanonical NF-kB signaling</td>
      <td>0.00008640543215</td>
      <td>0.001814514075</td>
    </tr>
    <tr>
      <td>Immunoregulatory interactions between a lymphoid and a non-lymphoid cell</td>
      <td>0.0001083388675</td>
      <td>0.002058438482</td>
    </tr>
    <tr>
      <td>Class A/1 (rhodopsin-like receptors)</td>
      <td>0.0001833048828</td>
      <td>0.003116183008</td>
    </tr>
    <tr>
      <td>Interleukin-10 signaling</td>
      <td>0.0002366961934</td>
      <td>0.0035504429</td>
    </tr>
    <tr>
      <td>RUNX3 regulates immune response and cell migration</td>
      <td>0.0005791814113</td>
      <td>0.007747184934</td>
    </tr>
    <tr>
      <td>Extra-nuclear estrogen signaling</td>
      <td>0.0005959373026</td>
      <td>0.007747184934</td>
    </tr>
    <tr>
      <td>BH3-only proteins associate with and inactivate anti-apoptotic BCL-2 members</td>
      <td>0.0006992547523</td>
      <td>0.008391057028</td>
    </tr>
    <tr>
      <td>CLEC7A (Dectin-1) signaling</td>
      <td>0.0008228035145</td>
      <td>0.00905083866</td>
    </tr>
    <tr>
      <td>Generation of second messenger molecules</td>
      <td>0.001171991908</td>
      <td>0.01171991908</td>
    </tr>
    <tr>
      <td>Innate immune system</td>
      <td>0.001676404092</td>
      <td>0.01572360367</td>
    </tr>
    <tr>
      <td>GPCR ligand binding</td>
      <td>0.001747067074</td>
      <td>0.01572360367</td>
    </tr>
    <tr>
      <td>Adaptive immune system</td>
      <td>0.002059835991</td>
      <td>0.01853852391</td>
    </tr>
    <tr>
      <td>Estrogen-dependent nuclear events downstream of ESR-membrane signaling</td>
      <td>0.00467005583</td>
      <td>0.03736044664</td>
    </tr>
    <tr>
      <td>C-type lectin receptors (CLRs)</td>
      <td>0.00545804495</td>
      <td>0.0436643596</td>
    </tr>
    <tr>
      <td>Transcriptional regulation by RUNX3</td>
      <td>0.008124332599</td>
      <td>0.05687032819</td>
    </tr>
    <tr>
      <td>BMAL1:CLOCK, NPAS2 activates circadian gene expression</td>
      <td>0.009518272709</td>
      <td>0.06662790896</td>
    </tr>
    <tr>
      <td>ESR-mediated signaling</td>
      <td>0.01207376237</td>
      <td>0.08451633662</td>
    </tr>
    <tr>
      <td>Transcriptional regulation by RUNX1</td>
      <td>0.01288156371</td>
      <td>0.08786708747</td>
    </tr>
    <tr>
      <td>TCR signaling</td>
      <td>0.01464451458</td>
      <td>0.08786708747</td>
    </tr>
  </tbody>
</table>

Next, we analyzed the datasets from our ALO monolayers for DEGs when challenged with SARS-COV-2 (Figure 5A,B). Genes and pathways upregulated in the infected lung organoid-derived monolayer models (Figure 5—figure supplements 1–2) overlapped significantly with those that were upregulated in the COVID-19 lung signature (compare Figure 4C,D with Figure 5C,D, Table 6, Table 7, Table 8). We observed only a partial overlap (ranging from ~22–55% across various human datasets; Figure 5—figure supplement 3) in upregulated genes and no overlaps among downregulated genes between model and disease (COVID-19; Figure 5E). Because the degree of overlap was even lesser (ranging from ~10 to 25% across various human datasets; Figure 5—figure supplement 3) in the case of another publicly released model (GSE160435) (Mulay et al., 2020), these discrepancies between the model and the actual disease likely reflect the missing stromal and immune components in our organoid monolayers. Regardless of these missing components, the model-derived DEG signature was sufficient to consistently and accurately classify diverse cohorts of patient-derived respiratory samples (ROC AUC ranging from 0.88 to 1.00; Figure 5F); the model-derived DEG signature was significantly induced in COVID-19 samples compared to normal controls (Figure 5G,H). Most importantly, the model-derived DEG signature was significantly induced in the epithelial cells recovered from bronchoalveolar lavage (Figure 5I).

**Table 6.**
 The list of GSE numbers used in the figures.


<table>
  <thead>
    <tr>
      <th>GSE#</th>
      <th>Cell type/tissue</th>
      <th>References</th>
      <th>Figure</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GSE132914</td>
      <td>Tissue from idiopathic pulmonary fibrosis subjects and donor controls</td>
      <td>PMID:32991815</td>
      <td>Figure 1A</td>
    </tr>
    <tr>
      <td>GSE151764</td>
      <td>COVID-19 and normal lung tissue post-mortem</td>
      <td>PMID:33033248</td>
      <td>Figure 4A–E, Figure 5E–G</td>
    </tr>
    <tr>
      <td>GSE155241</td>
      <td>hPSC lung organoids and colon organoids infected with SARS-CoV-2</td>
      <td>PMID:33116299</td>
      <td>Figure 4E,F, Figure 6D</td>
    </tr>
    <tr>
      <td>GSE156063</td>
      <td>Upper airway of COVID-19 patients and other acute respiratory illnesses</td>
      <td>PMID:33203890</td>
      <td>Figure 4E, Figure 5F,H</td>
    </tr>
    <tr>
      <td>GSE147507</td>
      <td>A549 cells and bulk lung</td>
      <td>PMID:32416070; PMID:33782412</td>
      <td>Figure 4E,F, Figure 5F</td>
    </tr>
    <tr>
      <td>GSE145926</td>
      <td>Bronchoalveolar lavage fluid (BALF) immune cells from COVID-19 and healthy subjects</td>
      <td>PMID:32398875</td>
      <td>Figure 4E, Figure 5F,I</td>
    </tr>
    <tr>
      <td>GSE150819</td>
      <td>Human bronchial organoids</td>
      <td>From commercially available HBEpC</td>
      <td>Figure 4F, Figure 6C</td>
    </tr>
    <tr>
      <td>GSE149312</td>
      <td>Intestinal organoids infected with SARS-CoV or SARS-CoV-2</td>
      <td>PMID:32358202</td>
      <td>Figure 4F</td>
    </tr>
    <tr>
      <td>GSE151803</td>
      <td>hPSC-derived pancreatic and lung organoids infected with SARS-CoV-2</td>
      <td>No publication yet</td>
      <td>Figure 4F</td>
    </tr>
    <tr>
      <td>GSE153940</td>
      <td>Vero E6 control or SARS-CoV-2-infected cells</td>
      <td>PMID:32707573</td>
      <td>Figure 6B</td>
    </tr>
    <tr>
      <td>GSE153218</td>
      <td>SARS-CoV-2-infected bronchoalveolar cells derived from organoids grown using progenitor cells from human fetal lung but tip (LBT).</td>
      <td>PMID:33283287</td>
      <td>Figure 6H</td>
    </tr>
  </tbody>
</table>

**Table 7.**
 Upregulated genes and pathways: uninfected vs infected (48 hpi) lung organoid monolayers.


<table>
  <thead>
    <tr>
      <th>Genes</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>IFI35</td>
      <td>EPSTI1</td>
      <td>AMIGO2</td>
      <td>IFITM2</td>
    </tr>
    <tr>
      <td>SLC4A11</td>
      <td>CMPK2</td>
      <td>WARS1</td>
      <td>FAAP100</td>
    </tr>
    <tr>
      <td>APOL1</td>
      <td>OASL</td>
      <td>IFI27</td>
      <td>ISG15</td>
    </tr>
    <tr>
      <td>OAS3</td>
      <td>IFI44L</td>
      <td>CD14</td>
      <td>SLC35F6</td>
    </tr>
    <tr>
      <td>IFIT3</td>
      <td>IFI44</td>
      <td>SAMD9L</td>
      <td></td>
    </tr>
    <tr>
      <td>IFIT2</td>
      <td>PARP9</td>
      <td>SRP9P1</td>
      <td></td>
    </tr>
    <tr>
      <td>Pathways</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Name</td>
      <td>p-value</td>
      <td>FDR</td>
    </tr>
    <tr>
      <td>Interferon signaling</td>
      <td>1.11E-16</td>
      <td>4.22E-15</td>
    </tr>
    <tr>
      <td>Interferon alpha/beta signaling</td>
      <td>1.11E-16</td>
      <td>4.22E-15</td>
    </tr>
    <tr>
      <td>Cytokine signaling in Immune system</td>
      <td>1.15E-10</td>
      <td>2.89E-09</td>
    </tr>
    <tr>
      <td>Immune system</td>
      <td>0.000002540114879</td>
      <td>0.00004826218271</td>
    </tr>
    <tr>
      <td>OAS antiviral response</td>
      <td>0.0004764545663</td>
      <td>0.007146818495</td>
    </tr>
    <tr>
      <td>Antiviral mechanism by IFN-stimulated genes</td>
      <td>0.001033347261</td>
      <td>0.01240016713</td>
    </tr>
    <tr>
      <td>Interferon gamma signaling</td>
      <td>0.001889694619</td>
      <td>0.02078664081</td>
    </tr>
    <tr>
      <td>Transfer of LPS from LBP carrier to CD14</td>
      <td>0.006318772245</td>
      <td>0.05686895021</td>
    </tr>
    <tr>
      <td>TRIF-mediated programmed cell death</td>
      <td>0.02091267586</td>
      <td>0.1656073329</td>
    </tr>
    <tr>
      <td>MyD88 deficiency (TLR2/4)</td>
      <td>0.03733748271</td>
      <td>0.1656073329</td>
    </tr>
    <tr>
      <td>IRAK2-mediated activation of TAK1 complex upon TLR7/8 or 9 stimulation</td>
      <td>0.03733748271</td>
      <td>0.1656073329</td>
    </tr>
    <tr>
      <td>TRAF6-mediated induction of TAK1 complex within TLR4 complex</td>
      <td>0.03937173812</td>
      <td>0.1656073329</td>
    </tr>
    <tr>
      <td>IRAK4 deficiency (TLR2/4)</td>
      <td>0.03937173812</td>
      <td>0.1656073329</td>
    </tr>
    <tr>
      <td>Activation of IRF3/IRF7 mediated by TBK1/IKK epsilon</td>
      <td>0.04140183322</td>
      <td>0.1656073329</td>
    </tr>
    <tr>
      <td>Caspase activation via death receptors in the presence of ligand</td>
      <td>0.04140183322</td>
      <td>0.1656073329</td>
    </tr>
    <tr>
      <td>IKK complex recruitment mediated by RIP1</td>
      <td>0.04948077476</td>
      <td>0.1855013265</td>
    </tr>
  </tbody>
</table>

**Table 8.**
 Downregulated genes and pathways: uninfected vs. infected (48 hpi) lung organoid monolayers.


<table>
  <tbody>
    <tr>
      <td>AC093392.1</td>
      <td>ARHGAP19</td>
      <td>HLA-V</td>
      <td>RN7SL718P</td>
    </tr>
    <tr>
      <td>MT-TV</td>
      <td>AC138969.3</td>
      <td>AC016766.1</td>
      <td></td>
    </tr>
    <tr>
      <td>Pathways</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Name</td>
      <td>p-value</td>
      <td>FDR</td>
      <td></td>
    </tr>
    <tr>
      <td>rRNA processing in the mitochondrion</td>
      <td>0.01892731246</td>
      <td>0.08366120773</td>
      <td></td>
    </tr>
    <tr>
      <td>tRNA processing in the mitochondrion</td>
      <td>0.02127149105</td>
      <td>0.08366120773</td>
      <td></td>
    </tr>
    <tr>
      <td>Mitochondrial translation termination</td>
      <td>0.04399155446</td>
      <td>0.08366120773</td>
      <td></td>
    </tr>
    <tr>
      <td>Mitochondrial translation elongation</td>
      <td>0.04399155446</td>
      <td>0.08366120773</td>
      <td></td>
    </tr>
    <tr>
      <td>Mitochondrial translation initiation</td>
      <td>0.04490921762</td>
      <td>0.08366120773</td>
      <td></td>
    </tr>
    <tr>
      <td>Mitochondrial translation</td>
      <td>0.04765767844</td>
      <td>0.08366120773</td>
      <td></td>
    </tr>
  </tbody>
</table>

Taken together, these cross-validation studies from disease to model (Figure 4) and vice versa (Figure 5) provide an objective assessment of the match between the host response in COVID-19 lungs and our submerged ALO monolayers. Such a match was not seen in the case of the other models, for example, the proximal airway-mimic ALI model, HSAEpC monolayer, or hiPSC-derived AT2 models. Because the submerged ALO monolayers contained both proximal airway epithelia (basal cells) and promoted AT2→AT1 differentiation, findings demonstrate that mixed cellular monolayers can mimic the host response in COVID-19. A subtractive analysis revealed that the cell type that is shared between models that showed induction of host response signatures [i.e., ALO submerged monolayers and GSE155241 (Han et al., 2020a; Figure 5F)] but is absent in models that do not show such response (hu bronchial organoids, small airway epi, ALI-model of ALO) is AT1. We conclude that distal differentiation from AT2→AT1, a complex process that comprises distinct intermediates (Choi et al., 2020), is essential for modeling the host immune response in COVID-19. Further experimental evidence is needed to directly confirm if and which intermediate states during the differentiation of AT2 to AT1 are essential for the immune response to COVID19.

### Both proximal and distal airway epithelia are required to mount the overzealous host response in COVID-19

We next asked which model best simulated the overzealous host immune response that has been widely implicated in fatal COVID-19 (Lowery et al., 2021; Lucas et al., 2020; Schultze and Aschenbrenner, 2021). To this end, we relied upon a recently described artificial intelligence (AI)-guided definition of the nature of the overzealous response in fatal COVID-19 (Sahoo et al., 2021). Using ACE2 as a seed gene, a 166-gene signature was identified and validated as an invariant immune response that was shared among all respiratory viral pandemics, including COVID-19 (Figure 6A). A subset of 20 genes within the 166-gene signature was subsequently identified as a determinant of disease severity/fatality; these 20 genes represented translational arrest, senescence, and apoptosis. These two signatures, referred to as ViP (166-gene) and severe ViP (20-gene) signatures, were used as a computational framework to first vet existing SARS-CoV-2 infection models that have been commonly used for therapeutic screens (Figure 6B–D). Surprisingly, we found that each model fell short in one way or another. For example, the Vero E6, which is a commonly used cultured cell model, showed a completely opposite response; instead of being induced, both the 166-gene and 20-gene ViP signatures were suppressed in infected Vero E6 monolayers (Figure 6B). Similarly, neither ViP signature was induced in the case of SARS-CoV-2-challenged human bronchial organoids (Suzuki, 2020) (Figure 6C). Finally, in the case of the hiPSC-derived AT1/2 organoids, which recapitulated the COVID-19-lung derived immune signatures (in Figure 4F), the 166-gene ViP signature was induced significantly (Figure 6D, top), but the 20-gene severity signature was not (Figure 6D, bottom). These findings show that none of the existing models capture the overzealous host immune response that has been implicated in a fatality.

![Figure 6.](https://cdn.elifesciences.org/articles/66417/elife-66417-fig6-v2.jpg)

**Figure 6.:** (A) Schematic summarizing the immune signatures identified based on ACE2-equivalent gene induction observed invariably in any respiratory viral pandemic. The 166-gene ViP signature captures the cytokine storm in COVID-19, whereas the 20-gene subset severe ViP signature is indicative of disease severity/fatality. (B–D) Publicly available RNA seq datasets from commonly used lung models, Vero E6 (B), human bronchial organoids (C), and hPSC-derived AT1/2 cell-predominant lung organoids are classified using the 166-gene ViP signature (top row) and 20-gene severity signature (bottom row). (E–G) RNA seq datasets generated in this work using either human small airway epithelial cells (E), adult lung organoids as submerged or air-liquid interphase (ALI) models (left and right, respectively, in F) and hiPSC-derived AT2 cells (G) were analyzed and visualized as in (B–D). (H) Publicly available RNA seq datasets from fetal lung organoid monolayers (Lamers et al., 2021) infected or not with SARS-CoV-2 were analyzed as in (B–D) for the ability of ViP signatures to classify infected (I) from uninfected (U) samples. Receiver operating characteristics area under the curve (ROC AUC) in all figure panels indicate the performance of a classification model using the ViP signatures. (I) Summary of findings in this work, its relationship to the observed clinical phases in COVID-19, and key aspects of modeling the same. Table 6 lists details regarding the patient cohorts/tissue or cell types represented in each transcriptomic dataset.

Our lung models showed that both the 166- and 20-gene ViP signatures were induced significantly in the submerged ALO-derived monolayers that had distal differentiation (Figure 6E, left), but not in the proximal-mimic ALI model (Figure 6E, right). Neither signatures were induced in monolayers of small airway epithelial cells (Figure 6F) or hiPSC-derived AT2 cells (Figure 6G). Finally, we analyzed a recently published lung organoid model that supports robust SARS-CoV-2 infection; this model was generated using multipotent SOX2+ SOX9+ lung bud tip (LBT) progenitor cells that were isolated from the canalicular stage of human fetal lungs (~16–17 weeks post-conception) (Lamers et al., 2021). Despite mixed cellularity (proximal and distal), this fetal lung organoid model failed to induce the ViP signatures (Sahoo et al., 2021) (Figure 6H). These findings indicate that despite having mixed cellular composition and the added advantage of being able to support robust viral replication (achieving ~5 log-fold increase in titers), the model lacks the signature host response that is seen in all human samples of COVID-19.

Taken together with our infectivity analyses, these findings demonstrate that although the proximal airway epithelia and AT2 cells may be infected, and as described by others (Dye et al., 2015; Hou et al., 2020), may be vital for mounting a viral response and for disease transmission, these cells alone cannot mount the overzealous host immune response that is associated with the fatal disease. Similarly, even though the alveolar pneumocytes, AT1 and AT2 cells, are sufficient to mount the host immune response, in the absence of proximal airway components, they too are insufficient to recapitulate the severe ViP signature that is characterized by cellular senescence and apoptosis. However, when both proximal and distal components are present, that is, basal, ciliated, and AT1 cells, the model mimicked the overzealous host immune response in COVID-19 (Figure 6I).

## Discussion

The most important discovery we report here is the creation of adult lung organoids that are complete with both proximal airway and distal alveolar epithelia; these organoids can not only be stably propagated and expanded in 3D cultures but also used as monolayers of mixed cellularity for modeling viral and host immune responses during respiratory viral pandemics. Furthermore, an objective analysis of this model and other existing SARS-CoV-2-infected lung models against patient-lung-derived transcriptomes showed that the model that most closely emulates the elements of viral infectivity, lung injury, and inflammation in COVID-19 is one that contained both proximal and distal alveolar signatures (Figure 6H), whereas the presence of just one or the other fell short.

There are three important impacts of this work. First, the successful creation of adult human lung organoids that are complete with both proximal and distal signatures has not been accomplished before. Previous works show the successful use of airway basal cells for organoid creationtion, but ensuring the completeness of the model with all other lung cells has been challenging to create (Nikolić and Rawlins, 2017). The multicellularity of the lung has been a daunting challenge that many experts have tried to recreate in vitro; in fact, the demand for perfecting such a model has always remained high, not just in the current context of the COVID-19 pandemic but also with the potential of future pandemics. We have provided evidence that the organoids that were created using our methodology retain proximal and distal cellularity throughout multiple passages and even within the same organoid. Although a systematic design of experiment (DoE) approach (Bukys et al., 2020) was not involved in getting to this desirable goal, a rationalized approach was taken. For example, a Wnt/R-spondin/Noggin-containing conditioned media was used as a source of the so-called ‘niche factors’ for any organoid growth (Sato and Clevers, 2015). This was supplemented with recombinant FGF7/10; FGF7 is known to help cell proliferation and differentiation and is required for normal branching morphogenesis (Padela et al., 2008), whereas FGF10 helps in cell maturation (Rabata et al., 2020) and in alveolar regeneration upon injury (Yuan et al., 2019). Together, they are likely to have directed the differentiation toward distal lung lineages (hence, the preservation of alveolar signatures). The presence of both distal alveolar and proximal ciliated cells was critical: proximal cells were required to recreate sustained viral infectivity, and the distal alveolar pneumocytes, in particular, the ability of AT2 cells to differentiate into AT1 pneumocytes was essential to recreate the host response. It is possible that the response is mediated by a distinct AT2-lineage population, that is, damage-associated transient progenitors (DATPs), which arise as intermediates during AT2→AT1 differentiation upon injury-induced alveolar regeneration (Choi et al., 2020). Although somewhat unexpected, the role of AT1 pneumocytes in mounting innate immune responses has been documented before in the context of bacterial pneumonia (Yamamoto et al., 2012; Wong and Johnson, 2013). In work (Huang et al., 2020) that was published during the preparation of this article, authors used long-term ALI models of hiPSC-derived AT2 monolayers (in growth conditions that inhibit AT2→AT1 differentiation, as we did here for our AT2 model) and showed that SARS-CoV-2 induces iAT2-intrinsic cytotoxicity and inflammatory response, but failed to induce type 1 interferon pathways (IFN α/β). It is possible that prolonged culture of iAT2 pneumocytes gives rise to some DATPs but cannot robustly do so in the presence of inhibitors of AT1 differentiation. This (spatially segregated viral and host immune response) is a common theme across many lung infections (including bacterial pneumonia and other viral pandemics (Hou et al., 2020; Taubenberger and Morens, 2008; Weinheimer et al., 2012; Chan et al., 2013) and hence, this mixed cellularity model is appropriate for use in modeling diverse lung infections and respiratory pandemics to come.

Second, among all the established lung models so far, ours features four key properties that are desirable whenever disease models are being considered for their use in HTP modes for rapid screening of candidate therapeutics and vaccines: (i) reproducibility, propagability, and scalability; (ii) cost-effectiveness; (iii) personalization; and (iv) modularity, with the potential to add other immune and nonimmune cell types to our multicellular complex lung model. We showed that the protocol we have optimized supports isolation, expansion, and propagability at least up to 12–15 passages (at the time of submission of this work), with documented retention of proximal and distal airway components up to P8 (by RNA seq). We noted some variability of cell types between patient to patient, and between early and late passages of ALOs, which is probably because of the heterogeneity of organoids isolated from patient’s lung specimens. Feasibility has also been established for scaling up and optimizing the conditions for them to be used in miniaturized 384-well infectivity assays. We also showed that the protocols for generating lung organoids could be reproduced in both genders, and regardless of the donor’s smoking status, consistency in outcome and growth characteristics was observed across all isolation attempts. The ALOs are also cost-effective; the need for exclusive reliance on recombinant growth factors was replaced at least in part with conditioned media from a commonly used cell line (L-WRN/ ATCC CRL-2647 cells). Such media has a batch-to-batch stable cocktail of Wnt, R-Spondin, and Noggin, and has been shown to improve reproducibility in the context of GI organoids in independent laboratories (VanDussen et al., 2019). By that token, our culture conditions may have also improved reproducibility. The major disadvantage, however, remains that the composition of the media is undefined. Because the model is propagable, repeated iPSC-reprogramming (another expensive step) is also eliminated, further cutting costs compared to many other models. As for personalization, our model is derived from adult lung stem cells from deep lung biopsies; each organoid line was established from one patient. By avoiding iPSCs or expanded potential stem cells (EPSCs), this model not only captures genetics but also retains organ-specific epigenetic programming in the lung, and hence, potentially additional programming that may occur in disease (such as in the setting of chronic infection, injury, inflammation, somatic mutations, etc.). The ability to replicate donor phenotype and genotype in vitro allows for potential use as preclinical human models for phase ‘0’ clinical trials. As for modularity, by showing that the 3D lung organoids could be used as polarized monolayers on transwells to allow infectious agents to access the apical surface (in this case, SARS-CoV-2), we demonstrate that the organoids have the potential to be reverse-engineered with additional components in a physiologically relevant spatially segregated manner: for example, immune and stromal cells can be placed in the lower chamber to model complex lung diseases that are yet to be modeled and have no cure (e.g., idiopathic pulmonary fibrosis, etc.).

Third, the value of the ALO models is further enhanced due to the availability of companion readouts/biomarkers (e.g., ViP signatures in the case of respiratory viral pandemics, or monitoring the E gene, or viral shedding, etc.) that can rapidly and objectively vet treatment efficacy based on set therapeutic goals. Of these readouts, the host response, as assessed by ViP signatures, is a key vantage point because an overzealous host response is what is known to cause fatality. Recently, a systematic review of the existing preclinical animal models revealed that most of the animal models of COVID-19 recapitulated mild patterns of human COVID-19; no severe illness associated with mortality was observed, suggesting a wide gap between COVID-19 in humans (Spagnolo et al., 2020) and animal models (Ehaideb et al., 2020). It is noteworthy that alternative models that effectively support viral replication, such as the proximal airway epithelium or iPSC-derived AT2 cells (analyzed in this work) or a fetal lung bud tip-derived organoid model recently described by others (Lamers et al., 2021), do not recapitulate the host response in COVID-19. The lung model we present here is distinct from all currently available other models (see Table 1) because of the confirmed presence of both proximal and distal airway cell types over successive passages, which is yet to be accomplished for adult lung organoid models. Another distinguishing feature of our model is the way we rigorously validated its usefulness in modeling COVID-19 via computational approaches. We confirmed, based on the gene expression changes upon SARS-CoV-2-challenge, that our model most closely recapitulates the human disease, that is, COVID-19. Analyses also pinpointed the importance of two factors that were critical in modeling COVID-19: (i) adult source and (ii) model completeness, with both proximal and distal airway cells. We conclude that the model revealed here, in conjunction with the ViP signatures described earlier (Sahoo et al., 2021), could serve as a preclinical model with companion diagnostics to identify drugs that target both the viral and host response in pandemics.

### Limitations of the study

Our adult stem-cell-derived lung organoids, complete with all epithelial cell types, can model COVID-19, but remains a simplified/rudimentary version compared to the adult human organ. While we successfully demonstrated the proximo-distal mixed cellular composition of the ALOs using four different approaches (flow cytometry, RNA seq, confocal immunofluorescence, and targeted qPCR) and showed that such mixed cellularity is preserved during prolonged culture, the exact cellular proportion was not assessed here. Single-cell sequencing and multiplexed profiling by flow cytometry are some of the approaches that can provide such in-depth characterization to assess cellular composition at baseline and track how such composition changes upon infection and injury. For instance, although the epithelial contributions to the host response are important, they alone cannot account for the response of the immune cells and the nonimmune stromal cells, and their crosstalk with the epithelium. Given that epithelial inflammation and damage is propagated by vicious forward-feedback loops of multicellular crosstalk, it is entirely possible that the epithelial signatures induced in infected ALO-derived monolayers are also only a fraction of the actual epithelial response mounted in vivo. Regardless of the missing components, what appears to be the case is that we already have a model that recapitulates approximately a quarter to half of the genes that are induced across diverse COVID-19-infected patient samples. This model can be further improved by the simultaneous addition of endothelial cells and immune cells to better understand the pathophysiological basis for DAD, microangiopathy, and even organizing fibrosis with loss of lung capacity that has been observed in many patients (Spagnolo et al., 2020); these insights should be valuable to fight some of the long-term sequelae of COVID-19. Future work with flow cytometry and cell sorting of our lung organoids would help us understand each cell type’s role in viral pathogenesis. Larger living biobanks of genotyped and phenotyped ALOs, representing donors of different age, ethnicity, predisposing conditions, and coexisting comorbidities, will advance our understanding of why SARS-CoV-2 and possibly other infectious agents may trigger different disease course in different hosts. Although we provide proof-of-concept studies in low-throughput mode demonstrating the usefulness of the ALOs as human preclinical models for screening therapeutics in phase ‘0’ trials, optimization for the same to be adapted in HTP mode was not attempted here.

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
      <td>Antibody</td>
      <td>Anti-ACE2 (mouse monoclonal)</td>
      <td>Santa Cruz</td>
      <td>Cat# sc390851RRID::AB_2861379</td>
      <td>IF (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-human ACE2 (rat monoclonal)</td>
      <td>BioLegend</td>
      <td>Cat# 375802RRID::AB_2860959</td>
      <td>IF (1:50)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-acetylated ɑ tubulin (mouse monoclonal)</td>
      <td>Santa Cruz</td>
      <td>Cat# sc23950RRID::AB_628409</td>
      <td>IF (1:500)FC (1:8000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-AQP5 (mouse monoclonal)</td>
      <td>Santa Cruz</td>
      <td>Cat# sc514022RRID::AB_2891066</td>
      <td>IF (1:100)FC (1:800)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-CC10 (mouse monoclonal)</td>
      <td>Santa Cruz</td>
      <td>Cat# sc365992RRID::AB_10915481</td>
      <td>IF (1:100)</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>DAPI</td>
      <td>Invitrogen</td>
      <td>Cat# D1306RRID::AB_2629482</td>
      <td>IF (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Recombinant anti-cytokeratin 5 (rabbit monoclonal)</td>
      <td>Abcam</td>
      <td>Cat# ab52635RRID::AB_869890</td>
      <td>IF (1:100)FC (1:8000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Recombinant anti-mucin 5AC (rabbit monoclonal)</td>
      <td>Abcam</td>
      <td>Cat# ab229451RRID::AB_2891067</td>
      <td>IF (1:150)FC (1:800)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-sodium potassium ATPase (rabbit monoclonal)</td>
      <td>Abcam</td>
      <td>Cat# ab76020RRID::AB_1310695</td>
      <td>IF (1:400)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-occludin (mouse monoclonal)</td>
      <td>Thermo Fisher</td>
      <td>Cat# OC-3F10RRID::AB_2533101</td>
      <td>IF (1:500)</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Phalloidin, Alexa Fluor 594</td>
      <td>Invitrogen</td>
      <td>Cat# A12381RRID:AB_2315633</td>
      <td>IF (1:500)</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Propidium iodide</td>
      <td>Invitrogen</td>
      <td>V13241</td>
      <td>FC (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>SARS-CoV/SARS-CoV-2 nucleocapsid antibody (mouse monoclonal)</td>
      <td>Sino Biological</td>
      <td>Cat# 40143-MM05RRID::AB_2827977</td>
      <td>IF (1:250)IHC (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-SARS spike glycoprotein (mouse monoclonal)</td>
      <td>Abcam</td>
      <td>Cat# ab273433RRID::AB_2891068</td>
      <td>IHC (1:250)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-SP-B (mouse monoclonal)</td>
      <td>Santa Cruz</td>
      <td>Cat# sc133143RRID::AB_2285686</td>
      <td>IF (1:100)FC (1:8000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-prosurfactant protein C (rabbit polyclonal)</td>
      <td>Abcam</td>
      <td>Cat# ab90716RRID::AB_10674024</td>
      <td>IF (1:150)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat anti-rat IgG H&amp;L secondary antibody, Alexa Flour 594</td>
      <td>Invitrogen</td>
      <td>Cat# A-11007RRID:AB_10561522</td>
      <td>IF (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat anti-rabbit IgG H&amp;L secondary antibody, Alexa Fluor 594</td>
      <td>Invitrogen</td>
      <td>Cat# A-11012RRID:AB_2534079</td>
      <td>IF (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat anti-mouse IgG H&amp;L secondary antibody, Alexa Fluor 488</td>
      <td>Invitrogen</td>
      <td>Cat# A-11011RRID:AB_143157</td>
      <td>IF (1:500)FC (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat anti-rabbit IgG H&amp;L secondary antibody, Alexa Fluor 488</td>
      <td>Abcam</td>
      <td>Cat# ab150077RRID:AB_2630356</td>
      <td>FC (1:1000)</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Countess II Automated Cell Counter</td>
      <td>Thermo Fisher Scientific</td>
      <td>AMQAX1000</td>
      <td>Section‘The preparation of lung organoid-derived monolayers’</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Epithelial Volt-Ohm (TEER) Meter</td>
      <td>Millipore</td>
      <td>MERS00002</td>
      <td>Section ‘Permeability of lung monolayer using FITC-dextran’</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Leica TCS SPE Confocal</td>
      <td>Leica Microsystems</td>
      <td>TCS SPE</td>
      <td>Section‘Immunofluorescence’</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Power Pressure Cooker XL</td>
      <td>Tristar Products</td>
      <td></td>
      <td>Section‘Immunohistochemistry’</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Canon Rebel XS DLSR</td>
      <td>Canon</td>
      <td></td>
      <td>Figure 2—figure supplement 1</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>MiniAmp Plus Thermal Cycler</td>
      <td>Applied Biosystems</td>
      <td>Cat# A37835</td>
      <td>Section‘Quantitative (q)RT-PCR’</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>QuantStudio5</td>
      <td>Applied Biosystems</td>
      <td>Cat# A28140 RRID:SCR_020240</td>
      <td>Section‘Quantitative (q)RT-PCR’</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Light Microscope (brightfield images)</td>
      <td>Carl Zeiss LLC</td>
      <td>Axio Observer, Inverted; 491917-0001-000</td>
      <td>Figure 2—figure supplement 1</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Spark 20 M Multimode Microplate Reader</td>
      <td>Tecan</td>
      <td></td>
      <td>Section‘Permeability of lung monolayer using FITC-dextran’</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Guava easyCyte Benchtop Flow Cytometer</td>
      <td>Millipore</td>
      <td>Guava easyCyte 62L</td>
      <td>Section‘The characterization of lung cell types using flow cytometry’</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ImageJ</td>
      <td>ImageJ</td>
      <td>RRID:SCR_003070</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GraphPad Prism</td>
      <td>GraphPad Prism</td>
      <td>RRID:SCR_002798</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>LAS AF Software</td>
      <td>LAS AF Software</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>QuantStudio Design &amp; Analysis Software</td>
      <td>QuantStudio Design &amp; Analysis Software</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>CIBERSORTx</td>
      <td>CIBERSORTx</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>FlowJo</td>
      <td>FlowJo V10, BD BioSciences</td>
      <td>RRID:SCR_008520</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Zinc formalin</td>
      <td>Fisher Scientific</td>
      <td>Cat# 23-313096</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Xylene</td>
      <td>VWR</td>
      <td>Cat# XX0060-4</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Hematoxylin</td>
      <td>Sigma-Aldrich Inc</td>
      <td>Cat# MHS1</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Ethanol</td>
      <td>Koptec</td>
      <td>Cat# UN1170</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Sodium citrate</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# W302600</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DAB (10×)</td>
      <td>Thermo Fisher</td>
      <td>Cat# 1855920</td>
      <td>(1:10)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Stable peroxidase substrate buffer (10×)</td>
      <td>Thermo Fisher</td>
      <td>Cat# 34062</td>
      <td>(1:10)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>3%hydrogen peroxide</td>
      <td>Target</td>
      <td>Cat# 245-07-3628</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Horse serum</td>
      <td>Vector Labs</td>
      <td>Cat# 30022</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>HRP Horse Anti-Rabbit IgG Polymer Detection Kit</td>
      <td>Vector Laboratories</td>
      <td>Cat# MP-7401</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Paraformaldehyde 16% Solution, EM Grade</td>
      <td>Electron Microscopy Sciences</td>
      <td>Cat# 15710</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>100%methanol</td>
      <td>Supelco</td>
      <td>Cat# MX0485</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Glycine</td>
      <td>Fisher Scientific</td>
      <td>Cat# BP381-5</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Bovine serum albumin</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# A9647-100G</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Triton-X 100</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# X100-500ML</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>ProLong Glass</td>
      <td>Invitrogen</td>
      <td>Cat# P36984</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Nail Polish (Rapid Dry)</td>
      <td>Electron Microscopy Sciences</td>
      <td>Cat# 72180</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Gill Modified Hematoxylin (Solution II)</td>
      <td>Millipore Sigma</td>
      <td>Cat# 65066-85</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>HistoGel</td>
      <td>Thermo Scientific</td>
      <td>Cat# HG4000012</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>TrypLE Select</td>
      <td>Thermo Scientific</td>
      <td>Cat# 12563-011</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Advanced DMEM/F-12</td>
      <td>Thermo Scientific</td>
      <td>Cat# 12634-010</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>HEPES buffer</td>
      <td>Life Technologies</td>
      <td>Cat# 15630080</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Glutamax</td>
      <td>Thermo Scientific</td>
      <td>Cat# 35050-061</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Penicillin-streptomycin</td>
      <td>Thermo Scientific</td>
      <td>Cat# 15140-122</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Collagenase type I</td>
      <td>Thermo Scientific</td>
      <td>Cat# 17100-017</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Matrigel</td>
      <td>Corning</td>
      <td>Cat# 354234</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>B-27</td>
      <td>Thermo Scientific</td>
      <td>Cat# 17504044</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>N-acetyl-L-cysteine</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# A9165</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Nicotinamide</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# N0636</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>FGF-7 (KGF)</td>
      <td>PeproTech</td>
      <td>Cat# 100-19-50ug</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>FGF10</td>
      <td>PeproTech</td>
      <td>Cat# 100-26-50ug</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>A-83-01</td>
      <td>Bio-Techne Sales Corp.</td>
      <td>Cat# 2939/50</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>SB202190</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# S7067-25MG</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Y-27632</td>
      <td>R&amp;D Systems</td>
      <td>Cat# 1254/50</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DPBS</td>
      <td>Thermo Scientific</td>
      <td>Cat# 14190-144</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Ultrapure Water</td>
      <td>Invitrogen</td>
      <td>Cat# 10977-015</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>EDTA</td>
      <td>Thermo Scientific</td>
      <td>Cat# AM9260G</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Hydrocortisone</td>
      <td>STEMCELL Technologies</td>
      <td>Cat# 7925</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Heparin</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# H3149</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>PneumaCult Ex-Plus Medium</td>
      <td>STEMCELL Technologies</td>
      <td>Cat# 5040</td>
      <td>Section‘The preparation of lung organoid-derived monolayers’</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>PneumaCult ALI Medium</td>
      <td>STEMCELL Technologies</td>
      <td>Cat# 5001</td>
      <td>Section‘ALImodel of lung organoids’</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Goat serum</td>
      <td>Vector Laboratories</td>
      <td>Cat# MP-7401</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Fetal bovine serum</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# F2442-500ML</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Animal Component-Free Cell Dissociation Kit</td>
      <td>STEMCELL Technologies</td>
      <td>Cat# 5426</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Red Blood Cell Lysis Buffer</td>
      <td>Invitrogen</td>
      <td>Cat# 00-4333-57</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Cell Recovery Solution</td>
      <td>Corning</td>
      <td>Cat# 354253</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Sodium azide</td>
      <td>Fisher Scientific</td>
      <td>Cat# S227I-100</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Cyto-Fast Fix/Perm Buffer Set</td>
      <td>BioLegend</td>
      <td>Cat# 426803</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>FITC-dextran</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# FD10S</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Quick-RNA MicroPrep Kit</td>
      <td>Zymo Research</td>
      <td>Cat# R1051</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Quick-RNA MiniPrep Kit</td>
      <td>Zymo Research</td>
      <td>Cat#R1054</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Ethyl alcohol, pure</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# E7023</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>TRI Reagent</td>
      <td>Zymo Research</td>
      <td>Cat# R2050-1-200</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>2x SYBR Green qPCR Master Mix</td>
      <td>Bimake</td>
      <td>Cat# B21203</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qScript cDNA SuperMix</td>
      <td>Quanta Biosciences</td>
      <td>Cat# 95048</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Applied Biosystems TaqMan Fast Advanced Master Mix</td>
      <td>Thermo Scientific</td>
      <td>Cat# 4444557</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>18S, Hs99999901_s1</td>
      <td>Thermo Scientific</td>
      <td>Cat# 4331182</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>E_Sarbeco_F1 Forward Primer</td>
      <td>IDT</td>
      <td>Cat# 10006888</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>E_Sarbeco_R2 Reverse Primer</td>
      <td>IDT</td>
      <td>Cat# 10006890</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>E_Sarbeco_P1 Probe</td>
      <td>IDT</td>
      <td>Cat# 10006892</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>12-well Tissue Culture Plate</td>
      <td>CytoOne</td>
      <td>Cat# CC7682-7512</td>
      <td>Section‘Isolation and culture of human whole lung-derived organoids’</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Transwell Inserts (6.5 mm, 0.4µm pore size)</td>
      <td>Corning</td>
      <td>Cat# 3470</td>
      <td>Section‘The preparation of lung organoid-derived monolayers’</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Microscope Cover Glass (#1 Thickness) 24 × 50 mm</td>
      <td>VWR</td>
      <td>Cat# 16004-098</td>
      <td>Section‘Immunofluorescence’</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Microscope Cover Glass (#1 Thickness) 25 mm diameter</td>
      <td>Chemglass Life Sciences</td>
      <td>Cat# CLS-1760-025</td>
      <td>Section‘Immunofluorescence’</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Millicell EZ Slide 8-Well Chamber</td>
      <td>Millipore Sigma</td>
      <td>Cat# PEZGS0816</td>
      <td>Section‘Immunofluorescence’</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Trypan Blue Stain</td>
      <td>Invitrogen</td>
      <td>Cat# T10282</td>
      <td>(1:2)</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>70µm Cell Strainer</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# 22-363-548</td>
      <td>Section‘The preparation of lung organoid-derived monolayers’</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>100 µm Cell Strainer</td>
      <td>Corning</td>
      <td>Cat# 352360</td>
      <td>Section‘Isolation and culture of human whole lung-derived organoids’</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Noyes Spring Scissors – Angled</td>
      <td>Fine Science Tools</td>
      <td>Cat# 15013-12</td>
      <td>Section‘Isolation and culture of human whole lung-derived organoids’</td>
    </tr>
  </tbody>
</table>

### Detailed methods

#### Collection of human lung specimens for organoid isolation

To generate adult healthy lung organoids, fresh biopsy bites were prospectively collected after surgical resection of the lung by the cardiothoracic surgeon. Before collection of the lung specimens, each tissue was sent to a gross anatomy room where a pathologist cataloged the area of focus, and the extra specimens were routed to the research lab in Human Transport Media (HTM, Advanced DMEM/F-12, 10 mM HEPES, 1× Glutamax, 1× penicillin-streptomycin, 5 μM Y-27632) for cell isolation. Deidentified lung tissues obtained during surgical resection, which were deemed excess by clinical pathologists, were collected using an approved human research protocol (IRB# 101590; PI: Thistlethwaite). Isolation and biobanking of organoids from these lung tissues were carried out using an approved human research protocol (IRB# 190105: PI Ghosh and Das) that covers human subject research at the UC San Diego HUMANOID Center of Research Excellence (CoRE). For all the deidentified human subjects, information, including age, gender, and previous history of the disease, was collected from the chart following the rules of HIPAA and described in Table 3.

A portion of the same lung tissue specimen was fixed in 10% zinc-formalin for at least 24 hr followed by submersion in 70% EtOH until embedding in FFPE blocks.

#### Autopsy procedures for lung tissue collection from COVID-19-positive human subjects

The lung specimens from COVID-19-positive human subjects were collected through autopsy (the study was IRB exempt). All donations to this trial were obtained after telephone consent followed by written email confirmation by the next of kin/power of attorney per California state law (no in-person visitation could be allowed into our COVID-19 ICU during the pandemic). The team member followed the CDC guidelines for COVID19 and the autopsy procedures (CAP, 2020; CDC, 2020). Lung specimens were collected in 10% zinc-formalin and stored for 72 hr before processing for histology. Patient characteristics are listed in Table 3.

Autopsy #2 was a standard autopsy performed by anatomical pathology in the BSL3 autopsy suite. The patient expired and his family consented for autopsy. After 48 hr, the lungs were removed and immersion fixed whole in 10% formalin for 48 hr and then processed further. Lungs were only partially fixed at this time (about 50% fixed in thicker segments) and were sectioned into small 2–4 cm chunks and immersed in 10% formalin for further investigation.

Autopsy #4 and #5 were collected from rapid postmortem lung biopsies. The procedure was performed in the Jacobs Medical Center ICU (all of the ICU rooms have a pressure-negative environment, with air exhausted through HEPA filters [Biosafety Level 3 (BSL3)] for isolation of SARS-CoV-2 virus). Biopsies were performed 2–4 hr after patient expiration. The ventilator was shut off to reduce the aerosolization of viral particles at least 1 hr after the loss of pulse and before sample collection. Every team member had personal protective equipment in accordance with the university policies for procedures on patients with COVID-19 (N95 mask+ surgical mask, hairnet, full face shield, surgical gowns, double surgical gloves, booties). Lung biopsies were obtained after L-thoracotomy in the fifth intercostal space by the cardiothoracic surgery team. Samples were taken from the left upper lobe (LUL) and left lower lobe (LLL) and then sectioned further.

#### Isolation and culture of human whole lung-derived organoids

A previously published protocol was modified to isolate lung organoids from three human subjects (Sachs et al., 2019; Zhou et al., 2018). Briefly, normal human lung specimens were washed with PBS/4× penicillin-streptomycin and minced with surgical scissors. Tissue fragments were resuspended in 10 ml of wash buffer (Advanced DMEM/F-12, 10 mM HEPES, 1× Glutamax, 1× penicillin-streptomycin) containing 2 mg/ml Collagenase Type I (Thermo Fisher, USA) and incubated at 37°C for approximately 1 hr. During incubation, tissue pieces were sheared every 10 min with a 10 ml serological pipette and examined under a light microscope to monitor the progress of digestion. When 80–100% of single cells were released from connective tissue, the digestion buffer was neutralized with 10 ml wash buffer with added 2% fetal bovine serum; the suspension was passed through a 100 µm cell strainer and centrifuged at 200 rcf. Remaining erythrocytes were lysed in 2 ml red blood cell lysis buffer (Invitrogen) at room temperature for 5 min, followed by the addition of 10 ml of wash buffer and centrifugation at 200 rcf. Cell pellets were resuspended in cold Matrigel (Corning, USA) and seeded in 25 µl droplets on a 12-well tissue culture plate. The plate was inverted and incubated at 37°C for 10 min to allow complete polymerization of the Matrigel before the addition of 1 ml Lung Expansion Medium per well. Lung expansion media was prepared by modifying a media that was optimized previously for growing GI-organoids (50% conditioned media, prepared from L-WRN cells with Wnt3a, R-spondin, and Noggin, ATCC-CRL-3276) (Sayed et al., 2020c; Ghosh et al., 2020; Sayed et al., 2020a; Sayed et al., 2020b) with a proprietary cocktail from the HUMANOID CoRE containing B27, TGF-β receptor inhibitor, antioxidants, p38 MAPK inhibitor, FGF 7, FGF 10, and ROCK inhibitor. The lung expansion media was compared to alveolosphere media I (IMDM and F12 as the basal medium with B27, low concentration of KGF, monothioglycerol, GSK3 inhibitor, ascorbic acid, dexamethasone, IBMX, cAMP, and ROCK inhibitor) and II (F12 as the basal medium with added CaCl2, B27, low concentration of KGF, GSK3 inhibitor, TGF-β receptor inhibitor dexamethasone, IBMX, cAMP, and ROCK inhibitor) modified from previously published literature (Jacob et al., 2019; Yamamoto et al., 2017). Neither alvelosphere media contain any added Wnt3a, R-spondin, and Noggin. The composition of these media was developed either by fundamentals of adult stem cell-derived mixed epithelial cellularity in other organs (like the GI tract [Miyoshi and Stappenbeck, 2013; Sato et al., 2009; Sayed et al., 2020c]) or rationalized based on published growth conditions for proximal and distal airway components (Gotoh et al., 2014; Sachs et al., 2019; van der Vaart and Clevers, 2021). Organoids were maintained in a humidified incubator at 37°C/5% CO2, with a complete media change performed every 3 days. After the organoids reached confluency between 7 and 10 days, organoids were collected in PBS/0.5 mM EDTA and centrifuged at 200 rcf for 5 min. Organoids were dissociated in 1 ml trypLE Select (Gibco, USA) per well at 37°C for 4–5 min and mechanically sheared. Wash buffer was added at a 1:5, trypLE to wash buffer ratio. The cell suspension was subsequently centrifuged, resuspended in Matrigel, and seeded at a 1:5 ratio. Lung organoids were biobanked and passage 3–8 cells were used for experiments. Subculture was performed every 7–10 days.

#### The preparation of lung organoid-derived monolayers

Lung organoid-derived monolayers were prepared using a modified protocol of GI organoid-derived monolayers (Sayed et al., 2020c; Ghosh et al., 2020; Sayed et al., 2020a; Sayed et al., 2020b). Briefly, transwell inserts (6.5 mm diameter, 0.4 µm pore size, Corning) were coated in Matrigel diluted in cold PBS at a 1:40 ratio and incubated for 1 hr at room temperature. Confluent organoids were collected in PBS/EDTA on day 7 and dissociated into single cells in trypLE for 6–7 min at 37°C. Following enzymatic digestion, the cell suspension was mechanically sheared through vigorous pipetting with a 1000 µl pipette and neutralized with wash buffer. The suspension was centrifuged, resuspended in PneumaCult Ex-Plus Medium (StemCell, Canada), and passed through a 70 µm cell strainer. The coating solution was aspirated, and cells were seeded onto the apical membrane at 1.8E5 cells per transwell with 200 µl PneumaCult Ex-Plus media. 700 µl of PneumaCult Ex-Plus was added to the basal chamber. Cells were cultured over the course of 2–4 days. A media change of both the apical and basal chambers was performed every 24 hr.

### ALI model of lung organoids

Organoids were dissociated into single cells and expanded in T-75 flasks in PneumaCult Ex-Plus Medium until confluency was reached. Cells were dissociated in ACF Enzymatic Dissociation Solution (StemCell) for 6–7 min at 37°C and neutralized in equal volume ACF Enzyme Inhibition Solution (StemCell). Cells were seeded in the apical chamber of transwells at 3.3E4 cells per transwell in 200 µl of PneumaCult Ex-Plus Medium. 500 µl of PneumaCult Ex-Plus was added to the basal chamber. Media in both chambers was changed every other day until confluency was reached (~4 days). The media was completely removed from the apical chamber, and media in the basal chamber was replaced with ALI Maintenance Medium (StemCell). The media in the basal chamber was changed every 2 days. The apical chamber was washed with warm PBS every 5–7 days to remove accumulated mucus. Cells were cultured under ALI conditions for 21+ days until they completed differentiation into a pseudostratified mucociliary epithelium. To assess the integrity of the epithelial barrier, TEER was measured with an Epithelial Volt-Ohm Meter (Millicell, USA). The media was removed from the basal chamber, and wash media was added to both chambers. Cultures were equilibrated to 37°C before TEER values were measured. Final values were expressed as Ω·cm2 units and were calculated by multiplying the growth area of the membrane by the raw TEER value.

#### The culture of primary airway epithelial cells and iPSC-derived alveolar epithelial cells

Primary NHBE cells were obtained from Lonza and grown according to instructions. NHBE cells were cultured in T25 cell culture tissue flasks with PneumaCult-Ex Plus media (StemCell). Cells were seeded at ~100,000 cells/T25 flask and incubated at 37°C, 5% CO2. Once cells reached 70–80% confluency, they were dissociated using 0.25% Trypsin in dissociation media and plated in 24-well transwells (Corning). Primary human bronchial epithelial cells (HBEpC) and small airway epithelial cells (HSAEpC) were obtained from Cell Applications Inc The HBEpC and HSAEpC were cultured in human bronchial/tracheal epithelial cell media and small airway epithelial cell media, respectively, following the instructions of Cell Application.

Human iPSC-derived alveolar epithelial type 2 cells (iHAEpC2) were obtained from Cell Applications Inc and cultured in growth media (i536K-05, Cell Applications Inc) according to the manufacturer’s instructions. All the primary cells were used within early passages (5–6) to avoid any gradual disintegration of the airway epithelium with columnar epithelial structure and epithelial integrity.

#### The infection with SARS-Cov2

Lung organoid-derived monolayers or primary airway epithelial cells either in 384-well plates or in transwells were washed twice with antibiotic-free lung wash media. 1E5 PFU of SARS-CoV-2 strain USA-WA1/2020 (BEI Resources NR-52281) in complete DMEM was added to the apical side of the transwell and allowed to incubate for 24, 48, 72, and 96 hr at 34°C and 5% CO2. After incubation, the media was removed from the basal side of the transwell. The apical side of the transwells was then washed twice with (antibiotic-free lung wash media) and then twice with PBS. TRIzol Reagent (Thermo Fisher 15596026) was added to the well and incubated at 34°C and 5% CO2 for 10 min. The TRIzol Reagent was removed and stored at –80°C for RNA analysis.

### RNA isolation

Organoids and monolayers used for lung cell-type studies were lysed using RNA lysis buffer followed by RNA extraction per Zymo Research Quick-RNA MicroPrep Kit instructions. Tissue samples and monolayers in SARS-CoV2 studies were lysed in TRI-Reagent and RNA was extracted using Zymo Research Direct-zol RNA Miniprep.

#### Quantitative (q)RT-PCR

Organoid and monolayer cell-type gene expression was measured by qRT-PCR using 2x SYBR Green qPCR Master Mix. cDNA was amplified with gene-specific primer/probe set for the lung cell type markers and qScript cDNA SuperMix (5×). qRT-PCR was performed with the Applied Biosystems QuantStudio 5 Real-Time PCR System. Cycling parameters were as follows: 95°C for 20 s, followed by 40 cycles of 1 s at 95°C and 20 s at 60°C. All samples were assayed in triplicate and eukaryotic 18S ribosomal RNA was used as a reference.

<table>
  <thead>
    <tr>
      <th>Cell types</th>
      <th>Marker</th>
      <th>Primer sequence</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Basal cells</td>
      <td>ITGA6, NGFR, TP63</td>
      <td>ITGA6 F ′CGAAACCAAGGTTCTGAGCCC′ITGA6 R ′CTTGGATCTCCACTGAGGCAGT′NGFR F′ CCTCATCCCTGTCTATTGCTCCNGFR R′ GTTGGCTCCTTGCTTGTTCTGCTP63 F′ CAGGAAGACAGAGTGTGCTGGTTP63 R′ AATTGGACGGCGGTTCATCCCT</td>
    </tr>
    <tr>
      <td>Goblet</td>
      <td>Muc5AC</td>
      <td>Muc5AC F ′GGAACTGTGGGGACAGCTCTT′Muc5AC R ′GTCACATTCCTCAGCGAGGTC′</td>
    </tr>
    <tr>
      <td>Cilia</td>
      <td>FoxJ1</td>
      <td>FoxJ1 F ′ACTCGTATGCCACGCTCATCTG′’FoxJ1 R ′GAGACAGGTTGTGGCGGATTGA′</td>
    </tr>
    <tr>
      <td>Club cell</td>
      <td>SCGB1A1</td>
      <td>SCGB1A1 F ′CAAAAGCCCAGAGAAAGCATC′SCGB1A1 R ′CAGTTGGGGATCTTCAGCTTC′</td>
    </tr>
    <tr>
      <td>Alveolar type 1</td>
      <td>AQP5, PDPN</td>
      <td>AQP5 F ′TACGGTGTGGCACCGCTCAATG′AQP5 R ′AGTCAGTGGAGGCGAAGATGCA′PDPN F ′GTGCCGAAGATGATGTGGTGAC′PDPN R ′GGACTGTGCTTTCTGAAGTTGGC′</td>
    </tr>
    <tr>
      <td>Alveolar type 2</td>
      <td>SFTPA1, SFTPC</td>
      <td>SFTPA1 F ′CACCTGGAGAAATGCCATGTCC′SFTPA1 R ′AAGTCGTGGAGTGTGGCTTGGA′SFTPC F ′GTCCTCATCGTCGTGGTGATTG′SFTPC R ′AGAAGGTGGCAGTGGTAACCAG′</td>
    </tr>
  </tbody>
</table>

#### Assessment of SARS-CoV-2 infectivity test

Assessment of SARS-CoV-2 infectivity test was determined by qPCR using TaqMan assays and TaqMan Universal PCR Master Mix as done before (Corman et al., 2020; Lamers et al., 2020). cDNA was amplified with gene-specific primer/probe set for the E gene and QPCR was performed with the Applied Biosystems QuantStudio 3 Real-Time PCR System. The specific TaqMan primer/probe set for E gene are as follows: forward 5′-ACAGGTACGTTAATAGTTAATAGCGT-3′ (IDT, Cat# 10006888); reverse 5′-ATATTGCAGCAGTACGCACACA-3′; probe 5′-FAM-ACACTAGCCATCCTTACTGCGCTTCG-BBQ-3′ and 18S rRNA. Cycling parameters were as follows: 95°C for 20 s, followed by 40 cycles of 1 s at 95°C and 20 s at 60°C. All samples were assayed in triplicate, and gene eukaryotic 18S ribosomal RNA was used as a reference.

### Immunofluorescence

Organoids and lung organoid-derived monolayers in plates or in 8-well chamber slides were fixed by either (i) 4% PFA at room temperature for 30 min and quenched with 30 mM glycine for 5 min, (ii) ice-cold 100% methanol at –20°C for 20 min, and (iii) ice-cold 100% methanol on ice for 20 min. Subsequently, samples were permeabilized and blocked for 2 hr using an in-house blocking buffer (2 mg/ml BSA and 0.1% Triton X-100 in PBS); as described previously (Lopez-Sanchez et al., 2014). Primary antibodies were diluted in blocking buffer and allowed to incubate overnight at 4°C; secondary antibodies were diluted in blocking buffer and allowed to incubate for 2 hr in the dark. Antibody dilutions are listed in the key resources table. ProLong Glass was used as a mounting medium. #1 Thick Coverslips were applied to slides and sealed. Samples were stored at 4°C until imaged. FFPE-embedded organoid and lung tissue sections underwent antigen retrieval as previously described in Materials and methods for immunohistochemistry staining. After antigen retrieval and cooling in DI water, samples were permeabilized and blocked in blocking buffer and treated as mentioned above for immunofluorescence. Images were acquired at room temperature with Leica TCS SPE confocal and with DMI4000 B microscope using the Leica LAS-AF Software. Images were taken with a 40× oil-immersion objective using 405-, 488-, 561 nm laser lines for excitation. z-stack images were acquired by successive z-slices of 1 µm in the desired confocal channels. Fields of view that were representative and/or of interest were determined by randomly imaging three different fields. z-slices of a z-stack were overlaid to create maximum intensity projection images; all images were processed using FIJI (ImageJ) software.

### Embedding of organoids in HistoGel

Organoids were seeded on a layer of Matrigel in 6-well plates and grown for 7–8 days. Once mature, organoids were fixed in 4% PFA at room temperature for 30 min and quenched with 30 mM glycine for 5 min. Organoids were gently washed with PBS and harvested using a cell scraper. Organoids were resuspended in PBS using wide-bore 1000 µl pipette tips. Organoids were stained using Gill’s hematoxylin for 5 min for easier FFPE embedding and sectioning visualization. Hematoxylin-stained organoids were gently washed in PBS and centrifuged and excess hematoxylin was aspirated. Organoids were resuspended in 65°C HistoGel and centrifuged at 65°C for 5 min. HistoGel-embedded organoid pellets were allowed to cool to room temperature and stored in 70% ethanol at 4°C until ready for FFPE embedding by LJI Histology Core. Successive FFPE-embedded organoid sections were cut at a 4 µm thickness and fixed on to microscope slides.

### Immunohistochemistry

For SARS CoV-nucleoprotein (np) antigen retrieval, slides were immersed in Tris-EDTA buffer (pH 9.0) and boiled for 10 min at 100°C inside a pressure cooker. Endogenous peroxidase activity was blocked by incubation with 3% H2O2 for 10 min. To block nonspecific protein binding, 2.5% goat serum was added. Tissues were then incubated with a rabbit SARS CoV-NP antibody (Sino Biological, see key resource table) for 1.5 hr at room temperature in a humidified chamber and then rinsed with TBS or PBS three times, for 5 min each. Sections were incubated with horse anti-rabbit IgG secondary antibodies for 30 min at room temperature and then washed with TBS or PBS three times for 5 min each. Sections were incubated with DAB and counterstained with hematoxylin for 30 s.

### Permeability of lung monolayer using FITC-dextran

Adult lung monolayers were grown for 2 days in PneumaCult Ex-Plus media on transwell inserts (6.5 mm diameter, 0.4 µm pore size, Corning). TEER was monitored with an Epithelial Volt-Ohm Meter (Millicell). On the second day of growth, FITC-dextran (10 kD) was added at a 1:50 dilution in lung wash media. The basolateral side of the insert was changed to lung wash media only. After 30 min of incubation with FITC-dextran, 50 µl of the basolateral supernatant was transferred to an opaque welled 96-well plate. Fluorescence was measured using a TECAN plate reader.

### The characterization of lung cell types using flow cytometry

Lung organoids were dissociated into single cells via trypLE digestion and strained with a 30 µm filter (Miltenyi Biotec, Germany). Approximately 2.5E5 cells for each sample were fixed and permeabilized at room temperature in Cyto-Fast Fix Perm buffer (BioLegend, USA) for 20 min. The samples were subsequently washed with Cyto-Fast Perm Wash solution (BioLegend) and incubated with lung epithelial cell-type markers for 30 min. Following primary antibody incubation, the samples were washed and incubated with propidium iodide (Invitrogen) and Alexa Flour 488 secondary antibodies (Invitrogen) for 30 min. Samples were resuspended in FACS buffer (PBS, 5% FBS, 2 mM sodium azide). Flow cytometry was performed using Guava easyCyte Benchtop Flow Cytometer (Millipore) and data was analyzed using InCyte (version 3.3) and FlowJo X v10 software.

### RNA sequencing

RNA sequencing libraries were generated using the Illumina TruSeq Stranded Total RNA Library Prep Gold with TruSeq Unique Dual Indexes (Illumina, San Diego, CA). Samples were processed following the manufacturer’s instructions, except modifying RNA shear time to 5 min. The resulting libraries were multiplexed and sequenced with 100 basepair (bp) paired-end (PE100) to a depth of approximately 25–40 million reads per sample on an Illumina NovaSeq 6000 by the Institute of Genomic Medicine (IGM) at the University of California San Diego. Samples were demultiplexed using bcl2fastq v2.20 Conversion Software (Illumina). RNAseq data was processed using kallisto (version 0.45.0) and human genome GRCh38 Ensembl version 94 annotation (Homo_sapiens GRCh38.94 chr_patch_hapl_scaff.gtf). Gene-level transcripts per million (TPM) values and gene annotations were computed using tximport and biomaRt R package. A custom Python script was used to organize the data and log reduced using log2(TPM +1). The raw data and processed data are deposited in Gene Expression Omnibus under accession nos. GSE157055 and GSE157057.

### Data collection and annotation

Publicly available COVID-19 gene expression databases were downloaded from the National Center for Biotechnology Information (NCBI) Gene Expression Omnibus website (GEO) (Edgar et al., 2002; Barrett et al., 2005; Barrett et al., 2013). If the dataset is not normalized, RMA (Robust Multichip Average) (Irizarry et al., 2003a; Irizarry et al., 2003b) is used for microarrays and TPM (Li and Dewey, 2011; Pachter, 2011) is used for RNA seq data for normalization. We used log2(TPM +1) to compute the final log-reduced expression values for RNA seq data. Accession numbers for these crowdsourced datasets are provided in the figures and article. All of the above datasets were processed using the Hegemon data analysis framework (Dalerba et al., 2011; Dalerba et al., 2016; Volkmer et al., 2012).

### Analysis of RNA seq datasets

DESeq2 (Love et al., 2014) was applied to uninfected and infected samples to identify up- and downregulated genes. A gene signature score is computed using both the up- and downregulated genes that are used to order the sample. To compute the gene signature score, first, the genes present in this list were normalized according to a modified Z-score approach centered around StepMiner threshold (formula = (expr -SThr)/3*stddev). The normalized expression values for every probeset for all the genes were added or subtracted (depending on up and downregulated genes) together to create the final score. The samples were ordered based on the final gene signature score. The gene signature score is used to classify sample categories, and the performance of the multiclass classification is measured by ROC-AUC values. A color-coded bar plot is combined with a violin plot to visualize the gene signature-based classification. All statistical tests were performed using R version 3.2.3 (2015-12-10). Standard t-tests were performed using Python scipy.stats.ttest_ind package (version 0.19.0) with Welch’s two-sample t-test (unpaired, unequal variance (equal_var = False), and unequal sample size) parameters. Multiple hypothesis correction was performed by adjusting p-values with statsmodels.stats.multitest.multipletests (fdr_bh: Benjamini/Hochberg principles). The results were independently validated with R statistical software (R version 3.6.1; 2019-07-05). Pathway analysis of gene lists was carried out via the Reactome database and algorithm (Fabregat et al., 2018). Reactome identifies signaling and metabolic molecules and organizes their relations into biological pathways and processes. Violin, swarm, and bubble plots were created using Python seaborn package version 0.10.1.

### Single-Cell RNA seq data analysis

Single-Cell RNA seq data from GSE145926 was downloaded from GEO in the HDF5 Feature Barcode Matrix Format. The filtered barcode data matrix was processed using Seurat v3 R package (Stuart et al., 2019) and Scanpy Python package (Wolf et al., 2018). Pseudo bulk analysis of GSE145926 data was performed by adding counts from the different cell subtypes and normalized using log2(CPM + 1). Epithelial cells were identified using SFTPA1, SFTPB, AGER, AQP4, SFTPC, SCGB3A2, KRT5, CYP2F1, CCDC153, and TPPP3 genes using SCINA algorithm (Zhang et al., 2019). Pseudo bulk datasets were prepared by adding counts from the selected cells and normalized using log(CPM + 1).

### Assessment of cell-type proportions

CIBERSORTx (https://cibersortx.stanford.edu/runcibersortx.php) was used for cell-type deconvolution of our dataset (which was normalized by CPM). As reference samples, we first used the single-cell RNA seq dataset (GSE132914) from Gene Expression Omnibus (GEO). Next, we analyzed the bulk RNA seq datasets for the identification of cell types of interest using relevant gene markers (see Table 2): AT1 cells (PDPN, AQP5, P2RX4, TIMP3, SERPINE1), AT2 cells (SFTPA1, SFTPB, SFTPC, SFTPD, SCGB1A1, ABCA3, LAMP3), BASAL cells (CD44, KRT5, KRT13, KRT14, CKAP4, NGFR, ITGA6), CLUB cells (SCGB1A1, SCGB3A2, SFTPA1, SFTPB, SFTPD, ITGA6, CYP2F1), GOBLET cells (CDX2, MUC5AC, MUC5B, TFF3), ciliated cells (ACTG2, TUBB4A, FOXA3, FOXJ1, SNTN), and generic lung lineage cells (GJA1, TTF1, EPCAM) were identified using SCINA algorithm. Then, normalized pseudo counts were obtained with the CPM normalization method. The cell-type signature matrix was derived from the single-cell RNA seq dataset, cell types, and gene markers of interest. It was constructed by taking an average from gene expression levels for each of the markers across each cell type.

### Statistical analysis

All experiments were repeated at least three times, and results were presented either as one representative experiment or as average ± SEM. Statistical significance between datasets with three or more experimental groups was determined using one-way ANOVA including a Tukey’s test for multiple comparisons. For all tests, a p-value of 0.05 was used as the cutoff to determine significance (*p<0.05, **p<0.01, ***p<0.001, and ****p<0.0001). All experiments were repeated a least three times, and p-values are indicated in each figure. All statistical analyses were performed using GraphPad Prism 6.1. A part of the statistical tests was performed using R version 3.2.3 (2015-12-10). Standard t-tests were performed using Python scipy.stats.ttest_ind package (version 0.19.0).
