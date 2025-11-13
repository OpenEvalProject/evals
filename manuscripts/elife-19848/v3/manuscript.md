# Transcription leads to pervasive replisome instability in bacteria

## Authors

- Sarah M Mangiameli<sup>1</sup>
- Christopher N Merrikh<sup>2</sup>
- Paul A Wiggins<sup>1</sup> †
- Houra Merrikh<sup>2</sup> ([ORCID: 0000-0001-9956-9640](https://orcid.org/0000-0001-9956-9640)) †

### Affiliations

1. Department of Physics University of Washington Seattle United States
2. Department of Microbiology University of Washington Seattle United States
3. Department of Bioengineering University of Washington Seattle United States
4. Department of Genome Sciences University of Washington Seattle United States

† Corresponding author

## Abstract

The canonical model of DNA replication describes a highly-processive and largely continuous process by which the genome is duplicated. This continuous model is based upon in vitro reconstitution and in vivo ensemble experiments. Here, we characterize the replisome-complex stoichiometry and dynamics with single-molecule resolution in bacterial cells. Strikingly, the stoichiometries of the replicative helicase, DNA polymerase, and clamp loader complexes are consistent with the presence of only one active replisome in a significant fraction of cells (>40%). Furthermore, many of the observed complexes have short lifetimes (<8 min), suggesting that replisome disassembly is quite prevalent, possibly occurring several times per cell cycle. The instability of the replisome complex is conflict-induced: transcription inhibition stabilizes these complexes, restoring the second replisome in many of the cells. Our results suggest that, in contrast to the canonical model, DNA replication is a largely discontinuous process in vivo due to pervasive replication-transcription conflicts.

## Introduction

The rapid and faithful replication of the genome is essential to cell proliferation. Although the replisome, the cellular machinery responsible for DNA replication, has been extensively studied both in vitro and in vivo (O'Donnell et al., 2013), fundamental questions remain about the dynamics and stability of the replication complex in the context of the living cell, where replication is one of a number of essential cellular processes competing for the genetic material as a template. This competition results in replication conflicts, the stalling or pausing of the replication process in the face of obstacles, including transcription and tightly-bound DNA-binding proteins (Baharoglu et al., 2010; Bidnenko et al., 2006; Boubakri et al., 2010; Brewer, 1988; Dutta et al., 2011; Marsin et al., 2001; Merrikh et al., 2011, 2012; Mirkin and Mirkin, 2005, 2007; Soultanas, 2011). Genetic evidence from bacterial studies suggests these replication conflicts can routinely necessitate a replication-restart process at highly-transcribed regions and genes transcribed in the opposite orientation to replication (Merrikh et al., 2015, 2011; Million-Weaver et al., 2015a). However, whether the replisome disassembles in response to conflicts, the rapidity of the restart process, and the frequency of such events per cell cycle are unknown (Bruand et al., 2005; Gabbai and Marians, 2010; Lovett, 2005; Marsin et al., 2001; Zavitz and Marians, 1992). The current estimates for the number of replication restart events per cell cycle vary greatly, with numbers ranging from one per cell cycle to one in seven generations (Beattie and Reyes-Lamothe, 2015; Cox et al., 2000; Maisnier-Patin et al., 2001; McGlynn and Lloyd, 2002). However, estimates of less than one event per cell cycle are in conflict with the essentiality of the restart protein PriA in (Bacillus subtilis essentiality is demonstrated in rapid growth [Polard et al., 2002]), and the synthetic lethality of PriB and PriC proteins in Escherichia coli (PriA mutants as well as PriB PriC double mutants are largely unviable [Gabbai and Marians, 2010; Sandler and Marians, 2000; Sandler et al., 1999]). These observations are consistent with a more frequent requirement for replisome reactivation after conflicts (Gabbai and Marians, 2010; Polard et al., 2002; Sandler and Marians, 2000) and provide indirect evidence against the canonical model that replication is continuous in vivo.

Our previous investigations using chromatin immunoprecipitation (ChIP) of replication restart proteins determined the chromosomal locations of conflicts in very large ensembles of cells (in the population average) (Merrikh et al., 2015, 2011). However, due to population averaging over cells in various stages of the replication conflict and restart process, ChIP experiments are poor reporters of potential conflict-induced changes to the structure of the replisome complex, the frequency of conflicts in a single cell, and the rapidity of the replication restart process. Therefore understanding the fundamental character of DNA replication and conflicts necessitates a single-cell approach in which conflicts can be observed and quantitatively characterized one event at a time. The molecular-scale stoichiometry of the replisome further necessitates experiments with single-molecule sensitivity to detect any potential changes to replisome structure.

We visualized the replication process in single cells by in vivo Single-Molecule Fluorescence Microscopy (SMFM). We characterized the stoichiometry and lifetimes of the replicative helicase complexes (and other replication proteins) in growing B. subtilis and E. coli cells. These measurements revealed that a significant percentage of cells only have a single helicase complex and that many of the complexes are short-lived. These results are consistent with pervasive disassembly of replisomes. We find that transcription inhibition both increases the lifetimes and stoichiometry of several core replisome components, suggesting that endogenous replication-transcription conflicts frequently lead to disassembly of replisomes, potentially every cell cycle. The replication-conflict induced disassembly model suggests that conflicts may limit the rate of replication. Consistent with this model, we find that the inhibition of transcription, and the amelioration of conflicts, increases the replication rate as measured by thymidine incorporation assays.

## Results

### Replicative helicase and DNA polymerase stoichiometries are consistent with a single active complex in a large population of cells

To probe replisome stoichiometry in single cells with single-molecule sensitivity, we employ SMFM. In short, the discrete transitions in fluorophore intensity due to bleaching can be detected and analyzed to deduce the stoichiometry of localized fluorophores with single-molecule resolution. The quantitative characterization of the molecular stoichiometry of the replisome in living E. coli cells was recently realized by SMFM (Reyes-Lamothe et al., 2010), and this SMFM analysis has been applied in many other contexts (e.g. [Leake et al., 2006] and [Ulbrich and Isacoff, 2007]). However, SMFM has not been exploited to determine the impact of conflicts on the replisome, the continuity of the replication process, or frequency of disruptions to the replisome within living cells.

We analyzed replisome stoichiometry of the replicative helicase DnaC in B. subtilis. DnaC was chosen due to its essential role in the replication process, extensive biochemical characterization, its relatively large and well-accepted stoichiometry in the replisome, and because it is the first replisome protein reloaded onto the DNA during PriA-dependent replication restart (Bruand et al., 2001, 2005; Marsin et al., 2001). The replicative helicase is responsible for facilitating replication by unzipping the two strands of DNA ahead of the replication forks. In vitro biochemical studies, including X-ray crystallography, reveal that the helicase forms a homo-hexameric ring encircling the lagging strand of the DNA template (Bailey et al., 2007; Fass et al., 1999; Kaplan et al., 2013). In vivo measurements of stoichiometry in E. coli further support this model in the context of the living cell (Reyes-Lamothe et al., 2010). For our studies, we used a DnaC-GFP fusion (Figure 1—figure supplement 1), which was expressed from its endogenous promoter, at its endogenous locus. The fusion protein localized to midcell in a replication-dependent manner, consistent with association with the replisome (Lemon and Grossman, 1998). Under our experimental conditions (minimal arabinose medium), the growth rate (and the replication rate—see below) of the DnaC-GFP strain was indistinguishable from that in wild-type cells (During rapid growth in Luria-Bertani medium, DnaC-GFP strain has a minor growth defect [Figure 1—figure supplement 1A and B]).

To measure the in vivo stoichiometry of the replisome proteins, we performed SMFM bleaching analysis (Figure 1A and B, and, Figure 1—figure supplements 2 and 3). Most bacteria have a circular chromosome and a single origin of replication. After initiation, DNA replication progresses bi-directionally around the chromosome, with two active replisomes in each cell. The two forks in B. subtilis often localize to a single replication factory (Lemon and Grossman, 1998) (Figure 1A). The small fraction of cells (~16%) having focus localization inconsistent with a replication factory were excluded from analysis. It is expected that in cells where the replication forks are co-localized, two replicative helicase complexes, and therefore 12 molecules of DnaC, will be localized to the factory (Figure 1C). However, stoichiometry analysis of DnaC at the replication factory in cells undergoing active replication reveals that just under half the cells (41%) have a factory with only 6 DnaC proteins, corresponding to a single helicase complex (Figure 1D and E). The rest of the population (59%) has 12 DnaC proteins, corresponding to two active helicases. Note that incomplete protein labeling cannot account for the low helicase stoichiometry since two sub-populations with an integer multiple of fundamental hexameric stoichiometry are observed, as has also been previously reported in E. coli (Reyes-Lamothe et al., 2010). Western-blot analyses further confirm that >98% of DnaC protein in the cell is indeed labeled with GFP (Figure 1—figure supplement 4). The incorrect determination of the bleaching step size also cannot account for these observations since results can be reproduced by using an in vitro measure of the fluorophore step size (Figure 1—figure supplement 5). These results are consistent with a model where elongating replisomes are frequently disrupted and disassembled.

![Figure 1.](https://cdn.elifesciences.org/articles/19848/elife-19848-fig1-v3.jpg)

**Figure 1.:** (A) Photobleaching of DnaC-GFP in a replication factory. (B) A typical intensity trace (blue) is shown for a DnaC-GFP focus. Stepwise transitions are observed as the fluorescent protein bleaches. The intensity is filtered using Change-Point analysis (red) which determines the intensity step-size corresponding to the bleaching of single fluorophores (complete stoichiometry calculation is demonstrated in Figure 1—figure supplements 2 and 3, and detailed in the materials and methods section). The image mosaic above shows the time-averaged image of the focus over each intensity level. (C) A schematic of the replication factory consisting of either one or two assembled replisomes (black dots) in a diffraction-limited spot (green). (D) Histogram of estimated factory DnaC-GFP stoichiometry in B. subtilis. Error bars represent counting error. The observed distribution is well fit by a two Gaussian model (solid blue), representing a mixed population of single-helicase (6 DnaC molecules) and two-helicase (12 DnaC molecules) factories. (Analysis for N = 213 factories.) (E) Relative abundance of factories with one and two helicases. (F) Estimated stoichiometry distribution for PolC-YPet in B. subtilis shows two populations (N = 125). Peak stoichiometries for each population (dashed blue) were determined by maximum likelihood fitting with a two Gaussian model (solid blue) to be 2 and 4 copies. (Note: the distribution included a small fraction (~5%) of factories with stoichiometries greater than 10 copies which were removed for the purpose of fitting.) (G) Relative abundance of factories with 2 and 4 copies of PolC-GFP.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/19848/elife-19848-fig1-figsupp1-v3.jpg)

**Figure 1—figure supplement 1.:** For growth curves, the optical density of wild type and dnaC-gfp strains growing in minimal arabinose medium at 30°C were monitored for 5 hr. Linear regression to OD600 readings were used to determine doubling time. (A) The dnaC-gfp allele does not confer a detectable growth defect in minimal medium. OD600 readings for a representative culture of wild type and dnaC-gfp cells. (B) Calculated doubling times and OD600 readings show a small growth defect for the dnaC-gfp strain relative to wild type in LB medium.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/19848/elife-19848-fig1-figsupp2-v3.jpg)

**Figure 1—figure supplement 2.:** (A) The phase-contrast image of the cells was segmented to identify the cell boundaries (orange) surrounding each cell mask (black). (B) The integrated raw focus intensity (blue) and scaled background intensity (green) are plotted for a bleaching experiment. The intensity trace is computed by subtracting the background from the raw intensity. (C) The summed image is shown in yellow. The outline of the cell mask is shown in blue. The intensity regions (red outline) are determined by watersheding the summed intensity to divide the image into local maxima. The focus positions (points) are determined by fitting a Gaussian distribution in the intensity regions. (D) The raw focus intensity is determined by summing the intensity in a mask centered on the locus position. The background is computed by calculating the average intensity inside the cell (blue outline) but outside the intensity region (red).

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/19848/elife-19848-fig1-figsupp3-v3.jpg)

**Figure 1—figure supplement 3.:** (A) Intensity tracking of a DnaC-GFP focus in B. subtilis. A decaying exponential (solid blue) is fit to the background subtracted raw intensities (blue points) traced over a series of 120 fluorescence images. The value of the exponential fit in the first frame is taken as the initial intensity of the DnaC-GFP complex (see methods). (B) The raw intensities (solid blue) are filtered (mean value in red) to reveal stepwise transitions. Summed fluorescence images of the DnaC-GFP complex are shown corresponding to each level detected by the filter in the image strip above the plot area. (C) The PPDD of the filtered intensities (red) reveals peaks at integral multiples of the unitary intensity step that would not be detectable in PPDD of the raw intensities (blue). (D) The power spectrum is used to identify the location of the first order peak in the PPDD which corresponds to the highest peak in the power spectrum (dashed gray). The unitary intensity step determined by the power spectrum corresponds to the spacing of the dashed gray lines in panels B and C.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/19848/elife-19848-fig1-figsupp4-v3.jpg)

