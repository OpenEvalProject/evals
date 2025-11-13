# Control of nuclear size by osmotic forces in Schizosaccharomyces pombe

## Authors

- Joël Lemière<sup>1</sup> ([ORCID: 0000-0002-9017-1959](https://orcid.org/0000-0002-9017-1959))
- Paula Real-Calderon<sup>1</sup> ([ORCID: 0000-0002-4158-9582](https://orcid.org/0000-0002-4158-9582))
- Liam J Holt<sup>3</sup>
- Thomas G Fai<sup>4</sup> ([ORCID: 0000-0003-0383-5217](https://orcid.org/0000-0003-0383-5217)) †
- Fred Chang<sup>1</sup> ([ORCID: 0000-0002-8907-3286](https://orcid.org/0000-0002-8907-3286)) †

### Affiliations

1. Department of Cell and Tissue Biology, University of California, San Francisco San Francisco United States ([ROR:043mz5j54](https://ror.org/043mz5j54))
2. Centro Andaluz de Biología del Desarrollo Sevilla Spain ([ROR:01v5e3436](https://ror.org/01v5e3436))
3. Institute for Systems Genetics, New York University Langone Health New York United States ([ROR:0190ak572](https://ror.org/0190ak572))
4. Department of Mathematics and Volen Center for Complex Systems, Brandeis University Waltham United States ([ROR:05abbep66](https://ror.org/05abbep66))

† Corresponding author

## Abstract

The size of the nucleus scales robustly with cell size so that the nuclear-to-cell volume ratio (N/C ratio) is maintained during cell growth in many cell types. The mechanism responsible for this scaling remains mysterious. Previous studies have established that the N/C ratio is not determined by DNA amount but is instead influenced by factors such as nuclear envelope mechanics and nuclear transport. Here, we developed a quantitative model for nuclear size control based upon colloid osmotic pressure and tested key predictions in the fission yeast Schizosaccharomyces pombe. This model posits that the N/C ratio is determined by the numbers of macromolecules in the nucleoplasm and cytoplasm. Osmotic shift experiments showed that the fission yeast nucleus behaves as an ideal osmometer whose volume is primarily dictated by osmotic forces. Inhibition of nuclear export caused accumulation of macromolecules in the nucleoplasm, leading to nuclear swelling. We further demonstrated that the N/C ratio is maintained by a homeostasis mechanism based upon synthesis of macromolecules during growth. These studies demonstrate the functions of colloid osmotic pressure in intracellular organization and size control.

## Introduction

It has been known for more than a century that the size of the nucleus scales with cell size. Since the initial observation in plants (Strasburger, 1893) the scaling of nuclear and cell volume has been documented across the eukaryotic domain (Conklin, 1912; Gregory, 2005; Moore et al., 2019; Neumann and Nurse, 2007). More recently, scaling was even observed for nucleoids in prokaryotes (Gray et al., 2019). In multicellular organisms, the nuclear-to-cell volume (N/C) ratio varies among cell types, but this ratio is generally maintained as a constant within a given cell type (Conklin, 1912; Hertwig, 1903). During cell growth, the N/C ratio is also maintained through much of the cell cycle (Jorgensen et al., 2007; Neumann and Nurse, 2007; Willis et al., 2016), as the nucleus grows in volume at the same rate as the cell. Abnormal N/C ratios are a hallmark of diseases such as certain cancers and are sometimes used as diagnostic criteria (Foraker, 1954; Slater et al., 2005; Webster et al., 2009; Zink et al., 2004). The N/C ratio may play an important role in regulatory mechanisms, for instance, in the mid-blastula transition in embryonic development (Amodeo et al., 2015; Jevtić and Levy, 2015). However, despite the universal and fundamental nature of this cellular property, the mechanistic basis for nuclear size scaling remains poorly understood.

Although there is a correlation between nuclear size and amount of DNA, it is unlikely that DNA itself is the responsible scaling factor. DNA is only a minor component in the nucleus by volume; it has been estimated to occupy <1% of the nuclear volume and is many times less abundant in the nucleus than RNA (Milo and Phillips, 2015). Nuclear size does increase with increased ploidy in a given cell type, but generally this increase is accompanied by a similar increase in cell size (Cavalier-Smith, 2005; Gregory, 2005; Gregory and Mable, 2005; Jorgensen et al., 2007; Robinson et al., 2018). During the cell cycle, nuclear size continues to grow in the G2 phase even when DNA content is no longer increasing (Jorgensen et al., 2007; Neumann and Nurse, 2007). Further, through manipulating genome content in fission yeast, it has been shown that cells with DNA content ranging from 2N to 32N have a similar N/C ratio (Neumann and Nurse, 2007). Thus, DNA is unlikely to be the rate-limiting structural component that determines nuclear size.

Nuclear size and shape are dictated both by nuclear volume and surface area. It is clear however that nuclear volume and surface area can be uncoupled and are regulated independently. For instance, arrest of budding yeast cells in mitosis can lead to continued growth of the nuclear envelope without growth in nuclear volume, leading to misshapen nuclei and formation of nuclear envelope protrusions (Webster et al., 2009). Growth of the nuclear envelope may occur through the transfer of membranes from the endoplasmic reticulum or by lipid assembly at the nuclear envelope (Blank et al., 2017; Hirano et al., 2020; Kim et al., 2007). Studies have shown, however, that nuclear volume, not surface area, is the relevant geometric parameter that is maintained for the N/C ratio (Cantwell and Nurse, 2019a; Neumann and Nurse, 2007; Walters et al., 2019).

Efforts to define molecular-based control mechanisms have been largely unsuccessful. Genome-wide screens in fission yeast have demonstrated that mutants in the vast majority of genes exhibit normal N/C ratios, ruling out many possible cellular processes and molecular pathways (Cantwell and Nurse, 2019b; Kume et al., 2017). For instance, the N/C ratio is independent of cell size, shape, and number of nuclei (Neumann and Nurse, 2007). Screens have so far identified only a small number of genes that impact the N/C ratio, mostly related to nuclear transport or lipid synthesis (Cantwell and Nurse, 2019b; Kume et al., 2017). In vertebrate cell systems, lamins and chromatin factors have been implicated in the control of nuclear size and shape (Edens et al., 2017; Levy and Heald, 2010; Muchir et al., 2004). For example, depletion of lamin in Xenopus eggs extract resulted in a reduction of nuclear size and formation of abnormal nuclear shapes (Newport et al., 1990). However, as yeast lack lamins, it is unlikely that the nuclear lamins themselves represent a universal mechanism for nuclear size control.

Another potential factor in nuclear size control is osmotic pressure. Instead of a rigid structure, the nucleus may be regarded as a structure similar to a balloon whose size is dependent on the balance of pressures and membrane tension. The rounded shape of the typical nucleus suggests there may be slightly higher osmotic pressure in the nucleoplasm compared to the cytoplasm, which is balanced by the nuclear membrane tension. These pressures likely arise from macromolecular crowding forces termed ‘colloid osmotic pressure’, which are produced by the distinct sets of macromolecules in the nucleus and cytoplasm (Mitchison, 2019). The osmotic nature of the nucleus has been shown in various ways. Treatment of cells with osmotic shocks causes both the cell and nucleus to swell and shrink (Churney, 1942). Classic experiments demonstrated that injection of crowding agents such as polyethylene glycol into the cytoplasm cause shrinkage of the nucleus (Harding and Feldherr, 1958; Harding and Feldherr, 1959). Isolated nuclei are also responsive to osmotic shifts but the osmotic behavior depends on the molecular size of the osmolytes such that only macromolecules larger than 30 kDa will affect their volumes (Finan et al., 2009). In general, a rigorous quantitative assessment of the osmotic model for nuclear size control is lacking.

Here, we developed a quantitative model for nuclear size control based upon osmotic forces, using a combination of theoretical modeling and quantitative experiments. We used fission yeast as a tractable model in which cellular and nuclear volumes can be accurately measured. We propose a theoretical framework that represents the nucleus and cell as a system of nested osmometers. We show that nuclei in fission yeast behave as ideal osmometers, which allows for the direct study of the effects of osmotic pressure on nuclear volume and its responses to changes in macromolecular crowding. This osmotic model suggests a mechanism for maintenance of the N/C ratio during cell growth, as well as for homeostasis behavior that corrects an aberrant N/C ratio over time. Together, these studies provide critical quantitative support for an osmotic-based mechanism for nuclear size control.

## Results

### Model of the nucleus and a cell as two nested osmometers

We developed a quantitative model of nuclear and cell size control based on the physical mechanism of osmosis. The nucleus and the cell are represented as a system of nested osmometers, whose volumes are determined by osmotic pressure differences, membrane tensions, and non-osmotic volumes (Figure 1A). The cell is inflated by turgor pressure, which is defined as the osmotic pressure difference across the plasma membrane (Cout, CCy) balanced by the elastic wall surrounding the cell. Turgor pressure is produced largely from small molecules, such as ions and metabolites, attracting water into the cell through osmosis. The nuclear envelope is a semi-permeable membrane with pores that allow water, ions and other small molecules to pass with a Stoke radius below <2.5 nm (Mohr et al., 2009), but remains relatively impermeable to large proteins, macromolecular complexes, DNA and RNA, with the exception of specific nuclear transport mechanisms through nuclear pores. Macromolecules produce colloid osmotic pressures, by attracting a shell of water around them (Mitchison, 2019; Vink, 1971; Vink, 1974). For this model on nuclear volume establishment, the relevant colloid osmotic pressures in the cytoplasm ($\pi$Cy) and nucleoplasm ($\pi$N) are generated by distinct sets of macromolecules that are too large to freely diffuse across the nuclear envelope. These pressures are estimated to be orders of magnitude smaller than turgor pressure (kPa versus MPa in yeast). The apparent absolute numbers of osmotically active molecules in the nucleus and cytoplasm that generate this colloid osmotic pressure are denoted as NN and NCy, respectively. In addition, there are also non-osmotically active volumes in the cytoplasm and nucleoplasm (bCy, bN), which represent the dry volume taken up by cellular components. The percentage of the dry volume of the nucleus and the cell in isotonic conditions is called the normalized non-osmotic volume (defined as $v_{b}^{N}=b^{N}/V_{iso}^{N}$ and $v_{b}^{C}=b^{C}/V_{iso}^{C}$, with $b^{C}=b^{N}+b^{Cy}$) such that $V_{iso}^{}−b^{}$ represents the free water within each compartment, and  $v_{b}^{}$ describes the degree of macromolecular crowding.

![Figure 1.](https://cdn.elifesciences.org/articles/76075/elife-76075-fig1-v2.jpg)

**Figure 1.:** (A) Schematic of the model and parameters used in the mathematical model: membrane tension σ, non-osmotic volume b, number (N) of macromolecules that cannot freely cross either the cell or nuclear membranes, concentration of the buffer Cout. (B) Theoretical prediction of the effect of a change in the external concentration on the N/C ratio for various ratios of normalized cellular (νC) and nuclear (νN) non-osmotic volume values keeping the cell and nuclear membrane tensions (σC, σN) constant. (C) Predictions of osmotic shifts on the N/C ratio for various nuclear membrane tensions (σN), keeping a high cell tension (σC) constant. (D) Same as (C) keeping a low membrane tension. (E) Phase diagram of the N/C ratio sensitivity to osmotic shocks defined as [max(N/C ratio)-min(N/C ratio)] / (N/C ratioisotonic) for various ratios of non-osmotic volumes and nuclear membrane tension.

We postulated that the size of the nucleus is set by a combination of forces that include colloid osmotic pressures of the nucleoplasm and cytoplasm and membrane tensions that restrict expansion of the cell and nuclear membranes (σ). Membrane tension at the cell surface σC includes plasma membrane tension as well as other mechanically relevant features such as the cell wall or cortex. Similarly, membrane tension of the nuclear envelope, σN includes the tension in the inner and outer envelopes and potentially the mechanical properties of the lamina, cytoskeleton, chromatin and factors anchored to the membrane (Schreiner et al., 2015). Membrane reservoirs such as eisosomes (Lemière et al., 2021) and caveolae (Sinha et al., 2011) at the plasma membrane and inner nuclear envelope invaginations and the endoplasmic reticulum for the nuclear envelope (Fricker et al., 1997) may reduce membrane tension by allowing for increases in membrane surface area while keeping membrane tension low.

We used established osmotic theory based upon Boyle Van’t Hoff’s relationship (Hoff, 1887) and (Laplace, 1805) to analyze the steady state behavior of osmometers in our model. We treated the cell and nucleus as two spherical nested osmometers having respective membrane tensions σC and σN and interpreted Van’t Hoff’s Law in terms of the concentrations of apparent osmotically active particles in the cytoplasm (CCy), nucleoplasm (CN), and extracellular space (Cout). We described the steady state solutions in which colloid osmotic pressures in the cytoplasm and nucleus are in balance with their respective membrane tension, which results in the coupled equations:

$$
(C^{Cy}−C^{out})k_{B}T=2\sigma^{C}\frac{4\pi}{3V^{C}}^{1/3},
$$



$$
(C^{N}−C^{Cy})k_{B}T=2\sigma^{N}\frac{4\pi}{3V^{N}}^{1/3},
$$

where $k_{B}T$ is the product of Boltzmann’s constant and the temperature. Solving this system of equations for the unknown cell volume (VC) and nuclear volume (VN) yields a unique steady-state value for the N/C ratio (Appendix 1). In certain limiting cases, the N/C ratio may be written explicitly in terms of the parameters, as we show later on. However, in general the equations are solved numerically. Note that small molecules that are permeable to the nuclear envelope such as ions do not contribute on their own to the osmotic balance in Equation 2.

Using this model, we evaluated what key parameters affect the N/C ratio. To do this, we solved this system of equations (Appendix 1 Equation A14; A15) for different sets of parameters to find the resulting N/C ratio. One prediction of this model is that if the normalized non-osmotic volume of the cell equals that of its nucleus ($v_{b}^{C}=v_{b}^{N}$) then the N/C ratio remains constant under osmotic shifts (Figure 1B). Conversely, whenever $v_{b}^{N}/v_{b}^{C}\neq1$, the model predicts that the N/C ratio will vary with osmotic shocks (Figure 1B). In the case of negligible nuclear tension σN ≈ 0 N/m, the N/C ratio remains constant upon osmotic shifts precisely when $v_{b}^{C}=v_{b}^{N}$ (Appendix 1 Equation A16). In Figure 1C and D we plotted the effects of varying nuclear membrane tension σN (from 0 to 2.7 N/m) on the N/C ratio upon osmotic shifts. The results also reveal that the N/C ratio is relatively insensitive to osmotic shocks for small values of σN independently of σC (σN = 0.5 mN/m, Figure 1C and D, Appendix 1 and 3). Figure 1E summarizes these findings on the effects of varying both σN/ σC and $v_{b}^{C}/v_{b}^{N}$.

We further considered the limiting case mentioned above of negligible nuclear membrane tension σN = 0 N/m and in which the normalized non-osmotic volumes of the nucleus and cytoplasm are balanced, with $v_{b}^{C}=v_{b}^{N}$ . As explained in Appendix 4, in this case the N/C ratio is set simply by the ratio of the apparent numbers of osmotically active molecules in the nucleoplasm and in the whole cell:

$$
N/C_{ratio}=N^{Nucleus}/N^{Cell}.
$$

In the sections below, we tested and further developed this osmotic-based model with experiments with fission yeast to measure key parameters and test model predictions.

### The S. pombe nucleus behaves as an ideal osmometer

To quantify the osmotic forces that control cell and nuclear size, we experimentally determined the volume responses of fission yeast cells and their nuclei to osmotic shifts in their media. To visualize the cell and nucleus, we imaged fission yeast cells expressing a nuclear membrane marker (Ish1-GFP, Expósito-Serrano et al., 2020) and a plasma membrane marker (mCherry-Psy1 (Kashiwazaki et al., 2011, Figure 2A and B)). We placed live cells in flow chambers and treated them with media containing various concentrations of sorbitol, an osmotic agent (see Methods). Nuclear and cell volumes were measured using a semi-automated 3D segmentation approach (Methods; Figure 2—figure supplement 1A). As cells adapt to hyperosmotic shocks by gradually increasing glycerol production to recover their volume (Chen et al., 2003), we minimized these adaptation effects by taking measurements acutely upon shocks (<1 min) and by using a gpd1∆ mutant background that is delayed in this response (Hohmann, 2002; Minc et al., 2009, Figure 2—figure supplement 1A–C). To analyze volume responses, we used Boyle Van’t Hoff (BVH) plots in which the normalized volumes are plotted as a function of normalized inverse concentration in medium (Figure 2C). Ideal osmometers are characterized by linear responses following BVH’s Law (Nobel, 1969), showing that their volume is determined primarily by the osmotic environment with negligible effects of surface tension (Figure 2C; dotted line). In contrast, in cases with significant membrane tension, the plots exhibit non-linear responses (Figure 2C; green line). Further, the intersection of the BVH plot at the Y-axis provides a measure of the normalized non-osmotic volume ($ν_{b}$; Figure 2C).

![Figure 2.](https://cdn.elifesciences.org/articles/76075/elife-76075-fig2-v2.jpg)

**Figure 2.:** (A) Images of cells expressing a plasma membrane marker mCherry-Psy1 (green) and a nuclear envelope marker Ish1-GFP (purple). Individual cells in isotonic medium (Ciso) were shifted to hypertonic or hypotonic medium and imaged for 3D volume measurements (Materials and methods). (B) Images of individual protoplasts in response to hypertonic and hypotonic shifts. See also Figure 2—figure supplement 1. Scale bar = 5 µm. (C–E) BVH plots of the effects of osmotic shifts on the volume of the cell and nucleus. (C) Theoretical predictions of effects of osmotic concentration in the medium (Ciso/C) on the volume of a cell or nucleus with zero (black) or large (green) membrane tension (σ). Dashed line (black) depicts the behavior of an ideal osmometer in which there is no effect of membrane tension. (D) Effect of osmotic shifts on the relative volumes (V/Viso, mean ± STD) of whole fission yeast cells (N=707, three biological replicates) and protoplasts (N=441, from at least five biological replicates). (E) Effect of osmotic shifts on relative nuclear volume (V/Viso, mean ± STD) in protoplasts (N=441, from at least five biological replicates). Note that the response of nuclei fits to the predicted behavior of an ideal osmometer.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/76075/elife-76075-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Previous fission yeast cell studies estimated nuclear and cell volumes from length and single width measurements using assumptions of symmetric ellipsoid or cylindrical geometry (Facchetti et al., 2019; Kume et al., 2017; Lemière et al., 2021; Neumann and Nurse, 2007). As the shape of fission yeast cells are not perfectly symmetric ellipsoids, we determined volumes using a 3D segmentation approach (Machado et al., 2019). To minimize the adaptation responses to osmotic stress, most of these studies were done with cells with a gpd1∆ background, which is defective in glycerol synthesis responsible for the rapid volume adaptation to osmotic stresses (Hohmann, 2002). (A) N/C ratio is maintained in distinct cellular backgrounds. Scatter plot of cell size and nuclear size for asynchronous cells in growth medium. Right, Box and whisker plots of the N/C ratio for the three strains. Our 3D measurements of mean cell volume (97.5±27.1 µm3), nuclear volume (7.3±2.1 µm3), and the N/C ratio (7.5±0.8) of a population of asynchronous cells were consistent with previously reported values that used different image analysis methods. (Kume et al., 2017; Neumann and Nurse, 2007). For all box and whiskers plots, the horizontal line indicates the median, the box indicates the interquartile range (IQR) of the data set while the whiskers show the rest of the distribution within 1.5*IQR except for points that are defined as outliers. Statistical difference compared with an unpaired t-test. These data show that the N/C ratio measurements was not affected by the gpd1∆ background, or by use of different nuclear envelope markers ish1-GFP and cut11-GFP. (B&C) Time course of volume adaption in response to hyperosmotic shocks of 1 M sorbitol (B) and 0.5 M sorbitol (C). Normalized cell volume dynamics WT (chartreuse, N=12 cells) and gpd1Δ (green, N=12 cells) after 1 M sorbitol shock, mean ±STD. (C) Normalized cell and nucleus volume dynamics after 0.5 M sorbitol shock in WT (N=12) and gpd1Δ (N=10) background cells, mean values ±STD. These measurements of volume adaption enabled us to define time windows in which acute volume changes can be measured.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/76075/elife-76075-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) Defining an isotonic medium for protoplasts. The osmotic pressure of the medium changes the protoplasts’ volume and concentration of proteins due to addition or removal of water from the cell. To assess cytoplasmic concentration, we monitored fluorescence intensity of a protein E2-mCrimson expressed from the ACT1 promoter, which has been shown to normally maintain a largely constant concentration in whole cells throughout the cell cycle (Al-Sady et al., 2016; Knapp et al., 2019). mCrimson fluorescence intensity and cellular volume in a population of whole cells in isotonic medium (black) were similar to those of protoplasts in same medium supplemented with 0.4 M sorbitol (red), demonstrating that this is the isotonic condition for these protoplasts. Right panels, mid focal plane image of a cell (top) and protoplast (bottom) expressing mCrimson. (B) In contrast, comparison of mCrimson fluorescence intensities in protoplasts in 1 M sorbitol (dark red) and 0.4 M sorbitol (red), showed that 1 M sorbitol led to higher protein concentration than in isotonic conditions. (C–G) Number of intracellular osmolytes (N) was measured as described in Methods. Consistent with an ideal osmometer, N is directly proportional to the change in cell volume under osmotic shocks. N is proportional to the cell initial volume and does not depend on the range of osmotic shock used to probe the cells (Methods). R2 values are R-squared values for linear regression. Scale bar = 5 µm.

First, we analyzed the effect of osmotic shifts on cellular volume. Hyperosmotic shifts of various sorbitol concentrations caused sizable decrease (up to ~54%) in volume of cells, as previously noted (Atilgan et al., 2015; Knapp et al., 2019; Molines et al., 2022, Figure 2—figure supplement 1B–C). The BVH plot showed that the volume responses were non-linear, indicative of a non-ideal osmometer behavior (Figure 2D). The relationships were non-linear for both hyper- and hypotonic responses, consistent with the actions of the elastic cell wall that exerts compressive forces on the cell body and resists large expansions of volume (Atilgan et al., 2015; Davì and Minc, 2015; Schaber and Klipp, 2008).

To avoid the effects of the cell wall, we conducted osmotic shift experiments on protoplasts, which are yeast cells in which the cell walls has been enzymatically removed (Flor-Parra et al., 2014a; Lemière et al., 2021, Figure 2B). To maintain viability of protoplasts, sorbitol was added to the medium as osmotic support to substitute for the role of the cell wall and to prevent lysing. We determined the isotonic conditions for these protoplasts to be YE medium supplemented with 0.4 M sorbitol (hereafter called YE +0.4 M), as they had similar cytoplasmic properties as walled cells in YE +0 M sorbitol. At this concentration of sorbitol, an asynchronous population of protoplasts exhibited similar average volumes as those of walled cells in YE +0 M sorbitol, and similar cytoplasmic concentrations as assessed by fluorescence intensity of a cytoplasmic marker E2-mCrimson (Methods, Figure 2—figure supplement 2A–B, Al-Sady et al., 2016; Knapp et al., 2019). For osmotic shift experiments, we prepared protoplasts in this isotonic condition of YE +0.4 M sorbitol (Ciso), and then shifted them into medium containing a range of sorbitol concentrations below and above the isotonic condition (0.2–1.0 M). These methods allowed for quantitative probing of osmotic effects over a remarkable ~3 fold range of volume; notably, protoplasts were able to swell up to 40% in volume or shrink 40% without bursting.

The BVH plot of protoplast responses showed a linear behavior through this range of sorbitol concentrations (Figure 2D), indicative of an ideal osmometer. As the number of osmolytes is directly related to cell volume in osmotic shift experiments for ideal osmometers, this allowed us to estimate S. pombe solute concentration at ~30 × 107 solutes/µm3, which represents an osmolarity of 500±45 mOsmol (Methods, Figure 2—figure supplement 2C–G). The BVH plot also showed the normalized non-osmotic volume $ν_{b}^{C}$ to be 25%, similar to what has been previously reported for fission yeast cells (Atilgan et al., 2015) and other organisms (Dill et al., 2011; Ellis, 2001).

Having found that protoplasts behave as ideal osmometers, we then measured how nuclear volume responded to osmotic shocks. In hyperosmotic shifts, nuclei in both whole cells and protoplasts shrank into an abnormal involuted shape, suggesting a loss in volume but not surface area (Figure 2A and B), similar to what has been observed in mammalian cells (Kim et al., 2016). Strinkingly, in hypoosmotic shifts with protoplasts, nuclei were able to expand in <1 min into a spherical shape with an increase up to 40% in volume and 26% in surface area (Figure 2B and E). This large rapid expansion of the nuclear envelope suggested that the nuclear envelope can draw upon membrane stores, potentially from the endoplasmic reticulum (Fricker et al., 1997; Kume et al., 2019; Roubinet et al., 2021). BVH plots showed that the volume of nuclei in protoplasts followed a linear behavior in osmotic shifts over an impressive 3-fold range of volumes (Figure 2E). Importantly, this linear response showed that the nucleus behaved as an ideal osmometer. This finding implied that tension of the nuclear envelope was negligible on nuclear size: σN ≈ 0 N/m; the nuclear envelope does not exert tension that alters the volume response to osmotic forces, so that nuclear volume is directly responsive to its osmotic environment. The BVH plot also revealed that the normalized non-osmotic volumes in the nucleus $ν_{b}^{N}$ and cytoplasm $ν_{b}^{C}$ (i.e. the dry mass concentration) were similar (25% in nucleus; 25% in cytoplasm) (Figure 2D and E).

Thus, these experimental findings show that the protoplast and the nucleus approximate two nested spherical ideal osmometers as described in our theoretical model. As the physical properties of the nucleus are unlikely to change in the short amount of time needed to remove the cell wall, these results imply that the nucleus in whole cells (those with intact cell walls) are also ideal osmometers. Taken together, these findings indicated that fission yeast cells may be represented by the simplest version of the model where σN ≈ 0 N/m with matching $ν_{b}^{C}$ and $ν_{b}^{N}$ so that the N/C ratio is determined directly by the ratio of osmotically active molecules in the nucleoplasm to those in the cell.

### The N/C ratio does not depend on the presence of the cell wall

According to the model, the N/C ratio should be independent of the external tension (σC) and the outside concentration (Cout) (Figure 1). To reduce σC we examined the effects of removing the cell wall. The fission yeast cell wall has an elastic surface modulus of σC∼10–20 N/m which resists 1.5 MPa of turgor pressure (Atilgan et al., 2015; Minc et al., 2009). Upon removal of the cell wall, protoplasts are maintained in medium with sorbitol and have a five-orders-of-magnitude decrease in σC, with a membrane tension of ~4.5 × 10–4 N/m (Lemière et al., 2021). We tracked individual cells during cell wall digestion as they were converted to protoplasts (Figure 3A, right panel). There was no significant change in the N/C ratio before and after cell wall removal (Figure 3A, left panel). We noted that N/C ratios were slightly elevated in protoplasts in our initial population measurements, but this effect was due to loss of a portion of the cytoplasm trapped in the remaining cell wall during the process of protoplasting (Figure 3—figure supplement 1A). Thus, as predicted by our model, the N/C ratio is independent of the outer tension of the system (σC).

![Figure 3.](https://cdn.elifesciences.org/articles/76075/elife-76075-fig3-v2.jpg)

**Figure 3.:** (A) The N/C ratio of the same cells before and after cell wall digestion (mean ± STD) reveals no statistical differences (paired t test, p=0.36). Right panel, overlay of the plasma membrane (green) and nuclear membrane (purple) of the same cell middle plane before and after cell-wall digestion. For all box and whiskers plots, the horizontal line indicates the median, the box indicates the interquartile range of the data set (IQR) while the whiskers show the rest of the distribution within 1.5*IQR except for points that are defined as outliers. Scale bar = 5 µm. From six biological replicates. (B) Scatter plot of cell size and nuclear size for protoplasts under isotonic conditions (YE +0.4 M sorbitol) and immediately following osmotic shocks. Black and dashed red lines, measured N/C ratio of cells under isotonic conditions and osmotically shocked, respectively. From at least two biological replicates. (C) Protoplasts with the individual N/C ratio per osmotic condition described in (B). (D) Same as (B) for whole cells in YE under isotonic condition. Black line, measured N/C ratio of cells in isotonic conditions. From two biological replicates. (E) Same as (C) for whole cells with the individual N/C ratio per osmotic condition described in (D). See also Figure 3—figure supplement 1.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/76075/elife-76075-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) During protoplast preparation, a small portion of the cytoplasm was sometimes lost when the protoplast extruded out of the remaining cell wall. Image depicts a sum projection image of a protoplast with a portion of the plasma membrane (green) left behind (arrow). This behavior led to initial measurements that N/C ratio was slightly increased in some protoplasts compared to walled cells Figure 3B and D. To address this issue, for Figure 3 we therefore focused our analysis on cells that did not show any loss of cytoplasm during protoplasting. (B) Box and whisker plots for protoplasts showing individual cells volumes per osmotic condition described in main Figure 3. (C) (E) Same as (B) for protoplasts nuclei. (D) Separated plot from Figure 3B. Scatter plot of cell size and nuclear size for protoplasts under isotonic conditions (YE +0.4 M sorbitol, left panel) and immediately following osmotic shocks (right panel). Black and dashed red lines, measured N/C ratio of cells under isotonic conditions and osmotically shocked, respectively. (E) Box and whisker plots for whole cells showing individual cells volumes per osmotic condition described in main Figure 3. Mean ±STD are indicated under each condition. (F) Same as (E) for whole cells nuclei. (G) Separated plot from Figure 3D. Scatter plot of cell size and nuclear size for whole cells under isotonic conditions (YE, top panel) and immediately following osmotic shocks (bottom panel). Black and red lines, measured N/C ratio of cells under isotonic conditions and hypo-osmotically shocked, respectively. From two biological replicates. (H) Scatter plot of cell size and nuclear size for whole cells under isotonic conditions (YE) and immediately following hypo-osmotic shock. Black and blue lines, measured N/C ratio of cells under isotonic conditions and hypo-osmotically shocked, respectively. paired t test, p=0.0215 indicates a small difference in the N/C ratio. From two biological replicates. (I) Box and whisker plots for whole cells showing individual cells volumes per osmotic condition. Mean ±STD are indicated under each condition. (J) Same as (G) for whole cells nuclei. (I–J) Statistical differences indicate significant increase in nuclear and cell size under hypotonic cells (Wilcoxon paired t test, p<0.0001). For all box and whiskers plots, the horizontal line indicates the median, the box indicates the interquartile range (IQR) of the data set while the whiskers show the rest of the distribution within 1.5*IQR except for points that are defined as outliers.

### The N/C ratio is maintained under osmotic shifts in protoplasts and whole cells

An important prediction of the osmotic model is that the N/C ratio should not change upon osmotic shifts. To test this prediction, we subjected protoplasts to a range of hypo and hyper shocks and measured nuclear and cellular volumes. We varied sorbitol concentrations from 0.2 to 1.0 M with isotonic conditions defined as 0.4 M sorbitol (Figure 3—figure supplement 1B and C). A plot of nuclear versus cellular volumes showed scaling was robustly maintained throughout the range of osmotic conditions (Figure 3B, Figure 3—figure supplement 1D for separated plots). This was also shown by measurements of the N/C ratios at each sorbitol concentration (Figure 3C). Similar experiments in whole cells showed that the distribution of the N/C ratio under osmotic shock (0.1M to 1.0 M) also coincided with the distribution of the same population of whole cells in isotonic condition (Figure 3D–E, Figure 3—figure supplement 1E–G). Finally, we tested the effect of a hypo-osmotic shock on whole cells. Despite a significant increase of cells and nuclear volumes, the N/C ratio was maintained at 7.3±0.7 (Figure 3—figure supplement 1H–J). These results demonstrated that the N/C ratio does not change with the osmotic concentration of the media, confirming the predictions of the model that the sizes of the cell and nucleus are both regulated by osmotic pressures.

### Nanorheology reveals that physical properties of the cytoplasm and nucleoplasm are comparable under osmotic shocks

A key test of the model is to experimentally measure the relevant macromolecular concentrations and intracellular colloid osmotic pressures in both the cytoplasm and nucleoplasm. Recent advances have facilitated measurements of these parameters (Mitchison, 2019). We used forty nanometer-sized genetically encoded multimeric nanoparticles (GEMs) labeled with mSapphire fluorescent protein as nanorheological probes to quantitatively measure macromolecular crowding through analyses of their diffusive motions (Delarue et al., 2018; Knapp et al., 2019; Molines et al., 2022, Figure 4A, green). We used two versions of the GEMs: cytGEM and nucGEM, to measure crowding in the cytoplasm and nucleoplasm, respectively. The nucGEM protein is a version of GEMs that contains a nuclear localization signal (NLS) Szoradi et al., 2021; the NLS-GEM monomer is thought to be transported into the nucleus and retained once it assembles into the nucleus with the NLS embedded inside the spherical particle. Cells expressing this NLS-GEMs fusion exhibited motile fluorescent particles in the nucleus (Figure 4A). Projections of images over time showed that the nuclear GEMs were excluded from the nucleolus (Figure 4A, purple), so that nucGEMs primarily probe the properties of the nucleoplasm outside of the nucleolus.

![Figure 4.](https://cdn.elifesciences.org/articles/76075/elife-76075-fig4-v2.jpg)

**Figure 4.:** (A) Images of protoplasts (left) and whole cells (right) expressing cytoplasmic 40 nm GEMs and nucleoplasmic 40 nm GEMs. Top, single time point image; bottom, maximum projection of 100 frames. Dashed lines, the cell boundary. Scale bar = 5 µm. (B) GEMs effective diffusion coefficient (mean ± SEM) is slower in the cytoplasm (green) than in the nucleoplasm (purple) in whole cells in YE medium. Numbers indicate the number of tracks, p-value <0.0001 Mann-Whitney U test. (C) Effective diffusion coefficient of cytoplasmic GEMs (mean ± SEM) in protoplasts shifted to various sorbitol concentrations in the medium. Dashed lines, predictions of Phillies’ model for diffusion with a power law λ=1. NGEMs tracked = 4058, from at least two biological replicates per condition. (D) Effective diffusion coefficient of cytoplasmic GEMs (mean ± SEM) plotted against cell volume under hypotonic and hypertonic shock (light blue and blue background respectively). Volumes represent mean distribution of an asynchronous culture ± STD. Dashed line, fit of Phillies’ model for self-diffusing trackers in a polymer solution. Black arrow indicates Deff for a population of cells in YE and protoplasts in isotonic condition. Protoplasts: NGEMs = 3355, NVolume = 2216 cells, whole cells: NGEMs = 9849, NVolume = 981 cells. (E) Effects of hyperosmotic shifts on the relative effective diffusion coefficients (mean ± SEM) of cytoplasmic and nuclear GEMs; no statistically significant difference was detected (F-test, p-value = 0.90). Cytoplasm NGEMs = 9365,, nuclear NGEMs = 3732, from at least two biological replicates per condition. See also Figure 4—figure supplement 1.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/76075/elife-76075-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Example of MSD plots for cytoplasmic GEMs in whole cells under isotonic condition (0 M) or hypertonic shock (0.1–1.0 M of sorbitol). (B) Cytoplasmic (green) and nucleoplasmic (purple) GEM anomalous diffusion exponents for whole cells under osmotic shock. (C) Effects of hyperosmotic shifts on the effective diffusion coefficients (mean ± SEM) of cytoplasmic and nuclear GEMs; no statistically significant difference was detected (F-test, p-value = 0.90). Cytoplasm NGEMs = 9365, nuclear NGEMs = 3732, from at least two biological replicates per condition. (D) Example of cytoplasmic GEMs MSD plots in protoplasts in isotonic condition (0.4 M) or osmotically shocked (0.1–0.2 M and 0.6–1.0 M). (E) Anomalous diffusion exponent ⍺ obtained from linear fits of the MSD plots presented in (D). (F) Effective diffusion coefficient of cytoplasmic GEMs in protoplasts for various medium concentrations. Dashed lines, Phillies’ model for diffusion from three power law values: λ=0.5 (black), λ=1 (green), and λ=1.5 (gray).

We compared the behaviors of the GEMs in the cytoplasm and nucleoplasm. Mean square displacement (MSD) curves showed that the cytoplasmic GEMs displayed subdiffusive motion with an anomalous diffusive exponent α~0.9 comparable to measurements in HEK293, hPNE cells and S. cerevisiae (Delarue et al., 2018; Szoradi et al., 2021, Figure 4—figure supplement 1A–B). Nucleoplasmic GEMs exhibited a stronger subdiffusive behavior with α~0.8, suggesting a stronger caging effect compared to the cytoplasm (Figure 4—figure supplement 1B). Notably, nuclear GEMs consistently exhibited significantly higher Deff than cytoplasmic GEMs (DNeff ~0.55 µm2/s and DCyeff ~0.40 µm2/s, Figure 4B). These results demonstrated that at the 40 nm size scale, the ability of particles to diffuse is somewhat different in the nucleoplasm versus cytoplasm; these differences may reflect the differences in composition and nanoscale organization between nucleoplasm and cytoplasm. We also assessed cytoplasmic states in protoplasts compared to those in whole cells. Protoplasts in isotonic conditions exhibited similar Deff and α in the cytoplasm, showing that cytoplasmic properties probed by GEMs were not affected by removal of the cell wall (Figure 4D, black arrow; Figure 4—figure supplement 1D and E).

Next, we determined how Deff of the GEMs relates to macromolecular concentration. Because of the properties of the protoplasts as ideal osmometers, we were able to quantitatively tune macromolecule concentration in the cytoplasm by using osmotic shifts. We found that Deff of the cytoplasmic GEMs in protoplasts exhibited an exponential relationship with medium concentration and hence macromolecular concentration (Figure 4C). This relationship could be fit with a Phillies’ model (Masaro and Zhu, 1999; Phillies, 1988) which uses a unique stretched exponential equation to describe a tracer particle’s self-diffusive behavior in a wide range of polymer concentrations (Methods, Figure 4C, Figure 4—figure supplement 1F). The alignment of data from walled cells and protoplasts (Figure 4D) showed that this relationship also applied to cytGEMs analyses in walled cells. Hence, these relationships showed that Deff of the cytGEMs can be used to estimate the concentration of macromolecules in the cytoplasm over a large range of concentrations.

We then used the cytoGEMs and nucGEMs to determine how the nucleoplasm compares with the cytoplasm in their responses to osmotic shifts. The proportionate changes of nuclear and cellular volumes (Figure 3B–D) predicted that osmotic shifts affect the cytoplasm and nucleoplasm in similar ways. Indeed, even though the absolute values between cytoGEMs and nucGEMs Deff were slightly different, the normalized Deff and α values of cytoGEMS and nucGEMs were similar in cells treated with varying doses of sorbitol (Figure 4E, Figure 4—figure supplement 1B–E). Together, these findings showed that GEMs can be used to inform on relative changes in the concentration of macromolecules and resultant colloid osmotic pressures within each compartment; for example, both environments showed consistent behavior without evidence for sharp transitions in biophysical properties such as phase transitions. Therefore, these findings demonstrate that the movement of GEMs provides a quantitative approach to assess macromolecular crowding changes within the cytoplasm and nucleoplasm.

### Inhibition of nuclear export causes an increase in the N/C ratio

An important prediction is that changes in the relative numbers of osmotically active macromolecules in the nucleoplasm and cytoplasm would lead to a predictable change in the N/C ratio. It has been previously reported that inhibition of nuclear export leads to an increase in nuclear size, either through treatment with a drug leptomycin B (LMB, an inhibitor of the Crm1 exportin) or through mutants affecting the nuclear transport machinery (Kudo et al., 1999; Kume et al., 2017; Neumann and Nurse, 2007; Yoshida and Horinouchi, 1999). LMB causes the redistribution of only a small subset of proteins in Xenopus oocytes (Wühr et al., 2015). Our model predicted that inhibition of nuclear export would lead to an increase in macromolecule number in the nucleus relative to that in the cytoplasm. This redistribution would lead to increased osmotic pressure in the nucleus relative to cytoplasm, which would lead to expansion of nuclear volume and/or increased membrane tension. At steady state, in the absence of membrane tension, osmotic pressures and the concentrations of relevant macromolecules would equilibrate at a new larger N/C ratio.

In contrast to previous studies that described effects of LMB after hours of treatment (Kudo et al., 1998; Kume et al., 2019; Neumann and Nurse, 2007; Nishi et al., 1994), we examined the acute effects of LMB treatment in a time course, tracking both individual cells (Figure 5A–E) and asynchronous populations (Figure 5—figure supplement 1A–D). Upon LMB treatment, interphase fission yeast cells continued to grow at a similar rate as untreated cells, but their nucleus grew even faster (Figure 5A–C), causing a progressive increase in the N/C ratio from 8% to 9% in an hour (representing a 6% increase of the N/C ratio at 15 min and a 16% increase by 60 min)(Figure 5D–E).

![Figure 5.](https://cdn.elifesciences.org/articles/76075/elife-76075-fig5-v2.jpg)

**Figure 5.:** (A) Individual cells expressing plasma membrane and nuclear markers were imaged in time upon treatment with LMB or control (Ctrl). Images show a mid-focal plane of plasma membrane (green) and nuclear membrane (purple) treated with LMB (top) or not (Ctrl, bottom) over time (min). (B) Cell volumes were measured from 3D images. (C) Same as (B) for nuclear volume. (D) Box and whisker plot of N/C ratio of individual cells treated with LMB (cyan) and control condition (blue) at t=0 min and followed by time lapse microscopy. (E) N/C ratio dynamics of representative individual cells extracted from (D). (F) Cells expressing chromosomally tagged proteins that mark the large ribosomal subunit (Rpl3001-GFP) were treated with LMB and imaged over time. Mid focal plane confocal images and quantitation of their relative fluorescence intensities are displayed. Kruskal-Wallis statistical test was used. (G) Cells expressing cytoplasmic or nuclear GEMs were treated with LMB or control (0.05% ethanol) and were imaged for GEMs diffusion over time. Bar graphs show the relative changes in mean effective diffusion coefficients ± SEM for cytoplasmic (green) and nucleoplasmic (purple) GEMs in cells treated with LMB (left panel) and ethanol control (right panel). Statistical differences compared with Mann-Whitney U test. (A–G) From at least three biological replicates. (H) Cells were stained for total protein and RNA using FITC dye, plots indicate ratios of FITC intensities in nuclear and cytoplasmic regions over time after the addition of LMB. Statistical differences compared with Kruskal-Wallis test (p-value = 0.077), from at two biological replicates. (I) Normalized non-osmotic volume over time for cells and their nuclei in protoplasts treated with LMB. Scale bar = 5 µm. See also Figure 5—figure supplements 1 and 2.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/76075/elife-76075-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) Bright field mid-focal plane (top) and max Z-projection (bottom) images of the plasma membrane (green) and nuclear membrane (purple) of whole cells treated with LMB over time. Cells were selected to have approximately the same size. (B–C) Whole-cell volume and nuclear volume of distinct populations of cells treated with LMB and initial condition. (D) N/C ratio of a population of cells treated with LMB (light blue) and initial condition (blue). N≥463 per time point. (E–F) Cells expressing chromosomally tagged proteins that mark the large ribosomal subunit (Rpl2401-GFP) and the small ribosomal subunit (Rps2-GFP) were treated with LMB and imaged over time. Mid focal plane confocal images and quantitation of their relative fluorescence intensities are displayed. Statistical differences between 0 and 45 min were compared with Kruskal-Wallis test. (G) To reveal the distribution of total protein and RNA cells were fixed and stained with FITC dye. FITC fluorescence intensities along the normalized cell length were measured. (H) Same as (G), to reveal the distribution of total protein cells were also treated with RNAse. (G–H) FITC intensities in nuclear and cytoplasmic regions are defined by the signal in purple and green bar. Only a subpopulation of cells was plotted. (I) Evolution over time of the ratios of FITC intensities in nuclear and cytoplasmic regions after LMB treatment. Kruskal-Wallis statistical test was used, from at three biological replicates. Scale bar = 5 µm.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/76075/elife-76075-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (A–C) Time course of N/C ratio cellular volume and nuclear volume in individual control and LMB-treated protoplasts. (D) Z-sum projection image of the plasma membrane (green) and nuclear membrane (purple) of protoplasts over time treated with LMB (right) or not (Ctrl, left). Scale bar = 5 µm. (E) Scatter plot of cell size and nuclear size for protoplasts in isotonic condition treated with LMB for 15 min (YE +0.4 M sorbitol) and immediately following osmotic shock. Black line, N/C ratio of cells under isotonic condition (N/C=9%). Dashed line, N/C ratio of cells in isotonic condition before the addition of LMB (N/CT=0). (F) Same as (E) for protoplasts treated with LMB for 60 min. (G–H) Effect of osmotic shifts on the relative volumes (V/Viso, mean ±STD) protoplasts treated with LMB for 15 minutes (N=618, from at least two biological replicates). (I–J) Same as (G–H) for protoplasts treated with LMB for 60 minutes. (N=245, from at least two biological replicates).

We used multiple assays to assess quantitatively the redistribution of macromolecules and osmotic pressure effects in these cells. First, we measured the subcellular localization of ribosomal subunits. Ribosomes and their subunits are major components of biomass and contributors to macromolecular crowding in the cytoplasm (Delarue et al., 2018; Warner, 1999). Large ribosomal subunit proteins, which are transported into the nucleus to be assembled into pre-60S particles and then exported in a Crm1-dependent manner are known to be inhibited by LMB (Aitchison and Rout, 2000; Ho et al., 2000). We found that the concentrations of large ribosomal subunits Rpl3001 and Rpl2401 tagged with the GFP (Knapp et al., 2019) increased progressively in the nucleus so that by 60 min of LMB treatment, nuclear and cytoplasmic levels were similar (Figure 5F, Figure 5—figure supplement 1E). In contrast, a small ribosomal subunit protein Rps2-GFP (Knapp et al., 2019), which was not expected to be affected by LMB (Aitchison and Rout, 2000), showed little accumulation in the nucleus (Figure 5—figure supplement 1F). The cytoplasmic intensities of these three ribosomal markers decreased slightly by 45 min (Rpl3001 –19%, Rpl2401 –11% and Rps2-GFP –8%, Figure 5F, Figure 5—figure supplement 1E-F; right panel), which may be due to redistribution into the nucleus, as well through ribosomal turnover or impaired biogenesis. These examples illustrated how LMB causes a progressive redistribution of a subset of abundant proteins from the cytoplasm into the nucleus.

Second, we quantified concentrations of total protein and RNA by staining fixed cells with the fluorescent dye fluorescein isothiocyanate (FITC) and analyzed their fluorescence intensities (Knapp et al., 2019; Kume et al., 2017; Odermatt et al., 2021). FITC staining intensities in the cytoplasm and nucleoplasm were similar (ratio ~1) in both control cells and those treated with LMB (Figure 5H, Figure 5—figure supplement 1G). This assay suggested that there was no large redistribution in total protein and RNA. We quantified total protein without the RNA by FITC staining of cells treated with RNAse (Knapp et al., 2019; Odermatt et al., 2021). In control cells, this staining suggested that total protein concentration was lower in the nucleus than in the cytoplasm (Figure 5—figure supplement 1H–I). LMB-treated cells only exhibited a small (~8%) increase at 60 min in the ratio of nuclear to cytoplasmic protein staining compared to control cells (Figure 5—figure supplement 1I). This magnitude of protein accumulation in the nucleus was consistent with the observed increase in N/C ratio, as shown by simulations of the effects of redistributing solutes into the nucleus (Appendix 2—figure 1).

Third, we used the GEMs-based nanorheology to assess changes in the crowding of macromolecules. Deff of nuclear GEMs showed a small but significant initial decrease at 15 min of LMB treatment, but it subsequently returned to a normal level at 60 min (Figure 5G). In contrast, the cytGEMs Deff did not change significantly at 15 min, but increased significantly at 30 and 60 min. These results suggested that there may be a transient small increase in crowding in the nucleus at 15 min, but that crowding levels soon returned to normal; in contrast there was a more impressive progressive dilution of the cytoplasm (equivalent to 4% and 11% dilution at 30 and 60 min, respectively, Figure 5B, Figure 5—figure supplement 1E–F). LMB may lead to cytoplasmic dilution by inhibiting export of macromolecules such as mRNA out of the nucleus, leading to a decrease in protein synthesis, all while cells continue growing in volume at a normal rate (Figure 5B, Figure 5—figure supplement 1E–F, Neurohr et al., 2019).

Fourth, we determined the effects of LMB on the distribution of non-osmotic volumes $ν_{b}$ and nuclear membrane tension. To measure these parameters, we performed osmotic shift experiments on LMB-treated and control protoplasts and analyzed the results using BVH plots (similar to Figure 2). Protoplasts showed a similar increase in the N/C ratio in response to LMB (Figure 5—figure supplement 2A–D). The elevated N/C ratio was maintained upon osmotic shocks (Figure 5—figure supplement 2E–F); for instance, after 60 min of LMB treatment, protoplasts maintained an elevated N/C ratio of 10% over a range of hypoosmotic and hyperosmotic conditions (Figure 5—figure supplement 2F). BVH plots (Figure 5I) showed that in cells treated with LMB, the normalized non-osmotic volumes in the nucleus and cytoplasm were maintained at 25%. Thus, as nuclear volume increased, the total amount of non-osmotic volume (i.e. dry mass) increased proportionally so that its ratio remained constant. BVH plots also showed that the nuclei still behaved as ideal osmometers at the 15, 30, and 60 min timepoints (Figure 5—figure supplement 2G–J), indicating that membrane tension of the nucleus remained low throughout the time course.

In summary, we quantitated the effects on the nucleoplasm and cytoplasm during the progressive expansion in nuclear volume (16% increase in 60 min) in response to LMB. Various assays showed that LMB treatment not only caused an increase in the number of macromolecules in the nucleus, it also caused a progressive decrease in the number of macromolecules in the cytoplasm. The nucleus, which continued to act as an ideal osmometer, responded to these shifts by equilibrating to a larger size. Adjustments in nuclear volume may therefore maintain normal levels of crowding (GEMs) and density ($v_{b}$ and FITC staining) in the nucleus.

### Protein synthesis inhibition does not alter the N/C ratio

Another way to globally perturb macromolecular levels is by inhibiting protein synthesis. As LMB treatment disrupted ribosomal biogenesis (Figure 5F, Figure 5—figure supplement 1E–F), we tested whether inhibition of translation itself would alter the N/C ratio. We analyzed cells treated with 50 mg/mL cycloheximide (CHX, Polanshek, 1977, Figure 6A). At this relatively low dosage, interphase cells continued to grow in volume but at slower rates (Figure 6B). The nuclei also grew at the same slower rate, maintaining the N/C ratio (Kume et al., 2017, Figure 6C, D and E). This maintenance of the N/C ratio over time was also observed in asynchronous cell populations (Figure 6—figure supplement 1A–D). GEMs analyses revealed that Deff of nuclear and cytoplasmic GEMs increased proportionally (Figure 6F). Quantification of total protein and RNA on FITC stained cells showed no change in the ratio of nucleoplasmic to cytoplasmic distribution (ratio ~1) (Figure 6G, Figure 6—figure supplement 1E). However, FITC staining without the RNAs signal indicated a progressive decrease in concentration of total protein in both the nucleus and cytoplasm (Figure 6H, Figure 6—figure supplement 1F–G), leading to a ~30% decrease in total protein concentration in both compartments after 1 hr of CHX treatment.

![Figure 6.](https://cdn.elifesciences.org/articles/76075/elife-76075-fig6-v2.jpg)

**Figure 6.:** (A) Overlay of the plasma membrane (green) and nuclear membrane (purple) of whole cells middle plane over time treated with 50 mg/ml cycloheximide (CHX, top) or not (Ctrl, bottom). (B) Single whole-cell volume dynamics treated with CHX or not (Ctrl). (C) Same as (B) for single-nucleus volume dynamics treated with CHX or not (Ctrl). (D) Individual whole cells N/C ratio dynamics treated with CHX or not (Ctrl). (E) Single whole-cell N/C ratio dynamics extracted from (D) for each condition. (F) Relative cytoplasmic (green) and nucleoplasmic (purple) GEM effective diffusion dynamics for cells treated with CHX (left panel) or only the drug buffer for control (0.5% dimethyl sulfoxide (DMSO), right panel). Statistical differences compared with Mann-Whitney U test. (G) Cells were stained for total protein and RNA using FITC dye. Left, confocal middle plane image of cells before (0 min) or after CHX treatment for 60 min. Right, quantification ratios of FITC intensities in nuclear and cytoplasmic regions over time after the addition of CHX. Kruskal-Wallis statistical test was used, from at two biological replicates. (H) Cytoplasmic (green, left) and nucleoplasmic (purple, right) protein signals for the same cells over time under CHX treatment decrease similarly. Kruskal-Wallis statistical test was used. Scale bar = 5 µm. See also Figure 6—figure supplement 1. (A-F &H) From at least three biological replicates.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/76075/elife-76075-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A) Bright field (top) and max Z-projection (bottom) overlay of the plasma membrane (green) and nuclear membrane (purple) of whole cells treated with 50 mg/ml CHX over time. Cells were selected to have approximately the same size. (B–C) Whole-cell volume and nuclear volume of distinct populations of cells treated with CHX and initial condition. (D) N/C ratio of a population of cells treated with CHX (light blue) and initial condition (blue). N≥253 per time point. (E) Cells were stained with FITC dye to quantify protein and RNA distribution along the long cell axis of untreated cells, normalized by cell length. (F) As in (E) except cells were treated with RNAse for staining for total protein. (E–F) Purple and green boxes indicate the positions used to measure nuclear and cytoplasmic signals in Figure 5G–H. Only a subpopulation of cells was plotted. (G) Confocal middle plane image of cells stained with FITC for total protein, before (0 min) or after CHX treatment for 60 min. Scale bar = 5 µm.

These findings demonstrated that the proportionate dilution of macromolecular components in both compartments did not alter the N/C ratio. These experimental results strengthen our model of a nucleus behaving like an ideal osmometer for which a similar decrease in osmotically active particles in both sides of the nuclear envelope leads to a constant N/C ratio.

### N/C ratio homeostasis can be explained by an osmotic model for cell and nuclear growth

The N/C ratio is maintained with little variability, with a coefficient of variation of ~0.1 (Figure 7A, WT). The ratio is robustly maintained throughout the course of cell growth during the cell cycle (Figure 5D, Jorgensen et al., 2007; Neumann and Nurse, 2007), indicating that nuclear volume normally grows at the same rate as the volume of the cytoplasm. Like many other cell types, the growth rate of fission yeast cells is largely exponential in character, such that large cells grow faster than smaller ones (Knapp et al., 2019; Pickering et al., 2019; Tzur et al., 2009). One basis for this size dependence is thought to be due to the scaling of active ribosome number in the cytoplasm to cell size. The low variability of the N/C ratio suggests that it may be maintained by a homeostasis mechanism, so that cells with aberrant N/C ratio correct their nuclear size. Indeed, it was recently reported that S. pombe cells exhibit homeostasis behavior to maintain nuclear scaling (Cantwell and Nurse, 2019a; Neumann and Nurse, 2007). We sought to quantify this homeostasis behavior and to test whether the N/C ratio correction could be explained by a passive osmotic model or whether an additional active feedback mechanism needs to be invoked.

![Figure 7.](https://cdn.elifesciences.org/articles/76075/elife-76075-fig7-v2.jpg)

**Figure 7.:** (A) Asynchronous WT and pom1Δ whole cells N/C ratio (mean ±STD) in growth medium, from 1 biological replicate. (B) Z-sum projection overlay of the plasma membrane (green) and nuclear membrane (purple) of representative cells at septation (top) and divided (bottom) for WT (left) and pom1Δ (right). White arrow, septum location in the middle of WT cells and decentered for pom1Δ cells leading to asymmetric cell division. Scale bar = 5 µm. (C) N/C ratio over time for selected cells with low (light blue) or high (dark blue) initial N/C ratio. Dashed lines, linear regression for each cohort of cells. (D) Cellular growth rate as a function of a cell’s initial volume. Linear regression is shown in green with a slope γC. (D) N/C ratio change over time as a function of the initial N/C ratio. Experimental data (blue dots), linear fit (blue line), and predicted passive homeostasis N/C ratio behavior (black line) assuming N/C ratio = 7.5% at equilibrium from (A) and cell growth rate γC from (C). See also Figure 7—figure supplement 1. (F) Comparison of cell growth rate γC and the N/C ratio correction rate -γNC. (G–I) Same as D-F but in cells treated with 100 mg/ml CHX to decrease growth rate. (C–I) From two biological replicates.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/76075/elife-76075-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** (A) Wildtype and pom1Δ whole-cell volumes used for Figure 7A. (B) Same as A for nuclear volumes of WT (purple) and pom1Δ (pink) cells. (C) Nuclear and (D) cell volume dynamics for pom1Δ cells. Gray and black lines show tracks corresponding to two selected cells. The gray track represents a cell that divided before the end of the experiment. (E) The standard deviation (STD) of the N/C ratio measured for 91 pom1Δ cells decreases over time. (F) Cellular growth rate γC is independent of the N/C ratio. (G) Nuclear growth rate as a function of the initial N/C ratio over time. Nuclei in cells with high N/C ratio grow slower than nuclei in cells with low N/C ratio. (H) Nuclear growth rate as a function of a cell’s initial volume follows the predicted behavior described in Equation 8. Linear regression is shown in purple. (C–H) n=91 pom1Δ cells.

We measured homeostasis behavior in pom1∆ mutant cells, which display variable N/C ratios because of asymmetric cell division (Bähler and Pringle, 1998; Cantwell and Nurse, 2019a). Time lapse images showed that these cells exhibited normal mitosis that produced two equally sized nuclei, but often placed their division septum asymmetrically, yielding daughters that were born with either too low or too high N/C ratios (Figure 7A–B, Figure 7—figure supplement 1A–B). Consistent with this, an asynchronous population of pom1∆ cells displayed the same average N/C ratio as wildtype but with a ~threefold larger standard deviation (Figure 7A).

We tracked cell and nuclear growth in these cells with abnormal N/C ratio as they grew during interphase (Methods; Figure 7—figure supplement 1C–E). Cells born with abnormally large N/C ratios (>10) or abnormally small ratios (<7) gradually corrected their N/C ratio over time (Figure 7C, Figure 7—figure supplement 1E), consistent with previous findings (Cantwell and Nurse, 2019a). Cells exhibited an exponential growth rate of $\gamma_{C}≈0.006$ µm3/min, corresponding to an expected doubling time of ~115 min (Figure 7D). Cell growth rate was independent of their N/C ratio (Figure 7—figure supplement 1F). In contrast, nuclear growth rate was dependent on the N/C ratio: in cells with high N/C ratios nuclei grew slower than those in cells with normal N/C ratios, while nuclei in cells with low N/C ratios grew faster (Figure 7—figure supplement 1G). Cells with near normal N/C ratios showed little change in this ratio over time. These data revealed an inverse relationship between the initial ratio and the rate of correction (Figure 7E, blue dots). By fitting the N/C ratio change for a population of pom1∆ cells, we quantified the N/C ratio growth rate as a function of the initial N/C ratio (Figure 7E, blue line). This homeostasis plot revealed robust N/C ratio homeostasis behavior.

A previous paper proposed a model for N/C ratio homeostasis in which the rate of nuclear growth is function of the N/C ratio, suggestive of an active feedback mechanism ($dV^{N}/dt=0.73(0.12-NC)$, Cantwell and Nurse, 2019a). We tested whether this N/C ratio correction could be instead explained by a passive osmotic model without feedback. We built upon our simple osmotic model to incorporate dynamic growth (See Materials and methods and Appendix 2.2 for detailed derivations). We assumed that volume growth is driven by the rate of biosynthesis of cellular components that scales with the volume of the cytoplasm (Altenburg et al., 2019; Knapp et al., 2019; Midtvedt et al., 2019; Odermatt et al., 2021), likely dependent, in part, on the number of active ribosomes in the cytoplasm. The growth of the cytoplasm is driven by the biosynthesis of osmotically-active macromolecules targeted for the cytoplasm. Similarly, the growth of the nucleus is driven by the biosynthesis of macromolecules in the cytoplasm that are transported into the nucleus; assuming that nuclear transport is not limiting, the rate of nuclear growth may thus also scale with the volume of the cytoplasm. The balance of colloid osmotic forces in each compartment determines the cell and nuclear volumes. We also assumed that the rate of synthesis of nuclear components is a fixed percentage of total synthesis rate (e.g. 7.5%). Thus, assuming that the nucleus is an ideal osmometer, the percentage of total synthesis rate of components that end up in the nucleus versus in the cytoplasm is what ultimately sets the N/C ratio at equilibrium.

By assuming exponential cell growth, we can compute the change in N/C ratio over time such that:

$$
\frac{dNC}{dt}=\gamma_{C}f_{0}-NC
$$

where $f_{0}$ is a constant that represents the fraction of osmotically active particles transported into the nucleus and $\gamma_{C}$ is the exponential cellular growth rate. Our measurements gave us access to every parameter in Equation 4 with no free parameters.

The model predicts that in cells with an altered N/C ratio, the N/C ratio returns to $f_{0}$ over time, hence  $f_{0}$ = 7.5% ± 0.7% (Figure 7A, Appendix 2—figure 2). We used this relationship to determine the homeostasis behavior of the N/C ratio (Figure 7E, black line). Our experimental data were an excellent fit for this prediction using the measured parameters with no free parameters ($\gamma_{C}$ and N/C ratio at equilibrium; (Figure 7E; blue versus black lines)).

The model predicts that the rate at which cells correct aberrant N/C ratios $\gamma_{NC}$ is linked to the rate of cell growth ($\gamma_{C}=-\gamma_{NC}$). Our measurements showed indeed that these rates are similar (Figure 7F). It ensues from the model that an alteration in cellular growth rate would cause a proportionate change in the rate of N/C correction. To test this, we treated pom1 cells with a low dose of CHX that partially inhibits protein synthesis (Figure 7G). Under these conditions, the cell growth rate, and the N/C correction rate both decreased about threefold (Figure 7G,H) with $\gamma_{C}^{CHX}=-\gamma_{NC}^{CHX}$ (Figure 7I).

These findings show that the continued growth of the cell and nucleus is sufficient to explain the observed correction of the N/C ratio without having to invoke an active mechanism. The correction rates are on the time scales of growth rates, and thus large perturbations in N/C ratio were only partially corrected during a single cell cycle period. Modeling predicted that full correction of significant N/C alterations requires multiple generation times and showed how exponential growth dynamics versus linear growth dynamics affect N/C ratio correction dynamics (Appendix B -figure 2).

## Discussion

Here, we provide a quantitative model for nuclear size control based upon osmotic forces. This model, which has zero free parameters, postulates that nuclear size is dictated in part by the numbers of osmotically active molecules in the nucleus and cytoplasm that cannot readily diffuse through the nuclear membranes (Figure 1; see Appendix). These molecules, which include large proteins, RNAs, metabolites and other large molecules (>30 kDa), produce colloid osmotic pressure on the nuclear envelope to expand nuclear volume to a predicted size at steady state. Another potential parameter is membrane tension of the nuclear envelope, as determined by its ability to expand under pressure (Figure 1). In fission yeast, we determined that the nucleus readily changes in volume under osmotic perturbations, thus behaving as a near-ideal osmometer (Figure 2E); this behavior indicates that contributions of membrane tension of the nuclear envelope on nuclear size are negligible (or very small). The N/C ratio is then set as the ratio of nuclear to cytoplasmic solutes Equation 3; in the case of fission yeast, the number of these nuclear solutes is predicted to be about 8% of the total in the cell, giving rise to an average N/C ratio of 8%. Therefore, using this system, we confirm and define quantitatively the primary contributions of osmotic pressures to nuclear size control.

This physical model explains why the N/C ratio is so robustly maintained in the vast majority of mutant and physiological conditions (Cantwell and Nurse, 2019c). The N/C ratio arises because the cell globally maintains the relative quantities of nuclear to cytoplasmic solutes by protein expression and transport. During cell growth, the nucleus grows at the same rate as the cell because its growth is driven by the synthesis and transport of the nuclear macromolecules that contribute to osmotic pressure. This growth mechanism of the nucleus also explains the homeostasis behavior observed when the N/C ratio is too high or low (Figure 7). (Cantwell and Nurse, 2019a). The gradual correction of the N/C ratio by growth is reminiscent of ‘adder behavior’ for cell size homeostasis (Campos et al., 2014; Taheri-Araghi et al., 2015).

This proposed view suggests that the primary function of nuclear size control is perhaps not to specify a certain size, but to maintain healthy levels of macromolecular crowding in the nucleoplasm (Ellis, 2001). Our osmotic perturbations and GEMs measurements showed that the nuclear and cytoplasmic environments, which contain quite different components, nevertheless have similar degrees of mesoscale macromolecular crowding and similar concentrations of non-osmotic volumes. Even after long exposure to LMB, when cells exhibit a significative higher N/C ratio (Figure 5, Figure 5—figure supplement 2A), the normalized non-osmotic volumes of the nucleus and crowding in the nucleoplasm are similar to those in control cells (Figure 5I). The osmotic nature of nuclear size control thus allows nucleoplasm and cytoplasm to stay in balance through not only synthesis and transport but also by osmotic control of nuclear volume.

Our study provides a critical quantitative confirmation of proposed colloid osmotic pressure effects inside cells (Harding and Feldherr, 1958; Harding and Feldherr, 1959; Mitchison, 2019). Osmotic-based models for nuclear size control have been proposed (Churney, 1942; Kim et al., 2016), including a recent theoretical report (Deviri and Safran, 2022) that evaluates the potential colloid osmotic force contributions of chromatin (1.5 Pa), chromatin counterions (20 Pa), and proteins (8 kPa) to support a similar osmotic model. Our studies here provide quantitative experimental validation in a cell type in which nuclear size happens to be primarily dictated by colloid osmotic forces. The mechanisms by which macromolecules produce colloid osmotic pressure is complex and context dependent (Mitchison, 2019). For example, it has been postulated that charged macromolecules and DNA are surrounded by large number of counterions around them and collectively they exert osmotic effects (Donnan, 1911). However, under crowded conditions, colloid osmotic pressures generated by contact-interactions between macromolecules may predominate those generated by counterions (Mitchison, 2019).

This osmotic-based mechanism is likely the primary factor in nuclear scaling mechanisms in mammalian and other cell types. Osmotic shift experiments in mammalian chondrocytes cells (Finan et al., 2009) reveal that the nucleus in these cells is not an ideal osmometer, but is restricted from swelling due to hypoosmotic shocks because of nuclear membrane tension. Indeed, the BVH plot in this paper (Figure 1A of Finan et al., 2009) can be fitted with our model assuming NN=4.10–16 mol and a substantial nuclear membrane tension of σN = 0.02 N/m. This additional nuclear membrane tension may be due to nuclear lamina, peri-nuclear actin and/or perinuclear chromatin forces acting on the nuclear envelope (Edens et al., 2017; Newport et al., 1990; Schreiner et al., 2015), which may be absent or reduced in fission yeast . Thus, it is likely that osmotic forces act in concert with other mechanical elements to set nuclear size in these more complex systems. We note that models similar to ours can even account for bacterial nucleoid size scaling (Gray et al., 2019), where instead of a nuclear envelope tension term, a partition coefficient establishes the equilibrium concentration of molecules between the cytoplasm and the nucleoid/nucleus. Elucidation of mechanisms rooted in physics promise to give new insights into the range of nuclear shapes and sizes seen during development as well in diseases and aging (Foraker, 1954; Karoutas and Akhtar, 2021; Roubinet et al., 2021; Zink et al., 2004). Approaches such as osmotic shifts and nanorheology will allow for future investigation of similar osmotic mechanisms responsible for size control of the nucleus and other organelles.

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
      <td>Genetic reagent (Schizosacchoromyces pombe)</td>
      <td>mCherry-Psy1, Ish1-GFP</td>
      <td>This manuscript</td>
      <td>FC3318</td>
      <td>h- ade6 &lt;&lt;mCherry-psy1 ish1-GFP:kanMX ura4-D18</td>
    </tr>
    <tr>
      <td>Genetic reagent (S. pombe)</td>
      <td>gpd1 mutant, mCherry-Psy1, Ish1-GFP</td>
      <td>This manuscript</td>
      <td>FC3290</td>
      <td>h- ade6 &lt;&lt;mCherry-psy1 ish1-GFP:kanMX gpd1::hphMX6ura4-D18 ade6-</td>
    </tr>
    <tr>
      <td>Genetic reagent (S. pombe)</td>
      <td>gpd1 mutant</td>
      <td>This manuscript</td>
      <td>FC3291</td>
      <td>h- gpd1::hphMX6 ade6-M216 leu1-32 ura4-D18 his3-D1</td>
    </tr>
    <tr>
      <td>Genetic reagent (S. pombe)</td>
      <td>mCherry-Psy1, Cut11-GFP</td>
      <td>This manuscript</td>
      <td>FC3319</td>
      <td>h? cut11-GFP:ura4 +ade6:mCherry-psy1ura4-D18 leu1-32 ade6-M210</td>
    </tr>
    <tr>
      <td>Genetic reagent (S. pombe)</td>
      <td>gpd1 mutant, CytGEMs</td>
      <td>This manuscript</td>
      <td>FC3320</td>
      <td>h- gpd1::hphMX6 pREp41X-Pfv-Sapphire leu1-32 ade6- leu1-32 ura4-D18 his7-366</td>
    </tr>
    <tr>
      <td>Genetic reagent (S. pombe)</td>
      <td>gpd1 mutant, NucGEMs</td>
      <td>This manuscript</td>
      <td>FC3321</td>
      <td>h- gpd1::hphMX6 pREp41X-NLS-Pfv-Sapphire leu1-32 ade6- leu1-32 ura4-D18 his7-366</td>
    </tr>
    <tr>
      <td>Genetic reagent (S. pombe)</td>
      <td>CytGEMs</td>
      <td>This manuscript</td>
      <td>FC3289</td>
      <td>h- pREp41X-Pfv-Sapphire ade6-M216 leu1-32 ura4-D18 his3-D1</td>
    </tr>
    <tr>
      <td>Genetic reagent (S. pombe)</td>
      <td>NucGEMs</td>
      <td>This manuscript</td>
      <td>FC3322</td>
      <td>h- pREp41X-NLS-Pfv-Sapphire leu1-32 ade6- leu1-32 ura4-D18 his7-366</td>
    </tr>
    <tr>
      <td>Genetic reagent (S. pombe)</td>
      <td>pom1 mutant, mCherry-Psy1, Ish1-GFP</td>
      <td>This manuscript</td>
      <td>FC3323</td>
      <td>h- pom1::ura4 ade6 &lt;&lt;mCherry-psy1 ish1-GFP:kanMX</td>
    </tr>
    <tr>
      <td>Genetic reagent (S. pombe)</td>
      <td>Rpl3001-GFP</td>
      <td>Chang Lab collection</td>
      <td>FC3215</td>
      <td>h+rpl3001-GFP:kanR leu1-32 ura4-D18 ade6-210</td>
    </tr>
    <tr>
      <td>Genetic reagent (S. pombe)</td>
      <td>Rpl2401-GFP</td>
      <td>Chang Lab collection</td>
      <td>FC3213</td>
      <td>h- rpl2401-GFP:kanR leu1-32 ura4-D18 ade6-216</td>
    </tr>
    <tr>
      <td>Genetic reagent (S. pombe)</td>
      <td>Rps2-GFP</td>
      <td>Chang Lab collection</td>
      <td>FC3209</td>
      <td>h- rps2-GFP:kanR leu1-32 ura4-D18 ade6-210</td>
    </tr>
    <tr>
      <td>Genetic reagent (S. pombe)</td>
      <td>1XE2C, GFP-Psy1</td>
      <td>This manuscript</td>
      <td>FC3324</td>
      <td>h+act1p:1XE2C:HygR leu2:GFP-psy1 leu1- ura4-D18 his7-366</td>
    </tr>
    <tr>
      <td>Chemical compound/drug</td>
      <td>YES 225 Media</td>
      <td>Sunrise Science Production</td>
      <td>#2011</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound/drug</td>
      <td>Edinburgh Minimum Media (EMM)</td>
      <td>MP Biomedicals</td>
      <td>#4110–32</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound/drug</td>
      <td>Histidine</td>
      <td>Sigma-Aldrich</td>
      <td>#H8000</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound/drug</td>
      <td>Uracil</td>
      <td>Sigma-Aldrich</td>
      <td>#U0750</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound/drug</td>
      <td>Adenine</td>
      <td>Sigma-Aldrich</td>
      <td>#A9126</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound/drug</td>
      <td>Thiamine</td>
      <td>Sigma-Aldrich</td>
      <td>#T4625</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound/drug</td>
      <td>Lallzyme</td>
      <td>Lallemand</td>
      <td>#EL011-2240-15</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound/drug</td>
      <td>Leptomycin B (LMB)</td>
      <td>Alfa Aesar</td>
      <td>#87081-35-4</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound/drug</td>
      <td>Ethanol</td>
      <td>Fisher BioReagents</td>
      <td>#BP2818-500</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound/drug</td>
      <td>Dimethyl sulfoxide (DMSO)</td>
      <td>Fisher Scientific</td>
      <td>#67-68-5</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound/drug</td>
      <td>Cycloheximide (CHX)</td>
      <td>Sigma-Aldrich</td>
      <td>#C7698</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound/drug</td>
      <td>Agarose</td>
      <td>Invitrogen</td>
      <td>#16500500</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound/drug</td>
      <td>4% formaldehyde (methanol-free)</td>
      <td>Thermo Scientific</td>
      <td>#28,906</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound/drug</td>
      <td>RNAse</td>
      <td>Thermo Scientific</td>
      <td>#EN0531</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound/drug</td>
      <td>Fluorescein isothiocyanate isomer I (FITC)</td>
      <td>Sigma</td>
      <td>#F7250</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>µManager v. 1.41</td>
      <td>Edelstein et al., 2010; Edelstein et al., 2014</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Matlab</td>
      <td>Mathworks</td>
      <td>R2018b</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Python</td>
      <td>Drake Jr and Van Rossum, 1995</td>
      <td>5.5.0</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Prism</td>
      <td>GraphPad</td>
      <td>Version 9.3.1</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>FIJI ImageJ</td>
      <td>Schindelin et al., 2012</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>µ-Slide VI 0.4 channel slide</td>
      <td>Ibidi</td>
      <td>#80,606</td>
      <td>microfluidic chambers</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>µ-Slide VI 0.5 glass bottom channel slides</td>
      <td>Ibidi</td>
      <td>#80,607</td>
      <td>microfluidic chambers</td>
    </tr>
  </tbody>
</table>

### Yeast strains and media

Schizosaccharomyces pombe strains used in this study are listed in Key Resource Table. In general, fission yeast cells were grown in liquid cultures in rich medium YES 225 (#2011, Sunrise Science Production) at 30 °C with shaking. Strains carrying GEM expression vectors were grown in EMM3S – Edinburgh Minimum Media (#4110–32, MP Biomedicals) supplemented with 0.225 g/L of uracil, histidine, and adenine as well as 0.1 µg/mL of thiamine (#U0750, #H8000, #A9126, #T4625, Sigma-Aldrich).

### Microscopy

Cells were imaged on a Ti-Eclipse inverted microscope (Nikon Instruments) with a spinning-disk confocal system (Yokogawa CSU-10) that includes 488 nm and 541 nm laser illumination and emission filters 525±25 nm and 600±25 nm respectively, a 60 X (NA: 1.4) objective, and an EM-CCD camera (Hamamatsu, C9100-13). These components were controlled with µManager v. 1.41 (Edelstein et al., 2010; Edelstein et al., 2014). Temperature was maintained by a black panel cage incubation system (#748–3040, OkoLab).

For imaging of GEMs, live cells were imaged with a TIRF Diskovery system (Andor) with a Ti-Eclipse inverted microscope stand (Nikon Instruments), 488 nm laser illumination, a 60 X TIRF oil objective (NA:1.49, oil DIC N2) (#MRD01691, Nikon), and an EM-CCD camera (Ixon Ultra 888, Andor), controlled with µManager v. 1.41 (Edelstein et al., 2010; Edelstein et al., 2014). Temperature was maintained by a black panel cage incubation system (#748–3040, OkoLab).

For most live cell imaging, cells were mounted in µ-Slide VI 0.4 channel slides (#80606, Ibidi – 6 channels slide, channel height 0.4 mm, length 17 mm, and width 3.8 mm, tissue culture treated and sterilized). The µ-Slide channel was coated by pre-incubation with 100 µg/mL of lectin (#L1395, Sigma) for 15 min at room temperature, and then washed with medium. Cells in liquid culture were introduced into the chamber for 3 min and then washed three times with medium to remove non-adhered cells. As certain drugs may adhere to polymer slide material in the conventional chambers, µ-Slide chambers with glass bottoms (#80607, Ibidi – 6 channels slide, channel height 0.54 mm, length 17 mm and width 3.8 mm, D263M Schott glass and sterilized) were used for the drug treatments.

### 3D volume measurements

Nuclear and cell volumes were measured in living fission yeast cells expressing a nuclear membrane marker (Ish1-GFP, Expósito-Serrano et al., 2020) and a plasma membrane marker (mCherry-Psy1, Kashiwazaki et al., 2011) using a semi-automated 3D segmentation approach. Z stack images (0.5 µm z-slices) that covered the entire cell (for a total of ~20 slices) were obtained using spinning disk confocal microscopy. The 3D volumes were segmented using an ImageJ 3D image segmentation tool LimeSeg (Machado et al., 2019; Schneider et al., 2012) with these parameters:

For cells: run("Sphere Seg", "d_0=3.0 f_pressure = 0.016 z_scale = 4.5 range_in_d0_units = 3.0 color = 51,153,0 samecell = false show3d=false numberofintegrationstep=-1 realxypixelsize = 0.111"); For nuclei: run("Sphere Seg", "d_0=2.0 f_pressure = 0.016 z_scale = 4.5 range_in_d0_units = 2.0 color = 51,153,0 samecell = false show3d=false numberofintegrationstep=-1 realxypixelsize = 0.111").

After each 3D analysis converged, segmentation results were confirmed using a 2D result. If there was a discrepancy, additional analyses on individual cells were used, with multiple circular regions of interest if necessary. Data were analyzed with Python on Jupiter Notebook 5.5.0. In general, experiments are representative of at least two biological replicates with independent data sets as described in the figure legends.

### Protoplast preparation

S. pombe cells were inoculated from fresh agar plates into YES 225 or EMM3S liquid cultures and grown at 30 °C for about 20 hr into exponential phase (OD600=0.2–0.3). Ten milliliters of cells were harvested by centrifugation 2 min at 400 rcf, washed two times with SCS buffer (20 mM sodium citrate, 20 mM citric acid , 1 M D-sorbitol, pH = 5.8), resuspended in 1 mL of SCS buffer with 0.1 g/mL Lallzyme (#EL011-2240-15, Lallemand), and incubated with gentle shaking for 10 min at 37 °C in the dark (Flor-Parra et al., 2014b). The resulting protoplasts were gently washed three times in YES 225 or EMM3S with 0.4 M D-sorbitol, using centrifugation for 2 min at 400 rcf between washes. After the last wash, 900 µL of supernatant were removed, and the protoplasts in the pellet were gently resuspended in the remaining ~100 µL of solution. The resultant protoplasts were introduced into a lectin-coated µ-Slide VI 0.4 channel slide for imaging.

### Osmotic shocks

Fission cells or protoplasts were loaded in a lectin-treated µ-Slide VI 0.4 channel slide and maintained at 30 °C. After 5 min of incubation, cells were washed three times with their respective initial buffer (isotonic condition). Cells were imaged first in their initial buffer (isotonic condition). Then, hyper or hypotonic medium was introduced into the channel with three washes. For hypotonic medium YES 225 was diluted with sterile water. The same individual cells were then imaged (within 1 min of the osmotic shift) using the same parameters. To minimize the effect of volume adaptation response to osmotic shock, we assayed cells within 1 min of the osmotic shift and performed most of our experiments using cells in gpd1∆ mutant background that is defective in this response (Figure 2—figure supplement 1B and C, Hohmann, 2002; Minc et al., 2009).

### Diffusion imaging and analysis of GEMs

For cytoplasmic 40 nm GEMs, Pfv encapsulin-mSapphire was expressed in fission yeast cells carrying the multicopy thiamine-regulated plasmid pREP41X-Pfv-mSapphire (Delarue et al., 2018; Molines et al., 2022). For nuclear 40 nm GEMs, NLS-Pfv-mSapphire was expressed from a similar pREP41X-NLS-Pfv-mSapphire plasmid (Szoradi et al., 2021). The expression of these constructs was under the control of the thiamine repressible nmt41 promoter (Maundrell, 1990). Cells were grown using a protocol that produced appropriate, reproducible expression levels of the GEMs: cells carrying these plasmids were grown from a frozen stock on EMM3S -LEU plates without thiamine for 2–3 days at 30 °C and stored at room temperature for 1–2 days to induce expression. Cells were then inoculated in liquid EMM3S -LEU with 0.1 µg/mL of thiamine (#T4625-25G, Sigma Aldrich) for partial repression of the nmt41 promoter and grown for one day at 30 °C to exponential phase.

Cells in lectin-treated µ-Slide VI 0.4 channel slides (#80606, Ibidi) were imaged in fields of 250 × 250 pixels or smaller using highly inclined laser beam illumination at 100 Hz for 10 s. GEMs were tracked with the ImageJ Particle Tracker 2D-3D tracking algorithm from MosaicSuite (Sbalzarini and Koumoutsakos, 2005) with the following parameters: run("Particle Tracker 2D/3D", "radius = 3 cutoff = 0 per/abs = 0.03 link = 1 displacement = 6 dynamics = Brownian").

The analyses of the GEMs tracks were like those described in Delarue et al., 2018, with methods to compute mean square displacement (MSD) using MATLAB (MATLAB_R2018, MathWorks). The effective diffusion coefficient Deff was obtained by fitting the first 10 time points of the MSD curve (MSDtruncated) to the canonical 2D diffusion law for Brownian motion: MSDtruncated($\tau$)=4 Deff $\tau$. In general, experiments are representative of at least 2 biological replicates with independent data sets as described in the figure legends.

### LMB treatment

A stock solution of 0.1 mM LMB (#87081-35-4, Alfa Aesar) in ethanol (#BP2818-500, Fisher BioReagents) was prepared. The final concentration of 25 ng/mL in YES 225 contained 2.3 µL of the stock solution and 5 mL of cell culture. For imaging individual cells over time, exponential phase cells were placed in a µ-Slide VI 0.5 glass bottom channel slide (#80607, Ibidi). Cells where washed three times with a solution of YES 225+25 ng/mL LMB and then imaged. For measurements of a population of cells over time, exponential-phase cells were incubated with the drug at 30 °C with shaking. At each time point, 1 mL of the cell culture was harvested and centrifuged for 2 min at 0.4 rcf. One microliter of the pellet was spread on an 1% agarose (#16500500, Invitrogen) pad (with no drug added), sealed with Valap, and imaged within 5 min.

### Cycloheximide treatment

Cycloheximide (CHX, #C7698, Sigma-Aldrich) stock was prepared at 5 mg/mL in dimethyl sulfoxide (#67-68-5, Fisher Scientific) and stored at –20 °C. CHX was added to a final concentration of 50 µg/mL in Figure 7 and 100 µg/mL in Figure 6.

### FITC staining

Total protein was measured in individual fission yeast cells using FITC staining, similarly as described (Knapp et al., 2019; Odermatt et al., 2021). One milliliter of cell culture was fixed with 4% formaldehyde (methanol-free solution, #28906, Thermo Scientific, Waltham) for 60 min, washed with phosphate buffered saline (PBS) (#14190, Thermo Scientific,), and stored at 4 °C. One hundred microliters of fixed cells was treated with 0.1 mg/mL RNAse (#EN0531, Thermo Scientific) and incubated in a shaker for 2 hr at 37 °C. Next, cells were washed and re-suspended in PBS and stained with 50 ng/mL FITC (#F7250, Sigma) for 30 min, washed three times, and resuspended in PBS. Cells were mounted on a 1% agarose +PBS pad and imaged in bright field and with 488 nm laser illumination via spinning disk confocal microscopy. The FITC signal was acquired in 300 nm z-step stacks that covered the entire cell volume. For each selected cell, the FITC signal intensities were measured along the long cell axis (averaged over 10 pixels in width) and normalized by cell length. The signal was corrected for background intensity and normalized by the maximum intensity along the line profile within each cell (Figure 5—figure supplement 1G,H, Figure 6—figure supplement 1E,F). The nuclear and cytoplasmic FITC signals were defined as the sum of the signal from respectively 0.45–0.55 (middle of the cell, for the nucleus) and 0.7–0.8 (for the cytoplasm) along the normalized cell length normalized by the mean value at 0 min.

### N/C ratio homeostasis measurements

pom1∆ cells were grown in exponential phase in YES 225, loaded in a µ-Slide VI 0.4 channel slide (#80606, Ibidi), and imaged every 4 min for 40 min at 30 °C. The 3D volumes of each cell and nucleus were measured over time, and interphase growth rates were obtained by extracting the slope of a linear regression to the data over 40 min using a custom-written Python script. Growth rate of mitotic cells were not included in the analysis.

### mCrimson concentration measurements

For Figure 2—figure supplement 2A and B, m-Crimson intensity was measured for each cell using the mean fluorescence intensity of a ROI selected in the middle plane of the cell, corrected by the mean fluorescence of the background. The volume of the same cell was measured using the 3D measurement method described above.

### Determination of the intracellular osmolarity in S. pombe

For an ideal osmometer, the volume is solely determined by the balance between the outside and the intracellular concentration of osmotically active particles. As we reported that protoplasts behave like ideal osmometers (Figure 2D) they can therefore be used to quantify the number of osmolytes (NC) in S. pombe. For an ideal osmometer, NC is directly related to the cell volume (VC):

$$
\frac{N^{C}}{V^{C}-b^{C}}=C^{out}
$$

We explored the response of protoplast volumes VC to changes in medium concentration (Cout) for various osmotic shocks. Protoplasts were prepared in an isotonic solution and shifted in hypo or hyper conditions by the addition or removal of sorbitol in the buffer. The variation of total concentrations ∆Cout = Cfinal-Cinitial were known. Meanwhile, variations of cells’ volume were measured before and after shocks. Since the cell non-osmotic volume bC does not vary under osmotic shocks, we extracted the only unknown parameter of the equation: each cell’s value of NC. We found that NC is linearly related to the cell volume (Figure 2—figure supplement 2C–G), which means that cells keep a constant concentration of osmolytes during the cell cycle. We also confirmed by analyzing various shocks such that ∆Cout spanned from –0.2 to 0.6 M that NC does not depend on the range of osmotic shocks used to measure it (Figure 2—figure supplement 2C). The intracellular osmolyte concentration in S. pombe remained constant at a concentration of ~30.107 solutes/µm3.

### Measurement of effective diffusivity

Under acute osmotic perturbations, cell volume changes due to the flow of water, which also affects molecular crowding and the effective GEMs diffusion. We took advantage of these quantitative measurements to assess whether the change in GEMs movements due to osmotic shocks could be explained with a physical model of diffusion in polymer solution. Phillies’ model (Masaro and Zhu, 1999; Phillies, 1988) uses a unique stretched exponential equation to describe a tracer particle self-diffusive behavior in a wide range of polymer concentrations.

$$
D_{eff}=D_{0}e^{-\betaC^{\lambda}}
$$

where D0 is the diffusion of the tracer particle in aqueous solution, C is the concentration of polymers, and $\beta$ and $\lambda$ are scaling parameters. D0 can be calculated using the Stokes-Einstein relation for a spherical particle of 40 nm diameter in water. Because protoplasts behave like ideal osmometers (Figure 2C and D), their macromolecular intracellular concentration is proportional to the medium concentration Cout. We took advantage of this behavior to probe the variation of Deff as a function of the medium concentration and found that $\lambda=1$ fit our data (Figure 4C, Figure 4—figure supplement 1F). $\lambda$ has been found in in vitro experiments to depend on the molecular weight of the proteins (Banks and Fradin, 2005). Interestingly, $\lambda≈1$ corresponds to a polymer molecular weight of 43.5 kDa close to the average protein molecular weight for Eukaryotes (~50 kD Milo and Phillips, 2015) that fits our in vivo data. Protoplasts behave like ideal osmometers such that we can express the intracellular concentration C in the Phillies’ model as a function of the cell volume for each osmotic shock and see whether Deff follows this model for which we now have only one free parameter. The model, assuming a change in intracellular concentration, is in agreement with our experimental values under acute osmotic shifts (Figure 4C). We also found that the values for Deff and cell volumes measured on whole cells followed the same model (Figure 4D).

### Modeling nuclear growth and N/C ratio homeostasis

We started with a simple model for which nuclear growth was proportional to cell growth while keeping the osmotic behavior of the nucleus: nuclear volume is proportional to the number of osmotically active particles it contains. To determine the cells’ growth rate, we imaged cells at 30 °C initially at various stages of the cell cycle every 4 min for 40 min or until division happened. We plotted the change in cells volume as a function their volume at the beginning of the experiment and found a good linear correlation revealing that S. pombe growth is exponential with a growth rate $\gamma_{C}≈0.006$ µm3/min (Figure 7D) in the same range as previously reported values:

$$
\frac{dV^{C}}{dt}=\gamma_{C } V^{C}
$$

If now we assume that the nuclear growth rate is coupled (by a constant of proportionality) to the cell growth rate (Figure 7—figure supplement 1H), then the change in nuclear volume can be written as:

$$
\frac{dV^{N}}{dt}= f_{0} \gamma_{C}V^{C}
$$

where $f_{0}$ is a constant that represents the fraction of osmotically active particles synthesized by the cell that will enter the nucleus. As shown in SM Section S2.2, combining Equation 7 and Equation 8 results in Equation 4 for the rate of change of the N/C ratio.
