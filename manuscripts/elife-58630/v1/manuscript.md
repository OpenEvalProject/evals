# The Drosophila Individual Activity Monitoring and Detection System (DIAMonDS)

## Authors

- Ki-Hyeon Seong<sup>1</sup> ([ORCID: 0000-0002-0606-8896](https://orcid.org/0000-0002-0606-8896)) †
- Taishi Matsumura<sup>3</sup>
- Yuko Shimada-Niwa<sup>2</sup> ([ORCID: 0000-0001-5757-4329](https://orcid.org/0000-0001-5757-4329))
- Ryusuke Niwa<sup>2</sup> ([ORCID: 0000-0002-1716-455X](https://orcid.org/0000-0002-1716-455X))
- Siu Kang<sup>2</sup> †

### Affiliations

1. RIKEN Cluster for Pioneering Research, RIKEN Tsukuba Institute Tsukuba Japan
2. AMED-CREST, AMED Tokyo Japan
3. Graduate School of Science and Engineering, Yamagata University, Jonan Yonezawa Japan
4. Life Science Center for Survival Dynamics, University of Tsukuba Tsukuba Japan

† Corresponding author

## Abstract

Here, we have developed DIAMonDS (Drosophila Individual Activity Monitoring and Detection System) comprising time-lapse imaging by a charge-coupled device (CCD) flatbed scanner and Sapphire, a novel algorithm and web application. DIAMonDS automatically and sequentially identified the transition time points of multiple life cycle events such as pupariation, eclosion, and death in individual flies at high temporal resolution and on a large scale. DIAMonDS performed simultaneous multiple scans to measure individual deaths (≤1152 flies per scanner) and pupariation and eclosion timings (≤288 flies per scanner) under various chemical exposures, environmental conditions, and genetic backgrounds. DIAMonDS correctly identified 74–85% of the pupariation and eclosion events and ~ 92% of the death events within ± 10 scanning frames. This system is a powerful tool for studying the influences of genetic and environmental factors on fruit flies and efficient, high-throughput genetic and chemical screening in drug discovery.

## Introduction

Animal life develops through a sequence of characteristic events and stages. Embryogenesis starts with the fertilization of an egg. Thence, the embryo transitions to the juvenile stage at a certain time point. This stage persists for a certain period, during which the animal grows and develops into the adult stage in which it reproduces, senesces, and dies. The length of each stage and the timing of each developmental transition are determined by complex interactions between genetic and environmental factors. Thus, developmental timing may be defined as a phenotype. Accurate determination of developmental timing helps elucidate the molecular and physiological bases of biological events and may uncover new factors regulating development and lifespan.

Nevertheless, it is difficult to establish the precise time points of the developmental transitions in many animals including humans. One reason is that there may be no clear boundaries between stages throughout the entire lifetime of the organism. Consequently, it has been impractical to use developmental timing as a phenotype for investigations in developmental biology. However, holometabolous insects such as the fruit fly Drosophila melanogaster are important exceptions to this rule. These animals pass through four life stages, namely embryo, larva, pupa, and adult. Transitions between these stages are accompanied by drastic morphological events and behavioral changes including hatching, pupariation, eclosion, and death. Therefore, the time point of each developmental transition can be precisely determined. Drosophila has been extensively studied in the fields of genetics and developmental biology. Accurate tracking and recording of its life cycle could significantly promote the understanding of various aspects of biology, agriculture, and medicine.

Noteworthy, no recent improvements have been made in measuring the timing of the developmental transitions in Drosophila. Until now, the timing of each developmental stage was manually determined by counting the number of flies at each stage in each vial over 2, 6, 12, or 24 hr (Buhler et al., 2018; Demay et al., 2014; Külshammer et al., 2015; Nikhil et al., 2016; Yun et al., 2017); however, this technique has certain limitations. Increasing the temporal resolution is difficult as it would require intensive labor, preventing the detection of subtle changes in transition timing for each event. Moreover, manual counting is neither practicable for large-scale/high-throughput screening nor feasible for identifying multiple phenotypes in individual flies in transition events. In contrast, it does help elucidate the associations between developmental stages and the genetic and environmental factors affecting them. Recent studies reported the use of video cameras to measure developmental timing (Hironaka et al., 2019). However, this method is labor-intensive, requires long analytical periods, and is unsuitable for high-throughput analysis.

Here, we present a new scalable method that automatically determines multiple transition time points, such as pupariation, eclosion, and death, of individual fruit flies implementing a basic flatbed CCD scanner. We placed a single fly in each well of a 96- or 384-well microplate, acquired time-lapse images, and analyzed the output with our novel algorithm Sapphire. This system performs automatic developmental analyses at high temporal resolution and could be used in high-throughput gene and chemical screening and analyses of the effects of genetic and environmental factors on development.

## Results

### Design of the Drosophila Individual Activity Monitoring and Detection System (DIAMonDS)

Drosophila develops through four developmental stages (embryo, larva, pupa, and adult), subsequently finishing its own life. The static phases (embryo, pupa, and death) alternate with the dynamic phases (larva and adult; Figure 1A). Single-image processing between continuous images distinguishes both phases: dynamic phases are detected as positive signals while static phases simultaneously present no signal (Figure 1B). Therefore, we can precisely identify the transition points between phases by monitoring the static and dynamic status and separately detecting fly phases on all plates captured simultaneously in the same image.

![Figure 1.](https://cdn.elifesciences.org/articles/58630/elife-58630-fig1-v1.jpg)

**Figure 1.:** (A) Diagram of developmental stages and activity states in Drosophila melanogaster. (B) Schematic representation of the DIAMonDS procedure. DIAMonDS consists of: (i) microplate preparation; (ii) time-lapse imaging with CCD scanner; and (iii) data analysis by Sapphire. In step (iii), Sapphire calculates activity signal (green line) intensity via animal body detection from FCN images and subtraction processing of every two consecutive images and then determines the CF signal (purple line) from the activity signal. (C) Flowchart of Sapphire. Algorithm includes extraction of individual animals from population images (Step 1), training data preparation and augmentation (Step 2), training through data and animal body segmentation (Step 3), segmentation data signaling by subtracting labeled data and transition point detection algorithm (Step 4), event detection, signal processing, and visualization (Step 5).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/58630/elife-58630-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) Temperature measurement points on scan surface. Temperature measured by temperature data logger (Thermochron SL type, NK Labs, Cambridge, MA, USA) in high-resolution mode. (B) Daily temperature time course under 12:12 light-dark cycle. (C,D) Temperature at each time point under light (C) and dark (D) conditions. Dark and light green bands represent mean and maximum/minimum temperature ranges, respectively.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/58630/elife-58630-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** (A) Automatic life event detection algorithm. Detailed procedure described in Figure 1C. (B) Schematic architecture of fully convolutional network (FCN) designed for animal body segmentation.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/58630/elife-58630-fig1-figsupp3-v1.jpg)

**Figure 1—figure supplement 3.:** (A) Under the tab 'Main', appropriate datasets, detection methods, and inference data may be selected. We can also confirm and select well images and segmented areas of two consecutive images. We may confirm the result of Sapphire analysis on the selected well (upper left graph) and change ‘signal type,’ ‘smoothing,’ and ‘weight.’ We can compare data analyzed by Sapphire with those detected manually (lower panels). (B) In tab 'Data Table', we can download the timestamp and analyzed data.

DIAMonDS consists of an automated time-lapse imaging system and our novel image analysis software named ‘Sapphire’ (Figure 1B). We used a combination of a flatbed CCD scanner and VueScan software (https://www.hamrick.com), which enables multiple scanner units to capture images continuously at certain intervals (Smith et al., 2014). To identify the phase change time points for each fly event, single flies are inserted into each well of a 96- or 384-well microplate containing suitable fly media. Up to three microplates are then set on the scanner surface, and time-lapse images are acquired at appropriate intervals until the fly event is completed. A single scanner can monitor 288 or 1152 individuals in three 96-well or 384-well microplates, respectively for DIAMonDS. Because the well-size of 384-well microplate is too small to succeed in normal development and lifespan, we only use the 384-well microplate for measuring adult survivorships in the short term (within about 2 weeks) such as stress or drug resistance assays. Sapphire then automatically analyzes and detects the transition points of pupariation, eclosion, and death in the newly acquired time-lapse images (Figure 1B,C). Our system can simultaneously monitor multiple scanners with a single personal computer.

As positional bias and fluctuations in environmental factors such as ambient temperature and relative humidity (RH) might markedly reduce the reliability of our system, all experiments were conducted in a plant growth chamber (LPH-410NS) with automatic temperature and humidity regulation and additional USB fans (Appendix 6). The scan surface temperature was continuously recorded with button-sized temperature data loggers (NK Labs LLC, Cambridge, MA, USA). Temperatures widely varied among locations under external illumination on/off conditions possibly because of irregular and uneven irradiation. Thus, we acquired time-lapse images without external illumination to maintain a steady temperature (Figure 1—figure supplement 1).

### DIAMonDS software: Sapphire

Sapphire automatically determines the static-to-dynamic and dynamic-to-static phase changes for all flies according to the time-lapse images acquired by the aforementioned scanner system. The following four processes were implemented in Sapphire to enable automatic life event detection based on individual Drosophila images (Figure 1C):

The annotation data were manually created for larval and adult Drosophila and increased by general data augmentation techniques such as vertical and horizontal flips, rotation, and luminance modulation (Materials and methods).

After training with augmented data, the segmentation inference was calculated as a probability. If it was > 0.5, the system regarded it as the target region (animal body). If it was < 0.5, the system treated it as background. Consequently, the system obtained binary images wherein the animal body corresponded to one and the background was described as 0. Semantic segmentation was applied to all individuals and every sequential population image.

All trainings and inferences were performed on a Linux PC (Ubuntu) with four GPUs (GTX 1080Ti). All scripts were written in Python using the deep learning libraries keras (v. 2.0.9) and tensorflow-gpu (v. 1.4.0).

![Video 1.](https://cdn.elifesciences.org/articles/58630/elife-58630-video1.mp4.jpg)

### Pupariation and eclosion timing detection by DIAMonDS

Apparent dynamic-to-static and vice-versa phase changes occur at pupariation and eclosion (Figure 2A). We attempted to detect individual fly pupariation and eclosion with DIAMonDS to validate it. Newly hatched first-instar (L1) larvae were placed into 96-well microplates containing 100 µL well−1 standard fly media (Figure 2—figure supplement 1). Three microplates were fixed to the scanner surface, and the scanner was placed inverted in the incubator to prevent fly media leakage. The scanner was powered on, and time-lapse scanning was performed with VueScan (Materials and methods) until all flies eclosed. Thence, time-lapse images were analyzed with Sapphire (Figure 2A,B).

![Figure 2.](https://cdn.elifesciences.org/articles/58630/elife-58630-fig2-v1.jpg)

**Figure 2.:** (A) Schematic representation of pupariation and eclosion. Drastic changes in dynamic-to-static and static-to-dynamic states occur at pupariation and eclosion, respectively. At late L3, larval activity increases and transitions from feeding to wandering behavior. Dotted circles indicate animal bodies. (B) Time-lapse imaging was conducted until all flies eclosed into adults. Individual pupariation and eclosion transition points were separately analyzed in Sapphire. Wandering L3 larva showing high activity immediately before pupariation. (C,D) Scatterplot analyses comparing data for pupariation (C) and eclosion (D) obtained by Sapphire and visual handling to validate accuracy. (E–G) Scatterplot between pupariation and eclosion timing of individual flies (E) and box plots of pupariation (F) and eclosion (G) timing in males (n = 122; green dots) and females (n = 118; magenta dots). Whiskers indicate minima and maxima (***p<0.001; n.s., no significant difference; unpaired t-test).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/58630/elife-58630-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) Percent survival at each developmental stage (1 st instar (L1) larva, pupa, and adult stages) when a single embryo or L1 larva is installed in each well of a 96-well microplate. Averages with s.d. are shown (n = 6 each; ***p<0.001; **p<0.01; n.s., no significant difference; Student’s unpaired t-test). (B) Percent survival at each developmental stage (3rd instar (L3) larva, pupa, and adult stages) in 100 or 150 μL medium/well. Averages with s.d. are shown (n = 6 each;; ***p<0.001; n.s., no significant difference; Student’s unpaired t-test).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/58630/elife-58630-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** (A) Residual plots of pupariation corresponding to Figure 2C. (B) Residual plots of eclosion corresponding to Figure 2D.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/58630/elife-58630-fig2-figsupp3-v1.jpg)

**Figure 2—figure supplement 3.:** (A–D) Scatterplot and residual plot of eclosion timing between Sapphire (CF method: A and B; TH method: C and D) and visual handling of the same image data. Here, we transferred P14 stage pupae to new microplates once during time-lapse image acquisition.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/58630/elife-58630-fig2-figsupp4-v1.jpg)

**Figure 2—figure supplement 4.:** (A) Image of plates used for pupariation and eclosion time-lapse acquisition in DIAMonDS. (B–D) Box plots of pupariation (B), eclosion (C), and pupal duration (D) in male (green dots) and female (magenta dots) flies. Number of flies analyzed is indicated in parentheses on each graph. Whiskers indicate minima and maxima (***p<0.001; **p<0.01; n.s., no significant difference; Student’s unpaired t-test).

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/58630/elife-58630-fig2-figsupp5-v1.jpg)

**Figure 2—figure supplement 5.:** (A–C) Box plots of pupariation (A), eclosion (B), and pupal duration (C) in male flies. Number of flies analyzed is indicated in parentheses on each graph. Whiskers indicate minima and maxima (***p<0.001; **p<0.01; n.s., no significant difference; one-way ANOVA followed by Dunnett’s multiple comparison test).

The L1 larvae dove into the media until mid-L3 (~2 d). As time-lapse scanning could not detect larval movements here, this so-called feeding stage was designated as static. In contrast, the larvae typically left the media and moved around the well surface during late L3 (Figure 2A). This so-called wandering stage was designated as dynamic, as there were consecutive high-activity wandering larval signals (Figure 2B), and its duration was 12–24 hr. Thereafter, L3 larval activity gradually decreased, and pupariation followed. During the pupal stage (~100 hr), the activity was not detected in a static phase. The second signal wave activity was detected just after dynamic eclosion.

Sapphire independently and automatically detects maximum peaks at the pupariation and eclosion transition points using machine learning based on an FCN to detect larval and adult animals separately (Figures 1C and 2B). To verify Sapphire's accuracy, we compared pupariation and eclosion timings analyzed by Sapphire and those manually detected (visual handling) from the same images. The Sapphire and visual handling values were nearly identical (Figure 2C,D), 73.8% on pupariation and 84.2% on eclosion were only a slight difference within ± 10 frames between them (Figure 2—figure supplement 2). Film surface contamination after long-term rearing in small wells might have accounted for the observed decrease in Sapphire detection accuracy. Therefore, to investigate whether Sapphire's detection accuracy improves in a more transparent state of the lid, flies were transferred to the new microplate just after the time that all flies pupated (P14 stage) and scanned time-lapse scanning of the plates. The experiment resulted in 94.7% of values from Sapphire showed nearly identical (within ± 10 frames) to visual handling values, indicating that Sapphire's accuracy was greatly improved relative to the experimental setup in which the same microplate was used both for pupariation and eclosion detections (Figure 2—figure supplement 3A,B).

Arbitral image sequences such as raw images and the segmentation images could be analyzed in Sapphire (see Appendix 8). Sapphire calculates the CF signal obtained from the subtraction of consecutive segmentation images as fully automated method (CF method). Sapphire determined the timing of life-event by applying just thresholding on the arbitral time series data specified by user (TH method). At first, threshold is automatically calculated as an average of maximum and minimum value of the signal (auto-TH) and the threshold is modifiable by hands depending on user’s demand (manual-TH). Accuracy of CF method and auto- and manual- TH method on raw image subtraction was quantified in (Appendix 8). We compared CF and TH using the same time-lapse image set (Figure 2—figure supplement 3). The output of CF was superior to that of TH, as the former is relatively more sensitive to phase shifts. Thus, Sapphire is functional and highly invaluable in automatic analyses.

The relationship between pupariation and eclosion determined by DIAMonDS clearly revealed sexual dimorphism during development (Figure 2E). On average, females eclosed 4 hr earlier than males. A previous study corroborated this observation (Bainbridge and Bownes, 1981). The pupariation transition time points did not differ between sexes. Therefore, sexual dimorphism in the eclosion time points reflects the difference in pupal duration between sexes (Figure 2E–G). No significant differences were found between plates 1 and 3 used here, indicating a minimal scan surface positional effect in DIAMonDS during the detection of the pupariation and eclosion time points (Figure 2—figure supplement 4). Altogether, these results indicate that DIAMonDS is suitable for automatic measurement of both the pupariation and eclosion time points at high temporal resolution.

To understand the effect of chamber size on fly development, we used three different sizes of microplates (96-well, 48-well, and 24-well) contained normal fly media for measuring pupariation and eclosion. We observed that timings of pupariation and eclosion were slightly but significantly shorten both in the 48-well and 24-well conditions and the pupal duration might have the fewer effects of well-size, suggesting that the chamber size might affect fly’s development (Figure 2—figure supplement 5).

### DIAMonDS enables autonomic measurement of pupariation and eclosion timing at high temporal resolution for each individual

DIAMonDS showed excellent performance in large-scale pupariation timing analyses (Figure 3—figure supplement 1). To evaluate its performance, we explored whether two distinct genetic and environmental conditions affect larval development. First, we used larvae with delayed pupariation at 29°C (genotype: R29H01-GAL4 > UAS TeTxLC), in which tetanus toxin light chain (TeTxLC) impaired serotonergic SE0PG neuron activity (Shimada-Niwa and Niwa, 2014). To evaluate the influences of initial larval age on DIAMonDS measurement accuracy, we used L2, early L3, and late L3 larvae in the microplate assays. DIAMonDS successfully detected pupariation delays in larvae of all ages (Figure 3A). Thus, DIAMonDS performance remains highly stable over a wide range of conditions.

![Figure 3.](https://cdn.elifesciences.org/articles/58630/elife-58630-fig3-v1.jpg)

**Figure 3.:** (A) Box plot analysis of pupariation timing in flies with impaired ecdysteroid biosynthesis at 29°C (genotype: R29H01 > TeTxLC; R29H01>+ as a control). Larval age (L2, early L3, and late L3) at start of measurement had negligible impact on DIAMonDS analysis accuracy. Y-axis indicates pupariation timing from start of experiment. Number of flies analyzed indicated in parentheses on the graph. Whiskers indicate minima and maxima (*p<0.05; **p<0.01; ***p<0.001; n.s., no significant difference; multiple t-test). (B) Three 96-well microplates were subdivided into nine regions according to sucrose concentration (0.15–1 M) in media used for DIAMonDS. (C) Scatterplot between pupariation and eclosion timing in males and females. (D–F) Box plots of pupariation timing (D), eclosion timing (E), and pupal duration (F). Whiskers indicate minima and maxima (*p<0.05; **p<0.01; ***p<0.001; n.s., no significant difference vs. standard diet group; one-way ANOVA followed by Dunnett’s multiple comparison test). Number of flies analyzed indicated in parentheses on the graph.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/58630/elife-58630-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A,B) Scatterplot (A) and residual plot (B) between Sapphire (CF method) and manual analysis (n = 850).

We also used DIAMonDS to clarify the relationship between sugar concentration and development in the w1118 fruit fly strain (Figure 3B–F). A previous report stated that Drosophila larvae that were administered a high-sugar diet presented a type 2 diabetes-like phenotype and developmental delay (Musselman et al., 2011). L1 larvae were placed in wells containing normal to high-sugar concentrations, scanned by time-lapse imaging, and the pupariation and eclosion time points were detected by Sapphire. Both pupariation and eclosion were gradually delayed in a sugar concentration-dependent manner. Therefore, excess sugar adversely affects larval growth (Figure 3B–E). When we compared the pupariation and eclosion time points among individual larvae, the pupal durations were nearly constant regardless of sugar concentration. Thus, the sugar concentration determines the time spent as a larva until pupariation, but it does not influence the time spent as a pupa (Figure 3F). Interestingly, Northrop reported that prolongation of the pre-imago stage of D. melanogaster by yeast supplementation had no impact on pupal stage duration (Northrop, 1917a; Northrop, 1917b). The process by which pupal duration is determined may be independent of larval dietary intake. Overall, DIAMonDS is a powerful toolkit for detecting the pupariation and eclosion time points and discloses the effects of several endogenous and exogenous factors on individual fly development.

### Detection of individual adult death events by DIAMonDS

Adult death time points can be measured at high temporal resolution with DIAMonDS. This tool efficiently detects sudden shifts from a dynamic to a static phase. Depending on the objective, experiments are performed over a broad range of time scales extending to nearly 3 months. Small- and large-scale impact assessment targets may include mutant phenotype, environmental stress, and chemicals and drugs (Afschar et al., 2016; Harshman et al., 1999; Lin et al., 1998; Parkes et al., 1998; Piper and Partridge, 2016; Tsuda et al., 2010; Ziehm et al., 2015). DIAMonDS may be implemented using 96- and 384-well microplates to accommodate various parameters in death timing detection. The 96-well type is used in long-term detection, whereas the 384-well plate is better suited for short-term (≤10 d) detection and high-throughput assays.

We collected time-lapse scanning images at 1 min intervals for adult flies (4 day post-eclosion) maintained under starvation conditions (70 µL 1% agar/water (w/v)/well) in order to optimize DIAMonDS for 384-well microplates (Figure 4A). After the image data series consisted of dying individual flies, death time points were determined manually (visual manipulation) and by Sapphire. Both procedures generated nearly identical survival curves and were highly correlated (R = 0.9913), indicating the reliability of Sapphire (Figure 4A–D and Figure 4—figure supplement 1). Next, we examined whether the well positions within a microplate influence the death time points. No significant differences were found between each plate or among the sub-areas within each plate (Figure 4E and Figure 4—figure supplement 2). We also evaluated adult w1118 fly starvation tolerance in 96-well microplates and obtained results similar to those acquired from 384-well microplates (Figure 4F). Next, we tried to test whether the DIAMonDS can effectively detect the death time points even in flies showed a very reduced amount of activity. As a hypoactive fly model, we used decapitated females who keep motor skills but hardly moved until their death (Ejima and Griffith, 2008). DIAMonDS showed relatively good results that were comparable to the visual results although there was a tendency for the accuracy to reduce slightly in comparison with the case of wild-type flies (Figure 4—figure supplement 3). Altogether, these results indicate that DIAMonDS is highly effective at detecting fruit fly death events.

![Figure 4.](https://cdn.elifesciences.org/articles/58630/elife-58630-fig4-v1.jpg)

**Figure 4.:** (A) A 384-well microplate with flies prepared for DIAMonDS. (B) Survivorship curves in starvation condition plotted by Sapphire (red line) or visual handling (blue line) using the same data. (C,D) Scatterplot and residual plot analysis comparing Sapphire (CF method) and visual handling to validate accuracy (n = 382). (E,F) Survivorship curves for starvation resistance tests on adult male w1118 flies using three 384- (E) and three 96-well (F) microplates. Number of flies analyzed indicated in parentheses in each plate.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/58630/elife-58630-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A,B) Scatterplot (A) and residual plot (B) between Sapphire (TH method) and manual analysis (visual handling) to validate accuracy (n = 382). Results corresponding to Figure 4C,D.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/58630/elife-58630-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** (A–C) Box plots subdivided in the same dataset are shown as images on the left side of graphs. (n.s., no significant difference; Student’s unpaired t-test). Image of plates used to detect death timing in DIAMonDS. Number of flies analyzed indicated in parentheses on the graph.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/58630/elife-58630-fig4-figsupp3-v1.jpg)

**Figure 4—figure supplement 3.:** (A,B) Scatterplot (A) and residual plot (B) between Sapphire (CF method) and manual analysis (n = 45). (C) Survivorship curves. Red and blue lines indicate results determined by Sapphire (CF method) and visual handling, respectively (n = 45).

### DIAMonDS performs stress resistance assays with high temporal resolution

To assess the efficacy of DIAMonDS at evaluating fly survival under various stress conditions, we performed a starvation assay on male and female w1118 flies (Figure 5A). They presented sexual dimorphism in terms of starvation resistance. Moreover, the temporal resolution used here (15 min intervals) was higher than those reported in previous studies (Figure 5B and Figure 5—figure supplement 1A,B; Grönke et al., 2010; Li et al., 2018).

![Figure 5.](https://cdn.elifesciences.org/articles/58630/elife-58630-fig5-v1.jpg)

**Figure 5.:** (A,B) Starvation tolerance test using male and female w1118 flies (n = 192 each). Rows of males and females were alternately arranged in 384-well microplate (A). Representative male and female survivorship curves (B). (C,D) DDT resistance test on male w1118 flies (n = 48 each). A 384-well microplate with YS media containing DDT concentration series (0–0.1%). Forty-eight male flies were exposed to each concentration and subjected to DIAMonDS (C). Survivorship curves show concentration-dependent toxic effects of DDT (D). (E,F) Paraquat resistance test on male mth1 and w1118 flies (n = 32 each). A 384-well microplate containing media with paraquat (0, 5, 10, and 20 mM). Rows of mth1 and w1118 flies were alternately arranged in wells (E). Survivorship curves for mth1 mutants (solid lines) and w1118 flies (dotted lines) substantially differed at all paraquat concentrations (F).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/58630/elife-58630-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (A,B) Results corresponding to Figure 5A,B. (C,D) Results corresponding to Figure 5C,D. (A,C) Survivorship curves. Solid and dotted lines indicate results determined by CF and TH methods, respectively. (B,D) Example of analysis by Sapphire using TH and CF methods.

We then subjected the flies to various concentrations of dichlorodiphenyltrichloroethane (DDT) to identify possible resistance (Figure 5C,D; Afschar et al., 2016). To a 384-well microplate, we added media consisting of 5% (w/v) sucrose and 0.5% (w/v) yeast as described in Appendix 1. The 48 w1118 males in each well were exposed to 0, 0.005, 0.01, 0.05, or 0.1% DDT (Figure 5C). DIAMonDS showed distinct variance in DDT resistance even between only slightly differing DDT concentrations (Figure 5D and Figure 5—figure supplement 1C,D).

We also investigated whether DIAMonDS can detect mutant fly phenotypes in stress resistance assays. Flies with the loss-of-function mutation methuselah (mth) present extended lifespan and resistance to several stressors including paraquat (Lin et al., 1998). To test whether DIAMonDS can discriminate mth1 mutant stress tolerance phenotypes, we backcrossed the mth1 mutant five times with w1118 and compared the responses of both types of males to different paraquat concentrations (Figure 5E,F). The mth1 mutant presented significantly greater resistance to several paraquat concentrations than w1118. The results of this assay demonstrated that paraquat resistance could be detected in the mth1 mutant using lower paraquat concentrations than those tested in an earlier study (20 mM)(Lin et al., 1998). Thus, DIAMonDS can readily identify optimal concentrations at high temporal resolution in drug resistance assays.

### Sequential detection of multiple life events (pupariation, eclosion, and lifespan) using DIAMonDS

DIAMonDS successfully measured lifespans for individual w1118 flies. For long-term analysis, flies must be transferred to new microplates. We performed sequential pupariation, eclosion, and lifespan measurements for individual w1118 as shown in Figure 6A–C. The mean lifespans calculated and survival curves plotted for individual males and females were consistent with those of previous reports (Figure 6C; Liu et al., 2009; Schriner et al., 2014; Suh et al., 2008; Trostnikov et al., 2019).

![Figure 6.](https://cdn.elifesciences.org/articles/58630/elife-58630-fig6-v1.jpg)

**Figure 6.:** (A) Schematic diagram showing detection of pupariation, eclosion, and death transition points for each individual in DIAMonDS. (B) Scatterplot between pupariation and eclosion timing for individual female (n = 59) and male (n = 75) flies. (C) Survivorship curves for adult female (n = 59) and male (n = 75) flies. (D–I) Pearson’s correlation scatter plots indicate relationships between larval and pupal duration (D,G), between larval duration and adult lifespan (E,H), and between pupal duration and adult lifespan (F,I). Data are separately presented for female (D–F, n = 59 each) and male (G–I, n = 75 each) flies.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/58630/elife-58630-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** (A–C) Box plots of adult percent survival at 1 st, 2nd, 3rd, and 4th weeks in w1118 (A), Oregon-R (B), and Canton-S (C) male flies. Flies were reared in several plate well sizes (96-well, 48-well, and 24-well) and transferred to appropriate new plates every week or 2–3 days cycles. Twenty-four flies were selected randomly from each well of microplate and calculated percent survival at each time point. Whiskers indicate minima and maxima (***p<0.001; **p<0.01; *p<0.05; n.s., no significant difference; one-way ANOVA followed by Dunnett’s multiple comparison test, n = 6 each).

Several studies described the relationships between developmental time and adult lifespan among various species (Marchionni et al., 2020). Certain reports showed that prolonging developmental duration by yeast supplementation did not affect lifespan (Hunter, 1959; Northrop, 1917b). However, few studies focused on the associations between developmental timing and adult lifespan in Drosophila. To establish whether developmental stages and adult lifespans are interdependent in individual flies, we analyzed the following relationships: larval and pupal duration (Figure 6D,G), larval duration and adult lifespan (Figure 6E,H), and pupal duration and adult lifespan (Figure 6F,I). No significant correlations between the data for these pairs of parameters in either sex (Figure 6D–I) and those reported in previous studies were found. As the flies had the same genetic background and were exposed to the same diet and environmental conditions throughout all their life stages, it was unlikely that their genotypes influenced the relationship between development time and lifespan, demonstrating that DIAMonDS can detect unique relationships between developmental time and lifespan under different intrinsic and extrinsic conditions.

In this study, we were unsuccessful at using DIAMonDS to run long-term lifespan assays on other wild type fruit fly strains such as Oregon-R and Canton-S. Lethality accidentally escalated because the rearing conditions deteriorated. For instance, water droplets condensed and coalesced on the plate surfaces. However, these errors might have reflected relative metabolic and/or genetic differences among fly strains. To find common optimum conditions for measuring the lifespan of other laboratory strains, we have tried to observe the viability of three strains (w1118, Oregon-R, and Canton-S) in condition with several microplate well-size (96-well, 48-well, and 24-well) (Figure 6—figure supplement 1). The viabilities were measured at the time point at 1, 2, 3, and 4 weeks with once plate replacement a week. We observed that the reduced viability was not rescued by changing to bigger microplate-well size, and somewhat, increasing well-size might have harmful effects on the survival of aged flies (Figure 6—figure supplement 1A–C). We next tested the two different plate replacement cycles (once a week, or once 2–3 days) using Oregon-R and Canton-S in 96-well microplate. We observed a shorter plate replacement cycle could effectively improve the viability (Figure 6—figure supplement 1B,C). However, because plate replacement is required a lot of work time, it seems to be not suitable for the high-throughput experiments. Further optimization of the experimental conditions will be necessary to effectively use DIAMonDS to conduct lifespan tests on a wide range of fly strains.

## Discussion

In this study, we attempted to develop DIAMonDS as a new tool to analyze automatically and sequentially the transition time point in the growth and developmental multi-stage of individual flies and use the transition time points as a phenotype. We demonstrated that DIAMonDS determines Drosophila pupariation, eclosion, and death at high temporal resolution. Further, it can analyze the relationships among stages by sequentially detecting multiple life events in many individuals. Thus, DIAMonDS can help clarify the complex interactions among genetic and environmental factors throughout the Drosophila life cycle. DIAMonDS can also eliminate the constraint of long data acquisition and analysis time intervals, operate multiple scanners simultaneously, and facilitate high-throughput analysis. Overall, DIAMonDS substantially ameliorates Drosophila research endeavors compared to conventional manual counting methods.

DIAMonDS automatically detects time points from time-lapse images via the novel algorithm Sapphire. Our results indicated that relative to manual detection, DIAMonDS correctly detected 74–85% of the pupariation and eclosion and ~ 92% of the death events within ± 10 frames. Thus, DIAMonDS is fully functional both for preliminary experiments and large-scale screening. The output of Sapphire can guide the manual determination of exact values. Therefore, DIAMonDS can generate publishable high-quality data. Detection accuracy could be greatly improved by reducing noise in time-lapse image acquisition. Data quality can also be enhanced via the machine learning training step in Sapphire. Optimization of experimental conditions is an important initial prerequisite step for stable, highly reliable data acquisition.

Nevertheless, DIAMonDS has certain limitations. First, it is unsuitable for the analysis of insects with normal circadian rhythms as the flatbed scanners repeatedly emit light for imaging. Second, the confined well space used for insect rearing might adversely affect individual fly health and behavior. Third, this approach might be inappropriate for establishing the effects of volatile or unstable substances on flies. Fourth, the reliability of this system may be reduced as the surfaces of the microplate lids become dirty over time. Fifth, occasionally, an animal cannot be detected in the image by the existence of a blind area of scanning. The system is not greatly affected even if ‘off-camera’ occurs during an active state of an animal. But the accuracy of event detection might be slightly affected when ‘off-camera’ occurs just at the timing of the event shift. It could be reduced by increasing the spatial- or temporal-resolution to eliminate the blind-area of each well. These problems could be solved by further improvement in the system. For example, detection of the circadian rhythm might be achieved by image acquisition using infrared rays, and It seems that the use of large-wells might expect to reduce the adverse effects of rearing on small-wells.

To date, we successfully used DIAMonDS to analyze the normal lifespan of the w1118 fruit fly strain but not those of the wild-type Oregon-R and Canton-S. One reason for this constraint is the frequent occurrence of accidental death caused mainly by water droplet coalescence on the microplate wall surfaces. Differences between strains may be due to differences in genetic background or intestinal environment. The experimental setup will require further optimization to overcome these limitations in lifespan analysis by DIAMonDS.

Here, we reported a novel technique for measuring multiple life events and their transition time points in Drosophila. In principle, DIAMonDS can also determine life cycle phase shifts in other small animals, and we intend to expand its applicability in medical, agricultural, and ongoing biological research.

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
      <td>Gene (D. melanogaster )</td>
      <td>mth1</td>
      <td>Flybase</td>
      <td>FBti0012557</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (D. melanogaster )</td>
      <td>w1118</td>
      <td>Kept in lab stock</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (D. melanogaster )</td>
      <td>Oregon-R</td>
      <td>Kept in lab stock</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (D. melanogaster )</td>
      <td>Canton-S</td>
      <td>Gift from Dr. Uemura</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster )</td>
      <td>R29H01-GAL4</td>
      <td>Flybase</td>
      <td>FBti0191124</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster )</td>
      <td>UAS-TeTxLC</td>
      <td>Flybase</td>
      <td>FBtp0001264</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Sapphire</td>
      <td></td>
      <td></td>
      <td>https://github.com/kanglab/Sapphire/tree/master</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>VueScan</td>
      <td></td>
      <td></td>
      <td>https://www.hamrick.com</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Prism 8</td>
      <td></td>
      <td></td>
      <td>https://www.graphpad.com/scientific-software/prism/</td>
    </tr>
  </tbody>
</table>

### D. melanogaster stocks and rearing conditions

The wild-type strain used here was mainly w1118, Oregon-R, and Canton-S. The mth1 (BDSC #27896) mutant males were used in the paraquat resistance test after backcrossing six-fold with w1118. R29H01-GAL4 (BDSC #47343) and UAS-TeTxLC (BDSC #28838) were obtained from the Bloomington Drosophila Stock Center, Bloomington, IN, USA. All fly strains were maintained on standard medium at 25°C (Appendix 1).

Most experiments were conducted in a plant growth chamber (LPH-410NS; NK System Co. Ltd., Nagoya, Japan) maintained at 25°C and 60% RH. For the experiment using R29H01-GAL4 > UAS TeTxLC, the larvae were reared at 29°C to increase GAL4 activity.

### DIAMonDS hardware and layout

Detailed DIAMonDS hardware and layout are described in Appendix 6.

### Microplate preparation for DIAMonDS

Microplates with 96 or 384 wells were filled with standard fruit fly culture media (Appendix 1). A handmade acrylic lid was used for the 384-well microplate (Appendix 2). Titer stick film (Watson, Tokyo, Japan) was used for the 96-well microplate (Appendix 3). To determine the pupariation and eclosion timings, the film seal on the 96-well microplate was perforated with air holes (0.35 mm diameter; eight holes/well) over each well. For the stress resistance and lifespan tests, the 96-well microplate was sealed with film, which was then cut to form a cross shape over each well. Individual adult flies were transferred to each well without anesthesia. For the 384-well microplate, the flies were anesthetized with triethylamine and placed individually into each well (Appendix 4). The acrylic lid was then securely affixed to the microplate with screws and masking tape (Appendix 2).

### Time-lapse image acquisition

Three microplates were secured with glass slides to the flatbed scanner surface as described in Appendix 5. The scanner was then connected to a personal computer. ‘VueScan’ scanner software in the PC was launched, and time-lapse images were acquired at 1–15 min intervals (Appendix 6).

### Starvation and drug resistance test

For the drug resistance assay, the wells of a microplate were filled with yeast-sucrose medium containing the appropriate chemicals as shown in Appendix 1. For the starvation test, the wells of a microplate were filled with 1% (w/v) agar (Appendix 1). Virgin adult flies were collected under CO2 anesthesia, stored in a vial with normal food for 3–5 days, placed individually into each microplate well, and subjected to time-lapse image acquisition.

### Pupariation and eclosion time point detection for the same individuals

To measure pupariation and eclosion timing, newly hatched L1 larvae (24–25 hr AEL) were used as the lethality was too high when embryos were used (Figure 2—figure supplement 1A). The large media volume in each well (150 µL) also increased lethality because the embryos suffocated when the media became very viscous. Therefore, we used 100 µL media for this approach (Figure 2—figure supplement 1B). L2 or L3 larvae were also used in the DIAMonDS experiments. After the larvae were loaded into the microplate wells, the microplate was covered with Titer stick film (Watson, Tokyo, Japan), inverted on a predetermined area of the flatbed scanner surface, and fastened with tape. The scanner was then inverted in the incubator to prevent liquefied culture medium from falling onto the film surface. Time-lapse scanning was then run in VueScan in the PC. Scanning was terminated when all individuals eclosed to adults. The time-lapse images were analyzed in Sapphire (Figure 1B,C).

### Pupariation, eclosion, and lifespan detection in identical individuals in DIAMonDS

Microplates were prepared with synchronized L1 larva (one/well), and images were acquired as previously described. Developmental stages for individuals were analyzed according to the images saved to the PC. After all individuals reached the P14 stage pupa, the pupae were transferred to the same well positions in a new microplate. The wells were sealed with new film, and scanning was resumed. After all flies completely eclosed, the individual adults were transferred to the same well positions in a new microplate, and scanning was restarted to measure individual lifespans. Adult flies were transferred weekly to new microplates until all flies died. The acquired images were then analyzed in Sapphire. Finally, we introduced the data obtained by Sapphire into the DIAMonDS analysis templates (Supplementary file 1) and calculated the time of each life-event (Appendix 7).

### Life event detection algorithm and software: Sapphire

The present system included an automated, high-accuracy life event detection algorithm and image and signal processing (Figure 1C). The software could be obtained from (https://github.com/kanglab/Sapphire/tree/master; Seong et al., 2020; copy archived at https://github.com/elifesciences-publications/Sapphire). The contents in the address also describe the installation, license, and system requirements such as directory tree and external dependencies. Quantitative algorithm summary and robustness in various parameter spaces are described in Appendix 8.

### Image processing

The present system performed semantic segmentation via a deep neural network whose architecture is described in Figure 1—figure supplement 2. Sufficient annotation data increases inference accuracy in deep learning. For network training, handmade supervised data were prepared and applied to image data augmentation. For adult body segmentation in death detection, the annotation data for 178 adults were introduced and magnified up to 71,200 by general image data augmentation (vertical and horizontal flips, rotation, and luminance modulation). For adult body segmentation in pupariation and eclosion detection, annotation data for 300 adults and 5760 larvae (as distractors) were prepared and magnified by ≤ 60,000 and≤57,600, respectively. For larval body segmentation in pupariation and eclosion detection, annotation data for 1839 larvae and 183,900 augmented data were introduced to train the network. The present system detected rough outlines of the animal bodies (Appendix 8).

### Signal processing

In the present system, subtractions between consecutive segmentation images were converted to signals in CF, which is a change point detection algorithm (Takeuchi and Yamanishi, 2006).

The CF signal was obtained as follows:

1. Considering the following AR model for time series data $x_{t}$:

$$
x_{t}=A_{t-1}x_{t-1}+A_{t-2}x_{t-2}+⋯
$$

2. Inference of parameters $\theta=(A_{1},⋯,A_{k},\mu,\sigma)$ by maximizing I:

$$
I=\sum_{i=1}^{t}1-r^{t-1}log⁡Px_{i}|x_{i-1},\theta
$$

3. Calculation of scores:

$$
Scorex_{t}=-log⁡P_{t-1}x_{i}|x_{i-1}
$$

4. Time averaging of scores:

$$
y_{t}=\frac{1}{T}\sumi=t-T+1tScore(x_{i})
$$

5. Recalculating scores for $y_{t}$:

For death detection, the CF signal was calculated from the adult body segmentation and the death timing and determined as a maximum CF signal point capturing dynamic-to-static changes (Appendix 8). On the other hand, two CF signals were obtained from the adult and larval body segmentations in pupariation and eclosion detection. Pupariation is defined as the maximum dynamic-to-static transition point for larvae. Eclosion is defined as the maximum static-to-dynamic transition point for adults (Appendix 8). After time-lapse scanning, we can easily discriminate ‘out-of-event’, such as larval, and, pupal dead individuals. Sapphire can exclude ‘out-of-event’ wells by making the ‘black lists’ file (Appendix 7).

### Statistics

Data were analyzed, and graphs were plotted in GraphPad Prism v. 8 (GraphPad Software, San Diego, CA, USA). A student’s unpaired, two-tailed t-test was performed to compare differences between groups in each experiment and Dunnett's method of one-way ANOVA was used for multiple comparison test (***p<0.001; **p<0.01; *p<0.05; n.s., no significant).