**Figure 1—figure supplement 4.:** Cells produce complete DnaC-GFP fusion protein. Western blot analysis indicates that DnaC-GFP is fully synthesized, and that potentially truncated DnaC proteins lacking GFP are not detected. Individual lanes were normalized by total protein, and separate western blots were probed with either (A) anti-DnaC polyclonal antibodies or (B) anti-GFP polyclonal antibodies.

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/19848/elife-19848-fig1-figsupp5-v3.jpg)

**Figure 1—figure supplement 5.:** (A) Bleaching traces for two different surface immobilized GFP proteins. Inserts show the mean fluorescence images in the bleached and unbleached states. (B) Maximum likelihood fits to unitary intensity step distributions for isolated GFP in vitro. (C) Example in vivo unitary step distribution for DnaC-GFP in B. subtilis and its maximum likelihood fit. For all experimental conditions in B. subtilis, unitary step distributions were peaked within 19% found in vitro value.

![Figure 1—figure supplement 6.](https://cdn.elifesciences.org/articles/19848/elife-19848-fig1-figsupp6-v3.jpg)

**Figure 1—figure supplement 6.:** For growth curves, the optical density of wild type and polC-YPET strains growing in minimal arabinose medium at 30°C were monitored for 5 hr. Linear regression to OD600 readings were used to determine doubling time. (A–B) No growth defect is observed for polC-ypet in either minimal or LB growth medium.

Additionally, we analyzed the stoichiometry of PolC-YPet, a fluorescent fusion to the leading strand polymerase in B. subtilis. Even in rapid growth, the PolC-YPet fusion confers no growth defect relative to wild type cells (Figure 1—figure supplement 6). We again find that the stoichiometry distribution for co-localized replication forks consists of two sub-populations, with the second (~4 copies) centered at roughly twice the stoichiometry of the first (~2 copies) (Figure 1F). Importantly, these sub-populations were similarly proportioned to those observed for DnaC, with roughly 47% of factories having stoichiometries consistent with localization of PolC to only a single replication fork (Figure 1G). This implied disassembly of the DNA polymerase, in addition to the replicative helicase, further suggests that the replisome is frequently disrupted.

### Replicative helicase complexes are short-lived

To test the frequent-disruption model, we measured the lifetimes (replisome dynamics) of replicative helicase complexes. This model predicts that any given replisome complex is shorter lived than the time required to traverse each arm of the chromosome. We visualized the helicase complexes over twenty-two minutes to estimate their lifetimes. In the replisome dynamics measurements, cells were imaged at two-minute intervals such that the helicase complexes can be tracked (Figure 2A, left image strip; Figure 2—figure supplement 1) over the twenty-two minute time frame without significant bleaching (Figure 2—figure supplement 2). Disassembly events correspond to the cooperative loss of all fluorophores simultaneously. Although photobleaching affects our measurement only minimally over the course of the experiment, it would not be possible to visualize the replisome at this frame rate for the entire cell cycle (Figure 2—figure supplement 2). Using the complex lifetimes observed during these short time courses, we estimate the disassembly rate, predicting that roughly five disassembly events occur during each cell cycle.

![Figure 2.](https://cdn.elifesciences.org/articles/19848/elife-19848-fig2-v3.jpg)

**Figure 2.:** (A) Typical frame mosaics for dynamics of the helicase in three conditions: Untreated (WT), rifampicin-treated (Rif) and rpoB* cells (see also Figure 2—figure supplement 1). (In this context, WT refers to cells carrying the dnaC-gfp allele but not the rpoB* allele.) The helicase complexes in WT cells were observed to be intermittent: assembling and disassembling on the timescale of minutes. The helicase complexes in rifampicin-treated and rpoB* cells were observed to be more persistent. The complexes were tracked by an automated algorithm (red, detailed description in material and methods). (B) Distribution of helicase complex lifetime in WT (gray, N = 327 complexes), rifampicin-treated (blue, N = 183 complexes) and rpoB* (red, N = 165 complexes) cells. Data collection is limited to 22 min. (C) Probability of helicase survival as a function of helicase complex lifetime. Solid lines represent the empirical survival curves. Dashed lines show fits determined by maximum likelihood estimation. (D) Estimated number of disassembly events per 40 min of replication using the Poisson process model (see also Table 1). Error bars were generated by simulating 100,000 distributions with the same rate parameter and number of complexes as the observed distribution. Simulated distributions were then fit, and the width of the rate parameter distribution was used to quantify the error.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/19848/elife-19848-fig2-figsupp1-v3.jpg)

**Figure 2—figure supplement 1.:** Under normal growth conditions, a typical trajectory resulting from dynamics analysis shows rapid appearance and disappearance of DnaC-GFP foci. Both rifampicin treatment and a rpoB* mutation results in longer-lived foci. Image strips to the left show raw images with dashed red lines indicating automatically detected trajectories. Corresponding filtered images to the right additionally show focus scores for all automatically detected foci. Scores printed in red indicate that the focus is included in a trajectory. Low scoring foci not selected for a trajectory are indicated in white. A detailed description of scoring and automated focus tracking is included in the materials and methods section.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/19848/elife-19848-fig2-figsupp2-v3.jpg)

**Figure 2—figure supplement 2.:** (A) To isolate the effects of photobleaching, cells are imaged with the same intensity and exposure as in the dynamics measurement, but with no delay between frames. Red line indicates equivalent of the 12 frame time course used in the dynamics measurement for B. subtilis. (B) Automated tracking used for the dynamics measurement was applied to the bleaching data. Survival curve (blue) shows the fraction of (N = 132) complexes that were successfully tracked through a given number of frames. Survival curve for dynamics experiment (gray) is shown for comparison. (C) 92% of complexes were traceable for 12 frames. In contrast, only 9% of complexes survive the duration of the dynamics experiment.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/19848/elife-19848-fig2-figsupp3-v3.jpg)

**Figure 2—figure supplement 3.:** (A) Survival assays show that the depletion of PriA is lethal on LB medium, but the control strains (which contain either the sgRNA-priA or dcas9) survive under both conditions. We find the same result using minimal arabinose medium. (B) Sample snapshots showing the full PriA CRISPR strain, and the control (no sgRNA), both after induction with 1% xylose for approximately two hours. (C) Disruption of PriA results in a decrease in the number of cells with DnaC-GFP foci from 43% in the control strain (N = 518 cells) to 13% in the CRISPR strain (N = 413 cells). Error bars represent counting error.

