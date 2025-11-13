# History-dependent physiological adaptation to lethal genetic modification under antibiotic exposure

## Authors

- Yuta Koganezawa<sup>1</sup> ([ORCID: 0000-0001-7720-0113](https://orcid.org/0000-0001-7720-0113))
- Miki Umetani<sup>1</sup> ([ORCID: 0000-0002-3171-4327](https://orcid.org/0000-0002-3171-4327))
- Moritoshi Sato<sup>2</sup> ([ORCID: 0000-0002-3095-5831](https://orcid.org/0000-0002-3095-5831))
- Yuichi Wakamoto<sup>1</sup> ([ORCID: 0000-0002-6233-0844](https://orcid.org/0000-0002-6233-0844)) †

### Affiliations

1. Department of Basic Science, Graduate School of Arts and Sciences, The University of Tokyo Meguro-ku Japan ([ROR:057zh3y96](https://ror.org/057zh3y96))
2. Research Center for Complex Systems Biology, The University of Tokyo Tokyo Japan ([ROR:057zh3y96](https://ror.org/057zh3y96))
3. Department of Life Sciences, Graduate School of Arts and Sciences, The University of Tokyo Tokyo Japan ([ROR:057zh3y96](https://ror.org/057zh3y96))
4. Universal Biology Institute, The University of Tokyo Tokyo Japan ([ROR:057zh3y96](https://ror.org/057zh3y96))

† Corresponding author

## Abstract

Genetic modifications, such as gene deletion and mutations, could lead to significant changes in physiological states or even cell death. Bacterial cells can adapt to diverse external stresses, such as antibiotic exposure, but can they also adapt to detrimental genetic modification? To address this issue, we visualized the response of individual Escherichia coli cells to deletion of the antibiotic resistance gene under chloramphenicol (Cp) exposure, combining the light-inducible genetic recombination and microfluidic long-term single-cell tracking. We found that a significant fraction (∼40%) of resistance-gene-deleted cells demonstrated a gradual restoration of growth and stably proliferated under continuous Cp exposure without the resistance gene. Such physiological adaptation to genetic modification was not observed when the deletion was introduced in 10 hr or more advance before Cp exposure. Resistance gene deletion under Cp exposure disrupted the stoichiometric balance of ribosomal large and small subunit proteins (RplS and RpsB). However, the balance was gradually recovered in the cell lineages with restored growth. These results demonstrate that bacterial cells can adapt even to lethal genetic modifications by plastically gaining physiological resistance. However, the access to the resistance states is limited by the environmental histories and the timings of genetic modification.

## Introduction

Bacteria in nature are constantly challenged by environmental and genetic perturbations and must be robust against them for survival. Bacterial cells possess programs to adapt or resist such perturbations. For example, under the conditions of nutrient deprivation, E. coli and related bacteria provoke RpoS-mediated general stress response and globally change the metabolic and gene expression profiles to protect themselves from the stress (Battesti et al., 2011). DNA damage also induces SOS response, which promotes both DNA repair and mutagenesis (Walker, 1996; Taddei et al., 1995). If the mutations in essential genetic elements remain unrepaired, their influence will be propagated to cellular phenotypes or even cause cell death. How rapidly new genetic changes alter cellular phenotypes and whether they always give rise to the same phenotypes in given environments are fundamental questions in genetics (Ryan, 1955; Sun et al., 2018). Nevertheless, such time-dependent and redundant genotype-phenotype correspondences are usually deemed negligible or insignificant in most genetics analyses.

However, the evidence suggests that biological systems can buffer or compensate for the impact of genetic changes at the cytoplasmic and physiological levels (Waddington, 1942). For example, specific molecular chaperons could hinder genetic variations from manifesting as morphological and growth phenotypes in fruit flies (Rutherford and Lindquist, 1998), plants (Queitsch et al., 2002), and bacteria (Fares et al., 2002). Furthermore, the loss of biological functions caused by genetic changes can be compensated for by modulating the RNA and protein levels of the mutated or other related genes in many organisms (El-Brolosy and Stainier, 2017). In Bacillus subtilis, the expression noise of mutant sporulation regulator results in the partial penetrance of its influence to spore-forming phenotypes (Eldar et al., 2009). These observations across diverse organisms suggest that phenotypic consequences of genetic modifications can be modulated based on environmental and physiological contexts, which may promote the survival and evolution of the organisms.

Despite these experimental implications, it remains elusive whether bacterial cells can circumvent even lethal genetic modifications such as antibiotic resistance gene deletion under antibiotic exposure. Furthermore, how cells initially respond to the genetic changes and how their physiological and phenotypic states are modulated in longer timescales are poorly characterized. However, addressing these issues requires precisely defining the timings of genetic changes and tracking individual cells for a long period to unravel their phenotypic transitions and consequences (Sun et al., 2018).

In this study, we resolve these technical issues by combining the photoactivatable Cre (PA-Cre) light-inducible genetic recombination technique (Kawano et al., 2016) and microfluidic long-term single-cell tracking (Wang et al., 2010). We induced a pre-designed deletion of chromosomally encoded and fluorescently tagged drug resistance gene in E. coli directly in the microfluidic device. The results show that all of the resistance-gene-deleted cells under continuous drug exposure showed a decline in growth in 5–7 generations, but a fraction of the resistance-gene-deleted cells gradually restored their growth without additional mutations. In contrast, no cells restored growth when the same deletion was introduced 10 hr or more in advance before drug exposure. Therefore, bacterial cells can physiologically adapt to lethal genetic modifications. However, its feasibility depends on environmental histories, the timings of genetic modifications, and the severity of the antibiotic stress.

## Results

### Resistance gene deletion in E. coli by blue-light illumination

To investigate the response of individual cells to antibiotic resistance gene deletion, we constructed an E. coli strain expressing chloramphenicol acetyltransferase (CAT) tagged with mCherry red fluorescent protein (Figure 1A). CAT confers resistance to chloramphenicol (Cp) by acetylating Cp (Shaw, 1967). The mcherry-cat resistance gene was integrated on the chromosome along with the upstream and downstream loxP sequences so that the resistance gene could be excised by Cre recombinase (Figure 1A). We also introduced the PA-Cre recombination system, which consists of split Cre-recombinase fragments, called CreC and CreN, attached to p-Magnet (p-Mag) and n-Magnet (n-Mag) monomers, respectively (Figure 1B; Kawano et al., 2015). p-Mag and n-Mag are heterodimers derived from the fungal photo-receptor, Vivid (Kawano et al., 2015), which heterodimerize upon blue-light illumination. In the PA-Cre system, blue-light illumination leads to heterodimerizations of p-Mag-CreC and n-Mag-CreN fragments and recovers Cre recombination activity (Figure 1B; Kawano et al., 2016). Therefore, this system allows us to induce the resistance gene deletion at arbitrary timings by blue-light illumination. The original PA-Cre system was designed for use in mammalian cells (Kawano et al., 2016); we thus replaced the plasmid backbone and the promoter for use in E. coli.

![Figure 1.](https://cdn.elifesciences.org/articles/74486/elife-74486-fig1-v1.jpg)

**Figure 1.:** (A) Schematic drawing of an E. coli strain, YK0083. This strain harbors the photo-removable mcherry-cat gene on the chromosome and a low-copy plasmid carrying the pa-cre genes (creN-nmag and pmag-creC). (B) The PA-Cre system. Blue-light illumination provokes the dimerization of two PA-Cre fragments and induces the deletion of the mcherry-cat gene. The micrographs represent the combined images of phase contrast and mCherry-CAT fluorescence channels. Left and right images show the cells before and after blue-light illumination, respectively. (C) Representative time-lapse images of gene-deletion experiments. The upper and lower images show the cells in phase contrast and mCherry-CAT fluorescence channels, respectively. The cell lineages at the closed end of the growth channel (outlined in white) were monitored. A 30-min blue-light illumination starting at $t$ = –0.5 hr led to the loss of mCherry-CAT fluorescence signals in this cell lineage. (D) The transitions of mCherry-CAT fluorescence intensities in resistance-gene-deleted (blue) and non-deleted (red) cell lineages. Lines and shaded areas represent the medians and the 25–75% ranges, respectively. The cyan broken line represents the expected fluorescence decay curve when the fluorescence intensity decreases to half in each generation. (E) Generation time of resistance-gene-deleted and non-deleted cells 10 generations before and after blue-light illumination. The middle line and both edges of the boxes represent the medians and the 25–75% ranges of generation time. Whiskers indicate the minimum and maximum of the data except for the outliers. The points represent the outliers. No significant differences in generation time were detected between the groups at the significance level of 0.01 (p = 0.47 for before BL, p = 0.027 for after BL, p = 0.055 for before BL vs after BL, Mann-Whitney U test).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/74486/elife-74486-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) Schematic diagram of microscope setup. A custom blue-light LED illuminator was placed on the microscope stage to illuminate the microfluidic device. The timing and duration of illumination were controlled by an external timer. (B) Photo images of the microfluidic device and LED illuminator mounted on the microscope stage.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/74486/elife-74486-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** (A) Colonies of YK0083 cells inoculated after blue-light illumination. The YK0083 cells were exposed to blue light for 1 hr in batch culture and spread on agar. The colonies were photographed under the exposure of ambient light (left) and excitation light (right). The colonies of the cells retaining the mcherry-cat gene were visually detectable under the excitation light (arrows). (B) Relationship between blue-light illumination duration and fractions of non-fluorescent colonies. Black points represent the means. Error bars represent standard errors ($N$ = 239 for no IPTG; $N$ = 327 for 0 hr; $N$ = 335 for 0.25 hr; $N$ = 373 for 0.5 hr; $N$ = 344 for 1 hr; $N$ = 350 for 2 hr; $N$ = 296 for 4 hr; $N$ = 209 for 6 hr). ‘no IPTG’ represents the condition where the cells were cultured in the M9 medium without IPTG and not exposed to blue light. (C) The correspondence between mCherry-CAT fluorescence and presence of the cat resistance gene. FL +and FL- represent the presence/absence of mCherry fluorescence visually inspected for the colonies. cat +and cat- represent the presence/absence of the cat gene detected by colony PCR. All non-fluorescent colonies had lost the cat gene. All but one fluorescent colony retained the cat gene.

We first analyzed the response of the constructed strain YK0083 to blue-light illumination under drug-free conditions. Single-cell observations with the mother machine microfluidic device (Wang et al., 2010) and custom stage-top LED illuminator (Figure 1—figure supplement 1) revealed that 30-min blue-light exposure ($\lambda=$ 464∼474 nm, 6.8 mW at the specimen position) led to the loss of mCherry-CAT fluorescence in 25% (50/200) cells (Figure 1C and D, and Video 1), suggesting the deletion of the mcherry-cat gene in these cell lineages. The fluorescence signals decayed to the background level in 4–5 generations, and the decay kinetics was consistent with the dilution by growth (Figure 1D). Furthermore, the 30 min blue-light illumination and genetic recombination did not affect the growth of individual cells (Figure 1E).

![Video 1.](https://cdn.elifesciences.org/articles/74486/elife-74486-video1.mp4.jpg)

**Video 1.:** YK0083 cells were cultured in the mother machine flowing the M9 minimal medium and exposed to blue light from $t$ = –30 min to 0 min (marked with ‘ + BL’). The merged images of phase contrast (grayscale) and mCherry-CAT fluorescence (red) channels are shown. The fluorescence of mCherry-CAT was gradually lost after blue-light illumination in this cell lineage. Scale bar, 5 µm.

Extending illumination duration increased the frequency of cells showing loss of fluorescence, reaching 100% ($n=296$) in 4 hr (Figure 1—figure supplement 2A and Figure 1—figure supplement 2B). We confirmed the correspondence between the loss of mCherry fluorescence and cat gene deletion by colony PCR (Figure 1—figure supplement 2C).

### Fractional continuation of growth against resistance gene deletion under drug exposure

We next induced the deletion of the resistance gene in YK0083 cells in the mother machine, continuously flowing a medium containing 15 µg/mL of Cp. This drug concentration was 1.5-fold higher than the minimum inhibitory concentration (MIC) of the non-resistant strain YK0085 (10 µg/mL), which was constructed by illuminating the YK0083 cells by blue light in batch culture (Figure 2). Therefore, it was expected that this drug concentration would inhibit the growth of resistance-gene-deleted cells. This Cp concentration was significantly lower than the MIC of resistant YK0083 cells (100 µg/mL, Figure 2) and did not influence their elongation rates (Figure 2—figure supplement 1).

![Figure 2.](https://cdn.elifesciences.org/articles/74486/elife-74486-fig2-v1.jpg)

**Figure 2.:** Gray points represent the OD600 of the indicated strains after a 23 hr incubation period in the M9 media containing the corresponding concentrations of Cp. The minimum concentration where OD600 became lower than 0.01 was adopted as the MIC for each strain. A total of 15 µg/mL of Cp was used in the time-lapse experiments (dashed line). The measurements were repeated at least thrice.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/74486/elife-74486-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** Box plots show the elongation rates of the YK0083 cells growing in the mother machine. ‘no Cp’ denotes the drug-free condition; ‘Cp’ denotes the condition under the exposure of 15 µg/mL of Cp. The elongation rates were obtained from the non-deleted cell lineages up to 10 generations after blue-light illumination. We detected no significant differences in elongation rates between the two conditions (p = 0.63, Welch’s $t$-test).

A 30-min blue-light illumination induced the mcherry-cat gene deletion in 24.5% (343/1399) in YK0083 cells (Figure 3A and Video 2). While non-deleted cells continued to grow with their generation time (interdivision time) and mCherry-CAT fluorescence intensity nearly unaffected (Figure 3B and C), resistance-gene-deleted cells gradually showed a decline in growth (Figure 3D–G). The fluorescence intensity of the resistance-gene-deleted cells decayed to the background levels in 4–5 generations (Figure 3D, F and H), and their generation time also increased correspondingly (Figure 3E, G and I). However, while the growth of 62.7% (163/260) of resistance-gene-deleted cells was eventually stopped, the other 37.3% cells restored and continued their growth over 30 generations without the cat resistance gene (Figure 3H and I). The generation time of these cell lineages recovered from 6.3 hr (the median of 6th-9th generations) to 3.0 hr (the median of 21st-30th generations) under the continuous drug exposure (Figure 3I). The elongation rate transitions across multiple generations also manifested the growth recovery (Figure 3—figure supplement 1).

![Figure 3.](https://cdn.elifesciences.org/articles/74486/elife-74486-fig3-v1.jpg)

**Figure 3.:** (A) Time-lapse images of a cell lineage that continued growth and division against mcherry-cat gene deletion. The upper and lower sequences show phase contrast and mCherry fluorescence images, respectively. Blue light was illuminated from $t$ = -0.5 h to 0 hr. The cells at the closed end of the growth channel were monitored during the experiment, which are outlined in white on the images. Scale bar, 5 µm. (B–G) The transitions of mCherry-CAT fluorescence intensities and cell size in single-cell lineages. (B, C) Non-deleted cell lineage. (D, E) Growth-halted resistance-gene-deleted cell lineage. The decrease in cell size after 60 hr was due to the shrinkage of the cell body. (F, G) Growth-restored resistance-gene-deleted cell lineage. (H, I) The transitions of mCherry-CAT fluorescence intensities (H) and generation time (I). The lines and shaded areas represent the medians and the 25–75% ranges, respectively. Red represents non-deleted cell lineages. Blue represents growth-restored resistance-gene-deleted cell lineages. The transitions are shown in generations.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/74486/elife-74486-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** The YK0083 cells were exposed to blue light for 30 min from $t$ = -0.5 hr to 0 hr. (A) Transitions of elongation rates of resistance-gene-deleted YK0083 cell lineages in generations. The lines and shaded areas represent the medians and the 25–75% data ranges, respectively. (B) Transitions of elongation rates in hours after blue-light illumination. The lines represent the medians of elongation rate at each time point. The shaded areas show the 95% error ranges of the median estimated by resampling the cell lineages 1000 times. Red represents the non-deleted cell lineages. Blue represents the growth-restored resistance-gene-deleted cell lineages. Green represents the growth-halted resistance-gene-deleted cell lineages. Gray represents the pre-deleted YK0085 cell lineages.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/74486/elife-74486-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** (A) The correspondence between mCherry-CAT fluorescence and presence of the cat resistance gene. Deletions of resistance gene were induced under exposure to 15 µg/mL of Cp. FL +and FL- represent the presence/absence of mCherry fluorescence visually inspected for the colonies. cat +and cat- represent the presence/absence of the cat gene detected by colony PCR. All non-fluorescent colonies had lost the cat gene. All fluorescent colonies retained the cat gene. (B) Competition between resistance-gene-deleted and non-deleted cells under Cp exposure. Batch cultures of YK0083 cells were illuminated by blue light for 30 min, and the fractions of resistance-gene-deleted cells were quantified by the proportions of non-fluorescence colonies in the cultures sampled at several time points after blue-light illumination. Black points represent the means. Error bars represent standard errors ($N$ = 409 for 0.5 hr; $N$ = 385 for 1 hr; $N$ = 219 for 2 hr; $N$ = 298 for 4 hr; $N$ = 283 for 6 hr).

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/74486/elife-74486-fig3-figsupp3-v1.jpg)

**Figure 3—figure supplement 3.:** (A) The scheme for acquiring the resistance-gene-deleted cells from the mother machine. The culture media flowing out from the mother machine were sampled to obtain the cells that lost the mcherry-cat gene. The media were diluted serially, and the limited-diluted media were taken in 96-well plates and incubated. (B) Correspondence between fluorescence loss and gene deletion. The cell populations were collected from the 96-well plates, and the deletion of mcherry-cat gene was examined by PCR. We detected no bands of both mcherry-cat and cat for Samples 1–5. Sample 6 retained the mcherry-cat gene. The bottom plot shows that the absence of mcherry-cat gene corresponds to the loss of mCherry-CAT fluorescence. (C) MIC test. The OD600 values of Samples 1–6, YK0083 and YK0085 after a 23 hr incubation period at the indicated Cp concentrations are shown (Start OD600, 0.001). The entries with colored backgrounds indicate OD600>0.04.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/74486/elife-74486-fig3-figsupp4-v1.jpg)

**Figure 3—figure supplement 4.:** (A,B) Representative time-lapse images of cell lineages that lost mcherry-cat resistance gene. (A) For growth-halted cell lineages; (B) for growth-restored cell lineages. The upper and lower sequences show phase contrast and mCherry fluorescence images, respectively. Blue light was illuminated from t = -0.5 hr to 0 hr. Cp was removed at t = 72 hr. The cells at the closed end of the growth channel were monitored during the experiment, which are outlined in white on the images. Scale bars, 2.5 µm. (C) Transitions of mCherry-CAT fluorescence intensities and cell size in single-cell lineages. The upper plots show the transitions in a growth-halted resistance-gene-deleted cell lineage; the lower plots show those of a growth-restored resistance-gene-deleted cell lineage. The solid black lines represent the end time of blue light illumination. The dashed black lines represent the time of Cp removal. (D) Transition of generation time after Cp removal. The lines and shaded areas represent the medians and the 25–75% ranges, respectively. The transitions are shown in generations after first cell divisions. Red, blue, and green represent non-deleted cell lineages, growth-restored resistance-gene-deleted cell lineages, and growth-halted resistance-gene-deleted cell lineages, respectively. The p-values of Mann-Whitney test were 0.11, 0.31, 0.45, 0.089, 0.50, 0.012, 0.038, and 0.27 for growth-halted vs growth-restored cell lineages for the generations from 1st to 8th, respectively. Also, the p-values were 0.057, 0.0070, 0.23, 0.48, 0.17, 0.032, 0.14, and 0.063 for resistance-gene-deleted vs non-deleted cell lineages. The p-values below 0.01 were assumed significant and indicated by asterisk.

![Figure 3—figure supplement 5.](https://cdn.elifesciences.org/articles/74486/elife-74486-fig3-figsupp5-v1.jpg)

**Figure 3—figure supplement 5.:** (A) mCherry-CAT fluorescence before blue-light illumination. Each point represents the fluorescence intensity of single-cell lineage averaged over the 1 hr period immediately before blue-light illumination. Blue points represent the growth-restored resistance-gene-deleted cell lineages. Green points represent the growth-halted resistance-gene-deleted cell lineages. Red points represent the non-deleted cell lineages. p = 0.30 for growth-restored resistance-gene-deleted cell lineages vs growth-halted resistance-gene-deleted cell lineages; p = 0.85 for resistance-gene-deleted cell lineages vs non-deleted cell lineages, Welch’s t-test. (B) Elongation rates before blue-light illumination. Each point represents the elongation rate of single-cell lineage averaged over the 1 h period immediately before blue-light illumination. The color correspondence remains the same as A. p = 0.12 for growth-restored resistance-gene-deleted cell lineages vs growth-halted resistance-gene-deleted cell lineages; p = 0.35 for resistance-gene-deleted cell lineages vs non-deleted cell lineages, Welch’s t-test.

![Video 2.](https://cdn.elifesciences.org/articles/74486/elife-74486-video2.mp4.jpg)

**Video 2.:** YK0083 cells were cultured in the mother machine flowing the M9 minimal medium containing 15 µg/mL of Cp. Blue light was illuminated from $t$ = –30 min to 0 min (marked with ‘ + BL’). The merged images of phase contrast (grayscale) and mCherry-CAT fluorescence (red) channels are shown. The illumination caused the loss of fluorescence signals, that is, the deletion of the mcherry-cat gene, in this cell lineage. Nevertheless, the cell gradually restored growth and division under continuous Cp exposure. Scale bar, 5 µm.

We first suspected that the growth recovery under Cp exposure was attributed to the presence of the cat gene untagged from the mcherry gene or by additional unintended resistance-enhancing mutations. To test this hypothesis, we illuminated batch cultures of YK0083 cells by blue light for 30 min under exposure to 15 µg/mL of Cp and plated them on agar plates. Colony PCR confirmed that all the cells that lost mCherry fluorescence were also cat-negative even when the deletion was introduced under Cp exposure (Figure 3—figure supplement 2A). This result strongly suggests that the growth-restored cells do not retain the cat-resistance gene as designed. The fraction of resistance-gene-deleted cells after 30-min blue-light illumination monotonically decreased in batch culture containing 15 µg/mL of Cp (Figure 3—figure supplement 2B), which is consistent with the observation that growth-restored resistance-gene-deleted cells grew more slowly than non-deleted cells.

In addition, we sampled the culture media flowing out from the microfluidic device and obtained cell populations derived from a single or few ancestral cells by limiting dilution (Figure 3—figure supplement 3A). PCR analysis confirmed the lack of cat gene in the non-fluorescent cell populations (Figure 3—figure supplement 3B). Furthermore, whole-genome sequencing of the cell populations obtained by limiting dilution showed no additional mutations in four out of five non-fluorescent cell populations tested (Table 1). One point mutation was present in one cellular population, but this mutation did not affect the MIC (Figure 3—figure supplement 3C). To calculate the probability that all of these five non-fluorescent cell populations had originated from resistance-gene-deleted growth-halted cells, we analyzed the regrowing dynamics of both growth-restored and growth-halted cell lineages after removing Cp in the microfluidic device (Figure 3—figure supplement 4A-C and Video 3). We found that 91.3% (73/80) of growth-restored cell lineages recovered fast growth after the exposure to 15 µg/mL of Cp for 72 hr. On the other hand, the proportion of cells that recovered growth was lower for the growth-halted cell lineages; only 69.3% (140/202) of growth-halted cell lineages could resume growth. The growth after first cell divisions were as fast as that for the non-deleted cells and was indistinguishable between the growth-restored and growth-halted cell lineages (Figure 3—figure supplement 4D). Taking the fraction of growth-restored cells among the resistance-gene-deleted cells and the proportions of growth-recovered cells after Cp removal into account, we found that the probability that all the five cell populations were derived from growth-halted cell lineages was 5.5% (see Materials and methods). Therefore, the probability that unintended genetic changes were responsible for the growth restoration is small.

**Table 1.**
 Mutations detected by whole-genome sequencing.We obtained isolated cellular populations derived from single or few cells by limiting dilution of the culture media flowing out from the mother machine. We detected only one point mutation in Sample 3.


<table>
  <thead>
    <tr>
      <th>Sample no.</th>
      <th>Mutation</th>
      <th>Position</th>
      <th>Base</th>
      <th>Annotation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Sample 1</td>
      <td>No mutation</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sample 2</td>
      <td>No mutation</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sample 3</td>
      <td>Mutation in leuC site</td>
      <td>80,471</td>
      <td>G - &gt; T</td>
      <td>A132S</td>
    </tr>
    <tr>
      <td>Sample 4</td>
      <td>No mutation</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sample 5</td>
      <td>No mutation</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

![Video 3.](https://cdn.elifesciences.org/articles/74486/elife-74486-video3.mp4.jpg)

**Video 3.:** Left, growth-halted resistance-gene-deleted cell; Right, Growth-restored resistance-gene-deleted cells. Cp was removed at $t$ = 0 min (72 hr after blue light illumination). The merged images of phase contrast (grayscale) and mCherry-CAT fluorescence (red) channels are shown. Scale bar, 5 µm.

It is also unlikely that the growth restoration was caused by the residual mCherry-CAT proteins because 30 consecutive cell divisions dilute cytoplasmic proteins $2^{30}≈10^{9}$ folds if additional production is prevented; note that even the total number of protein molecules in a bacterial cell are in the order of 106-107 (Milo, 2013) We also detected no significant differences in the mCherry-CAT fluorescence intensity before blue-light illumination between the growth-halted and growth-restored cell lineages (Figure 3—figure supplement 5A). Furthermore, no significant differences were observed even between the resistance-gene-deleted and non-deleted cell lineages (Figure 3—figure supplement 5A). We also examined the influence of elongation rate before blue-light illumination on the gene deletion and the fates after gene deletion, finding no correlations (Figure 3—figure supplement 5B). Therefore, neither the amount of mCherry-CAT proteins at the time of gene deletion nor pre-deletion elongation rate affected the likelihood of gene deletion and the determination of growth-halt and growth-restoration fates under these experimental conditions.

We also found that deleting the mcherry-cat gene flowing a medium containing a twofold concentration of Cp (i.e., 30 µg/mL) eliminated growth-restored cell lineages: 33.1% (361/1092) of the cells illuminated by blue light lost the resistance gene, and none of them restored growth. This result suggests that deleting the resistance gene at the concentrations of Cp sufficiently higher than the MIC can prevent physiological adaptation.

### Resistance gene deletion long before Cp exposure prevents growth restoration

The high frequency of growth restoration observed against the resistance gene deletion was unexpected since the MIC of the susceptible strain was below 15 µg/mL (Figure 2 and Figure 3—figure supplement 3C). To understand this discrepancy, we cultured the susceptible YK0085 cells in the mother machine first without Cp and then exposed them to 15 µg/mL of Cp directly in the device. In contrast to the previous observation, all cells stopped growth and division entirely, with no cells restoring growth (“Pre-deleted” in Figure 4A–C and Video 4). This result excludes the hypothesis that the unique cultivation environments in the microfluidics device are the cause of growth restoration. Instead, this observation implies that the timing of gene deletion is crucial for the cells to withstand the Cp exposure without the resistance gene and restore growth.

![Figure 4.](https://cdn.elifesciences.org/articles/74486/elife-74486-fig4-v1.jpg)

**Figure 4.:** (A) The schematic diagram of experiments. The duration from the end of blue-light illumination to the onset of Cp exposure ($T_{c}$) was varied from 0 to 10 h. $T_{c}≪0$ represents the continuous Cp-exposure condition. “Pre-deleted” denotes the results of the experiments performed with the mcherry-cat-deleted YK0085 strain. The non-resistant YK0085 cells were not exposed to blue light. (B) Fractions of mcherry-cat-deleted cell lineages across different $T_{c}$ conditions. The numbers of resistance-gene-deleted cell lineages among the total numbers of cell lineages observed during the measurements are shown above the bars. Error bars represent standard errors. (C) Fractions of growth-restored cell lineages among resistance-gene-deleted cell lineages. The numbers of growth-restored cell lineages among all the resistance-gene-deleted cell lineages are shown above the bars. Error bars represent standard errors. The numbers of resistance-gene-deleted cell lineages are different from those in B because some cell lineages were flushed away from the growth channels at the later time points of the measurements, and their fates could not be determined. (D, E) The distributions of the mCherry-CAT fluorescence intensities at the onset of Cp exposure across the different $T_{c}$ conditions represented by histograms (D) and box plots (E). (F) Fractions of growth-restored cell lineages and their dependence on the mCherry-CAT fluorescence at the onset of Cp exposure. Blue and orange bars indicate the fractions of growth-restored cells among cell lineages whose mCherry-CAT fluorescence intensities were higher and lower than the median, respectively. Error bars represent standard errors. The growth-restored cell lineages were not detected under the $T_{c}$ = 10 h and “Pre-deleted” conditions. Fractional differences between the top 50% and the bottom 50% of cell lineages were statistically significant only for the $T_{c}$ = 6 h condition (p = 0.86 for $T_{c}$ = 0 hr; p = 0.28 for $T_{c}$ = 3 hr; and p = 8.6 × 10–3 for $T_{c}$ = 6 hr, two proportional z-test).

![Video 4.](https://cdn.elifesciences.org/articles/74486/elife-74486-video4.mp4.jpg)

**Video 4.:** YK0085 cells were cultured in the mother machine flowing the M9 minimal medium and exposed to 15 µg/mL of Cp at $t$ = 0 min (marked with ‘ + Cp’). The Cp exposure caused growth arrest, and, unlike the YK0083 cells, the cell did not restore growth. We found no growth-restored cell lineages in this experimental condition. Scale bar, 5 µm.

To further investigate the importance of the timing of gene deletion, we performed microfluidic single-cell measurements with the resistant YK0083 strain, varying the duration from blue-light illumination to the onset of Cp exposure ($T_{c}$) between 0 h to 10 h (Figure 4A). The proportions of cells that lost the mcherry-cat gene in response to blue-light illumination almost remained unchanged among all conditions, ranging from 24% to 28% (Figure 4B). However, the proportions of growth-restored cell lineages among resistance-gene-deleted cells strongly depended on $T_{c}$ (Figure 4C). When Cp exposure was initiated immediately after the blue-light illumination ($T_{c}=$ 0 hr) or after 3 h ($T_{c}=$ 3 hr), the proportions of growth-restored cells were nearly equivalent to those observed under continuous Cp exposure conditions (Figure 4C). In contrast, the proportions of growth-restored cells were reduced to 18.5% (34/184) when $T_{c}=6$ hr, and we did not detect any growth restoration when $T_{c}$ = 10 hr (0/195; Figure 4C). The almost equivalent frequencies of growth-restored cell lineages under the $T_{c}$ = 0 hr and $T_{c}$ = 3 hr conditions and those observed under continuous exposure exclude the possibility that growth restoration requires prior exposure to Cp before resistance gene deletion.

We next conjectured that a low amount of mCherry-CAT proteins is required at the onset of Cp exposure to withstand and restore growth without the resistance gene. In fact, mcherry-cat gene deletion before Cp exposure led to the dilution of mCherry-CAT proteins by growth by the time of Cp exposure (Figure 4D and E).

To examine whether the mCherry-CAT concentration in individual cells affects growth restoration, we divided the resistance-gene-deleted cell lineages into two groups under each condition (top 50% and bottom 50%) based on their mCherry-CAT fluorescence intensities at the onset of Cp exposure. While we found no significant differences in the $T_{c}$ = 0 and 3 hr conditions, the top 50% group produced 2.4-fold more growth-restored cells than the bottom 50% group in the $T_{c}$ = 6 hr condition (Figure 4F). In the $T_{c}$ = 10 hr condition, we could barely detect the fluorescence signals from any cells (Figure 4D and E), and no cells showed growth restoration as mentioned above (Figure 4F). These results suggest that a low level of residual mCherry-CAT proteins is required at the onset of Cp exposure, but high amounts do not necessarily ensure the growth restoration in all resistance-gene-deleted cells. Moreover, 40% could be considered as the maximum frequencies at which cells can restore growth without the resistance gene.

### Growth restoration accompanies the recovery of stoichiometric balance of ribosomal subunits

The results above demonstrated that the residual mCherry-CAT proteins are important for initiating the transition to growth restoration without the resistance gene. However, the residual proteins cannot directly support the growth in later generations under Cp exposure as their levels are eventually diluted with growth. Indeed, the amounts of mCherry-CAT proteins during growth restoration were below the detection limit (Figure 3F and H). Therefore, we speculated that the other physiological changes were responsible for growth restoration.

Because Cp targets the 50 S ribosomal subunit (Pongs, 1979), it is plausible that ribosomal states were modulated in the duration beginning from resistance gene deletion to growth restoration. Hence, we constructed an E. coli strain YK0136 that expressed fluorescently-tagged dual ribosomal reporters, RplS-mCherry and RpsB-mVenus (Figure 5A; Nikolay et al., 2014). RplS and RpsB are ribosomal proteins in the 50 S and 30 S subunits, respectively. Their fluorescent reporters were utilized to probe the ribosomal subunit balance in living cells (Nikolay et al., 2014). YK0136 also harbors the cat resistance gene (not tagged with mcherry) between the upstream and downstream loxP sequences on the chromosome, and the PA-Cre recombination system was expressed via the plasmid (Figure 5A). We confirmed that YK0136 showed MIC values almost equivalent to those of the YK0083 strain (Figure 2 and Figure 5—figure supplement 1). Furthermore, 30-min blue-light illuminations provoked cat-gene deletion in 28.6% (452/1587) of YK0136 cells, which was comparable to the frequency of mcherry-cat-gene deletion in YK0083 (Figure 4B).

![Figure 5.](https://cdn.elifesciences.org/articles/74486/elife-74486-fig5-v1.jpg)

**Figure 5.:** (A) Schematic diagram of the ribosome reporter strain, YK0136. Fluorescently tagged ribosomal protein genes (rplS and rpsB) are expressed from the native loci on the chromosomes. Additionally, the photo-removable cat gene was integrated into the intC locus on the chromosome. The PA-Cre fragments were expressed via low-copy plasmids. (B) Transitions of elongation rates. Lines represent the medians of elongation rates at each time point, and shaded areas show the 95% error ranges of the medians estimated by resampling the cell lineages 1000 times. Red represents non-deleted cell lineages. Green shows growth-halted resistance-gene-deleted cell lineages. Blue represents growth-restored resistance-gene-deleted cell lineages. Gray represents pre-deleted cell lineages. Color correspondence remains the same in the following figures. The end of blue-light illumination was set to 0 hr on the horizontal axis. (C–E) Transitions of RplS-mCherry fluorescence intensities (C), RpsB-mVenus fluorescence intensities (D), and the fluorescence ratio of RplS-mCherry/RpsB-mVenus (E). The fluorescence intensities of RplS-mCherry and RpsB-mVenus were normalized by the intensity observed before blue light illumination to calculate the ratio in E. (F) Transitions of the RplS-mCherry/RpsB-mVenus fluorescence ratio distributions. The vertical dashed lines represent the position of ratio = 1; the solid lines represent the medians of the distributions. Significant differences in fluorescence ratio were detected between the growth-restored and growth-halted cell lineages at 50 hr and 65 hr (p = 5.6 × 10 –10 at 50 hr, p = 1.9 × 10 –13 at 65 hr, Mann-Whitney U test).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/74486/elife-74486-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** Gray points indicate the OD600 of the cell cultures after a 23 hr incubation period in the media containing the corresponding concentrations of Cp. The left shows the result of YK0136. The right shows the result of YK0138. The minimum concentration where OD600 became lower than 0.01 was adopted as the MIC for each strain. 15 µg/mL of Cp was used in the experiments (dashed line). The measurements were repeated at least thrice.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/74486/elife-74486-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** (A) Hierarchical clustering of single-cell lineages based on the transitions of mCherry-CAT fluorescence intensities. The mCherry-CAT fluorescence transitions in single-cell lineages over the entire periods of measurement were used for clustering. The distances between cell lineages were calculated by dynamic time warping. The numbers shown on the horizontal axis represent cell lineage IDs. The background colors behind the cell lineage IDs represent the fates of cell lineages assigned manually by the experimenters: Blue corresponds to growth-restored resistance-gene-deleted cell lineages; Green represents growth-halted resistance-gene-deleted cell lineages; Red represents non-deleted cell lineages. (B) Hierarchical clustering of single-cell lineages based on the transitions of elongation rates. The cell lineage clusters indicated by the blue and red dotted lines constitute two main groups, corresponding to resistance-gene-deleted and non-deleted cell lineages, respectively. Only one resistance-gene-deleted cell lineage (0011) was assigned wrongly as a non-deleted cell lineage. Therefore, the transitions of elongation rates are sufficient for classifying the resistance-gene-deleted and non-deleted cell lineages at high precision.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/74486/elife-74486-fig5-figsupp3-v1.jpg)

**Figure 5—figure supplement 3.:** Left: Generation time transitions; Right: RplS-mCherry/RpsB-mVenus fluorescence ratio transitions. The lines and shaded areas represent the medians and the 25%–75% data ranges, respectively. Blue corresponds to growth-restored resistance-gene-deleted cell lineages. Red corresponds to non-deleted cell lineages.

![Figure 5—figure supplement 4.](https://cdn.elifesciences.org/articles/74486/elife-74486-fig5-figsupp4-v1.jpg)

**Figure 5—figure supplement 4.:** Mann-Whitney U test was performed for the fluorescence ratio between growth-restored resistance-gene-deleted cell lineages and growth-halted resistance-gene-deleted cell lineages at each time point after blue-light illumination. Dashed horizontal line represents the p-value of 0.01.

![Figure 5—figure supplement 5.](https://cdn.elifesciences.org/articles/74486/elife-74486-fig5-figsupp5-v1.jpg)

**Figure 5—figure supplement 5.:** (A) Relationship between elongation rates before blue-light illumination and cellular fates. Blue represents growth-restored resistance-gene-deleted cell lineages. Green represents growth-halted resistance-gene-deleted cell lineages. Red represents non-deleted cell lineages (Color correspondence remains the same in the following figures). Each point represents the elongation rate of single-cell lineage averaged over the 1 hr period immediately before blue-light illumination. p = 0.10 for growth-restored vs growth-halted cell lineages; p = 0.54 for resistance-gene-deleted vs non-deleted cell lineages, Welch’s t-test. (B) Relationship between RplS-mCherry fluorescence intensities averaged over the 1 hr period before blue-light illumination and cellular fates. p = 0.87 for growth-restored vs growth-halted cell lineages; p = 0.038 for resistance-gene-deleted vs non-deleted cell lineages, Welch’s t-test. (C) Relationship between RpsB-mVenus fluorescence intensities averaged over the 1 hr period before blue-light illumination and cellular fates. p = 0.60 for growth-restored vs growth-halted cell lineages; p = 0.010 for resistance-gene-deleted vs non-deleted cell lineages, Welch’s t-test. Asterisk denotes the statistical difference judged at the significance level of 0.01. (D) Relationship between RplS-mCherry/RpsB-mVenus fluorescence ratio averaged over the 1 hr period before blue-light illumination and cellular fates. p = 0.098 for growth-restored vs growth-halted cell lineages; p = 0.15 for resistance-gene-deleted vs non-deleted cell lineages, Welch’s t-test.

We conducted time-lapse measurements of YK0136 cells in the mother machine and induced the deletion of the resistance gene via blue-light illumination under continuous exposure to 15 µg/mL of Cp (Video 5). Since previous experiments showed that the resistance gene deletion decelerates cellular growth significantly, the deletion of the cat gene in each cell lineage was evaluated based on the distinctive declines of cellular elongation rates after the blue-light illumination. We validated this criterion by hierarchical time-series clustering applied to the growth of YK0083 cells and mCherry-CAT fluorescence transitions (Figure 5—figure supplement 2 and Materials and methods).

![Video 5.](https://cdn.elifesciences.org/articles/74486/elife-74486-video5.mp4.jpg)

**Video 5.:** YK0136 cells were cultured in the mother machine flowing the M9 minimal medium containing 15 µg/mL of Cp. Blue light was illuminated from $t$ = –30 min to 0 min (marked with ‘ + BL’). The merged images of phase contrast (grayscale), RplS-mCherry fluorescence (red), and RpsB-mVenus fluorescence (green) channels are shown. The growth of the cell markedly slowed down after blue-light illumination, indicating the loss of the cat gene. The cell became red in response to blue-light illumination, indicating that the relative expression level of RplS-mCherry became higher than that of RpsB-mVenus. However, the balance was restored alongside growth restoration. Scale bar, 5 µm.

As observed previously, 45.9% (158/344) of the cat-deleted YK0136 cells gradually restored their growth after initial growth suppression (Figure 5B, Figure 5—figure supplement 3, and Video 5). Furthermore, such growth-restored cell lineages were not observed (0/1138) when YK0138 cells were exposed to 15 µg/mL of Cp; the YK0138 strain was constructed from YK0136 cells by deleting the cat gene beforehand in batch culture via blue-light illumination (Figure 5B and Video 6).

![Video 6.](https://cdn.elifesciences.org/articles/74486/elife-74486-video6.mp4.jpg)

**Video 6.:** YK0138 cells were cultured in the mother machine flowing the M9 minimal medium and exposed to 15 µg/mL of Cp at $t$ = 0 min (marked with ‘ + Cp’). The Cp exposure caused growth arrest and disruption of ribosomal proteins’ expression balance. No restoration of growth and ribosomal balance was observed. Scale bar, 5 µm.

The transitions of fluorescence intensities reveal that cat-gene deletion under Cp exposure increased the expression levels of both RplS-mCherry and RpsB-mVenus (Figure 5C and D). The relative changes triggered by deletion were more significant for RplS-mCherry than those for RpsB-mVenus (Figure 5C and D). Consequently, the ribosomal subunit balance probed by the RplS-mCherry/RpsB-mVenus ratio was disrupted, and the ratio increased approximately 3-fold (Figure 5E and F). The initial disruption kinetics was similar between growth-restored and growth-halted resistance-gene-deleted cell lineages (Figure 5E). However, the ratio of growth-restored cell lineages gradually returned to the original level, whereas the ratio of growth-halted cell lineages remained disrupted (Figure 5E and F). The difference in the ratio between growth-restored and growth-halted cell lineages became evident approximately 37 hr after resistance gene deletion (Figure 5—figure supplement 4). These results suggest that the regain of the ribosomal subunit balance under Cp exposure is correlated with growth restoration.

Analysis of the correlations between the pre-illumination phenotypic traits and post-illumination cellular fates reveals that elongation rates, fluorescence intensities of RplS-mCherry and RpsB-mVenus, and the fluorescence ratio observed before blue-light illumination did not strongly affect the likelihood of gene deletion and the determination of growth-halting and growth-restoration fates (Figure 5—figure supplement 5).

When non-resistant YK0138 cells were exposed to 15 µg/mL of Cp, the expression levels of RplS-mCherry increased initially following kinetics similar to those of the YK0136 cells observed after cat-gene deletion (Figure 5C). In contrast, the expression levels of RpsB-mVenus decreased in response to Cp exposure (Figure 5D), as previously reported for a wildtype E. coli strain exposed to Cp (Siibak et al., 2011). The initial decrease of RpsB-mVenus expression led to a more rapid disruption of the RplS-mCherry/RpsB-mVenus ratio in the susceptible YK0138 cells (Figure 5E and F). Consistently, the decline in the elongation rates of the YK0138 cells was faster than those of the YK0136 cells (Figure 5B).

We further examined the relationship between the RplS-mCherry/RpsB-mVenus ratio and elongation rates and observed a negative correlation (Spearman $ρ$ = –0.58, 95% confidence interval [-0.62,–0.53]; Figure 6A). The ratio was maintained within a narrow range (0.84–1.18, 95% interval) before blue-light illumination (Figures 5F and 6A). The disruption of ribosomal subunit balance exceeding this range was linked to growth suppression (Figure 6A). The relationships between the ratio and elongation rates were similar among growth-restored resistance-gene-deleted cell lineages, growth-halted resistance-gene-deleted cell lineages, and pre-deleted cell lineages (Figure 6A). However, the distribution of the points was shifted toward the original fluorescence ratio for the growth-restored resistance-gene-deleted cell lineages (Figure 6B–D). These results suggest that the ribosomal subunit balance is correlated with growth under Cp exposure and that restoration of the subunit balance might help cells to recover growth in the absence of the resistance gene.

![Figure 6.](https://cdn.elifesciences.org/articles/74486/elife-74486-fig6-v1.jpg)

**Figure 6.:** (A) Scatter plot of the RplS-mCherry/RpsB-mVenus fluorescence ratio and elongation rate. Small points represent the relations between the fluorescence ratio and elongation rates averaged over the two-hour periods at the different time points on the single-cell lineages. The larger open point represents the mean elongation rate in each bin of fluorescence ratio (bin width, 0.2 a.u.). Error bars represent the 1.96× standard error ranges. Blue represents growth-restored resistance-gene-deleted cell lineages. Green represents growth-halted resistance-gene-deleted cell lineages. Gray represents pre-deleted cell lineages. Dashed lines indicate the mean ± 1.96× standard error range of fluorescence ratio of non-deleted cell lineages before blue-light illumination. (B–D) Density plots of the points for the relationships between fluorescence ratio and elongation rate. (B) Growth-restored resistance-gene-deleted cell lineages. (C) Growth-halted resistance-gene-deleted cell lineages. (D) Pre-deleted cell lineages. Color represents the density of the points for each type of cell lineages shown in (A). Bin size was 0.05 hr-1 for elongation rate and 0.1 a.u. for fluorescence ratio.

## Discussion

Uncovering the genotype-phenotype correspondences in various biological contexts is the groundwork for genetics. However, the correspondences are usually investigated based on terminal phenotypes, which are often manifested after significant lags following genotypic changes. Consequently, our understanding of the dependence of terminal phenotypes on historical conditions and the heterogeneity of phenotypic consequences among individual cells remains limited. In this study, we demonstrated that E. coli cells could adapt even to a lethal genetic modification, that is the deletion of cat resistance gene under exposure to chloramphenicol (Figure 3). Importantly, such adaptation was not observed when an identical genetic modification was introduced long before Cp exposure (Figure 4). Therefore, whether cells could gain physiological resistance in the absence of a resistance gene depends on the timing of resistance gene deletion and environmental histories that the cells experienced.

The analyses revealed that the cat gene deletion under Cp exposure disrupted the stoichiometric balance of ribosomal proteins (RplS and RspB) and that the balance was gradually recovered alongside growth restoration (Figure 5). The elongation rate and the stoichiometric balance of ribosomal proteins were strongly correlated (Figure 6). Furthermore, the balance was tightly regulated within a narrow range in the fast-growing non-deleted cells (Figure 5F). Therefore, the recovery of ribosomal stoichiometric balance might contribute to restoring growth against the deletion of the resistance gene.

It still remains elusive how individual cells recovered the ribosomal stoichiometric balance under continuous Cp exposure. A plausible scenario might be that the multi-layered and interlinked feedback regulations on ribosomal components entailed stoichiometry readjustments (Yamagishi and Nomura, 1988; Nomura et al., 1984; Lindahl and Zengel, 1986; Keener and Nomura, 1996; Kaczanowska and Rydén-Aulin, 2007). Many ribosomal proteins bind to their own mRNAs, in addition to the target ribosomal RNAs (Nomura et al., 1984; Lindahl and Zengel, 1986; Keener and Nomura, 1996; Kaczanowska and Rydén-Aulin, 2007). These regulatory fractions of ribosomal proteins bind to their mRNAs and inhibit their own translation and that of other genes in the same operons. The competition among rRNA and mRNA for these regulatory ribosomal protein components is considered to regulate the stoichiometry of ribosomal components (Nomura et al., 1984; Lindahl and Zengel, 1986; Keener and Nomura, 1996; Kaczanowska and Rydén-Aulin, 2007). Therefore, it is plausible that these innate homeostatic mechanisms of ribosomes might have been exploited by cells to restore growth. It is also important to note that the operons for ribosomal proteins comprise genes encoding RNA polymerase subunits, translation initiation/elongation factors, DNA primase and protein transmembrane transporters (Lindahl and Zengel, 1986; Keener and Nomura, 1996). Hence, the feedback regulations in ribosomes could mediate changes in the global expression profiles, which might have helped the cells find growth-permissive states in the presence of Cp.

The necessity for a small amount of residual resistant proteins at the onset of Cp exposure (Figure 4) might suggest that experiencing such barely-tolerable intracellular states is crucial for gaining physiological resistance. The importance of near-critical states for survival might be related to the phenomenon that pre-treatment with a sublethal concentration of antibiotics increases the fraction of persister cells in response to the subsequent treatments with lethal antibiotic concentrations (Dörr et al., 2009; Johnson and Levin, 2013). We also remark that the physiological adaptation to the antibiotic stress caused by resistance gene deletion might be related to adaptive resistance. Adaptive resistance is a phenomenon in which bacterial populations progressively enhance their resistance levels (MICs) when subject to gradual increases of antibiotics (George and Levy, 1983; Adam et al., 2008; Sánchez-Romero and Casadesús, 2014; Motta et al., 2015). Adaptive resistance is achieved physiologically rather than genetically since the enhanced resistance is lost when the antibiotic is removed. Therefore, it is plausible that growth-restoration against resistance gene deletion might be realized by some mechanisms common to adaptive resistance. The fact that no cells recovered growth when the resistance gene was deleted at a high Cp concentration (30 µg/mL) also suggests a link to adaptive resistance; the speed of antibiotic stress intensification must be sufficiently slow for the cells to gain resistance physiologically. However, we also remark that it is nontrivial whether bacterial cells respond to the intensification of antibiotic stress caused by internal resistance-gene deletion similarly to the stress caused by gradual increases of external antibiotic concentrations. Although our results might support the hypothesis that physiological adaptation to genetic perturbations that sensitize cells to some antibiotics is feasible when bacterial cells exhibit adaptive resistance to those drugs, more careful examinations under diverse experimental conditions should be needed to understand the identity of these internally and externally intensified antibiotic stress. Additionally, we note that adaptive resistance has been investigated at the population level, not at the single-cell level, in the previous studies (George and Levy, 1983; Adam et al., 2008; Sánchez-Romero and Casadesús, 2014). Consequently, it remains elusive whether only a small fraction of cell lineages in the populations acquire resistance and dominate the populations by selection, or most cells can progressively enhance resistance in adaptive resistance. In this study, using the mother machine microfluidic device, we were able to quantify the fractions of cell lineages that restore growth against resistance-gene deletion and the changes of the fractions depending on the historical conditions. Such single-cell-level quantitative information would be valuable for unraveling the windows of phenotypic space and the ranges of conditions permitting physiological adaptation to antibiotics.

Though experimental evidence of history-dependent physiological adaptation to lethal genetic perturbations is still limited, the experimental strategy combining optogenetic recombination and single-cell lineage tracking is applicable for the modification of other genes or other cell types, including mammalian cells. Such approaches might offer new insights into the emergence of drug-resistant bacterial and cancer cells. We remark that growth-restoration of resistance-gene-deleted cells must have been hardly recognized in batch-culture experiments because the fractions of these slow-growing cells decrease in time by selection within cell populations (Figure 3—figure supplement 2B). Therefore, our study also confirms the advantage of microfluidic time-lapse microscopy for unraveling long-term adaptation phenomena that occur in slow-growing cell lineages. Gaining a more comprehensive picture of resistance evolution might help us design new drug treatment strategies to counter or control the emergence and spread of resistance.

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
      <td>Strain,strain background (Escherichia coli)</td>
      <td>F3</td>
      <td>[31]</td>
      <td></td>
      <td>W3110 ΔfliC::FRT ΔfimA::FRT Δflu::FRT</td>
    </tr>
    <tr>
      <td>Strain,strain background (Escherichia coli)</td>
      <td>YK0083</td>
      <td>This study</td>
      <td></td>
      <td>F3 intC::PLtetO1-loxP-RBS4-mcherry-cat-loxP-FRT/pYK022</td>
    </tr>
    <tr>
      <td>Strain,strain background (Escherichia coli)</td>
      <td>MUS6</td>
      <td>This study</td>
      <td></td>
      <td>F3 rplS-mcherry-FRT rpsB-mvenus-FRT</td>
    </tr>
    <tr>
      <td>Strain,strain background (Escherichia coli)</td>
      <td>YK0136</td>
      <td>This study</td>
      <td></td>
      <td>MUS6 intC::PLtetO1-loxP-RBS4-cat-loxP-FRT/pYK022</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pmag-creC</td>
      <td>[12]</td>
      <td></td>
      <td>gifted from Sato lab.</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>nmag-creN</td>
      <td>[12]</td>
      <td></td>
      <td>gifted from Sato lab.</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pYK022</td>
      <td>This study</td>
      <td></td>
      <td>plasmid expressing PA-Cre genes.</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>intC_check_F</td>
      <td>This study</td>
      <td>PCR primerfor intC check</td>
      <td>GATCGATACTTGCTGTGGTTGATG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>intC_check_R2</td>
      <td>This study</td>
      <td>PCR primerfor intC check</td>
      <td>CCTCTTAGTTAAATGGATATAACGAGCCCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>YKp0077</td>
      <td>This study</td>
      <td>PCR primerfor cat check</td>
      <td>CACCGTTGATATATCCCAATGGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>YKp0115</td>
      <td>This study</td>
      <td>PCR primerfor cat check</td>
      <td>CACTCATCGCAGTACTGTTG</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Wizard SVGel and PCRClean-Up System</td>
      <td>Promega</td>
      <td>Cat.# A9281</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>PureYieldPlasmid MiniprepSystem</td>
      <td>Promega</td>
      <td>Cat.# A1223</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>WizardGenomic DNAPurification Kit</td>
      <td>Promega</td>
      <td>Cat.# A1120</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>chloramphenicol</td>
      <td>Wako</td>
      <td>030-19452</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>isopropyl-β-D-thiogalactopyranoside</td>
      <td>Wako</td>
      <td>094-05144</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Bovine Serum Albumin</td>
      <td>Sigma-Aldrich</td>
      <td>Cat.# A6003</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>polydimethylsiloxane</td>
      <td>Dow Corning</td>
      <td>SYLGARD 184</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>FastDTW</td>
      <td>[32]</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>HyperStackReg</td>
      <td>[33]</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

### Bacterial strains, plasmids construction, and culture conditions

E. coli strains, plasmids, and primers are listed in Table 2, Table 3 and Table 4, respectively. For strain constructions, cells were grown in Luria Bertani (LB) broth (Difco) at 37 ºC unless stated otherwise. Plasmids were constructed using DNA ligase (T4 DNA Ligase, Takara) or by ExoIII cloning (Li and Evans, 1997) and introduced into the E. coli strain JM109 for cloning and stocking. The cat or mcherry-cat gene was introduced into the intC locus of F3 (W3110ΔfliC::FRTΔfimA::FRTΔflu::FRT) genome by $\lambda$-Red recombination (YK0080, YK0134) (Datsenko and Wanner, 2000). Fluorescently-tagged ribosome reporter genes were introduced into the E. coli strain BW25113 (MUS3, MUS13). These ribosome reporter genes were transferred into the F3 strain by P1 transduction (MUS5, MUS6). The colonies with intended genome integration were selected on LB plates containing kanamycin (Km, Wako). The Km resistant gene was removed by flp-FRT recombination using pCP20 plasmid (Datsenko and Wanner, 2000).

**Table 2.**
 Strain list used in this study.


<table>
  <thead>
    <tr>
      <th colspan="3">mCherry-CAT deletion</th>
    </tr>
    <tr>
      <th>Name</th>
      <th>Genotype</th>
      <th>Sourse</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>F3</td>
      <td>W3110 ΔfliC::FRT ΔfimA::FRT Δflu::FRT</td>
      <td>Hashimoto et al., 2016</td>
    </tr>
    <tr>
      <td>YK0080</td>
      <td>F3 intC::PLtetO1-loxP-RBS4-mcherry-cat-loxP-FRT</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>YK0083</td>
      <td>F3 intC::PLtetO1-loxP-RBS4-mcherry-cat-loxP-FRT/pYK022</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>YK0085</td>
      <td>F3 intC::PLtetO1-FRT/pYK022</td>
      <td>This study</td>
    </tr>
    <tr>
      <td colspan="3">Ribosome reporter</td>
    </tr>
    <tr>
      <td>Name</td>
      <td>Genotype</td>
      <td>Sourse</td>
    </tr>
    <tr>
      <td>MUS3</td>
      <td>BW25113 rplS-mcherry-FRT-kan-FRT</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>MUS13</td>
      <td>BW25113 rpsB-mvenus-FRT-kan-FRT</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>MUS5</td>
      <td>F3 rplS-mcherry-FRT</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>MUS6</td>
      <td>F3 rplS-mcherry-FRT rpsB-mvenus-FRT</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>YK0134</td>
      <td>MUS6 intC::PLtetO1P-loxP-RBS4-cat-loxP-FRT</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>YK0136</td>
      <td>MUS6 intC::PLtetO1-loxP-RBS4-cat-loxP-FRT/pYK022</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>YK0138</td>
      <td>MUS6 intC::PLtetO1-loxP-FRT/pYK022</td>
      <td>This study</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Plasmid list used in this study.


<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Backbone</th>
      <th>Gene</th>
      <th>Sourse</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>pKD46</td>
      <td></td>
      <td></td>
      <td>CGSC</td>
    </tr>
    <tr>
      <td>pCP20</td>
      <td></td>
      <td></td>
      <td>CGSC</td>
    </tr>
    <tr>
      <td></td>
      <td>pcDNA3.1</td>
      <td>pCMV-lox2272-loxP-inversed mvenus-lox2272-loxP</td>
      <td>Sato lab</td>
    </tr>
    <tr>
      <td></td>
      <td>pcDNA3.1</td>
      <td>pCMV-rfp-pmag-creC</td>
      <td>Sato lab</td>
    </tr>
    <tr>
      <td></td>
      <td>pcDNA3.1</td>
      <td>pCMV-rfp-nmag-creN</td>
      <td>Sato lab</td>
    </tr>
    <tr>
      <td>pTmCherryK3</td>
      <td>pMW118</td>
      <td>PLtetO1 -RBS3-mcherry-FLP-kan-FLP</td>
      <td>Wakamoto lab</td>
    </tr>
    <tr>
      <td>pLVK4</td>
      <td>pMW118</td>
      <td>PLlacO1 -RBS4-mvenus-FLP-kan-FLP</td>
      <td>Wakamoto lab</td>
    </tr>
    <tr>
      <td>pTVCK4</td>
      <td>pMW118</td>
      <td>PLtetO1 -RBS4-mvenus-cat-FLP-kan-FLP</td>
      <td>Wakamoto lab</td>
    </tr>
    <tr>
      <td>pKK1</td>
      <td>pMW118</td>
      <td>PLlacO1-rfp-pmag-creC-FLP-kan-FLP</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pKK2</td>
      <td>pMW118</td>
      <td>PLlacO1 -rfp-nmag-creN-FLP-kan-FLP</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pYK001</td>
      <td>pMW118</td>
      <td>PLlacO1-RBS3-pmag-creC-FLP-kan-FLP</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pYK002</td>
      <td>pMW118</td>
      <td>PLlacO1-RBS3-nmag-creN-FLP-kan-FLP</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pYK006</td>
      <td>pMW118</td>
      <td>PLtetO1-RBS3-lox2272-mvenus-loxP-FLP-kan-FLP</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pYK007</td>
      <td>pMW118</td>
      <td>PLtetO1-RBS3-lox2272-mcherry-loxP-FLP-kan-FLP</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pYK008</td>
      <td>pMW118</td>
      <td>PLtetO1-RBS3-lox2272-mcherry-loxP-FLP-kan-FLP</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pYK009</td>
      <td>pMW118</td>
      <td>PLtetO1-RBS3-lox2272-mcherry-loxP-FLP-kan-FLP</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pYK010</td>
      <td>pMW118</td>
      <td>PLtetO1-RBS4-lox2272-mcherry-loxP-FLP-kan-FLP</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pYK011</td>
      <td>pMW118</td>
      <td>PLtetO1-lox2272-RBS4-mcherry-loxP-FLP-kan-FLP</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pYK016</td>
      <td>pMW118</td>
      <td>PLlacO1-RBS3-pmag-creC-FLP-kan-FLP</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pYK017</td>
      <td>pMW118</td>
      <td>PLlacO1-RBS3-creN-nmag-FLP-kan-FLP</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pYK018</td>
      <td>pMW118</td>
      <td>PLlacO1-RBS3-creN-nmag-pmag-creC-FLP-kan-FLP</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pYK022</td>
      <td>pMW118</td>
      <td>PLlacO1-RBS3-creN-nmag-pmag-creC-FLP-kan-FLP</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pYK023</td>
      <td>pMW118</td>
      <td>PLtetO1-loxP-RBS4-mcherry-loxP-FLP-kan-FLP</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pYK028</td>
      <td>pMW118</td>
      <td>PLtetO1-loxP-RBS4-mcherry-loxP-FLP-kan-FLP</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pYK029</td>
      <td>pMW118</td>
      <td>PLtetO1-loxP-RBS4-mcherry-cat-loxP-FLP-kan-FLP</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pYK035</td>
      <td>pMW118</td>
      <td>PLtetO1-loxP-RBS4-cat-loxP-FLP-kan-FLP</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pMU1</td>
      <td>pMW118</td>
      <td>PLlacO1-RBS4-mcherry-FLP-kan-FLP</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pMU2</td>
      <td>pMW118</td>
      <td>PLlacO1-RBS4-mvenus-FLP-kan-FLP</td>
      <td>This study</td>
    </tr>
  </tbody>
</table>

**Table 4.**
 Primer list used in this study.


<table>
  <thead>
    <tr>
      <th colspan="3">PA-Cre plasmid construction</th>
    </tr>
    <tr>
      <th>Name</th>
      <th>Sequence</th>
      <th>Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>pLVK_pTVK_F</td>
      <td>CAGGCATCAAATAAAACGAAAGGCTCAGTC</td>
      <td rowspan="5">For constructing pKK1 and pKK2 plasmids using ExoIII cloning (Li and Evans, 1997). Templates: pLVK3 (pLVK_pTVK_F &amp; pLVK3_pTVK3_R), pCMV-rfp-pmag-creC (L3_TagRFP_F &amp; Crec_Term_R), and pCMV-rfp-nmag-creN (L3_TagRFP_F &amp; nMagCreN-R)</td>
    </tr>
    <tr>
      <td>pLVK3_pTVK3_R</td>
      <td>GGTACCTTTCTCCTCTTTAATGTTTTCGG</td>
    </tr>
    <tr>
      <td>L3_TagRFP_F</td>
      <td>GGACGCACTGACCGAAAACATTAAAGAG GAGAAAGGTACCATGGTGTCTAAGGGCGAAG</td>
    </tr>
    <tr>
      <td>Crec_Term_R</td>
      <td>CCAGTCTTTCGACTGAGCCTTTCGTTTT ATTTGATGCCTGTTAGTCCCCATCTTCGAGCAG</td>
    </tr>
    <tr>
      <td>nMagCreN-R</td>
      <td>TTCGTTTTATTTGATGCCTGTTAGTTCAGCTTGCACCAGG</td>
    </tr>
    <tr>
      <td>YKp0001</td>
      <td>ATGCATACTCTTTATGCCCCCGG</td>
      <td rowspan="2">For constructing pYK001 and pYK002 plasmids by removing the rfp gene from pKK1 and pKK2.</td>
    </tr>
    <tr>
      <td>YKp0002</td>
      <td>GGTACCTTTCTCCTCTTTAATG</td>
    </tr>
    <tr>
      <td>YKp0053</td>
      <td>AACAGGAAATGGTTCCCTGCTGAACC</td>
      <td rowspan="2">For constucting pYK016 plasmid by changing the linker between pmag and creC on pYK001.</td>
    </tr>
    <tr>
      <td>YKp0054</td>
      <td>GGTACCTTCTGTTTCGCACTGGAATC</td>
    </tr>
    <tr>
      <td>YKp0022</td>
      <td>GTGTAGGCTGGAGCTGCTTCG</td>
      <td rowspan="6">For constructing pYK017 plasmid using ExoIII cloning. PCR was conducted with the template pYK002 using YKp0022 &amp; YKp0052, YKp0049 &amp; YKp0056 and YKp0055 &amp; YKp0057 to change the order of nmag and creN.</td>
    </tr>
    <tr>
      <td>YKp0049</td>
      <td>AAGAGGAGAAAGGTACCATGACCTCTGATGAAGTCAGG</td>
    </tr>
    <tr>
      <td>YKp0052</td>
      <td>CATGGTACCTTTCTCC</td>
    </tr>
    <tr>
      <td>YKp0055</td>
      <td>CATACTCTTTATGCCCCCGGTGG</td>
    </tr>
    <tr>
      <td>YKp0056</td>
      <td>GCATAAAGAGTATGGGTACCGTTCAGCTTGCACCAG</td>
    </tr>
    <tr>
      <td>YKp0057</td>
      <td>CTCCAGCCTACACTTATTCTGTTTCGCACTGGAATC</td>
    </tr>
    <tr>
      <td>YKp0058</td>
      <td>TTATTCTGTTTCGCACTGGAATCCC</td>
      <td rowspan="3">For constructing pYK018 plasmid using ExoIII cloning. PCR was conducted on the template pYK016 with YKp0059 &amp; YKp0060 and pYK017 with YKp0022 &amp; YKp0058 to combine pmag-creC and creN-nmag.</td>
    </tr>
    <tr>
      <td>YKp0059</td>
      <td>GCGAAACAGAATAAAGGAGAAAGGTACCATGCATAC</td>
    </tr>
    <tr>
      <td>YKp0060</td>
      <td>GCTCCAGCCTACACTTAGTCCCCATCTTCGAGCAGC</td>
    </tr>
    <tr>
      <td>YKp0006</td>
      <td>CAGGCATCAAATAAAACGAAAGGCTCAGTCG</td>
      <td rowspan="2">For constructing pYK022 plasmid using ExoIII cloning. PCR was conducted on the template pYK001 with YKp0006 &amp; YKp0052 and pYK018 with YKp0049 &amp; YKp0061 to add a terminator.</td>
    </tr>
    <tr>
      <td>YKp0061</td>
      <td>TTATTTGATGCCTGTTAGTCCCCATCTTCGAGCAGC</td>
    </tr>
    <tr>
      <td colspan="2">Floxed cat plasmid construction</td>
      <td></td>
    </tr>
    <tr>
      <td>Name</td>
      <td>Sequence</td>
      <td>Usage</td>
    </tr>
    <tr>
      <td>YKp0026</td>
      <td>CGTTTTATTTGATGCCTGATAACTTCGTATAGCATAC</td>
      <td rowspan="2">For constructing pYK006 plasmid. Template: pCMV_lox2272_loxp_inverse-mvenus_lox2272_loxp.</td>
    </tr>
    <tr>
      <td>YKp0027</td>
      <td>CATTAAAGAGGAGAAAGGTACCATAACTTCGTATAGGATAC</td>
    </tr>
    <tr>
      <td>YKp0029</td>
      <td>CTTATTAGAATTCGCCGCCATGGTGAGCAAGGGCGAG</td>
      <td rowspan="4">For constructing pYK007 plasmid using ExoIII cloning. PCR was conducted on the template pTmCherryK3 with YKp0029 &amp; YKp0030 and pYK006 with YKp0031 &amp; YKp0032 to convert mvenus to mcherry.</td>
    </tr>
    <tr>
      <td>YKp0030</td>
      <td>CATTATACGAAGTTATCTCGAGTTATCCACGCGTGAGC</td>
    </tr>
    <tr>
      <td>YKp0031</td>
      <td>CTCGAGATAACTTCGTATAATG</td>
    </tr>
    <tr>
      <td>YKp0032</td>
      <td>GGCGGCGAATTCTAATAAGG</td>
    </tr>
    <tr>
      <td>YKp0035</td>
      <td>ATAACTTCGTATAAAGTATCCTATACGAAGTTATGGTACC</td>
      <td rowspan="2">For constructing pYK008 plasmid. PCR was conducted on the template pYK007 to delete spacer sequence.</td>
    </tr>
    <tr>
      <td>YKp0036</td>
      <td>ATGGTGAGCAAGGGCGAGGAGGATAACATGGCCATCATC</td>
    </tr>
    <tr>
      <td>YKp0037</td>
      <td>TAACTCGAGATAACTTCGTATAATG</td>
      <td rowspan="2">For constructing pYK009 plasmid with the template pYK008 to delete SacI and MluI restriction sites.</td>
    </tr>
    <tr>
      <td>YKp0038</td>
      <td>CTTGTACAGCTCGTCCATGC</td>
    </tr>
    <tr>
      <td>YKp0039</td>
      <td>GAAAAAAATAACTTCGTATAGGATAC</td>
      <td rowspan="2">For constructing pYK010 plasmid with the template pYK009 to change the ribosomal binding site (RBS).</td>
    </tr>
    <tr>
      <td>YKp0040</td>
      <td>CTCCTCTTTAATGTTTTCGGTCAGTGCG</td>
    </tr>
    <tr>
      <td>YKp0041</td>
      <td>GAAGTTATAGGAGGAAAAAAATGGTGAGCAAGGGCGAGGAGG</td>
      <td rowspan="2">For constructing pYK011 plasmid with the template pYK010 to transfer RBS in floxed site.</td>
    </tr>
    <tr>
      <td>YKp0042</td>
      <td>GTATAAAGTATCCTATACGAAGTTATCTTTAATGTTTTCGGTCAGTGCG</td>
    </tr>
    <tr>
      <td>YKp0069</td>
      <td>CCGAAAACATTAAAGATAACTTCGTATAGCATACATTATACG</td>
      <td>For constructing pYK023 with the template pYK011 (YKp0041 &amp; YKp0069) to change lox2272 to loxP.</td>
    </tr>
    <tr>
      <td>YKp0083</td>
      <td>ATACATTATACGAAGTTATCAGGCATCAAATAAAACG</td>
      <td rowspan="2">For constructing pYK028 plasmid with the template pYK023 to change the direction of loxP site.</td>
    </tr>
    <tr>
      <td>YKp0084</td>
      <td>GCTATACGAAGTTATCTCGAGTTACTTGTACAGCTC</td>
    </tr>
    <tr>
      <td>YKp0072</td>
      <td>CGAGCTGTACAAGGAGCTCGAGAAAAAAATCACTGG</td>
      <td rowspan="3">For constructing pYK029 plasmid using ExoIII cloning. PCR was conducted on the template pYK028 (YKp0072 YKp0089) and pTVCK4 (YKp0075 &amp; YKp0083) to insert cat gene.</td>
    </tr>
    <tr>
      <td>YKp0075</td>
      <td>CTTGTACAGCTCGTCCATGCCGCCGGTGG</td>
    </tr>
    <tr>
      <td>YKp0089</td>
      <td>CGTATAATGTATGCTATACGAAGTTATCTCGAGTTATCCAC</td>
    </tr>
    <tr>
      <td>YKp0109</td>
      <td>GAGAAAAAAATCACTGG</td>
      <td rowspan="2">For constructing pYK035 plasmid with the template pYK029 to remove mcherry gene.</td>
    </tr>
    <tr>
      <td>YKp0110</td>
      <td>CATTTTTTTCCTCCTATAAC</td>
    </tr>
    <tr>
      <td colspan="2">Genome integration by λ-Red recombination</td>
      <td></td>
    </tr>
    <tr>
      <td>Name</td>
      <td>Sequence</td>
      <td>Usage</td>
    </tr>
    <tr>
      <td>intC_PtetO1_F3</td>
      <td>AGTTGTTAAGGTCGCTCACTCCACCTTC TCATCAAGCCAGTCCGCCCATCCCTATCAGTGATAGAGATTG</td>
      <td rowspan="2">For genome integration of floxed mcherry-cat-FRT-kan-FRT or cat-FRT-kan-FRT at intC site by λ-Red recombination. PCR was conducted on the template pYK029 or pYK035.</td>
    </tr>
    <tr>
      <td>intC_R</td>
      <td>CCGTAGATTTACAGTTCGTCATGGTTCG CTTCAGATCGTTGACAGCCGCAATTCCGGGGATCCGTCGACC</td>
    </tr>
    <tr>
      <td>oMU94</td>
      <td>ACCTGCGTGAGCGTACTGGTAAGGCTGC TCGTATCAAAGAGCGTCTTAACGTGAGCAAGGGCGAGGA</td>
      <td rowspan="2">For integrating mcherry-FRT-kan-FRT fragment at rplS site. Template: pMU1.</td>
    </tr>
    <tr>
      <td>oMU107</td>
      <td>GCCAGCCAATTGGCCAGCCCTTCTTAAC AGGATGTCGCTTAAGCGAAATCTTGTGTAGGCTGGAGCTGCT</td>
    </tr>
    <tr>
      <td>oMU92</td>
      <td>GTTCTCAGGATCTGGCTTCCCAGGCGG AAGAAAGCTTCGTAGAAGCTGAGGTGAGCAAGGGCGAGGA</td>
      <td rowspan="2">For integrating mvenus-FRT-kan-FRT fragment at rpsB site. Template: pMU2.</td>
    </tr>
    <tr>
      <td>oMU108</td>
      <td>TTGCCGCCTTTCTGCAACTCGAACTATT TTGGGGGAGTTATCAAGCCTTATTGTGTAGGCTGGAGCTGCT</td>
    </tr>
    <tr>
      <td colspan="2">Primers for sequence check</td>
      <td></td>
    </tr>
    <tr>
      <td>Name</td>
      <td>Sequence</td>
      <td>Usage</td>
    </tr>
    <tr>
      <td>M13F</td>
      <td>CAGGAAACAGCTATGAC</td>
      <td rowspan="2">Sequence check for the pMW118 derivative plasmids.</td>
    </tr>
    <tr>
      <td>pM1_pVT_seq_primer1</td>
      <td>GGCACCCCAGGCTTTAC</td>
    </tr>
    <tr>
      <td>intC_check_F</td>
      <td>GATCGATACTTGCTGTGGTTGATG</td>
      <td rowspan="2">Sequence check for the intC site.</td>
    </tr>
    <tr>
      <td>intC_check_R2</td>
      <td>CCTCTTAGTTAAATGGATATAACGAGCCCC</td>
    </tr>
    <tr>
      <td>YKp0077</td>
      <td>CACCGTTGATATATCCCAATGGC</td>
      <td rowspan="2">Sequence check for the cat gene.</td>
    </tr>
    <tr>
      <td>YKp0115</td>
      <td>CACTCATCGCAGTACTGTTG</td>
    </tr>
    <tr>
      <td>oMU96</td>
      <td>TCCAGACTCACTCTCCGGTAGT</td>
      <td rowspan="2">Sequence check for the rplS site. For the BW25113 derivative strains oMU96 &amp; oMU97; For the W3110 derivative strains oMU96 &amp; oMU110</td>
    </tr>
    <tr>
      <td>oMU97</td>
      <td>ATAGCCAGTAACAAGACCGCCC</td>
    </tr>
    <tr>
      <td>oMU110</td>
      <td>GACAAATTCCACGCAGCAATCTCAC</td>
      <td></td>
    </tr>
    <tr>
      <td>oMU26</td>
      <td>AAGCAAACAACCTGGGTATTCCGGT</td>
      <td rowspan="2">Sequence check for the rpsB site</td>
    </tr>
    <tr>
      <td>oMU28</td>
      <td>CTCGCTCATCCCGGTCACTTACTGA</td>
    </tr>
  </tbody>
</table>

When constructing the resistance-gene-deleted strains (YK0085 and YK0138), YK0083 and YK0136 cells were pre-cultivated overnight in LB broth containing 50 µg/mL of ampicillin (Amp, Wako). 10 µL of overnight cultures were inoculated into 2 mL of the M9 medium containing 50 µg/mL of Amp and 0.1 mM isopropyl-β-D-thiogalactopyranoside (IPTG, Wako) in test tubes. The cell cultures were cultivated at 37 °C with shaking. After a 3-hr cultivation period for inducing the expression of PA-Cre system by IPTG, the batch cultures were illuminated by LED blue light (CCS) for 24 hr. The light intensity was adjusted to 6.8 mW, which is equivalent to the intensity in the microscopy experiments. The cell cultures were streaked on LB agar containing 100 µg/mL of Amp. The plates were incubated at 37 °C overnight. After overnight incubation, several colonies were selected. The deletion of the intended gene in these colonies was examined via PCR. The colonies with the intended gene deletion were cultured in LB medium containing 50 µg/mL of Amp at 37 °C. These cell cultures were stored at –80 °C as glycerol stocks.

The genomes of the constructed strains and plasmids were purified using the Promega Genomic DNA Purification kit and the Promega Plasmid Miniprep System, respectively, and the DNA sequence of the modified locus was amplified by Prime STAR (Takara). The sequence was examined by Sanger sequencing using a commercial service (FASMAC).

In microscopy experiments, we used M9 minimal medium, which consisted of M9 salt (Difco), 2 mM MgSO4 (Wako), 0.1 mM CaCl2 (Wako), 0.2% (w/v) glucose (Wako), and 0.2%(v/v) MEM amino acid (50 x) solution (Sigma). When necessary, antibiotics and chemicals were added at the following final concentrations unless otherwise noted: Amp 50 µg/mL, Km 20 µg/mL, chloramphenicol (Cp, Wako) 15 µg/mL, and IPTG 0.1 mM.

### Calculation of the fraction of resistance-gene-deleted cells in batch culture

YK0083 cells were pre-cultivated in LB broth containing 50 µg/mL of Amp overnight. 100 µL of the overnight culture was spun at 21,500 ×g for 1 min by a centrifuge (CT15E, himac, Hitachi) and resuspended in 1 mL of the M9 minimal medium. This culture was inoculated in 2 mL of the M9 medium containing 50 µg/mL of Amp and 0.1 mM IPTG (except for the ‘no IPTG’ condition) in test tubes covered with aluminum foil for light protection. The starting OD600 was adjusted to 0.001, and the cells were cultivated at 37 °C with shaking. After a 3-hr cultivation period for inducing the expression of the PA-Cre system by IPTG, the aluminum foil cover was removed, and the test tubes were exposed to blue light. The light intensity was adjusted to 6.8 mW. The illumination length was determined according to the experimental conditions (Figure 1—figure supplement 2B). For the conditions with an illumination duration of less than 6 hr, the test tubes were again covered with aluminum foil and incubated with shaking so that the total cultivation duration from the start of blue-light illumination was identical (6 hr) across all conditions. Under the ‘no IPTG’ condition, the test tubes were covered with the aluminum foil throughout the incubation period and were not exposed to blue light.

For calculating the fractions of resistance-gene-deleted cells, the cultures exposed to blue-light were diluted to OD600 = $1.0\times10^{-6}$, and 150 µL of the diluted cultures was spread on LB agar containing 100 µg/mL of Amp. The plates were incubated at 37 °C for 18 hr. After incubation, the number of colonies was counted under ambient light or excitation light for examining mCherry fluorescence using stereomicroscope (stereomicroscope: Olympus SZ61; LED source: NIGHTSEA SFA-GR). The fraction of resistance-gene-deleted cells was calculated as the number of non-fluorescent colonies divided by the number of total colonies (Figure 1—figure supplement 2B). To validate this classification, we conducted colony PCR and checked whether the designed deletion was introduced (Figure 1—figure supplement 2C).

We also performed the resistance-gene-deletion experiments under the Cp exposure (Figure 3—figure supplement 2A). YK0083 cells were pre-cultivated in LB broth containing 50 µg/mL of Amp overnight. 100 µL of the overnight culture was spun at 21,500 ×g for 1 min by a centrifuge and resuspended in 1 mL of the M9 minimal medium. This culture was inoculated in 2 mL of the M9 medium containing 50 µg/mL of Amp, 15 µg/mL of Cp and 0.1 mM IPTG in test tubes covered with aluminum foil for light protection. The starting OD600 was adjusted to 0.001, and the cells were cultivated at 37 °C with shaking. After a 3 hr cultivation period for inducing the expression of the PA-Cre system by IPTG, the aluminum foil cover was removed, and the test tubes were exposed to blue light for 30 min. The test tubes were again covered with aluminum foil and incubated with shaking for 2 hr. The cultures exposed to blue-light were diluted to OD600 = $1.0\times10^{-6}$, and 150 µL of the diluted cultures was spread on LB agar containing 100 µg/mL of Amp. The plates were incubated at 37 °C overnight. After incubation, we examined the fluorescence of mCherry under the excitation light. The correspondence between the loss of mCherry fluorescence and the absence of cat resistance gene was verified by colony PCR (Figure 3—figure supplement 2A).

### Sample preparation and experimental procedures for competition assay

YK0083 cells were pre-cultivated in LB broth containing 50 µg/mL of Amp overnight. 100 µL of the overnight culture was spun at 21,500 ×g for 1 min by a centrifuge and resuspended in 1 mL of the M9 minimal medium. This culture was inoculated in 2 mL of the M9 medium containing 50 µg/mL of Amp, 15 µg/mL of Cp and 0.1 mM IPTG in test tubes covered with aluminum foil for light protection. The starting OD600 was adjusted to 0.001, and the cells were cultivated at 37 °C with shaking. After a 3-hr cultivation period for inducing the expression of the PA-Cre system by IPTG, the aluminum foil cover was removed, and the test tubes were exposed to blue light for 30 min. The test tubes were again covered with aluminum foil and incubated with shaking. The cultivation length after blue light illumination was determined according to the experimental conditions (Figure 3—figure supplement 2B). After the cultivation, the cultures were diluted to OD600 = $1.0\times10^{-6}$, and 100 µL of the diluted cultures was spread on LB agar containing 100 µg/mL of Amp. The plates were incubated at 37 °C for 18 hr. After incubation, the number of colonies was counted under ambient light or excitation light for examining mCherry fluorescence using stereomicroscope. The fraction of resistance-gene-deleted cells was calculated as the number of non-fluorescent colonies divided by the number of total colonies (Figure 3—figure supplement 2B).

### Sample preparation and experimental procedures for MIC tests

Cells stored as a glycerol stock were inoculated in the LB broth (Figure 2 and Figure 5—figure supplement 1) or the M9 medium (Figure 3—figure supplement 3C) containing 50 µg/mL of Amp. The cells were cultured at 37 °C with shaking overnight. 100 µL of overnight culture was centrifuged at 21,500×g for 3 min. The supernatant was discarded, and the cells were resuspended in 1.0 mL of the M9 medium. This culture was diluted to the cell density corresponding to OD600 = 0.01 in the M9 medium containing 50 µg/mL of Amp and incubated with shaking for 3–4 hr at 37 °C. The cell culture was again diluted to OD600 = 0.001 in fresh M9 media containing different concentrations of Cp (Figure 2, Figure 3—figure supplement 3C and Figure 5—figure supplement 1). After 23 hr of incubation, the OD600 of these cultures was measured with a spectrometer (UV-1800, Shimadzu) in Figure 2 and Figure 5—figure supplement 1 or with a multi-mode microplate reader (FilterMax F5, Molecular Devices) in Figure 3—figure supplement 3C.

### Microfabrication of mother machine microfluidic device

We created two chromium photomasks, one for the main trench and the other for the observation channels, by laser drawing (DDB-201-TW, Neoark) on mask blanks (CBL4006Du-AZP, Clean Surface Technology). The photoresist on mask blanks was developed in NMD-3 (Tokyo Ohka Kogyo), and the uncovered parts of the chromium layer were removed by MPM-E30 (DNP Fine Chemicals). The remaining photoresist was removed by acetone. The photomasks were rinsed in MilliQ water and air-dried.

We created the mold for the mother machine on a silicon wafer (ID447, $ϕ$=76.2 mm, University Wafer). First, we spin-coated SU8-2 (MicroChem) on the wafer with the target height of 1.2 µm. The SU8-coated wafer was baked at 65 °C for 1 min and thereafter at 95 °C for 3 min. The SU8-layer was exposed to UV light thrice (each exposure, 22.4 mW/cm2, 1.7 sec) using a mask aligner (MA-20, Mikasa). The photomask for the observation channels was used in this step. The wafer was post-baked at 65 °C for 1 min and 95 °C for 3 min after the exposure and developed with the SU8 developer. The wafer was rinsed with isopropanol (Wako) and air-dried.

Next, we spin-coated SU8-3025 (MicroChem) with the target height of 20 µm. The pre-bake was performed at 65 °C for 3 min and thereafter at 95 °C for 7 min. The SU-8 layer was again exposed to UV light (22.4 mW/cm2, 30 s) with the photomask for the main trench. The wafer was post-baked at 65 °C for 3 min and 95 °C for 10 min and developed with the SU8 developer. The wafer was rinsed with isopropanol and air-dried.

The Part A and Part B of polydimethylsiloxane (PDMS) resin (Sylgard 184 Silicone Elastomer Kit, Dow Corning) were mixed at the ratio of 10:1 and poured onto the SU-8 mold placed in a tray made of aluminum foil. After removing the air bubbles under decreased pressure, the PDMS was cured at 65 °C for 1 hr. We cut out a PDMS block containing the channel structures and punched holes at both ends of the main trench. The PDMS block was washed with isopropanol and heated at 65 °C for 30 min.

We washed the coverslips (thickness: 0.13–0.17 mm, 24 × 60 mm, Matsunami) by sonication with 10-fold-diluted Contaminon solution (ContaminonR⃝ LS-II, Wako) for 30 min, with 99.5% ethanol (Wako) for 15 min, and with 0.8 M NaOH solution (10-fold diluted 8 M NaOH (Wako)) for 30 min. The coverslips were rinsed with milliQ water by sonication after each washing step. The coverslips were dried at 140 °C for 1 hr.

We exposed the PDMS block and the coverslips to oxygen plasma using a compact etcher (FA-1, SAMCO) and bonded them together at 65 °C for 5 min. After bonding, we inserted the silicone tubes (inner diameter: 1 mm, outer diameter: 2 mm, Tigers Polymer Corporation) into the holes and smeared a small amount of pre-cured PDMS. We cured the PDMS at 65 °C overnight to fix the tubes into the holes tightly.

### Sample preparation and experimental procedures for single-cell time-lapse experiments

Cells stored as a glycerol stock were inoculated in the LB broth containing 50 µg/mL of Amp and cultured at 37 °C overnight with shaking (200 rpm). 200 µL of overnight culture was centrifuged at 21,500×g for 3 min. The supernatant was discarded, and the cells were resuspended in 1.5 mL of the M9 medium. This culture was diluted to OD600 = 0.01 in the M9 medium containing 50 µg/mL of Amp, and incubated with shaking for 5–6 hr at 37 °C. The cell culture was again spun at 2350×g for 5 min using a centrifuge (CT6E, himac, Hitachi), and the cells were resuspended in 200 µL of the M9 medium.

Before loading the cells, the growth channels and the main trench in the mother machine device were washed by flowing 0.5 mL of 99.5% ethanol, M9 medium, and 1% (w/v) bovine serum albumin (BSA, Wako) solution sequentially using a syringe. After washing, we introduced the cell suspension into the device and let the cells enter the growth channels by placing the device at 37 °C for 1–2 hr without flow in a dark room. After confirming that the cells were trapped in many growth channels, we started flowing the M9 medium containing 0.1 mM IPTG and 0.1% (w/v) BSA at 2 mL/hr. For experiments with continuous Cp exposure, we also added 15 µg/mL or 30 µg/mL of Cp to the flowing medium from the beginning. We initiated time-lapse image acquisitions after overnight cultivation in the mother machine. We illuminated blue light for 30 min at pre-determined timings in all single-cell time-lapse experiments. The medium flow rate was maintained at 2 mL/hr and increased to 5 mL/hr for 30 min once or twice a day to prevent the formation of cell aggregates in the main trench. In Cp removal experiment, the flowing medium was switched to M9 medium containing 0.1 mM IPTG and 0.1% (w/v) BSA at 2 mL/h 72 hr after blue light exposure stopped.

### Time-lapse image acquisitions and analysis

Time-lapse image acquisitions were performed with ECLIPSE Ti fluorescent microscope (Nikon) equipped with 100× oil immersion objective lens (Plan Apo $\lambda$, NA 1.45, Nikon), digital CMOS camera (ORCA-frash, Hamamatsu Photonics), and LED light source (DC2100, Thorlabs) for fluorescence excitation. For acquiring phase-contrast images, the transmitted light was illuminated for 20 ms during mcherry-cat gene deletion experiments and for 50 ms during experiments performed with ribosome reporter strains through neutral density and red filters to avoid unintended activation of PA-Cre. Fluorescence images were acquired with appropriate filter cubes (YFP HQ (Nikon) for mVenus and Texas Red (Nikon) for mCherry). In the mcherry-cat gene deletion experiments, mCherry fluorescence was obtained every 2 min with excitation of 500 ms. The mCherry and mVenus fluorescence images were acquired every 10 min with the excitation of 100 ms in the experiments with ribosome reporter strains. IPTG was removed from the flowing media after blue-light illumination to avoid unintended gene deletion.

Blue-light illumination on the microscope for gene deletion experiments was regulated by an independent controller. We used a tape LED (7.2 mW, wave length:464∼474 nm, 60 LED/1 m, LED PARADISE) as the blue-light source and surrounded the mother machine device on the microscope stage with this tape LED. The LED light was switched on and off with a timer (REVEX).

Image analysis was performed using ImageJ Fiji (http://fiji.sc/). Image registration was performed by HyperStackReg described in MoMA Macro (Kaiser et al., 2018). Cell segmentation was semi-automated and retouched manually using iPad Pro Sidecar. Semi-automated segmentation and tracking Macro reported previously (Hashimoto et al., 2016) were used in this study. The data from image analysis were further analyzed using Python 3 (https://www.python.org/) with some general packages, including NumPy, SciPy, pandas, Matplotlib, seaborn, FastDTW, and JupyterLab.

The transitions of mCherry-CAT fluorescence intensities and elongation rates in single-cell lineages were classified using hierarchical clustering in Figure 5—figure supplement 2. The full-length single-cell lineage data were used in this analysis. The similarity of each pair of time series was measured by dynamic time warping (Salvador and Chan, 2007). Hierarchical clustering is agglomerative; the averaged dynamic time warping was used when similarity to another time series or cluster was evaluated.

### Cell sampling from the mother machine and whole-genome sequencing

After time-lapse observations performed with the mother machine, we switched the flowing media to the M9 medium containing 0.1% (w/v) BSA and no Cp. We recovered the growth of resistance-gene-deleted cell lineages by culturing them without Cp for more than 6 hr. Subsequently, we collected the media flowing out from the mother machine in a 1.5 mL tube. The OD600 of the collected cell suspension was measured with a spectrometer (UV-1800, Shimadzu). The cell suspension was diluted serially with the M9 medium to obtain a cell density corresponding to $OD_{600}=3.3\times10^{−9}$. A total of 200 µL of diluted cell suspension was taken in each well of 96-well plates. The number of cells in the 200 µL of cell suspension $k$ is expected to follow a Poisson distribution $P⁢(k)=\lambda^{k}⁢e^{-\lambda}/k!$ with the mean $\lambda$ = 0.54. Therefore, $P⁢(0)=0.58$, $P⁢(1)=0.31$, $P⁢(2)=0.085$, and $P⁢(k\geq3)=0.018$. The 96-well plates were incubated with shaking at 37 °C for two nights. We performed PCR on samples with high turbidity in wells to confirm the presence or absence of the cat gene. We selected both cat-positive and cat-negative cellular populations from the 96-well plates and cultured them in test tubes overnight at 37 °C. We stored these samples at –80 °C for further analyses.

For the measurement of mCherry-CAT fluorescence intensities of the selected samples (Figure 3—figure supplement 3), cells stored as a glycerol stock were inoculated in the M9 medium containing 50 µg/mL of Amp and cultured at 37 °C with shaking (200 rpm) overnight. 10 µL of overnight culture was inoculated in the M9 medium containing 50 µg/mL of Amp and incubated with shaking for 4 hr at 37 °C. A total of 0.3 µL of cell culture was placed on an agar pad prepared using the M9 medium and 1.5% (w/v) agar (Wako) and covered with a coverslip. Image acquisitions of the samples were performed with ECLIPSE Ti fluorescent microscope (Nikon) equipped with 100× oil immersion objective lens (Plan Apo $\lambda$, NA 1.45, Nikon), digital CCD camera (ORCA-R2, Hamamatsu Photonics), and LED light source (DC2100, Thorlabs) for fluorescence excitation. For acquiring phase-contrast images, the transmitted light was illuminated for 50 ms through neutral density. The mCherry fluorescence images were acquired with Texas Red filter cubes and an exposure time of 500 ms.

For the measurement of whole-genome sequencing of the selected samples, cells stored as a glycerol stock were inoculated in 5 mL of the M9 medium and cultured at 37 °C with shaking (200 rpm) overnight. The OD600 of overnight culture was measured with a spectrometer. Rifanpicin (Wako) was added to the overnight culture to the final concentration of 300 µg/mL. After 3 hr of incubation, the genomes of these samples were extracted with DNeasy Blood and Tissue kit (QIAGEN). TruSeq DNA PCR Free kit (Illumina) was used for the whole-genome sequencing library preparation. These libraries were sequenced using NovaSeq (Illumina). Library preparation and sequencing were outsourced to Macrogen Japan (Tokyo, Japan). The sequence data were analyzed with breseq (Deatherage and Barrick, 2014).

We evaluated the probability that all of the five cell populations for the whole-genome sequencing were derived from growth-halted cell lineages were 5.5%. This value was obtained as $(\frac{(1-0.373)\times0.693}{0.373\times0.913+(1-0.373)\times0.693})^{5}=0.055$, considering the fraction of growth-restored cell lineages among the resistance-gene-deleted cell lineages (37.3%) and the proportions of the cell lienages that recovered fast growth after Cp removal (91.3% for growth-restored cell lineages; 69.3% for growth-halted cell lineages).

### Data availability

All the data obtained in this study except for high-throughput sequencing data have been deposited to a Github repository (https://github.com/YKogane/History-Dependent-Physiological-Adaptation-2021, copy archived at swh:1:rev:ddbd24c49b29ade0f667a739c3f04b5d66e12488; Koganezawa, 2022). High-throughput sequencing data have been deposited in the NCBI Sequence Read Archive (SRA) under BioProject accession in no. PRJNA774496.

### Code availability

All the codes used for the data analysis are available from a Github repository (https://github.com/YKogane/History-Dependent-Physiological-Adaptation-2021).
