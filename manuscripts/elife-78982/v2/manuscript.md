# Conformational fingerprinting of allosteric modulators in metabotropic glutamate receptor 2

## Authors

- Brandon Wey-Hung Liauw<sup>1</sup> ([ORCID: 0000-0002-6186-7092](https://orcid.org/0000-0002-6186-7092))
- Arash Foroutan<sup>1</sup>
- Michael R Schamber<sup>1</sup>
- Weifeng Lu<sup>1</sup>
- Hamid Samareh Afsari<sup>1</sup> ([ORCID: 0000-0002-5839-4765](https://orcid.org/0000-0002-5839-4765)) †
- Reza Vafabakhsh<sup>1</sup> ([ORCID: 0000-0001-8384-3203](https://orcid.org/0000-0001-8384-3203)) †

### Affiliations

1. Department of Molecular Biosciences, Northwestern University Evanston United States ([ROR:000e0be47](https://ror.org/000e0be47))

† Corresponding author

## Abstract

Activation of G protein-coupled receptors (GPCRs) is an allosteric process. It involves conformational coupling between the orthosteric ligand binding site and the G protein binding site. Factors that bind at non-cognate ligand binding sites to alter the allosteric activation process are classified as allosteric modulators and represent a promising class of therapeutics with distinct modes of binding and action. For many receptors, how modulation of signaling is represented at the structural level is unclear. Here, we developed fluorescence resonance energy transfer (FRET) sensors to quantify receptor modulation at each of the three structural domains of metabotropic glutamate receptor 2 (mGluR2). We identified the conformational fingerprint for several allosteric modulators in live cells. This approach enabled us to derive a receptor-centric representation of allosteric modulation and to correlate structural modulation to the standard signaling modulation metrics. Single-molecule FRET analysis revealed that a NAM (egative allosteric modulator) increases the occupancy of one of the intermediate states while a positive allosteric modulator increases the occupancy of the active state. Moreover, we found that the effect of allosteric modulators on the receptor dynamics is complex and depend on the orthosteric ligand. Collectively, our findings provide a structural mechanism of allosteric modulation in mGluR2 and suggest possible strategies for design of future modulators.

## Introduction

G protein-coupled receptors (GPCRs) are the largest family of membrane receptors in humans and are key drug targets due to their role in nearly all physiological processes (Dorsam and Gutkind, 2007; Thal et al., 2018). Compounds that bind to the defined, endogenous ligand binding pocket in GPCRs are called orthosteric ligands. Many such orthosteric agonists or antagonists have been developed as successful therapies (Lindsley et al., 2016). Despite this success, achieving target specificity in closely related receptors has been a long-standing challenge due to high conservation of the orthosteric binding site. Moreover, tolerability and safety of orthosteric drugs in therapeutic applications have been difficult to achieve for some GPCRs (Lindsley et al., 2016).

Recently, allosteric modulators have emerged as a promising class of therapeutic compounds for fine-tuning physiological response of GPCRs with high receptor specificity and pathway specificity. Allosteric modulators bind to allosteric sites which are structurally distinct from the orthosteric pocket, to indirectly tune the response to the orthosteric ligand (Foster and Conn, 2017). Major advances in design, synthesis, and screening of small molecule compounds have produced multiple selective and potent allosteric modulators for many GPCRs (Lindsley et al., 2016). In addition, improvements in techniques for measuring GPCR activity have helped reveal the complex pharmacological properties of allosteric modulators (Christopoulos, 2014; Leach and Gregory, 2017) such as probe and cell-type context dependence (Sengmany et al., 2019), biased allosteric agonism, and biased modulation (Makita et al., 2007; Sengmany et al., 2017). Generally, functional characterization of allosteric modulators is done using assays that quantify changes at specific steps of the signaling cascade, downstream of receptor, such as intracellular Ca2+ levels, IP1 accumulation, cellular cAMP levels, ERK1/2 phosphorylation levels, or using energy transfer methods to quantify dissociation of signaling proteins. Collectively, these approaches have provided a pharmacological framework for characterizing and profiling allosteric modulators. However, as functional assays measure the effect of modulators downstream of the receptor, they are unable to provide direct mechanistic insight on allosteric modulation at the receptor level.

Advances in methods for structure determination of membrane proteins have yielded atomic structures of many GPCRs bound to different allosteric modulators and provided insight into different ligand binding modalities and distinct modulator-induced conformations (Bueno et al., 2020; Kruse et al., 2013; Liu et al., 2019; Seven et al., 2021; Shaye et al., 2020; Srivastava et al., 2014). However, despite these advances, for many receptors, structures of only a small subset of receptor-modulator combinations have been determined. Moreover, receptor activation and modulation are dynamic processes, and dynamic information is not achievable by structural representations alone. While progress has been made toward understanding the dynamics of allosteric modulation in class A GPCRs (Gentry et al., 2015; Thal et al., 2018; Wootten et al., 2013), more comprehensive mechanisms, especially for large multi-domain GPCRs, are lacking.

Among all GPCRs, the class C GPCRs are distinct as they are structurally modular, possessing a large extracellular domain and functioning as obligate dimers. Notably, the orthosteric ligand-binding site that is typically found within the 7 transmembrane (7TM) domain bundle in class A GPCRs is in the extracellular Venus flytrap (VFT) domain of class C GPCRs. The VFT domain is linked to the 7TM domain via the cysteine-rich domain (CRD) which is a semi-rigid linker domain. Thus, receptor activation is inherently an allosteric process that involves inter-subunit and inter-domain cooperativity. In the class C family, metabotropic glutamate receptors (mGluRs) are responsible for mediating the slow neuromodulatory effects of glutamate to tune synaptic excitability and transmission (Niswender and Conn, 2010; Pin and Bettler, 2016), making them promising therapeutic targets for treating a range of neurological and psychiatric disorders (Conn et al., 2009; Foster and Conn, 2017; Mantas et al., 2022). Based on structural (Doré et al., 2014; Du et al., 2021; Seven et al., 2021; Wu et al., 2014) and mutagenesis (Farinha et al., 2015; Gregory and Conn, 2015; Lundström et al., 2011) studies, the primary mGluR allosteric binding sites were determined to be located within the 7TM domain bundles. Previous work examining allosteric modulation of mGluR conformational dynamics generally used ensemble methods and was focused on the dimeric rearrangement of either the 7TM domain (Gutzeit et al., 2019; Nasrallah et al., 2021) or the extracellular ligand-binding domain (Cao et al., 2021). While these studies of individual domains provide insights into how allosteric modulators affect mGluR structure and dynamics, they are not conducive for the broader fingerprinting of the modulator effect across multiple domains of the receptor. Specifically, how key pharmacological parameters such as efficacy and potency of different orthosteric and allosteric ligands are manifested structurally at different domains, and how positive and negative allosteric modulators achieve their modulatory effect through modifying the receptor’s energy landscape are not known.

Here, we used live-cell fluorescence resonance energy transfer (FRET) and single-molecule FRET (smFRET) imaging with non-perturbing site-specific labeling, to explicitly examine and quantify the effects of orthosteric agonists and allosteric modulators on mGluR2 conformation and dynamics at the three structural domains of the receptor (Figure 1A). Comparing live-cell imaging results between the domains, we found that the effect of positive or negative allosteric modulators is represented at every domain of the receptor but to different levels. The effect of modulators on the glutamate efficacy and potency as quantified by the compaction and rearrangement at each receptor domain via the FRET sensors matches with the known functional classification of the compounds. Interestingly, positive allosteric modulators (PAMs) generally increased glutamate efficacy to a greater extent when measured at the CRD and 7TM domains compared to the VFT domain. A similar trend was observed for orthosteric agonists. Our results illustrate that the conformation of the CRD and 7TM domain are more accurate metrics for quantifying ligand efficacy than that of the VFT domain, possibly due to the loose conformational coupling between mGluR2 domains (Grushevskyi et al., 2019; Liauw et al., 2021). Further examination of the CRD sensor by smFRET revealed that the PAM compound BINA biases more compact intermediate CRD conformations even in the absence of glutamate and reduces the intrinsic CRD dynamics in the presence of glutamate. In contrast, we found that MNI-137, which is a negative allosteric modulator (NAM), blocked receptor activation by impeding CRD progression to the active conformation and preventing glutamate-induced stabilization of the domain. Collectively, the work presented here provides a dynamic receptor-centric model of allosteric modulator effects on mGluR2 conformation and dynamics, as well as mechanisms for positive and negative modulation.

![Figure 1.](https://cdn.elifesciences.org/articles/78982/elife-78982-fig1-v2.jpg)

**Figure 1.:** (A) Full-length cryo-EM structures of inactive (7EPA) and fully active (7E9G) metabotropic glutamate receptor 2 (mGluR2; human) and schematic illustrating fluorophore placement for each inter-domain sensor. (B) Representative normalized live-cell FRET trace from glutamate titration experiment on HEK293T cells expressing azi-extracellular loop 2 (azi-ECL2). Data was acquired at 4.5 s time resolution. Dose-response curves from live-cell FRET orthosteric agonist titration experiments using (C) azi-ECL2, (D) N-terminal SNAP-tag labeled mGluR2 (SNAP-m2), and (E) azi-cysteine-rich domain (azi-CRD). Data is acquired from individual cells and normalized to 1 mM glutamate response. Data represents mean ± SEM of responses from individual cells from at least three independent experiments. Total number of cells examined, mean half-maximum effective concentration (EC50), mean max response, and errors are listed in Tables 1–2.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/78982/elife-78982-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Representative image of HEK293T cells expressing N-terminal SNAP-tag labeled metabotropic glutamate receptor 2 (SNAP-m2), azi-cysteine-rich domain (azi-CRD), or azi-extracellular loop 2 (azi-ECL2) labeled with donor (left) and acceptor (right) fluorophores used for live-cell FRET experiments. Scale bar, 10 μM. (B) Representative normalized live-cell FRET traces of DCG-IV, LY379268, and (2R,4R)-APDC titration experiments on HEK293T cells expressing azi-ECL2. Data was acquired at 4.5 s time resolution.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/78982/elife-78982-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) Normalized maximal agonist-induced fluorescence resonance energy transfer (FRET) change for metabotropic glutamate receptor 2 (mGluR2) N-terminal SNAP-tag (SNAP-m2), azi-cysteine-rich domain (azi-CRD), and azi-extracellular loop 2 (azi-ECL2) sensors. Data represents mean ± SEM of responses from individual cells from at least three independent experiments. Total number of cells examined for normalization experiments, mean max response, and errors are listed in Table 2. (B) Representative normalized live-cell FRET traces from DCG-IV, LY379268, and (2R,4R)-APDC normalization experiments of azi-ECL2. Data is normalized to 1 mM glutamate response and collected at 4.5 s time resolution.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/78982/elife-78982-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** (A) Dose-response curves for metabotropic glutamate receptor 2 (mGluR2)-induced calcium flux during orthosteric agonist titrations. (B) Normalized maximal agonist-induced intracellular calcium levels. Glutamate dose-response curves for calcium flux induced by (C) azi-cysteine-rich domain (azi-CRD) and (D) azi-extracellular loop 2 (azi-ECL2). Data is normalized to 1 mM glutamate response. Data represents mean ± SEM of results from three independent experiments.

## Results

### CRD and 7TM domain conformation are sensitive measures of mGluR2 activation

According to the general model for mGluR activation, binding of an orthosteric agonist induces a local conformational change that causes global receptor rearrangement to activate the G protein-binding interface 10 nm away, through stabilization of an asymmetric 7TM domain interface (Seven et al., 2021). Therefore, activation involves coordinated conformational coupling of the three receptor domains. Structurally, the VFT domain, CRD, and 7TM domain undergo unique dynamics during receptor activation (Cao et al., 2021; Grushevskyi et al., 2019; Liauw et al., 2021). Moreover, how each domain within mGluRs contribute to the overall receptor regulation and activation is now better understood (Goudet et al., 2004; Huang et al., 2011; Thibado et al., 2021). Thus, the three domains can be viewed as modular units that are linked to form a complex and conformationally coupled signaling machine. To gain further insight into mGluR activation and allostery, a better understanding of the dynamics of individual domains and their relation to one another is essential.

Here, we used inter-subunit FRET sensors to measure the dimeric rearrangement of each structural domain within full-length mGluR2 in real-time and in vivo to obtain a more comprehensive picture of receptor activation (Figure 1A). Specifically, to study inter-7TM domain conformational change, we created a novel sensor based on an unnatural amino acid (UAA) incorporation strategy (Huber et al., 2013; Liauw et al., 2021; Noren et al., 1989; Serfling and Coin, 2016) to site-specifically label extracellular loop 2 (ECL2). We also utilized well established conformational sensors to examine the VFT domain and CRD (Doumazane et al., 2010; Liauw et al., 2021; Vafabakhsh et al., 2015). To generate the inter-7TM domain sensor, we inserted an amber codon between E715 and V716 which, after expression in HEK293T cells, was labeled with 4-azido-L-phenylalanine (hereafter, azi-ECL2). This sensor allowed us to precisely probe conformational changes at ECL2, which have been shown to be essential in coordinating structural transitions between the VFT domain and 7TM domain of not only mGluR2 (Du et al., 2021; Seven et al., 2021), but other class C GPCRs as well (Koehl et al., 2019; Shen et al., 2021). We observed a glutamate concentration-dependent increase in FRET signal in cells expressing azi-ECL2, confirming a general reduction in distance between ECL2s during mGluR2 activation and consistent with structural studies (Du et al., 2021; Seven et al., 2021; Figure 1B, Figure 1—figure supplement 1A). This glutamate-dependent increase in ensemble FRET had a half-maximum effective concentration (EC50) of 5.1 ± 0.6 μM, consistent with the concentration-dependent activation of GIRK currents (Vafabakhsh et al., 2015; Figure 1C, Table 1). These results validate the sensitivity and accuracy of this new FRET sensor. Next, we measured the concentration-dependent increases in ensemble FRET signals for other orthosteric ligands DCG-IV, LY379268, and (2R,4R)-APDC and measured EC50 values of 0.9 ± 0.1 μM, 10.2 ± 2.4 nM, and 6.7 ± 1.3 μM, respectively, in agreement with the published range of EC50 values for these compounds (Doumazane et al., 2013; Figure 1C, Table 1, Figure 1—figure supplement 1). Importantly, azi-ECL2 accurately reports that DCG-IV is less efficacious than glutamate, consistent with its characterization as a partial agonist. Likewise, this sensor was able to accurately report on LY379268 and (2R,4R)-APDC which are known to be more efficacious agonists than glutamate (Figure 1C, Table 2, Figure 1—figure supplement 2).

**Table 1.**
 Live-cell fluorescence resonance energy transfer (FRET) titration experiment data and statistics.Table 1—source data 1.Source data for Table 1.


<table>
  <thead>
    <tr>
      <th>Sensor</th>
      <th>Ligand</th>
      <th>N</th>
      <th>Mean half-maximum effective concentration (EC50)</th>
      <th>SEM</th>
      <th>Hill slope</th>
      <th>Standard error</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>SNAP-m2</td>
      <td>Glutamate</td>
      <td>9</td>
      <td>11.9</td>
      <td>1.5</td>
      <td>–1.44</td>
      <td>0.08</td>
    </tr>
    <tr>
      <td>SNAP-m2</td>
      <td>DCG-IV</td>
      <td>6</td>
      <td>0.4</td>
      <td>0.1</td>
      <td>–1.26</td>
      <td>0.11</td>
    </tr>
    <tr>
      <td>SNAP-m2</td>
      <td>LY379268</td>
      <td>6</td>
      <td>30.6</td>
      <td>9.3</td>
      <td>–1.12</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td>SNAP-m2</td>
      <td>(2R,4R)-APDC</td>
      <td>6</td>
      <td>6.9</td>
      <td>3.1</td>
      <td>–1.10</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td>SNAP-m2</td>
      <td>Glutamate + 10 μM BINA</td>
      <td>23</td>
      <td>1.2</td>
      <td>0.4</td>
      <td>–1.24</td>
      <td>0.09</td>
    </tr>
    <tr>
      <td>SNAP-m2</td>
      <td>Glutamate + 5 μM LY487379</td>
      <td>4</td>
      <td>3.8</td>
      <td>0.9</td>
      <td>–1.43</td>
      <td>0.11</td>
    </tr>
    <tr>
      <td>SNAP-m2</td>
      <td>Glutamate + 0.5 μM JNJ-42153605</td>
      <td>5</td>
      <td>4.2</td>
      <td>1.9</td>
      <td>–0.95</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td>SNAP-m2</td>
      <td>Glutamate + 10 μM MNI-137</td>
      <td>4</td>
      <td>17.2</td>
      <td>2.8</td>
      <td>–1.61</td>
      <td>0.06</td>
    </tr>
    <tr>
      <td>SNAP-m2</td>
      <td>Glutamate + 10 μM Ro 64–5229</td>
      <td>3</td>
      <td>19.6</td>
      <td>2.6</td>
      <td>–1.52</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td>azi-CRD</td>
      <td>Glutamate</td>
      <td>26</td>
      <td>11.6</td>
      <td>0.5</td>
      <td>1.19</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td>azi-CRD</td>
      <td>DCG-IV</td>
      <td>10</td>
      <td>1.1</td>
      <td>0.2</td>
      <td>0.94</td>
      <td>0.10</td>
    </tr>
    <tr>
      <td>azi-CRD</td>
      <td>LY379268</td>
      <td>20</td>
      <td>12.1</td>
      <td>0.5</td>
      <td>1.36</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td>azi-CRD</td>
      <td>(2R,4R)-APDC</td>
      <td>36</td>
      <td>6.5</td>
      <td>1.2</td>
      <td>1.10</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td>azi-CRD</td>
      <td>Glutamate + 10 μM BINA</td>
      <td>10</td>
      <td>1.6</td>
      <td>0.3</td>
      <td>1.16</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td>azi-CRD</td>
      <td>Glutamate + 5 μM LY487379</td>
      <td>22</td>
      <td>4.5</td>
      <td>0.6</td>
      <td>0.91</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td>azi-CRD</td>
      <td>Glutamate + 0.5 μM JNJ-42153605</td>
      <td>10</td>
      <td>4.7</td>
      <td>1.3</td>
      <td>0.84</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td>azi-CRD</td>
      <td>Glutamate + 10 μM MNI-137</td>
      <td>27</td>
      <td>13.8</td>
      <td>0.7</td>
      <td>1.10</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td>azi-CRD</td>
      <td>Glutamate + 10 μM Ro 64–5229</td>
      <td>13</td>
      <td>16.9</td>
      <td>1.2</td>
      <td>1.05</td>
      <td>0.06</td>
    </tr>
    <tr>
      <td>azi-ECL2</td>
      <td>Glutamate</td>
      <td>15</td>
      <td>5.1</td>
      <td>0.6</td>
      <td>0.96</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td>azi-ECL2</td>
      <td>DCG-IV</td>
      <td>24</td>
      <td>0.9</td>
      <td>0.1</td>
      <td>1.05</td>
      <td>0.06</td>
    </tr>
    <tr>
      <td>azi-ECL2</td>
      <td>LY379268</td>
      <td>9</td>
      <td>10.2</td>
      <td>2.4</td>
      <td>1.03</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td>azi-ECL2</td>
      <td>(2R,4R)-APDC</td>
      <td>13</td>
      <td>6.7</td>
      <td>1.3</td>
      <td>1.14</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td>azi-ECL2</td>
      <td>Glutamate + 10 μM BINA</td>
      <td>16</td>
      <td>2.5</td>
      <td>0.2</td>
      <td>1.06</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td>azi-ECL2</td>
      <td>Glutamate + 5 μM LY487379</td>
      <td>22</td>
      <td>3.5</td>
      <td>0.2</td>
      <td>0.98</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td>azi-ECL2</td>
      <td>Glutamate + 0.5 μM JNJ-42153605</td>
      <td>17</td>
      <td>2.2</td>
      <td>0.1</td>
      <td>0.97</td>
      <td>0.06</td>
    </tr>
    <tr>
      <td>azi-ECL2</td>
      <td>Glutamate + 10 μM MNI-137</td>
      <td>8</td>
      <td>14.4</td>
      <td>1.7</td>
      <td>1.32</td>
      <td>0.06</td>
    </tr>
    <tr>
      <td>azi-ECL2</td>
      <td>Glutamate + 10 μM Ro 64–5229</td>
      <td>5</td>
      <td>17.4</td>
      <td>2.4</td>
      <td>1.07</td>
      <td>0.09</td>
    </tr>
  </tbody>
</table>

_All EC50 and errors values are in μM, except for LY379268 (nM)._

**Table 2.**
 Live-cell fluorescence resonance energy transfer (FRET) max normalization experiment data and statistics.Table 2—source data 1.Source data for Table 2.


<table>
  <thead>
    <tr>
      <th>Sensor</th>
      <th>Ligand</th>
      <th>N</th>
      <th>Mean max response</th>
      <th>SEM</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>SNAP-m2</td>
      <td>Glutamate</td>
      <td>-</td>
      <td>1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>SNAP-m2</td>
      <td>DCG-IV</td>
      <td>25</td>
      <td>0.79</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>SNAP-m2</td>
      <td>LY379268</td>
      <td>23</td>
      <td>1.01</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>SNAP-m2</td>
      <td>(2R,4R)-APDC</td>
      <td>14</td>
      <td>0.96</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>SNAP-m2</td>
      <td>Glutamate + 10 μM BINA</td>
      <td>7</td>
      <td>1.02</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>SNAP-m2</td>
      <td>Glutamate + 5 μM LY487379</td>
      <td>14</td>
      <td>1.07</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>SNAP-m2</td>
      <td>Glutamate + 0.5 μM JNJ-42153605</td>
      <td>22</td>
      <td>1.01</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>SNAP-m2</td>
      <td>Glutamate + 10 μM MNI-137</td>
      <td>22</td>
      <td>0.85</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>SNAP-m2</td>
      <td>Glutamate + 10 μM Ro 64–5229</td>
      <td>35</td>
      <td>0.87</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>azi-CRD</td>
      <td>Glutamate</td>
      <td>-</td>
      <td>1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>azi-CRD</td>
      <td>DCG-IV</td>
      <td>19</td>
      <td>0.69</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>azi-CRD</td>
      <td>LY379268</td>
      <td>25</td>
      <td>1.06</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>azi-CRD</td>
      <td>(2R,4R)-APDC</td>
      <td>13</td>
      <td>1.02</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>azi-CRD</td>
      <td>Glutamate + 10 μM BINA</td>
      <td>9</td>
      <td>1.12</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td>azi-CRD</td>
      <td>Glutamate + 5 μM LY487379</td>
      <td>19</td>
      <td>1.56</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td>azi-CRD</td>
      <td>Glutamate + 0.5 μM JNJ-42153605</td>
      <td>8</td>
      <td>1.43</td>
      <td>0.08</td>
    </tr>
    <tr>
      <td>azi-CRD</td>
      <td>Glutamate + 10 μM MNI-137</td>
      <td>18</td>
      <td>0.86</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>azi-CRD</td>
      <td>Glutamate + 10 μM Ro 64–5229</td>
      <td>18</td>
      <td>0.59</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td>azi-ECL2</td>
      <td>Glutamate</td>
      <td>-</td>
      <td>1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>azi-ECL2</td>
      <td>DCG-IV</td>
      <td>25</td>
      <td>0.64</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>azi-ECL2</td>
      <td>LY379268</td>
      <td>22</td>
      <td>1.14</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td>azi-ECL2</td>
      <td>(2R,4R)-APDC</td>
      <td>56</td>
      <td>1.05</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>azi-ECL2</td>
      <td>Glutamate + 10 μM BINA</td>
      <td>14</td>
      <td>1.42</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td>azi-ECL2</td>
      <td>Glutamate + 5 μM LY487379</td>
      <td>7</td>
      <td>1.25</td>
      <td>0.09</td>
    </tr>
    <tr>
      <td>azi-ECL2</td>
      <td>Glutamate + 0.5 μM JNJ-42153605</td>
      <td>13</td>
      <td>0.99</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>azi-ECL2</td>
      <td>Glutamate + 10 μM MNI-137</td>
      <td>58</td>
      <td>0.78</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td>azi-ECL2</td>
      <td>Glutamate + 10 μM Ro 64–5229</td>
      <td>8</td>
      <td>0.84</td>
      <td>0.05</td>
    </tr>
  </tbody>
</table>

_All max response values are normalized to 1 mM glutamate._

Receptor rearrangement and activation requires local ligand-induced structural change to propagate from the VFT domain through the CRD to the 7TM domain. Thus, we next compared the orthosteric agonist-induced FRET change of azi-ECL2 with that of the VFT domain FRET sensor (N-terminal SNAP-tag labeled mGluR2; hereafter, SNAP-m2) and CRD FRET sensor (labeled via 4-azido-L-phenylalanine insertion at position 548; hereafter, azi-CRD). We found that all three sensors accurately predict the relative efficacy of tested orthosteric ligands (Figure 1C–E, Table 2, Figure 1—figure supplement 2A). Specifically, the three sensors rank the four agonists from most to least efficacious as LY379268 > (2R,4R)-APDC > glutamate > DCG-IV. However, the maximum response by highly efficacious agonists LY379268 and (2R,4R)-APDC are larger when measured at the CRD and 7TM domain compared to the VFT domain (Table 2, Figure 1—figure supplement 2). In contrast, maximum response by partial agonist DCG-IV is smaller at the CRD and 7TM domain as compared to measurements at the VFT domain. These findings are consistent with results from our functional calcium imaging assay that utilizes a chimeric G protein (Conklin et al., 1993; Figure 1—figure supplement 3). For example, DCG-IV shows 79% of glutamate efficacy via the VFT domain FRET sensor, while it shows 69% efficacy via CRD sensor and 64% efficacy via the ECL2 sensor, compared to 69% efficacy via the functional assay. Collectively, the results show that the novel ECL2 sensor accurately report the activation of mGluR2. Moreover, conformation of the CRD and 7TM domain are a more sensitive measure of receptor activation compared to the VFT domain and consistent with the loose coupling between mGluR domains (Grushevskyi et al., 2019; Liauw et al., 2021).

### Allosteric ligands modulate glutamate potency and efficacy at each structural domain

Establishing general principles to predict physiological outcome of mGluR allosteric modulators has been challenging due to their high context dependence and variability in functional measurements (Leach and Gregory, 2017; Thal et al., 2018). For example, many mGluR5 PAMs exhibit biased agonism when used in a panel of different functional assays and tested mGluR5 NAMs showed different effects between heterologous and endogenous systems (Sengmany et al., 2019; Sengmany et al., 2017). To overcome the inherent limitations due to convolution of responses of multiple components in the signaling pathway, we directly quantified the effects of a series of modulators on glutamate-induced rearrangement of mGluR2 using the three FRET sensors described above. This unique approach provides a conformational fingerprint of allosteric modulators, complementing available pharmacological and structural data.

We focused on three PAMs, BINA (Bonnefous et al., 2005), LY487379 (Johnson et al., 2003), and JNJ-42153605 (Cid et al., 2012), and two NAMs, MNI-137 (Hemstapat et al., 2007) and Ro 64–5229 (Kolczewski et al., 1999). We examined the ability of these compounds to modulate glutamate-induced FRET change of SNAP-m2, azi-CRD, and azi-ECL2 FRET sensors. Specifically, to quantify modulation of glutamate potency (EC50), we performed glutamate titrations using each sensor in the presence of a different allosteric modulator. Next, in separate experiments, we derived maximum responses (efficacy) to 1 mM glutamate with and without each of the modulators (Table 2, Figure 2—figure supplements 1–3). First, glutamate titrations in the presence of all tested PAMs resulted in increased glutamate potency and efficacy at every domain, as measured via FRET (Figure 2A, C. D, F, G, I, Tables 1–2). Therefore, the positive and negative allosteric modulation, which is defined through signaling assays, are generally manifested consistently at every structural domain of mGluR2. We found that PAMs generally increase glutamate efficacy to a greater extent as probed at the CRD and 7TM domain compared to the VFT domain (Figure 2J, Table 2). This is similar to the effects we observed for highly efficacious orthosteric agonists LY379268 and (2R,4R)-APDC. Specifically, glutamate efficacy in the presence of 10 μM BINA as reported by azi-CRD and azi-ECL2, and not SNAP-m2, are more consistent with our functional analysis, suggesting that the CRD and 7TM domain are better metrics of ligand efficacy (Figure 2—figure supplement 4). Interestingly, JNJ-42153605 showed no change in efficacy as quantified by the FRET signal at ECL2 while it showed changes at VFT domain and CRD (Figure 2G, I, J, Table 2). The ability of different mGluR2 PAMs to alter glutamate potency and efficacy as probed at each domain and to different degrees suggests that PAMs may utilize distinct mechanisms to achieve allosteric modulation of mGluR2, with each domain distinctly affected by each PAM.

![Figure 2.](https://cdn.elifesciences.org/articles/78982/elife-78982-fig2-v2.jpg)

**Figure 2.:** N-terminal SNAP-tag labeled mGluR2; hereafter (SNAP-m2) glutamate dose-response curves in the presence of (A) positive allosteric modulators (PAMs) or (B) NAMs. (C) Changes in glutamate potency and efficacy for SNAP-m2. The azi-cysteine-rich domain (azi-CRD) glutamate dose-response curves in the presence of (D) PAMs or (E) NAMs. (F) Changes in glutamate potency and efficacy for azi-CRD. The azi-extracellular loop 2 (azi-ECL2) glutamate dose-response curves in the presence of (G) PAMs or (H) NAMs. (I) Changes in glutamate potency and efficacy for azi-ECL2. (J) Changes in glutamate efficacy in response to PAMs and NAMs as measured by each conformational sensor. ΔPotency defined as (([modulator + glutamate]EC50 – [glutamate] EC50)/[glutamate] EC50) × 100. ΔEfficacy defined as ([1 mM glutamate + modulator] – [1 mM glutamate]) × 100. Data is acquired from individual cells and normalized to 1 mM glutamate response. Data represents mean ± SEM of responses from individual cells from at least three independent experiments. Total number of cells examined for titration and normalization experiments, mean half-maximum effective concentration (EC50), mean max response, and errors are listed in Tables 1–2.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/78982/elife-78982-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A–E) Representative normalized live-cell FRET traces of SNAP-m2 normalization experiments for all positive and negative allosteric modulators tested. Data was acquired at 4 s time resolution.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/78982/elife-78982-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A–E) Representative normalized live-cell FRET traces of azi-CRD normalization experiments for all positive and negative allosteric modulators tested. Data was acquired at 4.5 s time resolution.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/78982/elife-78982-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** (A–E) Representative normalized live-cell FRET traces of azi-ECL2 normalization experiments for all positive and negative allosteric modulators tested. Data was acquired at 4.5 s time resolution.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/78982/elife-78982-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** (A) Glutamate dose-response curves with and without allosteric modulators for metabotropic glutamate receptor 2 (mGluR2)-induced calcium flux. (B) Changes in glutamate potency and efficacy in response to allosteric modulator treatment, measured by intracellular calcium levels. ΔPotency defined as (([modulator + glutamate]EC50 – [glutamate] EC50)/[glutamate] EC50) × 100. ΔEfficacy defined as ([1 mM glutamate + modulator] – [1 mM glutamate]) × 100. Data is normalized to 1 mM glutamate response. Data represents mean ± SEM of results from three independent experiments.

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/78982/elife-78982-fig2-figsupp5-v2.jpg)

**Figure 2—figure supplement 5.:** The 7 transmembrane (7TM) domain (white) is from positive allosteric modulator (PAM) bound subunit of metabotropic glutamate receptor 2 (mGluR2; PDB:7MTS). Lateral view (left) and top view (right). Residues found to interact with PAM in structure (PDB: 7MTS) and from mutagenesis studies are shown with surface representations (gray). Ligands bound are superimposed volumes of PAMs (green; PDB: 7MTR, 7MTS, 7E9G) and NAMs (pink; PDB: 7EPE, 7EPF) solved in complex with metabotropic glutamate receptor 2 (mGluR2).

Next, glutamate titration in the presence of NAMs resulted in the overall reduction of glutamate potency and efficacy probed at each of the three domains, as expected for a NAM (Figure 2B, C, E, F, H, I, Tables 1–2). These results are consistent with our functional calcium imaging assay as well (Figure 2—figure supplement 4). Interestingly, at NAM concentration used for FRET imaging (10 μM) we observed robust glutamate-induced conformational change (Figure 2B, E and H, Figure 2—figure supplements 1–3) but could not detect receptor activation in the presence of glutamate, consistent with previous reports that high concentration of NAMs block mGluR2 signaling (Hemstapat et al., 2007; Kolczewski et al., 1999). This shows that MNI-137 and Ro 64–5229 can block receptor activation without blocking glutamate-induced conformational change at every domain, even at the 7TM domain where the NAMs bind. Whether this is due to induction of novel conformational states upon NAM binding or due to interruption in existing conformational changes that precede receptor activation, cannot be addressed using ensemble assays.

Together, the results show that the tested allosteric modulators affect glutamate-induced compaction and activation of mGluR2 in a manner consistent with their functional characterization. Interestingly, while having overlapping binding pockets that share key residues, PAMs and NAMs modulate glutamate-induced conformational change in different ways (Figure 2—figure supplement 5). Despite the overall trend for PAMs and NAMs, the general variability in the change of glutamate potency and efficacy between domains in response to individual modulators provides evidence for the existence of multiple pathways to achieve allosteric modulation of mGluR2.

### BINA can function independently of glutamate and stabilizes receptor during activation

Live-cell FRET experiments revealed the general conformational fingerprint of mGluR2 modulators, which are defined as changes in glutamate potency and efficacy as measured by rearrangement of different domains. However, the ensemble method cannot provide mechanistic information such as receptor conformation, state occupancy, and state transitions. For example, whether the modulators stabilize novel states or alter transition rates between existing states is not directly deducible from the ensemble characterization. To overcome this limitation, we performed single-molecule FRET (smFRET) using the CRD FRET sensor. We selected azi-CRD because our live-cell FRET analysis showed that quantification of modulator effects on the CRD was very consistent with our functional results. Moreover, we previously showed azi-CRD to be a sensitive reporter of mGluR2 allosteric modulation via smFRET analysis (Liauw et al., 2021).

To perform smFRET imaging, HEK293T cells expressing azi-CRD containing a C-terminal FLAG-tag were labeled using mixture of donor (Cy3) and acceptor (Cy5) fluorophores, then lysed. Cell lysate was then applied to a polyethylene glycol (PEG) passivated coverslip, functionalized with anti-FLAG-tag antibody to immunopurify the receptors (SiMPull) for total internal reflection fluorescence (TIRF) imaging (Jain et al., 2011; Liauw et al., 2021; Figure 3A). In the absence of glutamate, the CRD primarily occupied the inactive state and intermediate state 1, corresponding to open and inactive conformations of the VFT domains or the conformation where an individual VFT domain is closed, respectively (Liauw et al., 2021; Figure 3B and H, Table 3, Figure 3—figure supplement 1A). Importantly, the receptor showed dynamics between these states. A glutamate scavenging system was added for 0 μM glutamate conditions to ensure no glutamate contamination. Interestingly, in the absence of glutamate and presence of 10 μM BINA, we detected a small increase in FRET, primarily through increased occupancy of intermediate state 2, a conformation in which the 7TM domains are hypothesized to have not formed a stabilizing interaction with one another that is necessary for receptor activation (Liauw et al., 2021; Figure 3E and H, Table 3, Figure 3—figure supplement 2A). Upon the addition of intermediate (15 μM) and saturating (1 mM) concentrations of glutamate, a concentration-dependent increase in the active state occupancy was observed (Figure 3C, D and H, Table 3, Figure 3—figure supplement 1). The four conformational states and glutamate-dependent increase in FRET agree with previous work (Liauw et al., 2021). Specifically, addition of 15 μM glutamate in the presence of 10 μM BINA resulted in a FRET distribution similar to saturating glutamate alone (1 mM), consistent with the effect of PAM on increasing glutamate potency. Finally, 1 mM glutamate plus 10 µM BINA resulted in a further increase in active conformation occupancy, consistent with the effect of PAM on increasing glutamate efficacy (Figure 3F, G and H, Table 3, Figure 3—figure supplement 2). Interestingly, examination of CRD dynamics, as measured by cross-correlation between donor and acceptor intensities, showed that in the presence of intermediate (15 μM) and saturating (1 mM) glutamate concentrations, addition of 10 μM BINA reduced receptor dynamics (Figure 3I). Together, these observations suggests that PAMs may increase agonist efficacy by effectively increasing occupancy of the active conformation of the receptor. Moreover, these single-molecule measurements demonstrated that the effect of BINA on mGluR2 conformation and dynamics depends on the presence or absence of glutamate. In the absence of glutamate, BINA increased receptor dynamics and FRET by increasing the occupancy of intermediate state 2 (Figure 3E and H, Table 3, Figure 3—figure supplement 2). While in the presence of intermediate (15 μM) and saturating (1 mM) glutamate, BINA reduced the dynamics of the CRD and increased the occupancy of the active state (Figure 3F, G, H, I, Table 3, Figure 3—figure supplement 2). Interestingly, even in the presence of 1 mM glutamate and BINA, the receptors remained dynamic with the CRDs not fully stabilized in a single conformation.

![Figure 3.](https://cdn.elifesciences.org/articles/78982/elife-78982-fig3-v2.jpg)

**Figure 3.:** (A) Schematic of SiMPull assay (left) and representative image of donor and acceptor channels during data acquisition (right). Green circles indicate molecules selected by software for analysis. Scale bar, 3 μm. smFRET population histograms of azi-CRD in the presence of 0 μM, 15 μM, and 1 mM glutamate without (B–D) or with (E–G) 10 μM BINA. Histograms were fitted (black) to four Gaussian distributions centered around 0.24 (inactive; purple), 0.38 (intermediate 1; blue), 0.70 (intermediate 2; cyan), and 0.87 (active; red) FRET. Error bars represent SEM. Histograms (B–G) were generated from 332, 366, 253, 252, 418, and 367 individual particles, respectively. (H) Mean occupancy of four conformational states of azi-CRD in varying ligand conditions. Values represent area under each FRET peak from smFRET histogram as a fraction of total area. Mean and SEM values are reported in Table 3. (I) Mean cross-correlation of donor and acceptor intensities in the presence of intermediate (15 μM) and saturating (1 mM) glutamate with and without 10 μM BINA. Data was acquired at 50 ms time resolution. All data represents mean from three independent experiments.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/78982/elife-78982-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A–C) Representative smFRET traces of azi-cysteine-rich domain (azi-CRD) in the presence of (A) 0 μM, (B) 15 μM, and (C) 1 mM glutamate showing donor (green) and acceptor (red) and corresponding FRET (blue). Dashed lines represent four distinct FRET states. Data was acquired at 50 ms time resolution.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/78982/elife-78982-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A–C) Representative smFRET traces of azi-cysteine-rich domain (azi-CRD) in the presence of 10 μM BINA and (A) 0 μM, (B) 15 μM, and (C) 1 mM glutamate showing donor (green) and acceptor (red) and corresponding FRET (blue). Dashed lines represent four distinct FRET states. Data was acquired at 50 ms time resolution.

**Table 3.**
 Single-molecule fluorescence resonance energy transfer (smFRET) state occupancy data and statistics.Table 3—source data 1.Source data for Table 3.


<table>
  <thead>
    <tr>
      <th>Modulator</th>
      <th>Glut (μM)</th>
      <th>State (#)</th>
      <th>Mean occupancy</th>
      <th>SEM</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>None</td>
      <td>0</td>
      <td>1</td>
      <td>0.36067</td>
      <td>0.048</td>
    </tr>
    <tr>
      <td>None</td>
      <td>0</td>
      <td>2</td>
      <td>0.56526</td>
      <td>0.02692</td>
    </tr>
    <tr>
      <td>None</td>
      <td>0</td>
      <td>3</td>
      <td>0.06615</td>
      <td>0.02385</td>
    </tr>
    <tr>
      <td>None</td>
      <td>0</td>
      <td>4</td>
      <td>0.00792</td>
      <td>0.00792</td>
    </tr>
    <tr>
      <td>None</td>
      <td>15</td>
      <td>1</td>
      <td>0.01932</td>
      <td>0.01049</td>
    </tr>
    <tr>
      <td>None</td>
      <td>15</td>
      <td>2</td>
      <td>0.27699</td>
      <td>0.06688</td>
    </tr>
    <tr>
      <td>None</td>
      <td>15</td>
      <td>3</td>
      <td>0.29899</td>
      <td>0.01579</td>
    </tr>
    <tr>
      <td>None</td>
      <td>15</td>
      <td>4</td>
      <td>0.4047</td>
      <td>0.09147</td>
    </tr>
    <tr>
      <td>None</td>
      <td>1000</td>
      <td>1</td>
      <td>0.00642</td>
      <td>0.00292</td>
    </tr>
    <tr>
      <td>None</td>
      <td>1000</td>
      <td>2</td>
      <td>0.07841</td>
      <td>0.01209</td>
    </tr>
    <tr>
      <td>None</td>
      <td>1000</td>
      <td>3</td>
      <td>0.31131</td>
      <td>0.02404</td>
    </tr>
    <tr>
      <td>None</td>
      <td>1000</td>
      <td>4</td>
      <td>0.60386</td>
      <td>0.01743</td>
    </tr>
    <tr>
      <td>10 μM BINA</td>
      <td>0</td>
      <td>1</td>
      <td>0.30527</td>
      <td>0.02468</td>
    </tr>
    <tr>
      <td>10 μM BINA</td>
      <td>0</td>
      <td>2</td>
      <td>0.51994</td>
      <td>0.04492</td>
    </tr>
    <tr>
      <td>10 μM BINA</td>
      <td>0</td>
      <td>3</td>
      <td>0.14826</td>
      <td>0.04699</td>
    </tr>
    <tr>
      <td>10 μM BINA</td>
      <td>0</td>
      <td>4</td>
      <td>0.02653</td>
      <td>0.01748</td>
    </tr>
    <tr>
      <td>10 μM BINA</td>
      <td>15</td>
      <td>1</td>
      <td>0.01424</td>
      <td>0.00761</td>
    </tr>
    <tr>
      <td>10 μM BINA</td>
      <td>15</td>
      <td>2</td>
      <td>0.11217</td>
      <td>0.01526</td>
    </tr>
    <tr>
      <td>10 μM BINA</td>
      <td>15</td>
      <td>3</td>
      <td>0.3367</td>
      <td>0.07918</td>
    </tr>
    <tr>
      <td>10 μM BINA</td>
      <td>15</td>
      <td>4</td>
      <td>0.53688</td>
      <td>0.07621</td>
    </tr>
    <tr>
      <td>10 μM BINA</td>
      <td>1000</td>
      <td>1</td>
      <td>0.00296</td>
      <td>0.00154</td>
    </tr>
    <tr>
      <td>10 μM BINA</td>
      <td>1000</td>
      <td>2</td>
      <td>0.03751</td>
      <td>0.00782</td>
    </tr>
    <tr>
      <td>10 μM BINA</td>
      <td>1000</td>
      <td>3</td>
      <td>0.21791</td>
      <td>0.01663</td>
    </tr>
    <tr>
      <td>10 μM BINA</td>
      <td>1000</td>
      <td>4</td>
      <td>0.74162</td>
      <td>0.01093</td>
    </tr>
    <tr>
      <td>5 μM MNI-137</td>
      <td>0</td>
      <td>1</td>
      <td>0.74861</td>
      <td>0.02014</td>
    </tr>
    <tr>
      <td>5 μM MNI-137</td>
      <td>0</td>
      <td>2</td>
      <td>0.22198</td>
      <td>0.01316</td>
    </tr>
    <tr>
      <td>5 μM MNI-137</td>
      <td>0</td>
      <td>3</td>
      <td>0.02038</td>
      <td>0.01004</td>
    </tr>
    <tr>
      <td>5 μM MNI-137</td>
      <td>0</td>
      <td>4</td>
      <td>0.00903</td>
      <td>0.00541</td>
    </tr>
    <tr>
      <td>5 μM MNI-137</td>
      <td>15</td>
      <td>1</td>
      <td>0.10387</td>
      <td>0.02484</td>
    </tr>
    <tr>
      <td>5 μM MNI-137</td>
      <td>15</td>
      <td>2</td>
      <td>0.74937</td>
      <td>0.01688</td>
    </tr>
    <tr>
      <td>5 μM MNI-137</td>
      <td>15</td>
      <td>3</td>
      <td>0.12724</td>
      <td>0.01026</td>
    </tr>
    <tr>
      <td>5 μM MNI-137</td>
      <td>15</td>
      <td>4</td>
      <td>0.01952</td>
      <td>0.00254</td>
    </tr>
    <tr>
      <td>5 μM MNI-137</td>
      <td>1000</td>
      <td>1</td>
      <td>0.00207</td>
      <td>0.000954</td>
    </tr>
    <tr>
      <td>5 μM MNI-137</td>
      <td>1000</td>
      <td>2</td>
      <td>0.5597</td>
      <td>0.02561</td>
    </tr>
    <tr>
      <td>5 μM MNI-137</td>
      <td>1000</td>
      <td>3</td>
      <td>0.33098</td>
      <td>0.03204</td>
    </tr>
    <tr>
      <td>5 μM MNI-137</td>
      <td>1000</td>
      <td>4</td>
      <td>0.10725</td>
      <td>0.00734</td>
    </tr>
  </tbody>
</table>

### MNI-137 prevents CRD progression to the active conformation and glutamate-induced stabilization

Some mGluR2 NAMs that bind at the 7TM domain function as non-competitive antagonists and can prevent glutamate-dependent activation of the receptor (Hemstapat et al., 2007). To investigate the molecular mechanism underlying this phenomenon, we next performed smFRET analysis to directly visualize the effect of MNI-137 on the CRD sensor. In the absence of glutamate, 5 μM MNI-137 resulted in a decrease in FRET and increase in occupancy of the inactive conformation of the CRD as compared to unliganded receptor (Figure 4A and D, Table 3, Figure 4—figure supplement 1A). The increase in inactive state occupancy was accompanied by a stabilization of the CRD, demonstrating that MNI-137 reduces intrinsic CRD dynamics in the absence of glutamate, which contrasts with the effects of BINA alone (Figure 4—figure supplement 2A). Upon the addition of intermediate (15 μM) and saturating (1 mM) glutamate concentrations and in the presence of 5 μM MNI-137, occupancy of intermediate states 1 and 2 substantially increased with minimal change in the active conformation observed (Figure 4B–D, Table 3, Figure 4—figure supplement 1). To examine which specific state transitions are being hindered by MNI-137, we performed Hidden Markov modeling analysis on the smFRET time traces. Examination of the transition density plots (TDPs) obtained from this analysis showed that at 1 mM glutamate alone the dominant transitions occur between intermediate state 2 and the active conformation for the CRD (Figure 4E). This is consistent with the intermediate state 2 being the ‘pre-active’ conformation (Liauw et al., 2021). In contrast, in the presence of both 1 mM glutamate and MNI-137, the CRD primarily transitions between intermediate states 1 and 2, with few transitions to the active state. This suggests that MNI-137 effectively prevents the formation of the stabilizing 7TM domain interaction necessary for mGluR2 activation. Together, these results directly show that MNI-137 prevents receptor activation by blocking the last step toward receptor activation and effectively trapping the receptor in constant transition between the existing intermediate states.

![Figure 4.](https://cdn.elifesciences.org/articles/78982/elife-78982-fig4-v2.jpg)

**Figure 4.:** (A–C) smFRET population histograms of azi-CRD sensor in the presence of 0 μM (372 particles), 15 μM (560 particles), and 1 mM (479 particles) glutamate and 5 μM MNI-137. Histograms were fitted (black) to four Gaussian distributions centered around 0.24 (inactive; purple), 0.38 (intermediate 1; blue), 0.70 (intermediate 2; cyan), and 0.87 (active; red) FRET. Error bars represent SEM. (D) Mean occupancy of four conformational states of azi-CRD in varying ligand conditions. Values represent area under each FRET peak from smFRET histogram as a fraction of total area. Mean and SEM values are reported in Table 3. (E) Transition density plots of azi-CRD at 1 mM glutamate with and without MNI-137. Dashed lines represent four distinct FRET states. (F) Mean cross-correlation of donor and acceptor intensities in the presence of 0 μM, 15 μM, and 1 mM glutamate and 5 μM MNI-137. Data was acquired at 50 ms time resolution. Data represents mean from three independent experiments.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/78982/elife-78982-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A–C) Representative smFRET traces of azi-cysteine-rich domain (azi-CRD) in the presence of 5 μM MNI-137 and (A) 0 μM, (B) 15 μM, and (C) 1 mM glutamate showing donor (green) and acceptor (red) and corresponding FRET (blue). Dashed lines represent four distinct FRET states. Data was acquired at 50 ms time resolution.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/78982/elife-78982-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A) Cross-correlation of azi-CRD donor and acceptor intensities in the presence of 0 μM glutamate alone and with 5 μM MNI-137 or 10 μM BINA. (B) Cross-correlation of azi-CRD donor and acceptor intensities in the presence of 1 mM glutamate alone and with 5 μM MNI-137 or 10 μM BINA. Data was acquired at 50 ms time resolution.

Interestingly, examination of the CRD dynamics by cross-correlation analysis revealed that the effect of MNI-137 on receptor dynamics is dependent on whether glutamate is present or not. In the absence of glutamate, MNI-137 reduced CRD dynamics (Figure 4—figure supplement 1A). In contrast, when glutamate and MNI-137 were both present, we observed a glutamate concentration-dependent increase in the CRD dynamics (Figure 4F). This effect is the opposite to the effect of BINA, a PAM (Figure 3I, Figure 4—figure supplement 2B). Thus, in addition to impeding progression of the CRD to the active conformation, MNI-137 also effectively prevents glutamate-induced stabilization of the 7TM domain. Together, these results provide a mechanistic understanding of how MNI-137, a NAM, can block receptor activation. This reduction of CRD stability and blocking of entry into the active conformation also provides insight into why glutamate-induced conformational change can still be observed, both in live-cell and single-molecule imaging, despite the presence of inhibiting MNI-137 concentrations. Finally, the mechanisms of action for both MNI-137 and BINA highlights the importance of structural dynamics for mGluR activation and modulation.

## Discussion

A fundamental design principle for many receptors is that activation is allosteric in nature. Moreover, ligand ‘sensing’ and receptor activation is driven by the energy from ligand binding and cellular energy cost in the form of ATP or GTP hydrolysis that occurs after sensing. In GPCRs, activation involves conformational coupling between the ligand binding domain and the G protein binding interface. Recent experiments have shown that GPCRs are dynamic (Nygaard et al., 2013) and undergo transition between multiple conformational states, including multiple intermediate states. For class A GPCRs, studies using conformational biosensors based on nuclear magnetic resonance (NMR) spectroscopy (Huang et al., 2021), double electron-electron resonance spectroscopy (Wingler et al., 2019), smFRET (Gregorio et al., 2017), and fluorescent enhancement Wei et al., 2022 have revealed the importance of conformational dynamics for receptor activation, ligand efficacy, and biased signaling. Specifically, activation of mGluRs involves coordinated movement between three structural domains. In this case, local conformational changes result in major conformational rearrangement that propagate from the ligand binding site to the active site, consistent with the ‘domino’ model of allosteric signal transduction. Within this framework, allosteric modulators act on sites that are distinct from the orthosteric ligand binding site and affect the function of the receptor. Due to their potential to achieve subtype specificity, allosteric modulators have become a major focus for drug development. Common physiological characterization of GPCR allosteric modulators is often pathway specific and rely on the use of functional assays that quantify the output of the receptor along the signaling cascade. In this work we aimed to develop a receptor-centric view of allosteric modulation by quantifying the relationship between allosteric modulation and protein structural dynamics. Potential sources of heterogeneity arising from differences in post-translational modifications or differences in the local lipid environment, may affect receptor conformation. Therefore, our results represent the average of a heterogeneous population of such receptors. We identified the in vivo conformational fingerprint of multiple allosteric modulators of mGluR2 at three structural domains by using novel non-perturbing FRET sensors. This in vivo approach established a direct connection between the effect of allosteric modulators on receptor conformation at each domain and the physiological metrics of the modulator (i.e. efficacy and potency). Specifically, we found that modulators consistently affect the general trend of glutamate-induced conformational change underlying activation at every structural domain of mGluR2 (Figure 2). This result demonstrates the existence of a long-range allosteric pathway along the receptor and over a 10 nm distance. Interestingly, for the same modulator, the degree of conformational change was different among different domains (Figure 2J). In fact, we determined that the CRD and 7TM domain conformations are more accurate predictors of ligand efficacy as compared to the VFT domain conformation.

Previous research showed that the activation of mGluR2 is a stepwise process with transitions between four states, including two intermediate states (Liauw et al., 2021). Our smFRET analysis with a PAM and NAM showed that allosteric modulators do not induce a new conformational state, within the resolution of smFRET measurements. Instead, they produce their modulatory effect by employing the inherent conformational flexibility of receptors to modify receptor occupancy of the intermediate states. In the case of the PAM, BINA increases the efficacy and potency of glutamate by increasing the transitions from the intermediate state to the active state (Figure 3). On the other hand, previous work had shown that the mGluR2 NAM MNI-137 can block receptor signaling. Our analysis provides a mechanism for this observation where MNI-137 blocks entry into the active conformation and increases the transitions into the intermediate states, thereby increasing the occupancy of the intermediate states (Figure 4). As a result, the receptor is effectively trapped in the intermediate states. Further studies are necessary to determine the atomic structure of these intermediate states. Interestingly, the regulation of intermediate state occupancy has recently been shown to be a mechanism of allosteric modulation for other classes of GPCRs as well. NMR studies on the μ-opioid receptor (Kaneko et al., 2022) and cannabinoid receptor 1 (Wang et al., 2021) revealed that PAMs and NAMs regulate receptor function by acting on intermediate conformations in a manner similar to our findings for BINA and MNI-137. Collectively, these results suggest that designing compounds that regulate intermediate state occupancy is a plausible strategy for the development of allosteric modulators for mGluR2 and other families of GPCRs.

Protein allostery is intimately related to protein dynamics. Our results show that the effect of modulator binding at the 7TM domain on the receptor dynamics probed at the CRD, depends on the orthosteric agonist. In the absence of an orthosteric agonist, NAM stabilize the overall receptor dynamics while PAM increase receptor dynamics (Figure 4—figure supplement 2A). On the other hand, in the presence of saturating agonist, the PAM reduced receptor dynamics while the NAM increased receptor dynamics (Figure 4—figure supplement 2B). These results further highlight the roles of conformational dynamics in allosteric regulation.

In summary, our study provides a conformational fingerprint of diverse allosteric modulators of mGluR2 at different domains of the receptor. Classically receptors were thought of as two-state switches undergoing transition between on and off states. However, it is now clear that GPCRs’ ability to dynamically sample a repertoire of conformations is central to their overall function. Our findings highlight the significance of intermediate states in GPCRs for receptor modulation. Furthermore, our findings suggest that designing compounds that modulate the stability of intermediate states could be a promising direction for developing allosteric drugs. The tools we developed and applied here are not limited to mGluRs and can be extended to the study of other complex multi-domain proteins.

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
      <td>Cell line (Homo sapiens)</td>
      <td>HEK 293T</td>
      <td>Sigma Aldrich</td>
      <td>Cat # 12022001</td>
      <td></td>
    </tr>
    <tr>
      <td>Transfected construct (Mus musculus)</td>
      <td>SNAP-m2</td>
      <td>Liauw et al., 2021</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Transfected construct (Mus musculus)</td>
      <td>SNAP-m2 (no-FLAG)</td>
      <td>Liauw et al., 2021 (modified)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Transfected construct (Mus musculus)</td>
      <td>azi-CRD</td>
      <td>Liauw et al., 2021</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Transfected construct (Mus musculus)</td>
      <td>azi-ECL2</td>
      <td>Genscript (modified)</td>
      <td>ORF clone: OMu19627D</td>
      <td></td>
    </tr>
    <tr>
      <td>Transfected construct (Homo sapiens)</td>
      <td>pIRE4-Azi</td>
      <td>Addgene</td>
      <td>Plasmid # 105,829</td>
      <td></td>
    </tr>
    <tr>
      <td>Transfected construct (Mus musculus)</td>
      <td>Gqo5</td>
      <td>Addgene (modified)</td>
      <td>Plasmid # 24,500</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Glutamate</td>
      <td>Sigma Aldrich</td>
      <td>Cat # 6106-04-3</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>LY379268</td>
      <td>Tocris</td>
      <td>Cat # 2,453</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DCG-IV</td>
      <td>Tocris</td>
      <td>Cat # 0975</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>(2R,4R)-APDC</td>
      <td>Tocris</td>
      <td>Cat # 1,208</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>LY487379</td>
      <td>Tocris</td>
      <td>Cat # 3,283</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>BINA</td>
      <td>Tocris</td>
      <td>Cat # 4,048</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>JNJ-42153605</td>
      <td>Cayman Chemical</td>
      <td>21,984</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Ro 64–5229</td>
      <td>Tocris</td>
      <td>Cat # 2,913</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>MNI-137</td>
      <td>Tocris</td>
      <td>Cat # 4,388</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>SNAP-Surface Alexa Fluor 549</td>
      <td>New England Biolabs</td>
      <td>S9112S</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>SNAP-Surface Alexa Fluor 647</td>
      <td>New England Biolabs</td>
      <td>S9136S</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Oregon Green 488 BAPTA-1, AM</td>
      <td>Thermo Fisher Scientific</td>
      <td>O6807</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Cy3 Alkyne</td>
      <td>Click Chemistry Tools</td>
      <td>TA117-5</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Cy5 Alkyne</td>
      <td>Click Chemistry Tools</td>
      <td>TA116-5</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>4-azido-L-phenylalanine</td>
      <td>Chem-Impex International</td>
      <td>Cat # 06162</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Aminoguanidine (hydrochloride)</td>
      <td>Cayman Chemical</td>
      <td>81,530</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>BTTES</td>
      <td>Click Chemistry Tools</td>
      <td>1237–500</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Copper (II) sulfate</td>
      <td>Sigma Aldrich</td>
      <td>Cat # 451657–10 G</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>(+)-Sodium L-Ascorbate</td>
      <td>Sigma Aldrich</td>
      <td>Cat # 11140–250 G</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Glutamic-Pyruvic Transaminase</td>
      <td>Sigma Aldrich</td>
      <td>Cat # G8255-200UN</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Sodium Pyruvate</td>
      <td>Gibco</td>
      <td>11360–070</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DMEM</td>
      <td>Corning</td>
      <td>10–013-CV</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Defined Fetal Bovine Serum</td>
      <td>Thermo Fisher Scientific</td>
      <td>SH30070.03</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Penicillin-Streptomycin</td>
      <td>Gibco</td>
      <td>15140–122</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Lipofectamine 3000 Transfection Reagent</td>
      <td>Thermo Fisher Scientific</td>
      <td>L3000015</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Poly-L-lysine hydrobromide</td>
      <td>Sigma Aldrich</td>
      <td>Cat # P2636</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>FLAG-tag antibody</td>
      <td>Genscript</td>
      <td>A01429</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>smCamera (Version 1.0)</td>
      <td>http://ha.med.jhmi.edu/resources/</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ImageJ (Version 1.52 p)</td>
      <td>http://imagej.nih.gov/ij/</td>
      <td>RRID:SCR_003070</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>OriginPro (2020b)</td>
      <td>https://www.originlab.com/</td>
      <td>RRID:SCR_014212</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Adobe Illustrator (2022)</td>
      <td>https://www.adobe.com/</td>
      <td>RRID:SCR_010279</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Molecular cloning

The C-terminal FLAG-tagged mouse mGluR2 construct in pcDNA3.1(+) expression vector was purchased from GenScript (ORF clone: OMu19627D) and verified by sequencing (ACGT Inc). Full length mGluR2 construct with an amber codon (TAG) mutation of amino acid A548 (azi-CRD) or N-terminal SNAP-tag (SNAP-mGluR2) were generated as previously reported (Liauw et al., 2021). The insertion of an amber codon (TAG) between E715 and V716 in mGluR2 (azi-ECL2) was performed using the QuikChange site-directed mutagenesis kit (Agilent). SNAP-mGluR2 constructs used for calcium imaging had C-terminal FLAG-tag removed by PCR-based deletion using phosphorylated primers. All plasmids were sequence verified (ACGT Inc). DNA restriction enzymes, DNA polymerase and DNA ligase were from New England Biolabs. Plasmid preparation kits were purchased from Macherey-Nagel.

### Cell culture

HEK293T cells (Sigma) were authenticated (ATCC) and tested for mycoplasma contamination (Lonza). HEK293T cells were maintained in DMEM (Corning) supplemented with 10% (v/v) fetal bovine serum (Fisher Scientific), 100 unit/mL penicillin-streptomycin (Gibco) and 15 mM HEPES (pH = 7.4, Gibco) at 37°C and 5% CO2. The cells were passaged with 0.05% trypsin-EDTA (Gibco). For UAA-containing protein expression, the growth media was supplemented with 0.6 mM 4-azido-L-phenylalanine (Chem-Impex International). All media was filtered by 0.2 µM PES filter (Fisher Scientific).

### Transfection and protein expression

About 24 hr before transfection, HEK293T cells were cultured on poly-L-lysine-coated 18 mm glass coverslips (VWR). For SNAP-mGluR2 used in FRET experiments, media was refreshed with standard growth media and transfected using Lipofectamine 3000 (Fisher Scientific) (total plasmid: 1 µg/18 mm coverslip). Growth media was refreshed after 24 hr and cells were grown for an additional 24 hr.

For UAA-containing protein expression, 1 hr before transfection, media was changed to the growth media supplemented with 0.6 mM 4-azido-L-phenylalanine. mGluR2 plasmids with an amber codon (azi-CRD or azi-ECL2) and pIRE4-Azi plasmid (pIRE4-Azi was a gift from Irene Coin, Addgene plasmid # 105829) were co-transfected (1:1 w/w) into cells using Lipofectamine 3000 (Fisher Scientific) (total plasmid: 2 µg/18 mm coverslip). The growth media containing 0.6 mM 4-azido-L-phenylalanine was refreshed after 24 hr and cells were grown for an additional 24 hr. On the day of the experiment, 30 min before labeling, supplemented growth media was removed and cells were washed by extracellular buffer solution containing (in mM): 128 NaCl, 2 KCl, 2.5 CaCl2, 1.2 MgCl2, 10 sucrose, 10 HEPES, pH = 7.4 and were kept in growth medium without 4-azido-L-phenylalanine.

For calcium imaging experiments, media was refreshed with standard growth media and cells were co-transfected with SNAP-mGluR2 (no FLAG-tag) and chimeric G protein (Gqo5, Addgene plasmid #24500) (1:2 w/w) using Lipofectamine 3000 (Fisher Scientific) (total plasmid: 1.5 µg/18 mm coverslip). For calcium imaging using UAA-containing proteins (azi-CRD or azi-ECL2), we followed the transfection and growth protocol described above and included an additional 1 μg of chimeric G protein (Gqo5). Growth media was refreshed after 24 hr, and cells were grown for an additional 24 hr. Before the addition of labeling solutions, cells were washed with extracellular buffer solution.

### SNAP-tag labeling for FRET measurements

SNAP-tag labeling of SNAP-mGluR2 was done by incubating cells with 2 µM of SNAP-Surface Alexa Fluor 549 (NEB) and 2 µM of SNAP-Surface Alexa Fluor 647 (NEB) in extracellular buffer for 30 min at 37°C. After labelling, cells were washed by extracellular buffer solution to remove excess dye.

### UAA labeling by azide-alkyne click chemistry

The UAA labeling by azide-alkyne click chemistry was performed as previously reported (Liauw et al., 2021). Stock solutions were made as follows: Cy3 and Cy5 alkyne dyes (Click Chemistry Tools) 10 mM in DMSO, BTTES (Click Chemistry Tools) 50 mM, copper (II) sulfate (Sigma) 20 mM, aminoguanidine (Cayman Chemical) 100 mM, and (+)-sodium L-ascorbate (Sigma) 100 mM in ultrapure distilled water (Invitrogen). In 656 µL of extracellular buffer solution, Cy3 and Cy5 alkyne dyes were mixed to a final concentration of 18 µM for each dye. To this mixture, a fresh pre-mixed solution of copper (II) sulfate and BTTES (1:5 molar ratio) was added at the final concentration of 150 µM and 750 µM, respectively. Next, aminoguanidine was added to the final concentration of 1.25 mM. Lastly, (+)-sodium L-ascorbate was added to the mixture to a final concentration of 2.5 mM. Total labeling volume was 0.7 mL. The labeling mixture was incubated at 4°C for 8 min, followed by a 2 min incubation at room temperature before addition to cells. Cells were washed with extracellular buffer solution prior to addition of labeling mixture. During labeling, cells were kept in the dark at 37°C and 5% CO2. After 10 min, L-glutamate (Sigma) was added to the cells to a final concentration of 0.5 mM and cells were incubated for an additional 5 min. After labeling, cells were washed by the extracellular buffer solution to remove excess dye.

### Labeling for calcium imaging

Cells used for calcium imaging experiments were labeled using 1 µM SNAP-Surface Alexa Fluor 647 (NEB) and 4 µM Oregon Green 488 BAPTA-1 (Fisher Scientific) in extracellular buffer for 30 min at 37°C. For cells expressing UAA-containing proteins, we labeled the cells with 4 µM Oregon Green 488 BAPTA-1. After labeling, cells were washed by extracellular buffer solution to remove excess dye.

### Live-cell FRET measurements

The microscope and flow system setup used were as previously reported (Liauw et al., 2021). After labeling, coverslip was assembled in the flow chamber (Innova Plex) and attached to a gravity flow control system (ALA Scientific Instruments). Extracellular buffer solution was used as imaging buffer and applied at the rate of 5  mL min−1. Labeled cells were imaged on a home-built microscope equipped with a × 20 objective (Olympus, oil-immersion) and using an excitation filter set with a quad-edge dichroic mirror (Di03-R405/488/532/635, Semrock) and a long-pass filter (ET542lp, Chroma). All data were recorded at 4.5 s time resolution for UAA containing constructs and 4 s for SNAP-tag containing constructs. All experiments were performed at room temperature. Donor fluorophores were excited with a 532 nm laser (RPMC Lasers) and emissions from donor and acceptor fluorophores were simultaneously recorded.

Analysis of live-cell FRET data was performed using smCamera (http://ha.med.jhmi.edu/resources/), ImageJ (http://imagej.nih.gov/ij/), and OriginPro (OriginLab). Movies were corrected for bleed-through of the donor signal into the acceptor channel. Donor bleed-through correction was done by measuring signals from 50 ROIs of Cy3 labeled cells in both the donor and acceptor channels and was calculated to be 8.8%. ROIs used for analysis included the whole cell membrane for individual cells. Apparent FRET efficiency was calculated as FRET = (IA − 0.088 × ID)/(ID + (IA − 0.088 × ID)), where ID and IA are the donor and acceptor intensity after buffer-only background subtraction. ΔFRET was calculated as the difference between FRET signal during treatment condition and FRET signal before treatment. In each case, the fluorescence was averaged over 6 datapoints once the signal was stable. Dose-response equation $yx=A1+\frac{A_{2}-A_{1}}{1+10^{logx_{0}-xP}}$ was used for fitting FRET response to calculate EC50 values, where A1 is the lower asymptote, A2 is the upper asymptote, P is the Hill slope, and x0 is the EC50. Maximal responses were normalized to 1 mM glutamate response. All data is from at least three independent biological replicates.

As analysis was limited to relative FRET changes between drug treatments rather than absolute FRET values, no further corrections, aside from the 8.8% bleed-through subtraction, were applied. A small artifact in Cy3 signal (decrease in fluorescence) was observed in response to modulator application for donor-only labeled cells. However, this response showed the same relative amplitude and kinetics as FRET responses and were similar among all modulators tested, thus, was not corrected for. All analyzed FRET changes were verified showing anti-correlated behavior. Furthermore, analysis of acceptor signal in response to different modulator treatment qualitatively recapitulated results of FRET data.

### Calcium imaging

After labeling, sample was assembled in the flow chamber (Innova Plex) and attached to the flow control system (ALA Scientific Instruments) in an identical manner to live-cell FRET experiments. Labeled cells were imaged using an inverted confocal microscope (Zeiss, LSM-800) with a × 40 oil-immersion objective (Plan-Apochromat × 40/1.3oil DIC (UV) VIS-IR M27). Sample was illuminated using a 488 nm laser and fluorescence from Oregon Green 488 nm was measured by a GaAsP-PMT detector with detection wavelengths set to 410–617 nm. For cells expressing SNAP-mGluR2 (no FLAG-tag), samples were excited using the 488 nm laser and a 640 nm laser simultaneously, and Cy5 fluorescence was measured with detection wavelengths set to 648–700 nm. All calcium imaging data were recorded at 3 s time resolution and at room temperature.

Analysis of functional calcium imaging data was performed using ImageJ (http://imagej.nih.gov/ij/) and OriginPro (OriginLab). All cells showing agonist-induced calcium response were selected for initial analysis, with those showing significant drift or photobleaching being omitted from downstream analysis. Fluorescence signal was measured for individual cells from a given movie, normalized from 0 to 1, and averaged. Changes in calcium signal were calculated from these averaged responses as the difference between max response during treatment and response before treatment. Baseline signal intensity was the average over 6 datapoints prior to treatment application. Dose-response equation $yx=A1+\frac{A_{2}-A_{1}}{1+10^{logx_{0}-xP}}$ was used for fitting calcium response to calculate EC50 values, where A1 is the lower asymptote, A2 is the upper asymptote, P is the Hill slope, and x0 is the EC50. Maximal responses were calculated as a fraction of 10 μM ionomycin-induced response, then normalized to 1 mM glutamate response. Direct activation of mGluR2 and subsequent intracellular calcium flux caused by the positive allosteric modulators LY487379 and JNJ-42153605 precluded analysis of the compounds ability to affect glutamate potency and efficacy. All data are from three independent biological replicates.

### smFRET measurements

Single-molecule experiments were conducted using custom flow cells prepared from glass coverslips (VWR) and slides (Fisher Scientific) passivated with mPEG (Laysan Bio) and 1% (w/w) biotin-PEG to prevent unspecific protein adsorption, as previously described (Jain et al., 2011; Vafabakhsh et al., 2015). Prior to experiments, flow cells were functionalized with FLAG-tag antibody. This was achieved by first incubating flow cells with 500 nM NeutrAvidin (Fisher Scientific) for 2 min followed by 20 μM biotinylated FLAG-tag antibody (A01429, GenScript) for 30 min. Unbound NeutrAvidin and biotinylated FLAG-tag antibody were removed by washing between each incubation step. Washes and protein dilutions were done using T50 buffer (50 mM NaCl, 10 mM Tris, and pH 7.4).

After labeling, cells were recovered from an 18 mm poly-L-lysine coverslip by incubating with Ca2+-free DPBS followed by a gentle pipetting. Cells were then pelleted by a 4000 g centrifugation at 4°C for 10 min. The supernatant was removed and cells were resuspended in 100 µL lysis buffer consisting of 200 mM NaCl, 50 mM HEPES, 1 mM EDTA, protease inhibitor tablet (Fisher Scientific), and 0.1 w/v% LMNG-CHS (10:1, Anatrace), pH 7.4. Cells were allowed to lyse with gentle mixing at 4°C for 1 hr. Cell lysate was then centrifuged for 20 min at 20,000 g and 4°C. The supernatant was collected and immediately diluted 10-fold with dilution buffer consisting of 200 mM NaCl, 50 mM HEPES, 1 mM EDTA, protease inhibitor tablet, and 0.0004 w/v% GDN (Anatrace), pH 7.4. The diluted sample was then added to the flow chamber to achieve sparse surface immobilization of labeled receptors by their C-terminal FLAG-tag. After optimal receptor coverage was achieved, flow chamber was washed extensively (>20 × chamber volume) to remove unbound proteins and excess detergent with wash buffer consisting of 200 mM NaCl, 50 mM HEPES, 0.005 w/v% LMNG-CHS (10:1, Anatrace), and 0.0004 w/v% GDN, pH 7.4. Finally, labeled receptors were imaged in imaging buffer consisting of (in mM) 128 NaCl, 2 KCl, 2.5 CaCl2, 1.2 MgCl2, 40 HEPES, 4 Trolox, 0.005 w/v% LMNG-CHS (10:1), 0.0004 w/v% GDN, and an oxygen scavenging system consisting of protocatechuic acid (Sigma) and 1.6 U/mL bacterial protocatechuate 3,4-dioxygenase (rPCO) (Oriental Yeast Co.), pH 7.35. For glutamate-free conditions, imaging buffer contained 2 U/mL glutamic-pyruvic transaminase (Sigma) and 2 mM sodium pyruvate (Gibco) and was incubated at 37°C for 10 min. All reagents were prepared from ultrapure-grade chemicals (purity >99.99%) and were purchased from Sigma. All buffers were made using ultrapure distilled water (Invitrogen). Samples were imaged with a 100 × objective (Olympus, 1.49 NA, Oil-immersion) on a custom-built microscope with 50ms time resolution unless stated otherwise. 532 nm and 638 nm lasers (RPMC Lasers) were used for donor and acceptor excitation, respectively.

### smFRET data analysis

Analysis of single-molecule fluorescence data was performed using smCamera (http://ha.med.jhmi.edu/resources/), custom MATLAB (MathWorks) scripts, and OriginPro (OriginLab). Particle selection and generation of raw FRET traces were done automatically within the smCamera software. For the selection, particles that showed acceptor signal upon donor excitation, with acceptor brightness greater than 10% above background and had a Gaussian intensity profile, were automatically selected and donor and acceptor intensities were measured over all frames. Out of this pool, particles that showed a single donor and a single acceptor bleaching step during the acquisition time, stable total intensity (ID + IA), anti-correlated donor and acceptor intensity behavior without blinking events, and lasted for more than 4 s were manually selected for further analysis (~20%–30% of total molecules per movie). All data was analyzed by three individuals independently and the results were compared and showed to be identical. In addition, a subset of data was blindly analyzed to ensure no bias in analysis. Apparent FRET efficiency was calculated as (IA − 0.088 × ID)/(ID + (IA − 0.088 × ID)), where ID and IA are raw donor and acceptor intensities, respectively. Experiments were conducted on three independent biological replicates, to ensure reproducibility of the results. Population smFRET histograms were generated by compiling at least 250 total FRET traces of individual molecules from all replicates. Before compiling traces, FRET histograms of individual molecules were normalized to 1 to ensure that each trace contributes equally, regardless of trace length. Error bars on histograms represent the standard error of data from three independent biological replicates.

Peak fitting analysis on population smFRET histograms was performed with OriginPro and used four Gaussian distributions as $yx=\sum_{i=1}^{4}\frac{A_{i}}{w_{i}\sqrt{\frac{\pi}{2}}}e^{-2\frac{x-xc_{i}^{2}}{w_{i}^{2}}}$ ,where A is the peak area, w is the peak width, and xc is the peak center. Peak areas were constrained to A>0. Peak widths were constrained to 0.1 ≤ w ≤ 0.25. Peak centers were constrained to ±0.015 of mean FRET efficiency of each conformational state. The mean FRET efficiencies of the inactive state, intermediate state 1, intermediate state 2, and the active state were assigned to 0.24, 0.38, 0.70, and 0.87, respectively, based on the most common FRET states observed in TDPs. This analysis is described in further detail below. State occupancy probability was calculated as area of specified peak relative to total area, which is defined as the sum of all four individual peak areas.

Raw donor, acceptor, and FRET traces were idealized with a hidden Markov model (HMM) using vbFRET software (Bronson et al., 2009; Zhang et al., 2018). Transitions, defined as ΔFRET >0.1, were extracted from idealized fits and used to generate TDPs. In situations where the HMM fit does not converge to the data (e.g. due to long fluorophore blinking events or large non-anticorrelated intensity fluctuations), traces were omitted from downstream analysis.

The cross-correlation (CC) of donor and acceptor intensity traces at time τ is defined as

$$
CC(\tau)=\frac{\deltaI_{D}(t)\deltaI_{A}(t+\tau)}{<I_{D}(t)>+<I_{A}(t)>}
$$

where $\deltaI_{D}(t)=I_{D}(t)−<I_{D}(t)>$, and $\deltaI_{A}(t)=I_{A}(t)−<I_{A}(t)>⋅<I_{D}(t)>$ and $<I_{A}(t)>$ are time average donor and acceptor intensities, respectively. Cross-correlation calculations were performed on the same traces used to generate the histograms and fit to a single exponential function, $yx=Ae^{\frac{-x}{\tau}}+y_{0}$ .

### Structural representation of allosteric binding site by Chimera

Pairwise sequence alignment for PDB:7MTS, 7MTR, 7E9G, 7EPE, and 7EPF was performed using PDB:7MTS as the reference sequence. Alignment was based on best-aligning pair of chains and used the Needleman-Wunsch alignment algorithm. Unbound subunits and extracellular domains of mGluR2 were excluded prior to structure alignment. Specifically, residues L556-I816 (PDB: 7MTS, 7MTR, 7E9G) and G564-V825 (PDB:7EPE and 7EPF) were used for alignment. Allosteric pocket forming residues are from interacting residues in PDB:7MTS and previous mutagenesis studies (Farinha et al., 2015; Seven et al., 2021).
