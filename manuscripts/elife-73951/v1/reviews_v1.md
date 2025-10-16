# Peer review - Round 1

Editors:
- Jonathan K Pritchard, Stanford University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73951.sa0](https://doi.org/10.7554/eLife.73951.sa0)

The authors describe their work on an atlas of associations between polygenic scores for 125 different traits representing a variety of quantitative phenotypes and diseases, and a large set of metabolites measured in up to 83,000 participants in the UK Biobank. These associations are all available via a public browser, and may be used to identify candidate intermediate phenotypes, as well as potential biomarkers of disease.


---

# Peer review - Round 1

Editors:
- Jonathan K Pritchard, Stanford University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73951.sa1](https://doi.org/10.7554/eLife.73951.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Constructing an atlas of associations between polygenic risk scores from across the human phenome and circulating metabolic biomarkers" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Carlos Isales as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Scott Ritchie (Reviewer #2); Maik Pietzner (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) While this work provides a potentially important resource for the community, the examples provided tend to be illustrative, and do not really do justice to the resource. We strongly encourage the authors to revisit the data analysis for more-compelling examples of the types of impactful work that can be achieved using this resource. How and why should users want to use this Atlas?

2) One key question is whether these analyses bring us closer to causality compared to 'classical' observational associations, given LD confounding and strong metabolite variants included in PRS driving the associations. For example, how robust are PRS associations to the exclusion of individual regions? Second, can we determine whether the associations are causally upstream, or downstream of the identified phenotypes? At minimum the authors should demonstrate for examples how these issues can be teased apart (and optionally provide analyses atlas-wide).

3) The atlas would also be potentially strengthened by including additional results for sex-stratified models. Previous work has shown significant differences in NMR biomarker concentrations between males and females, so it would be valuable to see if these result in any differences in PRS associations which may arise despite PRSs largely being constructed from autosomal GWAS.

Furthermore, the reviewers provide numerous additional specific and insightful comments; we strongly encourage the authors to consider these points seriously in their revisions.

Reviewer #1 (Recommendations for the authors):

Specific comments:

Some of the text on figures is very small and it may be worth revisiting figure design.

P8: the positive control of creatinine and kidney disease seems a bit too trivial, given that creatinine is a diagnostic criterion. Perhaps there may be a better example?

P7 Para1: It would be helpful to the reader to say a bit more about the range of types of traits considered here, as well as typical sample sizes given that the data come from a variety of sources.

Consider using PGS instead of PRS as more accurate for quantitative and non-disease traits.

Reviewer #2 (Recommendations for the authors):

Introduction/discussion: this is not the first study that has demonstrated the utility of PRS associations for prioritising molecular traits for follow-up. We have recently published a paper doing so for cardiometabolic PRS and protein levels (Ritchie et al., 2021a) and this has been available as a preprint in various forms since 2019. This should be noted and cited appropriately at the relevant points in the introduction and discussion.

The associations in the atlas for the systolic blood pressure (SBP) and diastolic blood pressure (DBP) are invalid. As the authors note in the methods, PRSs for these two traits are constructed from GWAS that include UK Biobank samples. PRSs are invalid when used in samples that contributed to their underlying GWAS (Lambert et al., 2021; Wand et al., 2021; Wray et al., 2013) as this causes them to have dramatically inflated associations. Associations for these two PRS should be removed from the atlas and study, or if the authors think these two traits are of critical interest, an alternate source of GWAS that do not include UK Biobank participants should be used to construct these two PRSs.

