# Author response - Round 1

Authors:
- Ariana R Andrei ([ORCID: 0000-0003-2152-2580](https://orcid.org/0000-0003-2152-2580))
- Samantha Debes
- Mircea Chelaru
- Xiaoqin Liu
- Elsa Rodarte
- John L Spudich ([ORCID: 0000-0003-4167-8590](https://orcid.org/0000-0003-4167-8590))
- Roger Janz
- Valentin Dragoi ([ORCID: 0000-0002-9526-0926](https://orcid.org/0000-0002-9526-0926))

## Response text

DOI: [10.7554/eLife.66400.sa2](https://doi.org/10.7554/eLife.66400.sa2)

First, thank you very much for your very useful comments and suggestions. In this revised manuscript we present the results of the analyses that you have recommended and describe the new control experiments we have performed. Our new findings offer additional insight into the response types revealed by cortical suppression and provide additional, strong support for our previous conclusions.

1. The most common question among reviewers was how the 4 response categories were identified, and whether a clustering method was used.

Reviewer 1: “How was the choice of four categories motivated, was this done through a clustering mechanism?”; Reviewer 2: “The authors categorized the optogenetic induced neuronal responses at a distance in four classes, which is a nice finding. It is unclear, however, how the neurons were clustered.”; Reviewer 3: “The authors should describe in detail how the classification of the 4 response types was arrived at. How was the 'Type' category defined?”

a. We took several steps to address this point (as described below).

b. We thank the reviewers and editors for suggesting the UMAP clustering algorithm. We have included the results of the UMAP clustering algorithm performed on the firing rates of the different response types, using the correctly ascribed labels (Figure 2 – supplementary figure 1D) and randomized labels (Figure 2 – supplementary figure 1E). UMAP produces 4 clear, non-overlapping clusters when firing rates across contrasts are correctly labeled with the response type, but yields only one cluster when labels are randomly assigned to the same firing rate data. This analysis demonstrates that the classification of response types based primarily on the normalization fits corresponds to differences in firing rates for individual cells and is not due to errors in fitting accuracy. This new figure has been included in the revised Figure 2 – supplementary figure 1 (page 32).

c. As suggested by the editors and reviewers, we also implemented a similar clustering analysis using the t-SNE (t-distribution stochastic neighbor embedding) algorithm, using the identical data as for the UMAP analysis above. The t-SNE algorithm produced similar results, producing better grouping of data with correct labels versus randomized labels (Author response image 1) . However, this method was not as effective compared to the UMAP method and given its redundancy we did not include this analysis in the revised manuscript.

Error ellipses represent the covariance matrix and are centered on the median of tSNE results for each type.

d. Similar to the above clustering analysis above, in order to ensure that the response types categorized using the normalization fits corresponded to the underlying firing rate changes we implemented a classifier. The classifier was trained on the differences in firing rates (laser minus control) across all contrasts for each cell using either the correct labels (Figure 2 – supplementary figure 1F, left side black bar ‘Actual’) or randomly shuffled labels (Figure 2 – supplementary figure 1F, left side gray bar ‘Chance’). The classifier was validated using 25% holdout validation. This procedure was repeated 5 times and the mean ± s.e.m. classifier performance is shown in Figure 2 – supplementary figure 1F. The overall accuracy of the linear discriminant classifier to correctly classify firing rates changes into the ascribed classes was 74.3% ±2.6 (mean ± s.e.m.) compared to 33.2% ±1.9 on the randomized data. For individual response types (Figure 2 – supplementary figure 1F, right side), the area under the receiver operating characteristics curves (‘AUC’) are all significantly above chance (colored versus gray bars), and all AUC>0.8, indicating the classifier performed well for all types. This figure is included in Figure 2 – supplementary figure 1F, and is mentioned in the text (page 6, paragraph 2).

e. As suggested, we have now included a new paragraph to address the classification as a separate issue and describes the methods in detail (page 6, paragraph 2).

f. Taken together, the results of the clustering analysis and the classifier performance convincingly demonstrate that the response types can be well separated based on the measured light-evoked changes in firing rate across contrasts. Thus the identification of 4 response classes do not rely solely on the normalization fits, nor can they be attributable to chance.

2. Reviewers 1 and 3 ask about statistical testing to ensure that the responses are unlikely to be due to chance.

a. To address whether the heterogeneity could arise by chance, we re-examined the MATLAB code where the laser and stimulus responsiveness is statistically tested for each unit and found a typographical error in the methods describing this process. The laser responsiveness of each cell was based on an α value for the Wilcoxon ranked sum test of P<0.005 (0.05 divided by 10 comparisons), not 0.05 as previously stated. To assess responsiveness to the visual stimulus we used an α value of P<0.05, since only one comparison was made for each cell (highest contrast versus 0% contrast). This has now been corrected in the revised methods section (page 27, paragraph 2). Since this method includes a stringent Bonferroni correction for multiple comparisons to identify laser responsive units, this should provide a high degree of confidence that the laser responses are not due to chance.

b. In addition to showing example cells for each response type in Figure 2A, we have also included the population firing rates for each response type in Figure 2B (page 8), showing statistics with multiple comparisons corrections. This figure was previously provided in Supplementary Figure S2.

3. Reviewers 2 and 4 raised the important point of distinguishing direct activity suppression from indirect, network-based suppression. Reviewer 4 suggested that we perform a latency analysis to differentiate direct light suppressive effects from indirect ‘Type 1’ suppressive effects.

As suggested by Reviewer #4 – to test whether the Type 1 (all suppressive) responses at the distal/indirect site could actually be due direct activation of GtACR2 by a small amount of light scattering, we performed a suppression latency analysis. That is, we compared the time required to reach the maximum suppression following the onset of both the visual stimulus and the light for cells at the direct site and for Type 1 cells found at the distal site (Figure 1 – supplementary figure 1L). We also separated the indirect Type 1 cells across layers (Figure 1 – supplementary figure 1M). As expected, we found that the suppression latency at the direct sites was significantly shorter than that at the indirect sites (31.2 ± 1.15ms versus 92.9 ±1.10ms, respectively; P=0.00074 Wilcoxon ranked sum test). Suppression at direct site was also significantly different compared to Type 1 cells across all layers (P=0.0022 ANOVA test, d.f.=3), but no differences were found across layers. This analysis supports our previous interpretation that Type1 cells at the indirect site are suppressed due to their synaptic connections with the directly suppressed cells. This is now addressed in the manuscript (page 4, paragraph 3).

4. Reviewer 3 and the editors raised concerns about the number of contrasts used to fit the contrast response functions and suggested that we perform additional experiments using 7-8 stimulus contrasts.

a. We performed additional experiments using 9 stimulus contrasts to evaluate the accuracy of our previous fitting procedure (Figure 2 – supplementary figure 2). The responses of 54 units were either fit (i) using the mean firing rates from all 9 contrasts (0, 3.5, 5, 10, 15, 25, 50, 75, and 100%), or (ii) using a subset of 5 contrasts (0, 5, 10, 25, and 100%), with a similar range as in the original experiments. However, when we compared the fit parameters obtained from the 9-point and 5-point fits, we found that they were highly similar (assessed by a Pearson correlation coefficient). In particular, the more critical parameters of c50 (Figure 2 – supplementary figure 2C) and slope (Figure 2 – supplementary figure 2D, left) both had a Pearson correlation coefficient of 0.89 (Pearson P<0.001). This is now addressed in the manuscript (page 6, paragraph 3).

b. Interestingly, the above analysis also led us to notice that a portion of cells (~30%) do not have saturating responses at high contrasts. For these cells, the Naka-Rushton fitting parameter associated with c50 no longer corresponds with the contrast that elicits 50% of the maximal response, but rather this parameter approaches 100% contrast (Figure 2 – supplementary figure 2E-F). In our previous manuscript we reported the overall mean value of Naka-Rushton c50 parameter without accounting for these cells, which led to an over-estimation of the actual c50 of the population. To correct this, in the revised manuscript we have measured the actual c50 from the fits (new Figure 3G) and moved the report of the Naka-Rushton fit parameter c50 to Figure 2 – supplementary figure 2G. We now also report the percentage of cells within each of the 4 types that exhibit this non-saturating behavior (Figure 2 – supplementary figure 2H), and show the distributions of the Naka-Rushton c50 parameters (Figure 2 – supplementary figure 2I). Importantly, please note that for the majority of cells, both the empirically-measured c50 (Figure 2 – supplementary figure 2C, above; 12.6% ± 0.98 contrast, mean ± s.e.m., n=214) and the Naka-Rushton c50 parameter was contrast (Figure 2 – supplementary figure 2I) was less than 20% – which is within the range of contrasts sampled in the original manuscript. This is addressed in the manuscript (page 11, paragraph 4).

c. As a side note, the above analysis made us wonder whether these non-saturating cells maybe do actually saturate, but only at very high contrasts that our 9-point fits did not sample. To satisfy curiosity, we recorded an additional population of 28 cells and densely sampled at high contrasts (Figure 2 – supplementary figure 2J-L, above). We found that 21% of cells indeed do not seem to saturate (Figure 2 – supplementary figure 2J). This proportion was similar to that observed in the original data (compare Figure 2 – supplementary figure 2L with Figure 2 – supplementary figure 2I, above), leading us to conclude that the cells in the original data with high (>80%) Naka-Rushton c50 parameters represent a real type of cell behavior, and is not due to under sampling of high contrasts. This is addressed in the legend to Figure 2 – supplementary figure 2 (page 33).

d. The above experiments demonstrate that the range and number of contrasts used in the original experiments are sufficient to capture the contrast response parameters almost as well as it could have been obtained using 9 contrasts. Importantly, this analysis shows that the c50 parameter for the majority of cells falls within the range of contrasts tested in the original experiments. This is discussed in manuscript (page 6, paragraph 3).

5. Reviewer 4: “… and the thickness assigned to the G layer is too large. The latter in vivo typically spans about 3, not 4, contacts (if the penetration are vertical which this appears to be).”

a. In our laminar analysis we employed the same laminar definitions as many other physiology studies (Cox et al., 2019; Dougherty et al., 2019; Van Kerkoerle et al., 2017; Westerberg et al., 2019), with a granular layer depth of ~500 microns, as supported by anatomical studies (Lund, 1973; O’Kusky and Colonnier, 1982; Vanni et al., 2020).

b. However, since there is considerable variability in the thickness of the granular layer across anatomical studies (ranging between 360 – 580 microns from our literature survey), we have redefined granular as spanning 300 microns and replotted the laminar distribution of response types for comparison (Figure 2F, Figure 2—figure supplement 3C). Our previous analysis used a convention of 400 µm. Shifting this boundary by 100 µm (1 contact difference) resulted in layer assignment changes (G to SG) for 16 cells (n=7 Type 1, n=5 Type 2, n=4 Type 3 and n=0 Type 4).

6. Reviewer 1: “The nature of the model is not entirely clear: Which variables represent the local site and which variables represent the distant site? Do both have E/I neurons? What are the connections between those?”

The model output is the firing rate of one neuron at the distant site. The activity of this neuron is driven by stimulus-related activity, as well as by excitatory and inhibitory currents representing the local network. This has been clarified in the manuscript (page 12, paragraph 2), and the model schematic has been modified to show that both the local network and the output neuron receive feedforward input (Figure 4A left, page 13)

7. Reviewer 1: “It would be useful to explain better what standard normalization models would predict. There is some discussion on this, but it is not clear why one would expect suppression of a distal site rather than activation at these retinotopic distances. In this context it would also be useful to discuss Mexican-hat profiles of activation/suppression in relationship to the present findings.”

a. We have included the following paragraphs in the discussion (starting page 17, paragraph 3):

“Heterogeneity of normalization has not been well studied, nor is it well-defined for populations of neurons. The denominator of the normalization equation represents the cumulative activity of the local network (or ‘normalization pool’). […] It is quite possible that some of the effects recorded at the 300 µm distance, could be due to activity changes that occurred at longer distance (>500 µm) primarily mediated by long-range inhibitory projections.”

8. Reviewer 2: “This study yielded a number of interesting findings, but contrary to the framing of the authors, ("unexpected" "unpredicted" "most surprising" "unpredictable", "off-target effects have never been investigated…"etc.), a variety of immediate downstream "off-target" effects after optogenetic activation and inactivation have been amply described in primates -already starting with the first optogenetic study in monkeys (Han et al., 2009). The main 'selling' point of the study is unsurprising.”

a. We have noted that previously reported paradoxical effects (i.e. Nassi et al. 2015) were noted for cells recorded within the area where light was applied (page 17, paragraph 3). The novelty of our study is that our heterogeneous responses are away from the light source, in the local network where recordings are seldom made.

b. We have added to the discussion a useful counterpoint from Li et al. (Li et al., 2019), that measures the effects of optical suppression at various distances from the light source, in the mouse (page 19, paragraph 3). This study shows that suppression, in the absence of a sensory stimulus, is localized to an area about the size of the fiber optic. Li et al. (2019) conclude that optical suppression is highly localized to the area of the light, with virtually no lateral effects. The novelty of our study is that we show that once the network is driven by a stimulus, focal suppression produces unpredictable activity ripples in the local network, which has a behavioral impact. Our study is particularly useful for future implementations of optogenetics in NHPs aiming to drive/modulate behavior, which has proven notoriously difficult.

9. Reviewer 3 “The data shown in figure 3D-G are puzzling. The P values are mostly negative, i.e. they seem subtractive, rather than additive? That suggests the network does not provide excitation, unlike stated in the main text? Also, the c50 values of many neurons appear very high, and are in a range where sampling was basically absent. All examples shown in figure 2 have c50 values much lower.”

a. Negative P parameter values are not surprising since in this experiment the local network is suppressed, and the reported P parameters are from laser trials. The actual effect of the network under normal conditions can be inferred to be the opposite of this. We have emphasized that the P and Q parameters reported here were from laser trials (page 11, paragraph 4).

b. The c50 values measured from the fits (rather than the Naka-Rushton c50 parameter) are now shown in Figure 3G. See also point 4C above.

10. Reviewer 4: “Figure 1E. rather than one example cell, it would be preferable to show the full laminar profile of suppression at the photoactivated site to demonstrate that light is, indeed, limited to the SG layers. This is shown in Figure S1B-C, but this figure is difficult to interpret correctly because the Y axis is not labeled, and the estimated top and bottom of cortex as well as L4C are not indicated on the laminar plot.”

Figure 1E is actually a population average of all directly suppressed neurons. Unfortunately we could not obtain clear laminar information for the session in Figure 1-supplementary figure 1 (formerly Figure S1), possibly owing to the presence of 2 probes. However, we did measure the vertical distance between cells that were directly suppressed by light based on the distance between recording contacts (spaced every 100 µm). We found that these directly suppressed cells were clustered within 457.1 ± 104.3 µm (mean ± s.e.m., n=31 cells with maximum suppression within 30 ms of light onset). We have included this information in the revised manuscript (page 26, paragraph 3).

11. Reviewer 4: “Isn't it odd that effects on behavioral performance in Figure S7E are only seen at 20% contrast given that type 2 cells are suppressed at contrasts {greater than or equal to} 10?”

Overall, the Type 2 cells show greater suppression for higher contrasts. This is most obvious in Figure 2A-B above, where the suppression for the 100% contrast is stronger compared to control than the degree of suppression at 10% contrast. It is likely that the 20% contrast was high enough to sufficiently induce suppression in Type 2 cells, while being low enough to observe behavioral changes.

References

Ben-Yishai R, Lev Bar-Or R, Sompolinsky H. 1995. Theory of orientation tuning in visual cortex. Proc Natl Acad Sci U S A 92:3844–3848. doi:10.1073/pnas.92.9.3844

Cox MA, Dougherty K, Adams GK, Reavis EA, Westerberg JA, Moore BS, Leopold DA, Maier A. 2019. Spiking Suppression Precedes Cued Attentional Enhancement of Neural Responses in Primary Visual Cortex. Cereb Cortex 29:77–90. doi:10.1093/cercor/bhx305

Dougherty K, Cox MA, Westerberg JA, Maier A. 2019. Binocular Modulation of Monocular V1 Neurons. Curr Biol 29:381-391.e4. doi:10.1016/j.cub.2018.12.004

Lund JS. 1973. Organization of neurons in the visual cortex, area 17, of the monkey (Macaca mulatta). J Comp Neurol 147:455–495. doi:10.1002/cne.901470404

O’Kusky J, Colonnier M. 1982. A laminar analysis of the number of neurons, glia, and synapses in the visual cortex (area 17) of adult macaque monkeys. J Comp Neurol 210:278–290. doi:10.1002/cne.902100307

Spiridon M, Gerstner W. 2001. Effect of lateral connections on the accuracy of the population code for a network of spiking neurons. Netw Comput Neural Syst 12:409–421. doi:10.1080/net.12.4.409.421

Van Kerkoerle T, Self MW, Roelfsema PR. 2017. Layer-specificity in the effects of attention and working memory on activity in primary visual cortex. Nat Commun 8:13804. doi:10.1038/ncomms13804

Vanni S, Hokkanen H, Werner F, Angelucci A, Helsinki B. 2020. Anatomy and Physiology of Macaque Visual Cortical Areas V1, V2, and V5/MT: Bases for Biologically Realistic Models. Cereb Cortex 30:3483–3517. doi:10.1093/cercor/bhz322

Westerberg JA, Cox MA, Dougherty K, Maier A. 2019. V1 microcircuit dynamics: Altered signal propagation suggests intracortical origins for adaptation in response to visual repetition. J Neurophysiol 121:1938–1952. doi:10.1152/jn.00113.2019
