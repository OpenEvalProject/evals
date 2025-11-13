# Robotic search for optimal cell culture in regenerative medicine

## Authors

- Genki N Kanda<sup>1</sup> ([ORCID: 0000-0002-6372-241X](https://orcid.org/0000-0002-6372-241X)) †
- Taku Tsuzuki<sup>4</sup>
- Motoki Terada<sup>1</sup>
- Noriko Sakai<sup>1</sup>
- Naohiro Motozawa<sup>1</sup>
- Tomohiro Masuda<sup>1</sup>
- Mitsuhiro Nishida<sup>1</sup>
- Chihaya T Watanabe<sup>4</sup>
- Tatsuki Higashi<sup>4</sup>
- Shuhei A Horiguchi<sup>4</sup> ([ORCID: 0000-0002-8459-1914](https://orcid.org/0000-0002-8459-1914))
- Taku Kudo<sup>3</sup>
- Motohisa Kamei<sup>3</sup>
- Genshiro A Sunagawa<sup>1</sup>
- Kenji Matsukuma<sup>3</sup>
- Takeshi Sakurada<sup>4</sup>
- Yosuke Ozawa<sup>4</sup> †
- Masayo Takahashi<sup>1</sup>
- Koichi Takahashi<sup>2</sup> †
- Tohru Natsume<sup>3</sup> ([ORCID: 0000-0002-1510-2582](https://orcid.org/0000-0002-1510-2582)) †

### Affiliations

1. Laboratory for Retinal Regeneration, RIKEN Center for Biosystems Dynamics Research Kobe Japan ([ROR:023rffy11](https://ror.org/023rffy11))
2. Laboratory for Biologically Inspired Computing, RIKEN Center for Biosystems Dynamics Research Osaka Japan ([ROR:023rffy11](https://ror.org/023rffy11))
3. Robotic Biology Institute Inc. Tokyo Japan
4. Epistra Inc. Tokyo Japan
5. VCCT Inc. Kobe Japan
6. Laboratory for Molecular Biology of Aging, RIKEN Center for Biosystems Dynamics Research Kobe Japan ([ROR:023rffy11](https://ror.org/023rffy11))
7. Vision Care Inc. Kobe Japan
8. Graduate School of Media and Governance, Keio University Fujisawa Japan ([ROR:02kn6nx58](https://ror.org/02kn6nx58))
9. Graduate School of Frontier Biosciences, Osaka University Suita Japan ([ROR:035t8zc32](https://ror.org/035t8zc32))
10. Department of Life Science and Biotechnology, Cellular and Molecular Biotechnology Research Institute, National Institute of Advanced Industrial Science and Technology Tokyo Japan ([ROR:01703db54](https://ror.org/01703db54))

† Corresponding author

## Abstract

Induced differentiation is one of the most experience- and skill-dependent experimental processes in regenerative medicine, and establishing optimal conditions often takes years. We developed a robotic AI system with a batch Bayesian optimization algorithm that autonomously induces the differentiation of induced pluripotent stem cell-derived retinal pigment epithelial (iPSC-RPE) cells. From 200 million possible parameter combinations, the system performed cell culture in 143 different conditions in 111 days, resulting in 88% better iPSC-RPE production than that obtained by the pre-optimized culture in terms of the pigmentation scores. Our work demonstrates that the use of autonomous robotic AI systems drastically accelerates systematic and unbiased exploration of experimental search space, suggesting immense use in medicine and research.

## Introduction

Automating scientific discovery is one of the grandest challenges of the 21st century (Kitano, 2021; Kitano, 2016). A promising approach involves creating a closed loop of computation and experimentation by combining AI and robotics (King et al., 2009). A relatively simple form of autonomous knowledge discovery involves searching for optimal experimental procedures and parameter sets through repeated experimentation and result validation, according to a predefined validation method. For example, in material science, the parameters associated with the growth of carbon nanotubes have been explored using an autonomous closed-loop learning system (Nikolaev et al., 2016). In experimental physics, Bayesian optimization has been used to identify the optimal evaporation ramp conditions for Bose–Einstein condensate production (Wigley et al., 2016). In 2019, a promoter-combination search in molecular biology was automated using an optimization algorithm-driven robotic system (HamediRad et al., 2019). Some robotic systems for cell culture have already been developed (dos Santos et al., 2013; Kino-Oka et al., 2009; Konagaya et al., 2015; Liu et al., 2010; Matsumoto et al., 2019; Nishimura et al., 2019; Ochiai et al., 2021; Soares et al., 2014; Thomas et al., 2008); however, many of these fixed-process automation apparatuses lack the flexibility and precision necessary to execute comprehensive parameter searching.

Here, we report the development of a robotic search system that autonomously and efficiently searches for the optimal conditions for inducing iPS cell differentiation into retinal pigment epithelial (RPE) cells (iPSC-RPE cells). The system replaces the manual operations involved in cell culture with robotic arms. Cell culture is probably one of the most delicate procedures in two respects. First, the parameters related to physical manipulation can greatly affect the outcome of the experiment (Kanie et al., 2019). Secondly, it takes a long time to execute a series of protocols. For example, cells artificially differentiated from embryonic stem cells or induced pluripotent stem cells (ES/iPS cells) need to be processed using hundreds of experimental procedures that typically last for weeks or months before they can be used for transplantation in regenerative medicine.

During these processes, cells are given chemical perturbations (e.g. type, dose, and timing of reagents) and physical perturbations (e.g. strength of pipetting, vibration during handling of plates, timing of transfer from/to CO2 incubator, and accompanying changes in factors such as temperature, humidity, and CO2 concentration). Due to the heterogeneous and complex internal states of cells, suitable culture conditions must be determined for each strain and/or lot (Kino-Oka and Sakai, 2019). A small difference in a single chemical stimulus or physical procedure can lead to failure of differentiation or poor quality of the produced cells, and such consequences can often become experimentally detectable only days or weeks after the input is given (Kino-oka et al., 2019). Therefore, the use of robotic arms is a great addition in the search for optimal cell culture conditions because robots can repeatedly perform the same operation with high precision. Moreover, they hardly make any errors, which are logged when committed.

It is advantageous to utilize high-accuracy and programmable robotic arms for the search of optimal cell culture parameters. Unlike human hands, robotic arms can repeatedly perform the same procedure. They ensure reproducibility by keeping all parameters related to physical procedures constant. Furthermore, the actual operations are logged by the software along with sensor information when they are deviated from the established programs. Thus, robotization provides an ideal parameterization of experimental procedures. Some automated cell culture machines have already been proposed (Regent et al., 2019); however, proper formulation of an autonomous search for optimal culture conditions has not yet been determined.

In this study, we combined a Maholo LabDroid (Yachie et al., 2017) and an AI system that independently evaluates the experimental results and plans the next experiments to realize an autonomous robotic search for optimal culture conditions. We first created a digital representation of the regenerative medical cell culture protocol used for iPS cell differentiation into retinal pigment epithelial (RPE) cells (iPSC-RPE cells) (Mandai et al., 2017), which can be executed by the robot and used as a template for an AI-driven parameter search (Figure 2—video 1). We then implemented the experimental protocol on a LabDroid, which is a versatile humanoid robot that can perform a broad range of experimental procedures. Its flexibility allows frequent changes in protocols and protocol parameters, making it suitable for use in experimental parameter searches. The robot has an integrated microscope that provides data for image-processing through AI, which evaluates the quality of growing cells. The search process was mathematically formulated as a type of experimental design problem, and a batch Bayesian optimization (BBO; Figure 1, Figure 1—figure supplements 1 and 2) technique was employed as a solver. Finally, we demonstrated that iPSC-RPE cells generated by LabDroid satisfy the cell biological criteria for regenerative medicine research applications.

![Figure 1.](https://cdn.elifesciences.org/articles/77007/elife-77007-fig1-v1.jpg)

**Figure 1.:** (A) Overall workflow for the optimization of experimental procedures using combined experimental robotics and Bayesian optimization. The user defines the target experimental protocol, subject parameters of the protocol, and the validation function. In this study, we chose the differentiation procedure from iPS to RPE cells as a target protocol and selected the reagent concentration, administration period, and five other parameters (details are shown in Table 1). We defined the pigmented area in a culture well, which represents the degree of RPE differentiation induction, as the validation function. The optimization program presented multiple parameter candidates; the LabDroid performed the experiment, and then an evaluation value for each candidate was obtained. Subsequently, the Bayesian optimization presented a plurality of parameter candidates predicted to produce higher validation values. The optimal parameters were searched by repeating candidate presentation, experiment execution, validation, and prediction. The detailed components are shown in Figure 1—figure supplement 2. (B) Workflows performed in this study. First, robotization of the iPSC-RPE protocol was performed as a baseline. Next, the optimization process was conducted in three rounds, followed by statistical and biological validation. The figure numbers in parentheses represent the results shown in the figure.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/77007/elife-77007-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) Schematic diagram of the process from iPSC stock to iPSC-derived RPE cell transplantation. The steps are roughly divided into iPSC culture, iPSC-RPE differentiation, purification, storage, recovery culture, and surgery. Arrows indicate daily operations, and thick gray lines indicate multi-day operations. (B) Timeline of the baseline and optimization and validation experiments. The baseline and optimization experiments were completed with scoring. The validation experiments, however, were performed by generating an iPSC-RPE stock through a purification process and carrying out a cell biological analysis. The arrows represent the figure number in which the result from that process is displayed.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/77007/elife-77007-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** The system platform. The robotic search using this system starts with the provision of queries for round 1 from the optimizer to the protocol compiler and the provision of the base protocol from the user to the protocol compiler. Each rectangle represents a system component. Solid lines represent the movement of data (including cells), and dotted lines represent physical interactions.

## Results

### Robotization of the iPSC-RPE differentiation protocol

An overview of the iPSC-RPE differentiation protocol used for optimization is shown in Figure 2A and Figure 1—figure supplement 1. It consists of five steps: seeding, preconditioning, passage, RPE differentiation (induction), and RPE maintenance culture. The day on which the passage was performed was defined as differentiation day (DDay) 0, and the cultured cells were sampled and validated on DDays 33 and 34. To implement this protocol using LabDroid, the necessary peripheral devices were installed on and around LabDroid’s workbench (Figure 2B, Figure 2—figure supplement 1). We designed the system to work simultaneously with eight 6-well plates per batch, for a total of 48 cell-containing wells. LabDroid was programmed for three types of operations: seeding, medium exchange, and passage (Figure 2—figure supplements 2–7; Figure 2—source data 3; Figure 2—video 1). The steps for the preconditioning and induction, which correspond to the preparation of reagents, were named medium exchange type I, and the step for RPE maintenance culture, which does not involve reagent preparation, was named medium exchange type II (Figure 2A, Figure 2—figure supplement 2).

![Figure 2.](https://cdn.elifesciences.org/articles/77007/elife-77007-fig2-v1.jpg)

**Figure 2.:** (A) Schematic diagram of the standard iPSC-RPE differentiation procedures. DDay indicates the differentiation day. Filled circles represent days when the robot operated, solid circles represent days with human operations only, and dashed line circles represent days when no operations were conducted. F stands for FGF receptor inhibitor; Y for Y-27632, a Rho-kinase inhibitor; SB for SB431542, a TGF-β/Activin/Nodal signal inhibitor; CKI for a CKI-7, Wnt signal inhibitor; and MX for medium exchange. (B) The LabDroid Maholo including peripheral equipment. (C) Plate numbering and the orders of seeding, passage, and medium exchange operations. Eight 6-well plates were used for each experiment. (D) Well numbering. (E) Scores of the first trial. iPSC-RPE differentiation was conducted under six different trypsin treatment times using the LabDroid. Yellow bars represent the pigmented cell area score of each well. The bold black lines and the shaded area around the lines represent the mean score and SEM of eight samples operated at the same trypsin time, respectively. The raw values are shown in Figure 2—source data 2.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/77007/elife-77007-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) Exterior photograph of the LabDroid booth. The LabDroid consists of an acrylic box of W2500 x D2000 x H2200 (mm). (B) Plan view of the LabDroid booth (3D-CAD) and layout of the equipment. (C–D) Front view photograph of the LabDroid booth and schematic drawing of the equipment (these panels are identical to those in Figure 2B). (E) Top view photograph of the LabDroid booth. (F) A back view photograph of the LabDroid booth. Components: (1) dual-arm humanoid; (2) CO2 incubator; (3) micropipettes; (4) pipette tips; (5) tip sensor; (6) dustbin; (7) aspirator; (8) tube racks; (9) plate racks; (10) dry bath; and (11) microscope.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/77007/elife-77007-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** (A) Seeding (DDay −7). (B) Medium exchange type I for preconditioning (DDays −6 to −1) and the first part of RPE induction (DDays 1–19). (C) Medium exchange type II for the second part of RPE induction (DDays 20–25), and RPE maintenance (DDays 26–32). (D) Passage (DDay 0). The dashed line rectangles represent the operations carried out by humans, and solid line rectangles represent the operations carried out by the robot.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/77007/elife-77007-fig2-figsupp3-v1.jpg)

**Figure 2—figure supplement 3.:** (A) Entire image. (B) Enlarged image of the dotted rectangle from panel (A).

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/77007/elife-77007-fig2-figsupp4-v1.jpg)

**Figure 2—figure supplement 4.:** (A) Entire image. (B) Enlarged image of the dotted rectangle from panel (A).

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/77007/elife-77007-fig2-figsupp5-v1.jpg)

**Figure 2—figure supplement 5.:** (A) Entire image. (B) Enlarged image of the dotted rectangle from panel (A).

![Figure 2—figure supplement 6.](https://cdn.elifesciences.org/articles/77007/elife-77007-fig2-figsupp6-v1.jpg)

**Figure 2—figure supplement 6.:** (A) Entire image. (B) Enlarged image of the dotted rectangle from panel (A).

![Figure 2—figure supplement 7.](https://cdn.elifesciences.org/articles/77007/elife-77007-fig2-figsupp7-v1.jpg)

**Figure 2—figure supplement 7.:** (A) Entire image. (B) Enlarged image of the dotted rectangle from panel (A).

![Figure 2—figure supplement 8.](https://cdn.elifesciences.org/articles/77007/elife-77007-fig2-figsupp8-v1.jpg)

**Figure 2—figure supplement 8.:** (A–C) The 6-well plates were placed on top of a white LED lighting plate and photographed with a camera fixed to the mount (A). The raw images acquired (B) were cropped in a circle to the size of the bottom of the well (C). (D) Workflow of image processing performed using ImageJ/Fiji macro. The background was removed in steps 1–3, binarization in step 4, and noise in steps 5 and 6. Since it is empirically known that differentiation-inducing cells are less likely to grow near the sides of the wells, only the central portion was cropped (step 7) and the scores were subsequently calculated. (E–J) Examples of processed images. The images shown are samples from well 1 of plate 1 in the baseline experiment. Images after Gaussian blur (E), background subtraction (F), sharpening (G), binarization by thresholding (H), mathematical morphology processing (I), crop, and clear outside (J) processing. The orange circle in panel (I) represents the crop area in step 7. The pigmentation score was calculated as the area of the black region in panel (J). (K) Merged image of the image before processing (corresponding to panel C) and the area determined to be pigmented (corresponding to panel (J), red frame). All images shown in this figure have been contrast-optimized to facilitate the visualization of the examples, but the actual values were used when processing the images for quantification.

First, we used LabDroid to perform baseline experiments involving the induction of iPSC-RPE cell differentiation under the same conditions as the typical manual operations. Because of the differences in structure and experimental environment between the LabDroid and humans, some operations and movements, such as the use of a centrifuge, the presence or absence of cell counting at the time of passage, and the speed of movement, differed from those of humans. For example, achieving the same time interval for trypsin treatment in all wells of a single plate during cell detachment using LabDroid is difficult. Therefore, the passage operation was performed at six separate time intervals. The cells differentiating into RPE cells produce melanin, which causes them to turn brown. Therefore, the area ratio of the total number of pigmented cells on DDay 34 was used to estimate the differentiation induction efficiency and obtain evaluation scores, following the example of previous studies (Kuroda et al., 2019; Regent et al., 2019; Figure 2—figure supplement 8). These validation scores were used to simplify the validation process and do not reflect the entire quality of the RPE.

Baseline experiments were conducted and validated using six trypsin conditions and eight plates (Figure 2C–E; Figure 2—source data 1 and Figure 2—source data 2). The highest scoring was obtained when trypsin treatment was conducted for 20 min at 37 °C, followed by 14 min incubation at room temperature (RT, approximately 25 °C), with an eight-plate score of 0.44±0.03 (mean ± SEM, n=8). The lowest scoring was obtained when trypsin treatment was conducted for 20 min at 37 °C, followed by 23 min at RT, with an eight-plate score of 0.33±0.02 (mean ± SEM, n=8). LabDroid successfully performed the iPSC-RPE protocol, as evidenced by the detection of pigmented cells in all 48 wells and the lack of errors in the operating process. However, in the naive transplantation of the manual protocol to the robot, the induction efficiency was insufficient. This suggests that it is inherently difficult to describe physical parameters, including unrecorded human movements. Therefore, we attempted to optimize the protocol parameters to further improve the scores using a robotic search.

### Parameterization of the protocol

To improve the pigmentation score, we selected seven parameters for optimization: two from the preconditioning step, three from the passage step, and two from the induction step. Search domains were set for each parameter (Table 1; Figure 3A and B).

![Figure 3.](https://cdn.elifesciences.org/articles/77007/elife-77007-fig3-v1.jpg)

**Figure 3.:** (A) Definition of the target parameters and corresponding steps in the protocol: PC, preconditioning concentration; PP, preconditioning period; DP, detachment trypsin period; DS, detachment pipetting strength; DL, detachment pipetting length; KP, KSR concentration reducing period; and 3P, three chemical (Y, SB, CKI) supplement administration period. (B) Ranges and stepping of the parameters. (C) The Bayesian optimization module consists of two components: a Model updater and a Query generator. The Model updater updates the Gaussian process posterior on the experiment using all available data $D={(x_{i},y_{i})}_{i=1}^{n}$, where x indicates experimental parameter, and y indicates corresponding evaluation score. The Query generator calculates the acquisition function $\alpha(x;D)$ for an experiment parameter $x$ with the posterior distribution $P(y|x,D)$, and generates the experiment parameter set $X_{next}$ for the next 48 points using the policy function with $\alpha(x;D)$. (D and E) Test of the query generation process using a two-dimensional toy acquisition function. (D) Values of the toy acquisition function given an experimental parameter set. The horizontal axis represents the input values of $x_{DP}$ (contextual parameter), whereas the vertical axis represents the input values of the other six remaining context-free parameters $X=(x_{PC},x_{PP},x_{DS},x_{DL},x_{KP},x_{3P})$, which are collapsed into a single axis. The color of the heatmap indicates the value of the acquisition function. In the heat map, the acquisition value is higher in places where the color is closer to red and lower in places where the color is closer to blue. (E) Test of the query generation process for the experimental parameter set $X_{next}$ in the next experiment using a batch contextual local penalization policy (BCLP). The heat maps in the upper row show the (penalized) acquisition function values, and the lower row shows the penalization values for the acquisition function. The queries $X_{next}$ for 48 wells (right side figure) were iteratively generated from the maximization-penalization loop on the acquisition function.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/77007/elife-77007-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** Test of a Bayesian posterior updated in a Gaussian process (GP). (A) Sample paths from the zero-mean GP prior. (B) Sample paths from the GP posterior after executing some experiments (indicated by black dots). The gray shaded area represents the pointwise mean plus and minus twice the standard deviation for each input value.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/77007/elife-77007-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** Sequential Bayesian optimization was tested by determining the maximum of a one-dimensional toy objective function. This figure illustrates the Bayesian optimization procedure over several iterations. The objective function is indicated by a purple dashed curve on the left side of each plot. The past experimental results are indicated by dots, and the newest experimental results are indicated by white dots. The GP posterior mean function is indicated by a black line, and covariance intervals are indicated by purple shaded areas. The plots on the right side show the acquisition functions in the orange curves. The value of the acquisition function is high where the model predicts a high objective (exploitation) and where the prediction uncertainty is high (exploration). The black vertical dashed lines show the place of acquisition max, a factor of importance to be tested in a subsequent experiment.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/77007/elife-77007-fig3-figsupp3-v1.jpg)

**Figure 3—figure supplement 3.:** An approximate prediction of how much the value of each variable affects the score based on domain knowledge before performing a series of optimizations. The toy testing function was simply multiplied by the predicted function for each of the variables below, $f(x_{PC},x_{PP}x_{DS},x_{DL}x_{DP},x_{KP},x_{3P})=f_{PC}(x_{PC})f_{PP}(x_{PP})f_{DS}(x_{DS})f_{DL}(x_{DL})f_{DP}(x_{DP})f_{KP}(x_{KP})f_{3P}(x_{3P})$ (A) Prediction of preconditioning (FGFRi) concentration (PC) response. It increased from 0 nM, reached a maximum at 100 nM, decreased after 100 nM, and approached 0.5. (B) Prediction of the preconditioning period (PP) response: on Day 1 it was 0, it increased monotonically thereafter, and reached a maximum value on Day 6. (C) Prediction of the detachment trypsin period (DP) response: an optimal value between 13 and 20 min was expected. (D) Prediction of the detachment pipetting strength (DS) response: it achieved a maximum value at 10 mm/s and then decreased monotonically. Although an important parameter, the detachment pipetting length (DL) is always assumed to be 1 because of the difficulty of prediction. (E) Prediction of the KSR period (KP) response: it was expected to increase monotonically until Day 8, and to be stationary thereafter. (F) Prediction of the three-supplement period (3P) response: it was expected to take a non-zero value and increase monotonically from around Day 3 onwards.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/77007/elife-77007-fig3-figsupp4-v1.jpg)

**Figure 3—figure supplement 4.:** The vertical axis shows the value, and the horizontal axis shows the number of circles. The blue horizontal line represents the ground truth (optimal value). In each series, three experiments were conducted independently, and the score of the query with the highest evaluation score in the true function among the queries that had appeared in a certain round was plotted. The error bars represent the standard error (SEM) in each round. (A) The red series shows the results of batch Bayesian optimization (BCLP) with no observation noise. The yellow series shows the results of BCLP with a Gaussian noise SD=0.064. The green series shows the BCLP results with a high Gaussian noise SD=0.4. The black series represents the results of random sampling. Compared to random sampling, Bayesian optimization improved the convergence performance and converged to the optimal solution when the observation noise was sufficiently small. Black, random; green, BCLP (SD=0.4); orange, BCLP (SD=0.064); red, BCLP (SD=0). The shaded area represents the SEM image. (B) Comparison of BCLP performance when the batch size was changed. For the benchmark function (noise SD=0.064), optimization was performed using a different number of plates (Np) per round. The blue series represents Np=2, the green series represents Np=4, the orange series represents Np=8, and the red series represents Np=16. As the number of plates (the batch size) increased, batch Bayesian optimization tended to converge to an optimal solution with fewer rounds. Blue, Np=2; green, Np=4; orange, Np=8; red, Np=16. The shaded area represents the SEM image.

**Table 1.**
 Definition of optimized parameters.Parameter names, parameter name codes, description, parameter ranges, parameter units, correspondence between experimental procedure and parameters used (related to Figures 2A, 3A and B).


<table>
  <thead>
    <tr>
      <th>Parameter name</th>
      <th>Code</th>
      <th>Description</th>
      <th>Range</th>
      <th>Unit</th>
      <th>Protocol step</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Preconditioning concentration</td>
      <td>PC</td>
      <td>FGFRi concentration in medium</td>
      <td>0–505</td>
      <td>nM</td>
      <td>Preconditioning</td>
    </tr>
    <tr>
      <td>Preconditioning period</td>
      <td>PP</td>
      <td>FGFRi duration in medium</td>
      <td>1–6</td>
      <td>day</td>
      <td>Preconditioning</td>
    </tr>
    <tr>
      <td>Detachment trypsin period</td>
      <td>DP</td>
      <td>Trypsin incubation duration at room temperature after incubation at 37 °C, 20 min.</td>
      <td>5, 8, 11, 14, 17, 20, 23</td>
      <td>min</td>
      <td>Passage</td>
    </tr>
    <tr>
      <td>Detachment pipetting strength</td>
      <td>DS</td>
      <td>Pipetting strength during cell detachment</td>
      <td>10–100</td>
      <td>mm/s</td>
      <td>Passage</td>
    </tr>
    <tr>
      <td>Detachment pipetting length</td>
      <td>DL</td>
      <td>Bottom surface area to be pipetted</td>
      <td>short / long</td>
      <td>N/A</td>
      <td>Passage</td>
    </tr>
    <tr>
      <td>KSR period</td>
      <td>KP</td>
      <td>KSR concentration and duration in medium:KSR concentration is decreased linearly every day so that KSR becomes 10% on DDday of KP value</td>
      <td>1–19</td>
      <td>day</td>
      <td>RPE differentiation</td>
    </tr>
    <tr>
      <td>Three supplements period</td>
      <td>3P</td>
      <td>Three chemical supplements duration</td>
      <td>3–19</td>
      <td>day</td>
      <td>RPE differentiation</td>
    </tr>
  </tbody>
</table>

From the preconditioning step on DDays −1 to −6, we selected two parameters for optimization: the concentration of fibroblast growth factor receptor inhibitor (FGFRi) in the medium (PC, preconditioning concentration), and the duration of addition (PP, preconditioning period). From the passage step performed on DDay 0, we selected three parameters to optimize: the pipetting strength during cell detachment (DS, detachment pipetting strength), the area of the bottom surface to be pipetted (DL, detachment pipetting length), and trypsin processing time (DP, detachment trypsin period) of a passage. DP is a contextual parameter that can only be used to perform experiments at fixed values, owing to the specifications of the experimental system. In this case, DP is allowed to take different fixed values at three-minute intervals, corresponding to the number of wells in the plate. From the induction step on DDays 1–25, we selected two parameters to optimize: the concentration of KnockOut Serum Replacement (KSR) in the medium (KP, KSR period), and the duration of exposure period of the three chemical supplements (3P, three supplement period).

### Optimization of the protocol

To improve the optimization performance, 48 conditions (eight plates × six wells, as shown in Figure 2C) were executed in parallel in each batch. The 48 conditions were selected from the search space using the Bayesian optimization module to maximize the acquisition function calculated from the past experimental data. In general, solving a high-dimensional, expensive black-box optimization problem such as the present one with a limited number of rounds is challenging. In our case, some 200 million possible parameter combinations existed in the search space, and the point where the pigmented score was optimal in three rounds (144 queries) had to be determined, because one experiment round took 40–45 days. In recent studies, BBO has shown excellent performance in real-world black-box optimization problems (Burger et al., 2020; Gongora et al., 2020; HamediRad et al., 2019). We integrated an experimental design module based on BBO to effectively search for the optimal experimental parameters that maximize the pigmentation scores in the search space defined in Figure 3B.

The Bayesian optimization module generates queries using two components: the Model updater, which updates the surrogate model that captures the relationship between parameters and the scores using Bayesian inference (Figure 3—figure supplement 1); the Query generator, which generates the next experimental parameters $X_{next}$ using an acquisition function and a policy function (Figure 3C, Figure 3—figure supplement 2; Algorithm 1–3). In the Query generator, the acquisition function estimates the expected progress toward the optimal experimental parameter at a given experimental parameter (Figure 3D). Then, using the acquisition function, the policy function generates the next 48 experimental parameters $X_{next}$ considering the context of trypsin processing time $x_{DP}$ (Figure 3E).

<table>
  <thead>
    <tr>
      <th>Algorithm 1. Batch Bayesian Optimization for iPSC-RPE differentiation protocol.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Input: The search space χ, GP prior (μ0,σ0,k), number of rounds M, number of Plates P, number of Wells W, DatasetD={(xi,yi)}i=1nfor t=1 to M do 1. Construct GP posterior (μt,σt,k) using D. 2. Get the acquisition function α(x;D). 3. Generate a experiment parameter set Xnext using the policy function. Execute the experiments f(Xnext) . Append the experiment results to past data D=D∪{(Xnext,f(Xnext))}. 4. Compute optimal context cDP on Detatch trypsin Period in the next experiment.end</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Algorithm 2. The policy function for the iPSC-RPE differentiation protocol.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Input: The acquisition function α(x;D), number of Plates P, number of Wells WOutput: The next experiment parameter set Xnext={(xt,p,w)}(p,w)=1(P,W) 1. Calculate utility functions from the acquisition function   α~0(x;D)←g(α(x;D))α~(x;D)←α~0(x;D) 2. Generate next experiment parameters Xnext={(xt,p,w)}(p,w)=1(P,W) in Maximization-Penalization loop for P=1 to P do  for w=1 to W do   1. maximization-step: xt,p,w←argmaxx∈χ{α~(x;D)}    2. penalization-step: α~(x;D)←α~0(x;D)∏(k,h)=1(p,w)φ(x;xt,k,h,L^)  endend</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Algorithm 3. Detachment trypsin period adjustment on the iPSC-RPE differentiation protocol.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Input: The acquisition function α(x;D), current DP context cDP,t, context shift width Δc Output: The next DP context cDP, t+1 1. Candidates of DP context ranges for the next round. (In this study, Δc = 3 min)cDP←cDP,tcDP−←cDP,t−ΔccDP+←cDP,t+Δc2. Calculate values V, V-, V+ that accumulate α(x;D) on each context ranges cDP, cDP−, cDP+ V=∑i∫χα(x;D,xDP=cDP,i)V−=∑i∫χα(x;D,xDP=cDP,i−)V+=∑i∫χα(x;D,xDP=cDP,i+) 3. Calculate ratios R−, R+ between each values defined above.R−=V−/VR+=V+/V 4. Choose the next DP context cDP, t+1 in following rules.if (max R−,R+&lt;1.05) then cDP, t+1←cDPendelse if (R−&gt;R+) then   cDP, t+1←cDP−endelse if (R−≤R+) then cDP, t+1←cDP+end</td>
    </tr>
  </tbody>
</table>

To test the performance of the Bayesian optimization module in our case, we executed a preliminary performance validation using a toy testing function constructed on domain knowledge (Figure 3—figure supplements 3 and 4).

### Robotic optimization drastically improved the pigmentation score

In this study, three successive experiments were conducted to optimize the target protocol. In each round, 48 conditions were generated using the Bayesian optimization module and translated into LabDroid operating programs. The robot performed 40 days of iPSC-RPE induction culture under each condition, and we obtained the rate of pigmented cells in the dish as an evaluation score (pigmentation score) for each condition. In accordance with the experimental design, we incorporated the two highest-scoring conditions from the previous experiment (Figure 2E) as control conditions, performed differentiation-inducing cultures with the LabDroid, and validated the area of the colored cells. In round 1, although one condition was found to be experimentally deficient, the other 47 conditions were validated. The highest score was 0.86 (Figure 4A; Figure 4—source data 1, Figure 4—source data 4), yielding five conditions that exceeded the mean value (0.39) for all wells in the baseline experiment (Figure 2E). In round 2, 46 conditions were generated, and the two highest-scoring conditions in round 1 were incorporated as control conditions. The highest score was 0.83 (Figure 4B; Figure 4—source data 2, Figure 4—source data 4). In round 3, 48 experiments were conducted, yielding an improved highest score of 0.91. We obtained 26 other conditions that were better than the highest in round 2 (Figure 4C; Figure 4—source data 3, Figure 4—source data 4). A visualization diagram of a two-dimensional partial least squares regression (PLS) clearly revealed that the overall experimental parameters tended to converge in a higher pigmented score direction from rounds 1 to 3 (Figure 4D, Figure 4—figure supplement 1).

![Figure 4.](https://cdn.elifesciences.org/articles/77007/elife-77007-fig4-v1.jpg)

**Figure 4.:** (A–C) Parameter candidates sorted in order of the pigmentation score in optimization rounds 1 (A), 2 (B), and 3 (C). The ID label on the left represents 'Round No. - Plate No. - Well No.'. For example, ‘1-2-3’ means ‘(Round) 1-(Plate) 2-(Well) 3’. The parameter values and resulting pigmentation scores are plotted as horizontal bars. The parameter candidate with black frames (1-1-3) in (A) is the standard condition. Arrows indicate the control experiments; the top two conditions in round 1 were included in round 2, and the top two conditions in round 2 were implemented in round 3. The raw values are shown in Figure 4—source data 4. (D) Visualization of the parameter set and the pigmentation score distributions using partial least squares regression (PLS) in each round. The horizontal axis PC1 shows the values of the parameter candidates that are projected onto the first component of the PLS. The vertical axis shows the pigmentation score for each candidate parameter. As the rounds progressed, the overall score tended to converge in a higher direction. A full visualization of the experimental results using a parallel coordinate plot (PCP) is shown in Figure 4—figure supplement 1.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/77007/elife-77007-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** The experimental results were visualized in rounds 1–3 using a parallel coordinate plot (PCP) and represented in 8-dimensional space (seven-dimensional parameters +pigmentation scores) as a colored line with vertices on the parallel axes; the position of the vertex on the i-th axis corresponds to the i-th coordinate of the parameter. The color of the line represents the pigmented score: blue lines represent lower pigmentation scores, and the closer to red, the higher the pigmented score.

To determine whether the optimized conditions were statistically improved over the pre-optimized conditions, an additional multi-well validation experiment was conducted after round 3 using the top five conditions in round 3 and the pre-optimized conditions. The validation values, ordered by place, were 0.71±0.06, 0.72±0.03, 0.76±0.02, 0.79±0.02, and 0.81±0.02 (mean ± SEM, n=3 each). All scores after optimization were statistically significantly higher than the pre-optimization scores (0.43±0.02; mean ± SEM, n=3) (Figure 5A and B; Figure 5—source data 1, Figure 5—source data 2).

![Figure 5.](https://cdn.elifesciences.org/articles/77007/elife-77007-fig5-v1.jpg)

**Figure 5.:** (A) The pigmentation score evaluation of the pre-optimized conditions (n=3) and the top five conditions from round 3. Error bars represent the standard error of the mean (SEM). The numbers 1–5 in the optimized group represent the first to fifth place conditions for round 3 (Figure 4C). Circles represent an individual score, bars represent the mean score, and error bars represent the SEM. Statistical significance was examined using two-way ANOVA and SNK post-hoc tests. p<0.05 was considered significant. ***p<0.001 versus pre-optimized. In all other combinations, no statistical significance was detected. Raw values are shown in Figure 5—source data 2. (B) Representative pigmented images of the pre-optimized and five optimized iPSC-RPE cells. Images acquired on DDay 34. ID labeling on the bottom reads 'V (validation) - Plate No. - Well No.'. The other images are shown in Figure 5—source data 1. (C–F) Cell biological validation of the robot-induced RPE cells. After DDay 34, cells were purified, stocked, initiated, maintained for four weeks, and analyzed (Figure 1—figure supplement 1B). (C) Representative marker gene expression in RPE cells by RT-PCR. iPSC, undifferentiated iPSC; H-RPE (Lonza), Clonetics H-RPE (Lot #493461, Lonza, USA); pre-optimized and optimized LabDroid-induced RPE. (D–E) Quantification of representative secreted proteins from iPSC-RPE cells using ELISA. The supernatants were collected and the amount of VEGF (D) and PEDF (E) in the culture medium was analyzed 24 hr after medium exchange (n=3 wells each). Circles represent individual scores, bars represent the mean score, and error bars represent SEM. n.d.=not detected. The raw values are shown in Figure 5—source data 3. (F) Co-staining of ZO-1 (green) and MITF (magenta) using immunohistochemistry. Nuclei were stained with DAPI. The scale bars represent 20 µm.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/77007/elife-77007-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** Example pictures of the monitoring cameras. (A–B) Wide-angle cameras for 24×7 monitoring. Front camera (A) and back camera (B). (C–D) Magnifying cameras that record only when the robot is running. Right camera (C) and left camera (D). (E) Live streaming camera (available to research contributors only, no recordings).

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/77007/elife-77007-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** Robotic experiments were conducted for 185 days, with a total robot operating time of 995 hr, 39 min, and 21 s (Figure 5—source data 5). Each round consisted of 73 jobs, and five rounds were performed, including baseline and validation. The total number of jobs executed by the LabDroid was 365, of which 343 were successful on the first try; 22 required human intervention at least once. The job success rate was 93.973%. One job consisted of multiple commands. The total number of commands that the LabDroid was ordered to execute was 75039, of which 75,011 were successful on the first try, 25 required human intervention at least once, and 3 were aborted. The command success rate was 99.963%. The reasons for the errors included micropipette tip loading error, 4 commands; micropipette tip ejection error, 7 commands; microscope and its control PC-derived errors, 13 commands (including 3 aborted commands); defective labware, 1 command; and human error, 3 commands. The errors occurred on the following dates: 2019 Feb (baseline), 11 commands; 2019 Apr (round 1), 11 (including three aborted commands); 2019 Jul (round 2), 4; 2020 Jan (round 3), 0; and 2020 Mar (validation), 2. The number of motions requiring the use of micropipettes that the LabDroid was ordered to execute was 39421; the rate of failure of either tip loading or ejection was 0.0279%. The vertical and horizontal axes represent the causes and error timing of the errors that occurred during the robotic experiments, respectively. Each circle represents one error.

In summary, we conducted 216 40-day cell culture experiments with a total experimentation time of 8640 days. We accelerated the search using a BBO technique, compressing the search time to 185 days with a cumulative robot operating time of 995 hr (Figure 5—source data 5; Figure 5—figure supplements 1 and 2; Figure 4—videos 1–5).

In this study, we succeeded in replacing part of the process of iPS cell differentiation into RPE cells for transplantation using robots, and demonstrated an effective optimization method (Figure 1—figure supplement 2). However, it was unclear whether robot-manufactured RPE cells would have the characteristics required for transplantation. Therefore, we purified the cells of the validation round, prepared them for transplantation, and performed a biological quality evaluation (Figure 1—figure supplement 1B). The analyzed iPSC-RPE cells expressed BEST1, RPE65, and CRALBP (Figure 5C), which are characteristic marker genes of RPE cells. In addition, we observed secretion of VEGF and PEDF into the culture medium, a characteristic of RPE cells (Figure 5D and E; Figure 5—source data 3). The expression of tight junction-associated factor ZO-1 was examined using immunohistochemistry, and a ZO-1-derived fluorescence signal was observed in microphthalmia-associated transcription factor (MITF)-positive cells, which play a central role in RPE cell function (Figure 5F). These results indicated that the robot-manufactured iPSC-RPE cells had the characteristics of RPE cells, and fulfilled the criteria for use in regenerative medicine research using the type of analysis measured in a previous clinical study (Mandai et al., 2017).

## Discussion

In this study, we proposed a robotic search system to autonomously search for optimal cell culture conditions, bringing together experimental robotics and BBO. Our robotic search system autonomously discovered the optimal combination of seven parameters comprising the iPSC-RPE induction process (target process) required to increase the number of pigmented cells (pigmentation score). Our approach can be applied to cell culture protocols other than iPSC-RPE induction; however, it may not be optimal even when implemented with a completely identical hardware-software setup. Below, we discuss some considerations and potential limitations for tailoring the components of our robotic search system (robots, parameters, and evaluation scores) to other targets.

Robots: the requirements depend on the nature of the target process. The search parameters must be changeable (flexibility), non-search parameters must remain stable or change only within the range of the specifications (reliability), and the operation must be sufficiently repeatable (accuracy). In addition, the storage capacity for CO2 incubators and refrigerators needs to be set in accordance with the number of cell plates that are to be cultured concurrently. For target processes that require long-term culture (i.e. processes that have high retry costs) such as cell differentiation induction, the robots and peripheral equipment need to have low error rates. In target processes that have low retry costs, a lower priority on low error rates is required. We chose LabDroid for this research, as it meets these requirements and has good future operational extensibility.

Parameters: the number and range of searchable parameters is constrained by the number of experiments that can be performed. The more parameters to be searched, the greater the number of experiments required for sufficient optimization. The available experimental resources (number of iterations or parallel cultures) should be considered in advance for appropriate parameter optimization. Here, we limited the scope of our search to just seven parameters (Table 1). However, a myriad of potential parameter candidates, including other chemicals, culture media, and order of manipulations, can be considered. During parameter selection, we referred to previous cell culture studies and expert opinions, as well as preliminary simulations, to confirm that optimization was sufficiently feasible with our resources (Figure 3—figure supplement 4). The search ranges for the seven parameters were carefully selected for our target process; different appropriate search ranges should be selected in case of other target processes, including the induction of differentiation into other types of tissues.

Evaluation scores: since the optimization is performed on the evaluation scores, designing the evaluation function is critical. Here, we used the pigmentation score as the evaluation score because of the following reasons: when preparing iPSC-RPE cells for transplantation in clinical research, a clinical team evaluates the rate of pigmented cells, gene expression, and secretory substances in cells subjected to differentiation induction followed by purification (Figure 1—figure supplement 1A). This quality assessment is not based on a total score, and only those cells that satisfy all the criteria in all items are suitable for transplantation (Kuroda et al., 2019; Mandai et al., 2017; Regent et al., 2019). Because cell pigmentation is one of the criteria for the assessment, cell pigmentation alone is not sufficient to determine cell quality, but can be a requirement. It should be noted that the pigmentation score does not reflect the degree of pigmentation in individual cells, but indicates the number of cells in the dish whose pigmentation is above the threshold. Since pigmented cells and non-pigmented cells are mixed in the dishes at the end of the induction (i.e. before purification), single-cell omics analysis is needed to accurately evaluate the quality of individual cells. For example, in stem cells, a value (stemness index) has been proposed to evaluate stemness from single-cell mRNA-seq information (Gulati et al., 2020). We believe that if a similar index for iPSC-RPE cells indicating cell quality from transcriptome data is established, this could replace the pigmentation score that we used, and would make the process we have developed even more ideal.

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
      <td>Cell line (Homo-sapiens)</td>
      <td>hiPSC 253G1</td>
      <td>RIKEN BRC</td>
      <td>HPS0002</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-ZO-1 (Rabbit polyclonal)</td>
      <td>Thermo Fisher Scientific Inc.</td>
      <td>61–7300</td>
      <td>IHC (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-MITF (Mouse monoclonal)</td>
      <td>Abcam plc.</td>
      <td>ab80651</td>
      <td>IHC (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa Fluor 488 Goat Anti-rabbit IgG (Goat polyclonal)</td>
      <td>Thermo Fisher Scientific Inc.</td>
      <td>A-11034</td>
      <td>IHC (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa Fluor 546 Goat Anti-mouse IgG (Goat polyclonal)</td>
      <td>Thermo Fisher Scientific Inc.</td>
      <td>A-11030</td>
      <td>IHC (1:1000)</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>BEST1 (+)</td>
      <td>This paper</td>
      <td>RT-PCR primers</td>
      <td>TAGAACCATCAGCGCCGTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>BEST1 (−)</td>
      <td>This paper</td>
      <td>RT-PCR primers</td>
      <td>TGAGTGTAGTGTGTATGTTGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>RPE65 (+)</td>
      <td>This paper</td>
      <td>RT-PCR primers</td>
      <td>TCCCCAATACAACTGCCACT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>RPE65 (−)</td>
      <td>This paper</td>
      <td>RT-PCR primers</td>
      <td>CCTTGGCATTCAGAATCAGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>CRALBP (+)</td>
      <td>This paper</td>
      <td>RT-PCR primers</td>
      <td>GAGGGTGCAAGAGAAGGACA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>CRALBP (−)</td>
      <td>This paper</td>
      <td>RT-PCR primers</td>
      <td>TGCAGAAGCCATTGATTTGA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>GAPDH (+)</td>
      <td>This paper</td>
      <td>RT-PCR primers</td>
      <td>ACCACAGTCCATGCCATCAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>GAPDH (−)</td>
      <td>This paper</td>
      <td>RT-PCR primers</td>
      <td>TCCACCACCCTGTTGCTGTA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>RNeasy Micro Kit</td>
      <td>QIAGEN</td>
      <td>74004</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>SuperScript III</td>
      <td>Thermo Fisher Scientific Inc.</td>
      <td>18080–044</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>VEGF Human ELISA Kit</td>
      <td>Thermo Fisher Scientific Inc.</td>
      <td>BMS277-2</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>PEDF Human ELISA Kit</td>
      <td>BioVendor</td>
      <td>RD191114200R</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>PD 173074</td>
      <td>Merck &amp; Co., Inc.</td>
      <td>P2499-5MG</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>CultureSure Y-27632</td>
      <td>FUJIFILM Wako Pure Chemical Corporation</td>
      <td>036–24023</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>SB 431542 hydrate</td>
      <td>Merck &amp; Co., Inc.</td>
      <td>S4317-5MG</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>CKI-7 dihydrochloride</td>
      <td>Merck &amp; Co., Inc.</td>
      <td>C0742-5MG</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>LabDroid_optimizer</td>
      <td>This paper</td>
      <td></td>
      <td>Available at our Github (see Data and code availability)</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>StemFit AK02N</td>
      <td>Ajinomoto Co., Inc.</td>
      <td>AK02N</td>
      <td>see Materials and Methods &gt;Reagents</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>knockOut serum replacement (KSR)</td>
      <td>Thermo Fisher Scientific Inc.</td>
      <td>10828028</td>
      <td>see Materials and Methods &gt;Reagents</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>FBS</td>
      <td>Nichirei Corporation</td>
      <td>12007C</td>
      <td>see Materials and Methods &gt;Reagents</td>
    </tr>
  </tbody>
</table>

### Guidelines

All experiments that involved the use of human-derived samples were reviewed and approved by the institutional review board of the Institutional Committee of RIKEN Kobe Branch (#Kobe1 2019–05 (3)).

### Reagents

hiPSC maintenance medium: 80% StemFit Basal Solution A and 20% StemFit iPS Expansion Solution B (#AK02N, Ajinomoto Co., Inc, Japan).

RPE differentiation medium (20% KSR): 0.10 mM MEM non-essential amino acids solution (NEAA) (#11140050, Thermo Fisher Scientific Inc, MA, USA), 1.0 mM sodium pyruvate (#S8636, Merck & Co., Inc, NJ, USA), 19% knockOut serum replacement (KSR) (#10828028, Thermo Fisher Scientific Inc, MA, USA), 0.0007% 2-mercaptoethanol (#139–06861, FUJIFILM Wako Pure Chemical Corporation, Japan), 78 U/mL benzylpenicillin sodium, and 78 µg/mL streptomycin sulfate (#15140122, Thermo Fisher Scientific Inc, MA, USA). All diluted in GMEM (#11710035, Thermo Fisher Scientific Inc, MA, USA).

RPE differentiation medium (15% KSR): 0.10 mM MEM NEAA (#11140050, Thermo Fisher Scientific Inc, MA, USA), 0.99 mM sodium pyruvate (#S8636, Merck & Co., Inc, NJ, USA), 15% KSR (#10828028, Thermo Fisher Scientific Inc, MA, USA), 0.0007% 2-mercaptoethanol (#139–06861, FUJIFILM Wako Pure Chemical Corporation, Japan), 82 U/mL benzylpenicillin sodium, and 82 µg/mL streptomycin sulfate (#15140122, Thermo Fisher Scientific Inc, MA, USA). All diluted in GMEM (#11710035, Thermo Fisher Scientific Inc, MA, USA).

RPE differentiation medium (10% KSR): 0.094 mM MEM NEAA (#11140050, Thermo Fisher Scientific Inc, MA, USA), 0.94 mM sodium pyruvate (#S8636, Merck & Co., Inc, NJ, USA), 10% KSR (#10828028, Thermo Fisher Scientific Inc, MA, USA), 0.0007% 2-mercaptoethanol (#139–06861, FUJIFILM Wako Pure Chemical Corporation, Japan), 85 U/mL benzylpenicillin sodium, and 85 µg/mL streptomycin sulfate (#15140122, Thermo Fisher Scientific Inc, MA, USA). All diluted in GMEM (#11710035, Thermo Fisher Scientific Inc, MA, USA).

RPE maintenance medium: 29% Nutrient Mixture F-12 (#N6658, Merck & Co., Inc, NJ, USA), 1.9 mM L-glutamine (#G7513, Merck & Co., Inc, NJ, USA), 1.9% B-27 supplement, serum free (#17504044, Thermo Fisher Scientific Inc, MA, USA), 96 U/mL benzylpenicillin sodium, and 96 µg/mL streptomycin sulfate (#15140122, Thermo Fisher Scientific Inc, MA, USA). All diluted in DMEM (Low glucose) (#D6046, Merck & Co., Inc, NJ, USA).

FGF receptor inhibitor (FGFRi) stock: PD 173074 (#P2499-5MG, Merck & Co., Inc, NJ, USA) diluted in DMSO (#D2650−5X5ML, Merck & Co., Inc, NJ, USA).

Rho-kinase inhibitor (Y) stock (8–10 mM): CultureSure Y-27632 (#036–24023, FUJIFILM Wako Pure Chemical Corporation, Japan) diluted in distilled water (Otsuka Pharmaceutical Factory, Japan) to a final 10 µM concentration when added to the cell culture medium.

TGF-β/Activin/Nodal signal inhibitor (SB) stock (4–5 mM): SB 431542 hydrate (#S4317-5MG, Merck & Co., Inc, NJ, USA) diluted in DMSO (#D2650−5X5ML, Merck & Co., Inc, NJ, USA) to a final 5 µM concentration when added to the cell culture medium.

Wnt signal inhibitor (CKI) stock (2.4–3 mM): CKI-7 dihydrochloride (#C0742-5MG, Merck & Co., Inc, NJ, USA) diluted in distilled water (Otsuka Pharmaceutical Factory, Japan) to a final 3 µM concentration when added to the cell culture medium.

RPE adhesion medium: DMEM/F12 (D8437, Merck & Co., Inc, NJ, USA), 10% FBS (12,007C, Nichirei Corporation, Japan).

RPE washing solution: 98% DMEM/F12 (D8437, Merck & Co., Inc, NJ, USA), 1 mM sodium pyruvate (S8636, Merck & Co., Inc, NJ, USA), 2 mM L-glutamine (G7513, Merck & Co., Inc, NJ, USA).

### Labware

For human use: micropipette tip, 2140-05-HR/2149P-05/61849, Thermo Fisher Scientific Inc (MA, USA); micropipette tip, 30389165, Mettler Toledo (OH, USA); micropipette tip, 737251, Greiner Bio-One International GmbH (Germany); disposable pipette, 356507, Corning Incorporated (NY, USA); disposable pipette, 606160/607160/760160/768160, Greiner Bio-One International GmbH (Germany); filtration, SLGVJ13SL, Merck & Co., Inc (NJ, USA); filtration, SS-10LZ, Terumo Corporation (Japan); filtration, 431096/430281/431097/430282, Corning Incorporated (NY, USA); 1.5 mL tube, 72.692MS, Sarstedt K.K. (Japan); 15 mL tube, 352096, Corning Incorporated (NY, USA); 50 mL tube, 352070, Corning Incorporated (NY, USA).

For LabDroid use: 6-well plate, 353046, Corning Incorporated (NY, USA); 50 mL tube, MS-58500, Sumitomo Bakelite Co., Ltd. (Japan); micropipette tip, 3511-05-HR/3512-05-HR/94410313/94410713/94052550, Thermo Fisher Scientific Inc (MA, USA).

### LabDroid Maholo booth

LabDroid including peripheral equipment were placed inside a booth made of acrylic walls and a stainless steel frame with three fan-filter-units (Figure 2—figure supplement 1). The LabDroid booth included a dual-arm humanoid (Robotic Biology Institute Inc, Japan), a CO2 incubator (APC-30D, ASTEC Co., Ltd., Japan), micropipettes (4641110N/4641030N/4641230N/4641210N, Thermo Fisher Scientific Inc, MA, USA), a tube rack (Robotic Biology Institute Inc, Japan), a plate rack (Robotic Biology Institute Inc, Japan), a dry bath (EC-40RA, AS ONE Corporation, Japan), a tip sensor (Robotic Biology Institute Inc, Japan), an aspirator (SP-30, Air Liquide, Italy), a dust bin (EPD3S, Sekisui Techno Moulding Co., Ltd., Japan), and a microscope (EVOS FL Auto 2, Thermo Fisher Scientific Inc, MA, USA).

### hiPSC culture — initiation and preparation of cell suspensions (human part)

The hiPSC line 253G1 (Nakagawa et al., 2008), made from human dermal fibroblasts, was obtained from RIKEN BRC (HPS0002). The hiPSCs were cultured and differentiated using the method previously described (Haruta et al., 2004; Kawasaki et al., 2002; Osakada et al., 2008). Mycoplasma contamination tests were performed periodically during the study and the results were always negative.

On DDay −14, frozen hiPSCs were initiated using the following procedures: first, laminin-coated 6-well plates were prepared. A final concentration of 0.5 µg/cm2 iMatrix-511 (Matrixome Inc, Japan) diluted in PBS (-) was then added to each well of the four 6-well plates and incubated for a minimum of 60 min at 37 °C and 5% CO2, after which 0.75 mL/well of hiPSC maintenance medium was added. The supernatant was then removed. Next, 1 mL/well of hiPSC maintenance medium containing Rho-kinase inhibitor (final 10 µM concentration) was added, and the coated plates were incubated at 37 °C and 5% CO2 until further use.

For hiPSC initiation, frozen vials of hiPSCs stored in liquid nitrogen were thawed in a water bath set at 37 °C, and the cells were subsequently suspended in 5 mL of hiPSC maintenance medium. After centrifugation (160×g, 22 °C, 4 min), the supernatant was removed and an appropriate volume of hiPSC maintenance medium with a final 10 µM Rho-kinase inhibitor concentration was added. After counting the cells with a hemocytometer, the cells were seeded into laminin-coated 6-well plates at 43,300–45,000 cells/1.5 mL medium/well.

On DDay −13, the medium was replaced with hiPSC maintenance medium without Rho-kinase inhibitor. On DDays −12 to −8, the medium was replaced with the same medium composition at 24–72 hr intervals. On DDay −7, cells were collected from the plate, and cell suspensions were delivered to the LabDroid booth. The medium was aspirated and 2 mL/well of PBS (-) was gently added and then aspirated for washing, followed by addition of 1 mL of 0.5 x TrypLE Select CTS (#A12859-01, Thermo Fisher Scientific Inc, MA, USA) diluted in 0.5 mM EDTA/PBS (-) and incubated at 37 °C and 5% CO2 for 10–20 min. Then, cells were detached by pipetting and collected into a 50 mL tube, to which 1 mL of hiPSC maintenance medium and 3 mL of PBS (-) were added. After centrifugation (160×g, 22 °C, 4 min), the supernatant was removed, 0.75 mL of hiPSC maintenance medium with 10 µM Rho-kinase inhibitor was added, and the cells were resuspended. The cell suspension was filtered through a 40 µm cell strainer (#352340, Corning Incorporated, USA) with an additional 0.75 mL of hiPSC maintenance medium. After counting the cells with a hemocytometer, the cell suspension was set to 133,400 cells/20 mL with hiPSC maintenance medium containing 10 µM Rho-kinase inhibitor in eight 50 mL tubes. To prepare the cell suspensions, eight 6-well plates coated with laminin were prepared. A final concentration of 0.5 µg/cm2 of iMatrix-511 (Matrixome Inc, Japan) diluted in PBS (-) was added to each well of four 6-well plates and incubated for a minimum of 60 min at 37 °C and 5% CO2.

### iPSC-RPE differentiation (LabDroid part)

On DDay −7, the hiPSC suspension was seeded into eight 6-well plates by coating eight 6-well plates with laminin, and placing eight tubes of the iPSC suspension and labware in the appropriate positions. The task of seeding was initiated, and the robotic operation was performed by LabDroid (Figure 2—figure supplements 2A and 3; Figure 4—video 1). After the robotic operation, the eight cell-seeded plates were exported and incubated in a CO2 incubator outside the LabDroid booth.

On DDay −6, the eight seeded plates were imported into the CO2 incubator of the LabDroid booth. The users prepared eight 50 mL tubes of hiPSC maintenance medium with a final 10 µM Rho-kinase inhibitor concentration and two 50 mL tubes of hiPSC maintenance medium with final 5 µM FGFRi and 10 µM Rho-kinase inhibitor concentrations. The reagents and labware were placed in the appropriate positions. The task of preconditioning was then initiated, and the robotic operation was performed by LabDroid (medium exchange type I; Figure 2—figure supplements 2B and 4; Figure 4—video 2).

On DDays −5 to −1, the users prepared eight 50 mL tubes of hiPSC maintenance medium without Rho-kinase inhibitor and two 50 mL tubes of hiPSC maintenance medium with a final 5 µM FGFRi concentration. The reagents and labware were placed in the appropriate positions. The task of preconditioning was initiated, and the robotic operation was performed by LabDroid (medium exchange type I; Figure 2—figure supplements 2B and 4; Figure 4—video 2).

On DDay 0, the following procedure was used for the operation of four plates: the users prepared four 6-well plates coated with laminin. A final 0.5 µg/cm2 concentration of iMatrix-511 (Matrixome Inc, Japan) diluted in PBS (-) was added to each well of the four 6-well plates and then the plates were incubated for a minimum of 60 min at 37 °C and 5% CO2. The users also prepared two 50 mL tubes of PBS (-), two 50 mL tubes of 0.5 x TrypLE Select CTS (#A12859-01, Thermo Fisher Scientific Inc, MA, USA) diluted in 0.5 mM EDTA/PBS (-), and four plates with RPE differentiation medium (20% KSR) with final 10 µM Rho-kinase inhibitor/3 µM Wnt signal inhibitor/5 µM TGF-β/Activin/Nodal signal inhibitor (4 mL/well each) concentration. The cell plates, laminin-coated plates, plates with medium, reagents, and labware were placed in the appropriate positions. The task of passage was initiated, and robotic operations were performed by LabDroid (Figure 2—figure supplements 2D and 5; Figure 4—video 3). After performing this operation twice (four plates each), the eight cell-passaged plates were exported and incubated in a CO2 incubator outside the LabDroid booth.

On DDay 1, the eight cell-passaged plates were imported into the CO2 incubator of the LabDroid booth. Users prepared eight 50 mL tubes of RPE differentiation medium (10% KSR), two 50 mL tubes of 100% KSR, one 50 mL tube of 4 mM Rho-kinase inhibitor stock/1.2 mM Wnt signal inhibitor stock, and one 50 mL tube of 4 mM TGF-β/Activin/Nodal signal inhibitor stock. The reagents and labware were placed in the appropriate positions. The task of RPE differentiation was initiated, and the robotic operation was performed by LabDroid (medium exchange type I; Figure 2—figure supplements 2B and 6; Figure 4—video 4).

On DDays 2–19, the users prepared eight 50 mL tubes of RPE differentiation medium (10% KSR), two 50 mL tubes of 100% KSR, one 50 mL tube of 4 mM Rho-kinase inhibitor stock/1.2 mM Wnt signal inhibitor, and one 50 mL tube of 4 mM TGF-β/Activin/Nodal signal inhibitor. The reagents and labware were placed in the appropriate positions. The task of RPE differentiation was initiated, and the robotic operation was performed by LabDroid (medium exchange type I; Figure 2—figure supplements 2B and 6; Figure 4—video 4).

On DDays 20–32, the users prepared eight 50 mL tubes of RPE differentiation medium (10% KSR; DDays 10–25) or RPE maintenance medium (DDays 26–32). The reagents and labware were placed in the appropriate positions. RPE differentiation and maintenance were initiated and the robotic operations were performed by LabDroid (medium exchange type II; Figure 2—figure supplements 2C and 7; Figure 4—video 5).

### Scoring — sampling (human part)

On DDay 33, the cell plates were exported and the cell culture medium was replaced with fresh RPE maintenance medium. After 24 hr (DDay 34), the medium was collected for ELISA analysis. The remaining media were aspirated and 2 mL of PBS (-) were added and then aspirated for washing. After that, photographic images were acquired for the calculation of scoring values.

### Scoring — image analysis (human part)

Images were acquired using a digital camera (PSG7X MARKII, Canon Inc, Japan): ISO 500; focal length F=9.00, 50 mm; exposure time, 1/1250 s. The camera was set in the same position throughout all experiments. The acquired images were automatically processed by filtering with Gaussian blur, subtracting the background, binarizing by thresholding with a constant value, and cropping with a constant pixel value. The colored cell area was then calculated (Figure 2—figure supplement 8).

### Purification and storage (human part)

Purification of iPSC-RPE cells was conducted using the same protocol described in a study previously reported (Mandai et al., 2017). When the RPE colonies reached an appropriate size, the cells were suspended in RPE maintenance medium and kept as a floating culture for about 10 days in a low cell adhesion plate (MS-90600Z, Sumitomo Bakelite Co., Ltd., Japan). Under the microscope, colonies consisting only of black RPE cells were selected. Then, they were transferred to 12-well plates coated with iMatrix, and cultured in RPE adhesion medium/RPE maintenance medium (1:1). Once the RPE cell colonies became attached to the dish, they were cultured in RPE maintenance medium with basic fibroblast growth factor (bFGF), which was changed every 2–3 days.

After 10–12 days of cell selection, unsuitable cells were removed, and the cells were passaged. The medium was aspirated and 1 mL of RPE washing solution was added and aspirated again for washing. Then, 0.5 mL of RPE washing solution was added and atypical cells were eliminated using micropipette tips under microscope observation. After the removal process, the medium was aspirated, 1 mL/well of PBS (-) was added and aspirated for washing, and then 0.5 mL of Trypsin-EDTA solution (203–20251, FUJIFILM Wako Pure Chemical Corporation, Japan) was added, followed by incubation at RT and 5% CO2 for 8–10 min. Cells were detached by pipetting and collected into a 50 mL tube. After centrifugation (280×g, 25 °C, 4 min), the supernatant was removed, and the pellet was resuspended in 1 mL/plate of RPE adhesion medium/RPE maintenance medium (1:1) and filtered through a 40 μm cell strainer (352340, Corning Incorporated, NY, U.S.A.). After counting the cells with a hemocytometer, the cells were seeded into 12-well plates. The medium was changed to RPE maintenance medium with bFGF.

After 1–3 days of cell passage, the medium was aspirated, the cells were washed with 0.5 mL of RPE maintenance medium, and 1 mL of RPE maintenance medium containing 10 ng/mL bFGF and 0.5 µM SB431542 was added. This medium was exchanged every 2–3 days.

The cells were stored when they formed hexagonal shapes after sufficient confluency. For that, the medium was aspirated, 1 mL/well of PBS (-) was added and then aspirated for washing, and 0.5 mL of Trypsin-EDTA solution (203–20251, FUJIFILM Wako Pure Chemical Corporation, Japan) was added, followed by incubation at 37 °C and 5% CO2 for 10–15 min. After adding >0.5 mL of RPE adhesion medium, the cells were detached using a cell scraper (MS-93100, Sumitomo Bakelite Co., Ltd., Japan). The cell suspension was filtered through a 40 μm cell strainer (352340, Corning Incorporated, NY, USA) and then centrifuged for 4 min at 280×g to obtain a cell pellet. The pellet was resuspended in 1 mL of RPE adhesion medium/RPE maintenance medium (1:1) and filtered through a 40 μm cell strainer. After counting the cells with a hemocytometer, the cell suspension was centrifuged for 4 min at 280×g to obtain a cell pellet. Then, STEM-CELLBANKER (CB047, Zenoaq Resource Co., Ltd., Japan) was added until a cell concentration of 500,000 cells/0.5 mL/tube, and the cell suspensions were dispensed into cryovials. The cryotubes were placed in a cell freezing container at −80 °C for 3–24 hr, and then stored at −150 °C.

### Initiation of iPSC-RPE stock and recovery culture (human part)

Frozen vials of RPE cells were thawed in a 37 °C water bath and suspended in 4.5 mL of RPE adhesion medium. After centrifugation (280×g, 25 °C, 4 min), the supernatant was removed and RPE adhesion medium/RPE maintenance medium (1:1) was added. After counting the cells with a hemocytometer, the cells were seeded into 24-well plates (0.5 mL/well).

After 1–3 days of cell seeding, the medium was aspirated, the cells were washed with 0.25 mL of RPE maintenance medium, and 0.5 mL/well of RPE maintenance medium containing 10 ng/mL bFGF and 0.5 µM SB431542 was added. This same type of medium was exchanged every 2–3 days.

Two weeks after seeding, the RPE cells were passaged. Two weeks after cell passage, the RPE cells were used for cell biological validation processes (RT-PCR, ELISA, and immunohistochemistry).

### Validation — RT-PCR (human part)

Total RNA was extracted from transfected cells using RNeasy Micro Kit (#74004, QIAGEN, Germany). First-strand cDNA synthesis was performed on 500–1000 ng of total RNA, using SuperScript III (#18080–044, Thermo Fisher Scientific Inc, MA, USA) according to the manufacturer’s instructions. Each mRNA transcript was amplified using PCR with the following primers:

### Validation — ELISA (human part)

The collected media were centrifuged (90×g, 4 °C, 1 min), and the supernatant was collected and stored at −80 °C. The amount of VEGF contained in the thawed medium was measured using the protocols and reagents from the VEGF Human ELISA Kit (BMS277-2, Thermo Fisher Scientific, USA), and the amounts of PEDF were measured using a Human ELISA Kit (RD191114200R, BioVendor, Czech Republic).

### Validation — Immunohistochemistry (human part)

Cells were washed with PBS (-), fixed in 15% paraformaldehyde for 1 hr at RT (approximately 25 °C), and stored at 4 °C after removal of PFA and addition of PBS (-). After removal of the solutions, cells were treated with 50 µL/well of 0.2% Triton X-100/PBS (-), incubated for 30 min at RT, washed with PBS (-), blocked with 50 µL of Blocking One (03953–95, Nacalai Tesque Inc, Japan), and incubated for 1 h at RT. After removal of the solutions, cells were stained at 4 °C o/n in 50 µL of the 1st antibody diluent (rabbit anti-ZO-1, 61–7300, Thermo Fisher Scientific Inc, MA, USA; anti-MITF, mouse anti-MiTF, ab80651, Abcam plc., Britain; antibody diluent, S2022, Agilent Technologies Inc, USA). After removal of the solutions, cells were washed with PBS (-) and then stained at RT for 1 hr in 50 µL of the 2nd antibody diluent (Alexa Fluor 546 Goat Anti-mouse IgG, A-11030, Thermo Fisher Scientific Inc, MA, USA; Alexa Fluor 488 Goat Anti-rabbit IgG, A-11034, Thermo Fisher Scientific Inc, MA, USA; antibody diluent, S2022, Agilent Technologies Inc, USA) with DAPI (1 µg/mL, D1206, Thermo Fisher Scientific Inc, MA, USA). After removal of the solutions, cells were washed with PBS (-), and then 50 µL of PBS (-) was added. Images of immunohistochemistry samples were acquired using an IX73 inverted microscope (Olympus, Japan).

### Bayesian optimization module

When no prior experimental results exist, the Bayesian optimization module generates the next query from random uniform sampling. When past experimental results are available, the Bayesian optimization module generates queries using two components: the Model updater and the Query generator (Figure 3C).

The Model updater updates the surrogate model to predict the experimental results given past experimental results: $D={(x_{i},y_{i})}_{i=1}^{n}$. We adopted Gaussian process regression (GPR, Figure 3—figure supplement 1) with the ARD-RBF kernel as the surrogate model to estimate the expected score and confidence level for all unevaluated experimental parameters. Based on the experimental results shown in Figure 2E, the observation noise was assumed to follow a zero-mean Gaussian noise with a variance of 0.0039 at all points in the search space. By using the surrogate model, the Query generator generates the next queries in two steps. In step 1, the Query generator constructs an acquisition function that estimates the expected progress toward the optimal experimental parameter at a given experimental parameter $x$ in the search space. We adopted the Expected improvement (EI) (Jones et al., 1998), a commonly used acquisition function in BO. EI estimates how much improvement over the current best score is expected from each point in the search space. In step 2, by using the acquisition function, the Query generator decides where to evaluate next, and our problem required the simultaneous performance of 48 experiments corresponding to 8 plates x 6 wells in each round. In addition, because the DP is a batch contextual parameter as described herein, a policy function that generates parameter sets taking such structural context into account must be incorporated. Therefore, we developed the Batch Contextual Local Penalization (BCLP) as a policy function to generate multiple points with context in parallel. The BCLP is a batch generation policy that extends the local penalization (Gonzalez et al., 2016) to be applied to cases where complex structural context parameters exist. As shown in Figure 3E, for each value of the contextual parameter DP in ascending order, BCLP iteratively generated the parameter by maximizing and penalizing the acquisition function 48 times to obtain the next experimental parameters $X_{next}$ for each subsequent well (Algorithm 1, 2). In addition, after each round, the more promising KP intervals were reconfigured by calculating the integral value of the acquisition function (Algorithm 3). We also replaced the queries that corresponded to the place of the top two pigmentation scores in the previous experiments with the parameter of the top two pigmentation scores in the previous experiments as a positive control. For more information about the optimization module, see the Appendix.

### Statistical analysis

Statistical analyses were performed by Wolfram Mathematica version 11.2.0.0. In this study, p<0.05 was considered significant (*p<0.05, **p<0.01, ***p<0.001, and n.s.=not significant).

### Data and code availability

All code that supports the findings of this study is available at https://github.com/labauto/LabDroid_optimizer, (copy archived at swh:1:rev:661ef792d4b7568a2e673178d9f1e6ed3c84ab1b, Tsuzuki, 2022). This code is based on GPyOpt (GPyOpt: Gaussian Process Optimization using GPy).
