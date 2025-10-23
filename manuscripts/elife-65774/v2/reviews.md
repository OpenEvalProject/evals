# Peer review - Round 1

Editors:
- Jos WM van der Meer, Radboud University Medical Centre Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65774.sa1](https://doi.org/10.7554/eLife.65774.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The authors performed a systematic literature review and meta-analysis to develop a dataset of respiratory viral loads (rVLs)for three viruses (SARS-CoV-2, SARS-CoV-1 and influenza A(H1N1)pdm09). Furthermore, the kinetics of viral shedding over time during a respiratory infection are studied, and a model is developed for infectiousness via shedding of viable virus in aerosols and droplets. The study appears robust and comprehensive, and the results are valuable and contribute to the scientific knowledge in this field.

Decision letter after peer review:

Thank you for submitting your article "Heterogeneity in transmissibility and shedding SARS-CoV-2 via droplets and aerosols" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Senior/Reviewing Editor. The following individual involved in review of your submission has agreed to reveal their identity: Lucie Vermeulen (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Summary:

This is a very interesting study on an important subject. It uses a combination of approaches (systematic review, meta-regression, mathematical modelling) to study the association between the variability of respiratory viral loads (rVL) and heterogeneity in transmission rates. The authors argue that variability of rVL is a main determinant of the high heterogeneity of transmission rates and translate the rVL distribution into transmission probabilities for different transmission modes (droplets, aerosols; breathing, speaking, singing). These conclusions are interesting and potentially relevant for public health. The combination of rVL data from >60 studies represents an impressive amount of work which may also be useful for future research.

The paper does not stop at a descriptive summary of these data but uses several modelling approaches (meta-regression, "translation" into transmission probabilities, dynamical modelling) to interpret these data. The evidence provided by these analyses is more tentative than presented by the authors in this version of the manuscript.

Essential revisions:

1. The meta-regression is based on only three viral species and hence it is unclear how generalisable the observed association between rVL and transmission heterogeneity is. In the best case the data show that the three virus species exhibit significantly different rVL-variation, which coincides with their different k values at the epidemiological level. However, this latter association is essentially based on only three data points (i.e. the three viral species). The current meta-regression approach (applying a simple linear regression but essentially ignoring the fact that all studies stem from only three virus species; i.e., ignoring the hierarchical nature of the data) provides p values which strongly exaggerate the degree of evidence.

2. One major potential confounder is the very strong dependence of rVL on infection time. The authors consider this in the section "SARS-CoV 2 kinetics during respiratory infection" where they show also a substantial variation of rVL across different strata of days from symptom onset (DFSO). However, it is unclear to what extent this affects the previous analyses (e.g., the meta-regression models). More fundamentally, the cross-sectional nature of the rVL data leads almost by necessity to an overestimation of the variability in the transmission potential of infections and in a very strong dependency of the rVL variation on the distribution of sampling time. Even a stratification on DFSO can only partly address these problems, firstly because DFSO is in most cases associated with a substantial uncertainty which in the case of a highly dynamic infection will translate into an even larger variation of rVLs. Moreover, even if DFSO were an exact measure of infection time, different infections do not need to be synchronous (e.g. because of stochastic effects or variation of the processes corresponding to the model parameters across individuals) such that different individuals will have their peak rVL at different time points. Taken together this implies that a reliable measure of heterogeneity would require determining something like the area under the curve of rVL (which of course is very challenging).

3. This limitation also strongly affects the practical, public health relevance of the findings. For example, the authors state that "Our analyses suggest that heterogeneity in rVL may be generally associated with over-dispersion for viral respiratory infections. In this case, rVL distribution can serve as an early correlate for transmission patterns, including super-spreading, during outbreaks of novel respiratory viruses, providing insight for disease control before large-scale epidemiological studies empirically characterise k ". This potential application assumes that the timing of rVL measurements is known early in a pandemic and that it can be controlled for, which requires a detailed knowledge of the within patient dynamics of the virus. I would assume that achieving this knowledge would take at least as long as estimating k in epidemiological studies. Thus it may be more appropriate to think about the two approaches in characterising heterogeneity as complementary (in the context of epidemiological triangulation; i.e. both approaches having their weaknesses and biases but which can be overcome in a joint consideration; generally, I think that attempting to achieve such a triangulation is one of the main strengths of the present study, despite its limitations).

4. The variation of rVL might also be strongly driven by the sampling method/procedure (even the same method will give very different results across health-care workers), which implies the same problems as (2) – i.e. overestimation of rVL variability and potential confounding.

5. The authors note that "Talking, singing and coughing expelled virions at greater proportions via droplets (80.6-86.0%) than aerosols (14.0-19.4%)." It should be noted that although more virions are expelled via droplets than aerosols according to the findings of this study, exposure to droplets and aerosols is not equal and this could affect the probability of transmission via these routes. For example, if social distancing and masking is observed then it is possible that larger droplets are more easily captured by masks or fall on the ground quickly and do not reach a susceptible individual, while aerosols do. Furthermore, smaller droplets and aerosols can penetrate more deeply into the lungs. It is as of yet unclear whether this would influence the probability of becoming (more severely) infected. This may also differ per virus. A discussion on these issues is relevant.

6. The authors also note that their results "support aerosol spread as a transmission mode for SARS-CoV-2, including for conditional superspreading by highly infectious cases. However, with short durations of stay in well-ventilated areas, the exposure risk for aerosols, including long-range and buoyant ones, remains correlated with proximity to infectious cases."

7. A methodological note on the modelling that may affect the results (but likely do not impact the conclusions strongly) is the following.

The authors take a value of 0.1% for the fraction of SARS-CoV-2 RNA copies that represents viable virus (parameter 𝛾). This value is quite uncertain. More literature (not yet peer-reviewed) exists on the fraction of SARS-CoV-2 RNA copies that is infectious virus, providing different values. Van Kampen et al. (2020) only found a cytopathic effect on Vero cells if the swab sample from patients contained more than 7 log10 RNA copies/mL. Fears et al. (2020) find an average of 0.003 (range 0.0008 – 0.02) CCID50/RNA copy. However, Lednicky et al. (2020) sampled SARS-CoV-2-containing aerosols in a room with COVID-19 patients with air samplers using a water vapor condensation mechanism and as such collect virus particles without damaging them, and found an average of 0.6 CCID50/RNA copy, much higher. The model is likely sensitive to this parameter, and this could influence the result. These issues should be taken into account in the revision.

8. Another methodological point is that more datasets in literature are available on the emission rates and size distribution of particles during breathing, speaking, coughing etc., than are currently used to base the model on. Schijven et al. (2020) compared seven datasets and found that they sometimes differ quite strongly. For example, the median volume of aerosol particles produced for coughing differs over two orders of magnitude when comparing two data sets. It is unclear what this difference represents, it might have to do with the sampling method. Furthermore, observed size distributions also differ in literature, with peak particle emission rates at different sizes. The authors should be aware that the choice of particle emission data for their study can impact their results strongly, and including discussion on the choice of data set and the implications on the results is warranted.

9. Taking 0.5 for the evaporation diameter factor is probably too large. Liu et al. (2017) find a value around one third for respiratory droplets from coughing, and the recent study on the evaporation of saliva droplets and aerosols by Lieber et al. (2021) find a value of 0.2 (for a range of temperature of 20-29 degrees C, and range of relative humidity of 6 – 65%). This likely matters for the result, as the difference between 0.5 and 0.2 leads to a factor ~15 change in droplet volume.

10. The kinetic model assumes that viral replication is controlled by the reduction of target cells over the course of the infection, but it neglects the effect of the immune system. This seems a rather strong assumption. What is the evidence for this in the case of SARS-CoV2? Also, it would be good if the authors could comment on the identifiability of the model parameters- especially the high uncertainty of the half-life of SARS-CoV2 in the respiratory tract (2.62-66hours) suggests that this might be a problem.

Additional points:

11. Line 453-454: "log 𝑘 = 𝑎(𝑆𝐷) + 𝑏, where 𝑎 is the slope for association and 𝑏 is the intercept". This appears to be a strange notation for this equation, isn't "a*SD + b" more logical?

12. Line 544-545: "To estimate the average duration of shedding, we extrapolated the model to 0 log10 copies/ml post-symptom onset." If the tail of the model is very long, it might take a very long time to reach 0 log10. Is this the case? And if yes, is perhaps a 95% decrease compared to the maximum a better measure for the duration of shedding?

13. Line 560: Is this unit correct? "𝜌 is the material density of the respiratory particle (997 g/m3)" Shouldn't this density be in kg/m3?

14. Line 563 – 571: The estimate for 𝛾 for SARS-CoV-2 could turn out to be higher, if Lednicky et al. (2020) are to be believed. In any case, this warrants some further discussion in the paper, as the results are probably quite sensitive to this parameter!

15. Line 609 – 610: "𝜌 is the material density of the respiratory particle (taken to be 1 g/cm3 based on the composition of dehydrated respiratory particles)". What is the reference for this statement? Zhang et al. (2011) find densities between 1.25 and 1.62 g/mL (Table 2). It seems logical that the drying process increases the density somewhat as compared to the density of water, as for instance the heavier salts do not evaporate.

16. Figure 2: this figure is somewhat unclear, maybe I do not understand it correctly. Why does one study have multiple standard deviations? And as there are only three values of k, regression seems to be an odd choice. A comparison between different groups of k seems more appropriate?

References:

Fears AC, Klimstra WB, Duprex P, Hartman A, Weaver SC, Plante KS, et al. 2020. Comparative dynamic aerosol efficiencies of three emergent coronaviruses and the unusual persistence of sars-cov-2 in aerosol suspensions. medRxiv:2020.2004.2013.20063784.

Lednicky JA, Lauzardo M, Fan ZH, Jutla AS, Tilly TB, Gangwar M, et al. 2020. Viable sars-cov-2 in the air of a hospital room with covid-19 patients. medRxiv:2020.2008.2003.20167395.

Lieber, C., Melekidis, S., Koch, R., Bauer, H.-J., 2021. Insights into the evaporation characteristics of saliva droplets and aerosols: Levitation experiments and numerical modeling. Journal of Aerosol Science 154, 105760.

Liu, L., Wei, J., Li, Y., Ooi, A., 2017. Evaporation and dispersion of respiratory droplets from coughing. Indoor Air 27, 179-190.

Schijven, J.F., Vermeulen, L.C., Swart, A., Meijer, A., Duizer, E., de RodaHusman, A.M., 2020. Exposure assessment for airborne transmission of SARS-CoV-2 via breathing, speaking, coughing and sneezing. medRxiv, 2020.2007.2002.20144832.

van Kampen JJA, van de Vijver DAMC, Fraaij PLA, Haagmans BL, Lamers MM, Okba N, et al. 2020. Shedding of infectious virus in hospitalized patients with coronavirus disease-2019 (covid-19): Duration and key determinants. medRxiv: 2020.2006.2008. 20125310.

Zhang, T., 2011. Study on Surface Tension and Evaporation Rate of Human Saliva, Saline, and Water Droplets. West Virginia University,
