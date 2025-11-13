# Selective inhibition reveals the regulatory function of DYRK2 in protein synthesis and calcium entry

## Authors

- Tiantian Wei<sup>1</sup> ([ORCID: 0000-0001-8964-8839](https://orcid.org/0000-0001-8964-8839))
- Jue Wang<sup>4</sup>
- Ruqi Liang<sup>1</sup>
- Wendong Chen<sup>5</sup>
- Yilan Chen<sup>6</sup>
- Mingzhe Ma<sup>4</sup>
- An He<sup>7</sup>
- Yifei Du<sup>4</sup>
- Wenjing Zhou<sup>8</sup>
- Zhiying Zhang<sup>1</sup>
- Xin Zeng<sup>1</sup>
- Chu Wang<sup>1</sup>
- Jin Lu<sup>9</sup>
- Xing Guo<sup>11</sup>
- Xiao-Wei Chen<sup>1</sup> ([ORCID: 0000-0003-4564-5120](https://orcid.org/0000-0003-4564-5120))
- Youjun Wang<sup>6</sup> ([ORCID: 0000-0003-0961-1716](https://orcid.org/0000-0003-0961-1716))
- Ruijun Tian<sup>5</sup> †
- Junyu Xiao<sup>1</sup> ([ORCID: 0000-0003-1822-1701](https://orcid.org/0000-0003-1822-1701)) †
- Xiaoguang Lei<sup>1</sup> ([ORCID: 0000-0002-0380-8035](https://orcid.org/0000-0002-0380-8035)) †

### Affiliations

1. The State Key Laboratory of Protein and Plant Gene Research, School of Life Sciences, Peking University Beijing China ([ROR:02v51f717](https://ror.org/02v51f717))
2. Peking-Tsinghua Center for Life Sciences, Peking University Beijing China ([ROR:02v51f717](https://ror.org/02v51f717))
3. Academy for Advanced Interdisciplinary Studies, Peking University Beijing China ([ROR:02v51f717](https://ror.org/02v51f717))
4. Beijing National Laboratory for Molecular Sciences, Key Laboratory of Bioorganic Chemistry and Molecular Engineering of Ministry of Education, College of Chemistry and Molecular Engineering, Peking University Beijing China ([ROR:02v51f717](https://ror.org/02v51f717))
5. SUSTech Academy for Advanced Interdisciplinary Studies, Southern University of Science and Technology Shenzhen China ([ROR:049tv2d57](https://ror.org/049tv2d57))
6. Beijing Key Laboratory of Gene Resource and Molecular Development, Key Laboratory of Cell Proliferation and Regulation Biology, Ministry of Education, College of Life Sciences, Beijing Normal University Beijing China ([ROR:022k4wk35](https://ror.org/022k4wk35))
7. Department of Chemistry, Southern University of Science and Technology Shenzhen China ([ROR:049tv2d57](https://ror.org/049tv2d57))
8. Institute of Molecular Medicine, Peking University Beijing China ([ROR:02v51f717](https://ror.org/02v51f717))
9. Peking University Institute of Hematology, People’s Hospital Beijing China ([ROR:02v51f717](https://ror.org/02v51f717))
10. Collaborative Innovation Center of Hematology Suzhou China
11. Life Sciences Institute, Zhejiang University Hangzhou China ([ROR:00a2xv884](https://ror.org/00a2xv884))
12. Beijing Advanced Innovation Center for Genomics (ICG), Peking University Beijing China ([ROR:02v51f717](https://ror.org/02v51f717))
13. Institute for Cancer Research, Shenzhen Bay Laboratory Shenzhen China ([ROR:00sdcjz77](https://ror.org/00sdcjz77))

† Corresponding author

## Abstract

The dual-specificity tyrosine phosphorylation-regulated kinase DYRK2 has emerged as a critical regulator of cellular processes. We took a chemical biology approach to gain further insights into its function. We developed C17, a potent small-molecule DYRK2 inhibitor, through multiple rounds of structure-based optimization guided by several co-crystallized structures. C17 displayed an effect on DYRK2 at a single-digit nanomolar IC50 and showed outstanding selectivity for the human kinome containing 467 other human kinases. Using C17 as a chemical probe, we further performed quantitative phosphoproteomic assays and identified several novel DYRK2 targets, including eukaryotic translation initiation factor 4E-binding protein 1 (4E-BP1) and stromal interaction molecule 1 (STIM1). DYRK2 phosphorylated 4E-BP1 at multiple sites, and the combined treatment of C17 with AKT and MEK inhibitors showed synergistic 4E-BP1 phosphorylation suppression. The phosphorylation of STIM1 by DYRK2 substantially increased the interaction of STIM1 with the ORAI1 channel, and C17 impeded the store-operated calcium entry process. These studies collectively further expand our understanding of DYRK2 and provide a valuable tool to pinpoint its biological function.

## Introduction

Dual-specificity tyrosine phosphorylation-regulated kinases (DYRKs) belong to the CMGC group of kinases together with other critical human kinases, such as cyclin-dependent kinases (CDKs) and mitogen-activated protein kinases (MAPKs) (Aranda et al., 2011; Becker and Joost, 1999; Manning et al., 2002). DYRKs uniquely phosphorylate tyrosine residues within their activation loops in cis during biosynthesis, although mature proteins display exclusive serine/threonine kinase activities (Lochhead et al., 2005). There are five DYRKs in humans: DYRK1A, DYRK1B, DYRK2, DYRK3, and DYRK4. DYRK1A has been extensively studied due to its potential function in the pathogenesis of Down syndrome and neurodegenerative disorders (Becker and Sippl, 2011; Wegiel et al., 2011). DYRK3 has been shown to function as a central ‘dissolvase’ to regulate the formation of membrane-less organelles (Rai et al., 2018; Wippich et al., 2013). On the other hand, DYRK2 is a crucial regulator of 26S proteasome activity (Guo et al., 2016).

The 26S proteasome degrades the majority of proteins in human cells and plays a central role in many cellular processes, including the regulation of gene expression and cell division (Collins and Goldberg, 2017; Coux et al., 1996). Recent discoveries have revealed that the 26S proteasome is subjected to intricate regulation by reversible phosphorylation (Guo et al., 2017; Guo et al., 2016; Liu et al., 2020). DYRK2 phosphorylates the Rpt3 subunit in the regulatory particle of the proteasome at Thr25, leading to the upregulation of proteasome activity (Guo et al., 2016). DYRK2 is overexpressed in several tumors, including triple-negative breast cancer and multiple myeloma, which are known to rely heavily on proteasome activity for progression, and perturbation of DYRK2 activity impedes cancer cell proliferation and inhibits tumor growth (Banerjee et al., 2018; Banerjee et al., 2019).

Our knowledge of the physiological functions of DYRK2 remains in its infancy, and DYRK2 likely has cellular targets in addition to Rpt3. Substrates of many kinases, especially Ser/Thr kinases, remain insufficiently identified. A major obstacle to discovering physiologically relevant substrates of a kinase is the lack of highly specific chemical probes that allow precise modulation of kinase function. Some DYRK2 inhibitors have been reported; however, these compounds also inhibit other kinases, mostly other DYRK family members, to various degrees (Chaikuad et al., 2016; Jouanne et al., 2017). We have recently identified LDN192960 as a selective DYRK2 inhibitor and showed that LDN192960 could alleviate multiple myeloma and triple-negative breast cancer progression by inhibiting DYRK2-mediated proteasome phosphorylation (Banerjee et al., 2019). To obtain even more potent and selective DYRK2 inhibitors, we applied a structure-guided approach to further engineer chemical compounds based on the LDN192960 scaffold. One of the best compounds we generated, compound C17 (C17), displays an effect on DYRK2 at a single-digit nanomolar IC50 with moderate to excellent selectivity against kinases closely related to DYRK2. Using this potent DYRK2 inhibitor as a tool, we treated U266 cells with C17. We performed quantitative phosphoproteomic analyses, which led to identifying several novel DYRK2 targets, including eukaryotic translation initiation factor 4E-binding protein 1 (4E-BP1) and stromal interaction molecule 1 (STIM1). These results demonstrate that DYRK2 plays critical regulatory roles in multiple cellular processes, including protein translation and store-operated calcium entry, and indicate that C17 can serve as a valuable probe for the study of DYRK2 function.

**Table 1.**
 The Inhibitory activity and selectivity of acridine analogs of DYRK2.Table 1—source data 1.Raw data of inhibitors against kinases for Table 1.


<table>
  <thead>
    <tr>
      <th rowspan="2">Cmpd.</th>
      <th colspan="4"></th>
      <th colspan="6">IC50 at molecular level (nM)</th>
      <th colspan="5">Selectivity</th>
    </tr>
    <tr>
      <th>R1</th>
      <th>R2</th>
      <th>R3</th>
      <th>R4</th>
      <th>DYRK2</th>
      <th>DYRK1A</th>
      <th>DYRK1B</th>
      <th>DYRK3</th>
      <th>Haspin</th>
      <th>MARK3</th>
      <th>DYRK2&amp;DYRK1A</th>
      <th>DYRK2&amp;DYRK1B</th>
      <th>DYRK2&amp;DYRK3</th>
      <th>DYRK2&amp;Haspin</th>
      <th>DYRK2&amp;MARK3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>LDN192960</td>
      <td></td>
      <td>-CH3</td>
      <td>-CH3</td>
      <td>-H</td>
      <td>53 ± 2</td>
      <td>1859 ± 30</td>
      <td>2900 ± 39</td>
      <td>22 ± 4</td>
      <td>18 ± 2</td>
      <td>611 ± 19</td>
      <td>35</td>
      <td>55</td>
      <td>~</td>
      <td>~</td>
      <td>12</td>
    </tr>
    <tr>
      <td>1</td>
      <td></td>
      <td>-CH3</td>
      <td>-CH3</td>
      <td>-H</td>
      <td>38 ± 2</td>
      <td>651 ± 29</td>
      <td>1401 ± 91</td>
      <td>115 ± 4</td>
      <td>34 ± 3</td>
      <td>36 ± 2</td>
      <td>17</td>
      <td>17</td>
      <td>3</td>
      <td>~</td>
      <td>~</td>
    </tr>
    <tr>
      <td>2</td>
      <td></td>
      <td>-CH3</td>
      <td>-CH3</td>
      <td>-H</td>
      <td>31 ± 1</td>
      <td>731 ± 36</td>
      <td>1477 ± 128</td>
      <td>94 ± 9</td>
      <td>27 ± 3</td>
      <td>27 ± 5</td>
      <td>24</td>
      <td>48</td>
      <td>3</td>
      <td>~</td>
      <td>~</td>
    </tr>
    <tr>
      <td>3</td>
      <td></td>
      <td>-CH3</td>
      <td>-CH3</td>
      <td>-H</td>
      <td>41 ± 2</td>
      <td>1018 ± 78</td>
      <td>2495 ± 88</td>
      <td>157 ± 18</td>
      <td>24 ± 1</td>
      <td>33 ± 7</td>
      <td>25</td>
      <td>61</td>
      <td>4</td>
      <td>~</td>
      <td>~</td>
    </tr>
    <tr>
      <td>4</td>
      <td></td>
      <td>-CH3</td>
      <td>-CH3</td>
      <td>-H</td>
      <td>53 ± 2</td>
      <td>964 ± 14</td>
      <td>1386 ± 21</td>
      <td>234 ± 10</td>
      <td>30 ± 1</td>
      <td>96 ± 3</td>
      <td>18</td>
      <td>26</td>
      <td>4</td>
      <td>~</td>
      <td>2</td>
    </tr>
    <tr>
      <td>5</td>
      <td></td>
      <td>-CH3</td>
      <td>-CH3</td>
      <td>-H</td>
      <td>89 ± 2</td>
      <td>1026 ± 96</td>
      <td>3488 ± 86</td>
      <td>311 ± 22</td>
      <td>53 ± 4</td>
      <td>91 ± 5</td>
      <td>12</td>
      <td>39</td>
      <td>3</td>
      <td>~</td>
      <td>1</td>
    </tr>
    <tr>
      <td>6</td>
      <td></td>
      <td>-CH3</td>
      <td>-CH3</td>
      <td>-H</td>
      <td>20 ± 3</td>
      <td>889 ± 131</td>
      <td>697 ± 67</td>
      <td>110 ± 11</td>
      <td>45 ± 3</td>
      <td>100 ± 4</td>
      <td>44</td>
      <td>35</td>
      <td>6</td>
      <td>2</td>
      <td>5</td>
    </tr>
    <tr>
      <td>7</td>
      <td></td>
      <td>-CH3</td>
      <td>-CH3</td>
      <td>-CH2OH</td>
      <td>13 ± 1</td>
      <td>2844 ± 49</td>
      <td>2049 ± 116</td>
      <td>26 ± 2</td>
      <td>65 ± 5</td>
      <td>107 ± 4</td>
      <td>219</td>
      <td>158</td>
      <td>2</td>
      <td>5</td>
      <td>8</td>
    </tr>
    <tr>
      <td>8</td>
      <td></td>
      <td>-CH3</td>
      <td>-CH3</td>
      <td>-COOH</td>
      <td>342 ± 77</td>
      <td>7713 ± 1,249</td>
      <td>6311 ± 1,380</td>
      <td>8009 ± 130</td>
      <td>308 ± 26</td>
      <td>1613 ± 24</td>
      <td>23</td>
      <td>18</td>
      <td>23</td>
      <td>~</td>
      <td>5</td>
    </tr>
    <tr>
      <td>9</td>
      <td></td>
      <td>-CH3</td>
      <td>-CH3</td>
      <td>-CH2NH2</td>
      <td>797 ± 26</td>
      <td>8774 ± 508</td>
      <td>7799 ± 81</td>
      <td>665 ± 28</td>
      <td>716 ± 48</td>
      <td>3390 ± 301</td>
      <td>11</td>
      <td>10</td>
      <td>~</td>
      <td>~</td>
      <td>4</td>
    </tr>
    <tr>
      <td>10</td>
      <td></td>
      <td>-CH3</td>
      <td>-CH3</td>
      <td>-CF2H</td>
      <td>522 ± 210</td>
      <td>53206 ± 16,384</td>
      <td>47964 ± 3,582</td>
      <td>402 ± 13</td>
      <td>163 ± 21</td>
      <td>460 ± 25</td>
      <td>102</td>
      <td>92</td>
      <td>~</td>
      <td>~</td>
      <td>~</td>
    </tr>
    <tr>
      <td>11</td>
      <td></td>
      <td>-Bn</td>
      <td>-CH3</td>
      <td>-H</td>
      <td>646 ± 164</td>
      <td>139908 ± 677</td>
      <td>4975 ± 328</td>
      <td>2026 ± 600</td>
      <td>1608 ± 52</td>
      <td>555 ± 36</td>
      <td>217</td>
      <td>8</td>
      <td>3</td>
      <td>3</td>
      <td>~</td>
    </tr>
    <tr>
      <td>12</td>
      <td></td>
      <td>-Bn</td>
      <td>-CH3</td>
      <td>-H</td>
      <td>427 ± 109</td>
      <td>12504 ± 3,260</td>
      <td>8203 ± 674</td>
      <td>539 ± 353</td>
      <td>1085 ± 139</td>
      <td>1062 ± 54</td>
      <td>29</td>
      <td>19</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <td>13</td>
      <td></td>
      <td>-Bn</td>
      <td>-CH3</td>
      <td>-H</td>
      <td>124 ± 27</td>
      <td>21608 ± 3,431</td>
      <td>2812 ± 543</td>
      <td>1142 ± 129</td>
      <td>1588 ± 40</td>
      <td>359 ± 17</td>
      <td>174</td>
      <td>23</td>
      <td>9</td>
      <td>13</td>
      <td>3</td>
    </tr>
    <tr>
      <td>14</td>
      <td></td>
      <td>-iPr</td>
      <td>-CH3</td>
      <td>-H</td>
      <td>85 ± 17</td>
      <td>984 ± 127</td>
      <td>3787 ± 234</td>
      <td>93 ± 28</td>
      <td>300 ± 21</td>
      <td>215 ± 12</td>
      <td>12</td>
      <td>45</td>
      <td>1</td>
      <td>4</td>
      <td>3</td>
    </tr>
    <tr>
      <td>15</td>
      <td></td>
      <td>-Bn</td>
      <td>-Bn</td>
      <td>-H</td>
      <td>623 ± 18</td>
      <td>19244 ± 1,551</td>
      <td>21110 ± 1,388</td>
      <td>496 ± 36</td>
      <td>18643 ± 1,365</td>
      <td>1183 ± 127</td>
      <td>31</td>
      <td>34</td>
      <td>~</td>
      <td>30</td>
      <td>2</td>
    </tr>
    <tr>
      <td>16</td>
      <td></td>
      <td>-CH3</td>
      <td>-CH3</td>
      <td>-CH2OH</td>
      <td>25 ± 9</td>
      <td>2243 ± 74</td>
      <td>2257 ± 279</td>
      <td>33 ± 6</td>
      <td>90 ± 9</td>
      <td>134 ± 8</td>
      <td>90</td>
      <td>90</td>
      <td>1</td>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <td>17</td>
      <td></td>
      <td>-CH3</td>
      <td>-CH3</td>
      <td>-CH2OH</td>
      <td>9 ± 2</td>
      <td>2145 + 100</td>
      <td>2272 + 134</td>
      <td>68 + 5</td>
      <td>26 + 5</td>
      <td>87 + 7</td>
      <td>240</td>
      <td>252</td>
      <td>8</td>
      <td>3</td>
      <td>10</td>
    </tr>
    <tr>
      <td>18</td>
      <td></td>
      <td>-CH3</td>
      <td>-CH3</td>
      <td>-CH2OH</td>
      <td>18 ± 2</td>
      <td>1250 ± 95</td>
      <td>1222 ± 168</td>
      <td>73 ± 13</td>
      <td>16 ± 3</td>
      <td>116 ± 13</td>
      <td>69</td>
      <td>68</td>
      <td>4</td>
      <td>~</td>
      <td>6</td>
    </tr>
    <tr>
      <td>19</td>
      <td></td>
      <td>-CH3</td>
      <td>-CH3</td>
      <td>-CH2OH</td>
      <td>23 ± 3</td>
      <td>1531 ± 52</td>
      <td>3443 ± 294</td>
      <td>108 ± 17</td>
      <td>50 ± 1</td>
      <td>210 ± 4</td>
      <td>67</td>
      <td>150</td>
      <td>5</td>
      <td>2</td>
      <td>9</td>
    </tr>
    <tr>
      <td>20</td>
      <td></td>
      <td>-CH3</td>
      <td>-CH3</td>
      <td>-CH2NC(NH2)2</td>
      <td>1498 ± 104</td>
      <td>21535 ± 1910</td>
      <td>25850 ± 1,571</td>
      <td>8477 ± 655</td>
      <td>26509 ± 733</td>
      <td>25535 ± 1,385</td>
      <td>14</td>
      <td>16</td>
      <td>6</td>
      <td>18</td>
      <td>17</td>
    </tr>
    <tr>
      <td>21</td>
      <td colspan="4"></td>
      <td>159 ± 7</td>
      <td>3014 ± 137</td>
      <td>3514 ± 511</td>
      <td>69 ± 6</td>
      <td>1564 ± 252</td>
      <td>1315 ± 87</td>
      <td>19</td>
      <td>22</td>
      <td>~</td>
      <td>10</td>
      <td>8</td>
    </tr>
    <tr>
      <td>22</td>
      <td colspan="4"></td>
      <td>3761 ± 202</td>
      <td>24733 ± 1,669</td>
      <td>25948 ± 540</td>
      <td>2426 ± 257</td>
      <td>9750 ± 127</td>
      <td>16770 ± 1,788</td>
      <td>7</td>
      <td>7</td>
      <td>～</td>
      <td>3</td>
      <td>4</td>
    </tr>
  </tbody>
</table>

## Results

### Structure-based optimization of DYRK2 inhibitors

LDN192960 was identified as a DYRK2 inhibitor (Banerjee et al., 2019; Cuny et al., 2010; Cuny et al., 2012). It occupies the ATP-binding pocket of DYRK2 and mediates extensive hydrophobic and hydrogen bond interactions (Banerjee et al., 2019). Nevertheless, LDN192960 also inhibits other DYRK2-related kinases, especially Haspin and DYRK3 (Banerjee et al., 2019). To generate DYRK2 inhibitors with better selectivity, we synthesized a series of new compounds based on the same acridine core structure (Table 1). The amine side chain was first changed to a protected amine (compounds 1–3), a cyano group (compound 4), or a cyclic amine (compounds 5–6) (Figure 1—figure supplement 1A, Table 1). Among these candidates, compound 6 exhibited the most potent inhibitory effect towards DYRK2, with an in vitro IC50 of 17 nM. In comparison, LDN192960 showed an IC50 of 53 nM when the same protocol was used (Table 1)—treating HEK293T cells transiently expressing DYRK2 with increasing concentrations of compound 6 efficiently inhibited Rpt3-Thr25 phosphorylation, with the maximal effect observed at an inhibitor concentration of less than 3 μM (Figure 1—figure supplement 1B). Notably, compound 6 also displays good selectivity towards DYRK2 than other kinases, including DRYK1A, DRYK1B, DYRK3, Haspin, and MARK3 (IC50 values of 889, 697, 121305, 45, and 100 nM, respectively; Table 1). Therefore, compound 6 was chosen as the lead compound for further chemical modification.

We subsequently crystallized DYRK2 in complex with compound 6 and determined the structure at a resolution of 2.2 Å (Figure 1A, Figure 1—figure supplement 1C). Not surprisingly, compound 6 binds the ATP-binding site of DYRK2 like LDN192960. A water molecule is located deep inside the binding pocket acting as a bridge in the interactions between LDN192960 and the protein. The newly added amino side chain displays apparent densities and adopts an extended conformation. An in-depth analysis of the crystal structure revealed several additional sites for chemical expansion that may further strengthen its interaction with DYRK2 (Figure 1—figure supplement 2A-B). First, a hydrophilic group can be introduced into the acridine core to functionally replace the aforementioned water molecule and maintain constant contact with DYRK2. Second, a bulky functional group can replace the methoxy groups to mediate other interactions with DYRK2. Finally, the amine side chain can be altered to stabilize its conformation (Figure 1—figure supplement 2A-B). To this end, we synthesized 9 new compounds (compounds 7–15) and evaluated their inhibitory effects on DYRK2 and related kinases (Figure 1—figure supplement 2C-D). We also determined the co-crystallized structures of several of these compounds with DYRK2 to visualize their detailed interactions (Figure 1, Figure 1—figure supplement 3). Compound 7, introducing a hydroxymethyl group to the acridine core, inhibits DRYK2 efficiently as compound 6 while displaying better selectivity against other DRYK family members (Table 1). The co-crystallized structure shows that the hydroxymethyl group directly contacts the main chain amide group of Ile367 and indirectly coordinates Glu266 and Phe369 via a water molecule (Figure 1D). Compared to compound 7, compounds 8–10, which contain a carboxyl, aminomethyl, and fluoromethyl group, respectively, instead of a hydroxymethyl group, display reduced inhibition towards DYRK2. Compounds 11–15, designed to replace the methoxy group with a bulkier side chain, showed significantly decreased activity and selectivity and were not further pursued (Table 1).

![Figure 1.](https://cdn.elifesciences.org/articles/77696/elife-77696-fig1-v3.jpg)

**Figure 1.:** (A) Overall structure of DYRK2 (grey) bound to 6 (green), 7 (pink), C17 (orange), and 18 (blue). (B) Composite omit maps are contoured at 1.5σand shown as gray meshes to reveal the presence of compounds 6, 7, 17, and 18 in the respective crystal structures. (C–F) Close-up view of the DYRK2 binding pocket with compounds 6, 7, 17, and 18. Hydrogen bonds are shown as dashed lines. Water molecules are indicated with red spheres.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/77696/elife-77696-fig1-figsupp1-v3.jpg)

**Figure 1—figure supplement 1.:** (A) Structure of amino side chain change analogues 1–6 based on LDN192960. (B) HEK293T cells stably expressing FLAG-DYRK2 were treated with the indicated concentrations of compound 6 in 1 hr. Cells were lysed and immunoblotting was carried out with the indicated antibodies. (C) Structure of DYRK2 in complex with compound 6. DYRK2 is shown as ribbons and colored in blue white. The 2Fo-Fc difference electron density map (1.5 σwhich reveals the presence of 6 and water is shown as a gray mesh. The 6 and water are omitted to calculate the map).

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/77696/elife-77696-fig1-figsupp2-v3.jpg)

**Figure 1—figure supplement 2.:** (A) The possible sites for further expansion based on the co-crystal structure of 6 and DYRK2. (B) Overview of modification of compound 6. (C) Modifications for inner space 1. (D) Modifications for cavity around ATP-binding pocket. (E) Modifications of amine side chain based on compound 7. (F) Modifications based on compound 17.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/77696/elife-77696-fig1-figsupp3-v3.jpg)

Further chemical modification was carried out based on compound 7. By changing the 6-membered ring to a straight-chain or smaller ring, we synthesized compounds 16–19 (Table 1, Figure 1—figure supplement 2E). Among these compounds, C17 with an (S)–3-methylpyrrolidine side-chain exhibited the best potency and selectivity among all the analogs (Table 1). Interestingly, we noticed that compound 18 containing an (R)–3-methylpyrrolidine side chain was not as good as C17, indicating that the chirality of the 3-methylpyrrolidine motif plays an essential role in both potency and selectivity. Further modification of compound 17 (leading to compound 20) to promote further hydrogen bond interactions with DYRK2 failed to improve the inhibitory effect. We also wondered whether acridine was the best aromatic core structure and synthesized two new compounds (compounds 21 and 22) by changing one side of the benzene group to a sulfur-containing thiazole structure (Figure 1—figure supplement 2F), which we thought might facilitate hydrophobic interactions with DYRK2 within the ATP-binding pocket; however, they did not have as effective an inhibitory effect as compound 17 (Table 1).

### C17 is a potent and selective DYRK2 inhibitor

We set to comprehensively characterize the inhibitory function of compound 17 (Figure 2A), referred to as C17 hereafter. In vitro, C17 displays an effect on DYRK2 at a single-digit nanomolar IC50 value (9 nM) (Figure 2B, Figure 2—figure supplement 1A). To further evaluate the selectivity of C17, we performed kinome profiling analyses. Among the 468 human kinases tested, C17 targeted only DYRK2, Haspin, and MARK3 at a concentration of 500 nM (Figure 2C). Nonetheless, the in vitro IC50 values of C17 for Haspin and MARK3 (26 nM and 87 nM, respectively) were 3–10-fold higher than that for DYRK2 (Figure 2B, Figure 2—figure supplement 1B-F). Similarly, C17 also inhibited DYRK3 to a lesser extent (IC50 of 68 nM). In contrast, LDN192960 inhibited DYRK3 and Haspin more than it inhibited DYRK2 (Banerjee et al., 2019; Cuny et al., 2010). Significantly, C17 also efficiently suppressed DYRK2 activity in the cell and abolished Rpt3-Thr25 phosphorylation at an inhibitor concentration of less than 1 μM (Figure 2D). Taken together, these data demonstrate that C17 is a highly potent and selective DYRK2 inhibitor both in vitro and in vivo.

![Figure 2.](https://cdn.elifesciences.org/articles/77696/elife-77696-fig2-v3.jpg)

**Figure 2.:** (A) Chemical structure of C17. (B) IC50 values of C17 against DYRK1A, DYRKIB, DYRK3, Haspin and MARK3. (C) Kinome profiling of C17 at 500 nM was carried out using 468 human kinases (https://www.discoverx.com/). (D) C17 inhibits Rpt3-Thr25 phosphorylation. HEK293T cells stably expressing FLAG-DYRK2 were treated with the indicated concentrations of C17 for 1 hr. The cells were lysed, and immunoblotting was carried out with the indicated antibodies.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/77696/elife-77696-fig2-figsupp1-v3.jpg)

**Figure 2—figure supplement 1.:** (A–E) IC50 of C17 on DYRK2, DYRK1A, DYRK1B, DYRK3, Haspin and MARK3. The IC50 graph was plotted using GraphPad Prism 8.4.0 software. The results are presented as the percentage of kinase activity relative to the DMSO-treated control. Results are means ± SD for triplicate reactions with similar results obtained in at least one other experiment.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/77696/elife-77696-fig2-figsupp2-v3.jpg)

**Figure 2—figure supplement 2.:** (A) Binding strength of LDN192960 with calf thymus DNA tested by Isothermal titration calorimetry. (B) Binding strength of C17 with calf thymus DNA tested by Isothermal titration calorimetry.

Acridine derivatives have traditionally been used as antibacterial, antiparasitic, and anticancer agents since these compounds usually show strong DNA intercalating effects (Chaikuad et al., 2016; Jouanne et al., 2017). Considering the potential toxicity of C17 due to its possible DNA-binding capacity, we also assessed the DNA-binding effect of C17 (Figure 2—figure supplement 2). Isothermal titration calorimetry revealed that C17 (Kd = 22.9 µM) binds to DNA with significantly lower affinity than LDN192960 binds to DNA (Kd = 198 nM), possibly because of the introduction of hydroxymethyl group on the acridine core, which is not present in LDN192960.

### DYRK2 substrate profiling by quantitative phosphoproteomic analyses

Quantitative phosphoproteomic approaches have significantly expanded the scope of phosphorylation analysis, enabling the quantification of changes in thousands of phosphorylation sites simultaneously (Álvarez-Salamero et al., 2017). To obtain a comprehensive list of potential DYRK2 targets, we treated the myeloma U266 cells with C17 and carried out quantitative phosphoproteomic analyses (Chen et al., 2018; Hogrebe et al., 2018). We prepared lysates of U266 cells treated with C17 or the DMSO control and trypsinized them. Phosphorylated peptides were then enriched using Ti4+-immobilized metal ion affinity chromatography (IMAC) tips and analyzed by LC-MS/MS (Figure 3A). A total of 15,755 phosphosites were identified, among which 12,818 (81%) were serine, and 2,798 (18%) were threonine. A total of 10,647 (68%) phosphosites were Class I (localization probability >0.75), 2557 (16%) were Class II (0.5 < localization probability ≤0.75), and 2401 (16%) were Class III (0.25 < localization probability ≤0.5) (Figure 3B). This is a very comprehensive phosphoproteomic dataset prepared for DYRK2 substrate profiling by treating the U266 cells with 10 μM of C17. A good Pearson correlation coefficient of 0.9 was obtained for the phosphosite intensities among the treatment and control samples (Figure 3—figure supplement 1), and the coefficient of variance of the intensities of the majority of the phosphosites was lower than 20% (Figure 3—figure supplement 2), demonstrating the high quantification precision of our label-free phosphoproteomic analysis. Remarkably, C17 treatment led to significant downregulation of 373 phosphosites (Figure 3C), including pThr37 of the eukaryotic translation initiation factor 4E-binding protein 1 (4E-BP1), as well as pSer519 and pSer521 in the stromal interaction molecule 1 (STIM1) (Figure 3D, Figure 3—figure supplement 3). Interestingly, another 445 phosphosites were upregulated (Figure 3C), suggesting that DYRK2 likely inhibited some downstream kinases or activated phosphatases, and suppressing its activity reversed these effects. Together, these data demonstrate that DYRK2 is involved in a network of phosphorylation events and can directly or indirectly regulate the phosphorylation status of many proteins. The top pathways with which DYRK2 may participate were revealed by a global analysis of the significantly up-and down-regulated phosphoproteins (Figure 3E).

![Figure 3.](https://cdn.elifesciences.org/articles/77696/elife-77696-fig3-v3.jpg)

**Figure 3.:** (A) Workflow of the phosphoproteomic approach. Triplicate samples treated with/without 10 μM C17 for 1 hr were separately lysed and digested, and the phosphorylated peptides were enriched by the Ti4+-IMAC tip and analyzed by LC-MS/MS. (B) Distribution of the assigned amino acid residues and their localization probabilities (Class I > 0.75, Class II > 0.5 and ≤ 0.75, Class III > 0.25 and ≤ 0.5) for all identified phosphorylation sites. (C) Volcano plot (FDR < 0.05 and S0 = 2) shows the significantly up-and downregulated phosphosites after C17 treatment. (D) MS/MS spectra of the phosphosites of two potential DYRK2 substrates, pT37 of 4E-BP1 and pS519 and pS521 of STIM1. (E) Global canonical pathway analysis of the significantly up-and downregulated phosphoproteins. –Log10 adjusted p-values associated with a pathway are presented.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/77696/elife-77696-fig3-figsupp1-v3.jpg)

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/77696/elife-77696-fig3-figsupp2-v3.jpg)

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/77696/elife-77696-fig3-figsupp3-v3.jpg)

**Figure 3—figure supplement 3.:** Data was presented as mean values ± SD (error bars).

### 4E-BP1 is a direct cellular target of DYRK2

We set out to determine whether some of the 373 downregulated phosphosites are genuine DYRK2 targets. We first examined 4E-BP1 for several reasons. First, C17 treatment decreased the pThr37 level in U266 cells (Figure 3C). Second, a previous study showed that Ser65 and Ser101 in 4E-BP1 can be phosphorylated by DYRK2 in vitro, indicating that 4E-BP1 is a potential DYRK2 substrate (Wang et al., 2003). And lastly, several phosphosite-specific antibodies for 4E-BP1 are commercially available. 4E-BP1 is a master regulator of protein synthesis. It has been well established that its phosphorylation by other kinases such as mTORC1 leads to its dissociation from eukaryotic initiation factor 4E (eIF4E), allowing mRNA translation (Laplante and Sabatini, 2012; Ma et al., 2009).

Using an antibody that detects 4E-BP1 only when it is phosphorylated at Thr37 and Thr46, we found that C17 treatment significantly reduced the level of pThr37/pThr46 of endogenous 4E-BP1 in HEK293T cells (Figure 4A), consistent with our mass spec analyses in U266 cells. Further investigations using two other 4E-BP1 phosphosite-specific antibodies showed that C17 also decreased the phosphorylation of Ser65 in endogenous 4E-BP1 (Figure 4A) by a previous study Wang et al., 2003; as well as Thr70. Knockdown of endogenous DYRK2 using a short hairpin RNA (shRNA) also significantly reduced the phosphorylation of these sites (Figure 4B). Successful knockdown is demonstrated by quantitative RT-PCR analysis (Figure 4—figure supplement 1). Similarly, C17 suppressed DYRK2-mediated phosphorylation of 4E-BP1 when overexpressed in the HEK293 cells (Figure 4C). To ascertain whether DYRK2 can directly phosphate 4E-BP1, we performed an in vitro kinase assay using purified DYRK2 and 4E-BP1 proteins. DYRK2 efficiently phosphorylated 4E-BP1 at multiple sites, including Thr37/Thr46, Ser65, and Thr70, whereas the kinase-deficient DYRK2 mutant (D275N) displayed no activity (Figure 4D). C17 suppressed the phosphorylation of these sites in a dose-dependent manner (Figure 4E). These results demonstrate that DYRK2 effectively phosphorylated 4E-BP1 on multiple sites in vivo and in vitro.

![Figure 4.](https://cdn.elifesciences.org/articles/77696/elife-77696-fig4-v3.jpg)

**Figure 4.:** (A) C17 treatment for 1 hr reduced the phosphorylation of endogenous 4E-BP1 in HEK293T cells. The phosphorylation status of 4E-BP1 was analyzed by immunoblotting cell lysates using indicated antibodies. (B) DYRK2 knockdown decreases the phosphorylation of endogenous 4E-BP1 in HEK293T cells. (C) HEK293A cells stably expressing HA-DYRK2 and FLAG-4E-BP1 were treated with indicated concentrations of C17 for 1 hr. The cells were lysed, and immunoblotting was carried out with indicated antibodies. (D) DYRK2 directly phosphorylated 4E-BP1 at multiple sites. (E) C17 inhibited DYRK2-mediated 4E-BP1 phosphorylation in a concentration-dependent manner. (F–H) C17 displayed a synergistic effect with AKT and MEK inhibitors to suppress 4E-BP1 phosphorylation in HEK293A (F), HCT116 (G), and U266 cells. (H) The cells were treated with indicated concentrations of PD032590, AKTi-1/2, and C17 alone or in combination for 1 hr. Cell lysates were immunoblotted with indicated antibodies.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/77696/elife-77696-fig4-figsupp1-v3.jpg)

**Figure 4—figure supplement 1.:** GAPDH was used as an internal standard, and fold change was calculated by comparing expression levels relative to those of pLL3.7-shRNA-scramble (negative control). Data are presented as the means ± SD (n = 3 biological replicates per condition, ***, p = 0.0001, unpaired Student’s t-test).

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/77696/elife-77696-fig4-figsupp2-v3.jpg)

4E-BP1 is targeted by multiple kinases (Qin et al., 2016). Indeed, C17 or DYRK2 shRNA decreased but did not abolish the phosphorylation of 4E-BP1 (Figure 4A and B). A previous study showed that combined inhibition of AKT and MEK kinases suppressed 4E-BP1 phosphorylation and tumor growth (She et al., 2010). We observed similar results when we treated the HEK293A cells with AKTi (an AKT1/AKT2 inhibitor) and PD0325901 (a MEK inhibitor). Significantly, knockdown of DYRK2 in the presence of these compounds further markedly diminished 4E-BP1 phosphorylation (Figure 4B). To assess whether C17 can also elicit a synergistic effect with these kinase inhibitors, we treated HEK293A, HCT116, and U266 cells with these molecules, either alone or in combination, and examined the phosphorylation status of endogenous 4E-BP1 (Figure 4F–H). The presence of C17 potentiated the inhibitory effect of AKTi and PD0325901 in all these cells. Together, these results confirm that 4E-BP1 is a direct cellular target of DYRK2 and suggest the potential use of DYRK2 inhibitors in combination with other kinase inhibitors for cancer therapy.

### DYRK2 promotes STIM1-ORAI1 interaction to modulate SOCE

In addition to 4E-BP1, another potential target of DYRK2 is STIM1, as the phosphorylation levels of both Ser519 and Ser521 in endogenous STIM1 were significantly reduced upon DYRK2 inhibition in our mass spectrometry analyses (Figure 3C). STIM1 is a single-pass transmembrane protein residing in the endoplasmic reticulum (ER) and plays a vital role in the store-operated calcium entry (SOCE) process (Collins et al., 2013). The luminal domain of STIM1 senses calcium depletion in the ER and induces protein oligomerization and puncta formation (Liou et al., 2005; Prakriya and Lewis, 2015; Zheng et al., 2018). Oligomerized STIM1 then travels to the ER-plasma membrane contact site and activates the ORAI1 calcium channel. The cytosolic region of STIM1 contains multiple phosphorylation sites, and it has been shown that the function of STIM1 is regulated by several kinases, including ERK1/2 (Pozo-Guisado et al., 2013; Pozo-Guisado and Martin-Romero, 2013).

Purified wild-type DYRK2, but not the kinase-dead mutant D275N, induced mobility changes of the cytosolic region of STIM1 (STIM1235-END) in SDS-PAGE gel (Figure 5A). As increasing amounts of DYRK2 lead to greater shifts of STIM1235-END, there are likely multiple DYRK2 phosphorylation sites in STIM1. Consistently, DYRK2 induced a mobility shift of STIM1 when they were co-expressed in the HEK293A cells (Figure 5B). To further pinpoint DYRK2-specific phosphorylation sites, we co-expressed DYRK2, Orai1, and STIM1 in HEK293A cells, treated the cells with C17, isolated STIM1 using Anti-FLAG agarose, and then subjected it to label-free quantitative mass spectrometry analyses. The phosphorylation levels of at least eight phosphosites on four peptides of STIM1 were significantly reduced upon treatment with C17 compared with the untreated sample (Figure 5—figure supplement 1A-B), including Ser519 and Ser521 that were identified in the U266 phosphoproteome analysis (Figure 3C). In a separate mass spec experiment, phosphorylation of Ser608 and Ser616 were also reduced by C17. Together, these results demonstrate that DYRK2 can phosphorylate multiple sites in the cytosolic region of STIM1.

![Figure 5.](https://cdn.elifesciences.org/articles/77696/elife-77696-fig5-v3.jpg)

**Figure 5.:** (A) DYRK2 directly phosphorylated STIM1. GST-STIM1235-END was incubated with wild-type or kinase-deficient DYRK2 in the presence of Mn-ATP for 30 min. Phosphorylation of GST-STIM1235-END was indicated by the mobility change of STIM1 in SDS-PAGE gel. (B) DYRK2 phosphorylated STIM1 in vivo. HEK293A cells were co-transfected with FLAG-STIM1 and DYRK2 for 36 h, then states immunoblotted with the indicated antibodies. (C) Typical confocal microscopy images showing the effects of mCherry-DYRK2 and/or C17 (1 μM) on the puncta formation of STIM1 in the HEK293 Orai1/Orai2/Orai3-TKO cells. The scale bar is 10 μm. The experiments were repeated, six cells were examined each time. (D) DYRK2 promoted the interaction between STIM1 and OraiI1. HEK293A cells were co-transfected with FLAG-STIM1, GFP-Orai1, and DYRK2 for 36 hr. STIM1 was immunoprecipitated with FLAG agarose, and the associated proteins were analysed using the indicated antibodies. (E) Phosphosites mutations in STIM1 disrupt the interaction with Orai1. (F) C17 inhibits the interaction between FLAG-STIM1 and GFP-Orai1 without exogenously expressing DYRK2. (G–I) Effects of DYRK2 on the FRET signals between STIM1-YFP and CFP-Orai1. Upper panel, typical traces; lower panel, statistics. (G) HEK293 cells stably expressing STIM1-YFP and CFP-Orai1. (n = 3, ****, p < 0.0001. unpaired Student’s t-test). (H) HEK293 STIM1-STIM2 DKO cells stably expressing Orai1-CFP cells transiently expressing STIM1-1-491-YFP (n = 3, unpaired Student’s t-test). (I) HEK STIM1-STIM2 DKO cells transiently expressing STIM1-YFP (red) or STIM1-10M (blue). (n = 3, ****, p < 0.0001, unpaired Student’s t-test). (J) C17 inhibited SOCE in HEK293A cells. HEK293A cells were transfected with GCAMP6f or GCAMP6f plus STIM1 for 24 hr and then treated with 1 μM C17 for 1 hr. Before thapsigargin treatment, the cell culture medium was switched to a Ca2+-free medium containing thapsigargin (1 μM, solid lines) or DMSO (dashed lines) was added to the cells, and 2 mM Ca2+ was added 12 min later. The red and green lines correspond to C17-treated cells. Blue and black lines represent untreated cells. GCAMP6f fluorescence was monitored by a Zeiss LSM 700 laser scanning confocal microscope. (K) Quantification of (J). The following number of cells were monitored: STIM1, 45 cells on 3 coverslips (blue solid line); STIM1 +C17 (1 μM), 48 cells on 3 coverslips (red solid line); endogenous, 47 cells on 3 coverslips (black solid line); endogenous +C17 (1 μM), 42 cells on 3 coverslips (green solid line). STIM1(-Tg), 43 cells on 3 coverslips (blue dashed line). STIM1 +C17 (1 μM) (-Tg), 43 cells on 3 coverslips (red dashed line); endogenous (-Tg), 43 cells on 3 coverslips (black dashed line); and endogenous +C17 (1 μM) (-Tg), 43 cells on 3 coverslips (green dashed line). Error bars represent the means ± SEM. (L) A hypothetic model depicts DYRK2-mediated STIM1 activation.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/77696/elife-77696-fig5-figsupp1-v3.jpg)

**Figure 5—figure supplement 1.:** （A）Workflow for the identification of phosphosites influenced by C17 on STIM1. Triplicate HEK293A cells co-transfected with FLAG-STIM1 were treated with 10 μM C17 for 1 hr, enriched by FLAG-beads, digested by FASP (Filter-Aided Sample Preparation) and quantified by label-free proteomics. (B) The changed phosphorylation levels on peptides of STIM1. The phosphorylation of eight phosphosites (shown in red) on four peptides of STIM1 was significantly reduced upon treatment with C17 compared with the control group. (C) STIM1 constructs used.

STIM1 puncta formation indicates its oligomerization and activation (Liou et al., 2005; Prakriya and Lewis, 2015; Zheng et al., 2018). To assess the functional outcome of STIM1 phosphorylation by DYRK2, we co-expressed STIM1 and DYRK2 in an Orai-deficient (Orai-KO) cell line, which has all three Orai genes genetically ablated (Zheng et al., 2018). DYRK2 induced the appearance of STIM1 puncta under resting conditions, indicating that DYRK2 promotes STIM1 oligomerization (Figure 5C). In contrast, the STIM1 puncta were not observed in the presence of C17. DYRK2 also failed to promote the punctate formation of STIM1-10M, a STIM1 variant with all ten potential DYRK2 phosphorylation sites mutated to Ala (Figure 5C, Figure 5—figure supplement 1C).

To further understand the importance of STIM1 phosphorylation, we examined the interaction between STIM1 and Orai1 using co-immunoprecipitation. Expression of WT DYRK2 significantly increased the interaction between STIM1 and Orai1, whereas expression of DYRK2-KD exerted no such effect (Figure 5D). Treating cells with C17 effectively abolished the DYRK2-dependent STIM1-Orai1 interaction. Notably, both STIM1-1-491, a C-terminal truncated STIM1 (Figure 5C, Figure 5—figure supplement 1C), and STIM1-10M displayed significantly reduced interaction with Orai1 even in the presence of WT DYRK2 (Figure 5E), suggesting that DYRK2-mediated phosphorylation is essential to promote the binding between STIM1 and Orai1. C17 also decreased the interaction between STIM1 and Orai1 without exogenously expressing DYRK2 (Figure 5F).

We examined fluorescence resonance energy transfer (FRET) between STIM1-YFP and CFP-Orai1 to validate the regulatory function of DYRK2 on STIM1-Orai1 interaction. The FRET signals between STIM1-YFP and CFP-Orai1 were significantly increased in HEK293 cells in the presence of WT DYRK2 (Figure 5G). To exclude the influence of endogenous STIM1, we performed further analyses in a STIM1-STIM2 DKO cell line (Zheng et al., 2018). The FRET signals between STIM1-1-491 and Orai1 were unaltered by DYRK2 (Figure 5H), indicating that the effect of DYRK2 is dependent on the C-terminal region of STIM1. Furthermore, the FRET signals between STIM1-10M and Orai1 were unaffected by DYRK2 (Figure 5I). These results are consistent with the co-immunoprecipitation results and demonstrate that DYRK2 can promote the STIM1-Orai1 interaction via STIM1 phosphorylation.

Lastly, to examine the physiological relevance of the STIM1-Orai1 interaction regulated by DYRK2, we performed SOCE analyses in HEK293A cells expressing GCaMP6f, a genetically encoded calcium sensor (Nakai et al., 2001). Treating cells grown in a calcium-free medium containing thapsigargin resulted in a transient increase in GCaMP6f fluorescence due to calcium release from the ER to the cytosol (Figure 5J, black line). Subsequent addition of calcium to the cell culture medium resulted in a marked increase in GCaMP6f signaling, indicating calcium entry into the cells, further augmented by STIM1 overexpression (Figure 5J, blue line). Pre-treating cells with C17 for 1 hr substantially reduced SOCE in cells with either endogenous (Figure 5J, green line) or overexpressed STIM1 (Figure 5J, red line). Quantifications of these results are present in Figure 5K. Taken together, our results strongly suggest that DRYK2 can directly enhance SOCE by phosphorylating STIM1 and promoting its interaction with ORAI1, which can all be effectively inhibited by C17.

## Discussion

We used a structure-based approach to design, synthesize and evaluate a series of new analogs based on the acridine core structure and eventually identified C17 as a potent and selective DYRK2 inhibitor. We showed that C17 affects DYRK2 at a single-digit nanomolar IC50 and inhibits DYRK2 more potently than closely related kinases such as DYRK3, Haspin, and MARK3. The crystal structure of DYRK2 bound to C17 revealed critical interactions that explain its high selectivity, including a hydrogen bond between the (S)–3-methylpyrrolidine ring and Glu352 in DYRK2.

C17 provided us with a unique tool to interrogate the physiological functions of DYRK2. We treated U266 cells with C17 and performed quantitative phosphoproteomic analyses. We found that the cellular phosphorylation pattern is significantly altered by C17, suggesting that DYRK2 likely has multiple cellular targets and is involved in a network of biological processes. We then identified several leading phosphosites that are downregulated and demonstrated that 4E-BP1 and STIM1 are bona fide substrates of DYRK2. We showed that DYRK2 efficiently phosphorylated 4E-BP1 at multiple sites, including Thr37, and combined treatment of C17 with AKT and MEK inhibitors resulted in marked suppression of 4E-BP1 phosphorylation. Therefore, DYRK2 likely functions synergistically with other kinases to regulate protein synthesis.

For the first time, we also discovered that DYRK2 could efficiently phosphorylate STIM1, and phosphorylation of STIM1 by DYRK2 substantially increased the interaction between STIM1 and ORAI1. Treating cells with C17 suppressed SOCE, validating the critical role of DYRK2 in regulating calcium entry into cells. These data allow us to present a hypothetical model showing how DYRK2 triggers the activation of STIM1 (Figure 5L). Under resting conditions, the cytosolic portion of STIM1 likely adopts an inactive conformation. DYRK2 can phosphorylate STIM1 and induce its oligomerization, which then interacts with the Orai1 channel and leads to its opening. One inadequacy of our study is the lack of further insight into the regulation mechanism of this process. In particular, what is the upstream signal that triggers DYRK2 activation? Nevertheless, our data offer a valuable model that allows further investigation of the relationship between DYRK2 and SOCE.

Recently, Mehnert et al. developed a multilayered proteomic workflow and determined how different pathological-related DYRK2 mutations altered protein conformation, substrates modification, and biological function (Qin et al., 2016). DYRK2 is implicated in regulating multiple cellular processes, and the selective DYRK2 inhibitor we developed here will serve as a valuable tool in dissecting its complex downstream pathways.

## Materials and methods

### Antibodies and reagents

Antibodies used in this study were: anti-4E-PB1 (Cell Signaling Technology, RRID: AB_2097841), anti-phosphorylated 4E-BP1 (Thr37/46) (Cell Signaling Technology, RRID: AB_560835), anti-phosphorylated 4E-BP1 (Ser65) (Cell Signaling Technology, RRID: AB_330947), anti-phosphorylated 4E-BP1 (Thr70) (Cell Signaling Technology, RRID: AB_2798206), anti-HA (Cell Signaling Technology, RRID: AB_1549585), anti-Flag (Sigma, RRID: AB_259529), anti-Flag (Abcam, #ab205606), anti-GFP (Proteintech, RRID: AB_11182611), Anti-GFP (Abcam, #ab183734), anti-RPT3 (Thermo Fisher Scientific, RRID: AB_2781512), anti-GAPDH (TransGen Biotech, #HC301-01). Secondary antibodies were horseradish peroxidase (HRP)-conjugated anti-rabbit IgG (H + L) or HRP-conjugated anti-mouse IgG (H + L) purchased from Transgene Biotechnology (#HC101-01, #HC201-01). Rabbit anti-pThr25 polyclonal antibody was generated using the following phospho-peptide as immunogen: LSVSRPQ(pT)GLSFLGP as reported previously (Guo et al., 2016). Reagents used in this study were: AKTi-1/2 (Selleck, #S80837), PD0325901 (Aladdin, #P125494), Thapsigargin (Aladdin, #T135258). Inhibitors were dissolved in dimethyl sulfoxide. All chemical reagents were used as supplied by Sigma-Aldrich, J&K Scientific, Alfa Aesar Chemicals, Energy Chemicals and Bide Pharmatech. DCM, DMF, DMSO were distilled from calcium hydride; tetrahydrofuran was distilled from sodium/benzophenone ketyl prior to use.

### Cloning

The GCaMP6f, pEGFP-Orai1, and mCherry-STIM1 plasmids were kindly gifted from the Xiaowei Chen Lab (Peking University, China). The GFP-tagged human DYRK1A, 1B, 2, 3, 4, pLL3.7-DYRK2-shRNA, psPAX2, and pMD2.G plasmids were kindly gifted from the Xing Guo Lab (Zhejiang University, China). DYRK2208-552 was subcloned into the pQlinkHx vector (Clontech) with an engineered N-terminal His tag. STIM1235-END and full-length 4EBP1 were subcloned into the pQlinkGx vector (Clontech) with an engineered N-terminal GST tag. Full-length STIM1 was subcloned into a pCCF vector (Clontech) with an engineered N-terminal FLAG tag. The HA-mcherry-DYRK2 and HA-mcherry-DYRK2-D275N plasmids were generated by modification of pEGFP-DYRK2 and pEGFP-DYRK2-D275N plasmids. HA-mcherry was PCR amplified from pmCherry-N1 plasmid and replaced EGFP by homologous recombination. All plasmids were verified by DNA sequencing.

### Cell culture, transfection, and infection

Mammalian cells were all grown in a humidified incubator with 5% CO2 at 37 °C. HEK293T (RRID:CVCL_0063), HEK293A (Thermo Fisher, R70507), and HEK293 (RRID:CVCL_0045) cells were grown in Dulbecco’s Modified Eagle Media (DMEM, Gibco) supplemented with 10% FBS, 4 mM L-glutamine, 100 U/mL penicillin, and 100 mg/mL streptomycin (Gibco). U266 (RRID:CVCL_0566) cells were grown in RPMI 1640 (Gibco) supplemented with 10% FBS, 4 mM L-glutamine, 100 U/mL penicillin, and 100 mg/mL streptomycin (Gibco). HCT116 cells (China Infrastructure of Cell Line Resources, 1101HUM-PUMC000158) were grown in Iscove’s Modified Dulbecco’s Medium (IMDM, Gibco) supplemented with 10% FBS, 4 mM L-glutamine, 100 U/mL penicillin, and 100 mg/mL streptomycin (Gibco). All cell lines were confirmed by STR (short tandem repeat) profiling and tested negative for mycoplasma contamination. All cell lines are not in the list of commonly misidentified cell lines maintained by the International Cell Line Authentication Committee (version 11). Transient transfection of HEK293T, HEK293A cells were carried out using Lipofectamine 2000 (Thermo Fisher Scientific) or X-tremeGENE 9 DNA Transfection reagent (Roche) as recommended by the manufacturer, and transfected cells were used in experiments 24–48 hr later. In Lipofectamine transfection, the cells were cultured to ~70–80% confluency in 10 cm dishes, followed by transfection with 10–12 μg plasmid. The cells were changed with fresh DMEM after 12 hr and incubated for 36 hr before further experiments. In X-tremeGENE 9 DNA transfection, the cells were cultured to ~50 confluency in 35 mm glass bottom dishes coated with poly-D-lysine, followed by transfection with 1–3 μg plasmid. The cells were changed with fresh DMEM after 6 hr and incubated for 24–36 hr before further experiments. Lentiviruses were produced using the psPAX2 and pMD2.G packaging vectors. Viral media were passed through a pre-wetted 0.45 μm filter and mixed with 10 μg mL–1 Polybrene (Sigma) before being added to recipient cells. Infected cells were selected with puromycin (1–2 μg mL–1, Life Technologies) to generate stable populations.

### DYRK2 protein purification and co-crystallization

DYRK2208-552 with an N-terminal 6 × His affinity tag and TEV protease cleavage site which expressed in E. coli BL21 (DE3). Bacterial cultures were grown at 37 °C in LB medium to an OD600 of 0.6–0.8 before induced with 0.5 mM IPTG overnight at 18 °C. Cells were collected by centrifugation and frozen at –80 °C. For protein purification, the cells were suspended in the lysis buffer (50 mM HEPES, pH 7.5, 500 mM NaCl, 20 mM imidazole, 5% glycerol, 5 mM β-mercaptoethanol, and 1 mM phenylmethanesulfonylfluoride) and disrupted by sonication. The insoluble debris was removed by centrifugation. The supernatant was applied to a Ni-NTA column (GE Healthcare). The column was washed extensively with the wash buffer (50 mM HEPES, pH 7.5, 500 mM NaCl, 50 mM imidazole, 5% glycerol, and 5 mM β-mercaptoethanol) and bound DYRK2 protein was eluted using the elution buffer (50 mM HEPES, pH 7.5, 500 mM NaCl, 500 mM imidazole, 5% glycerol, and 5 mM β -mercaptoethanol). After cleavage with TEV protease, the protein sample was passed through a second Ni-NTA column to separate untagged DYRK2 from the uncut protein and the protease. Final purification was performed using a Superdex 200 gel filtration column (GE Healthcare), and the protein was eluted using the final buffer (25 mM HEPES, pH 7.5, 400 mM NaCl, 1 mM DTT, and 5% glycerol). Purify the DYRK2-D275N using the same method as shown above. Purified DYRK2 and DYRK2-D275N were concentrated to 10 mg mL–1 and flash-frozen with liquid nitrogen.

DYRK2208-552 was incubated with 200 µM compounds on ice before crystallization. The protein-compounds mixture was then mixed in a 1:1 ratio with the crystallization solution (0.36 M-0.5 M sodium citrate tribasic dihydrate, 0.01 M sodium borate, pH 7.5–9.5) in a final drop size of 2 µl. The DYRK2-compounds crystals were grown at 18 °C by the sitting-drop vapor diffusion method. Cuboid-shaped crystals appeared after 4–7 days. Crystals were cryoprotected in the crystallization solution supplemented with 35% glycerol before frozen in liquid nitrogen.

The X-ray diffraction data were collected at Shanghai Synchrotron Radiation Facility (SSRF) beamline BL17U. The diffraction data were indexed, integrated, and scaled using HKL-2000 (HKL Research). The structure was determined by molecular replacement using the published DYRK2 structure (PDB ID: 3K2L) (Soundararajan et al., 2013) as the search model using the Phaser program (McCoy et al., 2007). Chembiodraw (version 13.0) was used to generated the.cif files for compounds, and then compounds were fitted using the LigandFit program in Phenix (Adams et al., 2010). The structural model was further adjusted in Coot (Emsley et al., 2010) and refined using Phenix. The quality of the structural model was checked using the MolProbity program in Phenix. The crystallographic data and refinement statistics are summarized in Figure 1—source data 1.

### IC50 determination

IC50 determination was carried out using the ADP-Glo kinase assay system (Promega, Madison, WI). Active DYRK1A, DYRK1B, DYRK2, DYRK3, Haspin, and MARK3 were purified as reported previously. C17 IC50 measurements were carried out against the kinases with final concentrations between 0.01 nM to 100 μM in vitro (C17 was added to the kinase reaction prior to ATP master mix). The values were expressed as a percentage of the DMSO control. DYRK isoforms (1 ng/μL diluted in 50 mM Tris-HCl pH7.5, 2 mM DTT) were assayed against Woodtide (KKISGRLSPIMTEQ) in a final volume of 5 μL containing 50 mM Tris pH 7.5, 150 μM substrate peptide, 5 mM MgCl2 and 10–50 μM ATP (10 μM for DYRK2 and DYRK3, 25 μM for DYRK1A and 50 μM for DYRK1B) and incubated for 60 min at room temperature. Haspin (0.2 ng/μL diluted in 50 mM Tris-HCl pH7.5, 2 mM DTT) was assayed against a substrate peptide H3(1–21) (ARTKQTARKSTGGKAPRKQLA) in a final volume of 5 μL containing 50 mM Tris pH 7.5, 200 μM substrate peptide, 5 mM MgCl2 and 200 μM ATP and incubated for 120 min at room temperature. MARK3 (1 ng/μL diluted in 50 mM Tris-HCl pH7.5, 2 mM DTT) was assayed against Cdc25C peptide (KKKVSRSGLYRSPSMPENLNRPR) in a final volume of 5 μL 50 mM Tris pH 7.5, 200 μM substrate peptide, 10 mM MgCl2 and 5 μM ATP and incubated for 120 min at room temperature. After incubation, the ADP-Glo kinase assay system was used to determine kinase activity following the manufacturer’s protocol. IC50 curves were developed as % of DMSO control and IC50 values were calculated using GraphPad Prism 8.4.0 software. Results are means ± SD for triplicate reactions with similar results obtained in at least one other experiment.

### KINOMEscan kinase profiling

The KINOMEscan kinase profiling assay was carried out at The Largest Kinase Assay Panel in the world for Protein Kinase Profiling (https://www.discoverx.com). C17 kinase selectivity was determined against a panel of 468 protein kinases. Results are presented as a percentage of kinase activity in DMSO control reactions. Protein kinases were assayed in vitro with 500 nM final concentration of C17 and the results are presented as an average of triplicate reactions ± SD or in the form of comparative histograms.

### Quantitative phosphoproteomic analysis

Triplicate U266 cells treated with/without C17 were lysed by the lysis buffer containing 1% (v/v) Triton X-100, 7 M Urea, 50 mM Tris-HCl, pH 8.5, 1 mM pervanadate, protease inhibitor mixture (Roche), and phosphatase inhibitor mixtures (Roche). The cell lysates were firstly digested with trypsin (Promega, USA) by the in-solution digestion method (Chen et al., 2018). After desalting, the Ti4+-IMAC tip was used to purify the phosphopeptides. The phosphopeptides were desalted by the C18 StageTip prior to the LC MS/MS analysis (Chen et al., 2018). An Easy-nLC 1200 system coupled with the Q-Exactive HF-X mass spectrometer (Thermo Fisher Scientific, USA) was used to analyze the phosphopeptide samples with 1 hr LC gradient. The raw files were searched against Human fasta database (71,772 protein entries, downloaded from Uniprot on March 27, 2018) by MaxQuant (version 1.5.5.1). The oxidation (M), deamidation (NQ), and Phospho (STY) were selected as the variable modifications for the phosphopeptide identification, while the carbamidomethyl was set as the fixed modification. The false discovery rate (FDR) was set to 0.01 on PTM site, peptide, and protein level. Label-free quantification (LFQ) and match between runs were set for the triplicate analysis data. The MaxQuant searching file ‘Phospho (STY)Sites.txt’ was loaded into the Perseus software (version 1.5.5.3) to make volcano plots using student’s t-test and cutoff of ‘FDR < 0.05 and S0 = 2’. The pathway analysis was performed using the Kyoto Encyclopedia of Genes and Genomes (KEGG) database with cutoff of adjusted p-value < 0.05.

### Quantitative RT-PCR

Total RNA from cells was extracted using the RNeasy Mini Kit (Qiagen) and reverse-transcribed with the PrimeScript Real Time reagent Kit (with genomic DNA Eraser, TAKARA). The product of reverse transcription was diluted five times then subjected to quantitative rtPCR reaction in Applied Biosystems ViATM7 Real-Time PCR System (Applied Biosvstems). The 20 μl quantitative rtPCR reaction contained 2 μl of the reverse-transcription reaction mixture, 2 × Hieff quantitative rtPCR SYBR Green Master Mix (Yeasen), 0.2 μM quantitative rtPCR forward primer, 0.2 μM quantitative rtPCR reverse primer (Figure 4—figure supplement 2) and ddH2O. The quantitative rtPCR reaction condition was as follows: 95 °C, 5 min; (95 °C. 10 s; 60 °C, 30 s) × 40 cycles; 95 °C, 15 s; 60 °C, 1 min; 95 °C. 15 s (collect fluorescence at a ramping rate of 0.05 °C s-1); 4 °C, hold. Data analysis was performed by QuantStudioTM Real-Time PCR Software v.1.3.

### STIM1 and 4EBP1 protein purification

The cytosolic domain of STIM1 (bases 235-END) with an N-terminal GST-tag and TEV protease cleavage site which expressed in E. coli BL21 (DE3). Bacterial cultures were grown at 37 °C in LB medium to an OD600 of 0.6–0.8 before induced with 0.5 mM IPTG overnight at 18 °C. Cells were collected by centrifugation and frozen at –80 °C. For protein purification, the cells were suspended in the lysis buffer 50 mM Tris-HCl (pH 7.5), 500 mM NaCl, 5 mM β-mercaptoethanol, and 1 mM phenylmethanesulfonylfluoride and disrupted by sonication. The insoluble debris was removed by centrifugation. The supernatant was applied to a glutathione-Sepharose column (GE Healthcare) and eluted in lysis buffer containing 20 mM glutathione. Purify the GST-4EBP1 using the same method as shown above. Purified STIM1 and 4EBP1 were flash-frozen with liquid nitrogen.

### In vitro kinase assays

DYRK2 kinase assays were performed in 50 mM HEPES, pH 7.5, 100 mM NaCl, 10 mM MnCl2, 10 mM ATP using STIM1 or 4EBP1 as substrate. The kinase reactions were initiated by the addition of DYRK2 with indicated concentration. Assays (25 μl volume) were carried out at 30 °C for 30 min, and terminated by addition of SDS-PAGE buffer containing 20 mM EDTA and then boiled. The reaction mixtures were then separated by SDS-PAGE and visualized by Coomassie Blue staining or analyzed by immuno-blot using primary antibodies as indicated throughout.

### Co-immunoprecipitation and western blotting

HEK293A cells were cultured and transfected as described above. After transfection, the cells were washed three times with Ca2+-free buffer containing 10 mM HEPES, 10 mM D-glucose, 150 mM NaCl, 4 mM KCl, 3 mM MgCl2 and 0.1 mM EGTA (pH 7.4). Treatment of DMEM containing 1 μM of C17 at 37 °C were used for DYRK2 inhibition. Ca2+-store depletion was triggered by incubating cells with 2 μM thapsigargin for 20 min. The cells were then lysed with lysis buffer consisting of 50 mM Tris-HCl (pH 7.5), 1 mM EGTA, 1 mM EDTA, 1% (v/v) Nonidet P40 (substitute), 1 mM sodium orthovanadate, 50 mM sodium fluoride, 5 mM sodium pyrophosphate, 0.27 M sucrose, 2 mM dithiothreitol (DTT), 1 mM benzamidine, 0.1 mM PMSF (added before lysis), 1% (v/v) protease inhibitor cocktail (Roche) and 1% (v/v) Phosphatase Inhibitor Cocktail (Roche). Protein concentrations were determined with the BCA protein assay kit Pierce (Thermo-Pierce). For immunoprecipitations, lysates containing equal protein amounts were incubated with FLAG–beads 2 hr at 4 °C. FLAG–beads were washed three times with lysis buffer containing 0.15 M NaCl. Proteins were eluted from the FLAG–beads by addition of 300 µg FLAG peptides (Smart Lifesciences). Eluted proteins were reduced by addition of loading buffer with 4 mM DTT followed by heating at 95 °C for 10 min. For western blotting, samples were electrophoresed in 10% or 12% gels and transferred to PVDF membranes. All antibody dilutions and washes were carried out in Tris-buffered saline (TBS; 137 mM NaCl, 19 mM Tris HCl and 2.7 mM KCl, at pH 7.4) containing 0.1% Tween-20 (TBS-T). Membranes were blocked in 5% non-fat milk solution in TBS-T for 1 hr at room temperature, incubated with indicated primary antibodies overnight at 4 °C, and incubated with secondary antibodies (horseradish peroxidase-linked anti-mouse or anti-rabbit) for 1 hr at room temperature. Blots were developed with AMERSHAM ImageQuant 800 (GE Healthcare) and exposed to film.

### Quantitative analysis of phosphorylation sites on STIM1

Triplicate HEK293A cells co-transfected with GFP-ORAI1, FLAG-DRYK2 and FLAG-STIM1 for 36 hr was treated with 1 μM and 10 μM C17 respectively for 1 hr. After collected, cells were washed with the Ca2+-free buffer to remove excess Ca2+ and then lysed by the lysis buffer. For immunoprecipitations, lysates containing equal protein amounts were incubated with FLAG–beads for 1 hr at 4 °C, which were washed three times with the lysis buffer afterwards. The proteins were eluted from the FLAG–beads by addition of 500 μg FLAG peptides (Smart Lifesciences). Then the eluted proteins were digested with trypsin by the FASP digestion method (Wiśniewski et al., 2009). The peptides were analyzed on a Q Exactive Plus mass spectrometer (Thermo Fisher Scientific) with 1 hr LC gradient. The raw files were searched against Human fasta database (downloaded from Uniprot) by MaxQuant (version 1.6.3.4). The oxidation (M), deamidation (NQ), and Phospho (STY) were selected as the variable modifications for the phosphopeptide identification, while the carbamidomethyl was set as the fixed modification. The false discovery rate (FDR) was set to 0.01 on PTM site, peptide, and protein level. Label-free quantification (LFQ) and match between runs were set for the triplicate analysis data.

### Confocal microscopy

Confocal imaging were carried out with a ZEISS LSM880 imaging system equipped with 65 × oil objective (NA = 1.45, Zeiss), 488- and 543 nm laser, controlled by Zen 2.3 SP1 software. YFP (505 ± 35) and mCherry (640 ± 50) emission were collected with CaAsP PMT (Optical section, 1.1 μm). Image analysis was performed using Image J Fiji (NIH) (Zheng et al., 2018). Each repeat contains data from at least 6 cells.

### Fluorescence imaging

Fluorescence signals were recorded using a ZEISS obersever-7 microscope equipped with an X-Cite 120-Q (Lumen dynamics), brightline filter sets (Semrock Inc), a 40 × oil objective (NA = 1.30), and a Prime 95B Scientific CMOS (sCMOS) camera (Teledyne Imaging). This system was controlled by Slide book6 software (3i). For fluorescence resonance energy transfer (FRET) measurements, three-channel-corrected FRET include cyan fluorescent protein (CFP), yellow fluorescent protein(YFP) and FRET raw were collected with corresponding filters, FCFP (438 ± 12Ex/ 483 ± 16 Em), FYFP (510 ± 10Ex/542 ± 13.5 Em) and FRETraw (438 ± 12Ex/542 ± 13.5 Em), every 10 s. Calibration of bleed through from FRET donor or acceptor to FRET channel (0.20, and 0.36, correspondingly), as well as the system-dependent factor, G (2.473) were done as described earlier (Ma et al., 2015). These parameters were then used to generate calculate FRET efficiency (Eapp) values from raw fluorescent signals, similar to those previously described (Ma et al., 2017). At least 16 cells were collected for each repeat. Corresponding results were calculated with Matlab 2014a software and plotted with GraphPad Prism 8.4.0 software. Representative traces of at least three independent experiments are shown as mean ± SEM.

### Confocal imaging and intracellular Ca2+ measurement

Intracellular Ca2+ measurement was performed on a Zeiss LSM 700 laser scanning confocal microscope equipped with a 63 × oil immersion objective lens (N.A. = 1.4) controlled by ZEN software. GCaMP6f fluorescence was excited using a 488 nm line of solid-state laser and fluorescence emission was collected with a 490- to 555 nm band-pass filter; mCherry fluorescence was excited using a 555 nm line of solid-state laser and fluorescence emission was collected with a 580 nm long-pass filter. Two high-sensitivity PMTs were used for detection. Cells were imaged at 10 s intervals for up to 20 mins. All live cell imaging experiments were performed at room temperature. Data were processed and analyzed using Zen and ImageJ software.

For intracellular Ca2+ measurement, HEK293A cells were plated on glass-bottom 35 mm dishes and transfected as described above. Cells were washed with Ca2+ free buffer 3 times 24 hr after transfection. For DYRK2 inhibition, cells were treated with DMEM containing 1 μM of C17 at 37 for 1 hr before Ca2+ free buffer rinse. Depletion of Ca2+-stores was triggered by incubating cells with 1 μM thapsigargin in Ca2+-free buffer, and Store-operated Ca2+ entry (SOCE) was induced by addition of 2 mM CaCl2 to thapsigargin containing buffer. One μM C17 was added for DYRK2 inhibition assay. The intracellular free calcium concentration was measured by monitoring the fold change of GCaMP6f fluorescence, the data were shown as the mean ± SEM.

### Statistics and data presentation

Most experiments were repeated three times with multiple technical replicates to be eligible for the indicated statistical analyses, and representative image has been shown. All results are presented as mean ± SD unless otherwise mentioned. Data were analysed using Graphpad Prism 8.4.0 statistical package.
