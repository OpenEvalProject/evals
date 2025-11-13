# Antigenic strain diversity predicts different biogeographic patterns of maintenance and decline of antimalarial drug resistance

## Authors

- Qixin He<sup>1</sup> ([ORCID: 0000-0003-1696-8203](https://orcid.org/0000-0003-1696-8203)) †
- John K Chaillet<sup>1</sup> ([ORCID: 0000-0002-6156-4649](https://orcid.org/0000-0002-6156-4649))
- Frédéric Labbé<sup>2</sup> ([ORCID: 0000-0002-4064-2361](https://orcid.org/0000-0002-4064-2361))

### Affiliations

1. Department of Biological Sciences, Purdue University West Lafayette United States ([ROR:02dqehb95](https://ror.org/02dqehb95))
2. Department of Ecology and Evolution, University of Chicago Chicago United States ([ROR:024mw5h28](https://ror.org/024mw5h28))

† Corresponding author

## Abstract

The establishment and spread of antimalarial drug resistance vary drastically across different biogeographic regions. Though most infections occur in sub-Saharan Africa, resistant strains often emerge in low-transmission regions. Existing models on resistance evolution lack consensus on the relationship between transmission intensity and drug resistance, possibly due to overlooking the feedback between antigenic diversity, host immunity, and selection for resistance. To address this, we developed a novel compartmental model that tracks sensitive and resistant parasite strains, as well as the host dynamics of generalized and antigen-specific immunity. Our results show a negative correlation between parasite prevalence and resistance frequency, regardless of resistance cost or efficacy. Validation using chloroquine-resistant marker data supports this trend. Post discontinuation of drugs, resistance remains high in low-diversity, low-transmission regions, while it steadily decreases in high-diversity, high-transmission regions. Our study underscores the critical role of malaria strain diversity in the biogeographic patterns of resistance evolution.

## Introduction

Prolonged usage of antimicrobial drugs almost always results in the emergence and spread of resistant strains (zur Wiesch et al., 2011). The history of falciparum malaria chemotherapy over the last hundred years witnessed a succession of the spread of resistance to five classes of drugs region by region (Blasco et al., 2017). However, the patterns of drug resistance evolution, such as the speed of establishment and equilibrium frequencies, differ drastically across different biogeographic regions. Even though de novo-resistant alleles are constantly generated, widespread resistant strains can almost always be traced back to two unstable transmission regions, that is, Southeast Asia (especially the Greater Mekong Subregion) and South America (Ecker et al., 2012; Dondorp et al., 2009; Noedl et al., 2008). While the frequencies of resistant genotypes often sweep close to fixation in these regions under persistent drug usage (Chaijaroenkul et al., 2011; Plummer et al., 2004), their frequencies are more variable in endemic transmission regions such as sub-Saharan Africa (Talisuna et al., 2002). More interestingly, while in high-transmission regions a steady decrease of resistant genotypes often ensues from reducing the particular drug usage (Narh et al., 2020; Hemming-Schroeder et al., 2018), resistant genotypes are maintained at high frequency in low or unstable transmission regions even after the abandonment of the drug for several decades (Lanteri et al., 2014).

Plenty of mathematical models have been developed to explain some, but not all, of the empirical drug resistance patterns. Various relationships between transmission intensity and stable frequencies of resistance were discovered, each of which has some empirical support: (1) transmission intensity does not influence the fate of resistant genotypes (models: Koella and Antia, 2003; Masserey et al., 2022; empirical: Diallo et al., 2007; Shah et al., 2011; Shah et al., 2015); (2) resistance first increases in frequency and slowly decreases with increasing transmission rates (models: Klein et al., 2008; Klein et al., 2012); and (3) valley phenomenon: resistance can be fixed at both high and low end of transmission intensity (model: Artzy-Randrup et al., 2010; empirical: Talisuna et al., 2002). Other stochastic models predict that it is harder for resistance to spread in high-transmission regions, but patterns are not systematically inspected across the parameter ranges (model: Whitlock et al., 2021; model and examples in Ariey and Robert, 2003). Under non-equilibrium scenarios, that is, where insecticides or bednets temporarily reduced transmission, reductions in resistance frequency were also observed (Alifrangis et al., 2003; Mharakurwa et al., 2004; Myers-Hansen et al., 2020). Differences in these model predictions can be attributed to three types of model assumptions: (1) whether and how population immunity is considered, (2) how the cost of resistance is modeled, and (3) whether and how multiplicity of infection (MOI) is included. Although the great advances in malaria agent-based models (ABMs) enabled the inclusion of more detailed biological processes (Maire et al., 2006; Masserey et al., 2022; He et al., 2021; Labbé et al., 2023), the complexity of ABMs limits a direct application to analytical investigation. It is, therefore, critical to formulate a generalizable mathematical model that captures the most important biological processes that directly impact the survival and transmission of the parasites.

While most models have explored factors such as drug usage (Koella and Antia, 2003; Klein et al., 2012), treatment rate (Masserey et al., 2022), vectorial capacity (Artzy-Randrup et al., 2010; Bushman et al., 2018), within-host competition (Bushman et al., 2018; Hastings, 2006), population immunity (Klein et al., 2008; Artzy-Randrup et al., 2010), and recombination (Curtis and Otoo, 1986; Dye and Williams, 1997; Hastings, 1997; Hastings and D’Alessandro, 2000), strain diversity of parasites has not been explicitly considered in mathematical models of drug resistance. Yet, orders of magnitude differentiate antigenic diversity of Plasmodium falciparum strains among biogeographic zones and drive key differences in epidemiological features (Chen et al., 2011; Tonkin-Hill et al., 2018). Hyper-diverse antigens of parasites in sub-Saharan Africa emerged from the long-term co-evolutionary arms race among hosts, vectors, and parasites (Volkman et al., 2001). In endemic regions of falciparum malaria, hosts do not develop sterile immunity and can constantly get reinfected with reduced symptoms (Day and Marsh, 1991). These asymptomatic carriers of the parasite still constitute part of the transmission and serve as a reservoir of strain diversity (Tiedje et al., 2017; Bonnet et al., 2003) despite the fact that parasite prevalence decreases with host age in endemic regions (Aron, 1983). This age–prevalence pattern was attributed to acquired immunity after repeated infections and represented as different generalized immunity classes in disease dynamics models (Dietz et al., 1974; Molineaux and Gramiccia, 1980; Klein et al., 2008). Later advances in molecular epidemiology indicate the importance of strain-specific immunity (Kaufmann et al., 1999).

During the asexual blood stage, intra-erythrocytic parasites express adhesin proteins at the red blood cell surface that help mediate binding to the epithelial layers of vasculature to avoid the clearance by spleen during circulation (Bull et al., 1998). One of the major surface proteins, P. falciparum erythrocyte membrane protein 1 (PfEMP1), is encoded by var genes, a gene family of 60 different copies within a single parasite genome (Rask et al., 2010). Immune selection maintains the composition of var genes between different strains with minimal overlap (He et al., 2018). In high endemic regions, many antigenically distinct strains (or modules of strains) coexist in the transmission dynamics (Pilosof et al., 2019). Whether the hosts have seen the specific variants of the var genes largely determines the clearance rate of the parasites (Barry et al., 2011; Djimdé et al., 2003). Therefore, it is reasonable to suspect that variation in host-specific immunity, acquired from exposure to local antigenic diversity, plays a key role in local transmission dynamics as well as the fate of resistance. Thus, under the same vectorial capacity, different strain diversity results in significant changes in population-level immunity and transmission intensity, and the ensuing epidemiological patterns, such as MOI, age–prevalence curve, and the ratio of asymptomatic infections (Tiedje et al., 2017; Ruybal-Pesántez et al., 2022). These changes, in turn, alter the fate of resistance invasion. Therefore, in addition to generalized immunity represented in earlier studies, models need to formally incorporate specific immunity.

Another challenging aspect for earlier models is whether and how multiclonal infections (those with MOI > 1) are considered. Due to malaria’s long duration of infection (Collins and Jeffery, 1999), it is common for the host to carry infections that are contracted from separate bites, referred to as superinfections. Meanwhile, hosts can also receive multiple genetically distinct strains from a single bite, especially in high-transmission endemic regions (Nkhoma et al., 2018; Wong et al., 2017; Henden et al., 2018). Susceptible-infected-recovered (SIR) models that only consider non-overlapping infections (Koella and Antia, 2003; Klein et al., 2008; Artzy-Randrup et al., 2010) cannot incorporate within-host dynamics of strains explicitly, which strongly impacts the fitness of resistant genotypes (de Roode et al., 2004; Bushman et al., 2016). Other superinfection models employ complex structures or specific assumptions that make it hard to link MOI with strain diversity or host immunity (Koella and Antia, 2003; Klein et al., 2012).

Here, we present a novel ordinary differential equations (ODE) model that investigates how strain diversity and transmission potential influence disease prevalence, hosts’ strain-specific and generalized immunity, and the resulting MOI distribution. In this model, strain-specific immunity toward diverse surface proteins determines the probability of new infections. In contrast, generalized immunity of the hosts determines the likelihood of clinical symptoms. Hosts are less likely to show symptoms with repeated infections but can still be reinfected by antigenically new strains and contribute to transmission. Our modeling strategy combines the advantages of both the traditional compartmental epidemiological models (i.e., tracking transmission dynamics and population immunity responses to different levels of transmission intensity) (Koella and Antia, 2003; Klein et al., 2008; Artzy-Randrup et al., 2010; Klein et al., 2012) and population genetics ones (i.e., tracking within-host dynamics with detailed consideration of fitness cost and competition among strains) (Curtis and Otoo, 1986; Dye and Williams, 1997; Hastings, 2006; Hastings, 1997; Hastings et al., 2002). With varying strain diversity, transmission potential, resistance cost, and symptomatic treatment rates, we explore the key questions outlined above: whether strain diversity modulates the equilibrium resistance frequency given different transmission intensities, as well as changes in this frequency after drug withdrawal, and whether the model explains the biogeographic patterns of drug resistance evolution. We found that due to the feedback between transmission and host immunity, high equilibrium prevalence can only be achieved in transmission regions with high strain diversity. We observed a negative correlation between parasite prevalence and resistance frequency, regardless of resistance cost or efficacy. Post drug discontinuation, resistant frequency is maintained much longer in low-diversity regions than in high-diversity regions. We then verified the main qualitative outcome from the model against the empirical biogeographic patterns of chloroquine resistance evolution.

## Results

### Model structure

In the compartmental ODE model, hosts’ strain-specific immunity ($S$) regulates infectivity of parasite strains, while generalized immunity ($G$) determines symptomatic rate (Figure 1; see model details in ‘Methods’ and Appendix 1). Hosts are tracked in different classes of generalized immunity ($G$) and drug usage status (untreated, $U$; treated, $D$). Hosts move to a higher $G$ class if they have cleared enough infections and go back to a lower class if they lose generalized immunity (Figure 1B: $G_{i}→G_{j}$, Figure 1—figure supplement 1). Lower $G$ classes correspond to more severe and apparent symptoms, which increase the likelihood of being treated by drugs ($U→D$), as evidenced from most impacted countries where children are the main symptomatic hosts (Tiedje et al., 2017). The population sizes of resistant ($PR$) or sensitive (wild-type; $PW$) parasites are tracked separately in host compartments of different $G$ and drug status. Since hosts can harbor multiple parasite strains, parasites are assumed to be distributed independently and randomly among hosts within the same compartment (Anderson and May, 1978). Parasites can move between the compartments via the movement of hosts that harbor them or can be added to or subtracted from the compartments via new infections and parasite clearance, respectively. $PW$ can be cleared by host immunity and drug treatment, while $PR$ can only be cleared by host immunity. However, $PR$ has a cost, $s$, in transmissibility, and the cost is higher in mixed-genotype ($s_{mixed}$) infections than in single-genotype infections ($s_{single}$) following Bushman et al., 2016; Harrington et al., 2009; Bushman et al., 2018.

![Figure 1.](https://cdn.elifesciences.org/articles/90888/elife-90888-fig1-v2.jpg)

**Figure 1.:** (A) Rules for new infections given the host’s past infection history and current multiplicity of infection (i.e., multiplicity of infection [MO]). Upon transmission of a specific parasite strain A, if the host has had an infection of strain A in the past (hands raised), a new infection will not be added to the current MOI; instead, the infection will be considered cleared and added to the total number of cleared infections; if the host is new to strain A and does not have specific immunity to it (inferred from Equation 1), a new infection will be added (i.e., MOI increase by 1) as long as MOI does not exceed the carrying capacity of coexisting strains. (B) Rules of symptomatic infections and treatment in the different generalized immunity ($G$) classes. With increasing generalized immunity ($G$), hosts are less likely to show clinical symptoms. Hosts in $G_{0}$ have a risk of death in addition to symptomatic infections; Hosts in $G_{1}$ do not die from infections but show symptoms upon new infections; Hosts in $G_{2}$ carry asymptomatic infections most of the time with a slight chance of showing symptoms. Symptomatic infections result in a daily treatment rate that removes the infections caused by wild-type strains. Hosts that have cleared enough number of infections will move to the next $G$ class. Hosts will move back to a lower $G$ class when the generalized immunity memory is slowly lost if not boosted by constant infections.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/90888/elife-90888-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) The number of hosts and movements are tracked in different generalized immunity classes ($G$), together with their drug treatment states (treated, $D$; untreated, $U$); (B) wild-type ($PW$) and resistant parasite ($PR$) population sizes are tracked in different host immunity classes; (C) Changes in total immunity ($TI$, total number of cleared infections) per $G$ class are followed. See Appendix 1 for a detailed explanation of the ODE system.

Instead of tracking antigenic diversity explicitly, we assume parasites have $n_{strains}$ with unique antigen compositions at the population level. We incorporate specific immunity by calculating the probability of seeing a new strain given a $G$ class upon being bitten by an infectious mosquito,

$$
η_{i}=(1−\frac{1}{n_{strains}})^{ν_{i}}
$$

where $ν_{i}$ is the average number of cumulative infections received and cleared by a host in class $G_{i}$, and is updated at each time step as determined by the immune memory submodel (see Appendix 1).

### Impact of strain diversity and transmission potential on disease prevalence

To avoid assuming an arbitrary level of strain diversity given transmission rate, we explored the impacts of the number of strains and transmission potential on prevalence separately across the empirical range observed in the field using our compartmental ODE model (Figure 2A). Specifically, the number of unique strains ranges from 6 to 447, which corresponds to a pool of 360 (typical of low-transmission regions) to 27,000 unique surface antigens (typical of sub-Saharan Africa) (Chen et al., 2011; Tonkin-Hill et al., 2018). Transmission potential refers to the product of vectorial capacity ($C$) and the maximum transmissibility between host and mosquito in one transmission cycle ($g$) (see ‘Methods’). We model the pattern of transmissions through mosquito bites following a sinusoidal curve (Appendix 1), representing a peak transmission period in the wet season, and low transmission in the dry season annually, with a mean transmission potential from 0.007 to 5.8. Given $g$ of 0.08 (see ‘Methods’), this range encompasses the lowest vectorial capacity to maintain a constant transmission to the level of high-transmission settings in Africa (Garrett-Jones and Shidrawi, 1969). We observe that the range of transmission potential that leads to the highest prevalence given a specific strain diversity increases from low diversity to high diversity (see gray area in Figure 2A, Figure 2—figure supplement 1). The prevalence decreases under drug treatment, but maintains the same relationship with strain diversity and transmission potential as that without treatment (Figure 2—figure supplement 1). This is consistent with the strain diversity being the outcome of long-term coevolution between parasite transmission and host immunity, whereby high-transmission regions usually correspond to high antigenic diversity and low-transmission regions exhibit low antigenic diversity (Chen et al., 2011; Tonkin-Hill et al., 2018). Therefore, for the following analyses, we focused on the parameter combinations within the gray area in Figure 2A, where diversity tracks transmission intensity. We then compared strain diversity and transmission potential pairing to the tentative empirical ranges of different continents (see ‘Methods’, Figure 3). As expected, strain diversity in Africa is much higher than in other continents, while transmission potential varies widely within continents, with overlaps in medium ranges. Interestingly, while strain diversity in Africa and Asia tracks the range of transmission potential, Oceania and South America have lower strain diversity than expected by transmission potential.

![Figure 2.](https://cdn.elifesciences.org/articles/90888/elife-90888-fig2-v2.jpg)

**Figure 2.:** (A) The heatmap shows a nonlinear parasite prevalence response given increasing transmission potential and the number of strains under no drug treatment, with warmer colors representing high prevalence and cooler colors representing low prevalence. X and Y axes correspond to increasing transmission potential and the number of strains in logarithmic scales. White tiles indicate the highest prevalence given a fixed number of strains. (B) The heatmaps show resistance frequencies under varying strain diversity and transmission potential at two levels of drug treatment rate, with warmer colors representing higher resistance frequency (in this example, $s_{single}$ = 0.1, $s_{mixed}$ = 0.9). A comparison between the prevalence pattern in (A) and resistance frequency in (B) reveals that high-prevalence regions usually correspond to low resistance frequency at the end of resistance invasion dynamics. (C) A negative relationship between parasite prevalence and resistance frequency. The color of the points indicates combinations of resistance fitness costs in hosts with resistant strains alone ($s_{single}$) or mixed infections of resistant and wild-type strains ($s_{mixed}$).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/90888/elife-90888-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Gray areas indicate that transmission is eliminated.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/90888/elife-90888-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Total immunity divided by the number of hosts per $G$ class (see Equation 1). $s_{single}$: 0.1; $s_{mixed}$: 0.9.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/90888/elife-90888-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** Relationship between parasite prevalence and resistance frequency under full treatment (daily treatment rate $d1=0.2$).Each subgraph represents the combination of resistance fitness costs in hosts with resistant strains alone ($s_{single}$) and mixed-genotype infections of resistant and wild-type strains ($s_{mixed}$), as well as the efficacy of resistance ($\mu_{P_{RD}}$). Color indicates transmission potential.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/90888/elife-90888-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** Relationship between parasite prevalence and resistance frequency under partial treatment (daily treatment rate $d1=0.05$).Each subgraph represents the combination of resistance fitness costs in hosts with resistant strains alone ($s_{single}$) or mixed-genotype infections of resistant and wild-type strains ($s_{mixed}$). Color indicates transmission potential, as well as the efficacy of resistance ($\mu_{P_{RD}}$).

![Figure 3.](https://cdn.elifesciences.org/articles/90888/elife-90888-fig3-v2.jpg)

**Figure 3.:** Squares denote the known minimum and maximum values of transmission potential and the number of strains from literature see Tables 1 and 2 for parameter sources. We overlaid the empirical parameter ranges on the simulated equilibrium resistance frequency as a visual reference using the same parameters of Figure 2B. The empirical resistance frequency of these regions will depend on specific treatment rates and resistance costs, which is shown in Figure 4.

### A negative relationship between disease prevalence and drug resistance frequency

To investigate resistanceinvasion, we introduce 10 resistant infections to the equilibrium states of drug treatment with wild-type-only infections and follow the ODE dynamics till the next equilibrium. In general, the frequency of resistance decreases with increasing parasite prevalence (Figure 2B and C), except for very low transmission potential, where resistance always fixes because wild-type strains cannot sustain transmissions under treatment (Figure 2—figure supplement 1, Figure 2—figure supplements 3 and 4). The fitness costs of single- and mixed-genotype infections, symptomatic treatment rate, and the efficacy of drug resistance only influence the slope of the relationship and the range of coexistence of resistant and wild-type parasites, but do not alter the negative relationship qualitatively (Figure 2C, Figure 2—figure supplements 3 and 4). Note that the negative relationship holds even when resistant genotypes have zero cost in transmissibility: they might still coexist instead of fix under very high disease prevalence (green dots in Figure 2C). Therefore, in the following sections, we only present results from one set of fitness cost combinations (i.e., $s_{single}=0.1$ and $s_{mixed}=0.9$ to be consistent with an earlier modeling study of parasite competition; Bushman et al., 2018).

The negative relationship between resistance and prevalence is corroborated by the empirical observation of the chloroquine-resistant genotype. The global trend of the critical chloroquine-resistant mutation pfcrt 76T follows an overall decline in frequency with increasing prevalence, which qualitatively agrees with the similar relationship from our model (Figure 4; beta regression, $p value<2e−16$). Samples from Asia and South America cluster around low-prevalence and high-resistance regions, with Asian samples having more variation in resistance, whilst samples from Oceania and Africa display a wide range of prevalence and resistance frequency. These characteristics could have emerged from our model dynamics given the parameter ranges of transmission potential and strain diversity of different continents (Figure 3).

![Figure 4.](https://cdn.elifesciences.org/articles/90888/elife-90888-fig4-v2.jpg)

**Figure 4.:** Sampling between 1990 and 2000 was included to ensure genotyping was performed largely before the policy switch of the first-line antimalarial drugs to ACT. Different shapes indicate samples from different continents, while shape sizes correspond to sample sizes for genotyping (see ‘Methods’ for details).

### Dynamics of resistance invasion: Feedback between drug usage and host immunity modulated by strain diversity

The pattern of drug resistance and disease prevalence arises from the interaction between host immunity, drug treatment, and resistance invasion. In order to inspect the dynamics of resistance invasion in detail, we select a subset of strain diversity and transmission potential combinations as representative scenarios for the empirical gradient of low- to high-transmission settings for the following analyses (white squares in Figure 2A). So far, we have assumed that strain diversity and transmission potential may vary independently. However, in empirical settings, strain diversity is the outcome of long-term coevolution between parasite transmission and host immunity, whereby high-transmission regions usually correspond to high antigenic diversity and low-transmission regions exhibit low antigenic diversity (Chen et al., 2011). Therefore, given the level of strain diversity, we picked the transmission potential that generates the highest prevalence. Under this constraint, the relationship between transmission potential and prevalence or diversity and prevalence is monotonic, in accordance with the prevailing expectation (Figure 5A). From low to high diversity/transmission, hosts’ generalized immunity increases accordingly (higher fraction of hosts in $G_{1}$ or $G_{2}$ classes in Figure 5). When drug treatments are applied in a wild-type-only transmission setting, parasite prevalence is significantly reduced (Figure 2—figure supplement 1), as is host generalized immunity (Figure 5A, upper panel). A much larger proportion of hosts stay in $G_{0}$ and $G_{1}$ when effective drug treatment is applied compared to when there is no treatment. In addition, the proportion of hosts in drug-treated status increases under higher diversity. If instead the resistant genotype is present in the parasite population and starts invading when the drug is applied, hosts’ generalized immunity is comparable at equilibrium to that of the no-treatment scenario (Figure 5, lower panel). The drug-treated hosts in $G_{0}$ and $G_{1}$ are comparable from low to high transmission, while the frequency of resistance decreases with increasing diversity (Figure 5, lower panel).

![Figure 5.](https://cdn.elifesciences.org/articles/90888/elife-90888-fig5-v2.jpg)

**Figure 5.:** Fraction of hosts in different $G$ classes with increasing strain diversity and the corresponding transmission potential indicated by white circles in Figure 1A at equilibrium before drug treatment (left panel) or year 50 after the invasion of resistant genotypes (middle and right panels). Hosts under drug treatment are indicated by stripes. Red dotted lines show the corresponding frequency of resistance. The upper panel is generated under wild-type-only infections with increasing treatment rates. The lower panel represents resistance-only infections without treatment or resistant invasion under treatments.

Temporal trajectories of resistance invasion show that parasite population size surges as resistant parasites quickly multiply (Figure 6). In the meantime, resistance invasion boosts host immunity to a similar level before drug treatment (Figure 6, upper panel). The surge in host immunity, in turn, reduces the advantage of resistant parasites, leading to a quick drop in parasite prevalence. Under a low-diversity scenario, wild-type parasites quickly go extinct (Figure 6A). Under high diversity, however, a high proportion of hosts in the largely asymptomatic $G_{2}$ creates a niche for wild-type parasites because the higher transmissibility of wild-type parasites compensates for their high clearance rate under drug treatment (Figure 6B). To summarize, the coexistence between wild-type and resistant genotypes in high-diversity/transmission regions reflects an interplay between the self-limiting resistant invasion and higher transmissibility of wild-type parasites as resistant invasion elevates the overall host immunity and thus the presence of a large fraction of hosts carrying asymptomatic infections.

![Figure 6.](https://cdn.elifesciences.org/articles/90888/elife-90888-fig6-v2.jpg)

**Figure 6.:** Host (A) and parasite dynamics (B) under resistance invasion are shown for lower ($n_{strains}$ = 20) and higher ($n_{strains}$ = 113) diversity under the same daily treatment rate of 0.05. Wild-type parasite population size is also presented in inset C with a smaller scale for clarity. Because drug treatment does not affect resistant parasites, they surge quickly after introduction, thus leading to more infections (upper panel of B). Hosts recovered from a large number of new infections move into higher $G$ classes (from year 1–8) (B). The higher specific immunity reduces the infectivity of new strains, leading to a reduction of the resistant parasite population regardless of the diversity level (year 4–10; upper panel of B). Under low diversity, wild-type parasites quickly go to extinction C. Under high diversity, the less symptomatic $G_{2}$ class provides a niche for wild-type parasites to multiply (year 4–10), where the two genotypes coexist, with the wild-type parasite population size surpassing that of resistant ones. Meanwhile, resistant parasites dominate in hosts that are in $G_{0}$ and $G_{1}$ B.

### Response to drug policy change differs among high- and low-diversity scenarios

In our model, low-diversity scenarios suffer the slowest decline in resistant genotypes after switching to different drugs. In contrast, resistance frequency plunges quickly in high-diversity regions when the drug policy changes (Figure 7, Figure 7—figure supplement 1). Two processes are responsible for the observed trend. First, resistant genotypes have a much higher fitness advantage in low-diversity regions even with reduced drug usage because infected hosts are still highly symptomatic; this trend holds even if diversity is decoupled with transmission potential: given the same transmission potential, high-diversity scenarios have a faster percentage of reduction in resistance (see Figure 7—figure supplement 1). Second, if low transmission potential is coupled with low diversity, the rate of change in parasite populations is slower due to longer generation intervals between transmission events. This pattern corroborates similar observations across different biogeographic areas: while the transition of the first-line drug to ACT in Africa, such as Ghana and Kenya, resulted in a fast reduction in resistant genotypes, the reduction was only minor in Oceania, and resistant genotypes are still maintained at almost fixation in Southeast Asia and South America despite the change in the first-line drugs occurring more than 30 y ago (Figure 8).

![Figure 7.](https://cdn.elifesciences.org/articles/90888/elife-90888-fig7-v2.jpg)

**Figure 7.:** Each trajectory represents the mean resistance change from the combination of variables indicated by the gray area in Figure 1A. Color from cool to warm represents increasing diversity in strains. Here the usage of the drug, to which parasites have developed resistance, is reduced to 0.52, 0.52, 0.52, 0.52, 0.21, 0.21, 0.21, 0.21, 0, 0, 0, 0, 0, 0, 0, 0 each year following the change in the treatment regime. The trajectory of reduction in resistant drug usage follows the usage survey in western Kenya from 2003 to 2018 (Hemming-Schroeder et al., 2018).

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/90888/elife-90888-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** Percentage of reduction in resistance after 1 y of policy change in drug treatment as a function of transmission potential and the number of strains under different combinations of resistance costs ($s_{single}$; $s_{mixed}$).

![Figure 8.](https://cdn.elifesciences.org/articles/90888/elife-90888-fig8-v2.jpg)

**Figure 8.:** Each circle represents one studied sample (at least 20 infected hosts) from one geographic location. Circles connected by dotted lines represent longitudinal samples from the same study. After the policy switch in first-line antimalarial drugs, frequencies of resistance decreased gradually in Africa, but maintained high in Asia, Oceania, and South America despite the policy change for more than 20 y. CQ: chloroquine; SP: sulfadoxine-pyrimethamine; MQ: mefloquine; AQ: amodiaquine; PQ: primaquine; QN-TET: quinine + tetracycline; ACT: artemisinin-based combination therapy.

### Comparison to a generalized-immunity-only model

Previous results demonstrate how transmission and antigenic diversity influence host immunity and hence the infectivity and symptomatic ratio, which determine the invasion success and maintenance of resistant genotypes. In order to confirm whether antigenic diversity is required to generate these patterns, we investigated a generalized-immunity-only model, in which infectivity of a new infection per $G$ class is set at a fixed value (i.e., taken as the mean value per $G$ class from the full model across different scenarios; see ‘Methods’). We observe a valley phenomenon (i.e., resistance frequency is both high at the two ends of prevalence; Figure 9), which is qualitatively similar to Artzy-Randrup et al., 2010. Similarly, following the switch of first-line drugs, the medium-transmission region has the fastest reduction in resistance frequency, followed by the high- and low-transmission regions. This pattern also differs from that under the full model, where resistance in high-transmission regions reduces the fastest. When we compare how the host and parasite fraction in $G$ classes change with increasing transmission potential, we find that because the infectivity of bites does not decrease as transmission increases, the number of drug-treated hosts keeps increasing in the $G2$ class, resulting in the rising advantage of resistant genotypes (Figure 9—figure supplement 2). The comparison between the full model versus the generalized-immunity-only model emphasizes the importance of incorporating antigenic diversity to generate a negative relationship between resistance and prevalence.

![Figure 9.](https://cdn.elifesciences.org/articles/90888/elife-90888-fig9-v2.jpg)

**Figure 9.:** Paths are connected from low transmission potential to high-transmission potential. Colors represent different combinations of single-genotype infection cost and mixed-genotype infection cost of resistant parasites.

![Figure 9—figure supplement 1.](https://cdn.elifesciences.org/articles/90888/elife-90888-fig9-figsupp1-v2.jpg)

**Figure 9—figure supplement 1.:** Note that in the generalized-immunity-only model, there is no strain diversity. The only parameter that determines transmission intensity is transmission potential. Trajectories that end earlier than year 16 indicate the disease is eradicated.

![Figure 9—figure supplement 2.](https://cdn.elifesciences.org/articles/90888/elife-90888-fig9-figsupp2-v2.jpg)

**Figure 9—figure supplement 2.:** Note that in the generalized-immunity-only model, there is no strain diversity. The only parameter that determines transmission intensity is transmission potential. In general, prevalence (blue dotted line) increases as transmission potential increases despite hosts increasingly concentrating in $G_{2}$ class (A). The fraction of resistant parasites decreases initially with increasing transmission potential, but rises again as high transmission results in a higher proportion of $G_{2}$ hosts in the drug-treated class (B).

## Discussion

In this article, we present a theoretical argument, built on the basis of a mechanistic model, as to why different biogeographic regions show variation in the invasion and maintenance of antimalarial drug resistance. While past models have examined the frequency of drug resistance as a consequence of transmission intensity and generalized immunity, these models, unlike ours, failed to reproduce the observed patterns of monotonic decreasing trend of resistance frequency with prevalence despite varying resistance costs, access to treatments, or resistance efficacy. This contrast stems from two main innovations of our model. First, its formulation directly links selection pressure from drug usage with local transmission dynamics through the interaction between strain-specific immunity, generalized immunity, and host immune response. Second, this formulation relies on a macroparasitic modeling structure suitable for diseases with high variation in cooccurring infections and strain diversities (Anderson and May, 1978). Hosts are not tracked as infected or susceptible; rather, the distribution of infections in hosts of different immunity classes is followed so that within-host dynamics of parasites can be easily incorporated.

In essence, the dynamics of resistant genotypes of a single locus are governed by two opposing forces: the selective advantage from drug usage and the cost of resistance. Both forces emerge, however, from local transmission dynamics, contrary to many earlier population genetics or epidemiological models that set these as fixed parameters. For example, when a fixed fraction of hosts is assumed to be drug-treated upon infection (e.g., in Curtis and Otoo, 1986; Dye and Williams, 1997; Hastings, 1997; Koella and Antia, 2003), the frequency of resistance is found to be unrelated to transmission intensity or requires other mechanisms to explain why resistance is prevalent in low-transmission regions. Later models recognize the importance of clinical immunity gained through repeated reinfections (analogous to the $G2$ class in our model) in reducing drug usage (Klein et al., 2008; Artzy-Randrup et al., 2010). Countries with different access to treatment (i.e., different treatment rates of symptomatic patients) also influence the net advantage of resistance (Masserey et al., 2022). However, in these models, the infectivity of new bites constrained by antigen diversity is not considered such that under high transmission the clinically immune class still receives numerous new infections, and the lowered symptomatic rate does not offset the amount of drug treatment due to new infections, giving rise to the increasing resistance prevalence at the high end of transmission potential (see Figure 9 and Artzy-Randrup et al., 2010). In contrast, in our model the selective pressure from drug treatment not only depends on the host ratio in the clinically immune class, but also on the infectivity of new bites regulated by specific immune memory. Therefore, when the host population suffers a high parasite prevalence, most hosts have experienced many infections and have entered the clinically immune class, where the drastically reduced infectivity coupled with the reduced symptomatic rate result in an overall reduced drug treatment per infection, mitigating the advantage of resistance.

Cost of resistance in terms of its form and strength is a complicated topic by itself. On the one hand, replication rates of resistant parasites are consistently found to be slower such that they produce less parasitemia during the infection than wild-type parasites (Bushman et al., 2016; Koella, 1893; de Roode et al., 2005). On the other hand, field studies also show that the transmissibility could be partially compensated by a higher gametocyte production (reviewed in Koella, 1998). Here we assume resistant parasites have lower transmissibility, but the cost differs between mixed- vs. single-genotype infections. Empirical and modeling studies Bushman et al., 2016; Bushman et al., 2018; de Roode et al., 2004 have shown that within-host competition between resistant and wild-type infections results in a higher cost for resistant infections than in single-genotype infections. This phenomenon could potentially prevent resistance establishment under high-transmission settings where mixed-genotype infections are more common (Bushman et al., 2018). However, we did not find that the higher cost in mixed-genotype infections influenced the qualitative pattern of a negative relationship between transmission intensity (represented by parasite prevalence) and resistance frequency. In addition, an equal cost in mixed- vs. single-genotype infections also produced a lower frequency of resistance at high transmission in the full model, but not in the GI-only model, indicating that within-host competition will exacerbate the disadvantage of resistant parasites under high transmission, but does not generate the negative correlation. The temporal dynamics of resistance invasion showed that the self-limiting property of resistant parasites creates a specific niche for wild-type infections to coexist. Specifically, as resistance invades, hosts experience more infections, leading to higher generalized immunity. Wild-type infections will then dominate in the lower symptomatic class because they have higher transmissibility.

The inclusion of strain diversity in the model provides a new mechanistic explanation as to why Southeast Asia has persisting resistance to certain antimalarial drugs, including chloroquine, despite a lower transmission intensity than Africa. In these regions with low strain diversity, parasites cannot repeatedly reinfect hosts. Therefore, clinically immune hosts do not carry infections very often. Thus, in our model resistant strains reach fixation or near-fixation regardless of the actual transmission potential, and upon removal of the drug pressure, these regions continue to maintain high levels of drug resistance for a prolonged time. In contrast, high-diversity regions (e.g., Africa) should show a wide range of resistance frequency depending on how antigenic diversity is matched with local vectorial capacities and should respond more rapidly to changing drug pressures. These results are partially corroborated by a comparison with regions that have higher transmission potential than Southeast Asia but low diversity (e.g., Papua New Guinea) (Chen et al., 2011; Figure 3). The resistance trends for Papua New Guinea behave most similarly to those for Southeast Asia, suggesting that strain diversity, instead of transmission potential, is key to predicting trends in drug resistance frequency. When diversity is less than expected by transmission potential, most mosquito bites have low infectivity, and most infections only occur in hosts with lower generalized immunity. Therefore, resistant genotypes will help ensure disease transmission in these symptomatic hosts and be strongly selected to be maintained.

As comprehensive as the model is, it still has some limitations. First, it currently assumes that a single locus determines resistance. If resistance is encoded or augmented by two or more loci (e.g., ACT or SP), past population genetic models demonstrate that rates of recombination could strongly influence the spread and maintenance of resistance (Dye and Williams, 1997; Hastings, 2006). Recent models have shown that preexisting partner-drug-resistant genotypes promote the establishment of Artemisinin resistance (Watson et al., 2022). However, as recombination is one of the potential reasons why multilocus resistance has delayed appearance in high-transmission regions, the incorporation of recombination is not expected to alter the negative relationship between resistance and prevalence. These earlier population genetics models of drug resistance posit that a high selfing rate in low transmission ensures high linkage among multilocus resistance, promoting their higher frequencies (Dye and Williams, 1997; Hastings and D’Alessandro, 2000; Hastings and Donnelly, 2005). Thus, adding multilocus resistance is expected to augment the negative correlation between resistance and prevalence. Expansion of the current model to include multilocus resistance will shed light on this prediction.

Second, our deterministic compartmental model does not consider several sources of variation in parasite transmission. Genetic drift is not incorporated in the model, which could influence the variation of strain frequencies at the population level due to severe bottlenecks during vector transmission (Wong et al., 2018). Demographic stochasticity would be more likely to impact low-transmission areas during the resistance invasion, while less impacting the biogeographic patterns for resistance maintenance. Our model also assumes that parasites are independently and randomly distributed in hosts, while the negative binomial distribution (NBD) is widely used in macroparasitic models (Anderson and May, 1978). Empirical evidence of parasite burdens is usually over-dispersed in that relatively few members of the host population harbor the majority of the parasite population (Anderson and Gordon, 1982; Churcher et al., 2005; Grogan et al., 2016). In our model, we argue that despite the MOI within each $G$ class being Poisson distributed, the population-level MOI distribution is over-dispersed as hosts in the $G2$ class are much less likely to be infected than in $G1$ or $G0$ (Figure 2—figure supplement 2) and hosts in drug-treated classes have lower MOI than untreated classes as they harbor mostly resistant parasites only. By discretization of host classes and parasite types, we considered over-dispersion at the population level. Future models could expand on the NBD for individual classes by fitting empirical data from different age classes. The assumption of independent distribution of parasites also implies homogeneous within-host selection and equal frequency of the same genotype strains. In reality, within-host strain frequency will vary depending on the time of each infection, strain similarities, and host immunity to specific antigens. These processes will generally increase the variation of resistant genotype frequencies at the population level, but should not impact the overall biogeographic pattern inferred here.

Lastly, our model assumed a random association between resistant genotype and antigenic diversity. In reality, in the early stage of invasion, the resistant genotype should have a limited antigenic background until it becomes widespread. In an agent-based stochastic model, Whitlock et al., 2021 found that selection for high antigenic variation in high transmission slows the spread of resistance. The interference of immune selection and resistance might serve as an additional reason why resistant parasites are at lower frequencies in high-transmission settings. Future stochastic models are desirable for quantifying the dynamics of interactions between antigenic variation and resistant loci under different epidemiological settings.

It is also to be noted that the trend found in our model predicts an equilibrium state of resistance frequency under persistent drug usage, which cannot be extrapolated to transient dynamics of new drug introduction. As shown in Figure 7, a fast sweeping phase is always associated with a new introduction of resistant genotypes in both low- and high-diversity regions. Therefore, we focused on empirical comparison to Pfcrt 76T because this mutation is essential for chloroquine resistance (Ecker et al., 2012) and chloroquine has been heavily used as first-line drugs for years in most countries.

In sum, we show that strain diversity and associated strain-specific host immunity, dynamically tracked through the macroparasitic structure, can predict the complex relationship between transmission intensity and drug resistance frequencies. Our model implies that control protocols should vary from region to region and that there is no one-size-fits-all cure for malaria control worldwide (Rasmussen et al., 2022). In regions of low prevalence, such as Southeast Asia, long-term goals for malaria prevention will likely not be aided by intensive drug treatment (Delacollette et al., 2009; Imwong et al., 2020). In these regions, elimination of falciparum malaria through vector control measures could proceed with little effect on drug resistance levels, whereas continual drug treatment will almost certainly cause fixation or near-fixation of resistance for a prolonged period of time, even after discontinuation of one drug. In contrast, in high-prevalence regions such as sub-Saharan Africa, measures of prompt switching between first-line drugs and combination therapies will be quite robust against rapid increases and prolonged maintenance of drug resistance (Flegg et al., 2013).

## Methods

### Transmission dynamics

Rather than following the infected vector populations, transmission potential is given by a fixed contact rate, which represents the contact rate per host at which a mosquito bites a donor host, gets infected, survives the sporogonic period, and transmits to a recipient host. This contact rate is uniform across all host classes. Hosts may harbor 0 to $n_{max}$ strains of parasites. Those with $MOI>0$ will be able to infect mosquitoes. However, a strain from the donor does not guarantee its successful infection in a recipient. Instead, the infections will not result if the host has reached its carrying capacity of $n_{max}$ strains, at which they cannot harbor more infections, or if the host has encountered and acquired the specific immunity to the strain (Figure 1A). In these cases, the MOI in the host remains constant. Otherwise, infection will result, and MOI will increase by 1.

### Calculating MOI and parasite prevalence

A major assumption that links host and parasite populations is that the number of infections in an individual host (i.e., MOI) at any time follows some prespecified distribution. To reduce the number of parameters and simplify the model, a Poisson distribution was used for MOI within a given $G$ and treatment class. This assumption allows us to directly calculate the prevalence (i.e., the fraction of individuals carrying at least one infection) in a given $G$ class $i=0,1,2$ and treatment class $j=U,D$ as

$$
I_{i,j}=1−exp⁡(−r_{i,j})
$$

where $r$ is the mean MOI of the class and is equal to

$$
r_{i,j}=\frac{PW_{i,j}+PR_{i,j}}{H_{i,j}}
$$

where $PW_{i,j}$ and $PR_{i,j}$ are the numbers of wild-type (W) and resistant (R) infections circulating in the host class at a given time, and are determined from the system of mechanistic differential equations (Figure 1—figure supplement 1B). $H_{i,j}$ is the number of hosts in the class at a given time and is similarly determined by the ODE system (Figure 1—figure supplement 1A).

One justification for using a Poisson distribution for MOI is a reduction in complexity given a lack of knowledge from empirical data; however, the model can be extended to include an implicit clustering if the Poisson distribution is replaced by an NMD.

Finally, the population-level prevalence is thus the summation of prevalence in individual host classes,

$$
I=\sumi,jI_{i,j}\times(H_{i,j}/\sumH_{i,j})
$$

### MOI-dependent versus MOI-independent rates

The macroparasite modeling approach also impacts how transition rates are calculated, which is different from typical SIR models. Some transition rates of host classes in the ODE system are dependent on the number of parasite infections (i.e., MOI), whereas some are independent of MOI. For example, host natural death rate ($H_{ij}\alpha$) is MOI-independent because the rate itself need not be weighted by an additional factor related to MOI. Accordingly, parasite death rate due to host natural death is $(PW_{ij}+PR_{ij})\alpha$. Alternatively, host drug treatment rate depends on MOI. The value of this rate is explicitly equal to

$$
(G_{i,U}→G_{i,D})=H_{i,U}(t)\sumk=1|i,U∞k⋅p(k)d
$$

where each $k$ is the number of infections in a given host, $p(k)$ is the fraction of hosts having $k$ infections, and $d$ is the fixed treatment rate upon experiencing symptoms. The reason the second term is necessary is to count each separate infection as a different chance to experience symptoms. Given that this term is equal to $r_{i,U}=\frac{PW_{i,U}(t)+PR_{i,U}(t)}{H_{i,U}(t)}$, we get that

$$
(G_{i,U}→G_{i,D})=(PW_{i,U}(t)+PR_{i,U}(t))d
$$

Thus, the movement rates for parasites from untreated classes to drug-treated classes need to consider the host movement rates as well as the number of parasites that are ‘carried’ by the hosts. Using resistant parasites as an example,

$$
(PR_{i,U}→PR_{i,D})=H_{i,U}(t)\sumk=1|i,U∞k⋅d⋅k⋅p(k)=H_{i,U}(t)E(k^{2})d
$$

where $E(k^{2})$ refers to the expectation value of the square of the MOI distribution. Given that this expectation value can be written as $var(k)+(E(k))^{2}$, given the Poisson assumption (which implies that $var(k)$ and $E(k)$ are equal), we finally get an overall rate of

$$
(PR_{i,U}→PR_{i,D})=PR_{i,U}(t)(1+r_{i,U}^{PR})d
$$

where $r_{i,U}^{PR}$ is the mean MOI ($E(k)$) of resistant parasites in the $G_{i,U}$ class.

### Cost of resistance and contributions of wild-type and resistant parasites to transmission

Also calculated using Poisson statistics are the contributions of the two parasite genotypes to transmission originating from a host in a given $G$ class. These contributions are dependent on two fixed cost parameters: the fitness cost to transmission associated with resistance in the absence of sensitive parasites ($s_{single}$, for single-genotype), and the fitness cost to transmission associated with resistance due to competition with wild-type parasites present in the same host ($s_{mixed}$, for mixed-genotype). Parasite density is assumed to be regulated by similar resources within a host (e.g., red blood cells) regardless of MOI. Thus, each strain has a reduced transmissibility when MOI > 1. For wild-type-only infections of MOI = k, each strain has transmissibility of $1/k$; for resistant-only infections, each strain has transmissibility of $1/k⋅(1−s_{single})$; for mixed-genotype infections, if there are $m$ wild-type strains and $n$ resistant strains, transmission from $n$ resistant strains is $\frac{n}{m+n}(1−s_{mixed})$, while transmission from $m$ wild-type strains is $\frac{m}{m+n}+\frac{n}{m+n}s_{mixed}$ assuming wild-type strains outcompete resistant strains in growth rates and reach a higher cumulative density during the infective period.

Based on these assumptions, we then calculate transmissibility contributions at the population level from wild-type strains in purely wild-type infections ($ϕ_{WS,ij}$), wild-type strains in mixed-genotype infections ($ϕ_{WM,ij}$), resistant strains in purely resistant infections ($ϕ_{RS,ij}$), and resistant strains in mixed-genotype infections ($ϕ_{RM,ij}$). Details on how these terms were calculated using Poisson statistics are provided in Appendix 1. The total contributions to transmissibility from resistant and sensitive parasites at a given time step are then

$$
Ω_{W,ij}=ϕ_{WS,ij}+ϕ_{WM,ij}+(ϕ_{RM,ij})(s_{mixed})
$$



$$
Ω_{R,ij}=(ϕ_{RS,ij})(1−s_{single})+(ϕ_{RM,ij})(1−s_{mixed})
$$

These contributions can then be used to determine the realized transmission rates given a transmission potential, as shown in Appendix 1.

### The process of immunity loss

A significant challenge in developing the model is to describe a function for immunity loss for a given class. We adopted the classic equations for the dynamics of acquired immunity boosted by exposure to infection (Eq. 2.5 from Aron, 1983). This gives the following immunity loss rate from a higher generalized immunity class to a lower one:

$$
(G_{i,j}→G_{i−1,j})=h_{i,j}\frac{exp⁡(−\frac{h_{i,j}}{Λ})}{1−exp⁡(−\frac{h_{i,j}}{Λ})}
$$

In this case, $h_{i,j}$ is the sum of the inoculation rate and host death rate for the $G_{i,j}$ class and is determined mechanistically, and $Λ$ is a fixed immunity loss rate parameter with dimensions of $1/[time]$. The second factor in the equation represents the failure of boosting, that is, the probability that an individual is infected after the period of immunity has ended given that they were not infected within the immune state (Aron and May, 1982).

### Drug treatment and resistance invasion

Given each parameter set, we ran the ODE model six times until equilibrium with the following genotypic compositions: (1) wild-type-only scenario with no drug treatment; (2) wild-type-only scenario with 63.2% drug treatment (0.05 daily treatment rate); (3) wild-type-only scenario with 98.2% drug treatment (0.2 daily treatment rate); (4) resistant-only scenario with no drug treatment; (5) resistance invasion with 63.2% drug treatment; and (6) resistance invasion with 98.2% drug treatment. Runs 1–4 start with all hosts in $G_{0,U}$ compartment and 10 parasites. Runs 5 and 6 (resistance invasion) start from the equilibrium state of 2 and 3, with 10 resistant parasites introduced. We then followed the ODE dynamics till the next equilibrium.

### Sources of empirical parameters, measures and policies, and regression analysis

We define transmission potential ($k_{0}$) as effective contact rate via vectors, consistent with a recent immune-structured SIS model that does not explicitly model vector dynamics (de Roos et al., 2023). Specifically, it is the product of vectorial capacity ($C$) (Garrett-Jones, 1964) and the maximum transmissibility between host and mosquito in one transmission cycle ($g$) (Dietz et al., 1974). The transmissibility, $g$, has two components: infectivity of malaria patients to mosquitoes and transmissibility from infected mosquitoes to humans. The infectivity of falciparum malaria patients to mosquitoes was estimated to be around 0.1 from multiple studies (Timinao et al., 2021; Coleman et al., 2004). Transmissibility from infected mosquitoes to naïve hosts is around 0.8 for sporozoites density higher than 1000 per mosquito (Churcher et al., 2005). Thus, we set $g$ to be 0.08 in calculating empirical $k_{0}$. Empirical estimates of vectorial capacities were compiled from all known studies of different countries. Ranges of vectorial capacities, $C$, reported in Table 1 were calculated by summing $C$ of P. falciparum from all the local vectors. Transmission potential ($k_{0}$) for each continent was then obtained by the product of $C$ and $g$.

**Table 1.**
 Empirical ranges of transmission potential ($k_{0}$) of different continents.$k_{0}=C\timesg$, where $g$ is set at 0.08.


<table>
  <thead>
    <tr>
      <th>Continent</th>
      <th>C</th>
      <th>k0</th>
      <th>Source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Africa</td>
      <td>0.54–16.2</td>
      <td>0.043–1.3</td>
      <td>Dietz et al., 1974; Garrett-Jones and Shidrawi, 1969; Afrane et al., 2008</td>
    </tr>
    <tr>
      <td>Asia</td>
      <td>0.014–6.5</td>
      <td>0.0011–0.52</td>
      <td>Rattanarithikul et al., 1996; Rosenberg et al., 1990; Toma et al., 2002; Vythilingam et al., 2003; Zhou et al., 2010; Gunasekaran et al., 2014; Edalat et al., 2016</td>
    </tr>
    <tr>
      <td>Oceania</td>
      <td>1.60–9.64</td>
      <td>0.13–0.77</td>
      <td>Graves et al., 1990</td>
    </tr>
    <tr>
      <td>South America</td>
      <td>0.88–5.53</td>
      <td>0.070–0.44</td>
      <td>Rubio-Palis, 1994; Zimmerman et al., 2022</td>
    </tr>
  </tbody>
</table>

Empirical strain diversities were calculated by the local estimates of var diversity divided by the number of unique non-shared types per strain for each region (Table 2). Note that $var$ diversity in Asia from genomic sequencing was only available for two countries: Thailand and Iran. The variation in strain diversity in Asia might be underestimated.

**Table 2.**
 Empirical ranges of strain diversity of different continents.$u$, unique non-shared types per strain. $D_{var}$ is the Chao1 index (Chao, 1984) estimated from local sampling.


<table>
  <thead>
    <tr>
      <th>Continent</th>
      <th>Dvar</th>
      <th>u</th>
      <th>nstrain</th>
      <th>Source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Africa</td>
      <td>3712–20,000</td>
      <td>50</td>
      <td>74.24–400</td>
      <td>Chen et al., 2011; Day et al., 2017; Ruybal-Pesántez et al., 2022</td>
    </tr>
    <tr>
      <td>Asia</td>
      <td>1100–1700</td>
      <td>25</td>
      <td>44–68</td>
      <td>Tonkin-Hill et al., 2018</td>
    </tr>
    <tr>
      <td>Oceania</td>
      <td>290–1094</td>
      <td>20</td>
      <td>14.5–54.7</td>
      <td>Barry et al., 2007; Tessema et al., 2015</td>
    </tr>
    <tr>
      <td>South America</td>
      <td>113–351</td>
      <td>25</td>
      <td>4.52–14.04</td>
      <td>Albrecht et al., 2010; Rougeron et al., 2017</td>
    </tr>
  </tbody>
</table>

We acquired resistance marker pfcrt 76T frequencies from the Worldwide Antimalarial Resistance Network (WWARN). The website obtained resistant frequencies from 587 studies between 2001 and 2022 with specific curation methodologies. We then extracted geographic sampling locations from the database, and extracted Pf prevalence data estimated from 2- to 10-year-old children from Malaria Atlas Project. The Malaria Atlas Project does not have predicted prevalence before 2000, while the change in first-line antimalarial drugs started around early 2000 in most African countries. We, therefore, restricted our empirical comparisons of equilibrium levels of resistance and prevalence to studies that conducted surveys between 1990 and 2000 and used estimated prevalence from the year 2000 as the proxy for this sampling period. Studies with a host sampling size of less than 20 were excluded. Data sources on drug usage and policies for different countries are summarized in Table 3.

**Table 3.**
 Source of drug policy data.


<table>
  <thead>
    <tr>
      <th>Country</th>
      <th>Citations</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Kenya</td>
      <td>Hemming-Schroeder et al., 2018</td>
    </tr>
    <tr>
      <td>Ghana</td>
      <td>Flegg et al., 2013</td>
    </tr>
    <tr>
      <td>Cambodia</td>
      <td>Delacollette et al., 2009</td>
    </tr>
    <tr>
      <td>Thailand</td>
      <td>Delacollette et al., 2009; Rasmussen et al., 2022</td>
    </tr>
    <tr>
      <td>Papua New Guinea</td>
      <td>Nsanzabana et al., 2010</td>
    </tr>
    <tr>
      <td>Brazil</td>
      <td>Gama et al., 2009</td>
    </tr>
  </tbody>
</table>

The relationship between prevalence and resistant frequency was investigated using beta regression because both the explanatory variable and response variable are proportions, restricted to the unit interval (0,1) (Ferrari and Cribari-Neto, 2004; Simas et al., 2010). Thus, the proper distribution of the response variable (here, resistant prevalence) should be a beta distribution with a mean and precision parameter. Since resistant frequency also has extremes of 0 and 1, we transformed the frequency data to restrict its range between 0 and 1 first so that beta regression still applies,

$$
freq_{adj}=(freq⋅(n−1)+0.5)/n
$$

where $n$ is the sample size (Smithson and Verkuilen, 2006). We then used betareg function from R package 4.2.1 betareg 3.1–4 to perform the regression (Cribari-Neto and Zeileis, 2010).
