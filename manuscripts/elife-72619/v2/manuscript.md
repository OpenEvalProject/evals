# mRNA vaccine-induced T cells respond identically to SARS-CoV-2 variants of concern but differ in longevity and homing properties depending on prior infection status

## Authors

- Jason Neidleman<sup>1</sup>
- Xiaoyu Luo<sup>2</sup>
- Matthew McGregor<sup>1</sup>
- Guorui Xie<sup>1</sup>
- Victoria Murray<sup>3</sup>
- Warner C Greene<sup>2</sup> ([ORCID: 0000-0001-9896-8615](https://orcid.org/0000-0001-9896-8615))
- Sulggi A Lee<sup>4</sup> ([ORCID: 0000-0003-1560-2250](https://orcid.org/0000-0003-1560-2250)) †
- Nadia R Roan<sup>1</sup> ([ORCID: 0000-0002-5464-1976](https://orcid.org/0000-0002-5464-1976)) †

### Affiliations

1. Department or Urology, University of California, San Francisco San Francisco United States
2. Gladstone Institute of Virology San Francisco United States
3. University of California, San Francisco San Francisco United States
4. Medicine, University of California, San Francisco San Francisco United States

† Corresponding author

## Abstract

While mRNA vaccines are proving highly efficacious against SARS-CoV-2, it is important to determine how booster doses and prior infection influence the immune defense they elicit, and whether they protect against variants. Focusing on the T cell response, we conducted a longitudinal study of infection-naïve and COVID-19 convalescent donors before vaccination and after their first and second vaccine doses, using a high-parameter CyTOF analysis to phenotype their SARS-CoV-2-specific T cells. Vaccine-elicited spike-specific T cells responded similarly to stimulation by spike epitopes from the ancestral, B.1.1.7 and B.1.351 variant strains, both in terms of cell numbers and phenotypes. In infection-naïve individuals, the second dose boosted the quantity and altered the phenotypic properties of SARS-CoV-2-specific T cells, while in convalescents the second dose changed neither. Spike-specific T cells from convalescent vaccinees differed strikingly from those of infection-naïve vaccinees, with phenotypic features suggesting superior long-term persistence and ability to home to the respiratory tract including the nasopharynx. These results provide reassurance that vaccine-elicited T cells respond robustly to emerging viral variants, confirm that convalescents may not need a second vaccine dose, and suggest that vaccinated convalescents may have more persistent nasopharynx-homing SARS-CoV-2-specific T cells compared to their infection-naïve counterparts.

## Introduction

A year and a half since the December 2019 emergence of SARS-CoV-2, the novel betacoronavirus had already infected almost 200 million people and taken the lives of over 4 million, nearly collapsed worldwide health systems, disrupted the global economy, and perturbed society and public health on a scale not experienced within the past 100 years. Fortunately, multiple highly efficacious vaccines, including the two-dose mRNA-based ones developed by Pfizer/BioNTech and Moderna, which confer ~90 % protection against disease, were approved for emergency use before the end of 2020. Although the vaccines provide the most promising route for a rapid exit from the COVID-19 pandemic, concerns remain regarding the durability of the immunity elicited by these vaccines and the extent to which they will protect against the variants of SARS-CoV-2 now spreading rapidly around the world.

The first variant observed to display a survival advantage was the D614G, which was more transmissible than the original strain and quickly became the dominant variant throughout the world Korber et al., 2020. This variant, fortunately, did not evade immunity and in fact appeared to be more sensitive than the original strain to antibody neutralization by convalescent sera Weissman et al., 2021. More worrisome, however, was the emergence at the end of 2020 of rapidly spreading variants in multiple parts of the world, including B.1.1.7, B.1.351, P.1, and B.1.427/B.1.429 (originally identified in United Kingdom, South Africa, Brazil, and California, respectively) Plante et al., 2021, followed by additional highly transmissible variants in 2021 including the B.1.617.2 which was first detected in India Callaway, 2021. Some variants, including B.1.1.7, may be more virulent Davies et al., 2021. While antibodies against the original strain elicited by either vaccination or infection generally remain potent against B.1.1.7, their activity against B.1.351 and P.1 is compromised Wang et al., 2021; The CITIID-NIHR BioResource COVID-19 Collaboration et al., 2021; Muik et al., 2021; Garcia-Beltran et al., 2021; Stamatatos et al., 2021; Cele et al., 2021; Hoffmann et al., 2021; Planas et al., 2021; Edara et al., 2021; Kuzmina et al., 2021. Antibodies from vaccinees were 14-fold less effective against B.1.351 than against the ancestral strain, and a subset of individuals completely lacked neutralizing antibody activity against B.1.351 9 months or more after convalescence Planas et al., 2021.

Reassuringly, early data suggest that relative to antibody responses, T-cell-mediated immunity appears to be less prone to evasion by the variants Skelly et al., 2021; Tarke et al., 2021; Redd et al., 2021; Geers et al., 2021; Woldemeskel et al., 2021; Stankov et al., 2021; Tauzin et al., 2021. Among 280 CD4+ and 523 CD8+ T cell epitopes from the original SARS-CoV-2, an average of 91.5 % (for CD4) and 98.1 % (for CD8) mapped to regions not mutated in the B.1.1.7, B1.351, P.1, and B.1.427/B.1.429 variants. Focusing on just the spike response, the sole SARS-CoV-2 antigen in the mRNA-based vaccines, then 89.7 % of the CD4+ epitopes and 96.4 % of the CD8+ epitopes are conserved Tarke et al., 2021. In line with this, the magnitude of the response of T cells from convalescent or vaccinated individuals was not markedly reduced when assessed against any of the variants Tarke et al., 2021. The relative resistance of T cells against SARS-CoV-2 immune evasion is important in light of the critical role these immune effectors play during COVID-19. T cell numbers display a strong, inverse association with disease severity Chen et al., 2020; Woodruff et al., 2020, and the frequency of SARS-CoV-2-specific T cells predicts recovery from severe disease Rydyznski Moderbacher et al., 2020; Neidleman et al., 2021. SARS-CoV-2-specific T cells can also provide long-term, self-renewing immunological memory: these cells are detected more than half a year into convalescence and can proliferate in response to homeostatic signals Dan et al., 2021; Neidleman et al., 2020b. Furthermore, the ability of individuals with inborn deficiencies in B cell responses to recover from COVID-19 without intensive care suggests that the combination of T cells and innate immune mechanisms is sufficient for recovery when antibodies are lacking Soresina et al., 2020.

Although T cells against the ancestral strain display a response of similar magnitude and breadth to the variants Tarke et al., 2021, to what extent these T cells’ phenotypes and effector functions differ during their response to variant detection is a different question. Small changes in the sequences of T cell epitopes, in the form of altered peptide ligands (APLs), can theoretically alter how the T cells respond to stimulation. Indeed, change of a single residue can convert a proliferative, IL4-secreting effector response into one that continues to produce IL4 in the absence of proliferation Evavold and Allen, 1991. Furthermore, APLs can activate Th1 cells without inducing either proliferation or cytokine production, shift Th1 responses into Th2-focused ones, and in some instances even render T cells anergic or immunoregulatory by eliciting TGFβ production Sloan-Lancaster and Allen, 1996.

Another important aspect that has not been explored is to what extent vaccine- vs. infection-induced T cell responses differ phenotypically and functionally, and to what extent convalescent individuals benefit from vaccination as they already harbor some form of immunity against the virus. Studies based on the antibody and B cell response suggest that for COVID-19 convalescents, a single dose of the mRNA vaccines is helpful while the additional booster is not necessary Stamatatos et al., 2021; Goel et al., 2021; Ebinger et al., 2021; how this translates in the context of vaccine-elicited T cell immunity is not clear.

To address these knowledge gaps, we conducted 39-parameter phenotyping by CyTOF on 33 longitudinal specimens from 11 mRNA-vaccinated individuals, six of whom had previously contracted and recovered from COVID-19. For each participant, blood specimens were obtained prior to vaccination, two weeks following the first dose, and two weeks following the second. For every specimen, we assessed in depth the phenotypes and effector functions of total CD4+ and CD8+ T cells, and of CD4+ and CD8+ T cells responding to the original SARS-CoV-2 spike, to spike from variants B.1.1.7 and B.1.351, and to nucleocapsid. By conducting analyses on the resulting 165 high-dimensional datasets generated, we find a reassuringly unaltered T cell response against the variants, an ability of the booster dose to alter the phenotypes of vaccine-elicited T cells, and a striking impact of prior infection on qualitative features of T cells elicited by vaccination.

## Results

### Study design

To characterize the phenotypic features of mRNA vaccination-elicited SARS-CoV-2-specific T cells, we procured 33 longitudinal blood samples from the COVID-19 Host Immune Response and Pathogenesis (CHIRP) cohort. Four of the participants had received the Moderna (mRNA-1273) vaccine, while the remaining seven had received the Pfizer/BioNTech (BNT162b2) one. For all participants, longitudinal specimens were obtained at three timepoints: prior to vaccination, ~ 2 weeks (range 13–18 days) after the first vaccine dose, and ~2 weeks (range 6–38 days) after the second dose. Five of the participants were never infected with SARS-CoV-2, while the remaining six had completely recovered from mild (non-hospitalized) COVID-19 disease (Table 1). These prior infections had all occurred in the San Francisco Bay Area between March and July of 2020, when the dominant local strain was the original ancestral strain. Each specimen was phenotyped using a 39-parameter T cell-centric CyTOF panel (see Materials and methods and Table 2) at baseline (to establish the overall phenotypes of total CD4+ and CD8+ T cells), and following 6 hr of stimulation with overlapping 15-mer peptides spanning the entire original (ancestral) SARS-CoV-2-spike, B.1.1.7 spike, B.1.351 spike, or the original SARS-CoV-2 nucleocapsid (the latter as a control for a SARS-CoV-2-specific response not boosted by vaccination). Including all the baseline and stimulation conditions, a total of 165 specimens from the 11 participants were analyzed by CyTOF.

**Table 1.**
 Participant characteristics.


<table>
  <thead>
    <tr>
      <th>Patient ID</th>
      <th>Gender</th>
      <th>Age</th>
      <th>Prior infection status</th>
      <th>Vaccine</th>
      <th>Days post PCR+ test at pre-vaccination timepoint</th>
      <th>Days post vaccine dose #1</th>
      <th>Days post vaccine dose #2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>PID4101</td>
      <td>Female</td>
      <td>45</td>
      <td>Uninfected</td>
      <td>Pfizer/BioNT</td>
      <td>NA</td>
      <td>13</td>
      <td>12</td>
    </tr>
    <tr>
      <td>PID4109</td>
      <td>Male</td>
      <td>33</td>
      <td>Uninfected</td>
      <td>Pfizer/BioNT</td>
      <td>NA</td>
      <td>12</td>
      <td>33</td>
    </tr>
    <tr>
      <td>PID4197</td>
      <td>Female</td>
      <td>76</td>
      <td>Uninfected</td>
      <td>Pfizer/BioNT</td>
      <td>NA</td>
      <td>14</td>
      <td>13</td>
    </tr>
    <tr>
      <td>PID4198</td>
      <td>Male</td>
      <td>79</td>
      <td>Uninfected</td>
      <td>Moderna</td>
      <td>NA</td>
      <td>18</td>
      <td>10</td>
    </tr>
    <tr>
      <td>PID4199</td>
      <td>Female</td>
      <td>32</td>
      <td>Uninfected</td>
      <td>Pfizer/BioNT</td>
      <td>NA</td>
      <td>14</td>
      <td>10</td>
    </tr>
    <tr>
      <td>PID4104</td>
      <td>Female</td>
      <td>33</td>
      <td>Convalescent</td>
      <td>Moderna</td>
      <td>212</td>
      <td>14</td>
      <td>14</td>
    </tr>
    <tr>
      <td>PID4108</td>
      <td>Female</td>
      <td>20</td>
      <td>Convalescent</td>
      <td>Pfizer/BioNT</td>
      <td>226</td>
      <td>13</td>
      <td>38</td>
    </tr>
    <tr>
      <td>PID4112</td>
      <td>Female</td>
      <td>59</td>
      <td>Convalescent</td>
      <td>Moderna</td>
      <td>254</td>
      <td>16</td>
      <td>13</td>
    </tr>
    <tr>
      <td>PID4114</td>
      <td>Female</td>
      <td>46</td>
      <td>Convalescent</td>
      <td>Moderna</td>
      <td>216</td>
      <td>16</td>
      <td>50</td>
    </tr>
    <tr>
      <td>PID4117</td>
      <td>Female</td>
      <td>51</td>
      <td>Convalescent</td>
      <td>Pfizer/BioNT</td>
      <td>82</td>
      <td>16</td>
      <td>6</td>
    </tr>
    <tr>
      <td>PID4118</td>
      <td>Female</td>
      <td>39</td>
      <td>Convalescent</td>
      <td>Pfizer/BioNT</td>
      <td>173</td>
      <td>18</td>
      <td>28</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 List of CyTOF antibodies used in study.Antibodies were either purchased from the indicated vendor or prepared in-house using commercially available MaxPAR conjugation kits per manufacturer’s instructions (Fluidigm).


<table>
  <thead>
    <tr>
      <th>Antigen target</th>
      <th>Clone</th>
      <th>Elemental isotope</th>
      <th>Vendor</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>HLADR</td>
      <td>TÜ36</td>
      <td>Qdot (112 Cd)</td>
      <td>Thermofisher</td>
    </tr>
    <tr>
      <td>RORγt*</td>
      <td>AFKJS-9</td>
      <td>115 In</td>
      <td>In-house</td>
    </tr>
    <tr>
      <td>CD49d (α4)</td>
      <td>9F10</td>
      <td>141Pr</td>
      <td>Fluidigm</td>
    </tr>
    <tr>
      <td>CTLA4*</td>
      <td>14D3</td>
      <td>142Nd</td>
      <td>In-house</td>
    </tr>
    <tr>
      <td>NFAT*</td>
      <td>D43B1</td>
      <td>143Nd</td>
      <td>Fluidigm</td>
    </tr>
    <tr>
      <td>CCR5</td>
      <td>NP6G4</td>
      <td>144Nd</td>
      <td>Fluidigm</td>
    </tr>
    <tr>
      <td>CD137</td>
      <td>4B4-1</td>
      <td>145Nd</td>
      <td>In-house</td>
    </tr>
    <tr>
      <td>CD95</td>
      <td>BX2</td>
      <td>146Nd</td>
      <td>In-house</td>
    </tr>
    <tr>
      <td>CD7</td>
      <td>CD76B7</td>
      <td>147Sm</td>
      <td>Fluidigm</td>
    </tr>
    <tr>
      <td>ICOS</td>
      <td>C398.4A</td>
      <td>148Nd</td>
      <td>Fluidigm</td>
    </tr>
    <tr>
      <td>Tbet*</td>
      <td>4B10</td>
      <td>149Sm</td>
      <td>In-house</td>
    </tr>
    <tr>
      <td>IL4*</td>
      <td>MP4-25D2</td>
      <td>150Nd</td>
      <td>In-house</td>
    </tr>
    <tr>
      <td>CD2IL17*</td>
      <td>TS1/8BL168</td>
      <td>151Eu152Sm</td>
      <td>FluidigmIn-house</td>
    </tr>
    <tr>
      <td>CD62L</td>
      <td>DREG56</td>
      <td>153Eu</td>
      <td>Fluidigm</td>
    </tr>
    <tr>
      <td>TIGIT</td>
      <td>MBSA43</td>
      <td>154Sm</td>
      <td>Fluidigm</td>
    </tr>
    <tr>
      <td>CCR6</td>
      <td>11A9</td>
      <td>155Gd</td>
      <td>In-house</td>
    </tr>
    <tr>
      <td>IL6*</td>
      <td>MQ2-13A5</td>
      <td>156 Gd</td>
      <td>In-house</td>
    </tr>
    <tr>
      <td>CD8</td>
      <td>RPA-T8</td>
      <td>157Gd</td>
      <td>In-house</td>
    </tr>
    <tr>
      <td>CD19</td>
      <td>HIB19</td>
      <td>157Gd</td>
      <td>In-house</td>
    </tr>
    <tr>
      <td>CD14</td>
      <td>M5E2</td>
      <td>157Gd</td>
      <td>In-house</td>
    </tr>
    <tr>
      <td>OX40</td>
      <td>ACT35</td>
      <td>158Gd</td>
      <td>Fluidigm</td>
    </tr>
    <tr>
      <td>CCR7</td>
      <td>G043H7</td>
      <td>159Tb</td>
      <td>Fluidigm</td>
    </tr>
    <tr>
      <td>CD28</td>
      <td>CD28.2</td>
      <td>160Gd</td>
      <td>Fluidigm</td>
    </tr>
    <tr>
      <td>CD45RO</td>
      <td>UCHL1</td>
      <td>161Dy</td>
      <td>In-house</td>
    </tr>
    <tr>
      <td>CD69</td>
      <td>FN50</td>
      <td>162Dy</td>
      <td>Fluidigm</td>
    </tr>
    <tr>
      <td>CRTH2</td>
      <td>BM16</td>
      <td>163Dy</td>
      <td>Fluidigm</td>
    </tr>
    <tr>
      <td>PD-1</td>
      <td>EH12.1</td>
      <td>164Dy</td>
      <td>In-house</td>
    </tr>
    <tr>
      <td>CD127</td>
      <td>A019D5</td>
      <td>165Ho</td>
      <td>Fluidigm</td>
    </tr>
    <tr>
      <td>CXCR5</td>
      <td>RF8B2</td>
      <td>166Er</td>
      <td>In-house</td>
    </tr>
    <tr>
      <td>CD27</td>
      <td>L128</td>
      <td>167Er</td>
      <td>Fluidigm</td>
    </tr>
    <tr>
      <td>IFNγ*</td>
      <td>B27</td>
      <td>168Er</td>
      <td>Fluidigm</td>
    </tr>
    <tr>
      <td>CD45RA</td>
      <td>HI100</td>
      <td>169Tm</td>
      <td>Fluidigm</td>
    </tr>
    <tr>
      <td>CD3</td>
      <td>UCHT1</td>
      <td>170Er</td>
      <td>Fluidigm</td>
    </tr>
    <tr>
      <td>CD57</td>
      <td>HNK-1</td>
      <td>171Yb</td>
      <td>In-house</td>
    </tr>
    <tr>
      <td>CD38</td>
      <td>HIT2</td>
      <td>172Yb</td>
      <td>Fluidigm</td>
    </tr>
    <tr>
      <td>α4β7</td>
      <td>Act1</td>
      <td>173Yb</td>
      <td>In-house</td>
    </tr>
    <tr>
      <td>CD4</td>
      <td>SK3</td>
      <td>174Yb</td>
      <td>Fluidigm</td>
    </tr>
    <tr>
      <td>CXCR4</td>
      <td>12G5</td>
      <td>175Lu</td>
      <td>Fluidigm</td>
    </tr>
    <tr>
      <td>CD25</td>
      <td>M-A251</td>
      <td>176Yb</td>
      <td>In-house</td>
    </tr>
    <tr>
      <td>CD161</td>
      <td>NKR-P1A</td>
      <td>209 Bi</td>
      <td>In-house</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

_*Intracellular antibodies._

### SARS-CoV-2-specific T cells elicited by vaccination recognize B.1.1.7 and B.1.351 variants

We first confirmed our ability to identify SARS-CoV-2-specific T cells by stimulating PBMCs from vaccinated individuals with spike peptides. In line with our prior studies implementing a 6 hr peptide stimulation Neidleman et al., 2021; Neidleman et al., 2020b, spike-specific CD4+ T cells could be specifically identified through intracellular cytokine staining for IFNγ, and a more robust response was observed among CD4+ than CD8+ T cells (Figure 1 ). No specific induction of IL4 or IL17 by CD4+ T cells were observed in response to peptide stimulation (Figure 1—figure supplement 1). In addition, activation-induced markers (AIM) such as Ox40, 4-1BB, and CD69 could also be identified in T cells after spike peptide stimulation, but with a higher background in the baseline (no peptide stimulation) specimens relative to the intracellular cytokine staining approach (Figure 1—figure supplement 1). For these reasons, in this study we exclusively used IFNγ positivity in the peptide-stimulated samples as a marker of antigen-specific T cells.

![Figure 1.](https://cdn.elifesciences.org/articles/72619/elife-72619-fig1-v2.jpg)

**Figure 1.:** (A) Identification of vaccine-elicited spike-specific T cells. PBMCs before vaccination (Pre-Vac) or 2 weeks after each dose of vaccination were stimulated with spike peptides and assessed by CyTOF 6 hr later for the presence of spike-specific (IFNγ-producing) CD4+ (left) or CD8+ (right) T cells. The ‘no peptide’ conditions served as negative controls. Shown are longitudinal data from an infection-naïve (PID4101, top) and convalescent (PID4112, bottom) individual. (B) Quantification of the spike-specific CD4+ (left) and CD8+ (right) T cells recognizing the ancestral (squares), B.1.1.7 (triangles), and B.1.351 (circles) spike peptides ininfection-naïve (top) and a convalescent (bottom) individuals before and after vaccination. Note the similar frequencies of T cells responding to all three spike proteins in each donor, the clear boosting of spike-specific CD4+ T cell frequencies in infection-naïve but not convalescent individuals, and the overall higher proportion of responding CD4+ than CD8+ T cells. The dotted line corresponds to the magnitude of the maximal pre-vaccination response in infection-naïve individuals and is considered as background. The y-axes are fitted based upon the maximal post-vaccination response values for each patient group and T cell subset. The p-values shown (**p < 0.01, ***p < 0.001) were calculated by student’s t-test. (C) As expected, nucleocapsid-specific T cell responses are generally low over the course of vaccination, with the exception of convalescent donor PID4112. Shown are the frequencies of nucleocapsid-specific CD4+ (left) and CD8+ (right) T cells, as measured by IFNγ production upon stimulation with ancestral nucleocapsid peptides, in infection-naïve (top) and convalescent (bottom) individuals. The dotted line corresponds to the magnitude of the maximal pre-vaccination response in infection-naïve individuals and is considered as the background signal. Y-axes are labeled to match the corresponding y-axes for spike-specific T cell responses in panel B. (D) The CD4+ T cell response is boosted by the second vaccine dose to a greater extent in infection-naïve than convalescents individuals. Shown are the frequencies of spike-specific CD4+ (left) and CD8+ (right) T cells stimulated by the three spike proteins (squares: ancestral; triangles: B.1.1.7; circles: B.1.351) among the infection-naïve (aqua) and convalescent (coral) donors, after removal of outlier PID4112. ***p < 0.001 comparing the infection-naïve vs. convalescent post-dose two specimens, were calculated using student’s t-test.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/72619/elife-72619-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A, B) CD4+ T cells were assessed for expression of the Th2 cytokine IL4 (A) or the Th17 cytokine IL17 (B) following 6 hr of stimulation with ancestral spike peptides using PBMC specimens from a representative infection-naïve individual (PID4197) before vaccination (Pre-Vac), or 2 weeks after dose 1 or dose 2 of vaccination. (C) CD4+ T cells were assessed for co-expression of the activation-induced markers (AIM) Ox40 and 4-1BB following 6 hr of stimulation, using the same specimens as panel A. (D) CD8+ T cells were assessed for co-expression of the AIM CD69 and 4-1BB following 6 hr of stimulation, using the same specimens as panel A. Baseline specimens not treated with peptide are shown as a comparison control. Numbers correspond to percentages of cells within the gates. Note that the activated (AIM+) cells that appear in stimulated specimens probably do not reflect peptide-specific stimulation as AIM+ cells are also detected in the baseline specimens.

In the infection-naïve participants, the first vaccination dose primed a spike-specific CD4+ T cell response, which was further boosted with the second dose (Figure 1B, top left). For each participant and time point, similar numbers of cells were stimulated by exposure to the ancestral or variant spikes. This finding suggests that vaccine-elicited spike-specific CD4+ T cells recognize ancestral and variant spike equally well, and is consistent with their recently reported ability to recognize variant strains Tarke et al., 2021. The response of vaccine-elicited CD8+ T cells to spike peptides was weaker, and mostly apparent only after the second dose (Figure 1B, top right). As expected, vaccination did not elicit T cells able to respond to nucleocapsid peptides (Figure 1C, top panels).

In contrast to the infection-naïve individuals where spike-specific CD4+ T cells were clearly elicited and then boosted upon the second dose, spike-specific CD4+ T cell responses in convalescent individuals did not show a consistent upward trend. Convalescent donor PID4112 had a large frequency of pre-vaccination SARS-CoV-2-specific CD4+ T cells that increased to >1% of the total CD4+ T cell frequency after the first dose and then dampened after dose 2 (Figure 1B , bottom left). PID4112 also exhibited an elevated nucleocapsid-specific CD4+ T cell response after the first vaccination dose (Figure 1C, bottom left), which may have been due to bystander effects resulting from the concomitant large spike-specific response. In comparison, PID4112’s spike-specific CD8+ T cell response was low after dose 1, and boosted after dose 2 (Figure 1B, bottom right). In contrast to PID4112, the remaining five convalescent donors exhibited an overall weak spike-specific T cell response. In fact, when comparing these five donors to the five infection-naïve donors, there was a significant decrease in the magnitude of the spike-specific CD4+ T cell response, while the spike-specific CD8+ T cell response was equivalent between the two groups (Figure 1D). These results were unexpected and suggest that, when excluding outlier PID4112, the magnitude of the vaccine-elicited spike-specific CD4+ T cell response (after full vaccination) was lower in convalescent individuals than in infection-naïve individuals.

These assessments of the magnitude of the spike-specific T cell response together suggest that (1) in infection-naïve individuals the CD4+ T cell response is boosted by the second vaccination dose, (2) convalescent individuals exhibit a more disparate response, with most donors mounting a weaker response than infection-naïve individuals, and (3) the response is more robust among CD4+ than CD8+ T cells. As a higher number of SARS-CoV-2-specific CD4+ T cells were available for analysis, we focused on this subset for our subsequent analyses.

### Vaccine-elicited spike-specific CD4+ T cells responding to B.1.1.7 and B.1.351 spike are indistinguishable from those responding to ancestral spike

Leveraging our ability to not only assess the magnitude but also the detailed (39-parameter) phenotypic features of SARS-CoV-2-specific CD4+ T cells, we first determined whether the ancestral and variant spike epitopes stimulated different subsets of vaccine-elicited spike-specific CD4+ T cells. Such differences could theoretically result from the fact that ~5–10% of the spike epitopes differ between variants and ancestral strains Tarke et al., 2021, and may therefore act as APLs steering responding cells towards different fates. We isolated the datasets corresponding to both post-vaccination timepoints for all eleven donors, and then exported the data corresponding to spike-specific CD4+ T cells (as defined by IFNγ production, Figure 1 ). After reducing the multidimensional single-cell data for each individual specimen to a two-dimensional datapoint through multidimensional scaling (MDS) Ritchie et al., 2015, we observed the ancestral spike-stimulated samples to be interspersed among the B.1.1.7- and B.1.351-responding ones (Figure 2A). We then visualized the spike-specific CD4+ T cells at the single-cell level. When visualized alongside total (baseline) CD4+ T cells, spike-specific cells occupied a distinct ‘island’ defined by high expression of IFNγ (Figure 2B), suggesting unique phenotypic features of these cells. To better analyze these spike-responding CD4+ T cells, we visualized them in isolation within a new tSNE which clearly demonstrated complete mixing of the cells stimulated by the ancestral, B.1.1.7, and B.1.351 spike proteins (Figure 2C). Almost all the responding cells expressed high levels of CD45RO and low levels of CD45RA (Figure 2D), suggesting them to be mostly memory cells. These memory CD4+ T cells included central memory T cells (Tcm), T follicular helper cells (Tfh), and those expressing multiple activation markers (CD38, HLADR, CD69, CD25) and receptors known to direct cells to tissues including the respiratory tract (CXCR4, CCR5, CCR6, CD49d) (Figure 2E). The expression levels of these and all other antigens quantitated by CyTOF were not statistically different between CD4+ T cells responding to the three spike proteins (Figure 2—figure supplement 1). To confirm the identical phenotypes of the three groups of spike-responding cells, we implemented unbiased clustering by FlowSOM. Spike-stimulated cells were clustered into eight subsets, and no subset was preferentially enriched in any one of the three groups (Figure 2F). Together, these data suggest that vaccine-elicited spike-specific CD4+ T cells respond in the same manner to spike epitopes from the ancestral or variant strains, and would probably mount similar responses in vivo to infection by all three virus types.

![Figure 2.](https://cdn.elifesciences.org/articles/72619/elife-72619-fig2-v2.jpg)

**Figure 2.:** (A) Datasets corresponding to spike-specific CD4+ T cells after vaccination were visualized as a multidimensional scaling (MDS) plot. Each datapoint reflects the cumulative phenotypes averaged across all the SARS-CoV-2-specific CD4+ T cells from a single stimulated sample. Data for both infection-naïve and convalescent individuals, and for both the post-dose one and post-dose two timepoints, are shown. The lack of segregation of the cells responding to the ancestral, B.1.1.7, and B.1.351 spike proteins suggest phenotypic similarities. (B) Visualization of the datasets by tSNE dot plots. CD4+ T cells responding to ancestral or variant spike stimulation by producing high amounts of IFNγ (right) segregate together and away from the total CD4+ T cell population (left). Each dot represents one cell. (C) CD4+ T cells responding to ancestral spike and its variants are phenotypically similar, as shown by their complete mingling on a tSNE dot plot. (D, E) Spike-responding CD4+ T cells are mostly memory cells, as indicated by high CD45RO and low CD45RA expression levels, and include those expressing high levels of Tcm, Tfh, activation, and respiratory tract migration markers. Shown is the tSNE depicted in panel C displaying the relative expression levels of the indicated antigens (Red: high; Blue: low). Heatmaps were scaled from 0 to the maximal signal in each channel. (F) CD4+ T cells responding to ancestral spike and its variants distribute in a similar fashion among the eight clusters identified by FlowSOM. Shown on the left is the distribution of T cells responding to ancestral or variant spike peptides on the tSNE depicted in panel C, colored according to the FlowSOM clustering. Shown on the right is the quantification of the FlowSOM distribution data. No significant differences were observed between the three groups in the distribution of their cells among the eight clusters, as calculated using a one-way ANOVA and adjusted for multiple testing (n = 8) using Holm-Sidak method (p > 0.05).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/72619/elife-72619-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Shown are the mean expression levels of each antigen in post-vaccination spike-responding CD4+ T cells quantitated by CyTOF. Each datapoint corresponds to a single specimen. Data are presented as box plots. No significant differences were observed in expression levels for any of the antigens between any of the three groups, as assessed by one-way and ANOVA adjusted for multiple testing (n = 39) using the Holm-Sidak method (p > 0.05).

### Phenotypic alterations of spike-specific CD4+ T cells in infection-naïve recipients after the second vaccine dose

We next took advantage of our longitudinal study design to assess for any changes in the differentiation of spike-specific T cell responses over the course of the 2-dose vaccination. As the data presented above suggested no phenotypic differences between CD4+ T cells responding to the ancestral, B.1.1.7, and B.1.351 spike proteins, our subsequent analyses combined these datasets. We first assessed whether, among infection-naïve individuals, the phenotypes of spike-specific CD4+ T cells were different after the first and second doses. While MDS and tSNE visualizations of the data revealed that the cells from the two timepoints were somewhat interspersed (Figure 3A-B), FlowSOM clustering suggested some differences in cluster distribution (Figure 3C-D). Direct comparison of the cluster frequencies revealed a cluster (B8) significantly enriched after the first dose, and a different cluster (B5) significantly enriched after the second dose (Figure 3E). As these two clusters differentially expressed the Tcm markers CD27 and CCR7 (Figure 3F), we then assessed whether Tcm cells were differentially represented among spike-specific CD4+ T cells after each of the vaccination doses. Indeed, Tcm cells were significantly higher after the first dose (Figure 3G), consistent with Cluster 8 (enriched after the first dose) expressing high levels of these two receptors. Assessment of other canonical CD4+ T cell subsets – in particular naïve (Tn), stem cell memory (Tscm), effector memory RA (Temra), effector memory (Tem), T transitional memory (Ttm), Tfh, and regulatory T cells (Treg) – revealed Tn cells, like the Tcm subset, to be decreased after the second dose. By contrast, Ttm cells were found to be higher after the second dose, while the remaining subsets were not altered (Figure 3G-H). Overall, Tcm and Tfh were the most abundant subsets among the spike-specific CD4+ T cells (Figure 3G-H). These data together suggest that after receiving the second dose, infection-naïve individuals’ spike-specific CD4+ T cells increase in quantity (Figure 1B), and alter their phenotypes as reflected by a decrease Tcm cells and an increase in Ttm cells.

![Figure 3.](https://cdn.elifesciences.org/articles/72619/elife-72619-fig3-v2.jpg)

**Figure 3.:** (A) MDS plot depicting samples of spike-specific CD4+ T cells in vaccinated infection-naïve individuals, showing some interspersion of the cells from the two post-vaccination timepoints. Each dot represents a single specimen. (B) tSNE dot plot of spike-specific CD4+ T cells from vaccinated infection-naïve individuals. Each dot represents a single cell. (C) tSNE plots depicting cells from the two timepoints, colored according to the cells’ cluster classification as determined by FlowSOM. (D) Distribution among FlowSOM clusters of post-vaccination spike-specific CD4+ T cells from infection-naïve individuals between the two post-vaccination timepoints. (E) Two clusters of spike-specific CD4+ T cells (B5 and B8) are differentially abundant after the first vs. second vaccination doses. Data are presented as box plots. *p < 0.05, *** p < 0.001 as determined using student’s t-tests adjusted for multiple testing (n = 8) using Holm-Sidak method. (F) The Tcm markers CD27 and CCR7 are differentially expressed among Clusters B5 and B8, as depicted by histograms. (G) The proportions of Tn (CD45RO-CD45RA + CCR7+ CD95-), Tscm (CD45RO-CD45RA + CCR7+ CD95+), Temra (CD45RO-CD45RA + CCR7-), Tcm (CD45RO + CD45RA-CCR7+ CD27+), Tem (CD45RO + CD45RA-CCR7-CD27-), and Ttm (CD45RO + CD45RA-CCR7-CD27+) among spike-specific CD4+ cells in infection-naïve individuals after the first vs. second vaccination doses. *p < 0.05, ***p < 0.001, ns = non-significant as determined by student’s t-test. (H) The proportions of Tfh (CD45RO + CD45RA-PD1+ CXCR5+) and Treg (CD45RO + CD45RA-CD25+CD127low) among spike-specific CD4+ T cells are similar in infection-naïve individuals after the first vs. second vaccination doses. ns = non-significant as determined by student’s t-test. Error bars in panels G-H correspond to mean ± SD.

We then conducted a similar analysis in the convalescent individuals. As the pre-vaccination timepoint included spike-specific CD4+ T cells primed by prior SARS-CoV-2 infection, we included all three timepoints in this analysis. When the data were visualized by MDS, it was apparent that most of the pre-vaccination specimens localized away from the post-vaccination specimens, which were interspersed with each other (Figure 4A). Similar distinctions between pre-and post-vaccination specimens were visualized at the single-cell level by tSNE, which was particularly apparent when visualized as contour heatmaps (Figure 4B and C). Clustering of the cells by FlowSOM revealed that the cluster distribution was markedly skewed among the pre-vaccination cells (Figure 4D and E), with one cluster being under-represented (C2) and one over-represented (C5) as compared to both post-vaccination timepoints (Figure 4F). Cluster C3 was the only cluster that was significantly different after 1 vs 2 doses (Figure 4F) but as this cluster comprised only <5 % of the cells it was not analyzed further. To assess what may drive the differences between the phenotypes of the pre- vs. post-vaccination spike-specific CD4+ T cells, we assessed for markers differentially expressed between clusters C2 and C5. Cluster C2 cells preferentially expressed the Tcm markers CD27 and CCR7, the Tfh markers PD1 and CXCR5, and the co-stimulatory receptors ICOS and Ox40, while among these only CD27 was preferentially expressed in Cluster C5 (Figure 4—figure supplement 1). Manual gating confirmed Tcm, Tfh, and ICOS+ Ox40+ cells to be preferentially enriched in the post-vaccination specimens (Figure 4G-I). None of the canonical subsets were differentially abundant after the first vs. second vaccination dose. Together, these results suggest that, in contrast to the infection-naïve individuals, convalescents’ spike-specific CD4+ T cells were similar after the first vs. second vaccination dose; however, in these individuals vaccination drastically altered the phenotypes of the pre-existing spike-specific CD4+ T cells (presumably elicited from the original infection).

![Figure 4.](https://cdn.elifesciences.org/articles/72619/elife-72619-fig4-v2.jpg)

**Figure 4.:** (A) MDS plot depicting datasets corresponding to spike-specific CD4+ T cells in convalescent individuals before and after vaccination. (B) tSNE contour heatmaps of spike-specific CD4+ T cells from convalescent individuals emphasizes phenotypic differences between the pre- and post-vaccination cells. Cell densities are represented by color. (C) tSNE dot plot of spike-specific CD4+ T cells from convalescent individuals, demonstrating the distinct localization of the pre-vaccination cells on the right. (D) Spike-specific CD4+ T cells are phenotypically distinct between the pre- and post-vaccination specimens. Shown are tSNE plots depicting cells from the three indicated timepoints, colored according to the cells’ cluster classification as determined by FlowSOM. (E) The distribution of spike-specific CD4+ T cells classified as FlowSOM clusters differs between the pre- and post-vaccination timepoints. (F) Multiple clusters of spike-specific CD4+ T cells are differentially abundant between the pre- and post-vaccination specimens. Data are presented as box plots. **p < 0.01, ***p < 0.001, ****p < 0.0001 as determined by one-way ANOVA and adjusted for multiple testing (n = 8) using the Holm-Sidak method followed by Tukey’s honestly significant difference (HSD) post-hoc test. (G) Spike-specific CD4+ Tcm increase in convalescent individuals after vaccination. Shown are the proportions of Tn, Tscm, Temra Tcm, Tem, and Ttm among spike-specific CD4+ cells in convalescent individuals before and after vaccination. (H) Spike-specific CD4+ Tfh increase in convalescent individuals after vaccination. Shown are the proportions of Tfh and Treg among spike-specific CD4+ T cells in convalescent individuals before and after vaccination. (I) Spike-specific CD4+ T cells expressing ICOS and Ox40 increase in convalescent individuals after vaccination. In panels G-I, *p < 0.05, **p < 0.01, ***p < 0.001, and ****p < 0.0001 as determined by one-way ANOVA followed by Tukey’s HSD post-hoc test. Error bars in panels G-I correspond to mean ± SD.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/72619/elife-72619-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Shown are histogram depictions of the expression levels of the indicated activation markers in Cluster C2 (A) or C5 (B) from convalescent individuals. Cluster C2 was more abundant post-vaccination, while Cluster C5 was more abundant pre-vaccination.

### Vaccination-induced spike-specific CD4+ T cells from convalescent individuals exhibit unique phenotypic features of increased longevity and tissue homing

We next determined whether there were any phenotypic differences between the vaccine-induced spike-specific CD4+ T cells from the infection-naïve vs. convalescent individuals. Removal of convalescent outlier PID4112 revealed the magnitude of the spike-specific CD4+ T cell response to be lower in the convalescents than in infection-naïve participants after full vaccination (Figure 1D). But when all donors were included there was no statistically significant difference in response magnitude (Figure 5A). However, the spike-specific CD4+ T cells from the convalescent and infection-naïve individuals exhibited clear phenotypic differences when assessed by both MDS (Figure 5B) and tSNE contours (Figure 5C); this was more apparent after the second vaccine dose, but could already be observed after the first. Since the cells after the second dose are more clinically relevant (as they are the ones persisting in vaccinated individuals moving forward), we focused our subsequent analysis on just this timepoint. When visualized as a dot plot, it was apparent that the spike-specific CD4+ T cells from infection-naïve individuals segregated away from those from the convalescents (Figure 5D). Clustering of the data also demonstrated differences between the two patient groups (Figure 5E and F), which was confirmed by demonstration of a significant difference in Cluster A1 abundance (Figure 5G).

![Figure 5.](https://cdn.elifesciences.org/articles/72619/elife-72619-fig5-v2.jpg)

**Figure 5.:** (A) The frequency of spike-specific CD4+ T cells is similar in infection-naïve and convalescent individuals two weeks after the second vaccination dose. Note that when convalescent donor PID4112, who had an unusually high pre-vaccination frequency of spike-specific CD4+ T cells (Figure 1D), was excluded, the frequency was significantly lower among the convalescents. Error bars correspond to mean ± SD. (B) MDS plots of the phenotypes of spike-specific CD4+ T cells in infection-naïve and convalescent individuals after first and second dose vaccinations. (C) tSNE contour heatmaps of spike-specific CD4+ T cells from infection-naïve and convalescent individuals, after first and second dose vaccinations, highlighting the phenotypic differences between the two groups of patients. Cell densities are represented by color. (D) tSNE dot plot of spike-specific CD4+ T cells from infection-naïve and convalescent individuals after second dose of vaccination, demonstrating the segregation of the cells from the two groups of patients. (E) Spike-specific CD4+ T cells are phenotypically distinct between the infection-naïve and convalescent individuals. Shown are tSNE plots depicting cells after the second dose of vaccination, colored according to the cells’ cluster classification as determined by FlowSOM. (F) The distribution of spike-specific CD4+ T cells into FlowSOM clusters differs between the infection-naïve and convalescent individuals after the second vaccine dose. (G) Cluster A1 is over-represented in infection-naïve relative to convalescent individuals after the second dose of vaccination. Data are presented as box plots. **p < 0.01, as determined by student’s t-tests adjusted for multiple testing (n = 8) using the Holm-Sidak method.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/72619/elife-72619-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) Shown are histograms of the expression levels of the alpha chain of the IL7 receptor (CD127), the chemokine receptor CXCR4, and the lymph node homing receptor CCR7, among clusters A1 or A3, the former of was enriched in infection-naïve relative to convalescent individuals after vaccination. Data were concatenated from all clustered cells. (B) Relative expression levels, as depicted by normalized mean signal intensity (MSI), of CD127, CXCR4, and CCR7 among all specimens of spike-specific CD4+ T cells from infection-naïve and convalescent individuals, after the second vaccination dose. Data are presented as box plots. *p < 0.05, **p< 0.01, ns = non-significant, as determined using student’s t-tests and corrected for multiple testing (n = 39) using the Holm-Sidak method.

To identify these phenotypic differences, we first assessed the relative distributions of the main canonical CD4+ T cell subsets. Interestingly, the vaccinated convalescents harbored significantly more spike-specific Tcm and Tn, and less spike-specific Ttm (Figure 6A). By contrast, Tfh and Treg frequencies were not different between infection-naïve and convalescent vaccinees (Figure 6B). To broaden our analysis, we assessed for unique features of Cluster A1, which was over-represented in the infection-naïve donors, and Cluster A3, an abundant cluster which was over-represented in the convalescent donors albeit insignificantly (Figure 5G). Interestingly, Cluster A1 expressed low levels of CD127, CXCR4, and CCR7 in contrast to Cluster A3 (Figure 5—figure supplement 1A). As Cluster A1 is enriched among the infection-naïve individuals, these findings suggest that these three receptors may be expressed at lower levels on the cells from these individuals, relative to those from vaccinated convalescents. This was confirmed by our detection of higher expression of CD127, CXCR4, and CCR7 on spike-specific CD4+ T cells from the convalescents, although for CXCR4 the difference did not reach statistical significance (Figure 5—figure supplement 1B).

![Figure 6.](https://cdn.elifesciences.org/articles/72619/elife-72619-fig6-v2.jpg)

**Figure 6.:** (A) Spike-specific CD4+ T cells from convalescent vaccinated individuals harbor higher proportions of Tn and Tcm cells and lower proportions of Ttm cells than those from infection-naïve vaccinated individuals. The proportions of Tn, Tscm, Temra, Tcm, Tem, and Ttm cells among spike-specific CD4+ T cells were determined by manual gating. **p< 0.01, ***p < 0.001, ****p < 0.0001, ns = non-significant, as determined by student’s t-test. (B) The proportions of Tfh and Treg among spike-specific CD4+ T cells are similar in infection-naïve vs. convalescent individuals after vaccination. ns = non-significant, as determined by student’s t-test. (C) Spike-specific CD4+ T cells expressing the homeostatic proliferation marker CD127 and lacking expression of the terminal differentiation marker CD57 are more frequent in vaccinated convalescent than vaccinated infection-naïve individuals. **p < 0.01, as determined by student’s t-test. (D) Spike-specific CD4+ T cells expressing CXCR4, which directs cells to tissues including the lung, and CD69, a marker of T cell activation and tissue residence, are more frequent in convalescent vaccinated individuals. ***p < 0.001, as determined by student’s t-test. (E) Spike-specific CD4+ T cells expressing the lymph node homing receptors CCR7 and CD62L are more frequent in vaccinated convalescent individuals. *P < 0.05, as determined by student’s t-test. Error bars in panels A-E correspond to mean ± SD. (F) The proportions of CCR7+ CD62L + cells among spike-specific CD4+ T cells associate negatively with the frequencies of spike-specific CD4+ T cells after the second dose of vaccination (correlation coefficient (R) < 0). P-values were calculated using t distribution with n-2 degrees of freedom. (G) Expression levels (reported as mean signal intensity, or MSI) of CCR7 and CD62L among spike-specific CD4+ T cells associate negatively (R < 0) with overall frequencies of spike-specific CD4+ T cells after the second dose of vaccination. p-Values were calculated using t distribution with n-2 degrees of freedom. The 95 % confidence intervals of the regression lines in the scatter plots of panels F-G are shaded in grey. (H) CCR7+ CD62L + and CXCR4+ CD69+ CD4+ T cells are more frequent in nasopharynx than blood. Unstimulated CD4+ T cells from the blood (gray) or from an intranasal swab (red) were obtained on the same day from PID4101 and then phenotyped by CyTOF. Numbers indicate the percentages of the corresponding cell population within the gate. Results are gated on live, singlet CD3+ CD4+ CD8- cells.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/72619/elife-72619-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A–C) MDS (A) or tSNE (B, C) plots demonstrating phenotypic similarities between spike-specific CD8+ T cells responding to spike from the ancestral, B.1.1.7, or B.1.351 strains. Data are displayed in a format similar to that for CD4+ T cells presented in Figure 2A-C. (D) MDS plot depicting specimens of spike-specific CD8+ T cells in infection-naïve and convalescent individuals after second vaccination dose. (E) tSNE contour heatmaps depicting spike-specific CD8+ T cells from infection-naïve and convalescent individuals, after the second vaccination dose. Cell densities are represented by color. (F) tSNE dot plot of spike-specific CD8+ T cells from infection-naïve and convalescent individuals after second vaccination dose. (G) The distribution of spike-specific cells among the main canonical CD8+ T cell subsets (Tn, Tscm, Temra, Tcm, Tem, Ttm) is similar in infection-naïve vs. convalescent individuals after second vaccination dose. (H) T cell subsets that were differentially enriched in infection-naïve vs. convalescent individuals among spike-specific CD4+ T cells after second vaccination dose (Figure 6C) are not differentially enriched among spike-specific CD8+ T cells. Shown are the proportions of cells that are CD127+ CD57-, CXCR4+ CD69+, or CCR7+ CD62L+ cells among spike-specific CD8+ T cells as determined by manual gating. (I) Cells co-expressing CD27 and CD38, and CTLA4 and CD137, are elevated among spike-specific CD8+ T cells from vaccinated convalescent individuals relative to vaccinated infection-naïve individuals. *p < 0.05, **p < 0.01 as determined by student’s t-test. Error bars in panels G-I correspond to mean ± SD.

We then followed up on each of these three differentially expressed markers. CD127, the alpha chain of the IL7 receptor, can drive IL7-mediated homeostatic proliferation of SARS-CoV-2-specific CD4+ T cells Neidleman et al., 2020b, and serves as a marker of long-lived precursor memory cells Kaech et al., 2003. To assess the potential longevity of the spike-specific CD4+ T cells, we determined the percentage of CD127+ cells expressing low levels of the terminal differentiation marker CD57. After the second dose of vaccination, convalescent individuals harbored more long-lived (CD127+ CD57-) spike-specific CD4+ T cells than infection-naïve individuals (Figure 6C). CXCR4, the second preferentially-expressed marker among the convalescents’ spike-specific CD4+ T cells, was recently suggested to direct bystander T cells to the lung during COVID-19, and to be co-expressed with the T resident memory / activation marker CD69 Neidleman et al., 2021. Interestingly, spike-specific CD4+ T cells from convalescent donors harbored a highly significantly elevated proportion of CXCR4+ CD69+ cells (Figure 6D), suggesting a potentially superior ability to migrate into pulmonary tissues. The last differentially expressed antigen, CCR7, is a chemokine receptor that directs immune cells to lymph nodes. As CD62L, a selectin that also mediates lymph node homing, was also on our panel, we assessed whether CCR7+ CD62L+ cells were enriched among the spike-specific CD4+ T cells from the convalescent donors, and found this to be the case (Figure 6E).

Our finding that the convalescent donors’ spike-specific CD4+ T cells were preferentially CXCR4+ CD69+ and CCR7+ CD62L + suggested that they may preferentially migrate out of the blood into lymphoid tissues. Supporting this possibility was our observation that, after the second vaccine dose, the percentages of CCR7+ CD62L + spike-specific cells increased as the percentages of spike-specific CD4+ T cells decreased (Figure 6F). This suggests that the low spike-specific CD4+ T cell response after the second dose of vaccination in some convalescent donors (Figure 1D) may have resulted from these cells preferentially leaving the blood compartment. This was further supported by our finding that the expression levels of CCR7 and CD62L on spike-specific CD4+ T cells inversely correlated with the magnitude of the spike-specific CD4+ T cell response (Figure 6G). To assess whether the CCR7+ CD62L + and CXCR4+ CD69+ CD4+ T cells have the potential to migrate into the nasopharynx, the most common site of SARS-CoV-2 entry, we obtained paired blood and nasal swabs from one of the participants (PID4101) and phenotyped total CD4+ T cells isolated from these specimens. There was a marked enrichment of both CCR7+ CD62L + and CXCR4+ CD69+ CD4+ T cells in the intranasal specimens (Figure 6H), suggesting that CD4+ T cells expressing these markers preferentially exit the blood and enter the nasopharynx. Together, these data suggest that after vaccination, spike-specific CD4+ T cells from convalescent individuals differ from those in infection-naïve individuals in that they appear to be more long-lived, and may more readily migrate out of the blood to mucosal sites, thus explaining their overall lower frequencies measured from the blood.

### Phenotypic features of spike-specific CD8+ T cells from vaccinated, convalescent individuals are unique but differ from their CD4+ T cell counterparts

Finally, we assessed to what extent the main similarities and differences observed with spike-specific CD4+ T cells were also seen for spike-specific CD8+ T cells. Similar to the CD4+ T cells, spike-specific CD8+ T cells stimulated by the three different spike proteins (ancestral, B.1.1.7, B.1.351) did not differ in their phenotypic features (Figure 6—figure supplement 1A-C). Also similar to the CD4+ T cells, spike-specific CD8+ T cells elicited by vaccination differed phenotypically in the infection-naïve vs. convalescent individuals (Figure 6—figure supplement 1D-F). Unlike the CD4+ T cell data, however, these phenotypic differences could not be accounted for by distribution changes among the main canonical subsets Tn, Tscm, Temra, Tcm, Tem, and Ttm (Figure 6—figure supplement 1G). Also unlike the CD4+ T cells, these differences were also not explained by differential abundance of the CD127+ CD57-, CXCR4+ CD69+, or CCR7+ CD62L + subsets (Figure 6—figure supplement 1H). Instead, the differences appear to be due to other phenotypic changes, including elevated frequencies of activated cells in the convalescent donors, in particular those co-expressing the Tcm marker CD27 and activation marker CD38, and the checkpoint inhibitor molecule CTLA4 and activation marker 4-1BB (Figure 6—figure supplement 1I). These results suggest that vaccine-elicited spike-specific CD8+ T cells, like their CD4+ counterparts, respond equivalently to the B.1.1.7 and B.1.351 variants, and exhibit qualitative differences in convalescent individuals but via different phenotypic alterations than their CD4+ counterparts.

## Discussion

T cells are important orchestrators and effectors during antiviral immunity. They may hold the key to long-term memory due to their ability to persist for decades, yet these cells have been disproportionately understudied relative to their humoral immune counterparts in the context of COVID-19. Here, we designed a longitudinal study assessing both the frequency and phenotypic characteristics of SARS-CoV-2-specific T cells in order to address the following questions: (1) Do SARS-CoV-2-specific T cells elicited by vaccination respond similarly to ancestral and variant strains?; (2) To what extent is the second dose needed for boosting T cell responses in infection-naïve and convalescent individuals?; and (3) Do vaccine-elicited memory T cells differ in infection-naïve vs. convalescent individuals?

To answer the first question, we compared post-vaccination SARS-CoV-2 spike-specific T cell responses against ancestral vs. the variant B.1.1.7 and B.1.351 strains. Consistent with recent studies Skelly et al., 2021; Tarke et al., 2021; Redd et al., 2021; Geers et al., 2021; Woldemeskel et al., 2021; Stankov et al., 2021; Tauzin et al., 2021, we find that vaccination-elicited T cells specific to the ancestral spike protein also recognize variant spike proteins. We further demonstrate that the phenotypic features of these cells are identical, whether they are stimulated by ancestral or variant spike proteins. This was important to establish because of prior reports that effector T cells can respond differently to APLs by altering their cytokine production or by mounting an immunoregulatory response Evavold and Allen, 1991; Sloan-Lancaster and Allen, 1996. APLs could theoretically arise when a variant infects an individual that was previously exposed to ancestral spike through vaccination or prior infection. That both the quantity and quality of T cell responses is maintained against the variants may provide an explanation for the real-world efficacy of the vaccines against variants. Although limited data are available, thus far all vaccines deployed in areas where the B.1.1.7 or B.1.351 strains dominate have protected vaccinees from severe and fatal COVID-19 Gupta, 2021. Given the potentially important role of SARS-CoV-2-specific T cells in protecting against severe and fatal COVID-19 Neidleman et al., 2021; Dan et al., 2021, we postulate that this protection may have been in large part mediated by vaccine-elicited T cells. In contrast, efficacy of the vaccines against mild or moderate disease in variant-dominated regions of the world is more variable. For example, in South Africa where B.1.351 is dominant, the AstraZeneca ChAdOx1 vaccine only prevented ~10 % of mild-to-moderate disease cases Madhi et al., 2021, while more recent data from Pfizer/BioNTech’s vaccine administered in Qatar, where both B.1.1.7 and B.1.351 are dominant, revealed that fully vaccinated individuals were 75 % less likely to develop COVID-19 Abu-Raddad et al., 2021. The overall diminished vaccine-mediated protection against milder disease in variant-dominated regions of the world might be explained by the likely important role of antibodies to prevent initial infection by blocking viral entry into host cells (manifesting as protection against asymptomatic and mildly symptomatic infection), and the observation that vaccine-elicited antibodies are generally less effective against the variant than against ancestral spike in lab assays Wang et al., 2021; The CITIID-NIHR BioResource COVID-19 Collaboration et al., 2021; Muik et al., 2021; Garcia-Beltran et al., 2021; Stamatatos et al., 2021; Cele et al., 2021; Hoffmann et al., 2021; Planas et al., 2021; Edara et al., 2021; Kuzmina et al., 2021. Reassuringly, there is no evidence that vaccinated individuals mount a weaker immune response to variants than do unvaccinated individuals, which could theoretically result through a phenomenon termed original antigenic sin (where the recall response is inappropriately diverted to the vaccination antigen at the expense of a protective response against the infecting variant strain) Klenerman and Zinkernagel, 1998.

To address the second question of whether a booster dose is needed, we compared the T cells after the first vs. second vaccination doses, among the infection-naïve and convalescent individuals. In infection-naïve individuals, spike-specific responses were observed after the first vaccination dose, and were further boosted after the second. This enhancement of the T cell response after the second dose is similar to the reported increase in anti-spike IgG levels after a second dose in infection-naïve individuals Goel et al., 2021; Ebinger et al., 2021. Interestingly, phenotypic changes were also observed after the second dose in that the B cells producing the anti-spike antibodies differentiated from IgM-dominant to IgG-dominant producers Goel et al., 2021. We also observed some phenotypic changes among spike-specific CD4+ T cells after the second dose, as reflected by an increase in the Ttm response at the expense of the Tcm response. Importantly, however, after either dose, spike-specific CD4+ T cells were still primarily Tcm and Tfh cells, the latter of which are important for providing helper function for B cells. The prominence of SARS-CoV-2-specific Tfh cells after just one dose of vaccination is consistent with prior reports that a single dose of SARS-CoV-2 mRNA in mice is sufficient to elicit potent B and Tfh cell responses in germinal centers Lederer et al., 2020. These results suggest that with regard to T cells, the booster dose is necessary for enhancing the magnitude and results in some phenotypic changes although a robust Tfh response is already established the first dose. Overall, our conclusions are in line with those drawn from serological studies Goel et al., 2021; Ebinger et al., 2021: that it is important to administer the second vaccine dose in infection-naïve individuals to boost spike-specific responses.

A different situation appears to be the case for convalescent individuals. Longitudinal serological studies suggest that the spike-specific antibody response in convalescent individuals after the first mRNA dose is already equivalent to that of infection-naïve individuals after their second mRNA dose Goel et al., 2021; Ebinger et al., 2021, suggesting that convalescent individuals may only need a single dose of vaccination. We found no evidence of increased numbers of spike-specific CD4+ T cells after the second dose, and minimal phenotypic changes between the cells at the two post-vaccination timepoints. Spike-specific CD4+ T cells from these individuals did however exhibit marked phenotypic changes as they transitioned from the pre- to the post-vaccination timepoints. This was expected since the cells from the pre-vaccination timepoint are resting memory CD4+ T cells that were primed months prior, while the post-vaccination timepoints were more recently-reactivated memory cells. Interestingly, unlike for the infection-naïve individuals where all individuals responded similarly to each dose of vaccination, the magnitude of the CD4+ T cell response differed markedly between different convalescent individuals. PID4112 had a large pool of spike-specific CD4+ T cells prior to vaccination, and their numbers increased to extremely high levels after the first vaccination dose. Surprisingly, this large peak in the spike-specific response was accompanied by an increase in the nucleocapsid-specific CD4+ T cells, which was unexpected since the vaccine does not contain nucleocapsid. We suspect this high response to nucleocapsid was due to inflammation-mediated bystander activation of T cells in an antigen-independent manner. Consistent with this hypothesis, the participant reported severe side effects (severe headache, chills, myalgia, nausea, and diarrhea) after the first dose. The remaining five convalescent donors, by contrast, never exhibited a robust T cell response, and in fact after full vaccination actually exhibited a highly significantly lower CD4+ T cell response than the infection-naïve vaccinees. We speculate on an explanation further below. Overall, our results suggest that a second SARS-CoV-2 vaccine dose in individuals who have recovered from COVID-19 may provide less benefit than in individuals who have not previously been exposed to SARS-CoV-2; these findings are in line with recommendations from previously published serological studies Stamatatos et al., 2021; Goel et al., 2021; Ebinger et al., 2021.

One of the most striking observations from this study, and the third and final question we set out to answer, was the remarkably distinct phenotypes of spike-specific CD4+ T cells from infection-naïve vs. convalescent individuals who were fully vaccinated. The spike-specific CD4+ T cells from the convalescent individuals harbored features suggesting increased potential for long-term persistence: they were enriched for Tcm cells, which are have longer in vivo half-lives than their Tem and Ttm counterparts Bacchus-Souffan et al., 2021, and express elevated levels of CD127, a marker of long-lived memory T cells Kaech et al., 2003. Interestingly, CD127 expression on SARS-CoV-2-specific T cells has been implicated in COVID-19 disease amelioration and in these cells’ long-term persistence. CD127 expression was more frequent on spike-specific CD4+ T cells from ICU patients who eventually survived severe COVID-19 than in those that did not Neidleman et al., 2021. IL7, the ligand for CD127, can drive homeostatic proliferation and expansion of spike-specific CD4+ T cells Neidleman et al., 2020b, and CD127 is not only expressed on SARS-CoV-2-specific memory CD4+ and CD8+ T cells, but its levels increase further over the course of convalescence Neidleman et al., 2020b; Ma et al., 2021. Together, these findings suggest that after vaccination, spike-specific CD4+ T cells in convalescent individuals may persist longer than those from infection-naïve individuals, but additional long-term follow-up studies will be required to directly test whether this indeed is the case.

Another interesting characteristic of post-vaccination spike-specific CD4+ T cells from convalescent individuals relative to infection-naïve individuals was their expression of multiple tissue-homing receptors. In particular, these cells were preferentially CCR7+ CD62L + and CXCR4+ CD69+. CCR7 and CD62L mediate homing to lymph nodes, while CXCR4 is a chemokine receptor important in migration of hematopoietic stem cells to bone marrow, but also able to direct immune cells to the lung during inflammation Mamazhakypov et al., 2021. Interestingly, we recently observed co-expression of CXCR4 with CD69 (an activation marker that also identifies T resident memory cells) in pulmonary T cells from COVID-19 patients Neidleman et al., 2021. Many of these cells were bystander (non-SARS-CoV-2-specific) CXCR4+ CD69+ T cells whose numbers in blood increased prior to death from COVID-19. We therefore proposed a model whereby recruitment of non-SARS-CoV-2-specific T cells into the lungs of severe patients may exacerbate the cytokine storm and thereby contribute to death Neidleman et al., 2021. In the case of the vaccinated convalescent individuals, however, expression of CXCR4 and CD69 on SARS-CoV-2-specific T cells is expected to be beneficial as it would direct the T cells capable of recognizing infected cells into the lung. CCR7 and CD62L co-expression would further enable these cells to enter draining lymph nodes and participate in germinal center reactions. Supporting the hypothesis that the post-vaccination spike-specific CD4+ T cells from convalescent individuals may better home to lymphoid tissues is our observation that frequencies of these cells in blood correlated negatively with the extent to which they co-expressed CCR7 and CD62L. This was further supported by our finding that CD4+ T cells from the nasopharynx of the upper respiratory tract were preferentially CCR7+ CD62L + and CXCR4+ CD69+ relative to their blood counterparts. All together, these results imply that compared to infection-naïve individuals, convalescents’ spike-specific CD4+ T cells may be superior in surviving and migrating to the respiratory tract. Directly testing this hypothesis will require obtaining large numbers of respiratory tract cells from vaccinated, infection-naïve vs. convalescent individuals (e.g. via bronchoalveolar lavages or endotracheal aspirates), or from animal models of SARS-CoV-2 infection, for quantitation and characterization of SARS-CoV-2-specific T cells. Of note, vaccination of infection-naïve individuals might not induce a strong humoral immunity in the respiratory mucosa either, as neutralizing antibodies against SARS-CoV-2 are rarely detected in nasal swabs from vaccinees Planas et al., 2021. If it turns out that current vaccination strategies do not ensure robust humoral and cell-mediated immune responses in the respiratory tract, then strategies that better elicit mucosal-homing SARS-CoV-2-specific B and T cells in infection-naïve individuals – for example by implementing an intranasal route of mRNA immunization – may hold a greater chance of achieving sterilizing immunity.

### Limitations

As this study was aimed at using in-depth phenotyping as a discovery tool, it focused on deeply interrogating many different conditions (e.g. spike variants, longitudinal sampling) rather than many donors. Therefore, although a total of 165 CyTOF specimens were run, only 11 donors were analyzed. The main findings reported here should be confirmed in larger cohorts using more cost-effective and high-throughput alternatives to CyTOF such as conventional flow cytometry. Such follow-up studies should also examine the functional outcomes of the discoveries made here (e.g. effect of chemokine receptor expression on homing of infection- and vaccine-elicited SARS-CoV-2-specific T cells), including in animal models of SARS-CoV-2 infection. A second limitation of the study was the need to stimulate the specimens in order to identify and characterize the vaccine-elicited T cells, and our limiting our analyses of SARS-CoV-2-specific T cells to those inducing IFNγ, which may have restricted our ability to characterize subsets such as Tfh cells that are relatively poor producers of this cytokine. We note however that we limited peptide exposure to 6 hours to minimize phenotypic changes caused by the stimulation, similar to our prior studies Neidleman et al., 2021; Neidleman et al., 2020b. Our analysis focused on CD4+ T cells because the overall numbers of detectable spike-specific CD8+ T cells were low. Nonetheless, the main findings we made with the CD4+ T cells – that they recognize variants equivalently, and that the phenotypes of the responding cells differ by prior SARS-CoV-2 natural infection status – were recapitulated among CD8+ T cells. Future studies should assess the phenotypes of non-stimulated, vaccine-elicited SARS-CoV-2-specific T cells using peptide-MHC tetramers/multimers. Such studies, however, would be limited to analyzing responses against a small number of epitopes, although use of combinatorial tetramers in conjunction with high-parameter phenotyping Newell et al., 2013 would increase the ability to characterize a larger breadth of the vaccine-elicited T cell response. Such studies however would be limited for the most part to CD8+ T cells as tetramer reagents for CD4+ T cells are less robust. A final limitation is that serological analyses were not performed in this study. As coordination between the humoral and cellular arms of immunity are likely key to effectively controlling viral replication, future studies should assess to what extent the breadth, isotypes, and functional features of spike-specific antibodies elicited by vaccination associate with the herein described phenotypic features of vaccine-elicited SARS-CoV-2-specific T cells.

## Materials and methods

**Key resources table**


<table>
  <tbody>
    <tr>
      <td>Reagent type (species) or resource</td>
      <td>Designation</td>
      <td>Source or reference</td>
      <td>Identifiers</td>
      <td>Additional information</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>HLADR(mouse monoclonal)</td>
      <td>Thermofisher</td>
      <td>Cat#Q22158</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>RORγt(rat monoclonal)</td>
      <td>Fisher Scientific</td>
      <td>Cat#5013565</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CD49d (α4)(mouse monoclonal)</td>
      <td>Fluidigm</td>
      <td>Cat#3141004B</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CTLA4(mouse monoclonal)</td>
      <td>Fisher Scientific</td>
      <td>Cat#5012919</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>NFAT(rat monoclonal)</td>
      <td>Fluidigm</td>
      <td>Cat#3143023 A</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CCR5(mouse monoclonal)</td>
      <td>Fluidigm</td>
      <td>Cat#3144007 A</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CD137(mouse monoclonal)</td>
      <td>Fisher Scientific</td>
      <td>Cat#BDB555955</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CD95(mouse monoclonal)</td>
      <td>Fisher Scientific</td>
      <td>Cat#MAB326100</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CD7(mouse monoclonal)</td>
      <td>Fluidigm</td>
      <td>Cat#3147006B</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>ICOS(hamster monoclonal)</td>
      <td>Fluidigm</td>
      <td>Cat#3148019B</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Tbet(mouse monoclonal)</td>
      <td>Fisher Scientific</td>
      <td>Cat#5013190</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>IL4(rat monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#500829</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CD2(mouse monoclonal)</td>
      <td>Fluidigm</td>
      <td>Cat#3151003B</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>IL17(mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#512331</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CD62L(mouse monoclonal)</td>
      <td>Fluidigm</td>
      <td>Cat#3153004B</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>TIGIT(mouse monoclonal)</td>
      <td>Fludigm</td>
      <td>Cat#3154016B</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CCR6(mouse monoclonal)</td>
      <td>BD Biosciences</td>
      <td>Cat#559560</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>IL6(rat monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#501115</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CD8(mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#301053</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CD19(mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#302247</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CD14(mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#301843</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>OX40(mouse monoclonal)</td>
      <td>Fluidigm</td>
      <td>Cat#3158012B</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CCR7(mouse monoclonal)</td>
      <td>Fluidigm</td>
      <td>Cat#3159003 A</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CD28(mouse monoclonal)</td>
      <td>Fluidigm</td>
      <td>Cat#3160003B</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CD45RO(mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#304239</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CD69(mouse monoclonal)</td>
      <td>Fluidigm</td>
      <td>Cat#3162001B</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CRTH2(rat monoclonal)</td>
      <td>Fluidigm</td>
      <td>Cat#3163003B</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>PD-1(mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#329941</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CD127(mouse monoclonal)</td>
      <td>Fluidigm</td>
      <td>Cat#3165008B</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CXCR5(rat monoclonal)</td>
      <td>BD Biosciences</td>
      <td>Cat#552032</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CD27(mouse monoclonal)</td>
      <td>Fluidigm</td>
      <td>Cat#3167006B</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>IFNγ(mouse monoclonal)</td>
      <td>Fluidigm</td>
      <td>Cat#3168005B</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CD45RA(mouse monoclonal)</td>
      <td>Fluidigm</td>
      <td>Cat#3169008B</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CD3(mouse monoclonal)</td>
      <td>Fluidigm</td>
      <td>Cat#3170001B</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CD57(mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#359602</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CD38(mouse monoclonal)</td>
      <td>Fluidigm</td>
      <td>Cat#3172007B</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CD4(mouse monoclonal)</td>
      <td>Fluidigm</td>
      <td>Cat#3174004B</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CXCR4(mouse monoclonal)</td>
      <td>Fluidigm</td>
      <td>Cat#3175001B</td>
      <td>(1 μg/100 μl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CD25(mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#356102</td>
      <td>(1 μg/100 μl)</td>
    </tr>
  </tbody>
</table>

### Human subjects

Eleven participants from the COVID-19 Host Immune Pathogenesis (CHIRP) cohort were recruited for this study. Six were previously infected with SARS-CoV-2 as established by RT-PCR, and had fully recovered from a mild course of disease. Importantly, infections of these six individuals had all occurred in the San Francisco Bay Area between March and July of 2020, when the dominant local strain was the original ancestral (Wuhan) strain. The remaining five participants were not previously infected with the virus. All eleven participants were vaccinated with both doses of either of the Moderna or Pfizer/BioNTech mRNA vaccines (Table 1). Blood was drawn from each of the eleven participants prior to vaccination, ~ 2 weeks after the first vaccine dose, and ~2 weeks after the second vaccine dose (33 specimens total). On the day of each blood draw, PBMCs were isolated from blood using Lymphoprep (StemCell Technologies), and then cryopreserved in 90 % fetal bovine serum (FBS) and 10 % DMSO. For participant PID4101, an additional blood-draw and intranasal swab specimens were obtained for immunophenotyping studies. This study was approved by the University of California, San Francisco, and all participants provided informed consent (IRB # 20–30588).

### Preparation of specimens for CyTOF

Cryopreserved PBMCs were revived and cultured overnight to allow for antigen recovery. The cells were then counted, and then 2 million cells per treatment condition were stimulated with the co-stimulatory agents 0.5 μg/ml anti-CD49d clone L25 and 0.5 μg/ml anti-CD28 clone L293 (both from BD Biosciences), in the presence of 0.5 μM of overlapping 15-mer SARS-CoV-2 spike peptides PepMix SARS-CoV-2 peptides from the original SARS-CoV-2 strain, B.1.1.7, or B.1.351, or overlapping 15-mer SARS-CoV-2 nucleocapsid peptides (all from JPT Peptide Technologies). Stimulations were conducted for 6 hours in RP10 media (RPMI 1640 medium (Corning) supplemented with 10 % FBS (VWR), 1 % penicillin (Gibco), and 1 % streptomycin (Gibco)), in the presence of 3 μg/ml Brefeldin A Solution (eBioscience) to enable detection of intracellular cytokines. To establish the phenotypes of total T cells in the absence of stimulation, 2 million cells were cultured in parallel with the stimulated samples, but in the presence of only 3 μg/ml Brefeldin A.

After culture, the cells were treated with cisplatin (Sigma-Aldrich) as a live/dead marker and fixed with paraformaldehyde (PFA) as previously described Neidleman et al., 2020b; Ma et al., 2020. Cisplatin treatment and fixation was performed as follows: first, cells were resuspended in 2 ml PBS (Rockland) with 2 ml EDTA (Corning), followed by addition of 2 ml PBS/EDTA supplemented with 25 μM cisplatin (Sigma-Aldrich) for 60 s. Cisplatin staining was then quenched with 10 ml of CyFACS (metal contaminant-free PBS (Rockland) supplemented with 0.1 % FBS and 0.1 % sodium azide (Sigma-Aldrich)), centrifuged, and resuspended in 2 % PFA in CyFACS. Fixation was allowed to proceed for 10 minutes at room temperature, after which cells were washed twice with CyFACS, and then resuspended in CyFACS containing 10 % DMSO. Fixed cells were stored at –80 °C until analysis by CyTOF. For paired blood/swab specimens from PID4101, cells were immediately cisplatin-treated and fixed, without prior cryopreservation.

### CyTOF staining and data acquisition

CyTOF staining was conducted in a fashion similar to recently described methods Neidleman et al., 2021; Neidleman et al., 2020b; Ma et al., 2020; Cavrois et al., 2017; Neidleman et al., 2020a; Xie et al., 2021. Cisplatin-treated cells were thawed, counted, and each treatment condition was barcoded using the Cell-ID 20-Plex Pd Barcoding Kit (Fluidigm). After the cells were barcoded and washed, the barcoded samples were combined and diluted to 6 × 106 cells / 800 μl CyFACS per well in Nunc 96 DeepWell polystyrene plates (Thermo Fisher). Cells were blocked with mouse (Thermo Fisher), rat (Thermo Fisher), and human AB (Sigma-Aldrich) sera for 15 min at 4 °C, and then washed twice in CyFACS. Surface CyTOF antibody staining (Table 2) was conducted for 45 min at 4 °C, in a volume of 100 μl / sample. Cells were then washed three times with CyFACS and fixed overnight at 4 °C in 100 μl of 2 % PFA in PBS. The next day, samples were washed twice with Intracellular Fixation & Permeabilization Buffer (eBioscience), and incubated for 45 minutes at 4 °C. After two additional washes with Permeabilization Buffer (eBioscience), samples were blocked for 15 min at 4 °C in 100 μl of Permeabilization Buffer containing mouse and rat sera. After one additional wash with Permeabilization Buffer, samples were stained with the intracellular CyTOF antibodies (Table 2) at 4 °C for 45 min in a volume of 100 μl / sample. Cells were then washed once with CyFACS, and stained for 20 min at room temperature with 250 nM of Cell-ID Intercalator-IR (Fluidigm). Immediately prior to sample acquisition, cells were washed twice with CyFACS buffer, once with MaxPar cell staining buffer (Fluidigm), and once with Cell acquisition solution (CAS, Fluidigm). Cells were resuspended in EQ Four Element Calibration Beads (Fluidigm) diluted in CAS immediately prior to acquisition on a Helios-upgraded CyTOF2 instrument (Fluidigm) at the UCSF Parnassus flow core facility.

### CyTOF data analysis

CyTOF datasets, exported as flow cytometry standard (FCS) files, were de-barcoded and normalized according to manufacturer’s instructions (Fluidigm). FlowJo software (BD Biosciences) was used to identify CD4+ T cells (live, singlet CD3+ CD19 CD4+ CD8-) and CD8+ T cells (live, singlet CD3+ CD19 CD4-CD8+) among all analyzed samples. IFNγ+ in the stimulated samples were considered to be the SARS-CoV-2-responsive cells. For high-dimensional analyses of SARS-CoV-2-specific T cells among the stimulated samples, we excluded samples with an insufficient number of events ( ≤ 3) to limit skewing of the data. Manual gating analysis was initially performed using FlowJo, and then select populations were exported as FCS files and then imported into R software as GatingSet objects. Using the CytoExploreR package, 2D-gates were manually drawn on the imported samples. The 2D dot plots and statistical results were exported for data visualization, bar-graph generation, and statistical comparisons as previously described (https://github.com/DillonHammill/CytoExploreR; Hammill, 2021). High-dimensional analyses (MDS, tSNE, and FlowSOM) were performed using R software by implementing a CyTOF workflow recently described Nowicka et al., 2017.

For MDS plot generation, we used the plotMDS function from the limma package with default settings. Euclidean distances between all samples were calculated using the arcsinh-transformed median expression levels with cofactor 5, of the lineage and functional markers listed below.

<table>
  <thead>
    <tr>
      <th>CD8</th>
      <th>Lineage(Only for CD8 subset)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CD4</td>
      <td>Lineage(Only for CD4 subset)</td>
    </tr>
    <tr>
      <td>CD161</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>HLADR</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>CD45RO</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>CD69</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>CRTH2</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>PD1</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>CXCR5</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>CD27</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>CD3</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>CD2</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>CD62L</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>CCR6</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>OX40</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>CD28</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>CD127</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>RORγt</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>CXCR4</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>CTLA4</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>NFAT</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>CCR5</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>CD137</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>CD95</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>ICOS</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>CD49d</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>CD7</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>Tbet</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>TIGIT</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>CCR7</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>CD45RA</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>CD57</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>CD38</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>α4β7</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>CD25</td>
      <td>Lineage</td>
    </tr>
    <tr>
      <td>IFNγ</td>
      <td>Function</td>
    </tr>
    <tr>
      <td>IL6</td>
      <td>Function</td>
    </tr>
    <tr>
      <td>IL4</td>
      <td>Function</td>
    </tr>
    <tr>
      <td>IL17</td>
      <td>Function</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

The first (MDS1) and second (MDS2) MDS dimensions were plotted to show the dissimilarities between samples from the indicated conditions as described Ritchie et al., 2015.

tSNE was performed using the Trsne function from the Rtsne package using arcsinh-transformed expression of lineage markers (no PCA step, iterations = 1000,, perplexity = 30, theta = 0.5). Events corresponding to unstimulated T cells were down-sampled to 1000 cells per sample, and SARS-CoV-2-specific cells (cell numbers ranging from 4 to 229 per sample) were all included in the tSNE analyses without down-sampling. Each cell was displayed in a tSNE plot for dimension reduction visualization and colored with arcsinh-transformed cell marker expression as heatmaps, or pseudo-colored by the appropriate group.

Unsupervised cell subset clustering was performed using FlowSOM Van Gassen et al., 2015 and ConsensusClusterPlus packages using arcsinh-transformed expression levels of the lineage markers indicated above Wilkerson and Hayes, 2010. For clustering of SARS-CoV-2-specific T cells, we set the meta-cluster number to eight and cluster number to 40. The frequency of each cluster within each sample was calculated using the following equation:

(Frequency of cluster in specified sample) = (Cell count of cluster / Total cell count of specified sample).

This was then converted to a percentage by multiplying by 100. The percentages of each cluster from the selected samples were plotted as box plots with jittered points, followed by statistical analysis between the groups. To compare the abundance distribution of clusters between groups, frequencies of clusters in samples from each group were normalized using the equation below:

(Normalized frequency of cluster in specified sample) = (Frequency of cluster in specified sample/ Total number of samples in each group).

This was then converted to a percentage by multiplying by 100, and plotted as stacked bar charts.

### Statistical analysis

The statistical tests used in comparison of groups are indicated within the figure legends. For 2-group comparisons, student’s t-tests were performed and p-values were adjusted for multiple testing using the Holm-Sidak method where applicable. For comparisons of three or more groups, significance between groups was first evaluated by one-way ANOVA, and then the p-values were adjusted for multiple testing using the Holm-Sidak method where applicable. For datasets with significant ANOVA-adjusted p-values ( ≤ 0.05), we performed Tukey’s honestly significant difference (HSD) post-hoc test to determine the p-values between individual groups.

### Raw data availability

For this study, a total of 120 specimens were analyzed by CyTOF. Each specimen included both CD4+ and CD8+ T cells. For each specimen, we gated separately on events corresponding to CD4+ T cells (live, singlet CD3+ CD19- CD4+ CD8-) and CD8+ T cells (live, singlet CD3+ CD19- CD4 CD8+), and exported the files as 240 individual FCS files. These 240 raw CyTOF datasets are available for download through the public repository Dryad via the following link: https://doi.org/10.7272/Q60R9MMK.