We have found significant sources of technical variation exist in the NMR metabolomics data for UK Biobank (Ritchie et al., 2021b), which may confound some of the PRS associations here. Of particular concern in the context of this study are the presence of outlier shipping plates, on which samples have systematically high (or low) concentrations of non-biological origin (see Figure 5 in Ritchie et al. 2021b). This affects up to 5% of samples depending on the biomarker, but will have an outsized effect on associations as they result in samples being spuriously located at the extremities of biomarker distributions. I.e. this may result in associations being weaker or not significant, or less likely, false positives may be introduced if outlier plates happen to correlate with PRS. There are also a small number of biomarkers significantly impacted by other sources of technical variation, e.g. drift over time within spectrometer, or sample degradation due to extended time between sample preparation and sample measurement. We have made available an R package: ukbnmr (https://github.com/sritchie73/ukbnmr), for correcting for this technical variation, and removing samples on these outlier plates. Although this preprint is still under review, we would suggest using this package to remove the described technical variation, or at least checking whether doing so significantly changes associations in the atlas.

There are also major biological determinants of NMR biomarker concentrations that have not been accounted for, and thus may confound, PRS to biomarker associations. In addition to age, sex, and 10 genetic principal components that the authors already adjust for, NMR biomarker concentrations are also strongly correlated with body mass index (BMI), fasting time, and lipid lowering medication (statin) usage (see Figure 8 in Ritchie et al., 2021b). The atlas would be greatly improved by either appropriately accounting for these in the basic models, or including additional results using models that do so.

Regarding statin usage in particular, we appreciate that the authors have conducted a separate age-stratified analysis to evaluate the impact of medication usage on PRS to biomarker associations. However, the fact remains that statin usage will be confounding the PRS to biomarker associations in the main results (e.g. by artificially lowering LDL cholesterol in people at high CHD PRS). This confounding is typically removed in one of two ways: either (1) fitting associations excluding participants taking statins, or (2) applying biomarker-specific correction factors to concentrations prior to association analysis, such as those estimated by (Kofink et al., 2017; Sliz et al., 2018). The latter is probably the better approach as the former is likely to introduce further bias towards young and healthy participants.

The atlas would also be potentially strengthened by including additional results for sex-stratified models. We have observed significant differences in NMR biomarker concentrations between males and females, so it would be interesting to see if these result in any differences in PRS associations which may arise despite PRSs largely being constructed from autosomal GWAS.

Regarding the bi-directional Mendelian randomization analysis of GlycA, we would suggest using an alternative biomarker as exemplar in the study, as GlycA is heterogeneous and needs to be more carefully instrumented than has been done in the study currently. GlycA is an NMR signal that quantifies the total concentrations of five proteins in circulation (Otvos et al., 2015): α-1-acid glycoprotein (AGP), α-1-antitrypsin (AAT), α-1-antichymotrypsin (AACT), haptoglobin (HP), and transferrin (TF). These are acute-phase reactants whose concentrations each change in response to acute inflammation or in chronic inflammation (Connelly et al., 2017). Moreover these changes are differential with respect to each other, and over time (Ebersole and Cappelli, 2000; Gabay and Kushner, 1999). Further, a single GlycA measurement cannot be simply decomposed as two people with the same GlycA concentration can have different concentrations of the underlying proteins (Ritchie et al., 2019). This heterogeneity means that using genome-wide significant QTLs for GlycA is unlikely to be appropriate as these QTLs may include (1) protein-QTLs for one or more of the five proteins GlycA captures, and (2) signals involved in initiation of acute-phase response (e.g. interleukin-6 signalling pathways). To use GlycA as an exposure in Mendelian randomization analysis, the QTLs selected as instruments should be restricted to cis-pQTLs for the five proteins. These signals may need to be treated separately, as in the scenario GlycA is truly causal, it is unlikely that all five proteins are causal, or that they have similar causal effect sizes.

Data availability: the PRS should also be made publicly available, e.g. downloadable via the atlas. These should include at minimum: the set of variants in each PRS, variant identifier information (e.g. chromosome and position), genome build, effect allele, and weight (β or log odds from the underlying GWAS).

References

Bretherick AD, Canela-Xandri O, Joshi PK, Clark DW, Rawlik K, Boutin TS, Zeng Y, Amador C, Navarro P, Rudan I, Wright AF, Campbell H, Vitart V, Hayward C, Wilson JF, Tenesa A, Ponting CP, Baillie JK, Haley C. 2020. Linking protein to phenotype with Mendelian Randomization detects 38 proteins with causal roles in human diseases and traits. PLoS Genet 16:e1008785.

Bycroft C, Freeman C, Petkova D, Band G, Elliott LT, Sharp K, Motyer A, Vukcevic D, Delaneau O, O'Connell J, Cortes A, Welsh S, Young A, Effingham M, McVean G, Leslie S, Allen N, Donnelly P, Marchini J. 2018. The UK Biobank resource with deep phenotyping and genomic data. Nature 562:203-209.

Connelly MA, Otvos JD, Shalaurova I, Playford MP, Mehta NN. 2017. GlycA, a novel biomarker of systemic inflammation and cardiovascular disease risk. J Transl Med 15:219.

Ebersole JL, Cappelli D. 2000. Acute-phase reactants in infections and inflammatory diseases. Periodontol 2000 23:19-49.

Gabay C, Kushner I. 1999. Acute-phase proteins and other systemic responses to inflammation. N Engl J Med 340:448-454.

Kofink D, Eppinga RN, van Gilst WH, Bakker SJL, Dullaart RPF, van der Harst P, Asselbergs FW. 2017. Statin Effects on Metabolic Profiles: Data From the PREVEND IT (Prevention of Renal and Vascular End-stage Disease Intervention Trial). Circ Cardiovasc Genet 10. doi:10.1161/CIRCGENETICS.117.001759

Lambert SA, Gil L, Jupp S, Ritchie SC, Xu Y, Buniello A, McMahon A, Abraham G, Chapman M, Parkinson H, Danesh J, MacArthur JAL, Inouye M. 2021. The Polygenic Score Catalog as an open database for reproducibility and systematic evaluation. Nat Genet 53:420-425.

Otvos JD, Shalaurova I, Wolak-Dinsmore J, Connelly MA, Mackey RH, Stein JH, Tracy RP. 2015. GlycA: A Composite Nuclear Magnetic Resonance Biomarker of Systemic Inflammation. Clin Chem 61:714-723.

Ritchie SC, Kettunen J, Brozynska M, Nath AP, Havulinna AS, Männistö S, Perola M, Salomaa V, Ala-Korpela M, Abraham G, Würtz P, Inouye M. 2019. Elevated serum α-1 antitrypsin is a major component of GlycA-associated risk for future morbidity and mortality. PLoS One 14:e0223692.

Ritchie SC, Lambert SA, Arnold M, Teo SM, Lim S, Scepanovic P, Marten J, Zahid S, Chaffin M, Liu Y, Abraham G, Ouwehand WH, Roberts DJ, Watkins NA, Drew BG, Calkin AC, Di Angelantonio E, Soranzo N, Burgess S, Chapman M, Kathiresan S, Khera AV, Danesh J, Butterworth AS, Inouye M. 2021a. Integrative analysis of the plasma proteome and polygenic risk of cardiometabolic diseases. Nat Metab 3:1476-1483.

Ritchie SC, Surendran P, Karthikeyan S, Lambert SA, Bolton T, Pennells L, Danesh J, Di Angelantonio E, Butterworth AS, Inouye M. 2021b. Quality control and removal of technical variation of NMR metabolic biomarker data in ∼120,000 UK Biobank participants. medRxiv. doi:10.1101/2021.09.24.21264079

Sliz E, Kettunen J, Holmes MV, Williams CO, Boachie C, Wang Q, Männikkö M, Sebert S, Walters R, Lin K, Millwood IY, Clarke R, Li L, Rankin N, Welsh P, Delles C, Jukema JW, Trompet S, Ford I, Perola M, Salomaa V, Järvelin M-R, Chen Z, Lawlor DA, Ala-Korpela M, Danesh J, Davey Smith G, Sattar N, Butterworth A, Würtz P. 2018. Metabolomic consequences of genetic inhibition of PCSK9 compared with statin treatment. Circulation 138:2499-2512.

Wand H, Lambert SA, Tamburro C, Iacocca MA, O'Sullivan JW, Sillari C, Kullo IJ, Rowley R, Dron JS, Brockman D, Venner E, McCarthy MI, Antoniou AC, Easton DF, Hegele RA, Khera AV, Chatterjee N, Kooperberg C, Edwards K, Vlessis K, Kinnear K, Danesh JN, Parkinson H, Ramos EM, Roberts MC, Ormond KE, Khoury MJ, Janssens ACJW, Goddard KAB, Kraft P, MacArthur JAL, Inouye M, Wojcik GL. 2021. Improving reporting standards for polygenic scores in risk prediction studies. Nature 591:211-219.

Wray NR, Yang J, Hayes BJ, Price AL, Goddard ME, Visscher PM. 2013. Pitfalls of predicting complex traits from SNPs. Nat Rev Genet 14:507-515.

Zheng J, Haberland V, Baird D, Walker V, Haycock PC, Hurle MR, Gutteridge A, Erola P, Liu Y, Luo S, Robinson J, Richardson TG, Staley JR, Elsworth B, Burgess S, Sun BB, Danesh J, Runz H, Maranville JC, Martin HM, Yarmolinsky J, Laurin C, Holmes MV, Liu JZ, Estrada K, Santos R, McCarthy L, Waterworth D, Nelson MR, Davey Smith G, Butterworth AS, Hemani G, Scott RA, Gaunt TR. 2020. Phenome-wide Mendelian randomization mapping the influence of the plasma proteome on complex diseases. Nat Genet 52:1122-1131.

Reviewer #3 (Recommendations for the authors):

I have the following more specific comments that could possibly improve the study by Fang et al.:

1. The NMR platform used by the authors measures only a small number of small molecules and the vast majority of the derived measures refer to characteristics of lipoprotein particles, which are not 'classical' metabolites. The paper would benefit from a paper distinction between both measures. Therefore, it is questionable how many of the 100,000 metabolites mentioned by the authors are captured by the technology used and further it is even of interest how many approximately independent features are indeed captured by the technology. A principal component analysis or similar dimension reduction techniques would provide an important correction/estimate of/to the metabolic space captured. Given the high correlation among the NMR traits, it would be important to state how many likely independent associations have been found, for instance by clumping highly correlated metabolites in clusters, similar as the authors do for SNPs.

2. I find the section about collider bias in the introduction a bit as surprise and it is unclear to me, how this relates to the overall aim of the study. The high amount of self-citation in this section and in general throughout the paper makes me wonder, how much of an issue this really is compared to more substantial questions about the suitability of PRS to identify disease biomarkers or causal metabolites.

3. Investigating different types of genetic scores is a clear strength of this work. However, the study currently stops early leaving important questions unanswered. For instance, how many more 'helpful' associations between PRS and NMR measures are really gained by going genome-wide, that is, how many of the added associations are mainly due to unspecific pleiotropy? The authors have outstanding methodological skills in MR and related causal inference techniques, and I find it somewhat wasted here to go simply for more associations instead of digging into the relevant part, which in turn defines the usefulness of the whole atlas and hence this study. It currently reads mostly like a computational exercise.

4. In my opinion, the key question is, what do all those associations deliver, do they bring us any closer to causality compared to 'classical' observational associations, given LD confounding and strong metabolite variants included in PRS driving the associations. For example, how robust are PRS associations to the exclusion of single regions, Ritchie et al., 2021 Nat Metab provide a neat framework to address such questions. The APOE example goes in that direction and other locus-specific effects are likely underlying other disease PRS – NMR measure associations.

5. One might argue that the CKD example is somewhat self-fulling, given that the selection of cases is mainly done based on serum creatinine (or the eGFR derived from creatinine), but is a good example how strong and specific examples might point to disease biomarkers. Are there more examples for a given NMR trait being strongly and possibly specifically associated with a trait or a cluster of highly related traits? I would also tone the creatinine example done, since it is obvious that this marker is used for clinical decision making.

6. I am not quite sure about the bidirectional MR approach. By only testing diseases for which the PRS showed an association with the metabolite of interest, isn't it quite likely that an effect of the metabolite on the disease would be missed, as one would assume that a true causal association between a metabolite and a disease might well be lost in the large set of SNPs associated with the endpoint of interest.

7. I disagree with the statement on page 12 that all lipid traits associated with the CHD PRS are causal risk factors, most of them are likely not and the true underlying risk factor or biological mechanism is likely hidden among all those associations. The general inability to distinguish about the causal relevance of all those highly related measures is a massive challenge working with NMR data, in particular given that many are not real measurements but are only derived as proportion from other measures, including apolipoprotein B.

8. The authors need to do better in distinguishing between all the different lipid measures that are derived from the NMR platform, this is also seen in the discussion of Apo B. Apo B is the main structural protein for many lipoprotein particles of different densities and not just for atherogenic ones.

9. Instead of stratified analysis, why not correcting for statin intake to estimate lipid levels of participants without the use of statins? What about the effect of many other medications widely prescribed, with strong effects on NMR measures as described in van Duijn et al., Nat Med 2020?
