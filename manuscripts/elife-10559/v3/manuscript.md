# How competition governs whether moderate or aggressive treatment minimizes antibiotic resistance

## Authors

- Caroline Colijn<sup>1</sup> ([ORCID: 0000-0001-6097-6708](https://orcid.org/0000-0001-6097-6708)) †
- Ted Cohen<sup>2</sup>

### Affiliations

1. Department of Mathematics Imperial College London London United Kingdom
2. School of Public Health Yale University New Haven United States

† Corresponding author

## Abstract

Understanding how our use of antimicrobial drugs shapes future levels of drug resistance is crucial. Recently, there has been debate over whether an aggressive (i.e., high dose) or more moderate (i.e., lower dose) treatment of individuals will most limit the emergence and spread of resistant bacteria. In this study, we demonstrate how one can understand and resolve these apparently contradictory conclusions. We show that a key determinant of which treatment strategy will perform best at the individual level is the extent of effective competition between resistant and sensitive pathogens within a host. We extend our analysis to the community level, exploring the spectrum between strict inter-strain competition and strain independence. From this perspective as well, we find that the magnitude of effective competition between resistant and sensitive strains determines whether an aggressive approach or moderate approach minimizes the burden of resistance in the population.

## Introduction

The growing crisis of resistance to antimicrobial drugs has captured the attention of the global public health community as the harrowing reality of the loss of previously effective medicines combined with slow discovery of new agents threatens a post-antibiotic era of untreatable infectious diseases. Although the quality and completeness of surveillance is variable, current data are consistent with rising levels of resistance; this worrisome trend is not restricted to particular pathogens or specific geographic settings (WHO, 2014). While an accurate assessment of the current health and economic losses attributable to antibiotic resistance is elusive, the estimated numbers, ranging up to 2 million serious infections, 23,000 deaths, and 35 billion dollars in the United States alone, are staggering (CDC, 2013). Similar numbers of deaths have been attributed to antibiotic-resistant infections in Europe (O'Neill, 2014). Most recently, a projection of 10 million deaths and 100 trillion dollars in economic losses attributable to antimicrobial-resistant infections by 2050 has been circulated (O'Neill, 2014).

Given that antimicrobial treatment cures infections while simultaneously selecting for antimicrobial resistance, it is crucial to understand how alternative treatment strategies affect the probability of resistance. The conventional wisdom guiding the rapidity and dosing of drugs, often attributed to Paul Ehrlich, (Ehrlich, 1913) is that early and aggressive use of antimicrobial agents is most effective for optimizing cure and minimizing the risk of resistance (Levin et al., 1999). Recently, there has been some debate as to the universality of the claim that these aggressive approaches are optimal for minimizing the risk of resistance, with some researchers suggesting that more moderate approaches may perform better (Read et al., 2011) and others defending the standard approach (Ankomah and Levin, 2014).

A central rationale for an aggressive approach is that early high dose treatment will most rapidly reduce the size of the microbial population from which drug-resistant isolates appear and thus minimize the probability of the emergence of resistance during treatment (Bonhoeffer et al., 1997; Knudsen et al., 2003; Wiuff et al., 2003; Tam et al., 2005, 2007; D'Agata et al., 2007; Ankomah and Levin, 2014; Kim et al., 2014). In contrast, the rationale for a more moderate approach is that higher doses of antibiotics impose stronger selective pressure which drives a more rapid emergence of resistance (Read and Huijben, 2009; Read et al., 2011; Kouyos et al., 2014), and that rapid suppression of drug-susceptible isolates may allow for competitive release of existing drug-resistant isolates (de Roode et al., 2004; Wargo et al., 2007; Huijben et al., 2010; Pena-Miller et al., 2013; Pollitt et al., 2014). Recently, Kouyos et al. (2014) summarized the relevant, albeit limited, empirical evidence about dosing and risk of resistance, and described a ‘conceptual curve’ relating the strength of selection to the expected rate of resistance emergence, highlighting theoretical conditions under which aggressive and moderate approaches may be preferred.

How one formulates the question about optimal antimicrobial dosing strategies to minimize resistance will depend on one's perspective. For example, a clinician will likely be most concerned with identifying the dosing regimen that produces the best health outcome for the patient (i.e., highest probability of cure accounting for toxicities and the risk of resistance). A public health practitioner will likely seek to identify which treatment practices produce the greatest health gains while minimizing the long-term levels of resistance in the community. The recent debate over aggressive and moderate approaches has mainly been centered on identifying an optimal strategy for the treatment of individual hosts to minimize the probability of resistance. However, the emergence and subsequent transmission of resistance in the population may be of even greater concern. From a theoretical perspective, optimal dosing strategies for the prevention of resistance in individuals are not necessarily optimal for limiting resistance at the population level (Lipsitch and Samore, 2002; Mills et al., 2013).

Here, we provide a modeling framework that unifies the individual-level and population-level perspectives and provides additional insight into the debate about aggressive and moderate approaches for antimicrobial treatment. We demonstrate that the extent of effective competition between drug-susceptible and drug-resistant isolates is a key determinant of whether an aggressive approach is better (in terms of resistance prevention) than a moderate approach for hosts being treated for disease. Most importantly, we find that even within a model that allows for very strong competition, different realistic combinations of parameter values can support the aggressive or moderate approach as optimal. We illustrate how it is possible that models can support two such different conclusions by carefully considering the dominant interactions between the strains. We extend our analysis to the population level, exploring a spectrum of inter-strain interactions ranging from strict competition to independence. We find that the same framework explains why either aggressive or moderate treatment approaches can minimize resistance.

## Materials and methods

### Within-host model

We describe two populations of bacteria within a single host using a model based on Ankomah and Levin (2014). The model includes both wild-type (drug-sensitive; DS) bacteria and drug-resistant (DR) bacteria which arise by some presumably rare mechanism from the drug-sensitive type. This mechanism could be single-point mutation, acquisition of resistance genes through horizontal gene transfer, or another mechanism (Lipsitch and Samore, 2002; zur Wiesch et al., 2011). While we do not explictly model these differences, we note that the mechanisms of resistance and their probabilities affect the relative importance of de novo resistance compared to pre-existing resistance circulating in a population (Lipsitch and Samore, 2002). In our model, each strain initiates an immune response which follows density-dependent kinetics. Bacteria grow in a resource-dependent manner and have a death rate which increases under higher antibiotic concentrations. Antibiotics enter the system and degrade at a constant rate. The DR strain, by definition, has a higher minimum inhibitory concentration (MIC) than the DS strain and is assumed to have a slower growth rate reflecting fitness costs associated with mutation or acquisition of resistance genes. The phrase ‘minimum inhibitory concentration’ parallels the language in Ankomah and Levin (2014); the MIC is the value of antibiotic A at which the growth rate with the drug is half its baseline value (when A = 0). The strain interactions in the model are complex: strains compete for resources, and each strain can suppress the other by triggering a host immune response. Thus, we expect the strains to be under fairly strong competition. However, the DS strain also benefits the DR strain as DR is generated from the DS population through acquired resistance.

The equations are:

$$
\frac{dB_{s}}{dt}=G_{s}B_{s}−k_{p}PB_{s}−k_{i}IB_{s}−\muB_{s}\frac{dB_{r}}{dt}=G_{r}B_{r}−k_{p}PB_{r}−k_{i}IB_{r}+\muB_{s}\frac{dI}{dt}=\alphaI\frac{B_{s}+B_{r}}{B_{s}+B_{r}+\sigma_{i}}−u_{i}I\frac{dP}{dt}=η(P_{max}−P)\frac{B_{s}+B_{r}}{B_{s}+B_{r}+\sigma_{p}}−\gammaP\frac{dR}{dt}=w(C_{R}−R)−e(G_{s}B_{s}+G_{r}B_{r})\frac{dA}{dt}=A_{in}−(d+w)A.
$$

The variables are the densities of DS and DR bacteria (Bs, Br in cells/ml) and the adaptive and innate immune cells (I, P in cells/ml), and the concentration of the resource R (μmg/ml) and the antibiotic A (μmg/ml). Bacterial growth is resource dependent (Ankomah and Levin, 2014) with growth rate $\lambda_{s}=Λ_{s}\frac{R}{k+R}$ and similarly for λr, where Λs and Λr are the maximum growth rates of the two strains when the resource is not limiting. The net growth rate Gs is Gs = λs − (us + δs(A)) and Gr = λr − (ur + δr(A)), capturing death and the bactericidal effect of the antibiotic. We adopt the assumption that recruitment of activated effector cells of the innate system (P) is dependent on the density of the pathogen population (Bs + Br) and σp > 0 is a saturation constant. Similarly, we assume that the expansion of specific adaptive immune response I is dependent upon the density of the pathogen population, the maximal expansion rate α and σi, the pathogen density at which the increase in the adaptive immune response is half maximal. The resource is replenished at rate wCR and depleted at rate wR. In our baseline results we assume, as in previous work (Ankomah and Levin, 2014), that it is the net growth Gs and Gr that determine the extent of the depletion of resources. This means that if the net growth is negative, lysis of cells can replenish the resource. We assess the sensitivity of our findings to this assumption in Appendix 1 and find that the model's inter-strain dynamics and their dependence on the parameters are unaltered when the lysis effect is removed (in which case the resource equation in (1) reads dR/dt = w(CR − R) − e(ΛsBs + ΛrBr)). To incorporate the possibility of stochastic die-off of the DR population when its density is very low, the growth rate is 0 when the density is less than 30 cells/ml. Not allowing for stochastic die-off might allow resistant strains to enjoy an unrealistic advantage in the model due to its deterministic nature. Here, 30 cells/ml is approximately 10−8 times the maximum bacterial load, though this varies with the parameter choice. Antibiotic concentration A speeds the death of bacteria according to a saturating mechanism $\delta_{s}(A)=\lambda_{s}\frac{A/M_{s}}{A/M_{s}+1}$, and similarly for R, where Ms and Mr are the minimum inhibiting concentrations of antibiotic for the DS and DR strains, respectively. A is introduced through dosage Ain and is removed at rate d + w (Ankomah and Levin, 2014).

To explore these complex interactions, we drew 60,000 sets of parameters from ranges containing the values used previously (Ankomah and Levin, 2014) (see Table 1), spanning a range of strengths of the immune system (ki, kp, η, α), relative overall fitness of the DR strain (Λr, Mr), pre-existing DR bacilli, the growth rate of the DS strain (Λs), and the mutation parameter μ. Each parameter was chosen uniformly at random from the ranges given in Table 1. All were held fixed, and the model was simulated under multiple dosages. This gave us an understanding of how treatment affected resistance at each set of parameters. We captured the relationship between increasing Ain and the maximum and total (integrated over time in the simulations) DR at each randomly drawn set of parameters.

**Table 1.**
 Parameters and ranges


<table>
  <thead>
    <tr>
      <th>Symbol</th>
      <th>Description</th>
      <th>Range</th>
      <th>Unit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="4">Within-host model</td>
    </tr>
    <tr>
      <td>Λs</td>
      <td>Max growth rate (DS)</td>
      <td>0.4–0.8</td>
      <td>hr−1</td>
    </tr>
    <tr>
      <td>Λr</td>
      <td>Max growth rate (DR)</td>
      <td>(0.6–1) × Λs</td>
      <td>hr−1</td>
    </tr>
    <tr>
      <td>k</td>
      <td>Hill coeffient in bacterial growth</td>
      <td>0.5–50.5</td>
      <td>μg/ml</td>
    </tr>
    <tr>
      <td>us, ur</td>
      <td>Death rates DS, DR</td>
      <td>0.2</td>
      <td>hr−1</td>
    </tr>
    <tr>
      <td>mS</td>
      <td>MIC (DS)</td>
      <td>1</td>
      <td>μg/ml</td>
    </tr>
    <tr>
      <td>mR</td>
      <td>MIC (DR)</td>
      <td>1–8</td>
      <td>μg/ml</td>
    </tr>
    <tr>
      <td>kp</td>
      <td>Rate of innate immune clearance</td>
      <td>10−7 − 10−5</td>
      <td>hr−1</td>
    </tr>
    <tr>
      <td>ki</td>
      <td>Rate of adaptive immune clearance</td>
      <td>10−5 − 10−3</td>
      <td>hr−1</td>
    </tr>
    <tr>
      <td>μ</td>
      <td>Rate of DR mutation</td>
      <td>5 × 10−9 − 5 × 10−7</td>
      <td>#/division</td>
    </tr>
    <tr>
      <td>α</td>
      <td>Recruitment of adaptive immunity</td>
      <td>0.002–0.02</td>
      <td>hr−1</td>
    </tr>
    <tr>
      <td>σi, σp</td>
      <td>Hill parameter in I, P dynamics</td>
      <td>1000, 10,000</td>
      <td>cells/ml</td>
    </tr>
    <tr>
      <td>ui</td>
      <td>Loss rate of I</td>
      <td>5 × 10−5 − 5 × 10−4</td>
      <td>hr−1</td>
    </tr>
    <tr>
      <td>γ</td>
      <td>Loss rate of P</td>
      <td>5 × 10−4 − 5 × 10−3</td>
      <td>hr−1</td>
    </tr>
    <tr>
      <td>η</td>
      <td>Recruitment of innate immunity</td>
      <td>10−5 − 9 × 10−4</td>
      <td>hr−1</td>
    </tr>
    <tr>
      <td>w</td>
      <td>Washout rate</td>
      <td>0.2</td>
      <td>hr−1</td>
    </tr>
    <tr>
      <td>CR</td>
      <td>Resource reservoir concentration</td>
      <td>300–700</td>
      <td>μg/ml</td>
    </tr>
    <tr>
      <td>e</td>
      <td>Use of resource per unit growth</td>
      <td>5 × 10−7</td>
      <td>μg/cell</td>
    </tr>
    <tr>
      <td>Ain</td>
      <td>Antibiotic treatment</td>
      <td>0–2.5</td>
      <td>μg/(ml × 24 hr)</td>
    </tr>
    <tr>
      <td>d</td>
      <td>Loss rate of antibiotic</td>
      <td>0.1</td>
      <td>hr−1</td>
    </tr>
    <tr>
      <td colspan="4">Between-host model</td>
    </tr>
    <tr>
      <td>βx</td>
      <td>Transmission parameter (DS)</td>
      <td>1–4</td>
      <td>months−1</td>
    </tr>
    <tr>
      <td>βy</td>
      <td>Transmission parameter (DR)</td>
      <td>1 − βx</td>
      <td>months−1</td>
    </tr>
    <tr>
      <td>κ</td>
      <td>Partial immunity coefficient</td>
      <td>1</td>
      <td>none</td>
    </tr>
    <tr>
      <td>κt</td>
      <td>Treatment protection from DS</td>
      <td>1 − 0.3T</td>
      <td>none</td>
    </tr>
    <tr>
      <td>c</td>
      <td>Similarity coefficient</td>
      <td>0–1</td>
      <td>none</td>
    </tr>
    <tr>
      <td>u</td>
      <td>DS clearance without treatment</td>
      <td>13βx − 23βx</td>
      <td>months−1</td>
    </tr>
    <tr>
      <td>uy</td>
      <td>DR clearance</td>
      <td>βy/R01 − βy</td>
      <td>months−1</td>
    </tr>
    <tr>
      <td>T</td>
      <td>Intensity of treatment</td>
      <td>0–1</td>
      <td>none</td>
    </tr>
    <tr>
      <td>r</td>
      <td>Release of DS through treatment</td>
      <td>0–0.1</td>
      <td>months−1</td>
    </tr>
    <tr>
      <td>umax</td>
      <td>Max clearance DS under treatment</td>
      <td>1.05 βx</td>
      <td>months−1</td>
    </tr>
  </tbody>
</table>

_Ranges are indicated with a − separating lower and upper values. Where a single value is given the parameter was fixed. Within-host parameter ranges contain the values used in Ankomah and Levin (2014). The relative growth of the resistant and sensitive strains (without treatment) can be modified either through k or Λ. We have chosen to vary the Λ parameters as the effect on relative fitness is linear. In the between-host model the value of u was chosen such that the DS strain has a basic reproductive number in Bonhoeffer et al. (1997) and Ankomah and Levin (2014). Similarly, uy was chosen so that R02 ranges from 1 to R01, to ensure that the DR strain has a smaller maximum growth rate than the DS strain._

We determined whether ‘aggressive’ or ‘moderate’ therapy was the best approach according to which one minimized the overall (maximum and total) levels of resistance. If treatment is negatively correlated with resistance, then more treatment results in less resistance and an aggressive approach is best. Conversely, if the correlation is positive, then treatment drives increases in resistance, and a moderate approach is best (from a resistance standpoint). Accordingly, parameter sets in which resistance levels were negatively (S < −0.7) or positively (S > 0.7) correlated with antibiotic dosage as determined by the Spearman correlation S were classed as ‘aggressive is best’ or ‘moderate is best’; other results were classed as neutral. We removed parameter sets in which treatment does not succeed to avoid unfair inclusion of those parameter sets in which the long-term selective pressure of unsuccessful treatment drives resistance. In the main analyses, we assume that the threshold for successful treatment is defined as causing a >80% reduction in the maximum DS population; in sensitivity analyses, we vary this threshold and provide results from the full set of simulations in which such a threshold is not imposed (see Appendix 1).

### Between-host model

To explore a wide range of inter-strain interactions at the population level, we developed a model with four host compartments: susceptible, infected with DS (X), infected with DR (Y) and dually infected (D). We envision a continuum of inter-strain interactions that in principle describe co-circulating pathogens. At one of the continuum, we posit that distinct pathogens may be entirely independent of each other, not interacting directly or indirectly (e.g., through immune modulation or resource competition). In this case, infection with one strain does not affect infection or recovery with the other strain. At the other end of the continuum, very similar strains of the same pathogen are likely to be competing for hosts. Figure 1 illustrates two models, one with strict competition and one with independence.

![Figure 1.](https://cdn.elifesciences.org/articles/10559/elife-10559-fig1-v3.jpg)

**Figure 1.:** In the competing model (top row), decreasing the DS strain (X) paves the way for an increase in resistance (Y) by removing the DR strain's competitor, despite the fact that decreasing DS also removes a source of resistance. The bifurcation analysis illustrates competitive exclusion: whichever strain has the higher R0 excludes the other. In both cases, some resistance is present when the sensitive strain is present, due to acquisition of resistance, for example, through mutation. Consequently, the ‘1-only’ region of the plot has some strain 2 at very low prevalence. In contrast, if the strains are not competing (bottom row), including not competing for hosts, hosts must be able to harbor both infections (duals, D). In this case, reducing DS reduces DR by reducing a source of resistance. The bifurcation plot where strains are independent illustrates that strain 1 is present if R01 > 1, strain 2 is present if R02 > 1 and both are present if they are both >1. Our between-host model incorporates competition and independence, parameterized by a ‘similarity coefficient’ that smoothly moves from one to the other (see Appendix 1 for details).

We have previously described ‘neutral null’ models (Lipsitch et al., 2009), in which biologically indistinguishable strains have sensible dynamics in models (i.e., outcomes do not depend on which strain a host has). Our model spans this continuum, which is parameterized by a ‘similarity coefficient’ c. When c = 1 the strains are highly similar and neutral in the sense of Lipsitch et al. (2009) if they are identical. When c = 0, the two strains act independently; infection with one does not affect the spread of the other. See Appendix 1 for more details and a proof of these statements.

The model equations are:

$$
\frac{dX}{dt}=F_{x}S−κF_{y}X+\frac{1}{2}κ_{t}cF_{x}D−u_{x}X+(1−c)u_{y}D−(\mu+Tr)X\frac{dY}{dt}=F_{y}S−κ_{t}κF_{x}Y+\frac{1}{2}κ_{t}cF_{y}D−u_{y}Y+(1−c)u_{x}D+\frac{1}{2}TrD+(\mu+Tr)X\frac{dD}{dt}=κF_{y}X+κ_{t}κF_{x}Y−\frac{1}{2}κ_{t}c(F_{x}+F_{y})D−(1−c)(u_{x}+u_{y})D−\frac{1}{2}TrD−\frac{1}{2}c(u_{x}+u_{y})Du_{x}=u+(u_{max}−u)T, F_{x}=\beta_{x}X+(1−\frac{1}{2}c)D, F_{y}=\beta_{y}Y+(1−\frac{1}{2}c)D.
$$

In this model, hosts may become infected with both strains and enter the dually infected class (D); the chance of this may be reduced by cross-immunity, which we assume is symmetric between resistant and sensitive strains (κ). In models where dual infection cannot occur, there is an implicit assumption of very strong competition between strains. Dually infected individuals may also be again re-infected with a single strain (Lipsitch et al., 2009). Clearance terms (with recovery ux and uy) are modulated with the similarity coefficient, c, to ensure that the model has independent interactions when c = 0 and neutral null dynamics when c = 1 (see Appendix 1). Transmission rates are βx and βy, recovery rates are ux and uy, and we assume that over the time frame of the simulation the population does not change; we scale it to 1 so that S = 1 − X − Y − D. The forces of infection Fx and Fy contain a contribution from both singly and dually infected hosts such that when the strains are different, dually infected hosts contribute as much as singly infected ones, and when they are very similar, each strain contributes half what a singly infected host would (Lipsitch et al., 2009). Treatment T ranges from 0 to 1 (where the DS strain is eliminated) and has several effects. Primarily, it cures the sensitive strain by reducing its duration of infection 1/ux. Individuals with a resistant strain (Y) who are given treatment are partially protected (κt) from re-infection with the sensitive strain. Dually infected individuals given treatment have the drug-sensitive portion of their infection cured at an increased rate ux due to treatment, but their resistant infection is not cured.

To capture the risk of releasing small sub-populations of resistant bacilli within such hosts, we include a parameter r which is a small rate at which resistance is uncovered by treatment. This parameter links the in-host and between-host models: in circumstances in which strong treatment drives increases in resistance, r would be high (approaching the treatment rate ux of the sensitive strain).

We use a range of parameters such that the basic reproductive numbers (β/u) of the strains, R01 (DS) and R02 (DR), are greater than 1, with R02 < R01 (Table 1). We draw parameters randomly and increase the treatment T. We explore the relationship between the strength of treatment and the long-term and maximum level of resistance. We classify the resulting optimal strategy as aggressive if the Spearman correlation is less than −0.7 and moderate if it is larger than 0.7.

The between-host model admits three possible steady states (equilibria): a disease-free equilibrium (X = Y = D = 0 stable when R01 and R02 are both less than 1), a resistance-only steady state (X = D = 0, Y = 1 − uy/βy), and a steady state with X, Y, and D positive whose explicit form is not available. If there were no acquisition of resistance (μ = 0) and no ‘competitive release’ term (transition from X to Y), there would be an additional equilibrium with Y = D = 0 and X = 1 − ux/βx. We carried out an invasion analysis to determine the point at which the resistance-only equilibrium loses local stability as βx increases. When the two strains are independent, X should be prevalent if and only if R01 ≥ 1. But if they are not, the values of the strain Y parameters (and its prevalence) affect the prevalence of X. We performed the invasion analysis as follows: we computed the Jacobian of model (2) and evaluated it at the resistance-only steady state for a given set of parameters including βy. We used matlab's nonlinear solver, fsolve, to determine the value of βx at which the resistance-only steady state loses stability. We repeated this for a range of values of βy to produce the colored lines in Figure 5C.

### Determining the role of parameters in defining whether treatment increases or decreases resistance

We took several approaches to understand how the parameters of each model relate to whether aggressive or moderate treatment minimizes resistance. The most direct approach is simply to choose a set of parameters, vary the dosage, and examine how resistance changes (Figure 2). Naturally, the result depends strongly on the parameter choice. We also vary one parameter at a time, keeping others fixed, and examine the trajectories (Appendix figures 2, 3). The next approach is to examine, over all simulations simultaneously, how the outcome depends on each parameter by stratifying the outcomes (Figure 3). Using heatmaps or scatter plots, it is also possible to explore how pairs of parameters determine an outcome (Figure 4). We take the same approach in the between-host model, with Figure 5 showing demonstrative trajectories under varying treatment strength, Appendix figure 4 showing a sensitivity analysis varying one parameter at a time, and Figures 6, 7 showing the stratified dependence of the outcome on single and paired parameters while other parameters are allowed to vary.

![Figure 2.](https://cdn.elifesciences.org/articles/10559/elife-10559-fig2-v3.jpg)

**Figure 2.:** Parameters are (A) Λs = 0.5, Λr = 0.45, mR = 2.8 and (B) Λs = 0.6, Λr = 0.53, mR = 3.4. Other parameters are k = 48, kp = 2.2e−6, ki = 7.2e−4, μ = 4e−7, α = 0.018, σi = 1000, σp = 10000, γp = 0.001, and the remainder are as in Table 1.

![Figure 3.](https://cdn.elifesciences.org/articles/10559/elife-10559-fig3-v3.jpg)

**Figure 3.:** An aggressive policy (dark blue) is deemed best if the Spearman correlation S between treatment and resistance is S < −0.7, moderate (light blue) is deemed best if S > 0.7 and the classification is neutral (medium blue) otherwise. When the DR strain has a lower growth rate (LamR), an aggressive policy is more likely best because more of the DR strain's population arises through resistance acquisition from the DS population. In this case, reducing the DS strain also reduces DR. Conversely, when ΛR (LamR) is high the DR strain is a more robust competitor and a moderate policy is more frequently best. Similarly, when the DR strain has a low MIC (mR), it is a less robust competitor. In this case, an aggressive policy is more frequently best than when mR is high (second panel). The third panel shows that when the immune system is strong (high kp), an aggressive policy is more frequently best, because again more of the DR population increases are driven by acquisition from DS, due to immune suppression of DR growth. A plot with η on the horizontal axis is very similar to this one. Finally, the right plot shows that when the DS growth rate (LamS) is low, an aggressive strategy is more often best to minimize resistance; this depends on the ability of therapy to prevent the emergence of resistance.

![Figure 4.](https://cdn.elifesciences.org/articles/10559/elife-10559-fig4-v3.jpg)

**Figure 4.:** Color indicates the policy that minimizes resistance. Yellow: aggressive; green: neutral; blue: moderate. When the growth rate ΛR (LamR) is high, a moderate policy is more frequently best, but a strong immune system (high kp) can compensate by reducing DR growth. When the DR strain is a strong competitor, a moderate policy is frequently best; this can be achieved by either a high ΛR or a high DR MIC (mR) (top left). Either a high kp or a high η can compensate (bottom right), reducing the growth potential of the DR strain and leading to either a neutral outcome or an aggressive policy being best.

![Figure 5.](https://cdn.elifesciences.org/articles/10559/elife-10559-fig5-v3.jpg)

**Figure 5.:** Treatment is introduced at 5 years. (Left) Parameters are βx = 1.5, βy = 1.04, c = 0.05, r = 0, μ = 0.001. (Middle) Parameters are βx = 2, βy = 1.1, c = 0.3, r = 0.05, μ = 0.0001. (Right) Invasion analysis (bifurcation) plot. The plot shows regions of stability of the disease-free equilibrium (both R0 values less than one), the DR-only equilibrium (top left region), and the equilibrium with both (primarily DS, with low-level DR due to acquisition). The diagonal lines show the boundary at which the DR-only equilibrium loses stability. Lines move to the right as the similarity coefficient increases from 0 (light blue vertical line) to 1 (pink). When it reaches 1, the line is R01 = R02.

![Figure 6.](https://cdn.elifesciences.org/articles/10559/elife-10559-fig6-v3.jpg)

**Figure 6.:** Light blue corresponds to Spearman correlation greater than 0.7, dark corresponds to less than −0.7 and mid-range blue corresponds to all values in between. An aggressive policy is best when the DR strain is relatively unfit (low R0 value; left panel). When the acquisition rate is high, treatment-driven reductions in DS decrease the DR prevalence (second panel). When the two strains are more independent (low similarity coefficient), competition is reduced, so that reductions in the DS strain do not much benefit the DR strain, leading to the aggressive policy being preferred (third panel). When R01 is high, a moderate outcome results, because inter-strain competition is more effective. Vertical axes (‘count’) are the fraction of simulations in each category.

![Figure 7.](https://cdn.elifesciences.org/articles/10559/elife-10559-fig7-v3.jpg)

**Figure 7.:** A moderate-is-best (blue) outcome occurs when R01 and the similarity coefficient are high, because the strains are competing (left panel). When the DR strain is relatively unfit (low R02), an aggressive policy is likely best (second and third panels); we restricted R02 to be lower for the DR strain than the DS one. A high rate of acquisition can counter-balance a low R02 (second panel). When the strains are more independent (low similarity coefficient), an aggressive policy is more often best even over a much wider range of R02 (third panel).

However, we cannot expect any one or two parameters to entirely determine which approach minimizes resistance. We used discriminant analysis of principal components (DAPC, in the adegenet package in R [Jombart and Ahmed, 2011]) to systematically identify which parameters contribute to each outcome (Jombart et al., 2010). DAPC is related to principal component analysis (PCA) but instead of finding combinations of parameters to account for the variability in data (as PCA does), DAPC finds combinations of parameters that best account for variability between groups. Here, we used whether aggressive or moderate treatment minimizes resistance to define the groups (aggressive, neutral or moderate as above) and used DAPC to find combinations of parameters that separate these groups from each other.

## Results

The best policy for reducing the amount of resistance in both models can be either aggressive or moderate despite the fact that both models capture potentially strong competition and the acquisition of de novo resistance. The choice of best approach depends on the combined effect of the complex set of inter-strain interactions, and typically, one of these approaches is the clear winner (see Appendix figure 5).

### Within-host model

Figure 2 illustrates how treatment dosage may affect the level of resistance in the in-host model. Whether treatment increases or decreases resistance over the course of infection depends on many of the parameters in the model. We performed a sensitivity analysis to determine how the relationship between resistance and dosage changes with each parameter when the others are held fixed (Appendix figures 2, 3). We found that the relationship is relatively robust to variation in each parameter alone, but that small changes in several parameters can have a radical effect. In Appendix figure 2, increasing the dosage does not increase resistance and this result is fairly robust to variation in each parameter alone; Appendix figure 3 shows the contrasting robust scenario (increased dosage increases resistance). The difference is that the baseline parameters in Appendix figure 3 have somewhat higher growth Λs and Λr of both strains and the resistant strain has a higher MIC.

No single parameter determines whether aggressive or moderate treatment minimizes resistance. A relatively small change in several parameters can shift the model from one mode to the other. We separated parameter combinations in which aggressive vs moderate treatment minimizes resistance using a principled approach (DAPC; Appendix figure 6). We found that a linear combination of parameters (one ‘principle component’) captures almost all of the difference between the three groups (aggressive minimizes DR, moderate minimizes DR, or neutral, i.e., in between). The ‘loadings’ (e.g., coefficients) of the parameters in this linear combination correspond to the relative importance of the parameters in determining whether aggressive or moderate treatment minimizes resistance. The number of pre-existing resistant cells affects the outcome (coefficient 0.79). When pre-existing numbers are low (<10), parameters which lead to a ‘moderate’ policy to be best include higher growth rate of the DR and DS strains (ΛR, 1.4 and ΛS, 0.92), lower immune parameters kp and η (−0.74; −0.66) and a higher MIC of the DR strain (mR; 0.34). Other parameters had loadings less than 0.1 and did not contribute much to the classification.

In other words, we find that an aggressive approach is preferred when the immune system is relatively strong (higher values of immune parameters kp, η), and when the DR strain has a relatively low growth rate (ΛR) and low MIC (mr). Conversely, if there is pre-existing resistance, the immune system is weaker, and/or the growth rate or MIC higher, a moderate approach minimizes resistance. Pre-existing populations of DR pathogens (i.e., resistance that appears prior to exposure to treatment) favor a moderate approach, since there is no possibility that a hard-and-fast approach will clear the infection before resistance can arise.

Figure 3 illustrates how the best policy relates to individual model parameters, and Appendix figures 7, 8 show the distributions of individual parameters where treatment increases or decreases resistance. No single parameter determines which policy is best; rather, the outcome depends on the combined effects of a set of complex interactions. This means that from a location in parameter space where aggressive therapy minimizes resistance, a relatively small change in several parameters (e.g., a slight decrease in kp, increase in mR and increase in Λr) can result in a moderate policy being best.

Figure 4 shows the best policies for key pairs of parameters whose values combine to influence whether an aggressive or moderate policy minimizes resistance. These figures reveal a few intuitive trade-offs: a higher DR growth rate (ΛR) generally leads to a moderate policy being best (light blue; positive correlation between treatment and DR), but this can be offset with a strong immune system keeping both strains in check (high η or high kp). A higher DR growth rate or a higher MIC (mR) make the DR strain a robust competitor and also consequently favors a moderate policy. Interestingly, while the mutation rate affects the overall numbers of DR bacteria (particularly in cases when they are not present initially), it does not have a strong effect on the relationship between treatment and total resistance.

If resistant cells are present initially, then they do not need to emerge by (rare) mutation or acquisition mechanisms from the sensitive strain. This simple observation has consequences for our analysis; a ‘moderate is best’, or neutral conclusion is much more likely with pre-existing resistance, keeping everything else the same. When there is no pre-existing resistance, the DR strain must have a higher MIC, higher growth rate and face a weaker immune system in order to be a robust competitor than it does when it is present initially. Appendix figure 1 shows the heatmaps as in Figure 4 but stratified according to whether there is pre-existing resistance.

To understand which policy minimizes resistance, one must be able to characterize the net effect that the presence of one strain has on the other strain. There is strong opportunity for competition between strains encoded in the model; competition plays out through shared resources which may be limiting as well as through the triggering of an immune response that suppresses both strains equally. Both of these effects occur when bacterial populations are large. However, the initial appearance of resistance also depends critically on the presence of drug-sensitive organisms. Altering both the strength of competition and the dependence of the DR strain on the DS progenitor population determines whether or not such competition is effective. In particular, effective competition naturally requires a DR strain that has the capacity to be a robust competitor to the DS progenitor. This can be achieved in two ways: it can maintain a strong growth capacity in the presence of antibiotic treatment or immune pressure, or it can face an immune system that is not particularly strong. Our exploration of the parameter space uncovered both of these mechanisms. These findings are not an artifact of the model structure, and indeed they will likely occur in any model that includes de novo appearance of resistant strains by mutation or acquisition of resistance determinants by drug-sensitive organisms, and where resistant strains can then compete for resources with their drug-sensitive cousins.

Effective competition can be described as the net extent to which a decrease in one strain benefits the other. This should capture both direct and indirect effects. Quantifying effective competition is challenging because either strain may affect the other over short or long time frames and because different ways to decrease one strain have different effects. From the second equation of (1), the direct effect of a decrease in Bs on the immediate growth of the resistant strain is simply the change in the acquisition term (μBs). If the other terms are small, this term can make the difference between net growth and net decline of resistant cells. The indirect effects are more difficult to determine; a decrease in Bs will mean more available resource and reduced recruitment of immune cells which will have onward effects. We made a step towards quantifying effective competition as follows. We numerically solved the system, obtaining values of each variable through time. We decreased Bs and computed the predicted value of Br two time steps later, using Euler's method, the derivatives in (1) and the time steps defined by the adaptive ODE solver. We did this (separately) at each time point and averaged the fractional change in Br due to a 5% change in Bs over the portion of the trajectory where Bs > 105. We do this only in the untreated case, for each value of the parameters we sampled. This captures only the immediate indirect effects (occurring in the next two small time steps) and the intervention we made (reducing Bs when dosage is 0) is not the same as treatment. Nevertheless, this formulation of effective competition is a good predictor of whether treatment, when added, increases resistance. We used it to classify whether treatment would increase or decrease resistance, and found that the classification worked well, with an area under the receiver–operator characteristic curve (AUC) of 0.94 (the theoretical maximum is 1, and a classifier that guesses randomly has AUC of 0.5). See Appendix figure 10.

### Between-host model

Figure 5 illustrates the behavior of the between-host model at two demonstrative parameter sets, one illustrating resistance decreasing with treatment due to the dominant effect of acquisition of DR from the DS strain, and the other illustrating resistance increasing with treatment as a result of inter-strain competition. Appendix figure 4 shows the relationship between resistance and strength of treatment and its sensitivity to variation in single parameters. No one parameter defines whether treatment increases or decreases resistance.

The model has the possibility of three distinct steady states (equilibria): no disease, both DS and DR present, and only the DR strain present. If there were no acquisition of resistance, there would also be the possibility of an equilibrium with only the DS strain. Figure 5 shows that the stability region of the DR-only equilibrium changes as the similarity coefficient increases. When c = 0, the DR-only equilibrium is invaded by the DS strain as soon as R01 > 1 (vertical blue line). However, when the strains are more similar, R01 must be higher in order to invade, and when c = 1, there is no equilibrium DS prevalence unless R01 ≥ R02.

Appendix figure 9, Figures 6, 7 illustrate how the best policy depends on the fitness of the DR strain and the other parameters. Treatment decreases resistance when the R0 values of both strains are relatively low, the rate of acquisition of resistance is high and the similarity coefficient is low. We find that the parameter groups where aggressive therapy minimizes resistance are well separated by those where moderate therapy is best, by a single DAPC function (Appendix figure 6). Here, the strongest driver of a moderate policy being best is a high similarity coefficient (c, coefficient 0.93). High R02 and R01 (coefficients 1.01, 0.65) contribute, as does a low acquisition rate (coefficient −0.56). Somewhat surprisingly, the rate of competitive release does not contribute to the DAPC weighting (−0.02).

An aggressive strategy is more likely to minimize resistance when the DR strain is relatively unfit (low R02), and the DR population is supported by a high rate of acquisition. Furthermore, an aggressive strategy is likely to be best when the strains are more independent (a low similarity coefficient). Independence means that even a relatively unfit strain can be transmitted in the population, despite the presence of a more fit strain, because when strains are independent they can each super-infect hosts already infected with the other strain, and they can be transmitted from those with dual infection (if these cannot happen then the strains cannot be independent; rather, they would compete for hosts and/or for infectivity). We noted previously (Colijn et al., 2009) that such co-infection can, but does not always, allow DR strains to persist in the long term where they would not be able to do so otherwise; similar results were recently reported by Hansen and Day (2014). Our current results clarify that these effects are a result of the level of competition and are not a consequence of co-infection. Co-infection can be present under high, low, or intermediate levels of competition.

The factors that favor an aggressive policy—lower R02, higher rates of resistance acquisition and increased independence between strains—have the net impact of reducing inter-strain competition. A low R01 also makes an aggressive approach more likely to be preferred (see Appendix figure 9); competition for hosts is low when there are plenty of susceptible hosts, whether the model has strict competition mechanisms or not. This occurs when both R0 values are low. Low R02 means the DR strain is not a fit competitor, a high independence (1 − c) explicitly reduces competition through protection from re-infection and through independent recovery, and a higher mutation rate increases the benefit the DR strain enjoys from DS.

We used the same approach to quantify the short-term competitive interaction as in the within-host model. We reduced the population of the sensitive strain, iterated the model forward two time steps, and computed the effect on the resistant strain (in the absence of treatment). We used the average proportional change in the resistance strain following this direct reduction in the sensitive strain to predict what would happen (increase or decrease) to resistance under treatment. As in the within-host model, this measure of effective competition is a good predictor of the effect of treatment (AUC 0.94; Appendix figure 10).

The models are directly linked through the competitive release, r, which reflects a portion (in the between-host model) of treated sensitive infections that convert to resistant ones. Even where this does not occur at all (r = 0), successful treatment of individuals drives population-level resistance when strains are competing. Consider the within-host model in the regime where aggressive treatment minimizes resistance, for example, low DR growth Λr or a strong immune system, or high rate of acquisition of resistance. Individuals treated successfully are not susceptible to, or infectious with, the sensitive strain. At the between-host level, though, they may remain susceptible to a circulating resistant strain, which now has more susceptible hosts available than the sensitive strain. Treatment (reducing R01) moves the system to the left on the invasion plot (Figure 5C), increasing resistance if there is effective competition at the between-host level.

## Discussion

An aggressive policy for antibiotic treatment is preferred when the appearance and persistence of DR is driven by the existence of a sufficiently large DS population. In these settings, the benefits to the DR population which accrue from the acquisition of resistance from DS outweigh the costs of competition from a larger DS population. In contrast, a moderate dosing policy is preferred when the DR strain is a fit enough competitor that acquisition of resistance plays a sufficiently small role in the DR population dynamics. Here, the cost of competition from the DS population outweighs the benefit of additional DR bacteria appearing through acquired resistance. Both modes occur in models containing acquisition of resistance and competition, and a small change in parameters can shift models from one mode to the other. Understanding why previous models and theory have differed in support of aggressive (Ehrlich, 1913; Knudsen et al., 2003; Wiuff et al., 2003; Tam et al., 2005; D'Agata et al., 2007; Ankomah and Levin, 2014; Kim et al., 2014) and moderate (de Roode et al., 2004; Wargo et al., 2007; Gullberg et al., 2011; Huijben et al., 2013) approaches requires evaluating both structural assumptions and parameter choices (Spicknall et al., 2013) as these together affect the strength of effective competition between DR and DS strains. We have used a comprehensive approach to exploring these assumptions and have begun the process of defining measures of effective competition to predict whether moderate or aggressive treatment minimizes resistance.

Previous contradictory results on this question fit neatly into the framework we have presented. In Ankomah and Levin (2014), the model structure incorporates complex interactions between strains, allowing for many facets of competition to be explored. At their chosen parameter values, however, there is little effective competition between DR and DS strains and they found an aggressive policy to be best. In a recent work by Kim et al. (2014), DR strains had two alleles with no onward fitness evolution, little in-host competition, and low DR fitness; consequently, they also found that an aggressive approach would be best. Another recent model (Gomes et al., 2013) assumed that there was competition for resources at high bacterial populations, and concluded that this competition could play a role in suppression of resistant strains. Work by Geli et al. (2012) explored different ecological dynamics and found that strong immunity supports an aggressive policy, but that selection was most intensive at intermediate strengths of treatment in chronic infections (Geli et al., 2012; Kouyos et al., 2014). Gullberg et al. (2011) found that even low concentrations of antibiotic (where the DR and DS fitness may not differ) can rapidly enrich DR sub-populations. Huijben et al. (2013) found experimentally that competitive release of (pre-existing and relatively fit) resistant strains increased with increasing drug pressure.

We conclude that both of these perspectives are reasonable. We find that even in a system where aggressive approaches are most frequently best (the within-host model, based on Ankomah and Levin (2014)), a moderate approach can be preferred if the DR strain is slightly more fit and the environment is slightly more permissive; in this case, inter-strain competition mechanisms, which are always present, are more effective. Likewise, at the between-host level where we might expect herd-level competition effects to play out, we find that even where competition mechanisms are strong, an aggressive approach may be best of one or both strains have a low basic reproduction number or if the rate of acquisition of resistance is high. Both of these factors limit the effective competition.

In most circumstances, we expect that DR and DS variants of a single pathogen compete quite strongly: they will be closely related, and so are likely to share antigenic properties and induce a similar host immune response. They are also likely to consume or be reliant on similar host resources (Fiegna and Velicer, 2005) and occupy similar biological niches within hosts (Dall'Antonia et al., 2005; Lam and Monack, 2014). The extent to which these aspects dominate the fact that resistance is also driven by de novo acquisition, and hence benefits from high DS population levels, will depend on the acquisition rate and mechanism (Lipsitch and Samore, 2002) as well as on the degree of effective competition. Furthermore, models have typically reflected competition for host resources or via a carrying capacity (Geli et al., 2012; Gomes et al., 2013; Ankomah and Levin, 2014), such that competition takes place at high bacterial populations. If direct antagonistic (Claverys and Håvarstein, 2007; Baquero and Lemonnier, 2009) or cooperative (Diard et al., 2013) interactions occur, they are likely to substantially alter the extent and timing of competition, with profound onward consequences for optimal treatment.

We do want to emphasize some key differences between the problem of minimizing resistance among each individual receiving treatment and minimizing resistance of circulating pathogens in a community (Lipsitch et al., 2000; Lipsitch and Samore, 2002; Cohen et al., 2006; zur Wiesch et al., 2011; Geli et al., 2012; Mills et al., 2013). Consider, for example, an immune-competent individual initially harboring a drug-susceptible infection free of any (or many) sporadically resistant isolates. An aggressive approach may well be preferred for this individual. However, if there is a fit resistant strain circulating in the community, then this policy can drive substantial resistance at the population level (e.g., by selectively suppressing the DS strain, making hosts susceptible to re-infections only with the DR strain), even if it does not increase the risk of acquiring resistance in any individual given treatment. Consequently, an aggressive approach might well be best at the individual level while still driving resistance over longer time frames. An aggressive approach may also diminish in utility over time if DR strains become fitter through selection, if they begin to circulate widely and compete with DS strains (zur Wiesch et al., 2011).

Co-infection of individual hosts by multiple strains or isolates has been observed for most pathogens in which it has been investigated (Balmer and Tanner, 2011), and we have incorporated it in both models. At the population level, models that fail to include co-infection assume that co-infections do not occur; this equates to a very strong assumption about competition for hosts, regardless of whether there is sufficient data to inform co-infection parameters.

We have previously argued that diversity-promoting mechanisms in models should be explicit (Lipsitch et al., 2009) and that ‘neutral’ models are a useful framework for understanding implicit assumptions in multi-strain models. Here, we note that such neutrality is competition. The ‘no coexistence for free’ directive can be reframed: we expect identical strains to compete. The extent of competition is a key driver of how the balance between multiple strains changes in response to interventions; if we are to use models to understand these responses, we must be clear about the mechanisms and the extent of effective competition between strains.

These results highlight the importance of identifying empirical data that reveal whether effective competition between DS and DR strains is present. Experimental approaches in which mixed bacterial populations are studied in vitro or in vivo may reveal mechanisms by which these sub-populations may exhibit interference competition through direct interaction (Claverys and Håvarstein, 2007) or exploitative competition through shared dependence on a common resource (Fiegna and Velicer, 2005). These types of controlled experiments have been valuable for identifying conditions under which such direct competition effects are likely to manifest within individual hosts. Identifying data that would reveal the conditions under which we would expect competition between DS and DR strains at the community level is clearly more challenging. The scale and the timing at which we would expect to observe the effects of intraspecific competition will likely differ by pathogen type. Similar to studies of vaccines or other interventions in which indirect effects are important to consider, community-randomized trials are the most promising design, but the expense and logistics of such trials for considering different antibiotic dosing strategies may be prohibitive.

In the absence of such trials, relating population-level antibiotic use data to surveillance data describing trends in resistance in the community may help to identify signals of such competition. Detailed analysis of the numbers and ages of treated cases, the population density, ‘drug-bug’ interactions, and the time since resistance first emerged (Turnidge and Christiansen, 2005) could improve our ability to do this. Meanwhile, careful consideration of the level of effective competition is essential when using models to understand the relationship between antimicrobial use and resistance.
