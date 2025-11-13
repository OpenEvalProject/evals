# A discriminator code–based DTD surveillance ensures faithful glycine delivery for protein biosynthesis in bacteria

## Authors

- Santosh Kumar Kuncha<sup>1</sup> ([ORCID: 0000-0002-2538-8342](https://orcid.org/0000-0002-2538-8342))
- Katta Suma<sup>1</sup> ([ORCID: 0000-0003-4667-8768](https://orcid.org/0000-0003-4667-8768))
- Komal Ishwar Pawar<sup>1</sup> ([ORCID: 0000-0002-1968-9851](https://orcid.org/0000-0002-1968-9851))
- Jotin Gogoi<sup>1</sup> ([ORCID: 0000-0001-6791-6580](https://orcid.org/0000-0001-6791-6580))
- Satya Brata Routh<sup>1</sup>
- Sambhavi Pottabathini<sup>1</sup>
- Shobha P Kruparani<sup>1</sup> ([ORCID: 0000-0002-8955-1647](https://orcid.org/0000-0002-8955-1647))
- Rajan Sankaranarayanan<sup>1</sup> ([ORCID: 0000-0003-4524-9953](https://orcid.org/0000-0003-4524-9953)) †

### Affiliations

1. CSIR–Centre for Cellular and Molecular Biology Hyderabad India
2. Academy of Scientific and Innovative Research CSIR–CCMB Campus Hyderabad India

† Corresponding author

## Abstract

D-aminoacyl-tRNA deacylase (DTD) acts on achiral glycine, in addition to D-amino acids, attached to tRNA. We have recently shown that this activity enables DTD to clear non-cognate Gly-tRNAAla with 1000-fold higher efficiency than its activity on Gly-tRNAGly, indicating tRNA-based modulation of DTD (Pawar et al., 2017). Here, we show that tRNA’s discriminator base predominantly accounts for this activity difference and is the key to selection by DTD. Accordingly, the uracil discriminator base, serving as a negative determinant, prevents Gly-tRNAGly misediting by DTD and this protection is augmented by EF-Tu. Intriguingly, eukaryotic DTD has inverted discriminator base specificity and uses only G3•U70 for tRNAGly/Ala discrimination. Moreover, DTD prevents alanine-to-glycine misincorporation in proteins rather than only recycling mischarged tRNAAla. Overall, the study reveals the unique co-evolution of DTD and discriminator base, and suggests DTD’s strong selection pressure on bacterial tRNAGlys to retain a pyrimidine discriminator code.

## Introduction

Quality control during translation of the genetic code involves multiple stages and a multitude of proofreading factors (Guo and Schimmel, 2012; Ibba and Soll, 2000; Ling et al., 2009; Ogle and Ramakrishnan, 2005). A compromise in editing leads to serious pathologies including neurodegeneration in mouse, and even cell death (Bacher et al., 2005; Bullwinkle et al., 2014; Karkhanis et al., 2007; Korencic et al., 2004; Lee et al., 2006; Liu et al., 2014; Lu et al., 2014; Moghal et al., 2016; Nangle et al., 2002; Roy et al., 2004). Among these proofreading factors, D-aminoacyl-tRNA deacylase (DTD) is the one that specifically decouples wrongly acylated D-amino acids from tRNAs (Calendar and Berg, 1967; Soutourina et al., 1999; 2000). Our studies have shown that DTD is an RNA-based catalyst that uses an invariant Gly-cisPro motif as a ‘chiral selectivity filter’ to achieve substrate chiral specificity only through rejection of L-amino acid from the active site, thereby leading to Gly-tRNAGly misediting (Ahmad et al., 2013; Routh et al., 2016; Routh and Sankaranarayanan, 2017). Recently, we have also shown that DTD’s activity on achiral glycine helps in clearing Gly-tRNAAla, a misaminoacylation product of alanyl-tRNA synthetase (AlaRS), thus resolving a long-standing question in translational quality control (Pawar et al., 2017).

As DTD acts on multiple tRNAs charged with D-amino acids or glycine, tRNA’s role in modulating DTD’s activity was previously thought to be inconsequential (Calendar and Berg, 1967). However, our recent work has shown that DTD’s activity on Gly-tRNAAla is about 1000-fold higher than on Gly-tRNAGly, clearly demonstrating the profound effect of tRNA elements on DTD and suggesting an underlying tRNA code for DTD’s action. G3•U70, the universal tRNAAla-specific determinant for AlaRS, is also a determinant for DTD. However, it enhances DTD’s activity by only about 10-fold (Pawar et al., 2017), leaving the 100-fold difference in activity unaccounted for. Here, using exhaustive tRNA sequence analysis and biochemical studies, we identify tRNA’s discriminator base (N73) as the major modulator of DTD’s activity (unless stated otherwise, DTD refers to bacterial DTD). The invariant uracil (U73) in bacterial Gly-tRNAGly serves as an anti-determinant and enables the substrate’s escape from misediting by DTD, thereby preventing cognate depletion. Using a reporter assay based on green fluorescent protein (GFP), we further demonstrate that DTD is not merely a recycler of Gly-tRNAAla but avoids glycine misincorporation in proteins. Thus, the study has deciphered the tRNA elements that modulate DTD’s activity to ensure faithful delivery of glycine to the ribosomal apparatus during protein biosynthesis. The current work has elucidated why bacterial tRNAGlys—both proteinogenic and non-proteinogenic—have U73 and deviated from harboring purine as N73 during evolution, suggesting for the first time the role of proofreading factors such as DTD in shaping the discriminator base code of tRNAs. The study provides an explanation for a key anomaly in the elegant ‘Discriminator Hypothesis’ originally proposed by Donald Crothers nearly half a century ago (Crothers et al., 1972).

## Results

### U73 is an idiosyncratic feature of bacterial tRNAGly

To identify tRNA elements other than G3•U70 that play a role in modulating DTD’s activity, we performed a thorough bioinformatic analysis of all the available 2,671,763 tRNA sequences, which were retrieved from tRNADB-CE (Abe et al., 2014). Since DTD is known to act even on D-Tyr-tRNATyr digested with T1 RNase (Calendar and Berg, 1967), it is not expected to interact beyond tRNA’s acceptor stem. Therefore, we focused only on the conservation/variation of acceptor stem bases. The obvious difference is the invariable and unique G3•U70 in tRNAAla, while the rest of the acceptor stem paired bases have no striking partitioning between tRNAAla and tRNAGly, except the second base pair (Figure 1b). However, this is not likely to affect DTD’s activity because the second base pair position is not conserved among different tRNAs (e.g., tRNAPhe/Tyr/Trp/Asp) on which DTD is known to act with similar efficiency (Figure 1—figure supplement 1) (Calendar and Berg, 1967; Soutourina et al., 1999; 2000). Surprisingly, bacterial tRNAGly, tRNAHis and tRNACys have a pyrimidine as N73, while the rest of the tRNAs including tRNAAla have a purine at that position (Figure 1a,c; Figure 1—figure supplement 2; Table 1). This indicated that N73 could have a role in the differential activity of DTD on Gly-tRNAGly and Gly-tRNAAla.

![Figure 1.](https://cdn.elifesciences.org/articles/38232/elife-38232-fig1-v2.jpg)

**Figure 1.:** (a) Clover leaf model of tRNA with the discriminator base highlighted in red. (b) Frequency distribution of tRNA acceptor stem elements across bacterial tRNAs, comparing and contrasting between tRNAGly and tRNAAla. Red circle indicates the discriminator base. (c) Distribution of the discriminator base in all tRNAs across the three domains of life. The instances where the discriminator base shows >90% conservation has been represented by the most frequent base. In the case of tRNAThr, U73 and A73 together represent >90% frequency of occurrence; A/U in Bacteria implies A73 is more abundant than U73, whereas U/A in Eukarya denotes U73 is more abundant than A73. Amino acids are color-coded on the basis of the class to which the corresponding synthetases belong: yellow, class I; blue, class II; orange, both class I and II. Discriminator base color-coded as follows: green, purine (A or G); red, pyrimidine (U or C); grey, purine and pyrimidine (A/U or U/A).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/38232/elife-38232-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** The second position is highlighted with a blue star while the discriminator base is marked with a red circle.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/38232/elife-38232-fig1-figsupp2-v2.jpg)

**Table 1.**
 Table showing the number of tRNAs having a particular discriminator base for all tRNAs across bacteria.


<table>
  <thead>
    <tr>
      <th>tRNAX</th>
      <th>A73</th>
      <th>G73</th>
      <th>C73</th>
      <th>U73</th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ala</td>
      <td>136822</td>
      <td>9</td>
      <td>6</td>
      <td>9</td>
      <td>136846</td>
    </tr>
    <tr>
      <td>Ile</td>
      <td>61982</td>
      <td>28</td>
      <td>3</td>
      <td>3</td>
      <td>62016</td>
    </tr>
    <tr>
      <td>Leu</td>
      <td>259624</td>
      <td>13</td>
      <td>9</td>
      <td>5</td>
      <td>259651</td>
    </tr>
    <tr>
      <td>Lys</td>
      <td>123064</td>
      <td>122</td>
      <td>40</td>
      <td>510</td>
      <td>123736</td>
    </tr>
    <tr>
      <td>Met</td>
      <td>207181</td>
      <td>12</td>
      <td>253</td>
      <td>1868</td>
      <td>209314</td>
    </tr>
    <tr>
      <td>Phe</td>
      <td>68315</td>
      <td>20</td>
      <td>2</td>
      <td>4</td>
      <td>68341</td>
    </tr>
    <tr>
      <td>Pro</td>
      <td>110670</td>
      <td>9</td>
      <td>1</td>
      <td>3</td>
      <td>110683</td>
    </tr>
    <tr>
      <td>Tyr</td>
      <td>80595</td>
      <td>5</td>
      <td>6</td>
      <td>50</td>
      <td>80656</td>
    </tr>
    <tr>
      <td>Val</td>
      <td>187250</td>
      <td>10</td>
      <td>7</td>
      <td>3</td>
      <td>187270</td>
    </tr>
    <tr>
      <td>Arg</td>
      <td>119819</td>
      <td>103052</td>
      <td>32</td>
      <td>10151</td>
      <td>233054</td>
    </tr>
    <tr>
      <td>Glu</td>
      <td>29469</td>
      <td>54764</td>
      <td>8</td>
      <td>46</td>
      <td>84287</td>
    </tr>
    <tr>
      <td>Asn</td>
      <td>20</td>
      <td>129816</td>
      <td>6</td>
      <td>41</td>
      <td>129883</td>
    </tr>
    <tr>
      <td>Asp</td>
      <td>17</td>
      <td>121556</td>
      <td>1</td>
      <td>3</td>
      <td>121577</td>
    </tr>
    <tr>
      <td>Gln</td>
      <td>787</td>
      <td>102405</td>
      <td>6</td>
      <td>2250</td>
      <td>105448</td>
    </tr>
    <tr>
      <td>Ser</td>
      <td>1336</td>
      <td>192697</td>
      <td>6</td>
      <td>3119</td>
      <td>197158</td>
    </tr>
    <tr>
      <td>Trp</td>
      <td>5</td>
      <td>54387</td>
      <td>0</td>
      <td>23</td>
      <td>54415</td>
    </tr>
    <tr>
      <td>Thr</td>
      <td>131288</td>
      <td>34</td>
      <td>95</td>
      <td>28854</td>
      <td>160271</td>
    </tr>
    <tr>
      <td>Cys</td>
      <td>5</td>
      <td>2</td>
      <td>8</td>
      <td>56956</td>
      <td>56971</td>
    </tr>
    <tr>
      <td>Gly</td>
      <td>239</td>
      <td>11</td>
      <td>4</td>
      <td>231855</td>
      <td>232109</td>
    </tr>
    <tr>
      <td>His</td>
      <td>2004</td>
      <td>4</td>
      <td>56052</td>
      <td>17</td>
      <td>58077</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td colspan="3">Total bacterial tRNAs:</td>
      <td>2,671,763</td>
    </tr>
  </tbody>
</table>

### Pyrimidine as N73 acts as an anti-determinant for DTD

To test the role of N73 in modulating DTD’s activity, we generated U73A, U73G and U73C mutants of tRNAGly from Escherichia coli. Strikingly, biochemical assays showed that DTD from E. coli (EcDTD) deacylates Gly-tRNAGly(U73A) or Gly-tRNAGly(U73G) at 0.1 nM, whereas it shows similar activity on Gly-tRNAGly at 10 nM (Figure 2a,c,d). Thus, EcDTD has nearly 100-fold higher activity on Gly-tRNAGly(U73A) or Gly-tRNAGly(U73G) compared to its activity on the wild-type substrate. In the case of Gly-tRNAGly(U73C), EcDTD’s activity at 10 nM is similar to that on Gly-tRNAGly at the same concentration, thus displaying comparable efficiencies for both substrates (Figure 2a,b). This clearly demonstrates that N73 is a key element on tRNA that dictates the efficiency of DTD, and purine as N73 is the preferred base for the enzyme. Our data is further strengthened by the fact that all the reported substrates of DTD, namely D-Tyr-tRNATyr, D-Phe-tRNAPhe, D-Trp-tRNATrp and D-Asp-tRNAAsp, have purine as N73 (Figure 1c; Figure 1—figure supplement 1) (Calendar and Berg, 1967; Soutourina et al., 1999; 2000). This also shows that N73 has a stronger influence on DTD than G3•U70 (which creates only about 10-fold difference) and it can majorly account for the observed 1000-fold difference in DTD’s activity on Gly-tRNAGly and Gly-tRNAAla (Pawar et al., 2017). This further prompted us to test the combined effect of N73 and G3•U70 on DTD’s activity.

![Figure 2.](https://cdn.elifesciences.org/articles/38232/elife-38232-fig2-v2.jpg)

**Figure 2.:** (a–e) Deacylation of Gly-tRNAGly and its mutants by various concentrations of EcDTD. (f) Deacylation of Gly-tRNAAla by various concentrations of EcDTD. Lines indicate exponential decay fits and error bars represent one standard deviation from the mean of at least three independent readings.

### N73 and G3•U70 have an additive effect on DTD’s activity

To ascertain whether N73 and G3•U70 are mutually independent such that they can have a cumulative effect on DTD’s activity, we generated U73A/C70U double mutant of tRNAGly. Biochemical assays showed that EcDTD’s activity on Gly-tRNAGly(U73A/C70U) at 0.01 nM is comparable to that on Gly-tRNAAla, and is nearly 1000-fold higher than its activity on wild-type Gly-tRNAGly (Figure 2a,e,f). This unambiguously proves the additive effect of N73 and G3•U70 in modulating bacterial DTD’s activity, wherein N73 plays the major role. More importantly, it shows that just two point mutations in the acceptor stem are necessary and sufficient to completely switch the specificity of tRNAGly to tRNAAla, one which is an anti-determinant in tRNAGly and the other a positive determinant in tRNAAla. These results also clearly establish that functionally important interactions of DTD are confined only to the acceptor stem of tRNA.

### U73 is the key factor that prevents Gly-tRNAGly misediting by DTD

Our previous work had shown that elongation factor thermo unstable (EF-Tu) confers protection on Gly-tRNAGly from DTD’s unwarranted activity (Routh et al., 2016). tRNA elements on TΨC arm are known to be responsible for EF-Tu binding (LaRiviere et al., 2001; Sanderson and Uhlenbeck, 2007a; Schrader et al., 2009). Hence, N73 mutation in tRNAGly is not expected to alter the binding affinity of Gly-tRNAGly to EF-Tu. Moreover, since the effect of U73 as anti-determinant of DTD seen here appeared stronger than the protective effect of EF-Tu observed earlier (Routh et al., 2016), we hypothesized that N73 plays the dominant role in preventing misediting of Gly-tRNAGly by DTD. We probed this by performing competition experiments between EF-Tu and EcDTD. In the absence of EF-Tu, EcDTD acts on Gly-tRNAGly at 10 nM, while the presence of EF-Tu protects Gly-tRNAGly from 10 nM EcDTD. The substrate is, however, completely deacylated by 100 nM EcDTD even in the presence of EF-Tu. Thus, the protection offered by EF-Tu to Gly-tRNAGly against EcDTD is less than 10-fold (Figure 3a), which is in agreement with our previous study (Routh et al., 2016).

![Figure 3.](https://cdn.elifesciences.org/articles/38232/elife-38232-fig3-v2.jpg)

**Figure 3.:** Deacylation of (a) Gly-tRNAGly and (b) Gly-tRNAGly(U73A) by EcDTD in the presence or absence of EF-Tu (* indicates the data points are connected through line). Deacylation of (c) Gly-(Mm)tRNAGly and (d) Gly-(Mm)tRNAAla by various concentrations of MmDTD. Deacylation of (e) Gly-tRNAGly and (f) Gly-tRNAGly(U73A) by various concentrations of MmDTD. Lines indicate exponential decay fit and error bars represent one standard deviation from the mean of at least three independent readings.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/38232/elife-38232-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Tris pH nine is used as deacylation control.

In the case of Gly-tRNAGly(U73A), EcDTD’s activity without EF-Tu is at 0.1 nM, while in the presence of EF-Tu, similar activity is observed at 1 nM (Figure 3b). Hence, irrespective of the identity of N73, EF-Tu offers only about 10-fold protection. Furthermore, the 100-fold difference in the activity of EcDTD on Gly-tRNAGly(U73A) and wild-type Gly-tRNAGly is maintained even in the presence of EF-Tu. These findings clearly demonstrate that EF-Tu has no preference for N73, and it is DTD’s differential activity that predominantly determines the fate of the substrate. Thus, EF-Tu augments the protection of Gly-tRNAGly primarily/majorly conferred by U73, that is the enhancement in protection of Gly-tRNAGly by EF-Tu is consequential only if the substrate harbors U73. Nevertheless, cellular DTD levels must be tightly regulated because DTD overexpression has been shown to cause toxicity (Routh et al., 2016). While the above data indicated the role of DTD in depleting the cognate Gly-tRNAGly pool, it did not provide direct evidence to that effect. We therefore performed northern blotting analysis by overexpressing the wild-type and a catalytically inactive mutant of DTD (A112F) (Ahmad et al., 2013), and monitoring the aminoacylated and free tRNAGly levels. In case of mutant DTD overexpression, the aminoacylated fraction is about 80% of the total tRNAGly pool which is similar to empty vector control. By contrast, overexpression of wild-type DTD causes complete depletion of Gly-tRNAGly. Interestingly, cognate depletion is observed even in the uninduced sample of wild-type DTD, suggesting leaky expression of the wild-type copy from the recombinant plasmid (Figure 3—figure supplement 1). These data are suggestive that the toxicity caused by DTD overexpression is linked to the depletion of cellular Gly-tRNAGly levels.

### G3•U70 is a universal determinant for DTD

Intriguingly, our bioinformatic analysis also revealed that the dichotomy of N73 seen in bacterial tRNAGly and tRNAAla is lacking in Archaea and Eukarya, that is both tRNAGly and tRNAAla in Archaea and Eukarya harbor A73 (Figure 1c). Thus, we envisaged that the difference in eukaryotic DTD’s activity on eukaryotic Gly-tRNAGly and Gly-tRNAAla will be only about 10-fold due to G3•U70 in tRNAAla (notably, Archaea lacks canonical DTD and hence the problem of discrimination does not arise at all). To investigate this paradigm, we used DTD and tRNAs from Mus musculus (MmDTD and (Mm)tRNAGly/Ala). Biochemical assays revealed that MmDTD acts on Gly-(Mm)tRNAGly and Gly-(Mm)tRNAAla at 100 nM and 10 nM, respectively (Figure 3c,d). These results clearly show that G3•U70 recognition by DTD is conserved even in Eukarya, contributing about 10-fold discrimination between eukaryotic tRNAGly and tRNAAla. They also demonstrate that G3•U70 is the only available tRNA element that enables distinction between eukaryotic tRNAGly and tRNAAla by eukaryotic DTD. These findings further suggest that other mechanisms are possibly operating in eukaryotes to enhance the discrimination between Gly-tRNAGly and Gly-tRNAAla, as discussed later.

### Eukaryotic DTD has inverted N73 specificity

The lack of N73 difference in eukaryotic tRNAGly and tRNAAla further prompted us to investigate whether eukaryotic DTD has lost the specificity for N73. To probe the N73 effect on eukaryotic DTD, we performed biochemical assays using MmDTD and Gly-(Ec)tRNAGly. MmDTD acts on U73-containing wild-type Gly-(Ec)tRNAGly at a concentration of 0.1 nM while it acts on Gly-(Ec)tRNAGly(U73A) mutant with comparable efficiency at a concentration of 10 nM, thus displaying a 100-fold reduction in activity compared to the wild-type substrate (Figure 3e,f). The data indicate that N73 does affect eukaryotic DTD but the specificity/preference has switched from purine to pyrimidine. Therefore, eukaryotic DTD is equally modulated by N73 like its bacterial counterpart, but has inverted N73 specificity, that is bacterial DTD prefers purine while eukaryotic DTD prefers pyrimidine as N73; this provides a rationale as to why a mild overexpression of eukaryotic DTD from Plasmodium falciparum (PfDTD; eukaryotic DTD) creates more cellular toxicity when compared to that of EcDTD (Routh et al., 2016). These findings clearly establish that eukaryotic DTD has also co-evolved with N73 like bacterial DTD, thereby helping to relieve the selection pressure of keeping U/C73 in eukaryotic tRNAGly, as further explained later. Nevertheless, since none of the U/C73-containing eukaryotic tRNAs (Figure 1c) is known to be mischarged with glycine or corresponding D-amino acids, the physiological consequence of this switch in N73 specificity remains to be elucidated.

### DTD prevents glycine misincorporation in proteins in vivo

One of the major questions that came out of our recent work (Pawar et al., 2017) was whether DTD is just a ‘recycler’ of mischarged tRNAs, as has been shown in the case of D-aminoacyl-tRNAs (Soutourina et al., 2004). D-aminoacyl-tRNAs are discriminated against by other cellular ‘chiral checkpoints’, namely EF-Tu and ribosome (Bhuta et al., 1981; Englander et al., 2015; Pingoud and Urbanke, 1980; Yamane et al., 1981), which together with DTD preclude D-amino acid infiltration into the translational machinery. Since Gly-tRNAAla is not expected to be adequately distinguished from L-Ala-tRNAAla by EF-Tu and ribosome (Dale et al., 2004), we hypothesized that glycine mischarged on tRNAAla can be misincorporated into the growing polypeptide chain in the absence of DTD, and that DTD’s efficient activity on Gly-tRNAAla due to the presence of A73 and G3•U70 prevents this deleterious outcome. To test this hypothesis in vivo, we developed a GFP-based reporter assay (Figure 4a). The ability of GFP to fluoresce depends on a key motif (65S/TYG67) in which mutation of the invariant glycine to any other residue abrogates chromophore formation, resulting in complete loss of fluorescence (Tsien, 1998; Zimmer, 2002). We expressed the non-fluorescing G67A mutant of GFP in an E. coli strain with/without DTD in the editing-defective AlaRS background (Pawar et al., 2017). While no GFP fluorescence is observed in cells with the genomic copy of dtd gene (Figure 4b), the dtd knockout strain shows GFP fluorescence upon glycine supplementation, clearly indicating misincorporation of glycine in place of alanine (Figure 4c). Moreover, the increase in fluorescence with increasing glycine supplementation in the dtd-null E. coli strain substantiates the increased toxicity upon glycine supplementation observed in our recent study (Pawar et al., 2017). These data clearly reveal that DTD is not merely a ‘recycler’ of Gly-tRNAAla, but prevents alanine-to-glycine misincorporation in proteins and consequent cellular toxicity because A73 and G3•U70 in the substrate enable efficient editing by the enzyme.

![Figure 4.](https://cdn.elifesciences.org/articles/38232/elife-38232-fig4-v2.jpg)

**Figure 4.:** (a) GFP-based fluorescence reporter assay for visualizing alanine-to-glycine mistranslation, wherein the mutant GFP G67A (65TYA67) will fluoresce only when TYA is mistranslated to TYG. Microscopy images showing GFP fluorescence in E. coli at different concentrations of glycine supplementation (b) in the presence and (c) in the absence of DTD. The E. coli strain used is MG1655 with editing-defective AlaRS gene (i.e. ΔalaS) (Pawar et al., 2017). (d) Model showing N73 dichotomy in bacterial tRNAGly and tRNAAla, enabling protection of the cognate Gly-tRNAGly (both proteinogenic and non-proteinogenic) predominantly by U73, while effecting efficient removal of the non-cognate Gly-tRNAAla (having A73 and G3•U70) to prevent alanine-to-glycine mistranslation.

## Discussion

The present work has identified N73 as the major factor that modulates DTD’s activity. The invariant U73, which acts as an anti-determinant, is predominantly responsible for ensuring the escape of Gly-tRNAGly from DTD’s unwarranted activity. Strikingly, this protection is essential and significantly higher than that offered by EF-Tu. Notably, EF-Tu’s role in conferring protection on Gly-tRNAGly holds significance only when the substrate contains U73. Such a strong influence of U73 assumes even more importance for non-proteinogenic Gly-tRNAGly, which are required for non-canonical functions (e.g., cell wall synthesis in Gram-positive bacteria) but are not known to interact with EF-Tu or any other protein, except the enzymes (like FemXAB) that utilize it (Giannouli et al., 2009; Katz et al., 2016). For this achiral species, U73 is the only means of preventing misediting by DTD and consequent cognate depletion. Interestingly, we have now shown that just two tRNA elements—N73 and G3•U70—are sufficient to completely switch DTD’s tRNA specificity, thus accounting for the enzyme’s 1000-fold difference in activity on Gly-tRNAGly and Gly-tRNAAla. G3•U70 wobble base pair in the acceptor stem of tRNAAla is a universal determinant for AlaRS specificity (Beebe et al., 2008; Hou and Schimmel, 1988; McClain and Foss, 1988). This specificity is so strict that G•U at the third base pair position, or in certain cases even at the fourth base pair level, can result in AlaRS charging non-cognate tRNAs with L-alanine (Kuncha et al., 2018; Sun et al., 2016). We have further shown that G3•U70-based discrimination between tRNAGly and tRNAAla by DTD is also conserved in Eukarya. These findings unequivocally demonstrate the obligatory requirement for DTD to use tRNA elements in a major way to discriminate between two cellular substrates, one essential for protein synthesis and the other a misaminoacylated species, carrying the same amino acid, that is achiral glycine. Moreover, the study has also suggested that the high efficiency of bacterial DTD in clearing Gly-tRNAAla is the plausible reason why it shows significant activity on Gly-tRNAGly, albeit at a 1000-fold less efficiency. This points towards an interesting trade-off between speed and accuracy that exists in the case of DTD’s proofreading activity, thereby making DTD uniquely distinct from all other known editing enzymes. It further conforms to the notion that DTD levels in the cell must be tightly regulated.

Surprisingly, our in silico analysis has revealed that eukaryotic tRNAGly and tRNAAla both contain A73. The lack of N73 difference indicates that G3•U70 is the only discriminatory factor for eukaryotic DTD. It also suggests that in eukaryotes other mechanisms such as spatiotemporal regulation of expression and cellular compartmentalization of DTD may play role in preventing cognate (Gly-tRNAGly) depletion. It is worth mentioning in this context that human DTD has been shown to be enriched in the nuclear envelope region (Zheng et al., 2009). Intriguingly enough, our data have revealed that eukaryotic DTD shows a switch in N73 specificity, that is unlike bacterial DTD, the eukaryotic enzyme prefers pyrimidine. However, the physiological relevance of this specificity switch in eukaryotic DTD remains to be elucidated. Moreover, whether such a tRNA-based discriminatory code exists for other standalone proofreading modules such as AlaXs, YbaK and ProXp-ala remains to be probed. Interestingly, such an acceptor stem based tRNA determinants has been shown to exist for other standalone proofreading modules also such as AlaXs, YbaK and ProXp-ala (Bacusmo et al., 2017; Beebe et al., 2008; Das et al., 2014; Vargas-Rodriguez and Musier-Forsyth, 2013). These findings also suggest that bacterial DTD and A/G73-containing tRNAGly or eukaryotic DTD and U/C73-containing tRNAGly are likely to be incompatible. This can be seen from the delicate balance of the cellular concentrations of DTD and the deleterious effect of its overexpression in E. coli (Routh et al., 2016).

The uneven, yet interesting, distribution of tRNAs into different discriminator classes based on N73 was used to propose an elegant ‘Discriminator Hypothesis’ by Donald Crothers about 50 years ago (Crothers et al., 1972). This classification also reflects the partitioning of tRNAs based on the chemical nature of the amino acid to be attached, that is A73 class includes tRNAs which code for hydrophobic amino acids, while G73-containing tRNAs code for hydrophilic amino acids (Crothers et al., 1972). As can be seen from our current bioinformatic analysis on the discriminator code usage from all three branches of life (Figure 1c), N73 is predominantly a purine. It has been already noted that factors like RNase P and CCA-adding enzyme have led to purine bias in N73 in all the three domains of life (Figure 1c) (Burkard et al., 1988; Connolly et al., 2004; Giegé et al., 1998; Hamann and Hou, 1995; Hou et al., 2001; Puglisi et al., 1994; Wende et al., 2015). In the case of bacteria, the only variations to the purine-based discriminator code are tRNAGly/His/Cys. C73 in prokaryotic tRNAHis is essential to retain G-1 during processing by RNaseP, while in the case of eukaryotic tRNAHis, G-1 is added latter as a post-transcriptional modification (Burkard et al., 1988; Connolly et al., 2004). In tRNACys, U73 is essential for aminoacylation by cysteinyl-tRNA synthetase (Hamann and Hou, 1995). Recent evidence shows that CCA-adding enzyme prefers purine as N73 because pyrimidine at that position leads to slow addition of CCA as well as a compromise in the fidelity of CCA addition (Wende et al., 2015). The above examples in conjunction with the current day discriminator code usage (Figure 1c) clearly demonstrate that a stronger selection pressure is required to deviate from a purine-based discriminator code. Therefore, it was striking that the tRNA coding for an amino acid which is achiral, having no side chain and of primordial origin is the only bacterial tRNA containing U73 which remained a major anomaly to the discriminator code. The current study has elucidated this hitherto unexplained case of bacterial tRNAGly, wherein the evolutionary selection pressure exerted by DTD for retention of U73 appears stronger than that exerted by any of the other aforesaid factors. It also suggests that eukaryotes have evolved mechanisms that helped in relieving the selection pressure of keeping U73 in tRNAGly, and eukaryotic DTD has co-evolved to switch its N73 specificity accordingly.

Taken together, the present work has added a new dimension to DTD’s substrate selectivity, highlighting the role of two key tRNA elements, namely N73 and the G3•U70 wobble base pair. In this respect, it would be interesting to probe the mechanistic underpinnings for DTD’s recognition mode using both bacterial and eukaryotic systems to help us understand the underlying cause of switch in N73 specificity. Furthermore, the current study has underscored the physiological importance of N73 dichotomy in tRNAGly and tRNAAla that maintains ‘glycine fidelity’ during translation of the genetic code in Bacteria by preventing misediting of Gly-tRNAGly as well as misincorporation of glycine in proteins (Figure 4d). In the latter context, therefore, DTD is not just a recycler of Gly-tRNAAla, unlike its role in recycling D-aminoacyl-tRNAs (Soutourina et al., 2004). The work has brought to the fore the evolutionary selection pressure that the chiral proofreading enzyme has exerted on bacterial tRNAGly to retain U73. In the primordial scenario, U73 could have been the only factor that ensured utilization of glycine for protein synthesis by precluding the unwarranted activity of DTD-like factor. Our findings have also revealed the co-evolution of eukaryotic DTD via switching of N73 specificity as this selection pressure was released through unknown mechanisms during the 1.5 billion years of evolutionary transition from bacteria to eukaryotes. The study has therefore brought to limelight the deviations that occur in the usage of discriminator base—rare choices of pyrimidine instead of purine—in tRNAs across all life forms, and the need to probe the physiological necessity to deviate from it (Figures 1c and 4d). Considering the possibility that the early tRNAs operated using an acceptor stem–based ‘second genetic code’ or with mini-helices (Buechter and Schimmel, 1993; Schimmel et al., 1993), the choice of discriminator base must have played a crucial role during the early evolution of the translational apparatus.

## Materials and methods

### Cloning, expression and purification

The genes encoding E. coli DTD and Thermus thermophilus EF-Tu, and cDNA encoding M. musculus (residues 1–147) were cloned (with C-terminal 6X His-tag), expressed and purified as mentioned in Ahmad et al. (2013) and Kuncha et al. (2018). Briefly the proteins were overexpressed in E. coli BL21(DE3) by growing the culture to 0.6 OD600 at 37°C, followed by induction using 0.5 mM IPTG for 12 hr at 18°C. The cells were harvested by centrifugation at 8000 rpm for 10 min. The harvested cells were lysed and the supernatant was subjected to two-step purification involving affinity-based chromatography followed by size exclusion chromatography (SEC). Affinity purification was done using Ni-NTA column in a solution containing 250 mM NaCl and 100 mM Tris pH 8.0. Imidazole gradient from 10 mM to 500 mM was used to elute the bound protein. Affinity-purified protein was further subjected to SEC to achieve improved purity and homogeneity in a buffer containing 200 mM NaCl and 100 mM Tris pH 7.5. These purified proteins were quantified and stored at −30°C in a buffer containing 50% glycerol. Same procedure was followed for all the proteins except MmDTD which was expressed in E. coli BL21-CodonPlus(DE3)-RIL strain.

### Biochemical assays

tRNAs were generated by in vitro transcription of genes encoding E. coli tRNAGly/Ala and M. musculus tRNAGly/Ala using MEGAshortscript T7 Transcription Kit (Thermo Fisher Scientific, USA). Various mutants of tRNAGly were generated using QuickChange XL Site-Directed Mutagenesis Kit (Agilent Technologies, USA). The in vitro transcribed tRNAs were 3′ end labelled using CCA-adding enzyme (Ledoux and Uhlenbeck, 2008). Glycylation of tRNAGly and mutants of tRNAGly (U73A, U73G, U73C, U73A/C70U) were done using T. thermophilus glycyl-tRNA synthetase, while tRNAAla was glycylated using E. coli AlaRS as explained in Pawar et al. (2017). Deacylation assays and EF-Tu protection experiments were performed according to the protocol explained in Pawar et al. (2017). Briefly, deacylation was carried out, in 20 mM Tris pH 7.2, 5 mM dithiothreitol (DTT), 20 mM MgCl2, 0.2 µM of substrate (aminoacylated tRNA), at 30°C with variable concentrations of DTD. EF-Tu activation is done in buffer containing 50 mM HEPES pH 7.2, 20 mM MgCl2, 250 mM NH4Cl, 5 mM DTT, 3 mM phosphoenol pyruvate and pyruvate kinase as explained in Routh et al., 2016. EF-Tu protection assays were performed in a buffer containing 2 µM T. thermophilus EF-Tu’s (of which usually 10–15% is activated (Cvetesic et al., 2013; Sanderson and Uhlenbeck, 2007a), hence EF-Tu effective concentration is 200–300 nM), 100 mM HEPES pH 7.2, 2.5 mM DTT and variable concentrations of DTD (determined by Bradford assay). A range of enzyme (DTD) concentrations were tested, and, in general, the concentration that gave a gradual deacylation curve was selected for comparison and reporting. GraphPad Prism software was used for curve fitting and every data point represents mean of at least three independent readings. Error bars indicate one standard deviation from the mean.

### Northern blotting

Northern blotting was performed according to the protocol given in Varshney et al., 1991. Briefly, 1% of overnight-grown 2 mL primary culture (E. coli MG1655Δdtd::Kan cells overexpressing PfDTD wild-type or A112F mutant) was used to initiate 10 mL secondary culture and grown at 37°C till OD600 reached 0.6, following which the culture was induced with 0.1 mM IPTG and allowed to grow at 37°C for additional 5–6 hr. The culture was harvested and total RNA was extracted using the general acidic phenol–based method; all the steps were carried out on ice or at 4°C. This was followed by running the total RNA (0.15–0.25 A260 unit) on 6.5% acid–urea PAGE at 4°C for 20–24 hr. The RNA from the gel was electroblotted on Hybond+ membrane at 15 V, 3 A for 25 min, and tRNAGlyGCC was hybridized with [32P]-labeled probe (probe sequence: 5′-AGCGGGAAACGAGACTCGAACTCGC-3′). The probe was labeled using [γ-32P]-ATP in a general polynucleotide kinase reaction. The signal from the probe was recorded overnight on image plate and quantified using phosphoimager.

### Strain construction

Wild-type GFP (pBAD18-sfGFP) was a kind gift from Dr. Manjula Reddy’s laboratory. Non-fluorescing mutant of GFP was generated by introducing a glycine-to-alanine point mutation at the 67th position (sfGFP-G67A). Editing-defective alaS E. coli MG1655 strain (i.e. ΔalaS) was created by knocking out the genomic copy of alaS and complementing it with triple-mutant (T567F/S587W/C666F) AlaRS gene cloned in pBAD33 vector. The same strategy of making AlaRS editing-deficient was also used in Δdtd E. coli MG1655 strain, thereby creating dtd-null strain in AlaRS editing-defective background (i.e. ΔdtdΔalaS) (Pawar et al., 2017). sfGFP and sfGFP-G67A, cloned in pBAD18 vector, were under the control of an arabinose-inducible promoter.

### Microscopy

To monitor GFP fluorescence in ΔalaS (ΔalaS/para::alaS-T567F, S587W, C666F) and ΔdtdΔalaS (Δdtd, ΔalaS/para::alaS-T567F, S587W, C666F) strains were co-expressed with mutant GFP (pBAD18-GFP G67A). Primary cultures were grown at 37°C in LB medium containing 0.002% L-arabinose, 100 mg ml−1 ampicillin and 20 μg ml−1 chloramphenicol. 3% inoculum was used to initiate 5 mL secondary culture in 1X minimal salts with 0.2% maltose as carbon source and 0.002% L-arabinose; the secondary culture was supplemented with 0, 3, 10 or 60 mM glycine. Cells were immobilized on a thin agarose (1.5%) slide and visualized under a Zeiss Axioimager microscope in DIC (Nomarski optics) and EGFP (Fluorescence) mode. All the experiments were done in biological triplicates.

### Bioinformatic analysis

The prokaryotic tRNA sequences were analyzed using the tRNADB-CE (Abe et al., 2014). The numbers were derived using advance pattern search option, wherein anticodon sequence and the 73NCCA76 were used as the search parameters and the rest were set to default. While eukaryotic tRNAs were retrieved from GtRNAdb (http://gtrnadb.ucsc.edu/), only those sequences whose tRNA-scan score is above 50 were considered for analysis. The consensus sequence logo was obtained by using WebLogo server (http://weblogo.berkeley.edu/logo.cgi).
