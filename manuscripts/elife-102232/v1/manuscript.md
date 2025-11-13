# Temporal dynamics of viral fitness and the adaptive immune response in HCV infection

## Authors

- Melanie Rose Walker<sup>1</sup> ([ORCID: 0000-0002-9731-9880](https://orcid.org/0000-0002-9731-9880))
- Preston Leung<sup>1</sup>
- Elizabeth Keoshkerian<sup>1</sup>
- Mehdi R Pirozyan<sup>1</sup>
- Andrew Lloyd<sup>2</sup>
- Fabio Luciani<sup>2</sup> ([ORCID: 0000-0003-0666-6324](https://orcid.org/0000-0003-0666-6324)) †
- Rowena A Bull<sup>1</sup>

### Affiliations

1. Viral Immunology Systems Program, The Kirby Institute Sydney Australia
2. School of Biomedical Sciences, Faculty of Medicine, The University of New South Wales Sydney Australia ([ROR:03r8z3t63](https://ror.org/03r8z3t63))

† Corresponding author

## Abstract

Numerous studies have shown that viral variants that elude the host immune response may incur a fitness expense, diminishing the survival of the viral strain within the host, and the capacity of the variant to survive future transmission events. This definition can be divided into intrinsic fitness—fitness without immune pressure—and effective fitness, which includes immune influence. Co-occurring mutations outside immune-targeted epitope regions may also affect variant survival (epistasis). Analysis of viral fitness and epistasis over the non-structural protein regions is lacking for hepatitis C virus (HCV). Using a rare cohort of subjects recently infected with HCV, we build on prior work by integrating mathematical modeling and experimental data to examine the interplay between transmitted/founder (T/F) viruses, immune responses, fitness, and co-occurring mutations. We show that viral fitness declines during the first 90 days post-infection (DPI), associated with the magnitude of CD8 +T cell responses and early diversification. Fitness then rebounds in a complex pattern marked by co-occurring mutations. Finally, we demonstrate that an early, strong CD8 +T cell response in the absence of neutralizing antibodies (nAbs) exerts strong selective pressure, allowing escape and chronic infection. These insights support HCV vaccine strategies that elicit broad T and B cell immunity.

## Introduction

Hepatitis C virus (HCV) is a major cause of chronic liver disease globally (Lanini et al., 2016). Following acute infection, approximately 75% of people fail to clear the virus, resulting in chronic hepatitis with progressive fibrosis and ultimately cirrhosis, liver failure, and an increased risk of hepatocellular carcinoma (Seeff, 2002; Lavanchy, 2009; Micallef et al., 2006; Santantonio et al., 2008). Despite the arrival of direct-acting antiviral agents (DAA) with remarkable efficacy, the unresolved financial and health service challenges in ensuring universal DAA access to those infected globally, and likelihood of reinfection in high-risk populations, necessitate a prophylactic vaccine as an essential component for the WHO goal of global elimination of HCV infection as a public health threat (Fuerst et al., 2017).

Due to a high mutation rate during replication, the HCV genome is highly diverse, being classified into eight major genotypes (genotypes 1–8), and 86 subtypes (labeled alphabetically [a, b, c, etc.]) (Smith et al., 2014; Hedskog et al., 2019). HCV also exists within each infected host as a diverse, rapidly evolving population termed a quasispecies. Nevertheless, transmission of HCV is associated with a strong genetic bottleneck with as few as 1–3 transmitted/founder (T/F) viruses commonly establishing infection in the new host, despite hundreds of individual variants found in the source (Li et al., 2016; Bull et al., 2011). This is followed by a second genetic bottleneck at ~100 days post-infection (DPI), where T/F viruses become undetectable. At this stage, either an existing variant that was occurring in low frequency outside detection range or an existing variant with novel mutations generated following immune selection is observed in those who progress to chronic infection. These variants carry mutations within epitopes targeted by B cell and CD8 +T cells (Bull et al., 2011). Indeed, clearance of HCV has been associated with an early onset of T/F-specific neutralizing antibodies (nAbs) (Walker et al., 2019; Dowd et al., 2009; Lavillette et al., 2005; Osburn et al., 2014), while early and strong CD8 +T cell responses against the T/F virus have been associated with the generation of immune escape mutations found within MHC-I restricted epitopes which lead to the progression of chronic infection (Bull et al., 2015; Cai et al., 2022).

Numerous virological studies have shown that viral variants that elude the host immune response might incur a fitness expense, diminishing the survival of the viral strain and reducing the capacity of the variant to survive future transmission events as the variants mutate away from the T/F virus (Sanjuán et al., 2004; Venner et al., 2016). This generic definition of fitness can be further divided into intrinsic fitness (also referred to as replicative fitness), where the fitness of sequence composition of the variant is estimated without the influence of host immune pressure. On the other hand, effective fitness (from here on referred to as viral fitness) considers fundamental intrinsic fitness with host immune pressure acting as a selective force to direct mutational landscape (Hart and Ferguson, 2015), which subsequently influences future transmission events as it dictates which subvariants remain in the quasispecies. In HCV, the structural envelope proteins, E1 and E2, which are predominantly targeted by B cell responses including neutralizing antibodies (nAbs), have been found to collectively mediate viral fitness (Zhang et al., 2023). This interdependence suggests that mutations in the E1 protein could potentially compensate for fitness deficits, thereby facilitating the virus' ability to evade antibodies that specifically target the E2 protein (Zhang et al., 2023). Furthermore, comparative analyses of E2 fitness in genotype 1 a and genotype 1b sequences found that subtype 1b viruses have a higher probability to evade immune responses (Quadeer et al., 2019; Zhang et al., 2022). By contrast, a comprehensive analysis of the non-structural protein regions (NS1, NS2, NS3, NS4A, NS4B, NS5A, NS5B) in mediating viral fitness is lacking. For the scope of this study, a fitness model developed for HIV (Ferguson et al., 2013; Barton et al., 2016) and modified for HCV (Hart and Ferguson, 2015) was used to estimate the fitness landscape of HCV subtypes. Barton et al.’s approach to understand HIV mutational landscape resulting in immune escape had two fundamental points: (1) replicative fitness depends on the virus sequence and the requirement to consider the effect of co-occurring mutations, and (2) evolutionary dynamics (e.g. host immune pressure) (Barton et al., 2016). Together they pave the way to predict the mutational space in which viral strains can change given the unique immune pressure exerted by individuals infected with HIV. This model fits well with the pathology of HCV infection. For instance, HIV and HCV are both RNA viruses with rapid rates of mutation. Additionally, like HIV, chronic infection is an outcome for HCV-infected individuals; however, unlike HIV, there is a 25% probability that individuals infected with HCV will naturally clear the virus. Previously published studies (Keele et al., 2008) have shown that HIV also goes through a genetic bottleneck which results in the T/F virus losing dominance and being replaced by a chronic subtype, identified by the immune escape mutations. The concepts in Barton’s model and its functionality to assess fitness based on the complex interaction between viral sequence composition and host immune response are also applicable to early HCV infection. For generating the viral fitness models, sequences in clinical databases were used to represent the circulating viral variants with the assumption that commonly observed viral variants denoted higher fitness. This model was then used to infer the initial fitness landscape by providing the T/F virus and producing a fitness value. The fitness of the subsequent variants was then described as the relative fitness in comparison to the T/F virus, over the course of an infection.

Mutations that can incur a fitness expense can typically be alleviated or compensated by other mutations, making certain combinations of mutations beneficial (Campo et al., 2008). These co-occurring mutations can arise outside of the epitope regions and facilitate their compensatory effects, thus increasing the likelihood of survival of the variant (Oniangue-Ndza et al., 2011). This phenomenon is called positive epistasis. However, epistasis may also be negative if a combination of mutations provides a smaller fitness gain than anticipated based on the additive effects of the individual mutations. Nevertheless, epistatic interactions in HCV have not been studied over acute and chronic phase sequences to infer HCV evolution over the course of the infection. Understanding viral fitness and epistatic interactions in HCV is critical in anticipating future substitutions that are antigenically significant, thus aiding in not only mapping the potential landscape of evolution, but also an improved strategic approach for the selection of potent vaccine strains.

Previously, we longitudinally deep sequenced HCV in 14 individuals who were recently infected with HCV to identify the T/F virus and the evolving quasispecies during the infection (Bull et al., 2015; Cai et al., 2022). We identified Human Leucocyte Antigen class I (HLA-I) epitopes from the T/F viruses and the mutated variants. Experimental testing using IFN-γ ELISpot revealed that a strong CD8 +T cell response was linked to rapid immune evasion (Bull et al., 2015; Cai et al., 2022). Here, we build upon our prior investigations by integrating mathematical models and experimental data to examine the interplay between evolving T/F viruses, the adaptive immune response, viral fitness, and co-occurring mutations.

## Results

### Prediction, generation, and validation of HLA class I-restricted epitopes

A total of 14 subjects with primary HCV infection followed from pre-seroconversion until infection outcome were included in this study (Table 1). The first available viremic sample was collected at a median of 68 days post-infection (DPI) (range 2–337 DPI). Of the 14 subjects included in this study, 8 subjects naturally cleared the infection (termed here clearers) and 6 subjects progressed to chronic infection (termed here chronic progressors). The median time to natural clearance was 163 DPI (range 69–357). Next-generation sequencing (NGS) data were available for eight viremic time points from these subjects to study HCV RNA populations in depth. The T/F viruses were estimated from the distribution of variants at the earliest sampling time point as previously described (Bull et al., 2011; Walker et al., 2019; Bull et al., 2015). Thirteen of the 14 subjects had a single T/F virus, with only subject 300023 having two T/F viruses identified, as previously published (Bull et al., 2011; Bull et al., 2015). T/F genomes were utilized to predict HLA-I epitopes from the T/F viruses and the mutated variants (Cai et al., 2022). These epitopes were tested and validated for IFN-γ ELISPOT (Figure 1—figure supplement 1; Cai et al., 2022).

**Table 1.**
 Subject characteristics and time point analysis.


<table>
  <thead>
    <tr>
      <th>Subject ID*</th>
      <th>Age</th>
      <th>Sex</th>
      <th>Disease outcome</th>
      <th>GT†</th>
      <th colspan="2">HLA-A</th>
      <th colspan="2">HLA-B</th>
      <th>First sampling point (DPI‡)</th>
      <th>Time to clearance</th>
      <th>Initial viral load</th>
      <th>No. samples sequenced§</th>
      <th>No. T/F¶ viruses</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>300023</td>
      <td>22</td>
      <td>M</td>
      <td>Chronic</td>
      <td>1 a</td>
      <td>02:01</td>
      <td>02:01</td>
      <td>44:02:00</td>
      <td>57:01:00</td>
      <td>36</td>
      <td>-</td>
      <td>19,234,348</td>
      <td>6</td>
      <td>2</td>
    </tr>
    <tr>
      <td>300240</td>
      <td>21</td>
      <td>M</td>
      <td>Chronic</td>
      <td>3 a</td>
      <td>02:01</td>
      <td>02:01</td>
      <td>15:01</td>
      <td>57:01:00</td>
      <td>44</td>
      <td>-</td>
      <td>54,887</td>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr>
      <td>300256</td>
      <td>31</td>
      <td>M</td>
      <td>Chronic</td>
      <td>1 a</td>
      <td>03:01</td>
      <td>24:02:00</td>
      <td>07:02</td>
      <td>35:01:00</td>
      <td>44</td>
      <td>-</td>
      <td>34,149,824</td>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr>
      <td>HOKD0485FX</td>
      <td>26</td>
      <td>F</td>
      <td>Chronic</td>
      <td>1b</td>
      <td>01:01</td>
      <td>30:01:00</td>
      <td>08:01</td>
      <td>13:02</td>
      <td>30</td>
      <td>-</td>
      <td>733,849</td>
      <td>8</td>
      <td>1</td>
    </tr>
    <tr>
      <td>THDS1086MX</td>
      <td>25</td>
      <td>M</td>
      <td>Chronic</td>
      <td>1 a</td>
      <td>02:01</td>
      <td>32:01:00</td>
      <td>14:02</td>
      <td>27:05:00</td>
      <td>16</td>
      <td>-</td>
      <td>235,662</td>
      <td>6</td>
      <td>1</td>
    </tr>
    <tr>
      <td>THGS0684MX</td>
      <td>28</td>
      <td>M</td>
      <td>Chronic</td>
      <td>1 a</td>
      <td>02:01</td>
      <td>32:01:00</td>
      <td>27:02:00</td>
      <td>40:01:00</td>
      <td>2</td>
      <td>-</td>
      <td>140,200</td>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr>
      <td>300360</td>
      <td>29</td>
      <td>M</td>
      <td>Clearer</td>
      <td>3 a</td>
      <td>68:02:00</td>
      <td>32:01:00</td>
      <td>14:02</td>
      <td>40:01:00</td>
      <td>30</td>
      <td>178</td>
      <td>5,648,631</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <td>300277</td>
      <td>25</td>
      <td>M</td>
      <td>Clearer</td>
      <td>3 a</td>
      <td>02:01</td>
      <td>11:01</td>
      <td>44:02:00</td>
      <td>44:02:00</td>
      <td>39</td>
      <td>69</td>
      <td>5,482,503</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <td>MCRL0786FX</td>
      <td>25</td>
      <td>F</td>
      <td>Clearer</td>
      <td>1 a</td>
      <td>01:01</td>
      <td>29:02:00</td>
      <td>44:02:00</td>
      <td>44:02:00</td>
      <td>80</td>
      <td>115</td>
      <td>1846</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>400087</td>
      <td>32</td>
      <td>F</td>
      <td>Clearer</td>
      <td>1b</td>
      <td>24:02:00</td>
      <td>30:04:00</td>
      <td>14:02</td>
      <td>15:06</td>
      <td>45</td>
      <td>139</td>
      <td>13,118,082</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <td>300364</td>
      <td>29</td>
      <td>M</td>
      <td>Clearer</td>
      <td>1 a</td>
      <td>01:01</td>
      <td>03:01</td>
      <td>07:02</td>
      <td>57:01:00</td>
      <td>337</td>
      <td>352</td>
      <td>1932</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>300231</td>
      <td>22</td>
      <td>M</td>
      <td>Clearer</td>
      <td>3 a</td>
      <td>01:01</td>
      <td>01:01</td>
      <td>07:02</td>
      <td>57:01:00</td>
      <td>6</td>
      <td>148</td>
      <td>2,242,163</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>300089</td>
      <td>26</td>
      <td>M</td>
      <td>Clearer</td>
      <td>1b</td>
      <td>01:01</td>
      <td>30:01:00</td>
      <td>07:02</td>
      <td>57:01:00</td>
      <td>181</td>
      <td>357</td>
      <td>70,737</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>300164</td>
      <td>22</td>
      <td>F</td>
      <td>Clearer</td>
      <td>3 a</td>
      <td>24:02:00</td>
      <td>32:01:00</td>
      <td>07:02</td>
      <td>40:01:00</td>
      <td>71</td>
      <td>204</td>
      <td>684,028</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

_*Identification.†Genotype. ‡Days post infection. §Next generation sequencing. ¶Transmitted/Founder._

To examine the role of CD8 +T cell responses in driving viral evolution, longitudinal deep sequenced data was analyzed for fixation events as previously described (Cai et al., 2022). For those subjects who ultimately spontaneously cleared HCV infection, there were no non-synonymous fixation mutations (defined as having frequency of occurrence greater than or equal to 70% in the sequencing data) occurring within epitope regions (Supplementary file 1). Therefore, subjects who cleared infection were not included for further analysis of viral fitness and immune escape throughout this manuscript. From the six subjects who developed chronic infection, non-synonymous fixation mutations occurring within epitope regions were observed and peptide epitopes were selected (Supplementary file 2). A total of 494 out of 10945 (4.51%) potential epitopes across the six chronic subjects (45–100 epitopes per subject) were selected and tested for IFN-γ ELISPOT (Supplementary file 2, Figure 1—figure supplement 1). Of those selected for testing, 30 (6.68%) epitopes induced positive responses in the IFN-γ ELISPOT, and of these, 14 epitopes showed evidence of escape (as indicated by reduced recognition in the IFN-γ ELISPOT assay; Figure 1, Supplementary file 2, Figure 1—figure supplement 1).

![Figure 1.](https://cdn.elifesciences.org/articles/102232/elife-102232-fig1-v1.jpg)

**Figure 1.:** IFN-γ ELISpot values (SFU/million, right y-axis) and viral load (IU/mL, left y-axis) measured in subjects (A) 300256, (B) THDS1086MX and (C). THGS0684MX for epitope-specific CD8 +T cell responses (see key). Subjects HOKD0485FX, 300023 and 300240 have been shown previously (Bull et al., 2011; Cai et al., 2022). Escape variants are shown with a clear symbol of the original epitope found in the transmitted/founder (see key). IFN-γ ELISpot values were generated from multiple biological samples. Peptides were pooled and tested in technical duplicate; positive responses were confirmed by testing the individual peptide in a follow-up IFN-γ ELISpot assay. (D) Plot of average Shannon entropy (SE) against the rate of escape for each epitope in each protein region per subject. Plots of average SE against average IFN-γ ELISPOT response at >90 DPI (purple) (E) and <90 DPI (green) (F) are also shown. p-Values (P) and Pearson’s correlation coefficient (R) are shown in the top left corner of each panel.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/102232/elife-102232-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** CD8 +T cell responses were tested by IFN-γ ELISPOT assays measuring spot-forming unit per million cells (SFU/million cell) of epitopes (vertical axis) across three populations. The horizontal axis from left to right shows the population of epitopes that undergo fixation events in subjects who became chronically infected by HCV (Ch), epitopes that had no mutations, and epitopes from subjects that spontaneously cleared HCV infection (Cl). Statistical comparisons are Mann-Whitney tests. Scatter plots represent means and standard deviation.

The location of these 14 epitopes associated with escape was mostly within the non-structural regions of the HCV genome, with 7 (50%) epitopes identified in the NS3 region, 3 (21.4%) in NS5B, and 2 (14.3%) in NS2. One (7%) epitope was identified in the Core region and one (7%) in E2, which were both found in subject 300256 (Table 2). Single fixation events were observed in the majority of these epitopes, with the exception of two epitopes (in subjects HOKD0485FX and 300256) where two fixation events occurred (Table 2).

**Table 2.**
 Epitopes and escape rate of epitopes from chronic progressors with fixation events where positive IFN-γ ELISPOT response was detected on the T/F virus.


<table>
  <thead>
    <tr>
      <th>Subject ID</th>
      <th>GT</th>
      <th>Epitope (MT)*,†</th>
      <th>Epitope (WT)†</th>
      <th>Start aa</th>
      <th>End aa</th>
      <th>Region</th>
      <th>ELISPOT‡</th>
      <th>DPI§</th>
      <th>Matching Subject Allele</th>
      <th>Predicted Rank (WT)</th>
      <th>Rank Change</th>
      <th>Epsilon Estimate¶</th>
      <th>p-Value</th>
      <th>Fitness Estimated</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">300023</td>
      <td rowspan="2">1a</td>
      <td>RAEAHLHAW</td>
      <td>RAEAQLHAW</td>
      <td>852</td>
      <td>860</td>
      <td>NS2</td>
      <td>91</td>
      <td>60</td>
      <td>HLA-B*57:01</td>
      <td>0.3</td>
      <td>0</td>
      <td>0.0625</td>
      <td>0.0001</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>NSKRTPMGF</td>
      <td>KSKRTPMGF</td>
      <td>2629</td>
      <td>2637</td>
      <td>NS5B</td>
      <td>484</td>
      <td>60</td>
      <td>HLA-B*57:01</td>
      <td>0.45</td>
      <td>–2.2</td>
      <td>0.1243</td>
      <td>0.0036</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td rowspan="2">300240</td>
      <td rowspan="2">3a</td>
      <td>RAQALPPSW</td>
      <td>RAQAPPPSW</td>
      <td>1602</td>
      <td>1610</td>
      <td>NS3</td>
      <td>55</td>
      <td>44</td>
      <td>HLA-B*57:01</td>
      <td>0.2</td>
      <td>0</td>
      <td>0.1025</td>
      <td>0.0236</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>RLGPVQNEI</td>
      <td>RLGPVQNEV</td>
      <td>1633</td>
      <td>1641</td>
      <td>NS3</td>
      <td>300</td>
      <td>71</td>
      <td>HLA-A*02:01</td>
      <td>1.6</td>
      <td>–2.1</td>
      <td>0.0303</td>
      <td>0.0001</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td rowspan="3">300256</td>
      <td rowspan="3">1a</td>
      <td>DYPYRLWHY</td>
      <td>HYPYRLWHY</td>
      <td>610</td>
      <td>618</td>
      <td>E2</td>
      <td>750</td>
      <td>58</td>
      <td>HLA-A*24:02</td>
      <td>1.45</td>
      <td>–0.5</td>
      <td>0.4813</td>
      <td>0.0242</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>GPKMGVRAT</td>
      <td>GPRLGVRAT</td>
      <td>41</td>
      <td>49</td>
      <td>Core</td>
      <td>25</td>
      <td>58</td>
      <td>HLA-B*07:02</td>
      <td>0.4</td>
      <td>–1.4</td>
      <td>0.0532</td>
      <td>0.0413</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>HPSIEEVAL</td>
      <td>HPNIEEVAL</td>
      <td>1359</td>
      <td>1367</td>
      <td>NS3</td>
      <td>150</td>
      <td>58</td>
      <td>HLA-B*35:01</td>
      <td>0.5</td>
      <td>0</td>
      <td>0.0565</td>
      <td>0.0001</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>HOKD0485FX</td>
      <td>1b</td>
      <td>HSRRKCDEL</td>
      <td>HSKKKCDEL</td>
      <td>1395</td>
      <td>1403</td>
      <td>NS3</td>
      <td>55</td>
      <td>79</td>
      <td>HLA-B*08:01</td>
      <td>3.3</td>
      <td>0.5</td>
      <td>0.2685</td>
      <td>0.972</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td rowspan="3">THDS1086MX</td>
      <td rowspan="3">1a</td>
      <td>KLVAMGLNAV</td>
      <td>KLVAMGINAV</td>
      <td>1406</td>
      <td>1415</td>
      <td>NS3</td>
      <td>85</td>
      <td>72</td>
      <td>HLA-A*02:01</td>
      <td>0.75</td>
      <td>0.5</td>
      <td>0.5098</td>
      <td>0.0005</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>TLSPYYKRHI</td>
      <td>TLSPYYKRYI</td>
      <td>830</td>
      <td>839</td>
      <td>NS2</td>
      <td>30</td>
      <td>72</td>
      <td>HLA-A*02:01</td>
      <td>3.35</td>
      <td>–6.05</td>
      <td>0.0689</td>
      <td>0.0003</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>VRMVMMTHF</td>
      <td>ARMVMMTHF</td>
      <td>2841</td>
      <td>2849</td>
      <td>NS5B</td>
      <td>25</td>
      <td>72</td>
      <td>HLA-B*27:05</td>
      <td>0.2</td>
      <td>–0.1</td>
      <td>0.2582</td>
      <td>0.0034</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td rowspan="3">THGS0684MX</td>
      <td rowspan="3">1a</td>
      <td>TSILGIGTV</td>
      <td>TSILGIGTA</td>
      <td>1324</td>
      <td>1332</td>
      <td>NS3</td>
      <td>230</td>
      <td>58</td>
      <td>HLA-A*02:01</td>
      <td>32</td>
      <td>17</td>
      <td>0.2861</td>
      <td>0.0145</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>SILGIGTVL</td>
      <td>SILGIGTAL</td>
      <td>1325</td>
      <td>1333</td>
      <td>NS3</td>
      <td>405</td>
      <td>58</td>
      <td>HLA-A*02:01</td>
      <td>5.6</td>
      <td>–1.2</td>
      <td>0.2861</td>
      <td>0.0145</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>AWETARYTPV</td>
      <td>AWETARHTPV</td>
      <td>2816</td>
      <td>2825</td>
      <td>NS5B</td>
      <td>50</td>
      <td>58</td>
      <td>HLA-A*02:01</td>
      <td>36.5</td>
      <td>3.5</td>
      <td>0.1082</td>
      <td>0.0484</td>
      <td>Yes</td>
    </tr>
  </tbody>
</table>

_*Final most dominant escape variant is shown (i.e. frequency of occurrence >70%).†Red shows the positions which undergo amino acid change. ‡ IFN-γ ELISPOT test of autologous PBMC measured in SFU per million PBMC against wild type epitope at earliest sample time point with a positive assay (shown in DPI column). WT - Wild Type and MT - Mutant Mutant epitopes are sourced from the final available deep sequenced data point. §Days post infection. ¶The epsilon estimate is the rate of escape given in per day._

### CD8+ T-cell responses contribute to the diversification of the viral population

In these same subjects, we previously found that high magnitude of IFN-γ responses were associated with rapid viral immune escape (Cai et al., 2022). Additionally, the interaction between immunodominance, entropy, and escape rate in acute HIV infection has been described, where immunodominance during acute infection was the most significant factor influencing CD8 +T cell pressure, with higher immunodominance linked to faster escape (Liu et al., 2013). In contrast, lower epitope entropy slowed escape, and together, immunodominance and entropy explained half of the variability in escape timing (Liu et al., 2013). To expand on these findings and determine whether viral diversity correlated with immune escape, Shannon entropy (SE) was calculated (Bull et al., 2011) across each protein region at the preceding time points to those identified to have fixation in T-cell targeted epitopes, and tested (Table 2) against the rate of escape (ϵ) estimated from the distribution of viral mutations in the NGS data. A significant positive correlation was found between SE and the rate of escape (Pearson’s correlation = 0.73, p-value = 0.01), indicating the higher diversity was associated with the occurrence of immune escape (Figure 1D).

To determine whether CD8 +T cell pressure was driving genomic diversification before and after the genetic bottleneck, the average IFN-γ ELISPOT response within each subject was calculated across multiple epitopes in the same protein region at each time point. This data was then correlated with global SE at two periods,<90 DPI and >90 DPI. At >90 DPI a significant positive correlation was found (Pearson’s correlation = 0.83, p-value = 0.01, Figure 1E), indicating that a stronger IFN-γ ELISPOT response was associated with higher diversity following the second genetic bottleneck. Interestingly, this relationship was not evident when examining time points at <90 DPI (Pearson’s correlation = 0.33, p-value = 0.23, Figure 1F). When considering both pre- and post-90 DPI periods, diversity appeared to be influenced by distinct selective pressures where the CD8 +T cell response plays a significant role in shaping viral population diversity, along with the emergence of epitope escape variants at >90 DPI.

### Viral fitness decreases during the first 90 DPI and is associated with the magnitude of CD8+ T-cell responses and the initial level of diversification

To understand how CD8 +T cell responses influence the evolution of viral fitness in the acute phase of infection and how the viral population adapts to the host, a quantitative analysis of viral fitness in viral haplotypes on longitudinal samples was performed. We utilized a fitness model initially developed for HIV (Barton et al., 2016) and adapted for HCV to estimate the fitness landscape of various HCV subtypes [24]. This model was then applied to infer the initial fitness landscape by providing the T/F virus, which generated a fitness value. The fitness of subsequent variants was calculated as relative fitness compared to the T/F virus over the course of the infection. Specifically, fitness of the viral population was estimated for the six chronic progressors (Table 2) in regions NS2, NS3, and NS5B and for each epitope, the population average relative fitness of the viral population over the course of infection was measured (Tables 3 and 4, Supplementary files 3–6).

**Table 3.**
 Co-occurring mutations, epitope escape mutants, and the associated frequency of occurrence and relative fitness of the NS3 region of subject THDS1086MX.


<table>
  <thead>
    <tr>
      <th>Time</th>
      <th>Viral load (IU/ml)</th>
      <th>Frequency</th>
      <th>Relative fitness</th>
      <th>1406KLVAMGLNAV1415mutations</th>
      <th colspan="3">Co-occurring mutations†</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="8">16DPI</td>
      <td rowspan="8">235662</td>
      <td>61.70%</td>
      <td>1.000</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>18.10%</td>
      <td>1.000</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>6.00%</td>
      <td>1.000</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>4.80%</td>
      <td>0.364</td>
      <td>V1408A</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>4.60%</td>
      <td>1.000</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>1.70%</td>
      <td>1.000</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>1.60%</td>
      <td>0.364</td>
      <td>V1408A</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>1.40%</td>
      <td>1.000</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="9">72DPI</td>
      <td rowspan="9">176550</td>
      <td>48.50%</td>
      <td>0.453</td>
      <td></td>
      <td>H1115T</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>24.70%</td>
      <td>0.453</td>
      <td></td>
      <td>H1115T</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>6.20%</td>
      <td>0.453</td>
      <td></td>
      <td>H1115T</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>6.20%</td>
      <td>0.453</td>
      <td></td>
      <td>H1115T</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>3.70%</td>
      <td>0.084</td>
      <td></td>
      <td>H1115T</td>
      <td>C1318Y</td>
      <td></td>
    </tr>
    <tr>
      <td>3.60%</td>
      <td>0.453</td>
      <td></td>
      <td>H1115T</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>3.30%</td>
      <td>0.453</td>
      <td></td>
      <td>H1115T</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>2.10%</td>
      <td>0.084</td>
      <td></td>
      <td>H1115T</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>1.80%</td>
      <td>0.069</td>
      <td></td>
      <td>H1115T</td>
      <td>C1318Y</td>
      <td>V1458A</td>
    </tr>
    <tr>
      <td rowspan="13">109DPI</td>
      <td rowspan="13">108737</td>
      <td>35.80%</td>
      <td>0.223</td>
      <td>I1412V</td>
      <td>H1115S</td>
      <td>R1118H</td>
      <td></td>
    </tr>
    <tr>
      <td>19.10%</td>
      <td>0.384</td>
      <td>I1412L</td>
      <td>H1115S</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>8.60%</td>
      <td>0.910</td>
      <td>I1412L</td>
      <td>V1112A</td>
      <td>H1115S</td>
      <td></td>
    </tr>
    <tr>
      <td>7.70%</td>
      <td>0.360</td>
      <td>I1412L</td>
      <td>V1112I</td>
      <td>H1115S</td>
      <td></td>
    </tr>
    <tr>
      <td>6.30%</td>
      <td>0.061</td>
      <td>I1412L</td>
      <td>H1115G</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>5.70%</td>
      <td>0.247</td>
      <td>I1412L</td>
      <td>H1115T</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>3.70%</td>
      <td>0.657</td>
      <td>I1412L</td>
      <td>V1112T</td>
      <td>H1115S</td>
      <td></td>
    </tr>
    <tr>
      <td>2.60%</td>
      <td>0.145</td>
      <td>I1412L</td>
      <td>V1112A</td>
      <td>H1115T</td>
      <td></td>
    </tr>
    <tr>
      <td>2.30%</td>
      <td>0.062</td>
      <td>I1412L</td>
      <td>V1112I</td>
      <td>H1115G</td>
      <td></td>
    </tr>
    <tr>
      <td>2.20%</td>
      <td>0.229</td>
      <td>I1412L</td>
      <td>V1112I</td>
      <td>H1115T</td>
      <td></td>
    </tr>
    <tr>
      <td>2.20%</td>
      <td>0.573</td>
      <td>I1412L</td>
      <td>V1112A</td>
      <td>H1115T</td>
      <td></td>
    </tr>
    <tr>
      <td>2.10%</td>
      <td>0.624</td>
      <td>I1412V</td>
      <td>H1115S</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>1.80%</td>
      <td>0.309</td>
      <td>I1412L</td>
      <td>H1115A</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="8">198DPI</td>
      <td rowspan="8">681389</td>
      <td>73.60%</td>
      <td>0.360</td>
      <td>I1412L</td>
      <td>V1112I</td>
      <td>H1115S</td>
      <td></td>
    </tr>
    <tr>
      <td>12.60%</td>
      <td>2.149</td>
      <td>I1412L*</td>
      <td>V1112I</td>
      <td>H1115S</td>
      <td>A1593V</td>
    </tr>
    <tr>
      <td>4.70%</td>
      <td>1.683</td>
      <td>A1409T</td>
      <td>V1112P</td>
      <td>H1115S</td>
      <td></td>
    </tr>
    <tr>
      <td>2.90%</td>
      <td>0.360</td>
      <td>I1412L</td>
      <td>V1112I</td>
      <td>H1115S</td>
      <td></td>
    </tr>
    <tr>
      <td>1.80%</td>
      <td>0.360</td>
      <td>I1412L</td>
      <td>V1112I</td>
      <td>H1115S</td>
      <td></td>
    </tr>
    <tr>
      <td>1.70%</td>
      <td>1.683</td>
      <td>A1409T</td>
      <td>V1112P</td>
      <td>H1115S</td>
      <td></td>
    </tr>
    <tr>
      <td>1.60%</td>
      <td>0.066</td>
      <td>I1412L</td>
      <td>V1112I</td>
      <td>H1115S</td>
      <td>M1268I</td>
    </tr>
    <tr>
      <td>1.20%</td>
      <td>0.360</td>
      <td>I1412L</td>
      <td>V1112I</td>
      <td>H1115S</td>
      <td></td>
    </tr>
  </tbody>
</table>

_*Bold - indicate escape variants with fitness estimate ≥1.†Only non-synonymous mutations are shown._

**Table 4.**
 Co-occurring mutations, epitope escape mutants, and the associated frequency of occurrence and relative fitness of NS3 region of subject THGS0684MX.


<table>
  <thead>
    <tr>
      <th>Time</th>
      <th>Viral load (IU/ml)</th>
      <th>Frequency</th>
      <th>Relative fitness</th>
      <th>1325SILGIGTAL1333Mutations</th>
      <th colspan="2">Co-occurring mutations*</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="5">2DPI</td>
      <td rowspan="5">140,200</td>
      <td>87.9%</td>
      <td>1.000</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>4.8%</td>
      <td>0.148</td>
      <td></td>
      <td>G1076W</td>
      <td></td>
    </tr>
    <tr>
      <td>3.2%</td>
      <td>1.000</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>3%</td>
      <td>0.155</td>
      <td></td>
      <td>G1076R</td>
      <td></td>
    </tr>
    <tr>
      <td>1.1%</td>
      <td>0.022</td>
      <td></td>
      <td>G1076W</td>
      <td>Y1521C</td>
    </tr>
    <tr>
      <td rowspan="5">58DPI</td>
      <td rowspan="5">19,932</td>
      <td>74.2%</td>
      <td>1.000</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>10.8%</td>
      <td>1.000</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>8.4%</td>
      <td>0.322</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>5.5%</td>
      <td>0.162</td>
      <td></td>
      <td>M1649T</td>
      <td></td>
    </tr>
    <tr>
      <td>1%</td>
      <td>0.322</td>
      <td></td>
      <td>S1289G</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="2">184DPI</td>
      <td rowspan="2">221,964</td>
      <td>90.9%</td>
      <td>1.042</td>
      <td>A1332V†</td>
      <td>P1496S</td>
      <td></td>
    </tr>
    <tr>
      <td>9.1%</td>
      <td>0.157</td>
      <td>A1332V</td>
      <td>D1316G</td>
      <td>P1496S</td>
    </tr>
  </tbody>
</table>

_*Only non-synonymous mutations are shown.†Bold - indicate escape variants with fitness estimate ≥1._

In general, in the six subjects who progressed to chronic infection, there was a decrease in average relative fitness in the period of <90 DPI with respect to the T/F virus (Figure 2). This was with the exception of subject 300023 which can be explained by the presence of two T/F viruses (Figure 2A) where the observed mutations responsible for the increase in viral fitness were present in the genome of the second T/F virus detected at 44DPI carrying substitutions H2750Q and T2917A (Supplementary file 3, Figure 2—figure supplement 1, Figure 2A; Bull et al., 2011; Walker et al., 2019).

![Figure 2.](https://cdn.elifesciences.org/articles/102232/elife-102232-fig2-v1.jpg)

**Figure 2.:** Longitudinal fitness plots of subjects (A) 300023, (B) 300240, (C) 300256, (D) HOKD0485FX, (E) THDS1086MX and (F) THGS0684MX are shown. Gray shade indicates viral load and is measured in IU/ml on the right y-axis. Colored lines indicate population average relative fitness estimate (right y-axis) for protein regions (see key). Vertical bars indicate standard deviation of population average relative fitness.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/102232/elife-102232-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** Diamonds represent haplotypes with blue indicating consensus sequence and green diamonds representing reconstructed haplotypes at 36DPI. Purple diamonds indicate reconstructed haplotypes at 44DPI. The NS5B region shows diversity consistent with the presence of two T/F viruses as previously described by us (Bull et al., 2011; Walker et al., 2019; Bull et al., 2015; Cai et al., 2022).

To understand the observed reduction in viral fitness within the first 90 DPI, a statistical analysis was performed to examine the relationship between population fitness and immune escape (ϵ), IFN-γ ELISPOT responses, and SE values (Figure 3). In the <90 DPI period, a significant positive correlation (Pearson’s correlation = 0.84, p-value = 0.0004) was identified between population average relative fitness and IFN-γ ELISPOT response (Figure 3A). A significant negative correlation between fitness estimate and SE (Pearson’s correlation = –0.48, p-value = 0.01) was also identified in the <90 DPI period (Figure 3B). No significant correlation was observed between ϵ and fitness estimates at <90 DPI (Pearson’s correlation = 0.34, p-value = 0.32; Figure 3C).

![Figure 3.](https://cdn.elifesciences.org/articles/102232/elife-102232-fig3-v1.jpg)

**Figure 3.:** The relationship of population fitness against (A) average IFN-γ ELISPOT, (B) average Shannon entropy (SE), and (C) rate of escape at <90 DPI (green) was measured by Pearson’s correlation. The relationship of population fitness against (D) average IFN-γ ELISPOT, (E) average Shannon entropy (SE), and (F) rate of escape at >90 DPI (purple) was also measured by Pearson’s correlation. p-Values (P) and Pearson’s correlation coefficient (R) are shown in the top left corner of each panel.

Similar to the analysis performed at <90 DPI, correlation tests were performed to understand the change in fitness at >90 DPI (Figure 3). No significant correlations were observed between the average relative fitness estimates and IFN-γ ELISPOT (Pearson’s correlation = 0.55, p-value = 0.25, Figure 3D), SE (Pearson’s correlation = 0.26, p-value = 0.26, Figure 3E), and ϵ (Pearson’s correlation = 0.39, p-value = 0.31, Figure 3F).

Overall, these results suggest that in the early phase when the T/F virus was the major variant, a fit viral population was targeted by a strong CD8 +T cell response. Mutations away from the T/F virus then reduced fitness. Insignificant correlations observed in >90 DPI also confirmed that once the chronic phase population had adapted against host immune response, immune pressure showed less impact on viral population fitness and diversity when compared to <90 DPI.

### Viral fitness rebounds with co-occurring mutations after the second genetic bottleneck at >90 DPI

After the second genetic bottleneck at >90 DPI, when viral load begins to rise, the distribution of relative fitness continued to decrease in most genomic regions analyzed for all six chronic progressors (Figure 2). However, THDS1086MX and THGS0684MX showed a contrasting pattern where the relative fitness measured for the NS3 region exceeded the fitness measured for the T/F virus, while the relative fitness decreased for the viral variants in comparison to the fitness of the T/F virus in the NS5B region (Figure 2E–F). Of note, THDS1086MX and THGS0684MX are purported to be recipients from the same donor and share an identical consensus sequence at <16 DPI (; Walker et al., 2016). Furthermore, the pair carries the same HLA-A alleles but different HLA-B alleles (Table 1). We wanted to explore the NS3 regions of THDS1086MX and THGS0684MX to further understand the specific mutations contributing to their relative fitness rebound and to elucidate the mechanisms driving viral evolution and adaptation in these individuals.

Further analysis revealed a complex pattern of evolution characterized by multiple sets of co-occurring mutations (Figure 4, Table 3). In subject THDS1086MX, at 16DPI, viral haplotypes did not carry any co-occurring mutations. However, at 72DPI, a set of three mutations (H1115T, V1458A, C1318Y) was found to be co-occurring within the same viral variant, with its relative fitness estimated to be inferior to the T/F virus (relative fitness = 0.069; Table 3). At 109DPI, multiple combinations of co-occurring mutations were observed. In particular, immune escape mutation 1406KLVAMG(I\L)NAV1415 was identified co-occurring with H1115S/G/T and V1112A/I/T. Variants carrying I1412L and H1115S had a relative fitness of at least one third of the T/F virus. The combination of 1406KLVAMG(I\L)NAV1415, H1115S, and V1112A reached a fitness level nearly equal to the T/F variant (relative fitness of 0.91, Table 3). This suggested a 90% restoration of fitness compared to the T/F virus when H1115S and V1112A were combined with the immune escape mutation. Notably, a variant with only 1406KLVAMG(I\L)NAV1415 and H1115S exhibited positive epistasis, with a relative fitness of 0.384.

![Figure 4.](https://cdn.elifesciences.org/articles/102232/elife-102232-fig4-v1.jpg)

**Figure 4.:** Highlighter plots (Geneious Prime 2023) derived from longitudinal sequencing from subjects THDS1086MX (top) and THGS0684MX (bottom) indicating co-occurring mutations relative to the transmitted/founder (TF) across the NS3 region. Numbers above highlighter plots denote the genomic amino acid number for the NS3 region. Sequences are labeled by frequency of occurrence (%) and days post infection (DPI). Specific amino acid changes are shown in Tables 3 and 4.

Viral variants with higher fitness than the T/F virus of subject THDS1086MX were observed at 198DPI (Figure 4, Table 3). One variant carried the epitope mutation 1406KLVAMG(I\L)NAV1415 with V1112I, H1115S, and an additional mutation A1593V, achieving a relative fitness of 2.14 at a frequency of 12.6%. Another variant with only 1406KLVAMG(I\L)NAV1415 V1112I and H1115S, occurring at 73.6%, showed a relative fitness of 0.360. Additionally, a new immune escape mutation, A1409L, co-occurred with V1112P and H1115S at a frequency of 4.70% and exhibited a relative fitness greater than the T/F (relative fitness = 1.68). The combination of 1406KLV(A\T)MGINAV1415, V1112P, and H1115S did not co-occur with 1406KLVAMG(I\L)NAV1415, V1112I, and H1115S, indicating a diversifying strategy for host adaptation. Overall, the combination of I1412L, V1112I, and H1115S emerged as the most advantageous mutation combination, enhancing virus fitness and reaching fixation in the viral population over the course of infection.

For THGS0684MX, co-occurring mutations in the NS3 region occurred in a much simpler fashion (Table 4), where the immune escape mutation 1325SILGIGT(A\V)L1333 achieved a relative fitness of 1.042 when co-occurring with P1496S. The effect of the synergistic mutations was also reflected in the fact that this variant reached 90.9% frequency of occurrence in the viral population at the last sequenced time point of 184DPI (Figure 4, Table 4).

To determine if the increase in estimated fitness was associated with reversion events, namely mutations towards common circulating variants that are assumed to be a more fit HCV strain (generated as previously described Bull et al., 2015). A comparison of the non-synonymous mutations at the final sequence time point in both subjects THDS1086MX and THGS0684MX to the global Genbank genotype 1 a consensus sequence was performed. This revealed that V1112P and A1593V (12.6% frequency) in subject THDS1086MX were both reversions toward the worldwide consensus (Figure 4, Table 3). Similarly, for subject THGS0684MX, the mutation A1332Y (90.9% frequency) also reverted to the global consensus strain (Figure 4, Table 4).

These findings suggest rapid adaptation of chronic HCV variants post-strong CD8 +T cell responses during acute infection, supported by positive epistasis via compensatory mutations post-second genetic bottleneck. Variations between subjects with identical T/F viruses imply a unique fitness restoration strategy for each individual rather than a universal mutation pattern across subjects sharing the same T/F variant.

### In chronic progressors, nAbs emerge after CD8+ T-cells and coincide with the rebound of viral fitness

Previously, we have shown that an early nAb response is associated with clearance (Walker et al., 2019). In those that develop chronic infection, nAb activity is truly delayed and develops towards longitudinal variants after the T/F is cleared (Walker et al., 2019). Furthermore, we have shown previously (Bull et al., 2015; Cai et al., 2022) that CD8 +T cell responses impose a strong selective force on the T/F virus population, thus contributing to its extinction and to the rise of the escape variants with the establishment of chronic infection. Here, a comprehensive analysis integrating nAb responses, CD8 +T cell responses, and viral fitness was performed to elucidate the dynamic interplay between the adaptive immune system and viral evolution and fitness.

All six chronic subjects included in this study had data for nAb responses (Walker et al., 2019), IFN-γ ELISPOT responses, and viral fitness readily available. A subset of three clearer subjects had data for nAb responses (Walker et al., 2019) and IFN-γ ELISPOT responses (Figure 5, Figure 5—figure supplement 1). As mentioned above, viral fitness could not be estimated for clearer subjects due to a lack of non-synonymous fixation mutations occurring within epitope regions.

![Figure 5.](https://cdn.elifesciences.org/articles/102232/elife-102232-fig5-v1.jpg)

**Figure 5.:** The timing (Days post-infection) of CD8 +T cell and nAbs is compared for clearer subjects (A) and chronic subjects (B). Statistical significance (Wilcoxon matched-pairs signed rank test) is represented by asterisks (p<0.05 (*)) and non-significance by NS. (C-E) show three representative subjects who developed chronic HCV infection. The blue line represents the IFN-γ ELISPOT (SFU/million). The maroon line represents HCV nAb ID50 titer with squares representing timepoints tested on autologous virus and circles representing timepoints tested on heterologous virus. Population average relative fitness estimate of regions NS5B (purple), NS3 (green), and NS2 (pink) is shown. Black arrows represent increases in average relative fitness. Neutralization results were generated from multiple biological samples with each sample assayed in technical quadruplicates across two independent experiments.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/102232/elife-102232-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (A-C) show 3 subjects who cleared HCV infection and (D-F) show three subjects who developed chronic HCV infection. The blue line represents the IFN-γ ELISPOT response (SFU/million). The maroon line represents HCV nAb ID50 titer with squares representing timepoints tested on autologous virus and circles representing timepoints tested on heterologous virus. The green line illustrates average relative fitness values. (A-C) The shaded area represents the longitudinal HCV RNA levels (IU/ml). (D-F) Population average relative fitness estimates of regions are shown (see key).

The timing of the first nAb responses and the IFN-γ ELISPOT response were assessed to elucidate the dynamics of both CD8 +T cell and nAb responses and their role in clearance or chronic outcomes. In the subset of three clearer subjects (those tested for both nAb responses Walker et al., 2019 and IFN-γ ELISPOT responses) no significant difference was found in the timing of nAb and IFN-γ ELISPOT responses, with both responses emerging in all three subjects at <100 DPI (Figure 5A). However, for chronic progressors, IFN-γ ELISPOT responses were first detectable at an average of 48 DPI (range 30–80 DPI) whereas nAb responses occurred significantly later, with an average onset of 465 DPI (range 74–945 DPI), indicating a notable delay compared to CD8 +T cell responses (p=0.0313, Wilcoxon matched-pairs signed rank test, Figure 5B).

Interestingly, in subjects THDS1086MX and THGS0684MX, we observed escape variants with higher relative fitness emerging concurrently with the onset of nAbs at 198 and 184 DPI, respectively (Figure 5E and F). Additionally, upon the appearance of nAbs, there was a decline in IFN-γ ELISPOT towards the selected epitopes, while nAb responses remained stable. This suggests a transition from CD8 +T cell-dominant immune responses to nAb-dominant immune responses. It’s noteworthy that a similar pattern was observed in subject 300023, where an increase in viral fitness coincided with a weak but detectable nAb response towards the T/F virus at 74 DPI (Figure 5G). Nevertheless, nAbs were undetectable at the subsequent timepoint while the IFN-γ ELISPOT response dominated until 200 DPI when nAb responses reappeared and increased along with IFN-γ ELISPOT. This suggests that nAbs were ineffective in controlling the virus in subject 300023 during this period (<100 DPI). For the other three subjects, no consistent pattern was observed (Figure 5—figure supplement 1). Specifically, for subjects HOKD0485FX and 300256, nAbs emerged well after viral decline, and there was a lack of CD8 +T cell data at the positive nAb timepoints, while for subject 300240 both IFN-γ ELISPOT and nAb responses increased after 300DPI.

Together, these results show that an early and strong CD8 +T cell response in the absence of nAbs imposes a strong selective force on the T/F virus population, enabling the virus to escape and establish chronic infection.

## Discussion

Using a rare cohort of very recently infected individuals, we report the dynamics of evolution of the viral quasispecies and the role of the host cytotoxic T-cell and nAb responses during the acute phase of primary HCV infection. We show that viral fitness decreases during the first 90DPI associated with the magnitude of CD8 +T cell responses and the initial level of diversification. Thereafter, viral fitness rebounds in a complex pattern of evolution characterized by multiple sets of co-occurring mutations. Finally, within this cohort of very recently HCV-infected individuals, we show that an early and strong CD8 +T cell response in the absence of nAbs imposes a strong selective force on the T/F virus population, enabling the virus to escape and establish chronic infection. Understanding these dynamics is crucial for developing effective vaccines for HCV.

We have previously demonstrated in HCV that a genetic bottleneck occurs in the viral population at around three months post-infection, where the T/F is replaced with new viral variants that dominate infection (Bull et al., 2011; Bull et al., 2015) and this genetic bottleneck event was similarly reported in the case of early HIV infection (Li et al., 2016). In fact, many parallels can be drawn between HIV infections and HCV infections in the context of emerging viral species that escape T cell immune responses. For example, these new variants carry amino acid changes across the viral genome, including HLA-I restricted epitopes, highlighting that T-cell responses, in the absence of nAbs, play a significant role in driving immune escape. (Bull et al., 2011; Bull et al., 2015; Cai et al., 2022; Kuntzen et al., 2007; Kantzanou et al., 2003). Nevertheless, the majority of studies on HCV CD8 +T cell responses to date focus only on the epitope and its escape variant without analyzing viral fitness or surrounding mutations which co-occur with the immune escape mutation (Campo et al., 2014). One major difference between HCV and HIV infection is the event where patients infected with HCV have an approximately 25% chance to naturally clear the infection as opposed to just achieving viral control in HIV infections. Here, we probed the underlying mechanism and questioned how the host immune response and HCV mutational landscape can allow the virus to escape the immune system. To understand this process, taking inspiration from HIV studies (Barton et al., 2016), a quantitative analysis of viral fitness relative to viral haplotypes was conducted using longitudinal samples to investigate whether a similar phenomenon was identified in HCV infections for our cohort of patients who progress to chronic infection. We observed a decrease in population average relative fitness in the period of <90 DPI with respect to the T/F virus in chronic subjects infected with HCV. The decrease in fitness correlated positively with IFN-γ ELISPOT responses and negatively with SE, indicating that CD8 +T cell responses drove the rapid emergence of immune escape variants, which initially reduced viral fitness. This is similarly reflected in HIV-infected patients where strong CD8 +T cell responses drove quicker emergence of immune escape variants, often accompanied by compensatory mutations (Barton et al., 2016).

While a recent HCV infection study examined mutations in the E2 region, revealing that certain co-occurring mutations led to a loss of E2 function in clearers but a gain in function for chronic progressors (Frumento et al., 2024), the impact of co-occurring mutations in the nonstructural regions on HCV outcomes remains largely unexplored (Campo et al., 2008; Campo et al., 2014; Aurora et al., 2009; Murray et al., 2013). Furthermore, previous studies on HCV have not integrated CD8 +T cell responses, longitudinal tracking of immune escape mutations, co-occurring mutations, and fitness estimation to analyze HCV evolutionary mechanisms (Leung et al., 2014). Combining these approaches provides a clearer understanding of HCV evolution by showing how co-occurring mutations impact viral survival over time. We observed that in some subjects, combinations of mutations could compensate for the negative fitness cost of immune escape, leading to a rebound in viral fitness during infection. This was not observed in all subjects and indicates that each subject’s mutation strategy is unique, even when there are shared HLA alleles (such as for subjects THDS1086MX and THGS0684MX). Additionally, as described in Barton et al.’s study, it is quite possible that due to the sequence background (i.e. the T/F virus sequence composition), combined with unique immune pressure exerted by individual hosts, there exist multiple paths for immune escapes with diversifying levels of fitness (Barton et al., 2016).

When the analysis of nAb responses, CD8 +T cell responses, and viral fitness was performed, it was interesting to note the opposite trend with regards to the humoral response in these same subjects. While it remains unclear how T- and B-cell components of the immune system might co-operate to confer protection, the findings of the current study strongly suggest that the absence of nAbs in chronic progressors enables viruses to continue to infect new cells, replicate, and mutate. This suggests a synergistic interaction between B and T-cell responses targeting the virus, emphasizing the importance of their co-occurrence. Although several studies have alluded to this (Walker et al., 2019; Bull et al., 2015; Cai et al., 2022), none have directly compared longitudinal B and T-cell responses in recent clearers versus chronic progressors. In chronic subjects, increased viral fitness after the genetic bottleneck aligned with nAb onset (Walker et al., 2019; Frumento et al., 2024). Our fitness model, using the T/F virus as a baseline, enables tracking of relative viral fitness changes over time. Here, nAb appearance coincided with declining IFN-γ ELISPOT responses (Bull et al., 2015; Cai et al., 2022) towards selected epitopes that showed evidence of escape, suggesting a shift from CD8 +T cell to nAb responses.

While our findings here are promising, it should be recognized that although the bioinformatics tool (iedb_tool.py) proved useful for identifying potential epitopes, there could be epitopes that are not predicted or false positives from the output, which could lead to missing real epitopes.

In conclusion, this study provides initial insights into the evolutionary dynamics of HCV, showing that an early, robust CD8 +T cell response without nAbs strongly selects against the T/F virus, enabling it to escape and establish chronic infection. However, these findings are preliminary and not exhaustive, warranting further investigation to fully understand these dynamics. Nevertheless, the work presented here could explain the lack of association with a lower incidence of chronic HCV infection compared to placebo observed in the recent Phase I/II trials of the ChAd3-NSmut and MVA-NSmut vaccines, which aimed to induce T cell responses by encoding HCV NS proteins (Page et al., 2021). While much work is still required to be able to fully understand the factors contributing to the overall dynamics of HCV infections, this work has the potential to inform the design of the next generation of vaccines.

## Methods

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
      <td>Cell line (Homo sapiens)</td>
      <td>Lenti-X 293T Cell Line</td>
      <td>Takara, Mountain View, CA, USA</td>
      <td>Cat# 632180</td>
      <td>Cell line maintained in High Glucose Dulbecco’s Modified Eagle Medium supplemented with 10% (v/v) heat-inactivated fetal bovine serum</td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>Huh7.5</td>
      <td>Apath, New York, NY, USA</td>
      <td></td>
      <td>Cell line maintained in High Glucose Dulbecco’s Modified Eagle Medium supplemented with 10% (v/v) heat-inactivated fetal bovine serum</td>
    </tr>
    <tr>
      <td>Transfected construct (Photinus pyralis)</td>
      <td>pTG126 MLV luciferase</td>
      <td>Prof. Francois-Loic Cosset; Bartosch et al., 2003</td>
      <td></td>
      <td>Vector to produce HCVpp</td>
    </tr>
    <tr>
      <td>Transfected construct (murine leukemia virus)</td>
      <td>phCMV-5349 MLV gag/pol</td>
      <td>Prof. Francois-Loic Cosset</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>CD8 T-cell(9-10mers)</td>
      <td>Mimotopes</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Mammalian Calphos transfection kit</td>
      <td>Macherey-Nagel</td>
      <td>Cat#631312</td>
      <td>For HCVpp transfection</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ShoRAH</td>
      <td>ShoRAH</td>
      <td>RRID:SCR_005211</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>LoFreq</td>
      <td>LoFreq</td>
      <td>RRID:SCR_013054</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Geneious</td>
      <td>Geneious</td>
      <td>RRID:SCR_010519</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>QuasiRecomb</td>
      <td>QuasiRecomb</td>
      <td>RRID:SCR_008812</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GraphPad</td>
      <td>GraphPad</td>
      <td>RRID:SCR_000306</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Immune Epitope Database and Analysis Resource (IEDB)</td>
      <td>Immune Epitope Database and Analysis Resource (IEDB)</td>
      <td>RRID:SCR_006604</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Python</td>
      <td>Python</td>
      <td>RRID:SCR_008394</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>RStudio</td>
      <td>RStudio</td>
      <td>RRID:SCR_000432</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ShoRAH</td>
      <td>ShoRAH</td>
      <td>RRID:SCR_005211</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>LoFreq</td>
      <td>LoFreq</td>
      <td>RRID:SCR_013054</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Geneious</td>
      <td>Geneious</td>
      <td>RRID:SCR_010519</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>QuasiRecomb</td>
      <td>QuasiRecomb</td>
      <td>RRID:SCR_008812</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Subjects and samples

Samples were available from two prospective cohorts of HCV-seronegative and aviremic, high-risk, individuals enrolled in the Hepatitis C Incidence and Transmission Studies (HITS) in prisons (HITS-p), or in the general community (HITS-c), as previously described (Walker et al., 2019; Walker et al., 2016; Cunningham et al., 2017; White et al., 2014). Risk behavior data and blood samples were collected every six months to screen for HCV RNA positivity and seroconversion. Participants identified as early incident cases were enrolled into a sub-cohort called HITS-incident (HITS-i) upon detection of new onset viremia without antibodies, as described previously (Walker et al., 2019). These subjects were then frequently sampled for 12 weeks before being offered antiviral treatment at 24 weeks, allowing for the classification of outcomes as either natural clearance or chronic infection. The date of infection was estimated by subtracting the average HCV pre-seroconversion window period, which has been estimated at 51 days from the midpoint between last seronegative and first seropositive time points as previously described (Bull et al., 2011; Walker et al., 2019; Page-Shafer et al., 2008; Glynn et al., 2005). Molecular HLA typing was performed at the Institute of Immunology and Infectious Diseases in Perth, Australia, using second-generation sequencing of HLA-A/B/C genes as previously described (Gaudieri et al., 2006). 14 subjects with stored peripheral blood mononuclear cells (PBMCs) were selected from the HITS-i cohort. This group included eight subjects with acute HCV infection and six subjects who developed chronic infection.

PBMCs were isolated from peripheral blood via density-based centrifugation and resuspended in RPMI (Sigma-Aldrich, MO) supplemented with penicillin, streptomycin, l-glutamine, and fetal bovine serum at 1×106 cells/mL.

### Viral sequencing and identification of T/Fs and longitudinal variants

Near full-length HCV genome amplification and sequencing datasets of the full-length viral genomes at multiple time points have been published previously (Bull et al., 2011; Walker et al., 2019; Bull et al., 2015; Cai et al., 2022; Bull et al., 2016; Rodrigo et al., 2017). Briefly, near full-length HCV genome amplification was performed using an nRT-PCR (Bull et al., 2016). Illumina (MiSeq Benchtop sequence, San Diego, USA) sequencing was performed on amplicons from longitudinal time points of the 14 subjects (Walker et al., 2019; Cai et al., 2022; Bull et al., 2016). A bioinformatics pipeline was used to clean and align reads generated from next-generation sequencing (NGS; Bull et al., 2011; Walker et al., 2019; Bull et al., 2015). To accurately detect single nucleotide polymorphisms (SNPs) from the aligned and cleaned sequences, analysis was performed to correct for random technical errors using the software ShoRAH, LoFreq, and Geneious (Walker et al., 2019; Zagordi et al., 2011; Wilm et al., 2012). Haplotypes were reconstructed from NGS data across the full genome using ShoRAH and QuasiRecomb (Zagordi et al., 2011; Töpfer et al., 2013). As described previously (Bull et al., 2011; Walker et al., 2019; Bull et al., 2015; Cai et al., 2022), to determine T/Fs, a statistical model, Poisson fitter, as well as phylogenetic analysis was applied to haplotypes from the first available viremic timepoint but prior to the first HCV antibodies (seroconversion) detection, for each subject to determine the T/F (Salazar-Gonzalez et al., 2009). Shannon Entropy (SE) was determined from the NGS data as previously described (Bull et al., 2011) with modifications to extend to individual protein regions (namely NS2, NS3, and NS5B). Briefly, SE was calculated using the frequency of occurrence of SNPs based on per codon position, this was further normalized by the length of the number of codons in the sequence which made up respective protein. An average SE value was calculated for each time point in each protein region for all subjects until the fixation event.

### CD8+ T-cell epitope selection

For each of the 14 subjects, non-synonymous fixation events (>70% frequency in the viral population) from the last time point sequenced were substituted into the /TF sequence, thus generating a modified sequence termed the fixation sequence.

Identification of MHC Class I restricted epitopes (9–10 amino acids) was performed by analysis of both HCV /TF and fixation sequences in conjunction with MHC Class I genotyping to predict epitopes and then compared with previous experimentally confirmed epitopes from the Immune Epitope Data Base (IEDB [https://www.iedb.org/]). This resulted in each prediction list containing at least 10,000 epitope predictions.

Due to the large number of epitopes and the lack of available PBMCs, a bioinformatics pipeline, iedb_tool, was developed in Python 2.7 to identify a subset of epitopes for further experimental and bioinformatics analyses. This software package is freely available and can be downloaded at: https://github.com/PrestonLeung/IEDBTool2 (copy archived at Preston, 2025). The predicted epitopes generated from IEDB were downloaded in plain text format and parsed into iedb_predictionParser.py with options -lower 100.0 to extract relevant subject information (HLA genotypes, predicted epitope sequence, start and end positions of the epitope sequence). The predicted data set was then used with the experimentally validated epitopes from IEDB. This step generated a categorized list of ranked epitopes for which predicted epitopes and HLA-I typing for each subject were matched with experimentally validated epitopes. An 80% homology threshold was set to facilitate small differences between the autologous epitope sequence and those that were previously reported from the IEDB database.

We prioritized epitopes that matched the HLA allele of the subject and classified these into three categories. Category 1 included epitopes for each subject from which the mutated variant was no longer predicted to be recognized, indicating a potential escape variant. Category 2 included epitopes from those that underwent escape, but the variant was still predicted to be recognized by CD8 +T cells and category 3 included epitopes that did not mutate during infection. A threshold of 10th percentile ranking or higher was used as a cutoff for epitope selection. For categories 2 and 3, we selected a maximum of 10 epitopes due to limitations in PBMC samples. An upper limit of 100 epitopes was set for each subject to account for the total PBMCs available for each time point in the ELISpot matrix testing approach (see below). If the above criteria gave a total number of epitopes less than 40, then epitopes from categories 2 and 3 were searched with a lowered threshold of 50th percentile ranking or higher to increase the sample size to at least 40. This refined list of ranked epitopes we refer to throughout the manuscript as “potential epitopes”.

### IFN-γ ELISPOT validation

Potential epitopes generated above were analyzed using matrix IFN-γ ELISPOT assays as previously described (Bull et al., 2015; Cai et al., 2022). While the ELISpot assay detects responses from both CD4 and CD8 T cells, our peptide design (9-10mers) is strongly biased toward CD8 T-cell detection. We have therefore interpreted ELISpot responses primarily in terms of CD8 T-cell activity. Briefly, peptides were synthesized by Mimotopes Australia and used in autologous CD8 +T cell ELISpot assays in pools of ≤5 peptides per well in a matrix format. The peptides were pooled such that any two wells would only have one common peptide, and each peptide was tested in at least two separate wells.

As previously described by us (Bull et al., 2015; Cai et al., 2022), PBMC were added to a 96-well ELISpot plate (MAIPS; Millipore, USA) precoated with gamma interferon (IFN-γ; Mabtech, Sweden) at a concentration of 150,000 cells per well and incubated overnight with peptides (final concentration of 10 µg/ml). Plates were read and analyzed using an AID plate reader (Autoimmun Diagnostika GmbH, Germany). A peptide/well was concluded to be a positive if it demonstrated an interferon-γ (IFN-γ) response ≥25 spot-forming units per million cells (SFU/million) and a negative control count of zero. A confirmation experiment using the IFN-γ ELISpot assay was conducted for individual positive peptides using one peptide per well in a concentration of 200,000 cells per well. At least one well per study subject was allocated as a positive control (anti-CD3 antibody; Mabtech, Sweden), and three wells were used as negative controls. Background was defined as the mean plus 3 standard deviations of the number of spots counted across the three negative controls.

### Estimating the rate of CD8+ T-cell epitope escape

The estimation of the rate of CD8 +T cell epitope escape was performed as previously described (Bull et al., 2015; Cai et al., 2022). Briefly, the kinetics of CD8 +T cell escape was estimated with a simple population dynamics model (Bull et al., 2015; Cai et al., 2022; Asquith et al., 2006). The model predicts that the frequency of the escape variant f(t) is: $f(t)=f_{0}/f_{0}+(1−f_{0})e^{−kt}$, where k is the rate of escape and it is assumed that the escape variant is present at a low frequency beyond the range of detection during the initial phase of time (t) at zero, and its frequency is given by f0. The escape variant was defined as any observed mutations away from the wild-type sequence that consequently becomes fixed in the population. Therefore, the frequency of the escape variant at individual longitudinal time points was the total frequencies of each epitope carrying the escape mutation regardless of the other amino acid positions. In some cases where the escape variant was not observed in the earlier time points, an estimate of 1/(n+1) replaces a frequency of 0, where n is the average coverage of the corresponding time point from the deep sequencing data. This model was used to estimate the rate of escape only in those cases with experimental evidence (ELISpot data generated in this study) of CD8 +T-cell-driven immune escape. Estimates were performed in R usin ag non-linear least-squares approach for non-linear models (R Development Core Team, 2012).

### Estimating survival fitness of viral variants

The model used for estimating viral fitness has been previously described by Hart and Ferguson, 2015. Briefly, the original approach used HCV subtype 1 a sequences to generate the model for the NS5B protein region. To update the model for other regions (NS3 and NS2) as well as other HCV subtypes in this study, subtype 1b and subtype 3 a sequences were extracted from the Los Alamos National Laboratory HCV database. An intrinsic fitness model was first generated for each subtype for NS5B, NS3, and NS2 region of the HCV polyprotein. Then, using longitudinally sequenced data from patients chronically infected with HCV as well as clinically documented immune escape to describe high viral fitness variants, we generated estimates of the viral fitness for subjects chronically infected with HCV in our cohort. This was performed on each viral variant reconstructed by QuasiRecomb as previously described (Hart and Ferguson, 2015; Ferguson et al., 2013; Barton et al., 2016). Specifically, haplotype reconstruction was performed longitudinally for each subject in a region of approximately 600 amino acids surrounding the experimentally confirmed CD8 +T cell epitopes. The fitness landscape inference is obtained by estimating the parameter of a function $E(z→)$ representing the energy of the viral population and with $Pz→$:

$$
P(z→)=\frac{e^{−E(z→)}}{z},
$$



$$
E(z→)= \sumi=1mh_{i}(z_{i})+\sumi=1m\sumj=i+1mJ_{ij}(z_{i},z_{j})
$$

where $z→$ is the peptide sequence of length m such that $z→={z_{1,}z_{2},…z_{m}}$ describes individual amino acids in $z→$. $P(z→)$ is the prevalence fitness taken under the assumption that the frequently occurring variants represent the fitter strain (i.e. the common circulating virus, in this case the original T/F virus), and this mathematically defined fitness correlates positively to the actual viral fitness $fz→$ (Ferguson et al., 2013). $Ez→$ is the ‘energy’ of peptide $z→$ a pseudo measurement for fitness, and z is a normalization factor described in the following equation.

$$
z=\sumz_{i={1,0}}e^{−E(z→)}
$$

The parameter $h_{i}z_{i}$ is the contribution of energy of the single amino acid at position i of $z→$. $J_{ij}z_{i},z_{j}$ specifies the energy contribution associated with pairwise interactions between two amino acids in $z→$ at positions i and j. Under the model assumptions, the association between measurement of energy and fitness estimate showed a negative correlation where minimal $E(z→)$ maximizes the logarithm of the viral fitness $log⁡fz→$ (Hart and Ferguson, 2015).

A relative fitness estimate was also calculated for reconstructed haplotypes by normalizing individual fitness estimates with respect to the fitness of the haplotype corresponding to the T/F variant such that the T/F variant will have a fitness of 1.000. These values were used to represent the viral fitness of individual haplotypes to infer viral evolution dynamics with respect to the T/F virus.

This analysis was used to quantify the selection exerted by the host cytotoxic T cell response in driving the evolution of the T/F virus. The analysis also showed the role of specific co-evolving mutations and the identification of epistatic interactions that may determine the evolution of viral fitness and the overall success of the infection.

### Cell lines

Human cell lines, Lenti-XTM 293 T (Takara, Mountain View, CA, USA) and Huh7.5 (Apath, New York, NY, USA) were cultured at 37  °C in a humidified atmosphere containing 5% CO₂, using High Glucose Dulbecco’s Modified Eagle Medium (HG-DMEM; Gibco, Thermo Fisher Scientific, Waltham, MA, USA) supplemented with 10% (v/v) heat-inactivated fetal bovine serum (FBS; Gibco). These cells were authenticated by STR profiling and were confirmed to be mycoplasma negative.

### HCVpp production, infection, and neutralization

As previously described by us, E1E2 glycoproteins were cloned and co-transfected with MLV gag/pol and luciferase vectors in Lenti-X 293 T -cells to produce HCV-pseudo-particles (pp) (Walker et al., 2020; Walker et al., 2019). Briefly, neutralization assays were performed by incubating HCVpp with heat-inactivated plasma for one hour at 37  °C. This mixture was applied directly to Huh-7.5 hepatoma cells (Apath, L.L.C, New York, NY, USA), and incubated for 72 hr after which luciferase activity was measured (Walker et al., 2019). Neutralization of HCVpp was calculated using the formula: % inhibition  = 1 − (inhibited activity)/(‘normal’ activity)×100, after subtraction of negative control (pseudo-particle generated without glycoproteins) RLU, where normal activity is HCVpp incubated with plasma from a healthy donor. The 50% ID50 titer was calculated as the nAb concentration that caused a 50% reduction in RLU for each plasma/HCVpp combination tested in neutralization. All samples were also tested for neutralizing activity on control pseudo-particle VSV-G, to determine that nAbs were HCV E1E2 specific. All data were fitted using non-linear regression plots (GraphPad, Prism).

### Data visualization and statistical analysis

Data visualization for CD8 +T cell analyses was performed using ggplot2 package (Wickham, 2016) in R (R Development Core Team, 2012). Visualization of viral fitness estimates and longitudinal neutralization and CD8 +T cell data was performed using GraphPad Prism version 10.0 for Windows, GraphPad Software, La Jolla California USA (https://www.graphpad.com/). As were comparisons of timing of nAb and CD8 +T cell responses where Wilcoxon matched-pairs signed rank tests were performed. Sequence alignments for highlighter plots were performed on the variants generated here using Geneious Prime 2023 (https://www.geneious.com).
