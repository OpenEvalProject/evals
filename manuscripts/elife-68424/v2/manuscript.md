# Scaling of subcellular actin structures with cell length through decelerated growth

## Authors

- Shane G McInally<sup>1</sup> ([ORCID: 0000-0001-6145-4581](https://orcid.org/0000-0001-6145-4581))
- Jane Kondev<sup>2</sup> ([ORCID: 0000-0001-7522-7144](https://orcid.org/0000-0001-7522-7144)) †
- Bruce L Goode<sup>1</sup> ([ORCID: 0000-0002-6443-5893](https://orcid.org/0000-0002-6443-5893)) †

### Affiliations

1. Department of Biology, Brandeis University Waltham United States
2. Department of Physics, Brandeis University Waltham United States

† Corresponding author

## Abstract

How cells tune the size of their subcellular parts to scale with cell size is a fundamental question in cell biology. Until now, most studies on the size control of organelles and other subcellular structures have focused on scaling relationships with cell volume, which can be explained by limiting pool mechanisms. Here, we uncover a distinct scaling relationship with cell length rather than volume, revealed by mathematical modeling and quantitative imaging of yeast actin cables. The extension rate of cables decelerates as they approach the rear of the cell, until cable length matches cell length. Further, the deceleration rate scales with cell length. These observations are quantitatively explained by a ‘balance-point’ model, which stands in contrast to limiting pool mechanisms, and describes a distinct mode of self-assembly that senses the linear dimensions of the cell.

## Introduction

The size of a cell’s internal parts are scaled to its overall size. This size-scaling behavior has been demonstrated for organelles as well as large macromolecular assemblies, illustrating the broad importance of adapting the size of internal structures to the geometric dimensions of the cell (Rafelski et al., 2012; Levy and Heald, 2010; Hazel et al., 2013; Good et al., 2013; Weber and Brangwynne, 2015; Greenan et al., 2010; Jorgensen et al., 2007; Decker et al., 2011; Neumann and Nurse, 2007; Lacroix et al., 2018). A popular model of cellular scaling is the limiting pool mechanism, wherein maintaining a constant concentration of molecular components enables the subcellular structure to increase in size proportionally with cell volume (Goehring and Hyman, 2012; de Godoy et al., 2008) This allows larger cells to assemble larger structures, since the total number of molecular building blocks increases proportionally with cell volume. Additionally, this mechanism is biochemically simple because it does not require active processes that dynamically tune concentrations or activity levels of proteins involved in the construction . Indeed, cells appear to use a limiting pool mechanism to scale the size of their nucleoli, centrosomes, and mitotic spindles (Hazel et al., 2013; Good et al., 2013; Weber and Brangwynne, 2015; Greenan et al., 2010; Decker et al., 2011; Lacroix et al., 2018). However, limiting pool models cannot explain how the size of a linear subcellular structure scales with the linear dimensions of a cell, rather than its volume. Namely, these mechanisms predict that a two fold increase in the radius of a spherical cell will increase the length of a linear structure eight fold, following the eight fold increase in cell volume. This suggests that other mechanisms must account for how some subcellular structures are scaled with the linear dimensions of a cell.

Polarized actin cables in S. cerevisiae are an example of a linear structure that appear to grow to match the linear dimensions of the cell in order to effectively deliver secretory vesicles (Moseley and Goode, 2006). These cables are linear bundles of crosslinked actin filaments assembled by formins, which extend along the cell cortex and serve as tracks for intracellular transport of cargo from the mother cell to the growing bud, or daughter cell. Complementary sets of cables are assembled by two formins, Bni1 at the bud tip and Bnr1 at the bud neck (Pruyne et al., 2004). Throughout the cell cycle, cables are continuously polymerized, turn over at high rates, and appear to grow until they reach the back of the mother cell (Yu et al., 2011; Yang and Pon, 2002; Eskin et al., 2016). This prompted us to more rigorously investigate the relationship between cable length and cell size.

We started by comparing cable lengths to the lengths of the mother cells in which they grew. Cables were imaged in fixed wild-type haploid cells using super-resolution microscopy. Cable lengths were measured from their site of assembly (the bud neck) to their distal tip in the mother cell (note that mother cell and cell are synonymous and used interchangeably from this point on) (Figure 1—figure supplement 1A). Average cable length and average cell length were remarkably similar (4.5 ± 0.3 µm and 4.5 ± 0.2 µm, respectively), suggesting a scaling relationship. However, we note that there was a wider range in cable lengths (2.0–8.7 µm) compared to cell lengths (3.7–5.5 µm), presumably because cables in fixed cells are at different stages of growth. Further, because cables grow along the cortex of an ellipsoid shaped cell, their length can exceed the length of the cell while not growing past the back of the cell. Therefore, a cable that grows from the bud neck to the back of the cell is expected to be slightly longer than the direct distance between these two points.

The observations above led us to ask whether the relationship between cable length and cell length is maintained as cell size increases. To address this, we compared cable lengths in haploid and diploid cells, and cdc28-13ts temperature-sensitive mutants that grow abnormally large. Diploid mother cells had an ~2-fold increase in volume compared to haploid mother cells (81.8 ± 6.3 µm3 and 44.9 ± 4.7 µm3, respectively) (Figure 1A,B and E), consistent with previous studies (Jorgensen et al., 2002). The cdc28-13ts strain exhibited a normal haploid mother cell size at the permissive temperature. However, this strain displayed a ~ 5-fold increase in volume (198.3 ± 5.5 µm3 versus 40.9 ± 2.3 µm3) after growth at the restrictive temperature (37°C) for 8 hr, followed by 1 hr of growth at the permissive temperature (25°C) to allow cell polarization and bud growth (Figure 1C,D and E; and Figure 1—figure supplement 1B and C; Allard et al., 2018). Accordingly, cell length increased with cell volume (Figure 1F). Cable length was greater in diploids (6.3 ± 0.7 µm) compared to haploids (4.5 ± 0.3 µm), and greater in induced (8.2 ± 0.4 µm) compared to uninduced (4.3 ± 0.1 µm) cdc28-13ts cells (Figure 1G). However, the distribution of cable lengths for all strains collapsed when we divided the lengths of cables by the lengths of the cells in which they grew (Figure 1H and I). These results strongly suggest that cables grow to a length that matches cell length.

![Figure 1.](https://cdn.elifesciences.org/articles/68424/elife-68424-fig1-v2.jpg)

**Figure 1.:** (A–D) Representative images of haploid (A), diploid (B), uninduced cdc28-13ts (C), and induced cdc28-13ts (D) cells fixed and stained with labeled-phalloidin. Lengths of single actin cables are indicated (dashed lines) in maximum intensity projections (left, color) and single Z planes (right, inverted). Scale bar, 2 µm. (E–F) Mother cell volume (E) and length (F) measured in three independent experiments (≥30 cells/strain). Each data point is from an individual cell. Larger symbols represent the mean from each experiment. (G–H) Cable length (G) and ratio of cable length/cell length (H) measured from the same cells as in E and F (≥200 cables/strain). Each data point represents an individual cable. Larger symbols represent the mean from each experiment. Error bars, 95% confidence intervals. Statistical significance determined by students t-test. Significant differences (p≤0.05) indicated for comparisons with haploid (‘a’), diploid (‘b’), uninduced cdc28-13ts (‘c’), and induced cdc28-13ts (‘d’). Complete statistical results in Figure 1—source data 1. (I) Probability density functions for ratios in H. (J–K) Cable lengths plotted against mother cell length (J) or volume (K) on double-logarithmic plots and fit using the power-law. Hypothetical isometric scaling (dashed line) is compared to experimentally measured scaling exponent (solid line).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/68424/elife-68424-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Representative images uninduced cdc28-13ts (left), and induced cdc28-13ts (right) cells fixed and stained with labeled-phalloidin. Lengths of all actin cables measured in each are indicated (yellow line). Scale bar, 2 µm. (B–C) Changes in mother cell length (B) and cell volume (C) of cdc28-13ts cells after growth at the restrictive temperature for the indicated times (≥20 cells/strain). Dashed line indicates results from linear regression. (C–D) End-to-end cable distance (C) and length/distance, or tortuosity (D) measured in three independent experiments (≥200 cables/strain). Each data point represents an individual cable. Larger symbols, mean from each experiment. Error bars, 95% confidence intervals. Statistical significance determined by students t-test. Significant differences (p≤0.05) indicated for comparisons with haploid (‘a’), diploid (‘b’), uninduced cdc28-13ts (‘c’), and induced cdc28-13ts (‘d’). Complete statistical results in Figure 1—source data 1. (E) Cable lengths plotted against mother width on a double-logarithmic plot, and fit using the power-law. This analysis indicated that scaling between cable length and cell width is hypoallometric ($a_{W}=0.77\pm0.03,R^{2}=0.40)$, in contrast with the observed isometric scaling between cell length and cable length (Figure 1J) Hypothetical isometric scaling (dashed line) is compared to experimentally measured scaling exponent (solid line). (F–H) Binned data (black squares, mean ± standard deviation) from Figure 1J and K and E.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/68424/elife-68424-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) Representative images of uninduced cdc28-13ts cells fixed and stained with labeled-phalloidin. The aspect ratio for each cell is indicated, and example actin cables that reach the rear of the mother cell are highlighted (yellow arrow). Colored bars beneath each image indicate the corresponding bin used for subsequent analyses. Scale bar, 2 µm. (B) Probability density functions for the aspect ratios of cells within each bin. (C) Probability density functions for the ratio of average cable length/cell length for each bin. Aspect ratio (B) and ratio of average cable length/cell length (C) measured from the same cells and cables as in Figure 1. (D–G) Average length of cables in a cell plotted against cell length, for each cell in each bin. Data are presented on double-logarithmic plots and fit using the power-law. Experimentally measured scaling exponent is indicated (solid line).

Next, we used a power law analysis to rigorously test the scaling relationships of cable length with cell length and volume (Figure 1J and K). Generally, scaling relations can be described by the power law $y=Ax^{a}$, where $a$ is the scaling exponent that reflects the relationship between the two measured quantities, $x$ and $y$ (Reber and Goehring, 2015). This analysis revealed isometric scaling ($a_{L}=0.91\pm0.03,R^{2}=0.50$) between cable length and cell length (Figure 1J), whereas scaling between cable length and cell volume was hypoallometric ($a_{V}=0.36\pm0.01,R^{2}=0.46$) (Figure 1K).

To uncouple cell length from cell volume, we compared the length of cables in cells of different morphology. We computed the aspect ratio (the ratio of cell length to cell width) for the same cells analyzed above. This revealed that while some cells had nearly spherical morphologies, others had highly elongated morphologies (Figure 1—figure supplement 2A and B). Despite these differences in cell shape, the ratio of cable length to cell length, and the scaling exponents were similar for all cells (Figure 1—figure supplement 2C–G). Therefore, in cells of vastly different size and shape, the cable length directly scales with cell length, rather than with other dimensions such as cell surface area or volume.

We considered two distinct models to explain the control of cable length. In both models, the length of a cable is determined by competing rates of actin assembly $(k_{+})$ at the barbed ends of cables and disassembly $(k_{-})$ at the pointed ends of cables (Figure 2A and B). Therefore, at any given time, the extension rate of a cable is determined by the difference in its assembly and disassembly rates (Figure 2B). In the boundary-sensing model, the assembly rate is greater than the disassembly rate until the extending cable physically encounters the rear of the cell, causing one or both rates to abruptly change (Figure 2C, and Figure 2—figure supplement 1A; Reber and Goehring, 2015). This model predicts that the cable extension rate will be constant until the cable tip encounters the back of the cell. In contrast, the balance-point model requires that either the assembly rate, the disassembly rate, or both rates are length-dependent, and defines steady state cable length as the point at which these two rates are balanced (Figure 2D, and Figure 2—figure supplement 1B; Mohapatra et al., 2016). In clear contrast to the boundary-sensing model, this model predicts that the cable extension rate will steadily decrease as the cable lengthens.

![Figure 2.](https://cdn.elifesciences.org/articles/68424/elife-68424-fig2-v2.jpg)

**Figure 2.:** (A) Actin staining in haploid cell (left) and cable traces (right). (B) Relevant parameters and equation for cable extension, where assembly ($k_{+}$) and disassembly ($k_{-}$) rates change as a function of cable length. Cables are polymerized by formins (orange) from actin monomers (gray), bundled by crosslinkers (blue), and disassembled by factors not shown. Cable extension rate is the difference in assembly and disassembly rates. (C–D) Two models for cable length control. Additional information in Figure 2—figure supplement 1. (E) Maximum intensity projection of haploid cells expressing cable marker (Abp140-GFPEnvy) shown in color (top panels) and inverted gray scale (bottom panels). Yellow circle highlights tip of elongating cable over time. Scale bar, 5 µm. (F–G) Extension rate (F) and length (G) measured in five independent experiments (n = 82 cables). Symbols at each time point represents mean for individual experiment. Solid lines and shading, mean and 95% confidence interval for all five experiments. Dashed yellow lines, predictions of boundary-sensing model in C.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/68424/elife-68424-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) The boundary-sensing model proposes that cable length scales with mother cell length due to the growing tip of the cable physically encountering the rear of the mother cell (cell boundary). In this model, cable assembly and disassembly rates are length-independent until the boundary is reached. As the cable is growing (extending), the assembly rate must be greater than the disassembly rate. When the cable encounters the boundary, there is an abrupt shift in rates to prevent further growth of the cable: the assembly rate rapidly decreases (left panel), the disassembly rate rapidly increases (middle panel), or both rates change (right panel). Based on these changes to the assembly and/or disassembly rates, the boundary-sensing model predicts that the rate of cable extension remains constant until the cable physically encounters the rear of the mother cell, and then it abruptly decreases (Figure 2C). This behavior results in a cable that grows linearly with time until it reaches the boundary (Figure 2C). (B) In contrast, in balance-point model, the assembly rate (left panel), the disassembly rate (middle panel), or both rates (right panel) are length-dependent, and the intersection of these two rates (rate balance) produces a steady-state cable length (dashed line). Therefore, the balance-point model predicts that the cable extension rate will decelerate as a cable grows longer (Figure 2D). In the balance-point model, changes in cable length are expected to be greater during initial time points in a cable’s growth, and gradually decline until the steady-state length is reached (Figure 2D, dashed line). (C) Cartoon of yeast cell with actin cables (gray) extending from formins (orange) at the bud neck. Relevant parameters and mathematical form for the derived balance-point model are indicated, where the change in cable length as a function of time is controlled by the feedback function, $f$ (additional details in Materials and methods). (D) Cartoon depiction of a mechanism where actin cable length is scaled with cell length by a constant rate of cable assembly ($k_{+}$), and a variable rate of disassembly ($k_{-}$) controlled by a gradient of depolymerizing activity (red shading). The gradient is highest at the back of the mother cell, which leads to the disassembly rate (red line, lower plot) increasing as the cable lengthens. By this mechanism, the cable length will scale with cell length.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/68424/elife-68424-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) Yeast cells grown to early log-phase were mounted onto 1.2% agarose pads made with synthetic complete media and imaged on a spinning disk confocal microscope. 3D stacks were acquired at 0.3 μm intervals for approximately half of the cell height with no time delay for 2 min (approximately 0.30–0.43 frames per second). Images were processed using custom ImageJ macros to generate maximum intensity projections for each stack and apply a Gaussian blur (sigma = 1) to facilitate manual tracking of cable tips from the point where they emerged from the bud neck until they ceased extending. Individual trajectories were analyzed using custom Python scripts to compute the distance of cable tip extension between each frame, the rate of cable extension between each frame, and the total extension distance starting from initial growth at the bud neck. (B) Tracking the entire lifetime of a single cable was made possible by capturing 3D timeseries images in conjunction with our image analysis pipeline. Representative images of a single time point of a cell expressing the cable marker Abp140-GFPEnvy (integrated) show that 2D timeseries images do not have sufficient signal-to-noise ratio for long term cable tracking (upper right panel). Application of a Gaussian blur to the timeseries images helps enable reliable tracking of cables (bottom panels). Scale bar, 5 µm. (C) Maximum intensity projection of haploid cells expressing a cable marker (Abp140-GFPEnvy) shown in color (top panels) and inverted gray scale (bottom panels). Yellow circle highlights tip of an elongating cable over time. Scale bar, 5 µm. (D–E) Mean cable extension rates (D) and mean cable lengths (E) for the five independent experiments shown in Figure 2F and G (n = 82 cables). Line color indicates the mean of each replicate.

To directly test the predictions of the two models, we used live imaging to track the tips of cables as they grew from the bud neck into the mother cell (Figure 2E, Video 1, and Figure 2—figure supplement 2A–C). Initially cables extended at 0.36 ± 0.02 µm s−1, and as they grew longer their extension rates steadily decreased (Figure 2F, Figure 2—figure supplement 2D). Accordingly, we observed greater changes in cable length during earlier phases of cable growth (Figure 2G, Figure 2—figure supplement 2E). Thus, as cables lengthen their growth rate decelerates.

![Video 1.](https://cdn.elifesciences.org/articles/68424/elife-68424-video1.mp4.jpg)

**Video 1.:** Yellow circle highlights tip of an elongating cable over time. Video is played at 7 frames per second and time (seconds) is indicated in the top left corner. Scale bar, 5 µm.

Note that we detected cables that were very short (<2 µm) by live imaging, which were not seen in our analysis of fixed cells. We expect that this is because shorter cables extend at a faster rate compared to longer cables and are therefore less prevalent in fixed cell populations.

Our experimental observations above support a balance-point model in which steady state cable length is reached when the assembly and disassembly rates are balanced. In this model, the rate of cable extension at any given time is given by the difference between the assembly and disassembly rates, which we call the feedback function, $f=k_{+}-k_{-}.$ To account for the observed scaling of cable length with cell length (Figure 1H and I), we assume that $f$ depends on the cable length ($L_{cable}$) scaled by the cell length ($L_{cell}$), that is $fL_{cable},L_{cell}=f(L_{cable}/L_{cell})$. The steady state cable length $(L_{cable}^{*})$ is reached when the feedback function equals zero, $f(L_{cable}^{*}/L_{cell})=0$. Therefore, the scale-invariant feedback function leads to the scaling of $L_{cable}^{*}$ with $L_{cell}$ seen in Figure 1J. (Further mathematical details in Materials and methods.)

Smy1 is a factor implicated in cable length control, and therefore we considered whether it might be required for cable deceleration. It has been reported that cables are longer in smy1∆ compared to wildtype cells, and that Smy1 directly inhibits Bnr1-mediated actin assembly (Eskin et al., 2016; Chesarone-Cataldo et al., 2011). Further, Smy1 is transported by myosin along cables to the bud neck where Bnr1 is anchored. Based on these observations, an ‘antenna mechanism’ has been proposed in which longer cables deliver more Smy1 to slow cable extension and limit cable length (Mohapatra et al., 2015). We confirmed the increase in cable length in smy1∆ cells (Figure 3A, and Figure 3—figure supplement 1A and B; Eskin et al., 2016), but found that cables continued to decelerate in the absence of Smy1 (Figure 3B and C). Furthermore, we observed an increase in the initial cable extension rate in smy1Δ (0.42 ± 0.04 µm s−1) compared to wild-type cells (0.35 ± 0.02 µm s−1) (Figure 3D and E). Interestingly, the initial extension rate in smy1Δ cells increased by the same magnitude (1.2-fold ± 0.2) as the measured increase in cable length (1.2-fold ± 0.1). Thus, Smy1 affects cable length by limiting the initial cable growth rate (Figure 3F) but does not provide the feedback that results in cable deceleration. Importantly, this does not rule out the possibility of other cellular factors acting through an antenna mechanism to control cable growth in a length-dependent manner.

![Figure 3.](https://cdn.elifesciences.org/articles/68424/elife-68424-fig3-v2.jpg)

**Figure 3.:** All data are from three independent experiments. (A) Cable lengths (≥130 cables/strain). Each data point represents an individual cable. Larger symbols, mean from each experiment. Error bars, 95% confidence intervals. Statistical significance determined by students t-test. (B–C) Cable extension rates for wildtype (B) and smy1∆ (C) yeast (≥47 cables/strain). Symbols, mean from each experiment. Solid lines and shading, mean and 95% confidence interval for all experiments. Deceleration rates were derived from the slopes (±95% CI) of the dashed lines, which were determined by linear regression using the first ~10 s of extension. (D) Average extension rate as a function of cable length. Solid lines and shading, mean and 95% confidence interval for all experiments. Dashed box highlights region of no overlap in confidence intervals. (E) Initial cable extension rate for each strain. Small symbols, individual cables. Larger symbols, mean from each experiment. Error bars, 95% confidence intervals. Statistical significance determined by students t-test. (F) Cartoon comparing cable extension in wildtype and smy1∆ cells.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/68424/elife-68424-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A–B) Representative images of fixed haploid wild-type (A) and smy1Δ (B) cells stained with fluorescent phalloidin to label F-actin. Actin cables in wildtype cells grow to reach the back of the mother cell and have a relatively straight appearance (yellow arrows in A), whereas cables in smy1Δ are abnormally long and have a ‘wavy’ appearance (yellow arrows in B), in agreement with previous studies (Eskin et al., 2016; Chesarone-Cataldo et al., 2011). Scale bar, 2 µm.

Our model makes an interesting quantitative prediction for cables that have abnormally fast initial extension rates, such as those measured in smy1Δ cells above. Specifically, our model predicts that this increase in initial extension rate will lead to a proportional increase in the initial deceleration (see Equation 7 in Materials and methods). Thus, the measured 1.2-fold increase in initial extension rate seen in smy1∆ cells is expected to lead to a 1.2-fold increase in initial deceleration of cables, shortly after they emerge from the bud neck. Indeed, linear fits to the cable extension rate, as a function of time over the first 10 s (i.e. the first few microns of cable extension), yield, $d_{o}^{smy1Δ}=-0.018\pm0.010\mum/s^{2}$ and $d_{o}^{wt}=-0.015\pm0.005\mum/s^{2}$, for smy1∆ and wild-type cells, respectively (Figure 3B and C). The ratio of these two, $d_{0}^{smy1Δ}/d_{0}^{wt}=1.2\pm0.7$, matches the ratio of the initial extension rates, $f0^{smy1Δ}/f0^{wt}=1.2\pm0.2$. Therefore, these data lend additional quantitative support for our model.

A key prediction of our balance-point model is that cable extension rates should depend on cell length, that is a cable of a given length should grow faster (or slow down more gradually) in longer cells compared to shorter cells (Figure 4A, top). Further, it predicts that the cable extension rate profiles from cells of different lengths will collapse when cable length is normalized to cell length (Figure 4A, bottom; predictions of model derived in Materials and methods). To test these predictions, we compared cable extension dynamics in uninduced and induced cdc28-13ts cells (Figure 4B and C, Figure 4—figure supplement 1A and B, and Videos 2, 3, 4). When cables began to grow, they extended at similar rates in shorter and longer cells (Figure 4—figure supplement 1C). However, as the cables grew longer, they decelerated more gradually in the longer cells (Figure 4D–F). This led to longer cables in longer cells (Figure 4—figure supplement 1D). Linear regression analysis revealed that there is a nearly 2-fold greater initial deceleration in the shorter, uninduced cdc28-13ts cells ($d_{0}^{uninduced}=-0.019\pm0.005\mum/s^{2}$) compared to the longer, induced cdc28-13ts cells ($d_{0}^{induced}=-0.010\pm0.003\mum/s^{2}$). To determine how deceleration changes with respect to cell length, we compared the ratio of initial deceleration and cell length in induced $(L_{induced}=8.2\pm0.4\mum)$ and uninduced $(L_{uninduced}=4.3\pm0.1\mum)$ cdc28-13ts cells. We found that the initial deceleration rate is inversely proportional to cell length ($d_{0}^{uninduced}/d_{0}^{induced}=2\pm1$; $(L_{uninduced}/L_{induced})^{-1}=1.9\pm0.1$), consistent with the predictions of our balance-point model (Figure 4D and E and Equation 7 in Materials and methods). Further, once cable length was normalized to cell length, cables extended with similar dynamics (Figure 4G), as predicted by our model.

![Figure 4.](https://cdn.elifesciences.org/articles/68424/elife-68424-fig4-v2.jpg)

**Figure 4.:** (A) Predictions of balance-point model comparing how cable deceleration $(d_{0})$ changes as a function of cable length (top graph) in shorter (green curve) and longer (yellow curve) cells. This difference in the deceleration profiles is eliminated when cable length is normalized to cell length (bottom graph). (B–C) Maximum intensity projections of uninduced (B) and induced cdc28-13ts (C) cells expressing cable marker (Abp140-GFPEnvy). Yellow circle highlights tip of elongating cable over time. Scale bar, 5 µm. (D–E) Cable extension rates for uninduced (D) and induced cdc28-13ts (E) cells, from at least three independent experiments (≥57 cables/strain). Symbols and shading, mean and 95% confidence intervals for all experiments. Deceleration rates were derived from the slopes (±95% CI) of the dashed lines, which were determined by linear regression using the first ~10 s of extension. (F–G) Average extension rates in uninduced and induced cdc28-13ts cells (data from experiments in D and E) plotted as a function of cable length (F), or the ratio of cable length/cell length (G). Solid lines and shading, mean and 95% confidence interval for all experiments.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/68424/elife-68424-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A–B) Maximum intensity projections of uninduced (A) and induced cdc28-13ts (B) cells expressing cable marker (Abp140-GFPEnvy) shown in color (top panels) and inverted gray scale (bottom panels). Yellow circle highlights tip of elongating cable over time. Scale bar, 5 µm. (C) Initial cable extension rate for uninduced (green) and induced cdc28-13ts (yellow) cells. Data are from live-cell imaging experiments as in Figure 4. Small symbols, individual cables. Larger symbols, mean from at least three independent experiments (≥57 cables/strain). Error bars, 95% confidence intervals. Statistical significance determined by students t-test. (D) Analysis of data from C, showing changes in actin cable length (D) plotted versus extension time. Symbols, mean from each experiment. Solid lines and shading, mean and 95% confidence interval for all experiments.

![Video 2.](https://cdn.elifesciences.org/articles/68424/elife-68424-video2.mp4.jpg)

**Video 2.:** Yellow circle highlights tip of elongating cable over time. Video is played at 7 frames per second and time (s) is indicated in the top left corner. Scale bar, 5 µm.

![Video 3.](https://cdn.elifesciences.org/articles/68424/elife-68424-video3.mp4.jpg)

**Video 3.:** Yellow circle highlights tip of elongating cable over time. Video is played at 7 frames per second and time (s) is indicated in the top left corner. Scale bar, 5 µm.

![Video 4.](https://cdn.elifesciences.org/articles/68424/elife-68424-video4.mp4.jpg)

**Video 4.:** Yellow circle highlights tip of elongating cable over time. Video is played at 7 frames per second and time (s) is indicated in the top left corner. Scale bar, 5 µm.

Collectively, our observations demonstrate that cables grow until their length matches the length of the cell, and that this is achieved by length-dependent deceleration of cable extension. The precise mechanism providing the feedback to enable cable deceleration is not yet clear. One possibility is that it is controlled by a gradient of actin disassembly-promoting activity that is highest at the rear of the cell. Such a gradient could be established by the retrograde transport of disassembly factors on cables, leading to their release at the rear of the cell. This would produce a higher concentration of disassembly factors, and greater disassembly rate for cables, at the back of the cell. An alternative possibility is a reaction-diffusion mechanism, achieved by anchoring an activator of disassembly factors (such as a kinase) at the rear of the cell while having an inhibitor (such as a phosphatase) in the cytosol. This would be similar conceptually to how Ran GTPase gradients form around chromatin (Kalab et al., 2002), although it would require additional features to produce the scaling that we observe (Ben-Zvi et al., 2011). Either of these two mechanisms (retrograde transport or modified reaction-diffusion) has the potential to create a gradient that is shallower in longer cells compared to shorter cells, accounting for the cell-length-sensitive cable deceleration (Figure 2—figure supplement 1D). This mechanism also would allow cables to sense the rear of the cell without requiring physical interactions with that boundary. A third possibility, which is not mutually exclusive with either mechanism above, would be length-dependent inhibition of cable assembly, that is an antenna mechanism, albeit one that is dependent on cellular factors other than Smy1 (Mohapatra et al., 2015).

It has recently been shown for other subcellular structures (e.g. nucleus, spindle, centrosome, and nucleolus) that their sizes scale with cell volume, and this scaling is explained by limiting pool models (Hazel et al., 2013; Good et al., 2013; Weber and Brangwynne, 2015; Decker et al., 2011; Neumann and Nurse, 2007; Lacroix et al., 2018). However, we found that polarized actin cables scale with cell length rather than volume. This length control cannot be explained by a limiting pool mechanism, and instead is explained, both theoretically and experimentally, by a balance-point model. These results reveal a new strategy by which cells solve engineering challenges, enabling them to scale internal structures with the linear dimensions of the cell (Kirschner et al., 2000). Similar principles may underlie the length control of other polarized, linear actin structures, such as filopodia and stereocilia. Further, related strategies may be used to control the growth of radial microtubule arrays that reach the cell periphery (Lacroix et al., 2016; Wühr et al., 2010), and may explain the scaling relationships observed between flagellar length and cell length (Bauer et al., 2021) and between contractile ring diameter and cell diameter (Kukhtevich et al., 2020). Ultimately, the model of size control that we have presented here expands our understanding of the mechanisms used by cells to sense specific aspects of their geometry, including length, surface area, and volume, to assemble structures that scale with these different dimensions (Rieckhoff et al., 2020; Brownlee and Heald, 2019).

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
      <td>Strain, strain background (S. cerevisiae)</td>
      <td>See: Supplementary file 1</td>
      <td>This paper</td>
      <td>NCBITaxon:4932</td>
      <td>Strains maintained in the Goode lab</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Alexa Fluor 488- phalloidin</td>
      <td>Life Technologies</td>
      <td>A12379</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Alexa Fluor 568-phalloidin</td>
      <td>Life Technologies</td>
      <td>A12380</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pFA6a-link-GFPEnvy-SpHis5</td>
      <td>PMID:25612242</td>
      <td>RRID:Addgene_60782</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pFA6a-TRP1</td>
      <td>PMID:9717241</td>
      <td>RRID:Addgene_41603</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Plasmids and yeast strains

All strains (see Supplementary file 1) were constructed using standard methods. To integrate a bright GFP variant (GFPEnvy) at the C-terminus of the endogenous ABP140 gene, primers were designed with complementarity to the 3’ end of the GFPEnvy cassette and the C-terminal coding region of ABP140. PCR was used to generate amplicons from the pFA6a-link-GFPEnvy-SpHis5 (Slubowski et al., 2015) template that allow for selection of transformants using media lacking histidine. The parent strains, BGY12 (haploid) and cdc28-13ts, were transformed with PCR products, and transformants were selected by growth on synthetic media lacking histidine. Similarly, smy1Δ strains were generated by replacement of SMY1 with the TRP1 auxotrophic marker by designing primers with complementarity to regions 40 base-pairs immediately up-stream and down-stream of the SMY1 coding region (Longtine et al., 1998). Deletion of SMY1 was confirmed by genomic PCR with primers specific to the TRP1 promoter and the 5’UTR region of SMY1. The cdc28-13ts strain was a generous gift from Brian Graziano (UCSF). pFA6a-link-GFPEnvy-SpHis5 was a gift from Linda Huang (UMass Boston) (Addgene plasmid # 60782; http://n2t.net/addgene:60782; RRID:Addgene_60782).

### Induction of cell size changes

To induce enlargement of mother cells, cdc28-13ts cells were grown at the permissive temperature (25°C) overnight in synthetic complete media (SCM), then 10μL of overnight culture was diluted into 5mL of fresh SCM. Cultures were then shifted to the restrictive temperature (37°C) for 8 hr (except for the experiments in Figure 1—figure supplement 1B and C, where cultures were also shifted for only 4 hr). After this induction, cells were returned to the permissive temperature (25°C) for 1 hr of growth to allow cell polarization and bud growth, and then fixed or mounted for live-cell imaging.

### Quantitative analysis of actin cable length and architecture in fixed cells

Strains were grown at 25°C to mid-log phase (OD600 ~0.3) in yeast extract/peptone/dextrose (YEPD), or were first induced for cell size changes as indicated above. Then cells were fixed in 4.4% formaldehyde for 45 min, washed three times in phosphate-buffered saline (PBS), and stained with Alexa Fluor 488- phalloidin or Alexa Fluor 568-phalloidin (Life Technologies, Grand Island, NY) for ≥24 hr at 4°C. Next, cells were washed three times in PBS and imaged in mounting media (20 mM Tris, pH 8.0, 90% glycerol). 3D stacks were collected at 0.22 μm intervals on a Zeiss LSM 880 using Airyscan super-resolution imaging equipped with 63 × 1.4 Plan-Apochromat Oil objective lens. 3D stacks were acquired for the entire height of the cell. Airyscan image processing was performed using Zen Black software (Carl Zeiss). ImageJ was used to generate inverted greyscale and maximum projection images for analysis. Next ImageJ was used to manually trace each individual cable, from the bud neck to their terminus in the mother cell. The 3D stack was used to differentiate between cables that overlapped and to precisely determine both the origins and distal tips of the cables. For length analysis, we included every discernable cable in the cell that extended from the bud neck to some endpoint in the mother cell; the only cables excluded were the minority that became closely intertwined with other cables making it impossible to resolve their individual lengths. Then the xy-coordinates for each cable trace were exported into custom written Python scripts to compute cable length. Cell length was determined by measuring the distance from the bud neck to the distal end of the mother cell. Cell width was determined by measuring the widest point perpendicular to the cell length axis. Cell height was determined from the number of slices in the 3D stack and the interval size between slices. These values were recorded and imported into custom Python scripts to compute the ratio of cable length to mother cell length, the cell volume (using the ellipsoid formula), the aspect ratio (cell length/cell width), and to fit the scaling exponent for cable length versus mother cell length, width, and volume. For cell shape analysis, cells were binned based on their aspect ratio rounded to the nearest quarter value.

### Live-cell imaging and quantitative analysis of actin cable extension rate

Strains were grown at 25°C to mid-log phase (OD600 ~0.3) in either YEPD, or were first induced for cell size changes as indicated above, then harvested by centrifugation (30 s, 9000 x g). Media was decanted and cells were resuspended in 50 μL fresh media. Cells (~5 μL) were mounted onto 1.2% agarose pads made with SCM, and images were acquired on a Nikon i-E upright confocal microscope equipped with a CSU-W1 spinning-disk head (Yokogawa, Tokyo, Japan) and an Andor Ixon 897 Ultra CCD camera controlled by Nikon NIS-Elements Advanced Research software using a 100x, 1.45 NA objective. 3D stacks were acquired at 0.3 μm intervals for approximately half of the cell height with no time delay for 2 min (approximately 0.30–0.43 frames per second). Images were processed in ImageJ by generating maximum intensity projections of each stack and applying a Gaussian blur (sigma = 1) to facilitate manual tracking of cable tips. Cables included for analysis were those whose tips could be resolved in every frame, from when they emerged from the bud neck and until they stopped extending. Cables that could not be reliably tracked (e.g. dim cables, overlapping cables that prevented tracking of their tips, or cables that grew into regions not captured in the 3D stack) were excluded from the analysis. Individual cable trajectories were imported into custom Python scripts to compute the distance the cable tip travelled between each frame, the rate of extension between each frame, and the total distance travelled. The boundary-sensing model prediction depicted in Figure 2F was determined by plotting the mean initial cable extension rate as a function of time. The boundary-sensing model prediction depicted in Figure 2G was determined by using linear regression to measure the slope from the first ~10 s of cable extension. Initial cable extension rates (Figure 3C and Figure 4—figure supplement 1C) were determined by computing the extension rate measured during the first time interval.

### Mathematics of the balance point model

The rate of change of the cable length with time is given by the difference between the assembly ($k_{+}$) and disassembly ($k_{-}$) rates,

$$
\frac{dL_{cable}}{dt}=k_{+}(L_{cable},L_{cell})−k_{−}(L_{cable},L_{cell}).
$$

where we have made explicit the possibility that one or both rates depend on the length of the extending cable ($L_{cable}$) and the cell length ($L_{cell}$). The steady state length $L_{cable}^{*}$ is the cable length at which the assembly and disassembly rates are the same.

To account for the scaling of the steady state length with the cell length (as observed in Figure 1H,I and J), we make an additional assumption, namely that the feedback function, $f≡k_{+}-k_{-}$, which determines the rate of cable extension, is a function of the ratio of the cable length to the cell length, that is $fL_{cable},L_{cell}=f(L_{cable}/L_{cell}).$ Thus, our mathematical model of cable length control is described by the differential equation:

$$
\frac{dL_{cable}}{dt}=f(L_{cable}/L_{cell}),
$$

which is graphically summarized in Figure 2—figure supplement 1C.

At the molecular scale, this feedback could be accomplished with a constant rate of cable assembly and a variable rate of disassembly controlled by a gradient of depolymerizing activity that is highest at the back of the cell; see Figure 2—figure supplement 1C. In this mechanism, as the cable lengthens its distal end is subject to increasingly stronger depolymerizing activity. Further, the profile or decay-length of the depolymerizing gradient needs to scale with cell length. Such scaling of a cellular gradient with the linear distance between the two poles of the cell has been observed for the protein Bicoid in different size embryos, from different species of flies (Gregor et al., 2005). Other experimental observations and theoretical models of such scale-invariant gradients are reviewed in Ben-Zvi et al., 2011.

Figure 4F and G are a direct test of our model. In Figure 4F, we observe that the cable extension rate is dependent on cell length, consistent with Equation 1. In Figure 4G, we see that the two feedback functions, from cells of different size, collapse to a single function when the cable lengths are scaled by the cell length.

The scaling property of the feedback function immediately leads to scaling of steady state cable length with cell length. Namely, in steady state, the right-hand side of Equation 1 is zero, which implies $f(L_{cable}^{*}/L_{cell})=0$. If the zero of the feedback function is $x^{*}$ (i.e.,$fx^{*}=0$), then the steady state length $L_{cable}^{*}=x^{*}L_{cell}$, which is the scaling relation we observe in Figure 1H and J between the steady state length and the cell length.

The scaling property of the feedback function also makes a prediction for the initial rate of cable extension in cells of different size. Namely, for small cable lengths, when $L_{cable}≪L_{cell}$, we can expand Equation 2 into a Taylor series

$$
\frac{dL_{cable}}{dt}=f(\frac{L_{cable}}{L_{cell}})≈f(0)+f^{′}(0)\frac{L_{cable}}{L_{cell}},
$$

which states that the initial cable extension decreases linearly with the cable length (since $f^{'}0$ is negative) and is inversely proportional to cell length, $L_{cell}$.

Equation 3, with the initial condition $L_{cable}t=0=0$, can be solved for the cable length as a function of time,

$$
L_{cable}(t)=L_{cell}\frac{f(0)}{f^{′}(0)}[e^{\frac{f^{′}(0)}{L_{cell}}t}−1],
$$

which in turn yields, by differentiation, an exponentially decreasing in time extension rate:

$$
\frac{dL_{cable}}{dt}=f(0)e^{\frac{f^{′}(0)}{L_{cell}}t}.
$$

Since Equations 4 and 5 only hold at early times when the cable length is much smaller than the cell length (roughly, first 10 s of cable extension; see Figure 2G), we can further simplify Equation 5 by expanding it into a Taylor series:

$$
\frac{dL_{cable}}{dt}=f(0)+\frac{f(0)f^{′}(0)}{L_{cell}}t.
$$

Equation 6 makes very specific predictions about the initial deceleration of cable extension, in particular our model (Equation 2) predicts that the initial deceleration

$$
d_{0}=\frac{d^{2}L_{cable}}{dt^{2}}|_{t=0}=\frac{f(0)f^{′}(0)}{L_{cell}}
$$

scales inversely with the cell length, and proportionally with initial cable extension rate. Indeed, these predictions are supported in two independent experimental tests of this model. Our analysis of smy1Δ cells indicates that increasing $f0$, while $f'0$ and $L_{cell}$ are fixed, leads to a proportional increase in initial deceleration rate. Additionally, our analysis of induced and uninduced cdc28-13ts cells, where $L_{cell}$ increases ~2-fold, while $f0$ and $f'0$ are fixed, leads to a two fold difference in initial deceleration.

Finally, our model also makes a qualitative prediction about the probability distribution of cable lengths at steady state. Namely, the feedback function near the steady state cable length, $L_{cable}^{*}=x^{*}L_{cell}$ can be Taylor expanded to

$$
\frac{dL_{cable}}{dt}≈f(x^{∗})+f^{′}(x^{∗})\frac{L_{cable}−L_{cable}^{∗}}{L_{cell}}=f^{′}(x^{∗})\frac{L_{cable}−L_{cable}^{∗}}{L_{cell}},
$$

which shows that the strength of the feedback diminishes with cell length. This in turn implies that the steady state fluctuations of cable length will be larger in longer cells, which is consistent with data in Figure 1G. It is important to note that the above arguments pertain to cable length fluctuations over time, whereas the data in Figure 1G show cell-to-cell fluctuations in cable length, which could be influenced by cell-to-cell heterogeneity in some of the factors that affect cable assembly. Further experiments that carefully delineate between different sources of cable length fluctuations could provide more detailed tests of our model.

### Data and materials availability

Data are available in the main text or in the supplementary material. All images (McInally et al., 2021b) and source code (McInally, 2021a) are archived at Zenodo.
