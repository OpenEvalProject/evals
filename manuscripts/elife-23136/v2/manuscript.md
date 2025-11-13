# Bacterial flagella grow through an injection-diffusion mechanism

## Authors

- Thibaud T Renault<sup>1</sup> ([ORCID: 0000-0002-1530-2613](https://orcid.org/0000-0002-1530-2613))
- Anthony O Abraham<sup>3</sup> ([ORCID: 0000-0002-8710-1351](https://orcid.org/0000-0002-8710-1351))
- Tobias Bergmiller<sup>4</sup>
- Guillaume Paradis<sup>5</sup>
- Simon Rainville<sup>5</sup>
- Emmanuelle Charpentier<sup>2</sup>
- Călin C Guet<sup>4</sup> ([ORCID: 0000-0001-6220-2052](https://orcid.org/0000-0001-6220-2052))
- Yuhai Tu<sup>6</sup> †
- Keiichi Namba<sup>3</sup> †
- James P Keener<sup>8</sup> †
- Tohru Minamino<sup>3</sup> †
- Marc Erhardt<sup>1</sup> ([ORCID: 0000-0001-6292-619X](https://orcid.org/0000-0001-6292-619X)) †

### Affiliations

1. Junior Research Group, Infection Biology of Salmonella Helmholtz Centre for Infection Research Braunschweig Germany
2. Max Planck Institute for Infection Biology Berlin Germany
3. Graduate School of Frontier Biosciences Osaka University Osaka Japan
4. Institute of Science and Technology Austria Klosterneuburg Austria
5. Department of Physics, Engineering Physics and Optics Laval University, Quebec City Quebec Canada
6. IBM Thomas J Watson Research Center New York United States
7. RIKEN Quantitative Biology Center Suita Japan
8. Department of Mathematics University of Utah Salt Lake City United States

† Corresponding author

## Abstract

The bacterial flagellum is a self-assembling nanomachine. The external flagellar filament, several times longer than a bacterial cell body, is made of a few tens of thousands subunits of a single protein: flagellin. A fundamental problem concerns the molecular mechanism of how the flagellum grows outside the cell, where no discernible energy source is available. Here, we monitored the dynamic assembly of individual flagella using in situ labelling and real-time immunostaining of elongating flagellar filaments. We report that the rate of flagellum growth, initially ∼1,700 amino acids per second, decreases with length and that the previously proposed chain mechanism does not contribute to the filament elongation dynamics. Inhibition of the proton motive force-dependent export apparatus revealed a major contribution of substrate injection in driving filament elongation. The combination of experimental and mathematical evidence demonstrates that a simple, injection-diffusion mechanism controls bacterial flagella growth outside the cell.

## Introduction

Many bacteria move by rotation of a helical organelle, the flagellum. The external flagellar filament is several times longer than a bacterial cell body and is made out of up to 20,000 flagellin subunits (Berg and Anderson, 1973; Chevance and Hughes, 2008; Macnab, 2003; Silverman and Simon, 1974) (Figure 1a). A type III export apparatus located at the base of the flagellum utilizes the proton motive force (pmf) as the primary energy source to translocate axial components of the flagellum across the inner membrane (Minamino and Namba, 2008; Paul et al., 2008; Minamino et al., 2011; Erhardt et al., 2014). Exported substrates travel through a narrow 2 nm channel within the structure and self-assemble at the tip of the growing flagellum. It has been a mystery how bacteria manage to self-assemble several tens of thousands protein subunits outside the cell, where no discernible energy source is available. Previous reports in the literature concerning the mechanism of flagellum growth have been conflicting (Iino, 1974; Aizawa and Kubori, 1998; Turner et al., 2012; Evans et al., 2013). An exponential decay of filament elongation with length was observed using electron microscopic measurements, which was proposed to be a result of decreased translocation efficiency (Iino, 1974; Tanner et al., 2011). A recent study used dual-colour fluorescent labelling of flagellar filaments to distinguish basal from apical filament growth and found that the rate of polymerization was independent of filament length (Turner et al., 2012; Stern and Berg, 2013). A model based on the pulling force of a filament-spanning chain of flagellin subunits was proposed to explain the apparent length-independent growth (Evans et al., 2013).

![Figure 1.](https://cdn.elifesciences.org/articles/23136/elife-23136-fig1-v2.jpg)

**Figure 1.:** (a) Schematic depiction of the bacterial flagellum and proposed models to explain the filament elongation dynamics (Iino, 1974; Turner et al., 2012; Evans et al., 2013). OM=outer membrane, IM=inner membrane. (b) Top: Electron micrograph images of mutants deficient in the hook-filament junction protein FlgK or the flagellin-specific chaperone FliS. Bottom: Immunoblotting of cellular and Coomassie-staining of secreted flagellin (FliC) in ∆flgK and ∆fliS mutant strains (relative secreted flagellin levels report mean ± s.d., n = 3). (c) Representative images of a population-based flagellin immunostaining time-course. Time in minutes after induction of flagellin synthesis is indicated. (d) Continuous in situ flagellin immunostaining reveals elongation kinetics of individual filaments in real time. Exemplary movie frames are shown and elapsed time in minutes after start of imaging is indicated. (e) Quantification of the population immunostaining. Measured filaments per group: t15’ (n = 187), t30’ (n = 206), t45’ (n = 480), t60’ (n = 648), t90’ (n = 700), t120’ (n = 827), t180’ (n = 302), t240’ (n = 172). The box plot reports the median (in red), the 25th and 75th quartiles and the 1.5 interquartile range. (f) Quantification of the continuous in situ flagellin immunostaining. The dark line represents the global, averaged fit of 8 individual filaments. Raw data shown as coloured dots excluding measurement incidents as explained in Figure 1—figure supplement 2. The initial velocity (Vi) was measured on the initial, linear part of the growth curve. Scale bars 2 µm.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/23136/elife-23136-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (a) Schematic overview of experimental setup to determine flagellin leakage during filament assembly. The black elements represent the quantified fractions. (b) Coomassie-staining of total extracellular flagellin (filaments attached to cell bodies and flagellin secreted into culture supernatant), polymerized flagellin (filaments attached to cell bodies), detached and secreted flagellin (FliC detected in culture supernatant), detached flagellin (filaments detached from cell bodies as collected by ultracentrifugation of cleared culture supernatant) and secreted flagellin (FliC monomers detected in the culture supernatant after ultracentrifugation) of wild-type (WT) and ∆flgK mutant strains. Relative extracellular flagellin levels in the wild-type were 1.000 ± 0.175 for total extracellular flagellin, 0.756 ± 0.046 for polymerized flagellin, 0.239 ± 0.037 for detached and secreted flagellin, 0.057 ± 0.036 for detached flagellin and 0.085 ± 0.021 for secreted flagellin (mean ± s.d., n = 4).

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/23136/elife-23136-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** Raw data measurements of the real-time growth of individual filaments and corresponding fits to the saturated diffusion model are shown. The dashed grey line represents the global fit depicted in Figure 1f and the solid black line represents the fit computed for the individual filament. Arrows denote growth or measurement incidents (e.g. filament diffused out of focus, the filament stopped growing until the end of the experiment or the cell body rotated thereby preventing accurate length measurements, see Video 1). Only the growth rate data before the arrows were used to fit the model.

## Results and discussion

### Enhanced flagellin export in the absence of assembled filament

In order to test whether filament length itself affects the export rate of flagellin subunits during filament formation, we constructed a flagella-assembly mutant deleted for the first hook-filament junction protein (ΔflgK). This resulted in direct secretion of flagellin monomers into the culture media without transport through the elongated filament. The total amount of extracellular flagellin was analysed in the wild-type and the ΔflgK mutant by de-polymerizing flagellar filaments into flagellin monomers using heat treatment at 65°C. The amount of extracellular flagellin was approximately 1.6-fold higher in the ΔflgK mutant compared to wild-type cells. Consistently, cytoplasmic flagellin was substantially more abundant in the wild-type than in the ΔflgK mutant (Figure 1b). Measurements of flagellin leakage during filament formation revealed that only a small fraction of the total flagellin is leaked in monomeric form by wild-type cells during filament formation (Figure 1—figure supplement 1), demonstrating that the majority of exported flagellin subunits are incorporated into the growing filament under our experimental conditions. These results indicate that the presence of an assembled filament decreases the rate of flagellin transport, which is consistent with the decreased rates of FlgE and FliK export in a long hook mutant (Koroyasu et al., 1998; Erhardt et al., 2011). A similar filament length-dependent effect on flagellin transport was also observed in a mutant of the flagellin-specific cytoplasmic chaperone FliS (Figure 1b). FliS promotes docking and subsequent unfolding of flagellin at the export apparatus (Kinoshita et al., 2013; Furukawa et al., 2016), suggesting that the flagellin injection rate at the export apparatus substantially contributes to the flagellum growth dynamics.

### The elongation rate of bacterial flagella inversely correlates with filament length

We next measured the growth kinetics of flagellar filaments to determine the relation between growth rate and filament length. We engineered a Salmonella strain where the production of flagellar basal bodies (using the flhDC flagellar master regulatory operon under control of a anhydrotetracycline inducible promoter) is uncoupled from the expression of chromosomally-encoded flagellin (using the flagellin gene fliC under control of an arabinose inducible promoter). This well-established setup allowed for synchronization of flagella production (Erhardt et al., 2011; Karlinsey et al., 2000) by first assembling basal bodies before initiating filament synthesis. The flagella of the synchronized culture were immunostained after increasing growth times (Figure 1c). The initial filament growth rate was ~83 nm∙min−1, which decreased over time (Figure 1e). In a complementary approach, we monitored, in real-time, the dynamic assembly of individual filaments by employing a continuous in situ immunostaining approach (Berk et al., 2012) to visualize growing flagella (Figure 1d, Video 1). A Salmonella strain harbouring a functional, hemagglutinin-epitope tagged flagellin variant under its physiological promoter was grown in a microfluidic device in the presence of labelled, primary antibodies. We observed an initial filament growth rate of ~100 nm∙min−1, which decreased over time similar as for the population-wide approach described above (Figure 1f, Figure 1—figure supplement 2).

![Video 1.](https://cdn.elifesciences.org/articles/23136/elife-23136-media1.mp4.jpg)

**Video 1.:** The animation represents the raw data of the filament length measurements of five representative flagella as a function of time. The inset depicts a 400× time-lapse movie of the corresponding microcolony grown in a CellASIC microfluidic device in the presence of 10 nM anti-HA fluorochrome-coupled primary antibodies. Elapsed time is depicted in min’sec’’. Coloured circles highlight the onset of filament assembly of the respective length measurement data. Arrows denote growth or measurement incidents (e.g. filament flipped out of focus or broke off). Scale bar 1 µm.

In a previous study, Turner et al. (2012) measured the growth kinetics of individual filaments in Escherichia coli by site-specific labelling of flagellin subunits containing an exposed cysteine residue using sulfhydryl-specific (maleimide) fluorochromes and reported a length independent growth rate of ~13 nm∙min−1. We optimized this method to exchange dyes multiple (three to six) times in situ during normal culture growth with minimal perturbation of bacterial growth (Figure 2, Figure 2—figure supplement 1, Figure 2—figure supplement 2, Figure 3, Figure 3—figure supplement 1). The labelling of successive fragments of the flagellum with maleimide fluorochromes in situ allows observation of the filament growth dynamics at the end of the experiment. Triple labelling (exchange of dyes three times) demonstrated that the extension length of the filament (apical fragment) is inversely proportional to its initial length (basal fragment), until the growth rate for long filaments decreases to a point where it becomes minimal (Figure 2). Using this setup, the dynamic range of basal fragment lengths was increased by performing the experiment with varying growth durations (15 to 180 min).

![Figure 2.](https://cdn.elifesciences.org/articles/23136/elife-23136-fig2-v2.jpg)

**Figure 2.:** (a) Experimental design of the in situ triple-colour labelling time-course. Basal (F1) and apical (F2) fragments were grown for 15–180 min and 30 min, respectively. The growth duration of basal fragments is indicated in the legend. Coloured arrows indicate the coordinates of the representative example images. The fit represents the injection-diffusion model with parameters kon ≈ 33.35 s−1and D ≈ 5.90 × 10−13 m2 ⋅ s−1. Scale bar 2 µm. (b) Average size of the individual fragments for different durations of elongation of the first fragment. Error bars represent the 95% confidence interval of mean estimation. (c) Relation between the size of the second and third fragment. 93.4% of the filaments have F3 fragments shorter than the F2 fragment with the difference increasing with the length of F2. (d) Flagella labelled in panel a were measured and sorted according to the length of F1, which reveals the inverted relationship between the initial length and extension length of the filament. Each vertical line represents an individual filament (n = 1254).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/23136/elife-23136-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (a) Localization of the T237 residue in FliC, mutated to cysteine for the fluorochrome-maleimide labelling. The inset shows the structure of the polymerized filament with the localization of T237 in red. (b) Filament length distribution of the FliCT237C mutant strain EM2046 after 1 hr of growth in presence of the maleimide fluorochrome (Mal488) is identical to the wild-type (TH15801) grown in the same conditions or in absence of the maleimide fluorochrome in the medium. The box plot reports the median (in red), the 25th and 75th quartiles and the 1.5 interquartile range. (c) Representative images of the triple labelling of strain EM2400 with constant induction of FlhDC. Variations in F1 growth time (30 min and 60 min) demonstrate length-dependent decrease in filament growth rate. Scale bar 2 µm. (d) Triple filament labelling after constant (left, compare also panel c) or transient (right) induction of FlhDC led to comparable fragments size (n = 417 filaments for constant AnTc, n = 1254 filaments for AnTc pulse). Variations in F1 growth time (30 min and 60 min) highlight the length-dependent filament elongation rate. Error bars represent the 95% confidence interval of mean estimation. (e) Representative images for multiple labelling of strain EM2400 with constant (left) or transient (right) induction of FlhDC. Transient induction of FlhDC decreases the number of flagella per cell without changing the growth kinetics (see panel d), and accordingly facilitated quantitative analysis of filament length. Scale bar 2 µm.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/23136/elife-23136-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (a) Triple labelling with time course of the second fragment (F2), the first and third fragment were grown for 30 min. The dotted lines, shown for comparison, are the fit lines of the 30 and 60 min curves of the multiple labelling in Figure 3c. (b) Average length of the fragments for the different time points. Error bars represent the 95% confidence interval of mean estimation.

![Figure 3.](https://cdn.elifesciences.org/articles/23136/elife-23136-fig3-v2.jpg)

**Figure 3.:** (a) Left: Experimental design of the in situ, multicolour labelling. Right: Representative fluorescent microscopy image for multiple labelling of flagellar filaments with a series of maleimide dyes. TB: tryptone broth without dye, AnTc: anhydrotetracyline induction of flagella genes. Scale bar 2 µm. (b) Basal/apical length coordinates were obtained by varying the duration of basal growth and successive fragments were combined to generate a total of 1276 basal/apical coordinates from 291 filaments. The growth duration of the apical fragment was 30 min. Average speeds are calculated from the average elongation per 30 min (<1 µm or >8 µm). The fit represents the injection-diffusion model with parameters kon ≈ 27.09 s−1and D ≈ 5.41 × 10−13 m2 ⋅ s−1. (c) Basal/apical length coordinates were obtained for various durations of apical growth (30–150 min) from the multiple labelling data shown in panel b. (n = 1276 for 30 min, n = 986 for 60 min, n = 697 for 90 min, n = 422 for 120 min, n = 169 for 150 min). The fit for various durations of apical growth represents the injection-diffusion model with parameters kon and D (60 min: kon ≈ 27.72 s−1, D ≈ 5.56 × 10−13 m2 ⋅ s−1; 90 min: kon ≈ 28.06 s−1, D ≈ 5.63 × 10−13 m2 ⋅ s−1; 120 min: kon ≈ 27.03 s−1, D ≈ 5.42 × 10−13 m2 ⋅ s−1; 150 min: kon ≈ 26.36 s−1, D ≈ 5.29 × 10−13 m2 ⋅ s−1). Average growth rates were estimated from the Y-intercept of the fit curve. The inset presents the average growth plotted against time. (d) Filament length as a function of time of individual flagella from the multiple labelling data. Each grey line represents the growth curve of an individual filament. The average growth rates estimated in panel c are plotted for comparison. (e) Quality of multiple labelling data. Only a minor fraction of the filaments were broken or stalled (highlighted as red dots, Figure 3—figure supplement 1a), which has limited effect on the parameter fit.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/23136/elife-23136-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (a) Raw data of the multiple labelling. Each vertical line represents an individual filament (n = 291). Broken or strongly stalled filaments are denoted with a white arrow. Basal/apical length coordinates resulting from those filaments are highlighted in red in Figure 3e. (b) Basal/apical couples, as calculated in Figure 3c are shown in green/red, respectively. The elongation time of the apical fragment is indicated on top of each graph. Smoothing was applied on the apical data using exponentially weighted moving averages (span = 50) to remove the individual-based variability. The smoothed data is represented for each elongation time as a dotted line. (c) Comparison of the triple labelling data (1254 fragments) and the multiple labelling data for 30 min elongation (1276 fragments derived from 291 flagella). The multiple labelling allows obtaining greater resolution with about four times less flagella. (d) Basal/apical coordinates were obtained by smoothing of the raw data as described in panel b. The growth curves from Figure 3c are plotted for comparison.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/23136/elife-23136-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (a) The combined multiple-labelling approach and the in vitro labelling protocol ensured minimal filament breaks in our dataset (Figure 3—figure supplement 1a, compared to breaks induced by shearing in Figure 4). Each filament of the dataset was subjected to a virtual breakage/stalling event with a probability pbreak (pbreak = 0, 0.1, 0.25, 0.5, 0.75 or 1). The position of the breakage/stalling event was chosen randomly along the length of the filaments with a uniform probability. (b) Simulation of random filament breakage (of probability p) using the multiple labelling dataset presented in Figure 3. The random filament breakage simulation demonstrates that data points accumulate on the x-axis and below the fit curve (in red). It is crucial to note that a high fraction of broken filaments masks the obvious length-dependency of filament growth and prevents an accurate fit on the complete set of points (linear fit in blue; compare with Figure 3 of Turner et al. [2012]). (c) Combination of the data obtained in Figure 6a for the 0, 10, and 20 µM CCCP concentrations to simulate a heterogeneous injection rate. A variable injection rate within the population would mask the length-dependency of filament growth (compare with Figure 3A of Turner et al. [2012]).

Next, multiple labelling (exchange of dyes six times) of flagellar filaments allowed us to compute various basal/apical couples and increased the dynamic range of the growth rate data for individual flagella. The multiple labelling of flagellar filaments confirmed the length-dependent elongation mechanism with an elongation speed decreasing gradually from ~100 nm∙min−1 to ~20 nm∙min−1 (Figure 3, Figure 3—figure supplement 1). Alternative combination of the fragments allowed us to determine the filament elongation kinetics for various growth durations and in fine to derive a growth curve (Figure 3c–d). Our method further allowed us to exclude stalled or broken filaments and study the filament elongation dynamics under normal cultivation conditions for a wide range of fragment lengths. We note that we only observed a minor fraction of flagella that broke or stopped growing during the experiment (Figure 3e).

### An injection-diffusion mechanism explains the growth dynamics of flagellar filaments

The solid curves in Figure 2 and Figure 3 represent the best fit of the data to a growth curve for which the growth rate is a function of the length L of the form $\frac{a}{b+L}$, where the parameter a has units of a diffusion coefficient, and b has units of length. Derivation of this formula is based on an injection-diffusion model where flagellin monomers, which are at least partially α-helical inside the channel (Shibata et al., 2007), are pushed by a pmf-driven export apparatus into the channel and move diffusively in one dimension through the length of the flagellum (Stern and Berg, 2013; Keener, 2006). An analytical expression for the flagellum length dependent growth rate is based on a continuum injection-diffusion model for the growth of flagellar filaments. Monomers (each of length l) in the growing filament are assumed to move diffusively. Because the filaments are long narrow tubes, monomers are partially unfolded and diffusion is constrained to be strictly one-dimensional, i.e. no passing allowed. In the corresponding continuum model, we define $\frac{u(x,t)}{l}$ as the density of monomers per unit length at position x and time t. Then u satisfies the diffusion equation

$$
u_{t}=Du_{xx}.
$$

Here, D is the diffusion coefficient of the monomers. We assume that all end-to-end collisions between monomers are ballistic, with no end-to-end binding. For this, Fickian diffusion is the appropriate description of diffusion, even at high densities. We assume that at the growing end $X=L$, monomers are quickly removed by folding/polymerization so that effectively $u(L,t)=0$.

The details of the mechanism by which monomers are secreted at the basal end $X=0$ is not known, but it is known to be related to the pmf (Paul et al., 2008). We assume that the rate of secretion (number of monomers per unit time) into an empty filament is $K_{on}$, but if it is not empty, then the rate of secretion is decreased because of the no-passing restriction. Consequently, the flux $J_{0}$ (number of monomers per unit time at the basal end) is taken to be

$$
J_{0}=\frac{−D}{l}u_{x}(0,t)=K_{on}(1−u(0,t)).
$$

Finally, the rate of growth of the filament is given by

$$
\frac{dL}{dt}=\betaJ_{L}=\frac{−D\beta}{l}u_{x}(L,t),
$$

where $\beta$ is the length increment of the filament due to polymerization of a single monomer.

Since the filament growth rate is small compared to the average velocity of monomers, it is reasonable to take the monomer diffusion to be in quasisteady state, i.e. $u_{xx}=0$. Thus, the monomer density in the filament is a linearly decreasing function and ux is the constant $\frac{−u(0)}{L}$. It follows that the filament growth rate is

$$
\frac{dL}{dt}=\frac{\betaD}{l}\frac{1}{\frac{D}{k_{on}l}+L}=\frac{a}{b+L},
$$

where $a=\frac{\betaD}{l}$, with units of diffusion, and $b=\frac{D}{k_{on}l}$, with units of length. This is readily solved to find the filament length as a function of time

$$
L(t)=−b+\sqrt{b^{2}+2at}.
$$

We can estimate the diffusion coefficient using $a=\frac{\betaD}{l}$, so that

$$
D=\frac{al}{\beta}.
$$

From all the datasets presented above, we determined a ≈ 0.2 µm2 ⋅ min−1. Using β = 0.47 nm (a flagellar filament of 1 µm length is composed of approximately 2130 flagellin subunits [Yonekura et al., 2003]), l = 74 nm (assuming an extended, α-helical flagellin molecule) this leads to an estimate of D ≈ 5.25 × 10−13 m2 ⋅ s−1. Stern and Berg (Stern and Berg, 2013) estimated D ≈ 5.78 × 10−11 m2 ⋅ s−1 for freely moving α-helical flagellin in water. The actual diffusion coefficient for movement in the narrow 2 nm channel would be substantially smaller, however. Stern and Berg (Stern and Berg, 2013) (their Figure 2) used a 480 times smaller diffusion coefficient (D ≈ 1.25 × 10−13 m2 ⋅ s−1) for numerical simulations that resulted in a declining growth curve, which closely resembled the filament growth kinetics presented above.

Our triple and multiple labelling experiments demonstrated that the growth of a new part of the filament (apical fragment) shows a strong inverse dependence on its initial length (basal fragment) for short filaments, while the growth rate for long filaments decreases to a point where this dependence becomes minimal (Figure 2, Figure 3, Figure 3—figure supplement 1). We note that several differences in the experimental setup of Turner et al. (2012) from ours might have affected the injection rate and frequency of filament breakage. As described in detail in Appendix 1, the possibility of broken/stalled filaments and possible perturbations of the injection rate reconcile our data with the reported filament growth data of Turner et al. (2012) and explains why we observed a length-dependent decrease in growth rate. In support, we simulated in Figure 3—figure supplement 2 the effects of filament breaking/stalling events and heterogeneous injection rates. The simulated broken/stalled filaments accumulate on the x-axis, which results in a quasi-linear fit of the complete filament growth rate data, similar to the linear filament growth observed by Turner et al. (2012).

We further note that a length-dependent decrease in filament growth rate would explain why flagellar filaments do not growth indefinitely. However, flagellar filaments broken by mechanical shearing forces can re-grow (Turner et al., 2012; Rosu and Hughes, 2006; Vogler et al., 1991). The injection-diffusion model predicts that the elongation rate of re-growing filaments would increase compared to unbroken filaments. We performed multiple labelling in situ to determine the growth rate of individual filaments that had been broken using mechanical shearing forces. Consistent with the injection-diffusion mechanism, the elongation rate of re-growing, previously broken filaments was substantially faster than the elongation rate of unbroken filaments and was dependent on the length of the basal filament segment, which remained attached to the bacterial cell surface (Figure 4).

![Figure 4.](https://cdn.elifesciences.org/articles/23136/elife-23136-fig4-v2.jpg)

**Figure 4.:** (a) Experimental design to determine filament elongation rate after mechanical shearing using multicolour labelling. (b) A successful shearing event removed fragment F3 and partially or completely fragment F2. (c) Representative example images of control filaments and filaments broken using mechanical shearing forces. Flagellar filaments were sheared by passing the bacterial culture five times (mild shearing) or up to 30 times (strong shearing) in and out of a 22-gauge needle. Scale bar 2 µm. (d) Left panel: length of the basal, cell-attached filament after mechanical shearing demonstrating successful filament breakage. Right panel: length of apical, re-growing filament fragments demonstrating a length-dependent increase in filament elongation rate. The box plots reports the median, the 25th and 75th quartiles and the 1.5 interquartile range. Data points represent individual filament fragments. Statistical significance according to a two-tailed Student’s t-test is indicated. F4 strong vs. control: p-value=0.000026 (***); F5 strong vs. control: p-value=0.002452 (**); F6 strong vs. control: p-value=0.034514 (*); F7 strong vs. control: not significant (n.s.).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/23136/elife-23136-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Basal/apical coordinates of the data shown in Figure 4d of control filaments and filaments broken using mechanical shearing forces. The length of the apical F4 fragment (post-shearing) is shown in relation to the length of the basal fragment pre-shearing (F1→F3) and highlights the increased elongation rate of short filaments after shearing.

### Inter-subunit chain formation does not contribute to flagella growth dynamics

Based on the observations of Turner et al. (2012), Evans et al. (2013) developed a model where folding of newly arriving subunits at the tip of the flagellum would provide energy to pull successive subunits through the channel at a constant rate. Evans et al. demonstrated that N-terminal regions of flagellar substrates (FlgD, FlgE, FlgG and FliK) can bind to the C-terminal cytoplasmic domain of FlhB, which is a component of the pmf-driven transmembrane export gate complex. Further, site-specific cysteine-cysteine crosslinking showed that the N- and C-terminal regions of hook (FlgE) and flagellin (FliC) can interact to form head-to-tail dimers. They hypothesized that formation of inter-subunit chains resulting from those interactions could enable their transport at a length-independent speed, as the folding of the exported molecules at the filament tip would provide a continuous pulling force. While the N- and C-terminal interactions of flagellar substrates might play an important role during substrate docking and in the final fold of assembled hook and filament subunits, the proposed inter-subunit chain mechanism for flagellin transport and filament assembly raises several issues that are incompatible with the known biophysical properties of flagellum assembly (Yonekura et al., 2003; Samatey et al., 2001). A flagellum-spanning chain requires interactions of the N- and C-terminal α-helical domains of flagellin, but the 2 nm wide filament channel (Yonekura et al., 2003) is too narrow to accommodate the secretion of much more than one folded α-helix (Figure 5a). The chain mechanism hypothesizes that folding of a flagellin subunit at the tip of the flagellum can pull a chain of succeeding subunits, but the N- and C-termini of successive flagellin molecules are anti-parallel and far apart in the polymerized filament structure (∼17 Å on average) (Yonekura et al., 2003; Samatey et al., 2001) (Figure 5b). Further, the chain mechanism is not compatible with simultaneous secretion of non-chaining substrates (Figure 5d). Flagellar substrates such as FlgM or excess hook-associated proteins (FlgK, FlgL, FliD) are constantly exported during flagellum growth (Komoriya et al., 1999) and do not interact with flagellin (Furukawa et al., 2002). Also, premature termination of translation is occurring frequently (~1∙10−4 to ~5∙10−4 events per codon) (Sin et al., 2016). Thus, a high proportion of 5–20% newly synthesized flagellin might be truncated for the C-terminal domain needed for head-to-tail chain formation. We estimate that secretion of as little as one non-chaining substrate every 10,000 full-length flagellin molecules would prevent filament elongation if a chain mechanism drives flagellum growth (Figure 5d–g).

![Figure 5.](https://cdn.elifesciences.org/articles/23136/elife-23136-fig5-v2.jpg)

**Figure 5.:** (a) The 2 nm wide filament channel only accommodates one folded α-helix. (b) The N- and C-termini of successive flagellin molecules are anti-parallel and far apart in the polymerized filament structure. (c) Top: Structure, domains, and secondary structures of flagellin FliC (PDB: 1UCU). Mutant flagellins lacking combinations of the N- and C-terminal domains required for head-to-tail coiled-coil chaining (ΔN, ΔCS, ΔCL) were co-expressed together with endogenous flagellin (FliC) to disrupt chain formation. Bottom: Flagellin immunoblotting on cellular and secreted fractions (relative full-length flagellin levels report mean ± s.d., n = 3). (d) Simultaneous secretion of non-chaining substrates breaks a filament-spanning chain of flagellin molecules. A strict chain model requires the chain to span the entire filament and does not allow for disruptions of the chain. A chain model with the possibility of recovery by diffusion of broken chains is discussed in Figure 5—figure supplement 1. (e) In situ, multicolour labelling of flagellar filaments during competitive co-expression of chain-disrupting mutant flagellins. The average growth of fits computed from basal/apical coordinates presented in Figure 5—figure supplement 3c and as described in Figure 3c is shown as a function of time. Basal/apical coordinates were derived from multiple labelling data of individual filaments: n = 399 from 89 filaments (−), n = 271 from 58 filaments (WT), n = 278 from 62 filaments (∆CL), n = 412 from 93 filaments (∆N ∆CL), n = 209 from 46 filaments (∆CS), n = 312 from 73 filaments (∆N ∆CS). The fits represent the injection-diffusion model and parameters kon and D are given in Figure 5—source data 1. (f) Probability of existence of n-long chains defined by the binomial law. Long chains are highly improbable for a 15% proportion of competing substrates (i.e. formation of a more than 2.4 µm long chain (n > 33) has a probability of 1%). The bars show the individual probability of existence, the dotted blue line the cumulated probability of existence of chains longer than the number on the x-axis. The grey curve indicates the chain length in µm, which reflects that filaments cannot grow longer than a few hundred nanometres with a chain-based mechanism. (g) Simulation of filament growth dependent on inter-subunit chains or the injection-diffusion model in presence of random proportion of competing substrate. The injection-diffusion model fit represents the mean of the multi-labelling data set of Figure 3 with parameters kon ≈ 27.25 s−1and D ≈ 5.46 × 10−13 m2 ⋅ s−1. Dashed white line: median length of the filament for chain-model dependent growth. Grey box: expression range of chain-disrupting mutant flagellins used in panel e and Figure 5—figure supplement 1a.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/23136/elife-23136-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (a) Effect of deletion of fliS on secretion of flagellin truncation mutants. Anti-flagellin immunoblotting of secreted wild-type flagellin and flagellin truncation mutants. The flagellin truncation mutants additionally missing the FliS binding site (ΔN = ∆29–32, ΔCS = ∆450–495, ΔCL = ∆310–495) were secreted in similar quantity in both the wild-type and ∆fliS mutant. Full-length flagellin was expressed from its native promoter. (b) Schematic illustration of chain-model dependent filament growth. Unlike the simulation presented in Figure 5, we assume here that filament growth can resume after the basal part of the chain diffused to the tip. The diffusion coefficient depends on the number of flagellin subunits in the chain. (c) Simulation (n = 100) of filament growth in the presence of 10–20% competing substrate. At this proportion of competing substrates, chains would constantly be broken and have an average size of 6–11 subunits. This would induce significant delays in growth, which is not observed experimentally (Figures 1f and 5e). The dynamics of filament growth dependent on the injection-diffusion mechanism would not be perceptibly altered by this proportion of competing substrates and is consistent with the experimental observations (Figure 5e). (d) Simulation of chain-model dependent filament growth. In contrast to the simulation presented in Figure 5g, here we allow for recovery upon a chain-breaking event by diffusion of the basal chain fragment to the tip, where it resumes growth. This simulation reveals two ranges of possible chain model dependent filament growth. The first one (proportion of competing substrate p<10−4) is identical to the model without possibility to recover upon chain-breakage and requires a non-physiological low proportion of competing substrates. In this case chains are so long that it is virtually impossible to diffuse to the tip within the time frame of the simulation, thus effectively arresting filament elongation. The second range where a chain model dependent growth is valid (p>0.3) postulates frequent chain-breakage events. Here, short chains (1–5 flagellin subunits) are able to diffuse to the tip in a reasonable time frame, however, the contribution of the pulling force of such short chains to drive elongation of the filament is negligible and secretion of substrates is almost entirely driven by diffusion. The simulation of Figure 5g is shown in blue for comparison. The simulation with the injection-diffusion model is shown as a red dashed line. In all models, export starts to be affected by competition for injection when the number of competing substrates is significantly higher than the number of secreted flagellin molecules.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/23136/elife-23136-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** The simulation generates a random succession of substrates with a certain probability of non-chaining substrates incorporated into the chain of substrates that arrive at the export gate. If flagellin substrates arrive, they participate in filament elongation with the observed rate of growth. If, however, a non-chaining substrate arrives at the gate, then the simulation does either not allow for recovery of growth (top and bottom left) or introduces an elongation delay based on the time required for the newly formed basal chain to reach the tip through diffusion, where it then can resume rapid growth (middle and bottom right).

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/23136/elife-23136-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** (a) Schematic of flagellin FliC truncation constructs used to disrupt subunit chain formation. Overview of various flagellin mutants lacking parts and/or combinations of N- and C-terminal domains required for head-to-tail chain formation. Qualitative assessments of the ability to complement a fliC mutant strain (labelled ‘complementation’), the ability to form functional flagellar filaments (labelled ‘assembly’) and the secretion levels are indicated. Truncations in the D0 domain were expected to prevent flagellin polymerization and thus the truncation mutants do not assemble filaments and are unable to complement a fliC mutant strain. Overproduction of N-terminal domain truncation mutants that retain the C-terminal chaperone-binding domain competes with wild-type flagellin for the available pool of flagellin-specific chaperone FliS (Figure Supplement S6a). The absence of FliS impairs filament formation (Figure 1b) and thus overproduction of ∆29–33, ∆11–18 and ∆11–18 + ∆29–33 results in a dominant-negative motility phenotype. N.D. = not determined. (b) Expression and secretion profile of flagellin truncation mutants. Western blot analysis of cellular and supernatant fractions of strain TM113 (∆fliC) or strain NH001 (∆flhA) expressing various flagellin truncation variant as outlined in panel a. All flagellin mutants are secreted in the presence of a functional flagellar export apparatus. (c) Mutant flagellins lacking parts or combinations of the N- and C-terminal domains required for head-to-tail chain formation (ΔN = ∆29–32, ΔCS = ∆450–495, ΔCL = ∆310–495) or wild-type flagellin (WT) were co-expressed together with endogenous flagellin in strain EM2400 as shown in Figure 5. Multicolour labelling of flagellar filaments was performed and basal/apical coordinates were computed for various durations of apical growth and plotted as outlined in Figure 3c. Successive fragments of individual filaments were combined to obtain n basal/apical coordinates as follows: n = 399 from 89 filaments (−), n = 271 from 58 filaments (WT), n = 278 from 62 filaments (∆CL), n = 412 from 93 filaments (∆N ∆CL), n = 209 from 46 filaments (∆CS), n = 312 from 73 filaments (∆N ∆CS). The fits represent the injection-diffusion model. Parameters kon and D are given in Figure 5—source data 1.

To test the requirement of subunit chain formation for flagellum growth in more detail, we generated flagellin mutants truncated for the N- and C-termini that render head-to-tail linkage impossible (Figure 5c). All flagellin truncation mutants were secreted, but were deficient in flagellum assembly due to deletions in the D0 and D1 domains needed for filament polymerization and FliS chaperone binding (Yonekura et al., 2003) (Figure 5—figure supplement 1a, Figure 5—figure supplement 3). We expressed those non-chaining, but secreted flagellin mutants in trans to disrupt formation of a chain of wild-type flagellin molecules (Figure 5d). Competitive secretion of the flagellin truncation mutants did not affect endogenous flagellin transport during filament formation (Figure 5c). Filament extension kinetics were determined using multiple labelling of individual flagellar filaments and, similarly, no significant difference was observed when chain-disrupting flagellin mutants were co-expressed (Figure 5e, Figure 5—figure supplement 3c).

Mathematical modelling of the chain model-dependent filament elongation dynamics predicted a linear growth up to a very long flagellum (>0.1 mm), which is in clear contradiction with the experimental observations (Appendix 2).

### Inhibition of the pmf-dependent protein export prevents filament elongation

Our high-resolution filament growth rate data and the previous observations by Stern and Berg (2013) suggested that two major components drive flagellin export: pmf-dependent injection of subunits by the type III export apparatus at the base of the flagellum and diffusion of subunits along the length of the flagellum. We used carbonyl cyanide m-chlorophenyl hydrazone (CCCP) to disrupt the pmf, which is required for substrate translocation via the export apparatus into the central channel of the growing flagellar structure (Minamino and Namba, 2008; Paul et al., 2008). The injection-diffusion model predicts that a decrease in the injection rate Kon results in slow, quasi-linear growth for sufficiently small Kon. As expected, CCCP treatment resulted in impaired filament extension in a dose-dependent manner, which recovered upon removal of the uncoupler (Figure 6a, Figure 6—figure supplement 1). We hypothesized that in presence of high concentration of CCCP, the injection of substrate would be strongly reduced and result in low-speed growth. As shown in Figure 6c, the filament elongation rate for the highest CCCP concentration (~18 nm∙min−1) was virtually independent of the length of the filament as predicted by the model. Interestingly, some filaments were unaffected by the CCCP treatment, likely due to the action of multidrug transporters (Lomovskaya and Lewis, 1992), and displayed kinetics similar to the untreated population (Figure 6—figure supplement 1d), highlighting the major contribution of the pmf in energizing export.

![Figure 6.](https://cdn.elifesciences.org/articles/23136/elife-23136-fig6-v2.jpg)

**Figure 6.:** (a) Top: Experimental design. Carbonyl cyanide m-chlorophenyl hydrazone (CCCP) reduces the proton motive force (pmf) and was present during growth of the second fragment (60 min) and removed during growth of the third fragment, which allowed the pmf to regenerate. TB: tryptone broth without dye, AnTc: anhydrotetracyline induction of flagella genes. Bottom: Fragment lengths represented as basal/apical (F1/F2) coordinates (n = 255 for 0 µM CCCP, n = 395 for 10 µM CCCP, n = 371 for 20 µM CCCP, n = 353 for 30 µM CCCP). The fits represent the injection-diffusion model with parameters D ≈ 5.25 × 10−13 m2 ⋅ s−1, and kon ≈ 26.10, 3.19, 1.19, 0.70 s−1 for 0 µM, 10, 20, 30 µM CCCP respectively. Representative fluorescent microscopy images of labelled flagella and matching coordinates are highlighted by coloured frames and arrows. Scale bar 2 µm. (b) Filament length as a function of time for decreasing values of kon. For small values of kon, the injection rate but not flagellin transport is rate-limiting, which results in a quasi-linear growth. (c) Growth curves for the CCCP raw data of panel a determined by fitting the data to the injection-diffusion model with a fixed parameter a. The values for kon decrease by a factor of 8 (10 µM CCCP), 22 (20 µM CCCP), and 38 (30 µM CCCP), compared to the untreated control. (d) Equation and biophysical parameters of the injection-diffusion model.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/23136/elife-23136-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (a) Raw data of triple-labelled flagella after inhibition of the pmf-dependent export apparatus by treatment with increasing concentrations of CCCP were measured and sorted according to the length of F1. Each vertical line represents an individual filament (n = 255 for 0 µM CCCP, n = 395 for 10 µM CCCP, n = 371 for 20 µM CCCP, n = 353 for 30 µM CCCP). (b) Basal/apical relationship (30 min elongation) for decreasing values of kon, which result in linear-like growth rate. (c) Fragment lengths from the triple labelling data of Figure 6a presented as the average individual fragment size. Error bars represent the 95% confidence interval of mean estimation. (d) Minor population of CCCP-resistant flagella display filament elongation kinetics similar to the untreated control. Left panel: distribution of the second (F2) fragments for the untreated and 30 µM CCCP conditions. The presence of long filaments (F2 >2 µM) is characteristic for resistance to the uncoupler. Middle panel: the filaments with long F2 fragments follow a kinetic similar to the untreated population (blue curve). The fit curve for the 30 µM CCCP treatment is shown in orange for comparison. Right panel: the CCCP-sensitive population undergoes an increase in elongation speed after recovery from the CCCP treatment (F3 > F2) while the elongation speed of the CCCP-resistant population follows the normal kinetic (F3 < F2, see Figure 2c). The dotted lines mark a threshold of 2 µm for F2. The points above this threshold are shown in purple.

### Conclusion

The bacterial flagellum is a remarkably complex nanomachine. Here, we present the first real-time visualization and experimentally supported biophysical model of the dynamic self-assembly process of this large, widely conserved nanomachine. We propose that bacterial flagella grow through an injection-diffusion mechanism (Figure 6d), which provides a simple explanation why the flagellar filament does not grow infinitely in the absence of any other length-control mechanism. It appears likely that similar biophysical principles are conserved for effector protein secretion in the evolutionary related, virulence-associated injectisome with important implications for the rational design of novel anti-infectives targeted against type III secretion systems.

## Materials and methods

### Bacteria, plasmids and media

Salmonella enterica serovar Typhimurium strains and plasmids used in this study are listed in Table 1. Lysogeny broth (LB) contained 10 g of Bacto-Tryptone (Difco), 5 g of yeast extract, 5 g of NaCl and 0.2 ml of 5N NaOH per litre. Soft agar plates used for motility assays contained 10 g of Bacto-Tryptone, 5 g of NaCl, 3.5 g of Bacto-Agar (Difco) and 0.2 ml of 5N NaOH per liter. Tryptone broth (TB) contained 10 g of Bacto-Tryptone and 5 g of NaCl. Ampicillin was added to the medium at a final concentration of 100 µg/ml, L-arabinose at a final concentration of 0.2% and anhydrotetracyline at a final concentration of 100 ng/ml if required.

**Table 1.**
 Strains and plasmids used in this study.


<table>
  <thead>
    <tr>
      <th>Strain</th>
      <th>Relevant characteristics</th>
      <th>Source or reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>SJW1103</td>
      <td>Salmonella enterica serovar Typhimurium wild-type strain SJW1103 for motility and chemotaxis</td>
      <td>(Yamaguchi et al., 1984)</td>
    </tr>
    <tr>
      <td>TM113</td>
      <td>SJW1103 ∆fliC</td>
      <td>T. Miyata, unpublished</td>
    </tr>
    <tr>
      <td>NH001</td>
      <td>SJW1103 ∆flhA</td>
      <td>(Hara et al., 2011)</td>
    </tr>
    <tr>
      <td>MM1103iS</td>
      <td>SJW1103 ∆fliS::km</td>
      <td>(Furukawa et al., 2016)</td>
    </tr>
    <tr>
      <td>MM1103gK</td>
      <td>SJW1103 flgK::Tn10</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>MM1103gKiS</td>
      <td>SJW1103 ∆fliS::km flgK::Tn10</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>MM1103CPOP</td>
      <td>SJW1103 ∆PfliC::tetRA-62</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>TH437</td>
      <td>Salmonella enterica serovar Typhimurium wild-type strain LT2</td>
      <td>lab collection</td>
    </tr>
    <tr>
      <td>TH15801</td>
      <td>LT2 PflhDC5451::Tn10dTc[del-25] ∆hin-5717::FCF</td>
      <td>lab collection</td>
    </tr>
    <tr>
      <td>EM1237</td>
      <td>LT2 ∆araBAD1026::fliC ∆fliC7861::FRT ∆hin-5717::FCF PflhDC5451::Tn10dTc[del-25]</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>EM2046</td>
      <td>LT2 ∆hin-5717::FRT fliC6500 (T237C) PflhDC5451::Tn10dTc[del-25]</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>EM2400</td>
      <td>LT2 ∆hin-5717::FRT fliC6500(T237C) ∆araBAD1005::FRT PflhDC5451::Tn10dTc[del-25]</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>EM4076</td>
      <td>LT2 ∆hin-5717::FRT fliC7746::3xHA (∆aa201-213::3xHA) motA5461::MudJ PflhDC5451::Tn10dTc[del-25] ∆sseA-ssaU::FCF (deletes Spi-2)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>Plasmids</td>
      <td>Relevant characteristics</td>
      <td>Source or reference</td>
    </tr>
    <tr>
      <td>pBAD24</td>
      <td>Expression vector</td>
      <td>Invitrogen</td>
    </tr>
    <tr>
      <td>pAOA001</td>
      <td>pBAD24/FliC</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pAOA002</td>
      <td>pBAD24/FliC(∆29–32)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pAOA003</td>
      <td>pBAD24/FliC(∆11–18)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pAOA004</td>
      <td>pBAD24/FliC(∆11–18/∆29–32)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pAOA005</td>
      <td>pBAD24/FliC(∆310–495)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pAOA006</td>
      <td>pBAD24/FliC(∆29–32/∆310–495)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pAOA007</td>
      <td>pBAD24/FliC(∆450–495)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pAOA008</td>
      <td>pBAD24/FliC(∆29–32/∆450–495)</td>
      <td>This study</td>
    </tr>
  </tbody>
</table>

### DNA manipulations

DNA manipulations were carried out as described before (Hara et al., 2011). Site-directed mutagenesis was carried out using QuickChange site-directed mutagenesis method as described by Agilent Technologies, Santa Clara, CA, USA. DNA sequencing reactions were carried out using BigDye v3.1 as described in the manufacturer’s instructions (Applied Biosystems, Foster City, CA, USA), and then the reaction mixtures were analysed by a 3130 Genetic Analyzer (Applied Biosystems).

### Motility assays in soft agar

To check motility of the Salmonella SJW1103 (wild-type) and TM113 (∆fliC) cells carrying a pBAD24-based plasmid encoding wild-type or FliC deletion variants, motility assays were performed in soft agar plates. Single colonies of the cells were inoculated into soft agar plates containing ampicillin and 0.2% arabinose. Plates were then incubated at 30°C for the required period of time. Their motility was observed as a ring of migrating cells emanating from the point of inoculation.

### Flagellin transport assay

Salmonella cells were grown with shaking in 5 ml of LB at 30°C until the cell density had reached an OD600nm of approximately 1.0–1.2. To see the effect of the flagellar filament on flagellin transport during filament assembly, the cultures were heated at 65°C for 5 min to depolymerize the filaments into flagellin monomers and were centrifuged to obtain cell pellets and culture supernatants, which contains the cytoplasmic flagellin subunits and flagellins transported by the flagellar type III export apparatus, respectively. To test the effect of flagellin subunit linkage on the flagellar growth rate (compare Figure 5c), strain MM1103CPOP carrying a pBAD24-based plasmid encoding FliC(∆310–495), FliC(∆29–32/∆310–495), FliC(∆450–495) or FliC(∆29–32/∆450–495) was grown with shaking in 5 ml of LB containing ampicillin at 30°C until the cell density had reached an OD600 of approximately 0.6–0.8. To induce the expression of chromosomally encoded wild-type FliC (from a tetracycline-inducible promoter in the native fliC locus) and its deletion variant (from an arabinose-inducible promoter encoded on pBAD24), we added tetracycline and L-arabinose at the final concentrations of 15 µg/ml and 0.2%, respectively, and the incubation was continued for another hour. The cultures were directly heated at 65°C for 5 min, followed by centrifugation to obtain cell pellets and culture supernatants. Cell pellets were resuspended in the SDS-loading buffer, normalized to a cell density to give a constant amount of cells. Proteins in the culture supernatants were precipitated by 10% trichloroacetic acid, suspended in the Tris/SDS loading buffer and heated at 95°C for 3 min. After SDS-PAGE, both CBB-staining and immunoblotting with polyclonal anti-FliC antibodies were carried out as described before (Minamino and Macnab, 1999). Detection was performed with an ECL plus immunoblotting detection kit (GE Healthcare, Tampa, FL, USA). At least six independent experiments were performed.

### Flagellin leakage measurements during filament assembly

Salmonella cells were grown with gentle shaking in 5 ml of LB at 30°C until the cell density had reached an OD600 of approximately 1.0. After centrifugation, the cell pellets and the culture supernatants were collected separately. The culture supernatants were ultracentrifuged at 85,000 × g for 1 hr at 4°C and the pellets and the supernatants, which contain flagellar filaments detached from the cell bodies during shaking culture and flagellin monomers leaked out the culture media during filament formation, respectively, were collected separately. The cell pellets were suspended in 5 ml PBS and then were heated at 65°C for 5 min, followed by centrifugation to obtain the cell pellets and supernatants, which contained the cytoplasmic flagellin molecules and depolymerized flagellin monomers, respectively. The cell pellets and the pellet fractions after ultracentrifugation were resuspended in the SDS-loading buffer, normalized to the cell density to give a constant amount of cells. Proteins in the supernatants were precipitated by 10% trichloroacetic acid, suspended in Tris/SDS loading buffer and heated at 95°C for 3 min. After SDS-PAGE, both CBB-stating and immunoblotting with polyclonal anti-FliC antibodies were carried out. At least six independent experiments were performed.

### Electron microscopy observation of negatively stained Salmonella cells

Salmonella cells were exponentially grown with gentle shaking in 5 ml LB at 30°C. 5 µl of the cell culture were applied to carbon-coated copper grids and negatively stained with 0.5% (W/V) phosphotungstic acid. Micrographs were recorded at a magnification of 1200× with a JEM-1010 transmission electron microscope (JEOL, Tokyo, Japan) operating at 100 kV.

### Microscopy of flagellar filaments

For immunolabelling of flagellar filaments, polyclonal anti-FliC and anti-rabbit IgG antibodies conjugated with Alexa Fluor 488 and 594 (Invitrogen, Carlsbad, CA, USA) were used as described (Erhardt et al., 2011; Minamino et al., 2014).

For in situ labelling of flagellar filaments of the FliCT237C cysteine replacement mutant, an overnight culture was diluted 1:100 into 10 ml fresh TB in a 125 ml flask and grown at 30°C for 2 hr until OD600nm of 0.6. Production of the flagellar master regulatory operon flhDC was induced by addition of 100 ng/ml anhydrotetracycline (AnTc) for 30 min. Afterwards, the culture was centrifuged for 3 min at 2500 × g, resuspended in 10 ml fresh TB and grown at 30°C for 30 min. An aliquot was transferred to a 2 ml Eppendorf tube and grown with shaking at 30°C for 30 min in the presence of 10–25 µM Alexa or DyLight-coupled maleimide dye (ThermoFisher, Tampa, FL, USA). After the incubation, the dye was removed by centrifugation for 2 min at 2500 × g. The culture was resuspended in 1 mL fresh TB and incubated for additional 30 min in the presence of 10–25 µM Alexa or DyLight-coupled maleimide dye at 30°C. Dye removal and incubation with DyLight-coupled maleimide dye was repeated to label up to six flagellar filament fragments. After the final labelling period, the bacteria were resuspended in PBS and an aliquot was applied to a custom-made flow cell (Wozniak et al., 2010) with the modification of using Polysine microscope slides (ThermoFisher). Non-adhering cells were flushed by addition of PBS and bacteria were fixed by addition of 2% formaldehyde, 0.2% glutaraldehyde in PBS for 5 min, followed by a washing step with PBS. Fluoroshield mounting medium (Sigma-Aldrich, St. Louis, MO, USA) was added and the cells were observed by fluorescent microscopy using a Zeiss (Oberkochen, Germany) Axio Observer microscope at 100× magnification. Fluorescence images were analysed using ImageJ software version 1.48 (National Institutes of Health).

Continuous flow in situ immunostaining of 3× hemagglutinin epitope tagged FliC filaments was performed as described by Berk et al. (2012) with the following adaptions. Strain EM4076 expressing mCherry from pZS*12-mCherry (mCherry under control of Plac [Lutz and Bujard, 1997]) was grown to mid-log phase in M9-glucose minimal medium supplemented with 0.2% casamino acids and 0.1% bovine serum albumin (BSA) and induced for 30 min with 100 ng/ml AnTc. Bacteria were diluted 10-fold, and applied to a continuous flow CellASIC microfluidic plate (B04A; Merk Millipore, Billerica, MA, USA). Approximately 10 nM anti-HA Alexa Fluor488 fluorochrome-coupled primary antibodies (Thermo Fisher A-21287, final concentration 1 µg/ml) were added to the flow medium, which was identical to the above mentioned growth medium without addition of AnTc. Cells were imaged at 30°C with a temperature-controlled Olympus total internal reflection fluorescence microscope equipped with a water-cooled Hamamatsu (Hamamatsu City, Japan) ImageEM C9100-13 with a pixel size of 160 µm using a NA1.4 100× objective and an additional 1.6× tubular lens at a highly-inclined above-critical angle. To image anti-HA Alexa Fluor488 decorated flagellin and mCherry, a 488 nm diode laser set to 0.25 mW and a 561 nm solid-state laser set to 0.85 mW were used. Images were taken every 10 s with exposure times of 15 msec for 488 nm and 8 msec for 561 nm at low camera gain settings.

### Data reporting

No statistical methods were used to predetermine sample size. The experiments were not randomized and the investigators were not blinded to allocation during experiments and outcome assessment.

### Statistical analysis

Biochemistry experiments were performed at least three times and representative experiments are reported in the figures. Where indicated, mean values and standard deviations were obtained from at least three independent biological replicates. All microscopy experiments were performed at least twice and the figures present individual data points of a representative experiment. Box plots report the median (in red), the 25th and 75th quartiles and the 1.5 interquartile range. Error bars of bar graphs represent the 95% confidence interval of mean estimation.

### Fitting experimental data by the growth model

To compare the model with data, we need to find a best fit for the parameters a and b using the growth function (Equation 4). Accordingly, note that if F1 is the amount of filament growth in time ∆T following an initial growth of length F0, then

$$
\int_{F_{0}}^{F_{0}+F_{1}}(b+L)dL=aΔT,
$$

which reduces to the equation

$$
L(L+2b)|F_{0}+F_{1}F_{0}=2aΔT,
$$

or

$$
bF_{1}+\frac{1}{2}(2F_{0}F_{1}+F_{1}^{2})=aΔT.
$$

This could be solved for F0 as a function of F1 and then fitted by standard regression to find parameters a and b. However, to do so would ignore the important fact that there is measurement error in both of the measurements F0 and F1. Consequently, a different method of fitting this curve is needed.

The method used here is to seek numbers W0 and W1, which are approximations to F0 and F1 and satisfy the relationship

$$
bW_{1}+\frac{1}{2}(2W_{0}W_{1}+W_{1}^{2})=aΔT
$$

This can be done by minimizing the function

$$
E=\sumN((F_{0}−W_{0})^{2}+(F_{1}−W_{1})^{2}+\lambda(bW_{1}+\frac{1}{2}(2W_{0}W_{1}+W_{1}^{2})−aΔT)^{2}),
$$

where λ is a fixed constant. In this way, both F0 and F1 are treated as noisy data values which need to be fitted.

However, for this analysis, we found it better to introduce the change of variables $L=b\frac{U}{1−U}=g(U)$, $U=\frac{L}{L+b}$ and then to find numbers U0 and U1, $\alpha=\frac{aΔT}{b^{2}}$ and b so that

$$
E=\sumN((F_{0}−bg(U_{0}))^{2}+(F_{0}+F_{1}−bg(U_{1}))^{2}+\lambda(f(U_{1}))−f(U_{0})−\alpha)^{2})
$$

is minimized, where $f(U)=\frac{1}{b^{2}}(bL+\frac{1}{2}L^{2})≡\frac{1}{2}\frac{U(2−U)}{2(1−U)^{2}}$. The minimization of E is equivalent to finding the solution of the system of 2N + 2 nonlinear algebraic equations

$$
(13)\frac{∂}{∂\alpha}:\sumN(f(U_{1})−f(U_{0})−\alpha)=0,(14)\frac{∂}{∂b}:\sumN(F_{0}−bg(U_{0}))g(U_{0})+\sumN(F_{0}+F_{1}−bg(U_{1}))g(U_{1})=0,(15)\frac{∂}{∂U_{0}}:b(F_{0}−bg(U_{0}))g^{′}(U_{0})+\lambda(fU_{1})−f(U_{0})−\alpha(f^{′}(U_{0})=0,(16)\frac{∂}{∂U_{1}}:−b(F_{0}+F_{1}−bg(U_{1}))g^{′}(U_{1})+\lambda(f(U_{1})−f(U_{0})−\alpha)f^{′}(U_{1})=0.
$$

This system of equations is readily solved with an iterative solution method such as Newton’s Method, details of which are not described here.

Once U0 and U1 are known, so also are $W_{0}=b\frac{U_{0}}{1−U_{0}}$ and $W_{1}=b\frac{U_{1}}{1−U_{1}}−W_{0}$. From this we can estimate the time at which the F0 phase of growth ended to be

$$
t_{0}=\frac{1}{a}(bW_{0}+\frac{W_{0}^{2}}{2}),
$$

and the time at which the F1 growth phase ended is $t_{1}=t_{0}+ΔT$. This information enables us to plot the growth curve and plot the F0 and F1 measurements at the appropriate times.

### Simulation of filament growth in presence of competing substrates

Substrates arriving at the export gate were randomly chosen with a probability p = r / (1+r) to be a competing substrate (i.e., non-chaining or not incorporated in the filament), where r is the ratio of competing molecules relative to flagellin. The following rules were used:

In Figure 5 panel g and Figure 5—figure supplement 1 panel d, we simulated filament growth over 250 min for 20,000 filaments and assumed a mechanism based on the chain model (strict in blue, with recovery in yellow) or the injection-diffusion model (in red), in the presence of a random proportion of competing substrates (r) between 10−9 and 1,000. The simulation of chain model-dependent filament growth is illustrated in Figure 5—figure supplement 2.

The range of competing substrates compatible with a chain-driven elongation is very low (<10−4–10−5), while the injection-diffusion model allows for robust filament growth over a much broader range of competing substrate (up to about a 10-fold excess of competing substrates).

Complementary to the simulation, the median length of the filament under chain model-dependent growth and in presence of competing substrates can be calculated as follows:

The probability of sequentially forming a chain of exact length n is $P_{n}=p^{n}(1−p)$.

The expected number of molecules in the chain is:

$$
E(p)=(1−p)\sumnnp^{n}=\frac{p}{1−p}=\frac{1}{x}
$$

Thus, the median length of a filament grown from a continuous chain is kβ, where β = 0.47 nm and k can be determined by:

$$
\frac{1}{2}=\sumnkP_{n}=\sumnk(1−p)p^{n}=1−p^{k+1},
$$

which leads to:

$$
k=\frac{ln2}{ln(1+x)}−1.
$$
