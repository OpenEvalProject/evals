# Effects of common mutations in the SARS-CoV-2 Spike RBD and its ligand, the human ACE2 receptor on binding affinity and kinetics

## Authors

- Michael I Barton<sup>1</sup> ([ORCID: 0000-0002-9263-6481](https://orcid.org/0000-0002-9263-6481))
- Stuart A MacGowan<sup>2</sup> ([ORCID: 0000-0003-4233-5071](https://orcid.org/0000-0003-4233-5071))
- Mikhail A Kutuzov<sup>1</sup> ([ORCID: 0000-0003-3386-4350](https://orcid.org/0000-0003-3386-4350))
- Omer Dushek<sup>1</sup> ([ORCID: 0000-0001-5847-5226](https://orcid.org/0000-0001-5847-5226))
- Geoffrey John Barton<sup>2</sup> ([ORCID: 0000-0002-9014-5355](https://orcid.org/0000-0002-9014-5355)) †
- P Anton van der Merwe<sup>1</sup> ([ORCID: 0000-0001-9902-6590](https://orcid.org/0000-0001-9902-6590)) †

### Affiliations

1. Sir William Dunn School of Pathology, University of Oxford Oxford United Kingdom
2. School of Life Sciences, University of Dundee Dundee United Kingdom

† Corresponding author

## Abstract

The interaction between the SARS-CoV-2 virus Spike protein receptor binding domain (RBD) and the ACE2 cell surface protein is required for viral infection of cells. Mutations in the RBD are present in SARS-CoV-2 variants of concern that have emerged independently worldwide. For example, the B.1.1.7 lineage has a mutation (N501Y) in its Spike RBD that enhances binding to ACE2. There are also ACE2 alleles in humans with mutations in the RBD binding site. Here we perform a detailed affinity and kinetics analysis of the effect of five common RBD mutations (K417N, K417T, N501Y, E484K, and S477N) and two common ACE2 mutations (S19P and K26R) on the RBD/ACE2 interaction. We analysed the effects of individual RBD mutations and combinations found in new SARS-CoV-2 Alpha (B.1.1.7), Beta (B.1.351), and Gamma (P1) variants. Most of these mutations increased the affinity of the RBD/ACE2 interaction. The exceptions were mutations K417N/T, which decreased the affinity. Taken together with other studies, our results suggest that the N501Y and S477N mutations enhance transmission primarily by enhancing binding, the K417N/T mutations facilitate immune escape, and the E484K mutation enhances binding and immune escape.

## Introduction

Since its identification in 2019, a coronavirus able to induce a severe acute respiratory syndrome in humans, SARS-CoV-2, has resulted in arguably the most severe infectious disease pandemic in 100 years. To date, more than 135 million people have been infected, resulting in the deaths from the resulting disease, COVID-19, of more than 3 million people (WHO, 2021), and measures introduced to control spread have had harmful social and economic impacts. Fortunately, effective vaccines have been developed, and a global vaccination programme is underway (Mahase, 2021). New SARS-CoV-2 variants of concern are emerging that are making containment of the pandemic more difficult, perhaps by increasing transmissibility of the virus (Davies et al., 2021; Korber et al., 2020; Volz et al., 2021b; Volz et al., 2021b; Washington et al., 2021) and/or its resistance to protective immunity induced by previous infection or vaccines (Darby and Hiscox, 2021; Dejnirattisai et al., 2021; Garcia-Beltran et al., 2021; Madhi et al., 2021a; Madhi et al., 2021b; Mahase, 2021; Volz et al., 2021b; Volz et al., 2021b).

The SARS-CoV-2 virus enters cells following an interaction between the Spike (S) protein on its surface with angiotensin-converting enzyme 2 (ACE2) on cell surfaces (V’kovski et al., 2021). The receptor-binding domain (RBD) of the Spike protein binds the membrane-distal portion of the ACE2 protein. The S protein forms a homotrimer, which is cleaved shortly after synthesis into two fragments that remain associated non-covalently: S1, which contains the RBD, and S2, which mediates membrane fusion following the binding of Spike to ACE2 (V’kovski et al., 2021). During the pandemic, mutations have appeared in the Spike protein that may increase transmissibility (Davies et al., 2021; Korber et al., 2020; Richard et al., 2021; Volz et al., 2021b; Volz et al., 2021b; Washington et al., 2021). One that emerged early in Europe, D614G, and quickly became dominant globally (Korber et al., 2020), increases the density of intact Spike trimer on the virus surface by preventing premature dissociation of S1 from S2 following cleavage (Zhang et al., 2021; Zhang et al., 2020). A later mutation, N501Y, which has appeared in multiple lineages, lies within the RBD, and increases its affinity for ACE2 (Starr et al., 2020; Supasa et al., 2021). These findings suggest that mutations that directly or indirectly enhance Spike binding to ACE2 may increase transmissibility.

Prior infection by SARS-CoV-2 and current vaccines induce antibody responses to the Spike protein, and most neutralising antibodies appear to bind to the Spike RBD (Garcia-Beltran et al., 2021; Greaney et al., 2021a; Rogers et al., 2020). Some variants of concern have mutations in their RBD that confer resistance to neutralising antibodies (Darby and Hiscox, 2021; Dejnirattisai et al., 2021; Garcia-Beltran et al., 2021; Madhi et al., 2021a; Madhi et al., 2021b; Mahase, 2021). What is less clear is the precise effect of these mutations on the affinity and kinetics of the binding of RBD to ACE2. Previous studies of the interaction between the Spike RBD and ACE2 have produced a wide range of affinity and kinetic estimates under conditions (e.g. temperature) that are not always well defined (Lei et al., 2020; Shang et al., 2020; Supasa et al., 2021; Wrapp et al., 2020; Zhang et al., 2021; Zhang et al., 2020). Precise information is needed to assess the extent to which RBD mutations have been selected because they enhance ACE2 binding or facilitate immune evasion.

In this study, we undertook a detailed affinity and kinetic analysis of the interaction between Spike RBD and ACE2 at a physiological temperature (37°C), taking care to avoid common pitfalls. We used this optimised approach to analyse the effect of important common mutations identified in variants of RBD and ACE2. Both mutations of ACE2 (S19P, K26R) and most of the mutations of RBD (N501Y, E484K, and S477N) enhanced the interaction, with one RBD mutation (N501Y) increasing the affinity by ~10-fold. Increased binding was the result of decreases in dissociation rate constants (N501Y, S477N) and/or increases in association rate constants (N501Y, E484K). Although the K417N/T mutations found in the South African (B.1.351) and Brazilian (P.1) variants both decreased the affinity, the affinity-enhancing N501Y and E484K mutations that are also present in both variants confer a net ~4-fold increase in the affinity of their RBDs for ACE2.

## Results

### Selection of variants

The focus of this study was to analyse common and therefore important variants of RBD and ACE2. Henceforth, we will refer to the common ACE2 allele and RBD of the original SARS-CoV-2 strain sequenced in Wuhan as wild type (WT). We chose mutations of RBD within the ACE2 binding site that have appeared independently in multiple SARS-CoV-2 lineages/clades (Figure 1, Figure 1—figure supplement 1; Hodcroft, 2021; Rambaut et al., 2020), suggesting that they confer a selective advantage, rather than emerged by chance, such as through a founder effect. The N501Y mutation has appeared in the Alpha (B.1.1.7; 20I/501Y.V1), Beta (B.1.351; 20 H/501Y.V2), and Gamma (P.1; 20 J/501Y.V3) variants, which were first identified in the UK, South Africa, and Brazil, respectively. The E484K mutation is present in the Beta and Gamma variants and has appeared independently in many other lineages, including Zeta (P.2; 20B/S.484K), B.1.1.318, Eta (B.1.525; 20A/S:484 K), and Iota (B.1.526; 20 C/S.484K). E484K has also appeared in VOC-202102–02, a subset of the Alpha variant identified in the UK (SARS-CoV-2 Variants of concern and variants under investigation - GOV.UK, 2021). The S477N mutation became dominant for periods in Australia (clade 20 F) and parts of Europe (20A.EU2) and then appeared in New York in the Iota or B.1.526 lineage (Zhou et al., 2021a). Mutations of K417 have appeared independently in the Beta and Gamma variants. Interestingly, N501Y, E484K, and S477N were the main mutations that appeared following random RBD mutagenesis and in vitro selection of mutants with enhanced ACE2 binding (Zahradník et al., 2021).

![Figure 1.](https://cdn.elifesciences.org/articles/70658/elife-70658-fig1-v3.jpg)

**Figure 1.:** (A) Phylogenetic tree illustrating the clades containing the RBD mutations investigated in this study. Constructed using TreeTime (Sagulenko et al., 2018) from the Nextstrain Global (Hadfield et al., 2018) sample of SARS-CoV-2 sequences from the GISAID database (Shu and McCauley, 2017) (accessed 15 April 2021, N = 4017). (B) Alignment illustrating the Spike residues that differ between SARS-CoV-2 variants, with the RBD mutants boxed. The variants are labelled with their clade designation from Nextstrain (Hadfield et al., 2018) and/or PANGO lineage (Rambaut et al., 2020), where relevant. The RBD mutations were collated from CoVariants (Hodcroft, 2021) and Nextstrain. (C) The structure of human ACE2 (green) in complex with SARS-CoV-2 Spike RBD (cyan). The area enclosed by the box is shown enlarged on the right, with the residues mutated in this study labelled. Drawn using UCSF Chimera (Pettersen et al., 2004) using coordinates from PDB 6m0j (Lan et al., 2020).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/70658/elife-70658-fig1-figsupp1-v3.jpg)

**Figure 1—figure supplement 1.:** The figure highlights the SARS-CoV-2 clades containing RBD mutations investigated in this study. The phylogenetic trees were constructed as in Figure 1A from SARS-CoV-2 sequences accessed on 22 April 2021 (N = 3914). (A) N501Y has emerged independently in the three clades 501Y.V1, 501Y.V2, and 501Y.V3. Mutation to T at this position has also occurred frequently. (B) E484K has also been observed independently of its main progenitor clades 501Y.V2 and 501Y.V3. E484Q and E484G have also been observed. (C) S477N has been observed beyond clades 20 F and 20A.EU2. Mutations to I and R have also been occasionally observed at this position. (D) Mutations of K417 to N and T have been observed almost exclusively in the 20 H.501Y.V2 and 20 J.501Y.V3 clades.

We selected for analysis the two most common mutations of ACE2 within the RBD binding site, K26R and S19P (Figure 1C). They are present in 0.4% and 0.03%, respectively, of all samples in the gnomAD database (Karczewski et al., 2020), while other ACE2 mutations in the RBD binding site are much less frequent (<0.004%) (MacGowan et al., 2021). K26R is observed in all the major gnomAD populations but is most common in Ashkenazi Jews (1%) and (non-Finnish) north-western Europeans (0.6%). It is less common in Africans/African-Americans and South Asians (0.1%) and rare in Finnish (0.05%) and East-Asian (0.001%) populations. The S19P mutant is almost exclusively found in Africans/African-Americans (0.3%).

### Measurement of affinity and kinetics

To measure the effects of these mutations on the affinity and kinetics of the RBD/ACE2 interaction, we used surface plasmon resonance (SPR), which allows very accurate measurements, provided that common pitfalls are avoided, particularly protein aggregation, mass-transport limitations, and rebinding (van der Merwe and Barclay, 1996; Myszka, 1997). Monomeric, soluble forms of the ectodomain of ACE2 and the Spike RBD were expressed in human cells, to retain native glycosylation, and purified (Figure 2—figure supplement 1). ACE2 was captured onto the sensor surface via a carboxy-terminal biotin and RBD injected over ACE2 at different concentrations (Figure 2A). Excellent fits of 1:1 Langmuir binding model to the data yielded an association rate constant (kon) of 0.9 ± 0.05 μM–1s–1 and a dissociation rate constant (koff) of 0.067 ± 0.0011 s–1 (mean ± SD, n = 6, Table 1). These rate constants are up to 25- fold faster than previously reported for the same interaction (Lei et al., 2020; Shang et al., 2020; Supasa et al., 2021; Wrapp et al., 2020; Zhang et al., 2021). However, previous experiments were conducted at unphysiologically low temperatures (i.e. below 37°C) and under conditions in which mass-transport limitations and rebinding are highly likely (see Discussion). These factors, and the presence of protein aggregates (van der Merwe and Barclay, 1996), would all lower the measured rate constants. In contrast, our measurements were conducted at 37°C and under conditions in which mass-transfer limitation and rebinding were excluded. The latter is demonstrated by the fact that measured kon and koff rates approached maximal values at the low level of ACE2 immobilisation (~50 RU) used in our experiments (Figure 2B,C; Dejnirattisai et al., 2021). The excellent fit of the 1:1 binding model to our data excludes an effect of protein aggregates, which yield complex kinetics. The calculated dissociation constant (KD) was 74 ± 4 nM (mean ± SD, n = 6, Table 1). We also measured KD by equilibrium binding (Figure 2D), which avoids any artefacts induced by mass transfer limitations and rebinding. This KD was very similar to the value calculated from kinetic data (63 ± 7.7 nM [mean ± SD, n = 24, Table 1]), and did not vary with immobilisation level (Figure 2E), further validating our kinetic measurements. These affinity values are within the wide range reported in previous studies, which varied from KD 6–133 nM (Laffeber et al., 2021; Lei et al., 2020; Liu et al., 2021; Shang et al., 2020; Supasa et al., 2021; Wrapp et al., 2020; Zhang et al., 2021).

![Figure 2.](https://cdn.elifesciences.org/articles/70658/elife-70658-fig2-v3.jpg)

**Figure 2.:** (A) Overlay of traces showing association and dissociation when WT RBD is injected for 30 s at the indicated concentration over immobilised WT ACE2. The right panel shows an expanded view of the dissociation phase. The blue lines show the fits used for determining the kon and koff. The kon was determined as described in Figure 2—figure supplement 2. The koff (B) and kon (C) values measured at different levels of immobilised ACE2 are shown. (D) The equilibrium KD was determined by plotting the binding at equilibrium against [RBD] injected. Data from experiment shown in (A). (E) The equilibrium KD measured at different levels of immobilised ACE2 are shown.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/70658/elife-70658-fig2-figsupp1-v3.jpg)

**Figure 2—figure supplement 1.:** Size-exclusion chromatography traces of the indicated ACE2 and RBD proteins and reducing SDS–PAGE of the indicated peak fractions. UK2 refers to the VOC-202102–02 variants. In preparations of RBD, unidentified ~60 kDa contaminants were present at various levels, but always <5% by densitometry.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/70658/elife-70658-fig2-figsupp2-v3.jpg)

**Figure 2—figure supplement 2.:** Analysis of data from the fits in Figure 2A. (A) A plot of koff obtained for each injection versus [RBD]. (B) A plot of kobs for each injection versus [RBD]. The line shows a constrained fit of the equation kobs = kon*[RBD]+ koff, using the koff obtained in (A). The kon was obtained from the slope.

**Table 1.**
 Affinity and kinetic data for RBD variants and ACE2 variants.Mean and SD of the koff, kon, calculated KD, and equilibrium KD values for all RBD variants binding all ACE2 variants. For most measurements n = 3, the exceptions were RBD WT/ACE2 WT equilibrium KD measurements (n = 24) and other RBD WT measurements (n = 6). UK2 refers to the VOC-202102–02 variant.


<table>
  <thead>
    <tr>
      <th></th>
      <th>koff (s–1)</th>
      <th>SD</th>
      <th>kon (µM–1 s–1)</th>
      <th>SD</th>
      <th>KD calc. (nM)</th>
      <th>SD</th>
      <th>KD equi. (nM)</th>
      <th>SD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>RBD over WT ACE2</td>
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
      <td>WT</td>
      <td>0.0668</td>
      <td>0.00113</td>
      <td>0.90</td>
      <td>0.05</td>
      <td>74.4</td>
      <td>4.0</td>
      <td>62.6</td>
      <td>7.7</td>
    </tr>
    <tr>
      <td>K417N</td>
      <td>0.177</td>
      <td>0.00416</td>
      <td>0.49</td>
      <td>0.05</td>
      <td>364</td>
      <td>29</td>
      <td>349</td>
      <td>10</td>
    </tr>
    <tr>
      <td>K417T</td>
      <td>0.126</td>
      <td>0.00510</td>
      <td>0.55</td>
      <td>0.04</td>
      <td>230</td>
      <td>23</td>
      <td>226</td>
      <td>19</td>
    </tr>
    <tr>
      <td>S477N</td>
      <td>0.0348</td>
      <td>0.00037</td>
      <td>0.81</td>
      <td>0.03</td>
      <td>42.9</td>
      <td>2.1</td>
      <td>42.6</td>
      <td>3.0</td>
    </tr>
    <tr>
      <td>E484K</td>
      <td>0.0818</td>
      <td>0.00183</td>
      <td>1.54</td>
      <td>0.03</td>
      <td>53.1</td>
      <td>1.7</td>
      <td>52.6</td>
      <td>2.0</td>
    </tr>
    <tr>
      <td>N501Y (Alpha)</td>
      <td>0.0111</td>
      <td>0.00017</td>
      <td>1.59</td>
      <td>0.04</td>
      <td>7.0</td>
      <td>0.25</td>
      <td>5.5</td>
      <td>2.4</td>
    </tr>
    <tr>
      <td>K417N/E484K</td>
      <td>0.251</td>
      <td>0.00799</td>
      <td>1.02</td>
      <td>0.07</td>
      <td>247</td>
      <td>23</td>
      <td>251</td>
      <td>23</td>
    </tr>
    <tr>
      <td>K417T/E484K</td>
      <td>0.168</td>
      <td>0.00573</td>
      <td>1.10</td>
      <td>0.05</td>
      <td>153</td>
      <td>12</td>
      <td>147</td>
      <td>8.6</td>
    </tr>
    <tr>
      <td>E484K/N501Y (UK2)</td>
      <td>0.0118</td>
      <td>0.00037</td>
      <td>2.33</td>
      <td>0.10</td>
      <td>5.1</td>
      <td>0.36</td>
      <td>3.7</td>
      <td>2.7</td>
    </tr>
    <tr>
      <td>K417N/E484K/N501Y (Beta)</td>
      <td>0.0291</td>
      <td>0.00076</td>
      <td>1.46</td>
      <td>0.06</td>
      <td>20.0</td>
      <td>0.70</td>
      <td>17.4</td>
      <td>3.1</td>
    </tr>
    <tr>
      <td>K417T/E484K/N501Y (Gamma)</td>
      <td>0.0211</td>
      <td>0.00021</td>
      <td>1.56</td>
      <td>0.07</td>
      <td>13.5</td>
      <td>0.45</td>
      <td>12.2</td>
      <td>3.4</td>
    </tr>
    <tr>
      <td>RBD over S19P ACE2</td>
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
      <td>WT</td>
      <td>0.0298</td>
      <td>0.00039</td>
      <td>1.50</td>
      <td>0.12</td>
      <td>20.0</td>
      <td>1.3</td>
      <td>30.5</td>
      <td>2.2</td>
    </tr>
    <tr>
      <td>K417N</td>
      <td>0.0782</td>
      <td>0.00284</td>
      <td>0.72</td>
      <td>0.04</td>
      <td>108</td>
      <td>2.8</td>
      <td>129</td>
      <td>8.2</td>
    </tr>
    <tr>
      <td>K417T</td>
      <td>0.0521</td>
      <td>0.00196</td>
      <td>0.69</td>
      <td>0.02</td>
      <td>75.8</td>
      <td>4.7</td>
      <td>87.8</td>
      <td>7.0</td>
    </tr>
    <tr>
      <td>S477N</td>
      <td>0.0257</td>
      <td>0.00016</td>
      <td>1.05</td>
      <td>0.07</td>
      <td>24.6</td>
      <td>1.7</td>
      <td>30.3</td>
      <td>2.7</td>
    </tr>
    <tr>
      <td>E484K</td>
      <td>0.0325</td>
      <td>0.00031</td>
      <td>2.02</td>
      <td>0.08</td>
      <td>16.2</td>
      <td>0.55</td>
      <td>20.8</td>
      <td>1.3</td>
    </tr>
    <tr>
      <td>N501Y (Alpha)</td>
      <td>0.0051</td>
      <td>0.00004</td>
      <td>2.31</td>
      <td>0.09</td>
      <td>2.2</td>
      <td>0.09</td>
      <td>3.5</td>
      <td>0.4</td>
    </tr>
    <tr>
      <td>K417N/E484K</td>
      <td>0.0961</td>
      <td>0.00198</td>
      <td>1.28</td>
      <td>0.11</td>
      <td>75.6</td>
      <td>7.1</td>
      <td>91.3</td>
      <td>6.5</td>
    </tr>
    <tr>
      <td>K417T/E484K</td>
      <td>0.0660</td>
      <td>0.00255</td>
      <td>1.45</td>
      <td>0.03</td>
      <td>45.5</td>
      <td>2.5</td>
      <td>53.8</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td>E484K/N501Y (UK2)</td>
      <td>0.0051</td>
      <td>0.00008</td>
      <td>3.10</td>
      <td>0.10</td>
      <td>1.7</td>
      <td>0.05</td>
      <td>3.4</td>
      <td>0.4</td>
    </tr>
    <tr>
      <td>K417N/E484K/N501Y (Beta)</td>
      <td>0.0122</td>
      <td>0.00009</td>
      <td>2.16</td>
      <td>0.03</td>
      <td>5.7</td>
      <td>0.07</td>
      <td>10.4</td>
      <td>1.2</td>
    </tr>
    <tr>
      <td>K417T/E484K/N501Y (Gamma)</td>
      <td>0.0085</td>
      <td>0.00007</td>
      <td>2.11</td>
      <td>0.05</td>
      <td>4.0</td>
      <td>0.07</td>
      <td>6.1</td>
      <td>1.3</td>
    </tr>
    <tr>
      <td>RBD over K26R ACE2</td>
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
      <td>S477N</td>
      <td>0.0240</td>
      <td>0.00009</td>
      <td>1.07</td>
      <td>0.05</td>
      <td>22.6</td>
      <td>1.1</td>
      <td>33.4</td>
      <td>1.3</td>
    </tr>
    <tr>
      <td>WT</td>
      <td>0.0500</td>
      <td>0.00062</td>
      <td>1.60</td>
      <td>0.16</td>
      <td>31.4</td>
      <td>2.6</td>
      <td>48.8</td>
      <td>2.5</td>
    </tr>
    <tr>
      <td>K417N</td>
      <td>0.154</td>
      <td>0.00789</td>
      <td>0.88</td>
      <td>0.07</td>
      <td>175</td>
      <td>8.1</td>
      <td>237</td>
      <td>15</td>
    </tr>
    <tr>
      <td>K417T</td>
      <td>0.101</td>
      <td>0.00079</td>
      <td>0.81</td>
      <td>0.12</td>
      <td>127</td>
      <td>17.4</td>
      <td>154</td>
      <td>2.8</td>
    </tr>
    <tr>
      <td>S477N</td>
      <td>0.0240</td>
      <td>0.00009</td>
      <td>1.07</td>
      <td>0.05</td>
      <td>22.6</td>
      <td>1.1</td>
      <td>33.4</td>
      <td>1.3</td>
    </tr>
    <tr>
      <td>E484K</td>
      <td>0.0587</td>
      <td>0.00109</td>
      <td>2.03</td>
      <td>0.03</td>
      <td>28.9</td>
      <td>1.0</td>
      <td>35.9</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td>N501Y (Alpha)</td>
      <td>0.0081</td>
      <td>0.00002</td>
      <td>2.34</td>
      <td>0.09</td>
      <td>3.5</td>
      <td>0.15</td>
      <td>7.5</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td>K417N/E484K</td>
      <td>0.191</td>
      <td>0.00481</td>
      <td>1.48</td>
      <td>0.15</td>
      <td>130</td>
      <td>9.4</td>
      <td>166</td>
      <td>11</td>
    </tr>
    <tr>
      <td>K417T/E484K</td>
      <td>0.135</td>
      <td>0.00407</td>
      <td>1.53</td>
      <td>0.02</td>
      <td>88.0</td>
      <td>3.9</td>
      <td>105</td>
      <td>0.7</td>
    </tr>
    <tr>
      <td>E484K/N501Y (UK2)</td>
      <td>0.0085</td>
      <td>0.00018</td>
      <td>3.06</td>
      <td>0.23</td>
      <td>2.8</td>
      <td>0.17</td>
      <td>6.4</td>
      <td>0.3</td>
    </tr>
    <tr>
      <td>K417N/E484K/N501Y (Beta)</td>
      <td>0.0234</td>
      <td>0.00040</td>
      <td>2.13</td>
      <td>0.05</td>
      <td>11.0</td>
      <td>0.28</td>
      <td>18.7</td>
      <td>2.0</td>
    </tr>
    <tr>
      <td>K417T/E484K/N501Y (Gamma)</td>
      <td>0.0164</td>
      <td>0.00028</td>
      <td>2.21</td>
      <td>0.06</td>
      <td>7.4</td>
      <td>0.33</td>
      <td>15.3</td>
      <td>0.8</td>
    </tr>
  </tbody>
</table>

### The effect of RBD mutations

We next evaluated the effect of RBD mutations on the affinity and kinetics of binding to ACE2 (Figure 3 and Table 1). Example sensorgrams are shown of mutations that increased (N501Y, Figure 3A) or decreased (K417N, Figure 3B) the binding affinity, while the key results from all mutants are summarised in Figure 3C. The single mutations S477N, E484K, and N501Y all enhanced binding. The N501Y mutation had the biggest effect, increasing the affinity ~10 fold to KD ~7 nM, by increasing the kon ~1.8-fold and decreasing the koff by ~7-fold. The S477N and E484K mutations increased the affinity more modestly (~1.5-fold), by decreasing the koff (S477N) or increasing the kon (E484K). The K417T and K417N mutations decreased the affinity ~2- and ~ 4-fold, respectively, mainly by decreasing the kon but also by increasing the koff. Affinity-altering mutations in binding sites mainly affect the koff (Agius et al., 2013) and have more modest effects on the kon. Changes in electrostatic interactions can dramatically affect the kon (Schreiber and Fersht, 1996) and are a plausible explanation for the effects of the mutations K417T, K417N, and E484K on kon. K417 forms a salt bridge with D30 on ACE2 (Lan et al., 2020), while E484 is ~9 Å from E75 on ACE2 (Lan et al., 2020). Thus, the mutations K417N/T and E484K would decrease and increase, respectively, long-range electrostatic forces that may accelerate association (Schreiber and Fersht, 1996).

![Figure 3.](https://cdn.elifesciences.org/articles/70658/elife-70658-fig3-v3.jpg)

**Figure 3.:** Overlay of traces showing association and dissociation of N501Y (A) and K417N (B) RBD variants when injected at a range of concentrations over immobilised WT ACE2. The right panels show an expanded view of the dissociation phase. The blue lines show fits used for determining the kon and koff. (C) The fold change relative to WT RBD of the calculated KD, kon, and koff for binding of the indicated RBD variants to immobilised WT ACE2 (error bars show SD, n = 3). Representative sensorgrams from all mutants shown in Figure 3—figure supplement 2, and the mean values from multiple repeats are in Table 1. (D) The blue lines show the measured ΔΔG for indicated RBD variants. The red lines show the predicted ΔΔG for the RBD variants with multiple mutations, which were calculated by adding ΔΔG values for single mutation variants (error bars show SD, n = 3).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/70658/elife-70658-fig3-figsupp1-v3.jpg)

**Figure 3—figure supplement 1.:** The koff (A) and kon (B) for E484K/N501Y (UK2) RBD binding WT ACE2 at a range of surface immobilisations (n = 12). UK2 refers to VOC-202102–02.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/70658/elife-70658-fig3-figsupp2-v3.jpg)

**Figure 3—figure supplement 2.:** Binding traces for the indicated RBD variants injected at different concentrations over immobilised WT ACE2. The right panels show an expanded view of the dissociation phase. The blue lines show fits used for determining the kon and koff. UK2 refers to the VOC-202102–02 variant.

We also examined the effect on ACE2 binding of combinations of RBD mutations, including combinations present in VOC-202102–02, a subset of the Alpha lineage (N501Y) with the E484K mutation (“SARS-CoV-2 Variants of concern and variants under investigation – GOV.UK,” 2021), and the Beta and Gamma variants (Figure 3C, Table 1). In the case of VOC-202102–02, the addition of the E484K mutation to N501Y further increased the affinity, to ~15-fold higher than WT RBD (KD ~5 nM), by further increasing the kon. Because the higher kon could result in mass transfer limiting binding, we confirmed that the kinetic measurement for this variant was not substantially affected by varying levels of immobilisation (Figure 3—figure supplement 1). The affinity of the Beta (K417N/ E484K/N501Y) and Gamma (K417T/E484K/N501Y) RBD variants for ACE2 increased by 3.7- and 5.3-fold, respectively, relative to wild-type RBD, by both increasing the kon and decreasing the koff rate constants.

We next examined whether the effects of the mutations were additive, as is typically the case for multiple mutations at protein/protein interfaces (Wells, 1990). To do this, we converted the changes in KD to changes in binding energy (ΔΔG, Table 2) and examined whether the ΔΔG measured for RBD variants with multiple mutations was equal to the sum of the ΔΔG values measured for the individual RBD mutants. This was indeed the case (Figure 3D), indicating that the effects on each mutation are independent. This is consistent with them being spaced well apart within the interface (Figure 1C) and validates the accuracy of the affinity measurements.

**Table 2.**
 ΔΔG for RBD variants binding to ACE2 variants.Mean and SD of ΔΔG (n = 3, kcal/mol) were determined as described in Materials and methods using the calculated KD values in Table 1. UK2 refers to the VOC-202102–02 variant.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Ace2 wt</th>
      <th></th>
      <th>Ace2 s19p</th>
      <th></th>
      <th>Ace2 k26r</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>RBD variant</td>
      <td>ΔΔG</td>
      <td>SD</td>
      <td>ΔΔG</td>
      <td>SD</td>
      <td>ΔΔG</td>
      <td>SD</td>
    </tr>
    <tr>
      <td>WT</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.79</td>
      <td>0.05</td>
      <td>0.52</td>
      <td>0.06</td>
    </tr>
    <tr>
      <td>K417N</td>
      <td>–0.96</td>
      <td>0.06</td>
      <td>–0.23</td>
      <td>0.04</td>
      <td>–0.52</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td>K417T</td>
      <td>–0.68</td>
      <td>0.07</td>
      <td>–0.01</td>
      <td>0.05</td>
      <td>–0.32</td>
      <td>0.09</td>
    </tr>
    <tr>
      <td>S477N</td>
      <td>0.33</td>
      <td>0.04</td>
      <td>0.67</td>
      <td>0.05</td>
      <td>0.72</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td>E484K</td>
      <td>0.20</td>
      <td>0.04</td>
      <td>0.92</td>
      <td>0.04</td>
      <td>0.57</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td>N501Y (Alpha)</td>
      <td>1.43</td>
      <td>0.04</td>
      <td>2.13</td>
      <td>0.04</td>
      <td>1.86</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td>K417N/E484K</td>
      <td>–0.72</td>
      <td>0.07</td>
      <td>–0.01</td>
      <td>0.07</td>
      <td>–0.34</td>
      <td>0.06</td>
    </tr>
    <tr>
      <td>K417T/E484K</td>
      <td>–0.43</td>
      <td>0.06</td>
      <td>0.30</td>
      <td>0.05</td>
      <td>–0.10</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td>E484K/N501Y (UK2)</td>
      <td>1.62</td>
      <td>0.05</td>
      <td>2.30</td>
      <td>0.04</td>
      <td>1.98</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td>K417N/E484K/N501Y (Beta)</td>
      <td>0.79</td>
      <td>0.04</td>
      <td>1.56</td>
      <td>0.03</td>
      <td>1.16</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td>K417T/E484K/N501Y (Gamma)</td>
      <td>1.03</td>
      <td>0.04</td>
      <td>1.76</td>
      <td>0.03</td>
      <td>1.39</td>
      <td>0.04</td>
    </tr>
  </tbody>
</table>

### The effects of ACE2 mutations

We next examined the effects of mutations of ACE2 (S19P and K26R) on binding to both wild-type and common variants of RBD (Figure 4, Figure 4—figure supplement 1, and Table 1). Both S19P and K26R increased the affinity of WT RBD binding by ~3.7- and ~ 2.4-fold (Figure 4A). These increases in affinity were the result of both increases in the kon and decreases in the koff.

![Figure 4.](https://cdn.elifesciences.org/articles/70658/elife-70658-fig4-v3.jpg)

**Figure 4.:** (A) The fold change relative to WT ACE2 of the calculated KD, kon, and koff for the interaction of WT RBD and the indicated ACE2 variants (error bars show SD, n = 3). (B, C) Show the difference (ΔΔΔG) between the measured and predicted ΔΔG for S19P (B) and K26R (C) ACE2 variants binding to the indicated RBD variants, calculated from data in Table 2. The predicted ΔΔG values for each variant RBD/variant ACE2 interaction were calculated from the sum of the ΔΔG for the ACE2 variant binding WT RBD and the ΔΔG for the RBD variant binding WT ACE2 (Table 2).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/70658/elife-70658-fig4-figsupp1-v3.jpg)

**Figure 4—figure supplement 1.:** Binding traces for the WT RBD injected at different concentrations over the indicated immobilised ACE2 variants. The right panels show an expanded view of the dissociation phase. The blue lines show fits used for determining the kon and koff.

Finally, we looked for interactions between RBD and ACE2 mutations by measuring the effects of the ACE2 mutations on binding to all mutant forms of RBD (Table 1). After converting changes in KD to ΔΔG (Table 2), we examined whether ΔΔG measured for a given ACE2 variant/RBD variant interaction was equal to the sum of the ΔΔG measured for ACE2 variant/RBD WT and ACE WT/RBD variant interactions. This is depicted as the difference between the measured and predicted ΔΔG for interactions between ACE2 and RBD variants (ΔΔΔG in Figure 4B,C, Dejnirattisai et al., 2021). In most cases, ΔΔΔG values were close to zero, indicating that the effects of these mutations were largely independent. The one exception was the combination of ACE2 S19P and RBD S477N variants, where the measured value was significantly lower than the predicted value (Figure 4B), indicating that these mutations were not independent. This is consistent with the fact that the ACE2 residue S19 is adjacent to RBD residue S477 in the contact interface (Figure 1C). An important consequence of this is that the S477N mutation increased the affinity of RBD for ACE2 WT but decreased its affinity for ACE2 S19P.

## Discussion

While our finding that the SARS-CoV-2 RBD binds ACE2 with an affinity of KD 74 nM at 37°C is consistent with previous studies (KD 6–133 nM) (Laffeber et al., 2021; Lei et al., 2020; Liu et al., 2021; Shang et al., 2020; Supasa et al., 2021; Wrapp et al., 2020; Zhang et al., 2021; Zhang et al., 2020), the rate constants that we measured (kon 0.9 μM–1.s–1 and koff 0.067 s–1) were faster than all previous reports. One likely reason for this is that previous measurements were performed at a lower temperature, which almost always decreases rate constants. While some studies stated that binding constants were measured at 25°C (Laffeber et al., 2021; Zhang et al., 2020), most studies did not report the temperature, suggesting that they were performed at room temperature or the standard instrument temperature (20°C–25°C). A second likely reason is that previous kinetic studies were performed under conditions in which the rate of diffusion of soluble molecule to the sensor surface limits the association rate, and rebinding of dissociated molecules to the surface reduces the measured dissociation rate. These are known pitfalls of both techniques used in these studies, surface plasmon resonance (Myszka, 1997), and bilayer interferometry (Abdiche et al., 2008). In the present study, we avoided these issues by immobilising a very low level of ligand on the sensor surface. A third possible reason is that the proteins were aggregated, which can cause problems even when aggregates are a very minor contaminant (van der Merwe and Barclay, 1996). The presence of aggregates results in complex binding kinetics, which can be excluded if the simple 1:1 Langmuir binding model fits the kinetic data. While this was demonstrated in the present study, and some previous studies (Shang et al., 2020; Wrapp et al., 2020; Zhang et al., 2021), such fits were not shown in all studies, one of which reported more than 20-fold slower kinetics than reported here (Lei et al., 2020; Supasa et al., 2021).

The RBD mutations that we selected for analysis have all emerged independently and became dominant in a region at least once in different lineages, suggesting that they provide a selective advantage. Our finding that the N501Y, E484K, and S477N all increase the binding affinity of RBD for ACE2 raises the question as to whether this contributed to their selection. Several lines of evidence suggest that enhancing the Spike/ACE2 interaction would be advantageous for the virus. First, the virus has spread only very recently to humans from another mammalian host, providing insufficient time for optimisation of the affinity. Second, epidemiological studies have suggested that the Alpha variant, which has the N501Y mutation, has enhanced transmissibility (Volz et al., 2021a; Washington et al., 2021). Finally, a SARS-CoV-2 variant with the Spike mutation D614G, which increases its activity by stabilising it following furin cleavage (Zhang et al., 2021; Zhang et al., 2020), rapidly became dominant globally after it emerged (Korber et al., 2020; Volz et al., 2021b). Taken together, these findings suggest that the WT Spike/ACE2 interaction is limiting for transmission and that mutations that enhance it, including the N501Y, E484K, and S477N mutations, could provide a selective advantage by increasing transmissibility. This raises two questions. First, will other RBD mutations appear in SARS-CoV-2 which further enhance transmission? This seems likely, given that a large number of RBD mutations have been identified that increase the RBD/ACE2 affinity (Starr et al., 2020; Zahradník et al., 2021). Second, will combinations of existing mutations be selected because they further increase the affinity? While the appearance E484K, together with N501Y in three lineages (Alpha, Beta, and Gamma), supports this, it is also possible that E484K was selected because it disrupts antibody neutraliaation, as discussed below.

Our affinity and kinetic data on RBD variants are broadly consistent with some (Laffeber et al., 2021; Liu et al., 2021), but not all (Dejnirattisai et al., 2021; Zhou et al., 2021a), recent reports on the K417T/N, N501Y, and E484K variants. One caveat to our study is that we used monomeric forms of RBD and ACE2. The native Spike protein is a trimer and has several other domains, including the nearby N-teminal domain, and the native ACE2 protein can exist as a dimer (Yan et al., 2020). Because of these differences, our analysis may not detect the full effects of RBD and ACE2 mutations on the Spike/ACE2 interaction. A second caveat is that we have not examined the effect of these mutations on viral attachment to cells.

Studies of other enveloped viruses, including SARS-CoV, suggest that increases in affinity of viral ligands for their cellular receptors can increase cell infection and disease severity (Hasegawa et al., 2007; Li et al., 2005). One study found that increasing this affinity enabled the virus to infect cells with lower receptor surface density (Hasegawa et al., 2007). It follows that increases in affinity could increase the number of host tissues infected, which could increase the severity of disease (Cao and Li, 2020) and/or increase the viral load in the upper respiratory tract (Hoffmann et al., 2020; Wölfel et al., 2020), thereby increasing spread.

Another mechanism by which mutations of RBD could provide a selective advantage is through evasion of immune responses. This is supported by the observation that neutralising antibodies present in those infected by or vaccinated against SARS-CoV-2 primarily target the RBD (Garcia-Beltran et al., 2021; Greaney et al., 2021a; Rogers et al., 2020). Furthermore, two variants with RBD mutations that abrogate antibody neutralisation, Beta and Gamma, became dominant in regions with very high levels of prior SARS-CoV-2 infection (Cele et al., 2021; Dejnirattisai et al., 2021; Hoffmann et al., 2021; Sabino et al., 2021; Tegally et al., 2021; Zhou et al., 2021b). Both lineages include the N501Y mutation, but this appears to have modest effects on antibody neutralisation (Greaney et al., 2021a; Greaney et al., 2021b). In contrast, the E484K mutation, also present in both variants, potently disrupts antibody neutralisation (Greaney et al., 2021a; Greaney et al., 2021b). Our finding that the K417N/T mutations present in Beta and Gamma variants decrease the affinity of RBD for ACE2 suggests that they were selected because they facilitate immune escape. Indeed, mutations of K417 can block antibody neutralisation, albeit less effectively than E484K (Greaney et al., 2021a; Greaney et al., 2021b; Wang et al., 2021). It is notable that these affinity-reducing K417N/T mutations have only emerged together with mutations (N501Y and E484K) that increase the affinity of RBD for ACE2, suggesting a cooperative effect between mutations that enhance immune escape and mutations that increase affinity.

The effect of the increased affinity for SARS-CoV-2 Spike RBD of the K26R and S19P ACE2 mutants is less clear. The evidence summarised above that WT RBD/ACE2 binding is limiting for SARS-CoV-2 transmission, suggest that carriers of these ACE2 variants will be at greater risk of infection and/or severe disease. However, in contrast to SARS-CoV-2 RBD mutations, the effects of ACE2 variants are primarily relevant to the carriers of these mutations. A preliminary analysis (MacGowan et al., 2021) suggests that the carriers of the K26R ACE allele might be at increased risk of severe disease, but the findings did not reach statistical significance, and further studies are required.

The interaction that we identified between the RBD S477N and ACE2 S19P mutants highlights the importance of considering variation in the host population when studying the evolution of viral variants. In this case, the opposite effect of the RBD S477N mutation on its affinity for ACE2 S19P (decreased), compared with ACE2 WT (increased), suggests that this RBD variant may have a selective disadvantage amongst carriers of the ACE2 S19P variant, in contrast to those with ACE2 WT, where it appears to be advantageous. However, the low frequency of this variant means that this is unlikely to be important at a population level and will be difficult to detect.

It is noteworthy that the two most common ACE2 variants are in positions on ACE2 with no known functional activity. This raises the question as to whether these mutations are a remnant of historic adaption to pathogens that utilised this portion of ACE2. The fact that ACE2 S19P mutation is largely confined to African/African-American populations, suggests that it is more recent than K26R and/or selected by pathogen(s) confined to the African continent.

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
      <td>Transfected construct (human)</td>
      <td>ACE2 WT</td>
      <td>Oxford Protein Production Facility-UK</td>
      <td>pOPINTTGneo_ACE2-BAP</td>
      <td>T</td>
    </tr>
    <tr>
      <td>Transfected construct (human)</td>
      <td>ACE2 S19P; ACE2 K26R</td>
      <td>This paper</td>
      <td></td>
      <td>Available from authors</td>
    </tr>
    <tr>
      <td>Transfected construct (SARS-CoV-2)</td>
      <td>RBD WT</td>
      <td>BEI Resources, NIH</td>
      <td>NR-52309</td>
      <td>pCAGG plasmid</td>
    </tr>
    <tr>
      <td>Transfected construct (SARS-CoV-2)</td>
      <td>RBD K417N; RBD RBD K417T; RBD S477N; RBD E484K; RBD N501Y; RBD K417N/E484K; RBD K417T/E484K; RBD beta; RBD gamma</td>
      <td>This paper</td>
      <td></td>
      <td>pCAGG plasmid. Available from authors</td>
    </tr>
    <tr>
      <td>Transfected construct (human)</td>
      <td>pTT3-BirA-FLAG</td>
      <td>Addgene</td>
      <td>RRID:Addgene_64395</td>
      <td>Cotranfected for in-cell biotinylation</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>ACE2 WT; ACE2 S19P; ACE2 K26R</td>
      <td>This paper</td>
      <td></td>
      <td>Expressed in HEK293 cells and purified</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>RBD WT; RBD K417N; RBD K417T; RBD S477N; RBD E484K; RBD N501Y; RBD K417N/E484K; RBD K417T/E484K; RBD beta; RBD gamma</td>
      <td>This paper</td>
      <td></td>
      <td>Expressed in HEK293 cells and purified</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-human ACE2 (mouse monoclonal)</td>
      <td>NOVUS Biologicals</td>
      <td>AC384</td>
      <td>(5 µg/mL)</td>
    </tr>
    <tr>
      <td>Cell line (human)</td>
      <td>FreeStyle HEK293F Cells</td>
      <td>ThermoFisher Scientific</td>
      <td>RRID:CVCL_D603</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>FreeStyle MAX Reagent</td>
      <td>ThermoFisher</td>
      <td>16447100</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>FreeStyle 293 Expression Medium</td>
      <td>ThermoFisher</td>
      <td>12338018</td>
      <td></td>
    </tr>
    <tr>
      <td>commercial assay or kit</td>
      <td>QuikChange II XL</td>
      <td>Agilent</td>
      <td>200,521</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Amine coupling kit</td>
      <td>Cytiva</td>
      <td>BR100050</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GraphPad</td>
      <td>Prism</td>
      <td>Version 9</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>CM5 sensor chips</td>
      <td>Cytiva</td>
      <td>29149603</td>
      <td></td>
    </tr>
  </tbody>
</table>

### ACE2 and RBD variant constructs

The plasmid used to express soluble ACE2 WT (pOPINTTGneo_ACE2-BAP), which was kindly provided by Ray Owens (Oxford Protein Production Facility-UK), encoded the following protein:

The carboxy-terminal end has a biotin acceptor peptide (underlined) followed by an oligohistidine tag.

The pCAGG plasmid used to express the RBD WT construct (Amanat et al., 2020) encoded the following protein:

The carboxy-terminal end has an oligohistidine tag.

ACE2 and RBD point mutations were introduced into these plasmid constructs using the Agilent QuikChange II XL Site-Directed Mutagenesis Kit following the manufacturer’s instructions. The primers were designed using the Agilent QuikChange primer design web program.

### HEK293F cell transfection

Cells were grown in FreeStyle 293 Expression Medium (ThermoFisher Scientific, 12338018) in a 37°C incubator with 8% CO2 on a shaking platform at 130 rpm. Cells were passaged every 2–3 days with the suspension volume always kept below 33.3% of the total flask capacity. The cell density was kept between 0.5 and 2 million per ml. Before transfection cells were counted to check that cell viability was above 95%, and the density was adjusted to 1.0 million per ml. For 100 ml transfection, 100 µl FreeStyle MAX Reagent (ThermoFisher Scientific, 16447100) was mixed with 2 ml Opti-MEM (ThermoFisher Scientific, 51985034) for 5 min. During this incubation, 100 µg of expression plasmid was mixed with 2 ml Opti-MEM (or in situ biotinylation of ACE2 90 µg of expression plasmid was mixed with 10 µg of expression plasmid encoding the BirA enzyme). The DNA was then mixed with the MAX Reagent and incubated for 25 min before being added to the cell culture. For ACE2 in situ biotinylation, biotin was added to the cell culture at a final concentration of 50 µM. The culture was left for 5 days for protein expression to take place.

### Protein purification

Cells were harvested by centrifugation and the supernatant collected and filtered through a 0.22 μm filter. Imidazole was added to a final concentration of 10 mM and PMSF added to a final concentration of 1 mM; 1 ml of Ni-NTA Agarose (Qiagen; 30310) was added per 100 ml of supernatant and the mix was left on a rolling platform at 4°C overnight. The mix was poured through a gravity flow column to collect the Ni-NTA Agarose. The Ni-NTA Agarose was washed three times with 25 ml of wash buffer (50 mM NaH2PO4, 300 mM NaCl, and 20 mM imidazole at pH 8). The protein was eluted with elution buffer (50 mM NaH2PO4, 300 mM NaCl, and 250 mM imidazole at pH 8). The protein was concentrated, and buffer exchanged into size exclusion buffer (25 mM NaH2PO4 and 150 mM NaCl at pH 7.5) using a protein concentrator with a 10,000 molecular weight cut-off. The protein was concentrated down to less than 500 μl and loading onto a Superdex 200 10/300 GL (Cytiva, 17-5175-01) size exclusion column (Figure 2—figure supplement 1). Fractions corresponding to the desired peak were pooled and frozen at –80°C. Samples from all observed peaks were analysed on a reducing SDS–PAGE gel (Figure 2—figure supplement 1).

### Surface plasmon resonance

RBD binding to ACE2 was analysed on a Biacore T200 instrument (Cytiva) at 37°C and a flow rate of 30 µl/min. Running buffer was HBS-EP (Cytiva, BR100669). Streptavidin was coupled with a CM5 sensor chip (Cytiva, 29149603) using an amine coupling kit (Cytiva, BR100050) to near saturation, typically 10,000–12,000 response units (RU). Biotinylated ACE2 WT and variants were injected into the experimental flow cells (FC2–FC4) for different lengths of time to produce desired immobilisation levels (20–800 RU). FC1 was used as a reference and contained streptavidin only. Excess streptavidin was blocked with two 40 s injections of 250 µM biotin (Avidity). Before RBD injections, the chip surface was conditioned with eight injections of the running buffer. A dilution series of RBD was then injected in all FCs. Buffer alone was injected after every two or three RBD injections. The length of all injections was 30 s, and dissociation was monitored for 180–670 s. The background response measured in FC1 was subtracted from the response in the other three FCs. In addition, the responses measured during buffer injections closest in time were subtracted. Such double-referencing improves data quality when binding responses are low as needed to obtain accurate kinetic data (Myszka, 1999). At the end of each experiment, an ACE2-specific mouse monoclonal antibody (NOVUS Biologicals, AC384) was injected at 5 µg/ml for 10 min to confirm the presence and relative amounts of immobilised ACE2.

### Data analysis

Double-referenced binding data was fitted using GraphPad Prism. The koff was determined by fitting a mono-exponential decay curve to data from the dissociation phase of each injection. The koff from four to six RBD injections was averaged (Figure 2—figure supplement 2A). The kon was determined by first fitting a mono-exponential association curve to data from the association phase, yielding the kobs, and then plotting the kobs vs the concentration of RBD and performing a linear fit of the equation kobs = kon*[RBD]+ koff to this data (Figure 2—figure supplement 2B), using the koff determined as above to constrain the fit.

The KD was either calculated (calculated KD = koff/kon) or measured directly (equilibrium KD) as follows. Equilibrium binding levels at a given [RBD] were determined from the fit of the mono-exponential association phase model to the association phase data. These equilibrium binding levels were plotted against [RBD], and a fit of the simple 1:1 Langmuir binding model to this data was used to determine the equilibrium KD (Figure 2D).

ΔG for each affinity measurement was calculated from the relationship ΔG = R*T*lnKD, where R = 1.987 cal mol–1 K–1, T = 310.18 K, and KD is in units M. ΔΔG values (Table 2 and Figure 3D) were calculated for each mutant from the relationship ΔΔG = ΔGWT – DGM. The predicted ΔΔG for interactions with multiple mutants were calculated by adding the single mutant ΔΔG values (Figure 3D). The difference between the measured and predicted ΔΔG (ΔΔΔG) for interactions between the ACE2 and RBD mutants was calculates as ΔΔΔG = measured ΔΔG – predicted ΔΔG (Figure 4B).

All errors represent standard deviations and errors for calculated values were determined by error propagation.