We found that the majority of foci are short lived with a mean lifetime of roughly 8 min. The observed distribution of lifetimes (Figure 2B; Figure 2—source data 1) appears roughly exponential, suggesting that the occurrence of disassembly events in individual cells may be approximated as a Poisson process, providing a method for roughly estimating the number disassembly events per cell cycle. (For simplicity, we will ignore the distinction between focus loss and fork disassembly. We present a more complicated model, that treats the number of forks per focus explicitly (Supplementary file 1), but this model depends on a number of untested assumptions.) Figure 2C shows the model (dashed gray) and empirical (solid gray) survival curves for the helicase complex as a function of lifetime, where the model survival curve was fit using by maximum likelihood estimation. Multiplying the calculated rate of conflicts by the accepted 40 min long replication cycle predicts five conflicts per cell cycle (Figure 2D). It is important to note that this estimate has significant systematic uncertainty since it depends on the length of the replication cycle (which depends on growth conditions (Helmstetter and Cooper, 1968) as well as the assumption made in the modeling (see Supplementary file 1). A summary of the calculated parameters for the dynamics experiment is included in Table 1. Disassembly of the replisome on the time scale of single replication cycle is consistent with the instability inferred from the analysis of the estimated factory stoichiometry. Furthermore, the inferred frequency of disassembly events is significantly higher than expected from the continuous replication model.

**Table 1.**
 Parameters used in B. subtilis complex lifetime calculation. The parameters summarized above are defined as follows: T is the duration of the experiment, $N_{\tau<T}$ is the number of complexes interpreted to disassemble before the end of the experiment, $N_{\tau\geqT}$ is the number of complexes surviving the length of the experiment, $\tau_{min}$ is the minimum observable complex lifetime, $\tau¯$ is the empirical mean of the $N_{\tau<T}$ observable lifetimes, $k^$ is the calculated disassembly rate, $\tau¯_{calc}$ is the calculated mean lifetime (i.e. $1/k^$), and $N_{c}$ is the calculated number of conflicts per 40 min of replication.


<table>
  <thead>
    <tr>
      <th></th>
      <th>T (min)</th>
      <th>Nτ&lt;T</th>
      <th>Nτ≥T</th>
      <th>τmin (min)</th>
      <th>τ¯ (min)</th>
      <th>k^ (min-1)</th>
      <th>τ¯calc (min)</th>
      <th>Nc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Wild-Type</td>
      <td>22</td>
      <td>296</td>
      <td>31</td>
      <td>4</td>
      <td>10.4</td>
      <td>0.12</td>
      <td>8.3</td>
      <td>4.8</td>
    </tr>
    <tr>
      <td>Rif-Treated</td>
      <td>22</td>
      <td>86</td>
      <td>97</td>
      <td>4</td>
      <td>12.9</td>
      <td>0.03</td>
      <td>29.2</td>
      <td>1.4</td>
    </tr>
    <tr>
      <td>rpoB*</td>
      <td>22</td>
      <td>93</td>
      <td>72</td>
      <td>4</td>
      <td>12.5</td>
      <td>0.04</td>
      <td>22.4</td>
      <td>1.8</td>
    </tr>
  </tbody>
</table>

The frequent disassembly model further predicts that disrupting the restart protein PriA would prevent replisome reassembly, leaving disassembled replisomes in the majority of cells during a single cell cycle. To test this, we depleted PriA using CRISPR interference and visualized the number of cells with DnaC-GFP foci using snapshot imaging. Consistent with the frequent disassembly hypothesis, after inducing PriA depletion in liquid culture for roughly one doubling time, only 13% of cells had foci compared with the roughly 43% of cells with foci in the precursor strain to the PriA CRISPR, which lacks the sgRNA (Figure 2—figure supplement 3).

### Transcription inhibition increases the lifetimes of DnaC complexes

The results described support a model in which replication is discontinuous, with pervasive replisome disassembly and assembly dynamics. Our lab and others have shown that transcription, especially at the highly-transcribed rDNA or head-on genes (those transcribed in the opposite orientation relative to replication), results in potentially severe replication-transcription conflicts (De Septenville et al., 2012; Merrikh et al., 2011; Million-Weaver et al., 2015b; Wang et al., 2007a). Our previous work measuring chromosomal regions where replication conflicts were most prevalent suggested that transcription is the main obstacle to replication (Merrikh et al., 2011). Therefore, if transcription-induced conflicts were the principal mechanism responsible for replisome disassembly, we would predict that inhibition of transcription would result in a significant increase in replisome stability, either as assayed by stoichiometry or direct characterization of complex stability. To test this hypothesis, we perturbed transcription by (i) the treatment of cells with rifampicin (Rif), an antibiotic that directly inhibits transcription initiation (Sensi, 1969, 1983) and (ii) rpoB* mutants which destabilize RNA Polymerase - DNA association and/or rDNA expression (Bartlett et al., 1998; Maughan et al., 2004; Zhou and Jin, 1998). It has been previously shown that rpoB* mutations reduce severity of conflicts significantly (Baharoglu et al., 2010; Boubakri et al., 2010; Guy et al., 2009). Here, we observed that rifampicin treatment dramatically increases the lifetime of helicase complexes. For instance, the number of complexes that persisted longer than 20 min increased from 9% in untreated cells to 53% in rifampicin treated cells and the calculated number of conflicts per cell cycle decreased by a factor of four (Figure 2D; Table 1). We also isolated and examined an rpoB* mutant strain and found results consistent with those obtained from rifampicin-treated cells (Figure 2). This second transcription perturbation ensures that the observed increase in replisome stability is not an artifact of rifampicin treatment. In general, the increased stability of the helicase complex is consistent with the increased stability of the replisome.

### More cells have helicase and DNA polymerase stoichiometries consistent with two active replisome complexes upon transcription inhibition

To provide additional support for the transcription-dependence of the observed instability, we measured the stoichiometry of the helicase complexes in cells post transcription inhibition. An increase in replisome stability would predict an increase in the ratio of cells with two helicase complexes (12 DnaC molecules) relative to the number of cells with one helicase complex (6 DnaC molecules). Figure 3A shows the distribution of protein stoichiometry at the factory in cells with transcription inhibited by rifampicin. The data are clearly consistent with the majority of cells having two active replisomes. There was a significant increase in the percentage of cells containing two stable helicase complexes relative to cells containing one helicase complex in the rpoB* mutant backgrounds as well (Figure 3A and D, Table 2). A similar shift towards the higher order stoichiometry is observed for PolC after transcription inhibition by rifampicin (Figure 3B and D). Increased stability of the polymerase was also observed in the rpoB* mutant background. These results strongly support the model that the frequent dissociation of the replicative helicase complex during each cell cycle results from replication-transcription conflicts.

![Figure 3.](https://cdn.elifesciences.org/articles/19848/elife-19848-fig3-v3.jpg)

**Figure 3.:** (A) Helicase complex stoichiometry under three conditions: Untreated (WT), rifampicin-treated (Rif) and rpoB* cells. Probability densities are represented as Kernel Density Estimates (KDEs). In contrast to WT (gray), in both rifampicin-treated (blue) and rpoB* (red) cells, a significant fraction of single-helicase complexes (6 DnaC molecules) are lost with all observations being consistent with two-helicase complexes (12 DnaC molecules). (N = 70–117) (B) Estimated PolC stoichiometry in untreated (gray), rifampicin-treated (blue), and rpoB* (red) cells (N = 81–125). The low stoichiometry peak is no longer resolvable after rifampicin treatment or in the rpoB* mutant background, implying increased stability of the polymerase. (Note: rifampicin treatment also increased the exceedingly high fluorescence population which was again removed for the purpose of fitting.) (C) The relative abundance of helicase complex stoichiometries in cells with an ectopic inducible head-on replication-transcription conflict (lacZ). An IPTG (induction)-dependent increase in the single-helicase stoichiometry was observed, consistent with the reduction in factory stoichiometry being conflict-induced. (N = 108–174) (D) Summary of stoichiometry for transcription-inhibition and ectopic-conflict experiments. Estimates for the relative abundance of first and second order stoichiometry sub-populations are determined by fitting the distributions of estimated stoichiometries (Figure 3—figure supplement 1, Table 2).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/19848/elife-19848-fig3-figsupp1-v3.jpg)

**Figure 3—figure supplement 1.:** (A) The observed stoichiometry of DnaC-GFP was not significantly altered by the addition of IPTG. Compare to Figure 1D. (B) Addition of lacZ (transcription on) in the co-directional orientation causes a small decrease to replisome stability.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/19848/elife-19848-fig3-figsupp2-v3.jpg)

**Figure 3—figure supplement 2.:** The most likely two Gaussian model is selected varying the Gaussian means, widths and peak intensities. Maximum likelihood models (blue) and comprising Gaussians (dashed blue) are shown over histogram distributions. Error bars represent counting error. Calculated maximum likelihood fit parameters are summarized in Table 2.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/19848/elife-19848-fig3-figsupp3-v3.jpg)

**Figure 3—figure supplement 3.:** Amelioration of conflicts both by rifampicin or an rpoB* mutant increases the stability of the replisome. Conversely, addition of a highly transcribed gene in the head-on orientation decreases replisome stability.

**Table 2.**
 Maximum likelihood fit parameters for B. subtilis count distributions.


<table>
  <thead>
    <tr>
      <th></th>
      <th>N</th>
      <th>μ1 , μ2 (copies)</th>
      <th>FL (error)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>DnaC-GFP</td>
      <td>213</td>
      <td>6.2,11.2</td>
      <td>41 (9.1)%</td>
    </tr>
    <tr>
      <td>DnaC-GFP + Rif</td>
      <td>69</td>
      <td>N/A, 12.1</td>
      <td>0 (14)%</td>
    </tr>
    <tr>
      <td>DnaC-GFP rpoB*</td>
      <td>60</td>
      <td>N/A,11.1</td>
      <td>0 (10.0)%</td>
    </tr>
    <tr>
      <td>DnaC GFP lacZ off</td>
      <td>108</td>
      <td>5.6,11.5</td>
      <td>65 (5.6)%</td>
    </tr>
    <tr>
      <td>DnaC GFP lacZ on</td>
      <td>174</td>
      <td>6.0, 10.9</td>
      <td>88 (3.2)%</td>
    </tr>
    <tr>
      <td>DnaC-GFP CD lacZ</td>
      <td>185</td>
      <td>5.8, 10.2</td>
      <td>59 (9)%</td>
    </tr>
    <tr>
      <td>DnaC-GFP + IPTG</td>
      <td>261</td>
      <td>6.3,11.2</td>
      <td>54 (11)%</td>
    </tr>
    <tr>
      <td>PolC-YPet</td>
      <td>125</td>
      <td>2.2,4.9</td>
      <td>47 (13)%</td>
    </tr>
    <tr>
      <td>PolC-YPet +Rif</td>
      <td>117</td>
      <td>N/A, 4.4</td>
      <td>0 (14)%</td>
    </tr>
    <tr>
      <td>PolC-YPet rpoB*</td>
      <td>81</td>
      <td>N/A, 4.7</td>
      <td>0 (9%)</td>
    </tr>
  </tbody>
</table>

### A severe head-on conflict disassembles helicase complexes

Our data imply that replication-transcription conflicts increase the instability of replisome complexes. To test this model, we introduced an IPTG inducible lacZ gene (Pspank(hy)-lacZ) onto the chromosome in the head-on orientation (strain lacZ). We hypothesized that the induction of this ectopic conflict would further destabilize the replisome, leading to a reduction in the fraction of cells containing two intact helicase complexes relative to the control cells. As predicted, analysis of the single-molecule stoichiometry of DnaC in cells experiencing the additional severe engineered conflict (after addition of IPTG to induce lacZ expression) decreases the number of cells containing two intact helicase complexes (Figure 3C and D; >80% of cells contain only 6 rather than 12 molecules of DnaC in the factory), demonstrating that replication-transcription conflicts indeed lead to the disassembly of the replicative helicase complexes. We note that insertion of the lacZ gene in the co-directional orientation leads to a small, but detectable decrease in the number of cells with two assembled helicase complexes under induced conditions (Figure 3—figure supplement 1). This is consistent with previous reports from our lab showing that highly-transcribed co-directional genes can lead to conflicts as assayed by ChIP-qPCR experiments (Merrikh et al., 2015). Control experiments showed that the addition of IPTG to cells without the lacZ construct did not cause a significant shift in the stoichiometry distribution (Figure 3—figure supplement 1). These results (summarized in Figure 3D, see also Figure 3—figure supplement 2) altogether reveal that the inferred instability and disassembly of the helicase complexes, and potentially the replisome, is transcription-dependent. This is illustrated schematically in Figure 3—figure supplement 3.

### E. coli replisome stoichiometry and dynamics corroborate transcription-dependent instability

Given the universality of conflicts, we hypothesized that other bacteria, outside of B. subtilis, should experience this phenomenon. We therefore investigated the stoichiometry and lifetimes of three different replisome proteins in a second bacterial model organism, E. coli. The replisome localization patterns are similar in E. coli and B. subtilis, where both replication forks typically co-localize to a single diffraction limited focus (Koppes et al., 1999; Lau et al., 2003; Mangiameli et al., 2017).

