# A serine sensor for multicellularity in a bacterium

## Authors

- Arvind R Subramaniam<sup>1</sup>
- Aaron DeLoughery<sup>1</sup>
- Niels Bradshaw<sup>1</sup>
- Yun Chen<sup>1</sup>
- Erin O’Shea<sup>1</sup>
- Richard Losick<sup>1</sup> †
- Yunrong Chai<sup>1</sup> †

### Affiliations

1. Department of Molecular and Cellular Biology Harvard University Cambridge United States
2. Faculty of Arts and Sciences Center for Systems Biology Harvard University Cambridge United States
3. Department of Chemistry and Chemical Biology Harvard University Cambridge United States
4. Howard Hughes Medical Institute, Harvard University Cambridge United States
5. Department of Biology Northeastern University Boston United States

† Corresponding author

## Abstract

We report the discovery of a simple environmental sensing mechanism for biofilm formation in the bacterium Bacillus subtilis that operates without the involvement of a dedicated RNA or protein. Certain serine codons, the four TCN codons, in the gene for the biofilm repressor SinR caused a lowering of SinR levels under biofilm-inducing conditions. Synonymous substitutions of these TCN codons with AGC or AGT impaired biofilm formation and gene expression. Conversely, switching AGC or AGT to TCN codons upregulated biofilm formation. Genome-wide ribosome profiling showed that ribosome density was higher at UCN codons than at AGC or AGU during biofilm formation. Serine starvation recapitulated the effect of biofilm-inducing conditions on ribosome occupancy and SinR production. As serine is one of the first amino acids to be exhausted at the end of exponential phase growth, reduced translation speed at serine codons may be exploited by other microbes in adapting to stationary phase.

## Introduction

Bacteria constantly monitor their environment and internal physiological state so that they can adapt to changing conditions. A wide variety of sensing mechanisms are deployed for this purpose, including dedicated protein sensors, such as histidine kinases, which mediate changes in gene expression by controlling the phosphorylation of cognate response regulators in response to environmental cues (West and Stock, 2001). Bacteria also sense changes in their environment and physiology by means of dedicated RNAs, such as the highly structured, leader RNA for the tryptophan operon, which controls the transcription of downstream genes in the operon by a mechanism involving ribosome stalling at tryptophan codons (Henkin and Yanofsky, 2002). Here we report the discovery of an unusually simple mechanism of environmental sensing involved in the process of biofilm formation by the bacterium B. subtilis that does not require a dedicated RNA or protein.

Biofilm formation involves a switch from planktonic growth as individual cells to the formation of complex, multicellular communities in response to environmental cues (Kolter and Greenberg, 2006). In B. subtilis, these communities are embedded in a self-produced matrix consisting of polysaccharide and an amyloid-like protein, which are specified by the epsA-O and the tapA-sipW-tasA operons, respectively (Branda et al., 2001; Kearns et al., 2005). The transition to multicellularity is governed in part by four histidine kinases (KinA, KinB, KinC and KinD) that control the phosphorylation of the response regulator, Spo0A, a master regulator of post-exponential phase gene expression (Figure 1A) (Jiang et al., 2000; Vlamakis et al., 2013). Recent studies suggest that KinA and KinB respond to impaired respiration (Kolodkin-Gal et al., 2013), whereas KinC responds to membrane perturbations and KinD to unknown chemical signals (López et al., 2009; Shemesh et al., 2010; Chen et al., 2012; Beauregard et al., 2013). Once phosphorylated, Spo0A turns on sinI, a gene encoding a small protein antagonist of the biofilm-specific regulatory protein SinR (Molle et al., 2003; Kearns et al., 2005). SinR, which is produced constitutively, is a repressor of the matrix operons, epsA-O and the tapA-sipW-tasA, as well as other biofilm-related genes (Kearns et al., 2005; Chu et al., 2006; Chai et al., 2009). SinR is also a repressor of the gene for SlrR (Chu et al., 2008), which together with SinR sets up a self-reinforcing, double-negative feedback loop for matrix gene expression (Figure 1A) (Chai et al., 2010; Norman et al., 2013). A special feature of SinR of relevance to this investigation is that the expression of matrix genes is hypersensitive to small perturbations in the level of the protein (Chai et al., 2011). This hypersensitivity is attributed to molecular titration of SinR by SinI and cooperativity among SinR molecules bound to tandem target sequences at regulatory sites for the matrix operons (Chai et al., 2011; Chai et al., 2008).

