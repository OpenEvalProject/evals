# Feedback inhibition by a descending GABAergic neuron regulates timing of escape behavior in Drosophila larvae

## Authors

- Jiayi Zhu<sup>1</sup>
- Jean-Christophe Boivin<sup>1</sup>
- Alastair Garner<sup>1</sup>
- Jing Ning<sup>1</sup>
- Yi Q Zhao<sup>1</sup>
- Tomoko Ohyama<sup>1</sup> ([ORCID: 0000-0003-1697-1138](https://orcid.org/0000-0003-1697-1138)) †

### Affiliations

1. Department of Biology, McGill University Montreal Canada ([ROR:01pxwe438](https://ror.org/01pxwe438))
2. Integrated Program of Neuroscience, McGill University Montreal Canada ([ROR:01pxwe438](https://ror.org/01pxwe438))
3. Alan Edwards Center for Research on Pain, McGill University Montreal Canada ([ROR:01pxwe438](https://ror.org/01pxwe438))

† Corresponding author

## Abstract

Escape behaviors help animals avoid harm from predators and other threats in the environment. Successful escape relies on integrating information from multiple stimulus modalities (of external or internal origin) to compute trajectories toward safe locations, choose between actions that satisfy competing motivations, and execute other strategies that ensure survival. To this end, escape behaviors must be adaptive. When a Drosophila melanogaster larva encounters a noxious stimulus, such as the focal pressure a parasitic wasp applies to the larval cuticle via its ovipositor, it initiates a characteristic escape response. The escape sequence consists of an initial abrupt bending, lateral rolling, and finally rapid crawling. Previous work has shown that the detection of noxious stimuli primarily relies on class IV multi-dendritic arborization neurons (Class IV neurons) located beneath the body wall, and more recent studies have identified several important components in the nociceptive neural circuitry involved in rolling. However, the neural mechanisms that underlie the rolling-escape sequence remain unclear. Here, we present both functional and anatomical evidence suggesting that bilateral descending neurons within the subesophageal zone of D. melanogaster larva play a crucial role in regulating the termination of rolling and subsequent transition to escape crawling. We demonstrate that these descending neurons (designated SeIN128) are inhibitory and receive inputs from a second-order interneuron upstream (Basin-2) and an ascending neuron downstream of Basin-2 (A00c). Together with optogenetic experiments showing that co-activation of SeIN128 neurons and Basin-2 influence the temporal dynamics of rolling, our findings collectively suggest that the ensemble of SeIN128, Basin-2, and A00c neurons forms a GABAergic feedback loop onto Basin-2, which inhibits rolling and thereby facilitates the shift to escape crawling.

## Introduction

Virtually all organisms on earth face the threat of being maimed or killed by one or more predatory organisms. Not surprisingly, when organisms encounter threat-associated stimuli, they exhibit a wide variety of escape responses appropriate to their biological construction and the specific predators within their ecological niche (Burrell, 2017; Campagner et al., 2023; Chin and Tracey, 2017; Im and Galko, 2012; Peirs and Seal, 2016). Typically, these escape responses consist of a sequence of simple actions. The roundworm C. elegans, for example, in response to a touch to its head, exhibits rapid backward locomotion coupled with a suppression of head movements, followed by a deep ventral bend (omega turn) and a 180 degree reversal in the direction of locomotion. This sequence allows the roundworm to escape from nematophagal fungi that cohabitate with it in organic debris (Chalfie and Sulston, 1981; Chalfie et al., 1985).

When Drosophila melanogaster larvae encounter noxious stimuli, such as the stimulation that accompanies an attempt by a parasitic wasp to penetrate the larval cuticle with its ovipositor, they exhibit an escape response consisting of an initial abrupt bending, followed by lateral rolling, and finally, rapid crawling (Hwang et al., 2007; Ohyama et al., 2015; Onodera et al., 2017; Tracey et al., 2003). Previous work has shown that noxious stimuli are primarily detected by class IV dendritic arborization neurons (Class IV neurons) located beneath the body wall (Tracey et al., 2003). More recent studies have identified several important components in the downstream nociceptive neural circuitry, particularly those involved in rolling (Burgos et al., 2018; Dason et al., 2020; Hu et al., 2017; Hu et al., 2020; Imambocus et al., 2022; Kaneko et al., 2017; Ohyama et al., 2015; Takagi et al., 2017; Yoshino et al., 2017). To date, however, the neural mechanisms that underlie the rolling-escape sequence, notably, the transition from rolling to crawling, have remained unclear.

In this study, we provide both functional and anatomical evidence that, bilateral descending neurons in the subesophageal zone (SEZ) of D. melanogaster larva, which comprise part of a neural circuit underlying rolling, a characteristic nocifensive escape response, potentially regulate the termination of rolling and subsequent transition to escape crawling. We show that these descending neurons, which we designate as SeIN128, are identical to those denoted previously as SS04185 (Ohyama et al., 2015), are inhibitory neurons that receive inputs from Basin-2 (a second-order interneuron upstream) and A00c (an ascending neuron downstream of Basin-2), and provide GABAergic feedback onto Basin-2. Together with behavioral analyses of rolling during systematic optogenetic manipulation of SeIN128 and Basin-2 activity, our findings suggest that an ensemble of neurons—SeIN128, Basin-2, and A00c—forms an inhibitory feedback circuit that inhibits rolling, which in turn facilitates the shift to escape crawling.

## Results

### SS04185 facilitates rolling termination and shortens the latency of crawling behavior in the escape responses

In a previous study, we showed that activation of all Basin neurons (Basin-1, -2, -3, and -4) induced rolling followed by fast crawling (Figure 1A–D; Ohyama et al., 2015). Here, we first examined whether optogenetic activation of all four Basins expressing the red-shifted opsin CsChrimson (using Basin-1–4 Gal4, i.e., R72F11-Gal4) could elicit the same behavior. Upon activation of all Basins, we observed rolling mostly within the first 5 s, followed by crawling (Figure 1B (top panel), Figure 1C, D). The crawling speed during activation of all Basins following rolling was ~1.5 times that of the crawling speed at baseline (Figure 1D; Ohyama et al., 2015).

![Figure 1.](https://cdn.elifesciences.org/articles/93978/elife-93978-fig1-v1.jpg)

**Figure 1.:** (A) Schematic of Drosophila larval escape behavior sequence. (B) Ethograms of Basin activation (top panel) and co-activation of SS04185 and Basins (bottom panel). Each row represents an individual larva. Pink, blue, green, orange, and purple lines represent bouts of rolling, turning, crawling, backward crawling, and hunching. The red bar and dashed lines indicate the time window during which neural activation was present. Genotypes: 20xUAS-IVS-CsChrimson::mVenus/+;+; R72F11-Gal4/+ (top); 20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/ R72F11-Gal4 (bottom). Genotypes in (C, D, F–I) are the same as those mentioned here. (C) Time series of larval crawling speed during co-activation of SS04185 and Basins (red) and activation of Basins alone (black). Shaded areas represent the standard error. The red bar and dashed lines denote the optogenetic stimulation window. (D) Time series of rolling probabilities of larvae during co-activation of SS04185 and Basins (red) and activation of Basins alone (black). Shaded areas represent 95% confidential intervals for rolling probabilities. The red bar and dashed lines denote the optogenetic stimulation window. (E) Rolling probabilities of larvae with activation of different neurons. Error bars represent the 95% confidence interval. Genotypes from left to right: (1) 20xUAS-IVS-CsChrimson::mVenus/+;;, (2) 20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/+, (3) 20xUAS-IVS-CsChrimson::mVenus/+;; R72F11-Gal4/+, and (4) 20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/ R72F11-Gal4. n = 120, 118, 231, 155 from left to right. Statistics: Chi-square test, χ2 = 0, p > 0.05 for the first two groups; χ2 = 83.85, p < 0.001 for the last two groups; and χ2 = 365.51, p < 0.001 for the comparison between the first two groups and the last two groups. (F) Cumulative plot of rolling duration. Statistics: Mann–Whitney U test, p < 0.001, n = 652, 120. (G) A violin plot showing start of first rolling bout for each larva during stimulation. Statistics: Mann–Whitney U test, p = 0.027, n = 225, 89. (H) A violin plot displaying end of first rolling bout for each larva during stimulation. Statistics: Mann–Whitney U test, p < 0.001, n = 225, 89. (I) A violin plot presenting start of first crawling bout for each larva during stimulation. Statistics: Mann–Whitney U test, p < 0.001, n = 214, 70. ***p < 0.001.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/93978/elife-93978-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) Crawling probabilities of larvae with the activation of SS04185-expressing neurons. Error bars, 95% confidence interval. Genotypes: 20xUAS-IVS-CsChrimson::mVenus/+;; (black); 20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/+ (red). Genotypes in (B–D) are the same as shown here. n = 308, 172. Statistics: Chi-square test, χ2 = 2.32, p > 0.05. (B) Turning probabilities of larvae with activation of SS04185-expressing neurons. Error bars, 95% confidence interval. n = 308, 172. Statistics: Chi-square test, χ2 = 1.77, p > 0.05. (C) Hunching probabilities of larvae with activation of SS04185-expressing neurons. Error bars, 95% confidence interval. n = 308, 172. Statistics: Chi-square test, χ2 = 0.35, p > 0.05. (D) Stopping probabilities of larvae with activation of SS04185-expressing neurons. Error bars, 95% confidence interval. n = 308, 172. Statistics: Chi-square test, χ2 = 3.97, p = 0.046. (E) A violin plot of total time spent rolling for each individual larva during stimulation. Statistics: Mann–Whitney U test, p < 0.001, n = 225, 89. (F) Time series of crawling probabilities of SS04185 and Basin co-activation larvae (green) and Basin activation only larvae (black). Shaded areas show 95% confidential intervals of the crawling probabilities. Dashed lines display the window of optogenetic stimulation. Genotypes: 20xUAS-IVS-CsChrimson::mVenus/+; +; R72F11-Gal4/+ (control); 20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/R72F11-Gal4 (SS04185). Genotypes in (G–H) are the same as mentioned here. n = 228, 124. (G) A violin plot of interval between first roll and next crawl. Statistics: Mann–Whitney U test, p > 0.05, n = 151, 74. (H) Crawling probabilities of SS04185 and Basin co-activation larvae (red) and Basin activation only larvae (black). Error bars, 95% confidence interval. n = 228, 124. Statistics: Chi-square test, χ2 = 28.36, p < 0.001. (I) A violin plot of crawling speed ratio of larvae with null, SS04185 neuron, Basin, SS04185 neuron and Basin activation (from left to right). Crawling speed ratio = crawling speed 5–10 s after stimulation onset/crawling speed 0–5 s before stimulation onset. Statistics: Kruskal–Wallis test: H = 144, p < 0.001; Bonferroni-corrected Mann–Whitney U test: p > 0.05 for two groups on the left and two groups on the right. n = 308, 172, 227, 124. Genotypes from left to right: (1) 20xUAS-IVS-CsChrimson::mVenus/+;;; (2) 20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/+; (3) 20xUAS-IVS-CsChrimson::mVenus/+;; R72F11-Gal4/+; (4) 20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/R72F11-Gal4. ***p < 0.001.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/93978/elife-93978-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** (A) Time series of rolling probabilities of larvae during co-activation of SS04185 and Basins (red) and activation of Basins alone (black). Shaded areas represent 95% confidential intervals for rolling probabilities. The red bar and vertical dashed lines denote the optogenetic stimulation window. Genotypes: (1) 20xUAS-IVS-CsChrimson::mVenus/+;; R72F11-Gal4/+ (control), (2) 20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R72F11-Gal4/+ (54B01-AD), (3) 20xUAS-IVS-CsChrimson::mVenus/+;; R72F11-Gal4/R46E07-Gal4.DBD (46E07-DBD), and (4) 20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/ R72F11-Gal4 (SS04185). Genotypes in (B, C) are the same as mentioned here. n = 162, 209, 103, 153. (B) Rolling probabilities of larvae plotted in (A) in the first 5 s of stimulation. Error bars represent the 95% confidence interval. n = 162, 209, 103, 153 from left to right. Statistics: Chi-square test, χ2 = 6.66, p > 0.05 for the left three groups and χ2 = 72.52, p < 0.001 for the comparison between the left three groups and the SS04185 group. (C) A violin plot of total time spent rolling for each individual larva during stimulation. Statistics: Kruskal–Wallis test: H = 105.99, p < 0.001; Bonferroni-corrected Mann–Whitney U test, p > 0.05 for the comparison between control and 54B01-AD; p < 0.001 for all other pairwise comparisons, n = 151, 172, 100, 86. ***p < 0.001.

To identify the neurons responsible for escape behavior (rolling and/or fast crawling), we conducted a behavioral screening of ~250 split Gal4 lines that were labeled in the central nervous system (CNS) when co-activated with all Basins. With respect to rolling, we found that activation of the split-Gal4 line, SS04185 (i.e., w1118; R54B01-Gal4AD; R46E07-Gal4DBD), significantly reduced the probability of rolling when compared to activating only the Basins (Figure 1B, C, E, Videos 1 and 2) without affecting the crawling speed during stimulation (Figure 1D).

![Video 1.](https://cdn.elifesciences.org/articles/93978/elife-93978-video1.mp4.jpg)

**Video 1.:** Activation of Basins alone evokes protracted rolling followed by turning/crawling.

![Video 2.](https://cdn.elifesciences.org/articles/93978/elife-93978-video2.mp4.jpg)

**Video 2.:** Co-activation of SS04185 and Basins evokes only brief rolling followed by turning/crawling.

The likelihood of rolling upon co-activation of SS04185 neurons and Basins might decrease because activation of SS04185 neurons trigger other actions, such as crawling, head casting, hunching, or stopping, and not because they solely inhibit rolling evoked by Basins. To investigate this possibility, we examined the effect of activating only SS04185 and found that this did not induce any extra actions such as crawling, turning, hunching, or stopping (Figure 1—figure supplement 1A–D). These data suggest that co-activation of Basins and SS04185 neurons reduces rolling because SS04185 activation inhibits the Basin circuit.

Next, we explored how the quality of rolling changed during co-activation of SS04185 and Basin neurons. First, we examined the amount of time animals spent rolling during Basin activation. The average time spent rolling (percentage of the 30 s stimulation period) was 23.9% (7.2 s out of 30 s) following activation of Basins alone, whereas it was only 5.9% following co-activation of Basins and SS04185 (1.8 s out of 30 s) (Figure 1—figure supplement 1E). Additionally, the duration of each rolling bout was significantly shorter when SS04185 neurons were co-activated with Basins (Mann–Whitney U test, p < 0.001; Figure 1F).

The duration of a rolling bout could decrease because of changes in the latency to initiate rolling, latency to terminate rolling, or both. To investigate how SS04185 activation affects these temporal parameters of rolling, we analyzed the latencies for the initiation and termination of the first rolling bout. Compared to activating Basins alone, co-activating the Basins and SS04185-expressing neurons only marginally increased latency to onset of the first rolling bout (Figure 1G), whereas it markedly reduced the latency for the termination of rolling (Mann–Whitney U test, p < 0.001; Figure 1H). These data strongly suggest that SS04185-expressing neurons are involved in terminating rolling.

If the rolling module inhibits crawling, then premature termination of rolling might allow crawling to commence sooner than normal. Co-activation of SS04185 and Basins resulted in the initiation of the first crawling bout occurring earlier than when only Basins were activated (Mann–Whitney U test, p < 0.001; Figure 1I, Figure 1—figure supplement 1F). The time from the end of rolling to the start of crawling remained similar between the groups in which the Basins were activated alone and in which the Basins and SS04185 were co-activated (Figure 1—figure supplement 1G). This is consistent with the higher probability of crawling during activation of SS04185 and Basin neurons (Figure 1—figure supplement 1H). Lastly, activation of SS04185 neurons in conjunction with Basins did not change the crawling speed compared to activation of Basins alone (Figure 1—figure supplement 1I). These results collectively indicate that SS04185 activation terminates rolling and facilitates the shift to fast crawling.

### A pair of descending neurons in SS04185 contributes to termination of rolling

To identify the neurons that express SS04185 upon CsChrimson activation, we examined the localization of SS04185-labeled neurons. We found that SS04185 split-Gal4 strongly labeled a pair of descending neurons located within the SEZ and mushroom body (MB) neurons within the brain (Figure 2A). To pinpoint which of these neurons are involved in reducing the probability of rolling (Figure 1B, C, E), we varied the level of SS04185 expression among the pair of SS04185-expressing descending neurons (SS04185-DN) and the SS04185-expressing MB (SS04185-MB) neurons (jointly with the Basins as in Figure 1). These manipulations allowed us to assess the resultant behavioral outcomes.

![Figure 2.](https://cdn.elifesciences.org/articles/93978/elife-93978-fig2-v1.jpg)

**Figure 2.:** (A) Morphology of SS04185 neurons. GFP, gray (left), green (right); nc82, magenta. Anterior, up; dorsal view; scale bar, 100 µm. Genotype: 10xUAS-IVS-myr::GFP/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/+. (B) Kenyon cells are less labeled in SS04185 with MB>Killer Zipper. CsChrimson::mVenus expression in Kenyon cells of SS04185 in Control and SS04185 with Killer Zipper in mushroom body (MB). mVenus, gray (left), green (right); nc82, magenta. Anterior, up; dorsal view; scale bar, 20 µm. Genotype: 20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/+ (control); 20xUAS-IVS-CsChrimson::mVenus/+; R13F02-LexA,LexAop-KZip+/R54B01-Gal4.AD; R72F11-Gal4/R46E07-Gal4.DBD (MB>KZip+). (C) Rolling probabilities of larvae with activation of SS04185 reduce the expression of CsChrimson in MB neurons. Error bars, 95% confidence interval. n = 78, 55, 100 from left to right. Statistics: Chi-square test, χ2 = 2.32, p > 0.05 for the two groups with SS04185 expression; χ2 = 37.50, p < 0.001 for the comparison between the two groups on the left; χ2 = 70.45, p < 0.001 for the comparison between the groups with MB>KZip + expression which reduce expression of CsChrimson in MB. Genotypes: 20xUAS-IVS-CsChrimson::mVenus/+; R13F02-LexA,LexAop-KZip+/+; R72F11-Gal4/+ (black); 20xUAS-IVS-CsChrimson::mVenusR54B01-Gal4.AD/+; R46E07-Gal4.DBD/R72F11-Gal4 (orange); 20xUAS-IVS-CsChrimson::mVenus/+; R13F02-LexA,LexAop-KZip+/R54B01-Gal4.AD; R72F11-Gal4/R46E07-Gal4.DBD (red). Genotypes in (D–E) are the same as mentioned here. (D) Cumulative plot of rolling duration. Statistics: Kruskal–Wallis test: H = 8.28, p = 0.016; Bonferroni-corrected Mann–Whitney U test, p > 0.05 for all pairwise post hoc tests, n = 103, 20, 27 from left to right. (E) A violin plot of start of first crawling bout for each larva during stimulation. Statistics: Kruskal–Wallis test: H = 15.02, p < 0.001; Bonferroni-corrected Mann–Whitney U test, p > 0.05 for the two groups with SS04185 expression; p < 0.001 for the comparison between the group without SS04185 expression and the groups with full SS04185 expression, n = 65, 20, 7 from left to right. (F) The probabilities of larval rolling during first 5 s of stimulation. Error bars, 95% confidence interval. n = 101, 126. Statistics: Chi-square test, χ2 = 4.27, p = 0.039. Genotype: 13xLexAop2-IVS-CsChrimson::tdTomato/w+, hs-FLP; R54B01-Gal4.AD/72F11-LexA; 20XUAS-(FRT.stop)-CsChrimson::mVenus/R46E07-Gal4.DBD. Genotypes in (G, H) are the same as mentioned here. (G) Cumulative plot of rolling duration. Statistics: Mann–Whitney U test, p < 0.001, n = 350, 473. (H) A violin plot of start of first crawling bout for each larva during stimulation. Statistics: Mann–Whitney U test, p < 0.001, n = 97, 120. ***p < 0.001.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/93978/elife-93978-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) Morphology of SS04185 neurons with split Gal4 inhibition in mushroom body (MB). GFP, green. Anterior, up; dorsal view; scale bar, 100 µm. Genotype: 20xUAS-IVS-CsChrimson::mVenus/+; R13F02-LexA,LexAop-KZip+/R54B01-Gal4.AD; R72F11-Gal4/R46E07-Gal4.DBD. (B) Time series of rolling probabilities of larvae with split Gal4 inhibition in MB (black), SS04185 activation (orange), and both SS04185 activation and split Gal4 inhibition in MB (red). Shaded areas show 95% confidential intervals of rolling probabilities. The red bar and dashed lines display the window of optogenetic stimulation. Genotypes: 20xUAS-IVS-CsChrimson::mVenus/+; R13F02-LexA,LexAop-KZip+/+; R72F11-Gal4/+ (black); 20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/R72F11-Gal4 (orange); 20xUAS-IVS-CsChrimson::mVenus/+; R13F02-LexA,LexAop-KZip+/R54B01-Gal4.AD; R72F11-Gal4/R46E07-Gal4.DBD (red). Genotypes in (C) are the same as mentioned here. (C) A violin plot of total time spent rolling for each individual larva during stimulation. Statistics: Kruskal–Wallis test: H = 21.05, p < 0.001; Bonferroni-corrected Mann–Whitney U test, p > 0.05 for the two groups with SS04185 expression; p < 0.001 for the comparison between the group without SS04185 expression and the two groups with SS04185 expression, n = 66, 17, 21 from left to right. (D) Time series of rolling probabilities of larvae with Basin activation (black), or Basin and MB co-activation (red). The red bar and dashed lines display the window of optogenetic stimulation eliciting larval escape responses. Shaded areas show 95% confidential intervals of rolling probabilities. n = 150, 143. Genotype: 20xUAS-IVS-CsChrimson::mVenus/+; +; R72F11-Gal4/+ (control); 20xUAS-IVS-CsChrimson::mVenus/+;+; MB247-Gal4/R72F11-Gal4 (MB247). Genotypes in (E) are the same as mentioned here. (E) Binned larval rolling probabilities during the first 5 s of stimulation in (D). Error bars, 95% confidence interval. n = 150, 143. Statistics: Chi-square test, χ2 = 3.80, p > 0.05. (F) and (G) show immunostaining of SS04185-expressing neurons. SS04185, green. Anterior, up; dorsal view; scale bar, 100 µm. Genotype: w+, hs(KDRT.stop)FLP/13xLexAop2-IVS-CsChrimson::tdTomato; R54B01-Gal4.AD/72F11-LexA; 20xUAS-FRT(stop)-CsChrimson::mVenus/R46E07-Gal4.DB. Genotypes in (H–K) are the same as mentioned here. (F) has both SS04185-DN and SS04185-MB expression only, and (G) has SS04185-MB expression. (H) Time series of rolling probabilities of larvae with SS04185-MB activation (black), or SS04185-MB and SS04185-DN co-activation (red). The red bar and dashed lines display the window of optogenetic stimulation eliciting larval escape responses. Shaded areas show 95% confidential intervals of rolling probabilities. (I) A violin plot of total time spent rolling for each individual larva during stimulation. Statistics: Mann–Whitney U test, p < 0.001, n = 99, 124. (J) A violin plot of end of first rolling bout for each larva during stimulation. Statistics: Mann–Whitney U test, p < 0.001, n = 99, 124. (K) Time series of turning probabilities of larvae with SS04185-MB activation (black), or SS04185-MB and SS04185-DN co-activation (red). The red bar and dashed lines display the window of optogenetic stimulation eliciting larval escape responses. Shaded areas show 95% confidential intervals of turning probabilities. ***p < 0.001.

If SS04185-MB neurons are involved in the modulation of rolling, then reducing SS04185-MB expression should reduce the extent to which activation of both SS04185-DN neurons and SS04185-MB neurons decreases the probability of rolling. To test this conjecture, we expressed Killer Zipper (KZip+), which interferes with the binding of Gal4AD and Gal4DBD in SS04185-MB neurons with MB LexA line (R13F02-LexA), consequently leading to a significant reduction in CsChrimson expression in SS04185-MB neurons (Figure 2B, Figure 2—figure supplement 1A; Dolan et al., 2017; Vogt et al., 2016). When compared to KZip+ controls, which do not express SS04185 (Figure 2C, black bars), however, activation of SS04185 neurons with reduced SS04185-MB expression (Figure 2C, red bars on the right; Figure 2—figure supplement 1B) still reduced rolling probability (as well as the total duration of rolling [Figure 2—figure supplement 1C]) to a level no different from that of KZip− controls expressing SS04185 fully in both SS04185-MB and SS04185-DN neurons (Figure 2C, dark red bars in the middle). Additionally, co-activation of MB Gal4 lines (MB247-Gal4) with Basins (without activation of SS04185-DN neurons) did not reduce the probability of rolling (Figure 2—figure supplement 1D, E). These data indicate that SS04185-DN neurons inhibit rolling.

To further test the role of SS04185-DN neurons, we investigated whether these neurons were involved in reducing the duration of each rolling bout (Figure 1A, D, F). As a result, knockdown of SS04185-MB neurons did not increase the duration of rolling bouts (Figure 2D). Furthermore, the earlier onset of crawling triggered by the activation of SS04185 neurons remained the same with knockdown of SS04185-MB neurons (Figure 2E). Collectively, these results strongly suggest that the behavioral effects on both rolling and crawling, as illustrated in Figure 1, are primarily mediated by SS04185-DN neurons.

To further ascertain the role of SS04185-DN neurons in the regulation of rolling, we employed the heat shock FlpOut mosaic expression approach. This technique allowed for controlled and sporadic expression of CsChrimson in SS04185 neurons thorough random induction of Flippase by manipulating the timing and duration of heat shock (Golic and Lindquist, 1989; Nern et al., 2015). We compared larvae subjected to activation of both SS04185-MB and SS04185-DN neurons (red, Figure 2—figure supplement 1F) with those subjected only to activation of SS04185-MB neurons (black, Figure 2—figure supplement 1G), to assess the degree to which the former showed behavioral effects. Remarkably, activation of both SS04185-MB and SS04185-DN neurons resulted in a reduction in both the probability and duration of rolling when compared to activation of SS04185-MB neurons alone (Figure 2F, G, Figure 2—figure supplement 1H, I). Furthermore, activation of both SS04185-MB and SS04185-DN neurons reduced the latency to the end of the first rolling bout and the initiation of the first crawling bout (Figure 2H, Figure 2—figure supplement 1J). These findings provide compelling evidence that SS04185-DN neurons, but not SS04185-MB neurons, play an important role in the termination of rolling. Collectively, the results suggest that a single pair of descending neurons in SS04185 is important for termination of rolling during the activation of Basins.

### Descending neurons identified by SS04185 correspond to SeIN128 neurons

In a previous electron microscopy (EM) connectome study, we identified a set of neurons designated as SeIN128, whose-cell bodies in the SEZ send axonal projections throughout the thoracic and abdominal segments (Figure 3A; Ohyama et al., 2015). Our immunostaining data also showed that the cell bodies of SS04185-DN neurons are located in the SEZ, with axons bilaterally innervating the medial regions of the ventral nerve cord (VNC) from the thoracic to abdominal segments A8/9 (Figure 2A), suggesting that SS04185-DN and SeIN128 neurons are one and the same.

![Figure 3.](https://cdn.elifesciences.org/articles/93978/elife-93978-fig3-v1.jpg)

**Figure 3.:** (A) Transmission Electron microscopy (TEM) neuron reconstruction of SeIN128 neurons. Left panel: anterior, up; dorsal view. Right panel: anterior, up; dorsal, right; lateral view. Red dots, presynaptic sites. Cyan dots, postsynaptic sites. (B) A transverse section of larval central nervous system (CNS) from EM reconstruction data. SeIN128 (green), Basins (blue), and A00c (orange) are located in ventromedial tract (VM). mdIV, red; magenta, neural tracts. DM, dorsomedial tract; VM, ventromedial tract. Dorsal, up; anterior view; scale bar, 1 µm. (C) Cartoon generated based on transverse section of SeIN128, Basin-1 to Basin-4, A00c, and mdIV from EM neuron reconstruction data and (D). Nerve tracts are shown in magenta. Dorsal, up; posterior view. DM, dorsomedial tract; VM, ventromedial tract; CI, central-intermediate tract; CL, central-lateral tract; DL, dorsolateral tract; VL, ventrolateral tract. SeIN128, green; Basin-1 to Basin-4, blue; A00c, orange; mdIV, red. (D) SS04185-expressing neurons co-stained with N-cadherin. A cell body of SS04185-descending neuron located in ventral part of the subesophageal zone (SEZ). SS04185, green; N-cadherin, magenta. Anterior, up; left, dorsal view; right, longitudinal section; scale bar, 100 µm. Genotype: 10xUAS-IVS-myr::GFP/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/+. SS04185, green; Cadherin, magenta. Anterior, left, dorsal, up; lateral view; scale bar, 100 µm. (E) Transverse section of SS04185-DN co-stained with Fas2. SS04185-DN located at ventromedial tract (VM). SS04185, green; Fas2, magenta. Dorsal, up; posterior view; scale bar, 20 µm. DM, dorsomedial tract; VM, ventromedial tract; CI, central-intermediate tract; CL, central-lateral tract; DL, dorsolateral tract; VL, ventrolateral tract. Genotype: 10xUAS-IVS-myr::GFP/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/+. (F, H, J) SS04185-DN co-localized with Basins or A00C neuron tract but not MdIV. SS04185, green; Basins (F), A00c (H), or mdIV (J), magenta. Genotype: w; R54B01-Gal4.AD/R72F11-LexA(F) 71A10-LexA(H) or ppk1.9-LexA(J); R46E07-Gal4.DBD/13xLexAop2-IVS-CsChrimson::tdTomato,20xUAS-IVS-GCaMP6s. Top panel: anterior, up; dorsal view; scale bar, 10 µm. Bottom panel: dorsal, up; posterior view; scale bar, 5 µm. (G, I, K) SeIN128, Basin-2, A00c, or mdIV morphologies from the TEM neural reconstruction. Anterior, up; dorsal view. SS04185, green; Basin-2, blue; A00C, orange; mdIV, red.

To verify this possibility, we examined the detailed anatomy of SS04185-DN neurons by immunostaining them with several markers and compared our immunostaining images with the corresponding images obtained via EM reconstruction of the entire CNS of a first instar Drosophila larva (Ohyama et al., 2015; Winding et al., 2023). We confirmed that the projections of SeIN128 neurons are distributed within the ventromedial neural tract (one of the six major neural tracts) in Drosophila larvae (Figure 3A–C) in EM reconstruction data. We also confirmed that the cell bodies of SS04185-DN neurons were again located in the SEZ region, where the most anterior of the three neuropils in the thoracic region was marked by N-cadherin (Figure 3D). Viewed from the side (i.e., in the longitudinal or sagittal plane), both the cell bodies and axonal arbor were located ventrally (Figure 3D, far right). Immunostaining with Fasciclin2 (Fas2), which labels various neural tracts in the VNC (Grenningloh et al., 1991; Santos et al., 2007), showed colocalization of the axonal projections of SS04185-DN neurons and the Fas2-labeled ventromedial tract (Figure 3C, E). The similarity of the locations of their cell bodies and the distributions of their axonal processes suggests the identity of the SS04185-DN and SeIN128 neurons.

A previous EM study showed that SeIN128 neurons were located downstream of Basin neurons (Ohyama et al., 2015). To further confirm the identity of SS04185-DN and SeIN128 neurons, we compared the distributions of the axonal projections of SS04185-DN neurons in relation to those of several key neurons within the rolling circuit: the Basins, A00c neurons (a group of ascending neurons downstream of the Basins, and which facilitate rolling), and mdIV neurons (nociceptive sensory neurons upstream of the Basins). Immunostaining revealed that Basin projections colocalize with those of SS04185-DN neurons in both the horizontal and transverse planes (Figure 3F, top and lower panels, respectively), with the horizontal view showing that SS04185-DN projections are distributed slightly medial to those of Basins within the ventromedial tract (Figure 3F, top panels), which resembles their colocalization pattern reported in EM (Figure 3B, C, G). Similarly, we compared the distributions of SS04185-DN projections with those of A00c or mdIV projections. We found that the projections of A00c colocalize with those of SS04185-DN in a similar fashion along the rostrocaudal axis within the ventromedial tract (Figure 3H,I), with A00c projections distributed more medially than SS04185-DN projections, consistent with the distribution patterns of SeIN128 projections and A00c projections in the EM reconstruction dataset (Figure 3B, H, I). In contrast, the distributions of mdIV projections did not colocalize with those of SS04185-DN projections, as the mdIV projections were displaced more laterally relative to the SS04185-DN projections in the horizontal and transverse planes (Figure 3J, top and lower panels, respectively), consistent with the distribution patterns of SeIN128 and mdIV projections in the EM reconstruction dataset (Figure 3K). In the transverse plane, the projections of SS04185-DN neurons were also distributed dorsomedial to those of mdIV (Figure 3J, lower panel), consistent with the corresponding distribution patterns in the EM reconstruction dataset (Figure 3B, C, K).

We conclude that the morphological findings for SS04185-DN neurons, together with data on the distribution of their axonal projections in relation to that of Basin, A00c, and mdIV neurons, strongly suggest the identity of SS04185-DN and SeIN128 neurons.

### Connectome and functional connectivity analyses: SeIN128 neurons receive inputs from Basin-2 and A00c

A previous study that reconstructed larval neurons involved in the rolling circuit showed that Basin-2 and A00c neurons (in the VNC) make excitatory synaptic contacts onto SeIN128 neurons (in the CNS), which in turn make reciprocal inhibitory synaptic contacts onto Basin-2 and A00c neurons (Figure 4A, Figure 4—figure supplement 1A; Ohyama et al., 2015). These data suggest that SeIN128 neurons are directly activated by Basin-2 and A00c (which also receives inputs from Basin-1, Basin-2, and Basin-4).

![Figure 4.](https://cdn.elifesciences.org/articles/93978/elife-93978-fig4-v1.jpg)

**Figure 4.:** (A) Summary of the connectivity between SeIN128 and the escape circuit. SeIN128 receives inputs from Basin-2 and A00c and provide feedback to Basin-2 and A00c. Synapse number shown next to connection arrows, where line width is proportional to synapse number. All connections in the ventral nerve cord are shown except unilateral synapses, <5 synapses, between neurons. Each polygon represents a pair of the indicated neuron and segment (segment number is shown under the neuron name). SeIN128, green; Basin-2, blue; A00c, orange; mdIV, red. SeIN128 is functionally downstream of Basins (B) or A00c (C). Calcium transients, ΔF/F0 traces of GCaMP6s in SeIN128 axons (black line, mean; gray line, single larva) during 610 nm optogenetic activation of Basins at various intensities. Vertical gray line represents optogenetic activation. Genotype: w; R72F11-LexA (B) or R71A10-LexA (C) /R54B01-Gal4.AD; 13xLexAop2-IVS—CsChrimson::tdTomato, 20xUAS-IVS-GCaMP6s/R46E07-Gal4.DBD. (D) A00c responses are faster and stronger than SeIN128 responses during activation of Basins. Calcium transients (black line, mean; gray line, single larva) represented by ΔF/F0 in A00c by of 610 nm optogenetic activation of Basins at various intensities. Genotype: w; R72F11-LexA/+; 13xLexAop2-IVS-CsChrimson::tdTomato, 20xUAS-IVS-GCaMP6s/R71A10-Gal4. For (B–D), irradiances from left to right are 0.04, 0.1, 0.3, 0.5, and 1.4 µW/mm2. For each irradiance (n = 6), individual traces are shown with gray lines whereas the average of individuals is shown in black. The shaded gray area indicates the period of optogenetic activation (0–1 s). (E) The timing of the peak ΔF/F0 correlated with the identity of the neurons but not the peak ΔF/F0 value. SeIN128 neurons are shown as orange dots, whereas A00c is shown as a green dot.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/93978/elife-93978-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A) Connectivity among Basin, A00c, and SeIN128. Each line represents synaptic connections from the presynaptic neurons (left) to the postsynaptic neurons (right). Line widths are proportional to the counts of the synapses. (B) SeIN128 does not respond to light stimulation when all-trans retinal is not fed. Calcium transients, ΔF/F0 traces of GCaMP6s in SeIN128 axons (black line, mean; gray line, single larva) during 610 nm optogenetic activation of Basins at various intensities. Vertical gray line represents optogenetic activation. The shaded gray area indicates the period of optogenetic activation (0–1 s). Irradiance, 1.4 µW/mm2. n = 4. Genotype: w; R72F11-LexA (left panel) or R71A10-LexA (right panel) /R54B01-Gal4.AD; 13xLexAop2-IVS-CsChrimson::tdTomato, 20xUAS-IVS-GCaMP6s/R46E07-Gal4.DBD. (C) Peak ΔF/F0 increased with increasing irradiance in both SeIN128 and A00c neurons. The orange line corresponds with Figure 4B; yellow line corresponds with Figure 4C; and green line corresponds with Figure 4D.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/93978/elife-93978-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** (A) Basin-2 morphology and cell body location reported in EM reconstruction dataset (A1, left hemi-segment). Dorsal view. Red lines, presynaptic sites; cyan lines, postsynaptic sites. (B) A zoomed-in view of the square in (A). (C) SeIN128 morphology and cell body location reported in EM reconstruction dataset (right). Dorsal view. Red lines, presynaptic sites; cyan lines, postsynaptic sites. (D) A zoomed-in view of the square in (C). (E) Connections between SeIN128 and Basin-2. Dorsal view. Red lines, presynaptic sites of SeIN128; cyan lines, postsynaptic sites of Basin-2; brown lines, presynaptic sites of Basin-2. (F) Zoomed-in views of squares in (E). (G) EM view of left top panel in (F). Green, SeIN128; blue, Basin-2. White arrows show SeIN128 presynaptic sites adjacent to Basin-2. Yellow arrows are two presynaptic sites of Basin-2.

To assess the functional significance of these synaptic connections between SeIN128 neurons and Basins or A00c, we activated either Basins or A00c neurons and examined the resultant green fluorescent protein (GFP) calmodulin (CaM) protein (GCaMP) signaling in SeIN128 neurons. Specifically, after expressing CsChrimson in Basins and A00c neurons and GCaMP in SeIN128 neurons, we used a two-photon microscope (920 nm laser) and monitored GCaMP signaling in SeIN128 neurons during illumination of a specimen with a 620-nm light-emitting diode (LED) for 1 s (0.04–1.4 µW/mm2), which activated either Basins or A00c neurons. GCaMP signals in SeIN128 neurons increased in an intensity-dependent manner when either Basins and A00c were activated (Figure 4B, C) but not when larvae were not fed retinal (Figure 4—figure supplement 1C, D). Peak activity occurred at around 3 s after the onset of LED stimulation, which was similar to the results when Basins or A00c neurons were stimulated (Figure 4B, C). Finally, both Basin and A00c stimulation resulted in linear dose-dependent increases in SeIN128 firing (Figure 4—figure supplement 1B). These results are consistent with the notion that SeIN128 neurons are downstream of Basins and A00c neurons.

To compare the neural responses between Basins and SeIN128 or A00c neurons, we recorded neural activity in A00c neurons with GCaMP while stimulating Basin neurons in the same experimental setting. Although A00c neurons displayed a similar dose-dependent increase in peak axonal firing as the intensity of optogenetic stimulation of Basin neurons increased, unlike SeIN128 neurons they showed no delay in peak firing activity (Figure 4D, E, Figure 4—figure supplement 1B), suggesting that A00c and SeIN128 neurons function differently in the rolling circuit.

We then investigated the anatomical locations of the synaptic outputs and inputs of SeIN128 neurons, and found that, whereas their outgoing projections primarily make synaptic contacts along the anterior–posterior nerve axis, the inputs coming from other neurons are mainly located in the SEZ (Figure 3A). On the other hand, SeIN128 neurons make axo-axonal contacts onto Basin-2 neurons (Figure 4—figure supplement 2A–G) as well as A00c neurons: that is, their axons make synaptic contacts with the dorsal and medial processes of Basin-2, which correspond to their axonal compartments (Figure 4—figure supplement 2E–G). These data suggest that the delay of SeIN128 activity may be caused by multi-synaptic connections involving the SEZ or a feedback loop involving axo-axonal connections between SeIN128 and Basin-2 or A00c.

### SeIN128 neurons are GABAergic and inhibitory

The results thus far indicate that, activation of SeIN128 neurons inhibits rolling (Figure 1A–C); SeIN128 neurons receive functional inputs from Basin-2 and A00c (Figure 4A–C); and SeIN128 neurons make anatomical connections onto Basin-2 and A00c (Figure 4A). These findings suggest that SeIN128 neurons might be inhibitory. To test this possibility, we performed immunostaining experiments and found that SeIN128 neurons colocalized with glutamic acid decarboxylase (Gad)-positive neurons but not with acetylcholine- or glutamate-positive neurons, suggesting that SeIN128 neurons are GABAergic inhibitory neurons (Figure 5A, Figure 5—figure supplement 1A,B).

![Figure 5.](https://cdn.elifesciences.org/articles/93978/elife-93978-fig5-v1.jpg)

**Figure 5.:** (A) Immunostaining of SeIN128 cell body (green) and GABAergic neuron (magenta). Genotype: 10xUAS-IVS-myr::GFP; R54B01-Gal4.AD/13xLexAop-dsRed; R46E07-Gal4.DBD/Trojan-GAD-T2A-LexA. White triangles indicate locations of SeIN128 cell bodies. Anterior, up; dorsal view; scale bar, 10 µm. (B) Time series of rolling probabilities of larvae with Basin activation (black), or vesicular GABA transporter (VGAT) RNA interference (RNAi) in SS04185 and Basin activation (red). The red bar and dashed lines display the window of optogenetic stimulation eliciting larval escape responses. Shaded areas show 95% confidential intervals of rolling probabilities. Genotypes: 13xLexAop2-IVS-CsChrimson::mVenus; R72F11-LexA/+; HMS02355/+ (black); 13xLexAop2-IVS-CsChrimson::mVenus; R72F11-LexA/R54B01-Gal4.AD; HMS02355/R46E07-Gal4.DBD (red). Genotypes in (C, D) are the same as mentioned here. (C) Binned larval rolling probabilities during first 5 s of stimulation in (A). Error bars, 95% confidence interval. n = 110, 73. Statistics: Chi-square test, χ2 = 9.34, p < 0.001. (D) Cumulative plot of rolling duration. Statistics: Mann–Whitney U test, p = 0.015, n = 55, 73. **p < 0.01.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/93978/elife-93978-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (A) Immunostaining of SeIN128 cell body (green) and glutamatergic neuron (magenta). Genotype: 10xUAS-IVS-myr::GFP/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/+. (B) Immunostaining of SeIN128 cell body (green) and cholinergic neuron (magenta). Genotype: 10xUAS- IVS-myr::GFP/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/+. In (A, B), white triangles indicate locations of SeIN128 cell bodies. Anterior, up; dorsal view; scale bar, 10 µm. (C) Normalized anti-GABA fluorescence intensities in the neuropil by anti-Elav staining in segments A4 to A6. A.U., arbitrary unit. Genotype: w; R57C10-Gal4 /+ (black) and w; R57C10-Gal4/UAS-HMS02355 (red). Statistics: Student’s t test, **p = 0.0106, n = 7. (D) Normalized anti-VGAT fluorescence intensities in the neuropil by anti-Elav staining in segments A4 to A6. A.U., arbitrary unit. Genotype: w; R57C10-Gal4 /+ (black) and w;; R57C10-Gal4/UAS-HMS02355 (red). Statistics: Student’s t test, p = 0.0031, n = 6. *p = 0.0295.

We reasoned that if Gamma-aminobutyric acid (GABA) in SeIN128 neurons is necessary for inhibiting rolling, then selectively knocking down GABA secretion in SeIN128 neurons should enhance rolling. When we expressed RNA interference (RNAi) HMS02355 in SeIN128 neurons to knock down vesicular GABA transporter (VGAT) expression and suppress the release of GABA, the population-level rolling probability increased from 23.6% to 45.2% (Figure 5B, C; Kallman et al., 2015; Zhao et al., 2019). We confirmed the effect of HMS02355 by immunostaining: pan-neural HMS02355 expression decreased GABA and VGAT expression in the neuropil (Figure 5—figure supplement 1C, D). The control group (only Basins expressing CsChrimson with VGAT RNAi HMS02355 but without SS04185) showed a lower probability of rolling (23.6%) compared to similar genotypes without VGAT RNAi HMS02355 (Figure 2C, F). This indicates that VGAT RNAi HMS02355 background reduces the probability of rolling. Furthermore, the duration of each bout of rolling increased from 0.8 to 1.4 s (Figure 5D). These data support the idea that SeIN128 neurons inhibit rolling via GABAergic transmission.

### Inhibition of SeIN128 increases probability and duration of rolling

To further test whether the release of GABA upon activating SeIN128 neurons is necessary for inhibiting rolling, we expressed tetanus toxin (TNT) in SeIN128 neurons to block synaptic transmission. Silencing SeIN128 neurons via TNT while triggering rolling by optogenetically activating Basin neurons via R72F11-LexA>LexAop-CsChrimson significantly increased the probability of rolling compared to controls (Figure 6A, B). Silencing SeIN128 neurons via TNT extended the duration of each rolling bout, as well as the total rolling duration, in each larva (Figure 6C, D). We also examined the rolling-escape crawling sequence upon silencing SeIN128 neurons, and found that the time to offset of rolling and the time onset of crawling were both delayed relative to controls (Figure 6E, F).

![Figure 6.](https://cdn.elifesciences.org/articles/93978/elife-93978-fig6-v1.jpg)

**Figure 6.:** (A) Time series of rolling probabilities of larvae with Basin activation (black), or SS04185 inhibition and Basin activation (red). Shaded regions show 95% confidential intervals of rolling probabilities. Genotypes: 13xLexAop2-IVS-CsChrimson::mVenus; R72F11-LexA/+; UAS- TeTxLC.tnt/+ (black); 13xLexAop2-IVS-CsChrimson::mVenus; R72F11-LexA/R54B01-Gal4.AD; UAS-TeTxLC.tnt/R46E07-Gal4.DBD (red). Genotypes in (B–F) are the same as mentioned here. (B) Rolling probabilities during first 5 s of stimulation in (A). Error bars, 95% confidence interval. n = 241, 164. Statistics: Chi-square test, χ2 = 44.02, p < 0.001. (C) A violin plot of total time spent rolling for each individual larva during stimulation. Statistics: Mann–Whitney U test, p < 0.001, n = 221, 258. (D) Cumulative plot of rolling duration. Statistics: Mann–Whitney U test, p < 0.001, n = 160, 154. (E) A violin plot of end of first rolling bout for each larva during stimulation. Statistics: Mann–Whitney U test, p < 0.001, n = 160, 154. (F) A violin plot of start of first crawling bout for each larva during stimulation. Statistics: Mann–Whitney U test, p < 0.001, n = 65, 105. ***p < 0.001.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/93978/elife-93978-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** (A) Time series of rolling probabilities of larvae with Basin activation (black), or SS04185 inhibition and Basin activation (red). Larvae were incubated with heat to trigger the effect of shibirets1. The red bar and dashed lines display the window of optogenetic stimulation eliciting larval escape responses. Shaded areas show 95% confidential intervals of rolling probabilities. Genotypes: 13xLexAop2-IVS-CsChrimson::mVenus;R72F11-LexA/+; 20xUAS-TTS-Shibire/+ (black); 13xLexAop2-IVS-CsChrimson::mVenus; R72F11-LexA/R54B01-Gal4.AD; 20xUAS-TTS-Shibire/R46E07-Gal4.DBD (red). Genotypes in (B–G) are the same as mentioned here. (B) Binned larval rolling probabilities during first 5 s of stimulation in (A). Error bars, 95% confidence interval. n = 134, 143. Statistics: Chi-square test, χ2 = 12.33, p < 0.001. (C) A violin plot of total time spent rolling for each individual larva during stimulation. Statistics: Mann–Whitney U test, p > 0.05, n = 85, 115. (D) Cumulative plot of rolling duration. Statistics: Mann–Whitney U test, p > 0.05, n = 219, 352. (E) A violin plot of start of first rolling bout for each larva during stimulation. Statistics: Mann–Whitney U test, p > 0.05, n = 85, 115. (F) A violin plot of end of first rolling bout for each larva during stimulation. Statistics: Mann–Whitney U test, p = 0.013, n = 85, 115. (G) A violin plot of start of first crawling bout for each larva during stimulation. Statistics: Mann–Whitney U test, p = 0.034, n = 32, 22. ***p < 0.001.

Given that TNT is expressed constitutively during development, long-term compensatory changes in the nervous system could have contributed to alterations in the parameters of rolling and crawling. To test whether similar results could be replicated with the use of a temporally specific intervention, we expressed shibirets1 (shits1) in SeIN128 neurons to block synaptic transmission at temperatures above 30°C (van de Goor et al., 1995; Kitamoto, 2001). Silencing SeIN128 neurons via shibirets1 increased the probability of rolling from 60.4% to 79.7% (Figure 6—figure supplement 1A, B). The total duration of rolling per animal during stimulation increased from 10 to 12 s (Figure 6—figure supplement 1C). Although the duration of each rolling bout, the time to onset of the first rolling bout, and time to onset of the first crawling bout did not differ from those of controls (Figure 6—figure supplement 1D, E, G), the time to offset of the first rolling bout was delayed relative to controls (p = 0.013 for Figure 6—figure supplement 1F). Together with the results showing that activation of SeIN128 neurons inhibits rolling, these findings suggest that the activity of SeIN128 neurons is important in controlling the duration of rolling and the shift to crawling.

### Basins receive GABAergic inputs that inhibit rolling

Given that Basins receive axo-axonal inputs from SeIN128 neurons and GABA signaling in SeIN128 neurons inhibits rolling, we next used RNAi to test whether Basins receive GABAergic signals from SeIN128. We hypothesized that knockdown of GABA receptors in Basin neurons would increase the probability and duration of rolling at the population level. To knock down ionotropic GABA-A receptors (GABA-A-R) and G-protein-coupled GABA-B receptors (GABA-B-R1 and GABA-B-R2), we tested Basin neurons with GABA-A-R, GABA-B-R1, and GABA-B-R2 RNAi lines (i.e., HMC03643 for GABA-A-R, HMC03388 for GABA-B-R11, JF02989 for GABA-B-R12, and HMC02975 for GABA-B-R2, respectively). For all RNAi lines, the rolling probability at the population level increased from 80% to 90% or even higher (Figure 7A), while the total rolling duration at the individual level increased for each larva throughout the stimulation window (Figure 7—figure supplement 1A). All GABA receptor knockdown groups showed significant increases in rolling duration across multiple bouts (Figure 7B); all groups except for GABA-B-R11 showed a reduced time to onset of the first rolling bout (Figure 7—figure supplement 1B); and only the GABA-B-R2 and GABA-A-R groups showed a delayed offset of the first rolling bout (Figure 7—figure supplement 1C). None of the groups differed from controls in the time to onset of the first crawling bout (Figure 7—figure supplement 1D). The greatest increase in the probability and duration of rolling was seen during knockdown of ionotropic GABA-A-R (Rdl), suggesting that Rdl contributes most to the inhibition of Basin neurons (Figure 7A, B).

![Figure 7.](https://cdn.elifesciences.org/articles/93978/elife-93978-fig7-v1.jpg)

**Figure 7.:** (A) Rolling probabilities for larvae with GABAR-RNAi in their Basin neurons. From left to right, the genotypes are 20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4/+ (black), 20xUAS—IVS-CsChrimson::mVenus/+; R72F11-Gal4/UAS-HMC03388 (blue), 20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4/UAS-JF02989 (green), 20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4/UAS-HMC02975 (yellow), and 20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4/UAS-HMC03643 (orange). Genotypes in (B) are the same as mentioned here. N = 320, 205, 159, 183, 182 from left to right. Statistics: Chi-square test, Bonferroni correction. GABA-B-R11 group: χ2 = 8.76, p = 0.012. GABA-B-R12 group: χ2 = 24.70, p < 0.001. GABA-B-R2 group: χ2 = 25.77, p < 0.001. GABA-A-R group: χ2 = 16.29, p < 0.001. (B) Cumulative plot of rolling duration. Statistics: Kruskal–Wallis test: H = 69.52, p < 0.001; Bonferroni-corrected Mann–Whitney U test, p < 0.001 between control and the GABA-B-R11, GABA-B-R12, and GABA-B-R2 RNA interference (RNAi) groups; p < 0.001 between GABA-A-R and all other RNAi groups. Sample sizes for the colored bars from top (control, black) to bottom (GABA-A-R, red); n = 520, 488, 387, 582, 306. (C) Summary of peak ΔF/F0 in Basin axons with or without SeIN128 activation under various irradiances. Control groups shown in black are without SeIN128 activation while experimental groups shown in red are with SeIN128 activation. Statistics: Mann–Whitney U test, p > 0.05 for irradiances of 0.04, 0.1, and 1.4 µW/mm2; p = 0.016 for irradiance of 0.3 µW/mm2; p = 0.032 for irradiance of 0.5 µW/mm2. Genotype: 20xUAS-Syn21-opGCaMP6s, 10xUAS-Syn21-CsChrimson88::tdTomato/+; CyO/+;R72F11-Gal4/TM6 (black); 20xUAS-Syn21-opGCaMP6s,10xUAS-Syn21-CsChrimson88::tdTomato/+;CyO/R54B01-Gal4.AD;R72F11-Gal4/R46E07-Gal4.DBD (red). *p < 0.05, ***p < 0.001.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/93978/elife-93978-fig7-figsupp1-v1.jpg)

**Figure 7—figure supplement 1.:** (A) A violin plot of total time spent rolling for each individual larva with GABAR-RNAi in their Basin neurons during stimulation. Statistics: Kruskal–Wallis test: H = 110.86, p < 0.001; Bonferroni-corrected Mann–Whitney U test, p < 0.001 for all RNA interference (RNAi) groups, n = 271, 194, 154, 178, 174 from left to right. The genotypes are 20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4/+ (black), 20xUAS—IVS-CsChrimson::mVenus/+; R72F11-Gal4/UAS-HMC03388 (blue), 20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4/UAS-JF02989 (green), 20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4/UAS-HMC02975 (yellow), and 20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4/UAS-HMC03643 (orange). Genotypes in (B–D) are the same as mentioned here. (B) A violin plot of start of first rolling bout for each larva during stimulation. Statistics: Kruskal–Wallis test: H = 86.50, p < 0.001; Bonferroni-corrected Mann–Whitney U test, p < 0.001 for GABA-B-R12, GABA-B-R2, and GABA-A-R groups, n = 271, 194, 154, 178, 174 from left to right. (C) A violin plot of end of first rolling bout for each larva during stimulation. Statistics: Kruskal–Wallis test: H = 36.01, p < 0.001; Bonferroni-corrected Mann–Whitney U test, p < 0.001 for GABA-B-R2 and GABA-A-R groups, n = 271, 194, 154, 178, 174 from left to right. (D) A violin plot of start of first crawling bout for each larva during stimulation. Statistics: Kruskal–Wallis test: H = 53.07, p < 0.001; Bonferroni-corrected Mann–Whitney U test, p < 0.001 for GABA-B-R12 group, n = 89, 119, 139, 135, 137 from left to right. (E) Calcium transients (mean ± standard error of the mean [SEM]) represented by ΔF/F0 are evoked in Basin axons by optogenetic activation of Basin neurons various intensities. N = 9. Genotype: 20xUAS-Syn21-opGCaMP6s,10xUAS-Syn21-CsChrimson88::tdTomato/+;CyO/+;TM6/R72F11-Gal4. (F) Calcium transients (mean ± SEM) in Basin axons represented by ΔF/F0 are decreased by optogenetic activation of SeIN128 neurons at various intensities. N = 10. Genotype: 20xUAS-Syn21-opGCaMP6s,10xUAS-Syn21-CsChrimson88::tdTomato/+;CyO/R54B01-Gal4.AD;R72F11-Gal4/R46E07-Gal4.DBD. For (E, F), irradiances from left to right are 0.04, 0.1, 0.3, 0.5, and 1.4 µW/mm2. For each irradiance, individual traces are shown with gray lines, whereas the average of individuals is shown in black. Shaded gray area denotes period of optogenetic activation (0–1 s). ***p < 0.001.

To investigate whether SeIN128 neurons actually inhibit Basins, we recorded the activity of all Basins during activation of SeIN128 neurons. We compared GCaMP signaling in the Basins when they were co-activated with SeIN128 neurons (experimental treatment) or when they were activated alone (control treatment), with the intensity of optogenetic stimulation varied from 0.04 to 1.4 µW/mm2. We found that Basins in the experimental group showed reductions in GCaMP signaling by 11–36% compared to those in the control group (Figure 7C, Figure 7—figure supplement 1E, F). The reductions were observed at all stimulation intensities when contrasting peak GCaMP responses, and statistically significant at intensities of 0.3 and 0.5 µW/mm2 (Figure 7C, Figure 7—figure supplement 1E, F). Collectively, these data support the idea that SeIN128 neurons directly inhibit the activity of Basins via GABA.

### Effects of SeIN128 activation on rolling elicited by activating individual Basins

In the studies above, we measured the activity of all Basins while manipulating the activity of SeIN128 neurons. Connectome and behavioral analyses indicate, however, that of the four types of Basins, only Basin-2 and Basin-4 receive nociceptive input from mdIV and trigger rolling (Ohyama et al., 2015). Moreover, as noted above, an examination of the larval connectome (Ohyama et al., 2015; Winding et al., 2023) revealed that Basin-2 both receives axo-axonal inputs from SeIN128 neurons and sends excitatory projections to the same SeIN128 neurons, whereas a similar examination revealed that Basin-4 neither receives inputs from, nor sends any outputs to, SeiN128 neurons. Therefore, we hypothesized that activation of SeIN128 neurons would inhibit rolling elicited by Basin-2 activation and modify the temporal parameters of rolling, but not affect rolling elicited by Basin-4 activation.

We first examined the pattern of rolling evoked by optogenetically activating Basin-2. Basin-2 activation induced multiple bouts of rolling throughout the stimulation window (Figure 8—figure supplement 1A). Furthermore, the rolling elicited by Basin-2 activation tended to be sustained (Figure 8—figure supplement 1A). Next, to determine how SeIN128 activation affects the pattern of rolling elicited by Basin-2 activation, we optogenetically activated SeIN128 neurons and Basin-2 simultaneously. As expected, compared to the probability of rolling in control animals in which only Basin-2 was activated, the probability of rolling in experimental animals in which Basin-2 and SeIN128 neurons were simultaneously activated was significantly lower (66.7% vs 24.4%; Figure 8A, Figure 8—figure supplement 1D). We also examined other parameters of rolling, including the time from the start (onset) of stimulation to the onset of the first rolling bout, termination (offset) of the first rolling bout, and onset of the first crawling bout, as well as the duration of the rolling bout (i.e., the time from its onset to its offset). Consistent with the hypothesis that SeIN128 activation inhibits Basin-2 activity, the duration of the rolling bout significantly decreased (Figure 8B, Mann–Whitney U test, p = 0.0034, Cohen’s d = 0.351) and the time to onset of the first rolling bout significantly increased in experimental animals compared to controls (Figure 8—figure supplement 1E; Mann–Whitney U test, p < 0.001). In addition, as expected, the time to offset of the first rolling bout (Figure 8C; Mann–Whitney U test, p = 0.0047, Cohen’s d = 0.607) and time to onset of the first crawling bout (Figure 8D; Mann–Whitney U test, p = 0.0074, Cohen’s d = 0.548) both significantly decreased in experimental animals compared to controls. Collectively, these findings suggest that Basin-2 neurons play a major role in mediating the effects of SeIN128 activation on rolling induced by optogenetic activation of all Basin neurons.

![Figure 8.](https://cdn.elifesciences.org/articles/93978/elife-93978-fig8-v1.jpg)

**Figure 8.:** (A) Binned larval rolling probabilities during the first 5 s of stimulation. Error bars, 95% confidence interval. n = 81, 119. Statistics: Chi-square test, χ2 = 35.51, p < 0.001. Genotypes: 20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/+; R38H09-Gal4.DBD/+ (black); 20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/R54B01-Gal4.AD; R38H09-Gal4.DBD/R46E07-Gal4.DBD (red). Genotypes in (B–D) are the same as mentioned here. (B) Cumulative plot of rolling duration. Statistics: Mann–Whitney U test, p = 0.0034, n = 206, 83. (C) A violin plot of end of first rolling bout for each larva during stimulation. Statistics: Mann–Whitney U test, p = 0.0047, n = 57, 38. (D) A violin plot of start of first crawling bout for each larva during stimulation. Statistics: Mann–Whitney U test, p = 0.045, n = 107, 38. (E) Binned larval rolling probabilities during first 5 s of stimulation. Error bars, 95% confidence interval. n = 192, 213. Statistics: Chi-square test, χ2 = 64.81, p < 0.001. Genotypes: 20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/+; R57F07-Gal4.DBD/+ (black); 20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/R54B01-Gal4.AD; R57F07-Gal4.DBD/R46E07-Gal4.DBD (red). Genotypes in (F–H) are the same as mentioned here. (F) Cumulative plot of rolling duration. Statistics: Mann–Whitney U test, p = 0.032, n = 231, 71. (G) A violin plot of end of first rolling bout for each larva during stimulation. Statistics: Mann–Whitney U test, p = 0.0047, n = 129, 61. (H) A violin plot of start of first crawling bout for each larva during stimulation. Statistics: Mann–Whitney U test, p < 0.001, n = 159, 71. (I) A summarizing illustration. Basin-2 activates rolling and supresses fast crawling, while SeIN128 decreases Basin-2 activities to inhibit rolling and disinhibit fast crawling. Arrows show activation and blunt ends represent inhibition. **p < 0.01, ***p < 0.001.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/93978/elife-93978-fig8-figsupp1-v1.jpg)

**Figure 8—figure supplement 1.:** (A) and (B) show ethograms of Basin-2 activation (A) and Basin-4 activation (B). Each row represents an individual larva. Pink, blue, green, orange, and purple lines represent bouts of rolling, turning, crawling, backward crawling, and hunching. The red bar and dashed lines denote the time window during the period of neural activation. Genotypes: 20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/+; R38H09-Gal4.DBD/+ (A); 20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/+; R57F07-Gal4.DBD/+ (B). Genotypes in (C) are the same as mentioned here. (C) Cumulative plot of rolling duration. Statistics: Mann–Whitney U test, p < 0.001, n = 681, 141. (D) Time series of rolling probabilities of larvae with Basin-2 activation (black), or SS04185 and Basin-2 co-activation (red). The red bar and dashed lines display the window of optogenetic stimulation eliciting larval escape responses. Shaded areas show 95% confidential intervals of rolling probabilities. Genotypes: 20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/+; R38H09-Gal4.DBD/+ (black); 20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/R54B01-Gal4.AD; R38H09-Gal4.DBD/R46E07-Gal4.DBD (red). Genotypes in (E) are the same as mentioned here. (E) A violin plot of start of first rolling bout for each larva during stimulation. Statistics: Mann–Whitney U test, p < 0.001, n = 57, 38. (F) Time series of rolling probabilities of larvae with Basin-4 activation (black), or SS04185 and Basin-4 co-activation (red). The red bar and dashed lines display the window of optogenetic stimulation eliciting larval escape responses. Shaded areas show 95% confidential intervals of rolling probabilities. Genotypes: 20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/+; R57F07-Gal4.DBD/+ (black); 20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/R54B01-Gal4.AD; R57F07-Gal4.DBD/R46E07-Gal4.DBD (red). Genotypes in (G) are the same as mentioned here. (G) A violin plot of start of first rolling bout for each larva during stimulation. Statistics: Mann–Whitney U test, p > 0.05, n = 129, 61. ***p < 0.001.

To ascertain our expectation that SeIN128 activation would have little if any effect on the pattern of rolling elicited by Basin-4 activation, given the absence of any identifiable synaptic contacts between Basin-4 neurons and SeIN128 neurons based on available information on the larval connectome, we also carried out the same analyses as those described above for rolling elicited by Basin-2 activation. We examined the pattern of rolling evoked by optogenetically activating Basin-4, and found that this manipulation induced rolling mostly within the first 5 s of stimulation (Figure 8—figure supplement 1B, F). Consequently, at the population level, rolling elicited by Basin-4 activation was transient compared to the rolling elicited by Basin-2 activation (compare Figure 8—figure supplement 1A, B; Figure 8—figure supplement 1C).

We then assessed whether SeIN128 activation would affect rolling elicited by Basin-4 activation. Surprisingly, compared to control animals, the probability of rolling in experimental animals was significantly lower (66.7% vs 26.8%; Figure 8E), much as was the case for rolling elicited by Basin-2 activation. We also examined the other rolling parameters, and found that the duration of the rolling bouts (Figure 8F; Mann–Whitney U test, p = 0.032, Cohen’s d = 0.248), time to offset of the first rolling bout (Figure 8G; Mann–Whitney U test, p < 0.0047, Cohen’s d = 0.427), and time to onset of the first crawling bout (Figure 8H; Mann–Whitney U test, p < 0.001, Cohen’s d = 1.039) all significantly decreased in experimental animals compared to controls, although the effect sizes were smaller compared to those observed for rolling elicited by Basin-2 activation. The time to onset of the first rolling bout, however, did not significantly differ between experimental animals and controls (Figure 8—figure supplement 1G). These findings suggest the possibility that sites further downstream of Basin-4 neurons may be involved in inhibitory processes that affect rolling elicited by Basin-4 activation.

## Discussion

In this study, we provide both anatomical and functional evidence that, bilateral descending neurons in the brain of a D. melanogaster larva, which comprise part of a neural circuit underlying a characteristic rolling response that larvae exhibit when evading parasitization by wasps, potentially regulates the termination of rolling and the subsequent transition to escape crawling. We showed that these descending neurons, which we designated as SeIN128, were identical to those previously identified as a component of the nociceptive circuit; were inhibitory neurons that receive excitatory inputs from Basin-2, a second-order interneuron upstream, and A00c, an ascending neuron downstream of Basin-2; and provided GABAergic feedback onto Basin-2, presumably via the axo-axonal synaptic contacts made by the axon terminal endings of SeIN128 neurons onto the axons of Basin-2. Optogenetic activation studies further showed that co-activation of SeIN128 and Basin-2 neurons systematically altered the temporal dynamics of rolling and subsequent escape crawling. Collectively, the evidence suggests that the ensemble of SeIN128, Basin-2, and A00c neurons constitutes a novel inhibitory feedback circuit that reduces Basin-2 activity, which in turn, influences the activity of a key interneuron of the rolling circuit via a novel inhibitory mechanism.

### Feedback inhibition in a nociceptive circuit

Feedback inhibition occurs when an excitatory neuron sends projections to an inhibitory neuron, which in turn sends projections back onto the same excitatory neuron, often at its presynaptic terminals (Isaacson and Scanziani, 2011; Kapfer et al., 2007; Ray et al., 2020; Stokes and Isaacson, 2010; Yoshimura and Callaway, 2005). The hallmark of feedback inhibition lies in its ability to modulate the duration and magnitude of incoming excitatory signals, thereby fine-tuning neural responses and maintaining homeostasis (Kapfer et al., 2007; Papadopoulou et al., 2011; Stokes and Isaacson, 2010; Yoshimura and Callaway, 2005). Compared to the fast temporal dynamics of feedforward inhibition, in which an inhibitory neuron directly inhibits an excitatory neuron downstream of it, the temporal dynamics of feedback inhibition are slower, primarily due to the added synaptic delays (two or more) following activation of an excitatory neuron (Papadopoulou et al., 2011; Ray et al., 2020; Stokes and Isaacson, 2010). The slow temporal dynamics serve to inhibit the sustained neural activity and magnitude of incoming excitatory signals (Papadopoulou et al., 2011; Ray et al., 2020; Stokes and Isaacson, 2010).

In this study, we showed that SeIN128 neurons are descending neurons whose main inputs arrive in the brain and SEZ regions, and whose outputs target the VNC. We also found that SeIN128 neurons receive excitatory inputs from Basin-2 as well as its downstream neuron A00c, and in turn send inhibitory projections back to these neurons in the VNC, potentially establishing a feedback inhibition motif that modulates the nociceptive rolling circuit. The interplay we observed among SeIN128 neurons, Basin-2, and A00c is consistent with this view. Our findings revealed that activation of SeIN128 neurons has a suppressive effect on Basin-2 activity and, notably, on the duration of rolling. These observations support the idea that feedback inhibition is critical in regulating the temporal aspects of nociceptive responses.

### Inhibition of Basin-2 by SeIN128 neurons is mediated by axo-axonal synapses

Neurons form a wide variety of neural networks that perform various computations in the brain. Typically, a neuron receives inputs via axo-dendritic synapses (i.e., contacts made by the axon terminals of an upstream neuron with its dendrites), which play a role in the spatial and temporal computations that lead to the firing of action potentials. Less commonly, the axon terminals of an upstream neuron may contact the soma (i.e., via axo-somatic synapses) or axon (i.e., via axo-axonal synapses) of a downstream neuron (Palay, 1956; Pinault et al., 1997; Zheng et al., 2018). Axo-axonal synapses have a subtle effect on neurotransmission at the network level because the activity in presynaptic neurons does not alter the membrane potential (Cattaert and El Manira, 1999; Guo and Hu, 2014; McGann, 2013). Axo-axonal synapses mainly affect the release probability of neurotransmitter vesicles in response to an action potential triggered in the postsynaptic neuron (McGann, 2013; Oleson et al., 2012).

Recent studies suggest that the activity of axo-axonal synapses can prevent the transmission of action potentials. For example, it has been reported that, neurotransmission mediated by type-B muscarinic receptors at lateral axo-axonal connections between Drosophila Kenyon cells is critical for stimulus specificity learning in Drosophila Manoim et al., 2022; inhibitory axo-axonal connections between Chandelier cells and CA1 pyramidal cells are important for activity-dependent plasticity (Pan-Vazquez et al., 2020; Schneider-Mizell et al., 2021); and GABAergic axo-axonal interneurons in the amygdala are crucial for generating action potentials in the principal output cells (Veres et al., 2023). Furthermore, EM connectome analyses of the entire larval brain reveal that ~70% of all synapses in Drosophila larvae are axo-dendritic whereas ~30% are axo-axonal, suggesting that the latter may have considerable influence over network function (Winding et al., 2023).

In this study, we found a feedback connection between SeIN128 and Basin-2 mediated by axon-axonal synapses (Figure 4—figure supplement 2E–G). The slow increase of SeIN128 activity in response to Basin-2 or A00c activation could potentially occur because of these axo-axonal connections. Alternatively, the slow response in SeIN128 may involve as yet unidentified indirect connections from Basin-2 or A00c to the main inputs in the SEZ region. This delayed activity may play an important role in the feedback inhibition of Basin-2 activity and consequently in the termination of rolling.

### Role of SeIN128 in other escape behaviors

Although the current study focused on rolling, activation of SS04185 neurons appeared to influence other escape behaviors. First, during co-activation of SS04185 and Basins (Figure 1B, lower panel), the frequency of crawling following the initial rolling bout increased, whereas when only the Basins were activated, animals typically showed multiple rolling bouts during the 30-s stimulation period (Figure 1B, upper panel). This observation might be attributed to the strong stimulation induced by Chrimson activation of Basins alone that interrupts crawling via the intrusion of repeated rolling bouts, compared with the co-activation of SS04185 neurons and Basins that reduces the intrusion of rolling. More notably, after either co-activation of SS04185 neurons and Basins (Figure 1B, lower panel) or activation of SS04185 neurons alone (data not shown), the frequency of turning increased upon the cessation (offset) of stimulation, but not following the activation of Basins alone (Figure 1B, upper panel). This second observation suggests the possibility that activation of SS04185 neurons leads to sustained inhibition of turning throughout the stimulation period, which when released upon the offset of stimulation, results in a rebound in the frequency of turning beyond baseline levels. Alternatively, activation of SS04185-MB neurons alone may independently trigger the increase in turning frequency following the offset of stimulation (Figure 1B, Figure 2—figure supplement 1K). A comprehensive examination of this question, however, is beyond the scope of the present study.

### Roles of Basin-2 and Basin-4 in escape behavior

Previous studies have shown that, Basin-2 and Basin-4 receive both chordotonal sensory and nociceptive sensory inputs, and in addition, play a critical role in escape behavior (Ohyama et al., 2015). Here, we investigated the differences between rolling induced by activation of Basin-2 or Basin-4. We found that activation of Basin-2 induced rolling that was sustained. Furthermore, activation of SeIN128 neurons reduced the duration of rolling induced by co-activation of Basin-2, which resulted in a delay in the onset of rolling and an earlier termination of rolling. These data indicate that activation of Basin-2 serves to maintain rolling. Connectome data indicate that SeIN128 neurons provide inhibitory input onto Basin-2, which is consistent with the finding that SeIN128 activation reduces the duration of rolling.

On the other hand, activation of Basin-4 induced rolling that was transient, which was then followed by rapid crawling. Furthermore, activation of SeIN128 neurons reduced the probability of rolling but did not affect the duration of rolling (Figure 8F). This suggests that activation of Basin-4 is important for the induction of rolling, but not its maintenance. The behavioral effects of co-activating SeIN128 and Basin-4, together with connectome data indicating the lack of connections between SeIN128 neurons and Basin-4, suggest that these descending neurons target neurons downstream of Basin-4 neurons.

### Other inputs onto SeIN128 neurons modify escape behavior

The dendritic regions of SeIN128 neurons are located in the SEZ and brain, suggesting that SeIN128 neurons receive other inputs from the SEZ and brain neurons. In this study, we did not examine these inputs. Connectome data indicate that MB output neurons project onto SeIN128 neurons (Ohyama et al., 2015). Given the well-established role of MB neurons in learning, this finding suggests that SeIN128 neurons could play a role in experience-dependent modulation of rolling. Two recent studies have shown that descending neurons inhibit nociceptive neurons (Nakamizo-Dojo et al., 2023; Oikawa et al., 2023). Specifically, one study showed that insulin signaling modulates escape behavior by activating GABAergic descending neurons that inhibit nociceptive sensory neurons (Nakamizo-Dojo et al., 2023), whereas the other demonstrated an inhibitory mechanism mediated by the neuropeptide Drosulfakinin, a homolog of cholecystokinin in mammals (Oikawa et al., 2023). Whether SeIN128 neurons are also influenced by insulin signaling or Drosulfakinin, however, remains to be seen.

### Implications for mechanistic analyses of behavioral sequences

In this study, we did not investigate how crawling is initiated after rolling. Recent studies of the motor circuits underlying rolling and crawling suggest that different premotor neurons are involved in driving each action (Cooney et al., 2023; Kohsaka, 2023; Zarin et al., 2019). When we co-activated SS04185 and Basins, the duration of rolling decreased and the latency to onset of crawling decreased. These data are consistent with the notion that the rolling circuit inhibits the crawling circuit. It would be of interest to examine if premotor crawling neurons are inhibited during rolling, and if so, how they are activated following Basin inhibition to trigger crawling.

In summary, our study delineates a neuronal ensemble consisting of a set of descending inhibitory neurons, a first-order interneuron (Basin-2), and an ascending neuron (A00c) in fruit fly larvae, which functions as an inhibitory feedback circuit that regulates the probability and duration of rolling, and thereby facilitates the transition from rolling to crawling. This work represents another example of how detailed analyses of connectomes and functional analyses of neural and behavioral activity can identify mechanistic explanations of behavioral phenomena at the level of neural circuits—in this case, how neuronal ensembles generate behavioral sequences.

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
      <td>Gene (Drosophila melanogaster)</td>
      <td>Killer Zipper (KZip+)</td>
      <td>Dolan et al., 2017Bloomington Drosophila Stock Center (BDSC)</td>
      <td>RRID:BDRC_76254</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>R72F11-Gal4</td>
      <td>BDSC</td>
      <td>BDSC:39786; RRID:BDRC_39786</td>
      <td>FlyBase: P{GMR72F11-GAL4}</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>R71A10-Gal4</td>
      <td>BDSC</td>
      <td>BDSC:39562; RRID:BDRC_39562</td>
      <td>FlyBase P{GMR71A10-GAL4}</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>SS04185-Gal4</td>
      <td>Gift from Zlatic laboratory</td>
      <td>N/A</td>
      <td>R54B01-Gal4AD; R46E07-Gal4DBD</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>SS00739-Gal4</td>
      <td>Gift from Zlatic laboratory</td>
      <td>N/A</td>
      <td>R72F11-Gal4AD;R38H09-Gal4DBD</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>SS00740-Gal4</td>
      <td>Gift from Zlatic laboratory</td>
      <td>N/A</td>
      <td>R72F11-Gal4AD;R57F07-Gal4DBD</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>MB247-Gal4</td>
      <td>BDSC</td>
      <td>BDRC:50742; RRID:BDRC_50742</td>
      <td>FlyBase P{Mef2-GAL4.247}</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>R13F02-LexA</td>
      <td>BDSC</td>
      <td>BDRC:52460; RRID:BDRC_52460</td>
      <td>FlyBase P{GMR13F02-lexA}</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>R72F11-LexA</td>
      <td>BDSC</td>
      <td>BDRC:94661;RRID:BDRC_94661</td>
      <td>FlyBase P{GMR72F11-lexA}</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>R71A10-LexA</td>
      <td>Gift from Zlatic lab</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>Mi{Trojan-LexA-QFAD.2}Gad1</td>
      <td>BDSC</td>
      <td>BDRC:60324; RRID:BDRC_60324</td>
      <td>FlyBase Mi{Trojan-lexA:QFAD.2}</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>20xUAS-IVS-CsChrimson::mVenus</td>
      <td>BDSC</td>
      <td>BDRC:55134; RRID:BDRC_55134</td>
      <td>FlyBase P{20XUAS-IVS-CsChrimson.mVenus}</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>20xUAS-IVS-CsChrimson::mVenus</td>
      <td>BDSC</td>
      <td>BDRC:55136; RRID:BDRC_55136</td>
      <td>FlyBase P{20XUAS-IVS-CsChrimson.mVenus}</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>13xLexAop2-IVS-CsChrimson::mVenus</td>
      <td>BDSC</td>
      <td>BDRC:55137; RRID:BDRC_55137</td>
      <td>FlyBase P{13XLexAop2-IVS-CsChrimson.mVenus}</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>13xLexAop2-IVS-CsChrimson::tdTomato</td>
      <td>Gift from Rubin lab</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>13xLexAop2-IVS-CsChrimson::tdTomato</td>
      <td>BDSC</td>
      <td>BDRC:82183; RRID:BDRC_82183</td>
      <td>FlyBase PBac{13XLexAop2-IVS-CsChrimson.tdTomato}</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>20xUAS(FRT.stop)CsChrimson.mVenus(attP18), pBPhsFlp2::Pest</td>
      <td>Gift from Rubin lab</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>hs(KDRT.stop)FLP</td>
      <td>BDSC</td>
      <td>BDRC:67091; RRID:BDRC_67091</td>
      <td>FlyBase symbol: P{hs(KDRT.stop)FLP}</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>20xUAS(FRT.stop)CsChrimson::mVenus</td>
      <td>Gift from Rubin lab</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-TeTxLC.tnt</td>
      <td>BDSC</td>
      <td>BDRC:28838; RRID:BDRC_28838</td>
      <td>FlyBase symbol: P{UAS-TeTxLC.tnt}</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>20xUAS-TTS-Shibirets1-p10</td>
      <td>BDSC</td>
      <td>BDRC:66600; RRID:BDRC_66600</td>
      <td>FlyBase PBac{20XUAS-TTS-shits1-p10}</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>10xUAS-IVS-mry::GFP</td>
      <td>Gift from Rubin lab</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>13xLexAop-dsRed</td>
      <td>Gift from Rubin lab</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>20xUAS-IVS-GCaMP6s</td>
      <td>BDSC</td>
      <td>BDRC:42749; RRID:BDRC_42749</td>
      <td>FlyBase PBac{20XUAS-IVS-GCaMP6s}</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>20xLexAop-IVS-Syn21-GCaMP6s</td>
      <td>Gift from Rubin lab</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>20xUAS-Syn21-opGCaMP6s</td>
      <td>Gift from Rubin lab</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>10xUAS-Syn21-CsChrimson88::tdTomato</td>
      <td>Gift from Rubin lab</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>HMS02355</td>
      <td>BDSC</td>
      <td>BDRC:41958; RRID:BDRC_41958</td>
      <td>FlyBase P{TRiP.HMS02355}</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>HMC03388</td>
      <td>BDSC</td>
      <td>BDRC:51817; RRID:BDRC_51817</td>
      <td>FlyBase P{TRiP.HMC03388}</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>JF02989</td>
      <td>BDSC</td>
      <td>BDRC:28353; RRID:BDRC_28353</td>
      <td>FlyBase P{TRiP.JF02989}</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>HMC02975</td>
      <td>BDSC</td>
      <td>BDRC:50608; RRID:BDRC_50608</td>
      <td>FlyBase P{TRiP.HMC02975}</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>HMC03643</td>
      <td>BDSC</td>
      <td>BDRC:52903; RRID:BDRC_52903</td>
      <td>FlyBase P{TRiP.HMC03643}</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Brp, clone nc82 (Mouse monoclonal)</td>
      <td>Developmental Studies Hybridoma Bank</td>
      <td>Cat#: nc82,RRID:AB_2314866</td>
      <td>IHC (1:50)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>1D4 anti-fasciclin II (Mouse monoclonal)</td>
      <td>Developmental Studies Hybridoma Bank</td>
      <td>Cat#: 1D4 anti-Fasciclin II,RRID:AB_528235</td>
      <td>IHC (1:20)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-cadherin, DN-(extracellular domain) (Rat monoclonal)</td>
      <td>Developmental Studies Hybridoma Bank</td>
      <td>Cat#: DN-Ex #8, RRID:AB_528121</td>
      <td>IHC (1:20)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-GFP (Chicken polyclonal)</td>
      <td>Abcam</td>
      <td>Cat#:ab13970, RRID:AB_300798</td>
      <td>IHC (1:3000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-GFP (Rabbit polyclonal)</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#:A-6455, RRID:AB_221570</td>
      <td>IHC (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-DsRed (Rabbit polyclonal)</td>
      <td>Takara Bio</td>
      <td>Cat#:632496, RRID:AB_10013483</td>
      <td>IHC (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Drosophila choline acetyltransferase (Mouse monoclonal)</td>
      <td>Developmental Studies Hybridoma Bank</td>
      <td>Cat#:chat4b1, RRID:AB_528122</td>
      <td>IHC (1:20)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-GABA (Rabbit polyclonal)</td>
      <td>Millipore Sigma</td>
      <td>Cat#:A2052</td>
      <td>IHC (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Drosophila VGLUT (Rabbit polyclonal)</td>
      <td>Gift from McCabe laboratory; Banerjee et al., 2021</td>
      <td></td>
      <td>IHC (1:20)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-VGAT (Rabbit polyclonal)</td>
      <td>Gift from Krantz laboratory; Fei et al., 2010</td>
      <td></td>
      <td>IHC (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Elav (Rat polyclonal)</td>
      <td>Developmental Studies Hybridoma Bank</td>
      <td>Cat#:7E8A10, RRID:AB_528218</td>
      <td>IHC (1:50)</td>
    </tr>
    <tr>
      <td>Antibody (secondary)</td>
      <td>anti-chicken IgY (H+L) Alexa Fluor 488 (Goat polyclonal)</td>
      <td>Thermo FisherScientific</td>
      <td>Cat#:A-11039,RRID:AB_2534096</td>
      <td>IHC (1:500)</td>
    </tr>
    <tr>
      <td>Antibody (secondary)</td>
      <td>anti-rabbit IgG (H+L) Alexa Fluor 488 (Goat polyclonal)</td>
      <td>Thermo FisherScientific</td>
      <td>Cat#:A-11034, RRID:AB_ 2576217</td>
      <td>IHC (1:500)</td>
    </tr>
    <tr>
      <td>Antibody (secondary)</td>
      <td>anti-rabbit IgG (H+L) Alexa Fluor 568 (Goat polyclonal)</td>
      <td>Thermo FisherScientific</td>
      <td>Cat#:A-11011, RRID:AB_143157</td>
      <td>IHC (1:500)</td>
    </tr>
    <tr>
      <td>Antibody (secondary)</td>
      <td>anti-mouse IgG (H+L) Alexa Fluor 568 (Goat polyclonal)</td>
      <td>Thermo FisherScientific</td>
      <td>Cat#:A-11004, RRID:AB_2534072</td>
      <td>IHC (1:500)</td>
    </tr>
    <tr>
      <td>Antibody (secondary)</td>
      <td>anti-rat IgG (H+L) Alexa Fluor 568 (Goat polyclonal)</td>
      <td>Thermo FisherScientific</td>
      <td>Cat#:A-11077, RRID:AB_2534121</td>
      <td>IHC (1:500)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>PBS, phosphate-buffered saline, 10× solution</td>
      <td>Fisher Scientific</td>
      <td>Cat#:BP399-1</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Triton X-100</td>
      <td>Millipore Sigma</td>
      <td>Cat#:X100-100ML</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Paraformaldehyde 20% aqueous solution</td>
      <td>Electron MicroscopySciences</td>
      <td>Cat#:15713</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Normal goat serum</td>
      <td>Gibco</td>
      <td>Cat#:PCN5000</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>VECTASHIELD antifade mounting medium</td>
      <td>Vector Laboratories</td>
      <td>Cat#:H-1000-10</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Drosophila Agar</td>
      <td>Diamed</td>
      <td>Cat#:GEN66-103</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>All Trans Retinal</td>
      <td>Toronto ResearchChemicals Inc</td>
      <td>Cat#:R24000</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Poly-L-lysine</td>
      <td>Sigma-Aldrich</td>
      <td>Cat#:P1524</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>FIJI</td>
      <td>https://fiji.sc/</td>
      <td>RRID:SCR_002285</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MATLAB</td>
      <td>MathWorks</td>
      <td>RRID:SCR_001622</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>CATMAID</td>
      <td>https://catmaid.readthedocs.org/</td>
      <td>RRID:SCR_006278</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Multi Worm Tracker</td>
      <td>http://sourceforge.net/projects/mwt</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ZEN</td>
      <td>Carl Zeiss Microscopy</td>
      <td>Version 2.1</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Affinity Designer</td>
      <td>Affinity</td>
      <td>Version 1.10.5</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ScanImage</td>
      <td>MBF Bioscience</td>
      <td>N/A</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Fly stocks and maintenance

All D. melanogaster stock lines used in this study were raised on Bloomington Drosophila Stock Center cornmeal food. Flies were maintained in a humidity- and temperature-controlled chamber kept at 18 or 25°C, 40% humidity, and set to a 12-hr light/dark cycle. All crosses for experiments were reared at 25°C and 40% humidity.

### Heat shock FlpOut mosaic expression

First instar Drosophila larvae were heat shocked in water bath at 37°C for 12 min as previously reported (Nern et al., 2015). With the precise temporal and temperature control of heat shock, larvae with the genotype of w+, hs(KDRT.stop)FLP/13xLexAop2-IVS-CsChrimson::tdTomato; R54B01-Gal4.AD/72F11-LexA;20xUAS-(FRT.stop)-CsChrimson::mVenus/R46E07-Gal4.DBD had sporadic CsChrimson::mVenus expression driven by SS04185 split GAL4. As a result, the ratio of the larvae with SS04185-DN and SS04185-MB expression to those with only SS04185-MB expression was 1:1. Each individual larva was individually examined with optogenetic stimulation and behavior analysis. After behavioral experiments, mVenus expression in CNS was confirmed under the fluorescence microscope.

### Fly genotypes used in experiments

#### Main figures

<table>
  <thead>
    <tr>
      <th>Fig.</th>
      <th>Panel</th>
      <th>Labels</th>
      <th>Genotypes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>B</td>
      <td>Basins&gt;Chrimson</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+;+; R72F11-Gal4/+</td>
    </tr>
    <tr>
      <td>1</td>
      <td>B</td>
      <td>Basins+SS04185&gt;Chrimson</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/ R72F11-Gal4</td>
    </tr>
    <tr>
      <td>1</td>
      <td>C, D, F</td>
      <td>control</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; +; R72F11-Gal4/+</td>
    </tr>
    <tr>
      <td>1</td>
      <td>C, D, F</td>
      <td>SS04185</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/R72F11-Gal4</td>
    </tr>
    <tr>
      <td>1</td>
      <td>E</td>
      <td>ctrl/attp2&gt;Chrimson</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+;;</td>
    </tr>
    <tr>
      <td>1</td>
      <td>E</td>
      <td>SS04185/attp2&gt;Chrimson</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/+</td>
    </tr>
    <tr>
      <td>1</td>
      <td>E</td>
      <td>ctrl/Basins&gt;Chrimson</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; +; R72F11-Gal4/+</td>
    </tr>
    <tr>
      <td>1</td>
      <td>E</td>
      <td>SS04185/Basins&gt;Chrimson</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/R72F11-Gal4</td>
    </tr>
    <tr>
      <td>1</td>
      <td>G–I</td>
      <td>ctrl</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; +; R72F11-Gal4/+</td>
    </tr>
    <tr>
      <td>1</td>
      <td>G–I</td>
      <td>SS04185</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/R72F11-Gal4</td>
    </tr>
    <tr>
      <td>2</td>
      <td>A</td>
      <td></td>
      <td>10xUAS-IVS-myr::GFP/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/+</td>
    </tr>
    <tr>
      <td>2</td>
      <td>B</td>
      <td>control</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/R72F11-Gal4</td>
    </tr>
    <tr>
      <td>2</td>
      <td>B</td>
      <td>MB&gt;KZip+</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R13F02-LexA,LexAop-KZip+/R54B01-Gal4.AD; R72F11-Gal4/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>2</td>
      <td>C, E</td>
      <td>MB&gt;KZip+/ctrl</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R13F02-LexA,LexAop-KZip+/+; R72F11-Gal4/+</td>
    </tr>
    <tr>
      <td>2</td>
      <td>C, E</td>
      <td>-/SS04185</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/R72F11-Gal4</td>
    </tr>
    <tr>
      <td>2</td>
      <td>C, E</td>
      <td>MB&gt;KZip+/SS04185</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R13F02-LexA,LexAop-KZip+/R54B01-Gal4.AD; R72F11-Gal4/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>2</td>
      <td>D</td>
      <td>MB&gt;KZip+</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R13F02-LexA,LexAop-KZip+/+; R72F11-Gal4/+</td>
    </tr>
    <tr>
      <td>2</td>
      <td>D</td>
      <td>SS04185</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/R72F11-Gal4</td>
    </tr>
    <tr>
      <td>2</td>
      <td>D</td>
      <td>MB&gt;KZip+, SS04185</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R13F02-LexA,LexAop-KZip+/R54B01-Gal4.AD; R72F11-Gal4/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>2</td>
      <td>F, H</td>
      <td>ctrl</td>
      <td>w+, hs(KDRT.stop)FLP/13xLexAop2-IVS-CsChrimson::tdTomato; R54B01-Gal4.AD/72F11-LexA;20xUAS-(FRT.stop)-CsChrimson::mVenus/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>2</td>
      <td>F, H</td>
      <td>SS04185-DN</td>
      <td>w+, hs(KDRT.stop)FLP/13xLexAop2-IVS-CsChrimson::tdTomato; R54B01-Gal4.AD/72F11-LexA;20xUAS-(FRT.stop)-CsChrimson::mVenus/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>2</td>
      <td>G</td>
      <td>control</td>
      <td>w+, hs(KDRT.stop)FLP/13xLexAop2-IVS-CsChrimson::tdTomato; R54B01-Gal4.AD/72F11-LexA;20xUAS-(FRT.stop)-CsChrimson::mVenus/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>2</td>
      <td>G</td>
      <td>SS04185-DN</td>
      <td>w+, hs(KDRT.stop)FLP/13xLexAop2-IVS-CsChrimson::tdTomato; R54B01-Gal4.AD/72F11-LexA;20xUAS-(FRT.stop)-CsChrimson::mVenus/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>3</td>
      <td>D, E</td>
      <td></td>
      <td>10xUAS-IVS-myr::GFP/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/+</td>
    </tr>
    <tr>
      <td>3</td>
      <td>F</td>
      <td></td>
      <td>w; R54B01-Gal4.AD/R72F11-LexA; R46E07-Gal4.DBD/13xLexAop2-IVS-CsChrimson::tdTomato, 20xUAS-IVS-GCaMP6s</td>
    </tr>
    <tr>
      <td>3</td>
      <td>H</td>
      <td></td>
      <td>w; R54B01-Gal4.AD/R71A10-LexA; R46E07-Gal4.DBD/13xLexAop2-IVS-CsChrimson::tdTomato, 20xUAS-IVS-GCaMP6s</td>
    </tr>
    <tr>
      <td>3</td>
      <td>J</td>
      <td></td>
      <td>w; R54B01-Gal4.AD/ppk1.9-LexA; R46E07-Gal4.DBD/13xLexAop2-IVS-CsChrimson::tdTomato, 20xUAS-IVS-GCaMP6s</td>
    </tr>
    <tr>
      <td>4</td>
      <td>B</td>
      <td></td>
      <td>w; R72F11-LexA/R54B01-Gal4.AD; 13xLexAop-CsChrimson, 20xUAS-IVS-UAS-GCaMP6s/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>4</td>
      <td>C</td>
      <td></td>
      <td>w; R71A10-LexA/R54B01-Gal4.AD; 13xLexAop-CsChrimson, 20xUAS-IVS-UAS-GCaMP6s/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>4</td>
      <td>D</td>
      <td></td>
      <td>w; R72F11-LexA/+; 13xLexAop2-IVS -CsChrimson::tdTomato, 20xUAS-IVS-UAS-GCaMP6s/R71A10-Gal4</td>
    </tr>
    <tr>
      <td>4</td>
      <td>E</td>
      <td>A00c</td>
      <td>w; R72F11-LexA/+; 13xLexAop2-IVS -CsChrimson::tdTomato, 20xUAS-IVS-UAS-GCaMP6s/R71A10-Gal4</td>
    </tr>
    <tr>
      <td>4</td>
      <td>E</td>
      <td>SS04185</td>
      <td>w; R72F11-LexA/R54B01-Gal4.AD; 13xLexAop2-IVS -CsChrimson::tdTomato, 20xUAS-IVS-UAS-GCaMP6s/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>5</td>
      <td>A</td>
      <td></td>
      <td>10xUAS-myr::GFP; R54B01-Gal4.AD/13x-LexAop-dsRed; R46E07-Gal4.DBD/ Mi{Trojan-LexA-QFAD.2}Gad1</td>
    </tr>
    <tr>
      <td>5</td>
      <td>B, D</td>
      <td>control</td>
      <td>13xLexAop2-IVS-CsChrimson::mVenus;R72F11-lexA/+; HMS02355/+</td>
    </tr>
    <tr>
      <td>5</td>
      <td>B, D</td>
      <td>SS04185</td>
      <td>13xLexAop2-IVS-CsChrimson::mVenus; R72F11-lexA/R54B01-Gal4.AD; HMS02355/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>5</td>
      <td>C</td>
      <td>ctrl</td>
      <td>13xLexAop2-IVS-CsChrimson::mVenus;R72F11-lexA/+; HMS02355/+</td>
    </tr>
    <tr>
      <td>5</td>
      <td>C</td>
      <td>SS04185</td>
      <td>13xLexAop2-IVS-CsChrimson::mVenus; R72F11-lexA/R54B01-Gal4.AD; HMS02355/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>6</td>
      <td>A</td>
      <td>control&gt;TNT</td>
      <td>13xLexAop2-IVS-CsChrimson::mVenus; R72F11-LexA/+; UAS-TeTxLC.tnt /+</td>
    </tr>
    <tr>
      <td>6</td>
      <td>A</td>
      <td>SS04185&gt;TNT</td>
      <td>13xLexAop2-IVS-CsChrimson::mVenus; R72F11-LexA/R54B01-Gal4.AD; UAS-TeTxLC.tnt/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>6</td>
      <td>B, D–F</td>
      <td>ctrl</td>
      <td>13xLexAop2-IVS-CsChrimson::mVenus; R72F11-LexA/+; UAS-TeTxLC.tnt /+</td>
    </tr>
    <tr>
      <td>6</td>
      <td>B, D–F</td>
      <td>SS04185</td>
      <td>13xLexAop2-IVS-CsChrimson::mVenus; R72F11-LexA/R54B01-Gal4.AD; UAS-TeTxLC.tnt/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>6</td>
      <td>C</td>
      <td>control</td>
      <td>13xLexAop2-IVS-CsChrimson::mVenus; R72F11-LexA/+; UAS-TeTxLC.tnt /+</td>
    </tr>
    <tr>
      <td>6</td>
      <td>C</td>
      <td>SS04185</td>
      <td>13xLexAop2-IVS-CsChrimson::mVenus; R72F11-LexA/R54B01-Gal4.AD; UAS-TeTxLC.tnt/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>7</td>
      <td>A, B</td>
      <td>control</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+;; R72F11-Gal4/+</td>
    </tr>
    <tr>
      <td>7</td>
      <td>A, B</td>
      <td>GABA-B-R11</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+;; R72F11-Gal4/UAS-HMC03388</td>
    </tr>
    <tr>
      <td>7</td>
      <td>A, B</td>
      <td>GABA-B-R12</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+;; R72F11-Gal4/UAS-JF02989</td>
    </tr>
    <tr>
      <td>7</td>
      <td>A, B</td>
      <td>GABA-B-R2</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+;; R72F11-Gal4/UAS-HMC02975</td>
    </tr>
    <tr>
      <td>7</td>
      <td>A, B</td>
      <td>GABA-A-R</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+;; R72F11-Gal4/UAS-HMC03643</td>
    </tr>
    <tr>
      <td>7</td>
      <td>C</td>
      <td>control</td>
      <td>20xUAS-Syn21-opGCaMP6s,10xUAS-Syn21-CsChrimson88::tdTomato/+;CyO/+;TM6/R72F11-Gal4</td>
    </tr>
    <tr>
      <td>7</td>
      <td>C</td>
      <td>SS04185</td>
      <td>20xUAS-Syn21-opGCaMP6s,10xUAS-Syn21-CsChrimson88::tdTomato/+;CyO/R54B01-Gal4.AD;R72F11-Gal4/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>8</td>
      <td>A, C, D</td>
      <td>ctrl</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/+; R38H09-Gal4.DBD/+</td>
    </tr>
    <tr>
      <td>8</td>
      <td>A, C, D</td>
      <td>SS04185</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/R54B01-Gal4.AD; R38H09-Gal4.DBD/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>8</td>
      <td>B</td>
      <td>control</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/+; R38H09-Gal4.DBD/+</td>
    </tr>
    <tr>
      <td>8</td>
      <td>B</td>
      <td>SS04185</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/R54B01-Gal4.AD; R38H09-Gal4.DBD/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>8</td>
      <td>E, G, H</td>
      <td>ctrl</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/+; R57F07-Gal4.DBD/+</td>
    </tr>
    <tr>
      <td>8</td>
      <td>E, G, H</td>
      <td>SS04185</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/R54B01-Gal4.AD; R57F07-Gal4.DBD/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>8</td>
      <td>F</td>
      <td>control</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/+; R57F07-Gal4.DBD/+</td>
    </tr>
    <tr>
      <td>8</td>
      <td>F</td>
      <td>SS04185</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/R54B01-Gal4.AD; R57F07-Gal4.DBD/R46E07-Gal4.DBD</td>
    </tr>
  </tbody>
</table>

#### Figure supplements

<table>
  <thead>
    <tr>
      <th>Fig.</th>
      <th>Panel</th>
      <th>Labels</th>
      <th>Genotypes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>1–1</td>
      <td>A–D</td>
      <td>ctrl</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+;;</td>
    </tr>
    <tr>
      <td>1–1</td>
      <td>A–D</td>
      <td>SS04185</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/+</td>
    </tr>
    <tr>
      <td>1–1</td>
      <td>E, G, H</td>
      <td>ctrl</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; +; R72F11-Gal4/+</td>
    </tr>
    <tr>
      <td>1–1</td>
      <td>E, G, H</td>
      <td>SS04185</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/R72F11-Gal4</td>
    </tr>
    <tr>
      <td>1–1</td>
      <td>F</td>
      <td>control</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; +; R72F11-Gal4/+</td>
    </tr>
    <tr>
      <td>1–1</td>
      <td>F</td>
      <td>SS04185</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/R72F11-Gal4</td>
    </tr>
    <tr>
      <td>1–1</td>
      <td>I</td>
      <td>ctrl/attp2&gt;Chrimson</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+;;</td>
    </tr>
    <tr>
      <td>1–1</td>
      <td>I</td>
      <td>SS04185/attp2&gt;Chrimson</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/+</td>
    </tr>
    <tr>
      <td>1–1</td>
      <td>I</td>
      <td>ctrl/Basins&gt;Chrimson</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; +; R72F11-Gal4/+</td>
    </tr>
    <tr>
      <td>1–1</td>
      <td>I</td>
      <td>SS04185/Basins&gt;Chrimson</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/R72F11-Gal4</td>
    </tr>
    <tr>
      <td>1–2</td>
      <td>A–C</td>
      <td>control</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+;; R72F11-Gal4/+</td>
    </tr>
    <tr>
      <td>1–2</td>
      <td>A–C</td>
      <td>54B01-AD</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R72F11-Gal4/+</td>
    </tr>
    <tr>
      <td>1–2</td>
      <td>A–C</td>
      <td>46E07-DBD</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; +; R72F11-Gal4/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>1–2</td>
      <td>A–C</td>
      <td>SS04185</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/R72F11-Gal4</td>
    </tr>
    <tr>
      <td>2</td>
      <td>A</td>
      <td></td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R13F02-LexA,LexAop-KZip+/R54B01-Gal4.AD; R72F11-Gal4/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>2</td>
      <td>B</td>
      <td>MB&gt;Kzip+</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R13F02-LexA,LexAop-Kzip+/+; R72F11-Gal4/+</td>
    </tr>
    <tr>
      <td>2</td>
      <td>B</td>
      <td>SS04185</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/R72F11-Gal4</td>
    </tr>
    <tr>
      <td>2</td>
      <td>B</td>
      <td>MB&gt;Kzip+, SS04185</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R13F02-LexA,LexAop-Kzip+/R54B01-Gal4.AD; R72F11-Gal4/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>2</td>
      <td>C</td>
      <td>MB&gt;Kzip+/ctrl</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R13F02-LexA,LexAop-Kzip+/+; R72F11-Gal4/+</td>
    </tr>
    <tr>
      <td>2</td>
      <td>C</td>
      <td>-/SS04185</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/R72F11-Gal4</td>
    </tr>
    <tr>
      <td>2</td>
      <td>C</td>
      <td>MB&gt;Kzip+/SS04185</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R13F02-LexA,LexAop-Kzip+/R54B01-Gal4.AD; R72F11-Gal4/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>2</td>
      <td>D</td>
      <td>control</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; +; R72F11-Gal4/+</td>
    </tr>
    <tr>
      <td>2</td>
      <td>D</td>
      <td>MB247</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/R72F11-Gal4</td>
    </tr>
    <tr>
      <td>2</td>
      <td>E</td>
      <td>ctrl</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; +; R72F11-Gal4/+</td>
    </tr>
    <tr>
      <td>2</td>
      <td>E</td>
      <td>MB247</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/R72F11-Gal4</td>
    </tr>
    <tr>
      <td>2</td>
      <td>F, G</td>
      <td></td>
      <td>w+, hs(KDRT.stop)FLP/13xLexAop-CsChrimson::tdTomato; R54B01-Gal4.AD/72F11-LexA;20xUAS-(FRT.stop)-CsChrimson::mVenus/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>2</td>
      <td>H</td>
      <td>control</td>
      <td>w+, hs(KDRT.stop)FLP/13xLexAop-CsChrimson::tdTomato; R54B01-Gal4.AD/72F11-LexA; 20xUAS-(FRT.stop)-CsChrimson::mVenus/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>2</td>
      <td>H</td>
      <td>SS04185-DN</td>
      <td>w+, hs(KDRT.stop)FLP/13xLexAop-CsChrimson::tdTomato; R54B01-Gal4.AD/72F11-LexA; 20xUAS-(FRT.stop)-CsChrimson::mVenus/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>2</td>
      <td>I, J</td>
      <td>ctrl</td>
      <td>w+, hs(KDRT.stop)FLP/13xLexAop-CsChrimson::tdTomato; R54B01-Gal4.AD/72F11-LexA; 20xUAS-(FRT.stop)-CsChrimson::mVenus/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>2</td>
      <td>I, J</td>
      <td>SS04185-DN</td>
      <td>w+, hs(KDRT.stop)FLP/13xLexAop-CsChrimson::tdTomato; R54B01-Gal4.AD/72F11-LexA; 20xUAS-(FRT.stop)-CsChrimson::mVenus/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>4</td>
      <td>B</td>
      <td>Basins&gt;Chrimson</td>
      <td>w; R72F11-LexA/R54B01-Gal4.AD; 13xLexAop2-IVS -CsChrimson::tdTomato, 20xUAS-IVS- GCaMP6s/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>4</td>
      <td>B</td>
      <td>A00c&gt;Chrimson</td>
      <td>w; R71A10-LexA/R54B01-Gal4.AD; 13xLexAop2-IVS -CsChrimson::tdTomato, 20xUAS-IVS-GCaMP6s/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>4</td>
      <td>C</td>
      <td>SeIN128 (Basins&gt;Chrimson)</td>
      <td>w; R72F11-LexA/R54B01-Gal4.AD; 13xLexAop2-IVS -CsChrimson::tdTomato, 20xUAS-IVS- GCaMP6s/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>4</td>
      <td>C</td>
      <td>SeIN128 (A00c&gt;Chrimson)</td>
      <td>w; R71A10-LexA/R54B01-Gal4.AD; 13xLexAop2-IVS -CsChrimson::tdTomato, 20xUAS-IVS-GCaMP6s/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>4</td>
      <td>C</td>
      <td>A00c (Basins&gt;Chrimson)</td>
      <td>w; R72F11-LexA/+; 13xLexAop2-IVS -CsChrimson::tdTomato, 20xUAS-IVS-GCaMP6s/R71A10-Gal4</td>
    </tr>
    <tr>
      <td>5</td>
      <td>A, B</td>
      <td></td>
      <td>10xUAS-IVS-myr::GFP/+; R54B01-Gal4.AD/+; R46E07-Gal4.DBD/+</td>
    </tr>
    <tr>
      <td>5</td>
      <td>C, D</td>
      <td>ctrl</td>
      <td>w;; R57C10-Gal4/+</td>
    </tr>
    <tr>
      <td>5</td>
      <td>C, D</td>
      <td>VGAT-RNAi</td>
      <td>w;; R57C10-Gal4/UAS-HMS02355</td>
    </tr>
    <tr>
      <td>6</td>
      <td>A, D</td>
      <td>control</td>
      <td>13xLexAop2-IVS-CsChrimson::mVenus; R72F11-LexA/+; 20xUAS-TTS-Shibirets1/+</td>
    </tr>
    <tr>
      <td>6</td>
      <td>A, D</td>
      <td>SS04185</td>
      <td>13xLexAop2-IVS-CsChrimson::mVenus; R72F11-LexA/R54B01-Gal4.AD; 20xUAS-TTS-Shibirets1/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>6</td>
      <td>B, C, E–G</td>
      <td>ctrl</td>
      <td>13xLexAop2-IVS-CsChrimson::mVenus; R72F11-LexA/+; 20xUAS-TTS-Shibirets1/+</td>
    </tr>
    <tr>
      <td>6</td>
      <td>B, C, E–G</td>
      <td>SS04185</td>
      <td>13xLexAop2-IVS-CsChrimson::mVenus; R72F11-LexA/R54B01-Gal4.AD; 20xUAS-TTS-Shibirets1/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>7</td>
      <td>A–D</td>
      <td>control</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+;; R72F11-Gal4/+</td>
    </tr>
    <tr>
      <td>7</td>
      <td>A–D</td>
      <td>GABA-B-R11</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+;; R72F11-Gal4/UAS-HMC03388</td>
    </tr>
    <tr>
      <td>7</td>
      <td>A–D</td>
      <td>GABA-B-R12</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+;; R72F11-Gal4/UAS-JF02989</td>
    </tr>
    <tr>
      <td>7</td>
      <td>A–D</td>
      <td>GABA-B-R2</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+;; R72F11-Gal4/UAS-HMC02975</td>
    </tr>
    <tr>
      <td>7</td>
      <td>A–D</td>
      <td>GABA-A-R</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+;; R72F11-Gal4/UAS-HMC03643</td>
    </tr>
    <tr>
      <td>7</td>
      <td>E</td>
      <td>Basins&gt;Chrimson</td>
      <td>20xUAS-Syn21-opGCaMP6s,10xUAS-Syn21-CsChrimson88::tdTomato/+;CyO/+;TM6/R72F11-Gal4</td>
    </tr>
    <tr>
      <td>7</td>
      <td>F</td>
      <td>Basins+SeIN128&gt;Chrimson</td>
      <td>20xUAS-Syn21-opGCaMP6s,10xUAS-Syn21-CsChrimson88::tdTomato/+;CyO/R54B01-Gal4.AD;R72F11-Gal4/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>8</td>
      <td>A</td>
      <td>Basin2&gt;Chrimson</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/+; R38H09-Gal4.DBD/+</td>
    </tr>
    <tr>
      <td>8</td>
      <td>B</td>
      <td>Basin4&gt;Chrimson</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/+; R57F07-Gal4.DBD/+</td>
    </tr>
    <tr>
      <td>8</td>
      <td>C</td>
      <td>Basin-2</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/+; R38H09-Gal4.DBD/+</td>
    </tr>
    <tr>
      <td>8</td>
      <td>C</td>
      <td>Basin-4</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/+; R57F07-Gal4.DBD/+</td>
    </tr>
    <tr>
      <td>8</td>
      <td>D</td>
      <td>control</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/+; R38H09-Gal4.DBD/+</td>
    </tr>
    <tr>
      <td>8</td>
      <td>D</td>
      <td>SS04185</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/R54B01-Gal4.AD; R38H09-Gal4.DBD/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>8</td>
      <td>E</td>
      <td>ctrl</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/+; R38H09-Gal4.DBD/+</td>
    </tr>
    <tr>
      <td>8</td>
      <td>E</td>
      <td>SS04185</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/R54B01-Gal4.AD; R38H09-Gal4.DBD/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>8</td>
      <td>F</td>
      <td>control</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/+; R57F07-Gal4.DBD/+</td>
    </tr>
    <tr>
      <td>8</td>
      <td>F</td>
      <td>SS04185</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/R54B01-Gal4.AD; R57F07-Gal4.DBD/R46E07-Gal4.DBD</td>
    </tr>
    <tr>
      <td>8</td>
      <td>G</td>
      <td>ctrl</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/+; R57F07-Gal4.DBD/+</td>
    </tr>
    <tr>
      <td>8</td>
      <td>G</td>
      <td>SS04185</td>
      <td>20xUAS-IVS-CsChrimson::mVenus/+; R72F11-Gal4.AD/R54B01-Gal4.AD; R57F07-Gal4.DBD/R46E07-Gal4.DBD</td>
    </tr>
  </tbody>
</table>

### Behavior assay

To optogenetically stimulate neurons, embryos were collected for 24 hr and larvae were raised on fly food plates with 0.2 mM trans-retinal (Toronto Research Chemicals, R240000). The larvae were kept in the dark at 25°C for 4 days to grow to the third instar stage. Before the experiment, food plates with larvae were rinsed with a 15% sucrose solution to separate the larvae from the food. Larvae were then moved to a sieve, washed with water, dried, and placed evenly on 2% agar plates. The agar plate with animals were placed under a camera in the arena of the behavior rig.

#### Behavior apparatus

The behavior rig consisted of several apparatuses (see Ohyama et al., 2013 for details and modified by following), including a C-MOS camera (Grasshopper Camera USB3, GS3-U3-41C6M-C, FLIR), infrared 850 nm LED illumination (Waveform Lighting Co), a 624 nm (LED, Waveform Lighting Co), for optogenetic manipulations, a computer, and a heating panel. Both the camera and LED source were controlled by the computer. LED stimuli were controlled by customized software while larval behaviors were recorded using the Multi-Worm Tracker (MWT) software, a real-time image-analysis software (Swierczek et al., 2011). These two pieces of software were synchronized in the behavior assay to precisely deliver the stimulation during specified time windows.

#### Optogenetic stimulation

Before delivering optogenetic stimulation, larvae were placed in the arena for 45 s. Subsequently, two 30 s 624 nm LED stimuli were presented successively with a 30-s interval between them. The LED intensity used in each experiment is shown below.

<table>
  <thead>
    <tr>
      <th>Figure number</th>
      <th>Optogenetic stimulation irradiance (μW/mm2)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Figure 1</td>
      <td>0.84</td>
    </tr>
    <tr>
      <td>Figure 1—figure supplement 1</td>
      <td>0.84</td>
    </tr>
    <tr>
      <td>Figure 1—figure supplement 2</td>
      <td>0.48</td>
    </tr>
    <tr>
      <td>Figure 2C–E</td>
      <td>5.9</td>
    </tr>
    <tr>
      <td>Figure 2F–H</td>
      <td>1.8</td>
    </tr>
    <tr>
      <td>Figure 2—figure supplement 1B, C</td>
      <td>5.9</td>
    </tr>
    <tr>
      <td>Figure 2—figure supplement 1D, E</td>
      <td>0.84</td>
    </tr>
    <tr>
      <td>Figure 2—figure supplement 1H−J</td>
      <td>1.8</td>
    </tr>
    <tr>
      <td>Figure 5B–D</td>
      <td>1.8</td>
    </tr>
    <tr>
      <td>Figure 6</td>
      <td>1.8</td>
    </tr>
    <tr>
      <td>Figure 6—figure supplement 1</td>
      <td>1.8</td>
    </tr>
    <tr>
      <td>Figure 7A, B</td>
      <td>0.84</td>
    </tr>
    <tr>
      <td>Figure 7—figure supplement 1A−D</td>
      <td>0.84</td>
    </tr>
    <tr>
      <td>Figure 8A–D</td>
      <td>3.9</td>
    </tr>
    <tr>
      <td>Figure 8E–H</td>
      <td>1.8</td>
    </tr>
    <tr>
      <td>Figure 8—figure supplement 1A−C</td>
      <td>1.8</td>
    </tr>
    <tr>
      <td>Figure 8—figure supplement 1D, E</td>
      <td>3.9</td>
    </tr>
    <tr>
      <td>Figure 8—figure supplement 1F, G</td>
      <td>1.8</td>
    </tr>
  </tbody>
</table>

#### Thermal stimulation

To provide heat stimulation, we built thermal control systems with a proportional-integral-derivative temperature controller (ITC-106VH, Inkbird), a solid-state relay for temperature controllers (SSR-25A, Inkbird), a K-Type thermocouple to detect temperature, and a heat panel. The thermal control system was connected to a custom-built incubator designed to maintain a steady temperature inside the behavior rig at 32°C and warm the agar plates. The temperature of the agar plates was monitored by a thermometer gun (62 MAX+ Compact Infrared Thermometer, Fluke) before and after the experiment to verify the appropriate temperature for shibirets1 to be functional. Larvae were sealed in a plastic sieve and pre-heated in a water bath for 10 min to reach 32°C before the test. In order to maintain the temperature above 30°C during the test, a replica of the thermal control system mentioned above was installed in the behavior rig, and the behavior rig was pre-heated overnight before any thermal experiment.

For shibirets1 experiments with heat stimulation, during the first 5 s of the test, larvae were left on the agar plates without LED stimulation. Subsequently, the larvae were optogenetically stimulated with a 624-nm LED for 30 s.

### Behavior analysis

Larvae were tracked in real-time using Multi Worm Tracker (MWT) software (Swierczek et al., 2011, http://sourceforge.net/projects/mwt). The contour, spine, and center of mass for each larva were generated and recorded by MWT as a function of time. From these tracking data, the key parameters of larval motion were computed using Choreography software (a component of the MWT software package which measured the behavioral parameters offline) as described previously (Ohyama et al., 2013; Ohyama et al., 2015). The behavioral parameters generated by the Choreography algorithm include speed, crabspeed (i.e., speed perpendicular to the body axis), body curvature, angle of head bending, body length, body width, area (dorsal view), and bias (i.e., fractional excess of time spent moving in one direction). In this offline process, objects that were tracked for less than 5 seconds or moved less than one body length of a larva were rejected. We refer the reader to the open-source package for further details of the software implementations for the above calculations.

#### Behavior detection

After extracting behavioral parameters from Choreography, we used an unsupervised machine learning behavior classification algorithm to detect and quantify the following behaviors: hunching (Hunch), head-bending (Turn), stopping (Stop), and peristaltic crawling (Crawl) as previously reported (Masson et al., 2020). Escape rolling (Roll) was detected with a classifier developed using the Janelia Automatic Animal Behavior Annotator (JAABA) platform (Kabra et al., 2013; Ohyama et al., 2015). The rolling classifier is available at https://github.com/Jiayi2019/2024_elife (copy archieved at Zhu, 2024a). JAABA transforms the MWT tracking data into a collection of ‘per-frame’ behavioral parameters and regenerates two-dimensional dorsal-view videos of the tracked larvae. Based on such videos, we defined rolling as a rotation around the body while the larva maintains a C-shape, which results in a movement perpendicular to larval body axis (Videos 1 and 2). Using this definition, we trained the algorithm in the JAABA platform by labeling ~10,000 randomly chosen frames as rolling or non-rolling to develop the rolling classifier. If a larva did not curl into a C-shape or move sideways, it was labeled as a ‘non-roller’. Every animal with at least one rolling event longer than 0.2 s in a given period was labeled as a ‘roller’ (i.e., it was assumed to have rolled at least 360 degrees), based on the observation that when the start and end of rolling events were precisely measured, the algorithm could identify rolling events completed in 0.2 s.

The rejection of false positives, especially at the beginning and the end of each rolling bout, enhanced accuracy. The algorithm integrated these training labels and parameters generated with Choreography in a time series, such as speed, crabspeed, and body curvature, to generate a score for rolling detection. Above a certain threshold, the classifier labeled the frame as rolling. This classifier, which has false-negative and -positive rates of 7.4% and 7.8%, respectively (n = 102), was utilized to detect rolling in this paper.

#### Behavior quantification

The outputs of these behavior detection pipelines served as the input to a customized follow-up MATLAB-based analysis. Only the larvae being tracked fully during the stimulation window were selected for analysis. The percentages of animals performing given behaviors as well as their crawling speed in time series at a frame rate of 10 fps were plotted to depict the behavioral responses. To quantify the behavioral phenotype at the population level, the proportions of larvae that performed given behaviors at least once in the first 5 s after the onset of the stimulation were calculated in percentages. A collection of individual-level parameters (e.g., aggregated durations of rolling throughout the stimulation window, starts and ends of the first rolling event after stimulus onset, starts of the first crawling event after the first rolling event in the stimulation window) were generated and analyzed to describe the effects of stimulation on escape behaviors. Specifically, the starts of the first crawling events after the first rolling events were recorded as 30 s by default if larvae rolled but never initiated crawling during the stimulation window. Furthermore, the cumulative plots of the durations of each rolling event were contrasted to describe the event-level differences.

### Larval dissections and immunohistochemistry

Standard immunocytochemical procedures were followed (Patel, 1994). Briefly the CNSs of Drosophila larvae were dissected in phosphate-buffered saline (PBS). After dissection, tissues were fixed with 4% paraformaldehyde for 20 min, washed with PBS three times and then washed with 0.4% Triton X-100 in PBS (PBST) twice. Samples were incubated at room temperature with a blocking solution (5% normal goat serum [NGS]) for 1 hr. Next, the samples were incubated with the primary antibody solutions at 4°C overnight and washed for 15 min six times. Specially, anti-VGAT was incubated for 48 hr to compensate for the permeability. The primary antibodies were diluted at concentrations of 1:3000 for chicken anti-GFP; 1:1000 for rabbit anti-GFP, rabbit anti-GABA, and rabbit anti-dsRed; 1:200 for rabbit anti-VGAT; 1:50 for rat anti-Elav, 1:50 for mouse nc82; and 1:20 for rat anti-DN-Cadherin, mouse anti-Fas2, mouse anti-choline acetyltransferase (ChAT), and rabbit anti-VGLUT in 5% NGS. CNS samples were then incubated with a secondary antibody solution at 4°C overnight and washed 15 min for six times. The secondary antibodies, including anti-chicken Alexa488, anti-rabbit Alexa488, anti-mouse Alexa568, anti-rabbit Alexa568, and anti-rat Alexa568, were all diluted at the concentration of 1:500. These samples were mounted in VECTASHIELD antifade mounting medium and imaged by a Zeiss LSM 710 confocal microscope with a 20×/NA0.8 objective lens (Zeiss) and Zen digital imaging software (Zeiss). For quantifying the expression of VGAT or GABA expression, laser power and gains are consistent between samples. All images were processed using Fiji software (https://imagej.new/Fiji, ImageJ, NIH Bethesda).

### Immunohistochemistry image analysis

Larval CNS image stacks were processed with FIJI. For Figure 5—figure supplement 1C,D, four to six slices along the z dimension were averaged. The neuropil for VGAT or GABA channels at segments A4 to A6 and cell body regions for elav staining were manually selected as regions of interest (ROIs). The mean intensity of VGAT or GABA was measured and normalized by the mean value of elav staining.

### Two-photon calcium imaging assay

The CNSs of third instar larvae were dissected out in cold Baines external physiological saline (135 mM NaCl, 5 mM KCl, 5 mM TES, 36 mM sucrose, 2 mM CaCl2·2H2O, 4 mM MgCl2·6H2O, pH 7.15), and secured on a poly-L-lysine coated cover glass placed in a small Sylgard plate.

Functional calcium imaging experiments were performed on a customized two-photon microscope equipped with a Galvo-Resonant Scanner (Cambridge) controlled by Scanimage software (mbf BIOSCIENCE) using a 40×/0.80NA water immersion objective (LUMPlanFL, Olympus). A Mai Tai, Ti:Sapphire Ultrafast Laser (Spectra Physics) tuned to 925 nm was used for excitation of GCaMP protein. Fluorescence signals were collected with photomultiplier tubes (Hamamatsu) after bandpass filtering. Images were acquired by the Galvo-Resonant Scanner for a single plane of the CNS.

Each larva was stimulated by a 620-nm LED (Thorlabs) through the objective three times with a 30-s interval between periods of stimulation. Every stimulus consisted of a 30-ms pulse given every 100ms for a total of 1 s. Light intensity was measured to be 0.8–1.4 μW/mm2. Images were acquired at a resolution of 512 × 512 pixels with a frame rate of 30 fps. Fluorescence intensities were averaged to 6 fps and processed in FIJI, and analyzed in MATLABwith customized scripts (available at https://github.com/Jiayi2019/2-photon-analysis; copy archieved at Zhu, 2024b). ROIs were determined by the standard deviation of the full recording. ΔF = (F − F0)/F0. F0 is the average of images taken 10 frames (i.e., 1.7 s) before stimulation. F is the mean value of the fluorescence in the ROI averaged every five frames from the start of the 5 s period before stimulation to end of the 15 s period after the onset of each stimulation. For each larva, ΔF is obtained through averaging the ΔF during the three stimulation periods. The peak ΔFs were the maximal values selected from the onset of stimulation to 15 s after stimulus onset.

### Statistics

The probabilities for each response were analyzed by Chi-square tests. For the other parameters, when multiple groups were tested, their normality was examined first. If the normality assumption was rejected, Kruskal–Wallis tests were performed for multiple group variance comparisons, followed by multiple-comparison-corrected Wilcoxon–Mann–Whitney U tests as post hoc pairwise comparisons. If normality was met, analysis of variance was performed for variance comparisons and multiple-comparison-corrected Student’s t-tests were utilized for pairwise comparisons. For two group comparisons, the Wilcoxon–Mann–Whitney U test was conducted if the normality assumption was offended, and the Student’s t-test was applied if normality was met. All analyses were conducted with MATLAB.

### Inclusion and diversity

One or more of authors of this paper self-identifies as a member of the LGBTYQ+ community.
