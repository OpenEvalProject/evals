# Design of an optimal combination therapy with broadly neutralizing antibodies to suppress HIV-1

## Authors

- Colin LaMont<sup>1</sup>
- Jakub Otwinowski<sup>1</sup>
- Kanika Vanshylla<sup>2</sup>
- Henning Gruell<sup>2</sup> ([ORCID: 0000-0002-0725-7138](https://orcid.org/0000-0002-0725-7138))
- Florian Klein<sup>2</sup>
- Armita Nourmohammad<sup>1</sup> ([ORCID: 0000-0002-6245-3553](https://orcid.org/0000-0002-6245-3553)) †

### Affiliations

1. Max Planck Institute for Dynamics and Self-Organization Göttingen Germany ([ROR:0087djs12](https://ror.org/0087djs12))
2. Laboratory of Experimental Immunology, Institute of Virology Faculty of Medicine and University Hospital Cologne, University of Cologne Cologne Germany ([ROR:00rcxh774](https://ror.org/00rcxh774))
3. Department of Physics, University of Washington Seattle United States ([ROR:00cvxb145](https://ror.org/00cvxb145))
4. Fred Hutchinson Cancer Research Center Seattle United States ([ROR:007ps6h72](https://ror.org/007ps6h72))

† Corresponding author

## Abstract

Infusion of broadly neutralizing antibodies (bNAbs) has shown promise as an alternative to anti-retroviral therapy against HIV. A key challenge is to suppress viral escape, which is more effectively achieved with a combination of bNAbs. Here, we propose a computational approach to predict the efficacy of a bNAb therapy based on the population genetics of HIV escape, which we parametrize using high-throughput HIV sequence data from bNAb-naive patients. By quantifying the mutational target size and the fitness cost of HIV-1 escape from bNAbs, we predict the distribution of rebound times in three clinical trials. We show that a cocktail of three bNAbs is necessary to effectively suppress viral escape, and predict the optimal composition of such bNAb cocktail. Our results offer a rational therapy design for HIV, and show how genetic data can be used to predict treatment outcomes and design new approaches to pathogenic control.

## Introduction

Recent discoveries of highly potent broadly neutralizing antibodies (bNAbs) provide new opportunities to successfully prevent, treat, and potentially cure infections from evolving viruses such as HIV-1 (Walker et al., 2011; Walker et al., 2009; Liao et al., 2013; Mouquet and Nussenzweig, 2013; Klein et al., 2013; Kwong et al., 2013; Caskey et al., 2015; Caskey et al., 2017; Baron et al., 2018; Sok and Burton, 2018; Zwick et al., 2001; Burton et al., 2012, influenza Sparrow et al., 2016, and the Dengue virus Ekiert and Wilson, 2012; Durham et al., 2019). bNAbs target vulnerable regions of a virus, such as the CD4 binding site of HIV env protein, where escape mutations can be costly for the virus (Walker et al., 2009; Chen et al., 2009; Zhou et al., 2010; Walker et al., 2011; Liao et al., 2013; West et al., 2014; Burton and Hangartner, 2016). As a result, eliciting bNAbs is the goal of a universal vaccine against the otherwise rapidly evolving HIV-1. Apart from vaccination, bNAbs can also offer significant advances in therapy against both HIV-1 and influenza (West et al., 2014; Caskey et al., 2016; Gruell and Klein, 2018; Durham et al., 2019). Specifically, augmenting current anti-retroviral therapy (ART) drugs with bNAbs may provide the next generation of HIV therapies (Horwitz et al., 2013; Gruell and Klein, 2018).

Recent studies have used bNAb therapies to curb infections by the Simian immunodeficiency virus (SHIV) in non-human primates (Shingai et al., 2013; Barouch et al., 2013; Julg et al., 2017), and HIV-1 infections in human clinical trials (Caskey et al., 2015; Bar et al., 2016; Caskey et al., 2017; Baron et al., 2018). Monotherapy trials with potent bNAbs, including 3BNC117 (Caskey et al., 2015, VRC01 Bar et al., 2016, and 10–1074 Caskey et al., 2017) indicate that administering bNAbs is safe and can suppress viral load in patients. Nonetheless, in each trial, escape mutants emerge resulting in a viral rebound after about 20 days past infusion of the bNAb. However, in trials that administered a combination of 10–1074 and 3BNC117, viral rebound was substantially suppressed (Shingai et al., 2013; Baron et al., 2018). The success of combination therapy is not surprising. For example, combinations of drugs has been repeatedly used against infectious agents, including current HIV ART cocktails and combination antibiotic treatments against Tuberculosis (Lienhardt et al., 2012).

The principle behind combination therapy with either drugs or antibodies is clear: It is harder for a pathogen population to acquire resistance against multiple treatment targets simultaneously than to acquiring resistance against each target separately. But deciding on combination therapy means navigating an enormous number of possible treatment options.

Experimental data from neutralization assays against pseudo-viruses together with modeling and machine learning techniques have been used to statistically characterize the efficacy of bNAbs and their combinations against different variants of HIV (Wagh et al., 2016; Yu et al., 2019). Using these neutralization models, an optimal combination therapy was proposed based on their breadth, potency of neutralization, and other relevant measures (Wagh et al., 2016; Yu et al., 2019). In another study, pharmacokinetic dynamics was coupled with drug-interaction models to determine an optimal dosing strategies (Mayer et al., 2022). These modeling approaches shed light on how combinations of bNAbs that can neutralize a panel of viruses. However, the key obstacle in bNAb therapy is the possibility of viral escape.

To characterize viral escape, mechanistic models, partly inspired by previous work on HIV escape from the anti-retro viral therapy (ART), have been developed to explain the dynamics of viremia in patients, following passive infusion of bNAbs. By making a fit to the trial data, these models are used to infer parameters related to the efficacy of a bNAb in clearing virions, reducing viral load and infectivity, and also to infer the characteristics of the HIV and the T-cell populations, such as the initial viral population size, the death rates of uninfected and infected T-cells, and the number of virions released by an infected T-cell (Perelson et al., 1996; Ribeiro and Bonhoeffer, 2000; Rong et al., 2010; Rong et al., 2007; Tomaras et al., 2008; Lu et al., 2016; Reeves et al., 2020; Saha and Dixit, 2020; Cardozo-Ojeda and Perelson, 2021; Stephenson et al., 2021). These detailed mechanistic models cannot easily generalize from one trial to another in order to predict the efficacy of a new bNAb mono- or combination therapy.

Evolution of the HIV-1 population is another key factor to consider in modeling the dynamics and escape of viruses in response to therapy. Studies on population genetics of HIV-1 have found rapid intra-patient evolution and turnover of the virus (Lemey et al., 2006; Zanini et al., 2015) and have indicated that the efficacy of drugs in ART can severely impact the mode of viral evolution and escape (Feder et al., 2016). Despite the complex evolutionary dynamics of HIV-1 within patients due to individualized immune pressure (Nourmohammad et al., 2019), genetic linkage (Zanini et al., 2015), recombination (Neher and Leitner, 2010; Zanini et al., 2015), and epistasis between loci (Bonhoeffer et al., 2004; Zhang et al., 2020), the genetic composition of a population can still provide valuable information about the evolutionary significance of specific mutations, especially in highly vulnerable regions of the virus. For example, analysis of genomic covariation in the Gag protein of HIV-1 has been successful in predicting fitness effect of mutations in relatively conserved regions of the virus, which could inform the design of rational T-cell therapies that target these vulnerable regions (Ferguson et al., 2013). In the context of bNAb therapy trials, an evolutionary model accounting for the intrinsic fitness cost associated with escape variants against a specific bNAb has been used to characterize HIV-1 dynamics and escape following bNAb infusion (Meijers et al., 2021).

In this study, we present a coarse-grained evolutionary model of viral response to bNAb infusion that uses genetic data of HIV-1 in untreated patient to predict bNAb therapy outcome by characterizing the chances of viral escape from a given bNAb in patients. Specifically, we develop a statistical inference framework that uses the high throughput longitudinal survey of viral sequences collected from 11 ART-naive patients over about 10 years of infection (Zanini et al., 2015) to characterize the evolutionary fate of escape mutations and to predict patient outcomes in recent mono- and combination therapy trials with 10–1074 and 3BNC117 bNAbs (Caskey et al., 2015; Caskey et al., 2017; Baron et al., 2018), and a trial with PGT121 bNAb (Stephenson et al., 2021). Using the accumulated intra-patient genetic variation from deep sequencing of HIV-1 populations in ART–naive patients (Zanini et al., 2015), we can estimate the diversity and the fitness effects of mutations at sites mediating escape. These variables parametrize our individual-based model for viral dynamics and characterize the expected path for a potential escape of HIV-1 populations in response to bNAb therapies in patients enrolled in the clinical trials. Although our coarse-grained model does not accurately reproduce the detailed dynamics of viremia in each patient and lacks the mechanistic insight of richer models proposed by Perelson et al., 1996; Rong et al., 2010; Rong et al., 2007; Tomaras et al., 2008; Cardozo-Ojeda and Perelson, 2021; Stephenson et al., 2021, it still accurately predicts the distribution of viral rebound times in response to passive bNAb infusions — a key measure the efficacy for a bNAb clinical trial.

Our prediction for the viral rebound time in response to a bNAb relies on only a few patient-specific parameters (i.e. the genetic diversity of patients prior to treatment), and is primarily done based on the inferred genetic parameters from the deep sequencing of HIV-1 populations in a separate cohort of ART-naive patient. Therefore, our model could be used to guide therapy trial design with bNAbs against which viral escape variants are previously characterized. To this end, we use our approach to assess a broader panel of nine bNAbs, for which escape sites can be identified from prior deep mutational scanning experiments (Dingens et al., 2019), to characterize the therapeutic efficacy of each of these bNAbs and to propose optimal combination therapies that can efficiently curb an HIV-1 infection. Our results showcase how the wealth of genetic data can be leveraged to guide rational therapy approaches against HIV. Importantly, this approach is potentially applicable to therapy designs against other evolving pathogens, such as chronic viruses like HCV, resistant bacteria, or cancer tumor cells.

### Model

#### HIV-1 response to therapy

After infusion of bNAbs in a patient, the antibodies bind and neutralize the susceptible strains of HIV. The neutralized subpopulation of HIV-1 no longer infects T-cells, and the plasma RNA copy-number associated with this neutralized population decays. The dynamics of viremia in HIV-1 patients off ART following a bNAb therapy with 3BNC117 (Caskey et al., 2015), 10–1074 (Caskey et al., 2017), and their combination (Baron et al., 2018 ) are shown in Figure 3—figure supplements 1–3. With competition of the neutralized strains removed, the resistant subpopulation grows until the viral load typically recovers to a level close to the pretreatment state (i.e. the carrying capacity); see Figure 1A. The time it takes for the viral load to recover is the rebound time—a key quantity that characterizes treatment efficacy within a patient. Although the details of the viremia dynamics, especially at beginning and at the end of the therapy, may be complex (Lu et al., 2016; Reeves et al., 2020; Saha and Dixit, 2020; Meijers et al., 2021), the rebound time can be approximately modeled using a logistic growth after bNAb infusion (t > 0),

$$
N(t)={N_{k}t\leq0(1−x)N_{k}e^{−rt}+\frac{N_{k}}{1+\frac{1−x}{x}e^{−\gammat}}t>0
$$

with the initial condition set for pre-treatment fraction of resistant subpopulation $x=N_{r}⁢(0)/(N_{r}⁢(0)+N_{s}⁢(0))$, where $N_{r}⁢(0)$ and $N_{s}⁢(0)$ denote the size of resistant and susceptible subpopulations at time $t=0$, respectively. Here, $\gamma$ is the growth rate of the resistant population, $r$ is the neutralization rate impacting the susceptible subpopulation, and $N_{k}$ is the carrying capacity (Figure 1A, Methods). In our analysis, we set $\gamma=1/3⁢ days^{-1}$ or a doubling time of $∼2$ days, the known HIV-1 growth rate in patients (Perelson et al., 1996). We infer the neutralization rate $r$ as a global parameter for each trial, since it depends on the neutralization efficacy of a bNAb at the concentration used in the trial. We will infer the patient-specific pre-treatment fraction of resistant subpopulation $x$, using a population genetics based approach based on which we characterize the mutational target size and selection cost of escape in the absence of a bNAb (see below). The maximum-likelihood fits of $N⁢(t)$ to the viremia measurements in Figures 2 and 3, Figure 3—figure supplements 1–3 specifies the initial resistant fraction xp and the rebound time $T_{p}$ in each patient $p$, which in this simple model, is given by $T_{p}=-\gamma^{-1}⁢log⁡x_{p}$ (Methods).

![Figure 1.](https://cdn.elifesciences.org/articles/76004/elife-76004-fig1-v2.jpg)

**Figure 1.:** (A) The viral dynamics after the initiation of a treatment with bNAb infusion ($t=0$) is determined by two competing processes. Susceptible strains (sus) undergo exponential decay (red line) with decay rate given by $r$, while the resistant mutants (mut) undergo logistic growth back up to the carrying capacity ($N_{k}$) of the patient. In the deterministic limit (Equation 1), the rebound time is linearly related to the log-frequency of the mutant fraction. (B) The schematic shows the four stochastic processes of birth, death, mutation, and neutralization with their respective rates for susceptible (purple) and resistant (blue) variants. These processes define the evolution of a viral population. Note that both the susceptible and the resistant variants are subject to birth and death with their respective rates. (C) The birth and death rates can be visualized as a region of size $\lambda=\beta+\delta$ which is partitioned into birth and death events. In the absence of antibodies, the susceptible population has balanced birth and death rates, $\beta_{s}=\delta_{s}$, while the resistant population has a negative net birth rate equal to the fitness difference $Δ=\delta_{m}-\beta_{m}$. After introduction of the antibody, the susceptible population decays at rate $r$, and without competition from the susceptible population, the resistant population grows at the free growth-rate $\gamma$. (D) Mutational target size is inferred a priori from the genotype-phenotype mapping, which can be visualized as a bipartite graph. The nodes correspond to codons, while the edges are the mutations which link one codon to another, weighted according to the respective mutation rates. The average edge weight from codons of susceptible variants to the escape mutants determines the rate of escape mutations $\mu$. Mutations can be divided into two types: transitions (black) are within-class, and transversions (red) are out of class nucleotide changes. Transitions occur at about 8 times higher rate than transversions (Figure 2). (E) A coarse grained fitness and mutation model for two of the escape sites (281 and 282) against antibody 3BNC117 are shown. Left: At each escape mediating site, amino acids fall into one of three groups: (i) susceptible (wild-type), (ii) escape mutant, and (iii) fatal. For an escape-class amino acid at site $i$ the virus incurs a fitness cost $Δ_{i}$, and these costs are additive across sites. Right: Mutations at a given site $i$ occur with (independent) forward $\mu_{i}$ and backward $\mu_{i}^{†}$ rates which govern the substitution events between amino acid classes.

![Figure 2.](https://cdn.elifesciences.org/articles/76004/elife-76004-fig2-v2.jpg)

**Figure 2.:** (A) Statistics of the high-throughput longitudinal data collected from HIV-1 populations in 11 ART-naive patients from Zanini et al., 2015, is shown. Some of the have low diversity (vertical red lines) and were not usable for our study. Usable samples (vertical black lines) amount to 4–10 samples per patient, collected over 5–10 years of infection. (B) Lower panels show the relative frequencies (cube-root transformed for legibility) of different amino acids in four patients at the 3 escape sites against the 10–1074 bNAb, estimated from the polymorphism data at the nucleotide level in each patient over time. Despite 10–1074 being a broadly neutralizing antibody, mutations associated with escape (indicated by a *) are commonly observed in untreated patients. The upper right panel shows the number of individuals (out of the cohort of 11 bNAb-naive HIV-1 patients) that carry mutations associated with escape against the indicated bNAbs. (C) The nucleotide diversity associated with transversion $\theta_{tv}=2⁢N_{e}⁢\mu_{tv}$ is shown against the transition diversity $\theta_{ts}=2⁢N_{e}⁢\mu_{ts}$ for all patients (colors) and all time points. The covariance of these two diversity measurements yields an estimate for the transition/transversion ratio $\theta_{ts}/\theta_{tv}=7.6$. (D) Left: The transition diversity is shown to grow as a function of time since infection in all the 11 patients (colors according to (A)). Right: The neutral diversity of viral populations in patients (points) from the three different clinical trials (Caskey et al., 2015; Caskey et al., 2017; Baron et al., 2018) analyzed in this study resemble the larger diversities of long-established viral populations in untreated patients. (E) The inferred forward and backward mutation rates ($\mu,\mu^{†}$), relative to the transition rate, and the median selection strength $\sigma=2⁢N_{e}⁢(f_{sus}-f_{res})$ at each escape site against the two bNAbs (10–1074, and 3BNC117) from the trial data used in this study are shown. Compared to the 10–1074 bNAb, escape from the 3BNC117 bNAb appears to be less costly, and is associated with a smaller mutational target.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/76004/elife-76004-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) The inter-decile ranges of neutral diversity estimates for 103 simulations of genomes of 102 independent neutral sites are shown. The true values of the diversity used for simulations are shown in black. Inter-decile maximum likelihood estimate (MLE) for the diversity $\theta$ from Equation 22 are shown in red, and the observed variance of allele frequency $x$ as a measure of diversity $\theta=2⁢x⁢(1-x)$ is shown in blue. The inferred diversity associated with transversions $\theta_{tv}$ is shown against that of the transition $\theta_{ts}$ for patients (colors) enrolled in (B) the longitudinal study with high throughput HIV-1 sequence data (Zanini et al., 2015), and in the bNAB trials with (C) 10–1074 (Caskey et al., 2017), (D) 3BNC117 (Caskey et al., 2015), and (E) combination of 10–1074 and 3BNC117 (Baron et al., 2018). We find that all four diversity distributions share similar ratios $\theta_{ts}/\theta_{tv}$, indicated in each panel.

![Figure 3.](https://cdn.elifesciences.org/articles/76004/elife-76004-fig3-v2.jpg)

**Figure 3.:** (A) Panels show viremia of three patients from the 3BNC117 trial over time (black circles) and the fitted model of the viral decay and rebound processes from Equation 1 (orange line). The viral rebound time $T$ and the fitted carrying capacity $N_{k}$ is shown in each panel. Shown are examples of a non-responder (NR; left), a rebound occurring during the trial window ($0<T<56$ days; center), and a late rebound ($T>56$ days; right). (B) We compare the distribution of rebound times in patients from the three clinical trials with 10–1074 Caskey et al., 2017, 3BNC117 Scheid et al., 2016, and the combination of the two bNAbs Baron et al., 2018 to the predictions from the simulations based on our evolutionary model (Figure 1, and Methods). The error bars show the inter decile range (0.1–0.9 quantiles) generated by the simulations for the corresponding trial. (C) The summary table shows the number of patients for whom the infecting HIV-1 population shows no response (NR), rebound during the trial window $0<T<56$, and a late rebound ($T>56$ days) in each trial. Note that three patients were excluded from the 3BNC117 trial (*) because of insufficient dosage leading to weak viral response: $1⁢mg/kg$ compared to the $3-30⁢mg/kg$ in the other treatment groups. (D) Plotted are 1,200 trajectories of the mutant viral population simulated using our individual based model. Due to the individual birth-death events, fluctuations are larger when the population size is smaller. At a critical threshold, $x_{ext}$, fluctuations are large enough to lead to almost certain extinction in the existing viral population. The critical threshold (yellow line) is an order of magnitude larger than the post-treatment spontaneously-generated mutant fraction (red line). (E) The predicted fraction of escape events associated with post-treatment spontaneous mutations (red) and the pre-treatment standing variation (yellow) are shown for the three trials. Late rebound events are indicated in blue. Because the spontaneously-generated mutant fraction is smaller than the extinction threshold, these mutations contribute to less than 4% of escape events (red), and escape is likely primarily driven driven by standing variation (yellow), that is, pre-existing escape variants.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/76004/elife-76004-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Panels shows the measured viremia over time (black dots) and the fitted deterministic dynamics from Equation 5 (red line) for all patients off ART in the 10–1074 trial Caskey et al., 2017. Patient-specific fitted carrying capacity $N_{k}$ and the estimated rebound times are reported in each panel. A common decay rate $r=0.36⁢ day^{-1}$ is fitted to all patient data in this trial, and growth rate is set to $0.33⁢ day^{-1}$.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/76004/elife-76004-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Similar to Figure 3—figure supplement 1 but for the 3BNC117 trial Caskey et al., 2015. The cohort treated with a low dosage of bNAb ($1⁢ mg/kg$ as opposed to $3-30⁢ mg/kg$) is shown in yellow; these patients exhibited a very weak response to there treatment and were excluded from our analysis. A common decay rate $r=0.23⁢ day^{-1}$ is fitted to all patient data in this trial, and growth rate is set to $0.33⁢ day^{-1}$.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/76004/elife-76004-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** Similar to Figure 3—figure supplement 1 but for the combination therapy with 10–1074 and 3BNC117 Baron et al., 2018. A common decay rate $r=0.33⁢ day^{-1}$ is fitted to all patients off ART in this trial, and growth rate is set to $0.33⁢ day^{-1}$.

The rebound times following passive infusion of 3BNC117 (Caskey et al., 2015 and 10–1077 Caskey et al., 2017) bNAbs range from 1 to 4 weeks, with a small fraction of patients exceeding the monitoring time window in the studies (late rebounds past 56 days). The distribution of rebound times summarizes the escape response of the virus to a therapy and directly relates to the distribution for the pre-treatment fraction of resistant variants $P⁢(x)$ across patients $P⁢(T)∼x^{-1}⁢P⁢(x)$.

#### Stochastic evolutionary dynamics of HIV-1 subject to bNAb therapy

The fate of an HIV-1 population subject to bNAb therapy depends on the composition of the pre-treatment population with resistant and susceptible variants, and the establishment of resistant variants following the treatment. To capture these effects, we construct an individual-based stochastic model for viral rebound (Figure 1B). We specify a coarse-grained phenotypic model, where a viral strain of type $a$ is defined by a binary state vector $ρ→^{a}=[ρ_{1}^{a},…,ρ_{ℓ}^{a}]$, with $ℓ$ entries for potentially escape-mediating epitope sites; the binary entry of the state vector at the epitope site $i$ represents the presence ($ρ_{i}^{a}=1$) or absence ($ρ_{i}^{a}=0$) of an escape mediating mutation against a specified bNAb at this site of variant $a$. We assume that a variant is resistant to a given antibody if at least one of the entries of its corresponding state vector is non-zero. For multivalent treatment, a virus must be resistant to all antibodies comprising the treatment to have a positive growth after infusion.

At each generation, a virus with phenotype $a$ can undergo one of three processes: birth, death and mutation to another type $b$, with rates $\beta_{a}$, $\delta_{a}$, and $\mu_{a→b}$, respectively (Figure 1B). The net growth rate of the viral subpopulation with phenotype $a$ is the birth rate minus the death rate, $\gamma_{a}=\beta_{a}-\delta_{a}$ (Figure 1C). The total rate of events (birth and death) per virion $\lambda=\beta_{i}+\delta_{i}$ modulates the amount of stochasticity in this birth-death process (Methods), which we assume to be constant across phenotypic variants. The continuous limit for this birth-death process results in a stochastic evolutionary dynamics for the sub-population size $N_{a}$,

$$
\frac{dN_{a}}{dt}={absenceofbNAborifaisresistant:N_{a}(f_{a}−ϕ)+\sumb(N_{b}\mu_{_{b→a}}−N_{a}\mu_{_{a→b}})+\sqrt{N_{a}\lambda}η(t)presenceofbNAbandifaissusceptible:−rN_{a}+\sumb(N_{b}\mu_{_{b→a}}−N_{a}\mu_{_{a→b}})+\sqrt{N_{a}\lambda}η(t)
$$

where $η⁢(t)$ is a Gaussian random variable with mean $⟨η⁢(t)⟩=0$ and correlation $⟨η⁢(t)⁢η⁢(t^{′})⟩=\delta⁢(t-t^{′})$ (Methods). Here, fa denotes the intrinsic fitness of variant $a$ and its net growth rate $\gamma$ is mediated by a competitive pressure $ϕ=\frac{1}{N_{k}}⁢\sum_{b}N_{b}⁢f_{b}$ with the rest of the population constrained by the carrying capacity $N_{k}$, such that $\gamma_{a}=f_{a}-ϕ$. In the presence of a bNAb, birth is effectively halted for susceptible variants and their death rate is set by the neutralization rate of the antibody, resulting in a net growth rate, $\gamma_{sus.}=-r$. At the carrying capacity, the competitive pressure is the mean population fitness $ϕ=f¯$, making the net growth rate of the whole population zero (Figure 1C). When susceptible variants are neutralized by a bNAb, the competitive pressure $ϕ$ drops, and as a result, the resistant variants can rebound to carrying capacity, at growth rates near their intrinsic fitness.

To connect the birth-death model (Equation 2) with data, we should relate the simulation parameters of a birth-death process to molecular observables. We have already made a connection between the birth and death rates of a variant and its intrinsic fitness in Equation 2. In addition, the neutral diversity $\theta$ of a population at steady-state can be expressed as $\theta=2⁢N_{k}⁢\mu/\lambda$, where $\mu≈10^{-5}/ day$ is the per-nucleotide mutation rate, which we infer from intra-patient longitudinal HIV-1 sequence data (Zanini et al., 2015) (Methods). For consistency, we set the total rate of events $\lambda$ to be at least as large as the fastest process in the dynamics, which in this case is the growth rate of resistant viruses $\gamma≈(3⁢ days)^{-1}$, we choose $\lambda=(0.5⁢ days)^{-1}$ (Methods). Therefore, the key parameters of the birth-death model, that is, $\beta,\delta, and ⁢N_{k}$ can be expressed in terms of the intrinsic fitness of the variants fa and the neutral diversity $\theta$, which we will infer from data.

## Results

### Population genetics of HIV-1 escape from bNAbs

HIV-1 escape from different bNAbs has been a subject of interest for vaccine and therapy design, and a number of escape variants against different bNAbs have been identified in clinical trials or in infected individuals (Lynch et al., 2015; Caskey et al., 2015; Scheid et al., 2016; Caskey et al., 2017; Baron et al., 2018). This in-vivo data is often complemented with information from co-crystallized structures of bNAbs with the HIV-1 envelope protein (Pancera et al., 2017), and in-vitro deep mutational scanning (DMS) experiments, in which the relative change in the growth rate of tens of thousands of viral mutants are measured in the presence of different bNAbs (Dingens et al., 2019; Dingens et al., 2017; Schommers et al., 2020). We identify escape mutations against each of the bNAbs in this study by using information from clinical trials, the characterized binding sites, and the DMS assays (Methods); the list of escape mutations against each bNAb is given in Appendix 1—table 1.

The rise and establishment of an escape variant against a specific bNAb depend on three key factors, (i) neutral genetic diversity of the viral population, (ii) the mutational target size for escape from the bNAb (i.e. the number of paths leading to escape, weighted by their respective probabilities), and (iii) the intrinsic fitness associated with such mutations. Although viremia traces in clinical trials and growth experiments can be used to model the escape dynamics (Haddox et al., 2018; Lynch et al., 2015; Lu et al., 2016; Reeves et al., 2020; Saha and Dixit, 2020; Meijers et al., 2021), they do not offer a comprehensive statistical description for HIV-1 escape as they are limited by the number of enrolled individuals. Alternatively, mutation and fitness characteristics of such escape-mediating variants can be inferred from a broader cohort of untreated and bNAb-naive patients (Illingworth et al., 2020; Louie et al., 2018). We will infer statistical parameters for our coarse-grained fitness model (Figure 1E) from the large amount of high-throughput HIV-1 sequence data from Zanini et al., 2015 (see Figure 2A and B for details) and use them to parameterize the birth-death model (Figure 1B).

#### Diversity of the viral population

The neutral genetic diversity $\theta=2⁢N_{k}⁢\mu/\lambda$ (i.e. the number of segregating alleles) is an observable that relates to key population genetics parameters, that is, the per-nucleotide mutation rate $\mu$, the population carrying capacity $N_{k}$, and the total number of events per virus in the birth-death process $\lambda$, which determines the noise amplitude in the evolutionary dynamics (Methods). $N_{k}$ and $\lambda$ together determine the effective population size $N_{e}=N_{k}/\lambda$. We use synonymous changes as a proxy for diversity associated with the neutral variation in an HIV-1 population at a given time point within a patient. By developing a maximum-likelihood approach based on the multiplicities of different synonymous variants, we can accurately infer the neutral diversity of a population from the large survey of synonymous sites in the HIV-1 genome (Methods and Figure 2—figure supplement 1). Importantly, we infer the neutral diversity of transition $\theta_{ts}$ and transversion $\theta_{tv}$ mutations separately, and consistent with previous work (Feder et al., 2016; Zanini et al., 2017), find that transitions occur with a rate of about 8 times larger than transversions (Figure 2C, Figure 2—figure supplement 1B-E).

Our inference indicates that the neutral diversity grows over the course of an infection in untreated HIV-1 patients from Zanini et al., 2015 (Figure 2D). The patients enrolled in the three bNAb trials (Caskey et al., 2015; Caskey et al., 2017; Baron et al., 2018) show a broad range of neutral diversity prior to bNAb therapy (Figure 2D). In addition to the circulating viruses in a patient’s sera, the viral reservoir, which consists of replication-competent HIV-1 in latently infected cells or un-sampled tissue, can also contribute to a bNAb escape in a patient. Evidence that the latent reservoir can contribute to HIV escape from bnAbs is directly visible in trials as the failure of pre-trial sequencing to exclude patients who do not harbor escape variants. We model the effect of the reservoir as augmenting the neutral diversity by a constant multiplicative factor $r_{resv.}$, so that patients with more diverse sera, representing usually longer infections, are also expected to have correspondingly more diverse reservoir populations. By fitting the observed rebound data, we infer the reservoir factor $r_{resv.}≃2.07$ (Methods, Figure 4—figure supplement 1). We use the augmented genetic diversity of HIV-1 prior to the bNAb therapy in each trial to generate the rebound time and the probability of HIV-1 escape in patients.

#### Mutational target size for escape

We define the mutational target size for escape from a bNAb as the number of trajectories that connect the susceptible codon to codons associated with escape variants, weighed by their probability of occurrences (Methods). The connecting paths with only single nucleotide transitions or transversions dominate the escape and can be represented as connected graphs shown in Figure 1D. To characterize the target size of escape for each bNAb, we determine the forward mutation rate $\mu≡\mu_{sus.→res.}$ from the susceptible codons to the resistant (escape) codons, and the reverse mutation rate $\mu^{†}≡\mu_{sus.←res.}$ back to the susceptible variant (Figure 1D, Methods). The mutational target sizes vary across bNAbs, with HIV-1 escape being most restricted from 10E8 ($\mu/\mu_{ts}=1.8$ where $\mu_{ts}$ is the single-nucleotide transition substitution rate) and most accessible in the presence of 10–1074 ($\mu/\mu_{ts}=4.9$); see Figure 4C and Appendix 1—table 1 for the list of mutational target size for escape against all bNAbs in this study.

![Figure 4.](https://cdn.elifesciences.org/articles/76004/elife-76004-fig4-v2.jpg)

**Figure 4.:** (A) The posterior distribution for inferred selection strength on the escape-mediating sites associated with each of the 9 bNAbs in this study is shown (right); white line: median, box: 50% around the median, bar: 80% around median. Each escape site is color coded by its location on the env gene (left) and each antibody by its associated epitope location. (B) The harmonic mean of the selection strength $\sigma$ associated with cost of escape (scaled by transition diversity $\theta_{ts}$) is shown against the mutational target size for each bNAb; error bars indicate 50% around the median. For antibodies to be broadly neutralizing, it is sufficient that viral escape from them to be associated with a small mutational target size or a large fitness cost. The mutational target size is found to be weakly correlated with the average cost of escape from a given bNAb. We identify two distinct strategies for antibody breadth—selection limited and mutational-target-size limited escape pathways each highlighted in gray. (C) bNAb therapies with 1, 2, and 3 antibodies are ranked based on the predicted probability of early viral rebound, and in each case, six therapies with highest efficacies are shown; best ranked therapy is associated with the lowest probability of early rebound (lt56 days); indicate 50% around the median. Also for reference, the probability of early viral rebound two therapies from the trials in this study (10–1074 and 10–1074+3BNC117) are shown.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/76004/elife-76004-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Fitness cost for escape mediating sites of different bNAbs is shown based on the selection inference using (A) the time-averaged likelihood (Equation 40 $t$-averaged) with data from all patients, as a reference (similar to Figure 4A), (B) the time-averaged likelihood (Equation 40 $t$-averaged) with data from patients infected with HIV-1 clade B only, and (C) independent time likelihood (Equation 40 $t$-independent) with data from all patients. Limiting the inference to patients infected with clade B virus in (B) result in minor changes in the inferred selection strength and a slight increase in uncertainties due to a smaller data. However, the general structure of the posteriors remain similar to (A). Treating all time points as independent in (C) increases the effective sample-size of the data and reduces model uncertainty. Nonetheless, except for slight changes on the selection ordering of escape sites against 3BNC117, the median of the selection posteriors remain similar to (A). The color code is similar to Figure 4A and is determined by the env region associated with each site.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/76004/elife-76004-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Results of selection inference for simulated populations that carry escape mediating sites linked with other selected sites in the genome are shown. The blue shading shows the interdecile ranges (0.1–0.9 quantiles) for the inferred maximum likelihood estimates (MLE) of scaled selection $\sigma^=\sigma/\theta_{ts}$ on the escape mediating sites versus the true values used in the simulations, for different genetic linkage effects (columns) and different values of population diversity (rows). Each inferred value is based on 10 realizations of simulations (in-silico patients) for populations evolving over time, with samples taken at 10 time points spaced at 100 days. Simulations are done on whole genomes of length 512, in which 32 sites under strong selection $0.02⁢f_{0}$ are equally spaced throughout the genome; f0 is the base growth rate of $1.0⁢ day^{-1}$. Each day, the preferred allele in one of the 32 sites is swapped (selection changes sign) with probability $p_{flip}$. The rate of selection fluctuation $p_{flip}$ and the recombination rate $χ$ are given in each panel. The carrying capacity is set to $N_{k}=5,000$, and the event rate is $\lambda=2⁢ day^{-1}$; see Algorithm 3 (Appendix 5). To initialize, we let the populations equilibrate for $4⁢N_{e}$ generations, and then gather data for maximum likelihood inference of selection at the escape mediating sites. In all panels, the median MLE for selection (black line) closely matches the true selection strength (redline). Quantile lines are smoothened by a Gaussian kernel. Variation is largest when diversity is low and when mutants are rare, which concords with the results from the Bayesian inference procedure.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/76004/elife-76004-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** (A) The predicted rebound times without including an increase in diversity due to reservoirs (i.e. $ξ_{0}=1$ in Equation 42) qualitatively matches the data from the three trials (histograms in each panel), with an overestimation in the number of non-responders and patients with late rebound. For comparison, the predictions with reservoir-corrected diversity is shown in Figure 3A. (B) The disparity $R⁢(ξ|t_{1:p})$ (Equation 35) is shown as a function of the reservoir factor $ξ$ for the three trials (colors; left panel). The total disparity over all trials is shown in the right panel, where $Δ_{R}$ indicates the reduction in disparity by using the optimal reservoir factor $ξ^{*}=2.1$. (C) The distribution for the reduction in disparity $Δ_{R}$ (Equation 41) is shown for 1000 realizations of simulated data under the null hypothesis with $ξ_{0}=1$. The large reduction in disparity indicates that the null hypothesis can be rejected with $p-value=0.004$ (Equation 42).

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/76004/elife-76004-fig4-figsupp4-v2.jpg)

**Figure 4—figure supplement 4.:** (A) The disparity $R⁢(ξ_{s}|t_{1:p})$ (Equation 35) is shown as a function of rescaling of the selection strength $\sigma/\theta_{ts}$ by a multiplicative factor $ξ_{s}$. The total disparity over all trials is shown in the right panel, where $Δ_{R}$ indicates the reduction in disparity by using the optimal selection factor $ξ_{s}=.8$. In this case the null hypothesis is that the inferred selection by the Bayesian procedure in Equation 31 requires no further rescaling for the model to fit the distribution of the rebound times (i.e. $ξ_{s}=1$). The large $p-value=0.49$ shown in (B) indicates that the null hypothesis cannot be rejected and we have no statistical justification for adding an adjustment factor for selection inferred from untreated patients.

#### Fitness effect of escape mutations

Since bNAbs target highly conserved regions of the virus, we expect HIV-1 escape mutations to be intrinsically deleterious for the virus (Ferguson et al., 2013; Meijers et al., 2021), and incur a fitness cost relative to pre-treatment baseline f0. We assume that fitness cost associated with escape mutations are additive and background-independent so the fitness of a variant $a$ in the absence of bNAb follows, $f_{a}=f_{0}-\sum_{i}Δ_{i}⁢\sigma_{i}^{a}$, where $Δ_{i}$ is the cost associated with the presence of a escape mutation at site $i$ (i.e., for $\sigma_{i}^{a}=1$); see Figure 1D.

Interestingly, we observe the escape variants against different bNAbs to be circulating in the HIV-1 populations from the cohort of ART- and bNAb-naive patients (Zanini et al., 2015, Figure 2B). We use this data (Zanini et al., 2015) and extract the multiplicity of susceptible and escape variants in HIV-1 populations at each sampled time point from a given patient. We use a single locus approximation under strong selection to represent the stationary distribution of the underlying frequency of escape alleles $x$ in each patient from (Zanini et al., 2015), $P⁢(x;\sigma,\theta,\theta^{†})∼x^{-1+\theta}⁢(1-x)^{-1+\theta^{†}}⁢exp⁡[-\sigma⁢x]$, given the (scaled) fitness difference between the susceptible and the escape variants $\sigma=2⁢N_{e}⁢(f_{sus}-f_{mut})$; see Methods.

Based on the statistics of escape and susceptible variants in all patients, we define a likelihood function that determines a Bayesian posterior for selection $\sigma$ associated with escape at each site (Methods). We found that it is statistically more robust to infer the strength of selection relative to a reference diversity measure $\sigma/\theta_{ts}=(f_{sus.}-f_{res.})/\mu_{ts}$, for which we choose the transition rate (Methods). This approach generates unbiased selection estimates in simulations and is robust to effects of linkage and recombination (Methods and Model robustness Figure 4—figure supplement 1, Figure 4—figure supplement 2). The inferred values of the scaled fitness costs $\sigma/\theta_{ts}$ are shown for the escape-mediating sites of the trial bNAbs in Figure 2E, and are reported in Appendix 1—table 1.

### Predicting the efficacy of bNAb therapy in clinical trials

Monotherapy trials with 10–1074 (Caskey et al., 2017, 3BNC117 Caskey et al., 2015,PGT121 Stephenson et al., 2021), and the combination therapy with 10–1074+3BNC117 in Baron et al., 2018 have shown variable outcomes. In some patients, bNAb therapy did not suppress the viral load, whereas in others suppression was efficient and no rebound was observed up to 56 days after infusion (end of surveillance in these trials); see Figure 3A for examples of patients with different rebound times, Figure 3—figure supplements 1–3 for the viremia traces in all patients, and Figure 3B and C for the distributions and the summary statistics of the rebound times in patients in different trials.

Although we infer a large intrinsic fitness cost for a virus to harbor an escape allele (Figure 2E), these variants can emerge or already be present due to the large intra-patient diversity of HIV-1 populations (Figure 2C), or a larger mutational target size for these escape variants. Deep sequencing data in untreated (likely bNAb-naive) patients shows circulation of resistant variants against a panel of bNAbs in the majority of patients (Figure 2B). Our goal is to predict the efficacy of a bNAb trial, using the fitness effect and the mutational target size for escape from a given bNAb, both of which we infer from the high-throughput HIV-1 sequence data collected from bNAb-naive patients in Zanini et al., 2015 (Figure 2E, Appendix 1—table 1). In addition, we modulate these measures with the patient-specific neutral diversity $\theta$ inferred from whole genome sequencing of HIV-1 populations in each patient prior to bNAb therapy (Figure 2D). These quantities parametrize the birth-death process for viral escape in a bNAb therapy (Figure 1A), which we use to characterize the distribution of rebound times in a given trial (Methods).

For both the 3BNC117 and the 10–1074 trials (Caskey et al., 2015; Caskey et al., 2017), we see an excellent agreement between our predictions of the rebound time distribution and data; see Figure 3B, and Methods and Figure 4—figure supplement 3 for statistical accuracy of this comparison. For the PGT121 trial, the genomic data from patients’ HIV-1 populations are insufficient and therefore, we used the neutral diversity $\theta_{ts}$ estimated from the other three trials to predict the associated rebound time distribution (Appendix 4). Still, we see a good agreement between our predictions of the rebound time distribution and data; see Appendix 4—figure 1.

By assuming an additive fitness effect for escape from 10 to 1074 and 3BNC117, we also accurately predict the distribution of rebound times in the combination therapy (Baron et al., 2018, Figure 3B). The agreement of our results with data for combination therapy is consistent with the fact that the escape mediating sites from 10 to 1074 and 3BNC117 are spaced farther apart on the genome than 100 bp, beyond which linkage disequilibrium diminishes due to frequent recombination in HIV (Zanini et al., 2015). Importantly, in all the trials, our evolutionary model accurately predicts the fraction of participants for whom we should expect a late viral rebound (more than 56 days past bNAb infusion)—the quantity that determines the efficacy of a treatment.

Apart from the overall statistics of the rebound times, our stochastic model also enables us to characterize the relative contributions of the pre-treatment standing variation of the HIV-1 population versus the spontaneous mutations emerging during a trial to viral escape from a given bNAb. Given the large population size of HIV-1 and a high mutation rate ($\mu=10^{−5}$ per generation), spontaneous mutations generate a fraction $x^{(\mu)}$ of resistant variants during a trial, which we can express as,

$$
x^{(\mu)}=\int_{0}^{56⁢ wks}(1-x⁢(0))⁢e^{-r⁢t}⁢\mu⁢\gamma⁢d⁢t
$$

In the best case scenario, there are no resistant virions prior to treatment i.e., $x⁢(0)=0$. Since the neutralization rate $r$ and the growth rate $\gamma$ are comparable, this deterministic approach predicts that mutations can generate a resistant fraction of $x^{(\mu)}≈10^{-5}$ during a trial. However, stochastic effects from random birth and death events play an important role in the fate and establishment of these resistant variants. The probability of extinction for a variant at frequency $x$ can be approximated as $p⁢(extinct)≈1-e^{-x/x_{ext}}$ (see Extinction Probability); here $x_{ext}=\frac{\mu_{t⁢s}}{\gamma⁢\theta_{t⁢s}}≈10^{-4}$ and a variant with fraction $x$ that falls below this critical value is likely to go extinct (Figure 3D). Since the total integrated mutational flux fraction during a trial is $x^{(\mu)}∼10^{-5}$, mutational flux rarely decides the outcome of patient treatment. Indeed, we infer that spontaneous mutations contribute to less than 4% of escape events in all the three trials and escape is primarily attributed to the standing variation from the serum or the reservoirs prior to therapy (Figure 3E). A similar conclusion was previously drawn based on a mechanistic model of escape in VRC01 therapy trials (Saha and Dixit, 2020).

### Devising optimal bNAb therapy cocktails

Clinical trials with bNAbs have been instrumental in demonstrating the potential role of bNAbs as therapy agents and in measuring the efficacy of each bNAb to suppress HIV. Still, these clinical trials can only test a small fraction of the potential therapies that can be devised. It is therefore important that trials test therapies that have been optimized based on surrogate estimates of treatment efficacy. The accuracy of our predictions for the rebound time of a HIV-1 population subject to bNAb therapy suggests a promising approach to the rational design of therapies based on genetic data of HIV populations collected from bNAb-naive patients.

Here, we use viral genome sequences to infer the efficacy of therapies with bNAbs, for which clinal trials are not yet performed. To do so, we first need to identify the routes of HIV escape from these bNAbs. We use deep mutational scanning data (DMS) on HIV-1 subject to 9 different bNAbs from Dingens et al., 2019 together with information from literature to identify the escape mediating variants from each of these bNAbs (Methods and Table S1). We then determine the mutational target size and the fitness effect of these escape variants using high-throughput sequences of HIV-1 in bNAb-naive patients from Zanini et al., 2015; these inferred values are reported in Figure 4A and B and Table S1. Using the inferred fitness and mutational parameters and by setting the pre-treatment neutral diversity $\theta$ to be comparable to that of the patients in the previous three trials with 10–1074 and 3BNC117 (Figure 2C), we simulate treatment outcomes for these 9 bNAbs and their twofold and threefold combinations.

Interestingly, we infer that escape from mono-therapies is almost certain and a combination of at least three antibodies is necessary to limit the probability of early rebound (<56 days) to below 1% (Figure 4C). When considering each of the nine antibodies, interesting patterns emerge. We find that the mutational target size and the fitness cost of escape, estimated as the harmonic-mean selection cost of individual sites, obey a roughly linear relationship (Figure 4B). As all these bNAbs have similar overall breadth (i.e. they neutralize over 70% of panel strains), this result suggests that for an antibody to be broad, its escape mediating variants should either be rare (i.e. small mutational target size) or intrinsically costly (i.e. incurring a high fitness cost), but it is not necessary to satisfy both of these requirements. For instance, we find that resistant variants against 10E8 weaker negative selection but escape target size is small, while PGT151 has a larger escape target size but makes up for it by having resistant variants with unavoidably high fitness cost.

The fitness-limited versus the mutation-limited strategies have different implications for the design of combination cocktails. The small mutational target size of 10E8 makes it the best candidate antibody for mono-therapy among the antibodies we consider because the escape variants against this antibody are less likely to circulate in a patient’s serum prior to treatment. However, in combination, 10E8 appears less often in top ranked therapies than PGT151. PGT151 is unremarkable on its own because of a relatively large target size, but the high cost of escape makes it especially promising in combination therapies. Overall, fitness-limited bNAbs like PGT151 are more effective against high diversity viral populations, while mutation-limited bNAbs such as 10E8 are more effective against low diversity viral populations. Indeed, the best ranked therapy, namely the combination of PG9, PGT151, and VRC01, combines antibodies that target different regions of the virus and also have both types of fitness- and mutation-limited strategies for coverage against the full variability of viral diversities found in pre-treatment individuals (Figure 4C) participating in the clinical trials.

Escape from bNAbs in multivalent therapy is also influenced by the non-independence of escape pathways. Several of the bNAbs (e.g. 10–1074 and PG121) in this study target the same (or structurally adjacent) epitopes and escape from them is mediated by the same mutations. The sharing of mutational pathways invalidates the assumption of independence and may make our predictions too optimistic. However, the best performing antibody combinations in Figure 4C target multiple epitopes to reduce the chances of collective escape. Therefore, the assumptions of independent fitness effects and independent mutational pathways in this case are not consequential for the main predictions of our model (i.e., the choice of bNAb combinations). In vitro data shown in Kong et al., 2015 suggest that additive and independent effects are the norm, but that small but consistent synergistic effects may imply that our assumption of site-wise independence is conservative. More data on HIV escape from combinations of bNAbs would be informative for further modeling efforts and relevant for long-term therapy design.

## Discussion

HIV therapy with passive bNAb infusion has become a promising alternative to anti-retroviral drugs for suppressing and preventing the disease in patients without a need for daily administration. The current obstacle is the frequent escape of the virus seen in mono- and even combination bNAb therapy trials (Caskey et al., 2015; Bar et al., 2016; Caskey et al., 2017; Baron et al., 2018). The key is to identify bNAb cocktails that can target multiple vulnerable regions on the virus in order to reduce the likelihood for the rise of resistant variants with escape-mediating mutations in all these regions. Identifying an optimal bNAb cocktail can be a combinatorially difficult problem, and designing patient trials for all the potential combinations is a costly pursuit.

Here, we have proposed a computational approach to predict the efficacy of a bNAb therapy trial based on population genetics of HIV escape, which we parametrize using high-throughput HIV-1 sequence data collected from a separate cohort of bNAb-naive patients (Zanini et al., 2015). Specifically, we infer the mutational target size for escape and the fitness cost associated with escape-mediating mutations in the absence of a given bNAb. These quantities together with the neutral diversity of HIV-1 within a patient parametrize our stochastic model for HIV dynamics subject to bNAb infusion, based on which we can accurately predict the distribution of rebound times for HIV in therapy trials with 10–1074, 3BNC117 and their combination, as well as a trial with PGT121 bNAb. Consistent with previous work on VRC01 (Saha and Dixit, 2020), we found that viral rebounds in bNAb trials are primarily mediated by the escape variants present either in the patients’ sera or their latent reservoirs prior to treatment, and that the escape is not likely to be driven by the emergence of spontaneous mutations that establish during the therapy.

One key measure of success for a bNAb trial is the suppression of early viral rebound. Our model can accurately predict the rebound times of HIV-1 subject to three distinct therapies (Caskey et al., 2015; Caskey et al., 2017; Baron et al., 2018), based on the fitness and the mutational characteristics of escape variants inferred from high-throughput HIV-1 sequence data. This approach enables us to characterize routes of HIV-1 escape from other bNAbs, for which therapy trials are not available, and to design optimal therapies. We used deep mutational scanning data Dingens et al., 2019 to identify escape-mediating variants against 9 different bNAbs for HIV. Our genetic analysis shows that bNAbs gain breadth and limit viral escape either due to their small mutational target size for escape or because of the large intrinsic fitness cost incurred by escape mutations. bNAbs with mutation-limited strategy are more effective at preventing escape in patients with low viral genetic diversity, while bNAbs with selection-limited strategy are more effective at high viral diversity.

Combination therapy with more than two bnAbs (or drugs in ART) has long been shown to be more effective in suppressing early viral rebound, both in theory and practice (Perelson et al., 1996; Feder et al., 2016; Wagh et al., 2016; Klein et al., 2012; Mendoza et al., 2018; Yu et al., 2019). In addition to corroborating this conclusion quantitatively, we provide a method for assessing new bnAbs for which escape mutations are known. Our method can be understood as a tool to navigate the combinatorial explosion of higher order cocktails for which we cannot possibly test all combinations. By assessing the evolvability of resistance against different combinations we can identify the best therapies to target for clinical trial. Specifically, we show that to suppress the chance of viral rebound to below 1%, we show that a combo-therapy with 3 bNAbs with a mixture of mutation- and selection-limited strategies that target different regions of the viral envelope is necessary. Such combination can counter the full variation of viral diversity observed in patients. We found that PG9, PG151, and VRC01, which respectively target V2 loop, Interface, and CD4 binding site of HIV envelope, form an optimal combination for a 3-bNAb therapy to limit HIV escape in patients infected with clade B of the virus.

The statistical agreement between our coarse-grained model and the observed distribution of the viral rebound times in trials (Figure 3B) implies that many of the mechanistic details are of secondary importance in predicting viral escape. Nonetheless, our approach falls short of reproducing the detailed characteristics of viremia traces in patients, especially at very short or very long times, during which the dynamics of T-cell response or the decay of bNAbs could play a role (Lu et al., 2016; Reeves et al., 2020; Saha and Dixit, 2020). The relationship between the short-term suppression of the virus, which is the focus of this analysis, and the long-term treatment success is complicated by reestablishment of HIV from the latent reservoirs and different modes of intra-host HIV evolution (Liu et al., 2019; Margolis et al., 2017).

One strategy to achieve a longer term treatment success is by combining bNAb therapy with ART. One main advantage of bNAb therapy is the fact that it can be administered once every few months, in contrast to ART, which should be taken daily and missing a dose could lead to viral rebound. Although multivalent bNAb therapy reduces the chances of short-term viral escape, viral escape remains a real obstacle for longer term success of a treatment with bNAbs. Alternatively, (fewer) bNAbs can be administered in combination with ART (Horwitz et al., 2013; Gruell and Klein, 2018), whereby ART could lower the replication rate of the HIV population, reducing the viral diversity and the chances of viral escape. Specifically, we can expect that emergence and establishment of rare (i.e., strongly deleterious) escape variants against bNAbs to be less likely in ART+ patients, which suggests that fitness-limited bNAbs should be more effective in conjunction with ART. More data would be necessary to understand the long-term efficacy of such augmented therapy, and specifically the role of viral reservoirs in this context. A modeling approach could then shed light on how ART administration and bNAb therapy could be combined to efficiently achieve viral suppression.

### Limitations

We rest our analysis primarily on the predictive power of the observed variant frequencies in the untreated patients. Our model weighs these frequencies with respect to the viral diversity in a mathematically and biologically consistent way. However, we ignore the dynamics of antibody concentration and IC50 neutralization during treatments, the details of T-cell dynamics during infection (Perelson, 2002), and also the evolutionary features of the genetic data, such as epistasis between loci (Bonhoeffer et al., 2004; Zhang et al., 2020, genetic linkage Zanini et al., 2015, and codon usage bias Meintjes and Rodrigo, 2005).

In our model of viral escape, we neglect the possibility of incomplete escape of the virus due to the reduced neutralization efficacy of bNAbs as their concentrations decay during trials. In Appendix 3, we show that this simplifying assumption is valid as long as the IC50 is not the same order of magnitude as the initial dosage concentration of the infused bNAb. Notably, the data from therapy trials used in this study fall into the regime for which we can neglect the impact of incomplete neutralization (Appendix 3—figure 2). However, taking into account the dependence of viral fitness on bNAb concentration and its neutralization efficacy, as in the model proposed by Meijers et al., 2021, could improve the long-term predictive power of our approach.

Our predictions are limited by our ability to identify the escape variants for each bNAb, either based on the in vivo trial data and patient surveillance, or in-vitro assays such as DMS experiments. In Appendix 4, we compare the accuracy of our predictions for the rebound time distributions of HIV using DMS-inferred versus trial-inferred escape variants against the 10–1074 and the PGT121 bNAbs, and we find good agreements between the two approaches in both cases. However, it should be noted that identifying escape variants from DMS experiments lead to a more optimistic prediction for treatment success during the first 8 weeks of trials (i.e. they suggest a later rebound). One reason for this discrepancy may be related to the distinct genetic composition of viruses in the two approaches. DMS experiments characterize HIV escape by introducing mutations on a single genetic background (Dingens et al., 2019; Dingens et al., 2017; Schommers et al., 2020) (e.g. the HIV-1 strain BF520.W14M.C2 in Dingens et al., 2017), whereas clinical data contain diverse populations of viruses between and within individuals. It is more likely for diverse viral populations to contain variants in which positive epistasis between escape mutations and the background genome is present. Therefore, it is reasonable to expect that genetic data originating in clinical trials show more pathways of escape, resulting in a faster viral rebound following bNAb infusion. Nevertheless, DMS experiments are less costly for identifying escape variants compared to trials, and they provide a baseline to assess the efficacy of different bNAbs for therapy and further in-vivo investigations. More experiments would be necessary for a more systematic understanding of the limitations of each approach.

It should be noted that our analysis in Figure 4C only focuses on one aspect of therapy optimization, that is, the suppression of escape. Other factors, including potency (neutralization efficacy) and half-life of the bNAb, or the patient’s toleration to bNAbs at different dosages should also be taken into account for therapy design. For example, the bNAb 10E8, which we identified as of the most promising mono-therapy candidates in Figure 4C, is shown to be poorly tolerated by patients with short half-life (Kwon et al., 2016), making it undesirable for therapy purposes. Thus, the bNAb candidates shown in Figure 4C should be taken as a guideline to be complemented with further assessment of efficacy and safety for therapy design.

### Outlook

Our approach showcases that, when feasible, combining high-throughput genetic data with ecological and population genetics models can have surprisingly broad applicability, and their interpretability can shed light into the complex dynamics of pathogens subject to therapy. Application of similar methods to therapy design to curb the escape of cancer tumors against immune- or chemo-therapy, the resistance in bacteria against antibiotics, or the escape of seasonal influenza against vaccination is a promising avenue for future work. However, we expect that more sophisticated methods for inferring fitness from evolutionary trajectories may be necessary to capture the dynamical response of these populations.

## Methods

### Data and code accessibility

The code for the algorithms used in this work and the data are available on GitHub at https://github.com/StatPhysBio/HIVTreatmentOptimization (copy archived at swh:1:rev:0194cf6e554996a066633e99dd53cd5901da552e, Chelate, 2022a) and in the Julia package https://github.com/StatPhysBio/EscapeSimulator (copy archived at swh:1:rev:9a343f598820bafddfc7ea4547cefa90bf96fd6e, Chelate, 2022b).

### Description of molecular data

#### Data from bNAb trials

In this study, we considered four clinical trials for passive therapy with bNAbs:

All sequenced patients across all trials were infected with distinct HIV-1 clade B viral strains. We limited our analyses to those patients not on ART at the time of treatment initiation. In these studies, the injected bNAb level falls off over time within patients and therefore, we only considered dynamics within an 8-week window since infusion. This assures that rebound is not confounded by a drop in bNAb below sensitive-strain neutralizing levels of $IC_{50_{S}}<2\mug/m$.

We used single-genome sequence data of env collected from all patients in each trial to characterize the diversity of HIV-1 population within each patient shown in Figure 2 available from Zanini et al., 2015 and accessible through European Nucleotide Archive (Accession no: PRJEB9618). The patient sequence data for each trial is available through Caskey et al., 2015 GeneBank accession number: KX016803, Caskey et al., 2017 GenBank accession numbers KY323724.1 - KY324834.1, and Baron et al., 2018, GenBank accession numbers MH632763 - MH633255.

#### Longitudinal HIV-1 sequence data from untreated patients

Single nucleotide polymorphism (SNP) data was obtained from Zanini et al., 2015 and aligned to the HXB2 reference using HIV-align tool (Gaschen et al., 2001). The dataset includes 11 patients observed for 5–8 years of infection, with HIV-1 sequence data sampled over 6–12 time points per patient (Figure 2).

Patient 4 and patient 7 were excluded from the original analysis done in Zanini et al., 2015 because of suspected superinfection and failure to amplify early samples, respectively. These patients were included in our analysis, since (i) super-infection poses no additional difficulties for our tree-free procedure, and (ii) only time points with measurable viral diversity entered into our selection likelihood, which automatically limits our analysis to samples with high-quality sequences.

All patients were infected with clade B of HIV, except for patient 6 (clade C), and patient 1 (clade 01_AE). We assessed the robustness of our inference to exclusion of these patients from our analysis in Effect of genomic linkage on the inference of selection. Overall, our inference was not strongly affected by this choice (Model robustness Figure 4—figure supplement 1), and therefore, we included these patients in our main analyses to enhance the statistics with larger data.

For our analysis we considered only data reported in single nucleotide polymorphism (SNP) counts. The number of raw SNP counts are the result of amplification and must be converted into estimates for the number of pre-amplification template fragments. Zanini et. al. reported that on average about 102 templates of amplicon were associated with the fragments of the envelope (env) protein Zanini et al., 2015. We converted raw SNP counts into templates by normalizing to 120 counts and rounding the resulting number to the nearest integer.

### Identifying escape-mediating variants against bNAbs

The starting point for our analysis of HIV response to a given a bNAb is the description of the escape-mediating amino acids in the HIV env protein. We use a combination of methods to identify the escape variants for a given bNAb. First, we use deep mutational scanning (DMS) data of HIV-1 in the presence of a bNAb from Dingens et al., 2019 to identify these mutations. These DMS experiments have created libraries of all single mutations from a given genomic background of HIV-1 and tested the fitness of these variants (i.e. growth on T-cell culture) in the absence and presence of nine different bNAbs, including the 10–1074 and 3BNC117 Dingens et al., 2019.

Escape variants in DMS data are identified as those which are strongly selected for only in the presence of a bNAb. Specifically, we identify escape variants as those which show 3-logs-change in their frequency in the presence versus absence of a bNAb. DMS data reflects in vitro escape in cell culture. However, some of these variants may not be viable in vivo. To identify the reasonable candidates of escape in vivo, we limit our set to the variants that are also observed in the circulating viral strains of untreated HIV-1 patients from Zanini et al., 2015. It should be noted that since we use HIV-1 sequence data from Zanini et al., 2015 to infer selection on escape mediating variants in the absence of a bNAb, the candidates of escape that are not observed in the dataset Zanini et al., 2015 would be inferred to be strongly deleterious, and hence, unlikely to contribute to our predictions of viral rebound.

Our analysis of DMS data results in a set of escape mediating amino acids for 10–1074 that is consistent with the escape variants that emerge in response to the bNAb trial (Caskey et al., 2017; Stephenson et al., 2021 Appendix 4). However, the DMS data is very noisy for bNAbs that target CD4 binding site of HIV, that is, 3BNC117 and VRC01 (Dingens et al., 2019). One reason for this observation may be that the CD4 binding site is crucial for the entry of HIV to the host’s T-cells and mutations in this region are highly deleterious. As a results, only a small number of variants with mutations in this region can survive in the absence of a bNAb in a DMS experiment. Growth in the absence of a bNAb is the first step in the DMS experiments, which is then followed by exposure of the replicated variants to a bNAb. Therefore, a low multiplicity of variants in the absence of a bNAb could result in a noisy pattern of growth of the small subpopulation in the next stage of the experiment, in which growth is subject to a CD4-targeting bNAb.

For the CD4 binding site antibodies 3BNC117 and VRC01, we used additional data to call the escape variants. For 3BNC117, we used a combination of trial-patient sequences (Caskey et al., 2015; Scheid et al., 2016), that is post-treatment enrichment, along with contact site information compiled in the crystallographic studies to narrow down candidate sites (Zhou et al., 2015; LaBranche et al., 2018). For VRC01, we assumed a similar escape pattern to 3BNC117 but included sites known from other studies (Lynch et al., 2015) and the clear DMS signal at HXB2 site 197. The sites we called were similar to those identified using humanized-mouse models of HIV infection (Horwitz et al., 2013), although more complex mutational patterns were seen in the soft-randomization scanning of Otsuka et al., 2018. Although the complete list of escape substitutions are unknown and background-dependent (Otsuka et al., 2018), the escape profiles which are most important are those that are most likely to be seen consistently in data and to be correctly identified. The list of substitutions are shown in Appendix 1—table 1.

### Statistics and dynamics of viral rebound

#### Inference of growth parameters from dynamics of viremia

The concentration of viral RNA copies in blood serum is a delayed reflection of the total viral population size $N⁢(t)$, containing a resistant and susceptible subpopulations, with respective sizes $N_{r}⁢(t)$ and $N_{s}⁢(t)$. After infusion of bNAbs in a patient, the susceptible sub-population decays due to neutralization by bNAbs and the resistant sub-population grows and approaches the carrying capacity $N_{k}$, with the dynamics,

$$
\frac{dN_{r}}{dt}=\gammaN_{r}(1−N_{r}/N_{k})\frac{dN_{s}}{dt}=−rN_{s}
$$

Here, $\gamma$ is the growth rate of the resistant population, and $r$ is the neutralization rate impacting the susceptible subpopulation. By setting the initial condition for fraction of resistant subpopulation prior to treatment (at time $t=0$) $x=N_{r}⁢(0)/(N_{r}⁢(0)+N_{s}⁢(0))$, we can characterize the evolution of the total viremia in a patient. This dynamics is governed by the combined processes of neutralization by the infused bNAb and the viral rebound (Figure 1A), which entails,

$$
N(t)={N_{k}t\leq0(1−x)N_{k}e^{−rt}+\frac{N_{k}}{1+\frac{1−x}{x}e^{−\gammat}}t>0
$$

We use Equation 5 to define the evolution of blood concentration of viral RNA sequences which is observed indirectly via noisy viremia measurement data from Caskey et al., 2015; Caskey et al., 2017; Baron et al., 2018. To connect the data with the simple model of viral dynamics in Equation 5, we fit the initial frequency of resistant mutants $x$ for each patient separately, and fit a global estimate for the decay rate of susceptible variants $r$ shared across all patients in a trial, using a joint maximum-likelihood procedure. In addition, we fix the growth rate $\gamma$ to 1/3 days, corresponding to a doubling time of approximately 2 days García et al., 1999. Our analyses indicate that the initial viremia decline lagged treatment by about 1 day (Figure 3—figure supplements 1–3), consistent with previous findings (Ioannidis et al., 2000), and therefore, we included a 1 day lag between the fitted viremia response model and the treatment.

$t$ The number of viral RNA copies in a blood sample is subject to count fluctuations with respect to the true number of circulating virions in a given volume of the blood. We use a Poisson sampling model to define a likelihood for our model of viral population. The likelihood of observing viral counts in a sample collected from patient at time is given by a Poisson distribution,

$$
p⁢(k=n_{p}⁢(t)|η=N_{p}⁢(t))=e^{-η}⁢\frac{η^{k}}{k!}
$$

with rate parameter set by the model value of the viral multiplicity $N_{p}⁢(t)$ (Equation 5). We use the Poisson likelihood in Equation 6 to characterize an error model to fit the parameters of the viral dynamics in Equation 5. However, since the mean and variance of the Poisson distribution are related, combining data with different mean values $N_{p}⁢(t)$ at different times and from different patients can cause inconsistencies in evaluations of errors in our fits. To overcome this problem, we use a variance stabilizing transformation (McCullagh and Nelder, 2019) and define a change in variable $n^_{p}⁢(t)=\sqrt{n_{p}⁢(t)}$. This transformed variable has a constant variance, and in the limit of large-sample size, it is Gaussian distributed with a mean and variance given by, $n^_{p}(t)∼N(\sqrt{\lambda},1/4)$. The constant variance of the transformed variable enables us to combine data from all patients and time points, irrespective of the sample’s viral loads, and fit the model parameters $(r,x_{p})$ using (non-linear) least-squares fitting of the function

$$
R⁢(r,{x_{p}})=\sump: patients,t(\sqrt{N_{p}⁢(t|r,x_{p})}-\sqrt{n_{p}⁢(t)})^{2}
$$

Here, $N_{p}⁢(t|r,x_{p})$ is the model estimate of viremia in patient $p$ at time $t$ (Equation 5), given the pre-treatment fraction of resistant variants xp, and the decay rate $r$.

Note that the viremia measurements have a minimum sensitivity threshold of 20 RNA copies per ml. We treat the data points below the threshold of detection as missing data and if $n_{p}⁢(t)$ is below the threshold of detection we impute $n_{p}⁢(t)=min⁢(20,N_{t})$.

The fitted viremia curves for patients enrolled in the three bNAb trials under consideration are shown in Figure 3—figure supplements 1–3, and the respective decay rates $r$ for each experiment are,

$$
trial10-10743BNC117CombinationAvgfittedr(days^{−1})0.360.230.330.31
$$

#### Individual-based model for viral population dynamics

To encode for different viral variants, we specify a coarse-grained phenotypic model, where a viral strain of type $a$ is defined by a binary state vector $ρ→^{a}=[ρ_{1}^{a},…,ρ_{ℓ}^{a}]$, with $ℓ$ entries for potentially escape-mediating epitope sites; the binary entry of the state vector at the epitope site $i$ represents the presence ($ρ_{i}^{a}=1$) or absence ($ρ_{i}^{a}=0$) of a escape mediating mutation against a specified bNAb at site $i$ of variant $a$. We assume that a variant is resistant to a given antibody if at least one of the entries of its corresponding state vector is non-zero.

We define an individual-based stochastic birth-death model (Wilkinson, 2019) to capture the competitive dynamics of different HIV variants within a population. This dynamic model will allow us to predict the distribution of rebound times under any combination of antibodies.

We assume that a viral strain of type $a$ can undergo one of three processes: birth, death and mutation to another type $b$ with rates $\beta_{a}$, $\delta_{a}$, and $\mu_{a→b}$, respectively:

$$
birth:[a]⟶\beta_{a}2[a]death:[a]⟶\delta_{a}∗mutation:[a]⟶\mu_{a→b}[b]
$$

We specify an intrinsic fitness fa for a given variant a, defined as the growth rate of the virus in the absence of neutralizing antibody or competition. Since bNAbs target highly vulnerable regions of the virus, we expect that HIV-1 escape mutations to be in trinsically deleterious for the virus and to confer a fitness cost relative to the susceptible viral variants prior to the infusion of bNAbs. Assuming that fitness cost of escape is additive across sites and background-independent, we can express the fitness of a variant as , where Δ is the cost associated with the presence of an escape mutation at site of variant (i.e., for = 1).

We assume that growth is self-limiting via a competition for host T-cells. This competition enforces a carrying capacity, which sets the steady-state population size $N_{k}$. Competition is mediated through a competitive pressure term $ϕ=\frac{\sum_{a}N_{a}⁢f_{a}}{N_{K}}$ which attenuates the net growth rate $\gamma_{a}$ so that $\gamma_{a}=f_{a}-ϕ$. At the carrying capacity, the competitive pressure equals the mean population fitness $ϕ=f¯$, making the net growth rate of the population zero.

The net growth rate of a variant $a$ is given by its birth rate minus the death rate: $\gamma_{a}=\beta_{a}-\delta_{a}$. We assume that the total rate of events (i.e. the sum of birth and death events) is equal for all types, that is, $\lambda=\beta_{a}+\delta_{a},∀a$. Assuming that $\lambda$ is constant is to be agnostic about the mechanism of a fitness decrease, attributing fitness loss equally to (i) an increase in the death rate and (ii) a decrease in the birth rate.

Because the absolute magnitude of $\beta$ and $\delta$ asymptotically converge in the continuum limit for a surviving population, that is, $lim_{N→∞}⁡\beta/\delta=1$, it is impossible to distinguish between (i) and (ii) in the continuous limit. Choosing constant $\lambda$ simplifies both theoretical calculations and the simulation algorithm.

This leads to the following equations for the birth and the death rates:

$$
\beta_{i}=\frac{\lambda+(f_{i}−ϕ)}{2}\delta_{i}=\frac{\lambda−(f_{i}−ϕ)}{2}
$$

In the presence of an antibody, birth is effectively halted for susceptible variants, resulting in birth and death rate for a susceptible variant $s$,

$$
\beta_{s}=0\delta_{s}=r
$$

so that the susceptible phenotype decays at rate $r$.

We assume that mutations occur independently at each site,

$$
\mu_{a→b}={\mu_{i}if ⁢ρ^{a}-ρ^{b}=1_{i}\mu_{i}^{†}if ⁢ρ^{a}-ρ^{a}=-1_{s}0otherwise
$$

where $1_{s}$ is the vector which has only one non-zero entry at site $i$, and $\mu_{i}$ and $\mu_{i}^{†}$ are the forward the backward mutation rates at site $i$, respectively. We characterize the state of a population by vector $n=(n_{1},…n_{M})$, where na is the number of type $a$ variants within the population. We approximate the evolution of the population state distribution using a Fokker-Planck equation (see Appendix 2).

Of special interest for our analysis is the steady-state density of frequencies, which we use to describe the initial state of the population (before treatment) and to infer selection intensity. In the steady state, the population is fluctuating around carrying capacity $\sum_{a}n_{a}≈N_{k}$ and we can represent the population state via allele frequencies $x_{a}=n_{a}/N_{k}$. In the simple case of a bi-allelic problem, the equilibrium allele frequency distribution $P_{eq}⁢(x)$ follows the Wright-equilibrium distribution (Crow and Kimura, 2010) with modified rates,

$$
P_{eq}⁢(x)=\frac{1}{Z}⁢\frac{e^{\frac{2⁢N_{k}}{\lambda}⁢(f_{1}-f_{0})⁢x}⁢(1-x)^{\frac{2⁢N_{k}}{\lambda}⁢\mu^{†}}⁢x^{\frac{2⁢N_{k}}{\lambda}⁢\mu}}{(1-x)⁢x}≡\frac{1}{Z⁢(\sigma,\theta,\theta^{†})}⁢\frac{e^{-\sigma⁢x}⁢(1-x)^{\theta^{†}}⁢x^{\theta}}{(1-x)⁢x}
$$

where $Z$ is the normalization factor, f1 is the intrinsic fitness of the variant of interest, f0 is the fitness of the competing variant, $\mu$ and $\mu^{†}$ are the forward and backward mutation rates, $N_{k}$ is the carrying capacity, and $\lambda$ is the total rate of events in the birth-death process, which sets a characteristic time scale over which the impact of selection and mutations can be measured. In this case, we can define an ‘effective population size’ that sets the effective size of a bottleneck and the natural time scale of evolution as $N_{e}=N_{k}/\lambda$, and specify a scaled selection factor $\sigma=N_{e}⁢s=N_{e}⁢(f_{0}-f_{1})$, and scaled forward mutation and backward mutation rates (diversity) $\theta=2⁢N_{e}⁢\mu$, and $\theta^{†}=2⁢N_{e}⁢\mu^{†}$. The normalization factor is given by,

$$
Z≡Z⁢(\sigma,\theta,\theta^{†})=ℬ⁢(\theta,\theta^{†})_{1}⁢F_{1}⁢(\theta,\theta+\theta^{†},-\sigma)
$$

where $F11⁢(⋅)$ denotes a Kummer confluent hypergeometric function and $ℬ⁢(\theta,\theta^{†})=\frac{Γ⁢[\theta]⁢Γ⁢[\theta^{†}]}{Γ⁢[\theta+\theta^{†}]}$ is the Euler beta function.

#### Extinction Probability

The logistic dynamics describing a patient’s viremia over time in Equation 5 is the deterministic approximation to the underlying birth-death process. However, the resistant population can also go extinct due stochastic effects, which in turn contribute to the probability of late rebound in a population. To capture this effect, we derive an approximate closed form expression for the probability of extinction.

Using the standard birth-death process generating function theory Allen, 2010 the probability $P⁢(extinct|n_{i})$ that a population consisting of ni resistant variants of type $i$ go extinct can be expressed as,

$$
P⁢(extinct|n_{i})=(\frac{\delta_{i}}{\beta_{i}})^{n_{i}}.
$$

To characterize the probability of extinction for a population of size $N_{k}$ with pre-treatment fraction of $i^{t⁢h}$ resistant variants xi, we can convolve the extinction probability in Equation 14 with a Binomial probability density for sampling ni resistant variants from $N_{k}$ trials. Given that the pre-treatment fraction of resistant variants is small $x_{i}≪1$ and $N_{k}$ is large, this Binomial distribution can be well approximated by a Poisson distribution, $Poiss⁢(n_{i};N_{k}⁢x_{i})$ with rate $N_{k}⁢x_{i}$, resulting in an extinction probability,

$$
P⁢(extinct|x_{i})=\sum_{n_{i}}Poiss⁢(n_{i};N_{k}⁢x_{i})⁢(\frac{\delta_{i}}{\beta_{i}})^{n_{i}}=exp⁡(-N_{k}⁢x_{i})⁢\sum_{n_{i}}\frac{(N_{k}⁢x_{i})^{n_{i}}}{n_{i}!}⁢(\frac{\delta_{i}}{\beta_{i}})^{n_{i}}=exp⁡(-N_{k}⁢\frac{\beta_{i}-\delta_{i}}{\beta_{i}}⁢x_{i})
$$

Using the expressions for the growth in the absence of competition, $\beta_{i}-\delta_{i}=\gamma_{i}=f_{i}$ (since $ϕ=0$), and assuming that fitness is small relative to the total rate of birth and death events $f_{i}≪\lambda$, we can use the approximation $\beta_{i}=(\lambda+f_{i})/2≈\lambda/2$, to arrive at,

$$
P⁢(extinct|x_{i})≈exp⁡(\frac{-2⁢N_{k}⁢f_{i}}{\lambda}⁢x_{i})=exp⁡(-\frac{x_{i}}{x_{ext}})
$$

$x_{ext}$ where the characteristic escape threshold can be written in terms of concrete genetic observables,

$$
x_{ext}≡\frac{\lambda}{2⁢N_{k}⁢f_{i}}=\frac{\mu_{ts}}{f_{i}}⁢\theta_{ts}^{-1}.
$$

Figure 3 shows that this threshold can well separate the fate of stochastic evolutionary trajectories, simulated with relevant parameters for intra-patient HIV evolution.

#### Numerical simulations of the birth-death process

To treat the full viral dynamics including mutations, and transient competition effects, we can exactly simulate the viral dynamics defined by our individual based model. Below are the key steps in this simulation.

##### Population initialization

At the starting point, we set the population size (i.e. the carrying capacity in the simulations) $N_{k}$ as a free parameter chosen to be large enough to make discretization effects small. The population is then evolved through time using an exact stochastic sampling procedure (the Gillespie algorithm Gillespie (1977)). Simulating the outcome of this stochastic evolution generates the distribution of rebound times and the probability of late rebound—the key quantities related to treatment efficacy.

The input to our procedure is a list of antibodies for which we specify (i) the escape mediating sites for each antibody, and the (invariant) quantities describing (ii) the site-specific cost of escape $\frac{\sigma}{\theta_{ts}}$, and (iii) the forward and backward mutation rates $(\frac{\theta}{\theta_{ts}},\frac{\theta^{†}}{\theta_{ts}})$. To simulate the trial outcome for each patient, we use the neutral population diversity $\theta_{ts}$ directly inferred from the patients; see Inference of mutation rates and the neutral diversity within a population. From this, we construct the list of $L$ site parameters (concatenated across all antibodies) for selection and diversity: $\sigma_{1:L}$, $\theta_{1:L}$, $\theta_{1:L}^{†}$.

We assume that at the start of the simulation, populations are in the steady state and that the potential escape sites are at linkage equilibrium. The approximate linkage equilibrium assumption is justified since the distance between these escape sites along the HIV-1 genome is greater than the characteristic recombination length scale $≈100⁢bp$ of the virus (Zanini et al., 2015). As a result, we draw an independent frequency xi from the stationary distribution $P_{eq}⁢(x|\sigma_{i},\theta_{i},\theta_{i}^{†})$ in Equation 12 to describe the state of a give site $i$, and use these frequencies to construct the initial viral genotypes $ρ^{v}$ for each virus $v$ in our initial population; see Algorithm 1 (Appendix 5). In simulations, we show that this assumption does not bias our results even when $\theta_{ts}$ is fluctuating and recombination is absent (Section 6.1 and Figure 4—figure supplement 2).

To sample from the stationary distribution itself, we define a novel Gibbs-sampling procedure (Geman and Geman, 1984) for generating the allele frequencies of the escape variants for the initial state of the population $x∼P_{eq}⁢(x|\sigma,\theta,\theta^{†})$ (Equation 12). To characterize this procedure, we expand the exponential selection factor $e^{\sigma⁢(1-x)}$ in the original distribution, which results in,

$$
P_{eq}⁢(x|\sigma,\theta,\theta^{†})=\frac{e^{-\sigma}}{Z⁢(\sigma,\theta,\theta^{†})}⁢e^{\sigma⁢(1-x)}⁢\frac{x^{\theta}⁢(1-x)^{\theta^{†}}}{x⁢(1-x)}=\sum_{k=0}^{∞}\frac{e^{-\sigma}}{Z⁢(\sigma,\theta,\theta^{†})}⁢\frac{\sigma^{k}}{k!}⁢x^{\theta}⁢\frac{(1-x)^{\theta^{†}+k}}{x⁢(1-x)}≡\sum_{k=0}^{∞}Q_{eq}⁢(x,k|\sigma,\theta,\theta^{†})
$$

Here, $Q_{eq}⁢(x,k|\sigma,\theta,\theta^{†})$ is a joint distribution over $(x,k)$, and the desired distribution over the allele frequency $x$ can be achieved by marginalizing the joint distribution over the discrete variable $k$. We can also express the conditional distributions for $x$ and $k$ as,

$$
Q_{eq}⁢(x|k,\sigma,\theta,\theta^{†})=\frac{Q_{eq}⁢(x,k|\sigma,\theta,\theta^{†})}{\intd⁢x⁢Q_{eq}⁢(x,k|\sigma,\theta,\theta^{†})}=Beta⁢(x;\theta,\theta^{†}+k)
$$



$$
Q_{eq}⁢(k|x,\sigma,\theta,\theta^{†})=\frac{Q_{eq}⁢(x,k|\sigma,\theta,\theta^{†})}{\sum_{k}Q_{eq}⁢(x,k|\sigma,\theta,\theta^{†})}=Poisson⁢(k;(1-x)⁢\sigma)
$$

We use these conditional distributions to define a joint Gibbs sampler for $Q_{eq}$. We summarize the resulting $(x,k)∼Q_{eq}⁢(x,k|\sigma,\theta,\theta^{†})$ in the joint Gibbs sampler in Algorithm 2 (Appendix 5). This chain mixes extremely quickly and avoids calculation of the hypergeometric function for the normalization factor (Equation 20), which is computationally costly; see Algorithm 2 (Appendix 5).

##### Simulation of the evolutionary process

We use a Gillespie algorithm to simulate the evolutionary process, where we break up the reaction calculation into two parts: randomly choosing a viral strain $ρ_{i}$ from the population and then determining whether it reproduces or dies based on its fitness fi and escape status; see Algorithm 3 (Appendix 5).

### Determining the simulation parameters of the birth-death process from genetic data

We set the intrinsic growth rate (fitness) of the wild-type virus, in the absence of competition to be $\gamma=(3⁢ days)^{-1}$, consistent with intra-patient doubling time of the virus (García et al., 2001; Ioannidis et al., 2000; García et al., 1999). We infer the neutralization rate $r$ by fitting the viremia curves (Figure 3) in the trials under study, and use the averaged decay rate $r=0.31$ for simulations, fitted using Equation 8. For the absolute mutation rate $\mu_{ts}$ (per nucleotide per day), we use $1.1\times10^{-5}$ which is the average of the reported values for transitions per site per day from Zanini et al., 2017. Using the covariance of neutral diversity in twofold and four-fold synonymous sites, we determine the transition/transversion diversity ratio to be $\theta_{ts}/\theta_{tv}=7.8$ (Figure 2—figure supplement 1). We use these values to determine the forward and backward mutation rates $\mu_{s}$ and $\mu_{s}^{†}$ for each site (see Inference of mutational target size for each bNAb).

Generally, the trial patients show viral populations with larger neutral diversity at the start of the trial compared to the patients enrolled in the high-throughput study of Zanini et al., 2015 (Figure 2). We account for differences in the genetic makeup of the patients enrolled in the trial by directly estimating the neutral diversity $\theta_{ts}$ from the synonomous site-frequency data of patients, before the start of the trial. The estimated viral diversity $\theta_{ts}$, coupled with the mutation rate $\mu=1.1\times10^{-5}⁢ /day / nt$, and the total rate of birth and death events in the viral population $\lambda$, set the carrying capacity $N_{k}$ for a given individual,

$$
N_{k}=\frac{\lambda}{2⁢\mu_{ts}}⁢\theta_{ts}.
$$

It should be noted that the value of $N_{k}$, as the number of viruses in our individual-based simulations, is not related to the maximal viral load in the viremia measurements (i.e. steady state copy number per ml) as this relationship depends on the microscopic details of the population dynamics.

The total rate of birth and death events $\lambda=\beta+\delta$ tunes the amount of stochasticity, that is, more events cause noisier dynamics. Notably, stochasticity can be linked to the size of the population $N_{k}$, which is directly coupled to $\lambda$ (Equation 21). We set the value of $\lambda$ self-consistently by requiring the minimum frequency of a variant in our simulations $x_{min}=1/N_{k}=\frac{2⁢\mu_{ts}}{\lambda}⁢\theta_{ts}^{-1}$ to be smaller than the escape threshold $x_{ext}=\frac{\mu_{ts}}{\gamma}⁢\theta_{ts}^{-1}$ due to stochasticity (Equation 17). We set $\lambda=2⁢day^{-1}$ so that $x_{min}=\frac{1}{3}⁢x_{ext}$. Increasing $\lambda$ results in an increase in the size of population $N_{k}$ in our simulations, which is computationally costly, without qualitatively changing the statistics of the rebound trajectories.

### Inference of mutation rates and the neutral diversity within a population

Previous work has indicated an order of magnitude difference between the rate of transitions (mutations within a nucleotide class) and transversions (out-class mutations) in HIV (Nielsen, 2006; Zanini et al., 2017; Theys et al., 2018; Feder et al., 2017). Therefore, to infer the neutral diversity parameter $\theta_{ts}$, we also account for the differences between transition and transversion rates.

Consider the set of sequences sampled from a patient’s viral population at a particular time. Two neutral alleles that are linked by a symmetric mutational process $\mu_{1→2}=\mu_{2→1}$ have a simple count likelihood. The probability to see allele 1 with multiplicity $n$ and allele 2 with multiplicity $m$ is given by a binomial distribution $Binom⁢(n,m|x)$ with parameter $x$ denoting the probability for occurrence of allele 1, convolved with the neutral biallelic frequency distribution $P_{eq}⁢(x|\sigma=0,\theta)$ from Equation 12. Using this probability distribution, we can evaluate the log-likelihood $ℒ⁢(\theta|n,m)$ for the neutral diversity $\theta$ given the observations $(n,m)$ for the multiplicities of the two alleles in the population,

$$
ℒ⁢(\theta|n,m)=log⁢\intd⁢x⁢Binom⁢(n,m|x)\timesP_{eq}⁢(x|\sigma=0,\theta)=log⁢\intd⁢x⁢(\frac{n+m}{n})⁢x^{n}⁢(1-x)^{m}\times\frac{x^{\theta-1}⁢(1-x)^{\theta-1}}{Z⁢(\theta)}
$$

### Inference of netral diversity, mutational target size, and selection from genetic data

To estimate the transition diversity, we only use twofold synonymous sites, and treat each site independently but with a shared diversity parameter $\theta_{ts}$. For example, consider neutral variations for two amino acids glutamine and phenylalanine. The third position in a codon for both of these amino acids are twofold synonymous, as the two possible codons for glutamine are CAG and CAA, and for phenylalanine are TTT, and TTC. Now consider that in the data a conserved glutamine has $n=3$ G’s and $m=97$ A’s in the third codon position, and a conserved phenylalanine has $n=10$ T’s and $m=90$ C’s at its third codon position. In this case, the combined log-likelihood for the shared diversity parameter is $ℒ⁢(\theta|data)=ℒ⁢(\theta|3,97)+ℒ⁢(\theta|10,90)$. Extending to all of sites in the env protein, the maximum-likelihood estimator for the transition diversity $\theta_{ts}$ can be evaluated by maximizing the likelihood summed over all conserved twofold synonymous sites,

$$
\theta_{ts}^{∗}=arg⁡max\theta_{ts}\sumtwo-fold sitesL(\theta_{ts}|n=n_{A}+n_{T};m=n_{G}+n_{C})
$$

In Figure 2—figure supplement 1 (panel A), we show that the maximum likelihood estimation method described above has better properties than the more commonly used estimator of the variance $x(1−x)¯$ Stoddart and Taylor, 1988.

In a similar way, the likelihood for the transversion $\theta_{tv}$ is determined from polymorphic data at all conserved four-fold synonymous sites. One such example is the third position in a glycine codon, where (GGT, GGC, GGA, GGG) translate to the same amino acid. The maximum-likelihood estimator for the transversions is

$$
\theta_{tv}^{∗}=arg⁡max\theta_{tv}\sumfour-fold sitesL(2\theta_{tv}|n=n_{G}+n_{T};m=n_{C}+n_{A})
$$

The factor of 2 in the argument of the likelihood accounts for the multiplicity of mutational pathways, e.g. from a $G$ nucleotide there are two transversion possibilities, $G→C$ and $G→A$ for moving from one allele to the other Kimura, 1981.

Using this likelihood approach, we can infer the neutral diversities $\theta_{ts}^{*}$ and $\theta_{tv}^{*}$ for each patient at each time point from the polymorphism in twofold and fourfold synonymous sites. To characterize the ratio of transition to transversion rates, we use linear regression on the entire patient population and sample history and infer a constant ratio $\mu_{ts}/\mu_{tv}=\theta_{ts}/\theta_{tv}=7.8$ (Figure 2—figure supplement 1B). In Figure 2—figure supplement 1, we also show that the estimate for this ratio is relatively consistent across different data sources, produced even by different sequencing technologies. The previously reported relative rate of transitions to transversions, based on the estimates of sequence divergence along phylogenetic trees of HIV-1 is $\mu_{ts}/\mu_{tv}=5.6$ (Zanini et al., 2017), which is similar to our maximum likelihood estimate.

#### Inference of mutational target size for each bNAb

The nucleotide triplets which encode for amino acids at an escape site undergo substitutions which can change the amino acid type and create an escape variant. The changes in the state of an amino acid codon can be modeled as a Markov jump process and can be visualized as a weighted graph where the nodes represent codon states, and edges represent single nucleotide substitutions linking two codon states (Figure 1D). In our mutational model, these edges have weights associated with either the mutation rates for transitions $\mu_{ts}$ or transversions $\mu_{tv}$. We call this the codon substitution graph.

The codon states can be clustered into three distinct classes: (i) codons which are fatal $F$, (ii) wild-type (i.e. susceptible to neutralization by the bNAb) $W$, and escape mutants (i.e. resistant to the bNAb) $M$. We expect the escape mutants to be at a selective disadvantage compared to the resistant wild-type, and that the most common escape codons to be those which are adjacent to wild-type states.

The mutational target size is determined by the density of paths from the wild-type $W$ to the escape mutants $M$.

$$
\mu=\frac{1}{|W|}\sumc\inW;d\inM[c−d=ts]\mu_{ts}+[c−d=tv]\mu_{tv}
$$



$$
\mu^{†}=\frac{1}{|M|}\sumc\inW;d\inM[c−d=ts]\mu_{ts}+[c−d=tv]\mu_{tv}
$$

The functions $[c-d=ts]$ or $[c-d=tv]$ are 1 when the two codons are separated by a transition or transversion, and are zero otherwise. Note that since we only have an estimate for the ratio of the transition to transversion rates $\mu_{tv}/\mu_{ts}$, we can only determine the scaled mutational target sizes, $\mu^=\mu/\mu_{ts}$ and $\mu^^{†}=\mu^{†}/\mu_{ts}$, which are sufficient for inference of selection in the next section. The full list of mutational target sizes inferred for the bNAbs in this study are shown in Appendix 1—table 1.

When discussing the mutational target size of escape from a given bNAb, we refer to the total mutation rate from the susceptible (wild type) to the escape variant as,

$$
\mu=\sumi\in esc. sites\mu_{s→i}
$$

where the sum runs over all the mediating escape sites $i$, and can be interpreted as the average number of accessible escape variants. In the strong selection regime, we can write the frequency of escape mutants as,

$$
x_{mut}≈\sumix_{i}=\sumi\frac{\mu_{s→i}}{Δ_{i}}≈\frac{\mu}{Δ_{hm}}
$$

#### Inference of selection for escape mutations against each bNAb

Here, we develop an approximate likelihood approach to infer the selection ratio $\sigma^=\frac{\sigma}{\theta_{ts}}$, using the high-throughput sequence data from bNAb-naive HIV-1 patients from Zanini et al., 2017. The quantity $\sigma^$ is a dimensionless ratio which is independent of the coalescence timescale $N_{e}$, and therefore, represents a stable target for inference.

We assume that the probability to sample $m$ escape mutants and $s$ susceptible (wild-type) alleles at a given site in the genome of HIV in a population sampled from a patient at a given time point follows a binomial distribution $Binom⁢(m,s|x)$, governed by the underlying frequency $x$ of the mutant allele. In addition, the frequency $x$ of the allele of interest itself is drawn from the equilibrium distribution $P_{eq}⁢(x|\sigma,\theta,\theta^{†})$ (Equation 12), governed by the diversity $\theta_{ts}$ inferred from the neutral sites, the estimated mutational target sizes $\mu^=\mu/\mu_{ts},\mu^^{†}=\mu^{†}/\mu_{ts}$, and the unknown selection ratio $\sigma^=\sigma/\theta_{ts}$. As a result, we can characterize the probability $P⁢(m,s|\theta_{ts},\mu^,\mu^^{†},\sigma^)$ to sample $m$ escape mutants and $s$ susceptible-type alleles, given the scaled selection and diversity parameters as,

$$
P(m,s|\theta_{ts},\sigma^)=P(m,s|\sigma=\sigma^\theta_{ts},\theta=\mu^\theta_{ts},\theta^{†}=\mu^^{†}\theta_{ts})=\intdxBinom(m,s|x)P_{eq}(x|\sigma,\theta,\theta^{†})=\frac{1}{Z(\sigma,\theta,\theta^{†})}(\frac{s+m}{s})\intdx\frac{e^{−\sigmax}x^{\theta+m}(1−x)^{\theta^{†}+s}}{x(1−x)}
$$

Here, $Z⁢(\sigma,\theta,\theta^{†})$ is a confluent hypergeometric function of the model parameters that sets the normalization factor for the allele frequency distribution $P_{eq}⁢(x)$ (Equation 13). It should be noted that the viral population is in fact out of equilibrium, due to constant changes in immune pressure evolution from the B-cell and T-cell populations (Nourmohammad et al., 2016). Although we are ignoring these significant complications, we later use the same equilibrium distribution in a consistent way to generate standing variation in simulations. For the model to make accurate predictions, it is not necessary that the equilibrium model be exactly correct, but only that it is rich enough to provide a consistent description for the distribution of mutant frequencies observed across viral populations.

We will use the probability density in Equation 29 to define a log-likelihood function in order to infer the scaled selection $\sigma^=\sigma/\theta_{ts}$ from data. To do so, we first express the logarithm of this probability density as,

$$
log⁡P(m,s|\theta_{ts},\sigma^)=log⁡P(m,s|\sigma=\sigma^\theta_{ts},\theta=\mu^\theta_{ts},\theta^{†}=\mu^^{†}\theta_{ts})=log⁡Z(\sigma,\theta+m,\theta^{†}+s)−log⁡Z(\sigma,\theta,\theta^{†})+const.=log⁡E[e^{−\sigmax}]_{Beta(\theta+m,\theta^{†}+s)}−log⁡E[e^{−\sigmax}]_{Beta(\theta,\theta^{†})}+const.
$$

where the constant factors (const.) are independent of selection, and $E[⋅]_{Beta(⋅)}$ denotes the expectation of the argument over a Beta distribution with parameters specified in the subscript. The expression in Equation 30 implies that we can evaluate the likelihood of selection strength by computing the difference between the logarithms of the expectation for $e^{-\sigma⁢x}$ over allele frequencies drawn from two neutral distributions (Beta distributions), with parameters $(\theta,\theta^{†})$ and $(\theta+m,\theta^{†}+s)$, respectively. This approach is more attractive as it would not require direct evaluation of the confluent hypergeometric functions for the normalization factors in Equation 29. Estimating these normalization factors is computationally intensive for large values of $\sigma$, since many terms in the underlying hypergeometric series should be taken into account to stably compute them. However, evaluating the expectations via sampling from these two neutral distributions has the disadvantage that it is subject to variations across simulations. We reduce the variance of our estimate of $log⁡P⁢(m,s|\sigma,\theta,\theta^{†})$ in Equation 30 by using a mixture-importance sampling scheme (Owen and Zhou, 2000) with the details shown in Algorithm 4 (Appendix 5).

We use data collected across all time points and from all patients to infer reliable estimates for selection strengths. However, allele frequencies are correlated across time points within patients (Figure 2B), and thus, sequential measurements are not independent data points. Our estimates indicate a coalescence time of about $N_{e}∼10^{3}$ days based on the estimates for the mutation rate $\mu_{ts}=10^{-5}$ /nt/day, and the neutral diversity $\theta_{ts}=2⁢N_{e}⁢\mu_{ts}=0.01$. This coalescence time is much longer that the typical separation between sampled time points within a patient ($∼10^{2}$ days), suggesting that sequential samples collected from each individual in this data are correlated. Therefore, we treat each patient as effectively a single observation, using the time-averaged likelihood for the (scaled) selection factor $\sigma^$:

$$
L(\sigma^)=\sump\frac{1}{T_{p}}\sumtlog⁡P(m_{t},s_{t}|\theta_{ts}(t),\sigma^)
$$

where $p$ and $t$ denote patient identity and sampled time points, respectively, and $T_{p}$ is the total number of time points sampled in patient $p$. We use the likelihood in Equation 31 to generate samples from the posterior distribution for selection strengths under a flat prior, with a standard Metropolis-Hastings algorithm Hastings, 1970. Since the prior is constant, this procedure amounts to simply accepting or rejecting samples based on the likelihood ratio of Equation 31. We used the centered-normal distribution with standard deviation of 50 ($\times\mu_{ts}$ in absolute units) as the proposal density for the jumps in the Markov chain.

Prior work has also inferred the fitness effect of mutations in HIV, but our approach differs in important aspects. For instance, maximum entropy models have been used to infer the preference of different amino acids in the Gag and the env proteins of HIV-1 from their prevalences across sequences sampled from different patients( Louie et al., 2018; Ferguson et al., 2013). The inferred preference values can explain the in-vitro growth rate (fitness) of the associated viral strains, especially for sites that are relatively conserved and are not the drivers of antigenic evolution in HIV-1. However, further modeling would be needed to quantitively map these inferred amino acid preferences onto population genetics measures that can be used to characterize the evolutionary dynamics of an HIV population. Other work has used longitudinal HIV-1 sequence data to infer selection and to characterize the role of selective sweeps due to immune pressure, genetic hitchhiking and recombination in the turnover of HIV-1 populations within patients (Zanini et al., 2017; Neher and Leitner, 2010; Illingworth et al., 2020; Haddox et al., 2018). In contrast, our work focuses on the expected composition of the population in a viremic patient prior to the start of treatment as opposed to the history of a viral population. Our approach uses a self-consistent formalism for inference of the population genetics parameters (e.g. population diversity and selection strength) and for the evolutionary simulations used to predict outcomes. Therefore, we can directly interpret the fitted parameters in terms of both the viral dynamics and the pre-treatment state of HIV-1 populations within patients.

### Predicting trial outcomes from genetically informed evolutionary models

#### Predicting rebound times

We expect different distributions of patient outcomes depending on whether they have been recently infected and thus have relatively low viral diversity, or whether their infection is longstanding with a diverse viral population. To construct the distribution of initial population diversities $\theta_{ts}$ for simulating trial outcomes, we apply the $\theta_{ts}$ inference procedure (Equation 22) to pre-treatment sequence datasets available from the clinical trials under consideration. In Figure 2D this set of pre-trial $\theta_{ts}$ is compared to the longitudinal in-patient $\theta_{ts}$ from Zanini et al., 2017. We used random draws from the inferred $\theta_{ts}$ values for patients to generate $\theta_{ts}$ for simulations.

We found that there was considerably more viral escape and non-responders in our simulations than in the observed data as shown in Figure 4—figure supplement 3A. This is in addition to the fact that the patients were screened to have only susceptible variants to the antibodies used in trials (Caskey et al., 2015; Caskey et al., 2017; Baron et al., 2018). In theory, there should be zero non-responders, as such patients should have been excluded by screening. The over-prediction of both non-responders and late rebounds is a signature of undercounting the effective diversity of the viral populations.

The failure of both screening and our naive prediction in undercounting the diversity in the viral population can be explained by an effective viral reservoir. Viral variants which mediate rebound can come from compartments such as including bone marrow, lymph nodes, and organ tissues, and can be genetically distinct from those sample from the plasma T-cells during screening (Chaillon et al., 2020; Wong and Yukl, 2016; Chun et al., 2005). This reservoir of viral diversity can reappear in plasma after infusion of a bNAb and could in part contribute to treatment failure (Avettand-Fenoel et al., 2007; Shan and Siliciano, 2013; Sharkey et al., 2011; Tagarro et al., 2018).

#### Determining patient diversity enhancement due to latent reservoirs

We model the effect of reservoirs as a simple inflation of the diversity observed by a multiplicative factor $ξ$. We fit $ξ$ directly to trial observations, using a disparity-based approach by minimizing an empirical divergence estimator Ekström, 2008 between the observed and simulated data. To do so, we characterize the Hellinger distance Lindsay, 1994; Simpson, 1987 between the true distribution of rebound times $P⁢(t)$ and the rebound times $Q⁢(t|ξ)$ generated by simulations with a given reservoir factor $ξ$,

$$
D_{H}(P(t)||Q(t|ξ))=\intdt(Q(t|ξ)^{\frac{1}{2}}−P(t)^{\frac{1}{2}})^{2}≈\sum(i)n_{q}(Q_{(i)}(ξ)^{\frac{1}{2}}−P_{(i)}^{\frac{1}{2}})^{2}
$$

Algorithm 5 (Appendix 5) defines the procedure that we use to estimate the Hellinger distance DH(Q(t)||P(t|ξ)). Specifically, we use nq quantiles of the observed data x(i) ~ Q to partition the space of observations into discrete outcomes

$$
Q_{(i)}(ξ)=\intdtP(t|ξ)[t_{(i)}\leqt<t_{(i+1)}]P_{(i)}=\frac{1}{n_{q}}.
$$

where $P_{(i)}$ is a constant by construction, and $P_{(i)}⁢(ξ)$ is estimated by simulations, and $[⋅]$ is the Iverson bracket Graham et al., 1989; see Algorithm 5 (Appendix 5).

$$
[B]={1 if B=true0 if B=false
$$

To simulate data for this analysis, we generate $S$ rebound times ($T_{1:S}$) by simulations, given the scaled diversity values $ξ⁢\theta_{ts}$. We then find the optimal value $ξ^{*}$ by minimizing the disparity with the observed rebound times $t_{1:p}$ by brute-force search,

$$
R(ξ|t_{1:p})=\sumtrialsReboundDisparity(t_{1:p},T_{1:S}|ξ)
$$



$$
ξ^{∗}=arg⁡minξR(ξ|t_{1:p})
$$

Here, ReboundDisparity is the function defined by Algorithm 5 (Appendix 5); see Ekström, 2008 for details. We find the optimal reservoir factor to be $ξ^{*}=2.1$, which we use in subsequent therapy prediction. The disparity over various values of $ξ$ for different trials is shown in Figure 4—figure supplement 3.

#### Simulating outcomes of clinal trials

Given the reservoir-corrected estimate of the diversity $ξ⁢\theta$ and the posterior samples for selection factors $\sigma^$, we now summarize how we simulated the outcome of clinical trials.

For a given bNAb, we draw the selection factor at each of the escape mediating sites from the corresponding Bayesian posterior on $\sigma^$; the posterior distributions are shown in Figure 4A, and summarized in Appendix 1—table 1. We also use the mutational target size (forward $\mu$ and backward $\mu^{†}$ rates) associated with each of the escape mediating sites of a given bNAb; see Appendix 1—table 1. The result can be summarized in a mutation / selection matrix $M^_{a}$ for a given bNAb $a$, where each column corresponds to an escape mediating site $i$ against the bNAb,

$$
M^_{a}=(\mu^_{1}…\mu^_{i}\mu^_{1}^{†}…\mu^_{i}^{†}\sigma^_{1}…\sigma^_{i})
$$

The elements of the matrix $M^_{a}$ are the scaled mutation and selection factors, i.e., $\mu^_{i}=\mu_{i}/\mu_{ts},\mu^_{i}^{†}=\mu_{i}/\mu_{ts},and ⁢\sigma^_{i}=\sigma_{i}/\theta_{ts}$, where the absolute value of mutation rate is set to $\mu_{ts}=1.11\times10^{-5}/nt/day$ from Zanini et al., 2017.

For each patient in our simulated trial, we then draw diversity $\theta_{ts}$ from the patient pool, and scale it by our fitted $ξ=2.1$, resulting in patient-specific selection and mutation factors,

$$
ξ\times\theta_{ts}\timesM^_{a}=(\theta_{1}⁢…⁢\theta_{i}\theta_{1}^{†}⁢…⁢\theta_{i}^{†}\sigma_{1}⁢…⁢\sigma_{i})⁢\mu_{ts}\timesM^_{a}=(\mu_{1}⁢…⁢\mu_{i}\mu_{1}^{†}⁢…⁢\mu_{i}^{†}Δ_{1}⁢…⁢Δ_{i})
$$

These parameters are then used to initialize the state of an HIV population within a patient according to (Appendix 5), and to determine the absolute rates in Algorithm 3 (Appendix 5) for the population evolution according to Equation 38. The decay rate is set to the fitted trial average of $r=0.31⁢days^{-1}$ (Equation 8). The carrying capacity $N_{k}$ is set according to Equation 21. This determines all parameters of the birth-death process simulating the intra-patient evolution of HIV, which are used in Algorithm 3 (Appendix 5).

We evolve a population through time until 56 days have elapsed since treatment, or until the escape fraction relative to the carrying capacity xt is above 0.8; see Algorithm 3 (Appendix 5). After $x_{t}>.8$ the evolution is governed by the deterministic equations, and the stochastic simulation ends. The rebound time $T$, defined as the intersection of the exponential envelope and the carrying capacity, can then be calculated analytically as,

$$
T=\frac{1}{\gamma}⁢log⁡(1+exp⁡(\gamma⁢t)⁢\frac{1-x_{t}}{x_{t}}).
$$

The resulting distribution for rebound times are shown as model predictions in Figure 3B–D.

Rebound times generated in this fashion were also used to estimate the probability of late rebound to characterize the efficacy of a given bNAb in curbing viral rebound. The probability of late rebound was estimated from 104 simulated patients. The interdecile quantiles (0.1–0.9) of early rebound (lt56 days) probability over 200 values of scaled selection coefficients $\sigma^$ drawn from the posteriors in Figure 4A are shown in Figure 4C.

### Model robustness

#### Effect of genomic linkage on the inference of selection

In our inference of selection (Equation 31, Figure 4A), we assume that the escape-mediating sites are at linkage equilibrium and that the distribution of allele frequencies can be approximated by a skewed Beta distribution (Equation 12), reflecting the equilibrium of allele frequencies. In reality, despite recombination, the HIV genome exhibits linkage effects, especially at nearby sites Zanini et al., 2015, and the viral populations experience changing selective pressures by the immune system Feder et al., 2021; Theys et al., 2018; Nourmohammad et al., 2019, and the transient population bottlenecks during therapy Feder et al., 2016.

To test the limits on the validity of our inference procedure, we applied it to in silico populations generated by full-genome forward-time simulations (Appendix 5, Algorithm 3) in the presence and absence of recombination. To do so, we considered an ensemble of ten patients with 100 genomes sampled at 10 time points, and used two diversity parameters $\theta_{ts}=0.01$ and $\theta_{ts}=0.1$, to cover the range reflected in patient data (Figure 2D, Figure 4—figure supplement 2).

One relevant scenario to consider is the impact of other selected sites in the genome on the distribution of alleles at the escape mediating sites against bNAbs. The sites under a strong constant selection are likely to be already fixed (or at a high a frequency) at their favorable state in the population. However, the strong selection on a large fraction of antigenic sites can be thought as time-varying, due to the changing pressure imposed by the immune system or therapy. To capture this effect, we simulated whole genome evolution in which linked sites were under strong selection ($0.1\timesgrowth rate$), and where the sign of selection changed after exponentially distributed waiting times (i.e. as a Poisson process); this model of fluctuating selection has been used in the context of influenza evolution Strelkowa and Lässig, 2012, and for somatic evolution of B-cell repertoires in HIV patients Nourmohammad et al., 2019. The resulted evolutionary dynamics in this case can involve strong selective sweeps and clonal interference due to the continuous rise of beneficial mutations (in the linked sites) within a population.

To test the robustness of our selection inference, we evaluated the distribution of maximum likelihood estimates (MLEs) for the selection values $\sigma^=\sigma/\theta_{t}⁢s$ at the escape mediating sites, inferred from the ensemble of sequences obtain from simulated data with linkage. Figure 4—figure supplement 2 shows that even for fully linked genomes (zero recombination) our MLE estimate of selection has little bias relative to the true values used in the simulations. Adding recombination into the simulations only further attenuates the effect of linkage (Figure 4—figure supplement 2), making the estimates more accurate.

The reason that selective sweeps of linked beneficial mutations have only minor effects on our inference of selection for the escape mediating sites is two-fold: First, the primary mechanism by which selective sweeps change the strength of selection at linked sites is via a reduction in the effective population size Hill and Robertson, 2009; Comeron et al., 2008. However, variations in the effective population size are already accounted for in our inference procedure: The selection likelihood in Equation 31 is conditioned on the measured neutral-site diversity, $\theta=2⁢N_{e}⁢\mu$. The change in the effective population size impacts the selection coefficient $\sigma=2⁢N_{e}⁢Δ$ and the diversity $\theta=2⁢N_{e}⁢\mu$ in the same way, and therefore, the (scaled) selection parameter $\sigma^=\sigma/\theta$ that we infer from data remains insensitive to changes in the effective population size.

The second reason for the robustness of our selection inference to linkage is due to the fact that a beneficial allele in a linked locus can appear on a genetic background with or without a susceptible variant, leading to the rise of either variants in the population. As a results, the impact of such hitchhiking remains a secondary issue in inference of selection at the escape sites, for which an ensemble of populations from different patients with distinct evolutionary histories of HIV-1are used.

#### Robustness of selection inference to intra-patient temporal correlations of HIV alleles

To infer the selection effect of mutations from the longitudinal deep sequencing data of Zanini et al., 2015, we use time averaging of the likelihood (Equation 31) to avoid conflating our results due to temporal correlations between the circulating alleles within patients (Figure 2B). We can view this choice as being one choice among two extremes: (i) to treat each patient as effectively one independent data point so that all patients are given the same weight or (ii) to treat each time point as independent, giving patients with more time points a higher weight. These two choices correspond to different log-likelihood functions for the (scaled) selection factor $\sigma^$:

$$
ℒ⁢(\sigma^)={\sum_{p,t}log⁡P_{p}⁢(m_{t},s_{t}|\theta_{ts}⁢(t),\sigma^)(t-independent)\sum_{p}\frac{1}{T_{p}}⁢\sum_{t}log⁡P_{p}⁢(m_{t},s_{t}|\theta_{ts}⁢(t),\sigma^)(t-averaged)
$$

where $T_{p}$ is the total number of time points from patient $p$, and $P_{p}⁢(m_{t},s_{t}|\theta_{ts}⁢(t),\sigma^)$ is the probability to observe $m$ escape mutants, and $s$ susceptible variants at time $t$ in patient $p$, given the neutral diversity $\theta_{ts}⁢(t)$ and the scaled selection factor $\sigma^$.

We find that both of these approaches result in similar posteriors for selection $\sigma^$ (Model robustness Figure 4—figure supplement 1A and C), although the $t$-averaged likelihood has a higher uncertainty due to fewer independent time points. Thus, our inference of selection is insensitive to the exact choice of the likelihood function given in Equation 40, yet our time-averaged approach remains the more conservative choice between the two.

#### Statistical significance of the reservoir-corrected diversity

In Equation 36, we introduced the reservoir factor $ξ^{*}=2.1$ to account for the diversity of HIV-1that is not sampled from a patient’s plasma prior to therapy, which resulted in a better fit of the rebound time distributions (Figure 3) compared to a reservoir-free model (Figure 4—figure supplement 3A). Here, we quantify the importance of the reservoir factor with a statistical test on the null hypothesis, $ξ_{0}=1$. Specifically, we perform a hypothesis test to test the necessity of using an inflated diversity $ξ⁢\theta_{ts}$ relative to using the bare diversity observed in pre-trial sequence data $\theta_{ts}$. To do so, we construct a disparity-based test statistic Ekström, 2008, which is analogous to the likelihood ratio test statistic.

Recall that the optimal reservoir factor $ξ^{*}=arg⁡min_{ξ}⁡R⁢(ξ|t_{1:p})$ was obtained by minimizing the disparity function $R⁢(ξ|t_{1:p})$ across measurements of rebound times $t_{1:p}$ from all the $p$ patients in data (Equation 36). We can estimate the test statistic for the reduction in disparity between the null hypothesis, $ξ_{0}=1$ and the fitted reservoir factor $ξ^{*}$ as,

$$
Δ_{R}⁢(t_{1:p})=R⁢(ξ_{0}|t_{1:p})-minξ⁡R⁢(ξ|t_{1:p}).
$$

We can then determine the p-value by estimating the quantile of the observed test statistic $Δ_{R}(t_{1:p})$ relative to that inferred from the distribution of $Δ_{R}(T_{1:p})$ obtained from simulations under null hypothesis $ξ_{0}=1$ (Fisher, 1956). Specifically,

$$
p-value=ET_{1:p}|ξ_{0}([Δ_{R}(T_{1:p}|ξ_{0})>Δ_{R}(t_{1:p})])
$$

where $ET_{1:p}|ξ_{0}(⋅)$ denotes the expectation over the rebound times $T_{1:p}$ obtained from 1000 realizations of simulated populations each with $p$ patients, and under the null hypothesis $ξ_{0}=1$ is the Iverson bracket that takes value 1 when its argument is true and 0, otherwise (Equation 34). The observed $Δ_{R}$ (Equation 41), the distribution of simulated values of $Δ_{R}⁢(T_{1:p}|ξ_{0})$ under the null hypothesis, and the resulting $p-value=0.004$ are shown in Figure 4—figure supplement 3B, C.

It should be noted that here we use the disparity measure because the corresponding likelihood function for the reservoir factor is inaccessible through forward simulations of populations. However, a general analogy exists between our approach and the more commonly used likelihood approach. Specifically, in an analogous likelihood-ratio test, the test statistic $Δ_{L}=max_{ξ}⁡log⁡p⁢(ξ|t_{1:p})-log⁡p⁢(ξ_{0}|t_{1:p})$ would be asymptotically $χ^{2}$-distributed with one degree of freedom under the null hypothesis Fisher, 1954, and the quantile under the null-hypothesis (p-value) would be estimated by inverting the $χ^{2}$ cumulative distribution function (i.e. a $χ^{2}$ test).

#### Robustness of selection inference to strains from different clades of HIV

The longitudinal deep sequencing data of Zanini et al., 2015 is collected from 11 patients, 9 of whom are infected with clade B strains of HIV-1, which is the dominant clade circulating in Europe Spira et al., 2003. All of the clinical trials we considered Caskey et al., 2015; Caskey et al., 2017; Baron et al., 2018 are from patients carrying clade B strains. For the results presented in the main text, we included all the 11 patients in our analysis. Here, we test wether our inference of selection is sensitive to the choice of including or excluding non-clade B patients in our analysis. We therefore repeated our inference procedure for selection by excluding the two non-clade B patients. Model robustness Figure 4—figure supplement 1A,B shows a strong agreement between the Bayesian posterior for selection factors in the two cases, with a slight increase in uncertainty for the case with only clade B patients. This increased uncertainty is related to the reduction in sample size by excluding the non-clade B patients from data. Nonetheless, the richness of the intra-patient diversity makes the inference robust to the exclusion of one or two patients.

#### Robustness of predictions for trial efficacy to the inferred values of selection strength

How sensitive are the outcomes of our predictions for the rebound time distributions (Figure 1) to the exact values of inferred selection strengths we used for our simulations? We addressed this question by performing a disparity analysis similar to that for the diversity $\theta$ in Equation 41. Specifically, we assessed whether we might need to rescale our inferred selection strength $\sigma/\theta_{ts}$ by a multiplicative factor $ξ_{s}$ (Figure 4—figure supplement 4).

In contrast to diversity, the reduction in disparity for adjustment of selection with a factor $ξ_{s}$ is small (Figure 4—figure supplement 4A) and not statistically significant ($p-value=0.49$; Figure 4—figure supplement 4B), and could be attributed to count noise. Still, we cannot discount the possibility that selection was slightly overestimated, possibly due to the effect of compensatory mutations in linked genome, the interplay between the reservoir and the inference of selection, or other biological factors. Nonetheless, in absolute terms, the null hypothesis (i.e. $ξ_{s}=1$) cannot be rejected and we have no statistical justification for adding an adjustment factor for selection inferred from untreated patients.

#### Robustness of rebound time predictions to methods of identifying escape mutations

Our predictions rely on identifying escape variants against each bNAb, either based on in vivo trial data and patient surveillance, or in vitro DMS assays. To test the sensitivity of our results to these methods, we compare the predictions of rebound time distributions when identifying escape sites from the DMS data versus the trial data. In Appendix 4, we perform this comparison for the 10–1074 and the PGT121 bNAbs; we do not include the 3BNC117 bNAb in this analysis since it targets the CD4 binding site of HIV-1and the DMS data is unreliable for identifying escape variants against it. As shown in Appendix 4—figure 1, both trial-inferred and DMS-inferred escape sites result in good predictions for rebound time distributions. However, its appears that using the DMS-inferred escape sites could lead to a more optimistic prediction for treatment success (i.e. a later rebound). This inconsistency may be due to the fact that DMS data is collected in vitro, and other biological factors could be influencing the in vivo escape patterns. Moreover, the differences in the genetic composition of the HIV-1strains circulating in patients enrolled in trials and the strains used for the DMS experiments could lead to different epistatic interactions that can enhance or reduce the chances of escape. For a systematic understanding of these differences and limitations, more experiments would be necessary. Nonetheless, DMS data can provides baseline to gauge the efficacy of different bNAbs for therapy and further in vivo investigation.
