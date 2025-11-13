# Inferring characteristics of bacterial swimming in biofilm matrix from time-lapse confocal laser scanning microscopy

## Authors

- Guillaume Ravel<sup>1</sup>
- Michel Bergmann<sup>3</sup>
- Alain Trubuil<sup>6</sup>
- Julien Deschamps<sup>7</sup>
- Romain Briandet<sup>7</sup> ([ORCID: 0000-0002-8123-3492](https://orcid.org/0000-0002-8123-3492))
- Simon Labarthe<sup>1</sup> ([ORCID: 0000-0002-5463-7256](https://orcid.org/0000-0002-5463-7256)) †

### Affiliations

1. University of Bordeaux, INRAE, BIOGECO Cestas France ([ROR:033ebya06](https://ror.org/033ebya06))
2. Inria, INRAE Talence France ([ROR:003vg9w96](https://ror.org/003vg9w96))
3. Memphis Team, INRIA Talence France ([ROR:02kvxyf05](https://ror.org/02kvxyf05))
4. University of Bordeaux, IMB, UMR 5251 Talence France ([ROR:05m3r1b84](https://ror.org/05m3r1b84))
5. CNRS, IMB, UMR 5251 Talence France ([ROR:02feahw73](https://ror.org/02feahw73))
6. Université Paris-Saclay, INRAE, MaIAGE Jouy-en-Josas France ([ROR:03xjwb503](https://ror.org/03xjwb503))
7. Université Paris-Saclay, INRAE, AgroParisTech, Micalis Institute Jouy-en-Josas France ([ROR:00gtg0p11](https://ror.org/00gtg0p11))

† Corresponding author

## Abstract

Biofilms are spatially organized communities of microorganisms embedded in a self-produced organic matrix, conferring to the population emerging properties such as an increased tolerance to the action of antimicrobials. It was shown that some bacilli were able to swim in the exogenous matrix of pathogenic biofilms and to counterbalance these properties. Swimming bacteria can deliver antimicrobial agents in situ, or potentiate the activity of antimicrobial by creating a transient vascularization network in the matrix. Hence, characterizing swimmer trajectories in the biofilm matrix is of particular interest to understand and optimize this new biocontrol strategy in particular, but also more generally to decipher ecological drivers of population spatial structure in natural biofilms ecosystems. In this study, a new methodology is developed to analyze time-lapse confocal laser scanning images to describe and compare the swimming trajectories of bacilli swimmers populations and their adaptations to the biofilm structure. The method is based on the inference of a kinetic model of swimmer populations including mechanistic interactions with the host biofilm. After validation on synthetic data, the methodology is implemented on images of three different species of motile bacillus species swimming in a Staphylococcus aureus biofilm. The fitted model allows to stratify the swimmer populations by their swimming behavior and provides insights into the mechanisms deployed by the micro-swimmers to adapt their swimming traits to the biofilm matrix.

## Introduction

Biofilm is the most abundant mode of life of bacteria and archaea on earth (Flemming and Wuertz, 2019; Flemming et al., 2016b). They are composed of spatially organized communities of microorganisms embedded in a self-produced extracellular polymeric substances (EPS) matrix. EPS are typically forming a gel composed of a heterogenous mixture of water, polysaccharides, proteins, and DNA (Flemming et al., 2016a). The biofilm mode of life confers to the inhabitant microbial community strong ecological advantages such as resistance to mechanical or chemical stresses (Bridier et al., 2011) so that conventional antimicrobial treatments remain poorly efficient against biofilms (Bridier et al., 2015). Different mechanisms were invoked such as molecular diffusion-reaction limitations in the biofilm matrix and the cell type diversification associated with stratified local microenvironments (Bridier et al., 2017). Biofilms can induce harmful consequences in several industrial applications, such as water (Beech and Sunner, 2004), or agri-food industry (Doulgeraki et al., 2017), leading to significant economic and health burden (Köck et al., 2010). Indeed, it was estimated that the biofilm mode of life is involved in 80% of human infection and usual chemical control leads to serious environmental issues (Bridier et al., 2011). Hence, finding efficient ways to improve biofilm treatment represents important societal sustainable perspectives.

Motile bacteria have been observed in host biofilms formed by exogenous bacterial species (Houry et al., 2012; Li et al., 2014; Piard et al., 2016; Flemming et al., 2016a). These bacterial swimmers are able to penetrate the dense population of host bacteria and to find their way in the interlace of EPS. Doing so, they visit the 3D structure of the biofilm, leaving behind them a trace in the biofilm structure, that is a zone of extracellular matrix free of host bacteria (Figure 1a and Appendix 1—figure 3). Hence, bacterial swimmers are digging a network of capillars in the biofilm, enhancing the diffusivity of large molecules (Houry et al., 2012), allowing the transport of biocide at the heart of the biofilm, reducing islands of living cells. The potentiality of bigger swimmers has also been studied for biofilm biocontrol, including spermatozoa (Mayorga-Martinez et al., 2021), protozoans (Derlon et al., 2012), or metazoans (Klein et al., 2016). Recent results suggest a deeper role of bacterial swimmers in biofilm ecology with the concept of microbial hitchhiking: motile bacteria can transport sessile entities such as spores (Muok et al., 2021), phages (Yu et al., 2021) or even other bacteria (Samad et al., 2017), enhancing their dispersion within the biofilm. Hence, characterizing microbial swimming in the very specific environment of the biofilm matrix is of particular interest to decipher biofilm spatial regulations and their biocontrol, but more generally in an ecological perspective of microbial population dynamics in natural ecosystems.

![Figure 1.](https://cdn.elifesciences.org/articles/76513/elife-76513-fig1-v2.jpg)

**Figure 1.:** (a) Temporal stacks of 2D images are acquired, with different fluorescence colors for host bacteria (Staphylococcus aureus, green) and swimmers (Bacillus pumilus, Bacillus sphaericus or Bacillus cereus, red). Bacterial swimmers navigate in a host biofilm and are tracked in the different snapshots. Swimmer trajectories are represented with white lines. High density and low density zones of host cells are visible in the biofilm (green scale). (b) Additionally to speed and acceleration distributions, three trajectory descriptors are considered. Distance is the total length of the trajectory path. Displacement is the distance between the initial and final points of the trajectory. Visited area is the total area of the pores left by the swimmer during its path. Hence, when a swimmer retraces its steps, the displacement is incremented but not the visited area. (c) Three different mechanisms are considered in the mechanistic model. Biofilm-dependant speed. A target speed is defined accordingly to the local density of biofilm and asymptotically reached after a relaxation time. Biofilm-dependent direction. Swimming direction is defined accordingly to the local biofilm density gradient. Random walk. A Brownian motion is added. (d) The image acquisition workflow is composed of a first step at the wet lab where host biofilm and swimmer are plated and imaged in different color channels. Then a post-processing phase recomposes the swimmer trajectories with tracking algorithms. Finally, temporal positions, speeds and accelerations are computed. On the biofilm channel, density and density gradient maps are processed at each time step.

Bacterial swimming is strongly influenced by the micro-topography and bacteria deploy strategies to sense and adapt their motion to their environment (Lee et al., 2021), with specific implications for biofilm formation and dynamics (Conrad and Poling-Skutvik, 2018). Model-based studies were conducted to characterize bacterial active motion in interaction with an heterogeneous environment. An image and model-based analysis showed non-linear self-similar trajectories during chemotactic motion with obstacles (Koorehdavoudi et al., 2017). Theoretical studies explored Brownian dynamics of self-propelled particles in interaction with filamentous structures such as EPS (Jabbarzadeh et al., 2014) or with random obstacles, exhibiting continuous limits and different motion regimes depending on obstacle densities (Chepizhko and Peruani, 2013; Chepizhko et al., 2013). Image analysis characterized different swimming patterns in polymeric fluids (Patteson et al., 2015), completed by detailed comparisons between a micro-scale model of flagellated bacteria in polymeric fluids and high-throughput images (Martinez et al., 2014). Models of bacterial swimmers in visco-elastic fluids were also developed to study the force fields encountered during their run (Li and Ardekani, 2016). However, to our knowledge, no study tried to characterize swimming patterns in the highly heterogeneous environment presented by an exogenous biofilm matrix.

In this study, we aim to provide a quantitative characterization of the different swimming behaviours in adaptation to the host biofilm matrix observed by microscopy. We focus on identifying potential species-dependent swimming characteristics and quantifying the swimming speed and direction variations induced by the host biofilm structure. To address these goals, three different Bacillus species presenting contrasted physiological characteristics are selected. First, different trajectory descriptors accounting for interactions with the host biofilm are defined, allowing to discriminate the swim of these bacterial strains by differential analysis. Then, a mechanistic random-walk model including swimming adaptations to the host biofilm is introduced. This model is numerically explored to identify the sensitivity of the trajectory descriptors to the model parameters. An inference strategy is designed to fit the model to 2D+T microscopy images. The method is validated on synthetic data and applied to a microscopy dataset to decipher the swimming behaviour of the three Bacillus.

## Results

### Ultrastuctural bacterial morphology

To investigate how the shape and propelling mechanism of bacteria can affect the way they navigate in a porous media such as a biofilm, we first image three bacterial swimmers –Bacillus pumilus (B. pumilus), Bacillus sphaericus (B. sphaericus), and Bacillus cereus (B. cereus) – by Transmitted Electron Microscopy (TEM) (Figure 2) to seek for potential structural and physiological differences. Important discrepancies can be observed between these Bacillus. First, they show noticeable difference in length and diameter, B. sphaericus being the longest bacteria by a factor of approximatively 1.5, and B. cereus and B. pumilus having similar size, but B. cereus showing a higher aspect ratio. Secondly, they do not have the same type of flagella: B. pumilus and B. sphaericus present several long flagella distributed over the whole surface of the membrane while B. cereus shows a unique brush-like bundle of very thin flagella, at its back tip.

![Figure 2.](https://cdn.elifesciences.org/articles/76513/elife-76513-fig2-v2.jpg)

**Figure 2.:** TEM images of the three Bacillus are acquired, scaled in the same dimension and aligned (left panel). Images at lower scale are made with a zoom in on the flagella insertion (right panel). Note that the zoom in is optical so that the zoomed in image do not correspond to a zone of the larger scale images.

We then used these three species to test if these ultrastructural differences could impact their swimming behaviour in a host biofilm or in a Newtonian control fluid: could the longer body of B. sphaericus be an impediment in a crowded environment such as a biofilm or on the contrary could its larger size give it a higher strength to cross the biofilm matrix? Is the unique brush-like flagella of B. cereus an advantage or a disadvantage to swim in a Newtonian fluid or in a host biofilm?

### Characterizing bacterial swimming in a biofilm matrix through image descriptors

2D+T Confocal Laser Scanning Microscopy (CLSM) of the three Bacillus swimming in a Staphylococcus aureus (S. aureus) host biofilm or in a control Newtonian buffer are acquired (see Figure 1d). Swimmers and host biofilms are imaged with different fluorescent dyes, allowing their acquisition in different color channels, and to recover in the same spatio-temporal referential the swimmer trajectories and the host biofilm density (see Materials and methods, Figure 1 and Table 1). Namely, for each species $s$ and individual swimmer $i$, we recover the initial ($T_{0,i}^{s}$) and final ($T_{e⁢n⁢d,i}^{s}$) observation times (when the swimmer goes in and out the focal plane, see Materials and methods sect. Confocal Laser Scanning Microscopy [CLSM]), and the number $T_{i}^{s}$ of time points in the trajectory. We then extract from the 2D+T images the observed position, instantaneous speed and acceleration time-series

$$
t↦X_{i}^{s}⁢(t),t↦V_{i}^{s}⁢(t),t↦A_{i}^{s}⁢(t), for ⁢t\in(T_{0,i}^{s},T_{e⁢n⁢d,i}^{s}).
$$

**Table 1.**
 Dataset characteristics.We detailed, for each batch, the number of trajectories, the average number of time points by trajectory (and standard deviation), the total number of time points in the dataset, the total movie duration in seconds and the time interval between two snapshots in seconds.


<table>
  <thead>
    <tr>
      <th>Species</th>
      <th>Batch</th>
      <th># traject.</th>
      <th>traj. length</th>
      <th>time points</th>
      <th>Duration [s]</th>
      <th>Δ⁢t[s]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>B. pumilus</td>
      <td>1</td>
      <td>122</td>
      <td>40 (7.4)</td>
      <td>4,590</td>
      <td>30</td>
      <td>0.134</td>
    </tr>
    <tr>
      <td></td>
      <td>2</td>
      <td>152</td>
      <td>25 (5.7)</td>
      <td>3,543</td>
      <td>30</td>
      <td>0.134</td>
    </tr>
    <tr>
      <td></td>
      <td>3</td>
      <td>243</td>
      <td>38 (6.9)</td>
      <td>8,825</td>
      <td>30</td>
      <td>0.134</td>
    </tr>
    <tr>
      <td>B. sphaericus</td>
      <td>1</td>
      <td>98</td>
      <td>40 (7.6)</td>
      <td>3,762</td>
      <td>30</td>
      <td>0.134</td>
    </tr>
    <tr>
      <td></td>
      <td>2</td>
      <td>91</td>
      <td>43 (7.7)</td>
      <td>3,771</td>
      <td>30</td>
      <td>0.134</td>
    </tr>
    <tr>
      <td></td>
      <td>3</td>
      <td>48</td>
      <td>55 (7.9)</td>
      <td>2,543</td>
      <td>23</td>
      <td>0.134</td>
    </tr>
    <tr>
      <td>B. cereus</td>
      <td>1</td>
      <td>105</td>
      <td>47 (7.9)</td>
      <td>4,766</td>
      <td>30</td>
      <td>0.069</td>
    </tr>
    <tr>
      <td></td>
      <td>2</td>
      <td>53</td>
      <td>36 (7.7)</td>
      <td>1,808</td>
      <td>30</td>
      <td>0.069</td>
    </tr>
    <tr>
      <td></td>
      <td>3</td>
      <td>121</td>
      <td>43 (7.1)</td>
      <td>5,006</td>
      <td>30</td>
      <td>0.069</td>
    </tr>
  </tbody>
</table>

Noting $b^{s}⁢(t,x)$ the dynamic biofilm density maps obtained from the biofilm images, we also compute the local biofilm density and density gradient along trajectories

$$
t↦b^{s}⁢(t,X_{i}^{s}⁢(t)), and ⁢t↦\nabla⁡b^{s}⁢(t,X_{i}^{s}⁢(t)).
$$

The angle $\theta_{i}^{s}⁢(t)$ and the average velocity $V¯_{i}^{s}⁢(t)$ between two successive speed vectors are also collected (see Materials and methods sec. Post-processing of image data).

Different swimming patterns can be deciphered by qualitative observations of the trajectories $X_{i}^{s}⁢(t)$ (Figure 3) in the biofilm and in the control Newtonian buffer, and run-and-tumble swimming patterns are quantified with $\theta_{i}^{s}⁢(t)$ and $V¯_{i}^{s}⁢(t)$ (Figure 4). B. sphaericus has a similar run-and-reverse behaviour in the biofilm and the control buffer with trajectories divided between back and forth paths around the starting point and long runs, the biofilm strongly impairing its speed and increasing the number of reverse events. By contrast, B. pumilus clearly switches its swimming behaviour in the biofilm, from quasi-straight runs in the Newtonian buffer to a pronounced run-and-reverse behaviour in the biofilm with decreased speeds and chaotic trajectories. On the contrary, B. cereus swimmers manage to conserve comparable trajectories and distributions of swimming speed and direction in the biofilm compared to control. Interestingly, the number of reverse events is even reduced in the host biofilm for B. cereus.

![Figure 3.](https://cdn.elifesciences.org/articles/76513/elife-76513-fig3-v2.jpg)

**Figure 3.:** Note that the 3 batches of the different species are pooled on these images. Number of trajectories are n = 517 and 123 (B. pumilus), n = 237 and 94 (B. sphaericus) and n = 279 and 144 (B. cereus) for, respectively, the biofilm and the control buffer. The physical size of the domain is 147x147μm.

![Figure 4.](https://cdn.elifesciences.org/articles/76513/elife-76513-fig4-v2.jpg)

**Figure 4.:** For each time point, the swimmer mean speed $V¯_{i}^{s}⁢(t)$, defined as the mean between the incoming and outgoing velocity vectors $V¯_{i}^{s}(t)=(‖V_{i}^{s}(t)‖+‖V_{i}^{s}(t−Δt)‖)/2, for t\in(T_{0,i}^{s}+Δt,T_{end,i}^{s})$, is plotted versus the direction change, defined as the angle $\theta_{i}^{s}⁢(t)$ between the incoming and outgoing velocity vectors $\theta_{i}^{s}(t)=arccos⁡((V_{i}^{s}(t)⋅V_{i}^{s}(t−Δt))/(||V_{i}^{s}(t)||V_{i}^{s}(t−Δt)||))$. The left and bottom panels indicate the marginal distributions, with the mean (dashed line) and quantiles 0.05, 0.5, and 0.95 (plain lines). Number of times points are n = 6 848 and 6 509 (B.pumilus), n = 2 818 and 3 740 (B. sphaericus) and n = 3 526 and 4 435 (B. cereus) for, respectively, the biofilm and the control buffer.

For further quantitative analysis, trajectory descriptors are defined. We first investigate the distribution of the population-wide average acceleration and velocity norms $\frac{1}{T_{i}^{s}−2}\sum_{t}‖A_{i}^{s}(t)‖$ and $\frac{1}{T_{i}^{s}−1}\sum_{t}‖V_{i}^{s}(t)‖$, where $∥⋅∥$ denotes the Euclidian norm. We also quantify the swimming kinematics by computing the travelled distance $d⁢i⁢s⁢t_{i}^{s}$ along the path and the total displacement $d⁢i⁢s⁢p_{i}^{s}$, that is the distance between the initial and final trajectory points, with

$$
d⁢i⁢s⁢t_{i}^{s}=\int_{T_{0,i}^{s}}^{T_{e⁢n⁢d,i}^{s}}∥V_{i}^{s}⁢(t)∥⁢dt  and  d⁢i⁢s⁢p_{i}^{s}=∥X⁢(T_{e⁢n⁢d,i}^{s})-X⁢(T_{0,i}^{s})∥=∥\int_{T_{0,i}^{s}}^{T_{e⁢n⁢d,i}^{s}}V_{i}^{s}⁢(t)⁢dt∥.
$$

We finally compute the total biofilm area visited by a swimmer along its path (see Figure 1b). The same descriptors are computed in the control Newtonian buffer.

The three species present contrasted distributions for these descriptors (Figure 5). B. sphaericus has the smallest mean ($||A||=0.58$ and $||V||=0.70$) and median ($∥A∥=0.50$ and $∥V∥=0.53$) values of acceleration and speed, while B. pumilus has the widest distributions (difference between 95% and 5% centiles of 2.76 for $∥A∥$ and 2.45 for $∥V∥$ compared to 1.00, 1.51 and 1.90, 1.49 for B. sphaericus and B. cereus respectively). B. cereus for its part shows the highest accelerations, indicating larger changes in swimming velocities, but median and mean speeds comparable to B. pumilus (Figure 5, $∥A∥$ and $∥V∥$ panels). We also note that B. sphaericus and to a lower extent B. pumilus trajectories have a significant amount of null or small average speeds, while B. cereus trajectories have practically no zero velocity, consistently with the qualitative analysis (Figure 5, $∥V∥$ panels). Small velocities episodes of B. sphaericus and B. pumilus could occur during their back-and-forth trajectories, which produce small displacements and pull the displacement distribution towards lower values than B. cereus (Figure 5, Disp panel). B. pumilus displacement is intermediary. Conversely, back-and-forth trajectories can produce large swimming distances for B. sphaericus and B. pumilus (mean adimensioned value of 32.2 and 43.2 respectively) so that B. sphaericus has a distance distribution comparable to B. cereus (mean adimensioned value of 29.6, Figure 5, Dist panel), but lower than B. pumilus. Observing conjointly displacement and distance (Figure 5, lower-right panel) provides consistent insights: B. sphaericus shows a large variability of small displacement trajectories, from small to large distances, while B. cereus trajectory displacement seems to vary almost linearly with the distance at least for the points inside the isoline 50%. B. pumilus has again an intermediary distribution, with a large range of displacement-distance couples. The distributions of visited areas of B. pumilus and B. cereus are almost identical, and higher than B. sphaericus one. Compared to the control buffer, all descriptors are reduced in the biofilm. Consistently with previous observations, the displacement ($d⁢i⁢s⁢p$) is strongly reduced for B. pumilus, and less impacted for B. sphaericus and B. cereus. These observations must be related to the behavioural switch for B. pumilus and to the identical swimming patterns for the two other Bacilii in the biofilm compared to the control fluid.

![Figure 5.](https://cdn.elifesciences.org/articles/76513/elife-76513-fig5-v2.jpg)

**Figure 5.:** Upper panel: normalized acceleration, speed, distance, displacement, and area distributions structured by species are displayed, together with quantile 0.05, 0.5, and 0.95 (vertical plain lines) and mean (vertical dashed line). The descriptor distribution in the control Newtonian buffer is indicated with the dotted line. All values are normalized by the corresponding reference value as indicated in Materials and methods. T-test pairwise comparison p-values are displayed in Appendix 1—table 2. Number of trajectories are n = 517 and 123 (B.pumilus), n = 237 and 94 (B. sphaericus) and n = 279 and 144 (B. cereus) for, respectively, the biofilm and the control buffer. Lower panel: we display the distribution of the instantaneous acceleration norm respectively to the local biofilm density gradient (i.e. $||A_{i}⁢(t)||$ function of $\nabla⁡b⁢(X_{i}⁢(t))$) and of the instantaneous velocity norm respectively to the local biofilm density (i.e. $||V_{i}⁢(t)||$ function of $b⁢(X_{i}⁢(t))$), structured by population. The point cloud of each species is approximated by a gaussian kernel and gaussian kernel isolines enclosing 5, 50% and 95% of the points centered in the densest zones are displayed to facilitate comparisons between species (see Materials and methods Plots and statistics).

All together, this data depict (1) a long-range species, B. cereus, which moves efficiently in the biofilm during long, relatively straight, rapid runs, almost identically as in a Newtonian fluid (2) a short-range species, B. sphaericus, that moves mainly locally in small areas in the biofilm and in the control buffer with lower accelerations and speeds except few exceptions (only 6% of its trajectories induced a displacement higher than $10⁢\mu⁢m$ compared to 28% for B. cereus and 26% for B. pumilus) and (3) a medium-range species, B. pumilus, with a large diversity of rapid trajectories, from small to large displacement, and a behavioural change from straight runs in a Newtonian fluid to frequent run-and-reverse events in the biofilm. These kinematics discrepancies for B. pumilus and B. cereus allow them however to cover identical visited areas.

Though, these global descriptors do not inform about potential adaptations of the swimmers to the biofilm matrix. We first check if swimmer velocities are directly linked to the local biofilm density, and if the swimmers adapt their trajectory according to density gradients by plotting the points $(∥\nabla⁡b⁢(t,X_{i}^{s}⁢(t))∥,∥A_{i}^{s}⁢(t)∥)$ and $(b⁢(t,X_{i}^{s}⁢(t)),∥V_{i}^{s}⁢(t)∥)$ (Figure 5, lower panel). Clear differences between the three species can be deciphered. First, the three Bacillus do not have the same distribution of visited biofilm density and gradient. B. pumilus swimmers visit denser biofilm with higher variations than the other species while B. sphaericus and B. cereus stay in less dense and smoother areas, the quantile 0.5 of these species being circumscribed in low gradient and low density values. Next, B. cereus has a wider distribution of accelerations, specially for small-density gradients, compared to B. pumilus and B. sphaericus. This could indicate that when the biofilm is smooth, B. cereus samples its acceleration in a large distribution of possible values. Finally, we observe that the speed distribution rapidly drops for increasing biofilm densities for B. sphaericus and B. cereus, while the decrease is much smoother for B. pumilus. These observations provide additional insights in the species swimming characteristics: B. pumilus swimmers seem to be less inconvenienced by the host biofilm density than the other species, while B. cereus and B. sphaericus bacteria appear to be particularly impacted by higher densities and to favor low densities where it can efficiently move. Though, B. sphaericus has lower motile capabilities than B. cereus when the biofilm is not dense.

### Analysis of swimming data with an integrative swimming model

This descriptive analysis does not allow to clearly identify potential mechanisms by which the swimmers adapt their swim to the biofilm structure or to simulate new species-dependant trajectories. We then build a swimming model based on a Langevin-like equation on the acceleration that involves several swimming behaviours modelling the swimmer adaptation to the biofilm. Furthermore, after inference, new synthetic data can be produced by predicting swimmer random walks sharing characteristics comparable to the original data.

We consider bacterial swimmers as Lagrangian particles and we model the different forces involved in the update of their velocity $v$. We assume that the swimmer motion can be modelled by a stochastic process with a deterministic drift (Figure 1c):

$$
d⁢v=\gamma⁢(\alpha⁢(b)-∥v∥)⁢\frac{v}{∥v∥}⁢dt⏟speed selection+\beta⁢\frac{\nabla⁡b}{∥\nabla⁡b∥}⁢dt⏟direction selection+η⁢dt⏟random term
$$

where the right hand side is composed of two deterministic terms in addition to a gaussian noise, each weighted by the parameters $\gamma$, $\beta$ and $ϵ$.

The first term implements the biological observation (Figure 5, lower central panel) that the bacterial swimmers adapt their velocity to the biofilm density. This term can be interpreted as a speed selection term that pulls the instantaneous speed of the swimmer towards a prescribed target velocity $\alpha⁢(b)$ that depends on the host biofilm density $b$. The weight $\gamma$ can be interpreted as a penalization coefficient. In such a formalism, the difference between the swimmer and the prescribed speed is divided by a relaxation time $\tau$ to be homogeneous to an acceleration. Hence, $\gamma$ is proportionally inverse to $\tau$, $\gamma∼\frac{1}{\tau}$. As a first-order approximation of the speed drop observed in Figure 5 for increasing $b$, the target speed $\alpha⁢(b)$ is modeled as a linear variation between v0 and v1, where v0 is the swimmer characteristic speed in the lowest density regions, where $b=0$, and v1 in the highest density zones where $b=1$:

$$
\alpha⁢(b)=v_{0}⁢(1-b)+b⁢v_{1}=v_{0}+b⁢(v_{1}-v_{0})
$$

The second term updates the velocity direction according to the local gradient of the biofilm density $\nabla⁡b$. The sign of $\beta$ indicates if the swimmer is inclined to go up (negative $\beta$) or down (positive $\beta$) the host biofilm gradient, while the weight magnitude indicate the influence of this mechanism in the swimmer kinematics. We note that this term does not depend on the gradient magnitude but only on the gradient direction: this reflects the implicit assumption that the bacteria are able to sense density variations to find favorable directions, but that the biological sensors are not sensitive enough to evaluate the variation magnitudes.

The third term is a stochastic two-dimensional diffusive process that models the dispersion around the deterministic drift modelled by the two first terms. We define

$$
η∼N(0,ϵ)
$$

The term η can also be interpreted as a model of the modelling errors, tuned by the term $ϵ$. Equation 1 is supplemented by an initial condition by swimmer. For vanishing $∥v∥$ or $∥\nabla⁡b∥$ leading to an indetermination, the corresponding term in the equation is turned off.

Equation 1 links the observed biofilm density and the swimmer trajectories trough mechanistic swimming behaviours. The model fitting can be seen as an ANOVA-like integrative statistical analysis of the image data. It decomposes the observed acceleration variance between mechanistic processes describing different swimming traits in order to decipher their respective influence on the swimmer trajectories while integrating heterogeneous data (density maps $b$ and trajectories kinematics).

We can define characteristic speed and acceleration $V^{*}$ and $A^{*}$ in order to set a dimensionless version of Equation 1

$$
d⁢v=\gamma^{′}⁢(v_{0}^{′}+b⁢(v_{1}^{′}-v_{0}^{′})-∥v∥)⁢\frac{v}{∥v∥}⁢dt+\beta^{′}⁢\frac{\nabla⁡b}{∥\nabla⁡b∥}⁢dt+η^{′}⁢dt
$$

where $\gamma^{′}=\frac{\gamma⁢V^{*}}{A^{*}}$, $v_{0}^{′}=\frac{v_{0}}{V^{*}}$, $v_{1}^{′}=\frac{v_{1}}{V^{*}}$, $\beta^{′}=\frac{\beta}{A^{*}}$, $η^{′}∼N(0,ϵ^{′})$ and $ϵ^{′}=\frac{ϵ}{A^{*2}}$.

This dimensionless version will strongly improve the inference process and will allow an analysis of the relative contribution of the different terms in the kinematics. An extended numerical exploration of this model is performed in Appendix 2 Sec. Numerical exploration on mock biofilm images to illustrate the impact of the different parameters on the trajectories, showing in particular the interplay between $\gamma$ and $ϵ$: counter-intuitively, straight lines are induced when the stochastic part $ϵ$ is high compared to the speed selection parameter $\gamma$ (see also Appendix 2).

### Inferring swimming parameters from trajectory data

For each bacterial swimmer population, we now seek to infer with a Bayesian method population-wide model parameters governing the swimming model of a given species from microscope observations.

#### Inference model setting

Equation (2) is re-written as a state equation on the acceleration for the bacterial strain $s$ and the swimmer $i$

$$
A_{i}^{s}⁢(t)=\gamma^{s}⁢(v_{0}^{s}+b⁢(t,X_{i}^{s}⁢(t))⁢(v_{1}^{s}-v_{0}^{s})-∥V_{i}^{s}⁢(t)∥)⁢\frac{V_{i}^{s}⁢(t)}{∥V_{i}^{s}⁢(t)∥}+\beta^{s}⁢\frac{\nabla⁡b⁢(t,X_{i}^{s}⁢(t))}{∥\nabla⁡b⁢(t,X_{i}^{s}⁢(t))∥}+η^{s}
$$



$$
:=f_{A}⁢(\theta^{s},b⁢(t,X_{i}^{s}⁢(t)),V_{i}^{s}⁢(t),X_{i}^{s}⁢(t))+η^{s}
$$

where

$$
\theta^{s}:=(\gamma^{s},v_{0}^{s},v_{1}^{s},\beta^{s})
$$

are species-dependant equation parameters. The function $f_{A}$ can be seen as the deterministic drift of the random walk, gathering all the mechanisms included in the model. The inter-individual variability of the swimmers of a same species comes from the swimmer-dependent initial condition, the resulting biofilm matrix they encounter during their run, and the stochastic term.

Inferring the parameters $\theta^{s}$ can then be stated in a Bayesian framework as solving the non linear regression problem

$$
A_{i}^{s}(t)∼N(f_{A}(\theta^{s}|b(t,X_{i}^{s}(t)),V_{i}^{s}(t),X_{i}^{s}(t)),ϵ^{s})
$$

from the data $b⁢(t,X)$, $X_{i}^{s}⁢(t)$, $V_{i}^{s}⁢(t)$ and $A_{i}^{s}⁢(t)$, with truncated normal prior distributions

$$
\theta^{s}∼N(0,1),ϵ^{s}∼N(0,1),
$$

and additional constrains on the parameters

$$
\gamma^{s}\geq0,v_{0}^{s}\geq0,v_{1}^{s}\geq0,ϵ^{s}\geq0.
$$

We note that Equation (5) can be seen as a likelihood equation of the parameter $\theta^{s}$ knowing $A_{i}^{s}⁢(t),b⁢(t),V_{i}^{s}⁢(t)$ and $X_{i}^{s}⁢(t)$. The parameter $ϵ^{s}$ can now be seen as a corrector of both modelling errors in the deterministic drift and observation errors between the observed and the true instantaneous acceleration. Alternative settings where these uncertainties sources are separated and a true state for position and acceleration is inferred can be defined (see Annex Various inference models). The inference problem is implemented in the Bayesian HMC solver Stan (Stan Development Team, 2018) using its python interface pystan (Riddell et al., 2021). Inference accuracy is thoroughly assessed on synthetic data (see Appendix 1 Assessment of the inference with synthetic data and Figure 6).

![Figure 6.](https://cdn.elifesciences.org/articles/76513/elife-76513-fig6-v2.jpg)

**Figure 6.:** (a) Predicted vs true trajectories. Trajectories are recovered by sampling the parameter posterior distribution starting from the same initial condition than in the data. We represent a ground truth trajectory extracted randomly from the original dataset in red, the corresponding sampled trajectories with thin gray lines, and the trajectory obtained with the posterior means in orange. Note that in this simulation, the stochastic part is the same for all simulations, so that the only source of uncertainties comes from the inference procedure. (b) Trajectory descriptors. Trajectories are re-computed replacing the original parameters (ground truth) by the inferred parameters. The trajectory descriptors introduced in Characterizing bacterial swimming in a biofilm matrix through image descriptors are computed on the synthetic data (blue curves) and on the data obtained with the inferred parameters (orange curves). Number of trajectories are n = 72 for the ground truth and n = 100 after inference. (c) Ground truth vs fitted trajectories. The ground truth, that is the original trajectories (blue) and fitted (red) trajectories are displayed and show common characteristics. (d-e) Qqplot of fitted model output vs ground truth. After inference, the fitted model is used to re-compute the synthetic dataset. We plot the x (d) and y (e) components of the accelerations in a qqplot: the fitted model output quantiles are plotted against the quantiles of the original dataset (ground truth) with blue dots, together with the $y=x$ line (red).

#### Analysis of the confocal microscopy dataset

We now solve the inference problem (5)-(6) on the confocal microscopy dataset to identify population-wide swimming model parameters in order to decompose the swimmer kinematics in three mechanisms: biofilm-related speed selection, density-induced direction changes and random walk. The inference process is assessed by comparing the descriptors obtained on trajectories predicted by the fitted model (Figure 7a) with descriptors of real trajectories (Figure 5). The mean values of acceleration and speeds are accurately predicted for the three species ( Figure 7a panels $∥A∥$ and $∥V∥$, dashed lines). Relative positions of distance, displacement and visited area mean values are also correctly simulated (Figure 5 and Figure 7a, upper panel). B. sphaericus presents the lowest predicted accelerations and speeds while B. pumilus has the widest speed and acceleration distributions and B. cereus shows the highest accelerations, consistently with the data. The visited area and the distances are slightly over estimated, but the relative position and the shape of the distributions are conserved. The amount of null velocities for B. sphaericus is under estimated by the fitted model and not rendered for B. pumilus. The distance distributions of the three species are accurately predicted by the fitted model. When displaying conjointly the distance and the displacement (Figure 7a, right lower panel), the distribution of B. sphaericus is correctly predicted by the simulations, but B. cereus and B. pumilus displacements are underestimated. Some qualitative features can be recovered, such as the higher distribution of distance-distribution couples for B. cereus or higher displacement for B. cereus compared to B. sphaericus.

![Figure 7.](https://cdn.elifesciences.org/articles/76513/elife-76513-fig7-v2.jpg)

**Figure 7.:** (a) To validate the inference process, a synthetic dataset is assembled by computing Equation 1 with the inferred parameters and the trajectory descriptors introduced in section Characterizing bacterial swimming in a biofilm matrix through image descriptors are computed and can be compared to the data descriptors in Figure 5. Acceleration, speed, distance and displacement distributions are displayed in the upper panel, with quantiles 0.05, 0.5 and 0.95 (plain lines) and mean (dashed line). The mean values observed in the image data are also displayed for comparison (black dashed line). The number of trajectories are identical than in Figure 5: n = 517 (B. pumilus), n = 237 (B. sphaericus) and n = 279 (B. cereus). Interactions between the host biofilm and, respectively, acceleration and speed distributions are displayed in the lower panel with isolines enclosing 5, 50% and 95% of the points, centered in the densest zones. (b) Inferred parameter posterior distributions after analysis of the confocal swimmer images, and posterior mean (dashed line). We used 4000 points for the computation of the Gaussian KDE.

Descriptors of swimming adaptations to the host biofilm are also correctly preserved for the main part (Figure 5 and Figure 7 a, lower panel). B. pumilus is the species that crosses the highest biofilm densities in the fitted model simulations, showing the highest speeds in this crowded areas, and that visits the most frequently areas with high density gradients, consistently with the data. As in the confocal images, the simulated B. sphaericus and B. cereus favor smoother zones of the biofilm with lower biofilm densities. The B. cereus fitted model correctly renders the highest acceleration variance observed in the data for low biofilm gradients, while B. sphaericus speed and acceleration variance is the lowest for all ranges of biofilm densities and gradients, both in the data and in the fitted model predictions. The drop of speeds and accelerations for increasing biofilm densities and gradients is well predicted for B. pumilus, but is smoother in the simulation compared to the data for B. sphaericus and B. cereus. In particular, the sharp drop of speeds for $b≃0.25$ observed in the data for B. cereus and B. sphaericus is underestimated by the fitted model.

All together, the model reproduces very accurately the mean values of acceleration, speed and visited area, renders relative positions and the main characteristics of distributions for distance, displacement and interactions with the host biofilm matrix, but produces less variable outputs than observed in the data, meaning that the model is less accurate in the distribution tails. The main features of the swimmer adaptation to the underlying biofilm are however correctly predicted by the model.

To further inform the fitted model accuracy, the coefficient of determination $R_{d⁢e⁢t}^{2}$ of the deterministic components $f_{A}⁢(\theta^{s},b⁢(t),V_{i}^{s},X_{i}^{s}⁢(t))$ of Equation 4 is computed (Table 2), in order to quantify the goodness of fit of the friction and gradient terms of (Equation 2) that represent interactions with the biofilm. These results highlight that B. cereus bacteria do present an important stochastic part in the accelerations, while the B. pumilus species is the best represented by our deterministic modelling.

**Table 2.**
 Reference acceleration and speed, and acceleration variance decomposition between stochastic and deterministic terms.The number $N$ of acceleration time points is indicated for each specie. Then, reference values for acceleration $A_{r⁢e⁢f}$ and speed $V_{r⁢e⁢f}$ used for adimensionalization are computed by averaging the corresponding values by specie. Descriptive statistics of acceleration variance decomposition are then computed in order to illustrate the contribution of the deterministic terms in the observed acceleration distribution, and the part of the residual mechanisms that are not included in the model. We indicate for each species the acceleration variance $\sigma⁢(A)$, the part of the variance explained by the deterministic terms $R_{d⁢e⁢t}^{2}$ (see Materials and methods sec.Inference validation on experimental data) and the variance of the stochastic term $ϵ^{2}$. We note that in order to compare species at vizualisation step, they are re-normalized with the average of the species reference values: $A_{r⁢e⁢f}=$ 78.31 and $V_{r⁢e⁢f}=$ 6.55.


<table>
  <thead>
    <tr>
      <th>data</th>
      <th>N</th>
      <th>Ar⁢e⁢f</th>
      <th>Vr⁢e⁢f</th>
      <th>σ⁢(A)</th>
      <th>Rd⁢e⁢t2[%]</th>
      <th>ϵ2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>B.pumilus</td>
      <td>33,916</td>
      <td>81.08</td>
      <td>7.89</td>
      <td>0.87</td>
      <td>58.80</td>
      <td>0.36</td>
    </tr>
    <tr>
      <td>B.sphaericus</td>
      <td>20,152</td>
      <td>44.93</td>
      <td>4.74</td>
      <td>0.58</td>
      <td>48.50</td>
      <td>0.30</td>
    </tr>
    <tr>
      <td>B.cereus</td>
      <td>23,160</td>
      <td>108.92</td>
      <td>7.03</td>
      <td>0.63</td>
      <td>32.72</td>
      <td>0.42</td>
    </tr>
  </tbody>
</table>

The three species present very different inferred parameter values (Figure 7 b and Table 3), showing that the model inference captures contrasted swimming characteristics of these Bacillus. Due to the mechanistic terms introduced in Equation 1, these differences can be interpreted in term of speed and direction adaptations to the host biofilm. First, B. pumilus shows the highest v0 value, and the highest amplitude between v0 and v1, inducing a higher ability for B. pumilus to swim fast in low density biofilm zones and strong deceleration in crowded area. In comparison, B. sphaericus presents the smallest amplitude between v0 and v1 showing a poor adaptation to biofilm density. B. cereus has the highest $\gamma$ value, showing a reduced relaxation time toward the density dependant speed: in other words, B. cereus is able to adapt its swimming speed more rapidly than the other species when the biofilm density varies. B. cereus swimmers are also better able to change their swimming direction in function of the biofilm variations they encounter along their way, their $\beta$ distribution being markedly higher than the other species which have very low $\beta$. Finally, the stochastic parameter $ϵ$ is also contrasted, from a low distribution for B. sphaericus to high values for B. cereus. All together, the inference complete the observations made in Figure 5: B. pumilus poorly adapts its swimming direction to the host biofilm (low $\beta$) but has a wide range of possible speeds when the biofilm density varies (high v0, low v1), that it can reach quite rapidly (intermediary $\gamma$) with intermediary stochastic correction ($ϵ$). In contrast, B. cereus reaches lower speed values (intermediary v0, low v1) but is more agile to adapt its swimming to its environment by changing rapidly its speed when the biofilm density is more favorable (highest $\gamma$) and adapting its swimming direction to biofilm variations, with higher stochastic variability (large $ϵ$). Finally, B. sphaericus is the less flexible of the three bacteria: less fast (smallest difference between v0 and v1), they are also less responsive to biofilm variations (small $\gamma$ and $\beta$) with low random perturbations (small $ϵ$).

**Table 3.**
 Inference outputs for the three species.The posterior mean, standard deviation and inferred confidence interval are indicated for each parameter and each specie. Convergence diagnosis index $n_{e⁢f⁢f}$ and $R_{h⁢a⁢t}$ are provided.


<table>
  <thead>
    <tr>
      <th>species</th>
      <th>param</th>
      <th>mean</th>
      <th>std</th>
      <th>confidence interval [2.5%–97.5%]</th>
      <th>neff</th>
      <th>Rhat</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>B. pumilus</td>
      <td>γ</td>
      <td>0.77</td>
      <td>3.95×10–3</td>
      <td>[0.77–0.77]</td>
      <td>4,507</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td>v0</td>
      <td>0.14</td>
      <td>8.67×10–3</td>
      <td>[0.12–0.16]</td>
      <td>3,879</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td>v1</td>
      <td>1.69×10–3</td>
      <td>1.69×10–3</td>
      <td>[5.18×10–5−6.26×10–3]</td>
      <td>4,821</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td>β</td>
      <td>9.84×10–3</td>
      <td>5.07×10–3</td>
      <td>[1.45×10–5−2.07×10–2]</td>
      <td>5,223</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td>ε</td>
      <td>0.62</td>
      <td>2.48×10–3</td>
      <td>[0.61–0.62]</td>
      <td>5,307</td>
      <td>1</td>
    </tr>
    <tr>
      <td>B. sphaericus</td>
      <td>γ</td>
      <td>0.61</td>
      <td>4.53×10–3</td>
      <td>[0.60–0.62]</td>
      <td>4,965</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td>v0</td>
      <td>2.75×10–4</td>
      <td>2.75×10–4</td>
      <td>[4.91×10–6−1.01×10–3]</td>
      <td>4,019</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td>v1</td>
      <td>4.84×10–3</td>
      <td>4.77×10–3</td>
      <td>[9.39×10–5−1.45×10–2]</td>
      <td>5,001</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td>β</td>
      <td>4.25×10–3</td>
      <td>3.33×10–3</td>
      <td>[−2.18×10–3−1.15×10–2]</td>
      <td>4,668</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td>ε</td>
      <td>0.32</td>
      <td>1.55×10–3</td>
      <td>[0.31–0.32]</td>
      <td>5,943</td>
      <td>1</td>
    </tr>
    <tr>
      <td>B. cereus</td>
      <td>γ</td>
      <td>0.83</td>
      <td>1.11×10–2</td>
      <td>[0.80–0.86]</td>
      <td>2,700</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td>v0</td>
      <td>6.44×10–2</td>
      <td>1.07×10–2</td>
      <td>[3.22×10–2−9.66×10–2]</td>
      <td>2,510</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td>v1</td>
      <td>6.65×10–3</td>
      <td>6.33×10–3</td>
      <td>[1.50×10–4−2.15×10–2]</td>
      <td>4,061</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td>β</td>
      <td>2.78×10–2</td>
      <td>9.04×10–3</td>
      <td>[1.39×10–2−5.56×10–2]</td>
      <td>4,230</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td>ε</td>
      <td>0.9</td>
      <td>4.17×10–3</td>
      <td>[0.89–0.92]</td>
      <td>4,852</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

Finally, after inference, the impact of each term in the overall acceleration data can be quantified and analyzed by displaying its relative contribution in a ternary plot (Appendix 2—figure 6). This relative contribution can be measured thanks to the swimming model which integrates these different mechanisms in the same inference problem. The direction selection is the least influential mechanism for the three species, with a slightly higher impact for B. cereus (50% and 95% isolines slightly shifted towards $A⁢(\nabla⁡b)$ in Appendix 2—figure 6a). When zooming in, the three Bacillus show differences in the balance between speed selection and the random term (Appendix 2—figure 6b): while B. pumilus is slightly more influenced by the friction term than by stochasticity, these mechanisms are perfectly balanced in B. sphaericus accelerations, while B. cereus is more influenced by the random term.

#### Interpretation of the bacterial swimming at the light of their morphology

Kinematics descriptors and swimming parameters can then be reinterpreted through the insights provided by the morphology of each bacteria species as shown in Figure 2. As observed in Figure 2, B. pumilus and B. sphaericus are flagellated whereas B. cereus is equipped by a unique brush-like bundle of thin flagella at its tail. This morphology can be linked to their swimming patterns. The flagella could be linked to the run-and-tumble behaviour of B. pumilus and B. sphaericus, as shown for other flagellated bacteria such as E. coli, the tumbling events of which are induced by reverse rotation of the cellular motor of its multiple flagella (Patteson et al., 2015). Additional functional characteristics may discriminate B. pumilus and B. sphaericus, since run-and-reverse swimming is the natural behaviour of B. sphaericus even in the Newtonian control buffer, whereas B. pumilus drastically reduces its speed in high-density biofilms (Figure 7, a) and starts tumbling in the host biofilm (Figure 4). B. pumilus has the highest number of flagella and is the bacteria that reaches the highest speeds specially in the Newtonian buffer and in low-density areas, indicating that this characteristic may be an advantage for swimming fast in the extracellular matrix. The kind, size and disposition of the flagella bundle may help B. cereus swimmers to adapt their runs to their environment by changing directions to follow lower density areas (higher impact of direction selection term of the three Bacillus in Appendix 2—figure 6) or to adapt rapidly when biofilm density varies (largest $\gamma$). B. cereus being the bacteria with the strongest stochastic part (highest $ϵ$, density shifted towards $A⁢(ϵ)$ in Appendix 2—figure 6), this morphology could also help the swimmer to go through the biofilm by random navigation, which helps to maintain comparable straight trajectory with or without biofilm when the stochastic part is higher than the speed selection term (Appendix 1—figure 1, Appendix 2—figure 3 and Appendix 2—figure 6). Finally, B. sphaericus bacteria are much longer than the other two species, which may explain why this species is the least motile in terms of acceleration and kinematics, both in biofilms and in the Newtonian control buffer.

## Discussion

### Modelling and analysis of swimming trajectories

When analyzing microbial swimming trajectories, two general strategies can be found in the literature. The first one aims at designing statistical tests quantifying similarities with or deviations from typical motion of interest such as diffusion (Patteson et al., 2015). Another strategy consists in providing a generative model of the data, analyzing it (Chepizhko and Peruani, 2013; Chepizhko et al., 2013) and comparing model outputs with real data (Koorehdavoudi et al., 2017; Jabbarzadeh et al., 2014), possibly after inference. The model that is studied in this paper belong to the second category: the model includes deterministic mechanisms describing interactions with the host biofilm, together with a random correction counterbalancing the modelling errors. The parameter inference allows to interpret the data variance relatively to speed or direction adaptations to the host biofilm versus residual effects gathered in the stochastic term. This method is comparable to ANOVA-like multivariate analysis: the parametric phenomelogical mappings between explicative co-variables and a swimming behaviour (for example the function defining speed selection from biofilm density) are gathered in the same inference problem, enabling to decompose acceleration variability between the different swimming behaviours. This integrative method allows for multi-data integration and co-analysis. Furthermore, the fitted model allows to simulate typical swimming trajectories of a given species.

### Population-wide swimming characteristics vs true-state inference

In this study, we do not aim to recover ’true’ swimmer trajectories (a.e. the blue trajectory in Appendix 2—figure 4), that is identifying through smoothing techniques an approximation of the specific realization of the stochastic modeling and observation errors that lead to a given ’observed’ trajectory. Rather, the goal is to identify common characteristics shared by a population of trajectories by inferring the ‘population-wide’ parameters (the parameters $\alpha$, $\beta$, v0, v1, $\gamma$, and $ϵ$) that best explain the whole set of observed accelerations in a same population of swimmers. For this reason, we did not introduce swimmer-specific terms nor individual noise: they would have increased the model accuracy, but to the price of a blurrier characterization of the species specificities.

This choice determined our inference framework. Despite several alternative options for recovering hidden states, in particular SSM (space state models) which are common in spatial ecology (Auger‐Méthé et al., 2021), the Bayesian method we opted for is a simpler non-linear regression problem that proved to be sufficient to recover macroscopic features of swimmer trajectories and species stratification. We discuss in Appendix 3 Various inference models the different options that were tested and present in Materials and methods Sec. Inference the method for noise model selection. Among other interesting features, the Bayesian method provides confidence intervals on the final parameter estimation, and on the resulting trajectories as in Figure 6a.

### Predictive capabilities of the model

The deterministic terms of the model explain only half of the variance (Table 2). A major part of the underlying mechanisms is not correctly described by our model which is a common feature since it is a phenomenological model which only considers interactions with the underlying biofilm at a macroscopic level, without taking into account nanoscale physical mechanisms. A more detailed description of the underlying physics could have been designed as in Martinez et al., 2014, but it would have made more complex the analysis of the interactions between the host biofilm and the swimmer trajectories and the extraction of species-specific patterns. However, we note that our model correctly renders observations made through macroscopic trajectory descriptors, even though the inference process has not been made based on these observables. Furthermore, several repetitions of the same models with different samples of the stochastic terms give very similar values for the trajectory descriptors (see Appendix 2—figure 5 and section Influence of inference and stochastic terms on the trajectory descriptors), showing that these descriptors are robust to stochastic perturbations. Hence, the model (2) can be used to produce synthetic data sharing the same global characteristics than the original ones specifically taking into accounts interactions between the swimmers and the host biofilm. Furthermore, these predictions also reproduce the species stratification observed in the original data using the global descriptors.

### Biological interpretation of the fitted models

The direction selection term of the equation driven by $\beta$ has little impact in the swimmer model fitted on real data. However, the parameter $\beta$ can have a sensible impact on the kinematics as shown in the sensitivity analysis, and on the trajectories in mock biofilms (Appendix 2—figure 1). This could indicate that direction selection based on biofilm gradients is marginally effective in real-life swimming trajectories in a biofilm matrix. On the contrary, the speed selection term is more effective for the three Bacillus, showing that these micro-swimmer are able to adapt their swimming velocity to the biofilm density faced during their run. This term acts as an inertial term which enhances the stochastic term to provide direction and velocity changes.

The model has been used to decipher different adaptation strategies to the host biofilm of the three species during their swim. It confirms that B. sphaericus are the less motile bacteria in the biofilm, with reduced speeds and adaptation capabilities as indicated by the smallest model parameter values and a stereotypic run-and-reverse behaviour inside or outside the biofilm. B. pumilus on the contrary drastically changes its swimming behaviour in the biofilm compared to the Newtonian control buffer, which is reflected in the model by a high amplitude between v0 and v1 and a high $\gamma$ that indicates a rapid adaptation for varying biofilm densities. B. cereus shows the highest adaptation ability to the biofilm matrix, with the highest $\gamma$ and $\beta$ reflecting biofilm-induced speed and direction changes. Furthermore, the high stochastic effects (highest ∈) higher than the speed selection term tuned by $\gamma$ (see Appendix 2—figure 6) allows this swimmer to conserve straight runs in the biofilm (see Appendix 2 Sec. Friction and random term in Langevin equations.) in the same way than in the control Newtonian fluid.

This characterization methodology could be used to drive species selection for improved biofilm control. Furthermore, the model can be used to predict new trajectories and the resulting biofilm vascularization, in a similar framework as in Houry et al., 2012. Coupled with a model of biocide diffusion, these simulations could be used to test numerically the efficiency of mono- or multi-species swimmer pre-treatment to improve the removal of the host biofilm.

### Flagellated bacteria in polymeric solutions

Characterization of flagellated bacteria motility in polymeric solutions is a very active research area (Martinez et al., 2014; Patteson et al., 2015; Zöttl and Yeomans, 2019; Qu and Breuer, 2020; Qu et al., 2018). Speed and direction variations have been measured for various polymeric fluids with different visco-elastic properties. For the model bacteria E. coli in polymeric solutions, enhanced viscosity decreases tumbling while increased elasticity speeds up the swimmers (Patteson et al., 2015; Zöttl and Yeomans, 2019). In our experiments on the contrary, we observed decreased speeds and strong enhancement of reverse events for the flagellated B. sphaericus and B. pumilus in the biofilm compared to the Newtonian control buffer. However, the experimental set-up shows strong differences: the complex rheology of S. aureus biofilms may strongly differ from polymeric fluids even if under certain condition they can be considered as visco-elastic fluids (Gloag et al., 2020), impacting differently the swimmer behaviours. Furthermore, the physiology of the motor cell in the Gram-positive Bacillus differs from the one of the Gram-negative E. coli (Terahara et al., 2020; Szurmant and Ordal, 2004; Subramanian and Kearns, 2019). Finally, the particular brush-like flagella bundle of B. cereus may allow this species to conserve the same swimming in Newtonian and crowded environments, by adapting its swimming speed to the local density and otherwise randomly selecting swimming directions across the host biofilm. To generalize this approach to other contexts, this study should be reproduced for other swimmers and other host biofilms, together with polymeric fluids and porous media, including biochemical interactions.

## Materials and methods

### Infiltration of host biofilms by bacilli swimmers

Infiltration of S. aureus biofilms by bacilli swimmers were prepared in 96-well microplates. Submerged biofilms were grown on the surface of polystyrene 96-well microtiter plates with a μ clear base (Greiner Bio-one, France) enabling high-resolution fluorescence imaging (Bridier et al., 2010). 200 μL of an overnight S. aureus RN4220 pALC2084 expressing GFP (Malone et al., 2009) cultured in TSB (adjusted to an OD 600 $nm$ of 0.02) were added in each well. The microtiter plate was then incubated at 30°C for 60 $min$ to allow the bacteria to adhere to the bottom of the wells. Wells were then rinsed with TSB to eliminate non-adherent bacteria and refilled with 200 μL of sterile TSB prior incubation at 30 $celsius$ for 24 h. In parallel, B. sphaericus 9 A12, B. pumilus 3 F3 and B. cereus 10B3 were cultivated overnight planktonically in TSB at 30 °C. Overnight cultures were diluted 10 times and labelled in red with 5 μM of SYTO 61 (Molecular probes, France). After 5 min of contact, 50 μL of labelled fluorescent swimmers suspension were added immediately on the top of the S. aureus biofilm. All microscopic observations were collected within the following 30 min to avoid interference of the dyes with bacterial motility. Three replicates were conducted. The same protocol has been repeated without the host biofilm (control experiments): the swimmers are added to the buffer only which is a Newtonian fluid.

### Confocal laser scanning microscopy (CLSM)

The 96 well microtiter plate containing 24 hr S. aureus biofilm and recently added bacilli swimmers were mounted on the motorized stage of a Leica SP8 AOBS inverter confocal laser scanning microscope (CLSM, LEICA Microsystems, Germany) at the MIMA2 platform (https://www6.jouy.inra.fr/mima2_eng/). Temperature was maintained at 30 $celsius$ during all experiments. 2D+T acquisitions were performed with the following parameters: images of 147.62 × 147.62 $\mu⁢m$ were acquired at 8000 $Hz$ using a 63×/1.2 N.A. To detect GFP, an argon laser at 488 $nm$ set at 10% of the maximal intensity was used, and the emitted fluorescence was collected in the range 495–550 $nm$ using hybrid detectors (HyD LEICA Microsystems, Germany). To detect the red fluorescence of SYTO61, a 633 $nm$ helium-neon laser set at 25% and 2% of the maximal intensity was used, and fluorescence was collected in the range 650–750 $nm$ using hybrid detectors. Images were collected during 30 s (see Table 1 for sampling period).

Bacterial swimmers navigate within a three-dimensional biofilm matrix and confocal microscope refreshment time is not small enough to allow 3D+T images. To limit 3D trajectories, a focal plane near the well edge has been selected, where the well wall physically constrains the swimmer trajectories in one direction, which select longer trajectories in the 2D plane that can be tracked in time. Therefore, experimental data are composed of two-dimensional trajectories captured between the swimmer arrival and departure times in the focal plane, and the associated 2D+T biofilm density images that change over time due to swimmer action.

To check that the host biofilm structure is identical near the well’s edge compared to other 2D slices, we took 4 replicates of S. aureus biofilms that were imaged in 3D using a stack of 6 horizontal images, starting from $z=0$ near the well’s edge, to $z=6⁢Δ⁢z$, at the interface between the biofilm and the bulk solution. To study the between and within biofilm density variability in the horizontal images, we subsampled them with a regular Cartesian 4 × 4 grid, resulting in a 4 × 6 x(4 × 4)=384 2D images database supplemented by metadata (stack, $z$ and $x-y$ coordinate of the subsample), before computing a clustered pairwise correlation similarity matrix and a permanova.

### Transmitted electron microscopy

Materials were directly adsorbed onto a carbon film membrane on a 300-mesh copper grid, stained with 1% uranyl acetate, dissolved in distilled water, and dried at room temperature. Grids were examined with Hitachi HT7700 electron microscope operated at 80 $kV$ (Elexience – France), and images were acquired with a charge-coupled device camera (AMT).

### Post-processing of image data

See Figure 1 for a sketch of the datastream from microscope raw images to model inputs and Appendix 1—figure 1 for data visualization at each step of the post-processing pipeline.

Swimmer tracking has been applied on the red channel of the raw temporal stacks with IMARIS software (Oxford Instruments) using the tracking function after automated spots detection to get position time-series for each swimmer. Time-series with less than 8 time steps were filtered out.

Then, swimmer speed and acceleration time-series were computed from their position by finite-difference approximations and trajectory descriptors were extracted. The RGB green channel corresponding to the biofilm density temporal images were converted into grayscale and rescalled between 0 and 1 (linear scalling).

Trajectory descriptors are defined as follows. The mean acceleration and speed values, distance and displacement are computed with $∥A∥_{i}^{s}=\frac{1}{T_{i}^{s}-2}⁢\sum_{t}∥A_{i}^{s}⁢(t)∥$, $∥V∥_{i}^{s}=\frac{1}{T_{i}^{s}-1}⁢\sum_{t}∥V_{i}^{s}⁢(t)∥$, $d⁢i⁢s⁢t_{i}^{s}=Δ⁢t⁢\sum_{T_{0,i}^{s}}^{T_{e⁢n⁢d,i}^{s}-Δ⁢t}∥V_{i}^{s}⁢(t)∥$ and $d⁢i⁢s⁢p_{i}^{s}=∥X⁢(T_{e⁢n⁢d,i}^{s})-X⁢(T_{0,i}^{s})∥$. To compute the visited area, each trajectory piece was subsampled by computing $X_{i}^{s}⁢(t_{k})=\frac{k}{n_{s}}⁢X_{i}^{s}⁢(t)+(1-\frac{k}{n_{s}})⁢X_{i}^{s}⁢(t+Δ⁢t)$ for $k=0,n_{s}$, with $n_{s}=10$ and the pixels included in the ball $B⁢(X_{i}^{s}⁢(t_{k}),r)$ with radius $r=2$ were labeled. The total area of the labelled pixels is defined as the visited area of the swimmer $i$ of species $s$.

To assess run-and-tumble behaviour, the angle $\theta_{i}^{s}⁢(t)$ and the mean velocity $V¯_{i}^{s}⁢(t)$ between two consecutive speed vectors are defined with $\theta_{i}^{s}(t)$ = $arccos⁡((V_{i}^{s}(t)⋅V_{i}^{s}(t−Δt))/(‖V_{i}^{s}(t)‖‖V_{i}^{s}(t−Δt)‖))$ and $V¯_{i}^{s}(t)=(‖V_{i}^{s}(t)‖+‖V_{i}^{s}(t−Δt)‖)/2$, for $t\in(T_{0,i}^{s}+Δt,T_{end,i}^{s})$.

Post-processed data are available at https://forgemia.inra.fr/bioswimmers/swim-infer/SwimmerData.

### Computation of the forward swimming model

Time integration of equations (2) has been solved with an explicit Euler scheme regarding positions $x_{i,t}^{s}$ and velocities $v_{i,t}^{s}$ of the swimmer $i$ of species $s$ at time $t$:

$$
x_{i,t+1}^{s}=x_{i,t}^{s}+v_{i,t}^{s}⁢dt
$$



$$
v_{i,t+1}^{s}=v_{i,t}^{s}+dv_{i,t}^{s}
$$

where $dv_{i,t}^{s}$ is given by Equation 2, and depends on $\theta^{s}$, $V_{i,t}^{s}$, $x_{i,t}^{s}$, $b⁢(t,x_{i,t}^{s})$ and $\nabla⁡b⁢(t,x_{i,t}^{s})$. In practice, the biofilm density and gradient maps $b$ and $∇b$ are discretized with a Cartesian grid corresponding to the image pixels.

During random walks, swimmer may exit the biofilm domain. When the swimmer reaches the domain boundary, a new swimmer is introduced with a velocity oriented towards the interior of the domain while the original trajectory is stopped at the boundary.

### Sensitivity analysis

A local sensitivity analysis (Figure 1) is performed by comparing basal simulation obtained with $\gamma=\beta=ϵ=1$ (v0 and v1 where taken as in Appendix 1—table 3) with 3 simulations where $\gamma$, $\beta$ and $ϵ$ are alternatively set to 0, resulting in 3 alternative models where the speed or the direction selection or the random term is turned off. The interaction between the speed selection term (set by $\gamma$) and the random term is illustrated in Appendix 2—figure 3 where 5 repetitions of the same trajectory of a simplified Langevin equation (11) are displayed with or without friction ($\gamma=1$ or $\gamma=0$), but with the same random seed for the stochastic term so that the stochastic part is strictly identical.

To analyze the impacts of the non-dimensionalized swimming parameters $\gamma$, v0, v1, $\beta$, $ϵ$ on the locomotion behaviour, a global sensitivity analysis has been performed. The parameter space $[0,1]^{5}$ was uniformly sampled with n = 1000 points using the Fourier Amplitude Sensitivity Test (FAST) sampler of the SALib library that is the function SALib.sample.fast_sampler.sample (Cukier et al., 1973; Saltelli et al., 1999). We note that the interval $[0,1]$ covers a large parameter domain for some parameters, in particular $\beta$ which remains small after inference. For this parameter, the sensitivity analysis will show potential impact on the output, that may be ineffective in the parameter range of the inferred model.

For each point in the parameter space, a forward simulation is conducted on a population of swimmers on a representative biofilm extracted from the dataset (first batch of the B. pumilus dataset). Trajectory descriptors are then extracted and taken as observable of the sensitivity anaylsis that requires both the parameters sampling and the associated descriptors. Sobol indices of first order are then returned and pairwise partial correlations matrix has been calculated. Convergence of the Sobol indices has been checked by taking sub-samples containing less than $1,000$ points.

### Inference

#### Numerical implementation

The inverse problem (4)-(6) has been implemented using a Hamiltonian Monte Carlo (HMC) method to solve this Bayesian inference problem.

The three replicates for each swimmer species are pooled (trajectories and biofilm density maps) and the input data required for the inference procedure (velocity $yV$ and acceleration $yA$ times series for the whole batch of swimmers, biofilm densities $y⁢b$ and gradient $yGb$ extracted at swimmer positions) were assembled in a customed data structured. Normal standard prior distributions were set for all swimming parameters $\theta=(\gamma,v_{0},v_{1},\beta,ϵ)$. Additional positivity constrained were imposed for all parameters but $\beta$. Therefore, the implemented model can be summarized as:

$$
\theta∼N(0,1),\gamma\geq0,v_{0}\geq0,v_{1}\geq0,ϵ\geq0
$$



$$
yA∼N(f_{A}(\gamma,v_{0},v_{1},\beta|yb,yV,yb,yGb,dt),ϵ)
$$

A warmup of 1000 runs is followed by the Markov chains construction (4,000 iterations for 4 Markov chains). Markov chain convergence is assessed by direct visualization (Appendix 1—figure 4) by checking for biaised covariance structures in pair-plots (Appendix 1—figure 5). Standard convergence index were additionnaly computed: effective sample size per iteration ($n_{e⁢f⁢f}$) and potential scale reduction factor ($R_{h⁢a⁢t}$).

#### Noise model selection

Different noise models have been evaluated for the regression model (5) to take into account batch or individual effects. Namely, we decomposed the noise in Equation 5 by replacing $η^{s}$ by $ηsi$ and/or $η^{s,b}$ for individual $i$ and experimental batch $b$. Model selection has been conducted by computing the WAIC for the different noise models. A huge degradation of the WAIC has been observed for individual or batch dependant noises, indicating that the enhancement of the inference accuracy provided by the additional parameters can be considered as over-fitting and discarded.

### Inference validation on synthetic data

#### Ground truth data construction

Ground truth synthetic data (see section Assessment of the inference with synthetic data) were computed by solving Equations 2; 8 with $\gamma=10s^{-1}$, $v_{0}=5\mu⁢m.s^{-1}$, $v_{1}=1\mu⁢m.s^{-1}$, $\beta=10\mu⁢m.s^{-2}$, $ϵ=40\mu⁢m.s^{-2}$ and biofilm maps taken from the first batch of the B. pumilus dataset. The number of swimmers was fixed to $N=50$ and the number of time steps was taken identical to the experimental data that is $N_{t}=224$. Resulting mean speeds and accelerations were $A_{r⁢e⁢f}=68.29\mu⁢m.s^{-2}$, $V_{r⁢e⁢f}=7.47\mu⁢m.s^{-1}$ and were used to rescale the data before inference together with the ground truth parameters (Appendix 1—table 3). In total, the acceleration dataset contains 9,523 samples for each spatial direction.

#### Comparing ground truth data with the fitted model

After inference, a new dataset is obtained by solving Equation 8 with the fitted parameters. The same initial conditions for speeds and positions as the ground truth data are taken. Trajectories are stopped after the same number of time step as in the corresponding trajectory of the ground truth dataset. To discard spurious stochastic uncertainties, the same random seed as the ground truth simulations was taken, so that the unique uncertainty source was inference errors.

#### Checking the sensitivity to biofilm image noise

To produce Appendix 1—figure 6, the biofilm density and the biofilm density gradient maps have been noised with an additive gaussian noise with increasing variance, before inference: we set

$$
ϵ_{b}∼N(0,\sqrt{l}\sigma_{b})andϵ_{∇b}∼N(0,\frac{\sqrt{2l}}{Δx}\sigma_{b})
$$

where $\sigma_{b}$ is the variance observed in the original data, and $ϵ_{b}$ and $ϵ_{\nabla⁡b}$ are respectively the noise applied to the biofilm density and the biofilm density gradient. The parameter $l\in[0,0.01,0.02,0.03,0.04,0.05]$ is increased to apply a noise from 0% to 5%.

### Inference validation on experimental data

#### Comparing microscopy data with the fitted model

The same procedure is repeated on the microscopy data: after inference, a new dataset is obtained by solving Equation 8 with the fitted parameter, taking the same initial conditions for speeds and positions. Trajectories are stopped after the same number of time step as in the corresponding trajectory of the ground truth experimental dataset.

#### Measuring the deterministic reconstruction

The deterministic coefficient of determination $R_{d⁢e⁢t}^{2}$ was computed to measure how much the dataset is explained by the deterministic part of the model. Setting $A_{i}^{s,d⁢e⁢t}=f_{A}⁢(\gamma,v_{0},v_{1},\beta|y⁢b,yV,y⁢b,yGb,d⁢t)$:

$$
R_{d⁢e⁢t}^{2,s}=1-\frac{\sum_{i}(y⁢A_{i}^{s}-A_{i}^{s,d⁢e⁢t})^{2}}{\sum_{i}(y⁢A_{i}^{s}-y⁢A^{s}¯)^{2}}
$$

where $y⁢A^{s}¯$ is the acceleration mean. $R_{d⁢e⁢t}^{2,s}$ is expected to tend towards 1 when the stochastic term $η=N(0,ϵ)$ becomes negligible with respect to $A^{d⁢e⁢t}$.

### Plots and statistics

To allow inter-species comparisons in plots, the data and model outputs are re-normalized with common reference values $A_{r⁢e⁢f}$ and $V_{r⁢e⁢f}$ defined as the average of the species reference values (see Table 2 for values). Uni-dimensional distributions (Figure 5 upper panel, Figure 6b upper panel, Figure 7a, upper panel, and Figure 7b) were obtained with the gaussian_kde function of scipy.stats. T tests for mean comparison were performed using scipy.stats ttest_ind.

Two-dimensional distribution plots (Figures 5 and 6 b, Figure 7a lower panels) were obtained by first plotting the two-dimensional point cloud and approximating the point distribution with a gaussian KDE using scipy.stats gaussian_kde function. Then, the gaussian kde is evaluated at each point of the point cloud and quantiles 0.05, 0.5, and 0.95 of the resulting values are computed. Finally, quantile isovalues are plotted and the point cloud and the KDE are removed (see Appendix 4—figure 1 and Sec. KDE computation for details): this procedure ensures to enclose 5, 50% and 95% of the original points, centered in the densest zones of the initial point cloud.

Ternary plots (Appendix 2—figure 6) were obtained by first computing the contribution of each term of equation (4) to acceleration estimate. Namely, note

$$
s⁢(\nabla⁡b)_{i}^{s}=∥\beta^{s}⁢\frac{\nabla⁡b⁢(t,X_{i}^{s}⁢(t))}{∥\nabla⁡b⁢(t,X_{i}^{s}⁢(t))∥}∥, and  s⁢(η)_{i}^{s}=∥η^{s}∥.
$$



$$
s(Δb)_{i}^{s}=‖\beta^{s}\frac{Δb(t,X_{i}^{s}(t))}{‖Δb(t,X_{i}^{s}(t))‖}‖,ands(η)_{i}^{s}=‖η^{s}‖
$$

We compute the proportions $A⁢(k)_{i}^{s}$ for $k\in{b,\nabla⁡b,η}$,

$$
A⁢(k)_{i}^{s}=\frac{s⁢(k)_{i}^{s}}{s⁢(b)_{i}^{s}+s⁢(\nabla⁡b)_{i}^{s}+s⁢(η)}_{i}^{s}.
$$

Points $(A⁢(b)_{i}^{s},A⁢(\nabla⁡b)_{i}^{s},A⁢(η)_{i}^{s})$ are then plotted in ternary plots using the Ternary python package (Weinstein et al., 2019) and approximated by gaussian KDE. Isolines are finally plotted as previously described.

To construct the plot in Appendix 1—figure 2, pairwise correlation of the biofilm density in the 384 samples has been computed (scikit-learn pairwise_distances, ‘correlation’ metric parameter Pedregosa et al., 2011), and the resulting similarity matrix has been displayed using Seaborn package clustermap function (Waskom, 2021) after hierarchical clustering (scipy.cluster.hierarchy linkage function Virtanen et al., 2020). Additional permanova has been computed to assess the significance of between-group dissimilarities using stats.distance package permanova function (scikit-bio development team, 2020 ).

### Code availability

All the image pre- and post-processing, calculations and statistics have been performed with custom scripts using the standard python libraries numpy (Harris et al., 2020), scipy (Virtanen et al., 2020), imageio (Klein, 2021), and pandas (McKinney, 2010). The forward swimming problem computation is computed using customed scripts built upon numpy (Harris et al., 2020) and H5py (https://www.h5py.org). Sensitivity analysis has been conducted with the SALib library (Cukier et al., 1973; Saltelli et al., 1999) (Sobol index, function SALib.analyze.fast.analyze) and the pingouin library (Vallat, 2018) (PCC, pcorr method). The Bayesian inference has been conducted using the STAN library (Stan Development Team, 2018) through its python interface pystan (Riddell et al., 2021). All plots have been made with the matplotlib python library (Hunter, 2007).

The whole python code have been made available and accessible at the following git repository https://forgemia.inra.fr/bioswimmers/swim-infer.