We measured stoichiometries of three different E. coli replication proteins in the replisome complexes: the replicative helicase (DnaB), clamp loader (DnaX), and DNA polymerase (DnaE), both before and after transcription inhibition with rifampicin. For the E. coli experiments, the fluorescent fusions were constructed with distinct linkers to the fluorescent protein (YPet) (Reyes-Lamothe et al., 2010). As observed previously, there are 6, 3, and 3 molecules of DnaB, DnaX, and DnaE respectively in a significant proportion of the localized replisome foci in growing cells, corresponding to single a replisome complex (Figure 4). However, as predicted, rifampicin treatment results in the low stoichiometry population shifting towards the higher stoichiometry peak in the majority of these replisome foci (Figure 4D; Table 3; Figure 4—figure supplement 1). This suggests that there are indeed two co-localized replication forks in the observed foci in E. coli, but that one replisome is often at least partially dissociated from the DNA due to replication-transcription conflicts.

![Figure 4.](https://cdn.elifesciences.org/articles/19848/elife-19848-fig4-v3.jpg)

**Figure 4.:** Stoichiometry distributions are represented using kernel density estimation (N = 53–178 factories). (A) Estimated DnaB stoichiometry suggests that two hexameric helicases are present in most replication factories in the absence of transcription (blue). However, under normal conditions (gray) roughly half of factories consist of only a single helicase. (B) Transcription-inhibition increases the number of factories having higher DnaX stoichiometry. (C) Transcription-inhibition increases the number of factories having higher DnaE stoichiometry. (D) Estimates for the relative abundance of first and second order stoichiometry sub-populations are determined by fitting the distributions of estimated stoichiometries (Figure 4—figure supplement 1 and Table 3).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/19848/elife-19848-fig4-figsupp1-v3.jpg)

**Figure 4—figure supplement 1.:** The most likely two Gaussian model is selected varying the Gaussian means, widths and peak intensities. Maximum likelihood models (blue) and comprising Gaussians (dashed blue) are shown over histogram distributions. Error bars represent counting error. Error bars represent counting error. Calculated maximum likelihood fit parameters are summarized in Table 3.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/19848/elife-19848-fig4-figsupp2-v3.jpg)

**Figure 4—figure supplement 2.:** (A) Bleaching traces for two different surface immobilized YPet proteins. Inserts show the mean fluorescence images in the bleached and unbleached states. (B) Maximum likelihood fits to unitary intensity step distributions for isolated YPet in vitro. (C) Example in vivo unitary step distribution for DnaB-YPet in E. coli and its maximum likelihood fit. For all experimental conditions in E. coli, unitary step distributions were peaked within 18% found in vitro value.

**Table 3.**
 Maximum likelihood fit parameters for E. coli count distributions.


<table>
  <thead>
    <tr>
      <th></th>
      <th>N</th>
      <th>μ1 , μ2 (copies)</th>
      <th>FL (error)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>DnaB-YPet</td>
      <td>146</td>
      <td>6.6, 11.6</td>
      <td>59 (15)%</td>
    </tr>
    <tr>
      <td>DnaB-YPet + Rif</td>
      <td>53</td>
      <td>N/A, 12.1</td>
      <td>0 (13)%</td>
    </tr>
    <tr>
      <td>DnaX-YPet</td>
      <td>125</td>
      <td>2.8, 5.8</td>
      <td>53 (13)%</td>
    </tr>
    <tr>
      <td>DnaX-YPet + Rif</td>
      <td>154</td>
      <td>2.8, 5.7</td>
      <td>10.6 (17)%</td>
    </tr>
    <tr>
      <td>DnaE-YPet</td>
      <td>178</td>
      <td>2.8, 5.8</td>
      <td>46 (15)%</td>
    </tr>
    <tr>
      <td>DnaE-YPet + Rif</td>
      <td>144</td>
      <td>2.8, 5.6</td>
      <td>9.8 (9.3)%</td>
    </tr>
  </tbody>
</table>

Our replisome-stoichiometry measurements in E. coli predict that there is pervasive disassembly of replisomes in this species as well and therefore these protein complexes should also have short lifetimes. Because there are only 3 molecules of DnaE or DnaX, lifetimes of the localization of these components to the replisome foci cannot be reliably measured due to bleaching of a significant fraction of the fluorophores. However, because of the higher number of DnaB molecules in each complex, the helicase lifetimes can be measured over a twenty-minute time series without bleaching significantly affecting the results (Figure 5—figure supplement 1). The E. coli helicase complex lifetime measurements show that the majority of DnaB complexes are indeed short lived with a mean lifetime of about 9 min (Figure 5; Figure 5—source data 1). Furthermore, treatment with rifampicin extends the lifetime of these complexes, increasing the number of complexes that persist for 20 min (or longer) from 21% to 46% and the predicted number of conflicts per (40 min) replication cycle decreases from roughly 4 to 2 (Figure 5D; Table 4).

![Figure 5.](https://cdn.elifesciences.org/articles/19848/elife-19848-fig5-v3.jpg)

**Figure 5.:** Helicase complex dynamics in E. coli captured by time-lapse imaging. (A) Typical frame mosaics for dynamics of the helicase in two conditions: Untreated (WT), rifampicin-treated (Rif). The helicase complexes in WT cells were observed to be intermittent: assembling and disassembling on the timescale of minutes. The helicase complexes in rifampicin-treated cells were observed to be more persistent. The complexes were tracked by an automated algorithm (red). (B) Distribution of helicase complex lifetime in WT (gray, N = 217 complexes), rifampicin-treated (blue, N = 77 complexes). Data collection is limited to 20 min. (C) Probability of helicase survival as a function of helicase complex lifetime. Solid lines represent the empirical survival curves. Dashed lines show fits determined by maximum likelihood estimation. (D) Estimated number of disassembly events per cell cycle using the Poisson process model (see also Table 4). Simulating 100,000 distributions with the same rate parameter and number of complexes as the observed distribution generated error bars. Simulated distributions were then fit, and the width of the rate parameter distribution was used to quantify the error.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/19848/elife-19848-fig5-figsupp1-v3.jpg)

**Figure 5—figure supplement 1.:** (A) To isolate the effects of photobleaching, cells are imaged with the same intensity and exposure as in the dynamics measurement, but with no delay between frames. Red line indicates equivalent of the 11 frame time course used in the dynamics measurement. (B) Automated tracking used for the dynamics measurement was applied to the bleaching data. Survival curve (blue) shows the fraction of complexes that were successfully tracked through a given number of frames (N = 214). Survival curve for the dynamics experiment (gray) is shown for comparison (C) 86% of complexes were traceable for 11 frames. In the dynamics measurement, only 21% of complexes survive the duration of the experiment.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/19848/elife-19848-fig5-figsupp2-v3.jpg)

**Figure 5—figure supplement 2.:** (A) DnaB-YPet imaged at 2 min intervals in strains with and without the dnaC2 allele at 37°C (non-permissive for the temperature sensitive strain). In the temperature sensitive strain, either a complex is observed in the first frame (e. g. cells 1–3) or the cell generally does not develop complexes during the time course (e. g. cell 4). When a complex is observed, it most commonly disappears before the end of the time course. Once disappearance has occurred (red arrows), no new stable complexes are observed in the majority of cells (85%). In contrast, the wild type strain (e. g. cells 5–6) shows intermittent foci (as observed in the dynamics experiments at 30°C), and complexes may be assembled later in the time series. (B) Probability of observing a focus as a function of time in cells where at least one trajectory is observed. DnaC is involved both in initiation of replication at the origin and the rescue of stalled forks. The theoretical ‘Null hypothesis’ curve (red) assumes a continuous 40 min replication cycle imaged for a random 20 min window. However, the probability of observing a focus in the dnaC2 allele (blue, N = 72) decreases more quickly suggesting that the helicase is disassembled prior to completion of replication. Additionally, in the wild type strain, the probability of observing a focus is roughly independent of time, indicating that both disassembly and re-assembly events are present.

**Table 4.**
 Parameters used in E. coli complex lifetime calculation. The parameters summarized above are defined as follows: T is the duration of the experiment, $N_{\tau<T}$ is the number of complexes interpreted to disassemble before the end of the experiment, $N_{\tau\geqT}$ is the number of complexes surviving the length of the experiment, $\tau_{min}$ is the minimum observable complex lifetime, $\tau¯$ is the empirical mean of the $N_{\tau<T}$ observable lifetimes, $k^$ is the calculated disassembly rate, $\tau¯_{calc}$ is the calculated mean lifetime (i.e. $1/k^$), and $N_{c}$ is the calculated number of conflicts per 40 min of replication.


<table>
  <thead>
    <tr>
      <th></th>
      <th>T (min)</th>
      <th>Nτ&lt;T</th>
      <th>Nτ≥T</th>
      <th>τmin (min)</th>
      <th>τ¯ (min)</th>
      <th>k^ (min-1)</th>
      <th>τ¯calc (min)</th>
      <th>Nc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Wild-Type</td>
      <td>20</td>
      <td>171</td>
      <td>46</td>
      <td>4</td>
      <td>9.1</td>
      <td>0.12</td>
      <td>9.4</td>
      <td>4.2</td>
    </tr>
    <tr>
      <td>Rif-Treated</td>
      <td>20</td>
      <td>42</td>
      <td>35</td>
      <td>4</td>
      <td>12.3</td>
      <td>0.05</td>
      <td>21.6</td>
      <td>1.8</td>
    </tr>
  </tbody>
</table>

We further show that disruption of the restart process leads to permanent disappearance of the helicase complex. DnaC is required for the loading of the replicative helicase (DnaB), and is recruited to rescue stalled replication forks (Sandler, 2000). Here, we disrupted the restart process using a temperature-sensitive version of the helicase loader protein (dnaC2 allele) (Reyes-Lamothe et al., 2008). We visualized DnaB-YPet in the dnaC2 mutant under non-permissive conditions (37°C) using the same technique as in the dynamics experiments (Figure 5—figure supplement 2A). Helicase complexes observed in the first frame disassembled before the end of the time course in 86% of cases. Furthermore, new complexes rarely developed (15% of the time). To further quantitate this data, we calculate the probability of observing a focus as a function of time in cells that have at least one focus. In the strains containing the dnaC2 allele, this probability decreases throughout the time series, consistent with failure to restart (Figure 5—figure supplement 2B). This observed loss of foci is too rapid to be explained by replication termination (see Figure 5—figure supplement 2B, null hypothesis). In contrast, the probability of observing a focus in the wild type strain (at 37°C) does not depend strongly on time, indicating that the replisome is in steady state due to its ability to restart. These data are consistent with reports suggesting that dnaCts alleles are ineffective for synchronization because replication does not proceed to completion (Ferullo et al., 2009; Maisnier-Patin et al., 2001). Overall, these findings are consistent with both our observations in B. subtilis and our interpretations of the results of the E. coli stoichiometry measurements, suggesting that E. coli cells also experience pervasive replisome instability due to transcription.

### Transcription inhibition increases the rate of replication

