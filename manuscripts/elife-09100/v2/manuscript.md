# NF-κB oscillations translate into functionally related patterns of gene expression

## Authors

- Samuel Zambrano<sup>1</sup>
- Ilario De Toma<sup>2</sup>
- Arianna Piffer<sup>2</sup>
- Marco E Bianchi<sup>1</sup> ([ORCID: 0000-0002-5329-6445](https://orcid.org/0000-0002-5329-6445)) †
- Alessandra Agresti<sup>1</sup> ([ORCID: 0000-0001-5006-9506](https://orcid.org/0000-0001-5006-9506)) †

### Affiliations

1. Division of Genetics and Cell Biology San Raffaele Scientific Institute Milan Italy
2. San Raffaele University Milan Italy

† Corresponding author

## Abstract

Several transcription factors (TFs) oscillate, periodically relocating between the cytoplasm and the nucleus. NF-κB, which plays key roles in inflammation and cancer, displays oscillations whose biological advantage remains unclear. Recent work indicated that NF-κB displays sustained oscillations that can be entrained, that is, reach a persistent synchronized state through small periodic perturbations. We show here that for our GFP-p65 knock-in cells NF-κB behaves as a damped oscillator able to synchronize to a variety of periodic external perturbations with no memory. We imposed synchronous dynamics to prove that transcription of NF-κB-controlled genes also oscillates, but mature transcript levels follow three distinct patterns. Two sets of transcripts accumulate fast or slowly, respectively. Another set, comprising chemokine and chemokine receptor mRNAs, oscillates and resets at each new stimulus, with no memory of the past. We propose that TF oscillatory dynamics is a means of segmenting time to provide renewing opportunity windows for decision.

## Introduction

Genetic circuits are instrumental for cells to provide adequate transcriptional responses to different external and internal stimuli, but we are still far from a complete understanding of how they work. The growing availability of single-cell measurements is bringing unprecedented insights into the dynamics of transcriptional responses: although it was traditionally thought that gene circuits should provide a temporally stable response to constant external stimuli, there is increasing evidence that the dynamics of gene circuits is more elaborate, and is often characterized by pulses of activity (Levine et al., 2013). A special case is oscillatory dynamics, in which the activity of some element in the genetic circuit varies periodically, and so does the output of the circuit. Paradigmatic oscillatory dynamics are associated with circadian clocks, which are present in a wide variety of organisms that synchronize their activities to the periodic variation in external daylight (Bell-Pedersen et al., 2005). However, oscillatory dynamics with periods far shorter than 24 hr have been reported in genetic circuits of bacteria (Suel et al., 2007), yeast (Cai et al., 2008; Hao and O'Shea, 2012) and mammalian cells (Geva-Zatorsky et al., 2006; Hoffmann et al., 2002; Larson et al., 2013; Nelson et al., 2004; Shankaran et al., 2009).

The dynamics of transcription factors in gene circuits can play a key role in information transmission through biochemical networks (Selimkhanov et al., 2014) by selectively modulating the expression of different genes (Purvis and Lahav, 2013). A paradigmatic example is how different p53 dynamics can selectively activate transcriptional programs that commit the cell to different cell fate decisions (Purvis et al., 2012).

A property of free oscillating systems (or free oscillators, as analogy to simple mechanical oscillators such as the pendulum) is entrainment, by which an oscillator can gradually modulate its phase and frequency thanks to a small perturbation (forcing) that is itself periodic and oscillating with a period resonant with the intrinsic period of the oscillator (Pikovsky et al., 2003). A common forcing can also lead to the synchronous dynamics of multiple oscillators and thus to collective dynamical states. Entrainment was successfully reproduced in synthetic genetic oscillators, in which single bacterial cells (each expressing a fluorescent reporter protein in response to a synthetic genetic circuit) were entrained collectively to an oscillating provision of arabinose (Mondragon-Palomino et al., 2011). The forcing to one oscillator can also be provided by other oscillators, and this coupling can lead to the emergence of different collective dynamical states characterized by different synchronous dynamics (Pikovsky et al., 2003). Inter-cellular coupling has indeed been exploited to genetically engineer synchronous quorum sensing genetic oscillators in bacteria (Danino et al., 2010). On the other hand, intra-cellular coupling leads to locked oscillatory states for different cell oscillators, as recently shown for the circadian rhythm and the cell cycle (Bieler et al., 2014).

In mammalian cells, NF-κB is a typical transcription factor that displays intrinsic oscillatory behavior. NF-κB plays key roles in inflammation, immune responses, development and cancer (Chaturvedi et al., 2011; Ghosh and Hayden, 2008; Karin, 2006; Ledoux and Perkins, 2014; Naugler and Karin, 2008). Strictly speaking, NF-κB is a family of dimers encoded by 5 different genes, but in what follows we will refer to p65/RELA independently of the dimer it forms. In resting cells, p65 exists mostly within a cytoplasmic complex bound to the IκB inhibitors (Hoffmann et al., 2002). Inflammatory signals like tumor necrosis factor alpha (TNF-α) or lipopolysaccharide (LPS) induce phosphorylation of IκB proteins by IKKs–upstream kinases in the signaling pathway–, ubiquitination and degradation of IκBs, and the release of active NF-κB that translocates into the nucleus to activate the expression of several genes, including those encoding for the IκB inhibitors (Hoffmann et al., 2002). Re-expression of IκBs contributes to relocate NF-κB in the cytoplasm, which is an inhibitory feedback loop for the system. A second feedback loop is centred on the protein A20 (Ashall et al., 2009), which upon activation of the system inhibits the IKKs. Thus, these two layers provide a nonredundant regulation of NF-κB response to external stimuli (Werner et al., 2008). Of note, the IκB inhibitors also show variable sensitivity to different stimuli and respond on different timescales to fine-tune the signaling pathway (Paszek et al., 2010; Shih et al., 2009). This system of negative feedback loops (summarized in Figure 1A upper panel) provides both a tight control of the response to external stimuli and flexibility. As a consequence of this complex wiring, upon constant stimulation the nuclear concentration of NF-κB in each cell oscillates with heterogeneous dynamics according to each cell’s susceptibility and to the inherent stochasticity of the system (Nelson et al., 2004; Tay et al., 2010; Zambrano et al., 2014a). Due to such asynchrony at the single cell level, the NF-κB response appears almost non-oscillating at the cell population level (Hoffmann et al., 2002), and it is difficult to correlate NF-κB oscillatory profiles with gene expression outputs.

![Figure 1.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig1-v2.jpg)

**Figure 1.:** (A) The activity of NF-κB is regulated through different negative feedbacks provided by the inhibitors IκB and A20. The scheme at the bottom represents a generic forcing with periodically alternating TNF-α doses D1 and D2 of duration T2+T1 = Tf; Tf is the period of the forcing. (B, C) Oscillations observed in three GFP-p65 cells obtained by computing the nuclear to the cytoplasmic GFP intensity (NCI) for constant flow of 10 ng/ml TNF-α (B) and upon alternating doses D1=10 ng/ml TNF-α, D2=0 ng/ml and T1=T2 =45 min (C). Each colour corresponds to a single cell trace. Oscillatory patterns can be effectively visualised using the phase ϕ of the oscillation, which is 2π in the maxima of the oscillatory peaks (yellow) and π in the local minima (green) in the colour phase-plot of ϕ(t) below the panels. Scale-bar for ϕ is on the right. (D) Time lapse images of cells under constant stimulation displaying the characteristic heterogeneous nuclear-to-cytoplasmic translocations. (E) Phase plot drawn for 50 cells, of 105 analysed, showing the asynchrony of the oscillations except for the first peak. (F) Distribution of the experimentally computed period of the oscillations Texp, measured as the time between two consecutive oscillatory peaks. The distribution has a maximum at T0 =90 min, which corresponds to the natural period. (G) Quantification of the height for each peak. (H) Time lapse images of the cells under periodic stimulation, showing synchronous NF-κB translocations between cytoplasm and nucleus. (I) Phase plot for 50 cells, of 206 analysed, showing a clear synchrony of the oscillations. (J) Distribution of the period of the oscillations Texp. Texp corresponds almost perfectly to the period of the forcing. (K) Quantification of peaks height variation as described in G; values for n>1 are slightly higher than those observed under constant stimulation. Figure supplements from 1 to 10 are provided.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) GFP-p65 MEFs are plated in a microfluidics plate chamber. The perfusion barrier is visible. (B) TNF-α flows and diffuses inside the chamber through the perfusion barrier, minimizing cells’ shear stress. (C) Example of the nuclear segmentation. A square of the cytoplasm around the nucleus is used to compute the nuclear to cytoplasmic ratio of the intensities, an internally normalized measure. (D) The cells were subjected to two pulses of TNF-α of 30 min separated by a washout of 12 hr. The resulting time series shows that cells responded to both pulses with similar intensity, indicating a negligible degradation of TNF-α in our system.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) Distribution of the noisy peaks values for unstimulated (blue) and stimulated cells (red). A threshold θ=0.15 is enough to discriminate significant peaks from noisy peaks. (B) Peaks (blue triangles) detected in a typical time series and (C) Phase of the oscillation inferred from the same time series. (D) Selected NCI profiles upon automatic segmentation display a variety of dynamical phenotypes, including the previously oscillating and non oscillating cells.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** (A) NCI (nucleus to cytoplasm intensity) time series (green) and average (black) for cells under a continuous flow of 10 ng/ml TNF-α. Same cells as in Figure 1. (B) Distribution of peak numbers in 12 hr timespan for the cells in A: the average number of peaks (n=4) indicates that there are no sustained oscillations in the 12 hr. (C) NCI time series (green) and average (black) for cells stimulated with repeated pulses of 45 min of 10 ng/ml TNF-α followed by a 45 min wash-out. (D) The average number of peaks of these cells in 12 hr (close to 8) indicates that NF-κB shows sustained oscillations under pulsed stimulation.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** Green arrows from NF-κB indicate the contribution of NF-κB to the gene activation while red lines from IκBα represent the contribution to transcriptional repression. The red line from A20 represents the inhibition of IKK activation. This model gives rise to different dynamics for constant stimuli: damped oscillations that converge to a fixed point and sustained oscillations around an unstable fixed point as shown in Figure 1—figure supplement 5.

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig1-figsupp5-v2.jpg)

**Figure 1—figure supplement 5.:** (A) Real and imaginary parts of each eigenvalue of the fixed points of the NF-κB dynamical system. Red dots are for eigenvalues of unstable fixed points, corresponding to sustained oscillations. (B) The distribution of the number of imaginary eigenvalues in fixed points obtained from our set of parameter combinations. Most fixed points have four or more negative eigenvalues, indicating the coexistence of two or more characteristic frequencies. The distribution of the number of positive real parts of eigenvalues in fixed points obtained from our set of parameter combinations. This distribution suggests that sustained oscillations might be infrequent (right). (C) Mean and standard deviation of the parameter values giving rise to oscillating (red) and nonoscillating (blue) trajectories. The intervals are very similar except for parameters n and dA involved in the A20 negative feedback. (D) Examples of the variety of trajectories found in our numerical exploration, including oscillatory trajectories (red) with different peaks and a variety of damped oscillating and non-oscillating dynamics (blue). These computed trajectories are similar to those observed experimentally.

![Figure 1—figure supplement 6.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig1-figsupp6-v2.jpg)

**Figure 1—figure supplement 6.:** The cells were imaged for 15 hr in the presence of Hoechst, fixed and immunostained for thymine dimers (right panel, anti TDM-2 antibody, 20x obj; shown is a representative experiment of three performed). The last image of the GFP-p65 cells acquired at the end of the timelapse acquisition is reported in the middle panel. The green square in the Hoechst panel indicates the area enlarged in panel B. (B) Higher magnification of the selected area in panel A (63x obj). (C) Higher magnification of the selected area in panel B (63x obj, zoom 5). (D) For comparison, GFP-p65 cells were plated in the presence of Hoechst and exposed to increasing doses of UVC and immunostained together with the cells in A. Images were acquired with constant settings in the same microscopy session. Due to the very low intensity, the signal has been enhanced. Fluorescence is almost undetectable in both non-UVC-exposed (0 J/m2) and non-imaged cells (D and B, respectively). (E) Higher magnification of the selected area in panel D (63x obj, zoom 5), green square in 0 J/m2.

![Figure 1—figure supplement 7.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig1-figsupp7-v2.jpg)

**Figure 1—figure supplement 7.:** Immunostaining for gammaH2AX, a marker indicative of active DNA damage repair, was used to assess genetic damage in unstimulated cells exposed or not to Hoechst staining and UV and/or GFP imaging for 3 hr in microfluidic plates. All the images were acquired during the same microscope session keeping the acquisition parameters rigorously constant. (A) GFP-p65 cells treated with sub-toxic doses of doxorubicin (10 nM) for 2 hrs were used as positive control to set up imaging conditions. Obj: 63x. (B) Left panel contains the negative control: cells cultured in the microfluidic plate were not Hoechst stained, nor UV and GFP imaged. Middle and right panels: immunostaining of cells in microfluidic chambers that were Hoechst-stained but not imaged or both Hoechst-stained and UV-imaged, respectively. Obj: 63x. (C) To further confirm the previous results, and to exclude phototoxicity of the 488 nm laser in GFP imaging, we show fields from a chamber that did not received Hoechst staining and imaging (position 7) or was exposed to both (position 1) in the same experiment (20x Obj). The panel on the right shows an enlargement of a small portion of position 1 (green rectangle) to which the adjacent area outside the imaging field and not exposed to GFP imaging has been added to exclude indirect photodamage (Martin et al., 2005).

![Figure 1—figure supplement 8.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig1-figsupp8-v2.jpg)

**Figure 1—figure supplement 8.:** Shown is a montage of imaging fields (GFP channel) extracted from representative time-lapse experiments for the indicated time-points. Frame number 0, 10, 30, 60, 90 and 120 correspond to 0, 1, 3, 6, 9 and 12 hr, respectively. Red frames focus on fields with detectable apoptotic cells.

![Figure 1—figure supplement 9.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig1-figsupp9-v2.jpg)

**Figure 1—figure supplement 9.:** (A) NCI profiles of untreated cells imaged for 12 hr. (B) Correlation between NCI values and nuclear NF-κB content. (C) Comparison of NCI and background-corrected nuclear intensity profiles obtained by manual segmentation of cells stimulated with 10 ng/ml TNF-α without Hoechst/UV imaging.

![Figure 1—figure supplement 10.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig1-figsupp10-v2.jpg)

**Figure 1—figure supplement 10.:** Quantitative immunoblot analysis was performed on cells cultured in 0.1% FCS plus Hoechst and stimulated with TNF-α for the indicated times. Lysates from cells were normalized for their DNA content (De Toma et al., 2014), and the equivalent of 1.5 µg of DNA was loaded per well on 8% SDS-PAGE gels. The 95 kDa band corresponding to the GFP fusion (65 +29 kDa) was detected with anti-p65 antibody (Santa Cruz, Mab, Cat. # sc-372, upper panel) and quantified using the ECL Plex fluorescent western blotting system (GE Healthcare). Sixteen-bit images were acquired with FLA-9000 (Fuji Film); signals were within the linear part of the dynamic range (Celona et al., 2011). Quantification of western blot signals was performed with ImageJ software (Rasband, http://rsb.info.nih.gov/ij). GFP-p65 quantities were expressed as fold change upon setting to 1 the p65 levels in unstimulated cells (bottom panel). Shown is a representative experiment of the three performed. Statistical error: SD of technical replicates (behind symbols).

![Figure 1—figure supplement 11.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig1-figsupp11-v2.jpg)

**Figure 1—figure supplement 11.:** To determine whether Hoechst staining might alter the cell cycle, the imaging culture medium (50 ng/ml Hoechst, 0.1% FCS) was added to GFP-p65 MEFs for 2 hr (preincubation). After that time 10 ng/ml TNF-α was added and cells harvested at the indicated timepoints (magenta). For comparison a set of cell samples was left untreated and harvested at the same timepoints (blue ). In green, cells cultured in 10% FCS . Propidium Iodide staining was performed with standard protocols after cell fixation and cells analysed with an Accuri FACS instrument (Becton-Dickinson). The fractions of cells in each cell cycle phase are reported. Shown is one of three representative experiments.

Obtaining synchronous NF-κB dynamics in cell populations is therefore important to study gene expression, and can give insights into the dynamics at a collective level. White’s group showed that short trains of TNF-α pulses produce rounds of synchronous NF-κB translocation; the stimulation frequency affected both the translocation amplitude and gene expression levels (Ashall et al., 2009). A study performed while the present one was in progress indicated that entrainment of NF-κB oscillations at population level arises when 3T3 cells stably transfected with GFP-p65 are perturbed with regular trains of sawtooth-like profiles of TNF-α (Kellogg and Tay, 2015). Here, we used GFP-p65 mouse embryonic fibroblasts (MEFs) derived from knock-in mice and thus expressing physiological levels of p65 (De Lorenzi et al., 2009). Using a microfluidic device, we exposed cells to well-defined, periodic TNF-α stimuli, and eliminated continuously both catabolites produced by the cells and secreted proteins, which might generate a secondary autocrine/paracrine response. We find that GFP-p65 MEFs lock their NF-κB oscillations to the periodic external signal, and become synchronized. However, the 1:1 locking is maintained over a wide variety of frequencies of the driving TNF-α stimulus, does not improve over repeated stimulation and actually disappears fast when the external stimulus ceases, all of which suggest that entrainment is not achieved. The mathematical model we developed indeed suggests that NF-κB can behave as a damped oscillator, analogous to a mechanical damped harmonic oscillator; damped oscillators do not entrain but follow external forcing while it is present. Taking advantage of the fact that GFP-p65 MEFs under periodic stimulation behave as a synchronous population, we analyzed the transcriptional output at genome-wide level. We find that one single NF-κB dynamics translates into 3 different dynamics of transcriptional regulation, all of which can be reproduced by our mathematical model; the key discriminator is the parameter representing mRNA degradation. Furthermore, the three dynamical patterns correspond to specific functions, which suggests that group of genes were positively selected by evolution.

## Results

### Periodic forcing turns heterogeneous NF-κB oscillations into synchronous oscillations

To characterize the response of the NF-κB oscillatory system to different external stimuli, we made use of GFP-p65 knock-in MEFs (De Lorenzi et al., 2009; Sung et al., 2009; Zambrano et al., 2014a) cultured in a microfluidic device to control precisely the concentration and timing of the TNF-α stimulation (Materials and methods and Figure 1—figure supplement 1A and B). Notably, the flow rate in the microfluidic device is constant, so that the concentration of TNF-α cannot change due to the activity of the cells, nor can the medium accumulate catabolites or secreted proteins.

Constant stimulation of GFP-p65 knock-in cells in the microfluidic plate with a constant flow of 10 ng/ml TNF-α for up to 15 hr induced nuclear-to-cytoplasmic p65 oscillations (Figure 1B; Video 1 and Figure 1—figure supplement 2D) that are qualitatively similar to the heterogeneous oscillations observed with static stimulation (Sung et al., 2009; Zambrano et al., 2014a).

Several controls were performed to exclude possible damaging effects related to imaging. Cells under constant flow of fresh medium without TNF-α divide and show almost no cell death (Video 2); cell death observed under continuous flow depends on the dose of TNF-α (Figure 1—figure supplement 8 and Video 1) independently of the imaging conditions. UV-induced DNA damage due to imaging (Cadet et al., 2005) is negligible as assessed by immunostaining for thymine dimers (Komatsu et al., 1997; Sinha and Hader, 2002). DNA Damage Response (DDR) is also negligible as assessed by immunostaining of imaged cells for gammaH2AX (Marti et al., 2006; Oh et al., 2011; Staszewski et al., 2008) (Figure 1—figure supplement 5 and 6). Moreover, neither Hoechst exposure nor TNF-α affect dramatically the cell cycle (Figure 1—figure supplement 11). The controls to exclude possible effects of the nuclear dye (Ge et al., 2013; Martin et al., 2005) or photo-damage (Cole, 2014) are described in Materials and methods and in figure captions.

![Video 1.](https://cdn.elifesciences.org/articles/09100/elife-09100-media1.mp4.jpg)

**Video 1.:** Imaging of GFP-p65 knock-in cells in the microfluidic chamber stimulated with a constant flow of 10 ng/ml TNF-α for 12 hr. The stimulus induced nuclear-to-cytoplasmic p65 oscillations that are qualitatively similar to the heterogeneous oscillations observed with static stimulation. Along time, it is possible to appreciate the increase of TNF-induced cell death and apoptosis.

![Video 2.](https://cdn.elifesciences.org/articles/09100/elife-09100-media2.mp4.jpg)

**Video 2.:** Several controls were performed to exclude possible damaging effects related to imaging. This video shows that cells under constant flow of fresh medium without TNF-α divide and very few events of cell death are detectable. Left part: GFP channel; right part HOE channel. Twelve-hour imaging.

To analyse the oscillatory dynamics, we refined our recently published pipeline (Zambrano et al., 2014a) to compute the nuclear to cytoplasmic intensity (NCI) of GFP-p65 fluorescence for hundreds of cells per condition (Materials and methods and Figure 1—figure supplement 1C). Although this measure implies a partial segmentation of the cytoplasm and thus is more elaborate than the background-corrected mean nuclear intensity used recently by different authors (Kellogg and Tay, 2015; Lee et al., 2014; Lee et al., 2009; Sung et al., 2014) it is a ratio of intensities and thus it self-corrects for changes in image intensity in our experimental settings (see e.g. Video 1 or Video 2). Furthermore, provided that the total amount of p65 is constant (Figure 1—figure supplement 10), NCI(t) is a monotonic function of nuclear NF-κB (Figure 1—figure supplement 9B) so that oscillations are observed in the former if and only if they are present in the latter (further details in Materials and methods). Finally, a rigorous description of the observed dynamics was achieved through the automatic identification of statistically significant peaks (Materials and methods and Figure 1—figure supplement 2A and B).

The timing between two consecutive peaks is the experimental period Texp. Texp has a distribution with a maximum at 90 min (Figure 1F), which is the approximate intrinsic period reported for NF-κB oscillations that we called T0 (Nelson et al., 2004; Tay et al., 2010; Zambrano et al., 2014a). As observed for static stimulation (Zambrano et al., 2014a), the observed oscillations are very heterogeneous (Figure 1B) and asynchronous (Figure 1—figure supplement 3A and Figure 1—figure supplement 2D). However, the variety of behaviors observed, including non-oscillating cells, is compatible with the dynamics observed in the same cells for static culture conditions, see (Sung et al., 2009; Zambrano et al., 2014a). Similar behaviors are found in the absence of nuclear staining (see Figure 1—figure supplement 9C), which led us to conclude that imaging conditions do not interfere with NF-κB signaling.

The tail in the period distribution (Figure 1F) and the observed average of four peaks in 12 hr of stimulation (Figure 1—figure supplement 3B), instead of the expected eight, indicate that in our cells the heterogeneous oscillations are damped and tend to converge to an equilibrium state under stimulation (Figure 1B). Indeed, although oscillatory peaks are observed for most of the cells, they are infrequent and irregular for times beyond 6 hr (Figure 1B and Figure 1—figure supplement 2D) as previously reported for the same cells in static conditions (Sung et al., 2009; Zambrano et al., 2014a). Hence, we describe here these heterogeneous oscillations as damped in contrast with the sustained oscillations, which continue regularly and unabated for a very long time in continuously stimulated cells, see for example (Kellogg and Tay, 2015).

Damped oscillations can easily emerge in the NF-κB genetic circuit. Indeed, a minimal deterministic model that takes into account the basic elements of the NF-κB genetic circuit (Zambrano et al., 2014b) (Figure 1A, Figure 1—figure supplement 4, see Materials and methods for a complete description of the model) shows that different combinations of the parameters can lead to different dynamics. The model parameters that we used for our explorations are provided in Supplementary file 2. We denote as PS those specifying the external signal and as PNF-κB those used to model the double IκB and A20 negative feedback; in our explorations, we allow them to vary differently depending on the associated uncertainty about their values (Materials and methods and Supplementary file 2). We generated a library of randomized parameters and found that the system presents a fixed point whose stability changes depending on the parameters (details on the stability analysis are found in the Materials and methods section). The vast majority of parameter combinations give rise to damped oscillations (when all the eigenvalues have all negative real parts, see Figure 1—figure supplement 5A,B). A smaller fraction of parameter combinations give rise to trajectories that converge to a stable limit cycle around the unstable fixed points (so certain eigenvalues have positive real parts, see Figure 1—figure supplement 5A,B). Interestingly, parameters for oscillating and non-oscillating cells are in similar intervals suggesting that it is the precise combination of the parameters, rather than a single one, what determines the resulting dynamics (see Figure 1—figure supplement 5C). Our simulations might also explain why other researchers found continuous periodic oscillations with T0 = 90 min under a constant flow of TNF-α (Kellogg and Tay, 2015, and see Discussion) and the variety of damped oscillatory dynamics upon LPS recently reported for fibroblasts (Cheng et al., 2015) and macrophages (Sung et al., 2014). Our exploration shows further how variations of the parameters can give rise to a variety of dynamics that reflects what we find in an isogenic population (Figure 1B and Figure 1—figure supplement 2).

Considering the heterogeneity of dynamics, to better visualize the collective oscillatory state of the population in each condition, following Mondragon-Palomino et al., 2011, we computed and represented the phase of the oscillation ϕ(t) for each cell by detecting peaks and setting ϕ=0 (2π) at the maximum of each peak and ϕ(t)=π in the minimum between two peaks (phase plots for the green time series are depicted in Figures 1B,C. See also Materials and methods and Figure 1—figure supplement 2B,C). Time series for single cells (Figure 1B and C) were converted to phase plots (Figure 1E,I) where each row represents one cell. Thus, oscillatory peaks can be easily observed. In the phase plot, the first response to constant TNF-α right after t=0 hr is synchronous in the population, but this synchrony is quickly lost, as previously reported (Nelson et al., 2004; Tay et al., 2010; Zambrano et al., 2014a).

To investigate the response of the NF-κB oscillator to perturbations in the cell’s environment, we switched periodically the stimulus concentration in the culture chambers in the microfluidics apparatus. TNF-α switching between doses D1 and D2 occurs in less than 1 min and generates a tightly controlled square profile of stimulation. Stimuli were applied for intervals of time T1 and T2. We refer to Tf = T1+T2 as the period of the forcing and to D1–D2 as the amplitude of the forcing (Figure 1A, lower panel).

We started our analysis by applying a periodic stimulation of 90 min, which is close to the intrinsic period of the NF-κB oscillatory system. Single-cell traces are provided in Figure 1C for cells stimulated with D1 =10 ng/ml TNF-α, D2 =0 ng/ml with Tf=90 min. (T1=45 min and T2 =45). Peaks are present in all the forcing cycles (Figure 1C and Figure 1—figure supplement 3C) and synchronous, in contrast to the asynchronous peaks observed in constantly stimulated cells (Video 3). Hence, we observe in this condition – a square forcing – a forcing-induced synchronous dynamics reminiscent of that obtained by applying short trains of pulses (Ashall et al., 2009). Our synchronous oscillations are visually apparent both in time-lapse images (Figure 1H) and phase plots (Figure 1I). Texp is sharply distributed around 90 min (Figure 1J), corresponding to the expected eight peaks in 12 hr (Figure 1—figure supplement 3D). The height of the first peak (Figure 1K) is similar to the height of the first peak under constant stimulation (Figure 1G), indicating that the experimental conditions are highly comparable. The height of the subsequent peaks is slightly higher for periodically stimulated cells but still heterogeneous.

![Video 3.](https://cdn.elifesciences.org/articles/09100/elife-09100-media3.mp4.jpg)

**Video 3.:** Imaging of cells stimulated with D1 =10 ng/ml TNF-α, D2 =0 ng/ml and Tf=90 min. (T1=45 min and T2 =45). Peaks are present in all the forcing cycles and synchronous. Twelve-hour imaging.

Taken together, these results indicate that a periodic external stimulus can lock in step a population of cells in a long series of synchronous NF-κB oscillations, in clear contrast with the remarkable oscillatory asynchrony and heterogeneity under constant stimulation.

### Oscillatory synchrony increases with the forcing amplitude

We then systematically analysed the response to variable forcing amplitudes, by applying different concentrations of TNF-α. The phase plots obtained for TNF-α ranging from 10 to 0.1 ng/ml with D2 = 0 ng/ml show that the coherence of the oscillations decreases with decreasing doses of TNF-α but still persists at low doses (Figure 2A and Figure 2—figure supplement 1). Texp is less sharply distributed around 90 min as the forcing amplitude decreases. Concomitantly, a second peak corresponding to multiples of Tf becomes progressively more conspicuous (Figure 2B), suggesting that for lower doses of TNF-α an increasingly larger fraction of cells do not respond with a peak to some of the forcing cycles. In the plots of peak maxima (Figure 2C) the height of the first peak is not reproduced by the second and the third peaks, compatible with what reported for this forcing period (Ashall et al., 2009). However the heights converge under repeated forcing to a constant value for all the forcing amplitudes. This is typical of nonlinear dissipative oscillators in the presence of periodic forcing (Goldstein et al., 2001).

![Figure 2.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig2-v2.jpg)

**Figure 2.:** (A) Representative phase plots for 25 cells (out of 216, 80, 188, 263, 225 cells analysed) stimulated with D1=10, 1, 0.5, 0.25, 0.1 ng/ml TNF-α, D2=0 ng/ml, for Tf =90 min, T1=T2=45 min. (B) Distributions of the periods for the cells shown in panel (A); distributions become narrower as the dose D1 increases. The appearance of a second peak at Texp=3 hr at lower doses means that in some cycles a fraction of cells miss a peak and the interval to the next one is double. (C) Quantification of height of the nth peak in the different conditions considered in (A). By decreasing the stimulus amplitude, the ratio tends to stabilize to a constant value. (D) Distribution of the phase difference Δϕ for the forcings considered: Δϕ becomes narrower as the forcing amplitude is increased. (E) The synchrony intensity η, an entropy-based measure on how widely distributed the values of Δϕ are, increases with the amplitude of D1 for Tf =90 min. (F) The synchrony intensity ηn computed using only the peaks observed in each forcing cycle shows that the synchrony does not increase with the successive cycles of forcing. Figure supplements from 1 to 3 are provided.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** NCI of single cell time series (green) and average (black) for the indicated doses, (A) to (C) plots correspond to a forcing of 90 min. Cell numbers as in Figure 2.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** The distribution is almost flat and the synchronization intensity η is very low. Cell numbers as in Figure 1.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** Panels in each row (left to right) represent the single cell NCI dynamics (green) plus the average (black) and the detected peaks (triangles); the phase plot; the phase difference distribution (with the synchrony intensity value η) and the experimental period distribution. (A) D1=7.5, D2=2.5, (B) D1=6, D2=4 and (C) D1=5.2, D2=4.8 (in ng/ml TNF-α). Twentyfive cells are reported in the phase plots out of 111, 78, 66 analysed, respectively. T1 = T2 = 45 min.

The degree of synchrony for each experimental setting of forcing can be evaluated considering the distribution of the phase difference Δϕ between the timing of each oscillatory peak and the beginning of the forcing (see Materials and methods). For asynchronously oscillating cells under constant TNF-α stimulation, such distribution is flat (Figure 2—figure supplement 2). When cells are stimulated with different forcing amplitudes, the distribution of Δϕ is narrower for higher doses of TNF-α (Figure 2D), indicating a higher degree of locking of the oscillations to the forcing for increasing amplitudes.

We then compared the degree of synchrony of the cell populations using the synchrony intensity η, an entropy-based quantifier of the distribution of the phase difference Δϕ that is 0 for flat distributions and 1 for delta-like distributions (Mondragon-Palomino et al., 2011, and Materials and methods). Synchrony intensity increases with the dose, but is nonzero even when D1=0.1 ng/ml TNF-α (Figure 2E). To understand if D2=0 was a necessary condition for synchrony we applied D2>0. Results show that the synchrony is maintained when D1 is threefold D2, while for smaller differences synchrony is almost lost (Figure 2—figure supplement 3).

We next investigated whether synchrony improved under repeated forcing. We computed ηn, the synchrony intensity at the n-th cycle of forcing (i.e. Δϕ computed for peaks in the time intervals [(n–1)Tf,nTf) for n≥1). We find that ηn does not increase (Figure 2F) in successive cycles of external forcing, meaning that the oscillations do not become more synchronous as the system is perturbed repeatedly.

Taken together, the above results indicate that NF-κB dynamics adapts to varying amplitudes of periodic inputs. However the system does not seem to learn from the previous periodic forcing cycles.

### Cells oscillate synchronously following a variety of forcing amplitudes and periods

We then tested the adaptability of the NF-κB system to different forcing periods Tf, ranging from 0.5T0 to 2T0.

We first considered periodic perturbation of Tf=2T0=180 min, with T1=30 min and T2 =150 min, and TNF-α doses D1 ranging from 10 ng/ml to 0.1 ng/ml, D2 =0 ng/ml. Oscillations are locked to the forcing even for D1 =0.1 ng/ml (Figure 3A, see also Figure 3—figure supplement 1,A–C and Video 4). The use of T1=30 min assures the existence of sharp oscillatory and transcription peaks (see below) and also leads to synchrony of the oscillations for Tf=T0 (see Figure 3—figure supplement 3, bottom panels). For all doses we find a bimodal distribution of the oscillation periods, with an overall maximum at 180 min and a much smaller relative maximum at 90 min (Figure 3C). This indicates that after a single pulse of forcing some cells oscillate a second time with a period similar to the intrinsic one. However, a closer analysis of peak maxima for time intervals of the form [(n–1)T0, nT0) = [(n–1)Tf/2, nTf/2) (Figure 3E) reveals that peaks arising right after each periodic stimulation (even n) are higher than the rare ones (odd n) arising when stimulation is absent.

![Figure 3.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig3-v2.jpg)

**Figure 3.:** Representative phase plots for 25 cells stimulated with D1=10, 1, 0.1 ng/ml TNF-α (out of 151, 77, 123 cells analysed, respectively) D2=0 ng/ml for (A) Tf =180 min with T1= 30 min and (B) Tf =45 min with T1=22.5 min (analysed 101, 112, 119 cells). (C, D) Plots showing the distributions of the periods for the conditions given in panels (A) and (B), respectively. (E, F) Average peaks height in the intervals [(n–1) T0, T0) and [(n–1) T0/2, nT0/2), for A and B, respectively. In (E), even n correspond to peaks right after stimulation, odd n correspond to the small peak arising between two consecutive stimulations. (G, H) Distribution of the phase difference Δϕ for the forcings in A and B: Δϕ has narrower distributions for higher doses. (I) The synchrony intensity η grows with the doses for Tf=180 min (blue) and Tf=45 min (red). (J, K) Synchrony intensity plots show that ηn does not increase as successive cycles of forcing are applied to the system, both for Tf=180 min and Tf=45 min, respectively. All the analyses included all the tracked cells with no preselection of the responding ones. Figure supplements 1 to 3 are provided.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** NCI of single cell time series (green) and average (black) for the indicated doses and timings. (A–C) correspond to a forcing of 180 min, while (D–F) to a forcing of 45 min. D1 is indicated on the right.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Panels in each row (left to right) represent the single cell NCI dynamics (green) plus the average (black) and the detected peaks (triangles); the phase plot; the phase difference distribution (with the synchrony intensity value η) and the experimental period distribution. (A) D1=10, D2=0; (B) D1=7.5, D2=2.5; (C) D1=6, D2=4 and (D) D1=5.2, D2=4.8 ng/ml TNF-α. Number of cells analysed: 102, 68, 47, 70, respectively. T1=30 min, T2=150 min.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** NCI and average dynamics for 45 and 90 min forcing amplitudes, with TNF-α stimulation of 10 and 1 ng/ml, are reported here to integrate results presented in main Figures 2A and 3B. The aim was to assess synchronization for a constant T1 value of 30 min as opposed to 45 and 22 min. Each row shows (A) the phase plots (approximately 150 cells analysed per condition), (B) the single-cell NCI dynamics (green) plus the average (black) and the detected peaks (blue triangles) for a specific condition of synchronization. (C) The experimental period distribution ; (D) the phase difference distribution (with the synchrony intensity value η.

![Video 4.](https://cdn.elifesciences.org/articles/09100/elife-09100-media4.mp4.jpg)

**Video 4.:** Imaging of cells stimulated with D1 =10 ng/ml TNF-α, D2 =0 ng/ml and Tf=2T0=180 min (T1=30 min and T2 =150). Oscillations are locked to the forcing. Twelve-hour imaging.

Oscillations in each condition show a good degree of synchrony, as described by the distributions of the phase differences Δϕ, which are remarkably narrow for all doses (Figure 3G); the synchrony intensity η is nonzero even for D1 = 0.1 ng/ml and increases with the dose (Figure 3I, blue line). When D2>0 ng/ml we found synchronized oscillations for D1 at least three times D2 (Figure 3—figure supplement 2).

We considered also the ability of the NF-κB system to respond to stimulations of periodicity below the intrinsic one. We selected Tf=T0/2=45 min, but T1=30 min led to a poor synchrony (see Figure 3—figure supplement 3, top panels). We therefore reduced T1 to 22.5 min, and thus T2=22.5, which proved to be a sufficiently long resetting of the external signal; in these conditions we obtained a sharply defined dynamical response. Oscillations are locked in step with D1=10 and 1 ng/ml (Figure 3B, Video 5), whereas synchronization is weaker for D1=0.1 ng/ml (this is also evident in the average NCI dynamics, see Figure 3—figure supplement 1,D–F). The experimentally determined oscillatory period Texp (Figure 3D) is narrowly distributed around Tf=45 min for D1=10 ng/ml, but we also find a small peak around Texp=90 min, indicating that some cells skip the oscillation elicited by the forcing. The peak height for each forcing cycle tends to stabilize to a constant value and to be lower for lower forcing amplitude, although the differences are small (Figure 3F). Also in this case, the synchrony correlates with the dose: in fact, the phase difference Δϕ tends to be more narrowly distributed for higher values of D1 (Figure 3H), and the synchrony intensity η grows with the dose (Figure 3I, red line).

![Video 5.](https://cdn.elifesciences.org/articles/09100/elife-09100-media5.mp4.jpg)

**Video 5.:** Imaging of cells stimulated with D1 =10 ng/ml TNF-α, D2 =0 ng/ml and Tf=T0/2=45 min (T1=22.5 min and T2 =22.5 min). Such short wash-out provides a sufficient resetting of the external signal; in these conditions we obtained a sharply defined dynamical response and oscillations are locked in step. Twelve-hour imaging.

It has been recently reported that NF-κB oscillations can be synchronized by entrainment (Kellogg and Tay, 2015). However, in our experiments the synchrony intensity for each cycle, ηn, does not increase when the system is forced repeatedly, either with periods of 90, 180 or 45 min (Figures 2F, 3J,K), in contrast to what is observed for entrained oscillators (Mondragon-Palomino et al., 2011). Furthermore, when oscillators are entrained by external forcing, their oscillations also show m:n resonant patterns (m oscillations for each n cycles of the forcing) in so-called Arnold tongues (Pikovsky et al., 2003). However, we only observed 1:1 synchronization patterns for all the periods of forcing (Figure 3A,B), with no clear evidence of the 2:1 and 1:2 patterns expected for entrainment. We thus investigated further whether the synchronization mechanism we observed does correspond to entrainment.

### The synchronization mechanism of GFP-p65 knock-in MEFs is not entrainment

Once the forcing ceases, entrained oscillators dephase gradually, losing their sharply defined common entrained oscillatory period. We then investigated whether our cells kept a memory of the synchronous dynamics once the periodic forcing ceased. The phase plots for 75 cells forced with Tf=45 min D1 =10 ng/ml (Figure 4A, washing out after 16 forcing cycles), and for Tf=90 min with D1 =1 ng/ml (Figure 4B, washing out after eight forcing cycles), indicate that when the external stimulus stops, cells lose quickly their synchrony. This is also evident from single-cell NCI traces and from the peaks detected in the same conditions (Figure 4C and D respectively). Indeed, only for Tf=45 min we observed small peaks after the last cycle of the forcing, but these peaks are on average 90 min away from the last forced peak, and correspond to the intrinsic oscillatory period of our oscillator. The quick loss of synchrony can also be observed in the evolution of the synchrony quantifier ηn for the two last cycles of the forcing (Figure 4E, n=1,2) and the two subsequent (virtual) ones (Figure 4E, n=3,4). This is also the case when considering cells forced with Tf=90 min and a high stimulus amplitude D1 =10 ng/ml, after which we apply a constant flow of 10 ng/ml TNF-α: cells present a last well-defined translocation (Figure 4F and 4G) and rapidly dephase (Figure 4H).

![Figure 4.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig4-v2.jpg)

**Figure 4.:** (A, B) Phase plots of the last two oscillation cycles for Tf =45 min (D1=10 ng/ml) and Tf =90 min forcing (D1= 1 ng/ml) (number of forcing cycles are indicated above) followed by a period of 3 hr with no stimulation (75 cells are displayed out of 106 and 197 cells analysed, respectively). (C, D) NCI time series at single cell level (green lines) for the two conditions (A) and (B). Blue triangles indicate the peaks considered in the computing. The thick black line is the average NCI, showing a small peak 90 min after the last forced peak for Tf =45 min (C), compatible with the natural timescale of the free oscillations. (E) The synchrony intensity ηn for the last two forced peaks (n=1, 2) and for the peaks detected in the absence of the stimulus (n=3, 4) illustrates the fast loss of synchrony. (F) Phase plots of the last two oscillation cycles for Tf =90 min (number of forcing cycles are indicated above) (D1=10 ng/ml) followed by 4.5 hr flow of 10 ng/ml TNF-α (75 cells are displayed out of 149 cells analysed). (G) NCI time series at single-cell level (green lines). Blue triangles indicate the peaks considered in the computing. The thick black line is the average NCI, showing a small peak 90 min after the last forced peak, compatible with the natural timescale of the free oscillations. (H) The synchrony intensity ηn for the last two forced peaks (n=1, 2) and for the peaks detected in the presence of the stimulus (n=3,4) illustrates the fast loss of synchrony. Figure supplements from 1 to 4 are provided.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Panels in each row (left to right) represent the single cell NCI dynamics (green) plus the average (black) and the detected peaks (triangle); the phase plot; the phase difference distribution (with the synchrony intensity value η) and the experimental period distribution. (A) D1=10, D2=0; (B) D1=7.5, D2=2.5; (C) D1=6, D2=4 and (D) D1=5.2, D2=4.8 (in ng/ml TNF-α). Analysed cells: 102, 91, 70 and 104, respectively. T1=30 min, T2=30 min.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** We computed the period to which the NF-κB system converges (average timing between peaks in a 15-hr timespan) for different periods of the forcing and various forcing amplitudes. A representative plot of the results obtained is shown: we keep PNF-κB constant while varying the forcing parameters PS. D1 varies between 0 and Dmax=2 and T1=T2=Tf/2. The ratio Tnumerical/Tf between the computed NF-κB period and the forcing period is very close to one, as expected for damped oscillations when periodically forced. Only for high values of the period the ratio is close to 0.5.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** This ratio is due to the presence of smaller peaks between the bigger post-stimulation peaks in our simulations. An example of our simulations for NCI (green line) and the forcing (red line) is shown. Notice that the smaller peaks tend to decrease in time. This dynamics is reminiscent of the one observed for Tf=2T0=180 min in our experiments, see Figure 3A.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig4-figsupp4-v2.jpg)

**Figure 4—figure supplement 4.:** Each row shows (i) the phase plot for 25 cells ( Approximately 100 cells were analysed per condition), (ii) the single cell NCI dynamics (green) plus the average (black) and the detected peaks (blue triangles), (iii) the experimental period distribution and (iv) the phase difference distribution (with the synchrony intensity value η) for a specific condition ofstimulation with a sawtooth profile, generated by a 15 min pulse followed by no washout. The TNF-α concentrations used are indicated for each row. For forcings of 60 and 90 min we observe synchronization similar to the one obtained for alternating doses this is more blurred for forcing of 180 min.

Kellogg and Tay (2015) found no synchrony for Tf=60 min. However, we found that our cells can actually be synchronized under periodic stimulations with Tf=60 min (T1 =T2 =30 min) when D1 =10 ng/ml (Video 6) and D2 =0 ng/ml (Figure 4—figure supplement 1A). Furthermore, we found that synchrony is still visible for D2>0 ng/ml (Figure 4—figure supplement 1B–D), as we had observed for other stimulation periods. The difference might arise from the fact that we use a forcing different from the sawtooth-like TNF-α profile used by Kellogg and Tay (2015), which is obtained by periodically and quickly replacing the medium in contact with the cells with fresh TNF-α. The sawtooth concentration profile is assumed to arise due to a clearance process of TNF-α by degradation and internalization. We then applied sawtooth forcing to our cells (Figure 4—figure supplement 4). Cells lock their oscillations to the sawtooth forcing of periods Tf=60 min and Tf=90 min at the doses considered. Interestingly, the synchronization is lost for Tf=180, suggesting that autocrine-paracrine signalling might introduce a distortion in the cell environment, which is reduced when the medium is changed more frequently. Alternatively, the different geometry of our microfluidic with respect to the one used in Kellogg and Tay (2015) might lead to a slower TNF-α degradation and produce profiles closer to static concentration than to oscillatory stimulation. The profiles observed are indeed similar to some of the dynamics observed for alternating doses of TNF-α with D2>0 ng/ml, such as those for Tf=60 min (Figure 4—figure supplement 1B–D), Tf=90 min (Figure 2—figure supplement 3) and Tf=180 min (Figure 3—figure supplement 2), with compatible values of η. However, it is clear that with sawtooth forcing of Tf=60 min the synchrony is strong, at variance with the results reported by Kellogg and Tay (2015).

![Video 6.](https://cdn.elifesciences.org/articles/09100/elife-09100-media6.mp4.jpg)

**Video 6.:** GFP-p65 cells can be synchronized under periodic stimulations with Tf=60 min (T1 =T2 =30 min) when D1 =10 ng/ml and D2 =0 ng/ml. Twelve-hour imaging.

Overall, we conclude that the synchronization mechanism that we observe is not entrainment. Rather, it is similar to that of simple mechanical damped oscillators, such as the damped harmonic oscillator, which after a perturbation tend to relax to an equilibrium state. When these mechanical systems are challenged with an external periodic forcing, the period of the oscillations tends to match the period of the forcing (Pikovsky et al., 2003). In fact, our minimal mathematical model of the NF-κB circuit (Figure 1—figure supplement 4) reproduces damped oscillations (e.g. Figure 1—figure supplement 5A,B,D). In these conditions, the period of the periodically forced system converges to the period of the forcing (Figure 4—figure supplement 2). Of note, the model reproduces the small peaks appearing between two forcing cycles (Figure 4—figure supplement 3), similar to the small peaks that we observed for the same forcing as in Figure 3A.

When behaving as a damped oscillator, the NF-κB system is well suited to quickly synchronize its oscillatory period to input signals of a wide variety of timescales. This is probably a desired feature for a system that underlies responses to environmental challenges, which do not come with a particular periodicity. This is the reverse of what might be desirable for circadian clocks, whose design should privilege the entrainment to the 24-hr light/darkness period. To understand how the oscillatory pattern of NF-κB affects its biological output, we focused on the transcription dynamics of genes controlled by NF-κB.

### Synchronous NF-κB dynamics reveal different patterns of gene expression

The heterogeneity of NF-κB dynamics in the cell population under constant stimulation makes it difficult to establish a direct correspondence between NF-κB activity and transcription. However, under conditions of synchronous oscillation the average dynamics corresponds to the dynamics of single cells. This is for example the case for cells stimulated with D1 =10 ng/ml D2=0 ng/ml TNF-α, T1=30 min and T2 =150 min (Tf= 2T0) (Figure 5A). Numerical simulations with a simple mathematical model of transcription under the control of the regulatory network using parameters from our previous work (Figure 5—figure supplement 1, Materials and methods and Zambrano et al., 2014b) suggested that for some genes there should be a clear coordination between the input pulsed signal, the oscillating dynamics of NF-κB and the transcriptional output (Figure 5B).

![Figure 5.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig5-v2.jpg)

**Figure 5.:** (A) NCI plot of single cell oscillations (green lines) and population average (black lines) for cells stimulated with D1=10 ng/ml TNF-α, D2=0 ng/ml, T1=30 min and T2=150 min. The open circles represent the fitting obtained using our minimal mathematical model. (B) The mathematical model predicts waves of transcription (orange plot, right) coordinated with the stimulus (red plot, top) and p65 oscillations (green plot, left). (C, D) q-PCR time course of nascent and mature mRNAs for the prototypical early and late genes IκBα and Ccl5, respectively. (E, F) Transcription profiles for mature IκBα (red) and Ccl5 (blue) RNAs (dots) can be accurately fitted (lines) by our minimal mechanistic mathematical model. The fittings were performed by keeping common the parameters regulating the external signal (PS) and the dynamics (PNF-κB) in (A), (E) and (F) but using different gene expression parameters PG for (E) and (F). Figure supplements 1 to 2 are provided.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig5-figsupp1-v2.jpg)

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** Quantitative PCR for nascent (left) and mature (right) IκBα (upper panels) and Ccl5 (bottom panels) in GFP-p65 MEFs cultured in 10% FCS or 0.1% FCS plus Hoechst. The cells were stimulated with TNF-α for the indicated times. The plots represent the average of two independent experiments. Bars: SEM.

To validate the model’s prediction, we tested RNA transcription in the synchronous oscillatory condition shown in Figure 5A. RNA samples were prepared at time 0 and 20, 40 and 60 min after each TNF-α pulse. Quantitative RT-PCR was performed for both the nascent unspliced and the mature mRNA forms of the prototypical early and late genes IkBa and Ccl5/RANTES, respectively (Figure 5—figure supplement 2 and Materials and methods). Nascent transcription of both genes starts synchronously with each TNF-α pulse and p65 nuclear localization (Figure 5C,D), and the levels of nascent transcripts clearly oscillate. Mature transcripts of the early gene IκBα follow the oscillatory dynamics, show transcription-coordinated splicing and do not accumulate after stimulus wash-out (Figure 5C). On the contrary, the mature form of the late gene Ccl5 accumulates slowly and progressively along 12 hr (Figure 5D).

This latter observation extends the notion that the splicing rate for inflammatory genes plays a key role in regulating the timing of gene expression, as previously reported (Hao and Baltimore, 2013). The induction levels for IκBα in the first hours hardly differ from those under chronic stimulation ((Hao and Baltimore, 2013); Figure 5 and Figure 5—figure supplement 2). Interestingly, we also find oscillatory dynamics of IκBα and Ccl5 nascent transcripts when cells are stimulated with a forcing period of Tf= 90 min, although the oscillations are less prominent than for Tf=180 min. The expression of Ccl5 for Tf= 90 min grows monotonically (Figure 7—figure supplement 1).

We then asked whether our minimal mathematical model (Figure 5—figure supplement 1 and Figure 1—figure supplement 4) could simultaneously fit NCI dynamics (Figure 5A) and transcription profiles. Our model of transcription can be interpreted as a population-level NF-κB–driven telegraph model (Suter et al., 2011) that includes non-cooperative transcription activation by NF-κB (Giorgetti et al., 2010) and the role as transcriptional repressor reported for IκBα (Arenzana-Seisdedos et al., 1995; Kellogg and Tay, 2015; Lipniacki et al., 2004; Lipniacki et al., 2006a; Lipniacki et al., 2006b; Tay et al., 2010); we denote the parameters used to fit the transcription as PG (details in the Materials and methods section). The fittings were performed by keeping constant the parameters of the external signal PS (which is externally imposed) and using the same parameters regulating NF-κB dynamics, PNF-κB in Figure 5A,E,F, while using different individual transcription parameters PG for each gene (Figure 5E,F). Despite being much simpler than other existing models of NF-κB dynamics (Ashall et al., 2009; Tay et al., 2010), our model fits faithfully the observed transcription dynamics for both IκBα (Figure 5E) and Ccl5 (Figure 5F).

Overall, our results show that the expression of two different genes can follow different dynamical patterns even if the entire cell population is effectively locked to the dynamics of the transcription factor that controls both genes.

### Transcription dynamics discriminates between groups of functionally related genes

Genome-wide profiling represents the logical further step to understand whether additional NF-κB regulated genes follow the diversified dynamics observed for Nfkbia/IκBα and Ccl5. We performed microarray analysis on RNA purified from GFP-p65 knock-in cells under either constant or pulsed TNF-α stimulation (Zambrano et al., 2016). Transcriptional outputs were subjected to unsupervised clustering of standardized profiles to group the transcription profiles by their shape, while minimizing differences in fold-changes (Materials and methods). For constantly stimulated cells, gene expression profiles reproduce well the previously observed kinetics (Rabani et al., 2011; Sivriver et al., 2011), in which the maximum expression level is achieved with different timings for different genes, and no evidence of the oscillatory dynamics of NF-κB is discerned (Figure 6—figure supplement 1).

We then quantified genome-wide expression profiles in the population shown in Figure 5, which oscillates synchronously in the forcing regime of Tf=180 min (Materials and methods). We found 970 genes whose expression responds to TNF-α stimulation, of which 499 increase and 471 decrease relative to unstimulated cells. Genes distributed in six highly homogeneous clusters; a higher number of clusters did not reduce significantly the inter-cluster distance (Figure 6—figure supplement 2A). Three of the clusters contain genes with increasing expression and three contain genes with decreasing expression (Figure 6A, Figure 6—figure supplement 2). The clusters display profiles that range from the oscillatory dynamics of IκBα (Cluster 1) to the slowly increasing dynamics of Ccl5 (Cluster 3). Notably, while genes contained in the three clusters of increasing expression are enriched with known NF-κB target genes (10-14 < p < 0.05, Fisher’s exact test, Materials and methods and Figure 6—figure supplement 3), clusters with decreasing expression are not significantly enriched. The same is observed in chronic stimulation (Figure 6—figure supplement 4).

![Figure 6.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig6-v2.jpg)

**Figure 6.:** (A) Clusters 1–6 were obtained by an unsupervised k-means-like clustering from the genome-wide transcription profiling of samples harvested in the experiment shown in Figure 5A. Line colours are indicative of the membership value of each gene (colour scale at the bottom). Three clusters contain genes with increasing expression (1–3) and three with decreasing expression (4–6). On the y-axis, standardized expression profile in arbitrary units (see Materials and methods). (B) Plots show single-gene mRNA traces (median: thick blue line; 85% and 15% intervals, thin blue lines). The time courses can also be fitted using our minimal mathematical model: shown is the median of the single-gene fits (thick red line) and the 85% and 15% intervals (thin red lines). Fittings were performed using the same parameters for the external signal (PS) and the dynamics (PNF-κB) as in Figure 5, but using different gene expression parameters PG for each gene. (C) Top five pathways of hierarchical level 2 and 3 in the Reactome database significantly enriched in each dynamical cluster. Dot sizes are proportional to the percentage of genes in the cluster belonging to that pathway. Dot colours identify the corresponding p-values (p-value < 0.05 is set as threshold). Scale bars on the right. (D, E) Heatmaps shows the degree of overlap at gene level (D) and pathway level (E) between each of the 6 clusters. Colour scale bar on the right. Figure supplements from 1 to 6 are provided.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** Four clusters are obtained from the standardized gene expression profiles for cells stimulated with a constant concentration of 10 ng/ml TNF-α. Each line represents a gene. Lines colors: blue and red indicate low and high membership values, respectively.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** (A) Minimal inter-centroid distance as a function of the number of clusters considered for Figure 6 . (B) Principal Component Analysis based on two components segregates clusters containing genes with increased transcription (1, 2 and 3) from those with decreased transcription (4, 5 and 6).

![Figure 6—figure supplement 3.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig6-figsupp3-v2.jpg)

**Figure 6—figure supplement 3.:** Tf=180 with T1=30 min and T2=150 min. Two lists of NF-κB targets were considered. (A) Gilmore’s web-site (www.bu.edu/nf-kb/), (B) from (Li et al., 2014). Significance is shown as -Log10(p-value), a dashed line marks the threshold of significance at p=0.05.

![Figure 6—figure supplement 4.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig6-figsupp4-v2.jpg)

**Figure 6—figure supplement 4.:** Two lists of NF-κB targets were considered: (A) Gilmore’s web-site (www.bu.edu/nf-kb/). (B) from (Li et al., 2014). Significance is shown as –Log10(p-value), a dashed line marks the threshold of significance at p=0.05.

![Figure 6—figure supplement 5.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig6-figsupp5-v2.jpg)

**Figure 6—figure supplement 5.:** Distance distribution for single-gene fittings of genes with increased (left) or decreased (right) transcription in cells stimulated with a period of 180 min.

![Figure 6—figure supplement 6.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig6-figsupp6-v2.jpg)

**Figure 6—figure supplement 6.:** Upper panels: RNA degradation rates inferred from our model for the gene clusters, for a period of 180 min. Lower panels: example fittings of two genes for each cluster. Of note, the degradation rate is very high for oscillating genes in Cluster 1. Clusters 2 and 3 containing genes with “rapidly-increasing and slowly-decreasing” transcription or “slowly-increasing” transcription are characterised by degradation rates two orders of magnitude lower. Genes with decreasing transcription and belonging to Clusters 4–6 have very low RNA degradation rates.

![Figure 6—figure supplement 7.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig6-figsupp7-v2.jpg)

**Figure 6—figure supplement 7.:** The data were also fitted using a model in which IκBα (A) does not act as a transcriptional repressor in the feedbacks nor (B) in the expression of each single gene, while the role of NF-κB as transcriptional activator (green arrows in (A)) is preserved. (C) Gene expression data from the experiment in Figure 6 were fitted using the models of (A) and (B) analogously to our fittings of Figures 5 and 6 : with a common set of PNF-κB while each gene is fitted with its own PG. Again, the average relative error is lower for up-regulated genes. (D) Plots show single-gene traces (grey) of all mRNA (median: thick blue line; 85% and 15% intervals, thin blue lines). We show the median of the single-gene fits (thick red line) and the 85% and 15% intervals (thin red lines). (E) Histograms on the bottom part show the distribution of the degradation rates obtained from the fitting for each dynamical cluster. Here, again we have that the degradation rate is the key parameter to reproduce the gene expression patterns observed.

We tested if our model would also reproduce the patterns of gene expression dynamics at a genome-wide level in these conditions, keeping the same parameters PS and PNF-κB as in Figure 5 but using different gene expression parameters PG for each gene. Indeed, the model fits well the dynamical patterns observed experimentally in clusters with increasing expression (Figure 6B, grey lines). The median and the intervals of observed and simulated single gene expression levels match remarkably well (Figure 6B, red and blue lines respectively, individual fittings are shown in Figure 6—figure supplement 6, bottom-left panels); the average relative error per timepoint is less than 10% (Figure 6—figure supplement 5, left, further details on the fittings and metrics used are given in Materials and methods).

Genes in the clusters with decreasing expression cannot be fitted with the same accuracy (the average relative error per timepoint is above 10%, see Figure 6—figure supplement 5, right, individual gene fitting examples shown in Figure 6—figure supplement 6, bottom-right panels), further suggesting that these genes are not controlled directly by NF-κB. Indeed, an analysis of the parameters show that gene expression is essentially fitted for those genes as a simple RNA degradation with nearly no contribution of the gene activation/inactivation processes (low Kon,G and Koff,G, see Figure 5—figure supplement 1 and Materials and methods).

Interestingly, our mathematical model indicates that for a given stimulus impinging on NF-κB, the degradation rate of the mRNA is the key parameter for producing the most distinct dynamical profiles. Of note the highest degradation rates are specific for oscillating genes, while those for slowly increasing genes are two orders of magnitude lower (Figure 6—figure supplement 6, top panels). This further underlines the importance of mature RNA processing and degradation in the definition of different patterns of gene expression.

Although the role of IκBα as a repressor has been proposed in a number of theoretical analyses (Kellogg and Tay, 2015; Lipniacki et al., 2004; Lipniacki et al., 2006a; Lipniacki et al., 2006b; Tay et al., 2010) only limited evidence of this role is experimentally available (Arenzana-Seisdedos et al., 1995). Thus, to investigate the role of IκBα in patterning gene expression, we built a model where IκBα does not act as a direct repressor (Figure 6—figure supplement 7A,B). This alternative model fits the gene expression dynamics of each cluster well (Figure 6—figure supplement 7E), and again better for genes with increasing transcription than for those decreasing (Figure 6—figure supplement 7C). The mRNA degradation rate is again the key parameter to discriminate between the different patterns of gene expression (Figure 6—figure supplement 7D). While our fittings do not provide conclusive evidence on the role of IκBα as a transcriptional repressor, they suggest that this is not needed.

Finally, to understand if the different dynamics observed with Tf=90 min were also present in other conditions, we used the same clustering approach for gene expression profiles of cells stimulated with Tf=90 min, D1 =10 ng/ml and D2 = 0 ng/ml (as in Figure 1C). Oscillations in transcript levels were observed, although they were not as conspicuous as for Tf=180 min (Figure 7A), probably due to the fact that 90 min is not long enough for most transcripts to degrade. Enrichment of target genes is similar to the two previous cases (Figure 7C,D).

![Figure 7.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig7-v2.jpg)

**Figure 7.:** (A) Clusters obtained by unsupervised k-means clustering from the genome-wide transcription profiling of cells perturbed with a forcing of 90 min, D1=10 and D2=0 ng/ml of TNF-α. Lines colours: blue and red indicate low and high membership values, respectively. (B) Top five pathways of hierarchical level 2 and 3 in the Reactome database significantly enriched in each dynamical cluster. Dot sizes are proportional to the percentage of genes in the cluster belonging to that pathway. Dot colours identify the corresponding p-values (p-value<0.05 is set as threshold). Scale bars on the right. (C, D) Enrichment analysis for NF-κB targets from the clusters displayed in panel A. Two lists of NF-κB targets were considered: left: Gilmore’s web-site (www.bu.edu/nf-kb/); right: data from Brasier and Kudlicki groups (Li et al., 2014). Significance is shown as -Log(p-value), a dashed line marks the threshold of significance at p=0.05. (E, F) Heatmaps show the degree of overlap at gene level (E) and pathway level (F) between each of the 6 clusters. (G) Overlap at a gene level between clusters obtained for 180 min and for 90 min. It is particularly high for Clusters 1, those of oscillating genes. Colour scale bar on the right. Figure supplement 1 is provided.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** Q-PCR time-course of nascent and mature mRNAs for the prototypical late and early genes Ccl5 and IκBα are shown. PCR assays were performed on the same samples used for genome-wide transcription profiling shown in Figure 7.

We then performed a pathway analysis to determine if each of our dynamical clusters were enriched in functionally related pathways (see Materials and methods). Indeed, this is the case (Figure 6C): Cluster 1 is broadly related to chemokines and chemokine receptors and contains so-called early genes, Cluster 2 to the immune system and so-called intermediate genes, and Cluster 3 to extracellular matrix rearrangements and so-called late genes (Rabani et al., 2011; Tian et al., 2005a; 2005b). Thus, the clustering also indicates a precedence order in the articulation of the cell's response. Genes with decreasing expression comprise pathways related to metabolism (Cluster 4), cell cycle (Cluster 5) and chromosome maintenance (Cluster 6).

The overlap between clusters is minimal both at gene and pathway level (Figure 6D and Figure 6E, respectively, and Materials and methods). The correspondence between dynamics and gene function is also fulfilled in cells forced with Tf=90 min (Figure 7B), with a low intercluster overlap at gene level (Figure 7E), and slightly higher overlap at pathway level (Figure 7F). Interestingly, there is a good correspondence between clusters identified upon both 180 and 90 min forcing. In particular Cluster 1 (the oscillating cluster) contains almost exactly the same genes in both conditions (Figure 7G).

Taken together, the above results indicate that different gene expression dynamics identify functionally related categories of genes, suggesting a strict relationship between dynamics and function in the cell's response to external stimuli.

## Discussion

### The NF-κB system synchronizes to external periodic forcing as a damped oscillator

Our results show that single cells activate NF-κB signalling synchronously to external TNF-α stimulation, and that repeated forcing elicits synchronous NF-κB oscillations at population level. However, NF-κB does not behave as a free oscillator: no cell oscillates constantly in the presence of continuous stimulation (Figure 8A and B left, green lines). Furthermore, synchronization among cells does not improve upon repeated forcing (“training”), and single cells trained for a dozen forcing cycles stop oscillating and dephase (“forget”) as fast as cells stimulated only once. Finally, cells can be synchronized with a wide variety of forcing periods and forcing amplitudes, and synchronize to the external forcing (Figure 8A and B right, green lines) without showing any preference for periods resonating with the NF-κB intrinsic period of 90 min; synchronization is more pronounced with high than with low stimulation amplitude.

![Figure 8.](https://cdn.elifesciences.org/articles/09100/elife-09100-fig8-v2.jpg)

**Figure 8.:** (A) The NF-κB system is able to provide different responses to different inputs, from constant (left) to time-varying ones (right). (B) Our cells show damped oscillations to a constant stimulus (left, green lines), although for other cell types sustained oscillations might be possible (magenta line). Damped oscillations can adapt to timevarying inputs (right) and give rise to synchronous oscillations. (C) These synchronous oscillations produce different patterns of gene expression, from oscillating (left, orange lines) to slowly increasing (right, blue lines) and intermediate dynamics (pink lines, centre). We find that each kind of dynamics is typical for genes involved in different cellular functions.

The ability of NF-κB to oscillate in tune with a forcing of 45 min illustrates well the plasticity of synchronization: 45 min is equivalent to one half of the intrinsic period, and entrained cells would skip one forcing period out of 2 (following the 1:2 resonance), but our data do not support this interpretation, since cells only infrequently skip a forcing period. Simulations with our mathematical model can actually reproduce the ability of the system to synchronize to different forcing periods. The ability of our cells to synchronize to a 60 min periodic forcing points in the same direction.

Thus, we find that our GFP-p65 knock-in cells are not entrained, as do not satisfy the essential precondition – sustained oscillations – and two critical tests for entrainment – increasing synchronization upon repeated forcing, and synchronization to the natural frequency of the internal oscillator (Pikovsky et al., 2003). Our cells appear closer to the classical textbook example of a damped harmonic oscillator (Goldstein et al., 2001), whose frequency corresponds to the frequency of the external stimulation, and whose synchronization to the external stimulus increase monotonically with stimulus amplitude.

We interpret the damped oscillator behaviour of the NF-κB system as an intrinsic characteristic of the NF-κB system which allows it to adapt to a wide variety of inputs and to quickly reset. In fact, pathogens and inflammatory signals do not come in regular periodic patterns, and a carefully calibrated inflammatory response that would adapt itself to any irregular pattern of stimulation would be positively selected for.

We explored our minimal mathematical model to understand why we observed damped oscillations whereas Kellogg and Tay observed sustained oscillations under constant stimulation, a behaviour that presumably is the root of the different synchronization mechanisms observed. Our simulations suggest that sustained oscillations would not be the norm, but rather the result of a specific set of parameters (see Figure 1—figure supplement 5A,B). Indeed, the NF-κB network has an equilibrium that depending on the combinations of parameters can be stable, giving rise to damped oscillations that converge to it, or unstable, giving rise to a stable cycle around it (see e.g. Figure 8B, left, magenta line); transitions between these two states can be mediated by a Hopf bifurcation.

The simulations performed with our simple model can thus reconcile our experimental observations with the detection of sustained oscillations for different cells (Kellogg and Tay, 2015), but also with the rich variety of damped oscillatory dynamics reported for other cell types in recent works (Cheng et al., 2015; Sung et al., 2014). Other theoretical analyses have identified the amount of NF-κB expressed by a specific cell as the determinant of the Hopf bifurcation and the stability of the oscillator (Mothes et al., 2015). Notably, we used cells with physiological and uniform p65 levels. We also note that the interplay between different feedback loops, including the A20 feedback (Werner et al., 2008) can vary between cell types, leading to different degrees of dampening, as observed experimentally by selective knock-outs (Hoffmann et al., 2002); dissecting the contribution of each of these feedbacks will be the subject of future experimental and theoretical work.

### Oscillations in the nuclear concentration of NF-κB lead to different dynamical patterns of gene expression

The oscillatory behaviour of NF-κB consists in periodic relocalization between the nucleus and the cytoplasm, and entails corresponding cycles of NF-κB binding to cognate binding sites in the genome. Thus, NF-κB driven transcription should be pulsatile as well, and in fact we detect cycles in the levels of elongating transcripts in the prototypical early and late NF-κB-controlled genes IkBα and Ccl5. However, whereas mature mRNA oscillates for IκBα, it slowly accumulates for the late gene Ccl5, and this held true for different frequencies of the periodic stimulation. Genome-wide analysis of dynamics, using unsupervised clustering of whole transcriptome profiles, identified six highly homogeneous sets (“clusters”), three containing genes with increasing transcription and three containing genes with decreasing transcription. While the genes with increasing transcription are predicted NF-κB targets, those in the decreasing sets are not.

The train of p65 nuclear translocations is thus decoded by the cell into different transcriptional dynamics: genes in Cluster 1 display a clear and sustained oscillation in transcript level; instead, transcripts for genes in Clusters 2 and 3 accumulate fast or increase slowly and steadily over many cycles of NF-κB oscillations, respectively (see Figure 8C). The result is that each new wave of TNF-α elicits on Cluster 1 genes almost the same responses as the previous waves, and no memory is kept of the past; the expression of genes of Clusters 2 and 3 allows a long-lasting response that integrates over time the responses to previous waves.

All three dynamics of genes with increased expression could be reproduced by our minimal mathematical model of transcription, which incorporates the features of the paradigmatic telegraph model (Suter et al., 2011). Our model also suggests that mRNA degradation is the key parameter that allows a functional and temporal shaping of the NF-κB response, in particular for transcripts in Cluster 1 (Figure 6—figure supplement 6, top-left panel). The computational results fit well with the fast turnover of early transcripts, whose degradation depends on positive regulators like Zfp36 (Rabani et al., 2011). Of note, Zfp36 is in Cluster 1, and oscillates sharply and synchronously with the forcing; this might contribute further to the shaping of peaked responses.

### Oscillatory dynamics and functionally related patterns of gene expression: an adaptive viewpoint

Overall, our most remarkable finding is that NF-κB oscillations drive the expression of distinct sets of genes whose expression dynamics and functions correlate: the transcripts that oscillate encode mostly cytokines and cytokine receptors, the ones that rise fast and decrease slowly encode proteins involved in immunity, and the ones that rise steadily encode proteins involved in the rearrangement of the extracellular matrix (Figure 8C).

While steady-rise and rise/decline programs of gene expression can be operated by non-oscillatory transcription factors, oscillating transcription programs can be best achieved with oscillating transcription factors. We note that the transcripts that oscillate are involved in the decision of cells of whether to move or not, which has to be refreshed repeatedly over time. The oscillatory dynamics of NF-κB allows time to be segmented in units of 90 min cycles, with the option to resume chemokine-directed migration after each single cycle. As seen from this perspective, the operation of the NF-κB system as a damped, fast-detuning oscillator implies that in the presence of constant stimulation each motile cell will decide for itself, without synchrony to nearby cells. In contrast, in a situation where stimuli change over time beyond a certain threshold – at least three-fold variation in amplitude – cells would be broadly coordinated. Uncoordinated movement may maximize the volume randomly patrolled by cells, while coordinated movement may be optimal to reach a specific target location.

We thus speculate that NF-κB oscillations may have adaptive value in achieving oscillatory expression of genes involved in movement and direction, and the cells’ decision between uncoordinated or collective action. In conclusion, we suggest that the oscillatory dynamics of NF-κB (and other transcription factors) is a means of segmenting time to provide opportunity windows for decision.

## Materials and methods

Please note that this section contains both technical details and supplemental information explaining the rationale behind our experimental approaches. We also refer here to Figure supplements that are also discussed in the main text.

### Cell lines and cell culture

GFP-p65 knock-in fibroblasts were provided by M. Pasparakis (details in De Lorenzi et al (2009); Sung et al (2009)) and cultured in phenol-red free DMEM, with 10% FCS, 50 µM β-mercaptoethanol, 1x L-glutamine, 1x sodium pyruvate, 1x non-essential amino acids, and 1x pen/strep in standard tissue culture plastic.

GFP-p65 fibroblast cultures were started from original aliquots frozen upon arrival from Pasparakis' lab and tested every week to exclude mycoplasma contamination using approved kits. Since there are no approved STR profiling protocols for mouse cells ((Yu et al., 2015) and http://www.atcc.org/Global/FAQs/0/A/STR%20Testing%20Service%20-%20STR%20on%20mouse%20cell%20lines.aspx), we carefully tested our cells for the presence of non-green cells (not expressing GFP-p65) that could represent a cross-contamination of the original culture.

For imaging experiments, cells were plated one day before the experiment in CellASIC™ ONIX M04S-03 Microfluidic Plates at low density to avoid confluence on the day of the experiment (e.g. Figure 1—figure supplement 1A). These plates consist of chambers for cell culture connected through microfluidic channels to a series of reservoirs containing media with selected concentrations of stimuli that can be flown through the chambers. Of note, to avoid cell stress or toxicity, the microfluidic plates are primed with 10%FCS in DMEM for 2–4 hr before cell plating.

Before imaging, DMEM-0.1% FCS medium containing 50 ng/ml of the nuclear dye Hoechst33342 was replaced in the microfluidic chambers 3 hr prior to the experiment using the microfluidic platform, see details on the use of the CellASIC™ ONIX below. Mouse recombinant TNF-α (R&D Systems) was diluted in DMEM-0.1%FCS as specified in the text and added in the plate reservoirs. It is relevant to note that TNF-α activity is maintained after 12 hr incubation in the plate reservoirs at 37°C, indicating that TNF-α degradation is negligible when it is not in contact with the cells (Figure 1—figure supplement 1D).

### Microfluidics

The CellASIC® ONIX Microfluidic Platform allows to apply sharp stimuli by quickly replacing the medium in the cell chambers. The flexible proprietary software allows the delivery of medium containing different concentrations of TNF-α for specific time sequences for more than 10 hr while cell are imaged. The protocols are available upon request. The medium flows in the channels around the microfluidic chambers and diffuses through the perfusion barrier, minimizing the undesirable effect of shear stress (Babini et al., 2015) (see Figure 1—figure supplement 1A,B). The small volume of medium in the chambers (less than 1 µl) is replaced fast even at low pressures, as confirmed by the sharp oscillatory profiles obtained even for high frequency stimuli. In spite of the low pressure applied (1 psi), the flow rates of 10 µl/hr (manufacturer's website) are in the same order of magnitude as the 200 nl/min used in Kellogg and Tay (2015). We also generated “sawtooth-like” profiles as in Kellogg and Tay (2015) by periodically replacing the medium with a 15 min pulse and stopping the flow. However, the cell-to-medium ratio in our culture chambers might be different and relevant for TNF clearance due to cell-linked decay needed for the sawtooth profile.

### Live imaging and detection of NF-κB dynamics

Live cell imaging of GFP-p65 knock-in MEFs was performed using a Leica TCS SP5 confocal microscope with an incubation system where cells were stably maintained at 37°C in 5% CO2. Time-lapse images were acquired at 6 min intervals for more than 15 hr. We used a low magnification objective (20x, 0.5 NA) and an open pinhole (Airy 3), ensuring that the image depth (10.7 µm) contains the thickness of the whole cell so that images are a record of the total cell fluorescence. GFP-p65 is imaged with the 488 nm Argon laser (GFP channel) while Hoechst 33342 stained nuclei are imaged with the low energy 405 nm UV diode laser at 5% of its maximum intensity (HOE channel). Images were acquired as 16 bit, 1024×1024, TIFF files. Experiment replicates were acquired on different days starting from different batches of frozen cells (samples provided as Videos 1–5).

Nuclei were stained with Hoechst 33342 for imaging, segmentation and tracking (Zambrano et al., 2014a) without any interference with the natural signalling dynamics (see below for a description of the controls performed).

### Safety assessment for Hoechst staining

Stress from photo-damage during live-cell imaging can hamper cell biology studies (Cole, 2014), while nuclear dyes can interfere with the natural signaling dynamics (Ge et al., 2013; Martin et al., 2005). Hence different controls were performed to exclude distortions of the natural signalling in our imaging conditions.

#### Apoptosis and cell death

We noticed that cells under a constant flow of fresh medium do not display apoptotic events until very late in the experiments (10–12 hr; Video 2). Importantly, unstimulated cells are viable and undergo mitosis despite the presence of low serum concentration (0.1% FCS). In contrast, cells receiving a constant flow of TNF in the absence of Hoechst and UV imaging undergo apoptosis (Video 1), with a frequency that is proportional to the TNF concentration (Figure 1—figure supplement 7). The imaging fields contain detectable apoptotic cells after 3, between 6 and 9 or after 12 hr of stimulation with 10, 1 or 0.1 ng/ml of TNF, respectively. This suggests that cell death observed in Video 1 was due to the continuous flow of 10 ng/ml TNF-α and not due to the imaging conditions.

#### Photo-damage

The cells were either imaged for 15 hr in the presence of Hoechst or left without Hoechst and not imaged; we then immunostained cells to detect thymine dimers formation. Immunostaining intensities (Figure 1—figure supplement 6) are extremely low in cells exposed to Hoechst and imaging, especially when compared to cells exposed to UVC radiation. This suggests that imaging does not produce thymine dimers or that thymine dimers are repaired fast and do not accumulate in the cells.

To further exclude the possibility of DNA damage, we checked for the presence of gammaH2AX, which is a marker for early DNA repair after formation of DNA double strand breaks (DSB) (Turinetto and Giachino, 2015; Yang et al., 2015) and late DNA repair after the formation of UV-induced thymine dimers (Oh et al., 2011; Staszewski et al., 2008).

Again, the signal for gammaH2AX (Figure 1—figure supplement 7) is extremely low in imaged cells, when compared to the signal from cells treated with doxorubicin, which induces DSBs. Of note, the phosphorylated form of H2AX is found at DNA polymerase stalled forks (Turinetto and Giachino, 2015) as marker of replicative stress. This observation may explain the minimal signal present in some of the imaged cells. All together these results indicate negligible DNA damage in the conditions considered.

#### Interference with NF-κB dynamics

We performed a manual tracking of cells that received a constant flow of TNF-α but were not exposed to Hoechst nor to UV light (“unstained/non-imaged cells”, Figure 1—figure supplement 9). Manual segmentation of nuclei is simple when nuclei are either empty or full of p65, but becomes unreliable when concentrations in nucleus and cytoplasm are similar. Despite this caveat, we found a good qualitative agreement of dynamics in unstained/non-imaged cells with the heterogeneous but damped oscillatory dynamics observed under Hoechst/UV imaging conditions, as shown in Figure 1—figure supplement 9. Therefore, the p65 dynamics described in our manuscript represents the biological effect of stimulation with TNF-α, and is essentially undistorted by imaging.

### Immunobloting and immunostaining

Staining was performed according to manufacturers’ instructions. For WB, we used an anti p65 Rab (dil 1:1000, #sc-372 C20, Santa Cruz; Figure 1—figure supplement 10). For immunostaining we used anti gammaH2AX Mab (dil. 1:500; #05-636, Millipore; Figure 1—figure supplement 7) and anti thymine dimers TDM-2 (dil. 1:2000, Cosmo Bio, Japan (Komatsu et al., 1997); Figure 1—figure supplement 6). UV-photodamage was induced with 254 nm UV irradiation using an UVC 500 Crosslinker, Amersham. Panels in Figure 1—figure supplements 6 and 7 are representative of 3 independent experiments.

### Quantification of NF-κB dynamics

The following short description summarises the whole process in few sentences. Each passage will be then thoroughly described in the next paragraphs.

The dynamics were quantified by computing the nuclear to cytoplasmic ratio of the intensities (NCI) of single cells, which is a measure robust against distortions and reflects faithfully the oscillations in the nuclear concentration of NF-κB oscillatory dynamics. This holds true provided that the total amount of p65 is constant, as we show for our cells under stimulation (see Figure 1—figure supplement 9), and is also assumed by mathematical models (see Hoffmann et al (2002) and the more recent in Kellogg and Tay (2015)). Interestingly, p65 is not constant in macrophages stimulated with LPS (Sung et al., 2014). The analysis of time series relies on the detection of significant peaks, performed following our previously discussed procedure (Zambrano et al., 2014a) that allows to distinguish significant peaks from noisy peaks. Once peaks are detected we assign them a phase: 2π for the “maxima” and π for the “minima” between peaks.

### Selection of the quantifier of NF-κB dynamics

In order to assess the oscillations for a larger number of cells, we optimized our software (Zambrano et al., 2014a) to calculate the nuclear to cytoplasmic ratio of the intensity (NCI) of NF-κB signal for hundreds of cells; NCI is a quantifier that has been used by other groups (Ashall et al., 2009; Nelson et al., 2004). As we argue below, thanks to the fact that the total amount of NF-κB is constant (Figure 1—figure supplement 10), NCI depends univocally and monotonically on the nuclear amount of NF-κB. More importantly, due to the fact that it is a ratio of intensities, it is robust and independent of slight changes in the focus and in the laser intensity, among other possible experimental distortions, which are observed in our setup. The same rationale brought us to use ratios of intensities in our previous works (Sung et al., 2009; Zambrano et al., 2014b). Importantly, these distortions imply that the background-adjusted mean nuclear intensity used in other studies (Kellogg and Tay, 2015; Lee et al., 2014; Sung et al., 2014), although advantageous for other reasons (it only requires the segmentation of the nuclei and estimation of the background) would not be appropriate in our imaging experimental setup.

We provide below a more detailed argumentation of these ideas.

Following the notation of Zambrano et al (2014b) we have that the intensity measured in pixel p of the image at time t in a time lapse experiment can be described as:

$$
I(p,t)=A(p,t)P(p,t)+Bp,t
$$

where P(p,t) is the amount of NF-κB in pixel p, A(p,t) is the amplification coefficient between the protein brightness and the amount of protein and B(p,t) corresponds to the background. In our experiments with time-varying intensities, it is clear that both A(p,t) and B(p,t) vary in time, and presumably also in space, due to laser variations and/or slight variations in the illumination uniformity.

Our quantifier NCI, that we estimate using our software, is the ratio of the background corrected average intensities in the nucleus and the cytoplasm $I(t)_{nuc} and I(t)_{cyto}$ respectively, and can be defined using this notation as:

$$
NCI(t)≡\frac{I(t)_{nuc}}{I(t)_{cyto}}=\frac{S_{cyto}}{S_{nucleus}}\frac{\sum_{p\innucleus}I(p,t)-B(p,t)}{\sum_{q\incytoplasm}I(q,t)-B(q,t)}=\frac{S_{cyto}}{S_{nucleus}}\frac{\sum_{p\innucleus}A(p,t)P(p,t)}{\sum_{q\incytoplasm}A(q,t)P(q,t)}
$$

so we have that, if we consider that A(p,t) is approximately constant and equal to certain A(t) in the area occupied by the cell (as it is in our images):

$$
NCI(t)≅\frac{S_{cyto}}{S_{nucleus}}\frac{A(t)\sum_{p\innucleus}P(p,t)}{A(t)\sum_{p\incyto}P(q,t)}=\frac{S_{cyto}}{S_{nucleus}}\frac{(NF−κB_{nuc}(t))}{(NF−κB_{cyto}(t))}
$$

where Scyto and Snuc are the areas occupied by cytoplasm and the nucleus, respectively. Our quantifier is hence a good indicator of the ratio of the amount of NF-κB in the nucleus and in the cytoplasm. However the numerator and denominator of this ratio can fluctuate due to biological reasons and this might blur the existence of oscillations in the nuclear amount of NF-κB. But this is not the case, due to the fact that the total amount of NF-κB is constant for our stimulated fibroblasts. This has been assumed in different mathematical models present in the literature, from the seminal paper (Hoffmann et al., 2002) to more recent papers (Kellogg and Tay, 2015). Interestingly, though, this view has been challenged by the recent work of Sung et al. (2014), which shows that in macrophages under LPS stimulation p65 is regulated by a positive feedback. Thus, to confirm that our assumption is reasonable, we quantified p65 by western blotting for our cells under 10 ng/ml TNF-α at several timepoints from 1 to 8 hr. The results are shown in (Figure 1—figure supplement 10), showing no significant change in the p65 levels upon stimulation. Hence, we consider our assumption valid. This implies that:

$$
NCI(t)=\frac{S_{cyto}}{S_{nucleus}}\frac{(NF−κB_{nuc}(t))}{(NF−κB_{TOT})−(NF−κB_{nuc}(t))}
$$

hence we can see that NCI(t) depends monotonously on $(NF−κB_{nuc}(t))$, see Figure 1—figure supplement 9B. For this reason, it is intuitively clear that each local maximum or minimum of $(NF−κB_{nuc}(t))$ leads to a local maximum or minimum of $NCI(t)$. Hence, oscillations in the nuclear amount of NF-κB will be observed also using NCI(t). We can put this mathematically by saying that oscillations in the nuclear concentration of NF-κB occur at times t for which the condition $(NF−κB_{nuc}(t))'=0$. Similarly, oscillations in NCI will depend on the value of the derivative of NCI, that is:

$$
NCI'(t)∝\frac{((NF−κB_{TOT})−(NF−κB_{nuc}(t))+1)}{((NF−κB_{TOT})−(NF−κB_{nuc}(t)))^{2}}(NF−κB_{nuc}(t))'
$$

so from the above formula it is easy to see that:

$$
NCI'(t)=0↔(NF−κB_{nuc}(t))'=0
$$

Overall, then, imaging, mathematical and biochemical arguments confirm that computing $NCI(t)$ is an adequate way to quantify oscillatory dynamics.

Concerning the background-corrected average intensity, using the above notation it would be calculated as:

$$
I(t)_{nucleus}=\frac{1}{S_{nucleus}}\sum_{p\innucleus}I(p,t)−B(p,t)=\frac{1}{S_{nucleus}}\sum_{p\innucleus}A(p,t)P(p,t)
$$

thus $I(t)_{nucleus}∝\sum_{p\innucleus}P(p,t)=NF−κB_{nuc}(t)$ for all t only if $A(p,t)$ were constant in all time frames. As argued previously, this is not the case in our setting and that’s the reason why we preferred to use NCI.

Finally, variations in the areas of the nucleus and the cytoplasm might introduce small distortions, although they typically vary seldom and slowly. Notice though that our software discards cells for which the areas change abruptly, which typically is an indicator of imminent mitosis or cell death. We cannot totally exclude variations of p65 at single cell level, provided that we measured it using a population assay; however, p65 turnover is known to be long, so its slow variation would contribute with a small term in the derivative and thus would just slightly distort the times for which peaks in NCI appear compared to those of the nuclear concentration. To conclude, we think that NCI would still capture the peaks and hence would be able to assess the cell's oscillatory state, which is our aim here.

The data provided confirm the validity of NCI as a quantifier. First, we have that NCI(t) remains reasonably constant – except for some spontaneous oscillations, as previously reported (Zambrano et al., 2014b) for cells that are not stimulated, as shown in Figure 1—figure supplement 9A. This is remarkable because the movie from which these series were obtained present considerable variation in the image intensity (see the Video 2). Along the same lines we do not find upwards or downwards average trends in our data of NCI time series for different conditions discussed in the main figures and in the figure supplements, which indicates further that the time series are properly normalized and reflect well the dynamics. As an additional confirmation, we have plotted together the average nuclear intensity and the NCI values obtained from manual segmentation in Figure 1—figure supplement 9C, that show the same kind of qualitative behavior as NCI but with different trends, as expected. A last indicator of the sensitivity of the quantifier comes from its ability to detect even small oscillatory peaks, see Figure 3 and Figure 3—figure supplement 1 as an example. Overall, then, NCI is a faithful measure of the oscillatory state of our cells.

### Automated analysis of time-lapse experiments data

The major advantage of considering NCI with respect to the nuclear to total ratio used in Zambrano et al (2014a) is that it does not require a perfect segmentation of the cytoplasm, which might be complicated when cells touch each other. We developed a software that uses this quantifier and is thus able to multiply by a factor of 2 the number of cells tracked, and by a factor of 1.5 the average tracking time with respect to the one described in Zambrano et al (2014a).

The software used to calculate NCI is provided as source code and works as follows: for each time-lapse experiment, we have N frames images in the HOE channel and in the GFP channel, respectively. Nuclei were segmented and used for cell tracking following the procedure described in Zambrano et al (2014a). In order to estimate the average cytoplasmic intensity, the background was computed by taking a square area centred on the cell nucleus, dividing it in tiles and using the one with the smallest average intensity in the GFP channel to estimate the background intensity (this procedure gives values compatible with the values obtained using a clustering-based algorithm). Points belonging to the cytoplasm are those around the nucleus in a size window equal to 1.5 times the size of the nucleus. The average cytoplasmic intensity is computed from the intensity in the GFP channel of the pixels from this “ring”. An example is shown in Figure 1—figure supplement 1D.

Dividing or apoptotic cells were identified assessing their geometrical features (abrupt changes in size of the nucleus and of the “cytoplasmic ring”) and discarded automatically.

### Time series analysis

To analyse the resulting NCI time series, we adapted our peak detection algorithm (Zambrano et al., 2014a). We consider peaks as a sequence of a local minimum, local maximum and local minimum. The value of the peak θ is defined by the height of the peak (from the highest minimum to the maximum). A peak defined by only three consecutive time points is considered a noise peak. We plot the distribution of the noise peak values obtained from our unperturbed and chronic stimulation time series (Figure 1—figure supplement 2A), for which we observe our previously reported spontaneous activations (Zambrano et al., 2014a). We find that these noisy peaks have a low value, and hence by considering as significant those with a value over θ>0.15, we find a reasonably good compromise between the need to ignore noise peaks and the need to detect small peaks of valuable dynamical information. This was tested in a number of time series, and an example of time series with the significant peaks detected using this threshold is shown in Figure 1—figure supplement 2B. Calculations of magnitudes inferred from peaks take advantage of time series from cells that were tracked for at least 7 hr.

Following (Mondragon-Palomino et al., 2011) we used the peaks to assign a phase value: peak maxima are assigned a phase 0 (2π) and a phase π is assigned to peak minima. This was of particular interest to obtain an assessment of the oscillatory modes present in our system, provided that peaks can be very heterogeneous and plotting the peak height in colour-plots might make it difficult to appreciate the smaller ones and hence the possible resonant oscillatory patterns. An example of this transformation is shown in Figure 1—figure supplement 2C, which is the phase derived from the peaks obtained of the time series displayed in Figure 1—figure supplement 2B. As in Mondragon-Palomino et al (2011) we use the phase difference between the time series and the forcing to quantify the degree of synchrony. The phase difference Δφ was calculated from the timing ΔT between the beginning of each forcing cycle and the closest significant peak, as Δφ=2πΔT/Tf, where Tf is the forcing period. The entropy of the distribution of the phase is calculated as:

$$
S=−\sumkp_{k}logp_{k}
$$

where pk is the probability of the kth bin (we use eight bins for all the conditions considered). The synchrony intensity is then computed as:

$$
η=1−S/S_{max}
$$

where Smax is the value obtained for equal values of pk.

### Quantitative real-time PCR

Total RNA was isolated using the IllustraRNAspin Mini kit (GE Healthcare), and complementary DNA (cDNA) was obtained by retro-transcription with Random Hexamers and SuperScript II Reverse transcriptase (Invitrogen) following the manufacturers’ instructions. Primers for the detection of mature transcripts were designed in adjacent exons and spanned the intervening intron; primers for nascent transcripts were located across an exon-intron boundary. Primer sequences are listed in Supplementary file 1.

Quantitative real-time PCR was performed with SYBR Green I protocol using the LightCycler480 (Roche). The results are shown as averages of three technical replicates. Analysis was performed with the –ΔCt method corrected for primer efficiencies (Vandesompele et al., 2002) and normalised with two reference genes (Actb and Rplp1) (Nordgard et al., 2006). Experiments were repeated twice.

It is important to emphasize that we did not stain our cells nor did we illuminate them with our UV laser in our transcription experiments, neither in the RT-PCR assays nor in the Microarray experiments described below. The controls described previously show that the nuclear labelling and the imaging do not interfere with NF-κB signalling dynamics, so we expected the same for NF-κB-driven transcription. To further confirm this, we compared RT-PCR quantifications of transcription in cells stimulated with TNF and cultured in imaging medium (0.1% FCS+Hoechst) or standard MEF medium (10% FCS). The results for nascent and mature IκBα and Ccl5 transcripts reported in Figure 5—figure supplement 2 show no difference in the transcriptional response in the two conditions.

### Microarray experiments

RNA samples were extracted using the IllustraRNAspin Mini kit (GE Healthcare). Following extraction, RIN (RNA Integrity Number) was >9 (BioAnalyser, Agilent RNA Nano Kit). RNA samples (500 ng) were reverse transcribed with the IlluminaTotalPrep RNA Amplification Kit (Ambion) and copy RNA (cRNA) was generated with 14 hr in vitro transcription reactions and checked at the BioAnalyser. Washing, staining, and hybridization were performed according to standard Illumina protocols. cRNA samples were then hybridized to IlluminaBeadChip Array MouseRefSeq-8 v2. BeadChips were scanned with BeadArray™ Reader in channel 2. The data have been uploaded on the Dryad Digital Repository (Zambrano et al., 2016). Experiments were repeated twice.

### Bioinformatic analysis of microarray experiments

Genome Studio’s bead summary probe level data – not normalized and not background corrected – were analyzed using Bioconductor. We performed quality assessment by plotting the intensities of regular and control probes. Sample intensities were quantile normalized and filtered for expression and probe quality using beadarray R package: only probes with detection P-value <0.05 in at least one condition and whose categories is defined “Perfect” or “Good” were kept. Probes were labelled as deregulated if their absolute log2 fold change relative to the 0 time point were greater than 1.

Clustering was performed applying a soft clustering of deregulated probes with the Mfuzz R package, which is suggested for microarray time course-data (Kumar and Futschik, 2007). The optimal number of clusters was assessed with the d.min function. To focus on the shape of the gene expression profiles, we standardised the gene expression profiles by taking the usual base-two logarithm and normalizing to obtain mean 0 and standard deviation 1. The algorithm then groups genes based on the Euclidean distance between profiles and the c-means objective function, which is a weighted square error function. Each gene is assigned a membership value between 0 and 1 for each cluster. Hence, genes can be assigned to different clusters in a gradual manner. The parameters m defines the degree of “fuzzification”. It is defined for real values greater than 1 and the bigger it is the more fuzzy the membership values of the cluster. We used an m value estimated by the “mestimate” function of 1.5. Membership values indicate the similarity of vectors to each other defining a cluster cores. To extract list of genes belonging to the cluster cores, we used the “acore” function taking from each clusters all genes with a membership value of at least 0.5.

Pathway analysis of genes contained in each cluster was performed with the ClusterProfiling R packages using an adjusted p-value cut-off for enrichment <0.2 based on the hypergeometric distribution (Yu, 2015). We used for our analyses the Reactome database. In order to simplify the resulting output we plotted only the top five categories of the second and third level (Yu, 2015). Conversely, overlaps were calculated based on all categories of the second and third levels. The overlap coefficient (or Szymkiewicz-Simpson coefficient) between gene sets X and Y is given by:

$$
overlap (X,Y)=\frac{|X ∩ Y|}{min(|X|, |Y|)}
$$

For statistical significance we performed a Fisher's Exact Test for evaluating if the resulting clusters where enriched for NF-κB's targets. The resulting p-value has been converted in a significance measure (-Log10(p value)). We used both a list taken from Li et al (2014) and from Thomas Gilmore’s website, Boston University (http://www.bu.edu/nf-kb/gene-resources/target-genes/).

### Mathematical modelling

We propose here a mathematical model based on the one discussed in Zambrano et al (2014b) that adds the layer of regulation by considering the negative feedback provided by the protein A20 that blocks IKK activation upon stimulation (Figure 1—figure supplement 4). For the sake of completeness, we describe briefly below the basic process that we considered, together with the biochemical rates involved (values are given in Supplementary file 2) and a summary of our normalization procedure. Additional details on the motivations underlying certain selection of biochemical reactions and variables of interest can be found in that paper. Being a simple model, it provides important qualitative insights on the possible variety of single-cell dynamics, but we also use it to provide quantitative fittings of the average population dynamics and transcription.

### NF-κB activation and IκBα feedback

The biochemical reactions described here are essentially the basic ones given in the simple model given in Zambrano et al (2014b). The basic simplification of our model is to consider that free NF-κB is nuclear, while the complex with the inhibitor IκBα is cytoplasmic. The formation of the complex is given by (NF-κB:IκBα)

$$
NF−κB+IκB\alpha→A(NF−κB:IκB\alpha)
$$

that can also spontaneously dissociate

$$
(NF−κB:IκB\alpha)→dNF−κB+IκB\alpha
$$

An external signal can lead to the appeareance of IKKa that can free NF-κB by degrading of IκBα in the complex

$$
(NF−κB:IκB\alpha)+IKK_{a}→PNF−κB+IKK_{a}
$$

and in its free form

$$
IκB\alpha+IKK_{a}→κPIKK_{a}.
$$

The negative feedback loop is enabled by the fact that the gene encoding $IκB\alpha$, $G_{\alpha}$, can be activated by NF-κB

$$
G_{\alpha,OFF}+NF−κB→K_{on,I}G_{\alpha,ON}+NF−κB
$$

while the inactivation is modulated by

$$
G_{\alpha,ON}+IκB\alpha→K_{off,I}G_{\alpha,OFF}+IκB\alpha.
$$

Notice that we are assuming here that IκBα plays a role as transcriptional repressor, as suggested by experimental results (Arenzana-Seisdedos et al., 1995) and used in some mathematical models (Kellogg and Tay, 2015; Lipniacki et al., 2007; Tay et al., 2010), but not others (Ashall et al., 2009; Sung et al., 2014). We show later that this does not have a strong impact on the fittings, but to facilitate the correspondence with our previous work and in line with the mentioned modelling approach, we opt to keep this process for all the gene inactivations considered in most of our explorations. We only briefly explore the effect of setting the koff=0 in Figure 6—figure supplement 7, results are detailed in the text.

We also consider that the gene can be basally activated

$$
G_{\alpha,OFF}→k_{on0,I}G_{\alpha,ON}
$$

and inactivated

$$
G_{\alpha,ON}→k_{off0,I}G_{\alpha,OFF}
$$

Transcription (mRNA production) is given by

$$
G_{\alpha,ON}→K_{RI}G_{\alpha,ON}+IκB\alpha_{RNA}
$$

while the RNA degradation is given by

$$
IκB\alpha_{RNA}→d_{RI}∅.
$$

$IκB\alpha$ translation is given by

$$
IκB\alpha_{RNA}→K_{I}IκB\alpha
$$

while its spontaneous degradation is given by

$$
IκB\alpha→d_{I}∅,
$$

a degradation that is also possible while it is forming the complex

$$
(NF−κB:IκB\alpha)→\gammad_{I}NF−κB
$$

#### IKK activation and A20 feedback

The protein A20 is known to provide a negative feedback by modulating IKK activation process (Ashall et al., 2009). We summarize this in our new mathematical model using the following processes in which we just model the evolution of the active form, IKKa.

Given a external time dependent TNF-α variation, TNF(t), characterized by certain values of the alternating doses, D1 and D2 in times T1 and T2, we will assume that the appearance of the active IKK, IKKa, can be summarized as:

$$
TNF(t)→K(A20)IKK_{a}.
$$

In a situation of constant flow of TNF-α the value of TNF(t) would be constant and equal to a dose D.

The biochemical rate of this equation, K(A20), is the only rate that we consider as variable. In doing so, we aim to summarize in just one biochemical reaction the fact that A20 contributes to block IKK activation (Ashall et al., 2009) instead of modelling the whole IKK activation module, so

$$
K(A20)=\frac{K_{S}}{1+\frac{A20}{A20_{0}}^{n}}
$$

IKK gets spontaneously inactivated as

$$
IKK_{a}→d_{K}∅.
$$

The gene encoding A20 is regulated by the same activation and inactivation processes as IκBα so

$$
G_{A20OFF}+NF−κB→K_{on,A20}G_{A20,ON}+NF−κB
$$

$$
G_{A20,ON}+IκB\alpha→K_{off,A20}G_{A20,OFF}+IκB\alpha
$$

$$
G_{A20,OFF}→K_{on0,A20}G_{A20,ON}
$$

$$
G_{A20,ON}→K_{off0,A20}G_{A20,OFF}
$$

Transcription is given by

$$
G_{A20,ON}→K_{R,A20}G_{A2,ON}+A20_{RNA}
$$

while the RNA degradation is given by

$$
A20_{RNA}→d_{R,A}∅
$$

finally A20 is translated as

$$
A20_{RNA}→K_{A}A20
$$

and it is spontaneously degraded as

$$
A20_{}→d_{A}∅
$$

#### Transcription of an NF-κB controlled gene

As for the genes encoding for A20 and IκBα, we consider that for any NF-κB controlled gene transcription is regulated by the processes

$$
G_{OFF}+NF−κB→K_{on,G}G_{ON}+NF−κB
$$

$$
G_{ON}+IκB\alpha→K_{off,G}G_{OFF}+IκB\alpha
$$

$$
G_{OFF}→K_{on0,G}G_{ON}
$$

$$
G_{ON}→K_{off0,G}G_{OFF}
$$

while the RNA produced from the gene is provided by

$$
G_{ON}→K_{R}G_{ON}+A20_{RNA}
$$

and its degradation is given by

$$
G_{RNA}→d_{R,G}∅
$$

#### Model equations, normalization and parameter selection and uncertainty

The equations of the model are derived using mass-action kinetics and performing a normalization in much the same way as in Zambrano et al (2014b). We describe below the process, using the same symbols to represent biochemical species and their copy number.

First, as in previous existing models and as suggested by our experiments, the total amount of NF-κB, free plus bound to the inhibitor, remains constant and equal to NF-κB0 so we define N=NF-κB/ NF-κB0. We also normalize the amount of inhibitor as I= NF-κB/ NF-κB0 and the amount of A20 as A= A20/ A200 and K=IKK/IKK0, where A200 and IKK0 are amounts of reference in such a way that N, I and A are adimensional variables of the order of 1. On the other hand, for any gene we have that the maximum number of on states is G0=2 (the two alleles), so GI, and GA are a number between 0 and 1 representing the fraction of active genes encoding for IκBα and for A20, respectively – it is a continuous approximation to a discrete variable. Finally, notice that using our notation the maximum number of active genes is G0 so it can be proved that the maximum asymptotic value of the amount of RNA of the biochemical species X is of the form KR,X·G0/dR,X. Hence, we define the variables RI, and RA as proportional to the amount of mature RNA of IκBα and A20, respectively, via the relations

$$
R_{I}=IκB\alpha _{RNA} ·d_{R,I}/(K_{RI}·G_{0}) and R_{A}=A20_{RNA} ·d_{R,A20}/(K_{R,A20}·G_{0}).
$$

Overall, these normalizations allow one to pass from biochemical species with copy numbers of different orders of magnitudes to adimensionalized variables that are of the order of 1.

By using them, and renaming combinations of constants (in such a way that lowercase parameters are obtained from uppercase biochemical reaction rates), we have the following model of ordinary differential equations describing the dynamics of our system:

$$
\frac{dK}{dt}=−d_{K}·K+\frac{1}{1+(A)^{n}}S(t)
$$

$$
\frac{dN}{dt}=d·(1−N)+\gamma·d_{I}(1−N)+p·K·(1−N)−a·I·N
$$

$$
\frac{dG_{I}}{dt}=(k_{onI}N+k_{on,0,I})(1−G_{I})−(k_{offI}I+k_{off,0I})G_{I}
$$

$$
\frac{dR_{I}}{dt}=d_{RI}(G_{I}−R_{I})
$$

$$
\frac{dI}{dt}=d·(1−N)−κ·p·K·I−a·I·N+k_{I}·kR_{I}−d_{I}·I
$$

$$
\frac{dG_{A}}{dt}=(k_{on,A}N+k_{on,0,A})(1−G_{A})−(k_{off,A}I+k_{off,0,A})G_{A}
$$

$$
\frac{dR_{A}}{dt}=d_{RA}(G_{A}−R_{A})
$$

$$
\frac{dA}{dt}=k_{A}·R_{A}−d_{A}·A
$$

The parameters used as starting point in our explorations and the fittings can be found in the source code folder for mathematical modelling, while the original biochemical rates from which they were derived can be found in Supplementary file 2. Normalised parameter values are provided in the source codes. Many of them have the same values as the ones provided in Zambrano et al (2014b). Additional parameters were manually fitted or extracted from (Tay et al., 2010), as we did previously. Notice that the degradation rates of the kinase, the RNAs and the proteins appear as parameters in the equations above, unchanged. The remaining parameters are related to the original biochemical rates as p=P·IKK0,a=A·NF-κB0, kI=KI·KR,I·G0/(dR,I·NF-κB0), kA=KA·KR,A·G0/(dR,A·A200), kon,I=Kon,I· NF-κB0, koff,I=Koff,I· NF-κB0, kon,A=Kon,A· NF-κB0, koff,A=Koff,A· NF-κB0. S(t) is the normalized signal, in such a way that a constant TNF = 10 ng/ml is equivalent to S(t)=2 h-1 in the system of equations. For lower doses we use lower values of S.

Notice that the adimensionalization leads to a number of parameters smaller than the total number of biochemical rates and constants of the original system. Equations 2–5 are identical – except for the inclusion of spontaneous gene activation-inactivation – to the ones proposed in our previous minimal model of the regulatory network (Zambrano et al., 2014b). Equation 1 models the effect of A20 as inhibitor of the kinase activation. This second negative feedback is completed with Equations 6–8, that explicit NF-κB control of A20 expression.

As shown below, we use this model both to fit the observed dynamics and for numerical exploration of the dynamics observed under different stimuli. For simplicity, we call PNF-κB to the set of parameters of Equations 1–8 and PS to the parameters describing the parameters of the external signal, that can either be constant or a time varying rectangular forcing signal as shown in Figure 1A. Following what we did in previous numerical explorations (Zambrano et al., 2014b) we associate to each parameter an uncertainty degree D, so each parameter can be randomly varied by multiplying it by a factor in the interval [10-D, 10D] with D smaller or equal than 1. In other words, parameters with higher uncertainty degree can be varied up to one order of magnitude above or below their selected initial value, which is itself a moderate variation. Those degrees are specified in Supplementary file 2: note that we choose higher values of D for manually fitted parameters and lower for those from the literature or from our own measurements. We also consider a high value of D for parameters that summarize many different processes or for those in which our model is less detailed, as in the IKK activation – A20 regulatory module.

Finally, the equations for a gene under the control of NF-κB are:

$$
\frac{dG}{dt}=(k_{on,G}N+k_{on,0,G})(1−G)−(k_{off,G}I+k_{off,0,G})G
$$

$$
\frac{dR}{dt}=d_{R,G}(G−R)
$$

where in this case R=G RNA ·dR,G/(KR·G0), kon,G=Kon,G· NF-κB0, koff,G=Koff,G· NF-κB0. The parameters in (9) and (10) are used to model and fit different expression profiles are denoted as PG. Notice that to model the process of gene expression one needs to set PS, PNF-κB and PG. In this context, two different genes expressed under the same external stimuli conditions would share the parameters PS and PNF-κB but different values of PG. This idea is used in our fittings of dynamics and transcription in this work.

### Classification of the different dynamical responses for constant stimulus

We have observed experimentally that even for constant stimulation different dynamics are possible, with trajectories showing different degrees of dampening and sometimes even irregular and non-oscillating profiles (Figure 1—figure supplement 2D) as pointed out in previous works (Sung et al., 2009; Zambrano et al., 2014b). Our relatively simple model illustrates why this situation might arise and how a wider variety of dynamics might arise compared to the regular oscillations documented in the literature for more complicated models (e.g. (Ashall et al., 2009; Tay et al., 2010)).

To illustrate this, we analyzed the dynamics for a constant external stimulus (S(t)=2 h-1) and varying simultaneously each parameter of the parameter set PNF-κB according to their uncertainty degree D. We used them to generate trajectories and selected those giving rise to a response, i.e. those for which N(t) is bigger than 0.4 in the first 3 hr and whose average values in the last hours was smaller or equal than N=0.4. To characterized in a systematic way their dynamics, we located the fixed point of Equations 1–8 and calculated the eigenvalues {λi} (i=1,...8) of the Jacobian. In Figure 1—figure supplement 5A we plot the real and imaginary parts of each set of eigenvalues. We represent with a red dot the eigenvalues belonging to a set in which the real part of at least one of them is bigger than zero. This means that the fixed point for those parameters is unstable and hence trajectories converge to a stable limit cycle around it. In other words, for those parameter combinations sustained oscillations arise. The percentage of parameter sets giving sustained oscillations is below 10% (Figure 1—figure supplement 5B, right panel), which make us conjecture that parameters giving rise to sustained oscillations are not the norm.

We also plot in Figure 1—figure supplement 5C the parameter values giving rise to oscillating and non oscillating (but responding) trajectories. We note that the intervals are very similar except for parameters n and dA involved in the A20 negative feedback, which indicates that this feedback is critical in order to obtain a sustained or a damped oscillatory response. In previous works it was shown experimentally and through mathematical models that the interplay between the IκB and A20 regulatory modules regulate different phases of NF-κB response (Werner et al., 2008). Our numerical results suggest that it also plays a key role in the type of dynamics observed (oscillatory versus damped). Overall, this analysis further hints to the fact that it is the precise combination of parameters, rather than the precise single values, what determines the type of dynamics observed and might account for the different dynamics observed with respect to other groups (Ashall et al., 2009; Cheng et al., 2015; Kellogg and Tay, 2015; Lee et al., 2009; Sung et al., 2009; Tay et al., 2010).

Finally, we have to notice that being the system given by Equations 1–8 a dynamical system with real variables, the imaginary eigenvalues come in complex conjugate pairs. The distribution of parameter combinations with 2, 4 and 6 imaginary eigenvalues are shown in Figure 1—figure supplement 5B (left panel). Notice that an oscillatory frequency can be associated to each couple of complex conjugate pairs (Goldstein et al., 2001), so having more than one of such couples means that the dynamics will combine different frequencies.

To further illustrate all this, in Figure 1—figure supplement 5D we present examples of the variety of trajectories found. Some of them are oscillating (red), showing both smooth and spiky oscillatory peaks. Many others are damped and in some cases the concurrence of two oscillating timescales, fast and slow, is evident. Some others present clearly non-oscillating profiles. Overall, our numerical exploration of our relatively simple models shows that different dynamics are possible in presence of constant stimulation, as observed in the experiments of this and previous works (Sung et al., 2009; Zambrano et al., 2014a).

The model simulation routine was implemented in C code language and compiled using gcc. Routines for parameter variation and time series analysis and stability analysis (using the function fsolve of the Nonlinear Equations package) where written using GNU Octave.

### Parameter fitting

Routines were written in GNU octave to fit the model to the data by combining Markov Chain Monte Carlo for initial exploration of the parameter space and a Levenberg–Marquardt algorithm. Parameters of Equations 1–8 were varied within the specified uncertainty degree. The goal is to minimize the distance between a given goal signal X={X(tk)} for k=1,...,N and the theoretical values x={x(tk)} obtained from the model. We define the distance of a given fitting to the data as:

$$
d_{X,x}=\frac{1}{N}\sumk\frac{X(t_{k})−xt_{k}}{max(X(t_{k}),x(t_{k}))}
$$

When several data are fitted simultaneously, the total distance between model predictions and the data were obtained by summing each distance. Notice that the 1/N factor weighs for difference in the length of the data. For a given computations, this distance gives the average relative error per timepoint of the fitting.

- To fit NCI, theoretical NCI profiles from the model were obtained as:

$$
NCI(t)=\frac{S_{cyto}}{S_{nucleus}}\frac{N(t)}{1−N(t)}.
$$

where Scyto/Snuc is the ratio of the nuclear to total area of the cells in our image, which is estimated to be of around 1/3.

For parameter fitting of the gene expression obtained from Quantitative Real-Time and microarray experiments (see below), the fold change levels predicted by the models where computed as R(t)/R(0). For the simultaneous fitting of NCI, IκBα and Cccl5 mRNA shown in Figure 5, common PNF-κB parameters where found while for IκBα and CCL5 mRNA we independently fitted the respective set of parameters PG. For the fitting of PNF-κB the parameters were varied within the limits given by their uncertainty degree.

Fitting of the microarray data was performed by keeping constant the parameters PNF-κB obtained fitting the data of Figure 5 and varying PG (those of (9–10)) for each gene, as we did for IκBα and Cccl5. Examples are shown in Figure 6—figure supplement 6. Figure 6—figure supplement 5 shows that the distance between fitting and real data is better for genes with increased transcription with an average fitting error of 9%.
