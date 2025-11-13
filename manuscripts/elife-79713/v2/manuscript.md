# Evaluation of in silico predictors on short nucleotide variants in HBA1, HBA2, and HBB associated with haemoglobinopathies

## Authors

- Stella Tamana<sup>1</sup> ([ORCID: 0000-0002-3414-4972](https://orcid.org/0000-0002-3414-4972))
- Maria Xenophontos<sup>1</sup> ([ORCID: 0000-0001-5978-0193](https://orcid.org/0000-0001-5978-0193))
- Anna Minaidou<sup>1</sup>
- Coralea Stephanou<sup>1</sup>
- Cornelis L Harteveld<sup>1</sup>
- Celeste Bento<sup>3</sup>
- Joanne Traeger-Synodinos<sup>4</sup> ([ORCID: 0000-0002-1860-5628](https://orcid.org/0000-0002-1860-5628))
- Irene Fylaktou<sup>5</sup>
- Norafiza Mohd Yasin<sup>6</sup>
- Faidatul Syazlin Abdul Hamid<sup>6</sup>
- Ezalia Esa<sup>6</sup>
- Hashim Halim-Fikri<sup>7</sup>
- Bin Alwi Zilfalil<sup>8</sup>
- Andrea C Kakouri<sup>1</sup>
- Marina Kleanthous<sup>1</sup>
- Petros Kountouris<sup>1</sup> ([ORCID: 0000-0003-2681-4355](https://orcid.org/0000-0003-2681-4355)) †

### Affiliations

1. Molecular Genetics Thalassaemia Department, The Cyprus Institute of Neurology and Genetics Nicosia Cyprus ([ROR:01ggsp920](https://ror.org/01ggsp920))
2. Leiden University Medical Center Leiden Netherlands ([ROR:05xvt9f17](https://ror.org/05xvt9f17))
3. Centro Hospitalar e Universitário de Coimbra Coimbra Portugal
4. Laboratory of Medical Genetics, National and Kapodistrian University of Athens Athens Greece ([ROR:04gnjpq42](https://ror.org/04gnjpq42))
5. Division of Endocrinology, Metabolism and Diabetes, First Department of Pediatrics, National and Kapodistrian University of Athens Athens Greece ([ROR:04gnjpq42](https://ror.org/04gnjpq42))
6. Haematology Unit, Cancer Research Centre, Institute for Medical Research, National Health of Institutes (NIH), Ministry of Health Malaysia Selangor Malaysia ([ROR:03bpc5f92](https://ror.org/03bpc5f92))
7. Malaysian Node of the Human Variome Project, School of Medical Sciences, Health Campus, Universiti Sains Malaysia Kelantan Malaysia ([ROR:02rgb2k63](https://ror.org/02rgb2k63))
8. Human Genome Centre, School of Medical Sciences, Health Campus, Universiti Sains Malaysia Kelantan Malaysia ([ROR:02rgb2k63](https://ror.org/02rgb2k63))

† Corresponding author

## Abstract

Haemoglobinopathies are the commonest monogenic diseases worldwide and are caused by variants in the globin gene clusters. With over 2400 variants detected to date, their interpretation using the American College of Medical Genetics and Genomics (ACMG)/Association for Molecular Pathology (AMP) guidelines is challenging and computational evidence can provide valuable input about their functional annotation. While many in silico predictors have already been developed, their performance varies for different genes and diseases. In this study, we evaluate 31 in silico predictors using a dataset of 1627 variants in HBA1, HBA2, and HBB. By varying the decision threshold for each tool, we analyse their performance (a) as binary classifiers of pathogenicity and (b) by using different non-overlapping pathogenic and benign thresholds for their optimal use in the ACMG/AMP framework. Our results show that CADD, Eigen-PC, and REVEL are the overall top performers, with the former reaching moderate strength level for pathogenic prediction. Eigen-PC and REVEL achieve the highest accuracies for missense variants, while CADD is also a reliable predictor of non-missense variants. Moreover, SpliceAI is the top performing splicing predictor, reaching strong level of evidence, while GERP++ and phyloP are the most accurate conservation tools. This study provides evidence about the optimal use of computational tools in globin gene clusters under the ACMG/AMP framework.

## Introduction

With genetic testing frequently employed by clinical laboratories to aid diagnosis and treatment decisions in different diseases (Richards et al., 2015), advances in sequencing technology produce an excessive amount of sequencing data leading to a rapidly enlarging pool of new unclassified variants. While sequencing data provide new candidates for therapeutic interventions and personalised medicine, they also introduce challenges in correctly classifying variants as pathogenic or benign. Thus, variant interpretation often relies on human expertise to gather information from different and diverse sources as to combine individual pieces of evidence into a comprehensive estimate with high confidence (Luo et al., 2019).

To assist in the establishment of a common framework for standardised variant classification, the American College of Medical Genetics and Genomics (ACMG) and the Association for Molecular Pathology (AMP) published joint recommendations for the interpretation of genetic variants (Richards et al., 2015). The ACMG/AMP framework was designed for use across different genes and diseases, thus requiring further specification in disease-specific scenarios. In response to this need, the Clinical Genome (ClinGen) Resource formed various disease-specific variant curation expert panels (VCEPs) to develop specifications to the ACMG/AMP framework (Rehm et al., 2015). The ClinGen Haemoglobinopathy VCEP focuses on performing and testing the applicability of haemoglobinopathy-specific modifications to the standard ACMG/AMP framework before proceeding with the classification and interpretation of variants related to haemoglobinopathies (Kountouris et al., 2021). Haemoglobinopathies represent the commonest groups of inherited monogenic disorders affecting approximately 7% of the global population (Cao and Kan, 2013). They are caused by genetic defects in genes located in the α-globin locus (Accession: NG_000006) and in the β-globin locus (Accession: NG_000007). To date, there are over 2400 different naturally occurring globin gene variants, which are collected and manually curated in IthaGenes, a haemoglobinopathy-specific database on the ITHANET portal (Kountouris et al., 2014).

The ACMG/AMP guidelines propose the use of in silico predictors (namely criteria PP3 and BP4 for pathogenic and benign evidence, respectively) as supporting evidence for variant pathogenicity classification (Richards et al., 2015). Several tools have already been developed to predict the impact of genetic variants and their relation to developing diseases. These tools fall into four main categories based on the theoretical background and type of data they use for predicting variant effect, namely sequence conservation-based, structure-based analysis, combined (i.e., including both sequence and structural features), and meta-predictors (Li and Wang, 2017).

The performance of different in silico tools varies across genes and diseases as numerous studies illustrated discrepancies regarding variant pathogenicity prediction (Ernst et al., 2018; Fortuno et al., 2018; Luo et al., 2019; Masica and Karchin, 2016; Pshennikova et al., 2019). Previous studies have also evaluated the performance of in silico predictors for globin gene variants (AbdulAzeez and Borgio, 2016; Tchernitchko et al., 2004), demonstrating a high degree of discordance between in silico tools. Therefore, it is evident that a disease- or gene-specific evaluation of in silico tools can provide evidence for the optimal selection or combination of tools to identify the functional impact of variants. Recently, ClinGen published a study on the performance of four in silico predictors using a set of 237 variants (Wilcox et al., 2021), suggesting that custom thresholds should be explored for each in silico tool to establish PP3 and BP4 criteria. However, given the impact of in silico tools on variant classification, further calibration with larger datasets is still needed to optimise their performance.

The main purpose of this study is to compare the performance of various in silico predictors and determine the most appropriate ones for predicting the functional impact of short nucleotide variants (SNVs) in HBA1, HBA2, and HBB related to haemoglobinopathies. To our knowledge, this is the largest comparative study of in silico tools for SNVs related to haemoglobinopathies in terms of both the number of tools used and the size of utilised variant dataset.

## Results

We selected 31 in silico predictors, including those recommended by ClinGen (Rehm et al., 2015) and linked in the Variant Curation Interface (VCI) (Preston et al., 2022), along with additional tools described in literature. A total of 1627 SNVs were retrieved from the IthaGenes database (Kountouris et al., 2017; Kountouris et al., 2014) and were annotated using a Delphi approach with respect to their pathogenicity by experts (co-authoring this study) involved in haemoglobinopathy molecular diagnosis in five different countries. The annotated pathogenicity of each SNV was then used to evaluate its predicted pathogenicity provided by in silico tools. A detailed description of the overall methodology is provided in Materials and methods and illustrated in Figure 1.

![Figure 1.](https://cdn.elifesciences.org/articles/79713/elife-79713-fig1-v2.jpg)

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/79713/elife-79713-fig1-figsupp1-v2.jpg)

### Descriptive analysis

Initially, we performed a descriptive analysis of the full dataset, including variants annotated as variants of uncertain significance (VUS), which comprised 1627 SNVs. In terms of the annotated pathogenicity, 194 (11.9%) SNVs classified as benign/likely benign (B/LB), 832 (51.1%) as pathogenic/likely pathogenic (P/LP), and 601 (36.9%) as VUS. The distribution per globin gene is the following: 553 P/LP, 77 B/LB, and 403 VUS for HBB (total: 1033 SNVs; 63.5%), 173 P/LP, 66 B/LB, and 111 VUS for HBA2 (total: 350 SNVs; 21.5%), and 106 P/LP, 51 B/LB, and 87 VUS for HBA1 (total: 245 SNVs; 15%). Figure 2 illustrates the distribution of variants on each globin gene based on their annotated pathogenicity and demonstrates the highest fraction of P/LP variant in protein coding regions and in canonical splice sites. Increased numbers of P/LP variants are also observed in specific noncoding regions of the globin genes, such as polyadenylation regions and the promoter and 5’ UTR for HBB.

![Figure 2.](https://cdn.elifesciences.org/articles/79713/elife-79713-fig2-v2.jpg)

**Figure 2.:** A bin size of 3 bp (inframe) and 5 bp in exonic and intronic regions, respectively, is used for the illustration.

Figure 3 summarises the distribution of SNVs in the dataset according to their effect on gene/protein function with respect to the annotated pathogenicity (Panel A), the annotated haemoglobinopathy group (Panel B), the thalassaemia allele phenotype (Panel C), altered oxygen affinity (Panel D), altered stability (Panel E), and the molecular mechanism involved in pathogenesis (Panel F). The effect on gene/protein function includes the following categories: (a) missense variants (SO:0001583), (b) synonymous variants (SO:0001819), (c) frameshift (SO:0001589), (d) initiation codon (SO:0000318), (e) in-frame indels (SO:0001820), (f) splicing, including cryptic splice site (SO:0001569), splice acceptor (SO:0001574), splice donor (SO:0001575) and splice region variants (SO:0001630), (g) stop lost (SO:0001578), (h) stop gained (SO:0001587), and (i) variants in regulatory elements, including promoter (SO:0001631), 5’ UTR (SO:0001623), 3’ UTR (SO:0001624), and polyadenylation variants (SO:0001545). Importantly, there are no B/LB null variants (i.e., frameshifts, stop gained, canonical splice sites, initiation codon) in the dataset, which reflects that loss-of-function is a primary disease mechanism, particularly for thalassaemia syndromes. In contrast, missense variants, representing the largest variant type category (total: 960 SNVs; 59%), are present in all pathogenicity categories, with 115 (12% of SNVs in the category), 331 (34.5%), and 514 (53.5%) annotated as B/LB, P/LP, and VUS, respectively. The distribution of missense variants in the three categories and the high percentage of missense VUS highlight the challenge to interpret the pathogenicity of missense variants in the globin genes, requiring rigorous study of available evidence, including computational evidence.

![Figure 3.](https://cdn.elifesciences.org/articles/79713/elife-79713-fig3-v2.jpg)

**Figure 3.:** (A) Variant effect on gene/protein function with respect to the annotated pathogenicity status. (B) Haemoglobinopathy group, (C) thalassaemia phenotype, (D) O2 affinity, (E) Hb stability, and (F) molecular mechanisms.

Moreover, the dataset comprises SNVs causing structural haemoglobinopathies (986 SNVs), thalassaemia (445 SNVs), and both thalassaemia and structural haemoglobinopathies (128 SNVs). The thalassaemia phenotype group describes the allele phenotype and includes HBA1 and HBA2 variants (α+/α0 and α+; total: 146 SNVs) and HBB variants (β0, β0/β+, β+, β++ (silent) and β++; total: 289 SNVs). Here, we observed that most variants have allele phenotype of α+ (130 SNVs) and β0 (184 SNVs). The category of Hb stability is further divided into hyperunstable (39 SNVs) and unstable (299 SNVs), while the Hb O2 affinity group is divided into increased O2 affinity (212 SNVs) and decreased O2 affinity (88 SNVs). The main molecular mechanisms disrupted are alterations of the secondary structure (84 SNVs), heme pocket (57 SNVs), and α1β1 interface (46 SNVs). The disruption of the molecular mechanisms has been associated with clinical phenotypes, such as haemolytic anaemia, reticulocytosis, erythrocytosis, and cyanosis (Thom et al., 2013).

### Evaluation of in silico tools as binary predictors

Table 1 shows a comparison of all in silico predictors used in this study as binary classifiers of pathogenicity, against the consensus dataset with VUS removed. For each tool, we varied the decision threshold for the whole range of possible prediction scores and calculated all statistical measures in each step (Supplementary file 2). For binary pathogenicity classification, we selected the threshold that maximised the Matthews correlation coefficient (MCC) for each tool. Accuracy ranged from 51% (FATHMM) to 84% (CADD) with a median value of 76%. The sensitivity ranged from 41% (FATHMM) to 100% (fitCons) with a median of 82.5%, while specificity ranged from 1% (fitCons) to 81% (BayesDel) with a median of 54%. High sensitivity and low specificity indicate that most predictors correctly predict the P/LP variants but misclassify the B/LB ones. MCC values ranged from 0.04 (fitCons), indicating almost random prediction, to 0.49 (CADD) with a median value of 0.32. CADD achieved the highest accuracy and MCC among all in silico tools tested, using the threshold maximising the MCC (>10.44 for pathogenic prediction), indicating good performance as a binary classifier for globin gene variants. However, this threshold is not optimal for predicting benign variants, with the achieved specificity (0.47) being below the median, hence misclassifying 101 out of 192 B/LB SNVs. Eigen-PC achieved the second highest MCC (0.44), sensitivity of 0.79, and specificity of 0.7, with decision threshold of 1.87.

**Table 1.**
 Results and performance comparison of in silico predictors with the optimal threshold based on MCC.#PV: number of predicted variants; Ac: accuracy; Se: sensitivity; Sp: specificity; MCC: Matthews correlation coefficient; LR+: positive likelihood ratio; LR-: negative likelihood ratio; 95% CI: 95% confidence interval.


<table>
  <thead>
    <tr>
      <th>Tool</th>
      <th>Decision threshold</th>
      <th>#PV</th>
      <th>TP</th>
      <th>FN</th>
      <th>FP</th>
      <th>TN</th>
      <th>Ac</th>
      <th>Se</th>
      <th>Sp</th>
      <th>MCC</th>
      <th>LR+</th>
      <th>LR +95% CI</th>
      <th>LR-</th>
      <th>LR- 95% CI</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>BayesDel_addAF</td>
      <td>≥0.39</td>
      <td>531</td>
      <td>250</td>
      <td>164</td>
      <td>22</td>
      <td>95</td>
      <td>0.65</td>
      <td>0.6</td>
      <td>0.81</td>
      <td>0.34</td>
      <td>3.21</td>
      <td>[2.19, 4.72]</td>
      <td>0.49</td>
      <td>[0.42, 0.57]</td>
    </tr>
    <tr>
      <td>CADD</td>
      <td>&gt;10.44</td>
      <td>886</td>
      <td>655</td>
      <td>39</td>
      <td>101</td>
      <td>91</td>
      <td>0.84</td>
      <td>0.94</td>
      <td>0.47</td>
      <td>0.49</td>
      <td>1.79</td>
      <td>[1.57, 2.05]</td>
      <td>0.12</td>
      <td>[0.08, 0.17]</td>
    </tr>
    <tr>
      <td>ClinPred</td>
      <td>&gt;0.95</td>
      <td>481</td>
      <td>265</td>
      <td>99</td>
      <td>43</td>
      <td>74</td>
      <td>0.7</td>
      <td>0.73</td>
      <td>0.63</td>
      <td>0.32</td>
      <td>1.98</td>
      <td>[1.55, 2.53]</td>
      <td>0.43</td>
      <td>[0.35, 0.53]</td>
    </tr>
    <tr>
      <td>Condel</td>
      <td>&gt;0.3</td>
      <td>481</td>
      <td>331</td>
      <td>33</td>
      <td>76</td>
      <td>41</td>
      <td>0.77</td>
      <td>0.91</td>
      <td>0.35</td>
      <td>0.31</td>
      <td>1.4</td>
      <td>[1.22, 1.61]</td>
      <td>0.26</td>
      <td>[0.17, 0.39]</td>
    </tr>
    <tr>
      <td>DANN</td>
      <td>&gt;0.96</td>
      <td>531</td>
      <td>372</td>
      <td>42</td>
      <td>71</td>
      <td>46</td>
      <td>0.79</td>
      <td>0.9</td>
      <td>0.39</td>
      <td>0.33</td>
      <td>1.48</td>
      <td>[1.28, 1.72]</td>
      <td>0.26</td>
      <td>[0.18, 0.37]</td>
    </tr>
    <tr>
      <td>Eigen-PC</td>
      <td>&gt;1.87</td>
      <td>531</td>
      <td>329</td>
      <td>85</td>
      <td>35</td>
      <td>82</td>
      <td>0.77</td>
      <td>0.79</td>
      <td>0.7</td>
      <td>0.44</td>
      <td>2.66</td>
      <td>[2, 3.52]</td>
      <td>0.29</td>
      <td>[0.23, 0.37]</td>
    </tr>
    <tr>
      <td>FATHMM</td>
      <td>≤–3.39</td>
      <td>481</td>
      <td>150</td>
      <td>214</td>
      <td>23</td>
      <td>94</td>
      <td>0.51</td>
      <td>0.41</td>
      <td>0.8</td>
      <td>0.19</td>
      <td>2.1</td>
      <td>[1.42, 3.08]</td>
      <td>0.73</td>
      <td>[0.65, 0.83]</td>
    </tr>
    <tr>
      <td>fathmm-MKL</td>
      <td>&gt;0.7</td>
      <td>531</td>
      <td>328</td>
      <td>86</td>
      <td>39</td>
      <td>78</td>
      <td>0.76</td>
      <td>0.79</td>
      <td>0.67</td>
      <td>0.41</td>
      <td>2.38</td>
      <td>[1.83, 3.09]</td>
      <td>0.31</td>
      <td>[0.25, 0.39]</td>
    </tr>
    <tr>
      <td>GERP++</td>
      <td>&gt;3.49</td>
      <td>531</td>
      <td>248</td>
      <td>166</td>
      <td>26</td>
      <td>91</td>
      <td>0.64</td>
      <td>0.6</td>
      <td>0.78</td>
      <td>0.31</td>
      <td>2.7</td>
      <td>[1.9, 3.82]</td>
      <td>0.52</td>
      <td>[0.44, 0.6]</td>
    </tr>
    <tr>
      <td>integrated_fitCons</td>
      <td>&gt;0.05</td>
      <td>531</td>
      <td>414</td>
      <td>1</td>
      <td>117</td>
      <td>1</td>
      <td>0.78</td>
      <td>1</td>
      <td>0.01</td>
      <td>0.04</td>
      <td>1.01</td>
      <td>[0.99, 1.02]</td>
      <td>0.28</td>
      <td>[0.02, 4.51]</td>
    </tr>
    <tr>
      <td>LIST-S2</td>
      <td>≥0.75</td>
      <td>344</td>
      <td>246</td>
      <td>28</td>
      <td>39</td>
      <td>31</td>
      <td>0.81</td>
      <td>0.9</td>
      <td>0.44</td>
      <td>0.36</td>
      <td>1.61</td>
      <td>[1.3, 1.99]</td>
      <td>0.23</td>
      <td>[0.15, 0.36]</td>
    </tr>
    <tr>
      <td>LRT</td>
      <td>&lt;0.3</td>
      <td>270</td>
      <td>169</td>
      <td>7</td>
      <td>84</td>
      <td>10</td>
      <td>0.66</td>
      <td>0.96</td>
      <td>0.11</td>
      <td>0.13</td>
      <td>1.07</td>
      <td>[1, 1.16]</td>
      <td>0.37</td>
      <td>[0.15, 0.95]</td>
    </tr>
    <tr>
      <td>MetaLR_score</td>
      <td>&gt;0.8</td>
      <td>481</td>
      <td>251</td>
      <td>113</td>
      <td>42</td>
      <td>75</td>
      <td>0.68</td>
      <td>0.69</td>
      <td>0.64</td>
      <td>0.29</td>
      <td>1.92</td>
      <td>[1.49, 2.47]</td>
      <td>0.48</td>
      <td>[0.39, 0.59]</td>
    </tr>
    <tr>
      <td>MetaSVM_score</td>
      <td>&gt;0.6</td>
      <td>481</td>
      <td>260</td>
      <td>104</td>
      <td>39</td>
      <td>78</td>
      <td>0.7</td>
      <td>0.71</td>
      <td>0.67</td>
      <td>0.34</td>
      <td>2.14</td>
      <td>[1.65, 2.79]</td>
      <td>0.43</td>
      <td>[0.35, 0.53]</td>
    </tr>
    <tr>
      <td>MutationAssessor</td>
      <td>&gt;2.53</td>
      <td>359</td>
      <td>249</td>
      <td>36</td>
      <td>41</td>
      <td>33</td>
      <td>0.79</td>
      <td>0.87</td>
      <td>0.45</td>
      <td>0.33</td>
      <td>1.58</td>
      <td>[1.28, 1.94]</td>
      <td>0.28</td>
      <td>[0.19, 0.42]</td>
    </tr>
    <tr>
      <td>MutationTaster</td>
      <td>&gt;0.95</td>
      <td>531</td>
      <td>386</td>
      <td>28</td>
      <td>102</td>
      <td>15</td>
      <td>0.76</td>
      <td>0.93</td>
      <td>0.13</td>
      <td>0.09</td>
      <td>1.07</td>
      <td>[0.99, 1.15]</td>
      <td>0.53</td>
      <td>[0.29, 0.95]</td>
    </tr>
    <tr>
      <td>MutPred</td>
      <td>&gt;0.5</td>
      <td>467</td>
      <td>343</td>
      <td>12</td>
      <td>96</td>
      <td>16</td>
      <td>0.77</td>
      <td>0.97</td>
      <td>0.14</td>
      <td>0.2</td>
      <td>1.13</td>
      <td>[1.04, 1.22]</td>
      <td>0.24</td>
      <td>[0.12, 0.49]</td>
    </tr>
    <tr>
      <td>phastCons17way</td>
      <td>&gt;0.17</td>
      <td>531</td>
      <td>357</td>
      <td>57</td>
      <td>57</td>
      <td>60</td>
      <td>0.79</td>
      <td>0.86</td>
      <td>0.51</td>
      <td>0.38</td>
      <td>1.77</td>
      <td>[1.46, 2.14]</td>
      <td>0.27</td>
      <td>[0.2, 0.36]</td>
    </tr>
    <tr>
      <td>phastCons30way</td>
      <td>&gt;0.28</td>
      <td>531</td>
      <td>329</td>
      <td>85</td>
      <td>51</td>
      <td>66</td>
      <td>0.74</td>
      <td>0.79</td>
      <td>0.56</td>
      <td>0.33</td>
      <td>1.82</td>
      <td>[1.48, 2.25]</td>
      <td>0.36</td>
      <td>[0.28, 0.47]</td>
    </tr>
    <tr>
      <td>phyloP100way</td>
      <td>&gt;0.42</td>
      <td>531</td>
      <td>349</td>
      <td>65</td>
      <td>56</td>
      <td>61</td>
      <td>0.77</td>
      <td>0.84</td>
      <td>0.52</td>
      <td>0.35</td>
      <td>1.76</td>
      <td>[1.45, 2.14]</td>
      <td>0.3</td>
      <td>[0.23, 0.4]</td>
    </tr>
    <tr>
      <td>phyloP30way</td>
      <td>&gt;0.51</td>
      <td>531</td>
      <td>307</td>
      <td>107</td>
      <td>63</td>
      <td>54</td>
      <td>0.68</td>
      <td>0.74</td>
      <td>0.46</td>
      <td>0.18</td>
      <td>1.38</td>
      <td>[1.15, 1.64]</td>
      <td>0.56</td>
      <td>[0.43, 0.72]</td>
    </tr>
    <tr>
      <td>PolyPhen-2</td>
      <td>&gt;0.65</td>
      <td>481</td>
      <td>243</td>
      <td>121</td>
      <td>37</td>
      <td>80</td>
      <td>0.67</td>
      <td>0.67</td>
      <td>0.68</td>
      <td>0.31</td>
      <td>2.11</td>
      <td>[1.6, 2.78]</td>
      <td>0.49</td>
      <td>[0.4, 0.59]</td>
    </tr>
    <tr>
      <td>PROVEAN</td>
      <td>≤–1.03</td>
      <td>481</td>
      <td>358</td>
      <td>6</td>
      <td>106</td>
      <td>11</td>
      <td>0.77</td>
      <td>0.98</td>
      <td>0.09</td>
      <td>0.18</td>
      <td>1.09</td>
      <td>[1.02, 1.15]</td>
      <td>0.18</td>
      <td>[0.07, 0.46]</td>
    </tr>
    <tr>
      <td>REVEL</td>
      <td>&gt;0.65</td>
      <td>481</td>
      <td>294</td>
      <td>70</td>
      <td>46</td>
      <td>71</td>
      <td>0.76</td>
      <td>0.81</td>
      <td>0.61</td>
      <td>0.39</td>
      <td>2.05</td>
      <td>[1.63, 2.59]</td>
      <td>0.32</td>
      <td>[0.25, 0.41]</td>
    </tr>
    <tr>
      <td>SIFT</td>
      <td>&lt;0.1</td>
      <td>481</td>
      <td>325</td>
      <td>39</td>
      <td>74</td>
      <td>43</td>
      <td>0.77</td>
      <td>0.89</td>
      <td>0.37</td>
      <td>0.3</td>
      <td>1.41</td>
      <td>[1.22, 1.63]</td>
      <td>0.29</td>
      <td>[0.2, 0.43]</td>
    </tr>
    <tr>
      <td>SiPhy_29way</td>
      <td>&gt;10.62</td>
      <td>531</td>
      <td>233</td>
      <td>181</td>
      <td>33</td>
      <td>84</td>
      <td>0.6</td>
      <td>0.56</td>
      <td>0.72</td>
      <td>0.23</td>
      <td>2</td>
      <td>[1.48, 2.7]</td>
      <td>0.61</td>
      <td>[0.52, 0.71]</td>
    </tr>
    <tr>
      <td>VEST4</td>
      <td>&gt;0.7</td>
      <td>531</td>
      <td>273</td>
      <td>141</td>
      <td>33</td>
      <td>84</td>
      <td>0.67</td>
      <td>0.66</td>
      <td>0.72</td>
      <td>0.32</td>
      <td>2.34</td>
      <td>[1.74, 3.15]</td>
      <td>0.47</td>
      <td>[0.4, 0.57]</td>
    </tr>
    <tr>
      <td colspan="15">Splicing prediction</td>
    </tr>
    <tr>
      <td>ada</td>
      <td>&gt;0.5</td>
      <td>56</td>
      <td>47</td>
      <td>3</td>
      <td>1</td>
      <td>5</td>
      <td>0.93</td>
      <td>0.94</td>
      <td>0.83</td>
      <td>0.68</td>
      <td>5.64</td>
      <td>[0.94, 33.8]</td>
      <td>0.07</td>
      <td>[0.02, 0.23]</td>
    </tr>
    <tr>
      <td>MaxEntScan</td>
      <td>Diff &gt;2 and Per &gt;5</td>
      <td>54</td>
      <td>50</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>0.95</td>
      <td>0.96</td>
      <td>0.67</td>
      <td>0.55</td>
      <td>2.88</td>
      <td>[0.58, 14.31]</td>
      <td>0.06</td>
      <td>[0.01, 0.28]</td>
    </tr>
    <tr>
      <td>rf</td>
      <td>&gt;0.6</td>
      <td>56</td>
      <td>47</td>
      <td>3</td>
      <td>1</td>
      <td>5</td>
      <td>0.93</td>
      <td>0.94</td>
      <td>0.83</td>
      <td>0.68</td>
      <td>5.64</td>
      <td>[0.94, 33.8]</td>
      <td>0.07</td>
      <td>[0.02, 0.23]</td>
    </tr>
    <tr>
      <td>SpliceAI</td>
      <td>&gt;0.65</td>
      <td>663</td>
      <td>35</td>
      <td>23</td>
      <td>1</td>
      <td>604</td>
      <td>0.96</td>
      <td>0.6</td>
      <td>1</td>
      <td>0.75</td>
      <td>365.09</td>
      <td>[50.94, 2616.41]</td>
      <td>0.4</td>
      <td>[0.29, 0.55]</td>
    </tr>
  </tbody>
</table>

When used as binary predictors, the in silico tools were unable to reach the strength level required by the Bayesian framework (Tavtigian et al., 2018) to provide supporting evidence for variant classification. Although four tools (Eigen-PC, fathmm-MKL, VEST4, MetaSVM) achieved positive likelihood ratio (LR+) higher than 2.08 and negative likelihood ratio (LR-) lower than 0.48, required for supporting evidence strength for pathogenic and benign classification, respectively, their 95% confidence intervals (95% CI) extended beyond the above thresholds and, therefore, are not recommended alone for variant interpretation. Figure 4 shows a heatmap illustrating the extent of concordance among 27 in silico tools (excluding splicing tools) and clustering of the tools based on their concordance, using the thresholds that maximised the MCC (Table 1). Notably, we observe a high degree of concordance for P/LP variants in HBB (top of the heatmap), while there is a lower degree of concordance for variants in HBA1 and HBA2 (middle of the heatmap). The bottom part of the heatmap illustrates a higher discordance for B/LB variants in HBA1 and HBA2.

![Figure 4.](https://cdn.elifesciences.org/articles/79713/elife-79713-fig4-v2.jpg)

### Performance of splicing predictors

Table 1 summarises the performance of in silico splicing tools using the threshold that maximised the MCC. With most SNVs affecting splicing regions of the globin genes annotated as P/LP, the performance of splicing tools cannot be compared reliably because of the limited number of negative examples in the dataset, that is, B/LB SVNs in splicing regions. Out of the four in silico tools tested, only SpliceAI provides a prediction score for variants that are not located near the canonical splicing sites. All splicing effect predictors displayed high accuracy, ranging from 93% (ada and rf) to 96% (SpliceAI), moderate to high sensitivity, ranging from 0.6 (SpliceAI) to 0.96 (MaxEntScan), and moderate to high specificity ranging from 0.67 (MaxEntScan) to 1 (SpliceAI). The MCC values ranged from 0.55 (MaxEntScan) to 0.75 (SpliceAI). SpliceAI achieved a high LR+ indicating strong performance in predicting SNVs disrupting splicing. The low number (≤5) of TN, FP, and FN in the predictions make the calculation of LRs for the remaining tools unreliable.

### Evaluation with different pathogenic and benign thresholds

We subsequently calibrated separate non-overlapping thresholds for pathogenic and benign prediction for each in silico tool to maximise both the percentage of variants correctly predicted by the selected threshold pairs that meet at least the supporting strength LR thresholds as defined by the Bayesian framework. More specifically, we filtered tools that achieved a lower bound 95% CI LR+ of 2.08 or higher for pathogenic prediction and an upper bound 95% CI LR- of 0.48 or lower for benign prediction. Figure 5A illustrates the changing LR values for the nine tools that reached these thresholds, while varying the decision thresholds. For these tools, we further finetuned the decision thresholds using smaller steps for the varying thresholds to maximise the number of correctly predicted SNVs. Furthermore, we tested the performance of all tools in different subsets of the dataset, including missense-only, non-missense, HBB, HBA2, and HBA1 variants. Table 2 shows all threshold pairs that reach at least supporting level of evidence for both pathogenic and benign prediction in different SNV subsets. The full analysis for all thresholds and subsets is available in the Supplementary file 2 and the finetuning of the selected tools is available in Supplementary file 3.

![Figure 5.](https://cdn.elifesciences.org/articles/79713/elife-79713-fig5-v2.jpg)

**Figure 5.:** (A) Likelihood ratios of the top performing in silico tools with variable threshold. Vertical dashed lines indicate the optimal threshold based on the highest Matthews correlation coefficient (MCC). (B) Concordant pathogenic/likely pathogenic (P/LP) calls by any given combination of in silico tools (among top performing tools) for pathogenic variants. (C) Concordant benign/likely benign (B/LB) calls by any given combination of in silico tools (among top performing tools) for benign variants. For Panels B and C, the concordance rate (i.e., variant assertion for all tools in the combination matches the expert annotation) is provided as text annotation on the bar chart. Only the first top 10 tool combinations based on concordance rate are shown, with the top three shown in blue.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/79713/elife-79713-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) Heatmap illustrating the concordance and clustering of the top performing in silico tools with respect to the variant type and globin gene, using the separate non-overlapping thresholds for pathogenic and benign prediction, as shown in Table 2. (B) Prediction of variants of uncertain significance (VUS) using thresholds for the full dataset (at supporting strength).

**Table 2.**
 In silico tools with pairs of non-overlapping thresholds that reach at least supporting evidence strength for both pathogenic and benign prediction.LR: likelihood ratio; CI: confidence interval; PV: predicted variants.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="5">Pathogenic prediction</th>
      <th colspan="5">Benign Prediction</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Tool</td>
      <td>Pathogenic threshold</td>
      <td>Sensitivity</td>
      <td>LR+</td>
      <td>LR+ 95% CI</td>
      <td>Strength (pathogenic)</td>
      <td>Benign threshold</td>
      <td>Specificity</td>
      <td>LR-</td>
      <td>LR- 95% CI</td>
      <td>Strength (benign)</td>
      <td>Correctly PV</td>
      <td>% of correctly PV</td>
    </tr>
    <tr>
      <td colspan="13">All SNVs</td>
    </tr>
    <tr>
      <td>BayesDel_addAF</td>
      <td>≥0.39</td>
      <td>0.6</td>
      <td>3.21</td>
      <td>[2.19, 4.72]</td>
      <td>Supporting</td>
      <td>&lt;0.23</td>
      <td>0.44</td>
      <td>0.35</td>
      <td>[0.26, 0.47]</td>
      <td>Supporting</td>
      <td>302</td>
      <td>56.87</td>
    </tr>
    <tr>
      <td>CADD</td>
      <td>&gt;25</td>
      <td>0.39</td>
      <td>8.27</td>
      <td>[4.34, 15.75]</td>
      <td>Moderate</td>
      <td>≤21.75</td>
      <td>0.78</td>
      <td>0.42</td>
      <td>[0.37, 0.48]</td>
      <td>Supporting</td>
      <td>418</td>
      <td>47.18</td>
    </tr>
    <tr>
      <td>CADD</td>
      <td>&gt;16.3</td>
      <td>0.82</td>
      <td>2.59</td>
      <td>[2.1, 3.2]</td>
      <td>Supporting</td>
      <td>≤16.3</td>
      <td>0.68</td>
      <td>0.26</td>
      <td>[0.21, 0.31]</td>
      <td>Supporting</td>
      <td>703</td>
      <td>79.35</td>
    </tr>
    <tr>
      <td>Eigen-PC</td>
      <td>&gt;1.9</td>
      <td>0.79</td>
      <td>3</td>
      <td>[2.21, 4.07]</td>
      <td>Supporting</td>
      <td>≤1.9</td>
      <td>0.74</td>
      <td>0.28</td>
      <td>[0.22, 0.35]</td>
      <td>Supporting</td>
      <td>415</td>
      <td>78.15</td>
    </tr>
    <tr>
      <td>GERP++</td>
      <td>&gt;4.22</td>
      <td>0.44</td>
      <td>4.33</td>
      <td>[2.51, 7.49]</td>
      <td>Supporting</td>
      <td>≤0.15</td>
      <td>0.35</td>
      <td>0.32</td>
      <td>[0.22, 0.46]</td>
      <td>Supporting</td>
      <td>225</td>
      <td>42.37</td>
    </tr>
    <tr>
      <td>MetaSVM</td>
      <td>&gt;0.81</td>
      <td>0.55</td>
      <td>3.25</td>
      <td>[2.16, 4.89]</td>
      <td>Supporting</td>
      <td>≤0.46</td>
      <td>0.6</td>
      <td>0.38</td>
      <td>[0.3, 0.48]</td>
      <td>Supporting</td>
      <td>272</td>
      <td>56.55</td>
    </tr>
    <tr>
      <td>phyloP100way</td>
      <td>&gt;7.32</td>
      <td>0.15</td>
      <td>17.8</td>
      <td>[2.5, 127]</td>
      <td>Supporting</td>
      <td>≤0.8</td>
      <td>0.57</td>
      <td>0.36</td>
      <td>[0.28, 0.46]</td>
      <td>Supporting</td>
      <td>130</td>
      <td>24.48</td>
    </tr>
    <tr>
      <td>REVEL</td>
      <td>&gt;0.77</td>
      <td>0.63</td>
      <td>3.05</td>
      <td>[2.12, 4.4]</td>
      <td>Supporting</td>
      <td>≤0.7</td>
      <td>0.69</td>
      <td>0.38</td>
      <td>[0.31, 0.47]</td>
      <td>Supporting</td>
      <td>309</td>
      <td>64.24</td>
    </tr>
    <tr>
      <td>SpliceAI</td>
      <td>&gt;0.3</td>
      <td>0.67</td>
      <td>58.12</td>
      <td>[27.23, 124.03]</td>
      <td>Strong</td>
      <td>≤0.3</td>
      <td>0.99</td>
      <td>0.33</td>
      <td>[0.23, 0.48]</td>
      <td>Supporting</td>
      <td>637</td>
      <td>96.08</td>
    </tr>
    <tr>
      <td colspan="13">Missense only</td>
    </tr>
    <tr>
      <td>BayesDel_addAF</td>
      <td>≥0.41</td>
      <td>0.54</td>
      <td>3.35</td>
      <td>[2.2, 5.12]</td>
      <td>Supporting</td>
      <td>&lt;0.22</td>
      <td>0.44</td>
      <td>0.32</td>
      <td>[0.23, 0.45]</td>
      <td>Supporting</td>
      <td>241</td>
      <td>51.72</td>
    </tr>
    <tr>
      <td>CADD</td>
      <td>&gt;23.25</td>
      <td>0.6</td>
      <td>3.19</td>
      <td>[2.17, 4.69]</td>
      <td>Supporting</td>
      <td>≤20.9</td>
      <td>0.62</td>
      <td>0.36</td>
      <td>[0.28, 0.46]</td>
      <td>Supporting</td>
      <td>283</td>
      <td>60.6</td>
    </tr>
    <tr>
      <td>Eigen-PC</td>
      <td>&gt;1.9</td>
      <td>0.78</td>
      <td>2.93</td>
      <td>[2.16, 3.98]</td>
      <td>Supporting</td>
      <td>≤1.9</td>
      <td>0.74</td>
      <td>0.3</td>
      <td>[0.24, 0.38]</td>
      <td>Supporting</td>
      <td>357</td>
      <td>76.61</td>
    </tr>
    <tr>
      <td>GERP++</td>
      <td>&gt;4.22</td>
      <td>0.44</td>
      <td>4.27</td>
      <td>[2.47, 7.4]</td>
      <td>Supporting</td>
      <td>≤–0.87</td>
      <td>0.29</td>
      <td>0.31</td>
      <td>[0.2, 0.47]</td>
      <td>Supporting</td>
      <td>187</td>
      <td>40.13</td>
    </tr>
    <tr>
      <td>MetaSVM</td>
      <td>&gt;0.8</td>
      <td>0.58</td>
      <td>3.08</td>
      <td>[2.09, 4.53]</td>
      <td>Supporting</td>
      <td>≤0.39</td>
      <td>0.56</td>
      <td>0.37</td>
      <td>[0.29, 0.48]</td>
      <td>Supporting</td>
      <td>267</td>
      <td>57.3</td>
    </tr>
    <tr>
      <td>phastCons30way</td>
      <td>&gt;0.94</td>
      <td>0.52</td>
      <td>3.19</td>
      <td>[2.09, 4.88]</td>
      <td>Supporting</td>
      <td>≤0.41</td>
      <td>0.61</td>
      <td>0.36</td>
      <td>[0.28, 0.46]</td>
      <td>Supporting</td>
      <td>252</td>
      <td>54.08</td>
    </tr>
    <tr>
      <td>phyloP100way</td>
      <td>&gt;7.32</td>
      <td>0.16</td>
      <td>19.11</td>
      <td>[2.68, 136.47]</td>
      <td>Supporting</td>
      <td>≤0.56</td>
      <td>0.53</td>
      <td>0.35</td>
      <td>[0.27, 0.46]</td>
      <td>Supporting</td>
      <td>119</td>
      <td>25.54</td>
    </tr>
    <tr>
      <td>REVEL</td>
      <td>&gt;0.77</td>
      <td>0.62</td>
      <td>3.02</td>
      <td>[2.09, 4.35]</td>
      <td>Supporting</td>
      <td>≤0.7</td>
      <td>0.69</td>
      <td>0.39</td>
      <td>[0.32, 0.48]</td>
      <td>Supporting</td>
      <td>297</td>
      <td>63.73</td>
    </tr>
    <tr>
      <td colspan="13">Non-missense only</td>
    </tr>
    <tr>
      <td>CADD</td>
      <td>&gt;11.5</td>
      <td>0.93</td>
      <td>8.62</td>
      <td>[3.42, 21.77]</td>
      <td>Supporting</td>
      <td>≤11.5</td>
      <td>0.89</td>
      <td>0.08</td>
      <td>[0.05, 0.11]</td>
      <td>Supporting</td>
      <td>350</td>
      <td>92.84</td>
    </tr>
    <tr>
      <td colspan="13">SNVs in HBB</td>
    </tr>
    <tr>
      <td>BayesDel_addAF</td>
      <td>≥0.31</td>
      <td>0.8</td>
      <td>6.43</td>
      <td>[2.23, 18.58]</td>
      <td>Supporting</td>
      <td>&lt;0.31</td>
      <td>0.88</td>
      <td>0.22</td>
      <td>[0.17, 0.3]</td>
      <td>Supporting</td>
      <td>210</td>
      <td>81.08</td>
    </tr>
    <tr>
      <td>CADD</td>
      <td>&gt;25.25</td>
      <td>0.42</td>
      <td>31.64</td>
      <td>[4.5, 222.38]</td>
      <td>Moderate</td>
      <td>≤22.65</td>
      <td>0.92</td>
      <td>0.42</td>
      <td>[0.37, 0.48]</td>
      <td>Supporting</td>
      <td>264</td>
      <td>48.71</td>
    </tr>
    <tr>
      <td>CADD</td>
      <td>&gt;10.8</td>
      <td>0.94</td>
      <td>3.26</td>
      <td>[2.29, 4.64]</td>
      <td>Supporting</td>
      <td>≤10.8</td>
      <td>0.71</td>
      <td>0.08</td>
      <td>[0.05, 0.12]</td>
      <td>Supporting</td>
      <td>494</td>
      <td>91.14</td>
    </tr>
    <tr>
      <td colspan="13">SNVs in HBA1</td>
    </tr>
    <tr>
      <td>CADD</td>
      <td>&gt;22.95</td>
      <td>0.59</td>
      <td>4.94</td>
      <td>[2.29, 10.68]</td>
      <td>Supporting</td>
      <td>≤17</td>
      <td>0.66</td>
      <td>0.3</td>
      <td>[0.19, 0.48]</td>
      <td>Supporting</td>
      <td>84</td>
      <td>61.76</td>
    </tr>
  </tbody>
</table>

Notably, CADD is the only tool that reached a moderate level of evidence (LR+ lower bound 95% CI ≥4.33) for prediction of pathogenic variants (threshold >25), while BayesDel, Eigen-PC, GERP++, REVEL, MetaSVM, phyloP100way and CADD (with a lower threshold of 16.3) have also reached the supporting evidence strength. Importantly, CADD (at supporting strength), Eigen-PC and REVEL correctly predict the highest number of SNVs with 79.35%, 78.15%, and 64.24%, respectively. In addition, CADD and Eigen-PC achieve the highest sensitivity for pathogenic prediction with 0.82 (CADD threshold >16.3) and 0.79, respectively, as well as the highest specificity for benign prediction with 0.78 (CADD threshold ≤21.75) and 0.74, respectively. Moreover, SpliceAI reached strong level of evidence for splicing prediction (threshold >0.3), correctly predicting 96.08% of all variants, with a sensitivity of 0.67 and a specificity of 0.99.

When evaluating the performance of tools on the subset of missense variants, we identified eight tools (BayesDel, Eigen-PC, GERP++, MetaSVM, REVEL, CADD, phyloP100way, and phastCons30way) that reached supporting strength level. Eigen-PC, REVEL, and CADD achieved the highest percentages of correctly predicted SNVs with 76.61%, 63.73%, and 60.6%, respectively. Moreover, CADD performed well for non-missense variants where a single threshold of 11.5 produced an accuracy of 92.84%, while achieving supporting strength.

With regards to the gene-specific analysis, BayesDel and CADD performed well for the prediction of HBB variants using a single threshold and accuracies of 81.08% and 91.14%, respectively, with CADD achieving moderate strength for pathogenic prediction with a threshold of 25.25. Furthermore, CADD achieved supporting strength for SNVs in HBA1, whilst no tool reached the required LR thresholds for HBA2.

Figure 5B and C shows the concordance among the top performing tools of this study for pathogenic and benign prediction, respectively, using the recommended thresholds shown in Table 2 (full dataset; supporting strength thresholds). Although the overall concordance is low, some tools, such as Eigen-PC and REVEL, have higher concordance rates for both pathogenic (54.8%) and benign (65.8%) prediction. This is also demonstrated in the heatmap of Figure 5—figure supplement 1A illustrating the concordance of the top performing tools using the recommended thresholds. A higher degree of concordance is observed for P/LP variants in HBB (top and middle of the heatmap). The low concordance rate of the top performing tools is also reflected in the prediction of VUS (Figure 5—figure supplement 1B), where differences in the distribution of predicted pathogenicity classes are observed among in silico tools. Nonetheless, this will be further assessed when the pathogenicity status of these SNVs is clarified.

## Discussion

The main goal of this study was to assess the performance of in silico prediction tools in the context of haemoglobinopathy-specific SNVs and to provide evidence to the ClinGen Hemoglobinopathy VCEP for the most appropriate use of computational evidence in variant interpretation based on the ACMG/AMP guidelines. We evaluated the performance of 31 in silico predictors on a set of 1627 haemoglobinopathy-specific SNVs. The pathogenicity of these variants was assessed using a Delphi approach by haemoglobinopathy experts based on literature review and experimental evidence.

Our comparative analysis showed that, when used as binary predictors of pathogenicity, most tools have high sensitivity and accuracy but suffer from poor specificity. We show that binary classification results in low LRs for most tools and, thus, cannot be used alone based on the Bayesian framework for variant classification (Tavtigian et al., 2018). Instead, as we demonstrated in this study, stronger evidence is obtained when we trichotomised the problem by independently defining different non-overlapping thresholds for pathogenic and benign prediction of globin gene variants. This approach was previously described by other ClinGen VCEPs, evaluating sequence variants in other genes (Johnston et al., 2021; Pejaver et al., 2022) and, despite reducing the overall percentage of predicted variants, it increases the confidence of pathogenic and benign predictions because of higher LR values than the corresponding binary classifications. Our findings show that Eigen-PC, REVEL, and CADD performed well for predicting the functional effect of missense SNVs, while CADD was also a strong predictor of non-missense variants. Meta-predictors BayesDel and MetaSVM were also strong performers in our comparison, while GERP++, phyloP100way, and phastCons30way performed better among the conservation tools, albeit with a lower overall accuracy. Out of the four splicing prediction tools evaluated, SpliceAI performed better and produced the highest LR+ values reaching strong level of evidence. However, due to the low number of negative examples in our dataset for the other splicing tools evaluated, these results should be interpreted with caution. Our results show that SpliceAI is a reliable predictor of the splicing impact of SNVs in the globin genes.

In line with previous studies, our results reinforce the observation that several in silico predictors when utilised for binary variant classification perform differently for benign and pathogenic variants, by favoring the classification of variants as pathogenic (Ghosh et al., 2017; Gunning et al., 2021). The problem of false concordance has been widely reported in previous studies (Ghosh et al., 2017) and can be attributed to several reasons. Firstly, several in silico predictors do not directly predict the variant pathogenicity (i.e., the clinical effect) of a variant, but instead provide a prediction on how a variant affects a protein domain or reduces its catalytic activity, thus inferring it is damaging to protein function (Ernst et al., 2018; Ghosh et al., 2017; Shi et al., 2019; van der Velde et al., 2015). Moreover, low concordance may also arise due to variants with different allele frequencies, as studies have shown a strong correlation between specificity and allele frequency (Gunning et al., 2021; Niroula and Vihinen, 2019). In addition, data circularity can affect tools performance, with Ghosh R and colleagues showing that prediction efficacy is partly depended on the distribution of pathogenic and benign variants in a dataset (Ghosh et al., 2017).

In this study, we observed lower concordance for HBA1/HBA2 compared to HBB. This can be attributed to the fact that the pathogenicity of variants in HBA1/HBA2 is often less clear in the heterozygous state due to the number of genes involved (i.e., four copies of HBA1/HBA2 compared to two copies of HBB). Therefore, a variant on HBA1/HBA2 can be damaging at the gene level (e.g., reduced expression), with this effect not often being reflected on the phenotypic level in the heterozygous state. This is also reflected by the number of variants annotated with two stars in ClinVar, as previously highlighted by the ClinGen Hemoglobinopathy VCEP (Kountouris et al., 2021).

Notably, our analyses showed that meta-predictors, such as Eigen-PC, REVEL, and CADD, outperformed other tools. This category of algorithms uses the results of other individual prediction tools as features, thus integrating different types of information (e.g., conservation and sequence information) in the prediction model. The performance of meta-predictors is robust regardless of technical artifacts, levels of constraint on genes, variant type, and inheritance pattern mainly because their prediction scores are derived from weighing and combining multiple features and predictors (Ghosh et al., 2017; Gunning et al., 2021). However, as noted in previous studies, combinations of meta-predictors and any of the tools or conservation-based algorithms already incorporated in meta-predictors is not recommended, as it is more likely to yield discordant predictions and duplication in the analyses (Ghosh et al., 2017; Gunning et al., 2021).

The annotated pathogenicity of the variants in our dataset was based on criteria agreed by all co-authors of this paper. These criteria are not based on the ACMG/AMP framework, because there is currently no available standard for pathogenicity classification of globin gene variants. The ClinGen Hemoglobinopathy VCEP is currently piloting its ACMG/AMP specifications, which can be used for variant classification in the future, thus potentially leading to reassessment of in silico predictors for globin genes variants. Nevertheless, the current classification reflects the current knowledge about the pathogenicity of the variants in our dataset, agreed by experts involved in the molecular diagnosis of haemoglobinopathies in five countries (Cyprus, Greece, Malaysia, Netherlands, and Portugal). A potential limitation is that some benign variants have not been observed in trans with both a β-thalassaemia variant and the Hb S variant and, therefore, their pathogenicity is assigned based on the current knowledge in the field. However, our approach is justified, because small numbers of true benign SNVs reflect the reality in clinical diagnostics, where pathogenic SNVs associated with clinical phenotypes are more easily interpreted than benign ones.

This study provides evidence for the selection of the most suitable in silico tools for the interpretation of SNVs in the globin gene clusters using the ACMG/AMP guidelines. Specifically, we provide the optimal thresholds for different tools that can be used under the PP3/BP4 criteria, including missense and splicing variant interpretation, while optimal thresholds for conservation-based tools are also critical for the application of criterion BP7. To our knowledge, this is the largest study evaluating the disease-specific application of in silico predictors in variant classification under the ACMG/AMP framework and its associated Bayesian framework. Our approach can be further expanded for the optimal calibration of thresholds of in silico tools in other genes and diseases, hence facilitating variant interpretation using the ACMG/AMP framework.

## Materials and methods

### Dataset

Figure 1 shows a schematic representation of the main steps of our methodology. SNVs were retrieved from the IthaGenes database of the ITHANET portal (Kountouris et al., 2017; Kountouris et al., 2014). The dataset includes all SNVs (≤50 bp) curated in IthaGenes (access date: 05/02/2021) located in HBA1, HBA2, and HBB, excluding (a) disease-modifying variants, (b) complex variants with multiple DNA changes found in cis, and (c) variants whose genomic location is unclear, such as α-chain variants identified by protein studies without identifying the affected α-globin gene.

Additionally, we queried ClinVar (access date: 05/02/2021) (Landrum et al., 2018) for SNVs with a two-star review status and gnomAD (access date: 05/02/2021) (Karczewski et al., 2020) for benign/likely benign SNVs using PopMax Filtering Allele Frequency greater than 1% in HBA1, HBA2, and HBB. Any missing SNVs were added to both IthaGenes and the dataset of this study. The final dataset included 1627 distinct SNVs. Finally, the dataset was further processed using the batch service of Variant Validator (Freeman et al., 2018) to validate the HGVS names and correct any annotation errors.

### Annotated variant pathogenicity

To enable the evaluation of in silico predictions, we subsequently annotated the pathogenicity of each SNV and compared it to the results of in silico predictors. Specifically, we used existing curated information on IthaGenes and further collected available evidence in scientific literature for each SNV in the dataset. The pathogenicity for each SNV was annotated using the following criteria:

The SNV pathogenicity annotations produced in the above step (henceforth denoted as initial classification) were subsequently further assessed and reevaluated by the experts. We used a Delphi approach (Dalkey and Helmer, 1963) to allow independent evaluation of the curated evidence for each variant. The pathogenicity of each SNV was independently assessed by two different groups of haemoglobinopathy experts, using evidence curated by the IthaGenes database or collected as part of this study. Then, the independent expert annotations were merged into one final consensus classification. In cases of disagreement, a consensus pathogenicity status was decided, after discussion among all experts, or the SNV was marked as a VUS. SNVs that have been directly submitted to IthaGenes by experts not participating in this study and without a peer-reviewed publication describing the methodology and results, have been also annotated as VUS. Figure 1—figure supplement 1 illustrates the changes in pathogenicity annotation after the expert evaluation, demonstrating that most changes involved variants that were initially classified as VUS and were reclassified as P/LP or B/LB in the final annotation. The final consensus pathogenicity classifications produced for all SNV in this study have been added to the IthaGenes database and was used throughout this study. After descriptive analysis of the full dataset, 601 SNVs annotated as VUS were filtered out of the dataset.

For the evaluation of tools predicting the impact of variants on splicing, we further annotated variants with respect to their effect on gene/protein function and assembled the following datasets:

For SpliceAI, we selected the highest of the four Delta Scores provided as output, while for MaxEntScan we used two different thresholds as follows: (a) the absolute difference between the reference and alternative allele (denoted as Diff), and (b) the absolute percentage of change between the reference and alternative allele (denoted as Per) (Tey and Ng, 2019).

### In silico prediction tools

Thirty-one in silico predictors were compared in this study, as follows: ada (Jian et al., 2014), BayesDel (Feng, 2017), CADD (Kircher et al., 2014), ClinPred (Alirezaie et al., 2018), CONDEL (González-Pérez and López-Bigas, 2011), DANN (Quang et al., 2015), EIGEN-PC (Ionita-Laza et al., 2016), FATHMM (Shihab et al., 2013), FATHMM-MKL (Shihab et al., 2015), fitCons (Gulko et al., 2015), GERP++ (Davydov et al., 2010), LIST-S2 (Malhis et al., 2020), LRT (Chun and Fay, 2009), MaxEntScan (Yeo and Burge, 2004), Meta-SVM (Kim et al., 2017), MetaLR (Dong et al., 2015), MutationAssessor (Reva et al., 2011), MutationTaster (Schwarz et al., 2014), MutPred2 (Pejaver et al., 2020), PolyPhen-2 (Adzhubei et al., 2010), PROVEAN (Choi et al., 2012), REVEL (Ioannidis et al., 2016), rf (Jian et al., 2014), SIFT (Ng and Henikoff, 2003), SpliceAI (Jaganathan et al., 2019), VEST4 (Carter et al., 2013), phastCons (phastCons17way and phastCons30way) (Ramani et al., 2019), phyloP (phyloP100way and phyloP30way) (Ramani et al., 2019), and SiPhy_29way (Garber et al., 2009). Four of the tools are focused on predicting the splicing impact of a variant (ada, MaxEntScan, rf, and SpliceAI), while six tools produce conservation scores (GERP++, phastCons17way, phastCons30way, phyloP100way, phyloP30way, and SiPhy_29way). We selected in silico tools recommended by ClinGen and available in the ClinGen VCI (Preston et al., 2022), as well as additional established tools used in previous studies. We employed the online version of the Ensembl VEP (McLaren et al., 2016) and its dbNSFP (Liu et al., 2020) plugin (version 4.2a) to obtain the prediction scores of the variants in our dataset.

### Predictive performance assessment

Commonly used scalar measures were employed to compare the prediction accuracy of in silico tools, including specificity, sensitivity, and accuracy. All of them can be derived from two or more of the following quantities: (a) true positives (TP), the number of correctly predicted P/LP variants; (b) true negatives (TN), the number of correctly predicted B/LB variants; (c) false positives (FP), the number of B/LB variants incorrectly predicted as P/LP; (d) false negatives (FN), the number of P/LP variants incorrectly predicted as B/LB. Specificity is defined as the fraction of correctly predicted B/LB variants, sensitivity is the fraction of correctly predicted P/LP variants, and accuracy is the ratio of correct predictions versus the total number of predictions (Hassan et al., 2019).

Moreover, we used the MCC (Matthews, 1975) to compare the performance of in silico predictors. MCC ranges from –1 (i.e., always falsely predicted) to 1 (i.e., perfectly predicted) with a value of 0 corresponding to random prediction. MCC is considered one of the most robust measures to evaluate binary classifiers (Chicco and Jurman, 2020). Hence, in our analysis, the optimal threshold for binary classification was the one that maximised the MCC for each in silico tool.

Following the guidelines of a Bayesian variant classification framework (Tavtigian et al., 2018), LRs for pathogenic (LR+) and benign (LR-) outcomes were calculated for each tool to evaluate the evidence strength of their pathogenicity prediction using the odds of pathogenicity (OddsP) in the Bayesian framework. According to the Bayesian framework, the strength of OddsP for each evidence level was set as follows: ‘Very Strong’ (350:1), ‘Strong’ (18.7:1), ‘Moderate’ (4.33:1), and ‘Supporting’ (2.08:1).

### Comparative analysis

The analysis was separated into three parts. First, we performed descriptive analysis of the dataset, including variants annotated as VUS, based on the variant type, the variant effect on gene/protein function, the haemoglobinopathy disease group, thalassemia phenotype, molecular mechanism, and annotated pathogenicity. Subsequently, we removed variants annotated as VUS and we compared the 31 in silico tools as binary predictors of variant pathogenicity by selecting the threshold that maximised the MCC for each tool. For predictors whose output scores ranged from 0 to 1, we used thresholds with intervals of 0.05, whereas for predictors with scores falling outside this range, we set custom ranges based on the observed minimum and maximum scores in our dataset. Finally, we identified separate non-overlapping thresholds for prediction of pathogenic and benign effect as recommended by the Bayesian framework for variant interpretation (Tavtigian et al., 2018), by selecting thresholds passing the recommended LR+ and LR- thresholds, while maximising the percentage of correctly predicted variants for each tool. For tools passing the LR thresholds, we further finetuned the decision thresholds using smaller steps to optimise the prediction accuracy. Statistical analysis and visualisation of the results were performed using custom R scripts and the epiR package.

### Data availability statement

All data generated or analysed during this study are included in Supporting File 2 and Supporting File 3. Supporting File 2 provides the full dataset and subsets used as input in the analysis (sheet names starting with ‘Input’) as well as the results of the analysis (sheets starting with ‘On’). Supporting File 3 includes the finetuning analysis for specific tools and data subsets, as described in the manuscript.

We make the source code for evaluating the tools and generating the figures presented herein, freely available at https://github.com/cing-mgt/evaluation-of-in-silico-predictors, (Tamana et al., 2022 copy archived at swh:1:rev:c3d397be71733aaeaa3738c979899b1f23f7457f).