![Figure 1.](https://cdn.elifesciences.org/articles/01501/elife-01501-fig1-v1.jpg)

**Figure 1.:** (A) Regulatory circuit controlling biofilm formation in B. subtilis. (B) Top: Serine codon usage in the sinR coding sequence. Number within parenthesis indicates the frequency of the corresponding codon in sinR. Bottom: Average serine codon usage across 4153 protein-coding sequences in the B. subtilis genome. Number within parenthesis indicates the relative frequency of each codon in the genome. (C) Colony morphology for the wild-type strain and the indicated sinR synonymous variants grown on solid biofilm-inducing medium. Three TCA codons in the wild-type sequence of sinR were switched to each of the other five serine codons. The wild-type (WT) sinR sequence was replaced by the sinR synonymous mutant at the native sinR locus of the strain 3610. (D) SinR protein level during entry into biofilm formation (OD600 = 2) measured using an anti-SinR antibody that also cross-reacts with SlrR, a protein that is 85% identical to SinR. Western blot against the RNA polymerase subunit SigA was used as the loading control. Whole cell lysates were loaded at different dilutions (indicated as X, X/2, and X/3). (E) Densitometry of SinR bands in (D) after normalization by SigA. (F) Top panel: Western blot against SinR and SlrR using anti-SinR antibody. Bottom panel: Densitometry ratio of the SlrR and SinR bands in the top panel. Error bars represent standard error over three replicate Western blots. The SlrR/SinR ratio for each blot was normalized such that the wild-type strain had a ratio of 1. (G) Matrix gene expression monitored using a PepsA–lacZ transcriptional reporter inserted at the chromosomal amyE locus. β-galactosidase activity was measured at OD600 = 2 in liquid biofilm-inducing medium. Error bars represent standard error of three measurements.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/01501/elife-01501-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** The three TCA codons (switched in Figure 1) are highlighted in red. The three TCC codons and the two AGC/AGT codons (switched in Figure 1—figure supplement 2) are highlighted in green and blue respectively. The remaining serine codons are shown in yellow.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/01501/elife-01501-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** (A) Colony morphology for the indicated sinR synonymous variants grown on solid biofilm-inducing medium. Either three TCC codons or two AGC/AGT (AGY) codons in the wild-type sequence of sinR were switched to remaining serine synonymous codons. The wild-type (WT) sinR sequence was replaced by the sinR synonymous variant at the native sinR locus of the strain 3610. Colony morphology of the wild-type strain is shown in Figure 1. (B and C) Matrix gene expression monitored using a PepsA–lacZ transcriptional reporter inserted at the chromosomal amyE locus. Strains were grown in liquid biofilm-inducing medium and β-galactosidase activity was measured at an OD600 = 2. Error bars represent standard error of three measurements. The synonymous variants highlighted in red do not follow the hierarchy between TCN and AGC/AGT codons seen for the six TCA synonymous variants in Figure 1.

In the current study, we present evidence for the existence of a novel cellular sensing mechanism controlling biofilm formation. Rather than relying on regulation by a dedicated RNA or protein, the translation speed of ribosomes decreases at certain serine codons, resulting in lower SinR levels, which as a consequence, contributes to derepression of SinR-controlled genes. We propose that specific serine codons in the sinR mRNA act as a simple sensor for monitoring, and triggering a response to, serine depletion under biofilm-inducing conditions.

## Results

### Switching synonymous serine codons in sinR affects biofilm formation

In a genetic screen to identify suppressor mutations that rescued the biofilm-defective phenotype of a B. subtilis mutant (‘Materials and methods’), we unexpectedly recovered a variant that contained a ‘silent’ mutation that resulted in a switch from one serine codon to a synonymous codon in sinR. This observation prompted us to ask whether switching other serine codons might also influence biofilm formation. Serine is specified by six codons: AGC, AGT, TCA, TCC, TCG and TCT (where T is U in the mRNA). We noticed that the sinR coding sequence has a slightly higher frequency of the four TCN serine codons as compared to the average frequency of TCN codons in the B. subtilis genome (Figure 1B, p=0.22, N = 12). To test whether this bias towards TCN codons has an effect on biofilm formation, we systematically replaced the three TCA codons in sinR (Figure 1—figure supplement 1) with each of the other five serine codons. Replacing the TCA codons with AGT or AGC resulted in flat, featureless colonies on solid biofilm-inducing medium, indicating severely impaired biofilm formation (Figure 1C). In contrast, replacing the TCA codons with either TCC or TCT had little or no effect on colony morphology whereas switching to TCG increased the wrinkled appearance of the colonies (Figure 1C), which is indicative of robust biofilm formation.

Next, we asked whether switching serine codons was altering the level of SinR protein in liquid biofilm-inducing medium. Immunoblot analysis with anti-SinR antibodies revealed slightly yet consistently higher SinR levels in the strain with the AGT variant of sinR when compared to either the wild-type strain with three TCA codons or the TCG variant of sinR (Figure 1D,E).

SinR is highly similar (85% identity) to SlrR, which also plays a critical role in biofilm formation and whose gene (slrR) is under the direct negative control of SinR (Chu et al., 2008). Because SlrR cross reacts with the anti-SinR antibodies, we were also able to detect SlrR in our immunoblot analysis. Strikingly, the levels of SlrR were almost perfectly anti-correlated with those of SinR, with the differences in the SlrR protein levels among the sinR synonymous variants being much higher than the corresponding differences in SinR protein levels (Figure 1F). Because repression by SinR is ultrasensitive to SinR levels (Chai et al., 2011), small differences in SinR protein levels among sinR synonymous variants might be sufficient to cause large differences in the levels of expression of SinR-repressed genes such as slrR. Consistent with this idea, an eps-lacZ transcriptional fusion reporter for the SinR-repressed epsA-O matrix operon showed that the four TCN sinR variants had 3- to 19-fold higher β-galactosidase activity than the AGT and AGC variants (Figure 1G).

To test the generality of the observed hierarchy between the synonymous variants of sinR, we generated an additional set of eleven sinR synonymous variants in which we replaced either three TCC codons or two AGC/AGT codons (Figure 1—figure supplement 1) with their synonymous counterparts. Eight of these variants conformed to the hierarchy described above, namely, the four TCN variants behaved oppositely to the two AGC/AGT variants in colony morphology and in eps-lacZ reporter expression (Figure 1—figure supplement 2). The three variants that did not conform to the hierarchy could potentially reflect alterations to the mRNA sequence context near the mutation rather than the effect of a synonymous substitution per se. Taken together, the above results suggest that serine synonymous codons in the sinR coding sequence have a stereotypical effect on biofilm formation that is primarily determined by the differential usage of the four TCN and the two AGC/AGT codons.

### Entry into biofilm formation is accompanied by codon-specific increase in ribosome density

What is the mechanism by which serine codon usage affects SinR protein levels and biofilm formation? Synonymous codon changes can alter the synthesis of the encoded protein through changes in the translation initiation rate, mRNA levels or the ribosome elongation rate (Plotkin and Kudla, 2010). However, the effect of synonymous codon usage on the initiation rate and mRNA levels is context-specific; only codons near the AUG start site affect translation initiation (Kudla et al., 2009), whereas only codons that are located in certain regions of secondary structure or at ribonuclease cleavage sites affect mRNA levels (Bernstein et al., 2002). Our observation that synonymous codon replacements at multiple locations along sinR have a stereotypical effect on biofilm formation argues against such context-specific mechanisms (except for the three exceptional cases noted above).

To test the alternative hypothesis that serine codon usage might alter the ribosome elongation rate, and given that the ribosome elongation rate at a codon varies inversely with the average ribosome density at that codon, we measured ribosome density on mRNAs at single-codon resolution using the ribosome profiling method (Ingolia et al., 2009; Oh et al., 2011; Ingolia et al., 2012). We grew B. subtilis in liquid biofilm-inducing medium, harvested cells either during exponential phase growth (OD600 = 0.6) or during stationary phase when biofilm formation is induced (OD600 = 1.4), and performed deep-sequencing of ribosome protected mRNA fragments and size-matched total mRNA fragments. Ribosome profiling yielded 3.75 and 2.55 million sequencing reads aligning to annotated protein-coding sequences for the exponential phase sample and the biofilm entry sample, respectively. The number of reads aligning to a single codon on individual mRNAs was too low for accurate quantification of ribosome density, and was not sufficient to directly detect increased ribosome density on the sinR transcript. However, we reasoned that the global pattern of ribosome density at codons across all mRNAs should reflect the ribosome density on individual transcripts such as sinR. Therefore, we calculated the median ribosome density at each of the 61 sense codons across the 1556 protein-coding sequences in the exponential phase sample and the 1148 sequences in the biofilm entry sample that had an average coverage greater than one sequencing read per codon (Figure 2—figure supplement 1, ‘Materials and methods’). This analysis reproduced the previous observation (Li et al., 2012) of increased ribosome density 8 to 11 nt downstream of Shine-Dalgarno-like trinucleotide sequences both during exponential phase and during biofilm entry (Figure 2—figure supplement 2).

During exponential phase, median ribosome density varied over a twofold range, with no systematic difference between serine codons and the remaining codons (Figure 2A). By contrast, during biofilm entry, median ribosome density was significantly higher at serine and cysteine codons as compared to the remaining codons (Figure 2B), suggesting that the translation speed of ribosomes is selectively reduced at these codons during biofilm entry. Notably, the ribosome density at serine codons was not uniform: the four UCN codons had 1.9 to 2.1-fold higher ribosome density whereas the AGC and AGU codons had only 1.1 and 1.3-fold higher ribosome density respectively, relative to the median value across 61 sense codons. Further, this difference in ribosome density between UCN codons and the AGC/AGU codons was essentially identical when computed separately for codons located in the first half or in the second half of each gene (Figure 2—figure supplement 3), a finding that underscores the statistical robustness and the context independence of the observed difference.

![Figure 2.](https://cdn.elifesciences.org/articles/01501/elife-01501-fig2-v1.jpg)

**Figure 2.:** Genome-wide median ribosome density and total mRNA density at 61 sense codons (excluding start and stop codons) (A) during exponential phase growth (OD600 = 0.6), and (B) during stationary phase when biofilm formation is induced (OD600 = 1.4). The six serine (red) and two cysteine (green) codons are highlighted. Genome-wide ribosome density and total mRNA density were measured by deep-sequencing of ribosome-protected mRNA fragments and total mRNA fragments respectively, of a B. subtilis 3610 derivative (ΔepsH) grown in liquid biofilm-inducing medium.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/01501/elife-01501-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** All steps outlined here were performed in Bash and Python programming languages. For further details on individual steps, see ‘Materials and methods’.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/01501/elife-01501-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** Median ribosome density across all protein coding sequences was computed for the 60 nt region around each of six Shine-Dalgarno-like trinucleotide sequences (Li et al., 2012) for the exponential phase sample (left-hand panel) and the biofilm entry sample (right-hand panel).

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/01501/elife-01501-fig2-figsupp3-v1.jpg)

**Figure 2—figure supplement 3.:** Each gene was conceptually divided into two equal halves and the ribosome density and mRNA density was computed separately for codons located either in the first half (left-hand panel) or in the second half (right-hand panel) of each gene. All other analysis steps were identical to those in Figure 2.

### Serine starvation reduces translation speed and inhibits SinR synthesis in a codon-specific manner

Because ribosomes density increased at serine and cysteine codons only during biofilm formation and not during exponential phase growth, we hypothesized that the increased ribosome density was caused by the depletion of intracellular pools of these two amino acids during biofilm entry rather than by any intrinsic feature of the mRNA (Li et al., 2012) or the nascent polypeptide (Charneski and Hurst, 2013). Our hypothesis is also supported by the previous observation that synonymous codon usage can have a starvation-specific effect on protein levels (Subramaniam et al., 2013). Further, serine is a precursor metabolite for the biosynthesis of cysteine (Gagnon et al., 1994); hence cysteine depletion was likely the result of a decrease in intracellular serine concentration. Consistent with this hypothesis, we also observed an increase in ribosome density at both serine and cysteine codons during serine starvation of a B. subtilis serine-auxotrophic mutant (Figure 3C). Importantly, serine starvation resulted in an increase in ribosome density at only the four UCN serine codons but not at the AGC and AGU codons, matching the hierarchy seen during biofilm entry (Figure 2B). Serine starvation also resulted in differential levels of production of SinR-YFP protein fusions bearing different synonymous serine codons, whereas serine-rich growth resulted in identical levels of fusion protein production from these variants (Figure 3A,B). Finally, the addition of excess serine or cysteine (but not any of the other 18 amino acids) blocked biofilm formation in wild type cells as judged after 48 hr of growth in biofilm-inducing medium (Figure 3—figure supplement 1, and data not shown).

![Figure 3.](https://cdn.elifesciences.org/articles/01501/elife-01501-fig3-v1.jpg)

**Figure 3.:** (A and B) Three sinR synonymous variants were synthesized with 10 serine codons switched to AGC, TCA or TCG. The variants were expressed as SinR-YFP fusions from the amyE locus under the control of a lac promoter in a 3610-ΔserA serine auxotroph strain growing in serine-limited medium. Black arrow around 300 min indicates the onset of serine starvation caused by depletion of exogenously-added serine in the growth medium. Cell density (A) and the corresponding SinR-YFP protein level (B) were monitored using a 96-well spectrophotometer. (C) Genome-wide median ribosome density for 61 sense codons (excluding start and stop codons) during serine starvation (vertical axis) and serine-rich growth (horizontal axis) of a serine auxotrophic strain. (D) Fold-change in average ribosome density for individual genes upon biofilm entry (vertical axis) or serine starvation (horizontal axis). Genes that were preferentially up-regulated at least 10-fold upon biofilm entry in comparison to serine starvation are highlighted in red (68 genes, Table 1). Only genes with a minimum of 100 ribosome profiling reads in at least one of the samples were included in this analysis (1724 genes) and the reported log2 fold-changes are median-subtracted values across this gene set.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/01501/elife-01501-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** Single amino acids were added at 300 µg ml−1 to liquid MSgg medium. Biofilm formation of 3610 was assayed visually by pellicle formation at the air-liquid interface 48 hr after inoculation. Serine and cysteine were found to block pellicle formation out of all 20 amino acids tested.

Given that both biofilm entry and serine starvation resulted in increased ribosome density at serine and cysteine codons, we asked whether these two apparently different conditions invoke the same gene expression program in B. subtilis. The fold-change in average ribosome density of B. subtilis genes was positively correlated between biofilm entry and serine starvation (Figure 3D, R2 = 0.27, p=10−5, 1724 genes). However, a subset of 68 genes was induced at least 10-fold higher upon biofilm entry than during serine starvation (indicated by red markers in Figure 3D, Table 1). This subset included genes for anaerobic metabolism such as lctEP, nasDE, and cydAB, and is consistent with the recently proposed role of impaired respiration in biofilm formation (Kolodkin-Gal et al., 2013). We observed that sulfur metabolism genes were also enriched in this subset, possibly indicating a stronger response to cysteine depletion during biofilm entry than during serine starvation.

**Table 1.**
 B. subtilis genes that have greater than 10-fold difference in expression ratio between biofilm formation and serine starvation


<table>
  <thead>
    <tr>
      <th>Gene</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
      <th>F</th>
      <th>Function</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>albA</td>
      <td>9.35</td>
      <td>−0.69</td>
      <td>32</td>
      <td>10129</td>
      <td>175</td>
      <td>144</td>
      <td>antilisterial bacteriocin (subtilosin) production protein</td>
    </tr>
    <tr>
      <td>alsD</td>
      <td>6.38</td>
      <td>0.95</td>
      <td>34</td>
      <td>1384</td>
      <td>53</td>
      <td>135</td>
      <td>alpha-acetolactate decarboxylase</td>
    </tr>
    <tr>
      <td>alsS</td>
      <td>6.96</td>
      <td>1.79</td>
      <td>76</td>
      <td>4613</td>
      <td>86</td>
      <td>396</td>
      <td>acetolactate synthase</td>
    </tr>
    <tr>
      <td>cah</td>
      <td>2.08</td>
      <td>−2.74</td>
      <td>2531</td>
      <td>5254</td>
      <td>1486</td>
      <td>295</td>
      <td>S-deacylase</td>
    </tr>
    <tr>
      <td>ctc</td>
      <td>3.78</td>
      <td>−0.73</td>
      <td>327</td>
      <td>2206</td>
      <td>322</td>
      <td>257</td>
      <td>50S ribosomal protein L25</td>
    </tr>
    <tr>
      <td>cydA</td>
      <td>5.36</td>
      <td>−3.18</td>
      <td>234</td>
      <td>4720</td>
      <td>408</td>
      <td>60</td>
      <td>cytochrome bd ubiquinol oxidase subunit I</td>
    </tr>
    <tr>
      <td>cydB</td>
      <td>9.6</td>
      <td>−1.88</td>
      <td>9</td>
      <td>3374</td>
      <td>129</td>
      <td>46</td>
      <td>cytochrome bd ubiquinol oxidase subunit II</td>
    </tr>
    <tr>
      <td>cysK</td>
      <td>1.52</td>
      <td>−2.21</td>
      <td>15760</td>
      <td>22120</td>
      <td>8991</td>
      <td>2580</td>
      <td>cysteine synthase</td>
    </tr>
    <tr>
      <td>gcvPA</td>
      <td>0.97</td>
      <td>−2.38</td>
      <td>1500</td>
      <td>1440</td>
      <td>1001</td>
      <td>255</td>
      <td>glycine dehydrogenase subunit 1</td>
    </tr>
    <tr>
      <td>gcvPB</td>
      <td>1.05</td>
      <td>−2.28</td>
      <td>2029</td>
      <td>2057</td>
      <td>1224</td>
      <td>335</td>
      <td>glycine dehydrogenase subunit 2</td>
    </tr>
    <tr>
      <td>gspA</td>
      <td>4.54</td>
      <td>−0.75</td>
      <td>111</td>
      <td>1261</td>
      <td>135</td>
      <td>106</td>
      <td>glycosyl transferase (general stress protein)</td>
    </tr>
    <tr>
      <td>iseA</td>
      <td>2.24</td>
      <td>−1.14</td>
      <td>1117</td>
      <td>2579</td>
      <td>2521</td>
      <td>1516</td>
      <td>inhibitor of cell-separation enzymes</td>
    </tr>
    <tr>
      <td>lctP</td>
      <td>6.62</td>
      <td>−2.9</td>
      <td>62</td>
      <td>3009</td>
      <td>247</td>
      <td>44</td>
      <td>L-lactate permease</td>
    </tr>
    <tr>
      <td>ldh</td>
      <td>3.47</td>
      <td>−3.88</td>
      <td>2810</td>
      <td>15,254</td>
      <td>1732</td>
      <td>157</td>
      <td>L-lactate dehydrogenase</td>
    </tr>
    <tr>
      <td>maeN</td>
      <td>4.08</td>
      <td>−1.61</td>
      <td>148</td>
      <td>1226</td>
      <td>347</td>
      <td>151</td>
      <td>Na+/malate symporter</td>
    </tr>
    <tr>
      <td>mccA</td>
      <td>3.23</td>
      <td>−2.72</td>
      <td>759</td>
      <td>3494</td>
      <td>386</td>
      <td>78</td>
      <td>cystathionine beta-synthase</td>
    </tr>
    <tr>
      <td>metE</td>
      <td>2.72</td>
      <td>−2.13</td>
      <td>33,027</td>
      <td>106473</td>
      <td>32,231</td>
      <td>9760</td>
      <td>5-methyltetrahydropteroyltriglutamate/homocysteine S-methyltransferase</td>
    </tr>
    <tr>
      <td>mgsR</td>
      <td>4.72</td>
      <td>−1.53</td>
      <td>163</td>
      <td>2099</td>
      <td>202</td>
      <td>93</td>
      <td>stress transcriptional regulator</td>
    </tr>
    <tr>
      <td>mtlA</td>
      <td>3.92</td>
      <td>−0.22</td>
      <td>126</td>
      <td>934</td>
      <td>104</td>
      <td>119</td>
      <td>PTS system mannitol-specific transporter subunit IICB</td>
    </tr>
    <tr>
      <td>mtnA</td>
      <td>1.84</td>
      <td>−2.79</td>
      <td>2522</td>
      <td>4425</td>
      <td>3501</td>
      <td>671</td>
      <td>methylthioribose-1-phosphate isomerase</td>
    </tr>
    <tr>
      <td>mtnD</td>
      <td>1.72</td>
      <td>−1.63</td>
      <td>4095</td>
      <td>6600</td>
      <td>3182</td>
      <td>1361</td>
      <td>acireductone dioxygenase</td>
    </tr>
    <tr>
      <td>mtnK</td>
      <td>2.54</td>
      <td>−2.64</td>
      <td>4290</td>
      <td>12,196</td>
      <td>5866</td>
      <td>1250</td>
      <td>methylthioribose kinase</td>
    </tr>
    <tr>
      <td>nasD</td>
      <td>6.21</td>
      <td>−0.65</td>
      <td>217</td>
      <td>7872</td>
      <td>635</td>
      <td>536</td>
      <td>assimilatory nitrite reductase subunit</td>
    </tr>
    <tr>
      <td>nasE</td>
      <td>6.05</td>
      <td>0.38</td>
      <td>34</td>
      <td>1106</td>
      <td>63</td>
      <td>109</td>
      <td>assimilatory nitrite reductase subunit</td>
    </tr>
    <tr>
      <td>rbfK</td>
      <td>3.74</td>
      <td>−2.57</td>
      <td>1329</td>
      <td>8681</td>
      <td>434</td>
      <td>97</td>
      <td>RNA-binding riboflavin kinase</td>
    </tr>
    <tr>
      <td>sboA</td>
      <td>7.77</td>
      <td>0.64</td>
      <td>121</td>
      <td>12,895</td>
      <td>256</td>
      <td>530</td>
      <td>subtilosin A</td>
    </tr>
    <tr>
      <td>sboX</td>
      <td>8.26</td>
      <td>0.19</td>
      <td>21</td>
      <td>3128</td>
      <td>76</td>
      <td>115</td>
      <td>bacteriocin-like product</td>
    </tr>
    <tr>
      <td>ssuA</td>
      <td>2.09</td>
      <td>−2.3</td>
      <td>3691</td>
      <td>7682</td>
      <td>877</td>
      <td>236</td>
      <td>aliphatic sulfonate ABC transporter binding lipoprotein</td>
    </tr>
    <tr>
      <td>ssuB</td>
      <td>2.57</td>
      <td>−2.09</td>
      <td>2416</td>
      <td>7004</td>
      <td>779</td>
      <td>242</td>
      <td>aliphatic sulfonate ABC transporter ATP-binding protein</td>
    </tr>
    <tr>
      <td>ssuC</td>
      <td>2.17</td>
      <td>−2.16</td>
      <td>3784</td>
      <td>8362</td>
      <td>692</td>
      <td>206</td>
      <td>aliphatic sulfonate ABC transporter permease</td>
    </tr>
    <tr>
      <td>ssuD</td>
      <td>2.2</td>
      <td>−2.19</td>
      <td>12,961</td>
      <td>29,135</td>
      <td>2812</td>
      <td>817</td>
      <td>alkanesulfonate monooxygenase</td>
    </tr>
    <tr>
      <td>tcyJ</td>
      <td>3.25</td>
      <td>−3.26</td>
      <td>1046</td>
      <td>4856</td>
      <td>427</td>
      <td>59</td>
      <td>sulfur-containing amino acid ABC transporter binding lipoprotein</td>
    </tr>
    <tr>
      <td>tcyK</td>
      <td>3.79</td>
      <td>−3.55</td>
      <td>2815</td>
      <td>19,087</td>
      <td>1095</td>
      <td>124</td>
      <td>sulfur-containing amino acid ABC transporter binding lipoprotein</td>
    </tr>
    <tr>
      <td>tcyL</td>
      <td>3.33</td>
      <td>−3.05</td>
      <td>855</td>
      <td>4223</td>
      <td>387</td>
      <td>62</td>
      <td>sulfur-containing amino acid ABC transporter permease</td>
    </tr>
    <tr>
      <td>tcyM</td>
      <td>3.54</td>
      <td>−2.97</td>
      <td>1859</td>
      <td>10,556</td>
      <td>581</td>
      <td>99</td>
      <td>sulfur-containing amino acid ABC transporter permease</td>
    </tr>
    <tr>
      <td>tcyN</td>
      <td>3.38</td>
      <td>−2.74</td>
      <td>3363</td>
      <td>17,149</td>
      <td>1119</td>
      <td>223</td>
      <td>sulfur-containing amino acid ABC transporter ATP-binding protein</td>
    </tr>
    <tr>
      <td>ureA</td>
      <td>4.36</td>
      <td>0.78</td>
      <td>124</td>
      <td>1252</td>
      <td>77</td>
      <td>176</td>
      <td>urease subunit gamma</td>
    </tr>
    <tr>
      <td>ycgL</td>
      <td>0.99</td>
      <td>−3.01</td>
      <td>512</td>
      <td>500</td>
      <td>278</td>
      <td>46</td>
      <td>hypothetical protein</td>
    </tr>
    <tr>
      <td>ycgM</td>
      <td>2.46</td>
      <td>−1.35</td>
      <td>39</td>
      <td>105</td>
      <td>178</td>
      <td>93</td>
      <td>proline oxidase</td>
    </tr>
    <tr>
      <td>ycgN</td>
      <td>2.45</td>
      <td>−1.6</td>
      <td>928</td>
      <td>2475</td>
      <td>1267</td>
      <td>556</td>
      <td>1-pyrroline-5-carboxylate dehydrogenase</td>
    </tr>
    <tr>
      <td>ycnJ</td>
      <td>0.75</td>
      <td>−2.63</td>
      <td>168</td>
      <td>138</td>
      <td>121</td>
      <td>26</td>
      <td>copper import protein</td>
    </tr>
    <tr>
      <td>ydaG</td>
      <td>4.14</td>
      <td>0.49</td>
      <td>70</td>
      <td>604</td>
      <td>80</td>
      <td>150</td>
      <td>general stress protein</td>
    </tr>
    <tr>
      <td>ydbL</td>
      <td>3.07</td>
      <td>−0.31</td>
      <td>294</td>
      <td>1210</td>
      <td>130</td>
      <td>139</td>
      <td>hypothetical protein</td>
    </tr>
    <tr>
      <td>yeaA</td>
      <td>1.34</td>
      <td>−2.59</td>
      <td>112</td>
      <td>138</td>
      <td>139</td>
      <td>31</td>
      <td>hypothetical protein</td>
    </tr>
    <tr>
      <td>yezD</td>
      <td>2.52</td>
      <td>−4.17</td>
      <td>145</td>
      <td>406</td>
      <td>340</td>
      <td>25</td>
      <td>hypothetical protein</td>
    </tr>
    <tr>
      <td>yitJ</td>
      <td>3.01</td>
      <td>−2.43</td>
      <td>2785</td>
      <td>10,990</td>
      <td>4687</td>
      <td>1153</td>
      <td>bifunctional homocysteine S-methyltransferase/5,10-methylenetetrahydrofolate reductase</td>
    </tr>
    <tr>
      <td>yjbC</td>
      <td>3.67</td>
      <td>−0.57</td>
      <td>104</td>
      <td>647</td>
      <td>248</td>
      <td>222</td>
      <td>thiol oxidation management factor; acetyltransferase</td>
    </tr>
    <tr>
      <td>yjnA</td>
      <td>1.5</td>
      <td>−2.81</td>
      <td>972</td>
      <td>1342</td>
      <td>790</td>
      <td>149</td>
      <td>hypothetical protein</td>
    </tr>
    <tr>
      <td>yoaB</td>
      <td>2.28</td>
      <td>−2.26</td>
      <td>2206</td>
      <td>5244</td>
      <td>2862</td>
      <td>792</td>
      <td>negatively charged metabolite transporter</td>
    </tr>
    <tr>
      <td>yoaC</td>
      <td>2.92</td>
      <td>−1.89</td>
      <td>1200</td>
      <td>4459</td>
      <td>1436</td>
      <td>513</td>
      <td>hydroxylated metabolite kinase</td>
    </tr>
    <tr>
      <td>yrhB</td>
      <td>2.92</td>
      <td>−2.93</td>
      <td>3806</td>
      <td>14,096</td>
      <td>1904</td>
      <td>333</td>
      <td>cystathionine beta-lyase</td>
    </tr>
    <tr>
      <td>yrrT</td>
      <td>2.97</td>
      <td>−3.12</td>
      <td>546</td>
      <td>2089</td>
      <td>443</td>
      <td>68</td>
      <td>AdoMet-dependent methyltransferase</td>
    </tr>
    <tr>
      <td>ytlI</td>
      <td>1.66</td>
      <td>−3.2</td>
      <td>206</td>
      <td>318</td>
      <td>141</td>
      <td>20</td>
      <td>LysR family transcriptional regulator</td>
    </tr>
    <tr>
      <td>ytmI</td>
      <td>3.34</td>
      <td>−3.27</td>
      <td>3452</td>
      <td>17,173</td>
      <td>1640</td>
      <td>226</td>
      <td>N-acetyltransferase</td>
    </tr>
    <tr>
      <td>ytmO</td>
      <td>3.4</td>
      <td>−2.88</td>
      <td>3866</td>
      <td>20,007</td>
      <td>1179</td>
      <td>213</td>
      <td>monooxygenase</td>
    </tr>
    <tr>
      <td>ytnI</td>
      <td>3</td>
      <td>−2.6</td>
      <td>3522</td>
      <td>13,770</td>
      <td>867</td>
      <td>189</td>
      <td>redoxin</td>
    </tr>
    <tr>
      <td>ytnJ</td>
      <td>3.14</td>
      <td>−2.86</td>
      <td>10,645</td>
      <td>45,997</td>
      <td>2495</td>
      <td>456</td>
      <td>monooxygenase</td>
    </tr>
    <tr>
      <td>ytnL</td>
      <td>3.56</td>
      <td>−2.45</td>
      <td>1281</td>
      <td>7371</td>
      <td>354</td>
      <td>86</td>
      <td>aminohydrolase</td>
    </tr>
    <tr>
      <td>ytnM</td>
      <td>3.5</td>
      <td>−2.6</td>
      <td>4542</td>
      <td>25,202</td>
      <td>1264</td>
      <td>277</td>
      <td>transporter</td>
    </tr>
    <tr>
      <td>yuaF</td>
      <td>1.89</td>
      <td>−1.74</td>
      <td>87</td>
      <td>157</td>
      <td>158</td>
      <td>63</td>
      <td>membrane integrity integral inner membrane protein</td>
    </tr>
    <tr>
      <td>yvzB</td>
      <td>0.95</td>
      <td>−2.48</td>
      <td>125</td>
      <td>118</td>
      <td>168</td>
      <td>40</td>
      <td>flagellin</td>
    </tr>
    <tr>
      <td>yxaL</td>
      <td>3.54</td>
      <td>−0.41</td>
      <td>1069</td>
      <td>6077</td>
      <td>442</td>
      <td>442</td>
      <td>membrane associated protein kinase</td>
    </tr>
    <tr>
      <td>yxbB</td>
      <td>3.7</td>
      <td>−0.01</td>
      <td>108</td>
      <td>685</td>
      <td>118</td>
      <td>155</td>
      <td>S-adenosylmethionine-dependent methyltransferase</td>
    </tr>
    <tr>
      <td>yxeK</td>
      <td>0.86</td>
      <td>−2.72</td>
      <td>2702</td>
      <td>2406</td>
      <td>1073</td>
      <td>216</td>
      <td>monooxygenase</td>
    </tr>
    <tr>
      <td>yxeL</td>
      <td>1.29</td>
      <td>−2.94</td>
      <td>437</td>
      <td>525</td>
      <td>202</td>
      <td>35</td>
      <td>acetyltransferase</td>
    </tr>
    <tr>
      <td>yxeM</td>
      <td>0.87</td>
      <td>−2.57</td>
      <td>3003</td>
      <td>2692</td>
      <td>1047</td>
      <td>233</td>
      <td>ABC transporter binding lipoprotein</td>
    </tr>
    <tr>
      <td>yxeP</td>
      <td>1.75</td>
      <td>−2.24</td>
      <td>2577</td>
      <td>4246</td>
      <td>736</td>
      <td>207</td>
      <td>amidohydrolase</td>
    </tr>
    <tr>
      <td>yxjH</td>
      <td>2.02</td>
      <td>−1.82</td>
      <td>4162</td>
      <td>8243</td>
      <td>3811</td>
      <td>1432</td>
      <td>methyl-tetrahydrofolate methyltransferase</td>
    </tr>
  </tbody>
</table>

_A—median-subtracted log2 fold-change: biofilm/exponential-phase, B—median-subtracted log2 fold-change: serine starvation/serine rich, C—raw counts: biofilm entry, D—raw counts: exponential phase, E—raw counts: serine rich, F—raw counts: serine starvation._

In toto, the results with the serine auxotroph support the inference that ribosome stalling observed during biofilm formation is due to a drop in intracellular serine levels. Our efforts to measure intracellular serine levels directly during growth in minimal, biofilm-inducing medium (MSgg) have been unsuccessful. Hence, we cannot rule out the less likely possibilities that biofilm entry causes serine and cysteine to be sequestered away from protein synthesis or that aminoacylation rate of the corresponding tRNAs decreases without changes in the intracellular serine and cysteine pools.

### Serine codon bias in biofilm-regulated genes reflects their expression during serine starvation

Here we found that the translation speed of ribosomes decreases at UCN serine codons and thereby modulates production of SinR and entry into biofilm formation. Based on our genome-wide measurements of ribosome density, we expect that the translation speed of ribosomes should decrease during biofilm entry not only on the sinR mRNA, but also on other mRNAs that are enriched for any of the four UCN codons. For example, we found that the four TCN codons are over-represented in two nucleotide biosynthesis genes, pyrAA and purB (Figure 4A). These two genes are also transcriptionally down regulated during biofilm entry (Figure 4B). A high frequency of TCN codons in these genes might serve to reinforce their transcriptional down regulation by reducing translation speed. Conversely, TCN codons are under-represented in the genes encoding lactate dehydrogenase, ldh (Cruz Ramos et al., 2000) and a master regulator of post-exponential phase gene expression, spo0A (Molle et al., 2003) (Figure 4A). The two genes are transcriptionally up regulated upon biofilm entry (Figure 4B). The low frequency of TCN codons in these genes might represent a mechanism for optimizing the production of their protein products by minimizing the slowing down of translation during biofilm entry. Consistent with this idea, replacement of AGC/AGT codons by TCN codons in spo0A, whose protein product positively regulates biofilm entry (by turning on the synthesis of the SinR antagonist SinI), resulted in defective biofilm formation (Figure 4C) in contrast to the stimulatory effect of replacing AGC/AGT codons with TCN codons in sinR (Figure 1—figure supplement 2).

![Figure 4.](https://cdn.elifesciences.org/articles/01501/elife-01501-fig4-v1.jpg)

**Figure 4.:** (A) Relative serine codon fraction in genes for nucleotide biosynthesis (pyrAA, purB), lactate dehydrogenase (ldh) and a sporulation regulator (spo0A). Numbers in parentheses indicate the number of serine codons in each gene. Relative fraction of serine codons across the B. subtilis genome is shown for comparison. (B) Fold-change (expressed in log2 units) in average ribosome density upon biofilm entry for the four genes shown in A. (C) Colony morphology of a wild-type strain and two spo0A synonymous variants grown on solid biofilm-inducing medium. Seven AGC/AGT codons in wild-type spo0A were replaced by either 7 TCC codons or 3 TCC and 4 TCG codons and inserted at the chromosomal spo0A locus. Both the wild-type spo0A and the synonymous spo0A variants were inserted with a downstream selection marker. (D) Left: Codon Adaptation Index (CAI) for the four genes shown in A. Right: Distribution of CAI values for 4153 protein-coding sequences of B. subtilis.

## Discussion

Together, our results implicate serine depletion as an environmental cue that contributes to promoting biofilm formation in B. subtilis together with other cues that are sensed by the histidine kinases KinA–D. Serine depletion is sensed through a remarkably simple mechanism based on reduced translation speed at UCN serine codons in the mRNA for a regulatory protein, SinR, whose repressive effects are highly sensitive to small changes in the level of the protein. We presume that UCN codons lower SinR levels simply by slowing the rate of ribosome movement along the mRNA (elongation). However, it is possible that the reduced translation speed at UCN codons during biofilm entry could be followed by downstream events such as ribosome rescue (Keiler et al., 1996) or mRNA decay (Hayes and Sauer, 2003) that might also contribute to lowering the levels of the SinR protein.

The serine sensing mechanism uncovered here operates through over-representation of the TCN serine codons in the sinR gene without the necessity for any other dedicated protein or RNA for sensing serine depletion. By contrast, transcriptional attenuation, a widespread mechanism among bacteria for sensing amino acids that also relies on changes in translation speed, involves a translation-transcription coupling mechanism that is mediated by highly structured mRNAs and leader peptides (Henkin and Yanofsky, 2002).

We note that the biased usage of the four TCN serine codons, which act as starvation sensors during biofilm formation, is not evident from widely-used phenomenological measures of codon bias such as the codon adaptation index (Figure 4D), which primarily reflects codon preferences during exponential growth (Sharp and Li, 1987; Andersson and Kurland, 1990). The difference in translation speed between the four UCN codons and the two AGC/AGU codons under biofilm-inducing conditions is likely mediated by differences in concentration of the corresponding aminoacylated tRNAs (Elf et al., 2003; Dittmar et al., 2005), as was recently observed in serine-starved E. coli (Subramaniam et al., 2013). Interestingly, the hierarchy between UCN codons and AGC/AGU codons in B. subtilis during serine starvation is similar to the one in E. coli even though copy numbers of the corresponding tRNA genes have diverged significantly between these two organisms (Lowe and Eddy, 1997). Despite different tRNA gene copy numbers, it is possible that the relative abundances of the serine tRNA isoacceptors are similar between the two organisms or that their relative abundances might be regulated in the same manner in response to nutrient deprivation (Doi et al., 1966).

Serine is one of the first amino acids to be completely consumed from the culture medium when either B. subtilis or E. coli cells are grown in complex rich medium (Liebs et al., 1988; Prüss et al., 1994; Sezanov et al., 2007). Indeed, increased ribosome density has been observed at serine codons during growth of E. coli in Luria-Bertani broth (Li et al., 2012). Thus the role of synonymous serine codons as starvation sensors discovered here in the specific context of biofilm formation might be a general regulatory strategy in microbes for adapting to nutrient depletion at the end of exponential phase growth. It is noteworthy that depletion of specific amino acids affects developmental transitions in several eukaryotic cells (Marin, 1976; Sundrud et al., 2009; Wang et al., 2009). It will be interesting to test whether a codon-based sensing mechanism, similar to the one found here in bacterial biofilm development, also plays a role in eukaryotic cells during amino acid depletion.

## Materials and methods

### Bacterial strains and media

For ribosome profiling during biofilm formation, a 3610-ΔepsH strain (RL3852) was used to ensure dispersed growth in liquid media (Kearns et al., 2005). For serine starvation experiments, a serine-auxotrophic 3610-ΔserA strain (YC865) was used. A list of strains, plasmids, and oligonucleotides used in this work are summarized in Supplementary file 1.

For general purposes, B. subtilis strains PY79, 3610, and their derivatives were grown in Luria-Bertani (LB) medium (10 g tryptone, 5 g yeast extract, and 5 g NaCl per liter broth) at 37°C. Antibiotics were added to the media at the following concentrations for B. subtilis strains: 10 µg ml−1 of tetracycline, 100 µg ml−1 of spectinomycin, 10 µg ml−1 of kanamycin, 5 µg ml−1 of chloramphenicol, and 1 µg ml−1 of erythromycin. Minimal MSgg medium was used as the liquid biofilm-inducing medium. The same medium with 1.5% Bacto-agar (Difco, Franklin Lakes, NJ) was used as the solid biofilm-inducing medium. MSgg medium composition: 5 mM potassium phosphate (pH 7), 100 mM MOPS (pH 7), 2 mM MgCl2, 700 µM CaCl2, 50 µM MnCl2, 50 µM FeCl3, 1 µM ZnCl2, 2 µM thiamine, 0.5% glycerol, 0.5% glutamate, 50 µg ml−1 tryptophan, 50 µg ml−1 phenylalanine and 50 µg ml−1 threonine. For overnight growth of serine auxotrophic 3610 strains, MSgg medium was supplemented with serine to a final concentration of 5 mM. For serine starvation experiments in which YFP fluorescence was measured (Figure 3A,B), MSgg medium was supplemented with 800 µM serine and 400 µM serine methyl-ester (Sigma, St. Louis, MO). Serine methyl-ester was added to ensure slow growth under serine starvation conditions.

### Strain construction

General methods for molecular cloning followed published protocols (Sambrook 2001). SPP1 phage-mediated transduction was used to transfer antibiotic-marked DNA fragments between different strains (Kearns et al., 2005). Long-flanking PCR mutagenesis was applied to generate insertional deletion mutations (Wach 1996). Synonymous switches in sinR and spo0A were generated by using synthetic DNA fragments (Genewiz, South Plainfield, NJ) or by applying site-directed mutagenesis (Roche, Switzerland). Sequences of the primers used in constructing mutant sinR alleles are described in Supplementary file 1. Incorporation of synonymous substitutions into the sinR or spo0A gene at the native locus was done by allele exchange and followed a method described previously (Chai et al., 2011).

### Biofilm assays

B. subtilis cells were first grown in LB broth at 37°C to mid-exponential phase. For formation of biofilm colonies, 2 µl of the cells was spotted onto MSgg medium solidified with 1.5% agar. Plates were incubated at 23°C for 3–4 days before analysis. All images were taken using either a Nikon CoolPix 950 digital camera or using a SPOT camera (Diagnostic Instruments, Sterling Heights, MI). Assays for the β-galactosidase activities were described previously (Kearns et al., 2005).

### Genetic screen for suppressor mutants

Following a previously-published protocol (Chai et al., 2010), we set up a genetic screen to search for spontaneous mutations that suppressed the defective biofilm phenotype of a B. subtilis ΔslrR mutant (YC131). The defective biofilm phenotype of the ΔslrR mutant is manifested as an inability to form robust floating pellicles (Chu et al., 2008; Chai et al., 2010). Briefly, the ΔslrR strain was inoculated into liquid MSgg medium in 6-well plates and incubated at 30°C. After 48 hr, pellicle formation was examined visually. In some wells, robust pellicles appeared possibly due to a second, suppressor mutation elsewhere in the genome. Cells from those wells were picked and streaked out on fresh LB agar plates to isolate single colonies. Cells from the single colonies were then tested for altered colony morphology on solid MSgg medium to confirm the suppressor phenotype. Similar genetic screens in previous studies (Kearns et al., 2005; Chai et al., 2010) had established that mutations in the sinR gene could suppress the defective biofilm phenotype of the ΔslrR mutant. Therefore, we isolated genomic DNA from the putative suppressor mutants, amplified the sinR gene by PCR, and then sequenced the sinR locus. Once a mutation in the sinR gene was confirmed by sequencing, the same mutation was reconstituted in the wild type background (3610) following a previous protocol (Chai et al., 2010), and assayed for alteration in colony morphology on solid MSgg medium.

### Bacterial growth for ribosome profiling

For ribosome profiling during biofilm formation, fresh colonies were inoculated into 8 ml of MSgg liquid medium and grown for 12 hr at 30°C, 200 rpm. Saturated cultures were diluted 1:1000 into 200 ml aliquots of fresh MSgg medium and shaken in a 1L flask at 30°C, 200 rpm. For exponential-phase ribosome profiling (Figure 2A), cultures were harvested at OD600 = 0.6. For ribosome profiling during biofilm entry (Figure 2B), cultures were harvested at OD600 = 1.4. For the serine repletion experiment (Figure 4), serine was added to a final concentration of 2.5 mM at OD600 = 1.4 and harvested after 30 min at 30°C, 200 rpm. For the serine starvation experiment (Figure 3B,C), pre-cultures were grown in MSgg medium supplemented with 5 mM serine and then diluted into 200 ml of the same medium. At an OD600 = 0.6, the cultures were filtered and re-suspended either in MSgg medium (starvation) or in MSgg medium with 5 mM serine (control), and harvested after 60 min at 30°C, 200 rpm (Figure 3D).

### Western blotting

Cultures were grown with shaking at 37°C, and 14 ml culture aliquots were harvested at an OD600 between 2.0 and 2.5. Cell pellets were collected by centrifugation and washed once with 10 ml of lysis buffer (20 mM Tris-HCl, 200 mM NaCl, 1 mM EDTA pH 7.4). Pellets were resuspended in 1.2 ml lysis buffer and incubated with 20 µg/ml of lysozyme (Sigma) for 1 hr on ice. Cells were further lysed by sonication. Cell debris was removed by centrifugation (14,000 rpm, 30 min, 4°C). The concentration of total protein in the lysates was determined by a Bradford assay (Bio-Rad, Hercules, CA). Samples for SDS-PAGE were prepared in Laemmli buffer normalized to equal protein concentration. Samples were ran on an NuPAGE 12% gel (Invitrogen, Carlsbad, CA, 1.0 mm, Bis/Tris, 200 V, ∼50 min) and transferred to a PVDF membrane (Millipore, Billerica, MA) at 100 V for 1 hr. The membrane was blocked in 5% milk-TPBS for 1 hr, and then incubated with anti-SinR antibody (1:2500, polyclonal) and anti-SigA (1:100,000, polyclonal) overnight. The membranes were washed 3 times in TPBS for 5 min each. Blots were incubated with goat anti-rabbit secondary antibody conjugated to Horseradish peroxidase (1:10,000, Bio-Rad). Blots were washed three times in TPBS, and developed with SuperSignal West Dura chemiluminescent substrate (Thermo, Waltham, MA) and imaged on a gel-doc (Bio-Rad). Densitometry analysis of Western blot images was performed using ImageJ software (NIH, http://rsbweb.nih.gov/ij/). Rectangles were drawn around each distinct band and the average pixel intensity in this rectangle was calculated, followed by subtraction of background pixel intensity from an identical rectangle drawn in a region without any band. These background subtracted values were used for calculating SinR/SigA, SlrR/SigA and SinR / SlrR ratios in Figure 1.

### YFP fluorescence measurements

A previously published measurement protocol was used (Subramaniam et al., 2013). Fresh colonies were inoculated into 1 ml of MSgg liquid medium with 5 mM serine and grown overnight in deep 96-well plates at 30°C, 1400 rpm. In the morning, saturated cultures were diluted 1:100 into 1 ml of MSgg medium with 800 µM serine and 400 µM serine methyl-ester and shaken at 30°C, 1350 rpm for 3 hr. Three aliquots of 150 µl from each culture was pipetted into three wells of three 96-well plates (3799, Costar, Corning, NY). Wallac Victor2 plate reader (PerkinElmer, Waltham, MA) was used to monitor cell density (absorbance at 600 nm) and YFP expression (fluorescence, excitation 504 nm and emission 540 nm). Each plate was read every 15 min using a robotic system (Caliper Life Sciences, Hopkinton, MA) and shaken at 1000 rpm in between readings (Variomag Teleshake shaker, Daytona Beach, FL). 30°C and 60% relative humidity was maintained throughout the experiment.

### Ribosome profiling and mRNA quantification

Ribosome profiling protocol was adapted from published literature (Ingolia et al., 2009; Oh et al., 2011; Ingolia et al., 2012) with minor modifications as described below. Briefly, 200 ml of bacterial culture was harvested by filtration. The filter was immediately inserted into a 50 ml conical tube, flash frozen in liquid nitrogen, and stored at −80°C until further processing. Frozen cells were re-suspended in 8 ml of polysome resuspension buffer (20 mM Tris pH 8.0, 10 mM MgCl2, 100 mM NH4Cl, and 100 µg ml−1 Chloramphenicol). Re-suspended cells were pelleted by centrifugation (3000 g, 4°C, 5 min) and the supernatant was discarded. The cell pellet was re-suspended in 500 µl of polysome lysis buffer (1X polysome resuspension buffer, 5 mM CaCl2, 0.4% TritonX-100, 0.1% NP-40, and 100 U/ml RNase-free DNase [04716728001; Roche]), and transferred to an ice-cold 1.5 ml tube containing 500 µl of 0.2–0.3 µm acid-washed glass beads (G1277; Sigma). Cells were lysed by vortexing at maximum speed on a vortexer in a 4°C room (Vortex Genie 2, 10 × 30 s with 1 min cooling on ice in between). The lysate was clarified by centrifugation (20,000 g, 4°C, 10 min) and the supernatant was transferred to a fresh 1.5 ml tube. 500 µg of total RNA (A260 units) was digested (25°C, 1400 rpm, 60 min, 150 µl vol) with 2 U/µg of Micrococcal nuclease (LS004797; Worthington, Lakewood, NJ). The digestion was quenched with 1.5 µl of 0.5 M EGTA, loaded on top of a 10–50% sucrose gradient and ultra-centrifuged in a SW41 rotor (35000 rpm, 4°C, 150 min). Monosomes collected by gradient fractionation (Biocomp Instruments, Canada).

For total RNA extraction, 100 µl of polysome lysate was mixed with 400 µl of RNA extraction buffer (0.3 M sodium acetate, 10 mM EDTA, pH 4.5) and the aqueous phase was extracted twice with phenol-chloroform and once with chloroform. RNA was precipitated with an equal volume of isopropanol. The pellet was washed with 70% ice-cold ethanol and re-suspended in 100 µl of 10 mM Tris pH 7.0. 10 µg of total RNA was DNase-treated and mRNA enriched using the Microbe Express kit (Invitrogen). mRNA was fragmented by heating at 95°C with a bicarbonate buffer (Ingolia et al., 2009) for 20 min.

Collected monosome fractions were purified using the same phenol-chloroform method as used for total RNA extraction above. Monosomes and fragmented mRNA were then used for small RNA sequencing library preparation. Size selection, dephosphorylation, polyadenylation, reverse-transcription, circularization and PCR amplification were performed using the same protocol as in (Ingolia et al., 2009). An rRNA subtraction step was carried out between the circularization and PCR amplification steps using the same protocol as in (Oh et al., 2011). Typically, several samples were multiplexed for sequencing in an Illumina HiSeq sequencer such that at least 1 million reads were obtained for each sample.

### Deep-sequencing data analysis

Deep-sequencing data analysis was carried out in Bash and Python programming languages, and performed on the Harvard research computing Odyssey cluster. Main steps are summarized below and shown schematically in Figure 2—figure supplement 1.Each 50 nt single-end read was polyA-trimmed by identifying 10 or greater number of adjacent adenines and discarding all nucleotides starting from −1nt of the polyA run. The first 5′ nt of the read was also discarded since its identity was ambiguous in several reads. PolyA-trimmed reads were first aligned against all non-coding RNAs in the B. subtilis genome using bowtie aligner (ver. 0.12.7, Langmead et al., 2009).The non-coding RNA sequences were downloaded from NCBI (NC_000964.frn).Reads that did not align to non-coding RNAs were aligned against the whole B. subtilis genome using bowtie aligner. The B. subtilis genome was downloaded from NCBI (NC_000964.fna). Only reads that had less than three mismatches with the reference genome were considered for further analysis.Reads that aligned to the B. subtilis genome were further trimmed by 8 nt from each end to approximate the ribosome A-site coordinate. The remaining sequence was normalized by its length and assigned to the corresponding genomic coordinate, and this value was designated as the read density at this genomic coordinate during further downstream analyses.Average ribosome and mRNA density for a single gene was calculated by summing the read density between the start and stop codon, and then normalizing by the length of the gene.Fold-change in ribosome density for a single gene between two samples was calculated by taking the log2 of the ratio of average ribosome density between the two samples for that gene. The median value of this log2 fold-change across all genes that received a minimum of 100 reads in at least one of the two samples was then subtracted from the fold-change value for each gene. This median-subtracted log2 fold change in reported throughout this work. We note that the average ribosome density on any gene is directly proportional to the corresponding mRNA level in the absence of specific translational regulation. Hence fold-changes in ribosome density (such as the one shown in Figure 3D) primarily reflect fold-changes in mRNA level.To calculate the ribosome and mRNA density at individual codons,The start codon was treated as a single separate codon irrespective of its identity.Only genes with average ribosome density of at least 1 read per codon were considered.The ribosome density at the first nucleotide of each codon was assigned as the ribosome density at that codon. For each of the 64 codons and the start codon, read density at the first nucleotide of the codon was averaged across all occurrences of that codon in a single gene and then normalized by the average ribosome density for that gene. Hence a codon without over- or under- representation of ribosome or mRNA density will have a density value equal to 1.Genome-wide ribosome and mRNA density was calculated as the median of the individual gene read density from Step (3) across all genes that pass the threshold of Step (2).Ribosome profiling measurement resulted in a high ribosome density at start and stop codons. It is unclear whether this increase is a true biological signal or caused by the measurement protocol (Ingolia et al., 2011). Hence these codons were excluded from the ribosome density plots shown in Figure 2A,B and 3C. However, the increased ribosome density at these codons resulted in a concomitant decrease in ribosome density at the remaining codons due to normalization by the average ribosome density for each gene (which included the start and stop codons).

### Codon usage analysis

Codon Adpatiaton Index (CAI) was calculated according to the original prescription of Sharp and Li (Sharp and Li, 1987). For this calculation, 68 genes that had an annotation as ‘ribosomal’ were used as the reference set of highly expressed genes. The annotations file used for this analysis was downloaded from NCBI (NC_000964.ptt). The p value for the higher frequency of TCN codons in sinR was calculated by assuming a binomial distribution of TCN and AGC/AGT codons. The p value represents the binomial probability that there are 10 or more TCN codons in the sinR gene (12 serine codons total) given the genome-wide frequency of serine codons (0.66 for TCN codons and 0.34 for AGC/AGT codons).
