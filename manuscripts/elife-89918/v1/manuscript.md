# Structural characterization of ligand binding and pH-specific enzymatic activity of mouse Acidic Mammalian Chitinase

## Authors

- Roberto Efraín Díaz<sup>1</sup> ([ORCID: 0000-0002-1172-9919](https://orcid.org/0000-0002-1172-9919))
- Andrew K Ecker<sup>3</sup>
- Galen J Correy<sup>1</sup>
- Pooja Asthana<sup>1</sup>
- Iris D Young<sup>1</sup>
- Bryan Faust<sup>3</sup>
- Michael C Thompson<sup>7</sup>
- Ian B Seiple<sup>3</sup>
- Steven Van Dyken<sup>9</sup>
- Richard M Locksley<sup>10</sup>
- James S Fraser<sup>1</sup> ([ORCID: 0000-0002-5080-2859](https://orcid.org/0000-0002-5080-2859)) †

### Affiliations

1. Department of Bioengineering and Therapeutic Sciences, University of California, San Francisco San Francisco United States ([ROR:043mz5j54](https://ror.org/043mz5j54))
2. Tetrad Graduate Program, University of California, San Francisco San Francisco United States ([ROR:043mz5j54](https://ror.org/043mz5j54))
3. Department of Pharmaceutical Chemistry, University of California, San Francisco San Francisco United States ([ROR:043mz5j54](https://ror.org/043mz5j54))
4. Cardiovascular Research Institute, University of California, San Francisco San Francisco United States ([ROR:043mz5j54](https://ror.org/043mz5j54))
5. Department of Biochemistry and Biophysics, University of California, San Francisco San Francisco United States ([ROR:043mz5j54](https://ror.org/043mz5j54))
6. Biophysics Graduate Program, University of California, San Francisco San Francisco United States ([ROR:043mz5j54](https://ror.org/043mz5j54))
7. Chemistry and Chemical Biology Graduate Program, University of California, San Francisco San Francisco United States ([ROR:043mz5j54](https://ror.org/043mz5j54))
8. Department of Chemistry and Chemical Biology, University of California, Merced Merced United States ([ROR:00d9ah105](https://ror.org/00d9ah105))
9. Department of Pathology and Immunology, Washington University School of Medicine in St Louis St Louis United States ([ROR:036c27j91](https://ror.org/036c27j91))
10. Department of Medicine, University of California, San Francisco San Francisco United States ([ROR:043mz5j54](https://ror.org/043mz5j54))
11. Department of Microbiology and Immunology, University of California, San Francisco San Francisco United States ([ROR:043mz5j54](https://ror.org/043mz5j54))
12. University of California, Howard Hughes Medical Institute, San Francisco San Francisco United States ([ROR:006w34k90](https://ror.org/006w34k90))

† Corresponding author

## Abstract

Chitin is an abundant biopolymer and pathogen-associated molecular pattern that stimulates a host innate immune response. Mammals express chitin-binding and chitin-degrading proteins to remove chitin from the body. One of these proteins, Acidic Mammalian Chitinase (AMCase), is an enzyme known for its ability to function under acidic conditions in the stomach but is also active in tissues with more neutral pHs, such as the lung. Here, we used a combination of biochemical, structural, and computational modeling approaches to examine how the mouse homolog (mAMCase) can act in both acidic and neutral environments. We measured kinetic properties of mAMCase activity across a broad pH range, quantifying its unusual dual activity optima at pH 2 and 7. We also solved high-resolution crystal structures of mAMCase in complex with oligomeric GlcNAcn, the building block of chitin, where we identified extensive conformational ligand heterogeneity. Leveraging these data, we conducted molecular dynamics simulations that suggest how a key catalytic residue could be protonated via distinct mechanisms in each of the two environmental pH ranges. These results integrate structural, biochemical, and computational approaches to deliver a more complete understanding of the catalytic mechanism governing mAMCase activity at different pH. Engineering proteins with tunable pH optima may provide new opportunities to develop improved enzyme variants, including AMCase, for therapeutic purposes in chitin degradation.

## Introduction

Chitin, a polymer of β(1-4)-linked N-acetyl-D-glucosamine (GlcNAc), is the second most abundant polysaccharide in nature. Chitin is present in numerous pathogens, such as nematode parasites, dust mites, and fungi (Cabib and Bowers, 1975; Zhu et al., 2016; Tang et al., 2015), and is a pathogen-associated molecular pattern (PAMP) that activates mammalian innate immunity (Elieh Ali Komi et al., 2018). To mitigate constant exposure to environmental chitin, mammals have evolved unusual multi-gene loci that are highly conserved and encode chitin-response machinery, including chitin-binding (chi-lectins) and chitin-degrading (chitinases) proteins.

Humans express two active chitinases as well as five chitin-binding proteins that recognize chitin across many tissues (Bussink et al., 2007). Chitin levels can be potentially important for mammalian lung and gastrointestinal health. These tissues have distinct pH, with the lung environment normally ~pH 7.0 and the stomach environment normally ~pH 2.0, which raises the question of how chitin-response machinery has evolved to function optimally across such diverse chemical environments. Acidic Mammalian Chitinase (AMCase, also known as Chia, for chitinase, acidic) was originally discovered in the stomach and named for its acidic isoelectric point. AMCase is also constitutively expressed in the lungs at low levels and overexpressed upon chitin exposure (Van Dyken and Locksley, 2018; Zhu et al., 2004; Reese et al., 2007), suggesting this single enzyme has evolved to perform its function under vastly different chemical conditions. Chitin clearance is particularly important for mammalian pulmonary health, where exposure to and accumulation of chitin can be deleterious. In the absence of AMCase, chitin accumulates in the airways, leading to epithelial stress, chronic activation of type 2 immunity, and age-related pulmonary fibrosis (Van Dyken et al., 2017; Van Dyken and Locksley, 2018).

AMCase is a member of the glycosyl hydrolase family 18 (GH18) (Davies and Henrissat, 1995), the members of which hydrolyze sugar linkages through a conserved two-step mechanism where the glycosidic oxygen is protonated by an acidic residue and a nucleophile adds into the anomeric carbon leading to elimination of the hydrolyzed product (Figure 1A). This mechanism is corroborated by structures of different GH18 chitinases, most notably S. marcescens Chitinase A (PDB ID: 1FFQ) (Papanikolau et al., 2003). In inhibitor-bound structures for human AMCase (hAMCase; PDB ID: 3FY1), interactions mimicking the retentive, post-cleavage intermediate state pre-hydrolysis of the oxazolinium intermediate are adopted by the nonhydrolyzable analogs (Cole et al., 2010; Olland et al., 2009). Unlike the nonhydrolyzable inhibitors, we expect that the oxazolinium intermediate formed from chitin will reopen into the reducing-end GlcNAc monomer unit upon the nucleophilic addition of water.

![Figure 1.](https://cdn.elifesciences.org/articles/89918/elife-89918-fig1-v1.jpg)

**Figure 1.:** (A) Chemical depiction of the conserved two-step mechanism where the glycosidic oxygen is protonated by an acidic residue and a nucleophile adds into the anomeric carbon leading to elimination of the hydrolyzed product. (B) The rate of 4MU-chitobioside catalysis (1 /s) by mAMCase catalytic domain is plotted as a function of 4MU-chitobioside concentration (µM). Each data point represents n=4 with error bars representing the standard deviation. Michaelis-Menten equation without substrate inhibition was used to estimate the kcat and KM from the initial rate of reaction at various substrate concentrations. (C) The rate of substrate turnover (1 /s) by mAMCase catalytic domain is plotted as a function of pH. Error bars represent the 95% confidence interval. (D) The Michaelis-Menten constant of mAMCase catalytic domain is plotted as a function of pH. Error bars represent the 95% confidence interval. (E) The catalytic efficiency (kcat/KM) of mAMCase catalytic domain is plotted as a function of pH. (F) Hypothetical catalytic activity modeled explained by a low pH mechanism (red), and high pH mechanism (blue) and their corresponding total activity (dashed line).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/89918/elife-89918-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) Schematic of modified endpoint 4MU-chitobioside assay. (B) Reaction pH before and after quenching with 0.1 M Gly-NaOH pH 10.7, and (C) a pH strip reference sheet.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/89918/elife-89918-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** (A) A linear fit forced through Y=0 is used to generate the standard curve for converting RFU to 4MU [µM]. Each data point represents n=8 with error bars representing the standard deviation. (B) 4MU fluorescence (RFU) is plotted as a function of time (s). Each data point represents n=4 with error bars representing the standard deviation. A linear fit is applied to each concentration of 4MU-chitobioside to calculate an initial rate. RFU is converted to µM using a 4MU standard curve. (C) The rate of 4MU-chitobioside catalysis (1 /s) by mAMCase catalytic domain is plotted as a function of 4MU-chitobioside concentration (µM). Each data point represents n=4 with error bars representing the standard deviation. Michaelis-Menten equation without substrate inhibition was used to estimate the kcat and KM from the initial rate of reaction at various substrate concentrations.

Biochemical studies of mouse AMCase (mAMCase) measuring relative activity levels demonstrated a global maximum activity at acidic pH, but also a broad second local optimum near neutral pH (Boot et al., 2001). This result suggested that mAMCase exhibits two distinct pH optima, which is unlike most enzymes that exhibit a shift or broadening of enzymatic activity across conditions (Yoong et al., 2006; Sajedi et al., 2005; Bhunia et al., 2011). For mAMCase the global maximum near pH 2.0 resembles the chemical environments of the stomach and the local maximum near pH 7.0 is similar to the environment of the lung. These two pH optima in the same enzyme suggest that mAMCase may employ different mechanisms to perform its function in different environments (Seibold et al., 2009). In contrast, the human homolog has maximal activity at pH 4.6 with sharply declining activity at more acidic and basic pH (Seibold et al., 2009; Chou et al., 2006). This optimum corresponds with the pH of lung tissue in pulmonary fibrosis and other disease contexts, suggesting that hAMCase may have been selected for its ability to clear chitin from the lungs and restore healthy lung function.

The activity of mAMCase has been previously measured through endpoint experiments with limited insight into the rate of catalysis, substrate affinity, and potential substrate inhibition (Seibold et al., 2009). While the pH profile of mAMCase has been reported as a percentage of maximum activity at a given pH, it is unclear how the individual kinetic parameters (KM or kcat) vary (Boot et al., 2001). These gaps have made it challenging to define the mechanism by which mAMCase shows distinct enzymatic optima at different pHs. One possibility is that mAMCase undergoes structural rearrangements to support this adaptation. Alternatively AMCase may have subtly different mechanisms for protonating the catalytic glutamic acid depending on the environmental pH.

In this work, we explore these hypotheses by employing biophysical, biochemical, and computational approaches to observe and quantify mAMCase function at different pHs. We measured the mAMCase hydrolysis of chitin, which revealed significant activity increase under more acidic conditions compared to neutral or basic conditions. To understand the relationship between catalytic residue protonation state and pH-dependent enzyme activity, we calculated the theoretical pKa of the active site residues and performed molecular dynamics (MD) simulations of mAMCase at various pHs. We also directly observed conformational and chemical features of mAMCase between pH 4.74 and 5.60 by solving X-ray crystal structures of mAMCase in complex with oligomeric GlcNAcn across this range. Together these data support a model in which mAMCase employs two different mechanisms for obtaining a proton in a pH-dependent manner, providing a refined explanation as to how this enzyme recognizes its substrate in disparate environments.

## Results

### New assay confirms broad pH profile for mAMCase

Prior studies have focused on relative mAMCase activity at different pH (Boot et al., 2001; Seibold et al., 2009; Kashimura et al., 2015), limiting the ability to define its enzymological properties precisely and quantitatively across conditions of interest. To expand upon these previous observations of dual optima in mAMCase activity at pH 2.0 and 7.0, we measured mAMCase activity in vitro. We developed an approach that would enable direct measurement of kcat and KM for mAMCase across a broad pH range by modifying a prior assay that continuously measures mAMCase-dependent breakdown of a fluorogenic chitin analog, 4-methylumbelliferone (4MU) conjugated chitobioside. To overcome the pH-dependent fluorescent properties of 4MU-chitobioside, we reverted the assay into an endpoint assay, which allowed us to measure substrate breakdown across different pH (Barad et al., 2020; Figure 1—figure supplement 1).

We conducted our endpoint assay across a pH range of 2.0–7.4 to reflect the range of physiological conditions at its in vivo sites of action (Figure 1B; Data available at doi: 10.5281/zenodo.8250616). We then derived the Michaelis-Menten parameters at each pH value measured (Figure 1—figure supplement 2; Data available at doi: 10.5281/zenodo.8250616). We found that mAMCase has maximum activity at pH 2.0 with a secondary local maximum at pH 6.5, pointing to a bimodal distribution of activity across pH. This is consistent with the relative activity measurements previously performed on mAMCase, but distinct from a single broad pH range, as has been observed for kcat of hAMCase (Boot et al., 2001; Seibold et al., 2009). The two maxima at pH 2.0 and 6.5 are an approximate match the pH at the primary in vivo sites of mAMCase expression, the stomach and lungs, respectively (Seibold et al., 2009). These observations raise the possibility that mAMCase, unlike other AMCase homologs, may have evolved an unusual mechanism to accommodate multiple physiological conditions.

We also found that low pH primarily improves the rate of mAMCase catalysis 6.3-fold (kcat; Figure 1C), whereas KM (Figure 1D) worsens 2.5-fold from pH 7.4 to pH 2.0. Similar to chitotriosidase the other active chitinase in mammals and also a GH18 chitinase, we observe an apparent reduction in the rate of mAMCase catalysis across all pH values measured at 4MU-chitobioside concentrations above 80 μM, which suggests that mAMCase may be subject to product inhibition (Aguilera et al., 2003). The underlying mechanism for the observed product inhibition may be that mAMCase can transglycosylate the products, as has been previously observed at pH 2.0 and 7.0 (Wakita et al., 2017). This potential product inhibition leads to a systematic underprediction of rates by the Michaelis-Menten model at high substrate concentrations. The catalytic efficiency (kcat/KM) of mAMCase may not capture the effects of product inhibition given that these constants reflect sub-saturating substrate concentrations. Independent of the potential for product inhibition, the trend that mAMCase has highest kcat at very low pH and another local optimum at more neutral pH is clear. We hypothesize that these activity data resemble two overlapping activity distributions, suggesting that the rate at lower pH activity is dependent on the concentration of free protons in solution and that the higher pH optimum results from a distinct mechanism (Figure 1E).

### Characterization of mAMCase ligand occupancy and conformational heterogeneity

Our biochemical analyses led us to hypothesize that the pH-dependent activity profile of mAMCase is linked to the mechanism by which catalytic residues are protonated. Previous structural studies on AMCase have focused on interactions between inhibitors like methylallosamidin and the catalytic domain of the protein. We built on these efforts by solving the structure of mAMCase in complex with oligomeric GlcNAcn, the building block of chitin. We used chitin oligomers because they are chemically identical to polymeric chitin found in nature but are soluble and therefore more amenable for co-crystallization than crystalline chitin is. We successfully determined high resolution X-ray crystal structures of the apo mAMCase catalytic domain at pH 5.0 and 8.0 (PDB ID: 8FG5, 8FG7) and holo mAMCase catalytic domain between pH 4.74–5.60 in complex with either GlcNAc2 or GlcNAc3 (PDB ID: 8GCA, 8FRC, 8FR9, 8FRB, 8FRD, 8FRG, 8FRA; Figure 2—figure supplement 1; Table 1).

**Table 1.**
 Data collection and refinement statistics.Statistics for the highest resolution shell are shown in parentheses.


<table>
  <thead>
    <tr>
      <th>Dataset</th>
      <th>Apo at 100 K</th>
      <th>Apo at 277 K</th>
      <th>Holo with GlcNAc3 at pH 4.74</th>
      <th>Holo with GlcNAc2 at pH 4.91</th>
      <th>Holo with GlcNAc2 at pH 5.08</th>
      <th>Holo with GlcNAc2 at pH 5.25</th>
      <th>Holo with GlcNAc2 at pH 5.25</th>
      <th>Holo with GlcNAc2 at pH 5.43</th>
      <th>Holo with GlcNAc2 at pH 5.60</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>PDB ID</td>
      <td>8FG5</td>
      <td>8FG7</td>
      <td>8GCA</td>
      <td>8FRC</td>
      <td>8FR9</td>
      <td>8FRB</td>
      <td>8FRD</td>
      <td>8FRG</td>
      <td>8FRA</td>
    </tr>
    <tr>
      <td>Diffraction Data DOI</td>
      <td>10.18430/M38FG5</td>
      <td>10.18430/M38FG7</td>
      <td>10.18430/M38GCA</td>
      <td>10.18430/M38FRC</td>
      <td>10.18430/M38FR9</td>
      <td>10.18430/M38FRB</td>
      <td>10.18430/M38FRD</td>
      <td>10.18430/M38FRG</td>
      <td>10.18430/M38FRA</td>
    </tr>
    <tr>
      <td>pH</td>
      <td>5.00</td>
      <td>8.00</td>
      <td>4.74</td>
      <td>4.91</td>
      <td>5.08</td>
      <td>5.25</td>
      <td>5.25</td>
      <td>5.43</td>
      <td>5.60</td>
    </tr>
    <tr>
      <td>Ligand</td>
      <td>N/A</td>
      <td>N/A</td>
      <td>GlcNAc3</td>
      <td>GlcNAc2</td>
      <td>GlcNAc2</td>
      <td>GlcNAc2</td>
      <td>GlcNAc2</td>
      <td>GlcNAc2</td>
      <td>GlcNAc2</td>
    </tr>
    <tr>
      <td>[Ligand] mM</td>
      <td>N/A</td>
      <td>N/A</td>
      <td>12.67</td>
      <td>29.00</td>
      <td>19.33</td>
      <td>19.33</td>
      <td>29.00</td>
      <td>29.00</td>
      <td>19.33</td>
    </tr>
    <tr>
      <td>Wavelength</td>
      <td>1.117</td>
      <td>1.116</td>
      <td>1.116</td>
      <td>1.116</td>
      <td>1.116</td>
      <td>1.116</td>
      <td>1.116</td>
      <td>1.116</td>
      <td>1.116</td>
    </tr>
    <tr>
      <td>Resolution range</td>
      <td>46.8–1.3 (1.346–1.3)</td>
      <td>50.88–1.64 (1.699–1.64)</td>
      <td>61.83–1.7 (1.761–1.7)</td>
      <td>69.52–1.92 (1.989–1.92)</td>
      <td>69.59–1.5 (1.554–1.5)</td>
      <td>57.29–1.7 (1.761–1.7)</td>
      <td>58.67–1.68 (1.74–1.68)</td>
      <td>69.59–1.741 (1.803–1.741)</td>
      <td>86.27–1.95 (2.02–1.95)</td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>P 1 21 1</td>
      <td>P 21 21 21</td>
      <td>P 21 21 2</td>
      <td>P 2 21 21</td>
      <td>P 2 21 21</td>
      <td>P 21 21 21</td>
      <td>P 2 21 21</td>
      <td>P 21 21 2</td>
      <td>P 21 21 21</td>
    </tr>
    <tr>
      <td>Unit cell (length)</td>
      <td>60.04 42.25 67.41</td>
      <td>63.6466 71.8436 84.6724</td>
      <td>76.0664 91.7195 106.132</td>
      <td>70.9333 92.6896 105.123</td>
      <td>71.1131 92.6412 105.423</td>
      <td>91.9263 106.963 146.492</td>
      <td>70.755 92.451 104.99</td>
      <td>92.8934 105.041 70.8116</td>
      <td>92.0659 106.705 146.57</td>
    </tr>
    <tr>
      <td>Unit cell (angles)</td>
      <td>90 95.18 90</td>
      <td>90 90 90</td>
      <td>90 90 90</td>
      <td>90 90 90</td>
      <td>90 90 90</td>
      <td>90 90 90</td>
      <td>90 90 90</td>
      <td>90 90 90</td>
      <td>90 90 90</td>
    </tr>
    <tr>
      <td>Total reflections</td>
      <td>2099252 (194837)</td>
      <td>620486 (61796)</td>
      <td>516529 (48842)</td>
      <td>339863 (33874)</td>
      <td>702566 (63651)</td>
      <td>1010525 (98078)</td>
      <td>499250 (48902)</td>
      <td>420425 (37138)</td>
      <td>691049 (67775)</td>
    </tr>
    <tr>
      <td>Unique reflections</td>
      <td>83050 (8251)</td>
      <td>47999 (4678)</td>
      <td>82111 (8079)</td>
      <td>53587 (5242)</td>
      <td>109106 (10560)</td>
      <td>158679 (15679)</td>
      <td>78153 (7593)</td>
      <td>71329 (6974)</td>
      <td>105512 (10401)</td>
    </tr>
    <tr>
      <td>Multiplicity</td>
      <td>25.3 (23.6)</td>
      <td>12.9 (13.2)</td>
      <td>6.3 (6.0)</td>
      <td>6.3 (6.5)</td>
      <td>6.4 (6.0)</td>
      <td>6.4 (6.3)</td>
      <td>6.4 (6.4)</td>
      <td>5.9 (5.3)</td>
      <td>6.5 (6.6)</td>
    </tr>
    <tr>
      <td>Completeness (%)</td>
      <td>99.99 (99.98)</td>
      <td>99.37 (98.65)</td>
      <td>99.72 (99.42)</td>
      <td>99.88 (99.79)</td>
      <td>97.48 (95.47)</td>
      <td>99.87 (99.88)</td>
      <td>98.71 (97.03)</td>
      <td>99.56 (99.03)</td>
      <td>99.74 (99.62)</td>
    </tr>
    <tr>
      <td>Mean I/sigma(I)</td>
      <td>13.31 (1.88)</td>
      <td>7.00 (1.19)</td>
      <td>8.83 (3.12)</td>
      <td>7.72 (3.21)</td>
      <td>16.77 (5.46)</td>
      <td>9.09 (3.10)</td>
      <td>9.68 (3.09)</td>
      <td>6.18 (2.56)</td>
      <td>5.65 (1.26)</td>
    </tr>
    <tr>
      <td>Wilson B-factor</td>
      <td>15.81</td>
      <td>16.38</td>
      <td>12.17</td>
      <td>13.44</td>
      <td>9.16</td>
      <td>12.47</td>
      <td>11.55</td>
      <td>15.76</td>
      <td>12.64</td>
    </tr>
    <tr>
      <td>R-merge</td>
      <td>0.1342 (2.107)</td>
      <td>0.2489 (2.119)</td>
      <td>0.1811 (1.138)</td>
      <td>0.1531 (0.5265)</td>
      <td>0.06539 (0.2976)</td>
      <td>0.1111 (0.5593)</td>
      <td>0.1155 (0.569)</td>
      <td>0.1321 (0.4674)</td>
      <td>0.1619 (0.6276)</td>
    </tr>
    <tr>
      <td>R-meas</td>
      <td>0.137 (2.153)</td>
      <td>0.2591 (2.203)</td>
      <td>0.1972 (1.242)</td>
      <td>0.1669 (0.5728)</td>
      <td>0.07122 (0.3259)</td>
      <td>0.121 (0.61)</td>
      <td>0.126 (0.6197)</td>
      <td>0.1448 (0.5188)</td>
      <td>0.176 (0.6822)</td>
    </tr>
    <tr>
      <td>R-pim</td>
      <td>0.02718 (0.4382)</td>
      <td>0.07097 (0.5968)</td>
      <td>0.07709 (0.4917)</td>
      <td>0.06573 (0.2233)</td>
      <td>0.02784 (0.1311)</td>
      <td>0.04745 (0.2411)</td>
      <td>0.04965 (0.2425)</td>
      <td>0.05834 (0.2207)</td>
      <td>0.06836 (0.2647)</td>
    </tr>
    <tr>
      <td>CC1/2</td>
      <td>0.999 (0.858)</td>
      <td>0.996 (0.502)</td>
      <td>0.997 (0.805)</td>
      <td>0.994 (0.884)</td>
      <td>0.999 (0.943)</td>
      <td>0.997 (0.888)</td>
      <td>0.993 (0.68)</td>
      <td>0.994 (0.845)</td>
      <td>0.997 (0.845)</td>
    </tr>
    <tr>
      <td>CC*</td>
      <td>1 (0.961)</td>
      <td>0.999 (0.818)</td>
      <td>0.999 (0.944)</td>
      <td>0.998 (0.969)</td>
      <td>1 (0.985)</td>
      <td>0.999 (0.97)</td>
      <td>0.998 (0.9)</td>
      <td>0.998 (0.957)</td>
      <td>0.999 (0.957)</td>
    </tr>
    <tr>
      <td>Reflections used in refinement</td>
      <td>83046 (8251)</td>
      <td>47968 (4677)</td>
      <td>82030 (8059)</td>
      <td>53543 (5242)</td>
      <td>109065 (10557)</td>
      <td>158531 (15678)</td>
      <td>78103 (7592)</td>
      <td>71295 (6967)</td>
      <td>105380 (10401)</td>
    </tr>
    <tr>
      <td>Reflections used for R-free</td>
      <td>4099 (422)</td>
      <td>2328 (234)</td>
      <td>4142 (427)</td>
      <td>2738 (273)</td>
      <td>5449 (559)</td>
      <td>7978 (802)</td>
      <td>3878 (334)</td>
      <td>3561 (348)</td>
      <td>5174 (542)</td>
    </tr>
    <tr>
      <td>R-work</td>
      <td>0.1317 (0.2361)</td>
      <td>0.1469 (0.2707)</td>
      <td>0.1598 (0.2428)</td>
      <td>0.1472 (0.1616)</td>
      <td>0.1376 (0.1615)</td>
      <td>0.1423 (0.1850)</td>
      <td>0.1396 (0.1724)</td>
      <td>0.1657 (0.2194)</td>
      <td>0.1695 (0.2074)</td>
    </tr>
    <tr>
      <td>R-free</td>
      <td>0.1519 (0.2613)</td>
      <td>0.1717 (0.3244)</td>
      <td>0.1978 (0.2952)</td>
      <td>0.1898 (0.2065)</td>
      <td>0.1644 (0.1932)</td>
      <td>0.1778 (0.2315)</td>
      <td>0.1689 (0.2113)</td>
      <td>0.2083 (0.2737)</td>
      <td>0.2056 (0.2463)</td>
    </tr>
    <tr>
      <td>CC(work)</td>
      <td>0.970 (0.583)</td>
      <td>0.978 (0.789)</td>
      <td>0.969 (0.819)</td>
      <td>0.953 (0.846)</td>
      <td>0.971 (0.922)</td>
      <td>0.970 (0.878)</td>
      <td>0.963 (0.903)</td>
      <td>0.959 (0.749)</td>
      <td>0.961 (0.869)</td>
    </tr>
    <tr>
      <td>CC(free)</td>
      <td>0.969 (0.558)</td>
      <td>0.975 (0.729)</td>
      <td>0.953 (0.775)</td>
      <td>0.951 (0.793)</td>
      <td>0.966 (0.910)</td>
      <td>0.958 (0.791)</td>
      <td>0.954 (0.882)</td>
      <td>0.951 (0.757)</td>
      <td>0.970 (0.846)</td>
    </tr>
    <tr>
      <td>Number of non-hydrogen atoms</td>
      <td>3583</td>
      <td>3427</td>
      <td>7330</td>
      <td>6953</td>
      <td>7507</td>
      <td>13986</td>
      <td>6951</td>
      <td>7343</td>
      <td>14428</td>
    </tr>
    <tr>
      <td>macromolecules</td>
      <td>3107</td>
      <td>3097</td>
      <td>6094</td>
      <td>6016</td>
      <td>6186</td>
      <td>11938</td>
      <td>6019</td>
      <td>6286</td>
      <td>11900</td>
    </tr>
    <tr>
      <td>ligands</td>
      <td>1</td>
      <td>1</td>
      <td>394</td>
      <td>342</td>
      <td>516</td>
      <td>746</td>
      <td>344</td>
      <td>401</td>
      <td>571</td>
    </tr>
    <tr>
      <td>solvent</td>
      <td>475</td>
      <td>329</td>
      <td>1034</td>
      <td>763</td>
      <td>1057</td>
      <td>1666</td>
      <td>756</td>
      <td>852</td>
      <td>2237</td>
    </tr>
    <tr>
      <td>Protein residues</td>
      <td>376</td>
      <td>376</td>
      <td>752</td>
      <td>738</td>
      <td>750</td>
      <td>1478</td>
      <td>738</td>
      <td>738</td>
      <td>1478</td>
    </tr>
    <tr>
      <td>Nucleic acid bases</td>
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
      <td>RMS(bonds)</td>
      <td>0.006</td>
      <td>0.008</td>
      <td>0.008</td>
      <td>0.007</td>
      <td>0.01</td>
      <td>0.006</td>
      <td>0.007</td>
      <td>0.008</td>
      <td>0.003</td>
    </tr>
    <tr>
      <td>RMS(angles)</td>
      <td>0.88</td>
      <td>0.96</td>
      <td>1.05</td>
      <td>0.91</td>
      <td>1.1</td>
      <td>0.92</td>
      <td>0.91</td>
      <td>1.12</td>
      <td>0.66</td>
    </tr>
    <tr>
      <td>Ramachandran favored (%)</td>
      <td>98.4</td>
      <td>98.66</td>
      <td>98.8</td>
      <td>98.23</td>
      <td>98.26</td>
      <td>98.84</td>
      <td>98.64</td>
      <td>98.35</td>
      <td>98.1</td>
    </tr>
    <tr>
      <td>Ramachandran allowed (%)</td>
      <td>1.6</td>
      <td>1.34</td>
      <td>1.2</td>
      <td>1.77</td>
      <td>1.74</td>
      <td>1.16</td>
      <td>1.36</td>
      <td>1.65</td>
      <td>1.9</td>
    </tr>
    <tr>
      <td>Ramachandran outliers (%)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Rotamer outliers (%)</td>
      <td>1.22</td>
      <td>0.92</td>
      <td>0.62</td>
      <td>0.79</td>
      <td>0.92</td>
      <td>0.87</td>
      <td>0.63</td>
      <td>0.6</td>
      <td>0.88</td>
    </tr>
    <tr>
      <td>Clashscore</td>
      <td>1.66</td>
      <td>0.83</td>
      <td>1.25</td>
      <td>1.85</td>
      <td>1.3</td>
      <td>1.31</td>
      <td>1.6</td>
      <td>1.44</td>
      <td>1.66</td>
    </tr>
    <tr>
      <td>Average B-factor</td>
      <td>21.71</td>
      <td>19.1</td>
      <td>16.09</td>
      <td>14.55</td>
      <td>12.73</td>
      <td>15.72</td>
      <td>14.2</td>
      <td>17.9</td>
      <td>15.9</td>
    </tr>
    <tr>
      <td>macromolecules</td>
      <td>19.83</td>
      <td>17.9</td>
      <td>13.9</td>
      <td>13.24</td>
      <td>10.3</td>
      <td>13.76</td>
      <td>12.5</td>
      <td>16.36</td>
      <td>13.88</td>
    </tr>
    <tr>
      <td>ligands</td>
      <td>98.88</td>
      <td>46.35</td>
      <td>23.57</td>
      <td>18.87</td>
      <td>15.73</td>
      <td>17.53</td>
      <td>15.9</td>
      <td>23.5</td>
      <td>19.18</td>
    </tr>
    <tr>
      <td>solvent</td>
      <td>33.82</td>
      <td>30.3</td>
      <td>27.53</td>
      <td>23.9</td>
      <td>26.25</td>
      <td>29.3</td>
      <td>27.32</td>
      <td>27.98</td>
      <td>26.24</td>
    </tr>
    <tr>
      <td>Number of TLS groups</td>
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
  </tbody>
</table>

Across these different datasets, we observed complex ligand density in the active site of mAMCase. In all of our datasets, we observed continuous ligand density that resembled higher order chitin oligomers (e.g. GlcNAc4, GlcNAc5, or GlcNAc6). This observation was confusing given that these structures were co-crystallized with either GlcNAc2 or GlcNAc3. For example, due to the continuous nature of ligand density observed in our mAMCase-GlcNAc3 co-crystal structure at pH 4.74 (PDB ID: 8GCA, chain A), we initially modeled hexaacetyl-chitohexaose (H-(GlcNAc)6-OH) into the –4 to +2 sugar-binding subsites, using the nomenclature for sugar-binding subsites from Davies et al., 1997. This nomenclature defines the sugar-binding subsites as -n to +n, with -n corresponding to the non-reducing end and +n the reducing end.

We next continued with a modeling approach that replaced higher order oligomer models with models that only used the chemically defined oligomers present in the crystallization drop. To accomplish this modeling of different binding poses, we placed multiple copies of these oligomers consistent with an interpretation of extensive conformational heterogeneity (Figure 2—figure supplement 2). In one sample co-crystallized with GlcNAc3 at pH 4.74 (PDB ID: 8GCA, chains A-B), we identified ligand density that was consistent with GlcNAc2, suggesting that some hydrolysis occurs in the crystal. The resulting model includes compositional heterogeneity as there are both types of oligomer present.

Therefore, across all of our datasets, we modeled a combination of ligand binding events consisting of overlapping GlcNAc2 or GlcNAc3 molecules at each sugar-binding site, i.e. GlcNAc2 ResID 401 Conf. A occupied subsites –3 to –2 while GlcNAc2 ResID 401 Conf. C occupied subsites –2 to –1. By providing each ligand molecule with an alternative conformation ID, this allowed both occupancies and B-factors to be refined (Figure 2A, B and C; additional details in Methods). Across these different datasets, we observed ligand density for different combinations of occupancy over the –4 to +2 sugar-binding subsites (Figure 2A). While modeling chito-oligomers into strong electron density, we observed strong positive difference density between sugar-binding subsites near the C2 N-acetyl and the C6’ alcohol moieties. Using the non-crystallographic symmetry (NCS) ‘ghost’ feature in Coot, we were then able to observe that the positive difference density between ligand subsites in one chain could be explained by the dominant ligand pose observed in another associated crystallographic chain, suggesting the presence of a low-occupancy binding events. This observation led to the discovery that GlcNAcn occupies intermediate subsites, which we label n+0.5, continuing to follow the nomenclature established by Davies et al., in addition to canonical sugar-binding subsites (Figure 2B; Davies et al., 1997).

![Figure 2.](https://cdn.elifesciences.org/articles/89918/elife-89918-fig2-v1.jpg)

**Figure 2.:** (A) PDB ID: 8GCA, chain A. Stick representation of all GlcNAc2 sugar-binding events observed in n sugar-binding subsites with 2mFo-DFc map shown as a 1.2 Å contour (blue), the subsite nomenclature, and a schematic of alternative conformation ligand modeling. (B) PDB ID: 8FRA, chain D. Stick representation of all GlcNAcn binding events observed in n+0.5 sugar-binding subsites with 2mFo-DFc map shown as a 1.2 Å contour (blue), the subsite nomenclature, and a schematic of alternative conformation ligand modeling. (C) PDB ID: 8FR9, chain B. Stick representation of all GlcNAcn binding events observed in n and n+0.5 sugar-binding subsites with 2mFo-DFc map shown as a 1.2 Å contour (blue), the subsite nomenclature, and a schematic of alternative conformation ligand modeling.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/89918/elife-89918-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) Brightfield view of crystals used to determine the structures reported in this paper. (B) Hanging drop crystallization trays were set up as a 2-condition gradient to identify optimal crystallization conditions for AMCase +GlcNAcn. pH increased along the X-axis from pH 3.70–5.60. Ligand concentration increased along the Y-axis from 0 mM to 29 mM [GlcNAc2], 19 mM [GlcNAc3], 10 mM [GlcNAc4], or 8 mM [GlcNAc5]. Black boxes indicate conditions where crystals grew. Lilac boxes indicate conditions for structures reported in this paper.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/89918/elife-89918-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** PDB ID: 8FG5, 8FG7 (apo); 8GCA, 8FRC, 8FR9, 8FRB, 8FRD, 8FRG, 8FRA (holo). Violin plots showing the distribution of pKa across Asp136, Asp138, Glu140 between (A) apo and (B) holo mAMCase structures in the inactive or active conformation.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/89918/elife-89918-fig2-figsupp3-v1.jpg)

**Figure 2—figure supplement 3.:** (A) Stick representation of ligand and aromatic residues Trp31, Tyr34, Trp99, and Trp218 in the active site with 2mFo-DFc map shown as a 1.2 Å contour (blue). (B) Stick representation of ligand and polar residues Arg145, His208, Asp213, and His269 in the active site with 2mFo-DFc map shown as a 1.2 Å contour (blue). (C, D) Stick representation of ligand and catalytic residues Asp136, Asp138, and Glu140 in the active site with 2mFo-DFc map shown as a 1.2 Å contour (blue).

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/89918/elife-89918-fig2-figsupp4-v1.jpg)

**Figure 2—figure supplement 4.:** (A) PDB ID: 8GCA, chain A with GlcNAc6 modeled for viewing simplicity. Stick representation highlighting the stabilizing H-π interactions between Trp31, Trp360, and Trp218 and the −3,–1,+1, and +2 sugars, respectively. (B) PDB ID: 8GCA, chain A with GlcNAc6 modeled for viewing simplicity. Stick representation highlighting the stabilizing hydrogen bond interactions between the –1 sugar and Asp138 (2.6 Å) and Asp213 (3.4 Å), and between the +1 sugar and Tyr141 (3.0 Å). Glu140 is 2.8 Å from the glycosidic oxygen bridging the –1 and +1 sugars. (C) PDB ID: 8FRA, chains C (left) and D (right). Stick representation highlighting the stabilizing hydrogen bond interactions that we argue stabilize the +1 sugar (left; chain A) and the +1’ sugar-binding subsite (right; chain B).

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/89918/elife-89918-fig2-figsupp5-v1.jpg)

**Figure 2—figure supplement 5.:** (A) Ringer analysis to detect alternative conformations in electron density maps. Ringer detected one peak for Asp136 at χ1=180° and Glu140 at χ1=300°, indicating only one conformation, whereas two peaks were detected for Asp138 at χ1=180° and χ1=300°, indicating two alternative conformations. (B) Stick representation of Asp136, Asp138, and Glu140 with 2mFo-DFc map volume shown as a 1.2 Å contour (blue).

In addition to identifying novel n+0.5 sugar-binding subsites, we also observed strong positive difference density above the +1 subsite, which we label +1’. During ligand refinement, we observed density for both the α- and β–1,4-linked GlcNAc2 anomers in the active site. This unexpected configurational heterogeneity, which is observable because of the high resolution of our datasets (1.30–1.95 Å), likely formed as a result of equilibration between the two anomers through an oxocarbenium close-ion-pair intermediate. The ability for the active site to accommodate and form interactions with these ligands is important given its role in degrading crystalline chitin, a complex and often recalcitrant substrate that likely requires multiple binding events by AMCase before degradation can occur. We did not identify consistent trends between the contents of the crystallization drop (pH, substrate identity, and substrate concentration), the crystal properties (space group, unit cell dimensions, resolution), and the resulting density in the active site; however, as outlined below, the protein conformations and substrate states are highly correlated. Collectively, modeling a combination of ligand binding modes, linkages, and anomers allowed us to interpret the resulting coordinates in a more complete model of how mAMCase coordinates and stabilizes polymeric chitin for catalysis (Figure 2; Figure 2—figure supplement 2; Figure 2—figure supplement 3; Supplementary file 1).

### Structural characterization of mAMCase catalytic triad D1xD2xE

We interpreted the protein-ligand interactions along the canonical binding sites (Figure 2—figure supplement 2). As with other chitinases, we observe a network of tryptophans consisting of Trp31, Trp360, Trp99, and Trp218 stabilizing the positioning of the ligand into the binding site through a series of H-π interactions with the −3,–1,+1, and +2 sugars, respectively (Watanabe et al., 2003; Horn et al., 2006; Zakariassen et al., 2009). These interactions are primarily with the axial hydrogens of the respective sugars but also include the N-H of the –3 and +1 sugar and the 6’ O-H of the +2 sugar (Figure 2—figure supplement 3). Further, we observe Asp213 accepting a hydrogen bond with the 6’ OH of the –1 sugar and Tyr141 acting as a hydrogen bond donor to the 6’ OH of the +1 sugar. These two hydrogen bonds likely orient the ligand in the catalytically competent pose where the glycosidic oxygen bridging the –1 and +1 sugars is 2.8 Å away from the acidic Glu140 -OH (Figure 2—figure supplement 4). With this proximity, Glu140 can act as a hydrogen bond donor to the strained (122o bond angle) bridging oxygen forming a hydrogen bond to promote the formation of an oxazolinium intermediate and subsequent cleavage of the glycosidic bond. We observed two interactions with the sugar in the –4 position supporting the ligand orientation far from the enzymatic active site. Residues involved in ligand binding and catalysis adopt similar side chain conformations in the absence of ligand (PDB ID: 8FG5, 8FG7), suggesting that the active site is organized prior to ligand binding and not subject to ligand-stabilized conformational changes.

We hypothesize that the +1’ subsite is primarily occupied by the product GlcNAc2 prior to its displacement from the active site by subsequent sliding of polymeric chitin (Figure 2B; Jiménez-Ortega et al., 2021). At this position, Trp99 and Trp218 engage in CH-π interactions with the +1 and+2 sugars, respectively while Asp213 forms a new H-bond with the carbonyl oxygen and Tyr141 retains an H-bond with the hydroxyl moiety on the +1 sugar. We are able to observe this post-catalysis binding mode due to the stabilizing interactions between GlcNAc2 and Asp213, Trp99, Trp218, and Tyr141 (Figure 2—figure supplement 3). Together, these observations highlight the dynamic chitin binding modes within the mAMCase active site. Collectively, the observed non-canonical binding modes of these sugars is consistent with previous observations that once bound to polymeric chitin, GH18 chitinases engage in chain sliding from the reducing end of the substrate following catalysis (Nakamura et al., 2018).

In contrast to the largely static interactions outlined above, we observed conformational heterogeneity in the catalytically critical Asp138 residue, suggesting flipping between two equally stable states facing each of the other two residues in the catalytic triad (Asp136 or Glu140; van Aalten et al., 2001). Using Ringer, we confirmed that there are two Asp138 conformations and only a single conformation for Asp136 and Glu140 (Figure 2—figure supplement 4; Data available at doi: 10.5281/zenodo.7758815; Lang et al., 2010). Across 20 chains from the datasets derived from different pH and co-crystallization conditions (Supplementary file 1), we quantified whether Asp138 is preferentially oriented towards Asp136 (inactive conformation) or preferentially oriented towards Glu140 (active conformation).

Prior work has suggested that Asp138 orients itself towards Glu140 to promote stabilization of the substrate’s twisted boat conformation in the –1 subsite. Therefore, we explored if Asp138 conformation is correlated with ligand pose (Olland et al., 2009; van Aalten et al., 2001; Fusetti et al., 2002; Songsiriritthigul et al., 2008). As previously mentioned, we assign alternative conformation IDs to each ligand molecule based on its subsite positioning. We calculate subsite occupancy by taking the sum of all alternative ligand conformations at a given subsite, i.e. the occupancy of subsite –2 is equal to the occupancies of GlcNAc2 ResID 401 Conf. A and GlcNAc2 ResID 401 Conf. C (Figure 3A; see Methods for additional details; Data available at doi: 10.5281/zenodo.7905828). We observe a strong positive correlation between Asp138 conformation and ligand pose only in the –2 to +1 subsites (Figure 3B; Supplementary file 1). When the –1 subsite is at least 50% occupied, Asp138 prefers the active conformation (up towards Glu140). In this orientation, Asp138(HD2) forms a H-bond with Glu140(OE1) (2.6 Å) while Asp138(OD1) forms an H-bond with the amide nitrogen of GlcNAc in the –1 subsite (2.6 Å). Glu140(OE2) is 2.8 Å away from the glycosidic oxygen bridging the –1 and +1 sugars. We suspect that the inverse correlation between Asp138 active conformation and the –2.5 and –1.5 sugar-binding subsites represents ligand translocation toward the catalytic residues, prior to enzyme engagement with the ligand. When chitin occupies a canonical sugar-binding subsite, AMCase forms stabilizing H-bonds with the ligand prior to catalysis. These observations are consistent with the proposed catalytic mechanism where upon protonation, the equilibrium between Asp138 conformations shifts to favor the active conformation (toward Glu140) where Asp138 stabilizes Glu140 in proximity to the glycosidic oxygen prior to catalysis.

![Figure 3.](https://cdn.elifesciences.org/articles/89918/elife-89918-fig3-v1.jpg)

**Figure 3.:** (A) PDB ID: 8FR9, chain B. Schematic of the alternative conformation ligand modeling. (B) Linear correlation between sugar-binding subsite occupancy and Asp138 active conformation occupancy.

### Theoretical pKa calculations of mAMCase catalytic triad D1xD2xE

Based on the dual pH optimum observed in our kinetics assay and the conformational heterogeneity of Asp138, we calculated the theoretical pKa for catalytic D1xD2xE motif on mAMCase using PROPKA 3.0. PROPKA does not account for alternative conformations in its calculations, so we split our protein models to contain single conformations of the catalytic residues Asp136, Asp138, and Glu140. While PROPKA does account for ligands in its calculations, running the calculations with different alternative conformations of GlcNAc2 or GlcNAc3 had little effect on the calculated pKas for the active site residues (Figure 2—figure supplement 2; Data available at doi: 10.5281/zenodo.7905863). Despite the observed ligand heterogeneity, we observe a relatively narrow range of pKa values for the catalytic triad. This suggests that the pKa of the catalytic residues is primarily influenced by the position of nearby residues and that the placement of solvent or ligand molecules has little effect. When Asp138 is oriented towards Asp136 (the inactive conformation), the pKa of the catalytic residues are 2.0, 13.0, 7.7 for Asp136, Asp138, and Glu140 respectively. Similarly, when Asp138 is oriented towards Glu140 (the active conformation), the pKa of the catalytic residues are 3.4, 12.4, 6.4 for Asp136, Asp138, and Glu140, respectively. Taking this information together, it is clear that the pKa of Asp136 and Glu140 are both affected by the orientation of Asp138 (Figure 4A; Supplementary file 2; Data available at doi: 10.5281/zenodo.7905863). The pKa of Asp136 suggests that at pH >3.4, Asp136 is deprotonated, and its conjugate base is more stable. We observe a similar pKa distribution for the catalytic triad in human AMCase and other GH18 chitinases with publicly available structures and optimum pH activity profiles (Figure 4A–C).

![Figure 4.](https://cdn.elifesciences.org/articles/89918/elife-89918-fig4-v1.jpg)

**Figure 4.:** (A) PDB ID: 8GCA, chain A. Distribution of pKa across Asp136, Asp138, Glu140 of mAMCase structures in either Asp138 inactive or Asp138 active conformation. (B) PDB ID: 3FXY, 3RM4, 3RM8, 3RME (inactive conformation); 2YBU, 3FY1 (active conformation). Distribution of pKa across Asp136, Asp138, Glu140 of hAMCase structures in either Asp138 inactive or Asp138 active conformation. (C) PDB ID: 3ALF, 3AQU, 3FXY, 3RM4, 3RM8, 3RME (inactive conformation); 2UY2, 2UY3, 2YBU, 4HME, 4MNJ, 4R5E, 4TXE (active conformation). Distribution of pKa across the catalytic triad D1xD2xE of GH18 chitinases in either D2 inactive or active conformation.

Given the pH range of our crystallization conditions, we expect that Asp136 is deprotonated while Asp138 and Glu140 are protonated. We hypothesize that this anionic aspartate is capable of forming a strong ionic hydrogen bond interaction with Asp138 orienting it in the inactive conformation. When Asp136 is protonated to its aspartic acid state at pH <3.2, we expect that it is only capable of forming the relatively weaker neutral hydrogen bond with Asp138 lowering the favorability of the inactive conformation.

Additionally, when interpreting the pKa of Glu140, we hypothesize that under acidic conditions (pH 2.0–6.5), Glu140 is capable of obtaining its catalytic proton from solution. The accessibility of Asp138’s proton to Glu140 progressively decreases as pH increases from pH 2.0–6.5. In contrast, under neutral and basic conditions (pH 6.0–7.4), Asp138 can shuttle a proton from Asp136 by rotating about its Cα-Cβ bond to supply Glu140 with the proton. Glu140 subsequently uses the proton that it obtained from Asp138 to protonate the glycosidic bond in chitin, promoting hydrolysis as previously described in several chitinases (van Aalten et al., 2001; Synstad et al., 2004; Bussink et al., 2008). While this mechanism could explain how mAMCase has a local optimum at pH 2.0, it is insufficient to explain why we do not observe a similar optimum in hAMCase. The narrow range of pKa values across GH18 chitinases suggest that differences in optimal activity by pH may be influenced by other factors, such as protein stability, conformational dynamics, or coordination of distal GlcNAc residues by ionizable residues (Mishra et al., 2021).

### Molecular dynamics

Based on our enzymology results suggesting the possibility of differential activity between acidic pH (pH 2.0) and near neutral pH (pH 6.5) and theoretical pKa calculations of the active site residues, we performed short atomistic molecular dynamics simulations to interrogate the movement of catalytic residues. While all the crystal structures we obtained were collected in a narrow acidic pH range between 4.74–5.60, we ran simulations at pH 2.0 and pH 6.5, ensuring that the protonation states of side chains populated by 3DProtonate were supported by our PROPKA calculations (Data available at doi: 10.5281/zenodo.7758821; Labute, 2009; Olsson et al., 2011). These simulations allowed us to investigate our hypothesis that at neutral pH mAMCase enzymatic activity is dependent on the protonation state of Asp136. We performed simulations using protein models that contain Asp138 in either the inactive (down towards Asp136; ‘inactive simulation’) or active conformation (up towards Glu140; ‘active simulation’) to avoid bias from the starting conformation.

In all our simulations, we observe that Glu140 orients its acidic proton towards the glycosidic bond between the –1 and +1 sugars. The distance between the acidic proton of Glu140 and the glycosidic oxygen fluctuates between 1.5 and 2.3 Å for the duration of the simulation, with a median distance of 1.8 Å. The positioning of this proton is necessary to allow for the oxocarbenium cleavage of the glycosidic bond and recapitulates the positioning of Glu140 in our experimental structures. In simulations initiated from the inactive conformation at pH 2.0, we observe that Asp 138 is readily able to rotate about its Cα-Cβ bond to adopt the active conformation forming the same hydrogen bond between Asp138 and Glu140. In contrast, from simulations at pH 6.5 started from the Asp138 inactive conformation, we observe that Asp138 remains hydrogen bonded to Asp136 throughout the duration of the simulation (inactive conformation; Figure 5A–C; Data available at doi: 10.5281/zenodo.7758821). This series of simulations allowed us to better visualize which catalytic side chains are dynamic and which catalytic side chains positioning are well maintained to help build our catalytic mechanism.

![Figure 5.](https://cdn.elifesciences.org/articles/89918/elife-89918-fig5-v1.jpg)

**Figure 5.:** (A) Asp138 χ1 angles over a 10 ns simulation. (B) Representative minimum distance snapshots of structure during pH 6.5 inactive simulation (left), and pH 2.0 active simulation (right). (C) Distribution of Asp138 χ1 angles over a 10 ns simulation.

## Discussion

mAMCase is an unusual enzyme that can bind and degrade polymeric chitin in very different pH environments. We hypothesized that mAMCase employs different mechanisms to protonate its catalytic glutamate under acidic and neutral pH. Through our analysis, we hypothesize that the observed ligand and catalytic residue densities and occupancies in our crystal structures are consistent with the previously proposed GH18 catalytic mechanism (Meekrathok et al., 2017). By modeling GlcNAc2 as sequentially overlapping ligands in alternative conformations (Figure 2), we are able to visualize each step in the proposed catalytic cycle of mAMCase (Figure 6, Animation 1, Animation 2). This mechanism, which has been observed in other glycoside hydrolases, occurs when the glycosidic oxygen is protonated by an acidic residue and a nucleophile adds into the anomeric carbon leading to elimination of the hydrolyzed product.

![Figure 6.](https://cdn.elifesciences.org/articles/89918/elife-89918-fig6-v1.jpg)

**Figure 6.:** (A) PDB ID: 8GCA, chain A with no ligand (step 1); with GlcNAc4 generated by phenix.elbow using PubChem ID: 10985690 (step 2); with GlcNAc6 generated by phenix.elbow using PubChem ID: 6918014 (step 3–4, 8); with oxazolinium intermediate generated by phenix.elbow using PubChem ID: 25260046 (steps 5.1–5.2); with GlcNAc2 and GlcNAc4 generated by phenix.elbow using PubChem ID: 439544 and 10985690, respectively (steps 6–7). Chemical representation of GH18 catalytic cycle with corresponding molecular models of each step. Catalytic residues Asp136, Asp138, Glu140, and ligands are shown as sticks. Protons are shown as gray spheres.

![Animation 1.](https://cdn.elifesciences.org/articles/89918/elife-89918-animation1-v1.gif.jpg)

**Animation 1.:** Catalytic residues Asp136, Asp138, Glu140, and ligands are shown as sticks. Protons are shown as gray spheres.

![Animation 2.](https://cdn.elifesciences.org/articles/89918/elife-89918-animation2-v1.gif.jpg)

**Animation 2.:** Catalytic residues Asp136, Asp138, Glu140, and ligands are shown as sticks. Protons are shown as gray spheres.

Based on our crystal data and simulations, we envision that at neutral pH, Asp136 is deprotonated (pKa = 2.1) forming an ionic hydrogen bond with Asp138 (pKa = 13.1). In contrast, at low pH Asp136 is protonated, yet continues to form a weaker hydrogen bond with Asp138 (Figure 6 - Step 1). Glu140 (pKa = 7.7) is protonated across the enzyme’s active pH range. Upon ligand binding (Figure 6 - Step 2), Glu140 stabilizes the sugar at the –1 subsite. The ligand then translocates forward by one GlcNAc2 to occupy the +1 and+2 subsites (Figure 6 - Step 3). At neutral pH, Asp136 is predominantly deprotonated. When protonation of Asp136 occurs, this destabilizes the Asp136-Asp138 hydrogen bond and allows Asp138 to rotate about its Cα-Cβ bond into the active conformation (towards Glu140). However, since Asp136 is always protonated at low pH, the Asp136-Asp138 hydrogen bond is less energetically favorable, therefore Asp138 can adopt the active conformation more readily (Figure 6- Step 4).

Once Asp138 is in the active conformation, Asp138 and Glu140 form stabilizing interactions with the N-acetyl group of the ligand, priming it to become the nucleophile required for catalysis (Figure 6 - Step 4). Glu140 provides its ionizable proton to the ligand’s glycosidic oxygen, increasing the electrophilicity of the anomeric carbon (Figure 6 - Step 5; Iino et al., 2019). The carbonyl oxygen of the –1 sugar N-acetyl group then nucleophilically adds into the anomeric carbon from the β face to cleave the glycosidic bond, forming the oxazolinium intermediate. At neutral pH, the resultant deprotonated Glu140 is then re-protonated through proton shuttling in which Asp136 donates its proton to Asp138 and Asp138 donates its ionizable proton to Glu140. At acidic pH, we propose that Glu140 can be directly re-protonated by a proton in solution (Figure 6 - Step 5). At a neutral pH, this leads to Asp138 returning to an inactive conformation. However, at low pH Asp136 and Glu140 are both protonated due to the high concentration of protons in solution, allowing Asp138 to remain in the active conformation and form stabilizing interactions with the N-acetyl group on the ligand. The oxazolinium intermediate is then hydrolyzed by a water molecule, generating a GlcNAc2 catalysis product in the +1 and+2 sugar subsites (Figure 6 - Step 6). The GlcNAc2 product dissociates from the +1 to+2 sugar subsites, then the ligand undergoes ‘decrystallization’ and ‘chain sliding’ before re-entering the catalytic cycle, assuming AMCase is bound to a longer polymer such as its natural substrate (Nakamura et al., 2018). At neutral pH this catalytic mechanism is reset with Asp138 in its inactive conformation, however at low pH the catalytic mechanism is reset with Asp138 already in the active conformation. This could lead to faster rates of catalysis at lower pH compared to the neutral pH mechanism, providing a possible explanation for the observed changes in rate at varying pH.

While our model helps us propose a plausible explanation of why mAMCase is highly active at pH 2, it does not explain why hAMCase has a single activity optimum around pH 5.

Prior work by Kashimura et al. has demonstrated that E. coli-expressed mAMCase is remarkably stable across a broad pH range (Kashimura et al., 2013). Similar experiments have not yet been performed on hAMCase. Olland et al., 2009 previously identified Arg145, His208, and His269 as important for pH specificity . Seibold et al., 2009 argued that hAMCase isoforms containing asthma protective mutations N45D, D47N, and M61R, which are wildtype in mAMCase, may influence the pKa of Asp138-Glu140 by undergoing structural rearrangement . Tabata et al., 2022 identified mutations across the course of evolution in Carnivora that were inactivating or structurally destabilizing (loss of S-S bonds; ). Okawa et al., 2016 identified how primate AMCase lost activity by integration of specific, potentially pKa-shifting, mutations relative to the mouse counterpart .

To this end, we explored sequence differences between mouse and human AMCase homologs for insight into why mAMCase has such high enzymatic activity at pH 2.0 and 6.5 compared to hAMCase. We identified ionizable residues on mAMCase that likely contribute to its overall stability and are not present in hAMCase. Mutations Lys78Gln, Asp82Gly, and Lys160Gln result in the loss of surface-stabilizing salt bridges in hAMCase and may contribute to its reduced activity at more acidic pH. It is likely that the dual pH optima of mAMCase is intrinsic to the catalytic mechanism, where Glu140 can be protonated directly from solution (at low pH) or through proton shuttling across the catalytic triad (at neutral pH; Figure 1E). However, hAMCase is likely too destabilized at low pH to observe an increase in kcat. hAMCase may be under less pressure to maintain high activity at low pH due to humans’ noninsect-based diet, which contains less chitin compared to other mammals with primarily insect-based diets (Tabata et al., 2022).

Together, these data demonstrate the importance of using structural and biochemical assays to develop our understanding of the catalytic mechanism governing mAMCase activity. Using biochemical and structural methods, we have developed a detailed model of how AMCase fulfills its role in chitin recognition and degradation. Small chitin oligomers are ideal for measuring the ability of AMCase to cleave β–1,4-glycosidic linkages between GlcNAc units, but these small oligomers do not represent the complex crystalline chitin encountered by AMCase in the lung. It is difficult to extrapolate the effects we observe using small chitin oligomers to binding (kon), processivity (kproc), catalysis (kcat), or product release (koff) on the native large and heterogeneous oligomeric substrates. In the future, we hope to be able to directly visualize the mAMCase-chitin interactions and characterize each step of the catalytic mechanism including decrystallization, degradation, product release, and chain sliding (also known as processivity).

To further understand the impact of pH on the structure of AMCase, it will be necessary to crystallize AMCase across a broader pH range that may expose conformational and structural changes that contribute to mAMCase’s unique pH activity profile. Our simulations have important limitations that could be overcome by quantum mechanical simulations that allow for changes in protonation state and improved consideration of polarizability. Further, neutron diffraction crystallography could provide novel critical insight into the placement of protons across the active site and help to develop a more complete model of mAMCase’s catalytic mechanism at different pH. Understanding the mechanistic basis behind an enzyme’s dual pH optima will enable us to engineer proteins with tunable pH optima to develop improved enzyme variants for therapeutic purposes for diseases, such as asthma and lung fibrosis.

## Methods

### Protein expression and purification

Protein expression and purification mAMCase catalytic domain (UniProt: Q91XA9; residues 22–391) was cloned into a pTwist CMV [pmRED006; Twist Biosciences; Addgene ID: 200228] or pcDNA3.1(+) [pmRED013; Genscript; Addgene ID: 200229] expression vector with a C-terminal 6xHis tag. To express mAMCase catalytic domain, 0.8–1 µg/mL plasmid DNA was transfected into ExpiCHO-S cells (ThermoFisher Scientific #A29127) using the Max Titer protocol (ThermoFisher Scientific MAN0014337). After cells were grown shaking at 37 °C with 8% CO2 for 18–22 hours, ExpiFectamine CHO Enhancer (ThermoFisher Scientific #A29129) and ExpiCHO feed (ThermoFisher Scientific #A29129) was added to the flask. Cells were then transferred to 32 °C with 5% CO2 for an additional 9–13 days of growth, with a second volume of ExpiCHO feed added to the flask on day 5 post-transfection. Cells were removed by centrifugation at 4000 RCF for 15 min at 4 °C, and the remaining supernatant was filtered using a 0.22 µm filter at 4 °C. Filtered supernatant was either dialyzed into Ni–nitrilotriacetic acid (NTA) loading buffer [100 mM Tris-HCl (pH 8.0), 150 mM NaCl] at 4 °C in a 10 kDa molecular weight cutoff (MWCO) Slide-A-Lyzer Dialysis Cassette, (ThermoFisher Scientific #66810) for 18–24 hr or concentrated in a 10 kDa MWCO centrifugal concentrator (Amicon #UFC901008) at 4000 RCF in 5 min intervals until the final volume was equal to 10 mL, which was then diluted 1:10 with loading buffer for a total volume of 100 mL. The dialyzed supernatant volume was filtered using a 0.22 µm filter at 4 °C. All purification steps were performed at 4 °C using an ÄKTA fast protein liquid chromatography system (Cytiva). The dialyzed supernatant was applied to a 5 ml HisTrap FF column (Cytiva, 17525501). The column was washed with 40 mL of loading buffer followed by 25 mL of 10% Ni-NTA elution buffer [100 mM Tris-HCl (pH 8.0), 150 mM NaCl, 500 mM imidazole] and then eluted over a 50 mL gradient from 10% to 100% elution buffer. Eluted protein was concentrated to 2.5 mL using a 10 kDa MWCO centrifugal concentrator (Amicon, UFC901024). The sample was further purified by size exclusion chromatography (SEC) using a HiLoad 16/600 Superdex 75 pg column (Cytiva, 28989333) equilibrated with SEC buffer [25 mM Tris-HCl (pH 8.0), 50 mM NaCl]. Eluted fractions were collected and stored at 4 °C for further use.

### 4MU-chitobioside endpoint assay

Chitinase catalytic activity has previously been assayed using 4-methylumbelliferyl chitobioside (4MU-CB; Sigma-Aldrich M9763) (O’Brien and Colwell, 1987; Renkema et al., 1995). 100 nM chitinase enzyme was incubated with varying concentrations of 4MU-chitobioside up to 117 μM in McIlvaine Buffer at 37 °C (Barad et al., 2020). The 4-methylumbelliferone (4MU) fluorophore is quenched by a ß-glycosidic linkage to a short chitin oligomer, which is cleaved by a chitinase enzyme, which generates fluorescence with peak excitation at 360 nm and emission at 450 nm. 4MU fluorescence is pH-dependent with peak excitation at 360 nm and emission at 450 nm at pH 7.0. It has been previously reported that 4MU peak excitation/emission increases and fluorescence intensity decreases as pH becomes more acidic (Zhi et al., 2013). Given the pH-dependent fluorescence properties of the 4MU fluorophore, we incubate the reaction at different pH, then quench with 0.1 M Gly-NaOH pH 10.7. Quenching the reaction with 0.1 M Gly-NaOH pH 10.7 stops the enzyme reaction and shifts the pH to maximize the quantum yield of the 4MU substrate.

A Tecan Spark multimode microplate reader is pre-heated to 37 °C. 4MU-chitobioside (Sigma-Aldrich M9763) and AMCase are separately pre-incubated at 37 °C for 15 min. Twenty-five µL of 4MU-chitobioside or McIlvaine Buffer (Boston Bioproducts) is transferred into each well in a Multiplate 96-Well PCR Plate, high profile, unskirted, clear (Bio-Rad MLP9601). Using a Multidrop Combi Reagent Dispenser (Thermo Scientific #5840300), 25 µL of either 100 nM AMCase or McIlvaine Buffer (Boston Bioproducts) is dispensed into each well in the Multiplate 96-Well PCR Plate (Corning #3993). The Multiplate 96-Well PCR Plate is then incubated at 37 °C in a 96-well Non-Skirted PCR Plate Block (Thermo Scientific #88870120) in a digital dry bath (Thermo Scientific #88870006).

The reaction is quenched with 50 µL 0.1 M Gly-NaOH pH 10.7 at timepoints 0”, 15”, 30”, 45”, 60”, 90”. Forty µL of the quenched reaction is transferred to a 384-well Low Volume Black Flat Bottom Polystyrene NBS Microplate (Corning #3820), then immediately read using the following parameters:

This assay was performed in quadruplicate for each pH unit reported. This allowed us to reliably measure initial rates of catalysis across a large range of pH conditions. The workflow for this assay is illustrated in (Figure 1). A detailed protocol for this assay can be found on (protocols.io).

### Analysis of kinetic data

Twenty-five µL of 200 µM 4MU fluorophore (Sigma-Aldrich M1381) was serially diluted into 25 µL McIlvaine Buffer (Boston Bioproducts) across the range of pHs to obtain five diluted ligand concentrations ranging from 100 µM to 6.25 µM as well as ligand free. This dilution series was performed in duplicate per 96-Well PCR plate for a total of 8 replicates per ligand concentration at each given pH value. At the end of the experiment, the 4MU dilution series is quenched with 50 µL 0.1 M Gly-NaOH pH 10.7 for a final dilution series ranging from 50 µM to 3.125 µM.

Relative fluorescence (RFU) was plotted against 4MU concentration, then a simple linear regression with the constraint Y=0 when X=0 was performed to obtain a standard curve. We then used the equation Y=mX + b, where m is the slope from the standard curve and Y is the RFU from a given experimental data point, to determine the concentration of 4MU [µM] generated by AMCase at a given time point.

Average 4MU concentration [µM] (n=4) was plotted as a function of time with error bars representing the standard deviation. We then fit a simple linear regression with the constraint Y=0 when X=0 to obtain the initial rate of enzyme activity (4MU [µM]/sec) at each concentration of 4MU-chitobioside [µM]. Average initial rate (n=4) was plotted as a function of 4MU-chitobioside concentration [µM] with error bars representing the standard deviation. We fit our data to a Michaelis-Menten function without substrate inhibition to obtain Vmax and KM parameters. We used the equation kcat = Vmax/[Enzyme] where [Enzyme]=0.1 µM to calculate kcat. We calculated catalytic efficiency (CE) using the equation CE = KM/kcat. Kinetic parameters Vmax, KM, kcat, and catalytic efficiency were plotted as a function of pH.

### Apo crystallization

Using hanging-drop vapor diffusion, crystallization screens were performed using a 96-well Clear Flat Bottom Polystyrene High Binding microplate (Corning CLS9018BC) with 0.5 mL of reservoir solution in each well. Crystallization drops were set up on 96-well plate seals (SPT Labtech 4150–05100) with 0.2 µl of AMCase at 11 mg/ml and 0.2 µl of reservoir using an SPT Labtech mosquito crystal. After 21 days at 20 °C, we observed crystals in a reservoir solution containing 20% PEG-6000, 0.1 M Sodium Acetate pH 5.0, and 0.2 M Magnesium Chloride (II) (MgCl2) (NeXtal PACT Suite Well A10; #130718).

### Apo data collection, processing, and refinement at cryogenic temperature

Diffraction data were collected at the beamline ALS 8.3.1 at 100 K. Diffraction data from multiple crystals were merged using xia2 (Winter, 2010), implementing DIALS (Winter et al., 2018) for indexing and integration, and Aimless (Winn et al., 2011) for scaling and merging. We confirmed the space group assignment using DIMPLE (Wojdyr et al., 2013). We calculated phases by the method of molecular replacement, using the program Phaser (McCoy et al., 2007) and a previous structure of hAMCase (PDB: 3FXY) as the search model. The model was manually adjusted in Coot to fit the electron density map calculated from molecular replacement, followed by automated refinement of coordinates, atomic displacement parameters, and occupancies using phenix.refine (Afonine et al., 2012) with optimization of restraint weights. Default refinement parameters were used, except the fact that five refinement macrocycles were carried out per iteration and water molecules were automatically added to peaks in the 2mFo-DFc electron density map higher than 3.5 Å. The minimum model-water distance was set to 1.8 Å, and a maximum model-water distance was set to 6 Å. For later rounds of refinement, hydrogens were added to riding positions using phenix.ready_set, and B-factors were refined anisotropically for non-hydrogen and non-water atoms. Following two initial rounds of iterative model building and refinement using the aforementioned strategy, we began introducing additional parameters into the model, enabled by the extraordinarily high resolution of our diffraction data. First, we implemented anisotropic atomic displacement parameters for heavy atoms (C, N, O, and S), followed by refinement of explicit hydrogen atom positions. A final round of refinement was performed without updating water molecules.

### Apo data collection, processing, and refinement at room temperature

Diffraction data were collected at the beamline ALS 8.3.1 at 277 K. Data collection, processing, refinement, and model building were performed as described previously for the apo crystals at cryogenic temperature.

### Holo crystallization

Initially, crystals were grown by hanging-drop vapor diffusion with a reservoir solution containing 20% PEG-6000 (Hampton Research HR2533), 0.1 M Sodium Acetate (pH 3.6, Hampton Research HR293301; pH 4.1, Hampton Research HR293306; pH 5.0, Hampton Research HR293315; pH 5.6, Hampton Research HR293321), and 0.2 M Magnesium Chloride (II) (MgCl2) (Hampton Research HR2559). Screens were performed using a 96-well Clear Flat Bottom Polystyrene High Binding microplate (Corning CLS9018BC) with 0.5 mL of reservoir solution in each well. Crystallization drops were set up on 96-well plate seals (SPT Labtech 4150–05100) with 0.2 µl of AMCase at 11 mg/ml and 0.2 µl of reservoir using an SPT Labtech mosquito crystal. Crystals grew after 1–2 days at 20 °C.

Using hanging drop diffusion vapor, holo crystals grew after 12 hours at 20 °C. For the holo form with GlcNAc2 (Megazyme O-CHI2), this construct crystallized in either P21212 or P212121 with either 2 or 4 molecules in the ASU and diffracted to a maximum resolution between 1.50–1.95 Å. For the holo form with GlcNAc3 (Megazyme O-CHI3), this construct crystallized in P21212 with 2 molecules in the ASU and diffracted to a maximum resolution of 1.70 Å.

### Holo data collection, processing, and refinement at cryogenic temperature

Diffraction data were collected at the beamline ALS 8.3.1 and SSRL beamline 12–1 at 100 K. Data collection, processing, refinement, and model building were performed as described previously for the apo crystals.

Ligands were modeled into 2mFo-DFc maps with Coot, using restraints generated by phenix.elbow from an isomeric SMILES (simplified molecular input line-entry system) string (Emsley and Cowtan, 2004) using AM1 geometry optimization. Default refinement parameters were used, except the fact that five refinement macrocycles were carried out per iteration and water molecules were automatically added to peaks in the 2mFo-DFc electron density map higher than 3.5 Å. The minimum model-water distance was set to 1.8 Å, and a maximum model-water distance was set to 6 Å. Changes in protein conformation and solvation were also modeled. Hydrogens were added with phenix.ready_set, and waters were updated automatically. A final round of refinement was performed without updating water molecules (Wojdyr et al., 2013).

### Ligand modeling

For consistency, ligands were assigned an alternative conformation ID based on the sugar-binding subsites it occupied:

Ligand occupancies and B-factors using phenix.refine. Ligands with occupancies ≤0.10 were removed from the model.

### Ringer analysis

Individual residues in each of the mAMCase structures were run through Ringer using mmtbx.ringer. Outputs from the csv file were then plotted using Matplotlib.

### pKa analysis

We used the APBS-PDB2PQR software suite (https://server.poissonboltzmann.org/pdb2pqr; Jurrus et al., 2018). Each PDB model was separated into two separate models containing a single Asp138 conformation in either the inactive (down towards Asp136) or active conformation (up towards Glu140). Solvent and ligand molecules were not modified. The pH of the crystallization condition was provided for PROPKA to assign protonation states. The default forcefield PARSE was used. The following additional options were selected: Ensure that new atoms are not rebuilt too close to existing atoms; Optimize the hydrogen bonding network.

### Molecular dynamics

Simulations were performed using hexaacetyl-chitohexaose (PubChem Compound ID: 6918014) modeled into 8GCA with Asp138 in either the inactive (down towards Asp136) or active conformation (up towards Glu140). The model PDB file was opened in MOE and solvated in a sphere of water 10 Å away from the protein. This system then underwent structural preparation for simulations using the standard parameters with the AMBER14 forcefield. The system then was protonated to set pH {2.0, 6.5} based on sidechain pKa predictions using the 3DProtonate menu followed by confirmation of appropriate protonation by PROPKA calculations. Protonated models underwent energy minimization by steepest descent before simulations were set up. Equilibration was performed for 10 ps followed by 100 ps of thermal gradient equilibration from 0K to 300K. A thermal bath equilibration was run for 100 ps before the production runs were started. Productions were run for 10 ns with a time step of 0.5 fs to not overshoot bond vibrations. The simulation was sampled every 10 ps for subsequent data analysis which was performed using the MOE database viewer and replotted using GraphPad Prism.
