# Nuclei determine the spatial origin of mitotic waves

## Authors

- Felix E Nolet<sup>1</sup> ([ORCID: 0000-0001-9300-6302](https://orcid.org/0000-0001-9300-6302))
- Alexandra Vandervelde<sup>1</sup>
- Arno Vanderbeke<sup>1</sup> ([ORCID: 0000-0002-7240-8377](https://orcid.org/0000-0002-7240-8377))
- Liliana Piñeros<sup>1</sup> ([ORCID: 0000-0001-8872-9602](https://orcid.org/0000-0001-8872-9602))
- Jeremy B Chang<sup>3</sup> ([ORCID: 0000-0002-7381-6444](https://orcid.org/0000-0002-7381-6444))
- Lendert Gelens<sup>1</sup> ([ORCID: 0000-0001-7290-9561](https://orcid.org/0000-0001-7290-9561)) †

### Affiliations

1. Laboratory of Dynamics in Biological Systems, Department of Cellular and Molecular Medicine, Faculty of Medicine, KU Leuven Leuven Belgium
2. MeBioS - Biosensors Group, Department of Biosystems, KU Leuven Leuven Belgium
3. Department of Pharmaceutical Chemistry University of California, San Francisco United States

† Corresponding author

## Abstract

Traveling waves play an essential role in coordinating mitosis over large distances, but what determines the spatial origin of mitotic waves remains unclear. Here, we show that such waves initiate at pacemakers, regions that oscillate faster than their surroundings. In cell-free extracts of Xenopus laevis eggs, we find that nuclei define such pacemakers by concentrating cell cycle regulators. In computational models of diffusively coupled oscillators that account for nuclear import, nuclear positioning determines the pacemaker location. Furthermore, we find that the spatial dimensions of the oscillatory medium change the nuclear positioning and strongly influence whether a pacemaker is more likely to be at a boundary or an internal region. Finally, we confirm experimentally that increasing the system width increases the proportion of pacemakers at the boundary. Our work provides insight into how nuclei and spatial system dimensions can control local concentrations of regulators and influence the emergent behavior of mitotic waves.

## Introduction

Traveling waves are often used in nature to transmit information quickly and reliably over large distances (Cross and Hohenberg, 1993; Tyson and Keener, 1988; Gelens et al., 2014; Beta and Kruse, 2017; Deneke and Di Talia, 2018). For example, action potentials are well known to propagate along the axon of a neuron (Hodgkin and Huxley, 1952), but a wealth of other biological processes have been shown to be coordinated via traveling waves (Winfree, 1987; Dawson et al., 1999; Loose et al., 2008; Chang and Ferrell, 2013; Deneke et al., 2016; Prindle et al., 2015; Bement et al., 2015; Fukujin et al., 2016). In particular, cell cycle oscillations also self-organize via mitotic waves in a spatially extended system (Chang and Ferrell, 2013; Deneke et al., 2016). Such waves that coordinate cell division in space are especially relevant in the large developing eggs (ranging from ≈100 µm to ≈1 mm in diameter) that are laid externally by insects, amphibians, and fish, because they are too large to be synchronized by diffusion alone (see Box 1). While several studies have addressed the potential biochemical mechanisms of mitotic waves (Chang and Ferrell, 2013; Deneke et al., 2016; Vergassola et al., 2018), what determines the spatial origin of mitotic waves remains unclear.

Here, we address this open question using cell-free extracts made from eggs of the frog Xenopus laevis, which exhibit biochemical cell cycle oscillations in vitro that are similar to those found in vivo (Murray, 1991). We find that mitotic waves originate at nuclei, which act as so-called pacemakers, regions that oscillate faster than their surroundings (Kuramoto, 1984). While previous studies have suggested centrosomes or nuclei to serve as pacemakers (Chang and Ferrell, 2013; Ishihara et al., 2014), their role in organizing mitotic waves has not been empirically demonstrated. We provide evidence that nuclei serve as pacemakers, both in the absence and presence of centrosomes. Having the nucleus setting the pace of the cell cycle may help ensure proper DNA replication prior to initiation of mitosis. If the pacemaker were elsewhere, the decision to divide might be decoupled from DNA replication, leading to division occurring before DNA replication completes. We postulate that nuclei can concentrate cell cycle regulators, leading to faster cell cycle oscillations at those nuclear locations. Nuclei and their spatial positioning, which is affected by the spatial dimensions of the system, determine how the cell cycle is coordinated in space and time.

By monitoring mitotic waves in Teflon tubes using time-lapse microscopy (see Box 2), we find that pacemakers are often located near nuclei that are brighter due to increased import of exogeneously added GFP-NLS. We show that the generation of such pacemakers does not require centrosomes and explore the influence of nuclear density and nuclear import strength on cell cycle period and pacemaker wave formation. Based on these observations, we then develop a theoretical model where nuclei play an active role in concentrating cell cycle regulators. This concentration decreases the period of oscillation around the nuclei. Our modeling shows that the distribution of regulators depends on the nuclear positioning and spatial dimensions of the system, with thicker tubes having a larger tendency to concentrate cell cycle regulators at the boundaries (i.e. outer edges of the tube). Using both numerical simulations and experiments, we go on to show that mitotic waves can originate from the system interior or from the system boundary, depending on the spatial dimensions of the system. These observed dynamics are the result of competition between waves originating from different pacemaker regions, where the relative strength of the pacemakers in the interior and at the boundary is determined by the system dimensions.

## Results

### Nuclei serve as pacemakers to organize mitotic waves

We reconstituted mitotic waves in vitro according to Chang and Ferrell (Chang and Ferrell, 2013; Chang and Ferrell, 2018). We loaded cycling extracts in a 100 µm wide Teflon tube and used green fluorescent protein with a nuclear localization signal (GFP-NLS) to image mitotic waves (see Box 2). This approach allows visualization of regular oscillations between interphase and mitotic phase. In interphase, nuclei form spontaneously in the extract supplemented with sperm chromatin. These nuclei then import GFP-NLS. In mitosis, the nuclear envelope breaks down and GFP is no longer localized to nuclei. Mitotic waves can be observed by the disappearance of nuclei in a wave-like fashion. Waves become apparent after a couple of cell cycles and they self-organize so that they emerge from more clearly defined foci (see Figure 1A, Figure 1—video 1). The origin of the wave (point P) was determined as the intersection of straight lines drawn through the points where the nuclei disappear (see orange curve and Figure 1—figure supplement 1). The wave at cell cycle 5–6 was found to propagate with a speed of ∼ 20 µm/min.

![Figure 1.](https://cdn.elifesciences.org/articles/52868/elife-52868-fig1-v3.jpg)

**Figure 1.:** (A) Mitotic waves (orange) in a kymograph of cell-free extract experiment in a 100 µm Teflon tube. Wave dynamics are shown for cell cycle 1–6. For each time point we reduced the data from two to one spatial dimension by plotting the maximal GFP-NLS intensity along the transverse section of the tube. In the zoom, indicated by the gray box, we show snapshots of the whole 100 µm wide tube for different time points. The pacemaker location in cell cycle six is indicated by P. Approx. 250 nuclei/µl are added. (B) Analysis for the experiment in A. Left: GFP-NLS intensity profile, averaged over the times between the mitotic waves in cell cycle 5 and 6. The GFP-NLS intensity is highest close to the pacemaker region P. Middle: Difference in cell cycle period (with respect to the fastest period) at different locations along the tube, averaged over cell cycle 1–6, showing that the pacemaker region oscillates fastest. Right: Mean distance from the center of each nucleus to its two nearest neighboring nuclei. The nucleus close to the pacemaker region P is most separated from its neighbors. (C) Mitotic waves in a 200 µm Teflon tube shown by a fluorescent microtubule reporter (HiLyte Fluor 488).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/52868/elife-52868-fig1-figsupp1-v3.jpg)

**Figure 1—figure supplement 1.:** (A) Example of microscope image (top) and binarized image from ilastik (bottom), with in blue pixels recognized as background and orange the nuclei. (B) Intensity profile $I⁢(x)$ in blue and the filtered profile $y⁢(x)$ in red. The domain width is equal to $L$ and the parameter $k$ determines the boundary domain. (C) Maximum intensity over $y$ as function of $x$, calculated for the microscope image in A. (D) Sketch of analysis of mitotic waves in a kymograph. At every time a profile is calculated as in C, when this is plotted over time the appearance and disappearance of nuclei is visible. The disappearance of nuclei is manually detected by visual inspection, as indictated by the blue points. Our program then automatically draws lines between these points, representing the mitotic waves, and calculates periods and wave speeds. (E) Example of the methodology sketched out in panel D for actual data, showing two (parts of) mitotic waves. The orange and blue lines illustrate errors that could be made visually, but they lead to relatively small differences in estimated period and wave speed (up to 1 min difference in estimated period and up to 2 µm/min difference in estimated wave speed).

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/52868/elife-52868-fig1-figsupp2-v3.jpg)

**Figure 1—figure supplement 2.:** Analysis of the experiment shown in Figure 1. We plotted as function of the cycle number: the number of nuclei (A), the nuclear size (B), the observed wave speed (C), the period of the oscillation (D), the intensity of the nuclei (E), and the internuclear distance (F). Blue is individual data, orange lines give the median and the orange area is the 2/3 $\sigma$-interval. Red dots in (E) highlight the nuclei that are pacemakers. The internuclear distance is further analyzed in panels G and H, showing the averaged autocorrelation of projected binarized images (G) and a histogram of the distances between nuclei for all binarized images (H). Both analyses of the nuclear distribution show that the distance between neighboring nuclei is typically around 150 µm. (I) shows the same analysis as in (H), but now for an experiment in a 100 µm Teflon tube for ≈ 60 added sperm nuclei/µl.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/52868/elife-52868-fig1-figsupp3-v3.jpg)

**Figure 1—figure supplement 3.:** Kymographs of the GFP-NLS intensity for eight additional experiments in tubes of 100 and 200 µm, with a corresponding analysis of the spatial GFP-NLS intensity profile and the internuclear distances. The dots on the kymographs indicate the location of the pacemakers for two consecutive cell cycles indicated in blue and orange.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/52868/elife-52868-fig1-figsupp4-v3.jpg)

**Figure 1—figure supplement 4.:** (A) Mitotic waves (orange) in a kymograph of cell-free extract experiment in a 200 µm Teflon tube, using the GFP-NLS reporter. (B) Same as A, but using DNA staining (Hoechst 33342). C-J show an analysis of the experiment in A-B. (C,D) Mean distance from the center of each nucleus to its two nearest neighboring nuclei using the GFP-NLS and the Hoechst signal, respectively. (E) GFP-NLS intensity profile, averaged over the times between two mitotic waves. (F) Nuclear size in a single cell cycle determined from the Hoechst signal. G. Total GFP-NLS intensity per nucleus in a single cell cycle. (I) Maximal GFP-NLS intensity per nucleus in a single cell cycle. (H, J) Total and maximal GFP-NLS intensity per nucleus normalized by the nuclear size in a single cell cycle.

We noticed that the mitotic wave originated close to a nucleus that is considerably brighter than the surrounding nuclei (Figure 1A). We hypothesized that a region with higher GFP-NLS intensity correlates with a higher local oscillation frequency, serving as a pacemaker that organizes the mitotic wave. We therefore analyzed the spatial GFP-NLS intensity profile, the spatial profile of cell cycle periods, and the internuclear distance (Figure 1B). As a brighter nucleus has taken up more GFP-NLS, we reasoned that it similarly concentrates cell cycle regulators that lead to a local increase in the cell cycle frequency. We directly correlated this with the local period, which indeed showed that this region oscillated faster (Figure 1B). To further understand why certain nuclei were brighter, we explored whether their environment had any particular characteristics. We characterized the distance between the different nuclei and found that they were typically separated by 150–200 µm (Figure 1—figure supplement 2). However, we found that the brightest nucleus is also most separated from its neighboring nuclei (Figure 1B). This finding is consistent with the idea that nuclei increase their oscillation frequency by concentrating cell cycle regulators, as they have a larger pool of regulators in their surroundings to import. We analyzed the spatial GFP-NLS intensity profile and the internuclear distance for nine other experiments where we could clearly identify nuclei and mitotic waves. Overall, in 90% of the analyzed experiments the pacemaker location was well predicted by the region with the highest GFP-NLS intensity and/or the region where nuclei were most separated from their neighboring nuclei (Figure 1A,B, Figure 1—figure supplement 3, Figure 1—figure supplement 4). The total nuclear GFP-NLS intensity was also found to be a better indicator of the pacemaker location than the nuclear size as indicated by Hoechst staining, or than the GFP-NLS intensity normalized to the Hoechst signal (Figure 1—figure supplement 4).

In order to further test the role of nuclei as pacemakers, we explored alternative markers of mitotic entry that do not rely on the nuclei themselves. We repeated the experiment with a microtubule reporter, using fluorescently labeled tubulin (HiLyte Fluor 488). Figure 1C and Figure 1—video 2 show that mitotic waves are also observed using such a microtubule reporter, as well as in bright-field. With these tools in hand, we set out to test how critical system parameters such as nuclear density and nuclear import strength influence the mitotic wave dynamics.

### Nuclear density and nuclear import strength control cell cycle period and mitotic wave speed

We repeated the experiment in tubes of 100 and 200 µm width for two different concentrations of added demembranated sperm nuclei (approx. 60 and 250 nuclei/µl) (Figure 2A,B). We found that extracts with less added sperm nuclei had a faster cell cycle (Figure 2B). Mitotic waves were similarly observed, but the wave speeds were initially faster than in tubes with a higher nuclear density (Figure 2A). The waves then slowed down to similar speeds as in the case with the higher concentration of sperm nuclei. For both nuclear densities we also found that the average cell cycle period increases over time (Figure 2B). Such a correlation of mitotic wave speed with cell cycle duration is consistent with a transition from sweep waves to trigger waves as the cell cycle slows down (Vergassola et al., 2018). An increase in cell cycle period has been linked to a decrease in ATP supply over time (Guan et al., 2018). An additional explanation could be that an increase in cell cycle period is related to increasing levels of DNA as it is replicated (Dasso and Newport, 1990). This would also explain the decreasing period when reducing the concentration of added sperm nuclei.

![Figure 2.](https://cdn.elifesciences.org/articles/52868/elife-52868-fig2-v3.jpg)

**Figure 2.:** (A,B) Wave speed (A) and cell cycle period (B) over time obtained for N = 19 analyzed 100 and 200 µm Teflon tube experiments using the GFP-NLS reporter. Results are pooled from 11 different cell-free extracts for two different nuclear concentrations: ≈ 60, and ≈ 250 nuclei/µl. Each plotted point corresponds to the minimal wave speed or average cell cycle period in a single cell cycle of a single tube experiment. (C) Mitotic waves in a 200 µm Teflon tube using a GFP-MT reporter with few nuclei (≈ 30 nuclei/µl). Nuclear locations are identified in bright-field and indicated here. (D) Mitotic waves in a 200 µm Teflon tube using a GFP-NLS reporter with ≈ 10 ng/µl of added purified DNA. (E,F) Wave speed (E) and cell cycle period (F) over time obtained for N = 16 analyzed 200 µm Teflon tube experiments using the GFP-NLS reporter. Results are pooled from two different cell-free extracts for four different concentrations of the nuclear import inhibitor importazole: 0, 10, 20, 40 µM. Nuclear concentration: ≈ 250 nuclei/µl. Each plotted point corresponds to the minimal wave speed or average cell cycle period in a single cell cycle of a single tube experiment. (G) Mean nuclear size in the presence of varying concentrations of the nuclear import inhibitor importazole: 0, 20, 40 µM. Two tube experiments were analyzed per condition, which gave us nuclear sizes for 75, 62, and 25 nuclei, for 0, 20, 40 µM importazole, respectively. Error bars are one standard deviation of the mean.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/52868/elife-52868-fig2-figsupp1-v3.jpg)

**Figure 2—figure supplement 1.:** Cell cycle period over time obtained for N = 27 analyzed 100 and 200 µm Teflon tube experiments using the GFP-NLS reporter. Results are pooled from 14 different cell-free extracts for four different nuclear concentrations: 0, ≈ 30, ≈ 60, and ≈ 250 nuclei/µl. Each plotted point corresponds to the minimal wave speed or average cell cycle period in a single cell cycle of a single tube experiment. Note that for 0, ≈ 30 nuclei/µl, cell cycle periods could not be calculated as explained in the Image Analysis section due to the lack of nuclei with a GFP-NLS signal. Instead, they have been determined manually by looking at periodic variations in the microtubule reporter at different locations in the tube.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/52868/elife-52868-fig2-figsupp2-v3.jpg)

**Figure 2—figure supplement 2.:** Wave speed (A) and cell cycle period (B) over time obtained for N = 17 analyzed 200 µm Teflon tube experiments using the GFP-NLS reporter. Results are pooled from three different cell-free extracts for three different concentrations of the Eg5 kinesin inhibitor STLC: 0, 10, 20 µM. Nuclear concentration: ≈ 250 nuclei/µl. Each plotted point corresponds to the minimal wave speed or average cell cycle period in a single cell cycle of a single tube experiment. .

Interestingly, a decrease in nuclear density did not lead to a big change in the internuclear distance (Figure 1—figure supplement 2I). Instead, it created more and larger regions where nuclei were absent (Figure 1—figure supplement 3), and pacemakers were predominantly found close to these regions (Figure 1—figure supplement 3). Cheng and Ferrell observed a similar transition from a regular pattern of equidistantly spaced nuclei to a system with holes in Xenopus interphase egg extracts when decreasing the concentration of added sperm nuclei (Cheng and Ferrell, 2019). Next, we further decreased the nuclear density (approx. 30 nuclei/µl), such that only few nuclei remained in an entire tube. Here, we used the fluorescent microtubule reporter to visualize the spatial coordination of mitotic entry, while bright-field images were used to track the location of nuclei (Video 1). Mitotic waves were found to originate at the few nuclei present in the tube, and they traveled through the whole tube (several mm) at a speed of approx. 60 µm/min (Video 1, Figure 2C). In the absence of any nuclei in the tube (no added demembranated sperm nuclei), we still observed cell cycle oscillations with periods similar to extracts with low concentrations of demembranated sperm nuclei (Figure 2—figure supplement 1). However, no mitotic waves were observed (Video 1). These experiments underscore the critical role that nuclei play in changing the cell cycle period and organizing mitotic waves.

![Video 1.](https://cdn.elifesciences.org/articles/52868/elife-52868-video1.mp4.jpg)

Centrosomes have also been suggested to serve as pacemakers (Chang and Ferrell, 2013; Ishihara et al., 2014), potentially by concentrating pro-mitotic factors such as Cdc25 and cyclin B (Bonnet et al., 2008; Jackman et al., 2003). Demembranated sperm nuclei are known to have associated centrioles, which give rise to centrosomes that can generate microtubule asters. In order to test whether such centrosomes are critical to generate pacemakers, we added purified DNA to the extracts, which assembled into nuclei (Newmeyer et al., 1986). Mitotic waves were still observed indicating that DNA alone is sufficient to create pacemaker-generated mitotic waves without a need for centrosomes (Figure 2D, Figure 2—video 1).

As we hypothesize that the import of cell cycle regulators into the nucleus locally changes the cell cycle period, we decided to manipulate the nuclear import strength. We used the nuclear import inhibitor importazole, which is an inhibitor of importin-$\beta$ transport receptors. Increasing levels of importazole were found to increase the cell cycle period and slowed down the formation of nuclei (Figure 2E,F). Mitotic waves were still observed with similar speeds for lower concentrations of importazole, while concentrations higher than 60 µM abolished the formation of nuclei and mitotic waves. Increasing inhibition of nuclear import was also found to lead to smaller nuclei with dimmer levels of GFP-NLS (Figure 2G). When nuclei became very small (i.e. for 40 µM importazole), it took long for the extract to start cycling and mitotic waves were lost (Figure 2F, Figure 2—video 2). We also indirectly manipulated nuclear formation by inhibiting the kinesin Eg5 using S-Trityl-L-cysteine (STLC), which interferes with the proper formation of microtubule structures. We found that increasing concentrations of STLC gradually increased the average cell cycle period (Figure 2—figure supplement 2). Here too, nuclei no longer formed and mitotic waves were no longer observed when STLC was present in too high concentrations (approx. 40 µM STLC). Overall, these findings confirm that nuclear import processes are important in organizing mitotic waves. They ensure that nuclei are able to introduce sufficient spatial heterogeneity in cell cycle period to generate clear mitotic waves.

### A computational model where nuclei spatially redistribute cell cycle regulators predicts the location of pacemaker regions

Based on our experimental observation showing that brighter nuclei serve as pacemakers, we set out to develop a theoretical model that describes how GFP-NLS and other proteins can be spatially redistributed by nuclei. A sketch illustrating such a model is shown in Figure 3A. The system toggles between interphase and mitosis with a fixed period. During interphase, nuclei form and nuclear proteins (such as GFP-NLS) are actively imported into the nucleus. During mitosis, the nuclear envelope breaks down and proteins are free to diffuse away. We implemented the competing import and diffusion processes using a generic partial differential equation (PDE) model that describes the evolution of the concentration $C$ of nuclear protein, such as GFP-NLS (for details on this model, see Appendix 1). These competing processes are relevant for all proteins that localize to the nucleus. For example, it is known that APC/C is mostly localized in the nucleus, and Wee1 and Cdc25 are actively transported between cytoplasm and nucleus during the cell cycle (Baldin and Ducommun, 1995; Arnold et al., 2015). Such relocalization of cell cycle regulators can locally change the cell cycle oscillation frequency. Note that different different proteins can have opposing effects. For example, while increasing activity of Wee1 and APC/C tend to increase the cell cycle oscillation period, increasing Cdc25 activity leads to faster oscillations (Novak and Tyson, 1993; Tsai et al., 2014). Our experiments thus suggest that the overall effect of increasing nuclear import is to decrease the cell cycle period.

![Figure 3.](https://cdn.elifesciences.org/articles/52868/elife-52868-fig3-v3.jpg)

**Figure 3.:** (A) Schematic of the two phases of the model, interphase (import of regulators) and mitotic phase (diffusion). The cell cycle has a fixed period, which controls the periodic spatial redistribution of regulators. (B) Time evolution of Equation (8) in Appendix 1 in one spatial dimension for one nucleus, with the concentration C at the center of the domain shown in the top panel. The profile below is the time average of the intensity over one cell cycle period ($C_{a⁢v⁢g}$), where the red area highlights the build-up of cell cycle regulators close to the nucleus. The intensity $C$ is normalized such that $\frac{1}{L}\int_{x=0}^{x=L}C=1$. Parameters: $ϵ=4⋅10^{4}\mu$ µm3/min, $\sigma=60\mu$ µm, $\alpha=0.7$, $T=40$ min, $D=600\mu$ µm2/min and constant initial condition $C=1$. Domain size $L$ is 2400 µm. (C) Same as B, but now for 15 nuclei, where the time-averaged profile $C_{a⁢v⁢g}$ shows an overall build-up of regulators towards the boundary (see blue shaded area). (D) Same as C, but now varying the number of nuclei in the system, while keeping the distance of the outer nucleus to the system boundary constant. The total system size changes as a result of the changing number of nuclei. (E) Same as C, but now varying distances of the outer nucleus to the system boundary ($d_{b}$), while keeping the number of nuclei constant. The total system size changes as a result of the changing distance to the boundary $d_{b}$. (F) Same as B and C, but in a rectangular system of two spatial dimensions. The length of the system is fixed to 2400 µm, while the width of the system increases from 300 µm (with one nucleus) to 2400 µm (with 15 nuclei). The time-averaged profile $C_{a⁢v⁢g}$ is plotted, again illustrating the overall build-up of regulators towards the boundary.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/52868/elife-52868-fig3-figsupp1-v3.jpg)

**Figure 3—figure supplement 1.:** Influence of the distance of outer nuclei to the system boundary on the build-up of regulators at the boundary. (A) Same simulations as in Figure 3E, but continuously varying the distance $d_{b}$ of the outer nuclei to the system boundary. The strength of the build-up of regulators at the boundary is found to saturate as $d_{b}$ increases. This boundary strength is defined as the relative difference of the maximum (at the boundary) with respect to the background value in the middle, of the intensity profile averaged over time. The internuclear distance is 150 µm. (B) Same as A, but now for 15 nuclei with an increased internuclear distance of 400 µm. The distance $d_{b}$ of the outer nuclei to the system boundary needs to be larger than 200 µm (half of the internuclear distance) to have a build-up of regulators at the boundary. (C-E) Examples of the concentration profiles at $d_{b}$ = 200, 400, 600, respectively. The internuclear distance is 400 µm.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/52868/elife-52868-fig3-figsupp2-v3.jpg)

**Figure 3—figure supplement 2.:** Influence of system parameters on the build-up of regulators at the boundary. We define the boundary strength as the relative difference of the maximum (at the boundary) with respect to the background value in the middle, of the intensity profile averaged over time. (A) The strength of the effect increases with the attraction strength $ϵ$ (related to the nuclear import rate). (B) The boundary strength is found to be maximal for a certain attraction range $\sigma$. If $\sigma$ is too small, the nuclei are too far apart to effectively compete for shared resources, leading to a small boundary strength. When $\sigma$ is too large, however, the regions of attraction overlap so much that multiple nuclei are ‘competing’ for the same proteins, again leading to a smaller boundary strength. Interestingly, the optimal attraction range ≈ 150m ( corresponding to $2⁢\sigma-3⁢\sigma$) corresponds to the size of the nuclear domain reported in Landing et al., 1974; Telley et al., 2012 and the experimentally measured internuclear distance (Figure 1—figure supplement 2G–I, Figure 3—figure supplement 5). (C) The build-up of protein regulators at the boundary also decreases with increasing diffusion strength, effectively washing out the effect during mitosis. (D) Similarly, the boundary effect is thus also more pronounced with increasing $\alpha$, as this decreases the mitotic phase during which regulators are free to diffuse. Parameters (if not otherwise specified): $(D,T,ϵ,\sigma,\alpha)=(600,40,40000,60,0.7)$.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/52868/elife-52868-fig3-figsupp3-v3.jpg)

**Figure 3—figure supplement 3.:** (A) Different nuclear positioning influences the concentration profile (blue). The average concentration profile of the control is shown in red for comparison. The black dots denote the positions of the nuclei, while they are white when nuclei are absent. Top: deleted nuclei at the boundary (1 and 25), middle: deleted three nuclei randomly, bottom: adding noise to nuclei positions. (B) Repetition of the simulations in Figure 3D with noise on the positions of the nuclei, for one row (left) and 15 rows (right) of nuclei in the x direction. (C) Averaged projection on the y direction (orange) and the filtered signal (blue) of that profile, for 1, 3, 7 and 15 rows of nuclei (similar as in Figure 3D,E) with noise on the nuclear positions.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/52868/elife-52868-fig3-figsupp4-v3.jpg)

**Figure 3—figure supplement 4.:** Influence of internuclear distance on the build-up of regulators at the boundary. Same simulations as in Figure 3C, but changing the internuclear distance from 150 µm (A) to 100 µm (B) to 80 µm. The number of nuclei is kept fixed to 15 nuclei.

![Figure 3—figure supplement 5.](https://cdn.elifesciences.org/articles/52868/elife-52868-fig3-figsupp5-v3.jpg)

**Figure 3—figure supplement 5.:** Distance analysis of the tube experiments shown in Video 2 of the paper. Tube widths are 100 µm (A), 200 µm (B) and 560 µm (C). From the binarized kymographs, the centers of the nuclei are detected. For all nuclei, the (center-center) distances to the two nearest neighbors are calculated and after subtracting doubly counted distances shown in these histograms.

![Figure 3—figure supplement 6.](https://cdn.elifesciences.org/articles/52868/elife-52868-fig3-figsupp6-v3.jpg)

**Figure 3—figure supplement 6.:** Strength of the build-up of regulators at the boundary in 2D with increasing system width and number of rows of nuclei. This boundary strength is defined as the relative difference of the maximum (at the boundary) with respect to the background value in the middle, of the intensity profile averaged over time.

We start by studying the simplest case of a single nucleus in the center of a one-dimensional domain (see Figure 3B). We defined the spatial range of attraction around the nucleus to be approx. 100 µm, such that it is consistent with the so-called nuclear domain, a subdomain of the cytoplasm in which spatial constraints show an effect on nuclear growth (Hara and Merten, 2015). In Xenopus cell-free extract, this nuclear domain has a diameter of approx. 170 µm (Hara and Merten, 2015). The term nuclear domain was originally introduced to describe the surroundings of evenly spaced nuclei in syncytial muscle fibers and Drosophila embryos (Landing et al., 1974; Telley et al., 2012). In Drosophila embryos, the nuclear domain (also called energid) is approx. 30 µm for nuclei which are approx. 5–10 µm in diameter (Chen et al., 2012; Telley et al., 2012). In our experiments we find an internuclear distance of approx. 150 µm for nuclei of approx. 40 µm in diameter (Figure 1—figure supplement 2G-I). Figure 3B shows that proteins quickly build up in the nuclear region in the early phase of the import period and then the proteins quickly disperse after nuclear envelope breakdown. As expected, when averaging the concentration profile over one cell cycle, we find that the time-averaged concentration $C_{a⁢v⁢g}$ peaks around the nucleus (see red area in Figure 3B), defining a pacemaker at the nucleus.

While a typical cell contains a single nucleus, the cell-free extract experiment shown in Figure 1 consists of many distributed nuclei. From the experimental data, we calculated how far different nuclei are separated from each other, finding that the distance between neighboring nuclei is typically around 150 µm (Figure 1—figure supplement 2G–I). Note that this distance is consistent with the typical size of a nuclear domain in Xenopus cell-free extract as mentioned before. Moreover, the internuclear distance is also consistent with the size of the recently characterized cell-like compartments that self-organize from homogenized interphase egg cytoplasm (Cheng and Ferrell, 2019). Using this information, we carried out simulations where many nuclei are equidistantly distributed over the whole domain. Such a simulation with 15 nuclei in a domain of 2.4 mm is shown in Figure 3C. Similarly as in the case of a single nucleus, the concentration $C$ increases during interphase at each nuclear location, while it quickly decreases during mitosis. However, nuclei close to the boundary are found to have a higher average concentration $C_{a⁢v⁢g}$ (see blue shaded area in Figure 3C), which corresponds to a stronger pacemaker region at the boundary.

The build-up of regulators at the boundary is mainly attributed to the fact that nuclei in the interior of the domain compete with neighboring nuclei to attract the available proteins, while nuclei close to the boundary only have one such ‘competitor’. In Figure 3D we verify how the number of nuclei in the system affects the average distribution of regulators, keeping the distance between the outer nuclei and the system boundary constant. Starting from the situation with 15 nuclei in Figure 3C (blue), we gradually decreased the number of nuclei in the system. Figure 3D shows that for decreasing numbers of nuclei (nine in green, five in orange, and three in red), the build-up of regulators at the boundary gradually decreases. When only having three nuclei in the system (red), the central nucleus is found to be dominant and the boundary effect is completely lost. Apart from this competition for regulators between neighboring nuclei, the location of the boundary itself could play an important role. We quantified this boundary effect by changing the distance from the outer nuclei to the system boundary ($d_{b}$), while keeping the number of nuclei in the system fixed (15 nuclei). Figure 3E shows that initially an increase in the distance to the boundary $d_{b}$ leads to a larger build-up of regulators at the boundary, but this increase saturates as $d_{b}$ becomes larger (Figure 3—figure supplement 1). Although the extent to which regulators build up close to the boundary also depends on the model parameters and on the exact nuclear distribution (see Figure 3—figure supplement 2, Figure 3—figure supplement 3, Figure 3—figure supplement 4), it was found to be a robust phenomenon. Interestingly, however, randomly removing a few nuclei within the domain could abolish the build-up of regulators at the boundary. Instead, proteins build up close to the nuclei adjacent to the gaps (Figure 3—figure supplement 3).

Finally, we expanded our model to two spatial dimensions. We considered rectangular domains of varying aspect ratios, keeping one side fixed in length, while varying the other side in width. The long side was chosen the same as in Figure 3C in which we again define 15 nuclei. We then explored the effect of different widths with increasing rows of nuclei, see Figure 3F. The number of rows of nuclei was based on the experimental observation that wider systems support more nuclei and that those nuclei are separated by the same internuclear distance as in the thin tubes (Figure 3—figure supplement 5). Similarly as in the one-dimensional case, we observe that nuclear cell cycle regulators build up at the edges of the domain. This effect was particularly strong along the longest side of the rectangle, and strikingly, it became more pronounced as the width of the domain increased (see Figure 3F, Figure 3—figure supplement 6).

### Multiple pacemakers compete to define the direction of mitotic waves

Based on the model in the previous section, we were able to make predictions of how different nuclear patterns can lead to well-defined spatial distributions of cell cycle regulators. However, transitions between interphase (nuclear import) and mitotic phase (nuclear envelope breakdown and diffusion) occurred with a fixed period. Here, we expand the model by introducing a dependence of the cell cycle period on the local concentration of cell cycle regulators (see details in Appendix 1). In this way a spatial heterogeneity in the concentration of cell cycle regulators leads to a corresponding spatial frequency profile. In general, one expects that such spatial heterogeneities in the cell cycle period create multiple waves. These waves typically propagate into the surrounding medium and compete with each other until the pacemaker with the highest frequency ultimately entrains the whole system (Kuramoto, 1984).

We used this model to explore the dynamics of a pattern of 20 equidistantly distributed nuclei in a domain of 4.2 mm. Figure 4A,D shows that on average cell cycle regulators build up close to the boundary, similarly as in Figure 3C. In the current model, however, this build-up of regulators also leads to a decreased cell cycle period at the boundary. Such a pacemaker region close to the boundary then sends out waves that gradually control the whole domain and they travel more quickly for larger diffusion strengths $D$. We then gradually increased the strength of nuclear import of the three most central nuclei, which on average led to an increased concentration of cell cycle regulators here. For moderate increases in nuclear import strength, two waves compete with one another. A boundary-driven wave and a wave coming from the interior of the domain coexist (Figure 4B). Further increasing the nuclear import strength, waves no longer emerged from the boundary and were entirely controlled by the central region of ”bright" nuclei (Figure 4C).

![Figure 4.](https://cdn.elifesciences.org/articles/52868/elife-52868-fig4-v3.jpg)

**Figure 4.:** Time evolution of Equation (21) in Appendix 1 in one spatial dimension. The profile on the right is the time average of the intensity over one cell cycle period ($C_{a⁢v⁢g}$). The intensity $C$ is normalized such that $\frac{1}{L}\int_{x=0}^{x=L}C=1$. Parameters: $ϵ=6⋅10^{4}\mu$ µm3/min, $\sigma=60\mu$ µm, $\alpha=0.7$ and initial condition $C=1$. (A-C) $D=1000\mu$ µm2/min, domain size $L$ is 4400 µm including 21 nuclei separated by 200 µm. $\beta$ is defined as a factor by which the nuclear import strength $ϵ$ is increased in the middle nucleus (see Appendix 1). $\beta$ is 1 (A), 1.04 (B) and 1.08 (C). Upon increasing the nuclear import strength of the middle nucleus, a transition is observed from boundary-driven waves (A) to waves coming from an internal pacemaker (C). The internal pacemaker region has a higher average concentration of the regulator $C$, as indicated in orange. For intermediate values of $\beta$ both types of waves coexist (B). (D-E) $D=600\mu$ µm2/min, $\beta=1$, domain size $L$ is 4400 µm. When 21 nuclei are regularly separated by 200 µm, a boundary-driven wave is observed (D). While removing the middle nucleus leads to the coexistence of boundary-driven waves and a waves coming from an internal pacemaker region close to the introduced gap (E), removing three of the middle nuclei abolishes the boundary-driven wave and only the wave coming from the internal pacemaker region persists.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/52868/elife-52868-fig4-figsupp1-v3.jpg)

**Figure 4—figure supplement 1.:** (A-F) show that models of different complexity are able to capture cell cycle oscillations. (A,D) Core components and interactions of the cell cycle oscillator model (CCO) and the FitzHugh-Nagumo oscillator model (FHN), respectively. (B,E) Time series of relaxation oscillations in the CCO and the FHN, respectively. CCO parameters are set on $(a_{1},a_{2},a_{3})=(0.8,0.4,0.01)$ min-1, $(b_{1},b_{2},b_{3})=(4,2,0.06)$ min-1, $(E_{1},E_{2},E_{3})=(35,30,32)$ nM, $(n_{1},n_{2},n_{3})=(11,3.5,17)$ and $k=1.5$ nM/min. For the biological meaning of the parameters, see Appendix 1. FHN parameters are set on $(a,b,c,d,ϵ)=(-0.85,0.05,1.2,0.5,0.01)$ and we applied the linear mapping $(u,v,t)↦(-0.19⁢u+0.5,0.32⁢v+0.52,5.75⁢t)$ such that the output of both CCO and FHN models are similar. C,F. Phase space projection of the time series of the limit cycle solutions corresponding to (B,E), including nullclines of resp. [cdk1] and $u$. (G) Numerical simulation of the cell cycle oscillator (CCO) model where the Cdc25-related parameters ($a_{1}$ and $b_{1}$) are changed in space to define a spatially heterogeneous frequency profile. The left panel shows that the frequency is increased by $Δ_{b}$ at the boundary with respect to the cell cycle frequency elsewhere in the domain (see blue shaded region). The right panel illustrates the time series after a transient of ∼ 80 cycles in a domain of size $L=4.5$ mm. Boundary-driven waves are found to coordinate the whole domain ($2⁢x_{b}≈L$). (H) Same as A, but now a second internal pacemaker region is introduced (frequency increased by $Δ_{i}$ as indicated by orange region). Waves originating at the boundary and at the internal pacemaker region coexist ($Δ_{i}/Δ_{b}=1.5$). (I) Same as B, but with $Δ_{i}/Δ_{b}=3$. Mitotic waves are now dominated by the internal pacemaker ($2⁢x_{i}≈L$). (J) Domain fractions controlled by waves starting from the boundary ($2⁢x_{b}/L$) and from the internal pacemaker ($2⁢x_{i}/L$). $Δ_{b}$ is kept constant, while $Δ_{i}$ is changed for each simulation using the CCO model. K. Same as J, but for the FitzHugh-Nagumo (FHN) model.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/52868/elife-52868-fig4-figsupp2-v3.jpg)

**Figure 4—figure supplement 2.:** Boundary-driven waves can exist in spatially-extended systems based on different types of oscillators. We study the dynamics of mitotic waves using the same numerical setup as in Figure 4—figure supplement 1. (A) Time traces for the FitzHugh-Nagumo (FHN) model are shown for changing values of $ϵ$, a measure for the timescale separation in the system. When increasing $ϵ$ oscillations become more sinusoidal and less relaxation-like. (B) Kymographs, corresponding to the oscillations shown in A, show that boundary-driven waves persist when varying $ϵ$. (C,D) The effect of using time-dependent parameters in the FHN system on the existence and properties of boundary-driven waves. Parameters are changed with different velocities, either locally (C) or globally (D) (for more details, see Appendix 2). The kymographs are shown for three different velocities. Whereas boundary-driven waves persist, their wave speed increases with this velocity. In the global case (D), mitotic waves in the presence of such time-dependent changes have been dubbed 'sweep waves’ (Vergassola et al., 2018).

Next, we removed a nucleus from the center of the domain. Previously, for fixed cell cycle periods, we found that removing nuclei abolished the build-up of regulators at the boundary and proteins localized close to the nuclei adjacent to the gaps (Figure 3—figure supplement 3). Figure 4E indeed illustrates that there is an increased concentration of regulators close to the central gap, but a build-up of regulators close to the boundary also persisted, such that two competing waves were found. We then removed two more nuclei from the center (Figure 4F), which caused the central pacemaker region to send out a wave that controlled the whole domain. The fact that increasing nuclear import strengths and the absence of nuclei within a nuclear pattern both lead to the creation of waves from a nearby location is consistent with the experimental observations reported in Figure 1, Figure 1—figure supplement 3).

We wondered whether these dynamics of competing pacemakers are specific to this particular computational model that includes nuclear import and diffusion processes. Therefore, we also implemented known PDE models of cell cycle oscillations (Appendix 2), where we define two pacemaker regions (see Figure 4—figure supplement 1G–I): an internal pacemaker and a boundary pacemaker region. We carried out simulations continuously changing the relative strength of both pacemaker regions by increasing the difference in cell cycle period. We found a gradual transition from boundary-driven dynamics to internal pacemaker-driven dynamics (Figure 4—figure supplement 1). Similar results were found by using the FitzHugh-Nagumo oscillator model, a general model for relaxation-type oscillatory systems (Figure 4—figure supplement 1K, Figure 4—figure supplement 2). Moreover, we found that even more sinusoidal oscillations preserved boundary-driven waves (Figure 4—figure supplement 2). This suggests that the generation of boundary-driven waves is largely independent of the type of oscillations, as long as the oscillation period is decreased close to the boundary.

Our findings underscore the generic character of the dynamics of multiple competing pacemakers. Pacemaker-driven traveling waves, also often referred to as target patterns, have been widely studied and they form thanks to spatial heterogeneities that locally increase the oscillation frequency. The majority of such pacemaker waves were initially observed in chemical reaction-diffusion systems where heterogeneities were introduced as dust particles that locally modified the properties of the medium (Zaikin and Zhabotinsky, 1970; Zhabotinsky and Zaikin, 1973; Tyson and Fife, 1980). These experimental observations triggered many other studies on both traveling waves (Tyson and Fife, 1980; Kopell, 1981; Hagan, 1981; Kuramoto, 1984; Jakubith et al., 1990; Bugrim et al., 1996; Bub et al., 2005; Stich and Mikhailov, 2006) and spiral waves (Jakubith et al., 1990; Bub et al., 2002; Bub et al., 2005) triggered by a pacemaker. The interaction of multiple pacemaker waves has also been analyzed (Kuramoto, 1984; Walgraef et al., 1983; Mikhailov and Engel, 1986; Lee et al., 1996; Kheowan et al., 2007). In general, they propagate into the surrounding medium and compete with each other until the pacemaker with the highest frequency ultimately entrains the whole system (Kuramoto, 1984). The existence of the transition region is therefore somewhat surprising. However, simulating the system for increasingly longer transient times, we find that the transition region where boundary-driven waves and internal pacemaker-driven waves coexist shrinks, suggesting that after infinitely long transients one pacemaker indeed controls the whole domain. Such infinite transient times are, however, less biologically relevant as the early embryonic cell cycle oscillations only persist for about 13 cycles (Box 2). Therefore, one would expect to observe the full range of transient pacemaker dynamics in actual biological systems.

### Wider systems lead to boundary-driven mitotic waves

Our modeling leads to several predictions. First, wider systems lead to higher concentrations of cell cycle regulators at the boundary. Such a local decrease of the cell cycle period leads to boundary-driven mitotic waves. Second, systems with intermediate width allow both internally- and boundary-driven pacemakers. Third, sparsely distributed nuclei favor internal pacemakers. Based on these three predictions, we set out to verify them experimentally.

We repeated the experiment in Figure 1 for varying diameters of the Teflon tubes (approximately 100, 200, 300 and 560 µm) for a nuclear concentration of ≈ 250 nuclei/µl. A representative selection of videos corresponding to this set of experiments is shown in Video 2 (for corresponding kymographs, see Figure 5—figure supplement 1). While the thinnest tube shows mitotic waves coordinated by internal pacemakers, mitotic waves are boundary-driven over the whole domain in the thickest tube. This is consistent with the first theoretical prediction that wider systems lead to boundary-driven mitotic waves. Furthermore, Video 2 illustrates that in tubes of intermediate width (200 and 300 µm), boundary-driven waves coexist with mitotic waves that are driven by internal pacemakers. This is consistent with the second theoretical prediction. By analyzing experiments of 49 tubes of varying widths, we found these findings to be consistent (see Figure 5A). While the thinnest tubes have the lowest probability of finding boundary-driven mitotic waves, all of the experiments with the thickest 560 µm tubes showed boundary-driven waves (Figure 5—figure supplement 2). The fraction of experiments with boundary-driven wave dynamics increased smoothly with the tube width. For a more detailed analysis, see Figure 5—figure supplement 3.

![Figure 5.](https://cdn.elifesciences.org/articles/52868/elife-52868-fig5-v3.jpg)

**Figure 5.:** Fraction of experiments dominated by internally-driven waves (‘I’) and by boundary driven waves (‘B’), evaluated at the end of each of the $N=66$ imaged tubes of varying width and varying concentration of demembranated sperm nuclei. Cases where both wave types coexist (‘IB’) are counted half in each category. This is done for two different concentration of demembranated sperm nuclei: ≈ 250 nuclei/µL extract (A) or ≈ 60 nuclei/µL extract (B). For panel A (B), results are obtained for N = 49 (17) analyzed Teflon tube experiments using the GFP-NLS reporter, and they are pooled from 23 (7) different cell-free extracts.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/52868/elife-52868-fig5-figsupp1-v3.jpg)

**Figure 5—figure supplement 1.:** Kymographs corresponding to the experiments shown in Video 2 for the tubes of 100 µm (A), 200 µm (B), and 560 µm (C) in diameter. Boundary-driven waves are indicated by blue lines, while mitotic waves driven by internal pacemakers are highlighted by orange lines. On the right hand side, the corresponding averaged GFP-NLS intensity profiles are shown in black. Slow spatial changes are highlighted in blue. The resulting profiles after removing these slower changes are then shown in orange, highlighting internal pacemakers regions with a higher GFP-NLS intensity (A–E). Approx. 250 nuclei/µl are added.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/52868/elife-52868-fig5-figsupp2-v3.jpg)

**Figure 5—figure supplement 2.:** Three representative experiments in the thickest tubes with a diameter of 560 µm (corresponding to the situation in Figure 5—figure supplement 1C). Kymographs of mitotic waves (see blue lines) are shown which all converge to boundary-driven waves. Approx. 250 nuclei/µl are added.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/52868/elife-52868-fig5-figsupp3-v3.jpg)

**Figure 5—figure supplement 3.:** We carried out 120 experiments in total, 89 with a concentration of ∼ 250 nuclei/µL extract and 31 with a concentration of ∼ 60 nuclei/µL extract. These data also included experiments that showed few cell cycle oscillations, where we discarded all experiments that cycled less than five times (labeled as NC - No Cycling). We also discarded experiments which did not show clear mitotic wave behavior (labeled as NW - No Waves). For all experiments that showed wave behavior and has sufficient cycles, we then characterized its behavior towards the end of the experiment in three ways: (i) waves emerge from an internal pacemaker (labeled as I), (ii) waves emerge from the boundary (labeled as B), (iii) or waves emerge both internally and from the boundary (in which case we considered this experiment as 50% I and 50% B). All data including NC/NW for full tubes and concentrations of ∼ 250 nuclei/µL extract (left) and ∼ 60 nuclei/µL extract (right).

![Figure 5—figure supplement 4.](https://cdn.elifesciences.org/articles/52868/elife-52868-fig5-figsupp4-v3.jpg)

**Figure 5—figure supplement 4.:** GFP-NLS strength of internal peaks ($Γ_{i}$) vs. the GFP-NLS boundary strength ($Γ_{b}$) for $s=7.5/L$, $k\in{0.16⁢L,0.18⁢L,0.22⁢L,0.24⁢L}$ (A) and for $k=0.2⁢L$, $s\in{5/L,6.5/L,8.5/L,10/L}$ (B). Colors denote the type of observed mitotic waves: orange for boundary-driven waves, and blue for waves driven by internal pacemakers. Wave speed and cell cycle period for varying tube width. Wave speed (A,C) and cell cycle period (B,D) over time obtained for N = 27 analyzed Teflon tube experiments using the GFP-NLS reporter. Results are pooled from 15 different cell-free extracts for ≈ 250 nuclei/µl. Tube width is 100, 200, 300, and 560 µm.

![Figure 5—figure supplement 5.](https://cdn.elifesciences.org/articles/52868/elife-52868-fig5-figsupp5-v3.jpg)

**Figure 5—figure supplement 5.:** Wave speed (A,C) and cell cycle period (B,D) over time obtained for N=27 analyzed Teflon tube experiments using the GFP-NLS reporter. Results are pooled from 15 different cell-free extracts for ≈250 nuclei/µl. Tube width is 100, 200, 300, and 560 µm.

![Video 2.](https://cdn.elifesciences.org/articles/52868/elife-52868-video2.mp4.jpg)

**Video 2.:** Imaging is done with the GFP-NLS reporter. Mitotic waves are found to originate from the boundary as the system becomes wider. Scale bar is 200 µm.

Next, we repeated the experiments using a lower concentration of added sperm nuclei (≈ 60 nuclei/µl). This strongly decreased the probability for mitotic waves to originate from the boundary (see Figure 5B). We noticed that the regularity of the nuclear pattern was disrupted due to the decreased amount of nuclei. Consistent with our third theoretical prediction, the absence of neighboring nuclei was found to strengthen nearby pacemaker regions and decreased the likelihood of having pacemaker regions at the boundary (see Figure 1—figure supplement 3).

As boundary-driven waves were especially clear in the thickest Teflon tubes (560 µm), we wondered whether it was important for the system to be wide enough in all three spatial dimensions. In principle, the theory we developed predicts boundary-driven waves to be present in one-dimensional (Figure 3, Figure 4) and two-dimensional (Figure 3F) spatial systems. Therefore, we carried out experiments with droplets of cycling cell-free extracts on Teflon-coated glass slides, providing a thin structure, yet wide in diameter (≈ 1 mm). All such experiments showed that mitosis was coordinated via mitotic waves that originate at the boundary, consistent with the theoretical predictions (see Video 2).

Finally, we analyzed each individual experiment in more detail with the goal to directly link the presence of pacemaker regions (be it at the boundary or internally) to a local increase in GFP-NLS intensity. This analysis confirmed that there is a higher build-up of GFP-NLS intensity towards the boundaries in wider tubes (see Figure 5—figure supplement 4).

Our findings illustrate that the spatial environment has a strong influence on how biological processes self-organize. In particular, increasing the spatial dimensions of the system leads to a higher probability of observing mitotic waves that originate at the boundary of the system. Other studies have also stressed the importance of system size, boundaries, and geometry on self-organization processes. For example, using cell-free frog extracts, cytoplasmic volume was demonstrated to determine the spindle size (Good et al., 2013; Hazel et al., 2013) and the size of the nucleus (Hara and Merten, 2015).

System boundaries (Kopell et al., 1991; Haim et al., 1996; Rabinovitch et al., 2001; McNamara et al., 2016; Bernitt et al., 2017) and system geometry (Wettmann et al., 2018) have been shown to affect the dynamics of traveling waves. In the widely studied amoeba Dictyostelium discoideum, the origin of cAMP waves have been studied in inhomogeneous systems. Waves appear spontaneously in areas of higher cell density with the oscillation frequency of these centers depending on their density (Vidal-Henriquez and Gholami, 2019). In the presence of advection, a boundary-induced instability was found to periodically excite a cAMP wave near the boundary (Vidal-Henriquez et al., 2017). Another well-characterized model organism is the bacterium Escherichia coli, where Min-protein wave patterns help select the site of cell division (Hu and Lutkenhaus, 1999; Raskin and de Boer, 1999). Wave patterns and the location of cell division have been shown to strongly depend on the system size and geometry, both in vivo by deforming cell shape (Männik et al., 2012; Wu et al., 2015; Wettmann et al., 2018) and in vitro by reconstituting Min oscillations in open and enclosed compartments (Zieske and Schwille, 2014; Zieske et al., 2016; Caspi and Dekker, 2016; Wettmann et al., 2018). As thin compartments were gradually increased in length, multiple regions of oscillations were observed (Zieske and Schwille, 2014; Zieske et al., 2016; Caspi and Dekker, 2016; Wettmann et al., 2018). For more complex geometries, many more wave patterns have been observed, such as standing waves, traveling planar and spiral waves, and coexisting stable stationary distributions (Zieske and Schwille, 2014; Zieske et al., 2016; Caspi and Dekker, 2016; Wettmann et al., 2018). While there are similarities with our findings in the Xenopus cell-free extracts, one important difference is that the wave patterns in the Min system are mainly controlled by the spatial dimensions and geometry. In contrast, in our findings the influence of the spatial dimensions are, at least partially, mediated by the nuclei within the oscillatory medium that serve as pacemakers.

## Discussion

A crucial task that a developing cell needs to accomplish is the replication of its DNA and, subsequently, cell division. In large cells, which demand spatial coordination in order to accomplish this task, mitotic waves can organize the process. We have demonstrated that nuclei act as pacemakers generating the mitotic waves in Xenopus cell-free extracts. Pacemakers are regions that oscillate faster than their environment, and, as such, initiate traveling waves (Kuramoto, 1984). A nucleus becomes a pacemaker by its ability to import factors into the nucleus and, presumably, concentrate cell cycle regulators. Indeed, we found that pacemakers are often located near nuclei that are brighter due to increased import of exogeneously added GFP-NLS. We built a generic computational model, which showed that the distribution of cell cycle regulators also depends on the nuclear positioning and spatial dimensions of the system. We tested this idea by experimentally exploring the mitotic wave dynamics in cell-free extracts in which we changed the nuclear density and nuclear import strength. In cell-free extracts with only few nuclei, we found that mitotic waves originated at those nuclei and spread through the parts of the extract devoid of nuclei. In the absence of any nuclei in the system, no mitotic waves were observed. Decreasing the nuclear import strength similarly avoided the formation of mitotic waves. Finally, we changed the spatial dimensions of the system, and found that thicker tubes have a larger tendency to concentrate cell cycle regulators at the boundaries, leading to mitotic waves originating at the outer edges of the tubes. Thus, nuclei are central hubs that organize this complex cellular process.

One advantage to having the nucleus control the timing of mitosis is that it allows the cell to ensure that DNA replication has completed before initiating mitosis. While DNA checkpoints are largely silenced in the early Xenopus embryo (Newport and Dasso, 1989), in Drosophila DNA content is known to activate the DNA-replication checkpoint and alter the cell cycle period (Farrell and O'Farrell, 2014; Deneke et al., 2016). A failure in the correct regulation of mitosis is associated with polyploidy, which plays a key role in nonmalignant physiological and pathological processes (Fox and Duronio, 2013). In the absence of a proper pacemaker, or if the pacemaker were to be located elsewhere, linking DNA replication to mitosis would be more complicated and, perhaps, more prone to error.

Previous studies have pointed to the critical role of the nucleus in spatial redistributing cell cycle regulators (Gavet and Pines, 2010; Santos et al., 2012). In particular, the nuclear import of Cyclin B has been shown to lead to spatial positive feedback, ensuring a robust and irreversible mitotic entry (Santos et al., 2012). Nuclei have also been found to be crucial in ensuring cell cycle oscillations in the Drosophila embryo (Huang and Raff, 1999; Deneke et al., 2019). Interestingly, although previous reports have suggested that centrosomes serve as pacemakers (Chang and Ferrell, 2013; Ishihara et al., 2014), we found that they are dispensable. After treating extracts with purified DNA, which lacks centrosomes, we still observed mitotic waves.

We also found that the interaction of multiple nuclei in a shared cytoplasm can lead to unexpected behavior. Nuclei self-organize in regular spatial patterns within a tube of Xenopus cell-free extract. The measured regular spacing between neighboring nuclei was found to be approximately 150 µm, which coincides with the nuclear subdomain of the cytoplasm in which spatial constraints show an effect on nuclear growth as studied in syncytial muscle fibers (Landing et al., 1974), Drosophila embryos (Telley et al., 2012), and cell-free frog extracts (Hara and Merten, 2015). It is also consistent with the size of cell-like compartments that spontaneously form in homogenized interphase cell-free frog extracts (Cheng and Ferrell, 2019). We found that such regularity in the nuclear distribution led to a build-up of cell cycle regulators towards the boundary of the system, such that the collective behavior of many nuclei creates a pacemaker region at the boundary of the oscillatory medium. This boundary effect was stronger with increasing widths of the tubes, in the presence of more extended regular nuclear patterns. We consistently observed more boundary-driven waves in such wider tubes.

Mitotic waves in the early Drosophila embryo also often originate at the boundary (Foe and Alberts, 1983). During nuclear cycles 10–13 in the syncytial blastoderm of these early embryos, nuclei enter (and exit) mitosis in waves that originate from the opposite anterior and posterior poles of the embryo and terminate in its mid-region. While mitotic waves are associated to so-called trigger waves in the Xenopus embryo (Chang and Ferrell, 2013; Gelens et al., 2014), they have been shown to be so-called sweep waves in the Drosophila embryo (Vergassola et al., 2018). We find, by computational modeling, that sweep waves are also able to generate boundary-driven waves in a syncytium, and that they propagate faster than trigger waves as predicted by Vergassola et al. (2018); Figure 4—figure supplement 2. However, the internuclear distance of our simulations is significantly larger than the one observed in the more crowded Drosophila embryo, so it remains unclear whether our results can directly extend to that system. Despite the limitations of the model, our work is expected to be relevant for all coenocytes (Ondracka et al., 2018), where waves of mitosis have also been observed (Sears, 1967; Brown et al., 2003).

Nuclei are a natural choice of pacemaker for mitotic waves because they allow for a natural way to link one biological process, DNA replication, with another, mitosis. We hope that our work will further trigger new studies into the origin of pacemakers as the initiation of biological decisions mediated by traveling waves seem to be key in the proper coordination of a biological process. Traveling waves have, for example, also been found to propagate apoptosis (Cheng and Ferrell, 2018), action potentials (Hodgkin and Huxley, 1952), and calcium signals (Stricker, 1999) over large distances. In these systems, defective mitochondria, signals from neighboring neurons, or fertilization serve as the initial trigger to locally activate a wave.

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
      <td>Strain, strain background (Xenopus laevis, male and female)</td>
      <td>Xenopus laevis</td>
      <td>Centre de Res- sources Biolo- giques Xénopes</td>
      <td>RRID:XEP_Xla</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>GFP-NLS</td>
      <td>DOI: 10.1038/nature12321</td>
      <td></td>
      <td>Construct provided by James Ferrell (Stanford Univ., USA)</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>(fluorescent) microtubule reporter</td>
      <td>Cytoskeleton, Inc</td>
      <td>Cat. #: TL488M-B</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>GenElute Mammalian Genomic DNA kit</td>
      <td>Sigma-Aldrich</td>
      <td>Cat. #: G1N70</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Human chorionic gonadotropin</td>
      <td>MSD Animal Health</td>
      <td></td>
      <td>CHORULON</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Pregnant mare’s serumgonadotropin</td>
      <td>MSD Animal Health</td>
      <td></td>
      <td>FOLLIGON</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Calcium ionophore A23187</td>
      <td>Sigma-Aldrich</td>
      <td>PubChem CID: 11957499; Cat. #: C7522</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Leupeptin</td>
      <td>Sigma-Aldrich</td>
      <td>PubChem CID: 72429; Cat. #: L8511</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Pepstatin</td>
      <td>Sigma-Aldrich</td>
      <td>PubChem CID: 5478883; Cat. #: P5318</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Chymostatin</td>
      <td>Sigma-Aldrich</td>
      <td>PubChem CID: 443119; Cat. #: C7268</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Cytochalasin B</td>
      <td>Sigma-Aldrich</td>
      <td>PubChem CID: 5311281; Cat. #: C6762</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Proteinase K</td>
      <td>Sigma-Aldrich</td>
      <td>Cat. #: P2308</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Importazole</td>
      <td>Sigma-Aldrich</td>
      <td>PubChem CID: 2949965; Cat. #: SML0341</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>S-Trityl-L-cysteine</td>
      <td>Acros Organics</td>
      <td>PubChem CID: 76044; Cat. #: 173010050</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Fiji</td>
      <td>http://fiji.sc/</td>
      <td>RRID:SCR_002285</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Wolfram Mathematica</td>
      <td>www.wolfram.com/mathematical</td>
      <td>RRID:SCR_014448</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Ilastik</td>
      <td>www.ilastik.org</td>
      <td>RRID:SCR_015246</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Model for nuclear import</td>
      <td>This paper, used for Figure 3</td>
      <td></td>
      <td>Code on GitHub (Nolet, 2020)</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Model for nuclear import, frequency dependent</td>
      <td>This paper, used for Figure 4</td>
      <td></td>
      <td>Code on GitHub (Nolet, 2020)</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Teflon tube</td>
      <td>Cole-Parmer</td>
      <td>Cat. #: 06417–11</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Hoechst 33342</td>
      <td>ImmunoChemistry technologies</td>
      <td>RRID:AB_265113; Cat. #: 639</td>
      <td>(5 µg/mL)</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Leica TCS SPE confocal microscope</td>
      <td>Leica Microsystems</td>
      <td>RRID:SCR_002140</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Ultracentrifuge OPTIMA XPN - 90</td>
      <td>Beckman Coulter</td>
      <td>RRID:SCR_018238; Cat. #: A94468</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Numerical integration

All PDE models are solved by numerical integration using custom-made Fortran scripts. Discretization in time is done with a forward Euler method, while discretization in space is carried out with a central difference method. Data is written to .txt files which are then analyzed in Mathematica. The ODE models (CCO and FHN for Figure 4—figure supplement 1) are directly solved in Mathematica, since computational time is limited to seconds. The numerical codes that were used are available through GitHub (Nolet, 2020).

### Experimental setup

We reconstitute cell cycle oscillations in vitro in cell-free cycling extracts made from unfertilized Xenopus laevis frog eggs, following the protocol by Murray, 1991; Box 2). Female Xenopus laevis frogs are injected subcutaneously with 500 injection units (IU) human chorionic gonadotropin (MSD Animal Health) to induce ovulation, after prior priming with 100 IU pregnant mare’s serum gonadotropin (MSD Animal Health). The obtained eggs are rinsed with deionized water and subsequently their jelly coat is removed by incubation in a 2% w/v cysteine in 1 × XB salts solution. Dejellied eggs are now susceptible to activation with the calcium ionophore A23187 (0.5 µg/mL in 0.2 × Marc’s Modified Ringer’s buffer, Sigma-Aldrich) for 2 min to start the biochemical processes of the cell cycle. After a packing step, the activated eggs are crushed in an ultracentrifuge (XPN90, Optima) at 16,000 × g at 2°C for 10 min. This allows the collection of the cytoplasmic fraction to which the protease inhibitors leupeptin, pepstatin and chymostatin (Sigma-Aldrich) are added to a final concentration of 10 µg/mL. Cytochalasin B (10 µg/mL, Sigma-Aldrich) is also added to inhibit actin assembly and thus gelation-contraction, keeping the extract fluid at room temperature (Field et al., 2011).

Finally, the extract is supplemented with GFP-NLS (∼ 25 µM), green fluorescent protein with a nuclear localization signal, and sperm chromatin (using two different concentrations: ∼ 63 or 250 nuclei/µL extract). The construct for GFP-NLS was kindly provided by James Ferrell (Stanford Univ., USA). Sperm chromatin was prepared according the protocol by Murray, 1991. The supplemented extracts are then loaded in Teflon tubes (Cole-Parmer PTFE, 06417–11), through aspiration, and imaged at 24°C on a Leica TCS SPE confocal fluorescence microscope. This approach allows to visualize regular oscillations between interphase and mitotic phase. In interphase, nuclei form spontaneously in the extract supplemented with sperm chromatin. These nuclei then import GFP-NLS (see Box 2). In mitosis, the nuclear envelope breaks down and GFP is no longer localized to nuclei. Here, we use this experimental system to explore the influence of system size by varying the width of the Teflon tubes. The tubes were approximately 100, 200, 300, and 560 µm in width (the actual inner diameters are 102, 203, 305, and 559 µm). Furthermore, we change the amount of nuclear material and its distribution by considering two different concentrations of added sperm chromatin.

In addition, DNA was purified from the sperm chromatin. This was done using a GenElute Mammalian Genomic DNA kit (Sigma-Aldrich), with the use of proteinase K (Sigma-Aldrich) to release the DNA from the histones and give a higher yield. After purification, the concentration of DNA was determined using a NanoDrop spectrophotometer. Purified DNA was added to the extract at final concentrations of 5, 10, 15, 20, 25, 45 and 60 ng/µL.

Nuclear import was inhibited by adding importazole (Sigma-Aldrich), an inhibitor of importin-$\beta$ transport receptors. Final concentrations of 5, 10, 20, 40, and 60 µM were tested.

Microtubule dynamics was disrupted by adding S-Trityl-L-cysteine (STLC, Acros Organics), a kinesin Eg5 inhibitor. Final concentrations of 10, 20, 30, 40, and 50 µM were tested.

In some of the experiments fluorescent reporters other than GFP-NLS were used. These included a green microtubule reporter (Tubulin porcine HiLyte 488; Cytoskeleton, Inc) at 1 µM final concentration and DNA staining (Hoechst 33342) at 5 µg/mL final concentration.

### Image analysis

#### Microscope data

We used a Leica TCS SPE confocal fluorescence microscope (5x objective) in confocal mode to excite the GFP-NLS with a 488 nm solid state laser, and capture the emission from 493 to 600 nm. In the non-confocal experiments we used the Leica EL6000 metal halide external fluorescence light source for excitation of the fluorophores. The different filter cubes used were the L5 (excitation 480/40 nm bandpass, emission 527/30 nm bandpass) for GFP-NLS and HiLyte Fluor 488; and the A4 (excitation 360/40 nm bandpass, emission 470/40 nm bandpass) for the Hoechst 33342 staining. First, we fixed imaging positions at different (x,y) locations of the Teflon tubes, ensuring overlap between subsequent positions to capture the whole tubes. Within a tube, the z-position was fixed, but could differ between tubes to be able to image the central plane of the tubes. We then captured time-lapse images of these different positions during 18 hr, creating image stacks for each position in a .lif (Leica Image File) format. The .lif files belonging to one tube were then imported in Fiji (Schindelin et al., 2012). The maximum intensity of the different image stacks was put at the same level. Then, using the overlap between subsequent image positions, the image stacks were stitched pairwise (Preibisch et al., 2009). Subsequently, the images were cropped and saved as separate .tiff files per timepoint, an .avi file and a kymograph were made.

#### Data analysis from images

The .tiff files are imported in Mathematica and for all $x$ the maximum intensity over the width is calculated. This allows us to have a one-dimensional intensity profile for each time, see Figure 1—figure supplement 1C. Kymographs as in Figure 1A and Figure 1—figure supplement 3 were made from these profiles over time. Lines are drawn through the points of mitotic entry (disappearance of nuclei), for every visible cycle. This is done by manually detecting the start- and endpoints of the wave, as depicted in the sketch of Figure 1—figure supplement 1D. The lines are drawn through those points automatically and periods and wave speeds are then calculated based on these lines. The period is calculated by taking 20 points on these lines and determining the time to the next line. This gives an average period (and standard deviation) for each cycle. The wave speed is calculated by taking the derivative of the lines. For the full cycle, the wave speed is only reported if the wave travels a large enough (> 600 µm) distance (to only include well-formed waves and to reduce noise), and if multiple waves are present, the minimum speed is reported. The locations of the nuclei (one-dimensional) are extracted from the kymographs at the last one or two lines (if nuclei are well-separated). For each nucleus the average distance to their neighbors (left and right) is calculated which is also plotted in Figure 1C and Figure 1—figure supplement 3. For the last two cycles, the maximum intensity over the cycle is calculated at every $x$, yielding an intensity profile at each cycle.

#### Processing for specific analyses

When calculating properties of individual nuclei (e.g. size, location, intensity), the Ilastik software was used to automatically recognize nuclei in a series of .tiff files. This program relies on machine learning software which makes recognition a lot faster than manual tracking. The files are imported in Ilastik, where we provided three labels (’nucleus’, ’background’ or ’outside of the tube’) to train the implemented random forest classifier to recognize the labels in the images (Sommer et al., 2011). After the training phase, we exported the results as a .hdf5 file, which contains the probability of each pixel to be ’nucleus’, ’background’ and ’outside of the tube’ for each timepoint. The .hdf5 files were imported in Mathematica for further analysis. The data of these files was binarized by defining all pixels with a high probability (≥ 75%) as nuclei (1) and others as background (0). Adjacent pixels were grouped together and the separate groups were recognized as the nuclei. Noise was reduced by ignoring nuclei consisting only of a few pixels. This resulted in a binarized picture, such as in Figure 1—figure supplement 1A. Of all recognized nuclei (orange), information as location (center) and size is extracted with Mathematica. In order to obtain continuous-time kymographs (such as in Figure 1A and Figure 5—figure supplement 1, we overlayed the binarized matrix with the original .tiff and integrated over the width. In this way intensity differences were still visible.

#### Analysis of the pacemaker strength of internal regions and the boundary regions

The GFP-NLS intensity profile of the experiments is analyzed in order to calculate the strength of the boundary and of internal pacemakers (Figure 5—figure supplement 1 and Figure 5—figure supplement 4). An example of such an intensity profile $I⁢(x)$ is shown in Figure 1—figure supplement 1B. The averaged intensity profile is filtered using a low-pass filter, to obtain a ‘background’ signal $y⁢(x)$. This is the red line in Figure 1—figure supplement 1B. All frequencies higher than a threshold $s>0$ are filtered out. The obtained background profile $y⁢(x)$ does of course depend on the parameter $s$. The position of the minimum of $y⁢(x)$ is denoted by $x¯$, that is

$$
y⁢(x¯)=minx\in[0,L]⁡y⁢(x).
$$

From the background profile, we calculate two measures $L_{1},R_{1}$ for the GFP build-up at the boundary, by

$$
L_{1}=\frac{1}{x¯}⁢\int_{0}^{x¯}(y⁢(x)-y⁢(x¯))⁢𝑑x
$$

and

$$
R_{1}=\frac{1}{L-x¯}⁢\int_{x¯}^{L}(y⁢(x)-y⁢(x¯))⁢𝑑x.
$$

These correspond to the GFP build-up in the blue areas in Figure 5—figure supplement 1.

A second parameter, $k>0$, is introduced and defines the boundary width. In other words, the intervals $[0,k]$ and $[L-k,L]$ are the boundary domains and $[k,L-k]$ is the internal domain. The background profile $y⁢(x)$ might over- or underestimate GFP build-up in the boundary domains. This is compensated by calculating the second type of measures, $L_{2}$ and $R_{2}$. These are defined by

$$
L_{2}=\frac{1}{k}⁢\int_{0}^{k}(I⁢(x)-y⁢(x))⁢𝑑x
$$

and

$$
R_{2}=\frac{1}{k}⁢\int_{L-k}^{L}(I⁢(x)-y⁢(x))⁢𝑑x.
$$

The GFP build-up at the boundary, denoted by $Γ_{b}$, of this intensity profile is now defined as

$$
Γ_{b}=max⁡{L_{1}+L_{2},R_{1}+R_{2}}.
$$

The internal GFP build-up (i.e. by nuclei located internally) is defined by those areas where the intensity $I⁢(x)$ is higher than the background profile $y⁢(x)$. This internal GFP build-up $Γ_{i}$ is calculated by

$$
Γ_{i}=\frac{1}{L-2⁢k}⁢\int_{k}^{L-k}max⁡{0,I⁢(x)-y⁢(x)}⁢𝑑x,
$$

which correspond to the orange areas in Figure 5—figure supplement 1.

Figure 5—figure supplement 4 shows the GFP build-up at the boundary and internally, $Γ_{i}$ vs. $Γ_{b}$, for 20 experiments. This is done for various values of $k$ and $s$. Since $Γ_{i}$ and $Γ_{b}$ depend on these parameters, the figure will change with those parameters. However, we see that qualitatively differences are small.

### Data availability

All the data generated during the study are summarized and provided in the manuscript and supporting files. Source files have been provided for Figure 1, Figure 1—figure supplement 4, Figure 2, Figure 5—figure supplement 1, Box 2, Video 1 and Video 2 in the format of microscopy videos. Additionally, representative microscopy videos of all different conditions are provided as a Zenodo dataset (http://doi.org/10.5281/zenodo.3736728). The numerical codes that were used, together with an overview table of the performed experiments, are available through GitHub (Nolet, 2020; copy archived at https://github.com/elifesciences-publications/eLife_paper).
