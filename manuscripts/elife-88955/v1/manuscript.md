# Absence of electron-transfer-associated changes in the time-dependent X-ray free-electron laser structures of the photosynthetic reaction center

## Authors

- Gai Nishikawa<sup>1</sup>
- Yu Sugo<sup>1</sup>
- Keisuke Saito<sup>1</sup> ([ORCID: 0000-0002-2293-9743](https://orcid.org/0000-0002-2293-9743))
- Hiroshi Ishikita<sup>1</sup> ([ORCID: 0000-0002-5849-8150](https://orcid.org/0000-0002-5849-8150)) †

### Affiliations

1. Department of Applied Chemistry, The University of Tokyo Tokyo Japan ([ROR:057zh3y96](https://ror.org/057zh3y96))
2. Research Center for Advanced Science and Technology, The University of Tokyo Tokyo Japan ([ROR:057zh3y96](https://ror.org/057zh3y96))

† Corresponding author

## Abstract

Using the X-ray free-electron laser (XFEL) structures of the photosynthetic reaction center from Blastochloris viridis that show light-induced time-dependent structural changes (Dods et al., (2021) Nature 589, 310–314), we investigated time-dependent changes in the energetics of the electron-transfer pathway, considering the entire protein environment of the protein structures and titrating the redox-active sites in the presence of all fully equilibrated titratable residues. In the dark and charge separation intermediate structures, the calculated redox potential (Em) values for the accessory bacteriochlorophyll and bacteriopheophytin in the electron-transfer-active branch (BL and HL) are higher than those in the electron-transfer-inactive branch (BM and HM). However, the stabilization of the charge-separated [PLPM]•+HL•– state owing to protein reorganization is not clearly observed in the Em(HL) values in the charge-separated 5 ps ([PLPM]•+HL•– state) structure. Furthermore, the expected chlorin ring deformation upon formation of HL•– (saddling mode) is absent in the HL geometry of the original 5 ps structure. These findings suggest that there is no clear link between the time-dependent structural changes and the electron-transfer events in the XFEL structures.

## Introduction

Photosynthetic reaction centers from purple bacteria (PbRC) are heterodimeric reaction centers, which are formed by the protein subunits L and M (Figure 1). In PbRC from Blastochloris viridis, the electronic excitation of the bacteriochlorophyll b (BChlb) pair, [PLPM], leads to electron transfer to accessory BChlb, BL, followed by electron transfer via bacteriopheophytin b (BPheob), HL, to menaquinone, QA, along the electron-transfer active L-branch (A-branch) (Deisenhofer et al., 1985). Electron transfer further proceeds from QA to ubiquinone, QB, which is coupled with proton transfer via charged and polar residues in the QB binding region (Rabenstein et al., 1998). Although the counterpart M-branch (B-branch) is essentially electron-transfer inactive, mutations of the Phe-L181/Tyr-M208 pair to tyrosine/phenylalanine lead to an increase in the yield of [PLPM]•+HM•– formation (~30%), which suggests that these residues are responsible for the energetic asymmetry in the electron-transfer branches (e.g., Kirmaier et al., 2003). The anionic states BL•–, HL•–, and QA•– form in ~3.5 ps, ~5 ps, and ~200 ps upon the formation of the electronically excited [PLPM]* state, respectively (Holzapfel et al., 1990). The anionic state formation induces not only reoriganization of the protein environment (Marcus and Sutin, 1985) but also out-of-plane distortion of the chlorin ring (Saito et al., 2012). Two distinct conformations of HL•– were reported in spectroscopic studies of PbRC from Rhodobacter sphaeroides (Müh et al., 1998).

![Figure 1.](https://cdn.elifesciences.org/articles/88955/elife-88955-fig1-v1.jpg)

**Figure 1.:** The PbRC is composed of the L (red), M (blue), H (gold), and C (yellow) subunits. [PLPM]: BChlb pair; BL and BM: accessory BChlb; HL and HM: BPheob; QA: primary quinone (menaquinone); Fe: non-heme Fe complex.

Recently, using the X-ray free-electron laser (XFEL), light-induced electron density changes and structural changes of PbRC were analyzed at 1 ps, 5 ps, 20 ps, 300 ps, and 8 μs upon the electronic excitation of [PLPM] at 960 nm (Dods et al., 2021): the 1 ps XFEL structure represents the [PLPM]* state, the 5 ps and 20 ps XFEL structures represent the charge-separated [PLPM]•+HL•– state, and the 300 ps and 8 μs XFEL structures represent the charge-separated [PLPM]•+QA•– state. According to Dods et al., 2021, these XFEL structures revealed how the charge separation process was stabilized by protein conformational dynamics. However, the conclusions drawn from these XFEL structures are based on data with limited resolution. Specifically, eight out of nine XFEL structures have a relatively low resolution of 2.8 Å (atomic coordinates from PDB codes: 5O4C, 6ZI4, and 6ZI5 for dataset a and 6ZHW, 6ZID, 6ZI6, 6ZI9, and 6ZIA for dataset b) (Dods et al., 2021). In addition, the data statistics may indicate that the high-resolution range of some XFEL datasets exhibits high levels of noise (e.g., low CC1/2). These observations raise concerns about the reliable comparison of subtle conformational changes among these XFEL structures. Hence, caution must be exercised when interpreting these XFEL structures in terms of their ability to accurately capture relevant conformational changes.

Here, we investigated how the redox potential (Em) values of the BChlb and BPheob cofactors for one-electron reduction change as electron transfer proceeds using the dark (0 ps), 1 ps, 5 ps, 20 ps, 300 ps, and 8 μs XFEL structures, solving the linear Poisson-Boltzmann equation, and considering the protonation states of all titratable sites in the entire protein. Structural changes (e.g., side-chain reorientation) in the protein environment can be analyzed in the Em shift, as Em is predominantly determined by the sum of the electrostatic interactions between the redox-active site and all other groups (i.e., residues and cofactors) in the protein structure. Subtle structural changes of the BChlb and BPheob chlorin rings, which may not be pronounced even in the Em shift (Saito et al., 2012), can be analyzed in the out-of-plane distortion of the chlorin rings using a normal-coordinate structural decomposition (NSD) analysis (Jentzen et al., 1997; Shelnutt et al., 1998) with a combination of a quantum mechanical/molecular mechanical (QM/MM) approach in the entire PbRC protein environment.

## Results and discussion

### Energetically asymmetric electron-transfer branches

The XFEL structures show that the Em values for BL are ~50 mV higher than those for BM, which facilitates the formation of the charge-separated [PLPM]•+BL•– state and thereby electron transfer along the L-branch (Figures 2 and 3). As the Em profile is substantially consistent with the Em profile for PbRC from R. sphaeroides (Kawashima and Ishikita, 2018), it seems plausible that the charge-separated [PLPM]•+BL•– and [PLPM]•+HL•– states in the active L-branch are energetically lower than the [PLPM]•+BM•– and [PLPM]•+HM•– states in the inactive M-branch, respectively, as demonstrated in QM/MM calculations (Tamura et al., 2020). Indeed, the calculated Em values are largely correlated with the lowest unoccupied molecular orbital (LUMO) levels calculated using a QM/MM approach, as suggested previously (coefficient of determination R2=0.98, Figure 2—figure supplement 1). The Em(HL) value of –597 mV (in dataset a; –598 mV in dataset b) is in line with the experimentally estimated value of ca. –600 mV for HL in PbRC from B. viridis (Rutherford et al., 1979).

![Figure 2.](https://cdn.elifesciences.org/articles/88955/elife-88955-fig2-v1.jpg)

**Figure 2.:** (a) 0 ps. (b) 5 ps. (c) 300 ps.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/88955/elife-88955-fig2-figsupp1-v1.jpg)

![Figure 3.](https://cdn.elifesciences.org/articles/88955/elife-88955-fig3-v1.jpg)

**Figure 3.:** (a) 0 ps. (b) 1 ps. (c) 5 ps. (d) 20 ps. (e) 300 ps. (f) 8 μs.

Among the L/M residue pairs, the Phe-L181/Tyr-M208 pair contributes to Em(BL)>Em(BM) most significantly (25 mV), facilitating L-branch electron transfer, as suggested in theoretical studies (Gunner et al., 1996; Table 1, Figure 2; Figure 3; Figure 4). This result is also consistent with the contribution of the Phe-L181/Tyr-M210 pair to the difference between Em(BL) and Em(BM), which was the largest in PbRC from R. sphaeroides (Parson et al., 1990) (26 mV; Kawashima and Ishikita, 2018). The Asn-L158/Thr-M185 pair also contributes to the difference between Em(BL) and Em(BM) (12 mV, Table 1), as does the Val-L157/Thr-M186 pair in PbRC from R. sphaeroides (22 mV; Kawashima and Ishikita, 2018).

**Table 1.**
 Contributions of the L/M residue pairs that are responsible for Em(BL)>Em(BM) (more than 10 mV) in the dark-state structure (mV).Difference: [contribution of subunit L to Em(BL)] + [contribution of subunit M to Em(BL)] – [contribution of subunit L to Em(BM)] – [contribution of subunit M to Em(BM)].


<table>
  <thead>
    <tr>
      <th>Subunit L</th>
      <th>Em(BL)</th>
      <th>Em(BM)</th>
      <th>Subunit M</th>
      <th>Em(BL)</th>
      <th>Em(BM)</th>
      <th>Difference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Phe-L181</td>
      <td>0</td>
      <td>17</td>
      <td>Tyr-M208</td>
      <td>39</td>
      <td>–3</td>
      <td>25</td>
    </tr>
    <tr>
      <td>His-L144</td>
      <td>–8</td>
      <td>–2</td>
      <td>Glu-M171</td>
      <td>–14</td>
      <td>–45</td>
      <td>25</td>
    </tr>
    <tr>
      <td>Asn-L158</td>
      <td>5</td>
      <td>–6</td>
      <td>Thr-M185</td>
      <td>–3</td>
      <td>–4</td>
      <td>12</td>
    </tr>
  </tbody>
</table>

![Figure 4.](https://cdn.elifesciences.org/articles/88955/elife-88955-fig4-v1.jpg)

For dataset b, the Em values for HL are >50 mV higher than those for HM , as observed in Em(BL) and Em(BM) (Figure 3). However, the Em difference decreases to ~30 mV in the 8 μs XFEL structure (Figure 3f), which implies that the 8 μs XFEL structure is distinct from the other XFEL structures (see below). Below, we discuss the dark-state structure if not otherwise specified.

The Ala-L120/Asn-M147 pair contributes to Em(HL)>Em(HM) most significantly (38 mV) (Table 2, Figure 5). However, this holds true only for PbRC from B. viridis, as Asn-M147 is replaced with alanine (Ala-M149) in PbRC from R. sphaeroides. The Asp-L218/Trp-M252 pair decreases Em(HM) with respect to Em(HL), thereby contributing to Em(HL)>Em(HM) (20 mV) (Table 2; Figure 5). Arg-L103 orients toward the protein interior, whereas Arg-M130 orients toward the protein exterior (Figure 5), which contributes to Em(HL)>Em(HM) (17 mV) (Table 2). Ser-M271 forms an H-bond with Asn-M147 near HM (Figure 5). Thus, the contribution of Ser-M271 to Em(HL) is large, although this residue is replaced with alanine (Ala-M273) in PbRC from R. sphaeroides.

**Table 2.**
 Contributions of the L/M residue pairs that are responsible for Em(HL)>Em(HM) (more than 10 mV) in the dark-state structure (mV).Difference: [contribution of subunit L to Em(HL)] + [contribution of subunit M to Em(HL)] – [contribution of subunit L to Em(HM)] – [contribution of subunit M to Em(HM)].


<table>
  <thead>
    <tr>
      <th>Subunit L</th>
      <th>Em(HL)</th>
      <th>Em(HM)</th>
      <th>Subunit M</th>
      <th>Em(HL)</th>
      <th>Em(HM)</th>
      <th>Difference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ala-L120</td>
      <td>–4</td>
      <td>0</td>
      <td>Asn-M147</td>
      <td>0</td>
      <td>–42</td>
      <td>38</td>
    </tr>
    <tr>
      <td>Asp-L218</td>
      <td>–2</td>
      <td>–22</td>
      <td>Trp-M252</td>
      <td>1</td>
      <td>0</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Arg-L103</td>
      <td>77</td>
      <td>3</td>
      <td>Arg-M130</td>
      <td>3</td>
      <td>59</td>
      <td>17</td>
    </tr>
    <tr>
      <td>Ala-L237</td>
      <td>–2</td>
      <td>0</td>
      <td>Ser-M271</td>
      <td>3</td>
      <td>–16</td>
      <td>16</td>
    </tr>
    <tr>
      <td>Lys-L110</td>
      <td>17</td>
      <td>2</td>
      <td>Ala-M137</td>
      <td>0</td>
      <td>3</td>
      <td>14</td>
    </tr>
    <tr>
      <td>Val-L219</td>
      <td>1</td>
      <td>5</td>
      <td>Thr-M253</td>
      <td>17</td>
      <td>1</td>
      <td>11</td>
    </tr>
    <tr>
      <td>His-L211</td>
      <td>1</td>
      <td>0</td>
      <td>Arg-M245</td>
      <td>14</td>
      <td>4</td>
      <td>11</td>
    </tr>
  </tbody>
</table>

![Figure 5.](https://cdn.elifesciences.org/articles/88955/elife-88955-fig5-v1.jpg)

### Relevance of structural changes observed in XFEL structures

According to Dods et al., the 5 ps and 20 ps structures correspond to the charge-separated [PLPM]•+HL•– state (Dods et al., 2021). If this is the case, Em(HL) is expected to be exclusively higher in the 5 ps and 20 ps structures than in the other XFEL structures due to the stabilization of the [PLPM]•+HL•– state by protein reorganization. In dataset a, the Em(HL) value is only 4 mV higher in the 5 ps structure than in the dark structure (Figure 6a). In dataset b, the Em(HL) value is ~20 mV higher in the 5 ps and 20 ps structures than in the dark structure (Figure 6b). However, the Em(HL) value is 25 mV higher in the 300 ps structure than in the dark structure. Tables 3 and 4 show the residues that contribute to the slight increase in Em(HL) most significantly in the 5 ps and 20 ps structures. Most of these residues were in the region where Dods et al. specifically performed multiple rounds of partial occupancy refinement (e.g., 153–178, 190, 230, and 236–248 of subunit L and 193–221, 232, 243–253, 257–266 of subunit M) (Dods et al., 2021). In dataset b (Table 4), which has more data points than dataset a (Table 3), the contributions of these residues to Em(HL) often fluctuate (e.g., upshift/downshift followed by downshift/upshift) at different time intervals (e.g., 1–5 ps, 5–20 ps, and 20–300 ps). This result suggests that the structural differences among the XFEL structures are not related to the actual time course of charge separation. Furthermore, the Em(HM) value in the inactive M-branch is also ~15 mV higher in the 5 ps and 20 ps structures than in the dark structure (Figure 6b). These results suggest that the ~20 mV higher Em(HL) value in the 5 ps and 20 ps structures is not specifically due to the formation of the [PLPM]•+HL•– state. Thus, the stabilization of the [PLPM]•+HL•– state owing to protein reorganization is not clearly observed in the Em(HL) values.

![Figure 6.](https://cdn.elifesciences.org/articles/88955/elife-88955-fig6-v1.jpg)

**Figure 6.:** (a) Dataset a. (b) Dataset b. ΔEm denotes the Em shift with respect to the dark-state structure. Black solid lines: PL; black dotted lines: PM; blue solid lines BL; blue dotted lines: BM; red solid lines: HL; red dotted lines: HM.

**Table 3.**
 Residues that shift Em(HL) most significantly during putative electron transfer in the XFEL structures (dataset a) (mV).The same residues are highlighted in the same colors for clarity.


<table>
  <thead>
    <tr>
      <th>Dataset a</th>
      <th></th>
      <th>Shift</th>
      <th></th>
      <th>Shift</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0–5 ps</td>
      <td>Ser-L176</td>
      <td>5</td>
      <td>Cys-M210</td>
      <td>4</td>
    </tr>
    <tr>
      <td></td>
      <td>Thr-M220</td>
      <td>–7</td>
      <td>BL</td>
      <td>–5</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>5–300 ps</td>
      <td>BL</td>
      <td>7</td>
      <td>Gly-M209</td>
      <td>3</td>
    </tr>
    <tr>
      <td></td>
      <td>Gly-M211</td>
      <td>–11</td>
      <td>Leu-M212</td>
      <td>–8</td>
    </tr>
  </tbody>
</table>

**Table 4.**
 Residues that shift Em(HL) most significantly during putative electron transfer in the XFEL structures (dataset b) (mV).The same residues are highlighted in the same colors for clarity.


<table>
  <thead>
    <tr>
      <th>Dataset b</th>
      <th></th>
      <th>Shift</th>
      <th></th>
      <th>Shift</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0–1 ps</td>
      <td>Ser-L238</td>
      <td>8</td>
      <td>Ser-L176</td>
      <td>7</td>
    </tr>
    <tr>
      <td></td>
      <td>BL</td>
      <td>–7</td>
      <td>Leu-M213</td>
      <td>–3</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>1–5 ps</td>
      <td>Gly-M211</td>
      <td>6</td>
      <td>Leu-M213</td>
      <td>5</td>
    </tr>
    <tr>
      <td></td>
      <td>Ser-L238</td>
      <td>–6</td>
      <td>Thr-M253</td>
      <td>–5</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>5–20 ps</td>
      <td>BL</td>
      <td>12</td>
      <td>Thr-M253</td>
      <td>7</td>
    </tr>
    <tr>
      <td></td>
      <td>Leu-M213</td>
      <td>–4</td>
      <td>PM</td>
      <td>–3</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>20–300 ps</td>
      <td>Ser-L238</td>
      <td>3</td>
      <td>Gly-M211</td>
      <td>2</td>
    </tr>
    <tr>
      <td></td>
      <td>BL</td>
      <td>–10</td>
      <td>Glu-L212</td>
      <td>–4</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>300 ps to 8 μs</td>
      <td>Glu-L212</td>
      <td>4</td>
      <td>Leu-M213</td>
      <td>4</td>
    </tr>
    <tr>
      <td></td>
      <td>BL</td>
      <td>–6</td>
      <td>Gly-M211</td>
      <td>–5</td>
    </tr>
  </tbody>
</table>

An NSD analysis (Jentzen et al., 1997; Shelnutt et al., 1998) of the out-of-plane distortion of the chlorin ring is sensitive to subtle structural changes in the chlorin ring, which are not distinct in the Em changes (Saito et al., 2012). QM/MM calculations indicate that HL•– formation induces the saddling mode in the chlorin ring, which describes the movement of rings I and III being in the opposite direction to the movement of rings II and IV along the normal axis of the chlorin ring (Tables 5 and 6). However, (i) in the XFEL structures, the saddling mode of HL remains practically unchanged in dataset a during electron transfer (Figure 7 and Supplementary files 1 and 2). In dataset b, the saddling mode of HL is induced most significantly at 1 ps, which does not correspond to the charge-separated [PLPM]•+HL•– state (Figure 8). (ii) In addition, the ruffling mode is more pronounced than the saddling mode in HL (Figure 8), which suggests that the observed deformation of HL is not directly associated with the reduction of HL.

**Table 5.**
 Induced out-of-plane distortion of HL and HM in the PbRC protein environment of the dark structure for dataset a in response to the reduction (Å).Table 5—source data 1.Numerical source data for Table 5.


<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th>Saddling</th>
      <th>Ruffling</th>
      <th>Doming</th>
      <th>Waving</th>
      <th></th>
      <th>Propellering</th>
    </tr>
    <tr>
      <th>B2u</th>
      <th>B1u</th>
      <th>A2u</th>
      <th>Eg(x)</th>
      <th>Eg(y)</th>
      <th>A1u</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>HL</td>
      <td>0.18</td>
      <td>0.35</td>
      <td>–0.10</td>
      <td>0.13</td>
      <td>–0.11</td>
      <td>0.13</td>
    </tr>
    <tr>
      <td>HL•–</td>
      <td>0.24</td>
      <td>0.35</td>
      <td>–0.09</td>
      <td>0.12</td>
      <td>–0.12</td>
      <td>0.13</td>
    </tr>
    <tr>
      <td>(PL•+HL•–)</td>
      <td>(0.22)</td>
      <td>(0.36)</td>
      <td>(–0.07)</td>
      <td>(0.13)</td>
      <td>(–0.13)</td>
      <td>(0.13)</td>
    </tr>
    <tr>
      <td>HL/HL•– difference</td>
      <td>0.06</td>
      <td>0.00</td>
      <td>0.01</td>
      <td>–0.01</td>
      <td>–0.01</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>HM</td>
      <td>0.06</td>
      <td>0.40</td>
      <td>–0.20</td>
      <td>0.37</td>
      <td>0.12</td>
      <td>0.19</td>
    </tr>
    <tr>
      <td>HM•–</td>
      <td>0.12</td>
      <td>0.38</td>
      <td>–0.22</td>
      <td>0.33</td>
      <td>0.09</td>
      <td>0.22</td>
    </tr>
    <tr>
      <td>(PL•+HM•–)</td>
      <td>(0.14)</td>
      <td>(0.38)</td>
      <td>(–0.22)</td>
      <td>(0.33)</td>
      <td>(0.10)</td>
      <td>(0.22)</td>
    </tr>
    <tr>
      <td>HM/HM•– difference</td>
      <td>0.06</td>
      <td>–0.02</td>
      <td>–0.02</td>
      <td>–0.04</td>
      <td>–0.03</td>
      <td>0.03</td>
    </tr>
  </tbody>
</table>

**Table 6.**
 Induced out-of-plane distortion of HL and HM in the PbRC protein environment of the dark structure for dataset b in response to the reduction (Å).Table 6—source data 1.Numerical source data for Table 6.


<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th>Saddling</th>
      <th>Ruffling</th>
      <th>Doming</th>
      <th>Waving</th>
      <th></th>
      <th>Propellering</th>
    </tr>
    <tr>
      <th>B2u</th>
      <th>B1u</th>
      <th>A2u</th>
      <th>Eg(x)</th>
      <th>Eg(y)</th>
      <th>A1u</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>HL</td>
      <td>0.13</td>
      <td>0.35</td>
      <td>–0.13</td>
      <td>0.07</td>
      <td>–0.09</td>
      <td>0.20</td>
    </tr>
    <tr>
      <td>HL•–</td>
      <td>0.25</td>
      <td>0.34</td>
      <td>–0.02</td>
      <td>0.12</td>
      <td>–0.16</td>
      <td>0.13</td>
    </tr>
    <tr>
      <td>(PL•+HL•–)</td>
      <td>(0.23)</td>
      <td>(0.34)</td>
      <td>(–0.03)</td>
      <td>(0.12)</td>
      <td>(–0.16)</td>
      <td>(0.12)</td>
    </tr>
    <tr>
      <td>HL/HL•– difference</td>
      <td>0.12</td>
      <td>–0.01</td>
      <td>0.11</td>
      <td>0.05</td>
      <td>–0.07</td>
      <td>–0.07</td>
    </tr>
    <tr>
      <td>HM</td>
      <td>0.08</td>
      <td>0.57</td>
      <td>–0.11</td>
      <td>0.16</td>
      <td>0.20</td>
      <td>0.32</td>
    </tr>
    <tr>
      <td>HM•–</td>
      <td>0.16</td>
      <td>0.36</td>
      <td>–0.19</td>
      <td>0.36</td>
      <td>0.18</td>
      <td>0.21</td>
    </tr>
    <tr>
      <td>(PL•+HM•–)</td>
      <td>(0.16)</td>
      <td>(0.36)</td>
      <td>(–0.20)</td>
      <td>(0.36)</td>
      <td>(0.18)</td>
      <td>(0.21)</td>
    </tr>
    <tr>
      <td>HM/HM•– difference</td>
      <td>0.08</td>
      <td>–0.21</td>
      <td>–0.08</td>
      <td>0.20</td>
      <td>–0.02</td>
      <td>–0.11</td>
    </tr>
  </tbody>
</table>

![Figure 7.](https://cdn.elifesciences.org/articles/88955/elife-88955-fig7-v1.jpg)

**Figure 7.:** Sad: saddling (red); ruf: ruffling (blue); dom: doming (green); wav(x, y): waving (x, y) (gray, dark blue); pro: propellering (orange). Solid and dotted lines indicate L- and M-branches, respectively. See Supplementary file 1 for the absolute values in the dark state for dataset a.

![Figure 8.](https://cdn.elifesciences.org/articles/88955/elife-88955-fig8-v1.jpg)

**Figure 8.:** Sad: saddling (red); ruf: ruffling (blue); dom: doming (green); wav(x, y): waving (x, y) (gray, dark blue); pro: propellering (orange). Solid and dotted lines indicate L- and M-branches, respectively. See Supplementary file 2 for the absolute values in the dark state for dataset b Figure 8—source data 1.

One might argue that the loss of the link between the formation of the charge-separated state and the Em(HL) change (Figure 6) is not due to experimental errors, including data processing artifacts, but rather represents the actual ps timescale phenomena during the primary charge-separation reactions (e.g., Dods et al. noted that ‘the primary electron-transfer step to HL is more rapid than conventional Marcus theory’; Dods et al., 2021). Even if this were the case, this hypothesis regarding the relevance of the XFEL structures to the electron-transfer events could be further explored by examining the changes in Em(QA) among the XFEL structures, considering the relatively slow electron-transfer step to QA that allows sufficient protein relaxation to occur (e.g., Dods et al. stated that ‘the electron-transfer step to QA has a single exponential decay time of 230±30 ps, consistent with conventional Marcus theory’; Dods et al., 2021). That is, if the Em(QA) values are not higher in the 300 ps and 8 μs structures than in the other structures, it suggests that significant experimental errors exist, rendering the XFEL structures irrelevant to the electron-transfer events. Consistent with this perspective, the present results demonstrate that the Em(QA) values in the 300 ps and 8 μs structures are not significantly higher than those in the other structures, including the dark-state structure (Figure 9). Consequently, the lack of a clear relationship between the charge-separated state and the changes in Em(QA) at 300 ps and 8 μs further strengthens the argument that the XFEL structures are irrelevant to the electron-transfer events.

![Figure 9.](https://cdn.elifesciences.org/articles/88955/elife-88955-fig9-v1.jpg)

**Figure 9.:** (a) Dataset a. (b) Dataset b. ΔEm denotes the Em shift with respect to the dark-state structure. Note that the calculated Em(QA) values for dataset a and dataset b in the dark structure are –223 mV and –209 mV, respectively, which are comparable to experimentally measured values of –150 mV for PbRC from B. viridis (menaquinone) (Prince et al., 1976) and –180 mV for PbRC from R. sphaeroides (ubiquinone) (Prince and Dutton, 1976).

In summary, the Em values in the active L-branch are higher than those in the inactive M-branch in the XFEL structures, which suggests that electron transfer via BL•– and HL•– is energetically more favored than that via BM•– and HM•– (Figure 2). The Phe-L181/Tyr-M208 pair contributes to the difference between Em(BL) and Em(BM) the most significantly, as observed in the Phe-L181/Tyr-M210 pair in PbRC from R. sphaeroides (Kawashima and Ishikita, 2018; Parson et al., 1990). The stabilization of the [PLPM]•+HL•– state owing to protein reorganization is not clearly observed in the Em(HL) values (Figure 6). The absence of the induced saddling mode in the HL chlorin ring in the 5 ps and 20 ps structures suggests that HL•– does not specifically exist in these XFEL structures (Figures 7 and 8). The cyclic fluctuations in the contributions of the residues to Em(HL) at different time intervals suggest that the structural differences among the XFEL structures are not related to the actual time course of charge separation (Table 4). The major limitation of the structural studies conducted by Dods et al., 2021, is the relatively low resolution of their XFEL structures, primarily at 2.8 Å. Consequently, the observed changes in Em values and chlorin ring deformations are more likely to reflect experimental errors or data processing artifacts rather than actual structural changes induced by electron-transfer events. This concern is reinforced by the lack of a clear relationship between the actual QA•– formation and the Em(QA) values in the 300 ps and 8 μs structures (Figure 9). Consequently, the time-dependent structural changes proposed by Dods et al., 2021, are highly likely irrelevant to the electron-transfer events.

Hence, it is crucial to exercise caution when interpreting time-dependent XFEL structures, especially in the absence of comprehensive evaluations of the energetics for accompanying structural changes. This cautionary note should serve as a counterargument in the future, highlighting the potential pitfalls associated with presenting time-dependent XFEL structures of insufficient quality and drawing conclusive interpretations of protein structural changes that may not be distinguishable from significant experimental errors or data processing artifacts. Future high-resolution structures may provide further insights into the actual structural changes relevant to electron-transfer events. By combining both high-resolution structures and rigorous energetic evaluations, a more comprehensive understanding of the protein structure-function relationship can be achieved.

## Methods

### Coordinates and atomic partial charges

The atomic coordinates of PbRC from B. viridis were taken from the XFEL structures determined at 0 ps (dark state; PDB code 5O4C for dataset a and 5NJ4 for dataset b), 1 ps ([PLPM]* state; PDB code, 6ZHW for dataset b), 5 ps ([PLPM] •+HL•– state; PDB code, 6ZI4 for dataset a and 6ZID for dataset b), 20 ps ([PLPM] •+HL•– state; PDB code, 6ZI6 for dataset b), 300 ps ([PLPM] •+QA•– state; PDB code, 6ZI5 for dataset a and 6ZI9 for dataset b), and 8 μs ([PLPM] •+QA•– state; PDB code, 6ZIA for dataset b). Atoms with 30% occupancy for the photoactivated state (Dods et al., 2021) were used wherever present. Hydrogen atoms were generated and energetically optimized with CHARMM (Brooks et al., 1983). The atomic partial charges of the amino acids were obtained from the all-atom CHARMM22 (MacKerell et al., 1998) parameter set. For diacylglycerol, the Fe complex (Kawashima and Ishikita, 2018), and menaquinone (Kawashima and Ishikita, 2017), the atomic charges were adopted from previous studies. The atomic charges of BChlb and BPheob (BChlb, BChlb•+, BChlb•–, BPheob, and BPheob•–) were determined by fitting the electrostatic potential in the neighborhood of these molecules using the RESP procedure (Bayly et al., 1993; Supplementary file 3). The electronic densities were calculated after geometry optimization using the density functional theory (DFT) method with the B3LYP functional and 6-31G** basis sets in the JAGUAR program (Jaguar, 2012). For the atomic charges of the nonpolar CHn groups in the cofactors (e.g., the phytol chains of BChlb and BPheob and the isoprene side chains of quinone), a value of +0.09 was assigned to nonpolar H atoms.

### Calculation of Em: solving the linear Poisson-Boltzmann equation

The Em values in the protein were determined by calculating the electrostatic energy difference between the two redox states in a reference model system. This was achieved by solving the linear Poisson-Boltzmann equation with the MEAD program (Bashford and Karplus, 1990) and using Em(BChlb) = –665 mV and Em(BPheob) = –429 mV (based on Em(BChlb) = –700 mV and Em(BPheob) = –500 mV for one-electron reduction measured in dimethylformamide; Fajer et al., 1976; Watanabe and Kobayashi, 1991), considering the solvation energy difference. The Em(QA) value was calculated, using the reference Em value of –256 mV versus NHE for menaquinone-2 in water (Kishi et al., 2017). The difference in the Em value of the protein relative to the reference system was added to the known Em value. To account for the ensemble of protonation patterns, a Monte Carlo method with Karlsberg was used for sampling (Rabenstein and Knapp, 2001). The linear Poisson-Boltzmann equation was solved using a three-step grid-focusing procedure with resolutions of 2.5 Å, 1.0 Å, and 0.3 Å. Monte Carlo sampling provided the probabilities [Aox] and [Ared] of the two redox states of molecule A, and Em was evaluated using the Nernst equation. A bias potential was applied to ensure an equal amount of both redox states ([Aox] = [Ared]), thus determining the redox midpoint potential as the resulting bias potential. To ensure consistency with previous computational results, we used identical computational conditions and parameters as previous studies (e.g., Kawashima and Ishikita, 2018), performing all computations at 300 K, pH 7.0, and an ionic strength of 100 mM. The dielectric constants were set to 4 for the protein interior and 80 for water.

### QM/MM calculations

We employed the restricted DFT method for describing the closed-shell electronic structure and the unrestricted DFT method for the open-shell electronic structure with the B3LYP functional and LACVP* basis sets using the QSite (QSite, 2012) program. To neutralize the entire system, counter ions were added randomly around the protein using the Autoionize plugin in VMD (Humphrey et al., 1996). In the QM region, all atom positions were relaxed in the QM region, while the H-atom positions were relaxed in the MM region. The QM regions were defined as follows: for the BChlb pair [PLPM]: the side chains of the ligand residues (His-L173 and His-M200) and H-bond partners (His-L168, Tyr-M195, and Thr-L248); for accessory BChlb: BL/BM and the side chain of the ligand residue (His-L153 for BL/His-M180 for BM); for BPheob: HL/HM.

### NSD analysis

To analyze the out-of-plane distortions of chlorin rings, we employed an NSD procedure with the minimal basis approximation, where the deformation profile can be represented by the six lowest-frequency normal modes, that is, ruffling (B1u), saddling (B2u), doming (A2u), waving (Eg(x) and Eg(y)), and propellering (A1u) modes (Jentzen et al., 1997; Shelnutt et al., 1998). The NSD analysis was performed in the following three steps, as performed previously (Saito et al., 2012). First, the atomic coordinates of the Mg-substituted macrocycle were extracted from the crystal or QM/MM optimized structures (Table 5—source data 1, Table 6—source data 1). Second, the extracted coordinates were superimposed on the reference coordinates of the macrocycle. The superimposition is based on a least-square method, and the mathematical procedure is described in Zucchelli et al., 2007. Finally, the out-of-plane distortion in the superimposed coordinates was decomposed into the six lowest-frequency normal modes by the projection to the reference normal mode coordinates as

$$
d^{Γ}=\sumi=1NΔz_{i}(n_{z}^{Γ})_{i},
$$

where $d^{Γ}$ represents the distortion component of the mode Γ (i.e., Γ = B1u, B2u, A2u, Eg(x), Eg(y), or A1u), $Δz_{i}$ is the z-component of the superimposed coordinates in the ith heavy atom, and $(n_{z}^{Γ})_{i}$ is the z-component of the normalized eigenvector of the reference normal mode Γ in the ith heavy atom. N represents the number of heavy atoms. See Saito et al., 2012, for further details.
