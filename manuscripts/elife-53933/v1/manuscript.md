# Heterogeneous T cell motility behaviors emerge from a coupling between speed and turning in vivo

## Authors

- Elizabeth R Jerison<sup>1</sup> ([ORCID: 0000-0003-3793-8839](https://orcid.org/0000-0003-3793-8839)) †
- Stephen R Quake<sup>1</sup> ([ORCID: 0000-0002-1613-0809](https://orcid.org/0000-0002-1613-0809)) †

### Affiliations

1. Department of Applied Physics, Stanford University Stanford United States
2. Department of Bioengineering, Stanford University Stanford United States
3. Chan Zuckerberg Biohub San Francisco United States

† Corresponding author

## Abstract

T cells in vivo migrate primarily via undirected random walks, but it remains unresolved how these random walks generate an efficient search. Here, we use light sheet microscopy of T cells in the larval zebrafish as a model system to study motility across large populations of cells over hours in their native context. We show that cells do not perform Levy flight; rather, there is substantial cell-to-cell variability in speed, which persists over timespans of a few hours. This variability is amplified by a correlation between speed and directional persistence, generating a characteristic cell behavioral manifold that is preserved under a perturbation to cell speeds, and seen in Mouse T cells and Dictyostelium. Together, these effects generate a broad range of length scales over which cells explore in vivo.

## Introduction

Many immune cells migrate through tissue in search of antigen or pathogens. In some cases, such as during extravasation from blood vessels and homing to target organs, this migration is guided by chemokine gradients (Witt et al., 2005; Okada et al., 2005; Germain et al., 2012; Sarris and Sixt, 2015). However, for naive T cells within T cell zones, in situ imaging studies have found that unguided random walk processes dominate (Miller et al., 2002; Miller et al., 2003; Preston et al., 2006; Cahalan and Parker, 2008; Beltman et al., 2007; Banigan et al., 2015; Harris et al., 2012; Worbs et al., 2007; Textor et al., 2011; Beauchemin et al., 2007; Mrass et al., 2006; Katakai et al., 2013; Mrass et al., 2017, reviewed in Mrass et al., 2010; Krummel et al., 2016). This observation creates a conceptual challenge: T cells must dwell at scales of microns to make contact with antigen presenting cells (Wülfing et al., 1997; Krummel et al., 2000; Beltman et al., 2009a; Fricke et al., 2016), yet migrate over scales of millimeters to find rare targets. A conventional diffusive random walk struggles to access these varied scales efficiently, since a walker that dwells near another cell for 1 min would require several days to travel 1 mm. Several authors have suggested that T cells may have an intrinsic behavioral program that allows them to explore over different length scales (Harris et al., 2012; Krummel et al., 2016; Mempel et al., 2004). However, testing this hypothesis via in situ fluorescence microscopy raises inherent technical challenges: to observe a single cell accessing a broad range of spatial scales, it is necessary to have micron scale resolution over fields of view of millimeters, with low enough photodamage to observe the same cells at high spatiotemporal resolution over long periods. For example, one intriguing proposal is that T cells perform Levy flight (Harris et al., 2012), an anomalous random walk characterized by a power-law distribution of step sizes. Such random walks have been described in detail in the physics and ecology literature (Shlesinger et al., 1995; Bartumeus et al., 2005; Viswanathan et al., 2011), and their scale-free behavior provides a natural way for foragers to accelerate searches in many contexts (Bartumeus et al., 2002). However, observation over short periods cannot distinguish between Levy flight and heterogeneity amongst individual walkers (Petrovskii et al., 2011), both of which can create a broad distribution of displacements. More generally, we would like to understand whether there is a statistically-consistent behavioral program carried out by these cells.

To address this question, we used selective plane illumination microscopy (Pitrone et al., 2013; Power and Huisken, 2017) to observe the native population of T cells in the live larval zebrafish (Tg(lck:GFP, nacre-/-) Langenau et al., 2004), over millimeter fields of view and periods of a few hours. We observed a population of motile cells in tissue in the tail of the zebrafish, primarily in the tail fin and larval fin fold (Figure 1A, Figure 1—video 1). We chose this population for further study because of the potential to measure the interstitial exploration behavior of the cells over long length-scales, and to dissect the variation in behavior over a populations of cells.

![Figure 1.](https://cdn.elifesciences.org/articles/53933/elife-53933-fig1-v1.jpg)

**Figure 1.:** (A) Maximum Z projection of a Tg(lck:GFP, nacre-/-) zebrafish at 12 dpf. This projection represents the first frame of a timecourse; see Figure 1—video 1. (B) Brightfield of the region of tissue shown in A. Stitching across three tiles was performed in ImageJ. (C) Mean squared displacement as a function of time lag. The cells migrate super-diffusively on scales of a few minutes. The MSD for a persistent random walk is fit to the data (Materials and methods, Appendix 1). Error bars represent 95% confidence intervals on a bootstrap over n = 316 trajectories containing all measured time intervals. (See also Figure 1—figure supplement 2). Inset: linear scale for the first 10 min. (D) The velocity power spectrum, averaged across all trajectories (n = 634). A Levy (scale-free) process consistent with the short time behavior would result in a continuation of the high frequency slope (dashed line). Instead, we observe a timescale at a few minutes. (E) Distribution of bout lengths within a trajectory (Materials and methods), fit with a stretched exponential (n = 35819 bouts). The fitted stretch parameter $\beta=.9$. For all panels, trajectories were pooled from n = 16 fish.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/53933/elife-53933-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** Stitched brightfield image of the zebrafish tail, (same as Figure 1B), with the fin fold and tail fin regions indicated. Lines were added at the border between the fin fold and muscle regions of the tail to guide the eye.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/53933/elife-53933-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** MSD for all trajectories tracked through 15 min, including all measured time intervals (n = 612). As with the subset of longer trajectories, we observe a curved MSD consistent with a persistent random walk (PRW) model. Inset: linear scale through 10 min, showing a straight line consistent with diffusive behavior after the first few minutes. Error bars represent 95% confidence intervals on a bootstrap over trajectories.

Rather than a single broad distribution of speeds sampled by all cells, as in Levy flight, we observed considerable heterogeneity in both speed and turning behavior across cells. This observation, together with prior literature (Maiuri et al., 2015), prompted us to analyze the distribution of cell behaviors in a space defined by speed and turning statistics. Surprisingly, cell behaviors fell on a one dimensional manifold in this space, characterized by a coupling between speed and directional persistence. Analysis of previously-published data in mouse T cells (Gérard et al., 2014) and Dictyostelium (Dang et al., 2013) within this framework showed that their migration statistics fell along a similar manifold. Our results show that a wide variation in speeds, combined with a coupling between speed and persistence, generate a broad distribution of length scales of exploration in vivo.

## Results

### Cell motility behavior is inconsistent with Levy flight

To investigate the statistical properties of T cell motility in our system, we measured cell trajectories within the tissue posterior to the anus (Materials and methods, Figure 1—video 1, Figure 2—video 1). This region is composed primarily of the tail fin and larval fin fold, which represent a millimeter-scale tissue over which the cells can potentially migrate. We note that cells in circulation, while present, move orders of magnitude faster than those in tissue, and thus are not included in our observations or analysis. Note also that our observations were performed in the absence of an external perturbation such as an infection.

We first evaluated evidence for Levy flight behavior, as opposed to persistent random walks (Beauchemin et al., 2007; Beltman et al., 2007; Banigan et al., 2015; Harris et al., 2012), in our system. The distinction hinges on whether the statistics of individual trajectories are scale-free, so that super-diffusive behavior continues to long times; or if, alternatively, individual trajectories are diffusive at long times but there is heterogeneity across the population. To address this question, we performed a standard analysis of mean squared displacement as a function of time interval. Consistent with previous measurements (Beauchemin et al., 2007; Beltman et al., 2007; Banigan et al., 2015; Harris et al., 2012), we observed a faster-than-linear increase in MSD at early times, indicating super-diffusive behavior, with a best-fit line in surprisingly good quantitative agreement with previous observations up through 10 min (Harris et al., 2012; Fricke et al., 2016; Figure 1C). However, we observed a transition at the scale of minutes, consistent with persistent random walks, and inconsistent with Levy flight (also note the straight line on a linear scale, Figure 1C inset, characteristic of diffusive behavior). Note that while we have examined the subset of longer trajectories to measure the behavior through an additional order of magnitude in time, this result also holds when examining all trajectories through 15 min (Figure 1—figure supplement 2). To further test for an intermediate timescale, we computed the velocity-velocity power spectrum, using secant-approximated velocities along each trajectory (Materials and methods). This quantity captures the timescale at which the velocities become decorrelated, if it exists; for a Levy-flight process the same negative slope is observed at all frequencies (Viswanathan et al., 2005), while a persistent random walk model passes towards zero slope at low frequencies (Viswanathan et al., 2005; Pedersen et al., 2016). Consistent with the MSD analysis, we observe two regimes, with a clear timescale on the order of minutes (Figure 1D). Finally, we computed the distribution of lengths between direction changes (bout lengths) within a trajectory (Materials and methods), scaled by the average bout length as suggested in Petrovskii et al., 2011, and did not observe the characteristic Levy-flight power law (Figure 1E).

### Motility behavior is heterogeneous across cells

Since we did not find support for Levy flight in our system, we next evaluated evidence for cell-to-cell heterogeneity. From examples of velocity traces (Figure 2A,C–E, Figure 2—video 1), we observed substantial variation in speed between cells, that can persist over spans of a few hours. These trajectories are not atypical: overall, 88% of trajectories have distributions of secant-approximated speeds that are inconsistent with the speed distribution pooled on all trajectories (KS test, $p<.01$). Interestingly, we also found significant heterogeneity in cell turning behavior: 67% of cells had turn angle distributions inconsistent with the overall distribution (KS test, $p<.01$).

![Figure 2.](https://cdn.elifesciences.org/articles/53933/elife-53933-fig2-v1.jpg)

**Figure 2.:** (A) Example of trajectories recorded over 3 hr at a 12 s interval (Tg(lck:GFP, nacre-/-) zebrafish; 10 dpf). Here we show a maximum Z projection of the 900th frame with trajectories overlaid; see Figure 2—video 1 for the timecourse. Examples of four cell trajectories, with a range of characteristic speeds, are colored. (B) Spearman rank correlation between trajectory speeds measured on non-overlapping 19.5 min intervals, as a function of the time between the beginning of the intervals. Error bars represent 95% confidence intervals on a bootstrap over trajectories. The null model was constructed by permuting measured speeds across all the trajectories at each interval; error bars represent 95% confidence intervals over the permutations. (Calculations performed on the n = 321 trajectories of at least 117 min in length.) Trajectories were pooled over n = 16 fish. (C) Velocity traces for the four cells highlighted in A. (D) Secant-approximated speed distributions for each cell from A, compared with the distribution over all cells (grey;n = 98141 steps). (E) Turn angle distributions for each cell from A, compared with the distribution over all cells (grey;n = 96122 turn angles).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/53933/elife-53933-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** Best linear predictor of speed based on sample identity (i.e. mean speed within the sample) vs. trajectory speeds. There is both variation in speeds from sample to sample and also a broad distribution of speeds within each sample.

To evaluate the rate of speed switching in our system, we measured the average speeds of individual trajectories on non-overlapping ~20 min intervals, and evaluated how the speed ranks change as a function of the time between intervals (Figure 2B). We found a high correlation between speeds on adjacent non-overlapping intervals, which decays slowly on the timescale of the measurement. Thus each cell samples a characteristic distribution of speeds that is stable over one to two hours. For the remainder of the analysis, we will consider the average speed to be a property of the trajectory; we return to consider the implications of speed switching in the discussion.

We note that we observed variation in the distributions of cell speeds between samples: overall, 48% of the variance in cell speeds can be explained by the sample identity. Nonetheless, the distributions of cell speeds within each sample are broad and overlapping (Figure 2—figure supplement 1), accounting for the majority of the variance (52%). Amongst other effects, sample to sample variation could be the result of differences in antigen environment or global cytokine levels between fish.

### Heterogeneous cell migration statistics fall on a behavioral manifold

Previous work (Maiuri et al., 2015) has suggested that actin flows may generate a coupling between speed and directional persistance in migrating cells. This study generates the hypothesis that cells, in general, are not free to pick any turn and speed statistics, but rather that there may be underlying biophysical constraints. To investigate this hypothesis in our system, we divided the cells into quintiles based on speed, which we refer to as speed classes. We observed strong variation in the distribution of turn angles amongst speed classes (Figure 3A): fast cells are most likely to turn shallowly, slow cells are most likely to turn around, and the distribution varies smoothly across the speed classes. This dependence could be driven by a local coupling between speed and turn angle: cells tend to go straighter whenever they go fast, which the faster cells do more often. Alternatively, it could be driven by an overall behavioral difference between fast and slow cells. To distinguish these possibilities, we measured the average turn angle as a function of the size of the steps surrounding it (Figure 3B). We found that both of these effects contribute: all cells go straighter during faster periods, but for a given step size, slow cells are more likely to turn sharply.

![Figure 3.](https://cdn.elifesciences.org/articles/53933/elife-53933-fig3-v1.jpg)

**Figure 3.:** (A) Distribution of turn angles amongst cells grouped by speed class. The distribution varies smoothly from faster cells, which tend to go straighter, to slower cells, which tend to turn around more often. Error bars represent 95% confidence intervals from a bootstrap over trajectories in each speed class. The legend reports the mean speed for trajectories in each class. (B) Turning behavior conditioned on current cell speed. The average of the cosine of the turn angle as a function of the average length of the steps on either side. Cells are grouped into speed classes as in A. Error bars represent 95% confidence intervals from a bootstrap over trajectories in each speed class. (C) Mean squared displacement by speed class. Due to the variation in turning behavior, the faster cells appear initially more superdiffusive. Error bars represent 95% confidence intervals from a bootstrap over trajectories in each speed class. All speed class calculations were performed on the n = 569 trajectories that included all time intervals in the MSD analysis. (D) Organization of cell behavior into a curve in a three dimensional behavioral space. Each point represents a trajectory, and we show the average speed, turn angle, and local speed-turn correlation. Grey: projection into the x-y plane. The trajectories shown in Figure 2 are colored. Trajectories pooled over n = 16 fish.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/53933/elife-53933-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A) Spline fit to speed-turn angle relationship. (B) The fraction of the variance in the turn angle summary statistic explained by speed (estimated based on the spline fit in A.), by stochasticity, that is variance within a trajectory; and by other factors, which may include imperfections in the spline fit (see Materials and methods).

The relationship between speed and turning suggests that there may also be systematic differences in the scaling of the MSD at short times between cells. In particular, variation in speed alone amongst individuals would not change the shape of the MSD, which would collapse when appropriately scaled (Appendix 1). On the other hand, the systematically shallower turns of faster cells would be expected to boost the slope of their MSD at short times, an effect we observe in the data (Figure 3C).

The analysis at the level of speed classes suggested that there might be a single scalar variable, for which the cell’s average speed is a good proxy, that determines a number of higher-order statistics characterizing the cell’s migration behavior. To test this at the level of individual trajectories, we chose two summary statistics that capture the cell’s turning behavior: the average of the cosine of the turn angles along the trajectory, and the correlation between speeds and turn angles along the trajectory. The former is a summary of the overall distribution of turn angles for that cell, while the latter captures the degree of additional local coupling between speed and turn angle. Together with the cell’s speed, these two summary statistics form a three-dimensional behavioral space. We observed that the cell trajectories fall close to a curve in this space (Figure 3D). In particular, 73% of the variance in the average cosine can be explained by cell speed, with some residual variance due to the stochasticity of the process (7%) and other unknown effects (20%) (Figure 3—figure supplement 1). Thus T cell migration statistics can be organized into a one-dimensional behavioral manifold, characterized by a strong dependence between speed and turning behavior.

### Model predicts wide variation in length scales of exploration across the population

Our observation of a behavioral manifold suggests that, despite the apparent heterogeneity in migration strategies, there may be a common program with a single underlying variable, consistent with the work of Mauri et al. In this view, a cell’s location on the manifold reflects its internal value of this control variable, which in turn dictates its random walk behavior. Given the results of our MSD analysis, to determine candidates for a single-parameter migration model, we started with the canonical persistent random walk (Ornstein-Uhlenbeck) process (Uhlenbeck and Ornstein, 1930):

$$
\frac{d⁢v_{i}}{d⁢t}=-\frac{1}{P}⁢v_{i}+\frac{S}{\sqrt{P}}⁢η,
$$

where v is the velocity, $η$ is a white noise term, and $i$ labels the velocity component. This model has two free parameters: the speed, S, and the persistence time, P, which is the average time before a cell turns. (Note that speeds inherently vary along trajectories in this model; S controls the average speed.) Our observations suggest that there may in fact only be one control parameter; in particular, because faster cells tend to make shallower turns, we expect P to increase with S. To determine the relationship between these two variables, we measured the persistence time, averaged along each trajectory, as a function of cell speed, and found a linear dependence (Figure 4A). This suggests the following simple model of cell motility:

$$
\frac{d⁢v_{i}}{d⁢t}=-\frac{1}{\frac{S}{\alpha}+\beta}⁢v_{i}+\frac{S}{\sqrt{\frac{S}{\alpha}+\beta}}⁢η
$$

![Figure 4.](https://cdn.elifesciences.org/articles/53933/elife-53933-fig4-v1.jpg)

**Figure 4.:** (A) Mean persistence time as a function of cell speed, measured along trajectories (n = 710). Error bars represent 95% confidence intervals from a bootstrap over trajectories. UPT: Uniform persistence time; SPC: Speed-persistence coupling. (B) Scaling of the effective diffusion constant with cell speed. Except for a constant offset, parameters are fixed based on the speed-persistence relationship in A. Error bars represent 95% confidence intervals on a bootstrap over trajectories. Numbers of trajectories in each time interval: n = 704; n = 654; n = 607; n = 558; n = 523. Trajectories were pooled over n = 16 fish.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/53933/elife-53933-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** Panels A,B,D,E as in Figure 3A–D; Panels C,F as in Figure 4A–B; with all statistics re-calculated based on sub-sampling timepoints by a factor of 2. .

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/53933/elife-53933-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** As in Figure 4A, where the persistence time is defined to be the average time before the angle deviates by $\frac{\pi}{6}$.

where $\alpha$ is a constant with units of acceleration, $\beta$ is a constant with units of time, and both are constrained by the empirical relationship in Figure 4A. We call this the speed-persistence coupling model (SPC).

As in other persistent random walk models, SPC walkers are diffusive at long times; the MSD scales linearly with time, and the ratio between these quantities defines an effective diffusion constant (Appendix 1):

$$
D_{e⁢f⁢f}≡\frac{M⁢S⁢D⁢(\tau)}{4⁢\tau}=\frac{1}{2}⁢S^{2}⁢P.
$$

Due to the dependence of P on S, the SPC model predicts a strong scaling of the effective diffusion constant with cell speed. We tested this prediction at several time intervals $\tau$ and found good quantitative agreement between the model and the data (Figure 4B). In particular, heterogeneity in speeds creates a broad range of effective diffusion constants, spanning 2 orders of magnitude. The coupling between speed and persistence amplifies this effect, generating five-fold more variation in the effective diffusion constants across the cells than would be expected for a uniform persistence time model (UPT). We also note that the collapse of $D_{e⁢f⁢f}$ measured at different time lags $\tau$ provides additional corroboration of diffusive (as opposed to Levy/super-diffusive) scaling.

The analyses in this and the previous section depend on measured cell speeds and turn angles, which are an imperfect proxy for the true instantaneous process (Beltman et al., 2009b). In particular, both noise in the cell locations and finite sampling intervals can introduce bias in the measured speeds, which could in principle generate spurious relationships between measured speed and turning behavior. We took two approaches to addressing the sensitivity of our conclusions to these issues. First, we addressed sensitivity to sampling rate by repeating the analyses above, subsampling timepoints by a factor of 2. This makes the turning behavior of the slowest two speed classes harder to distinguish, because they are rarely persistent over more than one timestep (Figure 4—figure supplement 1A,D), and introduces more noise in the local coupling and persistence relationships (Figure 4—figure supplement 1B–C), but otherwise does not alter the structure of the correlations (Figure 4—figure supplement 1A–F). Second, we assessed the potential biases introduced by mislocation noise and finite sampling to the speed-persistence relationship in simulations (Appendix 1, Appendix 1—figure 1). We found that mislocation noise can lead to spurious correlations between speed and persistence at the slow end of the speed spectrum, but cannot account for the consistent correlation we observe across speeds.

Additionally, we note that our measured trajectories stay predominantly within the tail fin and larval fin fold (Figure 1—figure supplement 1), suggesting a boundary between the fin fold and muscle region of the tail. Such a boundary could influence the MSD. However, we compared to the MSD calculated on one held-out sample not subject to these boundary effects and observed no difference (see Appendix 1—figure 2).

Finally, we note that the SPC Langevin model describes the effective diffusive behavior of the trajectories and their scaling at longer times, but may not capture all the details of the microscopic dynamics. In particular, the propensity of trajectories to turn backwards (peak at $\theta=\pi$ radians, Figure 3A) is not captured by this model.

### Manifold is preserved under a drug perturbation to cell speeds, and in mouse T cells and Dictyostelium

We next asked about the robustness of the observed behavioral manifold under a perturbation to cell speeds. Given the role of actin nucleation and remodeling in leukocyte motility (Vicente-Manzanares et al., 2002), we chose the drug Rockout, a known Rho kinase inhibitor affecting this pathway (Barros-Becker et al., 2017), as a candidate for perturbing cell speed, and repeated the measurements and analysis of cell migration behavior in the presence of the drug (Materials and methods). We found that the distribution of cell speeds shifted downwards, but we still observed a quantitatively similar positive relationship between speed and turning behavior (Figure 5A,B). This is consistent with a model where the perturbation primarily shifted an internal cell state variable that determines location along the behavioral manifold, which in turn dictates both speed and turning behavior, although we note that there may be an additional small shift towards shallower turns in the drug condition.

![Figure 5.](https://cdn.elifesciences.org/articles/53933/elife-53933-fig5-v1.jpg)

**Figure 5.:** (A) Correlation between the average cosine of the turn angles along the trajectory and cell speed, for cells in control and Rockout-treatment conditions. Data for all cells is shown as well as a binned average. Error bars represent 95% confidence intervals on the binned average on a bootstrap over cells. (B) The distribution of speeds amongst control and Rockout-treated trajectories. The treatment lowers cell speeds but maintains the relationship between speed and persistence. Statistics based on trajectories pooled over n = 16 control fish (n = 712 trajectories) and n = 6 Rockout treatment fish (n = 236 trajectories). (See also Figure 5—figure supplement 1. (C) As in A, for mouse T cells (data from Gérard et al., 2014). The perturbation is a genetic knockout of a non-canonical myosin motor, Myo1g. E. As in A, for Dictyostelium (data from Dang et al., 2013). The perturbations are a knockout and rescue of the Arp2/3 inhibitor Arpin. (control: n = 42; Myo1g KO: n = 123) (D,F) Distributions of cell speeds for the control and treatment conditions shown in C,E. (WT: n = 42; Arpin KO: n = 38; Arpin rescue: n = 42) In each case, the distribution of speeds shifts, but the cells tend to move along the speed-turn curve. ).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/53933/elife-53933-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** As in Figure 5A,B, but including only those control samples with a paired Rockout treatment sample (n = 6 fish). Fish were imaged for 2.5 hr, and imaging media was replaced with media containing Rockout. Imaging over the same field of view was continued for 2.5 hr.

Finally, we analyzed published data from two other species, mouse T cells in situ (Gérard et al., 2014) and Dictyostelium (Dang et al., 2013), in this framework. While some of the analyses that depend on longer time traces and larger cell numbers are not possible with these datasets, we tested the relationship between average turn angle and cell speed. We found that this correlation held amongst the control cells in both studies (Figure 5C–F). This suggests that, as for zebrafish T cells, there is heterogeneity in speed and turning behavior amongst the cells, and is consistent with a similar behavioral manifold. In the two published studies, genetic perturbations that knocked out or down one member of the actin remodeling machinery were used: a knockout of the non-canonical myosin Myo1g in one case, and a knockout of the Arp2/3 inhibitor Arpin in the other. In each case, the perturbation had a substantial effect on the distribution of cell speeds (Figure 5, E-F). However, in both cases, a quantitatively similar positive relationship between the speed and turning behavior amongst the perturbed cells was preserved.

### Single cell RNA sequencing suggests transcriptional heterogeneity in actin nucleation activity

Our observation that cells maintain characteristic distributions of speeds over periods of a few hours suggests that there may be variation in transcriptional state that underlies some of the heterogeneity in cell migration behavior. To investigate this possibility, we performed single-cell RNA sequencing on cells isolated from the tail of 15 dpf Tg(lck:GFP) zebrafish. To assess the fidelity of the marker, we sorted GFP+ cells from an unbiased FSC/BSC gate (Materials and methods). We used standard dimensional reduction and clustering methods (Materials and methods) to identify 330 putative T cells (Figure 6—figure supplement 1). Unexpectedly, we also identified a population of epithelial cells that may mis-express lck at low levels (Materials and methods, Figure 6—figure supplement 1, Figure 6—figure supplement 2).

We next used a self-assembling manifold algorithm designed to detect subtle variation (Tarashansky et al., 2019) to examine finer-scale structure within the putative T cell cluster. This algorithm revealed a plate effect related to one of our sort plates (Figure 6—figure supplement 3), which we therefore excluded from the remainder of the analysis. We repeated the SAM analysis on the remaining (n = 237) cells, and identified two main subtypes (Figure 6A–B), consistent with a previous report (Tang et al., 2017). We note that the prior study identified the smaller subpopulation as NK cells; however, in addition to the previously-reported marker genes, we find that these cells have moderate expression of the T cell receptor trac. We have therefore chosen not to annotate these as NK cells.

![Figure 6.](https://cdn.elifesciences.org/articles/53933/elife-53933-fig6-v1.jpg)

**Figure 6.:** (A) UMAP dimensional reduction of single-cell RNA sequencing profiles of zebrafish T cells (Materials and methods) shows two main subtypes. Cluster colors are shared across panels A, B, D, and E. For a list of differentially-expressed genes between clusters, see Supplementary file 1. (B) Violin plots of marker genes in common to both subtypes (including immune, T cell, and motility markers), as well as selected marker genes for each subtype. (For the list of differentially-expressed genes, see Supplementary file 1). (C) Distribution of a rank correlation coefficient-related statistic between arpc1b and other moderate and high expressed genes, amongst all T cells (Materials and methods). Statistically significant outliers (after Bonferonni correction) are colored and labeled. The top correlated genes include three also involved in actin nucleation activity. (D) Correlation between expression (counts + 1) of arpc1b and actb2 across the T cells, with colors as in A. (E) Correlation between expression (counts + 1) of arpc1b and cdc24l, with colors as in A. Analysis performed on n = 237 cells (see Main Text, Materials and methods).

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/53933/elife-53933-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** (A) UMAP dimensional reduction of cell gene expression profiles from scRNAseq, with clusters assigned by HDBSCAN (colors). (B) Index sort data of FSC/BSC for these cells (colors correspond to cluster assignments from A). (C) Violin plot of a selection of the differentially-expressed genes between the two clusters (Wilcoxon rank-sum test, see Figure 6—figure supplement 2, Supplementary file 2), as well as a panel of markers associated with other types of immune cells. Genes expressed in the first cluster include immune, T-cell associated, and actin remodeling/motility associated genes. Genes expressed in the second cluster include keratin as well as the epithelial marker ahnak. .

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/53933/elife-53933-fig6-figsupp2-v1.jpg)

**Figure 6—figure supplement 2.:** Differential expression analysis between the two cell clusters in Figure 6—figure supplement 1. Named genes with the top 100 p values are labeled. See also Supplementary file 2.

![Figure 6—figure supplement 3.](https://cdn.elifesciences.org/articles/53933/elife-53933-fig6-figsupp3-v1.jpg)

**Figure 6—figure supplement 3.:** UMAP dimensional reduction of only the T cell cluster, using the self-assembling manifold algorithm, colored by sort plate. This revealed a significant plate effect involving p1. We therefore excluded this plate from further analysis of the fine-scale variation amongst T cells.

Both subpopulations of cells express high levels of genes canonically involved in actin nucleation and remodeling in the leukocyte cytoskeleton (Vicente-Manzanares et al., 2002; Takenawa and Suetsugu, 2007) (WASP/ARP2/3 pathway; Figure 6B); indeed, these genes are amongst the top differentially expressed between the T cells and putative epithelial cells in our sample (Figure 6—figure supplement 1, Figure 6—figure supplement 2). To analyze variation in this pathway amongst the T cells, we chose arpc1b, a subunit of the ARP2/3 complex, as a reference gene because ARP2/3 directly nucleates actin during ameboid cell migration, and its inhibition is known to modulate cell speed (Dang et al., 2013). We tested the rank correlation of expression of all other moderate to high expressed genes with arpc1b (Figure 6C). We found that 3 of the four top correlated genes (those that are statistically significant after Bonferonni correction) are also canonically involved in this pathway: the actin monomer genes act2b and act1b, as well as the upstream activator cdc42l. Unexpectedly, the fourth gene encodes a lincRNA whose biological function is unknown. Thus we detect real, although not strong, co-variation in genes involved with actin nucleation, which may create long-lived cell-intrinsic variation in motility.

While the two T cell subpopulations separate in some dimensions of gene expression space, including, for example, the marker genes shown in Figure 6B, both groups express arpc1b and its correlates. Indeed, the distributions of expression for the two subtypes overlap for these genes (Figure 6D). This is consistent with a single continuous motility axis, without two distinct subgroups, as in our microscopy data.

We have observed transcriptional heterogeneity in actin nucleation genes, which may underly variability in motility states. This observation suggests that cells may vary along a ‘nucleation high’ to ‘nucleation low’ axis, generating a range of long-lived speed states. However, it remains technologically infeasible to directly associate a cell trajectory with a gene expression profile, so a direct test awaits future work. Additionally, we note that regulation that occurs at the protein level, for example through phosphorylation states, is likely very important to shorter timescale variation in cell motility behavior, and is not reflected in gene expression.

## Discussion

We have measured and analyzed the variability in cell motility amongst the T cells of the zebrafish tail. We found that cell motility statistics are inconsistent with Levy flight; rather, speeds are heterogeneous from cell to cell. We note that a previous study that reported modified Levy flight in T cells (Harris et al., 2012) was carried out in a very different biological context (adoptively transferred CD8+ T cells in mouse CNS in the presence of an infection), which could drive differences in motility behavior. However, we note that the statistics of our trajectories closely resemble those measured by Harris et al. up through the 10 min time lag analyzed in that study.

We also found that migration statistics from zebrafish T cells as well as mouse T cells and Dictoystelium fell on a behavioral manifold, characterized by a coupling between speed and directional persistence. We note that, in general, heterogeneity of motility behavior across a population could be caused by the tissue context rather than by cell-intrinsic factors. However, the effects of the drug perturbation, as well as the effects of the genetic perturbations from Gérard et al., 2014 and Dang et al., 2013, support a cell-intrinsic basis for the behavioral manifold we observe here. In particular, we performed trials in which the same regions of tissue were imaged and cells tracked before and after addition of the drug (Figure 5—figure supplement 1); the observed changes in migration statistics must then be caused by the drug’s effect on the cell’s internal state, not by the tissue context.

The drug perturbation experiment and analysis of data from the other species suggests that there is one underlying cell-intrinsic variable that jointly controls speed and directional persistence. Maiuri et al. also observed a coupling between speed and directional persistence across multiple cell types, and performed elegant in vitro work to demonstrate that actin retrograde flow speed is correlated both with cell speed and persistence time (Maiuri et al., 2015). Using single cell RNA sequencing, we observed covariation amongst T cells in a group of genes involved in actin nucleation. This suggests that cells vary transcriptionally in their actin nucleation activity. Levels of these genes may represent an underlying cell control variable that determines actin retrograde flow speeds and hence both cell speed and persistence. A direct test of this hypothesis awaits development of techniques to link a single cell’s trajectory and its gene expression profile.

In two previous studies, genetic perturbations were performed that made cells faster and more persistent on average (Gérard et al., 2014; Dang et al., 2013). Our results suggest that this connection may be general to the cells rather than specific to the perturbation. In particular, shifts in the average turning behavior have been used to argue that Arpin and Myo1g control cell steering. Our analysis suggests that increasing cell speed may in many cases increase straightness, and vice versa, so that the effect on cell steering may be indirect.

We have analyzed cell migration in the context of a speed-persistence coupling model, which is a modified Orenstein-Uhlenbeck model where the speed and persistence time parameters are explicitly co-dependent. We chose this as the minimal model that captures both the diffusive behavior at long times and the coupling between speed and persistence, allowing for a prediction of the range of effective diffusion constants, and hence length scales of exploration, amongst the cells (Figure 4). Another feature of measured trajectories, in previous studies and in our work, is variation in speed along the trajectory, sometimes referred to as intermittency. We note that the Langevin dynamics of the SPC model inherently generate variation in speed, including pauses, along trajectories: the speed parameter sets the distribution of instantaneous speeds sampled by the cell. Other approaches have included adding pauses to a model with a fixed distribution of step sizes (Harris et al., 2012). Maiuri et al. considered an explicitly active model where actin dynamics within the cell generated motility. While slightly more complex, this model has several interesting features, including that the cell motility emerges from internal biophysical mechanisms, and also that it produces multiple phases of migratory behavior, including one with additional intermittency (Maiuri et al., 2015). Future work could use transgenic methods to label actin in the zebrafish to directly test this active matter model in vivo. Another mechanistic basis for intermittency was demonstrated by Dong et al., 2017, who showed that spontaneous cytosolic calcium signaling generates pauses during basal T cell motility. Investigation of this mechanism and its potential role in producing the speed fluctuations observed in our system would also be an interesting subject for further work.

Our results show that across the population, cells explore over a very broad range of length scales, covering orders of magnitude of variation in effective diffusion constants. This variability is driven primarily by differences in average speed between cells, which is amplified by the observed coupling between speed and persistence. However, analysis of the effectiveness of this variation as a search strategy, as compared with modified Levy flight (Harris et al., 2012) or models with additional intermittency (Maiuri et al., 2015), would require a detailed knowledge of the distribution of targets in the tissue as well as an additional order of magnitude in time of observation of the cell trajectories in our system, to fully characterize the slow timescale speed switching. We additionally note that several studies (Dustin et al., 1997; Mempel et al., 2004; Kawakami et al., 2005; Castellino et al., 2006; Moreau et al., 2015; Dong et al., 2017; Negulescu et al., 1996) have indicated that T cells react to local chemical signals by changing speed–in particular, that calcium signaling can cause cell arrest, and this is important to contact with antigen presenting cells and antigen recognition. This suggests that the local signaling environment may also be important to shifting the cell behavior along the manifold. Detecting these signaling and recognition events in vivo in real time would be an exciting avenue for future work.

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
      <td>Strain, strain background (Danio rerio)</td>
      <td>Tg(lck:GFP)</td>
      <td>Gift from Aya Ludin-Tal and Leonard Zon Langenau et al., 2004</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Tricaine-S, MS-222</td>
      <td>Pentair</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Rockout</td>
      <td>Sigma Aldrich</td>
      <td>#555553</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Ilastik</td>
      <td>Sommer et al., 2011</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Custom analysis software</td>
      <td>This paper</td>
      <td></td>
      <td>Available at https:// github.com/ erjerison/ TCellMigration</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>STAR</td>
      <td>Dobin et al., 2013</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>htseq</td>
      <td>Anders et al., 2015</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>SAMalg</td>
      <td>Tarashansky et al., 2019</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

### Zebrafish lines and procedures

Tg(lck:GFP, roy-/-, nacre-/-) zebrafish (Danio rerio) (Langenau et al., 2004) were obtained as a generous gift from Dr. Leonard Zon and Dr. Aya Ludin-Tal. Imaging was performed on Tg(lck:GFP) zebrafish crossed into a nacre-/- background, at between 9 and 13 dpf. All adult and larval zebrafish were maintained according to protocols approved by the Stanford Administrative Panel on Laboratory Animal Care.

### Microscopy

Imaging was performed on a single-plane illumination microscope constructed as specified in Pitrone et al., 2013, with the exception that a Prior ProScan XY stage (Prior Scientific) coupled to a Zaber T-LLS 105 stage (Zaber Technologies) was used for sample movement. The light sheet was generated using an Olympus UMPLFLN10XW objective (NA = 0.3) and detection was performed with an Olympus UMPLFLN20XW objective (NA = 0.5) and an achromatic doublet tube lens (AC508-180-A-ML, Thorlabs). Images were recorded either on a Retiga 2000R camera (Qimaging) or an Ace acA2040 (Basler). For the Ace ac2040 camera, a meniscus lens (LE1418-A - O2’ N-BK7, Thorlabs) was added as a zoom lens, to match the image pixel width between the two cameras at $.37⁢\mu⁢m$. The fluorescence source was an Obis LS 488 nm laser (Coherent), and the microscope was controlled by Micro-Manager.

Zebrafish between 9 and 13 dpf were anesthetized with Tricaine-S (MS-222, Pentair; .008% w/v, buffered to pH 7) and embedded in 2% low melting point agarose (Lonza SeaPlaque, #50100) with .004% w/v Tricaine. For imaging, the agarose was submerged in E3 with .008% w/v Tricaine and 50 mM Hepes. With the exception of Figure 2 and Figure 2—video 1, tiled z-stacks were obtained every 45 s for at least 180 timepoints, with a field of view of at least 592 $\mu⁢m$ (dorsal-ventral axis) by 1200 $\mu⁢m$ (anterior-posterior axis), in the tail region posterior to the anus. For Figure 2A and Figure 2—video 1, a z-stack was obtained every 12 s for 1100 timepoints, with a field of view of 757 × 568 µm (the first 900 timepoints are shown). For statistical comparison with the remainder of the data, trajectories from this final dataset were subsampled in time to give 48 s timesteps. Data was acquired with 2 × 2 binning, for an image pixel width of .74 µm.

For imaging in the presence of Rockout, embedded fish were submerged in E3 with .008% w/v Tricaine and 50 mM Hepes plus 12 µM Rockout (Sigma Aldrich #555553). For paired control/Rockout trials, fish were imaged for 2.5 hr in control conditions, followed by 2.5 hr in Rockout conditions over the same field of view.

### Single-cell RNA sequencing

Thirty 15 dpf Tg(lck:GFP) zebrafish were euthanized using .04% w/v Tricaine and transected posterior to the anus. Tail portions were pooled into HBSS (ThermoFisher #14025092) on ice. Tails were dissociated by incubating with 100 $\mu⁢g/m⁢L$ Liberase-TL (Sigma Aldrich #5401020001) at room temperature for 20 min, followed by trituration with a 23 gauge needle. The cell suspension was filtered through a 40 $\mu⁢m$ filter and washed once in HBSS. GFP+ cells were sorted from an unbiased FSC-SSC gate on a Sony SH800 cell sorter into 384-well hard-shell PCR plates (Bio-Rad HSP3901) containing .4 µl of lysis buffer, prepared as described previously (Tabula Muris Consortium et al., 2018). Reverse transcription following a Smart-Seq2 protocol, and Illumina library preparation, were carried out as described previously (Tabula Muris Consortium et al., 2018), except that following cDNA amplification, cDNA was diluted uniformly to a mean target concentration of $.4⁢n⁢g/\mu⁢l$ for library preparation. Libraries were sequenced on the NovaSeq 6000 Sequencing System (Illumina) using 2 × 100 bp paired-end reads.

### Image processing and cell tracking

Tiles were assembled based on recorded stage coordinates and a Maximum Z projection was applied to Z stacks. Sample drift in x and y was subtracted by identifying and tracking autofluorescent pigment spots. In particular, the coordinates of 1–3 isolated pigment spots were identified manually at the first timestep; at each timestep, the brightness centroid was computed for a circle with a 25 pixel radius around the previous centroid, and the average trajectory of the pixel spots was rounded to the nearest pixel and subtracted from the timeseries. Prior to cell segmentation, the average image across the whole timecourse was subtracted from each timestep. For data recorded on the Retiga 2000R camera, prior to segmentation the image was thresholded at the 30th pixel percentile and the maximum pixel value was fixed so that .4% of pixels were saturated. For data recorded on the Basler Ace acA2040 camera, no lower threshold was used and the maximum pixel value at each timepoint was fixed so that .2% of pixels were saturated. Ilastik software (Sommer et al., 2011) was used for cell segmentation and tracking: the Ilastik pixel classification module was used to classify foreground and background, and the manual tracking module was used to identify and track cells. Tracks were terminated if two segmented cells collided and it was not possible to disambiguate, or if a segmented cell was lost due to passing into an autofluorescent region or due to imperfections in segmentation and/or illumination. To define trajectories, the brightness centroid of each cell in x and y at each timestep was computed from Ilastik tracking masks and the Maximum Z projection. Processing steps not using Ilastik were performed using Python 3.6 (code available at: https://github.com/erjerison/TCellMigration; Jerison, 2020; copy archived at https://github.com/elifesciences-publications/TCellMigration).

### Trajectory analysis

Trajectories with at least 30 consecutive steps were included in the analysis; for MSD calculations, trajectories that included all time intervals were included. For calculations of power spectra, single missing timesteps were linearly interpolated based on the two adjacent positions, and computations were performed on the longest consecutive segment for each trajectory. For the M. musculum data, the time interval was 30 s. For the Dictyostelium data, timesteps were subsampled from the original to give an interval of 20 s. Unless otherwise noted, statistics are reported as the median of the statistic on a bootstrap over trajectories.

Mean-squared displacements were computed along each trajectory as:

$$
MSD(\tau=mt_{i⁢n⁢t})=\frac{1}{N-m}\sums=1N-m||x→(m+s)-x→(s)||^{2},
$$

where $N$ is the total number of timesteps and $t_{i⁢n⁢t}$ is the time interval. The overall MSD was computed by averaging the MSDs for each trajectory, and 95% confidence intervals were calculated via a bootstrap over trajectories.

The overall MSD was fit to:

$$
M⁢S⁢D⁢(\tau)=4⁢S^{2}⁢P⁢\tau⁢(1+\frac{P}{\tau}⁢(e^{-\frac{\tau}{P}}-1))+\sigma^{2},
$$

which we note is the common formula for mean squared displacement in both the Ornstein-Uhelnbeck model (see Appendix 1) and in the Kratky-Porod wormlike chain model. Unless otherwise noted, fitting was performed using the scipy.optimize.curvefit function in scipy 1.3.0; fitting was performed in log space and weighted by computed confidence intervals.

The velocity power spectrum was computed based on the vector of secant-approximated velocities for each trajectory. Velocity vectors were zero-padded to 400 timesteps, and the fourier transforms of the velocity components were computed using the the fft function in numpy (1.16.4). Letting the fourier-transformed velocity components for trajectory $m$ be $v_{x}⁢(k,m)$, $v_{y}⁢(k,m)$, the power spectrum for each trajectory was computed as:

$$
PSD(k,m)=\frac{1}{N^{2}}\frac{N}{N_{m}}\sumi=x,y(||v_{i}(k,m)||^{2}+||v_{i}(N−k,m)||^{2}),1<k<\frac{N}{2}
$$



$$
PSD(0,m)=\frac{1}{N^{2}}\frac{N}{N_{m}}\sumi=x,y||v_{i}(0,m)||^{2}
$$



$$
PSD(\frac{N}{2},m)=\frac{1}{N^{2}}\frac{N}{N_{m}}\sumi=x,y||v_{i}(\frac{N}{2},m)||^{2},
$$

where $N=400$ and $N_{m}$ is the length of trajectory $m$. The overall PSD was computed as the average over the PSDs for each trajectory:

$$
P⁢S⁢D⁢(k)=\frac{1}{n}⁢\summ=1nP⁢S⁢D⁢(k,m),
$$

where $n$ is the number of trajectories. For Figure 1D, a piecewise linear function was fit to the PSD in log space; we plot the high-frequency fitted line and a line with slope 0.

Following (Petrovskii et al., 2011), we calculated the distribution of bout lengths within a trajectory as the distribution of x displacements between reversals in direction in x, divided by the average of these displacements within each trajectory. The distribution was calculated using the numpy.histogram function on percentile bins with the option density = True; the x locations of points were determined based on the average value of points in each bin. We fit the distribution to a stretched exponential function $f⁢(x)=A⁢e^{-\gamma⁢x^{\beta}}$; the fitted value of the stretch parameter $\beta$ was .9.

The overall speed distribution was computed by collecting secant-approximated speeds across all trajectories and timepoints; similarly, the overall turn angle distribution was computed by collecting all relative angles between consecutive segments. For the Kolmogorov-Smirnov (KS) test, the overall CDFs of speeds and turn angles were estimated by measuring the cumulative frequency over 25 percentile bins and performing linear interpolation to yield a continuous function. A two-sided KS test (scipy.stats.kstest) was performed for the sets of speeds and turn angles of each trajectory.

We evaluated the fraction of the variance in cell speeds that can be explained by sample identity by fitting a linear model with indicator variables on the sample identity as predictor variables. We used the LinearRegression function of sklearn.linear_model to fit the model, and the ‘score’ method to evaluate $R^{2}$, the fraction of the variance explained by this model.

Turn angle distributions for each speed class were computed by collecting all relative angles between consecutive segments amongst cells in that speed class; the distributions were symmetric about θ = 0 and so were folded to be between 0 and $\pi$ radians. 95% confidence intervals were calculated based on a bootstrap over trajectories in each speed class. For the relationship between local speed and turn angles (Figure 2B), the local speed was estimated as the average speed of the two consecutive steps surrounding a turn. Turns were binned based on the local speed, and the average of the cosine of the turn angles was computed for each bin. For this and other binned statistics, the x location of the bin was fixed to be the average value for the points in that bin.

To estimate the rate of speed switching, all trajectories of at least 117 min in length were used. The average speed of each trajectory was measured on 19.5 min intervals; 19.5 min was chosen to minimize the bias-variance trade-off. Specifically, because every cell samples speeds from a distribution, there is trade-off between measuring speeds on intervals that are too short, which may not give a good estimate of the mean, and intervals that are too long, where cells may switch during the interval. To minimize this trade-off, the interval that maximized the rank correlation between adjacent non-overlapping blocks was used. The average speed of each cell was measured on non-overlapping intervals, and the Spearman rank correlation coefficient between all pairs of intervals was computed. The correlation as a function of time was calculated as the average over all pairs of intervals with the same difference in start times. We computed 95% confidence on a bootstrap over trajectories. For the null model, we permuted speeds amongst the trajectories on each interval; we calculated 95% confidence intervals over the permutations.

For Figure 3, the average of the cosine of turn angles between adjacent steps was calculated for each trajectory, as well as the average over all adjacent steps of the secant approximated speeds. For Figure 3D, the correlation between local speed and turns was computed as the Pearson correlation coefficient between the local speed, as defined above, and turn angles across the set of adjacent steps in the trajectory.

To estimate the fraction of the variance in turning behavior explained by the cell speed, we fit a spline curve (UnivariateSpline class of scipy 1.3.0; default parameters) to the relationship between speed and the average of the cosine of the turn angles (Figure 3—figure supplement 1A). Letting the spline function be $f$, we estimated the variance accounted for by the speed as $V_{s}=V⁢a⁢r⁢(f⁢(S_{m}))$, where the index $m$ labels trajectories. We estimated the variance in the means due to variation within trajectories, which we called stochasticity, as $V_{s⁢t}=\frac{1}{n}⁢\sum_{m=1}^{n}\frac{1}{k_{m}-1}⁢V⁢a⁢r_{j}⁢(cos⁡\theta_{j⁢m})$, where $n$ is the total number of trajectories, $k_{m}$ is the number of turn angles within trajectory $m$, and $cos⁡\theta_{j⁢m}$ is the cosine of the turn angle $j$ in trajectory $m$. Remaining variance we classified as other (Figure 3—figure supplement 1B); this may be due to imperfections in the spline model, other experimental noise, or additional biological variability.

The persistence time was defined to be the time elapsed before the trajectory turns at least $\frac{\pi}{2}$ radians, averaged along the trajectory. Specifically, letting the displacement between timepoints $s$ and $s+1$ be $x→⁢(s)$, the persistence time along each trajectory was calculated as:

$$
P~=\frac{1}{n}⁢\sums=1n\tau⁢(s),\tau⁢(s)=\sumt=sm-1t_{i⁢n⁢t}
$$

where $m>s$ is the first timestep for which $x→⁢(s)⋅x→⁢(m)<0$, $t_{i⁢n⁢t}$ is the time interval, and $n$ is the final base point for which $m\leqN$, where $N$ is the final timepoint. For Figure 4A, trajectories were binned into mean speed deciles, and the average persistence time was calculated over trajectories in the bin; error bars represent 95% confidence intervals on a bootstrap over trajectories. We also repeated this analysis to measure the average time elapsed before the trajectory turns at least $\frac{\pi}{6}$ radians (Figure 4—figure supplement 2).

The effective diffusion coefficient at time $\tau$ was measured as:

$$
D_{e⁢f⁢f}⁢(\tau)=\frac{M⁢S⁢D⁢(\tau)}{4⁢\tau}.
$$

To measure $D_{e⁢f⁢f}⁢(\tau)$ as a function of $S$, cells were divided into speed bins (with 5% of the speed distribution per bin); $D_{e⁢f⁢f}⁢(\tau)$ for each speed bin was measured by averaging the $D_{e⁢f⁢f}⁢(\tau)$ across trajectories, and error bars were computed based on a bootstrap over all trajectories. Note that $D_{e⁢f⁢f}⁢(\tau)$ will be independent of $\tau$ only if diffusion scaling is respected, so that the collapse of the data in Figure 4B is additional corroboration that the trajectories behave diffusively at long times.

As shown in the models section of the SI below, under the UPT model:

$$
D_{e⁢f⁢f}∝S^{2},
$$

whereas under the SPC model,

$$
D_{e⁢f⁢f}∝S^{2}⁢(\frac{S}{\alpha}+\beta),
$$

where $\alpha$ and $\beta$ are fixed across all trajectories. We fixed $\alpha$ and $\beta$ by fitting a line to the persistence time relationship in Figure 1C; note that this is a short-time statistic and need not a priori predict the effective diffusion constant at longer times. We fit the UPT model (dashed line) and the SPC model (solid) to the measured $D_{e⁢f⁢f}$ as a function of $S$; in both cases, there was one fitting parameter which was the constant of proportionality, which allows for an offset on the y-axis in log space but does not change the shape of the curve.

### Analysis of scRNAseq data

Reads were aligned to the Zebrafish reference genome (genome release: GRCz10; annotations: GRCz10.85) using STAR (2.5) Dobin et al., 2013; reads aligned to each gene were counted using the htseq-count function of HTseq (0.8.0) Anders et al., 2015, with the options -m intersection-nonempty and –nonunique all. Note that the final option counts reads that align to a location with more than one annotated feature (e.g. overlapping ORFs) as belonging to both features. This is necessary because of mis-annotation of the T cell receptor light chain constant region in the zebrafish reference genome; both ENSDARG00000075807 (traj39) and ENSDARG00000104132 (traj28) contain the trac, so that reads mapping to trac would otherwise be discarded.

Cells were filtered if they expressed fewer than 650 genes or more than 3250 genes, and if more than 8% of reads were of mitochondrial origin. We used UMAP (0.3.1) with the default options to embed the log-transformed counts table in two dimensions, including all genes expressed in at least 10% of cells; and HDBSCAN (0.8.22) with min_samples = 10 to call clusters (Figure 6—figure supplement 1A). Comparison with the index sort data (Figure 6—figure supplement 1B) showed that cells from the larger cluster had FSC-BSC consistent with lymphocytes, whereas cells from the other cluster had higher FSC and BSC. We called the major cluster as the first cell group, excluding the 4 cells with $BSC>2\times10^{5}$, and other cells as the second group. We measured differential expression of genes between the two clusters as: $D=\frac{1}{n}⁢\sum_{i=1}^{n}log_{2}⁡(E_{1⁢i})-\frac{1}{m}⁢\sum_{i=1}^{m}log_{2}⁡(E_{2⁢i})$, where $E_{1⁢i}$ are expression values, in counts per million (CPM) + 1, for the first cluster, $n$ is the number of cells in this cluster, $E_{2⁢i}$ are expression values (in CPM+1) for the second cluster, and $m$ is the number of cells in this cluster. (Note that this is the log of the ratio of the geometric means within each cluster.) In Supplementary file 2, we report the genes with $D>log_{2}⁡10$ and $p<.01$ (Wilcoxon rank-sum test, Bonferonni-corrected.) Genes enriched in the larger cluster included the T cell and immune-related genes tagapa, tagapb, ccr9a, tnfrs9b, il2rb, and ptprc (Tabula Muris Consortium et al., 2018); we also tested for expression of the T cell receptor light chain constant region (trac; expression estimated based on the expression of ENSDARG00000075807). Based on these markers, we identified the larger group (n = 330) as T cells. The significantly differentially expressed genes enriched in this group also included arpc1b, wasb, arhgdig, coro1a, scinlb, and capgb, which we classified as belonging to the WASP/ARP2/3 pathway based on the literature (Vicente-Manzanares et al., 2002). Finally, we observed very little expression of markers associated with other types of immune cells (the B cell light chain igic1s, the B cell marker ccl35.2, and the neutrophil and macrophage markers mpeg1 and mpx (Tang et al., 2017) in either group (Figure 6B, Figure 6—figure supplement 2). The genes most significantly enriched in the non-T cell group include keratin proteins (krt8, KRT1), as well as ahnak (Figure 6—figure supplement 2, Supplementary file 2). Based on these markers, we identified these cells as epithelial cells, possibly keratinocytes (Tabula Muris Consortium et al., 2018). We note that we observed GFP signal in the somite region of the Tg(lck:GFP) tail via microscopy (see, e.g., Figure 1A and Movie S1) which we did not observe in wildtype nacre-/- zebrafish, suggesting that these cells may mis-express the marker.

To analyze finer-scale variation within the T cell cluster, we used the self-assembling manifold algorithm method from Tarashansky et al., 2019. We first used the SAM algorithm with parameters thresh = 0.1 and k = 10 to perform dimensional reduction. Visualization of a UMAP projection together with the labels from our sort plates (Figure 6—figure supplement 3) showed that there was a plate effect related to p1; we excluded this plate from the remainder of the analysis. We re-ran the SAM algorithm using the remaining (n = 237) T cells, with parameters thresh = 0.1, k = 10, to produce the dimensional reduction shown in Figure 6A. Cluster labels were assigned using the KMeans class in sklearn.cluster. We measured differential expression of genes between the two subtypes as described above. In Supplementary file 1, we report the genes with $D>log_{2}⁡10$ and $p<.01$ (Wilcoxon rank-sum test, Bonferonni-corrected), for the two subtypes. In Figure 6B, we show a subset of markers associated with the whole T cell cluster, as well as selected marker genes between the two subtypes.

To identify potential co-variation with arpc1b expression amongst the T cells, we computed the Spearman rank correlation between expression of arpc1b (in counts per million) and all other genes expressed in at least 20% of cells. In each calculation of pairwise correlation coefficient, we excluded cells with zero counts for both genes to avoid biasing correlations upwards due to spurious points at the origin. We calculated p values using a permutation test: we permuted cell labels and re-calculated all correlation coefficients; p-values were calculated as the proportion of observations of a correlation coefficient higher than the observed coefficient, multiplied by the number of genes tested (Bonferonni correction).