To test the replisome-instability model, we measured replication rates in vivo by radioactive thymidine incorporation assays in B. subtilis, in both wild-type (without DnaC-GFP) and DnaC-GFP strains. It takes roughly 40 min to replicate 4.2 and 4.6 Mb of DNA in B. subtilis and E. coli, respectively; at the 500 bp/s −1 kb/sec measurements from in vitro and in vivo experiments (Kornberg, 1992), which assume replisome stability during a replication cycle. However, our observation of frequent conflicts (during which the replisome stalls) predicts that the in vivo rates should increase if conflicts are reduced. To test the prediction of our model, we measured the rate of thymidine incorporation with and without rifampicin treatment, as well as in the rpoB* strains – two different conditions where we observed the stabilization of the replisome. As predicted, both transcription perturbations (rifampicin and rpoB*) increase the replication rate: Thymidine incorporation rates in rifampicin-treated cells are roughly 60–65% higher than that measured for untreated cells (Figure 6A). The consistency of the incorporation rate in the rpoB* strain with rifampicin treatment suggests that the observed increase in rates is probably not an artifact of changes in nucleotide uptake in rifampicin-treated cells (Wang et al., 2007b). This interpretation is also supported by the insensitivity of rpoB* strains to rifampicin treatment with regards to thymidine incorporation rates. In addition, measurements of the thymidine incorporation rates in DnaC-GFP cells provide further evidence that DnaC-GFP is functional during slow growth: We did not detect any difference in thymidine incorporation rates between the wild-type and the DnaC-GFP strain under these conditions (Figure 6A). These results provide further evidence that the rate of replication is severely inhibited by transcription in wild-type cells.

