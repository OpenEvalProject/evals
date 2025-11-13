# 3D reconstruction of neuronal allometry and neuromuscular projections in asexual planarians using expansion tiling light sheet microscopy

## Authors

- Jing Lu<sup>1</sup>
- Hao Xu<sup>1</sup>
- Dongyue Wang<sup>2</sup>
- Yanlu Chen<sup>2</sup>
- Takeshi Inoue<sup>6</sup> ([ORCID: 0000-0003-3289-4478](https://orcid.org/0000-0003-3289-4478))
- Liang Gao<sup>2</sup> ([ORCID: 0000-0001-9983-0626](https://orcid.org/0000-0001-9983-0626)) †
- Kai Lei<sup>3</sup> ([ORCID: 0000-0003-0601-7391](https://orcid.org/0000-0003-0601-7391)) †

### Affiliations

1. College of Life Sciences, Zhejiang University Hangzhou China ([ROR:00a2xv884](https://ror.org/00a2xv884))
2. Key Laboratory of Structural Biology of Zhejiang Province, School of Life Sciences, Westlake University Hangzhou China ([ROR:05hfa4n20](https://ror.org/05hfa4n20))
3. Westlake Laboratory of Life Sciences and Biomedicine Hangzhou China
4. Key Laboratory of Growth Regulation and Translational Research of Zhejiang Province, School of Life Sciences, Westlake University Hangzhou China ([ROR:05hfa4n20](https://ror.org/05hfa4n20))
5. Institute of Biology, Westlake Institute for Advanced Study Hangzhou China
6. Division of Adaptation Physiology, Faculty of Medicine, Tottori University Yonago Japan ([ROR:024yc3q36](https://ror.org/024yc3q36))

† Corresponding author

## Abstract

The intricate coordination of the neural network in planarian growth and regeneration has remained largely unrevealed, partly due to the challenges of imaging the CNS in three dimensions (3D) with high resolution and within a reasonable timeframe. To address this gap in systematic imaging of the CNS in planarians, we adopted high-resolution, nanoscale imaging by combining tissue expansion and tiling light-sheet microscopy, achieving up to fourfold linear expansion. Using an automatic 3D cell segmentation pipeline, we quantitatively profiled neurons and muscle fibers at the single-cell level in over 400 wild-type planarians during homeostasis and regeneration. We validated previous observations of neuronal cell number changes and muscle fiber distribution. We found that the increase in neuron cell number tends to lag behind the rapid expansion of somatic cells during the later phase of homeostasis. By imaging the planarian with up to 120 nm resolution, we also observed distinct muscle distribution patterns at the anterior and posterior poles. Furthermore, we investigated the effects of β-catenin-1 RNAi on muscle fiber distribution at the posterior pole, consistent with changes in anterior-posterior polarity. The glial cells were observed to be close in contact with dorsal-ventral muscle fibers. Finally, we observed disruptions in neural-muscular networks in inr-1 RNAi planarians. These findings provide insights into the detailed structure and potential functions of the neural-muscular system in planarians and highlight the accessibility of our imaging tool in unraveling the biological functions underlying their diverse phenotypes and behaviors.

## Introduction

The CNS stands as a marvel of intricate organization, enabling the execution of complex functions crucial for an organism’s survival (Cajal, 1995). It is the hub for processing and coordinating information throughout the body, employing specialized regions with distinct structures and functions (Bullock and Horridge, 1965). However, the regenerative capacity of the CNS poses a formidable challenge, as it exhibits limited ability for de novo regeneration (Obernier et al., 2014).

The planarian CNS is a fascinating model for studying neural regeneration (Agata et al., 1998). Planarians are flatworms that possess a relatively simple CNS, yet they have an impressive ability to regenerate their neural tissue. The planarian CNS is organized into different molecular and functional domains defined by the expression of specific neural genes (Cebrià et al., 2002b). Planarians can regenerate functional brains from even tiny body fragments, highlighting their remarkable regenerative capabilities (Umesono and Agata, 2009). This unique regenerative potential is attributed to the presence of pluripotent stem cells called neoblasts, which can differentiate into various cell types, including neurons (Cebrià, 2007). The availability of hundreds of genes expressed in planarian neurons, coupled with the ability to silence them through RNA interference, has facilitated the unraveling of the molecular mechanisms underlying CNS regeneration in these organisms (Cebrià, 2007). The study of planarian CNS regeneration provides valuable insights into the fundamental processes of neural regeneration, which may have implications for regenerative medicine and understanding human nervous system repair.

Understanding the mechanisms underlying CNS regeneration requires applying powerful tools to study its structure and organization at the cellular to sub-cellular levels. Advanced imaging techniques, including high-resolution microscopy, offer exceptional opportunities to gain invaluable insights into the intricate architecture of the CNS. Gained from advanced imaging techniques, researchers can harness knowledge from the regenerative wonders observed in nature that hold promise for promoting CNS regeneration (Dodt et al., 2007; Tomer et al., 2011). However, the intricate network and the dynamics of planarian CNS have remained largely unrevealed due to the challenges of imaging the CNS in 3D with high resolution within a reasonable timeframe.

Tiling light sheet microscopy (TLSM) is a flexible imaging technique that has been adapted for use in live organisms and cleared tissues (Gao, 2015; Fu et al., 2016). Its flexible multicolor 3D imaging ability has been shown across a variety of samples, from structures as complex as the mouse spinal cord to the intricate tissues of planarians (Chen et al., 2020; Xie et al., 2023). In TLSM, a thin and focused light sheet is used to illuminate the sample from the side, exciting fluorophores close to the focal plane. By tiling the light sheet within the imaging field of view at multiple positions and using the images generated by the thinnest section of the light sheet, researchers can create a comprehensive and high-resolution image of the entire sample. This method combines the benefits of light sheet microscopy, which offers high spatial resolution and imaging speed, with tiling capabilities to capture larger samples (Chen et al., 2020). This technique is particularly useful for imaging cleared tissues, enabling rapid multicolor 3D imaging with micron-scale to submicron-scale spatial resolution (Chen et al., 2020). Expansion microscopy has been employed in planarian studies for the detailed visualization of neuronal structures (Wang et al., 2016; Khariton et al., 2020). It remained a challenge to image the entire CNS in 3D at high resolution within a reasonable time frame. While tissue clearing is a common practice in microscopy, we found it particularly useful as a pre-expansion treatment for lipid-rich samples such as planarians. This process allows homogenization without the need for heating or proteinase treatment. Clearing and Magnification Analysis of Proteome (C-MAP) was able to preserve the natural proteins during expansion, which allows the use of conventional FISH and antibody staining (Chen et al., 2020). The combination of C-MAP and tiling light sheet microscopy has achieved improved 3D resolution, signal-to-noise ratio, and sample compatibility (Chen et al., 2015; Ku et al., 2016; Tillberg et al., 2016; Chang et al., 2017; Gao et al., 2019; Wassie et al., 2019). TLSM has greatly advanced our understanding of complex biological systems and has opened new possibilities for studying cellular dynamics and interactions within multicellular organisms (Gao, 2015; Fu et al., 2016). The combination of TLSM and C-MAP suggests a potential method to study the regenerative CNS in planarian and other non-traditional model organisms.

In this study, we applied TLSM and C-MAP to record the planarian spatial information at single cellular or higher resolution levels. We present a 3D tissue reconstruction method to investigate neuron type diversity and development at the single-cell level by labeling various neuron types, including cholinergic, GABAergic, octopaminergic, dopaminergic, and serotonergic neurons. We successfully quantitatively profiled neurons at the single-cell level in over 400 wild-type planarians during homeostasis and regeneration. In addition to obtaining higher resolution images of known structures within planarians, such as muscles, we also discovered previously unreported muscle-muscle and neuron-muscle connections. We further provided evidence that suggests muscle fibers as a scaffold for targeted neuron projection. These results are of significant interest as they contribute to our understanding of how the primitive CNS coordinates the behavior and the underlying mechanism involved in the precise regeneration of neurons and their networks.

## Results

### Establishment of 3D tissue reconstruction using expansion tiling light sheet microscopy for planarian Schmidtea mediterranea

We first set up the experiment pipeline utilizing Clearing and Magnification Analysis of Proteome (C-MAP) for planarian expansion and tiling light-sheet microscope (TLSM) for imaging (Figure 1A). The expansion procedure was performed after the conventional staining in planarians (Chen et al., 2020). To improve the efficiency of sample processing, we have made several modifications to the original protocol (Figure 1A). First, we incorporated tissue clearing to ensure uniform homogenization of the entire planarian. Second, instead of relying on the conventional gelation incubation at 37 °C, we expedited gelation by exposing the samples to violet light for 30 s. Third, we conducted the procedure on ice to minimize the impact of high-temperature gelation. Last, we reduced or eliminated the time required for tissue clearing for smaller samples. It is important to point out that the strength of our C-MAP protocol lies in its fluorescence-protective nature and user convenience. Notably, the sample can be expanded up to 4.5-fold linearly without the need for heating or proteinase digestion, which helps preserve fluorescence signals. In addition, the entire expansion process can be completed within 48 hr. Based on our research requirement, two spatial resolutions were adopted to image expanded planarians, 2×2 × 5 μm3 and 0.5×0.5 × 1.6 μm3. The resolution can be further improved to 500 nm and 120 nm, respectively. The total hours required for expansion and imaging were summarized (Figure 1—figure supplement 1A). In the case of a 2 mm planarian, imaging at 2×2 × 5 μm3 spatial resolution requires approximately 1 hr with dual channel imaging. Imaging at 0.5×0.5 × 1.6 μm3 resolution requires about 12 hr. While our current analysis focused on cellular-level structures, our method can achieve a resolution of 0.5×0.5 × 1.6 µm3 and a spatial resolution of 0.12×0.12 × 0.4 µm3 with a 4.5×isotropic expansion, which is comparable to previously reported methods (Fan et al., 2021; Wang et al., 2016). The individual images were able to be conveniently integrated into a 3D tiff. file (Figure 1—figure supplement 1B). After all, we believe it is a practical pipeline to image planarians in 3D with high resolution within an acceptable time frame.

![Figure 1.](https://cdn.elifesciences.org/articles/101103/elife-101103-fig1-v1.jpg)

**Figure 1.:** (A) Planarian expansion workflow. Planarians were fixed and stained with FISH or immunostaining, followed by tissue expansion and tiling light sheet microscopy imaging. Created with Biorender. (B) Segmentation of PI and neuron pool riboprobes labeled cells in eyes, brain, and pharynx. Scale bar, 600 μm. (C) Staining of anti-Arrestin antibody for the planarian visual system. Scale bar, 600 μm. The lower image shows a magnification of the selected area in the upper image. Scale bar, 200 μm. (D) Neuron tracing of the upper image in panel C. (E) Tracing of single neurons in transverse view. Scale bar, 600 μm. (F) Traced axon projection trajectories from each eye. Scale bar, 600 μm. (G) Dual staining of glial cells (estrella+) and visual system (anti-Arrestin+) in the head region of a wild-type planarian. Scale bar, 350 μm. (H) Xz view of the image in panel G. (I) Zoom in of panel G shows the glial cells close to the visual axons. Scale bar, 100 μm. (J) Reconstruction of the glial and visual system. Scale bar, 100 μm. (K1) Anti-SYT staining in a wild-type planarian. Scale bar, 600 μm. (K2) The 3D reconstructed image of ganglia in the anterior tip of the brain. Scale bar, 120 μm. (K3) The 3D reconstructed image of ganglia in the branch region of the brain. Scale bar, 30 μm. (L1) Anti-Phospho (Ser/Thr) staining in a wild-type planarian. Scale bar, 600 μm. (L2) Single plane image of the brain. Scale bar, 150 μm. (L3) 3D reconstruction of brain region. Green represents the visual neurons, and yellow represents the brain. Scale bar, 180 μm.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/101103/elife-101103-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) Chart displaying the resolution and speed for imaging planarians of different sizes and at different developmental stages. (B) Selected xy slices of a 3D planarian labeled with PI of different z positions. Scale bar, 1000 μm. (C) Grayscale image of a single image plane at the brain region of a wild-type planarian head. Scale bar, 300 μm. (D) Segmented image with individual cells from the image of panel D. Scale bar, 300 μm. (E) Isolated epidermal cells of the whole planarian labeled with PI. Scale bar, 1000 μm. (F) Isolated epidermal cells of a selected region in (E). (G) Segmentation of epidermal cells in the image of panel F. Scale bar, 150 μm. (H)-(J) 3D display, grayscale, and cell segmentation of a pharynx. Segmented cells are assigned with different colors. Scale bar, 150 μm. (K)-(M) Selected single image planes from regions 1–3 in panel I. Green arrows represent the nucleus boundaries in grayscale images. (N)-(P) Segmentation of body cells in the images of panels K-M from the regions 1–3. White arrows represent segmented nucleus boundaries corresponding to the green arrows in K-M. Scale bar, 150 μm. (Q) Comparison of cell counting results with original grayscale fluorescent images slice by slice. Cells are delineated with green lines. Scale bar, 150 μm. (R and S) Comparison of max intensity projections of body cells (R) with 3D segmentation reconstruction (S) in a 1050 × 450 × 450 µm3 region. Scale bar, 120 μm. (T) The plot shows the validation of the cell segmentation through automatic workflow and manual counting across six 1050 × 450 µm2 regions. Differences are indicated.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/101103/elife-101103-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** (A) Distribution of cholinergic, serotonergic, GABAergic, dopaminergic, and octopaminergic neurons in wild-type planarians labeled with probes for chat, tph, gad, th, tbh, and their mixture (neuron pool). Scale bar, 600 μm. (B) FISH images (upper row) and segmentation (lower row) of cholinergic, serotonergic, GABAergic, dopaminergic, and octopaminergic neurons in the brain region. The unlabeled cells are in either the epidermis or non-brain regions. Scale bar, 900 μm. (C) Grayscale (upper row) and reconstruction (lower row) images of estrella+ glial cells. Scale bar, 120 μm.

We next set up the pipeline of 3D tissue reconstruction and cell segmentation for planarian CNS. To accurately count individual cells, we developed an automatic cell-counting pipeline to segment various planarian tissues and individual cells, including a plane section of the head, a layer of epidermis, and the whole organ of the pharynx (Figure 1—figure supplement 1C–P). This pipeline detects nucleus boundaries and assigns labels to each nucleus, thus facilitating accurate cell counting (Figure 1—figure supplement 1C–G, Q-T, Figure 1—video 1). Additionally, the neuron system of S. mediterranea is complex and characterized by considerable diversity among glutamatergic, glycinergic, and peptidergic neurons in planarians and many neurons in S. mediterranea express more than one neurotransmitter or neuropeptide, which adds further complexity to the system (Cebrià et al., 2002a; Collins et al., 2010; Fraguas et al., 2012; Ong et al., 2016; Rawls et al., 2009; Shimoyama et al., 2016; Vaaga et al., 2014; Wyss et al., 2022). We used five markers for a proof of concept illustration. By employing Fluorescence in Situ Hybridization (FISH), we successfully visualized a variety of planarian neurons, including cholinergic (chat+), serotonergic (tph+), octopaminergic (tbh+), GABAergic (gad+), and dopaminergic (th+) neurons based on their well-characterized roles in planarian neurobiology and the availability of reliable markers. (Figure 1—figure supplement 2A, Figure 1—video 2; Nishimura et al., 2007; Currie et al., 2016). The combination of these five types of neurons constitutes a neuron pool that enables the labeling of most of the neurons throughout the entire body, including the eyes, brain, and pharynx (Figure 1B). Segmentation of each neuron type showed their spatial atlas in the head (Figure 1—figure supplement 2B). Similarly, the estrella+ glial cells can be visualized and segmented (Figure 1—figure supplement 2C). The segmentation pipeline applied at 160 nm resolution at the single cell level was achieved for the nucleus and the cell body of neurons.

To visualize the neural network, we further stained the anti-Arrestin to image the visual projections (Figure 1C–E, Figure 1—video 3). We traced the trajectories of the photoreceptor axons, corroborating the existence of both ipsilateral and contralateral projections (Figure 1F; Okamoto et al., 2005). Photoreceptor axons displayed the trajectories to the contralateral or the ipsilateral side of the brain. Choice points were observed at the optic chiasm, consistent with the previous description (Agata et al., 1998; Okamoto et al., 2005; Scimone et al., 2020). Glial cells have been observed to be closely associated with neurons in the brain region (Wang et al., 2016; Roberts-Galbraith et al., 2016). Additionally, it has been reported that glial cells might assist in the projection of photoreceptors (Chandra et al., 2023). To validate these observations, we performed co-staining of anti-Arrestin and estrella (Figure 1G and H). Our results consistently showed a strong association between glial cells and the projections of photoreceptors in the brain region (Figure 1I and J). To visualize the neuronal network of the planarian, we used antibody staining with anti-SYT (Figure 1K; Tazaki et al., 1999) and anti-Phospho (Ser/Thr; Figure 1L), respectively. Both anti-SYT and anti-Phospho (Ser/Thr) staining effectively stained the planarian brain and ventral nerve cord (VNC), therefore facilitating the observation of the planarian neuron network. Above all, we developed a platform for digital documentation and exploration of planarian CNS structures.

### Cell counting reveals a potential threshold in the increase of neuron numbers during planarian growth

Our method allows for a comprehensive quantitative analysis of the cell number change. Planarians ranging in length from 1 mm to 10 mm were carefully selected during the homeostatic phase to model planarian growth (Figure 2A, Figure 2—figure supplement 1A). In total, 99 samples were analyzed for 3D tissue reconstruction and cell segmentation. Images of alive planarians were captured, and accurate length was measured. By dual staining of the neuron pool and propidium iodide (PI), 3D images of the planarians were analyzed to measure the volume, length, width, and depth of all planarians, and numbers of whole-body cells and neurons (Figure 2B and C). The volume and surface areas were quantified, revealing a consistent ratio of the square root of surface area to the cube root of volume during homeostasis (Figure 2—figure supplement 1B). The cell number-to-volume ratio remained stable in planarians during homeostasis (Figure 2—figure supplement 1C). Furthermore, brain volumes were measured, and brain volume increases proportionally with the growth of body length and volume (Figure 2—figure supplement 1D, E). Our results indicate the ability of planarians to flexibly regulate their cell number and scale of surface area relative to volume to adapt to the developmental changes during homeostasis.

![Figure 2.](https://cdn.elifesciences.org/articles/101103/elife-101103-fig2-v1.jpg)

**Figure 2.:** (A) Workflow of sample collection of homeostatic planarians. Scale bar, 500 μm. (B) 3D reconstruction of a planarian with PI staining. Length, volume, and surface area were measured using reconstructed images. The planarian brain is segmented and shown in a black dotted box. Scale bar, 2700 μm. (C) Representative fluorescent images of planarians stained with neuron pool riboprobes and PI at sizes of 2 mm, 4 mm, 6 mm, and 8 mm. Scale bar, 6000 μm. (D) Dot plot shows the correlation of whole-body cell number with neuron number in different sizes of intact planarians during homeostasis. Two trendlines are shown to represent planarians with differing cell counts. (E) Zoomed grayscale (PI) and segmented neurons (green) of selected brain regions of planarians at sizes of 2 mm, 4 mm, and 8 mm. Scale bar, 450 μm. (F) Correlation of total neuron number with neuron number in brains in different sizes of intact planarians. (G) Segmented images of octopaminergic neurons in the main brain region (blue) and brain branch region (red) of planarians with the indicated body length are shown with xy and yz views. Scale bar, 900 μm. (H) Dot plot shows the correlation of the total number of octopaminergic neurons with the octopaminergic neuron number in the brains (blue dots) and branches (red dots). (I) The plot illustrates the correlation between the angle of the brain lobe and the number of octopaminergic neurons in two groups of intact planarians: one with 80–160 octopaminergic neurons and the other with 160–220 octopaminergic neurons. n=8 in each condition. The data is shown as the mean ± SEM. Statistical significance was evaluated using the two-tailed unpaired Student’s t-test, with **p<0.01, ***p<0.001 indicating significance, while ns indicates lack of significance. (J) Segmented images of GABAergic neurons in the brains of planarians with the indicated body length are shown with xy and yz views. Scale bar, 900 μm. (K) Dot plot shows the correlation of the total number of GABAergic neurons with the GABAergic neuron number in the VM region (yellow dots) and DL region (green dots).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/101103/elife-101103-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) Representative live images of planarians ranging from 1 to 8 mm. Scale bar, 3500 μm. (B) Graph shows the correlation between the square root of surface area and the cube root of volume in homeostatic and regenerative planarians. (C) Graph shows the correlation between cell number and 3D volume in homeostatic planarians. (D) Graph shows the correlation between brain volume and body length in intact planarians. (E) Graph shows the correlation between brain volume and body volume in intact planarians. (F) Ratio of neuron cells relative to planarians measuring 2–6 mm and 7–9 mm in the 7–9 mm group. The data is shown as the mean ± SEM. n=17 in the 2–6 mm group and n=7 in the 7–9 mm group. Statistical significance was assessed by the two-tailed unpaired Student’s t-test: ***p<0.001. (G) Graph shows the correlation between GABAergic neuron number and total cell number. (H) Graph shows the correlation between octopaminergic neuron number and total cell number. (I) Graph shows the correlation between dopaminergic neuron number and total cell number. (J) Graph shows the correlation between serotonergic neuron number and total cell number.

Previous studies reported that body cells increase in number in correlation with planarian size growth through quantitative western blotting of worm lysates and image-based cell counting of dissociated worms (Baguñá and Romero, 1981; Thommen et al., 2019). In this study, we sought to validate this quantification at the single-cell level in intact planarians. We calculated the neuron numbers and cell numbers in planarians with different sizes, including neurons specifically located in the brain (Figure 2D–F). We observed a proportional increase in the total count of neuron cells with the overall size of the body, comprising approximately 10% of the total body cells when the length is shorter than 7 mm (Figure 2D). Dividing the planarians into 2–6 mm and 7–9 mm groups, we observed that the neuron number to cell number ratio is significantly higher in the 2–6 mm planarian group (Figure 2—figure supplement 1F). However, it is important to mention that the number of neurons in the brain exhibits a linear increase with overall neuron count (Figure 2F). Beyond this threshold, the proportion of neurons in the brain relative to the total cell population decreases (Figure 2D). Referring to the images, the decreased ratio in large planarians may be caused by the reduced density of neurons in the brain (Figure 2E). These findings provide evidence to support the previous prediction and consistency between different planarian species (Baguñá and Romero, 1981; Emili et al., 2023). Because the tail is proportionately longer in large than in small planarians, the allometric growth of the planarians can be one possibility for this decrease along with the increase in animal size. The phenomenon may also suggest the existence of a threshold in the increase of planarian neuron numbers, which may ultimately contribute to some physiological changes, such as planarian fission.

We further analyzed different neuron types to examine their correlation with the increase in body size. Within the five types of neurons, we noticed that GABAergic, serotonergic, dopaminergic, and octopaminergic neurons increase in linear to the total cell number (Figure 2—figure supplement 1G–J). These results suggest that the above observation of the non-linear dynamics between neuron and total cell number is not likely from the octopaminergic, GABAergic, dopaminergic, and serotonergic neurons. Since our neuron pool may not include glutamatergic, glycinergic, and peptidergic neurons, the non-linear dynamics may be from cholinergic neurons or other neurons not included in our staining. We further analyzed the octopaminergic neurons in the brain and branch regions (Figure 2G) and the GABAergic neurons in the ventral medial (VM) and the dorsal lateral (DL) regions (Figure 2J; Nishimura et al., 2008; Currie et al., 2016). By quantifying these two groups, we found that the number of octopaminergic neurons in the brain increased concurrently with the overall increase of octopaminergic neurons; in contrast, the number of octopaminergic neurons in the branch region did not show a noticeable increase (Figure 2H). To examine if the morphology of the brain changes according to the growth of the body size, our measurement showed that the range of the angle of the brain lobe remains stable around 17.12°–20.88° (Figure 2I). Similarly, the proportion of dorsal lateral GABAergic neurons increased relative to the total number of GABAergic neurons; in contrast, the increase rate of the VM region neurons was much higher than the rate of the DL region (Figure 2K). These findings indicate that octopaminergic and GABAergic neurons in different locations may be controlled by distinct mechanisms for their growth.

### Differential increase trends by neuron types during planarian regeneration

To comprehensively observe the dynamic changes of the neuron population during regeneration in S. med, an experiment was conducted using the tail fragments of 5–6 mm-long planarians by cutting their posterior tails into 2 mm fragments. Over a period of 14 days, daily fixation of planarian fragments was carried out. Four planarian fragments were analyzed at each time point (Figure 3A, Figure 3—figure supplement 1A). Similar to homeostasis, a consistent surface area-to-volume ratio was maintained in the regenerative processes (Figure 3B, Figure 3—figure supplement 1B). We further segmented the brain during regeneration and found that the brain size increased during the 14-day regeneration period (Figure 3—figure supplement 1C). To subsequently analyze each neuron type, probes such as chat, gad, tbh, tph, th, and PI were used to stain the regenerating fragments (Figure 3—figure supplement 1E). In total, 251 samples were analyzed for 3D tissue reconstruction and cell segmentation.

![Figure 3.](https://cdn.elifesciences.org/articles/101103/elife-101103-fig3-v1.jpg)

**Figure 3.:** (A) Workflow of sample collection of regenerative planarians. (B) Reconstructed 3D brains segmented from PI-labeled regenerative tail fragments at various time points post-amputation. Scale bar, 900 μm. (C) Representative xy views of segmented cholinergic neurons on 0-, 3-, 9-, and 14 days post-amputation. Scale bar, 1500 μm. (D) Dot plot shows the increase of cholinergic neurons (chat) at different time points after amputation. n≥3 in each condition. The data is shown as the mean ± SEM. (E) Dot plot shows the increase of serotonergic neurons (tph) at different time points after amputation. n≥3 in each condition. The data is shown as the mean ± SEM. (F) Dot plot shows the increase of GABAergic (gad), octopaminergic (tbh), and dopaminergic (th) neurons at different time points after amputation. n≥3 in each condition. The data is shown as the mean ± SEM. (G) Representative xy and yz views of segmented GABAergic neurons on 4, 6, 8, 10, 12, and 14 days post-amputation. Scale bar, 900 μm. (H) Dot plot shows the correlation of the total number of brain GABAergic neurons with the neuron number in the VM region (yellow dots) and DL region (green dots) in regenerative planarians. (I) Representative xy and yz views of segmented octopaminergic neurons on 3, 5, 6, 8, 10, 13 days post-amputation. Scale bar, 900 μm. (J) Correlation of the total number of the brain octopaminergic neurons with the octopaminergic neuron number in the brains (blue dots) and branches (red dots) in regenerative planarians. (K) Percentage of each type of neuron in the total cell number between 14 dpa planarians and the same size homeostatic planarians. n=3. Statistical significance was assessed by the two-tailed unpaired Student’s t-test: **p<0.01, ***p<0.001; ns, not significant.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/101103/elife-101103-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A) Live images of regenerative tail fragments from 0 to 14 days post-amputation (dpa). Scale bar, 3000 μm. (B) Graph shows the correlation between the square root of surface area and the cube root of volume in homeostatic and regenerative planarians. (C) Graph shows the correlation of brain volume with the regeneration time points. n≥3 in each condition. The data is shown as the mean ± SEM. (D) FISH images of regenerative tail fragments stained by probes for cholinergic, serotonergic, octopaminergic, GABAergic, and dopaminergic neurons at various time points post-amputation. Scale bar, 7500 μm. (E) Correlation of brain lobe angle with the octopaminergic neuron numbers in regenerative planarians (blue dots).

Previous studies have shown that the balance of cell numbers in planarians is influenced by cell proliferation, differentiation, and cell death during regeneration (Eisenhoffer et al., 2008; Takeda et al., 2009; Arnold et al., 2019; Oviedo et al., 2003; Hill and Petersen, 2015). Cell numbers were counted from 0 to 14 days post-amputation (dpa). Cholinergic and serotonergic neurons were present not only in the brain but also distributed across the body’s superficial layers (Figure 3C, Figure 3—figure supplement 1D). The count of cholinergic neurons initially started at ~7000 and continued to increase throughout the entire 14-day regeneration period (Figure 3D). For serotonergic neurons, they showed a similar pattern to cholinergic neurons (Figure 3E). GABAergic, octopaminergic, and dopaminergic neurons began to appear around days 3 and 4. Subsequently, the number of these neurons increased and reached a plateau after day 10 (Figure 3F, Figure 3—figure supplement 1D). It was reported that neurons exhibit an increase phase and plateau phase during planarian regeneration in Dugesia japonica (Takeda et al., 2009). Our results showed the similar pattern of neuron regrowth with two distinct phases, including an initial increasing phase (0–10 dpa) followed by a plateau phase (10–14 dpa).

Due to the linear and non-linear dynamics between neuron number and cell number in homeostatic growth, we further examined the dynamics of cell growth during regeneration. The GABAergic neurons in the VM and DL regions showed patterning on 4 dpa (Figure 3G). The growth of DL and VM GABAergic neurons occurs proportionally during regeneration, in which the DL GABAergic neurons increase faster than the VM GABAergic neurons (Figure 3H). In contrast, the octopaminergic neurons in the brain and branch regions began to appear on 3 dpa (Figure 3I). Similarly, the number of octopaminergic neurons in the brain region increases proportionally, while those in the branch region continue to increase until reaching a number approximately from 15 to 20 neurons at 13 or 14 dpa (Figure 3J). Moreover, the angle of octopaminergic neurons in the brain decreased during regeneration and stabilized at 20°, which remained consistent during homeostasis (Figure 3—figure supplement 1E, Figure 2I). These findings suggest that the reconstruction of DL, VM, branch, and main brain regions in planarians initiates concomitantly with the appearance of GABAergic and octopaminergic neurons. We further compared the ratio of different neuron types between planarians of the same body size at 14 dpa and in homeostasis. Our analysis revealed that the ratio of cholinergic and serotonergic neurons remained relatively constant in homeostasis. Conversely, the ratio of GABAergic, octopaminergic, and dopaminergic neurons is significantly lower in regeneration than in homeostatic planarians (Figure 3K). Different populations of neurons exhibit diverse growth patterns during the process of regeneration (Takeda et al., 2009). Our results provided additional evidence, obtained through comprehensive analyses of entire animals at the single-cellular level and in greater sample sizes, to support the model that proposes distinctive growth patterns for different populations of neurons during regeneration.

### Fine network of planarian musculature and distinct intersections at head-tail poles

Motivated by the crucial function of muscle in regeneration and the need to comprehend the control of movement by the neuromuscular system, we investigated the interaction between the neuronal and muscular systems. Initially, we examined the distribution of musculature in planarians. The 6G10 antibody was used to visualize the distribution of muscles throughout the planarian (Ross et al., 2015; Cebrià, 2016; Cote et al., 2019). Consequently, we validated that the body-wall musculature of adult planarians is composed of four layers of fibers, including circular, diagonal, longitudinal, dorsal-ventral (DV), and intestinal muscle fibers from the outmost to the innermost (Figure 4A, Figure 4—figure supplement 1A-D and J, Figure 4—video 1).

![Figure 4.](https://cdn.elifesciences.org/articles/101103/elife-101103-fig4-v1.jpg)

**Figure 4.:** (A) Illustration of the major five muscle fibers in wild-type planarians according to their orientation and distribution. A: anterior; P: posterior; D: dorsal; V: ventral. (B) Segmented fibers of planarian body-wall muscle. Scale bar, 200 μm. (C) Schematic depicting selected segmented areas of planarian body-wall muscle, with a chart depicting the number of different orientational fibers in those regions. d: dorsal region; v: ventral region. The data is shown as the mean ± SEM. n≥3. Statistical significance was evaluated using the two-tailed unpaired Student’s t-test, with *p<0.05, **p<0.01, ***p<0.001 indicating significance, while ns indicates lack of significance. (D) Planarian dorsal body-wall muscle fiber labeled with 6G10 antibody staining, with segmented circular (green), diagonal (blue), longitudinal (yellow), and D-V fibers (purple). Scale bar, 150 μm. (E) An xz view of the image in panel D. Scale bar, 150 μm. (F) Selected 100 μm depth region showing DV fiber (White arrows) located around diagonal fibers. Scale bar, 80 μm. (G) Body-wall muscle fiber of a region in the image of panel F. Segmented D-V fibers are shown in a tracked line. Scale bar, 50 μm. (H) An xz view of the segmented D-V fiber and its connecting fibers in panels F and G. Scale bar, 50 μm. (I) Xz projection of planarian anterior and posterior muscle fiber and their segmented muscle fibers in control planarian. Scale bar, 300 μm. (J) Xz projection of planarian anterior and posterior muscle fiber and their segmented muscle fibers in β-catenin-1 RNAi planarian. Scale bar, 300 μm.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/101103/elife-101103-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A) Planarian body-wall muscles labeled with the antibody 6G10. Scale bar, 1200 μm. (B) Magnification image of selected region (left) in panel A. Scale bar, 210 μm. (C) Projection of planarian dorsal epidermis muscle. Scale bar, 150 μm. (D) Projection of planarian ventral epidermis muscle. Scale bar, 150 μm. (E) Magnification image of the ventral region. Scale bar, 40 μm. (F) Segmented DV muscle fibers. Scale bar, 40 μm. (G) Segmented DV muscle fibers and ventral muscle fibers. Scale bar, 40 μm. (H) A cartoon illustration depicting planarians' intestines and eyes. The selected ROI is shown upright as the grayscale of the xy projection. (I) Max projection intensity of planarian eye and intestine region indicated in panel H. Scale bar, 1150 μm. (J) Selected segmented region of the indicated area in panel I. (K) The xy projection of pharynx muscle fibers. Scale bar, 150 μm. (L) Muscle fiber of 150 μm depth projection of pharynx at the dorsal plane. Scale bar, 150 μm. (M) Yz view of a 300 μm depth of planarian pharynx region. Scale bar, 90 μm. (N) Segmented muscle fiber of the connecting DV fibers and pharynx fibers in panel N. Scale bar, 90 μm. (O1) Illustration of muscle fiber regeneration process at 0, 2, and 4 days post-amputation (dpa). (O2) Xz view of blastema region with staining of neurons and muscles on 0, 2, and 4 dpa. Scale bar, 150 μm. (O3) Segmentation of single muscle fiber on 0, 2, 4 dpa. (P1) Staining of 6G10, neuron pool, and DAPI of planarian at 0 dpa. Xz view of the blastema is shown. Scale bar, 150 μm. 1 represents the xy view of the yellow dotted box in panel P1, and 2 represents the single slice of panel P1. Scale bar, 75 μm. (P2) Staining of 6G10, neuron pool, and DAPI of planarian at 2 dpa. Xz view of the blastema is shown. Scale bar, 150 μm. 1 represents the xy view of the yellow dotted box in panel P2, and 2 represents the single slice of panel P2. Scale bar, 75 μm. (P3) Staining of 6G10, neuron pool, and DAPI of planarian at 4 dpa. Xz view of the blastema is shown. Scale bar, 150 μm. 1 represents the xy view of the yellow dotted box in panel P3, and 2 represents the single slice of panel P3. Scale bar, 75 μm.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/101103/elife-101103-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** (A–C) Magnification images of three regions showing the muscle fibers. (D–F) Segmented muscle fibers corresponding to images of A-C. Scale bar, 60 μm. (G) Merged image of the original and segmented muscle fibers in A-F. Red boxes indicate the ROI for A-D, B-E, and C-F, respectively. Scale bar, 100 μm.

With our higher-resolution images, we conducted segmentation to gain a better understanding of the organization and orientation of the muscle fibers (Figure 4B-H, Figure 4—figure supplement 1E-G, J, N). A ground truth comparison of our automated muscle fiber segmentation with the original image was conducted to show the consistency (Figure 4—figure supplement 2). The planarian primarily relies on the movement of its cilia, which are mainly located on the ventral surface of the body (Rink et al., 2009). By closely examining the fiber structure, it becomes apparent that the circular muscle fibers dominate in all directions of the dorsal muscle wall (Figure 4C). However, the ventral body-wall muscles contain diagonal and longitudinal fibers at the tail region (Figure 4C). In contrast, the proportion of these fibers decreases in the dorsal muscle wall (Figure 4C). DV fibers are shorter compared with fibers in other orientations (Figure 4F, Figure 4—figure supplement 1E-G). We observe that these DV fibers have close contact with diagonal and longitudinal fibers (Figure 4G, H, Figure 4—figure supplement 1G, M, N).

Internal organs, such as the eyes and intestine, consist of a sophisticated distribution of muscle fibers (Scimone et al., 2020). We were able to visualize the intricate musculature in these organs with a resolution of 120 nm. The eyes of planarians contain short, sparsely distributed muscle fibers (Figure 4—figure supplement 1H–J, Figure 4—video 2). The pharynx, which serves as the feeding organ, is a muscular tube characterized by external and internal monostratified epithelia (Figure 4—figure supplement 1K, L). The intestine muscle fibers are located around the intestine, which are short and connected with small muscle fibers (Figure 4—figure supplement 1H–J). Furthermore, we investigated the connection between the dorsal epidermis and pharynx. We found that DV muscle fibers extend from the diagonal and circular layers of the dorsal body-wall muscles and connect with the longitudinal fibers of the pharynx (Figure 4—figure supplement 1M, N, Figure 4—video 3). These observations suggest that the planarian musculature is an interconnected unit, with the internal tissue muscles connected to the external body-wall muscles. It is noted that previous studies reported that 6G10 does not label all body wall muscles equivalently with the limitation of predominantly labeling circular and diagonal fibers (Scimone et al., 2017; Ross et al., 2015). Our observation may be limited by this preference.

Through the 3D tissue reconstruction method, we validated that the dorsal and ventral muscle fibers combine with circular muscle fibers, resembling a cobweb-like structure in the anterior pole (Cebrià, 2016; Li et al., 2019). Moreover, we observed that the integration of the ventral and dorsal body wall muscles differs in the anterior and posterior regions of the body. In the posterior region, the dorsal and ventral muscle walls integrate differently with longitudinal muscle fibers (Figure 4I, Figure 4—videos 4 and 5). It raised the possibility of whether the different morphologies are related to the A-P polarity. We thus examined the muscle structure at both the anterior and posterior heads of β-catenin-1 RNAi planarians. Both the anterior and posterior muscle fibers of β-catenin-1 RNAi planarians resemble the cobweb-like structure (Figure 4J). These detailed structures suggest a correlation between muscle structure and the establishment of the anterior-posterior axis. The results highlight a noticeable contrast between the muscle fiber patterning of head and tail regions in terms of their responses to targets and adjustments in body posture. Unlike the tail, which doesn't need to react as actively, the head requires rapid reactions and precise posture changes. This is reflected in the more intricate muscle fiber arrangements observed in the head, suggesting a greater requirement for neural control.

#### Neural-muscular connection in planarian homeostasis and regeneration

We next observed the interaction between neuronal and muscular networks. The estrella+ glial cells are widespread (Figure 5A1–A3), and the glial cells extend from the planarian CNS to the body-wall muscle fibers (Figure 5A4 and A5). On closer examination of the epidermis region, we observed a tight association between glial cells and muscle fibers (Figure 5 1-3, Figure 5—video 1). We further investigated the neuronal and muscular connection through dual staining of 6G10 antibody (muscles) and anti-Phospho (Ser/Thr; Figure 5B1–B3) or anti-SYT (neurons) (Figure 5C1 and C2). Both dual-labeling revealed that neural cells are closely associated with muscle fibers with their projections (Figure 5B4–B6 and C3–C5).

![Figure 5.](https://cdn.elifesciences.org/articles/101103/elife-101103-fig5-v1.jpg)

**Figure 5.:** (A1) Dual staining for glial cells (estrella+) and muscles (6G10+) in a wild-type planarian. The representative brain region of xy is shown. (A2) Dual staining for glial cells (estrella+) and muscles (6G10+) in a wild-type planarian. The representative brain region of xz is shown. (A3) Dual staining for glial cells (estrella+) and muscles (6G10+) in a wild-type planarian. The representative brain region of yz is shown. Scale bar, 600 μm. (A4) A single slice of glial cells (estrella+) and muscles (6G10+) close to the epidermis of the anterior pole is shown. The arrowhead indicates the interaction of glial cells (estrella+) and muscles (6G10+). Scale bar, 250 μm. (A5) A single slice of glial cells (estrella+) and muscles (6G10+) close to the epidermis of the posterior pole is shown. The arrowhead indicates the interaction of glial cells (estrella+) and muscles (6G10+). Scale bar, 250 μm. (1-3) Zoomed in white dotted box region in A1 showing the estrella+ glial projection to the muscles. Scale bar, 150 μm. (B1) Dual staining for CNS (Anti-Phospho (Ser/Thr) staining) and muscles (6G10+) in a wild-type planarian. Scale bar, 600 μm. (B2) Single slice of anti-Phospho (Ser/Thr) and 6G10 expression around planarian’s eye. Scale bar, 300 μm. (B3) Magnification of selected region in panel B2. Scale bar, 200 μm. (B4) Single slice of Anti-Phospho (Ser/Thr) and 6G10 staining in a brain region. Scale bar, 200 μm. (B5) Volume rendering of selected region in panel B4. (B6) Reconstruction of B5. Scale bar, 60 μm. (C1) Dual staining for CNS (anti-SYT staining) and muscles (6G10+) in a wild-type planarian. Scale bar, 600 μm. (C2) Single slice of Anti-SYT and 6G10 staining in brain region. Scale bar, 600 μm. (C3) Single slice of Anti-SYT and 6G10 staining close to the epidermis in the middle part of the body. Scale bar, 450 μm. (C4) Single slice of Anti-SYT and 6G10 staining close to the epidermis in the anterior part of the body. Scale bar, 450 μm. (C5) Single slice of Anti-SYT and 6G10 staining close to the epidermis in the anterior part of the body. Scale bar, 450 μm.

In the context of planarian regeneration, the expression of positional control genes (PCGs) by muscles is vital for orchestrating the complex process of tissue regrowth (Scimone et al., 2017). During the regeneration process, DV muscle fibers reconnect at the wound site, with longitudinal fibers and other muscle types gradually restoring the structure at the anterior tip and later integrating with circular and diagonal fibers through small DV fiber branches (Figure 4—figure supplement 1O1-O3). By visualizing the dual-staining of cholinergic neurons and muscle fibers, we can observe that cholinergic neurons are closely located to muscle fibers from day 0 (Figure 4—figure supplement 1P1). We found that the appearance of newly regenerated diagonal and circular muscle fibers is located closely with cholinergic neurons (Figure 4—figure supplement 1P2, P3). These results suggest that the newly formed muscle fibers organize and connect potentially with a strong correlation with CNS.

#### Muscular infrastructure may support as a scaffold for the neuron projection

To further investigate the functional relationship between neuronal and muscular networks, we utilized previously reported gene RNAi strategy (Roberts-Galbraith, 2022) that are likely to impact the structures of muscle. Insulin may influence the proper signaling of skeletal muscles and neoblasts (Miller and Newmark, 2012; Lei et al., 2016; Sylow et al., 2021). Inr-1 RNAi animals exhibited locomotion defects (Lei et al., 2016) and also displayed a higher length-to-width ratio compared to control animals (Figure 6—figure supplement 1A, Figure 6—video 1), suggesting possible neuromuscular system abnormalities. The body wall muscle fiber distribution in inr-1 RNAi and β-catenin-1 RNAi planarians differs from egfp RNAi planarians (Figure 6A and B). By calculating the concentration of different orientations of muscle fibers in inr-1 RNAi and β-catenin-1 RNAi planarians in a 500×250 × 300 μm3 region (Figure 6C), we noticed that inr-1 RNAi planarian has more circular fibers in both dorsal and ventral regions; β-catenin-1 RNAi planarian has more longitudinal fibers in dorsal regions (Figure 6C).

![Figure 6.](https://cdn.elifesciences.org/articles/101103/elife-101103-fig6-v1.jpg)

**Figure 6.:** (A) Representative images of dorsal and ventral muscle in egfp RNAi, inr-1 RNAi, and β-catenin-1 RNAi planarians. Scale bar, 120 μm. (B) Images depicting enhanced muscle fibers within dorsal and ventral regions of egfp RNAi, inr-1 RNAi, and β-catenin-1 RNAi planarian. Scale bar, 40 μm. (C) Schematic depicting selected segmented areas of planarian body-wall muscle in DV view. The plot shows the proportion of circular, longitudinal, and diagonal fibers in ventral and dorsal body muscle wall in egfp RNAi, inr-1 RNAi, and β-catenin-1 RNAi planarians. The data is shown as the mean ± SEM. n=3. Statistical significance was evaluated using the two-tailed unpaired Student’s t-test, with *p<0.05, **p<0.01, ***p<0.001 indicating significance, while ns indicates lack of significance. (D) Illustration of egfp RNAi, inr-1 RNAi, and β-catenin-1 RNAi planarian glial cell structure and its connection with muscle fibers. (E) Anti-Phospho (Ser/Thr) and 6G10 staining and its reconstructed data in selected regions of egfp RNAi, inr-1 RNAi, and β-catenin-1 RNAi planarians (left). The estrella+ glia and 6G10+ muscles and their reconstructed images in selected regions of egfp RNAi, inr-1 RNAi, and β-catenin-1 RNAi planarians (right). Scale bar, 150 μm.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/101103/elife-101103-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** (A) Length and width measurements of live egfp RNAi and inr-1 RNAi planarians. (B) Cholinergic, dopaminergic, octopaminergic, serotonergic, and GABAergic neuron labeling of egfp RNAi and inr-1 RNAi planarians. Scale bar, 450 μm (egfp RNAi) and 450 μm (inr-1 RNAi). (C) Representative images of estrella+ glial cells in egfp RNAi and inr-1 RNAi planarian. Scale bar, 400 μm. Magnifications in brain region and selected slices. Scale bars, 180 μm (up), 60 μm (down). (D) 6G10 staining in inr-1 RNAi planarian. Selected dorsal (left) and ventral (right) regions in white dotted line boxes are shown in magnification. Scale bars, 500 μm (left), 200 μm (middle and right). (E) Dual-staining of estrella and 6G10 in egfp RNAi (up) and inr-1 RNAi (down) planarians. Head regions are shown. Scale bar, 300 μm. (F) A representative region in egfp RNAi (up) and inr-1 RNAi (down) planarians with dual-staining of estrella and 6G10. (G) Single channel of estrella+ glia in egfp RNAi (up) and inr-1 RNAi (down) planarians shown in panel F. (H) Single channel of 6G10+ muscles in egfp RNAi (up) and inr-1 RNAi (down) planarians shown in panel F. Scale bar, 150 μm. (I) Xy view of isolated glial cell in egfp RNAi (up) and inr-1 RNAi (down) planarians. (J) Xz view of isolated glial cell in egfp RNAi (up) and inr-1 RNAi (down) planarians. Scale bar, 80 μm. (K) Segmented isolated glial cell in egfp RNAi (up) and inr-1 RNAi (down) planarians. Scale bar, 120 μm.

Furthermore, an examination of sub-cellular neuronal expression is conducted using FISH labeling to identify cholinergic, dopaminergic, serotonergic, octopaminergic, GABAergic neurons, and glial cells (Figure 6—figure supplement 1B, C). Inr-1 RNAi planarians manifested fewer cholinergic neurons and less glial branching in the brain region (Figure 6—figure supplement 1B, C). The distribution of GABAergic neurons was disordered in inr-1 RNAi planarians (Figure 6—figure supplement 1B). Enhancement of muscle fibers revealed a substantial increase in the concentration of circular muscle fibers in both the ventral and dorsal regions (Figure 6A-C, Figure 6—figure supplement 1D). These results imply that the decreased presence of neurons and unusual arrangement of fibers with varying orientations within the body muscle wall may lead to locomotion impairments in inr-1 RNAi planarians.

Considering the interaction between glial and muscle cells, the localization of estrella+ glial and muscle fibers is further investigated. By dual-staining of anti-Phospho (Ser/Thr) and 6G10 in inr-1 RNAi and β-catenin-1 RNAi planarians, we found that the morphologies of neurons are normal, and they have close contact with muscle fibers (Figure 6D and E). However, by dual staining of estrella and 6G10, we found that the structure of glial cells is star-shaped in egfp RNAi planarian, however, glial cells in inr-1 RNAi and β-catenin-1 RNAi planarians have shorter cytoplasmic projections, and their sizes are smaller, lacking the major projection onto the muscles (Figure 6D, E, Figure 6—figure supplement 1E-K). Especially, in the posterior head of β-catenin-1 RNAi planarians, the glial cell has few processes and can hardly connect with muscle fibers (Figure 6E). These results indicated that proper neuronal guidance and muscle fiber distribution could potentially contribute to facilitating accurate glial-to-muscle projections. Further investigation is required to distinguish the cell-autonomous and non-autonomous effects of inr-1 RNAi and β-catenin-1 RNAi on muscle and glial cells.

## Discussion

In this study, we employed TLSM and C-MAP to investigate the spatial organization in planarians at the single-cell level. This combination offers several key advantages over standard techniques. For example, it enables high-throughput imaging across entire organisms with a level of detail and speed that is not easily achieved using confocal methods. This approach allows us to investigate the planarian nervous system at multiple developmental and regenerative stages in a more comprehensive manner, capturing large-scale structures while preserving fine cellular details. The ability to rapidly image whole planarians in 3D with this resolution provides a more efficient workflow for studying complex biological processes. Above all, our findings provide valuable insights into the cellular composition and neuronal diversity of planarians, shedding light on their regenerative capabilities and the interactions between muscle fibers and neurons during the regeneration process. One of the key observations in our study was the development of a robust segmentation method that allowed for the accurate identification and characterization of individual cells throughout the planarian body. This segmentation method, combined with the application of tissue expansion techniques, provided an accessible approach to obtaining high-resolution spatial information and enabled us to obtain a comprehensive view of the cellular landscape. Through the application of a 3D tissue reconstruction method, we investigated the development and diversity of various neuron types, including cholinergic, GABAergic, octopaminergic, dopaminergic, and serotonergic neurons, at the single-cell level. In addition, we pay attention to the neural networks of the planarian visual system, and we validated that there are contralateral axon projections onto the brain with single axon tracing results. It should be noted that the current resolution for our segmentation may be limited when resolving fibers within densely packed regions of the nerve tracts. Our analysis unveiled the intricate distribution of neurons throughout the planarian nervous system, encompassing regions such as the brain, ventral nerve cords, optic, and pharyngeal nerve complex.

Notably, as the planarian’s body size increased, we observed that all neuron subtypes exhibited growth alongside the body cells, consistent with previous reports (Takeda et al., 2009; Arnold et al., 2019; Oviedo et al., 2003). Multiple approaches were used and validated to study the planarian cell changes (Thommen et al., 2019; Oviedo et al., 2003; Hill and Petersen, 2015). It is worth noticing that until reaching a threshold, beyond which the proportion of neurons decreases. This intriguing observation suggests a correlation with planarian fission, where the reduction in neuron proportion may be associated with the division of the planarian into two separate individuals. Our findings suggest that different neuron populations have coinciding regeneration speeds, and even the same neuron population may separate into different regeneration groups. Further investigations into the molecular and cellular mechanisms underlying this phenomenon would provide deeper insights into the factors governing planarian fission and the regenerative capacities of these organisms.

An important aspect of our study was the exploration of the interaction between muscle fibers and neurons during the regeneration process. By examining the structure, location, and regeneration of muscle fibers, as well as their connections to cholinergic neurons and glial cells labeled with estrella, we discovered a close correlation between ventral muscle fibers in the inner epidermal layer and cholinergic neurons and glial cytoplasmic projections. This finding suggests that muscle may play a crucial role in guiding the regeneration of the planarian nervous system, laying the foundation for future investigations into the neuron and muscle regeneration dynamics. Furthermore, 3D tissue imaging offers several advantages for clinical research and the medical industry by enhancing diagnostic accuracy through improved spatial resolution. Notably, techniques such as light sheet microscopy and tissue clearing have shown their utility in visualizing human tissues, as well as mouse tissues and various other model animals (Chung et al., 2013; Liebmann et al., 2016; Liu et al., 2016). The integration of two modalities, TLSM and C-MAP, allows for effective 3D imaging with a resolution range of 120 nm to 500 nm. We envision opportunities to expand our efforts to include additional research organisms, such as axolotls, hydra, and frogs, thereby broadening the scope of our research.

In conclusion, our study utilizing TLSM and C-MAP expansion techniques provides a comprehensive understanding of planarian spatial organization and cellular dynamics at the single-cell level. The development of a robust segmentation method, combined with the analysis of various neuron types and their relationship with muscle fibers, highlights the intricate interactions between different cell populations during planarian regeneration. These findings significantly contribute to our knowledge of regenerative biology and provide a foundation for future studies to understand similar processes in other organisms. Further investigations into the functional significance of the observed cellular dynamics and interactions will undoubtedly advance our understanding of planarian biology and regenerative mechanisms.

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
      <td>Strain, strain background (Schmidtea mediterranea)</td>
      <td>Schmidtea mediterranea, asexual</td>
      <td>CIW4</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>DH5a</td>
      <td>SangonBiotech</td>
      <td>B528413</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>HT115</td>
      <td>Sangon Biotech</td>
      <td>A338983</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Digoxigenin (DIG)-POD, sheep polyclonal</td>
      <td>Roche</td>
      <td>11207733910</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Fluorescein-POD, sheep polyclonal</td>
      <td>Roche</td>
      <td>11426346910</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>6G10, mouse monoclonal</td>
      <td>DSHB</td>
      <td>6G10-2C7</td>
      <td>IF(1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Arrestin, rabbit polyclonal</td>
      <td>Gift from Takeshi Inuoe</td>
      <td></td>
      <td>IF(1:500),</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-SYT, rabbit polyclonal</td>
      <td>Gift from Takeshi Inuoe</td>
      <td></td>
      <td>IF(1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Phospho (Ser/Thr) Phe antibody,, rabbit polyclonal</td>
      <td>CST</td>
      <td>9631 S</td>
      <td>IF(1:1000)</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>urea</td>
      <td>SangonBiotech</td>
      <td>A600148</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>N-butyl diethanolamine</td>
      <td>TCL chemicals</td>
      <td>#B0725</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Triton X-100</td>
      <td>SIGMA</td>
      <td>T8787-250ml</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Tween20</td>
      <td>SIGMA</td>
      <td>P9416-100ml</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>methanol</td>
      <td>SCR</td>
      <td>80080418</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Acrylamide</td>
      <td>Sangon Biotech</td>
      <td>A100341</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>N,N-Dimethylacrylamide</td>
      <td>SigmaAldrich</td>
      <td>M7279</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Sodium acrylate</td>
      <td>Macklin</td>
      <td>S833838</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>2,2'-Azobis[2-(2-imidazolin-2-yl) propane] dihydrochloride (VA-044)</td>
      <td>Rhawn</td>
      <td>R008695</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Formaldehyde</td>
      <td>SIGMA</td>
      <td>F8775</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Heparin</td>
      <td>SIGMA</td>
      <td>H3149</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Torula Yeast RNA</td>
      <td>SIGMA</td>
      <td>R6625</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Western Blocking Reagent</td>
      <td>Roche</td>
      <td>11921681001</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Horse Serum</td>
      <td>hyclone</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Dextran Sulfate</td>
      <td>Sangon Biotech</td>
      <td>A600160</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Maleic acid</td>
      <td>aladdin</td>
      <td>M108866</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>NAC</td>
      <td>SIGMA</td>
      <td>A7250</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>DAPI</td>
      <td>Thermo Fisher Scientific</td>
      <td>D3306</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>DIG RNA Labeling Mix</td>
      <td>Roche</td>
      <td>11277073910</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Fluorescein RNA Labeling Mix</td>
      <td>Roche</td>
      <td>11685619910</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>DNase (RQ1 rnase free DNase)</td>
      <td>Promaga</td>
      <td>PAM 6101</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Phusion High-Fidelity DNA Polymerase</td>
      <td>NEB</td>
      <td>M0530L</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>T7 RNA Polymerase</td>
      <td>Promega</td>
      <td>P207E</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay kit</td>
      <td>MicroSpin G-50 Columns</td>
      <td>Cytiva</td>
      <td>27533002</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay kit</td>
      <td>StarPrep Gel Extraction Kit</td>
      <td>GenStar</td>
      <td>D205-04</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay kit</td>
      <td>FsatPure Plasmid Mini Kit</td>
      <td>Vazyme</td>
      <td>DC201-01</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Amira 3D</td>
      <td>Thermo Fisher Scientific</td>
      <td></td>
      <td>v2023</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>hybridization oven</td>
      <td>xingfen</td>
      <td>FYY-3</td>
      <td>equipment</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Thermocycler</td>
      <td>Analytik Jena</td>
      <td>Biometra TRIO 48</td>
      <td>equipment</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Microscope Cameras</td>
      <td>Leica</td>
      <td>DFC7000 T</td>
      <td>equipment</td>
    </tr>
  </tbody>
</table>

### Planarian culture and amputation

Schmidtea mediterranea clonal asexual strain CIW4 animals were maintained in 1×Montjuïc salts (1.6  mmol/L NaCl, 1.0  mmol/L CaCl2, 1.0  mmol/L MgSO4, 0.1  mmol/L MgCl2, 0.1  mmol/L KCl and 1.2  mmol/L NaHCO3 prepared in Milli-Q water) at 20 °C as previously described (Cebrià and Newmark, 2005), and were fed with liver paste every 3 days. Intact animals (1–14 mm in length) were starved for at least 7 days before each experiment. The worms (5–6 mm long) were amputated into two sections: anterior fragment (including pharynx) and tail.

### In situ hybridization and immunostaining

Fluorescence in situ hybridization was performed as previously described (Pearson et al., 2009; King and Newmark, 2013). Intact and regeneration samples were treated with reduction solution (1% v/v NP-40, 0.5% w/v SDS, and 50 mM DTT in 1×PBS) for 10  min at 37  °C, except for worms within 3 days post-amputation, and all samples were bleach with Ryan King’s Bleach (5% Formamide, 1.2% H2O2 in 0.5×SSC) for 2 hr. Riboprobes were synthesized as previously described (King and Newmark, 2013). The primers are as follows: Smed-chat (SMED30031525) forward primer 5’-CTTTGGCACTTCCGATAAAC-3’, reverse primer 5’-CCATTTCTGTTGTCGATTGG-3’; Smed-gad (SMED30001003) forward primer 5’-TATCAAAATAGGTCAGGGCC-3’, reverse primer 5’-AAACGCCGCCATCTAATTTC-3’; Smed-tbh (SMED30017498) forward primer 5’-TTGGTCTGTTGAACCGAATC-3’, reverse primer 5’-AATCTCCCTCAAAAGAGTCG-3’; Smed-th (SMED30012000) forward primer 5’-CACCAGTCAGAATTTCATCG-3’, reverse primer 5’-TATCATGAAAACCCGGATGG-3’; Smed-tph (SMED30012020) forward primer 5’-ACCAGACGAGGAAGATTTTC-3’, reverse primer 5’-GCAAGACCAGCTAAAAAGTC-3’; Smed-estrella (KY024338.1) forward primer 5’-CAAATGCTGAGAATACTGGC-3’, reverse primer 5’-TCGGAGTAAGCATCGTTTAG-3’. Animals were incubated with probes labeled with DIG (1:500) for more than 18 hr at 56 °C. Anti-DIG-POD 1:1000 (Roche) was used in MABT containing 5% Horse Serum and 0.5% Roche Western Blocking Reagent. The antibody 6G10 (1:1000, DSHB) was used in PBSTB (PBSTx 0.1%+ 1% Bovine Serum Albumin [Jackson Immuno Research Laboratories]) for FISH. For anti-DIG-POD labeling, samples were incubated overnight at 4 °C and then developed with FITC-conjugated tyramide (1:2000) in borate buffer containing 0.006% H2O2 for 1 hr at room temperature. For dual staining with antibodies, the worms were overnight incubated at 4 °C with 6G10 (1:1000), followed by incubation with the secondary antibody Goat Anti-mouse IgG H&L (HRP) pre-adsorbed (1:1000 in PBSTx0.3%, Abcam) on the following day. Subsequently, the worms were incubated with rhodamine-tyramide (1:5000) in borate buffer containing 0.006% H2O2 for 1 hr on the third day. The same procedure was repeated for the additional antibody staining, including anti-Arrestin (rabbit, 1:500), anti-SYT (rabbit, 1:1100), and anti-Phospho (Ser/Thr) (rabbit, 1:1000).

### Tissue clearing for planarians

Tissue clearing was performed following the CUBIC protocol (Matsumoto et al., 2019), with specific optimizations for the planarian sample. The tissue-clearing solution consisted of 15% urea, 10% N-butyl diethanolamine, 10% Triton X-100, and 65% deionized water (ddH2O). The specimens were immersed in this solution and gently shaken at either room temperature or 37 °C.

The duration of tissue clearing varied depending on the size and starvation state of the planarians, ranging from 30 min to overnight. It is worth noting that excessively long tissue clearing can compromise the integrity of planarian tissues. Starved planarians measuring 2–3 mm should skip the tissue-clearing step and proceed directly to the expansion procedure. Conversely, tail fragments that have been amputated from a 6 mm planarian require the tissue-clearing step.

For planarians of different sizes and developmental stages, the tissue clearing time should be adjusted based on their starvation status. An extended period of starvation allows for a reduction in tissue clearing time.

### C-MAP for planarians

The planarian specimen should be washed with 0.01 M PBS for 30 min at room temperature, with gentle shaking to ensure thorough clearance. To prepare the monomer solution, the final concentrations of the components should be as follows: 30% Acrylamide (AA), 0.075% N, N-Dimethylacrylamide (BA), 10% Sodium acrylate (SA), and 0.5% 2,2'-Azobis[2-(2-imidazolin-2-yl)propane] dihydrochloride (VA-044) in 0.01 M PBS. It is important to store the monomer solution at 4 °C and use it within 7 days.

Next, the planarian specimen should be immersed in the monomer solution for 30 min at 4 °C. The length of monomer incubation may vary depending on the size of the planarians, ranging from 30 min to overnight. For planarian of 2 mm length, the monomer incubation time is 30 min.

To perform the gelation step, it is necessary to work on ice. To create a double-layer gel that prevents direct contact between the specimen and the mold surface, start by adding 200 µL of the monomer solution onto the cap of a 1.5 mL Eppendorf (EP) tube on ice. Make sure that no sample is included in this first layer. The polymerization is initiated by exposing the gel to ultraviolet (UV) light for approximately 5 s, resulting in the formation of a coagulated gel with a tacky surface for support.

Afterward, carefully pipette the planarian specimen and 250 µL of monomer solution onto the first gel layer. This second layer should be solidified using UV light for 30 s, with the light source positioned 15 cm away from the sample. It is important not to use UV light to check the sample’s position until it is properly placed in the mold. Once the specimen is embedded in the gel, separate the gel containing the specimen from the EP tube cap using tweezers and transfer it to ddH2O in a 10 cm Corning cell culture plate. The specimen should be stored at room temperature for 2 days, with the ddH2O changed after overnight incubation. Gentle shaking can be applied to expedite the expansion process.

To further increase the expansion ratio, the monomer solution should have the following final concentrations: 30% Acrylamide (AA), 0.05% N, N-Dimethylacrylamide (BA), 10% Sodium acrylate (SA), and 0.5% 2,2'-Azobis[2-(2-imidazolin-2-yl)propane] dihydrochloride (VA-044) in 0.01 M PBS.

### Labeling of planarian nuclei

After an overnight expansion, the gel underwent a twofold increase in size. To achieve accurate results, carefully use a blade accompanied by an illuminating light to precisely section the gel. These incisions should be in accordance with the contour of the planarian specimen, resulting in a cuboid shape. Subsequently, immerse the trimmed gel once again in fresh ddH2O supplemented with 0.50 μg/mL of Propidium Iodide (PI) for nuclei staining at room temperature with gentle shaking. Stain the planarian overnight and wash the sample with ddH2O for 10 min before imaging.

### Sample mounting

The planarian specimen, which had been embedded within the gel, was carefully trimmed with a blade to achieve a flat bottom surface. Following this, the gel was affixed onto a thin magnet using adhesive glue. The magnet’s dimensions were modifiable to align with the sample’s proportions. Lastly, the gel-magnet assembly was secured onto a designated sample holder prepared for imaging.

### Imaging

The configuration and operational details of the microscope were described in earlier publications (Chen et al., 2020; Feng et al., 2021). Employing distinct arrangements of light sheet configuration and detective objectives, the expanded planarian specimen was subjected to imaging for specific experiment purposes. The planarians labeled with nuclei and neuron pool were imaged with OLYMPUS MV PLAPO 1×objective with micron-scale spatial resolution. The planarians labeled with 6G10 and estrella were imaged with OLYMPUS 10×0.6 SV MP to achieve sub-micron spatial resolution. The resolution can be up to ~70 × 70 × 210 nm3 with this combination of objective and tilling light sheets. The image processing, registration, and merging procedure was described in detail in a previous publication (Chen et al., 2020).

### Resolution calculation

For cellular resolution imaging, we utilized a 1×air objective with a numerical aperture (NA) of 0.25 and a working distance of 60 mm (OLYMPUS MV PLAPO). The voxel size used was 0.8×0.8 × 2.5 µm3. This configuration resulted in a resolution of 2×2 × 5 µm3 and a spatial resolution of 0.5×0.5 × 1.25 µm3 with 4×isotropic expansion. Alternatively, for sub-cellular imaging, we employed a 10×0.6 SV MP water immersion objective with 0.8 NA and a working distance of 8 mm (OLYMPUS). The voxel size used in this configuration was 0.26×0.26 × 0.8 µm3. As a result of this configuration, we achieved a resolution of 0.5×0.5 × 1.6 µm3 and a spatial resolution of 0.12×0.12 × 0.4 µm3 with a 4.5×isotropic expansion.

### RNAi interference

egfp, without nucleotide sequence homology in planarians, was used as control RNAi. Animals were fed 1–6 times bacterially colored food (90% liver, 5.5% water containing 1×Montjuïc salts with 4.5% red food coloring)-expressed egfp, smed-inr-1, and β-catenin-1 double-stranded RNA, once every 3 days. Animals were fixed 7 days after the last feeding.

### Nuclei quantification

The cellular quantification workflow was developed using the Amira 3D software environment (https://www.thermofisher.com/software-em-3d-vis/customerportal/download-center/amira-avizo-3d-installers/). A recipe and an example for nuclei counting can be assessed from https://zenodo.org/records/11724834. This recipe is designed for the segmentation of planarian nuclei-labeled images. The image analysis modules in the recipe provide flexibility for users to interactively check results at each step. Modules such as interactive thresholding and structure enhancement filters are designated as check breakpoints for parameter adjustment. The workflow consists of the following steps:

#### Neuron quantification

The recipe of neuron counting and an example can be freely accessed from https://zenodo.org/records/11724834. The workflow used for quantifying neurons closely resembled that of nuclei quantification, with two important considerations. First, due to the sparser distribution of neurons compared to somatic cells, the overall neuron data can be analyzed without the need to distinguish between the brain and other regions. Second, adjustments were made to the minimum and maximum parameters of the structure enhancement function standard deviation based on the staining size of the neuronal markers. The workflow can be broken down into the following steps.

### Measurement of planarian length and volume

The recipe and an example of measuring volumetric parameters can be freely accessed from https://zenodo.org/records/11724834. The workflow can be broken down into the following steps.

### Neuron tracing

Single anti-Arrestin labelled neuron tracing analysis was conducted with Amira 3D filament editor. Initially, 10–50 single-layer images were selected for maximum intensity projection display, based on their grayscale signals. Next, we identified and selected the axons to be tracked by determining their starting and ending points. Subsequently, layers were selected for display using the maximum intensity projection method. This approach facilitated the segmental tracking of the main axon, as well as the identification of branching points, thereby enabling the comprehensive tracking of neural fibers in 3D. Following the completion of the fiber tracking, we conducted a validation process to assess the accuracy of the traced fibers by comparing them with the original single-layer images. This validation was performed in multiple directions, with different branches of the fibers displayed in distinct colors.

To render the anti-SYT, anti-Phospho (Ser/Thr), estrella, and anti-Arrestin labeled data, we utilized Amira 3D segmentation editor. First, the datasets were transformed from grayscale to binary using interactive thresholding. Subsequently, the mis-segmented areas were evaluated and corrected using either the brush tool or the lasso tool. Lastly, the data was displayed using either volume rendering or the surface module generation method.

### Muscle fiber tracing

The muscle fiber tracing workflow was developed using Amira 3D. The data and project file related to muscle fiber tracing can be freely accessed from https://zenodo.org/records/11724834. The workflow can be broken down into the following steps.

### Statistical analyses

Microsoft Excel and Prism 9 were used for statistical analysis. The data in all graphs are shown as the mean ± SEM. An unpaired two-tailed Student’s t-test was used to determine the significance of differences between the two conditions. Differences for which p<0.05 were considered statistically significant.