![Figure 6.](https://cdn.elifesciences.org/articles/19848/elife-19848-fig6-v3.jpg)

**Figure 6.:** (A) DNA replication rates increase upon transcription-inhibition and in rpoB* strains. Thymidine incorporation assays were used to measure the relative rates of DNA replication in WT and DnaC-GFP strains, with (blue bars) and without (gray bars) perturbations to transcription by rifampicin treatment (Rif) or rpoB* cells. Note that rpoB* strains are resistant to rifampicin and therefore show no additional increase in replication rate after rifampicin treatment. (B) DNA replication rates increase in cells grown in minimal arabinose medium, relative to glucose, where transcription of rRNA and other ribosomal protein genes is higher.

The observed transcription-induced replication conflicts should be at least partially due to the ribosomal RNA and protein genes. We previously showed that replication restart proteins preferentially associate with these regions during fast growth (Merrikh et al., 2011). Although somewhat counterintuitive, our model predicts that replication rates should be slower during fast growth due to conflicts with transcription. To test this prediction, we measured replication-rates in slow and fast growth conditions. Despite the faster growth rate of B. subtilis on minimal glucose versus arabinose medium, we observe significantly higher thymidine incorporation rates in arabinose compared to glucose, where ribosomal RNA and protein genes are much more highly expressed and are a major source of conflicts (Figure 6B, and Mirouze et al., 2011).

## Discussion

The basic principles underlying the mechanism of genome replication are thought to be well established, especially in bacteria. Yet, a great part of this work has relied on a combination of in vitro reconstitution, from which potentially essential cellular factors and/or processes are absent, or in vivo ensemble measurements which are sensitive only to ensemble-averaged cellular behavior. Based primarily on these results and the absence of significant evidence to the contrary, DNA replication was thought to be largely a continuous process that initiates at the origin and moves processively to the terminus. However, there is a contradiction to this widely-accepted model: Our laboratory and others have demonstrated that the replication process can be disrupted from a number of concurrent processes including transcription. The resulting replication conflicts have dire consequences in the absence of rapid and efficient replication restart. If transcription is both an obstacle to the replisome and active throughout the cell cycle, how can the replication process be continuous? If conflicts can occur, what is their frequency? And if these events are frequent, what are the consequences for the replication machinery?

Using in vivo single-molecule fluorescence microscopy techniques in combination with a genetic and cell-biology toolkit developed for studying replication conflicts, we measured the stoichiometry and lifetimes of replication complexes in single cells with single-molecule resolution. The results of the replicative helicase complex stoichiometry experiments could be explained by a number of models. It is conceivable that the replisome traverses one of the two arms of chromosome much more rapidly than the other, reaching the terminus and disassembling much earlier than the second replisome complex. However, genomic DNA analyses have already demonstrated that in growing cells, the copy number of the two arms are roughly equal, implying that the average rate of replisome movement on the two arms is about the same (Srivatsan et al., 2010). Another model for the low observed replisome stoichiometry is the observation of individual forks, as has previously been reported in E. coli. But, our own quantitative characterization of replisome localization reveals factory-like (co-localized) replisome positioning for 80% of the cell cycle in both E. coli and B. subtilis, which cannot account for the low observed stoichiometry in our own experiments (Mangiameli et al., 2017) or previous work (Reyes-Lamothe et al., 2010). The data presented here is most consistent with the model that elongating replisomes are frequently disrupted (roughly 50% of the time) and disassembled during a single replication cycle.

The direct visualization of the replisome with SMFM in two different bacterial species strongly suggests that the replisome is frequently destabilized by transcription. The observation that these inferred disassembly events are transcription-dependent not only suggests that these events correspond to replication-transcription conflicts previously observed via biochemical means, but also that vast majority of replication conflicts are the result of transcription.

Our findings suggest that replicating cells often possess only a single active replisome complex. Together, the stoichiometry and dynamics of the replicative helicase and polymerase complexes as well as the replication rate measurements suggest that the replisome is subject to pervasive disassembly and reassembly events. These observations provide a potential explanation for the essentiality of replication restart proteins – at least under growth conditions where rDNA and ribosomal protein genes are relatively highly expressed and PriA is essential.

Due to the low intensity of single fluorescent molecules, both the stoichiometry and dynamics experiments are technically challenging. In addition, the bacteria themselves are potentially subject to photo damage at the intensities required to resolve single molecules, and this photo damage itself affects cellular processes and replication in particular. Therefore, it is essential to consider these measurements in the context of additional corroboratory biochemical and genetic evidence. The essentiality of restart proteins and the measurement of the replication rates provide independent lines of evidence for the pervasive disassembly model.

We propose that the number of replication-transcription conflicts is significantly greater than previously suggested: far from being rare, we infer from the data presented here that conflicts are generic and occur multiple times per cell cycle. If so, then these encounters frequently compromise the integrity of the replisome, leading to discontinuity in the process of DNA replication. These observations therefore present a new model for the canonical states of DNA replication, arguing against the well-accepted model that the process of replication is highly continuous in vivo.

## Materials and methods

### Growth curves

Cell cultures were grown for 16 hours in minimal arabinose (or LB) medium supplemented with threonine and tryptophan until cells reached log phase growth. Cells were then diluted back to an OD600 of 0.1 and monitored at 25 min intervals.

### Western blots

B. subtilis cells harboring the dnaC-gfp allele as well as the isogenic wild type were grown to an OD600 of 0.3 and then harvested. Total protein was prepared in SDS loading buffer, and the same volume was loaded on each of the lanes shown. Western blots were probed in Odyssey blocking buffer (Li-Cor P/N 927–40100) with either rabbit anti-DnaC polyclonal antibodies (1:5000 dilution), or rabbit anti-GFP polyclonal antibodies (1:7500 dilution). Blots were then probed with Li-Cor secondary anti-rabbit IR800 antibody at 1:15000 dilution. Blots were scanned and quantified on a Li-Cor Odyssey.

### Strain list and strain constructions

All strains used in this study are listed in Table 5. The strain containing the IPTG-inducible lacZ (Pspank(hy)-lacZ) construct (HM1316), was built by transformation of the plasmid (pHM149) encoding thrC::Pspank(hy)-lacZ into strain HM262. The polC-ypet strain (HM604) was constructed by transforming pHM93 (3` polC-LEGSG-ypet A206K) into wild-type JH642 B. subtilis cells. rpoB* mutants were isolated by plating 3 ml of saturated B. subtilis cells harboring dnaC-gfp, or E. coli cells harboring dnaB-ypet, on LB +0.3 µg/ml rifampicin plates. Revertant colonies were isolated and their rpoB gene was sequenced. Rifampicin revertant strains having mutations within rpoB were considered rpoB* strains. We examined mutants harboring the H482Y mutation which is in cluster 1 of the rpoB gene. The strains containing this mutation do not display growth defects on LB or LB supplemented with rifampicin, as was also previously reported (Maughan et al., 2004). HM2475 (PriA CRISPR precursor) was constructed by transforming the plasmid pHM273 into HM262 to incorporate the sgRNA at amyE. The full PriA CRISPR resulted from transformation of gDNA from HM1500 into HM2475. Additional control strain HM2387 containing only dcas9 resulted from transformation of gDNA from HM1500 into HM1. The E. coli strain containing the dnaC2 allele was constructed by P1 transduction of dnaB-ypet from HM1391 into PAW542.

**Table 5.**
 Strains used in this study.


<table>
  <thead>
    <tr>
      <th>Strain #</th>
      <th>Genotype</th>
      <th>Species</th>
      <th>Reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>HM1</td>
      <td>trpC2 pheA1; wild-type</td>
      <td>B. subtilis</td>
      <td>Smith et al.</td>
    </tr>
    <tr>
      <td>HM262</td>
      <td>dnaC-gfp-spec</td>
      <td>B. subtilis</td>
      <td>Lemon et al.</td>
    </tr>
    <tr>
      <td>HM1312</td>
      <td>dnaC-gfp rpoB (H482Y)</td>
      <td>B. subtilis</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>HM1316</td>
      <td>dnaC-gfp-spec thrC::Pspank(hy)-lacZ::erm</td>
      <td>B. subtilis</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>HM604</td>
      <td>polC-ypet-mls</td>
      <td>B. subtilis</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>HM1275</td>
      <td>polC-ypet rpoB (H482Y)</td>
      <td>B. subtilis</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>HM1500</td>
      <td>lacA::Pxl-dcas9-mls</td>
      <td>B. subtilis</td>
      <td>Peters et al.</td>
    </tr>
    <tr>
      <td>HM2387</td>
      <td>HM1 lacA::Pxl-dcas9-mls</td>
      <td>B. subtilis</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>HM2475</td>
      <td>dnaC-gfp-spec amyE::Pveg-sgRNA-priA-cat</td>
      <td>B. subtilis</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>HM2486</td>
      <td>dnaC-gfp-spec amyE::Pveg-sgRNA-priA-cat lacA::Pxl-dcas9-mls</td>
      <td>B. subtilis</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>HM1318</td>
      <td>wild-type (AB1157)</td>
      <td>E. coli</td>
      <td>Dewitt et al.</td>
    </tr>
    <tr>
      <td>HM1319</td>
      <td>dnaB-ypet-kan</td>
      <td>E. coli</td>
      <td>Reyes-Lamothe et al.</td>
    </tr>
    <tr>
      <td>PAW912</td>
      <td>dnaX-ypet-kan</td>
      <td>E. coli</td>
      <td>Reyes-Lamothe et al.</td>
    </tr>
    <tr>
      <td>PAW909</td>
      <td>dnaE-ypet-kan</td>
      <td>E. coli</td>
      <td>Reyes-Lamothe et al.</td>
    </tr>
    <tr>
      <td>PAW542</td>
      <td>dnaC2 thrA::tn10-tet</td>
      <td>E. coli</td>
      <td>Reyes-Lamothe et al.</td>
    </tr>
    <tr>
      <td>PAW1182</td>
      <td>dnaB-ypet-km dnaC2 thrA::tn10-tet</td>
      <td>E. coli</td>
      <td>This study</td>
    </tr>
  </tbody>
</table>

### Localization of replisome components

We ensure that fluorescent foci localize near midcell during active replication, consistent with localization to the replication factory. Stationary phase cells harboring replisome fusions do not have foci indicating that replication is required for localization and that the observed foci are not a result of protein aggregates.

### Cell preparation for microscopy

The following protocol was used to prepare cells for microscopy: (i) Cultures were grown overnight in a shaking incubator at 30°C. (ii) E. coli was cultured in M9-minimal media (1X M9 salts, 2 mM MgSO4, 0.1 mM CaCl2, 0.2% Glycerol, 100 μg/ml each Arginine, Histidine, Leucine, Threonine and Proline and 10 μg/ml Thiamine hydrochloride). (iii) B. subtilis was cultured in minimal arabinose media (1x Spitzizen’s salts (3 mM (NH4)2SO4, 17 mM K2HPO4, 8 mM KH2PO4, 1.2 mM Na3C6H5O7, 0.16 mM MgSO4-(7H2O), pH 7.0), 1x metals (2 mM MgCl2, 0.7 mM CaCl2,. 05 mM MnCl2, 1 µM ZnCl2, 5 µM FeCl2, 1 µg/ml thymine-HCl) 1% arabinose, 0.1% glutamic acid, 0.04 mg/ml phenylalanine, 0.04 mg/ml tryptophan, and as needed 0.12 mg/ml tryptophan.) (iv) Overnight cultures at an OD600 of 0.3–0.9 were diluted back to an OD600 of 0.2 and incubated again for about 2 hr until they reached approximately OD600 0.4. (v) Cells were then concentrated by a factor of 10 immediately before imaging by centrifugation. (vi) 1 μL of concentrated cell culture was spotted on a thin 2% (by weight) low-melt agarose pad (invitrogen UltraPure LMP Agarose, Cat. no. 16520–050). (vii) The sample was sealed on the slide under a glass cover slip using VaLP (a 1:1:1 Vaseline, lanolin, and paraffin mixture.) (viii) For rifampicin treatment, a final concentration of 100 μg/mL was added to both the agarose pad and the liquid culture immediately prior to imaging. (ix) Cells were imaged at 30°C.

### Microscope configuration

Imaging was performed on a custom-built inverted fluorescence microscope. To avoid light loss at the phase plate, cells were imaged through a Nikon CFI Plan Apo VC 100 × 1.4 NA objective. An external phase plate (Ti-C CLWD Ph3 Annulus Module) was inserted into the beam path during phase-contrast imaging and retracted for fluorescence imaging to avoiding decreased signal due to the neutral density annulus on the phase plate. The microscope focus was controlled by an IR-autofocus system. In short, an infrared beam was reflected off the coverslip-media interface and the back reflection is detected by a position-sensitive detector (PSD). The displacement was then processed using a PID feedback system to control the z-height of the piezo stage.

Fluorophores were excited by laser illumination. A Coherent Sapphire 50 mW 488 nm or 150 mW 514 nm CW laser is used to excite GFP and YPet, respectively. We expand the beam diameter is expanded to provide even illumination over the field of view. The excitation intensity is controlled via an Acousto-Optic Tunable Filters (AOTF, AA Opto-Electronic AOTFnC-400.650). Images were collected on an iXon Ultra 897 512 × 512 pixel EMCCD camera. The microscope system is controlled by Micro-Manager.

### Imaging protocol for bleaching analysis

A single phase contrast image is followed by a stack of 300 ms fluorescence images (settings summarized in Table 6). Fluorescence images are continued until all foci become photobleached (~120 frames). The imaging time is sufficiently fast that photodamage to the cells is not an issue. Because YPet is brighter, and the 514 nm laser tends to excite lower cellular background intensities (see section 1.4 of supplement for calculation of background), we were able to image at lower laser power.

**Table 6.**
 Microscopy parameters.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Laser power at objective (mW)</th>
      <th>Exposure time (ms)</th>
      <th>Med. background 1st frame (electrons/pixel)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Bleaching (GFP)</td>
      <td>1.3</td>
      <td>300</td>
      <td>87</td>
    </tr>
    <tr>
      <td>Bleaching (YPet)</td>
      <td>0.4</td>
      <td>300</td>
      <td>24.1</td>
    </tr>
    <tr>
      <td>Lifetime (GFP)</td>
      <td>1.1</td>
      <td>600</td>
      <td>76</td>
    </tr>
    <tr>
      <td>Lifetime (YPet)</td>
      <td>0.1</td>
      <td>600</td>
      <td>4.5</td>
    </tr>
  </tbody>
</table>

### Bleaching analysis

The method for determining the in vivo stoichiometry of fluorescent-fusion proteins in active replisomes is outlined below. Our protocol is based-upon the method described recently by Reyes-Lamothe et al.(Reyes-Lamothe et al., 2010) with a number of modifications described in detail below.

### Segmentation of the cells from the phase-contrast image

Cells are initially imaged in phase contrast for the purpose of segmentation, the computational process of determining cell boundaries from an image (Figure 1—figure supplement 2A). Imaging for bleaching analysis is sufficiently fast (36 s) that the cells do not grow appreciably during the process, allowing only a single phase image to be collected at the beginning of data acquisition. We then used the Wiggins Lab’s custom segmentation tool (superSegger) on the phase image to generate cell masks for analysis (Kuwada et al., 2013). The Wiggins Lab's custom image processing software (superSegger) and documentation is available at the following link: http://mtshasta.phys.washington.edu/website/SuperSegger.php

### Location and scoring of foci in the summed image

Firstly, to remove xy sample drift, all fluorescence images in the stack are aligned against the first. This corrected alignment is retained for the rest of analysis. Analysis of cell fluorescence begins by computing the summed image, which constitutes of summing the intensity values over all frames in the image stack and then applying a one pixel radius Gaussian blur. We then watershed the conjugate of the summed image to generate sub-regions around each intensity maximum (Figure 1—figure supplement 2). Taking the union of these regions with the cell masks excludes regions external to the cells from analysis. These sub-regions will be called intensity regions. The intensity profile in each intensity region is modeled by a Gaussian distribution:

$$
G( x→ ) = G_{G} exp[−\frac{(x→ − x→_{0})^{2}}{2 b^{2}}] + G_{0},
$$

where, the peak amplitude Gaussian intensity is defined by parameter $G_{G}$ and the parameter $G_{0}$ defines the background intensity. The focus position is parameterized by $x→_{0}$ and the focus width by parameter $b$. Within each intensity region, a three pixel radius circular region is centered on the position of the maximum-intensity pixel. The Gaussian intensity model is then fit inside the union of each intensity region and the corresponding circular region. The resulting focus position from the fit $(x→_{0})$ is then retained throughout the analysis.

Once the fit has been performed in each region in the cell, these foci are excised from the cell image using a mask radius of 3 pixels. We compute the per-pixel mean and standard deviation of the intensity ($I_{B}$ and $\deltaI, $respectively) in the remaining cell area. We define the background-subtracted intensity:

$$
ΔI ≡ I − I_{B}.
$$

In general, we found that the background-subtracted intensity had better statistical properties than the Gaussian fit parameters.

### Focus scores

The focus score $\sigma$ is a measure of the statistical significance of a focus. The integrated background-subtracted intensity $I_{A} $in a region (radius three pixels and area $A_{M}=\pir^{2}$) is computed. We define the score:

$$
\sigma= I_{A}/\deltaI\sqrt{A_{M}},
$$

where the factor of $\sqrt{A_{M}}$ in the denominator accounts for extended area $A_{M}$ over which the intensity is integrated. The intensity noise at each pixel is assumed to be uncorrelated and therefore the expected standard deviation in the integrated intensity in area $A_{M}$ is $\deltaI\sqrt{A_{M}}$.

All foci scoring two or smaller tended to be located randomly throughout the cell, inconsistent with localization to the replication factory. We therefor retain foci with scores greater than two for further analysis.

### Determination of the focus and background intensities in individual frames

Returning to the stack of fluorescence images, we compute the raw focus intensity ($I_{R}) $in each frame by summing the intensity within a disk (radius three pixels) centered on the position of the focus ($x→_{0}$, determined in the previous step). The per-pixel background intensity was again computed by excising each locus (using a mask radius three pixels) and then computing the mean intensity over the remaining cell area ($I_{B})$. We define the focus intensity ($I_{F}$) as the difference between the raw focus intensity and the total background intensity within the area of the 3-pixel-radius mask ($A_{M})$:

$$
I_{F} = I_{R} − A_{M}I_{B}
$$

This background subtraction method is illustrated for a focus in Figure 1—figure supplement 3, Panel B. The intensity, $I_{F}$, is interpreted as the intensity of the fluorophores at the focus for each frame and plotted to form bleaching traces.

### Analysis of bleaching traces

A key step in the determination of the single-molecule protein stoichiometry is the determination of the fluorescence intensity of a single fluorescent molecule, which M. Leake has called the unitary step (Leake et al., 2006). Two independent methods were used to determine this fluorescence intensity: (i) The intensity of GFP and YPet molecules were measured in vitro and (ii) the fluorophore intensity was inferred for each complex in vivo from the analysis of the bleaching curves (Leake et al., 2006).

In both cases, the intensity must be inferred from a noisy intensity trace. The method for trace analysis of Leake et al. (Leake et al., 2006, Reyes-Lamothe et al., 2010) was:

### Smoothing the intensity trace

Because the raw intensity data has too large a variance to directly detect steps by analysis of the pairwise differences, Leake et al. applied an Edge-Preserving Chung-Kennedy (SED) Filter to smooth the intensity data (Smith, 1998). Instead, we use a parameter-free change-point (CP) analysis to idealize the bleaching curves (Wiggins, 2015). The analysis of simulated intensity traces (Figure 7) with similar statistical properties to the observed data illustrates our method for calculating stoichiometry, and the performance of our CP idealization compared to the SED filter. We provide a more detailed discussion of the comparison of the CP method to competing methods in the following sections.

![Figure 7.](https://cdn.elifesciences.org/articles/19848/elife-19848-fig7-v3.jpg)

**Figure 7.:** (A) Simulated intensity data. A bleaching experiment was simulated to demonstrate the performance of the CP Algorithm against the SED filter. The noise and trace length were chosen to closely approximate the observed data. (B) Idealized intensity traces. The data (blue dots) is identical to Panel a. True simulated mean (Truth) is shown in blue. There is excellent agreement between the truth (blue) and the CP idealization (red). The SED filtered trace is shown in green. (C) Pairwise intensity difference probability distribution (PDPD). The black dotted lines represent multiples of the true step-size 1 AU. (D) Power spectrum of the PDPD. The largest peak in the power spectrum is selected as the unitary step (red dotted). The true step-size is also shown (black dotted).

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/19848/elife-19848-fig7-figsupp1-v3.jpg)

**Figure 7—figure supplement 1.:** The performance of the CP versus the SED filter is measured by a histogram of the relative size of the unitary step in simulated data. The CP idealization clearly results in a sharper distribution about the true value (unity).

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/19848/elife-19848-fig7-figsupp2-v3.jpg)

**Figure 7—figure supplement 2.:** We simulated two approaches for determining the initial intensity of the trace: Exponential Fit and Highest-Level. The probability of the estimated intensity is shown relative to the true initial intensity. The Highest Level method is clearly biased from below relative to the Exponential Fit method which is centered around the true value (unity).

![Figure 7—figure supplement 3.](https://cdn.elifesciences.org/articles/19848/elife-19848-fig7-figsupp3-v3.jpg)

**Figure 7—figure supplement 3.:** (A) Eight typical datasets (black dots) are plotted with the true mean (blue) and idealizations using both the KV (red) and CP (green) algorithms. The simulated data consisted of 10,000 Gaussian processes with unit variance simulated for 120 frames each. The over segmentation generated by the KV algorithm is clearly visible in the (false) transitions shown in the third, fourth, and fifth traces. No false steps were observed in these eight traces using the CP algorithm. (B) The total number of states for the 10,000 simulated datasets is shown for the true mean and the CP and KV idealization. All datasets consisted of a single true level. The true number of states (one) was found 95% of the time using the CP algorithm and only 55% of the time using the KV algorithm.

![Figure 7—figure supplement 4.](https://cdn.elifesciences.org/articles/19848/elife-19848-fig7-figsupp4-v3.jpg)

**Figure 7—figure supplement 4.:** The efficiency of change-point detection was measured for fixed-lifetime and variable-lifetime (constant decay rate) steps. In both cases the mean lifetime was equal to the inverse observed decay rate (41 frames). For fixed-lifetime steps (blue), the detection efficiency is essentially unity for relative step-size greater than two. (We define the relative step size as the mean intensity difference divided by the standard deviation: Δµ/σ.) For variable-lifetime steps (red), the detection efficiency is reduced by the existence of a small fraction of short-lived steps.

![Figure 7—figure supplement 5.](https://cdn.elifesciences.org/articles/19848/elife-19848-fig7-figsupp5-v3.jpg)

**Figure 7—figure supplement 5.:** (A) Distribution of estimated stoichiometry for simulated data with true stoichiometries from 4–14 proteins. (Integer stoichiometries between 3 and 15 were simulated. For clarity only the distributions for even stoichiometries are plotted.) (B) Mean estimated stoichiometry as a function of true stoichiometry. The estimated stoichiometry slightly overestimates the true stoichiometry (by a fraction of a protein).

### Pairwise distribution

Figure 7C shows the PPDD for the raw simulated data (blue), CP idealization (red) and SED filtered data (green). The black dotted lines are placed at integral multiples of the true step size (1 AU). Note that the peak widths in the CP idealization are computed from the Fisher Information (Wiggins, 2015). The first peak in the pairwise distribution of the CP idealization is centered around the true value (1 AU), showing excellent agreement between the calculated and the true step sizes.

### Power spectrum

Figure 7D shows the Power Spectrum of the PPDD. Again, the CP idealization shows a stronger enrichment in power at the true intensity step-size (1 AU). Note that the power spectrum is not an FFT, but rather a continuous representation of the Fourier transform of discrete data that is commonly applied in this context (e.g. (Little and Jones, 2013).

### Determination of the unitary step

Leake et al. report that they select the first peak (with respect to increasing intensity) in power spectrum that is four standard deviations above the noise (Leake et al., 2006). Clearly this method is ad hoc since lower noise would resolve higher harmonics of the unitary step, as are easily visible in the power spectrum for the CP idealization. Instead, we selected the largest peak in the power spectrum, as illustrated by the dotted red line (Figure 7D). This approach resulted in the reliable determination of the unitary step in simulations. We show a histogram estimating unitary step size (relative to the true step size) in Figure 7—figure supplement 1. In our simulations, the Leake et al. method (using the SED filter) resulted in a greater number of failures to correctly identify the unitary step. Most worrying of all, the SED filter lead to a fairly frequent identification of the unitary step as roughly twice the true unitary step, leading to anomalous counts of complexes with half the true stoichiometry.

### Determination of the initial focus intensity

Because the probability of a fluorescent protein bleaching is proportional to the number of unbleached proteins, we expect the raw intensities follow a decaying exponential profile. To determine the initial focus intensity $(I_{0})$, we fit the background subtracted raw intensities to a model of the form

$$
I(t)=I_{0}exp(−t/t_{b}),
$$

optimizing both $I_{0}$ and the characteristic bleaching time $(t_{b})$. We found that this method was more reliable than simply taking $I_{0}$ as the highest level of the filter based on simulated intensity traces (see Figure 7—figure supplement 2). Although the highest level is less noisy than the exponential fit, we find highest level to be biased from below.

The mechanism for the bias generation for the highest-level method is as follows: The initial decay in intensity is too rapid to resolve all bleaching steps at high stoichiometry and therefore bleaching steps are merged at the beginning of the bleaching process. As a result the highest-level method typically averages over the first few true levels in the bleaching process. We note that, in general, both the highest-level and exponential fitting techniques produced acceptable results.

### Data selection

After automatic processing, all traces are refereed by hand. We remove cells where:

While applying these data-selection rules had no qualitative effect on our results and conclusions, the selection rules did remove data points that were clearly aberrant from the analysis. All datasets were repeated on at least two occasions, with similar results.

### Analysis of final count distributions

We divide the initial focus intensity by the unitary step size for a large number of cells, obtaining final count distributions for each strain. Many of these distributions were bi-modal. We fit all count distributions using a two-Gaussian mixture model where the Gaussian widths, means ($\mu_{1 }, \mu_{2}$) and peak amplitudes were optimized. To avoid binning the data, we use a maximum likelihood process to determine the best-fit parameters. The fractional population of factories in the low and high stoichiometry populations (FL and FH) is proportional to the area of the model Gaussians peaked near the appropriate values. See Figure 3—figure supplement 2 and Figure 4—figure supplement 1 for maximum likelihood fits to all stoichiometry distributions not shown in the main figures. The fit parameters are represented graphically in main Figures 3D and 5D, and numerically in Table 2 and Table 3 for B. subtilis and E. coli, respectively. Note that the error in FH and FL was calculated by simulating 10,000 stoichiometry distributions with the same statistical properties as the corresponding empirical distribution. The width of the distribution of FL (or FH) based on the simulated distributions was taken as the error.

### Kernel density estimates

For plotting the probability densities for protein stoichiometry, we used a Kernel Density Estimate (KDE) in order to avoid binning the data (e.g. [Reyes-Lamothe et al., 2010]). A Gaussian kernel was used, and the optimal bandwidth was selected by minimization of the asymptotic mean integrated squared error.

### Discussion of filtering algorithms

Because the raw intensity data has too large a variance to directly detect steps by analysis of the pairwise differences, Leake et al. applied an Edge-Preserving Chung-Kennedy (SED) Filter to smooth the intensity data (Smith, 1998). Although we could also detect intensity steps using the SED filter, this approach appeared to have two important shortcomings: (i) The filter had what we considered poor performance under many scenarios (described below) and (ii) the filter uses two ad hoc filtering parameters which must be optimized. In our hands, the results of the SED filter were not particularly robust to parameter choice.

To eliminate the need to specify ad hoc parameters for the data analysis, we attempted to apply an objective parameter-free step-detection algorithm developed by Kalafut and Visscher (KV) (Kalafut and Visscher, 2008). The KV filter uses a Change-Point Algorithm for determining steps in a signal. The KV filter, as described, has two important shortcomings with respect to the current application: (i) The signal is assumed to have constant variance for all states (false) and (ii) the statistical test for step determination uses the Bayes Information Criterion (BIC), which we have recently demonstrated does not result in optimal performance (Wiggins, 2015), resulting in either over or underfitting depending on the application.

We describe the adaptation of Change-Point Methods to biophysical applications elsewhere (Wiggins, 2015). In short, our CP algorithm is parameter free. The performance of the CP Algorithm and the SED filter applied to simulated intensity data is shown in Figure 7A shows the raw (unfiltered) data. Panel B shows the truth (blue, true mean intensity simulated), the simulated data (blue dots), CP idealization (red) and the SED filter (green). The performance of the CP Algorithm correctly determines the position of all steps except one and is qualitatively superior to the performance of the SED filter.

Note that in general the step determination at high intensity is imprecise due to the large variance ($\deltaI^{2}∝I$). For higher intensities than those shown in the simulation, the CP algorithm cannot reliably determine the steps, although the CP idealization represents an optimal guess (Wiggins, 2015). One might worry that these imprecisely-determined high-intensity steps could result in a significant degradation in the pairwise distribution function, but there are two natural mechanisms for the suppression of their contribution: (i) The short duration of these steps in frames and the large std both result in a small Fisher Information. (ii) Furthermore the weighting in the PPDD is proportional to the lifetime of the step. Therefore these short steps have a much weaker role in determining the single-fluorophore intensity than the long-lived and less noisy steps at the end of the bleaching trace (Wiggins, 2015).

### The KV versus CP filter

We discovered that the KV filter does not apply a statistical test with suitable frequentist statistical performance to evaluate the existence of new intensity levels. To compare the performance of the KV and CP filters, we simulated intensity data with no transitions. For simplicity, we used a Gaussian process with unit variance for 120 frames for 10,000 independent simulated datasets. We then idealized this data using both the KV and CP filters. Figure 7—figure supplement 3 for the analysis of 10 typical simulated traces and their idealization using both the KV and CP filters. The KV algorithm has a Type I error (finding at least one false transition) 45% of the time! (See the bar plot of algorithm performance in Figure 7—figure supplement 3B) This result implies that data analysis is performed with a 55% confidence level in a Neyman-Pearson Hypothesis Test. Such a small confidence level is clearly unacceptable from a canonical frequentist perspective. In contrast, the Type I error rate for the CP filter is 5%, corresponding to a 95% confidence level. (Although the above simulation describes a scenario under which the KV filter leads to significant over-fitting, in other circumstances, the KV filter can result in significant under-fitting and therefore should not be used for quantitative applications.)

### Simulation: Step detection efficiency using the CP filter as a function of step size

There are a number of important factors that influence the resolution of the CP filter. The ability of the CP algorithm to resolve steps depends principally on the lifetime of the states and the step size between states. To estimate the resolution of the CP filter in step determination, we first simulated transitions from one to zero flours (the final bleaching step) using a constant lifetime equal to the inverse observed intensity decay rate (tb = 41 frames). The Fixed-Lifetime curve in Figure 7—figure supplement 4 shows the detection efficiency for the bleaching step as a function of step size. In our experiments, the step-size to the standard deviation ratio (Δµ/σ) is between 2 and 3. Under these conditions, the step detection efficiency is essentially unity. Of course, the last bleaching step has a distribution of lifetimes, rather than a fixed lifetime equal to the mean lifetime. Next we simulated photobleaching events with variable lifetimes (i.e. stochastic lifetimes with a bleaching rate of k = 1/41 frames). The variable-lifetime curve shows the detection efficiency for the bleaching step as a function of step size. Unlike the Fixed-lifetime curve, the variable-lifetime curve never reaches unity due to the existence of a small subset of events that are not long enough to resolve. In spite of the inability to resolve very short-lived states, the detection efficiency is still roughly 90% in the simulation at the observed signal to noise ratio (Δµ/σ ≈ 2.5).

### Simulation: Data generated by different protein stoichiometries

To test the overall consistency of the analysis approach, we simulated intensity traces using the observed ratio of step size to standard deviation (Δµ/σ ≈ 2.5 and assuming linear scaling of the variance with intensity) and state lifetime (k = 1/41 frames−1) for different stoichiometries between 3 and 15 proteins. The distribution of estimated stoichiometries for selected simulated stoichiometries is shown in Figure 7—figure supplement 5A. The mean estimated stoichiometry as a function of the true stoichiometry is shown in Figure 7—figure supplement 5B. Our simulated analysis results in a very small (<0.5) bias in the mean estimated stoichiometry and a mono-modal distribution of stoichiometry around the true value. The widths of the distributions are roughly consistent with those observed in experiment.

### Imaging protocol for replication-complex lifetime

Cells are imaged at two-minute intervals, taking both a phase and fluorescence image at each time point. For lifetime measurements, where the foci must be tracked over a longer time scale, bleaching is undesirable. In order to minimize both bleaching and possible photodamage to the cells (as indicated by abnormally slowed elongation), we find a longer (600 ms) exposure at lower laser intensity to be optimal. Imaging may continue for about 20 min before focus visibility is significantly impaired by photobleaching, and we note that cells were elongating exponentially regardless of laser use (data not shown).

### Analysis of replisome-complex lifetime

Replisome foci were observed to undergo step-like transitions between on and off states. We attempted to use the same analysis used for the bleaching experiments. But, this analysis is designed around the assumption that the replisome undergoes minimal motion. Over the 20 min timescale, the replisome can undergo significant movement and therefore we needed to find an alternative approach.

The phase contrast image for each time point is segmented to determine cell boundaries. For analysis of the fluorescence images, we used a locus-tracking engine that we have described previously to track and quantify loci (Kuwada et al., 2013). In short, foci are detected and fit to a Gaussian point-spread function in each frame. Up to four foci are identified per cell. Each focus is assigned a score (as described in the section titled ‘Focus scores’ above). The larger the score the more confidence the algorithm has identified a true focus (versus a stochastic fluctuation is fluorescence intensity). Trajectories of replication complexes are then constructed by grouping foci based on the following rules: (i) No foci in the trajectory may score lower than 3. (ii) A focus cannot move more than 350 nm between frames. (iii) The mean of all scores in the trajectory must be a minimum of 4. (iv) At least one focus in the trajectory must score five or higher. (v) Trajectories may continue through a single frame with no (or score $\leq3$) focus provided that all of the above conditions are still met. (vi) Trajectories must last more than three frames. (vii) Included foci must show localization consistent with the replisome.

We have experimented with various rules for grouping foci, but the above best reproduced trajectories qualitatively consistent with the raw images. Foci scoring three or lower appeared randomly throughout the cell, inconsistent with protein bound to the replication factory. Higher cutoffs were found to lead to gaps in the locus trajectories that lasted for a single frame, consistent with stochastic fluctuations in intensity. We have also required that trajectories last a minimum of three frames. Shorter-lived events are consistent with events observed in cells without active replication, and therefore we believe that these events are also predominantly the result of stochastic fluctuations in fluorescence intensity. Note that, regardless of our choice of grouping, trajectories were always longer lived (on average) for rifampicin treatment and the rpoB* mutation.

For a disassembly event, foci must disappear for more than two minutes to be counted as disassembly events. (i.e. we require the off state to last for more than one frame to remove most intensity-fluctuation induced false negative events.) A typical trajectory corresponds to a cell containing a focus track with foci scores 3–7 transitioning to a cell with no foci or low-scoring foci (≤2 appearing in inconsistent locations in the cell from frame to frame, consistent with false positive focus identification due to photon shot noise (see Figure 2—figure supplement 1 for examples of scored trajectories).

### Controlling for bleaching in replisome-complex lifetime experiments

To exclude the possibility that disappearance events are due to photobleaching, we image the cells with the same settings as in the replisome-complex lifetime experiment, but remove the delay between frames. Under these conditions the cells will be dosed with the same amount of light, but over the shortened time scale we would expect bleaching to occur before disassembly due to a conflict. The results confirm that minimal bleaching occurs over the time course. The algorithm successfully tracks 92% and 86% of complexes for the duration of the lifetime experiments in B. subtilis and E. coli, respectively.

### Estimation of conflict number based on replisome complex lifetime

Modeling replisome disassembly events as a Poisson process, the distribution of focus lifetimes was fit using an exponential distribution. The likelihood for the focus lifetime is:

$$
p(\tau|k)=k exp(−k(\tau−\tau_{min})),
$$

where k is the disassembly rate, $\tau_{min}$ is the shortest observable lifetime (in our case, 4 min since we disregard events lasting less than three consecutive frames). Since some foci persist throughout the experiment, duration $T$, we must also compute the survival probability. The survival probability is (one minus the cumulative probability):

$$
Pr{\tau>t}=1−P(t|k)=exp(−k(t−\tau_{min})).
$$

The disassembly rate k was estimated using Maximum Likelihood Estimation. The sum of the log-likelihood for the observed lifetimes is:

$$
\sum_{i}log⁡ℒ(\tau_{i}|k)=\sum_{\tau_{i}<T}log⁡p(\tau_{i}|k)+\sum_{\tau_{i}\geqT}log⁡(1−P(T|k)).
$$

Note that the sum in the first term is taken only over the observable lifetimes while the second term accounts for long-lived states. Maximizing the likelihood leads to the following expression for the maximum likelihood estimate of $k$:

$$
k^=N_{\tau<T}/[N_{\tau<T}(\tau¯−\tau_{min})+N_{\tau\geqT}(T−\tau_{min})],
$$

where $N_{\tau\geqT}$ is the number of lifetimes that were at least the duration of the experiment and $N_{\tau<T}$ is the number of observed lifetimes and $\bar\tau $ is their empirical mean. A summary of the parameters used in the replisome-complex lifetime is provided in Table 1 (B. subtilis) and Table 4 (E. coli).

### Protocol for temperature-sensitive DnaC experiment

Cells were prepared for microscopy as described above, and imaged under non-permissive conditions using an objective heater (Bioptechs). Imaging started roughly 10 min after cells were placed on the heated objective. Trajectories were generated using the algorithm developed to measure complex lifetime, and foci included in these trajectories counted towards the probability of observing a focus as a function of time. The theoretical ‘null-hypothesis’ curve is generated by assuming a random segment of continuous (no disassemblies due to conflicts) 40 min replication cycle is visualized for 10 frames at 2 min intervals. We include all possible outcomes where a focus is visible in the first frame.

### Protocol for PriA CRISPR experiment

Due to the leakiness of the CRISPR system, PriA is already depleted three-fold before induction (Peters et al., 2016), and we note that the strain grew unusually slowly in minimal arabinose (however, the precursor strain without the sgRNA grew normally). The CRISPR system was fully induced by the addition of 1% xylose in liquid culture roughly 2 hr before imaging to allow the remaining PriA to be diluted out. DnaC-GFP foci were then identified from snapshot images (one phase contrast and one fluorescence image at each field of view). The number of cells with foci was quantified using the following rules: (i) the focus must score three or higher, (ii) the elipticity of the focus must be smaller than 1.2, and (iii) the focus localization must be consistent with the replisome. Because of the leakiness of the CRISPR, we compare to the number of foci in the precursor strain (does not contain sgRNA), also with the addition of 1% xylose. Time-lase microscopy was not productive because the PriA CRISPR strain formed few DnaC-GFP foci even without induction.

### Protein purification

Purified GFP was gifted to us by the Asbury Lab at the University of Washington. For purification of YPet, DH5α E. coli cells were transformed with the plasmid ROD49 carrying an arabinose-inducible his-tagged mYPet with the monomeric A206K mutation. (This plasmid was the gift of R. Reyes-Lamothe.) The expression was induced at an optical density (OD600) of 0.1 with 0.2% L-arabinose for 1 hr at 37°C. Cells resuspended in 20 mM HEPES pH 7.5, 0.5 M NaCl, 25 mM imidazole were lysed by sonication. Lysate was cleared by centrifugation for 1 hr at 18,000 x g, and proteins were purified by fast protein liquid chromatography (ÄKTA System, GE Healthcare) using a metal-chelating affinity column (HisTrap HP, GE Healthcare). YPet-containing fractions eluted at high imidazole concentrations were identified by absorbance at 280 nm and confirmed using a microplate photometer to verify the correct excitation and emission spectra.

### Preparation and imaging of surface immobilized protein

For imaging, we dilute purified protein in PBS to the point where individual molecules are visible during fluorescence microscopy. We fill a 10 µL flow cell (constructed by sticking a KOH cleaned coverslip to a base slide with two strips of two sided tape) with the PBS-fluorescent protein solution and allow it to sit upside down for 10 min, binding the proteins to the coverslip. The channel is then rinsed with 400 µL of PBS to clear any remaining fluorescent protein from the background.

We image and the isolated protein using the same settings as the in vivo bleaching experiments, and analysis proceeds as for live cell bleaching experiments (the only difference being that we do not take a phase contrast image and intensity regions are identified from the fluorescent images alone). See Figure 1—figure supplement 5A and Figure 4—figure supplement 2A for example isolated protein bleaching traces. We arrive at the unitary intensity step distribution for known single fluorophores. As a consistency check, we confirm that the in vivo unitary intensity step distributions for all strains are highly similar to those found in vitro. We find agreement of the peak values for in vivo and in vitro distributions to within 19% for GFP and 18% for YPet.

### Thymidine incorporation assays

Exponentially growing cells raised in minimal MOPS medium (Wang et al., 2007b) supplemented with either 1% arabinose or glucose, at 30°C, were split at OD 0.2 into equal 1.2 ml cultures. Cells continued to grow until they reached OD 0.3., at which point 30 µg/ml rifampicin was added to one of the cultures for 2 min. Next, 38 µCi 3H-thymidine (Perkin Elmer 70–90 Ci/mMol) was added to both cultures, and timepoints were taken at 2 min intervals by pipetting 200 µl of cells into 3 ml of ice-cold 10% TCA. Samples were collected on glass microfiber filters (GE Healtthcare #1825–025), and washed 3x with 5% TCA prior to detection on a liquid scintillation counter.
